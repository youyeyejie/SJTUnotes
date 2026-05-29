from __future__ import annotations

import argparse
import re
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


def normalize_inline_math_spacing(line: str) -> str:
    parts: list[str] = []
    cursor = 0

    for match in INLINE_MATH_RE.finditer(line):
        start, end = match.span()
        prefix = line[cursor:start]
        if start > 0 and TEXT_CHAR_RE.fullmatch(line[start - 1]):
            if prefix and not prefix.endswith(" "):
                prefix = prefix + " "
        parts.append(prefix)

        parts.append(match.group(0))
        cursor = end

        if end < len(line) and TEXT_CHAR_RE.fullmatch(line[end]):
            parts.append(" ")
            continue

        if end < len(line):
            continue

    parts.append(line[cursor:])
    return "".join(parts)


def normalize_mixed_text_spacing(line: str) -> str:
    updated = line
    updated = re.sub(rf"([{ZH_CHAR}])([{LATIN_NUM}])", r"\1 \2", updated)
    updated = re.sub(rf"([{LATIN_NUM}])([{ZH_CHAR}])", r"\1 \2", updated)
    return updated


def normalize_line(line: str, in_block_math: bool) -> tuple[str, bool]:
    stripped = line.strip()

    if stripped == "$$" or stripped == r"\]":
        return line, False
    if SINGLE_LINE_BLOCK_MATH_RE.match(line):
        return line, False
    if stripped.startswith("$$") or stripped == r"\[":
        return line, True
    if in_block_math or BLOCK_MATH_LINE_RE.match(line):
        return line, in_block_math

    updated = normalize_inline_math_spacing(line)
    updated = normalize_mixed_text_spacing(updated)
    return updated, False


def normalize_segment(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_block_math = False

    for line in lines:
        updated, in_block_math = normalize_line(line, in_block_math)
        out.append(updated)

    return "".join(out)


def normalize_mixed_spacing(text: str) -> str:
    parts: list[str] = []
    for is_code, segment in split_by_code_fences(text):
        if is_code:
            parts.append(segment)
            continue
        parts.append(normalize_segment(segment))
    return "".join(parts)


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
        description="Insert spaces between Chinese and English text, and around inline math."
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
        updated = normalize_mixed_spacing(original)
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
