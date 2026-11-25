#!/usr/bin/env python3
"""#74 Search a 2D Matrix: read row by row, the grid is one sorted list, so
binary search over positions 0..m*n-1 and turn each position back into a cell
with row = mid // n, column = mid % n (n = number of COLUMNS).

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import bisect
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

MATRIX = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
TARGET = 3                                                   # LeetCode example 1: true

# Hard example 1: a wide grid. Converting a position with the number of ROWS
# (mid // m, mid % m) passes both LeetCode samples on their 3x4 grid, but on
# this 2x5 grid the very first probe, position 4, becomes row 4 // 2 = 2,
# which doesn't exist.
HARD1 = ([[2, 4, 6, 8, 10], [13, 15, 17, 19, 21]], 19)

# Hard example 2: the target is the FIRST number of a row. Two binary searches
# (pick the last row whose first number is < target, then search that row)
# pass both samples, but the strict < sends 19 to the row above: false.
HARD2 = ([[1, 4, 7], [10, 13, 16], [19, 22, 25], [28, 31, 34]], 19)


class Solution:
    # ---- the notebook's solution, unchanged (used to check the answers) ----
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


def wrong_by_rows(matrix, target):
    """First attempt: convert a position with the number of rows instead of columns."""
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = matrix[mid // m][mid % m]
        if val == target:
            return True
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def wrong_two_searches(matrix, target):
    """First attempt: find the last row whose first number is < target, then search that row."""
    lo, hi = 0, len(matrix) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if matrix[mid][0] < target:
            lo = mid
        else:
            hi = mid - 1
    row = matrix[lo]
    i = bisect.bisect_left(row, target)
    return i < len(row) and row[i] == target


def crashes(f, *a):
    try:
        f(*a)
    except IndexError:
        return True
    return False


for _t, _ans in ((3, True), (13, False)):          # both first attempts pass both LeetCode samples
    assert Solution().searchMatrix(MATRIX, _t) == wrong_by_rows(MATRIX, _t) == wrong_two_searches(MATRIX, _t) == _ans
assert Solution().searchMatrix(*HARD1) is True and crashes(wrong_by_rows, *HARD1)
assert Solution().searchMatrix(*HARD2) is True and wrong_two_searches(*HARD2) is False


def trace(matrix, target):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, lo=lo, hi=hi, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    rec('start', m=m, n=n)
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            rec('found', mid=mid, val=val)
            return events
        was = (lo, hi)
        if val < target:
            lo = mid + 1
            rec('right', mid=mid, val=val, was=was)
        else:
            hi = mid - 1
            rec('left', mid=mid, val=val, was=was)
    rec('empty')
    return events


def build(matrix, target, subtitle, notes=None, show_rows_bug=False):
    """notes: {kind or (kind, mid): text} replaces that frame's second caption line, held as KEY.
    show_rows_bug: add a side row with what mid // m, mid % m would have pointed at."""
    notes = notes or {}
    m, n = len(matrix), len(matrix[0])
    flat = [v for r in matrix for v in r]
    sc = Scene('#74 Search a 2D Matrix: one sorted list in disguise', subtitle)
    legend = [(style('window')[1], 'still possible'), (ACTIVE, 'probe (mid)'), (style('muted')[1], 'ruled out'),
              (style('good')[1], 'found')]
    first = set()
    for e in trace(matrix, target):
        k, lo, hi = e['kind'], e['lo'], e['hi']
        mid = e.get('mid')
        live = (e['was'] if k in ('right', 'left') else (lo, hi))
        st = {}
        for p in range(m * n):
            st[p] = 'window' if live[0] <= p <= live[1] else 'muted'
        if mid is not None:
            st[mid] = 'good' if k == 'found' else 'active'
        cells = [[{'style': st[r * n + c], 'label': str(matrix[r][c]), 'sub': f'#{r * n + c}'}
                  for c in range(n)] for r in range(m)]
        rings = [((mid // n, mid % n), ACTIVE if k != 'found' else style('good')[1], 5)] if mid is not None else []
        hold, sub = STEP, ''
        side = [('target', str(target)), ('lo .. hi', f'{live[0]} .. {live[1]}')]
        if k == 'start':
            cap = f"Number the {m * n} cells 0 to {m * n - 1}, row by row. Read that way, they're sorted."
            sub = f"Binary search on those positions. Position p is row p // {n}, column p % {n} ({n} = columns)."
            hold = KEY
        else:
            if mid is not None:
                side += [('mid', str(mid)), ('row = mid // n', f'{mid} // {n} = {mid // n}'),
                         ('col = mid % n', f'{mid} % {n} = {mid % n}'), ('value', str(e['val']), 'active')]
                if show_rows_bug:
                    r2, c2 = mid // m, mid % m
                    ok = r2 < m and c2 < n
                    side.append(('mid // m, mid % m', f'({r2},{c2})' + ('' if ok else ': no such cell'), 'bad'))
            if k == 'right':
                cap = f"Probe {mid} = cell ({mid // n},{mid % n}) = {e['val']} < {target}: the target is further on. lo = {mid + 1}."
            elif k == 'left':
                cap = f"Probe {mid} = cell ({mid // n},{mid % n}) = {e['val']} > {target}: the target is earlier. hi = {mid - 1}."
            elif k == 'found':
                cap = f"Probe {mid} = cell ({mid // n},{mid % n}) = {e['val']}: found it. Return true."
                hold = END
            else:
                cap = f"lo ({lo}) has passed hi ({hi}): no positions left. Return false."
                hold = END
            if k in ('right', 'left') and 'probe' not in first:
                first.add('probe')
                sub = "Each probe throws away half of what's left, including mid itself."
                hold = KEY
            if k == 'found' and not sub:
                sub = f"{m * n} cells, and a binary search needs at most about log2({m * n}) + 1 probes."
        for key in ((k, mid), k):
            if key in notes:
                sub, hold = notes[key], max(hold, KEY)
                break
        arr = ArrayView(flat, {p: st[p] for p in range(m * n)},
                        pointers=({'mid': mid} if k == 'found' else
                                  {'lo': live[0], 'hi': live[1], **({'mid': mid} if mid is not None else {})}),
                        title='as a list')
        grid = GridView(cells, outlines=rings, bridges=False, cell=min(66, int(300 / m)))
        sc.frame([grid, arr], cap, sub, hold, side=MapView(side, 'Binary search', headers=('', '')), legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(*HARD1, 'A 2 × 5 grid, target 19. Wider than tall, so rows and columns differ a lot.',
                {('right', 4): "Divide by the number of ROWS (2) instead and position 4 is 'row 2': there is no row 2.",
                 'found': "Both LeetCode samples use the same 3 × 4 grid, so dividing by rows gets past them; here it crashes."},
                show_rows_bug=True)
    sc2 = build(*HARD2, 'A 4 × 3 grid, target 19: the first number of row 2.',
                {'start': "The target starts a row. Picking a row first with 'first number < target' skips past it.",
                 'found': "Two searches with a strict < choose row 1 (it starts with 10) and answer false. One flat search has no row step to get wrong."})
    return [(sc1, "A 2 × 5 grid. Turning a position into a cell with the number of rows instead of columns passes "
                  "both LeetCode samples, but here the first probe already points at a row that doesn't exist."),
            (sc2, "19 is the first number in its row. Finding the row first with 'first number < target' passes both "
                  "samples, then searches the row above and answers false.")]


def main():
    args = cli()
    sc = build(MATRIX, TARGET, 'LeetCode example 1: is 3 in the grid? Each row is sorted and starts above the last.')
    finish(sc, 74, "Watch how each probe's position becomes a cell: divide by the number of columns for the "
                   "row, take the remainder for the column.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
