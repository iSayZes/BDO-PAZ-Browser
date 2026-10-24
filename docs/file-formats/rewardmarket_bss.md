# `rewardmarket.bss` Format

## Purpose

The pet exchange: per trade the pet it takes and the items it gives for
it. On client 3482 every trade takes one pet and gives a Choose Your Tier 3
Exchange Gift Box (`1000130`) for a tier 3 pet, or a Choose Your Tier 4
Exchange Gift Box (`1000131`) and an `[Event] Pet Exchange Token`
(`1000692`) for a tier 4 pet. The exchange window Lua
(`panel_window_rewardmarket_all_1.luac`) reads a trade through
`ToClient_GetRewardMarketStaticStatusByKey(tradeKey)` and its rewards
through `ToClient_GetRewardMarketRewardItemKey(tradeKey, index)` and
`ToClient_GetRewardMarketRewardItemCount(tradeKey, index)`; its tabs are
`__eRewardMarketTradeType_PetToItem` and `_ItemToItem`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records               | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | --------------------- | --------- |
| 1      | 2844 and later | 3483    | `rewardmarket.bss` | 33,122 | 1,264 Reward, 854 Row | 12        |

| Layout | File               | Known            | Unknown         |
| ------ | ------------------ | ---------------- | --------------- |
| 1      | `rewardmarket.bss` | 23,728 B (71.6%) | 9,394 B (28.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `421799c0ebcf`  |
| 3482   | Layout 1 | `421799c0ebcf`  |
| 3474   | Layout 1 | `421799c0ebcf`  |
| 3473   | Layout 1 | `421799c0ebcf`  |
| 3464   | Layout 1 | `421799c0ebcf`  |
| 3458   | Layout 1 | `421799c0ebcf`  |
| 3454   | Layout 1 | `421799c0ebcf`  |
| 3444   | Layout 1 | `421799c0ebcf`  |
| 3435   | Layout 1 | `421799c0ebcf`  |
| 3426   | Layout 1 | `421799c0ebcf`  |
| 3418   | Layout 1 | `421799c0ebcf`  |
| 3412   | Layout 1 | `421799c0ebcf`  |
| 3402   | Layout 1 | `421799c0ebcf`  |
| 3396   | Layout 1 | `421799c0ebcf`  |
| 3387   | Layout 1 | `421799c0ebcf`  |
| 3381   | Layout 1 | `421799c0ebcf`  |
| 3373   | Layout 1 | `421799c0ebcf`  |
| 3364   | Layout 1 | `421799c0ebcf`  |
| 3356   | Layout 1 | `421799c0ebcf`  |
| 3349   | Layout 1 | `421799c0ebcf`  |
| 3342   | Layout 1 | `421799c0ebcf`  |
| 3335   | Layout 1 | `421799c0ebcf`  |
| 3326   | Layout 1 | `421799c0ebcf`  |
| 3321   | Layout 1 | `421799c0ebcf`  |
| 3314   | Layout 1 | `421799c0ebcf`  |
| 3303   | Layout 1 | `421799c0ebcf`  |
| 3302   | Layout 1 | `421799c0ebcf`  |
| 3293   | Layout 1 | `421799c0ebcf`  |
| 3283   | Layout 1 | `421799c0ebcf`  |
| 3275   | Layout 1 | `421799c0ebcf`  |
| 3267   | Layout 1 | `421799c0ebcf`  |
| 3258   | Layout 1 | `421799c0ebcf`  |
| 3251   | Layout 1 | `421799c0ebcf`  |
| 3242   | Layout 1 | `421799c0ebcf`  |
| 3235   | Layout 1 | `421799c0ebcf`  |
| 3229   | Layout 1 | `421799c0ebcf`  |
| 3212   | Layout 1 | `421799c0ebcf`  |
| 3203   | Layout 1 | `421799c0ebcf`  |
| 3193   | Layout 1 | `421799c0ebcf`  |
| 3186   | Layout 1 | `421799c0ebcf`  |
| 3177   | Layout 1 | `421799c0ebcf`  |
| 3169   | Layout 1 | `421799c0ebcf`  |
| 3158   | Layout 1 | `421799c0ebcf`  |
| 3151   | Layout 1 | `421799c0ebcf`  |
| 3144   | Layout 1 | `421799c0ebcf`  |
| 3133   | Layout 1 | `421799c0ebcf`  |
| 3125   | Layout 1 | `421799c0ebcf`  |
| 3118   | Layout 1 | `421799c0ebcf`  |
| 3111   | Layout 1 | `421799c0ebcf`  |
| 3103   | Layout 1 | `421799c0ebcf`  |
| 3095   | Layout 1 | `421799c0ebcf`  |
| 3086   | Layout 1 | `421799c0ebcf`  |
| 3072   | Layout 1 | `421799c0ebcf`  |
| 3062   | Layout 1 | `421799c0ebcf`  |
| 3052   | Layout 1 | `421799c0ebcf`  |
| 3045   | Layout 1 | `421799c0ebcf`  |
| 3037   | Layout 1 | `421799c0ebcf`  |
| 3030   | Layout 1 | `421799c0ebcf`  |
| 3021   | Layout 1 | `421799c0ebcf`  |
| 3012   | Layout 1 | `421799c0ebcf`  |
| 3002   | Layout 1 | `421799c0ebcf`  |
| 2995   | Layout 1 | `421799c0ebcf`  |
| 2987   | Layout 1 | `421799c0ebcf`  |
| 2978   | Layout 1 | `421799c0ebcf`  |
| 2970   | Layout 1 | `421799c0ebcf`  |
| 2959   | Layout 1 | `421799c0ebcf`  |
| 2951   | Layout 1 | `421799c0ebcf`  |
| 2942   | Layout 1 | `421799c0ebcf`  |
| 2935   | Layout 1 | `421799c0ebcf`  |
| 2932   | Layout 1 | `421799c0ebcf`  |
| 2923   | Layout 1 | `421799c0ebcf`  |
| 2919   | Layout 1 | `421799c0ebcf`  |
| 2907   | Layout 1 | `421799c0ebcf`  |
| 2900   | Layout 1 | `421799c0ebcf`  |
| 2891   | Layout 1 | `421799c0ebcf`  |
| 2882   | Layout 1 | `421799c0ebcf`  |
| 2872   | Layout 1 | `421799c0ebcf`  |
| 2863   | Layout 1 | `421799c0ebcf`  |
| 2855   | Layout 1 | `421799c0ebcf`  |
| 2849   | Layout 1 | `421799c0ebcf`  |
| 2844   | Layout 1 | `421799c0ebcf`  |
| 2834   | No file  | `421799c0ebcf`  |
| 2825   | No file  | `421799c0ebcf`  |
| 2819   | No file  | `421799c0ebcf`  |
| 2811   | No file  | `421799c0ebcf`  |
| 2803   | No file  | `421799c0ebcf`  |
| 2794   | No file  | `421799c0ebcf`  |
| 2783   | No file  | `421799c0ebcf`  |
| 2774   | No file  | `421799c0ebcf`  |
| 2765   | No file  | `421799c0ebcf`  |
| 2756   | No file  | `421799c0ebcf`  |
| 2750   | No file  | `421799c0ebcf`  |
| 2743   | No file  | `421799c0ebcf`  |
| 2736   | No file  | `421799c0ebcf`  |
| 2726   | No file  | `421799c0ebcf`  |
| 2717   | No file  | `421799c0ebcf`  |
| 2709   | No file  | `421799c0ebcf`  |
| 2703   | No file  | `421799c0ebcf`  |
| 2695   | No file  | `421799c0ebcf`  |
| 2684   | No file  | `421799c0ebcf`  |
| 2672   | No file  | `421799c0ebcf`  |
| 2665   | No file  | `421799c0ebcf`  |
| 2657   | No file  | `421799c0ebcf`  |
| 2649   | No file  | `421799c0ebcf`  |
| 2644   | No file  | `421799c0ebcf`  |
| 2637   | No file  | `421799c0ebcf`  |
| 2629   | No file  | `421799c0ebcf`  |
| 2619   | No file  | `421799c0ebcf`  |
| 2612   | No file  | `421799c0ebcf`  |
| 2606   | No file  | `421799c0ebcf`  |
| 2602   | No file  | `421799c0ebcf`  |
| 2601   | No file  | `421799c0ebcf`  |
| 2592   | No file  | `421799c0ebcf`  |
| 2583   | No file  | `421799c0ebcf`  |
| 2575   | No file  | `421799c0ebcf`  |
| 2567   | No file  | `421799c0ebcf`  |
| 2560   | No file  | `421799c0ebcf`  |
| 2553   | No file  | `421799c0ebcf`  |
| 2545   | No file  | `421799c0ebcf`  |
| 2538   | No file  | `421799c0ebcf`  |
| 2529   | No file  | `421799c0ebcf`  |
| 2519   | No file  | `421799c0ebcf`  |
| 2513   | No file  | `421799c0ebcf`  |
| 2510   | No file  | `421799c0ebcf`  |
| 2507   | No file  | `421799c0ebcf`  |
| 2503   | No file  | `421799c0ebcf`  |
| 2498   | No file  | `421799c0ebcf`  |
| 2492   | No file  | `421799c0ebcf`  |
| 2487   | No file  | `421799c0ebcf`  |
| 2480   | No file  | `421799c0ebcf`  |
| 2474   | No file  | `421799c0ebcf`  |
| 2468   | No file  | `421799c0ebcf`  |
| 2460   | No file  | `421799c0ebcf`  |
| 2453   | No file  | `421799c0ebcf`  |
| 2444   | No file  | `421799c0ebcf`  |
| 2438   | No file  | `421799c0ebcf`  |
| 2434   | No file  | `421799c0ebcf`  |
| 2429   | No file  | `421799c0ebcf`  |
| 2421   | No file  | `421799c0ebcf`  |
| 2414   | No file  | `421799c0ebcf`  |
| 2407   | No file  | `421799c0ebcf`  |
| 2401   | No file  | `421799c0ebcf`  |
| 2397   | No file  | `421799c0ebcf`  |
| 2393   | No file  | `421799c0ebcf`  |
| 2384   | No file  | `421799c0ebcf`  |
| 2378   | No file  | `421799c0ebcf`  |
| 2372   | No file  | `421799c0ebcf`  |
| 2358   | No file  | `421799c0ebcf`  |
| 2352   | No file  | `421799c0ebcf`  |
| 2347   | No file  | `421799c0ebcf`  |
| 2343   | No file  | `421799c0ebcf`  |
| 2335   | No file  | `421799c0ebcf`  |
| 2327   | No file  | `421799c0ebcf`  |
| 2324   | No file  | `421799c0ebcf`  |
| 2319   | No file  | `421799c0ebcf`  |
| 2313   | No file  | `421799c0ebcf`  |
| 2308   | No file  | `421799c0ebcf`  |
| 2302   | No file  | `421799c0ebcf`  |
| 2295   | No file  | `421799c0ebcf`  |
| 2290   | No file  | `421799c0ebcf`  |
| 2284   | No file  | `421799c0ebcf`  |
| 2276   | No file  | `421799c0ebcf`  |
| 2269   | No file  | `421799c0ebcf`  |
| 2259   | No file  | `421799c0ebcf`  |
| 2250   | No file  | `421799c0ebcf`  |
| 2243   | No file  | `421799c0ebcf`  |
| 2235   | No file  | `421799c0ebcf`  |
| 2229   | No file  | `421799c0ebcf`  |
| 2224   | No file  | `421799c0ebcf`  |
| 2218   | No file  | `421799c0ebcf`  |
| 2215   | No file  | `421799c0ebcf`  |
| 2207   | No file  | `421799c0ebcf`  |
| 2203   | No file  | `421799c0ebcf`  |
| 2196   | No file  | `421799c0ebcf`  |
| 2192   | No file  | `421799c0ebcf`  |
| 2189   | No file  | `421799c0ebcf`  |
| 2183   | No file  | `421799c0ebcf`  |
| 2179   | No file  | `421799c0ebcf`  |
| 2171   | No file  | `421799c0ebcf`  |
| 2163   | No file  | `421799c0ebcf`  |
| 2156   | No file  | `421799c0ebcf`  |
| 2151   | No file  | `421799c0ebcf`  |
| 2147   | No file  | `421799c0ebcf`  |
| 2142   | No file  | `421799c0ebcf`  |
| 2138   | No file  | `421799c0ebcf`  |
| 2134   | No file  | `421799c0ebcf`  |
| 2130   | No file  | `421799c0ebcf`  |
| 2122   | No file  | `421799c0ebcf`  |
| 2107   | No file  | `421799c0ebcf`  |
| 2098   | No file  | `421799c0ebcf`  |
| 2089   | No file  | `421799c0ebcf`  |
| 2081   | No file  | `421799c0ebcf`  |
| 2073   | No file  | `421799c0ebcf`  |
| 2067   | No file  | `421799c0ebcf`  |
| 2063   | No file  | `421799c0ebcf`  |
| 2059   | No file  | `421799c0ebcf`  |
| 2052   | No file  | `421799c0ebcf`  |
| 2044   | No file  | `421799c0ebcf`  |
| 2039   | No file  | `421799c0ebcf`  |
| 2032   | No file  | `421799c0ebcf`  |
| 2025   | No file  | `421799c0ebcf`  |
| 2011   | No file  | `421799c0ebcf`  |
| 2005   | No file  | `421799c0ebcf`  |
| 2000   | No file  | `421799c0ebcf`  |
| 1996   | No file  | `421799c0ebcf`  |
| 1991   | No file  | `421799c0ebcf`  |
| 1985   | No file  | `421799c0ebcf`  |
| 1980   | No file  | `421799c0ebcf`  |
| 1969   | No file  | `421799c0ebcf`  |
| 1964   | No file  | `421799c0ebcf`  |
| 1958   | No file  | `421799c0ebcf`  |
| 1950   | No file  | `421799c0ebcf`  |
| 1945   | No file  | `421799c0ebcf`  |
| 1937   | No file  | `421799c0ebcf`  |
| 1933   | No file  | `421799c0ebcf`  |
| 1927   | No file  | `421799c0ebcf`  |
| 1921   | No file  | `421799c0ebcf`  |
| 1914   | No file  | `421799c0ebcf`  |
| 1908   | No file  | `421799c0ebcf`  |
| 1897   | No file  | `421799c0ebcf`  |
| 1892   | No file  | `421799c0ebcf`  |
| 1886   | No file  | `421799c0ebcf`  |
| 1881   | No file  | `421799c0ebcf`  |
| 1871   | No file  | `421799c0ebcf`  |
| 1866   | No file  | `421799c0ebcf`  |
| 1862   | No file  | `421799c0ebcf`  |
| 1854   | No file  | `421799c0ebcf`  |
| 1846   | No file  | `421799c0ebcf`  |
| 1838   | No file  | `421799c0ebcf`  |
| 1832   | No file  | `421799c0ebcf`  |
| 1826   | No file  | `421799c0ebcf`  |
| 1822   | No file  | `421799c0ebcf`  |
| 1818   | No file  | `421799c0ebcf`  |
| 1804   | No file  | `421799c0ebcf`  |
| 1794   | No file  | `421799c0ebcf`  |
| 1790   | No file  | `421799c0ebcf`  |
| 1784   | No file  | `421799c0ebcf`  |
| 1774   | No file  | `421799c0ebcf`  |
| 1771   | No file  | `421799c0ebcf`  |
| 1762   | No file  | `421799c0ebcf`  |
| 1759   | No file  | `421799c0ebcf`  |
| 1754   | No file  | `421799c0ebcf`  |
| 1749   | No file  | `421799c0ebcf`  |
| 1743   | No file  | `421799c0ebcf`  |
| 1737   | No file  | `421799c0ebcf`  |
| 1731   | No file  | `421799c0ebcf`  |
| 1725   | No file  | `421799c0ebcf`  |
| 1717   | No file  | `421799c0ebcf`  |
| 1710   | No file  | `421799c0ebcf`  |
| 1704   | No file  | `421799c0ebcf`  |
| 1698   | No file  | `421799c0ebcf`  |
| 1690   | No file  | `421799c0ebcf`  |
| 1685   | No file  | `421799c0ebcf`  |
| 1680   | No file  | `421799c0ebcf`  |
| 1674   | No file  | `421799c0ebcf`  |
| 1668   | No file  | `421799c0ebcf`  |
| 1659   | No file  | `421799c0ebcf`  |
| 1649   | No file  | `421799c0ebcf`  |
| 1642   | No file  | `421799c0ebcf`  |
| 1636   | No file  | `421799c0ebcf`  |
| 1628   | No file  | `421799c0ebcf`  |
| 1622   | No file  | `421799c0ebcf`  |
| 1614   | No file  | `421799c0ebcf`  |
| 1608   | No file  | `421799c0ebcf`  |
| 1602   | No file  | `421799c0ebcf`  |
| 1598   | No file  | `421799c0ebcf`  |
| 1594   | No file  | `421799c0ebcf`  |
| 1590   | No file  | `421799c0ebcf`  |
| 1587   | No file  | `421799c0ebcf`  |
| 1584   | No file  | `421799c0ebcf`  |
| 1579   | No file  | `421799c0ebcf`  |
| 1572   | No file  | `421799c0ebcf`  |
| 1565   | No file  | `421799c0ebcf`  |
| 1559   | No file  | `421799c0ebcf`  |
| 1554   | No file  | `421799c0ebcf`  |
| 1547   | No file  | `421799c0ebcf`  |
| 1537   | No file  | `421799c0ebcf`  |
| 1529   | No file  | `421799c0ebcf`  |
| 1524   | No file  | `421799c0ebcf`  |
| 1519   | No file  | `421799c0ebcf`  |
| 1509   | No file  | `421799c0ebcf`  |
| 1506   | No file  | `421799c0ebcf`  |
| 1504   | No file  | `421799c0ebcf`  |
| 1500   | No file  | `421799c0ebcf`  |
| 1493   | No file  | `421799c0ebcf`  |
| 1489   | No file  | `421799c0ebcf`  |
| 1485   | No file  | `421799c0ebcf`  |
| 1481   | No file  | `421799c0ebcf`  |
| 1474   | No file  | `421799c0ebcf`  |
| 1466   | No file  | `421799c0ebcf`  |
| 1462   | No file  | `421799c0ebcf`  |
| 1459   | No file  | `421799c0ebcf`  |
| 1453   | No file  | `421799c0ebcf`  |
| 1450   | No file  | `421799c0ebcf`  |
| 1445   | No file  | `421799c0ebcf`  |
| 1439   | No file  | `421799c0ebcf`  |
| 1433   | No file  | `421799c0ebcf`  |
| 1430   | No file  | `421799c0ebcf`  |
| 1426   | No file  | `421799c0ebcf`  |
| 1421   | No file  | `421799c0ebcf`  |
| 1417   | No file  | `421799c0ebcf`  |
| 1416   | No file  | `421799c0ebcf`  |
| 1409   | No file  | `421799c0ebcf`  |
| 1405   | No file  | `421799c0ebcf`  |
| 1401   | No file  | `421799c0ebcf`  |
| 1396   | No file  | `421799c0ebcf`  |
| 1391   | No file  | `421799c0ebcf`  |
| 1390   | No file  | `421799c0ebcf`  |
| 1386   | No file  | `421799c0ebcf`  |
| 1381   | No file  | `421799c0ebcf`  |
| 1379   | No file  | `421799c0ebcf`  |
| 1372   | No file  | `421799c0ebcf`  |
| 1366   | No file  | `421799c0ebcf`  |
| 1364   | No file  | `421799c0ebcf`  |
| 1363   | No file  | `421799c0ebcf`  |
| 1360   | No file  | `421799c0ebcf`  |
| 1358   | No file  | `421799c0ebcf`  |
| 1355   | No file  | `421799c0ebcf`  |
| 1351   | No file  | `421799c0ebcf`  |
| 1348   | No file  | `421799c0ebcf`  |
| 1346   | No file  | `421799c0ebcf`  |
| 1341   | No file  | `421799c0ebcf`  |
| 1340   | No file  | `421799c0ebcf`  |
| 1338   | No file  | `421799c0ebcf`  |
| 1335   | No file  | `421799c0ebcf`  |
| 1333   | No file  | `421799c0ebcf`  |
| 1329   | No file  | `421799c0ebcf`  |
| 1327   | No file  | `421799c0ebcf`  |
| 1324   | No file  | `421799c0ebcf`  |
| 1321   | No file  | `421799c0ebcf`  |
| 1319   | No file  | `421799c0ebcf`  |
| 1318   | No file  | `421799c0ebcf`  |
| 1316   | No file  | `421799c0ebcf`  |
| 1313   | No file  | `421799c0ebcf`  |
| 1311   | No file  | `421799c0ebcf`  |
| 1309   | No file  | `421799c0ebcf`  |
| 1304   | No file  | `421799c0ebcf`  |
| 1292   | No file  | `421799c0ebcf`  |
| 1286   | No file  | `421799c0ebcf`  |
| 1280   | No file  | `421799c0ebcf`  |
| 1276   | No file  | `421799c0ebcf`  |
| 1267   | No file  | `421799c0ebcf`  |
| 1261   | No file  | `421799c0ebcf`  |
| 1256   | No file  | `421799c0ebcf`  |
| 1250   | No file  | `421799c0ebcf`  |
| 1246   | No file  | `421799c0ebcf`  |
| 1239   | No file  | `421799c0ebcf`  |
| 1230   | No file  | `421799c0ebcf`  |
| 1226   | No file  | `421799c0ebcf`  |
| 1220   | No file  | `421799c0ebcf`  |
| 1217   | No file  | `421799c0ebcf`  |
| 1211   | No file  | `421799c0ebcf`  |
| 1210   | No file  | `421799c0ebcf`  |
| 1208   | No file  | `421799c0ebcf`  |
| 1203   | No file  | `421799c0ebcf`  |
| 1197   | No file  | `421799c0ebcf`  |
| 1194   | No file  | `421799c0ebcf`  |
| 1192   | No file  | `421799c0ebcf`  |
| 1187   | No file  | `421799c0ebcf`  |
| 1183   | No file  | `421799c0ebcf`  |
| 1177   | No file  | `421799c0ebcf`  |
| 1173   | No file  | `421799c0ebcf`  |
| 1167   | No file  | `421799c0ebcf`  |
| 1164   | No file  | `421799c0ebcf`  |
| 1156   | No file  | `421799c0ebcf`  |
| 1149   | No file  | `421799c0ebcf`  |
| 1144   | No file  | `421799c0ebcf`  |
| 1137   | No file  | `421799c0ebcf`  |
| 1132   | No file  | `421799c0ebcf`  |
| 1127   | No file  | `421799c0ebcf`  |
| 1122   | No file  | `421799c0ebcf`  |
| 1118   | No file  | `421799c0ebcf`  |
| 1114   | No file  | `421799c0ebcf`  |
| 1109   | No file  | `421799c0ebcf`  |
| 1102   | No file  | `421799c0ebcf`  |
| 1096   | No file  | `421799c0ebcf`  |
| 1088   | No file  | `421799c0ebcf`  |
| 1081   | No file  | `421799c0ebcf`  |
| 1076   | No file  | `421799c0ebcf`  |
| 1069   | No file  | `421799c0ebcf`  |
| 1064   | No file  | `421799c0ebcf`  |
| 1058   | No file  | `421799c0ebcf`  |
| 1051   | No file  | `421799c0ebcf`  |
| 1044   | No file  | `421799c0ebcf`  |
| 1036   | No file  | `421799c0ebcf`  |
| 1026   | No file  | `421799c0ebcf`  |
| 1016   | No file  | `421799c0ebcf`  |
| 1009   | No file  | `421799c0ebcf`  |
| 1005   | No file  | `421799c0ebcf`  |
| 1000   | No file  | `421799c0ebcf`  |
| 998    | No file  | `421799c0ebcf`  |
| 990    | No file  | `421799c0ebcf`  |
| 979    | No file  | `421799c0ebcf`  |
| 972    | No file  | `421799c0ebcf`  |
| 963    | No file  | `421799c0ebcf`  |
| 955    | No file  | `421799c0ebcf`  |
| 946    | No file  | `421799c0ebcf`  |
| 938    | No file  | `421799c0ebcf`  |
| 927    | No file  | `421799c0ebcf`  |
| 911    | No file  | `421799c0ebcf`  |
| 904    | No file  | `421799c0ebcf`  |
| 899    | No file  | `421799c0ebcf`  |
| 894    | No file  | `421799c0ebcf`  |
| 885    | No file  | `421799c0ebcf`  |
| 879    | No file  | `421799c0ebcf`  |
| 872    | No file  | `421799c0ebcf`  |
| 864    | No file  | `421799c0ebcf`  |
| 855    | No file  | `421799c0ebcf`  |
| 853    | No file  | `421799c0ebcf`  |
| 845    | No file  | `421799c0ebcf`  |
| 837    | No file  | `421799c0ebcf`  |
| 829    | No file  | `421799c0ebcf`  |
| 822    | No file  | `421799c0ebcf`  |
| 814    | No file  | `421799c0ebcf`  |
| 805    | No file  | `421799c0ebcf`  |
| 794    | No file  | `421799c0ebcf`  |
| 787    | No file  | `421799c0ebcf`  |
| 780    | No file  | `421799c0ebcf`  |
| 771    | No file  | `421799c0ebcf`  |
| 760    | No file  | `421799c0ebcf`  |
| 748    | No file  | `421799c0ebcf`  |
| 741    | No file  | `421799c0ebcf`  |
| 736    | No file  | `421799c0ebcf`  |
| 731    | No file  | `421799c0ebcf`  |
| 723    | No file  | `421799c0ebcf`  |
| 711    | No file  | `421799c0ebcf`  |
| 707    | No file  | `421799c0ebcf`  |
| 697    | No file  | `421799c0ebcf`  |
| 689    | No file  | `421799c0ebcf`  |
| 683    | No file  | `421799c0ebcf`  |
| 678    | No file  | `421799c0ebcf`  |
| 670    | No file  | `421799c0ebcf`  |
| 661    | No file  | `421799c0ebcf`  |
| 656    | No file  | `421799c0ebcf`  |
| 652    | No file  | `421799c0ebcf`  |
| 643    | No file  | `421799c0ebcf`  |
| 637    | No file  | `421799c0ebcf`  |
| 630    | No file  | `421799c0ebcf`  |
| 627    | No file  | `421799c0ebcf`  |
| 621    | No file  | `421799c0ebcf`  |
| 617    | No file  | `421799c0ebcf`  |
| 615    | No file  | `421799c0ebcf`  |
| 606    | No file  | `421799c0ebcf`  |
| 599    | No file  | `421799c0ebcf`  |
| 592    | No file  | `421799c0ebcf`  |
| 586    | No file  | `421799c0ebcf`  |
| 577    | No file  | `421799c0ebcf`  |
| 569    | No file  | `421799c0ebcf`  |
| 561    | No file  | `421799c0ebcf`  |
| 554    | No file  | `421799c0ebcf`  |
| 542    | No file  | `421799c0ebcf`  |
| 532    | No file  | `421799c0ebcf`  |
| 531    | No file  | `421799c0ebcf`  |
| 526    | No file  | `421799c0ebcf`  |
| 521    | No file  | `421799c0ebcf`  |
| 517    | No file  | `421799c0ebcf`  |
| 510    | No file  | `421799c0ebcf`  |
| 508    | No file  | `421799c0ebcf`  |
| 504    | No file  | `421799c0ebcf`  |
| 497    | No file  | `421799c0ebcf`  |
| 491    | No file  | `421799c0ebcf`  |
| 485    | No file  | `421799c0ebcf`  |
| 478    | No file  | `421799c0ebcf`  |
| 472    | No file  | `421799c0ebcf`  |
| 466    | No file  | `421799c0ebcf`  |
| 457    | No file  | `421799c0ebcf`  |
| 452    | No file  | `421799c0ebcf`  |
| 449    | No file  | `421799c0ebcf`  |
| 435    | No file  | `421799c0ebcf`  |

<!-- versions:end -->

## Companion Files

None. The handler names the pet from LOC type 6 and links it to its
[`pet.dbss`](pet_dbss.md) row; the reward items take their names and icons
from the item lookup indexes.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                       |
| ------------------- | -------------- | ------------ | ------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                |
| `+0x04`             | u32            | row_count    | Number of trades, `854` on client 3482      |
| `+0x08`             | Row[row_count] | rows         | See Row                                     |
| `rows+0x00`         | String Table   | string_table | See String Table                            |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                  |

### Row (variable: 21 bytes + rewards)

| Offset  | Type                 | Field        | Notes                                                                       |
| ------- | -------------------- | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u16                  | trade_key    | Row key, the Lua `tradeKeyRaw`; unique, `1` to `866` on client 3482          |
| `+0x02` | u32                  | pet_key      | The pet traded in: a [`pet.dbss`](pet_dbss.md) pet ID (854 of 854 on client 3482), named by LOC type 6 |
| `+0x06` | bytes[11]            | unknown_06   | `0` on every row of client 3482                                             |
| `+0x11` | u32                  | reward_count | Number of `rewards`, `1` or `2` on client 3482                              |
| `+0x15` | Reward[reward_count] | rewards      | See Reward                                                                  |

### Reward (12 bytes)

| Offset  | Type | Field      | Notes                                       |
| ------- | ---- | ---------- | ------------------------------------------- |
| `+0x00` | u32  | item_key   | Item given (`ItemEnchantKey`, level 0 here) |
| `+0x04` | u64  | item_count | Count, `1` on every reward of client 3482   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes             |
| ------- | ------------------ | ------------ | ----------------- |
| `+0x00` | u32                | string_count | `0` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | None              |

## Notes

- The tier 3 box goes with the pets whose `pet.dbss` `tier` is `2` (444
  trades), the tier 4 box and token with `tier` `3` (410 trades), on
  client 3482.
- Client 1784 has no `rewardmarket.bss`, and a private server's
  `DataSheets.bexcel` on client 1784 has no reward market sheet, so the
  field names come from the Lua.

## Open Questions

### What the Eleven Zero Bytes Hold

`unknown_06` is `0` on all 854 rows of client 3482, where every trade is
`PetToItem`. An item to item trade would need a material item key and
count, and a trade type byte would tell the two tabs apart; the eleven
bytes would hold those if an `ItemToItem` trade ever ships.
