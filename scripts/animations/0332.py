#!/usr/bin/env python3
"""#332 Reconstruct Itinerary: fly greedily, but write an airport down only when stuck there.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
from collections import defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

# The smallest input where "always fly to the smallest airport" gets stuck early.
TICKETS = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
POS = {'JFK': (0.15, 0.5), 'KUL': (0.95, 0.5), 'NRT': (0.55, 0.0)}


def trace(tickets):
    events, calls, used = [], [], []

    def rec(kind, graph, result, **kw):
        events.append(dict(kind=kind, left={k: list(v) for k, v in graph.items()}, result=list(result),
                           calls=list(calls), used=list(used), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    graph = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    result = []
    rec('start', graph, result)

    def dfs(airport):
        calls.append(airport)
        rec('arrive', graph, result, at=airport)
        while graph[airport]:
            nxt = graph[airport][-1]
            used.append((airport, nxt))
            rec('fly', graph, result, at=airport, to=nxt)
            dfs(graph[airport].pop())
            rec('back', graph, result, at=airport)
        result.append(airport)
        rec('stuck', graph, result, at=airport)
        calls.pop()

    dfs('JFK')
    rec('done', graph, result, answer=result[::-1])
    return events


def words(e, seen):
    k = e['kind']
    if k == 'start':
        return ("Group the tickets by departure, smallest destination last so pop() takes it.",
                "JFK's list is [NRT, KUL]: KUL comes out first.", STEP)
    if k == 'arrive':
        return (f"dfs({e['at']}): arrive at {e['at']}.", "", QUICK * 2)
    if k == 'fly':
        if e['at'] == 'JFK' and e['to'] == 'KUL':
            return ("JFK takes its smallest ticket: fly to KUL and tear the ticket up.",
                    "A plain greedy walk would write JFK, KUL now and be stuck with 2 tickets left.", KEY)
        return (f"{e['at']} still has a ticket: fly {e['at']} → {e['to']}.", "", STEP)
    if k == 'stuck':
        if not seen.get('stuck'):
            seen['stuck'] = True
            return (f"KUL has no tickets out: we're stuck, so write KUL down.",
                    "A dead end can only be the LAST stop. The list is built from the end backwards.", KEY)
        return (f"No tickets left at {e['at']}: write it down. Written so far: {', '.join(e['result'])}.", "", STEP)
    if k == 'back':
        if e['at'] == 'JFK' and e['left'].get('JFK'):
            return ("Back at JFK, and it still has the NRT ticket, so the loop keeps going.",
                    "That's why it's `while`, not `if`: the detour to KUL is already placed at the end.", KEY)
        return (f"Back at {e['at']}.", "", QUICK * 2)
    return (f"Reverse the written-down list: {' → '.join(e['answer'])}.",
            "Every ticket used once, and the dead end KUL landed last on its own.", END)


def main():
    args = cli()
    events = trace(TICKETS)
    sc = Scene('#332 Reconstruct Itinerary: write it down when stuck',
               'tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]. Start at JFK; smallest name first.')
    edges = [(a, b) for a, b in TICKETS]
    legend = [(ACTIVE, 'current airport'), (style('muted')[1], 'ticket used'), (style('good')[1], 'written down')]
    seen = {}
    for e in events:
        k = e['kind']
        styles = {a: 'good' for a in e['result']}
        if e['calls']:
            styles[e['calls'][-1]] = 'active'
        estyles = {ed: 'muted' for ed in e['used']}
        if k == 'fly':
            estyles[(e['at'], e['to'])] = 'active'
        graph = GraphView(POS, edges, directed=True, styles=styles, edge_styles=estyles, height=200, split=True)
        res = e['result']
        written = ArrayView(res + [''] * (len(TICKETS) + 1 - len(res)), styles={i: 'good' for i in range(len(res))},
                            title='written down', cell=58, indices=False)
        final = e.get('answer') or []
        itin = ArrayView(final + [''] * (len(TICKETS) + 1 - len(final)), styles={i: 'window' for i in range(len(final))},
                         title='reversed    ', cell=58, indices=False)
        stack = StackView([f'dfs({a})' for a in e['calls']], 'Call stack')
        tickets_left = len(TICKETS) - len(e['used'])
        cap, sub, hold = words(e, seen)
        sc.frame([graph, written, itin], cap, sub, hold, side=stack,
                 counters={'tickets left': tickets_left}, legend=legend)
    finish(sc, 332, "Watch the walk reach KUL first: it's a dead end, so KUL is written down first, which makes it "
                    "the last stop once the list is reversed, while JFK goes on to use the NRT tickets.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
