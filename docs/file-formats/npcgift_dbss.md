# npcgift.dbss + npcgiftdata.dbss

Defines the NPC gift/confession data used by the "Give Gift" interaction. The
main file maps NPC IDs to accepted gift item IDs and the Amity gained for each
gift. The data file maps the same NPC IDs to Korean confession-response
dialogue text.

Companion files:

- `npcgiftoffset.dbss` — ID-keyed index into `npcgift.dbss`.
- `npcgiftdataoffset.dbss` — ID-keyed index into `npcgiftdata.dbss`.
- `npcgiftetc.bss` — small PABR config block with global gift-system values.

All multi-byte values are little-endian.

## npcgiftoffset.dbss

### Header (4 bytes)

| Offset | Type | Field | Notes                                     |
| ------ | ---- | ----- | ----------------------------------------- |
| 0x00   | u32  | count | Number of NPC gift records (observed: 24) |

### Offset Record (10 bytes, repeated `count` times)

| Offset | Type | Field       | Notes                                                                 |
| ------ | ---- | ----------- | --------------------------------------------------------------------- |
| 0x00   | u16  | npc_id      | NPC key; matches the record's leading `npc_id`                        |
| 0x02   | u32  | data_offset | Byte offset into `npcgift.dbss`; points 2 bytes past the record start |
| 0x06   | u16  | data_size   | Byte count after the leading `npc_id`                                 |
| 0x08   | u16  | padding     | Observed: 0                                                           |

To locate a record in `npcgift.dbss`: `record_start = data_offset - 2`.

## npcgift.dbss

### Header (4 bytes)

| Offset | Type | Field | Notes                                     |
| ------ | ---- | ----- | ----------------------------------------- |
| 0x00   | u32  | count | Number of NPC gift records (observed: 24) |

### Gift Record (variable length)

| Offset | Type       | Field      | Notes                            |
| ------ | ---------- | ---------- | -------------------------------- |
| 0x00   | u16        | npc_id     | NPC key                          |
| 0x02   | u32        | gift_count | Number of gift rows              |
| 0x06   | Gift Row[] | gifts      | `gift_count` rows, 12 bytes each |

Observed `gift_count` values: 23 records have 5 rows; NPC 41002 has 4 rows.
The companion `data_size` equals `4 + gift_count * 12`.

### Gift Row (12 bytes)

| Offset | Type | Field   | Notes                                                              |
| ------ | ---- | ------- | ------------------------------------------------------------------ |
| 0x00   | u32  | item_id | Gift item ID; matches item LOC type 0 names                        |
| 0x04   | u32  | amity_a | Amity gained by giving this item                                   |
| 0x08   | u32  | amity_b | Duplicate Amity value; equal to `amity_a` in all 119 observed rows |

Example: NPC 40012 (Crio) accepts item 7023, which resolves through LOC type 0
to "Haystack", and the same ID resolves through LOC type 34 to the knowledge
entry "Omelet". Use LOC type 0 when displaying gift item names.

## npcgiftdataoffset.dbss

Same 4-byte header and 10-byte offset record layout as `npcgiftoffset.dbss`,
but offsets point into `npcgiftdata.dbss`.

## npcgiftdata.dbss

### Header (4 bytes)

| Offset | Type | Field | Notes                                     |
| ------ | ---- | ----- | ----------------------------------------- |
| 0x00   | u32  | count | Number of dialogue records (observed: 24) |

### Dialogue Record (variable length)

| Offset | Type              | Field         | Notes                                                                                                                        |
| ------ | ----------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 0x00   | u16               | npc_id        | NPC key                                                                                                                      |
| 0x02   | u32               | unknown_param | Observed: 70 for 23 records, 35 for NPC 43408. This is not the LOC type.                                                     |
| 0x06   | u32               | text_len      | Number of visible UTF-16 code units in `text`                                                                                |
| 0x0A   | u32               | zero          | Observed: 0                                                                                                                  |
| 0x0E   | utf16le[text_len] | text          | Korean confession-response dialogue                                                                                          |
| varies | u16[2]            | tail          | Two trailing code units after `text`; observed values include `00 00 00 00`, `FF FF FF FF`, `00 00 41 DF`, and `00 00 3D E6` |

The companion `data_size` equals `12 + text_len * 2 + 4`, excluding the leading
`npc_id`. English localized equivalents are present in LOC type 54 keyed by the
same `npc_id`; for example, LOC type 54 / ID 43431 matches the Brego Williar
confession-response text.

## npcgiftetc.bss

Small PABR config block (32 bytes):

| Offset | Type    | Field     | Observed |
| ------ | ------- | --------- | -------- |
| 0x00   | char[4] | magic     | `PABR`   |
| 0x04   | u16     | unknown_a | 5        |
| 0x06   | u16     | unknown_b | 5        |
| 0x08   | u32     | unknown_c | 1000     |
| 0x0C   | u32     | unknown_d | 50000000 |
| 0x10   | u32     | unknown_e | 0        |
| 0x14   | u32     | unknown_f | 0        |
| 0x18   | u32     | unknown_g | 20       |
| 0x1C   | u32     | unknown_h | 0        |

## Suggested UI Layout

### npcgift.dbss

| Column    | Type | Notes                                                |
| --------- | ---- | ---------------------------------------------------- |
| NPC ID    | num  | `npc_id`                                             |
| NPC Name  | text | LOC type 6 / `npc_id`                                |
| Item ID   | num  | `item_id`                                            |
| Item Name | text | LOC type 0 / `item_id`                               |
| Amity     | num  | `amity_a`; `amity_b` is a duplicate in observed data |

### npcgiftdata.dbss

| Column        | Type | Notes                                                              |
| ------------- | ---- | ------------------------------------------------------------------ |
| NPC ID        | num  | `npc_id`                                                           |
| NPC Name      | text | LOC type 6 / `npc_id`                                              |
| Unknown Param | num  | `unknown_param`                                                    |
| Dialogue      | text | English LOC type 54 when available; Korean inline text as fallback |

## Notes

- `npcgift.dbss` and `npcgiftdata.dbss` share the same 24 NPC IDs and offset
  record order, but the main records are not stored in ID-sorted order.
- `npc_id` resolves through LOC type 6 for NPC names and LOC type 32 / ID4 29
  for the "Give Gift" interaction label.
- `item_id` is ambiguous across LOC types; use LOC type 0 for item display
  names, not type 34 knowledge names.
- The meaning of `unknown_param` in `npcgiftdata.dbss` and the trailing two
  UTF-16 code units after dialogue text is not yet known.
