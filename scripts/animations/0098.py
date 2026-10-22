#!/usr/bin/env python3
"""#98 Validate BST: every node must fit the (lo, hi) range handed down by ALL its ancestors.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The tree is the notebook's scenario 2,
where 6 passes a parent-only check (6 < 15) but breaks its grandparent's rule.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [10, 5, 15, None, None, 6, 20]


class TreeNode:
    def __init__(self, val, idx):
        self.val, self.idx, self.left, self.right = val, idx, None, None


def build(level):
    kids = TreeView.structure(level)
    nodes = {i: TreeNode(level[i], i) for i in kids}
    for i, (l, r) in kids.items():
        nodes[i].left, nodes[i].right = nodes.get(l), nodes.get(r)
    return nodes[0]


def b(x):
    return '-∞' if x == float('-inf') else ('+∞' if x == float('inf') else str(x))


def trace(level):
    events, calls, verdict, rng = [], [], {}, {}

    def rec(kind, **kw):
        events.append(dict(kind=kind, calls=[list(c) for c in calls], verdict=dict(verdict),
                           rng=dict(rng), **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def isValidBST(self, root) -> bool:
            def validate(node, lo, hi):
                if not node:
                    rec('null', parent=calls[-1][0], lo=lo, hi=hi)
                    return True
                calls.append([node.idx, lo, hi, None])
                rng[node.idx] = (lo, hi)
                if node.val <= lo or node.val >= hi:
                    verdict[node.idx] = False; calls[-1][3] = False
                    rec('fail', node=node.idx, lo=lo, hi=hi); calls.pop()
                    return False
                verdict[node.idx] = True
                rec('pass', node=node.idx, lo=lo, hi=hi)
                ans = validate(node.left, lo, node.val) and \
                    validate(node.right, node.val, hi)
                calls[-1][3] = ans
                rec('return', node=node.idx, ans=ans); calls.pop()
                return ans

            return validate(root, float('-inf'), float('inf'))

    rec('start')
    ans = Solution().isValidBST(build(level))
    rec('done', ans=ans)
    return events


def words(e):
    k = e['kind']
    v = LEVEL[e['node']] if 'node' in e else None
    if k == 'start':
        return ("Each node must lie strictly inside a range (lo, hi) set by all its ancestors.",
                "The root has no limits. Going left caps the range; going right raises its floor.", STEP)
    if k == 'pass':
        lo, hi = b(e['lo']), b(e['hi'])
        if e['node'] == 2:
            return (f"15 is inside ({lo}, {hi}): fine. Its children get ({lo}, 15) and (15, {hi}).",
                    "The 10 from the root is still in force: anything under 15 must be above 10.", KEY)
        return (f"{v} is inside ({lo}, {hi}): fine.",
                f"Left child gets ({lo}, {v}); right child gets ({v}, {hi}).", STEP)
    if k == 'null':
        return (f"An empty child of {LEVEL[e['parent']]}: nothing there to break a rule.", "", QUICK)
    if k == 'fail':
        return (f"6 must be inside ({b(e['lo'])}, {b(e['hi'])}), and 6 is not above 10. Invalid.",
                "6 < 15 passes a parent-only check. The range remembers the grandparent's rule.", KEY)
    if k == 'return':
        if e['ans']:
            return (f"Everything under {v} checks out: return true.", "", STEP)
        return (f"{v} got false from below, so it returns false at once.",
                "'and' stops at the first false: 20 is never checked.", STEP)
    return (f"isValidBST returns {str(e['ans']).lower()}.",
            "Each node was checked once against its range: O(n), stopping at the first failure.", END)


def main():
    args = cli()
    sc = Scene('#98 Validate BST: carry the (lo, hi) range down',
               'Under each node: the range it had to fit when it was checked.')
    legend = [(ACTIVE, 'current call'), (style('window')[1], 'waiting'),
              (style('good')[1], 'inside its range'), (style('bad')[1], 'outside its range')]
    kids = TreeView.structure(LEVEL)
    parent = {c: p for p, cs in kids.items() for c in cs if c is not None}
    for e in trace(LEVEL):
        styles = {i: ('good' if ok else 'bad') for i, ok in e['verdict'].items()}
        waiting = [c[0] for c in e['calls']]
        for i in waiting:
            if e['verdict'].get(i):
                styles[i] = 'window'
        if e['kind'] == 'done':
            styles.update({i: 'muted' for i in kids if i not in e['verdict']})
        cur = e.get('node', e.get('parent'))
        rings = [(cur, ACTIVE)] if cur is not None and e['kind'] != 'done' else []
        edges = {(parent[i], i): 'active' for i in waiting if i in parent}
        labels = {i: f'({b(lo)}, {b(hi)})' for i, (lo, hi) in e['rng'].items()}
        stack = []
        for i, lo, hi, res in e['calls']:
            stack.append((f'validate({LEVEL[i]}, {b(lo)}, {b(hi)})' + ('' if res is None else f' = {str(res).lower()}'),
                          None if res is None else ('good' if res else 'bad')))
        if e['kind'] == 'null':
            stack.append((f'validate(empty, {b(e["lo"])}, {b(e["hi"])}) = true', 'muted'))
        cap, sub, hold = words(e)
        sc.frame(TreeView(LEVEL, styles=styles, labels=labels, edges=edges, rings=rings),
                 cap, sub, hold, side=StackView(stack, 'Call stack', base='isValidBST'),
                 counters={'answer': str(e['ans']).lower() if e['kind'] == 'done' else '?'}, legend=legend)
    finish(sc, 98, "Watch 6: it's smaller than its parent 15, which looks fine, but its range is (10, 15) "
                   "because it's in 10's right subtree, and 6 isn't above 10.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
