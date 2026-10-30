#!/usr/bin/env python3
"""#49 Group Anagrams: letter counts are the fingerprint, a map files the words.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
from collections import defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

STRS = ["eat", "tea", "tan", "ate", "nat", "bat"]          # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible fingerprint.
HARD_SUM = ["ad", "bc", "da", "cb"]                 # letter sums: all four total 5
HARD_SET = ["aab", "abb", "", "bab", "aba"]         # letter sets: aab and abb both use {a, b}


def key_text(count):
    """The 26 counts, written short: only the letters that appear."""
    s = ' '.join(f'{chr(97 + i)}{v}' for i, v in enumerate(count) if v)
    return s or 'all zeros'


def trace(strs):
    events, order = [], []
    st = {'w': None}

    def rec(kind, groups, count=None, **kw):
        events.append(dict(kind=kind, groups={k: list(v) for k, v in groups.items()}, order=list(order),
                           count=list(count) if count else None, **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    groups = defaultdict(list)
    rec('start', groups)
    for w, s in enumerate(strs):
        st['w'] = w
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        new = tuple(count) not in groups                                   # display only
        rec('counted', groups, count, new=new)
        groups[tuple(count)].append(s)
        if new:
            order.append(tuple(count))
        rec('filed', groups, count, new=new)
    st['w'] = None
    rec('done', groups)
    answer = list(groups.values())
    assert answer == Solution().groupAnagrams(list(strs))
    return events


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())


def by_letter_sum(strs):
    """First attempt: fingerprint = sum of letter values (a=1, b=2, ...)."""
    groups = defaultdict(list)
    for s in strs:
        groups[sum(ord(c) - 96 for c in s)].append(s)
    return list(groups.values())


def by_letter_set(strs):
    """First attempt: fingerprint = the set of letters used."""
    groups = defaultdict(list)
    for s in strs:
        groups[frozenset(s)].append(s)
    return list(groups.values())


def words(e, strs, notes, first):
    k, w = e['kind'], e['w']
    if k == 'start':
        return ("Give every word a fingerprint: how many of each letter it has.",
                "Anagrams have exactly the same counts. Words with the same counts go in one bucket.", KEY)
    s = strs[w] if w is not None else ''
    kt = key_text(e['count']) if e['count'] else ''
    shown = f'"{s}"' if s else 'The empty string ""'
    if k == 'counted':
        if (w, 'counted') in notes:
            return (f"{shown}: counts {kt}.", notes[(w, 'counted')], KEY)
        if e['new']:
            return (f"{shown}: counts {kt}. No bucket has that key yet.", "",
                    KEY if first.get('new') == id(e) else STEP)
        return (f"{shown}: counts {kt}. That key is already in the map!",
                "Same counts, so it's an anagram of the words already there.",
                KEY if first.get('hit') == id(e) else STEP)
    if k == 'filed':
        grp = e['groups'][tuple(e['count'])]
        if (w, 'filed') in notes:
            return (f"File {shown} under {kt}: bucket is now {', '.join(grp) or chr(34) * 2}.",
                    notes[(w, 'filed')], KEY)
        if e['new']:
            return (f"Start a new bucket under {kt} and put {shown} in it.", "", QUICK * 2.5)
        return (f"Add {shown} to the {kt} bucket: {', '.join(grp)}.", "", QUICK * 2.5)
    n = len(e['groups'])
    return (f"Done: {n} groups. The map's buckets are the answer.",
            notes.get('done', "Each word was counted once and filed with one lookup: O(n·k) for n words of length k."),
            END)


def build(strs, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#49 Group Anagrams: count the letters, bucket by counts', subtitle)
    legend = [(ACTIVE, 'word being filed'), (style('region0')[1], 'one colour per bucket')]
    events = trace(strs)
    first = {}
    for e in events:
        if e['kind'] == 'counted':
            tag = 'new' if e['new'] else 'hit'
            first.setdefault(tag, id(e))
    letters = sorted({ord(c) - 97 for s in strs for c in s})
    for e in events:
        k, w = e['kind'], e['w']
        styles = {}
        # colour each word already filed with its bucket's colour
        for j, s in enumerate(strs):
            if w is not None and j >= w and not (k == 'filed' and j == w):
                continue
            if k == 'start':
                continue
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - 97] += 1
            gi = e['order'].index(tuple(cnt))
            styles[j] = f'region{gi}'
        if w is not None:
            styles[w] = 'active' if k == 'counted' else styles.get(w, 'active')
        shown = [s if s else '""' for s in strs]
        arr = ArrayView(shown, styles, pointers={'word': w} if w is not None else {}, title='strs')
        views = [arr]
        if e['count'] is not None:
            vals = [e['count'][i] for i in letters]
            cst = {j: 'active' if v else 'muted' for j, v in enumerate(vals)}
            views.append(ArrayView(vals, cst, title='count', indices=False,
                                   subs={j: chr(97 + i) for j, i in enumerate(letters)}, cell=54))
            others = 26 - len(letters)
            views.append(TextView([(f'key = {key_text(e["count"])}   (the other {others} letters count 0)', None)],
                                  size=15))
        rows = []
        for gi, key in enumerate(e['order']):
            hot = e['count'] is not None and tuple(e['count']) == key
            rows.append((key_text(key), ', '.join(x if x else '""' for x in e['groups'][key]),
                         f'region{gi}' if not hot or k == 'done' else 'active'))
        cap, sub, hold = words(e, strs, notes, first)
        sc.frame(views, cap, sub, hold,
                 side=MapView(rows, 'Buckets (key → words)', headers=('key: letter counts', 'words'),
                              empty='(empty)'),
                 counters={'groups': len(e['groups'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert Solution().groupAnagrams(list(HARD_SUM)) == [["ad", "da"], ["bc", "cb"]]
    assert by_letter_sum(HARD_SUM) == [["ad", "bc", "da", "cb"]]
    assert Solution().groupAnagrams(list(HARD_SET)) == [["aab", "aba"], ["abb", "bab"], [""]]
    assert by_letter_set(HARD_SET) == [["aab", "abb", "bab", "aba"], [""]]
    sums = build(HARD_SUM, 'strs = ["ad","bc","da","cb"]. Answer [[ad,da],[bc,cb]]. Letter sums put all four together.', {
        (1, 'counted'): "a+d = 1+4 = 5 and b+c = 2+3 = 5. A letter-sum key would file bc with ad. The counts differ.",
        'done': "Two groups. Summing letter values would have given one group of four, without any error.",
    })
    sets = build(HARD_SET, 'strs = ["aab","abb","","bab","aba"]. Answer [[aab,aba],[abb,bab],[""]]. Letter sets merge them.', {
        (1, 'counted'): "Same letters as aab, {a, b}, but not the same NUMBER of each. Only counts tell them apart.",
        (2, 'counted'): "The empty string counts zero of every letter. That's a valid key, so it gets its own group.",
        'done': "Three groups. A set-of-letters key would put aab, abb, bab and aba in one.",
    })
    return [
        (sums, '["ad","bc","da","cb"]: a+d and b+c both total 5. A first attempt keyed on the sum of letter values '
               'puts all four in one group; the answer is [["ad","da"],["bc","cb"]].'),
        (sets, '["aab","abb","","bab","aba"]: aab and abb use the same letters in different amounts. A first attempt '
               'keyed on the set of letters merges them; the answer is [["aab","aba"],["abb","bab"],[""]].'),
    ]


def main():
    args = cli()
    sc = build(STRS, 'strs = ["eat","tea","tan","ate","nat","bat"]. Group the anagrams together.')
    finish(sc, 49, 'Watch "tea": its counts, one a, one e, one t, are a key the map already has, '
                   'so it lands in the same bucket as "eat" with a single lookup.',
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
