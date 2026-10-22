# `siegedayoption.bss` Format

## Purpose

The Node War schedule: for each day of the week, Sunday to Saturday, the
territories whose nodes hold a node war that day. One record of seven
u64-counted lists of u16 territory keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records                | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ---------------------- | --------- |
| 1      | 1348 and later | 3482    | `siegedayoption.bss` | 108   | 1 Days, 1 String Table | 92        |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 1      | `siegedayoption.bss` | 108 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                           |
| ------------------- | ------------ | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                    |
| `+0x04`             | Days         | days         | See Days; no row count, the file has one record |
| `days+0x00`         | String Table | string_table | See String Table                                |
| `string_table+0x00` | u32          | table_start  | Offset of the string table, where `days` ends   |
| `string_table+0x04` | u32          | zero         | Always `0`                                      |

### Days (variable: 56 bytes + territory keys)

| Offset                       | Type                               | Field                          | Notes                                                                              |
| ---------------------------- | ---------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------- |
| `+0x00`                      | u64                                | sunday_territory_key_count     | Number of `sunday_territory_keys`                                                  |
| `+0x08`                      | u16[sunday_territory_key_count]    | sunday_territory_keys          | `territoryinfo.bss` keys, LOC type 12 names. See Schedule                          |
| `sunday_territory_keys+0x00` | u64                                | monday_territory_key_count     |                                                                                    |
| `sunday_territory_keys+0x08` | u16[monday_territory_key_count]    | monday_territory_keys          |                                                                                    |
| `monday_territory_keys+0x00` | u64                                | tuesday_territory_key_count    |                                                                                    |
| `monday_territory_keys+0x08` | u16[tuesday_territory_key_count]   | tuesday_territory_keys         |                                                                                    |
| `tuesday_territory_keys+0x00` | u64                               | wednesday_territory_key_count  |                                                                                    |
| `tuesday_territory_keys+0x08` | u16[wednesday_territory_key_count] | wednesday_territory_keys      |                                                                                    |
| `wednesday_territory_keys+0x00` | u64                             | thursday_territory_key_count   |                                                                                    |
| `wednesday_territory_keys+0x08` | u16[thursday_territory_key_count] | thursday_territory_keys      |                                                                                    |
| `thursday_territory_keys+0x00` | u64                              | friday_territory_key_count     |                                                                                    |
| `thursday_territory_keys+0x08` | u16[friday_territory_key_count]  | friday_territory_keys          |                                                                                    |
| `friday_territory_keys+0x00` | u64                                | saturday_territory_key_count   | `0` on every client checked                                                        |
| `friday_territory_keys+0x08` | u16[saturday_territory_key_count]  | saturday_territory_keys        |                                                                                    |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Schedule

The territories of each day. The keys are those of
`_eTerritoryKeyRaw` in `panel_window_villagesiegemenu_all.luac` (client
3482): `0` Balenos, `1` Serendia, `2` Calpheon, `3` Mediah, `4` Valencia,
`6` Kamasylvia.

| Day       | Client 3482                                           | Client 1784                                           |
| --------- | ----------------------------------------------------- | ----------------------------------------------------- |
| Sunday    | Balenos, Serendia, Calpheon, Mediah, Valencia, Kamasylvia | Balenos, Serendia, Calpheon, Mediah, Valencia, Kamasylvia |
| Monday    | Balenos, Calpheon, Kamasylvia                         | none                                                  |
| Tuesday   | Serendia, Mediah                                      | all six                                               |
| Wednesday | Calpheon, Valencia                                    | all six                                               |
| Thursday  | Balenos, Mediah, Kamasylvia                           | all six                                               |
| Friday    | Serendia, Valencia                                    | all six                                               |
| Saturday  | none                                                  | none                                                  |

## Field Names

The `MinorSiegeDayOption` sheet of a private server's `DataSheets.bexcel`
on client 1784 (Node War is `MinorSiege` in the client's names, the
Conquest War `MajorSiege`) has one row with the columns `Sunday` to
`Saturday`, each a comma list. All seven lists equal the lists of the
client 3482 file in order and value (7 of 7); `Saturday` is `<null>`.
The client 1784 file holds other lists: all six territories on Sunday
and Tuesday to Friday, none on Monday; its `ForeignMinorSiegeDayOption`
sheet has all six on Monday too. The day order is that of `CppEnums.VillageSiegeType` (Sunday `0`
to Saturday `6`).

## Notes

- The file holds no row count: `+0x04` starts the first list, and the
  string table follows the Saturday list.
- No client Lua reads the file; the node war menu takes the day from
  `ToClient_GetDayOfWeekByVillageSiege()`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: one column per day with the
  territory names.
