# `regionmapinfo.bss` Format

## Purpose

The bitmaps the game looks a world position up in (its region, siege area
or audio zone): one row per map with its key, its map type, the sector
rectangle the image covers and the image file name. The image is
`ui_texture/minimap/area/<image_path>.bkd` in lower case with its `.rid`
palette (`RegionMap_New.bmp` is `regionmap_new.bmp.bkd`).
[fieldinfo.bss](fieldinfo_bss.md) stores these keys in its
`*_map_index` fields (see its Map Index Fields). The file is the client copy
of the developers' `RegionMap_Table` sheet (see
[Field Names](#field-names)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                | Bytes | Records | Row bytes               |
| ------ | ------------- | ------- | ------------------- | ----- | ------- | ----------------------- |
| 2      | 805 and later | 3483    | `regionmapinfo.bss` | 896   | 13 Row  | 25                      |
| 1      | 435 to 794    | 794     | `regionmapinfo.bss` | 240   | 4 Row   | 53 to 67, 59 on average |

| Layout | File                | Known          | Unknown    |
| ------ | ------------------- | -------------- | ---------- |
| 2      | `regionmapinfo.bss` | 896 B (100.0%) | 0 B (0.0%) |
| 1      | `regionmapinfo.bss` | 240 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3464   | Layout 2 |
| 3458   | Layout 2 |
| 3454   | Layout 2 |
| 3444   | Layout 2 |
| 3435   | Layout 2 |
| 3426   | Layout 2 |
| 3418   | Layout 2 |
| 3412   | Layout 2 |
| 3402   | Layout 2 |
| 3396   | Layout 2 |
| 3387   | Layout 2 |
| 3381   | Layout 2 |
| 3373   | Layout 2 |
| 3364   | Layout 2 |
| 3356   | Layout 2 |
| 3349   | Layout 2 |
| 3342   | Layout 2 |
| 3335   | Layout 2 |
| 3326   | Layout 2 |
| 3321   | Layout 2 |
| 3314   | Layout 2 |
| 3303   | Layout 2 |
| 3302   | Layout 2 |
| 3293   | Layout 2 |
| 3283   | Layout 2 |
| 3275   | Layout 2 |
| 3267   | Layout 2 |
| 3258   | Layout 2 |
| 3251   | Layout 2 |
| 3242   | Layout 2 |
| 3235   | Layout 2 |
| 3229   | Layout 2 |
| 3212   | Layout 2 |
| 3203   | Layout 2 |
| 3193   | Layout 2 |
| 3186   | Layout 2 |
| 3177   | Layout 2 |
| 3169   | Layout 2 |
| 3158   | Layout 2 |
| 3151   | Layout 2 |
| 3144   | Layout 2 |
| 3133   | Layout 2 |
| 3125   | Layout 2 |
| 3118   | Layout 2 |
| 3111   | Layout 2 |
| 3103   | Layout 2 |
| 3095   | Layout 2 |
| 3086   | Layout 2 |
| 3072   | Layout 2 |
| 3062   | Layout 2 |
| 3052   | Layout 2 |
| 3045   | Layout 2 |
| 3037   | Layout 2 |
| 3030   | Layout 2 |
| 3021   | Layout 2 |
| 3012   | Layout 2 |
| 3002   | Layout 2 |
| 2995   | Layout 2 |
| 2987   | Layout 2 |
| 2978   | Layout 2 |
| 2970   | Layout 2 |
| 2959   | Layout 2 |
| 2951   | Layout 2 |
| 2942   | Layout 2 |
| 2935   | Layout 2 |
| 2932   | Layout 2 |
| 2923   | Layout 2 |
| 2919   | Layout 2 |
| 2907   | Layout 2 |
| 2900   | Layout 2 |
| 2891   | Layout 2 |
| 2882   | Layout 2 |
| 2872   | Layout 2 |
| 2863   | Layout 2 |
| 2855   | Layout 2 |
| 2849   | Layout 2 |
| 2844   | Layout 2 |
| 2834   | Layout 2 |
| 2825   | Layout 2 |
| 2819   | Layout 2 |
| 2811   | Layout 2 |
| 2803   | Layout 2 |
| 2794   | Layout 2 |
| 2783   | Layout 2 |
| 2774   | Layout 2 |
| 2765   | Layout 2 |
| 2756   | Layout 2 |
| 2750   | Layout 2 |
| 2743   | Layout 2 |
| 2736   | Layout 2 |
| 2726   | Layout 2 |
| 2717   | Layout 2 |
| 2709   | Layout 2 |
| 2703   | Layout 2 |
| 2695   | Layout 2 |
| 2684   | Layout 2 |
| 2672   | Layout 2 |
| 2665   | Layout 2 |
| 2657   | Layout 2 |
| 2649   | Layout 2 |
| 2644   | Layout 2 |
| 2637   | Layout 2 |
| 2629   | Layout 2 |
| 2619   | Layout 2 |
| 2612   | Layout 2 |
| 2606   | Layout 2 |
| 2602   | Layout 2 |
| 2601   | Layout 2 |
| 2592   | Layout 2 |
| 2583   | Layout 2 |
| 2575   | Layout 2 |
| 2567   | Layout 2 |
| 2560   | Layout 2 |
| 2553   | Layout 2 |
| 2545   | Layout 2 |
| 2538   | Layout 2 |
| 2529   | Layout 2 |
| 2519   | Layout 2 |
| 2513   | Layout 2 |
| 2510   | Layout 2 |
| 2507   | Layout 2 |
| 2503   | Layout 2 |
| 2498   | Layout 2 |
| 2492   | Layout 2 |
| 2487   | Layout 2 |
| 2480   | Layout 2 |
| 2474   | Layout 2 |
| 2468   | Layout 2 |
| 2460   | Layout 2 |
| 2453   | Layout 2 |
| 2444   | Layout 2 |
| 2438   | Layout 2 |
| 2434   | Layout 2 |
| 2429   | Layout 2 |
| 2421   | Layout 2 |
| 2414   | Layout 2 |
| 2407   | Layout 2 |
| 2401   | Layout 2 |
| 2397   | Layout 2 |
| 2393   | Layout 2 |
| 2384   | Layout 2 |
| 2378   | Layout 2 |
| 2372   | Layout 2 |
| 2358   | Layout 2 |
| 2352   | Layout 2 |
| 2347   | Layout 2 |
| 2343   | Layout 2 |
| 2335   | Layout 2 |
| 2327   | Layout 2 |
| 2324   | Layout 2 |
| 2319   | Layout 2 |
| 2313   | Layout 2 |
| 2308   | Layout 2 |
| 2302   | Layout 2 |
| 2295   | Layout 2 |
| 2290   | Layout 2 |
| 2284   | Layout 2 |
| 2276   | Layout 2 |
| 2269   | Layout 2 |
| 2259   | Layout 2 |
| 2250   | Layout 2 |
| 2243   | Layout 2 |
| 2235   | Layout 2 |
| 2229   | Layout 2 |
| 2224   | Layout 2 |
| 2218   | Layout 2 |
| 2215   | Layout 2 |
| 2207   | Layout 2 |
| 2203   | Layout 2 |
| 2196   | Layout 2 |
| 2192   | Layout 2 |
| 2189   | Layout 2 |
| 2183   | Layout 2 |
| 2179   | Layout 2 |
| 2171   | Layout 2 |
| 2163   | Layout 2 |
| 2156   | Layout 2 |
| 2151   | Layout 2 |
| 2147   | Layout 2 |
| 2142   | Layout 2 |
| 2138   | Layout 2 |
| 2134   | Layout 2 |
| 2130   | Layout 2 |
| 2122   | Layout 2 |
| 2107   | Layout 2 |
| 2098   | Layout 2 |
| 2089   | Layout 2 |
| 2081   | Layout 2 |
| 2073   | Layout 2 |
| 2067   | Layout 2 |
| 2063   | Layout 2 |
| 2059   | Layout 2 |
| 2052   | Layout 2 |
| 2044   | Layout 2 |
| 2039   | Layout 2 |
| 2032   | Layout 2 |
| 2025   | Layout 2 |
| 2011   | Layout 2 |
| 2005   | Layout 2 |
| 2000   | Layout 2 |
| 1996   | Layout 2 |
| 1991   | Layout 2 |
| 1985   | Layout 2 |
| 1980   | Layout 2 |
| 1969   | Layout 2 |
| 1964   | Layout 2 |
| 1958   | Layout 2 |
| 1950   | Layout 2 |
| 1945   | Layout 2 |
| 1937   | Layout 2 |
| 1933   | Layout 2 |
| 1927   | Layout 2 |
| 1921   | Layout 2 |
| 1914   | Layout 2 |
| 1908   | Layout 2 |
| 1897   | Layout 2 |
| 1892   | Layout 2 |
| 1886   | Layout 2 |
| 1881   | Layout 2 |
| 1871   | Layout 2 |
| 1866   | Layout 2 |
| 1862   | Layout 2 |
| 1854   | Layout 2 |
| 1846   | Layout 2 |
| 1838   | Layout 2 |
| 1832   | Layout 2 |
| 1826   | Layout 2 |
| 1822   | Layout 2 |
| 1818   | Layout 2 |
| 1804   | Layout 2 |
| 1794   | Layout 2 |
| 1790   | Layout 2 |
| 1784   | Layout 2 |
| 1774   | Layout 2 |
| 1771   | Layout 2 |
| 1762   | Layout 2 |
| 1759   | Layout 2 |
| 1754   | Layout 2 |
| 1749   | Layout 2 |
| 1743   | Layout 2 |
| 1737   | Layout 2 |
| 1731   | Layout 2 |
| 1725   | Layout 2 |
| 1717   | Layout 2 |
| 1710   | Layout 2 |
| 1704   | Layout 2 |
| 1698   | Layout 2 |
| 1690   | Layout 2 |
| 1685   | Layout 2 |
| 1680   | Layout 2 |
| 1674   | Layout 2 |
| 1668   | Layout 2 |
| 1659   | Layout 2 |
| 1649   | Layout 2 |
| 1642   | Layout 2 |
| 1636   | Layout 2 |
| 1628   | Layout 2 |
| 1622   | Layout 2 |
| 1614   | Layout 2 |
| 1608   | Layout 2 |
| 1602   | Layout 2 |
| 1598   | Layout 2 |
| 1594   | Layout 2 |
| 1590   | Layout 2 |
| 1587   | Layout 2 |
| 1584   | Layout 2 |
| 1579   | Layout 2 |
| 1572   | Layout 2 |
| 1565   | Layout 2 |
| 1559   | Layout 2 |
| 1554   | Layout 2 |
| 1547   | Layout 2 |
| 1537   | Layout 2 |
| 1529   | Layout 2 |
| 1524   | Layout 2 |
| 1519   | Layout 2 |
| 1509   | Layout 2 |
| 1506   | Layout 2 |
| 1504   | Layout 2 |
| 1500   | Layout 2 |
| 1493   | Layout 2 |
| 1489   | Layout 2 |
| 1485   | Layout 2 |
| 1481   | Layout 2 |
| 1474   | Layout 2 |
| 1466   | Layout 2 |
| 1462   | Layout 2 |
| 1459   | Layout 2 |
| 1453   | Layout 2 |
| 1450   | Layout 2 |
| 1445   | Layout 2 |
| 1439   | Layout 2 |
| 1433   | Layout 2 |
| 1430   | Layout 2 |
| 1426   | Layout 2 |
| 1421   | Layout 2 |
| 1417   | Layout 2 |
| 1416   | Layout 2 |
| 1409   | Layout 2 |
| 1405   | Layout 2 |
| 1401   | Layout 2 |
| 1396   | Layout 2 |
| 1391   | Layout 2 |
| 1390   | Layout 2 |
| 1386   | Layout 2 |
| 1381   | Layout 2 |
| 1379   | Layout 2 |
| 1372   | Layout 2 |
| 1366   | Layout 2 |
| 1364   | Layout 2 |
| 1363   | Layout 2 |
| 1360   | Layout 2 |
| 1358   | Layout 2 |
| 1355   | Layout 2 |
| 1351   | Layout 2 |
| 1348   | Layout 2 |
| 1346   | Layout 2 |
| 1341   | Layout 2 |
| 1340   | Layout 2 |
| 1338   | Layout 2 |
| 1335   | Layout 2 |
| 1333   | Layout 2 |
| 1329   | Layout 2 |
| 1327   | Layout 2 |
| 1324   | Layout 2 |
| 1321   | Layout 2 |
| 1319   | Layout 2 |
| 1318   | Layout 2 |
| 1316   | Layout 2 |
| 1313   | Layout 2 |
| 1311   | Layout 2 |
| 1309   | Layout 2 |
| 1304   | Layout 2 |
| 1292   | Layout 2 |
| 1286   | Layout 2 |
| 1280   | Layout 2 |
| 1276   | Layout 2 |
| 1267   | Layout 2 |
| 1261   | Layout 2 |
| 1256   | Layout 2 |
| 1250   | Layout 2 |
| 1246   | Layout 2 |
| 1239   | Layout 2 |
| 1230   | Layout 2 |
| 1226   | Layout 2 |
| 1220   | Layout 2 |
| 1217   | Layout 2 |
| 1211   | Layout 2 |
| 1210   | Layout 2 |
| 1208   | Layout 2 |
| 1203   | Layout 2 |
| 1197   | Layout 2 |
| 1194   | Layout 2 |
| 1192   | Layout 2 |
| 1187   | Layout 2 |
| 1183   | Layout 2 |
| 1177   | Layout 2 |
| 1173   | Layout 2 |
| 1167   | Layout 2 |
| 1164   | Layout 2 |
| 1156   | Layout 2 |
| 1149   | Layout 2 |
| 1144   | Layout 2 |
| 1137   | Layout 2 |
| 1132   | Layout 2 |
| 1127   | Layout 2 |
| 1122   | Layout 2 |
| 1118   | Layout 2 |
| 1114   | Layout 2 |
| 1109   | Layout 2 |
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
| 829    | Layout 2 |
| 822    | Layout 2 |
| 814    | Layout 2 |
| 805    | Layout 2 |
| 794    | Layout 1 |
| 787    | Layout 1 |
| 780    | Layout 1 |
| 771    | Layout 1 |
| 760    | Layout 1 |
| 748    | Layout 1 |
| 741    | Layout 1 |
| 736    | Layout 1 |
| 731    | Layout 1 |
| 723    | Layout 1 |
| 711    | Layout 1 |
| 707    | Layout 1 |
| 697    | Layout 1 |
| 689    | Layout 1 |
| 683    | Layout 1 |
| 678    | Layout 1 |
| 670    | Layout 1 |
| 661    | Layout 1 |
| 656    | Layout 1 |
| 652    | Layout 1 |
| 643    | Layout 1 |
| 637    | Layout 1 |
| 630    | Layout 1 |
| 627    | Layout 1 |
| 621    | Layout 1 |
| 617    | Layout 1 |
| 615    | Layout 1 |
| 606    | Layout 1 |
| 599    | Layout 1 |
| 592    | Layout 1 |
| 586    | Layout 1 |
| 577    | Layout 1 |
| 569    | Layout 1 |
| 561    | Layout 1 |
| 554    | Layout 1 |
| 542    | Layout 1 |
| 532    | Layout 1 |
| 531    | Layout 1 |
| 526    | Layout 1 |
| 521    | Layout 1 |
| 517    | Layout 1 |
| 510    | Layout 1 |
| 508    | Layout 1 |
| 504    | Layout 1 |
| 497    | Layout 1 |
| 491    | Layout 1 |
| 485    | Layout 1 |
| 478    | Layout 1 |
| 472    | Layout 1 |
| 466    | Layout 1 |
| 457    | Layout 1 |
| 452    | Layout 1 |
| 449    | Layout 1 |
| 435    | Layout 1 |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

A PABR file with fixed rows and the counted string table that
`fieldinfo.bss` also ends with (`_common/pabr_strings.py`).

| Offset              | Type              | Field              | Notes                                                       |
| ------------------- | ----------------- | ------------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                              |
| `+0x04`             | u32               | record_count       | Number of rows; `13` on client 3482                         |
| `+0x08`             | Row[record_count] | records            | See Row; not sorted by `map_index`                          |
| `records+0x00`      | String Table      | string_table       | See String Table                                            |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 25 x count`  |
| `string_table+0x04` | u32               | zero               | Always `0`                                                  |

The parser rejects a file whose rows do not end at `string_table_start`.

### Row (25 bytes)

| Offset  | Type | Field          | Notes |
| ------- | ---- | -------------- | ----- |
| `+0x00` | u16  | map_index      | Unique; the value of the `fieldinfo.bss` `*_map_index` fields |
| `+0x02` | u8   | map_type       | See [Map Types](#map-types) |
| `+0x03` | u16  | map_index_dup  | Equals `map_index` on every row of every client read (794 to 3482); the parser rejects a row where it differs |
| `+0x05` | i32  | sector_start_x | Left edge of the image, in 12,800-unit sectors; `-160` on every row |
| `+0x09` | i32  | sector_end_y   | Top edge; `160` on every row |
| `+0x0D` | i32  | sector_end_x   | Right edge; `112` on every row |
| `+0x11` | i32  | sector_start_y | Bottom edge; `-88` on every row |
| `+0x15` | u32  | image_path_ref | String-table index of `image_path`, the map image file name (`RegionMap_New.bmp`) |

The map's Y axis is the world's Z axis (north). The rectangle is one sector
wider on every side than the box of `fieldinfo.bss` field `1`, the open
world (X `-159` to `111`, Z `-87` to `159` on client 3482), as the sheet
comment asks: a field is written one sector smaller than its map. The
parser stores `image_path_ref` as the string under `image_path`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Equals `record_count` on every client read               |
| `+0x04` | pstr[string_count] | strings      | Counted entries, indexed from `0`; one image name per row, in row order |

## Layout 1

The client 794 file (in `gamecommondata/binary/en/`) has no PABR header
and no string table: a u32 row count, then rows that hold the image name
inline as a `str16`. The row fields before it are those of Layout 2.

### File Layout

| Offset  | Type              | Field        | Notes                   |
| ------- | ----------------- | ------------ | ----------------------- |
| `+0x00` | u32               | record_count | `4` on client 794       |
| `+0x04` | Row[record_count] | records      | See Row                 |

### Row (variable: 29 bytes + image name)

| Offset  | Type  | Field          | Notes |
| ------- | ----- | -------------- | ----- |
| `+0x00` | u16   | map_index      | |
| `+0x02` | u8    | map_type       | `0`, `3`, `4` and `6` on client 794 |
| `+0x03` | u16   | map_index_dup  | |
| `+0x05` | i32   | sector_start_x | |
| `+0x09` | i32   | sector_end_y   | |
| `+0x0D` | i32   | sector_end_x   | |
| `+0x11` | i32   | sector_start_y | |
| `+0x15` | str16 | image_path     | `AudioMap.bmp`, `VillageSiegemap.bmp`, `Siegemap.bmp`, `RegionMap_New.bmp` |

## Map Types

`map_type` is the 2016 client's `gc::BitmapMapInfoType` (a u8 enum), the
value `gc::BitmapMapInfo::getBitmapMapInfo()` returns for each map class.
The 2016 enum ends at `5`; the later values have no name there. Every map
except the village siege maps has `map_type` = `map_index - 1`.

| Value | 2016 name                        | Maps (key) on client 3482 |
| ----- | -------------------------------- | ------------------------- |
| `0`   | `BitmapMapInfoType_Region`       | `RegionMap_New.bmp` (1)   |
| `1`   | `BitmapMapInfoType_Fishing`      | none                      |
| `2`   | `BitmapMapInfoType_Water`        | none                      |
| `3`   | `BitmapMapInfoType_Siege`        | `Siegemap.bmp` (4)        |
| `4`   | `BitmapMapInfoType_VillageSiege` | none                      |
| `5`   | `BitmapMapInfoType_Underground`  | none                      |
| `6`   | none                             | `AudioMap.bmp` (7)        |
| `7`   | none                             | `GreatSeaMap.bmp` (8)     |
| `8`   | none                             | `HorseRaceCourseMap.bmp` (9) |
| `10`  | none                             | `ElfWar_SiegeMap.bmp` (11) |
| `11`  | none                             | `VillageSiegemap.bmp` (5), `VillageSiegemap_New.bmp` (10), `VillageSiegemap_2024.bmp` (12) |
| `13`  | none                             | `HardCoreChannelMap.bmp` (14) |
| `14`  | none                             | `SnowBoardCourseMap.bmp` (15) |
| `15`  | none                             | `EdaniaRegionMap.bmp` (16) |
| `16`  | none                             | `OceanSiegemap.bmp` (17)  |

The village siege maps share one value, and it moved between clients:

| Clients      | `map_type` of the village siege maps | Village siege maps (key)   |
| ------------ | ------------------------------------ | -------------------------- |
| 794 to 1485  | `4` (`BitmapMapInfoType_VillageSiege`) | 5                        |
| 1636         | `4`                                  | 5, 10                      |
| 1784, 2107   | `9`                                  | 5, 10                      |
| 2519 to 3482 | `11`                                 | 5, 10, 12                  |

## Field Names

The row is the `RegionMap_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (10 rows, developer workbook
`datasheet_regiondatatable.xlsm`). The `regionmapinfo.bss` of the client
1784 test client is byte for byte the private server's build of that sheet:
7 rows, the sheet without keys 2 (`FishingMap.bmp`), 3 (`WaterMap.bmp`) and
6 (`Undergroundmap.bmp`). Over the 7 shared keys:

| Field                      | Sheet column                     | Match                       |
| -------------------------- | -------------------------------- | --------------------------- |
| `map_index`                | `Index`                          | 7 of 7                      |
| `sector_start_x`           | `MapSectorStartX`                | 7 of 7 (`-160`)             |
| `sector_end_y`             | `MapSectorEndY`                  | 7 of 7 (`160`)              |
| `sector_end_x`             | `MapSectorEndX`                  | 7 of 7 (`112`)              |
| `sector_start_y`           | `MapSectorStartY`                | 7 of 7 (`-88`)              |
| `image_path`               | `ImagePath`                      | 7 of 7                      |
| `map_type`                 | `Type`                           | `Type - 1` on 5 of 7; keys 5 and 10 hold `9`, the sheet `5` and `10` |

The four sector values differ from each other, so their match places each
field. The 2016 client's `gc::BitmapMapInfo` holds `_key` (a u16),
`m_sector` (a `CRect`: `left`, `top`, `right`, `bottom`) and
`m_strImagePath`, the row order with `map_type` and `map_index_dup` between
the key and the rectangle. `map_type` takes its name from
`gc::BitmapMapInfoType`: on clients 794 to 1636 the region map holds `0`
(`Region`), the siege map `3` (`Siege`) and the village siege maps `4`
(`VillageSiege`). The sheet's `Description` (Korean notes, `월드 지도`
"world map") is not in the file; its comment says the game does not use it.

## Notes

- The 1784 sheet comments: `Index` counts from `1` and must be unique;
  `ImagePath` is relative to the UI folder, and a `*` after the name loads
  every file with that name. No row on any client read uses `*`.
- The 2016 client has a map class for each named type (`RegionMapInfo`,
  `FishingMapInfo`, `WaterMapInfo`, `SiegeMapInfo`, `VillageSiegeMapInfo`,
  `UndergroundMapInfo`). The server build of a private server on client 1784
  adds `AudioMapInfo`, `GreatSeaMapInfo` and `HorseRaceMapInfo`.
- Client 2107 also has six `_Morning` maps keyed `10000` plus the key of the
  map they copy (`10000` `RegionMap_Morning.bmp` to `10009`
  `VillageSiegemap_New_Morning.bmp`), each with the `map_type` of that map.
  Client 2519 and later have no `_Morning` rows, though the client 3482
  folder still has `regionmap_morning.bmp.bkd` and the other `_morning`
  images.
- Keys `2`, `3` and `6` (fishing, water and underground maps) are in no
  client read; `fieldinfo.bss` still stores them in `fishing_map_index`,
  `water_info_map_index` and `underground_map_index`.
- Client 1058 ships the table as `#na#regionmapinfo.bss`: four
  Layout 2 rows (keys 1, 4, 5 and 7), so the doc check finds no
  `regionmapinfo.bss` there. Client 794 has the same four maps in Layout 1,
  under `gamecommondata/binary/en/`.

## Open Questions

### Why the Village Siege Maps Moved to a Later Map Type

The village siege maps hold `4`, the 2016 `VillageSiege` value, up to client
1636, then `9` on clients 1784 and 2107 and `11` from client 2519, each time
the key of the newest village siege map minus one. Every other map keeps
`map_index - 1`. Whether the enum was renumbered or the newest village siege
class reads all three images is open; no client 3482 `.luac` file names a
map type.
