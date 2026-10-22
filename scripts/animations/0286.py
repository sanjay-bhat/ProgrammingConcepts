#!/usr/bin/env python3
"""#286 Walls and Gates: start the BFS from every gate at once.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Which gate's wave reached a room is
display-only bookkeeping (it isn't part of the algorithm).
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403
from collections import deque  # noqa: E402

INF = 2 ** 31 - 1
ROOMS = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]   # LeetCode example 1


def trace(rooms):
    m, n = len(rooms), len(rooms[0])
    src = [[None] * n for _ in range(m)]
    events = []

    def rec(kind, queue, **kw):
        events.append(dict(kind=kind, rooms=[r[:] for r in rooms], src=[r[:] for r in src],
                           queue=list(queue), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    queue = deque()
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j))
                src[i][j] = len(queue) - 1
    rec('seed', queue)
    while queue:
        r, c = queue.popleft()
        looked = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))
                src[nr][nc] = src[r][c]
                looked.append(((nr, nc), 'fill'))
            elif 0 <= nr < m and 0 <= nc < n:
                looked.append(((nr, nc), 'wall' if rooms[nr][nc] == -1 else
                               'gate' if rooms[nr][nc] == 0 else 'done'))
        rec('pop', queue, cell=(r, c), looked=looked)
    rec('done', queue)
    return events


def words(e, first):
    k = e['kind']
    if k == 'seed':
        gates = [(i, j) for i, row in enumerate(e['rooms']) for j, v in enumerate(row) if v == 0]
        return (f"Put BOTH gates, {gates[0]} and {gates[1]}, in the queue before anything else.",
                "Their waves now grow one step at a time, together, so the closer gate always arrives first.", KEY)
    if k == 'pop':
        (r, c), d = e['cell'], e['rooms'][e['cell'][0]][e['cell'][1]]
        fills = [p for p, o in e['looked'] if o == 'fill']
        done = [p for p, o in e['looked'] if o == 'done']
        if first.get('done') == id(e):
            mine = e['src'][r][c]
            p = next((q for q in done if e['src'][q[0]][q[1]] != mine), done[0])
            return (f"From {(r, c)} (distance {d}): {p} already holds {e['rooms'][p[0]][p[1]]}. Leave it alone.",
                    "A wave got there first, and waves arrive in distance order, so that number is already the smallest.", KEY)
        if not fills:
            return (f"Take {(r, c)} (distance {d}): no empty rooms next to it.", "", QUICK * 1.6)
        names = ', '.join(str(p) for p in fills)
        if first.get('second') == id(e):
            return (f"Now the other gate, {(r, c)}: {names} get{'s' if len(fills) == 1 else ''} distance 1.",
                    "Both waves are one step out before either takes a second step. That's why sharing one queue works.", KEY)
        if first.get('pop') == id(e):
            return (f"Take gate {(r, c)} off the queue. Its empty neighbours {names} are 1 step away.",
                    "Write the distance the moment a room is reached, and queue it: it'll never be reached sooner.", KEY)
        return (f"Take {(r, c)} (distance {d}): {names} get{'s' if len(fills) == 1 else ''} distance {d + 1}.", "", STEP)
    left = sum(v == INF for row in e['rooms'] for v in row)
    return ("Queue empty: every reachable room holds its distance to the nearest gate.",
            "Each room was written once and queued once, so the work grows with the number of squares."
            if not left else f"{left} rooms stay at infinity: no gate can reach them.", END)


def cells(e):
    out = []
    for i, row in enumerate(e['rooms']):
        out.append([])
        for j, v in enumerate(row):
            if v == -1:
                out[-1].append({'water': True})
            elif v == 0:
                out[-1].append({'style': f'region{e["src"][i][j]}', 'label': 'G', 'sub': 'gate'})
            elif v == INF:
                out[-1].append({'style': 'plain', 'label': '∞'})
            else:
                out[-1].append({'style': f'region{e["src"][i][j]}', 'label': str(v)})
    return out


def main():
    args = cli()
    events = trace([r[:] for r in ROOMS])
    first = {}
    for e in events:
        if e['kind'] == 'pop':
            if 'pop' not in first:
                first['pop'] = id(e)
            elif 'second' not in first:
                first['second'] = id(e)
            if 'done' not in first and any(o == 'done' for _, o in e['looked']):
                first['done'] = id(e)
    sc = Scene('#286 Walls and Gates: one BFS from every gate at once',
               'Slashed = wall. ∞ = empty room not reached yet. Colour = which gate\'s wave got there first.')
    legend = [(ACTIVE, 'taken off the queue'), (style('good')[1], 'just filled'), (REJECT, 'already has a distance')]
    for e in events:
        rings, marks = [], {}
        if e['kind'] == 'pop':
            rings.append((e['cell'], ACTIVE, 5))
            for p, o in e['looked']:
                if o == 'fill':
                    rings.append((p, style('good')[1], 4))
                elif o == 'done':
                    rings.append((p, REJECT, 3))
                    marks[p] = '×'
        q = [(f'({r},{c}) d={e["rooms"][r][c]}', f'region{e["src"][r][c]}') for r, c in e['queue']]
        cap, sub, hold = words(e, first)
        sc.frame([GridView(cells(e), outlines=rings, marks=marks, bridges=False, cell=72)], cap, sub, hold,
                 side=StackView(list(reversed(q)), 'Queue', note='front on top', empty='(empty)'),
                 counters={'in queue': len(e['queue'])}, legend=legend)
    finish(sc, 286, "Watch both gates start in the queue together: the room at (2,0) is reached from the "
                    "bottom-left gate in one step, before the far gate's wave could ever get there.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
