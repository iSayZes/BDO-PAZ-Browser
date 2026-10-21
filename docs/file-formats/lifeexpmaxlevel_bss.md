# `lifeexpmaxlevel.bss` Format

## Purpose

Max level of every life skill. Value N is the max level of life skill N, numbered as in the Life Skills table of [lifeexp](lifeexp_dbss.md). On client 3464 all 15 values are `180` (Guru 100), and each `lifeexp.dbss` block ends on that level (181 rows for levels 0 to 180).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------- | --------- |
| 1      | 1485 and later | 3474    | `lifeexpmaxlevel.bss` | 60    | -       | -         |

| Layout | File                  | Known         | Unknown    |
| ------ | --------------------- | ------------- | ---------- |
| 1      | `lifeexpmaxlevel.bss` | 60 B (100.0%) | 0 B (0.0%) |

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
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File              | Required | Role                                                                |
| ----------------- | -------- | ------------------------------------------------------------------- |
| `stringtable.bss` | Optional | Hashes of the `GAME` sheet keys that name the life skills and ranks |

The life skill names and rank groups are the ones in [lifeexp](lifeexp_dbss.md); the handler imports them from `_dbss/lifeexp/labels.py`.

All multi-byte values are little-endian.

## Layout 1

### File Layout

A bare array of u32 values with no header and no `PABR` magic. 60 bytes on client 3464, one value per `lifeexp.dbss` block.

| Offset  | Type       | Field     | Notes                                                        |
| ------- | ---------- | --------- | ------------------------------------------------------------ |
| `+0x00` | u32[..end] | max_level | Max level of life skill N at `+N x 4`; runs to the end of the file |

## Notes

- Trading (7) gets `180` here although `lifeexp.dbss` holds finite EXP for it only up to level 60; see the [lifeexp](lifeexp_dbss.md) Notes.
- `fitnessmaxlevel.bss` is the matching file for `fitnesslevel.dbss` but has `PABR` magic and a different layout; see [fitnessmaxlevel](fitnessmaxlevel_bss.md).
