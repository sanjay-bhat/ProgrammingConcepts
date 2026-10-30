#!/usr/bin/env python3
"""#110 Balanced Binary Tree: heights travel up; the first imbalance becomes -1 and skips the rest.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The tree is the classic trap: the
root's two sides are equally tall (3 and 3), but each child of the root is
lopsided, so checking only the root would wrongly say true.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]


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

    def ret(node, value, why, **kw):          # recorder only: logs what this call returns
        calls[-1][1] = value
        done[node.idx] = value
        rec('return', node=node.idx, value=value, why=why, **kw)
        calls.pop()

    class Solution:
        # ---- the notebook's solution, with rec()/ret() calls added ----
        def isBalanced(self, root) -> bool:
            def check_height(node) -> int:
                if calls:
                    calls[-1][2] += 1
                if not node:
                    rec('null', parent=calls[-1][0], side='left' if calls[-1][2] == 1 else 'right')
                    return 0
                calls.append([node.idx, None, 0])
                rec('call', node=node.idx)
                left_h  = check_height(node.left)
                if left_h  == -1: ret(node, -1, 'left-bad'); return -1
                right_h = check_height(node.right)
                if right_h == -1: ret(node, -1, 'right-bad'); return -1
                if abs(left_h - right_h) > 1: ret(node, -1, 'gap', l=left_h, r=right_h); return -1
                ret(node, 1 + max(left_h, right_h), 'ok', l=left_h, r=right_h)
                return 1 + max(left_h, right_h)
            return check_height(root) != -1

    rec('start')
    answer = Solution().isBalanced(build(level))
    rec('done', ans=answer)
    return events


def words(e, level):
    k = e['kind']
    v = lambda i: level[i]
    if k == 'start':
        return ("The root's two sides are both 3 tall, so a root-only check would say true.",
                "But the rule applies at every node. Each call returns a height, or -1 for trouble.", KEY)
    if k == 'call':
        return (f"check_height({v(e['node'])}): left child first.",
                "This call waits on the stack until its children report.", STEP)
    if k == 'null':
        return (f"{v(e['parent'])}'s {e['side']} child is empty: height 0.", "", QUICK)
    if k == 'return':
        n, w = v(e['node']), e['why']
        if w == 'ok':
            return (f"Node {n}: heights {e['l']} and {e['r']}, gap {abs(e['l'] - e['r'])}. Fine, return {e['value']}.",
                    "", STEP if e['l'] or e['r'] else QUICK * 2)
        if w == 'gap':
            return (f"Node {n}: heights {e['l']} and {e['r']}, a gap of {abs(e['l'] - e['r'])}. Unbalanced: return -1.",
                    "This node is below the root, so a root-only check never sees it.", KEY)
        return (f"Node {n}: its left child reported -1, so it returns -1 at once.",
                "It doesn't even look at its right side: the answer is already settled.", KEY)
    return (f"isBalanced returns {str(e['ans']).lower()}.",
            "The faded nodes on the right were never visited: the -1 skipped them.", END)


def main():
    args = cli()
    sc = Scene('#110 Balanced Binary Tree: check every node, pass -1 up',
               'Under each node: the height it returned, or -1 if something below is unbalanced.')
    legend = [(ACTIVE, 'current call'), (style('window')[1], 'waiting'),
              (style('good')[1], 'balanced here'), (style('bad')[1], 'returned -1')]
    kids = TreeView.structure(LEVEL)
    parent = {c: p for p, cs in kids.items() for c in cs if c is not None}
    for e in trace(LEVEL):
        waiting = [c[0] for c in e['calls']]
        styles = {i: ('bad' if h == -1 else 'good') for i, h in e['done'].items()}
        styles.update({i: 'window' for i in waiting if i not in e['done']})
        if e['kind'] == 'done':
            styles.update({i: 'muted' for i in kids if i not in e['done']})
        rings = []
        cur = e.get('node') if e['kind'] in ('call', 'return') else (e.get('parent') if e['kind'] == 'null' else None)
        if cur is not None:
            rings.append((cur, ACTIVE))
            if e['kind'] == 'call':
                styles[cur] = 'active'
        edges = {(parent[i], i): 'active' for i in waiting if i in parent}
        labels = {i: f'{h}' if h == -1 else f'h {h}' for i, h in e['done'].items()}
        stack = [(f'check_height({LEVEL[i]})' + ('' if a is None else f'  = {a}'),
                  None if a is None else ('bad' if a == -1 else 'good')) for i, a, _ in e['calls']]
        if e['kind'] == 'null':
            stack.append(('check_height(empty)  = 0', 'muted'))
        cap, sub, hold = words(e, LEVEL)
        res = str(e['ans']).lower() if e['kind'] == 'done' else '?'
        sc.frame(TreeView(LEVEL, styles=styles, labels=labels, edges=edges, rings=rings),
                 cap, sub, hold,
                 side=StackView(stack, 'Call stack', base='isBalanced', empty='(empty)'),
                 counters={'answer': res}, legend=legend)
    finish(sc, 110, "Watch the left 2: one side is 2 tall and the other is empty, so it returns -1, "
                    "and the root passes that straight up without visiting its right side.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
