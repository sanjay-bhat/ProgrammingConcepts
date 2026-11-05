#!/usr/bin/env python3
"""#48 Rotate Image: a quarter turn clockwise is two mirror images in a row,
first across the main diagonal (transpose), then left to right (reverse each row).

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Cells are coloured by the row they
started in, so you can watch row 0 become the last column.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]          # LeetCode example 1

# The hard example (interactive page only): a 5x5 picture of an arrow pointing
# right (0 = background). A clockwise quarter turn must make it point DOWN.
# Two first attempts that use the same two steps get it wrong:
#   - transpose, then reverse the ORDER of the rows: a counter-clockwise turn,
#     the arrow points up;
#   - transpose with j running over every column: each pair is swapped twice,
#     so the transpose undoes itself and only the left-right mirror is left,
#     the arrow points left.
HARD = [[0, 0, 1, 0, 0],
        [0, 0, 0, 2, 0],
        [3, 4, 5, 6, 7],
        [0, 0, 0, 8, 0],
        [0, 0, 9, 0, 0]]
HARD_DOWN = [[0, 0, 3, 0, 0], [0, 0, 4, 0, 0], [9, 0, 5, 0, 1], [0, 8, 6, 2, 0], [0, 0, 7, 0, 0]]
HARD_UP = [[0, 0, 7, 0, 0], [0, 2, 6, 8, 0], [1, 0, 5, 0, 9], [0, 0, 4, 0, 0], [0, 0, 3, 0, 0]]
HARD_LEFT = [[0, 0, 1, 0, 0], [0, 2, 0, 0, 0], [7, 6, 5, 4, 3], [0, 8, 0, 0, 0], [0, 0, 9, 0, 0]]
HARD_NOTES = {
    'start': "Clockwise, the tip at the right edge must end at the bottom: the arrow should point down.",
    ('swap', (2, 4)): "The tip 7 jumps from (2,4) to (4,2). Halfway there: it's at the bottom, but on the wrong side.",
    'transposed': "The arrow points down already, but it's a mirror image. Reversing the row ORDER here would point it up.",
    'done': "Points down. Reversing the row order instead gives up (counter-clockwise); swapping every pair twice gives left.",
}


def rows_order_attempt(matrix):
    """First attempt #1: transpose, then reverse the order of the rows."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix.reverse()


def every_pair_attempt(matrix):
    """First attempt #2: transpose with j over every column (each pair swapped twice)."""
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()


def trace(start):
    matrix = [r[:] for r in start]
    n = len(matrix)
    who = [[r for _ in range(n)] for r in range(n)]      # original row of each value (display only)
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, m=[r[:] for r in matrix], who=[r[:] for r in who], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    rec('start')
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            who[i][j], who[j][i] = who[j][i], who[i][j]
            rec('swap', cell=(i, j), a=matrix[j][i], b=matrix[i][j])
    rec('transposed')
    for r, row in enumerate(matrix):
        row.reverse()
        who[r].reverse()
        rec('reverse', row=r)
    rec('done')
    return events, matrix


def fmt(m):
    return '[' + ','.join('[' + ','.join(map(str, r)) + ']' for r in m) + ']'


def words(e, n, firsts, notes):
    k = e['kind']
    key = k if k in ('start', 'transposed', 'done') else (k, e.get('cell', e.get('row')))
    cap, sub, hold = _words(e, n, firsts)
    if notes and key in notes:
        return cap, notes[key], (END if k == 'done' else KEY)
    return cap, sub, hold


def _words(e, n, firsts):
    k = e['kind']
    if k == 'start':
        return ("Turn it a quarter turn clockwise, without a second matrix.",
                "Colour = the row each value starts in. Row 0 has to end up as the last column.", KEY)
    if k == 'swap':
        i, j = e['cell']
        cap = f"Swap ({i},{j}) and ({j},{i}): {e['b']} and {e['a']} trade places across the diagonal."
        if firsts['swap'] == e['cell']:
            return cap, "j starts at i + 1, so each pair is swapped once. A second swap would put them back.", KEY
        return cap, "", STEP
    if k == 'transposed':
        return ("Transpose done: every row is now a column. The diagonal never moved.",
                "Row 0 is column 0, but clockwise needs it in the LAST column. One more mirror fixes that.", KEY)
    if k == 'reverse':
        r = e['row']
        cap = f"Reverse row {r}: its left and right ends trade places."
        if r == 0:
            return cap, "Mirror across the diagonal, then left-to-right: together, a quarter turn.", KEY
        return cap, "", STEP
    return (f"Done: {fmt(e['m'])}. Row 0 is now the last column.",
            f"{n * (n - 1) // 2} swaps for the transpose, {n} row reversals, one spare variable.", END)


def build(start, subtitle, notes=None):
    events, _ = trace(start)
    n = len(start)
    firsts = {'swap': next((e['cell'] for e in events if e['kind'] == 'swap'), None)}
    sc = Scene('#48 Rotate Image: transpose, then reverse each row', subtitle)
    legend = [(ACTIVE, 'cells being swapped'), (CURSOR, 'row being reversed'),
              (REJECT, '\\ marks the diagonal (it stays put in the transpose)')]
    phase = {'start': 'not started', 'swap': '1. transpose', 'transposed': '1. transpose',
             'reverse': '2. reverse rows', 'done': 'finished'}
    swaps = 0
    for e in events:
        k = e['kind']
        if k == 'swap':
            swaps += 1
        cells = [[{'style': f'region{e["who"][r][c]}', 'label': str(e['m'][r][c])} for c in range(n)]
                 for r in range(n)]
        rings = []
        if k == 'swap':
            i, j = e['cell']
            rings += [((i, j), ACTIVE, 5), ((j, i), ACTIVE, 5)]
        if k == 'reverse':
            rings += [((e['row'], c), CURSOR, 3) for c in range(n)]
        marks = {}
        if k in ('start', 'transposed') or (k == 'swap' and firsts['swap'] == e['cell']):
            marks = {(d, d): '\\' for d in range(n)}
        rows = [('step', phase[k]),
                ('i, j', f"{e['cell'][0]}, {e['cell'][1]}" if k == 'swap' else
                 (f"row {e['row']}" if k == 'reverse' else '-')),
                ('swaps', str(swaps), 'gold'),
                ('rows reversed', str(e['row'] + 1 if k == 'reverse' else (n if k == 'done' else 0)), 'good')]
        cap, sub, hold = words(e, n, firsts, notes)
        sc.frame(GridView(cells, outlines=rings, marks=marks, cell=72 if n <= 4 else 64), cap, sub, hold,
                 side=MapView(rows, 'Progress', headers=('', '')),
                 counters={'swaps': swaps}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    for s in ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]):
        good = trace(s)[1]
        for wrong in (rows_order_attempt, every_pair_attempt):
            m = [r[:] for r in s]
            wrong(m)
            assert m != good                     # both attempts also fail the samples
    assert trace(HARD)[1] == HARD_DOWN
    up, left = [r[:] for r in HARD], [r[:] for r in HARD]
    rows_order_attempt(up)
    every_pair_attempt(left)
    assert up == HARD_UP and left == HARD_LEFT
    sc = build(HARD, 'A 5×5 picture of an arrow pointing right (0 = background). Clockwise, it must point down.',
               HARD_NOTES)
    return sc, ("An arrow pointing right must end up pointing down. Transposing and then reversing the order "
                "of the rows points it up (that's counter-clockwise), and swapping every pair twice points it left.")


def main():
    args = cli()
    sc = build(MATRIX, 'Colour = the row each value started in. Watch row 0 (green) become the last column.')
    finish(sc, 48, "Watch the frame after the transpose: every row has become a column, just in mirror order, "
                   "and reversing each row puts them in place.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
