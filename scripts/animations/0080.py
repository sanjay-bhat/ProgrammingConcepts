#!/usr/bin/env python3
"""#80 Remove Duplicates from Sorted Array II: a write head k, and one test, nums[k-2] != num.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [1, 1, 1, 2, 2, 3]                 # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_READ = [0, 1, 1, 1, 2, 2, 2, 3, 3]   # 7; comparing with nums[i-2] (the READ side) gives 6
HARD_GUARD = [-1, 0, 0, 0, 0]             # 3; dropping `k < 2` in Python (nums[-2] wraps) gives 1


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for num in nums:
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1
        return k


def read_side(nums):
    """First attempt: compare with nums[i-2], two behind the READ position."""
    k = 0
    for i in range(len(nums)):
        if i < 2 or nums[i] != nums[i - 2]:
            nums[k] = nums[i]
            k += 1
    return k


def no_guard(nums):
    """First attempt: drop `k < 2`, trusting Python's nums[-2] not to crash."""
    k = 0
    for num in nums:
        if num != nums[k - 2]:
            nums[k] = num
            k += 1
    return k


def trace(nums):
    nums = list(nums)
    events, log = [], []
    st = {'i': None, 'k': 0}

    def rec(kind, **kw):
        events.append(dict(kind=kind, nums=list(nums), log=list(log), **st, **kw))

    rec('start')
    # ---- the notebook's solution, with rec() calls added ----
    k = 0
    i = -1                                                   # display only: the read position
    for num in nums:
        i += 1
        st.update(i=i, k=k)
        # what the two wrong first attempts would look at, on the array as it is now
        wrong_read = (i >= 2 and nums[i] == nums[i - 2])     # display only
        wrong_wrap = nums[k - 2] if len(nums) >= 2 else None  # display only
        if k < 2 or num != nums[k - 2]:
            rec('check', num=num, ok=True, free=k < 2, wrong_read=wrong_read, wrap=wrong_wrap)
            nums[k] = num
            k += 1
            st['k'] = k
            log.append((f'i={i}  ({num})', f'write at {k - 1}', 'good'))
            rec('write', num=num, at=k - 1)
        else:
            rec('check', num=num, ok=False, free=False, wrong_read=wrong_read, wrap=wrong_wrap)
            log.append((f'i={i}  ({num})', 'skip', 'bad'))
    st['i'] = None
    rec('done')
    assert k == Solution().removeDuplicates(list(events[0]['nums']))
    return events


def words(e, notes, trap):
    kd, n, i, k = e['kind'], e['nums'], e['i'], e['k']
    if kd == 'start':
        return ("Two positions: i reads every element, k is where the next survivor will be written.",
                notes.get('start', "Slots before k are the finished answer. k never gets ahead of i."), KEY)
    if kd == 'check':
        num = e['num']
        if e['free']:
            extra = "The first two always survive: two copies are allowed."
            hold = STEP
            if trap == 'guard' and e['wrap'] == num:
                extra = (f"Without the k < 2 check, Python's nums[{k - 2}] reads the END of the list: {e['wrap']}. "
                         f"It equals {num}, so {num} would be wrongly skipped.")
                hold = KEY
            return (f"Read nums[{i}] = {num}. k = {k} is under 2, so keep it without comparing.", extra, hold)
        back = n[k - 2]
        if trap == 'read' and e['wrong_read'] != (not e['ok']):
            extra = (f"Comparing with nums[{i - 2}] instead (the READ side) sees {n[i - 2]}, an overwritten slot, "
                     f"and would {'skip' if e['wrong_read'] else 'keep'} it.")
            hold = KEY
        elif e['ok']:
            extra, hold = "", STEP
        else:
            extra, hold = notes.get('skip', "nums[k-1] sits between them, so it's the same too: this would be a third copy."), KEY
        if e['ok']:
            return (f"Read nums[{i}] = {num}. Two slots back in the answer, nums[{k - 2}] = {back}: different, so keep it.",
                    extra, hold)
        return (f"Read nums[{i}] = {num}. Two slots back in the answer, nums[{k - 2}] = {back}: the same. Skip it.",
                extra, hold)
    if kd == 'write':
        if e['at'] != i:
            if notes.get('_seen_shift'):
                return (f"Write {e['num']} into slot {e['at']} (it was read from slot {i}), then k = {k}.", "", STEP)
            return (f"Write {e['num']} into slot {e['at']} (it was read from slot {i}), then k = {k}.",
                    "From here on, survivors land left of where they were read. That's why we compare with the written side.",
                    KEY)
        return (f"Write {e['num']} into slot {e['at']} (onto itself), then k = {k}.", "", QUICK * 2)
    return (f"Done. Return k = {k}: the answer is the first {k} slots, {n[:k]}.",
            notes.get('done', "Each element was read once and written at most once: O(n) time, O(1) extra space."), END)


def build(nums, subtitle, notes=None, trap=None):
    notes = dict(notes or {})
    sc = Scene('#80 Remove Duplicates from Sorted Array II: write head', subtitle)
    legend = [(style('good')[1], 'the answer so far (before k)'), (style('gold')[1], 'nums[k-2], the test'),
              (ACTIVE, 'being read'), (style('muted')[1], 'read, not kept')]
    for e in trace(nums):
        kd, n, i, k = e['kind'], e['nums'], e['i'], e['k']
        styles = {j: 'good' for j in range(k)}
        if i is not None:
            for j in range(k, i):
                styles[j] = 'muted'
        if kd == 'done':
            styles.update({j: 'muted' for j in range(k, len(n))})   # past k: ignored by the judge
        if kd == 'check':
            if not e['free']:
                styles[k - 2] = 'gold'
            styles[i] = 'active' if e['ok'] else 'bad'
        if kd == 'write':
            styles[e['at']] = 'good'
        ptrs = {}
        if i is not None:
            ptrs['i'] = i
        if kd != 'done':
            if ptrs.get('i') == k:
                ptrs = {'i = k': k}      # one label, not two stacked carets
            else:
                ptrs['k'] = k
        views = [ArrayView(n, styles, pointers=ptrs, title='nums')]
        if kd == 'check':
            if e['free']:
                lines = [f'k = {k} < 2  ->  keep {e["num"]}']
            else:
                same = n[k - 2] == e['num']
                lines = [(f'nums[k-2] = nums[{k - 2}] = {n[k - 2]}  vs  num = {e["num"]}', 'bad' if same else 'good'),
                         'same: a third copy, skip' if same else 'different: write it at k']
            views.append(TextView(lines, size=18))
        if kd in ('write', 'done', 'start'):
            ans = [str(v) for v in n[:k]]
            views.append(TextView([('answer = [' + ', '.join(ans) + ']', 'good')], title='First k slots', size=18))
        cap, sub, hold = words(e, notes, trap)
        if kd == 'write' and e['at'] != i:
            notes['_seen_shift'] = True
        sc.frame(views, cap, sub, hold,
                 side=MapView(e['log'], 'What happened', headers=('read', 'decision'), empty='(nothing read yet)'),
                 counters={'k': k}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert Solution().removeDuplicates(list(HARD_READ)) == 7
    assert read_side(list(HARD_READ)) == 6
    assert Solution().removeDuplicates(list(HARD_GUARD)) == 3
    assert no_guard(list(HARD_GUARD)) == 1
    rd = build(HARD_READ, f'nums = {HARD_READ}. Answer 7. Comparing with nums[i-2], the read side, gives 6.', {
        'start': "Watch the 2s: by the time the third one is read, the slot two behind it has been overwritten.",
        'done': "Answer 7. The read-side test kept only one 2, because it compared against a copy it had just written.",
    }, trap='read')
    gd = build(HARD_GUARD, f'nums = {HARD_GUARD}. Answer 3. Dropping the k < 2 check (Python) gives 1.', {
        'start': "In Python nums[-2] and nums[-1] don't crash: they read from the END of the list. Watch k = 1.",
        'done': "Answer 3. Without k < 2, the 0 at slot 1 was compared with the last element, also 0, and lost.",
    }, trap='guard')
    return [
        (rd, "[0,1,1,1,2,2,2,3,3]: a first attempt that compares with nums[i-2], two behind the READ position, "
             "compares the third 2 with a slot it already overwrote and keeps only one 2. The answer is 7, not 6."),
        (gd, "[-1,0,0,0,0]: a first attempt that drops the k < 2 check works in Python without crashing, "
             "but nums[k-2] at k = 1 reads the last element, a 0, and throws the first 0 away. The answer is 3, not 1."),
    ]


def main():
    args = cli()
    sc = build(NUMS, f'nums = {NUMS}. Keep each value at most twice, in place, and return how many are kept.')
    finish(sc, 80, "Watch the third 1: two slots back in the answer is another 1, so it's skipped, "
                   "and then the first 2 is written into the slot that 1 was read from.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
