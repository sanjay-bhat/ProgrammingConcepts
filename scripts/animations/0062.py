#!/usr/bin/env python3
"""#62 Unique Paths: every square's count is the count above it plus the count
to its left, and the corner's count is the number of ways to choose which of
the moves go down.

The notebook's Python answer is one call, math.comb(m + n - 2, m - 1). The
number of paths to square (r, c) is the answer for an (r+1) x (c+1) grid, so
every box below is filled by RUNNING that solution, unchanged, and the script
checks that each box equals above + left before drawing the arrows. The final
frames run the multiply-then-divide loop from the C#/Go/Rust cells.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

M, N = 3, 7   # LeetCode example 1: answer 28

# The hard example (interactive page only): a 3×4 grid, answer 10. Dividing
# before multiplying, result / (i + 1) * (total - i), passes both LeetCode
# samples (3×7 and 3×2) but here does 5 / 2 = 2 in whole numbers, then 2 × 4 = 8.
# Notes are keyed by ('loop', step number) or 'done' and replace that frame's
# second caption line (held as a KEY moment).
HARD_M, HARD_N = 3, 4
HARD_NOTES = {
    ('loop', 2): "Divide first and 5 / 2 = 2 in whole numbers loses the half: 2 × 4 = 8, not 10.",
    'done': "Dividing before multiplying answers 8 here, though it gets both LeetCode samples right.",
}


# ---- the notebook's solution, unchanged ----
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)


def loop_trace(m, n):
    """The C#/Go/Rust loop, with its steps recorded."""
    steps = []
    result = 1
    k = min(m - 1, n - 1)
    total = m + n - 2
    for i in range(k):
        before = result
        result = result * (total - i) // (i + 1)
        steps.append((before, total - i, i + 1, result))
    return steps


def trace(m, n):
    sol = Solution()
    events = [dict(kind='start')]
    grid = [[None] * n for _ in range(m)]
    for c in range(n):
        grid[0][c] = sol.uniquePaths(1, c + 1)
    events.append(dict(kind='row0', grid=[r[:] for r in grid]))
    for r in range(m):
        grid[r][0] = sol.uniquePaths(r + 1, 1)
    events.append(dict(kind='col0', grid=[r[:] for r in grid]))
    for r in range(1, m):
        for c in range(1, n):
            grid[r][c] = sol.uniquePaths(r + 1, c + 1)
            assert grid[r][c] == grid[r - 1][c] + grid[r][c - 1]
            events.append(dict(kind='cell', r=r, c=c, grid=[x[:] for x in grid]))
    events.append(dict(kind='choose', grid=grid, ans=sol.uniquePaths(m, n)))
    for st in loop_trace(m, n):
        events.append(dict(kind='loop', step=st, grid=grid))
    events.append(dict(kind='done', grid=grid, ans=sol.uniquePaths(m, n)))
    return events


def build(M, N, subtitle, notes=None):
    sc = Scene('#62 Unique Paths: each square = above + left', subtitle)
    legend = [(ACTIVE, 'just filled'), (style('good')[1], 'filled'), (style('gold')[1], 'edges: one path')]
    loop_lines = []
    total, downs, rights = M + N - 2, M - 1, N - 1
    for e in trace(M, N):
        k, g = e['kind'], e.get('grid')
        styles, links, rings = {}, [], []
        vals = [[('' if v is None else v) for v in row] for row in (g or [[None] * N for _ in range(M)])]
        for r in range(M):
            for c in range(N):
                if g and g[r][c] is not None:
                    styles[(r, c)] = 'gold' if (r == 0 or c == 0) else 'good'
        hold = STEP
        rows = []
        if k == 'start':
            cap, sub, hold = ("dp[r][c] = how many different paths reach square (r, c).",
                              f"The answer is the bottom-right box. Start = (0, 0), finish = ({M - 1}, {N - 1}).", STEP)
            styles[(0, 0)] = 'active'; styles[(M - 1, N - 1)] = 'active'
        elif k == 'row0':
            cap, sub, hold = ("Top row: every box is 1. The only way along it is right, right, right.",
                              "These come from math.comb(c, 0) = 1. No arrows: nothing above them.", KEY)
            rings = [((0, c), ACTIVE) for c in range(N)]
        elif k == 'col0':
            cap, sub, hold = ("Left column: also 1 each. The only way down it is down, down.",
                              "The edges are the starting values every other box is built from.", KEY)
            rings = [((r, 0), ACTIVE) for r in range(M)]
        elif k == 'cell':
            r, c = e['r'], e['c']
            up, left = g[r - 1][c], g[r][c - 1]
            styles[(r, c)] = 'active'
            links = [dict(src=(r - 1, c), dst=(r, c)), dict(src=(r, c - 1), dst=(r, c))]
            rings = [((r, c), ACTIVE)]
            rows = [('from above', str(up)), ('from the left', str(left)), ('total', str(g[r][c]), 'active')]
            if (r, c) == (1, 1):
                cap = f"(1,1) = {up} + {left} = {g[r][c]}. The last move was either down or right."
                sub = "Every path in arrives from above or from the left, never both, so add them."
                hold = KEY
            elif (r, c) == (M - 1, N - 1):
                cap = f"The corner: {up} from above + {left} from the left = {g[r][c]}."
                sub = "That's the answer. Now see why it's also a 'choose' number."
                hold = KEY
            else:
                cap = f"({r},{c}) = {up} from above + {left} from the left = {g[r][c]}."
                sub = ''
                hold = QUICK * 2 if r == 2 else QUICK * 1.6
        elif k == 'choose':
            ans = e['ans']
            cap = (f"Every path is {total} moves: {downs} downs and {rights} rights. "
                   f"Pick which {downs} are downs: C({total}, {downs}) = {ans}.")
            sub = f"The notebook skips the table and computes that number directly: math.comb({total}, {downs})."
            hold = KEY
            rings = [((M - 1, N - 1), style('good')[1])]
            rows = [('moves', f'{total} = {downs} down + {rights} right'), ('choose', f'C({total}, {downs})'),
                    ('answer', str(ans), 'good')]
        elif k == 'loop':
            before, mul, div, res = e['step']
            loop_lines.append(f'{before} × {mul} / {div} = {res}')
            cap = f"The C#/Go/Rust loop: {before} × {mul} / {div} = {res}."
            sub = ("Multiply first, then divide: the division always comes out exact." if div == 1 else
                   f"After step i the running value is C({total}, i), so it's always a whole number.")
            hold = STEP
            if notes and ('loop', div) in notes:
                sub, hold = notes[('loop', div)], KEY
            rings = [((M - 1, N - 1), style('good')[1])]
            rows = [('step', l) for l in loop_lines]
        else:
            cap = f"uniquePaths({M}, {N}) returns {e['ans']}."
            sub = notes['done'] if notes else "The table costs m × n steps; the formula takes min(m, n) - 1 multiplications."
            hold = END
            rings = [((M - 1, N - 1), style('good')[1])]
            rows = [('step', l) for l in loop_lines] + [('answer', str(e['ans']), 'good')]
        table = DPTableView(vals, row_labels=[f'r={r}' for r in range(M)],
                            col_labels=[f'c={c}' for c in range(N)],
                            styles=styles, rings=rings, links=links, max_cell=58, gap=16)
        side = MapView(rows, 'Working', headers=('', ''), empty='')
        sc.frame([table], cap, sub, hold, side=side, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    sc = build(HARD_M, HARD_N, f'm = {HARD_M}, n = {HARD_N}. Watch the loop at the end: multiply first, then divide.',
               HARD_NOTES)
    return sc, ("A 3×4 grid, answer 10. Dividing before multiplying gets both LeetCode samples right, then "
                "here 5 / 2 rounds down to 2 and the loop answers 8. Watch the loop's second step.")


def main():
    args = cli()
    sc = build(M, N, 'Robot starts top-left, moves only right or down. Box = number of paths that reach it.')
    finish(sc, 62, "Watch square (1,1): its 2 is the 1 above plus the 1 to its left, and that "
                   "same 'above + left' rule builds the corner's 28.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
