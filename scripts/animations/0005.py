#!/usr/bin/env python3
"""#5 Longest Palindromic Substring: stand at each middle and step outwards
while the two ends match.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S = "babad"                     # LeetCode example 1

# Hard examples (interactive page only), each breaking a plausible first attempt.
HARD_MIRROR = "aacabdkacaa"     # "aca"; reverse + longest common substring gives "aaca"
HARD_EVEN = "abccbaxyx"         # "abccba"; trying only letter-middles gives "xyx"


class Solution:
    """The notebook's solution (comments dropped), to cross-check the traced run."""
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, end = 0, 0

        def expand_from_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            length = max(expand_from_center(i, i), expand_from_center(i, i + 1))
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]


def reverse_common(s):
    """First attempt: a palindrome equals its reverse, so take the longest
    substring that s shares with reversed(s)."""
    r, n, best = s[::-1], len(s), (0, 0)
    run = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == r[j - 1]:
                run[i][j] = run[i - 1][j - 1] + 1
                if run[i][j] > best[0]:
                    best = (run[i][j], i)
    return s[best[1] - best[0]:best[1]]


def letter_middles_only(s):
    """First attempt: expand around each letter, forgetting the gaps between letters."""
    best = s[0]
    for i in range(len(s)):
        left = right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        if right - left - 1 > len(best):
            best = s[left + 1:right]
    return best


def trace(s):
    events = []
    st = {'i': None, 'mid': None, 'start': 0, 'end': 0, 'odd': None}

    def rec(kind, **kw):
        events.append(dict(kind=kind, **st, **kw))

    # ---- the notebook's solution, with rec() calls added ----
    start, end = 0, 0

    def expand_from_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            rec('match', left=left, right=right)
            left -= 1
            right += 1
        why = 'edge' if left < 0 or right >= len(s) else 'mismatch'          # display only
        rec('stop', left=left, right=right, why=why, length=right - left - 1)
        return right - left - 1

    rec('start', left=None, right=None)
    for i in range(len(s)):
        st.update(i=i, mid='odd')
        odd = expand_from_center(i, i)
        st.update(mid='even', odd=odd)
        even = expand_from_center(i, i + 1)                                    # display only
        length = max(odd, even)
        old = (start, end)
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
            st.update(start=start, end=end, mid=None)
            rec('best', left=None, right=None, length=length, even=even, old=old)
        else:
            st.update(mid=None)
            rec('keep', left=None, right=None, length=length, even=even)
    st.update(i=None)
    rec('done', left=None, right=None, ans=s[start:end + 1])
    assert s[start:end + 1] == Solution().longestPalindrome(s)
    return events


def q(s):
    return f'"{s}"'


def words(e, s, notes, seen):
    k, i = e['kind'], e['i']
    best = s[e['start']:e['end'] + 1]
    mid = (f"Letter middle {i} ('{s[i]}')" if e['mid'] == 'odd'
           else f"Gap middle {i}|{i + 1}") if i is not None and e['mid'] else ''
    if k == 'start':
        return ("Every palindrome mirrors around a middle. Try each one and step outwards.",
                "A middle is a letter (\"aba\") or the gap between two letters (\"abba\").", KEY)
    if k == 'match':
        L, R = e['left'], e['right']
        if (k, i, e['mid'], L) in notes:
            return (f"{mid}: s[{L}] = s[{R}] = '{s[L]}'. Grow to {q(s[L:R + 1])}.",
                    notes[(k, i, e['mid'], L)], KEY)
        if L == R:
            return (f"{mid}: a single letter is always a palindrome.", "", QUICK * 1.4)
        if 'grow' not in seen:
            seen.add('grow')
            return (f"{mid}: s[{L}] = s[{R}] = '{s[L]}', so {q(s[L:R + 1])} is a palindrome too.",
                    "Both ends matched, so step out one more on each side.", KEY)
        return (f"{mid}: s[{L}] = s[{R}] = '{s[L]}'. Grow to {q(s[L:R + 1])}.", "", STEP)
    if k == 'stop':
        L, R, n = e['left'], e['right'], e['length']
        if e['why'] == 'edge':
            head = f"{mid}: {'left' if L < 0 else 'right'} pointer ran off the string."
        else:
            head = f"{mid}: s[{L}] '{s[L]}' ≠ s[{R}] '{s[R]}', stop."
        key = (k, i, e['mid'])
        if key in notes:
            return (head, notes[key], KEY)
        if n > 1 and 'formula' not in seen:
            seen.add('formula')
            return (head, f"Both pointers are one step past it: length = {R} - ({L}) - 1 = {n}.", KEY)
        if e['mid'] == 'even' and 'gap' not in seen:
            seen.add('gap')
            return (head, "Nothing here, but gap middles are how even lengths like \"abba\" get found.", KEY)
        return (head + f" Length {n}.", "", QUICK * 1.6)
    if k in ('best', 'keep'):
        n = e['length']
        cmp = f"{n} > end - start" if k == 'best' else f"{n} ≤ end - start"
        if (k, i) in notes:
            sub = notes[(k, i)]
        elif k == 'best' and e['old'] != (0, 0) and n == e['old'][1] - e['old'][0] + 1:
            sub = (f"end - start was {e['old'][1] - e['old'][0]}, one less than the best length, "
                   "so a tie replaces it. Either answer is accepted.")
        else:
            sub = ''
        if k == 'best':
            return (f"Index {i}: longest here is {n}, a new best {q(best)} (start {e['start']}, end {e['end']}).",
                    sub, KEY if sub else STEP)
        return (f"Index {i}: longest here is {n}. Best stays {q(best)}.", sub, KEY if sub else QUICK * 1.6)
    return (f"Every middle tried. Answer: {q(e['ans'])}.",
            notes.get('done', "2n - 1 middles, each growing at most n/2 steps: O(n²) time, O(1) space."), END)


def build(s, subtitle, notes=None):
    notes = notes or {}
    n = len(s)
    sc = Scene('#5 Longest Palindromic Substring: expand around center', subtitle)
    legend = [(style('good')[1], 'ends match'), (style('bad')[1], 'mismatch'),
              (style('window')[1], 'palindrome so far'), (style('gold')[1], 'best so far')]
    seen = set()
    for e in trace(s):
        L, R = e['left'], e['right']
        vals = ['·'] + list(s) + ['·']
        subs = {k + 1: str(k) for k in range(n)}
        styles = {0: 'muted', n + 1: 'muted'}
        bs, be = e['start'], e['end']
        if e['kind'] not in ('start',) and e['i'] is not None or e['kind'] == 'done':
            for k in range(bs, be + 1):
                styles[k + 1] = 'gold'
        if e['kind'] == 'done':
            for k in range(bs, be + 1):
                styles[k + 1] = 'good'
        ptrs = {}
        if e['kind'] == 'match':
            for k in range(L + 1, R):
                styles[k + 1] = 'window'
            styles[L + 1] = styles[R + 1] = 'good'
            ptrs = {'L': L + 1, 'R': R + 1} if L != R else {'L=R': L + 1}
        elif e['kind'] == 'stop':
            for k in range(L + 1, R):
                styles[k + 1] = 'window'
            if e['why'] == 'mismatch':
                styles[L + 1] = styles[R + 1] = 'bad'
            ptrs = {'L': L + 1, 'R': R + 1}
        arr = ArrayView(vals, styles, ptrs,
                        indices=False, subs=subs, title='s')
        lines = []
        if e['kind'] == 'stop':
            lines.append(f"length = R - L - 1 = {R} - ({L}) - 1 = {e['length']}")
        elif e['kind'] in ('best', 'keep'):
            lines.append(f"max(letter {e['odd']}, gap {e['even']}) = {e['length']}")
            if e['kind'] == 'best':
                ln = e['length']
                lines.append(f"start = {e['i']} - ({ln} - 1) // 2 = {bs},  end = {e['i']} + {ln} // 2 = {be}")
        else:
            lines.append('')
        rows = [('middle', '-' if e['i'] is None else (f"{e['i']}" if e['mid'] == 'odd' else
                                                         f"{e['i']}|{e['i'] + 1}" if e['mid'] == 'even' else f"{e['i']}")),
                ('left', '-' if L is None else str(L)), ('right', '-' if R is None else str(R)),
                ('start, end', f"{bs}, {be}"), ('best', q(s[bs:be + 1]), 'gold')]
        cap, sub, hold = words(e, s, notes, seen)
        sc.frame([arr, TextView(lines, size=17)], cap, sub, hold,
                 side=MapView(rows, 'State', headers=('name', 'value')),
                 counters={'best length': be - bs + 1}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    assert Solution().longestPalindrome(HARD_MIRROR) == "aca" and reverse_common(HARD_MIRROR) == "aaca"
    assert Solution().longestPalindrome(HARD_EVEN) == "abccba" and letter_middles_only(HARD_EVEN) == "xyx"
    mirror = build(HARD_MIRROR, f's = "{HARD_MIRROR}". Answer "aca". Reverse + common substring gives "aaca".', {
        ('best', 2): "\"aaca\" just before it reads \"acaa\" backwards, so it isn't a palindrome, even though "
                     "\"acaa\" sits at the end of the string.",
        'done': "Reversing the string and matching it against itself finds \"aaca\", which isn't a palindrome. "
                "Expanding only ever grows real palindromes.",
    })
    even = build(HARD_EVEN, f's = "{HARD_EVEN}". Answer "abccba". Letter middles alone give "xyx".', {
        ('stop', 2, 'even'): "The gap between the two c's grows all the way to \"abccba\", length 6.",
        ('stop', 7, 'odd'): "\"xyx\" is the best a letter middle can do. It doesn't beat 6.",
        'done': "Only the gap middle found \"abccba\". A version that tries letters only returns \"xyx\".",
    })
    return [
        (mirror, "\"aacabdkacaa\" contains \"aaca\" at the start and its mirror image \"acaa\" at the end. Reversing the "
                 "string and taking the longest common substring returns \"aaca\", which isn't a palindrome; the answer is \"aca\"."),
        (even, "\"abccbaxyx\": the longest palindrome has an even length, so its middle is a gap. A first attempt that only "
               "expands around letters returns \"xyx\"; the answer is \"abccba\"."),
    ]


def main():
    args = cli()
    sc = build(S, f's = "{S}". Find the longest stretch that reads the same both ways.')
    finish(sc, 5, "Watch the middle at index 1: 'b' matches 'b', \"a\" grows to \"bab\", and the pointers stop one step "
                  "past it, which is why the length is right - left - 1.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
