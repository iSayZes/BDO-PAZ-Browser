# `zodiacsignorder.dbss` Format

## Purpose

The order in which the stars of a zodiac constellation light up, per
personality type: 2 variants x 12 signs = 24 records. The stars are the
`star_positions` of [`zodiacsign.dbss`](zodiacsign_dbss.md), and
`personality_type` is the one `npcpersonality.dbss` uses.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                          |
| ---------------------------- | -------- | --------------------------------------------- |
| `zodiacsignorderoffset.dbss` | Required | ID-keyed index into this file, see below      |
| `languagedata_en.loc`        | Optional | Zodiac sign names (7)                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The records are back to back, but not in the order of the offset file; use
the offset file to find a record by key.

| Offset  | Type          | Field   | Notes                    |
| ------- | ------------- | ------- | ------------------------ |
| `+0x00` | u32           | count   | Number of records (= 24) |
| `+0x04` | Record[count] | records | See Record               |

### Record (variable: 13 bytes + trigger_order)

23 to 29 bytes on client 3473 (5 to 8 stars); the offset row's `data_size`
leaves out the leading `personality_type`.

| Offset               | Type               | Field                | Notes                                      |
| -------------------- | ------------------ | -------------------- | ------------------------------------------ |
| `+0x00`              | u16                | personality_type     | `major × 100 + variant`; range 101 to 1202 |
| `+0x02`              | u32                | trigger_count        | Number of `trigger_order` values           |
| `+0x06`              | u32                | unknown_06           | Always 0                                   |
| `+0x0A`              | u16[trigger_count] | trigger_order        | 0-indexed star slots, in lighting order    |
| `trigger_order+0x00` | u8                 | zodiac_id            | Which zodiac sign (1 to 12)                |
| `trigger_order+0x01` | u16                | personality_type_dup | Duplicate of `personality_type` at `+0x00` |

The first star is stored like the others. It is not always slot 0: on
client 3464, 7 of the 24 records start elsewhere (902, 102, 1002, 202, 302,
1202, 502).

`slots` = `zodiacsign.float_count` for that `zodiac_id`.

### `zodiacsignorderoffset.dbss`

| Offset  | Type                 | Field | Notes                         |
| ------- | -------------------- | ----- | ----------------------------- |
| `+0x00` | u32                  | count | Number of rows (= 24)         |
| `+0x04` | Offset Record[count] | rows  | See Offset Record             |

### Offset Record (10 bytes)

| Offset  | Type | Field            | Notes                                                              |
| ------- | ---- | ---------------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | personality_type | Matches `personality_type` in the main record                      |
| `+0x02` | u32  | data_offset      | Byte offset into `zodiacsignorder.dbss`; 2 bytes past record start |
| `+0x06` | u16  | data_size        | Size of record data (excluding leading `personality_type` u16)     |
| `+0x08` | u16  | unknown_08       | Always 0                                                           |

`record_start = data_offset - 2`

## Notes

- Variant 2 is a second drawing order for the same stars. It can reverse variant 1 (1001 is `0,1,2,3,4`, 1002 is `4,3,2,1,0`) or reorder it (902 is `2,1,0,3,2,1`).
- Major 9 (Key): only `personality_type` 901 exists in `npcpersonality.dbss`, but `zodiacsignorder.dbss` defines both 901 and 902.
