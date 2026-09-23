from __future__ import annotations

import argparse
import sys
from pathlib import Path

from fix_list_spacing import normalize_list_spacing
from fix_math_block import normalize_block_math
from fix_math_punctuation import normalize_math_punctuation
from fix_mixed_spacing import normalize_mixed_spacing


PROCESSORS = (
    ("数学公式标点", normalize_math_punctuation),
    ("行间公式", normalize_block_math),
    ("混合空格", normalize_mixed_spacing),
    ("列表空行", normalize_list_spacing),
)


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
                return output / file_path.relative_to(root)
            except ValueError:
                continue

    return output / file_path.name


def process_file(text: str) -> tuple[str, list[tuple[str, int]]]:
    stage_counts: list[tuple[str, int]] = []
    updated = text

    for name, processor in PROCESSORS:
        if name == "数学公式标点":
            updated, records = processor(updated)
            count = len(records)
        elif name == "混合空格":
            updated, changes, _ = processor(updated)
            count = sum(changes.values())
        else:
            updated, count = processor(updated)
        stage_counts.append((name, count))

    return updated, stage_counts


def main() -> int:
    parser = argparse.ArgumentParser(
        description="按顺序运行数学公式标点、行间公式、混合空格和列表格式化。"
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs="*",
        type=Path,
        default=None,
        help="要处理的 Markdown 文件或目录。省略时默认为 docs/。",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="可选的输出文件或目录。未指定时配合 --write 覆盖源文件。",
    )
    parser.add_argument(
        "-w",
        "--write",
        action="store_true",
        help="将结果写入磁盘；不加此参数时只打印预览。",
    )

    if not sys.argv[1:]:
        parser.print_help()
        return 0

    args = parser.parse_args()
    inputs = args.input or [Path("docs")]
    changed_files = 0
    total_places = 0

    for file_path in iter_markdown_files(inputs):
        original = file_path.read_text(encoding="utf-8")
        updated, stage_counts = process_file(original)
        if updated == original:
            continue

        changed_files += 1
        total_places += sum(count for _, count in stage_counts)
        print(file_path)
        for name, count in stage_counts:
            if count:
                print(f"  {name}: {count}")

        if args.write:
            output_path = resolve_output_path(file_path, inputs, args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(updated, encoding="utf-8")

    summary = "Changed" if args.write else "Will change"
    print(f"{summary} {changed_files} files, total {total_places} places")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
