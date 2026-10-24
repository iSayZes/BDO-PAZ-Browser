# `servantinteraction.dbss` Format

## Purpose

Which horse interactions (Horse Communion) each servant offers: one record
per servant character with a cooldown and a list of
[servantbuff.dbss](servantbuff_dbss.md) keys. On client 3474 the file has
311 records, and every one holds cooldown 1,200,000 and the buff keys 1, 2
and 3.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | -------------- | --------- |
| 2      | 3464 and later | 3483    | `servantinteraction.dbss`       | 9,956 | 311 Record     | 32        |
| 2      | 3464 and later | 3483    | `servantinteractionoffset.dbss` | 3,114 | 311 Offset Row | 10        |
| 1      | 1346 to 3458   | 3458    | `servantinteraction.dbss`       | 8,090 | 311 Record     | 26        |
| 1      | 1346 to 3458   | 3458    | `servantinteractionoffset.dbss` | 3,114 | 311 Offset Row | 10        |

| Layout | File                            | Known            | Unknown    |
| ------ | ------------------------------- | ---------------- | ---------- |
| 2      | `servantinteraction.dbss`       | 9,956 B (100.0%) | 0 B (0.0%) |
| 2      | `servantinteractionoffset.dbss` | 3,114 B (100.0%) | 0 B (0.0%) |
| 1      | `servantinteraction.dbss`       | 8,090 B (100.0%) | 0 B (0.0%) |
| 1      | `servantinteractionoffset.dbss` | 3,114 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `6a12f2bbb493`  |
| 3482   | Layout 2             | `6a12f2bbb493`  |
| 3474   | Layout 2             | `6a12f2bbb493`  |
| 3473   | Layout 2             | `6a12f2bbb493`  |
| 3464   | Layout 2             | `6a12f2bbb493`  |
| 3458   | Layout 1             | `6a12f2bbb493`  |
| 3454   | Layout 1             | `6a12f2bbb493`  |
| 3444   | Layout 1             | `6a12f2bbb493`  |
| 3435   | Layout 1             | `6a12f2bbb493`  |
| 3426   | Layout 1             | `6a12f2bbb493`  |
| 3418   | Layout 1             | `6a12f2bbb493`  |
| 3412   | Layout 1             | `6a12f2bbb493`  |
| 3402   | Layout 1             | `6a12f2bbb493`  |
| 3396   | Layout 1             | `6a12f2bbb493`  |
| 3387   | Layout 1             | `6a12f2bbb493`  |
| 3381   | Layout 1             | `6a12f2bbb493`  |
| 3373   | Layout 1             | `6a12f2bbb493`  |
| 3364   | Layout 1             | `6a12f2bbb493`  |
| 3356   | Layout 1             | `6a12f2bbb493`  |
| 3349   | Layout 1             | `6a12f2bbb493`  |
| 3342   | Layout 1             | `6a12f2bbb493`  |
| 3335   | Layout 1             | `6a12f2bbb493`  |
| 3326   | Layout 1             | `6a12f2bbb493`  |
| 3321   | Layout 1             | `6a12f2bbb493`  |
| 3314   | Layout 1             | `6a12f2bbb493`  |
| 3303   | Layout 1             | `6a12f2bbb493`  |
| 3302   | Layout 1             | `6a12f2bbb493`  |
| 3293   | Layout 1             | `6a12f2bbb493`  |
| 3283   | Layout 1             | `6a12f2bbb493`  |
| 3275   | Layout 1             | `6a12f2bbb493`  |
| 3267   | Layout 1             | `6a12f2bbb493`  |
| 3258   | Layout 1             | `6a12f2bbb493`  |
| 3251   | Layout 1             | `6a12f2bbb493`  |
| 3242   | Layout 1             | `6a12f2bbb493`  |
| 3235   | Layout 1             | `6a12f2bbb493`  |
| 3229   | Layout 1             | `6a12f2bbb493`  |
| 3212   | Layout 1             | `6a12f2bbb493`  |
| 3203   | Layout 1             | `6a12f2bbb493`  |
| 3193   | Layout 1             | `6a12f2bbb493`  |
| 3186   | Layout 1             | `6a12f2bbb493`  |
| 3177   | Layout 1             | `6a12f2bbb493`  |
| 3169   | Layout 1             | `6a12f2bbb493`  |
| 3158   | Layout 1             | `6a12f2bbb493`  |
| 3151   | Layout 1             | `6a12f2bbb493`  |
| 3144   | Layout 1             | `6a12f2bbb493`  |
| 3133   | Layout 1             | `6a12f2bbb493`  |
| 3125   | Layout 1             | `6a12f2bbb493`  |
| 3118   | Layout 1             | `6a12f2bbb493`  |
| 3111   | Layout 1             | `6a12f2bbb493`  |
| 3103   | Layout 1             | `6a12f2bbb493`  |
| 3095   | Layout 1             | `6a12f2bbb493`  |
| 3086   | Layout 1             | `6a12f2bbb493`  |
| 3072   | Layout 1             | `6a12f2bbb493`  |
| 3062   | Layout 1             | `6a12f2bbb493`  |
| 3052   | Layout 1             | `6a12f2bbb493`  |
| 3045   | Layout 1             | `6a12f2bbb493`  |
| 3037   | Layout 1             | `6a12f2bbb493`  |
| 3030   | Layout 1             | `6a12f2bbb493`  |
| 3021   | Layout 1             | `6a12f2bbb493`  |
| 3012   | Layout 1             | `6a12f2bbb493`  |
| 3002   | Layout 1             | `6a12f2bbb493`  |
| 2995   | Layout 1             | `6a12f2bbb493`  |
| 2987   | Layout 1             | `6a12f2bbb493`  |
| 2978   | Layout 1             | `6a12f2bbb493`  |
| 2970   | Layout 1             | `6a12f2bbb493`  |
| 2959   | Layout 1             | `6a12f2bbb493`  |
| 2951   | Layout 1             | `6a12f2bbb493`  |
| 2942   | Layout 1             | `6a12f2bbb493`  |
| 2935   | Layout 1             | `6a12f2bbb493`  |
| 2932   | Layout 1             | `6a12f2bbb493`  |
| 2923   | Layout 1             | `6a12f2bbb493`  |
| 2919   | Layout 1             | `6a12f2bbb493`  |
| 2907   | Layout 1             | `6a12f2bbb493`  |
| 2900   | Layout 1             | `6a12f2bbb493`  |
| 2891   | Layout 1             | `6a12f2bbb493`  |
| 2882   | Layout 1             | `6a12f2bbb493`  |
| 2872   | Layout 1             | `6a12f2bbb493`  |
| 2863   | Layout 1             | `6a12f2bbb493`  |
| 2855   | Layout 1             | `6a12f2bbb493`  |
| 2849   | Layout 1             | `6a12f2bbb493`  |
| 2844   | Layout 1             | `6a12f2bbb493`  |
| 2834   | Layout 1             | `6a12f2bbb493`  |
| 2825   | Layout 1             | `6a12f2bbb493`  |
| 2819   | Layout 1             | `6a12f2bbb493`  |
| 2811   | Layout 1             | `6a12f2bbb493`  |
| 2803   | Layout 1             | `6a12f2bbb493`  |
| 2794   | Layout 1             | `6a12f2bbb493`  |
| 2783   | Layout 1             | `6a12f2bbb493`  |
| 2774   | Layout 1             | `6a12f2bbb493`  |
| 2765   | Layout 1             | `6a12f2bbb493`  |
| 2756   | Layout 1             | `6a12f2bbb493`  |
| 2750   | Layout 1             | `6a12f2bbb493`  |
| 2743   | Layout 1             | `6a12f2bbb493`  |
| 2736   | Layout 1             | `6a12f2bbb493`  |
| 2726   | Layout 1             | `6a12f2bbb493`  |
| 2717   | Layout 1             | `6a12f2bbb493`  |
| 2709   | Layout 1             | `6a12f2bbb493`  |
| 2703   | Layout 1             | `6a12f2bbb493`  |
| 2695   | Layout 1             | `6a12f2bbb493`  |
| 2684   | Layout 1             | `6a12f2bbb493`  |
| 2672   | Layout 1             | `6a12f2bbb493`  |
| 2665   | Layout 1             | `6a12f2bbb493`  |
| 2657   | Layout 1             | `6a12f2bbb493`  |
| 2649   | Layout 1             | `6a12f2bbb493`  |
| 2644   | Layout 1             | `6a12f2bbb493`  |
| 2637   | Layout 1             | `6a12f2bbb493`  |
| 2629   | Layout 1             | `6a12f2bbb493`  |
| 2619   | Layout 1             | `6a12f2bbb493`  |
| 2612   | Layout 1             | `6a12f2bbb493`  |
| 2606   | Layout 1             | `6a12f2bbb493`  |
| 2602   | Layout 1             | `6a12f2bbb493`  |
| 2601   | Layout 1             | `6a12f2bbb493`  |
| 2592   | Layout 1             | `6a12f2bbb493`  |
| 2583   | Layout 1             | `6a12f2bbb493`  |
| 2575   | Layout 1             | `6a12f2bbb493`  |
| 2567   | Layout 1             | `6a12f2bbb493`  |
| 2560   | Layout 1             | `6a12f2bbb493`  |
| 2553   | Layout 1             | `6a12f2bbb493`  |
| 2545   | Layout 1             | `6a12f2bbb493`  |
| 2538   | Layout 1             | `6a12f2bbb493`  |
| 2529   | Layout 1             | `6a12f2bbb493`  |
| 2519   | Layout 1             | `6a12f2bbb493`  |
| 2513   | Layout 1             | `6a12f2bbb493`  |
| 2510   | Layout 1             | `6a12f2bbb493`  |
| 2507   | Layout 1             | `6a12f2bbb493`  |
| 2503   | Layout 1             | `6a12f2bbb493`  |
| 2498   | Layout 1             | `6a12f2bbb493`  |
| 2492   | Layout 1             | `6a12f2bbb493`  |
| 2487   | Layout 1             | `6a12f2bbb493`  |
| 2480   | Layout 1             | `6a12f2bbb493`  |
| 2474   | Layout 1             | `6a12f2bbb493`  |
| 2468   | Layout 1             | `6a12f2bbb493`  |
| 2460   | Layout 1             | `6a12f2bbb493`  |
| 2453   | Layout 1             | `6a12f2bbb493`  |
| 2444   | Layout 1             | `6a12f2bbb493`  |
| 2438   | Layout 1             | `6a12f2bbb493`  |
| 2434   | Layout 1             | `6a12f2bbb493`  |
| 2429   | Layout 1             | `6a12f2bbb493`  |
| 2421   | Layout 1             | `6a12f2bbb493`  |
| 2414   | Layout 1             | `6a12f2bbb493`  |
| 2407   | Layout 1             | `6a12f2bbb493`  |
| 2401   | Layout 1             | `6a12f2bbb493`  |
| 2397   | Layout 1             | `6a12f2bbb493`  |
| 2393   | Layout 1             | `6a12f2bbb493`  |
| 2384   | Layout 1             | `6a12f2bbb493`  |
| 2378   | Layout 1             | `6a12f2bbb493`  |
| 2372   | Layout 1             | `6a12f2bbb493`  |
| 2358   | Layout 1             | `6a12f2bbb493`  |
| 2352   | Layout 1             | `6a12f2bbb493`  |
| 2347   | Layout 1             | `6a12f2bbb493`  |
| 2343   | Layout 1             | `6a12f2bbb493`  |
| 2335   | Layout 1             | `6a12f2bbb493`  |
| 2327   | Layout 1             | `6a12f2bbb493`  |
| 2324   | Layout 1             | `6a12f2bbb493`  |
| 2319   | Layout 1             | `6a12f2bbb493`  |
| 2313   | Layout 1             | `6a12f2bbb493`  |
| 2308   | Layout 1             | `6a12f2bbb493`  |
| 2302   | Layout 1             | `6a12f2bbb493`  |
| 2295   | Layout 1             | `6a12f2bbb493`  |
| 2290   | Layout 1             | `6a12f2bbb493`  |
| 2284   | Layout 1             | `6a12f2bbb493`  |
| 2276   | Layout 1             | `6a12f2bbb493`  |
| 2269   | Layout 1             | `6a12f2bbb493`  |
| 2259   | Layout 1             | `6a12f2bbb493`  |
| 2250   | Layout 1             | `6a12f2bbb493`  |
| 2243   | Layout 1             | `6a12f2bbb493`  |
| 2235   | Layout 1             | `6a12f2bbb493`  |
| 2229   | Layout 1             | `6a12f2bbb493`  |
| 2224   | Layout 1             | `6a12f2bbb493`  |
| 2218   | Layout 1             | `6a12f2bbb493`  |
| 2215   | Layout 1             | `6a12f2bbb493`  |
| 2207   | Layout 1             | `6a12f2bbb493`  |
| 2203   | Layout 1             | `6a12f2bbb493`  |
| 2196   | Layout 1             | `6a12f2bbb493`  |
| 2192   | Layout 1             | `6a12f2bbb493`  |
| 2189   | Layout 1             | `6a12f2bbb493`  |
| 2183   | Layout 1             | `6a12f2bbb493`  |
| 2179   | Layout 1             | `6a12f2bbb493`  |
| 2171   | Layout 1             | `6a12f2bbb493`  |
| 2163   | Layout 1             | `6a12f2bbb493`  |
| 2156   | Layout 1             | `6a12f2bbb493`  |
| 2151   | Layout 1             | `6a12f2bbb493`  |
| 2147   | Layout 1             | `6a12f2bbb493`  |
| 2142   | Layout 1             | `6a12f2bbb493`  |
| 2138   | Layout 1             | `6a12f2bbb493`  |
| 2134   | Layout 1             | `6a12f2bbb493`  |
| 2130   | Layout 1             | `6a12f2bbb493`  |
| 2122   | Layout 1             | `6a12f2bbb493`  |
| 2107   | Layout 1             | `6a12f2bbb493`  |
| 2098   | Layout 1             | `6a12f2bbb493`  |
| 2089   | Layout 1             | `6a12f2bbb493`  |
| 2081   | Layout 1             | `6a12f2bbb493`  |
| 2073   | Layout 1             | `6a12f2bbb493`  |
| 2067   | Layout 1             | `6a12f2bbb493`  |
| 2063   | Layout 1             | `6a12f2bbb493`  |
| 2059   | Layout 1             | `6a12f2bbb493`  |
| 2052   | Layout 1             | `6a12f2bbb493`  |
| 2044   | Layout 1             | `6a12f2bbb493`  |
| 2039   | Layout 1             | `6a12f2bbb493`  |
| 2032   | Layout 1             | `6a12f2bbb493`  |
| 2025   | Layout 1             | `6a12f2bbb493`  |
| 2011   | Layout 1             | `6a12f2bbb493`  |
| 2005   | Layout 1             | `6a12f2bbb493`  |
| 2000   | Layout 1             | `6a12f2bbb493`  |
| 1996   | Layout 1             | `6a12f2bbb493`  |
| 1991   | Layout 1             | `6a12f2bbb493`  |
| 1985   | Layout 1             | `6a12f2bbb493`  |
| 1980   | Layout 1             | `6a12f2bbb493`  |
| 1969   | Layout 1             | `6a12f2bbb493`  |
| 1964   | Layout 1             | `6a12f2bbb493`  |
| 1958   | Layout 1             | `6a12f2bbb493`  |
| 1950   | Layout 1             | `6a12f2bbb493`  |
| 1945   | Layout 1             | `6a12f2bbb493`  |
| 1937   | Layout 1             | `6a12f2bbb493`  |
| 1933   | Layout 1             | `6a12f2bbb493`  |
| 1927   | Layout 1             | `6a12f2bbb493`  |
| 1921   | Layout 1             | `6a12f2bbb493`  |
| 1914   | Layout 1             | `6a12f2bbb493`  |
| 1908   | Layout 1             | `6a12f2bbb493`  |
| 1897   | Layout 1             | `6a12f2bbb493`  |
| 1892   | Layout 1             | `6a12f2bbb493`  |
| 1886   | Layout 1             | `6a12f2bbb493`  |
| 1881   | Layout 1             | `6a12f2bbb493`  |
| 1871   | Layout 1             | `6a12f2bbb493`  |
| 1866   | Layout 1             | `6a12f2bbb493`  |
| 1862   | Layout 1             | `6a12f2bbb493`  |
| 1854   | Layout 1             | `6a12f2bbb493`  |
| 1846   | Layout 1             | `6a12f2bbb493`  |
| 1838   | Layout 1             | `6a12f2bbb493`  |
| 1832   | Layout 1             | `6a12f2bbb493`  |
| 1826   | Layout 1             | `6a12f2bbb493`  |
| 1822   | Layout 1             | `6a12f2bbb493`  |
| 1818   | Layout 1             | `6a12f2bbb493`  |
| 1804   | Layout 1             | `6a12f2bbb493`  |
| 1794   | Layout 1             | `6a12f2bbb493`  |
| 1790   | Layout 1             | `6a12f2bbb493`  |
| 1784   | Layout 1             | `6a12f2bbb493`  |
| 1774   | Layout 1             | `6a12f2bbb493`  |
| 1771   | Layout 1             | `6a12f2bbb493`  |
| 1762   | Layout 1             | `6a12f2bbb493`  |
| 1759   | Layout 1             | `6a12f2bbb493`  |
| 1754   | Layout 1             | `6a12f2bbb493`  |
| 1749   | Layout 1             | `6a12f2bbb493`  |
| 1743   | Layout 1             | `6a12f2bbb493`  |
| 1737   | Layout 1             | `6a12f2bbb493`  |
| 1731   | Layout 1             | `6a12f2bbb493`  |
| 1725   | Layout 1             | `6a12f2bbb493`  |
| 1717   | Layout 1             | `6a12f2bbb493`  |
| 1710   | Layout 1             | `6a12f2bbb493`  |
| 1704   | Layout 1             | `6a12f2bbb493`  |
| 1698   | Layout 1             | `6a12f2bbb493`  |
| 1690   | Layout 1             | `6a12f2bbb493`  |
| 1685   | Layout 1             | `6a12f2bbb493`  |
| 1680   | Layout 1             | `6a12f2bbb493`  |
| 1674   | Layout 1             | `6a12f2bbb493`  |
| 1668   | Layout 1             | `6a12f2bbb493`  |
| 1659   | Layout 1             | `6a12f2bbb493`  |
| 1649   | Layout 1             | `6a12f2bbb493`  |
| 1642   | Layout 1             | `6a12f2bbb493`  |
| 1636   | Layout 1             | `6a12f2bbb493`  |
| 1628   | Layout 1             | `6a12f2bbb493`  |
| 1622   | Layout 1             | `6a12f2bbb493`  |
| 1614   | Layout 1             | `6a12f2bbb493`  |
| 1608   | Layout 1             | `6a12f2bbb493`  |
| 1602   | Layout 1             | `6a12f2bbb493`  |
| 1598   | Layout 1             | `6a12f2bbb493`  |
| 1594   | Layout 1             | `6a12f2bbb493`  |
| 1590   | Layout 1             | `6a12f2bbb493`  |
| 1587   | Layout 1             | `6a12f2bbb493`  |
| 1584   | Layout 1             | `6a12f2bbb493`  |
| 1579   | Layout 1             | `6a12f2bbb493`  |
| 1572   | Layout 1             | `6a12f2bbb493`  |
| 1565   | Layout 1             | `6a12f2bbb493`  |
| 1559   | Layout 1             | `6a12f2bbb493`  |
| 1554   | Layout 1             | `6a12f2bbb493`  |
| 1547   | Layout 1             | `6a12f2bbb493`  |
| 1537   | Layout 1             | `6a12f2bbb493`  |
| 1529   | Layout 1             | `6a12f2bbb493`  |
| 1524   | Layout 1             | `6a12f2bbb493`  |
| 1519   | Layout 1             | `6a12f2bbb493`  |
| 1509   | Layout 1             | `6a12f2bbb493`  |
| 1506   | Layout 1             | `6a12f2bbb493`  |
| 1504   | Layout 1             | `6a12f2bbb493`  |
| 1500   | Layout 1             | `6a12f2bbb493`  |
| 1493   | Layout 1             | `6a12f2bbb493`  |
| 1489   | Layout 1             | `6a12f2bbb493`  |
| 1485   | Layout 1             | `6a12f2bbb493`  |
| 1481   | Layout 1             | `6a12f2bbb493`  |
| 1474   | Layout 1             | `6a12f2bbb493`  |
| 1466   | Layout 1             | `6a12f2bbb493`  |
| 1462   | Layout 1             | `6a12f2bbb493`  |
| 1459   | Layout 1             | `6a12f2bbb493`  |
| 1453   | Layout 1             | `6a12f2bbb493`  |
| 1450   | Layout 1             | `6a12f2bbb493`  |
| 1445   | Layout 1             | `6a12f2bbb493`  |
| 1439   | Layout 1             | `6a12f2bbb493`  |
| 1433   | Layout 1             | `6a12f2bbb493`  |
| 1430   | Layout 1             | `6a12f2bbb493`  |
| 1426   | Layout 1             | `6a12f2bbb493`  |
| 1421   | Layout 1             | `6a12f2bbb493`  |
| 1417   | Layout 1             | `6a12f2bbb493`  |
| 1416   | Layout 1             | `6a12f2bbb493`  |
| 1409   | Layout 1             | `6a12f2bbb493`  |
| 1405   | Layout 1             | `6a12f2bbb493`  |
| 1401   | Layout 1             | `6a12f2bbb493`  |
| 1396   | Layout 1             | `6a12f2bbb493`  |
| 1391   | Layout 1             | `6a12f2bbb493`  |
| 1390   | Layout 1             | `6a12f2bbb493`  |
| 1386   | Layout 1             | `6a12f2bbb493`  |
| 1381   | Layout 1             | `6a12f2bbb493`  |
| 1379   | Layout 1             | `6a12f2bbb493`  |
| 1372   | Layout 1             | `6a12f2bbb493`  |
| 1366   | Layout 1             | `6a12f2bbb493`  |
| 1364   | Layout 1             | `6a12f2bbb493`  |
| 1363   | Layout 1             | `6a12f2bbb493`  |
| 1360   | Layout 1             | `6a12f2bbb493`  |
| 1358   | Layout 1             | `6a12f2bbb493`  |
| 1355   | Layout 1             | `6a12f2bbb493`  |
| 1351   | Layout 1             | `6a12f2bbb493`  |
| 1348   | Layout 1             | `6a12f2bbb493`  |
| 1346   | Layout 1             | `6a12f2bbb493`  |
| 1341   | No documented layout | `6a12f2bbb493`  |
| 1340   | No documented layout | `6a12f2bbb493`  |
| 1338   | No documented layout | `6a12f2bbb493`  |
| 1335   | No documented layout | `6a12f2bbb493`  |
| 1333   | No documented layout | `6a12f2bbb493`  |
| 1329   | No documented layout | `6a12f2bbb493`  |
| 1327   | No documented layout | `6a12f2bbb493`  |
| 1324   | No documented layout | `6a12f2bbb493`  |
| 1321   | No documented layout | `6a12f2bbb493`  |
| 1319   | No documented layout | `6a12f2bbb493`  |
| 1318   | No documented layout | `6a12f2bbb493`  |
| 1316   | No documented layout | `6a12f2bbb493`  |
| 1313   | No documented layout | `6a12f2bbb493`  |
| 1311   | No documented layout | `6a12f2bbb493`  |
| 1309   | No documented layout | `6a12f2bbb493`  |
| 1304   | No documented layout | `6a12f2bbb493`  |
| 1292   | No documented layout | `6a12f2bbb493`  |
| 1286   | No documented layout | `6a12f2bbb493`  |
| 1280   | No documented layout | `6a12f2bbb493`  |
| 1276   | No documented layout | `6a12f2bbb493`  |
| 1267   | No file              | `6a12f2bbb493`  |
| 1261   | No file              | `6a12f2bbb493`  |
| 1256   | No documented layout | `6a12f2bbb493`  |
| 1250   | No file              | `6a12f2bbb493`  |
| 1246   | No file              | `6a12f2bbb493`  |
| 1239   | No file              | `6a12f2bbb493`  |
| 1230   | No file              | `6a12f2bbb493`  |
| 1226   | No file              | `6a12f2bbb493`  |
| 1220   | No file              | `6a12f2bbb493`  |
| 1217   | No file              | `6a12f2bbb493`  |
| 1211   | No file              | `6a12f2bbb493`  |
| 1210   | No file              | `6a12f2bbb493`  |
| 1208   | No file              | `6a12f2bbb493`  |
| 1203   | No file              | `6a12f2bbb493`  |
| 1197   | No file              | `6a12f2bbb493`  |
| 1194   | No file              | `6a12f2bbb493`  |
| 1192   | No file              | `6a12f2bbb493`  |
| 1187   | No file              | `6a12f2bbb493`  |
| 1183   | No file              | `6a12f2bbb493`  |
| 1177   | No file              | `6a12f2bbb493`  |
| 1173   | No file              | `6a12f2bbb493`  |
| 1167   | No file              | `6a12f2bbb493`  |
| 1164   | No file              | `6a12f2bbb493`  |
| 1156   | No file              | `6a12f2bbb493`  |
| 1149   | No file              | `6a12f2bbb493`  |
| 1144   | No file              | `6a12f2bbb493`  |
| 1137   | No file              | `6a12f2bbb493`  |
| 1132   | No file              | `6a12f2bbb493`  |
| 1127   | No file              | `6a12f2bbb493`  |
| 1122   | No file              | `6a12f2bbb493`  |
| 1118   | No file              | `6a12f2bbb493`  |
| 1114   | No file              | `6a12f2bbb493`  |
| 1109   | No file              | `6a12f2bbb493`  |
| 1102   | No file              | `6a12f2bbb493`  |
| 1096   | No file              | `6a12f2bbb493`  |
| 1088   | No file              | `6a12f2bbb493`  |
| 1081   | No file              | `6a12f2bbb493`  |
| 1076   | No file              | `6a12f2bbb493`  |
| 1069   | No file              | `6a12f2bbb493`  |
| 1064   | No file              | `6a12f2bbb493`  |
| 1058   | No file              | `6a12f2bbb493`  |
| 1051   | No file              | `6a12f2bbb493`  |
| 1044   | No file              | `6a12f2bbb493`  |
| 1036   | No file              | `6a12f2bbb493`  |
| 1026   | No file              | `6a12f2bbb493`  |
| 1016   | No file              | `6a12f2bbb493`  |
| 1009   | No file              | `6a12f2bbb493`  |
| 1005   | No file              | `6a12f2bbb493`  |
| 1000   | No file              | `6a12f2bbb493`  |
| 998    | No file              | `6a12f2bbb493`  |
| 990    | No file              | `6a12f2bbb493`  |
| 979    | No file              | `6a12f2bbb493`  |
| 972    | No file              | `6a12f2bbb493`  |
| 963    | No file              | `6a12f2bbb493`  |
| 955    | No file              | `6a12f2bbb493`  |
| 946    | No file              | `6a12f2bbb493`  |
| 938    | No file              | `6a12f2bbb493`  |
| 927    | No file              | `6a12f2bbb493`  |
| 911    | No file              | `6a12f2bbb493`  |
| 904    | No file              | `6a12f2bbb493`  |
| 899    | No file              | `6a12f2bbb493`  |
| 894    | No file              | `6a12f2bbb493`  |
| 885    | No file              | `6a12f2bbb493`  |
| 879    | No file              | `6a12f2bbb493`  |
| 872    | No file              | `6a12f2bbb493`  |
| 864    | No file              | `6a12f2bbb493`  |
| 855    | No file              | `6a12f2bbb493`  |
| 853    | No file              | `6a12f2bbb493`  |
| 845    | No file              | `6a12f2bbb493`  |
| 837    | No file              | `6a12f2bbb493`  |
| 829    | No file              | `6a12f2bbb493`  |
| 822    | No file              | `6a12f2bbb493`  |
| 814    | No file              | `6a12f2bbb493`  |
| 805    | No file              | `6a12f2bbb493`  |
| 794    | No file              | `6a12f2bbb493`  |
| 787    | No file              | `6a12f2bbb493`  |
| 780    | No file              | `6a12f2bbb493`  |
| 771    | No file              | `6a12f2bbb493`  |
| 760    | No file              | `6a12f2bbb493`  |
| 748    | No file              | `6a12f2bbb493`  |
| 741    | No file              | `6a12f2bbb493`  |
| 736    | No file              | `6a12f2bbb493`  |
| 731    | No file              | `6a12f2bbb493`  |
| 723    | No file              | `6a12f2bbb493`  |
| 711    | No file              | `6a12f2bbb493`  |
| 707    | No file              | `6a12f2bbb493`  |
| 697    | No file              | `6a12f2bbb493`  |
| 689    | No file              | `6a12f2bbb493`  |
| 683    | No file              | `6a12f2bbb493`  |
| 678    | No file              | `6a12f2bbb493`  |
| 670    | No file              | `6a12f2bbb493`  |
| 661    | No file              | `6a12f2bbb493`  |
| 656    | No file              | `6a12f2bbb493`  |
| 652    | No file              | `6a12f2bbb493`  |
| 643    | No file              | `6a12f2bbb493`  |
| 637    | No file              | `6a12f2bbb493`  |
| 630    | No file              | `6a12f2bbb493`  |
| 627    | No file              | `6a12f2bbb493`  |
| 621    | No file              | `6a12f2bbb493`  |
| 617    | No file              | `6a12f2bbb493`  |
| 615    | No file              | `6a12f2bbb493`  |
| 606    | No file              | `6a12f2bbb493`  |
| 599    | No file              | `6a12f2bbb493`  |
| 592    | No file              | `6a12f2bbb493`  |
| 586    | No file              | `6a12f2bbb493`  |
| 577    | No file              | `6a12f2bbb493`  |
| 569    | No file              | `6a12f2bbb493`  |
| 561    | No file              | `6a12f2bbb493`  |
| 554    | No file              | `6a12f2bbb493`  |
| 542    | No file              | `6a12f2bbb493`  |
| 532    | No file              | `6a12f2bbb493`  |
| 531    | No file              | `6a12f2bbb493`  |
| 526    | No file              | `6a12f2bbb493`  |
| 521    | No file              | `6a12f2bbb493`  |
| 517    | No file              | `6a12f2bbb493`  |
| 510    | No file              | `6a12f2bbb493`  |
| 508    | No file              | `6a12f2bbb493`  |
| 504    | No file              | `6a12f2bbb493`  |
| 497    | No file              | `6a12f2bbb493`  |
| 491    | No file              | `6a12f2bbb493`  |
| 485    | No file              | `6a12f2bbb493`  |
| 478    | No file              | `6a12f2bbb493`  |
| 472    | No file              | `6a12f2bbb493`  |
| 466    | No file              | `6a12f2bbb493`  |
| 457    | No file              | `6a12f2bbb493`  |
| 452    | No file              | `6a12f2bbb493`  |
| 449    | No file              | `6a12f2bbb493`  |
| 435    | No file              | `6a12f2bbb493`  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                  |
| ------------------------------- | -------- | ----------------------------------------------------- |
| `servantinteractionoffset.dbss` | Optional | Index: character ID to the record's offset and size   |
| `servantbuff.dbss`              | Optional | The interactions `buff_keys` point at                 |
| `characterstaticoffset.dbss`    | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |
| `languagedata_en.loc`           | Optional | Servant names (LOC type 6, `str_id1` = `character_id`) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | 311 on client 3474                     |
| `+0x04` | Record[count] | records | Back to back, variable size, up to EOF |

### Record (variable: 20 bytes + buff keys)

| Offset  | Type             | Field            | Notes |
| ------- | ---------------- | ---------------- | ----- |
| `+0x00` | u16              | character_id     | Servant character, as in `servant.bss` |
| `+0x02` | u16              | character_id_dup | Equals `character_id` on every record |
| `+0x04` | u64              | cool_time        | Milliseconds ([Notes](#notes)); 1,200,000 (20 minutes) on every record (client 3474) |
| `+0x0C` | u64              | buff_count       | 3 on every record (client 3474) |
| `+0x14` | u32[buff_count]  | buff_keys        | `servantbuff.dbss` keys; 1, 2, 3 on every record (client 3474) |

### `servantinteractionoffset.dbss`

| Offset  | Type              | Field   | Notes                          |
| ------- | ----------------- | ------- | ------------------------------ |
| `+0x00` | u32               | count   | Equals the main file's count   |
| `+0x04` | Offset Row[count] | entries | `count` entries of 10 bytes; not in file order |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                        |
| ------- | ---- | ------------ | ------------------------------------------------------------ |
| `+0x00` | u16  | character_id | The record's `character_id`                                  |
| `+0x02` | u32  | offset       | Where the record's `character_id_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size         | Record size minus 2                                          |

## Layout 1

Client 1784 stores the buff keys as u16, as `servantbuff.dbss` does its keys
there; it has 255 records.

### Record (variable: 20 bytes + buff keys)

| Offset  | Type             | Field            | Notes |
| ------- | ---------------- | ---------------- | ----- |
| `+0x00` | u16              | character_id     | |
| `+0x02` | u16              | character_id_dup | |
| `+0x04` | u64              | cool_time        | |
| `+0x0C` | u64              | buff_count       | |
| `+0x14` | u16[buff_count]  | buff_keys        | |

## Field Names

The names follow the `ServantInteraction_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (`CharacterKey`, `BuffList`,
`CoolTime`): all 255 records of client 1784 and the 258 client 3474 records
in the sheet match in every column. The 2016
`gc::ServantInteractionStaticStatus` holds `_key`, `_buffKeyList` and
`_coolTime`; the file stores the cooldown before the list.

## Notes

- `cool_time` is in milliseconds: the interaction panel
  (`panel_interaction.luac`) shows the remaining Horse Communion cooldown
  from `vehicleWrapper:getSympatheticCoolTime()` through
  `convertStringFromMillisecondtime`.
- On client 3474, 20 records name a character that is not in
  [servant.bss](servant_bss.md): 9033, 9884 to 9886, 9900, 9986, 31518,
  31534, 31535, 31537, 31538, 31540 to 31543, 31546, 31547, 31561, 31593
  and 35129. All but 9033, 9986 and 35129 have no `characterstatic.dbss`
  row either.
