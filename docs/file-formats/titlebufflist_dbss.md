# `titlebufflist.dbss` Format

## Purpose

Stores the title collection bonus/effect list shown in-game under **Title Effects**. Each record maps a required title count threshold to the bonus effects unlocked at that tier. This file is **not** responsible for individual title name colors.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records       | Row bytes                  |
| ------ | -------------- | ------- | -------------------------- | ----- | ------------- | -------------------------- |
| 1      | 1250 and later | 3483    | `titlebufflist.dbss`       | 5,972 | 18 Block      | 140 to 410, 332 on average |
| 1      | 1250 and later | 3483    | `titlebufflistoffset.dbss` | 220   | 18 Offset Row | 12                         |

| Layout | File                       | Known           | Unknown      |
| ------ | -------------------------- | --------------- | ------------ |
| 1      | `titlebufflist.dbss`       | 5,828 B (97.6%) | 144 B (2.4%) |
| 1      | `titlebufflistoffset.dbss` | 220 B (100.0%)  | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6981208bd58f`  |
| 3482   | Layout 1 | `6981208bd58f`  |
| 3474   | Layout 1 | `6981208bd58f`  |
| 3473   | Layout 1 | `6981208bd58f`  |
| 3464   | Layout 1 | `6981208bd58f`  |
| 3458   | Layout 1 | `6981208bd58f`  |
| 3454   | Layout 1 | `6981208bd58f`  |
| 3444   | Layout 1 | `6981208bd58f`  |
| 3435   | Layout 1 | `6981208bd58f`  |
| 3426   | Layout 1 | `6981208bd58f`  |
| 3418   | Layout 1 | `6981208bd58f`  |
| 3412   | Layout 1 | `6981208bd58f`  |
| 3402   | Layout 1 | `6981208bd58f`  |
| 3396   | Layout 1 | `6981208bd58f`  |
| 3387   | Layout 1 | `6981208bd58f`  |
| 3381   | Layout 1 | `6981208bd58f`  |
| 3373   | Layout 1 | `6981208bd58f`  |
| 3364   | Layout 1 | `6981208bd58f`  |
| 3356   | Layout 1 | `6981208bd58f`  |
| 3349   | Layout 1 | `6981208bd58f`  |
| 3342   | Layout 1 | `6981208bd58f`  |
| 3335   | Layout 1 | `6981208bd58f`  |
| 3326   | Layout 1 | `6981208bd58f`  |
| 3321   | Layout 1 | `6981208bd58f`  |
| 3314   | Layout 1 | `6981208bd58f`  |
| 3303   | Layout 1 | `6981208bd58f`  |
| 3302   | Layout 1 | `6981208bd58f`  |
| 3293   | Layout 1 | `6981208bd58f`  |
| 3283   | Layout 1 | `6981208bd58f`  |
| 3275   | Layout 1 | `6981208bd58f`  |
| 3267   | Layout 1 | `6981208bd58f`  |
| 3258   | Layout 1 | `6981208bd58f`  |
| 3251   | Layout 1 | `6981208bd58f`  |
| 3242   | Layout 1 | `6981208bd58f`  |
| 3235   | Layout 1 | `6981208bd58f`  |
| 3229   | Layout 1 | `6981208bd58f`  |
| 3212   | Layout 1 | `6981208bd58f`  |
| 3203   | Layout 1 | `6981208bd58f`  |
| 3193   | Layout 1 | `6981208bd58f`  |
| 3186   | Layout 1 | `6981208bd58f`  |
| 3177   | Layout 1 | `6981208bd58f`  |
| 3169   | Layout 1 | `6981208bd58f`  |
| 3158   | Layout 1 | `6981208bd58f`  |
| 3151   | Layout 1 | `6981208bd58f`  |
| 3144   | Layout 1 | `6981208bd58f`  |
| 3133   | Layout 1 | `6981208bd58f`  |
| 3125   | Layout 1 | `6981208bd58f`  |
| 3118   | Layout 1 | `6981208bd58f`  |
| 3111   | Layout 1 | `6981208bd58f`  |
| 3103   | Layout 1 | `6981208bd58f`  |
| 3095   | Layout 1 | `6981208bd58f`  |
| 3086   | Layout 1 | `6981208bd58f`  |
| 3072   | Layout 1 | `6981208bd58f`  |
| 3062   | Layout 1 | `6981208bd58f`  |
| 3052   | Layout 1 | `6981208bd58f`  |
| 3045   | Layout 1 | `6981208bd58f`  |
| 3037   | Layout 1 | `6981208bd58f`  |
| 3030   | Layout 1 | `6981208bd58f`  |
| 3021   | Layout 1 | `6981208bd58f`  |
| 3012   | Layout 1 | `6981208bd58f`  |
| 3002   | Layout 1 | `6981208bd58f`  |
| 2995   | Layout 1 | `6981208bd58f`  |
| 2987   | Layout 1 | `6981208bd58f`  |
| 2978   | Layout 1 | `6981208bd58f`  |
| 2970   | Layout 1 | `6981208bd58f`  |
| 2959   | Layout 1 | `6981208bd58f`  |
| 2951   | Layout 1 | `6981208bd58f`  |
| 2942   | Layout 1 | `6981208bd58f`  |
| 2935   | Layout 1 | `6981208bd58f`  |
| 2932   | Layout 1 | `6981208bd58f`  |
| 2923   | Layout 1 | `6981208bd58f`  |
| 2919   | Layout 1 | `6981208bd58f`  |
| 2907   | Layout 1 | `6981208bd58f`  |
| 2900   | Layout 1 | `6981208bd58f`  |
| 2891   | Layout 1 | `6981208bd58f`  |
| 2882   | Layout 1 | `6981208bd58f`  |
| 2872   | Layout 1 | `6981208bd58f`  |
| 2863   | Layout 1 | `6981208bd58f`  |
| 2855   | Layout 1 | `6981208bd58f`  |
| 2849   | Layout 1 | `6981208bd58f`  |
| 2844   | Layout 1 | `6981208bd58f`  |
| 2834   | Layout 1 | `6981208bd58f`  |
| 2825   | Layout 1 | `6981208bd58f`  |
| 2819   | Layout 1 | `6981208bd58f`  |
| 2811   | Layout 1 | `6981208bd58f`  |
| 2803   | Layout 1 | `6981208bd58f`  |
| 2794   | Layout 1 | `6981208bd58f`  |
| 2783   | Layout 1 | `6981208bd58f`  |
| 2774   | Layout 1 | `6981208bd58f`  |
| 2765   | Layout 1 | `6981208bd58f`  |
| 2756   | Layout 1 | `6981208bd58f`  |
| 2750   | Layout 1 | `6981208bd58f`  |
| 2743   | Layout 1 | `6981208bd58f`  |
| 2736   | Layout 1 | `6981208bd58f`  |
| 2726   | Layout 1 | `6981208bd58f`  |
| 2717   | Layout 1 | `6981208bd58f`  |
| 2709   | Layout 1 | `6981208bd58f`  |
| 2703   | Layout 1 | `6981208bd58f`  |
| 2695   | Layout 1 | `6981208bd58f`  |
| 2684   | Layout 1 | `6981208bd58f`  |
| 2672   | Layout 1 | `6981208bd58f`  |
| 2665   | Layout 1 | `6981208bd58f`  |
| 2657   | Layout 1 | `6981208bd58f`  |
| 2649   | Layout 1 | `6981208bd58f`  |
| 2644   | Layout 1 | `6981208bd58f`  |
| 2637   | Layout 1 | `6981208bd58f`  |
| 2629   | Layout 1 | `6981208bd58f`  |
| 2619   | Layout 1 | `6981208bd58f`  |
| 2612   | Layout 1 | `6981208bd58f`  |
| 2606   | Layout 1 | `6981208bd58f`  |
| 2602   | Layout 1 | `6981208bd58f`  |
| 2601   | Layout 1 | `6981208bd58f`  |
| 2592   | Layout 1 | `6981208bd58f`  |
| 2583   | Layout 1 | `6981208bd58f`  |
| 2575   | Layout 1 | `6981208bd58f`  |
| 2567   | Layout 1 | `6981208bd58f`  |
| 2560   | Layout 1 | `6981208bd58f`  |
| 2553   | Layout 1 | `6981208bd58f`  |
| 2545   | Layout 1 | `6981208bd58f`  |
| 2538   | Layout 1 | `6981208bd58f`  |
| 2529   | Layout 1 | `6981208bd58f`  |
| 2519   | Layout 1 | `6981208bd58f`  |
| 2513   | Layout 1 | `6981208bd58f`  |
| 2510   | Layout 1 | `6981208bd58f`  |
| 2507   | Layout 1 | `6981208bd58f`  |
| 2503   | Layout 1 | `6981208bd58f`  |
| 2498   | Layout 1 | `6981208bd58f`  |
| 2492   | Layout 1 | `6981208bd58f`  |
| 2487   | Layout 1 | `6981208bd58f`  |
| 2480   | Layout 1 | `6981208bd58f`  |
| 2474   | Layout 1 | `6981208bd58f`  |
| 2468   | Layout 1 | `6981208bd58f`  |
| 2460   | Layout 1 | `6981208bd58f`  |
| 2453   | Layout 1 | `6981208bd58f`  |
| 2444   | Layout 1 | `6981208bd58f`  |
| 2438   | Layout 1 | `6981208bd58f`  |
| 2434   | Layout 1 | `6981208bd58f`  |
| 2429   | Layout 1 | `6981208bd58f`  |
| 2421   | Layout 1 | `6981208bd58f`  |
| 2414   | Layout 1 | `6981208bd58f`  |
| 2407   | Layout 1 | `6981208bd58f`  |
| 2401   | Layout 1 | `6981208bd58f`  |
| 2397   | Layout 1 | `6981208bd58f`  |
| 2393   | Layout 1 | `6981208bd58f`  |
| 2384   | Layout 1 | `6981208bd58f`  |
| 2378   | Layout 1 | `6981208bd58f`  |
| 2372   | Layout 1 | `6981208bd58f`  |
| 2358   | Layout 1 | `6981208bd58f`  |
| 2352   | Layout 1 | `6981208bd58f`  |
| 2347   | Layout 1 | `6981208bd58f`  |
| 2343   | Layout 1 | `6981208bd58f`  |
| 2335   | Layout 1 | `6981208bd58f`  |
| 2327   | Layout 1 | `6981208bd58f`  |
| 2324   | Layout 1 | `6981208bd58f`  |
| 2319   | Layout 1 | `6981208bd58f`  |
| 2313   | Layout 1 | `6981208bd58f`  |
| 2308   | Layout 1 | `6981208bd58f`  |
| 2302   | Layout 1 | `6981208bd58f`  |
| 2295   | Layout 1 | `6981208bd58f`  |
| 2290   | Layout 1 | `6981208bd58f`  |
| 2284   | Layout 1 | `6981208bd58f`  |
| 2276   | Layout 1 | `6981208bd58f`  |
| 2269   | Layout 1 | `6981208bd58f`  |
| 2259   | Layout 1 | `6981208bd58f`  |
| 2250   | Layout 1 | `6981208bd58f`  |
| 2243   | Layout 1 | `6981208bd58f`  |
| 2235   | Layout 1 | `6981208bd58f`  |
| 2229   | Layout 1 | `6981208bd58f`  |
| 2224   | Layout 1 | `6981208bd58f`  |
| 2218   | Layout 1 | `6981208bd58f`  |
| 2215   | Layout 1 | `6981208bd58f`  |
| 2207   | Layout 1 | `6981208bd58f`  |
| 2203   | Layout 1 | `6981208bd58f`  |
| 2196   | Layout 1 | `6981208bd58f`  |
| 2192   | Layout 1 | `6981208bd58f`  |
| 2189   | Layout 1 | `6981208bd58f`  |
| 2183   | Layout 1 | `6981208bd58f`  |
| 2179   | Layout 1 | `6981208bd58f`  |
| 2171   | Layout 1 | `6981208bd58f`  |
| 2163   | Layout 1 | `6981208bd58f`  |
| 2156   | Layout 1 | `6981208bd58f`  |
| 2151   | Layout 1 | `6981208bd58f`  |
| 2147   | Layout 1 | `6981208bd58f`  |
| 2142   | Layout 1 | `6981208bd58f`  |
| 2138   | Layout 1 | `6981208bd58f`  |
| 2134   | Layout 1 | `6981208bd58f`  |
| 2130   | Layout 1 | `6981208bd58f`  |
| 2122   | Layout 1 | `6981208bd58f`  |
| 2107   | Layout 1 | `6981208bd58f`  |
| 2098   | Layout 1 | `6981208bd58f`  |
| 2089   | Layout 1 | `6981208bd58f`  |
| 2081   | Layout 1 | `6981208bd58f`  |
| 2073   | Layout 1 | `6981208bd58f`  |
| 2067   | Layout 1 | `6981208bd58f`  |
| 2063   | Layout 1 | `6981208bd58f`  |
| 2059   | Layout 1 | `6981208bd58f`  |
| 2052   | Layout 1 | `6981208bd58f`  |
| 2044   | Layout 1 | `6981208bd58f`  |
| 2039   | Layout 1 | `6981208bd58f`  |
| 2032   | Layout 1 | `6981208bd58f`  |
| 2025   | Layout 1 | `6981208bd58f`  |
| 2011   | Layout 1 | `6981208bd58f`  |
| 2005   | Layout 1 | `6981208bd58f`  |
| 2000   | Layout 1 | `6981208bd58f`  |
| 1996   | Layout 1 | `6981208bd58f`  |
| 1991   | Layout 1 | `6981208bd58f`  |
| 1985   | Layout 1 | `6981208bd58f`  |
| 1980   | Layout 1 | `6981208bd58f`  |
| 1969   | Layout 1 | `6981208bd58f`  |
| 1964   | Layout 1 | `6981208bd58f`  |
| 1958   | Layout 1 | `6981208bd58f`  |
| 1950   | Layout 1 | `6981208bd58f`  |
| 1945   | Layout 1 | `6981208bd58f`  |
| 1937   | Layout 1 | `6981208bd58f`  |
| 1933   | Layout 1 | `6981208bd58f`  |
| 1927   | Layout 1 | `6981208bd58f`  |
| 1921   | Layout 1 | `6981208bd58f`  |
| 1914   | Layout 1 | `6981208bd58f`  |
| 1908   | Layout 1 | `6981208bd58f`  |
| 1897   | Layout 1 | `6981208bd58f`  |
| 1892   | Layout 1 | `6981208bd58f`  |
| 1886   | Layout 1 | `6981208bd58f`  |
| 1881   | Layout 1 | `6981208bd58f`  |
| 1871   | Layout 1 | `6981208bd58f`  |
| 1866   | Layout 1 | `6981208bd58f`  |
| 1862   | Layout 1 | `6981208bd58f`  |
| 1854   | Layout 1 | `6981208bd58f`  |
| 1846   | Layout 1 | `6981208bd58f`  |
| 1838   | Layout 1 | `6981208bd58f`  |
| 1832   | Layout 1 | `6981208bd58f`  |
| 1826   | Layout 1 | `6981208bd58f`  |
| 1822   | Layout 1 | `6981208bd58f`  |
| 1818   | Layout 1 | `6981208bd58f`  |
| 1804   | Layout 1 | `6981208bd58f`  |
| 1794   | Layout 1 | `6981208bd58f`  |
| 1790   | Layout 1 | `6981208bd58f`  |
| 1784   | Layout 1 | `6981208bd58f`  |
| 1774   | Layout 1 | `6981208bd58f`  |
| 1771   | Layout 1 | `6981208bd58f`  |
| 1762   | Layout 1 | `6981208bd58f`  |
| 1759   | Layout 1 | `6981208bd58f`  |
| 1754   | Layout 1 | `6981208bd58f`  |
| 1749   | Layout 1 | `6981208bd58f`  |
| 1743   | Layout 1 | `6981208bd58f`  |
| 1737   | Layout 1 | `6981208bd58f`  |
| 1731   | Layout 1 | `6981208bd58f`  |
| 1725   | Layout 1 | `6981208bd58f`  |
| 1717   | Layout 1 | `6981208bd58f`  |
| 1710   | Layout 1 | `6981208bd58f`  |
| 1704   | Layout 1 | `6981208bd58f`  |
| 1698   | Layout 1 | `6981208bd58f`  |
| 1690   | Layout 1 | `6981208bd58f`  |
| 1685   | Layout 1 | `6981208bd58f`  |
| 1680   | Layout 1 | `6981208bd58f`  |
| 1674   | Layout 1 | `6981208bd58f`  |
| 1668   | Layout 1 | `6981208bd58f`  |
| 1659   | Layout 1 | `6981208bd58f`  |
| 1649   | Layout 1 | `6981208bd58f`  |
| 1642   | Layout 1 | `6981208bd58f`  |
| 1636   | Layout 1 | `6981208bd58f`  |
| 1628   | Layout 1 | `6981208bd58f`  |
| 1622   | Layout 1 | `6981208bd58f`  |
| 1614   | Layout 1 | `6981208bd58f`  |
| 1608   | Layout 1 | `6981208bd58f`  |
| 1602   | Layout 1 | `6981208bd58f`  |
| 1598   | Layout 1 | `6981208bd58f`  |
| 1594   | Layout 1 | `6981208bd58f`  |
| 1590   | Layout 1 | `6981208bd58f`  |
| 1587   | Layout 1 | `6981208bd58f`  |
| 1584   | Layout 1 | `6981208bd58f`  |
| 1579   | Layout 1 | `6981208bd58f`  |
| 1572   | Layout 1 | `6981208bd58f`  |
| 1565   | Layout 1 | `6981208bd58f`  |
| 1559   | Layout 1 | `6981208bd58f`  |
| 1554   | Layout 1 | `6981208bd58f`  |
| 1547   | Layout 1 | `6981208bd58f`  |
| 1537   | Layout 1 | `6981208bd58f`  |
| 1529   | Layout 1 | `6981208bd58f`  |
| 1524   | Layout 1 | `6981208bd58f`  |
| 1519   | Layout 1 | `6981208bd58f`  |
| 1509   | Layout 1 | `6981208bd58f`  |
| 1506   | Layout 1 | `6981208bd58f`  |
| 1504   | Layout 1 | `6981208bd58f`  |
| 1500   | Layout 1 | `6981208bd58f`  |
| 1493   | Layout 1 | `6981208bd58f`  |
| 1489   | Layout 1 | `6981208bd58f`  |
| 1485   | Layout 1 | `6981208bd58f`  |
| 1481   | Layout 1 | `6981208bd58f`  |
| 1474   | Layout 1 | `6981208bd58f`  |
| 1466   | Layout 1 | `6981208bd58f`  |
| 1462   | Layout 1 | `6981208bd58f`  |
| 1459   | Layout 1 | `6981208bd58f`  |
| 1453   | Layout 1 | `6981208bd58f`  |
| 1450   | Layout 1 | `6981208bd58f`  |
| 1445   | Layout 1 | `6981208bd58f`  |
| 1439   | Layout 1 | `6981208bd58f`  |
| 1433   | Layout 1 | `6981208bd58f`  |
| 1430   | Layout 1 | `6981208bd58f`  |
| 1426   | Layout 1 | `6981208bd58f`  |
| 1421   | Layout 1 | `6981208bd58f`  |
| 1417   | Layout 1 | `6981208bd58f`  |
| 1416   | Layout 1 | `6981208bd58f`  |
| 1409   | Layout 1 | `6981208bd58f`  |
| 1405   | Layout 1 | `6981208bd58f`  |
| 1401   | Layout 1 | `6981208bd58f`  |
| 1396   | Layout 1 | `6981208bd58f`  |
| 1391   | Layout 1 | `6981208bd58f`  |
| 1390   | Layout 1 | `6981208bd58f`  |
| 1386   | Layout 1 | `6981208bd58f`  |
| 1381   | Layout 1 | `6981208bd58f`  |
| 1379   | Layout 1 | `6981208bd58f`  |
| 1372   | Layout 1 | `6981208bd58f`  |
| 1366   | Layout 1 | `6981208bd58f`  |
| 1364   | Layout 1 | `6981208bd58f`  |
| 1363   | Layout 1 | `6981208bd58f`  |
| 1360   | Layout 1 | `6981208bd58f`  |
| 1358   | Layout 1 | `6981208bd58f`  |
| 1355   | Layout 1 | `6981208bd58f`  |
| 1351   | Layout 1 | `6981208bd58f`  |
| 1348   | Layout 1 | `6981208bd58f`  |
| 1346   | Layout 1 | `6981208bd58f`  |
| 1341   | Layout 1 | `6981208bd58f`  |
| 1340   | Layout 1 | `6981208bd58f`  |
| 1338   | Layout 1 | `6981208bd58f`  |
| 1335   | Layout 1 | `6981208bd58f`  |
| 1333   | Layout 1 | `6981208bd58f`  |
| 1329   | Layout 1 | `6981208bd58f`  |
| 1327   | Layout 1 | `6981208bd58f`  |
| 1324   | Layout 1 | `6981208bd58f`  |
| 1321   | Layout 1 | `6981208bd58f`  |
| 1319   | Layout 1 | `6981208bd58f`  |
| 1318   | Layout 1 | `6981208bd58f`  |
| 1316   | Layout 1 | `6981208bd58f`  |
| 1313   | Layout 1 | `6981208bd58f`  |
| 1311   | Layout 1 | `6981208bd58f`  |
| 1309   | Layout 1 | `6981208bd58f`  |
| 1304   | Layout 1 | `6981208bd58f`  |
| 1292   | Layout 1 | `6981208bd58f`  |
| 1286   | Layout 1 | `6981208bd58f`  |
| 1280   | Layout 1 | `6981208bd58f`  |
| 1276   | Layout 1 | `6981208bd58f`  |
| 1267   | Layout 1 | `6981208bd58f`  |
| 1261   | Layout 1 | `6981208bd58f`  |
| 1256   | Layout 1 | `6981208bd58f`  |
| 1250   | Layout 1 | `6981208bd58f`  |
| 1246   | No file  | `6981208bd58f`  |
| 1239   | No file  | `6981208bd58f`  |
| 1230   | No file  | `6981208bd58f`  |
| 1226   | No file  | `6981208bd58f`  |
| 1220   | No file  | `6981208bd58f`  |
| 1217   | No file  | `6981208bd58f`  |
| 1211   | No file  | `6981208bd58f`  |
| 1210   | No file  | `6981208bd58f`  |
| 1208   | No file  | `6981208bd58f`  |
| 1203   | No file  | `6981208bd58f`  |
| 1197   | No file  | `6981208bd58f`  |
| 1194   | No file  | `6981208bd58f`  |
| 1192   | No file  | `6981208bd58f`  |
| 1187   | No file  | `6981208bd58f`  |
| 1183   | No file  | `6981208bd58f`  |
| 1177   | No file  | `6981208bd58f`  |
| 1173   | No file  | `6981208bd58f`  |
| 1167   | No file  | `6981208bd58f`  |
| 1164   | No file  | `6981208bd58f`  |
| 1156   | No file  | `6981208bd58f`  |
| 1149   | No file  | `6981208bd58f`  |
| 1144   | No file  | `6981208bd58f`  |
| 1137   | No file  | `6981208bd58f`  |
| 1132   | No file  | `6981208bd58f`  |
| 1127   | No file  | `6981208bd58f`  |
| 1122   | No file  | `6981208bd58f`  |
| 1118   | No file  | `6981208bd58f`  |
| 1114   | No file  | `6981208bd58f`  |
| 1109   | No file  | `6981208bd58f`  |
| 1102   | No file  | `6981208bd58f`  |
| 1096   | No file  | `6981208bd58f`  |
| 1088   | No file  | `6981208bd58f`  |
| 1081   | No file  | `6981208bd58f`  |
| 1076   | No file  | `6981208bd58f`  |
| 1069   | No file  | `6981208bd58f`  |
| 1064   | No file  | `6981208bd58f`  |
| 1058   | No file  | `6981208bd58f`  |
| 1051   | No file  | `6981208bd58f`  |
| 1044   | No file  | `6981208bd58f`  |
| 1036   | No file  | `6981208bd58f`  |
| 1026   | No file  | `6981208bd58f`  |
| 1016   | No file  | `6981208bd58f`  |
| 1009   | No file  | `6981208bd58f`  |
| 1005   | No file  | `6981208bd58f`  |
| 1000   | No file  | `6981208bd58f`  |
| 998    | No file  | `6981208bd58f`  |
| 990    | No file  | `6981208bd58f`  |
| 979    | No file  | `6981208bd58f`  |
| 972    | No file  | `6981208bd58f`  |
| 963    | No file  | `6981208bd58f`  |
| 955    | No file  | `6981208bd58f`  |
| 946    | No file  | `6981208bd58f`  |
| 938    | No file  | `6981208bd58f`  |
| 927    | No file  | `6981208bd58f`  |
| 911    | No file  | `6981208bd58f`  |
| 904    | No file  | `6981208bd58f`  |
| 899    | No file  | `6981208bd58f`  |
| 894    | No file  | `6981208bd58f`  |
| 885    | No file  | `6981208bd58f`  |
| 879    | No file  | `6981208bd58f`  |
| 872    | No file  | `6981208bd58f`  |
| 864    | No file  | `6981208bd58f`  |
| 855    | No file  | `6981208bd58f`  |
| 853    | No file  | `6981208bd58f`  |
| 845    | No file  | `6981208bd58f`  |
| 837    | No file  | `6981208bd58f`  |
| 829    | No file  | `6981208bd58f`  |
| 822    | No file  | `6981208bd58f`  |
| 814    | No file  | `6981208bd58f`  |
| 805    | No file  | `6981208bd58f`  |
| 794    | No file  | `6981208bd58f`  |
| 787    | No file  | `6981208bd58f`  |
| 780    | No file  | `6981208bd58f`  |
| 771    | No file  | `6981208bd58f`  |
| 760    | No file  | `6981208bd58f`  |
| 748    | No file  | `6981208bd58f`  |
| 741    | No file  | `6981208bd58f`  |
| 736    | No file  | `6981208bd58f`  |
| 731    | No file  | `6981208bd58f`  |
| 723    | No file  | `6981208bd58f`  |
| 711    | No file  | `6981208bd58f`  |
| 707    | No file  | `6981208bd58f`  |
| 697    | No file  | `6981208bd58f`  |
| 689    | No file  | `6981208bd58f`  |
| 683    | No file  | `6981208bd58f`  |
| 678    | No file  | `6981208bd58f`  |
| 670    | No file  | `6981208bd58f`  |
| 661    | No file  | `6981208bd58f`  |
| 656    | No file  | `6981208bd58f`  |
| 652    | No file  | `6981208bd58f`  |
| 643    | No file  | `6981208bd58f`  |
| 637    | No file  | `6981208bd58f`  |
| 630    | No file  | `6981208bd58f`  |
| 627    | No file  | `6981208bd58f`  |
| 621    | No file  | `6981208bd58f`  |
| 617    | No file  | `6981208bd58f`  |
| 615    | No file  | `6981208bd58f`  |
| 606    | No file  | `6981208bd58f`  |
| 599    | No file  | `6981208bd58f`  |
| 592    | No file  | `6981208bd58f`  |
| 586    | No file  | `6981208bd58f`  |
| 577    | No file  | `6981208bd58f`  |
| 569    | No file  | `6981208bd58f`  |
| 561    | No file  | `6981208bd58f`  |
| 554    | No file  | `6981208bd58f`  |
| 542    | No file  | `6981208bd58f`  |
| 532    | No file  | `6981208bd58f`  |
| 531    | No file  | `6981208bd58f`  |
| 526    | No file  | `6981208bd58f`  |
| 521    | No file  | `6981208bd58f`  |
| 517    | No file  | `6981208bd58f`  |
| 510    | No file  | `6981208bd58f`  |
| 508    | No file  | `6981208bd58f`  |
| 504    | No file  | `6981208bd58f`  |
| 497    | No file  | `6981208bd58f`  |
| 491    | No file  | `6981208bd58f`  |
| 485    | No file  | `6981208bd58f`  |
| 478    | No file  | `6981208bd58f`  |
| 472    | No file  | `6981208bd58f`  |
| 466    | No file  | `6981208bd58f`  |
| 457    | No file  | `6981208bd58f`  |
| 452    | No file  | `6981208bd58f`  |
| 449    | No file  | `6981208bd58f`  |
| 435    | No file  | `6981208bd58f`  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                               |
| -------------------------- | -------- | ---------------------------------- |
| `titlebufflistoffset.dbss` | Required | Provides block offsets and sizes   |
| `stringtable.bss`          | Optional | Key hash of the tooltip text in LOC, see Localised Text |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A block count, then the blocks back to back.

| Offset  | Type         | Field  | Notes                                |
| ------- | ------------ | ------ | ------------------------------------ |
| `+0x00` | u32          | count  | Number of blocks, 18 on client 3458  |
| `+0x04` | Block[count] | blocks | See Block                            |

### Block (variable: 32 bytes + texts)

| Offset             | Type  | Field           | Confidence | Notes                                                                                             |
| ------------------ | ----- | --------------- | ---------- | ------------------------------------------------------------------------------------------------- |
| `+0x00`            | u32   | internal_id     | High       | Zero-based buff/effect row ID, same as the offset file entry_id                                   |
| `+0x04`            | u32   | required_titles | High       | Title count to unlock this tier                                                                   |
| `+0x08`            | u8    | unknown_08      | High       | `1` on all 18 tiers                                                                               |
| `+0x09`            | u8    | unknown_09      | High       | `0` on all 18 tiers                                                                               |
| `+0x0A`            | u16   | unknown_0a      | High       | `58501 + internal_id` on all 18 tiers, see Open Questions                                         |
| `+0x0C`            | str16 | label_kr        | High       | Korean tier label, `칭호 50개 습득 : ` ("50 titles acquired: "); the u64 counts UTF-16 code units |
| `label_kr+0x00`    | str16 | effect_kr       | High       | Korean effects with PAColor markup, `행운 잠재력 <PAColor0xFF00BAFF>+1단계<PAOldColor>`           |
| `effect_kr+0x00`   | u32   | unknown_end     | High       | `0` on all 18 tiers; the block ends here                                                          |

Checked on all 18 blocks of client 3458: each one ends exactly after `unknown_end`. An earlier version of this doc left everything after `required_titles` as one text payload, and the parser read only from the first PAColor tag, so the Korean fallback showed just `+1단계`.

#### internal_id / Display Level

The offset file's `entry_id` and block `internal_id` identify the same row. Display level is usually `internal_id + 1`:

| Display Level | internal_id |
| ------------- | ----------- |
| 1             | 0           |
| 2             | 1           |
| 3             | 2           |

#### required_titles Examples

| internal_id | required_titles | Meaning            |
| ----------- | --------------- | ------------------ |
| 0           | 50              | Acquire x50 titles |
| 1           | 60              | Acquire x60 titles |
| 2           | 70              | Acquire x70 titles |

### `titlebufflistoffset.dbss`

| Offset  | Type              | Field | Notes          |
| ------- | ----------------- | ----- | -------------- |
| `+0x00` | u32               | count | Entry count    |
| `+0x04` | Offset Row[count] | rows  | See Offset Row |

Observed entry IDs are zero-based and align with `internal_id` inside each block.

Observed entries: 18 in the pre-2026-09-27 test fixture and in the 2026-09-27 client.

### Offset Row (12 bytes)

| Offset  | Type | Field    | Notes                                 |
| ------- | ---- | -------- | ------------------------------------- |
| `+0x00` | u32  | entry_id | Zero-based buff/effect row ID         |
| `+0x04` | u32  | offset   | Byte offset into `titlebufflist.dbss` |
| `+0x08` | u32  | size     | Block size in bytes                   |

## Embedded Korean Text

The DBSS block contains Korean text directly, `label_kr` followed by `effect_kr`:

```text
칭호 50개 습득 : 행운 잠재력 <PAColor0xFF00BAFF>+1단계<PAOldColor>
```

### PAColor Tags

Effect values use PA color markup:

```text
<PAColor0xFF00BAFF>+1단계<PAOldColor>
```

| Color      | Meaning                                           |
| ---------- | ------------------------------------------------- |
| `FF00BAFF` | Blue/cyan highlight used for numeric bonus values |

These tags color the bonus numbers in the Title Effects tooltip, not individual title name colors.

## Localised Text

The tooltip in the user's language is one multiline UI string, `GAME` sheet key `LUA_CHARACTERINFO_TITLE_TOOLTIP_DESC` (key hash `3723587620`, LOC `str_type=37`, `str_id1=3723587620`, `str_id2=1`). `stringtable.bss` gives the hash and keeps the same Korean text; `RESOURCE` key `PANEL_CHARACTERINFO_TITLE_TOOLTIP_DESC` holds a copy. Each line is one tier, in `internal_id` order (18 lines, 18 tiers):

```text
Acquire x50: Luck <PAColor0xff00baff>+1<PAOldColor>
Acquire x60: Luck <PAColor0xff00baff>+2<PAOldColor>
Acquire x70: Luck <PAColor0xff00baff>+2<PAOldColor> / Max Energy <PAColor0xff00baff>+1<PAOldColor>
```

Pick the line by `internal_id`, not by matching the `Acquire x50:` prefix, since other languages word the prefix differently.

## Reference Data

### Known Effect Progression

| Required Titles | Effects                                               |
| --------------- | ----------------------------------------------------- |
| 50              | Luck +1                                               |
| 60              | Luck +2                                               |
| 70              | Luck +2 / Max Energy +1                               |
| 80              | Luck +2 / Max Energy +2                               |
| 90              | Luck +2 / Max Energy +3                               |
| 100             | Luck +2 / Max Energy +3 / EXP +3%                     |
| 150             | Luck +3 / Max Energy +3 / EXP +3%                     |
| 200             | Luck +3 / Max Energy +4 / EXP +3%                     |
| 300             | Luck +3 / Max Energy +4 / EXP +6% / Max Stamina +50   |
| 400             | Luck +3 / Max Energy +5 / EXP +6% / Max Stamina +50   |
| 500             | Luck +3 / Max Energy +5 / EXP +9% / Max Stamina +50   |
| 600             | Luck +3 / Max Energy +5 / EXP +9% / Max Stamina +100  |
| 700             | Luck +3 / Max Energy +6 / EXP +9% / Max Stamina +100  |
| 800             | Luck +3 / Max Energy +6 / EXP +9% / Max Stamina +150  |
| 900             | Luck +3 / Max Energy +6 / EXP +12% / Max Stamina +150 |
| 1,000           | Luck +3 / Max Energy +7 / EXP +12% / Max Stamina +150 |
| 1,500           | Luck +3 / Max Energy +8 / EXP +12% / Max Stamina +150 |
| 2,000           | Luck +3 / Max Energy +8 / EXP +12% / Max Stamina +200 |

## Open Questions

### What do `unknown_08`, `unknown_09` and `unknown_0a` encode?

`unknown_0a` counts up from `58501` with the tier. Buffs `58501` to `58503` are the title Luck buffs (`(칭호) 행운 1레벨` to `3레벨`, Luck +1 to +3), but tier 3 (`58503`) gives Luck +2 / Max Energy +1, so it is not the tier's buff. `unknown_08` is always `1` and `unknown_09` always `0`.
