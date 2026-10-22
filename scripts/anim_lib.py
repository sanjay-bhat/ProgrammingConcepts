#!/usr/bin/env python3
"""Step-by-step animated walkthroughs ("Watch It Run") for the notebooks.

Each problem gets a small script in scripts/animations/NNNN.py that RUNS the
notebook's algorithm (an instrumented copy of the Python solution), records a
state at every step that matters, and hands each state to a Scene as a list
of views. Never hand-write the trace: if the code and the animation can
disagree, one day they will.

    from anim_lib import *
    sc = Scene('#200 Number of Islands: sweep and sink',
               '1 = land, slashed = water (0). Only up/down/left/right connect.')
    sc.frame([GridView(cells, outlines=...), StackView(calls, 'Call stack')],
             'sink(0,1): set it to 0 FIRST, then try down, up, right, left.',
             'Marking before recursing stops two neighbours calling each other.',
             hold=STEP, counters={'islands': 1})
    sc.save_gif('/path/out.gif')           # shared palette + gifsicle, ~300-500 KB

Layout: a title band, a main area on the left, an optional side panel on the
right, and a two-line caption at the bottom. Views take a box and size
themselves to fit it; Scene.frame places them (see Scene.frame for how).

Holds: QUICK for routine steps the eye only needs to register (water skipped,
a neighbour rejected), STEP for ordinary progress, KEY for the moments the
whole problem turns on. Pause on the aha; hurry through the bookkeeping.
"""
import io
import math
import os
import shutil
import subprocess

from PIL import Image, ImageDraw, ImageFont

QUICK, STEP, KEY, END = 0.45, 1.3, 2.6, 4.0

# ------------------------------------------------------------------ theme
BG, CARD, INK, MUTED, FAINT = '#eef1f5', '#ffffff', '#1f2430', '#5b6475', '#d5dae2'
PANEL, PANEL_BORDER = '#f7f8fa', '#d5dae2'
CAPTION_BG, CAPTION_BORDER = '#fff8e6', '#e0c27a'
WATER, WATER_BORDER, SLASH = '#e6e9ee', '#c5ccd6', '#9fb6d6'
CURSOR, ACTIVE, REJECT = '#1f2430', '#e8590c', '#c92a2a'

# name -> (fill, border, text)
STYLES = {
    'plain':  ('#ffffff', '#c5ccd6', INK),
    'active': ('#fff1e6', '#e8590c', '#8a3a06'),     # what the algorithm is looking at now
    'good':   ('#e4f7ea', '#2f9e58', '#155724'),     # matched / kept / answer
    'bad':    ('#fde8e8', '#c92a2a', '#7a1a1a'),     # rejected / conflict
    'muted':  ('#f1f3f6', '#dde1e7', '#a3abb8'),     # done with, out of play
    'window': ('#e7f0fb', '#2f7e9e', '#1a4f6b'),     # inside the current range
    'land':   ('#f3e3c3', '#b08a4a', '#6b4e1f'),
    'gold':   ('#f5eed4', '#9e8e2f', '#6b5f1a'),
}
REGIONS = [  # distinct components / islands / groups, cycle in order
    ("#d4f5d4", "#2f9e58", "#1a6b35"), ("#d4e8f5", "#2f7e9e", "#1a4f6b"),
    ("#f5d4e8", "#9e2f7e", "#6b1a4f"), ("#f5eed4", "#9e8e2f", "#6b5f1a"),
    ("#e8d4f5", "#7e2f9e", "#4f1a6b"), ("#d4f5ef", "#2f9e8e", "#1a6b5f"),
    ("#f5ddd4", "#9e5a2f", "#6b3a1a"), ("#ddf5d4", "#5a9e2f", "#3a6b1a"),
    ("#f5d4d4", "#9e2f2f", "#6b1a1a"), ("#d4ddf5", "#2f5a9e", "#1a3a6b"),
]
for _i, _t in enumerate(REGIONS):
    STYLES[f'region{_i}'] = _t


def style(name):
    """(fill, border, text) for a style name or 'regionN' (N wraps)."""
    if name and name.startswith('region'):
        return REGIONS[int(name[6:]) % len(REGIONS)]
    return STYLES[name or 'plain']


def _key_colors():
    cols = {BG, CARD, INK, MUTED, FAINT, PANEL, PANEL_BORDER, CAPTION_BG, CAPTION_BORDER,
            WATER, WATER_BORDER, SLASH, CURSOR, ACTIVE, REJECT}
    for t in list(STYLES.values()) + REGIONS:
        cols.update(t)
    return [tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) for c in sorted(cols)]


# ------------------------------------------------------------------ fonts
S = 2   # supersample factor: draw at 2x, downscale once for clean text
_F = '/System/Library/Fonts/'
_cache = {}


def font(kind, size):
    """kind: 'sans' | 'bold' | 'mono' | 'monob' | 'uni'. Sizes are in output pixels.

    Sans is San Francisco (it has arrows and ≤ ≥ that Helvetica Neue lacks);
    'uni' is Arial Unicode, used automatically for strings with rarer symbols.
    """
    key = (kind, size)
    if key not in _cache:
        spec = {'sans': ('SFNS.ttf', 0, b'Regular'), 'bold': ('SFNS.ttf', 0, b'Bold'),
                'mono': ('Menlo.ttc', 0, None), 'monob': ('Menlo.ttc', 1, None),
                'uni': ('Supplemental/Arial Unicode.ttf', 0, None)}[kind]
        try:
            f = ImageFont.truetype(_F + spec[0], int(size * S), index=spec[1])
            if spec[2]:
                f.set_variation_by_name(spec[2])
        except OSError:                                  # non-macOS fallback
            f = ImageFont.load_default(size=int(size * S))
        _cache[key] = f
    return _cache[key]


_missing = {}


def _has_glyphs(kind, s):
    """False if any character in s would render as a missing-glyph box."""
    f = font(kind, 20)
    nd = _missing.setdefault(kind, bytes(f.getmask('\uffff')))
    return all(ch.isascii() or bytes(f.getmask(ch)) != nd for ch in s)


def _pick(kind, s):
    return kind if _has_glyphs(kind, s) else 'uni'


# ------------------------------------------------------------------ drawing kit
class Pen:
    """Thin wrapper so views draw in output pixels; scaling is handled here."""

    def __init__(self, im):
        self.d = ImageDraw.Draw(im)

    def box(self, b, fill=None, outline=None, width=1, r=8):
        self.d.rounded_rectangle([v * S for v in b], radius=r * S, fill=fill,
                                 outline=outline, width=max(1, int(width * S)))

    def line(self, pts, fill=INK, width=2):
        self.d.line([(x * S, y * S) for x, y in pts], fill=fill, width=int(width * S))

    def circle(self, cx, cy, r, fill=None, outline=None, width=2):
        self.d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
                       fill=fill, outline=outline, width=int(width * S))

    def text(self, xy, s, kind='sans', size=16, fill=INK, anchor='la'):
        s = str(s)
        self.d.text((xy[0] * S, xy[1] * S), s, font=font(_pick(kind, s), size),
                    fill=fill, anchor=anchor)

    def width(self, s, kind='sans', size=16):
        s = str(s)
        return self.d.textlength(s, font=font(_pick(kind, s), size)) / S

    def fit(self, s, kind, size, maxw, minsize=10):
        """Largest size <= `size` at which `s` fits in `maxw`."""
        while size > minsize and self.width(s, kind, size) > maxw:
            size -= 1
        return size

    def arrow(self, a, b, fill=INK, width=2.5, head=9, shorten=0):
        (x1, y1), (x2, y2) = a, b
        ang = math.atan2(y2 - y1, x2 - x1)
        x1 += shorten * math.cos(ang); y1 += shorten * math.sin(ang)
        x2 -= shorten * math.cos(ang); y2 -= shorten * math.sin(ang)
        self.line([(x1, y1), (x2, y2)], fill, width)
        p1 = (x2 - head * math.cos(ang - 0.45), y2 - head * math.sin(ang - 0.45))
        p2 = (x2 - head * math.cos(ang + 0.45), y2 - head * math.sin(ang + 0.45))
        self.d.polygon([(x2 * S, y2 * S), (p1[0] * S, p1[1] * S), (p2[0] * S, p2[1] * S)], fill=fill)

    def curve_arrow(self, a, b, lift=40, fill=INK, width=2.5, head=9):
        """Quadratic arc from a to b bowing upward by `lift` (negative bows down)."""
        (x1, y1), (x2, y2) = a, b
        cx, cy = (x1 + x2) / 2, min(y1, y2) - lift
        pts = [((1 - t) ** 2 * x1 + 2 * (1 - t) * t * cx + t * t * x2,
                (1 - t) ** 2 * y1 + 2 * (1 - t) * t * cy + t * t * y2)
               for t in [i / 24 for i in range(25)]]
        self.line(pts[:-1], fill, width)
        self.arrow(pts[-3], pts[-1], fill, width, head)


def _cell(p, b, st, label='', sub='', size=None, slash=False, lw=2.5):
    """One labelled square: the atom most views are built from."""
    x0, y0, x1, y1 = b
    if slash:
        p.box(b, WATER, WATER_BORDER, 2)
        p.line([(x0 + 10, y1 - 10), (x1 - 10, y0 + 10)], SLASH, 3)
    else:
        fill, border, tc = style(st)
        p.box(b, fill, border, lw)
    if label != '' and not slash:
        w = x1 - x0
        fs = p.fit(label, 'monob', size or int(min(w, y1 - y0) * 0.36), w - 8)
        p.text(((x0 + x1) / 2, (y0 + y1) / 2 - (6 if sub else 0)), label, 'monob', fs,
               style(st)[2], 'mm')
    if sub:
        p.text(((x0 + x1) / 2, y1 - 11), sub, 'sans', 11, style(st)[2] if not slash else MUTED, 'mm')


def _ring(p, b, color, width=4, pad=4, r=11):
    x0, y0, x1, y1 = b
    p.box((x0 - pad, y0 - pad, x1 + pad, y1 + pad), None, color, width, r)


# ------------------------------------------------------------------ views
class View:
    """A view draws itself into box (x0, y0, x1, y1) and reports the height it
    actually used via .used (so Scene can stack views vertically)."""
    used = 0

    def draw(self, p, box):
        raise NotImplementedError


class GridView(View):
    """2D grid. `cells[r][c]` is a dict (or None for plain empty):
        {'style': 'land'|'regionN'|..., 'label': '1', 'sub': 'island 1', 'water': True}
    outlines: [((r, c), color, width)] rings drawn on top (cursor, active...).
    bridges: draw connectors between orthogonal neighbours sharing a region.
    marks: {(r, c): text} small badge in the top-right corner (e.g. '×').
    """

    def __init__(self, cells, outlines=(), bridges=True, marks=None, indices=True, cell=None):
        self.cells, self.outlines, self.bridges = cells, outlines, bridges
        self.marks, self.indices, self.cell = marks or {}, indices, cell

    def draw(self, p, box):
        rows, cols = len(self.cells), len(self.cells[0])
        x0, y0, x1, y1 = box
        off = 24 if self.indices else 0
        gap = 10
        size = self.cell or int(min((x1 - x0 - off - gap * (cols - 1)) / cols,
                                    (y1 - y0 - off - gap * (rows - 1)) / rows, 80))
        gap = max(4, min(10, size // 7))
        ox, oy = x0 + off, y0 + off
        at = lambda r, c: (ox + c * (size + gap), oy + r * (size + gap))
        if self.indices:
            for c in range(cols):
                p.text((at(0, c)[0] + size / 2, y0 + 8), c, 'sans', 13, MUTED, 'mm')
            for r in range(rows):
                p.text((x0 + 8, at(r, 0)[1] + size / 2), r, 'sans', 13, MUTED, 'mm')
        get = lambda r, c: self.cells[r][c] or {}
        if self.bridges:
            for r in range(rows):
                for c in range(cols):
                    st = get(r, c).get('style', '')
                    if not st.startswith('region'):
                        continue
                    bc = style(st)[1]
                    x, y = at(r, c)
                    t = max(6, size // 5)
                    if c + 1 < cols and get(r, c + 1).get('style') == st:
                        p.box((x + size - 4, y + size / 2 - t / 2, x + size + gap + 4, y + size / 2 + t / 2), bc, r=2)
                    if r + 1 < rows and get(r + 1, c).get('style') == st:
                        p.box((x + size / 2 - t / 2, y + size - 4, x + size / 2 + t / 2, y + size + gap + 4), bc, r=2)
        for r in range(rows):
            for c in range(cols):
                d = get(r, c)
                x, y = at(r, c)
                _cell(p, (x, y, x + size, y + size), d.get('style', 'plain'), d.get('label', ''),
                      d.get('sub', '') if size >= 60 else '', slash=d.get('water', False))
        for (r, c), txt in self.marks.items():
            x, y = at(r, c)
            p.text((x + size - 11, y + 13), txt, 'bold', 16, REJECT, 'mm')
        for (r, c), color, w in self.outlines:
            x, y = at(r, c)
            _ring(p, (x, y, x + size, y + size), color, w)
        self.used = off + rows * size + (rows - 1) * gap


class ArrayView(View):
    """A row of cells with indices above and named pointers below.
        values:   list of values
        styles:   {index: style}  (default 'plain')
        pointers: {'L': 0, 'R': 5} -> labelled carets under the cells; several
                  pointers on one index stack downward
        window:   (lo, hi) inclusive -> a bracket under the range
        title:    optional label at the left (e.g. 'nums')
        cuts:     [i, ...] -> a divider drawn just before cell i (i == len(values)
                  means after the last cell): partitions, split points
    """

    def __init__(self, values, styles=None, pointers=None, window=None, title=None,
                 indices=True, subs=None, cell=None, cuts=()):
        self.values, self.styles = values, styles or {}
        self.pointers, self.window, self.title = pointers or {}, window, title
        self.indices, self.subs, self.cell = indices, subs or {}, cell
        self.cuts = cuts

    def draw(self, p, box):
        x0, y0, x1, _ = box
        n = max(1, len(self.values))
        tw = (p.width(self.title, 'monob', 15) + 14) if self.title else 0
        gap = 6
        size = self.cell or int(min((x1 - x0 - tw - gap * (n - 1)) / n, 62))
        gap = max(3, min(6, size // 9))
        top = y0 + (18 if self.indices else 0)
        if self.title:
            p.text((x0, top + size / 2), self.title, 'monob', 15, MUTED, 'lm')
        at = lambda i: x0 + tw + i * (size + gap)
        for i, v in enumerate(self.values):
            x = at(i)
            if self.indices:
                p.text((x + size / 2, y0 + 6), i, 'sans', 12, MUTED, 'mm')
            _cell(p, (x, top, x + size, top + size), self.styles.get(i, 'plain'),
                  '' if v is None else v, self.subs.get(i, ''))
        for i in self.cuts:
            cx = at(i) - gap / 2
            p.line([(cx, top - 8), (cx, top + size + 8)], ACTIVE, 4)
        y = top + size + 6
        if self.window:
            lo, hi = self.window
            if lo <= hi:
                xa, xb = at(lo), at(hi) + size
                p.line([(xa, y), (xa, y + 7), (xb, y + 7), (xb, y)], style('window')[1], 3)
            y += 12
        stacks = {}
        for name, i in self.pointers.items():
            if i is None or not (0 <= i < n):
                continue
            k = stacks.get(i, 0); stacks[i] = k + 1
            cx = at(i) + size / 2
            yy = y + k * 22
            p.d.polygon([(cx * S, yy * S), ((cx - 6) * S, (yy + 9) * S), ((cx + 6) * S, (yy + 9) * S)], fill=ACTIVE)
            p.text((cx, yy + 17), name, 'monob', 13, ACTIVE, 'mm')
        deepest = max(stacks.values()) if stacks else 0
        self.used = (y - y0) + deepest * 22 + (4 if deepest else 0)


class StackView(View):
    """Vertical stack (newest on top) — call stacks, explicit stacks, monotonic stacks.
    items: list bottom -> top of str or (str, style). `base` is an optional greyed
    bottom row (e.g. the caller)."""

    def __init__(self, items, title='Stack', note='newest on top', base=None, empty='(empty)'):
        self.items, self.title, self.note, self.base, self.empty = items, title, note, base, empty

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        p.box(box, PANEL, PANEL_BORDER, 2, 12)
        p.text((x0 + 16, y0 + 14), self.title, 'bold', 18)
        if self.note:
            p.text((x0 + 16, y0 + 40), self.note, 'sans', 13, MUTED)
        rowh, step = 30, 38
        y = y1 - 16 - rowh
        if self.base:
            p.box((x0 + 16, y, x1 - 16, y + rowh), '#e9ecf1', WATER_BORDER, 1, 6)
            p.text((x0 + 28, y + rowh / 2), self.base, 'mono', p.fit(self.base, 'mono', 16, x1 - x0 - 56), MUTED, 'lm')
            y -= step
        room = int((y - (y0 + 60)) / step) + 1
        items = self.items[-room:] if room > 0 else []
        hidden = len(self.items) - len(items)
        for k, it in enumerate(items):
            s, st = (it, None) if isinstance(it, str) else it
            top = k == len(items) - 1
            fill, border, tc = style(st) if st else (CARD, INK, INK)
            p.box((x0 + 16, y, x1 - 16, y + rowh), fill, ACTIVE if top else border, 3 if top else 1, 6)
            p.text((x0 + 28, y + rowh / 2), s, 'monob' if top else 'mono',
                   p.fit(s, 'mono', 16, x1 - x0 - 56), tc, 'lm')
            y -= step
        if hidden:
            p.text(((x0 + x1) / 2, y + rowh / 2), f'… {hidden} more below', 'sans', 13, MUTED, 'mm')
        if not self.items:
            p.text(((x0 + x1) / 2, (y0 + y1) / 2), self.empty, 'sans', 14, MUTED, 'mm')
        self.used = y1 - y0


class QueueView(View):
    """Horizontal queue, front on the left. items: list of str or (str, style)."""

    def __init__(self, items, title='Queue', empty='(empty)'):
        self.items, self.title, self.empty = items, title, empty

    def draw(self, p, box):
        x0, y0, x1, _ = box
        p.text((x0, y0 + 10), self.title, 'bold', 16, anchor='lm')
        p.text((x0 + p.width(self.title, 'bold', 16) + 10, y0 + 10), 'front → back', 'sans', 12, MUTED, 'lm')
        y = y0 + 26
        x = x0
        if not self.items:
            p.text((x0, y + 18), self.empty, 'sans', 14, MUTED, 'lm')
        for it in self.items:
            s, st = (it, None) if isinstance(it, str) else it
            w = max(44, p.width(s, 'monob', 15) + 20)
            if x + w > x1:
                p.text((x + 4, y + 18), '…', 'bold', 18, MUTED, 'lm')
                break
            _cell(p, (x, y, x + w, y + 36), st or 'plain', s, size=15)
            x += w + 6
        self.used = 26 + 36


class MapView(View):
    """Key -> value table (hash maps, counters, memo). rows: list of (key, value)
    or (key, value, style). Shows the newest rows when it overflows."""

    def __init__(self, rows, title='Hash map', headers=('key', 'value'), empty='(empty)'):
        self.rows, self.title, self.headers, self.empty = rows, title, headers, empty

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        p.box(box, PANEL, PANEL_BORDER, 2, 12)
        p.text((x0 + 16, y0 + 14), self.title, 'bold', 18)
        mid = x0 + (x1 - x0) * 0.5
        p.text((x0 + 22, y0 + 46), self.headers[0], 'sans', 13, MUTED)
        p.text((mid + 6, y0 + 46), self.headers[1], 'sans', 13, MUTED)
        y = y0 + 62
        rowh = 30
        room = max(0, int((y1 - 12 - y) / (rowh + 6)))
        rows = self.rows[-room:] if room else []
        if len(self.rows) > len(rows):
            p.text((x1 - 16, y0 + 46), f'+{len(self.rows) - len(rows)} earlier', 'sans', 12, MUTED, 'ra')
        for row in rows:
            k, v = row[0], row[1]
            st = row[2] if len(row) > 2 else None
            fill, border, tc = style(st) if st else (CARD, FAINT, INK)
            p.box((x0 + 16, y, x1 - 16, y + rowh), fill, border, 2 if st else 1, 6)
            p.text((x0 + 26, y + rowh / 2), k, 'monob', p.fit(k, 'monob', 15, mid - x0 - 30), tc, 'lm')
            p.text((mid + 6, y + rowh / 2), v, 'mono', p.fit(v, 'mono', 15, x1 - mid - 30), tc, 'lm')
            y += rowh + 6
        if not self.rows:
            p.text(((x0 + x1) / 2, (y0 + y1) / 2 + 20), self.empty, 'sans', 14, MUTED, 'mm')
        self.used = y1 - y0


class ListView(View):
    """Singly linked list, drawn as a row of nodes.
        values:   node values in their array order
        nxt:      nxt[i] = index the node points to, or None (default: i+1, last None)
        styles:   {i: style}
        pointers: {'prev': i, 'curr': j} labels under nodes; None index -> shown at 'null'
        cut:      set of i whose outgoing arrow is drawn faded (just broken)
        extra:    [(i, j)] or [(i, j, color)] second pointers (random, child, skip)
                  drawn as arcs UNDER the row; i == j draws a small self-loop
    Arrows to i+1 are straight, to i-1 are drawn under the row, others arc above.
    With null=False a None in nxt draws no arrow at all (nodes not linked yet).
        title:    optional label at the left (e.g. 'list 0')
        room:     space kept above the row for arcs (default 46; ~8 for plain chains)
    """

    EXTRA = '#7e2f9e'

    def __init__(self, values, nxt=None, styles=None, pointers=None, cut=(), null=True, extra=(),
                 title=None, room=46):
        self.values = values
        self.nxt = nxt if nxt is not None else [i + 1 if i + 1 < len(values) else None for i in range(len(values))]
        self.styles, self.pointers, self.cut, self.null = styles or {}, pointers or {}, set(cut), null
        self.extra = list(extra)
        self.title, self.room = title, room

    def draw(self, p, box):
        x0, y0, x1, _ = box
        n = len(self.values)
        slots = max(1, n + (1 if self.null else 0))
        tw = (p.width(self.title, 'monob', 15) + 14) if self.title else 0
        size = int(min(58, (x1 - x0 - tw) / (slots * 1.75)))
        gap = int(size * 0.75)
        top = y0 + self.room
        if self.title:
            p.text((x0, top + size / 2), self.title, 'monob', 15, MUTED, 'lm')
            x0 += tw
        at = lambda i: x0 + i * (size + gap)
        nullx = at(n)
        for i, v in enumerate(self.values):
            _cell(p, (at(i), top, at(i) + size, top + size), self.styles.get(i, 'plain'), v)
        if self.null:
            p.text((nullx + size / 2, top + size / 2), 'null', 'mono', 14, MUTED, 'mm')
        for i, j in enumerate(self.nxt):
            col = FAINT if i in self.cut else INK
            if j is None:
                if self.null and i == n - 1:
                    p.arrow((at(i) + size, top + size / 2), (nullx + 4, top + size / 2), col)
                elif self.null:
                    p.curve_arrow((at(i) + size / 2, top), (nullx + size / 2, top - 2),
                                  lift=30 + 6 * (n - i), fill=col)
                continue
            if j == i + 1:
                p.arrow((at(i) + size, top + size / 2), (at(j), top + size / 2), col)
            elif j == i - 1:
                p.arrow((at(i), top + size / 2 + 10), (at(j) + size, top + size / 2 + 10), col)
            else:
                p.curve_arrow((at(i) + size / 2, top), (at(j) + size / 2, top - 2),
                              lift=24 + 8 * abs(j - i), fill=col)
        drop = 0                      # how far the extra arcs reach below the row
        for e in self.extra:
            i, j = e[0], e[1]
            col = e[2] if len(e) > 2 else self.EXTRA
            by = top + size
            if i == j:
                cx = at(i) + size / 2
                p.curve_arrow((cx - size * 0.3, by), (cx + size * 0.3, by + 2), lift=-34, fill=col, width=2)
                drop = max(drop, 17)
            else:
                lift = 26 + 8 * abs(j - i)
                p.curve_arrow((at(i) + size / 2 - 5, by), (at(j) + size / 2 + 5, by + 2), lift=-lift,
                              fill=col, width=2)
                drop = max(drop, lift / 2)
        stacks = {}
        for name, i in self.pointers.items():
            slot = n if i is None else i
            k = stacks.get(slot, 0); stacks[slot] = k + 1
            cx = at(slot) + size / 2
            yy = top + size + 8 + drop + k * 22
            p.d.polygon([(cx * S, yy * S), ((cx - 6) * S, (yy + 9) * S), ((cx + 6) * S, (yy + 9) * S)], fill=ACTIVE)
            p.text((cx, yy + 17), name, 'monob', 13, ACTIVE, 'mm')
        deepest = max(stacks.values()) if stacks else 0
        self.used = int(self.room + size + 12 + drop + deepest * 22)


class TreeView(View):
    """Binary tree from a LeetCode level-order list ([3,9,20,None,None,15,7]).
        styles: {node_index: style}   (index into the level-order list)
        labels: {node_index: text}    small tag under the node (visit order, depth...)
        edges:  {(parent_idx, child_idx): style}  highlighted edges
        rings:  [(node_index, color)]
    Node indices are positions in the level-order list, so the trace can refer to
    nodes without building a separate id scheme.
    """

    def __init__(self, level, styles=None, labels=None, edges=None, rings=()):
        self.level, self.styles = level, styles or {}
        self.labels, self.edges, self.rings = labels or {}, edges or {}, rings

    @staticmethod
    def structure(level):
        """[(idx, left_idx, right_idx)] following LeetCode's serialisation."""
        if not level or level[0] is None:
            return {}
        kids = {0: [None, None]}
        q, i = [0], 1
        while q and i < len(level):
            par = q.pop(0)
            for side in (0, 1):
                if i < len(level):
                    if level[i] is not None:
                        kids[par][side] = i
                        kids[i] = [None, None]
                        q.append(i)
                    i += 1
        return kids

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        kids = self.structure(self.level)
        if not kids:
            p.text(((x0 + x1) / 2, y0 + 30), '(empty tree)', 'sans', 15, MUTED, 'mm')
            self.used = 60
            return
        order, depth = [], {}

        def walk(i, d):
            if i is None:
                return
            depth[i] = d
            walk(kids[i][0], d + 1)
            order.append(i)
            walk(kids[i][1], d + 1)
        walk(0, 0)
        maxd = max(depth.values())
        r = int(min(24, (x1 - x0) / (len(order) * 2.4)))
        r = max(r, 13)
        dy = min(78, (y1 - y0 - 2 * r - 20) / max(1, maxd))
        xs = {i: x0 + r + k * (x1 - x0 - 2 * r) / max(1, len(order) - 1) for k, i in enumerate(order)}
        if len(order) == 1:
            xs = {order[0]: (x0 + x1) / 2}
        ys = {i: y0 + r + 4 + depth[i] * dy for i in order}
        for i, (a, b) in kids.items():
            for c in (a, b):
                if c is not None:
                    st = self.edges.get((i, c))
                    p.line([(xs[i], ys[i]), (xs[c], ys[c])], style(st)[1] if st else '#9aa3b2', 5 if st else 2.5)
        for i in order:
            fill, border, tc = style(self.styles.get(i, 'plain'))
            p.circle(xs[i], ys[i], r, fill, border, 3)
            v = str(self.level[i])
            p.text((xs[i], ys[i]), v, 'monob', p.fit(v, 'monob', int(r * 0.85), 2 * r - 6), tc, 'mm')
            if i in self.labels:
                p.text((xs[i], ys[i] + r + 11), self.labels[i], 'bold', 12, ACTIVE, 'mm')
        for i, color in self.rings:
            p.circle(xs[i], ys[i], r + 6, None, color, 4)
        self.used = int(2 * r + 8 + maxd * dy + (22 if self.labels else 6))


class GraphView(View):
    """Nodes + edges.
        nodes:  {id: (x, y)} positions in 0..1 (relative to the box), or a list of
                ids for an automatic circle layout
        edges:  [(u, v)] or [(u, v, label)]
        directed: draw arrowheads
        styles: {id: style}; edge_styles: {(u, v): style}
        labels: {id: text} small tag under the node
    """

    def __init__(self, nodes, edges, directed=False, styles=None, edge_styles=None,
                 labels=None, rings=(), height=None):
        if isinstance(nodes, (list, tuple)):
            k = len(nodes)
            nodes = {v: (0.5 + 0.42 * math.cos(2 * math.pi * i / k - math.pi / 2),
                         0.5 + 0.42 * math.sin(2 * math.pi * i / k - math.pi / 2))
                     for i, v in enumerate(nodes)}
        self.nodes, self.edges, self.directed = nodes, edges, directed
        self.styles, self.edge_styles = styles or {}, edge_styles or {}
        self.labels, self.rings, self.height = labels or {}, rings, height

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        if self.height:
            y1 = y0 + self.height
        r = 22
        pos = {v: (x0 + r + 6 + fx * (x1 - x0 - 2 * r - 12), y0 + r + 6 + fy * (y1 - y0 - 2 * r - 22))
               for v, (fx, fy) in self.nodes.items()}
        for e in self.edges:
            u, v = e[0], e[1]
            st = self.edge_styles.get((u, v)) or (None if self.directed else self.edge_styles.get((v, u)))
            col = style(st)[1] if st else '#9aa3b2'
            w = 4.5 if st else 2.5
            if self.directed:
                p.arrow(pos[u], pos[v], col, w, 11, shorten=r + 2)
            else:
                p.line([pos[u], pos[v]], col, w)
            if len(e) > 2:
                mx, my = (pos[u][0] + pos[v][0]) / 2, (pos[u][1] + pos[v][1]) / 2
                lw = p.width(e[2], 'bold', 12) + 10
                p.box((mx - lw / 2, my - 10, mx + lw / 2, my + 10), CARD, FAINT, 1, 5)
                p.text((mx, my), e[2], 'bold', 12, MUTED, 'mm')
        for v, (x, y) in pos.items():
            fill, border, tc = style(self.styles.get(v, 'plain'))
            p.circle(x, y, r, fill, border, 3)
            p.text((x, y), v, 'monob', p.fit(str(v), 'monob', 17, 2 * r - 6), tc, 'mm')
            if v in self.labels:
                p.text((x, y + r + 11), self.labels[v], 'bold', 12, ACTIVE, 'mm')
        for v, color in self.rings:
            p.circle(*pos[v], r + 6, None, color, 4)
        self.used = y1 - y0


class TableView(View):
    """DP table / matrix with headers.
        values: 2D list (None -> blank)
        row_labels / col_labels: header text
        styles: {(r, c): style}; rings: [((r, c), color)]
        arrows: [((r1, c1), (r2, c2))] dependency arrows (from -> to)
    """

    def __init__(self, values, row_labels=None, col_labels=None, styles=None, rings=(),
                 arrows=(), title=None):
        self.values, self.rl, self.cl = values, row_labels, col_labels
        self.styles, self.rings, self.arrows, self.title = styles or {}, rings, arrows, title

    def draw(self, p, box):
        x0, y0, x1, y1 = box
        rows, cols = len(self.values), len(self.values[0])
        ty = 24 if self.title else 0
        if self.title:
            p.text((x0, y0 + 8), self.title, 'bold', 16)
        lw = 0
        if self.rl:
            lw = max(p.width(s, 'monob', 14) for s in map(str, self.rl)) + 14
        hh = 22 if self.cl else 0
        gap = 4
        size = int(min((x1 - x0 - lw - gap * (cols - 1)) / cols,
                       (y1 - y0 - ty - hh - gap * (rows - 1)) / rows, 56))
        ox, oy = x0 + lw, y0 + ty + hh
        at = lambda r, c: (ox + c * (size + gap), oy + r * (size + gap))
        if self.cl:
            for c, s in enumerate(self.cl):
                p.text((at(0, c)[0] + size / 2, oy - 11), s, 'monob', 13, MUTED, 'mm')
        if self.rl:
            for r, s in enumerate(self.rl):
                p.text((x0 + lw - 10, at(r, 0)[1] + size / 2), s, 'monob', 13, MUTED, 'rm')
        for r in range(rows):
            for c in range(cols):
                x, y = at(r, c)
                v = self.values[r][c]
                _cell(p, (x, y, x + size, y + size), self.styles.get((r, c), 'plain'),
                      '' if v is None else v, lw=2)
        for a, b in self.arrows:
            (xa, ya), (xb, yb) = at(*a), at(*b)
            p.arrow((xa + size / 2, ya + size / 2), (xb + size / 2, yb + size / 2), ACTIVE, 3, 9,
                    shorten=size * 0.32)
        for (r, c), color in self.rings:
            x, y = at(r, c)
            _ring(p, (x, y, x + size, y + size), color, 4, 3, 9)
        self.used = ty + hh + rows * size + (rows - 1) * gap


class IntervalView(View):
    """Intervals on a number line. bars: list of (start, end, label, style);
    rows are assigned top to bottom in the given order. lo/hi fix the axis."""

    def __init__(self, bars, lo=None, hi=None, title=None, marker=None):
        self.bars, self.title, self.marker = bars, title, marker
        ends = [b[0] for b in bars] + [b[1] for b in bars] or [0, 1]
        self.lo = min(ends) if lo is None else lo
        self.hi = max(ends) if hi is None else hi

    def draw(self, p, box):
        x0, y0, x1, _ = box
        ty = 24 if self.title else 0
        if self.title:
            p.text((x0, y0 + 8), self.title, 'bold', 16)
        span = max(1, self.hi - self.lo)
        X = lambda v: x0 + 10 + (v - self.lo) / span * (x1 - x0 - 20)
        y = y0 + ty + 6
        for s, e, label, st in self.bars:
            fill, border, tc = style(st)
            p.box((X(s), y, max(X(e), X(s) + 6), y + 26), fill, border, 2, 6)
            p.text((X(s) + 8, y + 13), label, 'monob', 13, tc, 'lm')
            y += 34
        p.line([(x0 + 10, y + 6), (x1 - 10, y + 6)], MUTED, 2)
        step = max(1, round(span / 10))
        v = self.lo
        while v <= self.hi:
            p.line([(X(v), y + 2), (X(v), y + 10)], MUTED, 2)
            p.text((X(v), y + 20), v, 'sans', 12, MUTED, 'mm')
            v += step
        if self.marker is not None:
            p.line([(X(self.marker), y0 + ty), (X(self.marker), y + 6)], ACTIVE, 3)
        self.used = (y - y0) + 30


class TextView(View):
    """A few lines of monospace text (a running string, a formula, the output so far)."""

    def __init__(self, lines, title=None, size=16):
        self.lines, self.title, self.size = lines, title, size

    def draw(self, p, box):
        x0, y0, x1, _ = box
        y = y0
        if self.title:
            p.text((x0, y + 8), self.title, 'bold', 16); y += 26
        for ln in self.lines:
            s, st = (ln, None) if isinstance(ln, str) else ln
            p.text((x0, y + 10), s, 'mono', p.fit(s, 'mono', self.size, x1 - x0), style(st)[2] if st else INK)
            y += self.size + 10
        self.used = y - y0


class ChipsView(View):
    """A titled collection of small labelled chips that wraps onto new lines:
    the answers collected so far by a backtracking search, a set of words.
        items: list of str or (str, style), in the order they were added
        title: label above the chips; empty: text shown when there are none
        max_rows: when the chips need more rows, only the newest rows are shown
                  and a '+N earlier' note appears beside the title
    """

    def __init__(self, items, title=None, empty='(none yet)', size=15, max_rows=None):
        self.items, self.title, self.empty = items, title, empty
        self.size, self.max_rows = size, max_rows

    def draw(self, p, box):
        x0, y0, x1, _ = box
        y = y0
        if self.title:
            p.text((x0, y + 8), self.title, 'bold', 16)
            y += 26
        h, gap = self.size + 18, 6
        rows, row, w = [], [], 0
        for it in self.items:
            s, st = (it, None) if isinstance(it, str) else it
            cw = max(36, p.width(s, 'monob', self.size) + 18)
            if row and w + cw > x1 - x0:
                rows.append(row); row, w = [], 0
            row.append((s, st, cw)); w += cw + gap
        if row:
            rows.append(row)
        hidden = 0
        if self.max_rows and len(rows) > self.max_rows:
            hidden = sum(len(r) for r in rows[:-self.max_rows])
            rows = rows[-self.max_rows:]
        if hidden and self.title:
            p.text((x0 + p.width(self.title, 'bold', 16) + 12, y0 + 8), f'+{hidden} earlier',
                   'sans', 12, MUTED)
        if not self.items:
            p.text((x0, y + h / 2), self.empty, 'sans', 14, MUTED, 'lm')
            y += h + gap
        for r in rows:
            x = x0
            for s, st, cw in r:
                _cell(p, (x, y, x + cw, y + h), st or 'plain', s, size=self.size, lw=2)
                x += cw + gap
            y += h + gap
        self.used = y - y0 - gap


# ------------------------------------------------------------------ scene
class Scene:
    """Collects frames. Layout per frame:

        main:  list of views stacked top to bottom in the left area (or full
               width when `side` is None)
        side:  one view (usually a StackView/MapView/QueueView) in the right panel
        counters: {'islands': 2} pills in the title band, right-aligned
        legend:  [(color, text)] small key under the main area
    """

    def __init__(self, title, subtitle='', width=960, height=650, side_width=330):
        self.title, self.subtitle = title, subtitle
        self.W, self.H, self.side_w = width, height, side_width
        self.frames, self.holds = [], []

    def frame(self, main, caption, sub='', hold=STEP, side=None, counters=None, legend=None):
        W, H = self.W, self.H
        im = Image.new('RGB', (W * S, H * S), BG)
        p = Pen(im)
        p.box((20, 16, W - 20, H - 16), CARD, INK, 2, 14)
        cw = 0
        if counters:
            x = W - 44
            for k, v in reversed(list(counters.items())):
                s = f'{k}: {v}'
                w = p.width(s, 'bold', 18) + 40
                p.box((x - w, 36, x, 78), STYLES['good'][0], STYLES['good'][1], 2, 21)
                p.text((x - w / 2, 57), s, 'bold', 18, STYLES['good'][2], 'mm')
                x -= w + 10
                cw += w + 10
        p.text((44, 38), self.title, 'bold', p.fit(self.title, 'bold', 25, W - 100 - cw))
        if self.subtitle:
            p.text((44, 76), self.subtitle, 'sans', p.fit(self.subtitle, 'sans', 14, W - 100 - cw), MUTED)

        cap_top = H - 120
        top, bottom = 112, cap_top - (34 if legend else 14)
        right = W - 44 - (self.side_w + 24 if side else 0)
        y = top
        mains = main if isinstance(main, (list, tuple)) else [main]
        for v in mains:
            v.draw(p, (52, y, right, bottom))
            y += v.used + 22
        if side:
            side.draw(p, (W - 44 - self.side_w, top, W - 44, bottom))
        if legend:
            x = 52
            for color, label in legend:
                p.box((x, bottom + 10, x + 18, bottom + 28), None, color, 3, 4)
                p.text((x + 26, bottom + 11), label, 'sans', 13, MUTED)
                x += 26 + p.width(label, 'sans', 13) + 24

        p.box((44, cap_top, W - 44, H - 36), CAPTION_BG, CAPTION_BORDER, 2, 10)
        cy = cap_top + (22 if sub else 42)
        p.text((64, cy), caption, 'bold', p.fit(caption, 'bold', 19, W - 128), anchor='lm')
        if sub:
            p.text((64, cap_top + 52), sub, 'sans', p.fit(sub, 'sans', 18, W - 128), MUTED, 'lm')
        self.frames.append(im.resize((W, H), Image.LANCZOS))
        self.holds.append(hold)

    # -------------------------------------------------------------- output
    def gif_bytes(self, colors=48):
        """One shared palette: every design colour exactly, plus `colors` shades
        for anti-aliasing. Per-frame adaptive palettes made the GIF 5x larger,
        and a plain 64-colour quantise turned the orange/red outlines brown."""
        fr = self.frames
        sheet = Image.new('RGB', (fr[0].width, fr[0].height * min(len(fr), 12)))
        pick = fr[::max(1, len(fr) // 12)][:12]
        for i, f in enumerate(pick):
            sheet.paste(f, (0, i * f.height))
        extra = sheet.quantize(colors=colors, method=Image.Quantize.MEDIANCUT).getpalette()[:colors * 3]
        keys = _key_colors()
        pal = [c for rgb in keys for c in rgb] + extra
        pal = pal[:768] + [0] * (768 - len(pal[:768]))
        pimg = Image.new('P', (1, 1)); pimg.putpalette(pal)
        q = [f.quantize(palette=pimg, dither=Image.Dither.NONE) for f in fr]
        buf = io.BytesIO()
        q[0].save(buf, format='GIF', save_all=True, append_images=q[1:],
                  duration=[int(h * 1000) for h in self.holds], loop=0, optimize=True, disposal=1)
        data = buf.getvalue()
        if shutil.which('gifsicle'):
            out = subprocess.run(['gifsicle', '-O3'], input=data, capture_output=True)
            if out.returncode == 0 and out.stdout:
                data = out.stdout
        return data

    def save_gif(self, path):
        data = self.gif_bytes()
        with open(path, 'wb') as f:
            f.write(data)
        return data

    def save_frames(self, folder, which=None):
        """Dump selected frames as PNG for a quick look (which = list of indices)."""
        os.makedirs(folder, exist_ok=True)
        for i in (which if which is not None else range(len(self.frames))):
            self.frames[i].save(os.path.join(folder, f'frame_{i:03d}.png'))

    def summary(self, data):
        return f'{len(self.frames)} frames, {sum(self.holds):.1f}s, {len(data) // 1024} KB'


# ------------------------------------------------------------------ embedding
MAX_KB = 600   # per-GIF budget; 550+ notebooks x 600 KB is the repo's ceiling


def finish(scene, num, blurb, embed=True, preview_dir=None, preview=()):
    """Render the GIF, enforce the size budget, and embed it in leetcode/NNNN.ipynb.

    Call at the end of every scripts/animations/NNNN.py:
        finish(sc, 200, 'Watch (0,1): ...', preview_dir=args.preview)
    """
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import nbcells
    data = scene.gif_bytes()
    print(f'#{num}: {scene.summary(data)}')
    if len(data) > MAX_KB * 1024:
        raise SystemExit(f'#{num}: GIF is {len(data) // 1024} KB, over the {MAX_KB} KB budget. '
                         'Cut routine frames (merge QUICK steps) or use fewer steps.')
    if preview_dir:
        os.makedirs(preview_dir, exist_ok=True)
        with open(os.path.join(preview_dir, f'{num:04d}.gif'), 'wb') as f:
            f.write(data)
        scene.save_frames(preview_dir, preview)
    if embed:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(root, 'leetcode', f'{num:04d}.ipynb')
        nb = nbcells.load(path)
        nbcells.set_animation(nb, data, blurb)
        nbcells.save(nb, path)
    return data


def cli():
    """Standard flags for animation scripts: --no-embed, --preview DIR, --frames 3,10."""
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-embed', action='store_true', help='render only; leave the notebook alone')
    ap.add_argument('--preview', metavar='DIR', help='also write the GIF and chosen frames here')
    ap.add_argument('--frames', default='', help='comma-separated frame indices to dump as PNG')
    a = ap.parse_args()
    a.frames = [int(x) for x in a.frames.split(',') if x.strip()]
    return a
