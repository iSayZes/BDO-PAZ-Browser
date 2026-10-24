# `elementalmonsterreward.bss` Format

## Purpose

The ranking rewards of the Black Shrine (검은 사당) bosses in the Land of the
Morning Light: per boss character, the items of each rank tier ("#1",
"#2 ~ #5") and the items of the "Bonus Rewards" row for players outside the
ranks. The detailed reward window
(`panel_window_morningland_detailreward_all.luac`) reads it per boss through
`ToClient_getElementalMonsterRankReward*` and
`ToClient_getElementalMonsterBaseReward*`, with a flag that picks the
second table for the Hwanghae (Party) ranking.

On client 3474 the first table has a record for each of the 108 bosses of
[`elementalmonsterstat.bss`](elementalmonsterstat_bss.md): the 94 Donghae
(Solo) bosses with the tiers `1`, `5` and `20` and two base items, the 14
Hwanghae (Party) bosses with two base items and no tiers. The second table
has the 14 Hwanghae (Party) bosses with their party tiers and no base items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes  | Records                                    | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ------ | ------------------------------------------ | --------- |
| 3      | 3473 and later | 3483    | `elementalmonsterreward.bss` | 18,240 | 797 Reward Item, 319 Rank Tier, 118 Record | 16        |
| 2      | 2619 to 3464   | 3464    | `elementalmonsterreward.bss` | 4,782  | 453 Reward Item, 331 Rank Tier, 122 Record | 6         |
| 1      | 2224 to 2612   | 2612    | `elementalmonsterreward.bss` | 4,204  | 400 Reward Item, 300 Rank Tier, 100 Record | 6         |

| Layout | File                         | Known             | Unknown    |
| ------ | ---------------------------- | ----------------- | ---------- |
| 3      | `elementalmonsterreward.bss` | 18,240 B (100.0%) | 0 B (0.0%) |
| 2      | `elementalmonsterreward.bss` | 4,782 B (100.0%)  | 0 B (0.0%) |
| 1      | `elementalmonsterreward.bss` | 4,204 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 3 |
| 3482   | Layout 3 |
| 3474   | Layout 3 |
| 3473   | Layout 3 |
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
| 2717   | Layout 2 |
| 2709   | Layout 2 |
| 2703   | Layout 2 |
| 2695   | Layout 2 |
| 2684   | Layout 2 |
| 2672   | Layout 2 |
| 2665   | Layout 2 |
| 2657   | Layout 2 |
| 2649   | Layout 2 |
| 2644   | Layout 2 |
| 2637   | Layout 2 |
| 2629   | Layout 2 |
| 2619   | Layout 2 |
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

| File                       | Required | Role                                                        |
| -------------------------- | -------- | ----------------------------------------------------------- |
| `elementalmonsterstat.bss` | Optional | The part and difficulty of each boss, by `character_key`    |
| `languagedata_*.loc`       | Optional | Boss and item names, and the rank labels of the window      |

All multi-byte values are little-endian.

## Layout 3

### File Layout

Plain binary: no `PABR` magic, no offset file and no trailer.

| Offset         | Type                 | Field         | Notes                                                     |
| -------------- | -------------------- | ------------- | --------------------------------------------------------- |
| `+0x00`        | u32                  | count         | Number of `records`                                       |
| `+0x04`        | Record[count]        | records       | The rewards the window reads with the Part 2 flag off     |
| `records+0x00` | u32                  | part2_count   | Number of `part2_records`                                 |
| `records+0x04` | Record[part2_count]  | part2_records | The rewards the window reads with the Part 2 flag on      |

### Record (variable: 14 bytes + rank tiers and base rewards)

| Offset            | Type                            | Field             | Notes                                                                 |
| ----------------- | ------------------------------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00`           | u16                             | character_key     | The boss, the `character_key` of `elementalmonsterstat.bss`           |
| `+0x02`           | u32                             | rank_tier_count   | Number of `rank_tiers`; `ToClient_getElementalMonsterRankRewardListCount` |
| `+0x06`           | Rank Tier[rank_tier_count]      | rank_tiers        | See Rank Tier                                                         |
| `rank_tiers+0x00` | u64                             | base_reward_count | Number of `base_rewards`; `ToClient_getElementalMonsterBaseRewardSize` |
| `rank_tiers+0x08` | Reward Item[base_reward_count]  | base_rewards      | The "Bonus Rewards" row, for players outside the ranks                |

### Rank Tier (variable: 12 bytes + rewards)

| Offset  | Type                       | Field        | Notes                                                                 |
| ------- | -------------------------- | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32                        | rank         | Lowest rank of the tier; `ToClient_getElementalMonsterRankByIndex`    |
| `+0x04` | u64                        | reward_count | Number of `rewards`; `ToClient_getElementalMonsterRankRewardSizeByIndex` |
| `+0x0c` | Reward Item[reward_count]  | rewards      | See Reward Item                                                       |

### Reward Item (16 bytes)

Same structure as the Reward Item of
[`elementalmonsterstat.bss`](elementalmonsterstat_bss.md#reward-item-16-bytes).

| Offset  | Type     | Field      | Notes                                                                     |
| ------- | -------- | ---------- | ------------------------------------------------------------------------- |
| `+0x00` | u32      | item_key   | Item key, `enchant_level << 24 \| item_id`; `...RewardItemKeyByIndex`     |
| `+0x04` | bytes[4] | padding_04 | Alignment of `count`; `fc 7f 00 00` or `f7 7f 00 00` (client 3474), see Notes |
| `+0x08` | i64      | count      | Number of the item; `...RewardItemCountByIndex`, `1` on every entry (client 3474) |

## Layout 2

### Record (variable: 12 bytes + rank tiers)

| Offset            | Type                        | Field           | Notes                                    |
| ----------------- | --------------------------- | --------------- | ---------------------------------------- |
| `+0x00`           | u16                         | character_key   |                                          |
| `+0x02`           | u32                         | rank_tier_count |                                          |
| `+0x06`           | Rank Tier[rank_tier_count]  | rank_tiers      |                                          |
| `rank_tiers+0x00` | Reward Item                 | base_rewards    | Exactly one item, no count before it     |

### Rank Tier (10 bytes)

| Offset  | Type        | Field   | Notes                                |
| ------- | ----------- | ------- | ------------------------------------ |
| `+0x00` | u32         | rank    |                                      |
| `+0x04` | Reward Item | rewards | Exactly one item, no count before it |

### Reward Item (6 bytes)

| Offset  | Type | Field    | Notes                              |
| ------- | ---- | -------- | ---------------------------------- |
| `+0x00` | u32  | item_key |                                    |
| `+0x04` | u16  | count    | `1` on every entry (client 3251)   |

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                       |
| ------- | ------------- | ------- | --------------------------- |
| `+0x00` | u32           | count   | Number of `records`         |
| `+0x04` | Record[count] | records | The only table; see Notes   |

## Rank Tiers

The window labels a tier with the GAME sheet key `LUA_MORNING_ATTRBOSS_RANK`
("#{rank}"). A tier whose `rank` is above 1 reads from one past the
previous tier's `rank` to its own (`#2 ~ #5`, and `#2 ~ #2` for the tiers
`1`, `2`), or `~ #50` when it is the first tier; the base rewards row reads
`LUA_MORNING_ATTRBOSS_OUTOFRANKREWARD` ("Bonus Rewards"). The window shows
the base rewards only for a boss that has rank tiers and only with the Part
2 flag off.

| Table           | Bosses (client 3474) | `rank` of the tiers        | Items per tier | Base rewards |
| --------------- | -------------------- | -------------------------- | -------------- | ------------ |
| `records`       | 94 Donghae (Solo)    | `1`, `5`, `20`             | 2              | 2            |
| `records`       | 14 Hwanghae (Party)  | None                       |                | 2            |
| `part2_records` | 7 Hwanghae (Party)   | `1`, `2`, `3`, `10`, `25`, `50` | 1         | 0            |
| `part2_records` | 7 Hwanghae (Party)   | `50`                       | 1              | 0            |

## Field Names

No reference source has the file. It first appears on client 2519 (absent
on client 2107), so a private server's `DataSheets.bexcel`, `.xlsm` sheets
and server dump on client 1784 have no `Elemental` sheet or column, and the
2016 client and the client 519 server tables predate it.

The names follow the client Lua of client 3474
(`panel_window_morningland_detailreward_all.luac`): per boss character
key and Part 2 flag it reads `ToClient_getElementalMonsterRankRewardListCount`,
then per tier `ToClient_getElementalMonsterRankByIndex`,
`ToClient_getElementalMonsterRankRewardSizeByIndex` and per item
`...RankRewardItemKeyByIndex` and `...RankRewardItemCountByIndex`; for the
base row `ToClient_getElementalMonsterBaseRewardSize`,
`...BaseRewardItemKey` and `...BaseRewardItemCount`. The counts, ranks and
items sit in the file in that order, and the item names match the tiers:
`790001` "C-1 Boss Blitz Reward: Golden Pig King (Rank 1)" is the tier `1`
item of the Calamity 1 Golden Pig King `23608`, `790011` "(Rank 2)" its
tier `5` item.

`part2_count` and `part2_records` are named after the Lua flag
`isMorningLandMonsterPart2`: its 14 keys are the Hwanghae (Party) bosses
(`monster_part` `2` in `elementalmonsterstat.bss`), and their tier items
are "Boss Blitz Reward (Rank 1)" `761108` to "(Rank 6)" `761113`.

## Notes

- The second item of every `records` tier and base row is `890117`
  (Korean name 전투 비급서(소형); no English LOC name on client 3474).
- The base items of the Hwanghae (Party) bosses in `records` are their
  "Boss Slayer's Haul" boxes, the same item as their `show_rewards` in
  `elementalmonsterstat.bss` (`761337` "Boss Slayer's Haul - Jigwi
  (Normal)" for `24562`). The window does not show them, as it skips the
  base row with the Part 2 flag on and the tier list is empty with it off.
- The handler (`_bss/elementalmonsterreward/`) shows one row per rank tier
  and per non-empty base rewards row, labelled as the window labels them,
  with a Party Ranking flag on the `part2_records` rows. It links each boss
  to its `elementalmonsterstat.bss` row and takes the part and difficulty
  from there.
- `padding_04` is the 4 bytes between the u32 `item_key` and the 8-aligned
  i64 `count`, as in `elementalmonsterstat.bss`.
- Layout 2 (clients 3002 and 3251) has one item per tier and one base item,
  with a u16 count; Layout 1 (client 2519) has the same records and no
  second table, as the Hwanghae (Party) bosses came later.
- The Layout 2 `count` is a u16 that holds `1` on every entry; it takes its
  name from the Layout 3 `count` at the same place after `item_key`.
