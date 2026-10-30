#!/usr/bin/env python3
"""Fail if a notebook's code cells changed in anything but comments/whitespace.

    python3 scripts/check_code_unchanged.py <worktree> <NNNN> <base-ref>

Compares each code cell with the same notebook at <base-ref> after removing
comments (// and /* */ in C#/Go/Rust; # comments and docstrings in Python)
and all whitespace. Only Python runs on this machine, so this is the guard
that commenting C#, Go and Rust didn't change them. A deliberate bug fix
fails it, correctly: say so in the commit message.
"""
import io
import json
import re
import subprocess
import sys
import tokenize


def strip_python(src):
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type == tokenize.COMMENT:
                continue
            if tok.type == tokenize.STRING and tok.string.lstrip('rbuRBU').startswith(('"""', "'''")):
                continue                                   # docstrings count as comments
            out.append(tok.string)
    except (tokenize.TokenError, IndentationError):
        return src
    return ''.join(out)


def strip_clike(src):
    src = re.sub(r"'(?:\\.|[^'\\\n])'", "'c'", src)      # char literals like '"'
    out, i, n = [], 0, len(src)
    while i < n:
        ch = src[i]
        if ch in '"`':                                     # string / Go raw string
            j = i + 1
            while j < n and src[j] != ch:
                j += 2 if src[j] == '\\' and ch == '"' else 1
            out.append(src[i:j + 1])
            i = j + 1
        elif src.startswith('//', i):
            while i < n and src[i] != '\n':
                i += 1
        elif src.startswith('/*', i):
            j = src.find('*/', i + 2)
            i = n if j < 0 else j + 2
        else:
            out.append(ch)
            i += 1
    return ''.join(out)


def norm(src, idx):
    s = strip_python(src) if idx == 1 else strip_clike(src)
    return re.sub(r'\s+', '', s)


def cells(nb):
    return [''.join(c['source']) if isinstance(c['source'], list) else c['source']
            for c in nb['cells'] if c['cell_type'] == 'code']


def main():
    wt, num, base = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    path = f'leetcode/{num:04d}.ipynb'
    old = json.loads(subprocess.run(['git', '-C', wt, 'show', f'{base}:{path}'],
                                    capture_output=True, text=True, check=True).stdout)
    with open(f'{wt}/{path}') as f:
        new = json.load(f)
    a, b = cells(old), cells(new)
    if len(a) != len(b):
        sys.exit(f'#{num}: code cell count changed {len(a)} -> {len(b)}')
    bad = [i for i, (x, y) in enumerate(zip(a, b)) if norm(x, i) != norm(y, i)]
    if bad:
        sys.exit(f'#{num}: non-comment changes in code cell(s) {bad} (0=C#,1=Python,2=Go,3=Rust)')
    print(f'#{num}: code unchanged apart from comments')


if __name__ == '__main__':
    main()
