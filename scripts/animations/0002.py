#!/usr/bin/env python3
"""#2 Add Two Numbers: column addition down two linked lists, carrying as you go.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. LeetCode example 3 is used because it
shows all three things the loop handles: the carry, a list running out, and a
final carry that needs its own node.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

A, B = [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]          # LeetCode example 3


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(v):
    nodes = [ListNode(x) for x in v]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    return nodes


def trace(a, b):
    n1, n2 = build(a), build(b)
    i1 = {id(x): i for i, x in enumerate(n1)}
    i2 = {id(x): i for i, x in enumerate(n2)}
    events = []

    def rec(kind, l1, l2, dummy, carry, **kw):
        out, x = [], dummy.next
        while x:
            out.append(x.val)
            x = x.next
        events.append(dict(kind=kind, p1=i1.get(id(l1)) if l1 else None, p2=i2.get(id(l2)) if l2 else None,
                           out=out, carry=carry, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    def addTwoNumbers(l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        rec('start', l1, l2, dummy_head, carry)

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            cin = carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            rec('add', l1, l2, dummy_head, carry, v1=val1, v2=val2, cin=cin, total=total,
                gone1=l1 is None, gone2=l2 is None)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        rec('done', l1, l2, dummy_head, carry)
        return dummy_head.next

    addTwoNumbers(n1[0], n2[0])
    return events


def num(v):
    return int(''.join(map(str, reversed(v))))


def words(e, seen):
    k = e['kind']
    if k == 'start':
        return (f"Add {num(A):,} + {num(B):,}. The digits are stored ones-first.",
                "So walking from the head is column addition, ones column first.", KEY)
    if k == 'add':
        s = f"{e['v1']} + {e['v2']} + carry {e['cin']} = {e['total']}: write {e['total'] % 10}, carry {e['carry']}."
        if e['gone1'] and e['gone2']:
            return (s, "Both lists are finished, but the carry is 1, so the loop runs once more.", KEY)
        if e['gone2'] and 'gone' not in seen:
            seen.add('gone')
            return (s, "l2 has run out, so it reads as 0. No special case needed.", KEY)
        if e['carry'] and 'carry' not in seen:
            seen.add('carry')
            return (s, "Write the last digit, carry the 1 into the next column.", KEY)
        return (s, "", STEP)
    return (f"Done: {num(e['out']):,}, stored as {e['out']}.",
            "One round per digit, plus one for the final carry. Return dummy.next.", END)


def main():
    args = cli()
    sc = Scene('#2 Add Two Numbers: column addition with a carry',
               f'l1 = {A}, l2 = {B}, digits ones-first. Loop while l1, l2 or the carry remains.',
               height=760)
    legend = [(style('window')[1], 'l1'), (style('gold')[1], 'l2'), (style('good')[1], 'the answer'),
              (style('muted')[1], 'dummy head'), (ACTIVE, 'pointer / digit being added')]
    seen = set()
    for e in trace(A, B):
        k = e['kind']
        s1 = {i: 'window' for i in range(len(A))}
        s2 = {i: 'gold' for i in range(len(B))}
        if k == 'add':
            if e['p1'] is not None:
                s1[e['p1']] = 'active'
            if e['p2'] is not None:
                s2[e['p2']] = 'active'
        out = ['D'] + e['out']
        so = {0: 'muted', **{i: 'good' for i in range(1, len(out))}}
        if k == 'add':
            so[len(out) - 1] = 'active'
        views = [ListView(A, None, s1, {'l1': e['p1']} if k != 'done' else {}),
                 ListView(B, None, s2, {'l2': e['p2']} if k != 'done' else {}),
                 ListView(out, None, so, {'current': len(out) - 1} if k != 'done' else {})]
        cap, sub, hold = words(e, seen)
        sc.frame(views, cap, sub, hold, counters={'carry': e['carry']}, legend=legend)
    finish(sc, 2, "Watch the last round: both lists are finished, but the carry is still 1, and that "
                  "carry alone writes the final digit.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
