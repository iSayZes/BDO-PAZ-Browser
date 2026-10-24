# `tooltiptable.dbss` Format

## Purpose

The tooltip text lines that skill and item tooltips are built from. Each
row is one line: the hash of its string key (`DAM_ATT`), the Korean text
with `{p0}` to `{p9}` placeholders for the values the tooltip fills in, the
number of placeholders, the tooltip type and, on skill lines, the effect
icons the skill window shows next to the line (Invincible, Super Armor,
Knockdown and so on). The rows sit in one section per tooltip type, and
the texts in the PABR string table at the end of the file.
`tooltiptableoffset.dbss` indexes every row by type and key hash. LOC type
46 holds the translated line under `(key_hash, 0, tooltip_type, 0)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes   | Records                          | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ------- | -------------------------------- | --------- |
| 2      | 1324 and later | 3483    | `tooltiptable.dbss`       | 885,245 | 4,615 Row, 3 Section             | 21        |
| 2      | 1324 and later | 3483    | `tooltiptableoffset.dbss` | 55,408  | 4,615 Index Row, 3 Index Section | 12        |
| 1      | 1230 to 1321   | 1321    | `tooltiptable.dbss`       | 405,047 | 2,554 Row, 3 Section             | 17        |
| 1      | 1230 to 1321   | 1321    | `tooltiptableoffset.dbss` | 30,676  | 2,554 Index Row, 3 Index Section | 12        |

| Layout | File                      | Known             | Unknown          |
| ------ | ------------------------- | ----------------- | ---------------- |
| 2      | `tooltiptable.dbss`       | 880,630 B (99.5%) | 4,615 B (0.5%)   |
| 2      | `tooltiptableoffset.dbss` | 36,948 B (66.7%)  | 18,460 B (33.3%) |
| 1      | `tooltiptable.dbss`       | 402,493 B (99.4%) | 2,554 B (0.6%)   |
| 1      | `tooltiptableoffset.dbss` | 20,460 B (66.7%)  | 10,216 B (33.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `fff525ab805c`  |
| 3482   | Layout 2 | `fff525ab805c`  |
| 3474   | Layout 2 | `fff525ab805c`  |
| 3473   | Layout 2 | `fff525ab805c`  |
| 3464   | Layout 2 | `fff525ab805c`  |
| 3458   | Layout 2 | `fff525ab805c`  |
| 3454   | Layout 2 | `fff525ab805c`  |
| 3444   | Layout 2 | `fff525ab805c`  |
| 3435   | Layout 2 | `fff525ab805c`  |
| 3426   | Layout 2 | `fff525ab805c`  |
| 3418   | Layout 2 | `fff525ab805c`  |
| 3412   | Layout 2 | `fff525ab805c`  |
| 3402   | Layout 2 | `fff525ab805c`  |
| 3396   | Layout 2 | `fff525ab805c`  |
| 3387   | Layout 2 | `fff525ab805c`  |
| 3381   | Layout 2 | `fff525ab805c`  |
| 3373   | Layout 2 | `fff525ab805c`  |
| 3364   | Layout 2 | `fff525ab805c`  |
| 3356   | Layout 2 | `fff525ab805c`  |
| 3349   | Layout 2 | `fff525ab805c`  |
| 3342   | Layout 2 | `fff525ab805c`  |
| 3335   | Layout 2 | `fff525ab805c`  |
| 3326   | Layout 2 | `fff525ab805c`  |
| 3321   | Layout 2 | `fff525ab805c`  |
| 3314   | Layout 2 | `fff525ab805c`  |
| 3303   | Layout 2 | `fff525ab805c`  |
| 3302   | Layout 2 | `fff525ab805c`  |
| 3293   | Layout 2 | `fff525ab805c`  |
| 3283   | Layout 2 | `fff525ab805c`  |
| 3275   | Layout 2 | `fff525ab805c`  |
| 3267   | Layout 2 | `fff525ab805c`  |
| 3258   | Layout 2 | `fff525ab805c`  |
| 3251   | Layout 2 | `fff525ab805c`  |
| 3242   | Layout 2 | `fff525ab805c`  |
| 3235   | Layout 2 | `fff525ab805c`  |
| 3229   | Layout 2 | `fff525ab805c`  |
| 3212   | Layout 2 | `fff525ab805c`  |
| 3203   | Layout 2 | `fff525ab805c`  |
| 3193   | Layout 2 | `fff525ab805c`  |
| 3186   | Layout 2 | `fff525ab805c`  |
| 3177   | Layout 2 | `fff525ab805c`  |
| 3169   | Layout 2 | `fff525ab805c`  |
| 3158   | Layout 2 | `fff525ab805c`  |
| 3151   | Layout 2 | `fff525ab805c`  |
| 3144   | Layout 2 | `fff525ab805c`  |
| 3133   | Layout 2 | `fff525ab805c`  |
| 3125   | Layout 2 | `fff525ab805c`  |
| 3118   | Layout 2 | `fff525ab805c`  |
| 3111   | Layout 2 | `fff525ab805c`  |
| 3103   | Layout 2 | `fff525ab805c`  |
| 3095   | Layout 2 | `fff525ab805c`  |
| 3086   | Layout 2 | `fff525ab805c`  |
| 3072   | Layout 2 | `fff525ab805c`  |
| 3062   | Layout 2 | `fff525ab805c`  |
| 3052   | Layout 2 | `fff525ab805c`  |
| 3045   | Layout 2 | `fff525ab805c`  |
| 3037   | Layout 2 | `fff525ab805c`  |
| 3030   | Layout 2 | `fff525ab805c`  |
| 3021   | Layout 2 | `fff525ab805c`  |
| 3012   | Layout 2 | `fff525ab805c`  |
| 3002   | Layout 2 | `fff525ab805c`  |
| 2995   | Layout 2 | `fff525ab805c`  |
| 2987   | Layout 2 | `fff525ab805c`  |
| 2978   | Layout 2 | `fff525ab805c`  |
| 2970   | Layout 2 | `fff525ab805c`  |
| 2959   | Layout 2 | `fff525ab805c`  |
| 2951   | Layout 2 | `fff525ab805c`  |
| 2942   | Layout 2 | `fff525ab805c`  |
| 2935   | Layout 2 | `fff525ab805c`  |
| 2932   | Layout 2 | `fff525ab805c`  |
| 2923   | Layout 2 | `fff525ab805c`  |
| 2919   | Layout 2 | `fff525ab805c`  |
| 2907   | Layout 2 | `fff525ab805c`  |
| 2900   | Layout 2 | `fff525ab805c`  |
| 2891   | Layout 2 | `fff525ab805c`  |
| 2882   | Layout 2 | `fff525ab805c`  |
| 2872   | Layout 2 | `fff525ab805c`  |
| 2863   | Layout 2 | `fff525ab805c`  |
| 2855   | Layout 2 | `fff525ab805c`  |
| 2849   | Layout 2 | `fff525ab805c`  |
| 2844   | Layout 2 | `fff525ab805c`  |
| 2834   | Layout 2 | `fff525ab805c`  |
| 2825   | Layout 2 | `fff525ab805c`  |
| 2819   | Layout 2 | `fff525ab805c`  |
| 2811   | Layout 2 | `fff525ab805c`  |
| 2803   | Layout 2 | `fff525ab805c`  |
| 2794   | Layout 2 | `fff525ab805c`  |
| 2783   | Layout 2 | `fff525ab805c`  |
| 2774   | Layout 2 | `fff525ab805c`  |
| 2765   | Layout 2 | `fff525ab805c`  |
| 2756   | Layout 2 | `fff525ab805c`  |
| 2750   | Layout 2 | `fff525ab805c`  |
| 2743   | Layout 2 | `fff525ab805c`  |
| 2736   | Layout 2 | `fff525ab805c`  |
| 2726   | Layout 2 | `fff525ab805c`  |
| 2717   | Layout 2 | `fff525ab805c`  |
| 2709   | Layout 2 | `fff525ab805c`  |
| 2703   | Layout 2 | `fff525ab805c`  |
| 2695   | Layout 2 | `fff525ab805c`  |
| 2684   | Layout 2 | `fff525ab805c`  |
| 2672   | Layout 2 | `fff525ab805c`  |
| 2665   | Layout 2 | `fff525ab805c`  |
| 2657   | Layout 2 | `fff525ab805c`  |
| 2649   | Layout 2 | `fff525ab805c`  |
| 2644   | Layout 2 | `fff525ab805c`  |
| 2637   | Layout 2 | `fff525ab805c`  |
| 2629   | Layout 2 | `fff525ab805c`  |
| 2619   | Layout 2 | `fff525ab805c`  |
| 2612   | Layout 2 | `fff525ab805c`  |
| 2606   | Layout 2 | `fff525ab805c`  |
| 2602   | Layout 2 | `fff525ab805c`  |
| 2601   | Layout 2 | `fff525ab805c`  |
| 2592   | Layout 2 | `fff525ab805c`  |
| 2583   | Layout 2 | `fff525ab805c`  |
| 2575   | Layout 2 | `fff525ab805c`  |
| 2567   | Layout 2 | `fff525ab805c`  |
| 2560   | Layout 2 | `fff525ab805c`  |
| 2553   | Layout 2 | `fff525ab805c`  |
| 2545   | Layout 2 | `fff525ab805c`  |
| 2538   | Layout 2 | `fff525ab805c`  |
| 2529   | Layout 2 | `fff525ab805c`  |
| 2519   | Layout 2 | `fff525ab805c`  |
| 2513   | Layout 2 | `fff525ab805c`  |
| 2510   | Layout 2 | `fff525ab805c`  |
| 2507   | Layout 2 | `fff525ab805c`  |
| 2503   | Layout 2 | `fff525ab805c`  |
| 2498   | Layout 2 | `fff525ab805c`  |
| 2492   | Layout 2 | `fff525ab805c`  |
| 2487   | Layout 2 | `fff525ab805c`  |
| 2480   | Layout 2 | `fff525ab805c`  |
| 2474   | Layout 2 | `fff525ab805c`  |
| 2468   | Layout 2 | `fff525ab805c`  |
| 2460   | Layout 2 | `fff525ab805c`  |
| 2453   | Layout 2 | `fff525ab805c`  |
| 2444   | Layout 2 | `fff525ab805c`  |
| 2438   | Layout 2 | `fff525ab805c`  |
| 2434   | Layout 2 | `fff525ab805c`  |
| 2429   | Layout 2 | `fff525ab805c`  |
| 2421   | Layout 2 | `fff525ab805c`  |
| 2414   | Layout 2 | `fff525ab805c`  |
| 2407   | Layout 2 | `fff525ab805c`  |
| 2401   | Layout 2 | `fff525ab805c`  |
| 2397   | Layout 2 | `fff525ab805c`  |
| 2393   | Layout 2 | `fff525ab805c`  |
| 2384   | Layout 2 | `fff525ab805c`  |
| 2378   | Layout 2 | `fff525ab805c`  |
| 2372   | Layout 2 | `fff525ab805c`  |
| 2358   | Layout 2 | `fff525ab805c`  |
| 2352   | Layout 2 | `fff525ab805c`  |
| 2347   | Layout 2 | `fff525ab805c`  |
| 2343   | Layout 2 | `fff525ab805c`  |
| 2335   | Layout 2 | `fff525ab805c`  |
| 2327   | Layout 2 | `fff525ab805c`  |
| 2324   | Layout 2 | `fff525ab805c`  |
| 2319   | Layout 2 | `fff525ab805c`  |
| 2313   | Layout 2 | `fff525ab805c`  |
| 2308   | Layout 2 | `fff525ab805c`  |
| 2302   | Layout 2 | `fff525ab805c`  |
| 2295   | Layout 2 | `fff525ab805c`  |
| 2290   | Layout 2 | `fff525ab805c`  |
| 2284   | Layout 2 | `fff525ab805c`  |
| 2276   | Layout 2 | `fff525ab805c`  |
| 2269   | Layout 2 | `fff525ab805c`  |
| 2259   | Layout 2 | `fff525ab805c`  |
| 2250   | Layout 2 | `fff525ab805c`  |
| 2243   | Layout 2 | `fff525ab805c`  |
| 2235   | Layout 2 | `fff525ab805c`  |
| 2229   | Layout 2 | `fff525ab805c`  |
| 2224   | Layout 2 | `fff525ab805c`  |
| 2218   | Layout 2 | `fff525ab805c`  |
| 2215   | Layout 2 | `fff525ab805c`  |
| 2207   | Layout 2 | `fff525ab805c`  |
| 2203   | Layout 2 | `fff525ab805c`  |
| 2196   | Layout 2 | `fff525ab805c`  |
| 2192   | Layout 2 | `fff525ab805c`  |
| 2189   | Layout 2 | `fff525ab805c`  |
| 2183   | Layout 2 | `fff525ab805c`  |
| 2179   | Layout 2 | `fff525ab805c`  |
| 2171   | Layout 2 | `fff525ab805c`  |
| 2163   | Layout 2 | `fff525ab805c`  |
| 2156   | Layout 2 | `fff525ab805c`  |
| 2151   | Layout 2 | `fff525ab805c`  |
| 2147   | Layout 2 | `fff525ab805c`  |
| 2142   | Layout 2 | `fff525ab805c`  |
| 2138   | Layout 2 | `fff525ab805c`  |
| 2134   | Layout 2 | `fff525ab805c`  |
| 2130   | Layout 2 | `fff525ab805c`  |
| 2122   | Layout 2 | `fff525ab805c`  |
| 2107   | Layout 2 | `fff525ab805c`  |
| 2098   | Layout 2 | `fff525ab805c`  |
| 2089   | Layout 2 | `fff525ab805c`  |
| 2081   | Layout 2 | `fff525ab805c`  |
| 2073   | Layout 2 | `fff525ab805c`  |
| 2067   | Layout 2 | `fff525ab805c`  |
| 2063   | Layout 2 | `fff525ab805c`  |
| 2059   | Layout 2 | `fff525ab805c`  |
| 2052   | Layout 2 | `fff525ab805c`  |
| 2044   | Layout 2 | `fff525ab805c`  |
| 2039   | Layout 2 | `fff525ab805c`  |
| 2032   | Layout 2 | `fff525ab805c`  |
| 2025   | Layout 2 | `fff525ab805c`  |
| 2011   | Layout 2 | `fff525ab805c`  |
| 2005   | Layout 2 | `fff525ab805c`  |
| 2000   | Layout 2 | `fff525ab805c`  |
| 1996   | Layout 2 | `fff525ab805c`  |
| 1991   | Layout 2 | `fff525ab805c`  |
| 1985   | Layout 2 | `fff525ab805c`  |
| 1980   | Layout 2 | `fff525ab805c`  |
| 1969   | Layout 2 | `fff525ab805c`  |
| 1964   | Layout 2 | `fff525ab805c`  |
| 1958   | Layout 2 | `fff525ab805c`  |
| 1950   | Layout 2 | `fff525ab805c`  |
| 1945   | Layout 2 | `fff525ab805c`  |
| 1937   | Layout 2 | `fff525ab805c`  |
| 1933   | Layout 2 | `fff525ab805c`  |
| 1927   | Layout 2 | `fff525ab805c`  |
| 1921   | Layout 2 | `fff525ab805c`  |
| 1914   | Layout 2 | `fff525ab805c`  |
| 1908   | Layout 2 | `fff525ab805c`  |
| 1897   | Layout 2 | `fff525ab805c`  |
| 1892   | Layout 2 | `fff525ab805c`  |
| 1886   | Layout 2 | `fff525ab805c`  |
| 1881   | Layout 2 | `fff525ab805c`  |
| 1871   | Layout 2 | `fff525ab805c`  |
| 1866   | Layout 2 | `fff525ab805c`  |
| 1862   | Layout 2 | `fff525ab805c`  |
| 1854   | Layout 2 | `fff525ab805c`  |
| 1846   | Layout 2 | `fff525ab805c`  |
| 1838   | Layout 2 | `fff525ab805c`  |
| 1832   | Layout 2 | `fff525ab805c`  |
| 1826   | Layout 2 | `fff525ab805c`  |
| 1822   | Layout 2 | `fff525ab805c`  |
| 1818   | Layout 2 | `fff525ab805c`  |
| 1804   | Layout 2 | `fff525ab805c`  |
| 1794   | Layout 2 | `fff525ab805c`  |
| 1790   | Layout 2 | `fff525ab805c`  |
| 1784   | Layout 2 | `fff525ab805c`  |
| 1774   | Layout 2 | `fff525ab805c`  |
| 1771   | Layout 2 | `fff525ab805c`  |
| 1762   | Layout 2 | `fff525ab805c`  |
| 1759   | Layout 2 | `fff525ab805c`  |
| 1754   | Layout 2 | `fff525ab805c`  |
| 1749   | Layout 2 | `fff525ab805c`  |
| 1743   | Layout 2 | `fff525ab805c`  |
| 1737   | Layout 2 | `fff525ab805c`  |
| 1731   | Layout 2 | `fff525ab805c`  |
| 1725   | Layout 2 | `fff525ab805c`  |
| 1717   | Layout 2 | `fff525ab805c`  |
| 1710   | Layout 2 | `fff525ab805c`  |
| 1704   | Layout 2 | `fff525ab805c`  |
| 1698   | Layout 2 | `fff525ab805c`  |
| 1690   | Layout 2 | `fff525ab805c`  |
| 1685   | Layout 2 | `fff525ab805c`  |
| 1680   | Layout 2 | `fff525ab805c`  |
| 1674   | Layout 2 | `fff525ab805c`  |
| 1668   | Layout 2 | `fff525ab805c`  |
| 1659   | Layout 2 | `fff525ab805c`  |
| 1649   | Layout 2 | `fff525ab805c`  |
| 1642   | Layout 2 | `fff525ab805c`  |
| 1636   | Layout 2 | `fff525ab805c`  |
| 1628   | Layout 2 | `fff525ab805c`  |
| 1622   | Layout 2 | `fff525ab805c`  |
| 1614   | Layout 2 | `fff525ab805c`  |
| 1608   | Layout 2 | `fff525ab805c`  |
| 1602   | Layout 2 | `fff525ab805c`  |
| 1598   | Layout 2 | `fff525ab805c`  |
| 1594   | Layout 2 | `fff525ab805c`  |
| 1590   | Layout 2 | `fff525ab805c`  |
| 1587   | Layout 2 | `fff525ab805c`  |
| 1584   | Layout 2 | `fff525ab805c`  |
| 1579   | Layout 2 | `fff525ab805c`  |
| 1572   | Layout 2 | `fff525ab805c`  |
| 1565   | Layout 2 | `fff525ab805c`  |
| 1559   | Layout 2 | `fff525ab805c`  |
| 1554   | Layout 2 | `fff525ab805c`  |
| 1547   | Layout 2 | `fff525ab805c`  |
| 1537   | Layout 2 | `fff525ab805c`  |
| 1529   | Layout 2 | `fff525ab805c`  |
| 1524   | Layout 2 | `fff525ab805c`  |
| 1519   | Layout 2 | `fff525ab805c`  |
| 1509   | Layout 2 | `fff525ab805c`  |
| 1506   | Layout 2 | `fff525ab805c`  |
| 1504   | Layout 2 | `fff525ab805c`  |
| 1500   | Layout 2 | `fff525ab805c`  |
| 1493   | Layout 2 | `fff525ab805c`  |
| 1489   | Layout 2 | `fff525ab805c`  |
| 1485   | Layout 2 | `fff525ab805c`  |
| 1481   | Layout 2 | `fff525ab805c`  |
| 1474   | Layout 2 | `fff525ab805c`  |
| 1466   | Layout 2 | `fff525ab805c`  |
| 1462   | Layout 2 | `fff525ab805c`  |
| 1459   | Layout 2 | `fff525ab805c`  |
| 1453   | Layout 2 | `fff525ab805c`  |
| 1450   | Layout 2 | `fff525ab805c`  |
| 1445   | Layout 2 | `fff525ab805c`  |
| 1439   | Layout 2 | `fff525ab805c`  |
| 1433   | Layout 2 | `fff525ab805c`  |
| 1430   | Layout 2 | `fff525ab805c`  |
| 1426   | Layout 2 | `fff525ab805c`  |
| 1421   | Layout 2 | `fff525ab805c`  |
| 1417   | Layout 2 | `fff525ab805c`  |
| 1416   | Layout 2 | `fff525ab805c`  |
| 1409   | Layout 2 | `fff525ab805c`  |
| 1405   | Layout 2 | `fff525ab805c`  |
| 1401   | Layout 2 | `fff525ab805c`  |
| 1396   | Layout 2 | `fff525ab805c`  |
| 1391   | Layout 2 | `fff525ab805c`  |
| 1390   | Layout 2 | `fff525ab805c`  |
| 1386   | Layout 2 | `fff525ab805c`  |
| 1381   | Layout 2 | `fff525ab805c`  |
| 1379   | Layout 2 | `fff525ab805c`  |
| 1372   | Layout 2 | `fff525ab805c`  |
| 1366   | Layout 2 | `fff525ab805c`  |
| 1364   | Layout 2 | `fff525ab805c`  |
| 1363   | Layout 2 | `fff525ab805c`  |
| 1360   | Layout 2 | `fff525ab805c`  |
| 1358   | Layout 2 | `fff525ab805c`  |
| 1355   | Layout 2 | `fff525ab805c`  |
| 1351   | Layout 2 | `fff525ab805c`  |
| 1348   | Layout 2 | `fff525ab805c`  |
| 1346   | Layout 2 | `fff525ab805c`  |
| 1341   | Layout 2 | `fff525ab805c`  |
| 1340   | Layout 2 | `fff525ab805c`  |
| 1338   | Layout 2 | `fff525ab805c`  |
| 1335   | Layout 2 | `fff525ab805c`  |
| 1333   | Layout 2 | `fff525ab805c`  |
| 1329   | Layout 2 | `fff525ab805c`  |
| 1327   | Layout 2 | `fff525ab805c`  |
| 1324   | Layout 2 | `fff525ab805c`  |
| 1321   | Layout 1 | `fff525ab805c`  |
| 1319   | Layout 1 | `fff525ab805c`  |
| 1318   | Layout 1 | `fff525ab805c`  |
| 1316   | Layout 1 | `fff525ab805c`  |
| 1313   | Layout 1 | `fff525ab805c`  |
| 1311   | Layout 1 | `fff525ab805c`  |
| 1309   | Layout 1 | `fff525ab805c`  |
| 1304   | Layout 1 | `fff525ab805c`  |
| 1292   | Layout 1 | `fff525ab805c`  |
| 1286   | Layout 1 | `fff525ab805c`  |
| 1280   | Layout 1 | `fff525ab805c`  |
| 1276   | Layout 1 | `fff525ab805c`  |
| 1267   | Layout 1 | `fff525ab805c`  |
| 1261   | Layout 1 | `fff525ab805c`  |
| 1256   | Layout 1 | `fff525ab805c`  |
| 1250   | Layout 1 | `fff525ab805c`  |
| 1246   | Layout 1 | `fff525ab805c`  |
| 1239   | Layout 1 | `fff525ab805c`  |
| 1230   | Layout 1 | `fff525ab805c`  |
| 1226   | No file  | `fff525ab805c`  |
| 1220   | No file  | `fff525ab805c`  |
| 1217   | No file  | `fff525ab805c`  |
| 1211   | No file  | `fff525ab805c`  |
| 1210   | No file  | `fff525ab805c`  |
| 1208   | No file  | `fff525ab805c`  |
| 1203   | No file  | `fff525ab805c`  |
| 1197   | No file  | `fff525ab805c`  |
| 1194   | No file  | `fff525ab805c`  |
| 1192   | No file  | `fff525ab805c`  |
| 1187   | No file  | `fff525ab805c`  |
| 1183   | No file  | `fff525ab805c`  |
| 1177   | No file  | `fff525ab805c`  |
| 1173   | No file  | `fff525ab805c`  |
| 1167   | No file  | `fff525ab805c`  |
| 1164   | No file  | `fff525ab805c`  |
| 1156   | No file  | `fff525ab805c`  |
| 1149   | No file  | `fff525ab805c`  |
| 1144   | No file  | `fff525ab805c`  |
| 1137   | No file  | `fff525ab805c`  |
| 1132   | No file  | `fff525ab805c`  |
| 1127   | No file  | `fff525ab805c`  |
| 1122   | No file  | `fff525ab805c`  |
| 1118   | No file  | `fff525ab805c`  |
| 1114   | No file  | `fff525ab805c`  |
| 1109   | No file  | `fff525ab805c`  |
| 1102   | No file  | `fff525ab805c`  |
| 1096   | No file  | `fff525ab805c`  |
| 1088   | No file  | `fff525ab805c`  |
| 1081   | No file  | `fff525ab805c`  |
| 1076   | No file  | `fff525ab805c`  |
| 1069   | No file  | `fff525ab805c`  |
| 1064   | No file  | `fff525ab805c`  |
| 1058   | No file  | `fff525ab805c`  |
| 1051   | No file  | `fff525ab805c`  |
| 1044   | No file  | `fff525ab805c`  |
| 1036   | No file  | `fff525ab805c`  |
| 1026   | No file  | `fff525ab805c`  |
| 1016   | No file  | `fff525ab805c`  |
| 1009   | No file  | `fff525ab805c`  |
| 1005   | No file  | `fff525ab805c`  |
| 1000   | No file  | `fff525ab805c`  |
| 998    | No file  | `fff525ab805c`  |
| 990    | No file  | `fff525ab805c`  |
| 979    | No file  | `fff525ab805c`  |
| 972    | No file  | `fff525ab805c`  |
| 963    | No file  | `fff525ab805c`  |
| 955    | No file  | `fff525ab805c`  |
| 946    | No file  | `fff525ab805c`  |
| 938    | No file  | `fff525ab805c`  |
| 927    | No file  | `fff525ab805c`  |
| 911    | No file  | `fff525ab805c`  |
| 904    | No file  | `fff525ab805c`  |
| 899    | No file  | `fff525ab805c`  |
| 894    | No file  | `fff525ab805c`  |
| 885    | No file  | `fff525ab805c`  |
| 879    | No file  | `fff525ab805c`  |
| 872    | No file  | `fff525ab805c`  |
| 864    | No file  | `fff525ab805c`  |
| 855    | No file  | `fff525ab805c`  |
| 853    | No file  | `fff525ab805c`  |
| 845    | No file  | `fff525ab805c`  |
| 837    | No file  | `fff525ab805c`  |
| 829    | No file  | `fff525ab805c`  |
| 822    | No file  | `fff525ab805c`  |
| 814    | No file  | `fff525ab805c`  |
| 805    | No file  | `fff525ab805c`  |
| 794    | No file  | `fff525ab805c`  |
| 787    | No file  | `fff525ab805c`  |
| 780    | No file  | `fff525ab805c`  |
| 771    | No file  | `fff525ab805c`  |
| 760    | No file  | `fff525ab805c`  |
| 748    | No file  | `fff525ab805c`  |
| 741    | No file  | `fff525ab805c`  |
| 736    | No file  | `fff525ab805c`  |
| 731    | No file  | `fff525ab805c`  |
| 723    | No file  | `fff525ab805c`  |
| 711    | No file  | `fff525ab805c`  |
| 707    | No file  | `fff525ab805c`  |
| 697    | No file  | `fff525ab805c`  |
| 689    | No file  | `fff525ab805c`  |
| 683    | No file  | `fff525ab805c`  |
| 678    | No file  | `fff525ab805c`  |
| 670    | No file  | `fff525ab805c`  |
| 661    | No file  | `fff525ab805c`  |
| 656    | No file  | `fff525ab805c`  |
| 652    | No file  | `fff525ab805c`  |
| 643    | No file  | `fff525ab805c`  |
| 637    | No file  | `fff525ab805c`  |
| 630    | No file  | `fff525ab805c`  |
| 627    | No file  | `fff525ab805c`  |
| 621    | No file  | `fff525ab805c`  |
| 617    | No file  | `fff525ab805c`  |
| 615    | No file  | `fff525ab805c`  |
| 606    | No file  | `fff525ab805c`  |
| 599    | No file  | `fff525ab805c`  |
| 592    | No file  | `fff525ab805c`  |
| 586    | No file  | `fff525ab805c`  |
| 577    | No file  | `fff525ab805c`  |
| 569    | No file  | `fff525ab805c`  |
| 561    | No file  | `fff525ab805c`  |
| 554    | No file  | `fff525ab805c`  |
| 542    | No file  | `fff525ab805c`  |
| 532    | No file  | `fff525ab805c`  |
| 531    | No file  | `fff525ab805c`  |
| 526    | No file  | `fff525ab805c`  |
| 521    | No file  | `fff525ab805c`  |
| 517    | No file  | `fff525ab805c`  |
| 510    | No file  | `fff525ab805c`  |
| 508    | No file  | `fff525ab805c`  |
| 504    | No file  | `fff525ab805c`  |
| 497    | No file  | `fff525ab805c`  |
| 491    | No file  | `fff525ab805c`  |
| 485    | No file  | `fff525ab805c`  |
| 478    | No file  | `fff525ab805c`  |
| 472    | No file  | `fff525ab805c`  |
| 466    | No file  | `fff525ab805c`  |
| 457    | No file  | `fff525ab805c`  |
| 452    | No file  | `fff525ab805c`  |
| 449    | No file  | `fff525ab805c`  |
| 435    | No file  | `fff525ab805c`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                         |
| ---------------------------- | -------- | ---------------------------------------------------------------------------- |
| `tooltiptableoffset.dbss`    | Optional | `(tooltip_type, key_hash) -> offset` of every row; the parser walks the main file without it |
| `languagedata_en.loc`        | Optional | The line in the user's language: LOC type 46, `(key_hash, 0, tooltip_type, 0)` |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset             | Type                    | Field        | Notes                                                       |
| ------------------ | ----------------------- | ------------ | ----------------------------------------------------------- |
| `+0x00`            | char[4]                 | magic        | ASCII `PABR`                                                |
| `+0x04`            | Section[..table_start]  | sections     | No count: section `n` holds the rows of `tooltip_type` `n`; 3 sections on clients 1784 and 3483 |
| `sections+0x00`    | String Table            | string_table | See String Table                                            |
| `EOF-0x08`         | u32                     | table_start  | Offset of the string table, where `sections` ends           |
| `EOF-0x04`         | u32                     | zero         | Always `0`                                                  |

### Section (variable: 4 bytes + rows)

| Offset  | Type           | Field     | Notes                                                    |
| ------- | -------------- | --------- | -------------------------------------------------------- |
| `+0x00` | u32            | row_count | Rows of this tooltip type; 3,252, 564 and 799 on client 3483 |
| `+0x04` | Row[row_count] | rows      | See Row; the rows follow each other with no gap          |

### Row (21 bytes)

| Offset  | Type | Field        | Notes                                                                   |
| ------- | ---- | ------------ | ----------------------------------------------------------------------- |
| `+0x00` | u32  | key_hash     | `key_hash()` of the string key (`_common/string_hash.py`), `DAM_ATT` is `3080225168`; unique within a section, 35 keys sit in two sections (clients 1784 and 3483) |
| `+0x04` | u32  | format_ref   | Index of the Korean text in `string_table.strings`; rows that share a text share an index, and every string is used (clients 1784 and 3483) |
| `+0x08` | u32  | param_count  | Equals the highest `{pN}` placeholder of the text plus one, `0` without placeholders, on every row of clients 1784 and 3483 |
| `+0x0C` | u32  | tooltip_type | The section's number; see Tooltip Types                                 |
| `+0x10` | u8   | unknown_10   | `0` on every row of clients 1784 and 3483; see Open Questions           |
| `+0x11` | u32  | icon_flags   | One bit per effect icon; see Icon Flags. Set on 757 of the 3,252 type `0` rows, `0` on every type `1` and `2` row (client 3483) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                       |
| ------- | ------------------ | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32                | string_count | 4,362 on client 3483 in `tooltiptable.dbss`; `0` in `tooltiptableoffset.dbss` |
| `+0x04` | pstr[string_count] | strings      | UTF-16 (`is_wide` `1`) on every string of client 3483       |

### `tooltiptableoffset.dbss`

Same frame as the main file: one section per tooltip type, in the same
order, then an empty string table and the 8-byte trailer.

| Offset             | Type                          | Field        | Notes                                                   |
| ------------------ | ----------------------------- | ------------ | ------------------------------------------------------- |
| `+0x00`            | char[4]                       | magic        | ASCII `PABR`                                            |
| `+0x04`            | Index Section[..table_start]  | sections     | Section `n` indexes the rows of section `n` of the main file |
| `sections+0x00`    | String Table                  | string_table | `string_count` is `0`                                   |
| `EOF-0x08`         | u32                           | table_start  | Offset of the string table, where `sections` ends       |
| `EOF-0x04`         | u32                           | zero         | Always `0`                                              |

### Index Section (variable: 4 bytes + index rows)

| Offset  | Type                  | Field     | Notes                                              |
| ------- | --------------------- | --------- | -------------------------------------------------- |
| `+0x00` | u32                   | row_count | Equals the `row_count` of the main file's section  |
| `+0x04` | Index Row[row_count]  | rows      | See Index Row                                      |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                 |
| ------- | ---- | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | key_hash    | Equals the `key_hash` of the row it points at                         |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `tooltiptable.dbss`, at its `key_hash`  |
| `+0x08` | u32  | unknown_08  | `0` on every row of clients 1784 and 3483; see Open Questions         |

The index rows of a section are neither in file order nor in key order;
read in offset order they point at every row of the main file's section,
21 bytes apart (clients 1784 and 3483).

## Layout 1

The row has no `icon_flags`: it ends after `unknown_10`. Only the Row
differs from Layout 2.

### Row (17 bytes)

| Offset  | Type | Field        | Notes                                     |
| ------- | ---- | ------------ | ----------------------------------------- |
| `+0x00` | u32  | key_hash     |                                           |
| `+0x04` | u32  | format_ref   |                                           |
| `+0x08` | u32  | param_count  |                                           |
| `+0x0C` | u32  | tooltip_type |                                           |
| `+0x10` | u8   | unknown_10   | `0` on every row of clients 1230 and 1321 |

## Tooltip Types

The type is the section number. Counts and LOC type 46 coverage on client
3483:

| Type | Rows  | With LOC text | Lines                                                              |
| ---- | ----- | ------------- | ------------------------------------------------------------------ |
| `0`  | 3,252 | 3,240         | Skill tooltip lines: damage per hit (`DAM_ATT`), effects on hit, recovery, class-specific notes |
| `1`  | 564   | 561           | Item effect headings and lines: `ITEM_EFFECT` "Item Effect", enhancement and added effects |
| `2`  | 799   | 799           | Item description lines: set effects (`ITEM_WEAR_EFFECT_COOK`), outfit notes, appearance weapons |

## Icon Flags

Bit `n` of `icon_flags` is one icon. Each bit is named after the English
LOC type 46 lines of the rows that set it (client 3483): the bit-0 rows
read "Invincible for {p0} sec", "Invincible while moving", the bit-9 rows
"Bound on Grapple", "Knockdown on Grapple" and so on.

| Bit  | Icon           | Rows (client 3483) |
| ---- | -------------- | ------------------ |
| `0`  | Invincible     | 47                 |
| `1`  | Super Armor    | 86                 |
| `2`  | Forward Guard  | 69                 |
| `3`  | Knockdown      | 45                 |
| `4`  | Floating       | 54                 |
| `5`  | Bound          | 49                 |
| `6`  | Stun           | 38                 |
| `7`  | Stiffness      | 58                 |
| `8`  | Knockback      | 38                 |
| `9`  | Grapple        | 11                 |
| `10` | Freezing       | 14                 |
| `11` | Down Smash     | 17                 |
| `12` | Air Smash      | 14                 |
| `13` | Down Attack    | 27                 |
| `14` | Air Attack     | 28                 |
| `15` | HP Recovery    | 101                |
| `16` | Resource Recovery (WP, MP or SP) | 97 |
| `17` | Counter Attack | 7                  |
| `18` | Speed Attack   | 4                  |

A row can set several bits ("Super Armor -> Invincible -> Super Armor"
sets bits `0` and `1`). On client 1784 bits `0` to `14` are the same, and
bits `15` to `18` are Counter Attack, Speed Attack, HP Recovery and
Resource Recovery: the `#Table` sheet of a private server's
`datasheet_tooltip_table.xlsm` on client 1784 lists the skill window icons
`1` to `19` in that order (`0` is no icon, `20` unassigned), and on client
1784 icon `N` is bit `N - 1` on every row.

## Field Names

The `Tooltip_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Type`, `Key`, `StringFormat`, `ParamCount`,
`DoNotTranslate` and `Icon`, 3,703 rows. Matched by `(Type,
key_hash(Key))`, 3,496 of the 3,498 rows of client 1784 have a sheet row:

| Field        | Column         | Same value (client 1784) | Same value (client 3483) |
| ------------ | -------------- | ------------------------ | ------------------------ |
| key_hash     | `Key`          | 3,496 of 3,496           | 3,525 of 3,525           |
| tooltip_type | `Type`         | 3,496 of 3,496           | 3,525 of 3,525           |
| format_ref   | `StringFormat` | 3,496 of 3,496           | 2,729 of 3,525           |
| param_count  | `ParamCount`   | 3,496 of 3,496           | 3,449 of 3,525           |
| icon_flags   | `Icon`         | 3,496 of 3,496           | 3,358 of 3,525           |

`key_hash` and `tooltip_type` match by construction of the join. The
client 3483 misses are edited texts and the icon renumbering (Icon Flags).
`Icon` holds a comma-separated list of icon numbers (`1, 2`), which the
file stores as bits; its cell comment calls it the icon number shown in
the skill description window. `DoNotTranslate` (`1` on 17 rows: "do not translate"
in the sheet's cell comment) is not compiled: those rows hold `0` in
`unknown_10` like every other row.

## Notes

- The string key itself is not stored, only its hash. The sheet's cell
  comment calls `Key` the string key and `StringFormat` the format string,
  with parameters `{p0}` to `{p9}`.
- 12 type `0` rows and 3 type `1` rows have no LOC type 46 text on client
  3483.
- The client Lua of client 3483 names no getter of this table.

## Open Questions

### What the Byte Before the Icons Holds

`unknown_10` is `0` on every row of clients 1784 and 3483, including the 17
rows the client 1784 sheet marks `DoNotTranslate`. It could also be the low
byte of a u32 `icon_flags` at `+0x10` with the icons from bit `8`; the
icon numbering from `1` reads more naturally from `+0x11`.

### What the Last u32 of an Index Row Holds

`unknown_08` of `tooltiptableoffset.dbss` is `0` on every index row of
clients 1784 and 3483. Other offset tables store the row size there (21
here); it may also be the high half of a u64 offset.

### Which Tables Use the Keys

No table field documented so far holds a tooltip key hash. Which skill or
item data names the lines, and how the client fills the `{pN}`
placeholders, is open.
