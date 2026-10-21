# `npcgift.dbss` Format

## Purpose

The gift items of the in-game "Give Gift" interaction: per NPC, the accepted gift item IDs and the Amity gained for each. The NPC's reply to a confession is in [`npcgiftdata.dbss`](npcgiftdata_dbss.md), keyed by the same NPC IDs.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ---------------------------- | --------- |
| 1      | 1485 and later | 3474    | `npcgift.dbss`       | 1,552 | 117 Gift Row, 24 Gift Record | 12        |
| 1      | 1485 and later | 3474    | `npcgiftoffset.dbss` | 244   | 24 Offset Record             | 10        |

| Layout | File                 | Known            | Unknown      |
| ------ | -------------------- | ---------------- | ------------ |
| 1      | `npcgift.dbss`       | 1,552 B (100.0%) | 0 B (0.0%)   |
| 1      | `npcgiftoffset.dbss` | 196 B (80.3%)    | 48 B (19.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                        |
| --------------------- | -------- | ------------------------------------------- |
| `languagedata_en.loc` | Optional | NPC names (6), item names (0)               |

`npcgiftoffset.dbss` is the ID-keyed index into this file (below).
`npcgiftetc.bss` holds the global gift-system values, see
[npcgiftetc_bss.md](npcgiftetc_bss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field   | Notes                                     |
| ------- | ------------------ | ------- | ----------------------------------------- |
| `+0x00` | u32                | count   | Number of NPC gift records (observed: 24) |
| `+0x04` | Gift Record[count] | records | See Gift Record                           |

### Gift Record (variable: 6 bytes + gift rows)

| Offset  | Type                 | Field      | Notes                            |
| ------- | -------------------- | ---------- | -------------------------------- |
| `+0x00` | u16                  | npc_id     | NPC key                          |
| `+0x02` | u32                  | gift_count | Number of gift rows              |
| `+0x06` | Gift Row[gift_count] | gifts      | `gift_count` rows, 12 bytes each |

Observed `gift_count` values: in the pre-2026-09-27 fixture 23 records have 5 rows and NPC 41002 has 4 (119 gift rows); in the 2026-09-27 client 22 have 5, NPC 43408 has 4 and NPC 41002 has 3 (117 gift rows). The companion `data_size` equals `4 + gift_count * 12`.

### Gift Row (12 bytes)

| Offset  | Type | Field   | Notes                                                              |
| ------- | ---- | ------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_id | Gift item ID; matches item LOC type 0 names                        |
| `+0x04` | u32  | amity_a | Amity gained by giving this item                                   |
| `+0x08` | u32  | amity_b | Duplicate Amity value; equal to `amity_a` on every observed row (119 pre-2026-09-27, 117 in the 2026-09-27 client) |

### `npcgiftoffset.dbss`

| Offset  | Type                 | Field   | Notes                                     |
| ------- | -------------------- | ------- | ----------------------------------------- |
| `+0x00` | u32                  | count   | Number of NPC gift records (observed: 24) |
| `+0x04` | Offset Record[count] | records | See Offset Record                         |

### Offset Record (10 bytes)

| Offset  | Type | Field       | Notes                                                                 |
| ------- | ---- | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | npc_id      | NPC key; matches the record's leading `npc_id`                        |
| `+0x02` | u32  | data_offset | Byte offset into `npcgift.dbss`; points 2 bytes past the record start |
| `+0x06` | u16  | data_size   | Byte count after the leading `npc_id`                                 |
| `+0x08` | u16  | unknown_08  | Observed: 0                                                           |

`record_start = data_offset - 2`

## Notes

- `npcgift.dbss` and [`npcgiftdata.dbss`](npcgiftdata_dbss.md) share the same 24 NPC IDs and offset record order, but the main records are not stored in ID-sorted order.
- `item_id` is ambiguous across LOC types; use str_type=0 for item display names, not str_type=34 knowledge names.
- Example: NPC 40012 (Crio) accepts item 7023, which resolves via str_type=0 to "Haystack" and via str_type=34 to "Omelet". Use str_type=0 for gift item names.
- `npc_id` resolves via LOC str_type=32, str_id4=29 for the "Give Gift" interaction label.
