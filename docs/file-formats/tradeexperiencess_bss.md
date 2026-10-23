# `tradeexperiencess.bss` Format

## Purpose

A list of 180 u64 values after a u32 count, with no `PABR` magic and no
string table. Row `r` lines up with Trading level `r + 1`: on levels 1 to
49 the Trading EXP of level `r + 1` in [`lifeexp.dbss`](lifeexp_dbss.md)
is a whole number of times the value of row `r` (see Rows and Trading
Levels). What one such part stands for is open (see Open Questions). The
file first ships in client 3473, the same client that replaced the Trading
EXP curve of `lifeexp.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 1      | 3473 and later | 3483    | `tradeexperiencess.bss` | 1,444 | 180 Row | 8         |

| Layout | File                    | Known      | Unknown         |
| ------ | ----------------------- | ---------- | --------------- |
| 1      | `tradeexperiencess.bss` | 4 B (0.3%) | 1,440 B (99.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3464   | No file  |
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

## Rows and Trading Levels

Counted on client 3473 against the Trading row of
[`lifeexp.dbss`](lifeexp_dbss.md) from the same client, where the row for
level `n` holds the EXP to go from `n` to `n + 1`:

| Trading levels | Rows      | Trading EXP of level `n` / row `n - 1`                                                                               |
| -------------- | --------- | -------------------------------------------------------------------------------------------------------------------- |
| 1 to 49        | 0 to 48   | A whole number `N` to within rounding, and the row is `round(EXP / N)`                                               |
| 50 to 61       | 49 to 60  | No whole number: 522.3 on level 50, then 1.3 times larger per level (1.385 from level 59 to 60), 9,969.2 on level 61 |
| 62 to 180      | 61 to 179 | No relation: the rows shrink, `lifeexp.dbss` keeps its sentinels                                                         |

`N` is 5, 5, 6, 9, 10, 11, 13, 16, 19 and 23 on Beginner 1 to 10, and
then grows by 4 to 22 per level up to 514 on level 49 (Artisan 9). On level 61,
the 9,969.2 divides the `999,999,999,999` sentinel that stops Trading at
Master 11.

Read this way, level 0 (20 EXP, no rank) has no row, row 60 is Master 11,
the highest level Trading can reach, and row 179 is Guru 100, the Trading
max level of [`lifeexpmaxlevel.bss`](lifeexpmaxlevel_bss.md).

## Notes

- The values on client 3474, by row index from 0: `1`, `1`, `2`, `5`,
  `16`, `43`, `91` and up to `210540` at row 45, then a steep rise to the
  largest value, `100308581`, at row 60. From there each value is about
  13/18 and 10/13 of the one before in turn (`72445086`, `55726989`,
  ...), down to `1023` at row 99, then `34` less per row to `3` at row
  129, and `3` on rows 129 to 179.
- The values are not EXP thresholds: they fall after row 60, and the
  per-level EXP of Trading is the `lifeexp.dbss` row.
- Client 3473 (2026-10-15 build) is the first client with the file; 3473,
  3474 and 3482 ship the same 1,444 bytes. Client 3464 (2026-10-08) has no
  such file, and its Trading row of `lifeexp.dbss` is the older curve
  (20 EXP for Beginner 1, 212,980,644 for level 60). Its level 4 needs 33
  EXP, 6.6 times row 3, so the whole-number fit holds only for the new
  curve.
- No client Lua of client 3482 names the table or calls a getter for it;
  the trade dialog Lua reads only `getLifeExperienceLevel` for item level
  requirements. The 2016 PDB has no trade experience struct; its only trade EXP members are
  `_tradeExp` of `ActionExpStaticStatus` and `_getSellingTradeExpRate` of
  `ItemTradeGroupValue`. The client 1784 sheets have no sheet of this name;
  the closest column there is `TradeExperiencePerDistance` of `EtcOption`,
  a single value.

## Open Questions

### What unknown_00 Holds

An amount in Trading EXP: on levels 1 to 49 the EXP of level `r + 1` is a
whole number of these. What one part is (the EXP of one sale, one trade
item or one other action at that level) is not in the client Lua or the
other sources above. This in-game check tests the one-sale reading:

1. On a character with Trading at Beginner 1, sell one trade item to a
   trade manager.
2. Read the Trading EXP gained in the life skill window.
3. Expected if a part is one sale: the bar moves by 1 EXP of 5 (row 0),
   whatever the item or the distance.

No handler shows the file until the value has a name.
