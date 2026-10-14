#!/usr/bin/env python3
"""Shared infographic building blocks for LeetCode notebook visualizations.

Each generator returns an HTML snippet (a <div class="card">...</div>) given
structured data, so per-problem scripts supply data instead of hand-writing
large HTML/SVG (which tends to stall agents). Compose cards with page_shell().

Visualization families:
  - card()          : wrapper for one example (title, subtitle, input, body, result)
  - array_row()     : 1D array of colored cells with optional pointer labels
  - trace_table()   : step-by-step table
  - linked_list()   : horizontal node chain with -> pointer arrows
  - binary_tree()   : SVG binary tree from a level-order list
  - decision_tree() : SVG backtracking/decision tree from nested nodes
  - stack_view()    : vertical stack with push/pop annotations
  - dp_table()      : 2D DP grid with row/col headers and highlighted cells
  - bar_chart()     : vertical bars (heights), e.g. container-with-most-water
  - grid()          : 2D grid with region colors + connection bars + crossouts
"""

# ---- shared palette (fill, border, text) ----
PALETTE = [
    ("#d4f5d4", "#2f9e58", "#1a6b35"),  # green
    ("#d4e8f5", "#2f7e9e", "#1a4f6b"),  # blue
    ("#f5d4e8", "#9e2f7e", "#6b1a4f"),  # pink
    ("#f5eed4", "#9e8e2f", "#6b5f1a"),  # gold
    ("#e8d4f5", "#7e2f9e", "#4f1a6b"),  # purple
    ("#d4f5ef", "#2f9e8e", "#1a6b5f"),  # teal
    ("#f5ddd4", "#9e5a2f", "#6b3a1a"),  # orange
    ("#ddf5d4", "#5a9e2f", "#3a6b1a"),  # lime
    ("#f5d4d4", "#9e2f2f", "#6b1a1a"),  # red
    ("#d4ddf5", "#2f5a9e", "#1a3a6b"),  # indigo
]
GREEN = PALETTE[0]
BLUE = PALETTE[1]


def color(i):
    return PALETTE[i % len(PALETTE)]


# ---------------------------------------------------------------- page shell
def page_shell(title, cards, legend=None):
    legend_html = f'<div class="legend-top">{legend}</div>' if legend else ''
    return f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#eef1f5; font-family:'Segoe UI',system-ui,-apple-system,sans-serif; padding:28px; }}
h1 {{ text-align:center; font-size:26px; color:#1f2430; margin-bottom:8px; font-weight:700; }}
.legend-top {{ text-align:center; font-size:13px; color:#666; margin-bottom:22px; }}
.card {{ background:#fff; border:2px solid #1f2430; border-radius:12px; padding:24px 28px; margin:0 auto 20px; width:968px; }}
.card-title {{ font-size:18px; font-weight:700; color:#1f2430; margin-bottom:6px; }}
.card-subtitle {{ font-size:13px; color:#666; margin-bottom:16px; font-style:italic; }}
.input-line {{ font-family:'Courier New',monospace; font-size:13px; background:#f4f5f7; padding:8px 12px; border-radius:6px; margin-bottom:20px; color:#333; }}
.body-center {{ display:flex; justify-content:center; margin-bottom:18px; flex-wrap:wrap; gap:24px; }}
.note {{ font-size:13px; color:#666; font-style:italic; margin-bottom:12px; text-align:center; max-width:820px; margin:0 auto 12px; }}
.result-box {{ display:block; width:fit-content; margin:0 auto; padding:8px 20px; border-radius:8px; font-weight:700; font-size:15px; }}
.result-success {{ background:#d4edda; color:#155724; border:1px solid #c3e6cb; }}
.result-fail {{ background:#f8d7da; color:#721c24; border:1px solid #f5c6cb; }}
.result-info {{ background:#d1ecf1; color:#0c5460; border:1px solid #bee5eb; }}
/* array */
.arr {{ display:inline-grid; gap:4px; }}
.acell {{ width:46px; height:46px; display:flex; align-items:center; justify-content:center; font-family:'Courier New',monospace; font-size:15px; font-weight:700; border-radius:8px; border:2px solid #b0b8c8; background:#e8edf3; color:#1f2430; position:relative; }}
.aidx {{ position:absolute; bottom:-16px; left:50%; transform:translateX(-50%); font-size:9px; color:#999; }}
.aptr {{ position:absolute; top:-18px; left:50%; transform:translateX(-50%); font-size:11px; font-weight:700; }}
/* trace table */
table.trace {{ border-collapse:collapse; font-size:13px; margin:0 auto; }}
table.trace th {{ background:#1f2430; color:#fff; padding:7px 14px; text-align:left; font-weight:600; }}
table.trace td {{ padding:6px 14px; border-bottom:1px solid #eee; font-family:'Courier New',monospace; }}
table.trace tr:nth-child(even) td {{ background:#fafbfc; }}
.hit {{ color:#2f9e58; font-weight:700; }}
.miss {{ color:#999; }}
/* linked list */
.ll {{ display:flex; align-items:center; gap:0; flex-wrap:wrap; justify-content:center; }}
.llnode {{ display:flex; align-items:center; }}
.llbox {{ min-width:46px; height:46px; padding:0 12px; display:flex; align-items:center; justify-content:center; font-family:'Courier New',monospace; font-size:16px; font-weight:700; border-radius:8px; border:2px solid #2f7e9e; background:#d4e8f5; color:#1a4f6b; }}
.llarrow {{ color:#1f2430; font-size:22px; margin:0 8px; }}
.llnull {{ color:#999; font-family:'Courier New',monospace; font-size:14px; margin-left:8px; }}
/* stack */
.stack {{ display:inline-flex; flex-direction:column-reverse; border:2px solid #1f2430; border-top:none; border-radius:0 0 8px 8px; min-width:80px; }}
.stackcell {{ height:40px; display:flex; align-items:center; justify-content:center; font-family:'Courier New',monospace; font-weight:700; border-top:1px solid #ccc; background:#d4e8f5; color:#1a4f6b; }}
.stacklabel {{ text-align:center; font-size:12px; color:#666; margin-top:6px; }}
/* bars */
.bars {{ display:flex; align-items:flex-end; gap:6px; height:200px; }}
.bar {{ width:36px; background:#d4e8f5; border:2px solid #2f7e9e; border-radius:4px 4px 0 0; display:flex; align-items:flex-start; justify-content:center; font-family:'Courier New',monospace; font-size:12px; font-weight:700; color:#1a4f6b; padding-top:4px; position:relative; }}
.bar.active {{ background:#d4f5d4; border-color:#2f9e58; color:#1a6b35; }}
.bar .bidx {{ position:absolute; bottom:-18px; left:50%; transform:translateX(-50%); font-size:10px; color:#999; }}
/* dp table */
table.dp {{ border-collapse:collapse; margin:0 auto; font-family:'Courier New',monospace; font-size:14px; }}
table.dp th {{ background:#1f2430; color:#fff; padding:6px 10px; font-weight:600; }}
table.dp td {{ width:40px; height:40px; text-align:center; border:1px solid #ccc; background:#fff; }}
table.dp td.fill {{ background:#d4f5d4; color:#1a6b35; font-weight:700; }}
table.dp td.base {{ background:#f5eed4; color:#6b5f1a; }}
/* counter */
.counter {{ text-align:center; font-size:15px; color:#1f2430; font-weight:600; margin-bottom:12px; }}
.count-step {{ display:inline-block; min-width:26px; padding:2px 8px; border-radius:6px; background:#eef1f5; color:#888; font-family:'Courier New',monospace; }}
.count-final {{ display:inline-block; min-width:26px; padding:2px 10px; border-radius:6px; background:#2f9e58; color:#fff; font-family:'Courier New',monospace; font-weight:700; }}
.count-arrow {{ color:#aaa; }}
/* matrix */
table.mtx {{ border-collapse:collapse; margin:0 auto; font-family:'Courier New',monospace; }}
table.mtx td {{ width:40px; height:40px; text-align:center; border:1px solid #c7ccd6; font-size:15px; font-weight:700; color:#1f2430; background:#fff; }}
table.mtx td.hl {{ outline:3px solid #2f9e58; outline-offset:-3px; }}
table.mtx td.bt {{ border-top:3px solid #1f2430; }}
table.mtx td.bl {{ border-left:3px solid #1f2430; }}
table.mtx td.br {{ border-right:3px solid #1f2430; }}
table.mtx td.bb {{ border-bottom:3px solid #1f2430; }}
/* timeline / intervals */
.tl {{ position:relative; width:860px; margin:0 auto; }}
.tlrow {{ position:relative; height:34px; margin-bottom:6px; }}
.tlbar {{ position:absolute; height:28px; border-radius:6px; display:flex; align-items:center; justify-content:center; font-family:'Courier New',monospace; font-size:12px; font-weight:700; border:2px solid; }}
.tlaxis {{ position:relative; height:22px; border-top:2px solid #b0b8c8; margin-top:4px; }}
.tltick {{ position:absolute; font-size:10px; color:#999; transform:translateX(-50%); top:4px; }}
/* grid */
.grid-wrap {{ position:relative; }}
.gcell {{ position:absolute; width:46px; height:46px; display:flex; align-items:center; justify-content:center; font-family:'Courier New',monospace; font-size:17px; font-weight:700; border-radius:8px; border:2px solid transparent; z-index:2; }}
.gcell.water {{ background:#f3f4f6; color:#c2c7d0; border-color:#e2e5ea; background-image:linear-gradient(to top right, transparent 44%, #6ea8d8 44%, #6ea8d8 56%, transparent 56%); }}
.bridge {{ position:absolute; border-radius:3px; z-index:1; }}
</style></head><body>
<h1>{title}</h1>
{legend_html}
{''.join(cards)}
</body></html>'''


def card(title, subtitle, input_line, body, result=None, note=None):
    rtype, rtext = result if result else ("info", "")
    note_html = f'<div class="note">{note}</div>' if note else ''
    res_html = f'<div class="result-box result-{rtype}">&#10004; {rtext}</div>' if result else ''
    return f'''<div class="card">
<div class="card-title">{title}</div>
<div class="card-subtitle">{subtitle}</div>
<div class="input-line">{input_line}</div>
<div class="body-center">{body}</div>
{note_html}{res_html}
</div>'''


# ---------------------------------------------------------------- array
def array_row(values, colors=None, pointers=None, show_index=True):
    """values: list. colors: optional list of PALETTE indices or None per cell.
    pointers: optional dict {index: 'label'} drawn above a cell."""
    cells = []
    for i, v in enumerate(values):
        style = ''
        if colors and colors[i] is not None:
            f, b, t = color(colors[i])
            style = f'background:{f};border-color:{b};color:{t};'
        ptr = ''
        if pointers and i in pointers:
            f, b, t = GREEN
            ptr = f'<span class="aptr" style="color:{b};">{pointers[i]}</span>'
        idx = f'<span class="aidx">{i}</span>' if show_index else ''
        cells.append(f'<div class="acell" style="{style}">{ptr}{v}{idx}</div>')
    cols = len(values)
    return f'<div class="arr" style="grid-template-columns:repeat({cols},46px);">{"".join(cells)}</div>'


def trace_table(headers, rows):
    """headers: list of column names. rows: list of lists (cells may contain HTML)."""
    head = ''.join(f'<th>{h}</th>' for h in headers)
    body = ''
    for r in rows:
        body += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return f'<table class="trace"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


# ---------------------------------------------------------------- linked list
def linked_list(values, color_idx=1, highlight=None):
    """values: list of node values. highlight: set of indices to color green."""
    highlight = highlight or set()
    parts = ['<div class="ll">']
    for i, v in enumerate(values):
        f, b, t = GREEN if i in highlight else color(color_idx)
        parts.append(f'<div class="llnode"><div class="llbox" style="background:{f};border-color:{b};color:{t};">{v}</div>')
        if i < len(values) - 1:
            parts.append('<span class="llarrow">&rarr;</span>')
        parts.append('</div>')
    parts.append('<span class="llnull">&rarr; null</span>')
    parts.append('</div>')
    return ''.join(parts)


# ---------------------------------------------------------------- stack
def stack_view(items, label='stack'):
    """items: bottom-to-top list of values currently on the stack."""
    cells = ''.join(f'<div class="stackcell">{v}</div>' for v in items)
    if not items:
        cells = '<div class="stackcell" style="color:#bbb;background:#f8f9fa;">(empty)</div>'
    return f'<div><div class="stack">{cells}</div><div class="stacklabel">{label}</div></div>'


# ---------------------------------------------------------------- bars
def bar_chart(heights, active=None, scale=None):
    """heights: list of ints. active: set of indices to color green."""
    active = active or set()
    mx = scale or max(heights) or 1
    bars = []
    for i, h in enumerate(heights):
        px = int(h / mx * 180) + 20
        cls = 'bar active' if i in active else 'bar'
        bars.append(f'<div class="{cls}" style="height:{px}px;">{h}<span class="bidx">{i}</span></div>')
    return f'<div class="bars">{"".join(bars)}</div>'


# ---------------------------------------------------------------- dp table
def dp_table(matrix, col_headers=None, row_headers=None, fills=None, bases=None):
    """matrix: 2D list. fills/bases: sets of (r,c) to style."""
    fills = fills or set()
    bases = bases or set()
    html = '<table class="dp">'
    if col_headers is not None:
        html += '<tr><th></th>' + ''.join(f'<th>{h}</th>' for h in col_headers) + '</tr>'
    for r, row in enumerate(matrix):
        html += '<tr>'
        if row_headers is not None:
            html += f'<th>{row_headers[r]}</th>'
        for c, v in enumerate(row):
            cls = 'fill' if (r, c) in fills else ('base' if (r, c) in bases else '')
            html += f'<td class="{cls}">{v}</td>'
        html += '</tr>'
    html += '</table>'
    return html


# ---------------------------------------------------------------- counter
def counter(n, label='Count'):
    if n <= 1:
        seq = f'<span class="count-final">{n}</span>'
    else:
        seq = ' <span class="count-arrow">&rarr;</span> '.join(
            [f'<span class="count-step">{i}</span>' for i in range(1, n)]
            + [f'<span class="count-final">{n}</span>'])
    return f'<div class="counter">{label}: {seq}</div>'


# ---------------------------------------------------------------- trees (SVG)
def _tree_layout(node, depth, xcounter, positions, edges, parent=None):
    """Assign x by in-order leaf position, y by depth. node is a dict:
    {'label': str, 'children': [...], 'leaf': bool(optional), 'ok': bool(optional)}."""
    children = node.get('children', [])
    nid = id(node)
    if parent is not None:
        edges.append((parent, nid))
    if not children:
        x = xcounter[0]
        xcounter[0] += 1
    else:
        child_xs = []
        for ch in children:
            _tree_layout(ch, depth + 1, xcounter, positions, edges, nid)
            child_xs.append(positions[id(ch)][0])
        x = sum(child_xs) / len(child_xs)
    positions[nid] = (x, depth, node)
    return nid


def tree_svg(root, node_w=58, node_h=34, x_gap=70, y_gap=78, pad=28):
    """Render a decision/backtracking/binary tree from a nested dict.
    Node dict keys: label (str), children (list), leaf (bool -> rounded pill),
    ok (True=green success leaf, False=pruned/red), accent (palette idx).
    NOTE: escape < > & in labels before passing them in."""
    positions, edges = {}, []
    _tree_layout(root, 0, [0], positions, edges)
    max_x = max(p[0] for p in positions.values())
    max_d = max(p[1] for p in positions.values())
    W = int(max_x * x_gap + node_w + 2 * pad)
    H = int(max_d * y_gap + node_h + 2 * pad)

    def cx(x):
        return int(pad + x * x_gap + node_w / 2)

    def cy(d):
        return int(pad + d * y_gap + node_h / 2)

    svg = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Courier New, monospace">']
    for a, b in edges:
        xa, da, _ = positions[a]
        xb, db, _ = positions[b]
        svg.append(f'<line x1="{cx(xa)}" y1="{cy(da)+node_h//2}" x2="{cx(xb)}" y2="{cy(db)-node_h//2}" stroke="#b0b8c8" stroke-width="2"/>')
    for nid, (x, d, node) in positions.items():
        label = node.get('label', '')
        ok = node.get('ok', None)
        leaf = node.get('leaf', False) or not node.get('children')
        if ok is True:
            fill, border, text = '#d4edda', '#2f9e58', '#155724'
        elif ok is False:
            fill, border, text = '#f8d7da', '#c0392b', '#721c24'
        elif 'accent' in node:
            fill, border, text = color(node['accent'])
        else:
            fill, border, text = '#e8edf3', '#8792a6', '#1f2430'
        rx = node_h // 2 if leaf else 7
        X = cx(x) - node_w // 2
        Y = cy(d) - node_h // 2
        svg.append(f'<rect x="{X}" y="{Y}" width="{node_w}" height="{node_h}" rx="{rx}" '
                   f'fill="{fill}" stroke="{border}" stroke-width="2"/>')
        svg.append(f'<text x="{cx(x)}" y="{cy(d)+5}" text-anchor="middle" font-size="14" '
                   f'font-weight="700" fill="{text}">{label}</text>')
    svg.append('</svg>')
    return ''.join(svg)


# ---------------------------------------------------------------- matrix (general 2D grid)
def matrix(grid, cell_colors=None, highlights=None, boxes=None, cell=40):
    """General 2D matrix of values (sudoku, chessboard, rotate, spiral).
    grid: 2D list of display values (str/int; '' for blank).
    cell_colors: optional 2D list of (fill,border,text) triples or palette idx or None.
    highlights: set of (r,c) to outline green.
    boxes: int box size for thick separators (e.g. 3 for sudoku 9x9); or None.
    NOTE: escape < > & in values."""
    highlights = highlights or set()
    rows, cols = len(grid), len(grid[0])
    html = ['<table class="mtx">']
    for r in range(rows):
        html.append('<tr>')
        for c in range(cols):
            v = grid[r][c]
            style = ''
            if cell_colors and cell_colors[r][c] is not None:
                cc = cell_colors[r][c]
                f, b, t = color(cc) if isinstance(cc, int) else cc
                style = f'background:{f};color:{t};'
            cls = []
            if (r, c) in highlights:
                cls.append('hl')
            if boxes:
                if r % boxes == 0:
                    cls.append('bt')
                if c % boxes == 0:
                    cls.append('bl')
                if r == rows - 1:
                    cls.append('bb')
                if c == cols - 1:
                    cls.append('br')
            clsattr = f' class="{" ".join(cls)}"' if cls else ''
            html.append(f'<td{clsattr} style="{style}">{v}</td>')
        html.append('</tr>')
    html.append('</table>')
    return ''.join(html)


# ---------------------------------------------------------------- intervals / timeline
def intervals(items, lo=None, hi=None, width=860, ticks=None):
    """Horizontal timeline of intervals.
    items: list of (start, end, label, palette_idx) — one bar each, stacked in rows.
    lo/hi: axis bounds (auto from items if None). ticks: list of tick values.
    NOTE: escape < > & in labels."""
    starts = [s for s, *_ in items]
    ends = [e for _, e, *_ in items]
    lo = lo if lo is not None else min(starts)
    hi = hi if hi is not None else max(ends)
    span = (hi - lo) or 1

    def px(v):
        return int((v - lo) / span * (width - 20)) + 10

    rows_html = []
    for (s, e, label, ci) in items:
        f, b, t = color(ci)
        left = px(s)
        w = max(px(e) - px(s), 24)
        rows_html.append(
            f'<div class="tlrow"><div class="tlbar" style="left:{left}px;width:{w}px;'
            f'background:{f};border-color:{b};color:{t};">{label}</div></div>')

    if ticks is None:
        ticks = list(range(lo, hi + 1, max(1, span // 10)))
    tick_html = ''.join(
        f'<span class="tltick" style="left:{px(tv)}px;">{tv}</span>' for tv in ticks)

    return (f'<div class="tl">{"".join(rows_html)}'
            f'<div class="tlaxis">{tick_html}</div></div>')
