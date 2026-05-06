# `zodiacsignindex.bss` Format

## Purpose

Lists zodiac sign IDs in display/index order. The file is a compact `PABR` lookup table for the 12 horoscope signs defined by `zodiacsign.dbss`.

Example:

```text
slot 0 -> zodiac_id 1 -> Hammer
slot 11 -> zodiac_id 12 -> Goblin
```

## Graph

### Tags

- file format
- bss
- zodiac
- index

### Connections

- [zodiacsign.dbss](zodiacsign_dbss.md) - zodiac sign definitions, names, star coordinates, and texture paths
- [zodiacsignoffset.dbss](zodiacsign_dbss.md#zodiacsignoffsetdbss) - confirms same 12 zodiac IDs in the same order
- [languagedata_en.loc](languagedata_loc.md) - English sign names for display

---

## Companion Files

| File                  | Required | Role                                   |
| --------------------- | -------- | -------------------------------------- |
| `zodiacsign.dbss`     | Required | Resolves each `zodiac_id` to sign data |
| `languagedata_en.loc` | Optional | English names for display              |

All multi-byte values are little-endian.

---

## File Layout

### Header (8 bytes)

| Offset  | Type  | Field | Notes                          |
| ------- | ----- | ----- | ------------------------------ |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)                 |
| `+0x04` | u32   | count | Number of entries; observed 12 |

### Entry (1 byte, repeated `count` times)

| Offset  | Type | Field     | Notes                                            |
| ------- | ---- | --------- | ------------------------------------------------ |
| `+0x00` | u8   | zodiac_id | 1-based ID into `zodiacsign.dbss`; observed 1-12 |

### Trailer (12 bytes)

Follows the last entry.

| Offset  | Type | Field          | Notes                                                  |
| ------- | ---- | -------------- | ------------------------------------------------------ |
| `+0x00` | u32  | reserved_a     | Always 0                                               |
| `+0x04` | u32  | end_of_entries | Byte offset immediately after entries; observed `0x14` |
| `+0x08` | u32  | reserved_b     | Always 0                                               |

---

## Reference Table

| Slot | Zodiac ID | English Name  |
| ---- | --------- | ------------- |
| 0    | 1         | Hammer        |
| 1    | 2         | Boat          |
| 2    | 3         | Shield        |
| 3    | 4         | Giant         |
| 4    | 5         | Camel         |
| 5    | 6         | Black Dragon  |
| 6    | 7         | Treant Owl    |
| 7    | 8         | Elephant      |
| 8    | 9         | Key           |
| 9    | 10        | Wagon         |
| 10   | 11        | Sealing Stone |
| 11   | 12        | Goblin        |

---

## Suggested UI Layout

| Column    | Type | Notes                                               |
| --------- | ---- | --------------------------------------------------- |
| Zodiac ID | num  | `zodiac_id`                                         |
| Name      | text | Prefer LOC str_type=7, str_id1=zodiac_id, str_id4=0 |

---

## Notes

- File size is 32 bytes: 8-byte header, 12 one-byte entries, and 12-byte trailer.
- Entry IDs match `zodiacsignoffset.dbss` exactly: `1..12`.
- `end_of_entries` is `20` decimal (`0x14`), equal to `8 + count`.
- Existing `zodiacsign.dbss` parsing does not require this file because the main and offset files already store the same zodiac IDs.
