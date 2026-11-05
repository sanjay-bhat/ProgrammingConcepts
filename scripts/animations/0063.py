#!/usr/bin/env python3
"""#63 Unique Paths II: routes into a square = routes into the square above +
routes into the square to its left; an obstacle holds 0. The code keeps only
one row, dp, and updates it in place.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The 2D table drawn is dp[j] right
after square (i, j) is processed, which is that square's route count.
"""
import math
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

GRID = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]   # LeetCode example 1: answer 2

# Hard examples (interactive page only), each breaking a plausible first attempt
# that passes both LeetCode samples.
# 1) Obstacles on the top row and the left column. Setting the first row and
#    column to 1 except on the obstacles themselves counts (0,3) and (3,0) as
#    reachable: 14 instead of 12.
HARD_EDGE = [[0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
# 2) Two obstacles on one diagonal. #62's formula minus the paths through each
#    obstacle subtracts the 8 paths through both twice: 20 - 12 - 12 = -4, not 4.
HARD_DIAG = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
NOTES_EDGE = {
    (0, 3): "(0,3) is open but gets 0: on the top row the only way in is from the left, and the obstacle is in "
            "the way. 'Top row = 1 unless it's an obstacle' would put a 1 here.",
    (3, 0): "Same on the left column: (3,0) is open, but the only way in is from above, through the obstacle. 0.",
    'done': "12 routes. Edge squares set to 1 'unless they're an obstacle' would count (0,3) and (3,0) and give 14.",
}
NOTES_DIAG = {
    (1, 1): "First obstacle. 2 routes reach it and 6 leave it for the corner, so 12 routes go through it.",
    (2, 2): "Second obstacle, also on 12 routes. But 8 routes pass through BOTH obstacles.",
    'done': "4 routes. #62's 20, minus 12 through each obstacle, gives −4: the 8 routes through both are "
            "subtracted twice. The table never subtracts, so it can't double-count.",
}


class Solution:
    """The notebook's solution, to cross-check the traced run."""
    def uniquePathsWithObstacles(self, obstacle_grid):
        m, n = len(obstacle_grid), len(obstacle_grid[0])
        dp = [0] * n
        dp[0] = 0 if obstacle_grid[0][0] == 1 else 1
        for i in range(m):
            for j in range(n):
                if obstacle_grid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[-1]


def edges_all_ones(g):
    """First attempt: first row and column are 1 unless that square is an obstacle."""
    m, n = len(g), len(g[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 0 if g[i][0] else 1
    for j in range(n):
        dp[0][j] = 0 if g[0][j] else 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = 0 if g[i][j] else dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


def subtract_each_obstacle(g):
    """First attempt: #62's formula minus the paths through each obstacle."""
    m, n = len(g), len(g[0])
    paths = lambda a, b: math.comb(a + b - 2, a - 1)
    total = paths(m, n)
    for i in range(m):
        for j in range(n):
            if g[i][j]:
                total -= paths(i + 1, j + 1) * paths(m - i, n - j)
    return total


def trace(g):
    m, n = len(g), len(g[0])
    table = [[None] * n for _ in range(m)]
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, dp=list(dp), table=[r[:] for r in table], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    dp = [0] * n
    dp[0] = 0 if g[0][0] == 1 else 1
    rec('seed')
    for i in range(m):
        for j in range(n):
            above = dp[j]
            if g[i][j] == 1:
                dp[j] = 0
                table[i][j] = 0
                rec('wall', i=i, j=j, above=above)
            elif j > 0:
                left = dp[j - 1]
                dp[j] += dp[j - 1]
                table[i][j] = dp[j]
                rec('add', i=i, j=j, above=above, left=left)
            else:
                table[i][j] = dp[j]
                rec('keep', i=i, j=j, above=above)
    rec('done', ans=dp[-1])
    assert dp[-1] == Solution().uniquePathsWithObstacles(g)
    return events


def build(g, subtitle, notes=None):
    notes = notes or {}
    m, n = len(g), len(g[0])
    sc = Scene('#63 Unique Paths II: above + left, obstacles hold 0', subtitle, side_width=270)
    legend = [(ACTIVE, 'just filled'), (style('good')[1], 'routes reach it'), (style('muted')[1], 'no route'),
              (style('bad')[1], 'obstacle'), (style('window')[1], 'dp: this row already')]
    first_add = True
    for e in trace(g):
        k = e['kind']
        t = e['table']
        vals, styles = [], {}
        for i in range(m):
            row = []
            for j in range(n):
                if g[i][j]:
                    row.append('#'); styles[(i, j)] = 'bad'
                elif t[i][j] is None:
                    row.append('')
                else:
                    row.append(t[i][j]); styles[(i, j)] = 'good' if t[i][j] else 'muted'
            vals.append(row)
        links, rings = [], []
        dp_styles, ptr = {}, {}
        hold, sub = STEP, ''
        if k == 'seed':
            cap = ("dp[0] = 1: one route to the start square." if e['dp'][0] else
                   "The start square is an obstacle: dp[0] = 0, and nothing will ever get a route.")
            sub = "The rest of dp is 0: an imaginary row above the grid that no route comes from."
            hold = KEY
            dp_styles = {0: 'active'}
        elif k == 'done':
            ans = e['ans']
            cap = f"Answer: dp[{n - 1}] = {ans}."
            sub = notes.get('done', "One pass over the squares, O(m × n), with one row of memory, O(n).")
            hold = END
            rings = [((m - 1, n - 1), style('good')[1])]
        else:
            i, j = e['i'], e['j']
            styles[(i, j)] = 'bad' if k == 'wall' else 'active'
            rings = [((i, j), ACTIVE)]
            ptr = {'j': j}
            dp_styles = {x: ('window' if x < j else 'plain') for x in range(n)}
            dp_styles[j] = 'active'
            if k == 'wall':
                cap = f"({i},{j}) is an obstacle: dp[{j}] = 0."
                sub = "Set it to 0, don't skip it: the old value from above would leak into the next square."
                hold = KEY if (i, j) == (1, 1) or (i, j) in notes else STEP
            elif k == 'keep':
                cap = f"({i},{j}): left column, nothing to its left. dp[0] keeps {e['above']} from above."
                if i > 0:
                    links = [dict(src=(i - 1, j), dst=(i, j))]
                hold = QUICK * 2
            else:
                a, l = e['above'], e['left']
                cap = f"({i},{j}) = {a} from above + {l} from the left = {a + l}."
                if i > 0:
                    links.append(dict(src=(i - 1, j), dst=(i, j), cross=(g[i - 1][j] == 1)))
                links.append(dict(src=(i, j - 1), dst=(i, j), cross=(g[i][j - 1] == 1)))
                if first_add and i > 0:
                    sub = (f"dp[{j}] still held {a}, the square above; dp[{j - 1}] was just updated to {l}, "
                           "this row's left neighbour. So dp[j] += dp[j-1] is above + left.")
                    hold = KEY
                    first_add = False
                elif i == 0:
                    sub = "Top row: nothing above, so it copies its left neighbour." if j == 1 else ''
                    hold = QUICK * 2
                else:
                    hold = QUICK * 2.4
            if (i, j) in notes:
                sub, hold = notes[(i, j)], KEY
        table = DPTableView(vals, row_labels=[f'r{i}' for i in range(m)], col_labels=[f'c{j}' for j in range(n)],
                            styles=styles, rings=rings, links=links, max_cell=60, gap=14)
        dpv = ArrayView(e['dp'], styles=dp_styles, pointers=ptr, title='dp', cell=46)
        rows = [('dp', str(e['dp']))]
        if k in ('add', 'keep', 'wall'):
            rows += [('above', str(e['above']))]
            if k == 'add':
                rows += [('left', str(e['left'])), ('new dp[j]', str(e['above'] + e['left']), 'active')]
        sc.frame([table, dpv], cap, sub, hold, side=MapView(rows, 'This step', headers=('', '')), legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = [([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2), ([[0, 1], [0, 0]], 1)]
    for f in (edges_all_ones, subtract_each_obstacle):
        assert all(f(g) == want for g, want in samples)
    assert Solution().uniquePathsWithObstacles(HARD_EDGE) == 12 and edges_all_ones(HARD_EDGE) == 14
    assert Solution().uniquePathsWithObstacles(HARD_DIAG) == 4 and subtract_each_obstacle(HARD_DIAG) == -4
    edge = build(HARD_EDGE, 'Obstacles on the top row and the left column. Answer 12.', NOTES_EDGE)
    diag = build(HARD_DIAG, 'Two obstacles on one diagonal. Answer 4.', NOTES_DIAG)
    return [
        (edge, "An obstacle on each edge. Setting the top row and left column to 1 except on obstacles passes both "
               "samples, then counts the cut-off squares (0,3) and (3,0) and answers 14; the answer is 12."),
        (diag, "Two obstacles on one diagonal. #62's formula minus the paths through each obstacle passes both "
               "samples, then subtracts the 8 routes through both twice and answers −4; the answer is 4."),
    ]


def main():
    args = cli()
    sc = build(GRID, 'Right or down only; # is an obstacle. Box = routes that reach that square.')
    finish(sc, 63, "Watch (1,2): its 1 comes only from above, because the obstacle to its left holds 0, and that "
                   "0 is why the corner ends up with 2.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
