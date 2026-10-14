# LeetCode Notebook Standards

## Notebook Structure

Each problem lives in `leetcode/NNNN.ipynb` (zero-padded to 4 digits), numbered to match the order in `markdown/All Problems List - Leetcode.md`.

Kernel: `.NET (C#)` — all notebooks use the .NET Interactive C# kernel.

### Cell Layout

| Cell | Type     | Content                            |
|------|----------|------------------------------------|
| 0    | markdown | Title, URL, complexity table, methodology |
| 1    | markdown | `## Solutions` header + `### C#`   |
| 2    | code     | C# solution                        |
| 3    | markdown | `### Python`                       |
| 4    | code     | Python solution                    |
| 5    | markdown | `### Go`                           |
| 6    | code     | Go solution                        |
| 7    | markdown | `### Rust`                         |
| 8    | code     | Rust solution                      |
| 9    | markdown | Example scenarios (5 examples)     |
| 10   | markdown | Infographic image attachment       |

---

## Cell 0 — Header

```
# LeetCode #N: <Title>

https://leetcode.com/problems/<slug>/

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Brute Force** | ... | ... |
| **<Other Optimal Name>** | ... | ... |
| **<Best Optimal Name>** | ... | ... |

---

## Understanding the Methods

### Brute Force
<1-3 sentences. Explain what it does and why it's slow.>

### <Other Optimal Name>
<1-3 sentences. Explain the approach and note its limitation vs the best.>

### Optimal: <Best Name> ★
<1-3 sentences. Explain the core idea.>

**Why this is better than <Other>:** <1-2 sentences comparing them directly.>

**Constraints:**
* <from the problem>
```

### Multiple Optimal Approaches

When a problem has more than one optimal-class solution (same or similar Big-O):

- **List all** of them in the complexity table, ordered worst → best (brute force first, best optimal last).
- **Describe each** under "Understanding the Methods" with 1-3 sentences.
- **Mark the best one** with a ★ after the heading (`### Optimal: <Name> ★`).
- **Explain why** the chosen one is better — even if the Big-O is identical, call out the practical difference (e.g., one-pass vs two-pass, stack overhead, short-circuit behavior).
- **Only code the best optimal** in all four languages. Other approaches are described in prose only.

If there is genuinely only one optimal approach, skip the comparison — just list brute force and the optimal.

Keep descriptions concise — an entry-level developer should understand them without extra context.

---

## Cells 1–8 — Solutions (C#, Python, Go, Rust)

- Only implement the **optimal** approach (brute force is explained in prose, not coded).
- All four languages use the **same comment structure** so the logic can be followed across languages.
- Comments explain the *why*, not the *what* — e.g., "Calculate the complement needed to hit the target" not "subtract nums[i] from target".
- Use each language's idiomatic naming conventions (PascalCase for C#, snake_case for Python/Rust, camelCase for Go).

---

## Cell 9 — Example Scenarios

Exactly **5 examples**, each with `**Input:**` and a short walkthrough:

1. **Common Case** — straightforward, happy-path input
2. **Slightly Complex** — needs a bit more thought (negatives, longer arrays, etc.)
3. **Edge Case: Time Factor** — worst case for time (e.g., match at the very end, forcing full scan)
4. **Edge Case: Space Factor** — worst case for space (e.g., no match found, dictionary fills completely)
5. **Almost-Impossible but Plausible** — extreme boundary values, overflow-adjacent, near-miss decoys

Each walkthrough should be 1-2 sentences. Use LaTeX for math notation (`$O(n)$`, `$\approx$`, `$\pm$`).

---

## Cell 10 — Infographic Image

An embedded PNG (`image.png` attachment) rendered from an HTML template via headless Chrome.

### Match the Visualization to the Data Structure ★

**The most important rule: draw the problem's actual data structure, not a flattened array.**
A 1D array of cells + a trace table is only right for genuinely 1D problems (two-pointer, sliding
window, prefix sums). For anything with spatial or relational structure, show that structure
directly — the way a good YouTube walkthrough sketches it on a whiteboard:

| Problem shape | Visualization |
| :--- | :--- |
| **Grid / matrix** (islands, flood fill, DP on grid) | A real 2D grid. Color each region/component distinctly, draw **connection bars** between adjacent cells that belong together, **cross out** inactive/water cells (diagonal slash), and show a **running counter** when something is being tallied. See the `#200` generator in `scripts/`. |
| **Tree** (BST, binary tree, traversal) | An SVG node-and-edge tree. Highlight the visited path / target nodes; number nodes in traversal order. |
| **Graph** (topological sort, union-find, shortest path) | An SVG node-edge diagram with colored traversal order or component grouping — not an adjacency array. |
| **Linked list** | A horizontal chain of node boxes with `→` pointer arrows; show before/after for pointer surgery. |
| **Intervals** | A horizontal timeline with overlapping bars. |
| **1D array / string** | Flat colored cells + trace table (the original default). |

Show **input → after** side by side where it clarifies the transformation (e.g. grid before vs.
after flood fill). Each example should make the *mechanism* visible at a glance, not just the answer.

A reusable grid generator lives at `scripts/gen_grid_infographic.py` — feed it a grid and an
island/region assignment and it auto-places cells, connection bars, crossouts, and the counter.
Prefer extending a generator like this over hand-writing hundreds of cell `<div>`s (hand-writing
large grids by hand tends to stall the agent).

### Image Generation Steps

1. **Create the HTML file** in the scratchpad directory with all 5 examples laid out as cards. Pick
   the visualization that matches the data structure (see the table above). Each card contains:
   - Example title and input line (monospace)
   - The structure visualization (2D grid / tree / graph / chain / timeline / array as appropriate)
   - A step indicator where it helps (trace table, running counter, or numbered traversal order)
   - Result box (green checkmark for success, red X / blue info for other outcomes)
   - Optional note for non-obvious behavior

2. **Preview in browser** to verify layout — use `preview_start` with a local HTTP server, check for overlaps, truncated text, or misaligned elements.

3. **Render to PNG** via headless Chrome:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless=new --disable-gpu --hide-scrollbars \
     --screenshot="NNNN_final.png" \
     --window-size=1024,<content_height> \
     --force-device-scale-factor=2 \
     "file:///path/to/NNNN_infographic.html"
   ```
   Measure `<content_height>` from the rendered page (`.card` bounding rect height + ~56px margin).

4. **Embed into notebook** by base64-encoding the PNG and writing it into the last cell's `attachments.image.png.image/png` field in the notebook JSON.

### Image Design Rules

- Card width: 968px inside a 1024px viewport
- Background: `#eef1f5`, card: `#ffffff` with `#1f2430` border, rounded corners
- Array / grid cells: 46×46px default, 42×42px for 6+ per row, 72×42px for wide values (e.g., `-1e9`)
- **Grid cells** sit in a `position:relative` wrapper with ~10px gaps; connection bars are absolutely
  positioned in those gaps (thickness ~16px) colored to match the region
- **Region palette**: cycle 10 distinct (fill, border, text) triples so adjacent components never
  share a color. Green `#d4f5d4`/`#2f9e58`, blue `#d4e8f5`/`#2f7e9e`, pink, gold, purple, teal, etc.
  (full list in `scripts/gen_grid_infographic.py`)
- **Water / inactive cells**: grey fill with a blue diagonal slash via `linear-gradient`
- Matched elements highlighted with green border/background (`#2f9e58` / `#e4f7ea`)
- Trace table uses monospace font, green for matches, grey for misses
- Result boxes: green for success (`#d4edda`/`#155724`), red for failure (`#f8d7da`/`#721c24`), blue info (`#d1ecf1`/`#0c5460`)
- Notes in italic, kept to 1-2 lines

---

## Editing Notebooks Programmatically

Notebooks are JSON files. Use Python with a **heredoc** (`<< 'PYEOF'`) to avoid backslash escaping issues — Python string literals will eat `\a`, `\t`, `\p` etc. which breaks LaTeX (`\approx`, `\times`, `\pm`).

```bash
python3 << 'PYEOF'
import json
with open('NNNN.ipynb') as f:
    nb = json.load(f)
# ... modify nb['cells'] ...
with open('NNNN.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
    f.write('\n')
PYEOF
```

Always verify LaTeX escapes survived by checking the written file for `\\approx`, `\\times`, `\\pm` etc.
