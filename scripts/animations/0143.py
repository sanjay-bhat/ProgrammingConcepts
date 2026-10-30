#!/usr/bin/env python3
"""#143 Reorder List: find the middle, cut, reverse the second half, zip.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Nodes keep their original position
as an id, so every frame is drawn from the real `next` pointers.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

VALUES = [1, 2, 3, 4, 5]          # LeetCode example 2


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def trace(values):
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    ids = {id(n): i for i, n in enumerate(nodes)}
    events = []

    def rec(kind, **ptrs):
        events.append(dict(kind=kind,
                           nxt=[ids[id(n.next)] if n.next else None for n in nodes],
                           ptrs={k: (ids[id(v)] if v else None) for k, v in ptrs.items()}))

    # ---- the notebook's solution, with rec() calls added ----
    def reorderList(head):
        if not head or not head.next:
            return
        slow, fast = head, head
        rec('start', slow=slow, fast=fast)
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            rec('walk', slow=slow, fast=fast)
        rec('mid', slow=slow, fast=fast)
        prev, cur = None, slow.next
        slow.next = None
        rec('cut', slow=slow, cur=cur)
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
            rec('flip', prev=prev, cur=cur)
        first, second = head, prev
        rec('merge0', first=first, second=second)
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            rec('splice', first=first, second=second)
        rec('done', head=head)

    reorderList(nodes[0])
    return events


def walk(nxt, start=0):
    out, i = [], start
    while i is not None and len(out) <= len(nxt):
        out.append(i)
        i = nxt[i]
    return out


def words(e, n_flip, n_splice):
    k, p, V = e['kind'], e['ptrs'], VALUES
    v = lambda key: V[p[key]] if p.get(key) is not None else 'null'
    if k == 'start':
        return ("Goal: first, last, second, second-to-last... = 1 5 2 4 3.",
                "That's the first half zipped with the second half backwards. Step 1: find the middle.", KEY)
    if k == 'walk':
        return (f"slow moves one node (to {v('slow')}), fast moves two (to {v('fast')}).",
                "", STEP)
    if k == 'mid':
        return (f"fast can't take two more steps, so stop. slow is on {v('slow')}: the end of the first half.",
                "With an odd length the middle node stays in the first half. It'll end up last.", KEY)
    if k == 'cut':
        return (f"Cut: {v('slow')}.next = null. The first half now really ends at {v('slow')}.",
                "Skip this and the finished list loops forever: its last node still points back inside.", KEY)
    if k == 'flip':
        if n_flip == 1:
            return (f"Reverse the second half: {v('prev')} now points backwards, at null.",
                    "Save cur.next first, or the rest of the list is lost when the arrow flips.", KEY)
        return (f"{v('prev')} now points back at the node before it." +
                (" Second half reversed: 5 -> 4." if p.get('cur') is None else ""), "", STEP)
    if k == 'merge0':
        return ("Two lists now: 1 -> 2 -> 3 and 5 -> 4. Zip them, one node from each.",
                "Taking from the back has become taking from the front, which lists are good at.", KEY)
    if k == 'splice':
        if n_splice == 1:
            return ("Splice 5 in after 1: save both nexts, then 1 -> 5 -> 2.",
                    "Both next fields get overwritten in the same round, so both are saved first.", KEY)
        if p.get('second') is None:
            return ("Splice 4 in after 2. The second half is empty, so the zip stops.",
                    "3 is already last, and the cut already pointed it at null.", STEP)
        return ("Splice the next second-half node in.", "", STEP)
    return ("Done: 1 -> 5 -> 2 -> 4 -> 3, built by relinking the original nodes.",
            "Three passes over the list and a handful of pointers: O(n) time, O(1) space.", END)


def main():
    args = cli()
    sc = Scene('#143 Reorder List: middle, reverse, merge',
               f'head = {VALUES}. Relink nodes into first, last, second, second-to-last...')
    legend = [(style('window')[1], 'first half'), (style('gold')[1], 'second half'),
              (ACTIVE, 'pointer')]
    events = trace(VALUES)
    mid = next(e['ptrs']['slow'] for e in events if e['kind'] == 'mid')
    n_flip = n_splice = 0
    for e in events:
        k = e['kind']
        n_flip += k == 'flip'
        n_splice += k == 'splice'
        cutdone = k not in ('start', 'walk', 'mid')
        styles = {i: ('window' if i <= mid else 'gold') if cutdone else 'plain' for i in range(len(VALUES))}
        if k == 'done':
            styles = {i: 'good' for i in range(len(VALUES))}
        ptrs = {name: i for name, i in e['ptrs'].items() if name != 'head'}
        views = [ListView(VALUES, e['nxt'], styles, ptrs)]
        order = walk(e['nxt'])
        fmt = lambda idx: ' -> '.join(str(VALUES[i]) for i in idx) + ' -> null'
        lines = [f'from head:      {fmt(order)}']
        if k == 'flip':
            lines.append(f"reversed part:  {fmt(walk(e['nxt'], e['ptrs']['prev']))}")
            if e['ptrs']['cur'] is not None:
                lines.append(f"still to flip:  {fmt(walk(e['nxt'], e['ptrs']['cur']))}")
        elif k == 'cut':
            lines.append(f"cut off:        {fmt(walk(e['nxt'], e['ptrs']['cur']))}")
        elif k in ('merge0', 'splice') and e['ptrs'].get('second') is not None:
            lines.append(f"second half:    {fmt(walk(e['nxt'], e['ptrs']['second']))}")
        if k in ('splice', 'done'):
            # the same nodes laid out in reading order, since the arcs above get crowded
            views.append(TextView([], title='The same nodes, in reading order from head'))
            views.append(ListView([VALUES[i] for i in order], None,
                                  {j: styles[i] for j, i in enumerate(order)}))
            lines = lines[1:]
        if lines:
            views.append(TextView(lines, title='Reading the chains', size=16))
        rows = [(name, 'null' if i is None else f'node {VALUES[i]}') for name, i in e['ptrs'].items()
                if name != 'head']
        phase = {'start': 'find middle', 'walk': 'find middle', 'mid': 'find middle', 'cut': 'cut',
                 'flip': 'reverse', 'merge0': 'merge', 'splice': 'merge', 'done': 'done'}[k]
        cap, sub, hold = words(e, n_flip, n_splice)
        sc.frame(views, cap, sub, hold,
                 side=MapView(rows, 'Pointers', headers=('name', 'points at'), empty='(none)'),
                 counters={'step': phase}, legend=legend)
    finish(sc, 143, "Watch the cut after node 3: it's one line, and it's what stops the finished list "
                    "from pointing back into itself.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
