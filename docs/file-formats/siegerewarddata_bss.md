# `siegerewarddata.bss` Format

## Purpose

The siege reward items by tier and the Conquest War medals, in two
blocks with no row count. Each block opens with a medal item ID and a
u16 tier count and ends with the same 64-byte Major Rewards structure:
the Conquest War victory, defeat, liberation and score place items.
The first block (Grid Block) holds per tier only counts and a plus
item, in four identical 48-byte grids; the second (Tier Block) holds
per tier a victory, defeat and liberation item with counts. On client
3482 the Tier Block's tiers give the Fervent, Determined, Kindling and
Blazing Triumph and Resolve Rewards, and its Major Rewards the Tier 1
Conquest War boxes; the Grid Block's Major Rewards hold the older boxes
of the same names.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records                                                | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------------------------------------------------------ | --------- |
| 1      | 2560 and later | 3483    | `siegerewarddata.bss` | 444   | 4 Tier Grid, 10 Release Medal, 2 Major Rewards, 4 Tier | 6         |

| Layout | File                  | Known         | Unknown      |
| ------ | --------------------- | ------------- | ------------ |
| 1      | `siegerewarddata.bss` | 348 B (78.4%) | 96 B (21.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `05812a69f476`  |
| 3482   | Layout 1 | `05812a69f476`  |
| 3474   | Layout 1 | `05812a69f476`  |
| 3473   | Layout 1 | `05812a69f476`  |
| 3464   | Layout 1 | `05812a69f476`  |
| 3458   | Layout 1 | `05812a69f476`  |
| 3454   | Layout 1 | `05812a69f476`  |
| 3444   | Layout 1 | `05812a69f476`  |
| 3435   | Layout 1 | `05812a69f476`  |
| 3426   | Layout 1 | `05812a69f476`  |
| 3418   | Layout 1 | `05812a69f476`  |
| 3412   | Layout 1 | `05812a69f476`  |
| 3402   | Layout 1 | `05812a69f476`  |
| 3396   | Layout 1 | `05812a69f476`  |
| 3387   | Layout 1 | `05812a69f476`  |
| 3381   | Layout 1 | `05812a69f476`  |
| 3373   | Layout 1 | `05812a69f476`  |
| 3364   | Layout 1 | `05812a69f476`  |
| 3356   | Layout 1 | `05812a69f476`  |
| 3349   | Layout 1 | `05812a69f476`  |
| 3342   | Layout 1 | `05812a69f476`  |
| 3335   | Layout 1 | `05812a69f476`  |
| 3326   | Layout 1 | `05812a69f476`  |
| 3321   | Layout 1 | `05812a69f476`  |
| 3314   | Layout 1 | `05812a69f476`  |
| 3303   | Layout 1 | `05812a69f476`  |
| 3302   | Layout 1 | `05812a69f476`  |
| 3293   | Layout 1 | `05812a69f476`  |
| 3283   | Layout 1 | `05812a69f476`  |
| 3275   | Layout 1 | `05812a69f476`  |
| 3267   | Layout 1 | `05812a69f476`  |
| 3258   | Layout 1 | `05812a69f476`  |
| 3251   | Layout 1 | `05812a69f476`  |
| 3242   | Layout 1 | `05812a69f476`  |
| 3235   | Layout 1 | `05812a69f476`  |
| 3229   | Layout 1 | `05812a69f476`  |
| 3212   | Layout 1 | `05812a69f476`  |
| 3203   | Layout 1 | `05812a69f476`  |
| 3193   | Layout 1 | `05812a69f476`  |
| 3186   | Layout 1 | `05812a69f476`  |
| 3177   | Layout 1 | `05812a69f476`  |
| 3169   | Layout 1 | `05812a69f476`  |
| 3158   | Layout 1 | `05812a69f476`  |
| 3151   | Layout 1 | `05812a69f476`  |
| 3144   | Layout 1 | `05812a69f476`  |
| 3133   | Layout 1 | `05812a69f476`  |
| 3125   | Layout 1 | `05812a69f476`  |
| 3118   | Layout 1 | `05812a69f476`  |
| 3111   | Layout 1 | `05812a69f476`  |
| 3103   | Layout 1 | `05812a69f476`  |
| 3095   | Layout 1 | `05812a69f476`  |
| 3086   | Layout 1 | `05812a69f476`  |
| 3072   | Layout 1 | `05812a69f476`  |
| 3062   | Layout 1 | `05812a69f476`  |
| 3052   | Layout 1 | `05812a69f476`  |
| 3045   | Layout 1 | `05812a69f476`  |
| 3037   | Layout 1 | `05812a69f476`  |
| 3030   | Layout 1 | `05812a69f476`  |
| 3021   | Layout 1 | `05812a69f476`  |
| 3012   | Layout 1 | `05812a69f476`  |
| 3002   | Layout 1 | `05812a69f476`  |
| 2995   | Layout 1 | `05812a69f476`  |
| 2987   | Layout 1 | `05812a69f476`  |
| 2978   | Layout 1 | `05812a69f476`  |
| 2970   | Layout 1 | `05812a69f476`  |
| 2959   | Layout 1 | `05812a69f476`  |
| 2951   | Layout 1 | `05812a69f476`  |
| 2942   | Layout 1 | `05812a69f476`  |
| 2935   | Layout 1 | `05812a69f476`  |
| 2932   | Layout 1 | `05812a69f476`  |
| 2923   | Layout 1 | `05812a69f476`  |
| 2919   | Layout 1 | `05812a69f476`  |
| 2907   | Layout 1 | `05812a69f476`  |
| 2900   | Layout 1 | `05812a69f476`  |
| 2891   | Layout 1 | `05812a69f476`  |
| 2882   | Layout 1 | `05812a69f476`  |
| 2872   | Layout 1 | `05812a69f476`  |
| 2863   | Layout 1 | `05812a69f476`  |
| 2855   | Layout 1 | `05812a69f476`  |
| 2849   | Layout 1 | `05812a69f476`  |
| 2844   | Layout 1 | `05812a69f476`  |
| 2834   | Layout 1 | `05812a69f476`  |
| 2825   | Layout 1 | `05812a69f476`  |
| 2819   | Layout 1 | `05812a69f476`  |
| 2811   | Layout 1 | `05812a69f476`  |
| 2803   | Layout 1 | `05812a69f476`  |
| 2794   | Layout 1 | `05812a69f476`  |
| 2783   | Layout 1 | `05812a69f476`  |
| 2774   | Layout 1 | `05812a69f476`  |
| 2765   | Layout 1 | `05812a69f476`  |
| 2756   | Layout 1 | `05812a69f476`  |
| 2750   | Layout 1 | `05812a69f476`  |
| 2743   | Layout 1 | `05812a69f476`  |
| 2736   | Layout 1 | `05812a69f476`  |
| 2726   | Layout 1 | `05812a69f476`  |
| 2717   | Layout 1 | `05812a69f476`  |
| 2709   | Layout 1 | `05812a69f476`  |
| 2703   | Layout 1 | `05812a69f476`  |
| 2695   | Layout 1 | `05812a69f476`  |
| 2684   | Layout 1 | `05812a69f476`  |
| 2672   | Layout 1 | `05812a69f476`  |
| 2665   | Layout 1 | `05812a69f476`  |
| 2657   | Layout 1 | `05812a69f476`  |
| 2649   | Layout 1 | `05812a69f476`  |
| 2644   | Layout 1 | `05812a69f476`  |
| 2637   | Layout 1 | `05812a69f476`  |
| 2629   | Layout 1 | `05812a69f476`  |
| 2619   | Layout 1 | `05812a69f476`  |
| 2612   | Layout 1 | `05812a69f476`  |
| 2606   | Layout 1 | `05812a69f476`  |
| 2602   | Layout 1 | `05812a69f476`  |
| 2601   | Layout 1 | `05812a69f476`  |
| 2592   | Layout 1 | `05812a69f476`  |
| 2583   | Layout 1 | `05812a69f476`  |
| 2575   | Layout 1 | `05812a69f476`  |
| 2567   | Layout 1 | `05812a69f476`  |
| 2560   | Layout 1 | `05812a69f476`  |
| 2553   | No file  | `05812a69f476`  |
| 2545   | No file  | `05812a69f476`  |
| 2538   | No file  | `05812a69f476`  |
| 2529   | No file  | `05812a69f476`  |
| 2519   | No file  | `05812a69f476`  |
| 2513   | No file  | `05812a69f476`  |
| 2510   | No file  | `05812a69f476`  |
| 2507   | No file  | `05812a69f476`  |
| 2503   | No file  | `05812a69f476`  |
| 2498   | No file  | `05812a69f476`  |
| 2492   | No file  | `05812a69f476`  |
| 2487   | No file  | `05812a69f476`  |
| 2480   | No file  | `05812a69f476`  |
| 2474   | No file  | `05812a69f476`  |
| 2468   | No file  | `05812a69f476`  |
| 2460   | No file  | `05812a69f476`  |
| 2453   | No file  | `05812a69f476`  |
| 2444   | No file  | `05812a69f476`  |
| 2438   | No file  | `05812a69f476`  |
| 2434   | No file  | `05812a69f476`  |
| 2429   | No file  | `05812a69f476`  |
| 2421   | No file  | `05812a69f476`  |
| 2414   | No file  | `05812a69f476`  |
| 2407   | No file  | `05812a69f476`  |
| 2401   | No file  | `05812a69f476`  |
| 2397   | No file  | `05812a69f476`  |
| 2393   | No file  | `05812a69f476`  |
| 2384   | No file  | `05812a69f476`  |
| 2378   | No file  | `05812a69f476`  |
| 2372   | No file  | `05812a69f476`  |
| 2358   | No file  | `05812a69f476`  |
| 2352   | No file  | `05812a69f476`  |
| 2347   | No file  | `05812a69f476`  |
| 2343   | No file  | `05812a69f476`  |
| 2335   | No file  | `05812a69f476`  |
| 2327   | No file  | `05812a69f476`  |
| 2324   | No file  | `05812a69f476`  |
| 2319   | No file  | `05812a69f476`  |
| 2313   | No file  | `05812a69f476`  |
| 2308   | No file  | `05812a69f476`  |
| 2302   | No file  | `05812a69f476`  |
| 2295   | No file  | `05812a69f476`  |
| 2290   | No file  | `05812a69f476`  |
| 2284   | No file  | `05812a69f476`  |
| 2276   | No file  | `05812a69f476`  |
| 2269   | No file  | `05812a69f476`  |
| 2259   | No file  | `05812a69f476`  |
| 2250   | No file  | `05812a69f476`  |
| 2243   | No file  | `05812a69f476`  |
| 2235   | No file  | `05812a69f476`  |
| 2229   | No file  | `05812a69f476`  |
| 2224   | No file  | `05812a69f476`  |
| 2218   | No file  | `05812a69f476`  |
| 2215   | No file  | `05812a69f476`  |
| 2207   | No file  | `05812a69f476`  |
| 2203   | No file  | `05812a69f476`  |
| 2196   | No file  | `05812a69f476`  |
| 2192   | No file  | `05812a69f476`  |
| 2189   | No file  | `05812a69f476`  |
| 2183   | No file  | `05812a69f476`  |
| 2179   | No file  | `05812a69f476`  |
| 2171   | No file  | `05812a69f476`  |
| 2163   | No file  | `05812a69f476`  |
| 2156   | No file  | `05812a69f476`  |
| 2151   | No file  | `05812a69f476`  |
| 2147   | No file  | `05812a69f476`  |
| 2142   | No file  | `05812a69f476`  |
| 2138   | No file  | `05812a69f476`  |
| 2134   | No file  | `05812a69f476`  |
| 2130   | No file  | `05812a69f476`  |
| 2122   | No file  | `05812a69f476`  |
| 2107   | No file  | `05812a69f476`  |
| 2098   | No file  | `05812a69f476`  |
| 2089   | No file  | `05812a69f476`  |
| 2081   | No file  | `05812a69f476`  |
| 2073   | No file  | `05812a69f476`  |
| 2067   | No file  | `05812a69f476`  |
| 2063   | No file  | `05812a69f476`  |
| 2059   | No file  | `05812a69f476`  |
| 2052   | No file  | `05812a69f476`  |
| 2044   | No file  | `05812a69f476`  |
| 2039   | No file  | `05812a69f476`  |
| 2032   | No file  | `05812a69f476`  |
| 2025   | No file  | `05812a69f476`  |
| 2011   | No file  | `05812a69f476`  |
| 2005   | No file  | `05812a69f476`  |
| 2000   | No file  | `05812a69f476`  |
| 1996   | No file  | `05812a69f476`  |
| 1991   | No file  | `05812a69f476`  |
| 1985   | No file  | `05812a69f476`  |
| 1980   | No file  | `05812a69f476`  |
| 1969   | No file  | `05812a69f476`  |
| 1964   | No file  | `05812a69f476`  |
| 1958   | No file  | `05812a69f476`  |
| 1950   | No file  | `05812a69f476`  |
| 1945   | No file  | `05812a69f476`  |
| 1937   | No file  | `05812a69f476`  |
| 1933   | No file  | `05812a69f476`  |
| 1927   | No file  | `05812a69f476`  |
| 1921   | No file  | `05812a69f476`  |
| 1914   | No file  | `05812a69f476`  |
| 1908   | No file  | `05812a69f476`  |
| 1897   | No file  | `05812a69f476`  |
| 1892   | No file  | `05812a69f476`  |
| 1886   | No file  | `05812a69f476`  |
| 1881   | No file  | `05812a69f476`  |
| 1871   | No file  | `05812a69f476`  |
| 1866   | No file  | `05812a69f476`  |
| 1862   | No file  | `05812a69f476`  |
| 1854   | No file  | `05812a69f476`  |
| 1846   | No file  | `05812a69f476`  |
| 1838   | No file  | `05812a69f476`  |
| 1832   | No file  | `05812a69f476`  |
| 1826   | No file  | `05812a69f476`  |
| 1822   | No file  | `05812a69f476`  |
| 1818   | No file  | `05812a69f476`  |
| 1804   | No file  | `05812a69f476`  |
| 1794   | No file  | `05812a69f476`  |
| 1790   | No file  | `05812a69f476`  |
| 1784   | No file  | `05812a69f476`  |
| 1774   | No file  | `05812a69f476`  |
| 1771   | No file  | `05812a69f476`  |
| 1762   | No file  | `05812a69f476`  |
| 1759   | No file  | `05812a69f476`  |
| 1754   | No file  | `05812a69f476`  |
| 1749   | No file  | `05812a69f476`  |
| 1743   | No file  | `05812a69f476`  |
| 1737   | No file  | `05812a69f476`  |
| 1731   | No file  | `05812a69f476`  |
| 1725   | No file  | `05812a69f476`  |
| 1717   | No file  | `05812a69f476`  |
| 1710   | No file  | `05812a69f476`  |
| 1704   | No file  | `05812a69f476`  |
| 1698   | No file  | `05812a69f476`  |
| 1690   | No file  | `05812a69f476`  |
| 1685   | No file  | `05812a69f476`  |
| 1680   | No file  | `05812a69f476`  |
| 1674   | No file  | `05812a69f476`  |
| 1668   | No file  | `05812a69f476`  |
| 1659   | No file  | `05812a69f476`  |
| 1649   | No file  | `05812a69f476`  |
| 1642   | No file  | `05812a69f476`  |
| 1636   | No file  | `05812a69f476`  |
| 1628   | No file  | `05812a69f476`  |
| 1622   | No file  | `05812a69f476`  |
| 1614   | No file  | `05812a69f476`  |
| 1608   | No file  | `05812a69f476`  |
| 1602   | No file  | `05812a69f476`  |
| 1598   | No file  | `05812a69f476`  |
| 1594   | No file  | `05812a69f476`  |
| 1590   | No file  | `05812a69f476`  |
| 1587   | No file  | `05812a69f476`  |
| 1584   | No file  | `05812a69f476`  |
| 1579   | No file  | `05812a69f476`  |
| 1572   | No file  | `05812a69f476`  |
| 1565   | No file  | `05812a69f476`  |
| 1559   | No file  | `05812a69f476`  |
| 1554   | No file  | `05812a69f476`  |
| 1547   | No file  | `05812a69f476`  |
| 1537   | No file  | `05812a69f476`  |
| 1529   | No file  | `05812a69f476`  |
| 1524   | No file  | `05812a69f476`  |
| 1519   | No file  | `05812a69f476`  |
| 1509   | No file  | `05812a69f476`  |
| 1506   | No file  | `05812a69f476`  |
| 1504   | No file  | `05812a69f476`  |
| 1500   | No file  | `05812a69f476`  |
| 1493   | No file  | `05812a69f476`  |
| 1489   | No file  | `05812a69f476`  |
| 1485   | No file  | `05812a69f476`  |
| 1481   | No file  | `05812a69f476`  |
| 1474   | No file  | `05812a69f476`  |
| 1466   | No file  | `05812a69f476`  |
| 1462   | No file  | `05812a69f476`  |
| 1459   | No file  | `05812a69f476`  |
| 1453   | No file  | `05812a69f476`  |
| 1450   | No file  | `05812a69f476`  |
| 1445   | No file  | `05812a69f476`  |
| 1439   | No file  | `05812a69f476`  |
| 1433   | No file  | `05812a69f476`  |
| 1430   | No file  | `05812a69f476`  |
| 1426   | No file  | `05812a69f476`  |
| 1421   | No file  | `05812a69f476`  |
| 1417   | No file  | `05812a69f476`  |
| 1416   | No file  | `05812a69f476`  |
| 1409   | No file  | `05812a69f476`  |
| 1405   | No file  | `05812a69f476`  |
| 1401   | No file  | `05812a69f476`  |
| 1396   | No file  | `05812a69f476`  |
| 1391   | No file  | `05812a69f476`  |
| 1390   | No file  | `05812a69f476`  |
| 1386   | No file  | `05812a69f476`  |
| 1381   | No file  | `05812a69f476`  |
| 1379   | No file  | `05812a69f476`  |
| 1372   | No file  | `05812a69f476`  |
| 1366   | No file  | `05812a69f476`  |
| 1364   | No file  | `05812a69f476`  |
| 1363   | No file  | `05812a69f476`  |
| 1360   | No file  | `05812a69f476`  |
| 1358   | No file  | `05812a69f476`  |
| 1355   | No file  | `05812a69f476`  |
| 1351   | No file  | `05812a69f476`  |
| 1348   | No file  | `05812a69f476`  |
| 1346   | No file  | `05812a69f476`  |
| 1341   | No file  | `05812a69f476`  |
| 1340   | No file  | `05812a69f476`  |
| 1338   | No file  | `05812a69f476`  |
| 1335   | No file  | `05812a69f476`  |
| 1333   | No file  | `05812a69f476`  |
| 1329   | No file  | `05812a69f476`  |
| 1327   | No file  | `05812a69f476`  |
| 1324   | No file  | `05812a69f476`  |
| 1321   | No file  | `05812a69f476`  |
| 1319   | No file  | `05812a69f476`  |
| 1318   | No file  | `05812a69f476`  |
| 1316   | No file  | `05812a69f476`  |
| 1313   | No file  | `05812a69f476`  |
| 1311   | No file  | `05812a69f476`  |
| 1309   | No file  | `05812a69f476`  |
| 1304   | No file  | `05812a69f476`  |
| 1292   | No file  | `05812a69f476`  |
| 1286   | No file  | `05812a69f476`  |
| 1280   | No file  | `05812a69f476`  |
| 1276   | No file  | `05812a69f476`  |
| 1267   | No file  | `05812a69f476`  |
| 1261   | No file  | `05812a69f476`  |
| 1256   | No file  | `05812a69f476`  |
| 1250   | No file  | `05812a69f476`  |
| 1246   | No file  | `05812a69f476`  |
| 1239   | No file  | `05812a69f476`  |
| 1230   | No file  | `05812a69f476`  |
| 1226   | No file  | `05812a69f476`  |
| 1220   | No file  | `05812a69f476`  |
| 1217   | No file  | `05812a69f476`  |
| 1211   | No file  | `05812a69f476`  |
| 1210   | No file  | `05812a69f476`  |
| 1208   | No file  | `05812a69f476`  |
| 1203   | No file  | `05812a69f476`  |
| 1197   | No file  | `05812a69f476`  |
| 1194   | No file  | `05812a69f476`  |
| 1192   | No file  | `05812a69f476`  |
| 1187   | No file  | `05812a69f476`  |
| 1183   | No file  | `05812a69f476`  |
| 1177   | No file  | `05812a69f476`  |
| 1173   | No file  | `05812a69f476`  |
| 1167   | No file  | `05812a69f476`  |
| 1164   | No file  | `05812a69f476`  |
| 1156   | No file  | `05812a69f476`  |
| 1149   | No file  | `05812a69f476`  |
| 1144   | No file  | `05812a69f476`  |
| 1137   | No file  | `05812a69f476`  |
| 1132   | No file  | `05812a69f476`  |
| 1127   | No file  | `05812a69f476`  |
| 1122   | No file  | `05812a69f476`  |
| 1118   | No file  | `05812a69f476`  |
| 1114   | No file  | `05812a69f476`  |
| 1109   | No file  | `05812a69f476`  |
| 1102   | No file  | `05812a69f476`  |
| 1096   | No file  | `05812a69f476`  |
| 1088   | No file  | `05812a69f476`  |
| 1081   | No file  | `05812a69f476`  |
| 1076   | No file  | `05812a69f476`  |
| 1069   | No file  | `05812a69f476`  |
| 1064   | No file  | `05812a69f476`  |
| 1058   | No file  | `05812a69f476`  |
| 1051   | No file  | `05812a69f476`  |
| 1044   | No file  | `05812a69f476`  |
| 1036   | No file  | `05812a69f476`  |
| 1026   | No file  | `05812a69f476`  |
| 1016   | No file  | `05812a69f476`  |
| 1009   | No file  | `05812a69f476`  |
| 1005   | No file  | `05812a69f476`  |
| 1000   | No file  | `05812a69f476`  |
| 998    | No file  | `05812a69f476`  |
| 990    | No file  | `05812a69f476`  |
| 979    | No file  | `05812a69f476`  |
| 972    | No file  | `05812a69f476`  |
| 963    | No file  | `05812a69f476`  |
| 955    | No file  | `05812a69f476`  |
| 946    | No file  | `05812a69f476`  |
| 938    | No file  | `05812a69f476`  |
| 927    | No file  | `05812a69f476`  |
| 911    | No file  | `05812a69f476`  |
| 904    | No file  | `05812a69f476`  |
| 899    | No file  | `05812a69f476`  |
| 894    | No file  | `05812a69f476`  |
| 885    | No file  | `05812a69f476`  |
| 879    | No file  | `05812a69f476`  |
| 872    | No file  | `05812a69f476`  |
| 864    | No file  | `05812a69f476`  |
| 855    | No file  | `05812a69f476`  |
| 853    | No file  | `05812a69f476`  |
| 845    | No file  | `05812a69f476`  |
| 837    | No file  | `05812a69f476`  |
| 829    | No file  | `05812a69f476`  |
| 822    | No file  | `05812a69f476`  |
| 814    | No file  | `05812a69f476`  |
| 805    | No file  | `05812a69f476`  |
| 794    | No file  | `05812a69f476`  |
| 787    | No file  | `05812a69f476`  |
| 780    | No file  | `05812a69f476`  |
| 771    | No file  | `05812a69f476`  |
| 760    | No file  | `05812a69f476`  |
| 748    | No file  | `05812a69f476`  |
| 741    | No file  | `05812a69f476`  |
| 736    | No file  | `05812a69f476`  |
| 731    | No file  | `05812a69f476`  |
| 723    | No file  | `05812a69f476`  |
| 711    | No file  | `05812a69f476`  |
| 707    | No file  | `05812a69f476`  |
| 697    | No file  | `05812a69f476`  |
| 689    | No file  | `05812a69f476`  |
| 683    | No file  | `05812a69f476`  |
| 678    | No file  | `05812a69f476`  |
| 670    | No file  | `05812a69f476`  |
| 661    | No file  | `05812a69f476`  |
| 656    | No file  | `05812a69f476`  |
| 652    | No file  | `05812a69f476`  |
| 643    | No file  | `05812a69f476`  |
| 637    | No file  | `05812a69f476`  |
| 630    | No file  | `05812a69f476`  |
| 627    | No file  | `05812a69f476`  |
| 621    | No file  | `05812a69f476`  |
| 617    | No file  | `05812a69f476`  |
| 615    | No file  | `05812a69f476`  |
| 606    | No file  | `05812a69f476`  |
| 599    | No file  | `05812a69f476`  |
| 592    | No file  | `05812a69f476`  |
| 586    | No file  | `05812a69f476`  |
| 577    | No file  | `05812a69f476`  |
| 569    | No file  | `05812a69f476`  |
| 561    | No file  | `05812a69f476`  |
| 554    | No file  | `05812a69f476`  |
| 542    | No file  | `05812a69f476`  |
| 532    | No file  | `05812a69f476`  |
| 531    | No file  | `05812a69f476`  |
| 526    | No file  | `05812a69f476`  |
| 521    | No file  | `05812a69f476`  |
| 517    | No file  | `05812a69f476`  |
| 510    | No file  | `05812a69f476`  |
| 508    | No file  | `05812a69f476`  |
| 504    | No file  | `05812a69f476`  |
| 497    | No file  | `05812a69f476`  |
| 491    | No file  | `05812a69f476`  |
| 485    | No file  | `05812a69f476`  |
| 478    | No file  | `05812a69f476`  |
| 472    | No file  | `05812a69f476`  |
| 466    | No file  | `05812a69f476`  |
| 457    | No file  | `05812a69f476`  |
| 452    | No file  | `05812a69f476`  |
| 449    | No file  | `05812a69f476`  |
| 435    | No file  | `05812a69f476`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                               |
| ------------------- | ------------ | ------------ | --------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                        |
| `+0x04`             | Grid Block   | grid_block   | See Grid Block                                      |
| `grid_block+0x00`   | Tier Block   | tier_block   | See Tier Block                                      |
| `tier_block+0x00`   | String Table | string_table | See String Table                                    |
| `string_table+0x00` | u32          | table_start  | Offset of the string table, where `tier_block` ends |
| `string_table+0x04` | u32          | zero         | Always `0`                                          |

### Grid Block (variable: 70 bytes + tier grids)

| Offset             | Type                       | Field           | Notes                                              |
| ------------------ | -------------------------- | --------------- | -------------------------------------------------- |
| `+0x00`            | u32                        | medal_item_id   | Item ID of the medals the `plus_medal_counts` give; `2` (Gold Bar 1G) on client 3482 |
| `+0x04`            | u16                        | tier_grid_count | Number of `tier_grids`; `4` on every client checked |
| `+0x06`            | Tier Grid[tier_grid_count] | tier_grids      | See Tier Grid; the four are byte for byte the same on client 3482 |
| `tier_grids+0x00`  | Major Rewards              | major_rewards   | See Major Rewards                                  |

### Tier Grid (48 bytes)

| Offset  | Type   | Field             | Notes                                                    |
| ------- | ------ | ----------------- | -------------------------------------------------------- |
| `+0x00` | u16[4] | unknown_00        | One per tier: `12, 16, 20, 24` on client 3482            |
| `+0x08` | u16[4] | unknown_08        | `12, 16, 20, 24`                                         |
| `+0x10` | u16[4] | unknown_10        | `12, 16, 20, 24`                                         |
| `+0x18` | u16[4] | plus_medal_counts | Medals per tier: `5, 5, 5, 5`                            |
| `+0x20` | u32[4] | plus_item_ids     | Plus item per tier: `44392, 44392, 44391, 44391` (Battlefield Honor, Battlefield Glory) |

### Tier Block (variable: 70 bytes + tiers)

| Offset        | Type             | Field         | Notes                                               |
| ------------- | ---------------- | ------------- | --------------------------------------------------- |
| `+0x00`       | u32              | medal_item_id | As in the Grid Block; `2` on client 3482            |
| `+0x04`       | u16              | tier_count    | Number of `tiers`; `4` on every client checked      |
| `+0x06`       | Tier[tier_count] | tiers         | See Tier                                            |
| `tiers+0x00`  | Major Rewards    | major_rewards | See Major Rewards                                   |

### Tier (24 bytes)

| Offset  | Type | Field                  | Notes                                                        |
| ------- | ---- | ---------------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | win_reward_count       | `1` on every tier of client 3482                             |
| `+0x02` | u16  | lose_reward_count      | `1`                                                          |
| `+0x04` | u16  | release_reward_count   | `1`                                                          |
| `+0x06` | u16  | plus_medal_count       | Medals of `medal_item_id`; `5`                               |
| `+0x08` | u32  | win_reward_item_id     | A Triumph Reward: Fervent, Determined, Kindling, Blazing      |
| `+0x0C` | u32  | lose_reward_item_id    | The Resolve Reward of the same name                          |
| `+0x10` | u32  | release_reward_item_id | The same item as `lose_reward_item_id` on client 3482        |
| `+0x14` | u32  | plus_item_id           | `44392, 44392, 44391, 44391` by tier                         |

### Major Rewards (64 bytes)

| Offset  | Type             | Field                     | Notes                                                    |
| ------- | ---------------- | ------------------------- | -------------------------------------------------------- |
| `+0x00` | u16              | win_medal_count           | `1` in both blocks on client 3482                        |
| `+0x02` | u16              | lose_medal_count          | `1`                                                      |
| `+0x04` | u16              | release_medal_count       | `1`                                                      |
| `+0x06` | u16              | plus_medal_count          | `5`                                                      |
| `+0x08` | u32              | plus_item_id              | `44391` Battlefield Glory                                |
| `+0x0C` | u32              | win_medal_item_id         | Glorious Victor Reward: `45964`, `761591` (Tier Block)   |
| `+0x10` | u32              | lose_medal_item_id        | Fighting Spirit Reward: `45971`, `761598`                |
| `+0x14` | u32              | release_medal_item_id     | Burning Inspiration Reward: `45970`, `761597`            |
| `+0x18` | u32              | plus_medal_item_id        | The same as the block's `medal_item_id`                  |
| `+0x1C` | Release Medal[5] | release_medals            | Score 2nd to 6th: Burning Spirit Reward (V) to (I)       |
| `+0x3A` | u32              | release_win_medal_item_id | Score 1st: Burning Spirit Victor Reward, `59796`, `761590` |
| `+0x3E` | u16              | release_win_medal_count   | `1`                                                      |

### Release Medal (6 bytes)

| Offset  | Type | Field   | Notes                                                  |
| ------- | ---- | ------- | ------------------------------------------------------ |
| `+0x00` | u16  | count   | `1` on client 3482                                     |
| `+0x02` | u32  | item_id | `45965` to `45969` (Grid Block), `761592` to `761596` (Tier Block) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names come from the `SiegeReward` sheet of a private server's
`DataSheets.bexcel` on client 1784 (keyed by `PA_GAME_SERVICE_TYPE`; the
file is not in that client's archives). The Grid Block's Major Rewards
match its Conquest War columns by value, 21 of 21 on client 3002, where
the medal was still the sheet's `15692`: `WinMedal_Major`,
`LoseMedal_Major`, `ReleaseMedal_Major` and `PlusMedal_Major` (`1, 1, 1,
5`), `PlusItem_Major` (`44391`), `MajorWinMedal_ItemKey` (`45964`),
`MajorLoseMedal_ItemKey` (`45971`), `MajorReleaseMedal_ItemKey`
(`45970`), `MajorPlusMedal_ItemKey` (`15692`), the five
`ReleaseMedal_Major_N` and `MajorReleaseMedal_ItemKey_N` pairs (`1`,
`45965` to `45969`), `MajorReleaseWinMedal_ItemKey` (`59796`) and
`ReleaseWinMedal_Major` (`1`). `medal_item_id` is `MedalItemKey`
(`15692` on clients 2765 and 3002, `2` from client 3251). The LOC type
0 text of the Tier Block's Conquest War items gives the roles: "How to
Obtain: Tier 1 Conquest War victory", "defeat", "liberation", "Score
1st" to "Score 6th", the same as the lists of
[`majorsiegerewardstaticstatus.bss`](majorsiegerewardstaticstatus_bss.md).

A Tier holds the sheet's per-tier columns `WinRewardCount_N`,
`LoseRewardCount_N`, `ReleaseRewardCount_N`, `PlusMedal_N`,
`WinRewardItem_N`, `LoseRewardItem_N`, `ReleaseRewardItem_N` and
`PlusItem_N`: the counts (`1, 1, 1, 5`) and the plus items (`44392,
44392, 44391, 44391`) match for all four tiers; the reward items differ
(the sheet's `45185` to `45196` are older boxes), and the LOC text of the
client 3482 items fits the roles: a Triumph Reward is "issued to those
who achieve glorious victory", a Resolve Reward "to those whose resolve
remained determined". The Tier Grid's `plus_medal_counts` and
`plus_item_ids` match `PlusMedal_0` to `_3` and `PlusItem_0` to `_3`
(8 of 8 per grid).

## Notes

- Every client checked has 444 bytes. Clients 3002 to 3482 differ only
  in the four medal item IDs (`medal_item_id` and `plus_medal_item_id`
  of both blocks): `15692` (Resplendent Medal of Honor) on client 3002,
  `2` (Gold Bar 1G) from client 3251. Client 2765 also has the medal
  `15692`, and the Tier Block's Major Rewards hold other boxes of the
  same names and roles: `65309` Glorious Victor Reward ("Tier 1 Conquest
  War victory"), `65316` Fighting Spirit Reward, `65308` Burning Spirit
  Victor Reward and so on. Client 2637 has the bytes of client 2765.
- The struct packs the four u16 counts of the Major Rewards before the
  item IDs they count, and the release win medal's item ID before its
  count.
- The handler (`_bss/siegerewarddata/`) shows one row per reward slot:
  the item, its count, the reward it is, the tier, the tier grid and the
  block. Per tier and grid the Grid Block gives the medals and the plus
  item; per tier the Tier Block gives the victory, defeat and liberation
  items, the medals and the plus item; each block ends with its eleven
  Conquest War slots. A plus item has no count.

## Open Questions

### What the Tier Grid Stands For

A Tier Grid holds four values per field, one per tier, where a Tier
holds one: `plus_medal_counts` and `plus_item_ids` match the sheet's per
tier medals and plus items. The three u16 arrays before them (`12, 16,
20, 24` each) sit where a Tier holds the victory, defeat and liberation
counts, but no item IDs go with them, and the four grids are the same.
What the grid count stands for (four days, four node levels) and what
`unknown_00` to `unknown_10` count is open; no Lua of client 3482 reads
the file.

### Which Block Is in Use

The Tier Block's items are the current boxes (the Conquest War boxes'
LOC text names Tier 1), while the Grid Block's Major Rewards still hold
the client 1784 items `45964` to `45971` and `59796`, which carry no
"How to Obtain" line. Which block the server reads for which siege is
open.
