#!/usr/bin/env python3
"""#15 3Sum: sort, pick an anchor, then a two-pointer Two Sum on the rest.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [-1, 0, 1, 2, -1, -4]          # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_DUP = [-2, 0, 0, 2, 2]           # [[-2,0,2]]; skipping repeats only for the anchor reports it twice
HARD_NEXT = [-2, 0, 2, -2, 4]         # [[-2,-2,4],[-2,0,2]]; comparing the anchor with the NEXT number loses [-2,-2,4]


def fmt(xs):
    return '[' + ','.join(map(str, xs)) + ']'


def trace(nums):
    nums = list(nums)
    events, anchors = [], []
    st = {'i': None, 'left': None, 'right': None}

    def rec(kind, result, **kw):
        events.append(dict(kind=kind, nums=list(nums), result=[list(r) for r in result],
                           anchors=list(anchors), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    result = []
    original = list(nums)                                                 # display only
    nums.sort()
    rec('sorted', result, original=original)
    for i in range(len(nums) - 2):
        st.update(i=i, left=None, right=None)
        if i > 0 and nums[i] == nums[i - 1]:
            anchors.append((i, nums[i], 'skipped: repeat'))
            rec('skip_anchor', result)
            continue
        left, right = i + 1, len(nums) - 1
        st.update(left=left, right=right)
        anchors.append((i, nums[i], 'searching'))
        found_before = len(result)                                        # display only
        rec('anchor', result)
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                rec('match', result, total=total)
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                    st['left'] = left
                    rec('dup_left', result)
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    st['right'] = right
                    rec('dup_right', result)
                left += 1
                right -= 1
                st.update(left=left, right=right)
                rec('both', result)
            elif total < 0:
                rec('small', result, total=total)
                left += 1
                st['left'] = left
            else:
                rec('big', result, total=total)
                right -= 1
                st['right'] = right
        n_found = len(result) - found_before
        anchors[-1] = (i, nums[i], f'found {n_found}' if n_found else 'no match')
        rec('anchor_done', result, found=n_found)
    st.update(i=None, left=None, right=None)
    rec('done', result)
    assert result == Solution().threeSum(list(original))
    return events


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result


def anchor_skip_only(nums):
    """First attempt: skip repeated anchors, but not repeats after a match."""
    nums, result = sorted(nums), []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


def compare_next(nums):
    """First attempt: skip an anchor equal to the NEXT number instead of the previous one."""
    nums, result = sorted(nums), []
    for i in range(len(nums) - 2):
        if nums[i] == nums[i + 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


def words(e, notes, firsts):
    k, n, i, L, R = e['kind'], e['nums'], e['i'], e['left'], e['right']
    if k == 'sorted':
        if e['original'] == n:
            return (f"Sort first. {fmt(n)} is already sorted.",
                    "Equal numbers sit side by side, which is what the repeat checks rely on.", KEY)
        return (f"Sort first: {fmt(e['original'])} becomes {fmt(n)}.",
                "Now the two-pointer sweep works, and equal numbers sit side by side.", KEY)
    if k == 'skip_anchor':
        return (f"The anchor at index {i} is {n[i]}, the same as the anchor before it. Skip it.",
                notes.get('skip_anchor', f"The previous {n[i]} already found every triplet this one could."), KEY)
    if k == 'anchor':
        return (f"Anchor at index {i}: {n[i]}. Find two numbers after it that add up to {-n[i]}.",
                notes.get(('anchor', i), "left starts just after the anchor, right at the end."),
                KEY if firsts.get('anchor') == id(e) else STEP)
    if k in ('small', 'big', 'match'):
        a, b, c, t = n[i], n[L], n[R], e['total']
        head = f"{a} + {b} + {c} = {t}"
        if k == 'small':
            return (f"{head}: too small. Move left one step right, to a bigger number.", "",
                    STEP if firsts.get('small') == id(e) else QUICK * 2)
        if k == 'big':
            return (f"{head}: too big. Move right one step left, to a smaller number.", "",
                    STEP if firsts.get('big') == id(e) else QUICK * 2)
        return (f"{head}: a match! Record {fmt([a, b, c])}.",
                notes.get(('match', len(e['result'])), "Then step both pointers past any copies of their values."), KEY)
    if k == 'dup_left':
        return (f"The next number, nums[{L}], is {n[L]} again: a copy of the left value just matched. Slide left onto it.",
                notes.get('dup_left', "left slides along every copy; the move-both step then jumps past the last one."), KEY)
    if k == 'dup_right':
        return (f"nums[{R}] is {n[R]} again: a copy of the right value just matched. Slide right onto it.",
                notes.get('dup_right', "right slides along every copy; the move-both step then jumps past the last one."), KEY)
    if k == 'both':
        if L >= R:
            return ("Move both pointers inward. They've met, so this anchor is done.", "", STEP)
        return (f"Move both pointers inward: left = {L}, right = {R}.",
                "Moving only one can't reach zero again with a new pair of values.", STEP)
    if k == 'anchor_done':
        return (f"The anchor {n[i]} at index {i} is done: {e['found']} triplet{'s' if e['found'] != 1 else ''} found.", "", QUICK * 2)
    res = ', '.join(fmt(r) for r in e['result']) or 'none'
    return (f"Done. Triplets: {res}.",
            notes.get('done', "Each anchor's sweep is one pass, so it's O(n²) in all."), END)


def build(nums, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#15 3Sum: anchor plus two pointers', subtitle)
    legend = [(style('gold')[1], 'anchor'), (ACTIVE, 'left / right'), (style('window')[1], 'still to search'),
              (style('bad')[1], 'skipped repeat')]
    events = trace(nums)
    firsts = {}
    for e in events:
        if e['kind'] in ('anchor', 'small', 'big') and e['kind'] not in firsts:
            firsts[e['kind']] = id(e)
    for e in events:
        k, i, L, R = e['kind'], e['i'], e['left'], e['right']
        n = e['nums']
        styles = {}
        for j in range(len(n)):
            if i is not None and j < i:
                styles[j] = 'muted'
            elif L is not None and L <= j <= R:
                styles[j] = 'window'
            elif i is not None and j > i:
                styles[j] = 'muted'
        if i is not None:
            styles[i] = 'bad' if k == 'skip_anchor' else 'gold'
        if k == 'skip_anchor':
            styles[i - 1] = 'gold'
        if L is not None and L < len(n) and L <= R:
            styles[L] = 'active'
            styles[R] = 'active'
        if k == 'match':
            styles[L] = styles[R] = 'good'
            styles[i] = 'good'
        if k == 'dup_left':
            styles[L - 1], styles[L] = 'muted', 'bad'
        if k == 'dup_right':
            styles[R + 1], styles[R] = 'muted', 'bad'
        if k == 'done':
            styles = {}
        ptrs = {}
        if i is not None:
            ptrs['i'] = i
        if L is not None and L <= R:
            ptrs['left'], ptrs['right'] = L, R
        win = (L, R) if L is not None and L <= R else None
        arr = ArrayView(n, styles, pointers=ptrs, window=win, title='nums')
        views = [arr]
        if k in ('small', 'big', 'match'):
            t = e['total']
            need = -n[i]
            views.append(TextView([(f'{n[i]} + {n[L]} + {n[R]} = {t}', 'good' if t == 0 else None),
                                   f'need left + right = {need}, have {n[L] + n[R]}'], size=18))
        newest = len(e['result']) - 1 if k == 'match' else None
        chips = [(fmt(r), 'good' if j == newest or k == 'done' else None) for j, r in enumerate(e['result'])]
        views.append(ChipsView(chips, 'Triplets found', empty='(none yet)', size=17))
        rows = []
        for j, v, what in e['anchors']:
            st = 'bad' if what.startswith('skipped') else ('gold' if what == 'searching' else None)
            rows.append((f'i = {j}  ({v})', what, st))
        cap, sub, hold = words(e, notes, firsts)
        sc.frame(views, cap, sub, hold,
                 side=MapView(rows, 'Anchors', headers=('anchor', 'what happened'), empty='(none yet)'),
                 counters={'triplets': len(e['result'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert Solution().threeSum(list(HARD_DUP)) == [[-2, 0, 2]]
    assert anchor_skip_only(HARD_DUP) == [[-2, 0, 2], [-2, 0, 2]]
    assert Solution().threeSum(list(HARD_NEXT)) == [[-2, -2, 4], [-2, 0, 2]]
    assert compare_next(HARD_NEXT) == [[-2, 0, 2]]
    dup = build(HARD_DUP, f'nums = {HARD_DUP}. Answer [[-2,0,2]]. Skipping only repeated anchors reports it twice.', {
        'dup_left': "Without these slides, moving both would land on 0 and 2 again: [-2,0,2] a second time.",
        'dup_right': "Same on the right. Now the move-both step takes both pointers past their copies.",
        'done': "One anchor, one triplet. The step-past-copies loops are what kept it to one.",
    })
    nxt = build(HARD_NEXT, f'nums = {HARD_NEXT}. Answer [[-2,-2,4],[-2,0,2]]. Comparing with the next number loses one.', {
        ('anchor', 0): "Its twin -2 sits right after it. Checking nums[i + 1] would skip this anchor, and its triplet with it.",
        ('match', 1): "This triplet uses BOTH -2s: the first as anchor, the second as left. Only the first anchor can find it.",
        'skip_anchor': "Skipping the SECOND -2 is safe: the first one already searched everything to its right.",
        'done': "Comparing with the previous anchor keeps the first -2, which is the only one that finds [-2,-2,4].",
    })
    return [
        (dup, "[-2,0,0,2,2]: after the first match the pointers would land on the second 0 and the second 2. "
              "A first attempt that only skips repeated anchors reports [-2,0,2] twice; the answer is [[-2,0,2]]."),
        (nxt, "[-2,0,2,-2,4] sorts to [-2,-2,0,2,4]. A first attempt that compares the anchor with the NEXT number "
              "skips the first -2 and loses [-2,-2,4]; the answer is [[-2,-2,4],[-2,0,2]]."),
    ]


def main():
    args = cli()
    sc = build(NUMS, f'nums = {NUMS}. Find every triplet that adds up to 0, each one once.')
    finish(sc, 15, "Watch the second -1: it's the same value as the anchor before it, so it's skipped "
                   "instead of finding [-1,0,1] a second time.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
