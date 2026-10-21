# `itemenchantsafety.dbss` Format

## Purpose

The enhancement safety limits per gear type: for the enhancement levels
`min_level` to `max_level`, the failstack at which enhancing stops
(`stack`) and the failstack and success chance above which the game shows a
caution (`caution_stack`, `caution_rate`). Companion
`itemenchantsafetyoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `itemenchantsafety.dbss`       | 94    | 6 Row        | 15        |
| 1      | 1485 and later | 3474    | `itemenchantsafetyoffset.dbss` | 76    | 6 Offset Row | 12        |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `itemenchantsafety.dbss`       | 94 B (100.0%) | 0 B (0.0%) |
| 1      | `itemenchantsafetyoffset.dbss` | 76 B (100.0%) | 0 B (0.0%) |

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

| File                           | Required | Role                                                                     |
| ------------------------------ | -------- | ------------------------------------------------------------------------ |
| `itemenchantsafetyoffset.dbss` | Optional | `type -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 6 x 15 = 94 bytes.

### Row (15 bytes)

| Offset  | Type | Field         | Notes                                                                       |
| ------- | ---- | ------------- | --------------------------------------------------------------------------- |
| `+0x00` | u8   | type          | Gear type, see Gear Types; unique                                           |
| `+0x01` | u8   | min_level     | Lowest enhancement level of the range; `0` on every row of clients 1784 and 3474 |
| `+0x02` | u8   | max_level     | Highest enhancement level of the range                                      |
| `+0x03` | u32  | stack         | Failstack from which enhancing in the range is blocked                      |
| `+0x07` | u32  | caution_stack | Failstack from which a caution can show                                     |
| `+0x0B` | u32  | caution_rate  | Success chance above which the caution shows, 1,000,000 = 100%              |

The rows are sorted by `type`.

### `itemenchantsafetyoffset.dbss`

Bare offset table into `itemenchantsafety.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `itemenchantsafety.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | type        | `type` of the row it points at                                     |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `itemenchantsafety.dbss`, at its `type` |
| `+0x08` | u32  | data_size   | `15` on every row: the whole row                                   |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. On
clients 1784 and 3474 every index row points at the row with its type, in
file order.

## Gear Types

The developer comment on the `Type` column of the `Enchant_Safetymode`
sheet (a private server's `datasheet_enchantdatatable_new.xlsm`, client
1784) names types `0` to `4`. Type `5` came between clients 3002 and 3251:
clients 3251 and 3474 have it, 3002 and older do not.

| Type | Gear (sheet comment)                                                                      | Levels (client 3474) | `stack` | `caution_stack` | `caution_rate` |
| ---- | ----------------------------------------------------------------------------------------- | -------------------- | ------- | --------------- | -------------- |
| 0    | Main weapons, sub-weapons, awakening weapons                                              | 0 to 18              | 100     | 150             | 30%            |
| 1    | Armor                                                                                     | 0 to 18              | 100     | 150             | 30%            |
| 2    | Accessories                                                                               | 0 to 2               | 100     | 50              | 70%            |
| 3    | Fishing rods, matchlocks, Trina battle axes, mount gear (ships, boats, wagons, horse gear, elephants) | 0 to 5 | 100     | 50              | 70%            |
| 4    | Silver Embroidered clothes (armor that takes more than one equipment slot)                 | 0 to 2               | 100     | 50              | 70%            |
| 5    | Not in the sheet                                                                          | 0 to 18              | 100     | 150             | 30%            |

On client 1784 types `0` and `1` read `0` to `17`, `caution_stack` `50` and
`caution_rate` 70%, like the other three.

## Field Names

The `Enchant_Safetymode` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Type`, `Min`, `Max`, `Stack`, `CautionStack`
and `CautionRate`, and its 5 rows match the client 1784 file on all 5 types
and every column. The developer comments on the sheet's header cells
(`datasheet_enchantdatatable_new.xlsm`, dated 2019-08-22 for the two
caution columns) say:

| Column         | Comment (translated)                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------- |
| `Min`, `Max`   | The group of levels where enhancing is blocked: Min `0` and Max `7` make +0 to +7 one group                   |
| `Stack`        | Enhancing is blocked when the character's failstack, without Valks' Cry, is at or above the value            |
| `CautionStack` | With a failstack at or above the value, a caution message shows when the success chance is above `CautionRate` |
| `CautionRate`  | `10000` = 1%                                                                                                  |

## Notes

- No client Lua script names a getter for the file: none of the 3,073
  scripts of client 3473 holds `Safety`, `SafeMode` or `Caution` next to
  enhancing, so the block and the caution run in the exe or on the server.
- The file exists on every checked client from 1485 to 3474 (1485, 1784,
  2107, 2519, 3002, 3251, 3474); clients 1485 and 1784 hold the same five
  rows. Client 1230 has an `itemenchantsafety.bss` in its place.

## Open Questions

### Gear Type 5

Type `5` (levels 0 to 18, `stack` 100, `caution_stack` 150, `caution_rate`
30%) has the values of types `0` and `1` but no name in the 1784 sheet, which
ends at type `4`. Which gear it covers is unknown.

### Current or Target Level

The sheet comment says Min `0` and Max `7` make "+0 to +7" one group, which
does not say whether the range holds the gear's level before the attempt or
the level it enhances to. With `max_level` 18 the two readings differ on the
TRI to TET attempt.
