#!/usr/bin/env python3
"""#73 Set Matrix Zeroes: the first row and first column double as the notes
"zero this column" and "zero this row", so no extra memory is needed. Two
flags, saved BEFORE any note is written, remember whether the first row and
first column had a zero of their own.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import copy
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

MATRIX = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]     # LeetCode example 2

# Hard example 1: a zero in the first row but none in the first column. Using
# the single corner cell matrix[0][0] as the note for BOTH the first row and
# the first column passes both LeetCode samples, then wipes column 0 here too.
HARD1 = [[1, 2, 0, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]
HARD1_ANSWER = [[0, 0, 0, 0], [5, 0, 0, 8], [0, 0, 0, 0], [3, 0, 0, 6]]
HARD1_WRONG = [[0, 0, 0, 0], [0, 0, 0, 8], [0, 0, 0, 0], [0, 0, 0, 6]]

# Hard example 2: -1 is a legal value. Marking doomed cells with a sentinel
# like -1 and turning them into 0 at the end passes both samples, then also
# zeroes the two -1s that were never in a zeroed row or column.
HARD2 = [[3, -1, 5, 7], [2, 4, 0, 1], [-1, 6, 8, 9]]
HARD2_ANSWER = [[3, -1, 0, 7], [0, 0, 0, 0], [-1, 6, 0, 9]]
HARD2_WRONG = [[3, 0, 0, 7], [0, 0, 0, 0], [0, 6, 0, 9]]


class Solution:
    # ---- the notebook's solution, unchanged (used to check the answers) ----
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_zero:
            for j in range(n): matrix[0][j] = 0
        if first_col_zero:
            for i in range(m): matrix[i][0] = 0


def solved(mat):
    mat = copy.deepcopy(mat)
    Solution().setZeroes(mat)
    return mat


def wrong_shared_corner(mat):
    """First attempt: matrix[0][0] is the note for both the first row and the first column."""
    M = copy.deepcopy(mat)
    m, n = len(M), len(M[0])
    for i in range(m):
        for j in range(n):
            if M[i][j] == 0:
                M[i][0] = 0
                M[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if M[i][0] == 0 or M[0][j] == 0:
                M[i][j] = 0
    if M[0][0] == 0:
        for j in range(n): M[0][j] = 0
        for i in range(m): M[i][0] = 0
    return M


def wrong_sentinel(mat):
    """First attempt: overwrite doomed non-zero cells with -1, then turn every -1 into 0."""
    M = copy.deepcopy(mat)
    m, n = len(M), len(M[0])
    for i in range(m):
        for j in range(n):
            if M[i][j] == 0:
                for k in range(n):
                    if M[i][k] != 0: M[i][k] = -1
                for k in range(m):
                    if M[k][j] != 0: M[k][j] = -1
    return [[0 if v == -1 else v for v in r] for r in M]


SAMPLES = [([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
           (MATRIX, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])]
for _in, _out in SAMPLES:          # both first attempts pass both LeetCode samples
    assert solved(_in) == wrong_shared_corner(_in) == wrong_sentinel(_in) == _out
assert solved(HARD1) == HARD1_ANSWER and wrong_shared_corner(HARD1) == HARD1_WRONG
assert solved(HARD2) == HARD2_ANSWER and wrong_sentinel(HARD2) == HARD2_WRONG


def trace(mat):
    matrix = copy.deepcopy(mat)
    events = []
    st = {'fr': None, 'fc': None}
    orig = {(i, j) for i, r in enumerate(mat) for j, v in enumerate(r) if v == 0}
    notes, zeroed = set(), set()

    def rec(kind, **kw):
        events.append(dict(kind=kind, M=[r[:] for r in matrix], notes=set(notes), zeroed=set(zeroed),
                           orig=orig, **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    m, n = len(matrix), len(matrix[0])
    rec('start')
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    st['fr'] = first_row_zero
    rec('flag_row')
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    st['fc'] = first_col_zero
    rec('flag_col')
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                notes.update({(i, 0), (0, j)})
                rec('note', cell=(i, j))
            else:
                rec('scan', cell=(i, j))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                was = matrix[i][j]
                matrix[i][j] = 0
                if (i, j) not in orig:
                    zeroed.add((i, j))
                rec('zero', cell=(i, j), was=was, by_row=matrix[i][0] == 0, by_col=matrix[0][j] == 0)
            else:
                rec('keep', cell=(i, j))
    if first_row_zero:
        for j in range(n): matrix[0][j] = 0
        zeroed.update((0, j) for j in range(n) if (0, j) not in orig)
        rec('row0')
    if first_col_zero:
        for i in range(m): matrix[i][0] = 0
        zeroed.update((i, 0) for i in range(m) if (i, 0) not in orig)
        rec('col0')
    rec('done')
    return events


def cells(e):
    out = []
    for i, row in enumerate(e['M']):
        out.append([])
        for j, v in enumerate(row):
            if (i, j) in e['orig']:
                s = 'bad'
            elif (i, j) in e['zeroed']:
                s = 'window'
            elif (i, j) in e['notes']:
                s = 'active'
            elif i == 0 or j == 0:
                s = 'gold'
            else:
                s = 'plain'
            out[-1].append({'style': s, 'label': str(v)})
    return out


def build(mat, subtitle, notes=None):
    """notes: {kind or (kind, cell): text} replaces that frame's second caption line, held as KEY."""
    notes = notes or {}
    sc = Scene('#73 Set Matrix Zeroes: the first row and column are the notes', subtitle)
    legend = [(style('gold')[1], 'first row / column'), (style('bad')[1], '0 in the input'),
              (ACTIVE, 'note written'), (style('window')[1], 'set to 0')]
    first = set()
    for e in trace(mat):
        k, c = e['kind'], e.get('cell')
        rings, hold, sub = [], STEP, ''
        if c:
            rings.append((c, CURSOR, 3))
        if k == 'start':
            cap = "Every 0 must wipe its whole row and column, but only the 0s in the INPUT count."
            sub = "No extra grid allowed: the first row and column will hold the notes."
            hold = KEY
        elif k == 'flag_row':
            cap = f"first_row_zero = {e['fr']}: does the first row have a 0 of its own?"
            sub = "Save it NOW. Once notes are written into row 0, its own zeros and the notes look the same."
            hold = KEY
            rings += [((0, j), ACTIVE, 3) for j in range(len(e['M'][0]))]
        elif k == 'flag_col':
            cap = f"first_col_zero = {e['fc']}: does the first column have a 0 of its own?"
            sub = "A separate flag: row 0 and column 0 share only the corner, and can disagree."
            hold = KEY
            rings += [((i, 0), ACTIVE, 3) for i in range(len(e['M']))]
        elif k == 'scan':
            cap = f"({c[0]},{c[1]}) = {e['M'][c[0]][c[1]]}: not a 0, nothing to note."
            hold = QUICK * 1.4
        elif k == 'note':
            i, j = c
            cap = f"({i},{j}) is 0: note it at the start of row {i} and the top of column {j}."
            sub = "matrix[i][0] = 0 means 'zero row i'; matrix[0][j] = 0 means 'zero column j'."
            rings += [((i, 0), ACTIVE, 5), ((0, j), ACTIVE, 5)]
            hold = KEY
        elif k == 'zero':
            i, j = c
            why = ' and '.join(w for w, b in ((f'row {i}', e['by_row']), (f'column {j}', e['by_col'])) if b)
            cap = f"({i},{j}): the note for {why} says 0, so {e['was']} becomes 0."
            ring = [((i, 0), ACTIVE, 4)] if e['by_row'] else []
            ring += [((0, j), ACTIVE, 4)] if e['by_col'] else []
            rings += ring
            if 'zero' not in first:
                first.add('zero')
                sub = "Second pass: read the notes. The notes themselves aren't touched yet."
                hold = KEY
            else:
                hold = QUICK * 2
        elif k == 'keep':
            cap = f"({c[0]},{c[1]}): neither its row nor its column is noted. Keep {e['M'][c[0]][c[1]]}."
            hold = QUICK * 1.4
        elif k == 'row0':
            cap = "first_row_zero was True, so now the whole first row becomes 0."
            sub = "Last, because the row was the notebook for the columns until the pass above finished."
            hold = KEY
        elif k == 'col0':
            cap = "first_col_zero was True, so the whole first column becomes 0."
            sub = "Same reason: the column held the notes for the rows."
            hold = KEY
        else:
            cap = "Done, in place, with two booleans of extra memory."
            sub = "Two passes over m × n squares: O(m × n) time, O(1) extra space."
            hold = END
        key = (k, c) if (k, c) in notes else k
        if key in notes:
            sub, hold = notes[key], max(hold, KEY)
        flag = lambda v: '?' if v is None else str(v)
        side = [('first_row_zero', flag(e['fr']), 'gold' if e['fr'] is not None else None),
                ('first_col_zero', flag(e['fc']), 'gold' if e['fc'] is not None else None)]
        nm = e['M']
        side += [('zero rows', ', '.join(str(i) for i in range(1, len(nm)) if nm[i][0] == 0) or '-'),
                 ('zero cols', ', '.join(str(j) for j in range(1, len(nm[0])) if nm[0][j] == 0) or '-')]
        sc.frame(GridView(cells(e), outlines=rings, bridges=False), cap, sub, hold,
                 side=MapView(side, 'Flags and notes', headers=('', '')), legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(HARD1, 'A 0 in the first row, none in the first column. Column 0 must survive.',
                {'flag_col': "False. Using matrix[0][0] for both would say True once row 0's zero writes there.",
                 'done': "Rows 1 and 3 keep their 5 and 3. One shared corner note would have zeroed them."})
    sc2 = build(HARD2, 'Two -1s that are never in a zeroed row or column. -1 is a legal value.',
                {'start': "The notes are zeros, not a special value: any number, even -1, can appear in the input.",
                 'done': "Both -1s survive. Marking doomed cells with -1 and clearing them later zeroes these too."})
    return [(sc1, "A 0 in the first row but not the first column. Using the corner as the note for both "
                  "passes both LeetCode samples, then wipes column 0 and loses the 5 and the 3."),
            (sc2, "Two -1s off to the side. Marking doomed cells with -1 and turning them into 0 later passes "
                  "both samples, then zeroes these -1s as well.")]


def main():
    args = cli()
    sc = build(MATRIX, 'LeetCode example 2. Every 0 zeroes its row and column, using O(1) extra memory.')
    finish(sc, 73, "Watch the two flags at the start: they record the first row's and column's own zeros "
                   "before those cells start holding notes for everyone else.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
