"""The list of every doc that the index table and the doc sidebar show (`formats.js`)."""
from __future__ import annotations

import json
import re
from collections.abc import Iterable
from dataclasses import asdict, dataclass

from format_docs.doc_index import index_rows

from .doc_source import DocSource, first_sentence
from .layout_view import layout_views

_COUNTED_EXTS = ("bss", "dbss")
# README's Supported Formats lines, kept current from the game files by the pre-commit hook.
_GAME_TOTAL = re.compile(r"Handler Supported \d+/(?P<total>\d+) \.(?P<ext>bss|dbss) formats")


@dataclass(frozen=True)
class FormatEntry:
    page: str
    name: str
    others: tuple[str, ...]
    desc: str
    ext: str
    oq: int
    ig: int
    converted: bool
    known: int
    unknown: int


def format_entry(doc: DocSource, rows: list[tuple[str, str]]) -> FormatEntry:
    files = [file for file, _ in rows]
    desc = next((text for file, text in rows if file == doc.name), rows[0][1] if rows else "")
    purpose = doc.section("Purpose")
    if not desc and purpose is not None:
        desc = first_sentence(purpose.markdown)
    known = unknown = 0
    if doc.is_converted:
        newest = layout_views(doc)[0]
        known, unknown = newest.known, newest.unknown
    return FormatEntry(
        page=doc.page,
        name=doc.name,
        others=tuple(file for file in files if file != doc.name),
        desc=desc,
        ext=_ext(doc.path.stem),
        oq=doc.open_questions,
        ig=doc.in_game_checks,
        converted=doc.is_converted,
        known=known,
        unknown=unknown,
    )


def documented_counts(rows: dict[str, list[tuple[str, str]]]) -> dict[str, int]:
    """How many `.bss` and `.dbss` files the index rows document; patterns like `*.ai` are left out."""
    files = {file for doc_rows in rows.values() for file, _ in doc_rows if not any(char in file for char in "*{")}
    return {ext: sum(1 for file in files if file.endswith(f".{ext}")) for ext in _COUNTED_EXTS}


def game_totals(readme: str) -> dict[str, int]:
    """The `.bss` and `.dbss` file counts of the game, from README's Supported Formats lines."""
    return {match.group("ext"): int(match.group("total")) for match in _GAME_TOTAL.finditer(readme)}


def formats_script(entries: Iterable[FormatEntry], documented: dict[str, int], totals: dict[str, int]) -> str:
    data = json.dumps([asdict(entry) for entry in entries], ensure_ascii=False, separators=(",", ":"))
    summary = json.dumps({"documented": documented, "totals": totals}, separators=(",", ":"))
    return f"var FORMATS = {data};\nvar SUMMARY = {summary};\n"


def _ext(doc_stem: str) -> str:
    """`bss` or `dbss` from the doc's file name (`buff_dbss`), else `other`."""
    suffix = doc_stem.rsplit("_", 1)[-1]
    return suffix if suffix in ("bss", "dbss") else "other"
