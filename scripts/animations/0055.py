#!/usr/bin/env python3
"""#55 Jump Game: one number, max_reach, says how far you could possibly get.
Every index up to it is reachable (a shorter jump is always allowed), so the
only way to fail is to walk past it.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [3, 2, 1, 0, 4]          # LeetCode example 2: false

# Hard examples (interactive page only). Two first attempts pass both LeetCode
# samples ([2,3,1,1,4] -> true, [3,2,1,0,4] -> false):
#   - "a 0 before the end means you're stuck": wrong whenever a jump clears the 0.
#     [3, 0, 0, 2, 0, 1, 0] is reachable (0 -> 3 -> 5 -> 6); it says false.
#   - "always jump as far as you can": lands on a 0 that a shorter jump avoids.
#     [2, 5, 0, 0, 0, 0, 0]: the long jump from index 0 lands on index 2, a dead end;
#     the short jump to index 1 reaches the end. It says false.
HARD1 = [3, 0, 0, 2, 0, 1, 0]
HARD1_NOTES = {
    ('scan', 1): "This 0 doesn't matter: index 0 already reaches 3, past both zeros.",
    ('scan', 3): "Index 3 was reached by jumping over the zeros. 'A 0 means stuck' would have said false already.",
    'done': "true. 'Any 0 before the end means stuck' says false here, yet passes both LeetCode samples.",
}
HARD2 = [2, 5, 0, 0, 0, 0, 0]
HARD2_NOTES = {
    ('scan', 0): "The longest jump from here lands on index 2, a 0. 'Always jump as far as you can' gets stuck there.",
    ('scan', 1): "The shorter jump to index 1 is the one that matters: 1 + 5 reaches the last index.",
    'done': "true. 'Always jump as far as you can' says false here, yet passes both LeetCode samples.",
}


def zero_attempt(nums):
    """First attempt #1: any 0 before the last index means you're stuck."""
    return 0 not in nums[:-1]


def farthest_jump_attempt(nums):
    """First attempt #2: from where you stand, always take the longest jump."""
    i = 0
    while i < len(nums) - 1:
        if nums[i] == 0:
            return False
        i += nums[i]
    return True


def trace(nums):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, reach=max_reach, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    max_reach = 0
    rec('start', i=None)
    for i, v in enumerate(nums):
        if i > max_reach:
            rec('stuck', i=i)
            return events, False
        before = max_reach
        max_reach = max(max_reach, i + v)
        rec('scan', i=i, before=before)
    rec('done', i=None)
    return events, True


def words(e, nums, firsts, notes):
    k = e['kind']
    key = 'done' if k in ('done', 'stuck') else (k, e['i'])
    cap, sub, hold = _words(e, nums, firsts)
    if notes and key in notes:
        return cap, notes[key], (END if key == 'done' else KEY)
    return cap, sub, hold


def _words(e, nums, firsts):
    k, i, n = e['kind'], e['i'], len(nums)
    if k == 'start':
        return ("Stand on index 0. max_reach = 0: so far, index 0 is the only place you can be.",
                "max_reach will track the furthest index any reachable square can jump to.", KEY)
    if k == 'scan':
        reach = i + nums[i]
        grew = e['reach'] > e['before']
        cap = (f"i = {i} ≤ max_reach, so you can stand here. It reaches {i} + {nums[i]} = {reach}: "
               + (f"max_reach grows to {e['reach']}." if grew else f"max_reach stays {e['reach']}."))
        if firsts.get('scan') == i:
            return cap, "Everything up to max_reach is reachable too: a shorter jump is always allowed.", KEY
        if nums[i] == 0 and i < n - 1:
            return cap, "A 0 can't take you anywhere, but standing on it is harmless while others reach further.", KEY
        return cap, "", STEP
    if k == 'stuck':
        return (f"i = {i} is past max_reach = {e['reach']}. Nothing before it can jump this far.",
                f"Index {i} is unreachable, so the last index is too. Return false.", END)
    return (f"Every index up to {n - 1} was within reach. Return true.",
            "One pass and one number: no route was ever chosen, only how far you could get.", END)


def build(nums, subtitle, notes=None):
    events, ans = trace(nums)
    n = len(nums)
    firsts = {}
    for e in events:
        if e['kind'] == 'scan':
            firsts.setdefault('scan', e['i'])
    sc = Scene(f'#55 Jump Game: is the last index reachable?', subtitle)
    legend = [(ACTIVE, 'index being checked'), (style('window')[1], 'within max_reach'),
              (style('bad')[1], 'past max_reach'), (CURSOR, 'max_reach')]
    for e in events:
        k, i = e['kind'], e['i']
        styles, rings, links = {}, [], []
        for c in range(n):
            if c <= e['reach']:
                styles[(0, c)] = 'window'
        if k == 'stuck':
            for c in range(e['reach'] + 1, n):
                styles[(0, c)] = 'bad'
        if k == 'done':
            styles[(0, n - 1)] = 'good'
        if i is not None:
            rings.append(((0, i), ACTIVE))
            reach = min(i + nums[i], n - 1)
            if k == 'scan' and reach > i:
                links.append(dict(src=(0, i), dst=(0, reach), color=ACTIVE, lift=-36, label=f'+{nums[i]}'))
        if e['reach'] < n and k != 'done':
            rings.append(((0, min(e['reach'], n - 1)), CURSOR))
        table = DPTableView([nums], row_labels=['nums'], col_labels=[str(c) for c in range(n)], styles=styles,
                            rings=rings, links=links, max_cell=60, gap=12)
        rows = [('i', '-' if i is None else str(i)), ('nums[i]', '-' if i is None else str(nums[i])),
                ('max_reach', str(e['reach']), 'gold'), ('last index', str(n - 1))]
        if k in ('stuck', 'done'):
            rows.append(('answer', 'false' if k == 'stuck' else 'true', 'bad' if k == 'stuck' else 'good'))
        cap, sub, hold = words(e, nums, firsts, notes)
        sc.frame(table, cap, sub, hold, side=MapView(rows, 'Variables', headers=('', '')),
                 counters={'max_reach': e['reach']}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    for s in ([2, 3, 1, 1, 4], [3, 2, 1, 0, 4]):                     # LeetCode samples
        assert zero_attempt(s) == farthest_jump_attempt(s) == trace(s)[1]
    assert trace(HARD1)[1] is True and zero_attempt(HARD1) is False
    assert trace(HARD2)[1] is True and farthest_jump_attempt(HARD2) is False
    one = build(HARD1, f'nums = {HARD1}. Two zeros right after the start, and another near the end.', HARD1_NOTES)
    two = build(HARD2, f'nums = {HARD2}. The longest first jump is a trap.', HARD2_NOTES)
    return [(one, "'Any 0 before the end means stuck' passes both samples and says false here. Watch index 0 "
                  "reach past both zeros, so they never matter."),
            (two, "'Always jump as far as you can' passes both samples, then jumps from index 0 straight onto "
                  "a 0. max_reach never picks a jump, so the 5 at index 1 still counts.")]


def main():
    args = cli()
    sc = build(NUMS, 'Each number is the longest jump from that square. Arcs show how far it reaches.')
    finish(sc, 55, "Watch max_reach stall at 3: every square up to the 0 reaches exactly index 3, so when i "
                   "reaches 4 it's past max_reach, and the answer is false.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
