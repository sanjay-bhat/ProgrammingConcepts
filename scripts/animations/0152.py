#!/usr/bin/env python3
"""#152 Maximum Product Subarray: carry the biggest AND the smallest product
ending here, because a negative number turns one into the other.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The input is LeetCode's example 1,
[2,3,-2,4], with a -1 on the end so the stored minimum gets its payoff.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUMS = [2, 3, -2, 4, -1]   # LeetCode example 1 plus a trailing -1


def trace(nums):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def maxProduct(self, nums) -> int:
            max_p = min_p = result = nums[0]
            rec('init', i=0, mx=max_p, mn=min_p, res=result)
            for i, n in enumerate(nums[1:], 1):
                old_mx, old_mn = max_p, min_p
                if n < 0:
                    max_p, min_p = min_p, max_p
                    rec('swap', i=i, n=n, mx=max_p, mn=min_p, res=result)
                max_p = max(n, max_p * n)
                min_p = min(n, min_p * n)
                result = max(result, max_p)
                rec('update', i=i, n=n, mx=max_p, mn=min_p, res=result,
                    old_mx=old_mx, old_mn=old_mn)
            rec('done', res=result)
            return result

    Solution().maxProduct(nums)
    return events


def src(e, val):
    """Which earlier value produced `val`: 'alone', 'max' or 'min'."""
    n = e['n']
    if val == e['old_mx'] * n and val != n:
        return 'max'
    if val == e['old_mn'] * n and val != n:
        return 'min'
    return 'alone'


def words(e):
    k = e['kind']
    if k == 'init':
        return ("Start at 2: the biggest and the smallest product ending here are both just 2.",
                "Top row: biggest product of a run ending at this box. Bottom row: smallest.", KEY)
    if k == 'swap':
        return (f"{e['n']} is negative, so swap the two before multiplying.",
                "Times a negative, the biggest becomes the smallest and the smallest becomes the biggest.", KEY)
    if k == 'done':
        return (f"maxProduct returns {e['res']}: the whole array, 2 × 3 × -2 × 4 × -1.",
                "The -48 we kept in the bottom row is what made 48 possible.", END)
    n, mx, mn = e['n'], e['mx'], e['mn']
    sm, sn = src(e, mx), src(e, mn)
    name = {'alone': f'{n} alone', 'max': f"{e['old_mx']} × {n}", 'min': f"{e['old_mn']} × {n}"}
    i = e['i']
    if i == 4:
        return (f"Biggest = {name[sm]} = {mx}. The smallest, -48, flipped into the biggest.",
                f"Best jumps to {e['res']}. Tracking only the biggest would have thrown -48 away.", KEY)
    if i == 2:
        return (f"Biggest = {name[sm]} = {mx}; smallest = {name[sn]} = {mn}.",
                "Starting fresh at -2 beats -6. The -12 looks useless, but we keep it.", KEY)
    if i == 3:
        return (f"Biggest = {name[sm]} = {mx}; smallest = {name[sn]} = {mn}.",
                "The smallest keeps growing in size. One more negative would make it huge.", STEP)
    return (f"Biggest = {name[sm]} = {mx}; smallest = {name[sn]} = {mn}. Best = {e['res']}.",
            "Each box is the number alone, or it times one of the two boxes on its left.", STEP)


def main():
    args = cli()
    n = len(NUMS)
    sc = Scene('#152 Max Product Subarray: keep the biggest AND the smallest',
               'Columns are positions. Each box only looks at the column to its left.')
    legend = [(ACTIVE, 'just computed'), (style('good')[1], 'filled'), (style('window')[1], 'swapped')]
    MX, NU, MN = 0, 1, 2
    hi, lo = [None] * n, [None] * n
    for e in trace(NUMS):
        k = e['kind']
        styles, links, rings = {}, [], []
        if 'i' in e:
            i = e['i']
            hi[i], lo[i] = e['mx'], e['mn']
        for c in range(n):
            if hi[c] is not None:
                styles[(MX, c)] = styles[(MN, c)] = 'good'
        if k == 'init':
            rings = [((MX, 0), ACTIVE), ((MN, 0), ACTIVE)]
        if k == 'swap':
            i = e['i']
            hi[i] = lo[i] = None
            styles.pop((MX, i), None); styles.pop((MN, i), None)
            styles[(MX, i - 1)] = styles[(MN, i - 1)] = 'window'
            styles[(NU, i)] = 'active'
            rings = [((MX, i - 1), style('window')[1]), ((MN, i - 1), style('window')[1])]
        if k == 'update':
            i = e['i']
            styles[(NU, i)] = 'active'
            rings = [((MX, i), ACTIVE), ((MN, i), ACTIVE)]
            for row, val in ((MX, e['mx']), (MN, e['mn'])):
                s = src(e, val)
                if s == 'alone':
                    links.append(dict(src=(NU, i), dst=(row, i)))
                else:
                    r0 = MX if s == 'max' else MN
                    links.append(dict(src=(r0, i - 1), dst=(row, i)))
        if k == 'done':
            rings = [((MX, n - 1), style('good')[1])]
        vals = [[('' if v is None else v) for v in hi], NUMS,
                [('' if v is None else v) for v in lo]]
        # the swap frame shows the swapped pair in the previous column
        if k == 'swap':
            i = e['i']
            vals[MX][i - 1], vals[MN][i - 1] = e['mx'], e['mn']
        table = DPTableView(vals, row_labels=['biggest', 'nums', 'smallest'],
                            col_labels=[f'i={c}' for c in range(n)],
                            styles=styles, rings=rings, links=links, max_cell=84)
        rows = []
        if k != 'done':
            rows = [('max_p', str(e['mx'])), ('min_p', str(e['mn'])), ('result', str(e['res']), 'good')]
            if k == 'swap':
                rows = [('max_p', f"{e['mx']}  (was min)", 'window'), ('min_p', f"{e['mn']}  (was max)", 'window'),
                        ('result', str(e['res']), 'good')]
        else:
            rows = [('result', str(e['res']), 'good')]
        cap, sub, hold = words(e)
        sc.frame([table], cap, sub, hold, side=MapView(rows, 'Variables', headers=('name', 'value')),
                 counters={'best': e['res']}, legend=legend)
    finish(sc, 152, "Watch the -48 in the bottom row: it looks like the worst product so far, "
                    "and one more negative turns it into the answer, 48.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
