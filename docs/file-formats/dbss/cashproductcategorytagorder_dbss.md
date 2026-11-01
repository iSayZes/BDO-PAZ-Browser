# `cashproductcategorytagorder.dbss` Format

## Purpose

A sort rank per Pearl Shop product tag: one i32 per tag, the row position
being the tag number a product returns from `cashProduct:getTag()` in the
Pearl Shop Lua (`panel_ingamecashshop`). The ranks run from `1` up, and
`-1` marks a tag with no rank. The file is a plain PABR table after
decoding and has no offset companion. On client 3483 it holds 18 tags,
`0` to `17`; client 1784 holds 8.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                               | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------------------------- | ----- | ------- | --------- |
| 1      | 1286 and later | `cashproductcategorytagorder.dbss` | 92    | 18 Row  | 4         |

| Layout | File                               | Known         | Unknown    |
| ------ | ---------------------------------- | ------------- | ---------- |
| 1      | `cashproductcategorytagorder.dbss` | 92 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a5198219ff18`  |
| 3482   | Layout 1 | `a5198219ff18`  |
| 3474   | Layout 1 | `a5198219ff18`  |
| 3473   | Layout 1 | `a5198219ff18`  |
| 3464   | Layout 1 | `a5198219ff18`  |
| 3458   | Layout 1 | `a5198219ff18`  |
| 3454   | Layout 1 | `a5198219ff18`  |
| 3444   | Layout 1 | `a5198219ff18`  |
| 3435   | Layout 1 | `a5198219ff18`  |
| 3426   | Layout 1 | `a5198219ff18`  |
| 3418   | Layout 1 | `a5198219ff18`  |
| 3412   | Layout 1 | `a5198219ff18`  |
| 3402   | Layout 1 | `a5198219ff18`  |
| 3396   | Layout 1 | `a5198219ff18`  |
| 3387   | Layout 1 | `a5198219ff18`  |
| 3381   | Layout 1 | `a5198219ff18`  |
| 3373   | Layout 1 | `a5198219ff18`  |
| 3364   | Layout 1 | `a5198219ff18`  |
| 3356   | Layout 1 | `a5198219ff18`  |
| 3349   | Layout 1 | `a5198219ff18`  |
| 3342   | Layout 1 | `a5198219ff18`  |
| 3335   | Layout 1 | `a5198219ff18`  |
| 3326   | Layout 1 | `a5198219ff18`  |
| 3321   | Layout 1 | `a5198219ff18`  |
| 3314   | Layout 1 | `a5198219ff18`  |
| 3303   | Layout 1 | `a5198219ff18`  |
| 3302   | Layout 1 | `a5198219ff18`  |
| 3293   | Layout 1 | `a5198219ff18`  |
| 3283   | Layout 1 | `a5198219ff18`  |
| 3275   | Layout 1 | `a5198219ff18`  |
| 3267   | Layout 1 | `a5198219ff18`  |
| 3258   | Layout 1 | `a5198219ff18`  |
| 3251   | Layout 1 | `a5198219ff18`  |
| 3242   | Layout 1 | `a5198219ff18`  |
| 3235   | Layout 1 | `a5198219ff18`  |
| 3229   | Layout 1 | `a5198219ff18`  |
| 3212   | Layout 1 | `a5198219ff18`  |
| 3203   | Layout 1 | `a5198219ff18`  |
| 3193   | Layout 1 | `a5198219ff18`  |
| 3186   | Layout 1 | `a5198219ff18`  |
| 3177   | Layout 1 | `a5198219ff18`  |
| 3169   | Layout 1 | `a5198219ff18`  |
| 3158   | Layout 1 | `a5198219ff18`  |
| 3151   | Layout 1 | `a5198219ff18`  |
| 3144   | Layout 1 | `a5198219ff18`  |
| 3133   | Layout 1 | `a5198219ff18`  |
| 3125   | Layout 1 | `a5198219ff18`  |
| 3118   | Layout 1 | `a5198219ff18`  |
| 3111   | Layout 1 | `a5198219ff18`  |
| 3103   | Layout 1 | `a5198219ff18`  |
| 3095   | Layout 1 | `a5198219ff18`  |
| 3086   | Layout 1 | `a5198219ff18`  |
| 3072   | Layout 1 | `a5198219ff18`  |
| 3062   | Layout 1 | `a5198219ff18`  |
| 3052   | Layout 1 | `a5198219ff18`  |
| 3045   | Layout 1 | `a5198219ff18`  |
| 3037   | Layout 1 | `a5198219ff18`  |
| 3030   | Layout 1 | `a5198219ff18`  |
| 3021   | Layout 1 | `a5198219ff18`  |
| 3012   | Layout 1 | `a5198219ff18`  |
| 3002   | Layout 1 | `a5198219ff18`  |
| 2995   | Layout 1 | `a5198219ff18`  |
| 2987   | Layout 1 | `a5198219ff18`  |
| 2978   | Layout 1 | `a5198219ff18`  |
| 2970   | Layout 1 | `a5198219ff18`  |
| 2959   | Layout 1 | `a5198219ff18`  |
| 2951   | Layout 1 | `a5198219ff18`  |
| 2942   | Layout 1 | `a5198219ff18`  |
| 2935   | Layout 1 | `a5198219ff18`  |
| 2932   | Layout 1 | `a5198219ff18`  |
| 2923   | Layout 1 | `a5198219ff18`  |
| 2919   | Layout 1 | `a5198219ff18`  |
| 2907   | Layout 1 | `a5198219ff18`  |
| 2900   | Layout 1 | `a5198219ff18`  |
| 2891   | Layout 1 | `a5198219ff18`  |
| 2882   | Layout 1 | `a5198219ff18`  |
| 2872   | Layout 1 | `a5198219ff18`  |
| 2863   | Layout 1 | `a5198219ff18`  |
| 2855   | Layout 1 | `a5198219ff18`  |
| 2849   | Layout 1 | `a5198219ff18`  |
| 2844   | Layout 1 | `a5198219ff18`  |
| 2834   | Layout 1 | `a5198219ff18`  |
| 2825   | Layout 1 | `a5198219ff18`  |
| 2819   | Layout 1 | `a5198219ff18`  |
| 2811   | Layout 1 | `a5198219ff18`  |
| 2803   | Layout 1 | `a5198219ff18`  |
| 2794   | Layout 1 | `a5198219ff18`  |
| 2783   | Layout 1 | `a5198219ff18`  |
| 2774   | Layout 1 | `a5198219ff18`  |
| 2765   | Layout 1 | `a5198219ff18`  |
| 2756   | Layout 1 | `a5198219ff18`  |
| 2750   | Layout 1 | `a5198219ff18`  |
| 2743   | Layout 1 | `a5198219ff18`  |
| 2736   | Layout 1 | `a5198219ff18`  |
| 2726   | Layout 1 | `a5198219ff18`  |
| 2717   | Layout 1 | `a5198219ff18`  |
| 2709   | Layout 1 | `a5198219ff18`  |
| 2703   | Layout 1 | `a5198219ff18`  |
| 2695   | Layout 1 | `a5198219ff18`  |
| 2684   | Layout 1 | `a5198219ff18`  |
| 2672   | Layout 1 | `a5198219ff18`  |
| 2665   | Layout 1 | `a5198219ff18`  |
| 2657   | Layout 1 | `a5198219ff18`  |
| 2649   | Layout 1 | `a5198219ff18`  |
| 2644   | Layout 1 | `a5198219ff18`  |
| 2637   | Layout 1 | `a5198219ff18`  |
| 2629   | Layout 1 | `a5198219ff18`  |
| 2619   | Layout 1 | `a5198219ff18`  |
| 2612   | Layout 1 | `a5198219ff18`  |
| 2606   | Layout 1 | `a5198219ff18`  |
| 2602   | Layout 1 | `a5198219ff18`  |
| 2601   | Layout 1 | `a5198219ff18`  |
| 2592   | Layout 1 | `a5198219ff18`  |
| 2583   | Layout 1 | `a5198219ff18`  |
| 2575   | Layout 1 | `a5198219ff18`  |
| 2567   | Layout 1 | `a5198219ff18`  |
| 2560   | Layout 1 | `a5198219ff18`  |
| 2553   | Layout 1 | `a5198219ff18`  |
| 2545   | Layout 1 | `a5198219ff18`  |
| 2538   | Layout 1 | `a5198219ff18`  |
| 2529   | Layout 1 | `a5198219ff18`  |
| 2519   | Layout 1 | `a5198219ff18`  |
| 2513   | Layout 1 | `a5198219ff18`  |
| 2510   | Layout 1 | `a5198219ff18`  |
| 2507   | Layout 1 | `a5198219ff18`  |
| 2503   | Layout 1 | `a5198219ff18`  |
| 2498   | Layout 1 | `a5198219ff18`  |
| 2492   | Layout 1 | `a5198219ff18`  |
| 2487   | Layout 1 | `a5198219ff18`  |
| 2480   | Layout 1 | `a5198219ff18`  |
| 2474   | Layout 1 | `a5198219ff18`  |
| 2468   | Layout 1 | `a5198219ff18`  |
| 2460   | Layout 1 | `a5198219ff18`  |
| 2453   | Layout 1 | `a5198219ff18`  |
| 2444   | Layout 1 | `a5198219ff18`  |
| 2438   | Layout 1 | `a5198219ff18`  |
| 2434   | Layout 1 | `a5198219ff18`  |
| 2429   | Layout 1 | `a5198219ff18`  |
| 2421   | Layout 1 | `a5198219ff18`  |
| 2414   | Layout 1 | `a5198219ff18`  |
| 2407   | Layout 1 | `a5198219ff18`  |
| 2401   | Layout 1 | `a5198219ff18`  |
| 2397   | Layout 1 | `a5198219ff18`  |
| 2393   | Layout 1 | `a5198219ff18`  |
| 2384   | Layout 1 | `a5198219ff18`  |
| 2378   | Layout 1 | `a5198219ff18`  |
| 2372   | Layout 1 | `a5198219ff18`  |
| 2358   | Layout 1 | `a5198219ff18`  |
| 2352   | Layout 1 | `a5198219ff18`  |
| 2347   | Layout 1 | `a5198219ff18`  |
| 2343   | Layout 1 | `a5198219ff18`  |
| 2335   | Layout 1 | `a5198219ff18`  |
| 2327   | Layout 1 | `a5198219ff18`  |
| 2324   | Layout 1 | `a5198219ff18`  |
| 2319   | Layout 1 | `a5198219ff18`  |
| 2313   | Layout 1 | `a5198219ff18`  |
| 2308   | Layout 1 | `a5198219ff18`  |
| 2302   | Layout 1 | `a5198219ff18`  |
| 2295   | Layout 1 | `a5198219ff18`  |
| 2290   | Layout 1 | `a5198219ff18`  |
| 2284   | Layout 1 | `a5198219ff18`  |
| 2276   | Layout 1 | `a5198219ff18`  |
| 2269   | Layout 1 | `a5198219ff18`  |
| 2259   | Layout 1 | `a5198219ff18`  |
| 2250   | Layout 1 | `a5198219ff18`  |
| 2243   | Layout 1 | `a5198219ff18`  |
| 2235   | Layout 1 | `a5198219ff18`  |
| 2229   | Layout 1 | `a5198219ff18`  |
| 2224   | Layout 1 | `a5198219ff18`  |
| 2218   | Layout 1 | `a5198219ff18`  |
| 2215   | Layout 1 | `a5198219ff18`  |
| 2207   | Layout 1 | `a5198219ff18`  |
| 2203   | Layout 1 | `a5198219ff18`  |
| 2196   | Layout 1 | `a5198219ff18`  |
| 2192   | Layout 1 | `a5198219ff18`  |
| 2189   | Layout 1 | `a5198219ff18`  |
| 2183   | Layout 1 | `a5198219ff18`  |
| 2179   | Layout 1 | `a5198219ff18`  |
| 2171   | Layout 1 | `a5198219ff18`  |
| 2163   | Layout 1 | `a5198219ff18`  |
| 2156   | Layout 1 | `a5198219ff18`  |
| 2151   | Layout 1 | `a5198219ff18`  |
| 2147   | Layout 1 | `a5198219ff18`  |
| 2142   | Layout 1 | `a5198219ff18`  |
| 2138   | Layout 1 | `a5198219ff18`  |
| 2134   | Layout 1 | `a5198219ff18`  |
| 2130   | Layout 1 | `a5198219ff18`  |
| 2122   | Layout 1 | `a5198219ff18`  |
| 2107   | Layout 1 | `a5198219ff18`  |
| 2098   | Layout 1 | `a5198219ff18`  |
| 2089   | Layout 1 | `a5198219ff18`  |
| 2081   | Layout 1 | `a5198219ff18`  |
| 2073   | Layout 1 | `a5198219ff18`  |
| 2067   | Layout 1 | `a5198219ff18`  |
| 2063   | Layout 1 | `a5198219ff18`  |
| 2059   | Layout 1 | `a5198219ff18`  |
| 2052   | Layout 1 | `a5198219ff18`  |
| 2044   | Layout 1 | `a5198219ff18`  |
| 2039   | Layout 1 | `a5198219ff18`  |
| 2032   | Layout 1 | `a5198219ff18`  |
| 2025   | Layout 1 | `a5198219ff18`  |
| 2011   | Layout 1 | `a5198219ff18`  |
| 2005   | Layout 1 | `a5198219ff18`  |
| 2000   | Layout 1 | `a5198219ff18`  |
| 1996   | Layout 1 | `a5198219ff18`  |
| 1991   | Layout 1 | `a5198219ff18`  |
| 1985   | Layout 1 | `a5198219ff18`  |
| 1980   | Layout 1 | `a5198219ff18`  |
| 1969   | Layout 1 | `a5198219ff18`  |
| 1964   | Layout 1 | `a5198219ff18`  |
| 1958   | Layout 1 | `a5198219ff18`  |
| 1950   | Layout 1 | `a5198219ff18`  |
| 1945   | Layout 1 | `a5198219ff18`  |
| 1937   | Layout 1 | `a5198219ff18`  |
| 1933   | Layout 1 | `a5198219ff18`  |
| 1927   | Layout 1 | `a5198219ff18`  |
| 1921   | Layout 1 | `a5198219ff18`  |
| 1914   | Layout 1 | `a5198219ff18`  |
| 1908   | Layout 1 | `a5198219ff18`  |
| 1897   | Layout 1 | `a5198219ff18`  |
| 1892   | Layout 1 | `a5198219ff18`  |
| 1886   | Layout 1 | `a5198219ff18`  |
| 1881   | Layout 1 | `a5198219ff18`  |
| 1871   | Layout 1 | `a5198219ff18`  |
| 1866   | Layout 1 | `a5198219ff18`  |
| 1862   | Layout 1 | `a5198219ff18`  |
| 1854   | Layout 1 | `a5198219ff18`  |
| 1846   | Layout 1 | `a5198219ff18`  |
| 1838   | Layout 1 | `a5198219ff18`  |
| 1832   | Layout 1 | `a5198219ff18`  |
| 1826   | Layout 1 | `a5198219ff18`  |
| 1822   | Layout 1 | `a5198219ff18`  |
| 1818   | Layout 1 | `a5198219ff18`  |
| 1804   | Layout 1 | `a5198219ff18`  |
| 1794   | Layout 1 | `a5198219ff18`  |
| 1790   | Layout 1 | `a5198219ff18`  |
| 1784   | Layout 1 | `a5198219ff18`  |
| 1774   | Layout 1 | `a5198219ff18`  |
| 1771   | Layout 1 | `a5198219ff18`  |
| 1762   | Layout 1 | `a5198219ff18`  |
| 1759   | Layout 1 | `a5198219ff18`  |
| 1754   | Layout 1 | `a5198219ff18`  |
| 1749   | Layout 1 | `a5198219ff18`  |
| 1743   | Layout 1 | `a5198219ff18`  |
| 1737   | Layout 1 | `a5198219ff18`  |
| 1731   | Layout 1 | `a5198219ff18`  |
| 1725   | Layout 1 | `a5198219ff18`  |
| 1717   | Layout 1 | `a5198219ff18`  |
| 1710   | Layout 1 | `a5198219ff18`  |
| 1704   | Layout 1 | `a5198219ff18`  |
| 1698   | Layout 1 | `a5198219ff18`  |
| 1690   | Layout 1 | `a5198219ff18`  |
| 1685   | Layout 1 | `a5198219ff18`  |
| 1680   | Layout 1 | `a5198219ff18`  |
| 1674   | Layout 1 | `a5198219ff18`  |
| 1668   | Layout 1 | `a5198219ff18`  |
| 1659   | Layout 1 | `a5198219ff18`  |
| 1649   | Layout 1 | `a5198219ff18`  |
| 1642   | Layout 1 | `a5198219ff18`  |
| 1636   | Layout 1 | `a5198219ff18`  |
| 1628   | Layout 1 | `a5198219ff18`  |
| 1622   | Layout 1 | `a5198219ff18`  |
| 1614   | Layout 1 | `a5198219ff18`  |
| 1608   | Layout 1 | `a5198219ff18`  |
| 1602   | Layout 1 | `a5198219ff18`  |
| 1598   | Layout 1 | `a5198219ff18`  |
| 1594   | Layout 1 | `a5198219ff18`  |
| 1590   | Layout 1 | `a5198219ff18`  |
| 1587   | Layout 1 | `a5198219ff18`  |
| 1584   | Layout 1 | `a5198219ff18`  |
| 1579   | Layout 1 | `a5198219ff18`  |
| 1572   | Layout 1 | `a5198219ff18`  |
| 1565   | Layout 1 | `a5198219ff18`  |
| 1559   | Layout 1 | `a5198219ff18`  |
| 1554   | Layout 1 | `a5198219ff18`  |
| 1547   | Layout 1 | `a5198219ff18`  |
| 1537   | Layout 1 | `a5198219ff18`  |
| 1529   | Layout 1 | `a5198219ff18`  |
| 1524   | Layout 1 | `a5198219ff18`  |
| 1519   | Layout 1 | `a5198219ff18`  |
| 1509   | Layout 1 | `a5198219ff18`  |
| 1506   | Layout 1 | `a5198219ff18`  |
| 1504   | Layout 1 | `a5198219ff18`  |
| 1500   | Layout 1 | `a5198219ff18`  |
| 1493   | Layout 1 | `a5198219ff18`  |
| 1489   | Layout 1 | `a5198219ff18`  |
| 1485   | Layout 1 | `a5198219ff18`  |
| 1481   | Layout 1 | `a5198219ff18`  |
| 1474   | Layout 1 | `a5198219ff18`  |
| 1466   | Layout 1 | `a5198219ff18`  |
| 1462   | Layout 1 | `a5198219ff18`  |
| 1459   | Layout 1 | `a5198219ff18`  |
| 1453   | Layout 1 | `a5198219ff18`  |
| 1450   | Layout 1 | `a5198219ff18`  |
| 1445   | Layout 1 | `a5198219ff18`  |
| 1439   | Layout 1 | `a5198219ff18`  |
| 1433   | Layout 1 | `a5198219ff18`  |
| 1430   | Layout 1 | `a5198219ff18`  |
| 1426   | Layout 1 | `a5198219ff18`  |
| 1421   | Layout 1 | `a5198219ff18`  |
| 1417   | Layout 1 | `a5198219ff18`  |
| 1416   | Layout 1 | `a5198219ff18`  |
| 1409   | Layout 1 | `a5198219ff18`  |
| 1405   | Layout 1 | `a5198219ff18`  |
| 1401   | Layout 1 | `a5198219ff18`  |
| 1396   | Layout 1 | `a5198219ff18`  |
| 1391   | Layout 1 | `a5198219ff18`  |
| 1390   | Layout 1 | `a5198219ff18`  |
| 1386   | Layout 1 | `a5198219ff18`  |
| 1381   | Layout 1 | `a5198219ff18`  |
| 1379   | Layout 1 | `a5198219ff18`  |
| 1372   | Layout 1 | `a5198219ff18`  |
| 1366   | Layout 1 | `a5198219ff18`  |
| 1364   | Layout 1 | `a5198219ff18`  |
| 1363   | Layout 1 | `a5198219ff18`  |
| 1360   | Layout 1 | `a5198219ff18`  |
| 1358   | Layout 1 | `a5198219ff18`  |
| 1355   | Layout 1 | `a5198219ff18`  |
| 1351   | Layout 1 | `a5198219ff18`  |
| 1348   | Layout 1 | `a5198219ff18`  |
| 1346   | Layout 1 | `a5198219ff18`  |
| 1341   | Layout 1 | `a5198219ff18`  |
| 1340   | Layout 1 | `a5198219ff18`  |
| 1338   | Layout 1 | `a5198219ff18`  |
| 1335   | Layout 1 | `a5198219ff18`  |
| 1333   | Layout 1 | `a5198219ff18`  |
| 1329   | Layout 1 | `a5198219ff18`  |
| 1327   | Layout 1 | `a5198219ff18`  |
| 1324   | Layout 1 | `a5198219ff18`  |
| 1321   | Layout 1 | `a5198219ff18`  |
| 1319   | Layout 1 | `a5198219ff18`  |
| 1318   | Layout 1 | `a5198219ff18`  |
| 1316   | Layout 1 | `a5198219ff18`  |
| 1313   | Layout 1 | `a5198219ff18`  |
| 1311   | Layout 1 | `a5198219ff18`  |
| 1309   | Layout 1 | `a5198219ff18`  |
| 1304   | Layout 1 | `a5198219ff18`  |
| 1292   | Layout 1 | `a5198219ff18`  |
| 1286   | Layout 1 | `a5198219ff18`  |
| 1280   | No file  | `a5198219ff18`  |
| 1276   | No file  | `a5198219ff18`  |
| 1267   | No file  | `a5198219ff18`  |
| 1261   | No file  | `a5198219ff18`  |
| 1256   | No file  | `a5198219ff18`  |
| 1250   | No file  | `a5198219ff18`  |
| 1246   | No file  | `a5198219ff18`  |
| 1239   | No file  | `a5198219ff18`  |
| 1230   | No file  | `a5198219ff18`  |
| 1226   | No file  | `a5198219ff18`  |
| 1220   | No file  | `a5198219ff18`  |
| 1217   | No file  | `a5198219ff18`  |
| 1211   | No file  | `a5198219ff18`  |
| 1210   | No file  | `a5198219ff18`  |
| 1208   | No file  | `a5198219ff18`  |
| 1203   | No file  | `a5198219ff18`  |
| 1197   | No file  | `a5198219ff18`  |
| 1194   | No file  | `a5198219ff18`  |
| 1192   | No file  | `a5198219ff18`  |
| 1187   | No file  | `a5198219ff18`  |
| 1183   | No file  | `a5198219ff18`  |
| 1177   | No file  | `a5198219ff18`  |
| 1173   | No file  | `a5198219ff18`  |
| 1167   | No file  | `a5198219ff18`  |
| 1164   | No file  | `a5198219ff18`  |
| 1156   | No file  | `a5198219ff18`  |
| 1149   | No file  | `a5198219ff18`  |
| 1144   | No file  | `a5198219ff18`  |
| 1137   | No file  | `a5198219ff18`  |
| 1132   | No file  | `a5198219ff18`  |
| 1127   | No file  | `a5198219ff18`  |
| 1122   | No file  | `a5198219ff18`  |
| 1118   | No file  | `a5198219ff18`  |
| 1114   | No file  | `a5198219ff18`  |
| 1109   | No file  | `a5198219ff18`  |
| 1102   | No file  | `a5198219ff18`  |
| 1096   | No file  | `a5198219ff18`  |
| 1088   | No file  | `a5198219ff18`  |
| 1081   | No file  | `a5198219ff18`  |
| 1076   | No file  | `a5198219ff18`  |
| 1069   | No file  | `a5198219ff18`  |
| 1064   | No file  | `a5198219ff18`  |
| 1058   | No file  | `a5198219ff18`  |
| 1051   | No file  | `a5198219ff18`  |
| 1044   | No file  | `a5198219ff18`  |
| 1036   | No file  | `a5198219ff18`  |
| 1026   | No file  | `a5198219ff18`  |
| 1016   | No file  | `a5198219ff18`  |
| 1009   | No file  | `a5198219ff18`  |
| 1005   | No file  | `a5198219ff18`  |
| 1000   | No file  | `a5198219ff18`  |
| 998    | No file  | `a5198219ff18`  |
| 990    | No file  | `a5198219ff18`  |
| 979    | No file  | `a5198219ff18`  |
| 972    | No file  | `a5198219ff18`  |
| 963    | No file  | `a5198219ff18`  |
| 955    | No file  | `a5198219ff18`  |
| 946    | No file  | `a5198219ff18`  |
| 938    | No file  | `a5198219ff18`  |
| 927    | No file  | `a5198219ff18`  |
| 911    | No file  | `a5198219ff18`  |
| 904    | No file  | `a5198219ff18`  |
| 899    | No file  | `a5198219ff18`  |
| 894    | No file  | `a5198219ff18`  |
| 885    | No file  | `a5198219ff18`  |
| 879    | No file  | `a5198219ff18`  |
| 872    | No file  | `a5198219ff18`  |
| 864    | No file  | `a5198219ff18`  |
| 855    | No file  | `a5198219ff18`  |
| 853    | No file  | `a5198219ff18`  |
| 845    | No file  | `a5198219ff18`  |
| 837    | No file  | `a5198219ff18`  |
| 829    | No file  | `a5198219ff18`  |
| 822    | No file  | `a5198219ff18`  |
| 814    | No file  | `a5198219ff18`  |
| 805    | No file  | `a5198219ff18`  |
| 794    | No file  | `a5198219ff18`  |
| 787    | No file  | `a5198219ff18`  |
| 780    | No file  | `a5198219ff18`  |
| 771    | No file  | `a5198219ff18`  |
| 760    | No file  | `a5198219ff18`  |
| 748    | No file  | `a5198219ff18`  |
| 741    | No file  | `a5198219ff18`  |
| 736    | No file  | `a5198219ff18`  |
| 731    | No file  | `a5198219ff18`  |
| 723    | No file  | `a5198219ff18`  |
| 711    | No file  | `a5198219ff18`  |
| 707    | No file  | `a5198219ff18`  |
| 697    | No file  | `a5198219ff18`  |
| 689    | No file  | `a5198219ff18`  |
| 683    | No file  | `a5198219ff18`  |
| 678    | No file  | `a5198219ff18`  |
| 670    | No file  | `a5198219ff18`  |
| 661    | No file  | `a5198219ff18`  |
| 656    | No file  | `a5198219ff18`  |
| 652    | No file  | `a5198219ff18`  |
| 643    | No file  | `a5198219ff18`  |
| 637    | No file  | `a5198219ff18`  |
| 630    | No file  | `a5198219ff18`  |
| 627    | No file  | `a5198219ff18`  |
| 621    | No file  | `a5198219ff18`  |
| 617    | No file  | `a5198219ff18`  |
| 615    | No file  | `a5198219ff18`  |
| 606    | No file  | `a5198219ff18`  |
| 599    | No file  | `a5198219ff18`  |
| 592    | No file  | `a5198219ff18`  |
| 586    | No file  | `a5198219ff18`  |
| 577    | No file  | `a5198219ff18`  |
| 569    | No file  | `a5198219ff18`  |
| 561    | No file  | `a5198219ff18`  |
| 554    | No file  | `a5198219ff18`  |
| 542    | No file  | `a5198219ff18`  |
| 532    | No file  | `a5198219ff18`  |
| 531    | No file  | `a5198219ff18`  |
| 526    | No file  | `a5198219ff18`  |
| 521    | No file  | `a5198219ff18`  |
| 517    | No file  | `a5198219ff18`  |
| 510    | No file  | `a5198219ff18`  |
| 508    | No file  | `a5198219ff18`  |
| 504    | No file  | `a5198219ff18`  |
| 497    | No file  | `a5198219ff18`  |
| 491    | No file  | `a5198219ff18`  |
| 485    | No file  | `a5198219ff18`  |
| 478    | No file  | `a5198219ff18`  |
| 472    | No file  | `a5198219ff18`  |
| 466    | No file  | `a5198219ff18`  |
| 457    | No file  | `a5198219ff18`  |
| 452    | No file  | `a5198219ff18`  |
| 449    | No file  | `a5198219ff18`  |
| 435    | No file  | `a5198219ff18`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of product tags                        |
| `+0x08`             | Row[row_count] | rows         | See Row; row `n` is product tag `n`           |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (4 bytes)

| Offset  | Type | Field     | Notes                                  |
| ------- | ---- | --------- | -------------------------------------- |
| `+0x00` | i32  | tag_order | Sort rank of the tag; `-1` for no rank |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Tag Ranks

| Product tag | `tag_order` (client 3483) | `tag_order` (client 1784) |
| ----------- | ------------------------- | ------------------------- |
| 0           | -1                        | -1                        |
| 1           | 4                         | 3                         |
| 2           | 2                         | 2                         |
| 3           | 7                         | 6                         |
| 4           | 6                         | 5                         |
| 5           | 5                         | 4                         |
| 6           | -1                        | -1                        |
| 7           | 1                         | 1                         |
| 8 to 17     | 3                         | (no row)                  |

Client 3483 inserts rank `3` for the ten new tags and moves the ranks of
tags 1, 3, 4 and 5 up by one; the order of the old tags among themselves
stays the same.

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
the ranks (its `CashProduct_Table` has the per-product `ProductTag`
column), and no Lua of client 3482 names the file or a tag order getter.
The row position is the product tag: the Pearl Shop Lua of client 3482
keeps a `tagTexture` table with one texture region for each tag `0` to
`17`, 18 entries as the file has 18 rows, and draws every tag from `8` up
with the same texture file (`CashShop_05.dds`), the tags that share rank
`3`. `tag_order` takes its name from the file name; the values are a rank
order with each rank once, except the shared rank of tags `8` to `17`.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/enchantshop_tables.py`:
  the product tag (row position) and its rank.

## Open Questions

### Where the Client Uses the Rank

No Lua of client 3482 sorts products by tag; the rank is applied in the
client code, if at all. Which list it orders (the category product list
or the tag filter) is not known.
