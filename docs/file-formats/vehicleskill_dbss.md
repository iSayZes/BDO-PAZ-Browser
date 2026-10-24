# `vehicleskill.dbss` Format

## Purpose

Mount and ship skills: one record per skill with its Korean name, skill EXP
cap, price, icon, key-command and description texts, contents groups,
condition, lock flag, the ship skills' display order and the Training level
that unlocks auto-sprint. On client 3474 the file has 106 records, keys 1 to
106, from Hind Kick (1) and Drift (3) to the ship skills such as
`충각 (항해 초급Lv.1이상)` (Ram, 36).
[servant.bss](servant_bss.md) lists the skills each servant starts with by
these keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records        | Row bytes                    |
| ------ | -------------- | ------- | ------------------------- | ------ | -------------- | ---------------------------- |
| 1      | 1572 and later | 3483    | `vehicleskill.dbss`       | 70,285 | 106 Record     | 268 to 1,646, 663 on average |
| 1      | 1572 and later | 3483    | `vehicleskilloffset.dbss` | 974    | 106 Offset Row | 9                            |

| Layout | File                      | Known            | Unknown        |
| ------ | ------------------------- | ---------------- | -------------- |
| 1      | `vehicleskill.dbss`       | 69,012 B (98.2%) | 1,273 B (1.8%) |
| 1      | `vehicleskilloffset.dbss` | 974 B (100.0%)   | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `475a87269a5c`  |
| 3482   | Layout 1             | `475a87269a5c`  |
| 3474   | Layout 1             | `475a87269a5c`  |
| 3473   | Layout 1             | `475a87269a5c`  |
| 3464   | Layout 1             | `475a87269a5c`  |
| 3458   | Layout 1             | `475a87269a5c`  |
| 3454   | Layout 1             | `475a87269a5c`  |
| 3444   | Layout 1             | `475a87269a5c`  |
| 3435   | Layout 1             | `475a87269a5c`  |
| 3426   | Layout 1             | `475a87269a5c`  |
| 3418   | Layout 1             | `475a87269a5c`  |
| 3412   | Layout 1             | `475a87269a5c`  |
| 3402   | Layout 1             | `475a87269a5c`  |
| 3396   | Layout 1             | `475a87269a5c`  |
| 3387   | Layout 1             | `475a87269a5c`  |
| 3381   | Layout 1             | `475a87269a5c`  |
| 3373   | Layout 1             | `475a87269a5c`  |
| 3364   | Layout 1             | `475a87269a5c`  |
| 3356   | Layout 1             | `475a87269a5c`  |
| 3349   | Layout 1             | `475a87269a5c`  |
| 3342   | Layout 1             | `475a87269a5c`  |
| 3335   | Layout 1             | `475a87269a5c`  |
| 3326   | Layout 1             | `475a87269a5c`  |
| 3321   | Layout 1             | `475a87269a5c`  |
| 3314   | Layout 1             | `475a87269a5c`  |
| 3303   | Layout 1             | `475a87269a5c`  |
| 3302   | Layout 1             | `475a87269a5c`  |
| 3293   | Layout 1             | `475a87269a5c`  |
| 3283   | Layout 1             | `475a87269a5c`  |
| 3275   | Layout 1             | `475a87269a5c`  |
| 3267   | Layout 1             | `475a87269a5c`  |
| 3258   | Layout 1             | `475a87269a5c`  |
| 3251   | Layout 1             | `475a87269a5c`  |
| 3242   | Layout 1             | `475a87269a5c`  |
| 3235   | Layout 1             | `475a87269a5c`  |
| 3229   | Layout 1             | `475a87269a5c`  |
| 3212   | Layout 1             | `475a87269a5c`  |
| 3203   | Layout 1             | `475a87269a5c`  |
| 3193   | Layout 1             | `475a87269a5c`  |
| 3186   | Layout 1             | `475a87269a5c`  |
| 3177   | Layout 1             | `475a87269a5c`  |
| 3169   | Layout 1             | `475a87269a5c`  |
| 3158   | Layout 1             | `475a87269a5c`  |
| 3151   | Layout 1             | `475a87269a5c`  |
| 3144   | Layout 1             | `475a87269a5c`  |
| 3133   | Layout 1             | `475a87269a5c`  |
| 3125   | Layout 1             | `475a87269a5c`  |
| 3118   | Layout 1             | `475a87269a5c`  |
| 3111   | Layout 1             | `475a87269a5c`  |
| 3103   | Layout 1             | `475a87269a5c`  |
| 3095   | Layout 1             | `475a87269a5c`  |
| 3086   | Layout 1             | `475a87269a5c`  |
| 3072   | Layout 1             | `475a87269a5c`  |
| 3062   | Layout 1             | `475a87269a5c`  |
| 3052   | Layout 1             | `475a87269a5c`  |
| 3045   | Layout 1             | `475a87269a5c`  |
| 3037   | Layout 1             | `475a87269a5c`  |
| 3030   | Layout 1             | `475a87269a5c`  |
| 3021   | Layout 1             | `475a87269a5c`  |
| 3012   | Layout 1             | `475a87269a5c`  |
| 3002   | Layout 1             | `475a87269a5c`  |
| 2995   | Layout 1             | `475a87269a5c`  |
| 2987   | Layout 1             | `475a87269a5c`  |
| 2978   | Layout 1             | `475a87269a5c`  |
| 2970   | Layout 1             | `475a87269a5c`  |
| 2959   | Layout 1             | `475a87269a5c`  |
| 2951   | Layout 1             | `475a87269a5c`  |
| 2942   | Layout 1             | `475a87269a5c`  |
| 2935   | Layout 1             | `475a87269a5c`  |
| 2932   | Layout 1             | `475a87269a5c`  |
| 2923   | Layout 1             | `475a87269a5c`  |
| 2919   | Layout 1             | `475a87269a5c`  |
| 2907   | Layout 1             | `475a87269a5c`  |
| 2900   | Layout 1             | `475a87269a5c`  |
| 2891   | Layout 1             | `475a87269a5c`  |
| 2882   | Layout 1             | `475a87269a5c`  |
| 2872   | Layout 1             | `475a87269a5c`  |
| 2863   | Layout 1             | `475a87269a5c`  |
| 2855   | Layout 1             | `475a87269a5c`  |
| 2849   | Layout 1             | `475a87269a5c`  |
| 2844   | Layout 1             | `475a87269a5c`  |
| 2834   | Layout 1             | `475a87269a5c`  |
| 2825   | Layout 1             | `475a87269a5c`  |
| 2819   | Layout 1             | `475a87269a5c`  |
| 2811   | Layout 1             | `475a87269a5c`  |
| 2803   | Layout 1             | `475a87269a5c`  |
| 2794   | Layout 1             | `475a87269a5c`  |
| 2783   | Layout 1             | `475a87269a5c`  |
| 2774   | Layout 1             | `475a87269a5c`  |
| 2765   | Layout 1             | `475a87269a5c`  |
| 2756   | Layout 1             | `475a87269a5c`  |
| 2750   | Layout 1             | `475a87269a5c`  |
| 2743   | Layout 1             | `475a87269a5c`  |
| 2736   | Layout 1             | `475a87269a5c`  |
| 2726   | Layout 1             | `475a87269a5c`  |
| 2717   | Layout 1             | `475a87269a5c`  |
| 2709   | Layout 1             | `475a87269a5c`  |
| 2703   | Layout 1             | `475a87269a5c`  |
| 2695   | Layout 1             | `475a87269a5c`  |
| 2684   | Layout 1             | `475a87269a5c`  |
| 2672   | Layout 1             | `475a87269a5c`  |
| 2665   | Layout 1             | `475a87269a5c`  |
| 2657   | Layout 1             | `475a87269a5c`  |
| 2649   | Layout 1             | `475a87269a5c`  |
| 2644   | Layout 1             | `475a87269a5c`  |
| 2637   | Layout 1             | `475a87269a5c`  |
| 2629   | Layout 1             | `475a87269a5c`  |
| 2619   | Layout 1             | `475a87269a5c`  |
| 2612   | Layout 1             | `475a87269a5c`  |
| 2606   | Layout 1             | `475a87269a5c`  |
| 2602   | Layout 1             | `475a87269a5c`  |
| 2601   | Layout 1             | `475a87269a5c`  |
| 2592   | Layout 1             | `475a87269a5c`  |
| 2583   | Layout 1             | `475a87269a5c`  |
| 2575   | Layout 1             | `475a87269a5c`  |
| 2567   | Layout 1             | `475a87269a5c`  |
| 2560   | Layout 1             | `475a87269a5c`  |
| 2553   | Layout 1             | `475a87269a5c`  |
| 2545   | Layout 1             | `475a87269a5c`  |
| 2538   | Layout 1             | `475a87269a5c`  |
| 2529   | Layout 1             | `475a87269a5c`  |
| 2519   | Layout 1             | `475a87269a5c`  |
| 2513   | Layout 1             | `475a87269a5c`  |
| 2510   | Layout 1             | `475a87269a5c`  |
| 2507   | Layout 1             | `475a87269a5c`  |
| 2503   | Layout 1             | `475a87269a5c`  |
| 2498   | Layout 1             | `475a87269a5c`  |
| 2492   | Layout 1             | `475a87269a5c`  |
| 2487   | Layout 1             | `475a87269a5c`  |
| 2480   | Layout 1             | `475a87269a5c`  |
| 2474   | Layout 1             | `475a87269a5c`  |
| 2468   | Layout 1             | `475a87269a5c`  |
| 2460   | Layout 1             | `475a87269a5c`  |
| 2453   | Layout 1             | `475a87269a5c`  |
| 2444   | Layout 1             | `475a87269a5c`  |
| 2438   | Layout 1             | `475a87269a5c`  |
| 2434   | Layout 1             | `475a87269a5c`  |
| 2429   | Layout 1             | `475a87269a5c`  |
| 2421   | Layout 1             | `475a87269a5c`  |
| 2414   | Layout 1             | `475a87269a5c`  |
| 2407   | Layout 1             | `475a87269a5c`  |
| 2401   | Layout 1             | `475a87269a5c`  |
| 2397   | Layout 1             | `475a87269a5c`  |
| 2393   | Layout 1             | `475a87269a5c`  |
| 2384   | Layout 1             | `475a87269a5c`  |
| 2378   | Layout 1             | `475a87269a5c`  |
| 2372   | Layout 1             | `475a87269a5c`  |
| 2358   | Layout 1             | `475a87269a5c`  |
| 2352   | Layout 1             | `475a87269a5c`  |
| 2347   | Layout 1             | `475a87269a5c`  |
| 2343   | Layout 1             | `475a87269a5c`  |
| 2335   | Layout 1             | `475a87269a5c`  |
| 2327   | Layout 1             | `475a87269a5c`  |
| 2324   | Layout 1             | `475a87269a5c`  |
| 2319   | Layout 1             | `475a87269a5c`  |
| 2313   | Layout 1             | `475a87269a5c`  |
| 2308   | Layout 1             | `475a87269a5c`  |
| 2302   | Layout 1             | `475a87269a5c`  |
| 2295   | Layout 1             | `475a87269a5c`  |
| 2290   | Layout 1             | `475a87269a5c`  |
| 2284   | Layout 1             | `475a87269a5c`  |
| 2276   | Layout 1             | `475a87269a5c`  |
| 2269   | Layout 1             | `475a87269a5c`  |
| 2259   | Layout 1             | `475a87269a5c`  |
| 2250   | Layout 1             | `475a87269a5c`  |
| 2243   | Layout 1             | `475a87269a5c`  |
| 2235   | Layout 1             | `475a87269a5c`  |
| 2229   | Layout 1             | `475a87269a5c`  |
| 2224   | Layout 1             | `475a87269a5c`  |
| 2218   | Layout 1             | `475a87269a5c`  |
| 2215   | Layout 1             | `475a87269a5c`  |
| 2207   | Layout 1             | `475a87269a5c`  |
| 2203   | Layout 1             | `475a87269a5c`  |
| 2196   | Layout 1             | `475a87269a5c`  |
| 2192   | Layout 1             | `475a87269a5c`  |
| 2189   | Layout 1             | `475a87269a5c`  |
| 2183   | Layout 1             | `475a87269a5c`  |
| 2179   | Layout 1             | `475a87269a5c`  |
| 2171   | Layout 1             | `475a87269a5c`  |
| 2163   | Layout 1             | `475a87269a5c`  |
| 2156   | Layout 1             | `475a87269a5c`  |
| 2151   | Layout 1             | `475a87269a5c`  |
| 2147   | Layout 1             | `475a87269a5c`  |
| 2142   | Layout 1             | `475a87269a5c`  |
| 2138   | Layout 1             | `475a87269a5c`  |
| 2134   | Layout 1             | `475a87269a5c`  |
| 2130   | Layout 1             | `475a87269a5c`  |
| 2122   | Layout 1             | `475a87269a5c`  |
| 2107   | Layout 1             | `475a87269a5c`  |
| 2098   | Layout 1             | `475a87269a5c`  |
| 2089   | Layout 1             | `475a87269a5c`  |
| 2081   | Layout 1             | `475a87269a5c`  |
| 2073   | Layout 1             | `475a87269a5c`  |
| 2067   | Layout 1             | `475a87269a5c`  |
| 2063   | Layout 1             | `475a87269a5c`  |
| 2059   | Layout 1             | `475a87269a5c`  |
| 2052   | Layout 1             | `475a87269a5c`  |
| 2044   | Layout 1             | `475a87269a5c`  |
| 2039   | Layout 1             | `475a87269a5c`  |
| 2032   | Layout 1             | `475a87269a5c`  |
| 2025   | Layout 1             | `475a87269a5c`  |
| 2011   | Layout 1             | `475a87269a5c`  |
| 2005   | Layout 1             | `475a87269a5c`  |
| 2000   | Layout 1             | `475a87269a5c`  |
| 1996   | Layout 1             | `475a87269a5c`  |
| 1991   | Layout 1             | `475a87269a5c`  |
| 1985   | Layout 1             | `475a87269a5c`  |
| 1980   | Layout 1             | `475a87269a5c`  |
| 1969   | Layout 1             | `475a87269a5c`  |
| 1964   | Layout 1             | `475a87269a5c`  |
| 1958   | Layout 1             | `475a87269a5c`  |
| 1950   | Layout 1             | `475a87269a5c`  |
| 1945   | Layout 1             | `475a87269a5c`  |
| 1937   | Layout 1             | `475a87269a5c`  |
| 1933   | Layout 1             | `475a87269a5c`  |
| 1927   | Layout 1             | `475a87269a5c`  |
| 1921   | Layout 1             | `475a87269a5c`  |
| 1914   | Layout 1             | `475a87269a5c`  |
| 1908   | Layout 1             | `475a87269a5c`  |
| 1897   | Layout 1             | `475a87269a5c`  |
| 1892   | Layout 1             | `475a87269a5c`  |
| 1886   | Layout 1             | `475a87269a5c`  |
| 1881   | Layout 1             | `475a87269a5c`  |
| 1871   | Layout 1             | `475a87269a5c`  |
| 1866   | Layout 1             | `475a87269a5c`  |
| 1862   | Layout 1             | `475a87269a5c`  |
| 1854   | Layout 1             | `475a87269a5c`  |
| 1846   | Layout 1             | `475a87269a5c`  |
| 1838   | Layout 1             | `475a87269a5c`  |
| 1832   | Layout 1             | `475a87269a5c`  |
| 1826   | Layout 1             | `475a87269a5c`  |
| 1822   | Layout 1             | `475a87269a5c`  |
| 1818   | Layout 1             | `475a87269a5c`  |
| 1804   | Layout 1             | `475a87269a5c`  |
| 1794   | Layout 1             | `475a87269a5c`  |
| 1790   | Layout 1             | `475a87269a5c`  |
| 1784   | Layout 1             | `475a87269a5c`  |
| 1774   | Layout 1             | `475a87269a5c`  |
| 1771   | Layout 1             | `475a87269a5c`  |
| 1762   | Layout 1             | `475a87269a5c`  |
| 1759   | Layout 1             | `475a87269a5c`  |
| 1754   | Layout 1             | `475a87269a5c`  |
| 1749   | Layout 1             | `475a87269a5c`  |
| 1743   | Layout 1             | `475a87269a5c`  |
| 1737   | Layout 1             | `475a87269a5c`  |
| 1731   | Layout 1             | `475a87269a5c`  |
| 1725   | Layout 1             | `475a87269a5c`  |
| 1717   | Layout 1             | `475a87269a5c`  |
| 1710   | Layout 1             | `475a87269a5c`  |
| 1704   | Layout 1             | `475a87269a5c`  |
| 1698   | Layout 1             | `475a87269a5c`  |
| 1690   | Layout 1             | `475a87269a5c`  |
| 1685   | Layout 1             | `475a87269a5c`  |
| 1680   | Layout 1             | `475a87269a5c`  |
| 1674   | Layout 1             | `475a87269a5c`  |
| 1668   | Layout 1             | `475a87269a5c`  |
| 1659   | Layout 1             | `475a87269a5c`  |
| 1649   | Layout 1             | `475a87269a5c`  |
| 1642   | Layout 1             | `475a87269a5c`  |
| 1636   | Layout 1             | `475a87269a5c`  |
| 1628   | Layout 1             | `475a87269a5c`  |
| 1622   | Layout 1             | `475a87269a5c`  |
| 1614   | Layout 1             | `475a87269a5c`  |
| 1608   | Layout 1             | `475a87269a5c`  |
| 1602   | Layout 1             | `475a87269a5c`  |
| 1598   | Layout 1             | `475a87269a5c`  |
| 1594   | Layout 1             | `475a87269a5c`  |
| 1590   | Layout 1             | `475a87269a5c`  |
| 1587   | Layout 1             | `475a87269a5c`  |
| 1584   | Layout 1             | `475a87269a5c`  |
| 1579   | Layout 1             | `475a87269a5c`  |
| 1572   | Layout 1             | `475a87269a5c`  |
| 1565   | No documented layout | `475a87269a5c`  |
| 1559   | No documented layout | `475a87269a5c`  |
| 1554   | No documented layout | `475a87269a5c`  |
| 1547   | No documented layout | `475a87269a5c`  |
| 1537   | No documented layout | `475a87269a5c`  |
| 1529   | No documented layout | `475a87269a5c`  |
| 1524   | No documented layout | `475a87269a5c`  |
| 1519   | No documented layout | `475a87269a5c`  |
| 1509   | No documented layout | `475a87269a5c`  |
| 1506   | No documented layout | `475a87269a5c`  |
| 1504   | No documented layout | `475a87269a5c`  |
| 1500   | No documented layout | `475a87269a5c`  |
| 1493   | No documented layout | `475a87269a5c`  |
| 1489   | No documented layout | `475a87269a5c`  |
| 1485   | No documented layout | `475a87269a5c`  |
| 1481   | No documented layout | `475a87269a5c`  |
| 1474   | No documented layout | `475a87269a5c`  |
| 1466   | No documented layout | `475a87269a5c`  |
| 1462   | No documented layout | `475a87269a5c`  |
| 1459   | No documented layout | `475a87269a5c`  |
| 1453   | No documented layout | `475a87269a5c`  |
| 1450   | No documented layout | `475a87269a5c`  |
| 1445   | No documented layout | `475a87269a5c`  |
| 1439   | No documented layout | `475a87269a5c`  |
| 1433   | No documented layout | `475a87269a5c`  |
| 1430   | No documented layout | `475a87269a5c`  |
| 1426   | No documented layout | `475a87269a5c`  |
| 1421   | No documented layout | `475a87269a5c`  |
| 1417   | No documented layout | `475a87269a5c`  |
| 1416   | No documented layout | `475a87269a5c`  |
| 1409   | No documented layout | `475a87269a5c`  |
| 1405   | No documented layout | `475a87269a5c`  |
| 1401   | No documented layout | `475a87269a5c`  |
| 1396   | No documented layout | `475a87269a5c`  |
| 1391   | No documented layout | `475a87269a5c`  |
| 1390   | No documented layout | `475a87269a5c`  |
| 1386   | No documented layout | `475a87269a5c`  |
| 1381   | No documented layout | `475a87269a5c`  |
| 1379   | No documented layout | `475a87269a5c`  |
| 1372   | No documented layout | `475a87269a5c`  |
| 1366   | No documented layout | `475a87269a5c`  |
| 1364   | No documented layout | `475a87269a5c`  |
| 1363   | No documented layout | `475a87269a5c`  |
| 1360   | No documented layout | `475a87269a5c`  |
| 1358   | No documented layout | `475a87269a5c`  |
| 1355   | No documented layout | `475a87269a5c`  |
| 1351   | No documented layout | `475a87269a5c`  |
| 1348   | No documented layout | `475a87269a5c`  |
| 1346   | No documented layout | `475a87269a5c`  |
| 1341   | No documented layout | `475a87269a5c`  |
| 1340   | No documented layout | `475a87269a5c`  |
| 1338   | No documented layout | `475a87269a5c`  |
| 1335   | No documented layout | `475a87269a5c`  |
| 1333   | No documented layout | `475a87269a5c`  |
| 1329   | No documented layout | `475a87269a5c`  |
| 1327   | No documented layout | `475a87269a5c`  |
| 1324   | No documented layout | `475a87269a5c`  |
| 1321   | No documented layout | `475a87269a5c`  |
| 1319   | No documented layout | `475a87269a5c`  |
| 1318   | No documented layout | `475a87269a5c`  |
| 1316   | No documented layout | `475a87269a5c`  |
| 1313   | No documented layout | `475a87269a5c`  |
| 1311   | No documented layout | `475a87269a5c`  |
| 1309   | No documented layout | `475a87269a5c`  |
| 1304   | No documented layout | `475a87269a5c`  |
| 1292   | No documented layout | `475a87269a5c`  |
| 1286   | No documented layout | `475a87269a5c`  |
| 1280   | No file              | `475a87269a5c`  |
| 1276   | No documented layout | `475a87269a5c`  |
| 1267   | No documented layout | `475a87269a5c`  |
| 1261   | No documented layout | `475a87269a5c`  |
| 1256   | No file              | `475a87269a5c`  |
| 1250   | No file              | `475a87269a5c`  |
| 1246   | No file              | `475a87269a5c`  |
| 1239   | No file              | `475a87269a5c`  |
| 1230   | No file              | `475a87269a5c`  |
| 1226   | No file              | `475a87269a5c`  |
| 1220   | No file              | `475a87269a5c`  |
| 1217   | No file              | `475a87269a5c`  |
| 1211   | No file              | `475a87269a5c`  |
| 1210   | No file              | `475a87269a5c`  |
| 1208   | No file              | `475a87269a5c`  |
| 1203   | No file              | `475a87269a5c`  |
| 1197   | No file              | `475a87269a5c`  |
| 1194   | No file              | `475a87269a5c`  |
| 1192   | No file              | `475a87269a5c`  |
| 1187   | No file              | `475a87269a5c`  |
| 1183   | No file              | `475a87269a5c`  |
| 1177   | No file              | `475a87269a5c`  |
| 1173   | No file              | `475a87269a5c`  |
| 1167   | No file              | `475a87269a5c`  |
| 1164   | No file              | `475a87269a5c`  |
| 1156   | No file              | `475a87269a5c`  |
| 1149   | No file              | `475a87269a5c`  |
| 1144   | No file              | `475a87269a5c`  |
| 1137   | No file              | `475a87269a5c`  |
| 1132   | No file              | `475a87269a5c`  |
| 1127   | No file              | `475a87269a5c`  |
| 1122   | No file              | `475a87269a5c`  |
| 1118   | No file              | `475a87269a5c`  |
| 1114   | No file              | `475a87269a5c`  |
| 1109   | No file              | `475a87269a5c`  |
| 1102   | No file              | `475a87269a5c`  |
| 1096   | No file              | `475a87269a5c`  |
| 1088   | No file              | `475a87269a5c`  |
| 1081   | No file              | `475a87269a5c`  |
| 1076   | No file              | `475a87269a5c`  |
| 1069   | No file              | `475a87269a5c`  |
| 1064   | No file              | `475a87269a5c`  |
| 1058   | No file              | `475a87269a5c`  |
| 1051   | No file              | `475a87269a5c`  |
| 1044   | No file              | `475a87269a5c`  |
| 1036   | No file              | `475a87269a5c`  |
| 1026   | No file              | `475a87269a5c`  |
| 1016   | No file              | `475a87269a5c`  |
| 1009   | No file              | `475a87269a5c`  |
| 1005   | No file              | `475a87269a5c`  |
| 1000   | No file              | `475a87269a5c`  |
| 998    | No file              | `475a87269a5c`  |
| 990    | No file              | `475a87269a5c`  |
| 979    | No file              | `475a87269a5c`  |
| 972    | No file              | `475a87269a5c`  |
| 963    | No file              | `475a87269a5c`  |
| 955    | No file              | `475a87269a5c`  |
| 946    | No file              | `475a87269a5c`  |
| 938    | No file              | `475a87269a5c`  |
| 927    | No file              | `475a87269a5c`  |
| 911    | No file              | `475a87269a5c`  |
| 904    | No file              | `475a87269a5c`  |
| 899    | No file              | `475a87269a5c`  |
| 894    | No file              | `475a87269a5c`  |
| 885    | No file              | `475a87269a5c`  |
| 879    | No file              | `475a87269a5c`  |
| 872    | No file              | `475a87269a5c`  |
| 864    | No file              | `475a87269a5c`  |
| 855    | No file              | `475a87269a5c`  |
| 853    | No file              | `475a87269a5c`  |
| 845    | No file              | `475a87269a5c`  |
| 837    | No file              | `475a87269a5c`  |
| 829    | No file              | `475a87269a5c`  |
| 822    | No file              | `475a87269a5c`  |
| 814    | No file              | `475a87269a5c`  |
| 805    | No file              | `475a87269a5c`  |
| 794    | No file              | `475a87269a5c`  |
| 787    | No file              | `475a87269a5c`  |
| 780    | No file              | `475a87269a5c`  |
| 771    | No file              | `475a87269a5c`  |
| 760    | No file              | `475a87269a5c`  |
| 748    | No file              | `475a87269a5c`  |
| 741    | No file              | `475a87269a5c`  |
| 736    | No file              | `475a87269a5c`  |
| 731    | No file              | `475a87269a5c`  |
| 723    | No file              | `475a87269a5c`  |
| 711    | No file              | `475a87269a5c`  |
| 707    | No file              | `475a87269a5c`  |
| 697    | No file              | `475a87269a5c`  |
| 689    | No file              | `475a87269a5c`  |
| 683    | No file              | `475a87269a5c`  |
| 678    | No file              | `475a87269a5c`  |
| 670    | No file              | `475a87269a5c`  |
| 661    | No file              | `475a87269a5c`  |
| 656    | No file              | `475a87269a5c`  |
| 652    | No file              | `475a87269a5c`  |
| 643    | No file              | `475a87269a5c`  |
| 637    | No file              | `475a87269a5c`  |
| 630    | No file              | `475a87269a5c`  |
| 627    | No file              | `475a87269a5c`  |
| 621    | No file              | `475a87269a5c`  |
| 617    | No file              | `475a87269a5c`  |
| 615    | No file              | `475a87269a5c`  |
| 606    | No file              | `475a87269a5c`  |
| 599    | No file              | `475a87269a5c`  |
| 592    | No file              | `475a87269a5c`  |
| 586    | No file              | `475a87269a5c`  |
| 577    | No file              | `475a87269a5c`  |
| 569    | No file              | `475a87269a5c`  |
| 561    | No file              | `475a87269a5c`  |
| 554    | No file              | `475a87269a5c`  |
| 542    | No file              | `475a87269a5c`  |
| 532    | No file              | `475a87269a5c`  |
| 531    | No file              | `475a87269a5c`  |
| 526    | No file              | `475a87269a5c`  |
| 521    | No file              | `475a87269a5c`  |
| 517    | No file              | `475a87269a5c`  |
| 510    | No file              | `475a87269a5c`  |
| 508    | No file              | `475a87269a5c`  |
| 504    | No file              | `475a87269a5c`  |
| 497    | No file              | `475a87269a5c`  |
| 491    | No file              | `475a87269a5c`  |
| 485    | No file              | `475a87269a5c`  |
| 478    | No file              | `475a87269a5c`  |
| 472    | No file              | `475a87269a5c`  |
| 466    | No file              | `475a87269a5c`  |
| 457    | No file              | `475a87269a5c`  |
| 452    | No file              | `475a87269a5c`  |
| 449    | No file              | `475a87269a5c`  |
| 435    | No file              | `475a87269a5c`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                               |
| ------------------------- | -------- | ------------------------------------------------------------------ |
| `vehicleskilloffset.dbss` | Optional | PABR index: key to the record's offset and size                    |
| `languagedata_en.loc`     | Optional | LOC type 8, `str_id1` = `key`: `str_id4` 0 name, 1 key command, 3 description, 4 console key command |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field      | Notes                                         |
| ------- | ------------- | ---------- | --------------------------------------------- |
| `+0x00` | u8            | unknown_00 | `count` + 1 on clients 1784 (77) and 3474 (107) |
| `+0x01` | u32           | count      | 106 on client 3474                            |
| `+0x05` | Record[count] | records    | Back to back in key order, up to EOF          |

### Record (variable: 104 bytes + texts and contents groups)

| Offset                                | Type                         | Field                                | Notes |
| ------------------------------------- | ---------------------------- | ------------------------------------ | ----- |
| `+0x00`                               | u8                           | key                                  | 1 to 106 on client 3474 |
| `+0x01`                               | str16                        | name_kr                              | `뒷발차기` (Hind Kick) |
| `name_kr+0x00`                        | u32                          | max_exp                              | 30,000 on every record (client 3474) |
| `name_kr+0x04`                        | u32                          | add_exp_for_check                    | |
| `name_kr+0x08`                        | u64                          | base_price                           | |
| `name_kr+0x10`                        | u32                          | add_mating_rate                      | 0, or 20,000 to 40,000 on 5 records (client 3474) |
| `name_kr+0x14`                        | u8                           | is_learn_from_item                   | 1 on 16 records (client 3474) |
| `name_kr+0x15`                        | str16                        | icon_path                            | `New_Icon\04_PC_Skill/06_Riding_Skill/Riding_Skill_0004.dds` |
| `icon_path+0x00`                      | str16                        | desc_kr                              | Key command, `뒷발 공격 ↓+ F`; LOC `str_id4` 1 |
| `desc_kr+0x00`                        | str16                        | desc2_kr                             | Description with `<PAColor>` tags and `\n`; LOC `str_id4` 3 |
| `desc2_kr+0x00`                       | str16                        | console_desc_kr                      | Key command with `{KeyBind:...}`; LOC `str_id4` 4 |
| `console_desc_kr+0x00`                | str16                        | training_skill_characters            | Empty, or servant character IDs as text (`9989, 9889`) on keys 49 to 51 |
| `training_skill_characters+0x00`      | u8                           | is_market_filter                     | |
| `training_skill_characters+0x01`      | u32                          | contents_group_count                 | 1, or 2 on 4 records (client 3474) |
| `training_skill_characters+0x05`      | u32[contents_group_count]    | contents_group_key_hashes            | `key_hash` of each contents group key; `"0"` hashes to `1612107767` |
| `contents_group_key_hashes+0x00`      | bytes[8]                     | unknown_contents_group_key_hashes_00 | `0` on every record (clients 1784 and 3474) |
| `contents_group_key_hashes+0x08`      | str16                        | condition_desc                       | Empty, or a script call such as `VEHICLESKILL_CONDITION_4();` on 19 records (client 3474) |
| `condition_desc+0x00`                 | u8                           | vehicle_skill_lock                   | 0 on 9 records (client 3474) |
| `condition_desc+0x01`                 | u32                          | unknown_condition_desc_01            | `0` on every record (clients 1784 and 3474) |
| `condition_desc+0x05`                 | u32                          | skill_order                          | 0, or 101 to 115 on the 15 ship skills (client 3474) |
| `condition_desc+0x09`                 | u32                          | need_life_level_for_auto_skill       | 0, or 31 on the 5 sprint skills (client 3474) |

### `vehicleskilloffset.dbss`

| Offset              | Type              | Field              | Notes                                        |
| ------------------- | ----------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                                       |
| `+0x04`             | u32               | count              | Equals the main file's `count`               |
| `+0x08`             | Offset Row[count] | entries            | Key order                                    |
| `entries+0x00`      | String Table      | string_table       | Present but empty                            |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`            |
| `string_table+0x04` | u32               | zero               | `0`                                          |

### Offset Row (9 bytes)

| Offset  | Type | Field  | Notes                                         |
| ------- | ---- | ------ | --------------------------------------------- |
| `+0x00` | u8   | key    | The record's `key`                            |
| `+0x01` | u32  | offset | Start of the record; the first is `5`         |
| `+0x05` | u32  | size   | Record size; each record ends where the next starts |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Field Names

The names follow the `VehicleSkill_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched value by value against client
1784 (76 records, every one in the sheet) and the 76 client 3474 records in
the sheet:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `Index`, `Name`, `Icon` | `key`, `name_kr`, `icon_path` | 76 | 76 |
| `MaxExp`, `AddMatingRate`, `IsLearnFromItem` | `max_exp`, `add_mating_rate`, `is_learn_from_item` | 76 | 76 |
| `AddExpForCheck` | `add_exp_for_check` | 76 | 72 |
| `basePrice` | `base_price` | 76 | 12 |
| `Desc`, `Desc2`, `ConsoleDesc` | `desc_kr`, `desc2_kr`, `console_desc_kr` | 76 | 65, 61, 63 |
| `IsTrainingSkill` | `training_skill_characters` | 76 | 76 |
| `isMarketFilter` | `is_market_filter` | 76 | 76 |
| `ContentsGroupKey` (comma list) | `contents_group_key_hashes`, by `key_hash` | 76 | 76 |
| `ConditionDesc`, `VehicleSkillLock` | `condition_desc`, `vehicle_skill_lock` | 76 | 76 |
| `isSkillOrder` | `skill_order` | 76 | 68 |
| `LifeExperienceLevForAutoSkill` | `need_life_level_for_auto_skill` | 71 | 71 |

`key_hash` is the client's contents group key hash
([contentsgroupoptionstaticstatusmanager.bss](contentsgroupoptionstaticstatusmanager_bss.md#key-hash)):
`ContentsGroupKey` `284,80` is stored as the two hashes of `"284"` and
`"80"`, and an empty cell as the hash of `"0"`.

`need_life_level_for_auto_skill` is 41 on client 1784 and 31 on client 3474
for Sprint (4), `빠른발걸음` (22), `빠른 뛰기` (28), `숲의 질주` (55) and
`달려달려` (62); the sheet and the private server's own compiled file hold 0
there. The client Lua confirms the field: the horse stamina widget
(`horsemp`, `panel_widget_horsemp_renew`) blocks auto-sprint while the
player's life level is below `vehicleProxy:getNeedLifeLevelForAutoSkill(skillKey)`
(`LUA_AUTOSPRINT_CANNOTUSE`).

`skill_order` holds the column `isSkillOrder`, which is a number, not a flag:
the 15 ship skills on client 3474 run 101 to 115, the 10 on client 1784
101 to 110, and the new skills moved the old ones (Ram 101 on both,
`급발진` 105 on client 1784 and 108 on client 3474). `training_skill_characters` holds the column
`IsTrainingSkill`, a text list of servant character IDs (9989 and 9889 are
the male and female Arduanatt); the servant windows hide skills whose
wrapper says `isTrainingSkill()`. The client 3474 text misses are rewrites
of the descriptions and key hints; the price and EXP misses are rebalances.

The sheet's `PriceRate_0` to `PriceRate_2` (1,000,000 on every row) have no
field.

## Notes

- Client 1784 has the same layout with 76 records; 30 skills were added by
  client 3474.
- The highest key plus one is in its own one-byte file,
  [vehicleskillcount.dbss](vehicleskillcount_dbss.md). The skills each
  servant can learn are in
  [vehicleskillowner.dbss](vehicleskillowner_dbss.md).

## Open Questions

### The Header Byte and Zero Fields

`unknown_00` holds the same value as
[vehicleskillcount.dbss](vehicleskillcount_dbss.md) on clients 1485 to
3474: the highest key plus one, the 2016
`gc::VehicleSkillStaticStatusManager::_count`. The keys have no gap on any
of these clients, so the byte cannot be told apart from the record count
plus one, and nothing shows which of the two files the client takes
`_count` from. `unknown_contents_group_key_hashes_00`
(8 bytes) and `unknown_condition_desc_01` (u32) are `0` on every record of
both clients and match no sheet column.
