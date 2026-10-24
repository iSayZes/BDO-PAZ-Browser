# `majorsiegerewardstaticstatus.bss` Format

## Purpose

The Conquest War (major siege) rewards: per row a u8, eleven item lists
(victory, defeat, score places 1st to 6th, liberation, a medal and a
plus item), a u32 and three item IDs; after the rows one booty list of
item IDs per territory. On client 3482 the three rows (`unknown_00`
`5`, `6` and `7`) hold the Tier 1, Tier 2 and Unlimited Conquest War
reward boxes, and the five booty lists the temporary crown and armor of
Balenos to Valencia with [Guild] Reminiscence of Battle.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records                   | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ----- | ------------------------- | --------- |
| 3      | 3473 and later | 3483    | `majorsiegerewardstaticstatus.bss` | 1,409 | 60 Reward, 3 Row, 5 Booty | 16        |
| 2      | 3235 to 3464   | 3464    | `majorsiegerewardstaticstatus.bss` | 581   | 33 Reward, 3 Row, 5 Booty | 12        |
| 1      | 2900 to 3212   | 3212    | `majorsiegerewardstaticstatus.bss` | 533   | 33 Reward, 3 Row, 5 Booty | 12        |

| Layout | File                               | Known           | Unknown       |
| ------ | ---------------------------------- | --------------- | ------------- |
| 3      | `majorsiegerewardstaticstatus.bss` | 1,154 B (81.9%) | 255 B (18.1%) |
| 2      | `majorsiegerewardstaticstatus.bss` | 566 B (97.4%)   | 15 B (2.6%)   |
| 1      | `majorsiegerewardstaticstatus.bss` | 530 B (99.4%)   | 3 B (0.6%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 3             |
| 3482   | Layout 3             |
| 3474   | Layout 3             |
| 3473   | Layout 3             |
| 3464   | Layout 2             |
| 3458   | Layout 2             |
| 3454   | Layout 2             |
| 3444   | Layout 2             |
| 3435   | Layout 2             |
| 3426   | Layout 2             |
| 3418   | Layout 2             |
| 3412   | Layout 2             |
| 3402   | Layout 2             |
| 3396   | Layout 2             |
| 3387   | Layout 2             |
| 3381   | Layout 2             |
| 3373   | Layout 2             |
| 3364   | Layout 2             |
| 3356   | Layout 2             |
| 3349   | Layout 2             |
| 3342   | Layout 2             |
| 3335   | Layout 2             |
| 3326   | Layout 2             |
| 3321   | Layout 2             |
| 3314   | Layout 2             |
| 3303   | Layout 2             |
| 3302   | Layout 2             |
| 3293   | Layout 2             |
| 3283   | Layout 2             |
| 3275   | Layout 2             |
| 3267   | Layout 2             |
| 3258   | Layout 2             |
| 3251   | Layout 2             |
| 3242   | Layout 2             |
| 3235   | Layout 2             |
| 3229   | No documented layout |
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
| 2891   | No file              |
| 2882   | No file              |
| 2872   | No file              |
| 2863   | No file              |
| 2855   | No file              |
| 2849   | No file              |
| 2844   | No file              |
| 2834   | No file              |
| 2825   | No file              |
| 2819   | No file              |
| 2811   | No file              |
| 2803   | No file              |
| 2794   | No file              |
| 2783   | No file              |
| 2774   | No file              |
| 2765   | No file              |
| 2756   | No file              |
| 2750   | No file              |
| 2743   | No file              |
| 2736   | No file              |
| 2726   | No file              |
| 2717   | No file              |
| 2709   | No file              |
| 2703   | No file              |
| 2695   | No file              |
| 2684   | No file              |
| 2672   | No file              |
| 2665   | No file              |
| 2657   | No file              |
| 2649   | No file              |
| 2644   | No file              |
| 2637   | No file              |
| 2629   | No file              |
| 2619   | No file              |
| 2612   | No file              |
| 2606   | No file              |
| 2602   | No file              |
| 2601   | No file              |
| 2592   | No file              |
| 2583   | No file              |
| 2575   | No file              |
| 2567   | No file              |
| 2560   | No file              |
| 2553   | No file              |
| 2545   | No file              |
| 2538   | No file              |
| 2529   | No file              |
| 2519   | No file              |
| 2513   | No file              |
| 2510   | No file              |
| 2507   | No file              |
| 2503   | No file              |
| 2498   | No file              |
| 2492   | No file              |
| 2487   | No file              |
| 2480   | No file              |
| 2474   | No file              |
| 2468   | No file              |
| 2460   | No file              |
| 2453   | No file              |
| 2444   | No file              |
| 2438   | No file              |
| 2434   | No file              |
| 2429   | No file              |
| 2421   | No file              |
| 2414   | No file              |
| 2407   | No file              |
| 2401   | No file              |
| 2397   | No file              |
| 2393   | No file              |
| 2384   | No file              |
| 2378   | No file              |
| 2372   | No file              |
| 2358   | No file              |
| 2352   | No file              |
| 2347   | No file              |
| 2343   | No file              |
| 2335   | No file              |
| 2327   | No file              |
| 2324   | No file              |
| 2319   | No file              |
| 2313   | No file              |
| 2308   | No file              |
| 2302   | No file              |
| 2295   | No file              |
| 2290   | No file              |
| 2284   | No file              |
| 2276   | No file              |
| 2269   | No file              |
| 2259   | No file              |
| 2250   | No file              |
| 2243   | No file              |
| 2235   | No file              |
| 2229   | No file              |
| 2224   | No file              |
| 2218   | No file              |
| 2215   | No file              |
| 2207   | No file              |
| 2203   | No file              |
| 2196   | No file              |
| 2192   | No file              |
| 2189   | No file              |
| 2183   | No file              |
| 2179   | No file              |
| 2171   | No file              |
| 2163   | No file              |
| 2156   | No file              |
| 2151   | No file              |
| 2147   | No file              |
| 2142   | No file              |
| 2138   | No file              |
| 2134   | No file              |
| 2130   | No file              |
| 2122   | No file              |
| 2107   | No file              |
| 2098   | No file              |
| 2089   | No file              |
| 2081   | No file              |
| 2073   | No file              |
| 2067   | No file              |
| 2063   | No file              |
| 2059   | No file              |
| 2052   | No file              |
| 2044   | No file              |
| 2039   | No file              |
| 2032   | No file              |
| 2025   | No file              |
| 2011   | No file              |
| 2005   | No file              |
| 2000   | No file              |
| 1996   | No file              |
| 1991   | No file              |
| 1985   | No file              |
| 1980   | No file              |
| 1969   | No file              |
| 1964   | No file              |
| 1958   | No file              |
| 1950   | No file              |
| 1945   | No file              |
| 1937   | No file              |
| 1933   | No file              |
| 1927   | No file              |
| 1921   | No file              |
| 1914   | No file              |
| 1908   | No file              |
| 1897   | No file              |
| 1892   | No file              |
| 1886   | No file              |
| 1881   | No file              |
| 1871   | No file              |
| 1866   | No file              |
| 1862   | No file              |
| 1854   | No file              |
| 1846   | No file              |
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

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0), territory names (LOC type 12) |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type               | Field        | Notes                                               |
| ------------------- | ------------------ | ------------ | --------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                        |
| `+0x04`             | u32                | row_count    | Number of rows                                      |
| `+0x08`             | Row[row_count]     | rows         | See Row                                             |
| `rows+0x00`         | u32                | booty_count  | Number of booty lists                               |
| `rows+0x04`         | Booty[booty_count] | booty_items  | See Booty                                           |
| `booty_items+0x00`  | String Table       | string_table | See String Table                                    |
| `string_table+0x00` | u32                | table_start  | Offset of the string table, where `booty_items` ends |
| `string_table+0x04` | u32                | zero         | Always `0`                                          |

### Row (variable: 105 bytes + rewards)

| Offset                   | Type                           | Field                        | Notes                                                    |
| ------------------------ | ------------------------------ | ---------------------------- | -------------------------------------------------------- |
| `+0x00`                  | u8                             | unknown_00                   | `5`, `6`, `7` on client 3482; see Open Questions         |
| `+0x01`                  | u64                            | win_reward_count             | Number of `win_rewards`                                  |
| `+0x09`                  | Reward[win_reward_count]       | win_rewards                  | Victory: Glorious Victor Reward and a Combat Secret Book |
| `win_rewards+0x00`       | u64                            | lose_reward_count            | Number of `lose_rewards`                                 |
| `win_rewards+0x08`       | Reward[lose_reward_count]      | lose_rewards                 | Defeat: Fighting Spirit Reward and a Combat Secret Book  |
| `lose_rewards+0x00`      | u64                            | release_win_reward_count     | Number of `release_win_rewards`                          |
| `lose_rewards+0x08`      | Reward[release_win_reward_count] | release_win_rewards        | Score 1st: Burning Spirit Victor Reward                  |
| `release_win_rewards+0x00` | u64                          | release_reward_count_0       | Number of `release_rewards_0`                            |
| `release_win_rewards+0x08` | Reward[release_reward_count_0] | release_rewards_0          | Score 2nd: Burning Spirit Reward (V)                     |
| `release_rewards_0+0x00` | u64                            | release_reward_count_1       | Number of `release_rewards_1`                            |
| `release_rewards_0+0x08` | Reward[release_reward_count_1] | release_rewards_1            | Score 3rd: Burning Spirit Reward (IV)                    |
| `release_rewards_1+0x00` | u64                            | release_reward_count_2       | Number of `release_rewards_2`                            |
| `release_rewards_1+0x08` | Reward[release_reward_count_2] | release_rewards_2            | Score 4th: Burning Spirit Reward (III)                   |
| `release_rewards_2+0x00` | u64                            | release_reward_count_3       | Number of `release_rewards_3`                            |
| `release_rewards_2+0x08` | Reward[release_reward_count_3] | release_rewards_3            | Score 5th: Burning Spirit Reward (II)                    |
| `release_rewards_3+0x00` | u64                            | release_reward_count_4       | Number of `release_rewards_4`                            |
| `release_rewards_3+0x08` | Reward[release_reward_count_4] | release_rewards_4            | Score 6th: Burning Spirit Reward (I)                     |
| `release_rewards_4+0x00` | u64                            | release_reward_count         | Number of `release_rewards`                              |
| `release_rewards_4+0x08` | Reward[release_reward_count]   | release_rewards              | Liberation: Burning Inspiration Reward                   |
| `release_rewards+0x00`   | u64                            | plus_medal_reward_count      | Number of `plus_medal_rewards`                           |
| `release_rewards+0x08`   | Reward[plus_medal_reward_count] | plus_medal_rewards          | Medal of Glory x5 on client 3482                         |
| `plus_medal_rewards+0x00` | u64                           | plus_item_reward_count       | Number of `plus_item_rewards`                            |
| `plus_medal_rewards+0x08` | Reward[plus_item_reward_count] | plus_item_rewards           | Battlefield Glory x1 on client 3482                      |
| `plus_item_rewards+0x00` | u32                            | unknown_plus_item_rewards_00 | `200000`, `300000`, `500000` by row on client 3482      |
| `plus_item_rewards+0x04` | u32                            | item_id_1                    | Item ID; `44732` [Guild] Valencia/Edania Elephant Nursery |
| `plus_item_rewards+0x08` | u32                            | item_id_2                    | Item ID; `44733` [Guild] Balenos/Serendia Indomitable Flag Factory |
| `plus_item_rewards+0x0C` | u32                            | item_id_3                    | Item ID; `44734` [Guild] Calpheon/Ulukita Indomitable Flag Factory |

The names are the client 3482 boxes of row `5`; rows `6` and `7` hold
the Tier 2 and Unlimited boxes of the same kinds.

### Reward (16 bytes)

| Offset  | Type     | Field      | Notes                                                             |
| ------- | -------- | ---------- | ----------------------------------------------------------------- |
| `+0x00` | u32      | item_id    | `itemenchant.dbss` item ID; the handler shows its LOC type 0 name |
| `+0x04` | bytes[4] | unknown_04 | `00 00 00 00` in the first three lists, `A4 00 00 00` in the others on client 3482 |
| `+0x08` | u64      | count      | How many of the item                                              |

### Booty (variable: 10 bytes + item IDs)

| Offset  | Type            | Field         | Notes                                                           |
| ------- | --------------- | ------------- | --------------------------------------------------------------- |
| `+0x00` | u16             | territory_key | `territoryinfo.bss` key, LOC type 12 name; `0` to `4` on client 3482 |
| `+0x02` | u64             | item_count    | Number of `item_ids`; `3` on every list of client 3482          |
| `+0x0A` | u32[item_count] | item_ids      | The territory's crown and armor (Temp) and [Guild] Reminiscence of Battle |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 2

### Row (149 bytes)

| Offset  | Type   | Field                        | Notes                     |
| ------- | ------ | ---------------------------- | ------------------------- |
| `+0x00` | u8     | unknown_00                   | `5`, `6`, `7`             |
| `+0x01` | Reward | win_rewards                  | One item, no count before |
| `+0x0D` | Reward | lose_rewards                 |                           |
| `+0x19` | Reward | release_win_rewards          |                           |
| `+0x25` | Reward | release_rewards_0            |                           |
| `+0x31` | Reward | release_rewards_1            |                           |
| `+0x3D` | Reward | release_rewards_2            |                           |
| `+0x49` | Reward | release_rewards_3            |                           |
| `+0x55` | Reward | release_rewards_4            |                           |
| `+0x61` | Reward | release_rewards              |                           |
| `+0x6D` | Reward | plus_medal_rewards           |                           |
| `+0x79` | Reward | plus_item_rewards            |                           |
| `+0x85` | u32    | unknown_plus_item_rewards_00 |                           |
| `+0x89` | u32    | item_id_1                    |                           |
| `+0x8D` | u32    | item_id_2                    |                           |
| `+0x91` | u32    | item_id_3                    |                           |

### Reward (12 bytes)

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | u32  | item_id |       |
| `+0x04` | u64  | count   |       |

## Layout 1

### Row (133 bytes)

| Offset  | Type   | Field               | Notes                     |
| ------- | ------ | ------------------- | ------------------------- |
| `+0x00` | u8     | unknown_00          | `5`, `6`, `7`             |
| `+0x01` | Reward | win_rewards         | One item, no count before |
| `+0x0D` | Reward | lose_rewards        |                           |
| `+0x19` | Reward | release_win_rewards |                           |
| `+0x25` | Reward | release_rewards_0   |                           |
| `+0x31` | Reward | release_rewards_1   |                           |
| `+0x3D` | Reward | release_rewards_2   |                           |
| `+0x49` | Reward | release_rewards_3   |                           |
| `+0x55` | Reward | release_rewards_4   |                           |
| `+0x61` | Reward | release_rewards     |                           |
| `+0x6D` | Reward | plus_medal_rewards  |                           |
| `+0x79` | Reward | plus_item_rewards   |                           |

## Field Names

The lists take the names of the Conquest War columns of the
`SiegeReward` sheet of a private server's `DataSheets.bexcel` on client
1784, where they are single items: `MajorWinMedal_ItemKey`,
`MajorLoseMedal_ItemKey`, `MajorReleaseWinMedal_ItemKey`,
`MajorReleaseMedal_ItemKey_0` to `_4`, `MajorReleaseMedal_ItemKey`,
`MajorPlusMedal_ItemKey` with `PlusMedal_Major` (`5`) and
`PlusItem_Major` (`44391`, Battlefield Glory, the same item as client
3482's `plus_item_rewards`). That sheet's item IDs are older boxes of
the same names (Glorious Victor Reward `45964`, Fighting Spirit Reward
`45971`, Burning Spirit Reward (V) to (I) `45965` to `45969`). The LOC
type 0 text of each client 3482 box confirms the list: "How to Obtain:
Tier 1 Conquest War victory", "defeat", "Score 1st" to "Score 6th" and
"liberation", so `Release` is the liberation and `ReleaseWin` the
first score place. The same columns name the Major Rewards of
[`siegerewarddata.bss`](siegerewarddata_bss.md).

The booty lists match the `BootyItem_0` to `BootyItem_4` columns of the
same sheet's service type `1` (DEV) and `3` (KOR_REAL) rows
(`731901,731906,45113` to `731905,731910,45113`, 5 of 5; the other
service types list the permanent `23381,23386` and so on), and
`territory_key` the suffix: each list holds the Temp copies of the crown
and armor that `territoryinfo.bss` gives the lord of that territory in
`booty_item_ids` (Silver Mane for `0` Balenos, Blue Lion for `1`
Serendia, Golden Eagle for `2` Calpheon, Asula for `3` Mediah, Aal for
`4` Valencia).

## Notes

- Clients 3474 and later use Layout 3 (1,409 bytes on client 3482).
  Client 3251 uses Layout 2: one item per list with no counts (581
  bytes). Client 3002 uses Layout 1, without the u32 and the three item
  IDs (533 bytes), and the Resplendent Medal of Honor (`15692`) as the
  medal. The file is not in the archives of client 2765 or 1784.
- The three item IDs are the same on all three rows of client 3482: the
  Elephant Nursery and the two Indomitable Flag Factories, guild siege
  buildings.
- The handler (`_bss/majorsiegerewardstaticstatus/`) shows one row per
  item: each row's list items with their count and list, then the three
  item IDs, then each booty list's items with the territory name, in
  file order.

## Open Questions

### The Row u8

`unknown_00` is `5`, `6` and `7`, and the rows' boxes say Tier 1, Tier 2
and Unlimited Conquest War in their LOC text. A siege tier enum where
`1` to `4` are the Node War tiers fits, but no Lua of client 3482 names
such an enum.

### The u32 and the Three Item IDs

`unknown_plus_item_rewards_00` grows by row (`200000`, `300000`,
`500000`), which fits a silver or guild fund amount. The three item IDs
are guild siege building items; whether the row gives them, or allows
them in that tier, is open.
