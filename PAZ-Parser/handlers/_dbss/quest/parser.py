from __future__ import annotations

import re
import struct
from dataclasses import dataclass

from .model import QuestRecord


_MAX_SCRIPT_CHARS = 20_000
_MAX_OBJECTIVE_SCAN = 1024
_ICON_RE = re.compile(rb"Icon/[A-Za-z0-9_./ \-]+\.dds", re.IGNORECASE)


@dataclass(frozen=True)
class QuestIndex:
    declared_count: int
    starts: list[int]


def _u32(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 4 > len(data):
        return 0
    return struct.unpack_from("<I", data, offset)[0]


def _is_text_clean(text: str) -> bool:
    return "\ufffd" not in text and all(ch >= " " or ch in "\n\r\t" for ch in text)


def _read_utf16_field(
    data: bytes,
    offset: int,
    max_chars: int = _MAX_SCRIPT_CHARS,
) -> tuple[str, int] | None:
    if offset + 8 > len(data):
        return None

    char_count = _u32(data, offset)
    zero = _u32(data, offset + 4)
    byte_count = char_count * 2
    text_start = offset + 8
    text_end = text_start + byte_count

    if zero != 0 or char_count > max_chars or text_end > len(data):
        return None

    text = data[text_start:text_end].decode("utf-16-le", errors="replace")
    if not _is_text_clean(text):
        return None

    return text, text_end


def _find_objective_field(data: bytes, offset: int) -> tuple[str, int] | None:
    scan_end = min(len(data) - 8, offset + _MAX_OBJECTIVE_SCAN)

    for candidate in range(offset, scan_end + 1):
        if any(data[offset:candidate]):
            break
        parsed = _read_utf16_field(data, candidate, max_chars=5000)
        if parsed is None:
            continue
        text, end = parsed
        if text:
            return text, end

    return None


def _parse_fixed_strings(data: bytes, offset: int) -> tuple[str, str, str, int] | None:
    condition = _read_utf16_field(data, offset + 12)
    if condition is None:
        return None

    condition_script, pos = condition
    action = _read_utf16_field(data, pos)
    if action is None:
        return None

    action_script, pos = action
    objective = _find_objective_field(data, pos)
    if objective is None:
        return condition_script, action_script, "", pos

    objective_text_kr, pos = objective
    return condition_script, action_script, objective_text_kr, pos


def looks_like_quest_start(data: bytes, offset: int) -> bool:
    if offset + 24 > len(data):
        return False

    quest_id = _u32(data, offset)
    if quest_id == 0 or quest_id > 10_000_000:
        return False

    if _u32(data, offset + 4) != quest_id:
        return False

    if _u32(data, offset + 8) != 0:
        return False

    parsed = _parse_fixed_strings(data, offset)
    return parsed is not None


def _find_next_start(data: bytes, start: int) -> int:
    offset = start + (start & 1)
    while offset + 24 <= len(data):
        if looks_like_quest_start(data, offset):
            return offset
        offset += 2
    return len(data)


def build_quest_index(data: bytes) -> QuestIndex:
    if len(data) < 4:
        return QuestIndex(0, [])

    declared_count = _u32(data, 0)
    starts: list[int] = []
    offset = 4

    while len(starts) < declared_count and offset + 24 <= len(data):
        if not looks_like_quest_start(data, offset):
            break

        starts.append(offset)
        parsed = _parse_fixed_strings(data, offset)
        next_scan_start = parsed[3] if parsed is not None else offset + 24
        next_offset = _find_next_start(data, max(next_scan_start, offset + 24))
        if next_offset <= offset or next_offset >= len(data):
            break
        offset = next_offset

    return QuestIndex(declared_count, starts)


def _icon_path(data: bytes, start: int, end: int) -> str:
    match = None
    for match in _ICON_RE.finditer(data, start, end):
        pass

    if match is None:
        return ""

    return match.group(0).decode("ascii", errors="replace")


def parse_quest_record(
    data: bytes,
    row: int,
    start: int,
    end: int,
    loc_texts: list[str] | None = None,
) -> QuestRecord | None:
    parsed = _parse_fixed_strings(data, start)
    if parsed is None:
        return None

    condition_script, action_script, objective_text_kr, _pos = parsed

    return QuestRecord(
        row=row,
        offset=start,
        size=max(0, end - start),
        quest_id=_u32(data, start),
        condition_script=condition_script,
        action_script=action_script,
        objective_text_kr=objective_text_kr,
        icon_path=_icon_path(data, start, end),
        loc_texts_en=loc_texts or [],
    )


def parse_quest_records(data: bytes) -> list[QuestRecord]:
    index = build_quest_index(data)
    records: list[QuestRecord] = []

    for row, start in enumerate(index.starts):
        end = index.starts[row + 1] if row + 1 < len(index.starts) else len(data)
        record = parse_quest_record(data, row, start, end)
        if record is not None:
            records.append(record)

    return records
