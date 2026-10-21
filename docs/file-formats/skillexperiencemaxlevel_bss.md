# `skillexperiencemaxlevel.bss` Format

## Purpose

Max level of a skill point EXP table. `skillexperiencemaxlevel.bss` holds the top level of [skillexperience](skillexperience_dbss.md) (combat skill points) and `guildskillexperiencemaxlevel.bss` the top level of [guildskillexperience](guildskillexperience_dbss.md) (guild points). Both files share this layout and one handler class. On client 3464 they hold `2000` and `1000`, the last row of each EXP table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ----- | ------- | --------- |
| 1      | 1230 and later | 3474    | `guildskillexperiencemaxlevel.bss` | 18    | -       | -         |
| 1      | 1230 and later | 3474    | `skillexperiencemaxlevel.bss`      | 18    | -       | -         |

| Layout | File                               | Known         | Unknown    |
| ------ | ---------------------------------- | ------------- | ---------- |
| 1      | `guildskillexperiencemaxlevel.bss` | 18 B (100.0%) | 0 B (0.0%) |
| 1      | `skillexperiencemaxlevel.bss`      | 18 B (100.0%) | 0 B (0.0%) |

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
| 1230   | Layout 1 |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

`PABR` magic, a bare u16 array with no count, then the 12-byte PABR trailer. 18 bytes on client 3464 (one value).

| Offset     | Type       | Field        | Notes                                        |
| ---------- | ---------- | ------------ | -------------------------------------------- |
| `+0x00`    | char[4]    | magic        | `PABR` (ASCII)                               |
| `+0x04`    | u16[..end_of_data] | max_level | One value on client 3464; runs up to `end_of_data` |
| `EOF-0x0C` | u32        | string_count | `0`: the PABR string table, here with no strings |
| `EOF-0x08` | u32        | end_of_data  | `6`; byte offset right after the last `max_level` |
| `EOF-0x04` | u32        | zero         | `0`                                          |

The array length is not stored; the parser takes it from the trailer's `end_of_data`: `(end_of_data - 4) / 2` values.

The same trailer closes [fitnessmaxlevel](fitnessmaxlevel_bss.md), which stores u32 values instead.

## Notes

- `end_of_data` is `6` in both files, so the value is a u16, not the u32 that the first 8 bytes suggest (`d0 07 00 00`): the next two zero bytes start the trailer.
- The life skill point table [productexperience](productexperience_dbss.md) has no max level file.
