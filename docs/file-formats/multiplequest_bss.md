# `multiplequest.bss` Format

## Purpose

Quest ID ranges: per quest chain a first and a last quest ID. The quests of a range are versions of one quest, and the `condition_script` of each version in `quest.dbss` lets a character see one of them at a time: by life skill level, contribution points, an owned item, a random roll or a knowledge entry (see [Ranges](#ranges)). No quest script names another quest of its own range, while chains 4549 and 9053, two ranges of the same Training quest, exclude each other by script. What the game does with a range is open (see Open Questions). The plain PABR file holds fixed-size rows, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 1405 and later | 3483    | `multiplequest.bss` | 266   | 41 Row  | 6         |

| Layout | File                | Known          | Unknown    |
| ------ | ------------------- | -------------- | ---------- |
| 1      | `multiplequest.bss` | 266 B (100.0%) | 0 B (0.0%) |

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

| File                  | Required | Role                                                                           |
| --------------------- | -------- | ------------------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 at `str_id1=quest_chain_id`, `str_id2=min_quest_id` or `max_quest_id` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                                    |
| ------------------- | ------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                             |
| `+0x04`             | u32          | count              | Number of rows                                           |
| `+0x08`             | Row[count]   | rows               | See Row                                                  |
| `rows+0x00`         | String Table | string_table       | The PABR string table, present but empty                 |
| `string_table+0x00` | u32          | string_table_start | Absolute offset of `string_count`; equals `8 + 6 × count` |
| `string_table+0x04` | u32          | zero               | Always `0`                                               |

The string table tail is the one `barterlifelevelinfo.bss` and `questprogressgroup.bss` use (`_common/pabr_strings.py`).

### Row (6 bytes)

| Offset  | Type | Field          | Notes                                                                   |
| ------- | ---- | -------------- | ----------------------------------------------------------------------- |
| `+0x00` | u16  | quest_chain_id | LOC type 18 `str_id1`; unique per row                                   |
| `+0x02` | u16  | min_quest_id   | First quest of the range, LOC type 18 `str_id2`                          |
| `+0x04` | u16  | max_quest_id   | Last quest of the range, LOC type 18 `str_id2`; never below `min_quest_id` |

`quest_chain_id` with a quest ID is the quest key, the `(quest_id << 16) | quest_chain_id` of `allquestlist.bss` read as two u16 values.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Ranges

On client 3474 the file holds 41 rows. In 39 of them every quest from `min_quest_id` to `max_quest_id` is a `quest.dbss` record; chains 11210 (1 to 23) and 11368 (1 to 3) have no record at all. `min_quest_id` is `1` on 39 rows and `2` on chains 3907 and 11422.

What the `condition_script` of the quests in a range checks, client 3474:

| Chains                       | Range              | Quests                                                                     | Each version needs                                         |
| ---------------------------- | ------------------ | -------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 4549, 9053                   | 1 to 7             | `[Daily] [Beginner]` to `[Guru] No Worries for the Prepared`               | A Training level band, `getLifeLevel(6)`                   |
| 4576, 9054                   | 1 to 8             | `Krogdalo's Origin Stone Support`, then `[Beginner]` to `[Guru] Carrot Confit Support` | A Training level band (quest 1 has none)          |
| 9039                         | 1 to 35            | `[Daily] [Gathering] Researching ...`                                      | Quests 1 to 30 `getLevel()>99`; 31 to 35 a Gathering level band |
| 9044, 9045                   | 1 to 6, 1 to 12    | `[Daily] [Cooking]` and `[Alchemy] Striving Towards Imperial Delivery`     | A Cooking or Alchemy level band and a `checkRandom` roll   |
| 9047, 9048                   | 1 to 6             | `[Weekly Contribution]` quests                                             | A contribution point band, `getAquredExplorepoint()`       |
| 9058                         | 1 to 42            | `[Select One]` weekly quests, 7 kinds (subjugation, gathering, training, farming, barter, sailing, hunting) | A contribution point band, 6 bands per kind |
| 3737, 3738, 3739             | 1 to 4             | `[Crossroad] [Difficulty 0]` to `[Difficulty 3] Otterly-concerned Vellonia Merchants` | Nothing that tells them apart (`getLevel()>1`)  |
| 3907                         | 2 to 11            | `[Daily] Kakuo Paw-doodles!`                                               | Class 10 or not, and a `checkRandom(n,5)` roll; quest 1 is outside the range |
| 8741                         | 1 to 20            | `Big Bad Auntie's Foreign Cuisine Study`                                   | A `checkRandom(n,4)` roll, one knowledge entry not learned yet and the entries of the quests before |
| 8746                         | 1 to 3             | Three `[Daily]` quests with different titles                               | A `checkRandom(n,3)` roll                                  |
| 9022                         | 1 to 9             | `[Crossroad] Adonna's Fortune Telling - First Card` to `Ninth Card`        | The card's knowledge entry not yet learned                 |
| 9026                         | 1 to 11            | `Agris:` quests, one per hunting ground                                    | The same event condition, word for word, on all 11         |
| 11241                        | 1 to 7             | `[Event] What's in the Cards for Today?`                                   | `getLevel()>99` on all 7                                   |
| 11356                        | 1 to 5             | `[Event] [Weekly] Gather ... Samples`                                      | The same event condition, word for word, on all 5          |
| 11422                        | 2 to 3             | `[Crossroad] [Event] Choose Zobadi`, `Choose Afuaru`                       | Quest 11422 / 1 cleared; quest 1 is outside the range      |
| 40027, 40048, 40061, 40064   | 1 to 5             | `[Awakening Weapon EXC]` PRI (I) to PEN (V)                                | The item at that enhancement level, `getitemcount(item,16..20)` |
| 41005 to 41011               | 1 to 5, 1 to 7, 1 to 13 | `Old Moon's Resplendent` armor and weapons, one per boss item         | The item (41011: an item group) owned or equipped at enhancement level 19 or 20 |
| 41013                        | 1 to 13            | `[Weekly] Imperfect Beings`                                                | Quest 1 open; 2 to 13 `getLevel()>99`                      |
| 41017 to 41022               | 1 to 2, 1 to 34, 1 to 30 | `[Once per Family] Old Moon's Resplendent ...`, one per item         | The item owned or equipped at enhancement level 19         |

Outside their range: 4549 / 8 to 11 (Grand Prix quests), 3907 / 1, 11422 / 1, 41021 / 35 to 50 and 41022 / 31 to 48. The last two are newer items of the same `[Once per Family]` quests.

## Field Names

The `Multiple_Quest` sheet of a private server's `DataSheets.bexcel` on client 1784 has three columns: `Multiple_QuestGroup` (`quest_chain_id`), `Min` (`min_quest_id`) and `Max` (`max_quest_id`). Its 26 rows are the 26 rows of the client 1784 file, value for value; the file has them in another order. On client 3474, 17 of the 18 shared chains have the same range; chain 41010 grew from 1 to 9 to 1 to 13. The 8 chains only the sheet has (11262, 11275 to 11279, 40030, 40031) are gone from the client 3474 file, which has 23 newer chains. Every quest workbook (`datasheet_questtable_*.xlsm`) of that private server has a `Multiple_Quest` sheet with the same three columns and a `#^E_Merge Index` note column; only the event, journal, season and season2 workbooks fill it. The server executable names the manager `MultipleQuestStaticStatusManager` and the loader step `loadMultipleQuestInformation`. The 2016 PDB has no `MultipleQuest` symbol.

## Notes

- Decompressed size on client 3474: `266` bytes, 41 rows, `8 + 41 × 6 + 12`. Client 1784 has the same layout: `176` bytes, 26 rows.
- Rows are not in key order, on client 1784 and on client 3474.
- None of the 3,073 client Lua files (`luacscript/x64/`, client 3474) has `MultipleQuest` or `Multiple_Quest` in it, and no `quest.dbss` script calls a function with `multi` in its name.

## Open Questions

### What a Range Does

The rows group versions of one quest, but nothing in the client data says what the game does with a group. Chains 4549 and 9053 hold the same `No Worries for the Prepared` quest and block each other with `!clearQuest` and `!progressQuest` for every quest of the other chain, while no quest names a quest of its own range; 4576 and 9054 do the same. That points to the range making its versions exclusive (one accepted or cleared version blocks the rest, or the daily and weekly reset counts the range as one quest), but the server may also use the range for something the client never sees, such as picking which version an NPC offers. The `[Select One]` title of chain 9058 fits exclusivity across its 7 kinds.

## In-Game Checks

### Chain 9058 Versions as Exclusive

Needs zone: the city where Liana (NPC 59717) stands

This checks whether accepting one quest of a range hides the other quests of that range. bdocodex lists Liana as the start NPC of 9058/1 `[Weekly Subjugation] Subjugation Request for the Villagers` and 9058/7 `[Weekly Gathering] About the Mysterious Fairy's Breath`.

1. Talk to Liana and open her quest list.
2. Note every `[Select One]` quest she offers.
3. Accept one of them.
4. Open her quest list again and note which `[Select One]` quests are left.

Expected result: the other `[Select One]` quests are gone after step 3. Then a range makes its versions exclusive and What a Range Does is answered. If they are still offered, the range does something else.
