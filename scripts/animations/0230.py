#!/usr/bin/env python3
"""#230 Kth Smallest in a BST: hand-written inorder walk with a stack, stopping at the k-th pop.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. LeetCode's example-1 tree with k = 3,
so the walk has to step into node 1's right subtree to find 2 before 3.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [3, 1, 4, None, 2]          # LeetCode example 1's tree
K = 3


class TreeNode:
    def __init__(self, val, idx):
        self.val, self.idx, self.left, self.right = val, idx, None, None


def build(level):
    kids = TreeView.structure(level)
    nodes = {i: TreeNode(level[i], i) for i in kids}
    for i, (l, r) in kids.items():
        nodes[i].left, nodes[i].right = nodes.get(l), nodes.get(r)
    return nodes[0]


def trace():
    events, counted = [], []
    st = {'stack': [], 'k': K}

    def rec(kind, **kw):
        events.append(dict(kind=kind, stack=[n.idx for n in st['stack']], k=st['k'],
                           counted=list(counted), **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def kthSmallest(self, root, k: int) -> int:
            stack = []
            st['stack'] = stack
            curr = root
            while curr or stack:
                while curr:
                    stack.append(curr)
                    rec('push', node=curr.idx)
                    curr = curr.left
                curr = stack.pop()
                k -= 1
                st['k'] = k
                counted.append(curr.idx)
                rec('pop', node=curr.idx)
                if k == 0:
                    return curr.val
                rec('right', node=curr.idx, to=curr.right.idx if curr.right else None)
                curr = curr.right
            return -1

    rec('start')
    ans = Solution().kthSmallest(build(LEVEL), K)
    rec('done', ans=ans)
    return events


def words(e):
    k = e['kind']
    v = LEVEL[e['node']] if 'node' in e else None
    if k == 'start':
        return (f"Find the {K}rd smallest. In a BST, smaller values are always to the left.",
                "Slide left pushing nodes; the top of the stack is then the smallest uncounted value.", STEP)
    if k == 'push':
        return (f"Push {v} and keep going left.", "It's owed a visit once everything on its left is counted.", STEP)
    if k == 'pop':
        n = len(e['counted'])
        if e['k'] == 0:
            return (f"Pop {v}: that's value number {n}. k reached 0, so {v} is the answer.",
                    "Everything smaller was counted first, in order.", KEY)
        if n == 1:
            return (f"Pop {v}: the smallest value. Count it: {e['k']} more to go.",
                    "", STEP)
        return (f"Pop {v}: value number {n}. Count it: {e['k']} more to go.",
                "2 comes before its grandparent 3, because it's in 1's right subtree.", KEY)
    if k == 'right':
        if e['to'] is None:
            return (f"{v} has no right child, so go back to the stack.", "", QUICK * 2)
        return (f"Now step into {v}'s right child, {LEVEL[e['to']]}, before going back up to 3.",
                "Counting up the left edge (1, then 3) would skip it. This line is the trap.", KEY)
    return (f"Answer: {e['ans']}. Node 4 was never touched.",
            "The walk stops after k values: O(H + k), not the whole tree.", END)


def main():
    args = cli()
    sc = Scene(f'#230 Kth Smallest in a BST: inorder walk, stop at k = {K}',
               'Under each node: the order it was counted in (1st, 2nd, ...).')
    legend = [(ACTIVE, 'current node'), (style('window')[1], 'on the stack'),
              (style('good')[1], 'counted')]
    ordinal = {1: '1st', 2: '2nd', 3: '3rd'}
    for e in trace():
        styles = {i: 'window' for i in e['stack']}
        styles.update({i: 'good' for i in e['counted']})
        if e['kind'] == 'done':
            styles.update({i: 'muted' for i in TreeView.structure(LEVEL) if i not in e['counted']})
        labels = {i: ordinal.get(n + 1, f'{n + 1}th') for n, i in enumerate(e['counted'])}
        rings = [(e['node'], ACTIVE)] if 'node' in e else []
        stack = [(f'node {LEVEL[i]}', 'window') for i in e['stack']]
        cap, sub, hold = words(e)
        sc.frame([TreeView(LEVEL, styles=styles, labels=labels, rings=rings),
                  TextView([(f'counted so far: {[LEVEL[i] for i in e["counted"]]}', 'good')], size=17)],
                 cap, sub, hold, side=StackView(stack, 'Stack', note='top = smallest uncounted',
                                                empty='(empty)'),
                 counters={'k left': e['k'], 'answer': e.get('ans', '?')}, legend=legend)
    finish(sc, 230, "Watch what happens after 1 is counted: the walk steps into 1's right child and "
                    "counts 2 before going back up to 3. Counting up the left edge would skip it.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
