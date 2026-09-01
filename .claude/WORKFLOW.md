# Notebook Batch Workflow

Step-by-step process for adding a batch of 15 LeetCode notebooks and merging them to main.

---

## 1. Identify the next 15 problems

```bash
grep -n "^| [0-9]" leetcode/README.md | grep -v "📓" | head -20
```

Take the next 15 unsolved problems in README order. Skip SQL-only problems (no algorithmic C# solution — typically database problems on LeetCode).

---

## 2. Create a feature branch

```bash
git checkout main && git pull origin main
git checkout -b feature/<category>_$(date +%H%M)
```

Branch naming: `feature/description_HHMM` using the current time.

---

## 3. Spawn the background agent

Use the Agent tool with `run_in_background: true`. The prompt must include:
- The 15 problem numbers and titles
- The CLAUDE.md notebook structure (11 cells, C#/Python/Go/Rust, 5 examples, infographic)
- Commit instructions with the correct git identity (see §6)
- List-file update instructions (all 6 files, with `📓` links and `<span title="...">` hover tooltips)
- PR creation at the end

---

## 4. Wait for agent completion

Do not do anything with the same files while the agent runs. When the task-notification arrives, the PR URL is in the agent output.

---

## 5. Merge the PR

```bash
gh pr merge <N> --squash --admin
git checkout main && git pull origin main
```

`--admin` bypasses branch protection. Always squash-merge to keep main history clean.

---

## 6. Git identity (CRITICAL)

Every commit must use the noreply email or GitHub will reject the push (GH007):

```bash
GIT_COMMITTER_EMAIL="12857923+sanjay-bhat@users.noreply.github.com" \
git commit --author="Sanjay Bhat <12857923+sanjay-bhat@users.noreply.github.com>" \
  -m "Add #NNNN: <Title> (#PR)"
```

**Never use** `sanjaybhat18492@gmail.com` for commits that will be pushed.

---

## 7. Hover tooltips

The Data Structure column in all 6 list files uses `<span title="...">` for native GitHub hover tooltips. These are applied by:

```bash
python3 /private/tmp/claude-501/-Users-sanjaybhat-Desktop-Leetcode/43a65a4d-9706-4ca9-9548-6d2fe81c27c5/scratchpad/add_hover_titles.py
```

The script is already populated with 60+ approach descriptions. If a new approach name is unmapped, add it to the `DESCRIPTIONS` dict and re-run. The agent adds `<span>` wrapping as part of each notebook batch, so a separate tooltip-only PR is only needed for bulk retroactive updates.

---

## 8. Infographic pipeline

For each notebook's cell 10:

1. Write `NNNN_infographic.html` to the scratchpad directory
2. Render with headless Chrome (`--force-device-scale-factor=2`, `--window-size=1024,<height>`)
3. Auto-crop with Pillow (`getbbox` + 112 px margin)
4. Base64-encode and embed in `cell[10].attachments.image.png.image/png`

---

## 9. List files to update per notebook

| File | Link format |
|------|-------------|
| `README.md` (root) | `[📓 Title](leetcode/NNNN.ipynb)` |
| `leetcode/README.md` | `[📓 Title](NNNN.ipynb)` |
| `lists/README.md` | `[📓 Title](../leetcode/NNNN.ipynb)` |
| `lists/all-problems.md` | `[📓 Title](../leetcode/NNNN.ipynb)` |
| `lists/by-difficulty.md` | `[📓 Title](../leetcode/NNNN.ipynb)` |
| `lists/by-complexity.md` | `[📓 Title](../leetcode/NNNN.ipynb)` |

---

## 10. Conflict resolution (rebase)

If a PR has merge conflicts (usually in list files):

```bash
git fetch origin
git rebase origin/main
# resolve conflicts: keep HEAD's 📓 rows, take new problem row from feature branch
git rebase --continue
git push --force-with-lease origin <branch>
```

Force-push requires explicit user confirmation before running.
