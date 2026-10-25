# `servnatmarkettax.dbss` Format

## Purpose

The Horse Market silver bonus per Training level: one row per level from
`1` with the extra share of silver a player collects from the Horse and
Breeding Markets. The character window shows it in the Training tooltip
("+{rate3}% Silver collection when using the Horse or Breeding Markets"),
the stable market in its discount tooltip. The file name is a misspelling
of "servant market tax". Companion `servnatmarkettaxoffset.dbss` lists
where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes | Records        | Row bytes |
| ------ | -------------- | ----------------------------- | ----- | -------------- | --------- |
| 1      | 1346 and later | `servnatmarkettax.dbss`       | 1,444 | 180 Row        | 8         |
| 1      | 1346 and later | `servnatmarkettaxoffset.dbss` | 2,164 | 180 Offset Row | 12        |

| Layout | File                          | Known            | Unknown    |
| ------ | ----------------------------- | ---------------- | ---------- |
| 1      | `servnatmarkettax.dbss`       | 1,444 B (100.0%) | 0 B (0.0%) |
| 1      | `servnatmarkettaxoffset.dbss` | 2,164 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `ad4502dbc019`  |
| 3482   | Layout 1             | `ad4502dbc019`  |
| 3474   | Layout 1             | `ad4502dbc019`  |
| 3473   | Layout 1             | `ad4502dbc019`  |
| 3464   | Layout 1             | `ad4502dbc019`  |
| 3458   | Layout 1             | `ad4502dbc019`  |
| 3454   | Layout 1             | `ad4502dbc019`  |
| 3444   | Layout 1             | `ad4502dbc019`  |
| 3435   | Layout 1             | `ad4502dbc019`  |
| 3426   | Layout 1             | `ad4502dbc019`  |
| 3418   | Layout 1             | `ad4502dbc019`  |
| 3412   | Layout 1             | `ad4502dbc019`  |
| 3402   | Layout 1             | `ad4502dbc019`  |
| 3396   | Layout 1             | `ad4502dbc019`  |
| 3387   | Layout 1             | `ad4502dbc019`  |
| 3381   | Layout 1             | `ad4502dbc019`  |
| 3373   | Layout 1             | `ad4502dbc019`  |
| 3364   | Layout 1             | `ad4502dbc019`  |
| 3356   | Layout 1             | `ad4502dbc019`  |
| 3349   | Layout 1             | `ad4502dbc019`  |
| 3342   | Layout 1             | `ad4502dbc019`  |
| 3335   | Layout 1             | `ad4502dbc019`  |
| 3326   | Layout 1             | `ad4502dbc019`  |
| 3321   | Layout 1             | `ad4502dbc019`  |
| 3314   | Layout 1             | `ad4502dbc019`  |
| 3303   | Layout 1             | `ad4502dbc019`  |
| 3302   | Layout 1             | `ad4502dbc019`  |
| 3293   | Layout 1             | `ad4502dbc019`  |
| 3283   | Layout 1             | `ad4502dbc019`  |
| 3275   | Layout 1             | `ad4502dbc019`  |
| 3267   | Layout 1             | `ad4502dbc019`  |
| 3258   | Layout 1             | `ad4502dbc019`  |
| 3251   | Layout 1             | `ad4502dbc019`  |
| 3242   | Layout 1             | `ad4502dbc019`  |
| 3235   | Layout 1             | `ad4502dbc019`  |
| 3229   | Layout 1             | `ad4502dbc019`  |
| 3212   | Layout 1             | `ad4502dbc019`  |
| 3203   | Layout 1             | `ad4502dbc019`  |
| 3193   | Layout 1             | `ad4502dbc019`  |
| 3186   | Layout 1             | `ad4502dbc019`  |
| 3177   | Layout 1             | `ad4502dbc019`  |
| 3169   | Layout 1             | `ad4502dbc019`  |
| 3158   | Layout 1             | `ad4502dbc019`  |
| 3151   | Layout 1             | `ad4502dbc019`  |
| 3144   | Layout 1             | `ad4502dbc019`  |
| 3133   | Layout 1             | `ad4502dbc019`  |
| 3125   | Layout 1             | `ad4502dbc019`  |
| 3118   | Layout 1             | `ad4502dbc019`  |
| 3111   | Layout 1             | `ad4502dbc019`  |
| 3103   | Layout 1             | `ad4502dbc019`  |
| 3095   | Layout 1             | `ad4502dbc019`  |
| 3086   | Layout 1             | `ad4502dbc019`  |
| 3072   | Layout 1             | `ad4502dbc019`  |
| 3062   | Layout 1             | `ad4502dbc019`  |
| 3052   | Layout 1             | `ad4502dbc019`  |
| 3045   | Layout 1             | `ad4502dbc019`  |
| 3037   | Layout 1             | `ad4502dbc019`  |
| 3030   | Layout 1             | `ad4502dbc019`  |
| 3021   | Layout 1             | `ad4502dbc019`  |
| 3012   | Layout 1             | `ad4502dbc019`  |
| 3002   | Layout 1             | `ad4502dbc019`  |
| 2995   | Layout 1             | `ad4502dbc019`  |
| 2987   | Layout 1             | `ad4502dbc019`  |
| 2978   | Layout 1             | `ad4502dbc019`  |
| 2970   | Layout 1             | `ad4502dbc019`  |
| 2959   | Layout 1             | `ad4502dbc019`  |
| 2951   | Layout 1             | `ad4502dbc019`  |
| 2942   | Layout 1             | `ad4502dbc019`  |
| 2935   | Layout 1             | `ad4502dbc019`  |
| 2932   | Layout 1             | `ad4502dbc019`  |
| 2923   | Layout 1             | `ad4502dbc019`  |
| 2919   | Layout 1             | `ad4502dbc019`  |
| 2907   | Layout 1             | `ad4502dbc019`  |
| 2900   | Layout 1             | `ad4502dbc019`  |
| 2891   | Layout 1             | `ad4502dbc019`  |
| 2882   | Layout 1             | `ad4502dbc019`  |
| 2872   | Layout 1             | `ad4502dbc019`  |
| 2863   | Layout 1             | `ad4502dbc019`  |
| 2855   | Layout 1             | `ad4502dbc019`  |
| 2849   | Layout 1             | `ad4502dbc019`  |
| 2844   | Layout 1             | `ad4502dbc019`  |
| 2834   | Layout 1             | `ad4502dbc019`  |
| 2825   | Layout 1             | `ad4502dbc019`  |
| 2819   | Layout 1             | `ad4502dbc019`  |
| 2811   | Layout 1             | `ad4502dbc019`  |
| 2803   | Layout 1             | `ad4502dbc019`  |
| 2794   | Layout 1             | `ad4502dbc019`  |
| 2783   | Layout 1             | `ad4502dbc019`  |
| 2774   | Layout 1             | `ad4502dbc019`  |
| 2765   | Layout 1             | `ad4502dbc019`  |
| 2756   | Layout 1             | `ad4502dbc019`  |
| 2750   | Layout 1             | `ad4502dbc019`  |
| 2743   | Layout 1             | `ad4502dbc019`  |
| 2736   | Layout 1             | `ad4502dbc019`  |
| 2726   | Layout 1             | `ad4502dbc019`  |
| 2717   | Layout 1             | `ad4502dbc019`  |
| 2709   | Layout 1             | `ad4502dbc019`  |
| 2703   | Layout 1             | `ad4502dbc019`  |
| 2695   | Layout 1             | `ad4502dbc019`  |
| 2684   | Layout 1             | `ad4502dbc019`  |
| 2672   | Layout 1             | `ad4502dbc019`  |
| 2665   | Layout 1             | `ad4502dbc019`  |
| 2657   | Layout 1             | `ad4502dbc019`  |
| 2649   | Layout 1             | `ad4502dbc019`  |
| 2644   | Layout 1             | `ad4502dbc019`  |
| 2637   | Layout 1             | `ad4502dbc019`  |
| 2629   | Layout 1             | `ad4502dbc019`  |
| 2619   | Layout 1             | `ad4502dbc019`  |
| 2612   | Layout 1             | `ad4502dbc019`  |
| 2606   | Layout 1             | `ad4502dbc019`  |
| 2602   | Layout 1             | `ad4502dbc019`  |
| 2601   | Layout 1             | `ad4502dbc019`  |
| 2592   | Layout 1             | `ad4502dbc019`  |
| 2583   | Layout 1             | `ad4502dbc019`  |
| 2575   | Layout 1             | `ad4502dbc019`  |
| 2567   | Layout 1             | `ad4502dbc019`  |
| 2560   | Layout 1             | `ad4502dbc019`  |
| 2553   | Layout 1             | `ad4502dbc019`  |
| 2545   | Layout 1             | `ad4502dbc019`  |
| 2538   | Layout 1             | `ad4502dbc019`  |
| 2529   | Layout 1             | `ad4502dbc019`  |
| 2519   | Layout 1             | `ad4502dbc019`  |
| 2513   | Layout 1             | `ad4502dbc019`  |
| 2510   | Layout 1             | `ad4502dbc019`  |
| 2507   | Layout 1             | `ad4502dbc019`  |
| 2503   | Layout 1             | `ad4502dbc019`  |
| 2498   | Layout 1             | `ad4502dbc019`  |
| 2492   | Layout 1             | `ad4502dbc019`  |
| 2487   | Layout 1             | `ad4502dbc019`  |
| 2480   | Layout 1             | `ad4502dbc019`  |
| 2474   | Layout 1             | `ad4502dbc019`  |
| 2468   | Layout 1             | `ad4502dbc019`  |
| 2460   | Layout 1             | `ad4502dbc019`  |
| 2453   | Layout 1             | `ad4502dbc019`  |
| 2444   | Layout 1             | `ad4502dbc019`  |
| 2438   | Layout 1             | `ad4502dbc019`  |
| 2434   | Layout 1             | `ad4502dbc019`  |
| 2429   | Layout 1             | `ad4502dbc019`  |
| 2421   | Layout 1             | `ad4502dbc019`  |
| 2414   | Layout 1             | `ad4502dbc019`  |
| 2407   | Layout 1             | `ad4502dbc019`  |
| 2401   | Layout 1             | `ad4502dbc019`  |
| 2397   | Layout 1             | `ad4502dbc019`  |
| 2393   | Layout 1             | `ad4502dbc019`  |
| 2384   | Layout 1             | `ad4502dbc019`  |
| 2378   | Layout 1             | `ad4502dbc019`  |
| 2372   | Layout 1             | `ad4502dbc019`  |
| 2358   | Layout 1             | `ad4502dbc019`  |
| 2352   | Layout 1             | `ad4502dbc019`  |
| 2347   | Layout 1             | `ad4502dbc019`  |
| 2343   | Layout 1             | `ad4502dbc019`  |
| 2335   | Layout 1             | `ad4502dbc019`  |
| 2327   | Layout 1             | `ad4502dbc019`  |
| 2324   | Layout 1             | `ad4502dbc019`  |
| 2319   | Layout 1             | `ad4502dbc019`  |
| 2313   | Layout 1             | `ad4502dbc019`  |
| 2308   | Layout 1             | `ad4502dbc019`  |
| 2302   | Layout 1             | `ad4502dbc019`  |
| 2295   | Layout 1             | `ad4502dbc019`  |
| 2290   | Layout 1             | `ad4502dbc019`  |
| 2284   | Layout 1             | `ad4502dbc019`  |
| 2276   | Layout 1             | `ad4502dbc019`  |
| 2269   | Layout 1             | `ad4502dbc019`  |
| 2259   | Layout 1             | `ad4502dbc019`  |
| 2250   | Layout 1             | `ad4502dbc019`  |
| 2243   | Layout 1             | `ad4502dbc019`  |
| 2235   | Layout 1             | `ad4502dbc019`  |
| 2229   | Layout 1             | `ad4502dbc019`  |
| 2224   | Layout 1             | `ad4502dbc019`  |
| 2218   | Layout 1             | `ad4502dbc019`  |
| 2215   | Layout 1             | `ad4502dbc019`  |
| 2207   | Layout 1             | `ad4502dbc019`  |
| 2203   | Layout 1             | `ad4502dbc019`  |
| 2196   | Layout 1             | `ad4502dbc019`  |
| 2192   | Layout 1             | `ad4502dbc019`  |
| 2189   | Layout 1             | `ad4502dbc019`  |
| 2183   | Layout 1             | `ad4502dbc019`  |
| 2179   | Layout 1             | `ad4502dbc019`  |
| 2171   | Layout 1             | `ad4502dbc019`  |
| 2163   | Layout 1             | `ad4502dbc019`  |
| 2156   | Layout 1             | `ad4502dbc019`  |
| 2151   | Layout 1             | `ad4502dbc019`  |
| 2147   | Layout 1             | `ad4502dbc019`  |
| 2142   | Layout 1             | `ad4502dbc019`  |
| 2138   | Layout 1             | `ad4502dbc019`  |
| 2134   | Layout 1             | `ad4502dbc019`  |
| 2130   | Layout 1             | `ad4502dbc019`  |
| 2122   | Layout 1             | `ad4502dbc019`  |
| 2107   | Layout 1             | `ad4502dbc019`  |
| 2098   | Layout 1             | `ad4502dbc019`  |
| 2089   | Layout 1             | `ad4502dbc019`  |
| 2081   | Layout 1             | `ad4502dbc019`  |
| 2073   | Layout 1             | `ad4502dbc019`  |
| 2067   | Layout 1             | `ad4502dbc019`  |
| 2063   | Layout 1             | `ad4502dbc019`  |
| 2059   | Layout 1             | `ad4502dbc019`  |
| 2052   | Layout 1             | `ad4502dbc019`  |
| 2044   | Layout 1             | `ad4502dbc019`  |
| 2039   | Layout 1             | `ad4502dbc019`  |
| 2032   | Layout 1             | `ad4502dbc019`  |
| 2025   | Layout 1             | `ad4502dbc019`  |
| 2011   | Layout 1             | `ad4502dbc019`  |
| 2005   | Layout 1             | `ad4502dbc019`  |
| 2000   | Layout 1             | `ad4502dbc019`  |
| 1996   | Layout 1             | `ad4502dbc019`  |
| 1991   | Layout 1             | `ad4502dbc019`  |
| 1985   | Layout 1             | `ad4502dbc019`  |
| 1980   | Layout 1             | `ad4502dbc019`  |
| 1969   | Layout 1             | `ad4502dbc019`  |
| 1964   | Layout 1             | `ad4502dbc019`  |
| 1958   | Layout 1             | `ad4502dbc019`  |
| 1950   | Layout 1             | `ad4502dbc019`  |
| 1945   | Layout 1             | `ad4502dbc019`  |
| 1937   | Layout 1             | `ad4502dbc019`  |
| 1933   | Layout 1             | `ad4502dbc019`  |
| 1927   | Layout 1             | `ad4502dbc019`  |
| 1921   | Layout 1             | `ad4502dbc019`  |
| 1914   | Layout 1             | `ad4502dbc019`  |
| 1908   | Layout 1             | `ad4502dbc019`  |
| 1897   | Layout 1             | `ad4502dbc019`  |
| 1892   | Layout 1             | `ad4502dbc019`  |
| 1886   | Layout 1             | `ad4502dbc019`  |
| 1881   | Layout 1             | `ad4502dbc019`  |
| 1871   | Layout 1             | `ad4502dbc019`  |
| 1866   | Layout 1             | `ad4502dbc019`  |
| 1862   | Layout 1             | `ad4502dbc019`  |
| 1854   | Layout 1             | `ad4502dbc019`  |
| 1846   | Layout 1             | `ad4502dbc019`  |
| 1838   | Layout 1             | `ad4502dbc019`  |
| 1832   | Layout 1             | `ad4502dbc019`  |
| 1826   | Layout 1             | `ad4502dbc019`  |
| 1822   | Layout 1             | `ad4502dbc019`  |
| 1818   | Layout 1             | `ad4502dbc019`  |
| 1804   | Layout 1             | `ad4502dbc019`  |
| 1794   | Layout 1             | `ad4502dbc019`  |
| 1790   | Layout 1             | `ad4502dbc019`  |
| 1784   | Layout 1             | `ad4502dbc019`  |
| 1774   | Layout 1             | `ad4502dbc019`  |
| 1771   | Layout 1             | `ad4502dbc019`  |
| 1762   | Layout 1             | `ad4502dbc019`  |
| 1759   | Layout 1             | `ad4502dbc019`  |
| 1754   | Layout 1             | `ad4502dbc019`  |
| 1749   | Layout 1             | `ad4502dbc019`  |
| 1743   | Layout 1             | `ad4502dbc019`  |
| 1737   | Layout 1             | `ad4502dbc019`  |
| 1731   | Layout 1             | `ad4502dbc019`  |
| 1725   | Layout 1             | `ad4502dbc019`  |
| 1717   | Layout 1             | `ad4502dbc019`  |
| 1710   | Layout 1             | `ad4502dbc019`  |
| 1704   | Layout 1             | `ad4502dbc019`  |
| 1698   | Layout 1             | `ad4502dbc019`  |
| 1690   | Layout 1             | `ad4502dbc019`  |
| 1685   | Layout 1             | `ad4502dbc019`  |
| 1680   | Layout 1             | `ad4502dbc019`  |
| 1674   | Layout 1             | `ad4502dbc019`  |
| 1668   | Layout 1             | `ad4502dbc019`  |
| 1659   | Layout 1             | `ad4502dbc019`  |
| 1649   | Layout 1             | `ad4502dbc019`  |
| 1642   | Layout 1             | `ad4502dbc019`  |
| 1636   | Layout 1             | `ad4502dbc019`  |
| 1628   | Layout 1             | `ad4502dbc019`  |
| 1622   | Layout 1             | `ad4502dbc019`  |
| 1614   | Layout 1             | `ad4502dbc019`  |
| 1608   | Layout 1             | `ad4502dbc019`  |
| 1602   | Layout 1             | `ad4502dbc019`  |
| 1598   | Layout 1             | `ad4502dbc019`  |
| 1594   | Layout 1             | `ad4502dbc019`  |
| 1590   | Layout 1             | `ad4502dbc019`  |
| 1587   | Layout 1             | `ad4502dbc019`  |
| 1584   | Layout 1             | `ad4502dbc019`  |
| 1579   | Layout 1             | `ad4502dbc019`  |
| 1572   | Layout 1             | `ad4502dbc019`  |
| 1565   | Layout 1             | `ad4502dbc019`  |
| 1559   | Layout 1             | `ad4502dbc019`  |
| 1554   | Layout 1             | `ad4502dbc019`  |
| 1547   | Layout 1             | `ad4502dbc019`  |
| 1537   | Layout 1             | `ad4502dbc019`  |
| 1529   | Layout 1             | `ad4502dbc019`  |
| 1524   | Layout 1             | `ad4502dbc019`  |
| 1519   | Layout 1             | `ad4502dbc019`  |
| 1509   | Layout 1             | `ad4502dbc019`  |
| 1506   | Layout 1             | `ad4502dbc019`  |
| 1504   | Layout 1             | `ad4502dbc019`  |
| 1500   | Layout 1             | `ad4502dbc019`  |
| 1493   | Layout 1             | `ad4502dbc019`  |
| 1489   | Layout 1             | `ad4502dbc019`  |
| 1485   | Layout 1             | `ad4502dbc019`  |
| 1481   | Layout 1             | `ad4502dbc019`  |
| 1474   | Layout 1             | `ad4502dbc019`  |
| 1466   | Layout 1             | `ad4502dbc019`  |
| 1462   | Layout 1             | `ad4502dbc019`  |
| 1459   | Layout 1             | `ad4502dbc019`  |
| 1453   | Layout 1             | `ad4502dbc019`  |
| 1450   | Layout 1             | `ad4502dbc019`  |
| 1445   | Layout 1             | `ad4502dbc019`  |
| 1439   | Layout 1             | `ad4502dbc019`  |
| 1433   | Layout 1             | `ad4502dbc019`  |
| 1430   | Layout 1             | `ad4502dbc019`  |
| 1426   | Layout 1             | `ad4502dbc019`  |
| 1421   | Layout 1             | `ad4502dbc019`  |
| 1417   | Layout 1             | `ad4502dbc019`  |
| 1416   | Layout 1             | `ad4502dbc019`  |
| 1409   | Layout 1             | `ad4502dbc019`  |
| 1405   | Layout 1             | `ad4502dbc019`  |
| 1401   | Layout 1             | `ad4502dbc019`  |
| 1396   | Layout 1             | `ad4502dbc019`  |
| 1391   | Layout 1             | `ad4502dbc019`  |
| 1390   | Layout 1             | `ad4502dbc019`  |
| 1386   | Layout 1             | `ad4502dbc019`  |
| 1381   | Layout 1             | `ad4502dbc019`  |
| 1379   | Layout 1             | `ad4502dbc019`  |
| 1372   | Layout 1             | `ad4502dbc019`  |
| 1366   | Layout 1             | `ad4502dbc019`  |
| 1364   | Layout 1             | `ad4502dbc019`  |
| 1363   | Layout 1             | `ad4502dbc019`  |
| 1360   | Layout 1             | `ad4502dbc019`  |
| 1358   | Layout 1             | `ad4502dbc019`  |
| 1355   | Layout 1             | `ad4502dbc019`  |
| 1351   | Layout 1             | `ad4502dbc019`  |
| 1348   | Layout 1             | `ad4502dbc019`  |
| 1346   | Layout 1             | `ad4502dbc019`  |
| 1341   | No documented layout | `ad4502dbc019`  |
| 1340   | No documented layout | `ad4502dbc019`  |
| 1338   | No documented layout | `ad4502dbc019`  |
| 1335   | No documented layout | `ad4502dbc019`  |
| 1333   | No documented layout | `ad4502dbc019`  |
| 1329   | No documented layout | `ad4502dbc019`  |
| 1327   | No documented layout | `ad4502dbc019`  |
| 1324   | No documented layout | `ad4502dbc019`  |
| 1321   | No documented layout | `ad4502dbc019`  |
| 1319   | No documented layout | `ad4502dbc019`  |
| 1318   | No documented layout | `ad4502dbc019`  |
| 1316   | No documented layout | `ad4502dbc019`  |
| 1313   | No documented layout | `ad4502dbc019`  |
| 1311   | No documented layout | `ad4502dbc019`  |
| 1309   | No documented layout | `ad4502dbc019`  |
| 1304   | No documented layout | `ad4502dbc019`  |
| 1292   | No documented layout | `ad4502dbc019`  |
| 1286   | No documented layout | `ad4502dbc019`  |
| 1280   | No documented layout | `ad4502dbc019`  |
| 1276   | No documented layout | `ad4502dbc019`  |
| 1267   | No file              | `ad4502dbc019`  |
| 1261   | No file              | `ad4502dbc019`  |
| 1256   | No documented layout | `ad4502dbc019`  |
| 1250   | No file              | `ad4502dbc019`  |
| 1246   | No file              | `ad4502dbc019`  |
| 1239   | No file              | `ad4502dbc019`  |
| 1230   | No file              | `ad4502dbc019`  |
| 1226   | No file              | `ad4502dbc019`  |
| 1220   | No file              | `ad4502dbc019`  |
| 1217   | No file              | `ad4502dbc019`  |
| 1211   | No file              | `ad4502dbc019`  |
| 1210   | No file              | `ad4502dbc019`  |
| 1208   | No file              | `ad4502dbc019`  |
| 1203   | No file              | `ad4502dbc019`  |
| 1197   | No file              | `ad4502dbc019`  |
| 1194   | No file              | `ad4502dbc019`  |
| 1192   | No file              | `ad4502dbc019`  |
| 1187   | No file              | `ad4502dbc019`  |
| 1183   | No file              | `ad4502dbc019`  |
| 1177   | No file              | `ad4502dbc019`  |
| 1173   | No file              | `ad4502dbc019`  |
| 1167   | No file              | `ad4502dbc019`  |
| 1164   | No file              | `ad4502dbc019`  |
| 1156   | No file              | `ad4502dbc019`  |
| 1149   | No file              | `ad4502dbc019`  |
| 1144   | No file              | `ad4502dbc019`  |
| 1137   | No file              | `ad4502dbc019`  |
| 1132   | No file              | `ad4502dbc019`  |
| 1127   | No file              | `ad4502dbc019`  |
| 1122   | No file              | `ad4502dbc019`  |
| 1118   | No file              | `ad4502dbc019`  |
| 1114   | No file              | `ad4502dbc019`  |
| 1109   | No file              | `ad4502dbc019`  |
| 1102   | No file              | `ad4502dbc019`  |
| 1096   | No file              | `ad4502dbc019`  |
| 1088   | No file              | `ad4502dbc019`  |
| 1081   | No file              | `ad4502dbc019`  |
| 1076   | No file              | `ad4502dbc019`  |
| 1069   | No file              | `ad4502dbc019`  |
| 1064   | No file              | `ad4502dbc019`  |
| 1058   | No file              | `ad4502dbc019`  |
| 1051   | No file              | `ad4502dbc019`  |
| 1044   | No file              | `ad4502dbc019`  |
| 1036   | No file              | `ad4502dbc019`  |
| 1026   | No file              | `ad4502dbc019`  |
| 1016   | No file              | `ad4502dbc019`  |
| 1009   | No file              | `ad4502dbc019`  |
| 1005   | No file              | `ad4502dbc019`  |
| 1000   | No file              | `ad4502dbc019`  |
| 998    | No file              | `ad4502dbc019`  |
| 990    | No file              | `ad4502dbc019`  |
| 979    | No file              | `ad4502dbc019`  |
| 972    | No file              | `ad4502dbc019`  |
| 963    | No file              | `ad4502dbc019`  |
| 955    | No file              | `ad4502dbc019`  |
| 946    | No file              | `ad4502dbc019`  |
| 938    | No file              | `ad4502dbc019`  |
| 927    | No file              | `ad4502dbc019`  |
| 911    | No file              | `ad4502dbc019`  |
| 904    | No file              | `ad4502dbc019`  |
| 899    | No file              | `ad4502dbc019`  |
| 894    | No file              | `ad4502dbc019`  |
| 885    | No file              | `ad4502dbc019`  |
| 879    | No file              | `ad4502dbc019`  |
| 872    | No file              | `ad4502dbc019`  |
| 864    | No file              | `ad4502dbc019`  |
| 855    | No file              | `ad4502dbc019`  |
| 853    | No file              | `ad4502dbc019`  |
| 845    | No file              | `ad4502dbc019`  |
| 837    | No file              | `ad4502dbc019`  |
| 829    | No file              | `ad4502dbc019`  |
| 822    | No file              | `ad4502dbc019`  |
| 814    | No file              | `ad4502dbc019`  |
| 805    | No file              | `ad4502dbc019`  |
| 794    | No file              | `ad4502dbc019`  |
| 787    | No file              | `ad4502dbc019`  |
| 780    | No file              | `ad4502dbc019`  |
| 771    | No file              | `ad4502dbc019`  |
| 760    | No file              | `ad4502dbc019`  |
| 748    | No file              | `ad4502dbc019`  |
| 741    | No file              | `ad4502dbc019`  |
| 736    | No file              | `ad4502dbc019`  |
| 731    | No file              | `ad4502dbc019`  |
| 723    | No file              | `ad4502dbc019`  |
| 711    | No file              | `ad4502dbc019`  |
| 707    | No file              | `ad4502dbc019`  |
| 697    | No file              | `ad4502dbc019`  |
| 689    | No file              | `ad4502dbc019`  |
| 683    | No file              | `ad4502dbc019`  |
| 678    | No file              | `ad4502dbc019`  |
| 670    | No file              | `ad4502dbc019`  |
| 661    | No file              | `ad4502dbc019`  |
| 656    | No file              | `ad4502dbc019`  |
| 652    | No file              | `ad4502dbc019`  |
| 643    | No file              | `ad4502dbc019`  |
| 637    | No file              | `ad4502dbc019`  |
| 630    | No file              | `ad4502dbc019`  |
| 627    | No file              | `ad4502dbc019`  |
| 621    | No file              | `ad4502dbc019`  |
| 617    | No file              | `ad4502dbc019`  |
| 615    | No file              | `ad4502dbc019`  |
| 606    | No file              | `ad4502dbc019`  |
| 599    | No file              | `ad4502dbc019`  |
| 592    | No file              | `ad4502dbc019`  |
| 586    | No file              | `ad4502dbc019`  |
| 577    | No file              | `ad4502dbc019`  |
| 569    | No file              | `ad4502dbc019`  |
| 561    | No file              | `ad4502dbc019`  |
| 554    | No file              | `ad4502dbc019`  |
| 542    | No file              | `ad4502dbc019`  |
| 532    | No file              | `ad4502dbc019`  |
| 531    | No file              | `ad4502dbc019`  |
| 526    | No file              | `ad4502dbc019`  |
| 521    | No file              | `ad4502dbc019`  |
| 517    | No file              | `ad4502dbc019`  |
| 510    | No file              | `ad4502dbc019`  |
| 508    | No file              | `ad4502dbc019`  |
| 504    | No file              | `ad4502dbc019`  |
| 497    | No file              | `ad4502dbc019`  |
| 491    | No file              | `ad4502dbc019`  |
| 485    | No file              | `ad4502dbc019`  |
| 478    | No file              | `ad4502dbc019`  |
| 472    | No file              | `ad4502dbc019`  |
| 466    | No file              | `ad4502dbc019`  |
| 457    | No file              | `ad4502dbc019`  |
| 452    | No file              | `ad4502dbc019`  |
| 449    | No file              | `ad4502dbc019`  |
| 435    | No file              | `ad4502dbc019`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                  |
| ----------------------------- | -------- | --------------------------------------------------------------------- |
| `servnatmarkettaxoffset.dbss` | Optional | `life_level -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`         | Optional | The rank names (Beginner to Guru) for the Rank column, LOC type `37`   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 180 x 8 = 1,444 bytes.

### Row (8 bytes)

| Offset  | Type | Field                    | Notes                                                                  |
| ------- | ---- | ------------------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32  | life_level               | Training level, the row key; `1` to `count` in order                    |
| `+0x04` | u32  | horse_market_tax_percent | Silver bonus in units of 0.0001%: `10000` is 1%; see Notes              |

### `servnatmarkettaxoffset.dbss`

Bare offset table into `servnatmarkettax.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                    |
| ------- | ----------------- | ----- | ---------------------------------------- |
| `+0x00` | u32               | count | Equals the `servnatmarkettax.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                           |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | life_level  | Key of the row it points at                              |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `servnatmarkettax.dbss`, at `life_level` |
| `+0x08` | u32  | data_size   | `8` on every row: the whole row                          |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in level order, as the file; on clients 1784 and 3474 every
index row points at the row with its key.

## Field Names

The `ServantMarketTax_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `LifeLevel` and `HorseMarketTaxPercent`. Its
note column `#조련 레벨` (Training level) labels each row with the rank
(`초급 Lv.1`, Beginner 1). The 2016 client's debug symbols have no struct
for the table.

| Field                    | Column                  | Same value (client 1784) | Same value (client 3474) |
| ------------------------ | ----------------------- | ------------------------ | ------------------------ |
| life_level               | `LifeLevel`             | 130 of 130               | 130 of 180               |
| horse_market_tax_percent | `HorseMarketTaxPercent` | 130 of 130               | 130 of 130               |

Client 3474 adds levels 131 to 180 and keeps the values of levels 1 to 130.

## Notes

- Two Lua files read the value for the player's own Training level through
  `ToClient_GetServantMarketTaxPercent()` and divide it by `10000`:
  `panel_characterinfo_basic_all_2.luac` fills `{rate3}` of
  `LUA_CHARACTERINFO_LIFE_TRAINING_DESC_2` with one decimal, and
  `panel_dialog_servantmarket_all_2.luac` fills `{rate}` of
  `LUA_STABLEMARKET_DISCOUNT_BTN_TOOLTIP_DESC` ("Current: +{rate}%") under
  `PANEL_STABLEMARKET_DISCOUNT_TOOLTIP_NAME` ("Rates per Training Grade").
- On client 3474 the bonus is `0` for levels 1 to 10 (Beginner), `10000`
  (1%) at level 11 and `300000` (30%) from level 81 (Guru 1) to 180.
- The levels are Training levels: the sheet's note column and the
  character window's Training tooltip both name them so. The ranks follow
  `PaGlobalFunc_Util_CraftLevelReplace` (see
  [`barterlifelevelinfo.bss`](barterlifelevelinfo_bss.md), same row shape).
