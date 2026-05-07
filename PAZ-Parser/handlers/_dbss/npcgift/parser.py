from __future__ import annotations

from _common.binary import u16 as _u16, u32 as _u32
from _common.loc import is_loc_loaded, loc_lookup, loc_lookup_prefix, strip_pa_tags

from .model import NpcGiftDataRecord, NpcGiftFlatRecord, NpcGiftOffsetRecord

_OFFSET_RECORD_SIZE = 10  # u16 npc_id + u32 data_offset + u16 data_size + u16 padding
_GIFT_ROW_SIZE = 12       # u32 item_id + u32 amity_a + u32 amity_b


def _npc_name(npc_id: int) -> str:
    raw = loc_lookup(6, npc_id)
    return strip_pa_tags(raw) if raw else ""


def _item_name(item_id: int) -> str:
    raw = loc_lookup(0, item_id)
    return strip_pa_tags(raw) if raw else ""


def _dialogue_en(npc_id: int) -> str:
    texts = loc_lookup_prefix(54, npc_id)
    for t in texts:
        clean = strip_pa_tags(t).strip()
        if clean:
            return clean
    return ""


def parse_gift_offset_records(data: bytes) -> list[NpcGiftOffsetRecord]:
    if len(data) < 4:
        return []

    count = _u32(data, 0)
    records: list[NpcGiftOffsetRecord] = []
    pos = 4

    for _ in range(count):
        if pos + _OFFSET_RECORD_SIZE > len(data):
            break
        records.append(NpcGiftOffsetRecord(
            npc_id=_u16(data, pos),
            data_offset=_u32(data, pos + 2),
            data_size=_u16(data, pos + 6),
            padding=_u16(data, pos + 8),
        ))
        pos += _OFFSET_RECORD_SIZE

    return records


def parse_npcgift_records(data: bytes) -> list[NpcGiftFlatRecord]:
    """Parse npcgift.dbss sequentially, yielding one flat row per gift item."""
    if len(data) < 4:
        return []

    count = _u32(data, 0)
    records: list[NpcGiftFlatRecord] = []
    pos = 4
    loc = is_loc_loaded()

    for _ in range(count):
        if pos + 6 > len(data):
            break

        npc_id     = _u16(data, pos)
        gift_count = _u32(data, pos + 2)
        pos += 6

        npc_name = _npc_name(npc_id) if loc else ""

        for _ in range(gift_count):
            if pos + _GIFT_ROW_SIZE > len(data):
                break

            item_id = _u32(data, pos)
            amity_a = _u32(data, pos + 4)
            # amity_b at pos+8 is a duplicate of amity_a in all observed rows
            pos += _GIFT_ROW_SIZE

            records.append(NpcGiftFlatRecord(
                npc_id=npc_id,
                npc_name=npc_name,
                item_id=item_id,
                item_name=_item_name(item_id) if loc else "",
                amity=amity_a,
            ))

    return records


def parse_npcgiftdata_records(data: bytes) -> list[NpcGiftDataRecord]:
    """Parse npcgiftdata.dbss sequentially, resolving English dialogue from LOC type 54."""
    if len(data) < 4:
        return []

    count = _u32(data, 0)
    records: list[NpcGiftDataRecord] = []
    pos = 4
    loc = is_loc_loaded()

    for _ in range(count):
        # Record header: u16(2) + u32(4) + u32(4) + u32(4) = 14 bytes
        if pos + 14 > len(data):
            break

        npc_id        = _u16(data, pos)
        unknown_param = _u32(data, pos + 2)
        text_len      = _u32(data, pos + 6)
        # zero field at pos+10 is always 0, skip
        pos += 14

        text_bytes = text_len * 2
        # +4 for the two trailing u16 tail values
        if pos + text_bytes + 4 > len(data):
            break

        inline_text = data[pos:pos + text_bytes].decode("utf-16-le", errors="replace")
        pos += text_bytes + 4

        npc_name = _npc_name(npc_id) if loc else ""

        en_text = _dialogue_en(npc_id) if loc else ""
        if en_text:
            dialogue = en_text
            source = "loc"
        else:
            dialogue = inline_text
            source = "inline"

        records.append(NpcGiftDataRecord(
            npc_id=npc_id,
            npc_name=npc_name,
            unknown_param=unknown_param,
            dialogue=dialogue,
            dialogue_source=source,
        ))

    return records
