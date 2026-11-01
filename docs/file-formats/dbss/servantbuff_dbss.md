# `servantbuff.dbss` Format

## Purpose

Horse interaction (Horse Communion) actions: one record per interaction with
an optional class condition, the player's action, the horse's action and the
skill it uses. [servantinteraction.dbss](servantinteraction_dbss.md) lists
which of these each servant offers. On client 3474 the file has 4 records:
keys 1 to 3 are Horse Communion 1 to 3 (skills 220 to 222), key 4 is the
Tamer's version (`checkClass(16)`, skill 15526 `말과교감_금수랑전용`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records      | Row bytes                |
| ------ | -------------- | ------------------------ | ----- | ------------ | ------------------------ |
| 2      | 3464 and later | `servantbuff.dbss`       | 384   | 4 Record     | 88 to 116, 95 on average |
| 2      | 3464 and later | `servantbuffoffset.dbss` | 52    | 4 Offset Row | 12                       |
| 1      | 1346 to 3458   | `servantbuff.dbss`       | 368   | 4 Record     | 84 to 112, 91 on average |
| 1      | 1346 to 3458   | `servantbuffoffset.dbss` | 44    | 4 Offset Row | 10                       |

| Layout | File                     | Known          | Unknown    |
| ------ | ------------------------ | -------------- | ---------- |
| 2      | `servantbuff.dbss`       | 384 B (100.0%) | 0 B (0.0%) |
| 2      | `servantbuffoffset.dbss` | 52 B (100.0%)  | 0 B (0.0%) |
| 1      | `servantbuff.dbss`       | 368 B (100.0%) | 0 B (0.0%) |
| 1      | `servantbuffoffset.dbss` | 44 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `a395f18365da`  |
| 3482   | Layout 2             | `a395f18365da`  |
| 3474   | Layout 2             | `a395f18365da`  |
| 3473   | Layout 2             | `a395f18365da`  |
| 3464   | Layout 2             | `a395f18365da`  |
| 3458   | Layout 1             | `a395f18365da`  |
| 3454   | Layout 1             | `a395f18365da`  |
| 3444   | Layout 1             | `a395f18365da`  |
| 3435   | Layout 1             | `a395f18365da`  |
| 3426   | Layout 1             | `a395f18365da`  |
| 3418   | Layout 1             | `a395f18365da`  |
| 3412   | Layout 1             | `a395f18365da`  |
| 3402   | Layout 1             | `a395f18365da`  |
| 3396   | Layout 1             | `a395f18365da`  |
| 3387   | Layout 1             | `a395f18365da`  |
| 3381   | Layout 1             | `a395f18365da`  |
| 3373   | Layout 1             | `a395f18365da`  |
| 3364   | Layout 1             | `a395f18365da`  |
| 3356   | Layout 1             | `a395f18365da`  |
| 3349   | Layout 1             | `a395f18365da`  |
| 3342   | Layout 1             | `a395f18365da`  |
| 3335   | Layout 1             | `a395f18365da`  |
| 3326   | Layout 1             | `a395f18365da`  |
| 3321   | Layout 1             | `a395f18365da`  |
| 3314   | Layout 1             | `a395f18365da`  |
| 3303   | Layout 1             | `a395f18365da`  |
| 3302   | Layout 1             | `a395f18365da`  |
| 3293   | Layout 1             | `a395f18365da`  |
| 3283   | Layout 1             | `a395f18365da`  |
| 3275   | Layout 1             | `a395f18365da`  |
| 3267   | Layout 1             | `a395f18365da`  |
| 3258   | Layout 1             | `a395f18365da`  |
| 3251   | Layout 1             | `a395f18365da`  |
| 3242   | Layout 1             | `a395f18365da`  |
| 3235   | Layout 1             | `a395f18365da`  |
| 3229   | Layout 1             | `a395f18365da`  |
| 3212   | Layout 1             | `a395f18365da`  |
| 3203   | Layout 1             | `a395f18365da`  |
| 3193   | Layout 1             | `a395f18365da`  |
| 3186   | Layout 1             | `a395f18365da`  |
| 3177   | Layout 1             | `a395f18365da`  |
| 3169   | Layout 1             | `a395f18365da`  |
| 3158   | Layout 1             | `a395f18365da`  |
| 3151   | Layout 1             | `a395f18365da`  |
| 3144   | Layout 1             | `a395f18365da`  |
| 3133   | Layout 1             | `a395f18365da`  |
| 3125   | Layout 1             | `a395f18365da`  |
| 3118   | Layout 1             | `a395f18365da`  |
| 3111   | Layout 1             | `a395f18365da`  |
| 3103   | Layout 1             | `a395f18365da`  |
| 3095   | Layout 1             | `a395f18365da`  |
| 3086   | Layout 1             | `a395f18365da`  |
| 3072   | Layout 1             | `a395f18365da`  |
| 3062   | Layout 1             | `a395f18365da`  |
| 3052   | Layout 1             | `a395f18365da`  |
| 3045   | Layout 1             | `a395f18365da`  |
| 3037   | Layout 1             | `a395f18365da`  |
| 3030   | Layout 1             | `a395f18365da`  |
| 3021   | Layout 1             | `a395f18365da`  |
| 3012   | Layout 1             | `a395f18365da`  |
| 3002   | Layout 1             | `a395f18365da`  |
| 2995   | Layout 1             | `a395f18365da`  |
| 2987   | Layout 1             | `a395f18365da`  |
| 2978   | Layout 1             | `a395f18365da`  |
| 2970   | Layout 1             | `a395f18365da`  |
| 2959   | Layout 1             | `a395f18365da`  |
| 2951   | Layout 1             | `a395f18365da`  |
| 2942   | Layout 1             | `a395f18365da`  |
| 2935   | Layout 1             | `a395f18365da`  |
| 2932   | Layout 1             | `a395f18365da`  |
| 2923   | Layout 1             | `a395f18365da`  |
| 2919   | Layout 1             | `a395f18365da`  |
| 2907   | Layout 1             | `a395f18365da`  |
| 2900   | Layout 1             | `a395f18365da`  |
| 2891   | Layout 1             | `a395f18365da`  |
| 2882   | Layout 1             | `a395f18365da`  |
| 2872   | Layout 1             | `a395f18365da`  |
| 2863   | Layout 1             | `a395f18365da`  |
| 2855   | Layout 1             | `a395f18365da`  |
| 2849   | Layout 1             | `a395f18365da`  |
| 2844   | Layout 1             | `a395f18365da`  |
| 2834   | Layout 1             | `a395f18365da`  |
| 2825   | Layout 1             | `a395f18365da`  |
| 2819   | Layout 1             | `a395f18365da`  |
| 2811   | Layout 1             | `a395f18365da`  |
| 2803   | Layout 1             | `a395f18365da`  |
| 2794   | Layout 1             | `a395f18365da`  |
| 2783   | Layout 1             | `a395f18365da`  |
| 2774   | Layout 1             | `a395f18365da`  |
| 2765   | Layout 1             | `a395f18365da`  |
| 2756   | Layout 1             | `a395f18365da`  |
| 2750   | Layout 1             | `a395f18365da`  |
| 2743   | Layout 1             | `a395f18365da`  |
| 2736   | Layout 1             | `a395f18365da`  |
| 2726   | Layout 1             | `a395f18365da`  |
| 2717   | Layout 1             | `a395f18365da`  |
| 2709   | Layout 1             | `a395f18365da`  |
| 2703   | Layout 1             | `a395f18365da`  |
| 2695   | Layout 1             | `a395f18365da`  |
| 2684   | Layout 1             | `a395f18365da`  |
| 2672   | Layout 1             | `a395f18365da`  |
| 2665   | Layout 1             | `a395f18365da`  |
| 2657   | Layout 1             | `a395f18365da`  |
| 2649   | Layout 1             | `a395f18365da`  |
| 2644   | Layout 1             | `a395f18365da`  |
| 2637   | Layout 1             | `a395f18365da`  |
| 2629   | Layout 1             | `a395f18365da`  |
| 2619   | Layout 1             | `a395f18365da`  |
| 2612   | Layout 1             | `a395f18365da`  |
| 2606   | Layout 1             | `a395f18365da`  |
| 2602   | Layout 1             | `a395f18365da`  |
| 2601   | Layout 1             | `a395f18365da`  |
| 2592   | Layout 1             | `a395f18365da`  |
| 2583   | Layout 1             | `a395f18365da`  |
| 2575   | Layout 1             | `a395f18365da`  |
| 2567   | Layout 1             | `a395f18365da`  |
| 2560   | Layout 1             | `a395f18365da`  |
| 2553   | Layout 1             | `a395f18365da`  |
| 2545   | Layout 1             | `a395f18365da`  |
| 2538   | Layout 1             | `a395f18365da`  |
| 2529   | Layout 1             | `a395f18365da`  |
| 2519   | Layout 1             | `a395f18365da`  |
| 2513   | Layout 1             | `a395f18365da`  |
| 2510   | Layout 1             | `a395f18365da`  |
| 2507   | Layout 1             | `a395f18365da`  |
| 2503   | Layout 1             | `a395f18365da`  |
| 2498   | Layout 1             | `a395f18365da`  |
| 2492   | Layout 1             | `a395f18365da`  |
| 2487   | Layout 1             | `a395f18365da`  |
| 2480   | Layout 1             | `a395f18365da`  |
| 2474   | Layout 1             | `a395f18365da`  |
| 2468   | Layout 1             | `a395f18365da`  |
| 2460   | Layout 1             | `a395f18365da`  |
| 2453   | Layout 1             | `a395f18365da`  |
| 2444   | Layout 1             | `a395f18365da`  |
| 2438   | Layout 1             | `a395f18365da`  |
| 2434   | Layout 1             | `a395f18365da`  |
| 2429   | Layout 1             | `a395f18365da`  |
| 2421   | Layout 1             | `a395f18365da`  |
| 2414   | Layout 1             | `a395f18365da`  |
| 2407   | Layout 1             | `a395f18365da`  |
| 2401   | Layout 1             | `a395f18365da`  |
| 2397   | Layout 1             | `a395f18365da`  |
| 2393   | Layout 1             | `a395f18365da`  |
| 2384   | Layout 1             | `a395f18365da`  |
| 2378   | Layout 1             | `a395f18365da`  |
| 2372   | Layout 1             | `a395f18365da`  |
| 2358   | Layout 1             | `a395f18365da`  |
| 2352   | Layout 1             | `a395f18365da`  |
| 2347   | Layout 1             | `a395f18365da`  |
| 2343   | Layout 1             | `a395f18365da`  |
| 2335   | Layout 1             | `a395f18365da`  |
| 2327   | Layout 1             | `a395f18365da`  |
| 2324   | Layout 1             | `a395f18365da`  |
| 2319   | Layout 1             | `a395f18365da`  |
| 2313   | Layout 1             | `a395f18365da`  |
| 2308   | Layout 1             | `a395f18365da`  |
| 2302   | Layout 1             | `a395f18365da`  |
| 2295   | Layout 1             | `a395f18365da`  |
| 2290   | Layout 1             | `a395f18365da`  |
| 2284   | Layout 1             | `a395f18365da`  |
| 2276   | Layout 1             | `a395f18365da`  |
| 2269   | Layout 1             | `a395f18365da`  |
| 2259   | Layout 1             | `a395f18365da`  |
| 2250   | Layout 1             | `a395f18365da`  |
| 2243   | Layout 1             | `a395f18365da`  |
| 2235   | Layout 1             | `a395f18365da`  |
| 2229   | Layout 1             | `a395f18365da`  |
| 2224   | Layout 1             | `a395f18365da`  |
| 2218   | Layout 1             | `a395f18365da`  |
| 2215   | Layout 1             | `a395f18365da`  |
| 2207   | Layout 1             | `a395f18365da`  |
| 2203   | Layout 1             | `a395f18365da`  |
| 2196   | Layout 1             | `a395f18365da`  |
| 2192   | Layout 1             | `a395f18365da`  |
| 2189   | Layout 1             | `a395f18365da`  |
| 2183   | Layout 1             | `a395f18365da`  |
| 2179   | Layout 1             | `a395f18365da`  |
| 2171   | Layout 1             | `a395f18365da`  |
| 2163   | Layout 1             | `a395f18365da`  |
| 2156   | Layout 1             | `a395f18365da`  |
| 2151   | Layout 1             | `a395f18365da`  |
| 2147   | Layout 1             | `a395f18365da`  |
| 2142   | Layout 1             | `a395f18365da`  |
| 2138   | Layout 1             | `a395f18365da`  |
| 2134   | Layout 1             | `a395f18365da`  |
| 2130   | Layout 1             | `a395f18365da`  |
| 2122   | Layout 1             | `a395f18365da`  |
| 2107   | Layout 1             | `a395f18365da`  |
| 2098   | Layout 1             | `a395f18365da`  |
| 2089   | Layout 1             | `a395f18365da`  |
| 2081   | Layout 1             | `a395f18365da`  |
| 2073   | Layout 1             | `a395f18365da`  |
| 2067   | Layout 1             | `a395f18365da`  |
| 2063   | Layout 1             | `a395f18365da`  |
| 2059   | Layout 1             | `a395f18365da`  |
| 2052   | Layout 1             | `a395f18365da`  |
| 2044   | Layout 1             | `a395f18365da`  |
| 2039   | Layout 1             | `a395f18365da`  |
| 2032   | Layout 1             | `a395f18365da`  |
| 2025   | Layout 1             | `a395f18365da`  |
| 2011   | Layout 1             | `a395f18365da`  |
| 2005   | Layout 1             | `a395f18365da`  |
| 2000   | Layout 1             | `a395f18365da`  |
| 1996   | Layout 1             | `a395f18365da`  |
| 1991   | Layout 1             | `a395f18365da`  |
| 1985   | Layout 1             | `a395f18365da`  |
| 1980   | Layout 1             | `a395f18365da`  |
| 1969   | Layout 1             | `a395f18365da`  |
| 1964   | Layout 1             | `a395f18365da`  |
| 1958   | Layout 1             | `a395f18365da`  |
| 1950   | Layout 1             | `a395f18365da`  |
| 1945   | Layout 1             | `a395f18365da`  |
| 1937   | Layout 1             | `a395f18365da`  |
| 1933   | Layout 1             | `a395f18365da`  |
| 1927   | Layout 1             | `a395f18365da`  |
| 1921   | Layout 1             | `a395f18365da`  |
| 1914   | Layout 1             | `a395f18365da`  |
| 1908   | Layout 1             | `a395f18365da`  |
| 1897   | Layout 1             | `a395f18365da`  |
| 1892   | Layout 1             | `a395f18365da`  |
| 1886   | Layout 1             | `a395f18365da`  |
| 1881   | Layout 1             | `a395f18365da`  |
| 1871   | Layout 1             | `a395f18365da`  |
| 1866   | Layout 1             | `a395f18365da`  |
| 1862   | Layout 1             | `a395f18365da`  |
| 1854   | Layout 1             | `a395f18365da`  |
| 1846   | Layout 1             | `a395f18365da`  |
| 1838   | Layout 1             | `a395f18365da`  |
| 1832   | Layout 1             | `a395f18365da`  |
| 1826   | Layout 1             | `a395f18365da`  |
| 1822   | Layout 1             | `a395f18365da`  |
| 1818   | Layout 1             | `a395f18365da`  |
| 1804   | Layout 1             | `a395f18365da`  |
| 1794   | Layout 1             | `a395f18365da`  |
| 1790   | Layout 1             | `a395f18365da`  |
| 1784   | Layout 1             | `a395f18365da`  |
| 1774   | Layout 1             | `a395f18365da`  |
| 1771   | Layout 1             | `a395f18365da`  |
| 1762   | Layout 1             | `a395f18365da`  |
| 1759   | Layout 1             | `a395f18365da`  |
| 1754   | Layout 1             | `a395f18365da`  |
| 1749   | Layout 1             | `a395f18365da`  |
| 1743   | Layout 1             | `a395f18365da`  |
| 1737   | Layout 1             | `a395f18365da`  |
| 1731   | Layout 1             | `a395f18365da`  |
| 1725   | Layout 1             | `a395f18365da`  |
| 1717   | Layout 1             | `a395f18365da`  |
| 1710   | Layout 1             | `a395f18365da`  |
| 1704   | Layout 1             | `a395f18365da`  |
| 1698   | Layout 1             | `a395f18365da`  |
| 1690   | Layout 1             | `a395f18365da`  |
| 1685   | Layout 1             | `a395f18365da`  |
| 1680   | Layout 1             | `a395f18365da`  |
| 1674   | Layout 1             | `a395f18365da`  |
| 1668   | Layout 1             | `a395f18365da`  |
| 1659   | Layout 1             | `a395f18365da`  |
| 1649   | Layout 1             | `a395f18365da`  |
| 1642   | Layout 1             | `a395f18365da`  |
| 1636   | Layout 1             | `a395f18365da`  |
| 1628   | Layout 1             | `a395f18365da`  |
| 1622   | Layout 1             | `a395f18365da`  |
| 1614   | Layout 1             | `a395f18365da`  |
| 1608   | Layout 1             | `a395f18365da`  |
| 1602   | Layout 1             | `a395f18365da`  |
| 1598   | Layout 1             | `a395f18365da`  |
| 1594   | Layout 1             | `a395f18365da`  |
| 1590   | Layout 1             | `a395f18365da`  |
| 1587   | Layout 1             | `a395f18365da`  |
| 1584   | Layout 1             | `a395f18365da`  |
| 1579   | Layout 1             | `a395f18365da`  |
| 1572   | Layout 1             | `a395f18365da`  |
| 1565   | Layout 1             | `a395f18365da`  |
| 1559   | Layout 1             | `a395f18365da`  |
| 1554   | Layout 1             | `a395f18365da`  |
| 1547   | Layout 1             | `a395f18365da`  |
| 1537   | Layout 1             | `a395f18365da`  |
| 1529   | Layout 1             | `a395f18365da`  |
| 1524   | Layout 1             | `a395f18365da`  |
| 1519   | Layout 1             | `a395f18365da`  |
| 1509   | Layout 1             | `a395f18365da`  |
| 1506   | Layout 1             | `a395f18365da`  |
| 1504   | Layout 1             | `a395f18365da`  |
| 1500   | Layout 1             | `a395f18365da`  |
| 1493   | Layout 1             | `a395f18365da`  |
| 1489   | Layout 1             | `a395f18365da`  |
| 1485   | Layout 1             | `a395f18365da`  |
| 1481   | Layout 1             | `a395f18365da`  |
| 1474   | Layout 1             | `a395f18365da`  |
| 1466   | Layout 1             | `a395f18365da`  |
| 1462   | Layout 1             | `a395f18365da`  |
| 1459   | Layout 1             | `a395f18365da`  |
| 1453   | Layout 1             | `a395f18365da`  |
| 1450   | Layout 1             | `a395f18365da`  |
| 1445   | Layout 1             | `a395f18365da`  |
| 1439   | Layout 1             | `a395f18365da`  |
| 1433   | Layout 1             | `a395f18365da`  |
| 1430   | Layout 1             | `a395f18365da`  |
| 1426   | Layout 1             | `a395f18365da`  |
| 1421   | Layout 1             | `a395f18365da`  |
| 1417   | Layout 1             | `a395f18365da`  |
| 1416   | Layout 1             | `a395f18365da`  |
| 1409   | Layout 1             | `a395f18365da`  |
| 1405   | Layout 1             | `a395f18365da`  |
| 1401   | Layout 1             | `a395f18365da`  |
| 1396   | Layout 1             | `a395f18365da`  |
| 1391   | Layout 1             | `a395f18365da`  |
| 1390   | Layout 1             | `a395f18365da`  |
| 1386   | Layout 1             | `a395f18365da`  |
| 1381   | Layout 1             | `a395f18365da`  |
| 1379   | Layout 1             | `a395f18365da`  |
| 1372   | Layout 1             | `a395f18365da`  |
| 1366   | Layout 1             | `a395f18365da`  |
| 1364   | Layout 1             | `a395f18365da`  |
| 1363   | Layout 1             | `a395f18365da`  |
| 1360   | Layout 1             | `a395f18365da`  |
| 1358   | Layout 1             | `a395f18365da`  |
| 1355   | Layout 1             | `a395f18365da`  |
| 1351   | Layout 1             | `a395f18365da`  |
| 1348   | Layout 1             | `a395f18365da`  |
| 1346   | Layout 1             | `a395f18365da`  |
| 1341   | No documented layout | `a395f18365da`  |
| 1340   | No documented layout | `a395f18365da`  |
| 1338   | No documented layout | `a395f18365da`  |
| 1335   | No documented layout | `a395f18365da`  |
| 1333   | No documented layout | `a395f18365da`  |
| 1329   | No documented layout | `a395f18365da`  |
| 1327   | No documented layout | `a395f18365da`  |
| 1324   | No documented layout | `a395f18365da`  |
| 1321   | No documented layout | `a395f18365da`  |
| 1319   | No documented layout | `a395f18365da`  |
| 1318   | No documented layout | `a395f18365da`  |
| 1316   | No documented layout | `a395f18365da`  |
| 1313   | No documented layout | `a395f18365da`  |
| 1311   | No documented layout | `a395f18365da`  |
| 1309   | No documented layout | `a395f18365da`  |
| 1304   | No documented layout | `a395f18365da`  |
| 1292   | No documented layout | `a395f18365da`  |
| 1286   | No documented layout | `a395f18365da`  |
| 1280   | No documented layout | `a395f18365da`  |
| 1276   | No documented layout | `a395f18365da`  |
| 1267   | No file              | `a395f18365da`  |
| 1261   | No file              | `a395f18365da`  |
| 1256   | No documented layout | `a395f18365da`  |
| 1250   | No file              | `a395f18365da`  |
| 1246   | No file              | `a395f18365da`  |
| 1239   | No file              | `a395f18365da`  |
| 1230   | No file              | `a395f18365da`  |
| 1226   | No file              | `a395f18365da`  |
| 1220   | No file              | `a395f18365da`  |
| 1217   | No file              | `a395f18365da`  |
| 1211   | No file              | `a395f18365da`  |
| 1210   | No file              | `a395f18365da`  |
| 1208   | No file              | `a395f18365da`  |
| 1203   | No file              | `a395f18365da`  |
| 1197   | No file              | `a395f18365da`  |
| 1194   | No file              | `a395f18365da`  |
| 1192   | No file              | `a395f18365da`  |
| 1187   | No file              | `a395f18365da`  |
| 1183   | No file              | `a395f18365da`  |
| 1177   | No file              | `a395f18365da`  |
| 1173   | No file              | `a395f18365da`  |
| 1167   | No file              | `a395f18365da`  |
| 1164   | No file              | `a395f18365da`  |
| 1156   | No file              | `a395f18365da`  |
| 1149   | No file              | `a395f18365da`  |
| 1144   | No file              | `a395f18365da`  |
| 1137   | No file              | `a395f18365da`  |
| 1132   | No file              | `a395f18365da`  |
| 1127   | No file              | `a395f18365da`  |
| 1122   | No file              | `a395f18365da`  |
| 1118   | No file              | `a395f18365da`  |
| 1114   | No file              | `a395f18365da`  |
| 1109   | No file              | `a395f18365da`  |
| 1102   | No file              | `a395f18365da`  |
| 1096   | No file              | `a395f18365da`  |
| 1088   | No file              | `a395f18365da`  |
| 1081   | No file              | `a395f18365da`  |
| 1076   | No file              | `a395f18365da`  |
| 1069   | No file              | `a395f18365da`  |
| 1064   | No file              | `a395f18365da`  |
| 1058   | No file              | `a395f18365da`  |
| 1051   | No file              | `a395f18365da`  |
| 1044   | No file              | `a395f18365da`  |
| 1036   | No file              | `a395f18365da`  |
| 1026   | No file              | `a395f18365da`  |
| 1016   | No file              | `a395f18365da`  |
| 1009   | No file              | `a395f18365da`  |
| 1005   | No file              | `a395f18365da`  |
| 1000   | No file              | `a395f18365da`  |
| 998    | No file              | `a395f18365da`  |
| 990    | No file              | `a395f18365da`  |
| 979    | No file              | `a395f18365da`  |
| 972    | No file              | `a395f18365da`  |
| 963    | No file              | `a395f18365da`  |
| 955    | No file              | `a395f18365da`  |
| 946    | No file              | `a395f18365da`  |
| 938    | No file              | `a395f18365da`  |
| 927    | No file              | `a395f18365da`  |
| 911    | No file              | `a395f18365da`  |
| 904    | No file              | `a395f18365da`  |
| 899    | No file              | `a395f18365da`  |
| 894    | No file              | `a395f18365da`  |
| 885    | No file              | `a395f18365da`  |
| 879    | No file              | `a395f18365da`  |
| 872    | No file              | `a395f18365da`  |
| 864    | No file              | `a395f18365da`  |
| 855    | No file              | `a395f18365da`  |
| 853    | No file              | `a395f18365da`  |
| 845    | No file              | `a395f18365da`  |
| 837    | No file              | `a395f18365da`  |
| 829    | No file              | `a395f18365da`  |
| 822    | No file              | `a395f18365da`  |
| 814    | No file              | `a395f18365da`  |
| 805    | No file              | `a395f18365da`  |
| 794    | No file              | `a395f18365da`  |
| 787    | No file              | `a395f18365da`  |
| 780    | No file              | `a395f18365da`  |
| 771    | No file              | `a395f18365da`  |
| 760    | No file              | `a395f18365da`  |
| 748    | No file              | `a395f18365da`  |
| 741    | No file              | `a395f18365da`  |
| 736    | No file              | `a395f18365da`  |
| 731    | No file              | `a395f18365da`  |
| 723    | No file              | `a395f18365da`  |
| 711    | No file              | `a395f18365da`  |
| 707    | No file              | `a395f18365da`  |
| 697    | No file              | `a395f18365da`  |
| 689    | No file              | `a395f18365da`  |
| 683    | No file              | `a395f18365da`  |
| 678    | No file              | `a395f18365da`  |
| 670    | No file              | `a395f18365da`  |
| 661    | No file              | `a395f18365da`  |
| 656    | No file              | `a395f18365da`  |
| 652    | No file              | `a395f18365da`  |
| 643    | No file              | `a395f18365da`  |
| 637    | No file              | `a395f18365da`  |
| 630    | No file              | `a395f18365da`  |
| 627    | No file              | `a395f18365da`  |
| 621    | No file              | `a395f18365da`  |
| 617    | No file              | `a395f18365da`  |
| 615    | No file              | `a395f18365da`  |
| 606    | No file              | `a395f18365da`  |
| 599    | No file              | `a395f18365da`  |
| 592    | No file              | `a395f18365da`  |
| 586    | No file              | `a395f18365da`  |
| 577    | No file              | `a395f18365da`  |
| 569    | No file              | `a395f18365da`  |
| 561    | No file              | `a395f18365da`  |
| 554    | No file              | `a395f18365da`  |
| 542    | No file              | `a395f18365da`  |
| 532    | No file              | `a395f18365da`  |
| 531    | No file              | `a395f18365da`  |
| 526    | No file              | `a395f18365da`  |
| 521    | No file              | `a395f18365da`  |
| 517    | No file              | `a395f18365da`  |
| 510    | No file              | `a395f18365da`  |
| 508    | No file              | `a395f18365da`  |
| 504    | No file              | `a395f18365da`  |
| 497    | No file              | `a395f18365da`  |
| 491    | No file              | `a395f18365da`  |
| 485    | No file              | `a395f18365da`  |
| 478    | No file              | `a395f18365da`  |
| 472    | No file              | `a395f18365da`  |
| 466    | No file              | `a395f18365da`  |
| 457    | No file              | `a395f18365da`  |
| 452    | No file              | `a395f18365da`  |
| 449    | No file              | `a395f18365da`  |
| 435    | No file              | `a395f18365da`  |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                          |
| ------------------------ | -------- | --------------------------------------------- |
| `servantbuffoffset.dbss` | Optional | Index: key to the record's offset and size    |
| `languagedata_en.loc`    | Optional | `skill_no` names (LOC type 10); without a row, the Korean `skilltype.dbss` name |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | 4 on client 3474                       |
| `+0x04` | Record[count] | records | Back to back, variable size, up to EOF |

### Record (variable: 42 bytes + condition and action names)

| Offset                       | Type  | Field               | Notes |
| ---------------------------- | ----- | ------------------- | ----- |
| `+0x00`                      | u32   | key                 | 4 down to 1 on client 3474 |
| `+0x04`                      | u32   | key_dup             | Equals `key` on every record |
| `+0x08`                      | str16 | condition           | Empty except `checkClass(16)` (Tamer) on key 4 |
| `condition+0x00`             | str8  | action_name         | `VEHICLE_INTERACTION_HORSE_1` to `_4` |
| `action_name+0x00`           | u32   | action_hash         | Hash of `action_name` ([Action Hashes](#action-hashes)) |
| `action_name+0x04`           | str8  | servant_action_name | `HORSE_INTERACTION_1` to `_3`; key 4 uses `_3` |
| `servant_action_name+0x00`   | u32   | servant_action_hash | Hash of `servant_action_name`; equal on keys 3 and 4 |
| `servant_action_name+0x04`   | u16   | skill_no            | `skill.dbss` skill number: 220, 221, 222, 15526 |

### `servantbuffoffset.dbss`

| Offset  | Type              | Field   | Notes                          |
| ------- | ----------------- | ------- | ------------------------------ |
| `+0x00` | u32               | count   | Equals the main file's count   |
| `+0x04` | Offset Row[count] | entries | `count` entries of 12 bytes    |

### Offset Row (12 bytes)

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u32  | key    | The record's `key`                                       |
| `+0x04` | u32  | offset | Where the record's `key_dup` starts, 4 bytes into the record |
| `+0x08` | u32  | size   | Record size minus 4                                      |

## Layout 1

Client 1784 stores both keys and the index key as u16 and has 3 records
(keys 3 to 1, no condition).

### Record (variable: 38 bytes + condition and action names)

| Offset                       | Type  | Field               | Notes |
| ---------------------------- | ----- | ------------------- | ----- |
| `+0x00`                      | u16   | key                 | |
| `+0x02`                      | u16   | key_dup             | |
| `+0x04`                      | str16 | condition           | Empty on every record |
| `condition+0x00`             | str8  | action_name         | |
| `action_name+0x00`           | u32   | action_hash         | |
| `action_name+0x04`           | str8  | servant_action_name | |
| `servant_action_name+0x00`   | u32   | servant_action_hash | |
| `servant_action_name+0x04`   | u16   | skill_no            | |

### Offset Row (10 bytes)

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u16  | key    | |
| `+0x02` | u32  | offset | Where the record's `key_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size   | Record size minus 2                                      |

## Field Names

The record follows the 2016 `gc::ServantBuffStaticStatus` member for member:
`_key`, `_conditionString`, `_actionName`, `_actionHashKey`,
`_servantActionName`, `_servantActionHashKey`, `_skillNo`. The
`ServantBuff_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 (`Index`, `UseCondition`, `ActionName`, `SkillNo`,
`ServantActionName`) matches all 3 records of clients 1784 and 3474 by
value in every column.

## Action Hashes

`action_hash` and `servant_action_hash` are the client's lookup3
`hashlittle` with seed `0xC5EDE` over the ASCII bytes of the name before
them, as in `manufacture.bss` (`ascii_key_hash` in
`_common/string_hash.py`); all 4 records of client 3474 match.

## Notes

- No `servantinteraction.dbss` record lists key 4 on client 3474; every
  record lists 1, 2 and 3. How the Tamer's version is offered is not in
  either file.
