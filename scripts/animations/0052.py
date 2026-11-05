#!/usr/bin/env python3
"""#52 N-Queens II: the N-Queens search, but each call RETURNS how many
complete boards lie below it, and the counts add up on the way back.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The queens drawn on the board and
the per-call counts in the stack are display-only copies of what the
recursion holds in its locals.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

N = 4          # LeetCode example 1: 2

# The hard example (interactive page only): n = 5, answer 10. Two first
# attempts pass both LeetCode samples (n = 4 -> 2, n = 1 -> 1) and fail here:
#   - checking diagonals only against the queen in the row directly above
#     counts 14: four boards have a clash three rows apart;
#   - the mirror trick done carelessly: count boards whose first queen is in
#     the left half of row 0 and double it. For odd n that forgets the middle
#     column, which holds 2 of the 10 boards, so it returns 8. (It also needs
#     n = 1 special-cased, which is how it slips past the samples.)
HARD_N = 5
HARD_NOTES = {
    ('return', 0, 2): "Row 0's middle column found 2 boards. Doubling only the left half forgets these: 8, not 10.",
    ('row', (1, 3, 0)): "Column 4 is attacked from (0,1), three rows up. Checking only the row above would allow it.",
    'done': "10. Checking only the row above counts 14; doubling the left half of row 0 gives 8.",
}


def row_above_attempt(n):
    """First attempt #1: check columns, but diagonals only against the row directly above."""
    def go(row, used, prev):
        if row == n:
            return 1
        return sum(go(row + 1, used | {c}, c) for c in range(n)
                   if c not in used and (prev is None or abs(prev - c) != 1))
    return go(0, frozenset(), None)


def mirror_attempt(n):
    """First attempt #2: count first queens in the left half of row 0 and double (n = 1 special-cased)."""
    if n == 1:
        return 1
    full = (1 << n) - 1

    def bt(c, d, a):
        if c == full:
            return 1
        cnt, av = 0, full & ~(c | d | a)
        while av:
            b = av & -av
            av -= b
            cnt += bt(c | b, (d | b) >> 1, (a | b) << 1)
        return cnt
    return 2 * sum(bt(1 << c, (1 << c) >> 1, (1 << c) << 1) for c in range(n // 2))


def trace(n):
    events = []
    placed, counts = [], []          # display only: queens so far, and each active call's count

    def rec(kind, masks, **kw):
        events.append(dict(kind=kind, placed=list(placed), counts=list(counts), masks=masks, n=n, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    full = (1 << n) - 1  # all n column bits set — fully occupied mask

    def backtrack(col_mask, diag_mask, anti_mask):
        masks = (col_mask, diag_mask, anti_mask)
        if col_mask == full:
            rec('record', masks)
            return 1
        count = 0
        counts.append(0)
        available = full & ~(col_mask | diag_mask | anti_mask)
        rec('row' if available else 'dead', masks, available=available)
        while available:
            bit = available & (-available)
            available -= bit
            placed.append(bit.bit_length() - 1)
            rec('place', masks, col=placed[-1])
            got = backtrack(
                col_mask | bit,
                (diag_mask | bit) >> 1,
                (anti_mask | bit) << 1)
            count += got
            counts[-1] = count
            col = placed.pop()
            rec('return', masks, col=col, got=got)
        counts.pop()
        return count

    total = backtrack(0, 0, 0)
    rec('done', (0, 0, 0), total=total)
    return events, total


def bits(mask, n):
    return ' '.join('1' if mask >> c & 1 else '·' for c in range(n))


def words(e, first, notes):
    cap, sub, hold = _words(e, first)
    if notes:
        k = e['kind']
        key = 'done' if k == 'done' else (
            ('return', len(e['placed']), e['col']) if k == 'return' else (k, tuple(e['placed'])))
        if key in notes:
            return cap, notes[key], (END if k == 'done' else KEY)
    return cap, sub, hold


def _words(e, first):
    k, n = e['kind'], e['n']
    r = len(e['placed'])
    if k == 'row':
        free = [c for c in range(n) if e['available'] >> c & 1]
        if r == 0:
            return ("Row 0: nothing is attacked, so every column is free.",
                    "Each call places one queen in its row and returns how many full boards lie below.", KEY)
        if first.get('row') == id(e):
            return (f"Row {r}: free columns {free}. Red squares are attacked by the queens above.",
                    "Three masks hold the attacked columns: straight down, and the two diagonals.", KEY)
        return (f"Row {r}: free columns {free}.", "", STEP)
    if k == 'dead':
        if first.get('dead') == id(e):
            return (f"Row {r}: every square is attacked. This call's count stays 0.",
                    "It returns 0, so the queen above moves on to its next free column.", KEY)
        return (f"Row {r}: every square is attacked. Return 0.", "", STEP)
    if k == 'place':
        return (f"Queen at row {r - 1}, column {e['col']}. Ask the next row how many boards follow.", "", QUICK * 2)
    if k == 'record':
        if first.get('record') == id(e):
            return (f"Every column is used: a complete board. This call returns 1.",
                    "No board is built or stored. The 1 is all the caller needs.", KEY)
        return ("A complete board. Return 1.", "", STEP)
    if k == 'return':
        mine = e['counts'][-1] if e['counts'] else 0
        cap = f"Back in row {r}: column {e['col']} led to {e['got']} board{'s' if e['got'] != 1 else ''}. Count here: {mine}."
        if e['got'] and first.get('return') == id(e):
            return cap, "count += what the call below returned: the totals add up on the way back.", KEY
        return cap, "", QUICK * 2 if not e['got'] else STEP
    return (f"Row 0 has tried every column. Answer: {e['total']}.",
            "Only counts travel back up; the boards themselves were never written down.", END)


def cells(e):
    n = e['n']
    out = [[{'style': 'muted' if (i + j) % 2 else 'plain'} for j in range(n)] for i in range(n)]
    for i, c in enumerate(e['placed']):
        out[i][c] = {'style': 'good', 'label': 'Q'}
    r = len(e['placed'])
    if e['kind'] in ('row', 'dead') and r < n:
        cm, dm, am = e['masks']
        for c in range(n):
            if (cm | dm | am) >> c & 1:
                out[r][c] = {'style': 'bad', 'label': '×'}
    return out


def build(n, subtitle, notes=None):
    events, _ = trace(n)
    first = {}
    for e in events:
        if e['kind'] == 'row' and e['placed'] and 'row' not in first:
            first['row'] = id(e)
        if e['kind'] == 'return' and e['got'] and 'return' not in first:
            first['return'] = id(e)
        for k in ('dead', 'record'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
    sc = Scene(f'#52 N-Queens II: count the boards, n = {n}', subtitle)
    legend = [(style('good')[1], 'queen'), (style('bad')[1], 'attacked'), (ACTIVE, 'queen just placed')]
    found = 0
    for e in events:
        k = e['kind']
        if k == 'record':
            found += 1
        rings = []
        if k == 'place':
            rings.append(((len(e['placed']) - 1, e['col']), ACTIVE, 5))
        cm, dm, am = e['masks']
        lines = [f'columns  {bits(cm, n)}', f'diag ↙   {bits(dm, n)}', f'diag ↘   {bits(am, n)}']
        stack = []
        for d, c in enumerate(e['counts']):
            q = f'col {e["placed"][d]}' if d < len(e['placed']) else 'choosing'
            stack.append((f'row {d}: {q}, count {c}', 'good' if c else 'plain'))
        if k == 'record':
            stack.append((f'row {n}: board complete, return 1', 'gold'))
        cap, sub, hold = words(e, first, notes)
        sc.frame([GridView(cells(e), outlines=rings, cell=48 if n <= 4 else 40),
                  TextView(lines, title='Masks for the row being filled: 1 = attacked', size=14)],
                 cap, sub, hold,
                 side=StackView(stack, 'Calls (count so far)', base='totalNQueens', empty='(no calls yet)'),
                 counters={'boards found': found}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    for s in (4, 1):                                       # LeetCode samples
        assert row_above_attempt(s) == mirror_attempt(s) == trace(s)[1]
    assert trace(HARD_N)[1] == 10
    assert row_above_attempt(HARD_N) == 14 and mirror_attempt(HARD_N) == 8
    sc = build(HARD_N, 'Q = queen, red × = attacked, even by queens several rows up on a long diagonal.', HARD_NOTES)
    return sc, ("n = 5, answer 10. Checking diagonals only against the row above counts 14, and doubling the "
                "left half of row 0 counts 8; both pass the samples. Watch row 0's middle column bring back 2.")


def main():
    args = cli()
    sc = build(N, 'Q = queen. Red × = square in the current row attacked by a queen above.')
    finish(sc, 52, "Watch the call stack when a board is completed: the 1 travels back up and each row adds it "
                   "to its own count, so nothing but numbers is ever stored.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
