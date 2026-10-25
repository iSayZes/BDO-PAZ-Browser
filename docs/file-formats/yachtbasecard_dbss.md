# `yachtbasecard.dbss` Format

## Purpose

The cards on the faces of the Yar! dice: each row is one card, its symbol,
its eye value (`1` to `6`) and the `UI_Artwork` picture the card shows.
[`yachtdice.dbss`](yachtdice_dbss.md) lists six cards per die.
`yachtbasecardoffset.dbss` is the index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes | Records       | Row bytes |
| ------ | -------------- | -------------------------- | ----- | ------------- | --------- |
| 1      | 1680 and later | `yachtbasecard.dbss`       | 1,924 | 30 Row        | 64        |
| 1      | 1680 and later | `yachtbasecardoffset.dbss` | 364   | 30 Offset Row | 12        |

| Layout | File                       | Known            | Unknown    |
| ------ | -------------------------- | ---------------- | ---------- |
| 1      | `yachtbasecard.dbss`       | 1,924 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtbasecardoffset.dbss` | 364 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `8b4a8133d4a8`  |
| 3482   | Layout 1 | `8b4a8133d4a8`  |
| 3474   | Layout 1 | `8b4a8133d4a8`  |
| 3473   | Layout 1 | `8b4a8133d4a8`  |
| 3464   | Layout 1 | `8b4a8133d4a8`  |
| 3458   | Layout 1 | `8b4a8133d4a8`  |
| 3454   | Layout 1 | `8b4a8133d4a8`  |
| 3444   | Layout 1 | `8b4a8133d4a8`  |
| 3435   | Layout 1 | `8b4a8133d4a8`  |
| 3426   | Layout 1 | `8b4a8133d4a8`  |
| 3418   | Layout 1 | `8b4a8133d4a8`  |
| 3412   | Layout 1 | `8b4a8133d4a8`  |
| 3402   | Layout 1 | `8b4a8133d4a8`  |
| 3396   | Layout 1 | `8b4a8133d4a8`  |
| 3387   | Layout 1 | `8b4a8133d4a8`  |
| 3381   | Layout 1 | `8b4a8133d4a8`  |
| 3373   | Layout 1 | `8b4a8133d4a8`  |
| 3364   | Layout 1 | `8b4a8133d4a8`  |
| 3356   | Layout 1 | `8b4a8133d4a8`  |
| 3349   | Layout 1 | `8b4a8133d4a8`  |
| 3342   | Layout 1 | `8b4a8133d4a8`  |
| 3335   | Layout 1 | `8b4a8133d4a8`  |
| 3326   | Layout 1 | `8b4a8133d4a8`  |
| 3321   | Layout 1 | `8b4a8133d4a8`  |
| 3314   | Layout 1 | `8b4a8133d4a8`  |
| 3303   | Layout 1 | `8b4a8133d4a8`  |
| 3302   | Layout 1 | `8b4a8133d4a8`  |
| 3293   | Layout 1 | `8b4a8133d4a8`  |
| 3283   | Layout 1 | `8b4a8133d4a8`  |
| 3275   | Layout 1 | `8b4a8133d4a8`  |
| 3267   | Layout 1 | `8b4a8133d4a8`  |
| 3258   | Layout 1 | `8b4a8133d4a8`  |
| 3251   | Layout 1 | `8b4a8133d4a8`  |
| 3242   | Layout 1 | `8b4a8133d4a8`  |
| 3235   | Layout 1 | `8b4a8133d4a8`  |
| 3229   | Layout 1 | `8b4a8133d4a8`  |
| 3212   | Layout 1 | `8b4a8133d4a8`  |
| 3203   | Layout 1 | `8b4a8133d4a8`  |
| 3193   | Layout 1 | `8b4a8133d4a8`  |
| 3186   | Layout 1 | `8b4a8133d4a8`  |
| 3177   | Layout 1 | `8b4a8133d4a8`  |
| 3169   | Layout 1 | `8b4a8133d4a8`  |
| 3158   | Layout 1 | `8b4a8133d4a8`  |
| 3151   | Layout 1 | `8b4a8133d4a8`  |
| 3144   | Layout 1 | `8b4a8133d4a8`  |
| 3133   | Layout 1 | `8b4a8133d4a8`  |
| 3125   | Layout 1 | `8b4a8133d4a8`  |
| 3118   | Layout 1 | `8b4a8133d4a8`  |
| 3111   | Layout 1 | `8b4a8133d4a8`  |
| 3103   | Layout 1 | `8b4a8133d4a8`  |
| 3095   | Layout 1 | `8b4a8133d4a8`  |
| 3086   | Layout 1 | `8b4a8133d4a8`  |
| 3072   | Layout 1 | `8b4a8133d4a8`  |
| 3062   | Layout 1 | `8b4a8133d4a8`  |
| 3052   | Layout 1 | `8b4a8133d4a8`  |
| 3045   | Layout 1 | `8b4a8133d4a8`  |
| 3037   | Layout 1 | `8b4a8133d4a8`  |
| 3030   | Layout 1 | `8b4a8133d4a8`  |
| 3021   | Layout 1 | `8b4a8133d4a8`  |
| 3012   | Layout 1 | `8b4a8133d4a8`  |
| 3002   | Layout 1 | `8b4a8133d4a8`  |
| 2995   | Layout 1 | `8b4a8133d4a8`  |
| 2987   | Layout 1 | `8b4a8133d4a8`  |
| 2978   | Layout 1 | `8b4a8133d4a8`  |
| 2970   | Layout 1 | `8b4a8133d4a8`  |
| 2959   | Layout 1 | `8b4a8133d4a8`  |
| 2951   | Layout 1 | `8b4a8133d4a8`  |
| 2942   | Layout 1 | `8b4a8133d4a8`  |
| 2935   | Layout 1 | `8b4a8133d4a8`  |
| 2932   | Layout 1 | `8b4a8133d4a8`  |
| 2923   | Layout 1 | `8b4a8133d4a8`  |
| 2919   | Layout 1 | `8b4a8133d4a8`  |
| 2907   | Layout 1 | `8b4a8133d4a8`  |
| 2900   | Layout 1 | `8b4a8133d4a8`  |
| 2891   | Layout 1 | `8b4a8133d4a8`  |
| 2882   | Layout 1 | `8b4a8133d4a8`  |
| 2872   | Layout 1 | `8b4a8133d4a8`  |
| 2863   | Layout 1 | `8b4a8133d4a8`  |
| 2855   | Layout 1 | `8b4a8133d4a8`  |
| 2849   | Layout 1 | `8b4a8133d4a8`  |
| 2844   | Layout 1 | `8b4a8133d4a8`  |
| 2834   | Layout 1 | `8b4a8133d4a8`  |
| 2825   | Layout 1 | `8b4a8133d4a8`  |
| 2819   | Layout 1 | `8b4a8133d4a8`  |
| 2811   | Layout 1 | `8b4a8133d4a8`  |
| 2803   | Layout 1 | `8b4a8133d4a8`  |
| 2794   | Layout 1 | `8b4a8133d4a8`  |
| 2783   | Layout 1 | `8b4a8133d4a8`  |
| 2774   | Layout 1 | `8b4a8133d4a8`  |
| 2765   | Layout 1 | `8b4a8133d4a8`  |
| 2756   | Layout 1 | `8b4a8133d4a8`  |
| 2750   | Layout 1 | `8b4a8133d4a8`  |
| 2743   | Layout 1 | `8b4a8133d4a8`  |
| 2736   | Layout 1 | `8b4a8133d4a8`  |
| 2726   | Layout 1 | `8b4a8133d4a8`  |
| 2717   | Layout 1 | `8b4a8133d4a8`  |
| 2709   | Layout 1 | `8b4a8133d4a8`  |
| 2703   | Layout 1 | `8b4a8133d4a8`  |
| 2695   | Layout 1 | `8b4a8133d4a8`  |
| 2684   | Layout 1 | `8b4a8133d4a8`  |
| 2672   | Layout 1 | `8b4a8133d4a8`  |
| 2665   | Layout 1 | `8b4a8133d4a8`  |
| 2657   | Layout 1 | `8b4a8133d4a8`  |
| 2649   | Layout 1 | `8b4a8133d4a8`  |
| 2644   | Layout 1 | `8b4a8133d4a8`  |
| 2637   | Layout 1 | `8b4a8133d4a8`  |
| 2629   | Layout 1 | `8b4a8133d4a8`  |
| 2619   | Layout 1 | `8b4a8133d4a8`  |
| 2612   | Layout 1 | `8b4a8133d4a8`  |
| 2606   | Layout 1 | `8b4a8133d4a8`  |
| 2602   | Layout 1 | `8b4a8133d4a8`  |
| 2601   | Layout 1 | `8b4a8133d4a8`  |
| 2592   | Layout 1 | `8b4a8133d4a8`  |
| 2583   | Layout 1 | `8b4a8133d4a8`  |
| 2575   | Layout 1 | `8b4a8133d4a8`  |
| 2567   | Layout 1 | `8b4a8133d4a8`  |
| 2560   | Layout 1 | `8b4a8133d4a8`  |
| 2553   | Layout 1 | `8b4a8133d4a8`  |
| 2545   | Layout 1 | `8b4a8133d4a8`  |
| 2538   | Layout 1 | `8b4a8133d4a8`  |
| 2529   | Layout 1 | `8b4a8133d4a8`  |
| 2519   | Layout 1 | `8b4a8133d4a8`  |
| 2513   | Layout 1 | `8b4a8133d4a8`  |
| 2510   | Layout 1 | `8b4a8133d4a8`  |
| 2507   | Layout 1 | `8b4a8133d4a8`  |
| 2503   | Layout 1 | `8b4a8133d4a8`  |
| 2498   | Layout 1 | `8b4a8133d4a8`  |
| 2492   | Layout 1 | `8b4a8133d4a8`  |
| 2487   | Layout 1 | `8b4a8133d4a8`  |
| 2480   | Layout 1 | `8b4a8133d4a8`  |
| 2474   | Layout 1 | `8b4a8133d4a8`  |
| 2468   | Layout 1 | `8b4a8133d4a8`  |
| 2460   | Layout 1 | `8b4a8133d4a8`  |
| 2453   | Layout 1 | `8b4a8133d4a8`  |
| 2444   | Layout 1 | `8b4a8133d4a8`  |
| 2438   | Layout 1 | `8b4a8133d4a8`  |
| 2434   | Layout 1 | `8b4a8133d4a8`  |
| 2429   | Layout 1 | `8b4a8133d4a8`  |
| 2421   | Layout 1 | `8b4a8133d4a8`  |
| 2414   | Layout 1 | `8b4a8133d4a8`  |
| 2407   | Layout 1 | `8b4a8133d4a8`  |
| 2401   | Layout 1 | `8b4a8133d4a8`  |
| 2397   | Layout 1 | `8b4a8133d4a8`  |
| 2393   | Layout 1 | `8b4a8133d4a8`  |
| 2384   | Layout 1 | `8b4a8133d4a8`  |
| 2378   | Layout 1 | `8b4a8133d4a8`  |
| 2372   | Layout 1 | `8b4a8133d4a8`  |
| 2358   | Layout 1 | `8b4a8133d4a8`  |
| 2352   | Layout 1 | `8b4a8133d4a8`  |
| 2347   | Layout 1 | `8b4a8133d4a8`  |
| 2343   | Layout 1 | `8b4a8133d4a8`  |
| 2335   | Layout 1 | `8b4a8133d4a8`  |
| 2327   | Layout 1 | `8b4a8133d4a8`  |
| 2324   | Layout 1 | `8b4a8133d4a8`  |
| 2319   | Layout 1 | `8b4a8133d4a8`  |
| 2313   | Layout 1 | `8b4a8133d4a8`  |
| 2308   | Layout 1 | `8b4a8133d4a8`  |
| 2302   | Layout 1 | `8b4a8133d4a8`  |
| 2295   | Layout 1 | `8b4a8133d4a8`  |
| 2290   | Layout 1 | `8b4a8133d4a8`  |
| 2284   | Layout 1 | `8b4a8133d4a8`  |
| 2276   | Layout 1 | `8b4a8133d4a8`  |
| 2269   | Layout 1 | `8b4a8133d4a8`  |
| 2259   | Layout 1 | `8b4a8133d4a8`  |
| 2250   | Layout 1 | `8b4a8133d4a8`  |
| 2243   | Layout 1 | `8b4a8133d4a8`  |
| 2235   | Layout 1 | `8b4a8133d4a8`  |
| 2229   | Layout 1 | `8b4a8133d4a8`  |
| 2224   | Layout 1 | `8b4a8133d4a8`  |
| 2218   | Layout 1 | `8b4a8133d4a8`  |
| 2215   | Layout 1 | `8b4a8133d4a8`  |
| 2207   | Layout 1 | `8b4a8133d4a8`  |
| 2203   | Layout 1 | `8b4a8133d4a8`  |
| 2196   | Layout 1 | `8b4a8133d4a8`  |
| 2192   | Layout 1 | `8b4a8133d4a8`  |
| 2189   | Layout 1 | `8b4a8133d4a8`  |
| 2183   | Layout 1 | `8b4a8133d4a8`  |
| 2179   | Layout 1 | `8b4a8133d4a8`  |
| 2171   | Layout 1 | `8b4a8133d4a8`  |
| 2163   | Layout 1 | `8b4a8133d4a8`  |
| 2156   | Layout 1 | `8b4a8133d4a8`  |
| 2151   | Layout 1 | `8b4a8133d4a8`  |
| 2147   | Layout 1 | `8b4a8133d4a8`  |
| 2142   | Layout 1 | `8b4a8133d4a8`  |
| 2138   | Layout 1 | `8b4a8133d4a8`  |
| 2134   | Layout 1 | `8b4a8133d4a8`  |
| 2130   | Layout 1 | `8b4a8133d4a8`  |
| 2122   | Layout 1 | `8b4a8133d4a8`  |
| 2107   | Layout 1 | `8b4a8133d4a8`  |
| 2098   | Layout 1 | `8b4a8133d4a8`  |
| 2089   | Layout 1 | `8b4a8133d4a8`  |
| 2081   | Layout 1 | `8b4a8133d4a8`  |
| 2073   | Layout 1 | `8b4a8133d4a8`  |
| 2067   | Layout 1 | `8b4a8133d4a8`  |
| 2063   | Layout 1 | `8b4a8133d4a8`  |
| 2059   | Layout 1 | `8b4a8133d4a8`  |
| 2052   | Layout 1 | `8b4a8133d4a8`  |
| 2044   | Layout 1 | `8b4a8133d4a8`  |
| 2039   | Layout 1 | `8b4a8133d4a8`  |
| 2032   | Layout 1 | `8b4a8133d4a8`  |
| 2025   | Layout 1 | `8b4a8133d4a8`  |
| 2011   | Layout 1 | `8b4a8133d4a8`  |
| 2005   | Layout 1 | `8b4a8133d4a8`  |
| 2000   | Layout 1 | `8b4a8133d4a8`  |
| 1996   | Layout 1 | `8b4a8133d4a8`  |
| 1991   | Layout 1 | `8b4a8133d4a8`  |
| 1985   | Layout 1 | `8b4a8133d4a8`  |
| 1980   | Layout 1 | `8b4a8133d4a8`  |
| 1969   | Layout 1 | `8b4a8133d4a8`  |
| 1964   | Layout 1 | `8b4a8133d4a8`  |
| 1958   | Layout 1 | `8b4a8133d4a8`  |
| 1950   | Layout 1 | `8b4a8133d4a8`  |
| 1945   | Layout 1 | `8b4a8133d4a8`  |
| 1937   | Layout 1 | `8b4a8133d4a8`  |
| 1933   | Layout 1 | `8b4a8133d4a8`  |
| 1927   | Layout 1 | `8b4a8133d4a8`  |
| 1921   | Layout 1 | `8b4a8133d4a8`  |
| 1914   | Layout 1 | `8b4a8133d4a8`  |
| 1908   | Layout 1 | `8b4a8133d4a8`  |
| 1897   | Layout 1 | `8b4a8133d4a8`  |
| 1892   | Layout 1 | `8b4a8133d4a8`  |
| 1886   | Layout 1 | `8b4a8133d4a8`  |
| 1881   | Layout 1 | `8b4a8133d4a8`  |
| 1871   | Layout 1 | `8b4a8133d4a8`  |
| 1866   | Layout 1 | `8b4a8133d4a8`  |
| 1862   | Layout 1 | `8b4a8133d4a8`  |
| 1854   | Layout 1 | `8b4a8133d4a8`  |
| 1846   | Layout 1 | `8b4a8133d4a8`  |
| 1838   | Layout 1 | `8b4a8133d4a8`  |
| 1832   | Layout 1 | `8b4a8133d4a8`  |
| 1826   | Layout 1 | `8b4a8133d4a8`  |
| 1822   | Layout 1 | `8b4a8133d4a8`  |
| 1818   | Layout 1 | `8b4a8133d4a8`  |
| 1804   | Layout 1 | `8b4a8133d4a8`  |
| 1794   | Layout 1 | `8b4a8133d4a8`  |
| 1790   | Layout 1 | `8b4a8133d4a8`  |
| 1784   | Layout 1 | `8b4a8133d4a8`  |
| 1774   | Layout 1 | `8b4a8133d4a8`  |
| 1771   | Layout 1 | `8b4a8133d4a8`  |
| 1762   | Layout 1 | `8b4a8133d4a8`  |
| 1759   | Layout 1 | `8b4a8133d4a8`  |
| 1754   | Layout 1 | `8b4a8133d4a8`  |
| 1749   | Layout 1 | `8b4a8133d4a8`  |
| 1743   | Layout 1 | `8b4a8133d4a8`  |
| 1737   | Layout 1 | `8b4a8133d4a8`  |
| 1731   | Layout 1 | `8b4a8133d4a8`  |
| 1725   | Layout 1 | `8b4a8133d4a8`  |
| 1717   | Layout 1 | `8b4a8133d4a8`  |
| 1710   | Layout 1 | `8b4a8133d4a8`  |
| 1704   | Layout 1 | `8b4a8133d4a8`  |
| 1698   | Layout 1 | `8b4a8133d4a8`  |
| 1690   | Layout 1 | `8b4a8133d4a8`  |
| 1685   | Layout 1 | `8b4a8133d4a8`  |
| 1680   | Layout 1 | `8b4a8133d4a8`  |
| 1674   | No file  | `8b4a8133d4a8`  |
| 1668   | No file  | `8b4a8133d4a8`  |
| 1659   | No file  | `8b4a8133d4a8`  |
| 1649   | No file  | `8b4a8133d4a8`  |
| 1642   | No file  | `8b4a8133d4a8`  |
| 1636   | No file  | `8b4a8133d4a8`  |
| 1628   | No file  | `8b4a8133d4a8`  |
| 1622   | No file  | `8b4a8133d4a8`  |
| 1614   | No file  | `8b4a8133d4a8`  |
| 1608   | No file  | `8b4a8133d4a8`  |
| 1602   | No file  | `8b4a8133d4a8`  |
| 1598   | No file  | `8b4a8133d4a8`  |
| 1594   | No file  | `8b4a8133d4a8`  |
| 1590   | No file  | `8b4a8133d4a8`  |
| 1587   | No file  | `8b4a8133d4a8`  |
| 1584   | No file  | `8b4a8133d4a8`  |
| 1579   | No file  | `8b4a8133d4a8`  |
| 1572   | No file  | `8b4a8133d4a8`  |
| 1565   | No file  | `8b4a8133d4a8`  |
| 1559   | No file  | `8b4a8133d4a8`  |
| 1554   | No file  | `8b4a8133d4a8`  |
| 1547   | No file  | `8b4a8133d4a8`  |
| 1537   | No file  | `8b4a8133d4a8`  |
| 1529   | No file  | `8b4a8133d4a8`  |
| 1524   | No file  | `8b4a8133d4a8`  |
| 1519   | No file  | `8b4a8133d4a8`  |
| 1509   | No file  | `8b4a8133d4a8`  |
| 1506   | No file  | `8b4a8133d4a8`  |
| 1504   | No file  | `8b4a8133d4a8`  |
| 1500   | No file  | `8b4a8133d4a8`  |
| 1493   | No file  | `8b4a8133d4a8`  |
| 1489   | No file  | `8b4a8133d4a8`  |
| 1485   | No file  | `8b4a8133d4a8`  |
| 1481   | No file  | `8b4a8133d4a8`  |
| 1474   | No file  | `8b4a8133d4a8`  |
| 1466   | No file  | `8b4a8133d4a8`  |
| 1462   | No file  | `8b4a8133d4a8`  |
| 1459   | No file  | `8b4a8133d4a8`  |
| 1453   | No file  | `8b4a8133d4a8`  |
| 1450   | No file  | `8b4a8133d4a8`  |
| 1445   | No file  | `8b4a8133d4a8`  |
| 1439   | No file  | `8b4a8133d4a8`  |
| 1433   | No file  | `8b4a8133d4a8`  |
| 1430   | No file  | `8b4a8133d4a8`  |
| 1426   | No file  | `8b4a8133d4a8`  |
| 1421   | No file  | `8b4a8133d4a8`  |
| 1417   | No file  | `8b4a8133d4a8`  |
| 1416   | No file  | `8b4a8133d4a8`  |
| 1409   | No file  | `8b4a8133d4a8`  |
| 1405   | No file  | `8b4a8133d4a8`  |
| 1401   | No file  | `8b4a8133d4a8`  |
| 1396   | No file  | `8b4a8133d4a8`  |
| 1391   | No file  | `8b4a8133d4a8`  |
| 1390   | No file  | `8b4a8133d4a8`  |
| 1386   | No file  | `8b4a8133d4a8`  |
| 1381   | No file  | `8b4a8133d4a8`  |
| 1379   | No file  | `8b4a8133d4a8`  |
| 1372   | No file  | `8b4a8133d4a8`  |
| 1366   | No file  | `8b4a8133d4a8`  |
| 1364   | No file  | `8b4a8133d4a8`  |
| 1363   | No file  | `8b4a8133d4a8`  |
| 1360   | No file  | `8b4a8133d4a8`  |
| 1358   | No file  | `8b4a8133d4a8`  |
| 1355   | No file  | `8b4a8133d4a8`  |
| 1351   | No file  | `8b4a8133d4a8`  |
| 1348   | No file  | `8b4a8133d4a8`  |
| 1346   | No file  | `8b4a8133d4a8`  |
| 1341   | No file  | `8b4a8133d4a8`  |
| 1340   | No file  | `8b4a8133d4a8`  |
| 1338   | No file  | `8b4a8133d4a8`  |
| 1335   | No file  | `8b4a8133d4a8`  |
| 1333   | No file  | `8b4a8133d4a8`  |
| 1329   | No file  | `8b4a8133d4a8`  |
| 1327   | No file  | `8b4a8133d4a8`  |
| 1324   | No file  | `8b4a8133d4a8`  |
| 1321   | No file  | `8b4a8133d4a8`  |
| 1319   | No file  | `8b4a8133d4a8`  |
| 1318   | No file  | `8b4a8133d4a8`  |
| 1316   | No file  | `8b4a8133d4a8`  |
| 1313   | No file  | `8b4a8133d4a8`  |
| 1311   | No file  | `8b4a8133d4a8`  |
| 1309   | No file  | `8b4a8133d4a8`  |
| 1304   | No file  | `8b4a8133d4a8`  |
| 1292   | No file  | `8b4a8133d4a8`  |
| 1286   | No file  | `8b4a8133d4a8`  |
| 1280   | No file  | `8b4a8133d4a8`  |
| 1276   | No file  | `8b4a8133d4a8`  |
| 1267   | No file  | `8b4a8133d4a8`  |
| 1261   | No file  | `8b4a8133d4a8`  |
| 1256   | No file  | `8b4a8133d4a8`  |
| 1250   | No file  | `8b4a8133d4a8`  |
| 1246   | No file  | `8b4a8133d4a8`  |
| 1239   | No file  | `8b4a8133d4a8`  |
| 1230   | No file  | `8b4a8133d4a8`  |
| 1226   | No file  | `8b4a8133d4a8`  |
| 1220   | No file  | `8b4a8133d4a8`  |
| 1217   | No file  | `8b4a8133d4a8`  |
| 1211   | No file  | `8b4a8133d4a8`  |
| 1210   | No file  | `8b4a8133d4a8`  |
| 1208   | No file  | `8b4a8133d4a8`  |
| 1203   | No file  | `8b4a8133d4a8`  |
| 1197   | No file  | `8b4a8133d4a8`  |
| 1194   | No file  | `8b4a8133d4a8`  |
| 1192   | No file  | `8b4a8133d4a8`  |
| 1187   | No file  | `8b4a8133d4a8`  |
| 1183   | No file  | `8b4a8133d4a8`  |
| 1177   | No file  | `8b4a8133d4a8`  |
| 1173   | No file  | `8b4a8133d4a8`  |
| 1167   | No file  | `8b4a8133d4a8`  |
| 1164   | No file  | `8b4a8133d4a8`  |
| 1156   | No file  | `8b4a8133d4a8`  |
| 1149   | No file  | `8b4a8133d4a8`  |
| 1144   | No file  | `8b4a8133d4a8`  |
| 1137   | No file  | `8b4a8133d4a8`  |
| 1132   | No file  | `8b4a8133d4a8`  |
| 1127   | No file  | `8b4a8133d4a8`  |
| 1122   | No file  | `8b4a8133d4a8`  |
| 1118   | No file  | `8b4a8133d4a8`  |
| 1114   | No file  | `8b4a8133d4a8`  |
| 1109   | No file  | `8b4a8133d4a8`  |
| 1102   | No file  | `8b4a8133d4a8`  |
| 1096   | No file  | `8b4a8133d4a8`  |
| 1088   | No file  | `8b4a8133d4a8`  |
| 1081   | No file  | `8b4a8133d4a8`  |
| 1076   | No file  | `8b4a8133d4a8`  |
| 1069   | No file  | `8b4a8133d4a8`  |
| 1064   | No file  | `8b4a8133d4a8`  |
| 1058   | No file  | `8b4a8133d4a8`  |
| 1051   | No file  | `8b4a8133d4a8`  |
| 1044   | No file  | `8b4a8133d4a8`  |
| 1036   | No file  | `8b4a8133d4a8`  |
| 1026   | No file  | `8b4a8133d4a8`  |
| 1016   | No file  | `8b4a8133d4a8`  |
| 1009   | No file  | `8b4a8133d4a8`  |
| 1005   | No file  | `8b4a8133d4a8`  |
| 1000   | No file  | `8b4a8133d4a8`  |
| 998    | No file  | `8b4a8133d4a8`  |
| 990    | No file  | `8b4a8133d4a8`  |
| 979    | No file  | `8b4a8133d4a8`  |
| 972    | No file  | `8b4a8133d4a8`  |
| 963    | No file  | `8b4a8133d4a8`  |
| 955    | No file  | `8b4a8133d4a8`  |
| 946    | No file  | `8b4a8133d4a8`  |
| 938    | No file  | `8b4a8133d4a8`  |
| 927    | No file  | `8b4a8133d4a8`  |
| 911    | No file  | `8b4a8133d4a8`  |
| 904    | No file  | `8b4a8133d4a8`  |
| 899    | No file  | `8b4a8133d4a8`  |
| 894    | No file  | `8b4a8133d4a8`  |
| 885    | No file  | `8b4a8133d4a8`  |
| 879    | No file  | `8b4a8133d4a8`  |
| 872    | No file  | `8b4a8133d4a8`  |
| 864    | No file  | `8b4a8133d4a8`  |
| 855    | No file  | `8b4a8133d4a8`  |
| 853    | No file  | `8b4a8133d4a8`  |
| 845    | No file  | `8b4a8133d4a8`  |
| 837    | No file  | `8b4a8133d4a8`  |
| 829    | No file  | `8b4a8133d4a8`  |
| 822    | No file  | `8b4a8133d4a8`  |
| 814    | No file  | `8b4a8133d4a8`  |
| 805    | No file  | `8b4a8133d4a8`  |
| 794    | No file  | `8b4a8133d4a8`  |
| 787    | No file  | `8b4a8133d4a8`  |
| 780    | No file  | `8b4a8133d4a8`  |
| 771    | No file  | `8b4a8133d4a8`  |
| 760    | No file  | `8b4a8133d4a8`  |
| 748    | No file  | `8b4a8133d4a8`  |
| 741    | No file  | `8b4a8133d4a8`  |
| 736    | No file  | `8b4a8133d4a8`  |
| 731    | No file  | `8b4a8133d4a8`  |
| 723    | No file  | `8b4a8133d4a8`  |
| 711    | No file  | `8b4a8133d4a8`  |
| 707    | No file  | `8b4a8133d4a8`  |
| 697    | No file  | `8b4a8133d4a8`  |
| 689    | No file  | `8b4a8133d4a8`  |
| 683    | No file  | `8b4a8133d4a8`  |
| 678    | No file  | `8b4a8133d4a8`  |
| 670    | No file  | `8b4a8133d4a8`  |
| 661    | No file  | `8b4a8133d4a8`  |
| 656    | No file  | `8b4a8133d4a8`  |
| 652    | No file  | `8b4a8133d4a8`  |
| 643    | No file  | `8b4a8133d4a8`  |
| 637    | No file  | `8b4a8133d4a8`  |
| 630    | No file  | `8b4a8133d4a8`  |
| 627    | No file  | `8b4a8133d4a8`  |
| 621    | No file  | `8b4a8133d4a8`  |
| 617    | No file  | `8b4a8133d4a8`  |
| 615    | No file  | `8b4a8133d4a8`  |
| 606    | No file  | `8b4a8133d4a8`  |
| 599    | No file  | `8b4a8133d4a8`  |
| 592    | No file  | `8b4a8133d4a8`  |
| 586    | No file  | `8b4a8133d4a8`  |
| 577    | No file  | `8b4a8133d4a8`  |
| 569    | No file  | `8b4a8133d4a8`  |
| 561    | No file  | `8b4a8133d4a8`  |
| 554    | No file  | `8b4a8133d4a8`  |
| 542    | No file  | `8b4a8133d4a8`  |
| 532    | No file  | `8b4a8133d4a8`  |
| 531    | No file  | `8b4a8133d4a8`  |
| 526    | No file  | `8b4a8133d4a8`  |
| 521    | No file  | `8b4a8133d4a8`  |
| 517    | No file  | `8b4a8133d4a8`  |
| 510    | No file  | `8b4a8133d4a8`  |
| 508    | No file  | `8b4a8133d4a8`  |
| 504    | No file  | `8b4a8133d4a8`  |
| 497    | No file  | `8b4a8133d4a8`  |
| 491    | No file  | `8b4a8133d4a8`  |
| 485    | No file  | `8b4a8133d4a8`  |
| 478    | No file  | `8b4a8133d4a8`  |
| 472    | No file  | `8b4a8133d4a8`  |
| 466    | No file  | `8b4a8133d4a8`  |
| 457    | No file  | `8b4a8133d4a8`  |
| 452    | No file  | `8b4a8133d4a8`  |
| 449    | No file  | `8b4a8133d4a8`  |
| 435    | No file  | `8b4a8133d4a8`  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                                     |
| -------------------------- | -------- | ------------------------------------------------------------------------ |
| `yachtbasecardoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `30` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 18 bytes + image path)

| Offset  | Type  | Field        | Notes                                                        |
| ------- | ----- | ------------ | ------------------------------------------------------------ |
| `+0x00` | u32   | card_key     | Card key; unique per row                                     |
| `+0x04` | u32   | card_key_dup | Equal to `card_key` in every row; the offset file points here |
| `+0x08` | u8    | symbol       | Card symbol, `1` to `4`; see Symbols                         |
| `+0x09` | u8    | eye          | Eye value, `1` to `6`                                        |
| `+0x0A` | str16 | image_path   | Picture path under `ui_texture/` (`UI_Artwork/IC_00015.dds`) |

The rows run from key 15 down to 1, then from 30 down to 16 (clients 1784
and 3474).

### `yachtbasecardoffset.dbss`

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `yachtbasecard.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row  |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                              |
| `+0x04` | u32  | data_offset | Row start + 4, at `card_key_dup`                         |
| `+0x08` | u32  | data_size   | The row without its leading key: `60` on client 3474     |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order, and every index row points at the row with
its key (clients 1784 and 3474).

## Symbols

The `#참조` sheet of a private server's `datasheet_minigame.xlsm` on client
1784 names the symbols in its note on the `Symbol` column: `1` sun (`해`),
`2` moon (`달`), `3` star (`별`), `4` flower (`꽃`). The live match window
draws the eye on a card texture named after a suit instead,
`UI_Artwork/Card/Card_<suit>_<eye>.dds` with `Space`, `Diamonds`, `Heart`
and `Clover` (`_symbolString` in `panel_window_minigame_yachtdice.luac`,
keyed by the `__eYachtSymbol_*` enum, whose values the Lua does not show).

On client 3474 cards 1 to 24 hold every symbol with every eye (symbol 1
on cards 1 to 6, 2 on 7 to 12, 3 on 13 to 18, 4 on 19 to 24). Cards 25 to
30 repeat six of those pairs with other pictures: `1`/`1`, `2`/`2`,
`3`/`3`, `4`/`4`, `1`/`5` and `2`/`6`.

## Field Names

The `BaseCardList` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `DicecardIndex` (`card_key`), `Symbol`
(`symbol`), `Eye` (`eye`) and `Image` (`image_path`). Its 30 rows match the
30 rows of clients 1784 and 3474 in every column. The file writes the key
twice: once as the index key, once inside the row.

## Notes

- Clients 1784 and 3474 ship the same `yachtbasecard.dbss` and
  `yachtbasecardoffset.dbss`, byte for byte.
- Every `image_path` on client 3474 is a knowledge picture
  (`UI_Artwork/IC_000NN.dds`); the match window draws it on the card as
  `stc_knowledgeImage` through `getCardTextureName()` of
  `ToClient_getYachtDiceCardWrapper()`. Cards 13 and 19 use `IC_00032` and
  `IC_00034` where the key would give `IC_00013` and `IC_00019`.
