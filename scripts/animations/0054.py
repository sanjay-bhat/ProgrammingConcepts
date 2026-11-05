#!/usr/bin/env python3
"""#54 Spiral Matrix: four walls (top, bottom, left, right) close in. Each
pass walks along one wall and moves it inward; the two checks in the middle
of the loop stop a pass from re-walking a row or column already taken.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged (the two `else` branches only record
that a check skipped its pass).
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

MATRIX = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]      # LeetCode example 2

# The hard example (interactive page only): a tall 5x3 matrix. Guarding only the
# leftward pass (`if top <= bottom`) and not the upward one passes both LeetCode
# samples, which are 3 rows tall, and fails here: on the last lap only the middle
# column is left, the upward pass walks it again and 8 is taken twice
# (16 values instead of 15).
HARD = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
HARD_NOTES = {
    ('down', (3, 1)): "Only the middle column was left, and the downward pass just took all of it.",
    ('guard', 'left'): "Without this check the upward pass walks column 1 again and takes 8 twice: 16 values, not 15.",
    'done': "15 values. Guarding only the leftward pass gives 16 here, yet passes both 3-row samples.",
}


def bottom_guard_only_attempt(matrix):
    """First attempt: the notebook's loop with the `if left <= right` check left out."""
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        for row in range(bottom, top - 1, -1):
            result.append(matrix[row][left])
        left += 1
    return result


def trace(matrix):
    events = []
    order = {}                       # display only: (r, c) -> (visit number, pass)

    def rec(kind, **kw):
        events.append(dict(kind=kind, result=list(result), order=dict(order),
                           walls=(top, bottom, left, right), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    rec('start')

    while top <= bottom and left <= right:
        rec('lap')
        before = len(result)
        # Traverse right across the top boundary row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
            order[(top, col)] = (len(result), 'right')
            rec('right', cell=(top, col))
        top += 1
        rec('wall', wall='top', took=len(result) - before)
        before = len(result)
        # Traverse down along the right boundary column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
            order[(row, right)] = (len(result), 'down')
            rec('down', cell=(row, right))
        right -= 1
        rec('wall', wall='right', took=len(result) - before)
        before = len(result)
        # Traverse left across the bottom boundary row (guard against single row)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
                order[(bottom, col)] = (len(result), 'left')
                rec('left', cell=(bottom, col))
            bottom -= 1
            rec('wall', wall='bottom', took=len(result) - before)
            before = len(result)
        else:
            rec('guard', which='bottom')
        # Traverse up along the left boundary column (guard against single column)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
                order[(row, left)] = (len(result), 'up')
                rec('up', cell=(row, left))
            left += 1
            rec('wall', wall='left', took=len(result) - before)
        else:
            rec('guard', which='left')
    rec('done')
    return events, result


PASS_STYLE = {'right': 'region2', 'down': 'region0', 'left': 'region3', 'up': 'region4'}
ARROW = {'right': '→', 'down': '↓', 'left': '←', 'up': '↑'}


def words(e, m, firsts, notes):
    k = e['kind']
    key = 'done' if k == 'done' else (('guard', e['which']) if k == 'guard' else
                                      (k, e.get('cell', e.get('wall'))))
    cap, sub, hold = _words(e, m, firsts)
    if notes and key in notes:
        return cap, notes[key], (END if k == 'done' else KEY)
    return cap, sub, hold


def _words(e, m, firsts):
    k = e['kind']
    top, bottom, left, right = e['walls']
    if k == 'start':
        return ("Four walls: top, bottom, left and right. Everything between them is still to visit.",
                "Each pass walks along one wall, then moves that wall one step inward.", KEY)
    if k == 'lap':
        return (f"New lap: rows {top}–{bottom}, columns {left}–{right} are left.", "", QUICK * 2)
    if k in ARROW:
        r, c = e['cell']
        what = {'right': 'right along the top row', 'down': 'down the right column',
                'left': 'left along the bottom row', 'up': 'up the left column'}[k]
        return (f"Go {what}: take {m[r][c]}.", "", QUICK * 1.8)
    if k == 'wall':
        w = e['wall']
        val = {'top': top, 'bottom': bottom, 'left': left, 'right': right}[w]
        line = 'row' if w in ('top', 'bottom') else 'column'
        if not e['took']:
            return (f"That pass had nothing left to take, but the {w} wall still moves in, to {val}.",
                    "", STEP)
        cap = f"That {w} {line} is used up: {w} moves to {val}."
        if firsts.get('wall') == id(e):
            return cap, "The walls are the only memory: anything outside them has been taken.", KEY
        return cap, "", QUICK * 2
    if k == 'guard':
        if e['which'] == 'bottom':
            return (f"Check: top ({top}) > bottom ({bottom}). No row is left between the walls.",
                    f"So skip the leftward pass. Without the check it would walk row {bottom} again.", KEY)
        return (f"Check: left ({left}) > right ({right}). No column is left between the walls.",
                f"So skip the upward pass. Without the check it would walk column {left - 1} again.", KEY)
    return (f"The walls have crossed, so the loop stops. {len(e['result'])} values, each taken once.",
            "Every cell is visited exactly once: O(m×n) time, four integers of bookkeeping.", END)


def build(m, subtitle, notes=None):
    events, _ = trace(m)
    R, C = len(m), len(m[0])
    firsts = {}
    for e in events:
        if e['kind'] == 'wall' and 'wall' not in firsts:
            firsts['wall'] = id(e)
    sc = Scene('#54 Spiral Matrix: walk the walls, move them in', subtitle)
    legend = [(style(PASS_STYLE[d])[1], f'{ARROW[d]} pass') for d in ('right', 'down', 'left', 'up')] + \
             [(style('window')[1], 'still inside the walls')]
    for e in events:
        k = e['kind']
        top, bottom, left, right = e['walls']
        cells = []
        for r in range(R):
            row = []
            for c in range(C):
                if (r, c) in e['order']:
                    n, d = e['order'][(r, c)]
                    row.append({'style': PASS_STYLE[d], 'label': str(m[r][c]), 'sub': f'#{n} {ARROW[d]}'})
                elif top <= r <= bottom and left <= c <= right:
                    row.append({'style': 'window', 'label': str(m[r][c])})
                else:
                    row.append({'style': 'plain', 'label': str(m[r][c])})
            cells.append(row)
        rings = []
        if 'cell' in e:
            rings.append((e['cell'], ACTIVE, 5))
        marks = {}
        rows = [('top', str(top), 'gold' if e.get('wall') == 'top' else 'plain'),
                ('bottom', str(bottom), 'gold' if e.get('wall') == 'bottom' else 'plain'),
                ('left', str(left), 'gold' if e.get('wall') == 'left' else 'plain'),
                ('right', str(right), 'gold' if e.get('wall') == 'right' else 'plain')]
        if k == 'guard':
            rows.append(('check', 'top <= bottom ✗' if e['which'] == 'bottom' else 'left <= right ✗', 'bad'))
        chips = ChipsView([(str(v), 'good') for v in e['result']], 'result so far', empty='(empty)', size=12 if R * C > 12 else 14)
        cap, sub, hold = words(e, m, firsts, notes)
        sc.frame([GridView(cells, outlines=rings, marks=marks, bridges=False, cell=64 if R <= 3 else 42), chips],
                 cap, sub, hold, side=MapView(rows, 'Walls', headers=('wall', 'index')),
                 counters={'taken': f'{len(e["result"])}/{R * C}'}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    for s in ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], MATRIX):          # LeetCode samples
        assert bottom_guard_only_attempt(s) == trace(s)[1]
    assert trace(HARD)[1] == [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]
    assert bottom_guard_only_attempt(HARD) == [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11, 8]
    sc = build(HARD, 'A tall 5×3 matrix: the last lap is a single column, and a single column can be walked twice.',
               HARD_NOTES)
    return sc, ("A tall matrix. Leaving out the `left <= right` check passes both LeetCode samples (3 rows "
                "each), then takes 8 twice here. Watch the last lap: only the middle column is left.")


def main():
    args = cli()
    sc = build(MATRIX, 'LeetCode example 2. Shaded cells are still inside the walls; #n is the order taken.')
    finish(sc, 54, "Watch the second lap: only the middle row is left, and the check top <= bottom stops the "
                   "leftward pass from walking it a second time.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
