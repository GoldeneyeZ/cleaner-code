# Token Estimator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superfastpowers:subagent-driven-development (recommended), superfastpowers:goal-driven-development, or superfastpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python CLI that recursively estimates token counts for a folder with `tiktoken`.

**Architecture:** Keep the utility in one script because the repo has no Python package scaffold. Separate pure scanning/counting functions from CLI formatting so tests can exercise behavior without requiring a shell subprocess.
**Plan Acronym:** TE


**Tech Stack:** Python stdlib, `tiktoken`, `unittest`

---

### Task 1: Recursive Token Estimator CLI

<TASK-ID>TE-1</TASK-ID>

**Files:**
- Create: `scripts/estimate_tokens.py`
- Test: `tests/test_estimate_tokens.py`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_estimate_tokens.py` with tests that import `scripts/estimate_tokens.py`, build temporary folders, use a fake encoder, and assert recursive totals, skipped directories, and skipped binary files.

- [ ] **Step 2: Run tests to verify failure**

Run: `python -m unittest tests.test_estimate_tokens -v`

Expected: FAIL because `scripts/estimate_tokens.py` does not exist yet.

- [ ] **Step 3: Write minimal implementation**

Create `scripts/estimate_tokens.py` with:

- `DEFAULT_SKIP_DIRS`
- `ScanResult`
- `format_tokens`
- `is_binary_like`
- `read_text_file`
- `estimate_tokens`
- `print_report`
- `parse_args`
- `load_encoding`
- `main`

- [ ] **Step 4: Run tests to verify pass**

Run: `python -m unittest tests.test_estimate_tokens -v`

Expected: PASS.

- [ ] **Step 5: Verify CLI help and dependency behavior**

Run: `python scripts/estimate_tokens.py --help`

Expected: exits successfully and prints usage text.

- [ ] **Step 6: Commit**

```bash
git add docs/superfastpowers/plans/TE/2026-06-10-token-estimator.md scripts/estimate_tokens.py tests/test_estimate_tokens.py
git commit -m "feat: add token estimator script"
```
