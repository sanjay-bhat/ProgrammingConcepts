#!/usr/bin/env python3
"""#25 Reverse Nodes in k-Group: look k ahead, reverse the group in place, splice it back.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The dummy node is drawn as 'D'.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

VALUES, K = [1, 2, 3, 4, 5], 2          # LeetCode example 1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def trace(values, k):
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    everything, events = [], []

    def rec(kind, **ptrs):
        ids = {id(x): i for i, x in enumerate(everything)}
        events.append(dict(kind=kind,
                           nxt=[ids[id(x.next)] if x.next else None for x in everything],
                           ptrs={n: (ids[id(v)] if v else None) for n, v in ptrs.items()}))

    # ---- the notebook's solution, with rec() calls added ----
    def reverseKGroup(head, k):
        def get_kth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        dummy = ListNode(0, head)
        everything[:] = [dummy] + nodes
        group_prev = dummy
        rec('start', group_prev=group_prev)
        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                rec('stop', group_prev=group_prev)
                break
            group_start = group_prev.next
            next_group = kth.next
            rec('found', group_prev=group_prev, kth=kth, next_group=next_group)
            prev, curr = next_group, group_start
            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                rec('flip', group_prev=group_prev, prev=prev, curr=curr, next_group=next_group)
            group_prev.next = kth
            rec('splice', group_prev=group_prev, kth=kth, group_start=group_start)
            group_prev = group_start
            rec('advance', group_prev=group_prev)
        return dummy.next

    reverseKGroup(nodes[0], k)
    return events


def label(i):
    return 'D' if i == 0 else ('null' if i is None else str(VALUES[i - 1]))


def words(e, seen):
    k, p = e['kind'], e['ptrs']
    if k == 'start':
        return (f"Reverse every full group of k = {K}. D is a dummy node in front of the head.",
                "It gives the first group a 'node before it', like every other group.", KEY)
    if k == 'found':
        first = 'found' not in seen
        seen.add('found')
        return (f"Step {K} from {label(p['group_prev'])}: we reach {label(p['kth'])}, so a full group exists.",
                "Look ahead BEFORE flipping anything: a short group must be left alone." if first else
                f"The node after this group is {label(p['next_group'])}.", KEY if first else STEP)
    if k == 'flip':
        if 'flip' not in seen:
            seen.add('flip')
            return (f"Flip {label(p['prev'])}: it now points at {label(e['nxt'][p['prev']])}, the node AFTER the group.",
                    "prev started at next_group, not null, so the group's new tail is already reconnected.", KEY)
        return (f"Flip {label(p['prev'])} to point back at {label(e['nxt'][p['prev']])}.", "", STEP)
    if k == 'splice':
        first = 'splice' not in seen
        seen.add('splice')
        return (f"{label(p['group_prev'])}.next = {label(p['kth'])}: the node before the group points at its new head.",
                "That ties the other loose end. The group is reversed and back in the list.", KEY if first else STEP)
    if k == 'advance':
        return (f"group_prev moves to {label(p['group_prev'])}: the old first node, now this group's last.",
                "Moving it to kth instead is the classic slip: kth is now the group's FIRST node.", STEP)
    if k == 'stop':
        return (f"Step {K} from {label(p['group_prev'])} falls off the end: fewer than {K} nodes left.",
                "So the 5 stays exactly where it is. Answer: 2 1 4 3 5.", END)
    return ('', '', STEP)


def main():
    args = cli()
    sc = Scene('#25 Reverse Nodes in k-Group',
               f'head = {VALUES}, k = {K}. Look ahead k, reverse the group in place, splice it back.')
    legend = [(style('muted')[1], 'dummy'), (style('window')[1], 'current group'),
              (style('good')[1], 'done'), (ACTIVE, 'pointer')]
    seen = set()
    done = set()
    for e in trace(VALUES, K):
        k, p = e['kind'], e['ptrs']
        if k == 'advance':
            # everything before the new group_prev (inclusive) is final
            i = e['nxt'][0]
            while i is not None:
                done.add(i)
                if i == p['group_prev']:
                    break
                i = e['nxt'][i]
        styles = {0: 'muted', **{i: 'good' for i in done}}
        if k in ('found', 'flip', 'splice'):
            # the current group: everything between group_prev and next_group in original order
            grp = [i for i in range(1, len(VALUES) + 1) if i not in done]
            for i in grp[:K]:
                styles[i] = 'window'
        order, i = [], e['nxt'][0]
        while i is not None and len(order) <= len(VALUES):
            order.append(label(i))
            i = e['nxt'][i]
        view = ListView(['D'] + VALUES, e['nxt'], styles, {n: v for n, v in p.items()})
        text = TextView([f"reading from D.next:  {' -> '.join(order)} -> null"], size=16)
        rows = [(n, label(v)) for n, v in p.items()]
        cap, sub, hold = words(e, seen)
        sc.frame([view, text], cap, sub, hold,
                 side=MapView(rows, 'Pointers', headers=('name', 'on'), empty='(none)'),
                 counters={'k': K}, legend=legend)
    finish(sc, 25, "Watch the first flip: because prev starts on the node after the group, the group's "
                   "new tail is reconnected before the reversal even finishes.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
