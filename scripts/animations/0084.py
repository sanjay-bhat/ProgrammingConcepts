#!/usr/bin/env python3
"""#84 Largest Rectangle in Histogram: a rising stack; each pop measures one bar as the shortest.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

HEIGHTS = [2, 1, 5, 6, 2, 3]              # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_LEFT = [6, 2, 5, 4, 5, 1, 6]         # 12; measuring width from the popped bar's own index gives 8
HARD_FLUSH = [1, 2, 3, 4, 5]              # 9; no sentinel 0 at the end gives 0 (nothing ever pops)


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        heights = heights + [0]
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area


def own_index_width(heights):
    """First attempt: width = i - popped, measured from the popped bar's own position."""
    stack, best, heights = [], 0, heights + [0]
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] >= h:
            p = stack.pop()
            best = max(best, heights[p] * (i - p))
        stack.append(i)
    return best


def no_flush(heights):
    """First attempt: no sentinel 0 at the end, so bars still on the stack are never measured."""
    stack, best = [], 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)
    return best


def trace(heights_in):
    events = []
    st = {'best': 0, 'best_rect': None}

    def rec(kind, **kw):
        events.append(dict(kind=kind, stack=list(stack), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    stack = []
    max_area = 0
    heights = heights_in + [0]
    rec('start', heights=heights)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] >= h:
            p = stack[-1]                                       # display only
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            grew = height * width > max_area                    # display only
            max_area = max(max_area, height * width)
            lo = i - width                                      # display only: the rectangle's left edge
            if grew:
                st.update(best=max_area, best_rect=(lo, i - 1, height))
            rec('pop', heights=heights, i=i, p=p, height=height, width=width, lo=lo, grew=grew, empty=not stack)
        stack.append(i)
        rec('push', heights=heights, i=i)
    rec('done', heights=heights)
    assert max_area == Solution().largestRectangleArea(list(heights_in))
    return events


def skyline(e, n):
    """One column per bar (plus the sentinel), one row per unit of height, then heights and indices."""
    hs = e['heights']
    top = max(hs)
    k = e['kind']
    rect = None
    if k == 'pop':
        rect = (e['lo'], e['i'] - 1, e['height'])
    elif k == 'done' and e['best_rect']:
        rect = e['best_rect']
    on_stack = set(e['stack'])
    rows = []
    for r in range(top):
        y = top - r
        row = []
        for c, v in enumerate(hs):
            if rect and rect[0] <= c <= rect[1] and y <= rect[2]:
                row.append({'style': 'good'})
            elif v >= y:
                cur = e.get('i')
                if c in on_stack:
                    st = 'window'
                elif cur is not None and c == cur and k != 'done':
                    st = 'active'           # the bar doing the popping
                elif k == 'start' or (cur is not None and c > cur):
                    st = 'plain'            # not reached yet
                else:
                    st = 'land'             # already popped and measured
                row.append({'style': st})
            else:
                row.append({'style': 'muted'})
        rows.append(row)
    cur = e.get('i')
    popped = e.get('p') if k == 'pop' else None
    rows.append([{'style': 'gold' if c == popped else ('active' if c == cur and k != 'done' else ('muted' if c == n else 'plain')),
                  'label': v} for c, v in enumerate(hs)])
    rows.append([{'style': 'muted', 'label': (c if c < n else 'end')} for c in range(len(hs))])
    return rows


def build(heights, subtitle, notes=None):
    notes = notes or {}
    n = len(heights)
    sc = Scene('#84 Largest Rectangle in Histogram: monotonic stack', subtitle)
    legend = [(style('window')[1], 'on the stack'), (style('land')[1], 'already measured'),
              (style('gold')[1], 'bar being popped'), (style('good')[1], 'its rectangle'), (ACTIVE, 'current bar i')]
    rows_n = max(heights) + 2
    cell = max(18, min(40, (366 - 4 * (rows_n - 1)) // rows_n))
    seen = set()
    for e in trace(list(heights)):
        k, hs = e['kind'], e['heights']
        if k == 'start':
            cap, sub, hold = ("Walk left to right, keeping a stack of bars whose heights rise from bottom to top.",
                              notes.get('start', "A 0 is added at the end (the 'end' column): it's lower than everything, so it flushes the stack."), KEY)
        elif k == 'push':
            i = e['i']
            if i == n:
                cap, sub, hold = ("The end 0 is pushed. Every real bar has been measured.", "", QUICK * 2)
            else:
                cap = f"Push bar {i} (height {hs[i]}). The stack still rises from bottom to top."
                sub, hold = "", QUICK * 2
        elif k == 'pop':
            i, p, hgt, w, lo = e['i'], e['p'], e['height'], e['width'], e['lo']
            why = (f"bar {i} ({hs[i]}) is no taller than bar {p} ({hgt}), so bar {p}'s rectangle can't reach past {i - 1}."
                   if i < n else f"the end 0 is lower than bar {p} ({hgt}), so it gets measured now.")
            cap = f"Pop bar {p}: {why}"
            if e['empty']:
                left = f"The stack is now empty, so bar {p} was the lowest so far and stretches back to index 0: width {w}."
            else:
                left = f"Left edge: one past the new top (bar {e['stack'][-1]}), so width = {i} - {e['stack'][-1]} - 1 = {w}."
            area = f"{hgt} × {w} = {hgt * w}" + (", a new best." if e['grew'] else ".")
            sub = left + ' ' + area
            key = ('pop', p)
            if key in notes:
                sub = notes[key] + ' ' + area
            first = 'pop' not in seen
            seen.add('pop')
            reach = w > i - p                      # stretches left over bars popped earlier
            hold = KEY if first or e['grew'] or key in notes or (reach and 'reach' not in seen) else STEP
            if reach:
                seen.add('reach')
        else:
            lo, hi, hgt = e['best_rect']
            cap = f"Done. The largest rectangle is {e['best']}: height {hgt} over bars {lo} to {hi}."
            sub, hold = notes.get('done', "Each bar is pushed once and popped once: O(n) time, O(n) for the stack."), END
        stack = [(f'bar {j}  (h = {hs[j]})' if j < n else 'end  (h = 0)') for j in e['stack']]
        sc.frame(GridView(skyline(e, n), bridges=False, indices=False, cell=cell), cap, sub, hold,
                 side=StackView(stack, 'Stack', note='heights rise upward', empty='(empty)'),
                 counters={'best': e['best']}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert Solution().largestRectangleArea(HARD_LEFT) == 12 and own_index_width(HARD_LEFT) == 8
    assert Solution().largestRectangleArea(HARD_FLUSH) == 9 and no_flush(HARD_FLUSH) == 0
    left = build(HARD_LEFT, f'heights = {HARD_LEFT}. Answer 12. Measuring width from the popped bar\'s own index gives 8.', {
        'start': "Watch bar 3 (height 4): its rectangle reaches LEFT over bar 2, which was popped before it.",
        ('pop', 3): "The new top is bar 1, so bar 3's rectangle starts at index 2, over the 5 popped earlier: width 5 - 1 - 1 = 3. From bar 3's own index it'd be 2.",
        'done': "Answer 12, bars 2 to 4 at height 4. Width from the popped index (i - p) gives 8, because it can't see the 5 that was popped earlier.",
    })
    flush = build(HARD_FLUSH, f'heights = {HARD_FLUSH}. Answer 9. Without the 0 at the end, nothing is ever popped and the answer is 0.', {
        'start': "A staircase: every bar is taller than the last, so no real bar ever pops another. Only the end 0 measures anything.",
        'done': "Answer 9: height 3 over bars 2 to 4. Every one of these rectangles was measured by the end 0; without it the answer is 0.",
    })
    return [
        (left, "[6,2,5,4,5,1,6]: the 4 at index 3 stretches left over a 5 that was popped earlier. A first attempt that measures "
               "width from the popped bar's own index misses that and answers 8. The answer is 12."),
        (flush, "[1,2,3,4,5]: heights only rise, so nothing pops until the extra 0 at the end. A first attempt without that "
                "0 never measures a single rectangle and answers 0. The answer is 9."),
    ]


def main():
    args = cli()
    sc = build(HEIGHTS, f'heights = {HEIGHTS}. Find the largest rectangle that fits under the bars.')
    finish(sc, 84, "Watch bar 4 (height 2) arrive: it pops the 6 and then the 5, and the 5's rectangle "
                   "spans both tall bars for area 10.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
