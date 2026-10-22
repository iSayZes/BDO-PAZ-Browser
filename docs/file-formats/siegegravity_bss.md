# `siegegravity.bss` Format

## Purpose

One world position and an f32 per Conquest War territory: rows of a u16
territory key, three f32 coordinates and an unnamed f32. On client 3482
the three rows are Calpheon (`2`), Mediah (`3`) and Valencia (`4`), and
each position lies in that territory's castle. What the client does with
the point is open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------ | ----- | ------- | --------- |
| 1      | 2637 and later | 3482    | `siegegravity.bss` | 74    | 3 Row   | 18        |

| Layout | File               | Known        | Unknown      |
| ------ | ------------------ | ------------ | ------------ |
| 1      | `siegegravity.bss` | 62 B (83.8%) | 12 B (16.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                          |
| --------------------- | -------- | ----------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (18 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | territory_key | `territoryinfo.bss` key (LOC type 12); one row each                   |
| `+0x02` | f32  | position_x    | World X                                                               |
| `+0x06` | f32  | position_y    | World Y (height)                                                      |
| `+0x0A` | f32  | position_z    | World Z                                                               |
| `+0x0E` | f32  | unknown_0e    | `13500` to `18000` on client 3482, a round number per row             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Rows

Client 3482, in file order.

| `territory_key` | Territory | `position_x` | `position_y` | `position_z` | `unknown_0e` |
| --------------- | --------- | ------------ | ------------ | ------------ | ------------ |
| 4               | Valencia  | 1160597      | 18668        | 299213       | 18000        |
| 3               | Mediah    | 310370       | -3626        | 53438        | 15000        |
| 2               | Calpheon  | -354348      | 3293         | -59848       | 13500        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
these rows, and client 1784 does not ship the file. The territory keys
are the three Conquest War territories of `siegegovernorcarriagespawn.bss`
(`MajorSiegeRegion`). The three coordinates are a world position: each
lies within about 1,000 units of the four castle gate positions the
`SiegeCastleTeleportPos` sheet (client 1784) gives for the same territory
key, e.g. Calpheon `-348487` to `-354847` (X) and `-55022` to `-61718`
(Z).

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  the territory with its name and the position.

## Open Questions

### What the Gravity Point Is

No client Lua of client 3482 names `siegegravity` or a getter for it. The
Lua has the event `FromClient_DestroyedSiegeGravityMagician`
(`panel_warinfomessage.luac`), whose message
`LUA_WARINFOMESSAGE_NOTIFYKINGORLORDTENTCHANGE_DESTROYGRAVITY_MAIN` reads
"All Dekrogda relics have been destroyed, undoing the barrier." The rows
may be the centre of that barrier at each castle, with `unknown_0e` its
radius (13,500 to 18,000 units); nothing in the client data ties the two
together yet.
