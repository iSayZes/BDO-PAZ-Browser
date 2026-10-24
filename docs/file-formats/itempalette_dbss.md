# `itempalette.dbss` Format

## Purpose

The dye colour each dye item applies: per item key a palette type (a row
of [`dyeingpalette.dbss`](dyeingpalette_dbss.md)) and the index of the
colour in that palette. Palette types `1` to `8` are the eight tabs of the
dye window, Basic Dye to Valencian Dye. Companion `itempaletteoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ------ | ---------------- | --------- |
| 1      | 1276 and later | 3483    | `itempalette.dbss`       | 6,766  | 1,127 Row        | 6         |
| 1      | 1276 and later | 3483    | `itempaletteoffset.dbss` | 13,528 | 1,127 Offset Row | 12        |

| Layout | File                     | Known             | Unknown    |
| ------ | ------------------------ | ----------------- | ---------- |
| 1      | `itempalette.dbss`       | 6,766 B (100.0%)  | 0 B (0.0%) |
| 1      | `itempaletteoffset.dbss` | 13,528 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `0910b3dbea5e`  |
| 3482   | Layout 1 | `0910b3dbea5e`  |
| 3474   | Layout 1 | `0910b3dbea5e`  |
| 3473   | Layout 1 | `0910b3dbea5e`  |
| 3464   | Layout 1 | `0910b3dbea5e`  |
| 3458   | Layout 1 | `0910b3dbea5e`  |
| 3454   | Layout 1 | `0910b3dbea5e`  |
| 3444   | Layout 1 | `0910b3dbea5e`  |
| 3435   | Layout 1 | `0910b3dbea5e`  |
| 3426   | Layout 1 | `0910b3dbea5e`  |
| 3418   | Layout 1 | `0910b3dbea5e`  |
| 3412   | Layout 1 | `0910b3dbea5e`  |
| 3402   | Layout 1 | `0910b3dbea5e`  |
| 3396   | Layout 1 | `0910b3dbea5e`  |
| 3387   | Layout 1 | `0910b3dbea5e`  |
| 3381   | Layout 1 | `0910b3dbea5e`  |
| 3373   | Layout 1 | `0910b3dbea5e`  |
| 3364   | Layout 1 | `0910b3dbea5e`  |
| 3356   | Layout 1 | `0910b3dbea5e`  |
| 3349   | Layout 1 | `0910b3dbea5e`  |
| 3342   | Layout 1 | `0910b3dbea5e`  |
| 3335   | Layout 1 | `0910b3dbea5e`  |
| 3326   | Layout 1 | `0910b3dbea5e`  |
| 3321   | Layout 1 | `0910b3dbea5e`  |
| 3314   | Layout 1 | `0910b3dbea5e`  |
| 3303   | Layout 1 | `0910b3dbea5e`  |
| 3302   | Layout 1 | `0910b3dbea5e`  |
| 3293   | Layout 1 | `0910b3dbea5e`  |
| 3283   | Layout 1 | `0910b3dbea5e`  |
| 3275   | Layout 1 | `0910b3dbea5e`  |
| 3267   | Layout 1 | `0910b3dbea5e`  |
| 3258   | Layout 1 | `0910b3dbea5e`  |
| 3251   | Layout 1 | `0910b3dbea5e`  |
| 3242   | Layout 1 | `0910b3dbea5e`  |
| 3235   | Layout 1 | `0910b3dbea5e`  |
| 3229   | Layout 1 | `0910b3dbea5e`  |
| 3212   | Layout 1 | `0910b3dbea5e`  |
| 3203   | Layout 1 | `0910b3dbea5e`  |
| 3193   | Layout 1 | `0910b3dbea5e`  |
| 3186   | Layout 1 | `0910b3dbea5e`  |
| 3177   | Layout 1 | `0910b3dbea5e`  |
| 3169   | Layout 1 | `0910b3dbea5e`  |
| 3158   | Layout 1 | `0910b3dbea5e`  |
| 3151   | Layout 1 | `0910b3dbea5e`  |
| 3144   | Layout 1 | `0910b3dbea5e`  |
| 3133   | Layout 1 | `0910b3dbea5e`  |
| 3125   | Layout 1 | `0910b3dbea5e`  |
| 3118   | Layout 1 | `0910b3dbea5e`  |
| 3111   | Layout 1 | `0910b3dbea5e`  |
| 3103   | Layout 1 | `0910b3dbea5e`  |
| 3095   | Layout 1 | `0910b3dbea5e`  |
| 3086   | Layout 1 | `0910b3dbea5e`  |
| 3072   | Layout 1 | `0910b3dbea5e`  |
| 3062   | Layout 1 | `0910b3dbea5e`  |
| 3052   | Layout 1 | `0910b3dbea5e`  |
| 3045   | Layout 1 | `0910b3dbea5e`  |
| 3037   | Layout 1 | `0910b3dbea5e`  |
| 3030   | Layout 1 | `0910b3dbea5e`  |
| 3021   | Layout 1 | `0910b3dbea5e`  |
| 3012   | Layout 1 | `0910b3dbea5e`  |
| 3002   | Layout 1 | `0910b3dbea5e`  |
| 2995   | Layout 1 | `0910b3dbea5e`  |
| 2987   | Layout 1 | `0910b3dbea5e`  |
| 2978   | Layout 1 | `0910b3dbea5e`  |
| 2970   | Layout 1 | `0910b3dbea5e`  |
| 2959   | Layout 1 | `0910b3dbea5e`  |
| 2951   | Layout 1 | `0910b3dbea5e`  |
| 2942   | Layout 1 | `0910b3dbea5e`  |
| 2935   | Layout 1 | `0910b3dbea5e`  |
| 2932   | Layout 1 | `0910b3dbea5e`  |
| 2923   | Layout 1 | `0910b3dbea5e`  |
| 2919   | Layout 1 | `0910b3dbea5e`  |
| 2907   | Layout 1 | `0910b3dbea5e`  |
| 2900   | Layout 1 | `0910b3dbea5e`  |
| 2891   | Layout 1 | `0910b3dbea5e`  |
| 2882   | Layout 1 | `0910b3dbea5e`  |
| 2872   | Layout 1 | `0910b3dbea5e`  |
| 2863   | Layout 1 | `0910b3dbea5e`  |
| 2855   | Layout 1 | `0910b3dbea5e`  |
| 2849   | Layout 1 | `0910b3dbea5e`  |
| 2844   | Layout 1 | `0910b3dbea5e`  |
| 2834   | Layout 1 | `0910b3dbea5e`  |
| 2825   | Layout 1 | `0910b3dbea5e`  |
| 2819   | Layout 1 | `0910b3dbea5e`  |
| 2811   | Layout 1 | `0910b3dbea5e`  |
| 2803   | Layout 1 | `0910b3dbea5e`  |
| 2794   | Layout 1 | `0910b3dbea5e`  |
| 2783   | Layout 1 | `0910b3dbea5e`  |
| 2774   | Layout 1 | `0910b3dbea5e`  |
| 2765   | Layout 1 | `0910b3dbea5e`  |
| 2756   | Layout 1 | `0910b3dbea5e`  |
| 2750   | Layout 1 | `0910b3dbea5e`  |
| 2743   | Layout 1 | `0910b3dbea5e`  |
| 2736   | Layout 1 | `0910b3dbea5e`  |
| 2726   | Layout 1 | `0910b3dbea5e`  |
| 2717   | Layout 1 | `0910b3dbea5e`  |
| 2709   | Layout 1 | `0910b3dbea5e`  |
| 2703   | Layout 1 | `0910b3dbea5e`  |
| 2695   | Layout 1 | `0910b3dbea5e`  |
| 2684   | Layout 1 | `0910b3dbea5e`  |
| 2672   | Layout 1 | `0910b3dbea5e`  |
| 2665   | Layout 1 | `0910b3dbea5e`  |
| 2657   | Layout 1 | `0910b3dbea5e`  |
| 2649   | Layout 1 | `0910b3dbea5e`  |
| 2644   | Layout 1 | `0910b3dbea5e`  |
| 2637   | Layout 1 | `0910b3dbea5e`  |
| 2629   | Layout 1 | `0910b3dbea5e`  |
| 2619   | Layout 1 | `0910b3dbea5e`  |
| 2612   | Layout 1 | `0910b3dbea5e`  |
| 2606   | Layout 1 | `0910b3dbea5e`  |
| 2602   | Layout 1 | `0910b3dbea5e`  |
| 2601   | Layout 1 | `0910b3dbea5e`  |
| 2592   | Layout 1 | `0910b3dbea5e`  |
| 2583   | Layout 1 | `0910b3dbea5e`  |
| 2575   | Layout 1 | `0910b3dbea5e`  |
| 2567   | Layout 1 | `0910b3dbea5e`  |
| 2560   | Layout 1 | `0910b3dbea5e`  |
| 2553   | Layout 1 | `0910b3dbea5e`  |
| 2545   | Layout 1 | `0910b3dbea5e`  |
| 2538   | Layout 1 | `0910b3dbea5e`  |
| 2529   | Layout 1 | `0910b3dbea5e`  |
| 2519   | Layout 1 | `0910b3dbea5e`  |
| 2513   | Layout 1 | `0910b3dbea5e`  |
| 2510   | Layout 1 | `0910b3dbea5e`  |
| 2507   | Layout 1 | `0910b3dbea5e`  |
| 2503   | Layout 1 | `0910b3dbea5e`  |
| 2498   | Layout 1 | `0910b3dbea5e`  |
| 2492   | Layout 1 | `0910b3dbea5e`  |
| 2487   | Layout 1 | `0910b3dbea5e`  |
| 2480   | Layout 1 | `0910b3dbea5e`  |
| 2474   | Layout 1 | `0910b3dbea5e`  |
| 2468   | Layout 1 | `0910b3dbea5e`  |
| 2460   | Layout 1 | `0910b3dbea5e`  |
| 2453   | Layout 1 | `0910b3dbea5e`  |
| 2444   | Layout 1 | `0910b3dbea5e`  |
| 2438   | Layout 1 | `0910b3dbea5e`  |
| 2434   | Layout 1 | `0910b3dbea5e`  |
| 2429   | Layout 1 | `0910b3dbea5e`  |
| 2421   | Layout 1 | `0910b3dbea5e`  |
| 2414   | Layout 1 | `0910b3dbea5e`  |
| 2407   | Layout 1 | `0910b3dbea5e`  |
| 2401   | Layout 1 | `0910b3dbea5e`  |
| 2397   | Layout 1 | `0910b3dbea5e`  |
| 2393   | Layout 1 | `0910b3dbea5e`  |
| 2384   | Layout 1 | `0910b3dbea5e`  |
| 2378   | Layout 1 | `0910b3dbea5e`  |
| 2372   | Layout 1 | `0910b3dbea5e`  |
| 2358   | Layout 1 | `0910b3dbea5e`  |
| 2352   | Layout 1 | `0910b3dbea5e`  |
| 2347   | Layout 1 | `0910b3dbea5e`  |
| 2343   | Layout 1 | `0910b3dbea5e`  |
| 2335   | Layout 1 | `0910b3dbea5e`  |
| 2327   | Layout 1 | `0910b3dbea5e`  |
| 2324   | Layout 1 | `0910b3dbea5e`  |
| 2319   | Layout 1 | `0910b3dbea5e`  |
| 2313   | Layout 1 | `0910b3dbea5e`  |
| 2308   | Layout 1 | `0910b3dbea5e`  |
| 2302   | Layout 1 | `0910b3dbea5e`  |
| 2295   | Layout 1 | `0910b3dbea5e`  |
| 2290   | Layout 1 | `0910b3dbea5e`  |
| 2284   | Layout 1 | `0910b3dbea5e`  |
| 2276   | Layout 1 | `0910b3dbea5e`  |
| 2269   | Layout 1 | `0910b3dbea5e`  |
| 2259   | Layout 1 | `0910b3dbea5e`  |
| 2250   | Layout 1 | `0910b3dbea5e`  |
| 2243   | Layout 1 | `0910b3dbea5e`  |
| 2235   | Layout 1 | `0910b3dbea5e`  |
| 2229   | Layout 1 | `0910b3dbea5e`  |
| 2224   | Layout 1 | `0910b3dbea5e`  |
| 2218   | Layout 1 | `0910b3dbea5e`  |
| 2215   | Layout 1 | `0910b3dbea5e`  |
| 2207   | Layout 1 | `0910b3dbea5e`  |
| 2203   | Layout 1 | `0910b3dbea5e`  |
| 2196   | Layout 1 | `0910b3dbea5e`  |
| 2192   | Layout 1 | `0910b3dbea5e`  |
| 2189   | Layout 1 | `0910b3dbea5e`  |
| 2183   | Layout 1 | `0910b3dbea5e`  |
| 2179   | Layout 1 | `0910b3dbea5e`  |
| 2171   | Layout 1 | `0910b3dbea5e`  |
| 2163   | Layout 1 | `0910b3dbea5e`  |
| 2156   | Layout 1 | `0910b3dbea5e`  |
| 2151   | Layout 1 | `0910b3dbea5e`  |
| 2147   | Layout 1 | `0910b3dbea5e`  |
| 2142   | Layout 1 | `0910b3dbea5e`  |
| 2138   | Layout 1 | `0910b3dbea5e`  |
| 2134   | Layout 1 | `0910b3dbea5e`  |
| 2130   | Layout 1 | `0910b3dbea5e`  |
| 2122   | Layout 1 | `0910b3dbea5e`  |
| 2107   | Layout 1 | `0910b3dbea5e`  |
| 2098   | Layout 1 | `0910b3dbea5e`  |
| 2089   | Layout 1 | `0910b3dbea5e`  |
| 2081   | Layout 1 | `0910b3dbea5e`  |
| 2073   | Layout 1 | `0910b3dbea5e`  |
| 2067   | Layout 1 | `0910b3dbea5e`  |
| 2063   | Layout 1 | `0910b3dbea5e`  |
| 2059   | Layout 1 | `0910b3dbea5e`  |
| 2052   | Layout 1 | `0910b3dbea5e`  |
| 2044   | Layout 1 | `0910b3dbea5e`  |
| 2039   | Layout 1 | `0910b3dbea5e`  |
| 2032   | Layout 1 | `0910b3dbea5e`  |
| 2025   | Layout 1 | `0910b3dbea5e`  |
| 2011   | Layout 1 | `0910b3dbea5e`  |
| 2005   | Layout 1 | `0910b3dbea5e`  |
| 2000   | Layout 1 | `0910b3dbea5e`  |
| 1996   | Layout 1 | `0910b3dbea5e`  |
| 1991   | Layout 1 | `0910b3dbea5e`  |
| 1985   | Layout 1 | `0910b3dbea5e`  |
| 1980   | Layout 1 | `0910b3dbea5e`  |
| 1969   | Layout 1 | `0910b3dbea5e`  |
| 1964   | Layout 1 | `0910b3dbea5e`  |
| 1958   | Layout 1 | `0910b3dbea5e`  |
| 1950   | Layout 1 | `0910b3dbea5e`  |
| 1945   | Layout 1 | `0910b3dbea5e`  |
| 1937   | Layout 1 | `0910b3dbea5e`  |
| 1933   | Layout 1 | `0910b3dbea5e`  |
| 1927   | Layout 1 | `0910b3dbea5e`  |
| 1921   | Layout 1 | `0910b3dbea5e`  |
| 1914   | Layout 1 | `0910b3dbea5e`  |
| 1908   | Layout 1 | `0910b3dbea5e`  |
| 1897   | Layout 1 | `0910b3dbea5e`  |
| 1892   | Layout 1 | `0910b3dbea5e`  |
| 1886   | Layout 1 | `0910b3dbea5e`  |
| 1881   | Layout 1 | `0910b3dbea5e`  |
| 1871   | Layout 1 | `0910b3dbea5e`  |
| 1866   | Layout 1 | `0910b3dbea5e`  |
| 1862   | Layout 1 | `0910b3dbea5e`  |
| 1854   | Layout 1 | `0910b3dbea5e`  |
| 1846   | Layout 1 | `0910b3dbea5e`  |
| 1838   | Layout 1 | `0910b3dbea5e`  |
| 1832   | Layout 1 | `0910b3dbea5e`  |
| 1826   | Layout 1 | `0910b3dbea5e`  |
| 1822   | Layout 1 | `0910b3dbea5e`  |
| 1818   | Layout 1 | `0910b3dbea5e`  |
| 1804   | Layout 1 | `0910b3dbea5e`  |
| 1794   | Layout 1 | `0910b3dbea5e`  |
| 1790   | Layout 1 | `0910b3dbea5e`  |
| 1784   | Layout 1 | `0910b3dbea5e`  |
| 1774   | Layout 1 | `0910b3dbea5e`  |
| 1771   | Layout 1 | `0910b3dbea5e`  |
| 1762   | Layout 1 | `0910b3dbea5e`  |
| 1759   | Layout 1 | `0910b3dbea5e`  |
| 1754   | Layout 1 | `0910b3dbea5e`  |
| 1749   | Layout 1 | `0910b3dbea5e`  |
| 1743   | Layout 1 | `0910b3dbea5e`  |
| 1737   | Layout 1 | `0910b3dbea5e`  |
| 1731   | Layout 1 | `0910b3dbea5e`  |
| 1725   | Layout 1 | `0910b3dbea5e`  |
| 1717   | Layout 1 | `0910b3dbea5e`  |
| 1710   | Layout 1 | `0910b3dbea5e`  |
| 1704   | Layout 1 | `0910b3dbea5e`  |
| 1698   | Layout 1 | `0910b3dbea5e`  |
| 1690   | Layout 1 | `0910b3dbea5e`  |
| 1685   | Layout 1 | `0910b3dbea5e`  |
| 1680   | Layout 1 | `0910b3dbea5e`  |
| 1674   | Layout 1 | `0910b3dbea5e`  |
| 1668   | Layout 1 | `0910b3dbea5e`  |
| 1659   | Layout 1 | `0910b3dbea5e`  |
| 1649   | Layout 1 | `0910b3dbea5e`  |
| 1642   | Layout 1 | `0910b3dbea5e`  |
| 1636   | Layout 1 | `0910b3dbea5e`  |
| 1628   | Layout 1 | `0910b3dbea5e`  |
| 1622   | Layout 1 | `0910b3dbea5e`  |
| 1614   | Layout 1 | `0910b3dbea5e`  |
| 1608   | Layout 1 | `0910b3dbea5e`  |
| 1602   | Layout 1 | `0910b3dbea5e`  |
| 1598   | Layout 1 | `0910b3dbea5e`  |
| 1594   | Layout 1 | `0910b3dbea5e`  |
| 1590   | Layout 1 | `0910b3dbea5e`  |
| 1587   | Layout 1 | `0910b3dbea5e`  |
| 1584   | Layout 1 | `0910b3dbea5e`  |
| 1579   | Layout 1 | `0910b3dbea5e`  |
| 1572   | Layout 1 | `0910b3dbea5e`  |
| 1565   | Layout 1 | `0910b3dbea5e`  |
| 1559   | Layout 1 | `0910b3dbea5e`  |
| 1554   | Layout 1 | `0910b3dbea5e`  |
| 1547   | Layout 1 | `0910b3dbea5e`  |
| 1537   | Layout 1 | `0910b3dbea5e`  |
| 1529   | Layout 1 | `0910b3dbea5e`  |
| 1524   | Layout 1 | `0910b3dbea5e`  |
| 1519   | Layout 1 | `0910b3dbea5e`  |
| 1509   | Layout 1 | `0910b3dbea5e`  |
| 1506   | Layout 1 | `0910b3dbea5e`  |
| 1504   | Layout 1 | `0910b3dbea5e`  |
| 1500   | Layout 1 | `0910b3dbea5e`  |
| 1493   | Layout 1 | `0910b3dbea5e`  |
| 1489   | Layout 1 | `0910b3dbea5e`  |
| 1485   | Layout 1 | `0910b3dbea5e`  |
| 1481   | Layout 1 | `0910b3dbea5e`  |
| 1474   | Layout 1 | `0910b3dbea5e`  |
| 1466   | Layout 1 | `0910b3dbea5e`  |
| 1462   | Layout 1 | `0910b3dbea5e`  |
| 1459   | Layout 1 | `0910b3dbea5e`  |
| 1453   | Layout 1 | `0910b3dbea5e`  |
| 1450   | Layout 1 | `0910b3dbea5e`  |
| 1445   | Layout 1 | `0910b3dbea5e`  |
| 1439   | Layout 1 | `0910b3dbea5e`  |
| 1433   | Layout 1 | `0910b3dbea5e`  |
| 1430   | Layout 1 | `0910b3dbea5e`  |
| 1426   | Layout 1 | `0910b3dbea5e`  |
| 1421   | Layout 1 | `0910b3dbea5e`  |
| 1417   | Layout 1 | `0910b3dbea5e`  |
| 1416   | Layout 1 | `0910b3dbea5e`  |
| 1409   | Layout 1 | `0910b3dbea5e`  |
| 1405   | Layout 1 | `0910b3dbea5e`  |
| 1401   | Layout 1 | `0910b3dbea5e`  |
| 1396   | Layout 1 | `0910b3dbea5e`  |
| 1391   | Layout 1 | `0910b3dbea5e`  |
| 1390   | Layout 1 | `0910b3dbea5e`  |
| 1386   | Layout 1 | `0910b3dbea5e`  |
| 1381   | Layout 1 | `0910b3dbea5e`  |
| 1379   | Layout 1 | `0910b3dbea5e`  |
| 1372   | Layout 1 | `0910b3dbea5e`  |
| 1366   | Layout 1 | `0910b3dbea5e`  |
| 1364   | Layout 1 | `0910b3dbea5e`  |
| 1363   | Layout 1 | `0910b3dbea5e`  |
| 1360   | Layout 1 | `0910b3dbea5e`  |
| 1358   | Layout 1 | `0910b3dbea5e`  |
| 1355   | Layout 1 | `0910b3dbea5e`  |
| 1351   | Layout 1 | `0910b3dbea5e`  |
| 1348   | Layout 1 | `0910b3dbea5e`  |
| 1346   | Layout 1 | `0910b3dbea5e`  |
| 1341   | Layout 1 | `0910b3dbea5e`  |
| 1340   | Layout 1 | `0910b3dbea5e`  |
| 1338   | Layout 1 | `0910b3dbea5e`  |
| 1335   | Layout 1 | `0910b3dbea5e`  |
| 1333   | Layout 1 | `0910b3dbea5e`  |
| 1329   | Layout 1 | `0910b3dbea5e`  |
| 1327   | Layout 1 | `0910b3dbea5e`  |
| 1324   | Layout 1 | `0910b3dbea5e`  |
| 1321   | Layout 1 | `0910b3dbea5e`  |
| 1319   | Layout 1 | `0910b3dbea5e`  |
| 1318   | Layout 1 | `0910b3dbea5e`  |
| 1316   | Layout 1 | `0910b3dbea5e`  |
| 1313   | Layout 1 | `0910b3dbea5e`  |
| 1311   | Layout 1 | `0910b3dbea5e`  |
| 1309   | Layout 1 | `0910b3dbea5e`  |
| 1304   | Layout 1 | `0910b3dbea5e`  |
| 1292   | Layout 1 | `0910b3dbea5e`  |
| 1286   | Layout 1 | `0910b3dbea5e`  |
| 1280   | Layout 1 | `0910b3dbea5e`  |
| 1276   | Layout 1 | `0910b3dbea5e`  |
| 1267   | No file  | `0910b3dbea5e`  |
| 1261   | No file  | `0910b3dbea5e`  |
| 1256   | No file  | `0910b3dbea5e`  |
| 1250   | No file  | `0910b3dbea5e`  |
| 1246   | No file  | `0910b3dbea5e`  |
| 1239   | No file  | `0910b3dbea5e`  |
| 1230   | No file  | `0910b3dbea5e`  |
| 1226   | No file  | `0910b3dbea5e`  |
| 1220   | No file  | `0910b3dbea5e`  |
| 1217   | No file  | `0910b3dbea5e`  |
| 1211   | No file  | `0910b3dbea5e`  |
| 1210   | No file  | `0910b3dbea5e`  |
| 1208   | No file  | `0910b3dbea5e`  |
| 1203   | No file  | `0910b3dbea5e`  |
| 1197   | No file  | `0910b3dbea5e`  |
| 1194   | No file  | `0910b3dbea5e`  |
| 1192   | No file  | `0910b3dbea5e`  |
| 1187   | No file  | `0910b3dbea5e`  |
| 1183   | No file  | `0910b3dbea5e`  |
| 1177   | No file  | `0910b3dbea5e`  |
| 1173   | No file  | `0910b3dbea5e`  |
| 1167   | No file  | `0910b3dbea5e`  |
| 1164   | No file  | `0910b3dbea5e`  |
| 1156   | No file  | `0910b3dbea5e`  |
| 1149   | No file  | `0910b3dbea5e`  |
| 1144   | No file  | `0910b3dbea5e`  |
| 1137   | No file  | `0910b3dbea5e`  |
| 1132   | No file  | `0910b3dbea5e`  |
| 1127   | No file  | `0910b3dbea5e`  |
| 1122   | No file  | `0910b3dbea5e`  |
| 1118   | No file  | `0910b3dbea5e`  |
| 1114   | No file  | `0910b3dbea5e`  |
| 1109   | No file  | `0910b3dbea5e`  |
| 1102   | No file  | `0910b3dbea5e`  |
| 1096   | No file  | `0910b3dbea5e`  |
| 1088   | No file  | `0910b3dbea5e`  |
| 1081   | No file  | `0910b3dbea5e`  |
| 1076   | No file  | `0910b3dbea5e`  |
| 1069   | No file  | `0910b3dbea5e`  |
| 1064   | No file  | `0910b3dbea5e`  |
| 1058   | No file  | `0910b3dbea5e`  |
| 1051   | No file  | `0910b3dbea5e`  |
| 1044   | No file  | `0910b3dbea5e`  |
| 1036   | No file  | `0910b3dbea5e`  |
| 1026   | No file  | `0910b3dbea5e`  |
| 1016   | No file  | `0910b3dbea5e`  |
| 1009   | No file  | `0910b3dbea5e`  |
| 1005   | No file  | `0910b3dbea5e`  |
| 1000   | No file  | `0910b3dbea5e`  |
| 998    | No file  | `0910b3dbea5e`  |
| 990    | No file  | `0910b3dbea5e`  |
| 979    | No file  | `0910b3dbea5e`  |
| 972    | No file  | `0910b3dbea5e`  |
| 963    | No file  | `0910b3dbea5e`  |
| 955    | No file  | `0910b3dbea5e`  |
| 946    | No file  | `0910b3dbea5e`  |
| 938    | No file  | `0910b3dbea5e`  |
| 927    | No file  | `0910b3dbea5e`  |
| 911    | No file  | `0910b3dbea5e`  |
| 904    | No file  | `0910b3dbea5e`  |
| 899    | No file  | `0910b3dbea5e`  |
| 894    | No file  | `0910b3dbea5e`  |
| 885    | No file  | `0910b3dbea5e`  |
| 879    | No file  | `0910b3dbea5e`  |
| 872    | No file  | `0910b3dbea5e`  |
| 864    | No file  | `0910b3dbea5e`  |
| 855    | No file  | `0910b3dbea5e`  |
| 853    | No file  | `0910b3dbea5e`  |
| 845    | No file  | `0910b3dbea5e`  |
| 837    | No file  | `0910b3dbea5e`  |
| 829    | No file  | `0910b3dbea5e`  |
| 822    | No file  | `0910b3dbea5e`  |
| 814    | No file  | `0910b3dbea5e`  |
| 805    | No file  | `0910b3dbea5e`  |
| 794    | No file  | `0910b3dbea5e`  |
| 787    | No file  | `0910b3dbea5e`  |
| 780    | No file  | `0910b3dbea5e`  |
| 771    | No file  | `0910b3dbea5e`  |
| 760    | No file  | `0910b3dbea5e`  |
| 748    | No file  | `0910b3dbea5e`  |
| 741    | No file  | `0910b3dbea5e`  |
| 736    | No file  | `0910b3dbea5e`  |
| 731    | No file  | `0910b3dbea5e`  |
| 723    | No file  | `0910b3dbea5e`  |
| 711    | No file  | `0910b3dbea5e`  |
| 707    | No file  | `0910b3dbea5e`  |
| 697    | No file  | `0910b3dbea5e`  |
| 689    | No file  | `0910b3dbea5e`  |
| 683    | No file  | `0910b3dbea5e`  |
| 678    | No file  | `0910b3dbea5e`  |
| 670    | No file  | `0910b3dbea5e`  |
| 661    | No file  | `0910b3dbea5e`  |
| 656    | No file  | `0910b3dbea5e`  |
| 652    | No file  | `0910b3dbea5e`  |
| 643    | No file  | `0910b3dbea5e`  |
| 637    | No file  | `0910b3dbea5e`  |
| 630    | No file  | `0910b3dbea5e`  |
| 627    | No file  | `0910b3dbea5e`  |
| 621    | No file  | `0910b3dbea5e`  |
| 617    | No file  | `0910b3dbea5e`  |
| 615    | No file  | `0910b3dbea5e`  |
| 606    | No file  | `0910b3dbea5e`  |
| 599    | No file  | `0910b3dbea5e`  |
| 592    | No file  | `0910b3dbea5e`  |
| 586    | No file  | `0910b3dbea5e`  |
| 577    | No file  | `0910b3dbea5e`  |
| 569    | No file  | `0910b3dbea5e`  |
| 561    | No file  | `0910b3dbea5e`  |
| 554    | No file  | `0910b3dbea5e`  |
| 542    | No file  | `0910b3dbea5e`  |
| 532    | No file  | `0910b3dbea5e`  |
| 531    | No file  | `0910b3dbea5e`  |
| 526    | No file  | `0910b3dbea5e`  |
| 521    | No file  | `0910b3dbea5e`  |
| 517    | No file  | `0910b3dbea5e`  |
| 510    | No file  | `0910b3dbea5e`  |
| 508    | No file  | `0910b3dbea5e`  |
| 504    | No file  | `0910b3dbea5e`  |
| 497    | No file  | `0910b3dbea5e`  |
| 491    | No file  | `0910b3dbea5e`  |
| 485    | No file  | `0910b3dbea5e`  |
| 478    | No file  | `0910b3dbea5e`  |
| 472    | No file  | `0910b3dbea5e`  |
| 466    | No file  | `0910b3dbea5e`  |
| 457    | No file  | `0910b3dbea5e`  |
| 452    | No file  | `0910b3dbea5e`  |
| 449    | No file  | `0910b3dbea5e`  |
| 435    | No file  | `0910b3dbea5e`  |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                                          |
| ------------------------ | -------- | ----------------------------------------------------------------------------- |
| `itempaletteoffset.dbss` | Optional | `item_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `dyeingpalette.dbss`     | Optional | The colour at `palette_type` and `palette_index`, for the Color column         |
| `languagedata_en.loc`    | Optional | Item names (type `0`) and the dye window's tab names (type `37`)               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 1,127 x 6 = 6,766 bytes.

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                                                  |
| ------- | ---- | ------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key      | The dye item, an item enchant key (`enchant_level << 24 \| item_id`); level `0` on every row of clients 1784 and 3474 |
| `+0x04` | u8   | palette_type  | `palette_type` of a [`dyeingpalette.dbss`](dyeingpalette_dbss.md) row; `1` to `8`      |
| `+0x05` | u8   | palette_index | Position of the colour in that row's `colors`, from 0                                  |

The rows are not sorted by key.

### `itempaletteoffset.dbss`

Bare offset table into `itempalette.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `itempalette.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                  |
| ------- | ---- | ----------- | ------------------------------------------------------ |
| `+0x00` | u32  | item_key    | Key of the row it points at                            |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `itempalette.dbss`, at its `item_key` |
| `+0x08` | u32  | data_size   | `6` on every row: the whole row                        |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in another order than the file; on clients 1784 and 3474
every index row points at the row with its key.

## Palette Types

The dye window (`panel_window_dyeingpalette_renew.luac`) names its tabs
`LUA_PALETTE_TAB_MATERIAL_0` to `LUA_PALETTE_TAB_MATERIAL_7`, and the dye
items of palette type N are the dyes of tab N - 1: type `2` holds the
`[Olvian Dye]` items, type `8` the `[Valencian Dye]` items.

| Type | Tab (LOC English) | Rows (client 3474) |
| ---- | ----------------- | ------------------ |
| 1    | Basic Dye         | 196                |
| 2    | Olvian Dye        | 133                |
| 3    | Velian Dye        | 133                |
| 4    | Heidelian Dye     | 133                |
| 5    | Keplanian Dye     | 133                |
| 6    | Calpheonian Dye   | 133                |
| 7    | Mediahn Dye       | 133                |
| 8    | Valencian Dye     | 133                |

## Field Names

The 2016 client's debug symbols have `gc::ItemPaletteStaticStatus` as
`_key` (a `gc::ItemEnchantKey`), `_paletteType` and `_paletteIndex`, then a
pointer to the `gc::DyeingPaletteStaticStauts` (sic) it resolves to; the
file holds the first three. The `DyeingItem_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784 has the columns `ItemKey`,
`PaletteType` and `PaletteIndex`, and its 1,127 rows match the file on all
1,127 keys and both values, on client 1784 and on client 3474.

## Notes

- On client 3474, 1,119 of the 1,161 `dyeingpalette.dbss` colours have a
  dye item; 8 of them have two.
- Every row of clients 1784 and 3474 points at a colour that
  `dyeingpalette.dbss` holds.
