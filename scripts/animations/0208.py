#!/usr/bin/env python3
"""#208 Implement Trie: one walk from the root, letter by letter. insert creates
missing nodes and flags the last one; search needs the flag, startsWith doesn't.

The trace comes from running the notebook's Python Trie with a recorder added;
the algorithm lines are unchanged. The calls are LeetCode's example sequence.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

OPS = [('insert', 'apple'), ('search', 'apple'), ('search', 'app'),
       ('startsWith', 'app'), ('insert', 'app'), ('search', 'app')]   # LeetCode example 1


def trace(ops):
    events, log = [], []
    name = {}            # id(node) -> the prefix its path spells ('' for the root)
    st = {'op': None, 'at': None, 'walked': '', 'trie': None}

    def snapshot():
        nodes, ends = {}, set()

        def walk(n, pre):
            nodes[pre] = sorted(n.children)
            if n.is_end:
                ends.add(pre)
            for ch, kid in n.children.items():
                walk(kid, pre + ch)
        walk(st['trie'].root, '')
        return nodes, ends

    def rec(kind, **kw):
        nodes, ends = snapshot()
        events.append(dict(kind=kind, op=st['op'], at=st['at'], walked=st['walked'], nodes=nodes,
                           ends=ends, log=list(log), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    class TrieNode:
        def __init__(self):
            self.children: dict[str, 'TrieNode'] = {}
            self.is_end = False

    class Trie:
        def __init__(self):
            self.root = TrieNode()
            name[id(self.root)] = ''

        def insert(self, word: str) -> None:
            node = self.root
            for c in word:
                created = False
                if c not in node.children:
                    node.children[c] = TrieNode()
                    name[id(node.children[c])] = name[id(node)] + c; created = True
                node = node.children[c]
                st['at'], st['walked'] = name[id(node)], name[id(node)]
                rec('step', c=c, created=created)
            node.is_end = True
            rec('flag', node=name[id(node)])

        def search(self, word: str) -> bool:
            node = self._find(word)
            return node is not None and node.is_end

        def startsWith(self, prefix: str) -> bool:
            return self._find(prefix) is not None

        def _find(self, s: str) -> TrieNode | None:
            node = self.root
            for c in s:
                if c not in node.children:
                    rec('missing', c=c)
                    return None
                node = node.children[c]
                st['at'], st['walked'] = name[id(node)], name[id(node)]
                rec('step', c=c, created=False)
            return node

    st['trie'] = Trie()
    for op, arg in ops:
        st['op'], st['at'], st['walked'] = (op, arg), '', ''
        rec('call')
        if op == 'insert':
            st['trie'].insert(arg)
            log.append((f'insert("{arg}")', 'null'))
            rec('return', result=None)
        else:
            res = getattr(st['trie'], op)(arg)
            log.append((f'{op}("{arg}")', str(res).lower(), 'good' if res else 'bad'))
            rec('return', result=res)
    st['op'], st['at'], st['walked'] = None, None, ''
    rec('done')
    return events


def layout(nodes):
    """Vertical chain(s): depth top to bottom; siblings spread sideways."""
    pos, depth = {}, {}
    leaves = []

    def walk(pre, d):
        depth[pre] = d
        kids = nodes[pre]
        if not kids:
            leaves.append(pre)
        for ch in kids:
            walk(pre + ch, d + 1)
    walk('', 0)
    maxd = max(depth.values()) or 1
    order = {}

    def x(pre):
        kids = nodes[pre]
        if not kids:
            order[pre] = leaves.index(pre)
        else:
            order[pre] = sum(x(pre + ch) for ch in kids) / len(kids)
        return order[pre]
    x('')
    span = max(1, len(leaves) - 1)
    for pre in nodes:
        pos[pre] = (0.5 if len(leaves) == 1 else 0.3 + 0.4 * order[pre] / span, 0.92 * depth[pre] / max(5, maxd))
    return pos


def words(e):
    k = e['kind']
    op, arg = e['op'] or (None, None)
    if k == 'call':
        if op == 'insert':
            return (f'insert("{arg}"): walk from the root, creating any letter that is missing.', '', STEP)
        if op == 'search':
            return (f'search("{arg}"): walk the letters, then the last node must be flagged as a word end.', '', STEP)
        return (f'startsWith("{arg}"): walk the letters. If the path exists, that is enough.', '', STEP)
    if k == 'step':
        if e['created']:
            return (f"'{e['c']}' isn't there yet: create it, then step into it.", "", QUICK * 2)
        if op == 'insert':
            return (f"'{e['c']}' already exists (shared prefix): just step into it.",
                    "No new node: 'app' reuses the path 'apple' made.", STEP if e['walked'] == 'a' else QUICK * 2)
        return (f"Follow '{e['c']}': now at \"{e['walked']}\".", "", QUICK * 2)
    if k == 'flag':
        if e['node'] == 'app':
            return ('Set the end flag on "app". Nothing was created: only the flag changed.',
                    'Now "app" counts as a word, not just a prefix.', KEY)
        return (f'Out of letters: set the end flag on "{e["node"]}", and only there.',
                'Setting it inside the loop would make every prefix a word.', STEP)
    if k == 'missing':
        return (f"No '{e['c']}' child: the walk falls off, so the answer is false.", "", STEP)
    if k == 'return':
        if op == 'insert':
            return (f'insert("{arg}") is done.', '', QUICK * 2)
        if op == 'search' and arg == 'app' and not e['result']:
            return ('The "app" node exists, but its end flag is off. search returns false.',
                    'It exists only because "apple" runs through it.', KEY)
        if op == 'startsWith':
            return ('The path a-p-p exists, so startsWith returns true. No flag needed.',
                    'Same walk as search; the only difference is that one check.', KEY)
        if op == 'search' and arg == 'app':
            return ('Same walk as before, and this time the flag is on. search returns true.', '', KEY)
        return (f'Landed on "{arg}" and its flag is on: search returns {str(e["result"]).lower()}.', '', STEP)
    return ('All six calls done: null, true, false, true, null, true.',
            'Every call cost one step per letter of its own word: O(L).', END)


def main():
    args = cli()
    sc = Scene('#208 Implement Trie: one edge per letter, a flag for word ends',
               'Green node: a word ends here. Orange path: the walk for the current call.')
    legend = [(ACTIVE, 'current node'), (style('good')[1], 'end of a word'),
              (style('window')[1], 'on the current walk')]
    final = trace(OPS)[-1]['nodes']
    pos_all = layout(final)
    for e in trace(OPS):
        nodes = e['nodes']
        ids = list(nodes)
        pos = {p: pos_all[p] for p in ids}
        edges = [(p, p + ch) for p in ids for ch in nodes[p]]
        walked = e['walked']
        on = {walked[:i] for i in range(len(walked) + 1)} if e['op'] else set()
        styles = {}
        for p in ids:
            if p in e['ends']:
                styles[p] = 'good'
            elif p in on:
                styles[p] = 'window'
        estyles = {(walked[:i], walked[:i + 1]): 'active' for i in range(len(walked))}
        labels = {}
        text = {p: (p[-1] if p else 'root') for p in ids}
        rings = [(e['at'], ACTIVE)] if e['at'] is not None and e['at'] in pos and e['kind'] != 'done' else []
        g = GraphView(pos, edges, styles=styles, edge_styles=estyles, labels=labels, rings=rings, text=text)
        op = e['op']
        head = (f'{op[0]}("{op[1]}")' if op else 'all calls finished')
        log = list(e['log'])
        if op and e['kind'] != 'return':
            log.append((head, '…', 'active'))
        cap, sub, hold = words(e)
        sc.frame(g, cap, sub, hold, side=MapView(log, 'Calls so far', headers=('call', 'returns'),
                                                 empty='(no calls yet)'),
                 counters={'nodes': len(ids) - 1}, legend=legend)
    finish(sc, 208, 'Watch search("app") right after inserting "apple": the walk succeeds, but the node\'s '
                    'end flag is off, so the answer is false. startsWith("app") takes the same walk and says true.',
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
