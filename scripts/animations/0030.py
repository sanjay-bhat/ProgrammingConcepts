#!/usr/bin/env python3
"""#30 Substring with Concatenation of All Words: for each of the word-length
alignments, slide a window one whole word at a time, counting words in a
hash map and shrinking from the left when a word appears too often.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged. Long runs of unknown words are
shown as quick frames.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403
from typing import List  # noqa: E402
from collections import Counter  # noqa: E402

S, WORDS = "barfoothefoobarman", ["foo", "bar"]          # LeetCode example 1: [0, 9]

# Hard examples (interactive page only), each breaking a plausible first attempt.
# 1) Sliding only from index 0, in steps of one word. All three LeetCode
#    samples pass (every answer there is a multiple of the word length), but
#    here both answers start at odd positions. Answer [1, 4]; offset 0 alone: [].
HARD_OFFSET = ("abarfoobar", ["foo", "bar"])
# 2) Throwing the whole window away when a word appears too often, instead of
#    dropping words from the left until it fits. "cat dog cat" + "cat" has one
#    cat too many; dropping only the first cat keeps "dog cat cat", a match.
#    Answer [0, 3, 6]; restarting finds only [0].
HARD_SHRINK = ("catdogcatcatdog", ["cat", "dog", "cat"])


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, w_len, w_count = len(s), len(words[0]), len(words)
        freq = Counter(words)
        result = []
        for off in range(w_len):
            seen = Counter()
            left = off
            count = 0
            for right in range(off, n - w_len + 1, w_len):
                w = s[right:right + w_len]
                if w not in freq:
                    seen.clear()
                    count = 0
                    left = right + w_len
                    continue
                seen[w] += 1
                count += 1
                while seen[w] > freq[w]:
                    lw = s[left:left + w_len]
                    seen[lw] -= 1
                    count -= 1
                    left += w_len
                if count == w_count:
                    result.append(left)
        return result


def variant(s, words, offsets=None, restart=False):
    """The same window with the two first-attempt slips switchable:
    offsets=[0] slides from index 0 only; restart=True throws the window away
    (keeping just the new word) when a word appears too often."""
    n, w_len, w_count = len(s), len(words[0]), len(words)
    freq, result = Counter(words), []
    for off in (range(w_len) if offsets is None else offsets):
        seen, left, count = Counter(), off, 0
        for right in range(off, n - w_len + 1, w_len):
            w = s[right:right + w_len]
            if w not in freq:
                seen.clear()
                count = 0
                left = right + w_len
                continue
            seen[w] += 1
            count += 1
            if restart and seen[w] > freq[w]:
                seen, count, left = Counter({w: 1}), 1, right
            while seen[w] > freq[w]:
                lw = s[left:left + w_len]
                seen[lw] -= 1
                count -= 1
                left += w_len
            if count == w_count:
                result.append(left)
    return sorted(result)


def trace(s, words):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, seen=dict(seen), count=count, left=left,
                           result=result[:], off=off, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    n, w_len, w_count = len(s), len(words[0]), len(words)
    freq = Counter(words)
    result = []
    seen, count, left, off = Counter(), 0, 0, 0
    for off in range(w_len):
        seen = Counter()
        left = off
        count = 0
        rec('offset')
        for right in range(off, n - w_len + 1, w_len):
            w = s[right:right + w_len]
            if w not in freq:
                seen.clear()
                count = 0
                left = right + w_len
                rec('unknown', right=right, w=w)
                continue
            seen[w] += 1
            count += 1
            rec('add', right=right, w=w, over=seen[w] > freq[w])
            while seen[w] > freq[w]:
                lw = s[left:left + w_len]
                seen[lw] -= 1
                count -= 1
                left += w_len
                rec('shrink', right=right, w=w, lw=lw)
            if count == w_count:
                result.append(left)
                rec('match', right=right, w=w)
    off = None
    rec('done')
    assert result == Solution().findSubstring(s, words)
    return events, dict(freq), w_len, w_count


def merged(events):
    """Fold runs of 'unknown' words into one frame each."""
    out = []
    for e in events:
        if e['kind'] == 'unknown' and out and out[-1]['kind'] == 'unknown' and out[-1]['off'] == e['off']:
            out[-1] = dict(e, words=out[-1]['words'] + [e['w']], first=out[-1]['first'])
        elif e['kind'] == 'unknown':
            out.append(dict(e, words=[e['w']], first=e['right']))
        else:
            out.append(e)
    return out


def build(s, words, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#30 Concatenation of All Words: slide by whole words', subtitle)
    legend = [(style('window')[1], 'window'), (ACTIVE, 'word just read'), (style('bad')[1], 'not a word'),
              (style('good')[1], 'match starts here')]
    events, freq, w_len, w_count = trace(s, words)
    seen_keys = set()
    for idx, e in enumerate(merged(events)):
        k = e['kind']
        n = len(s)
        right = e.get('right')
        off = e['off'] if e['off'] is not None else 0
        # word-sized pieces at this offset; a leading/trailing scrap that can't be a word is greyed
        starts = list(range(off, n - w_len + 1, w_len))
        pieces = ([(0, off)] if off else []) + [(st, st + w_len) for st in starts]
        if pieces and pieces[-1][1] < n:
            pieces.append((pieces[-1][1], n))
        vals = [s[a_:b_] for a_, b_ in pieces]
        subs = {i: str(a_) for i, (a_, _) in enumerate(pieces)}
        at = {a_: i for i, (a_, b_) in enumerate(pieces) if b_ - a_ == w_len and a_ >= off}
        styles = {i: 'muted' for i, (a_, b_) in enumerate(pieces) if b_ - a_ != w_len or a_ < off}
        ptrs, window = {}, None
        if e['off'] is None:
            styles = {}
        if k in ('add', 'shrink', 'match'):
            lo, hi = at[e['left']], at[right]
            window = (lo, hi)
            for i in range(lo, hi + 1):
                styles[i] = 'window'
            styles[hi] = 'active' if k != 'match' else 'good'
            ptrs = {'left': lo, 'right': hi} if lo != hi else {'left=right': lo}
        if k == 'unknown':
            for i in range(at[e['first']], at[right] + 1):
                styles[i] = 'bad'
            ptrs = {'right': at[right]}
        view = ArrayView(vals, styles, ptrs, window=window, title='s', indices=False, subs=subs)
        rows = [(w, f"{e['seen'].get(w, 0)} of {c}",
                 'bad' if e['seen'].get(w, 0) > c else ('good' if e['seen'].get(w, 0) == c else None))
                for w, c in freq.items()]
        side = MapView(rows, 'Words in window', headers=('word', 'seen / need'))
        lines = [f"offset {e['off']}: pieces start at {e['off']}, {e['off'] + w_len}, {e['off'] + 2 * w_len}, ..."
                 if e['off'] is not None else f"all {w_len} offsets done",
                 f"answer so far: {e['result']}"]
        cap, sub, hold = words_for(e, w_len, w_count, seen_keys)
        key = (k, e.get('off'), right) if k != 'done' else 'done'
        if key in notes:
            sub, hold = notes[key], (END if k == 'done' else KEY)
        sc.frame([view, TextView(lines, size=16)], cap, sub, hold, side=side,
                 counters={'count': f"{e['count']}/{w_count}"}, legend=legend)
    return sc


def words_for(e, w_len, w_count, seen):
    k = e['kind']
    first = k not in seen
    seen.add(k)
    if k == 'offset':
        if e['off'] == 0:
            return ("Every word is the same length, so chop s into word-sized pieces.",
                    f"A match can start anywhere, so try all {w_len} ways to line the pieces up: offsets 0 to {w_len - 1}.",
                    KEY)
        return (f"Offset {e['off']}: line the pieces up one letter further along.",
                "A match starting at an index that isn't a multiple of the word length lives here." if e['off'] == 1
                else "", STEP)
    if k == 'unknown':
        ws = e['words']
        return ((f"\"{ws[0]}\" isn't one of the words. Empty the window and start after it." if len(ws) == 1 else
                 f"{', '.join(chr(34) + w + chr(34) for w in ws)}: none are words. Empty the window each time."),
                "No match can contain a non-word, so nothing in the window can be saved." if first else "",
                KEY if first else QUICK * 2.5)
    if k == 'add':
        over = e['over']
        cap = f"\"{e['w']}\" is a word: add it. count = {e['count']}."
        if over:
            return (cap + f" But that's one \"{e['w']}\" too many.",
                    "Drop words from the LEFT until it fits. Don't throw the whole window away.", KEY)
        return (cap, "", STEP if e['count'] < w_count else QUICK * 2)
    if k == 'shrink':
        return (f"Drop \"{e['lw']}\" from the left. left = {e['left']}.",
                "The words after it are still a valid start, so keep them." if first else "",
                KEY if first else STEP)
    if k == 'match':
        return (f"count = {w_count}: every word exactly as often as needed. Record {e['left']}.",
                "The next word will overflow one count, and the shrink slides the window on." if first else "",
                KEY if first else STEP)
    return (f"Answer: {e['result']}.",
            f"{w_len} offsets, each reading every piece once: about n steps per offset.", END)


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    samples = [("barfoothefoobarman", ["foo", "bar"], [0, 9]),
               ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
               ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12])]
    for s, w, want in samples:          # offset 0 alone passes every sample
        assert sorted(Solution().findSubstring(s, w)) == want == variant(s, w, offsets=[0])
    assert Solution().findSubstring(*HARD_OFFSET) == [1, 4] and variant(*HARD_OFFSET, offsets=[0]) == []
    assert Solution().findSubstring(*HARD_SHRINK) == [0, 3, 6] and variant(*HARD_SHRINK, restart=True) == [0]
    a = build(*HARD_OFFSET, f's = "{HARD_OFFSET[0]}", words = {HARD_OFFSET[1]}. Answer [1, 4]. Offset 0 alone finds nothing.', {
        'done': "[1, 4]: both matches start at offset 1. Sliding only from index 0 passes all three LeetCode "
                "samples, whose answers are all multiples of 3, and finds nothing here.",
    })
    b = build(*HARD_SHRINK, f's = "{HARD_SHRINK[0]}", words = {HARD_SHRINK[1]}. Answer [0, 3, 6]. Restarting finds [0].', {
        'done': "[0, 3, 6]. Throwing the window away at the extra \"cat\" loses \"dog cat\", so a restart "
                "finds only 0.",
    })
    return [
        (a, "Both matches start at index 1, which isn't a multiple of the word length. Sliding only from index 0 "
            "passes all three LeetCode samples and returns [] here; the answer is [1, 4]."),
        (b, "\"cat dog cat\" then another \"cat\": one cat too many. Dropping just the first cat keeps \"dog cat cat\", "
            "a match. Throwing the whole window away finds only [0]; the answer is [0, 3, 6]."),
    ]


def main():
    args = cli()
    sc = build(S, WORDS, f's = "{S}", words = {WORDS}. Find every start of all the words glued together.')
    finish(sc, 30, "Watch offset 0 reach \"foo\" after \"bar\": count hits 2 and index 0 is recorded, then \"the\" "
                   "isn't a word and the window empties.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
