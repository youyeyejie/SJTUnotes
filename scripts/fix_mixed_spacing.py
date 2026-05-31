from __future__ import annotations

import argparse
from collections import Counter
import re
import sys
from pathlib import Path


CODE_FENCE_START_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})")
INLINE_MATH_RE = re.compile(r"(?<!\\)(?<!\$)\$(?!\$).*?(?<!\\)\$(?!\$)|\\\(.*?\\\)")
INLINE_MARKUP_RE = re.compile(r"\*\*[^*\n]+?\*\*|\*[^*\n]+?\*|~~[^~\n]+?~~|`[^`\n]+?`")
BLOCK_MATH_LINE_RE = re.compile(r"^[ \t]*(\$\$|\\\[|\\\])")
SINGLE_LINE_BLOCK_MATH_RE = re.compile(r"^[ \t]*\$\$.*\$\$[ \t]*$")
ZH_CHAR = r"\u4e00-\u9fff"
LATIN_NUM = r"A-Za-z0-9"
TEXT_CHAR_RE = re.compile(rf"[{ZH_CHAR}{LATIN_NUM}]")
CHANGE_LABELS = {
    "zh_latin_num": "中后接英文/数字",
    "latin_num_zh": "英文/数字后接中文",
    "text_before_math": "文字前接公式",
    "math_before_text": "公式后接文字",
    "text_before_markup": "文字前接强调/代码标记",
    "markup_before_text": "强调/代码标记后接文字",
    "markup_before_math": "强调/代码标记前接公式",
    "math_before_markup": "公式前接强调/代码标记",
}
TOKEN_PATTERN = re.compile(
    r"(?<!\\)(?<!\$)\$(?!\$).*?(?<!\\)\$(?!\$)"
    r"|\\\(.*?\\\)"
    r"|\*\*[^*\n]+?\*\*"
    r"|\*[^*\n]+?\*"
    r"|~~[^~\n]+?~~"
    r"|`[^`\n]+?`"
)


def token_kind(token: str) -> str:
    if INLINE_MATH_RE.fullmatch(token):
        return "math"
    return "markup"


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


def normalize_inline_math_spacing(line: str) -> tuple[str, Counter[str]]:
    parts: list[str] = []
    cursor = 0
    changes: Counter[str] = Counter()

    for match in INLINE_MATH_RE.finditer(line):
        start, end = match.span()
        prefix = line[cursor:start]
        if start > 0 and TEXT_CHAR_RE.fullmatch(line[start - 1]):
            if prefix and not prefix.endswith(" "):
                prefix = prefix + " "
                changes["text_before_math"] += 1
        parts.append(prefix)

        parts.append(match.group(0))
        cursor = end

        if end < len(line) and TEXT_CHAR_RE.fullmatch(line[end]):
            parts.append(" ")
            changes["math_before_text"] += 1
            continue

        if end < len(line):
            continue

    parts.append(line[cursor:])
    return "".join(parts), changes


def normalize_token_spacing(line: str) -> tuple[str, Counter[str]]:
    parts: list[str] = []
    cursor = 0
    changes: Counter[str] = Counter()

    for match in TOKEN_PATTERN.finditer(line):
        start, end = match.span()
        token = match.group(0)
        kind = token_kind(token)

        prefix = line[cursor:start]
        previous_char = line[start - 1] if start > 0 else ""
        if previous_char and TEXT_CHAR_RE.fullmatch(previous_char):
            if prefix and not prefix.endswith(" "):
                prefix += " "
                changes[f"text_before_{kind}"] += 1

        parts.append(prefix)
        parts.append(token)
        cursor = end

        next_char = line[end] if end < len(line) else ""
        if next_char and TEXT_CHAR_RE.fullmatch(next_char):
            parts.append(" ")
            changes[f"{kind}_before_text"] += 1
        else:
            next_match = TOKEN_PATTERN.match(line, end)
            if next_match:
                parts.append(" ")
                next_kind = token_kind(next_match.group(0))
                if kind == "math" and next_kind == "markup":
                    changes["math_before_markup"] += 1
                elif kind == "markup" and next_kind == "math":
                    changes["markup_before_math"] += 1

    parts.append(line[cursor:])
    return "".join(parts), changes


def normalize_mixed_text_spacing(line: str) -> tuple[str, Counter[str]]:
    parts: list[str] = []
    changes: Counter[str] = Counter()
    cursor = 0

    for match in TOKEN_PATTERN.finditer(line):
        start, end = match.span()
        prefix = line[cursor:start]
        updated, count_1 = re.subn(rf"([{ZH_CHAR}])([{LATIN_NUM}])", r"\1 \2", prefix)
        updated, count_2 = re.subn(rf"([{LATIN_NUM}])([{ZH_CHAR}])", r"\1 \2", updated)
        if count_1:
            changes["zh_latin_num"] += count_1
        if count_2:
            changes["latin_num_zh"] += count_2
        parts.append(updated)
        parts.append(match.group(0))
        cursor = end

    suffix = line[cursor:]
    updated, count_1 = re.subn(rf"([{ZH_CHAR}])([{LATIN_NUM}])", r"\1 \2", suffix)
    updated, count_2 = re.subn(rf"([{LATIN_NUM}])([{ZH_CHAR}])", r"\1 \2", updated)
    if count_1:
        changes["zh_latin_num"] += count_1
    if count_2:
        changes["latin_num_zh"] += count_2
    parts.append(updated)
    return "".join(parts), changes


def normalize_line(line: str, in_block_math: bool) -> tuple[str, bool, Counter[str]]:
    stripped = line.strip()

    if stripped == "$$" or stripped == r"\]":
        return line, False, Counter()
    if SINGLE_LINE_BLOCK_MATH_RE.match(line):
        return line, False, Counter()
    if stripped.startswith("$$") or stripped == r"\[":
        return line, True, Counter()
    if in_block_math or BLOCK_MATH_LINE_RE.match(line):
        return line, in_block_math, Counter()

    updated, changes_1 = normalize_token_spacing(line)
    updated, changes_3 = normalize_mixed_text_spacing(updated)
    changes_1.update(changes_3)
    return updated, False, changes_1


def normalize_segment(text: str) -> tuple[str, Counter[str], list[int]]:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_block_math = False
    changes: Counter[str] = Counter()
    changed_lines: list[int] = []

    for line_number, line in enumerate(lines, start=1):
        updated, in_block_math, line_changes = normalize_line(line, in_block_math)
        out.append(updated)
        if line_changes:
            changes.update(line_changes)
            changed_lines.append(line_number)

    return "".join(out), changes, changed_lines


def normalize_mixed_spacing(text: str) -> tuple[str, Counter[str], list[int]]:
    parts: list[str] = []
    changes: Counter[str] = Counter()
    changed_lines: list[int] = []
    line_offset = 0

    for is_code, segment in split_by_code_fences(text):
        if is_code:
            parts.append(segment)
            line_offset += segment.count("\n")
            continue

        updated, segment_changes, segment_lines = normalize_segment(segment)
        parts.append(updated)
        changes.update(segment_changes)
        changed_lines.extend(line_offset + line_number for line_number in segment_lines)
        line_offset += segment.count("\n")

    return "".join(parts), changes, changed_lines


def format_change_summary(changes: Counter[str]) -> str:
    parts: list[str] = []
    for key in (
        "zh_latin_num",
        "latin_num_zh",
        "text_before_math",
        "math_before_text",
        "text_before_markup",
        "markup_before_text",
        "markup_before_math",
        "math_before_markup",
    ):
        count = changes.get(key, 0)
        if count:
            label = CHANGE_LABELS.get(key, key)
            parts.append(f"{label} x{count}")
    return ", ".join(parts)


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
    total_places = 0
    for file_path in iter_markdown_files(inputs):
        original = file_path.read_text(encoding="utf-8")
        updated, changes, changed_lines = normalize_mixed_spacing(original)
        if updated == original:
            continue

        changed_files += 1
        total_places += sum(changes.values())
        print(file_path)
        print(f"  replacements: {sum(changes.values())}")
        print(f"  symbols: {format_change_summary(changes)}")
        print(f"  lines: {', '.join(str(line) for line in changed_lines)}")
        if args.write:
            output_path = resolve_output_path(file_path, inputs, args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(updated, encoding="utf-8")

    summary = "Changed" if args.write else "Will change"
    print(f"{summary} {changed_files} files, total {total_places} places")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
