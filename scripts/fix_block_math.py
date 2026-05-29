from __future__ import annotations

import argparse
import re
from pathlib import Path


INLINE_BLOCK_MATH = re.compile(r"\$\$\s*(?P<formula>.+?)\s*\$\$")
LIST_MARKER = re.compile(r"^(?P<base>[ \t]*)(?P<marker>(?:[-+*]|\d+\.)[ \t]+)")
LIST_MARKER_ONLY = re.compile(r"^[ \t]*(?:[-+*]|\d+\.)$")


def block_indent_for_line(line: str) -> str:
    list_match = LIST_MARKER.match(line)
    if list_match:
        return list_match.group("base") + " " * 4

    return re.match(r"^[ \t]*", line).group(0)


def append_with_spacing(out: list[str], line: str) -> None:
    if line.strip() or not out or out[-1].strip():
        out.append(line)


def append_blank_line(out: list[str]) -> None:
    if out and out[-1] != "":
        out.append("")


def append_block(
    out: list[str],
    indent: str,
    formula: str,
    leading_blank: bool = True,
    opener: str | None = None,
) -> None:
    if leading_blank and out and out[-1].strip():
        out.append("")

    out.extend(
        [
            opener if opener is not None else f"{indent}$$",
            f"{indent}{formula.strip()}",
            f"{indent}$$",
        ]
    )
    append_blank_line(out)


def append_inline_block_sequence(out: list[str], line: str) -> None:
    matches = list(INLINE_BLOCK_MATH.finditer(line))
    if not matches:
        out.append(line)
        return

    indent = block_indent_for_line(line)
    leading = line[: matches[0].start()].rstrip()
    if leading:
        if not LIST_MARKER_ONLY.fullmatch(leading):
            out.append(leading)

    for index, match in enumerate(matches):
        marker_only_leading = bool(leading) and index == 0 and LIST_MARKER_ONLY.fullmatch(leading)
        append_block(
            out,
            indent,
            match.group("formula"),
            leading_blank=not marker_only_leading,
            opener=f"{leading} $$" if marker_only_leading else None,
        )

        next_start = matches[index + 1].start() if index + 1 < len(matches) else len(line)
        between = line[match.end() : next_start].strip()
        if between:
            out.append(f"{indent}{between}")


def normalize_block_math(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []

    for line in lines:
        if not line.strip():
            append_blank_line(out)
            continue

        if INLINE_BLOCK_MATH.search(line):
            append_inline_block_sequence(out, line)
            continue

        out.append(line)

    normalized = "\n".join(out)
    if text.endswith("\n"):
        normalized += "\n"
    return normalized


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
        description="Rewrite single-line $$ block formulas to multiline blocks."
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
        updated = normalize_block_math(original)
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
