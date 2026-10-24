# `monsterselfmanager.bss` Format

## Purpose

A PABR list of monster characters, each with one u32 value. On client
3482 it holds 40 rows, all of the Great Ocean and its pirates: sea
monsters (Nineshark, Black Rust, Candidum, Hekaru, Ocean Stalker,
Saltwater Crocodile, Lyngbakr and their Young versions), the Goldmont
Small, Medium and Large Battleships, the Cursed Pirate Ship and the Cox
Pirates' Shadow Ghost, Barrack and Pirate Flag. The value is `10000` on
every row; what it sets is open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------- | --------- |
| 1      | 2000 and later | 3483    | `monsterselfmanager.bss` | 260   | 40 Row  | 6         |

| Layout | File                     | Known         | Unknown       |
| ------ | ------------------------ | ------------- | ------------- |
| 1      | `monsterselfmanager.bss` | 100 B (38.5%) | 160 B (61.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `9695c8ca006a`  |
| 3482   | Layout 1 | `9695c8ca006a`  |
| 3474   | Layout 1 | `9695c8ca006a`  |
| 3473   | Layout 1 | `9695c8ca006a`  |
| 3464   | Layout 1 | `9695c8ca006a`  |
| 3458   | Layout 1 | `9695c8ca006a`  |
| 3454   | Layout 1 | `9695c8ca006a`  |
| 3444   | Layout 1 | `9695c8ca006a`  |
| 3435   | Layout 1 | `9695c8ca006a`  |
| 3426   | Layout 1 | `9695c8ca006a`  |
| 3418   | Layout 1 | `9695c8ca006a`  |
| 3412   | Layout 1 | `9695c8ca006a`  |
| 3402   | Layout 1 | `9695c8ca006a`  |
| 3396   | Layout 1 | `9695c8ca006a`  |
| 3387   | Layout 1 | `9695c8ca006a`  |
| 3381   | Layout 1 | `9695c8ca006a`  |
| 3373   | Layout 1 | `9695c8ca006a`  |
| 3364   | Layout 1 | `9695c8ca006a`  |
| 3356   | Layout 1 | `9695c8ca006a`  |
| 3349   | Layout 1 | `9695c8ca006a`  |
| 3342   | Layout 1 | `9695c8ca006a`  |
| 3335   | Layout 1 | `9695c8ca006a`  |
| 3326   | Layout 1 | `9695c8ca006a`  |
| 3321   | Layout 1 | `9695c8ca006a`  |
| 3314   | Layout 1 | `9695c8ca006a`  |
| 3303   | Layout 1 | `9695c8ca006a`  |
| 3302   | Layout 1 | `9695c8ca006a`  |
| 3293   | Layout 1 | `9695c8ca006a`  |
| 3283   | Layout 1 | `9695c8ca006a`  |
| 3275   | Layout 1 | `9695c8ca006a`  |
| 3267   | Layout 1 | `9695c8ca006a`  |
| 3258   | Layout 1 | `9695c8ca006a`  |
| 3251   | Layout 1 | `9695c8ca006a`  |
| 3242   | Layout 1 | `9695c8ca006a`  |
| 3235   | Layout 1 | `9695c8ca006a`  |
| 3229   | Layout 1 | `9695c8ca006a`  |
| 3212   | Layout 1 | `9695c8ca006a`  |
| 3203   | Layout 1 | `9695c8ca006a`  |
| 3193   | Layout 1 | `9695c8ca006a`  |
| 3186   | Layout 1 | `9695c8ca006a`  |
| 3177   | Layout 1 | `9695c8ca006a`  |
| 3169   | Layout 1 | `9695c8ca006a`  |
| 3158   | Layout 1 | `9695c8ca006a`  |
| 3151   | Layout 1 | `9695c8ca006a`  |
| 3144   | Layout 1 | `9695c8ca006a`  |
| 3133   | Layout 1 | `9695c8ca006a`  |
| 3125   | Layout 1 | `9695c8ca006a`  |
| 3118   | Layout 1 | `9695c8ca006a`  |
| 3111   | Layout 1 | `9695c8ca006a`  |
| 3103   | Layout 1 | `9695c8ca006a`  |
| 3095   | Layout 1 | `9695c8ca006a`  |
| 3086   | Layout 1 | `9695c8ca006a`  |
| 3072   | Layout 1 | `9695c8ca006a`  |
| 3062   | Layout 1 | `9695c8ca006a`  |
| 3052   | Layout 1 | `9695c8ca006a`  |
| 3045   | Layout 1 | `9695c8ca006a`  |
| 3037   | Layout 1 | `9695c8ca006a`  |
| 3030   | Layout 1 | `9695c8ca006a`  |
| 3021   | Layout 1 | `9695c8ca006a`  |
| 3012   | Layout 1 | `9695c8ca006a`  |
| 3002   | Layout 1 | `9695c8ca006a`  |
| 2995   | Layout 1 | `9695c8ca006a`  |
| 2987   | Layout 1 | `9695c8ca006a`  |
| 2978   | Layout 1 | `9695c8ca006a`  |
| 2970   | Layout 1 | `9695c8ca006a`  |
| 2959   | Layout 1 | `9695c8ca006a`  |
| 2951   | Layout 1 | `9695c8ca006a`  |
| 2942   | Layout 1 | `9695c8ca006a`  |
| 2935   | Layout 1 | `9695c8ca006a`  |
| 2932   | Layout 1 | `9695c8ca006a`  |
| 2923   | Layout 1 | `9695c8ca006a`  |
| 2919   | Layout 1 | `9695c8ca006a`  |
| 2907   | Layout 1 | `9695c8ca006a`  |
| 2900   | Layout 1 | `9695c8ca006a`  |
| 2891   | Layout 1 | `9695c8ca006a`  |
| 2882   | Layout 1 | `9695c8ca006a`  |
| 2872   | Layout 1 | `9695c8ca006a`  |
| 2863   | Layout 1 | `9695c8ca006a`  |
| 2855   | Layout 1 | `9695c8ca006a`  |
| 2849   | Layout 1 | `9695c8ca006a`  |
| 2844   | Layout 1 | `9695c8ca006a`  |
| 2834   | Layout 1 | `9695c8ca006a`  |
| 2825   | Layout 1 | `9695c8ca006a`  |
| 2819   | Layout 1 | `9695c8ca006a`  |
| 2811   | Layout 1 | `9695c8ca006a`  |
| 2803   | Layout 1 | `9695c8ca006a`  |
| 2794   | Layout 1 | `9695c8ca006a`  |
| 2783   | Layout 1 | `9695c8ca006a`  |
| 2774   | Layout 1 | `9695c8ca006a`  |
| 2765   | Layout 1 | `9695c8ca006a`  |
| 2756   | Layout 1 | `9695c8ca006a`  |
| 2750   | Layout 1 | `9695c8ca006a`  |
| 2743   | Layout 1 | `9695c8ca006a`  |
| 2736   | Layout 1 | `9695c8ca006a`  |
| 2726   | Layout 1 | `9695c8ca006a`  |
| 2717   | Layout 1 | `9695c8ca006a`  |
| 2709   | Layout 1 | `9695c8ca006a`  |
| 2703   | Layout 1 | `9695c8ca006a`  |
| 2695   | Layout 1 | `9695c8ca006a`  |
| 2684   | Layout 1 | `9695c8ca006a`  |
| 2672   | Layout 1 | `9695c8ca006a`  |
| 2665   | Layout 1 | `9695c8ca006a`  |
| 2657   | Layout 1 | `9695c8ca006a`  |
| 2649   | Layout 1 | `9695c8ca006a`  |
| 2644   | Layout 1 | `9695c8ca006a`  |
| 2637   | Layout 1 | `9695c8ca006a`  |
| 2629   | Layout 1 | `9695c8ca006a`  |
| 2619   | Layout 1 | `9695c8ca006a`  |
| 2612   | Layout 1 | `9695c8ca006a`  |
| 2606   | Layout 1 | `9695c8ca006a`  |
| 2602   | Layout 1 | `9695c8ca006a`  |
| 2601   | Layout 1 | `9695c8ca006a`  |
| 2592   | Layout 1 | `9695c8ca006a`  |
| 2583   | Layout 1 | `9695c8ca006a`  |
| 2575   | Layout 1 | `9695c8ca006a`  |
| 2567   | Layout 1 | `9695c8ca006a`  |
| 2560   | Layout 1 | `9695c8ca006a`  |
| 2553   | Layout 1 | `9695c8ca006a`  |
| 2545   | Layout 1 | `9695c8ca006a`  |
| 2538   | Layout 1 | `9695c8ca006a`  |
| 2529   | Layout 1 | `9695c8ca006a`  |
| 2519   | Layout 1 | `9695c8ca006a`  |
| 2513   | Layout 1 | `9695c8ca006a`  |
| 2510   | Layout 1 | `9695c8ca006a`  |
| 2507   | Layout 1 | `9695c8ca006a`  |
| 2503   | Layout 1 | `9695c8ca006a`  |
| 2498   | Layout 1 | `9695c8ca006a`  |
| 2492   | Layout 1 | `9695c8ca006a`  |
| 2487   | Layout 1 | `9695c8ca006a`  |
| 2480   | Layout 1 | `9695c8ca006a`  |
| 2474   | Layout 1 | `9695c8ca006a`  |
| 2468   | Layout 1 | `9695c8ca006a`  |
| 2460   | Layout 1 | `9695c8ca006a`  |
| 2453   | Layout 1 | `9695c8ca006a`  |
| 2444   | Layout 1 | `9695c8ca006a`  |
| 2438   | Layout 1 | `9695c8ca006a`  |
| 2434   | Layout 1 | `9695c8ca006a`  |
| 2429   | Layout 1 | `9695c8ca006a`  |
| 2421   | Layout 1 | `9695c8ca006a`  |
| 2414   | Layout 1 | `9695c8ca006a`  |
| 2407   | Layout 1 | `9695c8ca006a`  |
| 2401   | Layout 1 | `9695c8ca006a`  |
| 2397   | Layout 1 | `9695c8ca006a`  |
| 2393   | Layout 1 | `9695c8ca006a`  |
| 2384   | Layout 1 | `9695c8ca006a`  |
| 2378   | Layout 1 | `9695c8ca006a`  |
| 2372   | Layout 1 | `9695c8ca006a`  |
| 2358   | Layout 1 | `9695c8ca006a`  |
| 2352   | Layout 1 | `9695c8ca006a`  |
| 2347   | Layout 1 | `9695c8ca006a`  |
| 2343   | Layout 1 | `9695c8ca006a`  |
| 2335   | Layout 1 | `9695c8ca006a`  |
| 2327   | Layout 1 | `9695c8ca006a`  |
| 2324   | Layout 1 | `9695c8ca006a`  |
| 2319   | Layout 1 | `9695c8ca006a`  |
| 2313   | Layout 1 | `9695c8ca006a`  |
| 2308   | Layout 1 | `9695c8ca006a`  |
| 2302   | Layout 1 | `9695c8ca006a`  |
| 2295   | Layout 1 | `9695c8ca006a`  |
| 2290   | Layout 1 | `9695c8ca006a`  |
| 2284   | Layout 1 | `9695c8ca006a`  |
| 2276   | Layout 1 | `9695c8ca006a`  |
| 2269   | Layout 1 | `9695c8ca006a`  |
| 2259   | Layout 1 | `9695c8ca006a`  |
| 2250   | Layout 1 | `9695c8ca006a`  |
| 2243   | Layout 1 | `9695c8ca006a`  |
| 2235   | Layout 1 | `9695c8ca006a`  |
| 2229   | Layout 1 | `9695c8ca006a`  |
| 2224   | Layout 1 | `9695c8ca006a`  |
| 2218   | Layout 1 | `9695c8ca006a`  |
| 2215   | Layout 1 | `9695c8ca006a`  |
| 2207   | Layout 1 | `9695c8ca006a`  |
| 2203   | Layout 1 | `9695c8ca006a`  |
| 2196   | Layout 1 | `9695c8ca006a`  |
| 2192   | Layout 1 | `9695c8ca006a`  |
| 2189   | Layout 1 | `9695c8ca006a`  |
| 2183   | Layout 1 | `9695c8ca006a`  |
| 2179   | Layout 1 | `9695c8ca006a`  |
| 2171   | Layout 1 | `9695c8ca006a`  |
| 2163   | Layout 1 | `9695c8ca006a`  |
| 2156   | Layout 1 | `9695c8ca006a`  |
| 2151   | Layout 1 | `9695c8ca006a`  |
| 2147   | Layout 1 | `9695c8ca006a`  |
| 2142   | Layout 1 | `9695c8ca006a`  |
| 2138   | Layout 1 | `9695c8ca006a`  |
| 2134   | Layout 1 | `9695c8ca006a`  |
| 2130   | Layout 1 | `9695c8ca006a`  |
| 2122   | Layout 1 | `9695c8ca006a`  |
| 2107   | Layout 1 | `9695c8ca006a`  |
| 2098   | Layout 1 | `9695c8ca006a`  |
| 2089   | Layout 1 | `9695c8ca006a`  |
| 2081   | Layout 1 | `9695c8ca006a`  |
| 2073   | Layout 1 | `9695c8ca006a`  |
| 2067   | Layout 1 | `9695c8ca006a`  |
| 2063   | Layout 1 | `9695c8ca006a`  |
| 2059   | Layout 1 | `9695c8ca006a`  |
| 2052   | Layout 1 | `9695c8ca006a`  |
| 2044   | Layout 1 | `9695c8ca006a`  |
| 2039   | Layout 1 | `9695c8ca006a`  |
| 2032   | Layout 1 | `9695c8ca006a`  |
| 2025   | Layout 1 | `9695c8ca006a`  |
| 2011   | Layout 1 | `9695c8ca006a`  |
| 2005   | Layout 1 | `9695c8ca006a`  |
| 2000   | Layout 1 | `9695c8ca006a`  |
| 1996   | No file  | `9695c8ca006a`  |
| 1991   | No file  | `9695c8ca006a`  |
| 1985   | No file  | `9695c8ca006a`  |
| 1980   | No file  | `9695c8ca006a`  |
| 1969   | No file  | `9695c8ca006a`  |
| 1964   | No file  | `9695c8ca006a`  |
| 1958   | No file  | `9695c8ca006a`  |
| 1950   | No file  | `9695c8ca006a`  |
| 1945   | No file  | `9695c8ca006a`  |
| 1937   | No file  | `9695c8ca006a`  |
| 1933   | No file  | `9695c8ca006a`  |
| 1927   | No file  | `9695c8ca006a`  |
| 1921   | No file  | `9695c8ca006a`  |
| 1914   | No file  | `9695c8ca006a`  |
| 1908   | No file  | `9695c8ca006a`  |
| 1897   | No file  | `9695c8ca006a`  |
| 1892   | No file  | `9695c8ca006a`  |
| 1886   | No file  | `9695c8ca006a`  |
| 1881   | No file  | `9695c8ca006a`  |
| 1871   | No file  | `9695c8ca006a`  |
| 1866   | No file  | `9695c8ca006a`  |
| 1862   | No file  | `9695c8ca006a`  |
| 1854   | No file  | `9695c8ca006a`  |
| 1846   | No file  | `9695c8ca006a`  |
| 1838   | No file  | `9695c8ca006a`  |
| 1832   | No file  | `9695c8ca006a`  |
| 1826   | No file  | `9695c8ca006a`  |
| 1822   | No file  | `9695c8ca006a`  |
| 1818   | No file  | `9695c8ca006a`  |
| 1804   | No file  | `9695c8ca006a`  |
| 1794   | No file  | `9695c8ca006a`  |
| 1790   | No file  | `9695c8ca006a`  |
| 1784   | No file  | `9695c8ca006a`  |
| 1774   | No file  | `9695c8ca006a`  |
| 1771   | No file  | `9695c8ca006a`  |
| 1762   | No file  | `9695c8ca006a`  |
| 1759   | No file  | `9695c8ca006a`  |
| 1754   | No file  | `9695c8ca006a`  |
| 1749   | No file  | `9695c8ca006a`  |
| 1743   | No file  | `9695c8ca006a`  |
| 1737   | No file  | `9695c8ca006a`  |
| 1731   | No file  | `9695c8ca006a`  |
| 1725   | No file  | `9695c8ca006a`  |
| 1717   | No file  | `9695c8ca006a`  |
| 1710   | No file  | `9695c8ca006a`  |
| 1704   | No file  | `9695c8ca006a`  |
| 1698   | No file  | `9695c8ca006a`  |
| 1690   | No file  | `9695c8ca006a`  |
| 1685   | No file  | `9695c8ca006a`  |
| 1680   | No file  | `9695c8ca006a`  |
| 1674   | No file  | `9695c8ca006a`  |
| 1668   | No file  | `9695c8ca006a`  |
| 1659   | No file  | `9695c8ca006a`  |
| 1649   | No file  | `9695c8ca006a`  |
| 1642   | No file  | `9695c8ca006a`  |
| 1636   | No file  | `9695c8ca006a`  |
| 1628   | No file  | `9695c8ca006a`  |
| 1622   | No file  | `9695c8ca006a`  |
| 1614   | No file  | `9695c8ca006a`  |
| 1608   | No file  | `9695c8ca006a`  |
| 1602   | No file  | `9695c8ca006a`  |
| 1598   | No file  | `9695c8ca006a`  |
| 1594   | No file  | `9695c8ca006a`  |
| 1590   | No file  | `9695c8ca006a`  |
| 1587   | No file  | `9695c8ca006a`  |
| 1584   | No file  | `9695c8ca006a`  |
| 1579   | No file  | `9695c8ca006a`  |
| 1572   | No file  | `9695c8ca006a`  |
| 1565   | No file  | `9695c8ca006a`  |
| 1559   | No file  | `9695c8ca006a`  |
| 1554   | No file  | `9695c8ca006a`  |
| 1547   | No file  | `9695c8ca006a`  |
| 1537   | No file  | `9695c8ca006a`  |
| 1529   | No file  | `9695c8ca006a`  |
| 1524   | No file  | `9695c8ca006a`  |
| 1519   | No file  | `9695c8ca006a`  |
| 1509   | No file  | `9695c8ca006a`  |
| 1506   | No file  | `9695c8ca006a`  |
| 1504   | No file  | `9695c8ca006a`  |
| 1500   | No file  | `9695c8ca006a`  |
| 1493   | No file  | `9695c8ca006a`  |
| 1489   | No file  | `9695c8ca006a`  |
| 1485   | No file  | `9695c8ca006a`  |
| 1481   | No file  | `9695c8ca006a`  |
| 1474   | No file  | `9695c8ca006a`  |
| 1466   | No file  | `9695c8ca006a`  |
| 1462   | No file  | `9695c8ca006a`  |
| 1459   | No file  | `9695c8ca006a`  |
| 1453   | No file  | `9695c8ca006a`  |
| 1450   | No file  | `9695c8ca006a`  |
| 1445   | No file  | `9695c8ca006a`  |
| 1439   | No file  | `9695c8ca006a`  |
| 1433   | No file  | `9695c8ca006a`  |
| 1430   | No file  | `9695c8ca006a`  |
| 1426   | No file  | `9695c8ca006a`  |
| 1421   | No file  | `9695c8ca006a`  |
| 1417   | No file  | `9695c8ca006a`  |
| 1416   | No file  | `9695c8ca006a`  |
| 1409   | No file  | `9695c8ca006a`  |
| 1405   | No file  | `9695c8ca006a`  |
| 1401   | No file  | `9695c8ca006a`  |
| 1396   | No file  | `9695c8ca006a`  |
| 1391   | No file  | `9695c8ca006a`  |
| 1390   | No file  | `9695c8ca006a`  |
| 1386   | No file  | `9695c8ca006a`  |
| 1381   | No file  | `9695c8ca006a`  |
| 1379   | No file  | `9695c8ca006a`  |
| 1372   | No file  | `9695c8ca006a`  |
| 1366   | No file  | `9695c8ca006a`  |
| 1364   | No file  | `9695c8ca006a`  |
| 1363   | No file  | `9695c8ca006a`  |
| 1360   | No file  | `9695c8ca006a`  |
| 1358   | No file  | `9695c8ca006a`  |
| 1355   | No file  | `9695c8ca006a`  |
| 1351   | No file  | `9695c8ca006a`  |
| 1348   | No file  | `9695c8ca006a`  |
| 1346   | No file  | `9695c8ca006a`  |
| 1341   | No file  | `9695c8ca006a`  |
| 1340   | No file  | `9695c8ca006a`  |
| 1338   | No file  | `9695c8ca006a`  |
| 1335   | No file  | `9695c8ca006a`  |
| 1333   | No file  | `9695c8ca006a`  |
| 1329   | No file  | `9695c8ca006a`  |
| 1327   | No file  | `9695c8ca006a`  |
| 1324   | No file  | `9695c8ca006a`  |
| 1321   | No file  | `9695c8ca006a`  |
| 1319   | No file  | `9695c8ca006a`  |
| 1318   | No file  | `9695c8ca006a`  |
| 1316   | No file  | `9695c8ca006a`  |
| 1313   | No file  | `9695c8ca006a`  |
| 1311   | No file  | `9695c8ca006a`  |
| 1309   | No file  | `9695c8ca006a`  |
| 1304   | No file  | `9695c8ca006a`  |
| 1292   | No file  | `9695c8ca006a`  |
| 1286   | No file  | `9695c8ca006a`  |
| 1280   | No file  | `9695c8ca006a`  |
| 1276   | No file  | `9695c8ca006a`  |
| 1267   | No file  | `9695c8ca006a`  |
| 1261   | No file  | `9695c8ca006a`  |
| 1256   | No file  | `9695c8ca006a`  |
| 1250   | No file  | `9695c8ca006a`  |
| 1246   | No file  | `9695c8ca006a`  |
| 1239   | No file  | `9695c8ca006a`  |
| 1230   | No file  | `9695c8ca006a`  |
| 1226   | No file  | `9695c8ca006a`  |
| 1220   | No file  | `9695c8ca006a`  |
| 1217   | No file  | `9695c8ca006a`  |
| 1211   | No file  | `9695c8ca006a`  |
| 1210   | No file  | `9695c8ca006a`  |
| 1208   | No file  | `9695c8ca006a`  |
| 1203   | No file  | `9695c8ca006a`  |
| 1197   | No file  | `9695c8ca006a`  |
| 1194   | No file  | `9695c8ca006a`  |
| 1192   | No file  | `9695c8ca006a`  |
| 1187   | No file  | `9695c8ca006a`  |
| 1183   | No file  | `9695c8ca006a`  |
| 1177   | No file  | `9695c8ca006a`  |
| 1173   | No file  | `9695c8ca006a`  |
| 1167   | No file  | `9695c8ca006a`  |
| 1164   | No file  | `9695c8ca006a`  |
| 1156   | No file  | `9695c8ca006a`  |
| 1149   | No file  | `9695c8ca006a`  |
| 1144   | No file  | `9695c8ca006a`  |
| 1137   | No file  | `9695c8ca006a`  |
| 1132   | No file  | `9695c8ca006a`  |
| 1127   | No file  | `9695c8ca006a`  |
| 1122   | No file  | `9695c8ca006a`  |
| 1118   | No file  | `9695c8ca006a`  |
| 1114   | No file  | `9695c8ca006a`  |
| 1109   | No file  | `9695c8ca006a`  |
| 1102   | No file  | `9695c8ca006a`  |
| 1096   | No file  | `9695c8ca006a`  |
| 1088   | No file  | `9695c8ca006a`  |
| 1081   | No file  | `9695c8ca006a`  |
| 1076   | No file  | `9695c8ca006a`  |
| 1069   | No file  | `9695c8ca006a`  |
| 1064   | No file  | `9695c8ca006a`  |
| 1058   | No file  | `9695c8ca006a`  |
| 1051   | No file  | `9695c8ca006a`  |
| 1044   | No file  | `9695c8ca006a`  |
| 1036   | No file  | `9695c8ca006a`  |
| 1026   | No file  | `9695c8ca006a`  |
| 1016   | No file  | `9695c8ca006a`  |
| 1009   | No file  | `9695c8ca006a`  |
| 1005   | No file  | `9695c8ca006a`  |
| 1000   | No file  | `9695c8ca006a`  |
| 998    | No file  | `9695c8ca006a`  |
| 990    | No file  | `9695c8ca006a`  |
| 979    | No file  | `9695c8ca006a`  |
| 972    | No file  | `9695c8ca006a`  |
| 963    | No file  | `9695c8ca006a`  |
| 955    | No file  | `9695c8ca006a`  |
| 946    | No file  | `9695c8ca006a`  |
| 938    | No file  | `9695c8ca006a`  |
| 927    | No file  | `9695c8ca006a`  |
| 911    | No file  | `9695c8ca006a`  |
| 904    | No file  | `9695c8ca006a`  |
| 899    | No file  | `9695c8ca006a`  |
| 894    | No file  | `9695c8ca006a`  |
| 885    | No file  | `9695c8ca006a`  |
| 879    | No file  | `9695c8ca006a`  |
| 872    | No file  | `9695c8ca006a`  |
| 864    | No file  | `9695c8ca006a`  |
| 855    | No file  | `9695c8ca006a`  |
| 853    | No file  | `9695c8ca006a`  |
| 845    | No file  | `9695c8ca006a`  |
| 837    | No file  | `9695c8ca006a`  |
| 829    | No file  | `9695c8ca006a`  |
| 822    | No file  | `9695c8ca006a`  |
| 814    | No file  | `9695c8ca006a`  |
| 805    | No file  | `9695c8ca006a`  |
| 794    | No file  | `9695c8ca006a`  |
| 787    | No file  | `9695c8ca006a`  |
| 780    | No file  | `9695c8ca006a`  |
| 771    | No file  | `9695c8ca006a`  |
| 760    | No file  | `9695c8ca006a`  |
| 748    | No file  | `9695c8ca006a`  |
| 741    | No file  | `9695c8ca006a`  |
| 736    | No file  | `9695c8ca006a`  |
| 731    | No file  | `9695c8ca006a`  |
| 723    | No file  | `9695c8ca006a`  |
| 711    | No file  | `9695c8ca006a`  |
| 707    | No file  | `9695c8ca006a`  |
| 697    | No file  | `9695c8ca006a`  |
| 689    | No file  | `9695c8ca006a`  |
| 683    | No file  | `9695c8ca006a`  |
| 678    | No file  | `9695c8ca006a`  |
| 670    | No file  | `9695c8ca006a`  |
| 661    | No file  | `9695c8ca006a`  |
| 656    | No file  | `9695c8ca006a`  |
| 652    | No file  | `9695c8ca006a`  |
| 643    | No file  | `9695c8ca006a`  |
| 637    | No file  | `9695c8ca006a`  |
| 630    | No file  | `9695c8ca006a`  |
| 627    | No file  | `9695c8ca006a`  |
| 621    | No file  | `9695c8ca006a`  |
| 617    | No file  | `9695c8ca006a`  |
| 615    | No file  | `9695c8ca006a`  |
| 606    | No file  | `9695c8ca006a`  |
| 599    | No file  | `9695c8ca006a`  |
| 592    | No file  | `9695c8ca006a`  |
| 586    | No file  | `9695c8ca006a`  |
| 577    | No file  | `9695c8ca006a`  |
| 569    | No file  | `9695c8ca006a`  |
| 561    | No file  | `9695c8ca006a`  |
| 554    | No file  | `9695c8ca006a`  |
| 542    | No file  | `9695c8ca006a`  |
| 532    | No file  | `9695c8ca006a`  |
| 531    | No file  | `9695c8ca006a`  |
| 526    | No file  | `9695c8ca006a`  |
| 521    | No file  | `9695c8ca006a`  |
| 517    | No file  | `9695c8ca006a`  |
| 510    | No file  | `9695c8ca006a`  |
| 508    | No file  | `9695c8ca006a`  |
| 504    | No file  | `9695c8ca006a`  |
| 497    | No file  | `9695c8ca006a`  |
| 491    | No file  | `9695c8ca006a`  |
| 485    | No file  | `9695c8ca006a`  |
| 478    | No file  | `9695c8ca006a`  |
| 472    | No file  | `9695c8ca006a`  |
| 466    | No file  | `9695c8ca006a`  |
| 457    | No file  | `9695c8ca006a`  |
| 452    | No file  | `9695c8ca006a`  |
| 449    | No file  | `9695c8ca006a`  |
| 435    | No file  | `9695c8ca006a`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                             |
| ------- | ---- | ------------- | ----------------------------------------------------------------- |
| `+0x00` | u16  | character_key | `characterstatic.dbss` key; the handler shows its LOC type 6 name |
| `+0x02` | u32  | unknown_02    | `10000` on every row of client 3482                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

Every key resolves to a LOC type 6 character name, so `character_key`
names the meaning. The file is not in the archives of client 1784, no
sheet or column of a private server's `DataSheets.bexcel` on that client
has `SelfManager` in its name, and no client Lua on client 3482 names the
file or calls a getter for it. `unknown_02` stays unknown.

## Notes

- On client 3482 the characters come in key blocks (`21401` to `21405`,
  `21412` to `21430`, `21447` to `21449`, `21480` to `21484`) and single
  keys (`20751`, `20753`, `20754`, `21489`, `28682`, `28827`, `28829`,
  `28834`); several names repeat under different keys.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`: the
  character key and name per row.

## Open Questions

### What the Value Sets

`unknown_02` is `10000` on all 40 rows of client 3482, which would be
100% on a `10000` scale. Every
listed character is a Great Ocean monster, ship or pirate object, so the
file reads as a per-monster setting for that sea, but nothing in the
client Lua or UI XML reads it.
