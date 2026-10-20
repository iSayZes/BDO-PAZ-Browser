# `itemimprovementdefaultdisplaylist.bss` Format

## Purpose

The reform stones the Gear Reform window lists by default, in order. Each
entry is a stone item ID of
[`itemimprovementsource.dbss`](itemimprovementsource_dbss.md); the window
loads them through `ToClient_GetImprovementSourceItemCount()` and
`ToClient_GetDefaultDisplayImprovementSourceItemByIndex(index)`
(`panel_improvement_all_1`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `itemimprovementdefaultdisplaylist.bss` | 116   | 1 String Table | 4         |

| Layout | File                                    | Known          | Unknown    |
| ------ | --------------------------------------- | -------------- | ---------- |
| 1      | `itemimprovementdefaultdisplaylist.bss` | 116 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. The stone records are in [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of u32 rows with an empty string table, read by
`u32_rows()` in `_common/pabr_strings.py`.

| Offset              | Type         | Field        | Notes                                                       |
| ------------------- | ------------ | ------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | `PABR`                                                      |
| `+0x04`             | u32          | count        | Number of stones; `24` on client 3464                       |
| `+0x08`             | u32[count]   | item_ids     | `count` stone item IDs                                      |
| `item_ids+0x00`     | String Table | string_table | Empty string table                                          |
| `string_table+0x00` | u32          | table_start  | End of the rows (`8 + 4 * count`)                           |
| `string_table+0x04` | u32          | zero         | `0`                                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Notes

- On client 3464 the 24 stones are exactly the `itemimprovementsource.dbss`
  records with `is_default_display = 1`.
