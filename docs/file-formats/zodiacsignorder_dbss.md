# `zodiacsignorder.dbss` Format

## Purpose

The order in which the stars of a zodiac constellation light up, per
personality type: 2 variants x 12 signs = 24 records. The stars are the
`star_positions` of [`zodiacsign.dbss`](zodiacsign_dbss.md), and
`personality_type` is the one `npcpersonality.dbss` uses.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records          | Row bytes               |
| ------ | -------------- | ------- | ---------------------------- | ----- | ---------------- | ----------------------- |
| 1      | 1346 and later | 3483    | `zodiacsignorder.dbss`       | 604   | 24 Record        | 23 to 29, 25 on average |
| 1      | 1346 and later | 3483    | `zodiacsignorderoffset.dbss` | 244   | 24 Offset Record | 10                      |

| Layout | File                         | Known         | Unknown      |
| ------ | ---------------------------- | ------------- | ------------ |
| 1      | `zodiacsignorder.dbss`       | 508 B (84.1%) | 96 B (15.9%) |
| 1      | `zodiacsignorderoffset.dbss` | 196 B (80.3%) | 48 B (19.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `2fbad018e504`  |
| 3482   | Layout 1             | `2fbad018e504`  |
| 3474   | Layout 1             | `2fbad018e504`  |
| 3473   | Layout 1             | `2fbad018e504`  |
| 3464   | Layout 1             | `2fbad018e504`  |
| 3458   | Layout 1             | `2fbad018e504`  |
| 3454   | Layout 1             | `2fbad018e504`  |
| 3444   | Layout 1             | `2fbad018e504`  |
| 3435   | Layout 1             | `2fbad018e504`  |
| 3426   | Layout 1             | `2fbad018e504`  |
| 3418   | Layout 1             | `2fbad018e504`  |
| 3412   | Layout 1             | `2fbad018e504`  |
| 3402   | Layout 1             | `2fbad018e504`  |
| 3396   | Layout 1             | `2fbad018e504`  |
| 3387   | Layout 1             | `2fbad018e504`  |
| 3381   | Layout 1             | `2fbad018e504`  |
| 3373   | Layout 1             | `2fbad018e504`  |
| 3364   | Layout 1             | `2fbad018e504`  |
| 3356   | Layout 1             | `2fbad018e504`  |
| 3349   | Layout 1             | `2fbad018e504`  |
| 3342   | Layout 1             | `2fbad018e504`  |
| 3335   | Layout 1             | `2fbad018e504`  |
| 3326   | Layout 1             | `2fbad018e504`  |
| 3321   | Layout 1             | `2fbad018e504`  |
| 3314   | Layout 1             | `2fbad018e504`  |
| 3303   | Layout 1             | `2fbad018e504`  |
| 3302   | Layout 1             | `2fbad018e504`  |
| 3293   | Layout 1             | `2fbad018e504`  |
| 3283   | Layout 1             | `2fbad018e504`  |
| 3275   | Layout 1             | `2fbad018e504`  |
| 3267   | Layout 1             | `2fbad018e504`  |
| 3258   | Layout 1             | `2fbad018e504`  |
| 3251   | Layout 1             | `2fbad018e504`  |
| 3242   | Layout 1             | `2fbad018e504`  |
| 3235   | Layout 1             | `2fbad018e504`  |
| 3229   | Layout 1             | `2fbad018e504`  |
| 3212   | Layout 1             | `2fbad018e504`  |
| 3203   | Layout 1             | `2fbad018e504`  |
| 3193   | Layout 1             | `2fbad018e504`  |
| 3186   | Layout 1             | `2fbad018e504`  |
| 3177   | Layout 1             | `2fbad018e504`  |
| 3169   | Layout 1             | `2fbad018e504`  |
| 3158   | Layout 1             | `2fbad018e504`  |
| 3151   | Layout 1             | `2fbad018e504`  |
| 3144   | Layout 1             | `2fbad018e504`  |
| 3133   | Layout 1             | `2fbad018e504`  |
| 3125   | Layout 1             | `2fbad018e504`  |
| 3118   | Layout 1             | `2fbad018e504`  |
| 3111   | Layout 1             | `2fbad018e504`  |
| 3103   | Layout 1             | `2fbad018e504`  |
| 3095   | Layout 1             | `2fbad018e504`  |
| 3086   | Layout 1             | `2fbad018e504`  |
| 3072   | Layout 1             | `2fbad018e504`  |
| 3062   | Layout 1             | `2fbad018e504`  |
| 3052   | Layout 1             | `2fbad018e504`  |
| 3045   | Layout 1             | `2fbad018e504`  |
| 3037   | Layout 1             | `2fbad018e504`  |
| 3030   | Layout 1             | `2fbad018e504`  |
| 3021   | Layout 1             | `2fbad018e504`  |
| 3012   | Layout 1             | `2fbad018e504`  |
| 3002   | Layout 1             | `2fbad018e504`  |
| 2995   | Layout 1             | `2fbad018e504`  |
| 2987   | Layout 1             | `2fbad018e504`  |
| 2978   | Layout 1             | `2fbad018e504`  |
| 2970   | Layout 1             | `2fbad018e504`  |
| 2959   | Layout 1             | `2fbad018e504`  |
| 2951   | Layout 1             | `2fbad018e504`  |
| 2942   | Layout 1             | `2fbad018e504`  |
| 2935   | Layout 1             | `2fbad018e504`  |
| 2932   | Layout 1             | `2fbad018e504`  |
| 2923   | Layout 1             | `2fbad018e504`  |
| 2919   | Layout 1             | `2fbad018e504`  |
| 2907   | Layout 1             | `2fbad018e504`  |
| 2900   | Layout 1             | `2fbad018e504`  |
| 2891   | Layout 1             | `2fbad018e504`  |
| 2882   | Layout 1             | `2fbad018e504`  |
| 2872   | Layout 1             | `2fbad018e504`  |
| 2863   | Layout 1             | `2fbad018e504`  |
| 2855   | Layout 1             | `2fbad018e504`  |
| 2849   | Layout 1             | `2fbad018e504`  |
| 2844   | Layout 1             | `2fbad018e504`  |
| 2834   | Layout 1             | `2fbad018e504`  |
| 2825   | Layout 1             | `2fbad018e504`  |
| 2819   | Layout 1             | `2fbad018e504`  |
| 2811   | Layout 1             | `2fbad018e504`  |
| 2803   | Layout 1             | `2fbad018e504`  |
| 2794   | Layout 1             | `2fbad018e504`  |
| 2783   | Layout 1             | `2fbad018e504`  |
| 2774   | Layout 1             | `2fbad018e504`  |
| 2765   | Layout 1             | `2fbad018e504`  |
| 2756   | Layout 1             | `2fbad018e504`  |
| 2750   | Layout 1             | `2fbad018e504`  |
| 2743   | Layout 1             | `2fbad018e504`  |
| 2736   | Layout 1             | `2fbad018e504`  |
| 2726   | Layout 1             | `2fbad018e504`  |
| 2717   | Layout 1             | `2fbad018e504`  |
| 2709   | Layout 1             | `2fbad018e504`  |
| 2703   | Layout 1             | `2fbad018e504`  |
| 2695   | Layout 1             | `2fbad018e504`  |
| 2684   | Layout 1             | `2fbad018e504`  |
| 2672   | Layout 1             | `2fbad018e504`  |
| 2665   | Layout 1             | `2fbad018e504`  |
| 2657   | Layout 1             | `2fbad018e504`  |
| 2649   | Layout 1             | `2fbad018e504`  |
| 2644   | Layout 1             | `2fbad018e504`  |
| 2637   | Layout 1             | `2fbad018e504`  |
| 2629   | Layout 1             | `2fbad018e504`  |
| 2619   | Layout 1             | `2fbad018e504`  |
| 2612   | Layout 1             | `2fbad018e504`  |
| 2606   | Layout 1             | `2fbad018e504`  |
| 2602   | Layout 1             | `2fbad018e504`  |
| 2601   | Layout 1             | `2fbad018e504`  |
| 2592   | Layout 1             | `2fbad018e504`  |
| 2583   | Layout 1             | `2fbad018e504`  |
| 2575   | Layout 1             | `2fbad018e504`  |
| 2567   | Layout 1             | `2fbad018e504`  |
| 2560   | Layout 1             | `2fbad018e504`  |
| 2553   | Layout 1             | `2fbad018e504`  |
| 2545   | Layout 1             | `2fbad018e504`  |
| 2538   | Layout 1             | `2fbad018e504`  |
| 2529   | Layout 1             | `2fbad018e504`  |
| 2519   | Layout 1             | `2fbad018e504`  |
| 2513   | Layout 1             | `2fbad018e504`  |
| 2510   | Layout 1             | `2fbad018e504`  |
| 2507   | Layout 1             | `2fbad018e504`  |
| 2503   | Layout 1             | `2fbad018e504`  |
| 2498   | Layout 1             | `2fbad018e504`  |
| 2492   | Layout 1             | `2fbad018e504`  |
| 2487   | Layout 1             | `2fbad018e504`  |
| 2480   | Layout 1             | `2fbad018e504`  |
| 2474   | Layout 1             | `2fbad018e504`  |
| 2468   | Layout 1             | `2fbad018e504`  |
| 2460   | Layout 1             | `2fbad018e504`  |
| 2453   | Layout 1             | `2fbad018e504`  |
| 2444   | Layout 1             | `2fbad018e504`  |
| 2438   | Layout 1             | `2fbad018e504`  |
| 2434   | Layout 1             | `2fbad018e504`  |
| 2429   | Layout 1             | `2fbad018e504`  |
| 2421   | Layout 1             | `2fbad018e504`  |
| 2414   | Layout 1             | `2fbad018e504`  |
| 2407   | Layout 1             | `2fbad018e504`  |
| 2401   | Layout 1             | `2fbad018e504`  |
| 2397   | Layout 1             | `2fbad018e504`  |
| 2393   | Layout 1             | `2fbad018e504`  |
| 2384   | Layout 1             | `2fbad018e504`  |
| 2378   | Layout 1             | `2fbad018e504`  |
| 2372   | Layout 1             | `2fbad018e504`  |
| 2358   | Layout 1             | `2fbad018e504`  |
| 2352   | Layout 1             | `2fbad018e504`  |
| 2347   | Layout 1             | `2fbad018e504`  |
| 2343   | Layout 1             | `2fbad018e504`  |
| 2335   | Layout 1             | `2fbad018e504`  |
| 2327   | Layout 1             | `2fbad018e504`  |
| 2324   | Layout 1             | `2fbad018e504`  |
| 2319   | Layout 1             | `2fbad018e504`  |
| 2313   | Layout 1             | `2fbad018e504`  |
| 2308   | Layout 1             | `2fbad018e504`  |
| 2302   | Layout 1             | `2fbad018e504`  |
| 2295   | Layout 1             | `2fbad018e504`  |
| 2290   | Layout 1             | `2fbad018e504`  |
| 2284   | Layout 1             | `2fbad018e504`  |
| 2276   | Layout 1             | `2fbad018e504`  |
| 2269   | Layout 1             | `2fbad018e504`  |
| 2259   | Layout 1             | `2fbad018e504`  |
| 2250   | Layout 1             | `2fbad018e504`  |
| 2243   | Layout 1             | `2fbad018e504`  |
| 2235   | Layout 1             | `2fbad018e504`  |
| 2229   | Layout 1             | `2fbad018e504`  |
| 2224   | Layout 1             | `2fbad018e504`  |
| 2218   | Layout 1             | `2fbad018e504`  |
| 2215   | Layout 1             | `2fbad018e504`  |
| 2207   | Layout 1             | `2fbad018e504`  |
| 2203   | Layout 1             | `2fbad018e504`  |
| 2196   | Layout 1             | `2fbad018e504`  |
| 2192   | Layout 1             | `2fbad018e504`  |
| 2189   | Layout 1             | `2fbad018e504`  |
| 2183   | Layout 1             | `2fbad018e504`  |
| 2179   | Layout 1             | `2fbad018e504`  |
| 2171   | Layout 1             | `2fbad018e504`  |
| 2163   | Layout 1             | `2fbad018e504`  |
| 2156   | Layout 1             | `2fbad018e504`  |
| 2151   | Layout 1             | `2fbad018e504`  |
| 2147   | Layout 1             | `2fbad018e504`  |
| 2142   | Layout 1             | `2fbad018e504`  |
| 2138   | Layout 1             | `2fbad018e504`  |
| 2134   | Layout 1             | `2fbad018e504`  |
| 2130   | Layout 1             | `2fbad018e504`  |
| 2122   | Layout 1             | `2fbad018e504`  |
| 2107   | Layout 1             | `2fbad018e504`  |
| 2098   | Layout 1             | `2fbad018e504`  |
| 2089   | Layout 1             | `2fbad018e504`  |
| 2081   | Layout 1             | `2fbad018e504`  |
| 2073   | Layout 1             | `2fbad018e504`  |
| 2067   | Layout 1             | `2fbad018e504`  |
| 2063   | Layout 1             | `2fbad018e504`  |
| 2059   | Layout 1             | `2fbad018e504`  |
| 2052   | Layout 1             | `2fbad018e504`  |
| 2044   | Layout 1             | `2fbad018e504`  |
| 2039   | Layout 1             | `2fbad018e504`  |
| 2032   | Layout 1             | `2fbad018e504`  |
| 2025   | Layout 1             | `2fbad018e504`  |
| 2011   | Layout 1             | `2fbad018e504`  |
| 2005   | Layout 1             | `2fbad018e504`  |
| 2000   | Layout 1             | `2fbad018e504`  |
| 1996   | Layout 1             | `2fbad018e504`  |
| 1991   | Layout 1             | `2fbad018e504`  |
| 1985   | Layout 1             | `2fbad018e504`  |
| 1980   | Layout 1             | `2fbad018e504`  |
| 1969   | Layout 1             | `2fbad018e504`  |
| 1964   | Layout 1             | `2fbad018e504`  |
| 1958   | Layout 1             | `2fbad018e504`  |
| 1950   | Layout 1             | `2fbad018e504`  |
| 1945   | Layout 1             | `2fbad018e504`  |
| 1937   | Layout 1             | `2fbad018e504`  |
| 1933   | Layout 1             | `2fbad018e504`  |
| 1927   | Layout 1             | `2fbad018e504`  |
| 1921   | Layout 1             | `2fbad018e504`  |
| 1914   | Layout 1             | `2fbad018e504`  |
| 1908   | Layout 1             | `2fbad018e504`  |
| 1897   | Layout 1             | `2fbad018e504`  |
| 1892   | Layout 1             | `2fbad018e504`  |
| 1886   | Layout 1             | `2fbad018e504`  |
| 1881   | Layout 1             | `2fbad018e504`  |
| 1871   | Layout 1             | `2fbad018e504`  |
| 1866   | Layout 1             | `2fbad018e504`  |
| 1862   | Layout 1             | `2fbad018e504`  |
| 1854   | Layout 1             | `2fbad018e504`  |
| 1846   | Layout 1             | `2fbad018e504`  |
| 1838   | Layout 1             | `2fbad018e504`  |
| 1832   | Layout 1             | `2fbad018e504`  |
| 1826   | Layout 1             | `2fbad018e504`  |
| 1822   | Layout 1             | `2fbad018e504`  |
| 1818   | Layout 1             | `2fbad018e504`  |
| 1804   | Layout 1             | `2fbad018e504`  |
| 1794   | Layout 1             | `2fbad018e504`  |
| 1790   | Layout 1             | `2fbad018e504`  |
| 1784   | Layout 1             | `2fbad018e504`  |
| 1774   | Layout 1             | `2fbad018e504`  |
| 1771   | Layout 1             | `2fbad018e504`  |
| 1762   | Layout 1             | `2fbad018e504`  |
| 1759   | Layout 1             | `2fbad018e504`  |
| 1754   | Layout 1             | `2fbad018e504`  |
| 1749   | Layout 1             | `2fbad018e504`  |
| 1743   | Layout 1             | `2fbad018e504`  |
| 1737   | Layout 1             | `2fbad018e504`  |
| 1731   | Layout 1             | `2fbad018e504`  |
| 1725   | Layout 1             | `2fbad018e504`  |
| 1717   | Layout 1             | `2fbad018e504`  |
| 1710   | Layout 1             | `2fbad018e504`  |
| 1704   | Layout 1             | `2fbad018e504`  |
| 1698   | Layout 1             | `2fbad018e504`  |
| 1690   | Layout 1             | `2fbad018e504`  |
| 1685   | Layout 1             | `2fbad018e504`  |
| 1680   | Layout 1             | `2fbad018e504`  |
| 1674   | Layout 1             | `2fbad018e504`  |
| 1668   | Layout 1             | `2fbad018e504`  |
| 1659   | Layout 1             | `2fbad018e504`  |
| 1649   | Layout 1             | `2fbad018e504`  |
| 1642   | Layout 1             | `2fbad018e504`  |
| 1636   | Layout 1             | `2fbad018e504`  |
| 1628   | Layout 1             | `2fbad018e504`  |
| 1622   | Layout 1             | `2fbad018e504`  |
| 1614   | Layout 1             | `2fbad018e504`  |
| 1608   | Layout 1             | `2fbad018e504`  |
| 1602   | Layout 1             | `2fbad018e504`  |
| 1598   | Layout 1             | `2fbad018e504`  |
| 1594   | Layout 1             | `2fbad018e504`  |
| 1590   | Layout 1             | `2fbad018e504`  |
| 1587   | Layout 1             | `2fbad018e504`  |
| 1584   | Layout 1             | `2fbad018e504`  |
| 1579   | Layout 1             | `2fbad018e504`  |
| 1572   | Layout 1             | `2fbad018e504`  |
| 1565   | Layout 1             | `2fbad018e504`  |
| 1559   | Layout 1             | `2fbad018e504`  |
| 1554   | Layout 1             | `2fbad018e504`  |
| 1547   | Layout 1             | `2fbad018e504`  |
| 1537   | Layout 1             | `2fbad018e504`  |
| 1529   | Layout 1             | `2fbad018e504`  |
| 1524   | Layout 1             | `2fbad018e504`  |
| 1519   | Layout 1             | `2fbad018e504`  |
| 1509   | Layout 1             | `2fbad018e504`  |
| 1506   | Layout 1             | `2fbad018e504`  |
| 1504   | Layout 1             | `2fbad018e504`  |
| 1500   | Layout 1             | `2fbad018e504`  |
| 1493   | Layout 1             | `2fbad018e504`  |
| 1489   | Layout 1             | `2fbad018e504`  |
| 1485   | Layout 1             | `2fbad018e504`  |
| 1481   | Layout 1             | `2fbad018e504`  |
| 1474   | Layout 1             | `2fbad018e504`  |
| 1466   | Layout 1             | `2fbad018e504`  |
| 1462   | Layout 1             | `2fbad018e504`  |
| 1459   | Layout 1             | `2fbad018e504`  |
| 1453   | Layout 1             | `2fbad018e504`  |
| 1450   | Layout 1             | `2fbad018e504`  |
| 1445   | Layout 1             | `2fbad018e504`  |
| 1439   | Layout 1             | `2fbad018e504`  |
| 1433   | Layout 1             | `2fbad018e504`  |
| 1430   | Layout 1             | `2fbad018e504`  |
| 1426   | Layout 1             | `2fbad018e504`  |
| 1421   | Layout 1             | `2fbad018e504`  |
| 1417   | Layout 1             | `2fbad018e504`  |
| 1416   | Layout 1             | `2fbad018e504`  |
| 1409   | Layout 1             | `2fbad018e504`  |
| 1405   | Layout 1             | `2fbad018e504`  |
| 1401   | Layout 1             | `2fbad018e504`  |
| 1396   | Layout 1             | `2fbad018e504`  |
| 1391   | Layout 1             | `2fbad018e504`  |
| 1390   | Layout 1             | `2fbad018e504`  |
| 1386   | Layout 1             | `2fbad018e504`  |
| 1381   | Layout 1             | `2fbad018e504`  |
| 1379   | Layout 1             | `2fbad018e504`  |
| 1372   | Layout 1             | `2fbad018e504`  |
| 1366   | Layout 1             | `2fbad018e504`  |
| 1364   | Layout 1             | `2fbad018e504`  |
| 1363   | Layout 1             | `2fbad018e504`  |
| 1360   | Layout 1             | `2fbad018e504`  |
| 1358   | Layout 1             | `2fbad018e504`  |
| 1355   | Layout 1             | `2fbad018e504`  |
| 1351   | Layout 1             | `2fbad018e504`  |
| 1348   | Layout 1             | `2fbad018e504`  |
| 1346   | Layout 1             | `2fbad018e504`  |
| 1341   | No documented layout | `2fbad018e504`  |
| 1340   | No documented layout | `2fbad018e504`  |
| 1338   | No documented layout | `2fbad018e504`  |
| 1335   | No documented layout | `2fbad018e504`  |
| 1333   | No documented layout | `2fbad018e504`  |
| 1329   | No documented layout | `2fbad018e504`  |
| 1327   | No documented layout | `2fbad018e504`  |
| 1324   | No documented layout | `2fbad018e504`  |
| 1321   | No documented layout | `2fbad018e504`  |
| 1319   | No documented layout | `2fbad018e504`  |
| 1318   | No documented layout | `2fbad018e504`  |
| 1316   | No documented layout | `2fbad018e504`  |
| 1313   | No documented layout | `2fbad018e504`  |
| 1311   | No documented layout | `2fbad018e504`  |
| 1309   | No documented layout | `2fbad018e504`  |
| 1304   | No documented layout | `2fbad018e504`  |
| 1292   | No documented layout | `2fbad018e504`  |
| 1286   | No documented layout | `2fbad018e504`  |
| 1280   | No documented layout | `2fbad018e504`  |
| 1276   | No documented layout | `2fbad018e504`  |
| 1267   | No documented layout | `2fbad018e504`  |
| 1261   | No documented layout | `2fbad018e504`  |
| 1256   | No documented layout | `2fbad018e504`  |
| 1250   | No documented layout | `2fbad018e504`  |
| 1246   | No file              | `2fbad018e504`  |
| 1239   | No file              | `2fbad018e504`  |
| 1230   | No file              | `2fbad018e504`  |
| 1226   | No file              | `2fbad018e504`  |
| 1220   | No file              | `2fbad018e504`  |
| 1217   | No file              | `2fbad018e504`  |
| 1211   | No file              | `2fbad018e504`  |
| 1210   | No file              | `2fbad018e504`  |
| 1208   | No file              | `2fbad018e504`  |
| 1203   | No file              | `2fbad018e504`  |
| 1197   | No file              | `2fbad018e504`  |
| 1194   | No file              | `2fbad018e504`  |
| 1192   | No file              | `2fbad018e504`  |
| 1187   | No file              | `2fbad018e504`  |
| 1183   | No file              | `2fbad018e504`  |
| 1177   | No file              | `2fbad018e504`  |
| 1173   | No file              | `2fbad018e504`  |
| 1167   | No file              | `2fbad018e504`  |
| 1164   | No file              | `2fbad018e504`  |
| 1156   | No file              | `2fbad018e504`  |
| 1149   | No file              | `2fbad018e504`  |
| 1144   | No file              | `2fbad018e504`  |
| 1137   | No file              | `2fbad018e504`  |
| 1132   | No file              | `2fbad018e504`  |
| 1127   | No file              | `2fbad018e504`  |
| 1122   | No file              | `2fbad018e504`  |
| 1118   | No file              | `2fbad018e504`  |
| 1114   | No file              | `2fbad018e504`  |
| 1109   | No file              | `2fbad018e504`  |
| 1102   | No file              | `2fbad018e504`  |
| 1096   | No file              | `2fbad018e504`  |
| 1088   | No file              | `2fbad018e504`  |
| 1081   | No file              | `2fbad018e504`  |
| 1076   | No file              | `2fbad018e504`  |
| 1069   | No file              | `2fbad018e504`  |
| 1064   | No file              | `2fbad018e504`  |
| 1058   | No file              | `2fbad018e504`  |
| 1051   | No file              | `2fbad018e504`  |
| 1044   | No file              | `2fbad018e504`  |
| 1036   | No file              | `2fbad018e504`  |
| 1026   | No file              | `2fbad018e504`  |
| 1016   | No file              | `2fbad018e504`  |
| 1009   | No file              | `2fbad018e504`  |
| 1005   | No file              | `2fbad018e504`  |
| 1000   | No file              | `2fbad018e504`  |
| 998    | No file              | `2fbad018e504`  |
| 990    | No file              | `2fbad018e504`  |
| 979    | No file              | `2fbad018e504`  |
| 972    | No file              | `2fbad018e504`  |
| 963    | No file              | `2fbad018e504`  |
| 955    | No file              | `2fbad018e504`  |
| 946    | No file              | `2fbad018e504`  |
| 938    | No file              | `2fbad018e504`  |
| 927    | No file              | `2fbad018e504`  |
| 911    | No file              | `2fbad018e504`  |
| 904    | No file              | `2fbad018e504`  |
| 899    | No file              | `2fbad018e504`  |
| 894    | No file              | `2fbad018e504`  |
| 885    | No file              | `2fbad018e504`  |
| 879    | No file              | `2fbad018e504`  |
| 872    | No file              | `2fbad018e504`  |
| 864    | No file              | `2fbad018e504`  |
| 855    | No file              | `2fbad018e504`  |
| 853    | No file              | `2fbad018e504`  |
| 845    | No file              | `2fbad018e504`  |
| 837    | No file              | `2fbad018e504`  |
| 829    | No file              | `2fbad018e504`  |
| 822    | No file              | `2fbad018e504`  |
| 814    | No file              | `2fbad018e504`  |
| 805    | No file              | `2fbad018e504`  |
| 794    | No file              | `2fbad018e504`  |
| 787    | No file              | `2fbad018e504`  |
| 780    | No file              | `2fbad018e504`  |
| 771    | No file              | `2fbad018e504`  |
| 760    | No file              | `2fbad018e504`  |
| 748    | No file              | `2fbad018e504`  |
| 741    | No file              | `2fbad018e504`  |
| 736    | No file              | `2fbad018e504`  |
| 731    | No file              | `2fbad018e504`  |
| 723    | No file              | `2fbad018e504`  |
| 711    | No file              | `2fbad018e504`  |
| 707    | No file              | `2fbad018e504`  |
| 697    | No file              | `2fbad018e504`  |
| 689    | No file              | `2fbad018e504`  |
| 683    | No file              | `2fbad018e504`  |
| 678    | No file              | `2fbad018e504`  |
| 670    | No file              | `2fbad018e504`  |
| 661    | No file              | `2fbad018e504`  |
| 656    | No file              | `2fbad018e504`  |
| 652    | No file              | `2fbad018e504`  |
| 643    | No file              | `2fbad018e504`  |
| 637    | No file              | `2fbad018e504`  |
| 630    | No file              | `2fbad018e504`  |
| 627    | No file              | `2fbad018e504`  |
| 621    | No file              | `2fbad018e504`  |
| 617    | No file              | `2fbad018e504`  |
| 615    | No file              | `2fbad018e504`  |
| 606    | No file              | `2fbad018e504`  |
| 599    | No file              | `2fbad018e504`  |
| 592    | No file              | `2fbad018e504`  |
| 586    | No file              | `2fbad018e504`  |
| 577    | No file              | `2fbad018e504`  |
| 569    | No file              | `2fbad018e504`  |
| 561    | No file              | `2fbad018e504`  |
| 554    | No file              | `2fbad018e504`  |
| 542    | No file              | `2fbad018e504`  |
| 532    | No file              | `2fbad018e504`  |
| 531    | No file              | `2fbad018e504`  |
| 526    | No file              | `2fbad018e504`  |
| 521    | No file              | `2fbad018e504`  |
| 517    | No file              | `2fbad018e504`  |
| 510    | No file              | `2fbad018e504`  |
| 508    | No file              | `2fbad018e504`  |
| 504    | No file              | `2fbad018e504`  |
| 497    | No file              | `2fbad018e504`  |
| 491    | No file              | `2fbad018e504`  |
| 485    | No file              | `2fbad018e504`  |
| 478    | No file              | `2fbad018e504`  |
| 472    | No file              | `2fbad018e504`  |
| 466    | No file              | `2fbad018e504`  |
| 457    | No file              | `2fbad018e504`  |
| 452    | No file              | `2fbad018e504`  |
| 449    | No file              | `2fbad018e504`  |
| 435    | No file              | `2fbad018e504`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                          |
| ---------------------------- | -------- | --------------------------------------------- |
| `zodiacsignorderoffset.dbss` | Required | ID-keyed index into this file, see below      |
| `languagedata_en.loc`        | Optional | Zodiac sign names (7)                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The records are back to back, but not in the order of the offset file; use
the offset file to find a record by key.

| Offset  | Type          | Field   | Notes                    |
| ------- | ------------- | ------- | ------------------------ |
| `+0x00` | u32           | count   | Number of records (= 24) |
| `+0x04` | Record[count] | records | See Record               |

### Record (variable: 13 bytes + trigger_order)

23 to 29 bytes on client 3473 (5 to 8 stars); the offset row's `data_size`
leaves out the leading `personality_type`.

| Offset               | Type               | Field                | Notes                                      |
| -------------------- | ------------------ | -------------------- | ------------------------------------------ |
| `+0x00`              | u16                | personality_type     | `major × 100 + variant`; range 101 to 1202 |
| `+0x02`              | u32                | trigger_count        | Number of `trigger_order` values           |
| `+0x06`              | u32                | unknown_06           | Always 0                                   |
| `+0x0A`              | u16[trigger_count] | trigger_order        | 0-indexed star slots, in lighting order    |
| `trigger_order+0x00` | u8                 | zodiac_id            | Which zodiac sign (1 to 12)                |
| `trigger_order+0x01` | u16                | personality_type_dup | Duplicate of `personality_type` at `+0x00` |

The first star is stored like the others. It is not always slot 0: on
client 3464, 7 of the 24 records start elsewhere (902, 102, 1002, 202, 302,
1202, 502).

`slots` = `zodiacsign.float_count` for that `zodiac_id`.

### `zodiacsignorderoffset.dbss`

| Offset  | Type                 | Field | Notes                         |
| ------- | -------------------- | ----- | ----------------------------- |
| `+0x00` | u32                  | count | Number of rows (= 24)         |
| `+0x04` | Offset Record[count] | rows  | See Offset Record             |

### Offset Record (10 bytes)

| Offset  | Type | Field            | Notes                                                              |
| ------- | ---- | ---------------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | personality_type | Matches `personality_type` in the main record                      |
| `+0x02` | u32  | data_offset      | Byte offset into `zodiacsignorder.dbss`; 2 bytes past record start |
| `+0x06` | u16  | data_size        | Size of record data (excluding leading `personality_type` u16)     |
| `+0x08` | u16  | unknown_08       | Always 0                                                           |

`record_start = data_offset - 2`

## Notes

- Variant 2 is a second drawing order for the same stars. It can reverse variant 1 (1001 is `0,1,2,3,4`, 1002 is `4,3,2,1,0`) or reorder it (902 is `2,1,0,3,2,1`).
- Major 9 (Key): only `personality_type` 901 exists in `npcpersonality.dbss`, but `zodiacsignorder.dbss` defines both 901 and 902.
