# `npcpersonality.dbss` Format

## Purpose

Defines NPC personality entries used to parameterise AI behaviour. Each record maps a personality ID to three knowledge group references (each with a need count beside it) and four floating-point amity threshold parameters. Used to drive the in-game amity mini-game.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes  | Records             | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ------ | ------------------- | --------- |
| 1      | 1346 and later | 3483    | `npcpersonality.dbss`       | 40,192 | 1,182 Record        | 34        |
| 1      | 1346 and later | 3483    | `npcpersonalityoffset.dbss` | 11,824 | 1,182 Offset Record | 10        |

| Layout | File                        | Known             | Unknown         |
| ------ | --------------------------- | ----------------- | --------------- |
| 1      | `npcpersonality.dbss`       | 40,192 B (100.0%) | 0 B (0.0%)      |
| 1      | `npcpersonalityoffset.dbss` | 9,460 B (80.0%)   | 2,364 B (20.0%) |

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
| 3133   | Layout 1             |
| 3125   | Layout 1             |
| 3118   | Layout 1             |
| 3111   | Layout 1             |
| 3103   | Layout 1             |
| 3095   | Layout 1             |
| 3086   | Layout 1             |
| 3072   | Layout 1             |
| 3062   | Layout 1             |
| 3052   | Layout 1             |
| 3045   | Layout 1             |
| 3037   | Layout 1             |
| 3030   | Layout 1             |
| 3021   | Layout 1             |
| 3012   | Layout 1             |
| 3002   | Layout 1             |
| 2995   | Layout 1             |
| 2987   | Layout 1             |
| 2978   | Layout 1             |
| 2970   | Layout 1             |
| 2959   | Layout 1             |
| 2951   | Layout 1             |
| 2942   | Layout 1             |
| 2935   | Layout 1             |
| 2932   | Layout 1             |
| 2923   | Layout 1             |
| 2919   | Layout 1             |
| 2907   | Layout 1             |
| 2900   | Layout 1             |
| 2891   | Layout 1             |
| 2882   | Layout 1             |
| 2872   | Layout 1             |
| 2863   | Layout 1             |
| 2855   | Layout 1             |
| 2849   | Layout 1             |
| 2844   | Layout 1             |
| 2834   | Layout 1             |
| 2825   | Layout 1             |
| 2819   | Layout 1             |
| 2811   | Layout 1             |
| 2803   | Layout 1             |
| 2794   | Layout 1             |
| 2783   | Layout 1             |
| 2774   | Layout 1             |
| 2765   | Layout 1             |
| 2756   | Layout 1             |
| 2750   | Layout 1             |
| 2743   | Layout 1             |
| 2736   | Layout 1             |
| 2726   | Layout 1             |
| 2717   | Layout 1             |
| 2709   | Layout 1             |
| 2703   | Layout 1             |
| 2695   | Layout 1             |
| 2684   | Layout 1             |
| 2672   | Layout 1             |
| 2665   | Layout 1             |
| 2657   | Layout 1             |
| 2649   | Layout 1             |
| 2644   | Layout 1             |
| 2637   | Layout 1             |
| 2629   | Layout 1             |
| 2619   | Layout 1             |
| 2612   | Layout 1             |
| 2606   | Layout 1             |
| 2602   | Layout 1             |
| 2601   | Layout 1             |
| 2592   | Layout 1             |
| 2583   | Layout 1             |
| 2575   | Layout 1             |
| 2567   | Layout 1             |
| 2560   | Layout 1             |
| 2553   | Layout 1             |
| 2545   | Layout 1             |
| 2538   | Layout 1             |
| 2529   | Layout 1             |
| 2519   | Layout 1             |
| 2513   | Layout 1             |
| 2510   | Layout 1             |
| 2507   | Layout 1             |
| 2503   | Layout 1             |
| 2498   | Layout 1             |
| 2492   | Layout 1             |
| 2487   | Layout 1             |
| 2480   | Layout 1             |
| 2474   | Layout 1             |
| 2468   | Layout 1             |
| 2460   | Layout 1             |
| 2453   | Layout 1             |
| 2444   | Layout 1             |
| 2438   | Layout 1             |
| 2434   | Layout 1             |
| 2429   | Layout 1             |
| 2421   | Layout 1             |
| 2414   | Layout 1             |
| 2407   | Layout 1             |
| 2401   | Layout 1             |
| 2397   | Layout 1             |
| 2393   | Layout 1             |
| 2384   | Layout 1             |
| 2378   | Layout 1             |
| 2372   | Layout 1             |
| 2358   | Layout 1             |
| 2352   | Layout 1             |
| 2347   | Layout 1             |
| 2343   | Layout 1             |
| 2335   | Layout 1             |
| 2327   | Layout 1             |
| 2324   | Layout 1             |
| 2319   | Layout 1             |
| 2313   | Layout 1             |
| 2308   | Layout 1             |
| 2302   | Layout 1             |
| 2295   | Layout 1             |
| 2290   | Layout 1             |
| 2284   | Layout 1             |
| 2276   | Layout 1             |
| 2269   | Layout 1             |
| 2259   | Layout 1             |
| 2250   | Layout 1             |
| 2243   | Layout 1             |
| 2235   | Layout 1             |
| 2229   | Layout 1             |
| 2224   | Layout 1             |
| 2218   | Layout 1             |
| 2215   | Layout 1             |
| 2207   | Layout 1             |
| 2203   | Layout 1             |
| 2196   | Layout 1             |
| 2192   | Layout 1             |
| 2189   | Layout 1             |
| 2183   | Layout 1             |
| 2179   | Layout 1             |
| 2171   | Layout 1             |
| 2163   | Layout 1             |
| 2156   | Layout 1             |
| 2151   | Layout 1             |
| 2147   | Layout 1             |
| 2142   | Layout 1             |
| 2138   | Layout 1             |
| 2134   | Layout 1             |
| 2130   | Layout 1             |
| 2122   | Layout 1             |
| 2107   | Layout 1             |
| 2098   | Layout 1             |
| 2089   | Layout 1             |
| 2081   | Layout 1             |
| 2073   | Layout 1             |
| 2067   | Layout 1             |
| 2063   | Layout 1             |
| 2059   | Layout 1             |
| 2052   | Layout 1             |
| 2044   | Layout 1             |
| 2039   | Layout 1             |
| 2032   | Layout 1             |
| 2025   | Layout 1             |
| 2011   | Layout 1             |
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
| 1680   | Layout 1             |
| 1674   | Layout 1             |
| 1668   | Layout 1             |
| 1659   | Layout 1             |
| 1649   | Layout 1             |
| 1642   | Layout 1             |
| 1636   | Layout 1             |
| 1628   | Layout 1             |
| 1622   | Layout 1             |
| 1614   | Layout 1             |
| 1608   | Layout 1             |
| 1602   | Layout 1             |
| 1598   | Layout 1             |
| 1594   | Layout 1             |
| 1590   | Layout 1             |
| 1587   | Layout 1             |
| 1584   | Layout 1             |
| 1579   | Layout 1             |
| 1572   | Layout 1             |
| 1565   | Layout 1             |
| 1559   | Layout 1             |
| 1554   | Layout 1             |
| 1547   | Layout 1             |
| 1537   | Layout 1             |
| 1529   | Layout 1             |
| 1524   | Layout 1             |
| 1519   | Layout 1             |
| 1509   | Layout 1             |
| 1506   | Layout 1             |
| 1504   | Layout 1             |
| 1500   | Layout 1             |
| 1493   | Layout 1             |
| 1489   | Layout 1             |
| 1485   | Layout 1             |
| 1481   | Layout 1             |
| 1474   | Layout 1             |
| 1466   | Layout 1             |
| 1462   | Layout 1             |
| 1459   | Layout 1             |
| 1453   | Layout 1             |
| 1450   | Layout 1             |
| 1445   | Layout 1             |
| 1439   | Layout 1             |
| 1433   | Layout 1             |
| 1430   | Layout 1             |
| 1426   | Layout 1             |
| 1421   | Layout 1             |
| 1417   | Layout 1             |
| 1416   | Layout 1             |
| 1409   | Layout 1             |
| 1405   | Layout 1             |
| 1401   | Layout 1             |
| 1396   | Layout 1             |
| 1391   | Layout 1             |
| 1390   | Layout 1             |
| 1386   | Layout 1             |
| 1381   | Layout 1             |
| 1379   | Layout 1             |
| 1372   | Layout 1             |
| 1366   | Layout 1             |
| 1364   | Layout 1             |
| 1363   | Layout 1             |
| 1360   | Layout 1             |
| 1358   | Layout 1             |
| 1355   | Layout 1             |
| 1351   | Layout 1             |
| 1348   | Layout 1             |
| 1346   | Layout 1             |
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

| File                        | Required | Role                                    |
| --------------------------- | -------- | --------------------------------------- |
| `npcpersonalityoffset.dbss` | Required | ID-keyed index (same count, own order)  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                          |
| ------- | ------------- | ------- | ---------------------------------------------- |
| `+0x00` | u32           | count   | Number of personality records (observed: 1,182 in the pre-2026-09-27 fixture and in the 2026-09-27 client) |
| `+0x04` | Record[count] | records | See Record                                     |

### Record (34 bytes)

| Offset  | Type | Field              | Notes                                                         |
| ------- | ---- | ------------------ | ------------------------------------------------------------- |
| `+0x00` | u16  | personality_id     | Unique personality identifier (the NPC's character key)       |
| `+0x02` | u16  | group_a_id         | First amity interest group (knowledge group ID)               |
| `+0x04` | u16  | group_a_need_count | Need count for group A; see below                             |
| `+0x06` | u16  | group_b_id         | Second amity interest group                                   |
| `+0x08` | u16  | group_b_need_count | Need count for group B                                        |
| `+0x0A` | u16  | group_c_id         | Third amity interest group                                    |
| `+0x0C` | u16  | group_c_need_count | Need count for group C                                        |
| `+0x0E` | u16  | personality_id_dup | The row's own key member; always equal to `personality_id` at `+0x00` |
| `+0x10` | f32  | interest_min       | Inclusive lower bound for amity interest (range: 11–37)       |
| `+0x14` | f32  | interest_max       | Upper bound for amity interest (range: 23–70); inclusive or exclusive is open |
| `+0x18` | f32  | favor_min          | Inclusive lower bound for amity favor (range: 10–35)          |
| `+0x1C` | f32  | favor_max          | Upper bound for amity favor (range: 14–68; 15–70 in the 2026-09-27 client); inclusive or exclusive is open |
| `+0x20` | u16  | personality_type   | Personality category code (see enum below)                    |

#### Interest Groups

Each group is a u16 knowledge group ID (matches `node_id` in `mentalcard.dbss`) followed by its u16 need count (`group_a_need_count`, `group_b_need_count`, `group_c_need_count`; source names under Field Names). Earlier versions of this doc read each pair as one packed u32 and called the high half `item_count`.

The same numbers appear on the BDO wiki next to each NPC's interest groups, but the game does not show them: the conversation window lists only the topics you can use, with no per-group count or maximum (I checked in game, 2026-09-27). It is not the number of topics offered either: with Oliviero (`6` for Serendia Adventure Log II) the topic list showed 7 cards of that group. What the current game does with the need count is open. On client 3474 the values are 0, 1, 2, 4, 5, 6, 7, 8 and 10, and all three fields of a record share one value in 1,121 of 1,182 records.

### `npcpersonalityoffset.dbss`

An index file with one entry per personality record.

| Offset  | Type                 | Field   | Notes                                  |
| ------- | -------------------- | ------- | -------------------------------------- |
| `+0x00` | u32                  | count   | Must equal `npcpersonality.dbss` count |
| `+0x04` | Offset Record[count] | records | See Offset Record                      |

### Offset Record (10 bytes)

| Offset  | Type | Field          | Notes                                                                          |
| ------- | ---- | -------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u16  | personality_id | Matches `personality_id` in the main record                                    |
| `+0x02` | u32  | data_offset    | Byte offset into main file; 2 bytes past record start (skips `personality_id`) |
| `+0x06` | u16  | data_size      | Always 32 (= record size minus the 2-byte personality_id header)               |
| `+0x08` | u16  | unknown_08     | Not parsed                                                                     |

`record_start = data_offset - 2`

Every offset row points at a record that repeats its `personality_id`, and every record is indexed exactly once, but the rows are not in main-file order: only the first 53 step by the 34-byte stride, the rest are ordered differently (pre-2026-09-27 fixture and 2026-09-27 client alike). An earlier version of this doc called it a sequential index in main-file order.

## Enum Values

### personality_type Codes

24 distinct values in the range 101–1202, following the pattern `(major × 100) + variant` where variant is 1 or 2:

| Major | Variant 1 | Variant 2 | Horoscope     |
| ----- | --------- | --------- | ------------- |
| 1     | 101       | -         | Hammer        |
| 2     | 201       | 202       | Boat          |
| 3     | 301       | 302       | Shield        |
| 4     | 401       | 402       | Giant         |
| 5     | 501       | 502       | Camel         |
| 6     | 601       | 602       | Black Dragon  |
| 7     | 701       | 702       | Treant Owl    |
| 8     | 801       | 802       | Elephant      |
| 9     | 901       | -         | Key           |
| 10    | 1001      | 1002      | Wagon         |
| 11    | 1101      | 1102      | Sealing Stone |
| 12    | 1201      | 1202      | Goblin        |

[`zodiacsignorder.dbss`](zodiacsignorder_dbss.md) stores the sign of every `personality_type` as `zodiac_id`, and it equals the major in all 24 records (client 3464). The names are LOC type 7 sign names from [`zodiacsign.dbss`](zodiacsign_dbss.md). Majors 1 and 9 have only variant 1 here.

## Field Names

The 2016 client's debug symbols (`BlackDesert64.pdb`) list the members of
`gc::NpcPersonalityStaticStatus` in this order: `pa::Array<gc::FavoritedTheme,3> _themeList`
(each `gc::FavoritedTheme` is `KeyType<unsigned short> _key`, `unsigned short _needCount`
and a `gc::MentalThemeStaticStatus*`), `KeyType<unsigned short> _key`, `float _minDv`,
`float _maxDv`, `float _minPv`, `float _maxPv` and
`KeyType<unsigned short> _zodiacSignOrderKey`.

The server dump of a private server on client 1784 (`Instance_dumpFull.exe`) fills those
members twice. `NpcPersonalityStaticStatusManager::readFromBinarybyDynamic` (VA
`0x140b98880`) hands each `npcpersonality.dbss` row, past the leading key, to a row reader
(VA `0x140b96530`) that writes the 32 bytes in file order to the 2016 member offsets. The
`Personality_Table` sheet loader reads one column per member (VA `0x140956897` to
`0x1409569fa`) and stores the `Npc` ID column as `_key` (VA `0x140b95fca`):

| Field                | File    | Member (2016)                | Member  | Sheet column         |
| -------------------- | ------- | ---------------------------- | ------- | -------------------- |
| `group_a_id`         | `+0x02` | `_themeList[0]._key`         | `+0x00` | `Theme1`             |
| `group_a_need_count` | `+0x04` | `_themeList[0]._needCount`   | `+0x02` | `NeedCount1`         |
| `group_b_id`         | `+0x06` | `_themeList[1]._key`         | `+0x10` | `Theme2`             |
| `group_b_need_count` | `+0x08` | `_themeList[1]._needCount`   | `+0x12` | `NeedCount2`         |
| `group_c_id`         | `+0x0A` | `_themeList[2]._key`         | `+0x20` | `Theme3`             |
| `group_c_need_count` | `+0x0C` | `_themeList[2]._needCount`   | `+0x22` | `NeedCount3`         |
| `personality_id_dup` | `+0x0E` | `_key`                       | `+0x30` | `Npc`                |
| `interest_min`       | `+0x10` | `_minDv`                     | `+0x34` | `MinDv`              |
| `interest_max`       | `+0x14` | `_maxDv`                     | `+0x38` | `MaxDv`              |
| `favor_min`          | `+0x18` | `_minPv`                     | `+0x3C` | `MinPv`              |
| `favor_max`          | `+0x1C` | `_maxPv`                     | `+0x40` | `MaxPv`              |
| `personality_type`   | `+0x20` | `_zodiacSignOrderKey`        | `+0x44` | `ZodiacSignIndexKey` |

The values agree. The `Personality_Table` sheet in that server's `datasheet_memorycarddatatable.xlsm`
matches its own compiled `npcpersonality.dbss` on every column above in all 1,122 rows. On
the official client 1784 file all 1,055 records are in the sheet, and the group, need count
and `ZodiacSignIndexKey` columns match every one of them; the ten records whose three need
counts differ pin `NeedCount1` to `+0x04`, `NeedCount2` to `+0x08` and `NeedCount3` to
`+0x0C`. The four floats match the sheet exactly on only 230 to 310 of the 1,055, but each lies
within 3 of its column on 838 to 962 of them, a mean distance of 1.4 to 2.1 against 7.2 or
more to each of the other three float columns. The sheet's `NPC등급` and `NPC_Importance`
columns have no field in the file.

`personality_type` keeps its name; the sheet calls it `ZodiacSignIndexKey` and the 2016
member `_zodiacSignOrderKey`, the key of [`zodiacsignorder.dbss`](zodiacsignorder_dbss.md).
`interest_*` and `favor_*` keep theirs too, from the in-game readings under Notes. The server
code of a private server on client 519 reads `Personality_Table` the other way round:
`CardGame` rolls `npcInterest` between `MinPv` and `MaxPv` and `npcSympathy` between
`MinDv` and `MaxDv`. Ornella's in-game Interest of 22 to 23 fits `+0x10`, which holds
`MinDv`, so these names follow the client.

The same server code (`PersonalityT`, `MentalCardHandler.newGame`) reads `NeedCount1` as the
number of `Theme1` knowledge the player must hold to start the conversation game, and as the
number of card slots in that game. That is its own reconstruction of the older game, not
client data. The source sheet puts a reference column `#테마안에 있는 지식 개수` ("number of
knowledge in the theme") before each `NeedCount`; in its first row the three themes hold 14,
13 and 17 knowledge against a need count of 7 each.

## Notes

- All 1182 `personality_id` values are unique; it is a true record key.
- `personality_id_dup` at `+0x0E` is always identical to `personality_id` at `+0x00`: the leading u16 is the dbss row key, and `+0x0E` is the static status's own `_key` member (see Field Names).
- The `variant` in `personality_type` (1 or 2) picks one of the two star orders in `zodiacsignorder.dbss`; any other in-game meaning is unknown. Distribution is roughly even (584 variant-1, 598 variant-2).
- The groups and `unknown_*` numbers match the BDO wiki for Amerigo (41013): Vendors of Serendia, Serendia Adventure Log II and Plants (Serendia), `4` each.
- The NPC rolls its Interest Level and Favor at the start of each conversation, and keeps them when the conversation is continued ([Black Desert Foundry, Story Exchange guide](https://www.blackdesertfoundry.com/story-exchange-guide/)). Readings do not always fall inside the stored ranges, though: see the table below.
- They match the wiki for Oliviero (41091) too: Serendia Adventure Log II, Officers of Serendia and Plants (Serendia), `6` each. Each group holds more cards than its `unknown_*` number (18, 13 and 11 here). Sharing a group does not mean sharing topics: Amerigo, who also has Serendia Adventure Log II, did not offer the Log II cards Oliviero did. Which cards an NPC offers is open.
- The stored ranges change between client versions while the group IDs stay, and the ranges seen outside the file fit neither client consistently. Interest / favor, stored minimum to maximum:

  | NPC | Seen | Source of the seen range | Pre-2026-09-27 fixture | Client 3458 (2026-09-27) |
  | --- | --- | --- | --- | --- |
  | Lorenzo Murray (40015) | 32 / 15 | Foundry guide | 31-35 / 16-20 | 30-35 / 17-18 |
  | Ornella (41002) | 22-23 / 27-28 | In game | 22-23 / 25-28 | 22-23 / 26-29 |
  | Amerigo (41013) | 20-24 / 27-29 | Amity tracker dataset | 20-25 / 27-30 | 22-24 / 26-30 |
  | Amerigo (41013) | 22 / 28 | Topic tooltips, 2026-09-27 | 20-25 / 27-30 | 22-24 / 26-30 |
  | Cleia (41056) | 20-23 / 25-29 | Amity tracker dataset | 22-23 / 26-28 | 22-25 / 25-28 |
  | Cleia (41056) | 21 / 26 | Topic tooltips, 2026-09-27 | 22-23 / 26-28 | 22-25 / 25-28 |
  | Oliviero (41091) | 30 / 31 | Topic tooltips, 2026-09-27 | 32-35 / 32-33 | 31-33 / 32-33 |
  | George Fusto (41118) | 22-25 / 26-30 | Amity tracker dataset | 20-23 / 25-29 | 20-24 / 27-29 |

  Ornella and the 2026-09-27 Amerigo reading fit, but Oliviero's and Cleia's current readings sit one or two below the current minimums, and Lorenzo's favor 15 is below both files. The tracker dataset comes from a wiki and may predate both files. An earlier version of this table listed a "Stored" column that matched neither fixture; it was replaced with values read from both files (2026-09-28).

## Open Questions

### What does the need count control in the current game?

The 2016 member is `_needCount` and the sheet column `NeedCount1` to `3` (see Field Names), and the BDO wiki lists the same numbers next to each interest group. The game shows no per-group count, though, and Oliviero's topic list held 7 cards of a group whose need count is `6`. It may be a knowledge count the player needs for the group, cap how many of the group's topics the NPC accepts, or be unused since the conversation game changed. `0` occurs as well.

### Why do the official floats differ from the sheet?

The private server on client 1784 compiled its `npcpersonality.dbss` with every float equal to its `Personality_Table` sheet, but the official client 1784 file matches that sheet exactly on only 230 to 310 of 1,055 records per float, while groups, need counts and `ZodiacSignIndexKey` match on all of them. Whether the official build rolls the ranges when it compiles the sheet, or the private server edited three quarters of the float cells, is open. A roll at compile time would also explain why the stored ranges move between client versions while the groups stay (see Notes).

### Are the upper bounds inclusive?

An earlier version of this doc called `interest_max` and `favor_max` exclusive (usable maximum one less than stored) without recorded evidence. Ornella's in-game favor reached `28`, her stored maximum in the pre-2026-09-27 fixture (`29` in client 3458), which argues against that, but other readings fall below the stored minimums (see Notes), so the stored range may not bound what the game rolls. How the displayed range is derived from the stored one is open; the check for Ornella's current maximum is under In-Game Checks.

## In-Game Checks

### Ornella's Favor Maximum

Needs NPC: [Ornella](https://bdocodex.com/us/npc/41002/)

Ornella's stored favor range is `26` to `29` in client 3458. The NPC rolls Favor at the start of each conversation (see Notes), so start about 20 new conversations with her and write down each Favor. A `29` means `favor_max` is inclusive; `26` to `28` only, with `28` seen, means the usable maximum is one less than stored. Readings below `26` mean the stored range does not bound the roll, as for Oliviero and Cleia.
