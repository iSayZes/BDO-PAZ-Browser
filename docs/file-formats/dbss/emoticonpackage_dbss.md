# `emoticonpackage.dbss` Format

## Purpose

The emoticon packages: one row per package with a Korean name and the
[`emoticon.dbss`](emoticon_dbss.md) keys it unlocks. On client 3482, 38 of
the 47 packages hold one emoticon; package `1` holds the item link and
emoticons `2` to `5`. No Lua call names this table; the chat window lists
the unlocked emoticons through `ToClient_getEmoticonInfoList()` and shows
an expiry date from `ToClient_getEmoticonExpirationDate()`. Companion
`emoticonpackageoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records              | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | -------------------- | --------- |
| 1      | 1280 and later | `emoticonpackage.dbss`       | 2,186 | 120 Emoticon, 47 Row | 8         |
| 1      | 1280 and later | `emoticonpackageoffset.dbss` | 756   | 47 Offset Row        | 16        |

| Layout | File                         | Known           | Unknown       |
| ------ | ---------------------------- | --------------- | ------------- |
| 1      | `emoticonpackage.dbss`       | 1,518 B (69.4%) | 668 B (30.6%) |
| 1      | `emoticonpackageoffset.dbss` | 568 B (75.1%)   | 188 B (24.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `40e6326e69e3`  |
| 3482   | Layout 1 | `40e6326e69e3`  |
| 3474   | Layout 1 | `40e6326e69e3`  |
| 3473   | Layout 1 | `40e6326e69e3`  |
| 3464   | Layout 1 | `40e6326e69e3`  |
| 3458   | Layout 1 | `40e6326e69e3`  |
| 3454   | Layout 1 | `40e6326e69e3`  |
| 3444   | Layout 1 | `40e6326e69e3`  |
| 3435   | Layout 1 | `40e6326e69e3`  |
| 3426   | Layout 1 | `40e6326e69e3`  |
| 3418   | Layout 1 | `40e6326e69e3`  |
| 3412   | Layout 1 | `40e6326e69e3`  |
| 3402   | Layout 1 | `40e6326e69e3`  |
| 3396   | Layout 1 | `40e6326e69e3`  |
| 3387   | Layout 1 | `40e6326e69e3`  |
| 3381   | Layout 1 | `40e6326e69e3`  |
| 3373   | Layout 1 | `40e6326e69e3`  |
| 3364   | Layout 1 | `40e6326e69e3`  |
| 3356   | Layout 1 | `40e6326e69e3`  |
| 3349   | Layout 1 | `40e6326e69e3`  |
| 3342   | Layout 1 | `40e6326e69e3`  |
| 3335   | Layout 1 | `40e6326e69e3`  |
| 3326   | Layout 1 | `40e6326e69e3`  |
| 3321   | Layout 1 | `40e6326e69e3`  |
| 3314   | Layout 1 | `40e6326e69e3`  |
| 3303   | Layout 1 | `40e6326e69e3`  |
| 3302   | Layout 1 | `40e6326e69e3`  |
| 3293   | Layout 1 | `40e6326e69e3`  |
| 3283   | Layout 1 | `40e6326e69e3`  |
| 3275   | Layout 1 | `40e6326e69e3`  |
| 3267   | Layout 1 | `40e6326e69e3`  |
| 3258   | Layout 1 | `40e6326e69e3`  |
| 3251   | Layout 1 | `40e6326e69e3`  |
| 3242   | Layout 1 | `40e6326e69e3`  |
| 3235   | Layout 1 | `40e6326e69e3`  |
| 3229   | Layout 1 | `40e6326e69e3`  |
| 3212   | Layout 1 | `40e6326e69e3`  |
| 3203   | Layout 1 | `40e6326e69e3`  |
| 3193   | Layout 1 | `40e6326e69e3`  |
| 3186   | Layout 1 | `40e6326e69e3`  |
| 3177   | Layout 1 | `40e6326e69e3`  |
| 3169   | Layout 1 | `40e6326e69e3`  |
| 3158   | Layout 1 | `40e6326e69e3`  |
| 3151   | Layout 1 | `40e6326e69e3`  |
| 3144   | Layout 1 | `40e6326e69e3`  |
| 3133   | Layout 1 | `40e6326e69e3`  |
| 3125   | Layout 1 | `40e6326e69e3`  |
| 3118   | Layout 1 | `40e6326e69e3`  |
| 3111   | Layout 1 | `40e6326e69e3`  |
| 3103   | Layout 1 | `40e6326e69e3`  |
| 3095   | Layout 1 | `40e6326e69e3`  |
| 3086   | Layout 1 | `40e6326e69e3`  |
| 3072   | Layout 1 | `40e6326e69e3`  |
| 3062   | Layout 1 | `40e6326e69e3`  |
| 3052   | Layout 1 | `40e6326e69e3`  |
| 3045   | Layout 1 | `40e6326e69e3`  |
| 3037   | Layout 1 | `40e6326e69e3`  |
| 3030   | Layout 1 | `40e6326e69e3`  |
| 3021   | Layout 1 | `40e6326e69e3`  |
| 3012   | Layout 1 | `40e6326e69e3`  |
| 3002   | Layout 1 | `40e6326e69e3`  |
| 2995   | Layout 1 | `40e6326e69e3`  |
| 2987   | Layout 1 | `40e6326e69e3`  |
| 2978   | Layout 1 | `40e6326e69e3`  |
| 2970   | Layout 1 | `40e6326e69e3`  |
| 2959   | Layout 1 | `40e6326e69e3`  |
| 2951   | Layout 1 | `40e6326e69e3`  |
| 2942   | Layout 1 | `40e6326e69e3`  |
| 2935   | Layout 1 | `40e6326e69e3`  |
| 2932   | Layout 1 | `40e6326e69e3`  |
| 2923   | Layout 1 | `40e6326e69e3`  |
| 2919   | Layout 1 | `40e6326e69e3`  |
| 2907   | Layout 1 | `40e6326e69e3`  |
| 2900   | Layout 1 | `40e6326e69e3`  |
| 2891   | Layout 1 | `40e6326e69e3`  |
| 2882   | Layout 1 | `40e6326e69e3`  |
| 2872   | Layout 1 | `40e6326e69e3`  |
| 2863   | Layout 1 | `40e6326e69e3`  |
| 2855   | Layout 1 | `40e6326e69e3`  |
| 2849   | Layout 1 | `40e6326e69e3`  |
| 2844   | Layout 1 | `40e6326e69e3`  |
| 2834   | Layout 1 | `40e6326e69e3`  |
| 2825   | Layout 1 | `40e6326e69e3`  |
| 2819   | Layout 1 | `40e6326e69e3`  |
| 2811   | Layout 1 | `40e6326e69e3`  |
| 2803   | Layout 1 | `40e6326e69e3`  |
| 2794   | Layout 1 | `40e6326e69e3`  |
| 2783   | Layout 1 | `40e6326e69e3`  |
| 2774   | Layout 1 | `40e6326e69e3`  |
| 2765   | Layout 1 | `40e6326e69e3`  |
| 2756   | Layout 1 | `40e6326e69e3`  |
| 2750   | Layout 1 | `40e6326e69e3`  |
| 2743   | Layout 1 | `40e6326e69e3`  |
| 2736   | Layout 1 | `40e6326e69e3`  |
| 2726   | Layout 1 | `40e6326e69e3`  |
| 2717   | Layout 1 | `40e6326e69e3`  |
| 2709   | Layout 1 | `40e6326e69e3`  |
| 2703   | Layout 1 | `40e6326e69e3`  |
| 2695   | Layout 1 | `40e6326e69e3`  |
| 2684   | Layout 1 | `40e6326e69e3`  |
| 2672   | Layout 1 | `40e6326e69e3`  |
| 2665   | Layout 1 | `40e6326e69e3`  |
| 2657   | Layout 1 | `40e6326e69e3`  |
| 2649   | Layout 1 | `40e6326e69e3`  |
| 2644   | Layout 1 | `40e6326e69e3`  |
| 2637   | Layout 1 | `40e6326e69e3`  |
| 2629   | Layout 1 | `40e6326e69e3`  |
| 2619   | Layout 1 | `40e6326e69e3`  |
| 2612   | Layout 1 | `40e6326e69e3`  |
| 2606   | Layout 1 | `40e6326e69e3`  |
| 2602   | Layout 1 | `40e6326e69e3`  |
| 2601   | Layout 1 | `40e6326e69e3`  |
| 2592   | Layout 1 | `40e6326e69e3`  |
| 2583   | Layout 1 | `40e6326e69e3`  |
| 2575   | Layout 1 | `40e6326e69e3`  |
| 2567   | Layout 1 | `40e6326e69e3`  |
| 2560   | Layout 1 | `40e6326e69e3`  |
| 2553   | Layout 1 | `40e6326e69e3`  |
| 2545   | Layout 1 | `40e6326e69e3`  |
| 2538   | Layout 1 | `40e6326e69e3`  |
| 2529   | Layout 1 | `40e6326e69e3`  |
| 2519   | Layout 1 | `40e6326e69e3`  |
| 2513   | Layout 1 | `40e6326e69e3`  |
| 2510   | Layout 1 | `40e6326e69e3`  |
| 2507   | Layout 1 | `40e6326e69e3`  |
| 2503   | Layout 1 | `40e6326e69e3`  |
| 2498   | Layout 1 | `40e6326e69e3`  |
| 2492   | Layout 1 | `40e6326e69e3`  |
| 2487   | Layout 1 | `40e6326e69e3`  |
| 2480   | Layout 1 | `40e6326e69e3`  |
| 2474   | Layout 1 | `40e6326e69e3`  |
| 2468   | Layout 1 | `40e6326e69e3`  |
| 2460   | Layout 1 | `40e6326e69e3`  |
| 2453   | Layout 1 | `40e6326e69e3`  |
| 2444   | Layout 1 | `40e6326e69e3`  |
| 2438   | Layout 1 | `40e6326e69e3`  |
| 2434   | Layout 1 | `40e6326e69e3`  |
| 2429   | Layout 1 | `40e6326e69e3`  |
| 2421   | Layout 1 | `40e6326e69e3`  |
| 2414   | Layout 1 | `40e6326e69e3`  |
| 2407   | Layout 1 | `40e6326e69e3`  |
| 2401   | Layout 1 | `40e6326e69e3`  |
| 2397   | Layout 1 | `40e6326e69e3`  |
| 2393   | Layout 1 | `40e6326e69e3`  |
| 2384   | Layout 1 | `40e6326e69e3`  |
| 2378   | Layout 1 | `40e6326e69e3`  |
| 2372   | Layout 1 | `40e6326e69e3`  |
| 2358   | Layout 1 | `40e6326e69e3`  |
| 2352   | Layout 1 | `40e6326e69e3`  |
| 2347   | Layout 1 | `40e6326e69e3`  |
| 2343   | Layout 1 | `40e6326e69e3`  |
| 2335   | Layout 1 | `40e6326e69e3`  |
| 2327   | Layout 1 | `40e6326e69e3`  |
| 2324   | Layout 1 | `40e6326e69e3`  |
| 2319   | Layout 1 | `40e6326e69e3`  |
| 2313   | Layout 1 | `40e6326e69e3`  |
| 2308   | Layout 1 | `40e6326e69e3`  |
| 2302   | Layout 1 | `40e6326e69e3`  |
| 2295   | Layout 1 | `40e6326e69e3`  |
| 2290   | Layout 1 | `40e6326e69e3`  |
| 2284   | Layout 1 | `40e6326e69e3`  |
| 2276   | Layout 1 | `40e6326e69e3`  |
| 2269   | Layout 1 | `40e6326e69e3`  |
| 2259   | Layout 1 | `40e6326e69e3`  |
| 2250   | Layout 1 | `40e6326e69e3`  |
| 2243   | Layout 1 | `40e6326e69e3`  |
| 2235   | Layout 1 | `40e6326e69e3`  |
| 2229   | Layout 1 | `40e6326e69e3`  |
| 2224   | Layout 1 | `40e6326e69e3`  |
| 2218   | Layout 1 | `40e6326e69e3`  |
| 2215   | Layout 1 | `40e6326e69e3`  |
| 2207   | Layout 1 | `40e6326e69e3`  |
| 2203   | Layout 1 | `40e6326e69e3`  |
| 2196   | Layout 1 | `40e6326e69e3`  |
| 2192   | Layout 1 | `40e6326e69e3`  |
| 2189   | Layout 1 | `40e6326e69e3`  |
| 2183   | Layout 1 | `40e6326e69e3`  |
| 2179   | Layout 1 | `40e6326e69e3`  |
| 2171   | Layout 1 | `40e6326e69e3`  |
| 2163   | Layout 1 | `40e6326e69e3`  |
| 2156   | Layout 1 | `40e6326e69e3`  |
| 2151   | Layout 1 | `40e6326e69e3`  |
| 2147   | Layout 1 | `40e6326e69e3`  |
| 2142   | Layout 1 | `40e6326e69e3`  |
| 2138   | Layout 1 | `40e6326e69e3`  |
| 2134   | Layout 1 | `40e6326e69e3`  |
| 2130   | Layout 1 | `40e6326e69e3`  |
| 2122   | Layout 1 | `40e6326e69e3`  |
| 2107   | Layout 1 | `40e6326e69e3`  |
| 2098   | Layout 1 | `40e6326e69e3`  |
| 2089   | Layout 1 | `40e6326e69e3`  |
| 2081   | Layout 1 | `40e6326e69e3`  |
| 2073   | Layout 1 | `40e6326e69e3`  |
| 2067   | Layout 1 | `40e6326e69e3`  |
| 2063   | Layout 1 | `40e6326e69e3`  |
| 2059   | Layout 1 | `40e6326e69e3`  |
| 2052   | Layout 1 | `40e6326e69e3`  |
| 2044   | Layout 1 | `40e6326e69e3`  |
| 2039   | Layout 1 | `40e6326e69e3`  |
| 2032   | Layout 1 | `40e6326e69e3`  |
| 2025   | Layout 1 | `40e6326e69e3`  |
| 2011   | Layout 1 | `40e6326e69e3`  |
| 2005   | Layout 1 | `40e6326e69e3`  |
| 2000   | Layout 1 | `40e6326e69e3`  |
| 1996   | Layout 1 | `40e6326e69e3`  |
| 1991   | Layout 1 | `40e6326e69e3`  |
| 1985   | Layout 1 | `40e6326e69e3`  |
| 1980   | Layout 1 | `40e6326e69e3`  |
| 1969   | Layout 1 | `40e6326e69e3`  |
| 1964   | Layout 1 | `40e6326e69e3`  |
| 1958   | Layout 1 | `40e6326e69e3`  |
| 1950   | Layout 1 | `40e6326e69e3`  |
| 1945   | Layout 1 | `40e6326e69e3`  |
| 1937   | Layout 1 | `40e6326e69e3`  |
| 1933   | Layout 1 | `40e6326e69e3`  |
| 1927   | Layout 1 | `40e6326e69e3`  |
| 1921   | Layout 1 | `40e6326e69e3`  |
| 1914   | Layout 1 | `40e6326e69e3`  |
| 1908   | Layout 1 | `40e6326e69e3`  |
| 1897   | Layout 1 | `40e6326e69e3`  |
| 1892   | Layout 1 | `40e6326e69e3`  |
| 1886   | Layout 1 | `40e6326e69e3`  |
| 1881   | Layout 1 | `40e6326e69e3`  |
| 1871   | Layout 1 | `40e6326e69e3`  |
| 1866   | Layout 1 | `40e6326e69e3`  |
| 1862   | Layout 1 | `40e6326e69e3`  |
| 1854   | Layout 1 | `40e6326e69e3`  |
| 1846   | Layout 1 | `40e6326e69e3`  |
| 1838   | Layout 1 | `40e6326e69e3`  |
| 1832   | Layout 1 | `40e6326e69e3`  |
| 1826   | Layout 1 | `40e6326e69e3`  |
| 1822   | Layout 1 | `40e6326e69e3`  |
| 1818   | Layout 1 | `40e6326e69e3`  |
| 1804   | Layout 1 | `40e6326e69e3`  |
| 1794   | Layout 1 | `40e6326e69e3`  |
| 1790   | Layout 1 | `40e6326e69e3`  |
| 1784   | Layout 1 | `40e6326e69e3`  |
| 1774   | Layout 1 | `40e6326e69e3`  |
| 1771   | Layout 1 | `40e6326e69e3`  |
| 1762   | Layout 1 | `40e6326e69e3`  |
| 1759   | Layout 1 | `40e6326e69e3`  |
| 1754   | Layout 1 | `40e6326e69e3`  |
| 1749   | Layout 1 | `40e6326e69e3`  |
| 1743   | Layout 1 | `40e6326e69e3`  |
| 1737   | Layout 1 | `40e6326e69e3`  |
| 1731   | Layout 1 | `40e6326e69e3`  |
| 1725   | Layout 1 | `40e6326e69e3`  |
| 1717   | Layout 1 | `40e6326e69e3`  |
| 1710   | Layout 1 | `40e6326e69e3`  |
| 1704   | Layout 1 | `40e6326e69e3`  |
| 1698   | Layout 1 | `40e6326e69e3`  |
| 1690   | Layout 1 | `40e6326e69e3`  |
| 1685   | Layout 1 | `40e6326e69e3`  |
| 1680   | Layout 1 | `40e6326e69e3`  |
| 1674   | Layout 1 | `40e6326e69e3`  |
| 1668   | Layout 1 | `40e6326e69e3`  |
| 1659   | Layout 1 | `40e6326e69e3`  |
| 1649   | Layout 1 | `40e6326e69e3`  |
| 1642   | Layout 1 | `40e6326e69e3`  |
| 1636   | Layout 1 | `40e6326e69e3`  |
| 1628   | Layout 1 | `40e6326e69e3`  |
| 1622   | Layout 1 | `40e6326e69e3`  |
| 1614   | Layout 1 | `40e6326e69e3`  |
| 1608   | Layout 1 | `40e6326e69e3`  |
| 1602   | Layout 1 | `40e6326e69e3`  |
| 1598   | Layout 1 | `40e6326e69e3`  |
| 1594   | Layout 1 | `40e6326e69e3`  |
| 1590   | Layout 1 | `40e6326e69e3`  |
| 1587   | Layout 1 | `40e6326e69e3`  |
| 1584   | Layout 1 | `40e6326e69e3`  |
| 1579   | Layout 1 | `40e6326e69e3`  |
| 1572   | Layout 1 | `40e6326e69e3`  |
| 1565   | Layout 1 | `40e6326e69e3`  |
| 1559   | Layout 1 | `40e6326e69e3`  |
| 1554   | Layout 1 | `40e6326e69e3`  |
| 1547   | Layout 1 | `40e6326e69e3`  |
| 1537   | Layout 1 | `40e6326e69e3`  |
| 1529   | Layout 1 | `40e6326e69e3`  |
| 1524   | Layout 1 | `40e6326e69e3`  |
| 1519   | Layout 1 | `40e6326e69e3`  |
| 1509   | Layout 1 | `40e6326e69e3`  |
| 1506   | Layout 1 | `40e6326e69e3`  |
| 1504   | Layout 1 | `40e6326e69e3`  |
| 1500   | Layout 1 | `40e6326e69e3`  |
| 1493   | Layout 1 | `40e6326e69e3`  |
| 1489   | Layout 1 | `40e6326e69e3`  |
| 1485   | Layout 1 | `40e6326e69e3`  |
| 1481   | Layout 1 | `40e6326e69e3`  |
| 1474   | Layout 1 | `40e6326e69e3`  |
| 1466   | Layout 1 | `40e6326e69e3`  |
| 1462   | Layout 1 | `40e6326e69e3`  |
| 1459   | Layout 1 | `40e6326e69e3`  |
| 1453   | Layout 1 | `40e6326e69e3`  |
| 1450   | Layout 1 | `40e6326e69e3`  |
| 1445   | Layout 1 | `40e6326e69e3`  |
| 1439   | Layout 1 | `40e6326e69e3`  |
| 1433   | Layout 1 | `40e6326e69e3`  |
| 1430   | Layout 1 | `40e6326e69e3`  |
| 1426   | Layout 1 | `40e6326e69e3`  |
| 1421   | Layout 1 | `40e6326e69e3`  |
| 1417   | Layout 1 | `40e6326e69e3`  |
| 1416   | Layout 1 | `40e6326e69e3`  |
| 1409   | Layout 1 | `40e6326e69e3`  |
| 1405   | Layout 1 | `40e6326e69e3`  |
| 1401   | Layout 1 | `40e6326e69e3`  |
| 1396   | Layout 1 | `40e6326e69e3`  |
| 1391   | Layout 1 | `40e6326e69e3`  |
| 1390   | Layout 1 | `40e6326e69e3`  |
| 1386   | Layout 1 | `40e6326e69e3`  |
| 1381   | Layout 1 | `40e6326e69e3`  |
| 1379   | Layout 1 | `40e6326e69e3`  |
| 1372   | Layout 1 | `40e6326e69e3`  |
| 1366   | Layout 1 | `40e6326e69e3`  |
| 1364   | Layout 1 | `40e6326e69e3`  |
| 1363   | Layout 1 | `40e6326e69e3`  |
| 1360   | Layout 1 | `40e6326e69e3`  |
| 1358   | Layout 1 | `40e6326e69e3`  |
| 1355   | Layout 1 | `40e6326e69e3`  |
| 1351   | Layout 1 | `40e6326e69e3`  |
| 1348   | Layout 1 | `40e6326e69e3`  |
| 1346   | Layout 1 | `40e6326e69e3`  |
| 1341   | Layout 1 | `40e6326e69e3`  |
| 1340   | Layout 1 | `40e6326e69e3`  |
| 1338   | Layout 1 | `40e6326e69e3`  |
| 1335   | Layout 1 | `40e6326e69e3`  |
| 1333   | Layout 1 | `40e6326e69e3`  |
| 1329   | Layout 1 | `40e6326e69e3`  |
| 1327   | Layout 1 | `40e6326e69e3`  |
| 1324   | Layout 1 | `40e6326e69e3`  |
| 1321   | Layout 1 | `40e6326e69e3`  |
| 1319   | Layout 1 | `40e6326e69e3`  |
| 1318   | Layout 1 | `40e6326e69e3`  |
| 1316   | Layout 1 | `40e6326e69e3`  |
| 1313   | Layout 1 | `40e6326e69e3`  |
| 1311   | Layout 1 | `40e6326e69e3`  |
| 1309   | Layout 1 | `40e6326e69e3`  |
| 1304   | Layout 1 | `40e6326e69e3`  |
| 1292   | Layout 1 | `40e6326e69e3`  |
| 1286   | Layout 1 | `40e6326e69e3`  |
| 1280   | Layout 1 | `40e6326e69e3`  |
| 1276   | No file  | `40e6326e69e3`  |
| 1267   | No file  | `40e6326e69e3`  |
| 1261   | No file  | `40e6326e69e3`  |
| 1256   | No file  | `40e6326e69e3`  |
| 1250   | No file  | `40e6326e69e3`  |
| 1246   | No file  | `40e6326e69e3`  |
| 1239   | No file  | `40e6326e69e3`  |
| 1230   | No file  | `40e6326e69e3`  |
| 1226   | No file  | `40e6326e69e3`  |
| 1220   | No file  | `40e6326e69e3`  |
| 1217   | No file  | `40e6326e69e3`  |
| 1211   | No file  | `40e6326e69e3`  |
| 1210   | No file  | `40e6326e69e3`  |
| 1208   | No file  | `40e6326e69e3`  |
| 1203   | No file  | `40e6326e69e3`  |
| 1197   | No file  | `40e6326e69e3`  |
| 1194   | No file  | `40e6326e69e3`  |
| 1192   | No file  | `40e6326e69e3`  |
| 1187   | No file  | `40e6326e69e3`  |
| 1183   | No file  | `40e6326e69e3`  |
| 1177   | No file  | `40e6326e69e3`  |
| 1173   | No file  | `40e6326e69e3`  |
| 1167   | No file  | `40e6326e69e3`  |
| 1164   | No file  | `40e6326e69e3`  |
| 1156   | No file  | `40e6326e69e3`  |
| 1149   | No file  | `40e6326e69e3`  |
| 1144   | No file  | `40e6326e69e3`  |
| 1137   | No file  | `40e6326e69e3`  |
| 1132   | No file  | `40e6326e69e3`  |
| 1127   | No file  | `40e6326e69e3`  |
| 1122   | No file  | `40e6326e69e3`  |
| 1118   | No file  | `40e6326e69e3`  |
| 1114   | No file  | `40e6326e69e3`  |
| 1109   | No file  | `40e6326e69e3`  |
| 1102   | No file  | `40e6326e69e3`  |
| 1096   | No file  | `40e6326e69e3`  |
| 1088   | No file  | `40e6326e69e3`  |
| 1081   | No file  | `40e6326e69e3`  |
| 1076   | No file  | `40e6326e69e3`  |
| 1069   | No file  | `40e6326e69e3`  |
| 1064   | No file  | `40e6326e69e3`  |
| 1058   | No file  | `40e6326e69e3`  |
| 1051   | No file  | `40e6326e69e3`  |
| 1044   | No file  | `40e6326e69e3`  |
| 1036   | No file  | `40e6326e69e3`  |
| 1026   | No file  | `40e6326e69e3`  |
| 1016   | No file  | `40e6326e69e3`  |
| 1009   | No file  | `40e6326e69e3`  |
| 1005   | No file  | `40e6326e69e3`  |
| 1000   | No file  | `40e6326e69e3`  |
| 998    | No file  | `40e6326e69e3`  |
| 990    | No file  | `40e6326e69e3`  |
| 979    | No file  | `40e6326e69e3`  |
| 972    | No file  | `40e6326e69e3`  |
| 963    | No file  | `40e6326e69e3`  |
| 955    | No file  | `40e6326e69e3`  |
| 946    | No file  | `40e6326e69e3`  |
| 938    | No file  | `40e6326e69e3`  |
| 927    | No file  | `40e6326e69e3`  |
| 911    | No file  | `40e6326e69e3`  |
| 904    | No file  | `40e6326e69e3`  |
| 899    | No file  | `40e6326e69e3`  |
| 894    | No file  | `40e6326e69e3`  |
| 885    | No file  | `40e6326e69e3`  |
| 879    | No file  | `40e6326e69e3`  |
| 872    | No file  | `40e6326e69e3`  |
| 864    | No file  | `40e6326e69e3`  |
| 855    | No file  | `40e6326e69e3`  |
| 853    | No file  | `40e6326e69e3`  |
| 845    | No file  | `40e6326e69e3`  |
| 837    | No file  | `40e6326e69e3`  |
| 829    | No file  | `40e6326e69e3`  |
| 822    | No file  | `40e6326e69e3`  |
| 814    | No file  | `40e6326e69e3`  |
| 805    | No file  | `40e6326e69e3`  |
| 794    | No file  | `40e6326e69e3`  |
| 787    | No file  | `40e6326e69e3`  |
| 780    | No file  | `40e6326e69e3`  |
| 771    | No file  | `40e6326e69e3`  |
| 760    | No file  | `40e6326e69e3`  |
| 748    | No file  | `40e6326e69e3`  |
| 741    | No file  | `40e6326e69e3`  |
| 736    | No file  | `40e6326e69e3`  |
| 731    | No file  | `40e6326e69e3`  |
| 723    | No file  | `40e6326e69e3`  |
| 711    | No file  | `40e6326e69e3`  |
| 707    | No file  | `40e6326e69e3`  |
| 697    | No file  | `40e6326e69e3`  |
| 689    | No file  | `40e6326e69e3`  |
| 683    | No file  | `40e6326e69e3`  |
| 678    | No file  | `40e6326e69e3`  |
| 670    | No file  | `40e6326e69e3`  |
| 661    | No file  | `40e6326e69e3`  |
| 656    | No file  | `40e6326e69e3`  |
| 652    | No file  | `40e6326e69e3`  |
| 643    | No file  | `40e6326e69e3`  |
| 637    | No file  | `40e6326e69e3`  |
| 630    | No file  | `40e6326e69e3`  |
| 627    | No file  | `40e6326e69e3`  |
| 621    | No file  | `40e6326e69e3`  |
| 617    | No file  | `40e6326e69e3`  |
| 615    | No file  | `40e6326e69e3`  |
| 606    | No file  | `40e6326e69e3`  |
| 599    | No file  | `40e6326e69e3`  |
| 592    | No file  | `40e6326e69e3`  |
| 586    | No file  | `40e6326e69e3`  |
| 577    | No file  | `40e6326e69e3`  |
| 569    | No file  | `40e6326e69e3`  |
| 561    | No file  | `40e6326e69e3`  |
| 554    | No file  | `40e6326e69e3`  |
| 542    | No file  | `40e6326e69e3`  |
| 532    | No file  | `40e6326e69e3`  |
| 531    | No file  | `40e6326e69e3`  |
| 526    | No file  | `40e6326e69e3`  |
| 521    | No file  | `40e6326e69e3`  |
| 517    | No file  | `40e6326e69e3`  |
| 510    | No file  | `40e6326e69e3`  |
| 508    | No file  | `40e6326e69e3`  |
| 504    | No file  | `40e6326e69e3`  |
| 497    | No file  | `40e6326e69e3`  |
| 491    | No file  | `40e6326e69e3`  |
| 485    | No file  | `40e6326e69e3`  |
| 478    | No file  | `40e6326e69e3`  |
| 472    | No file  | `40e6326e69e3`  |
| 466    | No file  | `40e6326e69e3`  |
| 457    | No file  | `40e6326e69e3`  |
| 452    | No file  | `40e6326e69e3`  |
| 449    | No file  | `40e6326e69e3`  |
| 435    | No file  | `40e6326e69e3`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                       |
| ---------------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `emoticonpackageoffset.dbss` | Optional | `package_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `emoticon.dbss`              | Optional | The emoticon names (LOC type 60, else the Korean name) and icons of the listed keys        |
| `languagedata_en.loc`        | Optional | Emoticon names, LOC type 60                                                                |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 20 bytes + name and emoticons)

| Offset         | Type                      | Field          | Notes                                                                               |
| -------------- | ------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| `+0x00`        | u32                       | package_key    | Row key, `1` to `47` in file order on client 3482                                   |
| `+0x04`        | u32                       | unknown_04     | `0` on every row; the index rows carry it after the key too                         |
| `+0x08`        | str16                     | name_kr        | Korean name: `무제한` (unlimited) on 45 rows, `기간제` (limited-time) on rows `2` and `3` (client 3482) |
| `name_kr+0x00` | u32                       | emoticon_count | Number of `emoticons`, `1` to `12` on client 3482                                   |
| `name_kr+0x04` | Emoticon[emoticon_count]  | emoticons      | See Emoticon                                                                        |

### Emoticon (8 bytes)

| Offset  | Type | Field        | Notes                                                                       |
| ------- | ---- | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32  | emoticon_key | An [`emoticon.dbss`](emoticon_dbss.md) key; all 120 entries of client 3482 have a row there |
| `+0x04` | u32  | unknown_04   | `0` on every entry                                                          |

### `emoticonpackageoffset.dbss`

Bare offset table into `emoticonpackage.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `emoticonpackage.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                          |

### Offset Row (16 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | package_key | Key of the row it points at                                        |
| `+0x04` | u32  | unknown_04  | `0` on every row, as the row's `unknown_04`                        |
| `+0x08` | u32  | data_offset | Absolute offset of the row in `emoticonpackage.dbss`, at `package_key` |
| `+0x0C` | u32  | data_size   | The whole row                                                      |

The index rows are in file order; on clients 1784 and 3482 every index row
points at the row with its key.

## Field Names

The `EmoticonPackage_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `key`, `EmoticonKey` (a comma list) and
`name`, 7 rows.

| Field         | Column        | Same value (client 1784) | Same value (client 3482) |
| ------------- | ------------- | ------------------------ | ------------------------ |
| package_key   | `key`         | 7 of 7                   | 7 of 7                   |
| name_kr       | `name`        | 7 of 7                   | 7 of 7                   |
| emoticons     | `EmoticonKey` | 6 of 7                   | 6 of 7                   |

Package `2` lists the same seven keys as the sheet in another order
(`1, 2, 10, 3, 11, 4, 12` against `1,2,3,4,10,11,12`) on both clients, so
the file does not keep the sheet's list order.

## Open Questions

### What the Zero Fields Hold

`unknown_04` after the package key, in the row and the index row, and after
every emoticon key is `0` on clients 1784 and 3482, as in
[`emoticon.dbss`](emoticon_dbss.md). Each key and its `unknown_04` may be
one 8-byte key.

### How a Package Is Granted

No Lua call or sheet column links a package to the item or Pearl Shop
product that unlocks it, so where `package_key` is used is open. The
`기간제` (limited-time) rows suggest an expiry, which
`ToClient_getEmoticonExpirationDate()` reads without a package argument.
