#!/usr/bin/env python3
"""#543 Diameter of Binary Tree: each call records left + right, but returns 1 + max(left, right).

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [1, 2, 3, 4, 5]          # LeetCode example 1


class TreeNode:
    def __init__(self, val, idx):
        self.val, self.idx, self.left, self.right = val, idx, None, None


def build(level):
    kids = TreeView.structure(level)
    nodes = {i: TreeNode(level[i], i) for i in kids}
    for i, (l, r) in kids.items():
        nodes[i].left, nodes[i].right = nodes.get(l), nodes.get(r)
    return nodes[0]


def trace(level):
    events, calls, done = [], [], {}
    best = {'d': 0, 'at': None}

    def rec(kind, **kw):
        events.append(dict(kind=kind, calls=[list(c) for c in calls], done=dict(done),
                           best=best['d'], best_at=best['at'], **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def diameter_of_binary_tree(root) -> int:
        diameter = 0

        def depth(node) -> int:
            nonlocal diameter
            if calls:
                calls[-1][2] += 1
            if not node:
                rec('null', parent=calls[-1][0], side='left' if calls[-1][2] == 1 else 'right')
                return 0
            calls.append([node.idx, None, 0])
            rec('call', node=node.idx)
            l, r = depth(node.left), depth(node.right)
            old = diameter
            diameter = max(diameter, l + r)
            if diameter > old:
                best['d'], best['at'] = diameter, node.idx
            calls[-1][1] = max(l, r) + 1
            done[node.idx] = (max(l, r) + 1, l + r)
            rec('return', node=node.idx, l=l, r=r, ans=max(l, r) + 1, improved=diameter > old)
            calls.pop()
            return max(l, r) + 1

        depth(root)
        return diameter

    rec('start')
    answer = diameter_of_binary_tree(build(level))
    rec('done', ans=answer)
    return events


def words(e, level):
    k = e['kind']
    v = lambda i: level[i]
    if k == 'start':
        return ("At every node: record left + right as a path, return 1 + max(left, right) as a height.",
                "Children answer first, so each node has both heights when it decides.", KEY)
    if k == 'call':
        return (f"depth({v(e['node'])}): ask the left child, then the right.",
                "This call waits on the stack until both heights come back.", STEP)
    if k == 'null':
        return (f"{v(e['parent'])}'s {e['side']} child is empty: height 0.", "", QUICK)
    if k == 'return':
        n, l, r, a = v(e['node']), e['l'], e['r'], e['ans']
        if l == 0 and r == 0:
            return (f"Leaf {n}: path here is 0 + 0 = 0 edges, but it returns height 1.",
                    "Two different numbers: the path is recorded, the height goes up.",
                    KEY if e['node'] == 3 else QUICK * 2)
        if e['node'] == 0:
            return (f"Root {n}: heights {l} and {r}, so the path bending here is {l} + {r} = {l + r} edges.",
                    f"That beats the best so far. It returns height {a}, which nobody needs any more.", KEY)
        return (f"Node {n}: heights {l} and {r}. Path bending here: {l} + {r} = {l + r}. Best is now {e['best']}.",
                f"But it returns 1 + max({l}, {r}) = {a}: the parent can only extend one arm.", KEY)
    return (f"Done. Diameter = {e['ans']} edges: 4 - 2 - 1 - 3.",
            "Every node was a possible bend point, and each was checked once: O(n).", END)


def main():
    args = cli()
    sc = Scene('#543 Diameter: record left + right, return the taller arm',
               'Under each node: h = height it returns, path = left + right recorded there.')
    legend = [(ACTIVE, 'current call'), (style('window')[1], 'waiting on the stack'),
              (style('good')[1], 'answered'), (style('gold')[1], 'best path so far bends here')]
    kids = TreeView.structure(LEVEL)
    parent = {c: p for p, cs in kids.items() for c in cs if c is not None}
    for e in trace(LEVEL):
        waiting = [c[0] for c in e['calls']]
        styles = {i: 'good' for i in e['done']}
        styles.update({i: 'window' for i in waiting})
        if e['best_at'] is not None:
            styles[e['best_at']] = 'gold'
        rings = []
        cur = e.get('node') if e['kind'] in ('call', 'return') else (e.get('parent') if e['kind'] == 'null' else None)
        if cur is not None:
            rings.append((cur, ACTIVE))
            if e['kind'] == 'call':
                styles[cur] = 'active'
        edges = {(parent[i], i): 'active' for i in waiting if i in parent}
        if e['kind'] == 'done':
            edges = {(1, 3): 'good', (0, 1): 'good', (0, 2): 'good'}
        labels = {i: f'h {h}, path {p}' for i, (h, p) in e['done'].items()}
        stack = [(f'depth({LEVEL[i]})' + ('' if a is None else f'  returns {a}'),
                  'good' if a is not None else None) for i, a, _ in e['calls']]
        if e['kind'] == 'null':
            stack.append(('depth(empty)  returns 0', 'muted'))
        cap, sub, hold = words(e, LEVEL)
        sc.frame(TreeView(LEVEL, styles=styles, labels=labels, edges=edges, rings=rings),
                 cap, sub, hold,
                 side=StackView(stack, 'Call stack', base='diameter_of_binary_tree', empty='(empty)'),
                 counters={'diameter': e['best']}, legend=legend)
    finish(sc, 543, "Watch node 2: it records a path of 1 + 1 = 2 but hands its parent only 2, "
                    "the height of its taller arm. Those two numbers are the whole problem.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
