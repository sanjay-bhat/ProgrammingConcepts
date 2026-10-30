#!/usr/bin/env python3
"""#36 Valid Sudoku: every digit joins its row, its column and its box at once.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

BOARD = [                       # LeetCode example 1 (valid)
    "53..7....",
    "6..195...",
    ".98....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2...6",
    ".6....28.",
    "...419..5",
    "....8..79",
]
SPOTLIGHT = (2, 1)              # the walkthrough pauses here: its box already holds 5, 3, 6

# Hard example (interactive page only): the same board with an 8 written at (1, 1).
# Row 1 and column 1 have no other 8, but the box does, at (2, 2). Answer false;
# a checker that only tests rows and columns answers true.
HARD = [r if i != 1 else "68.195..." for i, r in enumerate(BOARD)]


def trace(rows):
    board = [list(r) for r in rows]
    events, scanned = [], set()
    st = {'cell': None}

    def rec(kind, seen, **kw):
        events.append(dict(kind=kind, seen=set(seen), scanned=set(scanned), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def isValidSudoku(board):
        seen = set()
        rec('start', seen)
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue
                st['cell'] = (r, c)
                row_key = ('row', r, ch)
                col_key = ('col', c, ch)
                box_key = ('box', r // 3, c // 3, ch)
                for key in (row_key, col_key, box_key):
                    if key in seen:
                        rec('clash', seen, key=key)
                        return False
                    seen.add(key)
                scanned.add((r, c))
                rec('digit', seen)
        st['cell'] = None
        rec('valid', seen)
        return True

    answer = isValidSudoku(board)
    assert answer == Solution().isValidSudoku([list(r) for r in rows])
    return events, answer


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue
                row_key = ('row', r, ch)
                col_key = ('col', c, ch)
                box_key = ('box', r // 3, c // 3, ch)
                for key in (row_key, col_key, box_key):
                    if key in seen:
                        return False
                    seen.add(key)
        return True


def rows_and_columns_only(rows):
    """First attempt: check rows and columns, forget the boxes."""
    seen = set()
    for r in range(9):
        for c in range(9):
            ch = rows[r][c]
            if ch == '.':
                continue
            for key in (('row', r, ch), ('col', c, ch)):
                if key in seen:
                    return False
                seen.add(key)
    return True


def group_digits(seen, kind, *where):
    """Digits recorded so far for one group, read back out of the single `seen` set."""
    return sorted(k[-1] for k in seen if k[0] == kind and tuple(k[1:-1]) == where)


def words(e, rows, notes, n_digit, spot):
    k, cell = e['kind'], e['cell']
    if k == 'start':
        return ("Scan every square, row by row. Skip the empty ones.",
                "Each digit must be new to its row, its column and its 3×3 box.", KEY)
    r, c = cell if cell else (None, None)
    ch = rows[r][c] if cell else ''
    if k == 'digit':
        b = (r // 3, c // 3)
        if (r, c) in notes:
            return (f"{ch} at ({r},{c}): new to row {r}, column {c} and box {b}.", notes[(r, c)], KEY)
        if n_digit == 1:
            return (f"{ch} at ({r},{c}) joins three groups: row {r}, column {c}, box {b}.",
                    "None of them has a 5 yet, so record all three facts.", KEY)
        if (r, c) == spot:
            have = ', '.join(d for d in group_digits(e['seen'], 'box', *b) if d != ch)
            return (f"{ch} at ({r},{c}): row {r}, column {c}, and box ({r}//3, {c}//3) = {b}.",
                    f"That box already holds {have}. No 9 among them, so it's fine.", KEY)
        return (f"{ch} at ({r},{c}): new to row {r}, column {c} and box {b}. Record it.", "",
                STEP if n_digit <= 3 else QUICK * 2)
    if k == 'clash':
        kind = e['key'][0]
        name = {'row': f'row {r}', 'col': f'column {c}', 'box': f'box {(r // 3, c // 3)}'}[kind]
        return (f"{ch} at ({r},{c}): {name} already has a {ch}. Invalid: return false.",
                notes.get('clash', "Two copies of one digit in a group break the rules."), END)
    return (f"Every digit was new to all three of its groups. The board is valid.",
            f"{len(e['seen'])} facts recorded, 3 per digit. The board is always 9×9, so it's O(1).", END)


def cells(e, rows):
    cell = e['cell']
    r0, c0 = cell if cell else (-9, -9)
    out = []
    for r in range(9):
        out.append([])
        for c in range(9):
            ch = rows[r][c]
            d = {'label': '' if ch == '.' else ch}
            odd = (r // 3 + c // 3) % 2 == 1
            if cell and (r // 3, c // 3) == (r0 // 3, c0 // 3):
                d['style'] = 'gold'
            elif cell and (r == r0 or c == c0):
                d['style'] = 'window'
            elif ch != '.' and (r, c) not in e['scanned'] and e['kind'] != 'valid':
                d['style'] = 'muted'
            else:
                d['style'] = 'muted' if odd and ch == '.' else 'plain'
            out[-1].append(d)
    if e['kind'] == 'clash':
        kind = e['key'][0]
        for r in range(9):
            for c in range(9):
                same = {'row': r == r0, 'col': c == c0,
                        'box': (r // 3, c // 3) == (r0 // 3, c0 // 3)}[kind]
                if same and rows[r][c] == rows[r0][c0] and (r, c) != cell:
                    out[r][c]['style'] = 'bad'
        out[r0][c0]['style'] = 'bad'
    elif cell:
        out[r0][c0]['style'] = 'active'
    return out


def build(rows, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#36 Valid Sudoku: three groups per digit', subtitle)
    legend = [(ACTIVE, 'digit being checked'), (style('window')[1], 'its row and column'),
              (style('gold')[1], 'its box'), (style('bad')[1], 'clash')]
    events, answer = trace(rows)
    n_digit = 0
    for e in events:
        n_digit += e['kind'] == 'digit'
        grid = GridView(cells(e, rows), bridges=False, outlines=[(e['cell'], ACTIVE, 4)] if e['cell'] else [],
                        cell=34)
        side_rows = []
        if e['cell']:
            r, c = e['cell']
            ch = rows[r][c]
            order = ('row', 'col', 'box')
            stop = order.index(e['key'][0]) if e['kind'] == 'clash' else 9
            for n, (kind, label, where) in enumerate((('row', f'row {r}', (r,)), ('col', f'column {c}', (c,)),
                                                      ('box', f'box {r // 3},{c // 3}', (r // 3, c // 3)))):
                ds = group_digits(e['seen'], kind, *where)
                if n == stop:
                    side_rows.append((label, f"has {ch} already", 'bad'))
                elif n > stop:
                    side_rows.append((label, '(not checked)', 'muted'))
                else:
                    shown = ' '.join(d for d in ds if d != ch)
                    side_rows.append((label, (shown + '  + ' if shown else '+ ') + ch,
                                      'gold' if kind == 'box' else 'window'))
        side = MapView(side_rows, 'Seen in its groups', headers=('group', 'digits so far'),
                       empty='(no digit being checked)')
        cap, sub, hold = words(e, rows, notes, n_digit, SPOTLIGHT if rows == BOARD else None)
        sc.frame(grid, cap, sub, hold, side=side,
                 counters={'facts': len(e['seen'])}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    assert Solution().isValidSudoku([list(r) for r in HARD]) is False
    assert rows_and_columns_only(HARD) is True
    sc = build(HARD, 'LeetCode example 1 with an 8 added at (1,1). Answer false. Rows and columns alone say true.', {
        (1, 1): "Row 1 has no other 8, and column 1 never gets one. Only the box has a second 8 coming, at (2,2).",
        'clash': "Its row and column are fine. Only the box check catches this, so a rows-and-columns checker says true.",
    })
    return sc, ("An 8 added at row 1, column 1 clashes only with the 8 at (2,2), inside the same box. "
                "A first attempt that checks only rows and columns answers true; the right answer is false.")


def main():
    args = cli()
    sc = build(BOARD, 'LeetCode example 1. No digit twice in any row, column or 3×3 box.')
    finish(sc, 36, "Watch the 9 at row 2, column 1: it joins row 2, column 1 and the top-left box at once, "
                   "and the box check is the one people forget.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
