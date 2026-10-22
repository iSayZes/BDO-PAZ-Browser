# `oceansiegeterritoryoption.bss` Format

## Purpose

The Blue Battlefield (ocean siege) options of each siege group: the two
territories the group fights over and the one console shows, the HP,
AP, damage reduction, accuracy, evasion and damage reduction rate limits
(all uncapped), amounts left unknown, a world position, the most
participants per day and the days the battle runs. Client 3482 has one
row, the only ocean group (`BEGINNER`), for Balenos and Calpheon. The Lua
reads it with `ToClient_GetOceanSiegeTerritoryOptionStaticStatusWrapper`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | --------------------- | --------- |
| 2      | 3474 and later | 3482    | `oceansiegeterritoryoption.bss` | 196   | 1 Row, 1 String Table | 176       |
| 1      | 3251           | 3251    | `oceansiegeterritoryoption.bss` | 192   | 1 Row, 1 String Table | 172       |

| Layout | File                            | Known        | Unknown       |
| ------ | ------------------------------- | ------------ | ------------- |
| 2      | `oceansiegeterritoryoption.bss` | 90 B (45.9%) | 106 B (54.1%) |
| 1      | `oceansiegeterritoryoption.bss` | 86 B (44.8%) | 106 B (55.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 1 |
| 3002   | No file  |
| 2765   | No file  |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                      |
| --------------------- | -------- | ----------------------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12              |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                                        |
| ------------------- | -------------- | ------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                                 |
| `+0x04`             | u32            | row_count    | Number of rows, one per ocean siege group; `1` on client 3482 |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                                         |
| `rows+0x00`         | String Table   | string_table | See String Table                                             |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends                |
| `string_table+0x04` | u32            | zero         | Always `0`                                                   |

### Row (variable: 152 bytes + start days)

| Offset  | Type                  | Field                       | Notes                                                                       |
| ------- | --------------------- | --------------------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16                   | territory_key_1             | `territoryinfo.bss` key, LOC type 12 name; `0` (Balenos) on client 3482     |
| `+0x02` | u16                   | territory_key_2             | `2` (Calpheon) on client 3482                                               |
| `+0x04` | u16                   | console_territory_key       | The territory console shows; `0` on client 3482                             |
| `+0x06` | f32                   | hp_limit                    | `100000000`                                                                 |
| `+0x0A` | f32                   | ap_limit                    | `9999`                                                                      |
| `+0x0E` | f32                   | dr_limit                    | `9999`                                                                      |
| `+0x12` | f32                   | unknown_12                  | FLT_MAX (`FF FF 7F 7F`); with `unknown_16` the AP+DP limit, see Field Names |
| `+0x16` | f32                   | unknown_16                  | FLT_MAX                                                                     |
| `+0x1A` | f32                   | accuracy_limit              | `9999`                                                                      |
| `+0x1E` | f32                   | evasion_limit               | `9999`                                                                      |
| `+0x22` | u32                   | dr_rate_limit               | `1000000`                                                                   |
| `+0x26` | u32                   | unknown_26                  | `1000000`                                                                   |
| `+0x2A` | u32                   | unknown_2a                  | `1000000`                                                                   |
| `+0x2E` | u32                   | unknown_2e                  | `0`                                                                         |
| `+0x32` | f32                   | unknown_32                  | `9999`                                                                      |
| `+0x36` | f32                   | unknown_36                  | `9999`                                                                      |
| `+0x3A` | f32                   | unknown_3a                  | `100000000`                                                                 |
| `+0x3E` | u32                   | unknown_3e                  | `1000000`                                                                   |
| `+0x42` | u32                   | unknown_42                  | `1000000`                                                                   |
| `+0x46` | u32                   | unknown_46                  | `1000000`                                                                   |
| `+0x4A` | u32                   | unknown_4a                  | `1000000`                                                                   |
| `+0x4E` | bytes[34]             | unknown_4e                  | All `0`                                                                     |
| `+0x70` | u32                   | unknown_70                  | `300000`                                                                    |
| `+0x74` | u32                   | unknown_74                  | `200000`                                                                    |
| `+0x78` | f32                   | unknown_78                  | `13534`; with the next two a world position near Velia, see Notes           |
| `+0x7C` | f32                   | unknown_7c                  | `-7676`                                                                     |
| `+0x80` | f32                   | unknown_80                  | `94091`                                                                     |
| `+0x84` | f32                   | unknown_84                  | `300`                                                                       |
| `+0x88` | u16                   | limit_member_count_sunday   | Most participants on a Sunday battle; `20` on every day on client 3482      |
| `+0x8A` | u16                   | limit_member_count_monday   | Monday                                                                      |
| `+0x8C` | u16                   | limit_member_count_tuesday  | Tuesday                                                                     |
| `+0x8E` | u16                   | limit_member_count_wednesday | Wednesday                                                                  |
| `+0x90` | u16                   | limit_member_count_thursday | Thursday                                                                    |
| `+0x92` | u16                   | limit_member_count_friday   | Friday                                                                      |
| `+0x94` | u32                   | start_day_count             | Number of `start_days`                                                      |
| `+0x98` | u32[start_day_count]  | start_days                  | `CppEnums.VillageSiegeType` days; `0` to `5` (Sunday to Friday) on client 3482 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### Row (variable: 148 bytes + start days)

| Offset  | Type                  | Field                        | Notes                                     |
| ------- | --------------------- | ---------------------------- | ----------------------------------------- |
| `+0x00` | u16                   | territory_key_1              | `0` (Balenos), the only ocean territory   |
| `+0x02` | f32                   | hp_limit                     |                                           |
| `+0x06` | f32                   | ap_limit                     |                                           |
| `+0x0A` | f32                   | dr_limit                     |                                           |
| `+0x0E` | f32                   | unknown_12                   |                                           |
| `+0x12` | f32                   | unknown_16                   |                                           |
| `+0x16` | f32                   | accuracy_limit               |                                           |
| `+0x1A` | f32                   | evasion_limit                |                                           |
| `+0x1E` | u32                   | dr_rate_limit                |                                           |
| `+0x22` | u32                   | unknown_26                   |                                           |
| `+0x26` | u32                   | unknown_2a                   |                                           |
| `+0x2A` | u32                   | unknown_2e                   |                                           |
| `+0x2E` | f32                   | unknown_32                   |                                           |
| `+0x32` | f32                   | unknown_36                   |                                           |
| `+0x36` | f32                   | unknown_3a                   |                                           |
| `+0x3A` | u32                   | unknown_3e                   |                                           |
| `+0x3E` | u32                   | unknown_42                   |                                           |
| `+0x42` | u32                   | unknown_46                   |                                           |
| `+0x46` | u32                   | unknown_4a                   |                                           |
| `+0x4A` | bytes[34]             | unknown_4e                   |                                           |
| `+0x6C` | u32                   | unknown_70                   |                                           |
| `+0x70` | u32                   | unknown_74                   |                                           |
| `+0x74` | f32                   | unknown_78                   |                                           |
| `+0x78` | f32                   | unknown_7c                   |                                           |
| `+0x7C` | f32                   | unknown_80                   |                                           |
| `+0x80` | f32                   | unknown_84                   |                                           |
| `+0x84` | u16                   | limit_member_count_sunday    |                                           |
| `+0x86` | u16                   | limit_member_count_monday    |                                           |
| `+0x88` | u16                   | limit_member_count_tuesday   |                                           |
| `+0x8A` | u16                   | limit_member_count_wednesday |                                           |
| `+0x8C` | u16                   | limit_member_count_thursday  |                                           |
| `+0x8E` | u16                   | limit_member_count_friday    |                                           |
| `+0x90` | u32                   | start_day_count              |                                           |
| `+0x94` | u32[start_day_count]  | start_days                   |                                           |

## Field Names

The Blue Battlefield is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client covers it. The names come from the Lua of client 3482, which reads
the row of each ocean group (`_eTerritoryOceanGroupType`, `BEGINNER = 0,
COUNT = 1` in `panel_window_villagesiegemenu_all.luac`) by its index.

| Field                           | Lua (client 3482)                                    | Match                                                                                   |
| ------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `territory_key_1`, `territory_key_2` | `getTerritoryKey1Raw()`, `getTerritoryKey2Raw()` | `0` and `2`, the two keys of `CppEnums.OceanSiegeTerritoryName` (Balenos, Calpheon)     |
| `console_territory_key`         | `getConsoleTerritoryKeyRaw()`                        | The Lua hides the flag of the territory it does not equal, so it is one of the two keys |
| `limit_member_count_*`          | `getLimitMemberCount(day)`                           | Six u16, one per `start_days` day; `day` comes from `ToClient_GetDayOfWeekByVillageSiege()` |
| `start_days`                    | `getStartDayListCount()`, `getStartDay(index)`       | A u32-counted list of `VillageSiegeType` days, which the Lua prints as day names        |

The land table `siegeterritoryoptionstaticstatus.bss`, which the same Lua
reads with `ToClient_GetSiegeTerritoryOptionStaticStatusWrapper`, starts
its rows with the same three u16: on client 3482 the territory pairs `0,
1` (Balenos, Serendia), `2, 11` and `4, 12`, each followed by a key equal
to one of the pair. That fixes the order key 1, key 2, console key. It
holds six u16 counts before the same `0` to `5` day list too (`30, 25,
30, 25, 30, 25` on its first row).

The limit block from `+0x06` to `+0x4E` has the shape of the one in
[`siegeterritoryoptionstaticstatus.bss`](siegeterritoryoptionstaticstatus_bss.md)
from `+0x08`, where node tooltips name `hp_limit`, `ap_limit`,
`dr_limit`, `accuracy_limit`, `evasion_limit` and `dr_rate_limit`. This
row holds the values of that table's uncapped Valencia and Outer Edania
row (`100000000`, `9999`, FLT_MAX, `1000000`), field for field.
`unknown_12` and `unknown_16` are the `_siegeMaxDDForUI` and
`_siegeMaxPVForUI` pair: FLT_MAX in both is the "No Stat Limit" case of
`isUnlimitedDDPV()`. Which of the two is DD stays open there.

## Notes

- Client 3251 uses Layout 1: one territory key and no second or console
  key (192 bytes); every other value is the one client 3482 has. Client
  3474 adds the second and console keys. The file is not in the archives
  of client 1784.
- `unknown_78`, `unknown_7c` and `unknown_80` read as a BDO world position
  (y the height): `(13534, -7676, 94091)`, near the first revive position
  of Balenos in [`oceansiegereviveposition.bss`](oceansiegereviveposition_bss.md),
  `(6186, -7676, 93658)`, and Velia's return point `(-1226, -7012,
  81647)`. `unknown_84` (`300`) fits a radius.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/oceansiege_tables.py`: the three territory keys with
  their names, the six named limits, the six day limits and the battle
  days by name.

## Open Questions

### The Fields Before the Position

What `unknown_4e` (34 zero bytes), `unknown_70` (`300000`) and
`unknown_74` (`200000`) hold. The Lua reads `_limitVolunteerCount` from
this wrapper, which no field here is known to hold.
