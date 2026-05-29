from __future__ import annotations

import argparse
import re
from pathlib import Path
from dataclasses import dataclass


MATH_DELIMITER_RE = re.compile(
    r"(?P<block_dollar>\$\$.*?\$\$)"
    r"|(?P<block_bracket>\\\[.*?\\\])"
    r"|(?P<inline_paren>\\\(.*?\\\))"
    r"|(?P<inline_dollar>(?<!\\)(?<!\$)\$(?!\$).*?(?<!\\)\$(?!\$))",
    re.DOTALL,
)

CODE_FENCE_START_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})")

PUNCTUATION_MAP = {
    "，": ",",
    "；": ";",
    "：": ":",
    "（": "(",
    "）": ")",
    "【": "[",
    "】": "]",
    "｛": "{",
    "｝": "}",
    "。": ".",
    "、": ",",
    "！": "!",
    "？": "?",
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
    "《": "<",
    "》": ">",
}
ELLIPSIS_REPLACEMENTS = {
    "……": r"\cdots",
    "…": r"\cdots",
}


@dataclass
class ReplacementRecord:
    line: int
    original: str
    replaced: str


def replace_punctuation_in_math(text: str, base_line: int) -> tuple[str, list[ReplacementRecord]]:
    records: list[ReplacementRecord] = []
    result_parts: list[str] = []
    last_end = 0

    for match in MATH_DELIMITER_RE.finditer(text):
        result_parts.append(text[last_end : match.start()])
        segment = match.group(0)
        segment_line = base_line + text.count("\n", 0, match.start())

        rebuilt: list[str] = []
        index = 0
        while index < len(segment):
            ellipsis_matched = False
            for original, replacement in ELLIPSIS_REPLACEMENTS.items():
                if segment.startswith(original, index):
                    rebuilt.append(replacement)
                    records.append(
                        ReplacementRecord(
                            line=segment_line + segment.count("\n", 0, index),
                            original=original,
                            replaced=replacement,
                        )
                    )
                    index += len(original)
                    ellipsis_matched = True
                    break

            if ellipsis_matched:
                continue

            char = segment[index]
            replacement = PUNCTUATION_MAP.get(char, char)
            rebuilt.append(replacement)
            if replacement != char:
                records.append(
                    ReplacementRecord(
                        line=segment_line + segment.count("\n", 0, index),
                        original=char,
                        replaced=replacement,
                    )
                )
            index += 1

        result_parts.append("".join(rebuilt))
        last_end = match.end()

    result_parts.append(text[last_end:])
    return "".join(result_parts), records


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


def normalize_math_punctuation(text: str) -> tuple[str, list[ReplacementRecord]]:
    parts: list[str] = []
    records: list[ReplacementRecord] = []
    current_line = 1
    for is_code, segment in split_by_code_fences(text):
        if is_code:
            parts.append(segment)
        else:
            updated, segment_records = replace_punctuation_in_math(segment, current_line)
            parts.append(updated)
            records.extend(segment_records)
        current_line += segment.count("\n")
    return "".join(parts), records


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            files.append(path)
            continue
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return files


def summarize_records(records: list[ReplacementRecord]) -> tuple[str, str]:
    symbol_counts: dict[str, int] = {}
    line_numbers: list[int] = []

    for record in records:
        key = f"{record.original}->{record.replaced}"
        symbol_counts[key] = symbol_counts.get(key, 0) + 1
        if record.line not in line_numbers:
            line_numbers.append(record.line)

    symbols = ", ".join(f"{key} x{count}" for key, count in sorted(symbol_counts.items()))
    lines = ", ".join(str(line) for line in line_numbers)
    return symbols, lines


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Replace Chinese punctuation with ASCII punctuation inside math formulas."
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
        updated, records = normalize_math_punctuation(original)
        if updated == original:
            continue

        changed_files += 1
        symbols, lines = summarize_records(records)
        print(file_path)
        print(f"  replacements: {len(records)}")
        print(f"  symbols: {symbols}")
        print(f"  lines: {lines}")
        if args.write:
            file_path.write_text(updated, encoding="utf-8")

    print(f"Changed files: {changed_files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
