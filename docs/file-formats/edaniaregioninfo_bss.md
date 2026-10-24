# `edaniaregioninfo.bss` Format

## Purpose

Holds one row per Edania region, the ten castle domains that guilds hold in Edania (Aetherion to Voidekaia), plus a row for the "no region" value. Each row stores the client's `__eEdaniaRegion` value and its colour in the Edania region map (`ui_texture/minimap/area/edaniaregionmap.bmp`), twice; for the five castles with a region of their own the colour equals that region's `regioninfo.bss` `color`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3483    | `edaniaregioninfo.bss` | 119   | 11 Row  | 9         |

| Layout | File                   | Known        | Unknown      |
| ------ | ---------------------- | ------------ | ------------ |
| 1      | `edaniaregioninfo.bss` | 64 B (53.8%) | 55 B (46.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `b86a06e366fe`  |
| 3482   | Layout 1 | `b86a06e366fe`  |
| 3474   | Layout 1 | `b86a06e366fe`  |
| 3473   | Layout 1 | `b86a06e366fe`  |
| 3464   | Layout 1 | `b86a06e366fe`  |
| 3458   | Layout 1 | `b86a06e366fe`  |
| 3454   | Layout 1 | `b86a06e366fe`  |
| 3444   | Layout 1 | `b86a06e366fe`  |
| 3435   | Layout 1 | `b86a06e366fe`  |
| 3426   | Layout 1 | `b86a06e366fe`  |
| 3418   | Layout 1 | `b86a06e366fe`  |
| 3412   | Layout 1 | `b86a06e366fe`  |
| 3402   | Layout 1 | `b86a06e366fe`  |
| 3396   | Layout 1 | `b86a06e366fe`  |
| 3387   | Layout 1 | `b86a06e366fe`  |
| 3381   | Layout 1 | `b86a06e366fe`  |
| 3373   | Layout 1 | `b86a06e366fe`  |
| 3364   | Layout 1 | `b86a06e366fe`  |
| 3356   | Layout 1 | `b86a06e366fe`  |
| 3349   | Layout 1 | `b86a06e366fe`  |
| 3342   | Layout 1 | `b86a06e366fe`  |
| 3335   | Layout 1 | `b86a06e366fe`  |
| 3326   | Layout 1 | `b86a06e366fe`  |
| 3321   | Layout 1 | `b86a06e366fe`  |
| 3314   | Layout 1 | `b86a06e366fe`  |
| 3303   | Layout 1 | `b86a06e366fe`  |
| 3302   | Layout 1 | `b86a06e366fe`  |
| 3293   | Layout 1 | `b86a06e366fe`  |
| 3283   | Layout 1 | `b86a06e366fe`  |
| 3275   | Layout 1 | `b86a06e366fe`  |
| 3267   | Layout 1 | `b86a06e366fe`  |
| 3258   | Layout 1 | `b86a06e366fe`  |
| 3251   | Layout 1 | `b86a06e366fe`  |
| 3242   | Layout 1 | `b86a06e366fe`  |
| 3235   | Layout 1 | `b86a06e366fe`  |
| 3229   | Layout 1 | `b86a06e366fe`  |
| 3212   | Layout 1 | `b86a06e366fe`  |
| 3203   | Layout 1 | `b86a06e366fe`  |
| 3193   | Layout 1 | `b86a06e366fe`  |
| 3186   | Layout 1 | `b86a06e366fe`  |
| 3177   | Layout 1 | `b86a06e366fe`  |
| 3169   | Layout 1 | `b86a06e366fe`  |
| 3158   | Layout 1 | `b86a06e366fe`  |
| 3151   | Layout 1 | `b86a06e366fe`  |
| 3144   | Layout 1 | `b86a06e366fe`  |
| 3133   | Layout 1 | `b86a06e366fe`  |
| 3125   | Layout 1 | `b86a06e366fe`  |
| 3118   | Layout 1 | `b86a06e366fe`  |
| 3111   | Layout 1 | `b86a06e366fe`  |
| 3103   | Layout 1 | `b86a06e366fe`  |
| 3095   | Layout 1 | `b86a06e366fe`  |
| 3086   | Layout 1 | `b86a06e366fe`  |
| 3072   | Layout 1 | `b86a06e366fe`  |
| 3062   | Layout 1 | `b86a06e366fe`  |
| 3052   | Layout 1 | `b86a06e366fe`  |
| 3045   | Layout 1 | `b86a06e366fe`  |
| 3037   | Layout 1 | `b86a06e366fe`  |
| 3030   | Layout 1 | `b86a06e366fe`  |
| 3021   | Layout 1 | `b86a06e366fe`  |
| 3012   | Layout 1 | `b86a06e366fe`  |
| 3002   | Layout 1 | `b86a06e366fe`  |
| 2995   | No file  | `b86a06e366fe`  |
| 2987   | No file  | `b86a06e366fe`  |
| 2978   | No file  | `b86a06e366fe`  |
| 2970   | No file  | `b86a06e366fe`  |
| 2959   | No file  | `b86a06e366fe`  |
| 2951   | No file  | `b86a06e366fe`  |
| 2942   | No file  | `b86a06e366fe`  |
| 2935   | No file  | `b86a06e366fe`  |
| 2932   | No file  | `b86a06e366fe`  |
| 2923   | No file  | `b86a06e366fe`  |
| 2919   | No file  | `b86a06e366fe`  |
| 2907   | No file  | `b86a06e366fe`  |
| 2900   | No file  | `b86a06e366fe`  |
| 2891   | No file  | `b86a06e366fe`  |
| 2882   | No file  | `b86a06e366fe`  |
| 2872   | No file  | `b86a06e366fe`  |
| 2863   | No file  | `b86a06e366fe`  |
| 2855   | No file  | `b86a06e366fe`  |
| 2849   | No file  | `b86a06e366fe`  |
| 2844   | No file  | `b86a06e366fe`  |
| 2834   | No file  | `b86a06e366fe`  |
| 2825   | No file  | `b86a06e366fe`  |
| 2819   | No file  | `b86a06e366fe`  |
| 2811   | No file  | `b86a06e366fe`  |
| 2803   | No file  | `b86a06e366fe`  |
| 2794   | No file  | `b86a06e366fe`  |
| 2783   | No file  | `b86a06e366fe`  |
| 2774   | No file  | `b86a06e366fe`  |
| 2765   | No file  | `b86a06e366fe`  |
| 2756   | No file  | `b86a06e366fe`  |
| 2750   | No file  | `b86a06e366fe`  |
| 2743   | No file  | `b86a06e366fe`  |
| 2736   | No file  | `b86a06e366fe`  |
| 2726   | No file  | `b86a06e366fe`  |
| 2717   | No file  | `b86a06e366fe`  |
| 2709   | No file  | `b86a06e366fe`  |
| 2703   | No file  | `b86a06e366fe`  |
| 2695   | No file  | `b86a06e366fe`  |
| 2684   | No file  | `b86a06e366fe`  |
| 2672   | No file  | `b86a06e366fe`  |
| 2665   | No file  | `b86a06e366fe`  |
| 2657   | No file  | `b86a06e366fe`  |
| 2649   | No file  | `b86a06e366fe`  |
| 2644   | No file  | `b86a06e366fe`  |
| 2637   | No file  | `b86a06e366fe`  |
| 2629   | No file  | `b86a06e366fe`  |
| 2619   | No file  | `b86a06e366fe`  |
| 2612   | No file  | `b86a06e366fe`  |
| 2606   | No file  | `b86a06e366fe`  |
| 2602   | No file  | `b86a06e366fe`  |
| 2601   | No file  | `b86a06e366fe`  |
| 2592   | No file  | `b86a06e366fe`  |
| 2583   | No file  | `b86a06e366fe`  |
| 2575   | No file  | `b86a06e366fe`  |
| 2567   | No file  | `b86a06e366fe`  |
| 2560   | No file  | `b86a06e366fe`  |
| 2553   | No file  | `b86a06e366fe`  |
| 2545   | No file  | `b86a06e366fe`  |
| 2538   | No file  | `b86a06e366fe`  |
| 2529   | No file  | `b86a06e366fe`  |
| 2519   | No file  | `b86a06e366fe`  |
| 2513   | No file  | `b86a06e366fe`  |
| 2510   | No file  | `b86a06e366fe`  |
| 2507   | No file  | `b86a06e366fe`  |
| 2503   | No file  | `b86a06e366fe`  |
| 2498   | No file  | `b86a06e366fe`  |
| 2492   | No file  | `b86a06e366fe`  |
| 2487   | No file  | `b86a06e366fe`  |
| 2480   | No file  | `b86a06e366fe`  |
| 2474   | No file  | `b86a06e366fe`  |
| 2468   | No file  | `b86a06e366fe`  |
| 2460   | No file  | `b86a06e366fe`  |
| 2453   | No file  | `b86a06e366fe`  |
| 2444   | No file  | `b86a06e366fe`  |
| 2438   | No file  | `b86a06e366fe`  |
| 2434   | No file  | `b86a06e366fe`  |
| 2429   | No file  | `b86a06e366fe`  |
| 2421   | No file  | `b86a06e366fe`  |
| 2414   | No file  | `b86a06e366fe`  |
| 2407   | No file  | `b86a06e366fe`  |
| 2401   | No file  | `b86a06e366fe`  |
| 2397   | No file  | `b86a06e366fe`  |
| 2393   | No file  | `b86a06e366fe`  |
| 2384   | No file  | `b86a06e366fe`  |
| 2378   | No file  | `b86a06e366fe`  |
| 2372   | No file  | `b86a06e366fe`  |
| 2358   | No file  | `b86a06e366fe`  |
| 2352   | No file  | `b86a06e366fe`  |
| 2347   | No file  | `b86a06e366fe`  |
| 2343   | No file  | `b86a06e366fe`  |
| 2335   | No file  | `b86a06e366fe`  |
| 2327   | No file  | `b86a06e366fe`  |
| 2324   | No file  | `b86a06e366fe`  |
| 2319   | No file  | `b86a06e366fe`  |
| 2313   | No file  | `b86a06e366fe`  |
| 2308   | No file  | `b86a06e366fe`  |
| 2302   | No file  | `b86a06e366fe`  |
| 2295   | No file  | `b86a06e366fe`  |
| 2290   | No file  | `b86a06e366fe`  |
| 2284   | No file  | `b86a06e366fe`  |
| 2276   | No file  | `b86a06e366fe`  |
| 2269   | No file  | `b86a06e366fe`  |
| 2259   | No file  | `b86a06e366fe`  |
| 2250   | No file  | `b86a06e366fe`  |
| 2243   | No file  | `b86a06e366fe`  |
| 2235   | No file  | `b86a06e366fe`  |
| 2229   | No file  | `b86a06e366fe`  |
| 2224   | No file  | `b86a06e366fe`  |
| 2218   | No file  | `b86a06e366fe`  |
| 2215   | No file  | `b86a06e366fe`  |
| 2207   | No file  | `b86a06e366fe`  |
| 2203   | No file  | `b86a06e366fe`  |
| 2196   | No file  | `b86a06e366fe`  |
| 2192   | No file  | `b86a06e366fe`  |
| 2189   | No file  | `b86a06e366fe`  |
| 2183   | No file  | `b86a06e366fe`  |
| 2179   | No file  | `b86a06e366fe`  |
| 2171   | No file  | `b86a06e366fe`  |
| 2163   | No file  | `b86a06e366fe`  |
| 2156   | No file  | `b86a06e366fe`  |
| 2151   | No file  | `b86a06e366fe`  |
| 2147   | No file  | `b86a06e366fe`  |
| 2142   | No file  | `b86a06e366fe`  |
| 2138   | No file  | `b86a06e366fe`  |
| 2134   | No file  | `b86a06e366fe`  |
| 2130   | No file  | `b86a06e366fe`  |
| 2122   | No file  | `b86a06e366fe`  |
| 2107   | No file  | `b86a06e366fe`  |
| 2098   | No file  | `b86a06e366fe`  |
| 2089   | No file  | `b86a06e366fe`  |
| 2081   | No file  | `b86a06e366fe`  |
| 2073   | No file  | `b86a06e366fe`  |
| 2067   | No file  | `b86a06e366fe`  |
| 2063   | No file  | `b86a06e366fe`  |
| 2059   | No file  | `b86a06e366fe`  |
| 2052   | No file  | `b86a06e366fe`  |
| 2044   | No file  | `b86a06e366fe`  |
| 2039   | No file  | `b86a06e366fe`  |
| 2032   | No file  | `b86a06e366fe`  |
| 2025   | No file  | `b86a06e366fe`  |
| 2011   | No file  | `b86a06e366fe`  |
| 2005   | No file  | `b86a06e366fe`  |
| 2000   | No file  | `b86a06e366fe`  |
| 1996   | No file  | `b86a06e366fe`  |
| 1991   | No file  | `b86a06e366fe`  |
| 1985   | No file  | `b86a06e366fe`  |
| 1980   | No file  | `b86a06e366fe`  |
| 1969   | No file  | `b86a06e366fe`  |
| 1964   | No file  | `b86a06e366fe`  |
| 1958   | No file  | `b86a06e366fe`  |
| 1950   | No file  | `b86a06e366fe`  |
| 1945   | No file  | `b86a06e366fe`  |
| 1937   | No file  | `b86a06e366fe`  |
| 1933   | No file  | `b86a06e366fe`  |
| 1927   | No file  | `b86a06e366fe`  |
| 1921   | No file  | `b86a06e366fe`  |
| 1914   | No file  | `b86a06e366fe`  |
| 1908   | No file  | `b86a06e366fe`  |
| 1897   | No file  | `b86a06e366fe`  |
| 1892   | No file  | `b86a06e366fe`  |
| 1886   | No file  | `b86a06e366fe`  |
| 1881   | No file  | `b86a06e366fe`  |
| 1871   | No file  | `b86a06e366fe`  |
| 1866   | No file  | `b86a06e366fe`  |
| 1862   | No file  | `b86a06e366fe`  |
| 1854   | No file  | `b86a06e366fe`  |
| 1846   | No file  | `b86a06e366fe`  |
| 1838   | No file  | `b86a06e366fe`  |
| 1832   | No file  | `b86a06e366fe`  |
| 1826   | No file  | `b86a06e366fe`  |
| 1822   | No file  | `b86a06e366fe`  |
| 1818   | No file  | `b86a06e366fe`  |
| 1804   | No file  | `b86a06e366fe`  |
| 1794   | No file  | `b86a06e366fe`  |
| 1790   | No file  | `b86a06e366fe`  |
| 1784   | No file  | `b86a06e366fe`  |
| 1774   | No file  | `b86a06e366fe`  |
| 1771   | No file  | `b86a06e366fe`  |
| 1762   | No file  | `b86a06e366fe`  |
| 1759   | No file  | `b86a06e366fe`  |
| 1754   | No file  | `b86a06e366fe`  |
| 1749   | No file  | `b86a06e366fe`  |
| 1743   | No file  | `b86a06e366fe`  |
| 1737   | No file  | `b86a06e366fe`  |
| 1731   | No file  | `b86a06e366fe`  |
| 1725   | No file  | `b86a06e366fe`  |
| 1717   | No file  | `b86a06e366fe`  |
| 1710   | No file  | `b86a06e366fe`  |
| 1704   | No file  | `b86a06e366fe`  |
| 1698   | No file  | `b86a06e366fe`  |
| 1690   | No file  | `b86a06e366fe`  |
| 1685   | No file  | `b86a06e366fe`  |
| 1680   | No file  | `b86a06e366fe`  |
| 1674   | No file  | `b86a06e366fe`  |
| 1668   | No file  | `b86a06e366fe`  |
| 1659   | No file  | `b86a06e366fe`  |
| 1649   | No file  | `b86a06e366fe`  |
| 1642   | No file  | `b86a06e366fe`  |
| 1636   | No file  | `b86a06e366fe`  |
| 1628   | No file  | `b86a06e366fe`  |
| 1622   | No file  | `b86a06e366fe`  |
| 1614   | No file  | `b86a06e366fe`  |
| 1608   | No file  | `b86a06e366fe`  |
| 1602   | No file  | `b86a06e366fe`  |
| 1598   | No file  | `b86a06e366fe`  |
| 1594   | No file  | `b86a06e366fe`  |
| 1590   | No file  | `b86a06e366fe`  |
| 1587   | No file  | `b86a06e366fe`  |
| 1584   | No file  | `b86a06e366fe`  |
| 1579   | No file  | `b86a06e366fe`  |
| 1572   | No file  | `b86a06e366fe`  |
| 1565   | No file  | `b86a06e366fe`  |
| 1559   | No file  | `b86a06e366fe`  |
| 1554   | No file  | `b86a06e366fe`  |
| 1547   | No file  | `b86a06e366fe`  |
| 1537   | No file  | `b86a06e366fe`  |
| 1529   | No file  | `b86a06e366fe`  |
| 1524   | No file  | `b86a06e366fe`  |
| 1519   | No file  | `b86a06e366fe`  |
| 1509   | No file  | `b86a06e366fe`  |
| 1506   | No file  | `b86a06e366fe`  |
| 1504   | No file  | `b86a06e366fe`  |
| 1500   | No file  | `b86a06e366fe`  |
| 1493   | No file  | `b86a06e366fe`  |
| 1489   | No file  | `b86a06e366fe`  |
| 1485   | No file  | `b86a06e366fe`  |
| 1481   | No file  | `b86a06e366fe`  |
| 1474   | No file  | `b86a06e366fe`  |
| 1466   | No file  | `b86a06e366fe`  |
| 1462   | No file  | `b86a06e366fe`  |
| 1459   | No file  | `b86a06e366fe`  |
| 1453   | No file  | `b86a06e366fe`  |
| 1450   | No file  | `b86a06e366fe`  |
| 1445   | No file  | `b86a06e366fe`  |
| 1439   | No file  | `b86a06e366fe`  |
| 1433   | No file  | `b86a06e366fe`  |
| 1430   | No file  | `b86a06e366fe`  |
| 1426   | No file  | `b86a06e366fe`  |
| 1421   | No file  | `b86a06e366fe`  |
| 1417   | No file  | `b86a06e366fe`  |
| 1416   | No file  | `b86a06e366fe`  |
| 1409   | No file  | `b86a06e366fe`  |
| 1405   | No file  | `b86a06e366fe`  |
| 1401   | No file  | `b86a06e366fe`  |
| 1396   | No file  | `b86a06e366fe`  |
| 1391   | No file  | `b86a06e366fe`  |
| 1390   | No file  | `b86a06e366fe`  |
| 1386   | No file  | `b86a06e366fe`  |
| 1381   | No file  | `b86a06e366fe`  |
| 1379   | No file  | `b86a06e366fe`  |
| 1372   | No file  | `b86a06e366fe`  |
| 1366   | No file  | `b86a06e366fe`  |
| 1364   | No file  | `b86a06e366fe`  |
| 1363   | No file  | `b86a06e366fe`  |
| 1360   | No file  | `b86a06e366fe`  |
| 1358   | No file  | `b86a06e366fe`  |
| 1355   | No file  | `b86a06e366fe`  |
| 1351   | No file  | `b86a06e366fe`  |
| 1348   | No file  | `b86a06e366fe`  |
| 1346   | No file  | `b86a06e366fe`  |
| 1341   | No file  | `b86a06e366fe`  |
| 1340   | No file  | `b86a06e366fe`  |
| 1338   | No file  | `b86a06e366fe`  |
| 1335   | No file  | `b86a06e366fe`  |
| 1333   | No file  | `b86a06e366fe`  |
| 1329   | No file  | `b86a06e366fe`  |
| 1327   | No file  | `b86a06e366fe`  |
| 1324   | No file  | `b86a06e366fe`  |
| 1321   | No file  | `b86a06e366fe`  |
| 1319   | No file  | `b86a06e366fe`  |
| 1318   | No file  | `b86a06e366fe`  |
| 1316   | No file  | `b86a06e366fe`  |
| 1313   | No file  | `b86a06e366fe`  |
| 1311   | No file  | `b86a06e366fe`  |
| 1309   | No file  | `b86a06e366fe`  |
| 1304   | No file  | `b86a06e366fe`  |
| 1292   | No file  | `b86a06e366fe`  |
| 1286   | No file  | `b86a06e366fe`  |
| 1280   | No file  | `b86a06e366fe`  |
| 1276   | No file  | `b86a06e366fe`  |
| 1267   | No file  | `b86a06e366fe`  |
| 1261   | No file  | `b86a06e366fe`  |
| 1256   | No file  | `b86a06e366fe`  |
| 1250   | No file  | `b86a06e366fe`  |
| 1246   | No file  | `b86a06e366fe`  |
| 1239   | No file  | `b86a06e366fe`  |
| 1230   | No file  | `b86a06e366fe`  |
| 1226   | No file  | `b86a06e366fe`  |
| 1220   | No file  | `b86a06e366fe`  |
| 1217   | No file  | `b86a06e366fe`  |
| 1211   | No file  | `b86a06e366fe`  |
| 1210   | No file  | `b86a06e366fe`  |
| 1208   | No file  | `b86a06e366fe`  |
| 1203   | No file  | `b86a06e366fe`  |
| 1197   | No file  | `b86a06e366fe`  |
| 1194   | No file  | `b86a06e366fe`  |
| 1192   | No file  | `b86a06e366fe`  |
| 1187   | No file  | `b86a06e366fe`  |
| 1183   | No file  | `b86a06e366fe`  |
| 1177   | No file  | `b86a06e366fe`  |
| 1173   | No file  | `b86a06e366fe`  |
| 1167   | No file  | `b86a06e366fe`  |
| 1164   | No file  | `b86a06e366fe`  |
| 1156   | No file  | `b86a06e366fe`  |
| 1149   | No file  | `b86a06e366fe`  |
| 1144   | No file  | `b86a06e366fe`  |
| 1137   | No file  | `b86a06e366fe`  |
| 1132   | No file  | `b86a06e366fe`  |
| 1127   | No file  | `b86a06e366fe`  |
| 1122   | No file  | `b86a06e366fe`  |
| 1118   | No file  | `b86a06e366fe`  |
| 1114   | No file  | `b86a06e366fe`  |
| 1109   | No file  | `b86a06e366fe`  |
| 1102   | No file  | `b86a06e366fe`  |
| 1096   | No file  | `b86a06e366fe`  |
| 1088   | No file  | `b86a06e366fe`  |
| 1081   | No file  | `b86a06e366fe`  |
| 1076   | No file  | `b86a06e366fe`  |
| 1069   | No file  | `b86a06e366fe`  |
| 1064   | No file  | `b86a06e366fe`  |
| 1058   | No file  | `b86a06e366fe`  |
| 1051   | No file  | `b86a06e366fe`  |
| 1044   | No file  | `b86a06e366fe`  |
| 1036   | No file  | `b86a06e366fe`  |
| 1026   | No file  | `b86a06e366fe`  |
| 1016   | No file  | `b86a06e366fe`  |
| 1009   | No file  | `b86a06e366fe`  |
| 1005   | No file  | `b86a06e366fe`  |
| 1000   | No file  | `b86a06e366fe`  |
| 998    | No file  | `b86a06e366fe`  |
| 990    | No file  | `b86a06e366fe`  |
| 979    | No file  | `b86a06e366fe`  |
| 972    | No file  | `b86a06e366fe`  |
| 963    | No file  | `b86a06e366fe`  |
| 955    | No file  | `b86a06e366fe`  |
| 946    | No file  | `b86a06e366fe`  |
| 938    | No file  | `b86a06e366fe`  |
| 927    | No file  | `b86a06e366fe`  |
| 911    | No file  | `b86a06e366fe`  |
| 904    | No file  | `b86a06e366fe`  |
| 899    | No file  | `b86a06e366fe`  |
| 894    | No file  | `b86a06e366fe`  |
| 885    | No file  | `b86a06e366fe`  |
| 879    | No file  | `b86a06e366fe`  |
| 872    | No file  | `b86a06e366fe`  |
| 864    | No file  | `b86a06e366fe`  |
| 855    | No file  | `b86a06e366fe`  |
| 853    | No file  | `b86a06e366fe`  |
| 845    | No file  | `b86a06e366fe`  |
| 837    | No file  | `b86a06e366fe`  |
| 829    | No file  | `b86a06e366fe`  |
| 822    | No file  | `b86a06e366fe`  |
| 814    | No file  | `b86a06e366fe`  |
| 805    | No file  | `b86a06e366fe`  |
| 794    | No file  | `b86a06e366fe`  |
| 787    | No file  | `b86a06e366fe`  |
| 780    | No file  | `b86a06e366fe`  |
| 771    | No file  | `b86a06e366fe`  |
| 760    | No file  | `b86a06e366fe`  |
| 748    | No file  | `b86a06e366fe`  |
| 741    | No file  | `b86a06e366fe`  |
| 736    | No file  | `b86a06e366fe`  |
| 731    | No file  | `b86a06e366fe`  |
| 723    | No file  | `b86a06e366fe`  |
| 711    | No file  | `b86a06e366fe`  |
| 707    | No file  | `b86a06e366fe`  |
| 697    | No file  | `b86a06e366fe`  |
| 689    | No file  | `b86a06e366fe`  |
| 683    | No file  | `b86a06e366fe`  |
| 678    | No file  | `b86a06e366fe`  |
| 670    | No file  | `b86a06e366fe`  |
| 661    | No file  | `b86a06e366fe`  |
| 656    | No file  | `b86a06e366fe`  |
| 652    | No file  | `b86a06e366fe`  |
| 643    | No file  | `b86a06e366fe`  |
| 637    | No file  | `b86a06e366fe`  |
| 630    | No file  | `b86a06e366fe`  |
| 627    | No file  | `b86a06e366fe`  |
| 621    | No file  | `b86a06e366fe`  |
| 617    | No file  | `b86a06e366fe`  |
| 615    | No file  | `b86a06e366fe`  |
| 606    | No file  | `b86a06e366fe`  |
| 599    | No file  | `b86a06e366fe`  |
| 592    | No file  | `b86a06e366fe`  |
| 586    | No file  | `b86a06e366fe`  |
| 577    | No file  | `b86a06e366fe`  |
| 569    | No file  | `b86a06e366fe`  |
| 561    | No file  | `b86a06e366fe`  |
| 554    | No file  | `b86a06e366fe`  |
| 542    | No file  | `b86a06e366fe`  |
| 532    | No file  | `b86a06e366fe`  |
| 531    | No file  | `b86a06e366fe`  |
| 526    | No file  | `b86a06e366fe`  |
| 521    | No file  | `b86a06e366fe`  |
| 517    | No file  | `b86a06e366fe`  |
| 510    | No file  | `b86a06e366fe`  |
| 508    | No file  | `b86a06e366fe`  |
| 504    | No file  | `b86a06e366fe`  |
| 497    | No file  | `b86a06e366fe`  |
| 491    | No file  | `b86a06e366fe`  |
| 485    | No file  | `b86a06e366fe`  |
| 478    | No file  | `b86a06e366fe`  |
| 472    | No file  | `b86a06e366fe`  |
| 466    | No file  | `b86a06e366fe`  |
| 457    | No file  | `b86a06e366fe`  |
| 452    | No file  | `b86a06e366fe`  |
| 449    | No file  | `b86a06e366fe`  |
| 435    | No file  | `b86a06e366fe`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                                   |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Castle name text (LOC type 37, keyed by the hash of the GAME sheet key `LUA_EDANIA_SYSTEM_CASTLE_NAME_<n>`) |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                                                   |
| ------------------- | ----------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                          |
| `+0x04`             | u32               | record_count       | Observed `11`                                           |
| `+0x08`             | Row[record_count] | records            | See Row; byte-packed                                    |
| `records+0x00`      | String Table      | string_table       | The PABR string table, present but empty                |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 9 × count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                              |

The file is `8 + 9 × 11 + 12 = 119` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (9 bytes)

| Offset  | Type     | Field         | Notes                                                                                                   |
| ------- | -------- | ------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | bytes[3] | map_color     | Region map colour, stored blue, green, red like the `regioninfo.bss` `color`; the parser returns `rrggbb`. See Notes |
| `+0x03` | u8       | unknown_03    | Always `0`                                                                                              |
| `+0x04` | bytes[3] | unknown_04    | Equals `map_color` on every row                                                                         |
| `+0x07` | u8       | unknown_07    | Always `0`                                                                                              |
| `+0x08` | u8       | edania_region | `__eEdaniaRegion` value, unique; `0` to `9` for the regions, `10` for `__eEdaniaRegion_Count`. Rows are not in key order |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Enum Values

`edania_region` is the client's `__eEdaniaRegion` enum. The Lua lists the names in this order (`panel_characternametag.luac`, `panel_widget_chatmain_2.luac`, `panel_window_edania_contents_all.luac`) and loops `0` to `Zephyros` for the first Edana group and `Aphrodon` to `Count - 1` for the second (`panel_characterinfo_cashbuff_all_1.luac`). The castle name key is the one the Edania window gives each region.

| Value | Enum name   | Castle name key                   | English castle name |
| ----- | ----------- | --------------------------------- | ------------------- |
| `0`   | Aetherion   | `LUA_EDANIA_SYSTEM_CASTLE_NAME_1`  | Aetherion Castle    |
| `1`   | Nymphamare  | `LUA_EDANIA_SYSTEM_CASTLE_NAME_2`  | Nymphamaré Castle   |
| `2`   | Orbita      | `LUA_EDANIA_SYSTEM_CASTLE_NAME_4`  | Orbita Castle       |
| `3`   | Tenebraum   | `LUA_EDANIA_SYSTEM_CASTLE_NAME_3`  | Tenebraum Castle    |
| `4`   | Zephyros    | `LUA_EDANIA_SYSTEM_CASTLE_NAME_5`  | Zephyros Castle     |
| `5`   | Aphrodon    | `LUA_EDANIA_SYSTEM_CASTLE_NAME_6`  | Aphrodon Temple     |
| `6`   | Hermesia    | `LUA_EDANIA_SYSTEM_CASTLE_NAME_7`  | Hermesia Castle     |
| `7`   | Magaia      | `LUA_EDANIA_SYSTEM_CASTLE_NAME_8`  | Magaia Temple       |
| `8`   | Aresion     | `LUA_EDANIA_SYSTEM_CASTLE_NAME_9`  | Aresion Temple      |
| `9`   | Voidekaia   | `LUA_EDANIA_SYSTEM_CASTLE_NAME_10` | Event Horizon       |
| `10`  | _Count      |                                   | none                |

Orbita and Tenebraum swap key numbers 3 and 4. The file confirms the values of the first five: their `map_color` matches the `regioninfo.bss` `color` of exactly one region each, and that region is the castle of the same name (1581 Aetherion Castle, 1621 Nymphamaré Castle, 1571 Orbita Castle, 1611 Tenebraum Castle, 1596 Zephyros Castle).

## Notes

- The client reads a player's Edania region with `ToClient_GetEdaniaRegion(userNo)` and picks the faction icon on the name tag and in chat from it (`Combine_Etc_EdaniaIcon_Jordain_Normal` for Aetherion ... `Combine_Etc_EdaniaIcon_Hadum_Normal` for Voidekaia). `_Count` is the "no Edania region" answer.
- `regioninfo.bss` has regions named after the second-group castles too (Aphrodon Temple, Hermesia Outer and Inner Castle, Magaia Temple, Aresion Temple), but none of them has the colour stored here, so only the first five rows link to a region.
- `map_color` follows `ui_texture/minimap/area/edaniaregionmap.bmp.rid`, the palette of the Edania region map, which lists exactly these 11 colours on client 3474 (`100d10` first); the same holds for the region maps of three other tables of this row shape ([`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md#field-names) Field Names).
- `blizzardregioninfo.bss` is the other small region-variant table. It does not share this layout (26-byte rows keyed by a region key), so the two files have separate parsers.

## Open Questions

### Why the Value Is Stored Twice

`unknown_04` equals `map_color` on every row. Whether the two are fill and
border, or two map layers, is not known. `100d10`, the `_Count` row's
colour, is the first colour of every region map palette of this row shape.

Each colour plus its zero byte has the shape of `regioninfo.bss` `color`
(u8[3]) and `color_alpha`, which the 2016 client types as one 4-byte
`pa::Color _colorKey`, so `unknown_03` and `unknown_07` read as alpha
bytes; that is a reading, not a name. No source names `unknown_03`,
`unknown_04` and `unknown_07`: the file is not in the client 1784 private server's binaries,
sheets or server dump (no `edania` string), the 2016 client predates
Edania, the live client exe holds no readable strings, and none of the
client 3474 Lua Edania calls (`ToClient_GetEdaniaRegion`,
`ToClient_GetEdaniaApplyRegion`, `ToClient_IsEdaniaAreaOn`,
`ToClient_ToggleEdaniaArea`, `ToClient_GetEdaniaEtcOption`) returns a
colour.

## In-Game Checks

### Edania Overlay Colours

Needs zone: Edania

This checks whether the world map overlay draws each Edania domain in its `map_color`, the colour of the domain in the Edania region map.

For the five first-group castles `map_color` equals the `regioninfo.bss` `color` of the castle's region, and `regioninfo.bss` stores that colour blue, green, red (its `R`, `G` and `B` match the server-side `Region_Table` on 895 of 896 regions, client 3464). Read the same way, the rows here are Aetherion `0a1cf5` (blue), Orbita `905037` (brown-red) and Event Horizon (Voidekaia) `770868` (purple).

1. Open the world map over Edania.
2. Switch the Edania area overlay on (`ToClient_ToggleEdaniaArea`).
3. Note the colour of the Aetherion, Orbita and Event Horizon domains.

Expected result: the three domains show those colours. A domain colour that matches no row means the overlay takes its colour from somewhere else.
