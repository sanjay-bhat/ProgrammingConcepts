#!/usr/bin/env python3
"""#68 Text Justification: pack as many words as fit, then share the spare
spaces between the gaps, extras to the left. The last line is left-justified.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

WORDS = ["This", "is", "an", "example", "of", "text", "justification."]   # LeetCode example 1
WIDTH = 16

# Hard example 1: two lines fill all 12 columns exactly, and the last line has
# two words. Packing with `<` instead of `<=` turns 3 lines into 4.
HARD1 = (["look", "closely", "at", "this", "edge", "case", "please"], 12)
HARD1_ANSWER = ["look closely", "at this edge", "case please "]
HARD1_WRONG = ["look        ", "closely   at", "this    edge", "case please "]

# Hard example 2: 5 spare spaces over 3 gaps (2, 2, 1), and a one-word line in
# the middle. Dumping the whole remainder into the first gap gives 3, 1, 1.
HARD2 = (["We", "are", "what", "we", "repeatedly", "do.", "Excellence,", "then,",
          "is", "not", "an", "act,", "but", "a", "habit."], 16)
HARD2_ANSWER = ["We  are  what we", "repeatedly   do.", "Excellence,     ",
                "then,  is not an", "act,    but    a", "habit.          "]
HARD2_WRONG_FIRST = "We   are what we"


class Solution:
    # ---- the notebook's solution, unchanged (used to check the answers) ----
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i, n = 0, len(words)
        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            word_count = j - i
            total_word_len = sum(len(words[k]) for k in range(i, j))
            total_spaces = maxWidth - total_word_len
            is_last = (j == n)
            if is_last or word_count == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                gaps = word_count - 1
                each = total_spaces // gaps
                extra = total_spaces % gaps
                line = words[i]
                for k in range(1, word_count):
                    spaces = each + (1 if k <= extra else 0)
                    line += " " * spaces + words[i + k]
            result.append(line)
            i = j
        return result


def wrong_strict(words, maxWidth):
    """First attempt: pack while the line stays SHORTER than maxWidth (< not <=)."""
    result, i, n = [], 0, len(words)
    while i < n:
        line_len, j = len(words[i]), i + 1
        while j < n and line_len + 1 + len(words[j]) < maxWidth:
            line_len += 1 + len(words[j]); j += 1
        cnt, total = j - i, maxWidth - sum(len(w) for w in words[i:j])
        if j == n or cnt == 1:
            line = " ".join(words[i:j]); line += " " * (maxWidth - len(line))
        else:
            each, extra, line = total // (cnt - 1), total % (cnt - 1), words[i]
            for k in range(1, cnt):
                line += " " * (each + (1 if k <= extra else 0)) + words[i + k]
        result.append(line); i = j
    return result


def wrong_first_gap(words, maxWidth):
    """First attempt: give the whole remainder to the first gap."""
    result, i, n = [], 0, len(words)
    while i < n:
        line_len, j = len(words[i]), i + 1
        while j < n and line_len + 1 + len(words[j]) <= maxWidth:
            line_len += 1 + len(words[j]); j += 1
        cnt, total = j - i, maxWidth - sum(len(w) for w in words[i:j])
        if j == n or cnt == 1:
            line = " ".join(words[i:j]); line += " " * (maxWidth - len(line))
        else:
            each, extra, line = total // (cnt - 1), total % (cnt - 1), words[i]
            for k in range(1, cnt):
                line += " " * (each + (extra if k == 1 else 0)) + words[i + k]
        result.append(line); i = j
    return result


assert Solution().fullJustify(*HARD1) == HARD1_ANSWER
assert wrong_strict(*HARD1) == HARD1_WRONG
assert Solution().fullJustify(*HARD2) == HARD2_ANSWER
assert wrong_first_gap(*HARD2)[0] == HARD2_WRONG_FIRST != HARD2_ANSWER[0]
assert wrong_strict(WORDS, WIDTH) == wrong_first_gap(WORDS, WIDTH) == Solution().fullJustify(WORDS, WIDTH)


def trace(words, maxWidth):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, result=list(result), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    result = []
    i, n = 0, len(words)
    rec('start', i=0)
    while i < n:
        line_len = len(words[i])
        j = i + 1
        rec('open', i=i, j=j, line_len=line_len)
        while j < n and line_len + 1 + len(words[j]) <= maxWidth:
            rec('fits', i=i, j=j, line_len=line_len, need=line_len + 1 + len(words[j]))
            line_len += 1 + len(words[j])
            j += 1
        if j < n:
            rec('nofit', i=i, j=j, line_len=line_len, need=line_len + 1 + len(words[j]))
        word_count = j - i
        total_word_len = sum(len(words[k]) for k in range(i, j))
        total_spaces = maxWidth - total_word_len
        is_last = (j == n)
        if is_last or word_count == 1:
            line = " ".join(words[i:j])
            line += " " * (maxWidth - len(line))
            rec('left', i=i, j=j, line=line, last=is_last, letters=total_word_len, spaces=total_spaces)
        else:
            gaps = word_count - 1
            each = total_spaces // gaps
            extra = total_spaces % gaps
            line = words[i]
            sizes = []
            for k in range(1, word_count):
                spaces = each + (1 if k <= extra else 0)
                sizes.append(spaces)
                line += " " * spaces + words[i + k]
            rec('spread', i=i, j=j, line=line, letters=total_word_len, spaces=total_spaces,
                gaps=gaps, each=each, extra=extra, sizes=sizes)
        result.append(line)
        i = j
    rec('done', i=n)
    return events, result


def line_cells(words, i, j, sizes=None, cand=None, width=0, pad_style='muted'):
    """Characters of words[i:j] as cells; spaces styled by role."""
    vals, st = [], {}
    for k in range(i, j):
        if k > i:
            n_sp = sizes[k - i - 1] if sizes else 1
            for s in range(n_sp):
                extra = sizes is not None and s == n_sp - 1 and n_sp > min(sizes)
                st[len(vals)] = 'active' if extra else 'gold'
                vals.append('')
        for ch in words[k]:
            st[len(vals)] = 'window'
            vals.append(ch)
    if cand is not None:
        over = len(vals) + 1 + len(words[cand]) > width
        st[len(vals)] = 'bad' if over else 'gold'
        vals.append('')
        for ch in words[cand]:
            st[len(vals)] = 'bad' if over else 'good'
            vals.append(ch)
    while len(vals) < width:
        st[len(vals)] = pad_style
        vals.append('')
    if len(vals) > width + 4:                  # show the overflow, not the whole word
        vals = vals[:width + 3] + ['…']
    return vals, st


def build(words, width, subtitle, notes=None):
    notes = notes or {}
    events, _ = trace(words, width)
    sc = Scene('#68 Text Justification: pack, then share out the spaces', subtitle)
    cols = width + 4
    cell = int(min(46, (864 - 70 - 5 * cols) / cols))
    legend = [(style('good')[1], 'word being tried'), (style('window')[1], 'on this line'),
              (style('gold')[1], 'space'), (ACTIVE, 'extra space (left gaps first)')]
    first = {}
    for e in events:
        k = e['kind']
        i, j = e.get('i'), e.get('j')
        done_upto = i if k != 'done' else len(words)
        chips = []
        for w_i, w in enumerate(words):
            if w_i < done_upto:
                chips.append((w, 'muted'))
            elif j is not None and i <= w_i < j:
                chips.append((w, 'window'))
            elif k in ('fits', 'nofit') and w_i == j:
                chips.append((w, 'good' if k == 'fits' else 'bad'))
            else:
                chips.append(w)
        hold, cap, sub = STEP, '', ''
        line_vals, line_st = [''] * width, {c: 'muted' for c in range(width)}
        if k in ('open', 'fits', 'nofit'):
            line_vals, line_st = line_cells(words, i, j, cand=j if k in ('fits', 'nofit') else None,
                                            width=width, pad_style='plain')
        elif k == 'spread':
            line_vals, line_st = line_cells(words, i, j, sizes=e['sizes'], width=width)
        elif k == 'left':
            line_vals, line_st = line_cells(words, i, j, width=width)
        if k == 'start':
            cap = f"Fill lines exactly {width} characters wide, using as many words per line as fit."
            sub = "Two jobs per line: decide which words go on it, then decide where the spaces go."
            hold = KEY
        elif k == 'open':
            cap = f'New line starts with "{words[i]}" ({len(words[i])} letters).'
            sub = "Every line takes at least one word: the rules promise no word is wider than the line."
            hold = QUICK * 2.4
        elif k == 'fits':
            w = words[j]
            exact = e['need'] == width
            cap = (f'Try "{w}": {e["line_len"]} + 1 space + {len(w)} = {e["need"]} ≤ {width}. It fits'
                   + (' exactly.' if exact else '.'))
            if exact:
                sub = notes.get('exact', "Equal to the width still fits: test with <=, not <.")
                hold = KEY
            else:
                sub, hold = '', STEP
        elif k == 'nofit':
            w = words[j]
            cap = f'Try "{w}": {e["line_len"]} + 1 + {len(w)} = {e["need"]} > {width}. Too wide, so the line is full.'
            sub = "Count one space per gap while packing: that's the least a gap can hold."
            if 'nofit' not in first:
                first['nofit'] = True
                hold = KEY
            else:
                sub, hold = '', STEP
        elif k == 'spread':
            sz = e['sizes']
            cap = (f"{width} − {e['letters']} letters = {e['spaces']} spaces for {e['gaps']} gaps: "
                   f"{e['spaces']} ÷ {e['gaps']} = {e['each']} each, {e['extra']} left over.")
            if e['extra']:
                sub = notes.get(('spread', i), f"The left-over {'space goes' if e['extra'] == 1 else 'spaces go'} "
                                f"one each to the leftmost gaps: {', '.join(map(str, sz))}.")
                hold = KEY
            else:
                sub = notes.get(('spread', i), f"It divides evenly, so every gap gets {e['each']}.")
                hold = KEY if 'even' not in first else STEP
                first['even'] = True
        elif k == 'left':
            if e['last']:
                cap = f'Last line: "{" ".join(words[i:j])}" gets single spaces, then padding on the right.'
                sub = notes.get('last', "The last line is never stretched, even if it has several words.")
            else:
                cap = f'"{words[i]}" is alone on its line: no gaps to share, so all the spaces go on the right.'
                sub = notes.get(('single', i), "Dividing by gaps here would divide by zero: the one-word check comes first.")
            hold = KEY
        else:
            cap = f"Done: {len(e['result'])} lines, each exactly {width} characters."
            sub = notes.get('done', "Each word is packed once and each character written once.")
            hold = END
        arr = ArrayView(line_vals, line_st, title='line', cuts=[width] if len(line_vals) > width else [],
                        cell=cell)
        out = [(f'"{ln.replace(" ", "·")}"', 'good') for ln in e['result']] or ['(no lines yet)']
        sc.frame([ChipsView(chips, 'words', size=14), arr,
                  TextView(out[-6:], title='result  (· = space)', size=17)],
                 cap, sub, hold, counters={'lines': len(e['result'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    w1, m1 = HARD1
    sc1 = build(w1, m1, f'maxWidth = {m1}. Two lines fill all {m1} columns with nothing to spare.',
                {'exact': "Exactly full still fits. Packing with < instead of <= would push this word "
                          "down and turn 3 lines into 4.",
                 'last': 'Justify it like the others and you get "case  please". The last line stays left.'})
    w2, m2 = HARD2
    sc2 = build(w2, m2, f'maxWidth = {m2}. Uneven gaps, and a word that fills a line on its own.',
                {('spread', 0): 'One extra each to the two leftmost gaps: 2, 2, 1. Putting both extras in '
                                'the first gap gives "We   are what we".',
                 ('single', 6): "No gaps to share, so dividing by gaps would crash here. "
                                "The one-word check must come before the division."})
    return [(sc1, "Two lines fit to the last column. Packing with < instead of <= pushes a word down "
                  "and answers 4 lines instead of 3; the 2-word last line must stay left-justified."),
            (sc2, "Five spare spaces over three gaps: the extras go 2, 2, 1, not 3, 1, 1. "
                  "Then a word fills a line alone, where dividing by the gap count would crash.")]


def main():
    args = cli()
    sc = build(WORDS, WIDTH, f'maxWidth = {WIDTH}. Each line must be exactly {WIDTH} characters wide.')
    finish(sc, 68, 'Watch line 2, "example of text": 3 spare spaces won\'t split evenly over 2 gaps, '
                   'so the extra one goes to the left gap.',
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
