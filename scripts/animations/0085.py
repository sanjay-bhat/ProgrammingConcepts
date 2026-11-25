#!/usr/bin/env python3
"""#85 Maximal Rectangle: each row turns the grid into a histogram, solved with #84's stack.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

MATRIX = ["10100", "10111", "11111", "10010"]          # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_RESET = ["01111", "11011", "11110", "10111"]      # 4; counting 1s per column without resetting on a 0 gives 15
HARD_LEFT = ["11011", "11111", "11111", "11111"]       # 15; measuring width from the popped bar's own index gives 9


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        for row in matrix:
            for c in range(n):
                heights[c] = heights[c] + 1 if row[c] == '1' else 0
            max_area = max(max_area, self._largest_in_histogram(heights))
        return max_area

    def _largest_in_histogram(self, h: list[int]) -> int:
        stack: list[int] = []
        max_a = 0
        for i in range(len(h) + 1):
            cur = h[i] if i < len(h) else 0
            while stack and h[stack[-1]] > cur:
                height = h[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_a = max(max_a, height * width)
            stack.append(i)
        return max_a


def _hist(h, own=False):
    stack, best = [], 0
    for i in range(len(h) + 1):
        cur = h[i] if i < len(h) else 0
        while stack and h[stack[-1]] > cur:
            p = stack.pop()
            width = (i - p) if own else (i if not stack else i - stack[-1] - 1)
            best = max(best, h[p] * width)
        stack.append(i)
    return best


def no_reset(matrix):
    """First attempt: a column's height counts its 1s so far, without dropping to 0 on a '0'."""
    n, h, best = len(matrix[0]), [0] * len(matrix[0]), 0
    for row in matrix:
        for c in range(n):
            h[c] += row[c] == '1'
        best = max(best, _hist(h))
    return best


def own_index_width(matrix):
    """First attempt: the histogram step measures width as i - popped (the popped bar's own index)."""
    n, h, best = len(matrix[0]), [0] * len(matrix[0]), 0
    for row in matrix:
        for c in range(n):
            h[c] = h[c] + 1 if row[c] == '1' else 0
        best = max(best, _hist(h, own=True))
    return best


def trace(matrix):
    events = []
    st = {'r': None, 'best': 0, 'best_rect': None, 'stack': []}
    counts = [0] * len(matrix[0])                       # display only: what no_reset would hold

    def rec(kind, **kw):
        events.append(dict(kind=kind, heights=list(heights), counts=list(counts),
                           **{k: (list(v) if isinstance(v, list) else v) for k, v in st.items()}, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def largest_in_histogram(h):
        stack: list[int] = []
        st['stack'] = stack
        max_a = 0
        for i in range(len(h) + 1):
            cur = h[i] if i < len(h) else 0
            while stack and h[stack[-1]] > cur:
                p = stack[-1]                                       # display only
                height = h[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_a = max(max_a, height * width)
                if height * width > st['best']:                     # display only
                    st.update(best=height * width, best_rect=(st['r'] - height + 1, st['r'], i - width, i - 1))
                    grew = True
                else:
                    grew = False
                rec('pop', i=i, p=p, height=height, width=width, grew=grew, empty=not stack)
            stack.append(i)
            if i < len(h):
                rec('push', i=i)
        st['stack'] = []
        return max_a

    n = len(matrix[0])
    heights = [0] * n
    max_area = 0
    rec('start')
    for r, row in enumerate(matrix):
        st['r'] = r
        for c in range(n):
            counts[c] += row[c] == '1'
        resets = [c for c in range(n) if row[c] != '1' and heights[c] > 0]      # display only
        for c in range(n):
            heights[c] = heights[c] + 1 if row[c] == '1' else 0
        rec('row', resets=resets)
        max_area = max(max_area, largest_in_histogram(heights))
        rec('row_done', row_best=max_area)
    st['r'] = None
    rec('done')
    assert max_area == Solution().maximalRectangle([list(x) for x in matrix])
    return events


def grid_cells(matrix, e):
    r = e['r']
    k = e['kind']
    rect = None
    if k == 'pop':
        rect = (r - e['height'] + 1, r, e['i'] - e['width'], e['i'] - 1)
    elif k == 'done':
        rect = e['best_rect']
    h = e['heights']
    rows = []
    for rr, line in enumerate(matrix):
        row = []
        for c, v in enumerate(line):
            in_bar = r is not None and r - h[c] < rr <= r
            if rect and rect[0] <= rr <= rect[1] and rect[2] <= c <= rect[3]:
                row.append({'style': 'good', 'label': '1'})
            elif v == '0':
                row.append({'water': True})
            elif in_bar and k != 'done':
                row.append({'style': 'window', 'label': '1'})
            else:
                row.append({'style': 'land' if r is None or rr <= r else 'plain', 'label': '1'})
        rows.append(row)
    return rows


def build(matrix, subtitle, notes=None, trap=None):
    notes = notes or {}
    n = len(matrix[0])
    sc = Scene('#85 Maximal Rectangle: a histogram per row', subtitle)
    legend = [(style('window')[1], "this row's bars"), (style('good')[1], 'rectangle being measured'),
              (style('gold')[1], 'bar being popped'), (ACTIVE, 'current row')]
    seen = set()
    m = len(matrix)
    cell = min(52, (250 - 24) // m - 7)      # leave room under the grid for the heights row
    for e in trace(matrix):
        k, r, h = e['kind'], e['r'], e['heights']
        rings = [((r, c), ACTIVE, 3) for c in range(n)] if r is not None and k != 'done' else []
        grid = GridView(grid_cells(matrix, e), outlines=rings, bridges=False, cell=cell)
        hstyles = {}
        if k == 'pop':
            hstyles = {c: 'good' for c in range(e['i'] - e['width'], e['i'])}
            hstyles[e['p']] = 'gold'
        if k == 'row':
            hstyles = {c: 'bad' for c in e['resets']}
        ptr = {'i': e['i']} if k in ('pop', 'push') and e['i'] < n else {}
        harr = ArrayView(h if k != 'start' else [0] * n, hstyles, pointers=ptr, title='heights', cell=cell - 8)
        views = [grid, harr]
        if k == 'start':
            cap, sub, hold = ("Go row by row. Each column's height = how many 1s stand in an unbroken run up to this row.",
                              notes.get('start', "Every row then looks like #84's bar chart, and #84's stack finds its biggest rectangle."), KEY)
        elif k == 'row':
            first = 'row' not in seen
            seen.add('row')
            cap = f"Row {r}: heights become {h}."
            if e['resets']:
                cs = ', '.join(map(str, e['resets']))
                sub = (f"Column{'s' if len(e['resets']) > 1 else ''} {cs} hit{'' if len(e['resets']) > 1 else 's'} a 0, "
                       "so the height drops to 0: a rectangle can't stand on a gap.")
                if trap == 'reset' and e['counts'] != h:
                    sub = (f"Reset to 0 on a 0. Just counting 1s per column would give {e['counts']} here: "
                           "bars standing on gaps.")
                hold = KEY if first or 'reset' not in seen or trap == 'reset' else STEP
                seen.add('reset')
            else:
                sub = ("A 1 adds one to the bar above it." if first else ""), 
                sub = sub[0]
                hold = KEY if first else STEP
        elif k == 'push':
            cap, sub, hold = (f"Push column {e['i']} (height {h[e['i']]}) onto the stack.", "", QUICK)
        elif k == 'pop':
            i, p, hg, w = e['i'], e['p'], e['height'], e['width']
            who = f"column {i} (height {h[i]})" if i < n else "the end (height 0)"
            cap = f"Pop column {p}: {who} is lower, so a height-{hg} rectangle ends at column {i - 1}."
            left = "stack empty, so it reaches column 0" if e['empty'] else f"left edge after column {e['stack'][-1]}"
            sub = f"Width {w} ({left}): {hg} × {w} = {hg * w}" + (", the best so far." if e['grew'] else ".")
            hold = KEY if e['grew'] else STEP
            if trap == 'left' and w != i - p:
                sub = (f"Width {w}: it stretches left over columns popped earlier. From column {p}'s own index it'd be "
                       f"{i - p}, area {hg * (i - p)}. {hg} × {w} = {hg * w}.")
                hold = KEY
        elif k == 'row_done':
            cap, sub, hold = (f"Row {r} is done. Best so far: {e['best']}.", "", QUICK * 2)
        else:
            r0, r1, c0, c1 = e['best_rect']
            rows_txt = f"row {r0}" if r0 == r1 else f"rows {r0}-{r1}"
            cap = f"Done. The largest rectangle of 1s has area {e['best']}: {rows_txt}, columns {c0}-{c1}."
            sub, hold = notes.get('done', "Each row costs O(n) to update and O(n) for the stack: O(m × n) in all."), END
        stack = [f'col {j}  (h = {h[j]})' for j in e['stack'] if j < n]
        sc.frame(views, cap, sub, hold,
                 side=StackView(stack, 'Stack', note='heights rise upward', empty='(empty)'),
                 counters={'best': e['best']}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    s = lambda m: Solution().maximalRectangle([list(x) for x in m])
    assert s(HARD_RESET) == 4 and no_reset(HARD_RESET) == 15
    assert s(HARD_LEFT) == 15 and own_index_width(HARD_LEFT) == 9
    reset = build(HARD_RESET, 'Answer 4. Counting 1s per column without resetting on a 0 gives 15.', {
        'start': "Every column has a 0 somewhere. Watch the heights drop back to 0 each time.",
        'done': "Answer 4. Without the reset, the last row's heights would be [3, 3, 3, 4, 3], bars standing on gaps, and the answer 15.",
    }, trap='reset')
    left = build(HARD_LEFT, 'Answer 15. Measuring width from the popped column\'s own index gives 9.', {
        'start': "Column 2 is one shorter than the rest. Its rectangle must stretch over the taller columns on BOTH sides.",
        'done': "Answer 15: height 3 across all five columns. Measured from column 2's own index, the width is 3, for 9.",
    }, trap='left')
    return [
        (reset, "Every column has a gap. A first attempt that adds up each column's 1s instead of resetting to 0 on a '0' "
                "builds bars that stand on gaps, and answers 15. The answer is 4."),
        (left, "The last row's heights are [4,4,3,4,4]. The 3 spans all five columns, but a first attempt that measures "
               "width from the popped column's own index can't see the 4s it popped earlier, and answers 9. The answer is 15."),
    ]


def main():
    args = cli()
    sc = build(MATRIX, "LeetCode example 1. Find the largest rectangle containing only 1s.")
    finish(sc, 85, "Watch row 2: its heights are [3,1,3,2,2], and the stack finds the 2-tall rectangle "
                   "across columns 2 to 4, area 6.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
