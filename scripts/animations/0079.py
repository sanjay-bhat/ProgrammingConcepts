#!/usr/bin/env python3
"""#79 Word Search: mark a square before going deeper, put its letter back after.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import copy
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

BOARD = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
WORD = "ABCB"          # LeetCode example 3: the B would have to be used twice


def trace(board, word):
    orig = copy.deepcopy(board)
    events, calls = [], []
    st = {'sweep': None}

    def rec(kind, **kw):
        events.append(dict(kind=kind, board=[r[:] for r in board], calls=list(calls), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    m, n = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            rec('complete', idx=idx)
            return True
        if r < 0 or r >= m or c < 0 or c >= n:
            rec('offgrid', tried=(r, c), idx=idx)
            return False
        if board[r][c] != word[idx]:
            rec('marked' if board[r][c] == '#' else 'mismatch', cell=(r, c), idx=idx,
                had=board[r][c], orig=orig[r][c])
            return False

        tmp, board[r][c] = board[r][c], '#'
        calls.append((r, c, idx))
        rec('mark', cell=(r, c), idx=idx)
        found = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1)
                 or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1))
        board[r][c] = tmp
        calls.pop()
        rec('restore', cell=(r, c), idx=idx, found=found)
        return found

    rec('start')
    for r in range(m):
        for c in range(n):
            st['sweep'] = (r, c)
            if dfs(r, c, 0):
                rec('done', answer=True)
                return events
    st['sweep'] = None
    rec('done', answer=False)
    return events


def words(e, first):
    k = e['kind']
    if k == 'start':
        return (f'Look for "{WORD}": try every square as the first letter.',
                "Each letter must touch the last one (up, down, left, right), and no square twice.", KEY)
    if k == 'mark':
        (r, c), idx = e['cell'], e['idx']
        if idx == 0:
            return (f"({r},{c}) is '{WORD[0]}', the first letter. Mark it '#' and look around it.",
                    "The mark means: this square is already in the path, don't step on it again.", KEY)
        return (f"({r},{c}) matches '{WORD[idx]}', letter {idx + 1} of {len(WORD)}. Mark it '#' and go deeper.",
                "", STEP)
    if k == 'mismatch':
        (r, c), idx = e['cell'], e['idx']
        if idx == 0:
            return (f"Start at ({r},{c})? It's '{e['had']}', not '{WORD[0]}'. Move on.", "", QUICK * 0.8)
        return (f"({r},{c}) is '{e['had']}', but we need '{WORD[idx]}'. Dead end.", "", QUICK)
    if k == 'marked':
        (r, c), idx = e['cell'], e['idx']
        if first.get('marked') == id(e):
            return (f"({r},{c}) was '{e['orig']}', the letter we need, but it's marked '#': already in the path.",
                    f"Without the mark, the search would reuse it and wrongly spell {WORD}.", KEY)
        return (f"({r},{c}) is marked '#', already in this path. Skip it.", "", QUICK)
    if k == 'offgrid':
        r, c = e['tried']
        return (f"({r},{c}) is off the board. Dead end.", "", QUICK * 0.8)
    if k == 'restore':
        (r, c), idx = e['cell'], e['idx']
        if first.get('restore') == id(e):
            return (f"Every direction from ({r},{c}) failed. Put its '{WORD[idx]}' back and return.",
                    "Another path may still need that square, so the mark must not outlive this attempt.", KEY)
        return (f"Nothing works from ({r},{c}): restore '{WORD[idx]}' and back up.", "", STEP)
    if k == 'complete':
        return ("All letters matched.", "", KEY)
    if e['answer']:
        return (f'Found "{WORD}". Answer: true.', "", END)
    return (f'No start square works, so "{WORD}" isn\'t on the board. Answer: false.',
            "Every mark was undone on the way back: the board is exactly as it started.", END)


def cells(e):
    out = []
    for r, row in enumerate(e['board']):
        out.append([])
        for c, v in enumerate(row):
            if v == '#':
                out[-1].append({'style': 'good', 'label': '#', 'sub': f'was {BOARD[r][c]}'})
            else:
                out[-1].append({'style': 'plain', 'label': v})
    return out


def main():
    args = cli()
    events = trace(copy.deepcopy(BOARD), WORD)
    first = {}
    for e in events:
        for k in ('marked', 'restore'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
    sc = Scene('#79 Word Search: mark, explore, restore',
               f'word = "{WORD}". Green # = square in the current path.')
    legend = [(CURSOR, 'start square'), (ACTIVE, 'being matched'), (REJECT, 'dead end')]
    for e in events:
        rings, marks = [], {}
        if e['sweep']:
            rings.append((e['sweep'], CURSOR, 3))
        if e['kind'] in ('mark', 'restore'):
            rings.append((e['cell'], ACTIVE, 5))
        if e['kind'] in ('mismatch', 'marked') and e['idx'] > 0:
            rings.append((e['cell'], REJECT, 4))
            marks[e['cell']] = '×'
        depth = len(e['calls'])
        wstyles = {j: 'good' for j in range(depth)}
        if e['kind'] in ('mismatch', 'marked', 'offgrid') and e['idx'] < len(WORD):
            wstyles[e['idx']] = 'bad' if e['idx'] > 0 or e['kind'] != 'mismatch' else 'active'
        wv = ArrayView(list(WORD), wstyles, title='word', cell=50,
                       pointers={'idx': e['idx']} if e.get('idx') is not None and e['idx'] < len(WORD) else {})
        stack = [(f"dfs({r},{c}) '{WORD[i]}'", 'good') for r, c, i in e['calls']]
        sw = e['sweep']
        cap, sub, hold = words(e, first)
        sc.frame([GridView(cells(e), outlines=rings, marks=marks, cell=70), wv], cap, sub, hold,
                 side=StackView(stack, 'Call stack', base=f'exist  start at {sw if sw else "-"}',
                                empty='(no path being explored)'),
                 counters={'matched': f'{depth}/{len(WORD)}'}, legend=legend)
    finish(sc, 79, "Watch (0,2) look back at the B it came from: the square is marked #, so the search "
                   "can't use it twice, and every mark is put back before the next start is tried.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
