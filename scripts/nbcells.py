#!/usr/bin/env python3
"""Locate and edit notebook cells by CONTENT, never by a hardcoded index.

Cell positions shift whenever a section is added (the "Explain Like I'm a
Newbie" cell moved examples from index 9 to 10 and the infographic from 10 to
11). Anything that hardcodes those numbers silently edits the wrong cell, so
use these helpers instead.

    import json, nbcells
    nb = nbcells.load('leetcode/0200.ipynb')
    nbcells.set_infographic(nb, open('x.png','rb').read())
    nbcells.set_examples(nb, markdown_text)
    nbcells.save(nb, 'leetcode/0200.ipynb')
"""
import base64
import json

EXAMPLES_HEADING = '## Example Scenarios'
# 38 older notebooks shipped with the shorter heading; accept both so lookups
# never silently fail, even though new work should use EXAMPLES_HEADING.
EXAMPLES_HEADINGS = ('## Example Scenarios', '## Examples')
NEWBIE_HEADING = "## Explain Like I'm a Newbie"
SOLUTIONS_HEADING = '## Solutions'
IMAGE_ATTACHMENT = 'image.png'


# ---------------------------------------------------------------- io
def load(path):
    with open(path) as f:
        return json.load(f)


def save(nb, path):
    """Write back in the repo's canonical format (indent=1 + trailing newline)."""
    with open(path, 'w') as f:
        json.dump(nb, f, indent=1)
        f.write('\n')


def text(cell):
    src = cell.get('source', '')
    return ''.join(src) if isinstance(src, list) else src


def _set_text(cell, s):
    cell['source'] = s.splitlines(keepends=True)


# ---------------------------------------------------------------- locate
def find_by_heading(nb, heading):
    """Index of the first markdown cell starting with `heading`, else None."""
    for i, c in enumerate(nb['cells']):
        if c.get('cell_type') == 'markdown' and text(c).lstrip().startswith(heading):
            return i
    return None


def find_examples(nb):
    for h in EXAMPLES_HEADINGS:
        i = find_by_heading(nb, h)
        if i is not None:
            return i
    return None


def find_newbie(nb):
    return find_by_heading(nb, NEWBIE_HEADING)


def find_solutions(nb):
    return find_by_heading(nb, SOLUTIONS_HEADING)


def find_infographic(nb):
    """Index of the cell carrying the embedded PNG.

    Prefers a real attachment; falls back to the last markdown cell that
    references attachment:image.png (an un-embedded placeholder).
    """
    for i, c in enumerate(nb['cells']):
        if IMAGE_ATTACHMENT in (c.get('attachments') or {}):
            return i
    for i in range(len(nb['cells']) - 1, -1, -1):
        c = nb['cells'][i]
        if c.get('cell_type') == 'markdown' and 'attachment:image.png' in text(c):
            return i
    return None


def code_cells(nb):
    """[(index, source)] for every code cell, in order (C#, Python, Go, Rust)."""
    return [(i, text(c)) for i, c in enumerate(nb['cells'])
            if c.get('cell_type') == 'code']


# ---------------------------------------------------------------- edit
def set_examples(nb, markdown):
    i = find_examples(nb)
    if i is None:
        raise LookupError(f'no cell starting with {EXAMPLES_HEADING!r}')
    _set_text(nb['cells'][i], markdown)
    return i


def set_infographic(nb, png_bytes):
    """Embed a PNG into the infographic cell as a base64 attachment."""
    i = find_infographic(nb)
    if i is None:
        raise LookupError('no infographic cell found')
    cell = nb['cells'][i]
    cell['attachments'] = {IMAGE_ATTACHMENT:
                           {'image/png': base64.b64encode(png_bytes).decode('ascii')}}
    cell['source'] = ['![image.png](attachment:image.png)']
    return i


def get_infographic(nb):
    """Raw PNG bytes of the embedded infographic, or None."""
    i = find_infographic(nb)
    if i is None:
        return None
    att = (nb['cells'][i].get('attachments') or {}).get(IMAGE_ATTACHMENT)
    return base64.b64decode(att['image/png']) if att else None


def upsert_newbie(nb, markdown):
    """Insert (or replace) the newbie section just before '## Solutions'."""
    i = find_newbie(nb)
    if i is not None:
        _set_text(nb['cells'][i], markdown)
        return i
    at = find_solutions(nb)
    if at is None:
        at = 1
    nb['cells'].insert(at, {'cell_type': 'markdown', 'metadata': {},
                            'source': markdown.splitlines(keepends=True)})
    return at


# ---------------------------------------------------------------- check
def audit(nb):
    """Quick structural report used by verification passes."""
    ex, ig = find_examples(nb), find_infographic(nb)
    c9 = text(nb['cells'][ex]) if ex is not None else ''
    return {
        'cells': len(nb['cells']),
        'examples_at': ex,
        'infographic_at': ig,
        'newbie_at': find_newbie(nb),
        'scenario_headings': c9.count('### '),
        'has_image': ig is not None and IMAGE_ATTACHMENT in (nb['cells'][ig].get('attachments') or {}),
        'code_cells': len(code_cells(nb)),
    }
