# `npcgift.dbss` Format

## Purpose

The gift items of the in-game "Give Gift" interaction: per NPC, the accepted gift item IDs and the Amity gained for each. The NPC's reply to a confession is in [`npcgiftdata.dbss`](npcgiftdata_dbss.md), keyed by the same NPC IDs.

Example:

```text
NPC: Crio (40012)  →  item: 7023 (Haystack)  →  amity: 40
```

## Companion Files

| File                  | Required | Role                                        |
| --------------------- | -------- | ------------------------------------------- |
| `languagedata_en.loc` | Optional | NPC names (6), item names (0)               |

`npcgiftoffset.dbss` is the ID-keyed index into this file (below).
`npcgiftetc.bss` holds the global gift-system values, see
[npcgiftetc_bss.md](npcgiftetc_bss.md).

All multi-byte values are little-endian.

## File Layout

### npcgiftoffset.dbss

#### Header (4 bytes)

| Offset  | Type | Field | Notes                                     |
| ------- | ---- | ----- | ----------------------------------------- |
| `+0x00` | u32  | count | Number of NPC gift records (observed: 24) |

#### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                                 |
| ------- | ---- | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | npc_id      | NPC key; matches the record's leading `npc_id`                        |
| `+0x02` | u32  | data_offset | Byte offset into `npcgift.dbss`; points 2 bytes past the record start |
| `+0x06` | u16  | data_size   | Byte count after the leading `npc_id`                                 |
| `+0x08` | u16  | padding     | Observed: 0                                                           |

`record_start = data_offset - 2`

### npcgift.dbss

#### Header (4 bytes)

| Offset  | Type | Field | Notes                                     |
| ------- | ---- | ----- | ----------------------------------------- |
| `+0x00` | u32  | count | Number of NPC gift records (observed: 24) |

#### Gift Record (variable length)

| Offset  | Type       | Field      | Notes                            |
| ------- | ---------- | ---------- | -------------------------------- |
| `+0x00` | u16        | npc_id     | NPC key                          |
| `+0x02` | u32        | gift_count | Number of gift rows              |
| `+0x06` | Gift Row[] | gifts      | `gift_count` rows, 12 bytes each |

Observed `gift_count` values: in the pre-2026-09-27 fixture 23 records have 5 rows and NPC 41002 has 4 (119 gift rows); in the 2026-09-27 client 22 have 5, NPC 43408 has 4 and NPC 41002 has 3 (117 gift rows). The companion `data_size` equals `4 + gift_count * 12`.

#### Gift Row (12 bytes)

| Offset  | Type | Field   | Notes                                                              |
| ------- | ---- | ------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_id | Gift item ID; matches item LOC type 0 names                        |
| `+0x04` | u32  | amity_a | Amity gained by giving this item                                   |
| `+0x08` | u32  | amity_b | Duplicate Amity value; equal to `amity_a` on every observed row (119 pre-2026-09-27, 117 in the 2026-09-27 client) |

## Suggested UI Layout

| Column    | Type | Notes                                                |
| --------- | ---- | ---------------------------------------------------- |
| NPC ID    | num  | `npc_id`                                              |
| NPC Name  | text | LOC str_type=6, str_id1=npc_id                        |
| Item ID   | num  | `item_id`                                             |
| Icon      | text | Item icon from the item icon index                    |
| Item Name | text | LOC str_type=0, str_id1=item_id, in its grade colour (`ITEM_GRADE`) |
| Amity     | num  | `amity_a`; `amity_b` is a duplicate in observed data  |

All 110 distinct gift items resolve an icon through the item icon index
(`_common/icon_index.py`), including those whose icon file is named after the
asset, not the ID (item 24626 is
`ui_texture/icon/new_icon/03_etc/06_housing/inhouse_cultivate_sea_clam_01_wall.dds`).

## Notes

- `npcgift.dbss` and [`npcgiftdata.dbss`](npcgiftdata_dbss.md) share the same 24 NPC IDs and offset record order, but the main records are not stored in ID-sorted order.
- `item_id` is ambiguous across LOC types; use str_type=0 for item display names, not str_type=34 knowledge names.
- Example: NPC 40012 (Crio) accepts item 7023, which resolves via str_type=0 to "Haystack" and via str_type=34 to "Omelet". Use str_type=0 for gift item names.
- `npc_id` resolves via LOC str_type=32, str_id4=29 for the "Give Gift" interaction label.
