# `siegeterritoryoptionstaticstatus.bss` Format

## Purpose

The Node War options of each territory group: the two territories a
group fights in and the one console shows, the stat limits of its node
wars, the most participants per day, the battle days, the map icon
positions of the two territories and a list of skills. Client 3482 has
three rows, one per `_eTerritoryGroupType` (`BEGINNER = 0`, `ADVANCED =
1`, `INTERMEDIATE = 2` in `panel_window_villagesiegemenu_all.luac`):
Balenos and Serendia, Calpheon and Ulukita, Valencia and Outer Edania.
The Lua reads a row with
`ToClient_GetSiegeTerritoryOptionStaticStatusWrapper(groupType)`. The
Blue Battlefield table
[`oceansiegeterritoryoption.bss`](oceansiegeterritoryoption_bss.md) opens
its rows with the same keys and limit block.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                   | Bytes | Records | Row bytes                  |
| ------ | -------------- | ------- | -------------------------------------- | ----- | ------- | -------------------------- |
| 2      | 3474 and later | 3482    | `siegeterritoryoptionstaticstatus.bss` | 797   | 3 Row   | 247 to 283, 259 on average |
| 1      | 2765 to 3251   | 3251    | `siegeterritoryoptionstaticstatus.bss` | 485   | 3 Row   | 155                        |

| Layout | File                                   | Known         | Unknown       |
| ------ | -------------------------------------- | ------------- | ------------- |
| 2      | `siegeterritoryoptionstaticstatus.bss` | 302 B (37.9%) | 495 B (62.1%) |
| 1      | `siegeterritoryoptionstaticstatus.bss` | 230 B (47.4%) | 255 B (52.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2765   | Layout 1             |
| 2519   | No documented layout |
| 2313   | No file              |
| 2107   | No file              |
| 1937   | No file              |
| 1784   | No file              |
| 1636   | No file              |
| 1485   | No file              |
| 1348   | No file              |
| 1230   | No file              |
| 1058   | No file              |
| 794    | No file              |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                                |
| ------------------- | -------------- | ------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                         |
| `+0x04`             | u32            | row_count    | Number of rows, one per territory group              |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                                 |
| `rows+0x00`         | String Table   | string_table | See String Table                                     |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends        |
| `string_table+0x04` | u32            | zero         | Always `0`                                           |

### Row (variable: 223 bytes + start days and skills)

Values in the Notes are those of the three rows of client 3482, in
order.

| Offset                | Type                          | Field                        | Notes                                                                       |
| --------------------- | ----------------------------- | ---------------------------- | --------------------------------------------------------------------------- |
| `+0x00`               | u16                           | territory_key_1              | `territoryinfo.bss` key, LOC type 12 name: `0`, `2`, `4`                     |
| `+0x02`               | u16                           | territory_key_2              | `1`, `11`, `12`                                                              |
| `+0x04`               | u16                           | console_territory_key        | The territory console shows: `1`, `11`, `12`                                |
| `+0x06`               | u16                           | unknown_06                   | `14`, `3`, `3`                                                               |
| `+0x08`               | f32                           | hp_limit                     | `6500`, `11000`, `100000000`. See Stat Limits                                |
| `+0x0C`               | f32                           | ap_limit                     | `395`, `680`, `9999`                                                         |
| `+0x10`               | f32                           | dr_limit                     | Damage reduction: `335`, `530`, `9999`                                       |
| `+0x14`               | f32                           | unknown_14                   | `270`, `309`, FLT_MAX; with `unknown_18` the AP+DP limit, see Stat Limits     |
| `+0x18`               | f32                           | unknown_18                   | `346`, `411`, FLT_MAX                                                        |
| `+0x1C`               | f32                           | accuracy_limit               | `650`, `820`, `9999`                                                         |
| `+0x20`               | f32                           | evasion_limit                | `738`, `908`, `9999`                                                         |
| `+0x24`               | u32                           | dr_rate_limit                | Damage reduction rate, `1000000` = 100%: `200000`, `300000`, `1000000`       |
| `+0x28`               | u32                           | unknown_28                   | `0`, `0`, `1000000`                                                          |
| `+0x2C`               | u32                           | unknown_2c                   | `0`, `0`, `1000000`                                                          |
| `+0x30`               | u32                           | unknown_30                   | `0` on every row                                                             |
| `+0x34`               | f32                           | unknown_34                   | Equals `ap_limit` on every row                                               |
| `+0x38`               | f32                           | unknown_38                   | Equals `ap_limit` on every row                                               |
| `+0x3C`               | f32                           | unknown_3c                   | `100000000` on every row                                                     |
| `+0x40`               | u32                           | unknown_40                   | `300000`, `1000000`, `1000000`; the next three equal it on every row         |
| `+0x44`               | u32                           | unknown_44                   |                                                                              |
| `+0x48`               | u32                           | unknown_48                   |                                                                              |
| `+0x4C`               | u32                           | unknown_4c                   |                                                                              |
| `+0x50`               | u16                           | unknown_50                   | `0`, `1`, `2`: the row's `_eTerritoryGroupType`                              |
| `+0x52`               | u16                           | unknown_52                   | `3` on every row                                                             |
| `+0x54`               | u16                           | unknown_54                   | `2` on every row                                                             |
| `+0x56`               | u16                           | unknown_56                   | `1` on every row                                                             |
| `+0x58`               | u16                           | unknown_58                   | `2` on every row                                                             |
| `+0x5A`               | u16                           | unknown_5a                   | `1` on every row                                                             |
| `+0x5C`               | u16                           | unknown_5c                   | `1` on every row                                                             |
| `+0x5E`               | u16                           | unknown_5e                   | `10` on every row                                                            |
| `+0x60`               | u16                           | unknown_60                   | `1` on every row                                                             |
| `+0x62`               | u32                           | unknown_62                   | `10000` on every row                                                         |
| `+0x66`               | u32                           | unknown_66                   | `0` on every row                                                             |
| `+0x6A`               | u32                           | unknown_6a                   | `30000` on every row                                                         |
| `+0x6E`               | u32                           | unknown_6e                   | `0` on every row                                                             |
| `+0x72`               | u16                           | limit_member_count_sunday    | Most participants on a Sunday node war: `30`, `50`, `75`                     |
| `+0x74`               | u16                           | limit_member_count_monday    | `25`, `40`, `55`                                                             |
| `+0x76`               | u16                           | limit_member_count_tuesday   | `30`, `40`, `55`                                                             |
| `+0x78`               | u16                           | limit_member_count_wednesday | `25`, `40`, `75`                                                             |
| `+0x7A`               | u16                           | limit_member_count_thursday  | `30`, `40`, `55`                                                             |
| `+0x7C`               | u16                           | limit_member_count_friday    | `25`, `50`, `75`                                                             |
| `+0x7E`               | u32                           | start_day_count              | Number of `start_days`                                                       |
| `+0x82`               | u32[start_day_count]          | start_days                   | `CppEnums.VillageSiegeType` days; `0` to `5` (Sunday to Friday) on every row |
| `start_days+0x00`     | u8                            | unknown_start_days_00        | `2`, `3`, `4`                                                                |
| `start_days+0x01`     | f32                           | territory_1_icon_x           | Map icon of `territory_key_1`: `630`, `430`, `1110`                          |
| `start_days+0x05`     | f32                           | territory_1_icon_y           | `270`, `410`, `220`                                                          |
| `start_days+0x09`     | f32                           | territory_2_icon_x           | Map icon of `territory_key_2`: `660`, `840`, `950`                           |
| `start_days+0x0D`     | f32                           | territory_2_icon_y           | `390`, `420`, `80`                                                           |
| `start_days+0x11`     | u32                           | unknown_start_days_11        | `200000` on the first row, `0x7FFFFFFF` on the others                        |
| `start_days+0x15`     | u32                           | unknown_start_days_15        | `0x7FFFFFFF` on every row                                                    |
| `start_days+0x19`     | u32                           | unknown_start_days_19        | As `unknown_start_days_11`                                                   |
| `start_days+0x1D`     | u32                           | unknown_start_days_1d        | As `unknown_start_days_15`                                                   |
| `start_days+0x21`     | u32                           | unknown_start_days_21        | As `unknown_start_days_11`                                                   |
| `start_days+0x25`     | u32                           | unknown_start_days_25        | As `unknown_start_days_15`                                                   |
| `start_days+0x29`     | u32                           | unknown_start_days_29        | As `unknown_start_days_11`                                                   |
| `start_days+0x2D`     | u32                           | unknown_start_days_2d        | As `unknown_start_days_15`                                                   |
| `start_days+0x31`     | u32                           | unknown_start_days_31        | As `unknown_start_days_11`                                                   |
| `start_days+0x35`     | u32                           | unknown_start_days_35        | As `unknown_start_days_15`                                                   |
| `start_days+0x39`     | u32                           | unknown_start_days_39        | As `unknown_start_days_11`                                                   |
| `start_days+0x3D`     | u32                           | unknown_start_days_3d        | As `unknown_start_days_15`                                                   |
| `start_days+0x41`     | u32                           | unknown_start_days_41        | `200000`, `1000000`, `1000000`                                               |
| `start_days+0x45`     | u32                           | unknown_start_days_45        | `200000`, `0x7FFFFFFF`, `0x7FFFFFFF`                                         |
| `start_days+0x49`     | f32                           | hp_recovery_limit            | `5`, `0`, `0`                                                                |
| `start_days+0x4D`     | u32                           | unknown_start_days_4d        | `10000`, `0`, `0`                                                            |
| `start_days+0x51`     | u32                           | unknown_start_days_51        | `15`, `0`, `0`                                                               |
| `start_days+0x55`     | u32                           | stamina_limit                | `2100`, `0`, `0`                                                             |
| `start_days+0x59`     | u32                           | unknown_skill_no_count       | Number of `unknown_skill_nos`: `18`, `0`, `0`                                |
| `start_days+0x5D`     | u16[unknown_skill_no_count]   | unknown_skill_nos            | Skill numbers, LOC type 10 names. See Notes                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### Row (variable: 131 bytes + start days)

| Offset            | Type                 | Field                        | Notes |
| ----------------- | -------------------- | ---------------------------- | ----- |
| `+0x00`           | u16                  | territory_key_1              |       |
| `+0x02`           | u16                  | territory_key_2              |       |
| `+0x04`           | u16                  | console_territory_key        |       |
| `+0x06`           | u16                  | unknown_06                   |       |
| `+0x08`           | f32                  | hp_limit                     |       |
| `+0x0C`           | f32                  | ap_limit                     |       |
| `+0x10`           | f32                  | dr_limit                     |       |
| `+0x14`           | f32                  | unknown_14                   |       |
| `+0x18`           | f32                  | unknown_18                   |       |
| `+0x1C`           | f32                  | accuracy_limit               |       |
| `+0x20`           | f32                  | evasion_limit                |       |
| `+0x24`           | u32                  | dr_rate_limit                |       |
| `+0x28`           | u32                  | unknown_28                   |       |
| `+0x2C`           | u32                  | unknown_2c                   |       |
| `+0x30`           | u32                  | unknown_30                   |       |
| `+0x34`           | f32                  | unknown_34                   |       |
| `+0x38`           | f32                  | unknown_38                   |       |
| `+0x3C`           | f32                  | unknown_3c                   |       |
| `+0x40`           | u32                  | unknown_40                   |       |
| `+0x44`           | u32                  | unknown_44                   |       |
| `+0x48`           | u32                  | unknown_48                   |       |
| `+0x4C`           | u32                  | unknown_4c                   |       |
| `+0x50`           | u16                  | unknown_50                   |       |
| `+0x52`           | u16                  | unknown_52                   |       |
| `+0x54`           | u16                  | unknown_54                   |       |
| `+0x56`           | u16                  | unknown_56                   |       |
| `+0x58`           | u16                  | unknown_58                   |       |
| `+0x5A`           | u16                  | unknown_5a                   |       |
| `+0x5C`           | u16                  | unknown_5c                   |       |
| `+0x5E`           | u16                  | unknown_5e                   |       |
| `+0x60`           | u16                  | unknown_60                   |       |
| `+0x62`           | u32                  | unknown_62                   |       |
| `+0x66`           | u32                  | unknown_66                   |       |
| `+0x6A`           | u32                  | unknown_6a                   |       |
| `+0x6E`           | u32                  | unknown_6e                   |       |
| `+0x72`           | u16                  | limit_member_count_sunday    |       |
| `+0x74`           | u16                  | limit_member_count_monday    |       |
| `+0x76`           | u16                  | limit_member_count_tuesday   |       |
| `+0x78`           | u16                  | limit_member_count_wednesday |       |
| `+0x7A`           | u16                  | limit_member_count_thursday  |       |
| `+0x7C`           | u16                  | limit_member_count_friday    |       |
| `+0x7E`           | u32                  | start_day_count              |       |
| `+0x82`           | u32[start_day_count] | start_days                   |       |
| `start_days+0x00` | u8                   | unknown_start_days_00        |       |

## Stat Limits

The limit block, matched against the node tooltips the
[`regioninfo.bss`](regioninfo_bss.md) Notes record from my game:

| Field            | Balenos, Serendia | Calpheon, Ulukita | Valencia, Outer Edania | Tooltip                                                         |
| ---------------- | ----------------- | ----------------- | ---------------------- | --------------------------------------------------------------- |
| `hp_limit`       | 6500              | 11000             | 100000000              | HP 6,500 on occupation nodes, 11,000 on Calpheon and Ulukita    |
| `ap_limit`       | 395               | 680               | 9999                   | AP 395 on occupation nodes, 680 at Trina Fort and City of the Dead |
| `dr_limit`       | 335               | 530               | 9999                   | Damage reduction 335 and 530                                    |
| `accuracy_limit` | 650               | 820               | 9999                   | Accuracy 650 and 820                                            |
| `evasion_limit`  | 738               | 908               | 9999                   | Evasion 738 and 908                                             |
| `dr_rate_limit`  | 200000            | 300000            | 1000000                | Damage reduction rate 20% and 30%                               |
| `hp_recovery_limit` | 5              | 0                 | 0                      | HP recovery 5 on occupation nodes                               |
| `stamina_limit`  | 2100              | 0                 | 0                      | Stamina 2,100 on occupation nodes                               |

`unknown_14` and `unknown_18` sum to the "Stats (AP+DP) Limit: {sum}"
line (`LUA_VILLAGESIEGE_LIMITVALUE`) the node war menu prints from
`_siegeMaxDDForUI + _siegeMaxPVForUI`: `616` for Balenos and Serendia,
`720` for Calpheon and Ulukita (the gear limit the `regioninfo.bss` Notes
give for those nodes), and FLT_MAX for Valencia and Outer Edania, where
`isUnlimitedDDPV()` prints "No Stat Limit".

## Field Names

The table is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`TerritoryOption` in its name. The names come from the Lua of client 3482
and the node tooltips:

| Field                                   | Source                                                          |
| --------------------------------------- | --------------------------------------------------------------- |
| `territory_key_1`, `territory_key_2`, `console_territory_key` | `getTerritoryKey1Raw()`, `getTerritoryKey2Raw()`, `getConsoleTerritoryKeyRaw()`; each pair is one row of `_eTerritoryKeyRaw` pairs the Lua draws as flags, and the console key always equals one of the two |
| `limit_member_count_*`, `start_days`    | `getLimitMemberCount(day)`, `getStartDayListCount()`, `getStartDay(index)`, as in `oceansiegeterritoryoption.bss` |
| `hp_limit` to `stamina_limit`           | See Stat Limits; each value matches its tooltip line on both capped rows, or on the occupation row for HP recovery and stamina |
| `territory_1_icon_x` to `territory_2_icon_y` | `_territory1IconPos.x`, `.y` and `_territory2IconPos.x`, `.y`, which `panel_window_villagesiegemenu_all_1.luac` passes to `SetPosXY` for the two territory icons under `_ContentsGroup_SiegeRenewal2026`; the four f32 are the only x, y pairs in the row and are whole tens inside the map panel |

## Notes

- Client 3474 has the same file as client 3482. Clients 2765 to 3251
  use Layout 1 (485 bytes): the rows stop after `unknown_start_days_00`,
  with no icon positions, tail values or skills. Client 2519 has a
  shorter row (428 bytes) that no layout here reads yet.
- `unknown_skill_nos` on the Balenos and Serendia row are the skills
  `10189` to `10194` (Blessing of Taebaek and its PRI to PEN levels) and
  `10206` to `10217` (Blessing of Asadal and Fury of Asadal with theirs).
- The tooltip of an occupation node lists 20% for critical hit rate and
  damage and for back, down and air attack damage, Black Spirit's Rage
  100% and its recovery 0.15%. The first row's twelve
  `unknown_start_days_11` to `_3d` hold six `200000` (20%) values, and
  `unknown_start_days_4d` (`10000`) and `_51` (`15`) read as 100% and
  0.15% on a 10,000 = 100% scale; which value is which line is open.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: the three territory keys with their
  names, the named limits, the six day limits, the battle days by name
  and the icon positions.

## Open Questions

### Which of the AP+DP Pair Is AP

`unknown_14` and `unknown_18` are `_siegeMaxDDForUI` and
`_siegeMaxPVForUI`, but the Lua only prints their sum. The smaller value
comes first on both capped rows (`270, 346` and `309, 411`), as AP comes
before damage reduction in `ap_limit` and `dr_limit`; no source shows
the two apart.

### The Tail Values

What `unknown_start_days_11` to `unknown_start_days_51` limit: the six
pairs of `200000` and `0x7FFFFFFF`, the two values after them and the
`10000` and `15` before the stamina (see Notes), and why the other two
rows leave them unlimited.

### The Skill List

What the game does with `unknown_skill_nos` in Balenos and Serendia node
wars, which list the Taebaek and Asadal skills, and whether it turns them
off there.

### The u16 Block

`unknown_06` (`14`, `3`, `3`; `13` on client 3251), `unknown_50` to
`unknown_60` and `unknown_start_days_00` (`2`, `3`, `4`). `unknown_52`
(`3`) may be the 3 war heroes the occupation tooltip shows, which
[`siegemercenarylimitcount.bss`](siegemercenarylimitcount_bss.md) also
lists.
