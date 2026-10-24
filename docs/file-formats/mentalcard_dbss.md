# `mentalcard.dbss` Format

## Purpose

Defines every knowledge entry (card). Each record holds the card ID, its owning knowledge category (theme), the amity conversation parameters and combo effect, the Korean source name, description and acquisition text, the icon path, and a world position. Used to build knowledge trees and place entries within the knowledge UI.

Field names `cardKey`, `themeKey`, `minFavor`, `maxFavor` and `interest` follow the notes of [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor); the layout below was re-checked against our files. The combo field names follow the client Lua getters (`getBuffType`, `getVariedValue`, `getValidTurn`, `getApplyTurn`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes     | Records          | Row bytes                    |
| ------ | -------------- | ------- | ----------------------- | --------- | ---------------- | ---------------------------- |
| 2      | 2098 and later | 3483    | `mentalcard.dbss`       | 6,461,923 | 12,604 Card      | 162 to 2,273, 513 on average |
| 2      | 2098 and later | 3483    | `mentalcardoffset.dbss` | 151,268   | 12,604 Index Row | 12                           |
| 1      | 1250 to 2089   | 2089    | `mentalcard.dbss`       | 4,291,476 | 8,576 Card       | 161 to 2,248, 500 on average |
| 1      | 1250 to 2089   | 2089    | `mentalcardoffset.dbss` | 102,932   | 8,576 Index Row  | 12                           |

| Layout | File                    | Known               | Unknown          |
| ------ | ----------------------- | ------------------- | ---------------- |
| 2      | `mentalcard.dbss`       | 6,178,315 B (95.6%) | 283,608 B (4.4%) |
| 2      | `mentalcardoffset.dbss` | 151,268 B (100.0%)  | 0 B (0.0%)       |
| 1      | `mentalcard.dbss`       | 4,105,848 B (95.7%) | 185,628 B (4.3%) |
| 1      | `mentalcardoffset.dbss` | 102,932 B (100.0%)  | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `98e40a9793ec`  |
| 3482   | Layout 2 | `98e40a9793ec`  |
| 3474   | Layout 2 | `98e40a9793ec`  |
| 3473   | Layout 2 | `98e40a9793ec`  |
| 3464   | Layout 2 | `98e40a9793ec`  |
| 3458   | Layout 2 | `98e40a9793ec`  |
| 3454   | Layout 2 | `98e40a9793ec`  |
| 3444   | Layout 2 | `98e40a9793ec`  |
| 3435   | Layout 2 | `98e40a9793ec`  |
| 3426   | Layout 2 | `98e40a9793ec`  |
| 3418   | Layout 2 | `98e40a9793ec`  |
| 3412   | Layout 2 | `98e40a9793ec`  |
| 3402   | Layout 2 | `98e40a9793ec`  |
| 3396   | Layout 2 | `98e40a9793ec`  |
| 3387   | Layout 2 | `98e40a9793ec`  |
| 3381   | Layout 2 | `98e40a9793ec`  |
| 3373   | Layout 2 | `98e40a9793ec`  |
| 3364   | Layout 2 | `98e40a9793ec`  |
| 3356   | Layout 2 | `98e40a9793ec`  |
| 3349   | Layout 2 | `98e40a9793ec`  |
| 3342   | Layout 2 | `98e40a9793ec`  |
| 3335   | Layout 2 | `98e40a9793ec`  |
| 3326   | Layout 2 | `98e40a9793ec`  |
| 3321   | Layout 2 | `98e40a9793ec`  |
| 3314   | Layout 2 | `98e40a9793ec`  |
| 3303   | Layout 2 | `98e40a9793ec`  |
| 3302   | Layout 2 | `98e40a9793ec`  |
| 3293   | Layout 2 | `98e40a9793ec`  |
| 3283   | Layout 2 | `98e40a9793ec`  |
| 3275   | Layout 2 | `98e40a9793ec`  |
| 3267   | Layout 2 | `98e40a9793ec`  |
| 3258   | Layout 2 | `98e40a9793ec`  |
| 3251   | Layout 2 | `98e40a9793ec`  |
| 3242   | Layout 2 | `98e40a9793ec`  |
| 3235   | Layout 2 | `98e40a9793ec`  |
| 3229   | Layout 2 | `98e40a9793ec`  |
| 3212   | Layout 2 | `98e40a9793ec`  |
| 3203   | Layout 2 | `98e40a9793ec`  |
| 3193   | Layout 2 | `98e40a9793ec`  |
| 3186   | Layout 2 | `98e40a9793ec`  |
| 3177   | Layout 2 | `98e40a9793ec`  |
| 3169   | Layout 2 | `98e40a9793ec`  |
| 3158   | Layout 2 | `98e40a9793ec`  |
| 3151   | Layout 2 | `98e40a9793ec`  |
| 3144   | Layout 2 | `98e40a9793ec`  |
| 3133   | Layout 2 | `98e40a9793ec`  |
| 3125   | Layout 2 | `98e40a9793ec`  |
| 3118   | Layout 2 | `98e40a9793ec`  |
| 3111   | Layout 2 | `98e40a9793ec`  |
| 3103   | Layout 2 | `98e40a9793ec`  |
| 3095   | Layout 2 | `98e40a9793ec`  |
| 3086   | Layout 2 | `98e40a9793ec`  |
| 3072   | Layout 2 | `98e40a9793ec`  |
| 3062   | Layout 2 | `98e40a9793ec`  |
| 3052   | Layout 2 | `98e40a9793ec`  |
| 3045   | Layout 2 | `98e40a9793ec`  |
| 3037   | Layout 2 | `98e40a9793ec`  |
| 3030   | Layout 2 | `98e40a9793ec`  |
| 3021   | Layout 2 | `98e40a9793ec`  |
| 3012   | Layout 2 | `98e40a9793ec`  |
| 3002   | Layout 2 | `98e40a9793ec`  |
| 2995   | Layout 2 | `98e40a9793ec`  |
| 2987   | Layout 2 | `98e40a9793ec`  |
| 2978   | Layout 2 | `98e40a9793ec`  |
| 2970   | Layout 2 | `98e40a9793ec`  |
| 2959   | Layout 2 | `98e40a9793ec`  |
| 2951   | Layout 2 | `98e40a9793ec`  |
| 2942   | Layout 2 | `98e40a9793ec`  |
| 2935   | Layout 2 | `98e40a9793ec`  |
| 2932   | Layout 2 | `98e40a9793ec`  |
| 2923   | Layout 2 | `98e40a9793ec`  |
| 2919   | Layout 2 | `98e40a9793ec`  |
| 2907   | Layout 2 | `98e40a9793ec`  |
| 2900   | Layout 2 | `98e40a9793ec`  |
| 2891   | Layout 2 | `98e40a9793ec`  |
| 2882   | Layout 2 | `98e40a9793ec`  |
| 2872   | Layout 2 | `98e40a9793ec`  |
| 2863   | Layout 2 | `98e40a9793ec`  |
| 2855   | Layout 2 | `98e40a9793ec`  |
| 2849   | Layout 2 | `98e40a9793ec`  |
| 2844   | Layout 2 | `98e40a9793ec`  |
| 2834   | Layout 2 | `98e40a9793ec`  |
| 2825   | Layout 2 | `98e40a9793ec`  |
| 2819   | Layout 2 | `98e40a9793ec`  |
| 2811   | Layout 2 | `98e40a9793ec`  |
| 2803   | Layout 2 | `98e40a9793ec`  |
| 2794   | Layout 2 | `98e40a9793ec`  |
| 2783   | Layout 2 | `98e40a9793ec`  |
| 2774   | Layout 2 | `98e40a9793ec`  |
| 2765   | Layout 2 | `98e40a9793ec`  |
| 2756   | Layout 2 | `98e40a9793ec`  |
| 2750   | Layout 2 | `98e40a9793ec`  |
| 2743   | Layout 2 | `98e40a9793ec`  |
| 2736   | Layout 2 | `98e40a9793ec`  |
| 2726   | Layout 2 | `98e40a9793ec`  |
| 2717   | Layout 2 | `98e40a9793ec`  |
| 2709   | Layout 2 | `98e40a9793ec`  |
| 2703   | Layout 2 | `98e40a9793ec`  |
| 2695   | Layout 2 | `98e40a9793ec`  |
| 2684   | Layout 2 | `98e40a9793ec`  |
| 2672   | Layout 2 | `98e40a9793ec`  |
| 2665   | Layout 2 | `98e40a9793ec`  |
| 2657   | Layout 2 | `98e40a9793ec`  |
| 2649   | Layout 2 | `98e40a9793ec`  |
| 2644   | Layout 2 | `98e40a9793ec`  |
| 2637   | Layout 2 | `98e40a9793ec`  |
| 2629   | Layout 2 | `98e40a9793ec`  |
| 2619   | Layout 2 | `98e40a9793ec`  |
| 2612   | Layout 2 | `98e40a9793ec`  |
| 2606   | Layout 2 | `98e40a9793ec`  |
| 2602   | Layout 2 | `98e40a9793ec`  |
| 2601   | Layout 2 | `98e40a9793ec`  |
| 2592   | Layout 2 | `98e40a9793ec`  |
| 2583   | Layout 2 | `98e40a9793ec`  |
| 2575   | Layout 2 | `98e40a9793ec`  |
| 2567   | Layout 2 | `98e40a9793ec`  |
| 2560   | Layout 2 | `98e40a9793ec`  |
| 2553   | Layout 2 | `98e40a9793ec`  |
| 2545   | Layout 2 | `98e40a9793ec`  |
| 2538   | Layout 2 | `98e40a9793ec`  |
| 2529   | Layout 2 | `98e40a9793ec`  |
| 2519   | Layout 2 | `98e40a9793ec`  |
| 2513   | Layout 2 | `98e40a9793ec`  |
| 2510   | Layout 2 | `98e40a9793ec`  |
| 2507   | Layout 2 | `98e40a9793ec`  |
| 2503   | Layout 2 | `98e40a9793ec`  |
| 2498   | Layout 2 | `98e40a9793ec`  |
| 2492   | Layout 2 | `98e40a9793ec`  |
| 2487   | Layout 2 | `98e40a9793ec`  |
| 2480   | Layout 2 | `98e40a9793ec`  |
| 2474   | Layout 2 | `98e40a9793ec`  |
| 2468   | Layout 2 | `98e40a9793ec`  |
| 2460   | Layout 2 | `98e40a9793ec`  |
| 2453   | Layout 2 | `98e40a9793ec`  |
| 2444   | Layout 2 | `98e40a9793ec`  |
| 2438   | Layout 2 | `98e40a9793ec`  |
| 2434   | Layout 2 | `98e40a9793ec`  |
| 2429   | Layout 2 | `98e40a9793ec`  |
| 2421   | Layout 2 | `98e40a9793ec`  |
| 2414   | Layout 2 | `98e40a9793ec`  |
| 2407   | Layout 2 | `98e40a9793ec`  |
| 2401   | Layout 2 | `98e40a9793ec`  |
| 2397   | Layout 2 | `98e40a9793ec`  |
| 2393   | Layout 2 | `98e40a9793ec`  |
| 2384   | Layout 2 | `98e40a9793ec`  |
| 2378   | Layout 2 | `98e40a9793ec`  |
| 2372   | Layout 2 | `98e40a9793ec`  |
| 2358   | Layout 2 | `98e40a9793ec`  |
| 2352   | Layout 2 | `98e40a9793ec`  |
| 2347   | Layout 2 | `98e40a9793ec`  |
| 2343   | Layout 2 | `98e40a9793ec`  |
| 2335   | Layout 2 | `98e40a9793ec`  |
| 2327   | Layout 2 | `98e40a9793ec`  |
| 2324   | Layout 2 | `98e40a9793ec`  |
| 2319   | Layout 2 | `98e40a9793ec`  |
| 2313   | Layout 2 | `98e40a9793ec`  |
| 2308   | Layout 2 | `98e40a9793ec`  |
| 2302   | Layout 2 | `98e40a9793ec`  |
| 2295   | Layout 2 | `98e40a9793ec`  |
| 2290   | Layout 2 | `98e40a9793ec`  |
| 2284   | Layout 2 | `98e40a9793ec`  |
| 2276   | Layout 2 | `98e40a9793ec`  |
| 2269   | Layout 2 | `98e40a9793ec`  |
| 2259   | Layout 2 | `98e40a9793ec`  |
| 2250   | Layout 2 | `98e40a9793ec`  |
| 2243   | Layout 2 | `98e40a9793ec`  |
| 2235   | Layout 2 | `98e40a9793ec`  |
| 2229   | Layout 2 | `98e40a9793ec`  |
| 2224   | Layout 2 | `98e40a9793ec`  |
| 2218   | Layout 2 | `98e40a9793ec`  |
| 2215   | Layout 2 | `98e40a9793ec`  |
| 2207   | Layout 2 | `98e40a9793ec`  |
| 2203   | Layout 2 | `98e40a9793ec`  |
| 2196   | Layout 2 | `98e40a9793ec`  |
| 2192   | Layout 2 | `98e40a9793ec`  |
| 2189   | Layout 2 | `98e40a9793ec`  |
| 2183   | Layout 2 | `98e40a9793ec`  |
| 2179   | Layout 2 | `98e40a9793ec`  |
| 2171   | Layout 2 | `98e40a9793ec`  |
| 2163   | Layout 2 | `98e40a9793ec`  |
| 2156   | Layout 2 | `98e40a9793ec`  |
| 2151   | Layout 2 | `98e40a9793ec`  |
| 2147   | Layout 2 | `98e40a9793ec`  |
| 2142   | Layout 2 | `98e40a9793ec`  |
| 2138   | Layout 2 | `98e40a9793ec`  |
| 2134   | Layout 2 | `98e40a9793ec`  |
| 2130   | Layout 2 | `98e40a9793ec`  |
| 2122   | Layout 2 | `98e40a9793ec`  |
| 2107   | Layout 2 | `98e40a9793ec`  |
| 2098   | Layout 2 | `98e40a9793ec`  |
| 2089   | Layout 1 | `98e40a9793ec`  |
| 2081   | Layout 1 | `98e40a9793ec`  |
| 2073   | Layout 1 | `98e40a9793ec`  |
| 2067   | Layout 1 | `98e40a9793ec`  |
| 2063   | Layout 1 | `98e40a9793ec`  |
| 2059   | Layout 1 | `98e40a9793ec`  |
| 2052   | Layout 1 | `98e40a9793ec`  |
| 2044   | Layout 1 | `98e40a9793ec`  |
| 2039   | Layout 1 | `98e40a9793ec`  |
| 2032   | Layout 1 | `98e40a9793ec`  |
| 2025   | Layout 1 | `98e40a9793ec`  |
| 2011   | Layout 1 | `98e40a9793ec`  |
| 2005   | Layout 1 | `98e40a9793ec`  |
| 2000   | Layout 1 | `98e40a9793ec`  |
| 1996   | Layout 1 | `98e40a9793ec`  |
| 1991   | Layout 1 | `98e40a9793ec`  |
| 1985   | Layout 1 | `98e40a9793ec`  |
| 1980   | Layout 1 | `98e40a9793ec`  |
| 1969   | Layout 1 | `98e40a9793ec`  |
| 1964   | Layout 1 | `98e40a9793ec`  |
| 1958   | Layout 1 | `98e40a9793ec`  |
| 1950   | Layout 1 | `98e40a9793ec`  |
| 1945   | Layout 1 | `98e40a9793ec`  |
| 1937   | Layout 1 | `98e40a9793ec`  |
| 1933   | Layout 1 | `98e40a9793ec`  |
| 1927   | Layout 1 | `98e40a9793ec`  |
| 1921   | Layout 1 | `98e40a9793ec`  |
| 1914   | Layout 1 | `98e40a9793ec`  |
| 1908   | Layout 1 | `98e40a9793ec`  |
| 1897   | Layout 1 | `98e40a9793ec`  |
| 1892   | Layout 1 | `98e40a9793ec`  |
| 1886   | Layout 1 | `98e40a9793ec`  |
| 1881   | Layout 1 | `98e40a9793ec`  |
| 1871   | Layout 1 | `98e40a9793ec`  |
| 1866   | Layout 1 | `98e40a9793ec`  |
| 1862   | Layout 1 | `98e40a9793ec`  |
| 1854   | Layout 1 | `98e40a9793ec`  |
| 1846   | Layout 1 | `98e40a9793ec`  |
| 1838   | Layout 1 | `98e40a9793ec`  |
| 1832   | Layout 1 | `98e40a9793ec`  |
| 1826   | Layout 1 | `98e40a9793ec`  |
| 1822   | Layout 1 | `98e40a9793ec`  |
| 1818   | Layout 1 | `98e40a9793ec`  |
| 1804   | Layout 1 | `98e40a9793ec`  |
| 1794   | Layout 1 | `98e40a9793ec`  |
| 1790   | Layout 1 | `98e40a9793ec`  |
| 1784   | Layout 1 | `98e40a9793ec`  |
| 1774   | Layout 1 | `98e40a9793ec`  |
| 1771   | Layout 1 | `98e40a9793ec`  |
| 1762   | Layout 1 | `98e40a9793ec`  |
| 1759   | Layout 1 | `98e40a9793ec`  |
| 1754   | Layout 1 | `98e40a9793ec`  |
| 1749   | Layout 1 | `98e40a9793ec`  |
| 1743   | Layout 1 | `98e40a9793ec`  |
| 1737   | Layout 1 | `98e40a9793ec`  |
| 1731   | Layout 1 | `98e40a9793ec`  |
| 1725   | Layout 1 | `98e40a9793ec`  |
| 1717   | Layout 1 | `98e40a9793ec`  |
| 1710   | Layout 1 | `98e40a9793ec`  |
| 1704   | Layout 1 | `98e40a9793ec`  |
| 1698   | Layout 1 | `98e40a9793ec`  |
| 1690   | Layout 1 | `98e40a9793ec`  |
| 1685   | Layout 1 | `98e40a9793ec`  |
| 1680   | Layout 1 | `98e40a9793ec`  |
| 1674   | Layout 1 | `98e40a9793ec`  |
| 1668   | Layout 1 | `98e40a9793ec`  |
| 1659   | Layout 1 | `98e40a9793ec`  |
| 1649   | Layout 1 | `98e40a9793ec`  |
| 1642   | Layout 1 | `98e40a9793ec`  |
| 1636   | Layout 1 | `98e40a9793ec`  |
| 1628   | Layout 1 | `98e40a9793ec`  |
| 1622   | Layout 1 | `98e40a9793ec`  |
| 1614   | Layout 1 | `98e40a9793ec`  |
| 1608   | Layout 1 | `98e40a9793ec`  |
| 1602   | Layout 1 | `98e40a9793ec`  |
| 1598   | Layout 1 | `98e40a9793ec`  |
| 1594   | Layout 1 | `98e40a9793ec`  |
| 1590   | Layout 1 | `98e40a9793ec`  |
| 1587   | Layout 1 | `98e40a9793ec`  |
| 1584   | Layout 1 | `98e40a9793ec`  |
| 1579   | Layout 1 | `98e40a9793ec`  |
| 1572   | Layout 1 | `98e40a9793ec`  |
| 1565   | Layout 1 | `98e40a9793ec`  |
| 1559   | Layout 1 | `98e40a9793ec`  |
| 1554   | Layout 1 | `98e40a9793ec`  |
| 1547   | Layout 1 | `98e40a9793ec`  |
| 1537   | Layout 1 | `98e40a9793ec`  |
| 1529   | Layout 1 | `98e40a9793ec`  |
| 1524   | Layout 1 | `98e40a9793ec`  |
| 1519   | Layout 1 | `98e40a9793ec`  |
| 1509   | Layout 1 | `98e40a9793ec`  |
| 1506   | Layout 1 | `98e40a9793ec`  |
| 1504   | Layout 1 | `98e40a9793ec`  |
| 1500   | Layout 1 | `98e40a9793ec`  |
| 1493   | Layout 1 | `98e40a9793ec`  |
| 1489   | Layout 1 | `98e40a9793ec`  |
| 1485   | Layout 1 | `98e40a9793ec`  |
| 1481   | Layout 1 | `98e40a9793ec`  |
| 1474   | Layout 1 | `98e40a9793ec`  |
| 1466   | Layout 1 | `98e40a9793ec`  |
| 1462   | Layout 1 | `98e40a9793ec`  |
| 1459   | Layout 1 | `98e40a9793ec`  |
| 1453   | Layout 1 | `98e40a9793ec`  |
| 1450   | Layout 1 | `98e40a9793ec`  |
| 1445   | Layout 1 | `98e40a9793ec`  |
| 1439   | Layout 1 | `98e40a9793ec`  |
| 1433   | Layout 1 | `98e40a9793ec`  |
| 1430   | Layout 1 | `98e40a9793ec`  |
| 1426   | Layout 1 | `98e40a9793ec`  |
| 1421   | Layout 1 | `98e40a9793ec`  |
| 1417   | Layout 1 | `98e40a9793ec`  |
| 1416   | Layout 1 | `98e40a9793ec`  |
| 1409   | Layout 1 | `98e40a9793ec`  |
| 1405   | Layout 1 | `98e40a9793ec`  |
| 1401   | Layout 1 | `98e40a9793ec`  |
| 1396   | Layout 1 | `98e40a9793ec`  |
| 1391   | Layout 1 | `98e40a9793ec`  |
| 1390   | Layout 1 | `98e40a9793ec`  |
| 1386   | Layout 1 | `98e40a9793ec`  |
| 1381   | Layout 1 | `98e40a9793ec`  |
| 1379   | Layout 1 | `98e40a9793ec`  |
| 1372   | Layout 1 | `98e40a9793ec`  |
| 1366   | Layout 1 | `98e40a9793ec`  |
| 1364   | Layout 1 | `98e40a9793ec`  |
| 1363   | Layout 1 | `98e40a9793ec`  |
| 1360   | Layout 1 | `98e40a9793ec`  |
| 1358   | Layout 1 | `98e40a9793ec`  |
| 1355   | Layout 1 | `98e40a9793ec`  |
| 1351   | Layout 1 | `98e40a9793ec`  |
| 1348   | Layout 1 | `98e40a9793ec`  |
| 1346   | Layout 1 | `98e40a9793ec`  |
| 1341   | Layout 1 | `98e40a9793ec`  |
| 1340   | Layout 1 | `98e40a9793ec`  |
| 1338   | Layout 1 | `98e40a9793ec`  |
| 1335   | Layout 1 | `98e40a9793ec`  |
| 1333   | Layout 1 | `98e40a9793ec`  |
| 1329   | Layout 1 | `98e40a9793ec`  |
| 1327   | Layout 1 | `98e40a9793ec`  |
| 1324   | Layout 1 | `98e40a9793ec`  |
| 1321   | Layout 1 | `98e40a9793ec`  |
| 1319   | Layout 1 | `98e40a9793ec`  |
| 1318   | Layout 1 | `98e40a9793ec`  |
| 1316   | Layout 1 | `98e40a9793ec`  |
| 1313   | Layout 1 | `98e40a9793ec`  |
| 1311   | Layout 1 | `98e40a9793ec`  |
| 1309   | Layout 1 | `98e40a9793ec`  |
| 1304   | Layout 1 | `98e40a9793ec`  |
| 1292   | Layout 1 | `98e40a9793ec`  |
| 1286   | Layout 1 | `98e40a9793ec`  |
| 1280   | Layout 1 | `98e40a9793ec`  |
| 1276   | Layout 1 | `98e40a9793ec`  |
| 1267   | Layout 1 | `98e40a9793ec`  |
| 1261   | Layout 1 | `98e40a9793ec`  |
| 1256   | Layout 1 | `98e40a9793ec`  |
| 1250   | Layout 1 | `98e40a9793ec`  |
| 1246   | No file  | `98e40a9793ec`  |
| 1239   | No file  | `98e40a9793ec`  |
| 1230   | No file  | `98e40a9793ec`  |
| 1226   | No file  | `98e40a9793ec`  |
| 1220   | No file  | `98e40a9793ec`  |
| 1217   | No file  | `98e40a9793ec`  |
| 1211   | No file  | `98e40a9793ec`  |
| 1210   | No file  | `98e40a9793ec`  |
| 1208   | No file  | `98e40a9793ec`  |
| 1203   | No file  | `98e40a9793ec`  |
| 1197   | No file  | `98e40a9793ec`  |
| 1194   | No file  | `98e40a9793ec`  |
| 1192   | No file  | `98e40a9793ec`  |
| 1187   | No file  | `98e40a9793ec`  |
| 1183   | No file  | `98e40a9793ec`  |
| 1177   | No file  | `98e40a9793ec`  |
| 1173   | No file  | `98e40a9793ec`  |
| 1167   | No file  | `98e40a9793ec`  |
| 1164   | No file  | `98e40a9793ec`  |
| 1156   | No file  | `98e40a9793ec`  |
| 1149   | No file  | `98e40a9793ec`  |
| 1144   | No file  | `98e40a9793ec`  |
| 1137   | No file  | `98e40a9793ec`  |
| 1132   | No file  | `98e40a9793ec`  |
| 1127   | No file  | `98e40a9793ec`  |
| 1122   | No file  | `98e40a9793ec`  |
| 1118   | No file  | `98e40a9793ec`  |
| 1114   | No file  | `98e40a9793ec`  |
| 1109   | No file  | `98e40a9793ec`  |
| 1102   | No file  | `98e40a9793ec`  |
| 1096   | No file  | `98e40a9793ec`  |
| 1088   | No file  | `98e40a9793ec`  |
| 1081   | No file  | `98e40a9793ec`  |
| 1076   | No file  | `98e40a9793ec`  |
| 1069   | No file  | `98e40a9793ec`  |
| 1064   | No file  | `98e40a9793ec`  |
| 1058   | No file  | `98e40a9793ec`  |
| 1051   | No file  | `98e40a9793ec`  |
| 1044   | No file  | `98e40a9793ec`  |
| 1036   | No file  | `98e40a9793ec`  |
| 1026   | No file  | `98e40a9793ec`  |
| 1016   | No file  | `98e40a9793ec`  |
| 1009   | No file  | `98e40a9793ec`  |
| 1005   | No file  | `98e40a9793ec`  |
| 1000   | No file  | `98e40a9793ec`  |
| 998    | No file  | `98e40a9793ec`  |
| 990    | No file  | `98e40a9793ec`  |
| 979    | No file  | `98e40a9793ec`  |
| 972    | No file  | `98e40a9793ec`  |
| 963    | No file  | `98e40a9793ec`  |
| 955    | No file  | `98e40a9793ec`  |
| 946    | No file  | `98e40a9793ec`  |
| 938    | No file  | `98e40a9793ec`  |
| 927    | No file  | `98e40a9793ec`  |
| 911    | No file  | `98e40a9793ec`  |
| 904    | No file  | `98e40a9793ec`  |
| 899    | No file  | `98e40a9793ec`  |
| 894    | No file  | `98e40a9793ec`  |
| 885    | No file  | `98e40a9793ec`  |
| 879    | No file  | `98e40a9793ec`  |
| 872    | No file  | `98e40a9793ec`  |
| 864    | No file  | `98e40a9793ec`  |
| 855    | No file  | `98e40a9793ec`  |
| 853    | No file  | `98e40a9793ec`  |
| 845    | No file  | `98e40a9793ec`  |
| 837    | No file  | `98e40a9793ec`  |
| 829    | No file  | `98e40a9793ec`  |
| 822    | No file  | `98e40a9793ec`  |
| 814    | No file  | `98e40a9793ec`  |
| 805    | No file  | `98e40a9793ec`  |
| 794    | No file  | `98e40a9793ec`  |
| 787    | No file  | `98e40a9793ec`  |
| 780    | No file  | `98e40a9793ec`  |
| 771    | No file  | `98e40a9793ec`  |
| 760    | No file  | `98e40a9793ec`  |
| 748    | No file  | `98e40a9793ec`  |
| 741    | No file  | `98e40a9793ec`  |
| 736    | No file  | `98e40a9793ec`  |
| 731    | No file  | `98e40a9793ec`  |
| 723    | No file  | `98e40a9793ec`  |
| 711    | No file  | `98e40a9793ec`  |
| 707    | No file  | `98e40a9793ec`  |
| 697    | No file  | `98e40a9793ec`  |
| 689    | No file  | `98e40a9793ec`  |
| 683    | No file  | `98e40a9793ec`  |
| 678    | No file  | `98e40a9793ec`  |
| 670    | No file  | `98e40a9793ec`  |
| 661    | No file  | `98e40a9793ec`  |
| 656    | No file  | `98e40a9793ec`  |
| 652    | No file  | `98e40a9793ec`  |
| 643    | No file  | `98e40a9793ec`  |
| 637    | No file  | `98e40a9793ec`  |
| 630    | No file  | `98e40a9793ec`  |
| 627    | No file  | `98e40a9793ec`  |
| 621    | No file  | `98e40a9793ec`  |
| 617    | No file  | `98e40a9793ec`  |
| 615    | No file  | `98e40a9793ec`  |
| 606    | No file  | `98e40a9793ec`  |
| 599    | No file  | `98e40a9793ec`  |
| 592    | No file  | `98e40a9793ec`  |
| 586    | No file  | `98e40a9793ec`  |
| 577    | No file  | `98e40a9793ec`  |
| 569    | No file  | `98e40a9793ec`  |
| 561    | No file  | `98e40a9793ec`  |
| 554    | No file  | `98e40a9793ec`  |
| 542    | No file  | `98e40a9793ec`  |
| 532    | No file  | `98e40a9793ec`  |
| 531    | No file  | `98e40a9793ec`  |
| 526    | No file  | `98e40a9793ec`  |
| 521    | No file  | `98e40a9793ec`  |
| 517    | No file  | `98e40a9793ec`  |
| 510    | No file  | `98e40a9793ec`  |
| 508    | No file  | `98e40a9793ec`  |
| 504    | No file  | `98e40a9793ec`  |
| 497    | No file  | `98e40a9793ec`  |
| 491    | No file  | `98e40a9793ec`  |
| 485    | No file  | `98e40a9793ec`  |
| 478    | No file  | `98e40a9793ec`  |
| 472    | No file  | `98e40a9793ec`  |
| 466    | No file  | `98e40a9793ec`  |
| 457    | No file  | `98e40a9793ec`  |
| 452    | No file  | `98e40a9793ec`  |
| 449    | No file  | `98e40a9793ec`  |
| 435    | No file  | `98e40a9793ec`  |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                                 |
| ----------------------- | -------- | ---------------------------------------------------- |
| `mentalcardoffset.dbss` | Required | Provides card ID, byte offset and size for each card |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type        | Field   | Notes                                           |
| ------- | ----------- | ------- | ----------------------------------------------- |
| `+0x00` | u32         | count   | Number of records; matches `mentalcardoffset`   |
| `+0x04` | Card[count] | records | Variable-size card records, back to back; see Card |

Strings are `i64` UTF-16 code-unit counts followed by that many UTF-16LE units, except the icon path, which is an `i64` byte count followed by ASCII.

### Card (variable: 97 bytes + strings and hashes)

A 33-byte header (`+0x00` to `+0x20`), then the body.

| Offset                | Type            | Field                     | Notes                                                                                   |
| --------------------- | --------------- | ------------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`               | u32             | card_id                   | Knowledge entry ID; equals the index key; LOC `str_type=34`, `str_id1`                  |
| `+0x04`               | u16             | theme_id                  | Owning category in `mentaltheme.dbss`; LOC `str_type=9`                                 |
| `+0x06`               | u8              | unknown_06                | Observed `0` or `1`; `1` on 172 cards, mostly story and adventure-log entries           |
| `+0x07`               | u8              | unknown_07                | Observed `0` or `1`; `1` on 373 cards, almost all under theme `10399` (None)            |
| `+0x08`               | f32             | min_favor                 | Amity conversation favor, lower bound; whole numbers `0` to `72`                        |
| `+0x0C`               | f32             | max_favor                 | Amity conversation favor, upper bound; whole numbers `0` to `100`                       |
| `+0x10`               | f32             | interest                  | Amity conversation interest; whole numbers `0` to `100`                                 |
| `+0x14`               | u8              | buff_type                 | Combo effect stat: `0` Favor, `1` Interest Level, `4` no combo (9,962 cards)            |
| `+0x15`               | f32             | varied_value              | Combo amount, unaligned; whole numbers `1` to `10` (one card `19`); `0` without a combo |
| `+0x19`               | u32             | valid_turn                | Combo duration in turns, `1` to `4`; `0` without a combo                                |
| `+0x1D`               | u32             | apply_turn                | Combo delay, `1` to `4`; the tooltip shows it plus one; `0` without a combo             |
| `+0x21`               | str16           | name_kr                   | Korean card name; English form is LOC `str_type=34`, `str_id4=0`                        |
| `name_kr+0x00`        | str16           | description_kr            | Korean description; English form is LOC `str_type=34`, `str_id4=1`                      |
| `description_kr+0x00` | u8              | unknown_description_kr_00 | `0` or `1`; `1` on 474 cards, mostly adventure-log themes                               |
| `description_kr+0x01` | u8              | unknown_description_kr_01 | Always `0`                                                                              |
| `description_kr+0x02` | u32             | unknown_description_kr_02 | `5` on 10,455 cards, `0` on 1,893, `1` to `4` on the rest                               |
| `description_kr+0x06` | str8            | icon_path                 | Always under `UI_Artwork/`, e.g. `UI_Artwork/IC_015879.dds`                             |
| `icon_path+0x00`      | str16           | acquisition_kr            | Korean "how to obtain" text; English form is LOC `str_type=34`, `str_id4=2`             |
| `acquisition_kr+0x00` | f32[3]          | position                  | World `x`, `y` (height), `z`; all zero on 9,356 cards                                   |
| `acquisition_kr+0x0C` | u8              | unknown_acquisition_kr_0c | `17` on 10,388 cards, otherwise `0` to `16`                                             |
| `acquisition_kr+0x0D` | u32             | unknown_acquisition_kr_0d | `0`, `1` or `3`                                                                         |
| `acquisition_kr+0x11` | u32             | hash_count                | `1` to `7`                                                                              |
| `acquisition_kr+0x15` | u32[hash_count] | unknown_hashes            | Hash-like values; 271 distinct, lists share prefixes between cards                      |
| `unknown_hashes+0x00` | bytes[5]        | unknown_end               | Always zero                                                                             |

Earlier versions of this doc called `unknown_06` `theme_flag_a`, `unknown_07` `theme_flag_b`, `unknown_description_kr_00` `body_flag`, `unknown_description_kr_01` `unknown_after_body_flag`, `unknown_description_kr_02` `body_value`, `unknown_acquisition_kr_0c` `tail_kind`, `unknown_acquisition_kr_0d` `tail_value` and `unknown_hashes` `hashes`.

The combo fields build the tooltip's "Next combo effect" line: "After `{apply_turn + 1}` turns, `{Favor | Interest Level}` will increase by `{varied_value}` for `{valid_turn}` turns", or "None" when `buff_type` is `4`. Confirmed in game on 2026-09-27 and 2026-09-28 against 19 cards, 10 with a combo and 9 without; see Confirmed Examples. No card stores a decrease or a `buff_type` other than `0`, `1` and `4`.

Every one of the 12,502 records parses with this layout and ends exactly at its index `size`. The same layout holds for the older test fixture (12,087 records) and for the 12,604 records after the 2026-09-27 update, which still tile the file from byte `4` to its end.

### `mentalcardoffset.dbss`

`PABR` index with 12-byte rows, the same shape as other `PABR` offset companions but with a u32 key.

| Offset              | Type             | Field        | Notes                                           |
| ------------------- | ---------------- | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]          | magic        | ASCII `PABR`                                    |
| `+0x04`             | u32              | count        | Number of rows; `12,604` after the 2026-09-27 client update, `12,502` before it, `12,087` in the test fixture |
| `+0x08`             | Index Row[count] | rows         | See Index Row                                   |
| `rows+0x00`         | String Table     | string_table | See String Table                                |
| `string_table+0x00` | u32              | rows_end     | End offset of the index rows (`150032`)         |
| `string_table+0x04` | u32              | zero         | Always `0`                                      |

Rows tile `mentalcard.dbss` exactly: the first record starts at `4`, each next record starts where the previous one ends, and the last ends at the file size.

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | card_id     | Equals the `card_id` at the start of the record          |
| `+0x04` | u32  | data_offset | Absolute offset of the record in `mentalcard.dbss`       |
| `+0x08` | u32  | size        | Record size in bytes                                     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

On client 1784 `unknown_end` is 4 zero bytes, so each card is one byte
shorter; every other field is as in Layout 2.

### Card (variable: 96 bytes + strings and hashes)

| Offset                | Type            | Field                     | Notes                    |
| --------------------- | --------------- | ------------------------- | ------------------------ |
| `+0x00`               | u32             | card_id                   |                          |
| `+0x04`               | u16             | theme_id                  |                          |
| `+0x06`               | u8              | unknown_06                |                          |
| `+0x07`               | u8              | unknown_07                |                          |
| `+0x08`               | f32             | min_favor                 |                          |
| `+0x0C`               | f32             | max_favor                 |                          |
| `+0x10`               | f32             | interest                  |                          |
| `+0x14`               | u8              | buff_type                 |                          |
| `+0x15`               | f32             | varied_value              |                          |
| `+0x19`               | u32             | valid_turn                |                          |
| `+0x1D`               | u32             | apply_turn                |                          |
| `+0x21`               | str16           | name_kr                   |                          |
| `name_kr+0x00`        | str16           | description_kr            |                          |
| `description_kr+0x00` | u8              | unknown_description_kr_00 |                          |
| `description_kr+0x01` | u8              | unknown_description_kr_01 |                          |
| `description_kr+0x02` | u32             | unknown_description_kr_02 |                          |
| `description_kr+0x06` | str8            | icon_path                 |                          |
| `icon_path+0x00`      | str16           | acquisition_kr            |                          |
| `acquisition_kr+0x00` | f32[3]          | position                  |                          |
| `acquisition_kr+0x0C` | u8              | unknown_acquisition_kr_0c |                          |
| `acquisition_kr+0x0D` | u32             | unknown_acquisition_kr_0d |                          |
| `acquisition_kr+0x11` | u32             | hash_count                |                          |
| `acquisition_kr+0x15` | u32[hash_count] | unknown_hashes            |                          |
| `unknown_hashes+0x00` | bytes[4]        | unknown_end               | Always zero              |

## Confirmed Examples

Client 3458:

| card_id | LOC Name                | theme_id | min/max favor | interest | combo (type, value, valid, apply) | position                     |
| ------- | ----------------------- | -------- | ------------- | -------- | --------------------------------- | ---------------------------- |
| `15879` | Despair-Consumed Blader | `10087`  | `1` / `8`     | `45`     | Favor, `6`, `1`, `3`              | `0, 0, 0`                    |
| `3001`  | Velia                   | `5101`   | `45` / `49`   | `20`     | none                              | `152611, -7849, 290383`      |
| `15949` | Ynix Remnant            | `355`    | `35` / `37`   | `22`     | none                              | `1115590, 6865, 651513`      |

Combo text checked in game (Ornella on 2026-09-27, the rest through Oliviero on 2026-09-28). Every card's Attributes (Interest Level, Favor range) also equal the stored values exactly:

| card_id | Name | Stored combo (type, value, valid, apply) | Tooltip "Next combo effect" |
| ---: | --- | --- | --- |
| 102 | Ornella | Favor, 4, 3, 1 | After 2 turns, Favor will increase by 4 for 3 turns |
| 6059 | Al Rhundi's Journal | Favor, 1, 3, 2 | After 3 turns, Favor will increase by 1 for 3 turns |
| 6062 | Lazy Soldiers | Favor, 5, 1, 1 | After 2 turns, Favor will increase by 5 for 1 turns |
| 6063 | Cruhorn's Errand | Interest, 3, 3, 1 | After 2 turns, Interest Level will increase by 3 for 3 turns |
| 6075 | Kite Flying | Interest, 3, 3, 1 | After 2 turns, Interest Level will increase by 3 for 3 turns |
| 6080 | Laborers of the Quarry | Favor, 4, 1, 3 | After 4 turns, Favor will increase by 4 for 1 turns |
| 6090 | Melissa's Heart | Interest, 3, 3, 1 | After 2 turns, Interest Level will increase by 3 for 3 turns |
| 6092 | Secret Mission at the Abandoned Fort Site | Interest, 3, 1, 2 | After 3 turns, Interest Level will increase by 3 for 1 turns |
| 6106 | Broken Wagon | Favor, 8, 2, 1 | After 2 turns, Favor will increase by 8 for 2 turns |
| 6122 | Demibeast and Shai | Favor, 8, 1, 4 | After 5 turns, Favor will increase by 8 for 1 turns |

Stored as no combo and shown as "None": `4024` Lost Lamb, `6066` Heidel Church Belfry, `6079` Cannonball Master, `6086` Mine Imps Gone Berserk, `6087` Bloodstained Letter, `6093` Risk Factors Everywhere, `6095` Broken Cannon, `6096` Ornella's taste, `6105` Orcs and Spirits.

## Notes

- `card_id` → LOC `str_type=34`, `str_id1=card_id`; `str_id4` selects name (0), description (1) and acquisition text (2). 12,485 of 12,502 cards have an English name.
- `theme_id` → LOC `str_type=9`, `str_id1=theme_id` → knowledge category name. Read it as a u16: 524 cards have a non-zero byte at `+0x06` or `+0x07`, and reading `+0x04` as a u32 gives values such as `86040` (`0x15018`) that match no theme. With the u16 read, every card's theme lists that card in its `mentaltheme.dbss` entries.
- The three floats are whole numbers. `min_favor <= max_favor` on 12,484 of 12,604 cards in client 3458. In client 3458 the median favor range is 34 to 39 with interest 22 on cards without a combo, and 20 to 26 with interest 30 on the 2,642 cards with one.
- `acquisition_kr` is empty on 651 cards. Whenever LOC has `str_id4=2` for a card, the card also has a non-empty `acquisition_kr` (11,766 cards).
- `characterstatic.dbss` `getknowledge(<id>)` scripts grant 3,556 of the 12,604 cards on client 3458 (`npcsimply.bss` adds none). Most are granted by one NPC or by copies of one NPC with the same name; card `19` "NPC Pathfind Preventive Knowledge" is granted by 352 characters.
- The monsters, NPCs and gathering nodes in [knowledgelearning.dbss](knowledgelearning_dbss.md) table 0 add 506 character links on client 3458, 177 of them for cards no script grants (card `1643` "Rhyolite" from the Rhyolite node `11982`). Learned From merges both indexes, so card `4678` "Helm Tribe Chief Steel Nux" reads `Helm Tribe Chief, Steel Nux`. Its table 1 items fill Learned From Items (card `8579` "Gurnard" from the Gurnard fish `8279`).
- Non-zero positions are on 3,147 cards in client 3458, mostly NPC, barterer and node-manager entries. They use the same world frame as the `exploration.bss` node positions: town cards sit exactly on their node (Olvia `3032`, Calpheon `3177`, Keplan `3176`), and NPC cards sit where the NPC stands (Igor Bartali `18`, Islin Bartali `1` and Marsella `6` are all within about 35 m of the Velia node at `18588, 76647`).
- The index key is not a separate row identifier: it equals `card_id` on every row.
- How the conversation uses the values, per the [Black Desert Foundry, Story Exchange guide](https://www.blackdesertfoundry.com/story-exchange-guide/): a topic (card) has a fixed Interest Level and a Favor range. The NPC rolls its own Interest Level and Favor each conversation (from its `npcpersonality.dbss` ranges). The window then shows values relative to that NPC: Sparking Interest = topic interest / NPC interest (the chance of a positive reaction, always positive when the topic's is higher), and Interest gained = topic favor minus NPC favor. So the same card shows different numbers with different NPCs (that is how I see it in game, 2026-09-27), and a reading converts back to base values: `interest ≈ sparking × NPC interest`, `favor = interest gained + NPC favor`.
- The guide's example is close to, but not equal to, the stored values: topic Shiel shows Interest Level `11` and Favor `31`-`39`; card `11` stored `10` and `33`-`38` before the 2026-09-27 update. Its NPC, Lorenzo Murray (`40015`), shows Interest `32` and Favor `15`, both inside his stored ranges (`31`-`34`, `15`-`19`).
- The topic tooltip has two parts: **Attributes**, the card's own Interest Level and Favor range, and **Interaction Effect**, the values relative to the current NPC. For Lost Lamb with Oliviero it shows Attributes `23` / `33` ~ `37` and Interaction Effect Sparking Interest `23 (77%)`, Favor `2-6`, which fits the formulas above exactly with Oliviero at Interest Level `30` (23 / 30 = 77%) and Favor `31` (33 - 31 = 2, 37 - 31 = 6).
- The stored Attributes equal what the game shows. On 2026-09-27 I compared readings through Oliviero (`41091`) with the pre-update fixture and found gaps of up to 2 interest and a few favor, but those readings equal client 3458 exactly (for example Lost Lamb `23` / `33`-`37`, stored `21` / `34`-`36` before the update), and so do all 19 cards read on 2026-09-28. The update rerolls many cards: Shiel (`11`) is `14` / `34`-`38` in client 3458, `10` / `33`-`38` before it and `11` / `31`-`39` in the 2024 guide above, so older readings (the guide, the tracker dataset below) differ because they come from older patches. Oliviero's own Interest Level stayed at 30 to 31 over several conversations (stored `30`-`34`), and his Favor stayed at `31` (stored `31`-`35`).
- The tooltip is built by `PaGlobal_MentalGame_All:updateTooltipContext` in `luacscript/x64/widget/dialogue/panel_mentalgame_all_1.luac` (Lua 5.1 bytecode, decompiled with unluac). Attributes come from the live conversation card, not from this record: Interest Level is `card:getHit()`, Favor is `card:getMinDD()` ~ `card:getMaxDD()`. The Interaction Effect is `getHit() / npc:getCurrentDV() * 100` (clamped to 0-100) and `getMinDD() - npc:getCurrentPV()` / `getMaxDD() - npc:getCurrentPV()` (clamped at 0), so the NPC's interest is `CurrentDV` and its favor `CurrentPV`. The static record (`card:getStaticStatus()`, this file) is only used for the card key and the combo text: `getBuffType()`, `getApplyTurn()` (shown plus one, "after N turns"), `getValidTurn()` and `getVariedValue()`. The live values equal the stored `interest`, `min_favor` and `max_favor` on every card checked (see the previous note).
- Stored favor and interest in the pre-update fixture are close to, but mostly not equal to, the readings in an amity tracker dataset from an older patch. Against 62 cards, 2 match exactly, 55 are within 5 on every value, and seven differ by 6 to 44, for example `6161` Slum in the City (interest `59` stored, `15` seen) and `4333` Calpheon Giant Bee (`28` / `24`-`30` stored, `2` / `40`-`47` seen). The dataset does not say which NPC each reading came from. No NPC in the current `npcpersonality.dbss` has card `4333`'s theme (`10321`, Creatures of Northern Calpheon) as an interest group.

## Open Questions

### Unknown Body And Tail Fields

`unknown_06`, `unknown_07`, `unknown_description_kr_00`, `unknown_description_kr_02`, `unknown_acquisition_kr_0c`, `unknown_acquisition_kr_0d` and `unknown_hashes` are not decoded. `unknown_description_kr_02` 1 to 4 appears on single NPC cards such as the Sausan Scout, Sniper and Assassin, which suggests a small enum.

### Position Meaning

The position is a world point, but which one is not settled. Town and NPC cards sit on their node or NPC (see Notes). The Iliya Island card (`3030`, `159209, -7831, 292072`) sits about 22 m from the Iliya Island node (`1002`, `157320, 290939`), so it marks the island, the exploration source in its acquisition text, and not Igor Bartali in Velia, its amity source. The Velia card (`3001`, `152611, -7849, 290383`) is the odd one: it also sits on Iliya Island, about 47 m from that node, instead of on the Velia node. Among its sources, only Diega (Amity) is on Iliya Island, but Diega's own card (`387`) sits about 72 m from it.
