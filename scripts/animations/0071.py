#!/usr/bin/env python3
"""#71 Simplify Path: split on '/', then a stack of folder names. A name is
pushed, '..' pops (unless already at the root), '' and '.' are skipped.

The trace comes from running the notebook's Python solution with a recorder
added; the algorithm lines are unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from anim_lib import *  # noqa: E402,F403

PATH = "/.../a/../b/c/../d/./"     # LeetCode example 5: every kind of token

# Hard example 1: '..' when the stack is already empty. Folding the emptiness
# check into the elif (`elif part == '..' and stack:`) sends that '..' to the
# else branch, which pushes it as a folder name.
HARD1 = "/home/../../usr/./local/../bin//"
HARD1_ANSWER, HARD1_WRONG = "/usr/bin", "/../usr/bin"

# Hard example 2: '/./././' in a row. Cleaning the string first with
# replace('/./', '/') misses overlapping matches and leaves a '.' behind.
HARD2 = "/a///b/./././c/"
HARD2_ANSWER, HARD2_WRONG = "/a/b/c", "/a/b/./c"


class Solution:
    # ---- the notebook's solution, unchanged (used to check the answers) ----
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)


def wrong_elif(path):
    """First attempt: `elif part == '..' and stack`, so '..' at the root falls through to push."""
    stack = []
    for part in path.split('/'):
        if part == '' or part == '.':
            continue
        elif part == '..' and stack:
            stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)


def wrong_replace(path):
    """First attempt: tidy the string with replace() first, then only handle '..'."""
    p = path.replace('//', '/').replace('/./', '/')
    out = []
    for x in p.strip('/').split('/'):
        if x == '..':
            if out:
                out.pop()
        elif x:
            out.append(x)
    return '/' + '/'.join(out)


SAMPLES = ["/home/", "/home//foo/", "/home/user/Documents/../Pictures", "/../", PATH]
assert Solution().simplifyPath(HARD1) == HARD1_ANSWER and wrong_elif(HARD1) == HARD1_WRONG
assert Solution().simplifyPath(HARD2) == HARD2_ANSWER and wrong_replace(HARD2) == HARD2_WRONG
assert all(wrong_replace(s) == Solution().simplifyPath(s) for s in SAMPLES)   # passes every sample


def trace(path):
    events = []

    def rec(kind, **kw):
        events.append(dict(kind=kind, stack=list(stack), **kw))

    # ---- the notebook's solution, with rec() calls added ----
    stack = []
    parts = path.split('/')
    rec('split', k=None)
    for k, part in enumerate(parts):
        if part == '' or part == '.':
            rec('skip', k=k, part=part)
            continue
        elif part == '..':
            if stack:
                top = stack[-1]
                stack.pop()
                rec('pop', k=k, part=part, popped=top)
            else:
                rec('root', k=k, part=part)
        else:
            stack.append(part)
            rec('push', k=k, part=part)
    rec('done', k=None, ans='/' + '/'.join(stack))
    return parts, events


def words(e, first, notes):
    k, part = e['kind'], e.get('part')
    if k == 'split':
        return ("Split on '/'. Every piece is a folder name, '..', '.', or empty.",
                "Empty pieces come from the leading '/', from '//', and from a trailing '/'.", KEY)
    if k == 'skip':
        if part == '':
            if 'empty' not in first:
                first['empty'] = True
                return ("Empty piece: skip it. It just means two slashes were next to each other.",
                        "'/' at the start, '//' in the middle and '/' at the end all leave one.", KEY)
            return ("Empty piece: skip it.", "", QUICK * 1.6)
        if 'dot' not in first:
            first['dot'] = True
            return ("'.' means 'this folder': stay where you are, skip it.", notes.get('dot', ''), KEY)
        return ("'.' again: skip it.", notes.get('dot2', ''), STEP)
    if k == 'push':
        if part.startswith('.') and part not in ('.', '..'):
            return (f"'{part}' is a folder name, not '..'. Push it.",
                    "Only exactly '.' and '..' are special. Compare the whole piece, not how it starts.", KEY)
        return (f"'{part}' is a folder name: push it. We're now inside it.", "", STEP)
    if k == 'pop':
        if 'pop' not in first:
            first['pop'] = True
            return (f"'..' means 'go up one': pop '{e['popped']}' off the stack.",
                    notes.get('pop', "The top of the stack is always the folder we're in, so that's the one we leave."), KEY)
        return (f"'..': pop '{e['popped']}'.", "", STEP)
    if k == 'root':
        return ("'..' with an empty stack: we're at the root, and there's nothing above it. Do nothing.",
                notes.get('root', "The root's parent is the root. That's why the pop is guarded."), KEY)
    return (f"Join the stack with '/' and put '/' in front: {e['ans']}",
            notes.get('done', "Each piece was looked at once: O(n) for a path of n characters."), END)


def build(path, subtitle, notes=None):
    notes = notes or {}
    parts, events = trace(path)
    sc = Scene('#71 Simplify Path: split on "/", then push and pop folders', subtitle)
    legend = [(ACTIVE, 'piece being read'), (style('good')[1], 'pushed folder'),
              (style('muted')[1], 'skipped'), (style('bad')[1], 'popped by ..')]
    first, fate, owners = {}, {}, []
    for e in events:
        k = e.get('k')
        if e['kind'] in ('skip', 'root'):
            fate[k] = 'muted'
        elif e['kind'] == 'pop':
            fate[k] = 'muted'
            fate[owners.pop()] = 'bad'          # the folder this '..' left
        elif e['kind'] == 'push':
            fate[k] = 'good'
            owners.append(k)
        chips = []
        for j, p in enumerate(parts):
            label = p if p else '""'
            st = fate.get(j) if j != k else 'active'
            chips.append((f'{j}: {label}', st))
        out = '/' + '/'.join(e['stack'])
        cap, sub, hold = words(e, first, notes)
        main = [TextView([f'path = "{path}"'], size=17),
                ChipsView(chips, "pieces after split('/')", size=15),
                TextView([(f'"/" + "/".join(stack)  =  "{out}"', 'good' if e['kind'] == 'done' else None)],
                         title='answer so far', size=17)]
        stack = [(s, 'good') for s in e['stack']]
        sc.frame(main, cap, sub, hold,
                 side=StackView(stack, 'Folder stack', note='top = folder we are in', base='/  (root)',
                                empty=''),
                 counters={'depth': len(e['stack'])}, legend=legend)
    return sc


def hard():
    """Harder inputs for the interactive page (scripts/motion_build.py)."""
    sc1 = build(HARD1, f'path = "{HARD1}". Two ".." in a row climb past the top.',
                {'root': "Write `elif part == '..' and stack:` and this '..' falls into the push branch: "
                         "the answer becomes /../usr/bin.",
                 'done': "The '..' at the root did nothing. A folded-in check would have pushed it as a folder."})
    sc2 = build(HARD2, f'path = "{HARD2}". Three "." pieces in a row, and a triple slash.',
                {'dot2': "replace('/./', '/') can't see overlapping matches: it would leave one '.' here.",
                 'done': "Splitting handles any run of '.' and '/'. Tidying with replace() first answers /a/b/./c."})
    return [(sc1, "Two '..' in a row climb above the root. Folding the empty-stack check into the elif "
                  "pushes '..' as a folder name and answers /../usr/bin instead of /usr/bin."),
            (sc2, "Three '.' in a row. Cleaning the string with replace('/./', '/') first passes every LeetCode "
                  "sample but misses overlapping matches here, answering /a/b/./c.")]


def main():
    args = cli()
    sc = build(PATH, f'path = "{PATH}". Simplify it to the shortest absolute path.')
    finish(sc, 71, "Watch the '..' after 'a': it pops 'a' off the stack, while '...' a step earlier was "
                   "pushed, because only exactly '..' means 'go up'.",
           embed=not args.no_embed, preview_dir=args.preview, preview=args.frames)


if __name__ == '__main__':
    main()
