from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CODE_FENCE_START_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})")
INLINE_MATH_RE = re.compile(r"(?<!\\)(?<!\$)\$(?!\$).*?(?<!\\)\$(?!\$)|\\\(.*?\\\)")
BLOCK_MATH_LINE_RE = re.compile(r"^[ \t]*(\$\$|\\\[|\\\])")
SINGLE_LINE_BLOCK_MATH_RE = re.compile(r"^[ \t]*\$\$.*\$\$[ \t]*$")
ZH_CHAR = r"\u4e00-\u9fff"
LATIN_NUM = r"A-Za-z0-9"
TEXT_CHAR_RE = re.compile(rf"[{ZH_CHAR}{LATIN_NUM}]")


def split_by_code_fences(text: str) -> list[tuple[bool, str]]:
    lines = text.splitlines(keepends=True)
    segments: list[tuple[bool, str]] = []
    current: list[str] = []
    in_code_fence = False
    active_fence = ""

    for line in lines:
        fence_match = CODE_FENCE_START_RE.match(line)
        if fence_match:
            fence = fence_match.group("fence")
            if not in_code_fence:
                if current:
                    segments.append((False, "".join(current)))
                    current = []
                in_code_fence = True
                active_fence = fence[0]
                current.append(line)
                continue

            if fence[0] == active_fence:
                current.append(line)
                segments.append((True, "".join(current)))
                current = []
                in_code_fence = False
                active_fence = ""
                continue

        current.append(line)

    if current:
        segments.append((in_code_fence, "".join(current)))

    return segments


def normalize_inline_math_spacing(line: str) -> tuple[str, int]:
    parts: list[str] = []
    cursor = 0
    modifications = 0

    for match in INLINE_MATH_RE.finditer(line):
        start, end = match.span()
        prefix = line[cursor:start]
        if start > 0 and TEXT_CHAR_RE.fullmatch(line[start - 1]):
            if prefix and not prefix.endswith(" "):
                prefix = prefix + " "
                modifications += 1
        parts.append(prefix)

        parts.append(match.group(0))
        cursor = end

        if end < len(line) and TEXT_CHAR_RE.fullmatch(line[end]):
            parts.append(" ")
            modifications += 1
            continue

        if end < len(line):
            continue

    parts.append(line[cursor:])
    return "".join(parts), modifications


def normalize_mixed_text_spacing(line: str) -> tuple[str, int]:
    updated, count_1 = re.subn(rf"([{ZH_CHAR}])([{LATIN_NUM}])", r"\1 \2", line)
    updated, count_2 = re.subn(rf"([{LATIN_NUM}])([{ZH_CHAR}])", r"\1 \2", updated)
    return updated, count_1 + count_2


def normalize_line(line: str, in_block_math: bool) -> tuple[str, bool, int]:
    stripped = line.strip()

    if stripped == "$$" or stripped == r"\]":
        return line, False, 0
    if SINGLE_LINE_BLOCK_MATH_RE.match(line):
        return line, False, 0
    if stripped.startswith("$$") or stripped == r"\[":
        return line, True, 0
    if in_block_math or BLOCK_MATH_LINE_RE.match(line):
        return line, in_block_math, 0

    updated, modifications_1 = normalize_inline_math_spacing(line)
    updated, modifications_2 = normalize_mixed_text_spacing(updated)
    return updated, False, modifications_1 + modifications_2


def normalize_segment(text: str) -> tuple[str, int]:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_block_math = False
    modifications = 0

    for line in lines:
        updated, in_block_math, line_modifications = normalize_line(line, in_block_math)
        out.append(updated)
        modifications += line_modifications

    return "".join(out), modifications


def normalize_mixed_spacing(text: str) -> tuple[str, int]:
    parts: list[str] = []
    modifications = 0
    for is_code, segment in split_by_code_fences(text):
        if is_code:
            parts.append(segment)
            continue
        updated, segment_modifications = normalize_segment(segment)
        parts.append(updated)
        modifications += segment_modifications
    return "".join(parts), modifications


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md" and path.name.lower() != "index.md":
            files.append(path)
            continue
        if path.is_dir():
            files.extend(sorted(file for file in path.rglob("*.md") if file.name.lower() != "index.md"))
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
        description="Insert spaces between Chinese and English text, and around inline math."
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
    for file_path in iter_markdown_files(inputs):
        original = file_path.read_text(encoding="utf-8")
        updated, modifications = normalize_mixed_spacing(original)
        if updated == original:
            continue

        changed_files += 1
        print(f"{file_path} ({modifications})")
        if args.write:
            output_path = resolve_output_path(file_path, inputs, args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(updated, encoding="utf-8")

    summary = "Changed" if args.write else "Will change"
    print(f"{summary} {changed_files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
