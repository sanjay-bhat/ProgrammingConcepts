#!/usr/bin/env python3
"""#207 Course Schedule: take whatever is free; courses in a loop never get free.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
from collections import deque, defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

# A diamond (0 -> 1, 2 -> 3) whose last course is also part of the loop 3 -> 4 -> 5 -> 3.
N_COURSES = 6
PREREQS = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4], [3, 5]]
POS = {0: (0.0, 0.5), 1: (0.3, 0.05), 2: (0.3, 0.95), 3: (0.58, 0.5), 4: (1.0, 0.05), 5: (1.0, 0.95)}


def trace(numCourses, prerequisites):
    events = []
    st = {'taken': [], 'done_edges': set()}

    def rec(kind, in_degree, queue, count, **kw):
        events.append(dict(kind=kind, deg=list(in_degree), queue=list(queue), count=count,
                           taken=list(st['taken']), done_edges=set(st['done_edges']), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    adj = defaultdict(list)
    in_degree = [0] * numCourses
    rec('start', in_degree, [], 0)

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1

    queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
    count = 0
    rec('seed', in_degree, queue, count)

    while queue:
        node = queue.popleft()
        count += 1
        st['taken'].append(node)
        rec('pop', in_degree, queue, count, node=node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            st['done_edges'].add((node, neighbor))
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            rec('dec', in_degree, queue, count, node=node, nb=neighbor)

    rec('done', in_degree, queue, count, answer=count == numCourses)
    return events


def words(e, seen):
    k = e['kind']
    if k == 'start':
        return ("Each pair [a, b] is an arrow b → a: take b before a.",
                "Can all 6 courses be taken? Only a loop of arrows can stop us.", STEP)
    if k == 'seed':
        return ("Count each course's prerequisites (its in-degree). Only course 0 is at 0.",
                "Courses at 0 can be taken right now, so they start in the queue.", KEY)
    if k == 'pop':
        if not seen.get('pop'):
            seen['pop'] = True
            return (f"Take course {e['node']} from the queue. Taken so far: {e['count']}.",
                    "Every course it unlocks now has one prerequisite fewer.", KEY)
        return (f"Take course {e['node']}. Taken so far: {e['count']}.", "", STEP)
    if k == 'dec':
        d, nb = e['deg'][e['nb']], e['nb']
        if d == 0:
            return (f"Course {nb} drops to 0: its last prerequisite is done, so it joins the queue.",
                    "", STEP)
        if nb == 3 and d == 1:
            return (f"Course 3 drops to 1, not 0. It's still waiting on course 5.",
                    "But 5 waits on 4, and 4 waits on 3: none of them can ever be first.", KEY)
        return (f"Course {nb} drops to {d}: still waiting, so it stays out of the queue.",
                "Joining on every decrement would take it more than once.", STEP)
    stuck = [v for v in range(N_COURSES) if v not in e['taken']]
    return (f"Queue empty after {e['count']} of {N_COURSES} courses. Answer: false.",
            f"Courses {', '.join(map(str, stuck))} never reached 0: they're the loop. We never had to search for it.",
            END)


def main():
    args = cli()
    events = trace(N_COURSES, PREREQS)
    sc = Scene('#207 Course Schedule: take whatever is free',
               'numCourses = 6, prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,3],[5,4],[3,5]]. Arrow b → a: take b first.')
    edges = [(p, c) for c, p in PREREQS]
    legend = [(style('good')[1], 'taken'), (ACTIVE, 'just taken'), (style('bad')[1], 'stuck in the loop')]
    seen = {}
    for e in events:
        k = e['kind']
        styles = {v: 'good' for v in e['taken']}
        if k in ('pop', 'dec'):
            styles[e['node']] = 'active'
        if k == 'done':
            styles.update({v: 'bad' for v in range(N_COURSES) if v not in e['taken']})
        estyles = {ed: 'muted' for ed in e['done_edges']}
        rings = []
        if k == 'dec':
            estyles[(e['node'], e['nb'])] = 'active'
            rings.append((e['nb'], CURSOR))
        labels = {} if k == 'start' else {v: f'needs {d}' for v, d in enumerate(e['deg']) if v not in e['taken']}
        graph = GraphView(POS, edges, directed=True, styles=styles, edge_styles=estyles,
                          labels=labels, rings=rings, height=300)
        q = QueueView([str(v) for v in e['queue']], 'Queue (courses at 0)')
        rows = [] if k == 'start' else [(f'course {v}', str(d), 'good' if v in e['taken'] else ('bad' if k == 'done' else None))
                for v, d in enumerate(e['deg'])]
        cap, sub, hold = words(e, seen)
        sc.frame([graph, q], cap, sub, hold,
                 side=MapView(rows, 'Prerequisites left', headers=('course', 'in-degree')),
                 counters={'taken': f"{e['count']} / {N_COURSES}"}, legend=legend)
    finish(sc, 207, "Watch course 3 drop to 1 instead of 0: its last prerequisite is course 5, which is "
                    "waiting on 3 itself, so the loop never gets free and the count stops at 3 of 6.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
