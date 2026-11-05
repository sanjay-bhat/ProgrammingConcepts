#!/usr/bin/env python3
"""#34 Find First and Last Position: two binary searches that don't stop on a match.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS, TARGET = [5, 7, 7, 8, 8, 10], 8          # LeetCode example 1: [3, 4]

# The hard example (interactive page only): the run of 4s reaches the last
# index. A common first attempt finds the last copy as "first number bigger
# than the target, minus one", searching with hi = len(nums) - 1. It passes
# all three LeetCode samples, but here there is no bigger number, the search
# can't move past index 7, and it answers [1, 6]. Correct: [1, 7].
HARD_NUMS, HARD_TARGET = [2, 4, 4, 4, 4, 4, 4, 4], 4
HARD_NOTES = {
    (2, 'match', 7): "The run reaches the very end. A 'first number bigger than 4' search capped at hi = 7 "
                     "has nowhere to go past here, and answers 7 - 1 = 6.",
    'done': "Upper-bound search with hi = len - 1 passes all three LeetCode samples and answers [1, 6] here.",
}


def wrong_upper_bound(nums, target):
    """The first attempt the hard example breaks: last = upper bound - 1, with hi = len(nums) - 1."""
    if not nums:
        return [-1, -1]
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        m = (lo + hi) // 2
        if nums[m] < target:
            lo = m + 1
        else:
            hi = m
    if nums[lo] != target:
        return [-1, -1]
    first = lo
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        m = (lo + hi) // 2
        if nums[m] <= target:
            lo = m + 1
        else:
            hi = m
    return [first, lo - 1]


def trace(nums, target):
    events = []
    st = {'search': 1, 'first': None, 'last': None, 'rounds': 0}

    def rec(kind, **kw):
        events.append(dict(kind=kind, **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    class Solution:
        def searchRange(self, nums, target):
            return [self._find_first(nums, target), self._find_last(nums, target)]

        def _find_first(self, nums, target):
            st['search'] = 1
            lo, hi, result = 0, len(nums) - 1, -1
            rec('start', lo=lo, hi=hi, result=result)
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                st['rounds'] += 1
                rec('look', lo=lo, hi=hi, mid=mid, result=result)
                if nums[mid] == target:
                    result = mid
                    hi = mid - 1
                    rec('match', lo=lo, hi=hi, mid=mid, result=result)
                elif nums[mid] < target:
                    lo = mid + 1
                    rec('small', lo=lo, hi=hi, mid=mid, result=result)
                else:
                    hi = mid - 1
                    rec('big', lo=lo, hi=hi, mid=mid, result=result)
            st['first'] = result
            rec('end', lo=lo, hi=hi, result=result)
            return result

        def _find_last(self, nums, target):
            st['search'] = 2
            lo, hi, result = 0, len(nums) - 1, -1
            rec('start', lo=lo, hi=hi, result=result)
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                st['rounds'] += 1
                rec('look', lo=lo, hi=hi, mid=mid, result=result)
                if nums[mid] == target:
                    result = mid
                    lo = mid + 1
                    rec('match', lo=lo, hi=hi, mid=mid, result=result)
                elif nums[mid] < target:
                    lo = mid + 1
                    rec('small', lo=lo, hi=hi, mid=mid, result=result)
                else:
                    hi = mid - 1
                    rec('big', lo=lo, hi=hi, mid=mid, result=result)
            st['last'] = result
            rec('end', lo=lo, hi=hi, result=result)
            return result

    ans = Solution().searchRange(nums, target)
    rec('done', lo=None, hi=None, result=None, ans=ans)
    return events, ans


def words(e, nums, target, first_match, notes):
    k, s = e['kind'], e['search']
    side = 'left' if s == 1 else 'right'
    which = 'first' if s == 1 else 'last'
    if notes:
        key = 'done' if k == 'done' else (s, k, e.get('mid'))
        if key in notes:
            cap, _, hold = _words(e, nums, target, first_match, side, which)
            return cap, notes[key], (END if k == 'done' else KEY)
    return _words(e, nums, target, first_match, side, which)


def _words(e, nums, target, first_match, side, which):
    k, s = e['kind'], e['search']
    m = e.get('mid')
    if k == 'start':
        if s == 1:
            return (f"Search 1 looks for the FIRST {target}. Window: the whole array, result = -1.",
                    "If nothing ever matches, the -1 is what comes back.", STEP)
        return (f"Search 2 looks for the LAST {target}. Same loop, one line different.",
                "On a match it keeps going right instead of left.", KEY)
    if k == 'look':
        return (f"Middle of the window {e['lo']}..{e['hi']} is index {m}: nums[{m}] = {nums[m]}.",
                f"Compare it with the target, {target}.", STEP)
    if k == 'small':
        return (f"{nums[m]} < {target}: everything up to index {m} is too small. Move lo to {e['lo']}.", "", STEP)
    if k == 'big':
        return (f"{nums[m]} > {target}: everything from index {m} on is too big. Move hi to {e['hi']}.", "", STEP)
    if k == 'match':
        if first_match.get(s) == m:
            if s == 1:
                return (f"nums[{m}] = {target}: a match! Record {m}, but DON'T stop.",
                        f"An earlier {target} could still sit to the left, so keep searching left: hi = {e['hi']}.", KEY)
            return (f"nums[{m}] = {target}: record {m}, and keep searching RIGHT: lo = {e['lo']}.",
                    f"A later {target} could still sit to the right.", KEY)
        nxt = f"hi = {e['hi']}" if s == 1 else f"lo = {e['lo']}"
        return (f"nums[{m}] = {target} again: record {m} and keep going {side}, {nxt}.", "", STEP)
    if k == 'end':
        r = e['result']
        if r == -1:
            return (f"Window empty: the target never matched, so search {s} returns -1.", "", KEY)
        return (f"Window empty (lo > hi). The last index recorded, {r}, is the {which} {target}.",
                "The loop only ends when there's nowhere left to look.", KEY)
    a = e['ans']
    return (f"searchRange returns [{a[0]}, {a[1]}].",
            "Each search halved the window every round: about log₂ n rounds, 17 for 100,000 numbers.", END)


def build(nums, target, subtitle, notes=None):
    events, ans = trace(nums, target)
    first_match = {}
    for e in events:
        if e['kind'] == 'match':
            first_match.setdefault(e['search'], e['mid'])
    sc = Scene('#34 First and Last Position: binary search that keeps going', subtitle)
    legend = [(ACTIVE, 'middle being checked'), (style('good')[1], 'recorded match'),
              (style('muted')[1], 'ruled out')]
    for e in events:
        lo, hi, m, k = e['lo'], e['hi'], e.get('mid'), e['kind']
        styles, ptrs, window = {}, {}, None
        if lo is not None:
            for i in range(len(nums)):
                if not (lo <= i <= hi):
                    styles[i] = 'muted'
            if lo <= hi:
                window = (lo, hi)
            if lo < len(nums):
                ptrs['lo'] = lo
            if hi >= 0:
                ptrs['hi'] = hi
        if e['result'] not in (None, -1):
            styles[e['result']] = 'good'
        if k in ('look', 'match', 'small', 'big'):
            styles[m] = 'good' if k == 'match' else 'active'
            ptrs['mid'] = m
        if k == 'done' and ans[0] != -1:
            for i in range(ans[0], ans[1] + 1):
                styles[i] = 'good'
            ptrs = {'first': ans[0], 'last': ans[1]} if ans[0] != ans[1] else {'first/last': ans[0]}
        view = ArrayView(nums, styles=styles, pointers=ptrs, window=window, title='nums')
        f = '-' if e['first'] is None else str(e['first'])
        l = '-' if e['last'] is None else str(e['last'])
        rows = [('target', str(target)),
                ('searching for', 'both done' if k == 'done' else
                 'first copy (leans left)' if e['search'] == 1 else 'last copy (leans right)'),
                ('result so far', '-' if e['result'] is None else str(e['result']), 'active'),
                ('first', f, 'good' if f not in ('-', '-1') else None),
                ('last', l, 'good' if l not in ('-', '-1') else None)]
        rows = [r if (len(r) == 2 or r[2]) else r[:2] for r in rows]
        cap, sub, hold = words(e, nums, target, first_match, notes)
        sc.frame([view], cap, sub, hold, side=MapView(rows, 'Searches', headers=('', '')),
                 counters={'search': e['search'] if k != 'done' else '-', 'rounds': e['rounds']}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    sc_ans = trace(HARD_NUMS, HARD_TARGET)[1]
    assert sc_ans == [1, 7] and wrong_upper_bound(HARD_NUMS, HARD_TARGET) == [1, 6]
    for nums, t in (([5, 7, 7, 8, 8, 10], 8), ([5, 7, 7, 8, 8, 10], 6), ([], 0)):   # the LeetCode samples
        assert wrong_upper_bound(nums, t) == trace(nums, t)[1]
    sc = build(HARD_NUMS, HARD_TARGET, f'nums = {HARD_NUMS}, target = {HARD_TARGET}. Answer [1, 7]: '
               'the run of 4s reaches the last index.', HARD_NOTES)
    return sc, ("The run of 4s runs to the end of the array. Finding the last copy as 'first bigger number "
                "minus one' with hi = len - 1 passes all three LeetCode samples, then answers [1, 6] here. "
                "Watch search 2 record index 7.")


def main():
    args = cli()
    sc = build(NUMS, TARGET, 'nums is sorted. Green = an index we recorded; grey = ruled out.')
    finish(sc, 34, "Watch search 1 land on index 4: it's an 8, but the search records it and keeps "
                   "looking left, which is how it finds the first 8 at index 3.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
