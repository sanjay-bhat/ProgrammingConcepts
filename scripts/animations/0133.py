#!/usr/bin/env python3
"""#133 Clone Graph: put each copy in the map BEFORE visiting its neighbours.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

ADJ = [[2, 4], [1, 3], [2, 4], [1, 3]]          # LeetCode example 1: the 4-cycle 1-2-3-4-1
POS = {1: (0.1, 0.1), 2: (0.9, 0.1), 3: (0.9, 0.9), 4: (0.1, 0.9)}


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build(adj):
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nbrs]
    return nodes[0]


def trace(node):
    events, calls = [], []

    def rec(kind, cloned, **kw):
        links = [(c.val, nb.val) for c in cloned.values() for nb in c.neighbors]
        events.append(dict(kind=kind, made=[(o.val, c.val) for o, c in cloned.items()],
                           links=links, calls=list(calls), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    cloned = {}

    def dfs(n):
        if n in cloned:
            rec('hit', cloned, val=n.val)
            return cloned[n]
        calls.append(n.val)
        clone = Node(n.val)
        cloned[n] = clone
        rec('make', cloned, val=n.val)
        for nb in n.neighbors:
            rec('try', cloned, val=n.val, nb=nb.val)
            clone.neighbors.append(dfs(nb))
            rec('link', cloned, val=n.val, nb=nb.val)
        calls.pop()
        rec('return', cloned, val=n.val)
        return clone

    rec('start', cloned)
    dfs(node)
    rec('done', cloned)
    return events


def words(e, first):
    k = e['kind']
    if k == 'start':
        return ("Copy every node and every edge, without ever touching the original nodes in the copy.",
                "The map remembers which copy belongs to which original.", KEY)
    if k == 'make':
        if first.get('make') == id(e):
            return (f"dfs({e['val']}): make copy {e['val']}' and put it in the map FIRST.",
                    "Only then visit the neighbours: any path that comes back here must find this copy.", KEY)
        return (f"dfs({e['val']}): new node. Make {e['val']}' and record {e['val']} → {e['val']}' before going on.", "", STEP)
    if k == 'try':
        return (f"Copy {e['val']}' needs neighbour {e['nb']}: ask dfs({e['nb']}) for its copy.", "", QUICK * 1.8)
    if k == 'hit':
        if first.get('hit') == id(e):
            return (f"{e['val']} is already in the map: return {e['val']}' straight away.",
                    "Without the map this would recurse around the cycle forever.", KEY)
        return (f"{e['val']} is already in the map: reuse {e['val']}'.", "", STEP)
    if k == 'link':
        return (f"Add the edge {e['val']}' → {e['nb']}' to the copy.", "", QUICK * 1.8)
    if k == 'return':
        return (f"Every neighbour of {e['val']} is linked, so dfs({e['val']}) returns {e['val']}'.", "", QUICK * 1.6)
    return (f"Done: {len(e['made'])} new nodes and {len(e['links']) // 2} edges, each node copied exactly once.",
            "Return 1', the copy of the node we were given.", END)


def main():
    args = cli()
    events = trace(build(ADJ))
    first = {}
    for e in events:
        for k in ('make', 'hit'):
            if e['kind'] == k and k not in first:
                first[k] = id(e)
    sc = Scene('#133 Clone Graph: DFS with an original → copy map',
               'adjList = [[2,4],[1,3],[2,4],[1,3]]: a 4-node cycle. Primes (1\') are the new nodes.')
    edges = sorted({tuple(sorted((i + 1, j))) for i, nb in enumerate(ADJ) for j in nb})
    legend = [(ACTIVE, 'being copied'), (style('good')[1], 'already copied'), (CURSOR, 'neighbour asked for')]
    for e in events:
        k = e['kind']
        made = {o for o, _ in e['made']}
        ostyles = {v: 'good' for v in made}
        rings = []
        if e['calls']:
            ostyles[e['calls'][-1]] = 'active'
        if k in ('try', 'link'):
            rings.append((e['nb'], CURSOR))
        if k == 'hit':
            rings.append((e['val'], ACTIVE))
        # one picture: the original on the left, the copy on the right
        pos = {v: (0.36 * x, y) for v, (x, y) in POS.items()}
        pos.update({f"{v}'": (0.64 + 0.36 * POS[v][0], POS[v][1]) for v in made})
        oedges = [(a, b) for a, nb in zip(range(1, len(ADJ) + 1), ADJ) for b in nb]
        cedges = [(f"{a}'", f"{b}'") for a, b in e['links']]
        estyles = {}
        if k == 'link':
            estyles[(f"{e['val']}'", f"{e['nb']}'")] = 'active'
        styles = dict(ostyles)
        styles.update({f"{v}'": 'active' if e['calls'] and v == e['calls'][-1] else 'good' for v in made})
        graph = GraphView(pos, oedges + cedges, directed=True, styles=styles, edge_styles=estyles,
                          rings=rings, height=262)
        stack = ' → '.join(f'dfs({v})' for v in e['calls']) or '(empty)'
        rows = [(f'{o}', f"{c}'", 'good') for o, c in e['made']]
        cap, sub, hold = words(e, first)
        sc.frame([TextView(['original (each arrow = one neighbour pointer)    copy being built'], size=14),
                  graph, TextView([f'call stack: {stack}'], size=15)], cap, sub, hold,
                 side=MapView(rows, 'Map: original → copy', headers=('original', 'copy'), empty='(empty)'),
                 counters={'copies': len(e['made'])}, legend=legend)
    finish(sc, 133, "Watch dfs(2) ask for node 1 again: 1' is already in the map, because it was registered "
                    "before its neighbours were visited, so the cycle closes instead of looping forever.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
