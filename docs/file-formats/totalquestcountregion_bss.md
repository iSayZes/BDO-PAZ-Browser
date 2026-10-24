# `totalquestcountregion.bss` Format

## Purpose

Quest totals. `totalquestcountregion.bss` holds the number of quests per quest region (`CppEnums.QuestRegionType` in the client Lua) and `totalquestcounttype.bss` the number of quests per quest type (`__eQuestType`). Value N of a file counts the quests of enum value N; the files store no keys. Both files share this layout and one handler class. On client 3474 the type file's values are, value for value, how many `quest.dbss` records hold each `quest_category` (see [Quest Types](#quest-types)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | -------------- | --------- |
| 1      | 1109 and later | 3483    | `totalquestcountregion.bss` | 88    | 1 String Table | 4         |
| 1      | 1109 and later | 3483    | `totalquestcounttype.bss`   | 96    | 1 String Table | 4         |

| Layout | File                        | Known         | Unknown    |
| ------ | --------------------------- | ------------- | ---------- |
| 1      | `totalquestcountregion.bss` | 88 B (100.0%) | 0 B (0.0%) |
| 1      | `totalquestcounttype.bss`   | 96 B (100.0%) | 0 B (0.0%) |

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
| 3426   | Layout 1 |
| 3418   | Layout 1 |
| 3412   | Layout 1 |
| 3402   | Layout 1 |
| 3396   | Layout 1 |
| 3387   | Layout 1 |
| 3381   | Layout 1 |
| 3373   | Layout 1 |
| 3364   | Layout 1 |
| 3356   | Layout 1 |
| 3349   | Layout 1 |
| 3342   | Layout 1 |
| 3335   | Layout 1 |
| 3326   | Layout 1 |
| 3321   | Layout 1 |
| 3314   | Layout 1 |
| 3303   | Layout 1 |
| 3302   | Layout 1 |
| 3293   | Layout 1 |
| 3283   | Layout 1 |
| 3275   | Layout 1 |
| 3267   | Layout 1 |
| 3258   | Layout 1 |
| 3251   | Layout 1 |
| 3242   | Layout 1 |
| 3235   | Layout 1 |
| 3229   | Layout 1 |
| 3212   | Layout 1 |
| 3203   | Layout 1 |
| 3193   | Layout 1 |
| 3186   | Layout 1 |
| 3177   | Layout 1 |
| 3169   | Layout 1 |
| 3158   | Layout 1 |
| 3151   | Layout 1 |
| 3144   | Layout 1 |
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
| 2951   | Layout 1 |
| 2942   | Layout 1 |
| 2935   | Layout 1 |
| 2932   | Layout 1 |
| 2923   | Layout 1 |
| 2919   | Layout 1 |
| 2907   | Layout 1 |
| 2900   | Layout 1 |
| 2891   | Layout 1 |
| 2882   | Layout 1 |
| 2872   | Layout 1 |
| 2863   | Layout 1 |
| 2855   | Layout 1 |
| 2849   | Layout 1 |
| 2844   | Layout 1 |
| 2834   | Layout 1 |
| 2825   | Layout 1 |
| 2819   | Layout 1 |
| 2811   | Layout 1 |
| 2803   | Layout 1 |
| 2794   | Layout 1 |
| 2783   | Layout 1 |
| 2774   | Layout 1 |
| 2765   | Layout 1 |
| 2756   | Layout 1 |
| 2750   | Layout 1 |
| 2743   | Layout 1 |
| 2736   | Layout 1 |
| 2726   | Layout 1 |
| 2717   | Layout 1 |
| 2709   | Layout 1 |
| 2703   | Layout 1 |
| 2695   | Layout 1 |
| 2684   | Layout 1 |
| 2672   | Layout 1 |
| 2665   | Layout 1 |
| 2657   | Layout 1 |
| 2649   | Layout 1 |
| 2644   | Layout 1 |
| 2637   | Layout 1 |
| 2629   | Layout 1 |
| 2619   | Layout 1 |
| 2612   | Layout 1 |
| 2606   | Layout 1 |
| 2602   | Layout 1 |
| 2601   | Layout 1 |
| 2592   | Layout 1 |
| 2583   | Layout 1 |
| 2575   | Layout 1 |
| 2567   | Layout 1 |
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
| 2444   | Layout 1 |
| 2438   | Layout 1 |
| 2434   | Layout 1 |
| 2429   | Layout 1 |
| 2421   | Layout 1 |
| 2414   | Layout 1 |
| 2407   | Layout 1 |
| 2401   | Layout 1 |
| 2397   | Layout 1 |
| 2393   | Layout 1 |
| 2384   | Layout 1 |
| 2378   | Layout 1 |
| 2372   | Layout 1 |
| 2358   | Layout 1 |
| 2352   | Layout 1 |
| 2347   | Layout 1 |
| 2343   | Layout 1 |
| 2335   | Layout 1 |
| 2327   | Layout 1 |
| 2324   | Layout 1 |
| 2319   | Layout 1 |
| 2313   | Layout 1 |
| 2308   | Layout 1 |
| 2302   | Layout 1 |
| 2295   | Layout 1 |
| 2290   | Layout 1 |
| 2284   | Layout 1 |
| 2276   | Layout 1 |
| 2269   | Layout 1 |
| 2259   | Layout 1 |
| 2250   | Layout 1 |
| 2243   | Layout 1 |
| 2235   | Layout 1 |
| 2229   | Layout 1 |
| 2224   | Layout 1 |
| 2218   | Layout 1 |
| 2215   | Layout 1 |
| 2207   | Layout 1 |
| 2203   | Layout 1 |
| 2196   | Layout 1 |
| 2192   | Layout 1 |
| 2189   | Layout 1 |
| 2183   | Layout 1 |
| 2179   | Layout 1 |
| 2171   | Layout 1 |
| 2163   | Layout 1 |
| 2156   | Layout 1 |
| 2151   | Layout 1 |
| 2147   | Layout 1 |
| 2142   | Layout 1 |
| 2138   | Layout 1 |
| 2134   | Layout 1 |
| 2130   | Layout 1 |
| 2122   | Layout 1 |
| 2107   | Layout 1 |
| 2098   | Layout 1 |
| 2089   | Layout 1 |
| 2081   | Layout 1 |
| 2073   | Layout 1 |
| 2067   | Layout 1 |
| 2063   | Layout 1 |
| 2059   | Layout 1 |
| 2052   | Layout 1 |
| 2044   | Layout 1 |
| 2039   | Layout 1 |
| 2032   | Layout 1 |
| 2025   | Layout 1 |
| 2011   | Layout 1 |
| 2005   | Layout 1 |
| 2000   | Layout 1 |
| 1996   | Layout 1 |
| 1991   | Layout 1 |
| 1985   | Layout 1 |
| 1980   | Layout 1 |
| 1969   | Layout 1 |
| 1964   | Layout 1 |
| 1958   | Layout 1 |
| 1950   | Layout 1 |
| 1945   | Layout 1 |
| 1937   | Layout 1 |
| 1933   | Layout 1 |
| 1927   | Layout 1 |
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
| 1784   | Layout 1 |
| 1774   | Layout 1 |
| 1771   | Layout 1 |
| 1762   | Layout 1 |
| 1759   | Layout 1 |
| 1754   | Layout 1 |
| 1749   | Layout 1 |
| 1743   | Layout 1 |
| 1737   | Layout 1 |
| 1731   | Layout 1 |
| 1725   | Layout 1 |
| 1717   | Layout 1 |
| 1710   | Layout 1 |
| 1704   | Layout 1 |
| 1698   | Layout 1 |
| 1690   | Layout 1 |
| 1685   | Layout 1 |
| 1680   | Layout 1 |
| 1674   | Layout 1 |
| 1668   | Layout 1 |
| 1659   | Layout 1 |
| 1649   | Layout 1 |
| 1642   | Layout 1 |
| 1636   | Layout 1 |
| 1628   | Layout 1 |
| 1622   | Layout 1 |
| 1614   | Layout 1 |
| 1608   | Layout 1 |
| 1602   | Layout 1 |
| 1598   | Layout 1 |
| 1594   | Layout 1 |
| 1590   | Layout 1 |
| 1587   | Layout 1 |
| 1584   | Layout 1 |
| 1579   | Layout 1 |
| 1572   | Layout 1 |
| 1565   | Layout 1 |
| 1559   | Layout 1 |
| 1554   | Layout 1 |
| 1547   | Layout 1 |
| 1537   | Layout 1 |
| 1529   | Layout 1 |
| 1524   | Layout 1 |
| 1519   | Layout 1 |
| 1509   | Layout 1 |
| 1506   | Layout 1 |
| 1504   | Layout 1 |
| 1500   | Layout 1 |
| 1493   | Layout 1 |
| 1489   | Layout 1 |
| 1485   | Layout 1 |
| 1481   | Layout 1 |
| 1474   | Layout 1 |
| 1466   | Layout 1 |
| 1462   | Layout 1 |
| 1459   | Layout 1 |
| 1453   | Layout 1 |
| 1450   | Layout 1 |
| 1445   | Layout 1 |
| 1439   | Layout 1 |
| 1433   | Layout 1 |
| 1430   | Layout 1 |
| 1426   | Layout 1 |
| 1421   | Layout 1 |
| 1417   | Layout 1 |
| 1416   | Layout 1 |
| 1409   | Layout 1 |
| 1405   | Layout 1 |
| 1401   | Layout 1 |
| 1396   | Layout 1 |
| 1391   | Layout 1 |
| 1390   | Layout 1 |
| 1386   | Layout 1 |
| 1381   | Layout 1 |
| 1379   | Layout 1 |
| 1372   | Layout 1 |
| 1366   | Layout 1 |
| 1364   | Layout 1 |
| 1363   | Layout 1 |
| 1360   | Layout 1 |
| 1358   | Layout 1 |
| 1355   | Layout 1 |
| 1351   | Layout 1 |
| 1348   | Layout 1 |
| 1346   | Layout 1 |
| 1341   | Layout 1 |
| 1340   | Layout 1 |
| 1338   | Layout 1 |
| 1335   | Layout 1 |
| 1333   | Layout 1 |
| 1329   | Layout 1 |
| 1327   | Layout 1 |
| 1324   | Layout 1 |
| 1321   | Layout 1 |
| 1319   | Layout 1 |
| 1318   | Layout 1 |
| 1316   | Layout 1 |
| 1313   | Layout 1 |
| 1311   | Layout 1 |
| 1309   | Layout 1 |
| 1304   | Layout 1 |
| 1292   | Layout 1 |
| 1286   | Layout 1 |
| 1280   | Layout 1 |
| 1276   | Layout 1 |
| 1267   | Layout 1 |
| 1261   | Layout 1 |
| 1256   | Layout 1 |
| 1250   | Layout 1 |
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
| 1144   | Layout 1 |
| 1137   | Layout 1 |
| 1132   | Layout 1 |
| 1127   | Layout 1 |
| 1122   | Layout 1 |
| 1118   | Layout 1 |
| 1114   | Layout 1 |
| 1109   | Layout 1 |
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
| `stringtable.bss`     | Optional | Hashes of the GAME sheet keys the quest window names regions and types with (see [stringtable](stringtable_bss.md)) |
| `languagedata_en.loc` | Optional | The text of those keys, LOC type 37                                                               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with no count after the magic: the values start at `+0x04` and fill the space up to the string table.

| Offset              | Type               | Field        | Notes                                                          |
| ------------------- | ------------------ | ------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                                   |
| `+0x04`             | u32[..table_start] | quest_count  | One per enum value, in value order; see Quest Regions and Quest Types |
| `quest_count+0x00`  | String Table       | string_table | See String Table                                               |
| `EOF-0x08`          | u32                | table_start  | Offset of the string table, where `quest_count` ends           |
| `EOF-0x04`          | u32                | zero         | Always `0`                                                     |

The parser takes the value count from the trailer: `(table_start - 4) / 4`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No value reads a string                        |

## Quest Regions

`totalquestcountregion.bss` value N is `CppEnums.QuestRegionType` N (`global_define_cpp_enum.luac`). The file has one value per enum value up to `eQuestRegionType_Count`: 18 on client 3474, 13 on client 1784, whose enum ends at `eQuestRegionType_MountainOfEternalWinter`. The name is the GAME sheet key that `_regionString` in `panel_window_quest_all.luac` gives the value, read through `stringtable.bss` and LOC type 37. The names below are the client 3474 order; the handler applies them only to a file with all 18 values (see Notes).

| Value | Enum name                 | GAME sheet key                         | Name (English LOC)                |
| ----- | ------------------------- | -------------------------------------- | --------------------------------- |
| 0     | `None`                    | `LUA_QUESTLIST_HISTORY_TXT_REGION_99`  | Etc.                              |
| 1     | `Balenos`                 | `LUA_QUESTLIST_HISTORY_TXT_REGION_1`   | Eastern Balenos                   |
| 2     | `Serendia`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_2`   | Serendia                          |
| 3     | `NorthCalpheon`           | `LUA_QUESTLIST_HISTORY_TXT_REGION_3`   | Northern Calpheon                 |
| 4     | `CalpheonBigCity`         | `LUA_QUESTLIST_HISTORY_TXT_REGION_4`   | Calpheon City                     |
| 5     | `Keplan`                  | `LUA_QUESTLIST_HISTORY_TXT_REGION_5`   | Keplan (Southeastern Calpheon)    |
| 6     | `SouthWestCalpheon`       | `LUA_QUESTLIST_HISTORY_TXT_REGION_6`   | Southwestern Calpheon             |
| 7     | `Media`                   | `LUA_QUESTLIST_HISTORY_TXT_REGION_7`   | Mediah                            |
| 8     | `Valencia`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_8`   | Valencia                          |
| 9     | `Kamasylvia`              | `LUA_QUESTLIST_HISTORY_TXT_REGION_9`   | Kamasylvia                        |
| 10    | `Drigan`                  | `LUA_QUESTLIST_HISTORY_TXT_REGION_10`  | Drieghan                          |
| 11    | `Odilita`                 | `LUA_QUESTLIST_HISTORY_TXT_REGION_11`  | O'dyllita                         |
| 12    | `MountainOfEternalWinter` | `LUA_QUESTLIST_HISTORY_TXT_REGION_12`  | Mountain of Eternal Winter        |
| 13    | `AbyssOne`                | `LUA_ABYSSONE_MSG_SERVERSELECT_TITLE`  | Abyss One                         |
| 14    | `MorningLand`             | `LUA_QUESTLIST_HISTORY_TXT_REGION_13`  | Land of the Morning Light - Nampo |
| 15    | `Ulukita`                 | `LUA_QUESTLIST_HISTORY_TXT_REGION_14`  | Ulukita                           |
| 16    | `Edania_1`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_17`  | Outer Edania                      |
| 17    | `Edania_2`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_20`  | Inner Edania                      |

On client 1784 the 13 values add up to 16,877, the record count of that client's `quest.dbss`. On client 3474 the 18 values add up to 18,980, 11 fewer than the 18,991 `quest.dbss` records (see Open Questions).

## Quest Types

`totalquestcounttype.bss` value N is `__eQuestType` N. The value order is the order in which `panel_window_quest_all.luac` lists the `__eQuestType_*` names, and the `_typeString` keys follow it: type N reads `LUA_QUESTLIST_HISTORY_TXT_TYPE_<N+1>`, except `DirectClear`, which reads `LUA_QUESTLIST_HISTORY_TXT_REGION_99`. On client 3474 the 20 values equal the per-category record counts of the `quest.dbss` [Quest Category](quest_dbss.md#quest-category) table for every category `0` to `19` (`16` has no record and holds `0`) and add up to all 18,991 records, so `quest_category` is the quest type. The `Adventurer's Tome` type is category `11`, the journal pages, and `Region Bonus` is category `12`, the quests of `regionmonsterkillquestlist.bss`.

| Value | Enum name                | GAME sheet key                        | Name (English LOC) |
| ----- | ------------------------ | ------------------------------------- | ------------------ |
| 0     | `BlackSpirit`            | `LUA_QUESTLIST_HISTORY_TXT_TYPE_1`    | Black Spirit       |
| 1     | `Main`                   | `LUA_QUESTLIST_HISTORY_TXT_TYPE_2`    | Main               |
| 2     | `Sub`                    | `LUA_QUESTLIST_HISTORY_TXT_TYPE_3`    | General            |
| 3     | `Repeat`                 | `LUA_QUESTLIST_HISTORY_TXT_TYPE_4`    | Recurring          |
| 4     | `Adventure`              | `LUA_QUESTLIST_HISTORY_TXT_TYPE_5`    | Adventure          |
| 5     | `BaseLife`               | `LUA_QUESTLIST_HISTORY_TXT_TYPE_6`    | Life               |
| 6     | `OceanLife`              | `LUA_QUESTLIST_HISTORY_TXT_TYPE_7`    | Sailing            |
| 7     | `CraftLife`              | `LUA_QUESTLIST_HISTORY_TXT_TYPE_8`    | Production         |
| 8     | `Contents`               | `LUA_QUESTLIST_HISTORY_TXT_TYPE_9`    | Content            |
| 9     | `Event`                  | `LUA_QUESTLIST_HISTORY_TXT_TYPE_10`   | Event              |
| 10    | `Guild`                  | `LUA_QUESTLIST_HISTORY_TXT_TYPE_11`   | Guild              |
| 11    | `DirectAccept`           | `LUA_QUESTLIST_HISTORY_TXT_TYPE_12`   | Adventurer's Tome  |
| 12    | `Sudden`                 | `LUA_QUESTLIST_HISTORY_TXT_TYPE_13`   | Region Bonus       |
| 13    | `SeasonPass`             | `LUA_QUESTLIST_HISTORY_TXT_TYPE_14`   | Season Pass        |
| 14    | `GrowthPass`             | `LUA_QUESTLIST_HISTORY_TXT_TYPE_15`   | Progression Pass   |
| 15    | `DirectClear`            | `LUA_QUESTLIST_HISTORY_TXT_REGION_99` | Etc.               |
| 16    | `Journal`                | `LUA_QUESTLIST_HISTORY_TXT_TYPE_17`   | Journal            |
| 17    | `OlviaAcademyPass`       | none                                  | none               |
| 18    | `OlviaAcademyReward`     | none                                  | none               |
| 19    | `OlviaAcademyCurriculum` | none                                  | none               |

`_typeString` has no key for the three Olvia Academy types; the handler shows their enum names. `LUA_QUESTLIST_HISTORY_TXT_TYPE_16` reads "Instant Clear", but the quest window names `DirectClear` "Etc.".

The client 1784 file holds 17 values that add up to 16,877, the record count of that client's `quest.dbss`. That client's Lua has another enum, `CppEnums.QuestType` (`BlackSpirit` `0` to `Guild` `7`, `Special` `10`, `RegionMonsterKill` `11`, `Production` `15`, `_Count` `16`), which is one value short of the file; the 1784 values are not named here (see Open Questions).

## Notes

- Decompressed sizes: `totalquestcountregion.bss` 88 bytes on client 3474 (`4 + 18 × 4 + 12`) and 68 bytes on client 1784; `totalquestcounttype.bss` 96 bytes on client 3474 (`4 + 20 × 4 + 12`) and 84 bytes on client 1784.
- The quest window (`panel_window_quest_all_2.luac`) shows a completion percentage per region or per type group in its progress tab: `ToClient_GetClearedQuestCountByQuestRegion(region) / ToClient_GetTotalQuestCountByQuestRegion(region) * 100`, and the same pair `ByQuestType` when the list is sorted by type. The totals these getters return have the shape of the two files.
- No sheet of a private server's `DataSheets.bexcel` on client 1784 has `TotalQuest` in its name or a column, while that server's `binary/` folder holds both files.
- The handler (`_bss/totalquestcount/`) gives each value its enum value as key (`quest_region` or `quest_type`), the quest window name next to it, and `quest_count`. It names the values only when the file holds at least as many values as the client 3474 enum (18 regions, 20 types); a shorter file, such as both client 1784 files, gets an empty name column, since its enum order is not checked against the client 3474 one. A value past the end of the enum, on a later client, also has no name.

## Open Questions

### Eleven Quests Without a Region Count

On client 3474 the region values add up to 18,980 and the type values to 18,991, the `quest.dbss` record count; on client 1784 both files add up to all 16,877 records. The 11 missing quests may carry a region value outside `QuestRegionType` (the enum has no value past `Edania_2` and `_Count` `18`), but `quest.dbss` has no decoded region field to check which quests they are.

### What Fills the Getters

`ToClient_GetTotalQuestCountByQuestRegion` and `ToClient_GetTotalQuestCountByQuestType` take a region or type value and return a total, which is what these files store per value, but nothing in the client Lua names the files. The client could also count the totals from `quest.dbss` itself, which on client 3474 gives the same type totals.

### Client 1784 Quest Types

The client 1784 type file has 17 values, while that client's Lua `CppEnums.QuestType` ends at `_Count` `16` and has no names for values `8`, `9` and `12` to `14`. Its value `6` holds 6,169 of the 16,877 quests, more than any other type, so the 3474 names (`6` is `OceanLife`) do not carry over. The 1784 `quest.dbss` layout has no decoded `quest_category` to count against. The handler shows no names for the client 1784 files.
