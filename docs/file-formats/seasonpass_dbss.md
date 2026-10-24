# `seasonpass.dbss` Format

## Purpose

The rows of the Black Spirit Pass (season pass) window: per row its number,
the free and the premium (Black Spirit Pass) quest, a season type, and a
replacement title and text that the window shows while a condition quest
is not done. Since client 2519 the rows are followed by the quest chain
range of each pass season. `panel_window_blackspiritpass_1.luac` reads a
row by its number through `ToClient_GetSeasonPassQuestAt(listIdx,
__eSeasonPassQuest_Normal)` and `__eSeasonPassQuest_SeasonPass`, and the
replacement texts through `ToClient_CanShowChangedSeasonPass(listIdx)`,
`ToClient_GetSeasonPassChangedTitle(listIdx)` and
`ToClient_GetSeasonPassChangedDesc(listIdx)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records                 | Row bytes                |
| ------ | -------------- | ------- | ----------------- | ----- | ----------------------- | ------------------------ |
| 3      | 2319 and later | 3483    | `seasonpass.dbss` | 7,737 | 205 Row, 5 Season Range | 37 to 149, 38 on average |
| 2      | 1329 to 2313   | 2313    | `seasonpass.dbss` | 2,262 | 58 Row                  | 37 to 149, 39 on average |
| 1      | 1360 to 1622   | 1622    | `seasonpass.dbss` | 693   | 53 Row                  | 13                       |

| Layout | File              | Known           | Unknown       |
| ------ | ----------------- | --------------- | ------------- |
| 3      | `seasonpass.dbss` | 6,905 B (89.2%) | 832 B (10.8%) |
| 2      | `seasonpass.dbss` | 2,030 B (89.7%) | 232 B (10.3%) |
| 1      | `seasonpass.dbss` | 693 B (100.0%)  | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 3 |
| 3482   | Layout 3 |
| 3474   | Layout 3 |
| 3473   | Layout 3 |
| 3464   | Layout 3 |
| 3458   | Layout 3 |
| 3454   | Layout 3 |
| 3444   | Layout 3 |
| 3435   | Layout 3 |
| 3426   | Layout 3 |
| 3418   | Layout 3 |
| 3412   | Layout 3 |
| 3402   | Layout 3 |
| 3396   | Layout 3 |
| 3387   | Layout 3 |
| 3381   | Layout 3 |
| 3373   | Layout 3 |
| 3364   | Layout 3 |
| 3356   | Layout 3 |
| 3349   | Layout 3 |
| 3342   | Layout 3 |
| 3335   | Layout 3 |
| 3326   | Layout 3 |
| 3321   | Layout 3 |
| 3314   | Layout 3 |
| 3303   | Layout 3 |
| 3302   | Layout 3 |
| 3293   | Layout 3 |
| 3283   | Layout 3 |
| 3275   | Layout 3 |
| 3267   | Layout 3 |
| 3258   | Layout 3 |
| 3251   | Layout 3 |
| 3242   | Layout 3 |
| 3235   | Layout 3 |
| 3229   | Layout 3 |
| 3212   | Layout 3 |
| 3203   | Layout 3 |
| 3193   | Layout 3 |
| 3186   | Layout 3 |
| 3177   | Layout 3 |
| 3169   | Layout 3 |
| 3158   | Layout 3 |
| 3151   | Layout 3 |
| 3144   | Layout 3 |
| 3133   | Layout 3 |
| 3125   | Layout 3 |
| 3118   | Layout 3 |
| 3111   | Layout 3 |
| 3103   | Layout 3 |
| 3095   | Layout 3 |
| 3086   | Layout 3 |
| 3072   | Layout 3 |
| 3062   | Layout 3 |
| 3052   | Layout 3 |
| 3045   | Layout 3 |
| 3037   | Layout 3 |
| 3030   | Layout 3 |
| 3021   | Layout 3 |
| 3012   | Layout 3 |
| 3002   | Layout 3 |
| 2995   | Layout 3 |
| 2987   | Layout 3 |
| 2978   | Layout 3 |
| 2970   | Layout 3 |
| 2959   | Layout 3 |
| 2951   | Layout 3 |
| 2942   | Layout 3 |
| 2935   | Layout 3 |
| 2932   | Layout 3 |
| 2923   | Layout 3 |
| 2919   | Layout 3 |
| 2907   | Layout 3 |
| 2900   | Layout 3 |
| 2891   | Layout 3 |
| 2882   | Layout 3 |
| 2872   | Layout 3 |
| 2863   | Layout 3 |
| 2855   | Layout 3 |
| 2849   | Layout 3 |
| 2844   | Layout 3 |
| 2834   | Layout 3 |
| 2825   | Layout 3 |
| 2819   | Layout 3 |
| 2811   | Layout 3 |
| 2803   | Layout 3 |
| 2794   | Layout 3 |
| 2783   | Layout 3 |
| 2774   | Layout 3 |
| 2765   | Layout 3 |
| 2756   | Layout 3 |
| 2750   | Layout 3 |
| 2743   | Layout 3 |
| 2736   | Layout 3 |
| 2726   | Layout 3 |
| 2717   | Layout 3 |
| 2709   | Layout 3 |
| 2703   | Layout 3 |
| 2695   | Layout 3 |
| 2684   | Layout 3 |
| 2672   | Layout 3 |
| 2665   | Layout 3 |
| 2657   | Layout 3 |
| 2649   | Layout 3 |
| 2644   | Layout 3 |
| 2637   | Layout 3 |
| 2629   | Layout 3 |
| 2619   | Layout 3 |
| 2612   | Layout 3 |
| 2606   | Layout 3 |
| 2602   | Layout 3 |
| 2601   | Layout 3 |
| 2592   | Layout 3 |
| 2583   | Layout 3 |
| 2575   | Layout 3 |
| 2567   | Layout 3 |
| 2560   | Layout 3 |
| 2553   | Layout 3 |
| 2545   | Layout 3 |
| 2538   | Layout 3 |
| 2529   | Layout 3 |
| 2519   | Layout 3 |
| 2513   | Layout 3 |
| 2510   | Layout 3 |
| 2507   | Layout 3 |
| 2503   | Layout 3 |
| 2498   | Layout 3 |
| 2492   | Layout 3 |
| 2487   | Layout 3 |
| 2480   | Layout 3 |
| 2474   | Layout 3 |
| 2468   | Layout 3 |
| 2460   | Layout 3 |
| 2453   | Layout 3 |
| 2444   | Layout 3 |
| 2438   | Layout 3 |
| 2434   | Layout 3 |
| 2429   | Layout 3 |
| 2421   | Layout 3 |
| 2414   | Layout 3 |
| 2407   | Layout 3 |
| 2401   | Layout 3 |
| 2397   | Layout 3 |
| 2393   | Layout 3 |
| 2384   | Layout 3 |
| 2378   | Layout 3 |
| 2372   | Layout 3 |
| 2358   | Layout 3 |
| 2352   | Layout 3 |
| 2347   | Layout 3 |
| 2343   | Layout 3 |
| 2335   | Layout 3 |
| 2327   | Layout 3 |
| 2324   | Layout 3 |
| 2319   | Layout 3 |
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
| 1622   | Layout 1 |
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
| 1466   | Layout 2 |
| 1462   | Layout 2 |
| 1459   | Layout 2 |
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
| 1396   | Layout 2 |
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

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Quest titles (LOC type 18)  |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset             | Type                             | Field              | Notes                                                    |
| ------------------ | -------------------------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`            | u32                              | count              | Number of rows                                           |
| `+0x04`            | Row[count]                       | rows               | See Row                                                  |
| `rows+0x00`        | u16                              | unknown_rows_00    | Equals `season_range_count` on every client checked; see Open Questions |
| `rows+0x02`        | u32                              | season_range_count | Number of `season_ranges`                                |
| `rows+0x06`        | Season Range[season_range_count] | season_ranges      | See Season Range                                         |

### Row (variable: 37 bytes + changed texts)

| Offset                  | Type  | Field                      | Notes                                                                                 |
| ----------------------- | ----- | -------------------------- | ------------------------------------------------------------------------------------- |
| `+0x00`                 | u32   | pass_no                    | Row key, the window's `listIdx`; `0` to `count - 1`                                    |
| `+0x04`                 | u32   | base_reward_quest          | Free quest, a packed quest ID (low u16 chain, high u16 quest); `__eSeasonPassQuest_Normal` |
| `+0x08`                 | u32   | premium_reward_quest       | Black Spirit Pass quest, same chain as `base_reward_quest`; `__eSeasonPassQuest_SeasonPass` |
| `+0x0C`                 | u8    | season_type                | `1` on every row (clients 1784 and 3482)                                               |
| `+0x0D`                 | str16 | changed_title_kr           | Korean title the window shows while `condition_quest` is open; empty on most rows     |
| `changed_title_kr+0x00` | str16 | changed_desc_kr            | Korean text shown with it                                                              |
| `changed_desc_kr+0x00`  | u32   | condition_quest            | Packed quest ID; `0` for none                                                          |
| `changed_desc_kr+0x04`  | u32   | unknown_changed_desc_kr_04 | `0` on every row (clients 1784 and 3482)                                               |

### Season Range (6 bytes)

| Offset  | Type | Field             | Notes                                               |
| ------- | ---- | ----------------- | --------------------------------------------------- |
| `+0x00` | u16  | unknown_00        | `1` to `season_range_count`, descending in the file  |
| `+0x02` | u16  | first_quest_chain | First quest chain of the range                       |
| `+0x04` | u16  | last_quest_chain  | Last quest chain of the range                        |

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                           |
| ------- | ---------- | ----- | ------------------------------- |
| `+0x00` | u32        | count | Number of rows                  |
| `+0x04` | Row[count] | rows  | The rows end at the end of file |

## Layout 1

### Row (13 bytes)

| Offset  | Type | Field                | Notes                                         |
| ------- | ---- | -------------------- | --------------------------------------------- |
| `+0x00` | u32  | pass_no              |                                               |
| `+0x04` | u32  | base_reward_quest    |                                               |
| `+0x08` | u32  | premium_reward_quest |                                               |
| `+0x0C` | u8   | season_type          | No changed texts and no condition quest after it |

## Season Ranges

Client 3482; every row's quest chain falls in one range.

| `unknown_00` | Chains         | Rows |
| ------------ | -------------- | ---- |
| 1            | 50000 to 50057 | 58   |
| 2            | 50100 to 50146 | 47   |
| 3            | 50150          | 37   |
| 4            | 50151          | 37   |
| 5            | 50152          | 26   |

Client 2107 (Layout 2) has the 58 rows of range 1; client 2519 adds range
2 and its rows and ranges 1 and 2 after them, client 3251 has four ranges.

## Field Names

The `Seasonpass_UI` sheet of a private server's `DataSheets.bexcel` on
client 1784 matches the file of that client on all 50 of 50 rows and every
column:

| Field                | Column                                                        |
| -------------------- | ------------------------------------------------------------- |
| pass_no              | `No`                                                          |
| base_reward_quest    | `Sp_BaseReward_QuestGroup`, `Sp_BaseReward_QuestID`           |
| premium_reward_quest | `Sp_PremiumReward_QuestGroup`, `Sp_PremiumReward_QuestID`     |
| season_type          | `Season_Type`                                                 |
| condition_quest      | `Condition` (`40022,1`, group and quest)                      |
| changed_title_kr     | `Changed_Tilte`                                               |
| changed_desc_kr      | `Changed_CompletedText`                                       |

The Lua names (`ChangedTitle`, `ChangedDesc`, `Normal` and `SeasonPass`
quest types) come from `panel_window_blackspiritpass_1.luac` of client
3482. The range fields are newer than client 1784 and have no column.

## Notes

- On client 3482 the free quests of the 205 rows are the quest set of
  `seasonpassquestlistfornormal.bss` and the premium quests the set of
  `seasonpassquestlistforcash.bss` ([`seasonpassquestlist.bss`](seasonpassquestlist_bss.md)).
  Each row pairs quest `n` (free) and `n + 1` (premium) of one chain.
- Client 1485 (Layout 1) has 50 rows of 13 bytes, without the changed
  texts and the condition quest; clients 1636 to 2313 (Layout 2) add them,
  and client 2519 (Layout 3) the season ranges. Client 1348 ships an empty
  file (a count of `0`).
- One row of client 3482 (`pass_no` 6, chain 50006) has a changed title
  (스스로 성장하는 즐거움) and condition quest `40022/1`; client 1784 has two
  such rows with the same condition.
- The handler (`_dbss/seasonpass/`) shows one row per pass row with the
  chain, quest and LOC title of its three quests.

## Open Questions

### What the Season Range Number and the u16 Before It Are

`unknown_00` counts the ranges from `1`, the oldest chains first, and the
u16 before the count equals the count on clients 2519 to 3482. A pass
season number and the current season fit, but no Lua getter reads either
value and client 1784's sheets have no column for them.
