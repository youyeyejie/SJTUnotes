from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


INLINE_BLOCK_MATH = re.compile(r"\$\$\s*(?P<formula>.+?)\s*\$\$")
LIST_MARKER = re.compile(r"^(?P<base>[ \t]*)(?P<marker>(?:[-+*]|\d+\.)[ \t]+)")
LIST_MARKER_ONLY = re.compile(r"^[ \t]*(?:[-+*]|\d+\.)$")
BLOCK_START_LINE = re.compile(r"^[ \t]*\$\$[ \t]*$")
LIST_BLOCK_START_LINE = re.compile(r"^[ \t]*(?:[-+*]|\d+\.)[ \t]+\$\$[ \t]*$")
BLOCK_INLINE_START_LINE = re.compile(r"^(?P<indent>[ \t]*)\$\$(?P<formula>.*\S.*)$")


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


def ensure_single_blank_line(out: list[str]) -> int:
    modifications = 0
    while len(out) >= 2 and out[-1] == "" and out[-2] == "":
        out.pop()
        modifications += 1
    if out and out[-1].strip():
        out.append("")
        modifications += 1
    return modifications


def append_block(
    out: list[str],
    indent: str,
    formula: str,
    leading_blank: bool = True,
    opener: str | None = None,
) -> None:
    if leading_blank:
        ensure_single_blank_line(out)

    out.extend(
        [
            opener if opener is not None else f"{indent}$$",
            f"{indent}{formula.strip()}",
            f"{indent}$$",
        ]
    )
    append_blank_line(out)


def append_inline_block_sequence(out: list[str], line: str) -> int:
    matches = list(INLINE_BLOCK_MATH.finditer(line))
    if not matches:
        out.append(line)
        return 0

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

    return len(matches)


def normalize_block_math(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out: list[str] = []
    modifications = 0
    in_block_math = False

    for line in lines:
        if not line.strip():
            append_blank_line(out)
            continue

        inline_start_match = BLOCK_INLINE_START_LINE.match(line)
        if inline_start_match and not line.strip().endswith("$$"):
            modifications += ensure_single_blank_line(out)
            out.append(f"{inline_start_match.group('indent')}$$")
            out.append(f"{inline_start_match.group('indent')}{inline_start_match.group('formula').strip()}")
            in_block_math = True
            modifications += 1
            continue

        if LIST_BLOCK_START_LINE.match(line):
            in_block_math = True
            out.append(line)
            continue

        if BLOCK_START_LINE.match(line):
            if not in_block_math:
                modifications += ensure_single_blank_line(out)
                in_block_math = True
                out.append(line)
            else:
                in_block_math = False
                out.append(line)
                append_blank_line(out)
            continue

        if INLINE_BLOCK_MATH.search(line):
            modifications += append_inline_block_sequence(out, line)
            continue

        out.append(line)

    normalized = "\n".join(out)
    if text.endswith("\n"):
        normalized += "\n"
    return normalized, modifications


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
        description="Rewrite single-line $$ block formulas to multiline blocks."
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
        updated, modifications = normalize_block_math(original)
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
