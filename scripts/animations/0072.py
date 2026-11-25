#!/usr/bin/env python3
"""#72 Edit Distance: box (i, j) is the fewest edits that turn the first i
letters of word1 into the first j letters of word2. Matching letters copy the
up-left box; otherwise it's 1 + the cheapest of up-left (replace), above
(delete) and left (insert).

The notebook keeps only ONE row, dp, and saves the up-left value in `prev`
before it's overwritten. The table drawn here is that row's history: each
row is a snapshot of dp after the notebook finished it, and the blue boxes
are the ones the one-row array actually holds at that moment.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

WORD1, WORD2 = "horse", "ros"          # LeetCode example 1: answer 3

# Hard example 1: greedy with a one-letter look-ahead (on a mismatch, skip a
# letter if that realigns the words, else replace) gets both LeetCode samples
# right (3 and 5), then answers 7 here. The cheap route inserts "at" early,
# which no local rule can see.
HARD1 = ("sunday", "saturday")
HARD1_ANSWER, HARD1_WRONG = 3, 7

# Hard example 2: "a match is free in every direction", i.e. on a match taking
# min(up-left, above, left) with no +1. Also passes both samples, then says
# "balloon" -> "balon" costs 0: the second 'l' and second 'o' ride for free on
# the box above, which really means deleting a letter.
HARD2 = ("balloon", "balon")
HARD2_ANSWER, HARD2_WRONG = 2, 0


class Column(View):
    """Side panel: the one-row dp array on top, this box's working below it."""

    def __init__(self, views):
        self.views = views

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        y = y0
        for v in self.views[:-1]:
            v.draw(p, (x0 + 4, y, x1, y1))
            y += v.used + 18
        self.views[-1].draw(p, (x0, y, x1, y1))
        self.used = y1 - y0


class Solution:
    # ---- the notebook's solution, unchanged (used to check the answers) ----
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(prev, dp[j], dp[j - 1]) + 1
                prev = temp
        return dp[n]


def wrong_lookahead(a, b):
    """First attempt: walk both words; on a mismatch skip a letter if the next one realigns, else replace."""
    i = j = cost = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1; j += 1
        elif i + 1 < len(a) and a[i + 1] == b[j]:
            cost += 1; i += 1            # delete a[i]
        elif j + 1 < len(b) and a[i] == b[j + 1]:
            cost += 1; j += 1            # insert b[j]
        else:
            cost += 1; i += 1; j += 1    # replace
    return cost + (len(a) - i) + (len(b) - j)


def wrong_free_match(a, b):
    """First attempt: on a match, take the cheapest of all three neighbours with no +1."""
    m, n = len(a), len(b)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            best = min(prev, dp[j], dp[j - 1])
            dp[j] = best if a[i - 1] == b[j - 1] else best + 1
            prev = temp
    return dp[n]


SAMPLES = [("horse", "ros", 3), ("intention", "execution", 5)]
for _a, _b, _ans in SAMPLES:          # both first attempts pass both LeetCode samples
    assert Solution().minDistance(_a, _b) == wrong_lookahead(_a, _b) == wrong_free_match(_a, _b) == _ans
assert Solution().minDistance(*HARD1) == HARD1_ANSWER and wrong_lookahead(*HARD1) == HARD1_WRONG
assert Solution().minDistance(*HARD2) == HARD2_ANSWER and wrong_free_match(*HARD2) == HARD2_WRONG


def trace(word1, word2):
    events, rows = [], []

    def rec(kind, **kw):
        events.append(dict(kind=kind, dp=dp[:], rows=[r[:] for r in rows], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    m, n = len(word1), len(word2)
    dp = list(range(n + 1))
    rows.append(dp[:])
    rec('base', i=0, j=n)
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        rec('row', i=i, j=0, prev=prev)
        for j in range(1, n + 1):
            temp = dp[j]
            left = dp[j - 1]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = prev
                rec('match', i=i, j=j, prev=prev, above=temp, left=left)
            else:
                dp[j] = min(prev, dp[j], dp[j - 1]) + 1
                rec('edit', i=i, j=j, prev=prev, above=temp, left=left)
            prev = temp
        rows.append(dp[:])
    rec('done', i=m, j=n, ans=dp[n])
    return events


def build(word1, word2, subtitle, notes=None):
    """notes: {(i, j): text} replaces that box's second caption line, held as KEY;
    'done' replaces the last frame's."""
    notes = notes or {}
    m, n = len(word1), len(word2)
    sc = Scene('#72 Edit Distance: each box = cheapest of its three neighbours', subtitle, side_width=320)
    legend = [(ACTIVE, 'just filled'), (style('window')[1], 'in the one-row array'),
              (style('gold')[1], 'prev: saved up-left'), (style('muted')[1], 'overwritten')]
    first = set()
    for e in trace(word1, word2):
        k, i, j, dp = e['kind'], e['i'], e['j'], e['dp']
        vals = [[''] * (n + 1) for _ in range(m + 1)]
        styles = {}
        for r, row in enumerate(e['rows']):
            for c, v in enumerate(row):
                vals[r][c] = v
                styles[(r, c)] = 'muted'
        if k != 'done':
            for c in range(n + 1):             # what the one array holds right now
                r = i if c <= j else i - 1
                if r >= 0:
                    vals[r][c] = dp[c]
                    styles[(r, c)] = 'window'
        links, rings, side, hold = [], [], [], STEP
        arr_styles = {c: 'window' for c in range(n + 1)}
        subs = {c: (f'row {i}' if c <= j else f'row {i - 1}') for c in range(n + 1)} if k not in ('base', 'done') else {}
        pointers = {'j': j} if k in ('match', 'edit', 'row') else {}
        if k == 'base':
            cap = f'Row 0: turning "" into the first j letters of "{word2}" takes j inserts.'
            sub = "So dp starts as 0, 1, 2, ... The notebook keeps only this one row and rewrites it."
            hold = KEY
            rings = [((0, c), style('window')[1]) for c in range(n + 1)]
            side = [('dp', 'range(n + 1)', 'window'), ('meaning', 'j inserts')]
        elif k == 'row':
            styles[(i - 1, 0)] = 'gold'
            styles[(i, 0)] = 'active'
            arr_styles[0] = 'active'
            rings = [((i, 0), ACTIVE)]
            cap = (f'Row {i} ("{word1[:i]}"): save the old dp[0] = {e["prev"]} as prev, '
                   f'then dp[0] = {i}.')
            if 'row' not in first:
                first.add('row')
                sub = (f'Turning "{word1[:i]}" into "" is {i} delete(s). Save BEFORE overwriting: '
                       'prev is the next box\'s up-left.')
                hold = KEY
            else:
                sub = ''
                hold = QUICK * 2
            side = [('prev (up-left)', str(e['prev']), 'gold'), ('dp[0]', f'{i} deletes', 'active')]
        elif k in ('match', 'edit'):
            up_left, above, left, val = e['prev'], e['above'], e['left'], dp[j]
            a, b = word1[i - 1], word2[j - 1]
            styles[(i, j)] = 'active'
            styles[(i - 1, j - 1)] = 'gold'
            vals[i - 1][j - 1] = up_left
            arr_styles[j] = 'active'
            rings = [((i, j), ACTIVE)]
            if k == 'match':
                links = [dict(src=(i - 1, j - 1), dst=(i, j), color=style('good')[1])]
                # the free-match trap: a neighbour that looks cheaper but still costs a letter
                for src, v in (((i - 1, j), above), ((i, j - 1), left)):
                    if v < up_left:
                        links.append(dict(src=src, dst=(i, j), cross=True))
                cap = f"'{a}' = '{b}': nothing to fix, so copy the up-left box. dp[{i}][{j}] = {val}."
                sub = ''
                if 'match' not in first:
                    first.add('match')
                    sub, hold = "Keep this letter and pay whatever the two shorter prefixes cost.", KEY
                else:
                    hold = STEP
                side = [('letters', f"'{a}' = '{b}'", 'good'), ('up-left (prev)', f'{up_left}  keep: {up_left}', 'good'),
                        ('above  dp[j]', f'{above}  delete: {above + 1}'),
                        ('left  dp[j-1]', f'{left}  insert: {left + 1}'),
                        (f'dp[{i}][{j}]', str(val), 'active')]
            else:
                opts = [(up_left, (i - 1, j - 1), 'replace'), (above, (i - 1, j), 'delete'),
                        (left, (i, j - 1), 'insert')]
                best = min(o[0] for o in opts)
                for v, src, _ in opts:
                    links.append(dict(src=src, dst=(i, j), color=ACTIVE if v == best else FAINT))
                pick = ' or '.join(name for v, _, name in opts if v == best)
                cap = f"'{a}' ≠ '{b}': 1 + min({up_left}, {above}, {left}) = {val}  (cheapest: {pick})."
                sub = ''
                if 'edit' not in first:
                    first.add('edit')
                    sub = ("Up-left = replace, above = delete a letter of word1, left = insert one of word2.")
                    hold = KEY
                else:
                    hold = QUICK * 2
                side = [('letters', f"'{a}' ≠ '{b}'", 'bad'),
                        ('up-left (prev)', f'{up_left}  replace', 'active' if up_left == best else None),
                        ('above  dp[j]', f'{above}  delete', 'active' if above == best else None),
                        ('left  dp[j-1]', f'{left}  insert', 'active' if left == best else None),
                        (f'dp[{i}][{j}]', f'1 + {best} = {val}', 'active')]
            if (i, j) == (m, n) and not notes.get((i, j)):
                sub, hold = f'The corner: "{word1}" into "{word2}" costs {val}.', KEY
            if (i, j) in notes:
                sub, hold = notes[(i, j)], KEY
        else:
            ans = e['ans']
            for c in range(n + 1):
                styles[(m, c)] = 'window'
            styles[(m, n)] = 'good'
            rings = [((m, n), style('good')[1])]
            arr_styles[n] = 'good'
            cap = f'minDistance("{word1}", "{word2}") returns dp[{n}] = {ans}.'
            sub = notes.get('done', f'{m} × {n} boxes, each from three neighbours: O(m × n) time, '
                                    f'and only {n + 1} numbers kept.')
            hold = END
            side = [('answer', str(ans), 'good')]
        table = DPTableView(vals, row_labels=['""'] + list(word1), col_labels=['""'] + list(word2),
                            styles=styles, rings=rings, links=links, max_cell=54, gap=14)
        arr = ArrayView(dp, styles=arr_styles, pointers=pointers, title='dp', subs=subs)
        sc.frame([table], cap, sub, hold, side=Column([arr, MapView(side, 'This box', headers=('', ''), empty='')]),
                 counters={'edits': dp[n]} if k == 'done' else None, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(*HARD1, 'word1 = "sunday", word2 = "saturday". Answer 3: insert "a", insert "t", replace n with r.',
                {(2, 4): "Up-left is 2: \"s\" into \"sat\" by inserting 'a' and 't'. That lines 'u' up with 'u'. Greedy never tries it.",
                 'done': "Greedy with a one-letter look-ahead replaces five letters in a row, then inserts two: 7."})
    sc2 = build(*HARD2, 'word1 = "balloon", word2 = "balon". Two doubled letters, so two deletes.',
                {(4, 3): "Above is 0, but above means deleting the second 'l': that still costs 1.",
                 (6, 4): "Above is 1, but that's deleting an 'o' again. Only the diagonal is free.",
                 'done': "Making a match free in every direction gets both LeetCode samples right and answers 0 here."})
    return [(sc1, 'Greedy with a one-letter look-ahead passes both LeetCode samples, then turns "sunday" into '
                  '"saturday" with 7 edits. The table finds 3, by inserting "at" early.'),
            (sc2, 'Taking min(up-left, above, left) on a match, with no +1, passes both samples, then says '
                  '"balloon" to "balon" costs 0. The crossed arrows are the free rides it would take.')]


def main():
    args = cli()
    sc = build(WORD1, WORD2, 'Rows: first i letters of "horse". Columns: first j letters of "ros". Answer: bottom-right.')
    finish(sc, 72, "Watch the first box of each row: the old up-left value is saved in prev before "
                   "it's overwritten, because the next box needs it for 'replace'.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
