# `npcgift.dbss` Format

## Purpose

Defines the NPC gift/confession data used by the in-game "Give Gift" interaction. The main file maps NPC IDs to accepted gift item IDs and the Amity gained for each gift. The data file maps the same NPC IDs to Korean confession-response dialogue text.

Example:

```text
NPC: Crio (40012)  →  item: 7023 (Haystack)  →  amity: 30
Confession response: "감사합니다! 정말 좋아해요."
```

## Graph

### Tags

- file format
- dbss
- npc
- amity
- gift

### Connections

- [languagedata_en.loc](languagedata_loc.md) — NPC names (str_type=6), item names (str_type=0), English dialogue (str_type=54)

---

## Companion Files

| File                     | Required | Role                                                   |
| ------------------------ | -------- | ------------------------------------------------------ |
| `npcgiftoffset.dbss`     | Required | ID-keyed index into `npcgift.dbss`                     |
| `npcgiftdataoffset.dbss` | Required | ID-keyed index into `npcgiftdata.dbss`                 |
| `npcgiftetc.bss`         | Optional | Small PABR config block with global gift-system values |

All multi-byte values are little-endian.

---

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

---

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

Observed `gift_count` values: 23 records have 5 rows; NPC 41002 has 4 rows. The companion `data_size` equals `4 + gift_count * 12`.

#### Gift Row (12 bytes)

| Offset  | Type | Field   | Notes                                                              |
| ------- | ---- | ------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_id | Gift item ID; matches item LOC type 0 names                        |
| `+0x04` | u32  | amity_a | Amity gained by giving this item                                   |
| `+0x08` | u32  | amity_b | Duplicate Amity value; equal to `amity_a` in all 119 observed rows |

---

### npcgiftdataoffset.dbss

Same 4-byte header and 10-byte offset record layout as `npcgiftoffset.dbss`, but offsets point into `npcgiftdata.dbss`.

---

### npcgiftdata.dbss

#### Header (4 bytes)

| Offset  | Type | Field | Notes                                     |
| ------- | ---- | ----- | ----------------------------------------- |
| `+0x00` | u32  | count | Number of dialogue records (observed: 24) |

#### Dialogue Record (variable length)

| Offset  | Type              | Field         | Notes                                                                                                                        |
| ------- | ----------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `+0x00` | u16               | npc_id        | NPC key                                                                                                                      |
| `+0x02` | u32               | unknown_param | Observed: 70 for 23 records, 35 for NPC 43408. Not the LOC type.                                                             |
| `+0x06` | u32               | text_len      | Number of visible UTF-16 code units in `text`                                                                                |
| `+0x0A` | u32               | zero          | Observed: 0                                                                                                                  |
| `+0x0E` | utf16le[text_len] | text          | Korean confession-response dialogue                                                                                          |
| varies  | u16[2]            | tail          | Two trailing code units after `text`; observed values include `00 00 00 00`, `FF FF FF FF`, `00 00 41 DF`, and `00 00 3D E6` |

The companion `data_size` equals `12 + text_len * 2 + 4`, excluding the leading `npc_id`. English localized equivalents are in LOC type 54 keyed by the same `npc_id`.

---

### npcgiftetc.bss

Small PABR config block (32 bytes) with global gift-system values:

| Offset  | Type    | Field     | Observed |
| ------- | ------- | --------- | -------- |
| `+0x00` | char[4] | magic     | `PABR`   |
| `+0x04` | u16     | unknown_a | 5        |
| `+0x06` | u16     | unknown_b | 5        |
| `+0x08` | u32     | unknown_c | 1000     |
| `+0x0C` | u32     | unknown_d | 50000000 |
| `+0x10` | u32     | unknown_e | 0        |
| `+0x14` | u32     | unknown_f | 0        |
| `+0x18` | u32     | unknown_g | 20       |
| `+0x1C` | u32     | unknown_h | 0        |

---

## Suggested UI Layout

### npcgift.dbss

| Column    | Type | Notes                                                |
| --------- | ---- | ---------------------------------------------------- |
| NPC ID    | num  | `npc_id`                                             |
| NPC Name  | text | LOC str_type=6, str_id1=npc_id                       |
| Item ID   | num  | `item_id`                                            |
| Item Name | text | LOC str_type=0, str_id1=item_id                      |
| Amity     | num  | `amity_a`; `amity_b` is a duplicate in observed data |

### npcgiftdata.dbss

| Column        | Type | Notes                                                                  |
| ------------- | ---- | ---------------------------------------------------------------------- |
| NPC ID        | num  | `npc_id`                                                               |
| NPC Name      | text | LOC str_type=6, str_id1=npc_id                                         |
| Unknown Param | num  | `unknown_param`                                                        |
| Dialogue      | text | English LOC str_type=54 when available; Korean inline text as fallback |

---

## Notes

- `npcgift.dbss` and `npcgiftdata.dbss` share the same 24 NPC IDs and offset record order, but the main records are not stored in ID-sorted order.
- `item_id` is ambiguous across LOC types; use str_type=0 for item display names, not str_type=34 knowledge names.
- Example: NPC 40012 (Crio) accepts item 7023, which resolves via str_type=0 to "Haystack" and via str_type=34 to "Omelet". Use str_type=0 for gift item names.
- `npc_id` resolves via LOC str_type=32, str_id4=29 for the "Give Gift" interaction label.

---

## Open Questions

### unknown_param in npcgiftdata.dbss

The meaning of `unknown_param` (observed: 70 for 23 records, 35 for NPC 43408) is not known.

### Dialogue Tail Bytes

The two trailing UTF-16 code units after dialogue text (`tail`) carry values including `FF FF FF FF` and non-zero pairs; their purpose is unknown.
