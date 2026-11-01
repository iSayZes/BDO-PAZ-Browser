# `duelcharacter.bss` Format

## Purpose

The options of Tag Characters (duel characters in the client code), one
58-byte record with no header: the quest that opens the item copy of
Marni's Suspicious Device, the fuel item the copy uses and the fuel item
the single copy uses, then eleven values not tied to a meaning yet. On
client 3482 the quest is Black Spirit's Gift (Marni's Suspicious Device)
(chain `21418`, quest `5`), the items Marni's Unstable Fuel (`45026`) and
Marni's Processed Fuel (`320157`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------- | ----- | ------- | --------- |
| 1      | 3258 and later | `duelcharacter.bss` | 58    | -       | -         |

| Layout | File                | Known        | Unknown      |
| ------ | ------------------- | ------------ | ------------ |
| 1      | `duelcharacter.bss` | 12 B (20.7%) | 46 B (79.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6fae1fcc85df`  |
| 3482   | Layout 1 | `6fae1fcc85df`  |
| 3474   | Layout 1 | `6fae1fcc85df`  |
| 3473   | Layout 1 | `6fae1fcc85df`  |
| 3464   | Layout 1 | `6fae1fcc85df`  |
| 3458   | Layout 1 | `6fae1fcc85df`  |
| 3454   | Layout 1 | `6fae1fcc85df`  |
| 3444   | Layout 1 | `6fae1fcc85df`  |
| 3435   | Layout 1 | `6fae1fcc85df`  |
| 3426   | Layout 1 | `6fae1fcc85df`  |
| 3418   | Layout 1 | `6fae1fcc85df`  |
| 3412   | Layout 1 | `6fae1fcc85df`  |
| 3402   | Layout 1 | `6fae1fcc85df`  |
| 3396   | Layout 1 | `6fae1fcc85df`  |
| 3387   | Layout 1 | `6fae1fcc85df`  |
| 3381   | Layout 1 | `6fae1fcc85df`  |
| 3373   | Layout 1 | `6fae1fcc85df`  |
| 3364   | Layout 1 | `6fae1fcc85df`  |
| 3356   | Layout 1 | `6fae1fcc85df`  |
| 3349   | Layout 1 | `6fae1fcc85df`  |
| 3342   | Layout 1 | `6fae1fcc85df`  |
| 3335   | Layout 1 | `6fae1fcc85df`  |
| 3326   | Layout 1 | `6fae1fcc85df`  |
| 3321   | Layout 1 | `6fae1fcc85df`  |
| 3314   | Layout 1 | `6fae1fcc85df`  |
| 3303   | Layout 1 | `6fae1fcc85df`  |
| 3302   | Layout 1 | `6fae1fcc85df`  |
| 3293   | Layout 1 | `6fae1fcc85df`  |
| 3283   | Layout 1 | `6fae1fcc85df`  |
| 3275   | Layout 1 | `6fae1fcc85df`  |
| 3267   | Layout 1 | `6fae1fcc85df`  |
| 3258   | Layout 1 | `6fae1fcc85df`  |
| 3251   | No file  | `6fae1fcc85df`  |
| 3242   | No file  | `6fae1fcc85df`  |
| 3235   | No file  | `6fae1fcc85df`  |
| 3229   | No file  | `6fae1fcc85df`  |
| 3212   | No file  | `6fae1fcc85df`  |
| 3203   | No file  | `6fae1fcc85df`  |
| 3193   | No file  | `6fae1fcc85df`  |
| 3186   | No file  | `6fae1fcc85df`  |
| 3177   | No file  | `6fae1fcc85df`  |
| 3169   | No file  | `6fae1fcc85df`  |
| 3158   | No file  | `6fae1fcc85df`  |
| 3151   | No file  | `6fae1fcc85df`  |
| 3144   | No file  | `6fae1fcc85df`  |
| 3133   | No file  | `6fae1fcc85df`  |
| 3125   | No file  | `6fae1fcc85df`  |
| 3118   | No file  | `6fae1fcc85df`  |
| 3111   | No file  | `6fae1fcc85df`  |
| 3103   | No file  | `6fae1fcc85df`  |
| 3095   | No file  | `6fae1fcc85df`  |
| 3086   | No file  | `6fae1fcc85df`  |
| 3072   | No file  | `6fae1fcc85df`  |
| 3062   | No file  | `6fae1fcc85df`  |
| 3052   | No file  | `6fae1fcc85df`  |
| 3045   | No file  | `6fae1fcc85df`  |
| 3037   | No file  | `6fae1fcc85df`  |
| 3030   | No file  | `6fae1fcc85df`  |
| 3021   | No file  | `6fae1fcc85df`  |
| 3012   | No file  | `6fae1fcc85df`  |
| 3002   | No file  | `6fae1fcc85df`  |
| 2995   | No file  | `6fae1fcc85df`  |
| 2987   | No file  | `6fae1fcc85df`  |
| 2978   | No file  | `6fae1fcc85df`  |
| 2970   | No file  | `6fae1fcc85df`  |
| 2959   | No file  | `6fae1fcc85df`  |
| 2951   | No file  | `6fae1fcc85df`  |
| 2942   | No file  | `6fae1fcc85df`  |
| 2935   | No file  | `6fae1fcc85df`  |
| 2932   | No file  | `6fae1fcc85df`  |
| 2923   | No file  | `6fae1fcc85df`  |
| 2919   | No file  | `6fae1fcc85df`  |
| 2907   | No file  | `6fae1fcc85df`  |
| 2900   | No file  | `6fae1fcc85df`  |
| 2891   | No file  | `6fae1fcc85df`  |
| 2882   | No file  | `6fae1fcc85df`  |
| 2872   | No file  | `6fae1fcc85df`  |
| 2863   | No file  | `6fae1fcc85df`  |
| 2855   | No file  | `6fae1fcc85df`  |
| 2849   | No file  | `6fae1fcc85df`  |
| 2844   | No file  | `6fae1fcc85df`  |
| 2834   | No file  | `6fae1fcc85df`  |
| 2825   | No file  | `6fae1fcc85df`  |
| 2819   | No file  | `6fae1fcc85df`  |
| 2811   | No file  | `6fae1fcc85df`  |
| 2803   | No file  | `6fae1fcc85df`  |
| 2794   | No file  | `6fae1fcc85df`  |
| 2783   | No file  | `6fae1fcc85df`  |
| 2774   | No file  | `6fae1fcc85df`  |
| 2765   | No file  | `6fae1fcc85df`  |
| 2756   | No file  | `6fae1fcc85df`  |
| 2750   | No file  | `6fae1fcc85df`  |
| 2743   | No file  | `6fae1fcc85df`  |
| 2736   | No file  | `6fae1fcc85df`  |
| 2726   | No file  | `6fae1fcc85df`  |
| 2717   | No file  | `6fae1fcc85df`  |
| 2709   | No file  | `6fae1fcc85df`  |
| 2703   | No file  | `6fae1fcc85df`  |
| 2695   | No file  | `6fae1fcc85df`  |
| 2684   | No file  | `6fae1fcc85df`  |
| 2672   | No file  | `6fae1fcc85df`  |
| 2665   | No file  | `6fae1fcc85df`  |
| 2657   | No file  | `6fae1fcc85df`  |
| 2649   | No file  | `6fae1fcc85df`  |
| 2644   | No file  | `6fae1fcc85df`  |
| 2637   | No file  | `6fae1fcc85df`  |
| 2629   | No file  | `6fae1fcc85df`  |
| 2619   | No file  | `6fae1fcc85df`  |
| 2612   | No file  | `6fae1fcc85df`  |
| 2606   | No file  | `6fae1fcc85df`  |
| 2602   | No file  | `6fae1fcc85df`  |
| 2601   | No file  | `6fae1fcc85df`  |
| 2592   | No file  | `6fae1fcc85df`  |
| 2583   | No file  | `6fae1fcc85df`  |
| 2575   | No file  | `6fae1fcc85df`  |
| 2567   | No file  | `6fae1fcc85df`  |
| 2560   | No file  | `6fae1fcc85df`  |
| 2553   | No file  | `6fae1fcc85df`  |
| 2545   | No file  | `6fae1fcc85df`  |
| 2538   | No file  | `6fae1fcc85df`  |
| 2529   | No file  | `6fae1fcc85df`  |
| 2519   | No file  | `6fae1fcc85df`  |
| 2513   | No file  | `6fae1fcc85df`  |
| 2510   | No file  | `6fae1fcc85df`  |
| 2507   | No file  | `6fae1fcc85df`  |
| 2503   | No file  | `6fae1fcc85df`  |
| 2498   | No file  | `6fae1fcc85df`  |
| 2492   | No file  | `6fae1fcc85df`  |
| 2487   | No file  | `6fae1fcc85df`  |
| 2480   | No file  | `6fae1fcc85df`  |
| 2474   | No file  | `6fae1fcc85df`  |
| 2468   | No file  | `6fae1fcc85df`  |
| 2460   | No file  | `6fae1fcc85df`  |
| 2453   | No file  | `6fae1fcc85df`  |
| 2444   | No file  | `6fae1fcc85df`  |
| 2438   | No file  | `6fae1fcc85df`  |
| 2434   | No file  | `6fae1fcc85df`  |
| 2429   | No file  | `6fae1fcc85df`  |
| 2421   | No file  | `6fae1fcc85df`  |
| 2414   | No file  | `6fae1fcc85df`  |
| 2407   | No file  | `6fae1fcc85df`  |
| 2401   | No file  | `6fae1fcc85df`  |
| 2397   | No file  | `6fae1fcc85df`  |
| 2393   | No file  | `6fae1fcc85df`  |
| 2384   | No file  | `6fae1fcc85df`  |
| 2378   | No file  | `6fae1fcc85df`  |
| 2372   | No file  | `6fae1fcc85df`  |
| 2358   | No file  | `6fae1fcc85df`  |
| 2352   | No file  | `6fae1fcc85df`  |
| 2347   | No file  | `6fae1fcc85df`  |
| 2343   | No file  | `6fae1fcc85df`  |
| 2335   | No file  | `6fae1fcc85df`  |
| 2327   | No file  | `6fae1fcc85df`  |
| 2324   | No file  | `6fae1fcc85df`  |
| 2319   | No file  | `6fae1fcc85df`  |
| 2313   | No file  | `6fae1fcc85df`  |
| 2308   | No file  | `6fae1fcc85df`  |
| 2302   | No file  | `6fae1fcc85df`  |
| 2295   | No file  | `6fae1fcc85df`  |
| 2290   | No file  | `6fae1fcc85df`  |
| 2284   | No file  | `6fae1fcc85df`  |
| 2276   | No file  | `6fae1fcc85df`  |
| 2269   | No file  | `6fae1fcc85df`  |
| 2259   | No file  | `6fae1fcc85df`  |
| 2250   | No file  | `6fae1fcc85df`  |
| 2243   | No file  | `6fae1fcc85df`  |
| 2235   | No file  | `6fae1fcc85df`  |
| 2229   | No file  | `6fae1fcc85df`  |
| 2224   | No file  | `6fae1fcc85df`  |
| 2218   | No file  | `6fae1fcc85df`  |
| 2215   | No file  | `6fae1fcc85df`  |
| 2207   | No file  | `6fae1fcc85df`  |
| 2203   | No file  | `6fae1fcc85df`  |
| 2196   | No file  | `6fae1fcc85df`  |
| 2192   | No file  | `6fae1fcc85df`  |
| 2189   | No file  | `6fae1fcc85df`  |
| 2183   | No file  | `6fae1fcc85df`  |
| 2179   | No file  | `6fae1fcc85df`  |
| 2171   | No file  | `6fae1fcc85df`  |
| 2163   | No file  | `6fae1fcc85df`  |
| 2156   | No file  | `6fae1fcc85df`  |
| 2151   | No file  | `6fae1fcc85df`  |
| 2147   | No file  | `6fae1fcc85df`  |
| 2142   | No file  | `6fae1fcc85df`  |
| 2138   | No file  | `6fae1fcc85df`  |
| 2134   | No file  | `6fae1fcc85df`  |
| 2130   | No file  | `6fae1fcc85df`  |
| 2122   | No file  | `6fae1fcc85df`  |
| 2107   | No file  | `6fae1fcc85df`  |
| 2098   | No file  | `6fae1fcc85df`  |
| 2089   | No file  | `6fae1fcc85df`  |
| 2081   | No file  | `6fae1fcc85df`  |
| 2073   | No file  | `6fae1fcc85df`  |
| 2067   | No file  | `6fae1fcc85df`  |
| 2063   | No file  | `6fae1fcc85df`  |
| 2059   | No file  | `6fae1fcc85df`  |
| 2052   | No file  | `6fae1fcc85df`  |
| 2044   | No file  | `6fae1fcc85df`  |
| 2039   | No file  | `6fae1fcc85df`  |
| 2032   | No file  | `6fae1fcc85df`  |
| 2025   | No file  | `6fae1fcc85df`  |
| 2011   | No file  | `6fae1fcc85df`  |
| 2005   | No file  | `6fae1fcc85df`  |
| 2000   | No file  | `6fae1fcc85df`  |
| 1996   | No file  | `6fae1fcc85df`  |
| 1991   | No file  | `6fae1fcc85df`  |
| 1985   | No file  | `6fae1fcc85df`  |
| 1980   | No file  | `6fae1fcc85df`  |
| 1969   | No file  | `6fae1fcc85df`  |
| 1964   | No file  | `6fae1fcc85df`  |
| 1958   | No file  | `6fae1fcc85df`  |
| 1950   | No file  | `6fae1fcc85df`  |
| 1945   | No file  | `6fae1fcc85df`  |
| 1937   | No file  | `6fae1fcc85df`  |
| 1933   | No file  | `6fae1fcc85df`  |
| 1927   | No file  | `6fae1fcc85df`  |
| 1921   | No file  | `6fae1fcc85df`  |
| 1914   | No file  | `6fae1fcc85df`  |
| 1908   | No file  | `6fae1fcc85df`  |
| 1897   | No file  | `6fae1fcc85df`  |
| 1892   | No file  | `6fae1fcc85df`  |
| 1886   | No file  | `6fae1fcc85df`  |
| 1881   | No file  | `6fae1fcc85df`  |
| 1871   | No file  | `6fae1fcc85df`  |
| 1866   | No file  | `6fae1fcc85df`  |
| 1862   | No file  | `6fae1fcc85df`  |
| 1854   | No file  | `6fae1fcc85df`  |
| 1846   | No file  | `6fae1fcc85df`  |
| 1838   | No file  | `6fae1fcc85df`  |
| 1832   | No file  | `6fae1fcc85df`  |
| 1826   | No file  | `6fae1fcc85df`  |
| 1822   | No file  | `6fae1fcc85df`  |
| 1818   | No file  | `6fae1fcc85df`  |
| 1804   | No file  | `6fae1fcc85df`  |
| 1794   | No file  | `6fae1fcc85df`  |
| 1790   | No file  | `6fae1fcc85df`  |
| 1784   | No file  | `6fae1fcc85df`  |
| 1774   | No file  | `6fae1fcc85df`  |
| 1771   | No file  | `6fae1fcc85df`  |
| 1762   | No file  | `6fae1fcc85df`  |
| 1759   | No file  | `6fae1fcc85df`  |
| 1754   | No file  | `6fae1fcc85df`  |
| 1749   | No file  | `6fae1fcc85df`  |
| 1743   | No file  | `6fae1fcc85df`  |
| 1737   | No file  | `6fae1fcc85df`  |
| 1731   | No file  | `6fae1fcc85df`  |
| 1725   | No file  | `6fae1fcc85df`  |
| 1717   | No file  | `6fae1fcc85df`  |
| 1710   | No file  | `6fae1fcc85df`  |
| 1704   | No file  | `6fae1fcc85df`  |
| 1698   | No file  | `6fae1fcc85df`  |
| 1690   | No file  | `6fae1fcc85df`  |
| 1685   | No file  | `6fae1fcc85df`  |
| 1680   | No file  | `6fae1fcc85df`  |
| 1674   | No file  | `6fae1fcc85df`  |
| 1668   | No file  | `6fae1fcc85df`  |
| 1659   | No file  | `6fae1fcc85df`  |
| 1649   | No file  | `6fae1fcc85df`  |
| 1642   | No file  | `6fae1fcc85df`  |
| 1636   | No file  | `6fae1fcc85df`  |
| 1628   | No file  | `6fae1fcc85df`  |
| 1622   | No file  | `6fae1fcc85df`  |
| 1614   | No file  | `6fae1fcc85df`  |
| 1608   | No file  | `6fae1fcc85df`  |
| 1602   | No file  | `6fae1fcc85df`  |
| 1598   | No file  | `6fae1fcc85df`  |
| 1594   | No file  | `6fae1fcc85df`  |
| 1590   | No file  | `6fae1fcc85df`  |
| 1587   | No file  | `6fae1fcc85df`  |
| 1584   | No file  | `6fae1fcc85df`  |
| 1579   | No file  | `6fae1fcc85df`  |
| 1572   | No file  | `6fae1fcc85df`  |
| 1565   | No file  | `6fae1fcc85df`  |
| 1559   | No file  | `6fae1fcc85df`  |
| 1554   | No file  | `6fae1fcc85df`  |
| 1547   | No file  | `6fae1fcc85df`  |
| 1537   | No file  | `6fae1fcc85df`  |
| 1529   | No file  | `6fae1fcc85df`  |
| 1524   | No file  | `6fae1fcc85df`  |
| 1519   | No file  | `6fae1fcc85df`  |
| 1509   | No file  | `6fae1fcc85df`  |
| 1506   | No file  | `6fae1fcc85df`  |
| 1504   | No file  | `6fae1fcc85df`  |
| 1500   | No file  | `6fae1fcc85df`  |
| 1493   | No file  | `6fae1fcc85df`  |
| 1489   | No file  | `6fae1fcc85df`  |
| 1485   | No file  | `6fae1fcc85df`  |
| 1481   | No file  | `6fae1fcc85df`  |
| 1474   | No file  | `6fae1fcc85df`  |
| 1466   | No file  | `6fae1fcc85df`  |
| 1462   | No file  | `6fae1fcc85df`  |
| 1459   | No file  | `6fae1fcc85df`  |
| 1453   | No file  | `6fae1fcc85df`  |
| 1450   | No file  | `6fae1fcc85df`  |
| 1445   | No file  | `6fae1fcc85df`  |
| 1439   | No file  | `6fae1fcc85df`  |
| 1433   | No file  | `6fae1fcc85df`  |
| 1430   | No file  | `6fae1fcc85df`  |
| 1426   | No file  | `6fae1fcc85df`  |
| 1421   | No file  | `6fae1fcc85df`  |
| 1417   | No file  | `6fae1fcc85df`  |
| 1416   | No file  | `6fae1fcc85df`  |
| 1409   | No file  | `6fae1fcc85df`  |
| 1405   | No file  | `6fae1fcc85df`  |
| 1401   | No file  | `6fae1fcc85df`  |
| 1396   | No file  | `6fae1fcc85df`  |
| 1391   | No file  | `6fae1fcc85df`  |
| 1390   | No file  | `6fae1fcc85df`  |
| 1386   | No file  | `6fae1fcc85df`  |
| 1381   | No file  | `6fae1fcc85df`  |
| 1379   | No file  | `6fae1fcc85df`  |
| 1372   | No file  | `6fae1fcc85df`  |
| 1366   | No file  | `6fae1fcc85df`  |
| 1364   | No file  | `6fae1fcc85df`  |
| 1363   | No file  | `6fae1fcc85df`  |
| 1360   | No file  | `6fae1fcc85df`  |
| 1358   | No file  | `6fae1fcc85df`  |
| 1355   | No file  | `6fae1fcc85df`  |
| 1351   | No file  | `6fae1fcc85df`  |
| 1348   | No file  | `6fae1fcc85df`  |
| 1346   | No file  | `6fae1fcc85df`  |
| 1341   | No file  | `6fae1fcc85df`  |
| 1340   | No file  | `6fae1fcc85df`  |
| 1338   | No file  | `6fae1fcc85df`  |
| 1335   | No file  | `6fae1fcc85df`  |
| 1333   | No file  | `6fae1fcc85df`  |
| 1329   | No file  | `6fae1fcc85df`  |
| 1327   | No file  | `6fae1fcc85df`  |
| 1324   | No file  | `6fae1fcc85df`  |
| 1321   | No file  | `6fae1fcc85df`  |
| 1319   | No file  | `6fae1fcc85df`  |
| 1318   | No file  | `6fae1fcc85df`  |
| 1316   | No file  | `6fae1fcc85df`  |
| 1313   | No file  | `6fae1fcc85df`  |
| 1311   | No file  | `6fae1fcc85df`  |
| 1309   | No file  | `6fae1fcc85df`  |
| 1304   | No file  | `6fae1fcc85df`  |
| 1292   | No file  | `6fae1fcc85df`  |
| 1286   | No file  | `6fae1fcc85df`  |
| 1280   | No file  | `6fae1fcc85df`  |
| 1276   | No file  | `6fae1fcc85df`  |
| 1267   | No file  | `6fae1fcc85df`  |
| 1261   | No file  | `6fae1fcc85df`  |
| 1256   | No file  | `6fae1fcc85df`  |
| 1250   | No file  | `6fae1fcc85df`  |
| 1246   | No file  | `6fae1fcc85df`  |
| 1239   | No file  | `6fae1fcc85df`  |
| 1230   | No file  | `6fae1fcc85df`  |
| 1226   | No file  | `6fae1fcc85df`  |
| 1220   | No file  | `6fae1fcc85df`  |
| 1217   | No file  | `6fae1fcc85df`  |
| 1211   | No file  | `6fae1fcc85df`  |
| 1210   | No file  | `6fae1fcc85df`  |
| 1208   | No file  | `6fae1fcc85df`  |
| 1203   | No file  | `6fae1fcc85df`  |
| 1197   | No file  | `6fae1fcc85df`  |
| 1194   | No file  | `6fae1fcc85df`  |
| 1192   | No file  | `6fae1fcc85df`  |
| 1187   | No file  | `6fae1fcc85df`  |
| 1183   | No file  | `6fae1fcc85df`  |
| 1177   | No file  | `6fae1fcc85df`  |
| 1173   | No file  | `6fae1fcc85df`  |
| 1167   | No file  | `6fae1fcc85df`  |
| 1164   | No file  | `6fae1fcc85df`  |
| 1156   | No file  | `6fae1fcc85df`  |
| 1149   | No file  | `6fae1fcc85df`  |
| 1144   | No file  | `6fae1fcc85df`  |
| 1137   | No file  | `6fae1fcc85df`  |
| 1132   | No file  | `6fae1fcc85df`  |
| 1127   | No file  | `6fae1fcc85df`  |
| 1122   | No file  | `6fae1fcc85df`  |
| 1118   | No file  | `6fae1fcc85df`  |
| 1114   | No file  | `6fae1fcc85df`  |
| 1109   | No file  | `6fae1fcc85df`  |
| 1102   | No file  | `6fae1fcc85df`  |
| 1096   | No file  | `6fae1fcc85df`  |
| 1088   | No file  | `6fae1fcc85df`  |
| 1081   | No file  | `6fae1fcc85df`  |
| 1076   | No file  | `6fae1fcc85df`  |
| 1069   | No file  | `6fae1fcc85df`  |
| 1064   | No file  | `6fae1fcc85df`  |
| 1058   | No file  | `6fae1fcc85df`  |
| 1051   | No file  | `6fae1fcc85df`  |
| 1044   | No file  | `6fae1fcc85df`  |
| 1036   | No file  | `6fae1fcc85df`  |
| 1026   | No file  | `6fae1fcc85df`  |
| 1016   | No file  | `6fae1fcc85df`  |
| 1009   | No file  | `6fae1fcc85df`  |
| 1005   | No file  | `6fae1fcc85df`  |
| 1000   | No file  | `6fae1fcc85df`  |
| 998    | No file  | `6fae1fcc85df`  |
| 990    | No file  | `6fae1fcc85df`  |
| 979    | No file  | `6fae1fcc85df`  |
| 972    | No file  | `6fae1fcc85df`  |
| 963    | No file  | `6fae1fcc85df`  |
| 955    | No file  | `6fae1fcc85df`  |
| 946    | No file  | `6fae1fcc85df`  |
| 938    | No file  | `6fae1fcc85df`  |
| 927    | No file  | `6fae1fcc85df`  |
| 911    | No file  | `6fae1fcc85df`  |
| 904    | No file  | `6fae1fcc85df`  |
| 899    | No file  | `6fae1fcc85df`  |
| 894    | No file  | `6fae1fcc85df`  |
| 885    | No file  | `6fae1fcc85df`  |
| 879    | No file  | `6fae1fcc85df`  |
| 872    | No file  | `6fae1fcc85df`  |
| 864    | No file  | `6fae1fcc85df`  |
| 855    | No file  | `6fae1fcc85df`  |
| 853    | No file  | `6fae1fcc85df`  |
| 845    | No file  | `6fae1fcc85df`  |
| 837    | No file  | `6fae1fcc85df`  |
| 829    | No file  | `6fae1fcc85df`  |
| 822    | No file  | `6fae1fcc85df`  |
| 814    | No file  | `6fae1fcc85df`  |
| 805    | No file  | `6fae1fcc85df`  |
| 794    | No file  | `6fae1fcc85df`  |
| 787    | No file  | `6fae1fcc85df`  |
| 780    | No file  | `6fae1fcc85df`  |
| 771    | No file  | `6fae1fcc85df`  |
| 760    | No file  | `6fae1fcc85df`  |
| 748    | No file  | `6fae1fcc85df`  |
| 741    | No file  | `6fae1fcc85df`  |
| 736    | No file  | `6fae1fcc85df`  |
| 731    | No file  | `6fae1fcc85df`  |
| 723    | No file  | `6fae1fcc85df`  |
| 711    | No file  | `6fae1fcc85df`  |
| 707    | No file  | `6fae1fcc85df`  |
| 697    | No file  | `6fae1fcc85df`  |
| 689    | No file  | `6fae1fcc85df`  |
| 683    | No file  | `6fae1fcc85df`  |
| 678    | No file  | `6fae1fcc85df`  |
| 670    | No file  | `6fae1fcc85df`  |
| 661    | No file  | `6fae1fcc85df`  |
| 656    | No file  | `6fae1fcc85df`  |
| 652    | No file  | `6fae1fcc85df`  |
| 643    | No file  | `6fae1fcc85df`  |
| 637    | No file  | `6fae1fcc85df`  |
| 630    | No file  | `6fae1fcc85df`  |
| 627    | No file  | `6fae1fcc85df`  |
| 621    | No file  | `6fae1fcc85df`  |
| 617    | No file  | `6fae1fcc85df`  |
| 615    | No file  | `6fae1fcc85df`  |
| 606    | No file  | `6fae1fcc85df`  |
| 599    | No file  | `6fae1fcc85df`  |
| 592    | No file  | `6fae1fcc85df`  |
| 586    | No file  | `6fae1fcc85df`  |
| 577    | No file  | `6fae1fcc85df`  |
| 569    | No file  | `6fae1fcc85df`  |
| 561    | No file  | `6fae1fcc85df`  |
| 554    | No file  | `6fae1fcc85df`  |
| 542    | No file  | `6fae1fcc85df`  |
| 532    | No file  | `6fae1fcc85df`  |
| 531    | No file  | `6fae1fcc85df`  |
| 526    | No file  | `6fae1fcc85df`  |
| 521    | No file  | `6fae1fcc85df`  |
| 517    | No file  | `6fae1fcc85df`  |
| 510    | No file  | `6fae1fcc85df`  |
| 508    | No file  | `6fae1fcc85df`  |
| 504    | No file  | `6fae1fcc85df`  |
| 497    | No file  | `6fae1fcc85df`  |
| 491    | No file  | `6fae1fcc85df`  |
| 485    | No file  | `6fae1fcc85df`  |
| 478    | No file  | `6fae1fcc85df`  |
| 472    | No file  | `6fae1fcc85df`  |
| 466    | No file  | `6fae1fcc85df`  |
| 457    | No file  | `6fae1fcc85df`  |
| 452    | No file  | `6fae1fcc85df`  |
| 449    | No file  | `6fae1fcc85df`  |
| 435    | No file  | `6fae1fcc85df`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest title (LOC type 18) and item names (type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type | Field                         | Notes                                                                                   |
| ------- | ---- | ----------------------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_copy_quest               | Packed quest ID: low u16 quest chain, high u16 quest (`349098` = chain 21418, quest 5) |
| `+0x04` | u32  | need_item_for_copy            | Item key of the item copy fuel (`45026`, enhancement level 0)                          |
| `+0x08` | u32  | need_item_for_individual_copy | Item key of the single copy fuel (`320157`)                                            |
| `+0x0C` | u32  | unknown_0c                    | `1500` (client 3482); see Open Questions                                                |
| `+0x10` | u32  | unknown_10                    | `100000000` (client 3482); see Open Questions                                           |
| `+0x14` | u32  | unknown_14                    | `0` (client 3482)                                                                       |
| `+0x18` | u32  | unknown_18                    | `0` (client 3482)                                                                       |
| `+0x1C` | u32  | unknown_1c                    | `0` (client 3482)                                                                       |
| `+0x20` | u32  | unknown_20                    | `2000` (client 3482)                                                                    |
| `+0x24` | u32  | unknown_24                    | `0` (client 3482)                                                                       |
| `+0x28` | u32  | unknown_28                    | `1` (client 3482)                                                                       |
| `+0x2C` | u32  | unknown_2c                    | `1` (client 3482)                                                                       |
| `+0x30` | u32  | unknown_30                    | `0` (client 3482)                                                                       |
| `+0x34` | u32  | unknown_34                    | `2` (client 3482)                                                                       |
| `+0x38` | u16  | unknown_38                    | `5396` (`0x1514`, client 3482)                                                          |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
the table, and client 1784 ships no `duelcharacter.bss`. The three names
follow the client Lua (3482) that reads them and the records they point at:

| Field                         | Lua call                                         | Evidence (client 3482)                                                                 |
| ----------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------- |
| item_copy_quest               | `ToClient_isClearedDuelCharacterItemCopyQuest()` | The quest's text says the player can now use Marni's Suspicious Device in the Tag Character menu |
| need_item_for_copy            | `ToClient_getNeedItemForDuelCopy()`              | Marni's Unstable Fuel, "Used to copy gear so that 2 tagged characters can use it at the same time" |
| need_item_for_individual_copy | `ToClient_getNeedItemForIndividuelCopy()`        | Marni's Processed Fuel, used "to use the Single Copy function"                          |

`panel_window_equip_charactertag_itemcopy_all_1.luac` passes both item
keys to `getItemEnchantStaticStatus()`.

## Notes

- The server dump of client 1784 names `DuelCharacterExpValue` with
  `_mainCharacterExpRate`, `_subCharacterExpRate` and
  `_mainCharacterSkillExpRate` under `LocalizingOption`, not under this
  table.

## Open Questions

### What the Eleven Values Hold

`unknown_0c` (`1500`), `unknown_10` (`100000000`), `unknown_20` (`2000`),
`unknown_28` and `unknown_2c` (`1`), `unknown_34` (`2`) and `unknown_38`
(`5396`) have no Lua getter that returns them as is. The item copy window
reads two fuel counts, `ToClient_getCopyItemForDuelNeedItemCount()` and
`ToClient_getAddCopyItemForDuelNeedItemCount()`; they are leads for
`unknown_0c` and one more field, but no data ties a count to an offset.
