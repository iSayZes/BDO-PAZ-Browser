from __future__ import annotations

import re

from _common.loc import parse_loc_entries, strip_pa_tags

from ..common.binary import debug_u32_fields
from ..common.constants import PA_COLOR_MARKER
from .model import TitleBuffRecord


def find_title_effects_en(raw: bytes) -> dict[int, str]:
    entries = parse_loc_entries(raw)
    result: dict[int, str] = {}

    for text in entries:
        if "Acquire x50: Luck" not in text:
            continue

        for line in text.splitlines():
            match = re.match(r"Acquire x([\d,]+):\s*(.+)", line)

            if not match:
                continue

            required = int(match.group(1).replace(",", ""))
            result[required] = line

        if result:
            break

    return result


def decode_titlebuff_text(block: bytes) -> str:
    start = block.find(PA_COLOR_MARKER)

    if start == -1:
        return "—"

    text = block[start:].decode("utf-16-le", errors="ignore")
    text = text.replace("\x00", "")

    return " ".join(text.split())


def extract_titlebuff_records(
    data: bytes,
    offset_map: dict[int, tuple[int, int]],
) -> list[TitleBuffRecord]:
    records: list[TitleBuffRecord] = []

    for buff_id, (offset, size) in sorted(offset_map.items()):
        if offset + size > len(data):
            continue

        block = data[offset:offset + size]

        records.append(TitleBuffRecord(
            buff_id=buff_id,
            offset=offset,
            raw_text=strip_pa_tags(decode_titlebuff_text(block)),
            debug_u32=debug_u32_fields(block),
        ))

    return records
