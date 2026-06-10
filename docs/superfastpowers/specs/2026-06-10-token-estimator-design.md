# Token Estimator Design

## Goal

Provide a local command-line script that estimates token counts for a folder by recursively scanning files and aggregating totals for each directory.

## Approach

Add a dependency-aware Python CLI at `scripts/estimate_tokens.py`. It will use `tiktoken` for model-compatible tokenization and default to the `cl100k_base` encoding unless the caller chooses another encoding.

## Behavior

- Accept a root folder argument.
- Recursively visit files below that folder.
- Skip common generated or irrelevant directories: `.git`, `.idea`, `node_modules`, `__pycache__`, `.venv`, `venv`, `.mypy_cache`, `.pytest_cache`, `dist`, and `build`.
- Read files as UTF-8 text.
- Skip unreadable, non-UTF-8, or binary-like files and include a skipped-file summary.
- Count tokens per file with `tiktoken`.
- Roll file token counts up into every ancestor directory from the scan root.
- Print a sorted directory table and a final total.

## CLI

```bash
python scripts/estimate_tokens.py <folder> --encoding cl100k_base
```

## Testing

Use stdlib `unittest` so the repo does not need a full Python package scaffold. Tests will cover recursive aggregation, skipped directory handling, encoding selection, and skipped non-text files.
