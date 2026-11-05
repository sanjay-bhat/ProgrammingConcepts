#!/usr/bin/env python3
"""#31 Next Permutation: find the rightmost place the numbers still go up,
swap that number with the smallest bigger one to its right, then reverse the
tail so it's as small as possible.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [2, 3, 1]              # from the problem statement: next is [3, 1, 2]

# Hard examples (interactive page only), each breaking a plausible first attempt.
# 1) Swapping the pivot with its right-hand NEIGHBOUR instead of the smallest
#    bigger number to its right. All three LeetCode samples pass ([1,2,3],
#    [3,2,1], [1,1,5]): there the neighbour happens to be the right one. Here it
#    swaps 4 with 7 instead of 5. Answer [1,5,8,5,1,3,4,6,7].
HARD_SWAP = [1, 5, 8, 4, 7, 6, 5, 3, 1]
# 2) Finding the pivot with nums[i] > nums[i+1] instead of >=. All three
#    samples pass. With a repeat at the end, 3 = 3 is taken as a pivot; no number
#    to its right is bigger, so j runs off the front and crashes. Answer [3,2,3].
HARD_DUP = [2, 3, 3]


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])


def variant(nums, neighbour=False, strict=False, no_reverse=False):
    """The same three steps with the first-attempt slips switchable."""
    nums = list(nums)
    n = len(nums)
    i = n - 2
    while i >= 0 and (nums[i] > nums[i + 1] if strict else nums[i] >= nums[i + 1]):
        i -= 1
    if i >= 0:
        j = i + 1 if neighbour else n - 1
        while not neighbour and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        if no_reverse:
            return nums
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums


def trace(nums):
    events = []
    original = list(nums)

    def rec(kind, **kw):
        events.append(dict(kind=kind, nums=nums[:], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    n = len(nums)
    i = n - 2
    rec('start')
    while i >= 0 and nums[i] >= nums[i + 1]:
        rec('scan', i=i)
        i -= 1
    if i >= 0:
        rec('pivot', i=i)
        j = n - 1
        while nums[j] <= nums[i]:
            rec('jscan', i=i, j=j)
            j -= 1
        rec('jfound', i=i, j=j)
        nums[i], nums[j] = nums[j], nums[i]
        rec('swap', i=i, j=j)
    else:
        rec('nopivot', i=i)
    before = nums[i + 1:]                                   # display only
    nums[i + 1:] = reversed(nums[i + 1:])
    rec('reverse', i=i, before=before)
    want = list(original)
    Solution().nextPermutation(want)
    assert nums == want
    return events


def build(nums, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#31 Next Permutation: pivot, swap, reverse', subtitle)
    legend = [(style('window')[1], 'tail: never goes up'), (style('gold')[1], 'pivot i'),
              (ACTIVE, 'j: candidate to swap in'), (style('good')[1], 'changed')]
    seen = set()
    n = len(nums)
    for idx, e in enumerate(trace(list(nums))):
        k, arr = e['kind'], e['nums']
        i, j = e.get('i'), e.get('j')
        styles, ptrs, window, cuts = {}, {}, None, []
        if k == 'scan':
            for x in range(i + 1, n):
                styles[x] = 'window'
            styles[i] = 'window'
            ptrs = {'i': i}
        elif k in ('pivot', 'jscan', 'jfound'):
            for x in range(i + 1, n):
                styles[x] = 'window'
            styles[i] = 'gold'
            ptrs = {'i': i}
            if j is not None:
                styles[j] = 'active' if k == 'jfound' else 'muted'
                ptrs['j'] = j
            window = (i + 1, n - 1)
            cuts = [i + 1]
        elif k == 'swap':
            for x in range(i + 1, n):
                styles[x] = 'window'
            styles[i] = styles[j] = 'good'
            ptrs = {'i': i, 'j': j}
            window = (i + 1, n - 1)
            cuts = [i + 1]
        elif k in ('nopivot',):
            for x in range(n):
                styles[x] = 'window'
        elif k == 'reverse':
            for x in range(i + 1, n):
                styles[x] = 'good'
            if i >= 0:
                styles[i] = 'good'
            window = (i + 1, n - 1) if i + 1 <= n - 1 else None
            cuts = [i + 1] if i >= 0 else []
        view = ArrayView(arr, styles, ptrs, window=window, title='nums', cuts=cuts)
        lines = []
        if k == 'reverse':
            lines = [f"tail {e['before']} reversed -> {arr[i + 1:]}", f"result: {arr}"]
        elif k in ('jscan', 'jfound') or k == 'swap':
            lines = [f"pivot nums[{i}] = {arr[i] if k != 'swap' else arr[j]}"]
        text = TextView(lines or [''], size=18)
        rows = [('i (pivot)', '-' if i is None else str(i)), ('j', '-' if j is None else str(j)),
                ('original', str(nums))]
        cap, sub, hold = words(e, n, seen)
        key = (k, i, j) if k not in ('start', 'reverse', 'nopivot') else k
        if key in notes:
            sub, hold = notes[key], (END if k == 'reverse' else KEY)
        sc.frame([view, text], cap, sub, hold, side=MapView(rows, 'State', headers=('', '')), legend=legend)
    return sc


def words(e, n, seen):
    k, arr = e['kind'], e['nums']
    i, j = e.get('i'), e.get('j')
    first = k not in seen
    seen.add(k)
    if k == 'start':
        return ("Find the next arrangement in dictionary order, in place.",
                "Change as little as possible, as far to the right as possible.", STEP)
    if k == 'scan':
        return (f"nums[{i}] = {arr[i]} ≥ nums[{i + 1}] = {arr[i + 1]}: still going down from the left. Move i left.",
                "A tail that never goes up is already its LARGEST order. Nothing in it can be bumped." if first else "",
                KEY if first else QUICK * 2.5)
    if k == 'pivot':
        return (f"nums[{i}] = {arr[i]} < nums[{i + 1}] = {arr[i + 1]}: the pivot. This is the number to bump up.",
                "It's the rightmost place the numbers still go up, so changing it changes as little as possible.", KEY)
    if k == 'jscan':
        return (f"nums[{j}] = {arr[j]} ≤ {arr[i]}: too small to swap in. Move j left.", "", QUICK * 2.5)
    if k == 'jfound':
        return (f"nums[{j}] = {arr[j]} > {arr[i]}: the smallest number in the tail that's bigger than the pivot.",
                "Scanning from the right finds it first, because the tail never goes up.", KEY)
    if k == 'swap':
        return (f"Swap: nums[{i}] = {arr[i]}, nums[{j}] = {arr[j]}.",
                "The tail still never goes up, so it's still in its largest order.", KEY)
    if k == 'nopivot':
        return ("No pivot: the whole array never goes up. It's the largest arrangement.",
                "Wrap around to the smallest: reverse everything.", KEY)
    return (f"Reverse the tail: {e['before']} becomes {arr[i + 1:]}. Answer {arr}.",
            "Reversing a never-going-up tail sorts it smallest first. Each step is one pass: O(n) time.", END)


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = [([1, 2, 3], [1, 3, 2]), ([3, 2, 1], [1, 2, 3]), ([1, 1, 5], [1, 5, 1])]
    for nums, want in samples:      # both first attempts pass all three samples
        got = list(nums)
        Solution().nextPermutation(got)
        assert got == want == variant(nums, neighbour=True) == variant(nums, strict=True)
    got = list(HARD_SWAP)
    Solution().nextPermutation(got)
    assert got == [1, 5, 8, 5, 1, 3, 4, 6, 7] and variant(HARD_SWAP, neighbour=True) == [1, 5, 8, 7, 1, 3, 5, 6, 4]
    got = list(HARD_DUP)
    Solution().nextPermutation(got)
    assert got == [3, 2, 3]
    try:
        variant(HARD_DUP, strict=True)
        raise AssertionError('expected the strict pivot test to crash')
    except IndexError:
        pass
    a = build(HARD_SWAP, f'nums = {HARD_SWAP}. Answer [1,5,8,5,1,3,4,6,7].', {
        ('jfound', 3, 6): "Swapping with the neighbour (7) would bump 4 up too far. 5 is the smallest number in "
                          "the tail that's bigger than 4.",
        'reverse': "Swapping with the neighbour gives [1,5,8,7,1,3,5,6,4]: a later arrangement, but not the NEXT one.",
    })
    b = build(HARD_DUP, f'nums = {HARD_DUP}. Answer [3,2,3]. A strict > in the pivot scan crashes.', {
        ('scan', 1, None): "3 ≥ 3 counts as 'not going up'. With a strict >, i would stop here, and no number to the "
                           "right is bigger than 3, so j would run off the front of the array.",
    })
    return [
        (a, "The pivot is 4. Swapping it with its neighbour (7) passes all three LeetCode samples, then returns "
            "[1,5,8,7,1,3,5,6,4]. The right partner is 5, the smallest bigger number in the tail: [1,5,8,5,1,3,4,6,7]."),
        (b, "A repeat at the end: 3 = 3 is not a step up. Testing nums[i] > nums[i+1] instead of >= passes all three "
            "samples, then takes 3 as the pivot here and crashes looking for a bigger number. The answer is [3,2,3]."),
    ]


def main():
    args = cli()
    sc = build(NUMS, f'nums = {NUMS}. The next arrangement in dictionary order is [3, 1, 2].')
    finish(sc, 31, "Watch the last step: after the swap the tail [2, 1] is still in its largest order, and "
                   "reversing it gives the smallest, [1, 2].",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
