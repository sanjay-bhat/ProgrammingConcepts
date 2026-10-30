#!/usr/bin/env python3
"""#297 Serialize and Deserialize Binary Tree: a preorder walk that writes `null`
for every empty slot, then the same walk run backwards with one shared cursor.

The trace comes from running the notebook's Python Codec with a recorder added;
the algorithm lines are unchanged. The tree is LeetCode's example 1.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [1, 2, 3, None, None, 4, 5]   # LeetCode example 1


class TreeNode:
    def __init__(self, x, idx=None):
        self.val, self.idx, self.left, self.right = x, idx, None, None


def build(level):
    kids = TreeView.structure(level)
    nodes = {i: TreeNode(level[i], i) for i in kids}
    for i, (l, r) in kids.items():
        nodes[i].left, nodes[i].right = nodes.get(l), nodes.get(r)
    return nodes[0]


def to_level(root, kids=None):
    """Level-order list of a (partly built) tree plus {id(node): index} for styling.
    kids: optional {id(node): [left, right]} links to follow instead of .left/.right."""
    if root is None:
        return [], {}
    out, ids, q = [], {}, [root]
    while q:
        n = q.pop(0)
        if n is None:
            out.append(None)
            continue
        ids[id(n)] = len(out)
        out.append(n.val)
        q += kids.get(id(n), [None, None]) if kids is not None else [n.left, n.right]
    while out and out[-1] is None:
        out.pop()
    return out, ids


def trace(level):
    events, calls = [], []
    st = {'phase': 'ser', 'result': [], 'tokens': [], 'pos': -1, 'root': None, 'done': set()}
    # the drawing's links: node.left/right are only assigned when a child call returns,
    # so record each new node under its parent the moment it's created
    links, left_done = {}, set()

    def rec(kind, **kw):
        if kind == 'de_node' and kw['parent'] is not None:
            par = kw['parent']
            links.setdefault(id(par), [None, None])[1 if id(par) in left_done else 0] = kw['node']
        if kind == 'de_left_done':
            left_done.add(id(kw['node']))
        lv, ids = to_level(st['root'], links if st['phase'] == 'de' else None)
        events.append(dict(kind=kind, phase=st['phase'], result=list(st['result']), tokens=list(st['tokens']),
                           pos=st['pos'], calls=list(calls), built=lv, ids=ids, done=set(st['done']), **kw))

    class Codec:
        # ---- the notebook's solution, with rec() calls added ----
        def serialize(self, root) -> str:
            result = []
            st['result'] = result

            def dfs(node):
                if not node:
                    result.append('null')
                    rec('ser_null', parent=calls[-1] if calls else None)
                    return
                result.append(str(node.val))
                calls.append(node.idx)
                rec('ser_node', node=node.idx)
                dfs(node.left)
                dfs(node.right)
                calls.pop()
                st['done'].add(node.idx)
            dfs(root)
            return ','.join(result)

        def deserialize(self, data: str):
            tokens = iter(data.split(','))
            st['tokens'] = data.split(',')

            def dfs():
                val = next(tokens)
                st['pos'] += 1
                if val == 'null':
                    rec('de_null', parent=calls[-1] if calls else None)
                    return None
                node = TreeNode(int(val))
                if st['root'] is None:
                    st['root'] = node
                parent = calls[-1] if calls else None
                calls.append(node)
                rec('de_node', node=node, parent=parent)
                node.left = dfs()
                rec('de_left_done', node=node)
                node.right = dfs()
                calls.pop()
                return node
            return dfs()

    rec('start')
    c = Codec()
    data = c.serialize(build(level))
    st['phase'] = 'de'
    rec('serialized', data=data)
    back = c.deserialize(data)
    st['phase'] = 'end'
    rec('done', same=to_level(back)[0] == level)
    return events


def words(e):
    k = e['kind']
    if k == 'start':
        return ("Serialize: write each node, then its left subtree, then its right subtree.",
                "Every empty child slot gets written down too, as 'null'.", STEP)
    if k == 'ser_node':
        v = LEVEL[e['node']]
        return (f"Write {v}. Then go left, then right.", "", STEP if e['node'] == 0 else QUICK * 2.5)
    if k == 'ser_null':
        p = e['parent']
        first = e['result'].count('null') == 1
        if first:
            return (f"{LEVEL[p]} has no left child: write 'null'.",
                    "This marker is what lets the reader know where 2's subtree ends.", KEY)
        return (f"Empty slot under {LEVEL[p]}: write 'null'.", "", QUICK * 1.5)
    if k == 'serialized':
        return (f"Done: 5 values and 6 nulls. A tree with n nodes always has n + 1 empty slots.",
                "Now read it back with the same walk: one token per call, one shared cursor.", KEY)
    if k == 'de_node':
        v = e['node'].val
        if e['pos'] == 4:
            return (f"Token 4 is {v}: the root's right child.",
                    "2's calls already used tokens 1 to 3, and the shared cursor is right here.", KEY)
        if e['parent'] is None:
            return (f"Token 0 is {v}: make the root, then build its left child.", "", STEP)
        return (f"Token {e['pos']} is {v}: make a node under {e['parent'].val}.", "", STEP)
    if k == 'de_null':
        p = e['parent']
        return (f"Token {e['pos']} is null: that slot under {p.val} stays empty.",
                "", QUICK * 2 if e['pos'] != 3 else STEP)
    if k == 'de_left_done':
        v = e['node'].val
        return (f"{v}'s left side is finished. The very next token belongs to its right side.", "", QUICK * 2)
    return ("Every token was used exactly once, and the rebuilt tree matches the original.",
            "Each node and each empty slot is written once and read once: O(n).", END)


def main():
    args = cli()
    sc = Scene('#297 Serialize / Deserialize: preorder with null markers',
               'Top: the tree. Bottom: the token list. Both directions walk node, left, right.')
    kids = TreeView.structure(LEVEL)
    parent = {c: p for p, cs in kids.items() for c in cs if c is not None}
    for e in trace(LEVEL):
        tok_styles, ptr = {}, {}
        if e['phase'] == 'ser' or e['kind'] == 'start':
            vals = e['result']
            styles = {i: 'muted' for i in e['done']}
            for i in e['calls']:
                styles[i] = 'window'
            cur = e.get('node', e.get('parent'))
            rings = [(cur, ACTIVE)] if cur is not None else []
            edges = {(parent[i], i): 'active' for i in e['calls'] if i in parent}
            tree = TreeView(LEVEL, styles=styles, rings=rings, edges=edges)
            for i, t in enumerate(vals):
                tok_styles[i] = 'muted' if t == 'null' else 'good'
            if vals:
                tok_styles[len(vals) - 1] = 'active'
            title = 'Tokens written so far'
            stack = [f'serialize({LEVEL[i]})' for i in e['calls']]
            if e['kind'] == 'ser_null':
                stack.append(('serialize(empty)', 'muted'))
            base = 'serialize'
        else:
            vals = e['tokens']
            lv, ids = e['built'], e['ids']
            styles, rings = {}, []
            on = {ids[id(n)] for n in e['calls'] if id(n) in ids}
            for i, v in enumerate(lv):
                if v is not None:
                    styles[i] = 'window' if i in on else 'good'
            node = e.get('node') or e.get('parent')
            if node is not None and id(node) in ids and e['kind'] != 'done':
                rings = [(ids[id(node)], ACTIVE)]
            tree = TreeView(lv, styles=styles, rings=rings) if lv else TextView(['(nothing built yet)'])
            for i, t in enumerate(vals):
                if i < e['pos']:
                    tok_styles[i] = 'muted'
                elif i == e['pos']:
                    tok_styles[i] = 'active'
            if 0 <= e['pos'] < len(vals) and e['kind'] != 'done':
                ptr = {'cursor': e['pos']}
            title = 'Tokens being read back'
            stack = [f'deserialize → {n.val}' for n in e['calls']]
            if e['kind'] == 'de_null':
                stack.append(('deserialize → null', 'muted'))
            base = 'deserialize' if e['phase'] != 'end' else 'done'
        cap, sub, hold = words(e)
        arr = ArrayView(vals, styles=tok_styles, pointers=ptr, title=None, cell=44)
        sc.frame([tree, TextView([], title=title, size=14), arr], cap, sub, hold,
                 side=StackView(stack, 'Call stack', base=base),
                 counters={'tokens': len(vals) if e['phase'] == 'ser' else f'{max(0, e["pos"] + 1)}/{len(vals)}'})
    finish(sc, 297, "Watch the reader reach token 4: the calls that built 2 used tokens 1 to 3, so the shared "
                    "cursor is already on the 3, the root's right child.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
