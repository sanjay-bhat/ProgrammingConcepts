#!/usr/bin/env python3
"""#105 Build Tree from Preorder + Inorder: preorder names the root, inorder says how big the left side is.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The tree on the right is the
finished tree drawn faintly from the start (it comes from running the
solution first); nodes light up as the recursion actually creates them.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

PRE, INO = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]          # LeetCode example 1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def trace():
    events, calls, made = [], [], []

    def rec(kind, **kw):
        events.append(dict(kind=kind, calls=[list(c) for c in calls], made=list(made), **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def buildTree(self, preorder: list[int], inorder: list[int]):
            inorder_map = {v: i for i, v in enumerate(inorder)}

            def build(pre_start, pre_end, in_start, in_end):
                if pre_start > pre_end:
                    rec('empty', rng=(pre_start, pre_end, in_start, in_end))
                    return None
                root_val   = preorder[pre_start]
                in_root    = inorder_map[root_val]
                left_size  = in_root - in_start
                node       = TreeNode(root_val)
                calls.append([root_val, (pre_start, pre_end, in_start, in_end)])
                made.append(root_val)
                rec('root', rng=(pre_start, pre_end, in_start, in_end), root=root_val,
                    in_root=in_root, left_size=left_size)
                node.left  = build(pre_start + 1,             pre_start + left_size, in_start,   in_root - 1)
                node.right = build(pre_start + left_size + 1, pre_end,               in_root + 1, in_end)
                rec('return', root=root_val, rng=(pre_start, pre_end, in_start, in_end))
                calls.pop()
                return node

            return build(0, len(preorder) - 1, 0, len(inorder) - 1)

    rec('start')
    root = Solution().buildTree(PRE, INO)
    out, q = [], [root]                  # serialise the result for the TreeView
    while q:
        n = q.pop(0)
        out.append(n.val if n else None)
        if n:
            q += [n.left, n.right]
    while out[-1] is None:
        out.pop()
    rec('done', level=out)
    return events, out


def words(e):
    k = e['kind']
    if k == 'start':
        return ("Preorder lists the root first. Inorder lists left subtree, root, right subtree.",
                "Together they pin the tree down. A map gives each value's inorder position.", STEP)
    if k == 'root':
        r, ir, ls = e['root'], e['in_root'], e['left_size']
        ps, pe, is_, ie = e['rng']
        if ps == 0:
            return (f"First in preorder: {r} is the root. In inorder it's at position {ir}: {ls} value on its left.",
                    f"So the next {ls} preorder value is the left subtree, and the rest is the right.", KEY)
        if is_ > 0 and ls > 0:
            return (f"Root of this range is {r}, at inorder position {ir}. This range starts at {is_}.",
                    f"Left size = {ir} - {is_} = {ls}, not {ir}. Subtracting the start is the trap.", KEY)
        return (f"Root of this range is {r}. Nothing to its left in this inorder range.",
                "Left size 0: both of its child ranges will be checked next.", STEP)
    if k == 'empty':
        return ("Empty range: no subtree here, return null.", "", QUICK)
    if k == 'return':
        return (f"{e['root']}'s subtree is finished; hand it back to the caller.", "", QUICK * 2)
    return (f"Built: {e['level']}.".replace('None', 'null'),
            "One node per call and an instant lookup each time: O(n).", END)


def main():
    args = cli()
    events, final = trace()
    idx = {v: i for i, v in enumerate(final) if v is not None}
    kids = TreeView.structure(final)
    parent = {c: p for p, cs in kids.items() for c in cs if c is not None}
    sc = Scene('#105 Preorder + Inorder: the root, then the left count',
               'Brackets mark the current call\'s ranges. Gold = root, blue = its left subtree, pink = its right.',
               height=740)
    legend = [(ACTIVE, 'root just found'), (style('good')[1], 'node created'), (style('muted')[1], 'not built yet')]
    for e in events:
        pst, ist, ptr_p, ptr_i, win_p, win_i = {}, {}, {}, {}, None, None
        if e['kind'] in ('root', 'empty', 'return'):
            ps, pe, is_, ie = e['rng']
            win_p, win_i = (ps, pe), (is_, ie)
        if e['kind'] == 'root':
            ps, pe, is_, ie = e['rng']
            ls, ir = e['left_size'], e['in_root']
            pst.update({ps: 'gold', **{j: 'window' for j in range(ps + 1, ps + ls + 1)},
                        **{j: 'region2' for j in range(ps + ls + 1, pe + 1)}})
            ist.update({ir: 'gold', **{j: 'window' for j in range(is_, ir)},
                        **{j: 'region2' for j in range(ir + 1, ie + 1)}})
            ptr_p, ptr_i = {'root': ps}, {'root': ir}
        styles = {i: 'muted' for i in kids}
        styles.update({idx[v]: 'good' for v in e['made']})
        rings = [(idx[e['root']], ACTIVE)] if e['kind'] == 'root' else []
        edges = {(parent[idx[v]], idx[v]): 'good' for v in e['made'] if idx[v] in parent}
        stack = [(f'build(pre {r[0]}..{r[1]}, in {r[2]}..{r[3]})  root {v}', None) for v, r in e['calls']]
        if e['kind'] == 'empty':
            r = e['rng']
            stack.append((f'build(pre {r[0]}..{r[1]}, in {r[2]}..{r[3]})  empty', 'muted'))
        cap, sub, hold = words(e)
        sc.frame([ArrayView(PRE, styles=pst, pointers=ptr_p, window=win_p, title='preorder'),
                  ArrayView(INO, styles=ist, pointers=ptr_i, window=win_i, title='inorder '),
                  TreeView(final, styles=styles, edges=edges, rings=rings)],
                 cap, sub, hold, side=StackView(stack, 'Call stack', base='buildTree'),
                 counters={'nodes built': len(e['made'])}, legend=legend)
    finish(sc, 105, "Watch the call for [20, 15, 7]: 20 sits at inorder position 3, but this range starts "
                    "at 2, so its left subtree has 3 - 2 = 1 node, not 3.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
