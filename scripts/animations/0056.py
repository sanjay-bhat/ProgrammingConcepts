#!/usr/bin/env python3
"""#56 Merge Intervals: sort by start, then each interval either overlaps the
LAST merged block (extend its end with max) or starts a new block.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Which block each input interval
joins is recorded for display only.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

INTERVALS = [[1, 3], [2, 6], [8, 10], [15, 18]]       # LeetCode example 1

# Hard examples (interactive page only). Two first attempts pass all three
# LeetCode samples ([[1,3],[2,6],[8,10],[15,18]], [[1,4],[4,5]], [[4,7],[1,4]]):
#   - on overlap, set the end to the new interval's end instead of the max.
#     A long interval that swallows short ones shrinks: [[1,10],[2,3],[4,5],[6,12]]
#     gives [[1,3],[4,5],[6,12]] instead of [[1,12]].
#   - sort by END instead of start. [[2,3],[4,5],[6,7],[8,9],[1,10]] is already in
#     end order, so the long [1,10] comes last and only merges with [8,9], keeping
#     that block's start: [[2,3],[4,5],[6,7],[8,10]] instead of [[1,10]].
HARD1 = [[1, 10], [2, 3], [4, 5], [6, 12]]
HARD1_NOTES = {
    ('merge', 1): "[2,3] sits inside [1,10]. Setting the end to 3 instead of the max would cut the block short.",
    ('merge', 2): "Still inside: the end stays 10. With 'end = new end' this would already be a separate block.",
    'done': "[[1,12]]. Taking the new end instead of the max gives [[1,3],[4,5],[6,12]], yet passes all 3 samples.",
}
HARD2 = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
HARD2_NOTES = {
    'sorted': "Sorted by START, [1,10] moves to the front. Sorted by end, it would stay last and arrive too late.",
    ('merge', 1): "[2,3] starts inside [1,10]: merged, and the end stays 10.",
    'done': "[[1,10]]. Sorting by end gives [[2,3],[4,5],[6,7],[8,10]], yet passes all 3 samples.",
}


def new_end_attempt(intervals):
    """First attempt #1: on overlap, take the new interval's end instead of the max."""
    intervals = sorted([iv[:] for iv in intervals])
    result = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = end
        else:
            result.append([start, end])
    return result


def sort_by_end_attempt(intervals):
    """First attempt #2: sort by end instead of start, then merge as usual."""
    intervals = sorted([iv[:] for iv in intervals], key=lambda x: x[1])
    result = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result


def trace(given):
    intervals = [iv[:] for iv in given]
    events = []
    shown, block = [], []            # display only: the sorted input, and which block each joined

    def rec(kind, **kw):
        events.append(dict(kind=kind, shown=[iv[:] for iv in shown], block=list(block),
                           result=[r[:] for r in result], **kw))

    result = []
    shown = [iv[:] for iv in intervals]
    rec('start')
    # ---- the notebook's solution, with rec() calls added ----
    intervals.sort(key=lambda x: x[0])
    shown = [iv[:] for iv in intervals]
    rec('sorted', moved=shown != [iv[:] for iv in given])
    result = [intervals[0]]
    block = [0]
    rec('first')
    for idx, (start, end) in enumerate(intervals[1:], 1):
        if start <= result[-1][1]:
            old = result[-1][1]
            result[-1][1] = max(result[-1][1], end)
            block.append(len(result) - 1)
            rec('merge', i=idx, old=old)
        else:
            result.append([start, end])
            block.append(len(result) - 1)
            rec('new', i=idx)
    rec('done')
    return events, result


def fmt(iv):
    return f'[{iv[0]},{iv[1]}]'


def words(e, firsts, notes):
    k = e['kind']
    key = k if k in ('start', 'sorted', 'first', 'done') else (k, e['i'])
    cap, sub, hold = _words(e, firsts)
    if notes and key in notes:
        return cap, notes[key], (END if k == 'done' else KEY)
    return cap, sub, hold


def _words(e, firsts):
    k = e['kind']
    if k == 'start':
        return ("Merge every group of overlapping intervals into one.",
                "In this order, an interval could overlap anything. Sorting fixes that.", STEP)
    if k == 'sorted':
        if e['moved']:
            return ("Sort by start.", "Now anything that overlaps the current block comes right after it.", KEY)
        return ("Sort by start (this input already is).",
                "Now anything that overlaps the current block comes right after it.", KEY)
    if k == 'first':
        return (f"The first interval {fmt(e['shown'][0])} starts the first block.",
                "The orange line marks where the last block currently ends.", STEP)
    if k == 'done':
        return (f"Done: {' '.join(fmt(r) for r in e['result'])}.",
                "One sort, then one pass: O(n log n), and the sort is the expensive part.", END)
    iv = e['shown'][e['i']]
    last = e['result'][-1]
    if k == 'merge':
        cap = f"{fmt(iv)} starts at {iv[0]} ≤ {e['old']}, the last block's end: overlap. End = max({e['old']}, {iv[1]}) = {last[1]}."
        if iv[1] < e['old']:
            return cap, "It's inside the block, so the end stays. Taking the new end would shrink the block.", KEY
        if iv[0] == e['old']:
            return cap, "Touching counts: they share the point " + str(iv[0]) + ", so the check is ≤, not <.", KEY
        if firsts.get('merge') == e['i']:
            return cap, "Starts are sorted, so only the LAST block can overlap it. Earlier blocks end before.", KEY
        return cap, "", STEP
    if k == 'new':
        prev = e['result'][-2]
        return (f"{fmt(iv)} starts at {iv[0]} > {prev[1]}: a gap. The last block is finished; start a new one.",
                "Every later interval starts even further right, so nothing can reach back into it.", STEP)


def build(given, subtitle, notes=None):
    events, _ = trace(given)
    firsts = {}
    for e in events:
        if e['kind'] == 'merge':
            firsts.setdefault('merge', e['i'])
    lo = min(s for s, _ in given)
    hi = max(t for _, t in given)
    sc = Scene('#56 Merge Intervals: sort by start, then extend or start a block', subtitle)
    legend = [(ACTIVE, 'interval being checked'), (style('region0')[1], 'colour = the block it joined'),
              (ACTIVE, 'line = end of last block')]
    for e in events:
        k = e['kind']
        bars = []
        for j, iv in enumerate(e['shown']):
            if j < len(e['block']):
                st = f'region{e["block"][j]}'
            else:
                st = 'plain'
            if k in ('merge', 'new') and j == e['i']:
                st = 'active'
            bars.append((iv[0], iv[1], fmt(iv), st))
        marker = e['result'][-1][1] if e['result'] and k not in ('done',) else None
        title = 'input, sorted by start' if k != 'start' else 'input, as given'
        view = IntervalView(bars, lo=lo, hi=hi, title=title, marker=marker)
        rows = [(f'block {b + 1}', fmt(r), f'region{b}') for b, r in enumerate(e['result'])]
        cap, sub, hold = words(e, firsts, notes)
        sc.frame(view, cap, sub, hold, side=MapView(rows, 'result', headers=('', 'interval'),
                                                     empty='(empty)'),
                 counters={'blocks': len(e['result'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 4], [4, 5]], [[4, 7], [1, 4]])
    for s in samples:
        assert new_end_attempt(s) == sort_by_end_attempt(s) == trace(s)[1]
    assert trace(HARD1)[1] == [[1, 12]] and new_end_attempt(HARD1) == [[1, 3], [4, 5], [6, 12]]
    assert trace(HARD2)[1] == [[1, 10]] and sort_by_end_attempt(HARD2) == [[2, 3], [4, 5], [6, 7], [8, 10]]
    one = build(HARD1, f'intervals = {HARD1}. A long interval swallows two short ones.', HARD1_NOTES)
    two = build(HARD2, f'intervals = {HARD2}. The interval that covers everything comes last.', HARD2_NOTES)
    return [(one, "Setting the end to the new interval's end instead of the max passes all three samples, then "
                  "splits this into three blocks. Watch [2,3] arrive inside [1,10]."),
            (two, "Sorting by end instead of start passes all three samples, then leaves [1,10] last, where it "
                  "can only stretch [8,9] to [8,10]. Watch the sort move it to the front.")]


def main():
    args = cli()
    sc = build(INTERVALS, 'Each bar is one interval on the number line. Overlapping bars should become one block.')
    finish(sc, 56, "Watch [2,6] arrive: it starts before the last block ends at 3, so the block stretches to 6; "
                   "[8,10] starts after 6, so a new block begins.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
