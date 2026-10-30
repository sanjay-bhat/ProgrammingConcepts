#!/usr/bin/env python3
"""#104 Maximum Depth of Binary Tree: each node asks both children, keeps the bigger answer, adds 1.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [3, 9, 20, None, None, 15, 7]          # LeetCode example 1


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

    def rec(kind, **kw):
        events.append(dict(kind=kind, calls=[list(c) for c in calls], done=dict(done), **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def maxDepth(self, root) -> int:
            if calls:
                calls[-1][2] += 1                      # which child the waiting call is asking
            if not root:
                rec('null', parent=calls[-1][0], side='left' if calls[-1][2] == 1 else 'right')
                return 0
            calls.append([root.idx, None, 0])
            rec('call', node=root.idx)
            ans = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            calls[-1][1] = ans
            done[root.idx] = ans
            rec('return', node=root.idx, ans=ans,
                kids=[done.get(c.idx, 0) if c else 0 for c in (root.left, root.right)])
            calls.pop()
            return ans

    rec('start')
    answer = Solution().maxDepth(build(level))
    rec('done', ans=answer)
    return events


def words(e, level):
    k = e['kind']
    v = lambda i: level[i]
    if k == 'start':
        return ("Depth of a node = 1 + the deeper of its two subtrees. An empty spot is 0.",
                "Each node asks both children before it can answer.", KEY)
    if k == 'call':
        return (f"maxDepth({v(e['node'])}): ask the left child first, then the right.",
                "This call waits on the stack until both answers come back.", STEP)
    if k == 'null':
        p = v(e['parent'])
        return (f"{p}'s {e['side']} child is empty, so it answers 0 straight away.", "", QUICK)
    if k == 'return':
        a, b = e['kids']
        n = v(e['node'])
        if a == 0 and b == 0:
            hold = KEY if e['node'] == 1 else STEP
            return (f"{n} is a leaf: 1 + max(0, 0) = 1.",
                    "Empty is 0, so a leaf comes out as 1. Returning 1 for empty would make it 2.", hold)
        if a != b:
            return (f"{n} heard {a} from the left and {b} from the right: 1 + max({a}, {b}) = {e['ans']}.",
                    "Keep the deeper side, add 1 for this node. Following just one path could miss it.", KEY)
        return (f"{n} heard {a} from both sides: 1 + max({a}, {b}) = {e['ans']}.",
                "Its answer goes back up to the call waiting for it.", STEP)
    return (f"The root has answered. Maximum depth = {e['ans']}.",
            "Every node was asked once: O(n) time, and the stack was never taller than the tree.", END)


def main():
    args = cli()
    sc = Scene('#104 Maximum Depth: ask both sides, keep the bigger',
               'Each node shows the depth it returned once it knows it.')
    legend = [(ACTIVE, 'current call'), (style('window')[1], 'waiting on the stack'),
              (style('good')[1], 'answered')]
    kids = TreeView.structure(LEVEL)
    parent = {c: p for p, cs in kids.items() for c in cs if c is not None}
    for e in trace(LEVEL):
        waiting = [c[0] for c in e['calls']]
        styles = {i: 'good' for i in e['done']}
        styles.update({i: 'window' for i in waiting})
        rings = []
        cur = e.get('node') if e['kind'] in ('call', 'return') else (e.get('parent') if e['kind'] == 'null' else None)
        if e['kind'] == 'return':
            styles[e['node']] = 'good'
        if cur is not None:
            rings.append((cur, ACTIVE))
            if e['kind'] == 'call':
                styles[cur] = 'active'
        edges = {(parent[i], i): 'active' for i in waiting if i in parent}
        labels = {i: f'depth {d}' for i, d in e['done'].items()}
        stack = []
        for i, ans, _ in e['calls']:
            stack.append((f'maxDepth({LEVEL[i]})' + ('' if ans is None else f'  = {ans}'),
                          'good' if ans is not None else None))
        if e['kind'] == 'null':
            stack.append(('maxDepth(empty)  = 0', 'muted'))
        cap, sub, hold = words(e, LEVEL)
        sc.frame(TreeView(LEVEL, styles=styles, labels=labels, edges=edges, rings=rings),
                 cap, sub, hold,
                 side=StackView(stack, 'Call stack', base='caller', empty='(empty)'),
                 counters={'answer': e['ans'] if e['kind'] == 'done' else '?'}, legend=legend)
    finish(sc, 104, "Watch node 20: it hears 1 from each side, and then the root hears 1 and 2 and "
                    "keeps the 2. Asking both sides is the whole trick.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
