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

# The hard example (interactive page only): n equals the length, so the node to
# remove is the head. Returning `head` instead of `sentinel.next` hands back
# [1,2,3], because node 1 still points at 2; and without a sentinel, fast falls
# off the end during the head start and `fast.next` crashes. Answer [2,3].
# Notes are keyed by event number and replace that frame's second caption line.
HARD_VALUES, HARD_N = [1, 2, 3], 3
HARD_NOTES = {
    0: "n is the whole length, so the node to remove is the head itself.",
    4: "Without a sentinel, fast starts on 1 and is null after 3 steps, so the next fast.next crashes.",
    5: "S is the only node in front of the head. It's what lets the head be unlinked like any other node.",
    6: "Node 1 still points at 2, so returning head gives [1,2,3]. S.next gives [2,3].",
}


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

        if not fast:
            rec('skipped', slow=slow, fast=fast)    # the loop below won't run at all
        while fast:
            fast = fast.next
            slow = slow.next
            rec('together', slow=slow, fast=fast)

        slow.next = slow.next.next
        rec('unlink', slow=slow)
        return sentinel.next

    removeNthFromEnd(nodes[0], n)
    return events


def ordinal(n):
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"


def words(e, k_ahead, last_ahead, values=VALUES, n=N):
    k, p = e['kind'], e['ptrs']
    lab = lambda i: 'S' if i == 0 else ('null' if i is None else str(values[i - 1]))
    tv = values[len(values) - n]
    if k == 'start':
        return (f"Remove the {ordinal(n)} node from the end (the {tv}). Both pointers start on the sentinel S.",
                "S sits in front of the head, so even the head has a node before it.", KEY)
    if k == 'ahead':
        if last_ahead:
            return (f"fast is now {n} + 1 = {n + 1} nodes ahead of slow.",
                    "Why +1? Unlinking needs the node BEFORE the target, so slow must stop one short.", KEY)
        return (f"Head start: fast moves alone, step {k_ahead} of {n + 1}.", "", STEP)
    if k == 'together':
        if p['fast'] is None:
            return (f"fast has fallen off the end. slow is on {lab(p['slow'])}, one before the {tv}.",
                    "The gap never changed, so slow is exactly n + 1 behind the end.", KEY)
        return (f"Move both: fast to {lab(p['fast'])}, slow to {lab(p['slow'])}. The gap stays the same.",
                "", STEP)
    if k == 'skipped':
        return (f"fast is already null, so the loop doesn't run. slow stays on {lab(p['slow'])}, one before the {tv}.",
                "", KEY)
    return (f"Unlink: {lab(p['slow'])}.next = {lab(e['nxt'][p['slow']])}. The {tv} is skipped.",
            "Return S.next, not head: if the head had been removed, head would still point at it.", END)


def build(values, n, subtitle, notes=None):
    sc = Scene('#19 Remove Nth Node From End of List', subtitle)
    legend = [(style('muted')[1], 'sentinel'), (style('bad')[1], 'the node to remove'),
              (style('good')[1], 'where slow stops'), (ACTIVE, 'pointer')]
    target = len(values) - n + 1                 # display index of the node to remove
    events = trace(values, n)
    n_ahead = 0
    for idx, e in enumerate(events):
        k = e['kind']
        n_ahead += k == 'ahead'
        last_ahead = k == 'ahead' and (idx + 1 == len(events) or events[idx + 1]['kind'] != 'ahead')
        styles = {0: 'muted', target: 'bad'}
        if (k == 'together' and e['ptrs']['fast'] is None) or k in ('unlink', 'skipped'):
            styles[e['ptrs']['slow']] = 'good'
        cut = {target} if k == 'unlink' else set()
        if k == 'unlink':
            styles[target] = 'muted'
        ptrs = dict(e['ptrs'])
        view = ListView(['S'] + values, e['nxt'], styles, ptrs, cut=cut)
        gap = None
        if 'fast' in ptrs and 'slow' in ptrs:
            f = ptrs['fast'] if ptrs['fast'] is not None else len(values) + 1
            gap = f - ptrs['slow']
        order, i = [], e['nxt'][0]
        while i is not None:
            order.append(str(values[i - 1]))
            i = e['nxt'][i]
        lines = [f"list from S.next:  {' -> '.join(order)} -> null"]
        if notes is not None:
            order, i = [], 1
            while i is not None:
                order.append(str(values[i - 1]))
                i = e['nxt'][i]
            lines.append(f"list from head:    {' -> '.join(order)} -> null")
        text = TextView(lines, size=16)
        rows = [(name, 'null' if v is None else ('S' if v == 0 else f'node {values[v - 1]}'))
                for name, v in ptrs.items()]
        if gap is not None:
            rows.append(('gap', f'{gap} steps', 'gold'))
        cap, sub, hold = words(e, n_ahead, last_ahead, values, n)
        if notes and idx in notes:
            sub, hold = notes[idx], (END if k == 'unlink' else KEY)
        sc.frame([view, text], cap, sub, hold,
                 side=MapView(rows, 'Pointers', headers=('name', 'on'), empty='(none)'),
                 counters={'n': n}, legend=legend)
    return sc


def hard():
    """Harder input for the interactive page (scripts/motion_build.py)."""
    sc = build(HARD_VALUES, HARD_N, f'head = {HARD_VALUES}, n = {HARD_N}. The node to remove is the head.',
               HARD_NOTES)
    return sc, ("n = 3 on a 3-node list removes the head. Return head instead of sentinel.next and you get "
                "[1,2,3] back, because node 1 still points at 2; skip the sentinel and fast.next crashes. "
                "Answer: [2,3].")


def main():
    args = cli()
    sc = build(VALUES, N, f'head = {VALUES}, n = {N}. A fixed gap between two pointers finds the end in one pass.')
    finish(sc, 19, "Watch fast fall off the end: because it started n + 1 ahead, slow is left one node "
                   "before the 4, which is exactly where the unlink needs it.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
