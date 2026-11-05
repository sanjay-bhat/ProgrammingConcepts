#!/usr/bin/env python3
"""#57 Insert Interval: copy what ends before the new interval, absorb what
starts by its end, append it, copy the rest.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import copy
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

INTERVALS, NEW = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]   # LeetCode example 2

# Hard examples (interactive page only), each breaking a plausible first attempt.
# 1) Touching on both sides. `<=` in the "before" test copies [3,5] as if it
#    didn't touch [5,7] and returns [[1,2],[3,5],[5,9]]. Answer [[1,2],[3,9]].
HARD_TOUCH = ([[1, 2], [3, 5], [7, 9]], [5, 7])
# 2) The merged interval is the last thing in the list. Adding the new interval
#    only when a later interval shows up never adds it: [[1,2]]. Answer [[1,2],[4,12]].
HARD_END = ([[1, 2], [4, 6], [8, 10]], [5, 12])


class Solution:
    """The notebook's solution, to cross-check the traced run."""
    def insert(self, intervals, new_interval):
        result = []
        i, n = 0, len(intervals)
        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
        result.append(new_interval)
        while i < n:
            result.append(intervals[i])
            i += 1
        return result


def before_with_le(intervals, new_interval):
    """First attempt: `<=` in the before test, so touching intervals are copied."""
    result, i, n = [], 0, len(intervals)
    while i < n and intervals[i][1] <= new_interval[0]:
        result.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
        i += 1
    return result + [new_interval] + intervals[i:]


def add_when_later_seen(intervals, new_interval):
    """First attempt: one loop, add the new interval when a later one appears."""
    result, added = [], False
    for s, e in intervals:
        if e < new_interval[0]:
            result.append([s, e])
        elif s > new_interval[1]:
            if not added:
                result.append(new_interval); added = True
            result.append([s, e])
        else:
            new_interval = [min(s, new_interval[0]), max(e, new_interval[1])]
    return result


def trace(intervals, new):
    intervals, new_interval = copy.deepcopy(intervals), list(new)
    events, phase = [], {}

    def rec(kind, **kw):
        events.append(dict(kind=kind, i=i, new=list(new_interval), phase=dict(phase),
                           result=[list(x) for x in result], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    result = []
    i, n = 0, len(intervals)
    rec('start')
    while i < n and intervals[i][1] < new_interval[0]:
        phase[i] = 'before'
        result.append(intervals[i])
        rec('copy')
        i += 1
    rec('stop1')
    while i < n and intervals[i][0] <= new_interval[1]:
        old = list(new_interval)
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        phase[i] = 'merged'
        rec('absorb', old=old)
        i += 1
    rec('stop2')
    result.append(new_interval)
    rec('append')
    while i < n:
        phase[i] = 'after'
        result.append(intervals[i])
        rec('copy3')
        i += 1
    rec('done')
    assert result == Solution().insert(copy.deepcopy(intervals), list(new))
    return events, intervals


STY = {'before': 'muted', 'merged': 'gold', 'after': 'window'}
fmt = lambda p: f'[{p[0]},{p[1]}]'


def words(e, iv, first):
    k, i, nw = e['kind'], e['i'], e['new']
    n = len(iv)
    if k == 'start':
        return (f"New interval {fmt(nw)}. Walk the sorted list once with index i.",
                "Three groups, in order: ends before it, touches it, starts after it.", STEP)
    if k == 'copy':
        s, t = iv[i]
        return (f"{fmt(iv[i])} ends at {t}, before {nw[0]}: it can't touch. Copy it.", "", STEP)
    if k == 'stop1':
        if i == n:
            return ("Every interval ended before the new one starts.", "Nothing to absorb.", KEY)
        s, t = iv[i]
        return (f"{fmt(iv[i])} ends at {t}, not before {nw[0]}. Stop copying.",
                "It's strict <: an interval ending exactly at the new start touches it.", KEY)
    if k == 'absorb':
        s, t = iv[i]
        old = e['old']
        touch = s == old[1]
        cap = f"{fmt(iv[i])} starts at {s}, ≤ {old[1]}: it overlaps. Stretch to {fmt(nw)}."
        if touch:
            return (cap, f"{s} = {old[1]}: the two only touch, and touching counts. That's why it's ≤.", KEY)
        return (cap, "Smaller start, larger end." if first else "", STEP)
    if k == 'stop2':
        if i == n:
            return ("The list ran out while merging.", "Nothing comes after the new interval.", KEY)
        s, t = iv[i]
        return (f"{fmt(iv[i])} starts at {s}, after {nw[1]}. The overlapping run is over.",
                "The list is sorted, so nothing further on can touch it either.", STEP)
    if k == 'append':
        return (f"Append {fmt(nw)}, outside every loop.",
                "Unconditional: it's added even if nothing comes after it.", KEY)
    if k == 'copy3':
        return (f"{fmt(iv[i])} starts after the merged end. Copy it as it is.", "", STEP)
    return (f"Answer: {' '.join(fmt(r) for r in e['result'])}.",
            "Each interval looked at once: O(n) time, and only the output as memory.", END)


def build(intervals, new, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#57 Insert Interval: before, overlap, after', subtitle, side_width=250)
    legend = [(style('muted')[1], 'copied before'), (style('gold')[1], 'absorbed'),
              (style('window')[1], 'copied after'), (ACTIVE, 'new interval'), (style('good')[1], 'appended')]
    events, iv = trace(intervals, new)
    hi = max(x for p in iv + [new] for x in p) + 1
    first_absorb = True
    for e in events:
        k, i = e['kind'], e['i']
        bars = []
        for j, (s, t) in enumerate(iv):
            st = STY.get(e['phase'].get(j), 'plain')
            if j == i and k in ('copy', 'stop1', 'absorb', 'stop2', 'copy3'):
                st = 'active' if k in ('stop1', 'stop2') else st
            bars.append((s, t, fmt([s, t]), st))
        nw = e['new']
        bars.append((nw[0], nw[1], 'new ' + fmt(nw), 'good' if k in ('append', 'copy3', 'done') else 'active'))
        chips = [(fmt(r), 'good' if r == nw and k in ('append', 'copy3', 'done') else
                  'window' if any(x == r and e['phase'].get(j) == 'after' for j, x in enumerate(iv)) else 'plain')
                 for r in e['result']]
        cap, sub, hold = words(e, iv, first_absorb)
        if k == 'absorb':
            first_absorb = False
        key = (k, i)
        if key in notes:
            sub, hold = notes[key], (END if k == 'done' else KEY)
        rows = [('i', str(i) if i < len(iv) else f'{i} (end)'), ('new_interval', fmt(nw))]
        if i < len(iv) and k not in ('start', 'append', 'done'):
            rows.append(('current', fmt(iv[i]), 'active'))
        main = [IntervalView(bars, lo=0, hi=hi, title='intervals (one per row), new interval last'),
                ChipsView(chips, title='result', empty='(nothing yet)')]
        sc.frame(main, cap, sub, hold, side=MapView(rows, 'State', headers=('name', 'value')), legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    iv, nw = HARD_TOUCH
    assert Solution().insert(copy.deepcopy(iv), list(nw)) == [[1, 2], [3, 9]]
    assert before_with_le(copy.deepcopy(iv), list(nw)) == [[1, 2], [3, 5], [5, 9]]
    touch = build(iv, nw, 'intervals = [[1,2],[3,5],[7,9]], new = [5,7]. Answer [[1,2],[3,9]].', {
        ('stop1', 1): "[3,5] ends at 5, exactly where [5,7] starts. With <= here it would be copied, "
                      "and the answer would hold [3,5] and [5,9], two intervals sharing the point 5.",
        ('absorb', 2): "[7,9] starts at 7, exactly where the new interval ends. Touching counts, so it's "
                       "absorbed: < here would leave it outside.",
    })
    iv2, nw2 = HARD_END
    assert Solution().insert(copy.deepcopy(iv2), list(nw2)) == [[1, 2], [4, 12]]
    assert add_when_later_seen(copy.deepcopy(iv2), list(nw2)) == [[1, 2]]
    end = build(iv2, nw2, 'intervals = [[1,2],[4,6],[8,10]], new = [5,12]. Answer [[1,2],[4,12]].', {
        ('stop2', 3): "The list ran out while merging: no interval comes after [4,12]. A version that adds the new "
                      "interval only when it meets a later one never adds it.",
        ('append', 3): "Append [4,12] anyway. That one unconditional line is the difference between "
                       "[[1,2],[4,12]] and [[1,2]].",
    })
    return [
        (touch, "The new [5,7] touches [3,5] at 5 and [7,9] at 7. With <= in the first test, [3,5] is copied "
                "untouched and the answer is [[1,2],[3,5],[5,9]]; the right answer is [[1,2],[3,9]]."),
        (end, "The merged interval is the last thing in the list. Adding the new interval only when a later "
              "interval shows up returns [[1,2]]; the right answer is [[1,2],[4,12]]."),
    ]


def main():
    args = cli()
    sc = build(INTERVALS, NEW, f'intervals = {INTERVALS}, newInterval = {NEW}. Sorted, no overlaps of their own.')
    finish(sc, 57, "Watch [8,10]: it starts exactly where the stretched interval ends, and because touching "
                   "counts, it's absorbed too.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
