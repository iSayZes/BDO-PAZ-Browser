# `siege2024revivepositionstaticstatus.bss` Format

## Purpose

Where Node War (the 2024 land siege) players can revive, per territory:
each row holds a territory key and up to three world positions, each
with an f32. On client 3482 the 8 rows cover Balenos, Serendia,
Calpheon, Ulukita, Mediah, Outer Edania, Valencia and Kamasylvia, in
that order, with 21 positions. The death window offers one revive
button per position of the player's territory.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                      | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ----------------------------------------- | ----- | ------------------ | --------- |
| 1      | 2519 and later | 3482    | `siege2024revivepositionstaticstatus.bss` | 404   | 21 Position, 8 Row | 16        |

| Layout | File                                      | Known         | Unknown      |
| ------ | ----------------------------------------- | ------------- | ------------ |
| 1      | `siege2024revivepositionstaticstatus.bss` | 320 B (79.2%) | 84 B (20.8%) |

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
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
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

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows, one per territory             |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 6 bytes + positions)

| Offset  | Type                     | Field          | Notes                                                       |
| ------- | ------------------------ | -------------- | ----------------------------------------------------------- |
| `+0x00` | u32                      | position_count | Number of positions; `1` to `3` on client 3482; the count comes before the key |
| `+0x04` | u16                      | territory_key  | `territoryinfo.bss` key, LOC type 12 name; one row each     |
| `+0x06` | Position[position_count] | positions      | See Position                                                |

### Position (16 bytes)

| Offset  | Type | Field      | Notes                                     |
| ------- | ---- | ---------- | ----------------------------------------- |
| `+0x00` | f32  | x          | World x                                   |
| `+0x04` | f32  | y          | Height                                    |
| `+0x08` | f32  | z          | World z                                   |
| `+0x0C` | f32  | unknown_0c | `500` on every position of client 3482    |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The file is newer than client 1784: it is not in that client's archives
and no sheet of a private server's `DataSheets.bexcel` on that client
covers it. `panel_window_deadmessage_all_1.luac` (client 3482) shows the
death window's `MinorSiegeOccupyModeRevivePosition0` to `3` buttons only
while the button index is below `ToClient_GetSiege2024RevivePositionCount()`
and the player takes part in the 2024 siege
(`ToClient_IsSelfParticipateInSiege2024()`); `panel_itemwarp_all_1.luac`
lists that many towns to warp to. The positions read as world
coordinates on the scale of the `regioninfo.bss` return points, and the
key is the territory they lie in: for 20 of the 21 positions of client
3482 the region with the nearest return point belongs to the row's
`territory_key` (LOC type 12: `0` Balenos, `1` Serendia, `2` Calpheon,
`3` Mediah, `4` Valencia, `6` Kamasylvia, `11` Ulukita, `12` Outer
Edania). The one other is a Calpheon position at `(-150360, -1424,
-144603)`, nearest the return point of Kamasylvia Castle.

## Notes

- Clients 2519 to 3251 hold six territories (328 bytes, no Ulukita or
  Outer Edania row) with the positions of client 3482, except one
  Valencia position at `(1262151, -3859, 181315)`, 278 units from the
  one client 3482 has there; client 2519 also has its second Serendia
  position at `(-12936, 248, -118908)`.
- The handler of `oceansiegereviveposition.bss`
  (`_bss/oceansiegereviveposition/`) previews this file with the reader
  in `_bss/siege2024revivepositionstaticstatus/`: one row per position,
  the territory key and name and the position rounded to whole units,
  in file order.

## Open Questions

### The f32 of Each Position

`unknown_0c` is `500` on every position. A spread radius around the
position fits, as the f32 after the positions of
[`oceansiegereviveposition.bss`](oceansiegereviveposition_bss.md) and
[`rosewarrevivepositionstaticstatus.bss`](rosewarrevivepositionstaticstatus_bss.md)
does, but nothing reads it.
