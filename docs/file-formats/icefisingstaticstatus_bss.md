# `icefisingstaticstatus.bss` Format

## Purpose

The settings of the ice fishing mini-game, one row per mini-game group:
wait and game times, the fish's HP and the HP a hit and a critical hit
take, block, speed and durability values and the reward drop group. [`icefisingregionstaticstatus.bss`](icefisingregionstaticstatus_bss.md)
gives each ice fishing region its group. The client Lua opens the game
through `Panel_MiniGame_IceFishing_All` behind
`_ContentsGroup_IceFishingGame` and shows the time left as
`LUA_ICEFISHING_TIME` ("Remaining: {time} sec"); it reads none of these
values.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | --------------------- | --------- |
| 2      | 2726 and later | 3483    | `icefisingstaticstatus.bss` | 240   | 2 Row                 | 110       |
| 1      | 1784 to 2717   | 2717    | `icefisingstaticstatus.bss` | 128   | 1 Row, 1 String Table | 108       |

| Layout | File                        | Known          | Unknown    |
| ------ | --------------------------- | -------------- | ---------- |
| 2      | `icefisingstaticstatus.bss` | 240 B (100.0%) | 0 B (0.0%) |
| 1      | `icefisingstaticstatus.bss` | 128 B (100.0%) | 0 B (0.0%) |

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

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of mini-game groups                    |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (110 bytes)

| Offset  | Type | Field                | Notes                                                                    |
| ------- | ---- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | mini_game_group      | Group key; `icefisingregionstaticstatus.bss` `mini_game_group_index`      |
| `+0x02` | u64  | min_wait_time        | Sheet `MinWaitTime`                                                      |
| `+0x0A` | u64  | max_wait_time        | Sheet `MaxWaitTime`                                                      |
| `+0x12` | u64  | game_total_time      | Sheet `GameTotalTime`                                                    |
| `+0x1A` | u64  | game_min_time        | Sheet `GameMinTime`; see Field Names                                     |
| `+0x22` | u64  | game_max_time        | Sheet `GameMaxTime`; see Field Names                                     |
| `+0x2A` | u32  | fish_hp              | Sheet `FishHP`                                                           |
| `+0x2E` | u32  | decrease_hp          | Sheet `DecreaseHP`                                                       |
| `+0x32` | u64  | time_per_tick        | Sheet `TimePerTick`                                                      |
| `+0x3A` | u32  | critical_percent     | Sheet `CriticalPercent`                                                  |
| `+0x3E` | u32  | critical_decrease_hp | Sheet `CriticalDecreaseHP`, a whole number                               |
| `+0x42` | u32  | possible_percent     | Sheet `PossiblePercent`                                                  |
| `+0x46` | u32  | total_block          | Sheet `TotalBlock`                                                       |
| `+0x4A` | u64  | minigame_time        | Sheet `MinigameTime`                                                     |
| `+0x52` | u64  | random_minigame_time | Sheet `RandomMinigameTime`                                               |
| `+0x5A` | u32  | fish_speed           | Sheet `FishSpeed`                                                        |
| `+0x5E` | u32  | random_fish_speed    | Sheet `RandomFishSpeed`                                                  |
| `+0x62` | u32  | player_move_speed    | Sheet `PlayerMoveSpeed`                                                  |
| `+0x66` | u32  | endurance_decrease   | Sheet `EnduranceDecrease`                                                |
| `+0x6A` | u32  | reward_drop_group    | Sheet `RewardDropGroup`                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

`reward_drop_group` is a u16, so the row is 2 bytes shorter. Only the Row
differs from Layout 2.

### Row (108 bytes)

| Offset  | Type | Field                | Notes                                                                    |
| ------- | ---- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | mini_game_group      |                                                                          |
| `+0x02` | u64  | min_wait_time        |                                                                          |
| `+0x0A` | u64  | max_wait_time        |                                                                          |
| `+0x12` | u64  | game_total_time      |                                                                          |
| `+0x1A` | u64  | game_min_time        |                                                                          |
| `+0x22` | u64  | game_max_time        |                                                                          |
| `+0x2A` | u32  | fish_hp              |                                                                          |
| `+0x2E` | u32  | decrease_hp          |                                                                          |
| `+0x32` | u64  | time_per_tick        |                                                                          |
| `+0x3A` | u32  | critical_percent     |                                                                          |
| `+0x3E` | u32  | critical_decrease_hp |                                                                          |
| `+0x42` | u32  | possible_percent     |                                                                          |
| `+0x46` | u32  | total_block          |                                                                          |
| `+0x4A` | u64  | minigame_time        |                                                                          |
| `+0x52` | u64  | random_minigame_time |                                                                          |
| `+0x5A` | u32  | fish_speed           |                                                                          |
| `+0x5E` | u32  | random_fish_speed    |                                                                          |
| `+0x62` | u32  | player_move_speed    |                                                                          |
| `+0x66` | u32  | endurance_decrease   |                                                                          |
| `+0x6A` | u16  | reward_drop_group    | `19840` on client 1784                                                   |

## Groups

The rows on the clients read, against the `IceFishing` sheet row of a
private server on client 1784 (its values are edited, see Field Names):

| Field                  | Sheet (1784) | Client 1784 | Client 3482, groups `2` and `1` |
| ---------------------- | ------------ | ----------- | ------------------------------- |
| `mini_game_group`      | `1`          | `1`         | `2`, `1`                        |
| `min_wait_time`        | `10000`      | `10`        | `10`                            |
| `max_wait_time`        | `20000`      | `20`        | `20`                            |
| `game_total_time`      | `30000`      | `30`        | `30`                            |
| `game_min_time`        | `10000`      | `3`         | `3`                             |
| `game_max_time`        | `20000`      | `100`       | `100`                           |
| `fish_hp`              | `100`        | `100`       | `100`                           |
| `decrease_hp`          | `5`          | `10`        | `10`                            |
| `time_per_tick`        | `500`        | `1`         | `1`                             |
| `critical_percent`     | `30`         | `30`        | `30`                            |
| `critical_decrease_hp` | `7.5`        | `15`        | `15`                            |
| `possible_percent`     | `30`         | `30`        | `30`                            |
| `total_block`          | `20`         | `20`        | `20`                            |
| `minigame_time`        | `3000`       | `3`         | `3`                             |
| `random_minigame_time` | `2000`       | `2`         | `2`                             |
| `fish_speed`           | `4`          | `4`         | `4`                             |
| `random_fish_speed`    | `3`          | `3`         | `3`                             |
| `player_move_speed`    | `1`          | `1`         | `1`                             |
| `endurance_decrease`   | `3`          | `3`         | `3`                             |
| `reward_drop_group`    | `19840`      | `19840`     | `16444` on both rows            |

The two rows of client 3482 differ in `mini_game_group` only.

## Field Names

The names follow the `IceFishing` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_minigame_2.xlsm`: 20 columns from `MiniGameGroup` to
`GameMaxTime`, one row. That server's `binary/icefisingstaticstatus.bss`,
compiled from the sheet, has the 108-byte row of Layout 1 and holds each
sheet value at one offset: `10000` and `20000` at `+0x02` and `+0x0A`
and again at `+0x1A` and `+0x22`, `30000` at `+0x12`, `500` at `+0x32`,
`7` (the sheet's `7.5`, cut to a whole number) at `+0x3E`, `3000` and
`2000` at `+0x4A` and `+0x52`, `19840` at `+0x6A`, the others as in the
table above.

Four pairs of offsets hold equal sheet values (`10000`, `20000`, `30`
and `3`), so the values alone do not place them. The server dump of the
same build places them: its `IceFishing` loader reads `MiniGameGroup`,
`MinWaitTime`, `MaxWaitTime`, `GameTotalTime`, `FishHP`, `DecreaseHP`,
`TimePerTick`, `CriticalPercent`, `CriticalDecreaseHP`,
`PossiblePercent`, `TotalBlock`, `MinigameTime`, `RandomMinigameTime`,
`FishSpeed`, `RandomFishSpeed`, `PlayerMoveSpeed`, `EnduranceDecrease`
and `RewardDropGroup` in this order, which is the file's field order, and
keeps `RewardDropGroup` as a 16-bit value, as Layout 1 stores it. That
places `CriticalPercent` before `PossiblePercent`, `RandomFishSpeed`
before `EnduranceDecrease` and the wait times at `+0x02` and `+0x0A`.
The loader does not read `GameMinTime` or `GameMaxTime`, so those two
take the u64 fields left after `GameTotalTime`, the only other place the
sheet values `10000` and `20000` occupy.

The sheet writes the times in milliseconds (`MinWaitTime` `10000`); the
client files store `10` where the sheet has `10000` and `3` where it has
`3000`.

## Notes

- `icefising` is the client's spelling.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/lifeskill_tables.py`, one
  row per mini-game group.

## Open Questions

### What game_min_time and game_max_time Limit

On client 3482 both rows store `3` and `100` there, next to a
`game_total_time` of `30`. Which time of the game they bound, and in which
unit, is not known; neither the dump's loader nor the client Lua reads
them.
