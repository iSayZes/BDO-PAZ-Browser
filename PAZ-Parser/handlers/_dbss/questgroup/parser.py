from __future__ import annotations

from .model import QuestGroupLink, QuestGroupRecord


def _u16(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 2 > len(data):
        raise ValueError(f"u16 read out of bounds at 0x{offset:X}")
    return int.from_bytes(data[offset:offset + 2], "little")


def _u32(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 4 > len(data):
        raise ValueError(f"u32 read out of bounds at 0x{offset:X}")
    return int.from_bytes(data[offset:offset + 4], "little")


def parse_questgroup_records(data: bytes) -> list[QuestGroupRecord]:
    if len(data) < 4:
        return []

    count = _u32(data, 0)
    offset = 4
    records: list[QuestGroupRecord] = []

    for row in range(count):
        start = offset
        if offset + 10 > len(data):
            raise ValueError(f"questgroup record {row} header exceeds file size")

        group_id = _u16(data, offset)
        name_len = _u16(data, offset + 2)
        unknown_04 = _u32(data, offset + 4)
        unknown_08 = _u16(data, offset + 8)
        offset += 10

        name_end = offset + name_len * 2
        if name_end + 8 > len(data):
            raise ValueError(f"questgroup record {row} text exceeds file size")

        name_kr = data[offset:name_end].decode("utf-16le", errors="replace")
        offset = name_end

        quest_count = _u32(data, offset)
        offset += 4
        quests: list[QuestGroupLink] = []
        for _ in range(quest_count):
            if offset + 4 > len(data):
                raise ValueError(f"questgroup record {row} quest list exceeds file size")
            child_group_id = _u16(data, offset)
            quest_no = _u16(data, offset + 2)
            quests.append(
                QuestGroupLink(
                    group_id=child_group_id,
                    quest_no=quest_no,
                    quest_id=(quest_no << 16) | child_group_id,
                )
            )
            offset += 4

        tail_zero = _u32(data, offset)
        offset += 4
        if unknown_04 != 0 or unknown_08 != 0 or tail_zero != 0:
            raise ValueError(f"questgroup record {row} has unexpected non-zero padding")

        records.append(
            QuestGroupRecord(
                row=row,
                offset=start,
                size=offset - start,
                group_id=group_id,
                name_kr=name_kr,
                quest_count=quest_count,
                quests=quests,
            )
        )

    if offset != len(data):
        raise ValueError(f"questgroup parser stopped at 0x{offset:X}, file size is 0x{len(data):X}")

    return records
