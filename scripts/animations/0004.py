#!/usr/bin/env python3
"""#4 Median of Two Sorted Arrays: binary search the cut in the shorter list.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The example is small but moves the
cut both ways (too many from nums1, then too few) before it lands.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS1, NUMS2 = [1, 15, 25, 27], [4, 8, 9, 26]     # merged: 1 4 8 9 | 15 25 26 27


def trace(a, b):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def findMedianSortedArrays(nums1, nums2):
        if len(nums1) > len(nums2):
            return findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        rec('start', A=nums1, B=nums2, low=low, high=high, half=(m + n + 1) // 2)

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (m + n + 1) // 2 - partition_x

            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]

            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]
            st = dict(A=nums1, B=nums2, low=low, high=high, px=partition_x, py=partition_y,
                      L1=max_left_x, R1=min_right_x, L2=max_left_y, R2=min_right_y)
            rec('cut', **st)

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (m + n) % 2 == 1:
                    ans = float(max(max_left_x, max_left_y))
                else:
                    ans = (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                rec('valid', **st, ans=ans, even=(m + n) % 2 == 0)
                return ans
            elif max_left_x > min_right_y:
                high = partition_x - 1
                rec('left', **dict(st, low=low, high=high))
            else:
                low = partition_x + 1
                rec('right', **dict(st, low=low, high=high))
        return 0.0

    findMedianSortedArrays(a, b)
    return events


def fv(v):
    return '-∞' if v == float('-inf') else ('+∞' if v == float('inf') else str(v))


def words(e, seen):
    k = e['kind']
    if k == 'start':
        return (f"Total 8, so the left half needs {e['half']} elements. Don't merge: just decide how many come from nums1.",
                "Pick that number (the cut in nums1) and nums2's cut is forced: 4 minus it.", KEY)
    if k == 'cut':
        first = 'cut' not in seen
        seen.add('cut')
        return (f"Try {e['px']} from nums1, so {e['py']} from nums2. Only the 4 values beside the cuts matter.",
                "Each list is sorted, so these are the only places the left could beat the right." if first else
                ("An empty side gets -∞ or +∞, so its check always passes." if e['px'] == 0 else ""), KEY if first or e['px'] == 0 else STEP)
    if k == 'left':
        return (f"{fv(e['L1'])} on the left beats {fv(e['R2'])} on the right: too many from nums1.",
                f"Move nums1's cut left. Its possible cuts are now {e['low']}..{e['high']}.", KEY)
    if k == 'right':
        return (f"{fv(e['L2'])} on the left beats {fv(e['R1'])} on the right: too few from nums1.",
                f"Move nums1's cut right. Its possible cuts are now {e['low']}..{e['high']}.", KEY)
    lm, rm = max(e['L1'], e['L2']), min(e['R1'], e['R2'])
    return (f"{fv(e['L1'])} ≤ {fv(e['R2'])} and {fv(e['L2'])} ≤ {fv(e['R1'])}: valid. Median = ({lm} + {rm}) / 2 = {e['ans']:g}.",
            "Even total: average the biggest left value and the smallest right value.", END)


def main():
    args = cli()
    sc = Scene('#4 Median of Two Sorted Arrays: cut, don\'t merge',
               f'nums1 = {NUMS1}, nums2 = {NUMS2}. Binary search how many of nums1 go in the left half.')
    legend = [(style('window')[1], 'left half'), (style('gold')[1], 'right half'),
              (ACTIVE, 'the cut'), (style('bad')[1], 'the check that failed')]
    seen = set()
    for e in trace(NUMS1, NUMS2):
        A, B = e['A'], e['B']
        cutx = [] if e['kind'] == 'start' else [e['px']]
        cuty = [] if e['kind'] == 'start' else [e['py']]
        sa = {i: ('window' if cutx and i < e['px'] else 'gold') if cutx else 'plain' for i in range(len(A))}
        sb = {i: ('window' if cuty and i < e['py'] else 'gold') if cuty else 'plain' for i in range(len(B))}
        if e['kind'] == 'left':
            sa[e['px'] - 1] = 'bad'; sb[e['py']] = 'bad'
        if e['kind'] == 'right':
            sb[e['py'] - 1] = 'bad'; sa[e['px']] = 'bad'
        if e['kind'] == 'valid':
            for arr, s, c in ((A, sa, e['px']), (B, sb, e['py'])):
                for i in range(len(arr)):
                    s[i] = 'good' if i < c else 'gold'
        lo, hi = e['low'], e['high']
        cands = ArrayView(list(range(len(A) + 1)),
                          {i: ('active' if 'px' in e and i == e['px'] and e['kind'] == 'cut' else
                               'window' if lo <= i <= hi else 'muted') for i in range(len(A) + 1)},
                          pointers={'low': lo, 'high': hi} if lo <= hi else {}, window=(lo, hi),
                          title='cut1 ', indices=False, cell=44)
        views = [ArrayView(A, sa, title='nums1', cuts=cutx, cell=58),
                 ArrayView(B, sb, title='nums2', cuts=cuty, cell=58), cands]
        rows = []
        if 'L1' in e:
            ok1, ok2 = e['L1'] <= e['R2'], e['L2'] <= e['R1']
            rows = [('nums1 left max', fv(e['L1'])), ('nums1 right min', fv(e['R1'])),
                    ('nums2 left max', fv(e['L2'])), ('nums2 right min', fv(e['R2'])),
                    (f"{fv(e['L1'])} ≤ {fv(e['R2'])}?", 'yes' if ok1 else 'no', 'good' if ok1 else 'bad'),
                    (f"{fv(e['L2'])} ≤ {fv(e['R1'])}?", 'yes' if ok2 else 'no', 'good' if ok2 else 'bad')]
        cap, sub, hold = words(e, seen)
        counters = {'cut1': e.get('px', '-'), 'cut2': e.get('py', '-')}
        sc.frame(views, cap, sub, hold,
                 side=MapView(rows, 'Values at the cuts', headers=('value', ''), empty='(no cut yet)'),
                 counters=counters, legend=legend)
    finish(sc, 4, "Watch the checks beside the cuts: each failed one says which way to move the cut in "
                  "nums1, so the search never has to merge anything.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
