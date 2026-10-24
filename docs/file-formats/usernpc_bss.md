# `usernpc.bss` Format

## Purpose

The Fishing God NPCs: NPCs that take the look of a player character. Each
row names the player character by its character number, places the NPC in
the world with a position and a facing angle, gives the action it plays
(`FISHING_GOD_WAIT`) and the class it is drawn as. The server dump of a
private server on client 1784 loads the table into `UserNpcStaticStatusManager`
(`loadUserNpcInformation`). The same dump has the database call
`SqlCharacter::getUserNpcCumtomize`; the file itself holds no appearance data.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File          | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------- | ----- | -------------- | --------- |
| 1      | 1506 and later | 3483    | `usernpc.bss` | 99    | 2 User NPC Row | 29        |

| Layout | File          | Known         | Unknown    |
| ------ | ------------- | ------------- | ---------- |
| 1      | `usernpc.bss` | 99 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c12de379c1c3`  |
| 3482   | Layout 1 | `c12de379c1c3`  |
| 3474   | Layout 1 | `c12de379c1c3`  |
| 3473   | Layout 1 | `c12de379c1c3`  |
| 3464   | Layout 1 | `c12de379c1c3`  |
| 3458   | Layout 1 | `c12de379c1c3`  |
| 3454   | Layout 1 | `c12de379c1c3`  |
| 3444   | Layout 1 | `c12de379c1c3`  |
| 3435   | Layout 1 | `c12de379c1c3`  |
| 3426   | Layout 1 | `c12de379c1c3`  |
| 3418   | Layout 1 | `c12de379c1c3`  |
| 3412   | Layout 1 | `c12de379c1c3`  |
| 3402   | Layout 1 | `c12de379c1c3`  |
| 3396   | Layout 1 | `c12de379c1c3`  |
| 3387   | Layout 1 | `c12de379c1c3`  |
| 3381   | Layout 1 | `c12de379c1c3`  |
| 3373   | Layout 1 | `c12de379c1c3`  |
| 3364   | Layout 1 | `c12de379c1c3`  |
| 3356   | Layout 1 | `c12de379c1c3`  |
| 3349   | Layout 1 | `c12de379c1c3`  |
| 3342   | Layout 1 | `c12de379c1c3`  |
| 3335   | Layout 1 | `c12de379c1c3`  |
| 3326   | Layout 1 | `c12de379c1c3`  |
| 3321   | Layout 1 | `c12de379c1c3`  |
| 3314   | Layout 1 | `c12de379c1c3`  |
| 3303   | Layout 1 | `c12de379c1c3`  |
| 3302   | Layout 1 | `c12de379c1c3`  |
| 3293   | Layout 1 | `c12de379c1c3`  |
| 3283   | Layout 1 | `c12de379c1c3`  |
| 3275   | Layout 1 | `c12de379c1c3`  |
| 3267   | Layout 1 | `c12de379c1c3`  |
| 3258   | Layout 1 | `c12de379c1c3`  |
| 3251   | Layout 1 | `c12de379c1c3`  |
| 3242   | Layout 1 | `c12de379c1c3`  |
| 3235   | Layout 1 | `c12de379c1c3`  |
| 3229   | Layout 1 | `c12de379c1c3`  |
| 3212   | Layout 1 | `c12de379c1c3`  |
| 3203   | Layout 1 | `c12de379c1c3`  |
| 3193   | Layout 1 | `c12de379c1c3`  |
| 3186   | Layout 1 | `c12de379c1c3`  |
| 3177   | Layout 1 | `c12de379c1c3`  |
| 3169   | Layout 1 | `c12de379c1c3`  |
| 3158   | Layout 1 | `c12de379c1c3`  |
| 3151   | Layout 1 | `c12de379c1c3`  |
| 3144   | Layout 1 | `c12de379c1c3`  |
| 3133   | Layout 1 | `c12de379c1c3`  |
| 3125   | Layout 1 | `c12de379c1c3`  |
| 3118   | Layout 1 | `c12de379c1c3`  |
| 3111   | Layout 1 | `c12de379c1c3`  |
| 3103   | Layout 1 | `c12de379c1c3`  |
| 3095   | Layout 1 | `c12de379c1c3`  |
| 3086   | Layout 1 | `c12de379c1c3`  |
| 3072   | Layout 1 | `c12de379c1c3`  |
| 3062   | Layout 1 | `c12de379c1c3`  |
| 3052   | Layout 1 | `c12de379c1c3`  |
| 3045   | Layout 1 | `c12de379c1c3`  |
| 3037   | Layout 1 | `c12de379c1c3`  |
| 3030   | Layout 1 | `c12de379c1c3`  |
| 3021   | Layout 1 | `c12de379c1c3`  |
| 3012   | Layout 1 | `c12de379c1c3`  |
| 3002   | Layout 1 | `c12de379c1c3`  |
| 2995   | Layout 1 | `c12de379c1c3`  |
| 2987   | Layout 1 | `c12de379c1c3`  |
| 2978   | Layout 1 | `c12de379c1c3`  |
| 2970   | Layout 1 | `c12de379c1c3`  |
| 2959   | Layout 1 | `c12de379c1c3`  |
| 2951   | Layout 1 | `c12de379c1c3`  |
| 2942   | Layout 1 | `c12de379c1c3`  |
| 2935   | Layout 1 | `c12de379c1c3`  |
| 2932   | Layout 1 | `c12de379c1c3`  |
| 2923   | Layout 1 | `c12de379c1c3`  |
| 2919   | Layout 1 | `c12de379c1c3`  |
| 2907   | Layout 1 | `c12de379c1c3`  |
| 2900   | Layout 1 | `c12de379c1c3`  |
| 2891   | Layout 1 | `c12de379c1c3`  |
| 2882   | Layout 1 | `c12de379c1c3`  |
| 2872   | Layout 1 | `c12de379c1c3`  |
| 2863   | Layout 1 | `c12de379c1c3`  |
| 2855   | Layout 1 | `c12de379c1c3`  |
| 2849   | Layout 1 | `c12de379c1c3`  |
| 2844   | Layout 1 | `c12de379c1c3`  |
| 2834   | Layout 1 | `c12de379c1c3`  |
| 2825   | Layout 1 | `c12de379c1c3`  |
| 2819   | Layout 1 | `c12de379c1c3`  |
| 2811   | Layout 1 | `c12de379c1c3`  |
| 2803   | Layout 1 | `c12de379c1c3`  |
| 2794   | Layout 1 | `c12de379c1c3`  |
| 2783   | Layout 1 | `c12de379c1c3`  |
| 2774   | Layout 1 | `c12de379c1c3`  |
| 2765   | Layout 1 | `c12de379c1c3`  |
| 2756   | Layout 1 | `c12de379c1c3`  |
| 2750   | Layout 1 | `c12de379c1c3`  |
| 2743   | Layout 1 | `c12de379c1c3`  |
| 2736   | Layout 1 | `c12de379c1c3`  |
| 2726   | Layout 1 | `c12de379c1c3`  |
| 2717   | Layout 1 | `c12de379c1c3`  |
| 2709   | Layout 1 | `c12de379c1c3`  |
| 2703   | Layout 1 | `c12de379c1c3`  |
| 2695   | Layout 1 | `c12de379c1c3`  |
| 2684   | Layout 1 | `c12de379c1c3`  |
| 2672   | Layout 1 | `c12de379c1c3`  |
| 2665   | Layout 1 | `c12de379c1c3`  |
| 2657   | Layout 1 | `c12de379c1c3`  |
| 2649   | Layout 1 | `c12de379c1c3`  |
| 2644   | Layout 1 | `c12de379c1c3`  |
| 2637   | Layout 1 | `c12de379c1c3`  |
| 2629   | Layout 1 | `c12de379c1c3`  |
| 2619   | Layout 1 | `c12de379c1c3`  |
| 2612   | Layout 1 | `c12de379c1c3`  |
| 2606   | Layout 1 | `c12de379c1c3`  |
| 2602   | Layout 1 | `c12de379c1c3`  |
| 2601   | Layout 1 | `c12de379c1c3`  |
| 2592   | Layout 1 | `c12de379c1c3`  |
| 2583   | Layout 1 | `c12de379c1c3`  |
| 2575   | Layout 1 | `c12de379c1c3`  |
| 2567   | Layout 1 | `c12de379c1c3`  |
| 2560   | Layout 1 | `c12de379c1c3`  |
| 2553   | Layout 1 | `c12de379c1c3`  |
| 2545   | Layout 1 | `c12de379c1c3`  |
| 2538   | Layout 1 | `c12de379c1c3`  |
| 2529   | Layout 1 | `c12de379c1c3`  |
| 2519   | Layout 1 | `c12de379c1c3`  |
| 2513   | Layout 1 | `c12de379c1c3`  |
| 2510   | Layout 1 | `c12de379c1c3`  |
| 2507   | Layout 1 | `c12de379c1c3`  |
| 2503   | Layout 1 | `c12de379c1c3`  |
| 2498   | Layout 1 | `c12de379c1c3`  |
| 2492   | Layout 1 | `c12de379c1c3`  |
| 2487   | Layout 1 | `c12de379c1c3`  |
| 2480   | Layout 1 | `c12de379c1c3`  |
| 2474   | Layout 1 | `c12de379c1c3`  |
| 2468   | Layout 1 | `c12de379c1c3`  |
| 2460   | Layout 1 | `c12de379c1c3`  |
| 2453   | Layout 1 | `c12de379c1c3`  |
| 2444   | Layout 1 | `c12de379c1c3`  |
| 2438   | Layout 1 | `c12de379c1c3`  |
| 2434   | Layout 1 | `c12de379c1c3`  |
| 2429   | Layout 1 | `c12de379c1c3`  |
| 2421   | Layout 1 | `c12de379c1c3`  |
| 2414   | Layout 1 | `c12de379c1c3`  |
| 2407   | Layout 1 | `c12de379c1c3`  |
| 2401   | Layout 1 | `c12de379c1c3`  |
| 2397   | Layout 1 | `c12de379c1c3`  |
| 2393   | Layout 1 | `c12de379c1c3`  |
| 2384   | Layout 1 | `c12de379c1c3`  |
| 2378   | Layout 1 | `c12de379c1c3`  |
| 2372   | Layout 1 | `c12de379c1c3`  |
| 2358   | Layout 1 | `c12de379c1c3`  |
| 2352   | Layout 1 | `c12de379c1c3`  |
| 2347   | Layout 1 | `c12de379c1c3`  |
| 2343   | Layout 1 | `c12de379c1c3`  |
| 2335   | Layout 1 | `c12de379c1c3`  |
| 2327   | Layout 1 | `c12de379c1c3`  |
| 2324   | Layout 1 | `c12de379c1c3`  |
| 2319   | Layout 1 | `c12de379c1c3`  |
| 2313   | Layout 1 | `c12de379c1c3`  |
| 2308   | Layout 1 | `c12de379c1c3`  |
| 2302   | Layout 1 | `c12de379c1c3`  |
| 2295   | Layout 1 | `c12de379c1c3`  |
| 2290   | Layout 1 | `c12de379c1c3`  |
| 2284   | Layout 1 | `c12de379c1c3`  |
| 2276   | Layout 1 | `c12de379c1c3`  |
| 2269   | Layout 1 | `c12de379c1c3`  |
| 2259   | Layout 1 | `c12de379c1c3`  |
| 2250   | Layout 1 | `c12de379c1c3`  |
| 2243   | Layout 1 | `c12de379c1c3`  |
| 2235   | Layout 1 | `c12de379c1c3`  |
| 2229   | Layout 1 | `c12de379c1c3`  |
| 2224   | Layout 1 | `c12de379c1c3`  |
| 2218   | Layout 1 | `c12de379c1c3`  |
| 2215   | Layout 1 | `c12de379c1c3`  |
| 2207   | Layout 1 | `c12de379c1c3`  |
| 2203   | Layout 1 | `c12de379c1c3`  |
| 2196   | Layout 1 | `c12de379c1c3`  |
| 2192   | Layout 1 | `c12de379c1c3`  |
| 2189   | Layout 1 | `c12de379c1c3`  |
| 2183   | Layout 1 | `c12de379c1c3`  |
| 2179   | Layout 1 | `c12de379c1c3`  |
| 2171   | Layout 1 | `c12de379c1c3`  |
| 2163   | Layout 1 | `c12de379c1c3`  |
| 2156   | Layout 1 | `c12de379c1c3`  |
| 2151   | Layout 1 | `c12de379c1c3`  |
| 2147   | Layout 1 | `c12de379c1c3`  |
| 2142   | Layout 1 | `c12de379c1c3`  |
| 2138   | Layout 1 | `c12de379c1c3`  |
| 2134   | Layout 1 | `c12de379c1c3`  |
| 2130   | Layout 1 | `c12de379c1c3`  |
| 2122   | Layout 1 | `c12de379c1c3`  |
| 2107   | Layout 1 | `c12de379c1c3`  |
| 2098   | Layout 1 | `c12de379c1c3`  |
| 2089   | Layout 1 | `c12de379c1c3`  |
| 2081   | Layout 1 | `c12de379c1c3`  |
| 2073   | Layout 1 | `c12de379c1c3`  |
| 2067   | Layout 1 | `c12de379c1c3`  |
| 2063   | Layout 1 | `c12de379c1c3`  |
| 2059   | Layout 1 | `c12de379c1c3`  |
| 2052   | Layout 1 | `c12de379c1c3`  |
| 2044   | Layout 1 | `c12de379c1c3`  |
| 2039   | Layout 1 | `c12de379c1c3`  |
| 2032   | Layout 1 | `c12de379c1c3`  |
| 2025   | Layout 1 | `c12de379c1c3`  |
| 2011   | Layout 1 | `c12de379c1c3`  |
| 2005   | Layout 1 | `c12de379c1c3`  |
| 2000   | Layout 1 | `c12de379c1c3`  |
| 1996   | Layout 1 | `c12de379c1c3`  |
| 1991   | Layout 1 | `c12de379c1c3`  |
| 1985   | Layout 1 | `c12de379c1c3`  |
| 1980   | Layout 1 | `c12de379c1c3`  |
| 1969   | Layout 1 | `c12de379c1c3`  |
| 1964   | Layout 1 | `c12de379c1c3`  |
| 1958   | Layout 1 | `c12de379c1c3`  |
| 1950   | Layout 1 | `c12de379c1c3`  |
| 1945   | Layout 1 | `c12de379c1c3`  |
| 1937   | Layout 1 | `c12de379c1c3`  |
| 1933   | Layout 1 | `c12de379c1c3`  |
| 1927   | Layout 1 | `c12de379c1c3`  |
| 1921   | Layout 1 | `c12de379c1c3`  |
| 1914   | Layout 1 | `c12de379c1c3`  |
| 1908   | Layout 1 | `c12de379c1c3`  |
| 1897   | Layout 1 | `c12de379c1c3`  |
| 1892   | Layout 1 | `c12de379c1c3`  |
| 1886   | Layout 1 | `c12de379c1c3`  |
| 1881   | Layout 1 | `c12de379c1c3`  |
| 1871   | Layout 1 | `c12de379c1c3`  |
| 1866   | Layout 1 | `c12de379c1c3`  |
| 1862   | Layout 1 | `c12de379c1c3`  |
| 1854   | Layout 1 | `c12de379c1c3`  |
| 1846   | Layout 1 | `c12de379c1c3`  |
| 1838   | Layout 1 | `c12de379c1c3`  |
| 1832   | Layout 1 | `c12de379c1c3`  |
| 1826   | Layout 1 | `c12de379c1c3`  |
| 1822   | Layout 1 | `c12de379c1c3`  |
| 1818   | Layout 1 | `c12de379c1c3`  |
| 1804   | Layout 1 | `c12de379c1c3`  |
| 1794   | Layout 1 | `c12de379c1c3`  |
| 1790   | Layout 1 | `c12de379c1c3`  |
| 1784   | Layout 1 | `c12de379c1c3`  |
| 1774   | Layout 1 | `c12de379c1c3`  |
| 1771   | Layout 1 | `c12de379c1c3`  |
| 1762   | Layout 1 | `c12de379c1c3`  |
| 1759   | Layout 1 | `c12de379c1c3`  |
| 1754   | Layout 1 | `c12de379c1c3`  |
| 1749   | Layout 1 | `c12de379c1c3`  |
| 1743   | Layout 1 | `c12de379c1c3`  |
| 1737   | Layout 1 | `c12de379c1c3`  |
| 1731   | Layout 1 | `c12de379c1c3`  |
| 1725   | Layout 1 | `c12de379c1c3`  |
| 1717   | Layout 1 | `c12de379c1c3`  |
| 1710   | Layout 1 | `c12de379c1c3`  |
| 1704   | Layout 1 | `c12de379c1c3`  |
| 1698   | Layout 1 | `c12de379c1c3`  |
| 1690   | Layout 1 | `c12de379c1c3`  |
| 1685   | Layout 1 | `c12de379c1c3`  |
| 1680   | Layout 1 | `c12de379c1c3`  |
| 1674   | Layout 1 | `c12de379c1c3`  |
| 1668   | Layout 1 | `c12de379c1c3`  |
| 1659   | Layout 1 | `c12de379c1c3`  |
| 1649   | Layout 1 | `c12de379c1c3`  |
| 1642   | Layout 1 | `c12de379c1c3`  |
| 1636   | Layout 1 | `c12de379c1c3`  |
| 1628   | Layout 1 | `c12de379c1c3`  |
| 1622   | Layout 1 | `c12de379c1c3`  |
| 1614   | Layout 1 | `c12de379c1c3`  |
| 1608   | Layout 1 | `c12de379c1c3`  |
| 1602   | Layout 1 | `c12de379c1c3`  |
| 1598   | Layout 1 | `c12de379c1c3`  |
| 1594   | Layout 1 | `c12de379c1c3`  |
| 1590   | Layout 1 | `c12de379c1c3`  |
| 1587   | Layout 1 | `c12de379c1c3`  |
| 1584   | Layout 1 | `c12de379c1c3`  |
| 1579   | Layout 1 | `c12de379c1c3`  |
| 1572   | Layout 1 | `c12de379c1c3`  |
| 1565   | Layout 1 | `c12de379c1c3`  |
| 1559   | Layout 1 | `c12de379c1c3`  |
| 1554   | Layout 1 | `c12de379c1c3`  |
| 1547   | Layout 1 | `c12de379c1c3`  |
| 1537   | Layout 1 | `c12de379c1c3`  |
| 1529   | Layout 1 | `c12de379c1c3`  |
| 1524   | Layout 1 | `c12de379c1c3`  |
| 1519   | Layout 1 | `c12de379c1c3`  |
| 1509   | Layout 1 | `c12de379c1c3`  |
| 1506   | Layout 1 | `c12de379c1c3`  |
| 1504   | No file  | `c12de379c1c3`  |
| 1500   | No file  | `c12de379c1c3`  |
| 1493   | No file  | `c12de379c1c3`  |
| 1489   | No file  | `c12de379c1c3`  |
| 1485   | No file  | `c12de379c1c3`  |
| 1481   | No file  | `c12de379c1c3`  |
| 1474   | No file  | `c12de379c1c3`  |
| 1466   | No file  | `c12de379c1c3`  |
| 1462   | No file  | `c12de379c1c3`  |
| 1459   | No file  | `c12de379c1c3`  |
| 1453   | No file  | `c12de379c1c3`  |
| 1450   | No file  | `c12de379c1c3`  |
| 1445   | No file  | `c12de379c1c3`  |
| 1439   | No file  | `c12de379c1c3`  |
| 1433   | No file  | `c12de379c1c3`  |
| 1430   | No file  | `c12de379c1c3`  |
| 1426   | No file  | `c12de379c1c3`  |
| 1421   | No file  | `c12de379c1c3`  |
| 1417   | No file  | `c12de379c1c3`  |
| 1416   | No file  | `c12de379c1c3`  |
| 1409   | No file  | `c12de379c1c3`  |
| 1405   | No file  | `c12de379c1c3`  |
| 1401   | No file  | `c12de379c1c3`  |
| 1396   | No file  | `c12de379c1c3`  |
| 1391   | No file  | `c12de379c1c3`  |
| 1390   | No file  | `c12de379c1c3`  |
| 1386   | No file  | `c12de379c1c3`  |
| 1381   | No file  | `c12de379c1c3`  |
| 1379   | No file  | `c12de379c1c3`  |
| 1372   | No file  | `c12de379c1c3`  |
| 1366   | No file  | `c12de379c1c3`  |
| 1364   | No file  | `c12de379c1c3`  |
| 1363   | No file  | `c12de379c1c3`  |
| 1360   | No file  | `c12de379c1c3`  |
| 1358   | No file  | `c12de379c1c3`  |
| 1355   | No file  | `c12de379c1c3`  |
| 1351   | No file  | `c12de379c1c3`  |
| 1348   | No file  | `c12de379c1c3`  |
| 1346   | No file  | `c12de379c1c3`  |
| 1341   | No file  | `c12de379c1c3`  |
| 1340   | No file  | `c12de379c1c3`  |
| 1338   | No file  | `c12de379c1c3`  |
| 1335   | No file  | `c12de379c1c3`  |
| 1333   | No file  | `c12de379c1c3`  |
| 1329   | No file  | `c12de379c1c3`  |
| 1327   | No file  | `c12de379c1c3`  |
| 1324   | No file  | `c12de379c1c3`  |
| 1321   | No file  | `c12de379c1c3`  |
| 1319   | No file  | `c12de379c1c3`  |
| 1318   | No file  | `c12de379c1c3`  |
| 1316   | No file  | `c12de379c1c3`  |
| 1313   | No file  | `c12de379c1c3`  |
| 1311   | No file  | `c12de379c1c3`  |
| 1309   | No file  | `c12de379c1c3`  |
| 1304   | No file  | `c12de379c1c3`  |
| 1292   | No file  | `c12de379c1c3`  |
| 1286   | No file  | `c12de379c1c3`  |
| 1280   | No file  | `c12de379c1c3`  |
| 1276   | No file  | `c12de379c1c3`  |
| 1267   | No file  | `c12de379c1c3`  |
| 1261   | No file  | `c12de379c1c3`  |
| 1256   | No file  | `c12de379c1c3`  |
| 1250   | No file  | `c12de379c1c3`  |
| 1246   | No file  | `c12de379c1c3`  |
| 1239   | No file  | `c12de379c1c3`  |
| 1230   | No file  | `c12de379c1c3`  |
| 1226   | No file  | `c12de379c1c3`  |
| 1220   | No file  | `c12de379c1c3`  |
| 1217   | No file  | `c12de379c1c3`  |
| 1211   | No file  | `c12de379c1c3`  |
| 1210   | No file  | `c12de379c1c3`  |
| 1208   | No file  | `c12de379c1c3`  |
| 1203   | No file  | `c12de379c1c3`  |
| 1197   | No file  | `c12de379c1c3`  |
| 1194   | No file  | `c12de379c1c3`  |
| 1192   | No file  | `c12de379c1c3`  |
| 1187   | No file  | `c12de379c1c3`  |
| 1183   | No file  | `c12de379c1c3`  |
| 1177   | No file  | `c12de379c1c3`  |
| 1173   | No file  | `c12de379c1c3`  |
| 1167   | No file  | `c12de379c1c3`  |
| 1164   | No file  | `c12de379c1c3`  |
| 1156   | No file  | `c12de379c1c3`  |
| 1149   | No file  | `c12de379c1c3`  |
| 1144   | No file  | `c12de379c1c3`  |
| 1137   | No file  | `c12de379c1c3`  |
| 1132   | No file  | `c12de379c1c3`  |
| 1127   | No file  | `c12de379c1c3`  |
| 1122   | No file  | `c12de379c1c3`  |
| 1118   | No file  | `c12de379c1c3`  |
| 1114   | No file  | `c12de379c1c3`  |
| 1109   | No file  | `c12de379c1c3`  |
| 1102   | No file  | `c12de379c1c3`  |
| 1096   | No file  | `c12de379c1c3`  |
| 1088   | No file  | `c12de379c1c3`  |
| 1081   | No file  | `c12de379c1c3`  |
| 1076   | No file  | `c12de379c1c3`  |
| 1069   | No file  | `c12de379c1c3`  |
| 1064   | No file  | `c12de379c1c3`  |
| 1058   | No file  | `c12de379c1c3`  |
| 1051   | No file  | `c12de379c1c3`  |
| 1044   | No file  | `c12de379c1c3`  |
| 1036   | No file  | `c12de379c1c3`  |
| 1026   | No file  | `c12de379c1c3`  |
| 1016   | No file  | `c12de379c1c3`  |
| 1009   | No file  | `c12de379c1c3`  |
| 1005   | No file  | `c12de379c1c3`  |
| 1000   | No file  | `c12de379c1c3`  |
| 998    | No file  | `c12de379c1c3`  |
| 990    | No file  | `c12de379c1c3`  |
| 979    | No file  | `c12de379c1c3`  |
| 972    | No file  | `c12de379c1c3`  |
| 963    | No file  | `c12de379c1c3`  |
| 955    | No file  | `c12de379c1c3`  |
| 946    | No file  | `c12de379c1c3`  |
| 938    | No file  | `c12de379c1c3`  |
| 927    | No file  | `c12de379c1c3`  |
| 911    | No file  | `c12de379c1c3`  |
| 904    | No file  | `c12de379c1c3`  |
| 899    | No file  | `c12de379c1c3`  |
| 894    | No file  | `c12de379c1c3`  |
| 885    | No file  | `c12de379c1c3`  |
| 879    | No file  | `c12de379c1c3`  |
| 872    | No file  | `c12de379c1c3`  |
| 864    | No file  | `c12de379c1c3`  |
| 855    | No file  | `c12de379c1c3`  |
| 853    | No file  | `c12de379c1c3`  |
| 845    | No file  | `c12de379c1c3`  |
| 837    | No file  | `c12de379c1c3`  |
| 829    | No file  | `c12de379c1c3`  |
| 822    | No file  | `c12de379c1c3`  |
| 814    | No file  | `c12de379c1c3`  |
| 805    | No file  | `c12de379c1c3`  |
| 794    | No file  | `c12de379c1c3`  |
| 787    | No file  | `c12de379c1c3`  |
| 780    | No file  | `c12de379c1c3`  |
| 771    | No file  | `c12de379c1c3`  |
| 760    | No file  | `c12de379c1c3`  |
| 748    | No file  | `c12de379c1c3`  |
| 741    | No file  | `c12de379c1c3`  |
| 736    | No file  | `c12de379c1c3`  |
| 731    | No file  | `c12de379c1c3`  |
| 723    | No file  | `c12de379c1c3`  |
| 711    | No file  | `c12de379c1c3`  |
| 707    | No file  | `c12de379c1c3`  |
| 697    | No file  | `c12de379c1c3`  |
| 689    | No file  | `c12de379c1c3`  |
| 683    | No file  | `c12de379c1c3`  |
| 678    | No file  | `c12de379c1c3`  |
| 670    | No file  | `c12de379c1c3`  |
| 661    | No file  | `c12de379c1c3`  |
| 656    | No file  | `c12de379c1c3`  |
| 652    | No file  | `c12de379c1c3`  |
| 643    | No file  | `c12de379c1c3`  |
| 637    | No file  | `c12de379c1c3`  |
| 630    | No file  | `c12de379c1c3`  |
| 627    | No file  | `c12de379c1c3`  |
| 621    | No file  | `c12de379c1c3`  |
| 617    | No file  | `c12de379c1c3`  |
| 615    | No file  | `c12de379c1c3`  |
| 606    | No file  | `c12de379c1c3`  |
| 599    | No file  | `c12de379c1c3`  |
| 592    | No file  | `c12de379c1c3`  |
| 586    | No file  | `c12de379c1c3`  |
| 577    | No file  | `c12de379c1c3`  |
| 569    | No file  | `c12de379c1c3`  |
| 561    | No file  | `c12de379c1c3`  |
| 554    | No file  | `c12de379c1c3`  |
| 542    | No file  | `c12de379c1c3`  |
| 532    | No file  | `c12de379c1c3`  |
| 531    | No file  | `c12de379c1c3`  |
| 526    | No file  | `c12de379c1c3`  |
| 521    | No file  | `c12de379c1c3`  |
| 517    | No file  | `c12de379c1c3`  |
| 510    | No file  | `c12de379c1c3`  |
| 508    | No file  | `c12de379c1c3`  |
| 504    | No file  | `c12de379c1c3`  |
| 497    | No file  | `c12de379c1c3`  |
| 491    | No file  | `c12de379c1c3`  |
| 485    | No file  | `c12de379c1c3`  |
| 478    | No file  | `c12de379c1c3`  |
| 472    | No file  | `c12de379c1c3`  |
| 466    | No file  | `c12de379c1c3`  |
| 457    | No file  | `c12de379c1c3`  |
| 452    | No file  | `c12de379c1c3`  |
| 449    | No file  | `c12de379c1c3`  |
| 435    | No file  | `c12de379c1c3`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Class names, LOC type 21        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The shared PABR string table layout of `mansionpartinfo.bss`
(`_common/pabr_strings.py`).

| Offset              | Type                 | Field        | Notes                                          |
| ------------------- | -------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                  | count        | Number of rows; `2` on client 3474             |
| `+0x08`             | User NPC Row[count]  | rows         | See User NPC Row; byte-packed                  |
| `rows+0x00`         | String Table         | string_table | See String Table                               |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                  | zero         | Always `0`                                     |

The file is `8 + 29 x 2 + 25 + 8 = 99` bytes on client 3474. The parser
rejects a file whose rows do not end exactly at `table_start`.

### User NPC Row (29 bytes)

| Offset  | Type | Field               | Notes                                                                 |
| ------- | ---- | ------------------- | --------------------------------------------------------------------- |
| `+0x00` | u64  | player_character_no | Character number of the player whose look the NPC takes               |
| `+0x08` | f32  | pos_x               | World X                                                               |
| `+0x0C` | f32  | pos_y               | World Y (height)                                                      |
| `+0x10` | f32  | pos_z               | World Z                                                               |
| `+0x14` | f32  | direction           | Facing angle in radians                                               |
| `+0x18` | u32  | action_ref          | String table index of the action the NPC plays                        |
| `+0x1C` | u8   | class_type          | Class the NPC is drawn as; LOC type 21 names it                       |

The two rows of client 3474:

| player_character_no | pos_x, pos_y, pos_z          | direction | Action             | class_type    |
| ------------------- | ---------------------------- | --------- | ------------------ | ------------- |
| `1000000000001304`  | 1112.81, -8091.49, 87251.80  | 3.14159   | `FISHING_GOD_WAIT` | 16 Tamer      |
| `643`               | 1191.38, -8106.86, 87098.83  | 4.5       | `FISHING_GOD_WAIT` | 12 Berserker  |

### String Table (variable: 4 bytes + strings)

One string on client 3474, `FISHING_GOD_WAIT`, which both rows point at.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Field Names

The names follow the `FishingGod_NPC` sheet of a private server's
`DataSheets.bexcel` on client 1784 and of the developer workbook
`datasheet_characterdatatable.xlsm`. Its columns are `PA_GAME_SERVICE_TYPE`,
`Player_CharacterNo`, `Position`, `Direction`, `ActionName`, `ItemNo` and
`ClassType`. The row stores five of them in sheet order, `Position` as three
f32 and `ActionName` as a string table index:

| Column               | In the row                                                    |
| -------------------- | ------------------------------------------------------------- |
| PA_GAME_SERVICE_TYPE | Not stored                                                    |
| Player_CharacterNo   | `player_character_no`                                         |
| Position             | `pos_x`, `pos_y`, `pos_z`                                      |
| Direction            | `direction`                                                   |
| ActionName           | `action_ref`                                                  |
| ItemNo               | Not stored                                                    |
| ClassType            | `class_type`                                                  |

The sheet's two rows hold `1112.81,-8091.49,87251.8`, `3.14159` and
`FISHING_GOD_WAIT`, the same position, angle and action as the first row of
client 3474. Their character numbers (`40000000000178712` and
`100000000000020879`) are not in the client file. The sheet's `#설명` note
column reads "3 (한국) - 레인저" and "1 (개발용) - 레인저" (service 3 Korea,
service 1 development, Ranger), and both rows have `ClassType` `4`, the
Ranger class type. Their `ItemNo` `22250,16152` is [Ranger] Da-Dum Da-Dum
Diving Suit and Golden Fishing Rod, the outfit of a Ranger.

The private server's own `usernpc.bss` and the one of client 1784 are 20
bytes with no rows, so no build of the sheet can be compared byte for byte.
The column-to-offset match rests on the values of the first row of client
3474 and on the column order.

Neither the 2016 client with debug symbols nor the tables of a private server on
client 519 have a user NPC type or table.

## Notes

- `PA_GAME_SERVICE_TYPE` is not stored: each sheet row belongs to one
  service, and the file of a client holds a subset of the rows. The sheet's
  character numbers are 4 x 10^16 + 178712 (service 3) and 10^17 + 20879
  (service 1); the first row of client 3474 is 10^15 + 1304.
- The client Lua (3,073 scripts on client 3473) has no `UserNpc` or
  `FISHING_GOD` text, so no UI window reads the table.
- LOC holds one Fishing God line, a dialog line of type 36: "Welcome,
  everyone! As Mena's first Fishing God, I wish you all the best of luck!"
- `ItemNo` (the equipment the NPC wears in the sheet) is not in the client
  file.

## Open Questions

### Who Is Character `643`

The second row of client 3474 has character number `643`, with none of the
per-service prefixes the sheet's numbers carry. The client data does not
show whether it is an older character number or a placeholder.
