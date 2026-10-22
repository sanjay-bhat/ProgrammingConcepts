#!/usr/bin/env python3
"""#78 Subsets: one working list. Record a copy, then for each later number:
add it, recurse from the next index, remove it again.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The input is LeetCode's example 1.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [1, 2, 3]   # LeetCode example 1


class Row(View):
    """Two views side by side (nums on the left, the working list on the right)."""

    def __init__(self, left, right, split=0.5):
        self.left, self.right, self.split = left, right, split

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        mid = x0 + (x1 - x0) * self.split
        self.left.draw(p, (x0, y0, mid - 10, y1))
        self.right.draw(p, (mid + 10, y0, x1, y1))
        self.used = max(self.left.used, self.right.used)


def trace(nums):
    events, calls = [], []

    def rec(kind, path, result, **kw):
        events.append(dict(kind=kind, path=list(path), result=[list(r) for r in result],
                           calls=[list(c) for c in calls], **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def subsets(self, nums: list[int]) -> list[list[int]]:
            result = []

            def backtrack(start: int, path: list[int]) -> None:
                calls.append([start, list(path)])
                result.append(list(path))
                rec('record', path, result, start=start)
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    rec('choose', path, result, start=start, i=i)
                    backtrack(i + 1, path)
                    path.pop()
                    rec('undo', path, result, start=start, i=i, removed=nums[i])
                calls.pop()
                rec('return', path, result, start=start)

            backtrack(0, [])
            return result

    ans = Solution().subsets(nums)
    events.append(dict(kind='done', path=[], result=ans, calls=[]))
    return events


def key(p):
    return '[' + ','.join(map(str, p)) + ']'


def tree_layout(nums):
    """Positions of the recursion tree (one node per subset), from a full run."""
    kids, order = {(): []}, []

    def walk(p, start):
        order.append(p)
        for i in range(start, len(nums)):
            c = p + (nums[i],)
            kids[p].append(c); kids[c] = []
            walk(c, i + 1)
    walk((), 0)
    xs, leaves = {}, [0]

    def place(p):
        if not kids[p]:
            xs[p] = leaves[0]; leaves[0] += 1
        else:
            for c in kids[p]:
                place(c)
            xs[p] = (xs[kids[p][0]] + xs[kids[p][-1]]) / 2
    place(())
    span = max(1, leaves[0] - 1)
    depth = max(len(p) for p in kids)
    pos = {key(p): (xs[p] / span, len(p) / depth) for p in kids}
    edges = [(key(p), key(c)) for p in kids for c in kids[p]]
    return pos, edges


def words(e):
    k = e['kind']
    p = key(e['path'])
    if k == 'record':
        if not e['path']:
            return ("Record a COPY of the working list: [ ] is a subset too.",
                    "A copy, because this same list keeps changing; storing it directly would leave every entry empty.", KEY)
        if e['path'] == [2]:
            return ("Record a copy: [2]. This call's loop starts at index 2, after the 2.",
                    "So the only number it can add is 3. [2,1] is never built, because [1,2] already was.", KEY)
        return (f"Record a copy: {p}.", "Every state the working list passes through is a subset.", STEP)
    if k == 'choose':
        v = NUMS[e['i']]
        return (f"Add {v}: the working list is now {p}. Recurse from the next index.", "", QUICK * 2.2)
    if k == 'undo':
        if e['removed'] == 3 and e['path'] == [1, 2]:
            return (f"Back from {key(e['path'] + [3])}: pop 3. Working list is {p} again.",
                    "This undo is what lets the loop above try a different number in that slot.", KEY)
        return (f"Pop {e['removed']} (undo): the working list is back to {p}.", "", QUICK * 2)
    if k == 'return':
        return (f"No numbers left to try after {p if e['path'] else '[ ]'}: return.", "", QUICK * 1.5)
    return ("All 8 subsets recorded, each exactly once.",
            "One call per subset, each copying at most n numbers: O(n · 2^n), the size of the answer.", END)


def main():
    args = cli()
    sc = Scene('#78 Subsets: record, add a later number, recurse, undo',
               'Each node is one call and the subset it records. Orange: the chain of calls running now.')
    legend = [(ACTIVE, 'current call'), (style('window')[1], 'waiting for a child call'), (style('good')[1], 'recorded')]
    pos_all, edges_all = tree_layout(NUMS)
    for e in trace(NUMS):
        recorded = {key(r) for r in e['result']}
        pos = {n: xy for n, xy in pos_all.items() if n in recorded or n == key(e['path'])}
        edges = [(a, b) for a, b in edges_all if a in pos and b in pos]
        chain = [key(c[1]) for c in e['calls']]
        styles = {n: 'good' for n in recorded}
        for n in chain:
            styles[n] = 'window'
        cur = key(e['path'])
        if cur not in recorded:
            styles[cur] = 'active'
        estyles = {(chain[j], chain[j + 1]): 'active' for j in range(len(chain) - 1)}
        if chain and cur != chain[-1] and e['kind'] == 'choose':
            estyles[(chain[-1], cur)] = 'active'
        rings = [(cur, ACTIVE)] if e['kind'] != 'done' else []
        g = GraphView(pos, edges, styles=styles, edge_styles=estyles, rings=rings, height=250,
                      text={n: (n if n != '[]' else '[ ]') for n in pos})
        nst, ptr, win = {}, {}, None
        if 'start' in e:
            win = (e['start'], len(NUMS) - 1)
            if 'i' in e:
                ptr = {'i': e['i']}
                nst[e['i']] = 'active'
        arr = ArrayView(NUMS, styles=nst, pointers=ptr, window=win, title='nums', cell=46)
        pth = ArrayView(e['path'] or [''], styles={j: 'window' for j in range(len(e['path']))}, title='path',
                        cell=46)
        stack = [f'backtrack(start={s}, {key(p)})' for s, p in e['calls']]
        cap, sub, hold = words(e)
        side = MapView([(str(j + 1), key(r), 'good') for j, r in enumerate(e['result'])], 'Recorded so far',
                       headers=('#', 'subset'), empty='(nothing yet)')
        sc.frame([g, Row(arr, pth)], cap, sub, hold, side=side,
                 counters={'subsets': len(e['result'])}, legend=legend)
    finish(sc, 78, "Watch the step back from [1,2,3]: popping 3 is the undo that lets the same working list "
                   "become [1,3], and copying it at each record is why the answer isn't eight empty lists.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
