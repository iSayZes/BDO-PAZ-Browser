# `instancedungeonskillstatic.dbss` Format

## Purpose

A keyed table whose name points at skill data for instance dungeons. On
client 3473 the file holds no records: it is a u32 count of `0`, and so is
its offset file. On client 1784 it holds 157 records, each a key and a
Korean text with `<PAColor0x...>` tags.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes  | Records                 | Row bytes                |
| ------ | -------------- | ------- | --------------------------------------- | ------ | ----------------------- | ------------------------ |
| 2      | 2243 and later | 3483    | `instancedungeonskillstatic.dbss`       | 4      | -                       | -                        |
| 2      | 2243 and later | 3483    | `instancedungeonskillstaticoffset.dbss` | 4      | -                       | -                        |
| 1      | 1346 to 2235   | 2235    | `instancedungeonskillstatic.dbss`       | 13,984 | 157 Skill Static Record | 20 to 166, 89 on average |
| 1      | 1346 to 2235   | 2235    | `instancedungeonskillstaticoffset.dbss` | 1,888  | 157 Index Row           | 12                       |

| Layout | File                                    | Known            | Unknown          |
| ------ | --------------------------------------- | ---------------- | ---------------- |
| 2      | `instancedungeonskillstatic.dbss`       | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `instancedungeonskillstaticoffset.dbss` | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `instancedungeonskillstatic.dbss`       | 632 B (4.5%)     | 13,352 B (95.5%) |
| 1      | `instancedungeonskillstaticoffset.dbss` | 1,888 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `ddf16dba2c06`  |
| 3482   | Layout 2             | `ddf16dba2c06`  |
| 3474   | Layout 2             | `ddf16dba2c06`  |
| 3473   | Layout 2             | `ddf16dba2c06`  |
| 3464   | Layout 2             | `ddf16dba2c06`  |
| 3458   | Layout 2             | `ddf16dba2c06`  |
| 3454   | Layout 2             | `ddf16dba2c06`  |
| 3444   | Layout 2             | `ddf16dba2c06`  |
| 3435   | Layout 2             | `ddf16dba2c06`  |
| 3426   | Layout 2             | `ddf16dba2c06`  |
| 3418   | Layout 2             | `ddf16dba2c06`  |
| 3412   | Layout 2             | `ddf16dba2c06`  |
| 3402   | Layout 2             | `ddf16dba2c06`  |
| 3396   | Layout 2             | `ddf16dba2c06`  |
| 3387   | Layout 2             | `ddf16dba2c06`  |
| 3381   | Layout 2             | `ddf16dba2c06`  |
| 3373   | Layout 2             | `ddf16dba2c06`  |
| 3364   | Layout 2             | `ddf16dba2c06`  |
| 3356   | Layout 2             | `ddf16dba2c06`  |
| 3349   | Layout 2             | `ddf16dba2c06`  |
| 3342   | Layout 2             | `ddf16dba2c06`  |
| 3335   | Layout 2             | `ddf16dba2c06`  |
| 3326   | Layout 2             | `ddf16dba2c06`  |
| 3321   | Layout 2             | `ddf16dba2c06`  |
| 3314   | Layout 2             | `ddf16dba2c06`  |
| 3303   | Layout 2             | `ddf16dba2c06`  |
| 3302   | Layout 2             | `ddf16dba2c06`  |
| 3293   | Layout 2             | `ddf16dba2c06`  |
| 3283   | Layout 2             | `ddf16dba2c06`  |
| 3275   | Layout 2             | `ddf16dba2c06`  |
| 3267   | Layout 2             | `ddf16dba2c06`  |
| 3258   | Layout 2             | `ddf16dba2c06`  |
| 3251   | Layout 2             | `ddf16dba2c06`  |
| 3242   | Layout 2             | `ddf16dba2c06`  |
| 3235   | Layout 2             | `ddf16dba2c06`  |
| 3229   | Layout 2             | `ddf16dba2c06`  |
| 3212   | Layout 2             | `ddf16dba2c06`  |
| 3203   | Layout 2             | `ddf16dba2c06`  |
| 3193   | Layout 2             | `ddf16dba2c06`  |
| 3186   | Layout 2             | `ddf16dba2c06`  |
| 3177   | Layout 2             | `ddf16dba2c06`  |
| 3169   | Layout 2             | `ddf16dba2c06`  |
| 3158   | Layout 2             | `ddf16dba2c06`  |
| 3151   | Layout 2             | `ddf16dba2c06`  |
| 3144   | Layout 2             | `ddf16dba2c06`  |
| 3133   | Layout 2             | `ddf16dba2c06`  |
| 3125   | Layout 2             | `ddf16dba2c06`  |
| 3118   | Layout 2             | `ddf16dba2c06`  |
| 3111   | Layout 2             | `ddf16dba2c06`  |
| 3103   | Layout 2             | `ddf16dba2c06`  |
| 3095   | Layout 2             | `ddf16dba2c06`  |
| 3086   | Layout 2             | `ddf16dba2c06`  |
| 3072   | Layout 2             | `ddf16dba2c06`  |
| 3062   | Layout 2             | `ddf16dba2c06`  |
| 3052   | Layout 2             | `ddf16dba2c06`  |
| 3045   | Layout 2             | `ddf16dba2c06`  |
| 3037   | Layout 2             | `ddf16dba2c06`  |
| 3030   | Layout 2             | `ddf16dba2c06`  |
| 3021   | Layout 2             | `ddf16dba2c06`  |
| 3012   | Layout 2             | `ddf16dba2c06`  |
| 3002   | Layout 2             | `ddf16dba2c06`  |
| 2995   | Layout 2             | `ddf16dba2c06`  |
| 2987   | Layout 2             | `ddf16dba2c06`  |
| 2978   | Layout 2             | `ddf16dba2c06`  |
| 2970   | Layout 2             | `ddf16dba2c06`  |
| 2959   | Layout 2             | `ddf16dba2c06`  |
| 2951   | Layout 2             | `ddf16dba2c06`  |
| 2942   | Layout 2             | `ddf16dba2c06`  |
| 2935   | Layout 2             | `ddf16dba2c06`  |
| 2932   | Layout 2             | `ddf16dba2c06`  |
| 2923   | Layout 2             | `ddf16dba2c06`  |
| 2919   | Layout 2             | `ddf16dba2c06`  |
| 2907   | Layout 2             | `ddf16dba2c06`  |
| 2900   | Layout 2             | `ddf16dba2c06`  |
| 2891   | Layout 2             | `ddf16dba2c06`  |
| 2882   | Layout 2             | `ddf16dba2c06`  |
| 2872   | Layout 2             | `ddf16dba2c06`  |
| 2863   | Layout 2             | `ddf16dba2c06`  |
| 2855   | Layout 2             | `ddf16dba2c06`  |
| 2849   | Layout 2             | `ddf16dba2c06`  |
| 2844   | Layout 2             | `ddf16dba2c06`  |
| 2834   | Layout 2             | `ddf16dba2c06`  |
| 2825   | Layout 2             | `ddf16dba2c06`  |
| 2819   | Layout 2             | `ddf16dba2c06`  |
| 2811   | Layout 2             | `ddf16dba2c06`  |
| 2803   | Layout 2             | `ddf16dba2c06`  |
| 2794   | Layout 2             | `ddf16dba2c06`  |
| 2783   | Layout 2             | `ddf16dba2c06`  |
| 2774   | Layout 2             | `ddf16dba2c06`  |
| 2765   | Layout 2             | `ddf16dba2c06`  |
| 2756   | Layout 2             | `ddf16dba2c06`  |
| 2750   | Layout 2             | `ddf16dba2c06`  |
| 2743   | Layout 2             | `ddf16dba2c06`  |
| 2736   | Layout 2             | `ddf16dba2c06`  |
| 2726   | Layout 2             | `ddf16dba2c06`  |
| 2717   | Layout 2             | `ddf16dba2c06`  |
| 2709   | Layout 2             | `ddf16dba2c06`  |
| 2703   | Layout 2             | `ddf16dba2c06`  |
| 2695   | Layout 2             | `ddf16dba2c06`  |
| 2684   | Layout 2             | `ddf16dba2c06`  |
| 2672   | Layout 2             | `ddf16dba2c06`  |
| 2665   | Layout 2             | `ddf16dba2c06`  |
| 2657   | Layout 2             | `ddf16dba2c06`  |
| 2649   | Layout 2             | `ddf16dba2c06`  |
| 2644   | Layout 2             | `ddf16dba2c06`  |
| 2637   | Layout 2             | `ddf16dba2c06`  |
| 2629   | Layout 2             | `ddf16dba2c06`  |
| 2619   | Layout 2             | `ddf16dba2c06`  |
| 2612   | Layout 2             | `ddf16dba2c06`  |
| 2606   | Layout 2             | `ddf16dba2c06`  |
| 2602   | Layout 2             | `ddf16dba2c06`  |
| 2601   | Layout 2             | `ddf16dba2c06`  |
| 2592   | Layout 2             | `ddf16dba2c06`  |
| 2583   | Layout 2             | `ddf16dba2c06`  |
| 2575   | Layout 2             | `ddf16dba2c06`  |
| 2567   | Layout 2             | `ddf16dba2c06`  |
| 2560   | Layout 2             | `ddf16dba2c06`  |
| 2553   | Layout 2             | `ddf16dba2c06`  |
| 2545   | Layout 2             | `ddf16dba2c06`  |
| 2538   | Layout 2             | `ddf16dba2c06`  |
| 2529   | Layout 2             | `ddf16dba2c06`  |
| 2519   | Layout 2             | `ddf16dba2c06`  |
| 2513   | Layout 2             | `ddf16dba2c06`  |
| 2510   | Layout 2             | `ddf16dba2c06`  |
| 2507   | Layout 2             | `ddf16dba2c06`  |
| 2503   | Layout 2             | `ddf16dba2c06`  |
| 2498   | Layout 2             | `ddf16dba2c06`  |
| 2492   | Layout 2             | `ddf16dba2c06`  |
| 2487   | Layout 2             | `ddf16dba2c06`  |
| 2480   | Layout 2             | `ddf16dba2c06`  |
| 2474   | Layout 2             | `ddf16dba2c06`  |
| 2468   | Layout 2             | `ddf16dba2c06`  |
| 2460   | Layout 2             | `ddf16dba2c06`  |
| 2453   | Layout 2             | `ddf16dba2c06`  |
| 2444   | Layout 2             | `ddf16dba2c06`  |
| 2438   | Layout 2             | `ddf16dba2c06`  |
| 2434   | Layout 2             | `ddf16dba2c06`  |
| 2429   | Layout 2             | `ddf16dba2c06`  |
| 2421   | Layout 2             | `ddf16dba2c06`  |
| 2414   | Layout 2             | `ddf16dba2c06`  |
| 2407   | Layout 2             | `ddf16dba2c06`  |
| 2401   | Layout 2             | `ddf16dba2c06`  |
| 2397   | Layout 2             | `ddf16dba2c06`  |
| 2393   | Layout 2             | `ddf16dba2c06`  |
| 2384   | Layout 2             | `ddf16dba2c06`  |
| 2378   | Layout 2             | `ddf16dba2c06`  |
| 2372   | Layout 2             | `ddf16dba2c06`  |
| 2358   | Layout 2             | `ddf16dba2c06`  |
| 2352   | Layout 2             | `ddf16dba2c06`  |
| 2347   | Layout 2             | `ddf16dba2c06`  |
| 2343   | Layout 2             | `ddf16dba2c06`  |
| 2335   | Layout 2             | `ddf16dba2c06`  |
| 2327   | Layout 2             | `ddf16dba2c06`  |
| 2324   | Layout 2             | `ddf16dba2c06`  |
| 2319   | Layout 2             | `ddf16dba2c06`  |
| 2313   | Layout 2             | `ddf16dba2c06`  |
| 2308   | Layout 2             | `ddf16dba2c06`  |
| 2302   | Layout 2             | `ddf16dba2c06`  |
| 2295   | Layout 2             | `ddf16dba2c06`  |
| 2290   | Layout 2             | `ddf16dba2c06`  |
| 2284   | Layout 2             | `ddf16dba2c06`  |
| 2276   | Layout 2             | `ddf16dba2c06`  |
| 2269   | Layout 2             | `ddf16dba2c06`  |
| 2259   | Layout 2             | `ddf16dba2c06`  |
| 2250   | Layout 2             | `ddf16dba2c06`  |
| 2243   | Layout 2             | `ddf16dba2c06`  |
| 2235   | Layout 1             | `ddf16dba2c06`  |
| 2229   | Layout 1             | `ddf16dba2c06`  |
| 2224   | Layout 1             | `ddf16dba2c06`  |
| 2218   | Layout 1             | `ddf16dba2c06`  |
| 2215   | Layout 1             | `ddf16dba2c06`  |
| 2207   | Layout 1             | `ddf16dba2c06`  |
| 2203   | Layout 1             | `ddf16dba2c06`  |
| 2196   | Layout 1             | `ddf16dba2c06`  |
| 2192   | Layout 1             | `ddf16dba2c06`  |
| 2189   | Layout 1             | `ddf16dba2c06`  |
| 2183   | Layout 1             | `ddf16dba2c06`  |
| 2179   | Layout 1             | `ddf16dba2c06`  |
| 2171   | Layout 1             | `ddf16dba2c06`  |
| 2163   | Layout 1             | `ddf16dba2c06`  |
| 2156   | Layout 1             | `ddf16dba2c06`  |
| 2151   | Layout 1             | `ddf16dba2c06`  |
| 2147   | Layout 1             | `ddf16dba2c06`  |
| 2142   | Layout 1             | `ddf16dba2c06`  |
| 2138   | Layout 1             | `ddf16dba2c06`  |
| 2134   | Layout 1             | `ddf16dba2c06`  |
| 2130   | Layout 1             | `ddf16dba2c06`  |
| 2122   | Layout 1             | `ddf16dba2c06`  |
| 2107   | Layout 1             | `ddf16dba2c06`  |
| 2098   | Layout 1             | `ddf16dba2c06`  |
| 2089   | Layout 1             | `ddf16dba2c06`  |
| 2081   | Layout 1             | `ddf16dba2c06`  |
| 2073   | Layout 1             | `ddf16dba2c06`  |
| 2067   | Layout 1             | `ddf16dba2c06`  |
| 2063   | Layout 1             | `ddf16dba2c06`  |
| 2059   | Layout 1             | `ddf16dba2c06`  |
| 2052   | Layout 1             | `ddf16dba2c06`  |
| 2044   | Layout 1             | `ddf16dba2c06`  |
| 2039   | Layout 1             | `ddf16dba2c06`  |
| 2032   | Layout 1             | `ddf16dba2c06`  |
| 2025   | Layout 1             | `ddf16dba2c06`  |
| 2011   | Layout 1             | `ddf16dba2c06`  |
| 2005   | Layout 1             | `ddf16dba2c06`  |
| 2000   | Layout 1             | `ddf16dba2c06`  |
| 1996   | Layout 1             | `ddf16dba2c06`  |
| 1991   | Layout 1             | `ddf16dba2c06`  |
| 1985   | Layout 1             | `ddf16dba2c06`  |
| 1980   | Layout 1             | `ddf16dba2c06`  |
| 1969   | Layout 1             | `ddf16dba2c06`  |
| 1964   | Layout 1             | `ddf16dba2c06`  |
| 1958   | Layout 1             | `ddf16dba2c06`  |
| 1950   | Layout 1             | `ddf16dba2c06`  |
| 1945   | Layout 1             | `ddf16dba2c06`  |
| 1937   | Layout 1             | `ddf16dba2c06`  |
| 1933   | Layout 1             | `ddf16dba2c06`  |
| 1927   | Layout 1             | `ddf16dba2c06`  |
| 1921   | Layout 1             | `ddf16dba2c06`  |
| 1914   | Layout 1             | `ddf16dba2c06`  |
| 1908   | Layout 1             | `ddf16dba2c06`  |
| 1897   | Layout 1             | `ddf16dba2c06`  |
| 1892   | Layout 1             | `ddf16dba2c06`  |
| 1886   | Layout 1             | `ddf16dba2c06`  |
| 1881   | Layout 1             | `ddf16dba2c06`  |
| 1871   | Layout 1             | `ddf16dba2c06`  |
| 1866   | Layout 1             | `ddf16dba2c06`  |
| 1862   | Layout 1             | `ddf16dba2c06`  |
| 1854   | Layout 1             | `ddf16dba2c06`  |
| 1846   | Layout 1             | `ddf16dba2c06`  |
| 1838   | Layout 1             | `ddf16dba2c06`  |
| 1832   | Layout 1             | `ddf16dba2c06`  |
| 1826   | Layout 1             | `ddf16dba2c06`  |
| 1822   | Layout 1             | `ddf16dba2c06`  |
| 1818   | Layout 1             | `ddf16dba2c06`  |
| 1804   | Layout 1             | `ddf16dba2c06`  |
| 1794   | Layout 1             | `ddf16dba2c06`  |
| 1790   | Layout 1             | `ddf16dba2c06`  |
| 1784   | Layout 1             | `ddf16dba2c06`  |
| 1774   | Layout 1             | `ddf16dba2c06`  |
| 1771   | Layout 1             | `ddf16dba2c06`  |
| 1762   | Layout 1             | `ddf16dba2c06`  |
| 1759   | Layout 1             | `ddf16dba2c06`  |
| 1754   | Layout 1             | `ddf16dba2c06`  |
| 1749   | Layout 1             | `ddf16dba2c06`  |
| 1743   | Layout 1             | `ddf16dba2c06`  |
| 1737   | Layout 1             | `ddf16dba2c06`  |
| 1731   | Layout 1             | `ddf16dba2c06`  |
| 1725   | Layout 1             | `ddf16dba2c06`  |
| 1717   | Layout 1             | `ddf16dba2c06`  |
| 1710   | Layout 1             | `ddf16dba2c06`  |
| 1704   | Layout 1             | `ddf16dba2c06`  |
| 1698   | Layout 1             | `ddf16dba2c06`  |
| 1690   | Layout 1             | `ddf16dba2c06`  |
| 1685   | Layout 1             | `ddf16dba2c06`  |
| 1680   | Layout 1             | `ddf16dba2c06`  |
| 1674   | Layout 1             | `ddf16dba2c06`  |
| 1668   | Layout 1             | `ddf16dba2c06`  |
| 1659   | Layout 1             | `ddf16dba2c06`  |
| 1649   | Layout 1             | `ddf16dba2c06`  |
| 1642   | Layout 1             | `ddf16dba2c06`  |
| 1636   | Layout 1             | `ddf16dba2c06`  |
| 1628   | Layout 1             | `ddf16dba2c06`  |
| 1622   | Layout 1             | `ddf16dba2c06`  |
| 1614   | Layout 1             | `ddf16dba2c06`  |
| 1608   | Layout 1             | `ddf16dba2c06`  |
| 1602   | Layout 1             | `ddf16dba2c06`  |
| 1598   | Layout 1             | `ddf16dba2c06`  |
| 1594   | Layout 1             | `ddf16dba2c06`  |
| 1590   | Layout 1             | `ddf16dba2c06`  |
| 1587   | Layout 1             | `ddf16dba2c06`  |
| 1584   | Layout 1             | `ddf16dba2c06`  |
| 1579   | Layout 1             | `ddf16dba2c06`  |
| 1572   | Layout 1             | `ddf16dba2c06`  |
| 1565   | Layout 1             | `ddf16dba2c06`  |
| 1559   | Layout 1             | `ddf16dba2c06`  |
| 1554   | Layout 1             | `ddf16dba2c06`  |
| 1547   | Layout 1             | `ddf16dba2c06`  |
| 1537   | Layout 1             | `ddf16dba2c06`  |
| 1529   | Layout 1             | `ddf16dba2c06`  |
| 1524   | Layout 1             | `ddf16dba2c06`  |
| 1519   | Layout 1             | `ddf16dba2c06`  |
| 1509   | Layout 1             | `ddf16dba2c06`  |
| 1506   | Layout 1             | `ddf16dba2c06`  |
| 1504   | Layout 1             | `ddf16dba2c06`  |
| 1500   | Layout 1             | `ddf16dba2c06`  |
| 1493   | Layout 1             | `ddf16dba2c06`  |
| 1489   | Layout 1             | `ddf16dba2c06`  |
| 1485   | Layout 1             | `ddf16dba2c06`  |
| 1481   | Layout 1             | `ddf16dba2c06`  |
| 1474   | Layout 1             | `ddf16dba2c06`  |
| 1466   | Layout 1             | `ddf16dba2c06`  |
| 1462   | Layout 1             | `ddf16dba2c06`  |
| 1459   | Layout 1             | `ddf16dba2c06`  |
| 1453   | Layout 1             | `ddf16dba2c06`  |
| 1450   | Layout 1             | `ddf16dba2c06`  |
| 1445   | Layout 1             | `ddf16dba2c06`  |
| 1439   | Layout 1             | `ddf16dba2c06`  |
| 1433   | Layout 1             | `ddf16dba2c06`  |
| 1430   | Layout 1             | `ddf16dba2c06`  |
| 1426   | Layout 1             | `ddf16dba2c06`  |
| 1421   | Layout 1             | `ddf16dba2c06`  |
| 1417   | Layout 1             | `ddf16dba2c06`  |
| 1416   | Layout 1             | `ddf16dba2c06`  |
| 1409   | Layout 1             | `ddf16dba2c06`  |
| 1405   | Layout 1             | `ddf16dba2c06`  |
| 1401   | Layout 1             | `ddf16dba2c06`  |
| 1396   | Layout 1             | `ddf16dba2c06`  |
| 1391   | Layout 1             | `ddf16dba2c06`  |
| 1390   | Layout 1             | `ddf16dba2c06`  |
| 1386   | Layout 1             | `ddf16dba2c06`  |
| 1381   | Layout 1             | `ddf16dba2c06`  |
| 1379   | Layout 1             | `ddf16dba2c06`  |
| 1372   | Layout 1             | `ddf16dba2c06`  |
| 1366   | Layout 1             | `ddf16dba2c06`  |
| 1364   | Layout 1             | `ddf16dba2c06`  |
| 1363   | Layout 1             | `ddf16dba2c06`  |
| 1360   | Layout 1             | `ddf16dba2c06`  |
| 1358   | Layout 1             | `ddf16dba2c06`  |
| 1355   | Layout 1             | `ddf16dba2c06`  |
| 1351   | Layout 1             | `ddf16dba2c06`  |
| 1348   | Layout 1             | `ddf16dba2c06`  |
| 1346   | Layout 1             | `ddf16dba2c06`  |
| 1341   | No documented layout | `ddf16dba2c06`  |
| 1340   | No documented layout | `ddf16dba2c06`  |
| 1338   | No documented layout | `ddf16dba2c06`  |
| 1335   | No documented layout | `ddf16dba2c06`  |
| 1333   | No documented layout | `ddf16dba2c06`  |
| 1329   | No documented layout | `ddf16dba2c06`  |
| 1327   | No documented layout | `ddf16dba2c06`  |
| 1324   | No documented layout | `ddf16dba2c06`  |
| 1321   | No documented layout | `ddf16dba2c06`  |
| 1319   | No documented layout | `ddf16dba2c06`  |
| 1318   | No documented layout | `ddf16dba2c06`  |
| 1316   | No documented layout | `ddf16dba2c06`  |
| 1313   | No documented layout | `ddf16dba2c06`  |
| 1311   | No documented layout | `ddf16dba2c06`  |
| 1309   | No documented layout | `ddf16dba2c06`  |
| 1304   | No documented layout | `ddf16dba2c06`  |
| 1292   | No documented layout | `ddf16dba2c06`  |
| 1286   | No documented layout | `ddf16dba2c06`  |
| 1280   | No documented layout | `ddf16dba2c06`  |
| 1276   | No documented layout | `ddf16dba2c06`  |
| 1267   | No file              | `ddf16dba2c06`  |
| 1261   | No file              | `ddf16dba2c06`  |
| 1256   | No file              | `ddf16dba2c06`  |
| 1250   | No file              | `ddf16dba2c06`  |
| 1246   | No file              | `ddf16dba2c06`  |
| 1239   | No file              | `ddf16dba2c06`  |
| 1230   | No file              | `ddf16dba2c06`  |
| 1226   | No file              | `ddf16dba2c06`  |
| 1220   | No file              | `ddf16dba2c06`  |
| 1217   | No file              | `ddf16dba2c06`  |
| 1211   | No file              | `ddf16dba2c06`  |
| 1210   | No file              | `ddf16dba2c06`  |
| 1208   | No file              | `ddf16dba2c06`  |
| 1203   | No file              | `ddf16dba2c06`  |
| 1197   | No file              | `ddf16dba2c06`  |
| 1194   | No file              | `ddf16dba2c06`  |
| 1192   | No file              | `ddf16dba2c06`  |
| 1187   | No file              | `ddf16dba2c06`  |
| 1183   | No file              | `ddf16dba2c06`  |
| 1177   | No file              | `ddf16dba2c06`  |
| 1173   | No file              | `ddf16dba2c06`  |
| 1167   | No file              | `ddf16dba2c06`  |
| 1164   | No file              | `ddf16dba2c06`  |
| 1156   | No file              | `ddf16dba2c06`  |
| 1149   | No file              | `ddf16dba2c06`  |
| 1144   | No file              | `ddf16dba2c06`  |
| 1137   | No file              | `ddf16dba2c06`  |
| 1132   | No file              | `ddf16dba2c06`  |
| 1127   | No file              | `ddf16dba2c06`  |
| 1122   | No file              | `ddf16dba2c06`  |
| 1118   | No file              | `ddf16dba2c06`  |
| 1114   | No file              | `ddf16dba2c06`  |
| 1109   | No file              | `ddf16dba2c06`  |
| 1102   | No file              | `ddf16dba2c06`  |
| 1096   | No file              | `ddf16dba2c06`  |
| 1088   | No file              | `ddf16dba2c06`  |
| 1081   | No file              | `ddf16dba2c06`  |
| 1076   | No file              | `ddf16dba2c06`  |
| 1069   | No file              | `ddf16dba2c06`  |
| 1064   | No file              | `ddf16dba2c06`  |
| 1058   | No file              | `ddf16dba2c06`  |
| 1051   | No file              | `ddf16dba2c06`  |
| 1044   | No file              | `ddf16dba2c06`  |
| 1036   | No file              | `ddf16dba2c06`  |
| 1026   | No file              | `ddf16dba2c06`  |
| 1016   | No file              | `ddf16dba2c06`  |
| 1009   | No file              | `ddf16dba2c06`  |
| 1005   | No file              | `ddf16dba2c06`  |
| 1000   | No file              | `ddf16dba2c06`  |
| 998    | No file              | `ddf16dba2c06`  |
| 990    | No file              | `ddf16dba2c06`  |
| 979    | No file              | `ddf16dba2c06`  |
| 972    | No file              | `ddf16dba2c06`  |
| 963    | No file              | `ddf16dba2c06`  |
| 955    | No file              | `ddf16dba2c06`  |
| 946    | No file              | `ddf16dba2c06`  |
| 938    | No file              | `ddf16dba2c06`  |
| 927    | No file              | `ddf16dba2c06`  |
| 911    | No file              | `ddf16dba2c06`  |
| 904    | No file              | `ddf16dba2c06`  |
| 899    | No file              | `ddf16dba2c06`  |
| 894    | No file              | `ddf16dba2c06`  |
| 885    | No file              | `ddf16dba2c06`  |
| 879    | No file              | `ddf16dba2c06`  |
| 872    | No file              | `ddf16dba2c06`  |
| 864    | No file              | `ddf16dba2c06`  |
| 855    | No file              | `ddf16dba2c06`  |
| 853    | No file              | `ddf16dba2c06`  |
| 845    | No file              | `ddf16dba2c06`  |
| 837    | No file              | `ddf16dba2c06`  |
| 829    | No file              | `ddf16dba2c06`  |
| 822    | No file              | `ddf16dba2c06`  |
| 814    | No file              | `ddf16dba2c06`  |
| 805    | No file              | `ddf16dba2c06`  |
| 794    | No file              | `ddf16dba2c06`  |
| 787    | No file              | `ddf16dba2c06`  |
| 780    | No file              | `ddf16dba2c06`  |
| 771    | No file              | `ddf16dba2c06`  |
| 760    | No file              | `ddf16dba2c06`  |
| 748    | No file              | `ddf16dba2c06`  |
| 741    | No file              | `ddf16dba2c06`  |
| 736    | No file              | `ddf16dba2c06`  |
| 731    | No file              | `ddf16dba2c06`  |
| 723    | No file              | `ddf16dba2c06`  |
| 711    | No file              | `ddf16dba2c06`  |
| 707    | No file              | `ddf16dba2c06`  |
| 697    | No file              | `ddf16dba2c06`  |
| 689    | No file              | `ddf16dba2c06`  |
| 683    | No file              | `ddf16dba2c06`  |
| 678    | No file              | `ddf16dba2c06`  |
| 670    | No file              | `ddf16dba2c06`  |
| 661    | No file              | `ddf16dba2c06`  |
| 656    | No file              | `ddf16dba2c06`  |
| 652    | No file              | `ddf16dba2c06`  |
| 643    | No file              | `ddf16dba2c06`  |
| 637    | No file              | `ddf16dba2c06`  |
| 630    | No file              | `ddf16dba2c06`  |
| 627    | No file              | `ddf16dba2c06`  |
| 621    | No file              | `ddf16dba2c06`  |
| 617    | No file              | `ddf16dba2c06`  |
| 615    | No file              | `ddf16dba2c06`  |
| 606    | No file              | `ddf16dba2c06`  |
| 599    | No file              | `ddf16dba2c06`  |
| 592    | No file              | `ddf16dba2c06`  |
| 586    | No file              | `ddf16dba2c06`  |
| 577    | No file              | `ddf16dba2c06`  |
| 569    | No file              | `ddf16dba2c06`  |
| 561    | No file              | `ddf16dba2c06`  |
| 554    | No file              | `ddf16dba2c06`  |
| 542    | No file              | `ddf16dba2c06`  |
| 532    | No file              | `ddf16dba2c06`  |
| 531    | No file              | `ddf16dba2c06`  |
| 526    | No file              | `ddf16dba2c06`  |
| 521    | No file              | `ddf16dba2c06`  |
| 517    | No file              | `ddf16dba2c06`  |
| 510    | No file              | `ddf16dba2c06`  |
| 508    | No file              | `ddf16dba2c06`  |
| 504    | No file              | `ddf16dba2c06`  |
| 497    | No file              | `ddf16dba2c06`  |
| 491    | No file              | `ddf16dba2c06`  |
| 485    | No file              | `ddf16dba2c06`  |
| 478    | No file              | `ddf16dba2c06`  |
| 472    | No file              | `ddf16dba2c06`  |
| 466    | No file              | `ddf16dba2c06`  |
| 457    | No file              | `ddf16dba2c06`  |
| 452    | No file              | `ddf16dba2c06`  |
| 449    | No file              | `ddf16dba2c06`  |
| 435    | No file              | `ddf16dba2c06`  |

<!-- versions:end -->

## Companion Files

None. `instancedungeonskillstaticoffset.dbss` is the offset file of this
table; the PAZ Browser reads both with the Layout 1 records, so client 3473
shows an empty table and client 1784 its 157 records.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type | Field | Notes                                 |
| ------- | ---- | ----- | ------------------------------------- |
| `+0x00` | u32  | count | Number of records; `0` on client 3473 |

### `instancedungeonskillstaticoffset.dbss`

| Offset  | Type | Field | Notes                                              |
| ------- | ---- | ----- | -------------------------------------------------- |
| `+0x00` | u32  | count | Equals the `instancedungeonskillstatic.dbss` count |

## Layout 1

On client 1784 the table holds 157 records, each with an index row in
`instancedungeonskillstaticoffset.dbss`.

### File Layout

| Offset  | Type                       | Field   | Notes                   |
| ------- | -------------------------- | ------- | ----------------------- |
| `+0x00` | u32                        | count   | `157` on client 1784    |
| `+0x04` | Skill Static Record[count] | records | See Skill Static Record |

### Skill Static Record (variable: 16 bytes + text)

| Offset            | Type  | Field         | Notes                                                                 |
| ----------------- | ----- | ------------- | --------------------------------------------------------------------- |
| `+0x00`           | u32   | key           | Record key, equals the index row key; read as two u16 it is `1`, then a number such as `17581` |
| `+0x04`           | str16 | unknown_04    | Korean text with `<PAColor0x...>` tags, such as `<PAColor0xffe9bd23>바운드<PAOldColor>` |
| `unknown_04+0x00` | u32   | unknown_04_00 | `0` on every record (client 1784)                                     |

### `instancedungeonskillstaticoffset.dbss`

| Offset  | Type             | Field | Notes                                              |
| ------- | ---------------- | ----- | -------------------------------------------------- |
| `+0x00` | u32              | count | Equals the `instancedungeonskillstatic.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row                                      |

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u32  | key    | The record's `key`                                       |
| `+0x04` | u32  | offset | Start of the record in the main file plus 4, after `key` |
| `+0x08` | u32  | size   | Record length minus the 4-byte `key`                     |

## Open Questions

### Current Record Layout

Client 3473 ships no records, so whether a filled table would still read
as the client 1784 Skill Static Record is unknown. The handler reads
a filled table as Layout 1 and raises an error when the bytes do not fit it.

### What the Key and Text Hold

The key reads as two u16, `1` and a number such as `17581` (client 1784).
Whether that number is a skill key, and whether `unknown_04` is a skill name
or a tooltip line, is open.
