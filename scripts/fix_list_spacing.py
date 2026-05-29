from __future__ import annotations

import argparse
import re
from pathlib import Path


def is_list_item(stripped_line: str) -> bool:
    if stripped_line.startswith("- ") or stripped_line.startswith("* ") or stripped_line.startswith("+ "):
        return True
    if re.match(r"^\d+\.\s", stripped_line):
        return True
    return False


def normalize_list_spacing(text: str) -> str:
    text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    new_lines: list[str] = []

    for line in lines:
        stripped = line.strip()

        if is_list_item(stripped):
            if new_lines and new_lines[-1].strip():
                last_non_empty = ""
                for prev in reversed(new_lines):
                    if prev.strip():
                        last_non_empty = prev.strip()
                        break
                if last_non_empty and not is_list_item(last_non_empty):
                    new_lines.append("")

        new_lines.append(line)

    return "\n".join(new_lines)


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            files.append(path)
            continue
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Insert a blank line before list items when they follow normal text."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("docs")],
        help="Markdown files or directories to process. Defaults to docs/.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes in place. Without this flag, only print changed files.",
    )
    args = parser.parse_args()

    changed_files = 0
    for file_path in iter_markdown_files(args.paths):
        original = file_path.read_text(encoding="utf-8")
        updated = normalize_list_spacing(original)
        if updated == original:
            continue

        changed_files += 1
        print(file_path)
        if args.write:
            file_path.write_text(updated, encoding="utf-8")

    print(f"Changed files: {changed_files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
