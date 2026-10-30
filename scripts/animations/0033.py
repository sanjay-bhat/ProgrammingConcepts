#!/usr/bin/env python3
"""#33 Search in Rotated Sorted Array: find the sorted half, test the target against it.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS, TARGET = [4, 5, 6, 7, 0, 1, 2], 0          # LeetCode example 1


def trace(nums, target):
    events, log = [], []

    def rec(kind, **kw):
        events.append(dict(kind=kind, log=list(log), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    lo, hi = 0, len(nums) - 1
    rec('start', lo=lo, hi=hi)
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        rec('mid', lo=lo, hi=hi, mid=mid)
        if nums[mid] == target:
            rec('found', lo=lo, hi=hi, mid=mid)
            return events
        if nums[lo] <= nums[mid]:
            rec('half', lo=lo, hi=hi, mid=mid, side='left', span=(lo, mid))
            if nums[lo] <= target < nums[mid]:
                log.append((f'{nums[lo]}..{nums[mid]}', True))
                hi = mid - 1
                rec('move', lo=lo, hi=hi, mid=mid, inside=True, span=(lo, mid), dir='left')
            else:
                log.append((f'{nums[lo]}..{nums[mid]}', False))
                lo = mid + 1
                rec('move', lo=lo, hi=hi, mid=mid, inside=False, span=(events[-1]['lo'], mid), dir='right')
        else:
            rec('half', lo=lo, hi=hi, mid=mid, side='right', span=(mid, hi))
            if nums[mid] < target <= nums[hi]:
                log.append((f'{nums[mid]}..{nums[hi]}', True))
                lo = mid + 1
                rec('move', lo=lo, hi=hi, mid=mid, inside=True, span=(mid, hi), dir='right')
            else:
                log.append((f'{nums[mid]}..{nums[hi]}', False))
                hi = mid - 1
                rec('move', lo=lo, hi=hi, mid=mid, inside=False, span=(mid, events[-1]['hi']), dir='left')
    rec('missing', lo=lo, hi=hi)
    return events


def words(e, first_half):
    k, n, t = e['kind'], NUMS, TARGET
    if k == 'start':
        return (f"Find {t}. The array was sorted, then cut and swapped, so it drops once: 7 then 0.",
                f"Plain binary search breaks: {t} is smaller than the middle 7, yet it's on the right.", KEY)
    if k == 'mid':
        return (f"Range {e['lo']}..{e['hi']}: the middle is index {e['mid']}, value {n[e['mid']]}. Not {t}.",
                "", STEP)
    if k == 'half':
        a, b = e['span']
        test = f"nums[lo] = {n[e['lo']]} ≤ nums[mid] = {n[e['mid']]}"
        if e is first_half:
            return (f"{test}, so the left half {n[a]}..{n[b]} has no drop in it: it's sorted.",
                    "The drop can only be on one side, so one half is always plainly sorted.", KEY)
        if e['side'] == 'left':
            return (f"{test}: the left half {n[a]}..{n[b]} is the sorted one.", "", STEP)
        return (f"nums[lo] > nums[mid]: the right half {n[a]}..{n[b]} is the sorted one.", "", STEP)
    if k == 'move':
        a, b = e['span']
        lo_v, hi_v = n[a], n[b]
        if e['inside']:
            return (f"{t} is inside {lo_v}..{hi_v}, so it must be in that half.",
                    f"Search inside it, minus mid (already checked): {'hi' if e['dir'] == 'left' else 'lo'} = {e['hi'] if e['dir'] == 'left' else e['lo']}.", KEY)
        return (f"{t} isn't inside {lo_v}..{hi_v}, so it can only be in the other half.",
                f"No need to know where the drop is. lo = {e['lo']}." if e['dir'] == 'right'
                else f"hi = {e['hi']}.", KEY)
    if k == 'found':
        return (f"The middle is index {e['mid']}, value {n[e['mid']]}. Found it: return {e['mid']}.",
                "Three looks for seven elements; 5,000 elements take about 13.", END)
    return ("lo passed hi: the target isn't here. Return -1.", "", END)


def main():
    args = cli()
    events = trace(NUMS, TARGET)
    first_half = next(e for e in events if e['kind'] == 'half')
    drop = NUMS.index(min(NUMS))
    sc = Scene('#33 Search in Rotated Sorted Array',
               f'nums = {NUMS}, target = {TARGET}. One half is always sorted: test the target against it.')
    legend = [(style('gold')[1], 'before the drop'), (style('window')[1], 'after the drop'),
              (style('good')[1], 'the sorted half'), (style('muted')[1], 'ruled out'), (ACTIVE, 'mid')]
    for e in events:
        lo, hi, mid = e['lo'], e['hi'], e.get('mid')
        styles = {}
        for i in range(len(NUMS)):
            styles[i] = 'muted' if not (lo <= i <= hi) else ('gold' if i < drop else 'window')
        if e['kind'] == 'half':
            a, b = e['span']
            for i in range(a, b + 1):
                styles[i] = 'good'
        if e['kind'] == 'move':
            a, b = e['span']
            for i in range(a, b + 1):
                if lo <= i <= hi:
                    styles[i] = 'good'
        if mid is not None and e['kind'] in ('mid', 'half'):
            styles[mid] = 'active'
        if e['kind'] == 'found':
            styles[mid] = 'good'
        ptrs = {'lo': lo, 'hi': hi}
        if e['kind'] in ('mid', 'half'):
            ptrs = {'lo': lo, 'mid': mid, 'hi': hi}
        if e['kind'] == 'found':
            ptrs = {'found': mid}
        view = ArrayView(NUMS, styles, pointers=ptrs, window=(lo, hi), title='nums', cell=62)
        rows = [(f'sorted {span}', f'{TARGET} {"inside: go there" if ok else "outside: other half"}',
                 'good' if ok else 'muted') for span, ok in e['log']]
        cap, sub, hold = words(e, first_half)
        sc.frame(view, cap, sub, hold,
                 side=MapView(rows, 'Sorted half tests', headers=('half', 'target?'), empty='(none yet)'),
                 counters={'target': TARGET}, legend=legend)
    finish(sc, 33, "Watch the first step: 4 ≤ 7 proves the left half is sorted, 0 isn't between 4 and 7, "
                   "so the search goes right without ever locating the drop.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
