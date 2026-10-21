# `bossmonsterhpsyncstaticstatus.bss` Format

## Purpose

Three boss characters, each with a key, a box of world sectors and two
unknown numbers. The name says "boss monster HP sync"; no client Lua names
the file, so what is synced and how is not known from the client.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `bossmonsterhpsyncstaticstatus.bss` | 98    | 3 Row   | 26        |

| Layout | File                                | Known        | Unknown      |
| ------ | ----------------------------------- | ------------ | ------------ |
| 1      | `bossmonsterhpsyncstaticstatus.bss` | 80 B (81.6%) | 18 B (18.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
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

None. Names come from LOC type 6.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                 |
| ------------------- | -------------- | ------------ | ------------------------------------- |
| `+0x00`             | char[4]        | magic        | `PABR`                                |
| `+0x04`             | u32            | row_count    | `3` on client 3464                    |
| `+0x08`             | Row[row_count] | rows         | See Row                               |
| `rows+0x00`         | String Table   | string_table | The string table is empty             |
| `string_table+0x00` | u32            | table_start  | Where the rows end                    |
| `string_table+0x04` | u32            | zero         |                                       |

### Row (26 bytes)

| Offset  | Type | Field        | Notes                                                             |
| ------- | ---- | ------------ | ----------------------------------------------------------------- |
| `+0x00` | u16  | key          | `1, 3, 2` in file order on client 3464                            |
| `+0x02` | u16  | character_id | `characterstatic.dbss` character ID, LOC type 6                   |
| `+0x04` | i32  | min_x        | Sector box, lower corner; one sector is 12,800 world units, as in `instancefield.dbss` |
| `+0x08` | i32  | min_z        |                                                                   |
| `+0x0C` | i32  | max_x        | Upper corner; 2 above `min_x` on Garmoth and Baby Vell, 1 on Gift Box |
| `+0x10` | i32  | max_z        |                                                                   |
| `+0x14` | u16  | unknown_14   | `30` (Garmoth) or `10`                                            |
| `+0x16` | u32  | unknown_16   | `300000`, `1000000` or `800000`                                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Notes

- Garmoth's Boss Info position in
  [`bossinfostaicstatusmanager.bss`](bossinfostaicstatusmanager_bss.md)
  (x -21,954, z -324,742) is sector (-2, -26), inside Garmoth's box here.
  Gift Box's Boss Info position (x -12,325, z 37,767, sector (-1, 2)) is
  outside its box (2, 6) to (3, 7), so the box is not the Boss Info spot
  for every row. Baby Vell has no Boss Info record.
- Reading the four i32s as (min_x, max_x, min_z, max_z) puts a minimum
  above its maximum on Garmoth (-3, -27), so the order is
  (min_x, min_z, max_x, max_z).
- The Lua of the boss HP bar (`panel_widget_monsterbar_renew`,
  `panel_widget_enemygauge_new`) and of the Boss Info window
  (`ToClient_getBossHPPercent`, `ToClient_updateBossHPList`) reads HP from
  the client, not from this file.

## Open Questions

### unknown_14 and unknown_16

`unknown_14` is `30` on Garmoth and `10` on the other two; `unknown_16` is
`300000`, `1000000` and `800000`. They could be an interval and a range or
an HP threshold, but nothing in the client names them.

### Gift Box Box

Gift Box's sector box does not hold its Boss Info position. The event may
place the box elsewhere, or the box may mean something other than the
boss's area.
