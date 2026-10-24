# `weburl.bss` Format

## Purpose

The web addresses the game client opens: payment pages, the coupon page,
the game portal, the news and notice pages. A PABR list of URLs with no
count; each URL is a string-table index and a list of insert points,
the character offsets in the URL where the client fills in a value such
as the account number or the language. The client Lua reads the URLs by
web URL type through `ToClient_getWebUrl`. On client 3482 it holds
17 URLs, all on the `naeu.playblackdesert.com` hosts and
`blackdesert.pearlabyss.com`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File         | Bytes | Records           | Row bytes              |
| ------ | -------------- | ------- | ------------ | ----- | ----------------- | ---------------------- |
| 2      | 1358 and later | 3483    | `weburl.bss` | 1,236 | 32 Insert, 17 Url | 5                      |
| 1      | 1309 to 1355   | 1355    | `weburl.bss` | 255   | 4 Insert, 8 Url   | 8 to 18, 10 on average |

| Layout | File         | Known           | Unknown    |
| ------ | ------------ | --------------- | ---------- |
| 2      | `weburl.bss` | 1,232 B (99.7%) | 4 B (0.3%) |
| 1      | `weburl.bss` | 255 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `bed36aa90c9f`  |
| 3482   | Layout 2 | `bed36aa90c9f`  |
| 3474   | Layout 2 | `bed36aa90c9f`  |
| 3473   | Layout 2 | `bed36aa90c9f`  |
| 3464   | Layout 2 | `bed36aa90c9f`  |
| 3458   | Layout 2 | `bed36aa90c9f`  |
| 3454   | Layout 2 | `bed36aa90c9f`  |
| 3444   | Layout 2 | `bed36aa90c9f`  |
| 3435   | Layout 2 | `bed36aa90c9f`  |
| 3426   | Layout 2 | `bed36aa90c9f`  |
| 3418   | Layout 2 | `bed36aa90c9f`  |
| 3412   | Layout 2 | `bed36aa90c9f`  |
| 3402   | Layout 2 | `bed36aa90c9f`  |
| 3396   | Layout 2 | `bed36aa90c9f`  |
| 3387   | Layout 2 | `bed36aa90c9f`  |
| 3381   | Layout 2 | `bed36aa90c9f`  |
| 3373   | Layout 2 | `bed36aa90c9f`  |
| 3364   | Layout 2 | `bed36aa90c9f`  |
| 3356   | Layout 2 | `bed36aa90c9f`  |
| 3349   | Layout 2 | `bed36aa90c9f`  |
| 3342   | Layout 2 | `bed36aa90c9f`  |
| 3335   | Layout 2 | `bed36aa90c9f`  |
| 3326   | Layout 2 | `bed36aa90c9f`  |
| 3321   | Layout 2 | `bed36aa90c9f`  |
| 3314   | Layout 2 | `bed36aa90c9f`  |
| 3303   | Layout 2 | `bed36aa90c9f`  |
| 3302   | Layout 2 | `bed36aa90c9f`  |
| 3293   | Layout 2 | `bed36aa90c9f`  |
| 3283   | Layout 2 | `bed36aa90c9f`  |
| 3275   | Layout 2 | `bed36aa90c9f`  |
| 3267   | Layout 2 | `bed36aa90c9f`  |
| 3258   | Layout 2 | `bed36aa90c9f`  |
| 3251   | Layout 2 | `bed36aa90c9f`  |
| 3242   | Layout 2 | `bed36aa90c9f`  |
| 3235   | Layout 2 | `bed36aa90c9f`  |
| 3229   | Layout 2 | `bed36aa90c9f`  |
| 3212   | Layout 2 | `bed36aa90c9f`  |
| 3203   | Layout 2 | `bed36aa90c9f`  |
| 3193   | Layout 2 | `bed36aa90c9f`  |
| 3186   | Layout 2 | `bed36aa90c9f`  |
| 3177   | Layout 2 | `bed36aa90c9f`  |
| 3169   | Layout 2 | `bed36aa90c9f`  |
| 3158   | Layout 2 | `bed36aa90c9f`  |
| 3151   | Layout 2 | `bed36aa90c9f`  |
| 3144   | Layout 2 | `bed36aa90c9f`  |
| 3133   | Layout 2 | `bed36aa90c9f`  |
| 3125   | Layout 2 | `bed36aa90c9f`  |
| 3118   | Layout 2 | `bed36aa90c9f`  |
| 3111   | Layout 2 | `bed36aa90c9f`  |
| 3103   | Layout 2 | `bed36aa90c9f`  |
| 3095   | Layout 2 | `bed36aa90c9f`  |
| 3086   | Layout 2 | `bed36aa90c9f`  |
| 3072   | Layout 2 | `bed36aa90c9f`  |
| 3062   | Layout 2 | `bed36aa90c9f`  |
| 3052   | Layout 2 | `bed36aa90c9f`  |
| 3045   | Layout 2 | `bed36aa90c9f`  |
| 3037   | Layout 2 | `bed36aa90c9f`  |
| 3030   | Layout 2 | `bed36aa90c9f`  |
| 3021   | Layout 2 | `bed36aa90c9f`  |
| 3012   | Layout 2 | `bed36aa90c9f`  |
| 3002   | Layout 2 | `bed36aa90c9f`  |
| 2995   | Layout 2 | `bed36aa90c9f`  |
| 2987   | Layout 2 | `bed36aa90c9f`  |
| 2978   | Layout 2 | `bed36aa90c9f`  |
| 2970   | Layout 2 | `bed36aa90c9f`  |
| 2959   | Layout 2 | `bed36aa90c9f`  |
| 2951   | Layout 2 | `bed36aa90c9f`  |
| 2942   | Layout 2 | `bed36aa90c9f`  |
| 2935   | Layout 2 | `bed36aa90c9f`  |
| 2932   | Layout 2 | `bed36aa90c9f`  |
| 2923   | Layout 2 | `bed36aa90c9f`  |
| 2919   | Layout 2 | `bed36aa90c9f`  |
| 2907   | Layout 2 | `bed36aa90c9f`  |
| 2900   | Layout 2 | `bed36aa90c9f`  |
| 2891   | Layout 2 | `bed36aa90c9f`  |
| 2882   | Layout 2 | `bed36aa90c9f`  |
| 2872   | Layout 2 | `bed36aa90c9f`  |
| 2863   | Layout 2 | `bed36aa90c9f`  |
| 2855   | Layout 2 | `bed36aa90c9f`  |
| 2849   | Layout 2 | `bed36aa90c9f`  |
| 2844   | Layout 2 | `bed36aa90c9f`  |
| 2834   | Layout 2 | `bed36aa90c9f`  |
| 2825   | Layout 2 | `bed36aa90c9f`  |
| 2819   | Layout 2 | `bed36aa90c9f`  |
| 2811   | Layout 2 | `bed36aa90c9f`  |
| 2803   | Layout 2 | `bed36aa90c9f`  |
| 2794   | Layout 2 | `bed36aa90c9f`  |
| 2783   | Layout 2 | `bed36aa90c9f`  |
| 2774   | Layout 2 | `bed36aa90c9f`  |
| 2765   | Layout 2 | `bed36aa90c9f`  |
| 2756   | Layout 2 | `bed36aa90c9f`  |
| 2750   | Layout 2 | `bed36aa90c9f`  |
| 2743   | Layout 2 | `bed36aa90c9f`  |
| 2736   | Layout 2 | `bed36aa90c9f`  |
| 2726   | Layout 2 | `bed36aa90c9f`  |
| 2717   | Layout 2 | `bed36aa90c9f`  |
| 2709   | Layout 2 | `bed36aa90c9f`  |
| 2703   | Layout 2 | `bed36aa90c9f`  |
| 2695   | Layout 2 | `bed36aa90c9f`  |
| 2684   | Layout 2 | `bed36aa90c9f`  |
| 2672   | Layout 2 | `bed36aa90c9f`  |
| 2665   | Layout 2 | `bed36aa90c9f`  |
| 2657   | Layout 2 | `bed36aa90c9f`  |
| 2649   | Layout 2 | `bed36aa90c9f`  |
| 2644   | Layout 2 | `bed36aa90c9f`  |
| 2637   | Layout 2 | `bed36aa90c9f`  |
| 2629   | Layout 2 | `bed36aa90c9f`  |
| 2619   | Layout 2 | `bed36aa90c9f`  |
| 2612   | Layout 2 | `bed36aa90c9f`  |
| 2606   | Layout 2 | `bed36aa90c9f`  |
| 2602   | Layout 2 | `bed36aa90c9f`  |
| 2601   | Layout 2 | `bed36aa90c9f`  |
| 2592   | Layout 2 | `bed36aa90c9f`  |
| 2583   | Layout 2 | `bed36aa90c9f`  |
| 2575   | Layout 2 | `bed36aa90c9f`  |
| 2567   | Layout 2 | `bed36aa90c9f`  |
| 2560   | Layout 2 | `bed36aa90c9f`  |
| 2553   | Layout 2 | `bed36aa90c9f`  |
| 2545   | Layout 2 | `bed36aa90c9f`  |
| 2538   | Layout 2 | `bed36aa90c9f`  |
| 2529   | Layout 2 | `bed36aa90c9f`  |
| 2519   | Layout 2 | `bed36aa90c9f`  |
| 2513   | Layout 2 | `bed36aa90c9f`  |
| 2510   | Layout 2 | `bed36aa90c9f`  |
| 2507   | Layout 2 | `bed36aa90c9f`  |
| 2503   | Layout 2 | `bed36aa90c9f`  |
| 2498   | Layout 2 | `bed36aa90c9f`  |
| 2492   | Layout 2 | `bed36aa90c9f`  |
| 2487   | Layout 2 | `bed36aa90c9f`  |
| 2480   | Layout 2 | `bed36aa90c9f`  |
| 2474   | Layout 2 | `bed36aa90c9f`  |
| 2468   | Layout 2 | `bed36aa90c9f`  |
| 2460   | Layout 2 | `bed36aa90c9f`  |
| 2453   | Layout 2 | `bed36aa90c9f`  |
| 2444   | Layout 2 | `bed36aa90c9f`  |
| 2438   | Layout 2 | `bed36aa90c9f`  |
| 2434   | Layout 2 | `bed36aa90c9f`  |
| 2429   | Layout 2 | `bed36aa90c9f`  |
| 2421   | Layout 2 | `bed36aa90c9f`  |
| 2414   | Layout 2 | `bed36aa90c9f`  |
| 2407   | Layout 2 | `bed36aa90c9f`  |
| 2401   | Layout 2 | `bed36aa90c9f`  |
| 2397   | Layout 2 | `bed36aa90c9f`  |
| 2393   | Layout 2 | `bed36aa90c9f`  |
| 2384   | Layout 2 | `bed36aa90c9f`  |
| 2378   | Layout 2 | `bed36aa90c9f`  |
| 2372   | Layout 2 | `bed36aa90c9f`  |
| 2358   | Layout 2 | `bed36aa90c9f`  |
| 2352   | Layout 2 | `bed36aa90c9f`  |
| 2347   | Layout 2 | `bed36aa90c9f`  |
| 2343   | Layout 2 | `bed36aa90c9f`  |
| 2335   | Layout 2 | `bed36aa90c9f`  |
| 2327   | Layout 2 | `bed36aa90c9f`  |
| 2324   | Layout 2 | `bed36aa90c9f`  |
| 2319   | Layout 2 | `bed36aa90c9f`  |
| 2313   | Layout 2 | `bed36aa90c9f`  |
| 2308   | Layout 2 | `bed36aa90c9f`  |
| 2302   | Layout 2 | `bed36aa90c9f`  |
| 2295   | Layout 2 | `bed36aa90c9f`  |
| 2290   | Layout 2 | `bed36aa90c9f`  |
| 2284   | Layout 2 | `bed36aa90c9f`  |
| 2276   | Layout 2 | `bed36aa90c9f`  |
| 2269   | Layout 2 | `bed36aa90c9f`  |
| 2259   | Layout 2 | `bed36aa90c9f`  |
| 2250   | Layout 2 | `bed36aa90c9f`  |
| 2243   | Layout 2 | `bed36aa90c9f`  |
| 2235   | Layout 2 | `bed36aa90c9f`  |
| 2229   | Layout 2 | `bed36aa90c9f`  |
| 2224   | Layout 2 | `bed36aa90c9f`  |
| 2218   | Layout 2 | `bed36aa90c9f`  |
| 2215   | Layout 2 | `bed36aa90c9f`  |
| 2207   | Layout 2 | `bed36aa90c9f`  |
| 2203   | Layout 2 | `bed36aa90c9f`  |
| 2196   | Layout 2 | `bed36aa90c9f`  |
| 2192   | Layout 2 | `bed36aa90c9f`  |
| 2189   | Layout 2 | `bed36aa90c9f`  |
| 2183   | Layout 2 | `bed36aa90c9f`  |
| 2179   | Layout 2 | `bed36aa90c9f`  |
| 2171   | Layout 2 | `bed36aa90c9f`  |
| 2163   | Layout 2 | `bed36aa90c9f`  |
| 2156   | Layout 2 | `bed36aa90c9f`  |
| 2151   | Layout 2 | `bed36aa90c9f`  |
| 2147   | Layout 2 | `bed36aa90c9f`  |
| 2142   | Layout 2 | `bed36aa90c9f`  |
| 2138   | Layout 2 | `bed36aa90c9f`  |
| 2134   | Layout 2 | `bed36aa90c9f`  |
| 2130   | Layout 2 | `bed36aa90c9f`  |
| 2122   | Layout 2 | `bed36aa90c9f`  |
| 2107   | Layout 2 | `bed36aa90c9f`  |
| 2098   | Layout 2 | `bed36aa90c9f`  |
| 2089   | Layout 2 | `bed36aa90c9f`  |
| 2081   | Layout 2 | `bed36aa90c9f`  |
| 2073   | Layout 2 | `bed36aa90c9f`  |
| 2067   | Layout 2 | `bed36aa90c9f`  |
| 2063   | Layout 2 | `bed36aa90c9f`  |
| 2059   | Layout 2 | `bed36aa90c9f`  |
| 2052   | Layout 2 | `bed36aa90c9f`  |
| 2044   | Layout 2 | `bed36aa90c9f`  |
| 2039   | Layout 2 | `bed36aa90c9f`  |
| 2032   | Layout 2 | `bed36aa90c9f`  |
| 2025   | Layout 2 | `bed36aa90c9f`  |
| 2011   | Layout 2 | `bed36aa90c9f`  |
| 2005   | Layout 2 | `bed36aa90c9f`  |
| 2000   | Layout 2 | `bed36aa90c9f`  |
| 1996   | Layout 2 | `bed36aa90c9f`  |
| 1991   | Layout 2 | `bed36aa90c9f`  |
| 1985   | Layout 2 | `bed36aa90c9f`  |
| 1980   | Layout 2 | `bed36aa90c9f`  |
| 1969   | Layout 2 | `bed36aa90c9f`  |
| 1964   | Layout 2 | `bed36aa90c9f`  |
| 1958   | Layout 2 | `bed36aa90c9f`  |
| 1950   | Layout 2 | `bed36aa90c9f`  |
| 1945   | Layout 2 | `bed36aa90c9f`  |
| 1937   | Layout 2 | `bed36aa90c9f`  |
| 1933   | Layout 2 | `bed36aa90c9f`  |
| 1927   | Layout 2 | `bed36aa90c9f`  |
| 1921   | Layout 2 | `bed36aa90c9f`  |
| 1914   | Layout 2 | `bed36aa90c9f`  |
| 1908   | Layout 2 | `bed36aa90c9f`  |
| 1897   | Layout 2 | `bed36aa90c9f`  |
| 1892   | Layout 2 | `bed36aa90c9f`  |
| 1886   | Layout 2 | `bed36aa90c9f`  |
| 1881   | Layout 2 | `bed36aa90c9f`  |
| 1871   | Layout 2 | `bed36aa90c9f`  |
| 1866   | Layout 2 | `bed36aa90c9f`  |
| 1862   | Layout 2 | `bed36aa90c9f`  |
| 1854   | Layout 2 | `bed36aa90c9f`  |
| 1846   | Layout 2 | `bed36aa90c9f`  |
| 1838   | Layout 2 | `bed36aa90c9f`  |
| 1832   | Layout 2 | `bed36aa90c9f`  |
| 1826   | Layout 2 | `bed36aa90c9f`  |
| 1822   | Layout 2 | `bed36aa90c9f`  |
| 1818   | Layout 2 | `bed36aa90c9f`  |
| 1804   | Layout 2 | `bed36aa90c9f`  |
| 1794   | Layout 2 | `bed36aa90c9f`  |
| 1790   | Layout 2 | `bed36aa90c9f`  |
| 1784   | Layout 2 | `bed36aa90c9f`  |
| 1774   | Layout 2 | `bed36aa90c9f`  |
| 1771   | Layout 2 | `bed36aa90c9f`  |
| 1762   | Layout 2 | `bed36aa90c9f`  |
| 1759   | Layout 2 | `bed36aa90c9f`  |
| 1754   | Layout 2 | `bed36aa90c9f`  |
| 1749   | Layout 2 | `bed36aa90c9f`  |
| 1743   | Layout 2 | `bed36aa90c9f`  |
| 1737   | Layout 2 | `bed36aa90c9f`  |
| 1731   | Layout 2 | `bed36aa90c9f`  |
| 1725   | Layout 2 | `bed36aa90c9f`  |
| 1717   | Layout 2 | `bed36aa90c9f`  |
| 1710   | Layout 2 | `bed36aa90c9f`  |
| 1704   | Layout 2 | `bed36aa90c9f`  |
| 1698   | Layout 2 | `bed36aa90c9f`  |
| 1690   | Layout 2 | `bed36aa90c9f`  |
| 1685   | Layout 2 | `bed36aa90c9f`  |
| 1680   | Layout 2 | `bed36aa90c9f`  |
| 1674   | Layout 2 | `bed36aa90c9f`  |
| 1668   | Layout 2 | `bed36aa90c9f`  |
| 1659   | Layout 2 | `bed36aa90c9f`  |
| 1649   | Layout 2 | `bed36aa90c9f`  |
| 1642   | Layout 2 | `bed36aa90c9f`  |
| 1636   | Layout 2 | `bed36aa90c9f`  |
| 1628   | Layout 2 | `bed36aa90c9f`  |
| 1622   | Layout 2 | `bed36aa90c9f`  |
| 1614   | Layout 2 | `bed36aa90c9f`  |
| 1608   | Layout 2 | `bed36aa90c9f`  |
| 1602   | Layout 2 | `bed36aa90c9f`  |
| 1598   | Layout 2 | `bed36aa90c9f`  |
| 1594   | Layout 2 | `bed36aa90c9f`  |
| 1590   | Layout 2 | `bed36aa90c9f`  |
| 1587   | Layout 2 | `bed36aa90c9f`  |
| 1584   | Layout 2 | `bed36aa90c9f`  |
| 1579   | Layout 2 | `bed36aa90c9f`  |
| 1572   | Layout 2 | `bed36aa90c9f`  |
| 1565   | Layout 2 | `bed36aa90c9f`  |
| 1559   | Layout 2 | `bed36aa90c9f`  |
| 1554   | Layout 2 | `bed36aa90c9f`  |
| 1547   | Layout 2 | `bed36aa90c9f`  |
| 1537   | Layout 2 | `bed36aa90c9f`  |
| 1529   | Layout 2 | `bed36aa90c9f`  |
| 1524   | Layout 2 | `bed36aa90c9f`  |
| 1519   | Layout 2 | `bed36aa90c9f`  |
| 1509   | Layout 2 | `bed36aa90c9f`  |
| 1506   | Layout 2 | `bed36aa90c9f`  |
| 1504   | Layout 2 | `bed36aa90c9f`  |
| 1500   | Layout 2 | `bed36aa90c9f`  |
| 1493   | Layout 2 | `bed36aa90c9f`  |
| 1489   | Layout 2 | `bed36aa90c9f`  |
| 1485   | Layout 2 | `bed36aa90c9f`  |
| 1481   | Layout 2 | `bed36aa90c9f`  |
| 1474   | Layout 2 | `bed36aa90c9f`  |
| 1466   | Layout 2 | `bed36aa90c9f`  |
| 1462   | Layout 2 | `bed36aa90c9f`  |
| 1459   | Layout 2 | `bed36aa90c9f`  |
| 1453   | Layout 2 | `bed36aa90c9f`  |
| 1450   | Layout 2 | `bed36aa90c9f`  |
| 1445   | Layout 2 | `bed36aa90c9f`  |
| 1439   | Layout 2 | `bed36aa90c9f`  |
| 1433   | Layout 2 | `bed36aa90c9f`  |
| 1430   | Layout 2 | `bed36aa90c9f`  |
| 1426   | Layout 2 | `bed36aa90c9f`  |
| 1421   | Layout 2 | `bed36aa90c9f`  |
| 1417   | Layout 2 | `bed36aa90c9f`  |
| 1416   | Layout 2 | `bed36aa90c9f`  |
| 1409   | Layout 2 | `bed36aa90c9f`  |
| 1405   | Layout 2 | `bed36aa90c9f`  |
| 1401   | Layout 2 | `bed36aa90c9f`  |
| 1396   | Layout 2 | `bed36aa90c9f`  |
| 1391   | Layout 2 | `bed36aa90c9f`  |
| 1390   | Layout 2 | `bed36aa90c9f`  |
| 1386   | Layout 2 | `bed36aa90c9f`  |
| 1381   | Layout 2 | `bed36aa90c9f`  |
| 1379   | Layout 2 | `bed36aa90c9f`  |
| 1372   | Layout 2 | `bed36aa90c9f`  |
| 1366   | Layout 2 | `bed36aa90c9f`  |
| 1364   | Layout 2 | `bed36aa90c9f`  |
| 1363   | Layout 2 | `bed36aa90c9f`  |
| 1360   | Layout 2 | `bed36aa90c9f`  |
| 1358   | Layout 2 | `bed36aa90c9f`  |
| 1355   | Layout 1 | `bed36aa90c9f`  |
| 1351   | Layout 1 | `bed36aa90c9f`  |
| 1348   | Layout 1 | `bed36aa90c9f`  |
| 1346   | Layout 1 | `bed36aa90c9f`  |
| 1341   | Layout 1 | `bed36aa90c9f`  |
| 1340   | Layout 1 | `bed36aa90c9f`  |
| 1338   | Layout 1 | `bed36aa90c9f`  |
| 1335   | Layout 1 | `bed36aa90c9f`  |
| 1333   | Layout 1 | `bed36aa90c9f`  |
| 1329   | Layout 1 | `bed36aa90c9f`  |
| 1327   | Layout 1 | `bed36aa90c9f`  |
| 1324   | Layout 1 | `bed36aa90c9f`  |
| 1321   | Layout 1 | `bed36aa90c9f`  |
| 1319   | Layout 1 | `bed36aa90c9f`  |
| 1318   | Layout 1 | `bed36aa90c9f`  |
| 1316   | Layout 1 | `bed36aa90c9f`  |
| 1313   | Layout 1 | `bed36aa90c9f`  |
| 1311   | Layout 1 | `bed36aa90c9f`  |
| 1309   | Layout 1 | `bed36aa90c9f`  |
| 1304   | No file  | `bed36aa90c9f`  |
| 1292   | No file  | `bed36aa90c9f`  |
| 1286   | No file  | `bed36aa90c9f`  |
| 1280   | No file  | `bed36aa90c9f`  |
| 1276   | No file  | `bed36aa90c9f`  |
| 1267   | No file  | `bed36aa90c9f`  |
| 1261   | No file  | `bed36aa90c9f`  |
| 1256   | No file  | `bed36aa90c9f`  |
| 1250   | No file  | `bed36aa90c9f`  |
| 1246   | No file  | `bed36aa90c9f`  |
| 1239   | No file  | `bed36aa90c9f`  |
| 1230   | No file  | `bed36aa90c9f`  |
| 1226   | No file  | `bed36aa90c9f`  |
| 1220   | No file  | `bed36aa90c9f`  |
| 1217   | No file  | `bed36aa90c9f`  |
| 1211   | No file  | `bed36aa90c9f`  |
| 1210   | No file  | `bed36aa90c9f`  |
| 1208   | No file  | `bed36aa90c9f`  |
| 1203   | No file  | `bed36aa90c9f`  |
| 1197   | No file  | `bed36aa90c9f`  |
| 1194   | No file  | `bed36aa90c9f`  |
| 1192   | No file  | `bed36aa90c9f`  |
| 1187   | No file  | `bed36aa90c9f`  |
| 1183   | No file  | `bed36aa90c9f`  |
| 1177   | No file  | `bed36aa90c9f`  |
| 1173   | No file  | `bed36aa90c9f`  |
| 1167   | No file  | `bed36aa90c9f`  |
| 1164   | No file  | `bed36aa90c9f`  |
| 1156   | No file  | `bed36aa90c9f`  |
| 1149   | No file  | `bed36aa90c9f`  |
| 1144   | No file  | `bed36aa90c9f`  |
| 1137   | No file  | `bed36aa90c9f`  |
| 1132   | No file  | `bed36aa90c9f`  |
| 1127   | No file  | `bed36aa90c9f`  |
| 1122   | No file  | `bed36aa90c9f`  |
| 1118   | No file  | `bed36aa90c9f`  |
| 1114   | No file  | `bed36aa90c9f`  |
| 1109   | No file  | `bed36aa90c9f`  |
| 1102   | No file  | `bed36aa90c9f`  |
| 1096   | No file  | `bed36aa90c9f`  |
| 1088   | No file  | `bed36aa90c9f`  |
| 1081   | No file  | `bed36aa90c9f`  |
| 1076   | No file  | `bed36aa90c9f`  |
| 1069   | No file  | `bed36aa90c9f`  |
| 1064   | No file  | `bed36aa90c9f`  |
| 1058   | No file  | `bed36aa90c9f`  |
| 1051   | No file  | `bed36aa90c9f`  |
| 1044   | No file  | `bed36aa90c9f`  |
| 1036   | No file  | `bed36aa90c9f`  |
| 1026   | No file  | `bed36aa90c9f`  |
| 1016   | No file  | `bed36aa90c9f`  |
| 1009   | No file  | `bed36aa90c9f`  |
| 1005   | No file  | `bed36aa90c9f`  |
| 1000   | No file  | `bed36aa90c9f`  |
| 998    | No file  | `bed36aa90c9f`  |
| 990    | No file  | `bed36aa90c9f`  |
| 979    | No file  | `bed36aa90c9f`  |
| 972    | No file  | `bed36aa90c9f`  |
| 963    | No file  | `bed36aa90c9f`  |
| 955    | No file  | `bed36aa90c9f`  |
| 946    | No file  | `bed36aa90c9f`  |
| 938    | No file  | `bed36aa90c9f`  |
| 927    | No file  | `bed36aa90c9f`  |
| 911    | No file  | `bed36aa90c9f`  |
| 904    | No file  | `bed36aa90c9f`  |
| 899    | No file  | `bed36aa90c9f`  |
| 894    | No file  | `bed36aa90c9f`  |
| 885    | No file  | `bed36aa90c9f`  |
| 879    | No file  | `bed36aa90c9f`  |
| 872    | No file  | `bed36aa90c9f`  |
| 864    | No file  | `bed36aa90c9f`  |
| 855    | No file  | `bed36aa90c9f`  |
| 853    | No file  | `bed36aa90c9f`  |
| 845    | No file  | `bed36aa90c9f`  |
| 837    | No file  | `bed36aa90c9f`  |
| 829    | No file  | `bed36aa90c9f`  |
| 822    | No file  | `bed36aa90c9f`  |
| 814    | No file  | `bed36aa90c9f`  |
| 805    | No file  | `bed36aa90c9f`  |
| 794    | No file  | `bed36aa90c9f`  |
| 787    | No file  | `bed36aa90c9f`  |
| 780    | No file  | `bed36aa90c9f`  |
| 771    | No file  | `bed36aa90c9f`  |
| 760    | No file  | `bed36aa90c9f`  |
| 748    | No file  | `bed36aa90c9f`  |
| 741    | No file  | `bed36aa90c9f`  |
| 736    | No file  | `bed36aa90c9f`  |
| 731    | No file  | `bed36aa90c9f`  |
| 723    | No file  | `bed36aa90c9f`  |
| 711    | No file  | `bed36aa90c9f`  |
| 707    | No file  | `bed36aa90c9f`  |
| 697    | No file  | `bed36aa90c9f`  |
| 689    | No file  | `bed36aa90c9f`  |
| 683    | No file  | `bed36aa90c9f`  |
| 678    | No file  | `bed36aa90c9f`  |
| 670    | No file  | `bed36aa90c9f`  |
| 661    | No file  | `bed36aa90c9f`  |
| 656    | No file  | `bed36aa90c9f`  |
| 652    | No file  | `bed36aa90c9f`  |
| 643    | No file  | `bed36aa90c9f`  |
| 637    | No file  | `bed36aa90c9f`  |
| 630    | No file  | `bed36aa90c9f`  |
| 627    | No file  | `bed36aa90c9f`  |
| 621    | No file  | `bed36aa90c9f`  |
| 617    | No file  | `bed36aa90c9f`  |
| 615    | No file  | `bed36aa90c9f`  |
| 606    | No file  | `bed36aa90c9f`  |
| 599    | No file  | `bed36aa90c9f`  |
| 592    | No file  | `bed36aa90c9f`  |
| 586    | No file  | `bed36aa90c9f`  |
| 577    | No file  | `bed36aa90c9f`  |
| 569    | No file  | `bed36aa90c9f`  |
| 561    | No file  | `bed36aa90c9f`  |
| 554    | No file  | `bed36aa90c9f`  |
| 542    | No file  | `bed36aa90c9f`  |
| 532    | No file  | `bed36aa90c9f`  |
| 531    | No file  | `bed36aa90c9f`  |
| 526    | No file  | `bed36aa90c9f`  |
| 521    | No file  | `bed36aa90c9f`  |
| 517    | No file  | `bed36aa90c9f`  |
| 510    | No file  | `bed36aa90c9f`  |
| 508    | No file  | `bed36aa90c9f`  |
| 504    | No file  | `bed36aa90c9f`  |
| 497    | No file  | `bed36aa90c9f`  |
| 491    | No file  | `bed36aa90c9f`  |
| 485    | No file  | `bed36aa90c9f`  |
| 478    | No file  | `bed36aa90c9f`  |
| 472    | No file  | `bed36aa90c9f`  |
| 466    | No file  | `bed36aa90c9f`  |
| 457    | No file  | `bed36aa90c9f`  |
| 452    | No file  | `bed36aa90c9f`  |
| 449    | No file  | `bed36aa90c9f`  |
| 435    | No file  | `bed36aa90c9f`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset                     | Type                     | Field              | Notes                                                                  |
| -------------------------- | ------------------------ | ------------------ | ---------------------------------------------------------------------- |
| `+0x00`                    | char[4]                  | magic              | ASCII `PABR`                                                           |
| `+0x04`                    | Url                      | first_url          | The URL at position `0`; see Url                                       |
| `first_url+0x00`           | Url[while url_ref != 0]  | urls               | The URLs at positions `1` and up, up to `unknown_after_urls`           |
| `urls+0x00`                | u32                      | unknown_after_urls | `0` on every client checked; the URL list has no count and ends here   |
| `urls+0x04`                | String Table             | string_table       | See String Table                                                       |
| `string_table+0x00`        | u32                      | table_start        | Offset of the string table, 4 bytes after the last URL                 |
| `string_table+0x04`        | u32                      | zero               | Always `0`                                                             |

The file stores no URL count. The string table lists its strings in
first-use order, so the first URL always reads string `0` and a later URL
reads `0` only if it repeats the first one, which no client checked does.
A reader takes `first_url`, then URLs up to the `url_ref` of `0` that
`unknown_after_urls` holds, which ends 4 bytes before `table_start`.

### Url (variable: 8 bytes + inserts)

| Offset  | Type                 | Field        | Notes                                                       |
| ------- | -------------------- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32                  | url_ref      | String table index of the URL text; the empty string for an unused position |
| `+0x04` | u32                  | insert_count | Number of insert points; `0` for the empty URL              |
| `+0x08` | Insert[insert_count] | inserts      | See Insert, in rising `insert_offset` order                 |

### Insert (5 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | insert_offset | Character offset in the URL text where the value goes in              |
| `+0x04` | u8   | insert_type   | Which value goes in, `0` to `7` without `1` on client 3482; see Insert Types |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                     |
| ------- | ------------------ | ------------ | --------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `16` on client 3482                    |
| `+0x04` | pstr[string_count] | strings      | UTF-8 URL texts in first-use order, one empty string      |

## Layout 1

### File Layout

| Offset      | Type               | Field        | Notes                                                   |
| ----------- | ------------------ | ------------ | ------------------------------------------------------- |
| `+0x00`     | char[4]            | magic        | ASCII `PABR`                                            |
| `+0x04`     | Url[..table_start] | urls         | The URLs from position `0`, up to the string table      |
| `urls+0x00` | String Table       | string_table | See String Table                                        |
| `EOF-0x08`  | u32                | table_start  | Offset of the string table, where `urls` ends           |
| `EOF-0x04`  | u32                | zero         | Always `0`                                              |

There is no `unknown_after_urls`. An unused position reads the empty
string, which is not string `0` here.

## Insert Types

Every insert point of client 3482 sits right after the text below. The
last column is the placeholder [`sha_weburl.bss`](sha_weburl_bss.md)
writes at the matching place of its Shadow Arena URLs: `{branch}` after
`https://` on every URL and `{region}` after it on the `game-*` hosts
only, as type `5` follows type `4` only on the `game-*` hosts here.

| `insert_type` | Text before the insert                               | URLs (client 3482) | Same place in `sha_weburl.bss` |
| ------------- | ---------------------------------------------------- | ------------------ | ------------------------------ |
| `0`           | `?userId=`, `?accountNo=`                            | 3                  | none                           |
| `2`           | `&sessionTicket=`                                    | 2                  | none                           |
| `3`           | `&lang=`                                             | 2                  | `{lang}` after `language=`     |
| `4`           | `https://`, on every URL                             | 16                 | `{branch}`                     |
| `5`           | `https://` after type `4`, on the `game-*` hosts     | 4                  | `{region}`                     |
| `6`           | `www.naeu.playblackdesert.com/`, before a page path  | 4                  | none                           |
| `7`           | `&userNo=`                                           | 1                  | none                           |

## URLs

Client 3482, the URL text with each insert point as `<insert_type>`:

| Position | URL                                                                                                   |
| -------- | ----------------------------------------------------------------------------------------------------- |
| `0`  | `https://<4>payment.naeu.playblackdesert.com/Pay/AcoinCharge?userId=<0>`                              |
| `1`  | `https://<4>payment.naeu.playblackdesert.com/Pay/Steam?accountNo=<0>&sessionTicket=<2>&lang=<3>`      |
| `2`  | `https://<4>www.naeu.playblackdesert.com/<6>/InGame/AdventurerNotes`                                  |
| `3`  | `https://<4><5>game-portal.naeu.playblackdesert.com/Coupon`                                           |
| `4`  | `https://<4><5>game.naeu.playblackdesert.com`                                                         |
| `5`  | `https://<4><5>game-api.naeu.playblackdesert.com`                                                     |
| `6`  | `https://<4><5>game-portal.naeu.playblackdesert.com`                                                  |
| `7`  | `https://<4>payment.naeu.playblackdesert.com`                                                         |
| `8`  | `https://<4>www.naeu.playblackdesert.com`                                                             |
| `9`  | `https://<4>www.naeu.playblackdesert.com/<6>/News/Notice/Search/`                                     |
| `10` | `https://<4>blackdesert.pearlabyss.com`                                                               |
| `11` | `https://<4>payment.naeu.playblackdesert.com/Pay/Steam/WebStorage?accountNo=<0>&userNo=<7>&sessionTicket=<2>&lang=<3>` |
| `12` | `https://<4>bdo-portal.naeu.playblackdesert.com`                                                      |
| `13` | `https://<4>www.naeu.playblackdesert.com/InGame/Banner/Index?bannerType=0&bannerPosition=`            |
| `14` | the same as position `9`                                                                                |
| `15` | empty                                                                                                 |
| `16` | `https://<4>www.naeu.playblackdesert.com/<6>/News/Detail?groupContentNo=`                             |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 has
the web URLs, and no enum of the 2016 PDB has `WebUrl` in its name. The
names follow the bytes: `url_ref` indexes the string table, and every
`insert_offset` of clients 1309, 1784, 2107, 2765 and 3482 lands at a
place where a URL takes a value (after
`https://`, after a `=` with nothing behind it, or after the host's
`/` before a page path), at most the length of its URL.

The client Lua of client 3482 reads the URLs through
`ToClient_getWebUrl(__eWebUrl_IngameWeb)` (the Arsha server application
page, `panel_arsha_applyweb_all_1.lua`),
`ToClient_getWebUrl(__eWebUrl_Notice) .. "hboost"`
(`panel_widget_menu_remake_2.lua`) and
`ToClient_getWebUrl(__eWebUrl_InGameCashWebDescUrl) .. tostring(keyword)`
(`panel_window_expiriencewiki_all_2.lua`). The `__eWebUrl_*` values are
set by the client code, so which position each one reads is open.

## Notes

- Layout 1 has no `unknown_after_urls`: its URLs run up to the string
  table, and its unused positions read the empty string, which is not
  string `0` there (`url_ref` `2` on client 1355).
- Client 1784 holds 17 URLs, client 2107 22 and client 2765 24. The
  older URLs spell the language into the path (`/en-US/Wiki?wikiNo=148`)
  where client 3482 has an insert of type `6`.
- The URL texts are those of the NA and EU client the test clients come
  from.
- The handler (`_bss/weburl/`) shows one row per URL, with the URL text
  and its insert points.

## Open Questions

### Which Value Each Insert Type Is

The insert types are named by where they sit only. Type `0` follows
`userId=` and `accountNo=`, `2` `sessionTicket=`, `3` `lang=`, `7`
`userNo=`, and `4` and `5` match the `{branch}` and `{region}`
placeholders of `sha_weburl.bss`; type `6` sits where older clients
spell the language into the path (`en-US`). No client file names the
types, and no URL of clients 1309, 1784, 2107, 2765 or 3482 has type
`1`.

### Which Position Each `__eWebUrl` Type Reads

The Lua appends `hboost` to `__eWebUrl_Notice`, which fits the
`/News/Notice/Search/` URLs at positions `9` and `14`, and a keyword to
`__eWebUrl_InGameCashWebDescUrl`. The enum values are not in the client
Lua, so the position of each type is open.

### The Value After the URLs

`unknown_after_urls` is `0` on every client checked. Whether it is the
count of a second, empty list or an end mark the reader checks is open.
