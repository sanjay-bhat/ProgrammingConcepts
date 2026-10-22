#!/usr/bin/env python3
"""#124 Binary Tree Maximum Path Sum: each node records the path that bends at it,
and passes only one side up to its parent.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The tree is LeetCode's example 2,
where the best path (15-20-7) never touches the root.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [-10, 9, 20, None, None, 15, 7]   # LeetCode example 2


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
    events, calls, up = [], [], {}
    st = {'best': None}

    def rec(kind, **kw):
        events.append(dict(kind=kind, calls=[list(c) for c in calls], up=dict(up), best=st['best'], **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def maxPathSum(self, root) -> int:
            self.ans = float('-inf')

            def dfs(node):
                if not node:
                    rec('null', parent=calls[-1][0])
                    return 0
                calls.append([node.idx, None, None])
                rec('enter', node=node.idx)
                left = max(0, dfs(node.left))
                calls[-1][1] = left
                right = max(0, dfs(node.right))
                calls[-1][2] = right
                old = self.ans
                self.ans = max(self.ans, node.val + left + right)
                st['best'] = self.ans
                rec('bend', node=node.idx, left=left, right=right, bend=node.val + left + right,
                    improved=self.ans != old, old=old)
                up[node.idx] = node.val + max(left, right)
                rec('return', node=node.idx, left=left, right=right, ret=up[node.idx])
                calls.pop()
                return node.val + max(left, right)
            dfs(root)
            return self.ans

    rec('start')
    ans = Solution().maxPathSum(build(level))
    rec('done', ans=ans)
    return events


def words(e):
    k = e['kind']
    v = LEVEL[e['node']] if 'node' in e else None
    if k == 'start':
        return ("Each node answers two questions: the best path that bends here,",
                "and the best path that keeps going up to its parent, which can only use one side.", STEP)
    if k == 'enter':
        return (f"dfs({v}): ask both children first. It can't answer until they do.", "", QUICK * 2)
    if k == 'null':
        return (f"An empty child of {LEVEL[e['parent']]} adds nothing: return 0.", "", QUICK)
    if k == 'bend':
        L, R, b = e['left'], e['right'], e['bend']
        if v == 20:
            return (f"Bend at 20: {L} + 20 + {R} = {b}. That beats {e['old']}, so best = {b}.",
                    "This path uses both sides of 20. It's recorded, but it will never be passed up.", KEY)
        if v == -10:
            return (f"Bend at the root: {L} + (-10) + {R} = {b}. That's less than 42, so best stays 42.",
                    "The best path never has to touch the root.", KEY)
        if e['improved']:
            extra = "A side that summed to less than 0 would be counted as 0: stop instead." if v == 9 else ""
            return (f"Bend at {v}: {L} + {v} + {R} = {b}. New best = {b}.", extra, STEP)
        return (f"Bend at {v}: {L} + {v} + {R} = {b}. Not better than {e['best']}.", "", STEP)
    if k == 'return':
        L, R, r = e['left'], e['right'], e['ret']
        if v == 20:
            return (f"20 passes up 20 + max(15, 7) = {r}, not 42.",
                    "Its parent will extend this path, and a path that used both sides would fork.", KEY)
        if v == -10:
            return (f"The root returns {r}, but nobody is waiting for it.", "", STEP)
        return (f"{v} passes up {v} + max({L}, {R}) = {r}.", "", STEP)
    return (f"maxPathSum returns {e['ans']}: the path 15 - 20 - 7.",
            "Each node was visited once and did a few additions: O(n).", END)


def main():
    args = cli()
    sc = Scene('#124 Max Path Sum: bend here, or pass one side up',
               'Tag under a node: what it passed up to its parent. Green: where the best path bends.')
    legend = [(ACTIVE, 'current call'), (style('window')[1], 'waiting for children'),
              (style('good')[1], 'best bend so far'), (style('muted')[1], 'finished')]
    kids = TreeView.structure(LEVEL)
    parent = {c: p for p, cs in kids.items() for c in cs if c is not None}
    best_node = None
    for e in trace(LEVEL):
        if e['kind'] == 'bend' and e['improved']:
            best_node = e['node']
        styles = {i: 'muted' for i in e['up']}
        waiting = [c[0] for c in e['calls']]
        for i in waiting:
            styles[i] = 'window'
        if best_node is not None:
            styles[best_node] = 'good'
        cur = e.get('node', e.get('parent'))
        rings = [(cur, ACTIVE)] if cur is not None and e['kind'] != 'done' else []
        edges = {(parent[i], i): 'active' for i in waiting if i in parent}
        if e['kind'] in ('bend', 'done') or (e['kind'] == 'return' and best_node is not None):
            if best_node is not None:
                for c in kids[best_node]:
                    if c is not None and e['up'].get(c, 0) > 0:
                        edges[(best_node, c)] = 'good'
        labels = {i: f'up {r}' for i, r in e['up'].items()}
        if e['kind'] == 'bend':
            labels[e['node']] = f'bend {e["bend"]}'
        stack = []
        for i, L, R in e['calls']:
            s = f'dfs({LEVEL[i]})'
            if L is not None:
                s += f'  left={L}'
            if R is not None:
                s += f' right={R}'
            stack.append(s)
        if e['kind'] == 'null':
            stack.append(('dfs(empty) = 0', 'muted'))
        cap, sub, hold = words(e)
        best = '-∞' if e['best'] is None else e['best']
        sc.frame(TreeView(LEVEL, styles=styles, labels=labels, edges=edges, rings=rings),
                 cap, sub, hold, side=StackView(stack, 'Call stack', base='maxPathSum'),
                 counters={'best': best}, legend=legend)
    finish(sc, 124, "Watch node 20: it records the bent path 15 + 20 + 7 = 42 as the best, "
                    "but passes only 35 up, because its parent can extend just one side.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
