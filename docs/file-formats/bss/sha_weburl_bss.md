# `sha_weburl.bss` Format

## Purpose

The web addresses of Shadow Arena: seven string-table indexes in one
PABR row, each pointing at a URL template with `{branch}`, `{region}`,
`{lang}` and `{pos}` placeholders, such as
`https://{branch}payment.pearlabyss.com`. The row has no count and no key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes | Records        | Row bytes |
| ------ | -------------- | ---------------- | ----- | -------------- | --------- |
| 4      | 1485 and later | `sha_weburl.bss` | 438   | 1 String Table | 398       |
| 3      | 1481           | `sha_weburl.bss` | 391   | 1 String Table | 355       |
| 2      | 1358 to 1474   | `sha_weburl.bss` | 329   | 1 String Table | 297       |
| 1      | 1355           | `sha_weburl.bss` | 92    | 1 String Table | 76        |

| Layout | File             | Known         | Unknown     |
| ------ | ---------------- | ------------- | ----------- |
| 4      | `sha_weburl.bss` | 426 B (97.3%) | 12 B (2.7%) |
| 3      | `sha_weburl.bss` | 379 B (96.9%) | 12 B (3.1%) |
| 2      | `sha_weburl.bss` | 317 B (96.4%) | 12 B (3.6%) |
| 1      | `sha_weburl.bss` | 92 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 4 | `b9ef52c85d7e`  |
| 3482   | Layout 4 | `b9ef52c85d7e`  |
| 3474   | Layout 4 | `b9ef52c85d7e`  |
| 3473   | Layout 4 | `b9ef52c85d7e`  |
| 3464   | Layout 4 | `b9ef52c85d7e`  |
| 3458   | Layout 4 | `b9ef52c85d7e`  |
| 3454   | Layout 4 | `b9ef52c85d7e`  |
| 3444   | Layout 4 | `b9ef52c85d7e`  |
| 3435   | Layout 4 | `b9ef52c85d7e`  |
| 3426   | Layout 4 | `b9ef52c85d7e`  |
| 3418   | Layout 4 | `b9ef52c85d7e`  |
| 3412   | Layout 4 | `b9ef52c85d7e`  |
| 3402   | Layout 4 | `b9ef52c85d7e`  |
| 3396   | Layout 4 | `b9ef52c85d7e`  |
| 3387   | Layout 4 | `b9ef52c85d7e`  |
| 3381   | Layout 4 | `b9ef52c85d7e`  |
| 3373   | Layout 4 | `b9ef52c85d7e`  |
| 3364   | Layout 4 | `b9ef52c85d7e`  |
| 3356   | Layout 4 | `b9ef52c85d7e`  |
| 3349   | Layout 4 | `b9ef52c85d7e`  |
| 3342   | Layout 4 | `b9ef52c85d7e`  |
| 3335   | Layout 4 | `b9ef52c85d7e`  |
| 3326   | Layout 4 | `b9ef52c85d7e`  |
| 3321   | Layout 4 | `b9ef52c85d7e`  |
| 3314   | Layout 4 | `b9ef52c85d7e`  |
| 3303   | Layout 4 | `b9ef52c85d7e`  |
| 3302   | Layout 4 | `b9ef52c85d7e`  |
| 3293   | Layout 4 | `b9ef52c85d7e`  |
| 3283   | Layout 4 | `b9ef52c85d7e`  |
| 3275   | Layout 4 | `b9ef52c85d7e`  |
| 3267   | Layout 4 | `b9ef52c85d7e`  |
| 3258   | Layout 4 | `b9ef52c85d7e`  |
| 3251   | Layout 4 | `b9ef52c85d7e`  |
| 3242   | Layout 4 | `b9ef52c85d7e`  |
| 3235   | Layout 4 | `b9ef52c85d7e`  |
| 3229   | Layout 4 | `b9ef52c85d7e`  |
| 3212   | Layout 4 | `b9ef52c85d7e`  |
| 3203   | Layout 4 | `b9ef52c85d7e`  |
| 3193   | Layout 4 | `b9ef52c85d7e`  |
| 3186   | Layout 4 | `b9ef52c85d7e`  |
| 3177   | Layout 4 | `b9ef52c85d7e`  |
| 3169   | Layout 4 | `b9ef52c85d7e`  |
| 3158   | Layout 4 | `b9ef52c85d7e`  |
| 3151   | Layout 4 | `b9ef52c85d7e`  |
| 3144   | Layout 4 | `b9ef52c85d7e`  |
| 3133   | Layout 4 | `b9ef52c85d7e`  |
| 3125   | Layout 4 | `b9ef52c85d7e`  |
| 3118   | Layout 4 | `b9ef52c85d7e`  |
| 3111   | Layout 4 | `b9ef52c85d7e`  |
| 3103   | Layout 4 | `b9ef52c85d7e`  |
| 3095   | Layout 4 | `b9ef52c85d7e`  |
| 3086   | Layout 4 | `b9ef52c85d7e`  |
| 3072   | Layout 4 | `b9ef52c85d7e`  |
| 3062   | Layout 4 | `b9ef52c85d7e`  |
| 3052   | Layout 4 | `b9ef52c85d7e`  |
| 3045   | Layout 4 | `b9ef52c85d7e`  |
| 3037   | Layout 4 | `b9ef52c85d7e`  |
| 3030   | Layout 4 | `b9ef52c85d7e`  |
| 3021   | Layout 4 | `b9ef52c85d7e`  |
| 3012   | Layout 4 | `b9ef52c85d7e`  |
| 3002   | Layout 4 | `b9ef52c85d7e`  |
| 2995   | Layout 4 | `b9ef52c85d7e`  |
| 2987   | Layout 4 | `b9ef52c85d7e`  |
| 2978   | Layout 4 | `b9ef52c85d7e`  |
| 2970   | Layout 4 | `b9ef52c85d7e`  |
| 2959   | Layout 4 | `b9ef52c85d7e`  |
| 2951   | Layout 4 | `b9ef52c85d7e`  |
| 2942   | Layout 4 | `b9ef52c85d7e`  |
| 2935   | Layout 4 | `b9ef52c85d7e`  |
| 2932   | Layout 4 | `b9ef52c85d7e`  |
| 2923   | Layout 4 | `b9ef52c85d7e`  |
| 2919   | Layout 4 | `b9ef52c85d7e`  |
| 2907   | Layout 4 | `b9ef52c85d7e`  |
| 2900   | Layout 4 | `b9ef52c85d7e`  |
| 2891   | Layout 4 | `b9ef52c85d7e`  |
| 2882   | Layout 4 | `b9ef52c85d7e`  |
| 2872   | Layout 4 | `b9ef52c85d7e`  |
| 2863   | Layout 4 | `b9ef52c85d7e`  |
| 2855   | Layout 4 | `b9ef52c85d7e`  |
| 2849   | Layout 4 | `b9ef52c85d7e`  |
| 2844   | Layout 4 | `b9ef52c85d7e`  |
| 2834   | Layout 4 | `b9ef52c85d7e`  |
| 2825   | Layout 4 | `b9ef52c85d7e`  |
| 2819   | Layout 4 | `b9ef52c85d7e`  |
| 2811   | Layout 4 | `b9ef52c85d7e`  |
| 2803   | Layout 4 | `b9ef52c85d7e`  |
| 2794   | Layout 4 | `b9ef52c85d7e`  |
| 2783   | Layout 4 | `b9ef52c85d7e`  |
| 2774   | Layout 4 | `b9ef52c85d7e`  |
| 2765   | Layout 4 | `b9ef52c85d7e`  |
| 2756   | Layout 4 | `b9ef52c85d7e`  |
| 2750   | Layout 4 | `b9ef52c85d7e`  |
| 2743   | Layout 4 | `b9ef52c85d7e`  |
| 2736   | Layout 4 | `b9ef52c85d7e`  |
| 2726   | Layout 4 | `b9ef52c85d7e`  |
| 2717   | Layout 4 | `b9ef52c85d7e`  |
| 2709   | Layout 4 | `b9ef52c85d7e`  |
| 2703   | Layout 4 | `b9ef52c85d7e`  |
| 2695   | Layout 4 | `b9ef52c85d7e`  |
| 2684   | Layout 4 | `b9ef52c85d7e`  |
| 2672   | Layout 4 | `b9ef52c85d7e`  |
| 2665   | Layout 4 | `b9ef52c85d7e`  |
| 2657   | Layout 4 | `b9ef52c85d7e`  |
| 2649   | Layout 4 | `b9ef52c85d7e`  |
| 2644   | Layout 4 | `b9ef52c85d7e`  |
| 2637   | Layout 4 | `b9ef52c85d7e`  |
| 2629   | Layout 4 | `b9ef52c85d7e`  |
| 2619   | Layout 4 | `b9ef52c85d7e`  |
| 2612   | Layout 4 | `b9ef52c85d7e`  |
| 2606   | Layout 4 | `b9ef52c85d7e`  |
| 2602   | Layout 4 | `b9ef52c85d7e`  |
| 2601   | Layout 4 | `b9ef52c85d7e`  |
| 2592   | Layout 4 | `b9ef52c85d7e`  |
| 2583   | Layout 4 | `b9ef52c85d7e`  |
| 2575   | Layout 4 | `b9ef52c85d7e`  |
| 2567   | Layout 4 | `b9ef52c85d7e`  |
| 2560   | Layout 4 | `b9ef52c85d7e`  |
| 2553   | Layout 4 | `b9ef52c85d7e`  |
| 2545   | Layout 4 | `b9ef52c85d7e`  |
| 2538   | Layout 4 | `b9ef52c85d7e`  |
| 2529   | Layout 4 | `b9ef52c85d7e`  |
| 2519   | Layout 4 | `b9ef52c85d7e`  |
| 2513   | Layout 4 | `b9ef52c85d7e`  |
| 2510   | Layout 4 | `b9ef52c85d7e`  |
| 2507   | Layout 4 | `b9ef52c85d7e`  |
| 2503   | Layout 4 | `b9ef52c85d7e`  |
| 2498   | Layout 4 | `b9ef52c85d7e`  |
| 2492   | Layout 4 | `b9ef52c85d7e`  |
| 2487   | Layout 4 | `b9ef52c85d7e`  |
| 2480   | Layout 4 | `b9ef52c85d7e`  |
| 2474   | Layout 4 | `b9ef52c85d7e`  |
| 2468   | Layout 4 | `b9ef52c85d7e`  |
| 2460   | Layout 4 | `b9ef52c85d7e`  |
| 2453   | Layout 4 | `b9ef52c85d7e`  |
| 2444   | Layout 4 | `b9ef52c85d7e`  |
| 2438   | Layout 4 | `b9ef52c85d7e`  |
| 2434   | Layout 4 | `b9ef52c85d7e`  |
| 2429   | Layout 4 | `b9ef52c85d7e`  |
| 2421   | Layout 4 | `b9ef52c85d7e`  |
| 2414   | Layout 4 | `b9ef52c85d7e`  |
| 2407   | Layout 4 | `b9ef52c85d7e`  |
| 2401   | Layout 4 | `b9ef52c85d7e`  |
| 2397   | Layout 4 | `b9ef52c85d7e`  |
| 2393   | Layout 4 | `b9ef52c85d7e`  |
| 2384   | Layout 4 | `b9ef52c85d7e`  |
| 2378   | Layout 4 | `b9ef52c85d7e`  |
| 2372   | Layout 4 | `b9ef52c85d7e`  |
| 2358   | Layout 4 | `b9ef52c85d7e`  |
| 2352   | Layout 4 | `b9ef52c85d7e`  |
| 2347   | Layout 4 | `b9ef52c85d7e`  |
| 2343   | Layout 4 | `b9ef52c85d7e`  |
| 2335   | Layout 4 | `b9ef52c85d7e`  |
| 2327   | Layout 4 | `b9ef52c85d7e`  |
| 2324   | Layout 4 | `b9ef52c85d7e`  |
| 2319   | Layout 4 | `b9ef52c85d7e`  |
| 2313   | Layout 4 | `b9ef52c85d7e`  |
| 2308   | Layout 4 | `b9ef52c85d7e`  |
| 2302   | Layout 4 | `b9ef52c85d7e`  |
| 2295   | Layout 4 | `b9ef52c85d7e`  |
| 2290   | Layout 4 | `b9ef52c85d7e`  |
| 2284   | Layout 4 | `b9ef52c85d7e`  |
| 2276   | Layout 4 | `b9ef52c85d7e`  |
| 2269   | Layout 4 | `b9ef52c85d7e`  |
| 2259   | Layout 4 | `b9ef52c85d7e`  |
| 2250   | Layout 4 | `b9ef52c85d7e`  |
| 2243   | Layout 4 | `b9ef52c85d7e`  |
| 2235   | Layout 4 | `b9ef52c85d7e`  |
| 2229   | Layout 4 | `b9ef52c85d7e`  |
| 2224   | Layout 4 | `b9ef52c85d7e`  |
| 2218   | Layout 4 | `b9ef52c85d7e`  |
| 2215   | Layout 4 | `b9ef52c85d7e`  |
| 2207   | Layout 4 | `b9ef52c85d7e`  |
| 2203   | Layout 4 | `b9ef52c85d7e`  |
| 2196   | Layout 4 | `b9ef52c85d7e`  |
| 2192   | Layout 4 | `b9ef52c85d7e`  |
| 2189   | Layout 4 | `b9ef52c85d7e`  |
| 2183   | Layout 4 | `b9ef52c85d7e`  |
| 2179   | Layout 4 | `b9ef52c85d7e`  |
| 2171   | Layout 4 | `b9ef52c85d7e`  |
| 2163   | Layout 4 | `b9ef52c85d7e`  |
| 2156   | Layout 4 | `b9ef52c85d7e`  |
| 2151   | Layout 4 | `b9ef52c85d7e`  |
| 2147   | Layout 4 | `b9ef52c85d7e`  |
| 2142   | Layout 4 | `b9ef52c85d7e`  |
| 2138   | Layout 4 | `b9ef52c85d7e`  |
| 2134   | Layout 4 | `b9ef52c85d7e`  |
| 2130   | Layout 4 | `b9ef52c85d7e`  |
| 2122   | Layout 4 | `b9ef52c85d7e`  |
| 2107   | Layout 4 | `b9ef52c85d7e`  |
| 2098   | Layout 4 | `b9ef52c85d7e`  |
| 2089   | Layout 4 | `b9ef52c85d7e`  |
| 2081   | Layout 4 | `b9ef52c85d7e`  |
| 2073   | Layout 4 | `b9ef52c85d7e`  |
| 2067   | Layout 4 | `b9ef52c85d7e`  |
| 2063   | Layout 4 | `b9ef52c85d7e`  |
| 2059   | Layout 4 | `b9ef52c85d7e`  |
| 2052   | Layout 4 | `b9ef52c85d7e`  |
| 2044   | Layout 4 | `b9ef52c85d7e`  |
| 2039   | Layout 4 | `b9ef52c85d7e`  |
| 2032   | Layout 4 | `b9ef52c85d7e`  |
| 2025   | Layout 4 | `b9ef52c85d7e`  |
| 2011   | Layout 4 | `b9ef52c85d7e`  |
| 2005   | Layout 4 | `b9ef52c85d7e`  |
| 2000   | Layout 4 | `b9ef52c85d7e`  |
| 1996   | Layout 4 | `b9ef52c85d7e`  |
| 1991   | Layout 4 | `b9ef52c85d7e`  |
| 1985   | Layout 4 | `b9ef52c85d7e`  |
| 1980   | Layout 4 | `b9ef52c85d7e`  |
| 1969   | Layout 4 | `b9ef52c85d7e`  |
| 1964   | Layout 4 | `b9ef52c85d7e`  |
| 1958   | Layout 4 | `b9ef52c85d7e`  |
| 1950   | Layout 4 | `b9ef52c85d7e`  |
| 1945   | Layout 4 | `b9ef52c85d7e`  |
| 1937   | Layout 4 | `b9ef52c85d7e`  |
| 1933   | Layout 4 | `b9ef52c85d7e`  |
| 1927   | Layout 4 | `b9ef52c85d7e`  |
| 1921   | Layout 4 | `b9ef52c85d7e`  |
| 1914   | Layout 4 | `b9ef52c85d7e`  |
| 1908   | Layout 4 | `b9ef52c85d7e`  |
| 1897   | Layout 4 | `b9ef52c85d7e`  |
| 1892   | Layout 4 | `b9ef52c85d7e`  |
| 1886   | Layout 4 | `b9ef52c85d7e`  |
| 1881   | Layout 4 | `b9ef52c85d7e`  |
| 1871   | Layout 4 | `b9ef52c85d7e`  |
| 1866   | Layout 4 | `b9ef52c85d7e`  |
| 1862   | Layout 4 | `b9ef52c85d7e`  |
| 1854   | Layout 4 | `b9ef52c85d7e`  |
| 1846   | Layout 4 | `b9ef52c85d7e`  |
| 1838   | Layout 4 | `b9ef52c85d7e`  |
| 1832   | Layout 4 | `b9ef52c85d7e`  |
| 1826   | Layout 4 | `b9ef52c85d7e`  |
| 1822   | Layout 4 | `b9ef52c85d7e`  |
| 1818   | Layout 4 | `b9ef52c85d7e`  |
| 1804   | Layout 4 | `b9ef52c85d7e`  |
| 1794   | Layout 4 | `b9ef52c85d7e`  |
| 1790   | Layout 4 | `b9ef52c85d7e`  |
| 1784   | Layout 4 | `b9ef52c85d7e`  |
| 1774   | Layout 4 | `b9ef52c85d7e`  |
| 1771   | Layout 4 | `b9ef52c85d7e`  |
| 1762   | Layout 4 | `b9ef52c85d7e`  |
| 1759   | Layout 4 | `b9ef52c85d7e`  |
| 1754   | Layout 4 | `b9ef52c85d7e`  |
| 1749   | Layout 4 | `b9ef52c85d7e`  |
| 1743   | Layout 4 | `b9ef52c85d7e`  |
| 1737   | Layout 4 | `b9ef52c85d7e`  |
| 1731   | Layout 4 | `b9ef52c85d7e`  |
| 1725   | Layout 4 | `b9ef52c85d7e`  |
| 1717   | Layout 4 | `b9ef52c85d7e`  |
| 1710   | Layout 4 | `b9ef52c85d7e`  |
| 1704   | Layout 4 | `b9ef52c85d7e`  |
| 1698   | Layout 4 | `b9ef52c85d7e`  |
| 1690   | Layout 4 | `b9ef52c85d7e`  |
| 1685   | Layout 4 | `b9ef52c85d7e`  |
| 1680   | Layout 4 | `b9ef52c85d7e`  |
| 1674   | Layout 4 | `b9ef52c85d7e`  |
| 1668   | Layout 4 | `b9ef52c85d7e`  |
| 1659   | Layout 4 | `b9ef52c85d7e`  |
| 1649   | Layout 4 | `b9ef52c85d7e`  |
| 1642   | Layout 4 | `b9ef52c85d7e`  |
| 1636   | Layout 4 | `b9ef52c85d7e`  |
| 1628   | Layout 4 | `b9ef52c85d7e`  |
| 1622   | Layout 4 | `b9ef52c85d7e`  |
| 1614   | Layout 4 | `b9ef52c85d7e`  |
| 1608   | Layout 4 | `b9ef52c85d7e`  |
| 1602   | Layout 4 | `b9ef52c85d7e`  |
| 1598   | Layout 4 | `b9ef52c85d7e`  |
| 1594   | Layout 4 | `b9ef52c85d7e`  |
| 1590   | Layout 4 | `b9ef52c85d7e`  |
| 1587   | Layout 4 | `b9ef52c85d7e`  |
| 1584   | Layout 4 | `b9ef52c85d7e`  |
| 1579   | Layout 4 | `b9ef52c85d7e`  |
| 1572   | Layout 4 | `b9ef52c85d7e`  |
| 1565   | Layout 4 | `b9ef52c85d7e`  |
| 1559   | Layout 4 | `b9ef52c85d7e`  |
| 1554   | Layout 4 | `b9ef52c85d7e`  |
| 1547   | Layout 4 | `b9ef52c85d7e`  |
| 1537   | Layout 4 | `b9ef52c85d7e`  |
| 1529   | Layout 4 | `b9ef52c85d7e`  |
| 1524   | Layout 4 | `b9ef52c85d7e`  |
| 1519   | Layout 4 | `b9ef52c85d7e`  |
| 1509   | Layout 4 | `b9ef52c85d7e`  |
| 1506   | Layout 4 | `b9ef52c85d7e`  |
| 1504   | Layout 4 | `b9ef52c85d7e`  |
| 1500   | Layout 4 | `b9ef52c85d7e`  |
| 1493   | Layout 4 | `b9ef52c85d7e`  |
| 1489   | Layout 4 | `b9ef52c85d7e`  |
| 1485   | Layout 4 | `b9ef52c85d7e`  |
| 1481   | Layout 3 | `b9ef52c85d7e`  |
| 1474   | Layout 2 | `b9ef52c85d7e`  |
| 1466   | Layout 2 | `b9ef52c85d7e`  |
| 1462   | Layout 2 | `b9ef52c85d7e`  |
| 1459   | Layout 2 | `b9ef52c85d7e`  |
| 1453   | Layout 2 | `b9ef52c85d7e`  |
| 1450   | Layout 2 | `b9ef52c85d7e`  |
| 1445   | Layout 2 | `b9ef52c85d7e`  |
| 1439   | Layout 2 | `b9ef52c85d7e`  |
| 1433   | Layout 2 | `b9ef52c85d7e`  |
| 1430   | Layout 2 | `b9ef52c85d7e`  |
| 1426   | Layout 2 | `b9ef52c85d7e`  |
| 1421   | Layout 2 | `b9ef52c85d7e`  |
| 1417   | Layout 2 | `b9ef52c85d7e`  |
| 1416   | Layout 2 | `b9ef52c85d7e`  |
| 1409   | Layout 2 | `b9ef52c85d7e`  |
| 1405   | Layout 2 | `b9ef52c85d7e`  |
| 1401   | Layout 2 | `b9ef52c85d7e`  |
| 1396   | Layout 2 | `b9ef52c85d7e`  |
| 1391   | Layout 2 | `b9ef52c85d7e`  |
| 1390   | Layout 2 | `b9ef52c85d7e`  |
| 1386   | Layout 2 | `b9ef52c85d7e`  |
| 1381   | Layout 2 | `b9ef52c85d7e`  |
| 1379   | Layout 2 | `b9ef52c85d7e`  |
| 1372   | Layout 2 | `b9ef52c85d7e`  |
| 1366   | Layout 2 | `b9ef52c85d7e`  |
| 1364   | Layout 2 | `b9ef52c85d7e`  |
| 1363   | Layout 2 | `b9ef52c85d7e`  |
| 1360   | Layout 2 | `b9ef52c85d7e`  |
| 1358   | Layout 2 | `b9ef52c85d7e`  |
| 1355   | Layout 1 | `b9ef52c85d7e`  |
| 1351   | No file  | `b9ef52c85d7e`  |
| 1348   | No file  | `b9ef52c85d7e`  |
| 1346   | No file  | `b9ef52c85d7e`  |
| 1341   | No file  | `b9ef52c85d7e`  |
| 1340   | No file  | `b9ef52c85d7e`  |
| 1338   | No file  | `b9ef52c85d7e`  |
| 1335   | No file  | `b9ef52c85d7e`  |
| 1333   | No file  | `b9ef52c85d7e`  |
| 1329   | No file  | `b9ef52c85d7e`  |
| 1327   | No file  | `b9ef52c85d7e`  |
| 1324   | No file  | `b9ef52c85d7e`  |
| 1321   | No file  | `b9ef52c85d7e`  |
| 1319   | No file  | `b9ef52c85d7e`  |
| 1318   | No file  | `b9ef52c85d7e`  |
| 1316   | No file  | `b9ef52c85d7e`  |
| 1313   | No file  | `b9ef52c85d7e`  |
| 1311   | No file  | `b9ef52c85d7e`  |
| 1309   | No file  | `b9ef52c85d7e`  |
| 1304   | No file  | `b9ef52c85d7e`  |
| 1292   | No file  | `b9ef52c85d7e`  |
| 1286   | No file  | `b9ef52c85d7e`  |
| 1280   | No file  | `b9ef52c85d7e`  |
| 1276   | No file  | `b9ef52c85d7e`  |
| 1267   | No file  | `b9ef52c85d7e`  |
| 1261   | No file  | `b9ef52c85d7e`  |
| 1256   | No file  | `b9ef52c85d7e`  |
| 1250   | No file  | `b9ef52c85d7e`  |
| 1246   | No file  | `b9ef52c85d7e`  |
| 1239   | No file  | `b9ef52c85d7e`  |
| 1230   | No file  | `b9ef52c85d7e`  |
| 1226   | No file  | `b9ef52c85d7e`  |
| 1220   | No file  | `b9ef52c85d7e`  |
| 1217   | No file  | `b9ef52c85d7e`  |
| 1211   | No file  | `b9ef52c85d7e`  |
| 1210   | No file  | `b9ef52c85d7e`  |
| 1208   | No file  | `b9ef52c85d7e`  |
| 1203   | No file  | `b9ef52c85d7e`  |
| 1197   | No file  | `b9ef52c85d7e`  |
| 1194   | No file  | `b9ef52c85d7e`  |
| 1192   | No file  | `b9ef52c85d7e`  |
| 1187   | No file  | `b9ef52c85d7e`  |
| 1183   | No file  | `b9ef52c85d7e`  |
| 1177   | No file  | `b9ef52c85d7e`  |
| 1173   | No file  | `b9ef52c85d7e`  |
| 1167   | No file  | `b9ef52c85d7e`  |
| 1164   | No file  | `b9ef52c85d7e`  |
| 1156   | No file  | `b9ef52c85d7e`  |
| 1149   | No file  | `b9ef52c85d7e`  |
| 1144   | No file  | `b9ef52c85d7e`  |
| 1137   | No file  | `b9ef52c85d7e`  |
| 1132   | No file  | `b9ef52c85d7e`  |
| 1127   | No file  | `b9ef52c85d7e`  |
| 1122   | No file  | `b9ef52c85d7e`  |
| 1118   | No file  | `b9ef52c85d7e`  |
| 1114   | No file  | `b9ef52c85d7e`  |
| 1109   | No file  | `b9ef52c85d7e`  |
| 1102   | No file  | `b9ef52c85d7e`  |
| 1096   | No file  | `b9ef52c85d7e`  |
| 1088   | No file  | `b9ef52c85d7e`  |
| 1081   | No file  | `b9ef52c85d7e`  |
| 1076   | No file  | `b9ef52c85d7e`  |
| 1069   | No file  | `b9ef52c85d7e`  |
| 1064   | No file  | `b9ef52c85d7e`  |
| 1058   | No file  | `b9ef52c85d7e`  |
| 1051   | No file  | `b9ef52c85d7e`  |
| 1044   | No file  | `b9ef52c85d7e`  |
| 1036   | No file  | `b9ef52c85d7e`  |
| 1026   | No file  | `b9ef52c85d7e`  |
| 1016   | No file  | `b9ef52c85d7e`  |
| 1009   | No file  | `b9ef52c85d7e`  |
| 1005   | No file  | `b9ef52c85d7e`  |
| 1000   | No file  | `b9ef52c85d7e`  |
| 998    | No file  | `b9ef52c85d7e`  |
| 990    | No file  | `b9ef52c85d7e`  |
| 979    | No file  | `b9ef52c85d7e`  |
| 972    | No file  | `b9ef52c85d7e`  |
| 963    | No file  | `b9ef52c85d7e`  |
| 955    | No file  | `b9ef52c85d7e`  |
| 946    | No file  | `b9ef52c85d7e`  |
| 938    | No file  | `b9ef52c85d7e`  |
| 927    | No file  | `b9ef52c85d7e`  |
| 911    | No file  | `b9ef52c85d7e`  |
| 904    | No file  | `b9ef52c85d7e`  |
| 899    | No file  | `b9ef52c85d7e`  |
| 894    | No file  | `b9ef52c85d7e`  |
| 885    | No file  | `b9ef52c85d7e`  |
| 879    | No file  | `b9ef52c85d7e`  |
| 872    | No file  | `b9ef52c85d7e`  |
| 864    | No file  | `b9ef52c85d7e`  |
| 855    | No file  | `b9ef52c85d7e`  |
| 853    | No file  | `b9ef52c85d7e`  |
| 845    | No file  | `b9ef52c85d7e`  |
| 837    | No file  | `b9ef52c85d7e`  |
| 829    | No file  | `b9ef52c85d7e`  |
| 822    | No file  | `b9ef52c85d7e`  |
| 814    | No file  | `b9ef52c85d7e`  |
| 805    | No file  | `b9ef52c85d7e`  |
| 794    | No file  | `b9ef52c85d7e`  |
| 787    | No file  | `b9ef52c85d7e`  |
| 780    | No file  | `b9ef52c85d7e`  |
| 771    | No file  | `b9ef52c85d7e`  |
| 760    | No file  | `b9ef52c85d7e`  |
| 748    | No file  | `b9ef52c85d7e`  |
| 741    | No file  | `b9ef52c85d7e`  |
| 736    | No file  | `b9ef52c85d7e`  |
| 731    | No file  | `b9ef52c85d7e`  |
| 723    | No file  | `b9ef52c85d7e`  |
| 711    | No file  | `b9ef52c85d7e`  |
| 707    | No file  | `b9ef52c85d7e`  |
| 697    | No file  | `b9ef52c85d7e`  |
| 689    | No file  | `b9ef52c85d7e`  |
| 683    | No file  | `b9ef52c85d7e`  |
| 678    | No file  | `b9ef52c85d7e`  |
| 670    | No file  | `b9ef52c85d7e`  |
| 661    | No file  | `b9ef52c85d7e`  |
| 656    | No file  | `b9ef52c85d7e`  |
| 652    | No file  | `b9ef52c85d7e`  |
| 643    | No file  | `b9ef52c85d7e`  |
| 637    | No file  | `b9ef52c85d7e`  |
| 630    | No file  | `b9ef52c85d7e`  |
| 627    | No file  | `b9ef52c85d7e`  |
| 621    | No file  | `b9ef52c85d7e`  |
| 617    | No file  | `b9ef52c85d7e`  |
| 615    | No file  | `b9ef52c85d7e`  |
| 606    | No file  | `b9ef52c85d7e`  |
| 599    | No file  | `b9ef52c85d7e`  |
| 592    | No file  | `b9ef52c85d7e`  |
| 586    | No file  | `b9ef52c85d7e`  |
| 577    | No file  | `b9ef52c85d7e`  |
| 569    | No file  | `b9ef52c85d7e`  |
| 561    | No file  | `b9ef52c85d7e`  |
| 554    | No file  | `b9ef52c85d7e`  |
| 542    | No file  | `b9ef52c85d7e`  |
| 532    | No file  | `b9ef52c85d7e`  |
| 531    | No file  | `b9ef52c85d7e`  |
| 526    | No file  | `b9ef52c85d7e`  |
| 521    | No file  | `b9ef52c85d7e`  |
| 517    | No file  | `b9ef52c85d7e`  |
| 510    | No file  | `b9ef52c85d7e`  |
| 508    | No file  | `b9ef52c85d7e`  |
| 504    | No file  | `b9ef52c85d7e`  |
| 497    | No file  | `b9ef52c85d7e`  |
| 491    | No file  | `b9ef52c85d7e`  |
| 485    | No file  | `b9ef52c85d7e`  |
| 478    | No file  | `b9ef52c85d7e`  |
| 472    | No file  | `b9ef52c85d7e`  |
| 466    | No file  | `b9ef52c85d7e`  |
| 457    | No file  | `b9ef52c85d7e`  |
| 452    | No file  | `b9ef52c85d7e`  |
| 449    | No file  | `b9ef52c85d7e`  |
| 435    | No file  | `b9ef52c85d7e`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset              | Type         | Field             | Notes                                                                 |
| ------------------- | ------------ | ----------------- | --------------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                                          |
| `+0x04`             | u32          | record_client_ref | String table index of the record client API URL                       |
| `+0x08`             | u32          | unknown_08        | String table index; the event banner URL on every client checked      |
| `+0x0C`             | u32          | unknown_0c        | String table index; the in-game banner URL on every client checked    |
| `+0x10`             | u32          | cash_shop_ref     | String table index of the cash shop (in-game banner) URL              |
| `+0x14`             | u32          | unknown_14        | String table index; the in-game banner URL on every client checked    |
| `+0x18`             | u32          | replay_ref        | String table index of the replay API URL                              |
| `+0x1C`             | u32          | payment_ref       | String table index of the payment URL                                 |
| `+0x20`             | String Table | string_table      | See String Table                                                      |
| `string_table+0x00` | u32          | table_start       | Offset of the string table; `0x20` on every client checked            |
| `string_table+0x04` | u32          | zero              | Always `0`                                                            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `5` on every client checked           |
| `+0x04` | pstr[string_count] | strings      | UTF-8 URL templates in first-use order; see URLs         |

## Layout 3

### File Layout

| Offset              | Type         | Field             | Notes                                           |
| ------------------- | ------------ | ----------------- | ----------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                    |
| `+0x04`             | u32          | record_client_ref | As in Layout 4                                  |
| `+0x08`             | u32          | unknown_08        | As in Layout 4                                  |
| `+0x0C`             | u32          | unknown_0c        | As in Layout 4                                  |
| `+0x10`             | u32          | cash_shop_ref     | As in Layout 4                                  |
| `+0x14`             | u32          | unknown_14        | As in Layout 4                                  |
| `+0x18`             | u32          | replay_ref        | As in Layout 4                                  |
| `+0x1C`             | String Table | string_table      | See String Table                                |
| `string_table+0x00` | u32          | table_start       | Offset of the string table, `0x1C`              |
| `string_table+0x04` | u32          | zero              | Always `0`                                      |

## Layout 2

### File Layout

| Offset              | Type         | Field             | Notes                                           |
| ------------------- | ------------ | ----------------- | ----------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                    |
| `+0x04`             | u32          | record_client_ref | As in Layout 4                                  |
| `+0x08`             | u32          | unknown_08        | As in Layout 4                                  |
| `+0x0C`             | u32          | unknown_0c        | As in Layout 4                                  |
| `+0x10`             | u32          | cash_shop_ref     | As in Layout 4                                  |
| `+0x14`             | u32          | unknown_14        | As in Layout 4                                  |
| `+0x18`             | String Table | string_table      | See String Table                                |
| `string_table+0x00` | u32          | table_start       | Offset of the string table, `0x18`              |
| `string_table+0x04` | u32          | zero              | Always `0`                                      |

## Layout 1

### File Layout

| Offset              | Type         | Field             | Notes                                           |
| ------------------- | ------------ | ----------------- | ----------------------------------------------- |
| `+0x00`             | char[4]      | magic             | ASCII `PABR`                                    |
| `+0x04`             | u32          | record_client_ref | As in Layout 4                                  |
| `+0x08`             | String Table | string_table      | See String Table                                |
| `string_table+0x00` | u32          | table_start       | Offset of the string table, `0x08`              |
| `string_table+0x04` | u32          | zero              | Always `0`                                      |

## URLs

Client 3482:

| Field               | URL                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `record_client_ref` | `https://{branch}{region}recordclient-api-shadowarena.pearlabyss.com`                         |
| `unknown_08`        | `https://{branch}{region}game-shadowarena.pearlabyss.com/InGameBanner/Home/EventBanner?language={lang}` |
| `unknown_0c`        | `https://{branch}{region}game-shadowarena.pearlabyss.com/InGameBanner/Home/Index?language={lang}&position={pos}` |
| `cash_shop_ref`     | the same as `unknown_0c`                                                                      |
| `unknown_14`        | the same as `unknown_0c`                                                                      |
| `replay_ref`        | `https://{branch}api-shadowarena.pearlabyss.com/Replay`                                       |
| `payment_ref`       | `https://{branch}payment.pearlabyss.com`                                                      |

## Field Names

The `SA_Web_URL` sheet of a private server's `DataSheets.bexcel` on
client 1784 has seven columns, `RecordClient`, `RecordServer`,
`EventBanner`, `CashShop`, `Policy`, `Replay` and `Payment`, and one row.
The client 1784 file is the same 438 bytes as the client 3482 file. Its
seven fields match the sheet by column position and value on four
columns, which name them: `RecordClient` (`+0x04`), `CashShop`
(`+0x10`), `Replay` (`+0x18`) and `Payment` (`+0x1C`).

The other three do not match. At `+0x08` the sheet has the
`RecordServer` URL (`recordserver-api-shadowarena`), which the file does
not hold; the file has the sheet's `EventBanner` URL there. At `+0x0C`
the sheet has `EventBanner`, the file the `CashShop` URL. At `+0x14` the
sheet has the `Policy` URL (`.../Policy?language={lang}`), which the
file does not hold; the file has the `CashShop` URL again. They stay
`unknown_*`.

## Notes

- The file is the same on clients 1784, 2107, 2765, 3002 and 3482. The
  older layouts hold the first fields only: Layout 1 `record_client_ref`,
  Layout 2 up to `unknown_14`, Layout 3 up to `replay_ref`.
- The `SA` prefix of the sheet and of [`bgmstatesa.bss`](bgmstatesa_bss.md)
  reads as Shadow Arena, the `*-shadowarena.pearlabyss.com` hosts of the
  URLs.
- No client Lua file of client 3482 names the table, a Shadow Arena URL
  or a `{branch}` placeholder.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/client_tables.py`, with
  the four named URLs.

## Open Questions

### The Three Unmatched URLs

The file was compiled from a sheet other than the client 1784 one: its
`+0x08`, `+0x0C` and `+0x14` URLs are not the sheet's `RecordServer`,
`EventBanner` and `Policy` values. Whether those are the three columns
of the file, with other values, or the file stores its URLs in another
order, is open.
