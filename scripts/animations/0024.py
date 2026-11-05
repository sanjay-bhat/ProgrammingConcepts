#!/usr/bin/env python3
"""#24 Swap Nodes in Pairs: a dummy node in front, then three pointer changes
per pair, then step prev to the pair's new tail.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The dummy node is drawn as 'D'.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403
from typing import Optional  # noqa: E402

VALUES = [1, 2, 3, 4]           # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
# 1) Odd length. Looping while prev.next alone (no check for a partner) reaches
#    the lone 5, takes second = None, and crashes reading second.next.
#    Answer [2,1,4,3,5].
HARD_ODD = [1, 2, 3, 4, 5]
# 2) Advancing prev to `second`, the pair's new FRONT, instead of `first`, its
#    new back. The next "pair" is then 1 and 3, so the 1 gets dragged to the
#    end: [2,3,4,5,6,1]. Answer [2,1,4,3,6,5].
HARD_PREV = [1, 2, 3, 4, 5, 6]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """The notebook's solution, to cross-check the traced run."""
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            first  = prev.next
            second = prev.next.next
            first.next  = second.next
            second.next = first
            prev.next   = second
            prev = first
        return dummy.next


def make(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def read(head, limit=50):
    out = []
    while head and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out


def no_partner_check(head):
    """First attempt: loop while prev.next, forgetting the lone last node."""
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next:
        first = prev.next
        second = prev.next.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next


def prev_to_second(head):
    """First attempt: step prev to the pair's new front (second)."""
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = second
    return dummy.next


def trace(values):
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    head = nodes[0] if nodes else None
    everything, events = [], []

    def rec(kind, **ptrs):
        ids = {id(x): i for i, x in enumerate(everything)}
        events.append(dict(kind=kind,
                           nxt=[ids[id(x.next)] if x.next else None for x in everything],
                           ptrs={n: (ids[id(v)] if v else None) for n, v in ptrs.items()}))

    # ---- the notebook's solution, with rec() calls added ----
    dummy = ListNode(0, head)
    everything[:] = [dummy] + nodes
    prev = dummy
    rec('start', prev=prev)
    while prev.next and prev.next.next:
        first  = prev.next
        second = prev.next.next
        rec('pair', prev=prev, first=first, second=second)
        first.next  = second.next
        rec('cut', prev=prev, first=first, second=second)
        second.next = first
        rec('back', prev=prev, first=first, second=second)
        prev.next   = second
        rec('stitch', prev=prev, first=first, second=second)
        prev = first
        rec('advance', prev=prev)
    rec('stop', prev=prev)
    ans = read(dummy.next)
    assert ans == read(Solution().swapPairs(make(values)))
    return events


def label(i, values):
    return 'D' if i == 0 else ('null' if i is None else str(values[i - 1]))


def order(e, values):
    out, i = [], e['nxt'][0]
    while i is not None and len(out) <= len(values):
        out.append(label(i, values))
        i = e['nxt'][i]
    return out


def words(e, seen, values):
    k, p = e['kind'], e['ptrs']
    lab = lambda i: label(i, values)
    first = k not in seen
    seen.add(k)
    if k == 'start':
        return ("D is a dummy node in front of the head. prev starts on it.",
                "Now the first pair has a node before it, like every other pair.", KEY)
    if k == 'pair':
        return (f"prev.next and prev.next.next both exist: pair {lab(p['first'])}, {lab(p['second'])}.",
                "Both checks matter: an odd last node has no partner." if first else "", KEY if first else STEP)
    if k == 'cut':
        return (f"first.next = second.next: {lab(p['first'])} now points past the pair, to "
                f"{lab(e['nxt'][p['first']])}.",
                "Do this FIRST. second.next is the only link to the rest of the list." if first else "",
                KEY if first else QUICK * 2.4)
    if k == 'back':
        return (f"second.next = first: {lab(p['second'])} points back at {lab(p['first'])}.",
                "", STEP if first else QUICK * 2.4)
    if k == 'stitch':
        return (f"prev.next = second: {lab(p['prev'])} now leads into {lab(p['second'])}.",
                "Three links changed: the pair is swapped and sewn back in." if first else "",
                KEY if first else QUICK * 2.4)
    if k == 'advance':
        return (f"prev moves to {lab(p['prev'])}, the pair's new BACK node.",
                "It's the node right before the next pair. Moving to second would pair the wrong nodes."
                if first else "", KEY if first else STEP)
    left = e['nxt'][p['prev']]
    tail = "Nothing left." if left is None else f"Only {lab(left)} is left, with no partner, so it stays."
    return (f"{tail} Answer: {' '.join(order(e, values)) or '(empty)'}.",
            "One pass, three pointer changes per pair: O(n) time, O(1) extra space.", END)


def build(values, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#24 Swap Nodes in Pairs: three links per pair', subtitle)
    legend = [(style('muted')[1], 'dummy'), (style('window')[1], 'current pair'),
              (style('good')[1], 'done'), (ACTIVE, 'pointer')]
    seen, done = set(), set()
    for idx, e in enumerate(trace(values)):
        k, p = e['kind'], e['ptrs']
        if k == 'advance':
            i = e['nxt'][0]
            while i is not None:
                done.add(i)
                if i == p['prev']:
                    break
                i = e['nxt'][i]
        styles = {0: 'muted', **{i: 'good' for i in done}}
        if k in ('pair', 'cut', 'back', 'stitch'):
            styles[p['first']] = styles[p['second']] = 'window'
        view = ListView(['D'] + values, e['nxt'], styles, dict(p))
        text = TextView([f"reading from D.next:  {' -> '.join(order(e, values) + ['null'])}"], size=16)
        rows = [(n, label(v, values)) for n, v in p.items()]
        cap, sub, hold = words(e, seen, values)
        if idx in notes:
            sub, hold = notes[idx], (END if k == 'stop' else KEY)
        sc.frame([view, text], cap, sub, hold,
                 side=MapView(rows, 'Pointers', headers=('name', 'on'), empty='(none)'), legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert read(Solution().swapPairs(make(HARD_ODD))) == [2, 1, 4, 3, 5]
    try:
        no_partner_check(make(HARD_ODD))
        raise AssertionError('expected the partner-less loop to crash')
    except AttributeError:
        pass
    assert read(Solution().swapPairs(make(HARD_PREV))) == [2, 1, 4, 3, 6, 5]
    assert read(prev_to_second(make(HARD_PREV))) == [2, 3, 4, 5, 6, 1]
    odd = build(HARD_ODD, f'head = {HARD_ODD}. Answer [2,1,4,3,5]. The 5 has no partner.', {
        11: "prev.next is 5 but prev.next.next is null. A loop that only checks prev.next would take "
            "second = null here and crash on second.next.",
    })
    wrong = build(HARD_PREV, f'head = {HARD_PREV}. Answer [2,1,4,3,6,5]. prev = second gives [2,3,4,5,6,1].', {
        5: "prev goes to 1, the pair's back node. Send it to 2 (second) instead and the next 'pair' is 1 and 3: "
           "the 1 gets dragged all the way to the end.",
    })
    return [
        (odd, "Five nodes: the 5 has no partner. A loop that only checks prev.next takes second = null at the end "
              "and crashes; the answer is [2,1,4,3,5]."),
        (wrong, "Six nodes. After a swap, prev must move to the pair's new BACK node (first). Moving it to second "
                "pairs 1 with 3, then 1 with 4, and returns [2,3,4,5,6,1]; the answer is [2,1,4,3,6,5]."),
    ]


def main():
    args = cli()
    sc = build(VALUES, f'head = {VALUES}. Swap every two neighbours by changing links, never values.')
    finish(sc, 24, "Watch the first pair's three link changes: 1 points past the pair first, then 2 points back "
                   "at 1, then the dummy points at 2.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
