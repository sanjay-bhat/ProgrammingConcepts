#!/usr/bin/env python3
"""#199 Right Side View: level order, keeping the last node taken out in each round.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
from collections import deque
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [1, 2, 3, None, 5, None, 4]          # LeetCode example 1


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
    events = []
    st = {'queue': [], 'result': [], 'seen': set(), 'hidden': set(), 'round': 0}

    def rec(kind, **kw):
        events.append(dict(kind=kind, queue=list(st['queue']), result=list(st['result']),
                           seen=set(st['seen']), hidden=set(st['hidden']), round=st['round'], **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def rightSideView(self, root):
            if not root:
                return []

            result = []
            queue = deque([root])
            st['queue'], st['result'] = queue, result

            while queue:
                size = len(queue)
                st['round'] += 1
                rec('count', size=size)
                for i in range(size):
                    node = queue.popleft()
                    if i == size - 1:
                        result.append(node.val)
                        st['seen'].add(node.idx)
                    else:
                        st['hidden'].add(node.idx)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    rec('pop', node=node.idx, i=i, size=size,
                        is_left=node.idx % 2 == 1)

            return result

    rec('start')
    ans = Solution().rightSideView(build(level))
    rec('done', ans=ans)
    return events


def words(e):
    k = e['kind']
    if k == 'start':
        return ("From the right you see one node per level: the last one on that level.",
                "So: go level by level with a queue, and keep the last node of each round.", STEP)
    if k == 'count':
        names = ', '.join(str(n.val) for n in e['queue'])
        return (f"Round {e['round']}: the queue holds {e['size']} ({names}). That's this whole level.",
                "Count first, so children added during the round wait for the next one.", STEP)
    if k == 'pop':
        v, i, size = LEVEL[e['node']], e['i'], e['size']
        if i == size - 1:
            if e['round'] == 3:
                return (f"Take out {v}: index {i} of {size}, the last of its level. You see it: record {v}.",
                        "The 5 came out earlier in the same round, so it's hidden behind the 4.", KEY)
            return (f"Take out {v}: index {i} of {size}, the last of its level. Record {v}.",
                    "Left children went in before right ones, so the last out is the rightmost.",
                    KEY if e['round'] == 2 else STEP)
        side = "a right child, but" if not e['is_left'] else ""
        return (f"Take out {v}: index {i} of {size}, not last. Someone further right hides it.",
                (f"{v} is {side} not the last on its level." if side else ""), STEP)
    return (f"Queue empty. Right side view: {e['ans']}.",
            "One node per level, each the last of its round. O(n): every node in and out once.", END)


def main():
    args = cli()
    sc = Scene('#199 Right Side View: the last node of each level',
               'Green = visible from the right. Faded = hidden behind a node further right.')
    legend = [(ACTIVE, 'just taken out'), (style('window')[1], 'in the queue'),
              (style('good')[1], 'visible'), (style('muted')[1], 'hidden')]
    for e in trace(LEVEL):
        styles = {i: 'muted' for i in e['hidden']}
        styles.update({i: 'good' for i in e['seen']})
        styles.update({n.idx: 'window' for n in e['queue']})
        rings = [(e['node'], ACTIVE)] if e['kind'] == 'pop' else []
        q = [(str(n.val), 'window') for n in e['queue']]
        cap, sub, hold = words(e)
        sc.frame([QueueView(q, 'Queue', empty='(empty)'),
                  TextView([(f'seen from the right: {e["result"]}', 'good')], size=17),
                  TreeView(LEVEL, styles=styles, rings=rings)],
                 cap, sub, hold, counters={'round': e['round'] or '-'}, legend=legend)
    finish(sc, 199, "Watch round 3: 5 comes out first and is hidden, then 4 comes out last and is "
                    "recorded. Visible means last on its level, not \"is a right child\".",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
