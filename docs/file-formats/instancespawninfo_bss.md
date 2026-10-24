# `instancespawninfo.bss` Format

## Purpose

The hunting grounds of the private monster zones (personal fields, Marni's
Realm): per zone a sector box, a centre point and radius, the Korean area
name, the recommended AP, the scroll a deep entry consumes and the entry
type. The Personal Field window (`panel_window_personalfield_main_all_1.luac`)
lists them through `ToClient_getInstanceSpawnInfoWrapperByIndex(index)`.
On client 3482 the file has 54 zones, from Tshira Ruins (recommended AP
140) to Event Horizon (420). The file is a u32 count and variable rows,
with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes                 |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | ------------------------- |
| 6      | 3435 and later | 3483    | `instancespawninfo.bss` | 4,582 | 54 Row  | 74 to 98, 85 on average   |
| 5      | 3125 to 3426   | 3426    | `instancespawninfo.bss` | 5,122 | 54 Row  | 84 to 108, 95 on average  |
| 4      | 3002 to 3118   | 3118    | `instancespawninfo.bss` | 4,592 | 44 Row  | 93 to 117, 104 on average |
| 3      | 2134 to 2995   | 2995    | `instancespawninfo.bss` | 3,490 | 38 Row  | 80 to 104, 92 on average  |
| 2      | 1881 to 2130   | 2130    | `instancespawninfo.bss` | 2,266 | 25 Row  | 78 to 102, 90 on average  |
| 1      | 1854 to 1871   | 1871    | `instancespawninfo.bss` | 40    | 1 Row   | 36                        |

| Layout | File                    | Known           | Unknown       |
| ------ | ----------------------- | --------------- | ------------- |
| 6      | `instancespawninfo.bss` | 3,664 B (80.0%) | 918 B (20.0%) |
| 5      | `instancespawninfo.bss` | 4,204 B (82.1%) | 918 B (17.9%) |
| 4      | `instancespawninfo.bss` | 4,064 B (88.5%) | 528 B (11.5%) |
| 3      | `instancespawninfo.bss` | 3,338 B (95.6%) | 152 B (4.4%)  |
| 2      | `instancespawninfo.bss` | 2,216 B (97.8%) | 50 B (2.2%)   |
| 1      | `instancespawninfo.bss` | 38 B (95.0%)    | 2 B (5.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 6             |
| 3482   | Layout 6             |
| 3474   | Layout 6             |
| 3473   | Layout 6             |
| 3464   | Layout 6             |
| 3458   | Layout 6             |
| 3454   | Layout 6             |
| 3444   | Layout 6             |
| 3435   | Layout 6             |
| 3426   | Layout 5             |
| 3418   | Layout 5             |
| 3412   | Layout 5             |
| 3402   | Layout 5             |
| 3396   | Layout 5             |
| 3387   | Layout 5             |
| 3381   | Layout 5             |
| 3373   | Layout 5             |
| 3364   | Layout 5             |
| 3356   | Layout 5             |
| 3349   | Layout 5             |
| 3342   | Layout 5             |
| 3335   | Layout 5             |
| 3326   | Layout 5             |
| 3321   | Layout 5             |
| 3314   | Layout 5             |
| 3303   | Layout 5             |
| 3302   | Layout 5             |
| 3293   | Layout 5             |
| 3283   | Layout 5             |
| 3275   | Layout 5             |
| 3267   | Layout 5             |
| 3258   | Layout 5             |
| 3251   | Layout 5             |
| 3242   | Layout 5             |
| 3235   | Layout 5             |
| 3229   | Layout 5             |
| 3212   | Layout 5             |
| 3203   | Layout 5             |
| 3193   | Layout 5             |
| 3186   | Layout 5             |
| 3177   | Layout 5             |
| 3169   | Layout 5             |
| 3158   | Layout 5             |
| 3151   | Layout 5             |
| 3144   | Layout 5             |
| 3133   | Layout 5             |
| 3125   | Layout 5             |
| 3118   | Layout 4             |
| 3111   | Layout 4             |
| 3103   | Layout 4             |
| 3095   | Layout 4             |
| 3086   | Layout 4             |
| 3072   | Layout 4             |
| 3062   | Layout 4             |
| 3052   | Layout 4             |
| 3045   | Layout 4             |
| 3037   | Layout 4             |
| 3030   | Layout 4             |
| 3021   | Layout 4             |
| 3012   | Layout 4             |
| 3002   | Layout 4             |
| 2995   | Layout 3             |
| 2987   | Layout 3             |
| 2978   | Layout 3             |
| 2970   | Layout 3             |
| 2959   | Layout 3             |
| 2951   | Layout 3             |
| 2942   | Layout 3             |
| 2935   | Layout 3             |
| 2932   | Layout 3             |
| 2923   | Layout 3             |
| 2919   | Layout 3             |
| 2907   | Layout 3             |
| 2900   | Layout 3             |
| 2891   | Layout 3             |
| 2882   | Layout 3             |
| 2872   | Layout 3             |
| 2863   | Layout 3             |
| 2855   | Layout 3             |
| 2849   | Layout 3             |
| 2844   | Layout 3             |
| 2834   | Layout 3             |
| 2825   | Layout 3             |
| 2819   | Layout 3             |
| 2811   | Layout 3             |
| 2803   | Layout 3             |
| 2794   | Layout 3             |
| 2783   | Layout 3             |
| 2774   | Layout 3             |
| 2765   | Layout 3             |
| 2756   | Layout 3             |
| 2750   | Layout 3             |
| 2743   | Layout 3             |
| 2736   | Layout 3             |
| 2726   | Layout 3             |
| 2717   | Layout 3             |
| 2709   | Layout 3             |
| 2703   | Layout 3             |
| 2695   | Layout 3             |
| 2684   | Layout 3             |
| 2672   | Layout 3             |
| 2665   | Layout 3             |
| 2657   | Layout 3             |
| 2649   | Layout 3             |
| 2644   | Layout 3             |
| 2637   | Layout 3             |
| 2629   | Layout 3             |
| 2619   | Layout 3             |
| 2612   | Layout 3             |
| 2606   | Layout 3             |
| 2602   | Layout 3             |
| 2601   | Layout 3             |
| 2592   | Layout 3             |
| 2583   | Layout 3             |
| 2575   | Layout 3             |
| 2567   | Layout 3             |
| 2560   | Layout 3             |
| 2553   | Layout 3             |
| 2545   | Layout 3             |
| 2538   | Layout 3             |
| 2529   | Layout 3             |
| 2519   | Layout 3             |
| 2513   | Layout 3             |
| 2510   | Layout 3             |
| 2507   | Layout 3             |
| 2503   | Layout 3             |
| 2498   | Layout 3             |
| 2492   | Layout 3             |
| 2487   | Layout 3             |
| 2480   | Layout 3             |
| 2474   | Layout 3             |
| 2468   | Layout 3             |
| 2460   | Layout 3             |
| 2453   | Layout 3             |
| 2444   | Layout 3             |
| 2438   | Layout 3             |
| 2434   | Layout 3             |
| 2429   | Layout 3             |
| 2421   | Layout 3             |
| 2414   | Layout 3             |
| 2407   | Layout 3             |
| 2401   | Layout 3             |
| 2397   | Layout 3             |
| 2393   | Layout 3             |
| 2384   | Layout 3             |
| 2378   | Layout 3             |
| 2372   | Layout 3             |
| 2358   | Layout 3             |
| 2352   | Layout 3             |
| 2347   | Layout 3             |
| 2343   | Layout 3             |
| 2335   | Layout 3             |
| 2327   | Layout 3             |
| 2324   | Layout 3             |
| 2319   | Layout 3             |
| 2313   | Layout 3             |
| 2308   | Layout 3             |
| 2302   | Layout 3             |
| 2295   | Layout 3             |
| 2290   | Layout 3             |
| 2284   | Layout 3             |
| 2276   | Layout 3             |
| 2269   | Layout 3             |
| 2259   | Layout 3             |
| 2250   | Layout 3             |
| 2243   | Layout 3             |
| 2235   | Layout 3             |
| 2229   | Layout 3             |
| 2224   | Layout 3             |
| 2218   | Layout 3             |
| 2215   | Layout 3             |
| 2207   | Layout 3             |
| 2203   | Layout 3             |
| 2196   | Layout 3             |
| 2192   | Layout 3             |
| 2189   | Layout 3             |
| 2183   | Layout 3             |
| 2179   | Layout 3             |
| 2171   | Layout 3             |
| 2163   | Layout 3             |
| 2156   | Layout 3             |
| 2151   | Layout 3             |
| 2147   | Layout 3             |
| 2142   | Layout 3             |
| 2138   | Layout 3             |
| 2134   | Layout 3             |
| 2130   | Layout 2             |
| 2122   | Layout 2             |
| 2107   | Layout 2             |
| 2098   | Layout 2             |
| 2089   | Layout 2             |
| 2081   | Layout 2             |
| 2073   | Layout 2             |
| 2067   | Layout 2             |
| 2063   | Layout 2             |
| 2059   | Layout 2             |
| 2052   | Layout 2             |
| 2044   | Layout 2             |
| 2039   | Layout 2             |
| 2032   | Layout 2             |
| 2025   | Layout 2             |
| 2011   | Layout 2             |
| 2005   | Layout 2             |
| 2000   | Layout 2             |
| 1996   | Layout 2             |
| 1991   | Layout 2             |
| 1985   | Layout 2             |
| 1980   | Layout 2             |
| 1969   | Layout 2             |
| 1964   | Layout 2             |
| 1958   | Layout 2             |
| 1950   | Layout 2             |
| 1945   | Layout 2             |
| 1937   | Layout 2             |
| 1933   | Layout 2             |
| 1927   | Layout 2             |
| 1921   | Layout 2             |
| 1914   | Layout 2             |
| 1908   | Layout 2             |
| 1897   | Layout 2             |
| 1892   | Layout 2             |
| 1886   | Layout 2             |
| 1881   | Layout 2             |
| 1871   | Layout 1             |
| 1866   | Layout 1             |
| 1862   | Layout 1             |
| 1854   | Layout 1             |
| 1846   | No documented layout |
| 1838   | No file              |
| 1832   | No file              |
| 1826   | No file              |
| 1822   | No file              |
| 1818   | No file              |
| 1804   | No file              |
| 1794   | No file              |
| 1790   | No file              |
| 1784   | No file              |
| 1774   | No file              |
| 1771   | No file              |
| 1762   | No file              |
| 1759   | No file              |
| 1754   | No file              |
| 1749   | No file              |
| 1743   | No file              |
| 1737   | No file              |
| 1731   | No file              |
| 1725   | No file              |
| 1717   | No file              |
| 1710   | No file              |
| 1704   | No file              |
| 1698   | No file              |
| 1690   | No file              |
| 1685   | No file              |
| 1680   | No file              |
| 1674   | No file              |
| 1668   | No file              |
| 1659   | No file              |
| 1649   | No file              |
| 1642   | No file              |
| 1636   | No file              |
| 1628   | No file              |
| 1622   | No file              |
| 1614   | No file              |
| 1608   | No file              |
| 1602   | No file              |
| 1598   | No file              |
| 1594   | No file              |
| 1590   | No file              |
| 1587   | No file              |
| 1584   | No file              |
| 1579   | No file              |
| 1572   | No file              |
| 1565   | No file              |
| 1559   | No file              |
| 1554   | No file              |
| 1547   | No file              |
| 1537   | No file              |
| 1529   | No file              |
| 1524   | No file              |
| 1519   | No file              |
| 1509   | No file              |
| 1506   | No file              |
| 1504   | No file              |
| 1500   | No file              |
| 1493   | No file              |
| 1489   | No file              |
| 1485   | No file              |
| 1481   | No file              |
| 1474   | No file              |
| 1466   | No file              |
| 1462   | No file              |
| 1459   | No file              |
| 1453   | No file              |
| 1450   | No file              |
| 1445   | No file              |
| 1439   | No file              |
| 1433   | No file              |
| 1430   | No file              |
| 1426   | No file              |
| 1421   | No file              |
| 1417   | No file              |
| 1416   | No file              |
| 1409   | No file              |
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

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `languagedata_en.loc` | Optional | Item names of `enter_item_key` (LOC type 0) |

All multi-byte values are little-endian.

## Layout 6

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 68 bytes + name text)

| Offset              | Type  | Field                       | Notes |
| ------------------- | ----- | --------------------------- | ----- |
| `+0x00`             | u16   | key                         | Row key, `0` to `53` (client 3482), not sorted |
| `+0x02`             | i32   | max_x                       | Sector box, upper corner, in world units; a multiple of 12,800 (one sector) |
| `+0x06`             | i32   | max_z                       | |
| `+0x0A`             | i32   | min_x                       | Lower corner |
| `+0x0E`             | i32   | min_z                       | |
| `+0x12`             | u16   | unknown_12                  | Equals `key` on every row of every client |
| `+0x14`             | f32   | x                           | Centre point (centimetres), inside the box on every row |
| `+0x18`             | f32   | y                           | |
| `+0x1C`             | f32   | z                           | |
| `+0x20`             | f32   | radius                      | Centimetres around the centre point (`5000` to `30000`) |
| `+0x24`             | str16 | area_name_kr                | Korean area name (`트쉬라 폐허`, `[엘비아] 오크 캠프`) |
| `area_name_kr+0x00` | f32   | offense_point               | Recommended AP, a whole number (`140` to `420`) |
| `area_name_kr+0x04` | u16   | unknown_area_name_kr_04     | `1` on every row |
| `area_name_kr+0x06` | u32   | enter_item_key              | Item a deep entry consumes, `0` for none (`761679` Zephyros Castle Scroll) |
| `area_name_kr+0x0A` | u32   | unknown_area_name_kr_0a     | `1` where `enter_item_key` is set, else `0` |
| `area_name_kr+0x0E` | u32   | unknown_area_name_kr_0e     | `0` on every row |
| `area_name_kr+0x12` | u8    | enter_type                  | `1` on the ten Edania zones, else `0`; see [Field Names](#field-names) |
| `area_name_kr+0x13` | u32   | unknown_item_key            | A different item key on every row; see [unknown_item_key](#unknown_item_key) |
| `area_name_kr+0x17` | u8    | unknown_area_name_kr_17     | `0` to `4`; `4` on the ten Edania zones |

## Layout 5

Clients 3144 to 3412 store the recommended AP as Korean text (`추천 공격력 340`,
"recommended AP 340") right after the name; the fields after it are the
same.

### Row (variable: 72 bytes + texts)

| Offset                 | Type  | Field                   | Notes |
| ---------------------- | ----- | ----------------------- | ----- |
| `+0x00`                | u16   | key                     | |
| `+0x02`                | i32   | max_x                   | |
| `+0x06`                | i32   | max_z                   | |
| `+0x0A`                | i32   | min_x                   | |
| `+0x0E`                | i32   | min_z                   | |
| `+0x12`                | u16   | unknown_12              | |
| `+0x14`                | f32   | x                       | |
| `+0x18`                | f32   | y                       | |
| `+0x1C`                | f32   | z                       | |
| `+0x20`                | f32   | radius                  | |
| `+0x24`                | str16 | area_name_kr            | |
| `area_name_kr+0x00`    | str16 | offense_text_kr         | `추천 공격력` and the AP |
| `offense_text_kr+0x00` | u16   | unknown_area_name_kr_04 | |
| `offense_text_kr+0x02` | u32   | enter_item_key          | |
| `offense_text_kr+0x06` | u32   | unknown_area_name_kr_0a | |
| `offense_text_kr+0x0A` | u32   | unknown_area_name_kr_0e | |
| `offense_text_kr+0x0E` | u8    | enter_type              | |
| `offense_text_kr+0x0F` | u32   | unknown_item_key        | |
| `offense_text_kr+0x13` | u8    | unknown_area_name_kr_17 | |

## Layout 4

Clients 3002 to 3103 end the row after `enter_type`.

### Row (variable: 67 bytes + texts)

| Offset                 | Type  | Field                   | Notes |
| ---------------------- | ----- | ----------------------- | ----- |
| `+0x00`                | u16   | key                     | |
| `+0x02`                | i32   | max_x                   | |
| `+0x06`                | i32   | max_z                   | |
| `+0x0A`                | i32   | min_x                   | |
| `+0x0E`                | i32   | min_z                   | |
| `+0x12`                | u16   | unknown_12              | |
| `+0x14`                | f32   | x                       | |
| `+0x18`                | f32   | y                       | |
| `+0x1C`                | f32   | z                       | |
| `+0x20`                | f32   | radius                  | |
| `+0x24`                | str16 | area_name_kr            | |
| `area_name_kr+0x00`    | str16 | offense_text_kr         | |
| `offense_text_kr+0x00` | u16   | unknown_area_name_kr_04 | |
| `offense_text_kr+0x02` | u32   | enter_item_key          | |
| `offense_text_kr+0x06` | u32   | unknown_area_name_kr_0a | |
| `offense_text_kr+0x0A` | u32   | unknown_area_name_kr_0e | |
| `offense_text_kr+0x0E` | u8    | enter_type              | |

## Layout 3

Clients 2134 to 2959 end the row after `unknown_area_name_kr_04`.

### Row (variable: 54 bytes + texts)

| Offset                 | Type  | Field                   | Notes |
| ---------------------- | ----- | ----------------------- | ----- |
| `+0x00`                | u16   | key                     | |
| `+0x02`                | i32   | max_x                   | |
| `+0x06`                | i32   | max_z                   | |
| `+0x0A`                | i32   | min_x                   | |
| `+0x0E`                | i32   | min_z                   | |
| `+0x12`                | u16   | unknown_12              | |
| `+0x14`                | f32   | x                       | |
| `+0x18`                | f32   | y                       | |
| `+0x1C`                | f32   | z                       | |
| `+0x20`                | f32   | radius                  | |
| `+0x24`                | str16 | area_name_kr            | |
| `area_name_kr+0x00`    | str16 | offense_text_kr         | |
| `offense_text_kr+0x00` | u16   | unknown_area_name_kr_04 | |

## Layout 2

Clients 1886 to 2107 end the row after the AP text.

### Row (variable: 52 bytes + texts)

| Offset              | Type  | Field           | Notes |
| ------------------- | ----- | --------------- | ----- |
| `+0x00`             | u16   | key             | |
| `+0x02`             | i32   | max_x           | |
| `+0x06`             | i32   | max_z           | |
| `+0x0A`             | i32   | min_x           | |
| `+0x0E`             | i32   | min_z           | |
| `+0x12`             | u16   | unknown_12      | |
| `+0x14`             | f32   | x               | |
| `+0x18`             | f32   | y               | |
| `+0x1C`             | f32   | z               | |
| `+0x20`             | f32   | radius          | |
| `+0x24`             | str16 | area_name_kr    | |
| `area_name_kr+0x00` | str16 | offense_text_kr | |

## Layout 1

Client 1866 has one row and no texts: the row ends after `radius`.

### Row (36 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u16  | key        | `0` |
| `+0x02` | i32  | max_x      | |
| `+0x06` | i32  | max_z      | |
| `+0x0A` | i32  | min_x      | |
| `+0x0E` | i32  | min_z      | |
| `+0x12` | u16  | unknown_12 | |
| `+0x14` | f32  | x          | |
| `+0x18` | f32  | y          | |
| `+0x1C` | f32  | z          | |
| `+0x20` | f32  | radius     | |

## Field Names

The names follow the getters of the wrapper the Personal Field window
reads (`panel_window_personalfield_main_all_1.luac`,
`panel_widget_personalfield_all_1.luac`, client 3482): `getAreaName()`,
`getCenterPos()`, `getRadius()` (the window offers the entry button below
80% of it), `getOffensePoint()` (shown after the "AP" label of
`LUA_DROPINFO_MYVIEWSTATSINFO_ATT`), `getEnterItemKey()` and
`getEnterType()`. The scrolls of `enter_item_key` say they are consumed on
entry to that zone (`761679` Zephyros Castle Scroll, `980137` Event
Horizon Scroll). `getEnterType()` is compared with
`__ePersonalMirrorFieldEnterType_Edania` to pick the Edania or the
Atoraxion button texture; `enter_type` is `1` on the ten zones whose
scroll pays a tax to an Edana (the five castles `39` to `43` and the
five zones `49` to `53`, Aphrodon Temple to Event Horizon) and `0` on Orzekea, whose entry item is
Maha's Fragment `757182` of Atoraxion. The getters `getIndex()` and
`getFieldNo()` match `key` or `unknown_12`; the two are equal on every row,
so which is which is not shown. The box fields follow the corner order of
the centre point: `max_x` is above and `min_x` below `x` on all 54 rows.
The file is not in client 1784 and has no sheet in a private server's
`DataSheets.bexcel` on client 1784.

## Notes

- Row counts: 24 on client 2107, 38 on clients 2519 and 2765, 42 on
  client 3002, 48 on client 3251 and 54 on client 3482.

## Open Questions

### unknown_item_key

Every row holds an item key that LOC type 0 names: Decayed Cloth `65330`
in `어둠 추종자 침소`, Hardened Lava Chunk `767248` in Zephyros Castle,
Black Crystal Fragment `980128` in Event Horizon. They look like a
typical drop of the zone, which the looting report window
(`panel_window_lootingitemreport_main_all_1.luac`) could show, but the Lua
reads no such getter.

### unknown_area_name_kr_17

`0` to `4`, with `4` on every Edania zone. It is not the recommended AP
band (Tshira Ruins at 140 has `2`, Hystria Ruins at 230 also `2`).
What it selects is open.
