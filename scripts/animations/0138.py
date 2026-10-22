#!/usr/bin/env python3
"""#138 Copy List with Random Pointer: make every copy, then wire through the map.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Both rows are drawn from the real
next/random pointers of the original nodes and of the copies.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

PAIRS = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]     # LeetCode example 1


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


def trace(pairs):
    orig = [Node(v) for v, _ in pairs]
    for a, b in zip(orig, orig[1:]):
        a.next = b
    for nd, (_, r) in zip(orig, pairs):
        nd.random = orig[r] if r is not None else None
    oid = {id(n): i for i, n in enumerate(orig)}
    events = []

    def rec(kind, node_map, cur=None):
        cid = {id(c): oid[id(o)] for o, c in ((o, node_map[o]) for o in orig if o in node_map)}
        copies = {oid[id(o)]: c for o, c in node_map.items()}
        events.append(dict(
            kind=kind, cur=oid[id(cur)] if cur else None,
            made=sorted(copies),
            cnext={i: cid.get(id(c.next)) if c.next else None for i, c in copies.items()},
            crand={i: cid.get(id(c.random)) if c.random else None for i, c in copies.items()},
            stray=any(c.random is not None and id(c.random) in oid for c in copies.values())))

    # ---- the notebook's solution, with rec() calls added ----
    def copyRandomList(head):
        if not head: return None
        node_map = {}
        cur = head
        rec('start', node_map)
        while cur:
            node_map[cur] = Node(cur.val)
            rec('make', node_map, cur)
            cur = cur.next
        cur = head
        while cur:
            if cur.next: node_map[cur].next = node_map[cur.next]
            if cur.random: node_map[cur].random = node_map[cur.random]
            rec('wire', node_map, cur)
            cur = cur.next
        rec('done', node_map)
        return node_map[head]

    copyRandomList(orig[0])
    return events


def words(e, first_make, first_rand):
    k, c = e['kind'], e['cur']
    V = [v for v, _ in PAIRS]
    if k == 'start':
        return ("Copy this list: values, next arrows, and the purple random arrows.",
                "Every arrow in the copy must point at a COPY, never back into the original.", KEY)
    if k == 'make':
        if e is first_make:
            return (f"Pass 1: make a bare copy of {V[c]} and write 'node {c} -> copy {c}' in the map.",
                    "No arrows yet. A random can point forward, so every copy must exist before wiring.", KEY)
        return (f"Pass 1: copy {V[c]}, record node {c} -> copy {c}.", "", QUICK * 1.6)
    if k == 'wire':
        r = PAIRS[c][1]
        if r is None:
            return (f"Pass 2 at {V[c]}: next goes through the map. Its random is null, so skip it.", "", STEP)
        if e is first_rand:
            return (f"{V[c]}'s random is node {r}. The map turns that into copy {r}.",
                    f"Writing copy.random = cur.random would point at the ORIGINAL {V[r]} instead.", KEY)
        if r > c:
            return (f"{V[c]}'s random points FORWARD to node {r}. Its copy already exists from pass 1.",
                    "That's why it takes two passes.", KEY)
        return (f"{V[c]}: next and random both translated through the map (random -> copy {r}).", "", STEP)
    return ("Done. Same values, same arrows, and not one of them points into the original.",
            "Two passes, one map entry per node: O(n) time, O(n) extra space.", END)


def main():
    args = cli()
    events = trace(PAIRS)
    first_make = next(e for e in events if e['kind'] == 'make')
    first_rand = next(e for e in events if e['kind'] == 'wire' and PAIRS[e['cur']][1] is not None)
    V = [v for v, _ in PAIRS]
    n = len(PAIRS)
    sc = Scene('#138 Copy List with Random Pointer',
               'Top row: the original. Bottom row: the copy. Black arrows are next, purple arcs are random.')
    legend = [(style('window')[1], 'original'), (style('good')[1], 'copy'),
              (ListView.EXTRA, 'random pointer'), (ACTIVE, 'cur')]
    orig_extra = [(i, r) for i, (_, r) in enumerate(PAIRS) if r is not None]
    for e in events:
        c = e['cur']
        ostyles = {i: 'window' for i in range(n)}
        if c is not None:
            ostyles[c] = 'active'
        top = ListView(V, None, ostyles, {'cur': c} if c is not None else {}, extra=orig_extra)
        made = e['made']
        labels = [f"{v}'" if i in made else '' for i, v in enumerate(V)]
        cstyles = {i: ('good' if i in made else 'muted') for i in range(n)}
        if c is not None and e['kind'] == 'wire':
            cstyles[c] = 'active'
        nxt = [e['cnext'].get(i) for i in range(n)]
        cextra = [(i, r) for i, r in e['crand'].items() if r is not None]
        bottom = ListView(labels, nxt, cstyles, null=e['kind'] == 'done', extra=cextra)
        rows = [(f'node {i} ({V[i]})', f"copy {i} ({V[i]}')", 'good' if i == c else None) for i in made]
        rows = [r if r[2] else r[:2] for r in rows]
        cap, sub, hold = words(e, first_make, first_rand)
        sc.frame([top, bottom], cap, sub, hold,
                 side=MapView(rows, 'The map', headers=('original', 'its copy'), empty='(empty)'),
                 counters={'copies': len(made)}, legend=legend)
    finish(sc, 138, "Watch pass 2 reach 11: its random points forward to the last node, and it works only "
                    "because pass 1 already made every copy and wrote it in the map.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
