#!/usr/bin/env python3
"""#211 Add and Search Words: a trie, searched recursively. A letter follows one
child; a dot tries every child and comes back when one is a dead end.

The trace comes from running the notebook's Python WordDictionary with a recorder
added; the algorithm lines are unchanged. The calls are LeetCode's example, plus
addWord("pit") and search(".it") at the end: in LeetCode's example the dot's first
child always works, so it never shows a dead end being backed out of.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

OPS = [('addWord', 'bad'), ('addWord', 'dad'), ('addWord', 'mad'),
       ('search', 'pad'), ('search', 'bad'), ('search', '.ad'), ('search', 'b..'),   # LeetCode example 1
       ('addWord', 'pit'), ('search', '.it')]                                        # shows a dead end


def trace(ops):
    events, calls, log = [], [], []
    name = {}
    st = {'op': None, 'd': None, 'tried': {}}

    def snapshot():
        nodes, ends = {}, set()

        def walk(n, pre):
            nodes[pre] = list(n.children)
            if n.is_end:
                ends.add(pre)
            for ch, kid in n.children.items():
                walk(kid, pre + ch)
        walk(st['d'].root, '')
        return nodes, ends

    def rec(kind, **kw):
        nodes, ends = snapshot()
        events.append(dict(kind=kind, op=st['op'], calls=[tuple(c) for c in calls], nodes=nodes, ends=ends,
                           tried=dict(st['tried']), log=list(log), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False

    class WordDictionary:
        def __init__(self):
            self.root = TrieNode()
            name[id(self.root)] = ''

        def addWord(self, word: str) -> None:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                    name[id(node.children[c])] = name[id(node)] + c
                node = node.children[c]
            node.is_end = True

        def search(self, word: str) -> bool:
            def dfs(i, node):
                calls.append((i, name[id(node)]))
                if i == len(word):
                    st['tried'][name[id(node)]] = node.is_end
                    rec('end', i=i, node=name[id(node)], ok=node.is_end)
                    calls.pop()
                    return node.is_end
                if word[i] == '.':
                    rec('dot', i=i, node=name[id(node)], kids=list(node.children))
                    r = any(dfs(i + 1, child) for child in node.children.values())
                    calls.pop()
                    return r
                if word[i] not in node.children:
                    st['tried'][name[id(node)]] = False
                    rec('missing', i=i, node=name[id(node)], c=word[i])
                    calls.pop()
                    return False
                rec('follow', i=i, node=name[id(node)], c=word[i])
                r = dfs(i + 1, node.children[word[i]])
                calls.pop()
                return r
            return dfs(0, self.root)

    st['d'] = WordDictionary()
    for op, arg in ops:
        st['op'], st['tried'] = (op, arg), {}
        if op == 'addWord':
            st['d'].addWord(arg)
            log.append((f'addWord("{arg}")', 'null'))
            rec('added', word=arg)
        else:
            rec('call')
            res = st['d'].search(arg)
            log.append((f'search("{arg}")', str(res).lower(), 'good' if res else 'bad'))
            rec('result', res=res)
    st['op'] = None
    rec('done')
    return events


def words(e):
    k, (op, arg) = e['kind'], (e['op'] or (None, None))
    if k == 'added':
        extra = {'bad': "Each edge is one letter; a green node marks a word end.",
                 'pit': "Not in LeetCode's example: added so a dot hits dead ends before it succeeds."}.get(arg, '')
        return (f'addWord("{arg}"): walk the letters, create what is missing, flag the last node.',
                extra, STEP if arg in ('bad', 'pit') else QUICK * 2.5)
    if k == 'call':
        if '.' in arg:
            return (f'search("{arg}"): a dot can be any letter, so it may have to try several children.', '', STEP)
        return (f'search("{arg}"): no dots, so there is only one path to follow.', '', STEP)
    if k == 'follow':
        return (f"Pattern letter '{e['c']}': follow that one child.", '', QUICK * 2)
    if k == 'missing':
        if arg == '.it':
            return (f"\"{e['node']}\" has no '{e['c']}' child. Dead end, but that's not the final answer:",
                    "the dot above goes back and tries its next child.", KEY if e['node'] == 'b' else STEP)
        return (f"No '{e['c']}' child here: this path fails.", '', STEP)
    if k == 'dot':
        kids = ', '.join(e['kids'])
        return (f"A dot at position {e['i']}: try every child in turn ({kids}).",
                "Stop at the first one that leads to a match.", STEP)
    if k == 'end':
        if e['ok']:
            return (f'Pattern used up on "{e["node"]}", and a word ends here: match.', '', STEP)
        return (f'Pattern used up on "{e["node"]}", but no word ends here: no match.', '', STEP)
    if k == 'result':
        r = str(e['res']).lower()
        if arg == '.it':
            return (f'search(".it") returns {r}: three dead ends, then p-i-t matched.',
                    'Recursion is what let the dot come back and try the next child.', KEY)
        if arg == '.ad':
            return (f'search(".ad") returns {r}. The first child b already matched,',
                    'so any() stops and never looks at d or m.', KEY)
        return (f'search("{arg}") returns {r}.', '', STEP)
    return ('All calls done: pad false, bad true, .ad true, b.. true, .it true.',
            'Letters never fan out; only a dot multiplies the paths, by at most 26.', END)


def layout(nodes):
    leaves, xs, depth = [], {}, {}

    def walk(p, d):
        depth[p] = d
        if not nodes[p]:
            xs[p] = len(leaves); leaves.append(p)
        else:
            for ch in nodes[p]:
                walk(p + ch, d + 1)
            xs[p] = (xs[p + nodes[p][0]] + xs[p + nodes[p][-1]]) / 2
    walk('', 0)
    span = max(1, len(leaves) - 1)
    return {p: (0.08 + 0.84 * xs[p] / span, depth[p] / 3) for p in nodes}


def main():
    args = cli()
    sc = Scene('#211 Add and Search Words: a dot tries every child',
               'Green node: a word ends here. Orange: the walk in progress. Red: tried and failed.')
    legend = [(ACTIVE, 'current node'), (style('good')[1], 'word end / matched'), (style('bad')[1], 'dead end')]
    evs = trace(OPS)
    pos_all = layout(evs[-1]['nodes'])
    for e in evs:
        nodes = e['nodes']
        pos = {p: pos_all[p] for p in nodes}
        edges = [(p, p + ch) for p in nodes for ch in nodes[p]]
        styles = {p: 'good' for p in e['ends']}
        for p, ok in e['tried'].items():
            styles[p] = 'good' if ok else 'bad'
        path = [c[1] for c in e['calls']]
        for p in path:
            if styles.get(p) != 'bad':
                styles[p] = 'window' if p not in e['ends'] else 'good'
        estyles = {(path[j], path[j + 1]): 'active' for j in range(len(path) - 1)}
        cur = e.get('node')
        rings = [(cur, ACTIVE)] if cur is not None else []
        text = {p: (p[-1] if p else 'root') for p in nodes}
        g = GraphView(pos, edges, styles=styles, edge_styles=estyles, rings=rings, text=text, height=250)
        views = [g]
        op = e['op']
        if op and op[0] == 'search':
            pat = list(op[1])
            ptr = {'i': e['i']} if 'i' in e and e['i'] < len(pat) else {}
            pst = {e['i']: 'active'} if 'i' in e and e['i'] < len(pat) else {}
            views.append(ArrayView(pat, styles=pst, pointers=ptr, title='pattern', cell=40))
        stack = [f'dfs(i={i}, at "{p}")' if p else f'dfs(i={i}, at root)' for i, p in e['calls']]
        cap, sub, hold = words(e)
        side = StackView(stack, 'Call stack', base=f'{op[0]}("{op[1]}")' if op else 'done',
                         empty='(no search running)')
        if not (op and op[0] == 'search') or e['kind'] in ('result',):
            side = MapView(e['log'], 'Calls so far', headers=('call', 'returns'))
        sc.frame(views, cap, sub, hold, side=side, counters={'words': len(e['ends'])}, legend=legend)
    finish(sc, 211, 'Watch search(".it") at the end: the dot tries b, d and m, hits a dead end in each, and comes '
                    'back to try p, which matches. That coming back is what the recursion is for.',
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
