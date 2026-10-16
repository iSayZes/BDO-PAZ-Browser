# `fitnessmaxlevel.bss` Format

## Purpose

Max level of every fitness stat. Value N is the max level of fitness type N, numbered as in the Fitness Type table of [fitnesslevel](fitnesslevel_dbss.md) (`0` Breath, `1` Strength, `2` Health). On client 3464 all three values are `50`, and each `fitnesslevel.dbss` block ends on that level (51 rows for levels 0 to 50).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------- | --------- |
| 1      | 3473 and later | 3473    | `fitnessmaxlevel.bss` | 28    | -       | -         |

| Layout | File                  | Known         | Unknown    |
| ------ | --------------------- | ------------- | ---------- |
| 1      | `fitnessmaxlevel.bss` | 28 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. The fitness type names come from `_dbss/fitnesslevel/labels.py` (see Notes).

All multi-byte values are little-endian.

## Layout 1

### File Layout

`PABR` magic, a bare u32 array with no count, then the 12-byte PABR trailer (the last three rows). 28 bytes on client 3464.

| Offset     | Type       | Field     | Notes                                                    |
| ---------- | ---------- | --------- | -------------------------------------------------------- |
| `+0x00`    | char[4]    | magic     | `PABR` (ASCII)                                           |
| `+0x04`    | u32[..end_of_data] | max_level | One per fitness type; value N is the max level of type N; runs up to `end_of_data` |
| `EOF-0x0C` | u32        | string_count | `0`: the empty PABR string table                      |
| `EOF-0x08` | u32        | end_of_data | `16`; byte offset right after the last `max_level`     |
| `EOF-0x04` | u32        | zero      | `0`                                                      |

The array length is not stored; the parser takes it from the trailer's `end_of_data`: `(end_of_data - 4) / 4` values.

The same trailer closes `acceptquest.bss` and the PABR offset files.

## Notes

- The fitness type names are the ones in [fitnesslevel](fitnesslevel_dbss.md); both handlers read them through `_dbss/fitnesslevel/labels.py`.
- Level 30 is the soft cap and this file does not store it. It shows only in the EXP column of `fitnesslevel.dbss`; see the [fitnesslevel](fitnesslevel_dbss.md) Notes.
- `lifeexpmaxlevel.bss` is the life skill counterpart, a bare u32 array with no magic and no trailer; see [lifeexpmaxlevel](lifeexpmaxlevel_bss.md).
- `skillexperiencemaxlevel.bss` and `guildskillexperiencemaxlevel.bss` (18 bytes each) use the same magic and trailer around a u16 array (`2000` and `1000`, trailer `end_of_data` `6`); see [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md).
