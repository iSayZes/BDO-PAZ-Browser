# `monsterbuffzone.bss` Format

## Purpose

A table of the monster buff zone, the zone a Dehkia's Lantern opens: the
zone window (`panel_window_monsterbuffzone`) shows the lantern's
durability (`ToClient_GetMonsterBuffZoneCurrentEndurance()`,
`ToClient_GetMonsterBuffZoneMaxEndurance()`), the player's distance to the
zone (`ToClient_GetDistanceMonsterBuffZoneToSelfPlayer()`) and plays the
`fUI_DekiaLanterns_Alarm_01A` effect past 80% of the largest distance; its
off button asks with the `LUA_DEKIA_SUMMONOFF_MSGTITLE` text. The repair
window (`panel_window_monsterbuffzoneitemrepair`) charges the lantern with
`ToClient_GetMonsterBuffZoneMaterialItemSSW()`. None of these calls takes
a key of this file. On client 3474 the file has 10 rows, keys `0x000` to
`0x004` and `0x100` to `0x104`. The file is a u32 count and fixed rows,
with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `monsterbuffzone.bss` | 224   | 10 Row  | 22        |

| Layout | File                  | Known        | Unknown       |
| ------ | --------------------- | ------------ | ------------- |
| 1      | `monsterbuffzone.bss` | 44 B (19.6%) | 180 B (80.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
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

### Row (22 bytes)

| Offset  | Type | Field      | Notes                                                        |
| ------- | ---- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u32  | key        | Row key: second byte `0` or `1`, first byte `0` to `4` (client 3474) |
| `+0x04` | u32  | unknown_04 | `2000` on every row of client 3474                           |
| `+0x08` | u32  | unknown_08 | `1` on every row                                             |
| `+0x0C` | u32  | unknown_0c | `1` on every row                                             |
| `+0x10` | u32  | unknown_10 | `1` on every row                                             |
| `+0x14` | u8   | unknown_14 | The key's second byte                                        |
| `+0x15` | u8   | unknown_15 | The key's first byte                                         |

The rows run `0x004` down to `0x000`, then `0x104` down to `0x100`.

## Notes

- The file is not in client 1784, and no sheet of a private server's
  `DataSheets.bexcel` on client 1784 or member of the 2016 client's debug
  symbols holds it. The client 1784 server dump has no monster buff zone
  text either.
- The two key bytes repeat as the last two bytes of the row, in the order
  second byte, first byte.

## Open Questions

### What the Key Bytes Select

The rows form two sets of five (`unknown_14` `0` and `1`, `unknown_15` `0`
to `4`). LOC type 0 names five Dehkia's Lantern items (`790584` Tier 1,
`790585` Tier 2, and three more named `Dehkia's Lantern`, `790586` to
`790588`). Whether `unknown_15` is the lantern tier, and what the second
byte splits, is open; every other value is the same on all 10 rows.

### unknown_04 to unknown_10

`2000`, `1`, `1` and `1` on all 10 rows. The Lua shows a maximum distance
and a maximum durability per zone, but reads both from the client, so
neither can be matched to a value here.
