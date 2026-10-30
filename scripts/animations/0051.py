#!/usr/bin/env python3
"""#51 N-Queens: one queen per row, three bitmasks say which squares are attacked.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The attacked squares drawn on the
board for the current row come straight from the three masks.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

N = 4          # LeetCode example 1

# The hard example (interactive page only): n = 5. Checking diagonals only
# against the row directly above passes n = 4 and n = 1, then returns 14 boards
# here instead of 10. The first extra one is 1 3 0 4 2: queens at (0,1) and
# (3,4) are three rows apart on the same diagonal. Notes are keyed by
# (kind, queens placed so far) or 'done' and replace that frame's second line.
HARD_N = 5
HARD_NOTES = {
    ('row', (1, 3, 0)): "Column 4 is red because of the queen at (0,1), three rows up on the same diagonal.",
    ('place', (1, 3, 0, 2)): "Checking only the row above would also allow column 4 here, and record 1 3 0 4 2.",
    'done': "Checking diagonals only against the row above returns 14: four boards have a long-range diagonal clash.",
}


def trace(n):
    events = []

    def rec(kind, row, placed, masks, results, **kw):
        events.append(dict(kind=kind, row=row, placed=list(placed), masks=masks,
                           results=[list(b) for b in results], n=n, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    results = []
    queens = [-1] * n

    def backtrack(row, col_mask, diag_mask, anti_mask):
        masks = (col_mask, diag_mask, anti_mask)
        if row == n:
            board = []
            for r in range(n):
                board.append('.' * queens[r] + 'Q' + '.' * (n - queens[r] - 1))
            results.append(board)
            rec('record', row, queens[:row], masks, results)
            return
        available = ((1 << n) - 1) & ~(col_mask | diag_mask | anti_mask)
        rec('row' if available else 'dead', row, queens[:row], masks, results, available=available)
        while available:
            bit = available & (-available)
            available -= bit
            col = bit.bit_length() - 1
            queens[row] = col
            rec('place', row, queens[:row + 1], masks, results, col=col, available=available)
            backtrack(row + 1,
                      col_mask | bit,
                      (diag_mask | bit) >> 1,
                      (anti_mask | bit) << 1)
            rec('back', row, queens[:row], masks, results, col=col, available=available)

    backtrack(0, 0, 0, 0)
    rec('done', None, [], (0, 0, 0), results)
    return events


def bits(mask, N=N):
    return ' '.join('1' if mask >> c & 1 else '·' for c in range(N))


def words(e, first, notes=None):
    cap, sub, hold = _words(e, first)
    if notes:
        key = e['kind'] if e['kind'] == 'done' else (e['kind'], tuple(e['placed']))
        if key in notes:
            return cap, notes[key], (END if e['kind'] == 'done' else KEY)
    return cap, sub, hold


def _words(e, first):
    k, r, N = e['kind'], e['row'], e['n']
    if k == 'row':
        if r == 0:
            return ("Row 0: nothing is attacked yet, so every column is free.",
                    "One queen per row, top to bottom. The masks track what earlier queens attack.", STEP)
        free = [c for c in range(N) if e['available'] >> c & 1]
        if first.get('row') == id(e):
            return (f"Row {r}: the masks say columns {free} are free; the red squares are attacked.",
                    "Column, and both diagonals: the diagonal masks shift one step each row, like the diagonals do.", KEY)
        return (f"Row {r}: free columns {free}.", "", STEP)
    if k == 'dead':
        if first.get('dead') == id(e):
            return (f"Row {r}: every square is attacked. No queen fits, so this arrangement is a dead end.",
                    "Back up and move the queen above to its next free column.", KEY)
        return (f"Row {r}: every square is attacked. Dead end, back up.", "", STEP)
    if k == 'place':
        return (f"Put a queen at row {r}, column {e['col']}, and go to row {r + 1}.", "", STEP)
    if k == 'back':
        if first.get('back') == id(e):
            return (f"Back in row {r}: the queen at column {e['col']} comes off. Nothing to undo by hand.",
                    "Each call got its own copies of the masks, so returning restores them automatically.", KEY)
        nxt = [c for c in range(N) if e['available'] >> c & 1]
        return (f"Row {r}: lift the queen from column {e['col']}" +
                (f"; next free column is {nxt[0]}." if nxt else "; no free columns left here."), "", QUICK * 1.8)
    if k == 'record':
        return (f"All {N} rows have a queen and none attack each other: solution {len(e['results'])}. Record it.",
                "Then keep searching: there may be more.", KEY)
    return (f"Done: {len(e['results'])} solutions for a {N}×{N} board.",
            "Attacked squares were never even tried, which is why this beats checking every arrangement.", END)


def cells(e):
    N = e['n']
    out = [[{'style': 'plain'} for _ in range(N)] for _ in range(N)]
    for (i, j) in [(i, j) for i in range(N) for j in range(N) if (i + j) % 2]:
        out[i][j] = {'style': 'muted'}
    for i, c in enumerate(e['placed']):
        out[i][c] = {'style': 'good', 'label': 'Q'}
    r = e['row']
    if e['kind'] in ('row', 'dead', 'place', 'back') and r is not None and r < N:
        cm, dm, am = e['masks']
        blocked = cm | dm | am
        for c in range(N):
            if blocked >> c & 1 and not (e['kind'] == 'place' and c == e['col']):
                out[r][c] = {'style': 'bad', 'label': '×'}
    return out


def build(N, subtitle, notes=None):
    events = trace(N)
    first = {}
    for e in events:
        if e['kind'] == 'row' and e['row'] > 0 and 'row' not in first and e['available'] != (1 << N) - 1:
            first['row'] = id(e)
        for k in ('dead', 'back'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
    sc = Scene(f'#51 N-Queens: one queen per row, n = {N}', subtitle)
    legend = [(style('good')[1], 'queen'), (style('bad')[1], 'attacked'), (ACTIVE, 'row being filled')]
    for e in events:
        k, r = e['kind'], e['row']
        rings = []
        if k == 'place':
            rings.append(((r, e['col']), ACTIVE, 5))
        cm, dm, am = e['masks']
        rows = [('columns', bits(cm, N)), ('diag ↙', bits(dm, N)), ('diag ↘', bits(am, N)),
                ('free', bits(((1 << N) - 1) & ~(cm | dm | am), N), 'good')]
        title = f'Masks for row {r}' if r is not None and r < N else 'Masks'
        side = MapView(rows, title, headers=('mask', 'col 0 … ' + str(N - 1)))
        sols = [(' '.join(str(b.index('Q')) for b in sol), 'good') for sol in e['results']]
        chips = ChipsView(sols, 'Solutions (queen column per row)')
        cap, sub, hold = words(e, first, notes)
        sc.frame([GridView(cells(e), outlines=rings, cell=64), chips], cap, sub, hold, side=side,
                 counters={'row': r if r is not None and r < N else '-', 'solutions': len(e['results'])},
                 legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    sc = build(HARD_N, 'Q = queen. Red × = attacked, including by queens several rows up on a long diagonal.',
               HARD_NOTES)
    return sc, ("n = 5. Checking diagonals only against the row directly above passes both LeetCode samples, "
                "then returns 14 boards here instead of 10. Watch row 3 under queens 1 3 0: column 4 is "
                "attacked from three rows up.")


def main():
    args = cli()
    sc = build(N, 'Q = queen. Red × = square in the current row attacked by a queen above.')
    finish(sc, 51, "Watch row 2 after queens at columns 0 and 2: every square is attacked, so the search "
                   "backs up at once instead of trying the rest of the board.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
