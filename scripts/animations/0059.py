#!/usr/bin/env python3
"""#59 Spiral Matrix II: four walls close in. Fill along a wall, move that wall
inward at once, repeat while the walls haven't crossed.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

N = 3   # LeetCode example 1

# The hard example (interactive page only): n = 4, even, so there is no middle
# square. Filling the rings and then writing n*n into matrix[n//2][n//2] passes
# both LeetCode samples (n = 3 and n = 1, both odd), but here it overwrites the
# 15 at (2,2) with a second 16. Answer [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]].
HARD_N = 4
HARD_NOTES = {
    ('fill', 15): "15 lands on (2,2), which is matrix[n//2][n//2]. A 'fill the rings, then write n² in the middle' "
                  "solution would overwrite it with 16 later.",
    ('fill', 16): "16 goes to (2,1). The inner ring is 2 × 2 and has no middle square at all.",
    'done': "Even n ends on a 2 × 2 ring. Both LeetCode samples are odd, so a middle-square special case passes "
            "them and fails here with two 16s and no 15.",
}

PASS_STYLE = {'right': 'region1', 'down': 'region0', 'left': 'region3', 'up': 'region2'}
PASS_WORDS = {'right': 'along the top wall, left to right', 'down': 'down the right wall',
              'left': 'back along the bottom wall, right to left', 'up': 'up the left wall'}


class Solution:
    """The notebook's solution, to cross-check the traced run."""
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                matrix[top][col] = num; num += 1
            top += 1
            for row in range(top, bottom + 1):
                matrix[row][right] = num; num += 1
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num; num += 1
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num; num += 1
                left += 1
        return matrix


def rings_then_middle(n):
    """First attempt: fill n // 2 rings, then always write n*n into the middle."""
    m, num = [[0] * n for _ in range(n)], 1
    for k in range(n // 2):
        for c in range(k, n - 1 - k): m[k][c] = num; num += 1
        for r in range(k, n - 1 - k): m[r][n - 1 - k] = num; num += 1
        for c in range(n - 1 - k, k, -1): m[n - 1 - k][c] = num; num += 1
        for r in range(n - 1 - k, k, -1): m[r][k] = num; num += 1
    m[n // 2][n // 2] = n * n
    return m


def trace(n):
    who = [[None] * n for _ in range(n)]
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, m=[r[:] for r in matrix], who=[r[:] for r in who],
                           walls=(top, bottom, left, right), num=num, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    rec('start')
    lap = 0
    while top <= bottom and left <= right:
        lap += 1
        rec('lap', lap=lap)
        for col in range(left, right + 1):
            matrix[top][col] = num; who[top][col] = 'right'; num += 1
            rec('fill', cell=(top, col), d='right', k=col - left)
        top += 1
        rec('wall', name='top', line=('row', top - 1))
        for row in range(top, bottom + 1):
            matrix[row][right] = num; who[row][right] = 'down'; num += 1
            rec('fill', cell=(row, right), d='down', k=row - top)
        right -= 1
        rec('wall', name='right', line=('col', right + 1))
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num; who[bottom][col] = 'left'; num += 1
                rec('fill', cell=(bottom, col), d='left', k=right - col)
            bottom -= 1
            rec('wall', name='bottom', line=('row', bottom + 1))
        else:
            rec('guard', name='bottom')
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num; who[row][left] = 'up'; num += 1
                rec('fill', cell=(row, left), d='up', k=bottom - row)
            left += 1
            rec('wall', name='left', line=('col', left - 1))
        else:
            rec('guard', name='left')
    rec('done')
    assert matrix == Solution().generateMatrix(n)
    return events


def build(n, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#59 Spiral Matrix II: four walls closing in', subtitle, side_width=280)
    legend = [(style('region1')[1], '→ top pass'), (style('region0')[1], '↓ right pass'),
              (style('region3')[1], '← bottom pass'), (style('region2')[1], '↑ left pass'),
              (ACTIVE, 'just written')]
    seen = set()
    for e in trace(n):
        k = e['kind']
        t, b, l, r = e['walls']
        cells = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                d = e['who'][i][j]
                if d:
                    cells[i][j] = {'style': PASS_STYLE[d], 'label': str(e['m'][i][j])}
                elif t <= i <= b and l <= j <= r:
                    cells[i][j] = {'style': 'plain', 'label': ''}
        outlines = []
        hold = STEP
        sub = ''
        if k == 'start':
            cap = f"An empty {n} × {n} grid. The walls start on the outer rows and columns."
            sub = "top/bottom = first/last row still empty, left/right = first/last column still empty."
        elif k == 'lap':
            cap = f"Lap {e['lap']}: the walls are top={t}, bottom={b}, left={l}, right={r}."
            sub = "top ≤ bottom and left ≤ right, so there's still room: go round once more."
            hold = STEP if e['lap'] == 1 else KEY
            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    outlines.append(((i, j), style('window')[1], 2))
        elif k == 'fill':
            i, j = e['cell']
            outlines = [((i, j), ACTIVE, 4)]
            cap = f"Write {e['num'] - 1} at ({i},{j}), {PASS_WORDS[e['d']]}."
            if e['k'] == 0 and e['d'] not in seen:
                seen.add(e['d'])
                hold = STEP
            else:
                hold = QUICK * 1.6
        elif k == 'wall':
            name = e['name']
            kind, idx = e['line']
            cells_done = [(idx, j) for j in range(n)] if kind == 'row' else [(i, idx) for i in range(n)]
            outlines = [(c, ACTIVE, 3) for c in cells_done if e['who'][c[0]][c[1]]]
            new = {'top': t, 'right': r, 'bottom': b, 'left': l}[name]
            cap = f"That {kind} is full: move {name} inward to {new}."
            if ('wall', name) not in seen:
                seen.add(('wall', name))
                hold = KEY if name == 'top' else STEP
                sub = ("Right away, before the next pass: the corner is done, so the down pass starts a row lower "
                       "and can't write it twice." if name == 'top' else "")
            else:
                hold = QUICK * 2
        elif k == 'guard':
            name = e['name']
            cap = (f"Check before the {name} pass: {'top ≤ bottom' if name == 'bottom' else 'left ≤ right'} "
                   "is false, so skip it.")
            sub = "In a square that pass would be empty anyway. In a rectangle this check stops a double walk."
            hold = STEP
        else:
            cap = f"The walls have crossed (top={t} > bottom={b}). Every square from 1 to {n * n} is written once."
            sub = notes.get('done', "One write per square: O(n²) time, and four walls are the only extra memory.")
            hold = END
        key = ('fill', e['num'] - 1) if k == 'fill' else None
        if key in notes:
            sub, hold = notes[key], KEY
        rows = [('top', str(t)), ('bottom', str(b)), ('left', str(l)), ('right', str(r)),
                ('next num', str(e['num']) if k != 'done' else '—')]
        if k == 'wall':
            rows = [(a, v, 'active') if a == e['name'] else (a, v) for a, v in rows]
        sc.frame([GridView(cells, outlines=outlines, bridges=False)], cap, sub, hold,
                 side=MapView(rows, 'Walls', headers=('name', 'value')), legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    want = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    assert Solution().generateMatrix(HARD_N) == want
    assert rings_then_middle(HARD_N) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 16, 6], [10, 9, 8, 7]]
    assert rings_then_middle(3) == Solution().generateMatrix(3) and rings_then_middle(1) == [[1]]
    sc = build(HARD_N, 'n = 4: even, so there is no middle square. The inner ring is 2 × 2.', HARD_NOTES)
    return sc, ("n = 4 has no middle square. Filling rings and then writing n² into the middle passes both "
                "LeetCode samples (both odd) but here overwrites the 15 with a second 16. Watch 15 land on (2,2).")


def main():
    args = cli()
    sc = build(N, f'n = {N}. Write 1 to {N * N} clockwise, from the top-left corner inward.')
    finish(sc, 59, "Watch the top wall move down right after the first pass: that's why the down pass starts "
                   "below the corner instead of writing over the 3.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
