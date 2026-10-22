# `siegegovernorcarriagespawn.bss` Format

## Purpose

The Conquest War supply wagon spawns per territory: rows of the wagon's
character key, the territory key, a start time, an action index, a u32,
a maximum term and a list of spawn position indexes into
[`siegegovernorcarriagespawnposition.bss`](siegegovernorcarriagespawnposition_bss.md).
On client 3482 the three rows are Calpheon, Mediah and Valencia, each
with the Military Supply Wagon (`59670`) and three positions.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3482    | `siegegovernorcarriagespawn.bss` | 152   | 3 Row   | 44        |

| Layout | File                             | Known         | Unknown     |
| ------ | -------------------------------- | ------------- | ----------- |
| 1      | `siegegovernorcarriagespawn.bss` | 140 B (92.1%) | 12 B (7.9%) |

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
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
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

| File                  | Required | Role                                       |
| --------------------- | -------- | ------------------------------------------ |
| `languagedata_en.loc` | Optional | Character names (LOC type 6) and territory names (LOC type 12) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `0` on clients that ship the file empty |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 32 bytes + positions)

| Offset  | Type                          | Field                     | Notes                                                                 |
| ------- | ----------------------------- | ------------------------- | --------------------------------------------------------------------- |
| `+0x00` | u16                           | character_key             | `characterstatic.dbss` key of the wagon; `59670` on every row         |
| `+0x02` | u16                           | territory_key             | `territoryinfo.bss` key (LOC type 12); one row each                   |
| `+0x04` | u64                           | start_time                | `1800` on every row of client 3482                                    |
| `+0x0C` | u32                           | action_index              | `0`, `1`, `2`: the row's place in file order                          |
| `+0x10` | u32                           | unknown_10                | `1` on every row of client 3482                                       |
| `+0x14` | u64                           | max_term                  | `3600` on every row of client 3482                                    |
| `+0x1C` | u32                           | spawn_position_count      | Number of spawn positions; `3` on every row of client 3482            |
| `+0x20` | u32[spawn_position_count]     | spawn_position_list       | `index` values of `siegegovernorcarriagespawnposition.bss`            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Rows

Client 3482, in file order. Every row has `character_key` `59670`
(Military Supply Wagon), `start_time` `1800`, `unknown_10` `1` and
`max_term` `3600`.

| `territory_key` | Territory | `action_index` | `spawn_position_list` |
| --------------- | --------- | -------------- | --------------------- |
| 2               | Calpheon  | 0              | 0, 1, 2               |
| 3               | Mediah    | 1              | 3, 4, 5               |
| 4               | Valencia  | 2              | 6, 7, 8               |

## Field Names

The `MajorSiegeTankSpawn` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `MajorSiegeRegion`, `CharacterKey`,
`ActionIndex`, `StartTime`, `MaxTerm` and `IndexPosition` and three rows.
Client 1784 ships the file empty, so the sheet is checked against client
3482: `CharacterKey` (`59670`), `MajorSiegeRegion` (`2`, `3`, `4`),
`ActionIndex` (`0`, `1`, `2`), `MaxTerm` (`3600`) and `IndexPosition`
(`0,1,2`, `3,4,5`, `6,7,8`) match all three rows; `StartTime` is `7200`
in the sheet and `1800` in the file. That server's dump (client 1784)
names the members `MajorSiegeTankSpawnStaticStatus _territoryKey`,
`_characterKey`, `_startTime` and `_spawnPositionList`. The u64 at
`+0x04` is the only field left for `StartTime`; `start_time` and the
other names follow the members, `action_index` and `max_term` the sheet.
The server calls the wagon a tank (`MajorSiegeTank`); the client file
name calls it the governor's carriage.

## Notes

- Clients 1784 to 2765 ship the file with `row_count` `0`; client 3002
  and later hold the three rows.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  the territory with its name first, then the wagon with its name and the
  other fields.

## Open Questions

### The u32 After the Action Index

`unknown_10` is `1` on every row of client 3482 and has no sheet column on
client 1784.

### The Units of start_time and max_term

The Pearl Abyss console notice
([board 13255](https://blackdesert.pearlabyss.com/Console/en-us/News/Notice/Detail?_boardNo=13255))
says the Military Supply Wagon spawns at a random time between 1 hour and
1 hour 30 minutes after the start of the Conquest War. In seconds, that is
`max_term` `3600` plus up to `start_time` `1800`. Which field is the fixed
delay and which the random window, and whether the PC client uses the same
times, is not confirmed.
