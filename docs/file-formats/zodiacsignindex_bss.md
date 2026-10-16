# `zodiacsignindex.bss` Format

## Purpose

Lists zodiac sign IDs in display/index order. The file is a compact `PABR` lookup table for the 12 horoscope signs defined by `zodiacsign.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                   |
| --------------------- | -------- | -------------------------------------- |
| `zodiacsign.dbss`     | Required | Resolves each `zodiac_id` to sign data |
| `languagedata_en.loc` | Optional | English names for display              |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field          | Notes                                                  |
| ------------------- | ------------ | -------------- | ------------------------------------------------------ |
| `+0x00`             | char[4]      | magic          | ASCII `PABR`                                           |
| `+0x04`             | u32          | count          | Number of entries; observed 12                         |
| `+0x08`             | Entry[count] | entries        | See Entry                                              |
| `entries+0x00`      | String Table | string_table   | The PABR string table, here with no strings            |
| `string_table+0x00` | u32          | end_of_entries | Byte offset immediately after entries; observed `0x14` |
| `string_table+0x04` | u32          | zero           | Always 0                                               |

### Entry (1 byte)

| Offset  | Type | Field     | Notes                                                       |
| ------- | ---- | --------- | ----------------------------------------------------------- |
| `+0x00` | u8   | zodiac_id | The 1-based ID into `zodiacsign.dbss`; observed 1-12        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes    |
| ------- | ------------------ | ------------ | -------- |
| `+0x00` | u32                | string_count | Always 0 |
| `+0x04` | pstr[string_count] | strings      | Empty    |

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

## Notes

- File size is 32 bytes: 8-byte header, 12 one-byte entries, and 12-byte trailer.
- Entry IDs match `zodiacsignoffset.dbss` exactly: `1..12`.
- `end_of_entries` is `20` decimal (`0x14`), equal to `8 + count`.
- Existing `zodiacsign.dbss` parsing does not require this file because the main and offset files already store the same zodiac IDs.
