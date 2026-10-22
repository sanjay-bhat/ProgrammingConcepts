#!/usr/bin/env python3
"""#46 Permutations: fill slots left to right inside the array. Swap each free
number into the current slot, recurse on the next slot, swap back.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The input is LeetCode's example 1.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [1, 2, 3]   # LeetCode example 1


def trace(nums_in):
    nums = list(nums_in)
    events, chain = [], []    # chain: the numbers placed in slots 0..start-1, i.e. the tree path

    def rec(kind, result, **kw):
        events.append(dict(kind=kind, nums=list(nums), result=[list(r) for r in result], chain=list(chain), **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def permute(self, nums: list[int]) -> list[list[int]]:
            result = []

            def backtrack(start: int) -> None:
                if start == len(nums):
                    result.append(list(nums))
                    rec('record', result, start=start)
                    return
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    chain.append(nums[start])
                    rec('swap_in', result, start=start, i=i)
                    backtrack(start + 1)
                    chain.pop()
                    nums[start], nums[i] = nums[i], nums[start]
                    rec('swap_back', result, start=start, i=i)

            backtrack(0)
            return result

    ans = Solution().permute(nums)
    events.append(dict(kind='done', nums=list(nums), result=ans, chain=[]))
    return events


def nid(chain):
    return 'n' + '.'.join(map(str, chain))


def layout(events):
    kids = {nid([]): []}
    for e in events:
        if e['kind'] == 'swap_in':
            n, par = nid(e['chain']), nid(e['chain'][:-1])
            if n not in kids:
                kids[par].append(n); kids[n] = []
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
    return ({n: (xs[n] / (leaves[0] - 1), depth[n] / md) for n in kids},
            [(a, b) for a in kids for b in kids[a]])


def words(e):
    k = e['kind']
    a = e['nums']
    if k == 'swap_in':
        s, i = e['start'], e['i']
        if s == i:
            nxt = f"Now decide slot {s + 1}." if s + 1 < len(a) else "That was the last slot."
            return (f"Slot {s}: keep {a[s]} where it is (swap with itself). {nxt}",
                    f"Slots before {s + 1} are decided; the rest are the numbers still free.", STEP if s == 0 else QUICK * 2.2)
        return (f"Slot {s}: swap {a[s]} in from position {i}. Array is now {a}.", "", STEP if s == 0 else QUICK * 2.2)
    if k == 'record':
        first = len(e['result']) == 1
        return (f"Every slot decided: record a COPY of {a}.",
                "A copy, because this same array keeps being swapped." if first else "", KEY if first else STEP)
    if k == 'swap_back':
        s, i = e['start'], e['i']
        if s == 0 and i == 1:
            return (f"Swap back: the array is {a} again, exactly as before choosing 2.",
                    "This undo is what lets the next choice (3 into slot 0) start from the original order.", KEY)
        if s == i:
            return (f"Undo slot {s} (nothing moved): array is {a}.", "", QUICK * 1.6)
        return (f"Swap back: undo the choice for slot {s}. Array is {a} again.", "", QUICK * 2)
    return ("All 6 permutations recorded, and the array is back to [1, 2, 3].",
            "Note [3,2,1] came before [3,1,2]: swapping doesn't give sorted order, and nothing asked for it.", END)


def main():
    args = cli()
    sc = Scene('#46 Permutations: swap into place, recurse, swap back',
               'Tree: the number placed in each slot. Array: decided slots (green) | free numbers.')
    legend = [(ACTIVE, 'slot being decided'), (style('good')[1], 'decided'), (style('window')[1], 'still free')]
    evs = trace(NUMS)
    pos_all, edges_all = layout(evs)
    seen = {nid([])}
    for e in evs:
        if e['kind'] == 'swap_in':
            seen.add(nid(e['chain']))
        recorded = {nid(r) for r in e['result']}
        pos = {n: pos_all[n] for n in seen}
        edges = [(x, y) for x, y in edges_all if x in seen and y in seen]
        path = [nid(e['chain'][:j]) for j in range(len(e['chain']) + 1)]
        styles = {n: 'good' for n in recorded}
        for n in path:
            styles.setdefault(n, 'window')
        estyles = {(path[j], path[j + 1]): 'active' for j in range(len(path) - 1)}
        rings = [(path[-1], ACTIVE)] if e['kind'] != 'done' else []
        text = {n: (n[1:].split('.')[-1] if n != 'n' else 'start') for n in pos}
        g = GraphView(pos, edges, styles=styles, edge_styles=estyles, rings=rings, text=text, height=240)
        st, ptr = {}, {}
        if 'start' in e and e['kind'] != 'record':
            s = e['start']
            decided = s + (1 if e['kind'] == 'swap_in' else 0)
            for j in range(len(NUMS)):
                st[j] = 'good' if j < decided else 'window'
            st[s] = 'active'
            ptr = {'start': s, 'i': e['i']}
        elif e['kind'] in ('record', 'done'):
            st = {j: 'good' for j in range(len(NUMS))}
        arr = ArrayView(e['nums'], styles=st, pointers=ptr, title='nums', cell=58)
        cap, sub, hold = words(e)
        sc.frame([g, arr], cap, sub, hold,
                 side=MapView([(str(j + 1), str(r), 'good') for j, r in enumerate(e['result'])], 'Recorded so far',
                              headers=('#', 'permutation'), empty='(nothing yet)'),
                 counters={'found': len(e['result'])}, legend=legend)
    finish(sc, 46, "Watch the swap back after the [2, ...] branch: the array returns to [1, 2, 3] so the next "
                   "choice starts from the original order. Without that undo, some orderings repeat and others never appear.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
