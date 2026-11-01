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

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File               | Bytes  | Records             | Row bytes |
| ------ | -------------- | ------------------ | ------ | ------------------- | --------- |
| 3      | 3412 and later | `exchangecoin.bss` | 27,980 | 752 Reward, 54 Coin | 35        |
| 2      | 3111 to 3402   | `exchangecoin.bss` | 28,824 | 810 Reward, 58 Coin | 34        |
| 1      | 2480 to 3103   | `exchangecoin.bss` | 22,114 | 623 Reward, 44 Coin | 34        |

| Layout | File               | Known            | Unknown         |
| ------ | ------------------ | ---------------- | --------------- |
| 3      | `exchangecoin.bss` | 21,258 B (76.0%) | 6,722 B (24.0%) |
| 2      | `exchangecoin.bss` | 21,586 B (74.9%) | 7,238 B (25.1%) |
| 1      | `exchangecoin.bss` | 16,598 B (75.1%) | 5,516 B (24.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `ddcdc1739136`  |
| 3482   | Layout 3 | `ddcdc1739136`  |
| 3474   | Layout 3 | `ddcdc1739136`  |
| 3473   | Layout 3 | `ddcdc1739136`  |
| 3464   | Layout 3 | `ddcdc1739136`  |
| 3458   | Layout 3 | `ddcdc1739136`  |
| 3454   | Layout 3 | `ddcdc1739136`  |
| 3444   | Layout 3 | `ddcdc1739136`  |
| 3435   | Layout 3 | `ddcdc1739136`  |
| 3426   | Layout 3 | `ddcdc1739136`  |
| 3418   | Layout 3 | `ddcdc1739136`  |
| 3412   | Layout 3 | `ddcdc1739136`  |
| 3402   | Layout 2 | `ddcdc1739136`  |
| 3396   | Layout 2 | `ddcdc1739136`  |
| 3387   | Layout 2 | `ddcdc1739136`  |
| 3381   | Layout 2 | `ddcdc1739136`  |
| 3373   | Layout 2 | `ddcdc1739136`  |
| 3364   | Layout 2 | `ddcdc1739136`  |
| 3356   | Layout 2 | `ddcdc1739136`  |
| 3349   | Layout 2 | `ddcdc1739136`  |
| 3342   | Layout 2 | `ddcdc1739136`  |
| 3335   | Layout 2 | `ddcdc1739136`  |
| 3326   | Layout 2 | `ddcdc1739136`  |
| 3321   | Layout 2 | `ddcdc1739136`  |
| 3314   | Layout 2 | `ddcdc1739136`  |
| 3303   | Layout 2 | `ddcdc1739136`  |
| 3302   | Layout 2 | `ddcdc1739136`  |
| 3293   | Layout 2 | `ddcdc1739136`  |
| 3283   | Layout 2 | `ddcdc1739136`  |
| 3275   | Layout 2 | `ddcdc1739136`  |
| 3267   | Layout 2 | `ddcdc1739136`  |
| 3258   | Layout 2 | `ddcdc1739136`  |
| 3251   | Layout 2 | `ddcdc1739136`  |
| 3242   | Layout 2 | `ddcdc1739136`  |
| 3235   | Layout 2 | `ddcdc1739136`  |
| 3229   | Layout 2 | `ddcdc1739136`  |
| 3212   | Layout 2 | `ddcdc1739136`  |
| 3203   | Layout 2 | `ddcdc1739136`  |
| 3193   | Layout 2 | `ddcdc1739136`  |
| 3186   | Layout 2 | `ddcdc1739136`  |
| 3177   | Layout 2 | `ddcdc1739136`  |
| 3169   | Layout 2 | `ddcdc1739136`  |
| 3158   | Layout 2 | `ddcdc1739136`  |
| 3151   | Layout 2 | `ddcdc1739136`  |
| 3144   | Layout 2 | `ddcdc1739136`  |
| 3133   | Layout 2 | `ddcdc1739136`  |
| 3125   | Layout 2 | `ddcdc1739136`  |
| 3118   | Layout 2 | `ddcdc1739136`  |
| 3111   | Layout 2 | `ddcdc1739136`  |
| 3103   | Layout 1 | `ddcdc1739136`  |
| 3095   | Layout 1 | `ddcdc1739136`  |
| 3086   | Layout 1 | `ddcdc1739136`  |
| 3072   | Layout 1 | `ddcdc1739136`  |
| 3062   | Layout 1 | `ddcdc1739136`  |
| 3052   | Layout 1 | `ddcdc1739136`  |
| 3045   | Layout 1 | `ddcdc1739136`  |
| 3037   | Layout 1 | `ddcdc1739136`  |
| 3030   | Layout 1 | `ddcdc1739136`  |
| 3021   | Layout 1 | `ddcdc1739136`  |
| 3012   | Layout 1 | `ddcdc1739136`  |
| 3002   | Layout 1 | `ddcdc1739136`  |
| 2995   | Layout 1 | `ddcdc1739136`  |
| 2987   | Layout 1 | `ddcdc1739136`  |
| 2978   | Layout 1 | `ddcdc1739136`  |
| 2970   | Layout 1 | `ddcdc1739136`  |
| 2959   | Layout 1 | `ddcdc1739136`  |
| 2951   | Layout 1 | `ddcdc1739136`  |
| 2942   | Layout 1 | `ddcdc1739136`  |
| 2935   | Layout 1 | `ddcdc1739136`  |
| 2932   | Layout 1 | `ddcdc1739136`  |
| 2923   | Layout 1 | `ddcdc1739136`  |
| 2919   | Layout 1 | `ddcdc1739136`  |
| 2907   | Layout 1 | `ddcdc1739136`  |
| 2900   | Layout 1 | `ddcdc1739136`  |
| 2891   | Layout 1 | `ddcdc1739136`  |
| 2882   | Layout 1 | `ddcdc1739136`  |
| 2872   | Layout 1 | `ddcdc1739136`  |
| 2863   | Layout 1 | `ddcdc1739136`  |
| 2855   | Layout 1 | `ddcdc1739136`  |
| 2849   | Layout 1 | `ddcdc1739136`  |
| 2844   | Layout 1 | `ddcdc1739136`  |
| 2834   | Layout 1 | `ddcdc1739136`  |
| 2825   | Layout 1 | `ddcdc1739136`  |
| 2819   | Layout 1 | `ddcdc1739136`  |
| 2811   | Layout 1 | `ddcdc1739136`  |
| 2803   | Layout 1 | `ddcdc1739136`  |
| 2794   | Layout 1 | `ddcdc1739136`  |
| 2783   | Layout 1 | `ddcdc1739136`  |
| 2774   | Layout 1 | `ddcdc1739136`  |
| 2765   | Layout 1 | `ddcdc1739136`  |
| 2756   | Layout 1 | `ddcdc1739136`  |
| 2750   | Layout 1 | `ddcdc1739136`  |
| 2743   | Layout 1 | `ddcdc1739136`  |
| 2736   | Layout 1 | `ddcdc1739136`  |
| 2726   | Layout 1 | `ddcdc1739136`  |
| 2717   | Layout 1 | `ddcdc1739136`  |
| 2709   | Layout 1 | `ddcdc1739136`  |
| 2703   | Layout 1 | `ddcdc1739136`  |
| 2695   | Layout 1 | `ddcdc1739136`  |
| 2684   | Layout 1 | `ddcdc1739136`  |
| 2672   | Layout 1 | `ddcdc1739136`  |
| 2665   | Layout 1 | `ddcdc1739136`  |
| 2657   | Layout 1 | `ddcdc1739136`  |
| 2649   | Layout 1 | `ddcdc1739136`  |
| 2644   | Layout 1 | `ddcdc1739136`  |
| 2637   | Layout 1 | `ddcdc1739136`  |
| 2629   | Layout 1 | `ddcdc1739136`  |
| 2619   | Layout 1 | `ddcdc1739136`  |
| 2612   | Layout 1 | `ddcdc1739136`  |
| 2606   | Layout 1 | `ddcdc1739136`  |
| 2602   | Layout 1 | `ddcdc1739136`  |
| 2601   | Layout 1 | `ddcdc1739136`  |
| 2592   | Layout 1 | `ddcdc1739136`  |
| 2583   | Layout 1 | `ddcdc1739136`  |
| 2575   | Layout 1 | `ddcdc1739136`  |
| 2567   | Layout 1 | `ddcdc1739136`  |
| 2560   | Layout 1 | `ddcdc1739136`  |
| 2553   | Layout 1 | `ddcdc1739136`  |
| 2545   | Layout 1 | `ddcdc1739136`  |
| 2538   | Layout 1 | `ddcdc1739136`  |
| 2529   | Layout 1 | `ddcdc1739136`  |
| 2519   | Layout 1 | `ddcdc1739136`  |
| 2513   | Layout 1 | `ddcdc1739136`  |
| 2510   | Layout 1 | `ddcdc1739136`  |
| 2507   | Layout 1 | `ddcdc1739136`  |
| 2503   | Layout 1 | `ddcdc1739136`  |
| 2498   | Layout 1 | `ddcdc1739136`  |
| 2492   | Layout 1 | `ddcdc1739136`  |
| 2487   | Layout 1 | `ddcdc1739136`  |
| 2480   | Layout 1 | `ddcdc1739136`  |
| 2474   | No file  | `ddcdc1739136`  |
| 2468   | No file  | `ddcdc1739136`  |
| 2460   | No file  | `ddcdc1739136`  |
| 2453   | No file  | `ddcdc1739136`  |
| 2444   | No file  | `ddcdc1739136`  |
| 2438   | No file  | `ddcdc1739136`  |
| 2434   | No file  | `ddcdc1739136`  |
| 2429   | No file  | `ddcdc1739136`  |
| 2421   | No file  | `ddcdc1739136`  |
| 2414   | No file  | `ddcdc1739136`  |
| 2407   | No file  | `ddcdc1739136`  |
| 2401   | No file  | `ddcdc1739136`  |
| 2397   | No file  | `ddcdc1739136`  |
| 2393   | No file  | `ddcdc1739136`  |
| 2384   | No file  | `ddcdc1739136`  |
| 2378   | No file  | `ddcdc1739136`  |
| 2372   | No file  | `ddcdc1739136`  |
| 2358   | No file  | `ddcdc1739136`  |
| 2352   | No file  | `ddcdc1739136`  |
| 2347   | No file  | `ddcdc1739136`  |
| 2343   | No file  | `ddcdc1739136`  |
| 2335   | No file  | `ddcdc1739136`  |
| 2327   | No file  | `ddcdc1739136`  |
| 2324   | No file  | `ddcdc1739136`  |
| 2319   | No file  | `ddcdc1739136`  |
| 2313   | No file  | `ddcdc1739136`  |
| 2308   | No file  | `ddcdc1739136`  |
| 2302   | No file  | `ddcdc1739136`  |
| 2295   | No file  | `ddcdc1739136`  |
| 2290   | No file  | `ddcdc1739136`  |
| 2284   | No file  | `ddcdc1739136`  |
| 2276   | No file  | `ddcdc1739136`  |
| 2269   | No file  | `ddcdc1739136`  |
| 2259   | No file  | `ddcdc1739136`  |
| 2250   | No file  | `ddcdc1739136`  |
| 2243   | No file  | `ddcdc1739136`  |
| 2235   | No file  | `ddcdc1739136`  |
| 2229   | No file  | `ddcdc1739136`  |
| 2224   | No file  | `ddcdc1739136`  |
| 2218   | No file  | `ddcdc1739136`  |
| 2215   | No file  | `ddcdc1739136`  |
| 2207   | No file  | `ddcdc1739136`  |
| 2203   | No file  | `ddcdc1739136`  |
| 2196   | No file  | `ddcdc1739136`  |
| 2192   | No file  | `ddcdc1739136`  |
| 2189   | No file  | `ddcdc1739136`  |
| 2183   | No file  | `ddcdc1739136`  |
| 2179   | No file  | `ddcdc1739136`  |
| 2171   | No file  | `ddcdc1739136`  |
| 2163   | No file  | `ddcdc1739136`  |
| 2156   | No file  | `ddcdc1739136`  |
| 2151   | No file  | `ddcdc1739136`  |
| 2147   | No file  | `ddcdc1739136`  |
| 2142   | No file  | `ddcdc1739136`  |
| 2138   | No file  | `ddcdc1739136`  |
| 2134   | No file  | `ddcdc1739136`  |
| 2130   | No file  | `ddcdc1739136`  |
| 2122   | No file  | `ddcdc1739136`  |
| 2107   | No file  | `ddcdc1739136`  |
| 2098   | No file  | `ddcdc1739136`  |
| 2089   | No file  | `ddcdc1739136`  |
| 2081   | No file  | `ddcdc1739136`  |
| 2073   | No file  | `ddcdc1739136`  |
| 2067   | No file  | `ddcdc1739136`  |
| 2063   | No file  | `ddcdc1739136`  |
| 2059   | No file  | `ddcdc1739136`  |
| 2052   | No file  | `ddcdc1739136`  |
| 2044   | No file  | `ddcdc1739136`  |
| 2039   | No file  | `ddcdc1739136`  |
| 2032   | No file  | `ddcdc1739136`  |
| 2025   | No file  | `ddcdc1739136`  |
| 2011   | No file  | `ddcdc1739136`  |
| 2005   | No file  | `ddcdc1739136`  |
| 2000   | No file  | `ddcdc1739136`  |
| 1996   | No file  | `ddcdc1739136`  |
| 1991   | No file  | `ddcdc1739136`  |
| 1985   | No file  | `ddcdc1739136`  |
| 1980   | No file  | `ddcdc1739136`  |
| 1969   | No file  | `ddcdc1739136`  |
| 1964   | No file  | `ddcdc1739136`  |
| 1958   | No file  | `ddcdc1739136`  |
| 1950   | No file  | `ddcdc1739136`  |
| 1945   | No file  | `ddcdc1739136`  |
| 1937   | No file  | `ddcdc1739136`  |
| 1933   | No file  | `ddcdc1739136`  |
| 1927   | No file  | `ddcdc1739136`  |
| 1921   | No file  | `ddcdc1739136`  |
| 1914   | No file  | `ddcdc1739136`  |
| 1908   | No file  | `ddcdc1739136`  |
| 1897   | No file  | `ddcdc1739136`  |
| 1892   | No file  | `ddcdc1739136`  |
| 1886   | No file  | `ddcdc1739136`  |
| 1881   | No file  | `ddcdc1739136`  |
| 1871   | No file  | `ddcdc1739136`  |
| 1866   | No file  | `ddcdc1739136`  |
| 1862   | No file  | `ddcdc1739136`  |
| 1854   | No file  | `ddcdc1739136`  |
| 1846   | No file  | `ddcdc1739136`  |
| 1838   | No file  | `ddcdc1739136`  |
| 1832   | No file  | `ddcdc1739136`  |
| 1826   | No file  | `ddcdc1739136`  |
| 1822   | No file  | `ddcdc1739136`  |
| 1818   | No file  | `ddcdc1739136`  |
| 1804   | No file  | `ddcdc1739136`  |
| 1794   | No file  | `ddcdc1739136`  |
| 1790   | No file  | `ddcdc1739136`  |
| 1784   | No file  | `ddcdc1739136`  |
| 1774   | No file  | `ddcdc1739136`  |
| 1771   | No file  | `ddcdc1739136`  |
| 1762   | No file  | `ddcdc1739136`  |
| 1759   | No file  | `ddcdc1739136`  |
| 1754   | No file  | `ddcdc1739136`  |
| 1749   | No file  | `ddcdc1739136`  |
| 1743   | No file  | `ddcdc1739136`  |
| 1737   | No file  | `ddcdc1739136`  |
| 1731   | No file  | `ddcdc1739136`  |
| 1725   | No file  | `ddcdc1739136`  |
| 1717   | No file  | `ddcdc1739136`  |
| 1710   | No file  | `ddcdc1739136`  |
| 1704   | No file  | `ddcdc1739136`  |
| 1698   | No file  | `ddcdc1739136`  |
| 1690   | No file  | `ddcdc1739136`  |
| 1685   | No file  | `ddcdc1739136`  |
| 1680   | No file  | `ddcdc1739136`  |
| 1674   | No file  | `ddcdc1739136`  |
| 1668   | No file  | `ddcdc1739136`  |
| 1659   | No file  | `ddcdc1739136`  |
| 1649   | No file  | `ddcdc1739136`  |
| 1642   | No file  | `ddcdc1739136`  |
| 1636   | No file  | `ddcdc1739136`  |
| 1628   | No file  | `ddcdc1739136`  |
| 1622   | No file  | `ddcdc1739136`  |
| 1614   | No file  | `ddcdc1739136`  |
| 1608   | No file  | `ddcdc1739136`  |
| 1602   | No file  | `ddcdc1739136`  |
| 1598   | No file  | `ddcdc1739136`  |
| 1594   | No file  | `ddcdc1739136`  |
| 1590   | No file  | `ddcdc1739136`  |
| 1587   | No file  | `ddcdc1739136`  |
| 1584   | No file  | `ddcdc1739136`  |
| 1579   | No file  | `ddcdc1739136`  |
| 1572   | No file  | `ddcdc1739136`  |
| 1565   | No file  | `ddcdc1739136`  |
| 1559   | No file  | `ddcdc1739136`  |
| 1554   | No file  | `ddcdc1739136`  |
| 1547   | No file  | `ddcdc1739136`  |
| 1537   | No file  | `ddcdc1739136`  |
| 1529   | No file  | `ddcdc1739136`  |
| 1524   | No file  | `ddcdc1739136`  |
| 1519   | No file  | `ddcdc1739136`  |
| 1509   | No file  | `ddcdc1739136`  |
| 1506   | No file  | `ddcdc1739136`  |
| 1504   | No file  | `ddcdc1739136`  |
| 1500   | No file  | `ddcdc1739136`  |
| 1493   | No file  | `ddcdc1739136`  |
| 1489   | No file  | `ddcdc1739136`  |
| 1485   | No file  | `ddcdc1739136`  |
| 1481   | No file  | `ddcdc1739136`  |
| 1474   | No file  | `ddcdc1739136`  |
| 1466   | No file  | `ddcdc1739136`  |
| 1462   | No file  | `ddcdc1739136`  |
| 1459   | No file  | `ddcdc1739136`  |
| 1453   | No file  | `ddcdc1739136`  |
| 1450   | No file  | `ddcdc1739136`  |
| 1445   | No file  | `ddcdc1739136`  |
| 1439   | No file  | `ddcdc1739136`  |
| 1433   | No file  | `ddcdc1739136`  |
| 1430   | No file  | `ddcdc1739136`  |
| 1426   | No file  | `ddcdc1739136`  |
| 1421   | No file  | `ddcdc1739136`  |
| 1417   | No file  | `ddcdc1739136`  |
| 1416   | No file  | `ddcdc1739136`  |
| 1409   | No file  | `ddcdc1739136`  |
| 1405   | No file  | `ddcdc1739136`  |
| 1401   | No file  | `ddcdc1739136`  |
| 1396   | No file  | `ddcdc1739136`  |
| 1391   | No file  | `ddcdc1739136`  |
| 1390   | No file  | `ddcdc1739136`  |
| 1386   | No file  | `ddcdc1739136`  |
| 1381   | No file  | `ddcdc1739136`  |
| 1379   | No file  | `ddcdc1739136`  |
| 1372   | No file  | `ddcdc1739136`  |
| 1366   | No file  | `ddcdc1739136`  |
| 1364   | No file  | `ddcdc1739136`  |
| 1363   | No file  | `ddcdc1739136`  |
| 1360   | No file  | `ddcdc1739136`  |
| 1358   | No file  | `ddcdc1739136`  |
| 1355   | No file  | `ddcdc1739136`  |
| 1351   | No file  | `ddcdc1739136`  |
| 1348   | No file  | `ddcdc1739136`  |
| 1346   | No file  | `ddcdc1739136`  |
| 1341   | No file  | `ddcdc1739136`  |
| 1340   | No file  | `ddcdc1739136`  |
| 1338   | No file  | `ddcdc1739136`  |
| 1335   | No file  | `ddcdc1739136`  |
| 1333   | No file  | `ddcdc1739136`  |
| 1329   | No file  | `ddcdc1739136`  |
| 1327   | No file  | `ddcdc1739136`  |
| 1324   | No file  | `ddcdc1739136`  |
| 1321   | No file  | `ddcdc1739136`  |
| 1319   | No file  | `ddcdc1739136`  |
| 1318   | No file  | `ddcdc1739136`  |
| 1316   | No file  | `ddcdc1739136`  |
| 1313   | No file  | `ddcdc1739136`  |
| 1311   | No file  | `ddcdc1739136`  |
| 1309   | No file  | `ddcdc1739136`  |
| 1304   | No file  | `ddcdc1739136`  |
| 1292   | No file  | `ddcdc1739136`  |
| 1286   | No file  | `ddcdc1739136`  |
| 1280   | No file  | `ddcdc1739136`  |
| 1276   | No file  | `ddcdc1739136`  |
| 1267   | No file  | `ddcdc1739136`  |
| 1261   | No file  | `ddcdc1739136`  |
| 1256   | No file  | `ddcdc1739136`  |
| 1250   | No file  | `ddcdc1739136`  |
| 1246   | No file  | `ddcdc1739136`  |
| 1239   | No file  | `ddcdc1739136`  |
| 1230   | No file  | `ddcdc1739136`  |
| 1226   | No file  | `ddcdc1739136`  |
| 1220   | No file  | `ddcdc1739136`  |
| 1217   | No file  | `ddcdc1739136`  |
| 1211   | No file  | `ddcdc1739136`  |
| 1210   | No file  | `ddcdc1739136`  |
| 1208   | No file  | `ddcdc1739136`  |
| 1203   | No file  | `ddcdc1739136`  |
| 1197   | No file  | `ddcdc1739136`  |
| 1194   | No file  | `ddcdc1739136`  |
| 1192   | No file  | `ddcdc1739136`  |
| 1187   | No file  | `ddcdc1739136`  |
| 1183   | No file  | `ddcdc1739136`  |
| 1177   | No file  | `ddcdc1739136`  |
| 1173   | No file  | `ddcdc1739136`  |
| 1167   | No file  | `ddcdc1739136`  |
| 1164   | No file  | `ddcdc1739136`  |
| 1156   | No file  | `ddcdc1739136`  |
| 1149   | No file  | `ddcdc1739136`  |
| 1144   | No file  | `ddcdc1739136`  |
| 1137   | No file  | `ddcdc1739136`  |
| 1132   | No file  | `ddcdc1739136`  |
| 1127   | No file  | `ddcdc1739136`  |
| 1122   | No file  | `ddcdc1739136`  |
| 1118   | No file  | `ddcdc1739136`  |
| 1114   | No file  | `ddcdc1739136`  |
| 1109   | No file  | `ddcdc1739136`  |
| 1102   | No file  | `ddcdc1739136`  |
| 1096   | No file  | `ddcdc1739136`  |
| 1088   | No file  | `ddcdc1739136`  |
| 1081   | No file  | `ddcdc1739136`  |
| 1076   | No file  | `ddcdc1739136`  |
| 1069   | No file  | `ddcdc1739136`  |
| 1064   | No file  | `ddcdc1739136`  |
| 1058   | No file  | `ddcdc1739136`  |
| 1051   | No file  | `ddcdc1739136`  |
| 1044   | No file  | `ddcdc1739136`  |
| 1036   | No file  | `ddcdc1739136`  |
| 1026   | No file  | `ddcdc1739136`  |
| 1016   | No file  | `ddcdc1739136`  |
| 1009   | No file  | `ddcdc1739136`  |
| 1005   | No file  | `ddcdc1739136`  |
| 1000   | No file  | `ddcdc1739136`  |
| 998    | No file  | `ddcdc1739136`  |
| 990    | No file  | `ddcdc1739136`  |
| 979    | No file  | `ddcdc1739136`  |
| 972    | No file  | `ddcdc1739136`  |
| 963    | No file  | `ddcdc1739136`  |
| 955    | No file  | `ddcdc1739136`  |
| 946    | No file  | `ddcdc1739136`  |
| 938    | No file  | `ddcdc1739136`  |
| 927    | No file  | `ddcdc1739136`  |
| 911    | No file  | `ddcdc1739136`  |
| 904    | No file  | `ddcdc1739136`  |
| 899    | No file  | `ddcdc1739136`  |
| 894    | No file  | `ddcdc1739136`  |
| 885    | No file  | `ddcdc1739136`  |
| 879    | No file  | `ddcdc1739136`  |
| 872    | No file  | `ddcdc1739136`  |
| 864    | No file  | `ddcdc1739136`  |
| 855    | No file  | `ddcdc1739136`  |
| 853    | No file  | `ddcdc1739136`  |
| 845    | No file  | `ddcdc1739136`  |
| 837    | No file  | `ddcdc1739136`  |
| 829    | No file  | `ddcdc1739136`  |
| 822    | No file  | `ddcdc1739136`  |
| 814    | No file  | `ddcdc1739136`  |
| 805    | No file  | `ddcdc1739136`  |
| 794    | No file  | `ddcdc1739136`  |
| 787    | No file  | `ddcdc1739136`  |
| 780    | No file  | `ddcdc1739136`  |
| 771    | No file  | `ddcdc1739136`  |
| 760    | No file  | `ddcdc1739136`  |
| 748    | No file  | `ddcdc1739136`  |
| 741    | No file  | `ddcdc1739136`  |
| 736    | No file  | `ddcdc1739136`  |
| 731    | No file  | `ddcdc1739136`  |
| 723    | No file  | `ddcdc1739136`  |
| 711    | No file  | `ddcdc1739136`  |
| 707    | No file  | `ddcdc1739136`  |
| 697    | No file  | `ddcdc1739136`  |
| 689    | No file  | `ddcdc1739136`  |
| 683    | No file  | `ddcdc1739136`  |
| 678    | No file  | `ddcdc1739136`  |
| 670    | No file  | `ddcdc1739136`  |
| 661    | No file  | `ddcdc1739136`  |
| 656    | No file  | `ddcdc1739136`  |
| 652    | No file  | `ddcdc1739136`  |
| 643    | No file  | `ddcdc1739136`  |
| 637    | No file  | `ddcdc1739136`  |
| 630    | No file  | `ddcdc1739136`  |
| 627    | No file  | `ddcdc1739136`  |
| 621    | No file  | `ddcdc1739136`  |
| 617    | No file  | `ddcdc1739136`  |
| 615    | No file  | `ddcdc1739136`  |
| 606    | No file  | `ddcdc1739136`  |
| 599    | No file  | `ddcdc1739136`  |
| 592    | No file  | `ddcdc1739136`  |
| 586    | No file  | `ddcdc1739136`  |
| 577    | No file  | `ddcdc1739136`  |
| 569    | No file  | `ddcdc1739136`  |
| 561    | No file  | `ddcdc1739136`  |
| 554    | No file  | `ddcdc1739136`  |
| 542    | No file  | `ddcdc1739136`  |
| 532    | No file  | `ddcdc1739136`  |
| 531    | No file  | `ddcdc1739136`  |
| 526    | No file  | `ddcdc1739136`  |
| 521    | No file  | `ddcdc1739136`  |
| 517    | No file  | `ddcdc1739136`  |
| 510    | No file  | `ddcdc1739136`  |
| 508    | No file  | `ddcdc1739136`  |
| 504    | No file  | `ddcdc1739136`  |
| 497    | No file  | `ddcdc1739136`  |
| 491    | No file  | `ddcdc1739136`  |
| 485    | No file  | `ddcdc1739136`  |
| 478    | No file  | `ddcdc1739136`  |
| 472    | No file  | `ddcdc1739136`  |
| 466    | No file  | `ddcdc1739136`  |
| 457    | No file  | `ddcdc1739136`  |
| 452    | No file  | `ddcdc1739136`  |
| 449    | No file  | `ddcdc1739136`  |
| 435    | No file  | `ddcdc1739136`  |

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
