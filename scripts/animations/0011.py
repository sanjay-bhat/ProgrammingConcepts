#!/usr/bin/env python3
"""#11 Container With Most Water: start wide, then throw away the shorter wall.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

HEIGHT = [1, 8, 6, 2, 5, 4, 8, 3, 7]          # LeetCode example 1

# Hard example (interactive page only): the two 9s sit inside tied 2s.
# Answer 27; stopping when the walls tie gives 10.
HARD = [2, 9, 1, 1, 9, 2]


def trace(height):
    events, log = [], []
    st = {'left': None, 'right': None, 'best': 0}

    def rec(kind, **kw):
        events.append(dict(kind=kind, log=list(log), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    left, right = 0, len(height) - 1
    max_water = 0
    st.update(left=left, right=right)
    rec('start')
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        grew = water > max_water                                   # display only
        max_water = max(max_water, water)
        st['best'] = max_water
        if height[left] < height[right]:
            drop = 'left'                                          # display only
        else:
            drop = 'tie' if height[left] == height[right] else 'right'
        log.append((left, right, water, grew))
        rec('measure', water=water, grew=grew, drop=drop)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        st.update(left=left, right=right)
    rec('done')
    assert max_water == Solution().maxArea(height)
    return events


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


def stop_on_tie(height):
    """First attempt: when the two walls tie, neither is 'shorter', so stop."""
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        max_water = max(max_water, min(height[left], height[right]) * (right - left))
        if height[left] == height[right]:
            break
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


def words(e, h, notes, first):
    k, L, R = e['kind'], e['left'], e['right']
    if k == 'start':
        return ("Start with the widest bucket: the two end walls.",
                "Each round: measure the water, then throw away the shorter wall.", KEY)
    if k == 'measure':
        lvl = min(h[L], h[R])
        head = f"Walls {L} and {R}: level min({h[L]}, {h[R]}) = {lvl}, width {R - L}, water {e['water']}."
        if e['drop'] == 'tie':
            tail = " The best bucket!" if first == 'best' else ""
            if first == 'first_tie' and 'tie' in notes:
                return (head, notes['tie'], KEY)
            return (head + tail, "A tie: both walls have had their best shot. Drop the right one (either is safe).",
                    KEY)
        side, i = ('left', L) if e['drop'] == 'left' else ('right', R)
        if first == 'first':
            why = (f"Wall {i} ({h[i]}) is shorter. Every other bucket it makes is narrower and still "
                   f"capped at {h[i]}, so drop it.")
            return (head, why, KEY)
        if first == 'best':
            return (head + " The best bucket!",
                    f"Nothing later beats it. Wall {i} ({h[i]}) is shorter, so it's the one to drop.", KEY)
        tail = " New best!" if e['grew'] else ""
        return (head + tail, f"Wall {i} ({h[i]}) is shorter: drop it, move {side} inward.", STEP)
    a, b, w, _ = max(e['log'], key=lambda x: x[2])
    return (f"The pointers meet. Best bucket: walls {a} and {b}, water {w}.",
            notes.get('done', f"{len(e['log'])} rounds for {len(h)} walls: each round threw one wall away."), END)


def skyline(h, e):
    """Bars as a grid: one column per wall, one row per unit of height, then a
    row of heights and a row of indices."""
    top = max(h)
    k, L, R = e['kind'], e['left'], e['right']
    if k == 'done':
        L, R = max(e['log'], key=lambda x: x[2])[:2]     # show the best bucket again
    lvl = min(h[L], h[R]) if k in ('measure', 'done') else 0
    walls = 'good' if k == 'done' else 'active'
    rows = []
    for r in range(top):
        y = top - r                     # height this row represents
        row = []
        for c, v in enumerate(h):
            gone = k not in ('done',) and not (L <= c <= R)
            if v >= y:
                row.append({'style': walls if c in (L, R) else ('bad' if gone else 'land')})
            elif L < c < R and y <= lvl:
                row.append({'style': 'window'})
            else:
                row.append({'style': 'muted'})
        rows.append(row)
    rows.append([{'style': walls if c in (L, R) else 'plain', 'label': v} for c, v in enumerate(h)])
    rows.append([{'style': walls if c in (L, R) else 'muted', 'label': c} for c in range(len(h))])
    return rows


def build(h, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#11 Container With Most Water: two pointers', subtitle)
    legend = [(ACTIVE, 'left / right walls'), (style('window')[1], 'water in this bucket'),
              (style('land')[1], 'still in play'), (style('bad')[1], 'thrown away')]
    events = trace(h)
    best_round = max((i for i, e in enumerate(events) if e['kind'] == 'measure'),
                     key=lambda i: events[i]['water'])
    seen_first = seen_tie = False
    rows_n = max(h) + 2
    cell = min(32, (366 - 4 * (rows_n - 1)) // rows_n)
    for i, e in enumerate(events):
        first = None
        if e['kind'] == 'measure' and not seen_first and e['drop'] != 'tie':
            first, seen_first = 'first', True
        elif i == best_round:
            first = 'best'
        elif e['kind'] == 'measure' and e['drop'] == 'tie' and not seen_tie:
            first, seen_tie = 'first_tie', True
        grid = GridView(skyline(h, e), bridges=False, indices=False, cell=cell)
        top = max((x[2] for x in e['log']), default=None)
        rows = [(f'walls {a}, {b}', f'{min(h[a], h[b])} × {b - a} = {w}',
                 'good' if w == top and e['kind'] == 'done' else ('active' if j == len(e['log']) - 1
                                                                  and e['kind'] == 'measure' else None))
                for j, (a, b, w, _) in enumerate(e['log'])]
        cap, sub, hold = words(e, h, notes, first)
        sc.frame(grid, cap, sub, hold,
                 side=MapView(rows, 'Buckets measured', headers=('pair', 'level × width'),
                              empty='(none yet)'),
                 counters={'best': e['best']}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    assert Solution().maxArea(HARD) == 27 and stop_on_tie(HARD) == 10
    sc = build(HARD, 'height = [2, 9, 1, 1, 9, 2]. Answer 27. Stopping when the walls tie gives 10.', {
        'tie': "A tie. Stopping here would answer 10, but the tall 9s are further in. Drop one and keep going.",
        'done': "Both 2s were dropped on ties, and that's what let the pointers reach the two 9s.",
    })
    return sc, ("The end walls tie at 2, and the two 9s hide inside them. A first attempt that stops on a tie "
                "answers 10; moving past the tie reaches the 9s, 3 apart, for 27.")


def main():
    args = cli()
    sc = build(HEIGHT, f'height = {HEIGHT}. Pick two walls that hold the most water.')
    finish(sc, 11, "Watch the first round: the wall of height 1 is shorter, so every other bucket it could "
                   "make is worse, and it's thrown away for good.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
