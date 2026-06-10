#!/usr/bin/env python3
"""Estimate token counts for a folder recursively."""

from __future__ import annotations

import argparse
import os
import sys
from collections import defaultdict
from pathlib import Path


DEFAULT_SKIP_DIRS = frozenset(
    {
        ".git",
        ".idea",
        ".mypy_cache",
        ".pytest_cache",
        ".venv",
        "__pycache__",
        "build",
        "dist",
        "node_modules",
        "venv",
    }
)


class ScanResult:
    def __init__(self, directory_totals, total_tokens, file_count, skipped_files, skipped_directories):
        self.directory_totals = directory_totals
        self.total_tokens = total_tokens
        self.file_count = file_count
        self.skipped_files = skipped_files
        self.skipped_directories = skipped_directories


def format_tokens(count):
    return f"{count:,}"


def is_binary_like(data):
    return b"\x00" in data


def read_text_file(path):
    try:
        data = path.read_bytes()
    except OSError:
        return None, "unreadable"

    if is_binary_like(data):
        return None, "binary"
    try:
        return data.decode("utf-8"), None
    except UnicodeDecodeError:
        return None, "non-utf-8"


def directory_chain(relative_parent):
    directories = [Path(".")]
    if str(relative_parent) == ".":
        return directories

    current = Path()
    for part in relative_parent.parts:
        current = current / part
        directories.append(current)
    return directories


def estimate_tokens(root, encoding, skip_dirs=DEFAULT_SKIP_DIRS):
    root = Path(root)
    if not root.exists():
        raise FileNotFoundError(root)
    if not root.is_dir():
        raise NotADirectoryError(root)

    directory_totals = defaultdict(int)
    skipped_files = []
    skipped_directories = []
    total_tokens = 0
    file_count = 0

    for current_root, dirnames, filenames in os.walk(root):
        current_root = Path(current_root)
        dirnames.sort()
        filenames.sort()

        kept_dirs = []
        for dirname in dirnames:
            relative_dir = (current_root / dirname).relative_to(root)
            if dirname in skip_dirs:
                skipped_directories.append(relative_dir)
            else:
                kept_dirs.append(dirname)
        dirnames[:] = kept_dirs

        for filename in filenames:
            path = current_root / filename
            relative_path = path.relative_to(root)
            text, skip_reason = read_text_file(path)
            if skip_reason:
                skipped_files.append((relative_path, skip_reason))
                continue

            token_count = len(encoding.encode(text))
            total_tokens += token_count
            file_count += 1

            relative_parent = relative_path.parent
            for directory in directory_chain(relative_parent):
                directory_totals[directory] += token_count

    return ScanResult(
        dict(directory_totals),
        total_tokens,
        file_count,
        skipped_files,
        skipped_directories,
    )


def print_report(result, output=sys.stdout):
    print("Directory token totals", file=output)
    print("----------------------", file=output)
    print(f"{'Tokens':>12}  Directory", file=output)

    for directory, token_count in sorted(result.directory_totals.items(), key=lambda item: str(item[0])):
        print(f"{format_tokens(token_count):>12}  {directory}", file=output)

    print(file=output)
    print(f"Total tokens: {format_tokens(result.total_tokens)}", file=output)
    print(f"Files counted: {format_tokens(result.file_count)}", file=output)

    if result.skipped_directories:
        print(f"Skipped directories: {format_tokens(len(result.skipped_directories))}", file=output)
        for directory in result.skipped_directories:
            print(f"  {directory}", file=output)

    if result.skipped_files:
        print(f"Skipped files: {format_tokens(len(result.skipped_files))}", file=output)
        for path, reason in result.skipped_files:
            print(f"  {path} ({reason})", file=output)


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Estimate tiktoken token counts for a folder.")
    parser.add_argument("folder", type=Path, help="Folder to scan recursively.")
    parser.add_argument(
        "--encoding",
        default="cl100k_base",
        help="tiktoken encoding name to use. Default: cl100k_base.",
    )
    return parser.parse_args(argv)


def load_encoding(name):
    try:
        import tiktoken
    except ModuleNotFoundError as exc:
        raise RuntimeError("Missing dependency: install tiktoken with `python -m pip install tiktoken`.") from exc

    return tiktoken.get_encoding(name)


def main(argv=None):
    args = parse_args(argv)
    try:
        encoding = load_encoding(args.encoding)
        result = estimate_tokens(args.folder, encoding)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print_report(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
