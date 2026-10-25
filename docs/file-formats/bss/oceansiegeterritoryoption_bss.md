# `oceansiegeterritoryoption.bss` Format

## Purpose

The Blue Battlefield (ocean siege) options of each siege group: the two
territories the group fights over and the one console shows, the HP,
AP, damage reduction, accuracy, evasion and damage reduction rate limits
(all uncapped), amounts left unknown, a world position, the most
participants per day and the days the battle runs. Client 3482 has one
row, the only ocean group (`BEGINNER`), for Balenos and Calpheon. The Lua
reads it with `ToClient_GetOceanSiegeTerritoryOptionStaticStatusWrapper`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                            | Bytes | Records               | Row bytes |
| ------ | -------------- | ------------------------------- | ----- | --------------------- | --------- |
| 2      | 3342 and later | `oceansiegeterritoryoption.bss` | 196   | 1 Row, 1 String Table | 176       |
| 1      | 3125 to 3335   | `oceansiegeterritoryoption.bss` | 192   | 1 Row, 1 String Table | 172       |

| Layout | File                            | Known        | Unknown       |
| ------ | ------------------------------- | ------------ | ------------- |
| 2      | `oceansiegeterritoryoption.bss` | 90 B (45.9%) | 106 B (54.1%) |
| 1      | `oceansiegeterritoryoption.bss` | 86 B (44.8%) | 106 B (55.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `96306a2d205d`  |
| 3482   | Layout 2             | `96306a2d205d`  |
| 3474   | Layout 2             | `96306a2d205d`  |
| 3473   | Layout 2             | `96306a2d205d`  |
| 3464   | Layout 2             | `96306a2d205d`  |
| 3458   | Layout 2             | `96306a2d205d`  |
| 3454   | Layout 2             | `96306a2d205d`  |
| 3444   | Layout 2             | `96306a2d205d`  |
| 3435   | Layout 2             | `96306a2d205d`  |
| 3426   | Layout 2             | `96306a2d205d`  |
| 3418   | Layout 2             | `96306a2d205d`  |
| 3412   | Layout 2             | `96306a2d205d`  |
| 3402   | Layout 2             | `96306a2d205d`  |
| 3396   | Layout 2             | `96306a2d205d`  |
| 3387   | Layout 2             | `96306a2d205d`  |
| 3381   | Layout 2             | `96306a2d205d`  |
| 3373   | Layout 2             | `96306a2d205d`  |
| 3364   | Layout 2             | `96306a2d205d`  |
| 3356   | Layout 2             | `96306a2d205d`  |
| 3349   | Layout 2             | `96306a2d205d`  |
| 3342   | Layout 2             | `96306a2d205d`  |
| 3335   | Layout 1             | `96306a2d205d`  |
| 3326   | Layout 1             | `96306a2d205d`  |
| 3321   | Layout 1             | `96306a2d205d`  |
| 3314   | Layout 1             | `96306a2d205d`  |
| 3303   | Layout 1             | `96306a2d205d`  |
| 3302   | Layout 1             | `96306a2d205d`  |
| 3293   | Layout 1             | `96306a2d205d`  |
| 3283   | Layout 1             | `96306a2d205d`  |
| 3275   | Layout 1             | `96306a2d205d`  |
| 3267   | Layout 1             | `96306a2d205d`  |
| 3258   | Layout 1             | `96306a2d205d`  |
| 3251   | Layout 1             | `96306a2d205d`  |
| 3242   | Layout 1             | `96306a2d205d`  |
| 3235   | Layout 1             | `96306a2d205d`  |
| 3229   | Layout 1             | `96306a2d205d`  |
| 3212   | Layout 1             | `96306a2d205d`  |
| 3203   | Layout 1             | `96306a2d205d`  |
| 3193   | Layout 1             | `96306a2d205d`  |
| 3186   | Layout 1             | `96306a2d205d`  |
| 3177   | Layout 1             | `96306a2d205d`  |
| 3169   | Layout 1             | `96306a2d205d`  |
| 3158   | Layout 1             | `96306a2d205d`  |
| 3151   | Layout 1             | `96306a2d205d`  |
| 3144   | Layout 1             | `96306a2d205d`  |
| 3133   | Layout 1             | `96306a2d205d`  |
| 3125   | Layout 1             | `96306a2d205d`  |
| 3118   | No documented layout | `96306a2d205d`  |
| 3111   | No documented layout | `96306a2d205d`  |
| 3103   | No file              | `96306a2d205d`  |
| 3095   | No file              | `96306a2d205d`  |
| 3086   | No file              | `96306a2d205d`  |
| 3072   | No file              | `96306a2d205d`  |
| 3062   | No file              | `96306a2d205d`  |
| 3052   | No file              | `96306a2d205d`  |
| 3045   | No file              | `96306a2d205d`  |
| 3037   | No file              | `96306a2d205d`  |
| 3030   | No file              | `96306a2d205d`  |
| 3021   | No file              | `96306a2d205d`  |
| 3012   | No file              | `96306a2d205d`  |
| 3002   | No file              | `96306a2d205d`  |
| 2995   | No file              | `96306a2d205d`  |
| 2987   | No file              | `96306a2d205d`  |
| 2978   | No file              | `96306a2d205d`  |
| 2970   | No file              | `96306a2d205d`  |
| 2959   | No file              | `96306a2d205d`  |
| 2951   | No file              | `96306a2d205d`  |
| 2942   | No file              | `96306a2d205d`  |
| 2935   | No file              | `96306a2d205d`  |
| 2932   | No file              | `96306a2d205d`  |
| 2923   | No file              | `96306a2d205d`  |
| 2919   | No file              | `96306a2d205d`  |
| 2907   | No file              | `96306a2d205d`  |
| 2900   | No file              | `96306a2d205d`  |
| 2891   | No file              | `96306a2d205d`  |
| 2882   | No file              | `96306a2d205d`  |
| 2872   | No file              | `96306a2d205d`  |
| 2863   | No file              | `96306a2d205d`  |
| 2855   | No file              | `96306a2d205d`  |
| 2849   | No file              | `96306a2d205d`  |
| 2844   | No file              | `96306a2d205d`  |
| 2834   | No file              | `96306a2d205d`  |
| 2825   | No file              | `96306a2d205d`  |
| 2819   | No file              | `96306a2d205d`  |
| 2811   | No file              | `96306a2d205d`  |
| 2803   | No file              | `96306a2d205d`  |
| 2794   | No file              | `96306a2d205d`  |
| 2783   | No file              | `96306a2d205d`  |
| 2774   | No file              | `96306a2d205d`  |
| 2765   | No file              | `96306a2d205d`  |
| 2756   | No file              | `96306a2d205d`  |
| 2750   | No file              | `96306a2d205d`  |
| 2743   | No file              | `96306a2d205d`  |
| 2736   | No file              | `96306a2d205d`  |
| 2726   | No file              | `96306a2d205d`  |
| 2717   | No file              | `96306a2d205d`  |
| 2709   | No file              | `96306a2d205d`  |
| 2703   | No file              | `96306a2d205d`  |
| 2695   | No file              | `96306a2d205d`  |
| 2684   | No file              | `96306a2d205d`  |
| 2672   | No file              | `96306a2d205d`  |
| 2665   | No file              | `96306a2d205d`  |
| 2657   | No file              | `96306a2d205d`  |
| 2649   | No file              | `96306a2d205d`  |
| 2644   | No file              | `96306a2d205d`  |
| 2637   | No file              | `96306a2d205d`  |
| 2629   | No file              | `96306a2d205d`  |
| 2619   | No file              | `96306a2d205d`  |
| 2612   | No file              | `96306a2d205d`  |
| 2606   | No file              | `96306a2d205d`  |
| 2602   | No file              | `96306a2d205d`  |
| 2601   | No file              | `96306a2d205d`  |
| 2592   | No file              | `96306a2d205d`  |
| 2583   | No file              | `96306a2d205d`  |
| 2575   | No file              | `96306a2d205d`  |
| 2567   | No file              | `96306a2d205d`  |
| 2560   | No file              | `96306a2d205d`  |
| 2553   | No file              | `96306a2d205d`  |
| 2545   | No file              | `96306a2d205d`  |
| 2538   | No file              | `96306a2d205d`  |
| 2529   | No file              | `96306a2d205d`  |
| 2519   | No file              | `96306a2d205d`  |
| 2513   | No file              | `96306a2d205d`  |
| 2510   | No file              | `96306a2d205d`  |
| 2507   | No file              | `96306a2d205d`  |
| 2503   | No file              | `96306a2d205d`  |
| 2498   | No file              | `96306a2d205d`  |
| 2492   | No file              | `96306a2d205d`  |
| 2487   | No file              | `96306a2d205d`  |
| 2480   | No file              | `96306a2d205d`  |
| 2474   | No file              | `96306a2d205d`  |
| 2468   | No file              | `96306a2d205d`  |
| 2460   | No file              | `96306a2d205d`  |
| 2453   | No file              | `96306a2d205d`  |
| 2444   | No file              | `96306a2d205d`  |
| 2438   | No file              | `96306a2d205d`  |
| 2434   | No file              | `96306a2d205d`  |
| 2429   | No file              | `96306a2d205d`  |
| 2421   | No file              | `96306a2d205d`  |
| 2414   | No file              | `96306a2d205d`  |
| 2407   | No file              | `96306a2d205d`  |
| 2401   | No file              | `96306a2d205d`  |
| 2397   | No file              | `96306a2d205d`  |
| 2393   | No file              | `96306a2d205d`  |
| 2384   | No file              | `96306a2d205d`  |
| 2378   | No file              | `96306a2d205d`  |
| 2372   | No file              | `96306a2d205d`  |
| 2358   | No file              | `96306a2d205d`  |
| 2352   | No file              | `96306a2d205d`  |
| 2347   | No file              | `96306a2d205d`  |
| 2343   | No file              | `96306a2d205d`  |
| 2335   | No file              | `96306a2d205d`  |
| 2327   | No file              | `96306a2d205d`  |
| 2324   | No file              | `96306a2d205d`  |
| 2319   | No file              | `96306a2d205d`  |
| 2313   | No file              | `96306a2d205d`  |
| 2308   | No file              | `96306a2d205d`  |
| 2302   | No file              | `96306a2d205d`  |
| 2295   | No file              | `96306a2d205d`  |
| 2290   | No file              | `96306a2d205d`  |
| 2284   | No file              | `96306a2d205d`  |
| 2276   | No file              | `96306a2d205d`  |
| 2269   | No file              | `96306a2d205d`  |
| 2259   | No file              | `96306a2d205d`  |
| 2250   | No file              | `96306a2d205d`  |
| 2243   | No file              | `96306a2d205d`  |
| 2235   | No file              | `96306a2d205d`  |
| 2229   | No file              | `96306a2d205d`  |
| 2224   | No file              | `96306a2d205d`  |
| 2218   | No file              | `96306a2d205d`  |
| 2215   | No file              | `96306a2d205d`  |
| 2207   | No file              | `96306a2d205d`  |
| 2203   | No file              | `96306a2d205d`  |
| 2196   | No file              | `96306a2d205d`  |
| 2192   | No file              | `96306a2d205d`  |
| 2189   | No file              | `96306a2d205d`  |
| 2183   | No file              | `96306a2d205d`  |
| 2179   | No file              | `96306a2d205d`  |
| 2171   | No file              | `96306a2d205d`  |
| 2163   | No file              | `96306a2d205d`  |
| 2156   | No file              | `96306a2d205d`  |
| 2151   | No file              | `96306a2d205d`  |
| 2147   | No file              | `96306a2d205d`  |
| 2142   | No file              | `96306a2d205d`  |
| 2138   | No file              | `96306a2d205d`  |
| 2134   | No file              | `96306a2d205d`  |
| 2130   | No file              | `96306a2d205d`  |
| 2122   | No file              | `96306a2d205d`  |
| 2107   | No file              | `96306a2d205d`  |
| 2098   | No file              | `96306a2d205d`  |
| 2089   | No file              | `96306a2d205d`  |
| 2081   | No file              | `96306a2d205d`  |
| 2073   | No file              | `96306a2d205d`  |
| 2067   | No file              | `96306a2d205d`  |
| 2063   | No file              | `96306a2d205d`  |
| 2059   | No file              | `96306a2d205d`  |
| 2052   | No file              | `96306a2d205d`  |
| 2044   | No file              | `96306a2d205d`  |
| 2039   | No file              | `96306a2d205d`  |
| 2032   | No file              | `96306a2d205d`  |
| 2025   | No file              | `96306a2d205d`  |
| 2011   | No file              | `96306a2d205d`  |
| 2005   | No file              | `96306a2d205d`  |
| 2000   | No file              | `96306a2d205d`  |
| 1996   | No file              | `96306a2d205d`  |
| 1991   | No file              | `96306a2d205d`  |
| 1985   | No file              | `96306a2d205d`  |
| 1980   | No file              | `96306a2d205d`  |
| 1969   | No file              | `96306a2d205d`  |
| 1964   | No file              | `96306a2d205d`  |
| 1958   | No file              | `96306a2d205d`  |
| 1950   | No file              | `96306a2d205d`  |
| 1945   | No file              | `96306a2d205d`  |
| 1937   | No file              | `96306a2d205d`  |
| 1933   | No file              | `96306a2d205d`  |
| 1927   | No file              | `96306a2d205d`  |
| 1921   | No file              | `96306a2d205d`  |
| 1914   | No file              | `96306a2d205d`  |
| 1908   | No file              | `96306a2d205d`  |
| 1897   | No file              | `96306a2d205d`  |
| 1892   | No file              | `96306a2d205d`  |
| 1886   | No file              | `96306a2d205d`  |
| 1881   | No file              | `96306a2d205d`  |
| 1871   | No file              | `96306a2d205d`  |
| 1866   | No file              | `96306a2d205d`  |
| 1862   | No file              | `96306a2d205d`  |
| 1854   | No file              | `96306a2d205d`  |
| 1846   | No file              | `96306a2d205d`  |
| 1838   | No file              | `96306a2d205d`  |
| 1832   | No file              | `96306a2d205d`  |
| 1826   | No file              | `96306a2d205d`  |
| 1822   | No file              | `96306a2d205d`  |
| 1818   | No file              | `96306a2d205d`  |
| 1804   | No file              | `96306a2d205d`  |
| 1794   | No file              | `96306a2d205d`  |
| 1790   | No file              | `96306a2d205d`  |
| 1784   | No file              | `96306a2d205d`  |
| 1774   | No file              | `96306a2d205d`  |
| 1771   | No file              | `96306a2d205d`  |
| 1762   | No file              | `96306a2d205d`  |
| 1759   | No file              | `96306a2d205d`  |
| 1754   | No file              | `96306a2d205d`  |
| 1749   | No file              | `96306a2d205d`  |
| 1743   | No file              | `96306a2d205d`  |
| 1737   | No file              | `96306a2d205d`  |
| 1731   | No file              | `96306a2d205d`  |
| 1725   | No file              | `96306a2d205d`  |
| 1717   | No file              | `96306a2d205d`  |
| 1710   | No file              | `96306a2d205d`  |
| 1704   | No file              | `96306a2d205d`  |
| 1698   | No file              | `96306a2d205d`  |
| 1690   | No file              | `96306a2d205d`  |
| 1685   | No file              | `96306a2d205d`  |
| 1680   | No file              | `96306a2d205d`  |
| 1674   | No file              | `96306a2d205d`  |
| 1668   | No file              | `96306a2d205d`  |
| 1659   | No file              | `96306a2d205d`  |
| 1649   | No file              | `96306a2d205d`  |
| 1642   | No file              | `96306a2d205d`  |
| 1636   | No file              | `96306a2d205d`  |
| 1628   | No file              | `96306a2d205d`  |
| 1622   | No file              | `96306a2d205d`  |
| 1614   | No file              | `96306a2d205d`  |
| 1608   | No file              | `96306a2d205d`  |
| 1602   | No file              | `96306a2d205d`  |
| 1598   | No file              | `96306a2d205d`  |
| 1594   | No file              | `96306a2d205d`  |
| 1590   | No file              | `96306a2d205d`  |
| 1587   | No file              | `96306a2d205d`  |
| 1584   | No file              | `96306a2d205d`  |
| 1579   | No file              | `96306a2d205d`  |
| 1572   | No file              | `96306a2d205d`  |
| 1565   | No file              | `96306a2d205d`  |
| 1559   | No file              | `96306a2d205d`  |
| 1554   | No file              | `96306a2d205d`  |
| 1547   | No file              | `96306a2d205d`  |
| 1537   | No file              | `96306a2d205d`  |
| 1529   | No file              | `96306a2d205d`  |
| 1524   | No file              | `96306a2d205d`  |
| 1519   | No file              | `96306a2d205d`  |
| 1509   | No file              | `96306a2d205d`  |
| 1506   | No file              | `96306a2d205d`  |
| 1504   | No file              | `96306a2d205d`  |
| 1500   | No file              | `96306a2d205d`  |
| 1493   | No file              | `96306a2d205d`  |
| 1489   | No file              | `96306a2d205d`  |
| 1485   | No file              | `96306a2d205d`  |
| 1481   | No file              | `96306a2d205d`  |
| 1474   | No file              | `96306a2d205d`  |
| 1466   | No file              | `96306a2d205d`  |
| 1462   | No file              | `96306a2d205d`  |
| 1459   | No file              | `96306a2d205d`  |
| 1453   | No file              | `96306a2d205d`  |
| 1450   | No file              | `96306a2d205d`  |
| 1445   | No file              | `96306a2d205d`  |
| 1439   | No file              | `96306a2d205d`  |
| 1433   | No file              | `96306a2d205d`  |
| 1430   | No file              | `96306a2d205d`  |
| 1426   | No file              | `96306a2d205d`  |
| 1421   | No file              | `96306a2d205d`  |
| 1417   | No file              | `96306a2d205d`  |
| 1416   | No file              | `96306a2d205d`  |
| 1409   | No file              | `96306a2d205d`  |
| 1405   | No file              | `96306a2d205d`  |
| 1401   | No file              | `96306a2d205d`  |
| 1396   | No file              | `96306a2d205d`  |
| 1391   | No file              | `96306a2d205d`  |
| 1390   | No file              | `96306a2d205d`  |
| 1386   | No file              | `96306a2d205d`  |
| 1381   | No file              | `96306a2d205d`  |
| 1379   | No file              | `96306a2d205d`  |
| 1372   | No file              | `96306a2d205d`  |
| 1366   | No file              | `96306a2d205d`  |
| 1364   | No file              | `96306a2d205d`  |
| 1363   | No file              | `96306a2d205d`  |
| 1360   | No file              | `96306a2d205d`  |
| 1358   | No file              | `96306a2d205d`  |
| 1355   | No file              | `96306a2d205d`  |
| 1351   | No file              | `96306a2d205d`  |
| 1348   | No file              | `96306a2d205d`  |
| 1346   | No file              | `96306a2d205d`  |
| 1341   | No file              | `96306a2d205d`  |
| 1340   | No file              | `96306a2d205d`  |
| 1338   | No file              | `96306a2d205d`  |
| 1335   | No file              | `96306a2d205d`  |
| 1333   | No file              | `96306a2d205d`  |
| 1329   | No file              | `96306a2d205d`  |
| 1327   | No file              | `96306a2d205d`  |
| 1324   | No file              | `96306a2d205d`  |
| 1321   | No file              | `96306a2d205d`  |
| 1319   | No file              | `96306a2d205d`  |
| 1318   | No file              | `96306a2d205d`  |
| 1316   | No file              | `96306a2d205d`  |
| 1313   | No file              | `96306a2d205d`  |
| 1311   | No file              | `96306a2d205d`  |
| 1309   | No file              | `96306a2d205d`  |
| 1304   | No file              | `96306a2d205d`  |
| 1292   | No file              | `96306a2d205d`  |
| 1286   | No file              | `96306a2d205d`  |
| 1280   | No file              | `96306a2d205d`  |
| 1276   | No file              | `96306a2d205d`  |
| 1267   | No file              | `96306a2d205d`  |
| 1261   | No file              | `96306a2d205d`  |
| 1256   | No file              | `96306a2d205d`  |
| 1250   | No file              | `96306a2d205d`  |
| 1246   | No file              | `96306a2d205d`  |
| 1239   | No file              | `96306a2d205d`  |
| 1230   | No file              | `96306a2d205d`  |
| 1226   | No file              | `96306a2d205d`  |
| 1220   | No file              | `96306a2d205d`  |
| 1217   | No file              | `96306a2d205d`  |
| 1211   | No file              | `96306a2d205d`  |
| 1210   | No file              | `96306a2d205d`  |
| 1208   | No file              | `96306a2d205d`  |
| 1203   | No file              | `96306a2d205d`  |
| 1197   | No file              | `96306a2d205d`  |
| 1194   | No file              | `96306a2d205d`  |
| 1192   | No file              | `96306a2d205d`  |
| 1187   | No file              | `96306a2d205d`  |
| 1183   | No file              | `96306a2d205d`  |
| 1177   | No file              | `96306a2d205d`  |
| 1173   | No file              | `96306a2d205d`  |
| 1167   | No file              | `96306a2d205d`  |
| 1164   | No file              | `96306a2d205d`  |
| 1156   | No file              | `96306a2d205d`  |
| 1149   | No file              | `96306a2d205d`  |
| 1144   | No file              | `96306a2d205d`  |
| 1137   | No file              | `96306a2d205d`  |
| 1132   | No file              | `96306a2d205d`  |
| 1127   | No file              | `96306a2d205d`  |
| 1122   | No file              | `96306a2d205d`  |
| 1118   | No file              | `96306a2d205d`  |
| 1114   | No file              | `96306a2d205d`  |
| 1109   | No file              | `96306a2d205d`  |
| 1102   | No file              | `96306a2d205d`  |
| 1096   | No file              | `96306a2d205d`  |
| 1088   | No file              | `96306a2d205d`  |
| 1081   | No file              | `96306a2d205d`  |
| 1076   | No file              | `96306a2d205d`  |
| 1069   | No file              | `96306a2d205d`  |
| 1064   | No file              | `96306a2d205d`  |
| 1058   | No file              | `96306a2d205d`  |
| 1051   | No file              | `96306a2d205d`  |
| 1044   | No file              | `96306a2d205d`  |
| 1036   | No file              | `96306a2d205d`  |
| 1026   | No file              | `96306a2d205d`  |
| 1016   | No file              | `96306a2d205d`  |
| 1009   | No file              | `96306a2d205d`  |
| 1005   | No file              | `96306a2d205d`  |
| 1000   | No file              | `96306a2d205d`  |
| 998    | No file              | `96306a2d205d`  |
| 990    | No file              | `96306a2d205d`  |
| 979    | No file              | `96306a2d205d`  |
| 972    | No file              | `96306a2d205d`  |
| 963    | No file              | `96306a2d205d`  |
| 955    | No file              | `96306a2d205d`  |
| 946    | No file              | `96306a2d205d`  |
| 938    | No file              | `96306a2d205d`  |
| 927    | No file              | `96306a2d205d`  |
| 911    | No file              | `96306a2d205d`  |
| 904    | No file              | `96306a2d205d`  |
| 899    | No file              | `96306a2d205d`  |
| 894    | No file              | `96306a2d205d`  |
| 885    | No file              | `96306a2d205d`  |
| 879    | No file              | `96306a2d205d`  |
| 872    | No file              | `96306a2d205d`  |
| 864    | No file              | `96306a2d205d`  |
| 855    | No file              | `96306a2d205d`  |
| 853    | No file              | `96306a2d205d`  |
| 845    | No file              | `96306a2d205d`  |
| 837    | No file              | `96306a2d205d`  |
| 829    | No file              | `96306a2d205d`  |
| 822    | No file              | `96306a2d205d`  |
| 814    | No file              | `96306a2d205d`  |
| 805    | No file              | `96306a2d205d`  |
| 794    | No file              | `96306a2d205d`  |
| 787    | No file              | `96306a2d205d`  |
| 780    | No file              | `96306a2d205d`  |
| 771    | No file              | `96306a2d205d`  |
| 760    | No file              | `96306a2d205d`  |
| 748    | No file              | `96306a2d205d`  |
| 741    | No file              | `96306a2d205d`  |
| 736    | No file              | `96306a2d205d`  |
| 731    | No file              | `96306a2d205d`  |
| 723    | No file              | `96306a2d205d`  |
| 711    | No file              | `96306a2d205d`  |
| 707    | No file              | `96306a2d205d`  |
| 697    | No file              | `96306a2d205d`  |
| 689    | No file              | `96306a2d205d`  |
| 683    | No file              | `96306a2d205d`  |
| 678    | No file              | `96306a2d205d`  |
| 670    | No file              | `96306a2d205d`  |
| 661    | No file              | `96306a2d205d`  |
| 656    | No file              | `96306a2d205d`  |
| 652    | No file              | `96306a2d205d`  |
| 643    | No file              | `96306a2d205d`  |
| 637    | No file              | `96306a2d205d`  |
| 630    | No file              | `96306a2d205d`  |
| 627    | No file              | `96306a2d205d`  |
| 621    | No file              | `96306a2d205d`  |
| 617    | No file              | `96306a2d205d`  |
| 615    | No file              | `96306a2d205d`  |
| 606    | No file              | `96306a2d205d`  |
| 599    | No file              | `96306a2d205d`  |
| 592    | No file              | `96306a2d205d`  |
| 586    | No file              | `96306a2d205d`  |
| 577    | No file              | `96306a2d205d`  |
| 569    | No file              | `96306a2d205d`  |
| 561    | No file              | `96306a2d205d`  |
| 554    | No file              | `96306a2d205d`  |
| 542    | No file              | `96306a2d205d`  |
| 532    | No file              | `96306a2d205d`  |
| 531    | No file              | `96306a2d205d`  |
| 526    | No file              | `96306a2d205d`  |
| 521    | No file              | `96306a2d205d`  |
| 517    | No file              | `96306a2d205d`  |
| 510    | No file              | `96306a2d205d`  |
| 508    | No file              | `96306a2d205d`  |
| 504    | No file              | `96306a2d205d`  |
| 497    | No file              | `96306a2d205d`  |
| 491    | No file              | `96306a2d205d`  |
| 485    | No file              | `96306a2d205d`  |
| 478    | No file              | `96306a2d205d`  |
| 472    | No file              | `96306a2d205d`  |
| 466    | No file              | `96306a2d205d`  |
| 457    | No file              | `96306a2d205d`  |
| 452    | No file              | `96306a2d205d`  |
| 449    | No file              | `96306a2d205d`  |
| 435    | No file              | `96306a2d205d`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                      |
| --------------------- | -------- | ----------------------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12              |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                                        |
| ------------------- | -------------- | ------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                                 |
| `+0x04`             | u32            | row_count    | Number of rows, one per ocean siege group; `1` on client 3482 |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                                         |
| `rows+0x00`         | String Table   | string_table | See String Table                                             |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends                |
| `string_table+0x04` | u32            | zero         | Always `0`                                                   |

### Row (variable: 152 bytes + start days)

| Offset  | Type                  | Field                       | Notes                                                                       |
| ------- | --------------------- | --------------------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16                   | territory_key_1             | `territoryinfo.bss` key, LOC type 12 name; `0` (Balenos) on client 3482     |
| `+0x02` | u16                   | territory_key_2             | `2` (Calpheon) on client 3482                                               |
| `+0x04` | u16                   | console_territory_key       | The territory console shows; `0` on client 3482                             |
| `+0x06` | f32                   | hp_limit                    | `100000000`                                                                 |
| `+0x0A` | f32                   | ap_limit                    | `9999`                                                                      |
| `+0x0E` | f32                   | dr_limit                    | `9999`                                                                      |
| `+0x12` | f32                   | unknown_12                  | FLT_MAX (`FF FF 7F 7F`); with `unknown_16` the AP+DP limit, see Field Names |
| `+0x16` | f32                   | unknown_16                  | FLT_MAX                                                                     |
| `+0x1A` | f32                   | accuracy_limit              | `9999`                                                                      |
| `+0x1E` | f32                   | evasion_limit               | `9999`                                                                      |
| `+0x22` | u32                   | dr_rate_limit               | `1000000`                                                                   |
| `+0x26` | u32                   | unknown_26                  | `1000000`                                                                   |
| `+0x2A` | u32                   | unknown_2a                  | `1000000`                                                                   |
| `+0x2E` | u32                   | unknown_2e                  | `0`                                                                         |
| `+0x32` | f32                   | unknown_32                  | `9999`                                                                      |
| `+0x36` | f32                   | unknown_36                  | `9999`                                                                      |
| `+0x3A` | f32                   | unknown_3a                  | `100000000`                                                                 |
| `+0x3E` | u32                   | unknown_3e                  | `1000000`                                                                   |
| `+0x42` | u32                   | unknown_42                  | `1000000`                                                                   |
| `+0x46` | u32                   | unknown_46                  | `1000000`                                                                   |
| `+0x4A` | u32                   | unknown_4a                  | `1000000`                                                                   |
| `+0x4E` | bytes[34]             | unknown_4e                  | All `0`                                                                     |
| `+0x70` | u32                   | unknown_70                  | `300000`                                                                    |
| `+0x74` | u32                   | unknown_74                  | `200000`                                                                    |
| `+0x78` | f32                   | unknown_78                  | `13534`; with the next two a world position near Velia, see Notes           |
| `+0x7C` | f32                   | unknown_7c                  | `-7676`                                                                     |
| `+0x80` | f32                   | unknown_80                  | `94091`                                                                     |
| `+0x84` | f32                   | unknown_84                  | `300`                                                                       |
| `+0x88` | u16                   | limit_member_count_sunday   | Most participants on a Sunday battle; `20` on every day on client 3482      |
| `+0x8A` | u16                   | limit_member_count_monday   | Monday                                                                      |
| `+0x8C` | u16                   | limit_member_count_tuesday  | Tuesday                                                                     |
| `+0x8E` | u16                   | limit_member_count_wednesday | Wednesday                                                                  |
| `+0x90` | u16                   | limit_member_count_thursday | Thursday                                                                    |
| `+0x92` | u16                   | limit_member_count_friday   | Friday                                                                      |
| `+0x94` | u32                   | start_day_count             | Number of `start_days`                                                      |
| `+0x98` | u32[start_day_count]  | start_days                  | `CppEnums.VillageSiegeType` days; `0` to `5` (Sunday to Friday) on client 3482 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### Row (variable: 148 bytes + start days)

| Offset  | Type                  | Field                        | Notes                                     |
| ------- | --------------------- | ---------------------------- | ----------------------------------------- |
| `+0x00` | u16                   | territory_key_1              | `0` (Balenos), the only ocean territory   |
| `+0x02` | f32                   | hp_limit                     |                                           |
| `+0x06` | f32                   | ap_limit                     |                                           |
| `+0x0A` | f32                   | dr_limit                     |                                           |
| `+0x0E` | f32                   | unknown_12                   |                                           |
| `+0x12` | f32                   | unknown_16                   |                                           |
| `+0x16` | f32                   | accuracy_limit               |                                           |
| `+0x1A` | f32                   | evasion_limit                |                                           |
| `+0x1E` | u32                   | dr_rate_limit                |                                           |
| `+0x22` | u32                   | unknown_26                   |                                           |
| `+0x26` | u32                   | unknown_2a                   |                                           |
| `+0x2A` | u32                   | unknown_2e                   |                                           |
| `+0x2E` | f32                   | unknown_32                   |                                           |
| `+0x32` | f32                   | unknown_36                   |                                           |
| `+0x36` | f32                   | unknown_3a                   |                                           |
| `+0x3A` | u32                   | unknown_3e                   |                                           |
| `+0x3E` | u32                   | unknown_42                   |                                           |
| `+0x42` | u32                   | unknown_46                   |                                           |
| `+0x46` | u32                   | unknown_4a                   |                                           |
| `+0x4A` | bytes[34]             | unknown_4e                   |                                           |
| `+0x6C` | u32                   | unknown_70                   |                                           |
| `+0x70` | u32                   | unknown_74                   |                                           |
| `+0x74` | f32                   | unknown_78                   |                                           |
| `+0x78` | f32                   | unknown_7c                   |                                           |
| `+0x7C` | f32                   | unknown_80                   |                                           |
| `+0x80` | f32                   | unknown_84                   |                                           |
| `+0x84` | u16                   | limit_member_count_sunday    |                                           |
| `+0x86` | u16                   | limit_member_count_monday    |                                           |
| `+0x88` | u16                   | limit_member_count_tuesday   |                                           |
| `+0x8A` | u16                   | limit_member_count_wednesday |                                           |
| `+0x8C` | u16                   | limit_member_count_thursday  |                                           |
| `+0x8E` | u16                   | limit_member_count_friday    |                                           |
| `+0x90` | u32                   | start_day_count              |                                           |
| `+0x94` | u32[start_day_count]  | start_days                   |                                           |

## Field Names

The Blue Battlefield is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client covers it. The names come from the Lua of client 3482, which reads
the row of each ocean group (`_eTerritoryOceanGroupType`, `BEGINNER = 0,
COUNT = 1` in `panel_window_villagesiegemenu_all.luac`) by its index.

| Field                           | Lua (client 3482)                                    | Match                                                                                   |
| ------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `territory_key_1`, `territory_key_2` | `getTerritoryKey1Raw()`, `getTerritoryKey2Raw()` | `0` and `2`, the two keys of `CppEnums.OceanSiegeTerritoryName` (Balenos, Calpheon)     |
| `console_territory_key`         | `getConsoleTerritoryKeyRaw()`                        | The Lua hides the flag of the territory it does not equal, so it is one of the two keys |
| `limit_member_count_*`          | `getLimitMemberCount(day)`                           | Six u16, one per `start_days` day; `day` comes from `ToClient_GetDayOfWeekByVillageSiege()` |
| `start_days`                    | `getStartDayListCount()`, `getStartDay(index)`       | A u32-counted list of `VillageSiegeType` days, which the Lua prints as day names        |

The land table `siegeterritoryoptionstaticstatus.bss`, which the same Lua
reads with `ToClient_GetSiegeTerritoryOptionStaticStatusWrapper`, starts
its rows with the same three u16: on client 3482 the territory pairs `0,
1` (Balenos, Serendia), `2, 11` and `4, 12`, each followed by a key equal
to one of the pair. That fixes the order key 1, key 2, console key. It
holds six u16 counts before the same `0` to `5` day list too (`30, 25,
30, 25, 30, 25` on its first row).

The limit block from `+0x06` to `+0x4E` has the shape of the one in
[`siegeterritoryoptionstaticstatus.bss`](siegeterritoryoptionstaticstatus_bss.md)
from `+0x08`, where node tooltips name `hp_limit`, `ap_limit`,
`dr_limit`, `accuracy_limit`, `evasion_limit` and `dr_rate_limit`. This
row holds the values of that table's uncapped Valencia and Outer Edania
row (`100000000`, `9999`, FLT_MAX, `1000000`), field for field.
`unknown_12` and `unknown_16` are the `_siegeMaxDDForUI` and
`_siegeMaxPVForUI` pair: FLT_MAX in both is the "No Stat Limit" case of
`isUnlimitedDDPV()`. Which of the two is DD stays open there.

## Notes

- Client 3251 uses Layout 1: one territory key and no second or console
  key (192 bytes); every other value is the one client 3482 has. Client
  3474 adds the second and console keys. The file is not in the archives
  of client 1784.
- `unknown_78`, `unknown_7c` and `unknown_80` read as a BDO world position
  (y the height): `(13534, -7676, 94091)`, near the first revive position
  of Balenos in [`oceansiegereviveposition.bss`](oceansiegereviveposition_bss.md),
  `(6186, -7676, 93658)`, and Velia's return point `(-1226, -7012,
  81647)`. `unknown_84` (`300`) fits a radius.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/oceansiege_tables.py`: the three territory keys with
  their names, the six named limits, the six day limits and the battle
  days by name.

## Open Questions

### The Fields Before the Position

What `unknown_4e` (34 zero bytes), `unknown_70` (`300000`) and
`unknown_74` (`200000`) hold. The Lua reads `_limitVolunteerCount` from
this wrapper, which no field here is known to hold.
