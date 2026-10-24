# `itemexchangetoclassmapkey.bss` Format

## Purpose

The reverse of [`itemexchangetoclass.dbss`](itemexchangetoclass_dbss.md):
every item key a weapon exchange group lists, once, with the key of its
group. Item `695113` Tuvala Longsword maps to group `165`, the Tuvala main
weapons. The plain PABR file holds the entries, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes  | Records     | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ------ | ----------- | --------- |
| 1      | 1246 and later | 3483    | `itemexchangetoclassmapkey.bss` | 36,188 | 4,521 Entry | 8         |

| Layout | File                            | Known             | Unknown    |
| ------ | ------------------------------- | ----------------- | ---------- |
| 1      | `itemexchangetoclassmapkey.bss` | 36,188 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d039106c9532`  |
| 3482   | Layout 1 | `d039106c9532`  |
| 3474   | Layout 1 | `d039106c9532`  |
| 3473   | Layout 1 | `d039106c9532`  |
| 3464   | Layout 1 | `d039106c9532`  |
| 3458   | Layout 1 | `d039106c9532`  |
| 3454   | Layout 1 | `d039106c9532`  |
| 3444   | Layout 1 | `d039106c9532`  |
| 3435   | Layout 1 | `d039106c9532`  |
| 3426   | Layout 1 | `d039106c9532`  |
| 3418   | Layout 1 | `d039106c9532`  |
| 3412   | Layout 1 | `d039106c9532`  |
| 3402   | Layout 1 | `d039106c9532`  |
| 3396   | Layout 1 | `d039106c9532`  |
| 3387   | Layout 1 | `d039106c9532`  |
| 3381   | Layout 1 | `d039106c9532`  |
| 3373   | Layout 1 | `d039106c9532`  |
| 3364   | Layout 1 | `d039106c9532`  |
| 3356   | Layout 1 | `d039106c9532`  |
| 3349   | Layout 1 | `d039106c9532`  |
| 3342   | Layout 1 | `d039106c9532`  |
| 3335   | Layout 1 | `d039106c9532`  |
| 3326   | Layout 1 | `d039106c9532`  |
| 3321   | Layout 1 | `d039106c9532`  |
| 3314   | Layout 1 | `d039106c9532`  |
| 3303   | Layout 1 | `d039106c9532`  |
| 3302   | Layout 1 | `d039106c9532`  |
| 3293   | Layout 1 | `d039106c9532`  |
| 3283   | Layout 1 | `d039106c9532`  |
| 3275   | Layout 1 | `d039106c9532`  |
| 3267   | Layout 1 | `d039106c9532`  |
| 3258   | Layout 1 | `d039106c9532`  |
| 3251   | Layout 1 | `d039106c9532`  |
| 3242   | Layout 1 | `d039106c9532`  |
| 3235   | Layout 1 | `d039106c9532`  |
| 3229   | Layout 1 | `d039106c9532`  |
| 3212   | Layout 1 | `d039106c9532`  |
| 3203   | Layout 1 | `d039106c9532`  |
| 3193   | Layout 1 | `d039106c9532`  |
| 3186   | Layout 1 | `d039106c9532`  |
| 3177   | Layout 1 | `d039106c9532`  |
| 3169   | Layout 1 | `d039106c9532`  |
| 3158   | Layout 1 | `d039106c9532`  |
| 3151   | Layout 1 | `d039106c9532`  |
| 3144   | Layout 1 | `d039106c9532`  |
| 3133   | Layout 1 | `d039106c9532`  |
| 3125   | Layout 1 | `d039106c9532`  |
| 3118   | Layout 1 | `d039106c9532`  |
| 3111   | Layout 1 | `d039106c9532`  |
| 3103   | Layout 1 | `d039106c9532`  |
| 3095   | Layout 1 | `d039106c9532`  |
| 3086   | Layout 1 | `d039106c9532`  |
| 3072   | Layout 1 | `d039106c9532`  |
| 3062   | Layout 1 | `d039106c9532`  |
| 3052   | Layout 1 | `d039106c9532`  |
| 3045   | Layout 1 | `d039106c9532`  |
| 3037   | Layout 1 | `d039106c9532`  |
| 3030   | Layout 1 | `d039106c9532`  |
| 3021   | Layout 1 | `d039106c9532`  |
| 3012   | Layout 1 | `d039106c9532`  |
| 3002   | Layout 1 | `d039106c9532`  |
| 2995   | Layout 1 | `d039106c9532`  |
| 2987   | Layout 1 | `d039106c9532`  |
| 2978   | Layout 1 | `d039106c9532`  |
| 2970   | Layout 1 | `d039106c9532`  |
| 2959   | Layout 1 | `d039106c9532`  |
| 2951   | Layout 1 | `d039106c9532`  |
| 2942   | Layout 1 | `d039106c9532`  |
| 2935   | Layout 1 | `d039106c9532`  |
| 2932   | Layout 1 | `d039106c9532`  |
| 2923   | Layout 1 | `d039106c9532`  |
| 2919   | Layout 1 | `d039106c9532`  |
| 2907   | Layout 1 | `d039106c9532`  |
| 2900   | Layout 1 | `d039106c9532`  |
| 2891   | Layout 1 | `d039106c9532`  |
| 2882   | Layout 1 | `d039106c9532`  |
| 2872   | Layout 1 | `d039106c9532`  |
| 2863   | Layout 1 | `d039106c9532`  |
| 2855   | Layout 1 | `d039106c9532`  |
| 2849   | Layout 1 | `d039106c9532`  |
| 2844   | Layout 1 | `d039106c9532`  |
| 2834   | Layout 1 | `d039106c9532`  |
| 2825   | Layout 1 | `d039106c9532`  |
| 2819   | Layout 1 | `d039106c9532`  |
| 2811   | Layout 1 | `d039106c9532`  |
| 2803   | Layout 1 | `d039106c9532`  |
| 2794   | Layout 1 | `d039106c9532`  |
| 2783   | Layout 1 | `d039106c9532`  |
| 2774   | Layout 1 | `d039106c9532`  |
| 2765   | Layout 1 | `d039106c9532`  |
| 2756   | Layout 1 | `d039106c9532`  |
| 2750   | Layout 1 | `d039106c9532`  |
| 2743   | Layout 1 | `d039106c9532`  |
| 2736   | Layout 1 | `d039106c9532`  |
| 2726   | Layout 1 | `d039106c9532`  |
| 2717   | Layout 1 | `d039106c9532`  |
| 2709   | Layout 1 | `d039106c9532`  |
| 2703   | Layout 1 | `d039106c9532`  |
| 2695   | Layout 1 | `d039106c9532`  |
| 2684   | Layout 1 | `d039106c9532`  |
| 2672   | Layout 1 | `d039106c9532`  |
| 2665   | Layout 1 | `d039106c9532`  |
| 2657   | Layout 1 | `d039106c9532`  |
| 2649   | Layout 1 | `d039106c9532`  |
| 2644   | Layout 1 | `d039106c9532`  |
| 2637   | Layout 1 | `d039106c9532`  |
| 2629   | Layout 1 | `d039106c9532`  |
| 2619   | Layout 1 | `d039106c9532`  |
| 2612   | Layout 1 | `d039106c9532`  |
| 2606   | Layout 1 | `d039106c9532`  |
| 2602   | Layout 1 | `d039106c9532`  |
| 2601   | Layout 1 | `d039106c9532`  |
| 2592   | Layout 1 | `d039106c9532`  |
| 2583   | Layout 1 | `d039106c9532`  |
| 2575   | Layout 1 | `d039106c9532`  |
| 2567   | Layout 1 | `d039106c9532`  |
| 2560   | Layout 1 | `d039106c9532`  |
| 2553   | Layout 1 | `d039106c9532`  |
| 2545   | Layout 1 | `d039106c9532`  |
| 2538   | Layout 1 | `d039106c9532`  |
| 2529   | Layout 1 | `d039106c9532`  |
| 2519   | Layout 1 | `d039106c9532`  |
| 2513   | Layout 1 | `d039106c9532`  |
| 2510   | Layout 1 | `d039106c9532`  |
| 2507   | Layout 1 | `d039106c9532`  |
| 2503   | Layout 1 | `d039106c9532`  |
| 2498   | Layout 1 | `d039106c9532`  |
| 2492   | Layout 1 | `d039106c9532`  |
| 2487   | Layout 1 | `d039106c9532`  |
| 2480   | Layout 1 | `d039106c9532`  |
| 2474   | Layout 1 | `d039106c9532`  |
| 2468   | Layout 1 | `d039106c9532`  |
| 2460   | Layout 1 | `d039106c9532`  |
| 2453   | Layout 1 | `d039106c9532`  |
| 2444   | Layout 1 | `d039106c9532`  |
| 2438   | Layout 1 | `d039106c9532`  |
| 2434   | Layout 1 | `d039106c9532`  |
| 2429   | Layout 1 | `d039106c9532`  |
| 2421   | Layout 1 | `d039106c9532`  |
| 2414   | Layout 1 | `d039106c9532`  |
| 2407   | Layout 1 | `d039106c9532`  |
| 2401   | Layout 1 | `d039106c9532`  |
| 2397   | Layout 1 | `d039106c9532`  |
| 2393   | Layout 1 | `d039106c9532`  |
| 2384   | Layout 1 | `d039106c9532`  |
| 2378   | Layout 1 | `d039106c9532`  |
| 2372   | Layout 1 | `d039106c9532`  |
| 2358   | Layout 1 | `d039106c9532`  |
| 2352   | Layout 1 | `d039106c9532`  |
| 2347   | Layout 1 | `d039106c9532`  |
| 2343   | Layout 1 | `d039106c9532`  |
| 2335   | Layout 1 | `d039106c9532`  |
| 2327   | Layout 1 | `d039106c9532`  |
| 2324   | Layout 1 | `d039106c9532`  |
| 2319   | Layout 1 | `d039106c9532`  |
| 2313   | Layout 1 | `d039106c9532`  |
| 2308   | Layout 1 | `d039106c9532`  |
| 2302   | Layout 1 | `d039106c9532`  |
| 2295   | Layout 1 | `d039106c9532`  |
| 2290   | Layout 1 | `d039106c9532`  |
| 2284   | Layout 1 | `d039106c9532`  |
| 2276   | Layout 1 | `d039106c9532`  |
| 2269   | Layout 1 | `d039106c9532`  |
| 2259   | Layout 1 | `d039106c9532`  |
| 2250   | Layout 1 | `d039106c9532`  |
| 2243   | Layout 1 | `d039106c9532`  |
| 2235   | Layout 1 | `d039106c9532`  |
| 2229   | Layout 1 | `d039106c9532`  |
| 2224   | Layout 1 | `d039106c9532`  |
| 2218   | Layout 1 | `d039106c9532`  |
| 2215   | Layout 1 | `d039106c9532`  |
| 2207   | Layout 1 | `d039106c9532`  |
| 2203   | Layout 1 | `d039106c9532`  |
| 2196   | Layout 1 | `d039106c9532`  |
| 2192   | Layout 1 | `d039106c9532`  |
| 2189   | Layout 1 | `d039106c9532`  |
| 2183   | Layout 1 | `d039106c9532`  |
| 2179   | Layout 1 | `d039106c9532`  |
| 2171   | Layout 1 | `d039106c9532`  |
| 2163   | Layout 1 | `d039106c9532`  |
| 2156   | Layout 1 | `d039106c9532`  |
| 2151   | Layout 1 | `d039106c9532`  |
| 2147   | Layout 1 | `d039106c9532`  |
| 2142   | Layout 1 | `d039106c9532`  |
| 2138   | Layout 1 | `d039106c9532`  |
| 2134   | Layout 1 | `d039106c9532`  |
| 2130   | Layout 1 | `d039106c9532`  |
| 2122   | Layout 1 | `d039106c9532`  |
| 2107   | Layout 1 | `d039106c9532`  |
| 2098   | Layout 1 | `d039106c9532`  |
| 2089   | Layout 1 | `d039106c9532`  |
| 2081   | Layout 1 | `d039106c9532`  |
| 2073   | Layout 1 | `d039106c9532`  |
| 2067   | Layout 1 | `d039106c9532`  |
| 2063   | Layout 1 | `d039106c9532`  |
| 2059   | Layout 1 | `d039106c9532`  |
| 2052   | Layout 1 | `d039106c9532`  |
| 2044   | Layout 1 | `d039106c9532`  |
| 2039   | Layout 1 | `d039106c9532`  |
| 2032   | Layout 1 | `d039106c9532`  |
| 2025   | Layout 1 | `d039106c9532`  |
| 2011   | Layout 1 | `d039106c9532`  |
| 2005   | Layout 1 | `d039106c9532`  |
| 2000   | Layout 1 | `d039106c9532`  |
| 1996   | Layout 1 | `d039106c9532`  |
| 1991   | Layout 1 | `d039106c9532`  |
| 1985   | Layout 1 | `d039106c9532`  |
| 1980   | Layout 1 | `d039106c9532`  |
| 1969   | Layout 1 | `d039106c9532`  |
| 1964   | Layout 1 | `d039106c9532`  |
| 1958   | Layout 1 | `d039106c9532`  |
| 1950   | Layout 1 | `d039106c9532`  |
| 1945   | Layout 1 | `d039106c9532`  |
| 1937   | Layout 1 | `d039106c9532`  |
| 1933   | Layout 1 | `d039106c9532`  |
| 1927   | Layout 1 | `d039106c9532`  |
| 1921   | Layout 1 | `d039106c9532`  |
| 1914   | Layout 1 | `d039106c9532`  |
| 1908   | Layout 1 | `d039106c9532`  |
| 1897   | Layout 1 | `d039106c9532`  |
| 1892   | Layout 1 | `d039106c9532`  |
| 1886   | Layout 1 | `d039106c9532`  |
| 1881   | Layout 1 | `d039106c9532`  |
| 1871   | Layout 1 | `d039106c9532`  |
| 1866   | Layout 1 | `d039106c9532`  |
| 1862   | Layout 1 | `d039106c9532`  |
| 1854   | Layout 1 | `d039106c9532`  |
| 1846   | Layout 1 | `d039106c9532`  |
| 1838   | Layout 1 | `d039106c9532`  |
| 1832   | Layout 1 | `d039106c9532`  |
| 1826   | Layout 1 | `d039106c9532`  |
| 1822   | Layout 1 | `d039106c9532`  |
| 1818   | Layout 1 | `d039106c9532`  |
| 1804   | Layout 1 | `d039106c9532`  |
| 1794   | Layout 1 | `d039106c9532`  |
| 1790   | Layout 1 | `d039106c9532`  |
| 1784   | Layout 1 | `d039106c9532`  |
| 1774   | Layout 1 | `d039106c9532`  |
| 1771   | Layout 1 | `d039106c9532`  |
| 1762   | Layout 1 | `d039106c9532`  |
| 1759   | Layout 1 | `d039106c9532`  |
| 1754   | Layout 1 | `d039106c9532`  |
| 1749   | Layout 1 | `d039106c9532`  |
| 1743   | Layout 1 | `d039106c9532`  |
| 1737   | Layout 1 | `d039106c9532`  |
| 1731   | Layout 1 | `d039106c9532`  |
| 1725   | Layout 1 | `d039106c9532`  |
| 1717   | Layout 1 | `d039106c9532`  |
| 1710   | Layout 1 | `d039106c9532`  |
| 1704   | Layout 1 | `d039106c9532`  |
| 1698   | Layout 1 | `d039106c9532`  |
| 1690   | Layout 1 | `d039106c9532`  |
| 1685   | Layout 1 | `d039106c9532`  |
| 1680   | Layout 1 | `d039106c9532`  |
| 1674   | Layout 1 | `d039106c9532`  |
| 1668   | Layout 1 | `d039106c9532`  |
| 1659   | Layout 1 | `d039106c9532`  |
| 1649   | Layout 1 | `d039106c9532`  |
| 1642   | Layout 1 | `d039106c9532`  |
| 1636   | Layout 1 | `d039106c9532`  |
| 1628   | Layout 1 | `d039106c9532`  |
| 1622   | Layout 1 | `d039106c9532`  |
| 1614   | Layout 1 | `d039106c9532`  |
| 1608   | Layout 1 | `d039106c9532`  |
| 1602   | Layout 1 | `d039106c9532`  |
| 1598   | Layout 1 | `d039106c9532`  |
| 1594   | Layout 1 | `d039106c9532`  |
| 1590   | Layout 1 | `d039106c9532`  |
| 1587   | Layout 1 | `d039106c9532`  |
| 1584   | Layout 1 | `d039106c9532`  |
| 1579   | Layout 1 | `d039106c9532`  |
| 1572   | Layout 1 | `d039106c9532`  |
| 1565   | Layout 1 | `d039106c9532`  |
| 1559   | Layout 1 | `d039106c9532`  |
| 1554   | Layout 1 | `d039106c9532`  |
| 1547   | Layout 1 | `d039106c9532`  |
| 1537   | Layout 1 | `d039106c9532`  |
| 1529   | Layout 1 | `d039106c9532`  |
| 1524   | Layout 1 | `d039106c9532`  |
| 1519   | Layout 1 | `d039106c9532`  |
| 1509   | Layout 1 | `d039106c9532`  |
| 1506   | Layout 1 | `d039106c9532`  |
| 1504   | Layout 1 | `d039106c9532`  |
| 1500   | Layout 1 | `d039106c9532`  |
| 1493   | Layout 1 | `d039106c9532`  |
| 1489   | Layout 1 | `d039106c9532`  |
| 1485   | Layout 1 | `d039106c9532`  |
| 1481   | Layout 1 | `d039106c9532`  |
| 1474   | Layout 1 | `d039106c9532`  |
| 1466   | Layout 1 | `d039106c9532`  |
| 1462   | Layout 1 | `d039106c9532`  |
| 1459   | Layout 1 | `d039106c9532`  |
| 1453   | Layout 1 | `d039106c9532`  |
| 1450   | Layout 1 | `d039106c9532`  |
| 1445   | Layout 1 | `d039106c9532`  |
| 1439   | Layout 1 | `d039106c9532`  |
| 1433   | Layout 1 | `d039106c9532`  |
| 1430   | Layout 1 | `d039106c9532`  |
| 1426   | Layout 1 | `d039106c9532`  |
| 1421   | Layout 1 | `d039106c9532`  |
| 1417   | Layout 1 | `d039106c9532`  |
| 1416   | Layout 1 | `d039106c9532`  |
| 1409   | Layout 1 | `d039106c9532`  |
| 1405   | Layout 1 | `d039106c9532`  |
| 1401   | Layout 1 | `d039106c9532`  |
| 1396   | Layout 1 | `d039106c9532`  |
| 1391   | Layout 1 | `d039106c9532`  |
| 1390   | Layout 1 | `d039106c9532`  |
| 1386   | Layout 1 | `d039106c9532`  |
| 1381   | Layout 1 | `d039106c9532`  |
| 1379   | Layout 1 | `d039106c9532`  |
| 1372   | Layout 1 | `d039106c9532`  |
| 1366   | Layout 1 | `d039106c9532`  |
| 1364   | Layout 1 | `d039106c9532`  |
| 1363   | Layout 1 | `d039106c9532`  |
| 1360   | Layout 1 | `d039106c9532`  |
| 1358   | Layout 1 | `d039106c9532`  |
| 1355   | Layout 1 | `d039106c9532`  |
| 1351   | Layout 1 | `d039106c9532`  |
| 1348   | Layout 1 | `d039106c9532`  |
| 1346   | Layout 1 | `d039106c9532`  |
| 1341   | Layout 1 | `d039106c9532`  |
| 1340   | Layout 1 | `d039106c9532`  |
| 1338   | Layout 1 | `d039106c9532`  |
| 1335   | Layout 1 | `d039106c9532`  |
| 1333   | Layout 1 | `d039106c9532`  |
| 1329   | Layout 1 | `d039106c9532`  |
| 1327   | Layout 1 | `d039106c9532`  |
| 1324   | Layout 1 | `d039106c9532`  |
| 1321   | Layout 1 | `d039106c9532`  |
| 1319   | Layout 1 | `d039106c9532`  |
| 1318   | Layout 1 | `d039106c9532`  |
| 1316   | Layout 1 | `d039106c9532`  |
| 1313   | Layout 1 | `d039106c9532`  |
| 1311   | Layout 1 | `d039106c9532`  |
| 1309   | Layout 1 | `d039106c9532`  |
| 1304   | Layout 1 | `d039106c9532`  |
| 1292   | Layout 1 | `d039106c9532`  |
| 1286   | Layout 1 | `d039106c9532`  |
| 1280   | Layout 1 | `d039106c9532`  |
| 1276   | Layout 1 | `d039106c9532`  |
| 1267   | Layout 1 | `d039106c9532`  |
| 1261   | Layout 1 | `d039106c9532`  |
| 1256   | Layout 1 | `d039106c9532`  |
| 1250   | Layout 1 | `d039106c9532`  |
| 1246   | Layout 1 | `d039106c9532`  |
| 1239   | No file  | `d039106c9532`  |
| 1230   | No file  | `d039106c9532`  |
| 1226   | No file  | `d039106c9532`  |
| 1220   | No file  | `d039106c9532`  |
| 1217   | No file  | `d039106c9532`  |
| 1211   | No file  | `d039106c9532`  |
| 1210   | No file  | `d039106c9532`  |
| 1208   | No file  | `d039106c9532`  |
| 1203   | No file  | `d039106c9532`  |
| 1197   | No file  | `d039106c9532`  |
| 1194   | No file  | `d039106c9532`  |
| 1192   | No file  | `d039106c9532`  |
| 1187   | No file  | `d039106c9532`  |
| 1183   | No file  | `d039106c9532`  |
| 1177   | No file  | `d039106c9532`  |
| 1173   | No file  | `d039106c9532`  |
| 1167   | No file  | `d039106c9532`  |
| 1164   | No file  | `d039106c9532`  |
| 1156   | No file  | `d039106c9532`  |
| 1149   | No file  | `d039106c9532`  |
| 1144   | No file  | `d039106c9532`  |
| 1137   | No file  | `d039106c9532`  |
| 1132   | No file  | `d039106c9532`  |
| 1127   | No file  | `d039106c9532`  |
| 1122   | No file  | `d039106c9532`  |
| 1118   | No file  | `d039106c9532`  |
| 1114   | No file  | `d039106c9532`  |
| 1109   | No file  | `d039106c9532`  |
| 1102   | No file  | `d039106c9532`  |
| 1096   | No file  | `d039106c9532`  |
| 1088   | No file  | `d039106c9532`  |
| 1081   | No file  | `d039106c9532`  |
| 1076   | No file  | `d039106c9532`  |
| 1069   | No file  | `d039106c9532`  |
| 1064   | No file  | `d039106c9532`  |
| 1058   | No file  | `d039106c9532`  |
| 1051   | No file  | `d039106c9532`  |
| 1044   | No file  | `d039106c9532`  |
| 1036   | No file  | `d039106c9532`  |
| 1026   | No file  | `d039106c9532`  |
| 1016   | No file  | `d039106c9532`  |
| 1009   | No file  | `d039106c9532`  |
| 1005   | No file  | `d039106c9532`  |
| 1000   | No file  | `d039106c9532`  |
| 998    | No file  | `d039106c9532`  |
| 990    | No file  | `d039106c9532`  |
| 979    | No file  | `d039106c9532`  |
| 972    | No file  | `d039106c9532`  |
| 963    | No file  | `d039106c9532`  |
| 955    | No file  | `d039106c9532`  |
| 946    | No file  | `d039106c9532`  |
| 938    | No file  | `d039106c9532`  |
| 927    | No file  | `d039106c9532`  |
| 911    | No file  | `d039106c9532`  |
| 904    | No file  | `d039106c9532`  |
| 899    | No file  | `d039106c9532`  |
| 894    | No file  | `d039106c9532`  |
| 885    | No file  | `d039106c9532`  |
| 879    | No file  | `d039106c9532`  |
| 872    | No file  | `d039106c9532`  |
| 864    | No file  | `d039106c9532`  |
| 855    | No file  | `d039106c9532`  |
| 853    | No file  | `d039106c9532`  |
| 845    | No file  | `d039106c9532`  |
| 837    | No file  | `d039106c9532`  |
| 829    | No file  | `d039106c9532`  |
| 822    | No file  | `d039106c9532`  |
| 814    | No file  | `d039106c9532`  |
| 805    | No file  | `d039106c9532`  |
| 794    | No file  | `d039106c9532`  |
| 787    | No file  | `d039106c9532`  |
| 780    | No file  | `d039106c9532`  |
| 771    | No file  | `d039106c9532`  |
| 760    | No file  | `d039106c9532`  |
| 748    | No file  | `d039106c9532`  |
| 741    | No file  | `d039106c9532`  |
| 736    | No file  | `d039106c9532`  |
| 731    | No file  | `d039106c9532`  |
| 723    | No file  | `d039106c9532`  |
| 711    | No file  | `d039106c9532`  |
| 707    | No file  | `d039106c9532`  |
| 697    | No file  | `d039106c9532`  |
| 689    | No file  | `d039106c9532`  |
| 683    | No file  | `d039106c9532`  |
| 678    | No file  | `d039106c9532`  |
| 670    | No file  | `d039106c9532`  |
| 661    | No file  | `d039106c9532`  |
| 656    | No file  | `d039106c9532`  |
| 652    | No file  | `d039106c9532`  |
| 643    | No file  | `d039106c9532`  |
| 637    | No file  | `d039106c9532`  |
| 630    | No file  | `d039106c9532`  |
| 627    | No file  | `d039106c9532`  |
| 621    | No file  | `d039106c9532`  |
| 617    | No file  | `d039106c9532`  |
| 615    | No file  | `d039106c9532`  |
| 606    | No file  | `d039106c9532`  |
| 599    | No file  | `d039106c9532`  |
| 592    | No file  | `d039106c9532`  |
| 586    | No file  | `d039106c9532`  |
| 577    | No file  | `d039106c9532`  |
| 569    | No file  | `d039106c9532`  |
| 561    | No file  | `d039106c9532`  |
| 554    | No file  | `d039106c9532`  |
| 542    | No file  | `d039106c9532`  |
| 532    | No file  | `d039106c9532`  |
| 531    | No file  | `d039106c9532`  |
| 526    | No file  | `d039106c9532`  |
| 521    | No file  | `d039106c9532`  |
| 517    | No file  | `d039106c9532`  |
| 510    | No file  | `d039106c9532`  |
| 508    | No file  | `d039106c9532`  |
| 504    | No file  | `d039106c9532`  |
| 497    | No file  | `d039106c9532`  |
| 491    | No file  | `d039106c9532`  |
| 485    | No file  | `d039106c9532`  |
| 478    | No file  | `d039106c9532`  |
| 472    | No file  | `d039106c9532`  |
| 466    | No file  | `d039106c9532`  |
| 457    | No file  | `d039106c9532`  |
| 452    | No file  | `d039106c9532`  |
| 449    | No file  | `d039106c9532`  |
| 435    | No file  | `d039106c9532`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                      |
| --------------------- | -------- | --------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item name (type `0`, `str_id1` = item ID)                 |

The handler links each `key` to its `itemexchangetoclass.dbss` row without
loading that file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                          |
| ------------------- | ------------ | ------------------ | ---------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                   |
| `+0x04`             | u32          | count              | Number of entries; `4521` on client 3474       |
| `+0x08`             | Entry[count] | entries            | See Entry                                      |
| `entries+0x00`      | String Table | string_table       | See String Table                               |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the entries end (`8 + 8 * count`) |
| `string_table+0x04` | u32          | zero               | Always `0`                                     |

The string table has the shape
[`guildhousecraftskillreverselinklist.bss`](guildhousecraftskillreverselinklist_bss.md)
and [`cutscenecharacterdata.bss`](cutscenecharacterdata_bss.md) use
(`_common/pabr_strings.py`).

### Entry (8 bytes)

| Offset  | Type | Field    | Notes                                                              |
| ------- | ---- | -------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_key | Item key (`enchant_level << 24 \| item_id`); unique                |
| `+0x04` | i32  | key      | Group, the `key` of an `itemexchangetoclass.dbss` row that lists `item_key` |

The entries follow neither the item keys nor the group rows: client 3474
starts with `745701` (group `203`), `737509` (`187`) and `930021` (`216`).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No entry reads a string                        |

## Field Names

The file is `_mapKeyFromItemKey` of the 2016
`gc::ItemExchangeToClassStaticStatusManager`, a
`pa_unordered_map<gc::ItemEnchantKey, gc::KeyType<int,0>>`: the map key is
the item, the value the i32 group key. `item_key` and `key` take their
names from [`itemexchangetoclass.dbss`](itemexchangetoclass_dbss.md)
(`_itemKey`, `_key`). No sheet of a private server's `DataSheets.bexcel` on
client 1784 names the file; it is built from the `Item_Exchange` sheet.

Inverting `itemexchangetoclass.dbss` (every filled `item_keys` slot gives
item and row key) gives exactly the items of this file, with no item
missing or extra, and every entry names a row that lists its item:

| Client | Entries | Distinct items in `itemexchangetoclass.dbss` | Items in two rows |
| ------ | ------- | -------------------------------------------- | ----------------- |
| 1784   | 2774    | 2774                                         | 0                 |
| 3474   | 4521    | 4521                                         | 2                 |

## Notes

- An item that two rows list maps to the row that comes first in
  `itemexchangetoclass.dbss`, which is also the higher key, on client 3474:
  `695193` Tuvala Pendant (rows `167` and `107`) maps to `167`, `931802`
  Ultimate Krea Clavis (rows `71` and `68`) to `71`.
- No item key carries an enhancement level on clients 1784 and 3474.
