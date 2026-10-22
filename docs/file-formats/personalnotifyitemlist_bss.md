# `personalnotifyitemlist.bss` Format

## Purpose

A list of item IDs in ascending order: 24,433 of the 70,826 items of
client 3482. Every entry is an item with a record in `itemenchant.dbss`.
No Lua file of client 3482 names the list, and what the client notifies
about these items is open.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ------ | -------------- | --------- |
| 1      | 1937 and later | 3482    | `personalnotifyitemlist.bss` | 97,752 | 1 String Table | 4         |

| Layout | File                         | Known             | Unknown    |
| ------ | ---------------------------- | ----------------- | ---------- |
| 1      | `personalnotifyitemlist.bss` | 97,752 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                |
| --------------------- | -------- | ------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of u32 rows with an empty string table, read by
`u32_rows()` in `_common/pabr_strings.py`.

| Offset              | Type         | Field        | Notes                                             |
| ------------------- | ------------ | ------------ | ------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | `PABR`                                            |
| `+0x04`             | u32          | count        | Number of items                                   |
| `+0x08`             | u32[count]   | item_ids     | Item IDs (LOC type 0 names), ascending and unique |
| `item_ids+0x00`     | String Table | string_table | Empty string table                                |
| `string_table+0x00` | u32          | table_start  | End of the rows (`8 + 4 * count`)                 |
| `string_table+0x04` | u32          | zero         | `0`                                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Notes

- The list starts with the gold bars (`2` to `5`). Among the lowest item
  IDs it leaves out silver (`1`), Pearls (`6`), Mileage (`7`) and the
  skill and life EXP items from `51` to `92`.
- The file is not in client 1784.

## Open Questions

### What the List Selects

Which items the list holds, and what the client does with them, is not
in the Lua. The name reads as a personal notice when the item is
obtained; nothing in the item records of client 3482 has been matched to
the list yet.
