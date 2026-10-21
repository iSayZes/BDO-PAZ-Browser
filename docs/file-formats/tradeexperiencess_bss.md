# `tradeexperiencess.bss` Format

## Purpose

A list of 180 u64 values after a u32 count, with no `PABR` magic and no
string table. The name points at trade (Trading life skill) experience, and
180 is the life skill max level of
[`lifeexpmaxlevel.bss`](lifeexpmaxlevel_bss.md), but what each value means
is open (see Open Questions). The file is not in clients 1784 to 3251.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 1      | 3474 and later | 3474    | `tradeexperiencess.bss` | 1,444 | 180 Row | 8         |

| Layout | File                    | Known      | Unknown         |
| ------ | ----------------------- | ---------- | --------------- |
| 1      | `tradeexperiencess.bss` | 4 B (0.3%) | 1,440 B (99.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | No file  |
| 3002   | No file  |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 180 x 8 = 1,444 bytes.

### Row (8 bytes)

| Offset  | Type | Field      | Notes                                                       |
| ------- | ---- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u64  | unknown_00 | `1` to `100308581`; the high u32 is `0` on every row (client 3474) |

## Notes

- The values on client 3474, by row index from 0: `1`, `1`, `2`, `5`,
  `16`, `43`, `91` and up to `210540` at row 45, then a steep rise to the
  largest value, `100308581`, at row 60. From there each value is about
  0.72 to 0.77 times the one before, down to `1023` at row 99, then `34`
  less per row to `3` at row 129, and `3` on rows 129 to 179.
- The values do not follow the Trading row of
  [`lifeexp.dbss`](lifeexp_dbss.md): that row rises on every level, this
  table falls after row 60.
- No client Lua names the table or calls a getter for it, and the client
  1784 sheets have no sheet of this name; the closest column there is
  `TradeExperiencePerDistance` of `EtcOption`, a single value.

## Open Questions

### What unknown_00 Holds

One value per row, 180 rows, bell-shaped over the row index with its peak at
row 60. Whether the row index is a Trading level (0 to 179) and the value an
EXP amount, a divisor or a weight is not known. No handler shows the file
until the value has a name.
