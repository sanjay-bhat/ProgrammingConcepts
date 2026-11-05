#!/usr/bin/env python3
"""#64 Minimum Path Sum: the cheapest way into a square is the cheaper of the
square above and the square to its left, plus its own cost. The code keeps one
row, dp, and overwrites it in place.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The table drawn is dp[j] right after
square (i, j) is written, which is the cheapest cost to reach that square.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

GRID = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]   # LeetCode example 1: answer 7

# Hard examples (interactive page only), each breaking a plausible first attempt.
# 1) Greedy: step to the cheaper neighbour each time. It runs along the cheap top
#    row and is forced through the 9 below it: 15. Answer 12 (down the left side).
HARD_GREEDY = [[1, 1, 1, 1], [2, 9, 9, 1], [2, 9, 9, 9], [2, 2, 2, 1]]
# 2) Python inner loop from j = 0: dp[j - 1] is dp[-1], the LAST column, so the
#    left column can borrow the right column's cost. Passes both LeetCode samples;
#    here it answers 8 instead of 14.
HARD_WRAP = [[1, 1, 1], [9, 9, 1], [1, 9, 9], [1, 1, 1]]
NOTES_GREEDY = {
    (1, 0): "Going down costs 2 here, more than the 1 to the right, so a greedy walker never comes this way. "
            "The table fills it anyway: 3.",
    (2, 3): "14: the right column is expensive below row 1. Greedy, already committed to the top row, has to pay it.",
    'done': "12, down the left and along the bottom. Picking the cheaper next square runs along the top row and "
            "pays the 9: 15.",
}
NOTES_WRAP = {
    (2, 0): "Left column: only from above, 10 + 1 = 11. An inner loop from j = 0 would compute min(dp[0], dp[-1]): "
            "dp[-1] is the right column's 4, so it would write 5, a jump no route can make.",
    'done': "14. With the loop starting at 0, the left column borrows that 4 and the answer comes out 8, while both "
            "LeetCode samples still pass.",
}


class Solution:
    """The notebook's solution, to cross-check the traced run."""
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]


def greedy(grid):
    """First attempt: always step to the cheaper of right and down."""
    m, n = len(grid), len(grid[0])
    i = j = 0
    total = grid[0][0]
    while (i, j) != (m - 1, n - 1):
        if i == m - 1:
            j += 1
        elif j == n - 1:
            i += 1
        elif grid[i][j + 1] <= grid[i + 1][j]:
            j += 1
        else:
            i += 1
        total += grid[i][j]
    return total


def loop_from_zero(grid):
    """First attempt: the inner loop starts at 0, so dp[-1] wraps to the last column."""
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]
    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(n):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    return dp[-1]


def trace(grid):
    m, n = len(grid), len(grid[0])
    table = [[None] * n for _ in range(m)]
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, dp=list(dp), table=[r[:] for r in table], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    dp = [0] * n
    dp[0] = grid[0][0]
    table[0][0] = dp[0]
    rec('start', i=0, j=0)
    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]
        table[0][j] = dp[j]
        rec('top', i=0, j=j, left=dp[j - 1])
    for i in range(1, m):
        above = dp[0]
        dp[0] += grid[i][0]
        table[i][0] = dp[0]
        rec('left', i=i, j=0, above=above)
        for j in range(1, n):
            above, left = dp[j], dp[j - 1]
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
            table[i][j] = dp[j]
            rec('cell', i=i, j=j, above=above, left=left)
    # walk back from the corner along whichever neighbour gave the minimum
    path, i, j = [(m - 1, n - 1)], m - 1, n - 1
    while (i, j) != (0, 0):
        if i == 0 or (j > 0 and table[i][j - 1] < table[i - 1][j]):
            j -= 1
        else:
            i -= 1
        path.append((i, j))
    rec('done', ans=dp[-1], path=path)
    assert dp[-1] == Solution().minPathSum(grid)
    return events


class Stack(View):
    """Side-panel helper: draws its views top to bottom (the page renders it as a container)."""

    def __init__(self, views):
        self.views = views

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        y = y0
        for v in self.views:
            v.draw(p, (x0, y, x1, y1))
            y += v.used + 8
        self.used = y - y0


def build(grid, subtitle, notes=None):
    notes = notes or {}
    m, n = len(grid), len(grid[0])
    sc = Scene('#64 Minimum Path Sum: cheaper of above and left, plus own cost', subtitle, side_width=250)
    legend = [(ACTIVE, 'just filled'), (style('good')[1], 'cheapest cost known'), (style('window')[1], 'cheapest route'),
              (style('gold')[1], 'dp: this row already')]
    first_cell = True
    for e in trace(grid):
        k, t = e['kind'], e['table']
        vals = [['' if v is None else v for v in r] for r in t]
        styles = {(i, j): 'good' for i in range(m) for j in range(n) if t[i][j] is not None}
        links, rings, cost_rings = [], [], []
        dp_styles, ptr = {}, {}
        hold, sub = STEP, ''
        if k != 'done':
            i, j = e['i'], e['j']
            styles[(i, j)] = 'active'
            rings = [((i, j), ACTIVE)]
            cost_rings = [((i, j), ACTIVE)]
            ptr = {'j': j}
            dp_styles = {x: ('gold' if x < j else 'plain') for x in range(n)}
            if i == 0:
                dp_styles = {x: ('gold' if x <= j else 'muted') for x in range(n)}
            dp_styles[j] = 'active'
        if k == 'start':
            cap = f"dp[0] = {grid[0][0]}: reaching the start costs the start square itself."
            sub = "Every box will hold the cheapest total cost of any route that reaches that square."
            hold = KEY
        elif k == 'top':
            i, j = e['i'], e['j']
            links = [dict(src=(0, j - 1), dst=(0, j))]
            cap = f"Top row: {e['left']} + {grid[0][j]} = {t[0][j]}. Only reachable from the left."
            sub = "A running sum. No min here: there's no row above to compare with." if j == 1 else ''
            hold = STEP if j == 1 else QUICK * 2
        elif k == 'left':
            i = e['i']
            links = [dict(src=(i - 1, 0), dst=(i, 0))]
            cap = f"Left column: {e['above']} + {grid[i][0]} = {t[i][0]}. Only reachable from above."
            sub = "That's why dp[0] gets its own line and the inner loop starts at 1." if i == 1 else ''
            hold = STEP if i == 1 else QUICK * 2
        elif k == 'cell':
            i, j, a, l = e['i'], e['j'], e['above'], e['left']
            win = 'above' if a < l else 'left'
            links = [dict(src=(i - 1, j), dst=(i, j), cross=(win != 'above')),
                     dict(src=(i, j - 1), dst=(i, j), cross=(win != 'left'))]
            cap = f"({i},{j}): min({a} above, {l} left) + {grid[i][j]} = {t[i][j]}."
            if first_cell:
                sub = (f"dp[{j}] still held {a}, the square above; dp[{j - 1}] was just written, {l}, the square "
                       "to the left. Keep the cheaper way in.")
                hold = KEY
                first_cell = False
            else:
                hold = QUICK * 2.6
        else:
            path = e['path']
            for p in path:
                styles[p] = 'window'
            styles[(m - 1, n - 1)] = 'good'
            rings = [((m - 1, n - 1), style('good')[1])]
            cost_rings = [(p, style('window')[1]) for p in path]
            route = ' + '.join(str(grid[r][c]) for r, c in reversed(path))
            cap = f"Answer: dp[{n - 1}] = {e['ans']}. Cheapest route: {route}."
            sub = notes.get('done', "One pass, O(m × n) time, one row of memory, O(n).")
            hold = END
        key = (e.get('i'), e.get('j')) if k != 'done' else None
        if key in notes:
            sub, hold = notes[key], KEY
        table = DPTableView(vals, row_labels=[f'r{i}' for i in range(m)], col_labels=[f'c{j}' for j in range(n)],
                            styles=styles, rings=rings, links=links, max_cell=60, gap=16)
        dpv = ArrayView(e['dp'], styles=dp_styles, pointers=ptr, title='dp', cell=46)
        costs = Stack([TextView(['cost of each square'], size=15), TableView(grid, styles={}, rings=cost_rings)])
        sc.frame([table, dpv], cap, sub, hold, side=costs, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = [([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7), ([[1, 2, 3], [4, 5, 6]], 12)]
    assert all(loop_from_zero(g) == want for g, want in samples)       # the wrap-around passes both samples
    assert greedy(samples[0][0]) == 9                                     # greedy already fails sample 1
    assert Solution().minPathSum(HARD_GREEDY) == 12 and greedy(HARD_GREEDY) == 15
    assert Solution().minPathSum(HARD_WRAP) == 14 and loop_from_zero(HARD_WRAP) == 8
    g = build(HARD_GREEDY, 'The cheap top row leads into an expensive right column. Answer 12.', NOTES_GREEDY)
    w = build(HARD_WRAP, 'Cheap right column at the top, cheap left column at the bottom. Answer 14.', NOTES_WRAP)
    return [
        (g, "Choosing the cheaper next square runs along the 1s on top and is then forced through a 9: 15. "
            "The table finds 12, down the left side and along the bottom."),
        (w, "An inner loop from j = 0 passes both samples in Python, because dp[-1] quietly reads the last column. "
            "Here the left column borrows the right column's 4 and the answer comes out 8 instead of 14."),
    ]


def main():
    args = cli()
    sc = build(GRID, 'Move right or down; pay every square you stand on. Box = cheapest total to reach it.')
    finish(sc, 64, "Watch (1,1): it compares 4 from above with 2 from the left, keeps the 2, and that habit of "
                   "keeping only the cheapest way in builds the corner's 7.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
