#!/usr/bin/env python3
"""#16 3Sum Closest: sort, fix one number, and walk two pointers inwards,
steering the sum towards the target and remembering the nearest one seen.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS, TARGET = [-1, 2, 1, -4], 1          # LeetCode example 1: answer 2

# Hard examples (interactive page only), each breaking a plausible first attempt.
# 1) Forgetting to sort. Both LeetCode samples pass by luck: the starting guess
#    nums[0] + nums[1] + nums[2] is already the answer (2, and 0). Here the
#    unsorted run steers the pointers the wrong way and returns -6. Answer -9.
HARD_SORT = ([1, 8, -3, 5, -4, -7], -9)
# 2) Starting closest at 10**4, "bigger than any sum" (sums are at most 3000).
#    What matters is the GAP to the target, and with target = 10000 the
#    sentinel's gap is 0, so it never gets replaced and 10000 comes back,
#    which isn't a sum at all. Answer 2300.
HARD_SENTINEL = ([300, 800, 1000, -200, 500], 10000)


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return closest


def run(nums, target, sort=True, start=None):
    """The same loop with the two first-attempt slips switchable."""
    nums = sorted(nums) if sort else list(nums)
    closest = nums[0] + nums[1] + nums[2] if start is None else start
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(closest - target):
                closest = total
            if total == target:
                return target
            elif total < target:
                left += 1
            else:
                right -= 1
    return closest


def trace(nums, target):
    events = []
    original = list(nums)

    def rec(kind, **kw):
        events.append(dict(kind=kind, nums=nums[:], closest=closest, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    closest = None
    rec('given')
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    rec('init')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        rec('anchor', i=i, left=left, right=right)
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            before = closest
            if abs(total - target) < abs(closest - target):
                closest = total
            if total == target:
                rec('try', i=i, left=left, right=right, total=total, before=before, move='hit')
                rec('done', ans=target)
                assert target == Solution().threeSumClosest(list(original), target)
                return events
            elif total < target:
                rec('try', i=i, left=left, right=right, total=total, before=before, move='left')
                left += 1
            else:
                rec('try', i=i, left=left, right=right, total=total, before=before, move='right')
                right -= 1
        rec('cross', i=i, left=left, right=right)
    rec('done', ans=closest)
    assert closest == Solution().threeSumClosest(list(original), target)
    return events


def build(nums, target, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#16 3Sum Closest: sort, anchor, squeeze', subtitle)
    legend = [(style('gold')[1], 'anchor nums[i]'), (style('window')[1], 'left and right'),
              (style('muted')[1], 'done as anchor'), (style('good')[1], 'closest triple')]
    seen = set()
    best_triple = None
    for idx, e in enumerate(trace(list(nums), target)):
        k = e['kind']
        arr, n = e['nums'], len(e['nums'])
        styles, ptrs, window = {}, {}, None
        if k == 'init':
            best_triple = (0, 1, 2)
        if k in ('anchor', 'try', 'cross'):
            i, L, R = e['i'], e['left'], e['right']
            for j in range(i):
                styles[j] = 'muted'
            styles[i] = 'gold'
            ptrs = {'i': i}
            if L < n:
                ptrs['L'] = L
            if R >= 0 and R != L:
                ptrs['R'] = R
            if k != 'cross':
                styles[L] = styles[R] = 'window'
                window = (L, R)
            if k == 'try' and e['closest'] != e['before']:
                best_triple = (i, L, R)
        if k in ('init', 'done') and best_triple:
            for j in best_triple:
                styles[j] = 'good'
        view = ArrayView(arr if k != 'given' else list(nums), styles, ptrs, window=window,
                         title='sorted' if k != 'given' else 'nums')
        lines = []
        if k == 'try':
            a, b, c = arr[e['i']], arr[e['left']], arr[e['right']]
            lines = [f"sum = {a} + {b} + {c} = {e['total']}",
                     f"gap = |{e['total']} - ({target})| = {abs(e['total'] - target)}"
                     f"    best gap so far = {abs(e['before'] - target)}"]
        elif k == 'init':
            lines = [f"closest = {arr[0]} + {arr[1]} + {arr[2]} = {e['closest']}",
                     f"gap = |{e['closest']} - ({target})| = {abs(e['closest'] - target)}"]
        elif k == 'done' and best_triple:
            a, b, c = (arr[j] for j in best_triple)
            lines = [f"{a} + {b} + {c} = {e['ans']}", f"gap = |{e['ans']} - ({target})| = {abs(e['ans'] - target)}"]
        text = TextView(lines or [''], size=18)
        rows = [('target', str(target))]
        if e['closest'] is not None:
            rows += [('closest', str(e['closest']), 'good'), ('its gap', str(abs(e['closest'] - target)))]
        if k == 'try':
            rows += [('sum', str(e['total']), 'window')]
        cap, sub, hold = words(e, target, seen)
        key = (k, e.get('i'), e.get('left'), e.get('right')) if k in ('try', 'cross') else k
        if key in notes:
            sub, hold = notes[key], (END if k == 'done' else KEY)
        counters = {'closest': e['closest']} if e['closest'] is not None else None
        sc.frame([view, text], cap, sub, hold, side=MapView(rows, 'State', headers=('', '')),
                 counters=counters, legend=legend)
    return sc


def words(e, target, seen):
    k = e['kind']
    arr = e['nums']
    if k == 'given':
        return (f"Find three numbers whose sum is as close to {target} as possible.",
                "First, sort. Then a sum that's too small can only grow by moving right.", STEP)
    if k == 'init':
        return (f"Sorted. Start closest at a real sum: the first three, {e['closest']}.",
                "A real triple, not a made-up 'big number', so the answer is always a sum that exists.", KEY)
    if k == 'anchor':
        return (f"Anchor nums[{e['i']}] = {arr[e['i']]}. L and R start at the two ends of what's left.",
                "Now it's a two-number search over the rest of the sorted array.", STEP)
    if k == 'cross':
        return (f"L and R have met: every pair for anchor {arr[e['i']]} has been considered.", "", QUICK * 2)
    if k == 'done':
        return (f"Answer: {e['ans']}.", "Sorting is n log n; each anchor's squeeze is n steps, so O(n²) overall.",
                END)
    t, gap, old = e['total'], abs(e['total'] - target), abs(e['before'] - target)
    better = e['closest'] != e['before']
    head = f"Sum {t}, gap {gap}." + (f" Better than {old}: closest = {t}." if better else f" Not better than {old}.")
    if e['move'] == 'hit':
        return (head.split('.')[0] + ": exactly the target. Nothing can be closer, so return it.", "", KEY)
    if e['move'] == 'left':
        first = 'left' not in seen
        seen.add('left')
        return (head + " Too small: move L right.",
                "Sorted, so the only way to make the sum bigger is a bigger left number." if first else "",
                KEY if first else STEP)
    first = 'right' not in seen
    seen.add('right')
    return (head + " Too big: move R left.",
            "Moving L instead would only make it bigger. R's partner can't help, so drop R." if first else "",
            KEY if first else STEP)


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = [([-1, 2, 1, -4], 1, 2), ([0, 0, 0], 1, 0)]
    for nums, t, want in samples:     # both slips pass both LeetCode samples
        assert Solution().threeSumClosest(list(nums), t) == want
        assert run(nums, t, sort=False) == want and run(nums, t, start=10 ** 4) == want
    assert Solution().threeSumClosest(list(HARD_SORT[0]), HARD_SORT[1]) == -9
    assert run(*HARD_SORT, sort=False) == -6
    assert Solution().threeSumClosest(list(HARD_SENTINEL[0]), HARD_SENTINEL[1]) == 2300
    assert run(*HARD_SENTINEL, start=10 ** 4) == 10000
    a = build(*HARD_SORT, f'nums = {HARD_SORT[0]}, target = {HARD_SORT[1]}. Answer -9. Without sorting: -6.', {
        'given': "Skip the sort and the pointer moves stop meaning anything: moving L right no longer "
                 "promises a bigger number.",
        'done': "-9, an exact hit. The same loop on the unsorted array steers the wrong way and returns -6.",
    })
    b = build(*HARD_SENTINEL, f'nums = {HARD_SENTINEL[0]}, target = {HARD_SENTINEL[1]}. Answer 2300. '
                              'Starting closest at 10**4 returns 10000.', {
        'init': "Start at 10**4 instead and its gap to 10000 is 0. No real sum can beat that, "
                "so 10000 would come back, and it isn't a sum of anything.",
        'done': "2300, the biggest sum there is. A sentinel bigger than any sum isn't the same as one "
                "further from the target than any sum.",
    })
    return [
        (a, "Unsorted input: the two LeetCode samples pass without sorting, because the first three numbers "
            "already happen to be the answer. Here the unsorted run returns -6; the answer is -9."),
        (b, "target = 10000, the largest allowed. Starting closest at 10**4 'because it's bigger than any sum' "
            "gives the sentinel a gap of 0, so it's returned. The answer is 2300."),
    ]


def main():
    args = cli()
    sc = build(NUMS, TARGET, f'nums = {NUMS}, target = {TARGET}. Sum of three numbers nearest the target.')
    finish(sc, 16, "Watch the first squeeze: the sum is too small, and because the array is sorted the only "
                   "way up is to move the left pointer right.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
