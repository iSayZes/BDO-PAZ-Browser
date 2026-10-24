# `sequencedatatable.bss` Format

## Purpose

Where and when a cutscene starts on its own, and what it runs. Each row
names one cutscene file (`CS_Tutorial_06_EternalWinter_0000.pas`), the
region it belongs to, a start condition script (`checkposition(x, y, z,
radius)`, quest state checks) and two scripts the client runs when the
cutscene starts and ends (`acceptquest`, `completequestcondition`,
`setPosition`). The file holds the `CutsceneBeginningLocationInfo` sheet
plus two columns that sheet did not have yet. It is a PABR table of
27-byte rows whose text sits in the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes  | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ------ | ------- | --------- |
| 2      | 2011 and later | 3483    | `sequencedatatable.bss` | 63,181 | 185 Row | 27        |
| 1      | 1927 to 2005   | 2005    | `sequencedatatable.bss` | 38,651 | 76 Row  | 26        |

| Layout | File                    | Known            | Unknown      |
| ------ | ----------------------- | ---------------- | ------------ |
| 2      | `sequencedatatable.bss` | 62,256 B (98.5%) | 925 B (1.5%) |
| 1      | `sequencedatatable.bss` | 38,347 B (99.2%) | 304 B (0.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `b79fda0e10ce`  |
| 3482   | Layout 2 | `b79fda0e10ce`  |
| 3474   | Layout 2 | `b79fda0e10ce`  |
| 3473   | Layout 2 | `b79fda0e10ce`  |
| 3464   | Layout 2 | `b79fda0e10ce`  |
| 3458   | Layout 2 | `b79fda0e10ce`  |
| 3454   | Layout 2 | `b79fda0e10ce`  |
| 3444   | Layout 2 | `b79fda0e10ce`  |
| 3435   | Layout 2 | `b79fda0e10ce`  |
| 3426   | Layout 2 | `b79fda0e10ce`  |
| 3418   | Layout 2 | `b79fda0e10ce`  |
| 3412   | Layout 2 | `b79fda0e10ce`  |
| 3402   | Layout 2 | `b79fda0e10ce`  |
| 3396   | Layout 2 | `b79fda0e10ce`  |
| 3387   | Layout 2 | `b79fda0e10ce`  |
| 3381   | Layout 2 | `b79fda0e10ce`  |
| 3373   | Layout 2 | `b79fda0e10ce`  |
| 3364   | Layout 2 | `b79fda0e10ce`  |
| 3356   | Layout 2 | `b79fda0e10ce`  |
| 3349   | Layout 2 | `b79fda0e10ce`  |
| 3342   | Layout 2 | `b79fda0e10ce`  |
| 3335   | Layout 2 | `b79fda0e10ce`  |
| 3326   | Layout 2 | `b79fda0e10ce`  |
| 3321   | Layout 2 | `b79fda0e10ce`  |
| 3314   | Layout 2 | `b79fda0e10ce`  |
| 3303   | Layout 2 | `b79fda0e10ce`  |
| 3302   | Layout 2 | `b79fda0e10ce`  |
| 3293   | Layout 2 | `b79fda0e10ce`  |
| 3283   | Layout 2 | `b79fda0e10ce`  |
| 3275   | Layout 2 | `b79fda0e10ce`  |
| 3267   | Layout 2 | `b79fda0e10ce`  |
| 3258   | Layout 2 | `b79fda0e10ce`  |
| 3251   | Layout 2 | `b79fda0e10ce`  |
| 3242   | Layout 2 | `b79fda0e10ce`  |
| 3235   | Layout 2 | `b79fda0e10ce`  |
| 3229   | Layout 2 | `b79fda0e10ce`  |
| 3212   | Layout 2 | `b79fda0e10ce`  |
| 3203   | Layout 2 | `b79fda0e10ce`  |
| 3193   | Layout 2 | `b79fda0e10ce`  |
| 3186   | Layout 2 | `b79fda0e10ce`  |
| 3177   | Layout 2 | `b79fda0e10ce`  |
| 3169   | Layout 2 | `b79fda0e10ce`  |
| 3158   | Layout 2 | `b79fda0e10ce`  |
| 3151   | Layout 2 | `b79fda0e10ce`  |
| 3144   | Layout 2 | `b79fda0e10ce`  |
| 3133   | Layout 2 | `b79fda0e10ce`  |
| 3125   | Layout 2 | `b79fda0e10ce`  |
| 3118   | Layout 2 | `b79fda0e10ce`  |
| 3111   | Layout 2 | `b79fda0e10ce`  |
| 3103   | Layout 2 | `b79fda0e10ce`  |
| 3095   | Layout 2 | `b79fda0e10ce`  |
| 3086   | Layout 2 | `b79fda0e10ce`  |
| 3072   | Layout 2 | `b79fda0e10ce`  |
| 3062   | Layout 2 | `b79fda0e10ce`  |
| 3052   | Layout 2 | `b79fda0e10ce`  |
| 3045   | Layout 2 | `b79fda0e10ce`  |
| 3037   | Layout 2 | `b79fda0e10ce`  |
| 3030   | Layout 2 | `b79fda0e10ce`  |
| 3021   | Layout 2 | `b79fda0e10ce`  |
| 3012   | Layout 2 | `b79fda0e10ce`  |
| 3002   | Layout 2 | `b79fda0e10ce`  |
| 2995   | Layout 2 | `b79fda0e10ce`  |
| 2987   | Layout 2 | `b79fda0e10ce`  |
| 2978   | Layout 2 | `b79fda0e10ce`  |
| 2970   | Layout 2 | `b79fda0e10ce`  |
| 2959   | Layout 2 | `b79fda0e10ce`  |
| 2951   | Layout 2 | `b79fda0e10ce`  |
| 2942   | Layout 2 | `b79fda0e10ce`  |
| 2935   | Layout 2 | `b79fda0e10ce`  |
| 2932   | Layout 2 | `b79fda0e10ce`  |
| 2923   | Layout 2 | `b79fda0e10ce`  |
| 2919   | Layout 2 | `b79fda0e10ce`  |
| 2907   | Layout 2 | `b79fda0e10ce`  |
| 2900   | Layout 2 | `b79fda0e10ce`  |
| 2891   | Layout 2 | `b79fda0e10ce`  |
| 2882   | Layout 2 | `b79fda0e10ce`  |
| 2872   | Layout 2 | `b79fda0e10ce`  |
| 2863   | Layout 2 | `b79fda0e10ce`  |
| 2855   | Layout 2 | `b79fda0e10ce`  |
| 2849   | Layout 2 | `b79fda0e10ce`  |
| 2844   | Layout 2 | `b79fda0e10ce`  |
| 2834   | Layout 2 | `b79fda0e10ce`  |
| 2825   | Layout 2 | `b79fda0e10ce`  |
| 2819   | Layout 2 | `b79fda0e10ce`  |
| 2811   | Layout 2 | `b79fda0e10ce`  |
| 2803   | Layout 2 | `b79fda0e10ce`  |
| 2794   | Layout 2 | `b79fda0e10ce`  |
| 2783   | Layout 2 | `b79fda0e10ce`  |
| 2774   | Layout 2 | `b79fda0e10ce`  |
| 2765   | Layout 2 | `b79fda0e10ce`  |
| 2756   | Layout 2 | `b79fda0e10ce`  |
| 2750   | Layout 2 | `b79fda0e10ce`  |
| 2743   | Layout 2 | `b79fda0e10ce`  |
| 2736   | Layout 2 | `b79fda0e10ce`  |
| 2726   | Layout 2 | `b79fda0e10ce`  |
| 2717   | Layout 2 | `b79fda0e10ce`  |
| 2709   | Layout 2 | `b79fda0e10ce`  |
| 2703   | Layout 2 | `b79fda0e10ce`  |
| 2695   | Layout 2 | `b79fda0e10ce`  |
| 2684   | Layout 2 | `b79fda0e10ce`  |
| 2672   | Layout 2 | `b79fda0e10ce`  |
| 2665   | Layout 2 | `b79fda0e10ce`  |
| 2657   | Layout 2 | `b79fda0e10ce`  |
| 2649   | Layout 2 | `b79fda0e10ce`  |
| 2644   | Layout 2 | `b79fda0e10ce`  |
| 2637   | Layout 2 | `b79fda0e10ce`  |
| 2629   | Layout 2 | `b79fda0e10ce`  |
| 2619   | Layout 2 | `b79fda0e10ce`  |
| 2612   | Layout 2 | `b79fda0e10ce`  |
| 2606   | Layout 2 | `b79fda0e10ce`  |
| 2602   | Layout 2 | `b79fda0e10ce`  |
| 2601   | Layout 2 | `b79fda0e10ce`  |
| 2592   | Layout 2 | `b79fda0e10ce`  |
| 2583   | Layout 2 | `b79fda0e10ce`  |
| 2575   | Layout 2 | `b79fda0e10ce`  |
| 2567   | Layout 2 | `b79fda0e10ce`  |
| 2560   | Layout 2 | `b79fda0e10ce`  |
| 2553   | Layout 2 | `b79fda0e10ce`  |
| 2545   | Layout 2 | `b79fda0e10ce`  |
| 2538   | Layout 2 | `b79fda0e10ce`  |
| 2529   | Layout 2 | `b79fda0e10ce`  |
| 2519   | Layout 2 | `b79fda0e10ce`  |
| 2513   | Layout 2 | `b79fda0e10ce`  |
| 2510   | Layout 2 | `b79fda0e10ce`  |
| 2507   | Layout 2 | `b79fda0e10ce`  |
| 2503   | Layout 2 | `b79fda0e10ce`  |
| 2498   | Layout 2 | `b79fda0e10ce`  |
| 2492   | Layout 2 | `b79fda0e10ce`  |
| 2487   | Layout 2 | `b79fda0e10ce`  |
| 2480   | Layout 2 | `b79fda0e10ce`  |
| 2474   | Layout 2 | `b79fda0e10ce`  |
| 2468   | Layout 2 | `b79fda0e10ce`  |
| 2460   | Layout 2 | `b79fda0e10ce`  |
| 2453   | Layout 2 | `b79fda0e10ce`  |
| 2444   | Layout 2 | `b79fda0e10ce`  |
| 2438   | Layout 2 | `b79fda0e10ce`  |
| 2434   | Layout 2 | `b79fda0e10ce`  |
| 2429   | Layout 2 | `b79fda0e10ce`  |
| 2421   | Layout 2 | `b79fda0e10ce`  |
| 2414   | Layout 2 | `b79fda0e10ce`  |
| 2407   | Layout 2 | `b79fda0e10ce`  |
| 2401   | Layout 2 | `b79fda0e10ce`  |
| 2397   | Layout 2 | `b79fda0e10ce`  |
| 2393   | Layout 2 | `b79fda0e10ce`  |
| 2384   | Layout 2 | `b79fda0e10ce`  |
| 2378   | Layout 2 | `b79fda0e10ce`  |
| 2372   | Layout 2 | `b79fda0e10ce`  |
| 2358   | Layout 2 | `b79fda0e10ce`  |
| 2352   | Layout 2 | `b79fda0e10ce`  |
| 2347   | Layout 2 | `b79fda0e10ce`  |
| 2343   | Layout 2 | `b79fda0e10ce`  |
| 2335   | Layout 2 | `b79fda0e10ce`  |
| 2327   | Layout 2 | `b79fda0e10ce`  |
| 2324   | Layout 2 | `b79fda0e10ce`  |
| 2319   | Layout 2 | `b79fda0e10ce`  |
| 2313   | Layout 2 | `b79fda0e10ce`  |
| 2308   | Layout 2 | `b79fda0e10ce`  |
| 2302   | Layout 2 | `b79fda0e10ce`  |
| 2295   | Layout 2 | `b79fda0e10ce`  |
| 2290   | Layout 2 | `b79fda0e10ce`  |
| 2284   | Layout 2 | `b79fda0e10ce`  |
| 2276   | Layout 2 | `b79fda0e10ce`  |
| 2269   | Layout 2 | `b79fda0e10ce`  |
| 2259   | Layout 2 | `b79fda0e10ce`  |
| 2250   | Layout 2 | `b79fda0e10ce`  |
| 2243   | Layout 2 | `b79fda0e10ce`  |
| 2235   | Layout 2 | `b79fda0e10ce`  |
| 2229   | Layout 2 | `b79fda0e10ce`  |
| 2224   | Layout 2 | `b79fda0e10ce`  |
| 2218   | Layout 2 | `b79fda0e10ce`  |
| 2215   | Layout 2 | `b79fda0e10ce`  |
| 2207   | Layout 2 | `b79fda0e10ce`  |
| 2203   | Layout 2 | `b79fda0e10ce`  |
| 2196   | Layout 2 | `b79fda0e10ce`  |
| 2192   | Layout 2 | `b79fda0e10ce`  |
| 2189   | Layout 2 | `b79fda0e10ce`  |
| 2183   | Layout 2 | `b79fda0e10ce`  |
| 2179   | Layout 2 | `b79fda0e10ce`  |
| 2171   | Layout 2 | `b79fda0e10ce`  |
| 2163   | Layout 2 | `b79fda0e10ce`  |
| 2156   | Layout 2 | `b79fda0e10ce`  |
| 2151   | Layout 2 | `b79fda0e10ce`  |
| 2147   | Layout 2 | `b79fda0e10ce`  |
| 2142   | Layout 2 | `b79fda0e10ce`  |
| 2138   | Layout 2 | `b79fda0e10ce`  |
| 2134   | Layout 2 | `b79fda0e10ce`  |
| 2130   | Layout 2 | `b79fda0e10ce`  |
| 2122   | Layout 2 | `b79fda0e10ce`  |
| 2107   | Layout 2 | `b79fda0e10ce`  |
| 2098   | Layout 2 | `b79fda0e10ce`  |
| 2089   | Layout 2 | `b79fda0e10ce`  |
| 2081   | Layout 2 | `b79fda0e10ce`  |
| 2073   | Layout 2 | `b79fda0e10ce`  |
| 2067   | Layout 2 | `b79fda0e10ce`  |
| 2063   | Layout 2 | `b79fda0e10ce`  |
| 2059   | Layout 2 | `b79fda0e10ce`  |
| 2052   | Layout 2 | `b79fda0e10ce`  |
| 2044   | Layout 2 | `b79fda0e10ce`  |
| 2039   | Layout 2 | `b79fda0e10ce`  |
| 2032   | Layout 2 | `b79fda0e10ce`  |
| 2025   | Layout 2 | `b79fda0e10ce`  |
| 2011   | Layout 2 | `b79fda0e10ce`  |
| 2005   | Layout 1 | `b79fda0e10ce`  |
| 2000   | Layout 1 | `b79fda0e10ce`  |
| 1996   | Layout 1 | `b79fda0e10ce`  |
| 1991   | Layout 1 | `b79fda0e10ce`  |
| 1985   | Layout 1 | `b79fda0e10ce`  |
| 1980   | Layout 1 | `b79fda0e10ce`  |
| 1969   | Layout 1 | `b79fda0e10ce`  |
| 1964   | Layout 1 | `b79fda0e10ce`  |
| 1958   | Layout 1 | `b79fda0e10ce`  |
| 1950   | Layout 1 | `b79fda0e10ce`  |
| 1945   | Layout 1 | `b79fda0e10ce`  |
| 1937   | Layout 1 | `b79fda0e10ce`  |
| 1933   | Layout 1 | `b79fda0e10ce`  |
| 1927   | Layout 1 | `b79fda0e10ce`  |
| 1921   | No file  | `b79fda0e10ce`  |
| 1914   | No file  | `b79fda0e10ce`  |
| 1908   | No file  | `b79fda0e10ce`  |
| 1897   | No file  | `b79fda0e10ce`  |
| 1892   | No file  | `b79fda0e10ce`  |
| 1886   | No file  | `b79fda0e10ce`  |
| 1881   | No file  | `b79fda0e10ce`  |
| 1871   | No file  | `b79fda0e10ce`  |
| 1866   | No file  | `b79fda0e10ce`  |
| 1862   | No file  | `b79fda0e10ce`  |
| 1854   | No file  | `b79fda0e10ce`  |
| 1846   | No file  | `b79fda0e10ce`  |
| 1838   | No file  | `b79fda0e10ce`  |
| 1832   | No file  | `b79fda0e10ce`  |
| 1826   | No file  | `b79fda0e10ce`  |
| 1822   | No file  | `b79fda0e10ce`  |
| 1818   | No file  | `b79fda0e10ce`  |
| 1804   | No file  | `b79fda0e10ce`  |
| 1794   | No file  | `b79fda0e10ce`  |
| 1790   | No file  | `b79fda0e10ce`  |
| 1784   | No file  | `b79fda0e10ce`  |
| 1774   | No file  | `b79fda0e10ce`  |
| 1771   | No file  | `b79fda0e10ce`  |
| 1762   | No file  | `b79fda0e10ce`  |
| 1759   | No file  | `b79fda0e10ce`  |
| 1754   | No file  | `b79fda0e10ce`  |
| 1749   | No file  | `b79fda0e10ce`  |
| 1743   | No file  | `b79fda0e10ce`  |
| 1737   | No file  | `b79fda0e10ce`  |
| 1731   | No file  | `b79fda0e10ce`  |
| 1725   | No file  | `b79fda0e10ce`  |
| 1717   | No file  | `b79fda0e10ce`  |
| 1710   | No file  | `b79fda0e10ce`  |
| 1704   | No file  | `b79fda0e10ce`  |
| 1698   | No file  | `b79fda0e10ce`  |
| 1690   | No file  | `b79fda0e10ce`  |
| 1685   | No file  | `b79fda0e10ce`  |
| 1680   | No file  | `b79fda0e10ce`  |
| 1674   | No file  | `b79fda0e10ce`  |
| 1668   | No file  | `b79fda0e10ce`  |
| 1659   | No file  | `b79fda0e10ce`  |
| 1649   | No file  | `b79fda0e10ce`  |
| 1642   | No file  | `b79fda0e10ce`  |
| 1636   | No file  | `b79fda0e10ce`  |
| 1628   | No file  | `b79fda0e10ce`  |
| 1622   | No file  | `b79fda0e10ce`  |
| 1614   | No file  | `b79fda0e10ce`  |
| 1608   | No file  | `b79fda0e10ce`  |
| 1602   | No file  | `b79fda0e10ce`  |
| 1598   | No file  | `b79fda0e10ce`  |
| 1594   | No file  | `b79fda0e10ce`  |
| 1590   | No file  | `b79fda0e10ce`  |
| 1587   | No file  | `b79fda0e10ce`  |
| 1584   | No file  | `b79fda0e10ce`  |
| 1579   | No file  | `b79fda0e10ce`  |
| 1572   | No file  | `b79fda0e10ce`  |
| 1565   | No file  | `b79fda0e10ce`  |
| 1559   | No file  | `b79fda0e10ce`  |
| 1554   | No file  | `b79fda0e10ce`  |
| 1547   | No file  | `b79fda0e10ce`  |
| 1537   | No file  | `b79fda0e10ce`  |
| 1529   | No file  | `b79fda0e10ce`  |
| 1524   | No file  | `b79fda0e10ce`  |
| 1519   | No file  | `b79fda0e10ce`  |
| 1509   | No file  | `b79fda0e10ce`  |
| 1506   | No file  | `b79fda0e10ce`  |
| 1504   | No file  | `b79fda0e10ce`  |
| 1500   | No file  | `b79fda0e10ce`  |
| 1493   | No file  | `b79fda0e10ce`  |
| 1489   | No file  | `b79fda0e10ce`  |
| 1485   | No file  | `b79fda0e10ce`  |
| 1481   | No file  | `b79fda0e10ce`  |
| 1474   | No file  | `b79fda0e10ce`  |
| 1466   | No file  | `b79fda0e10ce`  |
| 1462   | No file  | `b79fda0e10ce`  |
| 1459   | No file  | `b79fda0e10ce`  |
| 1453   | No file  | `b79fda0e10ce`  |
| 1450   | No file  | `b79fda0e10ce`  |
| 1445   | No file  | `b79fda0e10ce`  |
| 1439   | No file  | `b79fda0e10ce`  |
| 1433   | No file  | `b79fda0e10ce`  |
| 1430   | No file  | `b79fda0e10ce`  |
| 1426   | No file  | `b79fda0e10ce`  |
| 1421   | No file  | `b79fda0e10ce`  |
| 1417   | No file  | `b79fda0e10ce`  |
| 1416   | No file  | `b79fda0e10ce`  |
| 1409   | No file  | `b79fda0e10ce`  |
| 1405   | No file  | `b79fda0e10ce`  |
| 1401   | No file  | `b79fda0e10ce`  |
| 1396   | No file  | `b79fda0e10ce`  |
| 1391   | No file  | `b79fda0e10ce`  |
| 1390   | No file  | `b79fda0e10ce`  |
| 1386   | No file  | `b79fda0e10ce`  |
| 1381   | No file  | `b79fda0e10ce`  |
| 1379   | No file  | `b79fda0e10ce`  |
| 1372   | No file  | `b79fda0e10ce`  |
| 1366   | No file  | `b79fda0e10ce`  |
| 1364   | No file  | `b79fda0e10ce`  |
| 1363   | No file  | `b79fda0e10ce`  |
| 1360   | No file  | `b79fda0e10ce`  |
| 1358   | No file  | `b79fda0e10ce`  |
| 1355   | No file  | `b79fda0e10ce`  |
| 1351   | No file  | `b79fda0e10ce`  |
| 1348   | No file  | `b79fda0e10ce`  |
| 1346   | No file  | `b79fda0e10ce`  |
| 1341   | No file  | `b79fda0e10ce`  |
| 1340   | No file  | `b79fda0e10ce`  |
| 1338   | No file  | `b79fda0e10ce`  |
| 1335   | No file  | `b79fda0e10ce`  |
| 1333   | No file  | `b79fda0e10ce`  |
| 1329   | No file  | `b79fda0e10ce`  |
| 1327   | No file  | `b79fda0e10ce`  |
| 1324   | No file  | `b79fda0e10ce`  |
| 1321   | No file  | `b79fda0e10ce`  |
| 1319   | No file  | `b79fda0e10ce`  |
| 1318   | No file  | `b79fda0e10ce`  |
| 1316   | No file  | `b79fda0e10ce`  |
| 1313   | No file  | `b79fda0e10ce`  |
| 1311   | No file  | `b79fda0e10ce`  |
| 1309   | No file  | `b79fda0e10ce`  |
| 1304   | No file  | `b79fda0e10ce`  |
| 1292   | No file  | `b79fda0e10ce`  |
| 1286   | No file  | `b79fda0e10ce`  |
| 1280   | No file  | `b79fda0e10ce`  |
| 1276   | No file  | `b79fda0e10ce`  |
| 1267   | No file  | `b79fda0e10ce`  |
| 1261   | No file  | `b79fda0e10ce`  |
| 1256   | No file  | `b79fda0e10ce`  |
| 1250   | No file  | `b79fda0e10ce`  |
| 1246   | No file  | `b79fda0e10ce`  |
| 1239   | No file  | `b79fda0e10ce`  |
| 1230   | No file  | `b79fda0e10ce`  |
| 1226   | No file  | `b79fda0e10ce`  |
| 1220   | No file  | `b79fda0e10ce`  |
| 1217   | No file  | `b79fda0e10ce`  |
| 1211   | No file  | `b79fda0e10ce`  |
| 1210   | No file  | `b79fda0e10ce`  |
| 1208   | No file  | `b79fda0e10ce`  |
| 1203   | No file  | `b79fda0e10ce`  |
| 1197   | No file  | `b79fda0e10ce`  |
| 1194   | No file  | `b79fda0e10ce`  |
| 1192   | No file  | `b79fda0e10ce`  |
| 1187   | No file  | `b79fda0e10ce`  |
| 1183   | No file  | `b79fda0e10ce`  |
| 1177   | No file  | `b79fda0e10ce`  |
| 1173   | No file  | `b79fda0e10ce`  |
| 1167   | No file  | `b79fda0e10ce`  |
| 1164   | No file  | `b79fda0e10ce`  |
| 1156   | No file  | `b79fda0e10ce`  |
| 1149   | No file  | `b79fda0e10ce`  |
| 1144   | No file  | `b79fda0e10ce`  |
| 1137   | No file  | `b79fda0e10ce`  |
| 1132   | No file  | `b79fda0e10ce`  |
| 1127   | No file  | `b79fda0e10ce`  |
| 1122   | No file  | `b79fda0e10ce`  |
| 1118   | No file  | `b79fda0e10ce`  |
| 1114   | No file  | `b79fda0e10ce`  |
| 1109   | No file  | `b79fda0e10ce`  |
| 1102   | No file  | `b79fda0e10ce`  |
| 1096   | No file  | `b79fda0e10ce`  |
| 1088   | No file  | `b79fda0e10ce`  |
| 1081   | No file  | `b79fda0e10ce`  |
| 1076   | No file  | `b79fda0e10ce`  |
| 1069   | No file  | `b79fda0e10ce`  |
| 1064   | No file  | `b79fda0e10ce`  |
| 1058   | No file  | `b79fda0e10ce`  |
| 1051   | No file  | `b79fda0e10ce`  |
| 1044   | No file  | `b79fda0e10ce`  |
| 1036   | No file  | `b79fda0e10ce`  |
| 1026   | No file  | `b79fda0e10ce`  |
| 1016   | No file  | `b79fda0e10ce`  |
| 1009   | No file  | `b79fda0e10ce`  |
| 1005   | No file  | `b79fda0e10ce`  |
| 1000   | No file  | `b79fda0e10ce`  |
| 998    | No file  | `b79fda0e10ce`  |
| 990    | No file  | `b79fda0e10ce`  |
| 979    | No file  | `b79fda0e10ce`  |
| 972    | No file  | `b79fda0e10ce`  |
| 963    | No file  | `b79fda0e10ce`  |
| 955    | No file  | `b79fda0e10ce`  |
| 946    | No file  | `b79fda0e10ce`  |
| 938    | No file  | `b79fda0e10ce`  |
| 927    | No file  | `b79fda0e10ce`  |
| 911    | No file  | `b79fda0e10ce`  |
| 904    | No file  | `b79fda0e10ce`  |
| 899    | No file  | `b79fda0e10ce`  |
| 894    | No file  | `b79fda0e10ce`  |
| 885    | No file  | `b79fda0e10ce`  |
| 879    | No file  | `b79fda0e10ce`  |
| 872    | No file  | `b79fda0e10ce`  |
| 864    | No file  | `b79fda0e10ce`  |
| 855    | No file  | `b79fda0e10ce`  |
| 853    | No file  | `b79fda0e10ce`  |
| 845    | No file  | `b79fda0e10ce`  |
| 837    | No file  | `b79fda0e10ce`  |
| 829    | No file  | `b79fda0e10ce`  |
| 822    | No file  | `b79fda0e10ce`  |
| 814    | No file  | `b79fda0e10ce`  |
| 805    | No file  | `b79fda0e10ce`  |
| 794    | No file  | `b79fda0e10ce`  |
| 787    | No file  | `b79fda0e10ce`  |
| 780    | No file  | `b79fda0e10ce`  |
| 771    | No file  | `b79fda0e10ce`  |
| 760    | No file  | `b79fda0e10ce`  |
| 748    | No file  | `b79fda0e10ce`  |
| 741    | No file  | `b79fda0e10ce`  |
| 736    | No file  | `b79fda0e10ce`  |
| 731    | No file  | `b79fda0e10ce`  |
| 723    | No file  | `b79fda0e10ce`  |
| 711    | No file  | `b79fda0e10ce`  |
| 707    | No file  | `b79fda0e10ce`  |
| 697    | No file  | `b79fda0e10ce`  |
| 689    | No file  | `b79fda0e10ce`  |
| 683    | No file  | `b79fda0e10ce`  |
| 678    | No file  | `b79fda0e10ce`  |
| 670    | No file  | `b79fda0e10ce`  |
| 661    | No file  | `b79fda0e10ce`  |
| 656    | No file  | `b79fda0e10ce`  |
| 652    | No file  | `b79fda0e10ce`  |
| 643    | No file  | `b79fda0e10ce`  |
| 637    | No file  | `b79fda0e10ce`  |
| 630    | No file  | `b79fda0e10ce`  |
| 627    | No file  | `b79fda0e10ce`  |
| 621    | No file  | `b79fda0e10ce`  |
| 617    | No file  | `b79fda0e10ce`  |
| 615    | No file  | `b79fda0e10ce`  |
| 606    | No file  | `b79fda0e10ce`  |
| 599    | No file  | `b79fda0e10ce`  |
| 592    | No file  | `b79fda0e10ce`  |
| 586    | No file  | `b79fda0e10ce`  |
| 577    | No file  | `b79fda0e10ce`  |
| 569    | No file  | `b79fda0e10ce`  |
| 561    | No file  | `b79fda0e10ce`  |
| 554    | No file  | `b79fda0e10ce`  |
| 542    | No file  | `b79fda0e10ce`  |
| 532    | No file  | `b79fda0e10ce`  |
| 531    | No file  | `b79fda0e10ce`  |
| 526    | No file  | `b79fda0e10ce`  |
| 521    | No file  | `b79fda0e10ce`  |
| 517    | No file  | `b79fda0e10ce`  |
| 510    | No file  | `b79fda0e10ce`  |
| 508    | No file  | `b79fda0e10ce`  |
| 504    | No file  | `b79fda0e10ce`  |
| 497    | No file  | `b79fda0e10ce`  |
| 491    | No file  | `b79fda0e10ce`  |
| 485    | No file  | `b79fda0e10ce`  |
| 478    | No file  | `b79fda0e10ce`  |
| 472    | No file  | `b79fda0e10ce`  |
| 466    | No file  | `b79fda0e10ce`  |
| 457    | No file  | `b79fda0e10ce`  |
| 452    | No file  | `b79fda0e10ce`  |
| 449    | No file  | `b79fda0e10ce`  |
| 435    | No file  | `b79fda0e10ce`  |

<!-- versions:end -->

## Companion Files

None. The handler names the region with its LOC type 17 name from
`languagedata_*.loc` when it is loaded. The cutscene file stays a name:
the `.pas` cutscenes under `character/cutscene/` and the `.paseqfe`
sequences under `sequence/` have no handler.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of rows                                |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (27 bytes)

| Offset  | Type | Field              | Notes                                                                                                   |
| ------- | ---- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | u16  | region_key         | `regioninfo.bss` region the cutscene belongs to (`890` Duvencrune Mountain, LOC type 17)                |
| `+0x02` | u32  | file_name_hash     | ASCII key hash (lookup3, seed `0xC5EDE`) of `cutscene_file_name` without `.pas`; matches on every row   |
| `+0x06` | u32  | cutscene_file_name | Index into `strings`: the cutscene file with `.pas` (`CS_Tutorial_06_EternalWinter_0000.pas`); unique   |
| `+0x0A` | u32  | start_condition    | Index into `strings`: the script that must hold for the cutscene to start; empty when none              |
| `+0x0E` | u32  | start_execute      | Index into `strings`: the script run when the cutscene starts; empty on most rows                       |
| `+0x12` | u32  | end_execute        | Index into `strings`: the script run when the cutscene ends                                             |
| `+0x16` | u32  | unknown_16         | Unique per row, `2` to `288` with gaps on client 3482; see Open Questions                                |
| `+0x1A` | u8   | unknown_1a         | `0` or `1`; see Open Questions                                                                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                       |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                           |
| `+0x04` | pstr[string_count] | strings      | UTF-8 file names and scripts; one empty string serves every empty field     |

## Layout 1

The row has no `unknown_1a`.

### Row (26 bytes)

| Offset  | Type | Field              | Notes                                                    |
| ------- | ---- | ------------------ | -------------------------------------------------------- |
| `+0x00` | u16  | region_key         | As in Layout 2                                           |
| `+0x02` | u32  | file_name_hash     | As in Layout 2                                           |
| `+0x06` | u32  | cutscene_file_name | As in Layout 2                                           |
| `+0x0A` | u32  | start_condition    | As in Layout 2                                           |
| `+0x0E` | u32  | start_execute      | As in Layout 2                                           |
| `+0x12` | u32  | end_execute        | As in Layout 2                                           |
| `+0x16` | u32  | unknown_16         | Unique per row; see Notes                                |

## Scripts

The three script fields hold calls joined by `;`. A `!` in front of a
call negates it, and `<or>` splits a condition into alternatives (6 rows).
Counts are rows using each call, client 3482.

| Field             | Calls (rows)                                                                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_condition` | `clearquest` (123), `progressquest` (108), `checkposition` (90), `checkquestcondition` (69), `checkinstancefieldmapkey` (27), `checkreservedplaynewcutscene` (16), `isContentsGroupOpen` (13), `checkclass` (4), `getlevel` (1) |
| `start_execute`   | `acceptquest` (7), `executeonlypartyleaderskip` (3)                                                                                             |
| `end_execute`     | `setPosition` (153), `completequestcondition` (67), `acceptquest` (38), `pushitem` (22), `executereserveplaynewcutscene` (19), `completequest` (6), `executeaicall` (3) |

`checkposition(x, y, z, radius)` takes world coordinates and a radius in
the same units (`500` in 51 of the 90 calls, `300` to `10000` in the rest);
`setPosition(x, y, z, angle)` moves the player when the cutscene ends.
`executereserveplaynewcutscene` in one row's `end_execute` and
`checkreservedplaynewcutscene` in another's `start_condition` chain
cutscenes.

On client 3482 the 185 rows cover 63 regions. `start_condition` is empty
on 68 rows, `start_execute` on 175 and `end_execute` on 1. The file names
group by story: `AbyssEntranceS1` (34), `EternalWinter` (33), `AbyssOneS1`
(31), `AbyssActiveS1` (19), `ReBalenos` (18), `AbyssTerritoryS1` (16),
`Yolunakea` (15), `Tutorial` (7) and 10 more.

## Field Names

`region_key`, `cutscene_file_name`, `start_condition`, `start_execute`
and `end_execute` are the `RegionKey`, `CutsceneFileName`,
`StartCondition`, `StartExecute` and `EndExecute` columns of the
`CutsceneBeginningLocationInfo` sheet in a private server's
`DataSheets.bexcel` on client 1784. The sheet's 10 rows match the 10 rows
of that client's `newcutscenedatatable.bss` in every column. 9 of the 10
file names are in client 3482's file; the region matches on 8 of them and
all four text columns on 4; the other 5 check and grant other quest steps
now (`CS_Tutorial_01_EternalWinter_0000` added `isContentsGroupOpen(0,8)`
and checks on four more quests). The sheet stores the file name without
`.pas`; both clients' files add it. The sheet's `#RegionName` note column names each
start place (`드벤크룬 산 : 깨어났을 때`, Duvencrune Mountain: on waking up).
`file_name_hash` is not a sheet column; the hash matches the name on all
185 rows of client 3482.

## Notes

- Client 1784 has no `sequencedatatable.bss`. Its
  `newcutscenedatatable.bss` holds the sheet's rows as 22-byte rows: the
  fields up to `end_execute`. The test clients have
  `sequencedatatable.bss` in its place from client 1927, with 26-byte rows
  (Layout 1, `unknown_16` added) up to client 2005 and 27-byte rows
  (`unknown_1a` added) from client 2011.
- `unknown_16` keeps its number per file name across clients: the 61
  names client 1927 shares with client 3482 all have the same number, and
  142 of the 143 client 2011 shares
  (`CS_AbyssEntranceS1_53_LightScattering_00` moved from `191` to `242`).
- On client 3482, 114 of the file names are both a `character/cutscene/`
  `.pas` and a `sequence/` `.paseqfe` file of the same name (lower case),
  the other 71 only a `.pas`.
- Rows are in no key order: the file opens with
  `CS_Tutorial_06_EternalWinter_0000` (`unknown_16` `7`), then
  `CS_EternalWinter_50_RabreDDuk6_0000` (`43`).

## Open Questions

### What `unknown_16` Is

The u32 is unique per row and runs `2` to `288` with gaps; sorted by it,
the rows fall into story groups in release order (`2` to `47` Eternal
Winter and the Duvencrune tutorial, `50` to `69` Balenos, `105` to `245`
the Abyss chapters, `246` to `260` Yolunakea, `274` up the later
regions), and a file keeps its number across clients (Notes). It looks
like a key the source sheet gained after client 1784, but no other table
read so far points at these numbers.

### What `unknown_1a` Marks

`1` on 40 rows of client 3482, `0` on 145. The `1` rows are all 34
`AbyssEntranceS1` cutscenes and 6 of the 31 `AbyssOneS1` ones; 33 of the
40 have no start condition, but 35 `0` rows have none either, and the flag
does not follow the `.pas` or `.paseqfe` split.
