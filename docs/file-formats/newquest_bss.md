# `newquest.bss` Format

## Purpose

Defines the new-quest (event) list: quest IDs grouped under events such as `[Event] Mastering Life Skills`, each group with an event period, and per quest a condition line, a visible condition and a hide condition. 232 groups and 1,281 quest references on client 3458. All text sits in a string table at the end of the file (Korean group names, Korean condition lines, scripts, dates); LOC type 58 holds the English names and condition lines.

[`mainquest.bss`](mainquest_bss.md), [`recommendationquest.bss`](recommendationquest_bss.md) and [`repetitionquest.bss`](repetitionquest_bss.md) share this layout, each with its own LOC type; one handler reads all four. This doc is the layout reference for all four.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File           | Bytes   | Records                              | Row bytes |
| ------ | -------------- | ------- | -------------- | ------- | ------------------------------------ | --------- |
| 1      | 1304 and later | 3483    | `newquest.bss` | 790,158 | 1,237 Quest Reference Row, 229 Group | 17        |

| Layout | File           | Known             | Unknown      |
| ------ | -------------- | ----------------- | ------------ |
| 1      | `newquest.bss` | 789,242 B (99.9%) | 916 B (0.1%) |

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
| 1341   | Layout 1             |
| 1340   | Layout 1             |
| 1338   | Layout 1             |
| 1335   | Layout 1             |
| 1333   | Layout 1             |
| 1329   | Layout 1             |
| 1327   | Layout 1             |
| 1324   | Layout 1             |
| 1321   | Layout 1             |
| 1319   | Layout 1             |
| 1318   | Layout 1             |
| 1316   | Layout 1             |
| 1313   | Layout 1             |
| 1311   | Layout 1             |
| 1309   | Layout 1             |
| 1304   | Layout 1             |
| 1292   | No documented layout |
| 1286   | No documented layout |
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
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

None. LOC type 58 holds the English group names and condition lines (see Localization).

All multi-byte values are little-endian.

## Layout 1

### File Layout

A header, the groups back to back, the PABR string table and the file trailer.

| Offset              | Type                | Field        | Notes                                                    |
| ------------------- | ------------------- | ------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]             | magic        | `PABR` (ASCII)                                           |
| `+0x04`             | u32                 | group_count  | Number of quest groups; `232` on client 3458             |
| `+0x08`             | Group[group_count]  | groups       | See Group                                                |
| `groups+0x00`       | String Table        | string_table | See String Table                                         |
| `string_table+0x00` | u32                 | table_start  | File offset of the string table's `string_count` (`0x69F1` here) |
| `string_table+0x04` | u32                 | zero         | Observed `0`                                             |

### Group (variable: 23 bytes + quest rows)

An 11-byte group header, `quest_ref_count` quest rows and a 12-byte group trailer.

| Offset      | Type                        | Field             | Notes                                                                   |
| ----------- | --------------------------- | ----------------- | ----------------------------------------------------------------------- |
| `+0x00`     | u16                         | group_key         | The group's key, see Localization; unique per group                     |
| `+0x02`     | u32                         | name_index        | String table index of the Korean group name (`group_name_kr`); `0` for the first group |
| `+0x06`     | u8                          | group_type        | `0` on most groups; the server's `NewQuestType`, see Field Names and Open Questions |
| `+0x07`     | u32                         | quest_ref_count   | Number of following rows                                                |
| `+0x0B`     | Quest Reference Row[quest_ref_count] | rows | See Quest Reference Row                                                      |
| `rows+0x00` | u32                         | event_start_index | String table index of the event start (`event_start`), e.g. `2019-10-16 04:00`; the empty string in the other three lists |
| `rows+0x04` | u32                         | event_end_index   | String table index of the event end (`event_end`), e.g. `2019-11-13 05:59`; always after the start |
| `rows+0x08` | u32                         | unknown_tail_08   | Observed `0` in every group of the four files                          |

The start of group 1 `[Event] Black Desert 2019 Halloween` is `2019-10-16 04:00`, and its English condition lines read `Oct 16 (after maintenance) - ...`.

The times are stored without zero padding (`2018-10-3 10:00`, `2019-7-24 9:00`). The parser pads month, day and hour (`2018-10-03 10:00`) so they sort as text, and keeps text in any other form as stored. All 464 times on client 3458 have the `YYYY-M-D H:MM` form.

### Quest Reference Row (17 bytes)

| Offset  | Type | Field          | Notes                                                                   |
| ------- | ---- | -------------- | ----------------------------------------------------------------------- |
| `+0x00` | u16  | quest_chain_id | LOC type 18 `str_id1`; combines with `quest_id` to form quest key       |
| `+0x02` | u16  | quest_id       | LOC type 18 `str_id2`; combines with `quest_chain_id` to form quest key |
| `+0x04` | u32  | condition_index | String table index of the Korean condition line (`condition_kr`), the source of the LOC condition line |
| `+0x08` | u32  | hide_conditions_index | String table index of the hide condition script (`hide_conditions`), often the empty string; see String Table |
| `+0x0C` | u32  | visible_conditions_index | String table index of the visible condition script (`visible_conditions`), often the empty string; see String Table |
| `+0x10` | u8   | is_sub_quest   | `0` on every row here; `1` on 7 `mainquest.bss` rows                    |

Derived packed quest ID:

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

### String Table (variable: 4 bytes + strings)

Follows the last group: a u32 `string_count`, then `string_count` entries, indexed from `0`. It is the counted string table other PABR `.bss` files end with (`exploration.bss`, `npcsimply.bss`, `menu.bss`), read by `_common/pabr_strings.py`.

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of entries                         |
| `+0x04` | pstr[string_count] | strings      | `is_wide` is `1` on every entry here: UTF-16-LE (`0` would be UTF-8); `length` is the text length in bytes, no terminator |


The table holds each distinct string once, in first-use order: the group name, then each row's condition line, hide condition and visible condition, then the trailer's dates. On client 3458 every entry is used (1,840 here). Index `0` is the first group's name, and the empty string sits where it is first used: index `2` here and in `mainquest.bss` and `recommendationquest.bss`, `31` in `repetitionquest.bss`. That is why the condition indexes repeat one value on so many rows.

The condition lines are the Korean source of the LOC lines and carry the same `<PAColor>` tags. The scripts are client condition calls separated by `;`, with `<or>` between alternatives and `!` for negation: `checkperiodbyGmt(0, 2019/9/4-00:00, 2019/9/25-09:00);`, `clearquest(40022,1);`, `progressquest(...)`, `getLevel()>59;`, `isContentsGroupOpen(0,2177);`, `checkClass(...)`, `getLifeLevel(6)>80;`. Across the four files:

- `visible_conditions` must hold for the quest to be listed: event periods, content groups, level and class checks, prerequisite quests (`mainquest.bss` quest 40022 / 2 needs `clearquest(40022,1);`), and `!clearquest` / `!progressquest` of the quest itself.
- `hide_conditions` takes the quest off the list when it holds: the other branches of a crossroad (7500 / 81 lists 7500 / 82), `do not accept Techthon and Quality Iron` (2001 / 138 lists 2001 / 137), and the other quests of a "once a week per Family" set. No level check ever appears in it.

The quest window (`panel_window_quest_all`) lists a quest of these groups only when `checkHideCondition()` is false and `checkVisibleCondition()` is true.

Calls across the four files on client 3458: `hide_conditions` holds `clearquest` 2,846 times and `progressquest` 1,990 times against 336 negated calls, and never `getLevel` or `checkperiodbyGmt`. `visible_conditions` holds `isContentsGroupOpen` 6,833 times, `checkperiodbyGmt` 5,494, `getLevel` 1,410 and a negated `clearquest` / `progressquest` 4,577 times.

Neither condition holds every check its LOC line names: of 496 `repetitionquest.bss` lines that start `from Lv. N`, 75 have the level check in a script. The rest is likely checked by the quest itself.

## Localization

LOC type `58` holds the English text of this list, keyed by the group's
`group_key`:

| Key                                              | Text                                         |
| ------------------------------------------------ | -------------------------------------------- |
| `str_id1 = group_key`, `str_id4 = 0`             | Group name, e.g. key 1 `[Event] Mastering Life Skills` |
| `str_id1 = packed_quest_id`, `str_id2 = group_key`, `str_id4 = 1` | The quest's condition line, e.g. `From <PAColor0xfff3d900>Lara <PAOldColor>during the event, once per Family` |

On client 3458 all 232 groups have a name (type 58 has 265, so some
belong to groups no longer in the file) and all 1,281 rows have a
condition line. A quest in two groups has a line under each key: quest
11060 / 1 sits in the groups with keys 2 (`[Event] Black Desert 2019
Halloween`) and 62 (`[Event] Black Desert 2020 Halloween`). Condition lines carry `<PAColor>`
tags; group names do not. The Korean names and condition lines in the
string table are the source of both, and the handler shows them where LOC has no row.

## Reference Rows

Client 3458:

| Group | Row | Group Key | Quest Chain ID | Quest ID | condition_index | hide_conditions_index | visible_conditions_index | Example LOC Title |
| ----: | --: | --------: | -------------: | -------: | --------------: | -------------: | -------------: | ----------------- |
| 0     | 0   | `1`       | `11059`        | `9`      | `1`        | `2`        | `2`        | `[Event] Love for Pets` |
| 0     | 1   | `1`       | `11059`        | `10`     | `1`        | `2`        | `2`        | `[Event] Savory Good Feed` |

## Notes

- Decompressed size is `820,905` bytes on client 3458 (`816,761` with 224 groups and 1,255 rows before 2026-09-27).
- 27 quests sit in two groups (29 before 2026-09-27); each copy has its own condition line in LOC.
- The string table indexes shift whenever a string is added earlier in the file, so `condition_index` / `hide_conditions_index` / `visible_conditions_index` are not stable across patches: quest `77129` had `condition_index = 899` before 2026-09-27 and `896` after.
- Earlier versions of this doc and the handler read a 10-byte first group header and a 23-byte later one: the previous group's trailer followed by the next group's header. The rows were the same. They called the row flag `flags`, called `condition_index` / `hide_conditions_index` / `visible_conditions_index` `sequence_a` / `sequence_b` / `sequence_c` and later `unknown_05` / `unknown_09` / `unknown_0d`, and named the header fields `header_flag`, `unknown_a` to `unknown_d`, `group_key_a` and `group_key_b`.
- Until 2026-10-15 the conditions were `script_1` (hide) and `script_2` (visible), shown as Ruled Out When* and Offered When* with the role marked as a guess, and `group_type` and `is_sub_quest` were `unknown_06` and `unknown_10`.
- Until client 3464 this doc and the handler read a u16 `quest_ref_count` plus a padding byte, a row that opened with a u8 `unknown_00`, and a trailer that opened with a zero byte. Group sizes were the same, but each row took the flag byte of the row before it. `mainquest.bss` decides it: the 7 rows with the flag set are 6603 / 2 to 8, the whole run that shares the `hide_conditions` `getknowledge(6392);<or>clearquest(21601,1);<or>!clearquest(351,1);`. The old reading flagged 6603 / 3 to 8 and 6002 / 13, which has another `hide_conditions`. The [calpheonlabs](https://github.com/marceloclp/calpheonlabs) `newquest.bss` page reads the layout the same way.

## Field Names

The 2016 client has no struct or loader for these lists. The server-side tables of a private server on client 519 name every field: `<List>Quest_Table` (`<List>QuestGroupKey`, `QuestGroup`, `QuestID`, `AcceptConditionText`, `HideConditions`, `VisibleConditions`, `IsSubQuest`) and `Group_<List>Quest` (`<List>QuestGroupKey`, `<List>QuestType`, `<List>QuestGroupName`, `Desc`, and `StartDate` and `EndDate` for the event list), where `<List>` is `New`, `Main`, `Recommendation` or `Repetition`. Rows join on the group key and quest ID with client 3464:

| Field | Column | `newquest` | `mainquest` | `recommendationquest` | `repetitionquest` |
| ----- | ------ | ---------: | ----------: | --------------------: | ----------------: |
| shared rows | | 385 | 536 | 272 | 295 |
| condition_kr | `AcceptConditionText` | 160 | 171 | 156 | 55 |
| hide_conditions | `HideConditions` | 65 of 65 | 137 of 267 | 9 of 11 | 17 of 17 |
| visible_conditions | `VisibleConditions` | 144 of 175 | 131 of 131 | 4 of 211 | none set |
| is_sub_quest | `IsSubQuest` | none set | 7 of 7 | none set | none set |
| shared groups | | 43 | 12 | 24 | 20 |
| group_type | `<List>QuestType` | 3 of 3 | none set | 17 of 19 | none set |
| group_name_kr | `<List>QuestGroupName` | 43 | 8 | 4 | 0 |
| event_start, event_end | `StartDate`, `EndDate` | 38, 37 | - | - | - |

Counts with "of" are the rows where the server column is not empty or `0`. The low counts are text the client changed since: the server's `VisibleConditions` on 207 `recommendationquest` rows still checks levels the client dropped (`getLifeLevel(0)>9;getlevel()>19;` on 2100 / 115 to 118, where the client stores none), its `HideConditions` on 130 `mainquest` rows are longer versions of the client's (`clearquest(21401,1);<or>isContentsGroupOpen(0,110);!clearquest(4001,1);...` where 4001 / 1 to 4 store `!clearquest(4001,1);`), and Korean condition lines and group names were reworded.

The client Lua confirms the two condition roles: the quest window (`panel_window_quest_all`) lists a quest when `checkHideCondition()` is false and `checkVisibleCondition()` is true. `group_type` and `is_sub_quest` rest on the server columns alone; the Lua never calls a getter for either on these lists.

## Open Questions

### What Does `group_type` Select?

`0` on 227 of 232 groups here, and `1`, `2`, `6` or `8` on the rest (`[Hunting] Sniping, ...` 2, `Krogdalo's Three Seeds` 1, `[Season] Stronger Tuvala Gear` 8). In `recommendationquest.bss` it runs `0` to `8` and groups by theme ([Life] [Leap] gurus at 4 to 7, mounts and outfits at 2), so it may be a category or tab. The server calls it `NewQuestType`, but no Lua getter reads it, so which UI uses it is not confirmed.

### Duplicate Quest References

A quest in two groups has a condition line under both group keys, so a quest can be listed by two events (11060 / 1 in the 2019 and 2020 Halloween groups). Whether the game shows both copies at once is not confirmed.

### What Does `unknown_tail_08` Index?

`0` in every group of the four lists (clients 1784 and 3474). No sheet
column of `Group_MainQuest` or `Group_NewQuest` fills it. The client 1784
server dump has a u32 that its group loader sets to `0` as the last member
of the group struct (`+0x98`), and the only code that reads that member is
the language-data writer (VA `0x140c1faf0`): it passes the value with the
list's LOC type (28, 42, 43 or 58) to a lookup that skips `0` and otherwise
reads an 8-byte entry at `value * 8` of a `Head_LanguageData_` file. The
server has no reader for these files, so tying the file's trailer to that
member rests on position only, and nothing names it.
