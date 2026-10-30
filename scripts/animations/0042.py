#!/usr/bin/env python3
"""#42 Trapping Rain Water: fill from the side standing on the lower bar.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

HEIGHT = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]          # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_PEAK = [5, 2, 1, 3, 1, 2, 6]     # 16; filling between neighbouring peaks gives 6 (the 3 is under water)
HARD_STAIRS = [5, 0, 4, 0, 3, 0, 2]   # 9; filling only pools closed by a taller wall on the right gives 0


def trace(height):
    events, filled = [], [0] * len(height)
    st = {'left': None, 'right': None, 'left_max': 0, 'right_max': 0, 'water': 0}

    def rec(kind, **kw):
        events.append(dict(kind=kind, filled=list(filled), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    st.update(left=left, right=right)
    rec('start')
    while left < right:
        if height[left] <= height[right]:
            new_max = height[left] > left_max                         # display only
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            filled[left] = left_max - height[left]
            st.update(left_max=left_max, water=water)
            rec('left', i=left, added=left_max - height[left], new_max=new_max)
            left += 1
        else:
            new_max = height[right] > right_max                       # display only
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            filled[right] = right_max - height[right]
            st.update(right_max=right_max, water=water)
            rec('right', i=right, added=right_max - height[right], new_max=new_max)
            right -= 1
        st.update(left=left, right=right)
    rec('done')
    assert water == Solution().trap(height) == sum(filled)
    return events


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        return water


def between_peaks(height):
    """First attempt: find the peaks (bars at least as tall as both neighbours)
    and fill between each neighbouring pair up to the shorter of the two."""
    n = len(height)
    peaks = [i for i in range(n)
             if (i == 0 or height[i] >= height[i - 1]) and (i == n - 1 or height[i] >= height[i + 1])]
    water = 0
    for a, b in zip(peaks, peaks[1:]):
        level = min(height[a], height[b])
        water += sum(max(0, level - height[i]) for i in range(a + 1, b))
    return water


def close_on_taller(height):
    """First attempt: scan left to right and add a pool only once a bar at least
    as tall as the wall that opened it comes along."""
    water, wall, pool = 0, 0, 0
    for i in range(1, len(height)):
        if height[i] >= height[wall]:
            water, pool, wall = water + pool, 0, i
        else:
            pool += height[wall] - height[i]
    return water


def words(e, h, notes, first):
    k, L, R = e['kind'], e['left'], e['right']
    if k == 'start':
        return ("One pointer at each end. Each step fills the side standing on the LOWER bar.",
                "The other side is guaranteed a wall at least that tall, so only this side's max matters.", KEY)
    if k in ('left', 'right'):
        i, a = e['i'], e['added']
        side, mx = (k, e['left_max'] if k == 'left' else e['right_max'])
        other = R if k == 'left' else L
        cmp = f"{h[i]} ≤ {h[other]}" if k == 'left' else f"{h[other]} > {h[i]}"
        head = f"{cmp}: fill on the {side}. "
        if (k, i) in notes:
            return (head + f"Bar {i}: {side}_max {mx}, water {mx} - {h[i]} = {a}.", notes[(k, i)], KEY)
        if e['new_max'] and first.get('new_max') == id(e):
            return (head + f"Bar {i} ({h[i]}) is a new {side}_max, so it holds 0.",
                    "Update the max BEFORE subtracting; the other order would add a negative amount.", KEY)
        if a and first.get('water') == id(e):
            return (head + f"Bar {i}: water rises to {side}_max {mx}, so {mx} - {h[i]} = {a}.",
                    f"The {'right' if k == 'left' else 'left'} side has a wall at least {h[other]}, "
                    f"so {mx} is the level here.", KEY)
        if first.get('flip') == id(e):
            return (head + f"Bar {i}: {side}_max {mx}, water {a}.",
                    f"Now the right bar is the lower one, so the right pointer moves instead.", KEY)
        if a:
            return (head + f"Bar {i}: {mx} - {h[i]} = {a} more.", "", STEP)
        return (head + f"Bar {i} ({h[i]}) holds nothing: it's the {side}_max itself.", "", STEP)
    return (f"The pointers meet. Total water: {e['water']}.",
            notes.get('done', "One pass and a handful of numbers: O(n) time, O(1) space."), END)


def skyline(h, e):
    """Bars as a grid: one column per bar, one row per unit of height, then a row
    of heights and a row of indices. Settled water sits on top of the bars."""
    top = max(h)
    k, L, R = e['kind'], e['left'], e['right']
    cur = e.get('i')
    rows = []
    for r in range(top):
        y = top - r
        row = []
        for c, v in enumerate(h):
            if v >= y:
                row.append({'style': 'active' if c == cur else 'land'})
            elif y <= v + e['filled'][c]:
                row.append({'style': 'good' if c == cur else 'window'})
            else:
                row.append({'style': 'muted'})
        rows.append(row)
    rows.append([{'style': 'active' if c == cur else 'plain', 'label': v} for c, v in enumerate(h)])
    rows.append([{'style': 'gold' if c in (L, R) and k != 'done' else 'muted', 'label': c}
                 for c in range(len(h))])
    return rows


def build(h, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#42 Trapping Rain Water: two pointers', subtitle)
    legend = [(ACTIVE, 'bar being filled'), (style('good')[1], 'water just added'),
              (style('window')[1], 'water so far'), (style('gold')[1], 'left / right pointers')]
    events = trace(h)
    first = {}
    for e in events:
        if e['kind'] in ('left', 'right'):
            if e['added'] and 'water' not in first:
                first['water'] = id(e)
            if e['new_max'] and e['i'] > 0 and e['i'] < len(h) - 1 and 'new_max' not in first \
                    and any(x['kind'] == e['kind'] and x['added'] for x in events[:events.index(e)]):
                first['new_max'] = id(e)
            if e['kind'] == 'right' and 'flip' not in first and any(x['kind'] == 'left' for x in events):
                first['flip'] = id(e)
    rows_n = max(h) + 2
    cell = min(40, (366 - 4 * (rows_n - 1)) // rows_n, (500 - 5 * (len(h) - 1)) // len(h))
    for e in events:
        grid = GridView(skyline(h, e), bridges=False, indices=False, cell=cell)
        rows = [('left', f"{e['left']}", 'gold'), ('left_max', f"{e['left_max']}", None),
                ('right', f"{e['right']}", 'gold'), ('right_max', f"{e['right_max']}", None)]
        if e['kind'] in ('left', 'right'):
            mx = e['left_max'] if e['kind'] == 'left' else e['right_max']
            rows.append((f"bar {e['i']}", f"{mx} - {h[e['i']]} = {e['added']}", 'good' if e['added'] else 'active'))
        rows.append(('water', f"{e['water']}", 'good' if e['kind'] == 'done' else None))
        cap, sub, hold = words(e, h, notes, first)
        sc.frame(grid, cap, sub, hold,
                 side=MapView(rows, 'Pointers and maxes', headers=('name', 'value')),
                 counters={'water': e['water']}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert Solution().trap(HARD_PEAK) == 16 and between_peaks(HARD_PEAK) == 6
    assert Solution().trap(HARD_STAIRS) == 9 and close_on_taller(HARD_STAIRS) == 0
    peak = build(HARD_PEAK, f'height = {HARD_PEAK}. Answer 16. Filling between neighbouring peaks gives 6.', {
        ('left', 3): "The 3 looks like a peak, but it's under water: left_max is 5 and the right end is 6.",
        'done': "Every bar filled to 5, the shorter end wall. Splitting the basin at the 3 would cap it at 3.",
    })
    stairs = build(HARD_STAIRS, f'height = {HARD_STAIRS}. Answer 9. Waiting for a taller wall on the right gives 0.', {
        ('right', 5): "No wall to its right reaches 5, yet water sits here: the 2 at the end holds 2 squares in.",
        'done': "All the filling happened from the right. A left-to-right scan waiting for a wall as tall as 5 finds none.",
    })
    return [
        (peak, "[5,2,1,3,1,2,6]: the 3 in the middle looks like a peak but sits under water. A first attempt that "
               "fills between neighbouring peaks stops at 3 and gets 6; the answer is 16."),
        (stairs, "[5,0,4,0,3,0,2] steps down to the right. A first attempt that only counts a pool once a wall as tall "
                 "as 5 closes it gets 0; filling from the lower side gives 9."),
    ]


def main():
    args = cli()
    sc = build(HEIGHT, f'height = {HEIGHT}. How much rain is trapped between the bars?')
    finish(sc, 42, "Watch the first square of water at index 2: left_max is 1, and the right end is at least "
                   "as tall, so the water there is exactly 1 - 0, without knowing the true right maximum.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
