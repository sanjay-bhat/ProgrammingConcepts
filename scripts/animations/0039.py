#!/usr/bin/env python3
"""#39 Combination Sum: sorted backtracking. Recurse with the same index so a
number can repeat, never go back to earlier ones, and break at the first
candidate bigger than what's still missing.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The input is LeetCode's example 1.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

CANDS, TARGET = [2, 3, 6, 7], 7   # LeetCode example 1


class Row(View):
    """Two views side by side."""

    def __init__(self, left, right, split=0.56):
        self.left, self.right, self.split = left, right, split

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        mid = x0 + (x1 - x0) * self.split
        self.left.draw(p, (x0, y0, mid - 10, y1))
        self.right.draw(p, (mid + 10, y0, x1, y1))
        self.used = max(self.left.used, self.right.used)


def trace(cands, target):
    events, calls = [], []

    def rec(kind, path, result, **kw):
        events.append(dict(kind=kind, path=list(path), result=[list(r) for r in result],
                           calls=[list(c) for c in calls], **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
            candidates.sort()
            result = []

            def backtrack(start: int, path: list[int], remain: int) -> None:
                calls.append([start, list(path), remain])
                if remain == 0:
                    result.append(list(path))
                    rec('record', path, result, start=start, remain=remain)
                    calls.pop()
                    return
                for i in range(start, len(candidates)):
                    if candidates[i] > remain:
                        rec('break', path, result, start=start, i=i, remain=remain)
                        break
                    path.append(candidates[i])
                    rec('choose', path, result, start=start, i=i, remain=remain - candidates[i])
                    backtrack(i, path, remain - candidates[i])
                    path.pop()
                    rec('undo', path, result, start=start, i=i, remain=remain, removed=candidates[i])
                calls.pop()

            backtrack(0, [], target)
            return result

    ans = Solution().combinationSum(list(cands), target)
    events.append(dict(kind='done', path=[], result=ans, calls=[]))
    return events


def nid(path):
    return 'p' + '.'.join(map(str, path))


def layout(events):
    """Tree of choices (plus a red 'too big' leaf for each break), from the whole trace."""
    kids, label = {nid([]): []}, {nid([]): str(TARGET)}
    for e in events:
        if e['kind'] == 'choose':
            n, par = nid(e['path']), nid(e['path'][:-1])
            kids.setdefault(par, []).append(n); kids[n] = []
            label[n] = f"+{e['path'][-1]}"
        if e['kind'] == 'break':
            n = nid(e['path']) + 'x'
            kids[nid(e['path'])].append(n); kids[n] = []
            label[n] = f"{CANDS[e['i']]}>{e['remain']}"
    xs, depth, leaves = {}, {}, [0]

    def walk(n, d):
        depth[n] = d
        if not kids[n]:
            xs[n] = leaves[0]; leaves[0] += 1
        else:
            for c in kids[n]:
                walk(c, d + 1)
            xs[n] = (xs[kids[n][0]] + xs[kids[n][-1]]) / 2
    walk(nid([]), 0)
    md = max(depth.values())
    pos = {n: (xs[n] / (leaves[0] - 1), depth[n] / md) for n in kids}
    edges = [(a, b) for a in kids for b in kids[a]]
    return pos, edges, label


def words(e):
    k = e['kind']
    if k == 'choose':
        v = CANDS[e['i']]
        if e['path'] == [3]:
            return ("Add 3: 4 still missing. From here only 3, 6, 7 may follow, never 2.",
                    "That's why [3,2,2] is never built: [2,2,3] was already found going the other way.", KEY)
        return (f"Add {v}: {e['remain']} still missing. Recurse with the SAME index, so {v} can be used again.",
                "", QUICK * 2.4)
    if k == 'record':
        return (f"Nothing missing: record a copy of {e['path']}.",
                "Built in sorted order only, so [3,2,2] and [2,3,2] are never built.", KEY)
    if k == 'break':
        v = CANDS[e['i']]
        if e['path'] == [2, 2, 2]:
            return (f"{v} is bigger than the {e['remain']} still missing. Stop this whole loop.",
                    "The list is sorted, so every later candidate is even bigger. This break needs the sort.", KEY)
        return (f"{v} > {e['remain']} still missing: break, skip the rest of this loop.", "", QUICK * 2.4)
    if k == 'undo':
        return (f"Pop {e['removed']} (undo): back to {e['path']} with {e['remain']} missing.", "", QUICK * 1.6)
    return ("Done: [[2,2,3],[7]].", "Two answers, each built exactly once; most branches stopped at the first too-big number.", END)


def main():
    args = cli()
    sc = Scene('#39 Combination Sum: sorted order, reuse, early stop',
               f'candidates = {CANDS}, target = {TARGET}. Each node adds one number; red = too big, loop stops.')
    legend = [(ACTIVE, 'current'), (style('good')[1], 'hit the target'), (style('bad')[1], 'too big: break')]
    evs = trace(CANDS, TARGET)
    pos_all, edges_all, label = layout(evs)
    seen = {nid([])}
    for e in evs:
        if e['kind'] == 'choose':
            seen.add(nid(e['path']))
        if e['kind'] == 'break':
            seen.add(nid(e['path']) + 'x')
        pos = {n: pos_all[n] for n in seen}
        edges = [(a, b) for a, b in edges_all if a in seen and b in seen]
        styles = {n: 'bad' for n in seen if n.endswith('x')}
        for r in e['result']:
            styles[nid(r)] = 'good'
        chain = [nid(c[1]) for c in e['calls']]
        for n in chain:
            styles.setdefault(n, 'window')
        cur = nid(e['path']) + ('x' if e['kind'] == 'break' else '')
        rings = [(cur, ACTIVE)] if e['kind'] != 'done' else []
        estyles = {(chain[j], chain[j + 1]): 'active' for j in range(len(chain) - 1)}
        g = GraphView(pos, edges, styles=styles, edge_styles=estyles, rings=rings, height=250,
                      text={n: label[n] for n in pos})
        nst, ptr, win = {}, {}, None
        if 'start' in e:
            win = (e['start'], len(CANDS) - 1)
        if 'i' in e:
            ptr = {'i': e['i']}
            nst[e['i']] = 'bad' if e['kind'] == 'break' else 'active'
        arr = ArrayView(CANDS, styles=nst, pointers=ptr, window=win, title='cands', cell=44)
        pth = ArrayView(e['path'] or [''], styles={j: 'window' for j in range(len(e['path']))}, title='path', cell=44)
        cap, sub, hold = words(e)
        missing = e.get('remain', '-') if e['kind'] != 'done' else 0
        sc.frame([g, Row(arr, pth)], cap, sub, hold,
                 side=MapView([(str(j + 1), str(r), 'good') for j, r in enumerate(e['result'])], 'Found so far',
                              headers=('#', 'combination'), empty='(nothing yet)'),
                 counters={'still missing': missing}, legend=legend)
    finish(sc, 39, "Watch the branch [2,2,2]: 1 is still missing, the next candidate is too big, and the loop "
                   "stops outright, because in a sorted list every later candidate is bigger too.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
