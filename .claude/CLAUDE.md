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

### Image Generation Steps

1. **Create the HTML file** in the scratchpad directory with all 5 examples laid out as cards. Each card contains:
   - Example title and input line (monospace)
   - Array visualization (colored cells with index labels beneath)
   - Step-by-step trace table (columns: iteration var, value, computed result, lookup outcome)
   - Final data structure state box (e.g., hash map contents)
   - Result box (green checkmark for match, red X for no match)
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
- Array cells: 46×46px default, 42×42px for arrays with 6+ elements, 72×42px for wide values (e.g., `-1e9`)
- Matched elements highlighted with green border/background (`#2f9e58` / `#e4f7ea`)
- Trace table uses monospace font, green for matches, grey for misses
- Result boxes: green for success, red for failure
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
