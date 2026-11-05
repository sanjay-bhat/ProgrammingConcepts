#!/usr/bin/env python3
"""#45 Jump Game II: count rounds of jumps; each round is a stretch of
consecutive squares, so two numbers (cur_end, farthest) replace a BFS queue.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [2, 3, 1, 1, 4]          # LeetCode example 1: 2 jumps

# The hard example (interactive page only): jumping to the biggest number in
# reach passes both LeetCode samples, then takes 6 jumps here instead of 4.
# From index 0 the biggest number in reach is the 2 at index 1 (reaches 3), but
# the 1 at index 3 reaches 4, and from 4 the 3 reaches 7.
HARD = [3, 2, 1, 1, 3, 2, 1, 1, 1]
HARD_NOTES = {
    ('scan', 1): "The biggest number in reach is this 2, but it only gets to index 3. Size isn't distance.",
    ('jump', 3): "The 1 at index 3 reaches 4, further than the 2 at index 1. Only i + nums[i] counts.",
    'done': "4 jumps. Jumping to the biggest number in reach takes 6 here, yet passes both LeetCode samples.",
}


def biggest_number(nums):
    """First attempt the hard example breaks: jump to the biggest number in reach (the further one on a tie)."""
    i, jumps, n = 0, 0, len(nums)
    while i < n - 1:
        if i + nums[i] >= n - 1:
            return jumps + 1
        i = max(range(i + 1, i + nums[i] + 1), key=lambda k: (nums[k], k))
        jumps += 1
    return jumps


def trace(nums):
    events = []
    n = len(nums)
    rnd = [0] + [None] * (n - 1)     # which round first reaches each square (display only)

    def rec(kind, **kw):
        events.append(dict(kind=kind, rnd=rnd[:], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    jumps = cur_end = farthest = 0
    rec('start', i=None, jumps=0, cur_end=0, farthest=0)
    for i in range(len(nums) - 1):
        before = farthest
        farthest = max(farthest, i + nums[i])
        rec('scan', i=i, jumps=jumps, cur_end=cur_end, farthest=farthest, before=before)
        if i == cur_end:
            jumps += 1
            old = cur_end
            cur_end = farthest
            for k in range(old + 1, min(cur_end, n - 1) + 1):
                rnd[k] = jumps
            rec('jump', i=i, jumps=jumps, cur_end=cur_end, farthest=farthest, old=old)
    rec('done', i=None, jumps=jumps, cur_end=cur_end, farthest=farthest)
    return events, jumps


def words(e, nums, firsts, notes):
    k = e['kind']
    key = 'done' if k == 'done' else (k, e['i'])
    cap, sub, hold = _words(e, nums, firsts)
    if notes and key in notes:
        return cap, notes[key], (END if k == 'done' else KEY)
    return cap, sub, hold


def _words(e, nums, firsts):
    k, i, n = e['kind'], e['i'], len(nums)
    if k == 'start':
        return ("Round 0 is just index 0. cur_end = 0: the last square reachable with 0 jumps.",
                "farthest will track where the NEXT round can reach.", KEY)
    if k == 'scan':
        reach = i + nums[i]
        grew = e['farthest'] > e['before']
        cap = (f"i = {i}: from here you can reach {i} + {nums[i]} = {reach}. "
               + (f"farthest grows to {e['farthest']}." if grew else f"farthest stays {e['farthest']}."))
        sub = ("Update farthest BEFORE checking the boundary: this square belongs to the current round."
               if firsts.get('scan') == i else "")
        return cap, sub, KEY if sub else STEP
    if k == 'jump':
        last = e['cur_end'] >= n - 1
        cap = (f"i = {i} is cur_end: every square of round {e['jumps'] - 1} has been seen. "
               f"Jump {e['jumps']}: cur_end = {e['cur_end']}.")
        if last:
            sub = f"Round {e['jumps']} reaches the last square, so {e['jumps']} jumps is the answer."
        elif firsts.get('jump') == i:
            sub = "No later square can be part of this round, so the next round's end is final."
        else:
            sub = ""
        return cap, sub, KEY if sub else STEP
    return (f"The loop stops before the last index. Answer: {e['jumps']} jumps.",
            "One pass and three integers: the rounds were never stored, only their right ends.", END)


def build(nums, subtitle, notes=None):
    events, ans = trace(nums)
    n = len(nums)
    firsts = {}
    for e in events:
        if e['kind'] in ('scan', 'jump'):
            firsts.setdefault(e['kind'], e['i'])
    sc = Scene('#45 Jump Game II: count rounds, not routes', subtitle)
    legend = [(ACTIVE, 'square being scanned'), (style('region1')[1], 'colour = round that reaches it'),
              (CURSOR, 'cur_end')]
    for e in events:
        k, i = e['kind'], e['i']
        styles, rings, links = {}, [], []
        for c, r in enumerate(e['rnd']):
            if r is not None:
                styles[(0, c)] = f'region{r}'
        if i is not None:
            rings.append(((0, i), ACTIVE))
            reach = min(i + nums[i], n - 1)
            if reach > i:
                links.append(dict(src=(0, i), dst=(0, reach), color=ACTIVE, lift=-36, label=f'+{nums[i]}'))
        if k != 'done' and e['cur_end'] < n:
            rings.append(((0, e['cur_end']), CURSOR))
        labels = [f'{c}' for c in range(n)]
        table = DPTableView([nums], row_labels=['value'], col_labels=labels, styles=styles, rings=rings,
                            links=links, max_cell=60, gap=12)
        rounds = DPTableView([[('-' if r is None else r) for r in e['rnd']]], row_labels=['round'],
                             col_labels=None, styles=styles, max_cell=60, gap=12)
        rows = [('i', '-' if i is None else str(i)), ('cur_end', str(e['cur_end']), 'plain'),
                ('farthest', str(e['farthest']), 'gold'), ('jumps', str(e['jumps']), 'good')]
        cap, sub, hold = words(e, nums, firsts, notes)
        sc.frame([table, rounds], cap, sub, hold, side=MapView(rows, 'Variables', headers=('', '')),
                 counters={'jumps': e['jumps']}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    for s in ([2, 3, 1, 1, 4], [2, 3, 0, 1, 4]):          # LeetCode samples
        assert biggest_number(s) == trace(s)[1]
    assert trace(HARD)[1] == 4 and biggest_number(HARD) == 6
    sc = build(HARD, f'nums = {HARD}. Answer 4. The biggest numbers in reach are traps.', HARD_NOTES)
    return sc, ("Jumping to the biggest number in reach passes both LeetCode samples, then takes 6 jumps here "
                "instead of 4. Watch round 1: the 2 at index 1 reaches less far than the 1 at index 3.")


def main():
    args = cli()
    sc = build(NUMS, 'Each number is the longest jump from that square. Arcs show how far it reaches.')
    finish(sc, 45, "Watch i reach cur_end at index 2: by then index 1 has already pushed farthest to 4, so "
                   "the second jump lands on the last square.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
