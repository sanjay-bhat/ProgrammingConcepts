#!/usr/bin/env python3
"""#43 Multiply Strings: digit i times digit j always lands in column i + j + 1,
with its carry in column i + j, so one array of m + n cells replaces the rows
of long multiplication.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

NUM1, NUM2 = "123", "456"          # LeetCode example 2: "56088"

# The hard example (interactive page only): 999 x 999 = 998001 needs all
# m + n = 6 cells. Sizing the answer as m + n - 1 cells and dropping the final
# carry passes both LeetCode samples (2 x 3 = 6 and 123 x 456 = 56088 both
# have m + n - 1 digits) and answers "98001" here.
HARD1, HARD2 = "999", "999"
HARD_NOTES = {
    (0, 0): "The carry 9 goes into cell 0. With only m + n - 1 cells there's nowhere to put it, and the answer loses its 9.",
    'done': "All 6 cells hold a digit. An m + n - 1 array answers 98001, yet passes both LeetCode samples.",
}


def short_array(num1, num2):
    """The first attempt the hard example breaks: m + n - 1 cells, top carry dropped."""
    m, n = len(num1), len(num2)
    pos = [0] * (m + n - 1)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            total = int(num1[i]) * int(num2[j]) + pos[i + j]
            pos[i + j] = total % 10
            if i + j > 0:
                pos[i + j - 1] += total // 10
    return ''.join(map(str, pos)).lstrip('0') or '0'


def trace(num1, num2):
    events = []

    def rec(kind, pos, **kw):
        events.append(dict(kind=kind, pos=pos[:] if pos else None, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    class Solution:
        def multiply(self, num1, num2):
            if num1 == '0' or num2 == '0':
                return '0'
            m, n = len(num1), len(num2)
            pos = [0] * (m + n)
            rec('start', pos)
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    mul = int(num1[i]) * int(num2[j])
                    p1, p2 = i + j, i + j + 1
                    had, had1 = pos[p2], pos[p1]
                    total = mul + pos[p2]
                    pos[p2] = total % 10
                    pos[p1] += total // 10
                    rec('step', pos, i=i, j=j, mul=mul, p1=p1, p2=p2, had=had, had1=had1, total=total)
            result = ''.join(str(d) for d in pos).lstrip('0')
            rec('done', pos, ans=result or '0')
            return result or '0'

    ans = Solution().multiply(num1, num2)
    return events, ans


def words(e, num1, num2, firsts, notes):
    k = e['kind']
    key = 'done' if k == 'done' else (e.get('i'), e.get('j'))
    cap, sub, hold = _words(e, num1, num2, firsts)
    if notes and key in notes:
        return cap, notes[key], (END if k == 'done' else KEY)
    return cap, sub, hold


def _words(e, num1, num2, firsts):
    k = e['kind']
    m, n = len(num1), len(num2)
    if k == 'start':
        return (f"{m}-digit times {n}-digit: the answer has at most {m + n} digits, so make {m + n} cells of 0.",
                "Then multiply digit pairs from the right, adding each straight into its column.", KEY)
    if k == 'done':
        return (f'Join the cells and strip leading zeros: "{e["ans"]}".',
                f"{m} × {n} = {m * n} digit multiplications, one array: no rows, no string adding.", END)
    i, j, mul, p1, p2, t = e['i'], e['j'], e['mul'], e['p1'], e['p2'], e['total']
    cap = (f"{num1[i]} × {num2[j]} = {mul}, plus the {e['had']} in cell {p2} = {t}. "
           f"Keep {t % 10} in cell {p2}, carry {t // 10} to cell {p1}.")
    if firsts.get('first') == (i, j):
        return cap, f"Digit {i} times digit {j} always lands in column {i} + {j} + 1 = {p2}: no shifting rows needed.", KEY
    if firsts.get('plus') == (i, j):
        return cap, (f"Cell {p1} already held {e['had1']}, so the carry is ADDED (+=): it now holds {e['pos'][p1]}. "
                     "With = it would lose that."), KEY
    if (i, j) == (0, 0):
        return cap, "The last pair writes the leftmost cells. Cell 0 only ever gets this final carry.", KEY
    return cap, "", STEP


def build(num1, num2, subtitle, notes=None):
    events, ans = trace(num1, num2)
    firsts = {}
    for e in events:
        if e['kind'] == 'step':
            firsts.setdefault('first', (e['i'], e['j']))
            if e['had1'] and e['total'] // 10 and 'plus' not in firsts:
                firsts['plus'] = (e['i'], e['j'])
    m, n = len(num1), len(num2)
    sc = Scene('#43 Multiply Strings: one cell per column of the answer', subtitle)
    legend = [(ACTIVE, 'digits being multiplied'), (style('good')[1], 'cell i+j+1: keeps the last digit'),
              (style('gold')[1], 'cell i+j: gets the carry')]
    for e in events:
        k = e['kind']
        i, j = e.get('i'), e.get('j')
        a = ArrayView(list(num1), styles={i: 'active'} if i is not None else {},
                      pointers={'i': i} if i is not None else {}, title='num1')
        b = ArrayView(list(num2), styles={j: 'active'} if j is not None else {},
                      pointers={'j': j} if j is not None else {}, title='num2')
        styles, links, rings = {}, [], []
        if k == 'step':
            styles[(0, e['p2'])] = 'good'
            styles[(0, e['p1'])] = 'gold'
            rings = [((0, e['p2']), ACTIVE)]
            if e['total'] // 10:
                links = [dict(src=(0, e['p2']), dst=(0, e['p1']), color=style('gold')[1], lift=-34,
                              label=f"+{e['total'] // 10}")]
        if k == 'done':
            first = next((c for c, d in enumerate(e['pos']) if d), len(e['pos']))
            for c in range(first, m + n):
                styles[(0, c)] = 'good'
            for c in range(first):
                styles[(0, c)] = 'muted'
        pos = DPTableView([e['pos']], row_labels=['pos'], col_labels=[f'cell {c}' for c in range(m + n)],
                          styles=styles, links=links, rings=rings, max_cell=62, gap=12)
        if k == 'step':
            rows = [('pair', f'num1[{i}] × num2[{j}]'), ('product', str(e['mul'])),
                    (f'+ cell {e["p2"]}', str(e['had'])), ('total', str(e['total']), 'active'),
                    (f'keep → cell {e["p2"]}', str(e['total'] % 10), 'good'),
                    (f'carry → cell {e["p1"]}', str(e['total'] // 10), 'gold')]
        elif k == 'done':
            rows = [('answer', e['ans'], 'good')]
        else:
            rows = [('cells', f'{m} + {n} = {m + n}')]
        cap, sub, hold = words(e, num1, num2, firsts, notes)
        sc.frame([a, b, pos], cap, sub, hold, side=MapView(rows, 'This step', headers=('', '')),
                 counters={'steps': sum(1 for x in events[:events.index(e) + 1] if x['kind'] == 'step')},
                 legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    for a, b in (("2", "3"), ("123", "456")):          # the LeetCode samples
        assert short_array(a, b) == trace(a, b)[1]
    assert trace(HARD1, HARD2)[1] == "998001" and short_array(HARD1, HARD2) == "98001"
    sc = build(HARD1, HARD2, '999 × 999 = 998001: six digits, all m + n cells used.', HARD_NOTES)
    return sc, ("999 × 999 = 998001 fills every one of the m + n cells. Sizing the answer as m + n - 1 "
                "passes both LeetCode samples and answers 98001 here. Watch the last step's carry into cell 0.")


def main():
    args = cli()
    sc = build(NUM1, NUM2, 'Digit i of num1 times digit j of num2 adds into cell i + j + 1; the carry into cell i + j.')
    finish(sc, 43, "Watch the first step: 3 × 6 goes straight into the last cell, and every later pair lands in "
                   "cell i + j + 1 the same way, so no rows are ever written out.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
