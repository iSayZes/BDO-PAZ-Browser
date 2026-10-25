# `enchantactiveskillitem.bss` Format

## Purpose

Gear that grants a skill at a given enhancement level: per item enchant key
(item and level) the skill key it grants. On client 3474 these are the
Taebaek and Asadal belts and the two Asadal necklaces, each with one skill
per level from base to PEN (`Blessing of Taebaek` at base, `TET: Fury of
Asadal` at TET).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | ------- | --------- |
| 1      | 2171 and later | `enchantactiveskillitem.bss` | 628   | 48 Row  | 13        |

| Layout | File                         | Known         | Unknown     |
| ------ | ---------------------------- | ------------- | ----------- |
| 1      | `enchantactiveskillitem.bss` | 580 B (92.4%) | 48 B (7.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `2b734d718052`  |
| 3482   | Layout 1 | `2b734d718052`  |
| 3474   | Layout 1 | `2b734d718052`  |
| 3473   | Layout 1 | `2b734d718052`  |
| 3464   | Layout 1 | `2b734d718052`  |
| 3458   | Layout 1 | `2b734d718052`  |
| 3454   | Layout 1 | `2b734d718052`  |
| 3444   | Layout 1 | `2b734d718052`  |
| 3435   | Layout 1 | `2b734d718052`  |
| 3426   | Layout 1 | `2b734d718052`  |
| 3418   | Layout 1 | `2b734d718052`  |
| 3412   | Layout 1 | `2b734d718052`  |
| 3402   | Layout 1 | `2b734d718052`  |
| 3396   | Layout 1 | `2b734d718052`  |
| 3387   | Layout 1 | `2b734d718052`  |
| 3381   | Layout 1 | `2b734d718052`  |
| 3373   | Layout 1 | `2b734d718052`  |
| 3364   | Layout 1 | `2b734d718052`  |
| 3356   | Layout 1 | `2b734d718052`  |
| 3349   | Layout 1 | `2b734d718052`  |
| 3342   | Layout 1 | `2b734d718052`  |
| 3335   | Layout 1 | `2b734d718052`  |
| 3326   | Layout 1 | `2b734d718052`  |
| 3321   | Layout 1 | `2b734d718052`  |
| 3314   | Layout 1 | `2b734d718052`  |
| 3303   | Layout 1 | `2b734d718052`  |
| 3302   | Layout 1 | `2b734d718052`  |
| 3293   | Layout 1 | `2b734d718052`  |
| 3283   | Layout 1 | `2b734d718052`  |
| 3275   | Layout 1 | `2b734d718052`  |
| 3267   | Layout 1 | `2b734d718052`  |
| 3258   | Layout 1 | `2b734d718052`  |
| 3251   | Layout 1 | `2b734d718052`  |
| 3242   | Layout 1 | `2b734d718052`  |
| 3235   | Layout 1 | `2b734d718052`  |
| 3229   | Layout 1 | `2b734d718052`  |
| 3212   | Layout 1 | `2b734d718052`  |
| 3203   | Layout 1 | `2b734d718052`  |
| 3193   | Layout 1 | `2b734d718052`  |
| 3186   | Layout 1 | `2b734d718052`  |
| 3177   | Layout 1 | `2b734d718052`  |
| 3169   | Layout 1 | `2b734d718052`  |
| 3158   | Layout 1 | `2b734d718052`  |
| 3151   | Layout 1 | `2b734d718052`  |
| 3144   | Layout 1 | `2b734d718052`  |
| 3133   | Layout 1 | `2b734d718052`  |
| 3125   | Layout 1 | `2b734d718052`  |
| 3118   | Layout 1 | `2b734d718052`  |
| 3111   | Layout 1 | `2b734d718052`  |
| 3103   | Layout 1 | `2b734d718052`  |
| 3095   | Layout 1 | `2b734d718052`  |
| 3086   | Layout 1 | `2b734d718052`  |
| 3072   | Layout 1 | `2b734d718052`  |
| 3062   | Layout 1 | `2b734d718052`  |
| 3052   | Layout 1 | `2b734d718052`  |
| 3045   | Layout 1 | `2b734d718052`  |
| 3037   | Layout 1 | `2b734d718052`  |
| 3030   | Layout 1 | `2b734d718052`  |
| 3021   | Layout 1 | `2b734d718052`  |
| 3012   | Layout 1 | `2b734d718052`  |
| 3002   | Layout 1 | `2b734d718052`  |
| 2995   | Layout 1 | `2b734d718052`  |
| 2987   | Layout 1 | `2b734d718052`  |
| 2978   | Layout 1 | `2b734d718052`  |
| 2970   | Layout 1 | `2b734d718052`  |
| 2959   | Layout 1 | `2b734d718052`  |
| 2951   | Layout 1 | `2b734d718052`  |
| 2942   | Layout 1 | `2b734d718052`  |
| 2935   | Layout 1 | `2b734d718052`  |
| 2932   | Layout 1 | `2b734d718052`  |
| 2923   | Layout 1 | `2b734d718052`  |
| 2919   | Layout 1 | `2b734d718052`  |
| 2907   | Layout 1 | `2b734d718052`  |
| 2900   | Layout 1 | `2b734d718052`  |
| 2891   | Layout 1 | `2b734d718052`  |
| 2882   | Layout 1 | `2b734d718052`  |
| 2872   | Layout 1 | `2b734d718052`  |
| 2863   | Layout 1 | `2b734d718052`  |
| 2855   | Layout 1 | `2b734d718052`  |
| 2849   | Layout 1 | `2b734d718052`  |
| 2844   | Layout 1 | `2b734d718052`  |
| 2834   | Layout 1 | `2b734d718052`  |
| 2825   | Layout 1 | `2b734d718052`  |
| 2819   | Layout 1 | `2b734d718052`  |
| 2811   | Layout 1 | `2b734d718052`  |
| 2803   | Layout 1 | `2b734d718052`  |
| 2794   | Layout 1 | `2b734d718052`  |
| 2783   | Layout 1 | `2b734d718052`  |
| 2774   | Layout 1 | `2b734d718052`  |
| 2765   | Layout 1 | `2b734d718052`  |
| 2756   | Layout 1 | `2b734d718052`  |
| 2750   | Layout 1 | `2b734d718052`  |
| 2743   | Layout 1 | `2b734d718052`  |
| 2736   | Layout 1 | `2b734d718052`  |
| 2726   | Layout 1 | `2b734d718052`  |
| 2717   | Layout 1 | `2b734d718052`  |
| 2709   | Layout 1 | `2b734d718052`  |
| 2703   | Layout 1 | `2b734d718052`  |
| 2695   | Layout 1 | `2b734d718052`  |
| 2684   | Layout 1 | `2b734d718052`  |
| 2672   | Layout 1 | `2b734d718052`  |
| 2665   | Layout 1 | `2b734d718052`  |
| 2657   | Layout 1 | `2b734d718052`  |
| 2649   | Layout 1 | `2b734d718052`  |
| 2644   | Layout 1 | `2b734d718052`  |
| 2637   | Layout 1 | `2b734d718052`  |
| 2629   | Layout 1 | `2b734d718052`  |
| 2619   | Layout 1 | `2b734d718052`  |
| 2612   | Layout 1 | `2b734d718052`  |
| 2606   | Layout 1 | `2b734d718052`  |
| 2602   | Layout 1 | `2b734d718052`  |
| 2601   | Layout 1 | `2b734d718052`  |
| 2592   | Layout 1 | `2b734d718052`  |
| 2583   | Layout 1 | `2b734d718052`  |
| 2575   | Layout 1 | `2b734d718052`  |
| 2567   | Layout 1 | `2b734d718052`  |
| 2560   | Layout 1 | `2b734d718052`  |
| 2553   | Layout 1 | `2b734d718052`  |
| 2545   | Layout 1 | `2b734d718052`  |
| 2538   | Layout 1 | `2b734d718052`  |
| 2529   | Layout 1 | `2b734d718052`  |
| 2519   | Layout 1 | `2b734d718052`  |
| 2513   | Layout 1 | `2b734d718052`  |
| 2510   | Layout 1 | `2b734d718052`  |
| 2507   | Layout 1 | `2b734d718052`  |
| 2503   | Layout 1 | `2b734d718052`  |
| 2498   | Layout 1 | `2b734d718052`  |
| 2492   | Layout 1 | `2b734d718052`  |
| 2487   | Layout 1 | `2b734d718052`  |
| 2480   | Layout 1 | `2b734d718052`  |
| 2474   | Layout 1 | `2b734d718052`  |
| 2468   | Layout 1 | `2b734d718052`  |
| 2460   | Layout 1 | `2b734d718052`  |
| 2453   | Layout 1 | `2b734d718052`  |
| 2444   | Layout 1 | `2b734d718052`  |
| 2438   | Layout 1 | `2b734d718052`  |
| 2434   | Layout 1 | `2b734d718052`  |
| 2429   | Layout 1 | `2b734d718052`  |
| 2421   | Layout 1 | `2b734d718052`  |
| 2414   | Layout 1 | `2b734d718052`  |
| 2407   | Layout 1 | `2b734d718052`  |
| 2401   | Layout 1 | `2b734d718052`  |
| 2397   | Layout 1 | `2b734d718052`  |
| 2393   | Layout 1 | `2b734d718052`  |
| 2384   | Layout 1 | `2b734d718052`  |
| 2378   | Layout 1 | `2b734d718052`  |
| 2372   | Layout 1 | `2b734d718052`  |
| 2358   | Layout 1 | `2b734d718052`  |
| 2352   | Layout 1 | `2b734d718052`  |
| 2347   | Layout 1 | `2b734d718052`  |
| 2343   | Layout 1 | `2b734d718052`  |
| 2335   | Layout 1 | `2b734d718052`  |
| 2327   | Layout 1 | `2b734d718052`  |
| 2324   | Layout 1 | `2b734d718052`  |
| 2319   | Layout 1 | `2b734d718052`  |
| 2313   | Layout 1 | `2b734d718052`  |
| 2308   | Layout 1 | `2b734d718052`  |
| 2302   | Layout 1 | `2b734d718052`  |
| 2295   | Layout 1 | `2b734d718052`  |
| 2290   | Layout 1 | `2b734d718052`  |
| 2284   | Layout 1 | `2b734d718052`  |
| 2276   | Layout 1 | `2b734d718052`  |
| 2269   | Layout 1 | `2b734d718052`  |
| 2259   | Layout 1 | `2b734d718052`  |
| 2250   | Layout 1 | `2b734d718052`  |
| 2243   | Layout 1 | `2b734d718052`  |
| 2235   | Layout 1 | `2b734d718052`  |
| 2229   | Layout 1 | `2b734d718052`  |
| 2224   | Layout 1 | `2b734d718052`  |
| 2218   | Layout 1 | `2b734d718052`  |
| 2215   | Layout 1 | `2b734d718052`  |
| 2207   | Layout 1 | `2b734d718052`  |
| 2203   | Layout 1 | `2b734d718052`  |
| 2196   | Layout 1 | `2b734d718052`  |
| 2192   | Layout 1 | `2b734d718052`  |
| 2189   | Layout 1 | `2b734d718052`  |
| 2183   | Layout 1 | `2b734d718052`  |
| 2179   | Layout 1 | `2b734d718052`  |
| 2171   | Layout 1 | `2b734d718052`  |
| 2163   | No file  | `2b734d718052`  |
| 2156   | No file  | `2b734d718052`  |
| 2151   | No file  | `2b734d718052`  |
| 2147   | No file  | `2b734d718052`  |
| 2142   | No file  | `2b734d718052`  |
| 2138   | No file  | `2b734d718052`  |
| 2134   | No file  | `2b734d718052`  |
| 2130   | No file  | `2b734d718052`  |
| 2122   | No file  | `2b734d718052`  |
| 2107   | No file  | `2b734d718052`  |
| 2098   | No file  | `2b734d718052`  |
| 2089   | No file  | `2b734d718052`  |
| 2081   | No file  | `2b734d718052`  |
| 2073   | No file  | `2b734d718052`  |
| 2067   | No file  | `2b734d718052`  |
| 2063   | No file  | `2b734d718052`  |
| 2059   | No file  | `2b734d718052`  |
| 2052   | No file  | `2b734d718052`  |
| 2044   | No file  | `2b734d718052`  |
| 2039   | No file  | `2b734d718052`  |
| 2032   | No file  | `2b734d718052`  |
| 2025   | No file  | `2b734d718052`  |
| 2011   | No file  | `2b734d718052`  |
| 2005   | No file  | `2b734d718052`  |
| 2000   | No file  | `2b734d718052`  |
| 1996   | No file  | `2b734d718052`  |
| 1991   | No file  | `2b734d718052`  |
| 1985   | No file  | `2b734d718052`  |
| 1980   | No file  | `2b734d718052`  |
| 1969   | No file  | `2b734d718052`  |
| 1964   | No file  | `2b734d718052`  |
| 1958   | No file  | `2b734d718052`  |
| 1950   | No file  | `2b734d718052`  |
| 1945   | No file  | `2b734d718052`  |
| 1937   | No file  | `2b734d718052`  |
| 1933   | No file  | `2b734d718052`  |
| 1927   | No file  | `2b734d718052`  |
| 1921   | No file  | `2b734d718052`  |
| 1914   | No file  | `2b734d718052`  |
| 1908   | No file  | `2b734d718052`  |
| 1897   | No file  | `2b734d718052`  |
| 1892   | No file  | `2b734d718052`  |
| 1886   | No file  | `2b734d718052`  |
| 1881   | No file  | `2b734d718052`  |
| 1871   | No file  | `2b734d718052`  |
| 1866   | No file  | `2b734d718052`  |
| 1862   | No file  | `2b734d718052`  |
| 1854   | No file  | `2b734d718052`  |
| 1846   | No file  | `2b734d718052`  |
| 1838   | No file  | `2b734d718052`  |
| 1832   | No file  | `2b734d718052`  |
| 1826   | No file  | `2b734d718052`  |
| 1822   | No file  | `2b734d718052`  |
| 1818   | No file  | `2b734d718052`  |
| 1804   | No file  | `2b734d718052`  |
| 1794   | No file  | `2b734d718052`  |
| 1790   | No file  | `2b734d718052`  |
| 1784   | No file  | `2b734d718052`  |
| 1774   | No file  | `2b734d718052`  |
| 1771   | No file  | `2b734d718052`  |
| 1762   | No file  | `2b734d718052`  |
| 1759   | No file  | `2b734d718052`  |
| 1754   | No file  | `2b734d718052`  |
| 1749   | No file  | `2b734d718052`  |
| 1743   | No file  | `2b734d718052`  |
| 1737   | No file  | `2b734d718052`  |
| 1731   | No file  | `2b734d718052`  |
| 1725   | No file  | `2b734d718052`  |
| 1717   | No file  | `2b734d718052`  |
| 1710   | No file  | `2b734d718052`  |
| 1704   | No file  | `2b734d718052`  |
| 1698   | No file  | `2b734d718052`  |
| 1690   | No file  | `2b734d718052`  |
| 1685   | No file  | `2b734d718052`  |
| 1680   | No file  | `2b734d718052`  |
| 1674   | No file  | `2b734d718052`  |
| 1668   | No file  | `2b734d718052`  |
| 1659   | No file  | `2b734d718052`  |
| 1649   | No file  | `2b734d718052`  |
| 1642   | No file  | `2b734d718052`  |
| 1636   | No file  | `2b734d718052`  |
| 1628   | No file  | `2b734d718052`  |
| 1622   | No file  | `2b734d718052`  |
| 1614   | No file  | `2b734d718052`  |
| 1608   | No file  | `2b734d718052`  |
| 1602   | No file  | `2b734d718052`  |
| 1598   | No file  | `2b734d718052`  |
| 1594   | No file  | `2b734d718052`  |
| 1590   | No file  | `2b734d718052`  |
| 1587   | No file  | `2b734d718052`  |
| 1584   | No file  | `2b734d718052`  |
| 1579   | No file  | `2b734d718052`  |
| 1572   | No file  | `2b734d718052`  |
| 1565   | No file  | `2b734d718052`  |
| 1559   | No file  | `2b734d718052`  |
| 1554   | No file  | `2b734d718052`  |
| 1547   | No file  | `2b734d718052`  |
| 1537   | No file  | `2b734d718052`  |
| 1529   | No file  | `2b734d718052`  |
| 1524   | No file  | `2b734d718052`  |
| 1519   | No file  | `2b734d718052`  |
| 1509   | No file  | `2b734d718052`  |
| 1506   | No file  | `2b734d718052`  |
| 1504   | No file  | `2b734d718052`  |
| 1500   | No file  | `2b734d718052`  |
| 1493   | No file  | `2b734d718052`  |
| 1489   | No file  | `2b734d718052`  |
| 1485   | No file  | `2b734d718052`  |
| 1481   | No file  | `2b734d718052`  |
| 1474   | No file  | `2b734d718052`  |
| 1466   | No file  | `2b734d718052`  |
| 1462   | No file  | `2b734d718052`  |
| 1459   | No file  | `2b734d718052`  |
| 1453   | No file  | `2b734d718052`  |
| 1450   | No file  | `2b734d718052`  |
| 1445   | No file  | `2b734d718052`  |
| 1439   | No file  | `2b734d718052`  |
| 1433   | No file  | `2b734d718052`  |
| 1430   | No file  | `2b734d718052`  |
| 1426   | No file  | `2b734d718052`  |
| 1421   | No file  | `2b734d718052`  |
| 1417   | No file  | `2b734d718052`  |
| 1416   | No file  | `2b734d718052`  |
| 1409   | No file  | `2b734d718052`  |
| 1405   | No file  | `2b734d718052`  |
| 1401   | No file  | `2b734d718052`  |
| 1396   | No file  | `2b734d718052`  |
| 1391   | No file  | `2b734d718052`  |
| 1390   | No file  | `2b734d718052`  |
| 1386   | No file  | `2b734d718052`  |
| 1381   | No file  | `2b734d718052`  |
| 1379   | No file  | `2b734d718052`  |
| 1372   | No file  | `2b734d718052`  |
| 1366   | No file  | `2b734d718052`  |
| 1364   | No file  | `2b734d718052`  |
| 1363   | No file  | `2b734d718052`  |
| 1360   | No file  | `2b734d718052`  |
| 1358   | No file  | `2b734d718052`  |
| 1355   | No file  | `2b734d718052`  |
| 1351   | No file  | `2b734d718052`  |
| 1348   | No file  | `2b734d718052`  |
| 1346   | No file  | `2b734d718052`  |
| 1341   | No file  | `2b734d718052`  |
| 1340   | No file  | `2b734d718052`  |
| 1338   | No file  | `2b734d718052`  |
| 1335   | No file  | `2b734d718052`  |
| 1333   | No file  | `2b734d718052`  |
| 1329   | No file  | `2b734d718052`  |
| 1327   | No file  | `2b734d718052`  |
| 1324   | No file  | `2b734d718052`  |
| 1321   | No file  | `2b734d718052`  |
| 1319   | No file  | `2b734d718052`  |
| 1318   | No file  | `2b734d718052`  |
| 1316   | No file  | `2b734d718052`  |
| 1313   | No file  | `2b734d718052`  |
| 1311   | No file  | `2b734d718052`  |
| 1309   | No file  | `2b734d718052`  |
| 1304   | No file  | `2b734d718052`  |
| 1292   | No file  | `2b734d718052`  |
| 1286   | No file  | `2b734d718052`  |
| 1280   | No file  | `2b734d718052`  |
| 1276   | No file  | `2b734d718052`  |
| 1267   | No file  | `2b734d718052`  |
| 1261   | No file  | `2b734d718052`  |
| 1256   | No file  | `2b734d718052`  |
| 1250   | No file  | `2b734d718052`  |
| 1246   | No file  | `2b734d718052`  |
| 1239   | No file  | `2b734d718052`  |
| 1230   | No file  | `2b734d718052`  |
| 1226   | No file  | `2b734d718052`  |
| 1220   | No file  | `2b734d718052`  |
| 1217   | No file  | `2b734d718052`  |
| 1211   | No file  | `2b734d718052`  |
| 1210   | No file  | `2b734d718052`  |
| 1208   | No file  | `2b734d718052`  |
| 1203   | No file  | `2b734d718052`  |
| 1197   | No file  | `2b734d718052`  |
| 1194   | No file  | `2b734d718052`  |
| 1192   | No file  | `2b734d718052`  |
| 1187   | No file  | `2b734d718052`  |
| 1183   | No file  | `2b734d718052`  |
| 1177   | No file  | `2b734d718052`  |
| 1173   | No file  | `2b734d718052`  |
| 1167   | No file  | `2b734d718052`  |
| 1164   | No file  | `2b734d718052`  |
| 1156   | No file  | `2b734d718052`  |
| 1149   | No file  | `2b734d718052`  |
| 1144   | No file  | `2b734d718052`  |
| 1137   | No file  | `2b734d718052`  |
| 1132   | No file  | `2b734d718052`  |
| 1127   | No file  | `2b734d718052`  |
| 1122   | No file  | `2b734d718052`  |
| 1118   | No file  | `2b734d718052`  |
| 1114   | No file  | `2b734d718052`  |
| 1109   | No file  | `2b734d718052`  |
| 1102   | No file  | `2b734d718052`  |
| 1096   | No file  | `2b734d718052`  |
| 1088   | No file  | `2b734d718052`  |
| 1081   | No file  | `2b734d718052`  |
| 1076   | No file  | `2b734d718052`  |
| 1069   | No file  | `2b734d718052`  |
| 1064   | No file  | `2b734d718052`  |
| 1058   | No file  | `2b734d718052`  |
| 1051   | No file  | `2b734d718052`  |
| 1044   | No file  | `2b734d718052`  |
| 1036   | No file  | `2b734d718052`  |
| 1026   | No file  | `2b734d718052`  |
| 1016   | No file  | `2b734d718052`  |
| 1009   | No file  | `2b734d718052`  |
| 1005   | No file  | `2b734d718052`  |
| 1000   | No file  | `2b734d718052`  |
| 998    | No file  | `2b734d718052`  |
| 990    | No file  | `2b734d718052`  |
| 979    | No file  | `2b734d718052`  |
| 972    | No file  | `2b734d718052`  |
| 963    | No file  | `2b734d718052`  |
| 955    | No file  | `2b734d718052`  |
| 946    | No file  | `2b734d718052`  |
| 938    | No file  | `2b734d718052`  |
| 927    | No file  | `2b734d718052`  |
| 911    | No file  | `2b734d718052`  |
| 904    | No file  | `2b734d718052`  |
| 899    | No file  | `2b734d718052`  |
| 894    | No file  | `2b734d718052`  |
| 885    | No file  | `2b734d718052`  |
| 879    | No file  | `2b734d718052`  |
| 872    | No file  | `2b734d718052`  |
| 864    | No file  | `2b734d718052`  |
| 855    | No file  | `2b734d718052`  |
| 853    | No file  | `2b734d718052`  |
| 845    | No file  | `2b734d718052`  |
| 837    | No file  | `2b734d718052`  |
| 829    | No file  | `2b734d718052`  |
| 822    | No file  | `2b734d718052`  |
| 814    | No file  | `2b734d718052`  |
| 805    | No file  | `2b734d718052`  |
| 794    | No file  | `2b734d718052`  |
| 787    | No file  | `2b734d718052`  |
| 780    | No file  | `2b734d718052`  |
| 771    | No file  | `2b734d718052`  |
| 760    | No file  | `2b734d718052`  |
| 748    | No file  | `2b734d718052`  |
| 741    | No file  | `2b734d718052`  |
| 736    | No file  | `2b734d718052`  |
| 731    | No file  | `2b734d718052`  |
| 723    | No file  | `2b734d718052`  |
| 711    | No file  | `2b734d718052`  |
| 707    | No file  | `2b734d718052`  |
| 697    | No file  | `2b734d718052`  |
| 689    | No file  | `2b734d718052`  |
| 683    | No file  | `2b734d718052`  |
| 678    | No file  | `2b734d718052`  |
| 670    | No file  | `2b734d718052`  |
| 661    | No file  | `2b734d718052`  |
| 656    | No file  | `2b734d718052`  |
| 652    | No file  | `2b734d718052`  |
| 643    | No file  | `2b734d718052`  |
| 637    | No file  | `2b734d718052`  |
| 630    | No file  | `2b734d718052`  |
| 627    | No file  | `2b734d718052`  |
| 621    | No file  | `2b734d718052`  |
| 617    | No file  | `2b734d718052`  |
| 615    | No file  | `2b734d718052`  |
| 606    | No file  | `2b734d718052`  |
| 599    | No file  | `2b734d718052`  |
| 592    | No file  | `2b734d718052`  |
| 586    | No file  | `2b734d718052`  |
| 577    | No file  | `2b734d718052`  |
| 569    | No file  | `2b734d718052`  |
| 561    | No file  | `2b734d718052`  |
| 554    | No file  | `2b734d718052`  |
| 542    | No file  | `2b734d718052`  |
| 532    | No file  | `2b734d718052`  |
| 531    | No file  | `2b734d718052`  |
| 526    | No file  | `2b734d718052`  |
| 521    | No file  | `2b734d718052`  |
| 517    | No file  | `2b734d718052`  |
| 510    | No file  | `2b734d718052`  |
| 508    | No file  | `2b734d718052`  |
| 504    | No file  | `2b734d718052`  |
| 497    | No file  | `2b734d718052`  |
| 491    | No file  | `2b734d718052`  |
| 485    | No file  | `2b734d718052`  |
| 478    | No file  | `2b734d718052`  |
| 472    | No file  | `2b734d718052`  |
| 466    | No file  | `2b734d718052`  |
| 457    | No file  | `2b734d718052`  |
| 452    | No file  | `2b734d718052`  |
| 449    | No file  | `2b734d718052`  |
| 435    | No file  | `2b734d718052`  |

<!-- versions:end -->

## Companion Files

None. The handler names the items through LOC type 0 and the skills through
LOC type 10, with their icons.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 48 x 13 = 628 bytes.

### Row (13 bytes)

| Offset  | Type | Field        | Notes                                                                                 |
| ------- | ---- | ------------ | ------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key     | Item enchant key, `enchant_level << 24 \| item_id`; unique                            |
| `+0x04` | u32  | skill_key    | Skill granted, `skill_no << 16 \| level` as in [`skill.dbss`](skill_dbss.md); level `1` on every row of client 3474 |
| `+0x08` | u32  | item_key_dup | Equals `item_key` on every row of clients 2519 and 3474                               |
| `+0x0C` | u8   | unknown_0c   | `0` on every row of clients 2519 and 3474                                             |

The rows are grouped by enhancement level (4, 5, 2, 3, 0, 1 on client 3474),
each level listing the items in descending ID order.

## Items and Skills

On client 3474 the 48 rows are 8 items x 6 levels; the items of one set
share their skills:

| Items                                                          | Skills (base to PEN)   |
| -------------------------------------------------------------- | ---------------------- |
| 12282 Taebaek's Belt, 12283 Tidal, 12284 Nightfallen            | 10189 to 10194         |
| 11688 Asadal Necklace, 11689 Moonlit Asadal Necklace            | 10206 to 10211         |
| 12285 Asadal Belt, 12286 Tidal, 12287 Nightfallen               | 10212 to 10217         |

Client 2519 has the 18 Taebaek's Belt rows only.

## Field Names

Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
1784 has the table, and the client 1784 PAZ has no
`enchantactiveskillitem.bss`. `item_key` and `skill_key` follow their
values: every `item_key` is an item of LOC type 0 with level `0` to `5`, and
every `skill_key` splits into a skill number of LOC type 10 (`10189`
Blessing of Taebaek, `10216` TET: Fury of Asadal) and level `1`. The skill
window (`panel_window_skillgroup_all_1.luac`) shows skills with
`_isActiveItemSkill` as "active item skills" while
`ToClient_IsActiveItemSkillEquipBySkillKey(skillKey)` is true; no Lua names
this file.

## Open Questions

### Trailing Byte

`unknown_0c` is `0` on every row of clients 2519 and 3474. Whether it is a
flag that no row sets yet is unknown.
