from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def is_list_item(stripped_line: str) -> bool:
    if stripped_line.startswith("- ") or stripped_line.startswith("* ") or stripped_line.startswith("+ "):
        return True
    if re.match(r"^\d+\.\s", stripped_line):
        return True
    return False


def normalize_list_spacing(text: str) -> tuple[str, int]:
    text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    new_lines: list[str] = []
    modifications = 0

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
                    modifications += 1

        new_lines.append(line)

    return "\n".join(new_lines), modifications


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            files.append(path)
            continue
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return files


def resolve_output_path(file_path: Path, inputs: list[Path], output: Path | None) -> Path:
    if output is None:
        return file_path

    if len(inputs) == 1 and inputs[0].is_file():
        if output.suffix.lower() == ".md":
            return output
        return output / file_path.name

    for root in inputs:
        if root.is_dir():
            try:
                relative = file_path.relative_to(root)
                return output / relative
            except ValueError:
                continue

    return output / file_path.name


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Insert a blank line before list items when they follow normal text."
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs="*",
        type=Path,
        default=None,
        help="Markdown files or directories to process. Defaults to docs/ when omitted or left empty.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Optional output file or directory. Defaults to overwriting the source when used with --write.",
    )
    parser.add_argument(
        "-w",
        "--write",
        action="store_true",
        help="Write changes to disk. Without this flag, only print the files that would change.",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        return 0

    args = parser.parse_args()
    inputs = args.input or [Path("docs")]

    changed_files = 0
    total_places = 0
    for file_path in iter_markdown_files(inputs):
        original = file_path.read_text(encoding="utf-8")
        updated, modifications = normalize_list_spacing(original)
        if updated == original:
            continue

        changed_files += 1
        total_places += modifications
        print(f"{file_path} ({modifications})")
        if args.write:
            output_path = resolve_output_path(file_path, inputs, args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(updated, encoding="utf-8")

    summary = "Changed" if args.write else "Will change"
    print(f"{summary} {changed_files} files, total {total_places} places")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
