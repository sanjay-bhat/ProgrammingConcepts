#!/usr/bin/env python3
"""#130 Surrounded Regions: save what touches the border, capture everything else.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

BOARD = [list("XXXX"), list("XOOX"), list("XXOX"), list("XOXX")]          # LeetCode example 1


def trace(board):
    events, calls = [], []
    st = {'phase': 'border'}

    def rec(kind, **kw):
        events.append(dict(kind=kind, board=[r[:] for r in board], calls=list(calls), **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    m, n = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
            if 0 <= r < m and 0 <= c < n:
                rec('stop', cell=(r, c), seed=not calls)
            return
        board[r][c] = 'S'
        calls.append((r, c))
        rec('safe', cell=(r, c))
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        calls.pop()

    rec('start')
    for i in range(m):
        dfs(i, 0); dfs(i, n-1)
    for j in range(n):
        dfs(0, j); dfs(m-1, j)
    st['phase'] = 'scan'
    rec('scan')
    for r in range(m):
        for c in range(n):
            if board[r][c] == 'O':
                board[r][c] = 'X'
                rec('capture', cell=(r, c))
            elif board[r][c] == 'S':
                board[r][c] = 'O'
                rec('restore', cell=(r, c))
    rec('done')
    return events


def words(e, first):
    k = e['kind']
    if k == 'start':
        return ("Don't look for surrounded O's. Find the O's that CAN'T be surrounded: those linked to the edge.",
                "Start a search from every edge square; whatever O's it reaches are safe.", KEY)
    if k == 'stop':
        r, c = e['cell']
        if e['seed']:
            return (f"Edge square ({r},{c}) is {'X' if e['board'][r][c] == 'X' else 'already safe'}: nothing to start from.",
                    "", QUICK * 0.8)
        pr, pc = e['calls'][-1]
        if first.get('stop') == id(e):
            return (f"({pr},{pc}) looks up at ({r},{c}): it's X, so the safe region can't grow that way.",
                    "(2,2) touches (3,1) only at a corner, and corners don't connect, so it isn't saved.", KEY)
        return (f"({pr},{pc}) looks at ({r},{c}): it's X, so no growth that way either.", "", QUICK * 1.6)
    if k == 'safe':
        r, c = e['cell']
        if len(e['calls']) == 1:
            return (f"({r},{c}) is an O on the edge. Mark it S (safe) and spread to its neighbours.",
                    "It touches the outside, so nothing can surround it, or any O linked to it.", KEY)
        return (f"({r},{c}) is an O linked to a safe one: mark it S too.", "", STEP)
    if k == 'scan':
        return ("Edge searches done. Now one sweep: any O still left is cut off from the edge.",
                "O → X (captured). S → O (it was safe, so put it back).", KEY)
    if k == 'capture':
        r, c = e['cell']
        return (f"({r},{c}) is still O: no edge search reached it, so it's surrounded. Flip to X.", "",
                KEY if first.get('capture') == id(e) else STEP)
    if k == 'restore':
        r, c = e['cell']
        return (f"({r},{c}) is S: it was safe all along. Turn it back into O.", "", STEP)
    return ("Done: the three enclosed O's are captured; the edge O survives.",
            "Each square is marked at most once and swept once, so the work grows with the number of squares.", END)


def cells(e):
    out = []
    for row in e['board']:
        out.append([])
        for v in row:
            if v == 'X':
                out[-1].append({'style': 'muted', 'label': 'X'})
            elif v == 'S':
                out[-1].append({'style': 'good', 'label': 'S', 'sub': 'safe'})
            else:
                out[-1].append({'style': 'window', 'label': 'O'})
    return out


def main():
    args = cli()
    events = trace([r[:] for r in BOARD])
    first = {}
    for e in events:
        if e['kind'] == 'stop' and not e['seed'] and 'stop' not in first:
            first['stop'] = id(e)
        if e['kind'] == 'capture' and 'capture' not in first:
            first['capture'] = id(e)
    sc = Scene('#130 Surrounded Regions: save from the edge, capture the rest',
               'Only up/down/left/right count as connected. S = safe (linked to the edge).')
    legend = [(ACTIVE, 'being looked at'), (style('good')[1], 'safe'), (REJECT, 'stops the search')]
    for e in events:
        rings, marks = [], {}
        k = e['kind']
        if k in ('safe', 'capture', 'restore'):
            rings.append((e['cell'], ACTIVE, 5))
        if k == 'stop':
            rings.append((e['cell'], REJECT if not e['seed'] else CURSOR, 3))
            if not e['seed']:
                marks[e['cell']] = '×'
        stack = [f'dfs({r},{c})' for r, c in e['calls']]
        cap, sub, hold = words(e, first)
        phase = 'edge searches' if e['phase'] == 'border' else 'final sweep'
        sc.frame([GridView(cells(e), outlines=rings, marks=marks, bridges=False, cell=76)], cap, sub, hold,
                 side=StackView(stack, 'Call stack', base=f'solve  ({phase})', empty='(no search running)'),
                 counters={'safe': sum(v == 'S' for r in e['board'] for v in r)}, legend=legend)
    finish(sc, 130, "Watch the search start from the edge O at (3,1) and stop at once: the O's in the middle "
                    "are never reached, so the final sweep captures them.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
