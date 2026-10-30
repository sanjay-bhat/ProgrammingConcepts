#!/usr/bin/env python3
"""#212 Word Search II: one trie for all the words, and a backtracking walk from
every square that steps down the trie as it steps across the board.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The input is LeetCode's example 1.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

BOARD = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
WORDS = ["oath", "pea", "eat", "rain"]   # LeetCode example 1


class Row(View):
    """Two views side by side (board on the left, trie on the right)."""

    def __init__(self, left, right, split=0.52):
        self.left, self.right, self.split = left, right, split

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        mid = x0 + (x1 - x0) * self.split
        self.left.draw(p, (x0, y0, mid - 12, y1))
        self.right.draw(p, (mid + 12, y0, x1, y1))
        self.used = max(self.left.used, self.right.used)


def trace(board_in, words):
    board = [r[:] for r in board_in]
    events, calls, path, result = [], [], [], []
    st = {'start': None}

    def rec(kind, **kw):
        events.append(dict(kind=kind, board=[r[:] for r in board], calls=list(calls), path=list(path),
                           result=list(result), start=st['start'], **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
            root = {}
            for word in words:
                node = root
                for c in word:
                    node = node.setdefault(c, {})
                node['$'] = word

            m, n = len(board), len(board[0])
            result_ = result

            def dfs(i: int, j: int, node: dict) -> None:
                if i < 0 or i >= m or j < 0 or j >= n:
                    return
                c = board[i][j]
                if c not in node:
                    rec('reject', cell=(i, j), c=c, depth=len(path))
                    return
                node = node[c]
                path.append((i, j)); calls.append(''.join(board_in[a][b] for a, b in path))
                rec('enter', cell=(i, j), c=c)
                if '$' in node:
                    result_.append(node.pop('$'))
                    rec('found', cell=(i, j), word=result_[-1])
                board[i][j] = '#'
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    dfs(i + di, j + dj, node)
                board[i][j] = c
                path.pop(); calls.pop()
                rec('restore', cell=(i, j), c=c)

            for i in range(m):
                for j in range(n):
                    st['start'] = (i, j)
                    dfs(i, j, root)
            st['start'] = None
            return result_

    rec('begin')
    ans = Solution().findWords(board, words)
    rec('done', ans=ans)
    return events


def words(e):
    k = e['kind']
    c = e.get('cell')
    if k == 'begin':
        return ("All four words go into one trie. Then start a walk from every square.",
                "Each step on the board is a step down the trie; no child means no word goes this way.", STEP)
    if k == 'reject':
        if e['depth'] == 0:
            return (f"Start at ({c[0]},{c[1]}): no word begins with '{e['c']}'. Skip it.", "", QUICK * 0.8)
        if e['c'] == '#':
            return (f"({c[0]},{c[1]}) is already on this path: not allowed twice.", "", QUICK)
        return (f"Neighbour ({c[0]},{c[1]}) is '{e['c']}': no word continues \"{e['calls'][-1]}{e['c']}\".",
                "", QUICK)
    if k == 'enter':
        pre = e['calls'][-1]
        if pre == 'eat' or (pre == 'ea' and e['start'] == (1, 3)):
            if pre == 'eat':
                return (f"({c[0]},{c[1]}) is 't' again, free now: \"eat\".",
                        "The oath walk restored this square when it backed out, so eat can use it.", KEY)
        if len(pre) == 1:
            return (f"Start at ({c[0]},{c[1]}): '{pre}' begins a word, so walk from here.", "", STEP)
        return (f"Step to ({c[0]},{c[1]}): \"{pre}\" is still the start of a word. Mark it and keep going.", "", STEP)
    if k == 'found':
        return (f"The trie node for \"{e['word']}\" holds a word: record it and pop it.",
                "Popping means a second path to the same word would find nothing to add.", KEY)
    if k == 'restore':
        if e['c'] == 't' and len(e['path']) == 2 and e['start'] == (0, 0):
            return (f"Back out of ({c[0]},{c[1]}): restore its 't'.",
                    "Without this undo, the square stays blocked and eat is never found.", KEY)
        return (f"Back out of ({c[0]},{c[1]}): restore '{e['c']}' for other paths.", "", QUICK)
    return (f"findWords returns {e['ans']}.",
            "pea never starts (no p), and rain dies after r: no a beside it.", END)


def trie_nodes(words):
    kids = {'': []}
    for w in words:
        for i in range(len(w)):
            if w[:i + 1] not in kids:
                kids[w[:i + 1]] = []
                kids[w[:i]].append(w[:i + 1])
    leaves, xs = [], {}

    def walk(p):
        if not kids[p]:
            xs[p] = len(leaves); leaves.append(p)
        else:
            for c in kids[p]:
                walk(c)
            xs[p] = (xs[kids[p][0]] + xs[kids[p][-1]]) / 2
    walk('')
    pos = {p: (xs[p] / (len(leaves) - 1), len(p) / 4) for p in kids}
    return kids, pos


def main():
    args = cli()
    sc = Scene('#212 Word Search II: walk the board and the trie together',
               'Board left, trie of all four words right. Orange: the current path. # = square in use.',
               side_width=270)
    legend = [(ACTIVE, 'current square'), (style('window')[1], 'on the path'), (style('good')[1], 'word found'),
              (REJECT, 'rejected')]
    kids, pos = trie_nodes(WORDS)
    edges = [(p, c) for p, cs in kids.items() for c in cs]
    for e in trace(BOARD, WORDS):
        found_cells = set()
        cells = []
        on_path = set(e['path'])
        for i, row in enumerate(e['board']):
            cells.append([])
            for j, v in enumerate(row):
                st = 'window' if (i, j) in on_path else 'plain'
                cells[-1].append({'style': st, 'label': v})
        outlines, marks = [], {}
        if e['kind'] in ('enter', 'found', 'restore'):
            outlines.append((e['cell'], ACTIVE, 5))
        if e['kind'] == 'reject':
            outlines.append((e['cell'], REJECT, 3)); marks[e['cell']] = '×'
        if e['start'] and e['kind'] != 'reject':
            pass
        grid = GridView(cells, outlines=outlines, marks=marks)
        pre = e['calls'][-1] if e['calls'] else ''
        tstyles = {w: 'good' for w in e['result']}
        for i in range(len(pre) + 1):
            if pre[:i] in kids:
                tstyles[pre[:i]] = 'window' if pre[:i] not in e['result'] else 'good'
        estyles = {(pre[:i], pre[:i + 1]): 'active' for i in range(len(pre)) if pre[:i + 1] in kids}
        rings = [(pre, ACTIVE)] if pre in kids and pre else []
        text = {p: (p[-1] if p else 'root') for p in kids}
        trie = GraphView(pos, edges, styles=tstyles, edge_styles=estyles, rings=rings, text=text, height=300)
        stack = [f'dfs{a} "{w}"' for a, w in zip(e['path'], e['calls'])]
        cap, sub, hold = words(e)
        sc.frame(Row(grid, trie), cap, sub, hold,
                 side=StackView(stack, 'Call stack', base='findWords', empty='(between starts)'),
                 counters={'found': ', '.join(e['result']) or 'none'}, legend=legend)
    finish(sc, 212, "Watch the oath walk back out of (1,1) and restore its 't': a moment later the eat walk "
                    "comes through the same square and needs it.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
