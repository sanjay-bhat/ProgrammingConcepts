#!/usr/bin/env python3
"""#65 Valid Number: one pass, three flags (seen_digit, seen_dot, seen_exp) and
one rule per kind of character. The e/E resets seen_digit so the exponent has
to bring digits of its own.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

S = "-123.456e789"   # one of LeetCode's listed valid numbers

# Hard examples (interactive page only), each breaking a plausible first attempt
# that passes all three LeetCode samples ("0", "e", ".").
# 1) No reset of seen_digit at the e: "+3.14e-" ends with seen_digit still true
#    from the 4, so it returns true. Answer false.
HARD_RESET = "+3.14e-"
# 2) A dot rule that only checks for a second dot: the dot after the exponent
#    in "6e6.5" is accepted, so it returns true. Answer false.
HARD_DOT = "6e6.5"
NOTES_RESET = {
    5: "The e resets seen_digit to false. Skip this line and the 1, 4 from before the e would still count: "
       "the scan would end true.",
    'done': "Nothing after the sign: seen_digit is false, so the answer is false. Without the reset it would be "
            "true, though all three LeetCode samples still pass.",
}
NOTES_DOT = {
    3: "A dot after the e. The exponent must be a whole number, so seen_exp rejects it. A rule that only "
       "checks for a second dot lets it through and answers true.",
}


class Solution:
    """The notebook's solution, to cross-check the traced run."""
    def isNumber(self, s):
        seen_digit = seen_dot = seen_exp = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif c == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif c in 'eE':
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            else:
                return False
        return seen_digit


def no_reset(s):
    """First attempt: the e doesn't reset seen_digit."""
    seen_digit = seen_dot = seen_exp = False
    for i, c in enumerate(s):
        if c.isdigit():
            seen_digit = True
        elif c in '+-':
            if i > 0 and s[i-1] not in 'eE':
                return False
        elif c == '.':
            if seen_dot or seen_exp:
                return False
            seen_dot = True
        elif c in 'eE':
            if seen_exp or not seen_digit:
                return False
            seen_exp = True
        else:
            return False
    return seen_digit


def dot_ignores_exp(s):
    """First attempt: a dot is only rejected if it's the second dot."""
    seen_digit = seen_dot = seen_exp = False
    for i, c in enumerate(s):
        if c.isdigit():
            seen_digit = True
        elif c in '+-':
            if i > 0 and s[i-1] not in 'eE':
                return False
        elif c == '.':
            if seen_dot:
                return False
            seen_dot = True
        elif c in 'eE':
            if seen_exp or not seen_digit:
                return False
            seen_exp = True
            seen_digit = False
        else:
            return False
    return seen_digit


def trace(s):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, flags=(seen_digit, seen_dot, seen_exp), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    seen_digit = seen_dot = seen_exp = False
    rec('start')
    result = None
    for i, c in enumerate(s):
        if c.isdigit():
            seen_digit = True
            rec('digit', i=i)
        elif c in '+-':
            if i > 0 and s[i-1] not in 'eE':
                rec('reject', i=i, why='a sign that is neither first nor right after e')
                result = False
                break
            rec('sign', i=i)
        elif c == '.':
            if seen_dot or seen_exp:
                rec('reject', i=i, why='a second dot' if seen_dot else 'a dot inside the exponent')
                result = False
                break
            seen_dot = True
            rec('dot', i=i)
        elif c in 'eE':
            if seen_exp or not seen_digit:
                rec('reject', i=i, why='a second e' if seen_exp else 'an e with no digit before it')
                result = False
                break
            seen_exp = True
            seen_digit = False
            rec('exp', i=i)
        else:
            rec('reject', i=i, why=f"'{c}', which is never allowed")
            result = False
            break
    if result is None:
        result = seen_digit
        rec('end', result=result)
    else:
        rec('done_reject', result=result)
    assert result == Solution().isNumber(s)
    return events


KIND_STYLE = {'digit': 'region0', 'sign': 'region4', 'dot': 'region3', 'exp': 'region2'}


def char_kind(c):
    return 'digit' if c.isdigit() else 'sign' if c in '+-' else 'dot' if c == '.' else 'exp' if c in 'eE' else 'other'


def build(s, subtitle, notes=None):
    notes = notes or {}
    sc = Scene('#65 Valid Number: three flags, one pass', subtitle, side_width=270)
    legend = [(style('region0')[1], 'digit'), (style('region4')[1], 'sign'), (style('region3')[1], 'dot'),
              (style('region2')[1], 'e / E'), (style('bad')[1], 'rejected')]
    seen_kinds = set()
    for e in trace(s):
        k = e['kind']
        i = e.get('i')
        done_upto = i if i is not None else (len(s) - 1 if k == 'end' else -1)
        styles = {}
        for j, c in enumerate(s):
            if j <= done_upto:
                styles[j] = KIND_STYLE.get(char_kind(c), 'bad')
            else:
                styles[j] = 'plain'
        ptr = {'i': i} if i is not None else {}
        d, dot, ex = e['flags']
        hold, sub = STEP, ''
        if k == 'start':
            cap = f'Is "{s}" a number? Scan once, left to right, with three flags.'
            sub = "seen_digit, seen_dot, seen_exp all start false."
        elif k == 'digit':
            cap = f"'{s[i]}' is a digit: seen_digit = true."
            hold = STEP if 'digit' not in seen_kinds else QUICK * 1.6
        elif k == 'sign':
            cap = (f"'{s[i]}' is the first character: a sign is allowed here." if i == 0 else
                   f"'{s[i]}' comes right after '{s[i - 1]}': a sign is allowed there too.")
            sub = "Signs are legal only at the start of a part: index 0, or straight after the e."
        elif k == 'dot':
            cap = "'.' is the first dot, and no e yet: allowed. seen_dot = true."
            sub = "A dot is fine before any digit (\".9\") or after them (\"4.\"), but only before the e."
        elif k == 'exp':
            cap = f"'{s[i]}': a digit came before it and it's the first e. seen_exp = true, seen_digit = false."
            sub = "The reset: digits before the e don't count for the exponent. It needs its own."
            hold = KEY
        elif k == 'reject':
            styles[i] = 'bad'
            cap = f"'{s[i]}' at index {i} is {e['why']}: return false."
            hold = KEY
        elif k == 'end':
            cap = f"End of the string. seen_digit is {str(e['result']).lower()}: return {str(e['result']).lower()}."
            sub = ("The last part read, the exponent if there was one, has its own digits." if e['result'] else
                   "The last part read has no digits of its own.")
            hold = END
        else:
            cap = "Answer: false."
            hold = END
        if k in ('digit', 'sign', 'dot', 'exp'):
            seen_kinds.add(k)
        key = 'done' if k in ('end', 'done_reject') else i
        if key in notes:
            sub = notes[key]
            hold = END if key == 'done' else KEY
        arr = ArrayView(list(s), styles=styles, pointers=ptr, title='s')
        part = 'exponent' if ex else 'number'
        text = TextView([f"reading the {part} part" + (", which needs its own digits" if ex else '')], size=16)
        rows = [('seen_digit', str(d).lower(), 'good' if d else None), ('seen_dot', str(dot).lower(), 'good' if dot else None),
                ('seen_exp', str(ex).lower(), 'good' if ex else None)]
        rows = [r if r[2] else r[:2] for r in rows]
        sc.frame([arr, text], cap, sub, hold, side=MapView(rows, 'Flags', headers=('flag', 'value')), legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    for f in (no_reset, dot_ignores_exp):
        assert [f(x) for x in ('0', 'e', '.')] == [True, False, False]   # both pass all three samples
    assert Solution().isNumber(HARD_RESET) is False and no_reset(HARD_RESET) is True
    assert Solution().isNumber(HARD_DOT) is False and dot_ignores_exp(HARD_DOT) is True
    a = build(HARD_RESET, 's = "+3.14e-": the e has a sign after it but no digits. Answer false.', NOTES_RESET)
    b = build(HARD_DOT, 's = "6e6.5": a decimal exponent. Answer false.', NOTES_DOT)
    return [
        (a, "\"+3.14e-\" ends right after the exponent's sign. Without the reset at the e, the digits before it still "
            "count and the scan answers true; the right answer is false."),
        (b, "\"6e6.5\" puts a dot in the exponent. A dot rule that only checks for a second dot answers true; the "
            "exponent must be a whole number, so the answer is false."),
    ]


def main():
    args = cli()
    sc = build(S, f's = "{S}". Sign, digits, one dot, then e and the exponent\'s own digits.')
    finish(sc, 65, "Watch the e: it resets seen_digit to false, so the 789 after it have to set it again, "
                   "and that one line is what makes \"1e\" invalid.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
