#!/usr/bin/env python3
"""#81 Search in Rotated Sorted Array II: #33's sorted-half test, plus lo += 1 on a tie.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

# Neither LeetCode sample ever hits a tie, so the GIF uses the smallest input that
# does (the one #33's own notes point at): #33's rule returns false on it.
NUMS, TARGET = [1, 0, 1, 1, 1], 0

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_33 = ([3, 1, 2, 3, 3, 3, 3], 2)      # true; #33 unchanged (nums[lo] <= nums[mid]) says false
HARD_HI = ([3, 3, 3, 3, 1, 2, 3], 2)      # true; dropping hi instead of lo on a tie says false


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def search(self, nums: list[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid]:
                lo += 1
                continue
            if nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False


def search_33(nums, target):
    """First attempt: #33's solution unchanged; a tie counts as 'left half sorted'."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return True
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return False


def drop_hi(nums, target, dropped=None):
    """First attempt: on a tie, shrink from the right (hi -= 1) instead of the left."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return True
        if nums[lo] == nums[mid]:
            if dropped is not None:
                dropped.append(hi)
            hi -= 1
            continue
        if nums[lo] < nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return False


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
            log.append((f'mid {mid} = {nums[mid]}', 'found', 'good'))
            rec('found', lo=lo, hi=hi, mid=mid)
            assert Solution().search(list(nums), target)
            return events
        if nums[lo] == nums[mid]:
            log.append((f'mid {mid} = {nums[mid]}', 'tie: lo += 1', 'bad'))
            rec('tie', lo=lo, hi=hi, mid=mid)
            lo += 1
            continue
        if nums[lo] < nums[mid]:
            if nums[lo] <= target < nums[mid]:
                log.append((f'mid {mid} = {nums[mid]}', 'left sorted, in', None))
                rec('half', lo=lo, hi=hi, mid=mid, side='left', inside=True)
                hi = mid - 1
            else:
                log.append((f'mid {mid} = {nums[mid]}', 'left sorted, out', None))
                rec('half', lo=lo, hi=hi, mid=mid, side='left', inside=False)
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                log.append((f'mid {mid} = {nums[mid]}', 'right sorted, in', None))
                rec('half', lo=lo, hi=hi, mid=mid, side='right', inside=True)
                lo = mid + 1
            else:
                log.append((f'mid {mid} = {nums[mid]}', 'right sorted, out', None))
                rec('half', lo=lo, hi=hi, mid=mid, side='right', inside=False)
                hi = mid - 1
    rec('missing', lo=lo, hi=hi)
    assert not Solution().search(list(nums), target)
    return events


def words(e, nums, t, notes, trap, seen):
    k, lo, hi = e['kind'], e['lo'], e['hi']
    if k == 'start':
        return (f"Is {t} in the array? lo = {lo} and hi = {hi} mark the range still worth searching.",
                notes.get('start', "Each round: check the middle, then decide which half can still hold the target."), KEY)
    mid = e['mid']
    if k == 'mid':
        return (f"Range {lo}..{hi}: the middle is index {mid}, holding {nums[mid]}.",
                "Is it the target?" if nums[mid] == t else f"Not {t}. Which half can still hold it?", QUICK * 2)
    if k == 'found':
        return (f"nums[{mid}] = {nums[mid]} is the target. Return true.",
                notes.get('found', "Every tie only dropped an element that couldn't be the target."), END)
    if k == 'tie':
        head = f"nums[lo] = {nums[lo]} equals the middle {nums[mid]}: a tie."
        if lo == mid:
            return (head, "lo and mid are the same index here, so this just drops the one element left.", STEP)
        if trap == '33' and not seen.get('trap'):
            seen['trap'] = True
            gone = [j for j in range(lo, mid) if nums[j] == t]
            sub = (f"#33's rule would call {nums[lo]}..{nums[mid]} sorted, see {t} isn't in it and jump lo to {mid + 1}"
                   + (f", losing the {t} at index {gone[0]}." if gone else "."))
            if not seen.get('tie'):
                seen['tie'] = True
                return (head + " Can't tell which half is sorted, so drop nums[lo] (it isn't the target).", sub, KEY)
            return (head, sub, KEY)
        if trap == 'hi' and not seen.get('trap'):
            seen['trap'] = True
            return (head, notes['tie'], KEY)
        if not seen.get('tie'):
            seen['tie'] = True
            return (head, "Can't tell which half is sorted. But nums[lo] equals a non-target, so drop it: lo += 1.", KEY)
        return (head, "Same again: drop nums[lo] and look again.", STEP)
    if k == 'half':
        side, inside = e['side'], e['inside']
        a, b = (nums[lo], nums[mid]) if side == 'left' else (nums[mid], nums[hi])
        cmp = f"nums[lo] = {nums[lo]} {'<' if side == 'left' else '>'} nums[mid] = {nums[mid]}"
        where = ('so search the left half' if side == 'left' else 'so search the right half') if inside else \
                ('so it must be in the right half' if side == 'left' else 'so it must be in the left half')
        return (f"{cmp}: the {side} half {a}..{b} is sorted.",
                f"{t} is {'inside' if inside else 'outside'} {a}..{b}, {where}.", STEP)
    return ("The range is empty: lo passed hi. Return false.", notes.get('missing', ''), END)


def build(nums, target, subtitle, notes=None, trap=None):
    notes = notes or {}
    sc = Scene('#81 Search in Rotated Sorted Array II: skip the tie', subtitle)
    legend = [(style('window')[1], 'still in range'), (style('gold')[1], 'middle'),
              (style('bad')[1], 'tie: dropped'), (style('good')[1], 'found'), (style('muted')[1], 'ruled out')]
    seen = {}
    for e in trace(nums, target):
        k, lo, hi, mid = e['kind'], e['lo'], e['hi'], e.get('mid')
        styles = {j: ('window' if lo <= j <= hi else 'muted') for j in range(len(nums))}
        if k == 'half':
            span = range(lo, mid + 1) if e['side'] == 'left' else range(mid, hi + 1)
            for j in span:
                styles[j] = 'gold'
        if mid is not None:
            styles[mid] = {'found': 'good', 'tie': 'gold', 'mid': 'gold'}.get(k, 'active')
        if k == 'tie':
            styles[lo] = 'bad'
        ptrs = {}
        for name, j in (('lo', lo), ('mid', mid), ('hi', hi)):
            if j is not None and 0 <= j < len(nums):
                ptrs[name] = j
        win = (lo, hi) if lo <= hi else None
        views = [ArrayView(nums, styles, pointers=ptrs, window=win, title='nums'),
                 TextView([f'target = {target}'], size=18)]
        cap, sub, hold = words(e, nums, target, notes, trap, seen)
        sc.frame(views, cap, sub, hold,
                 side=MapView(e['log'], 'Rounds', headers=('middle', 'decision'), empty='(none yet)'),
                 counters={'rounds': len(e['log'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    (n1, t1), (n2, t2) = HARD_33, HARD_HI
    assert Solution().search(list(n1), t1) and not search_33(list(n1), t1)
    dropped = []
    assert Solution().search(list(n2), t2) and not drop_hi(list(n2), t2, dropped)
    lost = next(r for r, j in enumerate(dropped, 1) if n2[j] == t2)
    a = build(n1, t1, f'nums = {n1}, target = {t1}. Answer true. #33 unchanged says false.', {
        'start': "The drop (3 then 1) is in the LEFT half, but nums[lo] and the middle are both 3.",
        'found': "Found. #33's solution, run on this input, returns false.",
    }, trap='33')
    b = build(n2, t2, f'nums = {n2}, target = {t2}. Answer true. Dropping hi on a tie says false.', {
        'start': "Lots of 3s on both sides of the drop, and the target sits right next to hi.",
        'tie': (f"A version that drops hi instead throws away nums[{dropped[0]}] = {n2[dropped[0]]} now, "
                f"and the {t2} at index {dropped[lost - 1]} on tie number {lost}. The tie never said anything about hi."),
        'found': "Found, because only nums[lo], which the tie proved isn't the target, was ever dropped.",
    }, trap='hi')
    return [
        (a, f"{n1}, target {t1}: the first middle ties with nums[lo] although the drop is in the left half. "
            "Reusing #33 unchanged calls that half sorted, heads right and returns false. The answer is true."),
        (b, f"{n2}, target {t2}: a first attempt that shrinks from the right on a tie drops the 2 on its second tie "
            "and returns false. Only nums[lo] is proven not to be the target. The answer is true."),
    ]


def main():
    args = cli()
    sc = build(NUMS, TARGET, f'nums = {NUMS}, target = {TARGET}: the smallest input where #33\'s rule fails. '
                             'LeetCode\'s samples never tie.', trap='33')
    finish(sc, 81, "Watch the first round: nums[lo] and the middle are both 1, so neither half can be trusted, "
                   "and the search drops just nums[lo] instead of guessing.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
