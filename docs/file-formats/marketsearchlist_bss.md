# `marketsearchlist.bss` Format

## Purpose

The item list of the Central Market name search: one 12-byte row per item
with the item key, the string table index of the item's Korean name and a
u32 `unknown_08`. On client 3483 the file holds 12,842 items, every key an
item of [`itemenchant.dbss`](itemenchant_dbss.md), and each row's string
equals the Korean name `itemenchant.dbss` stores for that item (12,842 of
12,842).

The Central Market window (`panel_window_marketplace_itemmarket_renew.luac`,
client 3482) passes the typed text to `ToClient_searchWorldMarketItem`,
lists the hits with `ToClient_getSearchWorldMarketItemListSize`,
`ToClient_getSearchWorldMarketItemName(index)` and
`ToClient_getSearchWorldMarketItemKey(index)`, and draws each hit with
`PaGlobalFunc_ItemMarket_CreateControlMarketSearchList`. In a private server's server executable on
client 1784 the file is read by
`ItemEnchantStaticStatusManager::readFromBinary`, whose error text names
`marketSearchList()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes   | Records    | Row bytes |
| ------ | -------------- | ---------------------- | ------- | ---------- | --------- |
| 2      | 1319 and later | `marketsearchlist.bss` | 556,961 | 12,842 Row | 12        |
| 1      | 1109 to 1318   | `marketsearchlist.bss` | 285,016 | 7,594 Row  | 8         |

| Layout | File                   | Known              | Unknown         |
| ------ | ---------------------- | ------------------ | --------------- |
| 2      | `marketsearchlist.bss` | 505,593 B (90.8%)  | 51,368 B (9.2%) |
| 1      | `marketsearchlist.bss` | 285,016 B (100.0%) | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `74462d33c6db`  |
| 3482   | Layout 2 | `74462d33c6db`  |
| 3474   | Layout 2 | `74462d33c6db`  |
| 3473   | Layout 2 | `74462d33c6db`  |
| 3464   | Layout 2 | `74462d33c6db`  |
| 3458   | Layout 2 | `74462d33c6db`  |
| 3454   | Layout 2 | `74462d33c6db`  |
| 3444   | Layout 2 | `74462d33c6db`  |
| 3435   | Layout 2 | `74462d33c6db`  |
| 3426   | Layout 2 | `74462d33c6db`  |
| 3418   | Layout 2 | `74462d33c6db`  |
| 3412   | Layout 2 | `74462d33c6db`  |
| 3402   | Layout 2 | `74462d33c6db`  |
| 3396   | Layout 2 | `74462d33c6db`  |
| 3387   | Layout 2 | `74462d33c6db`  |
| 3381   | Layout 2 | `74462d33c6db`  |
| 3373   | Layout 2 | `74462d33c6db`  |
| 3364   | Layout 2 | `74462d33c6db`  |
| 3356   | Layout 2 | `74462d33c6db`  |
| 3349   | Layout 2 | `74462d33c6db`  |
| 3342   | Layout 2 | `74462d33c6db`  |
| 3335   | Layout 2 | `74462d33c6db`  |
| 3326   | Layout 2 | `74462d33c6db`  |
| 3321   | Layout 2 | `74462d33c6db`  |
| 3314   | Layout 2 | `74462d33c6db`  |
| 3303   | Layout 2 | `74462d33c6db`  |
| 3302   | Layout 2 | `74462d33c6db`  |
| 3293   | Layout 2 | `74462d33c6db`  |
| 3283   | Layout 2 | `74462d33c6db`  |
| 3275   | Layout 2 | `74462d33c6db`  |
| 3267   | Layout 2 | `74462d33c6db`  |
| 3258   | Layout 2 | `74462d33c6db`  |
| 3251   | Layout 2 | `74462d33c6db`  |
| 3242   | Layout 2 | `74462d33c6db`  |
| 3235   | Layout 2 | `74462d33c6db`  |
| 3229   | Layout 2 | `74462d33c6db`  |
| 3212   | Layout 2 | `74462d33c6db`  |
| 3203   | Layout 2 | `74462d33c6db`  |
| 3193   | Layout 2 | `74462d33c6db`  |
| 3186   | Layout 2 | `74462d33c6db`  |
| 3177   | Layout 2 | `74462d33c6db`  |
| 3169   | Layout 2 | `74462d33c6db`  |
| 3158   | Layout 2 | `74462d33c6db`  |
| 3151   | Layout 2 | `74462d33c6db`  |
| 3144   | Layout 2 | `74462d33c6db`  |
| 3133   | Layout 2 | `74462d33c6db`  |
| 3125   | Layout 2 | `74462d33c6db`  |
| 3118   | Layout 2 | `74462d33c6db`  |
| 3111   | Layout 2 | `74462d33c6db`  |
| 3103   | Layout 2 | `74462d33c6db`  |
| 3095   | Layout 2 | `74462d33c6db`  |
| 3086   | Layout 2 | `74462d33c6db`  |
| 3072   | Layout 2 | `74462d33c6db`  |
| 3062   | Layout 2 | `74462d33c6db`  |
| 3052   | Layout 2 | `74462d33c6db`  |
| 3045   | Layout 2 | `74462d33c6db`  |
| 3037   | Layout 2 | `74462d33c6db`  |
| 3030   | Layout 2 | `74462d33c6db`  |
| 3021   | Layout 2 | `74462d33c6db`  |
| 3012   | Layout 2 | `74462d33c6db`  |
| 3002   | Layout 2 | `74462d33c6db`  |
| 2995   | Layout 2 | `74462d33c6db`  |
| 2987   | Layout 2 | `74462d33c6db`  |
| 2978   | Layout 2 | `74462d33c6db`  |
| 2970   | Layout 2 | `74462d33c6db`  |
| 2959   | Layout 2 | `74462d33c6db`  |
| 2951   | Layout 2 | `74462d33c6db`  |
| 2942   | Layout 2 | `74462d33c6db`  |
| 2935   | Layout 2 | `74462d33c6db`  |
| 2932   | Layout 2 | `74462d33c6db`  |
| 2923   | Layout 2 | `74462d33c6db`  |
| 2919   | Layout 2 | `74462d33c6db`  |
| 2907   | Layout 2 | `74462d33c6db`  |
| 2900   | Layout 2 | `74462d33c6db`  |
| 2891   | Layout 2 | `74462d33c6db`  |
| 2882   | Layout 2 | `74462d33c6db`  |
| 2872   | Layout 2 | `74462d33c6db`  |
| 2863   | Layout 2 | `74462d33c6db`  |
| 2855   | Layout 2 | `74462d33c6db`  |
| 2849   | Layout 2 | `74462d33c6db`  |
| 2844   | Layout 2 | `74462d33c6db`  |
| 2834   | Layout 2 | `74462d33c6db`  |
| 2825   | Layout 2 | `74462d33c6db`  |
| 2819   | Layout 2 | `74462d33c6db`  |
| 2811   | Layout 2 | `74462d33c6db`  |
| 2803   | Layout 2 | `74462d33c6db`  |
| 2794   | Layout 2 | `74462d33c6db`  |
| 2783   | Layout 2 | `74462d33c6db`  |
| 2774   | Layout 2 | `74462d33c6db`  |
| 2765   | Layout 2 | `74462d33c6db`  |
| 2756   | Layout 2 | `74462d33c6db`  |
| 2750   | Layout 2 | `74462d33c6db`  |
| 2743   | Layout 2 | `74462d33c6db`  |
| 2736   | Layout 2 | `74462d33c6db`  |
| 2726   | Layout 2 | `74462d33c6db`  |
| 2717   | Layout 2 | `74462d33c6db`  |
| 2709   | Layout 2 | `74462d33c6db`  |
| 2703   | Layout 2 | `74462d33c6db`  |
| 2695   | Layout 2 | `74462d33c6db`  |
| 2684   | Layout 2 | `74462d33c6db`  |
| 2672   | Layout 2 | `74462d33c6db`  |
| 2665   | Layout 2 | `74462d33c6db`  |
| 2657   | Layout 2 | `74462d33c6db`  |
| 2649   | Layout 2 | `74462d33c6db`  |
| 2644   | Layout 2 | `74462d33c6db`  |
| 2637   | Layout 2 | `74462d33c6db`  |
| 2629   | Layout 2 | `74462d33c6db`  |
| 2619   | Layout 2 | `74462d33c6db`  |
| 2612   | Layout 2 | `74462d33c6db`  |
| 2606   | Layout 2 | `74462d33c6db`  |
| 2602   | Layout 2 | `74462d33c6db`  |
| 2601   | Layout 2 | `74462d33c6db`  |
| 2592   | Layout 2 | `74462d33c6db`  |
| 2583   | Layout 2 | `74462d33c6db`  |
| 2575   | Layout 2 | `74462d33c6db`  |
| 2567   | Layout 2 | `74462d33c6db`  |
| 2560   | Layout 2 | `74462d33c6db`  |
| 2553   | Layout 2 | `74462d33c6db`  |
| 2545   | Layout 2 | `74462d33c6db`  |
| 2538   | Layout 2 | `74462d33c6db`  |
| 2529   | Layout 2 | `74462d33c6db`  |
| 2519   | Layout 2 | `74462d33c6db`  |
| 2513   | Layout 2 | `74462d33c6db`  |
| 2510   | Layout 2 | `74462d33c6db`  |
| 2507   | Layout 2 | `74462d33c6db`  |
| 2503   | Layout 2 | `74462d33c6db`  |
| 2498   | Layout 2 | `74462d33c6db`  |
| 2492   | Layout 2 | `74462d33c6db`  |
| 2487   | Layout 2 | `74462d33c6db`  |
| 2480   | Layout 2 | `74462d33c6db`  |
| 2474   | Layout 2 | `74462d33c6db`  |
| 2468   | Layout 2 | `74462d33c6db`  |
| 2460   | Layout 2 | `74462d33c6db`  |
| 2453   | Layout 2 | `74462d33c6db`  |
| 2444   | Layout 2 | `74462d33c6db`  |
| 2438   | Layout 2 | `74462d33c6db`  |
| 2434   | Layout 2 | `74462d33c6db`  |
| 2429   | Layout 2 | `74462d33c6db`  |
| 2421   | Layout 2 | `74462d33c6db`  |
| 2414   | Layout 2 | `74462d33c6db`  |
| 2407   | Layout 2 | `74462d33c6db`  |
| 2401   | Layout 2 | `74462d33c6db`  |
| 2397   | Layout 2 | `74462d33c6db`  |
| 2393   | Layout 2 | `74462d33c6db`  |
| 2384   | Layout 2 | `74462d33c6db`  |
| 2378   | Layout 2 | `74462d33c6db`  |
| 2372   | Layout 2 | `74462d33c6db`  |
| 2358   | Layout 2 | `74462d33c6db`  |
| 2352   | Layout 2 | `74462d33c6db`  |
| 2347   | Layout 2 | `74462d33c6db`  |
| 2343   | Layout 2 | `74462d33c6db`  |
| 2335   | Layout 2 | `74462d33c6db`  |
| 2327   | Layout 2 | `74462d33c6db`  |
| 2324   | Layout 2 | `74462d33c6db`  |
| 2319   | Layout 2 | `74462d33c6db`  |
| 2313   | Layout 2 | `74462d33c6db`  |
| 2308   | Layout 2 | `74462d33c6db`  |
| 2302   | Layout 2 | `74462d33c6db`  |
| 2295   | Layout 2 | `74462d33c6db`  |
| 2290   | Layout 2 | `74462d33c6db`  |
| 2284   | Layout 2 | `74462d33c6db`  |
| 2276   | Layout 2 | `74462d33c6db`  |
| 2269   | Layout 2 | `74462d33c6db`  |
| 2259   | Layout 2 | `74462d33c6db`  |
| 2250   | Layout 2 | `74462d33c6db`  |
| 2243   | Layout 2 | `74462d33c6db`  |
| 2235   | Layout 2 | `74462d33c6db`  |
| 2229   | Layout 2 | `74462d33c6db`  |
| 2224   | Layout 2 | `74462d33c6db`  |
| 2218   | Layout 2 | `74462d33c6db`  |
| 2215   | Layout 2 | `74462d33c6db`  |
| 2207   | Layout 2 | `74462d33c6db`  |
| 2203   | Layout 2 | `74462d33c6db`  |
| 2196   | Layout 2 | `74462d33c6db`  |
| 2192   | Layout 2 | `74462d33c6db`  |
| 2189   | Layout 2 | `74462d33c6db`  |
| 2183   | Layout 2 | `74462d33c6db`  |
| 2179   | Layout 2 | `74462d33c6db`  |
| 2171   | Layout 2 | `74462d33c6db`  |
| 2163   | Layout 2 | `74462d33c6db`  |
| 2156   | Layout 2 | `74462d33c6db`  |
| 2151   | Layout 2 | `74462d33c6db`  |
| 2147   | Layout 2 | `74462d33c6db`  |
| 2142   | Layout 2 | `74462d33c6db`  |
| 2138   | Layout 2 | `74462d33c6db`  |
| 2134   | Layout 2 | `74462d33c6db`  |
| 2130   | Layout 2 | `74462d33c6db`  |
| 2122   | Layout 2 | `74462d33c6db`  |
| 2107   | Layout 2 | `74462d33c6db`  |
| 2098   | Layout 2 | `74462d33c6db`  |
| 2089   | Layout 2 | `74462d33c6db`  |
| 2081   | Layout 2 | `74462d33c6db`  |
| 2073   | Layout 2 | `74462d33c6db`  |
| 2067   | Layout 2 | `74462d33c6db`  |
| 2063   | Layout 2 | `74462d33c6db`  |
| 2059   | Layout 2 | `74462d33c6db`  |
| 2052   | Layout 2 | `74462d33c6db`  |
| 2044   | Layout 2 | `74462d33c6db`  |
| 2039   | Layout 2 | `74462d33c6db`  |
| 2032   | Layout 2 | `74462d33c6db`  |
| 2025   | Layout 2 | `74462d33c6db`  |
| 2011   | Layout 2 | `74462d33c6db`  |
| 2005   | Layout 2 | `74462d33c6db`  |
| 2000   | Layout 2 | `74462d33c6db`  |
| 1996   | Layout 2 | `74462d33c6db`  |
| 1991   | Layout 2 | `74462d33c6db`  |
| 1985   | Layout 2 | `74462d33c6db`  |
| 1980   | Layout 2 | `74462d33c6db`  |
| 1969   | Layout 2 | `74462d33c6db`  |
| 1964   | Layout 2 | `74462d33c6db`  |
| 1958   | Layout 2 | `74462d33c6db`  |
| 1950   | Layout 2 | `74462d33c6db`  |
| 1945   | Layout 2 | `74462d33c6db`  |
| 1937   | Layout 2 | `74462d33c6db`  |
| 1933   | Layout 2 | `74462d33c6db`  |
| 1927   | Layout 2 | `74462d33c6db`  |
| 1921   | Layout 2 | `74462d33c6db`  |
| 1914   | Layout 2 | `74462d33c6db`  |
| 1908   | Layout 2 | `74462d33c6db`  |
| 1897   | Layout 2 | `74462d33c6db`  |
| 1892   | Layout 2 | `74462d33c6db`  |
| 1886   | Layout 2 | `74462d33c6db`  |
| 1881   | Layout 2 | `74462d33c6db`  |
| 1871   | Layout 2 | `74462d33c6db`  |
| 1866   | Layout 2 | `74462d33c6db`  |
| 1862   | Layout 2 | `74462d33c6db`  |
| 1854   | Layout 2 | `74462d33c6db`  |
| 1846   | Layout 2 | `74462d33c6db`  |
| 1838   | Layout 2 | `74462d33c6db`  |
| 1832   | Layout 2 | `74462d33c6db`  |
| 1826   | Layout 2 | `74462d33c6db`  |
| 1822   | Layout 2 | `74462d33c6db`  |
| 1818   | Layout 2 | `74462d33c6db`  |
| 1804   | Layout 2 | `74462d33c6db`  |
| 1794   | Layout 2 | `74462d33c6db`  |
| 1790   | Layout 2 | `74462d33c6db`  |
| 1784   | Layout 2 | `74462d33c6db`  |
| 1774   | Layout 2 | `74462d33c6db`  |
| 1771   | Layout 2 | `74462d33c6db`  |
| 1762   | Layout 2 | `74462d33c6db`  |
| 1759   | Layout 2 | `74462d33c6db`  |
| 1754   | Layout 2 | `74462d33c6db`  |
| 1749   | Layout 2 | `74462d33c6db`  |
| 1743   | Layout 2 | `74462d33c6db`  |
| 1737   | Layout 2 | `74462d33c6db`  |
| 1731   | Layout 2 | `74462d33c6db`  |
| 1725   | Layout 2 | `74462d33c6db`  |
| 1717   | Layout 2 | `74462d33c6db`  |
| 1710   | Layout 2 | `74462d33c6db`  |
| 1704   | Layout 2 | `74462d33c6db`  |
| 1698   | Layout 2 | `74462d33c6db`  |
| 1690   | Layout 2 | `74462d33c6db`  |
| 1685   | Layout 2 | `74462d33c6db`  |
| 1680   | Layout 2 | `74462d33c6db`  |
| 1674   | Layout 2 | `74462d33c6db`  |
| 1668   | Layout 2 | `74462d33c6db`  |
| 1659   | Layout 2 | `74462d33c6db`  |
| 1649   | Layout 2 | `74462d33c6db`  |
| 1642   | Layout 2 | `74462d33c6db`  |
| 1636   | Layout 2 | `74462d33c6db`  |
| 1628   | Layout 2 | `74462d33c6db`  |
| 1622   | Layout 2 | `74462d33c6db`  |
| 1614   | Layout 2 | `74462d33c6db`  |
| 1608   | Layout 2 | `74462d33c6db`  |
| 1602   | Layout 2 | `74462d33c6db`  |
| 1598   | Layout 2 | `74462d33c6db`  |
| 1594   | Layout 2 | `74462d33c6db`  |
| 1590   | Layout 2 | `74462d33c6db`  |
| 1587   | Layout 2 | `74462d33c6db`  |
| 1584   | Layout 2 | `74462d33c6db`  |
| 1579   | Layout 2 | `74462d33c6db`  |
| 1572   | Layout 2 | `74462d33c6db`  |
| 1565   | Layout 2 | `74462d33c6db`  |
| 1559   | Layout 2 | `74462d33c6db`  |
| 1554   | Layout 2 | `74462d33c6db`  |
| 1547   | Layout 2 | `74462d33c6db`  |
| 1537   | Layout 2 | `74462d33c6db`  |
| 1529   | Layout 2 | `74462d33c6db`  |
| 1524   | Layout 2 | `74462d33c6db`  |
| 1519   | Layout 2 | `74462d33c6db`  |
| 1509   | Layout 2 | `74462d33c6db`  |
| 1506   | Layout 2 | `74462d33c6db`  |
| 1504   | Layout 2 | `74462d33c6db`  |
| 1500   | Layout 2 | `74462d33c6db`  |
| 1493   | Layout 2 | `74462d33c6db`  |
| 1489   | Layout 2 | `74462d33c6db`  |
| 1485   | Layout 2 | `74462d33c6db`  |
| 1481   | Layout 2 | `74462d33c6db`  |
| 1474   | Layout 2 | `74462d33c6db`  |
| 1466   | Layout 2 | `74462d33c6db`  |
| 1462   | Layout 2 | `74462d33c6db`  |
| 1459   | Layout 2 | `74462d33c6db`  |
| 1453   | Layout 2 | `74462d33c6db`  |
| 1450   | Layout 2 | `74462d33c6db`  |
| 1445   | Layout 2 | `74462d33c6db`  |
| 1439   | Layout 2 | `74462d33c6db`  |
| 1433   | Layout 2 | `74462d33c6db`  |
| 1430   | Layout 2 | `74462d33c6db`  |
| 1426   | Layout 2 | `74462d33c6db`  |
| 1421   | Layout 2 | `74462d33c6db`  |
| 1417   | Layout 2 | `74462d33c6db`  |
| 1416   | Layout 2 | `74462d33c6db`  |
| 1409   | Layout 2 | `74462d33c6db`  |
| 1405   | Layout 2 | `74462d33c6db`  |
| 1401   | Layout 2 | `74462d33c6db`  |
| 1396   | Layout 2 | `74462d33c6db`  |
| 1391   | Layout 2 | `74462d33c6db`  |
| 1390   | Layout 2 | `74462d33c6db`  |
| 1386   | Layout 2 | `74462d33c6db`  |
| 1381   | Layout 2 | `74462d33c6db`  |
| 1379   | Layout 2 | `74462d33c6db`  |
| 1372   | Layout 2 | `74462d33c6db`  |
| 1366   | Layout 2 | `74462d33c6db`  |
| 1364   | Layout 2 | `74462d33c6db`  |
| 1363   | Layout 2 | `74462d33c6db`  |
| 1360   | Layout 2 | `74462d33c6db`  |
| 1358   | Layout 2 | `74462d33c6db`  |
| 1355   | Layout 2 | `74462d33c6db`  |
| 1351   | Layout 2 | `74462d33c6db`  |
| 1348   | Layout 2 | `74462d33c6db`  |
| 1346   | Layout 2 | `74462d33c6db`  |
| 1341   | Layout 2 | `74462d33c6db`  |
| 1340   | Layout 2 | `74462d33c6db`  |
| 1338   | Layout 2 | `74462d33c6db`  |
| 1335   | Layout 2 | `74462d33c6db`  |
| 1333   | Layout 2 | `74462d33c6db`  |
| 1329   | Layout 2 | `74462d33c6db`  |
| 1327   | Layout 2 | `74462d33c6db`  |
| 1324   | Layout 2 | `74462d33c6db`  |
| 1321   | Layout 2 | `74462d33c6db`  |
| 1319   | Layout 2 | `74462d33c6db`  |
| 1318   | Layout 1 | `74462d33c6db`  |
| 1316   | Layout 1 | `74462d33c6db`  |
| 1313   | Layout 1 | `74462d33c6db`  |
| 1311   | Layout 1 | `74462d33c6db`  |
| 1309   | Layout 1 | `74462d33c6db`  |
| 1304   | Layout 1 | `74462d33c6db`  |
| 1292   | Layout 1 | `74462d33c6db`  |
| 1286   | Layout 1 | `74462d33c6db`  |
| 1280   | Layout 1 | `74462d33c6db`  |
| 1276   | Layout 1 | `74462d33c6db`  |
| 1267   | Layout 1 | `74462d33c6db`  |
| 1261   | Layout 1 | `74462d33c6db`  |
| 1256   | Layout 1 | `74462d33c6db`  |
| 1250   | Layout 1 | `74462d33c6db`  |
| 1246   | Layout 1 | `74462d33c6db`  |
| 1239   | Layout 1 | `74462d33c6db`  |
| 1230   | Layout 1 | `74462d33c6db`  |
| 1226   | Layout 1 | `74462d33c6db`  |
| 1220   | Layout 1 | `74462d33c6db`  |
| 1217   | Layout 1 | `74462d33c6db`  |
| 1211   | Layout 1 | `74462d33c6db`  |
| 1210   | Layout 1 | `74462d33c6db`  |
| 1208   | Layout 1 | `74462d33c6db`  |
| 1203   | Layout 1 | `74462d33c6db`  |
| 1197   | Layout 1 | `74462d33c6db`  |
| 1194   | Layout 1 | `74462d33c6db`  |
| 1192   | Layout 1 | `74462d33c6db`  |
| 1187   | Layout 1 | `74462d33c6db`  |
| 1183   | Layout 1 | `74462d33c6db`  |
| 1177   | Layout 1 | `74462d33c6db`  |
| 1173   | Layout 1 | `74462d33c6db`  |
| 1167   | Layout 1 | `74462d33c6db`  |
| 1164   | Layout 1 | `74462d33c6db`  |
| 1156   | Layout 1 | `74462d33c6db`  |
| 1149   | Layout 1 | `74462d33c6db`  |
| 1144   | Layout 1 | `74462d33c6db`  |
| 1137   | Layout 1 | `74462d33c6db`  |
| 1132   | Layout 1 | `74462d33c6db`  |
| 1127   | Layout 1 | `74462d33c6db`  |
| 1122   | Layout 1 | `74462d33c6db`  |
| 1118   | Layout 1 | `74462d33c6db`  |
| 1114   | Layout 1 | `74462d33c6db`  |
| 1109   | Layout 1 | `74462d33c6db`  |
| 1102   | No file  | `74462d33c6db`  |
| 1096   | No file  | `74462d33c6db`  |
| 1088   | No file  | `74462d33c6db`  |
| 1081   | No file  | `74462d33c6db`  |
| 1076   | No file  | `74462d33c6db`  |
| 1069   | No file  | `74462d33c6db`  |
| 1064   | No file  | `74462d33c6db`  |
| 1058   | No file  | `74462d33c6db`  |
| 1051   | No file  | `74462d33c6db`  |
| 1044   | No file  | `74462d33c6db`  |
| 1036   | No file  | `74462d33c6db`  |
| 1026   | No file  | `74462d33c6db`  |
| 1016   | No file  | `74462d33c6db`  |
| 1009   | No file  | `74462d33c6db`  |
| 1005   | No file  | `74462d33c6db`  |
| 1000   | No file  | `74462d33c6db`  |
| 998    | No file  | `74462d33c6db`  |
| 990    | No file  | `74462d33c6db`  |
| 979    | No file  | `74462d33c6db`  |
| 972    | No file  | `74462d33c6db`  |
| 963    | No file  | `74462d33c6db`  |
| 955    | No file  | `74462d33c6db`  |
| 946    | No file  | `74462d33c6db`  |
| 938    | No file  | `74462d33c6db`  |
| 927    | No file  | `74462d33c6db`  |
| 911    | No file  | `74462d33c6db`  |
| 904    | No file  | `74462d33c6db`  |
| 899    | No file  | `74462d33c6db`  |
| 894    | No file  | `74462d33c6db`  |
| 885    | No file  | `74462d33c6db`  |
| 879    | No file  | `74462d33c6db`  |
| 872    | No file  | `74462d33c6db`  |
| 864    | No file  | `74462d33c6db`  |
| 855    | No file  | `74462d33c6db`  |
| 853    | No file  | `74462d33c6db`  |
| 845    | No file  | `74462d33c6db`  |
| 837    | No file  | `74462d33c6db`  |
| 829    | No file  | `74462d33c6db`  |
| 822    | No file  | `74462d33c6db`  |
| 814    | No file  | `74462d33c6db`  |
| 805    | No file  | `74462d33c6db`  |
| 794    | No file  | `74462d33c6db`  |
| 787    | No file  | `74462d33c6db`  |
| 780    | No file  | `74462d33c6db`  |
| 771    | No file  | `74462d33c6db`  |
| 760    | No file  | `74462d33c6db`  |
| 748    | No file  | `74462d33c6db`  |
| 741    | No file  | `74462d33c6db`  |
| 736    | No file  | `74462d33c6db`  |
| 731    | No file  | `74462d33c6db`  |
| 723    | No file  | `74462d33c6db`  |
| 711    | No file  | `74462d33c6db`  |
| 707    | No file  | `74462d33c6db`  |
| 697    | No file  | `74462d33c6db`  |
| 689    | No file  | `74462d33c6db`  |
| 683    | No file  | `74462d33c6db`  |
| 678    | No file  | `74462d33c6db`  |
| 670    | No file  | `74462d33c6db`  |
| 661    | No file  | `74462d33c6db`  |
| 656    | No file  | `74462d33c6db`  |
| 652    | No file  | `74462d33c6db`  |
| 643    | No file  | `74462d33c6db`  |
| 637    | No file  | `74462d33c6db`  |
| 630    | No file  | `74462d33c6db`  |
| 627    | No file  | `74462d33c6db`  |
| 621    | No file  | `74462d33c6db`  |
| 617    | No file  | `74462d33c6db`  |
| 615    | No file  | `74462d33c6db`  |
| 606    | No file  | `74462d33c6db`  |
| 599    | No file  | `74462d33c6db`  |
| 592    | No file  | `74462d33c6db`  |
| 586    | No file  | `74462d33c6db`  |
| 577    | No file  | `74462d33c6db`  |
| 569    | No file  | `74462d33c6db`  |
| 561    | No file  | `74462d33c6db`  |
| 554    | No file  | `74462d33c6db`  |
| 542    | No file  | `74462d33c6db`  |
| 532    | No file  | `74462d33c6db`  |
| 531    | No file  | `74462d33c6db`  |
| 526    | No file  | `74462d33c6db`  |
| 521    | No file  | `74462d33c6db`  |
| 517    | No file  | `74462d33c6db`  |
| 510    | No file  | `74462d33c6db`  |
| 508    | No file  | `74462d33c6db`  |
| 504    | No file  | `74462d33c6db`  |
| 497    | No file  | `74462d33c6db`  |
| 491    | No file  | `74462d33c6db`  |
| 485    | No file  | `74462d33c6db`  |
| 478    | No file  | `74462d33c6db`  |
| 472    | No file  | `74462d33c6db`  |
| 466    | No file  | `74462d33c6db`  |
| 457    | No file  | `74462d33c6db`  |
| 452    | No file  | `74462d33c6db`  |
| 449    | No file  | `74462d33c6db`  |
| 435    | No file  | `74462d33c6db`  |

<!-- versions:end -->

## Companion Files

None. The handler names each item with LOC type 0 from
`languagedata_*.loc` when it is loaded, else with the Korean name of the
`ITEM_NAME_KR` lookup index (built from `itemenchant.dbss`), and draws its
icon from the item icon index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of items                               |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (12 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | item_key      | Item ID; no key above `0xFFFFFF`, so no enhancement level is packed in |
| `+0x04` | u32  | item_name_ref | String table index of the item's Korean name                          |
| `+0x08` | u32  | unknown_08    | `0` on every row (clients 1784 and 3483)                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                        |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE Korean item names, each distinct name once      |

## Layout 1

Rows of 8 bytes, without `unknown_08`. The File Layout and the String Table
are the same as in Layout 2.

### Row (8 bytes)

| Offset  | Type | Field         | Notes                                        |
| ------- | ---- | ------------- | -------------------------------------------- |
| `+0x00` | u32  | item_key      | Item ID                                      |
| `+0x04` | u32  | item_name_ref | String table index of the item's Korean name |

## Rows and Strings

Counted on client 3483 and on client 1784:

| Client | Rows   | Strings | Strings shared by several rows |
| ------ | ------ | ------- | ------------------------------ |
| 3483   | 12,842 | 12,669  | 158 strings, 331 rows          |
| 1784   | 9,000  | 8,776   | 156 strings, 380 rows          |

Every key appears once. The string table holds each distinct name once:
items with the same Korean name (the class variants of one costume piece,
for example) point at the same string. The strings are in the order of
their first use, so the first row that uses a name holds the next index.
Every string has `is_wide` `1` on both clients. The rows are not in key
order.

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 is named
after this file; the rows are a selection of its `Item_Table`. `item_key`
is the `Item_Table` `Index` of the row's item: the official client 1784
file's 9,000 keys are all in that sheet. `item_name_ref` points at the
item's `ItemName`; the live client check above (12,842 of 12,842 against
`itemenchant.dbss`, client 3483) confirms it without the sheet.

## Notes

- Every key of the official client 1784 file has `isDisplayWorldMarket`
  `1` in the `Item_Table` of a private server's `DataSheets.bexcel` on
  client 1784 (9,000 of 9,000). The flag does not decide the list alone:
  1,491 items of that sheet with the flag are missing from the file, 922 of
  them `ItemClassify` `9` (Pearl Shop goods). See Open Questions.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/item_tables.py`: the item
  ID, its icon and its name. The Korean name of the row stays on the record
  as `item_name_kr` for search and export.

## Open Questions

### Which Items the List Holds

Every item of the official client 1784 file has `isDisplayWorldMarket` `1`
in the client 1784 `Item_Table`, but 1,491 items with the flag are not in
the file. The sheet is a private server's, built later than the official
1784 client, so part of the gap can be items the official build did not
have yet; the rest (922 Pearl Shop goods, `ItemClassify` `9`) needs a
second condition. The tool that builds the file is not in any source I
have; the live client's `ToClient_searchWorldMarketItem` code could show
whether the client filters the list further.

### What `unknown_08` Holds

`unknown_08` is `0` on all 12,842 rows of client 3483 and on all 9,000 rows
of client 1784. It came with Layout 2: Layout 1 rows end after
`item_name_ref`. It can be a field that no item fills yet, or
`item_name_ref` widened to a u64. The loader in a private server's server
executable on client 1784 (`ItemEnchantStaticStatusManager::readFromBinary`,
error text `marketSearchList()`) would show which width it reads.
