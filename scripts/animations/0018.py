#!/usr/bin/env python3
"""#18 4Sum: sort, fix two numbers (i and j), and sweep two pointers over the
rest, skipping repeated values at every level so no quadruplet comes out twice.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Runs of repeated anchors that the
loops skip are shown as quick frames.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403
from typing import List  # noqa: E402

NUMS, TARGET = [1, 0, -1, 0, -2, 2], 0         # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
# 1) After a match, moving left and right one step each WITHOUT skipping equal
#    values. Both LeetCode samples still pass. Here the second 1 and the second
#    2 rebuild [-2,-1,1,2], so it comes out twice.
HARD_DUP = ([-2, -1, -1, 1, 1, 2, 2], 0)
# 2) A 32-bit sum (int in C#/Java/Go on 32-bit, i32 in Rust). Four 10^9s add up
#    to 4,000,000,000, which wraps to -294,967,296 in 32 bits: exactly this
#    target, so a 32-bit version reports a quadruplet that isn't there.
B = 10 ** 9
HARD_WRAP = ([B, B, B, B], -294967296)


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result


def wrap32(x):
    return (x + 2 ** 31) % 2 ** 32 - 2 ** 31


def variant(nums, target, skip_after_match=True, bits32=False):
    """The same loops with the two first-attempt slips switchable."""
    nums = sorted(nums)
    result, n = [], len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if bits32:
                    total = wrap32(total)
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    if skip_after_match:
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result


def trace(nums, target):
    events = []
    original = list(nums)
    result = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, nums=nums[:], result=[r[:] for r in result], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    rec('given')
    nums.sort()
    n = len(nums)
    rec('sorted')
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            rec('skip_i', i=i)
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                rec('skip_j', i=i, j=j)
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    rec('match', i=i, j=j, left=left, right=right, total=total)
                    l0, r0 = left, right                                 # display only
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    if (left, right) != (l0, r0):
                        rec('skip_lr', i=i, j=j, left=left, right=right, l0=l0, r0=r0)
                    left += 1
                    right -= 1
                elif total < target:
                    rec('less', i=i, j=j, left=left, right=right, total=total)
                    left += 1
                else:
                    rec('more', i=i, j=j, left=left, right=right, total=total)
                    right -= 1
    rec('done')
    assert result == Solution().fourSum(list(original), target)
    return events


def build(nums, target, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#18 4Sum: two anchors, two pointers', subtitle)
    legend = [(style('gold')[1], 'anchors i, j'), (style('window')[1], 'left, right'),
              (style('good')[1], 'match'), (style('muted')[1], 'repeat, skipped')]
    seen = set()
    wide = any(abs(x) >= 10 ** 6 for x in nums)
    show = (lambda x: '1e9' if x == B else ('-1e9' if x == -B else str(x))) if wide else str
    for e in trace(list(nums), target):
        k = e['kind']
        arr = e['nums']
        styles, ptrs = {}, {}
        i, j, L, R = e.get('i'), e.get('j'), e.get('left'), e.get('right')
        if i is not None:
            styles[i] = 'muted' if k == 'skip_i' else 'gold'
            ptrs['i'] = i
        if j is not None:
            styles[j] = 'muted' if k == 'skip_j' else 'gold'
            ptrs['j'] = j
        if L is not None:
            st = 'good' if k == 'match' else 'window'
            styles[L] = styles[R] = st
            ptrs['L'], ptrs['R'] = L, R
            if k == 'skip_lr':
                for x in list(range(e['l0'], L)) + list(range(R + 1, e['r0'] + 1)):
                    styles[x] = 'muted'
        view = ArrayView([show(x) for x in (arr if k != 'given' else nums)], styles, ptrs,
                         title='sorted' if k != 'given' else 'nums')
        lines = []
        if k in ('match', 'less', 'more'):
            parts = [arr[i], arr[j], arr[L], arr[R]]
            lines.append(f"{' + '.join(show(x) for x in parts)} = {e['total']:,}".replace('+ -', '- '))
            rel = {'match': '=', 'less': '<', 'more': '>'}[k]
            lines.append(f"{e['total']:,} {rel} target {target:,}")
        elif k == 'skip_lr':
            lines = [f"L slides {e['l0']} -> {L}, R slides {e['r0']} -> {R}",
                     "then both step once more, past the values just used"]
        text = TextView(lines or [''], size=18)
        chips = ChipsView([(str(r), 'good') for r in e['result']], title='quadruplets found', empty='(none yet)')
        cap, sub, hold = words(e, target, seen, show)
        key = k if k in ('given', 'sorted', 'done') else (k, i, j, L, R)
        if key in notes:
            sub, hold = notes[key], (END if k == 'done' else KEY)
        sc.frame([view, text, chips], cap, sub, hold, counters={'found': len(e['result'])}, legend=legend)
    return sc


def words(e, target, seen, show):
    k = e['kind']
    arr = e['nums']
    if k == 'given':
        return (f"Find every set of four numbers that adds up to {target:,}, with no repeats.",
                "Sort first: it gives the pointers a direction and puts equal values side by side.", STEP)
    if k == 'sorted':
        return ("Sorted. i and j fix two numbers; L and R squeeze the rest.",
                "That's 3Sum's two-pointer sweep with one extra loop around it.", KEY)
    if k == 'done':
        n = len(e['result'])
        return (f"Done: {n} quadruplet{'s' if n != 1 else ''}.",
                "Two anchor loops around a linear sweep: O(n³). At 200 numbers, about 1.3 million sums.", END)
    i, j = e.get('i'), e.get('j')
    if k == 'skip_i':
        return (f"nums[{i}] = {show(arr[i])} was already the first anchor. Skip it.",
                "Same value, same quadruplets. Trying it again would only produce repeats.", QUICK * 3)
    if k == 'skip_j':
        first = 'skip_j' not in seen
        seen.add('skip_j')
        return (f"nums[{j}] = {show(arr[j])} was already the second anchor for this i. Skip it.",
                "j > i + 1, so this is a repeat for the SAME i. Equal to nums[i] itself is fine." if first else "",
                KEY if first else QUICK * 3)
    L, R = e['left'], e['right']
    if k == 'match':
        first = 'match' not in seen
        seen.add('match')
        return (f"{e['total']:,} = target. Record {[arr[i], arr[j], arr[L], arr[R]]}.",
                "Now step BOTH pointers past their current values, or the next pair repeats it." if first else "",
                KEY if first else STEP)
    if k == 'skip_lr':
        return (f"Equal values next to L or R would rebuild the same quadruplet. Slide past them.",
                "This is the skip a first attempt leaves out.", KEY)
    if k == 'less':
        return (f"{e['total']:,} < {target:,}: too small, move L right.", "", QUICK * 2.2)
    return (f"{e['total']:,} > {target:,}: too big, move R left.", "", QUICK * 2.2)


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = [([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
               ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]])]
    for nums, t, want in samples:      # both slips pass both LeetCode samples
        assert Solution().fourSum(list(nums), t) == want
        assert variant(nums, t, skip_after_match=False) == want and variant(nums, t, bits32=True) == want
    assert Solution().fourSum(list(HARD_DUP[0]), HARD_DUP[1]) == [[-2, -1, 1, 2], [-1, -1, 1, 1]]
    assert variant(*HARD_DUP, skip_after_match=False) == [[-2, -1, 1, 2], [-2, -1, 1, 2], [-1, -1, 1, 1]]
    assert Solution().fourSum(list(HARD_WRAP[0]), HARD_WRAP[1]) == []
    assert variant(*HARD_WRAP, bits32=True) == [[B, B, B, B]]
    a = build(*HARD_DUP, f'nums = {HARD_DUP[0]}, target = {HARD_DUP[1]}. Answer [[-2,-1,1,2],[-1,-1,1,1]].', {
        'done': "Two quadruplets. Without the slide after a match, the second 1 and second 2 build "
                "[-2,-1,1,2] again and it's reported twice.",
    })
    b = build(*HARD_WRAP, f'nums = [1e9, 1e9, 1e9, 1e9], target = -294,967,296. Answer []. '
                          'A 32-bit sum finds a match.', {
        ('more', 0, 1, 2, 3): "In 32 bits this sum wraps past 2,147,483,647 and lands on -294,967,296, "
                              "exactly the target. The real sum is far too big.",
        'done': "No quadruplet. In 32 bits, 4,000,000,000 wraps round to -294,967,296, exactly the target, "
                "so a 32-bit sum reports one. The notebook's C#, Go and Rust add in 64 bits.",
    })
    return [
        (a, "Repeated values on both sides: after a match, a first attempt that steps L and R once without "
            "sliding past equal values passes both LeetCode samples, then reports [-2,-1,1,2] twice here."),
        (b, "Four 10^9s and target -294,967,296. Their real sum is 4,000,000,000, but a 32-bit integer wraps "
            "it to exactly -294,967,296 and reports a match. The answer is []."),
    ]


def main():
    args = cli()
    sc = build(NUMS, TARGET, f'nums = {NUMS}, target = {TARGET}. Every unique quadruplet that sums to the target.')
    finish(sc, 18, "Watch j skip the second 0: it's a repeat for the same i, so trying it again could only "
                   "produce quadruplets already found.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
