# Empty BSS Tables Format

## Purpose

PABR `.bss` tables the client ships with no records. Each is 20 bytes: the
`PABR` magic, a record count of `0`, a string table with no strings and the
8-byte PABR trailer. Every file below is that on client 3474. On the two
older clients checked it is the same 20 bytes, not in the archive, or (four
files) a table with records that this doc does not cover:

| File                                  | Client 1784 | Client 1485 |
| ------------------------------------- | ----------- | ----------- |
| `audiorenewal.bss`                    | empty       | empty       |
| `beginnerroadmaplinkurldata.bss`      | absent      | absent      |
| `cashproduct_discountperiodcheck.bss` | empty       | empty       |
| `cashproductcachedata.bss`            | records     | records     |
| `charactertrigger.bss`                | records     | records     |
| `commonskill.bss`                     | empty       | empty       |
| `dropuiurlinfo.bss`                   | absent      | absent      |
| `enchantlightstone.bss`               | absent      | absent      |
| `equipitemchanage.bss`                | records     | absent      |
| `fishinginfo.bss`                     | empty       | empty       |
| `instancefieldenteroption.bss`        | empty       | absent      |
| `instancefieldmanagement.bss`         | empty       | empty       |
| `itembundle.bss`                      | empty       | empty       |
| `lightstoneenchantgroup.bss`          | absent      | absent      |
| `naktype.bss`                         | empty       | records     |
| `normalgroupquest.bss`                | empty       | empty       |
| `openuiwhennak.bss`                   | absent      | absent      |
| `preloadpcactioncharacter.bss`        | empty       | empty       |
| `shadowarenalist.bss`                 | empty       | empty       |
| `skillselectuiinfo.bss`               | absent      | absent      |
| `spawngroup.bss`                      | empty       | empty       |
| `tempcashstaticstatus.bss`            | absent      | absent      |

The Lightstone names point at Lightstone enhancement and Lightstone
enhancement groups, but no record, Lua function or reference source shows
what a row would hold. `normalgroupquest.bss` is the quest list of the
quest widget's group quest line, a feature the live client keeps off; see
[Normal Group Quests](#normal-group-quests).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                  | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------------- | ----- | -------------- | --------- |
| 1      | 1208 and later | 3483    | `audiorenewal.bss`                    | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `beginnerroadmaplinkurldata.bss`      | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3483    | `cashproduct_discountperiodcheck.bss` | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `cashproductcachedata.bss`            | 20    | 1 String Table | 4         |
| 1      | 822 and later  | 3483    | `charactertrigger.bss`                | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3483    | `commonskill.bss`                     | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `dropuiurlinfo.bss`                   | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `enchantlightstone.bss`               | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `equipitemchanage.bss`                | 20    | 1 String Table | 4         |
| 1      | 805 and later  | 3483    | `fishinginfo.bss`                     | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3483    | `instancefieldenteroption.bss`        | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3483    | `instancefieldmanagement.bss`         | 20    | 1 String Table | 4         |
| 1      | 805 and later  | 3483    | `itembundle.bss`                      | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `lightstoneenchantgroup.bss`          | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `naktype.bss`                         | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3483    | `normalgroupquest.bss`                | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `openuiwhennak.bss`                   | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3483    | `preloadpcactioncharacter.bss`        | 20    | 1 String Table | 4         |
| 1      | 1784 and later | 3483    | `shadowarenalist.bss`                 | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `skillselectuiinfo.bss`               | 20    | 1 String Table | 4         |
| 1      | 805 and later  | 3483    | `spawngroup.bss`                      | 20    | 1 String Table | 4         |
| 1      | 3144 and later | 3483    | `tempcashstaticstatus.bss`            | 20    | 1 String Table | 4         |

| Layout | File                                  | Known         | Unknown    |
| ------ | ------------------------------------- | ------------- | ---------- |
| 1      | `audiorenewal.bss`                    | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `beginnerroadmaplinkurldata.bss`      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `cashproduct_discountperiodcheck.bss` | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `cashproductcachedata.bss`            | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `charactertrigger.bss`                | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `commonskill.bss`                     | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `dropuiurlinfo.bss`                   | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `enchantlightstone.bss`               | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `equipitemchanage.bss`                | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `fishinginfo.bss`                     | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `instancefieldenteroption.bss`        | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `instancefieldmanagement.bss`         | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `itembundle.bss`                      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `lightstoneenchantgroup.bss`          | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `naktype.bss`                         | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `normalgroupquest.bss`                | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `openuiwhennak.bss`                   | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `preloadpcactioncharacter.bss`        | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `shadowarenalist.bss`                 | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `skillselectuiinfo.bss`               | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `spawngroup.bss`                      | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `tempcashstaticstatus.bss`            | 20 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 1             |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3473   | Layout 1             |
| 3464   | Layout 1             |
| 3458   | Layout 1             |
| 3454   | Layout 1             |
| 3444   | Layout 1             |
| 3435   | Layout 1             |
| 3426   | Layout 1             |
| 3418   | Layout 1             |
| 3412   | Layout 1             |
| 3402   | Layout 1             |
| 3396   | Layout 1             |
| 3387   | Layout 1             |
| 3381   | Layout 1             |
| 3373   | Layout 1             |
| 3364   | Layout 1             |
| 3356   | Layout 1             |
| 3349   | Layout 1             |
| 3342   | Layout 1             |
| 3335   | Layout 1             |
| 3326   | Layout 1             |
| 3321   | Layout 1             |
| 3314   | Layout 1             |
| 3303   | Layout 1             |
| 3302   | Layout 1             |
| 3293   | Layout 1             |
| 3283   | Layout 1             |
| 3275   | Layout 1             |
| 3267   | Layout 1             |
| 3258   | Layout 1             |
| 3251   | Layout 1             |
| 3242   | Layout 1             |
| 3235   | Layout 1             |
| 3229   | Layout 1             |
| 3212   | Layout 1             |
| 3203   | Layout 1             |
| 3193   | Layout 1             |
| 3186   | Layout 1             |
| 3177   | Layout 1             |
| 3169   | Layout 1             |
| 3158   | Layout 1             |
| 3151   | Layout 1             |
| 3144   | Layout 1             |
| 3133   | No documented layout |
| 3125   | No documented layout |
| 3118   | No documented layout |
| 3111   | No documented layout |
| 3103   | No documented layout |
| 3095   | No documented layout |
| 3086   | No documented layout |
| 3072   | No documented layout |
| 3062   | No documented layout |
| 3052   | No documented layout |
| 3045   | No documented layout |
| 3037   | No documented layout |
| 3030   | No documented layout |
| 3021   | No documented layout |
| 3012   | No documented layout |
| 3002   | No documented layout |
| 2995   | No documented layout |
| 2987   | No documented layout |
| 2978   | No documented layout |
| 2970   | No documented layout |
| 2959   | No documented layout |
| 2951   | No documented layout |
| 2942   | No documented layout |
| 2935   | No documented layout |
| 2932   | No documented layout |
| 2923   | No documented layout |
| 2919   | No documented layout |
| 2907   | No documented layout |
| 2900   | No documented layout |
| 2891   | No documented layout |
| 2882   | No documented layout |
| 2872   | No documented layout |
| 2863   | No documented layout |
| 2855   | No documented layout |
| 2849   | No documented layout |
| 2844   | No documented layout |
| 2834   | No documented layout |
| 2825   | No documented layout |
| 2819   | No documented layout |
| 2811   | No documented layout |
| 2803   | No documented layout |
| 2794   | No documented layout |
| 2783   | No documented layout |
| 2774   | No documented layout |
| 2765   | No documented layout |
| 2756   | No documented layout |
| 2750   | No documented layout |
| 2743   | No documented layout |
| 2736   | No documented layout |
| 2726   | No documented layout |
| 2717   | No documented layout |
| 2709   | No documented layout |
| 2703   | No documented layout |
| 2695   | No documented layout |
| 2684   | No documented layout |
| 2672   | No documented layout |
| 2665   | No documented layout |
| 2657   | No documented layout |
| 2649   | No documented layout |
| 2644   | No documented layout |
| 2637   | No documented layout |
| 2629   | No documented layout |
| 2619   | No documented layout |
| 2612   | No documented layout |
| 2606   | No documented layout |
| 2602   | No documented layout |
| 2601   | No documented layout |
| 2592   | No documented layout |
| 2583   | No documented layout |
| 2575   | No documented layout |
| 2567   | No documented layout |
| 2560   | No documented layout |
| 2553   | No documented layout |
| 2545   | No documented layout |
| 2538   | No documented layout |
| 2529   | No documented layout |
| 2519   | No documented layout |
| 2513   | No documented layout |
| 2510   | No documented layout |
| 2507   | No documented layout |
| 2503   | No documented layout |
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
| 2005   | No documented layout |
| 2000   | No documented layout |
| 1996   | No documented layout |
| 1991   | No documented layout |
| 1985   | No documented layout |
| 1980   | No documented layout |
| 1969   | No documented layout |
| 1964   | No documented layout |
| 1958   | No documented layout |
| 1950   | No documented layout |
| 1945   | No documented layout |
| 1937   | No documented layout |
| 1933   | No documented layout |
| 1927   | No documented layout |
| 1921   | No documented layout |
| 1914   | No documented layout |
| 1908   | No documented layout |
| 1897   | No documented layout |
| 1892   | No documented layout |
| 1886   | No documented layout |
| 1881   | No documented layout |
| 1871   | No documented layout |
| 1866   | No documented layout |
| 1862   | No documented layout |
| 1854   | No documented layout |
| 1846   | No documented layout |
| 1838   | No documented layout |
| 1832   | No documented layout |
| 1826   | No documented layout |
| 1822   | No documented layout |
| 1818   | No documented layout |
| 1804   | No documented layout |
| 1794   | No documented layout |
| 1790   | No documented layout |
| 1784   | No documented layout |
| 1774   | No documented layout |
| 1771   | No documented layout |
| 1762   | No documented layout |
| 1759   | No documented layout |
| 1754   | No documented layout |
| 1749   | No documented layout |
| 1743   | No documented layout |
| 1737   | No documented layout |
| 1731   | No documented layout |
| 1725   | No documented layout |
| 1717   | No documented layout |
| 1710   | No documented layout |
| 1704   | No documented layout |
| 1698   | No documented layout |
| 1690   | No documented layout |
| 1685   | No documented layout |
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
| 1405   | No documented layout |
| 1401   | No documented layout |
| 1396   | No documented layout |
| 1391   | No documented layout |
| 1390   | No documented layout |
| 1386   | No documented layout |
| 1381   | No documented layout |
| 1379   | No documented layout |
| 1372   | No documented layout |
| 1366   | No documented layout |
| 1364   | No documented layout |
| 1363   | No documented layout |
| 1360   | No documented layout |
| 1358   | No documented layout |
| 1355   | No documented layout |
| 1351   | No documented layout |
| 1348   | No documented layout |
| 1346   | No documented layout |
| 1341   | No documented layout |
| 1340   | No documented layout |
| 1338   | No documented layout |
| 1335   | No documented layout |
| 1333   | No documented layout |
| 1329   | No documented layout |
| 1327   | No documented layout |
| 1324   | No documented layout |
| 1321   | No documented layout |
| 1319   | No documented layout |
| 1318   | No documented layout |
| 1316   | No documented layout |
| 1313   | No documented layout |
| 1311   | No documented layout |
| 1309   | No documented layout |
| 1304   | No documented layout |
| 1292   | No documented layout |
| 1286   | No documented layout |
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
| 1246   | Layout 1             |
| 1239   | Layout 1             |
| 1230   | Layout 1             |
| 1226   | Layout 1             |
| 1220   | Layout 1             |
| 1217   | Layout 1             |
| 1211   | Layout 1             |
| 1210   | Layout 1             |
| 1208   | Layout 1             |
| 1203   | Layout 1             |
| 1197   | Layout 1             |
| 1194   | Layout 1             |
| 1192   | Layout 1             |
| 1187   | Layout 1             |
| 1183   | Layout 1             |
| 1177   | Layout 1             |
| 1173   | Layout 1             |
| 1167   | Layout 1             |
| 1164   | Layout 1             |
| 1156   | Layout 1             |
| 1149   | Layout 1             |
| 1144   | No documented layout |
| 1137   | No documented layout |
| 1132   | No documented layout |
| 1127   | No documented layout |
| 1122   | No documented layout |
| 1118   | No documented layout |
| 1114   | No documented layout |
| 1109   | No documented layout |
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
| 829    | Layout 1             |
| 822    | Layout 1             |
| 814    | No documented layout |
| 805    | Layout 1             |
| 794    | No documented layout |
| 787    | No documented layout |
| 780    | No documented layout |
| 771    | No documented layout |
| 760    | No documented layout |
| 748    | No documented layout |
| 741    | No documented layout |
| 736    | No documented layout |
| 731    | No documented layout |
| 723    | No documented layout |
| 711    | No documented layout |
| 707    | No documented layout |
| 697    | No documented layout |
| 689    | No documented layout |
| 683    | No documented layout |
| 678    | No documented layout |
| 670    | No documented layout |
| 661    | No documented layout |
| 656    | No documented layout |
| 652    | No documented layout |
| 643    | No documented layout |
| 637    | No documented layout |
| 630    | No documented layout |
| 627    | No documented layout |
| 621    | No documented layout |
| 617    | No documented layout |
| 615    | No documented layout |
| 606    | No documented layout |
| 599    | No documented layout |
| 592    | No documented layout |
| 586    | No documented layout |
| 577    | No documented layout |
| 569    | No documented layout |
| 561    | No documented layout |
| 554    | No documented layout |
| 542    | No documented layout |
| 532    | No documented layout |
| 531    | No documented layout |
| 526    | No documented layout |
| 521    | No documented layout |
| 517    | No documented layout |
| 510    | No documented layout |
| 508    | No documented layout |
| 504    | No documented layout |
| 497    | No documented layout |
| 491    | No documented layout |
| 485    | No documented layout |
| 478    | No documented layout |
| 472    | No documented layout |
| 466    | No documented layout |
| 457    | No documented layout |
| 452    | No documented layout |
| 449    | No documented layout |
| 435    | No documented layout |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The PABR string table layout of `buffsimply.bss` (`_common/pabr_strings.py`)
with no rows. No record structure can be inferred because the files hold no
records.

| Offset              | Type         | Field        | Notes                                              |
| ------------------- | ------------ | ------------ | -------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                       |
| `+0x04`             | u32          | count        | Number of records; `0` in every file               |
| `+0x08`             | String Table | string_table | See String Table                                   |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x08` in every file   |
| `string_table+0x04` | u32          | zero         | Always 0                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | `0` in every file    |
| `+0x04` | pstr[string_count] | strings      | Empty                |

## Normal Group Quests

The client Lua on client 3474 reads `normalgroupquest.bss` through four
functions, all behind one switch: `global_contentsoptions.luac` sets
`_ContentsGroup_NormalGroupQuest = ToClient_IsContentsGroupOpen("1684")`,
and contents group `1684` is closed on client 3474
([`contentsgroupoptionstaticstatusmanager.bss`](contentsgroupoptionstaticstatusmanager_bss.md)).
The two quest widgets, `panel_widget_checkedquest.luac` and
`panel_widget_questlist_abyssone.luac`, use them the same way:

| Lua function                                 | Use in the quest widget                                                                                       |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `ToClient_GetNormalGroupQuestCount(group, quest)` | Quest count of the quest's group; the first recent quest with a count other than `0` becomes the group quest |
| `ToClient_GetNormalGroupQuestIndex(group, quest)` | The quest's position in its group, from `0`; shown as `index + 1` of the count                           |
| `ToClient_GetNormalGroupName(group, quest)`  | The group name in the `LUA_GROUPQUEST_WORDS_TITLE` line (`group_quest_name`, `group_quest_now`, `group_quest_total`) |
| `ToClient_GetGroupQuestInfo(group, quest)`   | On `FromClient_ClearNormalGroupQuestInformation`, the next quest of the group; `(0, 0)` ends the line         |

While a group quest is set, the widget shows the next quest under
`ToClient_GetGroupQuestTitle(group, quest)` as acceptable and hides it again
on `FromClient_AcceptNormalGroupQuestInformation` for that quest.

On client 1784 the source sheet and the struct name agree with that:

- The `New_Group_Quest` sheet of a private server's
  `DataSheet_QuestRecommendationTable.xlsm` on client 1784 has the columns
  `QuestGroupKey`, `GroupName`, `QuestGroup`, `QuestID` and
  `ContentsGroupKey`, the note columns `#~Title` and `#^E_Merge Index`, and
  no rows. The same sheet in its `DataSheets.bexcel` holds the five compiled
  columns and 0 rows, and its compiled `binary/normalgroupquest.bss` is the
  20 bytes above. The loader's file list names the workbook, which also
  holds the sheets `NewQuest_Table`, `MainQuest_Table`,
  `RecommendationQuest_Table` and `RepetitionQuest_Table`.
- The server dump of that build has four load errors for
  `NormalGroupQuestStaticStatus`: quest `(%#, %#)` has no group name, has a
  wrong key, has a wrong `QuestNo(%#, %#)`, and has no data. A row so holds a
  group name and a quest number `(group, quest)`.
- The same dump's list of string sheet names puts `NormalGroupQuestName`
  between `YachtDiceHandRank` and `SeasonPassQuickQuest`, then
  `SiegeBuildKit` and `YachtGameBoardString`. On client 3474 LOC type 105
  holds the Yar! hand names (`Straight Shot`, `Double Trouble`), 108 the
  Conquest War object descriptions and 109 the Yar! mode descriptions, which
  puts `NormalGroupQuestName` at type 106. The English LOC on client 3474 has
  no type 106 entry.

## Notes

- Raw bytes of every file on client 3474, and of every file marked empty on
  clients 1784 and 1485:
  `50 41 42 52 00 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00`.
- The list comes from a scan of every `.bss` under `gamecommondata/binary/`
  on client 3474 for files of at most 40 bytes. The spawn grid files under
  `mapdata_*/spawnplacementfieldgrid/` are left out.
- Four files with these 20 bytes on client 3474 hold records on an older
  client: `cashproductcachedata.bss` (1,509,235 bytes on client 1784,
  1,097.1 KB on client 1485), `charactertrigger.bss` (307 bytes, count 9, on
  clients 1784 and 1485), `equipitemchanage.bss` (464 bytes, count 37, on
  client 1784) and `naktype.bss` (empty on client 1784, 455 bytes and count 4
  on client 1485). The handler reads the live empty layout and rejects the
  older files; their record layouts wait for multi-version support.
- Two 20-byte PABR files are not empty tables: `cashproduct_newbieproduct.bss`
  holds `0x18CAD` at `+0x04` and `petfeedcount.bss` holds `10` there, each
  with no row bytes before the string table, so the u32 is a single value.
  They have their own docs,
  [cashproduct_newbieproduct](cashproduct_newbieproduct_bss.md) and
  [petfeedcount](petfeedcount_bss.md).
- Neither Lightstone file is in the client 1784 archive. The 2016 PDB, a
  private server's `DataSheets.bexcel`, `.xlsm` sheets, compiled `binary/`
  folder and server dump on client 1784 hold no table, file, struct or
  loader with `LightStone` in its name. That `ContentsGroupOption` sheet has
  no key between `1795` and `2000`, so contents group `1801` (below) is newer
  than client 1784 too.
- The installed `BlackDesert64.exe` (client 3473) holds neither Lightstone
  file name as ASCII or UTF-16 text, so it does not show the loader or its
  struct.
- The client Lua on client 3473 (3,073 `.luac` files) names neither
  Lightstone file. `global_contentsoptions.luac` sets
  `_ContentsGroup_EnchantLightStone = ToClient_IsContentsGroupOpen("1801")`,
  and no other Lua file reads `_ContentsGroup_EnchantLightStone`. The
  Lightstone bag (`_ContentsGroup_LightStoneBag`, contents group `1815`) and
  the set lookups (`ToClient_getLightStoneSet`, read from
  [`lightstoneset.bss`](lightstoneset_bss.md)) are separate features.
- The 2016 PDB has no `NormalGroupQuest` type.
- calpheonlabs lists `normalgroupquest.bss` with a decoder but no field
  ledger, so it gives no layout to compare.
- One handler class (`EmptyTableHandler`, `_common/empty_table.py`) with the
  PABR reader in `_bss/empty_tables/parser.py` previews every file in
  `_bss/empty_tables/tables.py`. A file that declares a record or a string
  raises an error, so a client that fills one of these tables shows up as a
  parse error and in the tests.
- The zero-count `.dbss` tables have their own doc:
  [empty](empty_dbss.md).

## Open Questions

### Record Layout

No client checked has a record in any of these files, so every row layout
is unknown. When a client ships `count > 0`, the file moves to its own doc
and handler, with rows starting at `+0x08` and ending at `table_start`. For
`normalgroupquest.bss` the five compiled `New_Group_Quest` columns are the
lead (`QuestGroupKey`, `GroupName`, `QuestGroup`, `QuestID`,
`ContentsGroupKey`); their types and order in the file are unknown. Whether
the group names come from LOC type 106 keyed by `QuestGroupKey`, as the
group names of the four quest lists of [`newquest.bss`](newquest_bss.md)
come from their own LOC types, is open too.

### Contents Group 1801

The Lua defines `_ContentsGroup_EnchantLightStone` for contents group `1801`
but never reads it. Whether that group gates whatever reads these two tables
is unknown.
