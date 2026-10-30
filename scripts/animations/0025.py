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

# Hard examples (interactive page only). Notes are keyed by event number and
# replace that frame's second caption line (held as a KEY moment).
# 1) The list ends exactly on a group boundary. The second group's kth is the
#    last node, so kth.next is null: "stop when kth.next is null" leaves 4 5 6
#    unreversed and returns [3,2,1,4,5,6]. Answer [3,2,1,6,5,4].
HARD1 = ([1, 2, 3, 4, 5, 6], 3)
HARD1_NOTES = {
    7: "kth is 6 and kth.next is null. That's fine: this full group just runs to the end of the list.",
    8: "Stopping because kth.next was null would have left 4 5 6 as they were.",
    13: "Nothing is left over. Answer: 3 2 1 6 5 4. Stopping on kth.next = null gave 3 2 1 4 5 6.",
}
# 2) Two nodes are left after the last full group. They must stay as they are;
#    reversing the leftover too returns [3,2,1,6,5,4,8,7]. Answer [3,2,1,6,5,4,7,8].
HARD2 = ([1, 2, 3, 4, 5, 6, 7, 8], 3)
HARD2_NOTES = {
    13: "7 and 8 are a short group, so they stay in order. Reversing them too gives ... 8 7. Answer: 3 2 1 6 5 4 7 8.",
}


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


def label(i, values=VALUES):
    return 'D' if i == 0 else ('null' if i is None else str(values[i - 1]))


def words(e, seen, values=VALUES, K=K):
    k, p = e['kind'], e['ptrs']
    lab = lambda i: label(i, values)
    if k == 'start':
        return (f"Reverse every full group of k = {K}. D is a dummy node in front of the head.",
                "It gives the first group a 'node before it', like every other group.", KEY)
    if k == 'found':
        first = 'found' not in seen
        seen.add('found')
        return (f"Step {K} from {lab(p['group_prev'])}: we reach {lab(p['kth'])}, so a full group exists.",
                "Look ahead BEFORE flipping anything: a short group must be left alone." if first else
                f"The node after this group is {lab(p['next_group'])}.", KEY if first else STEP)
    if k == 'flip':
        if 'flip' not in seen:
            seen.add('flip')
            return (f"Flip {lab(p['prev'])}: it now points at {lab(e['nxt'][p['prev']])}, the node AFTER the group.",
                    "prev started at next_group, not null, so the group's new tail is already reconnected.", KEY)
        return (f"Flip {lab(p['prev'])} to point back at {lab(e['nxt'][p['prev']])}.", "", STEP)
    if k == 'splice':
        first = 'splice' not in seen
        seen.add('splice')
        return (f"{lab(p['group_prev'])}.next = {lab(p['kth'])}: the node before the group points at its new head.",
                "That ties the other loose end. The group is reversed and back in the list.", KEY if first else STEP)
    if k == 'advance':
        return (f"group_prev moves to {lab(p['group_prev'])}: the old first node, now this group's last.",
                "Moving it to kth instead is the classic slip: kth is now the group's FIRST node.", STEP)
    if k == 'stop':
        order, left, i = [], [], e['nxt'][0]
        while i is not None:
            order.append(lab(i))
            i = e['nxt'][i]
        i = e['nxt'][p['group_prev']]
        while i is not None:
            left.append(lab(i))
            i = e['nxt'][i]
        if len(left) == 1:
            rest = f"So the {left[0]} stays exactly where it is."
        elif left:
            rest = f"So {' '.join(left)} stay exactly where they are."
        else:
            rest = "Nothing is left over."
        return (f"Step {K} from {lab(p['group_prev'])} falls off the end: fewer than {K} nodes left.",
                f"{rest} Answer: {' '.join(order)}.", END)
    return ('', '', STEP)


def build(values, K, subtitle, notes=None):
    sc = Scene('#25 Reverse Nodes in k-Group', subtitle)
    legend = [(style('muted')[1], 'dummy'), (style('window')[1], 'current group'),
              (style('good')[1], 'done'), (ACTIVE, 'pointer')]
    seen = set()
    done = set()
    for idx, e in enumerate(trace(values, K)):
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
            grp = [i for i in range(1, len(values) + 1) if i not in done]
            for i in grp[:K]:
                styles[i] = 'window'
        order, i = [], e['nxt'][0]
        while i is not None and len(order) <= len(values):
            order.append(label(i, values))
            i = e['nxt'][i]
        view = ListView(['D'] + values, e['nxt'], styles, {n: v for n, v in p.items()})
        text = TextView([f"reading from D.next:  {' -> '.join(order)} -> null"], size=16)
        rows = [(n, label(v, values)) for n, v in p.items()]
        cap, sub, hold = words(e, seen, values, K)
        if notes and idx in notes:
            sub, hold = notes[idx], (END if k == 'stop' else KEY)
        sc.frame([view, text], cap, sub, hold,
                 side=MapView(rows, 'Pointers', headers=('name', 'on'), empty='(none)'),
                 counters={'k': K}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(*HARD1, f'head = {HARD1[0]}, k = {HARD1[1]}. The list ends exactly where a group ends.', HARD1_NOTES)
    sc2 = build(*HARD2, f'head = {HARD2[0]}, k = {HARD2[1]}. Two nodes are left after the last full group.',
                HARD2_NOTES)
    return [(sc1, "Six nodes, k = 3: the last group ends on the last node, so kth.next is null. Stop on that "
                  "and 4 5 6 stay unreversed; the answer is 3 2 1 6 5 4."),
            (sc2, "Eight nodes, k = 3: 7 and 8 are a short leftover and must stay put. Reverse it too and "
                  "you get ... 8 7; the answer is 3 2 1 6 5 4 7 8.")]


def main():
    args = cli()
    sc = build(VALUES, K, f'head = {VALUES}, k = {K}. Look ahead k, reverse the group in place, splice it back.')
    finish(sc, 25, "Watch the first flip: because prev starts on the node after the group, the group's "
                   "new tail is reconnected before the reversal even finishes.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
