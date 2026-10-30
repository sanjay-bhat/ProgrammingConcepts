#!/usr/bin/env python3
"""#153 Find Minimum in Rotated Sorted Array: compare the middle with the right end.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [4, 5, 6, 7, 0, 1, 2]          # LeetCode example 2


def trace(nums):
    events, log = [], []

    def rec(kind, **kw):
        events.append(dict(kind=kind, log=list(log), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    lo, hi = 0, len(nums) - 1
    rec('start', lo=lo, hi=hi, mid=None)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        rec('compare', lo=lo, hi=hi, mid=mid)
        if nums[mid] > nums[hi]:
            log.append((mid, hi, True))
            lo = mid + 1
            rec('right', lo=lo, hi=hi, mid=mid, was=log[-1])
        else:
            log.append((mid, hi, False))
            hi = mid
            rec('left', lo=lo, hi=hi, mid=mid, was=log[-1])
    rec('done', lo=lo, hi=hi, mid=None)
    return events


def words(e):
    k, n = e['kind'], NUMS
    if k == 'start':
        return ("Two sorted runs: 4 5 6 7 (high), then 0 1 2 (low).",
                "The minimum is where the low run starts. Every step asks: which run is the middle in?", KEY)
    if k == 'compare':
        m, h = e['mid'], e['hi']
        return (f"Middle is index {m} ({n[m]}). Compare it with the right end, index {h} ({n[h]}).",
                "The right end is always in the low run, so it's the reference point.", STEP)
    if k == 'right':
        m, h = e['was'][0], e['was'][1]
        return (f"{n[m]} > {n[h]}: the middle is in the high run, so the drop is to its right.",
                f"{n[m]} can't be the minimum, so step past it: lo = {e['lo']}.", KEY)
    if k == 'left':
        m, h = e['was'][0], e['was'][1]
        if n[m] == min(n):
            return (f"{n[m]} ≤ {n[h]}: low run again, and this time the middle IS the minimum.",
                    f"That's why it's hi = mid, not mid - 1: mid - 1 would throw the {n[m]} away.", KEY)
        return (f"{n[m]} ≤ {n[h]}: the middle is in the low run.",
                f"The minimum is {n[m]} or something left of it. Keep mid: hi = {e['hi']}.", KEY)
    return (f"lo and hi meet at index {e['lo']}. The minimum is {n[e['lo']]}.",
            "Three comparisons for seven elements; 5,000 elements would take about 13.", END)


def main():
    args = cli()
    low_start = NUMS.index(min(NUMS))
    sc = Scene('#153 Find Minimum in Rotated Sorted Array',
               f'nums = {NUMS}. Binary search: compare nums[mid] with nums[hi].')
    legend = [(style('gold')[1], 'high run'), (style('window')[1], 'low run, still in range'),
              (style('muted')[1], 'ruled out'), (ACTIVE, 'mid')]
    for e in trace(NUMS):
        lo, hi, mid = e['lo'], e['hi'], e['mid']
        styles = {}
        for i in range(len(NUMS)):
            if not (lo <= i <= hi):
                styles[i] = 'muted'
            else:
                styles[i] = 'gold' if i < low_start else 'window'
        if e['kind'] == 'compare':
            styles[mid] = 'active'
            styles[hi] = 'land' if hi != mid else 'active'
        if e['kind'] == 'done':
            styles[lo] = 'good'
        ptrs = {'lo': lo, 'hi': hi} if e['kind'] != 'done' else {'min': lo}
        if e['kind'] == 'compare':
            ptrs = {'lo': lo, 'mid': mid, 'hi': hi}
        view = ArrayView(NUMS, styles, pointers=ptrs, window=(lo, hi), title='nums', cell=62)
        rows = [(f'nums[{m}] vs nums[{h}]', f'{NUMS[m]} {">" if r else "≤"} {NUMS[h]}  ' +
                 ('go right' if r else 'keep mid'), 'gold' if r else 'window')
                for m, h, r in e['log']]
        cap, sub, hold = words(e)
        sc.frame(view, cap, sub, hold,
                 side=MapView(rows, 'Comparisons', headers=('test', 'result'), empty='(none yet)'),
                 counters={'range': f'{lo}..{hi}'}, legend=legend)
    finish(sc, 153, "Watch the last comparison: the middle lands on the 0 itself, and hi = mid "
                    "(not mid - 1) is what keeps it in range.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
