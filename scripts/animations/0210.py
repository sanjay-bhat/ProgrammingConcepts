#!/usr/bin/env python3
"""#210 Course Schedule II: write courses down in the order they become free.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
from collections import deque, defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

N_COURSES = 4
PREREQS = [[1, 0], [2, 0], [3, 1], [3, 2]]          # LeetCode example 2: the diamond
POS = {0: (0.0, 0.5), 1: (0.5, 0.05), 2: (0.5, 0.95), 3: (1.0, 0.5)}


def trace(numCourses, prerequisites):
    events = []
    st = {'done_edges': set()}

    def rec(kind, in_degree, queue, order, **kw):
        events.append(dict(kind=kind, deg=list(in_degree), queue=list(queue), order=list(order),
                           done_edges=set(st['done_edges']), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    adj = defaultdict(list)
    in_degree = [0] * numCourses
    rec('start', in_degree, [], [])

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1

    queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
    order = []
    rec('seed', in_degree, queue, order)

    while queue:
        node = queue.popleft()
        order.append(node)
        rec('pop', in_degree, queue, order, node=node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            st['done_edges'].add((node, neighbor))
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            rec('dec', in_degree, queue, order, node=node, nb=neighbor)

    result = order if len(order) == numCourses else []
    rec('done', in_degree, queue, order, result=result)
    return events


def words(e, seen):
    k = e['kind']
    if k == 'start':
        return ("Each pair [a, b] is an arrow b → a: take b before a.",
                "We want an order for all 4 courses that never breaks an arrow.", STEP)
    if k == 'seed':
        return ("Count each course's prerequisites. Course 3 needs two: 1 and 2.",
                "Only course 0 needs nothing, so it starts in the queue.", KEY)
    if k == 'pop':
        if not seen.get('pop'):
            seen['pop'] = True
            return (f"Take course {e['node']} and write it down: order = {e['order']}.",
                    "Every course it unlocks now has one prerequisite fewer.", KEY)
        return (f"Take course {e['node']} and write it down: order = {e['order']}.", "", STEP)
    if k == 'dec':
        d, nb = e['deg'][e['nb']], e['nb']
        if d == 0:
            return (f"Course {nb} drops to 0: everything it needs is written down, so it joins the queue.",
                    "", STEP)
        return (f"Course {nb} drops to {d}, not 0. It still needs course 2, so it waits.",
                "Writing 3 down now would put it before one of its prerequisites.", KEY)
    return (f"All {len(e['order'])} courses written down, so the order is valid: {e['result']}.",
            "LeetCode shows [0,2,1,3]; any order that respects every arrow is accepted.", END)


def main():
    args = cli()
    events = trace(N_COURSES, PREREQS)
    sc = Scene('#210 Course Schedule II: the order you take them in',
               'numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]. Arrow b → a: take b first.')
    edges = [(p, c) for c, p in PREREQS]
    legend = [(style('good')[1], 'written down'), (ACTIVE, 'just taken'), (CURSOR, 'count being lowered')]
    seen = {}
    for e in events:
        k = e['kind']
        styles = {v: 'good' for v in e['order']}
        if k in ('pop', 'dec'):
            styles[e['node']] = 'active'
        estyles = {ed: 'muted' for ed in e['done_edges']}
        rings = []
        if k == 'dec':
            estyles[(e['node'], e['nb'])] = 'active'
            rings.append((e['nb'], CURSOR))
        labels = {} if k == 'start' else {v: f'needs {d}' for v, d in enumerate(e['deg']) if v not in e['order']}
        graph = GraphView(POS, edges, directed=True, styles=styles, edge_styles=estyles,
                          labels=labels, rings=rings, height=205)
        q = QueueView([str(v) for v in e['queue']], 'Queue (courses at 0)')
        order = ArrayView([str(v) for v in e['order']] + [''] * (N_COURSES - len(e['order'])),
                          styles={i: 'good' for i in range(len(e['order']))}, title='order', cell=44, indices=False)
        rows = [] if k == 'start' else [(f'course {v}', str(d), 'good' if v in e['order'] else None)
                                         for v, d in enumerate(e['deg'])]
        cap, sub, hold = words(e, seen)
        sc.frame([graph, q, order], cap, sub, hold,
                 side=MapView(rows, 'Prerequisites left', headers=('course', 'in-degree')),
                 counters={'written': f"{len(e['order'])} / {N_COURSES}"}, legend=legend)
    finish(sc, 210, "Watch course 3 after course 1 is taken: its count drops to 1, not 0, so it waits "
                    "until course 2 is written down too, and only then joins the order.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
