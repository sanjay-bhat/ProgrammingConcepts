#!/usr/bin/env python3
"""#75 Sort Colors: three pointers split the array into 0s | 1s | unsorted | 2s.
A 0 is swapped to the front and both lo and mid move; a 1 just moves mid; a 2
is swapped to the back and ONLY hi moves, because the value that came back
from the end hasn't been looked at yet.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [2, 0, 2, 1, 1, 0]          # LeetCode example 1

# Hard example 1: moving mid forward after swapping a 2 to the back (treating
# the swap like the 0 case) passes both LeetCode samples, then leaves a 0 and a
# 1 stranded here: [0, 1, 0, 2, 1, 2, 2].
HARD1 = [2, 1, 2, 0, 1, 0, 2]
HARD1_ANSWER, HARD1_WRONG = [0, 0, 1, 1, 2, 2, 2], [0, 1, 0, 2, 1, 2, 2]

# Hard example 2: all 2s. Every step swaps a 2 to the back and lowers hi, and
# the last one takes hi from 0 to -1. Fine in Python and Go; in Rust, with hi
# a usize and no `if hi == 0 { break; }` guard, that subtraction panics. Both
# LeetCode samples stop before hi reaches 0, so they never hit it.
HARD2 = [2, 2, 2, 2]
HARD2_ANSWER = [2, 2, 2, 2]


class Solution:
    # ---- the notebook's solution, unchanged (used to check the answers) ----
    def sortColors(self, nums: list[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1


def solved(nums):
    a = nums[:]
    Solution().sortColors(a)
    return a


def wrong_mid_after_two(nums):
    """First attempt: after swapping a 2 to the back, also move mid on (as in the 0 case)."""
    a = nums[:]
    lo, mid, hi = 0, 0, len(a) - 1
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]; lo += 1; mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[hi] = a[hi], a[mid]; hi -= 1; mid += 1
    return a


def wrong_unsigned(nums):
    """First attempt in Rust: hi is a usize and nothing guards hi -= 1 at 0 (a panic, modelled as an error)."""
    a = nums[:]
    lo, mid, hi = 0, 0, len(a) - 1
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]; lo += 1; mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            if hi == 0:
                raise OverflowError('attempt to subtract with overflow')
            hi -= 1
    return a


def panics(f, nums):
    try:
        f(nums)
    except OverflowError:
        return True
    return False


SAMPLES = [([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]), ([2, 0, 1], [0, 1, 2])]
for _in, _out in SAMPLES:          # both first attempts pass both LeetCode samples
    assert solved(_in) == wrong_mid_after_two(_in) == wrong_unsigned(_in) == _out
assert solved(HARD1) == HARD1_ANSWER and wrong_mid_after_two(HARD1) == HARD1_WRONG
assert solved(HARD2) == HARD2_ANSWER and panics(wrong_unsigned, HARD2)


def trace(arr):
    nums = arr[:]
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, nums=nums[:], lo=lo, mid=mid, hi=hi, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    lo, mid, hi = 0, 0, len(nums) - 1
    rec('start')
    while mid <= hi:
        if nums[mid] == 0:
            same = lo == mid
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
            rec('zero', at=mid - 1, to=lo - 1, same=same)
        elif nums[mid] == 1:
            mid += 1
            rec('one', at=mid - 1)
        else:  # nums[mid] == 2
            came = nums[hi]
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1
            rec('two', at=mid, to=hi + 1, came=came)
    rec('done')
    return events


VAL_STYLE = {0: 'bad', 1: 'plain', 2: 'window'}


def build(arr, subtitle, notes=None):
    """notes: {(kind, step) or kind: text} replaces that frame's second caption line, held as KEY."""
    notes = notes or {}
    sc = Scene('#75 Sort Colors: 0s | 1s | unsorted | 2s, in one pass', subtitle)
    legend = [(style('bad')[1], '0 (red)'), (style('plain')[1], '1 (white)'), (style('window')[1], '2 (blue)'),
              (ACTIVE, 'just swapped / checked')]
    first, last_two = set(), False
    for step, e in enumerate(trace(arr)):
        k, nums, lo, mid, hi = e['kind'], e['nums'], e['lo'], e['mid'], e['hi']
        n = len(nums)
        styles = {i: VAL_STYLE[v] for i, v in enumerate(nums)}
        subs = {}
        for i in range(n):
            subs[i] = '0s' if i < lo else '1s' if i < mid else '?' if i <= hi else '2s'
        hold, sub = STEP, ''
        if k == 'start':
            cap = "lo = 0, mid = 0, hi = end. Everything from mid to hi is still unsorted."
            sub = "Left of lo: 0s. lo to mid-1: 1s. Right of hi: 2s. Each step shrinks the '?' zone by one."
            hold = KEY
        elif k == 'zero':
            if e['same']:
                cap = f"nums[{e['at']}] is 0: swap it with nums[lo] (itself), then lo and mid both move on."
                sub = "lo == mid here, so the 'swap' changes nothing; the 0 is already in place."
            else:
                cap = f"nums[{e['at']}] is 0: swap it to index {e['to']}, the first 1. lo and mid both move on."
                sub = "What came back from lo is a 1 we've already checked, so mid can safely skip it."
                if 'zero' not in first:
                    first.add('zero')
                    hold = KEY
            if last_two:
                sub = "That 0 came from the back a moment ago. If mid had moved on after that swap, it'd be stuck here."
                hold = KEY
        elif k == 'one':
            cap = f"nums[{e['at']}] is 1: it's already in the middle zone. Just move mid on."
            hold = QUICK * 2.2
        elif k == 'two':
            if e['at'] == e['to']:
                cap = f"nums[{e['at']}] is 2 and it's the last unsorted spot: it swaps with itself, and hi moves back."
            else:
                cap = (f"nums[{e['at']}] is 2: swap it to index {e['to']} at the back, and only hi moves. "
                       f"A {e['came']} came back.")
            if 'two' not in first:
                first.add('two')
                sub = "mid stays put: the value that came back from the end hasn't been looked at yet."
                hold = KEY
            if hi < 0:
                sub = "hi is now -1. Fine in Python and Go; a Rust usize can't go below 0, hence its guard."
                hold = KEY
        else:
            cap = f"mid ({mid}) has passed hi ({hi}): nothing is unsorted. Done: {nums}."
            sub = "Each step either moves mid on or moves hi back, so it's at most n steps: O(n), O(1) memory."
            hold = END
        for key in ((k, step), k):
            if key in notes:
                sub, hold = notes[key], max(hold, KEY)
                break
        last_two = k == 'two'
        if k in ('zero', 'one', 'two'):
            styles[e['at']] = 'active' if k != 'one' else styles[e['at']]
        ptr = {'lo': lo, 'mid': mid, 'hi': hi}
        arrv = ArrayView(nums, styles=styles, pointers=ptr, window=(mid, hi) if mid <= hi else None,
                         title='nums', subs=subs, cell=min(62, int(520 / max(n, 1)) - 6))
        rule = {'zero': 'nums[mid] == 0 → swap with lo; lo += 1; mid += 1',
                'one': 'nums[mid] == 1 → mid += 1',
                'two': 'nums[mid] == 2 → swap with hi; hi -= 1  (mid stays)'}.get(k, 'while mid <= hi:')
        side = [('lo', str(lo)), ('mid', str(mid)), ('hi', str(hi), 'bad' if hi < 0 else None),
                ('0s', f'[0 .. {lo - 1}]' if lo else 'none yet', 'bad' if lo else None),
                ('1s', f'[{lo} .. {mid - 1}]' if mid > lo else 'none yet'),
                ('unsorted', f'[{mid} .. {hi}]' if mid <= hi else 'empty', 'active' if mid <= hi else None),
                ('2s', f'[{hi + 1} .. {n - 1}]' if hi < n - 1 else 'none yet', 'window' if hi < n - 1 else None)]
        sc.frame([arrv, TextView([rule], title='rule applied', size=16)], cap, sub, hold,
                 side=MapView(side, 'Pointers and zones', headers=('', '')), legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(HARD1, 'nums = [2, 1, 2, 0, 1, 0, 2]. Two of the swaps bring a 0 back from the end.',
                {'done': "Moving mid on after a 2-swap passes both LeetCode samples, then leaves [0, 1, 0, 2, 1, 2, 2] here."})
    sc2 = build(HARD2, 'nums = [2, 2, 2, 2]. Every step is a 2-swap, so hi walks all the way down.',
                {'done': "Correct, but hi ended at -1. A Rust usize with no `if hi == 0 { break; }` panics on that last step."})
    return [(sc1, "Moving mid forward after swapping a 2 to the back passes both LeetCode samples. Here the "
                  "swaps bring back a 0 and a 1 that never get looked at, leaving [0, 1, 0, 2, 1, 2, 2]."),
            (sc2, "All 2s: hi steps down past 0 to -1. Harmless in Python and Go, but it's why the Rust "
                  "version needs its `if hi == 0 { break; }` guard; neither LeetCode sample reaches it.")]


def main():
    args = cli()
    sc = build(NUMS, 'LeetCode example 1. Sort 0s, 1s and 2s in place, in one pass.')
    finish(sc, 75, "Watch the first step: a 2 is swapped to the back and a 0 comes back, and mid stays put "
                   "so that 0 gets checked next.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
