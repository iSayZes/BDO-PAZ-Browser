# `worldmapoptionstaticstatusmanager.bss` Format

## Purpose

A world map option table of one world position per territory: on client
3482 its 14 rows count `0` to `13`, the LOC type 12 territory keys from
Balenos to Inner Edania, and each position lies inside the territory of
its row. What the world map does with the positions is open.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ------- | --------- |
| 1      | 3435 and later | 3483    | `worldmapoptionstaticstatusmanager.bss` | 244   | 14 Row  | 16        |

| Layout | File                                    | Known       | Unknown       |
| ------ | --------------------------------------- | ----------- | ------------- |
| 1      | `worldmapoptionstaticstatusmanager.bss` | 20 B (8.2%) | 224 B (91.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3464   | Layout 1 |
| 3458   | Layout 1 |
| 3454   | Layout 1 |
| 3444   | Layout 1 |
| 3435   | Layout 1 |
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
| 3133   | No file  |
| 3125   | No file  |
| 3118   | No file  |
| 3111   | No file  |
| 3103   | No file  |
| 3095   | No file  |
| 3086   | No file  |
| 3072   | No file  |
| 3062   | No file  |
| 3052   | No file  |
| 3045   | No file  |
| 3037   | No file  |
| 3030   | No file  |
| 3021   | No file  |
| 3012   | No file  |
| 3002   | No file  |
| 2995   | No file  |
| 2987   | No file  |
| 2978   | No file  |
| 2970   | No file  |
| 2959   | No file  |
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
| 2560   | No file  |
| 2553   | No file  |
| 2545   | No file  |
| 2538   | No file  |
| 2529   | No file  |
| 2519   | No file  |
| 2513   | No file  |
| 2510   | No file  |
| 2507   | No file  |
| 2503   | No file  |
| 2498   | No file  |
| 2492   | No file  |
| 2487   | No file  |
| 2480   | No file  |
| 2474   | No file  |
| 2468   | No file  |
| 2460   | No file  |
| 2453   | No file  |
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
| 1921   | No file  |
| 1914   | No file  |
| 1908   | No file  |
| 1897   | No file  |
| 1892   | No file  |
| 1886   | No file  |
| 1881   | No file  |
| 1871   | No file  |
| 1866   | No file  |
| 1862   | No file  |
| 1854   | No file  |
| 1846   | No file  |
| 1838   | No file  |
| 1832   | No file  |
| 1826   | No file  |
| 1822   | No file  |
| 1818   | No file  |
| 1804   | No file  |
| 1794   | No file  |
| 1790   | No file  |
| 1784   | No file  |
| 1774   | No file  |
| 1771   | No file  |
| 1762   | No file  |
| 1759   | No file  |
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

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (16 bytes)

| Offset  | Type   | Field      | Notes                                                |
| ------- | ------ | ---------- | ---------------------------------------------------- |
| `+0x00` | u16    | unknown_00 | The row's position, `0` to `13` on client 3482       |
| `+0x02` | u16    | unknown_02 | Equal to `unknown_00` on every row (client 3482)     |
| `+0x04` | f32[3] | unknown_04 | World `x, y, z`; see Positions                       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Positions

Client 3482, rounded to whole units, with the LOC type 12 territory name
of the row's `unknown_00`:

| `unknown_00` | Territory (LOC type 12)    | x          | y      | z          |
| ------------ | -------------------------- | ---------- | ------ | ---------- |
| `0`          | Balenos                    | -27,413    | 31,792 | 180,549    |
| `1`          | Serendia                   | 4,329      | 39,165 | -76,638    |
| `2`          | Calpheon                   | -274,896   | 40,374 | -54,047    |
| `3`          | Mediah                     | 228,957    | 37,767 | 5,386      |
| `4`          | Valencia                   | 762,119    | 47,710 | 163,193    |
| `5`          | The Great Ocean            | -657,330   | 32,286 | 931,828    |
| `6`          | Kamasylvia                 | -466,849   | 49,392 | -369,512   |
| `7`          | Drieghan                   | -70,966    | 55,845 | -315,808   |
| `8`          | O'dyllita                  | -236,009   | 52,212 | -558,866   |
| `9`          | Mountain of Eternal Winter | 113,077    | 61,250 | -448,362   |
| `10`         | Land of the Morning Light  | -1,297,222 | 44,018 | 1,273,371  |
| `11`         | Ulukita                    | 371,205    | 44,703 | -300,007   |
| `12`         | Outer Edania               | 601,117    | 41,781 | 590,163    |
| `13`         | Inner Edania               | 1,000,000  | 46,300 | 751,000    |

## Field Names

No reference source names the fields. The file is not in client 1784, a
private server's `DataSheets.bexcel` on client 1784 has no sheet with
`WorldMapOption` in its name, and no client Lua file of client 3482
names the table or a getter that returns one of the positions. The
fields stay `unknown_<offset>`.

## Notes

- Row `13` (Inner Edania) holds the round `x` `1,000,000` and `z`
  `751,000`; the other rows hold no round numbers.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/ui_tables.py`. With no
  named field it shows each row's 16 bytes.

## Open Questions

### What the Positions Are

The two u16 fields count up as the LOC type 12 territory keys do, and
each position falls in the territory of that key (Valencia far east,
Kamasylvia and O'dyllita in the north-west, Edania in the south-east), so
the rows read as one point per territory: a camera target, a label
position or a centre. Which one, and why the key is stored twice, needs a
getter in a newer Lua or a sheet; until then the three fields keep their
offset names.
