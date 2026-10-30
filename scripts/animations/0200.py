#!/usr/bin/env python3
"""#200 Number of Islands: the sweep finds land, sink() erases the whole island.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

GRID = ["11000", "11000", "00100", "00011"]          # LeetCode example 2
DIAGONAL = {(2, 2)}                                   # touches island 1 only at a corner

# The hard example (interactive page only): a ring of land around a lake with an
# island inside it, a square touching two islands only at corners, and a ring
# long enough to stack 16 sink() calls. Answer: 4.
HARD = ["1111100", "1000101", "1010101", "1000101", "1111101", "0000010"]
HARD_NOTES = {
    (0, 0): "It's the corner of a big ring. Watch how deep the call stack gets as sink walks all the way round.",
    (1, 6): "A separate column on the right: the ring never touches it.",
    (2, 2): "It sits in the lake inside the ring. Water on all four sides, so it's its own island.",
    (5, 5): "It touches the ring and the column, but only at corners, which don't connect.",
}


def trace(rows):
    grid = [list(r) for r in rows]
    m, n = len(grid), len(grid[0])
    owner = [[0] * n for _ in range(m)]
    calls, events = [], []
    st = {'count': 0, 'sweep': None}

    def rec(kind, **kw):
        events.append(dict(kind=kind, grid=[r[:] for r in grid], owner=[r[:] for r in owner],
                           calls=list(calls), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            if 0 <= i < m and 0 <= j < n:
                rec('reject', cell=(i, j), why='sunk' if owner[i][j] else 'water')
            else:
                rec('offgrid', tried=(i, j))
            return
        grid[i][j] = '0'
        owner[i][j] = st['count']
        calls.append((i, j))
        rec('sink', cell=(i, j))
        dfs(i + 1, j)   # down
        dfs(i - 1, j)   # up
        dfs(i, j + 1)   # right
        dfs(i, j - 1)   # left
        calls.pop()
        rec('return', cell=(i, j))

    rec('start')
    for i in range(m):
        for j in range(n):
            st['sweep'] = (i, j)
            if grid[i][j] == '1':
                st['count'] += 1
                rec('found', cell=(i, j))
                dfs(i, j)
            else:
                rec('skip', cell=(i, j), why='sunk' if owner[i][j] else 'water')
    st['sweep'] = None
    rec('done')
    return events


def words(e, notes=None):
    k, c = e['kind'], e.get('cell')
    if k == 'start':
        return ("Sweep every square, left to right, top to bottom.",
                "Each time we land on a 1, it's a new island: count it, then sink the whole thing.", KEY)
    if k == 'skip':
        if e['why'] == 'sunk':
            return (f"({c[0]},{c[1]}) was land, but it's 0 now: we sank it with island {e['owner'][c[0]][c[1]]}.",
                    "That's why it isn't counted twice. This is the whole trick.", KEY)
        return (f"({c[0]},{c[1]}) is water. Nothing to do.", "", QUICK * 0.8)
    if k == 'found':
        if notes is not None:
            extra = notes.get(c, "Count it, then sink every square connected to it.")
        else:
            extra = ("It touches island 1 only at a corner, and corners don't connect."
                     if c in DIAGONAL else "Count it, then sink every square connected to it.")
        return (f"({c[0]},{c[1]}) is land the sweep hasn't seen. New island: count = {e['count']}.", extra, KEY)
    if k == 'sink':
        return (f"sink({c[0]},{c[1]}): set it to 0 FIRST, then try down, up, right, left.",
                "Marking before recursing stops two neighbours calling each other forever.", STEP)
    if k == 'reject':
        why = "already sunk (0)" if e['why'] == 'sunk' else "water"
        return (f"Try ({c[0]},{c[1]}): {why}, so return straight away.", "", QUICK)
    if k == 'offgrid':
        t = e['tried']
        return (f"Try ({t[0]},{t[1]}): off the grid, so return straight away.", "", QUICK * 0.9)
    if k == 'return':
        return (f"sink({c[0]},{c[1]}) has tried all four neighbours, so it returns.", "", QUICK * 1.2)
    return (f"Sweep finished. Answer: {e['count']} islands.",
            "Every square was sunk at most once, so it's O(m×n) time.", END)


def cells(e):
    out = []
    for i, row in enumerate(e['grid']):
        out.append([])
        for j, v in enumerate(row):
            o = e['owner'][i][j]
            if o:
                out[-1].append({'style': f'region{o - 1}', 'label': '0', 'sub': f'island {o}'})
            elif v == '1':
                out[-1].append({'style': 'land', 'label': '1'})
            else:
                out[-1].append({'water': True})
    return out


def build(grid, subtitle, notes=None):
    sc = Scene('#200 Number of Islands: sweep and sink', subtitle)
    legend = [(CURSOR, 'sweep position'), (ACTIVE, 'being sunk'), (REJECT, 'returns at once')]
    for e in trace(grid):
        rings = []
        if e['sweep']:
            rings.append((e['sweep'], CURSOR, 3))
        if e['kind'] in ('sink', 'found'):
            rings.append((e['cell'], ACTIVE, 5))
        marks = {}
        if e['kind'] == 'reject':
            rings.append((e['cell'], REJECT, 3))
            marks[e['cell']] = '×'
        stack = [(f'sink({i},{j})', f'region{e["owner"][i][j] - 1}') for i, j in e['calls']]
        sw = e['sweep']
        cap, sub, hold = words(e, notes)
        sc.frame(GridView(cells(e), outlines=rings, marks=marks), cap, sub, hold,
                 side=StackView(stack, 'Call stack', base=f'numIslands  sweep at {sw if sw else "-"}',
                                empty='(empty: no island being sunk)'),
                 counters={'islands': e['count']}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    sc = build(HARD, 'Hard example: a ring around a lake, an island in the lake, and corner-only touches.',
               HARD_NOTES)
    return sc, ("A 6×7 grid built to break first attempts: the lake's island must not join the ring, "
                "the bottom-right square touches two islands only at corners, and the ring stacks 16 calls deep.")


def main():
    args = cli()
    sc = build(GRID, '1 = land, slashed = water (0). Only up/down/left/right count as connected.')
    finish(sc, 200, "Watch the sweep reach (0,1): it was land, but island 1's sink already "
                    "turned it to 0, so it isn't counted again. That's the whole trick.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
