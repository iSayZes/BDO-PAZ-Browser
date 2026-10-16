# `pcgrowthdefaultcharacterkey.bss` Format

## Purpose

An 18-byte PABR file holding one u16 character key, `47` on client 3464. It sits next to [pcgrowth](pcgrowth_dbss.md) and [pcgrowthsimply](pcgrowthsimply_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | -------------- | --------- |
| 1      | 1784 and later | 3473    | `pcgrowthdefaultcharacterkey.bss` | 18    | 1 String Table | 4         |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `pcgrowthdefaultcharacterkey.bss` | 18 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes               |
| ------------------- | ------------ | ------------------ | ------------------- |
| `+0x00`             | char[4]      | magic              | `PABR`              |
| `+0x04`             | u16          | character_key      | `47` on client 3464 |
| `+0x06`             | String Table | string_table       | See String Table    |
| `string_table+0x00` | u32          | string_table_start | `6`                 |
| `string_table+0x04` | u32          | zero               | `0`                 |

The string table starts at `+0x06`, so the rows end after the single u16.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Notes

- `47` is the character key of class type 46 (`PYFW5`, LOC type 6 `PYFW5`) in `pcgrowth.dbss`, and also the row count of `pcgrowth.dbss`, `pcgrowthoffset.dbss` and `pcgrowthsimply.bss`.
- On client 1784 the file holds `65050`, a key of that client's `characterstaticoffset.dbss`, while its `pcgrowthoffset.dbss` declares 82 rows. The value is a character key on both clients; the match with the class count on client 3464 does not hold on client 1784.
