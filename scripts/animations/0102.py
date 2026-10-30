#!/usr/bin/env python3
"""#102 Level Order Traversal: count the queue at the start of each round; that's one whole level.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
from collections import deque
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

LEVEL = [3, 9, 20, None, None, 15, 7]          # LeetCode example 1
ROW_COLOURS = [0, 2, 3, 4, 5]                  # skips region1, which is the queue's blue


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
    st = {'row_of': {}, 'queue': [], 'result': [], 'level': [], 'round': 0}

    def rec(kind, **kw):
        events.append(dict(kind=kind, row_of=dict(st['row_of']), queue=list(st['queue']),
                           result=[list(r) for r in st['result']], level=list(st['level']),
                           round=st['round'], **kw))

    class Solution:
        # ---- the notebook's solution, with rec() calls added ----
        def levelOrder(self, root) -> list[list[int]]:
            if not root:
                return []
            result, queue = [], deque([root])
            st['queue'], st['result'] = queue, result
            while queue:
                level = []
                st['level'] = level
                st['round'] += 1
                rec('count', size=len(queue))
                for _ in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    st['row_of'][node.idx] = st['round'] - 1
                    added = [c.idx for c in (node.left, node.right) if c]
                    if node.left:  queue.append(node.left)
                    if node.right: queue.append(node.right)
                    rec('pop', node=node.idx, added=added)
                result.append(level)
                rec('row', row=list(level))
            return result

    rec('start')
    ans = Solution().levelOrder(build(level))
    rec('done', ans=ans)
    return events


def words(e):
    k = e['kind']
    v = lambda i: LEVEL[i]
    if k == 'start':
        return ("Put the root in the queue. Join at the back, leave from the front.",
                "Each round of the loop will produce one row of the answer.", STEP)
    if k == 'count':
        names = ', '.join(str(n.val) for n in e['queue'])
        hold = KEY if e['round'] == 2 else STEP
        return (f"Round {e['round']}: the queue holds {e['size']} node{'s' if e['size'] > 1 else ''} ({names}). That's this whole row.",
                f"Take out exactly {e['size']}. Children added from now on wait for the next round.", hold)
    if k == 'pop':
        kids = ' and '.join(str(LEVEL[c]) for c in e['added'])
        tail = f" {kids} join the back of the queue." if e['added'] else " It has no children."
        return (f"Take out {v(e['node'])} and add it to the current row.{tail}",
                "They're behind everything from this row, so they can't sneak into it." if e['added'] and e['round'] == 2 else "",
                KEY if e['added'] and e['round'] == 2 else STEP)
    if k == 'row':
        return (f"Took out {len(e['row'])}, as counted. Save row {e['round'] - 1}: {e['row']}.", "", STEP)
    return (f"The queue is empty. Answer: {e['ans']}.",
            "Every node went in once and came out once: O(n).", END)


def main():
    args = cli()
    sc = Scene('#102 Level Order: one queue, one row per round',
               'Each colour is a finished row. Blue outline = waiting in the queue.')
    legend = [(ACTIVE, 'just taken out'), (style('window')[1], 'in the queue')]
    for e in trace(LEVEL):
        styles = {i: f'region{ROW_COLOURS[r % len(ROW_COLOURS)]}' for i, r in e['row_of'].items()}
        styles.update({n.idx: 'window' for n in e['queue']})
        rings = []
        if e['kind'] == 'pop':
            rings = [(e['node'], ACTIVE)]
        q = [(str(n.val), 'window') for n in e['queue']]
        lines = [f'answer so far: {e["result"]}']
        if e['kind'] in ('count', 'pop'):
            lines.append((f'current row:   {e["level"]}', 'active'))
        cap, sub, hold = words(e)
        sc.frame([QueueView(q, 'Queue', empty='(empty)'), TextView(lines, size=16),
                  TreeView(LEVEL, styles=styles, rings=rings)],
                 cap, sub, hold, counters={'round': e['round'] or '-'}, legend=legend)
    finish(sc, 102, "Watch round 2 start: the queue holds 9 and 20, so exactly two come out, "
                    "and 15 and 7 join behind them for round 3 instead of sneaking into row 1.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
