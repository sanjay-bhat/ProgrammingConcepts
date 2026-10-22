#!/usr/bin/env python3
"""#127 Word Ladder: breadth-first search in rounds; a word leaves the set when it's queued.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
from collections import deque
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

BEGIN, END_WORD = 'hit', 'cog'
WORDS = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']        # LeetCode example 1
POS = {'hit': (0.0, 0.5), 'hot': (0.2, 0.5), 'dot': (0.45, 0.05), 'lot': (0.45, 0.95),
       'dog': (0.75, 0.05), 'log': (0.75, 0.95), 'cog': (1.0, 0.5)}


def trace(beginWord, endWord, wordList):
    events = []
    rounds = {beginWord: 1}

    def rec(kind, word_set, queue, **kw):
        events.append(dict(kind=kind, left=set(word_set), queue=list(queue), rounds=dict(rounds), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    queue = deque([(beginWord, 1)])
    rec('start', word_set, queue)
    while queue:
        word, dist = queue.popleft()
        rec('pop', word_set, queue, word=word, dist=dist)
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nw = word[:i] + c + word[i+1:]
                if nw == endWord:
                    rounds[nw] = dist + 1
                    rec('found', word_set, queue, word=word, nw=nw, dist=dist)
                    return events
                if nw in word_set:
                    word_set.discard(nw)
                    queue.append((nw, dist + 1))
                    rounds[nw] = dist + 1
                    rec('queue', word_set, queue, word=word, nw=nw, dist=dist)
                elif nw in wordList and nw != word:
                    rec('used', word_set, queue, word=word, nw=nw, dist=dist)
    return events


def words(e, seen):
    k = e['kind']
    if k == 'start':
        return ("Put the list in a set. cog is in it, so a ladder might exist. Queue (hit, 1).",
                "The number is how many words the ladder has so far, counting hit.", STEP)
    if k == 'pop':
        if e['word'] == BEGIN:
            return (f"Pop hit (1 word). Try every letter in every position: 26 × 3 = 78 new words.",
                    "Only the ones still in the set are allowed.", KEY)
        return (f"Pop {e['word']} ({e['dist']} words). Try its 78 one-letter changes.", "", STEP)
    if k == 'queue':
        first = not seen.get('queue')
        seen['queue'] = True
        return (f"{e['nw']} is in the set: remove it NOW and queue ({e['nw']}, {e['dist'] + 1}).",
                "Removing it as it's queued means nothing can queue it a second time." if first else "", KEY if first else STEP)
    if k == 'used':
        if e['rounds'][e['nw']] == e['dist'] and not seen.get('same'):
            seen['same'] = True
            return (f"{e['word']} → {e['nw']}: already out of the set, so it's skipped.",
                    f"{e['nw']} is in {e['word']}'s own round: hot queued it already. Without the removal it'd go in twice.", KEY)
        return (f"{e['word']} → {e['nw']}: already out of the set, so it's skipped.", "", QUICK * 2)
    return (f"{e['word']} → {e['nw']}: that's endWord! Answer: {e['dist']} + 1 = {e['dist'] + 1} words.",
            "Rounds go in order, so no shorter ladder can exist: hit → hot → dot → dog → cog.", END)


def main():
    args = cli()
    events = trace(BEGIN, END_WORD, WORDS)
    sc = Scene('#127 Word Ladder: breadth-first search in rounds',
               'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]')
    allw = [BEGIN] + WORDS
    edges = [(a, b) for i, a in enumerate(allw) for b in allw[i + 1:] if sum(x != y for x, y in zip(a, b)) == 1]
    legend = [(ACTIVE, 'word being expanded'), (CURSOR, 'new word built'), ('#9aa3b2', 'lines: one letter apart')]
    seen = {}
    for e in events:
        k = e['kind']
        styles = {w: f'region{r - 1}' for w, r in e['rounds'].items()}
        rings = []
        if k != 'start':
            styles[e['word']] = 'active'
        estyles = {}
        if 'nw' in e:
            rings.append((e['nw'], CURSOR))
            estyles[(e['word'], e['nw'])] = 'bad' if k == 'used' else 'active'
            if k == 'found':
                styles[e['nw']] = 'good'
        labels = {w: f'round {r}' for w, r in e['rounds'].items()}
        graph = GraphView(POS, edges, styles=styles, edge_styles=estyles, labels=labels, rings=rings, height=260)
        q = QueueView([(f'{w} · {d}', f'region{d - 1}') for w, d in e['queue']], 'Queue (word · words so far)')
        rows = []
        for w in WORDS:
            if w in e['left']:
                rows.append((w, 'in the set'))
            else:
                rows.append((w, f'removed, round {e["rounds"][w]}', 'muted'))
        cap, sub, hold = words(e, seen)
        sc.frame([graph, q], cap, sub, hold, side=MapView(rows, 'Word set', headers=('word', 'status')),
                 counters={'round': e.get('dist', 1) + (1 if k == 'found' else 0)}, legend=legend)
    finish(sc, 127, "Watch dot try to build lot: lot already left the set when hot queued it, so it's skipped, "
                    "and every word is visited exactly once, in the round it was first reached.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
