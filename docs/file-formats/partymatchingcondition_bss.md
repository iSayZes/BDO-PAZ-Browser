# `partymatchingcondition.bss` Format

## Purpose

The minimum AP and DP of Atoraxxion party matching, per Atoraxxion
instance field. Two lists of the same entry shape: the first holds the
normal-difficulty fields of Vahmalkea, Sycrakea, Yolunakea and Orzekea
(`151`, `153`, `155`, `157`) on client 3474, the second the first three of
them with the same values.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records     | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | ----------- | --------- |
| 1      | 2059 and later | `partymatchingcondition.bss` | 94    | 7 Condition | 10        |

| Layout | File                         | Known        | Unknown    |
| ------ | ---------------------------- | ------------ | ---------- |
| 1      | `partymatchingcondition.bss` | 90 B (95.7%) | 4 B (4.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `632a6d301335`  |
| 3482   | Layout 1 | `632a6d301335`  |
| 3474   | Layout 1 | `632a6d301335`  |
| 3473   | Layout 1 | `632a6d301335`  |
| 3464   | Layout 1 | `632a6d301335`  |
| 3458   | Layout 1 | `632a6d301335`  |
| 3454   | Layout 1 | `632a6d301335`  |
| 3444   | Layout 1 | `632a6d301335`  |
| 3435   | Layout 1 | `632a6d301335`  |
| 3426   | Layout 1 | `632a6d301335`  |
| 3418   | Layout 1 | `632a6d301335`  |
| 3412   | Layout 1 | `632a6d301335`  |
| 3402   | Layout 1 | `632a6d301335`  |
| 3396   | Layout 1 | `632a6d301335`  |
| 3387   | Layout 1 | `632a6d301335`  |
| 3381   | Layout 1 | `632a6d301335`  |
| 3373   | Layout 1 | `632a6d301335`  |
| 3364   | Layout 1 | `632a6d301335`  |
| 3356   | Layout 1 | `632a6d301335`  |
| 3349   | Layout 1 | `632a6d301335`  |
| 3342   | Layout 1 | `632a6d301335`  |
| 3335   | Layout 1 | `632a6d301335`  |
| 3326   | Layout 1 | `632a6d301335`  |
| 3321   | Layout 1 | `632a6d301335`  |
| 3314   | Layout 1 | `632a6d301335`  |
| 3303   | Layout 1 | `632a6d301335`  |
| 3302   | Layout 1 | `632a6d301335`  |
| 3293   | Layout 1 | `632a6d301335`  |
| 3283   | Layout 1 | `632a6d301335`  |
| 3275   | Layout 1 | `632a6d301335`  |
| 3267   | Layout 1 | `632a6d301335`  |
| 3258   | Layout 1 | `632a6d301335`  |
| 3251   | Layout 1 | `632a6d301335`  |
| 3242   | Layout 1 | `632a6d301335`  |
| 3235   | Layout 1 | `632a6d301335`  |
| 3229   | Layout 1 | `632a6d301335`  |
| 3212   | Layout 1 | `632a6d301335`  |
| 3203   | Layout 1 | `632a6d301335`  |
| 3193   | Layout 1 | `632a6d301335`  |
| 3186   | Layout 1 | `632a6d301335`  |
| 3177   | Layout 1 | `632a6d301335`  |
| 3169   | Layout 1 | `632a6d301335`  |
| 3158   | Layout 1 | `632a6d301335`  |
| 3151   | Layout 1 | `632a6d301335`  |
| 3144   | Layout 1 | `632a6d301335`  |
| 3133   | Layout 1 | `632a6d301335`  |
| 3125   | Layout 1 | `632a6d301335`  |
| 3118   | Layout 1 | `632a6d301335`  |
| 3111   | Layout 1 | `632a6d301335`  |
| 3103   | Layout 1 | `632a6d301335`  |
| 3095   | Layout 1 | `632a6d301335`  |
| 3086   | Layout 1 | `632a6d301335`  |
| 3072   | Layout 1 | `632a6d301335`  |
| 3062   | Layout 1 | `632a6d301335`  |
| 3052   | Layout 1 | `632a6d301335`  |
| 3045   | Layout 1 | `632a6d301335`  |
| 3037   | Layout 1 | `632a6d301335`  |
| 3030   | Layout 1 | `632a6d301335`  |
| 3021   | Layout 1 | `632a6d301335`  |
| 3012   | Layout 1 | `632a6d301335`  |
| 3002   | Layout 1 | `632a6d301335`  |
| 2995   | Layout 1 | `632a6d301335`  |
| 2987   | Layout 1 | `632a6d301335`  |
| 2978   | Layout 1 | `632a6d301335`  |
| 2970   | Layout 1 | `632a6d301335`  |
| 2959   | Layout 1 | `632a6d301335`  |
| 2951   | Layout 1 | `632a6d301335`  |
| 2942   | Layout 1 | `632a6d301335`  |
| 2935   | Layout 1 | `632a6d301335`  |
| 2932   | Layout 1 | `632a6d301335`  |
| 2923   | Layout 1 | `632a6d301335`  |
| 2919   | Layout 1 | `632a6d301335`  |
| 2907   | Layout 1 | `632a6d301335`  |
| 2900   | Layout 1 | `632a6d301335`  |
| 2891   | Layout 1 | `632a6d301335`  |
| 2882   | Layout 1 | `632a6d301335`  |
| 2872   | Layout 1 | `632a6d301335`  |
| 2863   | Layout 1 | `632a6d301335`  |
| 2855   | Layout 1 | `632a6d301335`  |
| 2849   | Layout 1 | `632a6d301335`  |
| 2844   | Layout 1 | `632a6d301335`  |
| 2834   | Layout 1 | `632a6d301335`  |
| 2825   | Layout 1 | `632a6d301335`  |
| 2819   | Layout 1 | `632a6d301335`  |
| 2811   | Layout 1 | `632a6d301335`  |
| 2803   | Layout 1 | `632a6d301335`  |
| 2794   | Layout 1 | `632a6d301335`  |
| 2783   | Layout 1 | `632a6d301335`  |
| 2774   | Layout 1 | `632a6d301335`  |
| 2765   | Layout 1 | `632a6d301335`  |
| 2756   | Layout 1 | `632a6d301335`  |
| 2750   | Layout 1 | `632a6d301335`  |
| 2743   | Layout 1 | `632a6d301335`  |
| 2736   | Layout 1 | `632a6d301335`  |
| 2726   | Layout 1 | `632a6d301335`  |
| 2717   | Layout 1 | `632a6d301335`  |
| 2709   | Layout 1 | `632a6d301335`  |
| 2703   | Layout 1 | `632a6d301335`  |
| 2695   | Layout 1 | `632a6d301335`  |
| 2684   | Layout 1 | `632a6d301335`  |
| 2672   | Layout 1 | `632a6d301335`  |
| 2665   | Layout 1 | `632a6d301335`  |
| 2657   | Layout 1 | `632a6d301335`  |
| 2649   | Layout 1 | `632a6d301335`  |
| 2644   | Layout 1 | `632a6d301335`  |
| 2637   | Layout 1 | `632a6d301335`  |
| 2629   | Layout 1 | `632a6d301335`  |
| 2619   | Layout 1 | `632a6d301335`  |
| 2612   | Layout 1 | `632a6d301335`  |
| 2606   | Layout 1 | `632a6d301335`  |
| 2602   | Layout 1 | `632a6d301335`  |
| 2601   | Layout 1 | `632a6d301335`  |
| 2592   | Layout 1 | `632a6d301335`  |
| 2583   | Layout 1 | `632a6d301335`  |
| 2575   | Layout 1 | `632a6d301335`  |
| 2567   | Layout 1 | `632a6d301335`  |
| 2560   | Layout 1 | `632a6d301335`  |
| 2553   | Layout 1 | `632a6d301335`  |
| 2545   | Layout 1 | `632a6d301335`  |
| 2538   | Layout 1 | `632a6d301335`  |
| 2529   | Layout 1 | `632a6d301335`  |
| 2519   | Layout 1 | `632a6d301335`  |
| 2513   | Layout 1 | `632a6d301335`  |
| 2510   | Layout 1 | `632a6d301335`  |
| 2507   | Layout 1 | `632a6d301335`  |
| 2503   | Layout 1 | `632a6d301335`  |
| 2498   | Layout 1 | `632a6d301335`  |
| 2492   | Layout 1 | `632a6d301335`  |
| 2487   | Layout 1 | `632a6d301335`  |
| 2480   | Layout 1 | `632a6d301335`  |
| 2474   | Layout 1 | `632a6d301335`  |
| 2468   | Layout 1 | `632a6d301335`  |
| 2460   | Layout 1 | `632a6d301335`  |
| 2453   | Layout 1 | `632a6d301335`  |
| 2444   | Layout 1 | `632a6d301335`  |
| 2438   | Layout 1 | `632a6d301335`  |
| 2434   | Layout 1 | `632a6d301335`  |
| 2429   | Layout 1 | `632a6d301335`  |
| 2421   | Layout 1 | `632a6d301335`  |
| 2414   | Layout 1 | `632a6d301335`  |
| 2407   | Layout 1 | `632a6d301335`  |
| 2401   | Layout 1 | `632a6d301335`  |
| 2397   | Layout 1 | `632a6d301335`  |
| 2393   | Layout 1 | `632a6d301335`  |
| 2384   | Layout 1 | `632a6d301335`  |
| 2378   | Layout 1 | `632a6d301335`  |
| 2372   | Layout 1 | `632a6d301335`  |
| 2358   | Layout 1 | `632a6d301335`  |
| 2352   | Layout 1 | `632a6d301335`  |
| 2347   | Layout 1 | `632a6d301335`  |
| 2343   | Layout 1 | `632a6d301335`  |
| 2335   | Layout 1 | `632a6d301335`  |
| 2327   | Layout 1 | `632a6d301335`  |
| 2324   | Layout 1 | `632a6d301335`  |
| 2319   | Layout 1 | `632a6d301335`  |
| 2313   | Layout 1 | `632a6d301335`  |
| 2308   | Layout 1 | `632a6d301335`  |
| 2302   | Layout 1 | `632a6d301335`  |
| 2295   | Layout 1 | `632a6d301335`  |
| 2290   | Layout 1 | `632a6d301335`  |
| 2284   | Layout 1 | `632a6d301335`  |
| 2276   | Layout 1 | `632a6d301335`  |
| 2269   | Layout 1 | `632a6d301335`  |
| 2259   | Layout 1 | `632a6d301335`  |
| 2250   | Layout 1 | `632a6d301335`  |
| 2243   | Layout 1 | `632a6d301335`  |
| 2235   | Layout 1 | `632a6d301335`  |
| 2229   | Layout 1 | `632a6d301335`  |
| 2224   | Layout 1 | `632a6d301335`  |
| 2218   | Layout 1 | `632a6d301335`  |
| 2215   | Layout 1 | `632a6d301335`  |
| 2207   | Layout 1 | `632a6d301335`  |
| 2203   | Layout 1 | `632a6d301335`  |
| 2196   | Layout 1 | `632a6d301335`  |
| 2192   | Layout 1 | `632a6d301335`  |
| 2189   | Layout 1 | `632a6d301335`  |
| 2183   | Layout 1 | `632a6d301335`  |
| 2179   | Layout 1 | `632a6d301335`  |
| 2171   | Layout 1 | `632a6d301335`  |
| 2163   | Layout 1 | `632a6d301335`  |
| 2156   | Layout 1 | `632a6d301335`  |
| 2151   | Layout 1 | `632a6d301335`  |
| 2147   | Layout 1 | `632a6d301335`  |
| 2142   | Layout 1 | `632a6d301335`  |
| 2138   | Layout 1 | `632a6d301335`  |
| 2134   | Layout 1 | `632a6d301335`  |
| 2130   | Layout 1 | `632a6d301335`  |
| 2122   | Layout 1 | `632a6d301335`  |
| 2107   | Layout 1 | `632a6d301335`  |
| 2098   | Layout 1 | `632a6d301335`  |
| 2089   | Layout 1 | `632a6d301335`  |
| 2081   | Layout 1 | `632a6d301335`  |
| 2073   | Layout 1 | `632a6d301335`  |
| 2067   | Layout 1 | `632a6d301335`  |
| 2063   | Layout 1 | `632a6d301335`  |
| 2059   | Layout 1 | `632a6d301335`  |
| 2052   | No file  | `632a6d301335`  |
| 2044   | No file  | `632a6d301335`  |
| 2039   | No file  | `632a6d301335`  |
| 2032   | No file  | `632a6d301335`  |
| 2025   | No file  | `632a6d301335`  |
| 2011   | No file  | `632a6d301335`  |
| 2005   | No file  | `632a6d301335`  |
| 2000   | No file  | `632a6d301335`  |
| 1996   | No file  | `632a6d301335`  |
| 1991   | No file  | `632a6d301335`  |
| 1985   | No file  | `632a6d301335`  |
| 1980   | No file  | `632a6d301335`  |
| 1969   | No file  | `632a6d301335`  |
| 1964   | No file  | `632a6d301335`  |
| 1958   | No file  | `632a6d301335`  |
| 1950   | No file  | `632a6d301335`  |
| 1945   | No file  | `632a6d301335`  |
| 1937   | No file  | `632a6d301335`  |
| 1933   | No file  | `632a6d301335`  |
| 1927   | No file  | `632a6d301335`  |
| 1921   | No file  | `632a6d301335`  |
| 1914   | No file  | `632a6d301335`  |
| 1908   | No file  | `632a6d301335`  |
| 1897   | No file  | `632a6d301335`  |
| 1892   | No file  | `632a6d301335`  |
| 1886   | No file  | `632a6d301335`  |
| 1881   | No file  | `632a6d301335`  |
| 1871   | No file  | `632a6d301335`  |
| 1866   | No file  | `632a6d301335`  |
| 1862   | No file  | `632a6d301335`  |
| 1854   | No file  | `632a6d301335`  |
| 1846   | No file  | `632a6d301335`  |
| 1838   | No file  | `632a6d301335`  |
| 1832   | No file  | `632a6d301335`  |
| 1826   | No file  | `632a6d301335`  |
| 1822   | No file  | `632a6d301335`  |
| 1818   | No file  | `632a6d301335`  |
| 1804   | No file  | `632a6d301335`  |
| 1794   | No file  | `632a6d301335`  |
| 1790   | No file  | `632a6d301335`  |
| 1784   | No file  | `632a6d301335`  |
| 1774   | No file  | `632a6d301335`  |
| 1771   | No file  | `632a6d301335`  |
| 1762   | No file  | `632a6d301335`  |
| 1759   | No file  | `632a6d301335`  |
| 1754   | No file  | `632a6d301335`  |
| 1749   | No file  | `632a6d301335`  |
| 1743   | No file  | `632a6d301335`  |
| 1737   | No file  | `632a6d301335`  |
| 1731   | No file  | `632a6d301335`  |
| 1725   | No file  | `632a6d301335`  |
| 1717   | No file  | `632a6d301335`  |
| 1710   | No file  | `632a6d301335`  |
| 1704   | No file  | `632a6d301335`  |
| 1698   | No file  | `632a6d301335`  |
| 1690   | No file  | `632a6d301335`  |
| 1685   | No file  | `632a6d301335`  |
| 1680   | No file  | `632a6d301335`  |
| 1674   | No file  | `632a6d301335`  |
| 1668   | No file  | `632a6d301335`  |
| 1659   | No file  | `632a6d301335`  |
| 1649   | No file  | `632a6d301335`  |
| 1642   | No file  | `632a6d301335`  |
| 1636   | No file  | `632a6d301335`  |
| 1628   | No file  | `632a6d301335`  |
| 1622   | No file  | `632a6d301335`  |
| 1614   | No file  | `632a6d301335`  |
| 1608   | No file  | `632a6d301335`  |
| 1602   | No file  | `632a6d301335`  |
| 1598   | No file  | `632a6d301335`  |
| 1594   | No file  | `632a6d301335`  |
| 1590   | No file  | `632a6d301335`  |
| 1587   | No file  | `632a6d301335`  |
| 1584   | No file  | `632a6d301335`  |
| 1579   | No file  | `632a6d301335`  |
| 1572   | No file  | `632a6d301335`  |
| 1565   | No file  | `632a6d301335`  |
| 1559   | No file  | `632a6d301335`  |
| 1554   | No file  | `632a6d301335`  |
| 1547   | No file  | `632a6d301335`  |
| 1537   | No file  | `632a6d301335`  |
| 1529   | No file  | `632a6d301335`  |
| 1524   | No file  | `632a6d301335`  |
| 1519   | No file  | `632a6d301335`  |
| 1509   | No file  | `632a6d301335`  |
| 1506   | No file  | `632a6d301335`  |
| 1504   | No file  | `632a6d301335`  |
| 1500   | No file  | `632a6d301335`  |
| 1493   | No file  | `632a6d301335`  |
| 1489   | No file  | `632a6d301335`  |
| 1485   | No file  | `632a6d301335`  |
| 1481   | No file  | `632a6d301335`  |
| 1474   | No file  | `632a6d301335`  |
| 1466   | No file  | `632a6d301335`  |
| 1462   | No file  | `632a6d301335`  |
| 1459   | No file  | `632a6d301335`  |
| 1453   | No file  | `632a6d301335`  |
| 1450   | No file  | `632a6d301335`  |
| 1445   | No file  | `632a6d301335`  |
| 1439   | No file  | `632a6d301335`  |
| 1433   | No file  | `632a6d301335`  |
| 1430   | No file  | `632a6d301335`  |
| 1426   | No file  | `632a6d301335`  |
| 1421   | No file  | `632a6d301335`  |
| 1417   | No file  | `632a6d301335`  |
| 1416   | No file  | `632a6d301335`  |
| 1409   | No file  | `632a6d301335`  |
| 1405   | No file  | `632a6d301335`  |
| 1401   | No file  | `632a6d301335`  |
| 1396   | No file  | `632a6d301335`  |
| 1391   | No file  | `632a6d301335`  |
| 1390   | No file  | `632a6d301335`  |
| 1386   | No file  | `632a6d301335`  |
| 1381   | No file  | `632a6d301335`  |
| 1379   | No file  | `632a6d301335`  |
| 1372   | No file  | `632a6d301335`  |
| 1366   | No file  | `632a6d301335`  |
| 1364   | No file  | `632a6d301335`  |
| 1363   | No file  | `632a6d301335`  |
| 1360   | No file  | `632a6d301335`  |
| 1358   | No file  | `632a6d301335`  |
| 1355   | No file  | `632a6d301335`  |
| 1351   | No file  | `632a6d301335`  |
| 1348   | No file  | `632a6d301335`  |
| 1346   | No file  | `632a6d301335`  |
| 1341   | No file  | `632a6d301335`  |
| 1340   | No file  | `632a6d301335`  |
| 1338   | No file  | `632a6d301335`  |
| 1335   | No file  | `632a6d301335`  |
| 1333   | No file  | `632a6d301335`  |
| 1329   | No file  | `632a6d301335`  |
| 1327   | No file  | `632a6d301335`  |
| 1324   | No file  | `632a6d301335`  |
| 1321   | No file  | `632a6d301335`  |
| 1319   | No file  | `632a6d301335`  |
| 1318   | No file  | `632a6d301335`  |
| 1316   | No file  | `632a6d301335`  |
| 1313   | No file  | `632a6d301335`  |
| 1311   | No file  | `632a6d301335`  |
| 1309   | No file  | `632a6d301335`  |
| 1304   | No file  | `632a6d301335`  |
| 1292   | No file  | `632a6d301335`  |
| 1286   | No file  | `632a6d301335`  |
| 1280   | No file  | `632a6d301335`  |
| 1276   | No file  | `632a6d301335`  |
| 1267   | No file  | `632a6d301335`  |
| 1261   | No file  | `632a6d301335`  |
| 1256   | No file  | `632a6d301335`  |
| 1250   | No file  | `632a6d301335`  |
| 1246   | No file  | `632a6d301335`  |
| 1239   | No file  | `632a6d301335`  |
| 1230   | No file  | `632a6d301335`  |
| 1226   | No file  | `632a6d301335`  |
| 1220   | No file  | `632a6d301335`  |
| 1217   | No file  | `632a6d301335`  |
| 1211   | No file  | `632a6d301335`  |
| 1210   | No file  | `632a6d301335`  |
| 1208   | No file  | `632a6d301335`  |
| 1203   | No file  | `632a6d301335`  |
| 1197   | No file  | `632a6d301335`  |
| 1194   | No file  | `632a6d301335`  |
| 1192   | No file  | `632a6d301335`  |
| 1187   | No file  | `632a6d301335`  |
| 1183   | No file  | `632a6d301335`  |
| 1177   | No file  | `632a6d301335`  |
| 1173   | No file  | `632a6d301335`  |
| 1167   | No file  | `632a6d301335`  |
| 1164   | No file  | `632a6d301335`  |
| 1156   | No file  | `632a6d301335`  |
| 1149   | No file  | `632a6d301335`  |
| 1144   | No file  | `632a6d301335`  |
| 1137   | No file  | `632a6d301335`  |
| 1132   | No file  | `632a6d301335`  |
| 1127   | No file  | `632a6d301335`  |
| 1122   | No file  | `632a6d301335`  |
| 1118   | No file  | `632a6d301335`  |
| 1114   | No file  | `632a6d301335`  |
| 1109   | No file  | `632a6d301335`  |
| 1102   | No file  | `632a6d301335`  |
| 1096   | No file  | `632a6d301335`  |
| 1088   | No file  | `632a6d301335`  |
| 1081   | No file  | `632a6d301335`  |
| 1076   | No file  | `632a6d301335`  |
| 1069   | No file  | `632a6d301335`  |
| 1064   | No file  | `632a6d301335`  |
| 1058   | No file  | `632a6d301335`  |
| 1051   | No file  | `632a6d301335`  |
| 1044   | No file  | `632a6d301335`  |
| 1036   | No file  | `632a6d301335`  |
| 1026   | No file  | `632a6d301335`  |
| 1016   | No file  | `632a6d301335`  |
| 1009   | No file  | `632a6d301335`  |
| 1005   | No file  | `632a6d301335`  |
| 1000   | No file  | `632a6d301335`  |
| 998    | No file  | `632a6d301335`  |
| 990    | No file  | `632a6d301335`  |
| 979    | No file  | `632a6d301335`  |
| 972    | No file  | `632a6d301335`  |
| 963    | No file  | `632a6d301335`  |
| 955    | No file  | `632a6d301335`  |
| 946    | No file  | `632a6d301335`  |
| 938    | No file  | `632a6d301335`  |
| 927    | No file  | `632a6d301335`  |
| 911    | No file  | `632a6d301335`  |
| 904    | No file  | `632a6d301335`  |
| 899    | No file  | `632a6d301335`  |
| 894    | No file  | `632a6d301335`  |
| 885    | No file  | `632a6d301335`  |
| 879    | No file  | `632a6d301335`  |
| 872    | No file  | `632a6d301335`  |
| 864    | No file  | `632a6d301335`  |
| 855    | No file  | `632a6d301335`  |
| 853    | No file  | `632a6d301335`  |
| 845    | No file  | `632a6d301335`  |
| 837    | No file  | `632a6d301335`  |
| 829    | No file  | `632a6d301335`  |
| 822    | No file  | `632a6d301335`  |
| 814    | No file  | `632a6d301335`  |
| 805    | No file  | `632a6d301335`  |
| 794    | No file  | `632a6d301335`  |
| 787    | No file  | `632a6d301335`  |
| 780    | No file  | `632a6d301335`  |
| 771    | No file  | `632a6d301335`  |
| 760    | No file  | `632a6d301335`  |
| 748    | No file  | `632a6d301335`  |
| 741    | No file  | `632a6d301335`  |
| 736    | No file  | `632a6d301335`  |
| 731    | No file  | `632a6d301335`  |
| 723    | No file  | `632a6d301335`  |
| 711    | No file  | `632a6d301335`  |
| 707    | No file  | `632a6d301335`  |
| 697    | No file  | `632a6d301335`  |
| 689    | No file  | `632a6d301335`  |
| 683    | No file  | `632a6d301335`  |
| 678    | No file  | `632a6d301335`  |
| 670    | No file  | `632a6d301335`  |
| 661    | No file  | `632a6d301335`  |
| 656    | No file  | `632a6d301335`  |
| 652    | No file  | `632a6d301335`  |
| 643    | No file  | `632a6d301335`  |
| 637    | No file  | `632a6d301335`  |
| 630    | No file  | `632a6d301335`  |
| 627    | No file  | `632a6d301335`  |
| 621    | No file  | `632a6d301335`  |
| 617    | No file  | `632a6d301335`  |
| 615    | No file  | `632a6d301335`  |
| 606    | No file  | `632a6d301335`  |
| 599    | No file  | `632a6d301335`  |
| 592    | No file  | `632a6d301335`  |
| 586    | No file  | `632a6d301335`  |
| 577    | No file  | `632a6d301335`  |
| 569    | No file  | `632a6d301335`  |
| 561    | No file  | `632a6d301335`  |
| 554    | No file  | `632a6d301335`  |
| 542    | No file  | `632a6d301335`  |
| 532    | No file  | `632a6d301335`  |
| 531    | No file  | `632a6d301335`  |
| 526    | No file  | `632a6d301335`  |
| 521    | No file  | `632a6d301335`  |
| 517    | No file  | `632a6d301335`  |
| 510    | No file  | `632a6d301335`  |
| 508    | No file  | `632a6d301335`  |
| 504    | No file  | `632a6d301335`  |
| 497    | No file  | `632a6d301335`  |
| 491    | No file  | `632a6d301335`  |
| 485    | No file  | `632a6d301335`  |
| 478    | No file  | `632a6d301335`  |
| 472    | No file  | `632a6d301335`  |
| 466    | No file  | `632a6d301335`  |
| 457    | No file  | `632a6d301335`  |
| 452    | No file  | `632a6d301335`  |
| 449    | No file  | `632a6d301335`  |
| 435    | No file  | `632a6d301335`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone; the instance field names come from
the `instancefield.dbss` lookup index the app loads at start.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                       | Type                                   | Field                    | Notes                                                       |
| ---------------------------- | -------------------------------------- | ------------------------ | ----------------------------------------------------------- |
| `+0x00`                      | char[4]                                | magic                    | ASCII `PABR`                                                |
| `+0x04`                      | u32                                    | matching_condition_count | Number of `matching_conditions`                             |
| `+0x08`                      | Condition[matching_condition_count]    | matching_conditions      | See Condition; 4 entries on client 3474                     |
| `matching_conditions+0x00`   | u32                                    | unknown_condition_count  | Number of `unknown_conditions`                              |
| `matching_conditions+0x04`   | Condition[unknown_condition_count]     | unknown_conditions       | See Condition; 3 entries on client 3474; see Open Questions |
| `unknown_conditions+0x00`    | String Table                           | string_table             | See String Table                                            |
| `string_table+0x00`          | u32                                    | table_start              | Offset of the string table, where `unknown_conditions` ends |
| `string_table+0x04`          | u32                                    | zero                     | Always `0`                                                  |

### Condition (10 bytes)

| Offset  | Type | Field              | Notes                                                                        |
| ------- | ---- | ------------------ | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | instance_field_key | `instancefield.dbss` key: `151` `Atoraxion_Desert_EZ`, `153` `Atoraxion_SEA_EZ`, `155` `Atoraxion_Jungle_EZ`, `157` `Atoraxion_Thorn_EZ` |
| `+0x02` | u32  | min_ap             | Minimum AP; `220`, `300` for `157` (client 3474)                             |
| `+0x06` | u32  | min_dp             | Minimum DP; `270`, `380` for `157` (client 3474)                             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 covers
the file, which client 1784 does not ship. `instance_field_key` follows
`instancefield.dbss`: the four keys are the odd keys of the Atoraxxion
fields `150` to `157`, the `_EZ` ones, and the party matching window
(`panel_partycontentsrecurit.luac`) offers the same four Atoraxxion kinds
(`__ePartyContentsType_AtoraxionDesert`, `...Sea`, `...Velly`,
`...Thorn`). `min_ap` and `min_dp` follow the RESOURCE sheet text of the
window on client 3474 (LOC type 37, hash `4156161109`): "At least 220 AP
and 270 DP is required to use (normal) Atoraxxion Party Matching. However,
at least 300 AP and 380 DP is required for Orzekea."

## Notes

- Clients 2107 and 2519 store 3 entries in each list (84 bytes); from
  client 3002 the first list has `157` too (94 bytes). Client 1784 does not
  ship the file.
- The window also checks character level 60 in Lua
  (`LUA_ATORAXXION_MATCHING_CONDITION_LV`), which the file does not store.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`:
  each entry as the field key, its internal name and `AP / DP`.
  `test_pvp_tables.py` checks that every key is an Atoraxxion field.

## Open Questions

### Second List

What `unknown_conditions` is for. It holds the same entries as
`matching_conditions` without Orzekea (`157`) on every client from 3002;
on clients 2107 and 2519 the two lists are the same. No Lua reads either
list by a name.
