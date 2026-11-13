# `skilltype.dbss` Format

## Purpose

The presentation record of every skill: the Korean skill name, its family
name, whether it is active or passive, the skill icon, its description and
whether it is an Awakening weapon skill. Most other fields copy the learning
rules of [`skillsimply.dbss`](skillsimply_dbss.md) for the same key. This is
where a skill's icon and its Awakening type come from.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes     | Records                       | Row bytes                    |
| ------ | -------------- | ---------------------- | --------- | ----------------------------- | ---------------------------- |
| 5      | 2259 and later | `skilltype.dbss`       | 8,685,956 | 30,475 Payload, 30,475 Record | 153 to 1,041, 281 on average |
| 5      | 2259 and later | `skilltypeoffset.dbss` | 365,720   | 30,475 Index Row              | 12                           |
| 4      | 1529 to 2250   | `skilltype.dbss`       | 7,826,183 | 25,941 Payload, 25,941 Record | 173 to 1,023, 298 on average |
| 4      | 1529 to 2250   | `skilltypeoffset.dbss` | 311,312   | 25,941 Index Row              | 12                           |
| 3      | 1519 to 1524   | `skilltype.dbss`       | 6,129,022 | 20,898 Payload, 20,898 Record | 165 to 1,015, 289 on average |
| 3      | 1519 to 1524   | `skilltypeoffset.dbss` | 250,796   | 20,898 Index Row              | 12                           |
| 2      | 1381 to 1509   | `skilltype.dbss`       | 6,070,920 | 20,764 Payload, 20,764 Record | 164 to 1,014, 288 on average |
| 2      | 1381 to 1509   | `skilltypeoffset.dbss` | 249,188   | 20,764 Index Row              | 12                           |
| 1      | 1346 to 1379   | `skilltype.dbss`       | 5,847,163 | 19,565 Payload, 19,565 Record | 163 to 1,062, 295 on average |
| 1      | 1346 to 1379   | `skilltypeoffset.dbss` | 234,800   | 19,565 Index Row              | 12                           |

| Layout | File                   | Known               | Unknown             |
| ------ | ---------------------- | ------------------- | ------------------- |
| 5      | `skilltype.dbss`       | 6,589,780 B (75.9%) | 2,096,176 B (24.1%) |
| 5      | `skilltypeoffset.dbss` | 365,720 B (100.0%)  | 0 B (0.0%)          |
| 4      | `skilltype.dbss`       | 5,828,151 B (74.5%) | 1,998,032 B (25.5%) |
| 4      | `skilltypeoffset.dbss` | 311,312 B (100.0%)  | 0 B (0.0%)          |
| 3      | `skilltype.dbss`       | 4,673,410 B (76.3%) | 1,455,612 B (23.7%) |
| 3      | `skilltypeoffset.dbss` | 250,796 B (100.0%)  | 0 B (0.0%)          |
| 2      | `skilltype.dbss`       | 4,645,944 B (76.5%) | 1,424,976 B (23.5%) |
| 2      | `skilltypeoffset.dbss` | 249,188 B (100.0%)  | 0 B (0.0%)          |
| 1      | `skilltype.dbss`       | 4,508,247 B (77.1%) | 1,338,916 B (22.9%) |
| 1      | `skilltypeoffset.dbss` | 234,800 B (100.0%)  | 0 B (0.0%)          |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 5             | `2067dedbd39e`  |
| 3482   | Layout 5             | `2067dedbd39e`  |
| 3474   | Layout 5             | `2067dedbd39e`  |
| 3473   | Layout 5             | `2067dedbd39e`  |
| 3464   | Layout 5             | `2067dedbd39e`  |
| 3458   | Layout 5             | `2067dedbd39e`  |
| 3454   | Layout 5             | `2067dedbd39e`  |
| 3444   | Layout 5             | `2067dedbd39e`  |
| 3435   | Layout 5             | `2067dedbd39e`  |
| 3426   | Layout 5             | `2067dedbd39e`  |
| 3418   | Layout 5             | `2067dedbd39e`  |
| 3412   | Layout 5             | `2067dedbd39e`  |
| 3402   | Layout 5             | `2067dedbd39e`  |
| 3396   | Layout 5             | `2067dedbd39e`  |
| 3387   | Layout 5             | `2067dedbd39e`  |
| 3381   | Layout 5             | `2067dedbd39e`  |
| 3373   | Layout 5             | `2067dedbd39e`  |
| 3364   | Layout 5             | `2067dedbd39e`  |
| 3356   | Layout 5             | `2067dedbd39e`  |
| 3349   | Layout 5             | `2067dedbd39e`  |
| 3342   | Layout 5             | `2067dedbd39e`  |
| 3335   | Layout 5             | `2067dedbd39e`  |
| 3326   | Layout 5             | `2067dedbd39e`  |
| 3321   | Layout 5             | `2067dedbd39e`  |
| 3314   | Layout 5             | `2067dedbd39e`  |
| 3303   | Layout 5             | `2067dedbd39e`  |
| 3302   | Layout 5             | `2067dedbd39e`  |
| 3293   | Layout 5             | `2067dedbd39e`  |
| 3283   | Layout 5             | `2067dedbd39e`  |
| 3275   | Layout 5             | `2067dedbd39e`  |
| 3267   | Layout 5             | `2067dedbd39e`  |
| 3258   | Layout 5             | `2067dedbd39e`  |
| 3251   | Layout 5             | `2067dedbd39e`  |
| 3242   | Layout 5             | `2067dedbd39e`  |
| 3235   | Layout 5             | `2067dedbd39e`  |
| 3229   | Layout 5             | `2067dedbd39e`  |
| 3212   | Layout 5             | `2067dedbd39e`  |
| 3203   | Layout 5             | `2067dedbd39e`  |
| 3193   | Layout 5             | `2067dedbd39e`  |
| 3186   | Layout 5             | `2067dedbd39e`  |
| 3177   | Layout 5             | `2067dedbd39e`  |
| 3169   | Layout 5             | `2067dedbd39e`  |
| 3158   | Layout 5             | `2067dedbd39e`  |
| 3151   | Layout 5             | `2067dedbd39e`  |
| 3144   | Layout 5             | `2067dedbd39e`  |
| 3133   | Layout 5             | `2067dedbd39e`  |
| 3125   | Layout 5             | `2067dedbd39e`  |
| 3118   | Layout 5             | `2067dedbd39e`  |
| 3111   | Layout 5             | `2067dedbd39e`  |
| 3103   | Layout 5             | `2067dedbd39e`  |
| 3095   | Layout 5             | `2067dedbd39e`  |
| 3086   | Layout 5             | `2067dedbd39e`  |
| 3072   | Layout 5             | `2067dedbd39e`  |
| 3062   | Layout 5             | `2067dedbd39e`  |
| 3052   | Layout 5             | `2067dedbd39e`  |
| 3045   | Layout 5             | `2067dedbd39e`  |
| 3037   | Layout 5             | `2067dedbd39e`  |
| 3030   | Layout 5             | `2067dedbd39e`  |
| 3021   | Layout 5             | `2067dedbd39e`  |
| 3012   | Layout 5             | `2067dedbd39e`  |
| 3002   | Layout 5             | `2067dedbd39e`  |
| 2995   | Layout 5             | `2067dedbd39e`  |
| 2987   | Layout 5             | `2067dedbd39e`  |
| 2978   | Layout 5             | `2067dedbd39e`  |
| 2970   | Layout 5             | `2067dedbd39e`  |
| 2959   | Layout 5             | `2067dedbd39e`  |
| 2951   | Layout 5             | `2067dedbd39e`  |
| 2942   | Layout 5             | `2067dedbd39e`  |
| 2935   | Layout 5             | `2067dedbd39e`  |
| 2932   | Layout 5             | `2067dedbd39e`  |
| 2923   | Layout 5             | `2067dedbd39e`  |
| 2919   | Layout 5             | `2067dedbd39e`  |
| 2907   | Layout 5             | `2067dedbd39e`  |
| 2900   | Layout 5             | `2067dedbd39e`  |
| 2891   | Layout 5             | `2067dedbd39e`  |
| 2882   | Layout 5             | `2067dedbd39e`  |
| 2872   | Layout 5             | `2067dedbd39e`  |
| 2863   | Layout 5             | `2067dedbd39e`  |
| 2855   | Layout 5             | `2067dedbd39e`  |
| 2849   | Layout 5             | `2067dedbd39e`  |
| 2844   | Layout 5             | `2067dedbd39e`  |
| 2834   | Layout 5             | `2067dedbd39e`  |
| 2825   | Layout 5             | `2067dedbd39e`  |
| 2819   | Layout 5             | `2067dedbd39e`  |
| 2811   | Layout 5             | `2067dedbd39e`  |
| 2803   | Layout 5             | `2067dedbd39e`  |
| 2794   | Layout 5             | `2067dedbd39e`  |
| 2783   | Layout 5             | `2067dedbd39e`  |
| 2774   | Layout 5             | `2067dedbd39e`  |
| 2765   | Layout 5             | `2067dedbd39e`  |
| 2756   | Layout 5             | `2067dedbd39e`  |
| 2750   | Layout 5             | `2067dedbd39e`  |
| 2743   | Layout 5             | `2067dedbd39e`  |
| 2736   | Layout 5             | `2067dedbd39e`  |
| 2726   | Layout 5             | `2067dedbd39e`  |
| 2717   | Layout 5             | `2067dedbd39e`  |
| 2709   | Layout 5             | `2067dedbd39e`  |
| 2703   | Layout 5             | `2067dedbd39e`  |
| 2695   | Layout 5             | `2067dedbd39e`  |
| 2684   | Layout 5             | `2067dedbd39e`  |
| 2672   | Layout 5             | `2067dedbd39e`  |
| 2665   | Layout 5             | `2067dedbd39e`  |
| 2657   | Layout 5             | `2067dedbd39e`  |
| 2649   | Layout 5             | `2067dedbd39e`  |
| 2644   | Layout 5             | `2067dedbd39e`  |
| 2637   | Layout 5             | `2067dedbd39e`  |
| 2629   | Layout 5             | `2067dedbd39e`  |
| 2619   | Layout 5             | `2067dedbd39e`  |
| 2612   | Layout 5             | `2067dedbd39e`  |
| 2606   | Layout 5             | `2067dedbd39e`  |
| 2602   | Layout 5             | `2067dedbd39e`  |
| 2601   | Layout 5             | `2067dedbd39e`  |
| 2592   | Layout 5             | `2067dedbd39e`  |
| 2583   | Layout 5             | `2067dedbd39e`  |
| 2575   | Layout 5             | `2067dedbd39e`  |
| 2567   | Layout 5             | `2067dedbd39e`  |
| 2560   | Layout 5             | `2067dedbd39e`  |
| 2553   | Layout 5             | `2067dedbd39e`  |
| 2545   | Layout 5             | `2067dedbd39e`  |
| 2538   | Layout 5             | `2067dedbd39e`  |
| 2529   | Layout 5             | `2067dedbd39e`  |
| 2519   | Layout 5             | `2067dedbd39e`  |
| 2513   | Layout 5             | `2067dedbd39e`  |
| 2510   | Layout 5             | `2067dedbd39e`  |
| 2507   | Layout 5             | `2067dedbd39e`  |
| 2503   | Layout 5             | `2067dedbd39e`  |
| 2498   | Layout 5             | `2067dedbd39e`  |
| 2492   | Layout 5             | `2067dedbd39e`  |
| 2487   | Layout 5             | `2067dedbd39e`  |
| 2480   | Layout 5             | `2067dedbd39e`  |
| 2474   | Layout 5             | `2067dedbd39e`  |
| 2468   | Layout 5             | `2067dedbd39e`  |
| 2460   | Layout 5             | `2067dedbd39e`  |
| 2453   | Layout 5             | `2067dedbd39e`  |
| 2444   | Layout 5             | `2067dedbd39e`  |
| 2438   | Layout 5             | `2067dedbd39e`  |
| 2434   | Layout 5             | `2067dedbd39e`  |
| 2429   | Layout 5             | `2067dedbd39e`  |
| 2421   | Layout 5             | `2067dedbd39e`  |
| 2414   | Layout 5             | `2067dedbd39e`  |
| 2407   | Layout 5             | `2067dedbd39e`  |
| 2401   | Layout 5             | `2067dedbd39e`  |
| 2397   | Layout 5             | `2067dedbd39e`  |
| 2393   | Layout 5             | `2067dedbd39e`  |
| 2384   | Layout 5             | `2067dedbd39e`  |
| 2378   | Layout 5             | `2067dedbd39e`  |
| 2372   | Layout 5             | `2067dedbd39e`  |
| 2358   | Layout 5             | `2067dedbd39e`  |
| 2352   | Layout 5             | `2067dedbd39e`  |
| 2347   | Layout 5             | `2067dedbd39e`  |
| 2343   | Layout 5             | `2067dedbd39e`  |
| 2335   | Layout 5             | `2067dedbd39e`  |
| 2327   | Layout 5             | `2067dedbd39e`  |
| 2324   | Layout 5             | `2067dedbd39e`  |
| 2319   | Layout 5             | `2067dedbd39e`  |
| 2313   | Layout 5             | `2067dedbd39e`  |
| 2308   | Layout 5             | `2067dedbd39e`  |
| 2302   | Layout 5             | `2067dedbd39e`  |
| 2295   | Layout 5             | `2067dedbd39e`  |
| 2290   | Layout 5             | `2067dedbd39e`  |
| 2284   | Layout 5             | `2067dedbd39e`  |
| 2276   | Layout 5             | `2067dedbd39e`  |
| 2269   | Layout 5             | `2067dedbd39e`  |
| 2259   | Layout 5             | `2067dedbd39e`  |
| 2250   | Layout 4             | `2067dedbd39e`  |
| 2243   | Layout 4             | `2067dedbd39e`  |
| 2235   | Layout 4             | `2067dedbd39e`  |
| 2229   | Layout 4             | `2067dedbd39e`  |
| 2224   | Layout 4             | `2067dedbd39e`  |
| 2218   | Layout 4             | `2067dedbd39e`  |
| 2215   | Layout 4             | `2067dedbd39e`  |
| 2207   | Layout 4             | `2067dedbd39e`  |
| 2203   | Layout 4             | `2067dedbd39e`  |
| 2196   | Layout 4             | `2067dedbd39e`  |
| 2192   | Layout 4             | `2067dedbd39e`  |
| 2189   | Layout 4             | `2067dedbd39e`  |
| 2183   | Layout 4             | `2067dedbd39e`  |
| 2179   | Layout 4             | `2067dedbd39e`  |
| 2171   | Layout 4             | `2067dedbd39e`  |
| 2163   | Layout 4             | `2067dedbd39e`  |
| 2156   | Layout 4             | `2067dedbd39e`  |
| 2151   | Layout 4             | `2067dedbd39e`  |
| 2147   | Layout 4             | `2067dedbd39e`  |
| 2142   | Layout 4             | `2067dedbd39e`  |
| 2138   | Layout 4             | `2067dedbd39e`  |
| 2134   | Layout 4             | `2067dedbd39e`  |
| 2130   | Layout 4             | `2067dedbd39e`  |
| 2122   | Layout 4             | `2067dedbd39e`  |
| 2107   | Layout 4             | `2067dedbd39e`  |
| 2098   | Layout 4             | `2067dedbd39e`  |
| 2089   | Layout 4             | `2067dedbd39e`  |
| 2081   | Layout 4             | `2067dedbd39e`  |
| 2073   | Layout 4             | `2067dedbd39e`  |
| 2067   | Layout 4             | `2067dedbd39e`  |
| 2063   | Layout 4             | `2067dedbd39e`  |
| 2059   | Layout 4             | `2067dedbd39e`  |
| 2052   | Layout 4             | `2067dedbd39e`  |
| 2044   | Layout 4             | `2067dedbd39e`  |
| 2039   | Layout 4             | `2067dedbd39e`  |
| 2032   | Layout 4             | `2067dedbd39e`  |
| 2025   | Layout 4             | `2067dedbd39e`  |
| 2011   | Layout 4             | `2067dedbd39e`  |
| 2005   | Layout 4             | `2067dedbd39e`  |
| 2000   | Layout 4             | `2067dedbd39e`  |
| 1996   | Layout 4             | `2067dedbd39e`  |
| 1991   | Layout 4             | `2067dedbd39e`  |
| 1985   | Layout 4             | `2067dedbd39e`  |
| 1980   | Layout 4             | `2067dedbd39e`  |
| 1969   | Layout 4             | `2067dedbd39e`  |
| 1964   | Layout 4             | `2067dedbd39e`  |
| 1958   | Layout 4             | `2067dedbd39e`  |
| 1950   | Layout 4             | `2067dedbd39e`  |
| 1945   | Layout 4             | `2067dedbd39e`  |
| 1937   | Layout 4             | `2067dedbd39e`  |
| 1933   | Layout 4             | `2067dedbd39e`  |
| 1927   | Layout 4             | `2067dedbd39e`  |
| 1921   | Layout 4             | `2067dedbd39e`  |
| 1914   | Layout 4             | `2067dedbd39e`  |
| 1908   | Layout 4             | `2067dedbd39e`  |
| 1897   | Layout 4             | `2067dedbd39e`  |
| 1892   | Layout 4             | `2067dedbd39e`  |
| 1886   | Layout 4             | `2067dedbd39e`  |
| 1881   | Layout 4             | `2067dedbd39e`  |
| 1871   | Layout 4             | `2067dedbd39e`  |
| 1866   | Layout 4             | `2067dedbd39e`  |
| 1862   | Layout 4             | `2067dedbd39e`  |
| 1854   | Layout 4             | `2067dedbd39e`  |
| 1846   | Layout 4             | `2067dedbd39e`  |
| 1838   | Layout 4             | `2067dedbd39e`  |
| 1832   | Layout 4             | `2067dedbd39e`  |
| 1826   | Layout 4             | `2067dedbd39e`  |
| 1822   | Layout 4             | `2067dedbd39e`  |
| 1818   | Layout 4             | `2067dedbd39e`  |
| 1804   | Layout 4             | `2067dedbd39e`  |
| 1794   | Layout 4             | `2067dedbd39e`  |
| 1790   | Layout 4             | `2067dedbd39e`  |
| 1784   | Layout 4             | `2067dedbd39e`  |
| 1774   | Layout 4             | `2067dedbd39e`  |
| 1771   | Layout 4             | `2067dedbd39e`  |
| 1762   | Layout 4             | `2067dedbd39e`  |
| 1759   | Layout 4             | `2067dedbd39e`  |
| 1754   | Layout 4             | `2067dedbd39e`  |
| 1749   | Layout 4             | `2067dedbd39e`  |
| 1743   | Layout 4             | `2067dedbd39e`  |
| 1737   | Layout 4             | `2067dedbd39e`  |
| 1731   | Layout 4             | `2067dedbd39e`  |
| 1725   | Layout 4             | `2067dedbd39e`  |
| 1717   | Layout 4             | `2067dedbd39e`  |
| 1710   | Layout 4             | `2067dedbd39e`  |
| 1704   | Layout 4             | `2067dedbd39e`  |
| 1698   | Layout 4             | `2067dedbd39e`  |
| 1690   | Layout 4             | `2067dedbd39e`  |
| 1685   | Layout 4             | `2067dedbd39e`  |
| 1680   | Layout 4             | `2067dedbd39e`  |
| 1674   | Layout 4             | `2067dedbd39e`  |
| 1668   | Layout 4             | `2067dedbd39e`  |
| 1659   | Layout 4             | `2067dedbd39e`  |
| 1649   | Layout 4             | `2067dedbd39e`  |
| 1642   | Layout 4             | `2067dedbd39e`  |
| 1636   | Layout 4             | `2067dedbd39e`  |
| 1628   | Layout 4             | `2067dedbd39e`  |
| 1622   | Layout 4             | `2067dedbd39e`  |
| 1614   | Layout 4             | `2067dedbd39e`  |
| 1608   | Layout 4             | `2067dedbd39e`  |
| 1602   | Layout 4             | `2067dedbd39e`  |
| 1598   | Layout 4             | `2067dedbd39e`  |
| 1594   | Layout 4             | `2067dedbd39e`  |
| 1590   | Layout 4             | `2067dedbd39e`  |
| 1587   | Layout 4             | `2067dedbd39e`  |
| 1584   | Layout 4             | `2067dedbd39e`  |
| 1579   | Layout 4             | `2067dedbd39e`  |
| 1572   | Layout 4             | `2067dedbd39e`  |
| 1565   | Layout 4             | `2067dedbd39e`  |
| 1559   | Layout 4             | `2067dedbd39e`  |
| 1554   | Layout 4             | `2067dedbd39e`  |
| 1547   | Layout 4             | `2067dedbd39e`  |
| 1537   | Layout 4             | `2067dedbd39e`  |
| 1529   | Layout 4             | `2067dedbd39e`  |
| 1524   | Layout 3             | `2067dedbd39e`  |
| 1519   | Layout 3             | `2067dedbd39e`  |
| 1509   | Layout 2             | `2067dedbd39e`  |
| 1506   | Layout 2             | `2067dedbd39e`  |
| 1504   | Layout 2             | `2067dedbd39e`  |
| 1500   | Layout 2             | `2067dedbd39e`  |
| 1493   | Layout 2             | `2067dedbd39e`  |
| 1489   | Layout 2             | `2067dedbd39e`  |
| 1485   | Layout 2             | `2067dedbd39e`  |
| 1481   | Layout 2             | `2067dedbd39e`  |
| 1474   | Layout 2             | `2067dedbd39e`  |
| 1466   | Layout 2             | `2067dedbd39e`  |
| 1462   | Layout 2             | `2067dedbd39e`  |
| 1459   | Layout 2             | `2067dedbd39e`  |
| 1453   | Layout 2             | `2067dedbd39e`  |
| 1450   | Layout 2             | `2067dedbd39e`  |
| 1445   | Layout 2             | `2067dedbd39e`  |
| 1439   | Layout 2             | `2067dedbd39e`  |
| 1433   | Layout 2             | `2067dedbd39e`  |
| 1430   | Layout 2             | `2067dedbd39e`  |
| 1426   | Layout 2             | `2067dedbd39e`  |
| 1421   | Layout 2             | `2067dedbd39e`  |
| 1417   | Layout 2             | `2067dedbd39e`  |
| 1416   | Layout 2             | `2067dedbd39e`  |
| 1409   | Layout 2             | `2067dedbd39e`  |
| 1405   | Layout 2             | `2067dedbd39e`  |
| 1401   | Layout 2             | `2067dedbd39e`  |
| 1396   | Layout 2             | `2067dedbd39e`  |
| 1391   | Layout 2             | `2067dedbd39e`  |
| 1390   | Layout 2             | `2067dedbd39e`  |
| 1386   | Layout 2             | `2067dedbd39e`  |
| 1381   | Layout 2             | `2067dedbd39e`  |
| 1379   | Layout 1             | `2067dedbd39e`  |
| 1372   | Layout 1             | `2067dedbd39e`  |
| 1366   | Layout 1             | `2067dedbd39e`  |
| 1364   | Layout 1             | `2067dedbd39e`  |
| 1363   | Layout 1             | `2067dedbd39e`  |
| 1360   | Layout 1             | `2067dedbd39e`  |
| 1358   | Layout 1             | `2067dedbd39e`  |
| 1355   | Layout 1             | `2067dedbd39e`  |
| 1351   | Layout 1             | `2067dedbd39e`  |
| 1348   | Layout 1             | `2067dedbd39e`  |
| 1346   | Layout 1             | `2067dedbd39e`  |
| 1341   | No documented layout | `2067dedbd39e`  |
| 1340   | No documented layout | `2067dedbd39e`  |
| 1338   | No documented layout | `2067dedbd39e`  |
| 1335   | No documented layout | `2067dedbd39e`  |
| 1333   | No documented layout | `2067dedbd39e`  |
| 1329   | No documented layout | `2067dedbd39e`  |
| 1327   | No documented layout | `2067dedbd39e`  |
| 1324   | No documented layout | `2067dedbd39e`  |
| 1321   | No documented layout | `2067dedbd39e`  |
| 1319   | No documented layout | `2067dedbd39e`  |
| 1318   | No documented layout | `2067dedbd39e`  |
| 1316   | No documented layout | `2067dedbd39e`  |
| 1313   | No documented layout | `2067dedbd39e`  |
| 1311   | No documented layout | `2067dedbd39e`  |
| 1309   | No documented layout | `2067dedbd39e`  |
| 1304   | No documented layout | `2067dedbd39e`  |
| 1292   | No documented layout | `2067dedbd39e`  |
| 1286   | No file              | `2067dedbd39e`  |
| 1280   | No file              | `2067dedbd39e`  |
| 1276   | No file              | `2067dedbd39e`  |
| 1267   | No file              | `2067dedbd39e`  |
| 1261   | No file              | `2067dedbd39e`  |
| 1256   | No file              | `2067dedbd39e`  |
| 1250   | No file              | `2067dedbd39e`  |
| 1246   | No file              | `2067dedbd39e`  |
| 1239   | No file              | `2067dedbd39e`  |
| 1230   | No file              | `2067dedbd39e`  |
| 1226   | No file              | `2067dedbd39e`  |
| 1220   | No file              | `2067dedbd39e`  |
| 1217   | No file              | `2067dedbd39e`  |
| 1211   | No file              | `2067dedbd39e`  |
| 1210   | No file              | `2067dedbd39e`  |
| 1208   | No file              | `2067dedbd39e`  |
| 1203   | No file              | `2067dedbd39e`  |
| 1197   | No file              | `2067dedbd39e`  |
| 1194   | No file              | `2067dedbd39e`  |
| 1192   | No file              | `2067dedbd39e`  |
| 1187   | No file              | `2067dedbd39e`  |
| 1183   | No file              | `2067dedbd39e`  |
| 1177   | No file              | `2067dedbd39e`  |
| 1173   | No file              | `2067dedbd39e`  |
| 1167   | No file              | `2067dedbd39e`  |
| 1164   | No file              | `2067dedbd39e`  |
| 1156   | No file              | `2067dedbd39e`  |
| 1149   | No file              | `2067dedbd39e`  |
| 1144   | No file              | `2067dedbd39e`  |
| 1137   | No file              | `2067dedbd39e`  |
| 1132   | No file              | `2067dedbd39e`  |
| 1127   | No file              | `2067dedbd39e`  |
| 1122   | No file              | `2067dedbd39e`  |
| 1118   | No file              | `2067dedbd39e`  |
| 1114   | No file              | `2067dedbd39e`  |
| 1109   | No file              | `2067dedbd39e`  |
| 1102   | No file              | `2067dedbd39e`  |
| 1096   | No file              | `2067dedbd39e`  |
| 1088   | No file              | `2067dedbd39e`  |
| 1081   | No file              | `2067dedbd39e`  |
| 1076   | No file              | `2067dedbd39e`  |
| 1069   | No file              | `2067dedbd39e`  |
| 1064   | No file              | `2067dedbd39e`  |
| 1058   | No file              | `2067dedbd39e`  |
| 1051   | No file              | `2067dedbd39e`  |
| 1044   | No file              | `2067dedbd39e`  |
| 1036   | No file              | `2067dedbd39e`  |
| 1026   | No file              | `2067dedbd39e`  |
| 1016   | No file              | `2067dedbd39e`  |
| 1009   | No file              | `2067dedbd39e`  |
| 1005   | No file              | `2067dedbd39e`  |
| 1000   | No file              | `2067dedbd39e`  |
| 998    | No file              | `2067dedbd39e`  |
| 990    | No file              | `2067dedbd39e`  |
| 979    | No file              | `2067dedbd39e`  |
| 972    | No file              | `2067dedbd39e`  |
| 963    | No file              | `2067dedbd39e`  |
| 955    | No file              | `2067dedbd39e`  |
| 946    | No file              | `2067dedbd39e`  |
| 938    | No file              | `2067dedbd39e`  |
| 927    | No file              | `2067dedbd39e`  |
| 911    | No file              | `2067dedbd39e`  |
| 904    | No file              | `2067dedbd39e`  |
| 899    | No file              | `2067dedbd39e`  |
| 894    | No file              | `2067dedbd39e`  |
| 885    | No file              | `2067dedbd39e`  |
| 879    | No file              | `2067dedbd39e`  |
| 872    | No file              | `2067dedbd39e`  |
| 864    | No file              | `2067dedbd39e`  |
| 855    | No file              | `2067dedbd39e`  |
| 853    | No file              | `2067dedbd39e`  |
| 845    | No file              | `2067dedbd39e`  |
| 837    | No file              | `2067dedbd39e`  |
| 829    | No file              | `2067dedbd39e`  |
| 822    | No file              | `2067dedbd39e`  |
| 814    | No file              | `2067dedbd39e`  |
| 805    | No file              | `2067dedbd39e`  |
| 794    | No file              | `2067dedbd39e`  |
| 787    | No file              | `2067dedbd39e`  |
| 780    | No file              | `2067dedbd39e`  |
| 771    | No file              | `2067dedbd39e`  |
| 760    | No file              | `2067dedbd39e`  |
| 748    | No file              | `2067dedbd39e`  |
| 741    | No file              | `2067dedbd39e`  |
| 736    | No file              | `2067dedbd39e`  |
| 731    | No file              | `2067dedbd39e`  |
| 723    | No file              | `2067dedbd39e`  |
| 711    | No file              | `2067dedbd39e`  |
| 707    | No file              | `2067dedbd39e`  |
| 697    | No file              | `2067dedbd39e`  |
| 689    | No file              | `2067dedbd39e`  |
| 683    | No file              | `2067dedbd39e`  |
| 678    | No file              | `2067dedbd39e`  |
| 670    | No file              | `2067dedbd39e`  |
| 661    | No file              | `2067dedbd39e`  |
| 656    | No file              | `2067dedbd39e`  |
| 652    | No file              | `2067dedbd39e`  |
| 643    | No file              | `2067dedbd39e`  |
| 637    | No file              | `2067dedbd39e`  |
| 630    | No file              | `2067dedbd39e`  |
| 627    | No file              | `2067dedbd39e`  |
| 621    | No file              | `2067dedbd39e`  |
| 617    | No file              | `2067dedbd39e`  |
| 615    | No file              | `2067dedbd39e`  |
| 606    | No file              | `2067dedbd39e`  |
| 599    | No file              | `2067dedbd39e`  |
| 592    | No file              | `2067dedbd39e`  |
| 586    | No file              | `2067dedbd39e`  |
| 577    | No file              | `2067dedbd39e`  |
| 569    | No file              | `2067dedbd39e`  |
| 561    | No file              | `2067dedbd39e`  |
| 554    | No file              | `2067dedbd39e`  |
| 542    | No file              | `2067dedbd39e`  |
| 532    | No file              | `2067dedbd39e`  |
| 531    | No file              | `2067dedbd39e`  |
| 526    | No file              | `2067dedbd39e`  |
| 521    | No file              | `2067dedbd39e`  |
| 517    | No file              | `2067dedbd39e`  |
| 510    | No file              | `2067dedbd39e`  |
| 508    | No file              | `2067dedbd39e`  |
| 504    | No file              | `2067dedbd39e`  |
| 497    | No file              | `2067dedbd39e`  |
| 491    | No file              | `2067dedbd39e`  |
| 485    | No file              | `2067dedbd39e`  |
| 478    | No file              | `2067dedbd39e`  |
| 472    | No file              | `2067dedbd39e`  |
| 466    | No file              | `2067dedbd39e`  |
| 457    | No file              | `2067dedbd39e`  |
| 452    | No file              | `2067dedbd39e`  |
| 449    | No file              | `2067dedbd39e`  |
| 435    | No file              | `2067dedbd39e`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                               |
| ---------------------- | -------- | -------------------------------------------------- |
| `skilltypeoffset.dbss` | Required | `skill_key → (offset, size)` index into this file  |
| `languagedata_en.loc`  | Optional | English names, LOC type `10`, `str_id1 = skill_no` |

The skill key is the one shared by the whole skill cluster; see
[`skill.dbss` Skill Keys](skill_dbss.md#skill-keys). All multi-byte values are
little-endian.

## Layout 5

### File Layout

The records tile the file like `skill.dbss`: each starts 4 bytes after the
previous one ends, the first at `8`, and the last ends at end of file. Strings
are a `u64` count followed by UTF-16LE units (text) or ASCII bytes (paths).

Every key is level `1`. 30,342 of the 30,352 keys are also in `skill.dbss`;
the 82 `skill.dbss` keys above level 1 have no record here.

| Offset  | Type          | Field   | Notes                                      |
| ------- | ------------- | ------- | ------------------------------------------ |
| `+0x00` | u32           | count   | Number of records; matches the offset file |
| `+0x04` | Record[count] | records | See Record                                 |

### Record (variable: 4 bytes + payload)

| Offset  | Type    | Field      | Notes                                                       |
| ------- | ------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32     | key_prefix | Each record is preceded by a repeated copy of its key       |
| `+0x04` | Payload | payload    | `size` bytes; the index row's `offset` points at this field |

### Payload (variable: 141 bytes + text and lists, size from `skilltypeoffset.dbss`)

Most fields after `kind` are copies of `skillsimply.dbss` fields of the same
key; the notes say "as `skillsimply.dbss`" where the two hold the same value
on every one of the 30,465 shared keys of clients 1784 and 3483. Record
counts are from client 3483. The sheet columns behind the fields are in
Field Names.

| Offset                         | Type                      | Field                     | Notes                                                                                            |
| ------------------------------ | ------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------ |
| `+0x00`                        | u32                       | skill_key                 | Equals the index key                                                                             |
| `+0x04`                        | str16                     | name                      | Korean skill name, e.g. `거대한 진노 III`                                                             |
| `name+0x00`                    | str16                     | group_name                | Korean family name, see [`group_name`](#group_name)                                              |
| `group_name+0x00`              | u32                       | kind                      | `0` other, `1` active, `2` passive; see [`kind`](#kind)                                          |
| `group_name+0x04`              | u16                       | unknown_group_name_04     | A skill number of this table on 4,622 records, else `0`; see Field Names                         |
| `group_name+0x06`              | u32                       | next_rank_count           | As `skillsimply.dbss`                                                                            |
| `group_name+0x0A`              | u32[next_rank_count]      | next_rank_keys            | As `skillsimply.dbss`                                                                            |
| `next_rank_keys+0x00`          | u64                       | class_mask                | Bit `n` set: class type `n` can learn it; as `skillsimply.dbss`, see [`class_mask`](#class_mask) |
| `next_rank_keys+0x08`          | u64                       | unknown_next_rank_keys_08 | Always `0`                                                                                       |
| `next_rank_keys+0x10`          | u8                        | require_equip_type        | As `skillsimply.dbss`                                                                            |
| `next_rank_keys+0x11`          | u8                        | uses_main_weapon          | As `skillsimply.dbss`                                                                            |
| `next_rank_keys+0x12`          | u8                        | uses_sub_weapon           | As `skillsimply.dbss`                                                                            |
| `next_rank_keys+0x13`          | bytes[4]                  | unknown_next_rank_keys_13 | The `skillsimply.dbss` bytes `unknown_n03` to `unknown_n06`                                      |
| `next_rank_keys+0x17`          | u8                        | require_equip_slot        | As `skillsimply.dbss`                                                                            |
| `next_rank_keys+0x18`          | u8                        | unknown_next_rank_keys_18 | The `skillsimply.dbss` byte `unknown_n08`                                                        |
| `next_rank_keys+0x19`          | u16                       | max_level                 | As `skillsimply.dbss`                                                                            |
| `next_rank_keys+0x1B`          | u32                       | skill_owner_type          | As `skillsimply.dbss`                                                                            |
| `next_rank_keys+0x1F`          | u32                       | first_rank_key            | As `skillsimply.dbss`                                                                            |
| `next_rank_keys+0x23`          | str8                      | icon_path                 | Icon path, see [`icon_path`](#icon_path)                                                         |
| `icon_path+0x00`               | str16                     | unknown_after_icon_path   | Empty on 29,223 records, `UNKNOWN` on 1,250                                                      |
| `unknown_after_icon_path+0x00` | str16                     | description               | Korean description; empty on 1,128 records                                                       |
| `description+0x00`             | u8                        | unknown_description_00    | Always `0`                                                                                       |
| `description+0x01`             | u16                       | unknown_description_01    | Bit flags: `2` on 21,463 records, `10` on 3,491, `42` on 2,481                                   |
| `description+0x03`             | u8                        | unknown_description_03    | `1` on 11 records                                                                                |
| `description+0x04`             | u8                        | can_quick_slot            | As `skillsimply.dbss`                                                                            |
| `description+0x05`             | u64                       | unknown_list_count        | `0` on 25,757 records, up to `3`                                                                 |
| `description+0x0D`             | u32[unknown_list_count]   | unknown_list              | Values `0`, `1` and `2`                                                                          |
| `unknown_list+0x00`            | u8                        | awakening_type            | `0` normal, `1` Awakening weapon (1,860 records); see [`awakening_type`](#awakening_type)        |
| `unknown_list+0x01`            | u8                        | unknown_list_01           | `1` on 5,286 records                                                                             |
| `unknown_list+0x02`            | u8                        | unknown_list_02           | `1` on 69 records                                                                                |
| `unknown_list+0x03`            | u8                        | is_developing_contents    | `1` on exactly the 1,250 records whose `name` and `unknown_after_icon_path` are `UNKNOWN`        |
| `unknown_list+0x04`            | u32                       | contents_group_count      | As `skillsimply.dbss`                                                                            |
| `unknown_list+0x08`            | u32[contents_group_count] | contents_group_hashes     | As `skillsimply.dbss`                                                                            |
| `contents_group_hashes+0x00`   | u32                       | exclusive_count           | The `skillsimply.dbss` count is a u64                                                            |
| `contents_group_hashes+0x04`   | u16[exclusive_count]      | exclusive_skill_nos       | As `skillsimply.dbss`                                                                            |
| `exclusive_skill_nos+0x00`     | u8                        | condition                 | As `skillsimply.dbss`                                                                            |
| `exclusive_skill_nos+0x01`     | str16                     | unknown_code              | A class or content code such as `ARCHER_01`, `GUILD_33`; set on 7,955 records                    |
| `unknown_code+0x00`            | u8                        | branch                    | `1` Awakening, `2` Succession, `0` neither; as `skillsimply.dbss`                                |
| `unknown_code+0x01`            | u32                       | unknown_code_01           | Always `0`                                                                                       |
| `unknown_code+0x05`            | u32                       | unknown_code_05           | `0` or a `u16 << 16 \| u16` pair (7,476 records); see Field Names                                |
| `unknown_code+0x09`            | u8                        | unknown_code_09           | `2` on all but 9 records, which hold `1`                                                         |
| `unknown_code+0x0A`            | str16                     | unknown_code_0a           | Always empty                                                                                     |

Every one of the 30,475 records on client 3483 walks to exactly its `size`
with this layout. The shortest is 153 bytes.

### `skilltypeoffset.dbss`

The layout of [`skilloffset.dbss`](skill_dbss.md#skilloffsetdbss). Read it with
`parse_pabr_u32_offset_rows()`.

| Offset              | Type             | Field        | Notes                                        |
| ------------------- | ---------------- | ------------ | -------------------------------------------- |
| `+0x00`             | char[4]          | magic        | ASCII `PABR`                                 |
| `+0x04`             | u32              | count        | Number of index rows; `30352` on client 3458 |
| `+0x08`             | Index Row[count] | rows         | See Index Row                                |
| `rows+0x00`         | String Table     | string_table | Empty: `string_count` is `0`                 |
| `string_table+0x00` | u32              | table_start  | End of the rows, `8 + 12 * count`            |
| `string_table+0x04` | u32              | zero         | Always 0                                     |

### Index Row (12 bytes)

| Offset  | Type | Field     | Notes                                                     |
| ------- | ---- | --------- | --------------------------------------------------------- |
| `+0x00` | u32  | skill_key | `skill_no << 16 \| level`                                 |
| `+0x04` | u32  | offset    | Byte offset of the record's `payload` in `skilltype.dbss` |
| `+0x08` | u32  | size      | Payload size in bytes                                     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                          |
| ------- | ------------------ | ------------ | ------------------------------ |
| `+0x00` | u32                | string_count | `0`                            |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none here |

## Layout 4

Two ASCII paths followed `description`: `movie_path` and
`unknown_after_movie_path`. Only the Payload differs from Layout 5.

### Payload (variable: 157 bytes + text and lists, size from `skilltypeoffset.dbss`)

| Offset                          | Type                      | Field                     | Notes                                                                                                                                                                                   |
| ------------------------------- | ------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+0x00`                         | u32                       | skill_key                 |                                                                                                                                                                                         |
| `+0x04`                         | str16                     | name                      |                                                                                                                                                                                         |
| `name+0x00`                     | str16                     | group_name                |                                                                                                                                                                                         |
| `group_name+0x00`               | u32                       | kind                      |                                                                                                                                                                                         |
| `group_name+0x04`               | u16                       | unknown_group_name_04     |                                                                                                                                                                                         |
| `group_name+0x06`               | u32                       | next_rank_count           |                                                                                                                                                                                         |
| `group_name+0x0A`               | u32[next_rank_count]      | next_rank_keys            |                                                                                                                                                                                         |
| `next_rank_keys+0x00`           | u64                       | class_mask                |                                                                                                                                                                                         |
| `next_rank_keys+0x08`           | u64                       | unknown_next_rank_keys_08 |                                                                                                                                                                                         |
| `next_rank_keys+0x10`           | u8                        | require_equip_type        |                                                                                                                                                                                         |
| `next_rank_keys+0x11`           | u8                        | uses_main_weapon          |                                                                                                                                                                                         |
| `next_rank_keys+0x12`           | u8                        | uses_sub_weapon           |                                                                                                                                                                                         |
| `next_rank_keys+0x13`           | bytes[4]                  | unknown_next_rank_keys_13 |                                                                                                                                                                                         |
| `next_rank_keys+0x17`           | u8                        | require_equip_slot        |                                                                                                                                                                                         |
| `next_rank_keys+0x18`           | u8                        | unknown_next_rank_keys_18 |                                                                                                                                                                                         |
| `next_rank_keys+0x19`           | u16                       | max_level                 |                                                                                                                                                                                         |
| `next_rank_keys+0x1B`           | u32                       | skill_owner_type          |                                                                                                                                                                                         |
| `next_rank_keys+0x1F`           | u32                       | first_rank_key            |                                                                                                                                                                                         |
| `next_rank_keys+0x23`           | str8                      | icon_path                 |                                                                                                                                                                                         |
| `icon_path+0x00`                | str16                     | unknown_after_icon_path   |                                                                                                                                                                                         |
| `unknown_after_icon_path+0x00`  | str16                     | description               |                                                                                                                                                                                         |
| `description+0x00`              | str8                      | movie_path                | A `.webm` skill video on 3,914 records of client 1348, e.g. `UI_Movie/Movie_Pc_Skill/9_PEM_Skill/PEM_3328.webm`; empty on every record of clients 1485, 1636, 1784, 1937, 2107 and 2243 |
| `movie_path+0x00`               | str8                      | unknown_after_movie_path  | Empty on every record of clients 1348 to 2243 checked                                                                                                                                   |
| `unknown_after_movie_path+0x00` | u8                        | unknown_description_00    |                                                                                                                                                                                         |
| `unknown_after_movie_path+0x01` | u16                       | unknown_description_01    |                                                                                                                                                                                         |
| `unknown_after_movie_path+0x03` | u8                        | unknown_description_03    |                                                                                                                                                                                         |
| `unknown_after_movie_path+0x04` | u8                        | can_quick_slot            |                                                                                                                                                                                         |
| `unknown_after_movie_path+0x05` | u64                       | unknown_list_count        |                                                                                                                                                                                         |
| `unknown_after_movie_path+0x0D` | u32[unknown_list_count]   | unknown_list              |                                                                                                                                                                                         |
| `unknown_list+0x00`             | u8                        | awakening_type            |                                                                                                                                                                                         |
| `unknown_list+0x01`             | u8                        | unknown_list_01           |                                                                                                                                                                                         |
| `unknown_list+0x02`             | u8                        | unknown_list_02           |                                                                                                                                                                                         |
| `unknown_list+0x03`             | u8                        | is_developing_contents    |                                                                                                                                                                                         |
| `unknown_list+0x04`             | u32                       | contents_group_count      |                                                                                                                                                                                         |
| `unknown_list+0x08`             | u32[contents_group_count] | contents_group_hashes     |                                                                                                                                                                                         |
| `contents_group_hashes+0x00`    | u32                       | exclusive_count           |                                                                                                                                                                                         |
| `contents_group_hashes+0x04`    | u16[exclusive_count]      | exclusive_skill_nos       |                                                                                                                                                                                         |
| `exclusive_skill_nos+0x00`      | u8                        | condition                 |                                                                                                                                                                                         |
| `exclusive_skill_nos+0x01`      | str16                     | unknown_code              |                                                                                                                                                                                         |
| `unknown_code+0x00`             | u8                        | branch                    |                                                                                                                                                                                         |
| `unknown_code+0x01`             | u32                       | unknown_code_01           |                                                                                                                                                                                         |
| `unknown_code+0x05`             | u32                       | unknown_code_05           |                                                                                                                                                                                         |
| `unknown_code+0x09`             | u8                        | unknown_code_09           |                                                                                                                                                                                         |
| `unknown_code+0x0A`             | str16                     | unknown_code_0a           |                                                                                                                                                                                         |

## Layout 3

The Payload ended after `unknown_code_09`: `unknown_code_0a` did not exist
yet. Only the Payload differs from Layout 4.

### Payload (variable: 149 bytes + text and lists, size from `skilltypeoffset.dbss`)

| Offset                          | Type                      | Field                     | Notes |
| ------------------------------- | ------------------------- | ------------------------- | ----- |
| `+0x00`                         | u32                       | skill_key                 |       |
| `+0x04`                         | str16                     | name                      |       |
| `name+0x00`                     | str16                     | group_name                |       |
| `group_name+0x00`               | u32                       | kind                      |       |
| `group_name+0x04`               | u16                       | unknown_group_name_04     |       |
| `group_name+0x06`               | u32                       | next_rank_count           |       |
| `group_name+0x0A`               | u32[next_rank_count]      | next_rank_keys            |       |
| `next_rank_keys+0x00`           | u64                       | class_mask                |       |
| `next_rank_keys+0x08`           | u64                       | unknown_next_rank_keys_08 |       |
| `next_rank_keys+0x10`           | u8                        | require_equip_type        |       |
| `next_rank_keys+0x11`           | u8                        | uses_main_weapon          |       |
| `next_rank_keys+0x12`           | u8                        | uses_sub_weapon           |       |
| `next_rank_keys+0x13`           | bytes[4]                  | unknown_next_rank_keys_13 |       |
| `next_rank_keys+0x17`           | u8                        | require_equip_slot        |       |
| `next_rank_keys+0x18`           | u8                        | unknown_next_rank_keys_18 |       |
| `next_rank_keys+0x19`           | u16                       | max_level                 |       |
| `next_rank_keys+0x1B`           | u32                       | skill_owner_type          |       |
| `next_rank_keys+0x1F`           | u32                       | first_rank_key            |       |
| `next_rank_keys+0x23`           | str8                      | icon_path                 |       |
| `icon_path+0x00`                | str16                     | unknown_after_icon_path   |       |
| `unknown_after_icon_path+0x00`  | str16                     | description               |       |
| `description+0x00`              | str8                      | movie_path                |       |
| `movie_path+0x00`               | str8                      | unknown_after_movie_path  |       |
| `unknown_after_movie_path+0x00` | u8                        | unknown_description_00    |       |
| `unknown_after_movie_path+0x01` | u16                       | unknown_description_01    |       |
| `unknown_after_movie_path+0x03` | u8                        | unknown_description_03    |       |
| `unknown_after_movie_path+0x04` | u8                        | can_quick_slot            |       |
| `unknown_after_movie_path+0x05` | u64                       | unknown_list_count        |       |
| `unknown_after_movie_path+0x0D` | u32[unknown_list_count]   | unknown_list              |       |
| `unknown_list+0x00`             | u8                        | awakening_type            |       |
| `unknown_list+0x01`             | u8                        | unknown_list_01           |       |
| `unknown_list+0x02`             | u8                        | unknown_list_02           |       |
| `unknown_list+0x03`             | u8                        | is_developing_contents    |       |
| `unknown_list+0x04`             | u32                       | contents_group_count      |       |
| `unknown_list+0x08`             | u32[contents_group_count] | contents_group_hashes     |       |
| `contents_group_hashes+0x00`    | u32                       | exclusive_count           |       |
| `contents_group_hashes+0x04`    | u16[exclusive_count]      | exclusive_skill_nos       |       |
| `exclusive_skill_nos+0x00`      | u8                        | condition                 |       |
| `exclusive_skill_nos+0x01`      | str16                     | unknown_code              |       |
| `unknown_code+0x00`             | u8                        | branch                    |       |
| `unknown_code+0x01`             | u32                       | unknown_code_01           |       |
| `unknown_code+0x05`             | u32                       | unknown_code_05           |       |
| `unknown_code+0x09`             | u8                        | unknown_code_09           |       |

## Layout 2

The Payload ended after `unknown_code_05`: `unknown_code_09` did not exist
yet. Only the Payload differs from Layout 3.

### Payload (variable: 148 bytes + text and lists, size from `skilltypeoffset.dbss`)

| Offset                          | Type                      | Field                     | Notes |
| ------------------------------- | ------------------------- | ------------------------- | ----- |
| `+0x00`                         | u32                       | skill_key                 |       |
| `+0x04`                         | str16                     | name                      |       |
| `name+0x00`                     | str16                     | group_name                |       |
| `group_name+0x00`               | u32                       | kind                      |       |
| `group_name+0x04`               | u16                       | unknown_group_name_04     |       |
| `group_name+0x06`               | u32                       | next_rank_count           |       |
| `group_name+0x0A`               | u32[next_rank_count]      | next_rank_keys            |       |
| `next_rank_keys+0x00`           | u64                       | class_mask                |       |
| `next_rank_keys+0x08`           | u64                       | unknown_next_rank_keys_08 |       |
| `next_rank_keys+0x10`           | u8                        | require_equip_type        |       |
| `next_rank_keys+0x11`           | u8                        | uses_main_weapon          |       |
| `next_rank_keys+0x12`           | u8                        | uses_sub_weapon           |       |
| `next_rank_keys+0x13`           | bytes[4]                  | unknown_next_rank_keys_13 |       |
| `next_rank_keys+0x17`           | u8                        | require_equip_slot        |       |
| `next_rank_keys+0x18`           | u8                        | unknown_next_rank_keys_18 |       |
| `next_rank_keys+0x19`           | u16                       | max_level                 |       |
| `next_rank_keys+0x1B`           | u32                       | skill_owner_type          |       |
| `next_rank_keys+0x1F`           | u32                       | first_rank_key            |       |
| `next_rank_keys+0x23`           | str8                      | icon_path                 |       |
| `icon_path+0x00`                | str16                     | unknown_after_icon_path   |       |
| `unknown_after_icon_path+0x00`  | str16                     | description               |       |
| `description+0x00`              | str8                      | movie_path                |       |
| `movie_path+0x00`               | str8                      | unknown_after_movie_path  |       |
| `unknown_after_movie_path+0x00` | u8                        | unknown_description_00    |       |
| `unknown_after_movie_path+0x01` | u16                       | unknown_description_01    |       |
| `unknown_after_movie_path+0x03` | u8                        | unknown_description_03    |       |
| `unknown_after_movie_path+0x04` | u8                        | can_quick_slot            |       |
| `unknown_after_movie_path+0x05` | u64                       | unknown_list_count        |       |
| `unknown_after_movie_path+0x0D` | u32[unknown_list_count]   | unknown_list              |       |
| `unknown_list+0x00`             | u8                        | awakening_type            |       |
| `unknown_list+0x01`             | u8                        | unknown_list_01           |       |
| `unknown_list+0x02`             | u8                        | unknown_list_02           |       |
| `unknown_list+0x03`             | u8                        | is_developing_contents    |       |
| `unknown_list+0x04`             | u32                       | contents_group_count      |       |
| `unknown_list+0x08`             | u32[contents_group_count] | contents_group_hashes     |       |
| `contents_group_hashes+0x00`    | u32                       | exclusive_count           |       |
| `contents_group_hashes+0x04`    | u16[exclusive_count]      | exclusive_skill_nos       |       |
| `exclusive_skill_nos+0x00`      | u8                        | condition                 |       |
| `exclusive_skill_nos+0x01`      | str16                     | unknown_code              |       |
| `unknown_code+0x00`             | u8                        | branch                    |       |
| `unknown_code+0x01`             | u32                       | unknown_code_01           |       |
| `unknown_code+0x05`             | u32                       | unknown_code_05           |       |

## Layout 1

`unknown_list_02` did not exist yet, so `is_developing_contents` and every
field after it sat 1 byte earlier than in Layout 2. On client 1348 the third
byte after `awakening_type` matches the fourth of client 1485 on 19,181 of
the 19,228 shared keys. Only the Payload differs from Layout 2.

### Payload (variable: 147 bytes + text and lists, size from `skilltypeoffset.dbss`)

| Offset                          | Type                      | Field                     | Notes |
| ------------------------------- | ------------------------- | ------------------------- | ----- |
| `+0x00`                         | u32                       | skill_key                 |       |
| `+0x04`                         | str16                     | name                      |       |
| `name+0x00`                     | str16                     | group_name                |       |
| `group_name+0x00`               | u32                       | kind                      |       |
| `group_name+0x04`               | u16                       | unknown_group_name_04     |       |
| `group_name+0x06`               | u32                       | next_rank_count           |       |
| `group_name+0x0A`               | u32[next_rank_count]      | next_rank_keys            |       |
| `next_rank_keys+0x00`           | u64                       | class_mask                |       |
| `next_rank_keys+0x08`           | u64                       | unknown_next_rank_keys_08 |       |
| `next_rank_keys+0x10`           | u8                        | require_equip_type        |       |
| `next_rank_keys+0x11`           | u8                        | uses_main_weapon          |       |
| `next_rank_keys+0x12`           | u8                        | uses_sub_weapon           |       |
| `next_rank_keys+0x13`           | bytes[4]                  | unknown_next_rank_keys_13 |       |
| `next_rank_keys+0x17`           | u8                        | require_equip_slot        |       |
| `next_rank_keys+0x18`           | u8                        | unknown_next_rank_keys_18 |       |
| `next_rank_keys+0x19`           | u16                       | max_level                 |       |
| `next_rank_keys+0x1B`           | u32                       | skill_owner_type          |       |
| `next_rank_keys+0x1F`           | u32                       | first_rank_key            |       |
| `next_rank_keys+0x23`           | str8                      | icon_path                 |       |
| `icon_path+0x00`                | str16                     | unknown_after_icon_path   |       |
| `unknown_after_icon_path+0x00`  | str16                     | description               |       |
| `description+0x00`              | str8                      | movie_path                |       |
| `movie_path+0x00`               | str8                      | unknown_after_movie_path  |       |
| `unknown_after_movie_path+0x00` | u8                        | unknown_description_00    |       |
| `unknown_after_movie_path+0x01` | u16                       | unknown_description_01    |       |
| `unknown_after_movie_path+0x03` | u8                        | unknown_description_03    |       |
| `unknown_after_movie_path+0x04` | u8                        | can_quick_slot            |       |
| `unknown_after_movie_path+0x05` | u64                       | unknown_list_count        |       |
| `unknown_after_movie_path+0x0D` | u32[unknown_list_count]   | unknown_list              |       |
| `unknown_list+0x00`             | u8                        | awakening_type            |       |
| `unknown_list+0x01`             | u8                        | unknown_list_01           |       |
| `unknown_list+0x02`             | u8                        | is_developing_contents    |       |
| `unknown_list+0x03`             | u32                       | contents_group_count      |       |
| `unknown_list+0x07`             | u32[contents_group_count] | contents_group_hashes     |       |
| `contents_group_hashes+0x00`    | u32                       | exclusive_count           |       |
| `contents_group_hashes+0x04`    | u16[exclusive_count]      | exclusive_skill_nos       |       |
| `exclusive_skill_nos+0x00`      | u8                        | condition                 |       |
| `exclusive_skill_nos+0x01`      | str16                     | unknown_code              |       |
| `unknown_code+0x00`             | u8                        | branch                    |       |
| `unknown_code+0x01`             | u32                       | unknown_code_01           |       |
| `unknown_code+0x05`             | u32                       | unknown_code_05           |       |

## `group_name`

Equal to `name` on 16,847 records. On the other 13,505 it is the name without
the rank or a qualifier: `거대한 진노 III` -> `거대한 진노`, `탈것 속도 증가 1.0%`
-> `속도 +1.0%`. Some are cut mid-phrase (`극 : 매화의 정신` -> `극 : 매화의`), so it
reads like a short label rather than a clean family name.

## `kind`

| Value | Meaning | Records | Example                                                      |
| ----- | ------- | ------- | ------------------------------------------------------------ |
| 0     | Other   | 14,382  | Item and event skills, "[Event] Energy of Happiness" (57005) |
| 1     | Active  | 10,219  | "Seismic Strike", "Fist Fury I"                              |
| 2     | Passive | 5,751   | "Mountain Aura IX" to "XVI"                                  |

## `class_mask`

Bit `n` is the class type `n` that LOC type `21` names; see
[`skillsimply.dbss` `class_mask`](skillsimply_dbss.md#class_mask). On client
1784 the 320 records with bit 31 set also have bits 32 to 63 set (for
example `0xFFFFFFFF80000040`), as a sign-extended i32 would; that client's
sheet has the 32 class columns `0` to `31` only, so bits 32 to 63 name no
class there.

## `icon_path`

The skill icon, a path relative to `ui_texture/icon/` such as
`New_Icon/04_PC_Skill/01_PC_Skill/09_PEM_Skill/PEM_Skill_3328.dds`. On client
3483 9,494 records hold a `.dds` path and 7,355 a `.png` path such as
`Real_ETC/Scroll/Icon_ETC_Scroll_00000000.png`; the rest are empty. The
parser keeps only the `.dds` paths as the skill icon.

Lower-cased under `ui_texture/icon/`, 3,452 of the 3,530 distinct `.dds`
paths exist in the client's PAZ files on client 3458; the other 78 point at
missing files (for example
`new_icon/04_pc_skill/01_pc_skill/31_prsa_skill/prsa_skill_8827.dds`).

## `awakening_type`

The value the client Lua reads with `getSkillAwakeningType()`; the client's
`CppEnums.SkillAwakeningType` names `0` `eSkillAwakeningType_Normal` and `1`
`eSkillAwakeningType_AwakeningWeapon`. Read from a running client 1784
through that call on 2026-11-13, Greatbow of Light (3458), Greatbow Training I (3905) and
Black Spirit: Luthraghon's Call I (3949) return `1` and Spirit Arrow I
(3328), Evasion (3347), Emergency Escape (92), Earth Kick I (3343), Winged
Strike I (3423) and Agile Strike I (3401) return `0`, as their records hold.

It is close to `branch` `1` without equalling it. On client 3483:

| `awakening_type` | `branch` | Records | Example                 |
| ---------------- | -------- | ------- | ----------------------- |
| `1`              | `1`      | 1,860   | Awakening weapon skills |
| `0`              | `1`      | 126     | `왕실 검술 : 본 IV`, `궤도 이탈` |
| `0`              | `2`      | 1,121   | Succession skills       |
| `0`              | `0`      | 27,368  | Everything else         |

1,824 of the 1,860 records with `1` have `require_equip_type` `57`, the
Awakening weapon.

## Notes

- The first keys (`0xDEAD0001`, `0xDEAC0001`) look like sentinels but are
  real skills; see [`skill.dbss` Skill Keys](skill_dbss.md#skill-keys).
- The record layout of the first four fields and the `kind` meaning come from
  bdo-data-extractor; the counts and the `group_name` reading were checked
  against client 3458.
- LOC type `10` covers 28,343 of its 29,398 IDs with a skill number from this
  table or `skill.dbss`; 2,009 skill numbers have no type `10` row and 1,055
  type `10` IDs have no skill.
- Nothing in the file names its layout. The parser reads it with the first
  layout, in client order, under which every record ends at its size.

## Field Names

The client 1784 server dump (`Instance_dumpFull.exe`) reads this file
with `SkillTypeStaticStatusManager::ReadRecord_skillType` (VA
`0x140c89610`), field by field in Layout 4's order, and fills the same
static status from the `SkillType_Table_New` sheet in the loader at VA
`0x14085bbe0`. The member is the static status offset the reader writes.
The names below rest on that server alone where the field keeps an
`unknown_*` name.

| Field                                               | Column                                                                        | Member                                                         |
| --------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `name`                                              | `SkillName`                                                                   |                                                                |
| `group_name`                                        | `SkillShortName`                                                              |                                                                |
| `kind`                                              | `SkillType`                                                                   |                                                                |
| `unknown_group_name_04`                             | `UpgradeSkillType`                                                            |                                                                |
| `next_rank_keys`                                    |                                                                               | `+0x50`                                                        |
| `class_mask`                                        | `0` to `31`                                                                   | `+0x78`                                                        |
| `unknown_next_rank_keys_08`                         |                                                                               | `+0x80`                                                        |
| `require_equip_type` to `unknown_next_rank_keys_18` | `RequireEquipType`                                                            |                                                                |
| `max_level`                                         |                                                                               | `+0x9A`                                                        |
| `skill_owner_type`                                  | `SkillOwnerType`                                                              |                                                                |
| `first_rank_key`                                    |                                                                               | `+0xA0`                                                        |
| `icon_path`                                         | `IconImageFile`                                                               |                                                                |
| `unknown_after_icon_path`                           | `Control`                                                                     |                                                                |
| `description`                                       | `Desc`                                                                        |                                                                |
| `movie_path`                                        | `MoviePath`                                                                   |                                                                |
| `unknown_after_movie_path`                          | `Combo_MoviePath`                                                             |                                                                |
| `unknown_description_00`                            | `PieceCountOfPartialSkill`                                                    |                                                                |
| `unknown_description_01`                            |                                                                               | `+0x192`; the loader sets bit `0x40` from `IsTestimonialSkill` |
| `unknown_description_03`                            |                                                                               | `+0x194`                                                       |
| `can_quick_slot`                                    |                                                                               | `+0x195`                                                       |
| `unknown_list`                                      |                                                                               | `+0x198`                                                       |
| `awakening_type`                                    | `skillAwakeningType`                                                          |                                                                |
| `unknown_list_01`                                   | `SkillCommandCheck`                                                           |                                                                |
| `unknown_list_02`                                   | `SkillAlert`                                                                  |                                                                |
| `is_developing_contents`                            |                                                                               | `+0x1CA`                                                       |
| `contents_group_hashes`                             |                                                                               | `+0x1B0`                                                       |
| `exclusive_skill_nos`                               |                                                                               | `+0x60`                                                        |
| `condition`                                         | `Condition`                                                                   |                                                                |
| `unknown_code`                                      | `PatternControl`                                                              |                                                                |
| `branch`                                            | `BranchType`                                                                  | `+0x189`                                                       |
| `unknown_code_01`                                   |                                                                               | `+0x1E0`                                                       |
| `unknown_code_05`                                   | `SkillUITreeGroup << 16 \| SkillUITreeGroupLevel`, `0` when either is below 1 | `+0x18C`                                                       |
| `unknown_code_09`                                   | `SkillCoolTimeUICheck`, `2` when the cell is empty                            |                                                                |
| `unknown_code_0a`                                   |                                                                               | `+0x128`                                                       |

The loader writes `BranchType` to byte 1 and the tree group pair to bytes 4
to 7 of one block; with the block at `+0x188` they land on `+0x189` and
`+0x18C`, the two members the reader fills there.

## Open Questions

### What does `unknown_list` hold?

A u64-counted list of up to three u32 values, each `0`, `1` or `2`, on 4,718
records of client 3483. The server reader passes it to a helper that also
reads lists in `itemimprovementsource.dbss` and `racecourse.dbss`. No sheet
column of `SkillType_Table_New` is read as a list of numbers except
`ForbidSkillType`, which the loader reads as a list of i64.
