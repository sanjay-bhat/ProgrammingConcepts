#!/usr/bin/env python3
"""#684 Redundant Connection: the first edge whose two ends already share a root.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

EDGES = [[1, 2], [3, 4], [2, 3], [1, 4]]     # scenario 5: both ends of [2,3] are seen, in different groups
POS = {1: (0.1, 0.1), 2: (0.9, 0.1), 3: (0.9, 0.9), 4: (0.1, 0.9)}


def trace(edges):
    events, seen = [], set()
    st = {'path': []}

    def rec(kind, parent, rank, **kw):
        events.append(dict(kind=kind, parent=list(parent), rank=list(rank), seen=set(seen), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    parent = list(range(len(edges) + 1))
    rank = [0] * (len(edges) + 1)
    rec('start', parent, rank)

    def find(x):
        st['path'].append(x)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        before = list(parent)
        st['path'] = []
        px = find(x)
        path_x = st['path']; st['path'] = []
        py = find(y)
        path_y = st['path']
        rec('find', parent, rank, edge=(x, y), px=px, py=py, path_x=path_x, path_y=path_y,
            compressed=[v for v in range(1, len(parent)) if parent[v] != before[v]])
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        rec('union', parent, rank, edge=(x, y), child=py, root=px)
        return True

    for u, v in edges:
        rec('edge', parent, rank, edge=(u, v))
        if not union(u, v):
            rec('done', parent, rank, edge=(u, v), answer=[u, v])
            return events
        seen.update((u, v))
    return events


def root(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x


class Panel(View):
    """A titled panel around another view (the input graph in the side area)."""

    def __init__(self, title, inner, note=''):
        self.title, self.inner, self.note = title, inner, note

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        p.box(box, PANEL, PANEL_BORDER, 2, 12)
        p.text((x0 + 16, y0 + 14), self.title, 'bold', 18)
        if self.note:
            p.text((x0 + 16, y0 + 40), self.note, 'sans', 13, MUTED)
        self.inner.draw(p, (x0 + 24, y0 + 70, x1 - 24, y1 - 30))
        self.used = y1 - y0


def chain(path):
    return ' → '.join(map(str, path))


def words(e):
    k = e['kind']
    if k == 'start':
        return ("Every node starts as its own group: parent[x] = x, so each one is a root.",
                "Add the edges in order. Before each, ask: are the two ends already connected?", STEP)
    u, v = e['edge']
    if k == 'edge':
        return (f"Next edge [{u},{v}]. Find the root of each end.", "", QUICK * 1.6)
    if k == 'find':
        same = e['px'] == e['py']
        walk = f"find({u}): {chain(e['path_x'])}.   find({v}): {chain(e['path_y'])}."
        if same and e['compressed']:
            c = e['compressed'][0]
            return (f"{walk} Same root! (find also pointed {c} straight at {e['parent'][c]}.)",
                    f"{u} and {v} were already connected, so [{u},{v}] closes the loop.", KEY)
        if same:
            return (f"{walk} Same root!",
                    f"{u} and {v} were already connected, so [{u},{v}] closes the loop.", KEY)
        if u in e['seen'] and v in e['seen']:
            return (f"{walk} Different roots.",
                    f"Both {u} and {v} were seen before, but in separate groups: this edge is fine.", KEY)
        return (f"{walk} Different roots, so they aren't connected yet.", "", STEP)
    if k == 'union':
        return (f"Join the ROOTS: parent[{e['child']}] = {e['root']}. One group now.",
                "Moving the root moves its whole group along with it.", STEP)
    return (f"Answer: [{u},{v}]. It's the last edge of the loop 1-2-3-4-1 in the input.",
            "Every other loop edge had to be added first for the loop to close.", END)


def main():
    args = cli()
    events = trace(EDGES)
    n = len(EDGES)
    sc = Scene('#684 Redundant Connection: union-find',
               'edges = [[1,2],[3,4],[2,3],[1,4]]. Right: the input graph. Left: the parent pointers.')
    legend = [(ACTIVE, 'edge being checked'), (style('good')[1], 'edge added'), (CURSOR, 'root')]
    for e in events:
        k, parent = e['kind'], e['parent']
        roots = sorted({root(parent, v) for v in range(1, n + 1)})
        colour = {v: f'region{roots.index(root(parent, v))}' for v in range(1, n + 1)}
        # forest: roots on top, children below, grouped by root
        depth = {}
        for v in range(1, n + 1):
            d, x = 0, v
            while parent[x] != x:
                x, d = parent[x], d + 1
            depth[v] = d
        maxd = max(depth.values())
        order = sorted(range(1, n + 1), key=lambda v: (roots.index(root(parent, v)), depth[v], v))
        levels = {}
        for v in order:
            levels.setdefault(depth[v], []).append(v)
        fpos = {}
        for d, vs in levels.items():
            for i, v in enumerate(vs):
                fpos[('f', v)] = ((i + 0.5) / len(vs), d / 2)
        fedges = [(('f', v), ('f', parent[v])) for v in range(1, n + 1) if parent[v] != v]
        fstyles = {('f', v): colour[v] for v in range(1, n + 1)}
        frings = [(('f', r), CURSOR) for r in roots]
        festyles = {}
        if k == 'union':
            festyles[(('f', e['child']), ('f', e['root']))] = 'active'
        if k == 'find':
            for v in e['compressed']:
                festyles[(('f', v), ('f', parent[v]))] = 'active'
        forest = GraphView(fpos, fedges, directed=True, styles=fstyles, edge_styles=festyles, rings=frings,
                           names={('f', v): v for v in range(1, n + 1)}, height=200)
        arr = ArrayView([parent[v] for v in range(1, n + 1)], title='parent',
                        styles={v - 1: colour[v] for v in range(1, n + 1)},
                        subs={v - 1: f'of {v}' for v in range(1, n + 1)}, cell=50, indices=False)
        rk = ArrayView([e['rank'][v] for v in range(1, n + 1)], title='rank  ',
                       styles={v - 1: ('plain' if v in roots else 'muted') for v in range(1, n + 1)},
                       subs={v - 1: f'of {v}' for v in range(1, n + 1)}, cell=50, indices=False)
        # input graph: edges added so far, the current one highlighted
        cur = tuple(e['edge']) if 'edge' in e else None
        done_idx = [i for i, ed in enumerate(EDGES) if ed[0] in e['seen'] and ed[1] in e['seen']]
        estyles = {}
        added = 0
        for ed in EDGES:
            if tuple(ed) == cur:
                break
            estyles[tuple(ed)] = 'good'
            added += 1
        if k == 'start':
            estyles = {}
        if cur:
            estyles[cur] = 'bad' if k == 'done' else 'active'
        graph = GraphView(POS, [tuple(ed) for ed in EDGES], styles=colour, edge_styles=estyles)
        cap, sub, hold = words(e)
        sc.frame([forest, arr, rk], cap, sub, hold,
                 side=Panel('Input graph', graph, 'colour = group (same root)'),
                 counters={'groups': len(roots)}, legend=legend)
    finish(sc, 684, "Watch edge [2,3]: both nodes were seen before, but their roots differ, so the edge is kept; "
                    "only [1,4] finds the same root at both ends and closes the loop.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
