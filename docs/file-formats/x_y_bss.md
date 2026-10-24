# `x_y.bss` Format

## Purpose

The spawn grid cells: the client copy of the NPC and monster spawn
placements of one field, cut into files by grid square. Each file sits at
`mapdata_<resource>/spawnplacementfieldgrid/<field_no>/7/<x>_<z>.bss` and is
named after its first grid square; the browser lists the family as
`x_y.bss`. `<field_no>` is the [fieldinfo.bss](fieldinfo_bss.md) field
number (its `resource_name` `_real` or `_instancedungeon/4001` gives the
`mapdata_` folder). A spawn holds its placement key, a world position and
direction, the character key, the spawn delays, the NPC's action and dialog
index, waypoint keys, a home position and optional spawn hours.

On client 3482 field `1` (the open world) has 1,430 cell files with 95,787
spawns, field `700` (`칼페온 크자카 인던`, the Calpheon Kzarka instance) one
file with 20 and field `701` (`아쳐 튜토리얼 인던`) two files with 16. The 66
`A1_` fields `4001` to `4066` have the folder with its two list files and
no cells.

The two list files of each folder have their own docs:
[fieldgridinfo.bss](fieldgridinfo_bss.md) lists the grid squares that hold
spawns, [fileinfo.bss](fileinfo_bss.md) the cell files.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                                                   | Bytes  | Records                                               | Row bytes |
| ------ | ------------- | ------- | ------------------------------------------------------ | ------ | ----------------------------------------------------- | --------- |
| 1      | 845 and later | 3483    | `mapdata_real/spawnplacementfieldgrid/1/7/651_259.bss` | 28,752 | 780 Waypoint, 176 Spawn, 14 Square, 34 Index Position | 5         |

| Layout | File                                                   | Known            | Unknown         |
| ------ | ------------------------------------------------------ | ---------------- | --------------- |
| 1      | `mapdata_real/spawnplacementfieldgrid/1/7/651_259.bss` | 22,700 B (79.0%) | 6,052 B (21.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3482   | No file  |
| 3474   | No file  |
| 3473   | No file  |
| 3464   | No file  |
| 3458   | No file  |
| 3454   | No file  |
| 3444   | No file  |
| 3435   | No file  |
| 3426   | No file  |
| 3418   | No file  |
| 3412   | No file  |
| 3402   | No file  |
| 3396   | No file  |
| 3387   | No file  |
| 3381   | No file  |
| 3373   | No file  |
| 3364   | No file  |
| 3356   | No file  |
| 3349   | No file  |
| 3342   | No file  |
| 3335   | No file  |
| 3326   | No file  |
| 3321   | No file  |
| 3314   | No file  |
| 3303   | No file  |
| 3302   | No file  |
| 3293   | No file  |
| 3283   | No file  |
| 3275   | No file  |
| 3267   | No file  |
| 3258   | No file  |
| 3251   | No file  |
| 3242   | No file  |
| 3235   | No file  |
| 3229   | No file  |
| 3212   | No file  |
| 3203   | No file  |
| 3193   | No file  |
| 3186   | No file  |
| 3177   | No file  |
| 3169   | No file  |
| 3158   | No file  |
| 3151   | No file  |
| 3144   | No file  |
| 3133   | Layout 1 |
| 3125   | Layout 1 |
| 3118   | Layout 1 |
| 3111   | Layout 1 |
| 3103   | Layout 1 |
| 3095   | Layout 1 |
| 3086   | Layout 1 |
| 3072   | Layout 1 |
| 3062   | Layout 1 |
| 3052   | Layout 1 |
| 3045   | Layout 1 |
| 3037   | Layout 1 |
| 3030   | Layout 1 |
| 3021   | Layout 1 |
| 3012   | Layout 1 |
| 3002   | Layout 1 |
| 2995   | Layout 1 |
| 2987   | Layout 1 |
| 2978   | Layout 1 |
| 2970   | Layout 1 |
| 2959   | Layout 1 |
| 2951   | No file  |
| 2942   | No file  |
| 2935   | No file  |
| 2932   | No file  |
| 2923   | No file  |
| 2919   | No file  |
| 2907   | No file  |
| 2900   | No file  |
| 2891   | No file  |
| 2882   | No file  |
| 2872   | No file  |
| 2863   | No file  |
| 2855   | No file  |
| 2849   | No file  |
| 2844   | No file  |
| 2834   | No file  |
| 2825   | No file  |
| 2819   | No file  |
| 2811   | No file  |
| 2803   | No file  |
| 2794   | No file  |
| 2783   | No file  |
| 2774   | No file  |
| 2765   | No file  |
| 2756   | No file  |
| 2750   | No file  |
| 2743   | No file  |
| 2736   | No file  |
| 2726   | No file  |
| 2717   | No file  |
| 2709   | No file  |
| 2703   | No file  |
| 2695   | No file  |
| 2684   | No file  |
| 2672   | No file  |
| 2665   | No file  |
| 2657   | No file  |
| 2649   | No file  |
| 2644   | No file  |
| 2637   | No file  |
| 2629   | No file  |
| 2619   | No file  |
| 2612   | No file  |
| 2606   | No file  |
| 2602   | No file  |
| 2601   | No file  |
| 2592   | No file  |
| 2583   | No file  |
| 2575   | No file  |
| 2567   | No file  |
| 2560   | Layout 1 |
| 2553   | Layout 1 |
| 2545   | Layout 1 |
| 2538   | Layout 1 |
| 2529   | Layout 1 |
| 2519   | Layout 1 |
| 2513   | Layout 1 |
| 2510   | Layout 1 |
| 2507   | Layout 1 |
| 2503   | Layout 1 |
| 2498   | Layout 1 |
| 2492   | Layout 1 |
| 2487   | Layout 1 |
| 2480   | Layout 1 |
| 2474   | Layout 1 |
| 2468   | Layout 1 |
| 2460   | Layout 1 |
| 2453   | Layout 1 |
| 2444   | No file  |
| 2438   | No file  |
| 2434   | No file  |
| 2429   | No file  |
| 2421   | No file  |
| 2414   | No file  |
| 2407   | No file  |
| 2401   | No file  |
| 2397   | No file  |
| 2393   | No file  |
| 2384   | No file  |
| 2378   | No file  |
| 2372   | No file  |
| 2358   | No file  |
| 2352   | No file  |
| 2347   | No file  |
| 2343   | No file  |
| 2335   | No file  |
| 2327   | No file  |
| 2324   | No file  |
| 2319   | No file  |
| 2313   | No file  |
| 2308   | No file  |
| 2302   | No file  |
| 2295   | No file  |
| 2290   | No file  |
| 2284   | No file  |
| 2276   | No file  |
| 2269   | No file  |
| 2259   | No file  |
| 2250   | No file  |
| 2243   | No file  |
| 2235   | No file  |
| 2229   | No file  |
| 2224   | No file  |
| 2218   | No file  |
| 2215   | No file  |
| 2207   | No file  |
| 2203   | No file  |
| 2196   | No file  |
| 2192   | No file  |
| 2189   | No file  |
| 2183   | No file  |
| 2179   | No file  |
| 2171   | No file  |
| 2163   | No file  |
| 2156   | No file  |
| 2151   | No file  |
| 2147   | No file  |
| 2142   | No file  |
| 2138   | No file  |
| 2134   | No file  |
| 2130   | No file  |
| 2122   | No file  |
| 2107   | No file  |
| 2098   | No file  |
| 2089   | No file  |
| 2081   | No file  |
| 2073   | No file  |
| 2067   | No file  |
| 2063   | No file  |
| 2059   | No file  |
| 2052   | No file  |
| 2044   | No file  |
| 2039   | No file  |
| 2032   | No file  |
| 2025   | No file  |
| 2011   | No file  |
| 2005   | No file  |
| 2000   | No file  |
| 1996   | No file  |
| 1991   | No file  |
| 1985   | No file  |
| 1980   | No file  |
| 1969   | No file  |
| 1964   | No file  |
| 1958   | No file  |
| 1950   | No file  |
| 1945   | No file  |
| 1937   | No file  |
| 1933   | No file  |
| 1927   | No file  |
| 1921   | Layout 1 |
| 1914   | Layout 1 |
| 1908   | Layout 1 |
| 1897   | Layout 1 |
| 1892   | Layout 1 |
| 1886   | Layout 1 |
| 1881   | Layout 1 |
| 1871   | Layout 1 |
| 1866   | Layout 1 |
| 1862   | Layout 1 |
| 1854   | Layout 1 |
| 1846   | Layout 1 |
| 1838   | Layout 1 |
| 1832   | Layout 1 |
| 1826   | Layout 1 |
| 1822   | Layout 1 |
| 1818   | Layout 1 |
| 1804   | Layout 1 |
| 1794   | Layout 1 |
| 1790   | Layout 1 |
| 1784   | No file  |
| 1774   | Layout 1 |
| 1771   | Layout 1 |
| 1762   | Layout 1 |
| 1759   | Layout 1 |
| 1754   | No file  |
| 1749   | No file  |
| 1743   | No file  |
| 1737   | No file  |
| 1731   | No file  |
| 1725   | No file  |
| 1717   | No file  |
| 1710   | No file  |
| 1704   | No file  |
| 1698   | No file  |
| 1690   | No file  |
| 1685   | No file  |
| 1680   | No file  |
| 1674   | No file  |
| 1668   | No file  |
| 1659   | No file  |
| 1649   | No file  |
| 1642   | No file  |
| 1636   | No file  |
| 1628   | No file  |
| 1622   | No file  |
| 1614   | No file  |
| 1608   | No file  |
| 1602   | No file  |
| 1598   | No file  |
| 1594   | No file  |
| 1590   | No file  |
| 1587   | No file  |
| 1584   | No file  |
| 1579   | No file  |
| 1572   | No file  |
| 1565   | No file  |
| 1559   | No file  |
| 1554   | No file  |
| 1547   | No file  |
| 1537   | No file  |
| 1529   | No file  |
| 1524   | No file  |
| 1519   | No file  |
| 1509   | No file  |
| 1506   | No file  |
| 1504   | No file  |
| 1500   | No file  |
| 1493   | No file  |
| 1489   | No file  |
| 1485   | No file  |
| 1481   | No file  |
| 1474   | No file  |
| 1466   | No file  |
| 1462   | No file  |
| 1459   | No file  |
| 1453   | No file  |
| 1450   | No file  |
| 1445   | No file  |
| 1439   | No file  |
| 1433   | No file  |
| 1430   | No file  |
| 1426   | No file  |
| 1421   | No file  |
| 1417   | No file  |
| 1416   | No file  |
| 1409   | No file  |
| 1405   | No file  |
| 1401   | No file  |
| 1396   | No file  |
| 1391   | No file  |
| 1390   | No file  |
| 1386   | No file  |
| 1381   | No file  |
| 1379   | No file  |
| 1372   | No file  |
| 1366   | No file  |
| 1364   | No file  |
| 1363   | No file  |
| 1360   | No file  |
| 1358   | No file  |
| 1355   | No file  |
| 1351   | No file  |
| 1348   | No file  |
| 1346   | No file  |
| 1341   | No file  |
| 1340   | No file  |
| 1338   | No file  |
| 1335   | No file  |
| 1333   | No file  |
| 1329   | No file  |
| 1327   | No file  |
| 1324   | No file  |
| 1321   | No file  |
| 1319   | No file  |
| 1318   | No file  |
| 1316   | No file  |
| 1313   | No file  |
| 1311   | No file  |
| 1309   | No file  |
| 1304   | No file  |
| 1292   | No file  |
| 1286   | No file  |
| 1280   | No file  |
| 1276   | No file  |
| 1267   | No file  |
| 1261   | No file  |
| 1256   | No file  |
| 1250   | No file  |
| 1246   | No file  |
| 1239   | No file  |
| 1230   | No file  |
| 1226   | No file  |
| 1220   | No file  |
| 1217   | No file  |
| 1211   | No file  |
| 1210   | No file  |
| 1208   | No file  |
| 1203   | No file  |
| 1197   | No file  |
| 1194   | No file  |
| 1192   | No file  |
| 1187   | No file  |
| 1183   | No file  |
| 1177   | No file  |
| 1173   | No file  |
| 1167   | No file  |
| 1164   | No file  |
| 1156   | No file  |
| 1149   | No file  |
| 1144   | No file  |
| 1137   | No file  |
| 1132   | No file  |
| 1127   | Layout 1 |
| 1122   | Layout 1 |
| 1118   | Layout 1 |
| 1114   | Layout 1 |
| 1109   | Layout 1 |
| 1102   | Layout 1 |
| 1096   | Layout 1 |
| 1088   | Layout 1 |
| 1081   | Layout 1 |
| 1076   | Layout 1 |
| 1069   | Layout 1 |
| 1064   | Layout 1 |
| 1058   | Layout 1 |
| 1051   | Layout 1 |
| 1044   | Layout 1 |
| 1036   | Layout 1 |
| 1026   | Layout 1 |
| 1016   | Layout 1 |
| 1009   | Layout 1 |
| 1005   | Layout 1 |
| 1000   | No file  |
| 998    | Layout 1 |
| 990    | Layout 1 |
| 979    | Layout 1 |
| 972    | Layout 1 |
| 963    | Layout 1 |
| 955    | Layout 1 |
| 946    | Layout 1 |
| 938    | Layout 1 |
| 927    | Layout 1 |
| 911    | Layout 1 |
| 904    | Layout 1 |
| 899    | Layout 1 |
| 894    | Layout 1 |
| 885    | Layout 1 |
| 879    | Layout 1 |
| 872    | Layout 1 |
| 864    | Layout 1 |
| 855    | Layout 1 |
| 853    | Layout 1 |
| 845    | Layout 1 |
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

| File                         | Required | Role                                                                    |
| ---------------------------- | -------- | ----------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a character key without a row shows as plain text |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR with no row count: the squares run up to the string table, whose
offset the trailer holds.

| Offset         | Type                  | Field        | Notes                                              |
| -------------- | --------------------- | ------------ | -------------------------------------------------- |
| `+0x00`        | char[4]               | magic        | ASCII `PABR`                                       |
| `+0x04`        | Square[..table_start] | squares      | Squares back to back until `table_start`; see Square |
| `squares+0x00` | String Table          | string_table | See String Table                                   |
| `EOF-0x08`     | u32                   | table_start  | Offset of the string table, where `squares` ends   |
| `EOF-0x04`     | u32                   | zero         | Always `0`                                         |

### Square (variable: 8 bytes + spawns)

| Offset  | Type               | Field       | Notes                                                                 |
| ------- | ------------------ | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u16                | grid_x      | Field grid square column; see [Grid Squares](#grid-squares)           |
| `+0x02` | u16                | grid_z      | Field grid square row                                                 |
| `+0x04` | u32                | spawn_count | Number of `spawns`, at least `1`                                      |
| `+0x08` | Spawn[spawn_count] | spawns      | See Spawn                                                             |

### Spawn (variable: 135 bytes + character key and lists)

| Offset                  | Type                                        | Field                     | Notes                                                                                 |
| ----------------------- | ------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| `+0x00`                 | u8                                          | is_spawnable              | `1` or `0`                                                                            |
| `+0x01`                 | u16                                         | key_index                 | Spawn number within its sector and type; with the next four fields the XML `Key`      |
| `+0x03`                 | i16                                         | key_sector_z              | Sector (12,800 units) row of the spawn's source file                                  |
| `+0x05`                 | i16                                         | key_sector_x              | Sector column of the spawn's source file                                              |
| `+0x07`                 | u8                                          | key_type                  | Source file kind: `2` `_Monster.xml`, `3` `_Npc.xml`; `11` on 9 field 700 and 701 spawns |
| `+0x08`                 | u8                                          | unknown_08                | `0` on every spawn                                                                    |
| `+0x09`                 | f32                                         | position_x                | World position                                                                        |
| `+0x0D`                 | f32                                         | position_y                | Height                                                                                |
| `+0x11`                 | f32                                         | position_z                |                                                                                       |
| `+0x15`                 | u16                                         | spawn_range               | `0` on 95,587 spawns                                                                  |
| `+0x17`                 | f32                                         | direction                 | Facing in radians                                                                     |
| `+0x1B`                 | u16                                         | unknown_1b                | `0` on every spawn                                                                    |
| `+0x1D`                 | u8                                          | has_character             | `1` when `character_key` follows; see Notes                                           |
| `+0x1E`                 | u16 if has_character = 1                    | character_key             | `characterstatic.dbss` key                                                            |
| `character_key+0x00`    | i32                                         | scene_sector_x            | Sector of a linked scene object; `0` with `scene_type` `0`                            |
| `character_key+0x04`    | i32                                         | scene_sector_y            |                                                                                       |
| `character_key+0x08`    | i32                                         | scene_sector_z            |                                                                                       |
| `character_key+0x0C`    | u16                                         | scene_type                | `2` on 720 spawns, else `0`                                                           |
| `character_key+0x0E`    | u16                                         | scene_index               | Object number in that sector                                                          |
| `character_key+0x10`    | u32                                         | unknown_character_key_10  | `1` on every spawn; see Field Names                                                   |
| `character_key+0x14`    | u32                                         | unknown_character_key_14  | `0` on every spawn                                                                    |
| `character_key+0x18`    | u32                                         | unknown_character_key_18  | `0` on every spawn                                                                    |
| `character_key+0x1C`    | u8                                          | unknown_character_key_1c  | `0` on every spawn                                                                    |
| `character_key+0x1D`    | u32                                         | spawn_delay_time          | Milliseconds; `120000` or `60000`                                                     |
| `character_key+0x21`    | u32                                         | spawn_delay_variable_time | Milliseconds; a quarter of `spawn_delay_time` on every spawn                     |
| `character_key+0x25`    | u8                                          | unknown_character_key_25  | `1` on every spawn                                                                    |
| `character_key+0x26`    | bytes[3]                                    | unknown_character_key_26  | `0` on every spawn                                                                    |
| `character_key+0x29`    | u32                                         | respawn_number            | `0` on all but 4 spawns                                                               |
| `character_key+0x2D`    | u8                                          | unknown_character_key_2d  | `0` on every spawn                                                                    |
| `character_key+0x2E`    | u32                                         | event_object_key          | `157` on one spawn, else `0`                                                          |
| `character_key+0x32`    | u32                                         | unknown_character_key_32  | `0` on every spawn                                                                    |
| `character_key+0x36`    | u32                                         | live_world_event_key      | `4`, `7`, `98` and `207` on one spawn each, else `0`                                  |
| `character_key+0x3A`    | i16                                         | territory                 | `-1` for none; `0`, `1` or `2` on 758 spawns                                          |
| `character_key+0x3C`    | u32                                         | action_index              | NPC action                                                                            |
| `character_key+0x40`    | u16                                         | dialog_index              | NPC dialog                                                                            |
| `character_key+0x42`    | u32                                         | dialog_update_time        | Milliseconds; `0` on 94,727 spawns                                                    |
| `character_key+0x46`    | bytes[4]                                    | unknown_character_key_46  | `0` on every spawn                                                                    |
| `character_key+0x4A`    | i32                                         | team_no                   | `-1` on 3,135 spawns, `0` on most                                                     |
| `character_key+0x4E`    | i32                                         | unknown_character_key_4e  | `-1` where `team_no` is `-1` or `-660`, else `0`                                      |
| `character_key+0x52`    | f32                                         | house_x                   | NPC home position; `0, 0, 0` on all but 1,035 spawns                                                   |
| `character_key+0x56`    | f32                                         | house_y                   |                                                                                       |
| `character_key+0x5A`    | f32                                         | house_z                   |                                                                                       |
| `character_key+0x5E`    | u32                                         | waypoint_count            | Number of `waypoints`: `5` or `0`                                                     |
| `character_key+0x62`    | Waypoint[waypoint_count]                    | waypoints                 | See Waypoint                                                                          |
| `waypoints+0x00`        | u8                                          | go_home_type              | `0`, `1` or `2`                                                                       |
| `waypoints+0x01`        | u8                                          | unknown_waypoints_01      | `0` on every spawn                                                                    |
| `waypoints+0x02`        | u32                                         | index_position_count      | Number of `index_positions`, `0` or `1`                                               |
| `waypoints+0x06`        | Index Position[index_position_count]        | index_positions           | See Index Position                                                                    |
| `index_positions+0x00`  | u8                                          | condition_count           | Number of `conditions`, `0` or `1`                                                    |
| `index_positions+0x01`  | Spawn Condition[condition_count]            | conditions                | See Spawn Condition                                                                   |

### Waypoint (5 bytes)

| Offset  | Type | Field        | Notes                                                                                   |
| ------- | ---- | ------------ | --------------------------------------------------------------------------------------- |
| `+0x00` | u8   | using_type   | `gc::SpawnWaypointUsingType`: `1` go home, `2` go back, `3` to `5` roaming 1 to 3; every list holds `1` to `5` in order |
| `+0x01` | i32  | waypoint_key | `0` for none; the go back key is the negated go home key on every spawn with both       |

### Index Position (18 bytes)

| Offset  | Type | Field      | Notes                          |
| ------- | ---- | ---------- | ------------------------------ |
| `+0x00` | u16  | unknown_00 | `0` on all 34 entries          |
| `+0x02` | f32  | x          | World position                 |
| `+0x06` | f32  | y          |                                |
| `+0x0A` | f32  | z          |                                |
| `+0x0E` | f32  | direction  | Radians                        |

### Spawn Condition (5 bytes)

| Offset  | Type | Field            | Notes                                   |
| ------- | ---- | ---------------- | --------------------------------------- |
| `+0x00` | u8   | unknown_00       | `0` on all 64 entries                   |
| `+0x01` | i16  | spawn_start_hour | `2` on 50 entries, `-1` on 13, `20` on 1 |
| `+0x03` | i16  | spawn_end_hour   | `22` on 50 entries, `-1` on 13, `2` on 1 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | `0` in every file                    |
| `+0x04` | pstr[string_count] | strings      | No field reads a string              |

Counts and values in the Notes cells are from the 1,433 cell files of
client 3482 (95,823 spawns).

## Grid Squares

A field grid square is 3,700 world units on a side, counted from the
field's `world_start_x` and `world_start_z` in
[fieldinfo.bss](fieldinfo_bss.md): square (`grid_x`, `grid_z`) covers
`world_start_x + grid_x * 3700` up to the next square in x, and the same in
z. Field `1` starts at (-2,035,200, -1,113,600), the corner of sector
(-159, -87). On client 3482 every one of the 95,787 field `1` spawns lies
inside the square it is listed under, and 3,700 is the only square size
from 3,600.0 to 3,800.0 (in steps of 0.1) that places them all. The
[instancefield.dbss](instancefield_dbss.md) loader of a private server on
client 1784 multiplies `field_grid_sector_count` by the same 3,700.

A cell file covers 7 x 7 squares, 25,900 units on a side: its name is its
first square, a multiple of 7 on both axes (the folder `7`), and every
square in `553_364.bss` has a `grid_x` of 553 to 559 and a `grid_z` of 364
to 370. This holds for all 1,433 files of client 3482.

The key's sector is the 12,800-unit sector of the spawn's source file
(`<sector_x>_0_<sector_z>_Npc.xml`); `position_x` and `position_z` fall
inside it on 95,785 of the 95,787 field `1` spawns.

## Field Names

The names follow the `SpawnPlacement` XML a private server on client 1784
compiles these files from (`Spawnplacement/MapData_real/1/<x>_0_<z>_<Kind>.xml`,
925,171 entries, most of them gathering points that the grid leaves out).
Its `Key` attribute is the spawn's eight key bytes read as a u64; 57,557 of
the 95,787 field `1` spawns of client 3482 have their key there. Matches
over those keys, by value:

| Field                                   | XML                                         | Match (client 3482)        |
| --------------------------------------- | ------------------------------------------- | -------------------------- |
| `is_spawnable`                          | `IsSpawnable`                               | 57,301 of 57,557           |
| `position_x`, `position_y`, `position_z` | `Position` `X`, `Y`, `Z`                    | 57,346, 57,345 and 57,331 of 57,557 |
| `spawn_range`                           | `Position` `SpawnRange`                     | 57,554 of 57,557           |
| `direction`                             | `Direction`                                 | 57,417 of 57,557           |
| `character_key`                         | `UseSpawnGroup` `SpawnCharacterKey`         | 57,434 of 57,557           |
| `scene_sector_x` to `scene_index`       | `UseSpawnGroup` `SceneUID_X`, `_Y`, `_Z`, `_Type`, `_Index` | 214 of 217 each |
| `spawn_delay_time`                      | `SpawnDelay` `Time`                         | 57,552 of 57,557           |
| `spawn_delay_variable_time`             | `SpawnDelay` `VariableTime`                 | 57,552 of 57,557           |
| `respawn_number`                        | `ReSpawnNumber`                             | 57,557 of 57,557, 3 of them not `0` |
| `event_object_key`                      | `EventObjectKey`                            | 1 of 1                     |
| `live_world_event_key`                  | `LiveWorldEventKey`                         | 1 of 1                     |
| `territory`                             | `Territory`                                 | 745 of 745                 |
| `action_index`                          | `ActionIndex`                               | 52,465 of 52,544           |
| `dialog_index`                          | `DialogIndex`                               | 30,303 of 30,309           |
| `dialog_update_time`                    | `DialogUpdateTime`                          | 1,041 of 1,041             |
| `team_no`                               | `TeamNo`                                    | 2,575 of 2,578             |
| `house_x`, `house_y`, `house_z`         | `House` `X`, `Y`, `Z`                       | 1,034 of 1,035             |
| `waypoint_key` of `using_type` 1 and 2  | `gohome`, `goback`                          | 764 of 766 each            |
| `go_home_type`                          | `GoHomeType`                                | 57,555 of 57,557           |
| Index Position `x` to `direction`       | `SpawnIndexPosition` `X`, `Y`, `Z`, `Direction` | 34 of 34               |
| `spawn_start_hour`, `spawn_end_hour`    | `CustomSpawnCondition` `SpawnStartHour`, `SpawnEndHour` | 64 of 64       |

The misses are keys whose values differ between clients 1784 and 3482. `key_type`
follows the source file name: on the shared keys every `2` comes from a
`_Monster.xml` (715) and every `3` from a `_Npc.xml` (56,842).
`using_type` takes its names from the 2016 `gc::SpawnWaypointUsingType`
(`SWUT_GOHOME` 1, `SWUT_GOBACK` 2, `SWUT_ROAMING1` to `SWUT_ROAMING3` 3 to
5); slots 1 and 2 hold the XML `gohome` and `goback` keys. The grid
squares are the 2016 `gc::FieldGridSectorIndex` (u16 `_x`, u16 `_z`), and
the scene fields the 2016 `PASceneUID` (three i32 sector indexes and two
u16), whose u16 order (`m_nSceneIndex` then `m_nSceneType`) is the reverse
of what the XML values show.

Several fields sit where an XML attribute would go but hold one value on
every spawn and in the XML, so the value cannot place them; they stay
`unknown_*` with their lead:

| Field                      | Lead                                                                 |
| -------------------------- | -------------------------------------------------------------------- |
| `unknown_character_key_10` | `UseSpawnGroup` `SpawnQuantity`, `1` on every entry                  |
| `unknown_character_key_14` | `SpawnDelay` `BootTime`, `0` on every entry                          |
| `unknown_character_key_18` | `SpawnDelay` `BootVariableTime`, `0` on every entry                  |
| `unknown_character_key_25` | `SpawnDelay` `IsSpawnOnBoot`, `1` on every entry                     |
| `unknown_character_key_26` | `SpawnDelay` `IsSpawnOnRealTime` and `IsMainChannelSync`, `0` on every entry |
| Index Position `unknown_00` | `SpawnIndexPosition` `PageIndex`, `0` on every entry                |
| Spawn Condition `unknown_00` | `CustomSpawnCondition` `SpawnConditionType`, `0` on every entry    |

## Notes

- `has_character` is `0` on 47 spawns of client 3482 (38 in field `1`, the
  9 `key_type` `11` spawns of fields 700 and 701), and those spawns have no
  `character_key` bytes. In field `1` their XML entries name characters
  `986` (32 spawns), `759` (4) and `59622` (2), none of which has a
  `characterstatic.dbss` row on client 3482. The private server's copy on
  client 1784 also leaves out `23411` (296 spawns), which client 3482
  writes and has a row for. The key seems to be written only when the
  character exists when the file is built.
- The grid holds key types `2` and `3` only; the XML's gathering
  (`_Collect.xml`), vehicle and stable files have no spawns in it.
- A private server's copy of `spawnplacementfieldgrid/1/7/` on client 1784
  (1,015 cell files, 58,988 spawns) walks by this layout; the client 1784
  test client holds no `mapdata_*` files.
- [fieldgridinfo.bss](fieldgridinfo_bss.md) lists exactly the squares the
  cell files of its folder hold, and [fileinfo.bss](fileinfo_bss.md)
  exactly the cell files.

## Open Questions

### What `key_type` 11 Is

Fields 700 and 701 hold 9 spawns with `key_type` `11` and no character
(`3377553690460161` and up in `700/7/427_238.bss`). The 1784 XML of those
fields is not in the private server's files, so the source file kind of
type `11` is open.

### What `territory` Keys

`territory` matches the XML `Territory` on all 745 shared keys and is `0`,
`1` or `2` where set. Whether these are `territoryinfo.bss` keys (Balenos,
Serendia, Calpheon) is not checked against the positions yet.
