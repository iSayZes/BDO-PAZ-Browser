from __future__ import annotations

import argparse
import logging
import struct
import sys
from pathlib import Path
from typing import BinaryIO

from bdo_meta_reader import read_bdo_meta
from bdo_models import MetaFile, PazEntry
from bdo_paz_reader import parse_paz_file
from bdo_payload_reader import read_entry_payload


class PazFormatError(Exception):
    pass


def configure_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def read_exact(stream: BinaryIO, size: int) -> bytes:
    data: bytes = stream.read(size)
    if len(data) != size:
        raise EOFError(f"Expected {size} bytes but got {len(data)}")
    return data


def read_u32(stream: BinaryIO) -> int:
    return struct.unpack("<I", read_exact(stream, 4))[0]


def read_u64(stream: BinaryIO) -> int:
    return struct.unpack("<Q", read_exact(stream, 8))[0]


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def sanitize_relative_path(path_value: str) -> Path:
    candidate: Path = Path(path_value.replace("\\", "/"))
    if candidate.is_absolute():
        raise ValueError(f"Absolute internal path is not allowed: {path_value}")

    normalized_parts: list[str] = []
    for part in candidate.parts:
        if part in ("", "."):
            continue
        if part == "..":
            raise ValueError(f"Parent traversal is not allowed: {path_value}")
        normalized_parts.append(part)

    if not normalized_parts:
        raise ValueError(f"Empty internal path is not allowed: {path_value}")

    return Path(*normalized_parts)


def find_single_meta_file(paz_root: Path) -> Path:
    meta_files: list[Path] = sorted(paz_root.glob("*.meta"))

    if len(meta_files) == 0:
        raise FileNotFoundError(f"No .meta file found in folder: {paz_root}")

    if len(meta_files) > 1:
        file_list: str = "\n".join(str(path) for path in meta_files[:20])
        raise ValueError(
            "Expected exactly one .meta file in the target folder, "
            f"but found {len(meta_files)}.\n"
            f"Folder: {paz_root}\n"
            f"Matches:\n{file_list}"
        )

    return meta_files[0]



def parse_meta_file(meta_path: Path) -> list[PazEntry]:
    paz_root: Path = meta_path.parent
    meta: MetaFile = read_bdo_meta(meta_path)

    all_entries: list[PazEntry] = []

    for paz_table in meta.paz_files:
        paz_name: str = f"pad{paz_table.paz_file_id:05d}.paz"
        paz_path: Path = paz_root / paz_name

        if not paz_path.exists():
            logging.warning("Referenced archive not found: %s", paz_path)
            continue

        paz_entries: list[PazEntry] = parse_paz_file(
            paz_path=paz_path,
            paz_table=paz_table,
        )
        all_entries.extend(paz_entries)

    return all_entries


def extract_entry(
    paz_root: Path,
    output_root: Path,
    entry: PazEntry,
    overwrite: bool,
    flat: bool = False,
) -> str:
    """Return 'extracted' or 'skipped'."""
    archive_path: Path = paz_root / entry.archive_name
    if not archive_path.exists():
        raise FileNotFoundError(f"Archive not found: {archive_path}")

    if flat:
        filename = Path(entry.internal_path.replace("\\", "/")).name
        output_path = output_root / filename
    else:
        relative_output_path: Path = sanitize_relative_path(entry.internal_path)
        output_path = output_root / relative_output_path

    if output_path.exists() and not overwrite:
        return "skipped"

    ensure_directory(output_path.parent)

    final_payload: bytes = read_entry_payload(
        archive_path=archive_path,
        entry=entry,
    )

    if len(final_payload) != entry.uncompressed_size:
        raise PazFormatError(
            f"Size mismatch for {entry.internal_path}: "
            f"expected {entry.uncompressed_size}, got {len(final_payload)}"
        )

    output_path.write_bytes(final_payload)
    return "extracted"


def _normalize_ext(raw: str) -> str:
    ext: str = raw.strip().lower()
    return ext if ext.startswith(".") else "." + ext


# ── Tree generation ──────────────────────────────────────────────────────────

def _build_tree(paths: list[str]) -> dict:
    root: dict = {}
    for path in paths:
        parts = Path(path.replace("\\", "/")).parts
        node = root
        for part in parts[:-1]:
            if part not in node or not isinstance(node[part], dict):
                node[part] = {}
            node = node[part]
        filename = parts[-1]
        if filename not in node:
            node[filename] = None
    return root


def _render_tree_lines(node: dict, continuation: str, lines: list[str]) -> None:
    items = sorted(node.items(), key=lambda x: (isinstance(x[1], dict), x[0].lower()))
    files = [(k, v) for k, v in items if v is None]
    dirs = [(k, v) for k, v in items if isinstance(v, dict)]

    for fname, _ in files:
        lines.append(f"{continuation}│   {fname}")

    for i, (dname, dnode) in enumerate(dirs):
        is_last = i == len(dirs) - 1
        lines.append(continuation + "│")
        connector = "└───" if is_last else "├───"
        lines.append(f"{continuation}{connector}{dname}")
        child_cont = continuation + ("    " if is_last else "│   ")
        _render_tree_lines(dnode, child_cont, lines)


def generate_tree_markdown(entries: list[PazEntry], root_name: str) -> str:
    paths = [e.internal_path for e in entries]
    tree = _build_tree(paths)

    lines: list[str] = [root_name]
    _render_tree_lines(tree, "", lines)

    tree_text = "\n".join(lines)
    return f"# PAZ File Tree\n\n```\n{tree_text}\n```\n\n*{len(paths):,} files total*\n"


def write_tree(
    paz_root: Path,
    meta_path: Path,
    output_file: Path,
    path_filter: str | None,
    type_filter: list[str] | None,
    exclude_type: list[str] | None,
) -> None:
    entries: list[PazEntry] = parse_meta_file(meta_path)

    if path_filter:
        normalized_filter = path_filter.lower()
        entries = [e for e in entries if normalized_filter in Path(e.internal_path).name.lower()]

    if type_filter:
        flat_exts: list[str] = [tok for t in type_filter for tok in t.split()]
        allowed_exts: set[str] = {_normalize_ext(t) for t in flat_exts}
        entries = [e for e in entries if Path(e.internal_path).suffix.lower() in allowed_exts]

    if exclude_type:
        flat_exts = [tok for t in exclude_type for tok in t.split()]
        blocked_exts: set[str] = {_normalize_ext(t) for t in flat_exts}
        entries = [e for e in entries if Path(e.internal_path).suffix.lower() not in blocked_exts]

    logging.info("Building tree for %d entries…", len(entries))
    markdown = generate_tree_markdown(entries, paz_root.name)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(markdown, encoding="utf-8")
    logging.info("Tree written to: %s", output_file)


def extract_all(
    paz_root: Path,
    meta_path: Path,
    output_root: Path,
    overwrite: bool,
    path_filter: str | None,
    type_filter: list[str] | None,
) -> None:
    entries: list[PazEntry] = parse_meta_file(meta_path)

    if path_filter:
        normalized_filter: str = path_filter.lower()
        entries = [
            entry
            for entry in entries
            if normalized_filter in entry.internal_path.lower()
        ]

    if type_filter:
        # Support both --type .dds .png  and  --type ".dds .png"
        flat_exts: list[str] = [tok for t in type_filter for tok in t.split()]
        allowed_exts: set[str] = {_normalize_ext(t) for t in flat_exts}
        entries = [
            entry
            for entry in entries
            if Path(entry.internal_path).suffix.lower() in allowed_exts
        ]

    total: int = len(entries)
    logging.info("Using meta file: %s", meta_path)
    logging.info("Entries to process: %d", total)

    extracted: int = 0
    skipped: int = 0
    failed: int = 0

    for i, entry in enumerate(entries, start=1):
        try:
            result: str = extract_entry(
                paz_root=paz_root,
                output_root=output_root,
                entry=entry,
                overwrite=overwrite,
            )
            if result == "skipped":
                skipped += 1
                logging.debug("[%d/%d] Skipped (exists): %s", i, total, entry.internal_path)
            else:
                extracted += 1
                logging.info("[%d/%d] Extracted: %s", i, total, entry.internal_path)
        except Exception as ex:
            failed += 1
            logging.error("[%d/%d] FAILED %s: %s", i, total, entry.internal_path, ex)

    logging.info(
        "Done — extracted: %d  skipped: %d  failed: %d  total: %d",
        extracted, skipped, failed, total,
    )


def build_parser() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Custom BDO PAZ extractor skeleton."
    )
    parser.add_argument(
        "--paz-root",
        type=Path,
        default=None,
        help="Folder containing BDO .paz files and exactly one .meta file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output folder.",
    )
    parser.add_argument(
        "--filter",
        type=str,
        default=None,
        help="Optional case-insensitive substring filter on internal paths.",
    )
    parser.add_argument(
        "--type",
        type=str,
        nargs="+",
        default=None,
        metavar="EXT",
        help="Only extract files with these extensions, e.g. --type .dds .png (case-insensitive).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging.",
    )
    parser.add_argument(
        "--exclude-type",
        type=str,
        nargs="+",
        default=None,
        metavar="EXT",
        help="Exclude files with these extensions, e.g. --exclude-type .dds .png (case-insensitive).",
    )
    parser.add_argument(
        "--tree",
        action="store_true",
        help="Generate a markdown file tree instead of extracting files.",
    )
    parser.add_argument(
        "--tree-file",
        type=Path,
        default=None,
        metavar="FILE",
        help="Output path for the markdown tree (default: <paz-root>/paz_tree.md). Implies --tree.",
    )
    return parser


def main() -> int:
    parser: argparse.ArgumentParser = build_parser()
    args: argparse.Namespace = parser.parse_args()

    configure_logging(args.verbose)

    paz_root: Path = args.paz_root
    output_root: Path = args.output

    if not paz_root.exists() or not paz_root.is_dir():
        logging.error("PAZ root does not exist: %s", paz_root)
        return 1

    try:
        meta_path: Path = find_single_meta_file(paz_root)
    except Exception as ex:
        logging.error(str(ex))
        return 1

    tree_mode: bool = args.tree or args.tree_file is not None

    if tree_mode:
        tree_output: Path = args.tree_file or (paz_root / "paz_tree.md")
        try:
            write_tree(
                paz_root=paz_root,
                meta_path=meta_path,
                output_file=tree_output,
                path_filter=args.filter,
                type_filter=args.type,
                exclude_type=args.exclude_type,
            )
        except Exception as ex:
            logging.exception("Fatal error: %s", ex)
            return 3
        return 0

    ensure_directory(output_root)

    try:
        extract_all(
            paz_root=paz_root,
            meta_path=meta_path,
            output_root=output_root,
            overwrite=args.overwrite,
            path_filter=args.filter,
            type_filter=args.type,
        )
    except NotImplementedError as ex:
        logging.error(str(ex))
        return 2
    except Exception as ex:
        logging.exception("Fatal error: %s", ex)
        return 3

    return 0


if __name__ == "__main__":
    sys.exit(main())