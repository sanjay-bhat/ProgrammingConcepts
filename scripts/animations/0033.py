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

# Hard examples (interactive page only). Notes are keyed by event number and
# replace that frame's second caption line (held as a KEY moment).
# 1) The drop is at the very end and the target is the last element. The range
#    shrinks to two elements where lo == mid, and the strict test
#    nums[lo] < nums[mid] calls that one-element half unsorted, so the search
#    goes left and returns -1. Answer 8.
HARD1 = ([2, 3, 4, 5, 6, 7, 8, 9, 1], 1)
HARD1_NOTES = {
    0: "The drop is right at the end, between 9 and 1, and 1 is what we're after.",
    8: "lo and mid are both index 7, so this 'half' is just the 9, and 9 ≤ 9 is true.",
    9: "With a strict <, 9 < 9 fails, the 'right half' 9..1 gets tested, 1 isn't in it, and the answer is -1.",
    'found': "Found at index 8. The strict-< version returned -1 on this input.",
}
# 2) The target equals the right end of the sorted half. The test must be
#    inclusive at that end (target <= nums[hi]); a strict < calls 6 "outside",
#    searches the wrong half and returns -1. Answer 8.
HARD2 = ([7, 8, 9, 1, 2, 3, 4, 5, 6], 6)
HARD2_NOTES = {
    0: "The target is the last element, so it's the right end of any sorted right half.",
    3: "6 equals nums[hi]. Only <= at that end counts it inside; a strict < sends the search left and returns -1.",
    'found': "Found at index 8. The bound at mid is strict (mid was checked), the bound at hi is inclusive.",
}


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


def words(e, first_half, nums=NUMS, target=TARGET):
    k, n, t = e['kind'], nums, target
    if k == 'start' and nums is not NUMS:
        d = nums.index(min(nums))
        return (f"Find {t}. The array was sorted, then cut and swapped, so it drops once: {n[d - 1]} then {n[d]}.",
                "", KEY)
    if k == 'start':
        return (f"Find {t}. The array was sorted, then cut and swapped, so it drops once: 7 then 0.",
                f"Plain binary search breaks: {t} is smaller than the middle 7, yet it's on the right.", KEY)
    if k == 'mid' and n[e['mid']] == t:
        return (f"Range {e['lo']}..{e['hi']}: the middle is index {e['mid']}, value {n[e['mid']]}. That's the target.",
                "", STEP)
    if k == 'mid':
        return (f"Range {e['lo']}..{e['hi']}: the middle is index {e['mid']}, value {n[e['mid']]}. Not {t}.",
                "", STEP)
    if k == 'half':
        a, b = e['span']
        test = f"nums[lo] = {n[e['lo']]} ≤ nums[mid] = {n[e['mid']]}"
        if e is first_half and e['side'] == 'right':
            return (f"nums[lo] = {n[e['lo']]} > nums[mid] = {n[e['mid']]}, so the drop is on the left and the "
                    f"right half {n[a]}..{n[b]} is sorted.",
                    "The drop can only be on one side, so one half is always plainly sorted.", KEY)
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


def build(nums, target, subtitle, notes=None):
    events = trace(nums, target)
    first_half = next(e for e in events if e['kind'] == 'half')
    drop = nums.index(min(nums))
    sc = Scene('#33 Search in Rotated Sorted Array', subtitle)
    legend = [(style('gold')[1], 'before the drop'), (style('window')[1], 'after the drop'),
              (style('good')[1], 'the sorted half'), (style('muted')[1], 'ruled out'), (ACTIVE, 'mid')]
    for idx, e in enumerate(events):
        lo, hi, mid = e['lo'], e['hi'], e.get('mid')
        styles = {}
        for i in range(len(nums)):
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
        view = ArrayView(nums, styles, pointers=ptrs, window=(lo, hi), title='nums', cell=62)
        rows = [(f'sorted {span}', f'{target} {"inside: go there" if ok else "outside: other half"}',
                 'good' if ok else 'muted') for span, ok in e['log']]
        cap, sub, hold = words(e, first_half, nums, target)
        if notes:
            key = 'found' if e['kind'] == 'found' and 'found' in notes else idx
            if key in notes:
                sub, hold = notes[key], (END if e['kind'] in ('found', 'missing') else KEY)
        sc.frame(view, cap, sub, hold,
                 side=MapView(rows, 'Sorted half tests', headers=('half', 'target?'), empty='(none yet)'),
                 counters={'target': target}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(*HARD1, f'nums = {HARD1[0]}, target = {HARD1[1]}. The drop is at the very end.', HARD1_NOTES)
    sc2 = build(*HARD2, f'nums = {HARD2[0]}, target = {HARD2[1]}. The target is the last element.', HARD2_NOTES)
    return [(sc1, "Target 1 at the very end: the range shrinks to two elements with lo == mid, and a strict "
                  "nums[lo] < nums[mid] sends the search the wrong way and returns -1. Answer: 8."),
            (sc2, "Target 6 is the right end of the sorted half. Test it with a strict < nums[hi] and 6 looks "
                  "outside, so the search goes left and returns -1. Answer: 8.")]


def main():
    args = cli()
    sc = build(NUMS, TARGET,
               f'nums = {NUMS}, target = {TARGET}. One half is always sorted: test the target against it.')
    finish(sc, 33, "Watch the first step: 4 ≤ 7 proves the left half is sorted, 0 isn't between 4 and 7, "
                   "so the search goes right without ever locating the drop.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
