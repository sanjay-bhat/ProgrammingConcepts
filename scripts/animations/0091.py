#!/usr/bin/env python3
"""#91 Decode Ways: each new digit can be read alone (from the count one step
back) or as a pair with the digit before it (from the count two steps back).

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The input is "11106", the example in
the problem statement, because its zero shows both checks failing in turn.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S = "11106"   # from the problem statement: "AAJF" (1 1 10 6) and "KJF" (11 10 6)


def trace(s):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def numDecodings(self, s: str) -> int:
            if s[0] == '0':
                return 0
            prev2, prev1 = 1, 1
            rec('base', prev2=prev2, prev1=prev1)
            for i in range(1, len(s)):
                curr = 0
                if s[i] != '0':
                    curr += prev1
                rec('single', i=i, ok=s[i] != '0', add=prev1, curr=curr, prev2=prev2, prev1=prev1)
                two_digit = int(s[i - 1:i + 1])
                if 10 <= two_digit <= 26:
                    curr += prev2
                rec('pair', i=i, ok=10 <= two_digit <= 26, two=s[i - 1:i + 1], add=prev2,
                    curr=curr, prev2=prev2, prev1=prev1)
                prev2, prev1 = prev1, curr
            rec('done', ans=prev1)
            return prev1

    rec('start')
    Solution().numDecodings(s)
    return events


def words(e):
    k = e['kind']
    if k == 'start':
        return ("ways[k] = how many ways to decode the first k digits.",
                "Fill it left to right; the answer is the last box. The code keeps only the newest two boxes.", STEP)
    if k == 'base':
        return ("Start: ways[0] = 1 (nothing to decode is one way), ways[1] = 1 ('1' is A).",
                "These two are the only boxes not built from earlier ones. prev2 and prev1 hold them.", KEY)
    if k == 'done':
        return (f"numDecodings returns {e['ans']}: AAJF (1 1 10 6) and KJF (11 10 6).",
                "One pass, two numbers remembered at a time: O(n) time, O(1) extra space.", END)
    i, d = e['i'], S[e['i']]
    if k == 'single':
        if e['ok']:
            extra = ("Every way to decode the first {0} digits, plus '{1}' on the end.".format(i, d))
            hold = KEY if i == 1 else STEP
            if i == 4:
                extra = "'6' alone is F, so every decoding of '1110' just gets an F added."
                hold = STEP
            return (f"Read '{d}' alone: it's a letter, so take ways[{i}] = {e['add']}.", extra, hold)
        return (f"Read '{d}' alone: no letter is 0, so this adds nothing.",
                "A zero can only ever be the second half of 10 or 20.", KEY)
    if k == 'pair':
        two = e['two']
        if e['ok']:
            if i == 3:
                return (f"Read '{two}' as a pair: that's J, so take ways[{i - 1}] = {e['add']}. Total {e['curr']}.",
                        "The zero survives only because the 1 before it can join it.", KEY)
            return (f"Read '{two}' as a pair: that's a letter, so add ways[{i - 1}] = {e['add']}. Total {e['curr']}.",
                    f"ways[{i + 1}] = ways[{i}] + ways[{i - 1}]: the last digit alone, or the last two together.",
                    KEY if i == 1 else STEP)
        return (f"Read '{two}' as a pair: a leading zero isn't a letter, so add nothing. Total {e['curr']}.",
                "Checking only '<= 26' would wrongly count 06 here and answer 5.", KEY)


def main():
    args = cli()
    n = len(S)
    sc = Scene('#91 Decode Ways: one digit alone, or two together',
               'Box k = ways to decode the first k digits. Arrows show which earlier boxes a new box adds up.')
    legend = [(ACTIVE, 'digits being read'), (style('good')[1], 'filled'),
              (REJECT, 'not a letter, adds nothing')]
    ways = [None] * (n + 1)
    for e in trace(S):
        k = e['kind']
        styles, links, rings = {}, [], []
        dig = [''] + list(S)
        if k == 'base':
            ways[0], ways[1] = 1, 1
        if k in ('single', 'pair'):
            i = e['i']
            ways[i + 1] = e['curr']
            if k == 'single':
                styles[(0, i + 1)] = 'active'
            else:
                styles[(0, i)] = styles[(0, i + 1)] = 'active'
            # the single-digit arrow stays on screen while the pair is checked
            sok = S[i] != '0'
            links.append(dict(src=(1, i), dst=(1, i + 1), cross=not sok, lift=-30,
                              color=style('good')[1] if k == 'pair' else ACTIVE,
                              label=None if k == 'pair' else (f'+{e["prev1"]}' if sok else None)))
            if k == 'pair':
                links.append(dict(src=(1, i - 1), dst=(1, i + 1), lift=-84, cross=not e['ok'],
                                  label=f'+{e["prev2"]}' if e['ok'] else None))
            rings = [((1, i + 1), ACTIVE)]
        for c in range(n + 1):
            if ways[c] is not None and (1, c) not in [r[0] for r in rings]:
                styles[(1, c)] = 'good'
        if k == 'done':
            styles[(1, n)] = 'good'
            rings = [((1, n), style('good')[1])]
        if k == 'base':
            rings = [((1, 0), ACTIVE), ((1, 1), ACTIVE)]
        vals = [dig, [('' if v is None else v) for v in ways]]
        table = DPTableView(vals, row_labels=['digit', 'ways'],
                            col_labels=[f'k={c}' for c in range(n + 1)],
                            styles=styles, rings=rings, links=links, max_cell=74)
        if k in ('single', 'pair', 'base'):
            p2 = e['prev2'] if k != 'base' else 1
            p1 = e['prev1'] if k != 'base' else 1
            rows = [('prev2', str(p2)), ('prev1', str(p1))]
            if k != 'base':
                rows = [('i', str(e['i'])), ('prev2', f'{p2}  = ways[{e["i"] - 1}]'),
                        ('prev1', f'{p1}  = ways[{e["i"]}]'), ('curr', str(e['curr']), 'active')]
        elif k == 'done':
            rows = [('prev1', f'{e["ans"]}  = ways[{n}]', 'good')]
        else:
            rows = []
        side = MapView(rows, 'Variables', headers=('name', 'value'), empty='(not started)')
        cap, sub, hold = words(e)
        sc.frame([TextView([f's = "{S}"'], size=18), table], cap, sub, hold, side=side, legend=legend)
    finish(sc, 91, "Watch the zero at k=4: read alone it's not a letter, so the only way in is "
                   "as the pair 10, and then 06 is rejected too.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
