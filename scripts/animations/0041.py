#!/usr/bin/env python3
"""#41 First Missing Positive: slot v-1 is a yes/no box for "is v present?",
and a negative sign is the tick.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [3, 4, -1, 1]          # LeetCode example 2: answer 2

# Hard example 1 (interactive page only): duplicates. Flipping the sign,
# nums[v-1] = -nums[v-1], passes all three LeetCode samples (none has a
# duplicate), but here the second 3 and the second 1 untick their slots and
# it answers 1. Correct: 4.
HARD_DUP = [3, 1, 3, 2, 1]
HARD_DUP_NOTES = {
    (2, 2): "The second 3. Flipping the sign would turn slot 2 back to +, as if 3 were missing.",
    (2, 4): "The second 1. A sign flip would untick slot 0 too, and the answer would come out as 1.",
    'done': "Force-negative keeps every tick. Flipping the sign answers 1 here, yet passes all three LeetCode samples.",
}
# Hard example 2: every number 1..n present, so the answer is n + 1, reached
# only by the final return. 'return n' there passes all three LeetCode samples
# (none of them contains all of 1..n) and answers 5 here. Correct: 6.
HARD_FULL = [2, 3, 4, 5, 1]
HARD_FULL_NOTES = {
    (3, 4): "The last slot is ticked too: 1 to 5 are all here. The answer must be bigger than anything in the array.",
    'done': "Only the final 'return n + 1' answers this. 'return n' passes all three LeetCode samples and says 5.",
}


def flip_sign(nums):
    """First attempt broken by HARD_DUP: flip the sign instead of forcing it negative."""
    nums, n = nums[:], len(nums)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    for i in range(n):
        val = abs(nums[i])
        if val <= n:
            nums[val - 1] = -nums[val - 1]
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    return n + 1


def return_n(nums):
    """First attempt broken by HARD_FULL: the fallback returns n, not n + 1."""
    nums, n = nums[:], len(nums)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    for i in range(n):
        val = abs(nums[i])
        if val <= n:
            nums[val - 1] = -abs(nums[val - 1])
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    return n


def trace(arr):
    events = []
    nums = arr[:]
    filler = set()

    def rec(kind, phase, **kw):
        events.append(dict(kind=kind, phase=phase, nums=nums[:], filler=set(filler), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def firstMissingPositive(nums):
        n = len(nums)
        rec('start', 0, n=n)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                old = nums[i]
                nums[i] = n + 1
                filler.add(i)
                rec('clean', 1, i=i, old=old, n=n)
            else:
                rec('keep', 1, i=i, n=n)

        for i in range(n):
            val = abs(nums[i])
            if val <= n:
                was = nums[val - 1]
                nums[val - 1] = -abs(nums[val - 1])
                rec('tick', 2, i=i, val=val, again=was < 0, n=n)
            else:
                rec('skip', 2, i=i, val=val, n=n)

        for i in range(n):
            if nums[i] > 0:
                rec('found', 3, i=i, n=n)
                return i + 1
            rec('ticked', 3, i=i, n=n)

        rec('full', 3, n=n)
        return n + 1

    ans = firstMissingPositive(nums)
    events.append(dict(events[-1], kind='done', ans=ans))
    return events, ans


def words(e, notes):
    cap, sub, hold = _words(e)
    if notes:
        key = 'done' if e['kind'] == 'done' else (e['phase'], e.get('i'))
        if key in notes and e['kind'] in ('tick', 'ticked', 'done', 'found'):
            return cap, notes[key], (END if e['kind'] == 'done' else KEY)
    return cap, sub, hold


def _words(e):
    k, n, i = e['kind'], e['n'], e.get('i')
    if k == 'start':
        return (f"n = {n}, so the answer is somewhere in 1..{n + 1}. Only values 1..{n} can matter.",
                f"Slot v-1 will answer 'is v present?': the column labels say which number each slot stands for.", KEY)
    if k == 'clean':
        if e['old'] <= 0:
            why = f"{e['old']} isn't positive"
        else:
            why = f"{e['old']} is bigger than n = {n}"
        return (f"Pass 1, slot {i}: {why}, so it can't matter. Replace it with the filler {n + 1}.",
                "Now every value is positive, so a minus sign can only mean 'ticked'.", KEY)
    if k == 'keep':
        return (f"Pass 1, slot {i}: {e['nums'][i]} is in 1..{n}. Keep it.", "", QUICK * 1.6)
    if k == 'tick':
        v = e['val']
        if e['again']:
            return (f"Pass 2, slot {i}: |{e['nums'][i]}| = {v}. Slot {v - 1} is already ticked; keep it negative.",
                    "-abs(...) forces negative. Flipping the sign would untick it.", KEY)
        return (f"Pass 2, slot {i}: value {v} is present, so tick slot {v - 1} by making it negative.",
                "Read with abs(): this slot may already carry a tick from an earlier value.", STEP)
    if k == 'skip':
        return (f"Pass 2, slot {i}: {e['val']} is the filler (> n), so it ticks nothing.", "", STEP)
    if k == 'ticked':
        return (f"Pass 3, slot {i} is negative: {i + 1} is present.", "", STEP)
    if k == 'found':
        return (f"Pass 3, slot {i} is still positive: nobody ticked it, so {i + 1} is missing.",
                "The first unticked slot is the smallest missing positive.", KEY)
    if k == 'full':
        return (f"Pass 3 found no positive slot: 1..{n} are all present.", f"So the answer is n + 1 = {n + 1}.", KEY)
    return (f"firstMissingPositive returns {e['ans']}.",
            "Three passes over the array and no extra memory: the signs were the checklist.", END)


def build(arr, subtitle, notes=None):
    events, ans = trace(arr)
    n = len(arr)
    sc = Scene('#41 First Missing Positive: the array is its own checklist', subtitle)
    legend = [(style('gold')[1], 'filler n + 1'), (style('good')[1], 'ticked (negative)'),
              (ACTIVE, 'slot being read'), (REJECT, 'first unticked slot')]
    for e in events:
        k, i = e['kind'], e.get('i')
        styles, rings, links = {}, [], []
        for c, v in enumerate(e['nums']):
            if v < 0:
                styles[(0, c)] = 'good'
            elif c in e['filler']:
                styles[(0, c)] = 'gold'
        if i is not None and k != 'done':
            rings.append(((0, i), ACTIVE))
        if k == 'tick':
            links.append(dict(src=(0, i), dst=(0, e['val'] - 1), color=style('good')[1],
                              lift=0 if i == e['val'] - 1 else -46, label=f"{e['val']}"))
        if k in ('found', 'done') and ans <= n:
            styles[(0, ans - 1)] = 'bad'
            rings.append(((0, ans - 1), REJECT))
        orig = DPTableView([arr], row_labels=['input'], col_labels=[f'slot {c}' for c in range(n)],
                           max_cell=72, gap=12)
        table = DPTableView([e['nums']], row_labels=['array'], col_labels=[f'{c + 1}?' for c in range(n)],
                            styles=styles, rings=rings, links=links, max_cell=72, gap=12)
        phase = {0: 'setup', 1: '1 clean up', 2: '2 tick', 3: '3 read'}[e['phase']]
        present = [str(c + 1) for c, v in enumerate(e['nums']) if v < 0]
        rows = [('n', str(n)), ('pass', phase if k != 'done' else 'done'),
                ('ticked so far', ', '.join(present) if present else '(none)', 'good'),
                ('answer', str(e['ans']) if k == 'done' else '?', 'bad' if k == 'done' else None)]
        rows = [r if len(r) == 2 or r[2] else r[:2] for r in rows]
        cap, sub, hold = words(e, notes)
        sc.frame([orig, table], cap, sub, hold, side=MapView(rows, 'State', headers=('', '')),
                 counters={'pass': e['phase'] if k != 'done' else '-'}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = ([1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12])
    for s in samples:                          # both first attempts pass every LeetCode sample
        assert flip_sign(s) == return_n(s) == trace(s)[1]
    assert trace(HARD_DUP)[1] == 4 and flip_sign(HARD_DUP) == 1
    assert trace(HARD_FULL)[1] == 6 and return_n(HARD_FULL) == 5
    dup = build(HARD_DUP, f'nums = {HARD_DUP}. Answer 4. Two duplicates tick the same slots twice.', HARD_DUP_NOTES)
    full = build(HARD_FULL, f'nums = {HARD_FULL}. Answer 6. Every number 1..n is present.', HARD_FULL_NOTES)
    return [
        (dup, "Duplicates: flipping the sign instead of forcing it negative passes all three LeetCode samples, "
              "then answers 1 here instead of 4. Watch the second 3 and the second 1 tick slots already ticked."),
        (full, "Every number from 1 to n is present, so no slot stays positive and only the final return can "
               "answer. Returning n there passes all three samples and says 5 instead of 6."),
    ]


def main():
    args = cli()
    sc = build(NUMS, 'Top row: the input. Bottom row: the array as it changes. "k?" = this slot answers "is k present?"')
    finish(sc, 41, "Watch pass 2 tick slots 2, 3 and 0 by making them negative: slot 1 is never ticked, "
                   "so pass 3 stops there and the answer is 2.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
