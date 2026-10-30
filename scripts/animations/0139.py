#!/usr/bin/env python3
"""#139 Word Break: dp[i] is True when the first i letters split into words,
and it becomes True when some earlier True cut j is followed by a word s[j:i].

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The input is LeetCode's example 3,
where two different routes reach "catsand" and then "og" leaves it stuck.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S = "catsandog"                                  # LeetCode example 3
WORDS = ["cats", "dog", "sand", "and", "cat"]


def trace(s, wordDict):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def wordBreak(self, s: str, wordDict: list[str]) -> bool:
            word_set = set(wordDict)
            n = len(s)
            dp = [False] * (n + 1)
            dp[0] = True
            rec('base', dp=dp[:])
            for i in range(1, n + 1):
                skipped = []
                for j in range(i):
                    if not dp[j]:
                        skipped.append(j)
                    else:
                        rec('check', i=i, j=j, word=s[j:i], hit=s[j:i] in word_set, dp=dp[:],
                            skipped=skipped[:])
                    if dp[j] and s[j:i] in word_set:
                        dp[i] = True
                        break
                rec('cell', i=i, dp=dp[:])
            rec('done', ans=dp[n], dp=dp[:])
            return dp[n]

    Solution().wordBreak(s, wordDict)
    return events


def main():
    args = cli()
    n = len(S)
    sc = Scene('#139 Word Break: a cut is reachable if a word ends there',
               'dp[i] = can the first i letters be split into dictionary words? T = yes, F = no.')
    legend = [(ACTIVE, 'piece being looked up'), (style('good')[1], 'True / word found'),
              (REJECT, 'not a word')]
    first_hit = {}
    evs = trace(S, WORDS)
    for e in evs:
        k = e['kind']
        dp = e['dp']
        styles, links, rings = {}, [], []
        filled = {c for c in range(n + 1)}
        if k == 'check':
            filled = set(range(e['i']))
        elif k in ('cell',):
            filled = set(range(e['i'] + 1))
        elif k == 'base':
            filled = {0}
        row = []
        for c in range(n + 1):
            if c in filled:
                row.append('T' if dp[c] else 'F')
                styles[(1, c)] = 'good' if dp[c] else 'muted'
            else:
                row.append('')
        letters = [''] + list(S)
        hl = 'plain'
        dictrows = [(w, f'{len(w)} letters') for w in WORDS]
        hold = STEP
        if k == 'base':
            rings = [((1, 0), ACTIVE)]
            cap = "dp[0] = T: the empty start can always be 'split' (into nothing)."
            sub = "Every real split begins here. Column i is the cut after the i-th letter."
            hold = KEY
        elif k == 'check':
            i, j, w = e['i'], e['j'], e['word']
            hl = 'good' if e['hit'] else 'bad'
            for c in range(j + 1, i + 1):
                styles[(0, c)] = hl if e['hit'] else 'active'
            links = [dict(src=(1, j), dst=(1, i), lift=-40 - 8 * min(i - j, 6), cross=not e['hit'],
                          color=style('good')[1], label=f'"{w}"')]
            rings = [((1, j), style('good')[1]), ((1, i), ACTIVE)]
            if e['hit']:
                dictrows = [(x, 'match', 'good') if x == w else (x, f'{len(x)} letters') for x in WORDS]
                if i == 7:
                    cap = f'dp[3] is T and "sand" is a word, so dp[7] = T. Stop looking.'
                    sub = '"cats"+"and" would also work, but one route is enough: break.'
                    hold = KEY
                elif i == 3:
                    cap = f'dp[0] is T and "{w}" is a word, so dp[3] = T.'
                    sub = "The first i letters split if an earlier cut is T and the rest is one word."
                    hold = KEY
                else:
                    cap = f'dp[{j}] is T and "{w}" is a word, so dp[{i}] = T.'
                    sub = ''
            else:
                cap = f'dp[{j}] is T, but "{w}" isn\'t a word.'
                sk = e['skipped']
                sub = (f"Cuts {', '.join(map(str, sk))} are F, so they're skipped without a lookup."
                       if sk and j == max(c for c in range(i) if dp[c]) else '')
                hold = QUICK * 2
                if i == 9 and j == 7:
                    cap = 'dp[7] is T, but "og" isn\'t a word. No True cut is left to try.'
                    sub = 'So dp[9] stays F, even though 7 of the 9 letters split fine.'
                    hold = KEY
        elif k == 'cell':
            i = e['i']
            rings = [((1, i), ACTIVE)]
            if dp[i]:
                continue
            tried = [c for c in range(i) if dp[c]]
            cap = f'dp[{i}] = F: no True cut is followed by a word ending at letter {i}.'
            sub = f"Tried from cut{'s' if len(tried) > 1 else ''} {', '.join(map(str, tried))}."
            hold = QUICK * 2 if i != 9 else STEP
        else:
            cap = f"wordBreak returns {e['ans']}: dp[9] is F, so \"catsandog\" can't be split."
            sub = "About n²/2 cut pairs at most, each a substring lookup. Here, 20 lookups."
            hold = END
            rings = [((1, n), REJECT)]
        table = DPTableView([letters, row], row_labels=['letter', 'dp'],
                            col_labels=[str(c) for c in range(n + 1)],
                            styles=styles, rings=rings, links=links, max_cell=50)
        sc.frame([TextView([f's = "{S}"'], size=18), table], cap, sub, hold,
                 side=MapView(dictrows, 'Dictionary', headers=('word', '')), legend=legend)
    finish(sc, 139, "Watch dp[7]: it becomes True from cut 3 plus \"sand\", and then every lookup "
                    "for the last two letters fails, so the answer is False.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
