#!/usr/bin/env python3
"""#19 Remove Nth Node From End: sentinel, head start of n + 1, move together, unlink.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The sentinel is drawn as node 'S'.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

VALUES, N = [1, 2, 3, 4, 5], 2          # LeetCode example 1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def trace(values, n):
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    events, everything = [], []

    def rec(kind, **ptrs):
        ids = {id(x): i for i, x in enumerate(everything)}
        events.append(dict(kind=kind,
                           nxt=[ids[id(x.next)] if x.next else None for x in everything],
                           ptrs={k: (ids[id(v)] if v else None) for k, v in ptrs.items()}))

    # ---- the notebook's solution, with rec() calls added ----
    def removeNthFromEnd(head, n):
        sentinel = ListNode(0, head)
        everything[:] = [sentinel] + nodes          # display order: S, 1, 2, ...
        fast = sentinel
        slow = sentinel
        rec('start', slow=slow, fast=fast)

        for _ in range(n + 1):
            fast = fast.next
            rec('ahead', slow=slow, fast=fast)

        while fast:
            fast = fast.next
            slow = slow.next
            rec('together', slow=slow, fast=fast)

        slow.next = slow.next.next
        rec('unlink', slow=slow)
        return sentinel.next

    removeNthFromEnd(nodes[0], n)
    return events


def words(e, k_ahead, last_ahead):
    k, p = e['kind'], e['ptrs']
    lab = lambda i: 'S' if i == 0 else ('null' if i is None else str(VALUES[i - 1]))
    if k == 'start':
        return (f"Remove the {N}nd node from the end (the 4). Both pointers start on the sentinel S.",
                "S sits in front of the head, so even the head has a node before it.", KEY)
    if k == 'ahead':
        if last_ahead:
            return (f"fast is now {N} + 1 = {N + 1} nodes ahead of slow.",
                    "Why +1? Unlinking needs the node BEFORE the target, so slow must stop one short.", KEY)
        return (f"Head start: fast moves alone, step {k_ahead} of {N + 1}.", "", STEP)
    if k == 'together':
        if p['fast'] is None:
            return (f"fast has fallen off the end. slow is on {lab(p['slow'])}, one before the 4.",
                    "The gap never changed, so slow is exactly n + 1 behind the end.", KEY)
        return (f"Move both: fast to {lab(p['fast'])}, slow to {lab(p['slow'])}. The gap stays the same.",
                "", STEP)
    return (f"Unlink: {lab(p['slow'])}.next = {lab(e['nxt'][p['slow']])}. The 4 is skipped.",
            "Return S.next, not head: if the head had been removed, head would still point at it.", END)


def main():
    args = cli()
    sc = Scene('#19 Remove Nth Node From End of List',
               f'head = {VALUES}, n = {N}. A fixed gap between two pointers finds the end in one pass.')
    legend = [(style('muted')[1], 'sentinel'), (style('bad')[1], 'the node to remove'),
              (style('good')[1], 'where slow stops'), (ACTIVE, 'pointer')]
    target = len(VALUES) - N + 1                 # display index of the 4
    events = trace(VALUES, N)
    n_ahead = 0
    for idx, e in enumerate(events):
        k = e['kind']
        n_ahead += k == 'ahead'
        last_ahead = k == 'ahead' and (idx + 1 == len(events) or events[idx + 1]['kind'] != 'ahead')
        styles = {0: 'muted', target: 'bad'}
        if (k == 'together' and e['ptrs']['fast'] is None) or k == 'unlink':
            styles[e['ptrs']['slow']] = 'good'
        cut = {target} if k == 'unlink' else set()
        if k == 'unlink':
            styles[target] = 'muted'
        ptrs = dict(e['ptrs'])
        view = ListView(['S'] + VALUES, e['nxt'], styles, ptrs, cut=cut)
        gap = None
        if 'fast' in ptrs and 'slow' in ptrs:
            f = ptrs['fast'] if ptrs['fast'] is not None else len(VALUES) + 1
            gap = f - ptrs['slow']
        order, i = [], e['nxt'][0]
        while i is not None:
            order.append(str(VALUES[i - 1]))
            i = e['nxt'][i]
        text = TextView([f"list from S.next:  {' -> '.join(order)} -> null"], size=16)
        rows = [(name, 'null' if v is None else ('S' if v == 0 else f'node {VALUES[v - 1]}'))
                for name, v in ptrs.items()]
        if gap is not None:
            rows.append(('gap', f'{gap} steps', 'gold'))
        cap, sub, hold = words(e, n_ahead, last_ahead)
        sc.frame([view, text], cap, sub, hold,
                 side=MapView(rows, 'Pointers', headers=('name', 'on'), empty='(none)'),
                 counters={'n': N}, legend=legend)
    finish(sc, 19, "Watch fast fall off the end: because it started n + 1 ahead, slow is left one node "
                   "before the 4, which is exactly where the unlink needs it.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
