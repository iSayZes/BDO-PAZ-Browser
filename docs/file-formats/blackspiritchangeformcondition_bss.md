# `blackspiritchangeformcondition.bss` Format

## Purpose

The condition a character must meet before it can change the Black
Spirit's form: the whole file is one UTF-16 condition script. On client
3482 it reads `clearquest(5007,4);getlevel()>55;<or>clearquest(9107,5);getlevel()>59;`
(client 1784: the first alternative only). The forms themselves and the
condition of each are in [`blackspirit.dbss`](blackspirit_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------------------ | ----- | ------- | --------- |
| 1      | 1239 and later | `blackspiritchangeformcondition.bss` | 148   | -       | -         |

| Layout | File                                 | Known          | Unknown    |
| ------ | ------------------------------------ | -------------- | ---------- |
| 1      | `blackspiritchangeformcondition.bss` | 148 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6bb94ac3cf15`  |
| 3482   | Layout 1 | `6bb94ac3cf15`  |
| 3474   | Layout 1 | `6bb94ac3cf15`  |
| 3473   | Layout 1 | `6bb94ac3cf15`  |
| 3464   | Layout 1 | `6bb94ac3cf15`  |
| 3458   | Layout 1 | `6bb94ac3cf15`  |
| 3454   | Layout 1 | `6bb94ac3cf15`  |
| 3444   | Layout 1 | `6bb94ac3cf15`  |
| 3435   | Layout 1 | `6bb94ac3cf15`  |
| 3426   | Layout 1 | `6bb94ac3cf15`  |
| 3418   | Layout 1 | `6bb94ac3cf15`  |
| 3412   | Layout 1 | `6bb94ac3cf15`  |
| 3402   | Layout 1 | `6bb94ac3cf15`  |
| 3396   | Layout 1 | `6bb94ac3cf15`  |
| 3387   | Layout 1 | `6bb94ac3cf15`  |
| 3381   | Layout 1 | `6bb94ac3cf15`  |
| 3373   | Layout 1 | `6bb94ac3cf15`  |
| 3364   | Layout 1 | `6bb94ac3cf15`  |
| 3356   | Layout 1 | `6bb94ac3cf15`  |
| 3349   | Layout 1 | `6bb94ac3cf15`  |
| 3342   | Layout 1 | `6bb94ac3cf15`  |
| 3335   | Layout 1 | `6bb94ac3cf15`  |
| 3326   | Layout 1 | `6bb94ac3cf15`  |
| 3321   | Layout 1 | `6bb94ac3cf15`  |
| 3314   | Layout 1 | `6bb94ac3cf15`  |
| 3303   | Layout 1 | `6bb94ac3cf15`  |
| 3302   | Layout 1 | `6bb94ac3cf15`  |
| 3293   | Layout 1 | `6bb94ac3cf15`  |
| 3283   | Layout 1 | `6bb94ac3cf15`  |
| 3275   | Layout 1 | `6bb94ac3cf15`  |
| 3267   | Layout 1 | `6bb94ac3cf15`  |
| 3258   | Layout 1 | `6bb94ac3cf15`  |
| 3251   | Layout 1 | `6bb94ac3cf15`  |
| 3242   | Layout 1 | `6bb94ac3cf15`  |
| 3235   | Layout 1 | `6bb94ac3cf15`  |
| 3229   | Layout 1 | `6bb94ac3cf15`  |
| 3212   | Layout 1 | `6bb94ac3cf15`  |
| 3203   | Layout 1 | `6bb94ac3cf15`  |
| 3193   | Layout 1 | `6bb94ac3cf15`  |
| 3186   | Layout 1 | `6bb94ac3cf15`  |
| 3177   | Layout 1 | `6bb94ac3cf15`  |
| 3169   | Layout 1 | `6bb94ac3cf15`  |
| 3158   | Layout 1 | `6bb94ac3cf15`  |
| 3151   | Layout 1 | `6bb94ac3cf15`  |
| 3144   | Layout 1 | `6bb94ac3cf15`  |
| 3133   | Layout 1 | `6bb94ac3cf15`  |
| 3125   | Layout 1 | `6bb94ac3cf15`  |
| 3118   | Layout 1 | `6bb94ac3cf15`  |
| 3111   | Layout 1 | `6bb94ac3cf15`  |
| 3103   | Layout 1 | `6bb94ac3cf15`  |
| 3095   | Layout 1 | `6bb94ac3cf15`  |
| 3086   | Layout 1 | `6bb94ac3cf15`  |
| 3072   | Layout 1 | `6bb94ac3cf15`  |
| 3062   | Layout 1 | `6bb94ac3cf15`  |
| 3052   | Layout 1 | `6bb94ac3cf15`  |
| 3045   | Layout 1 | `6bb94ac3cf15`  |
| 3037   | Layout 1 | `6bb94ac3cf15`  |
| 3030   | Layout 1 | `6bb94ac3cf15`  |
| 3021   | Layout 1 | `6bb94ac3cf15`  |
| 3012   | Layout 1 | `6bb94ac3cf15`  |
| 3002   | Layout 1 | `6bb94ac3cf15`  |
| 2995   | Layout 1 | `6bb94ac3cf15`  |
| 2987   | Layout 1 | `6bb94ac3cf15`  |
| 2978   | Layout 1 | `6bb94ac3cf15`  |
| 2970   | Layout 1 | `6bb94ac3cf15`  |
| 2959   | Layout 1 | `6bb94ac3cf15`  |
| 2951   | Layout 1 | `6bb94ac3cf15`  |
| 2942   | Layout 1 | `6bb94ac3cf15`  |
| 2935   | Layout 1 | `6bb94ac3cf15`  |
| 2932   | Layout 1 | `6bb94ac3cf15`  |
| 2923   | Layout 1 | `6bb94ac3cf15`  |
| 2919   | Layout 1 | `6bb94ac3cf15`  |
| 2907   | Layout 1 | `6bb94ac3cf15`  |
| 2900   | Layout 1 | `6bb94ac3cf15`  |
| 2891   | Layout 1 | `6bb94ac3cf15`  |
| 2882   | Layout 1 | `6bb94ac3cf15`  |
| 2872   | Layout 1 | `6bb94ac3cf15`  |
| 2863   | Layout 1 | `6bb94ac3cf15`  |
| 2855   | Layout 1 | `6bb94ac3cf15`  |
| 2849   | Layout 1 | `6bb94ac3cf15`  |
| 2844   | Layout 1 | `6bb94ac3cf15`  |
| 2834   | Layout 1 | `6bb94ac3cf15`  |
| 2825   | Layout 1 | `6bb94ac3cf15`  |
| 2819   | Layout 1 | `6bb94ac3cf15`  |
| 2811   | Layout 1 | `6bb94ac3cf15`  |
| 2803   | Layout 1 | `6bb94ac3cf15`  |
| 2794   | Layout 1 | `6bb94ac3cf15`  |
| 2783   | Layout 1 | `6bb94ac3cf15`  |
| 2774   | Layout 1 | `6bb94ac3cf15`  |
| 2765   | Layout 1 | `6bb94ac3cf15`  |
| 2756   | Layout 1 | `6bb94ac3cf15`  |
| 2750   | Layout 1 | `6bb94ac3cf15`  |
| 2743   | Layout 1 | `6bb94ac3cf15`  |
| 2736   | Layout 1 | `6bb94ac3cf15`  |
| 2726   | Layout 1 | `6bb94ac3cf15`  |
| 2717   | Layout 1 | `6bb94ac3cf15`  |
| 2709   | Layout 1 | `6bb94ac3cf15`  |
| 2703   | Layout 1 | `6bb94ac3cf15`  |
| 2695   | Layout 1 | `6bb94ac3cf15`  |
| 2684   | Layout 1 | `6bb94ac3cf15`  |
| 2672   | Layout 1 | `6bb94ac3cf15`  |
| 2665   | Layout 1 | `6bb94ac3cf15`  |
| 2657   | Layout 1 | `6bb94ac3cf15`  |
| 2649   | Layout 1 | `6bb94ac3cf15`  |
| 2644   | Layout 1 | `6bb94ac3cf15`  |
| 2637   | Layout 1 | `6bb94ac3cf15`  |
| 2629   | Layout 1 | `6bb94ac3cf15`  |
| 2619   | Layout 1 | `6bb94ac3cf15`  |
| 2612   | Layout 1 | `6bb94ac3cf15`  |
| 2606   | Layout 1 | `6bb94ac3cf15`  |
| 2602   | Layout 1 | `6bb94ac3cf15`  |
| 2601   | Layout 1 | `6bb94ac3cf15`  |
| 2592   | Layout 1 | `6bb94ac3cf15`  |
| 2583   | Layout 1 | `6bb94ac3cf15`  |
| 2575   | Layout 1 | `6bb94ac3cf15`  |
| 2567   | Layout 1 | `6bb94ac3cf15`  |
| 2560   | Layout 1 | `6bb94ac3cf15`  |
| 2553   | Layout 1 | `6bb94ac3cf15`  |
| 2545   | Layout 1 | `6bb94ac3cf15`  |
| 2538   | Layout 1 | `6bb94ac3cf15`  |
| 2529   | Layout 1 | `6bb94ac3cf15`  |
| 2519   | Layout 1 | `6bb94ac3cf15`  |
| 2513   | Layout 1 | `6bb94ac3cf15`  |
| 2510   | Layout 1 | `6bb94ac3cf15`  |
| 2507   | Layout 1 | `6bb94ac3cf15`  |
| 2503   | Layout 1 | `6bb94ac3cf15`  |
| 2498   | Layout 1 | `6bb94ac3cf15`  |
| 2492   | Layout 1 | `6bb94ac3cf15`  |
| 2487   | Layout 1 | `6bb94ac3cf15`  |
| 2480   | Layout 1 | `6bb94ac3cf15`  |
| 2474   | Layout 1 | `6bb94ac3cf15`  |
| 2468   | Layout 1 | `6bb94ac3cf15`  |
| 2460   | Layout 1 | `6bb94ac3cf15`  |
| 2453   | Layout 1 | `6bb94ac3cf15`  |
| 2444   | Layout 1 | `6bb94ac3cf15`  |
| 2438   | Layout 1 | `6bb94ac3cf15`  |
| 2434   | Layout 1 | `6bb94ac3cf15`  |
| 2429   | Layout 1 | `6bb94ac3cf15`  |
| 2421   | Layout 1 | `6bb94ac3cf15`  |
| 2414   | Layout 1 | `6bb94ac3cf15`  |
| 2407   | Layout 1 | `6bb94ac3cf15`  |
| 2401   | Layout 1 | `6bb94ac3cf15`  |
| 2397   | Layout 1 | `6bb94ac3cf15`  |
| 2393   | Layout 1 | `6bb94ac3cf15`  |
| 2384   | Layout 1 | `6bb94ac3cf15`  |
| 2378   | Layout 1 | `6bb94ac3cf15`  |
| 2372   | Layout 1 | `6bb94ac3cf15`  |
| 2358   | Layout 1 | `6bb94ac3cf15`  |
| 2352   | Layout 1 | `6bb94ac3cf15`  |
| 2347   | Layout 1 | `6bb94ac3cf15`  |
| 2343   | Layout 1 | `6bb94ac3cf15`  |
| 2335   | Layout 1 | `6bb94ac3cf15`  |
| 2327   | Layout 1 | `6bb94ac3cf15`  |
| 2324   | Layout 1 | `6bb94ac3cf15`  |
| 2319   | Layout 1 | `6bb94ac3cf15`  |
| 2313   | Layout 1 | `6bb94ac3cf15`  |
| 2308   | Layout 1 | `6bb94ac3cf15`  |
| 2302   | Layout 1 | `6bb94ac3cf15`  |
| 2295   | Layout 1 | `6bb94ac3cf15`  |
| 2290   | Layout 1 | `6bb94ac3cf15`  |
| 2284   | Layout 1 | `6bb94ac3cf15`  |
| 2276   | Layout 1 | `6bb94ac3cf15`  |
| 2269   | Layout 1 | `6bb94ac3cf15`  |
| 2259   | Layout 1 | `6bb94ac3cf15`  |
| 2250   | Layout 1 | `6bb94ac3cf15`  |
| 2243   | Layout 1 | `6bb94ac3cf15`  |
| 2235   | Layout 1 | `6bb94ac3cf15`  |
| 2229   | Layout 1 | `6bb94ac3cf15`  |
| 2224   | Layout 1 | `6bb94ac3cf15`  |
| 2218   | Layout 1 | `6bb94ac3cf15`  |
| 2215   | Layout 1 | `6bb94ac3cf15`  |
| 2207   | Layout 1 | `6bb94ac3cf15`  |
| 2203   | Layout 1 | `6bb94ac3cf15`  |
| 2196   | Layout 1 | `6bb94ac3cf15`  |
| 2192   | Layout 1 | `6bb94ac3cf15`  |
| 2189   | Layout 1 | `6bb94ac3cf15`  |
| 2183   | Layout 1 | `6bb94ac3cf15`  |
| 2179   | Layout 1 | `6bb94ac3cf15`  |
| 2171   | Layout 1 | `6bb94ac3cf15`  |
| 2163   | Layout 1 | `6bb94ac3cf15`  |
| 2156   | Layout 1 | `6bb94ac3cf15`  |
| 2151   | Layout 1 | `6bb94ac3cf15`  |
| 2147   | Layout 1 | `6bb94ac3cf15`  |
| 2142   | Layout 1 | `6bb94ac3cf15`  |
| 2138   | Layout 1 | `6bb94ac3cf15`  |
| 2134   | Layout 1 | `6bb94ac3cf15`  |
| 2130   | Layout 1 | `6bb94ac3cf15`  |
| 2122   | Layout 1 | `6bb94ac3cf15`  |
| 2107   | Layout 1 | `6bb94ac3cf15`  |
| 2098   | Layout 1 | `6bb94ac3cf15`  |
| 2089   | Layout 1 | `6bb94ac3cf15`  |
| 2081   | Layout 1 | `6bb94ac3cf15`  |
| 2073   | Layout 1 | `6bb94ac3cf15`  |
| 2067   | Layout 1 | `6bb94ac3cf15`  |
| 2063   | Layout 1 | `6bb94ac3cf15`  |
| 2059   | Layout 1 | `6bb94ac3cf15`  |
| 2052   | Layout 1 | `6bb94ac3cf15`  |
| 2044   | Layout 1 | `6bb94ac3cf15`  |
| 2039   | Layout 1 | `6bb94ac3cf15`  |
| 2032   | Layout 1 | `6bb94ac3cf15`  |
| 2025   | Layout 1 | `6bb94ac3cf15`  |
| 2011   | Layout 1 | `6bb94ac3cf15`  |
| 2005   | Layout 1 | `6bb94ac3cf15`  |
| 2000   | Layout 1 | `6bb94ac3cf15`  |
| 1996   | Layout 1 | `6bb94ac3cf15`  |
| 1991   | Layout 1 | `6bb94ac3cf15`  |
| 1985   | Layout 1 | `6bb94ac3cf15`  |
| 1980   | Layout 1 | `6bb94ac3cf15`  |
| 1969   | Layout 1 | `6bb94ac3cf15`  |
| 1964   | Layout 1 | `6bb94ac3cf15`  |
| 1958   | Layout 1 | `6bb94ac3cf15`  |
| 1950   | Layout 1 | `6bb94ac3cf15`  |
| 1945   | Layout 1 | `6bb94ac3cf15`  |
| 1937   | Layout 1 | `6bb94ac3cf15`  |
| 1933   | Layout 1 | `6bb94ac3cf15`  |
| 1927   | Layout 1 | `6bb94ac3cf15`  |
| 1921   | Layout 1 | `6bb94ac3cf15`  |
| 1914   | Layout 1 | `6bb94ac3cf15`  |
| 1908   | Layout 1 | `6bb94ac3cf15`  |
| 1897   | Layout 1 | `6bb94ac3cf15`  |
| 1892   | Layout 1 | `6bb94ac3cf15`  |
| 1886   | Layout 1 | `6bb94ac3cf15`  |
| 1881   | Layout 1 | `6bb94ac3cf15`  |
| 1871   | Layout 1 | `6bb94ac3cf15`  |
| 1866   | Layout 1 | `6bb94ac3cf15`  |
| 1862   | Layout 1 | `6bb94ac3cf15`  |
| 1854   | Layout 1 | `6bb94ac3cf15`  |
| 1846   | Layout 1 | `6bb94ac3cf15`  |
| 1838   | Layout 1 | `6bb94ac3cf15`  |
| 1832   | Layout 1 | `6bb94ac3cf15`  |
| 1826   | Layout 1 | `6bb94ac3cf15`  |
| 1822   | Layout 1 | `6bb94ac3cf15`  |
| 1818   | Layout 1 | `6bb94ac3cf15`  |
| 1804   | Layout 1 | `6bb94ac3cf15`  |
| 1794   | Layout 1 | `6bb94ac3cf15`  |
| 1790   | Layout 1 | `6bb94ac3cf15`  |
| 1784   | Layout 1 | `6bb94ac3cf15`  |
| 1774   | Layout 1 | `6bb94ac3cf15`  |
| 1771   | Layout 1 | `6bb94ac3cf15`  |
| 1762   | Layout 1 | `6bb94ac3cf15`  |
| 1759   | Layout 1 | `6bb94ac3cf15`  |
| 1754   | Layout 1 | `6bb94ac3cf15`  |
| 1749   | Layout 1 | `6bb94ac3cf15`  |
| 1743   | Layout 1 | `6bb94ac3cf15`  |
| 1737   | Layout 1 | `6bb94ac3cf15`  |
| 1731   | Layout 1 | `6bb94ac3cf15`  |
| 1725   | Layout 1 | `6bb94ac3cf15`  |
| 1717   | Layout 1 | `6bb94ac3cf15`  |
| 1710   | Layout 1 | `6bb94ac3cf15`  |
| 1704   | Layout 1 | `6bb94ac3cf15`  |
| 1698   | Layout 1 | `6bb94ac3cf15`  |
| 1690   | Layout 1 | `6bb94ac3cf15`  |
| 1685   | Layout 1 | `6bb94ac3cf15`  |
| 1680   | Layout 1 | `6bb94ac3cf15`  |
| 1674   | Layout 1 | `6bb94ac3cf15`  |
| 1668   | Layout 1 | `6bb94ac3cf15`  |
| 1659   | Layout 1 | `6bb94ac3cf15`  |
| 1649   | Layout 1 | `6bb94ac3cf15`  |
| 1642   | Layout 1 | `6bb94ac3cf15`  |
| 1636   | Layout 1 | `6bb94ac3cf15`  |
| 1628   | Layout 1 | `6bb94ac3cf15`  |
| 1622   | Layout 1 | `6bb94ac3cf15`  |
| 1614   | Layout 1 | `6bb94ac3cf15`  |
| 1608   | Layout 1 | `6bb94ac3cf15`  |
| 1602   | Layout 1 | `6bb94ac3cf15`  |
| 1598   | Layout 1 | `6bb94ac3cf15`  |
| 1594   | Layout 1 | `6bb94ac3cf15`  |
| 1590   | Layout 1 | `6bb94ac3cf15`  |
| 1587   | Layout 1 | `6bb94ac3cf15`  |
| 1584   | Layout 1 | `6bb94ac3cf15`  |
| 1579   | Layout 1 | `6bb94ac3cf15`  |
| 1572   | Layout 1 | `6bb94ac3cf15`  |
| 1565   | Layout 1 | `6bb94ac3cf15`  |
| 1559   | Layout 1 | `6bb94ac3cf15`  |
| 1554   | Layout 1 | `6bb94ac3cf15`  |
| 1547   | Layout 1 | `6bb94ac3cf15`  |
| 1537   | Layout 1 | `6bb94ac3cf15`  |
| 1529   | Layout 1 | `6bb94ac3cf15`  |
| 1524   | Layout 1 | `6bb94ac3cf15`  |
| 1519   | Layout 1 | `6bb94ac3cf15`  |
| 1509   | Layout 1 | `6bb94ac3cf15`  |
| 1506   | Layout 1 | `6bb94ac3cf15`  |
| 1504   | Layout 1 | `6bb94ac3cf15`  |
| 1500   | Layout 1 | `6bb94ac3cf15`  |
| 1493   | Layout 1 | `6bb94ac3cf15`  |
| 1489   | Layout 1 | `6bb94ac3cf15`  |
| 1485   | Layout 1 | `6bb94ac3cf15`  |
| 1481   | Layout 1 | `6bb94ac3cf15`  |
| 1474   | Layout 1 | `6bb94ac3cf15`  |
| 1466   | Layout 1 | `6bb94ac3cf15`  |
| 1462   | Layout 1 | `6bb94ac3cf15`  |
| 1459   | Layout 1 | `6bb94ac3cf15`  |
| 1453   | Layout 1 | `6bb94ac3cf15`  |
| 1450   | Layout 1 | `6bb94ac3cf15`  |
| 1445   | Layout 1 | `6bb94ac3cf15`  |
| 1439   | Layout 1 | `6bb94ac3cf15`  |
| 1433   | Layout 1 | `6bb94ac3cf15`  |
| 1430   | Layout 1 | `6bb94ac3cf15`  |
| 1426   | Layout 1 | `6bb94ac3cf15`  |
| 1421   | Layout 1 | `6bb94ac3cf15`  |
| 1417   | Layout 1 | `6bb94ac3cf15`  |
| 1416   | Layout 1 | `6bb94ac3cf15`  |
| 1409   | Layout 1 | `6bb94ac3cf15`  |
| 1405   | Layout 1 | `6bb94ac3cf15`  |
| 1401   | Layout 1 | `6bb94ac3cf15`  |
| 1396   | Layout 1 | `6bb94ac3cf15`  |
| 1391   | Layout 1 | `6bb94ac3cf15`  |
| 1390   | Layout 1 | `6bb94ac3cf15`  |
| 1386   | Layout 1 | `6bb94ac3cf15`  |
| 1381   | Layout 1 | `6bb94ac3cf15`  |
| 1379   | Layout 1 | `6bb94ac3cf15`  |
| 1372   | Layout 1 | `6bb94ac3cf15`  |
| 1366   | Layout 1 | `6bb94ac3cf15`  |
| 1364   | Layout 1 | `6bb94ac3cf15`  |
| 1363   | Layout 1 | `6bb94ac3cf15`  |
| 1360   | Layout 1 | `6bb94ac3cf15`  |
| 1358   | Layout 1 | `6bb94ac3cf15`  |
| 1355   | Layout 1 | `6bb94ac3cf15`  |
| 1351   | Layout 1 | `6bb94ac3cf15`  |
| 1348   | Layout 1 | `6bb94ac3cf15`  |
| 1346   | Layout 1 | `6bb94ac3cf15`  |
| 1341   | Layout 1 | `6bb94ac3cf15`  |
| 1340   | Layout 1 | `6bb94ac3cf15`  |
| 1338   | Layout 1 | `6bb94ac3cf15`  |
| 1335   | Layout 1 | `6bb94ac3cf15`  |
| 1333   | Layout 1 | `6bb94ac3cf15`  |
| 1329   | Layout 1 | `6bb94ac3cf15`  |
| 1327   | Layout 1 | `6bb94ac3cf15`  |
| 1324   | Layout 1 | `6bb94ac3cf15`  |
| 1321   | Layout 1 | `6bb94ac3cf15`  |
| 1319   | Layout 1 | `6bb94ac3cf15`  |
| 1318   | Layout 1 | `6bb94ac3cf15`  |
| 1316   | Layout 1 | `6bb94ac3cf15`  |
| 1313   | Layout 1 | `6bb94ac3cf15`  |
| 1311   | Layout 1 | `6bb94ac3cf15`  |
| 1309   | Layout 1 | `6bb94ac3cf15`  |
| 1304   | Layout 1 | `6bb94ac3cf15`  |
| 1292   | Layout 1 | `6bb94ac3cf15`  |
| 1286   | Layout 1 | `6bb94ac3cf15`  |
| 1280   | Layout 1 | `6bb94ac3cf15`  |
| 1276   | Layout 1 | `6bb94ac3cf15`  |
| 1267   | Layout 1 | `6bb94ac3cf15`  |
| 1261   | Layout 1 | `6bb94ac3cf15`  |
| 1256   | Layout 1 | `6bb94ac3cf15`  |
| 1250   | Layout 1 | `6bb94ac3cf15`  |
| 1246   | Layout 1 | `6bb94ac3cf15`  |
| 1239   | Layout 1 | `6bb94ac3cf15`  |
| 1230   | No file  | `6bb94ac3cf15`  |
| 1226   | No file  | `6bb94ac3cf15`  |
| 1220   | No file  | `6bb94ac3cf15`  |
| 1217   | No file  | `6bb94ac3cf15`  |
| 1211   | No file  | `6bb94ac3cf15`  |
| 1210   | No file  | `6bb94ac3cf15`  |
| 1208   | No file  | `6bb94ac3cf15`  |
| 1203   | No file  | `6bb94ac3cf15`  |
| 1197   | No file  | `6bb94ac3cf15`  |
| 1194   | No file  | `6bb94ac3cf15`  |
| 1192   | No file  | `6bb94ac3cf15`  |
| 1187   | No file  | `6bb94ac3cf15`  |
| 1183   | No file  | `6bb94ac3cf15`  |
| 1177   | No file  | `6bb94ac3cf15`  |
| 1173   | No file  | `6bb94ac3cf15`  |
| 1167   | No file  | `6bb94ac3cf15`  |
| 1164   | No file  | `6bb94ac3cf15`  |
| 1156   | No file  | `6bb94ac3cf15`  |
| 1149   | No file  | `6bb94ac3cf15`  |
| 1144   | No file  | `6bb94ac3cf15`  |
| 1137   | No file  | `6bb94ac3cf15`  |
| 1132   | No file  | `6bb94ac3cf15`  |
| 1127   | No file  | `6bb94ac3cf15`  |
| 1122   | No file  | `6bb94ac3cf15`  |
| 1118   | No file  | `6bb94ac3cf15`  |
| 1114   | No file  | `6bb94ac3cf15`  |
| 1109   | No file  | `6bb94ac3cf15`  |
| 1102   | No file  | `6bb94ac3cf15`  |
| 1096   | No file  | `6bb94ac3cf15`  |
| 1088   | No file  | `6bb94ac3cf15`  |
| 1081   | No file  | `6bb94ac3cf15`  |
| 1076   | No file  | `6bb94ac3cf15`  |
| 1069   | No file  | `6bb94ac3cf15`  |
| 1064   | No file  | `6bb94ac3cf15`  |
| 1058   | No file  | `6bb94ac3cf15`  |
| 1051   | No file  | `6bb94ac3cf15`  |
| 1044   | No file  | `6bb94ac3cf15`  |
| 1036   | No file  | `6bb94ac3cf15`  |
| 1026   | No file  | `6bb94ac3cf15`  |
| 1016   | No file  | `6bb94ac3cf15`  |
| 1009   | No file  | `6bb94ac3cf15`  |
| 1005   | No file  | `6bb94ac3cf15`  |
| 1000   | No file  | `6bb94ac3cf15`  |
| 998    | No file  | `6bb94ac3cf15`  |
| 990    | No file  | `6bb94ac3cf15`  |
| 979    | No file  | `6bb94ac3cf15`  |
| 972    | No file  | `6bb94ac3cf15`  |
| 963    | No file  | `6bb94ac3cf15`  |
| 955    | No file  | `6bb94ac3cf15`  |
| 946    | No file  | `6bb94ac3cf15`  |
| 938    | No file  | `6bb94ac3cf15`  |
| 927    | No file  | `6bb94ac3cf15`  |
| 911    | No file  | `6bb94ac3cf15`  |
| 904    | No file  | `6bb94ac3cf15`  |
| 899    | No file  | `6bb94ac3cf15`  |
| 894    | No file  | `6bb94ac3cf15`  |
| 885    | No file  | `6bb94ac3cf15`  |
| 879    | No file  | `6bb94ac3cf15`  |
| 872    | No file  | `6bb94ac3cf15`  |
| 864    | No file  | `6bb94ac3cf15`  |
| 855    | No file  | `6bb94ac3cf15`  |
| 853    | No file  | `6bb94ac3cf15`  |
| 845    | No file  | `6bb94ac3cf15`  |
| 837    | No file  | `6bb94ac3cf15`  |
| 829    | No file  | `6bb94ac3cf15`  |
| 822    | No file  | `6bb94ac3cf15`  |
| 814    | No file  | `6bb94ac3cf15`  |
| 805    | No file  | `6bb94ac3cf15`  |
| 794    | No file  | `6bb94ac3cf15`  |
| 787    | No file  | `6bb94ac3cf15`  |
| 780    | No file  | `6bb94ac3cf15`  |
| 771    | No file  | `6bb94ac3cf15`  |
| 760    | No file  | `6bb94ac3cf15`  |
| 748    | No file  | `6bb94ac3cf15`  |
| 741    | No file  | `6bb94ac3cf15`  |
| 736    | No file  | `6bb94ac3cf15`  |
| 731    | No file  | `6bb94ac3cf15`  |
| 723    | No file  | `6bb94ac3cf15`  |
| 711    | No file  | `6bb94ac3cf15`  |
| 707    | No file  | `6bb94ac3cf15`  |
| 697    | No file  | `6bb94ac3cf15`  |
| 689    | No file  | `6bb94ac3cf15`  |
| 683    | No file  | `6bb94ac3cf15`  |
| 678    | No file  | `6bb94ac3cf15`  |
| 670    | No file  | `6bb94ac3cf15`  |
| 661    | No file  | `6bb94ac3cf15`  |
| 656    | No file  | `6bb94ac3cf15`  |
| 652    | No file  | `6bb94ac3cf15`  |
| 643    | No file  | `6bb94ac3cf15`  |
| 637    | No file  | `6bb94ac3cf15`  |
| 630    | No file  | `6bb94ac3cf15`  |
| 627    | No file  | `6bb94ac3cf15`  |
| 621    | No file  | `6bb94ac3cf15`  |
| 617    | No file  | `6bb94ac3cf15`  |
| 615    | No file  | `6bb94ac3cf15`  |
| 606    | No file  | `6bb94ac3cf15`  |
| 599    | No file  | `6bb94ac3cf15`  |
| 592    | No file  | `6bb94ac3cf15`  |
| 586    | No file  | `6bb94ac3cf15`  |
| 577    | No file  | `6bb94ac3cf15`  |
| 569    | No file  | `6bb94ac3cf15`  |
| 561    | No file  | `6bb94ac3cf15`  |
| 554    | No file  | `6bb94ac3cf15`  |
| 542    | No file  | `6bb94ac3cf15`  |
| 532    | No file  | `6bb94ac3cf15`  |
| 531    | No file  | `6bb94ac3cf15`  |
| 526    | No file  | `6bb94ac3cf15`  |
| 521    | No file  | `6bb94ac3cf15`  |
| 517    | No file  | `6bb94ac3cf15`  |
| 510    | No file  | `6bb94ac3cf15`  |
| 508    | No file  | `6bb94ac3cf15`  |
| 504    | No file  | `6bb94ac3cf15`  |
| 497    | No file  | `6bb94ac3cf15`  |
| 491    | No file  | `6bb94ac3cf15`  |
| 485    | No file  | `6bb94ac3cf15`  |
| 478    | No file  | `6bb94ac3cf15`  |
| 472    | No file  | `6bb94ac3cf15`  |
| 466    | No file  | `6bb94ac3cf15`  |
| 457    | No file  | `6bb94ac3cf15`  |
| 452    | No file  | `6bb94ac3cf15`  |
| 449    | No file  | `6bb94ac3cf15`  |
| 435    | No file  | `6bb94ac3cf15`  |

<!-- versions:end -->

## Companion Files

None; the handler reads this file alone.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type  | Field            | Notes                                                   |
| ------- | ----- | ---------------- | ------------------------------------------------------- |
| `+0x00` | str16 | change_condition | Condition script, `<or>` between alternatives; ends the file |

On client 3482 the file is 8 + 2 x 70 = 148 bytes.

## Field Names

The `Option_Table` sheet of `DataSheet_BlackSpirit.xlsx` in a private
server's `DataSheet` folder on client 1784 has one column,
`ChangeCondition`, and one row: `clearquest(5007,4);getlevel()>55;`, the
same text as the client 1784 file. The server dump of that client names the
loader `loadBlackSpiritChangeFormConditionInfo`.

## Notes

- No client Lua (3482) reads the condition; the skin select window
  (`panel_widget_blackspirit_skillselect.luac`) lists only the forms the
  client reports as unlocked.
