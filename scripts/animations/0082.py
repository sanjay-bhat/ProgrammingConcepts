#!/usr/bin/env python3
"""#82 Remove Duplicates from Sorted List II: prev waits on the last keeper, runs are jumped whole.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. The dummy node is drawn as 'D'.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

VALUES = [1, 2, 3, 3, 4, 4, 5]            # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_TAIL = [1, 2, 3, 3, 4, 4]            # [1,2]; a "copy keepers onto a tail" version that never cuts the tail returns the input
HARD_ZERO = [0, 1, 1, 1, 2, 2, 3]         # [0,3]; using the dummy (value 0) as "the node before the head" deletes the 0


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            is_dup = curr.next and curr.val == curr.next.val
            if is_dup:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next


def make(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def no_cut(head):
    """First attempt: append each keeper to a tail pointer, but never cut the tail at the end."""
    dummy = ListNode(0, head)
    tail, before, curr = dummy, None, head
    while curr:
        nxt = curr.next
        if (before is None or curr.val != before.val) and (nxt is None or nxt.val != curr.val):
            tail.next = curr
            tail = curr
        before, curr = curr, nxt
    return dummy.next


def dummy_as_before(head):
    """First attempt: keep a node if it differs from both neighbours, with the dummy as the head's left neighbour."""
    dummy = ListNode(0, head)
    tail, before, curr = dummy, dummy, head
    while curr:
        nxt = curr.next
        if curr.val != before.val and (nxt is None or nxt.val != curr.val):
            tail.next = curr
            tail = curr
        before, curr = curr, nxt
    tail.next = None
    return dummy.next


def trace(values):
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    head = nodes[0] if nodes else None
    events, gone = [], set()
    allnodes = []

    def rec(kind, **kw):
        ids = {id(x): i for i, x in enumerate(allnodes)}
        nxt = [ids[id(x.next)] if x.next else None for x in allnodes]
        events.append(dict(kind=kind, nxt=nxt, gone=set(gone),
                           prev=ids[id(prev)], curr=(ids[id(curr)] if curr else None), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    dummy = ListNode(0, head)
    allnodes[:] = [dummy] + nodes
    prev = dummy
    curr = head
    rec('start')
    while curr:
        is_dup = curr.next and curr.val == curr.next.val
        if is_dup:
            val = curr.val
            rec('run', val=val)
            while curr and curr.val == val:
                gone.add(allnodes.index(curr))
                curr = curr.next
                rec('skip', val=val)
            prev.next = curr
            rec('jump', val=val)
        else:
            rec('keeper')
            prev = curr
            curr = curr.next
            rec('step')
    rec('done')
    assert to_list(dummy.next) == to_list(Solution().deleteDuplicates(make(values)))
    return events


def build(values, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#82 Remove Duplicates from Sorted List II', subtitle)
    legend = [(style('gold')[1], 'dummy D'), (style('good')[1], 'kept'), (style('bad')[1], 'removed run'),
              (style('active')[1], 'curr is looking at it')]
    lab = lambda i: 'null' if i is None else ('D' if i == 0 else str(values[i - 1]))
    seen = set()
    for e in trace(values):
        k, p, c = e['kind'], e['prev'], e['curr']
        # what is reachable from D right now
        order, i, kept = [], e['nxt'][0], set()
        while i is not None and len(order) <= len(values):
            order.append(lab(i))
            i = e['nxt'][i]
        styles = {0: 'gold'}
        i = e['nxt'][0]
        while i is not None and i != c:          # nodes up to prev are settled keepers
            styles[i] = 'good'
            if i == p:
                break
            i = e['nxt'][i]
        for g in e['gone']:
            styles[g] = 'bad'
        if c is not None and k in ('run', 'keeper'):
            styles[c] = 'active'
        if k == 'done':
            styles.update({i: 'good' for i in range(1, len(values) + 1) if i not in e['gone']})
        ptrs = {'prev': p, 'curr': c} if k != 'done' else {}
        cut = {g for g in e['gone']}
        view = ListView(['D'] + values, e['nxt'], styles, ptrs, cut=cut)
        text = TextView([(f"reading from D.next:  {' -> '.join(order + ['null'])}", 'good' if k == 'done' else None)], size=16)
        v = e.get('val')
        if k == 'start':
            cap, sub, hold = ("D is a dummy node in front of the head. prev starts on it, curr on the first real node.",
                              notes.get('start', "prev always sits on the last node we're sure to keep."), KEY)
        elif k == 'run':
            first = 'run' not in seen
            seen.add('run')
            cap = f"curr is {v} and the next node is {v} too: a run starts here."
            sub = ("Every copy has to go, so walk curr past all of them before relinking anything."
                   if first else notes.get('run2', "Another run. prev hasn't moved, so it can still relink."))
            hold = KEY if first or 'run2' in notes else STEP
        elif k == 'skip':
            cap = f"curr steps past a {v} and lands on {lab(c)}."
            sub, hold = ("", QUICK * 2)
            if c is not None and values[c - 1] == v:
                sub = "Same value, keep going."
        elif k == 'jump':
            first = 'jump' not in seen
            seen.add('jump')
            cap = f"{lab(p)}.next = {lab(c)}: the whole run of {v}s is jumped in one step."
            sub = ("prev stays on " + lab(p) + ": " + lab(c) + " might start another run, so it hasn't proved itself yet."
                   if c is not None else "curr ran off the end, so this cuts the list after " + lab(p) + ".")
            if c is None and 'tail' in notes:
                sub = notes['tail']
            hold = KEY if first or c is None else STEP
        elif k == 'keeper':
            nx = e['nxt'][c]
            cap = (f"curr is {lab(c)}; the next node is {lab(nx)}, a different value. {lab(c)} is a keeper." if nx is not None
                   else f"curr is {lab(c)} and nothing comes after it, so it can't start a run. {lab(c)} is a keeper.")
            sub = notes.get(('keeper', c), "")
            hold = KEY if ('keeper', c) in notes else STEP
        elif k == 'step':
            cap, sub, hold = (f"prev moves onto {lab(p)}, curr onto {lab(c)}.", "", QUICK * 2)
        else:
            cap, sub, hold = (f"curr is null: done. Return D.next: [{', '.join(order)}].",
                              notes.get('done', "curr passed every node once: O(n) time, and only two pointers: O(1) space."), END)
        ptr_line = f"prev = {lab(p)}    curr = {lab(c)}" if k != 'done' else "prev and curr are finished"
        sc.frame([view, text, TextView([ptr_line], size=16)], cap, sub, hold,
                 counters={'removed': len(e['gone'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert to_list(Solution().deleteDuplicates(make(HARD_TAIL))) == [1, 2]
    assert to_list(no_cut(make(HARD_TAIL))) == [1, 2, 3, 3, 4, 4]
    assert to_list(Solution().deleteDuplicates(make(HARD_ZERO))) == [0, 3]
    assert to_list(dummy_as_before(make(HARD_ZERO))) == [3]
    tail = build(HARD_TAIL, f'head = {HARD_TAIL}. Answer [1, 2]. The list ends in runs, so the last keeper must be cut loose.', {
        'start': "Both LeetCode samples end on a keeper. This one ends on two runs.",
        'tail': "curr ran off the end, so 2.next = null. A version that strings keepers onto a tail and never cuts it leaves 2 -> 3 -> 3 -> 4 -> 4.",
        'done': "Answer [1, 2]. The tail-building version returned the whole input, because 2.next still pointed at the old 3s.",
    })
    zero = build(HARD_ZERO, f'head = {HARD_ZERO}. Answer [0, 3]. The head is a 0, the same value as the dummy.', {
        'start': "The dummy holds a 0 and so does the head. This solution never compares the dummy's value.",
        ('keeper', 1): "Kept by comparing with the NEXT node only. A version that also compares with the node before, using the dummy as that node, sees 0 = 0 and deletes it.",
        'run2': "Back-to-back runs: the 2s start right after the 1s, which is why prev stayed on 0.",
        'done': "Answer [0, 3]. Treating the dummy as the head's left neighbour returned [3].",
    })
    return [
        (tail, "[1,2,3,3,4,4]: both LeetCode samples end on a keeper, so a first attempt that strings keepers onto a tail "
               "and forgets to cut it passes them, then returns this list unchanged. The answer is [1, 2]."),
        (zero, "[0,1,1,1,2,2,3]: the head is 0, the dummy's value. A first attempt that keeps a node only if it differs from "
               "the node before it, using the dummy as that node, deletes the 0 and returns [3]. The answer is [0, 3]."),
    ]


def main():
    args = cli()
    sc = build(VALUES, f'head = {VALUES}. Delete every value that appears more than once, all copies of it.')
    finish(sc, 82, "Watch prev after the 3s are jumped: it stays on 2, because the 4s straight after them "
                   "are a run too and need 2 to relink from.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
