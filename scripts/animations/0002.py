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

# Hard examples (interactive page only). Notes are keyed by 'start', 'done' or
# the column number (0 = ones) and replace that frame's second caption line.
# 1) 1 + 9,999: l1 is the SHORT list, and the carry has to ripple through all
#    of l2's leftover digits. "Add while both lists have digits, then paste the
#    rest of the longer one" gives [0,9,9,9,1] (19,990). Answer [0,0,0,0,1].
HARD1 = ([1], [9, 9, 9, 9])
HARD1_NOTES = {
    'start': "l1 is the shorter list this time, and it runs out after one column.",
    0: "l1 has nothing left. Pasting l2's rest [9,9,9] on here would skip the carry.",
    1: "So the carry has to keep adding into l2's leftover digits: 9 + 1 = 10 again.",
    3: "The last 9 turns into 0 too, and the carry is still 1.",
    4: "Both lists are done, so the carry writes the 1. Pasting the rest gave 19,990.",
    'done': "Answer: 10,000. Every leftover digit goes through the same addition.",
}
# 2) 9,223,372,036,854,775,807 + 1: each input fits in a 64-bit integer, but the
#    sum is one too big, so "convert, add, convert back" wraps to
#    -9,223,372,036,854,775,808. Answer 9,223,372,036,854,775,808.
HARD2 = ([int(c) for c in reversed(str(2 ** 63 - 1))], [1])
HARD2_NOTES = {
    'start': "l1 is the biggest 64-bit integer. Adding it as a number would overflow.",
    0: "7 + 1 = 8. The loop only ever holds one digit and a carry, so it can't overflow.",
    1: "From here l2 counts as 0 and each digit of l1 is copied down.",
    18: "The 19th and last digit. The sum is one past what a 64-bit integer holds, and the loop never noticed.",
    'done': "In a 64-bit integer this sum wraps to -9,223,372,036,854,775,808.",
}


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_nodes(v):
    nodes = [ListNode(x) for x in v]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    return nodes


def trace(a, b):
    n1, n2 = make_nodes(a), make_nodes(b)
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


def words(e, seen, a, b, notes=None):
    k = e['kind']
    if k == 'start':
        cap = f"Add {num(a):,} + {num(b):,}. The digits are stored ones-first."
        if notes:
            return (cap, notes['start'], KEY)
        return (cap, "So walking from the head is column addition, ones column first.", KEY)
    if k == 'add':
        s = f"{e['v1']} + {e['v2']} + carry {e['cin']} = {e['total']}: write {e['total'] % 10}, carry {e['carry']}."
        if notes is not None:
            col = len(e['out']) - 1
            return (s, notes[col], KEY) if col in notes else (s, "", STEP)
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
            notes['done'] if notes else "One round per digit, plus one for the final carry. Return dummy.next.",
            END)


def build(a, b, subtitle, notes=None):
    sc = Scene('#2 Add Two Numbers: column addition with a carry', subtitle, height=760)
    legend = [(style('window')[1], 'l1'), (style('gold')[1], 'l2'), (style('good')[1], 'the answer'),
              (style('muted')[1], 'dummy head'), (ACTIVE, 'pointer / digit being added')]
    seen = set()
    for e in trace(a, b):
        k = e['kind']
        s1 = {i: 'window' for i in range(len(a))}
        s2 = {i: 'gold' for i in range(len(b))}
        if k == 'add':
            if e['p1'] is not None:
                s1[e['p1']] = 'active'
            if e['p2'] is not None:
                s2[e['p2']] = 'active'
        out = ['D'] + e['out']
        so = {0: 'muted', **{i: 'good' for i in range(1, len(out))}}
        if k == 'add':
            so[len(out) - 1] = 'active'
        views = [ListView(a, None, s1, {'l1': e['p1']} if k != 'done' else {}),
                 ListView(b, None, s2, {'l2': e['p2']} if k != 'done' else {}),
                 ListView(out, None, so, {'current': len(out) - 1} if k != 'done' else {})]
        cap, sub, hold = words(e, seen, a, b, notes)
        sc.frame(views, cap, sub, hold, counters={'carry': e['carry']}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(*HARD1, f'l1 = {HARD1[0]}, l2 = {HARD1[1]}: the short list is l1, and the carry ripples to the end.',
                HARD1_NOTES)
    sc2 = build(*HARD2, 'l1 = the biggest 64-bit integer, l2 = [1]. Both fit in 64 bits; their sum doesn\'t.',
                HARD2_NOTES)
    return [(sc1, "1 + 9,999: \"add while both lists have digits, then paste the rest of the longer one\" "
                  "skips the carry and returns 19,990. Watch the carry ripple through l2's leftover 9s to "
                  "give 10,000."),
            (sc2, "9,223,372,036,854,775,807 + 1: each number fits in a 64-bit integer but the sum doesn't, "
                  "so \"convert, add, convert back\" wraps to a negative number. Digit by digit gives "
                  "9,223,372,036,854,775,808.")]


def main():
    args = cli()
    sc = build(A, B, f'l1 = {A}, l2 = {B}, digits ones-first. Loop while l1, l2 or the carry remains.')
    finish(sc, 2, "Watch the last round: both lists are finished, but the carry is still 1, and that "
                  "carry alone writes the final digit.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
