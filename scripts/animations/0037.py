#!/usr/bin/env python3
"""#37 Sudoku Solver: guess the smallest digit that fits, and erase it when a
square further on runs out of digits.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. LeetCode's board takes about 12,500
place/erase steps, far too many for a GIF, so the walkthrough starts from the
same board with its first 34 blanks already filled with their final digits:
the last 17 blanks still need 6 erasures.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

SAMPLE = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
          "7...2...6", ".6....28.", "...419..5", "....8..79"]          # LeetCode example
SOLVED = ["534678912", "672195348", "198342567", "859761423", "426853791",
          "713924856", "961537284", "287419635", "345286179"]
KEEP_OPEN = 17      # leave LeetCode's last 17 blanks open for the GIF

# The hard example (interactive page only): 38 blanks. Filling only squares
# that have a single legal digit solves LeetCode's example, but here it fills
# 16 squares and stops with 22 blanks, every one of them with 2+ options.
# Backtracking needs 10 erasures. Answer: SOLVED.
HARD = [".3..78.1.", ".72.9.3.8", "198..2.67", ".59.6.42.", "42..5.791",
        "71.924856", "9....7..4", "2.7......", "...28.1.9"]
HARD_NOTES = {
    'start': "Fill only the one-option squares and you get 16 in, then stop: the other 22 all have 2 or more options.",
    'done': "No guessing, no answer: a deduction-only solver leaves 22 blanks here, though it solves LeetCode's board.",
}


def walkthrough_board():
    blanks = [(r, c) for r in range(9) for c in range(9) if SAMPLE[r][c] == '.']
    b = [list(r) for r in SOLVED]
    for r, c in blanks[-KEEP_OPEN:]:
        b[r][c] = '.'
    return [''.join(r) for r in b]


def clash(board, row, col, c):
    """Which rule rejects digit c at (row, col): for the captions only."""
    if c in board[row]:
        return 'row'
    if any(board[i][col] == c for i in range(9)):
        return 'col'
    return 'box'


def only_singles(rows):
    """The first attempt the hard example breaks: fill one-option squares until none are left."""
    b = [list(r) for r in rows]
    ok = lambda r, c, v: all(b[r][i] != v and b[i][c] != v and
                             b[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] != v for i in range(9))
    changed = True
    while changed:
        changed = False
        for r in range(9):
            for c in range(9):
                if b[r][c] == '.':
                    cand = [v for v in '123456789' if ok(r, c, v)]
                    if len(cand) == 1:
                        b[r][c] = cand[0]
                        changed = True
    return [''.join(r) for r in b]


def trace(rows):
    board = [list(r) for r in rows]
    events, guesses = [], []

    def rec(kind, **kw):
        events.append(dict(kind=kind, board=[r[:] for r in board], guesses=list(guesses), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def is_valid(row, col, c):
        for i in range(9):
            if board[row][i] == c:
                return False
            if board[i][col] == c:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False
        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    rejected = []
                    for c in '123456789':
                        if is_valid(row, col, c):
                            board[row][col] = c
                            guesses.append((row, col, c))
                            rec('place', cell=(row, col), digit=c, rejected=rejected[:])
                            rejected = []
                            if solve():
                                return True
                            board[row][col] = '.'
                            guesses.pop()
                            rec('undo', cell=(row, col), digit=c)
                        else:
                            rejected.append((c, clash(board, row, col, c)))
                    rec('dead', cell=(row, col), rejected=rejected)
                    return False
        return True

    rec('start')
    solve()
    rec('done')
    return events, [''.join(r) for r in board]


def why(rejected):
    if not rejected:
        return ''
    groups = {}
    for d, g in rejected:
        groups.setdefault(g, []).append(d)
    name = {'row': 'row', 'col': 'column', 'box': 'box'}
    return '; '.join(f"{','.join(ds)} in its {name[g]}" for g, ds in groups.items())


def words(e, first, notes):
    k = e['kind']
    if notes and k in notes and k in ('start', 'done'):
        cap = _words(e, first)[0]
        return cap, notes[k], (END if k == 'done' else KEY)
    return _words(e, first)


def _words(e, first):
    k = e['kind']
    if k == 'start':
        return ("Find the first empty square, try digits 1 to 9, keep the first that fits.",
                "Every guess is a recursive call: the call stack on the right is the list of open guesses.", KEY)
    r, c = e.get('cell', (None, None))
    if k == 'place':
        rej = why(e['rejected'])
        lead = f"({r},{c}): " + (f"{rej}. " if rej else "") + f"{e['digit']} fits, so place it."
        if first.get('place') == id(e):
            return (lead, "It's a guess: nothing here proves it's right. Move on to the next blank.", KEY)
        return (lead, "", QUICK * 2.2 if rej else QUICK * 1.6)
    if k == 'dead':
        rej = why(e['rejected'])
        if first.get('dead') == id(e):
            return (f"({r},{c}): no digit fits. {rej}.",
                    "This square isn't the problem: an EARLIER guess is. Return false to it.", KEY)
        return (f"({r},{c}): no digit fits. Dead end, return false.", rej + '.', STEP)
    if k == 'undo':
        if first.get('undo') == id(e):
            return (f"Back at ({r},{c}): erase the {e['digit']} and try the next digit.",
                    "Erase BEFORE trying again: a leftover digit would be skipped by the scan for '.'.", KEY)
        if not e['guesses']:
            return (f"Back at ({r},{c}): erase the {e['digit']}. That was the very first guess.",
                    "Every guess built on top of it has already been erased. Now try its next digit.", KEY)
        return (f"Back at ({r},{c}): erase the {e['digit']}, try the next digit.", "", STEP)
    return ("No '.' left: solve() returns true all the way up. Solved.",
            "Every digit on the board survived the row, column and box check.", END)


def cells(e, given):
    out = []
    k, cell = e['kind'], e.get('cell')
    for r in range(9):
        row = []
        for c in range(9):
            v = e['board'][r][c]
            odd = ((r // 3) + (c // 3)) % 2 == 1
            if given[r][c] != '.':
                row.append({'style': 'gold' if odd else 'plain', 'label': v})
            elif v != '.':
                row.append({'style': 'good', 'label': v})
            else:
                row.append({'style': 'gold' if odd else 'plain'})
        out.append(row)
    if cell:
        r, c = cell
        if k == 'place':
            out[r][c] = {'style': 'active', 'label': e['digit']}
        elif k == 'dead':
            out[r][c] = {'style': 'bad', 'label': '?'}
        elif k == 'undo':
            out[r][c] = {'style': 'bad', 'label': '·'}
    return out


def build(rows, subtitle, notes=None):
    events, final = trace(rows)
    first = {}
    for e in events:
        if e['kind'] in ('dead', 'undo') and e['kind'] not in first:
            first[e['kind']] = id(e)
        if e['kind'] == 'place' and 'place' not in first:
            first['place'] = id(e)
    sc = Scene('#37 Sudoku Solver: guess, and erase when stuck', subtitle)
    legend = [(ACTIVE, 'digit just placed'), (style('good')[1], 'guessed digits'),
              (style('bad')[1], 'stuck / erased'), (style('gold')[1], 'alternate 3×3 boxes')]
    placed = erased = 0
    for e in events:
        k = e['kind']
        placed += k == 'place'
        erased += k == 'undo'
        rings = [(e['cell'], ACTIVE if k == 'place' else REJECT, 4)] if e.get('cell') else []
        stack = [(f'({r},{c}) = {d}', 'good') for r, c, d in e['guesses']]
        cap, sub, hold = words(e, first, notes)
        sc.frame(GridView(cells(e, rows), outlines=rings, bridges=False), cap, sub, hold,
                 side=StackView(stack, 'Open guesses (call stack)', base='solveSudoku',
                                empty='(no guesses yet)'),
                 counters={'blanks': sum(r.count('.') for r in e['board']), 'placed': placed, 'erased': erased},
                 legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    assert trace(HARD)[1] == SOLVED and trace(SAMPLE)[1] == SOLVED
    assert only_singles(SAMPLE) == SOLVED                                   # passes LeetCode's board
    assert sum(r.count('.') for r in only_singles(HARD)) == 22             # stuck here
    sc = build(HARD, '38 blanks. Plain digits are given; green ones are guesses the solver may still erase.',
               HARD_NOTES)
    return sc, ("38 blanks where filling only one-option squares stalls with 22 left, though it solves "
                "LeetCode's board. Watch the solver guess, hit dead ends, and erase its way back 10 times.")


def main():
    args = cli()
    sc = build(walkthrough_board(), "LeetCode's board with its first 34 blanks pre-filled; the last 17 play out.")
    finish(sc, 37, "Watch the first dead end: a square where every digit clashes means an earlier guess was "
                   "wrong, so the solver erases its latest guess and tries that square's next digit.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
