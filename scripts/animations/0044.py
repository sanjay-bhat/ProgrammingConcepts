#!/usr/bin/env python3
"""#44 Wildcard Matching: fill a table of "does s[:i] match p[:j]?" one row at
a time; the code keeps only one row and overwrites it in place.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The big table is the history of that
one row (row i = the row after the i-th character of s); the strip under it is
the actual 1-D array at that moment, half new row and half old.

The walkthrough uses s = "adceb", p = "*a*b", an example from LeetCode's
original problem statement: it has two stars and one of them must swallow
three characters.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S, P = "adceb", "*a*b"

# Hard example 1 (interactive page only): stopping a star at the first
# character that fits what follows passes all three LeetCode samples
# ("aa"/"a", "aa"/"*", "cb"/"?a"), then says false here: the star stops before
# the first 'a', the pattern's 'b' meets the second 'a', and there's no going
# back. Correct: true (the star takes "a").
HARD_LAZY = ("aab", "*ab")
HARD_LAZY_NOTES = {
    (2, 2): "The star took the first 'a' (the box above was T), so this 'a' can match the second one.",
    'done': "True. A star that stops at the first 'a' would leave 'b' facing 'a' and answer false.",
}
# Hard example 2: a sloppy top row. Marking every star column true in row 0
# (forgetting that everything before the star must match nothing too) passes
# all three LeetCode samples, then says "ab" matches "x*ab". Correct: false.
HARD_INIT = ("ab", "x*ab")
HARD_INIT_NOTES = {
    (0, 2): "False, because x can't match nothing. Writing T here just because it's a star is the bug: it leaks down the column.",
    'done': "False: the x has nothing to match. With a T in row 0 under the star, this corner comes out true.",
}


def lazy_star(s, p):
    """First attempt broken by HARD_LAZY: a star stops at the first character that fits what follows."""
    i = j = 0
    while j < len(p):
        if p[j] == '*':
            j += 1
            if j == len(p):
                return True
            while i < len(s) and not (p[j] == '?' or p[j] == s[i]):
                i += 1
        elif i < len(s) and (p[j] == '?' or p[j] == s[i]):
            i += 1
            j += 1
        else:
            return False
    return i == len(s)


def eat_all(s, p):
    """First attempt broken by the walkthrough's own input: a star swallows everything left."""
    i = j = 0
    while j < len(p):
        if p[j] == '*':
            i, j = len(s), j + 1
        elif i < len(s) and (p[j] == '?' or p[j] == s[i]):
            i, j = i + 1, j + 1
        else:
            return False
    return i == len(s)


def sloppy_top_row(s, p):
    """First attempt broken by HARD_INIT: row 0 marks every star column true."""
    m, n = len(s), len(p)
    dp = [False] * (n + 1)
    dp[0] = True
    for j in range(1, n + 1):
        dp[j] = p[j - 1] == '*'
    for i in range(1, m + 1):
        prev, dp[0] = dp[0], False
        for j in range(1, n + 1):
            temp = dp[j]
            dp[j] = (dp[j - 1] or dp[j]) if p[j - 1] == '*' else (prev and (p[j - 1] == '?' or p[j - 1] == s[i - 1]))
            prev = temp
    return dp[n]


def trace(s, p):
    events = []
    m, n = len(s), len(p)
    table = [[None] * (n + 1) for _ in range(m + 1)]

    def rec(kind, dp, i, j, **kw):
        events.append(dict(kind=kind, dp=dp[:], i=i, j=j, table=[r[:] for r in table], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    dp = [False] * (n + 1)
    dp[0] = True
    table[0][0] = True
    rec('start', dp, 0, 0)

    for j in range(1, n + 1):
        dp[j] = dp[j - 1] and p[j - 1] == '*'
        table[0][j] = dp[j]
        rec('init', dp, 0, j)

    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = False
        table[i][0] = False

        for j in range(1, n + 1):
            temp = dp[j]
            if p[j - 1] == '*':
                left, up = dp[j - 1], dp[j]
                dp[j] = dp[j - 1] or dp[j]
                table[i][j] = dp[j]
                rec('star', dp, i, j, left=left, up=up)
            else:
                diag = prev
                dp[j] = prev and (p[j - 1] == '?' or p[j - 1] == s[i - 1])
                table[i][j] = dp[j]
                rec('char', dp, i, j, diag=diag)
            prev = temp

    rec('done', dp, m, n, ans=dp[n])
    return events, dp[n]


def tf(b):
    return 'T' if b else 'F'


def words(e, s, p, firsts, notes):
    k = e['kind']
    key = 'done' if k == 'done' else (e['i'], e['j'])
    cap, sub, hold = _words(e, s, p, firsts)
    if notes and key in notes:
        return cap, notes[key], (END if k == 'done' else KEY)
    return cap, sub, hold


def _words(e, s, p, firsts):
    k, i, j = e['kind'], e['i'], e['j']
    if k == 'start':
        return ("Box (i, j): do the first i characters of s match the first j of p? Empty vs empty: T.",
                "The code keeps one row (the strip below) and overwrites it; the big table is its history.", KEY)
    if k == 'done':
        return (f"Bottom-right box: the whole string against the whole pattern = {tf(e['ans'])}.",
                f"{len(s) + 1} × {len(p) + 1} boxes, each from at most two others, and one row of memory.", END)
    pc, val = p[j - 1], e['table'][i][j]
    if k == 'init':
        if pc == '*':
            return (f"Row 0, '{p[:j]}' vs the empty string: a star can match nothing, and so did everything before it: {tf(val)}.",
                    "", STEP if val else KEY)
        return (f"Row 0, '{p[:j]}' vs the empty string: '{pc}' needs a real character. F.", "", QUICK * 2)
    sc = s[i - 1]
    if k == 'star':
        cap = (f"'{s[:i]}' vs '{p[:j]}': the star matches nothing (left = {tf(e['left'])}) "
               f"or swallows '{sc}' (above = {tf(e['up'])}): {tf(val)}.")
        if firsts.get('up') == (i, j):
            return cap, ("The box above is still in the array: the star takes this character and stays "
                         "available for the next one."), KEY
        return cap, "", STEP
    ok = pc == '?' or pc == sc
    cap = (f"'{s[:i]}' vs '{p[:j]}': '{pc}' {'matches' if ok else 'does not match'} '{sc}', "
           f"and the diagonal (saved in prev) is {tf(e['diag'])}: {tf(val)}.")
    if firsts.get('diag') == (i, j):
        return cap, "A letter or ? uses up exactly one character, so it needs everything before to match: the diagonal.", KEY
    return cap, "", STEP


def build(s, p, subtitle, notes=None):
    events, ans = trace(s, p)
    m, n = len(s), len(p)
    firsts = {}
    for e in events:
        if e['kind'] == 'star' and e['up'] and not e['left']:
            firsts.setdefault('up', (e['i'], e['j']))
        if e['kind'] == 'char' and e['table'][e['i']][e['j']]:
            firsts.setdefault('diag', (e['i'], e['j']))
    sc = Scene('#44 Wildcard Matching: fill the table, read the corner', subtitle)
    legend = [(style('good')[1], 'T: prefixes match'), (ACTIVE, 'box being filled'),
              (style('window')[1], 'the one row in memory'), (REJECT, 'rule that failed')]
    good = style('good')[1]
    for e in events:
        k, i, j = e['kind'], e['i'], e['j']
        vals, styles = [], {}
        for r in range(m + 1):
            row = []
            for c in range(n + 1):
                v = e['table'][r][c]
                row.append('' if v is None else tf(v))
                if v:
                    styles[(r, c)] = 'good'
                elif v is not None:
                    styles[(r, c)] = 'plain'
            vals.append(row)
        rings, links = [], []
        if k in ('init', 'star', 'char'):
            styles[(i, j)] = 'active'
            rings = [((i, j), ACTIVE)]
        if k == 'init' and p[j - 1] == '*':
            links = [dict(src=(0, j - 1), dst=(0, j), color=good if e['table'][0][j - 1] else REJECT,
                          cross=not e['table'][0][j - 1])]
        if k == 'star':
            links = [dict(src=(i, j - 1), dst=(i, j), color=good if e['left'] else REJECT, cross=not e['left']),
                     dict(src=(i - 1, j), dst=(i, j), color=good if e['up'] else REJECT, cross=not e['up'])]
        if k == 'char':
            ok = p[j - 1] == '?' or p[j - 1] == s[i - 1]
            links = [dict(src=(i - 1, j - 1), dst=(i, j), color=good if e['diag'] and ok else REJECT,
                          cross=not (e['diag'] and ok), label=None if ok else '≠')]
        if k == 'done':
            rings = [((m, n), good if ans else REJECT)]
        table = DPTableView(vals, row_labels=['∅'] + list(s), col_labels=['∅'] + list(p),
                            styles=styles, rings=rings, links=links, max_cell=40, gap=8)
        # the real 1-D array: cells 0..j hold the new row i, cells after j still hold row i - 1
        arr_styles = {}
        for c in range(n + 1):
            new = k == 'done' or c <= j
            arr_styles[c] = ('good' if e['dp'][c] else 'window') if new else 'muted'
        strip = ArrayView([tf(v) for v in e['dp']], styles=arr_styles,
                          pointers={'j': j} if k in ('init', 'star', 'char') else {}, title='dp', indices=False, cell=40)
        rows = [('i (chars of s)', str(i)), ('j (chars of p)', str(j))]
        if k == 'char':
            rows.append(('prev (diagonal)', tf(e['diag']), 'gold'))
        if k == 'star':
            rows += [('left: dp[j-1]', tf(e['left']), 'good' if e['left'] else 'bad'),
                     ('above: dp[j]', tf(e['up']), 'good' if e['up'] else 'bad')]
        if k == 'done':
            rows.append(('answer', tf(ans), 'good' if ans else 'bad'))
        cap, sub, hold = words(e, s, p, firsts, notes)
        sc.frame([table, strip], cap, sub, hold, side=MapView(rows, 'This box', headers=('', '')),
                 legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = (("aa", "a"), ("aa", "*"), ("cb", "?a"))
    for f in (lazy_star, eat_all, sloppy_top_row):          # every first attempt passes the samples
        assert all(f(a, b) == trace(a, b)[1] for a, b in samples)
    assert trace(S, P)[1] is True and eat_all(S, P) is False
    assert trace(*HARD_LAZY)[1] is True and lazy_star(*HARD_LAZY) is False
    assert trace(*HARD_INIT)[1] is False and sloppy_top_row(*HARD_INIT) is True
    lazy = build(*HARD_LAZY, 's = "aab", p = "*ab". Answer true: the star must take exactly one a.', HARD_LAZY_NOTES)
    init = build(*HARD_INIT, 's = "ab", p = "x*ab". Answer false: the x has nothing to match.', HARD_INIT_NOTES)
    return [
        (lazy, "Stopping a star at the first character that fits what follows passes all three LeetCode samples, "
               "then answers false here. Watch the star's column turn T in row 1: it takes the first a."),
        (init, "A top row that marks every star column true passes all three samples, then says \"ab\" matches "
               "\"x*ab\". Watch row 0: the star column stays F because x can't match nothing."),
    ]


def main():
    args = cli()
    sc = build(S, P, 's = "adceb", p = "*a*b". Rows: first i characters of s. Columns: first j characters of p.')
    finish(sc, 44, "Watch the second star's column fill with T from row 1 down: it swallows d, c and e one row at a "
                   "time by copying the box above, which is why the b at the end can still match.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
