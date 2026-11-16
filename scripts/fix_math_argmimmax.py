from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# Include the common argimin/argimax misspellings. A subscript is one
# TeX token or an existing braced group (which is preserved verbatim).
ARG_OPERATOR = re.compile(
    r"(?<!\\)\\arg(?:i)?(?P<kind>min|max)(?![A-Za-z])"
    r"(?:\s*(?:\\limits\s*)?(?:\\)?_(?P<space>\s*)"
    r"(?P<token>\{|\\[A-Za-z]+|\\[^A-Za-z]|[^\s{}]))?"
)


def normalize_argminmax(text: str) -> tuple[str, int]:
    def replace(match: re.Match[str]) -> str:
        operator = "\\mathop{\\arg\\" + match.group("kind") + r"}\limits"
        token = match.group("token")
        if token == "{":
            return operator + "_{"
        if token is not None:
            return operator + "_{" + token + "}"
        return operator

    return ARG_OPERATOR.subn(replace, text)


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
        description="Normalize argmin/argmax operators and their subscripts."
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
        updated, modifications = normalize_argminmax(original)
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
