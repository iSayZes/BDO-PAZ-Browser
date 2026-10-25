# `commandtooltip.dbss` Format

## Purpose

The key combination line of a skill tooltip, once for keyboard and mouse
(`pc_command_kr`) and once for the console pad (`console_command_kr`):
`<PAColor0xffd8ff00>{KeyBind:Dash} + {KeyBind:Attack2}<PAOldColor>`, or a
note such as `기술 슬롯에 등록해서 사용 가능` ("Can be added to a Quick
Slot"). Each row is keyed by the hash of a string key such as `WARRIOR_01`;
the key itself is not stored. Both texts are Korean; LOC type 55 holds the
user-language text under the same hash. Companion
`commandtooltipoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                        | Bytes     | Records          | Row bytes                   |
| ------ | -------------- | --------------------------- | --------- | ---------------- | --------------------------- |
| 2      | 1529 and later | `commandtooltip.dbss`       | 3,865,388 | 7,663 Row        | 36 to 2,614, 504 on average |
| 2      | 1529 and later | `commandtooltipoffset.dbss` | 91,976    | 7,663 Offset Row | 12                          |
| 1      | 1239 to 1524   | `commandtooltip.dbss`       | 1,001,964 | 5,289 Row        | 22 to 1,036, 189 on average |
| 1      | 1239 to 1524   | `commandtooltipoffset.dbss` | 63,488    | 5,289 Offset Row | 12                          |

| Layout | File                        | Known               | Unknown         |
| ------ | --------------------------- | ------------------- | --------------- |
| 2      | `commandtooltip.dbss`       | 3,834,736 B (99.2%) | 30,652 B (0.8%) |
| 2      | `commandtooltipoffset.dbss` | 91,976 B (100.0%)   | 0 B (0.0%)      |
| 1      | `commandtooltip.dbss`       | 980,808 B (97.9%)   | 21,156 B (2.1%) |
| 1      | `commandtooltipoffset.dbss` | 63,488 B (100.0%)   | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `866eb676fec0`  |
| 3482   | Layout 2             | `866eb676fec0`  |
| 3474   | Layout 2             | `866eb676fec0`  |
| 3473   | Layout 2             | `866eb676fec0`  |
| 3464   | Layout 2             | `866eb676fec0`  |
| 3458   | Layout 2             | `866eb676fec0`  |
| 3454   | Layout 2             | `866eb676fec0`  |
| 3444   | Layout 2             | `866eb676fec0`  |
| 3435   | Layout 2             | `866eb676fec0`  |
| 3426   | Layout 2             | `866eb676fec0`  |
| 3418   | Layout 2             | `866eb676fec0`  |
| 3412   | Layout 2             | `866eb676fec0`  |
| 3402   | Layout 2             | `866eb676fec0`  |
| 3396   | Layout 2             | `866eb676fec0`  |
| 3387   | Layout 2             | `866eb676fec0`  |
| 3381   | Layout 2             | `866eb676fec0`  |
| 3373   | Layout 2             | `866eb676fec0`  |
| 3364   | Layout 2             | `866eb676fec0`  |
| 3356   | Layout 2             | `866eb676fec0`  |
| 3349   | Layout 2             | `866eb676fec0`  |
| 3342   | Layout 2             | `866eb676fec0`  |
| 3335   | Layout 2             | `866eb676fec0`  |
| 3326   | Layout 2             | `866eb676fec0`  |
| 3321   | Layout 2             | `866eb676fec0`  |
| 3314   | Layout 2             | `866eb676fec0`  |
| 3303   | Layout 2             | `866eb676fec0`  |
| 3302   | Layout 2             | `866eb676fec0`  |
| 3293   | Layout 2             | `866eb676fec0`  |
| 3283   | Layout 2             | `866eb676fec0`  |
| 3275   | Layout 2             | `866eb676fec0`  |
| 3267   | Layout 2             | `866eb676fec0`  |
| 3258   | Layout 2             | `866eb676fec0`  |
| 3251   | Layout 2             | `866eb676fec0`  |
| 3242   | Layout 2             | `866eb676fec0`  |
| 3235   | Layout 2             | `866eb676fec0`  |
| 3229   | Layout 2             | `866eb676fec0`  |
| 3212   | Layout 2             | `866eb676fec0`  |
| 3203   | Layout 2             | `866eb676fec0`  |
| 3193   | Layout 2             | `866eb676fec0`  |
| 3186   | Layout 2             | `866eb676fec0`  |
| 3177   | Layout 2             | `866eb676fec0`  |
| 3169   | Layout 2             | `866eb676fec0`  |
| 3158   | Layout 2             | `866eb676fec0`  |
| 3151   | Layout 2             | `866eb676fec0`  |
| 3144   | Layout 2             | `866eb676fec0`  |
| 3133   | Layout 2             | `866eb676fec0`  |
| 3125   | Layout 2             | `866eb676fec0`  |
| 3118   | Layout 2             | `866eb676fec0`  |
| 3111   | Layout 2             | `866eb676fec0`  |
| 3103   | Layout 2             | `866eb676fec0`  |
| 3095   | Layout 2             | `866eb676fec0`  |
| 3086   | Layout 2             | `866eb676fec0`  |
| 3072   | Layout 2             | `866eb676fec0`  |
| 3062   | Layout 2             | `866eb676fec0`  |
| 3052   | Layout 2             | `866eb676fec0`  |
| 3045   | Layout 2             | `866eb676fec0`  |
| 3037   | Layout 2             | `866eb676fec0`  |
| 3030   | Layout 2             | `866eb676fec0`  |
| 3021   | Layout 2             | `866eb676fec0`  |
| 3012   | Layout 2             | `866eb676fec0`  |
| 3002   | Layout 2             | `866eb676fec0`  |
| 2995   | Layout 2             | `866eb676fec0`  |
| 2987   | Layout 2             | `866eb676fec0`  |
| 2978   | Layout 2             | `866eb676fec0`  |
| 2970   | Layout 2             | `866eb676fec0`  |
| 2959   | Layout 2             | `866eb676fec0`  |
| 2951   | Layout 2             | `866eb676fec0`  |
| 2942   | Layout 2             | `866eb676fec0`  |
| 2935   | Layout 2             | `866eb676fec0`  |
| 2932   | Layout 2             | `866eb676fec0`  |
| 2923   | Layout 2             | `866eb676fec0`  |
| 2919   | Layout 2             | `866eb676fec0`  |
| 2907   | Layout 2             | `866eb676fec0`  |
| 2900   | Layout 2             | `866eb676fec0`  |
| 2891   | Layout 2             | `866eb676fec0`  |
| 2882   | Layout 2             | `866eb676fec0`  |
| 2872   | Layout 2             | `866eb676fec0`  |
| 2863   | Layout 2             | `866eb676fec0`  |
| 2855   | Layout 2             | `866eb676fec0`  |
| 2849   | Layout 2             | `866eb676fec0`  |
| 2844   | Layout 2             | `866eb676fec0`  |
| 2834   | Layout 2             | `866eb676fec0`  |
| 2825   | Layout 2             | `866eb676fec0`  |
| 2819   | Layout 2             | `866eb676fec0`  |
| 2811   | Layout 2             | `866eb676fec0`  |
| 2803   | Layout 2             | `866eb676fec0`  |
| 2794   | Layout 2             | `866eb676fec0`  |
| 2783   | Layout 2             | `866eb676fec0`  |
| 2774   | Layout 2             | `866eb676fec0`  |
| 2765   | Layout 2             | `866eb676fec0`  |
| 2756   | Layout 2             | `866eb676fec0`  |
| 2750   | Layout 2             | `866eb676fec0`  |
| 2743   | Layout 2             | `866eb676fec0`  |
| 2736   | Layout 2             | `866eb676fec0`  |
| 2726   | Layout 2             | `866eb676fec0`  |
| 2717   | Layout 2             | `866eb676fec0`  |
| 2709   | Layout 2             | `866eb676fec0`  |
| 2703   | Layout 2             | `866eb676fec0`  |
| 2695   | Layout 2             | `866eb676fec0`  |
| 2684   | Layout 2             | `866eb676fec0`  |
| 2672   | Layout 2             | `866eb676fec0`  |
| 2665   | Layout 2             | `866eb676fec0`  |
| 2657   | Layout 2             | `866eb676fec0`  |
| 2649   | Layout 2             | `866eb676fec0`  |
| 2644   | Layout 2             | `866eb676fec0`  |
| 2637   | Layout 2             | `866eb676fec0`  |
| 2629   | Layout 2             | `866eb676fec0`  |
| 2619   | Layout 2             | `866eb676fec0`  |
| 2612   | Layout 2             | `866eb676fec0`  |
| 2606   | Layout 2             | `866eb676fec0`  |
| 2602   | Layout 2             | `866eb676fec0`  |
| 2601   | Layout 2             | `866eb676fec0`  |
| 2592   | Layout 2             | `866eb676fec0`  |
| 2583   | Layout 2             | `866eb676fec0`  |
| 2575   | Layout 2             | `866eb676fec0`  |
| 2567   | Layout 2             | `866eb676fec0`  |
| 2560   | Layout 2             | `866eb676fec0`  |
| 2553   | Layout 2             | `866eb676fec0`  |
| 2545   | Layout 2             | `866eb676fec0`  |
| 2538   | Layout 2             | `866eb676fec0`  |
| 2529   | Layout 2             | `866eb676fec0`  |
| 2519   | Layout 2             | `866eb676fec0`  |
| 2513   | Layout 2             | `866eb676fec0`  |
| 2510   | Layout 2             | `866eb676fec0`  |
| 2507   | Layout 2             | `866eb676fec0`  |
| 2503   | Layout 2             | `866eb676fec0`  |
| 2498   | Layout 2             | `866eb676fec0`  |
| 2492   | Layout 2             | `866eb676fec0`  |
| 2487   | Layout 2             | `866eb676fec0`  |
| 2480   | Layout 2             | `866eb676fec0`  |
| 2474   | Layout 2             | `866eb676fec0`  |
| 2468   | Layout 2             | `866eb676fec0`  |
| 2460   | Layout 2             | `866eb676fec0`  |
| 2453   | Layout 2             | `866eb676fec0`  |
| 2444   | Layout 2             | `866eb676fec0`  |
| 2438   | Layout 2             | `866eb676fec0`  |
| 2434   | Layout 2             | `866eb676fec0`  |
| 2429   | Layout 2             | `866eb676fec0`  |
| 2421   | Layout 2             | `866eb676fec0`  |
| 2414   | Layout 2             | `866eb676fec0`  |
| 2407   | Layout 2             | `866eb676fec0`  |
| 2401   | Layout 2             | `866eb676fec0`  |
| 2397   | Layout 2             | `866eb676fec0`  |
| 2393   | Layout 2             | `866eb676fec0`  |
| 2384   | Layout 2             | `866eb676fec0`  |
| 2378   | Layout 2             | `866eb676fec0`  |
| 2372   | Layout 2             | `866eb676fec0`  |
| 2358   | Layout 2             | `866eb676fec0`  |
| 2352   | Layout 2             | `866eb676fec0`  |
| 2347   | Layout 2             | `866eb676fec0`  |
| 2343   | Layout 2             | `866eb676fec0`  |
| 2335   | Layout 2             | `866eb676fec0`  |
| 2327   | Layout 2             | `866eb676fec0`  |
| 2324   | Layout 2             | `866eb676fec0`  |
| 2319   | Layout 2             | `866eb676fec0`  |
| 2313   | Layout 2             | `866eb676fec0`  |
| 2308   | Layout 2             | `866eb676fec0`  |
| 2302   | Layout 2             | `866eb676fec0`  |
| 2295   | Layout 2             | `866eb676fec0`  |
| 2290   | Layout 2             | `866eb676fec0`  |
| 2284   | Layout 2             | `866eb676fec0`  |
| 2276   | Layout 2             | `866eb676fec0`  |
| 2269   | Layout 2             | `866eb676fec0`  |
| 2259   | Layout 2             | `866eb676fec0`  |
| 2250   | Layout 2             | `866eb676fec0`  |
| 2243   | Layout 2             | `866eb676fec0`  |
| 2235   | Layout 2             | `866eb676fec0`  |
| 2229   | Layout 2             | `866eb676fec0`  |
| 2224   | Layout 2             | `866eb676fec0`  |
| 2218   | Layout 2             | `866eb676fec0`  |
| 2215   | Layout 2             | `866eb676fec0`  |
| 2207   | Layout 2             | `866eb676fec0`  |
| 2203   | Layout 2             | `866eb676fec0`  |
| 2196   | Layout 2             | `866eb676fec0`  |
| 2192   | Layout 2             | `866eb676fec0`  |
| 2189   | Layout 2             | `866eb676fec0`  |
| 2183   | Layout 2             | `866eb676fec0`  |
| 2179   | Layout 2             | `866eb676fec0`  |
| 2171   | Layout 2             | `866eb676fec0`  |
| 2163   | Layout 2             | `866eb676fec0`  |
| 2156   | Layout 2             | `866eb676fec0`  |
| 2151   | Layout 2             | `866eb676fec0`  |
| 2147   | Layout 2             | `866eb676fec0`  |
| 2142   | Layout 2             | `866eb676fec0`  |
| 2138   | Layout 2             | `866eb676fec0`  |
| 2134   | Layout 2             | `866eb676fec0`  |
| 2130   | Layout 2             | `866eb676fec0`  |
| 2122   | Layout 2             | `866eb676fec0`  |
| 2107   | Layout 2             | `866eb676fec0`  |
| 2098   | Layout 2             | `866eb676fec0`  |
| 2089   | Layout 2             | `866eb676fec0`  |
| 2081   | Layout 2             | `866eb676fec0`  |
| 2073   | Layout 2             | `866eb676fec0`  |
| 2067   | Layout 2             | `866eb676fec0`  |
| 2063   | Layout 2             | `866eb676fec0`  |
| 2059   | Layout 2             | `866eb676fec0`  |
| 2052   | Layout 2             | `866eb676fec0`  |
| 2044   | Layout 2             | `866eb676fec0`  |
| 2039   | Layout 2             | `866eb676fec0`  |
| 2032   | Layout 2             | `866eb676fec0`  |
| 2025   | Layout 2             | `866eb676fec0`  |
| 2011   | Layout 2             | `866eb676fec0`  |
| 2005   | Layout 2             | `866eb676fec0`  |
| 2000   | Layout 2             | `866eb676fec0`  |
| 1996   | Layout 2             | `866eb676fec0`  |
| 1991   | Layout 2             | `866eb676fec0`  |
| 1985   | Layout 2             | `866eb676fec0`  |
| 1980   | Layout 2             | `866eb676fec0`  |
| 1969   | Layout 2             | `866eb676fec0`  |
| 1964   | Layout 2             | `866eb676fec0`  |
| 1958   | Layout 2             | `866eb676fec0`  |
| 1950   | Layout 2             | `866eb676fec0`  |
| 1945   | Layout 2             | `866eb676fec0`  |
| 1937   | Layout 2             | `866eb676fec0`  |
| 1933   | Layout 2             | `866eb676fec0`  |
| 1927   | Layout 2             | `866eb676fec0`  |
| 1921   | Layout 2             | `866eb676fec0`  |
| 1914   | Layout 2             | `866eb676fec0`  |
| 1908   | Layout 2             | `866eb676fec0`  |
| 1897   | Layout 2             | `866eb676fec0`  |
| 1892   | Layout 2             | `866eb676fec0`  |
| 1886   | Layout 2             | `866eb676fec0`  |
| 1881   | Layout 2             | `866eb676fec0`  |
| 1871   | Layout 2             | `866eb676fec0`  |
| 1866   | Layout 2             | `866eb676fec0`  |
| 1862   | Layout 2             | `866eb676fec0`  |
| 1854   | Layout 2             | `866eb676fec0`  |
| 1846   | Layout 2             | `866eb676fec0`  |
| 1838   | Layout 2             | `866eb676fec0`  |
| 1832   | Layout 2             | `866eb676fec0`  |
| 1826   | Layout 2             | `866eb676fec0`  |
| 1822   | Layout 2             | `866eb676fec0`  |
| 1818   | Layout 2             | `866eb676fec0`  |
| 1804   | Layout 2             | `866eb676fec0`  |
| 1794   | Layout 2             | `866eb676fec0`  |
| 1790   | Layout 2             | `866eb676fec0`  |
| 1784   | Layout 2             | `866eb676fec0`  |
| 1774   | Layout 2             | `866eb676fec0`  |
| 1771   | Layout 2             | `866eb676fec0`  |
| 1762   | Layout 2             | `866eb676fec0`  |
| 1759   | Layout 2             | `866eb676fec0`  |
| 1754   | Layout 2             | `866eb676fec0`  |
| 1749   | Layout 2             | `866eb676fec0`  |
| 1743   | Layout 2             | `866eb676fec0`  |
| 1737   | Layout 2             | `866eb676fec0`  |
| 1731   | Layout 2             | `866eb676fec0`  |
| 1725   | Layout 2             | `866eb676fec0`  |
| 1717   | Layout 2             | `866eb676fec0`  |
| 1710   | Layout 2             | `866eb676fec0`  |
| 1704   | Layout 2             | `866eb676fec0`  |
| 1698   | Layout 2             | `866eb676fec0`  |
| 1690   | Layout 2             | `866eb676fec0`  |
| 1685   | Layout 2             | `866eb676fec0`  |
| 1680   | Layout 2             | `866eb676fec0`  |
| 1674   | Layout 2             | `866eb676fec0`  |
| 1668   | Layout 2             | `866eb676fec0`  |
| 1659   | Layout 2             | `866eb676fec0`  |
| 1649   | Layout 2             | `866eb676fec0`  |
| 1642   | Layout 2             | `866eb676fec0`  |
| 1636   | Layout 2             | `866eb676fec0`  |
| 1628   | Layout 2             | `866eb676fec0`  |
| 1622   | Layout 2             | `866eb676fec0`  |
| 1614   | Layout 2             | `866eb676fec0`  |
| 1608   | Layout 2             | `866eb676fec0`  |
| 1602   | Layout 2             | `866eb676fec0`  |
| 1598   | Layout 2             | `866eb676fec0`  |
| 1594   | Layout 2             | `866eb676fec0`  |
| 1590   | Layout 2             | `866eb676fec0`  |
| 1587   | Layout 2             | `866eb676fec0`  |
| 1584   | Layout 2             | `866eb676fec0`  |
| 1579   | Layout 2             | `866eb676fec0`  |
| 1572   | Layout 2             | `866eb676fec0`  |
| 1565   | Layout 2             | `866eb676fec0`  |
| 1559   | Layout 2             | `866eb676fec0`  |
| 1554   | Layout 2             | `866eb676fec0`  |
| 1547   | Layout 2             | `866eb676fec0`  |
| 1537   | Layout 2             | `866eb676fec0`  |
| 1529   | Layout 2             | `866eb676fec0`  |
| 1524   | Layout 1             | `866eb676fec0`  |
| 1519   | Layout 1             | `866eb676fec0`  |
| 1509   | Layout 1             | `866eb676fec0`  |
| 1506   | Layout 1             | `866eb676fec0`  |
| 1504   | Layout 1             | `866eb676fec0`  |
| 1500   | Layout 1             | `866eb676fec0`  |
| 1493   | Layout 1             | `866eb676fec0`  |
| 1489   | Layout 1             | `866eb676fec0`  |
| 1485   | Layout 1             | `866eb676fec0`  |
| 1481   | Layout 1             | `866eb676fec0`  |
| 1474   | Layout 1             | `866eb676fec0`  |
| 1466   | Layout 1             | `866eb676fec0`  |
| 1462   | Layout 1             | `866eb676fec0`  |
| 1459   | Layout 1             | `866eb676fec0`  |
| 1453   | Layout 1             | `866eb676fec0`  |
| 1450   | Layout 1             | `866eb676fec0`  |
| 1445   | Layout 1             | `866eb676fec0`  |
| 1439   | Layout 1             | `866eb676fec0`  |
| 1433   | Layout 1             | `866eb676fec0`  |
| 1430   | Layout 1             | `866eb676fec0`  |
| 1426   | Layout 1             | `866eb676fec0`  |
| 1421   | Layout 1             | `866eb676fec0`  |
| 1417   | Layout 1             | `866eb676fec0`  |
| 1416   | Layout 1             | `866eb676fec0`  |
| 1409   | Layout 1             | `866eb676fec0`  |
| 1405   | Layout 1             | `866eb676fec0`  |
| 1401   | Layout 1             | `866eb676fec0`  |
| 1396   | Layout 1             | `866eb676fec0`  |
| 1391   | Layout 1             | `866eb676fec0`  |
| 1390   | Layout 1             | `866eb676fec0`  |
| 1386   | Layout 1             | `866eb676fec0`  |
| 1381   | Layout 1             | `866eb676fec0`  |
| 1379   | Layout 1             | `866eb676fec0`  |
| 1372   | Layout 1             | `866eb676fec0`  |
| 1366   | Layout 1             | `866eb676fec0`  |
| 1364   | Layout 1             | `866eb676fec0`  |
| 1363   | Layout 1             | `866eb676fec0`  |
| 1360   | Layout 1             | `866eb676fec0`  |
| 1358   | Layout 1             | `866eb676fec0`  |
| 1355   | Layout 1             | `866eb676fec0`  |
| 1351   | Layout 1             | `866eb676fec0`  |
| 1348   | Layout 1             | `866eb676fec0`  |
| 1346   | Layout 1             | `866eb676fec0`  |
| 1341   | Layout 1             | `866eb676fec0`  |
| 1340   | Layout 1             | `866eb676fec0`  |
| 1338   | Layout 1             | `866eb676fec0`  |
| 1335   | Layout 1             | `866eb676fec0`  |
| 1333   | Layout 1             | `866eb676fec0`  |
| 1329   | Layout 1             | `866eb676fec0`  |
| 1327   | Layout 1             | `866eb676fec0`  |
| 1324   | Layout 1             | `866eb676fec0`  |
| 1321   | Layout 1             | `866eb676fec0`  |
| 1319   | Layout 1             | `866eb676fec0`  |
| 1318   | Layout 1             | `866eb676fec0`  |
| 1316   | Layout 1             | `866eb676fec0`  |
| 1313   | Layout 1             | `866eb676fec0`  |
| 1311   | Layout 1             | `866eb676fec0`  |
| 1309   | Layout 1             | `866eb676fec0`  |
| 1304   | Layout 1             | `866eb676fec0`  |
| 1292   | Layout 1             | `866eb676fec0`  |
| 1286   | Layout 1             | `866eb676fec0`  |
| 1280   | Layout 1             | `866eb676fec0`  |
| 1276   | Layout 1             | `866eb676fec0`  |
| 1267   | Layout 1             | `866eb676fec0`  |
| 1261   | Layout 1             | `866eb676fec0`  |
| 1256   | Layout 1             | `866eb676fec0`  |
| 1250   | Layout 1             | `866eb676fec0`  |
| 1246   | Layout 1             | `866eb676fec0`  |
| 1239   | Layout 1             | `866eb676fec0`  |
| 1230   | No documented layout | `866eb676fec0`  |
| 1226   | No file              | `866eb676fec0`  |
| 1220   | No file              | `866eb676fec0`  |
| 1217   | No file              | `866eb676fec0`  |
| 1211   | No file              | `866eb676fec0`  |
| 1210   | No file              | `866eb676fec0`  |
| 1208   | No file              | `866eb676fec0`  |
| 1203   | No file              | `866eb676fec0`  |
| 1197   | No file              | `866eb676fec0`  |
| 1194   | No file              | `866eb676fec0`  |
| 1192   | No file              | `866eb676fec0`  |
| 1187   | No file              | `866eb676fec0`  |
| 1183   | No file              | `866eb676fec0`  |
| 1177   | No file              | `866eb676fec0`  |
| 1173   | No file              | `866eb676fec0`  |
| 1167   | No file              | `866eb676fec0`  |
| 1164   | No file              | `866eb676fec0`  |
| 1156   | No file              | `866eb676fec0`  |
| 1149   | No file              | `866eb676fec0`  |
| 1144   | No file              | `866eb676fec0`  |
| 1137   | No file              | `866eb676fec0`  |
| 1132   | No file              | `866eb676fec0`  |
| 1127   | No file              | `866eb676fec0`  |
| 1122   | No file              | `866eb676fec0`  |
| 1118   | No file              | `866eb676fec0`  |
| 1114   | No file              | `866eb676fec0`  |
| 1109   | No file              | `866eb676fec0`  |
| 1102   | No file              | `866eb676fec0`  |
| 1096   | No file              | `866eb676fec0`  |
| 1088   | No file              | `866eb676fec0`  |
| 1081   | No file              | `866eb676fec0`  |
| 1076   | No file              | `866eb676fec0`  |
| 1069   | No file              | `866eb676fec0`  |
| 1064   | No file              | `866eb676fec0`  |
| 1058   | No file              | `866eb676fec0`  |
| 1051   | No file              | `866eb676fec0`  |
| 1044   | No file              | `866eb676fec0`  |
| 1036   | No file              | `866eb676fec0`  |
| 1026   | No file              | `866eb676fec0`  |
| 1016   | No file              | `866eb676fec0`  |
| 1009   | No file              | `866eb676fec0`  |
| 1005   | No file              | `866eb676fec0`  |
| 1000   | No file              | `866eb676fec0`  |
| 998    | No file              | `866eb676fec0`  |
| 990    | No file              | `866eb676fec0`  |
| 979    | No file              | `866eb676fec0`  |
| 972    | No file              | `866eb676fec0`  |
| 963    | No file              | `866eb676fec0`  |
| 955    | No file              | `866eb676fec0`  |
| 946    | No file              | `866eb676fec0`  |
| 938    | No file              | `866eb676fec0`  |
| 927    | No file              | `866eb676fec0`  |
| 911    | No file              | `866eb676fec0`  |
| 904    | No file              | `866eb676fec0`  |
| 899    | No file              | `866eb676fec0`  |
| 894    | No file              | `866eb676fec0`  |
| 885    | No file              | `866eb676fec0`  |
| 879    | No file              | `866eb676fec0`  |
| 872    | No file              | `866eb676fec0`  |
| 864    | No file              | `866eb676fec0`  |
| 855    | No file              | `866eb676fec0`  |
| 853    | No file              | `866eb676fec0`  |
| 845    | No file              | `866eb676fec0`  |
| 837    | No file              | `866eb676fec0`  |
| 829    | No file              | `866eb676fec0`  |
| 822    | No file              | `866eb676fec0`  |
| 814    | No file              | `866eb676fec0`  |
| 805    | No file              | `866eb676fec0`  |
| 794    | No file              | `866eb676fec0`  |
| 787    | No file              | `866eb676fec0`  |
| 780    | No file              | `866eb676fec0`  |
| 771    | No file              | `866eb676fec0`  |
| 760    | No file              | `866eb676fec0`  |
| 748    | No file              | `866eb676fec0`  |
| 741    | No file              | `866eb676fec0`  |
| 736    | No file              | `866eb676fec0`  |
| 731    | No file              | `866eb676fec0`  |
| 723    | No file              | `866eb676fec0`  |
| 711    | No file              | `866eb676fec0`  |
| 707    | No file              | `866eb676fec0`  |
| 697    | No file              | `866eb676fec0`  |
| 689    | No file              | `866eb676fec0`  |
| 683    | No file              | `866eb676fec0`  |
| 678    | No file              | `866eb676fec0`  |
| 670    | No file              | `866eb676fec0`  |
| 661    | No file              | `866eb676fec0`  |
| 656    | No file              | `866eb676fec0`  |
| 652    | No file              | `866eb676fec0`  |
| 643    | No file              | `866eb676fec0`  |
| 637    | No file              | `866eb676fec0`  |
| 630    | No file              | `866eb676fec0`  |
| 627    | No file              | `866eb676fec0`  |
| 621    | No file              | `866eb676fec0`  |
| 617    | No file              | `866eb676fec0`  |
| 615    | No file              | `866eb676fec0`  |
| 606    | No file              | `866eb676fec0`  |
| 599    | No file              | `866eb676fec0`  |
| 592    | No file              | `866eb676fec0`  |
| 586    | No file              | `866eb676fec0`  |
| 577    | No file              | `866eb676fec0`  |
| 569    | No file              | `866eb676fec0`  |
| 561    | No file              | `866eb676fec0`  |
| 554    | No file              | `866eb676fec0`  |
| 542    | No file              | `866eb676fec0`  |
| 532    | No file              | `866eb676fec0`  |
| 531    | No file              | `866eb676fec0`  |
| 526    | No file              | `866eb676fec0`  |
| 521    | No file              | `866eb676fec0`  |
| 517    | No file              | `866eb676fec0`  |
| 510    | No file              | `866eb676fec0`  |
| 508    | No file              | `866eb676fec0`  |
| 504    | No file              | `866eb676fec0`  |
| 497    | No file              | `866eb676fec0`  |
| 491    | No file              | `866eb676fec0`  |
| 485    | No file              | `866eb676fec0`  |
| 478    | No file              | `866eb676fec0`  |
| 472    | No file              | `866eb676fec0`  |
| 466    | No file              | `866eb676fec0`  |
| 457    | No file              | `866eb676fec0`  |
| 452    | No file              | `866eb676fec0`  |
| 449    | No file              | `866eb676fec0`  |
| 435    | No file              | `866eb676fec0`  |

<!-- versions:end -->

## Companion Files

| File                        | Required | Role                                                                          |
| --------------------------- | -------- | ----------------------------------------------------------------------------- |
| `commandtooltipoffset.dbss` | Optional | `key_hash -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`       | Optional | Both texts in the user's language (type `55`)                                  |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type       | Field | Notes                                 |
| ------- | ---------- | ----- | ------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `7663` on client 3483 |
| `+0x04` | Row[count] | rows  | See Row                               |

### Row (variable: 24 bytes + texts)

| Offset                    | Type  | Field                         | Notes |
| ------------------------- | ----- | ----------------------------- | ----- |
| `+0x00`                   | u32   | key_hash                      | `key_hash()` of the row's string key (lookup3 over its UTF-16LE text, seed `0xC5EDE`, `_common/string_hash.py`); unique per row |
| `+0x04`                   | str16 | pc_command_kr                 | Korean text for keyboard and mouse; LOC type 55 `(key_hash, 0)`. Line breaks are the two characters `\n` |
| `pc_command_kr+0x00`      | str16 | console_command_kr            | Korean text for the console pad; LOC type 55 `(key_hash, 1)`. Equals `pc_command_kr` on 6,817 of 7,663 rows (client 3483) |
| `console_command_kr+0x00` | u32   | unknown_console_command_kr_00 | `0` on every row of clients 1784 and 3483 |

The rows are not sorted by key. The LOC type 55 key is
`(key_hash, 0, 0, variant)`: variant `0` is `pc_command_kr`, `1` is
`console_command_kr`. On client 3483 every row has both LOC rows.

### `commandtooltipoffset.dbss`

`PABR` index with 12-byte rows and a u32 key.

| Offset              | Type              | Field              | Notes                                         |
| ------------------- | ----------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]           | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32               | count              | Equals the `commandtooltip.dbss` count        |
| `+0x08`             | Offset Row[count] | rows               | See Offset Row                                |
| `rows+0x00`         | String Table      | string_table       | The PABR string table, present but empty      |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 12 x count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                    |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                       |
| ------- | ---- | ----------- | ----------------------------------------------------------- |
| `+0x00` | u32  | key_hash    | Key of the row it points at                                 |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `commandtooltip.dbss`, at its `key_hash` |
| `+0x08` | u32  | data_size   | The whole row                                               |

Read by `parse_pabr_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in another order than the file; read in offset order they
cover the main file from `+0x04` to its end, and every index row points at
the row with its key (clients 1784 and 3483).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 1

### Row (variable: 16 bytes + text)

One text per row: `console_command_kr` is not there yet.

| Offset               | Type  | Field                         | Notes |
| -------------------- | ----- | ----------------------------- | ----- |
| `+0x00`              | u32   | key_hash                      |       |
| `+0x04`              | str16 | pc_command_kr                 |       |
| `pc_command_kr+0x00` | u32   | unknown_console_command_kr_00 |       |

## Field Names

The `Command_Tooltip_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Key`, `PC`, `Console`, `Sura` and `Nachal`,
5,822 rows. `key_hash()` of every `Key` is a `key_hash` of client 1784,
whose file also has 5,822 rows. Matched by that hash:

| Field              | Column    | Same value (client 1784) | Same value (client 3483) |
| ------------------ | --------- | ------------------------ | ------------------------ |
| key_hash           | `Key`     | 5,822 of 5,822 (hashed)  | 5,822 of 5,822 (hashed)  |
| pc_command_kr      | `PC`      | 5,822 of 5,822           | 1,394 of 5,822           |
| console_command_kr | `Console` | 5,822 of 5,822           | 3,813 of 5,822           |

`Sura` and `Nachal` equal `PC` on 5,814 of 5,822 rows and are not
compiled. The client 3483 misses are rewritten texts: on client 1784 no
`PC` text and 4,259 `Console` texts hold a `{KeyBind:...}` placeholder,
on client 3483 most texts of both fields do (see Notes). The field names add
`_command`, after the client Lua: `panel_tooltip_skill.luac` reads a skill's
`getCommand()`, and `getConsoleCommand()` when `_ContentsGroup_isConsole` is
set.

## Notes

- The sheet keys are `<CLASS>_<number>` (`WARRIOR_01`, `BLADER_102`) plus
  `COMMON_*`, `GUILD_*` and a few others. The `PatternControl` column of the
  `SkillType_Table_New` sheet of the same workbook names the key of each
  skill, and `skilltype.dbss` holds these keys as `str16` text in its
  `config` block: 7,535 of the 7,663 hashes of client 3483 are the hash of
  such a text there.
- On client 3483, 5,726 `pc_command_kr` and 5,623 `console_command_kr`
  texts hold a `{KeyBind:...}` placeholder.
- Client 1784 also has `simplecommandtooltip.dbss` and its offset file
  (sheet `SimpleCommandTooltip_Table`, columns `skillKey` and `Tooltip`);
  client 3483 has neither.
- Client 1230, the first test client with the file, fits neither layout:
  its first row breaks at `pc_command_kr` (`+0x10` in the file).

## Open Questions

### What the Last u32 Holds

`unknown_console_command_kr_00` is `0` on every row of clients 1784 and
3483. The sheet has no fifth compiled column (`Sura` and `Nachal` do not
reach the file), and the 2016 PDB has no command tooltip struct to give
the member its name.
