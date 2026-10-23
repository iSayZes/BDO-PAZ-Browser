# `magnuseasyteleport.bss` Format

## Purpose

The destinations of the Magnus teleport map
(`panel_window_magnuseasyteleportmap.luac`): one row per destination with
its waypoint, a world position, a GAME sheet key of the territory name,
the knowledge that unlocks the button and a region. On client 3482 it
holds 16 destinations, from Velia (Balenos) to Angavu Outpost (Inner
Edania); the map shows button `CheckButton_<index + 1>` for row `index`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------- | --------- |
| 2      | 3144 and later | 3482    | `magnuseasyteleport.bss` | 1,099 | 16 Row  | 32        |
| 1      | 2438 to 3103   | 3103    | `magnuseasyteleport.bss` | 899   | 14 Row  | 28        |

| Layout | File                     | Known         | Unknown       |
| ------ | ------------------------ | ------------- | ------------- |
| 2      | `magnuseasyteleport.bss` | 971 B (88.4%) | 128 B (11.6%) |
| 1      | `magnuseasyteleport.bss` | 787 B (87.5%) | 112 B (12.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3454   | Layout 2 |
| 3412   | Layout 2 |
| 3381   | Layout 2 |
| 3349   | Layout 2 |
| 3314   | Layout 2 |
| 3283   | Layout 2 |
| 3251   | Layout 2 |
| 3212   | Layout 2 |
| 3177   | Layout 2 |
| 3144   | Layout 2 |
| 3103   | Layout 1 |
| 3062   | Layout 1 |
| 3037   | Layout 1 |
| 3002   | Layout 1 |
| 2959   | Layout 1 |
| 2923   | Layout 1 |
| 2900   | Layout 1 |
| 2872   | Layout 1 |
| 2834   | Layout 1 |
| 2803   | Layout 1 |
| 2765   | Layout 1 |
| 2736   | Layout 1 |
| 2703   | Layout 1 |
| 2665   | Layout 1 |
| 2637   | Layout 1 |
| 2606   | Layout 1 |
| 2583   | Layout 1 |
| 2545   | Layout 1 |
| 2519   | Layout 1 |
| 2498   | Layout 1 |
| 2468   | Layout 1 |
| 2438   | Layout 1 |
| 2414   | No file  |
| 2384   | No file  |
| 2358   | No file  |
| 2335   | No file  |
| 2313   | No file  |
| 2290   | No file  |
| 2250   | No file  |
| 2224   | No file  |
| 2203   | No file  |
| 2179   | No file  |
| 2151   | No file  |
| 2134   | No file  |
| 2107   | No file  |
| 2073   | No file  |
| 2052   | No file  |
| 2011   | No file  |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
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
| 1137   | No file  |
| 1132   | No file  |
| 1127   | No file  |
| 1122   | No file  |
| 1118   | No file  |
| 1114   | No file  |
| 1109   | No file  |
| 1102   | No file  |
| 1096   | No file  |
| 1088   | No file  |
| 1081   | No file  |
| 1076   | No file  |
| 1069   | No file  |
| 1064   | No file  |
| 1058   | No file  |
| 1051   | No file  |
| 1044   | No file  |
| 1036   | No file  |
| 1026   | No file  |
| 1016   | No file  |
| 1009   | No file  |
| 1005   | No file  |
| 1000   | No file  |
| 998    | No file  |
| 990    | No file  |
| 979    | No file  |
| 972    | No file  |
| 963    | No file  |
| 955    | No file  |
| 946    | No file  |
| 938    | No file  |
| 927    | No file  |
| 911    | No file  |
| 904    | No file  |
| 899    | No file  |
| 894    | No file  |
| 885    | No file  |
| 879    | No file  |
| 872    | No file  |
| 864    | No file  |
| 855    | No file  |
| 853    | No file  |
| 845    | No file  |
| 837    | No file  |
| 829    | No file  |
| 822    | No file  |
| 814    | No file  |
| 805    | No file  |
| 794    | No file  |
| 787    | No file  |
| 780    | No file  |
| 771    | No file  |
| 760    | No file  |
| 748    | No file  |
| 741    | No file  |
| 736    | No file  |
| 731    | No file  |
| 723    | No file  |
| 711    | No file  |
| 707    | No file  |
| 697    | No file  |
| 689    | No file  |
| 683    | No file  |
| 678    | No file  |
| 670    | No file  |
| 661    | No file  |
| 656    | No file  |
| 652    | No file  |
| 643    | No file  |
| 637    | No file  |
| 630    | No file  |
| 627    | No file  |
| 621    | No file  |
| 617    | No file  |
| 615    | No file  |
| 606    | No file  |
| 599    | No file  |
| 592    | No file  |
| 586    | No file  |
| 577    | No file  |
| 569    | No file  |
| 561    | No file  |
| 554    | No file  |
| 542    | No file  |
| 532    | No file  |
| 531    | No file  |
| 526    | No file  |
| 521    | No file  |
| 517    | No file  |
| 510    | No file  |
| 508    | No file  |
| 504    | No file  |
| 497    | No file  |
| 491    | No file  |
| 485    | No file  |
| 478    | No file  |
| 472    | No file  |
| 466    | No file  |
| 457    | No file  |
| 452    | No file  |
| 449    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                              |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Node names (LOC type 29), knowledge names (LOC type 34), region names (LOC type 17), territory names (LOC type 37 under the GAME sheet key hash) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of destinations; `ToClient_GetMagnusEasyTeleportInfoCount()` |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (32 bytes)

| Offset  | Type | Field           | Notes                                                                                   |
| ------- | ---- | --------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u16  | waypoint_key    | Node key (LOC type 29 name) near the destination                                       |
| `+0x02` | f32  | x               | World X of the destination                                                              |
| `+0x06` | f32  | y               | World Y (height)                                                                        |
| `+0x0A` | f32  | z               | World Z                                                                                 |
| `+0x0E` | u32  | name_ref        | String-table index of the GAME sheet key of the button text; `getName()`                |
| `+0x12` | u32  | mental_card_key | `getMentalCardKeyRaw()`, the knowledge (LOC type 34) whose card shows the button        |
| `+0x16` | u64  | unknown_16      | `1` on every row of client 3482                                                         |
| `+0x1E` | u16  | region_key      | `regioninfo.bss` region key (LOC type 17); see Field Names                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                           |
| ------- | ------------------ | ------------ | --------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; one per row                                  |
| `+0x04` | pstr[string_count] | strings      | UTF-8 GAME sheet keys (`LUA_WORLDMAP_TERRITORYSTRING_0`), in row order |

## Layout 1

### Row (28 bytes)

| Offset  | Type | Field        | Notes                                                        |
| ------- | ---- | ------------ | ------------------------------------------------------------ |
| `+0x00` | u16  | waypoint_key | Node key near the destination                                |
| `+0x02` | f32  | x            | World X of the destination                                   |
| `+0x06` | f32  | y            | World Y (height)                                             |
| `+0x0A` | f32  | z            | World Z                                                      |
| `+0x0E` | u32  | name_ref     | String-table index of the GAME sheet key of the button text  |
| `+0x12` | u64  | unknown_16   | `1` on every row; no `mental_card_key` before it             |
| `+0x1A` | u16  | region_key   | `regioninfo.bss` region key                                  |

## Destinations

Client 3482, in file order, with the LOC names.

| Row | `waypoint_key`              | `name_ref` text                     | `mental_card_key`              | `region_key`               |
| --- | --------------------------- | ----------------------------------- | ------------------------------ | -------------------------- |
| 0   | 1 Velia                     | Balenos                             | 3001 Velia                     | 16 Bartali Farm            |
| 1   | 308 Eastern Border          | Serendia                            | 3058 Heidel, Serendia          | 318 Moretti Plantation     |
| 2   | 661 Falres Dirt Farm        | Calpheon                            | 3177 Calpheon                  | 300 Gabino Farm            |
| 3   | 1147 Stonebeak Shore        | Mediah                              | 3188 Altinova                  | 236 Altinova Gateway       |
| 4   | 1356 Fohalam Farm           | Valencia                            | 3364 Valencia City             | 639 Erdal Farm             |
| 5   | 1622 Lake Flondor           | Kamasylvia                          | 3454 Grána                     | 735 Grána                  |
| 6   | 1741 Salanar Pond           | O'dyllita                           | 3494 O'draxxia                 | 1023 Delmira Plantation    |
| 7   | 1649 Duvencrune             | Drieghan                            | 3472 Duvencrune                | 903 Marak Farm             |
| 8   | 1762 Zvier Highlands        | Mountain of Eternal Winter          | 3537 Eilton                    | 1121 Erethea's Belt        |
| 9   | 1785 Nampo's Moodle Village | Land of the Morning Light - Nampo   | 3573 Nampo's Moodle Village    | 1319 Chief's Home          |
| 10  | 1843 Muzgar                 | Ulukita                             | 3594 Muzgar                    | 1375 Muzgar                |
| 11  | 1727 Oquilla's Eye          | Oquilla's Eye                       | 3001 Velia                     | 1000 Oquilla's Eye         |
| 12  | 1853 Yukjo Street           | Land of the Morning Light - Seoul   | 3626 Seoul                     | 1420 Yukjo Street          |
| 13  | 2001 Hakinza Sanctuary      | Outer Edania                        | 14195 Hakinza Sanctuary        | 1553 Hakinza Sanctuary     |
| 14  | 2052 Olvia Academy          | Olvia Academy                       | 14691 Olvia Academy            | 1677 Olvia Academy Grounds |
| 15  | 2057 Angavu Outpost         | Inner Edania                        | 15127 Angavu Outpost           | 1733 Angavu Outpost        |

## Field Names

The Magnus is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers this file. The client 3482 Lua
reads each row with `ToClient_GetMagnusEasyTeleportInfoByIndex(idx)` and
three getters, `getName()`, `getMentalCardKeyRaw()` and
`getRegionKeyRaw()`:

- `name_ref`: `PAGetString(Defines.StringSheet_GAME, info:getName())`
  sets the button text, and every string is a GAME sheet key.
- `mental_card_key`: `ToClinet_getMentalCardStaticStatus(mentalCardKeyRaw):isHasCard()`
  shows the button; every value has a LOC type 34 knowledge name, on 15
  of 16 rows the city of the destination (row 11, Oquilla's Eye, holds
  Velia `3001`, as row 0 does).
- `waypoint_key`: every value has a LOC type 29 node name, and the node's
  world position in `exploration.bss` lies near `x` and `z` (Velia node
  `1` at `13800, 76996` against `-4222, 75613`; Eastern Border `308` at
  `99370, -39348` against `100689, -38203`).
- `region_key`: every value has a LOC type 17 region name, and the 16
  values are the 16 `region_key_1` values of
  [`abyssmovecost.bss`](abyssmovecost_bss.md#free-moves), the Magnus move
  regions.
- `x`, `y` and `z` read as a world position by the node distances above.

`getRegionKeyRaw()` goes to `ToClient_getRegionInfoWrapperByWaypoint`,
which takes a waypoint key; whether it returns `waypoint_key` or
`region_key` is open (see Open Questions).

## Notes

- Layout 1 (clients 2438 to 3103) has no `mental_card_key`; client 3103
  lists 14 destinations.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`.

## Open Questions

### Which Key getRegionKeyRaw Returns

The Lua passes `getRegionKeyRaw()` to
`ToClient_getRegionInfoWrapperByWaypoint` and skips the row when no
region comes back. `waypoint_key` holds node keys, which that call takes;
`region_key` holds region keys, which match the getter's name. `unknown_16`
is `1` on every row and is the only other unnamed field.
