#!/usr/bin/env python3
"""#10 Regular Expression Matching: fill a table of "does this much of s match
this much of p?", one square at a time, each answer read from squares already
filled.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Rows are prefixes of s (row i = the
first i letters), columns are prefixes of p, and the bottom-right square is
the answer.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S, P = "aab", "c*a*b"        # LeetCode's classic chained-star example: true

# Hard examples (interactive page only), each breaking a plausible first attempt.
# 1) Greedy: let x* swallow as many x's as it can, then carry on. Passes all
#    three LeetCode samples, but here a* eats both a's and leaves nothing for
#    the literal 'a' that follows. Answer true; greedy says false.
HARD_GREEDY = ("aab", "c*a*ab")
# 2) Zero copies of x* written as dp[i][j-1] (skip only the star) instead of
#    dp[i][j-2] (skip the whole pair). Also passes all three samples. Here c*
#    has to vanish completely in the middle of the string. Answer true; that
#    version says false.
HARD_PAIR = ("ab", "ac*b")


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]


def greedy(s, p):
    """First attempt: x* takes every x it can, then the rest of p carries on."""
    i = j = 0
    while j < len(p):
        if j + 1 < len(p) and p[j + 1] == '*':
            while i < len(s) and (p[j] == '.' or p[j] == s[i]):
                i += 1
            j += 2
        elif i < len(s) and (p[j] == '.' or p[j] == s[i]):
            i, j = i + 1, j + 1
        else:
            return False
    return i == len(s)


def skip_star_only(s, p):
    """First attempt: the notebook's table, but 'zero copies' reads dp[i][j-1]."""
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1]
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            elif p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]


def trace(s, p):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, dp=[row[:] for row in dp], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    rec('origin')
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
            rec('base', i=0, j=j)
    rec('base_done')
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                zero = dp[i][j]                                    # display only
                more = None
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    more = dp[i - 1][j]                            # display only
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                rec('star', i=i, j=j, zero=zero, more=more)
            elif p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
                rec('lit', i=i, j=j)
            else:
                rec('miss', i=i, j=j)
    rec('done', ans=dp[m][n])
    assert dp[m][n] == Solution().isMatch(s, p)
    return events


def q(x):
    return f'"{x}"'


def words(e, s, p, seen):
    k = e['kind']
    dp = e['dp']
    if k == 'origin':
        return ("Square (i, j) answers: do the first i letters of s match the first j of p?",
                "Top-left: empty s vs empty p. That always matches, so it starts true.", KEY)
    if k == 'base':
        j = e['j']
        v = dp[0][j]
        first = 'base' not in seen
        seen.add('base')
        return (f"Empty s vs {q(p[:j])}: '{p[j - 2]}*' can mean zero copies, so copy the square two to the left: "
                f"{'T' if v else 'F'}.",
                "This is how a pattern like \"c*\" matches nothing at all." if first else "", KEY if first else STEP)
    if k == 'base_done':
        return ("Row 0 is done. Every other square in it stays false: a letter can't match empty s.",
                "Now fill row by row, left to right. Each square only looks up and to the left.", STEP)
    i, j = e.get('i'), e.get('j')
    if k == 'done':
        return (f"Bottom-right square: {q(s)} vs {q(p)} is {'true' if e['ans'] else 'false'}.",
                "(m + 1) × (n + 1) squares, each filled in one step: O(m × n). At 20 × 20 that's 441 squares.", END)
    sp, pp = q(s[:i]), q(p[:j])
    v = 'T' if dp[i][j] else 'F'
    if k == 'lit':
        first = 'lit' not in seen
        seen.add('lit')
        return (f"{sp} vs {pp}: '{p[j - 1]}' matches '{s[i - 1]}', so take the answer without both: "
                f"square ({i - 1}, {j - 1}) = {v}.",
                "A plain letter or '.' eats exactly one letter of s. Go one up and one left." if first else "",
                KEY if first else STEP)
    if k == 'miss':
        return (f"{sp} vs {pp}: '{p[j - 1]}' can't match '{s[i - 1]}'. False.", "", QUICK * 1.6)
    # star
    x = p[j - 2]
    z = 'T' if e['zero'] else 'F'
    if e['more'] is None:
        first = 'star0' not in seen
        seen.add('star0')
        return (f"{sp} vs {pp}: zero copies of '{x}*' → square ({i}, {j - 2}) = {z}. "
                f"'{x}' can't match '{s[i - 1]}', so no more.",
                "Zero copies means skipping the letter AND its star: two columns left." if first else "",
                KEY if first else QUICK * 2)
    mo = 'T' if e['more'] else 'F'
    first = 'star1' not in seen
    seen.add('star1')
    return (f"{sp} vs {pp}: zero copies → ({i}, {j - 2}) = {z}; one more '{x}' → ({i - 1}, {j}) = {mo}. "
            + (f"One is enough: {v}." if dp[i][j] else "Neither: F."),
            "One more copy eats s's last letter and stays on the same star, so look straight up." if first else "",
            KEY if first else STEP)


def build(s, p, subtitle, notes=None):
    notes = notes or {}
    m, n = len(s), len(p)
    sc = Scene('#10 Regular Expression Matching: fill the table', subtitle)
    legend = [(ACTIVE, 'square being filled'), (style('good')[1], 'true: matches'),
              (style('muted')[1], 'false'), (style('gold')[1], 'answer')]
    rl = ['""'] + [f'{s[i - 1]}' for i in range(1, m + 1)]
    cl = ['""'] + list(p)
    seen = set()
    for e in trace(s, p):
        k, dp = e['kind'], e['dp']
        i, j = e.get('i'), e.get('j')
        filled = set()
        # squares the loops have reached so far
        for r in range(m + 1):
            for c in range(n + 1):
                if r == 0 and k != 'origin':
                    filled.add((r, c))
                elif k in ('star', 'lit', 'miss') and (r, c) <= (i, j) and r >= 1 and c >= 1:
                    filled.add((r, c))
                elif k == 'done' and r >= 1 and c >= 1:
                    filled.add((r, c))
        if k == 'base':
            filled = {(0, c) for c in range(j + 1)} | {(0, 0)}
        for r in range(1, m + 1):
            if k in ('star', 'lit', 'miss', 'done') and (r, 0) not in filled:
                if k == 'done' or r <= i:
                    filled.add((r, 0))
        filled.add((0, 0))
        vals = [[('T' if dp[r][c] else 'F') if (r, c) in filled else '' for c in range(n + 1)]
                for r in range(m + 1)]
        styles = {rc: ('good' if dp[rc[0]][rc[1]] else 'muted') for rc in filled}
        links, rings = [], []
        if k in ('base', 'star', 'lit', 'miss'):
            styles[(i, j)] = 'active'
            rings = [((i, j), ACTIVE)]
        if k == 'base':
            links = [dict(src=(0, j - 2), dst=(0, j), lift=34, label='zero')]
        elif k == 'star':
            links = [dict(src=(i, j - 2), dst=(i, j), lift=34, label='zero',
                          color=style('good')[1] if e['zero'] else MUTED)]
            if e['more'] is not None:
                links.append(dict(src=(i - 1, j), dst=(i, j), label='+1',
                                  color=style('good')[1] if e['more'] else MUTED))
        elif k == 'lit':
            links = [dict(src=(i - 1, j - 1), dst=(i, j), color=style('good')[1] if dp[i][j] else MUTED)]
        elif k == 'done':
            styles[(m, n)] = 'gold'
            rings = [((m, n), style('good')[1] if e['ans'] else REJECT)]
        table = DPTableView(vals, row_labels=rl, col_labels=cl, styles=styles, rings=rings, links=links,
                            max_cell=58, gap=26)
        if k in ('star', 'lit', 'miss'):
            rows = [('s so far', q(s[:i])), ('p so far', q(p[:j])), ('this square', vals[i][j], 'active')]
        elif k == 'base':
            rows = [('s so far', '""'), ('p so far', q(p[:j])), ('this square', vals[0][j], 'active')]
        elif k == 'done':
            rows = [('s', q(s)), ('p', q(p)), ('answer', 'true' if e['ans'] else 'false',
                                                 'good' if e['ans'] else 'bad')]
        else:
            rows = [('s', q(s)), ('p', q(p))]
        cap, sub, hold = words(e, s, p, seen)
        key = (k, i, j) if k != 'done' else 'done'
        if key in notes:
            sub, hold = notes[key], (END if k == 'done' else KEY)
        sc.frame([table], cap, sub, hold, side=MapView(rows, 'This square', headers=('', '')),
                 legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = [("aa", "a", False), ("aa", "a*", True), ("ab", ".*", True)]
    for s, p, want in samples:      # both first attempts pass every LeetCode sample
        assert Solution().isMatch(s, p) == greedy(s, p) == skip_star_only(s, p) == want
    assert Solution().isMatch(*HARD_GREEDY) is True and greedy(*HARD_GREEDY) is False
    assert Solution().isMatch(*HARD_PAIR) is True and skip_star_only(*HARD_PAIR) is False
    g = build(*HARD_GREEDY, f's = "{HARD_GREEDY[0]}", p = "{HARD_GREEDY[1]}". Answer true. Greedy a* says false.', {
        ('star', 1, 4): "The table keeps BOTH options open: a* has eaten one 'a' here, and the next square "
                        "lets the literal 'a' take the second.",
        ('lit', 2, 5): "\"aa\" vs \"c*a*a\" is true: a* took one 'a', the literal took the other. "
                       "Greedy a* took both and never tries this.",
        'done': "True. A greedy a* swallows both a's, leaves \"ab\" of the pattern facing \"b\", and answers false.",
    })
    z = build(*HARD_PAIR, f's = "{HARD_PAIR[0]}", p = "{HARD_PAIR[1]}". Answer true. Skipping only the star says false.', {
        ('star', 1, 3): "Zero copies of c* must skip 'c' AND '*': two columns left, to \"a\" vs \"a\" = T. "
                        "One column left lands on \"a\" vs \"ac\" = F.",
        'done': "True. With 'zero copies' read one column left, \"a\" vs \"ac*\" comes out false and so does the answer.",
    })
    return [
        (g, "\"aab\" against \"c*a*ab\": the a* must stop after one 'a' so the literal 'a' can take the next. "
            "Letting x* grab every x it can passes all three LeetCode samples, then answers false here; the answer is true."),
        (z, "\"ab\" against \"ac*b\": c* has to vanish in the middle of the string. Reading 'zero copies' as one "
            "column left (skipping just the star) passes all three samples, then answers false; the answer is true."),
    ]


def main():
    args = cli()
    sc = build(S, P, f's = "{S}", p = "{P}". Rows: letters of s used so far. Columns: pattern used so far.')
    finish(sc, 10, "Watch square (1, 4), \"a\" vs \"c*a*\": the star square looks two columns left for zero "
                   "copies and straight up for one more, and either one being true is enough.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
