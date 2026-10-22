#!/usr/bin/env python3
"""#235 LCA of a BST: walk down while both targets go the same way; the first split is the answer.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. p = 3, q = 5 on LeetCode's example
tree, because that pair makes the walk turn both left and right before it splits.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]      # LeetCode example tree
P, Q = 3, 5


class TreeNode:
    def __init__(self, x, idx):
        self.val, self.idx, self.left, self.right = x, idx, None, None


def build(level):
    kids = TreeView.structure(level)
    nodes = {i: TreeNode(level[i], i) for i in kids}
    for i, (l, r) in kids.items():
        nodes[i].left, nodes[i].right = nodes.get(l), nodes.get(r)
    return nodes[0], nodes


def trace():
    root, nodes = build(LEVEL)
    p = next(n for n in nodes.values() if n.val == P)
    q = next(n for n in nodes.values() if n.val == Q)
    events, path, decided = [], [], []

    def rec(kind, node=None, **kw):
        if kind in ('left', 'right', 'split'):
            decided.append((node.idx, kind))
        events.append(dict(kind=kind, node=node.idx if node else None, path=list(path),
                           decided=list(decided), **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def lowestCommonAncestor(self, root, p, q):
            node = root
            while node:
                path.append(node.idx)
                if p.val < node.val and q.val < node.val:
                    rec('left', node)
                    node = node.left
                elif p.val > node.val and q.val > node.val:
                    rec('right', node)
                    node = node.right
                else:
                    rec('split', node)
                    return node
            return None

    rec('start')
    ans = Solution().lowestCommonAncestor(root, p, q)
    rec('done', ans, ans=ans.val)
    return events


def words(e):
    k = e['kind']
    v = LEVEL[e['node']] if e['node'] is not None else None
    if k == 'start':
        return (f"Find the lowest node with both {P} and {Q} underneath it. Start at the root.",
                "In a BST, comparing values tells you which side each target is on.", STEP)
    if k == 'left':
        return (f"At {v}: {P} and {Q} are both smaller, so both are in the left subtree. Go left.",
                f"{v} is a common ancestor, but a lower one is still below it.", KEY)
    if k == 'right':
        return (f"At {v}: {P} and {Q} are both larger, so both are in the right subtree. Go right.",
                "Same reasoning: they haven't parted yet.", STEP)
    if k == 'split':
        return (f"At {v}: {P} is smaller and {Q} is larger. They split here.",
                f"Going lower on either side would lose one of them, so {v} is the lowest.", KEY)
    return (f"Answer: {e['ans']}. Three nodes visited, one pointer, no stack.",
            "The walk only goes down one path: O(h) time, O(1) memory.", END)


def main():
    args = cli()
    sc = Scene(f'#235 LCA of a BST: follow p = {P} and q = {Q} until they split',
               'Top: the values in sorted order. Bottom: the tree. One pointer walks down.')
    legend = [(ACTIVE, 'current node'), (style('gold')[1], 'already passed'),
              (style('window')[1], 'targets'), (style('good')[1], 'split point')]
    kids = TreeView.structure(LEVEL)
    parent = {c: p for p, cs in kids.items() for c in cs if c is not None}
    order = sorted(LEVEL[i] for i in kids)
    for e in trace():
        styles = {i: 'window' for i in kids if LEVEL[i] in (P, Q)}
        styles.update({i: 'gold' for i in e['path'][:-1]})
        rings = []
        cur = e['node']
        if cur is not None:
            styles[cur] = 'good' if e['kind'] in ('split', 'done') else 'active'
            rings = [(cur, ACTIVE)] if e['kind'] != 'done' else []
        edges = {(parent[i], i): 'gold' for i in e['path'] if i in parent}
        astyles = {order.index(P): 'window', order.index(Q): 'window'}
        ptr = {'p': order.index(P), 'q': order.index(Q)}
        if cur is not None:
            astyles[order.index(LEVEL[cur])] = 'good' if e['kind'] in ('split', 'done') else 'active'
            ptr['node'] = order.index(LEVEL[cur])
        said = {'left': 'both smaller: left', 'right': 'both larger: right', 'split': 'split: answer'}
        rows = [(str(LEVEL[i]), said[k]) + (('good',) if k == 'split' else ()) for i, k in e['decided']]
        cap, sub, hold = words(e)
        sc.frame([ArrayView(order, styles=astyles, pointers=ptr, title='sorted', indices=False),
                  TreeView(LEVEL, styles=styles, edges=edges, rings=rings)],
                 cap, sub, hold,
                 side=MapView(rows, 'Decisions', headers=('node', f'p={P}, q={Q} are...'), empty='(none yet)'),
                 counters={'answer': e.get('ans', '?')}, legend=legend)
    finish(sc, 235, f"Watch the pointer stop at 4: {P} is on its left and {Q} on its right, so no lower "
                    "node can hold both. The first split on the way down is the answer.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
