# `instancefieldmapinfo.bss` Format

## Purpose

Map data per instance field: a title and description as UI string keys, a map image, a centre point and radius, participant and team limits, a territory lock, an entry item, team spawn
points and a few values without a name yet. The key is the
[instancefield.dbss](instancefield_dbss.md) field key.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records    | Row bytes                  |
| ------ | -------------- | ------- | -------------------------- | ------ | ---------- | -------------------------- |
| 2      | 2503 and later | 3483    | `instancefieldmapinfo.bss` | 44,266 | 193 Record | 196 to 228, 199 on average |
| 1      | 1685 to 2005   | 2005    | `instancefieldmapinfo.bss` | 22,625 | 122 Record | 180                        |

| Layout | File                       | Known            | Unknown          |
| ------ | -------------------------- | ---------------- | ---------------- |
| 2      | `instancefieldmapinfo.bss` | 18,924 B (42.8%) | 25,342 B (57.2%) |
| 1      | `instancefieldmapinfo.bss` | 7,253 B (32.1%)  | 15,372 B (67.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 2             |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3464   | Layout 2             |
| 3458   | Layout 2             |
| 3454   | Layout 2             |
| 3444   | Layout 2             |
| 3435   | Layout 2             |
| 3426   | Layout 2             |
| 3418   | Layout 2             |
| 3412   | Layout 2             |
| 3402   | Layout 2             |
| 3396   | Layout 2             |
| 3387   | Layout 2             |
| 3381   | Layout 2             |
| 3373   | Layout 2             |
| 3364   | Layout 2             |
| 3356   | Layout 2             |
| 3349   | Layout 2             |
| 3342   | Layout 2             |
| 3335   | Layout 2             |
| 3326   | Layout 2             |
| 3321   | Layout 2             |
| 3314   | Layout 2             |
| 3303   | Layout 2             |
| 3302   | Layout 2             |
| 3293   | Layout 2             |
| 3283   | Layout 2             |
| 3275   | Layout 2             |
| 3267   | Layout 2             |
| 3258   | Layout 2             |
| 3251   | Layout 2             |
| 3242   | Layout 2             |
| 3235   | Layout 2             |
| 3229   | Layout 2             |
| 3212   | Layout 2             |
| 3203   | Layout 2             |
| 3193   | Layout 2             |
| 3186   | Layout 2             |
| 3177   | Layout 2             |
| 3169   | Layout 2             |
| 3158   | Layout 2             |
| 3151   | Layout 2             |
| 3144   | Layout 2             |
| 3133   | Layout 2             |
| 3125   | Layout 2             |
| 3118   | Layout 2             |
| 3111   | Layout 2             |
| 3103   | Layout 2             |
| 3095   | Layout 2             |
| 3086   | Layout 2             |
| 3072   | Layout 2             |
| 3062   | Layout 2             |
| 3052   | Layout 2             |
| 3045   | Layout 2             |
| 3037   | Layout 2             |
| 3030   | Layout 2             |
| 3021   | Layout 2             |
| 3012   | Layout 2             |
| 3002   | Layout 2             |
| 2995   | Layout 2             |
| 2987   | Layout 2             |
| 2978   | Layout 2             |
| 2970   | Layout 2             |
| 2959   | Layout 2             |
| 2951   | Layout 2             |
| 2942   | Layout 2             |
| 2935   | Layout 2             |
| 2932   | Layout 2             |
| 2923   | Layout 2             |
| 2919   | Layout 2             |
| 2907   | Layout 2             |
| 2900   | Layout 2             |
| 2891   | Layout 2             |
| 2882   | Layout 2             |
| 2872   | Layout 2             |
| 2863   | Layout 2             |
| 2855   | Layout 2             |
| 2849   | Layout 2             |
| 2844   | Layout 2             |
| 2834   | Layout 2             |
| 2825   | Layout 2             |
| 2819   | Layout 2             |
| 2811   | Layout 2             |
| 2803   | Layout 2             |
| 2794   | Layout 2             |
| 2783   | Layout 2             |
| 2774   | Layout 2             |
| 2765   | Layout 2             |
| 2756   | Layout 2             |
| 2750   | Layout 2             |
| 2743   | Layout 2             |
| 2736   | Layout 2             |
| 2726   | Layout 2             |
| 2717   | Layout 2             |
| 2709   | Layout 2             |
| 2703   | Layout 2             |
| 2695   | Layout 2             |
| 2684   | Layout 2             |
| 2672   | Layout 2             |
| 2665   | Layout 2             |
| 2657   | Layout 2             |
| 2649   | Layout 2             |
| 2644   | Layout 2             |
| 2637   | Layout 2             |
| 2629   | Layout 2             |
| 2619   | Layout 2             |
| 2612   | Layout 2             |
| 2606   | Layout 2             |
| 2602   | Layout 2             |
| 2601   | Layout 2             |
| 2592   | Layout 2             |
| 2583   | Layout 2             |
| 2575   | Layout 2             |
| 2567   | Layout 2             |
| 2560   | Layout 2             |
| 2553   | Layout 2             |
| 2545   | Layout 2             |
| 2538   | Layout 2             |
| 2529   | Layout 2             |
| 2519   | Layout 2             |
| 2513   | Layout 2             |
| 2510   | Layout 2             |
| 2507   | Layout 2             |
| 2503   | Layout 2             |
| 2498   | No documented layout |
| 2492   | No documented layout |
| 2487   | No documented layout |
| 2480   | No documented layout |
| 2474   | No documented layout |
| 2468   | No documented layout |
| 2460   | No documented layout |
| 2453   | No documented layout |
| 2444   | No documented layout |
| 2438   | No documented layout |
| 2434   | No documented layout |
| 2429   | No documented layout |
| 2421   | No documented layout |
| 2414   | No documented layout |
| 2407   | No documented layout |
| 2401   | No documented layout |
| 2397   | No documented layout |
| 2393   | No documented layout |
| 2384   | No documented layout |
| 2378   | No documented layout |
| 2372   | No documented layout |
| 2358   | No documented layout |
| 2352   | No documented layout |
| 2347   | No documented layout |
| 2343   | No documented layout |
| 2335   | No documented layout |
| 2327   | No documented layout |
| 2324   | No documented layout |
| 2319   | No documented layout |
| 2313   | No documented layout |
| 2308   | No documented layout |
| 2302   | No documented layout |
| 2295   | No documented layout |
| 2290   | No documented layout |
| 2284   | No documented layout |
| 2276   | No documented layout |
| 2269   | No documented layout |
| 2259   | No documented layout |
| 2250   | No documented layout |
| 2243   | No documented layout |
| 2235   | No documented layout |
| 2229   | No documented layout |
| 2224   | No documented layout |
| 2218   | No documented layout |
| 2215   | No documented layout |
| 2207   | No documented layout |
| 2203   | No documented layout |
| 2196   | No documented layout |
| 2192   | No documented layout |
| 2189   | No documented layout |
| 2183   | No documented layout |
| 2179   | No documented layout |
| 2171   | No documented layout |
| 2163   | No documented layout |
| 2156   | No documented layout |
| 2151   | No documented layout |
| 2147   | No documented layout |
| 2142   | No documented layout |
| 2138   | No documented layout |
| 2134   | No documented layout |
| 2130   | No documented layout |
| 2122   | No documented layout |
| 2107   | No documented layout |
| 2098   | No documented layout |
| 2089   | No documented layout |
| 2081   | No documented layout |
| 2073   | No documented layout |
| 2067   | No documented layout |
| 2063   | No documented layout |
| 2059   | No documented layout |
| 2052   | No documented layout |
| 2044   | No documented layout |
| 2039   | No documented layout |
| 2032   | No documented layout |
| 2025   | No documented layout |
| 2011   | No documented layout |
| 2005   | Layout 1             |
| 2000   | Layout 1             |
| 1996   | Layout 1             |
| 1991   | Layout 1             |
| 1985   | Layout 1             |
| 1980   | Layout 1             |
| 1969   | Layout 1             |
| 1964   | Layout 1             |
| 1958   | Layout 1             |
| 1950   | Layout 1             |
| 1945   | Layout 1             |
| 1937   | Layout 1             |
| 1933   | Layout 1             |
| 1927   | Layout 1             |
| 1921   | Layout 1             |
| 1914   | Layout 1             |
| 1908   | Layout 1             |
| 1897   | Layout 1             |
| 1892   | Layout 1             |
| 1886   | Layout 1             |
| 1881   | Layout 1             |
| 1871   | Layout 1             |
| 1866   | Layout 1             |
| 1862   | Layout 1             |
| 1854   | Layout 1             |
| 1846   | Layout 1             |
| 1838   | Layout 1             |
| 1832   | Layout 1             |
| 1826   | Layout 1             |
| 1822   | Layout 1             |
| 1818   | Layout 1             |
| 1804   | Layout 1             |
| 1794   | Layout 1             |
| 1790   | Layout 1             |
| 1784   | Layout 1             |
| 1774   | Layout 1             |
| 1771   | Layout 1             |
| 1762   | Layout 1             |
| 1759   | Layout 1             |
| 1754   | Layout 1             |
| 1749   | Layout 1             |
| 1743   | Layout 1             |
| 1737   | Layout 1             |
| 1731   | Layout 1             |
| 1725   | Layout 1             |
| 1717   | Layout 1             |
| 1710   | Layout 1             |
| 1704   | Layout 1             |
| 1698   | Layout 1             |
| 1690   | Layout 1             |
| 1685   | Layout 1             |
| 1680   | No documented layout |
| 1674   | No documented layout |
| 1668   | No documented layout |
| 1659   | No documented layout |
| 1649   | No documented layout |
| 1642   | No documented layout |
| 1636   | No documented layout |
| 1628   | No documented layout |
| 1622   | No documented layout |
| 1614   | No documented layout |
| 1608   | No documented layout |
| 1602   | No documented layout |
| 1598   | No documented layout |
| 1594   | No documented layout |
| 1590   | No documented layout |
| 1587   | No documented layout |
| 1584   | No documented layout |
| 1579   | No documented layout |
| 1572   | No documented layout |
| 1565   | No documented layout |
| 1559   | No documented layout |
| 1554   | No documented layout |
| 1547   | No documented layout |
| 1537   | No documented layout |
| 1529   | No documented layout |
| 1524   | No documented layout |
| 1519   | No documented layout |
| 1509   | No documented layout |
| 1506   | No documented layout |
| 1504   | No documented layout |
| 1500   | No documented layout |
| 1493   | No documented layout |
| 1489   | No documented layout |
| 1485   | No documented layout |
| 1481   | No documented layout |
| 1474   | No documented layout |
| 1466   | No documented layout |
| 1462   | No documented layout |
| 1459   | No documented layout |
| 1453   | No documented layout |
| 1450   | No documented layout |
| 1445   | No documented layout |
| 1439   | No documented layout |
| 1433   | No documented layout |
| 1430   | No documented layout |
| 1426   | No documented layout |
| 1421   | No documented layout |
| 1417   | No documented layout |
| 1416   | No documented layout |
| 1409   | No documented layout |
| 1405   | No file              |
| 1401   | No file              |
| 1396   | No file              |
| 1391   | No file              |
| 1390   | No file              |
| 1386   | No file              |
| 1381   | No file              |
| 1379   | No file              |
| 1372   | No file              |
| 1366   | No file              |
| 1364   | No file              |
| 1363   | No file              |
| 1360   | No file              |
| 1358   | No file              |
| 1355   | No file              |
| 1351   | No file              |
| 1348   | No file              |
| 1346   | No file              |
| 1341   | No file              |
| 1340   | No file              |
| 1338   | No file              |
| 1335   | No file              |
| 1333   | No file              |
| 1329   | No file              |
| 1327   | No file              |
| 1324   | No file              |
| 1321   | No file              |
| 1319   | No file              |
| 1318   | No file              |
| 1316   | No file              |
| 1313   | No file              |
| 1311   | No file              |
| 1309   | No file              |
| 1304   | No file              |
| 1292   | No file              |
| 1286   | No file              |
| 1280   | No file              |
| 1276   | No file              |
| 1267   | No file              |
| 1261   | No file              |
| 1256   | No file              |
| 1250   | No file              |
| 1246   | No file              |
| 1239   | No file              |
| 1230   | No file              |
| 1226   | No file              |
| 1220   | No file              |
| 1217   | No file              |
| 1211   | No file              |
| 1210   | No file              |
| 1208   | No file              |
| 1203   | No file              |
| 1197   | No file              |
| 1194   | No file              |
| 1192   | No file              |
| 1187   | No file              |
| 1183   | No file              |
| 1177   | No file              |
| 1173   | No file              |
| 1167   | No file              |
| 1164   | No file              |
| 1156   | No file              |
| 1149   | No file              |
| 1144   | No file              |
| 1137   | No file              |
| 1132   | No file              |
| 1127   | No file              |
| 1122   | No file              |
| 1118   | No file              |
| 1114   | No file              |
| 1109   | No file              |
| 1102   | No file              |
| 1096   | No file              |
| 1088   | No file              |
| 1081   | No file              |
| 1076   | No file              |
| 1069   | No file              |
| 1064   | No file              |
| 1058   | No file              |
| 1051   | No file              |
| 1044   | No file              |
| 1036   | No file              |
| 1026   | No file              |
| 1016   | No file              |
| 1009   | No file              |
| 1005   | No file              |
| 1000   | No file              |
| 998    | No file              |
| 990    | No file              |
| 979    | No file              |
| 972    | No file              |
| 963    | No file              |
| 955    | No file              |
| 946    | No file              |
| 938    | No file              |
| 927    | No file              |
| 911    | No file              |
| 904    | No file              |
| 899    | No file              |
| 894    | No file              |
| 885    | No file              |
| 879    | No file              |
| 872    | No file              |
| 864    | No file              |
| 855    | No file              |
| 853    | No file              |
| 845    | No file              |
| 837    | No file              |
| 829    | No file              |
| 822    | No file              |
| 814    | No file              |
| 805    | No file              |
| 794    | No file              |
| 787    | No file              |
| 780    | No file              |
| 771    | No file              |
| 760    | No file              |
| 748    | No file              |
| 741    | No file              |
| 736    | No file              |
| 731    | No file              |
| 723    | No file              |
| 711    | No file              |
| 707    | No file              |
| 697    | No file              |
| 689    | No file              |
| 683    | No file              |
| 678    | No file              |
| 670    | No file              |
| 661    | No file              |
| 656    | No file              |
| 652    | No file              |
| 643    | No file              |
| 637    | No file              |
| 630    | No file              |
| 627    | No file              |
| 621    | No file              |
| 617    | No file              |
| 615    | No file              |
| 606    | No file              |
| 599    | No file              |
| 592    | No file              |
| 586    | No file              |
| 577    | No file              |
| 569    | No file              |
| 561    | No file              |
| 554    | No file              |
| 542    | No file              |
| 532    | No file              |
| 531    | No file              |
| 526    | No file              |
| 521    | No file              |
| 517    | No file              |
| 510    | No file              |
| 508    | No file              |
| 504    | No file              |
| 497    | No file              |
| 491    | No file              |
| 485    | No file              |
| 478    | No file              |
| 472    | No file              |
| 466    | No file              |
| 457    | No file              |
| 452    | No file              |
| 449    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                       |
| --------------------- | -------- | ---------------------------------------------------------- |
| `stringtable.bss`     | Optional | Hashes of the `GAME` sheet keys that `title` and `description` store; without it both columns show the key |
| `languagedata_*.loc`  | Optional | LOC type 37 text under those hashes; item names (LOC type 0) |
| `instancefield.dbss`  | Optional | The internal field name per key, through the `INSTANCE_FIELD_NAME` lookup index |

All multi-byte values are little-endian.

## Layout 2

### File Layout

A PABR file with variable-size records and the counted string table that
`exploration.bss` and `npcsimply.bss` also end with (`_common/pabr_strings.py`).
The records end exactly where the string table starts.

| Offset              | Type          | Field              | Notes                               |
| ------------------- | ------------- | ------------------ | ----------------------------------- |
| `+0x00`             | char[4]       | magic              | `PABR`                              |
| `+0x04`             | u32           | count              | Number of records                   |
| `+0x08`             | Record[count] | records            | `count` x record, not sorted by key |
| `records+0x00`      | String Table  | string_table       | See String Table                    |
| `string_table+0x00` | u32           | string_table_start | Offset of the string table          |
| `string_table+0x04` | u32           | zero               | `0`                                 |

### String Table (variable: 4 bytes + strings)

String table entry 0 is the empty string; a string index of `0` means none.

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | Number of strings    |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries  |

### Record (variable: 196 bytes + lists)

| Offset               | Type                     | Field              | Notes |
| -------------------- | ------------------------ | ------------------ | ----- |
| `+0x00`              | u16                      | key                | `instancefield.dbss` key |
| `+0x02`              | u32                      | max_user           | Most participants: `6` on Solare arenas, `30` on guild matches, `40` on most Crimson fields and Oasis servers, `3000` on the `MajorSiege_*` maps |
| `+0x06`              | u32                      | max_team_count     | `1`, or `2` on team battles (Solare arenas, guild matches, Crimson fields, `PAPUCRIO_ARENA`, `CrewBattle`, `Edania_Field_1vs1`) |
| `+0x0A`              | f32                      | x                  | World position (centimetres); all `0` when unset |
| `+0x0E`              | f32                      | y                  | |
| `+0x12`              | f32                      | z                  | |
| `+0x16`              | f32                      | radius             | Centimetres around that position (`9000` on `Solare_Arena_Reed`); `0` when unset |
| `+0x1A`              | u32                      | title              | String index of a `GAME` sheet key (`LUA_LOCALWAR_SERVERNAME_MAP_1`, `INSTANCEDUNGEONDATA_A1_001_NAME`) |
| `+0x1E`              | u32                      | description        | String index of a `GAME` sheet key (`INSTANCEDUNGEONDATA_A1_001_DESC`) |
| `+0x22`              | u8                       | is_season_only     | `1` on six Crimson field records (keys 11, 12, 17, 18, 22, 24), else `0` |
| `+0x23`              | u32                      | min_user           | Fewest participants; equals `max_team_count` except on `Edania_Field_1vs1` (`1`), horse races (`2`, `3`, `5`) and `Yonggung` (`7`). Never above `max_user` |
| `+0x27`              | u32                      | image              | String index of a `.dds` path (`Map_Nest.dds`, `Combine_Etc_horseracing.dds`) |
| `+0x2B`              | u16[4]                   | image_region       | x1, y1, x2, y2 in pixels of `image`; `0, 0, 1, 1` on the Crimson field maps |
| `+0x33`              | bytes[106]               | unknown_33         | The same bytes in every record; the 8-byte groups hold `0x00007FFC...` and `0x00000293...` values, which read like memory addresses of the tool that wrote the file |
| `+0x9D`              | u8                       | is_show_name_when_camouflage | `1` on the Solare arenas, guild matches, `PAPUCRIO_ARENA` and 8 of the 16 Crimson field records: names stay visible under camouflage |
| `+0x9E`              | u16                      | restrict_territory | `territoryinfo.bss` territory key the map is locked to, `0xFFFF` for none; see [Territory locks](#territory-locks-client-3464) |
| `+0xA0`              | bytes[8]                 | unknown_a0         | Always `0` |
| `+0xA8`              | u32                      | entry_item_id      | Item ID, `0` for none; the "Access Granted" items of Atoraxion |
| `+0xAC`              | u32                      | unknown_ac         | `1` where `entry_item_id` is set, else `0`; possibly its count, see [Field Names](#field-names) |
| `+0xB0`              | u32                      | unknown_b0         | Always `0` |
| `+0xB4`              | u32                      | unknown_b4         | `0`, `3600` on the `A1_` fields, `10800` on the Atoraxion Single maps and key 210 |
| `+0xB8`              | u32                      | unknown_b8         | Always `0` |
| `+0xBC`              | u32                      | hash_count         | |
| `+0xC0`              | u32[hash_count]          | unknown_hashes     | `hash_count` values; only on `A1_` fields (1 to 3 each); not a `stringtable.bss` key hash |
| `unknown_hashes+0x00` | u32                     | spawn_count        | |
| `unknown_hashes+0x04` | f32[spawn_count][3]     | spawns             | World positions; `2` on every guild match map, one per side, both inside the map's box |
| `spawns+0x00`        | f32 if spawn_count != 0  | unknown_spawn_f32  | Only when `spawn_count` is not `0`; `200` on all |
| `unknown_spawn_f32+0x00` | u32 if spawn_count != 0 | unknown_spawn_u32 | Only when `spawn_count` is not `0`; `10` on all |

Earlier versions of this doc called `unknown_33` `filler` and the three
always-zero fields `unknown_a0`, `unknown_b0` and `unknown_b8` `zero`.

## Layout 1

On client 1784 a record is 180 bytes with no lists: it has no
`description`, so every later field sits 4 bytes earlier, and it ends after
`unknown_b0`, without `unknown_b4`, `unknown_b8`, the hash list or the spawn
list. `unknown_a0` is 12 bytes.

### Record (180 bytes)

| Offset  | Type       | Field                        | Notes |
| ------- | ---------- | ---------------------------- | ----- |
| `+0x00` | u16        | key                          | `instancefield.dbss` key |
| `+0x02` | u32        | max_user                     | |
| `+0x06` | u32        | max_team_count               | |
| `+0x0A` | f32        | x                            | |
| `+0x0E` | f32        | y                            | |
| `+0x12` | f32        | z                            | |
| `+0x16` | f32        | radius                       | |
| `+0x1A` | u32        | title                        | String index of a `GAME` sheet key |
| `+0x1E` | u8         | is_season_only               | |
| `+0x1F` | u32        | min_user                     | |
| `+0x23` | u32        | image                        | String index of a `.dds` path |
| `+0x27` | u16[4]     | image_region                 | |
| `+0x2F` | bytes[106] | unknown_33                   | |
| `+0x99` | u8         | is_show_name_when_camouflage | |
| `+0x9A` | u16        | restrict_territory           | `0xFFFF` for none |
| `+0x9C` | bytes[12]  | unknown_a0                   | `0` except on keys 150 to 153, where it holds the u32s `66012, 1, 0`: the first item and count of the sheet's `exchangeItemForNormalFieldEnter` |
| `+0xA8` | u32        | entry_item_id                | `65992` on keys 150 and 151, `757260` on 152 and 153 on client 1784 |
| `+0xAC` | u32        | unknown_ac                   | `1` where `entry_item_id` is set, else `0` |
| `+0xB0` | u32        | unknown_b0                   | Always `0` |

On client 1784 the file holds 77 records and 17 strings, none of them a
`_DESC` key.

## Field Names

The names of `max_user`, `max_team_count`, `is_season_only`, `min_user`, `is_show_name_when_camouflage` and `restrict_territory` follow the `InstanceEnterPosition` sheet of a private server's `DataSheets.bexcel` on client 1784 (columns `MaxUser`, `MaxTeamCount`, `isSeasonOnly`, `MinUser`, `isShowNameWnehCamoflage`, `restrictTerritory`). Matched by value over the 77 keys the sheet shares with client 3464: five columns equal the file on all 77 keys, every non-zero value included. `MaxUser` equals `max_user` on 57; the other 20 are later rebalances (Crimson fields `30` to `40` and `2` to `4`, `CrewBattle` `10` to `20`, Atoraxion `5` to `1`).

The same sheet has `exchangeItemForNormalFieldEnter` (`66012,0,1,65992,0,1` on key 150, item, enchant and count pairs) whose second item is that key's `entry_item_id`, so `unknown_ac` may be the count; the sheet has no column for `unknown_b4`, `unknown_hashes` or the spawn list, and its `Team_1` to `Team_4` positions are not the `spawns`.

## Territory Locks (Client 3464)

| Key | Field | restrict_territory | LOC name |
| --- | ----- | -----------------: | -------- |
| 131 | `Personal_Instance_Cal` | 2 | Calpheon |
| 134 | `Personal_Instance_Val` | 4 | Valencia |
| 135 | `Personal_Instance_Kama` | 6 | Kamasylvia |
| 136 | `Personal_Instance_SnowMountain` | 9 | Mountain of Eternal Winter |

`_Ser`, `_Bal` and `_Media` store `0xFFFF`.

## Entry Items (Client 3464)

| Key | Field                          | Item   | LOC name |
| --- | ------------------------------ | -----: | -------- |
| 150, 151, 174 | `Atoraxion_Desert`, `_EZ`, `_Single_Boss` | 65992 | Fate Fulfilled: Atoraxxion |
| 152, 153, 175 | `Atoraxion_SEA`, `_EZ`, `_Single_Boss` | 757260 | Access Granted: Underwater Entrance |
| 154, 155, 176 | `Atoraxion_Jungle`, `_EZ`, `_Single_Boss` | 757313 | Access Granted: Yolu's Nail |
| 156, 157, 177 | `Atoraxion_Thorn`, `_EZ`, `_Single_Boss` | 66948 | Access Granted: Orze's Root |
| 210 | not in `instancefield.dbss`    | 66942  | Access Granted: The Final Gladios |

## Notes

- On client 3464 the file holds 192 records and 164 strings (5 `.dds`
  paths). 185 keys are in both tables. Only here: 210, 4067 to 4071 (named
  `INSTANCEDUNGEONDATA_A1_067_NAME` onwards) and 5000. Only in
  `instancefield.dbss`: 1 to 9, 98, 99, 888, 999 and 9876.
- 142 of the 158 UI keys have `GAME` sheet text. Examples:
  `LUA_LOCALWAR_SERVERNAME_MAP_0` to `_3` read Castle Ruins, Garmoth's Nest,
  Valencia City and Sand Castle Shore-Down (the Crimson fields and
  `PAPUCRIO_ARENA`); `LUA_PERSONAL_SERVER_SER` reads Oasis Server: Serendia;
  `INSTANCEDUNGEONDATA_A1_002_NAME` reads Scarlet Thread. The `A1_003` to
  `A1_008` names are placeholders (`Title 003`, `Desc 003`); `A1_058`,
  `A1_063`, `A1_064` and `A1_067` to `A1_071` have no text.
- `image_region` fits its sheet: `Combine_Etc_horseracing.dds` is 1180 x
  1180 and holds the 500 x 160 boxes `(1, 1005)` and `(502, 1005)`;
  `Combine_Etc_horseracing_01.dds` is 512 x 512 and holds `(1, 1)` to
  `(501, 161)`.
- Positions match the `instancefield.dbss` boxes (sector = position /
  12,800, floored): 79 of the 80 set positions and all 22 spawns lie in the
  box of their key. `Solare_Arena_Reed` sits at sector `(-88, 2, 95)` in
  `-90..-86, 0..3, 93..97`. The exception is `HorseRace_SnowyMountain_Main`,
  whose point is at height sector `2` against a box of `-1..-1`.
- The `INSTANCE_FIELD_TITLE` lookup index holds the `GAME` sheet hash of
  each `title` key, so `instancefield.dbss` (Title column) and the
  `buff.dbss` type 176 Effect text (`Teleport to Instance Field The Magnus:
  The Great Single Path (A1_001)`) read the title without this file.
- The client Lua function `ToClient_GetInstanceFieldPlayerMaxCountByMapKey`
  takes this key; `max_user` is the player cap it names (Solare arenas,
  3 vs 3, store `6`).

## Open Questions

### What are `unknown_b4` and the `A1_` hash list?

`unknown_b4` is `3600` on every `A1_` field and `10800` on the Atoraxion
Single maps, which fits a time limit in seconds (the Lua calls
`ToClient_getInstanceFieldRemainTime`). The `unknown_hashes` on 34 `A1_`
fields match no `stringtable.bss` key hash and no LOC type 37 key.
