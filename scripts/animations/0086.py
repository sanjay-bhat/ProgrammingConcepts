#!/usr/bin/env python3
"""#86 Partition List: two chains behind dummy heads, then cut the big tail and join.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Dummy nodes are drawn as 'D'.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

VALUES, X = [1, 4, 3, 2, 5, 2], 3               # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_CYCLE = ([100, -100, 100, -100, 99], 100)  # [-100,-100,99,100,100]; skipping hi.next = None makes a cycle
HARD_EMPTY = ([5, 9, 7, 5], 5)                  # [5,9,7,5]; head/tail pairs without dummies crash: nothing is < 5


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def partition(self, head, x: int):
        lo_dummy = ListNode(0)
        hi_dummy = ListNode(0)
        lo = lo_dummy
        hi = hi_dummy
        curr = head
        while curr:
            if curr.val < x:
                lo.next = curr
                lo = lo.next
            else:
                hi.next = curr
                hi = hi.next
            curr = curr.next
        hi.next = None
        lo.next = hi_dummy.next
        return lo_dummy.next


def make(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head, cap=50):
    out = []
    while head and len(out) < cap:
        out.append(head.val)
        head = head.next
    return out, head is not None          # (values, still going = a cycle)


def no_cut(head, x):
    """First attempt: everything right except the hi.next = None line."""
    lo_d, hi_d = ListNode(0), ListNode(0)
    lo, hi = lo_d, hi_d
    while head:
        if head.val < x:
            lo.next = head
            lo = head
        else:
            hi.next = head
            hi = head
        head = head.next
    lo.next = hi_d.next
    return lo_d.next


def no_dummies(head, x):
    """First attempt: a head and tail per chain with None checks, no dummy nodes."""
    lo_h = lo_t = hi_h = hi_t = None
    while head:
        if head.val < x:
            if lo_h is None:
                lo_h = lo_t = head
            else:
                lo_t.next = head
                lo_t = head
        else:
            if hi_h is None:
                hi_h = hi_t = head
            else:
                hi_t.next = head
                hi_t = head
        head = head.next
    hi_t.next = None
    lo_t.next = hi_h          # lo_t is None when nothing was < x
    return lo_h


def trace(values, x):
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    head = nodes[0] if nodes else None
    events, lo_chain, hi_chain = [], [], []
    idx = {id(n): i for i, n in enumerate(nodes)}

    def rec(kind, **kw):
        stale = idx.get(id(hi.next)) if hi.next is not None else None
        events.append(dict(kind=kind, lo=list(lo_chain), hi=list(hi_chain),
                           curr=idx.get(id(curr)) if curr else None, stale=stale, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    lo_dummy = ListNode(0)
    hi_dummy = ListNode(0)
    lo = lo_dummy
    hi = hi_dummy
    curr = head
    rec('start')
    while curr:
        if curr.val < x:
            lo.next = curr
            lo = lo.next
            lo_chain.append(idx[id(curr)])
            rec('small', node=idx[id(curr)])
        else:
            hi.next = curr
            hi = hi.next
            hi_chain.append(idx[id(curr)])
            rec('big', node=idx[id(curr)])
        curr = curr.next
    rec('end')
    hi.next = None
    rec('cut')
    lo.next = hi_dummy.next
    rec('join')
    got, _ = to_list(lo_dummy.next)
    assert got == to_list(Solution().partition(make(values), x))[0]
    return events


def build(values, x, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#86 Partition List: two chains behind dummies', subtitle)
    legend = [(style('window')[1], f'less than {x}'), (style('land')[1], f'{x} or more'),
              (style('gold')[1], 'dummy D'), (style('active')[1], 'curr'), (REJECT, 'old link still there')]
    kind = lambda i: 'window' if values[i] < x else 'land'
    seen = set()
    for e in trace(values, x):
        k = e['kind']
        start = e['curr']
        if start is not None and k in ('small', 'big'):
            start += 1                     # this node has just been moved; curr steps on next
        rest = [] if start is None or start >= len(values) else list(range(start, len(values)))
        # still-to-visit row: the original list from curr onwards
        rv = [values[i] for i in rest]
        rst = {j: kind(i) for j, i in enumerate(rest)}
        if rest and k == 'start':
            rst[0] = 'active'
        views = [ListView(rv, styles=rst, title='to visit', room=8) if rest else
                 TextView(['to visit:  (nothing left)'], size=16)]
        if k != 'join':
            for name, chain, lab in (('lo', e['lo'], f'< {x}  '), ('hi', e['hi'], f'>= {x} ')):
                vals = ['D'] + [values[i] for i in chain]
                st = {0: 'gold', **{j + 1: kind(i) for j, i in enumerate(chain)}}
                extra = []
                if name == 'hi' and e['stale'] is not None and k in ('end', 'big', 'small'):
                    st[len(vals) - 1] = 'bad' if k == 'end' else st[len(vals) - 1]
                if k in ('small', 'big') and ((name == 'lo') == (k == 'small')):
                    st[len(vals) - 1] = 'active'
                # a chain's last node keeps its old next until it's cut, so no 'null' is drawn yet
                ends = name == 'hi' and k == 'cut'
                views.append(ListView(vals, styles=st, title=lab, room=8, null=ends))
            if e['stale'] is not None and k == 'end':
                views.append(TextView([(f"big tail {values[e['hi'][-1]]} still points at {values[e['stale']]} (its old next)", 'bad')], size=16))
        else:
            order = e['lo'] + e['hi']
            vals = ['D'] + [values[i] for i in order]
            st = {0: 'gold', **{j + 1: 'good' for j in range(len(order))}}
            views.append(ListView(vals, styles=st, title='answer ', room=8))
        if k == 'start':
            cap, sub, hold = (f"Two empty chains, each just a dummy D: values below {x}, and values {x} or more.",
                              notes.get('start', "Each node will be unhooked and added to the back of one chain."), KEY)
        elif k in ('small', 'big'):
            v = values[e['node']]
            side = f"less than {x}" if k == 'small' else f"{x} or more"
            cap = f"{v} is {side}: add it to the back of that chain."
            sub = ""
            first = k not in seen
            seen.add(k)
            if v == x:
                sub, first = f"Equal to {x} isn't less than {x}, so it goes right.", True
            elif first:
                sub = "Joining at the back keeps the original order inside each chain."
            hold = KEY if first and v == x else (STEP if first else QUICK * 2)
        elif k == 'end':
            if e['stale'] is not None:
                cap = f"Every node is placed. But the last big node, {values[e['hi'][-1]]}, still points at {values[e['stale']]}."
                sub = notes.get('end', "Nodes were moved, not copied, so it kept its old next.")
            else:
                cap, sub = ("Every node is placed.", "The big chain's last node already ends in null here.")
            hold = KEY if e['stale'] is not None else STEP
        elif k == 'cut':
            cap = "hi.next = None: the big chain now ends cleanly."
            sub = notes.get('cut', "Without this, joining the chains would make the list loop back on itself.")
            hold = KEY
        else:
            out = [values[i] for i in e['lo'] + e['hi']]
            cap = f"lo.next = big dummy's next: the chains are joined. Return D.next: {out}."
            sub = notes.get('join', "One walk, each node moved once: O(n) time, two dummies: O(1) space.")
            hold = END
        sc.frame(views, cap, sub, hold,
                 counters={f'< {x}': len(e['lo']), f'>= {x}': len(e['hi'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    (v1, x1), (v2, x2) = HARD_CYCLE, HARD_EMPTY
    assert to_list(Solution().partition(make(v1), x1)) == ([-100, -100, 99, 100, 100], False)
    assert to_list(no_cut(make(v1), x1))[1]                      # never reaches null: a cycle
    assert to_list(Solution().partition(make(v2), x2)) == ([5, 9, 7, 5], False)
    try:
        no_dummies(make(v2), x2)
        raise AssertionError('no_dummies should crash on an empty small chain')
    except AttributeError:
        pass
    cyc = build(v1, x1, f'head = {v1}, x = {x1}. Answer [-100, -100, 99, 100, 100]. Skipping the cut makes a cycle.', {
        'start': "The values alternate between the two sides, so old links cross from one chain into the other.",
        'end': "That -100 is in the small chain now. Join the chains like this and the list loops: ..., 100, 100, -100, 99, 100, ...",
        'cut': "The one line that stops the cycle. A version without it never reaches null when you read the answer.",
    })
    emp = build(v2, x2, f'head = {v2}, x = {x2}. Answer [5, 9, 7, 5]. Nothing is less than 5.', {
        'start': "Nothing here is less than 5, and the 5s are equal to x, so every node goes right.",
        'join': "The small chain is only its dummy, so the dummy links straight to 5. Without dummies, its tail is None here and lo_tail.next crashes.",
    })
    return [
        (cyc, "[100,-100,100,-100,99], x = 100: the last big node still points at a -100 that has moved to the small chain. "
              "A first attempt that skips hi.next = None returns a list that loops forever."),
        (emp, "[5,9,7,5], x = 5: no value is less than 5, so the small chain stays empty. A first attempt with a head and tail "
              "per chain instead of dummies passes both samples, then crashes here. The answer is [5, 9, 7, 5]."),
    ]


def main():
    args = cli()
    sc = build(VALUES, X, f'head = {VALUES}, x = {X}. Values below {X} first, each group in its original order.')
    finish(sc, 86, "Watch the end: the last big node, 5, still points at the final 2, which is now in the small chain. "
                   "hi.next = None cuts that link before the chains are joined.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
