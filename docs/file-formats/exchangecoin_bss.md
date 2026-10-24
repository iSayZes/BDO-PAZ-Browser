# `exchangecoin.bss` Format

## Purpose

The coin exchange: per coin item (seals, tokens and medals) its category,
the coin counts of its accumulated use levels and the rewards it buys, each
with its exchange number, coin cost, item and count, exchange type, limit
and the accumulated level it needs. The exchange window Lua
(`panel_exchangecoin_all_1.luac`) walks the coins with
`ToClient_getCountOfCoinList()` and `ToClient_getCoinItemEnchantKeyByIndex(index)`,
reads the category with `ToClient_getCoinInfoCategoryByIndex(index)` and a
reward with `ToClient_getExchangeNo`, `ToClient_getNeedCoinCount`,
`ToClient_getRewardItemWrapperByType`, `ToClient_getLimitCountByExchangeNo`
and `ToClient_getAccumulatedCoinNeedLevel`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records             | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | ------------------- | --------- |
| 3      | 3412 and later | 3483    | `exchangecoin.bss` | 27,980 | 752 Reward, 54 Coin | 35        |
| 2      | 3111 to 3402   | 3402    | `exchangecoin.bss` | 28,824 | 810 Reward, 58 Coin | 34        |
| 1      | 2480 to 3103   | 3103    | `exchangecoin.bss` | 22,114 | 623 Reward, 44 Coin | 34        |

| Layout | File               | Known            | Unknown         |
| ------ | ------------------ | ---------------- | --------------- |
| 3      | `exchangecoin.bss` | 21,258 B (76.0%) | 6,722 B (24.0%) |
| 2      | `exchangecoin.bss` | 21,586 B (74.9%) | 7,238 B (25.1%) |
| 1      | `exchangecoin.bss` | 16,598 B (75.1%) | 5,516 B (24.9%) |

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

None. The handler names the coin and reward items from the item lookup
indexes and LOC type 0.

All multi-byte values are little-endian.

## Layout 3

### File Layout

No `PABR` magic and no string table.

| Offset           | Type                     | Field              | Notes                                                                    |
| ---------------- | ------------------------ | ------------------ | ------------------------------------------------------------------------ |
| `+0x00`          | u32                      | coin_count         | Number of coins, `54` on client 3482                                     |
| `+0x04`          | Coin[coin_count]         | coins              | See Coin                                                                 |
| `coins+0x00`     | u32                      | unknown_order_count | Equals `coin_count` on client 3482                                      |
| `coins+0x04`     | u32[unknown_order_count] | unknown_order_keys | The `coin_item_key` of every coin, in another order than `coins`; see Open Questions |

### Coin (variable: 26 bytes + levels and rewards)

| Offset                            | Type                                | Field                     | Notes                                                                       |
| --------------------------------- | ----------------------------------- | ------------------------- | --------------------------------------------------------------------------- |
| `+0x00`                           | u8                                  | unknown_00                | `1` on four coins of client 3482 (`860216`, `860333`, `860451`, `890085`), else `0` |
| `+0x01`                           | u32                                 | coin_item_key             | The coin item (`ItemEnchantKey`, level 0 here); unique                      |
| `+0x05`                           | u8                                  | info_category             | See Info Categories                                                         |
| `+0x06`                           | i64                                 | unknown_06                | `-1` on every coin of client 3482                                           |
| `+0x0E`                           | u64                                 | accumulated_level_count   | Number of `accumulated_need_counts`; `4` on Agris Gold Coin (`890085`), `0` on the other 53 coins |
| `+0x16`                           | u64[accumulated_level_count]        | accumulated_need_counts   | Coins to have used for each accumulated level, rising (`200`, `1000`, `1800`, `3500`) |
| `accumulated_need_counts+0x00`    | u32                                 | reward_count              | Number of `rewards`                                                         |
| `accumulated_need_counts+0x04`    | Reward[reward_count]                | rewards                   | See Reward                                                                  |

### Reward (35 bytes)

| Offset  | Type | Field                  | Notes                                                                                      |
| ------- | ---- | ---------------------- | ------------------------------------------------------------------------------------------ |
| `+0x00` | u32  | exchange_no            | Exchange number (`ToClient_getExchangeNo`), unique over the file                           |
| `+0x04` | u64  | need_coin_count        | Coins one exchange costs                                                                   |
| `+0x0C` | u32  | item_key               | Item given (`ItemEnchantKey`)                                                              |
| `+0x10` | u64  | item_count             | Count given per exchange                                                                   |
| `+0x18` | u8   | exchange_type          | See Exchange Types                                                                         |
| `+0x19` | u8   | limit_count            | Exchanges allowed per period of `exchange_type` (`ToClient_getLimitCountByExchangeNo`); `0` on 331 of the 339 `Always` rewards of client 3482 |
| `+0x1A` | i64  | unknown_1a             | `-1` on every reward of client 3482                                                        |
| `+0x22` | u8   | accumulated_need_level | Accumulated level the reward needs, `0` to `accumulated_level_count`; `255` for none, the value of every reward of coins without levels |

On client 3482 the 54 coins hold 752 rewards.

## Layout 2

No accumulated levels: a coin has no `accumulated_level_count` and
`accumulated_need_counts`, a reward no `accumulated_need_level`. Only the
Coin and the Reward differ from Layout 3.

### Coin (variable: 18 bytes + rewards)

| Offset  | Type                 | Field         | Notes |
| ------- | -------------------- | ------------- | ----- |
| `+0x00` | u8                   | unknown_00    |       |
| `+0x01` | u32                  | coin_item_key |       |
| `+0x05` | u8                   | info_category |       |
| `+0x06` | i64                  | unknown_06    |       |
| `+0x0E` | u32                  | reward_count  |       |
| `+0x12` | Reward[reward_count] | rewards       |       |

### Reward (34 bytes)

| Offset  | Type | Field           | Notes |
| ------- | ---- | --------------- | ----- |
| `+0x00` | u32  | exchange_no     |       |
| `+0x04` | u64  | need_coin_count |       |
| `+0x0C` | u32  | item_key        |       |
| `+0x10` | u64  | item_count      |       |
| `+0x18` | u8   | exchange_type   |       |
| `+0x19` | u8   | limit_count     |       |
| `+0x1A` | i64  | unknown_1a      |       |

## Layout 1

No `unknown_00` byte before the coin item key; the rest is as in Layout 2.

### Coin (variable: 17 bytes + rewards)

| Offset  | Type                 | Field         | Notes |
| ------- | -------------------- | ------------- | ----- |
| `+0x00` | u32                  | coin_item_key |       |
| `+0x04` | u8                   | info_category |       |
| `+0x05` | i64                  | unknown_06    |       |
| `+0x0D` | u32                  | reward_count  |       |
| `+0x11` | Reward[reward_count] | rewards       |       |

## Info Categories

`ToClient_getCoinInfoCategoryByIndex()` returns a coin's category, which
the Lua compares with `__eExchangeCoinInfoCategory_Season`, `_Event`,
`_Contents`, `_BossReward` and `_Bookmark`; the Lua does not hold their
values. The coins of each value on client 3482 name it:

| Value | Category   | Coins (client 3482)                                                        |
| ----- | ---------- | -------------------------------------------------------------------------- |
| 0     | Season     | The two `[Season]` items (`[Season] Adventure Token`, `[Season] Seal of Journey`) |
| 1     | Event      | 16 coins, 13 of them named `[Event] ...`                                   |
| 2     | Contents   | 29 coins of standing content (`Hunter's Seal`, `Golden Seal - [Imperial Training]`, `Battlefield Token`) |
| 4     | BossReward | The seven `Boss Blitz Token - ...` items                                   |

No coin has `3`; the bookmark tab is the player's own list.

## Exchange Types

`exchange_type` is the `_exchangeTypeEnum` of the exchange window Lua
(`panel_exchangecoin_all.luac`), which passes it to
`ToClient_getCountOfRewardListByType(coin, type)`.

| Value | Lua name | Rewards (client 3482) |
| ----- | -------- | --------------------- |
| 0     | `ALWAYS` | 339                   |
| 1     | `DAY`    | 6                     |
| 2     | `WEEK`   | 65                    |
| 3     | `FAMILY` | 342                   |
| 4     | `LEVEL`  | 0                     |

The rewards of Agris Gold Coin that need an accumulated level are type `3`.

## Notes

- Client 1784 has no `exchangecoin.bss`, and a private server's
  `DataSheets.bexcel` on client 1784 has no coin exchange sheet, so the
  field names come from the Lua.

## Open Questions

### What the Coin Head Fields Hold

`unknown_00` is `1` on Faded Golden Seal, Dreamer's Seal, Strange
Moonlight Seal and Agris Gold Coin and `0` on the other 50 coins of client
3482; `ToClient_isSealedCoin(coin)` is a lead. `unknown_06` is `-1` on every
coin.

### What the Reward's `-1` Holds

`unknown_1a` is `-1` on all 752 rewards of client 3482. A sale end time or
a per-account limit that is off would read this way.

### What the Coin Key List Orders

`unknown_order_keys` lists the same 54 coins as `coins` in another order
(`860451`, `1000845`, `980170`, ...). The window sorts by its bookmark list
first and has a `LINEUP` tab; which of the two lists
`ToClient_getCoinItemEnchantKeyByIndex()` walks is open.
