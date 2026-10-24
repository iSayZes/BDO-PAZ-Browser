# `profiling.dbss` Format

## Purpose

Information messages grouped by profiling key: on client 3482 27 keys
with 75 messages, each a Korean text that opens with `[<subject>]에 대한
정보를 획득하였습니다.` ("Obtained information on [<subject>]") and goes on
about an NPC, a monster, a place or a game system. Three
messages carry a reward script that hands out an item. No client Lua names
the file or a getter for it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes  | Records         | Row bytes                   |
| ------ | -------------- | ------- | ---------------------- | ------ | --------------- | --------------------------- |
| 1      | 1280 and later | 3483    | `profiling.dbss`       | 23,948 | 75 Info, 27 Row | 66 to 1,766, 316 on average |
| 1      | 1280 and later | 3483    | `profilingoffset.dbss` | 274    | 27 Offset Row   | 10                          |

| Layout | File                   | Known            | Unknown      |
| ------ | ---------------------- | ---------------- | ------------ |
| 1      | `profiling.dbss`       | 23,840 B (99.5%) | 108 B (0.5%) |
| 1      | `profilingoffset.dbss` | 274 B (100.0%)   | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `77ec4cd15334`  |
| 3482   | Layout 1             | `77ec4cd15334`  |
| 3474   | Layout 1             | `77ec4cd15334`  |
| 3473   | Layout 1             | `77ec4cd15334`  |
| 3464   | Layout 1             | `77ec4cd15334`  |
| 3458   | Layout 1             | `77ec4cd15334`  |
| 3454   | Layout 1             | `77ec4cd15334`  |
| 3444   | Layout 1             | `77ec4cd15334`  |
| 3435   | Layout 1             | `77ec4cd15334`  |
| 3426   | Layout 1             | `77ec4cd15334`  |
| 3418   | Layout 1             | `77ec4cd15334`  |
| 3412   | Layout 1             | `77ec4cd15334`  |
| 3402   | Layout 1             | `77ec4cd15334`  |
| 3396   | Layout 1             | `77ec4cd15334`  |
| 3387   | Layout 1             | `77ec4cd15334`  |
| 3381   | Layout 1             | `77ec4cd15334`  |
| 3373   | Layout 1             | `77ec4cd15334`  |
| 3364   | Layout 1             | `77ec4cd15334`  |
| 3356   | Layout 1             | `77ec4cd15334`  |
| 3349   | Layout 1             | `77ec4cd15334`  |
| 3342   | Layout 1             | `77ec4cd15334`  |
| 3335   | Layout 1             | `77ec4cd15334`  |
| 3326   | Layout 1             | `77ec4cd15334`  |
| 3321   | Layout 1             | `77ec4cd15334`  |
| 3314   | Layout 1             | `77ec4cd15334`  |
| 3303   | Layout 1             | `77ec4cd15334`  |
| 3302   | Layout 1             | `77ec4cd15334`  |
| 3293   | Layout 1             | `77ec4cd15334`  |
| 3283   | Layout 1             | `77ec4cd15334`  |
| 3275   | Layout 1             | `77ec4cd15334`  |
| 3267   | Layout 1             | `77ec4cd15334`  |
| 3258   | Layout 1             | `77ec4cd15334`  |
| 3251   | Layout 1             | `77ec4cd15334`  |
| 3242   | Layout 1             | `77ec4cd15334`  |
| 3235   | Layout 1             | `77ec4cd15334`  |
| 3229   | Layout 1             | `77ec4cd15334`  |
| 3212   | Layout 1             | `77ec4cd15334`  |
| 3203   | Layout 1             | `77ec4cd15334`  |
| 3193   | Layout 1             | `77ec4cd15334`  |
| 3186   | Layout 1             | `77ec4cd15334`  |
| 3177   | Layout 1             | `77ec4cd15334`  |
| 3169   | Layout 1             | `77ec4cd15334`  |
| 3158   | Layout 1             | `77ec4cd15334`  |
| 3151   | Layout 1             | `77ec4cd15334`  |
| 3144   | Layout 1             | `77ec4cd15334`  |
| 3133   | Layout 1             | `77ec4cd15334`  |
| 3125   | Layout 1             | `77ec4cd15334`  |
| 3118   | Layout 1             | `77ec4cd15334`  |
| 3111   | Layout 1             | `77ec4cd15334`  |
| 3103   | Layout 1             | `77ec4cd15334`  |
| 3095   | Layout 1             | `77ec4cd15334`  |
| 3086   | Layout 1             | `77ec4cd15334`  |
| 3072   | Layout 1             | `77ec4cd15334`  |
| 3062   | Layout 1             | `77ec4cd15334`  |
| 3052   | Layout 1             | `77ec4cd15334`  |
| 3045   | Layout 1             | `77ec4cd15334`  |
| 3037   | Layout 1             | `77ec4cd15334`  |
| 3030   | Layout 1             | `77ec4cd15334`  |
| 3021   | Layout 1             | `77ec4cd15334`  |
| 3012   | Layout 1             | `77ec4cd15334`  |
| 3002   | Layout 1             | `77ec4cd15334`  |
| 2995   | Layout 1             | `77ec4cd15334`  |
| 2987   | Layout 1             | `77ec4cd15334`  |
| 2978   | Layout 1             | `77ec4cd15334`  |
| 2970   | Layout 1             | `77ec4cd15334`  |
| 2959   | Layout 1             | `77ec4cd15334`  |
| 2951   | Layout 1             | `77ec4cd15334`  |
| 2942   | Layout 1             | `77ec4cd15334`  |
| 2935   | Layout 1             | `77ec4cd15334`  |
| 2932   | Layout 1             | `77ec4cd15334`  |
| 2923   | Layout 1             | `77ec4cd15334`  |
| 2919   | Layout 1             | `77ec4cd15334`  |
| 2907   | Layout 1             | `77ec4cd15334`  |
| 2900   | Layout 1             | `77ec4cd15334`  |
| 2891   | Layout 1             | `77ec4cd15334`  |
| 2882   | Layout 1             | `77ec4cd15334`  |
| 2872   | Layout 1             | `77ec4cd15334`  |
| 2863   | Layout 1             | `77ec4cd15334`  |
| 2855   | Layout 1             | `77ec4cd15334`  |
| 2849   | Layout 1             | `77ec4cd15334`  |
| 2844   | Layout 1             | `77ec4cd15334`  |
| 2834   | Layout 1             | `77ec4cd15334`  |
| 2825   | Layout 1             | `77ec4cd15334`  |
| 2819   | Layout 1             | `77ec4cd15334`  |
| 2811   | Layout 1             | `77ec4cd15334`  |
| 2803   | Layout 1             | `77ec4cd15334`  |
| 2794   | Layout 1             | `77ec4cd15334`  |
| 2783   | Layout 1             | `77ec4cd15334`  |
| 2774   | Layout 1             | `77ec4cd15334`  |
| 2765   | Layout 1             | `77ec4cd15334`  |
| 2756   | Layout 1             | `77ec4cd15334`  |
| 2750   | Layout 1             | `77ec4cd15334`  |
| 2743   | Layout 1             | `77ec4cd15334`  |
| 2736   | Layout 1             | `77ec4cd15334`  |
| 2726   | Layout 1             | `77ec4cd15334`  |
| 2717   | Layout 1             | `77ec4cd15334`  |
| 2709   | Layout 1             | `77ec4cd15334`  |
| 2703   | Layout 1             | `77ec4cd15334`  |
| 2695   | Layout 1             | `77ec4cd15334`  |
| 2684   | Layout 1             | `77ec4cd15334`  |
| 2672   | Layout 1             | `77ec4cd15334`  |
| 2665   | Layout 1             | `77ec4cd15334`  |
| 2657   | Layout 1             | `77ec4cd15334`  |
| 2649   | Layout 1             | `77ec4cd15334`  |
| 2644   | Layout 1             | `77ec4cd15334`  |
| 2637   | Layout 1             | `77ec4cd15334`  |
| 2629   | Layout 1             | `77ec4cd15334`  |
| 2619   | Layout 1             | `77ec4cd15334`  |
| 2612   | Layout 1             | `77ec4cd15334`  |
| 2606   | Layout 1             | `77ec4cd15334`  |
| 2602   | Layout 1             | `77ec4cd15334`  |
| 2601   | Layout 1             | `77ec4cd15334`  |
| 2592   | Layout 1             | `77ec4cd15334`  |
| 2583   | Layout 1             | `77ec4cd15334`  |
| 2575   | Layout 1             | `77ec4cd15334`  |
| 2567   | Layout 1             | `77ec4cd15334`  |
| 2560   | Layout 1             | `77ec4cd15334`  |
| 2553   | Layout 1             | `77ec4cd15334`  |
| 2545   | Layout 1             | `77ec4cd15334`  |
| 2538   | Layout 1             | `77ec4cd15334`  |
| 2529   | Layout 1             | `77ec4cd15334`  |
| 2519   | Layout 1             | `77ec4cd15334`  |
| 2513   | Layout 1             | `77ec4cd15334`  |
| 2510   | Layout 1             | `77ec4cd15334`  |
| 2507   | Layout 1             | `77ec4cd15334`  |
| 2503   | Layout 1             | `77ec4cd15334`  |
| 2498   | Layout 1             | `77ec4cd15334`  |
| 2492   | Layout 1             | `77ec4cd15334`  |
| 2487   | Layout 1             | `77ec4cd15334`  |
| 2480   | Layout 1             | `77ec4cd15334`  |
| 2474   | Layout 1             | `77ec4cd15334`  |
| 2468   | Layout 1             | `77ec4cd15334`  |
| 2460   | Layout 1             | `77ec4cd15334`  |
| 2453   | Layout 1             | `77ec4cd15334`  |
| 2444   | Layout 1             | `77ec4cd15334`  |
| 2438   | Layout 1             | `77ec4cd15334`  |
| 2434   | Layout 1             | `77ec4cd15334`  |
| 2429   | Layout 1             | `77ec4cd15334`  |
| 2421   | Layout 1             | `77ec4cd15334`  |
| 2414   | Layout 1             | `77ec4cd15334`  |
| 2407   | Layout 1             | `77ec4cd15334`  |
| 2401   | Layout 1             | `77ec4cd15334`  |
| 2397   | Layout 1             | `77ec4cd15334`  |
| 2393   | Layout 1             | `77ec4cd15334`  |
| 2384   | Layout 1             | `77ec4cd15334`  |
| 2378   | Layout 1             | `77ec4cd15334`  |
| 2372   | Layout 1             | `77ec4cd15334`  |
| 2358   | Layout 1             | `77ec4cd15334`  |
| 2352   | Layout 1             | `77ec4cd15334`  |
| 2347   | Layout 1             | `77ec4cd15334`  |
| 2343   | Layout 1             | `77ec4cd15334`  |
| 2335   | Layout 1             | `77ec4cd15334`  |
| 2327   | Layout 1             | `77ec4cd15334`  |
| 2324   | Layout 1             | `77ec4cd15334`  |
| 2319   | Layout 1             | `77ec4cd15334`  |
| 2313   | Layout 1             | `77ec4cd15334`  |
| 2308   | Layout 1             | `77ec4cd15334`  |
| 2302   | Layout 1             | `77ec4cd15334`  |
| 2295   | Layout 1             | `77ec4cd15334`  |
| 2290   | Layout 1             | `77ec4cd15334`  |
| 2284   | Layout 1             | `77ec4cd15334`  |
| 2276   | Layout 1             | `77ec4cd15334`  |
| 2269   | Layout 1             | `77ec4cd15334`  |
| 2259   | Layout 1             | `77ec4cd15334`  |
| 2250   | Layout 1             | `77ec4cd15334`  |
| 2243   | Layout 1             | `77ec4cd15334`  |
| 2235   | Layout 1             | `77ec4cd15334`  |
| 2229   | Layout 1             | `77ec4cd15334`  |
| 2224   | Layout 1             | `77ec4cd15334`  |
| 2218   | Layout 1             | `77ec4cd15334`  |
| 2215   | Layout 1             | `77ec4cd15334`  |
| 2207   | Layout 1             | `77ec4cd15334`  |
| 2203   | Layout 1             | `77ec4cd15334`  |
| 2196   | Layout 1             | `77ec4cd15334`  |
| 2192   | Layout 1             | `77ec4cd15334`  |
| 2189   | Layout 1             | `77ec4cd15334`  |
| 2183   | Layout 1             | `77ec4cd15334`  |
| 2179   | Layout 1             | `77ec4cd15334`  |
| 2171   | Layout 1             | `77ec4cd15334`  |
| 2163   | Layout 1             | `77ec4cd15334`  |
| 2156   | Layout 1             | `77ec4cd15334`  |
| 2151   | Layout 1             | `77ec4cd15334`  |
| 2147   | Layout 1             | `77ec4cd15334`  |
| 2142   | Layout 1             | `77ec4cd15334`  |
| 2138   | Layout 1             | `77ec4cd15334`  |
| 2134   | Layout 1             | `77ec4cd15334`  |
| 2130   | Layout 1             | `77ec4cd15334`  |
| 2122   | Layout 1             | `77ec4cd15334`  |
| 2107   | Layout 1             | `77ec4cd15334`  |
| 2098   | Layout 1             | `77ec4cd15334`  |
| 2089   | Layout 1             | `77ec4cd15334`  |
| 2081   | Layout 1             | `77ec4cd15334`  |
| 2073   | Layout 1             | `77ec4cd15334`  |
| 2067   | Layout 1             | `77ec4cd15334`  |
| 2063   | Layout 1             | `77ec4cd15334`  |
| 2059   | Layout 1             | `77ec4cd15334`  |
| 2052   | Layout 1             | `77ec4cd15334`  |
| 2044   | Layout 1             | `77ec4cd15334`  |
| 2039   | Layout 1             | `77ec4cd15334`  |
| 2032   | Layout 1             | `77ec4cd15334`  |
| 2025   | Layout 1             | `77ec4cd15334`  |
| 2011   | Layout 1             | `77ec4cd15334`  |
| 2005   | Layout 1             | `77ec4cd15334`  |
| 2000   | Layout 1             | `77ec4cd15334`  |
| 1996   | Layout 1             | `77ec4cd15334`  |
| 1991   | Layout 1             | `77ec4cd15334`  |
| 1985   | Layout 1             | `77ec4cd15334`  |
| 1980   | Layout 1             | `77ec4cd15334`  |
| 1969   | Layout 1             | `77ec4cd15334`  |
| 1964   | Layout 1             | `77ec4cd15334`  |
| 1958   | Layout 1             | `77ec4cd15334`  |
| 1950   | Layout 1             | `77ec4cd15334`  |
| 1945   | Layout 1             | `77ec4cd15334`  |
| 1937   | Layout 1             | `77ec4cd15334`  |
| 1933   | Layout 1             | `77ec4cd15334`  |
| 1927   | Layout 1             | `77ec4cd15334`  |
| 1921   | Layout 1             | `77ec4cd15334`  |
| 1914   | Layout 1             | `77ec4cd15334`  |
| 1908   | Layout 1             | `77ec4cd15334`  |
| 1897   | Layout 1             | `77ec4cd15334`  |
| 1892   | Layout 1             | `77ec4cd15334`  |
| 1886   | Layout 1             | `77ec4cd15334`  |
| 1881   | Layout 1             | `77ec4cd15334`  |
| 1871   | Layout 1             | `77ec4cd15334`  |
| 1866   | Layout 1             | `77ec4cd15334`  |
| 1862   | Layout 1             | `77ec4cd15334`  |
| 1854   | Layout 1             | `77ec4cd15334`  |
| 1846   | Layout 1             | `77ec4cd15334`  |
| 1838   | Layout 1             | `77ec4cd15334`  |
| 1832   | Layout 1             | `77ec4cd15334`  |
| 1826   | Layout 1             | `77ec4cd15334`  |
| 1822   | Layout 1             | `77ec4cd15334`  |
| 1818   | Layout 1             | `77ec4cd15334`  |
| 1804   | Layout 1             | `77ec4cd15334`  |
| 1794   | Layout 1             | `77ec4cd15334`  |
| 1790   | Layout 1             | `77ec4cd15334`  |
| 1784   | Layout 1             | `77ec4cd15334`  |
| 1774   | Layout 1             | `77ec4cd15334`  |
| 1771   | Layout 1             | `77ec4cd15334`  |
| 1762   | Layout 1             | `77ec4cd15334`  |
| 1759   | Layout 1             | `77ec4cd15334`  |
| 1754   | Layout 1             | `77ec4cd15334`  |
| 1749   | Layout 1             | `77ec4cd15334`  |
| 1743   | Layout 1             | `77ec4cd15334`  |
| 1737   | Layout 1             | `77ec4cd15334`  |
| 1731   | Layout 1             | `77ec4cd15334`  |
| 1725   | Layout 1             | `77ec4cd15334`  |
| 1717   | Layout 1             | `77ec4cd15334`  |
| 1710   | Layout 1             | `77ec4cd15334`  |
| 1704   | Layout 1             | `77ec4cd15334`  |
| 1698   | Layout 1             | `77ec4cd15334`  |
| 1690   | Layout 1             | `77ec4cd15334`  |
| 1685   | Layout 1             | `77ec4cd15334`  |
| 1680   | Layout 1             | `77ec4cd15334`  |
| 1674   | Layout 1             | `77ec4cd15334`  |
| 1668   | Layout 1             | `77ec4cd15334`  |
| 1659   | Layout 1             | `77ec4cd15334`  |
| 1649   | Layout 1             | `77ec4cd15334`  |
| 1642   | Layout 1             | `77ec4cd15334`  |
| 1636   | Layout 1             | `77ec4cd15334`  |
| 1628   | Layout 1             | `77ec4cd15334`  |
| 1622   | Layout 1             | `77ec4cd15334`  |
| 1614   | Layout 1             | `77ec4cd15334`  |
| 1608   | Layout 1             | `77ec4cd15334`  |
| 1602   | Layout 1             | `77ec4cd15334`  |
| 1598   | Layout 1             | `77ec4cd15334`  |
| 1594   | Layout 1             | `77ec4cd15334`  |
| 1590   | Layout 1             | `77ec4cd15334`  |
| 1587   | Layout 1             | `77ec4cd15334`  |
| 1584   | Layout 1             | `77ec4cd15334`  |
| 1579   | Layout 1             | `77ec4cd15334`  |
| 1572   | Layout 1             | `77ec4cd15334`  |
| 1565   | Layout 1             | `77ec4cd15334`  |
| 1559   | Layout 1             | `77ec4cd15334`  |
| 1554   | Layout 1             | `77ec4cd15334`  |
| 1547   | Layout 1             | `77ec4cd15334`  |
| 1537   | Layout 1             | `77ec4cd15334`  |
| 1529   | Layout 1             | `77ec4cd15334`  |
| 1524   | Layout 1             | `77ec4cd15334`  |
| 1519   | Layout 1             | `77ec4cd15334`  |
| 1509   | Layout 1             | `77ec4cd15334`  |
| 1506   | Layout 1             | `77ec4cd15334`  |
| 1504   | Layout 1             | `77ec4cd15334`  |
| 1500   | Layout 1             | `77ec4cd15334`  |
| 1493   | Layout 1             | `77ec4cd15334`  |
| 1489   | Layout 1             | `77ec4cd15334`  |
| 1485   | Layout 1             | `77ec4cd15334`  |
| 1481   | Layout 1             | `77ec4cd15334`  |
| 1474   | Layout 1             | `77ec4cd15334`  |
| 1466   | Layout 1             | `77ec4cd15334`  |
| 1462   | Layout 1             | `77ec4cd15334`  |
| 1459   | Layout 1             | `77ec4cd15334`  |
| 1453   | Layout 1             | `77ec4cd15334`  |
| 1450   | Layout 1             | `77ec4cd15334`  |
| 1445   | Layout 1             | `77ec4cd15334`  |
| 1439   | Layout 1             | `77ec4cd15334`  |
| 1433   | Layout 1             | `77ec4cd15334`  |
| 1430   | Layout 1             | `77ec4cd15334`  |
| 1426   | Layout 1             | `77ec4cd15334`  |
| 1421   | Layout 1             | `77ec4cd15334`  |
| 1417   | Layout 1             | `77ec4cd15334`  |
| 1416   | Layout 1             | `77ec4cd15334`  |
| 1409   | Layout 1             | `77ec4cd15334`  |
| 1405   | Layout 1             | `77ec4cd15334`  |
| 1401   | Layout 1             | `77ec4cd15334`  |
| 1396   | Layout 1             | `77ec4cd15334`  |
| 1391   | Layout 1             | `77ec4cd15334`  |
| 1390   | Layout 1             | `77ec4cd15334`  |
| 1386   | Layout 1             | `77ec4cd15334`  |
| 1381   | Layout 1             | `77ec4cd15334`  |
| 1379   | Layout 1             | `77ec4cd15334`  |
| 1372   | Layout 1             | `77ec4cd15334`  |
| 1366   | Layout 1             | `77ec4cd15334`  |
| 1364   | Layout 1             | `77ec4cd15334`  |
| 1363   | Layout 1             | `77ec4cd15334`  |
| 1360   | Layout 1             | `77ec4cd15334`  |
| 1358   | Layout 1             | `77ec4cd15334`  |
| 1355   | Layout 1             | `77ec4cd15334`  |
| 1351   | Layout 1             | `77ec4cd15334`  |
| 1348   | Layout 1             | `77ec4cd15334`  |
| 1346   | Layout 1             | `77ec4cd15334`  |
| 1341   | Layout 1             | `77ec4cd15334`  |
| 1340   | Layout 1             | `77ec4cd15334`  |
| 1338   | Layout 1             | `77ec4cd15334`  |
| 1335   | Layout 1             | `77ec4cd15334`  |
| 1333   | Layout 1             | `77ec4cd15334`  |
| 1329   | Layout 1             | `77ec4cd15334`  |
| 1327   | Layout 1             | `77ec4cd15334`  |
| 1324   | Layout 1             | `77ec4cd15334`  |
| 1321   | Layout 1             | `77ec4cd15334`  |
| 1319   | Layout 1             | `77ec4cd15334`  |
| 1318   | Layout 1             | `77ec4cd15334`  |
| 1316   | Layout 1             | `77ec4cd15334`  |
| 1313   | Layout 1             | `77ec4cd15334`  |
| 1311   | Layout 1             | `77ec4cd15334`  |
| 1309   | Layout 1             | `77ec4cd15334`  |
| 1304   | Layout 1             | `77ec4cd15334`  |
| 1292   | Layout 1             | `77ec4cd15334`  |
| 1286   | Layout 1             | `77ec4cd15334`  |
| 1280   | Layout 1             | `77ec4cd15334`  |
| 1276   | No documented layout | `77ec4cd15334`  |
| 1267   | No documented layout | `77ec4cd15334`  |
| 1261   | No file              | `77ec4cd15334`  |
| 1256   | No file              | `77ec4cd15334`  |
| 1250   | No file              | `77ec4cd15334`  |
| 1246   | No file              | `77ec4cd15334`  |
| 1239   | No file              | `77ec4cd15334`  |
| 1230   | No file              | `77ec4cd15334`  |
| 1226   | No file              | `77ec4cd15334`  |
| 1220   | No file              | `77ec4cd15334`  |
| 1217   | No file              | `77ec4cd15334`  |
| 1211   | No file              | `77ec4cd15334`  |
| 1210   | No file              | `77ec4cd15334`  |
| 1208   | No file              | `77ec4cd15334`  |
| 1203   | No file              | `77ec4cd15334`  |
| 1197   | No file              | `77ec4cd15334`  |
| 1194   | No file              | `77ec4cd15334`  |
| 1192   | No file              | `77ec4cd15334`  |
| 1187   | No file              | `77ec4cd15334`  |
| 1183   | No file              | `77ec4cd15334`  |
| 1177   | No file              | `77ec4cd15334`  |
| 1173   | No file              | `77ec4cd15334`  |
| 1167   | No file              | `77ec4cd15334`  |
| 1164   | No file              | `77ec4cd15334`  |
| 1156   | No file              | `77ec4cd15334`  |
| 1149   | No file              | `77ec4cd15334`  |
| 1144   | No file              | `77ec4cd15334`  |
| 1137   | No file              | `77ec4cd15334`  |
| 1132   | No file              | `77ec4cd15334`  |
| 1127   | No file              | `77ec4cd15334`  |
| 1122   | No file              | `77ec4cd15334`  |
| 1118   | No file              | `77ec4cd15334`  |
| 1114   | No file              | `77ec4cd15334`  |
| 1109   | No file              | `77ec4cd15334`  |
| 1102   | No file              | `77ec4cd15334`  |
| 1096   | No file              | `77ec4cd15334`  |
| 1088   | No file              | `77ec4cd15334`  |
| 1081   | No file              | `77ec4cd15334`  |
| 1076   | No file              | `77ec4cd15334`  |
| 1069   | No file              | `77ec4cd15334`  |
| 1064   | No file              | `77ec4cd15334`  |
| 1058   | No file              | `77ec4cd15334`  |
| 1051   | No file              | `77ec4cd15334`  |
| 1044   | No file              | `77ec4cd15334`  |
| 1036   | No file              | `77ec4cd15334`  |
| 1026   | No file              | `77ec4cd15334`  |
| 1016   | No file              | `77ec4cd15334`  |
| 1009   | No file              | `77ec4cd15334`  |
| 1005   | No file              | `77ec4cd15334`  |
| 1000   | No file              | `77ec4cd15334`  |
| 998    | No file              | `77ec4cd15334`  |
| 990    | No file              | `77ec4cd15334`  |
| 979    | No file              | `77ec4cd15334`  |
| 972    | No file              | `77ec4cd15334`  |
| 963    | No file              | `77ec4cd15334`  |
| 955    | No file              | `77ec4cd15334`  |
| 946    | No file              | `77ec4cd15334`  |
| 938    | No file              | `77ec4cd15334`  |
| 927    | No file              | `77ec4cd15334`  |
| 911    | No file              | `77ec4cd15334`  |
| 904    | No file              | `77ec4cd15334`  |
| 899    | No file              | `77ec4cd15334`  |
| 894    | No file              | `77ec4cd15334`  |
| 885    | No file              | `77ec4cd15334`  |
| 879    | No file              | `77ec4cd15334`  |
| 872    | No file              | `77ec4cd15334`  |
| 864    | No file              | `77ec4cd15334`  |
| 855    | No file              | `77ec4cd15334`  |
| 853    | No file              | `77ec4cd15334`  |
| 845    | No file              | `77ec4cd15334`  |
| 837    | No file              | `77ec4cd15334`  |
| 829    | No file              | `77ec4cd15334`  |
| 822    | No file              | `77ec4cd15334`  |
| 814    | No file              | `77ec4cd15334`  |
| 805    | No file              | `77ec4cd15334`  |
| 794    | No file              | `77ec4cd15334`  |
| 787    | No file              | `77ec4cd15334`  |
| 780    | No file              | `77ec4cd15334`  |
| 771    | No file              | `77ec4cd15334`  |
| 760    | No file              | `77ec4cd15334`  |
| 748    | No file              | `77ec4cd15334`  |
| 741    | No file              | `77ec4cd15334`  |
| 736    | No file              | `77ec4cd15334`  |
| 731    | No file              | `77ec4cd15334`  |
| 723    | No file              | `77ec4cd15334`  |
| 711    | No file              | `77ec4cd15334`  |
| 707    | No file              | `77ec4cd15334`  |
| 697    | No file              | `77ec4cd15334`  |
| 689    | No file              | `77ec4cd15334`  |
| 683    | No file              | `77ec4cd15334`  |
| 678    | No file              | `77ec4cd15334`  |
| 670    | No file              | `77ec4cd15334`  |
| 661    | No file              | `77ec4cd15334`  |
| 656    | No file              | `77ec4cd15334`  |
| 652    | No file              | `77ec4cd15334`  |
| 643    | No file              | `77ec4cd15334`  |
| 637    | No file              | `77ec4cd15334`  |
| 630    | No file              | `77ec4cd15334`  |
| 627    | No file              | `77ec4cd15334`  |
| 621    | No file              | `77ec4cd15334`  |
| 617    | No file              | `77ec4cd15334`  |
| 615    | No file              | `77ec4cd15334`  |
| 606    | No file              | `77ec4cd15334`  |
| 599    | No file              | `77ec4cd15334`  |
| 592    | No file              | `77ec4cd15334`  |
| 586    | No file              | `77ec4cd15334`  |
| 577    | No file              | `77ec4cd15334`  |
| 569    | No file              | `77ec4cd15334`  |
| 561    | No file              | `77ec4cd15334`  |
| 554    | No file              | `77ec4cd15334`  |
| 542    | No file              | `77ec4cd15334`  |
| 532    | No file              | `77ec4cd15334`  |
| 531    | No file              | `77ec4cd15334`  |
| 526    | No file              | `77ec4cd15334`  |
| 521    | No file              | `77ec4cd15334`  |
| 517    | No file              | `77ec4cd15334`  |
| 510    | No file              | `77ec4cd15334`  |
| 508    | No file              | `77ec4cd15334`  |
| 504    | No file              | `77ec4cd15334`  |
| 497    | No file              | `77ec4cd15334`  |
| 491    | No file              | `77ec4cd15334`  |
| 485    | No file              | `77ec4cd15334`  |
| 478    | No file              | `77ec4cd15334`  |
| 472    | No file              | `77ec4cd15334`  |
| 466    | No file              | `77ec4cd15334`  |
| 457    | No file              | `77ec4cd15334`  |
| 452    | No file              | `77ec4cd15334`  |
| 449    | No file              | `77ec4cd15334`  |
| 435    | No file              | `77ec4cd15334`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role |
| ---------------------- | -------- | ---- |
| `profilingoffset.dbss` | Optional | `profiling_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type       | Field | Notes                                |
| ------- | ---------- | ----- | ------------------------------------ |
| `+0x00` | u32        | count | Number of keys; `27` on client 3482  |
| `+0x04` | Row[count] | rows  | See Row                              |

### Row (variable: 10 bytes + infos)

| Offset        | Type             | Field             | Notes |
| ------------- | ---------------- | ----------------- | ----- |
| `+0x00`       | u16              | profiling_key     | Row key: `1` to `23`, `51`, `52`, `101`, `102`, `151`, `152` and `300` on client 3482 |
| `+0x02`       | u32              | info_count        | `1` to `6`                                        |
| `+0x06`       | Info[info_count] | infos             | See Info                                          |
| `infos+0x00`  | u32              | unknown_infos_00  | `0` on every row of clients 1784 and 3482         |

### Info (variable: 16 bytes + texts)

| Offset                    | Type  | Field              | Notes |
| ------------------------- | ----- | ------------------ | ----- |
| `+0x00`                   | str16 | profile_message_kr | Korean message with `\n` line breaks |
| `profile_message_kr+0x00` | str16 | execute            | Reward script (`pushitem(34023,0,1);`, `PushItem(36014,0,1);`); empty on 72 of 75 infos |

### `profilingoffset.dbss`

Bare offset table into `profiling.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `profiling.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                           |
| ------- | ---- | ------------- | ----------------------------------------------- |
| `+0x00` | u16  | profiling_key | Key of the row it points at                     |
| `+0x02` | u32  | data_offset   | Absolute offset of the row in `profiling.dbss`  |
| `+0x06` | u32  | data_size     | Row size in bytes, `unknown_infos_00` included  |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3482 every one points at
the row with its key and the rows tile the file.

## Field Names

The 2016 `gc::ProfilingStaticStatus` is a `_key` (`u16`) and a list of
`gc::ProfilingInfo`, each a `_profileMessage`, a `_rewardsText` and the
compiled `_rewards`. The `Profiling` sheet of a private server's
`DataSheets.bexcel` on client 1784 has one row per info with the columns
`Key`, `DialogKey`, `ProfileMessage` and `Execute`: its 75 rows match the
75 infos of the client 1784 file in key, message and script, and 74 of
the 75 on client 3482 (one message was reworded). `DialogKey`
(`Profiling_Balenos_01`) is not in the file.
