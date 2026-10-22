#!/usr/bin/env python3
"""#1143 Longest Common Subsequence: a match steps diagonally (+1 on the box
up-left), a mismatch takes the better of dropping one letter (above or left).

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The input is LeetCode's example 1.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

A, B = "abcde", "ace"   # LeetCode example 1: answer 3 ("ace")


def trace(text1, text2):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            m, n = len(text1), len(text2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            rec('base', dp=[r[:] for r in dp], i=0, j=0)
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if text1[i - 1] == text2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                        rec('match', dp=[r[:] for r in dp], i=i, j=j)
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                        rec('skip', dp=[r[:] for r in dp], i=i, j=j)
            rec('done', dp=[r[:] for r in dp], ans=dp[m][n], i=m, j=n)
            return dp[m][n]

    Solution().longestCommonSubsequence(text1, text2)
    return events


def traceback(dp):
    """Walk back from the corner to find which match boxes built the answer."""
    i, j, cells = len(A), len(B), []
    while i and j:
        if A[i - 1] == B[j - 1]:
            cells.append((i, j)); i -= 1; j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return cells


def main():
    args = cli()
    m, n = len(A), len(B)
    sc = Scene('#1143 LCS: match = diagonal + 1, otherwise the better neighbour',
               f'dp[i][j] = longest common subsequence of the first i letters of "{A}" and the first j of "{B}".')
    legend = [(ACTIVE, 'just filled'), (style('good')[1], 'letters match'), (style('gold')[1], 'empty-prefix row/column')]
    filled, first_skip, first_match = set(), True, True
    for e in trace(A, B):
        k, dp, i, j = e['kind'], e['dp'], e['i'], e['j']
        if k in ('match', 'skip'):
            filled.add((i, j))
        styles, links, rings, matches = {}, [], [], set()
        vals = [[''] * (n + 1) for _ in range(m + 1)]
        for r in range(m + 1):
            for c in range(n + 1):
                if r == 0 or c == 0:
                    vals[r][c] = dp[r][c]
                    styles[(r, c)] = 'gold'
                elif (r, c) in filled:
                    vals[r][c] = dp[r][c]
                    styles[(r, c)] = 'good' if A[r - 1] == B[c - 1] else 'plain'
        hold, rows = STEP, []
        if k == 'base':
            cap = "Row 0 and column 0 are all 0: an empty string shares nothing with anything."
            sub = "Every other box is built from the box above, the box to the left, or the one up-left."
            hold = KEY
        elif k == 'match':
            styles[(i, j)] = 'active'
            links = [dict(src=(i - 1, j - 1), dst=(i, j), color=style('good')[1], label='+1')]
            rings = [((i, j), ACTIVE)]
            rows = [('compare', f"'{A[i - 1]}' vs '{B[j - 1]}'"), ('rule', 'up-left + 1', 'good'),
                    ('dp[i][j]', str(dp[i][j]), 'active')]
            cap = f"'{A[i - 1]}' = '{B[j - 1]}': dp[{i}][{j}] = up-left {dp[i - 1][j - 1]} + 1 = {dp[i][j]}."
            if first_match:
                sub = "Use the letter in both strings at once, on top of the best answer without either."
                hold, first_match = KEY, False
            elif (i, j) == (m, n):
                sub = "Always up-left: both 'e's are used now. 'Above + 1' could count one 'e' twice."
                hold = KEY
            else:
                sub = ''
        elif k == 'skip':
            up, left = dp[i - 1][j], dp[i][j - 1]
            styles[(i, j)] = 'active'
            src = (i - 1, j) if up >= left else (i, j - 1)
            other = (i, j - 1) if src == (i - 1, j) else (i - 1, j)
            links = [dict(src=src, dst=(i, j)), dict(src=other, dst=(i, j), color=FAINT)]
            rings = [((i, j), ACTIVE)]
            rows = [('compare', f"'{A[i - 1]}' vs '{B[j - 1]}'"), ('rule', 'max(above, left)'),
                    ('dp[i][j]', str(dp[i][j]), 'active')]
            cap = f"'{A[i - 1]}' ≠ '{B[j - 1]}': dp[{i}][{j}] = max(above {up}, left {left}) = {dp[i][j]}."
            if first_skip:
                sub = "One of the two letters can't be in the answer here, so drop one and keep the better result."
                hold, first_skip = KEY, False
            else:
                sub = ''
                hold = QUICK * 1.6
        else:
            matches = set(traceback(dp))
            for c in matches:
                styles[c] = 'good'
            rings = [((m, n), style('good')[1])] + [(c, style('good')[1]) for c in matches if c != (m, n)]
            rows = [('answer', str(e['ans']), 'good'), ('letters', '"ace"', 'good')]
            cap = f"Returns dp[{m}][{n}] = {e['ans']}. The ringed matches spell \"ace\"."
            sub = f"{m} × {n} boxes, each filled once from three neighbours: O(m × n) time."
            hold = END
        table = DPTableView(vals, row_labels=['""'] + [f'{c}' for c in A],
                            col_labels=['""'] + [f'{c}' for c in B],
                            styles=styles, rings=rings, links=links, max_cell=52, gap=12)
        sc.frame([table], cap, sub, hold, side=MapView(rows, 'This box', headers=('', ''), empty=''),
                 legend=legend)
    finish(sc, 1143, "Watch the 'e' box in the corner: the letters match, so it takes the up-left box "
                     "plus one, never the box above.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
