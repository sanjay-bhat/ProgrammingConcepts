#!/usr/bin/env python3
"""#417 Pacific Atlantic Water Flow: flood UPHILL from each ocean, keep the overlap.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Only the first "too low" rejection
is shown as its own frame; the rest are folded into the visit frames.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

HEIGHTS = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]   # LeetCode ex. 1


def trace(heights):
    events, calls = [], []
    m, n = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def rec(kind, **kw):
        events.append(dict(kind=kind, P=set(pacific), A=set(atlantic), calls=list(calls), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def dfs(r, c, visited):
        ocean = 'P' if visited is pacific else 'A'
        new = (r, c) not in visited
        visited.add((r, c))
        calls.append((r, c, ocean))
        rec('visit', cell=(r, c), ocean=ocean, new=new)
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                dfs(nr, nc, visited)
            elif 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                rec('low', cell=(r, c), nb=(nr, nc), ocean=ocean)
        calls.pop()

    rec('start')
    for i in range(m):
        dfs(i, 0, pacific)
        dfs(i, n - 1, atlantic)
    for j in range(n):
        dfs(0, j, pacific)
        dfs(m - 1, j, atlantic)
    result = [[r, c] for r, c in pacific & atlantic]
    rec('done', result=sorted(result))
    return events


NAME = {'P': 'Pacific', 'A': 'Atlantic'}


def words(e, first):
    k = e['kind']
    if k == 'start':
        return ("Don't follow water down from every square. Flood UPHILL from each ocean instead.",
                "Pacific = top and left edges, Atlantic = bottom and right. A square that both floods reach drains to both.", KEY)
    if k == 'visit':
        (r, c), o = e['cell'], e['ocean']
        h = HEIGHTS[r][c]
        if first.get('both') == id(e):
            return (f"The {NAME[o]} flood reaches ({r},{c}), which the other flood already holds. It turns green.",
                    "Water from this square can run down to the Pacific AND to the Atlantic: it's part of the answer.", KEY)
        if not e['calls'][:-1]:
            if not e['new']:
                return (f"Start the {NAME[o]} flood at edge square ({r},{c}): already reached, nothing new.", "", QUICK)
            return (f"{NAME[o]} flood starts at edge square ({r},{c}), height {h}: it touches that ocean.", "", STEP)
        pr, pc, _ = e['calls'][-2]
        if first.get('climb') == id(e):
            return (f"({r},{c}) is {h}, at least as high as ({pr},{pc}) at {HEIGHTS[pr][pc]}. The {NAME[o]} flood climbs in.",
                    f"Water at ({r},{c}) could run down to ({pr},{pc}) and on to the ocean, so mark it.", KEY)
        return (f"{NAME[o]} flood climbs to ({r},{c}), height {h}.", "", QUICK * 1.6)
    if k == 'low':
        (r, c), (a, b) = e['cell'], e['nb']
        return (f"({a},{b}) is {HEIGHTS[a][b]}, lower than ({r},{c}) at {HEIGHTS[r][c]}: the flood can't climb there.",
                f"Water can't run uphill from ({a},{b}) to ({r},{c}), so this route doesn't help it reach the {NAME[e['ocean']]}.", KEY)
    return (f"Answer: the {len(e['result'])} green squares both floods reached.",
            "Each flood adds a square at most once, so the work grows with the number of squares.", END)


def cells(e):
    out = []
    for i, row in enumerate(HEIGHTS):
        out.append([])
        for j, h in enumerate(row):
            p, a = (i, j) in e['P'], (i, j) in e['A']
            st = 'good' if p and a else 'region1' if p else 'region3' if a else 'plain'
            sub = 'both' if p and a else 'Pacific' if p else 'Atlantic' if a else ''
            out[-1].append({'style': st, 'label': str(h), 'sub': sub})
    return out


def main():
    args = cli()
    events = trace([r[:] for r in HEIGHTS])
    first = {}
    shown = []
    for e in events:
        if e['kind'] == 'visit' and len(e['calls']) > 1 and 'climb' not in first:
            first['climb'] = id(e)
        if e['kind'] == 'visit' and e['new'] and e['cell'] in e['P'] & e['A'] and 'both' not in first:
            first['both'] = id(e)
        if e['kind'] == 'low':
            if 'low' in first:
                continue
            first['low'] = id(e)
        shown.append(e)
    sc = Scene('#417 Pacific Atlantic: flood uphill from both oceans',
               'Numbers are heights. Water flows to a neighbour that is equal or lower.')
    legend = [(style('region1')[1], 'Pacific reaches'), (style('region3')[1], 'Atlantic reaches'),
              (style('good')[1], 'both'), (ACTIVE, 'current square')]
    for e in shown:
        rings, marks = [], {}
        if e['kind'] == 'visit':
            rings.append((e['cell'], ACTIVE, 5))
        if e['kind'] == 'low':
            rings.append((e['cell'], ACTIVE, 5))
            rings.append((e['nb'], REJECT, 4))
            marks[e['nb']] = '×'
        stack = [(f'dfs({r},{c}) {NAME[o]}', 'region1' if o == 'P' else 'region3') for r, c, o in e['calls']]
        cap, sub, hold = words(e, first)
        sc.frame([GridView(cells(e), outlines=rings, marks=marks, bridges=False, cell=64)], cap, sub, hold,
                 side=StackView(stack, 'Call stack', base='pacificAtlantic', empty='(between floods)'),
                 counters={'Pacific': len(e['P']), 'Atlantic': len(e['A']), 'both': len(e['P'] & e['A'])},
                 legend=legend)
    finish(sc, 417, "Watch the floods climb inward from the edges: a square goes green only when both the "
                    "Pacific and the Atlantic flood have reached it, which means its water can run down to both.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
