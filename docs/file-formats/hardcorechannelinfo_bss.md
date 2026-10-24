# `hardcorechannelinfo.bss` Format

## Purpose

The colours of the Hardcore channel's region map, one 9-byte row each: the
colour, a copy of it, and a u8 from `0` to `4`. The 15 colours on client
3474 are the 15 that `ui_texture/minimap/area/hardcorechannelmap.bmp.rid`
lists for the map bitmap of the same name, so each row ties one area of that
map to a value. The rows have the shape of
[`edaniaregioninfo.bss`](edaniaregioninfo_bss.md),
[`rosewarinfo.bss`](rosewarinfo_bss.md) and
[`snowboardcourseinfo.bss`](snowboardcourseinfo_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 2834 and later | 3483    | `hardcorechannelinfo.bss` | 155   | 15 Row  | 9         |

| Layout | File                      | Known        | Unknown      |
| ------ | ------------------------- | ------------ | ------------ |
| 1      | `hardcorechannelinfo.bss` | 65 B (41.9%) | 90 B (58.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `cb430810e3c2`  |
| 3482   | Layout 1 | `cb430810e3c2`  |
| 3474   | Layout 1 | `cb430810e3c2`  |
| 3473   | Layout 1 | `cb430810e3c2`  |
| 3464   | Layout 1 | `cb430810e3c2`  |
| 3458   | Layout 1 | `cb430810e3c2`  |
| 3454   | Layout 1 | `cb430810e3c2`  |
| 3444   | Layout 1 | `cb430810e3c2`  |
| 3435   | Layout 1 | `cb430810e3c2`  |
| 3426   | Layout 1 | `cb430810e3c2`  |
| 3418   | Layout 1 | `cb430810e3c2`  |
| 3412   | Layout 1 | `cb430810e3c2`  |
| 3402   | Layout 1 | `cb430810e3c2`  |
| 3396   | Layout 1 | `cb430810e3c2`  |
| 3387   | Layout 1 | `cb430810e3c2`  |
| 3381   | Layout 1 | `cb430810e3c2`  |
| 3373   | Layout 1 | `cb430810e3c2`  |
| 3364   | Layout 1 | `cb430810e3c2`  |
| 3356   | Layout 1 | `cb430810e3c2`  |
| 3349   | Layout 1 | `cb430810e3c2`  |
| 3342   | Layout 1 | `cb430810e3c2`  |
| 3335   | Layout 1 | `cb430810e3c2`  |
| 3326   | Layout 1 | `cb430810e3c2`  |
| 3321   | Layout 1 | `cb430810e3c2`  |
| 3314   | Layout 1 | `cb430810e3c2`  |
| 3303   | Layout 1 | `cb430810e3c2`  |
| 3302   | Layout 1 | `cb430810e3c2`  |
| 3293   | Layout 1 | `cb430810e3c2`  |
| 3283   | Layout 1 | `cb430810e3c2`  |
| 3275   | Layout 1 | `cb430810e3c2`  |
| 3267   | Layout 1 | `cb430810e3c2`  |
| 3258   | Layout 1 | `cb430810e3c2`  |
| 3251   | Layout 1 | `cb430810e3c2`  |
| 3242   | Layout 1 | `cb430810e3c2`  |
| 3235   | Layout 1 | `cb430810e3c2`  |
| 3229   | Layout 1 | `cb430810e3c2`  |
| 3212   | Layout 1 | `cb430810e3c2`  |
| 3203   | Layout 1 | `cb430810e3c2`  |
| 3193   | Layout 1 | `cb430810e3c2`  |
| 3186   | Layout 1 | `cb430810e3c2`  |
| 3177   | Layout 1 | `cb430810e3c2`  |
| 3169   | Layout 1 | `cb430810e3c2`  |
| 3158   | Layout 1 | `cb430810e3c2`  |
| 3151   | Layout 1 | `cb430810e3c2`  |
| 3144   | Layout 1 | `cb430810e3c2`  |
| 3133   | Layout 1 | `cb430810e3c2`  |
| 3125   | Layout 1 | `cb430810e3c2`  |
| 3118   | Layout 1 | `cb430810e3c2`  |
| 3111   | Layout 1 | `cb430810e3c2`  |
| 3103   | Layout 1 | `cb430810e3c2`  |
| 3095   | Layout 1 | `cb430810e3c2`  |
| 3086   | Layout 1 | `cb430810e3c2`  |
| 3072   | Layout 1 | `cb430810e3c2`  |
| 3062   | Layout 1 | `cb430810e3c2`  |
| 3052   | Layout 1 | `cb430810e3c2`  |
| 3045   | Layout 1 | `cb430810e3c2`  |
| 3037   | Layout 1 | `cb430810e3c2`  |
| 3030   | Layout 1 | `cb430810e3c2`  |
| 3021   | Layout 1 | `cb430810e3c2`  |
| 3012   | Layout 1 | `cb430810e3c2`  |
| 3002   | Layout 1 | `cb430810e3c2`  |
| 2995   | Layout 1 | `cb430810e3c2`  |
| 2987   | Layout 1 | `cb430810e3c2`  |
| 2978   | Layout 1 | `cb430810e3c2`  |
| 2970   | Layout 1 | `cb430810e3c2`  |
| 2959   | Layout 1 | `cb430810e3c2`  |
| 2951   | Layout 1 | `cb430810e3c2`  |
| 2942   | Layout 1 | `cb430810e3c2`  |
| 2935   | Layout 1 | `cb430810e3c2`  |
| 2932   | Layout 1 | `cb430810e3c2`  |
| 2923   | Layout 1 | `cb430810e3c2`  |
| 2919   | Layout 1 | `cb430810e3c2`  |
| 2907   | Layout 1 | `cb430810e3c2`  |
| 2900   | Layout 1 | `cb430810e3c2`  |
| 2891   | Layout 1 | `cb430810e3c2`  |
| 2882   | Layout 1 | `cb430810e3c2`  |
| 2872   | Layout 1 | `cb430810e3c2`  |
| 2863   | Layout 1 | `cb430810e3c2`  |
| 2855   | Layout 1 | `cb430810e3c2`  |
| 2849   | Layout 1 | `cb430810e3c2`  |
| 2844   | Layout 1 | `cb430810e3c2`  |
| 2834   | Layout 1 | `cb430810e3c2`  |
| 2825   | No file  | `cb430810e3c2`  |
| 2819   | No file  | `cb430810e3c2`  |
| 2811   | No file  | `cb430810e3c2`  |
| 2803   | No file  | `cb430810e3c2`  |
| 2794   | No file  | `cb430810e3c2`  |
| 2783   | No file  | `cb430810e3c2`  |
| 2774   | No file  | `cb430810e3c2`  |
| 2765   | No file  | `cb430810e3c2`  |
| 2756   | No file  | `cb430810e3c2`  |
| 2750   | No file  | `cb430810e3c2`  |
| 2743   | No file  | `cb430810e3c2`  |
| 2736   | No file  | `cb430810e3c2`  |
| 2726   | No file  | `cb430810e3c2`  |
| 2717   | No file  | `cb430810e3c2`  |
| 2709   | No file  | `cb430810e3c2`  |
| 2703   | No file  | `cb430810e3c2`  |
| 2695   | No file  | `cb430810e3c2`  |
| 2684   | No file  | `cb430810e3c2`  |
| 2672   | No file  | `cb430810e3c2`  |
| 2665   | No file  | `cb430810e3c2`  |
| 2657   | No file  | `cb430810e3c2`  |
| 2649   | No file  | `cb430810e3c2`  |
| 2644   | No file  | `cb430810e3c2`  |
| 2637   | No file  | `cb430810e3c2`  |
| 2629   | No file  | `cb430810e3c2`  |
| 2619   | No file  | `cb430810e3c2`  |
| 2612   | No file  | `cb430810e3c2`  |
| 2606   | No file  | `cb430810e3c2`  |
| 2602   | No file  | `cb430810e3c2`  |
| 2601   | No file  | `cb430810e3c2`  |
| 2592   | No file  | `cb430810e3c2`  |
| 2583   | No file  | `cb430810e3c2`  |
| 2575   | No file  | `cb430810e3c2`  |
| 2567   | No file  | `cb430810e3c2`  |
| 2560   | No file  | `cb430810e3c2`  |
| 2553   | No file  | `cb430810e3c2`  |
| 2545   | No file  | `cb430810e3c2`  |
| 2538   | No file  | `cb430810e3c2`  |
| 2529   | No file  | `cb430810e3c2`  |
| 2519   | No file  | `cb430810e3c2`  |
| 2513   | No file  | `cb430810e3c2`  |
| 2510   | No file  | `cb430810e3c2`  |
| 2507   | No file  | `cb430810e3c2`  |
| 2503   | No file  | `cb430810e3c2`  |
| 2498   | No file  | `cb430810e3c2`  |
| 2492   | No file  | `cb430810e3c2`  |
| 2487   | No file  | `cb430810e3c2`  |
| 2480   | No file  | `cb430810e3c2`  |
| 2474   | No file  | `cb430810e3c2`  |
| 2468   | No file  | `cb430810e3c2`  |
| 2460   | No file  | `cb430810e3c2`  |
| 2453   | No file  | `cb430810e3c2`  |
| 2444   | No file  | `cb430810e3c2`  |
| 2438   | No file  | `cb430810e3c2`  |
| 2434   | No file  | `cb430810e3c2`  |
| 2429   | No file  | `cb430810e3c2`  |
| 2421   | No file  | `cb430810e3c2`  |
| 2414   | No file  | `cb430810e3c2`  |
| 2407   | No file  | `cb430810e3c2`  |
| 2401   | No file  | `cb430810e3c2`  |
| 2397   | No file  | `cb430810e3c2`  |
| 2393   | No file  | `cb430810e3c2`  |
| 2384   | No file  | `cb430810e3c2`  |
| 2378   | No file  | `cb430810e3c2`  |
| 2372   | No file  | `cb430810e3c2`  |
| 2358   | No file  | `cb430810e3c2`  |
| 2352   | No file  | `cb430810e3c2`  |
| 2347   | No file  | `cb430810e3c2`  |
| 2343   | No file  | `cb430810e3c2`  |
| 2335   | No file  | `cb430810e3c2`  |
| 2327   | No file  | `cb430810e3c2`  |
| 2324   | No file  | `cb430810e3c2`  |
| 2319   | No file  | `cb430810e3c2`  |
| 2313   | No file  | `cb430810e3c2`  |
| 2308   | No file  | `cb430810e3c2`  |
| 2302   | No file  | `cb430810e3c2`  |
| 2295   | No file  | `cb430810e3c2`  |
| 2290   | No file  | `cb430810e3c2`  |
| 2284   | No file  | `cb430810e3c2`  |
| 2276   | No file  | `cb430810e3c2`  |
| 2269   | No file  | `cb430810e3c2`  |
| 2259   | No file  | `cb430810e3c2`  |
| 2250   | No file  | `cb430810e3c2`  |
| 2243   | No file  | `cb430810e3c2`  |
| 2235   | No file  | `cb430810e3c2`  |
| 2229   | No file  | `cb430810e3c2`  |
| 2224   | No file  | `cb430810e3c2`  |
| 2218   | No file  | `cb430810e3c2`  |
| 2215   | No file  | `cb430810e3c2`  |
| 2207   | No file  | `cb430810e3c2`  |
| 2203   | No file  | `cb430810e3c2`  |
| 2196   | No file  | `cb430810e3c2`  |
| 2192   | No file  | `cb430810e3c2`  |
| 2189   | No file  | `cb430810e3c2`  |
| 2183   | No file  | `cb430810e3c2`  |
| 2179   | No file  | `cb430810e3c2`  |
| 2171   | No file  | `cb430810e3c2`  |
| 2163   | No file  | `cb430810e3c2`  |
| 2156   | No file  | `cb430810e3c2`  |
| 2151   | No file  | `cb430810e3c2`  |
| 2147   | No file  | `cb430810e3c2`  |
| 2142   | No file  | `cb430810e3c2`  |
| 2138   | No file  | `cb430810e3c2`  |
| 2134   | No file  | `cb430810e3c2`  |
| 2130   | No file  | `cb430810e3c2`  |
| 2122   | No file  | `cb430810e3c2`  |
| 2107   | No file  | `cb430810e3c2`  |
| 2098   | No file  | `cb430810e3c2`  |
| 2089   | No file  | `cb430810e3c2`  |
| 2081   | No file  | `cb430810e3c2`  |
| 2073   | No file  | `cb430810e3c2`  |
| 2067   | No file  | `cb430810e3c2`  |
| 2063   | No file  | `cb430810e3c2`  |
| 2059   | No file  | `cb430810e3c2`  |
| 2052   | No file  | `cb430810e3c2`  |
| 2044   | No file  | `cb430810e3c2`  |
| 2039   | No file  | `cb430810e3c2`  |
| 2032   | No file  | `cb430810e3c2`  |
| 2025   | No file  | `cb430810e3c2`  |
| 2011   | No file  | `cb430810e3c2`  |
| 2005   | No file  | `cb430810e3c2`  |
| 2000   | No file  | `cb430810e3c2`  |
| 1996   | No file  | `cb430810e3c2`  |
| 1991   | No file  | `cb430810e3c2`  |
| 1985   | No file  | `cb430810e3c2`  |
| 1980   | No file  | `cb430810e3c2`  |
| 1969   | No file  | `cb430810e3c2`  |
| 1964   | No file  | `cb430810e3c2`  |
| 1958   | No file  | `cb430810e3c2`  |
| 1950   | No file  | `cb430810e3c2`  |
| 1945   | No file  | `cb430810e3c2`  |
| 1937   | No file  | `cb430810e3c2`  |
| 1933   | No file  | `cb430810e3c2`  |
| 1927   | No file  | `cb430810e3c2`  |
| 1921   | No file  | `cb430810e3c2`  |
| 1914   | No file  | `cb430810e3c2`  |
| 1908   | No file  | `cb430810e3c2`  |
| 1897   | No file  | `cb430810e3c2`  |
| 1892   | No file  | `cb430810e3c2`  |
| 1886   | No file  | `cb430810e3c2`  |
| 1881   | No file  | `cb430810e3c2`  |
| 1871   | No file  | `cb430810e3c2`  |
| 1866   | No file  | `cb430810e3c2`  |
| 1862   | No file  | `cb430810e3c2`  |
| 1854   | No file  | `cb430810e3c2`  |
| 1846   | No file  | `cb430810e3c2`  |
| 1838   | No file  | `cb430810e3c2`  |
| 1832   | No file  | `cb430810e3c2`  |
| 1826   | No file  | `cb430810e3c2`  |
| 1822   | No file  | `cb430810e3c2`  |
| 1818   | No file  | `cb430810e3c2`  |
| 1804   | No file  | `cb430810e3c2`  |
| 1794   | No file  | `cb430810e3c2`  |
| 1790   | No file  | `cb430810e3c2`  |
| 1784   | No file  | `cb430810e3c2`  |
| 1774   | No file  | `cb430810e3c2`  |
| 1771   | No file  | `cb430810e3c2`  |
| 1762   | No file  | `cb430810e3c2`  |
| 1759   | No file  | `cb430810e3c2`  |
| 1754   | No file  | `cb430810e3c2`  |
| 1749   | No file  | `cb430810e3c2`  |
| 1743   | No file  | `cb430810e3c2`  |
| 1737   | No file  | `cb430810e3c2`  |
| 1731   | No file  | `cb430810e3c2`  |
| 1725   | No file  | `cb430810e3c2`  |
| 1717   | No file  | `cb430810e3c2`  |
| 1710   | No file  | `cb430810e3c2`  |
| 1704   | No file  | `cb430810e3c2`  |
| 1698   | No file  | `cb430810e3c2`  |
| 1690   | No file  | `cb430810e3c2`  |
| 1685   | No file  | `cb430810e3c2`  |
| 1680   | No file  | `cb430810e3c2`  |
| 1674   | No file  | `cb430810e3c2`  |
| 1668   | No file  | `cb430810e3c2`  |
| 1659   | No file  | `cb430810e3c2`  |
| 1649   | No file  | `cb430810e3c2`  |
| 1642   | No file  | `cb430810e3c2`  |
| 1636   | No file  | `cb430810e3c2`  |
| 1628   | No file  | `cb430810e3c2`  |
| 1622   | No file  | `cb430810e3c2`  |
| 1614   | No file  | `cb430810e3c2`  |
| 1608   | No file  | `cb430810e3c2`  |
| 1602   | No file  | `cb430810e3c2`  |
| 1598   | No file  | `cb430810e3c2`  |
| 1594   | No file  | `cb430810e3c2`  |
| 1590   | No file  | `cb430810e3c2`  |
| 1587   | No file  | `cb430810e3c2`  |
| 1584   | No file  | `cb430810e3c2`  |
| 1579   | No file  | `cb430810e3c2`  |
| 1572   | No file  | `cb430810e3c2`  |
| 1565   | No file  | `cb430810e3c2`  |
| 1559   | No file  | `cb430810e3c2`  |
| 1554   | No file  | `cb430810e3c2`  |
| 1547   | No file  | `cb430810e3c2`  |
| 1537   | No file  | `cb430810e3c2`  |
| 1529   | No file  | `cb430810e3c2`  |
| 1524   | No file  | `cb430810e3c2`  |
| 1519   | No file  | `cb430810e3c2`  |
| 1509   | No file  | `cb430810e3c2`  |
| 1506   | No file  | `cb430810e3c2`  |
| 1504   | No file  | `cb430810e3c2`  |
| 1500   | No file  | `cb430810e3c2`  |
| 1493   | No file  | `cb430810e3c2`  |
| 1489   | No file  | `cb430810e3c2`  |
| 1485   | No file  | `cb430810e3c2`  |
| 1481   | No file  | `cb430810e3c2`  |
| 1474   | No file  | `cb430810e3c2`  |
| 1466   | No file  | `cb430810e3c2`  |
| 1462   | No file  | `cb430810e3c2`  |
| 1459   | No file  | `cb430810e3c2`  |
| 1453   | No file  | `cb430810e3c2`  |
| 1450   | No file  | `cb430810e3c2`  |
| 1445   | No file  | `cb430810e3c2`  |
| 1439   | No file  | `cb430810e3c2`  |
| 1433   | No file  | `cb430810e3c2`  |
| 1430   | No file  | `cb430810e3c2`  |
| 1426   | No file  | `cb430810e3c2`  |
| 1421   | No file  | `cb430810e3c2`  |
| 1417   | No file  | `cb430810e3c2`  |
| 1416   | No file  | `cb430810e3c2`  |
| 1409   | No file  | `cb430810e3c2`  |
| 1405   | No file  | `cb430810e3c2`  |
| 1401   | No file  | `cb430810e3c2`  |
| 1396   | No file  | `cb430810e3c2`  |
| 1391   | No file  | `cb430810e3c2`  |
| 1390   | No file  | `cb430810e3c2`  |
| 1386   | No file  | `cb430810e3c2`  |
| 1381   | No file  | `cb430810e3c2`  |
| 1379   | No file  | `cb430810e3c2`  |
| 1372   | No file  | `cb430810e3c2`  |
| 1366   | No file  | `cb430810e3c2`  |
| 1364   | No file  | `cb430810e3c2`  |
| 1363   | No file  | `cb430810e3c2`  |
| 1360   | No file  | `cb430810e3c2`  |
| 1358   | No file  | `cb430810e3c2`  |
| 1355   | No file  | `cb430810e3c2`  |
| 1351   | No file  | `cb430810e3c2`  |
| 1348   | No file  | `cb430810e3c2`  |
| 1346   | No file  | `cb430810e3c2`  |
| 1341   | No file  | `cb430810e3c2`  |
| 1340   | No file  | `cb430810e3c2`  |
| 1338   | No file  | `cb430810e3c2`  |
| 1335   | No file  | `cb430810e3c2`  |
| 1333   | No file  | `cb430810e3c2`  |
| 1329   | No file  | `cb430810e3c2`  |
| 1327   | No file  | `cb430810e3c2`  |
| 1324   | No file  | `cb430810e3c2`  |
| 1321   | No file  | `cb430810e3c2`  |
| 1319   | No file  | `cb430810e3c2`  |
| 1318   | No file  | `cb430810e3c2`  |
| 1316   | No file  | `cb430810e3c2`  |
| 1313   | No file  | `cb430810e3c2`  |
| 1311   | No file  | `cb430810e3c2`  |
| 1309   | No file  | `cb430810e3c2`  |
| 1304   | No file  | `cb430810e3c2`  |
| 1292   | No file  | `cb430810e3c2`  |
| 1286   | No file  | `cb430810e3c2`  |
| 1280   | No file  | `cb430810e3c2`  |
| 1276   | No file  | `cb430810e3c2`  |
| 1267   | No file  | `cb430810e3c2`  |
| 1261   | No file  | `cb430810e3c2`  |
| 1256   | No file  | `cb430810e3c2`  |
| 1250   | No file  | `cb430810e3c2`  |
| 1246   | No file  | `cb430810e3c2`  |
| 1239   | No file  | `cb430810e3c2`  |
| 1230   | No file  | `cb430810e3c2`  |
| 1226   | No file  | `cb430810e3c2`  |
| 1220   | No file  | `cb430810e3c2`  |
| 1217   | No file  | `cb430810e3c2`  |
| 1211   | No file  | `cb430810e3c2`  |
| 1210   | No file  | `cb430810e3c2`  |
| 1208   | No file  | `cb430810e3c2`  |
| 1203   | No file  | `cb430810e3c2`  |
| 1197   | No file  | `cb430810e3c2`  |
| 1194   | No file  | `cb430810e3c2`  |
| 1192   | No file  | `cb430810e3c2`  |
| 1187   | No file  | `cb430810e3c2`  |
| 1183   | No file  | `cb430810e3c2`  |
| 1177   | No file  | `cb430810e3c2`  |
| 1173   | No file  | `cb430810e3c2`  |
| 1167   | No file  | `cb430810e3c2`  |
| 1164   | No file  | `cb430810e3c2`  |
| 1156   | No file  | `cb430810e3c2`  |
| 1149   | No file  | `cb430810e3c2`  |
| 1144   | No file  | `cb430810e3c2`  |
| 1137   | No file  | `cb430810e3c2`  |
| 1132   | No file  | `cb430810e3c2`  |
| 1127   | No file  | `cb430810e3c2`  |
| 1122   | No file  | `cb430810e3c2`  |
| 1118   | No file  | `cb430810e3c2`  |
| 1114   | No file  | `cb430810e3c2`  |
| 1109   | No file  | `cb430810e3c2`  |
| 1102   | No file  | `cb430810e3c2`  |
| 1096   | No file  | `cb430810e3c2`  |
| 1088   | No file  | `cb430810e3c2`  |
| 1081   | No file  | `cb430810e3c2`  |
| 1076   | No file  | `cb430810e3c2`  |
| 1069   | No file  | `cb430810e3c2`  |
| 1064   | No file  | `cb430810e3c2`  |
| 1058   | No file  | `cb430810e3c2`  |
| 1051   | No file  | `cb430810e3c2`  |
| 1044   | No file  | `cb430810e3c2`  |
| 1036   | No file  | `cb430810e3c2`  |
| 1026   | No file  | `cb430810e3c2`  |
| 1016   | No file  | `cb430810e3c2`  |
| 1009   | No file  | `cb430810e3c2`  |
| 1005   | No file  | `cb430810e3c2`  |
| 1000   | No file  | `cb430810e3c2`  |
| 998    | No file  | `cb430810e3c2`  |
| 990    | No file  | `cb430810e3c2`  |
| 979    | No file  | `cb430810e3c2`  |
| 972    | No file  | `cb430810e3c2`  |
| 963    | No file  | `cb430810e3c2`  |
| 955    | No file  | `cb430810e3c2`  |
| 946    | No file  | `cb430810e3c2`  |
| 938    | No file  | `cb430810e3c2`  |
| 927    | No file  | `cb430810e3c2`  |
| 911    | No file  | `cb430810e3c2`  |
| 904    | No file  | `cb430810e3c2`  |
| 899    | No file  | `cb430810e3c2`  |
| 894    | No file  | `cb430810e3c2`  |
| 885    | No file  | `cb430810e3c2`  |
| 879    | No file  | `cb430810e3c2`  |
| 872    | No file  | `cb430810e3c2`  |
| 864    | No file  | `cb430810e3c2`  |
| 855    | No file  | `cb430810e3c2`  |
| 853    | No file  | `cb430810e3c2`  |
| 845    | No file  | `cb430810e3c2`  |
| 837    | No file  | `cb430810e3c2`  |
| 829    | No file  | `cb430810e3c2`  |
| 822    | No file  | `cb430810e3c2`  |
| 814    | No file  | `cb430810e3c2`  |
| 805    | No file  | `cb430810e3c2`  |
| 794    | No file  | `cb430810e3c2`  |
| 787    | No file  | `cb430810e3c2`  |
| 780    | No file  | `cb430810e3c2`  |
| 771    | No file  | `cb430810e3c2`  |
| 760    | No file  | `cb430810e3c2`  |
| 748    | No file  | `cb430810e3c2`  |
| 741    | No file  | `cb430810e3c2`  |
| 736    | No file  | `cb430810e3c2`  |
| 731    | No file  | `cb430810e3c2`  |
| 723    | No file  | `cb430810e3c2`  |
| 711    | No file  | `cb430810e3c2`  |
| 707    | No file  | `cb430810e3c2`  |
| 697    | No file  | `cb430810e3c2`  |
| 689    | No file  | `cb430810e3c2`  |
| 683    | No file  | `cb430810e3c2`  |
| 678    | No file  | `cb430810e3c2`  |
| 670    | No file  | `cb430810e3c2`  |
| 661    | No file  | `cb430810e3c2`  |
| 656    | No file  | `cb430810e3c2`  |
| 652    | No file  | `cb430810e3c2`  |
| 643    | No file  | `cb430810e3c2`  |
| 637    | No file  | `cb430810e3c2`  |
| 630    | No file  | `cb430810e3c2`  |
| 627    | No file  | `cb430810e3c2`  |
| 621    | No file  | `cb430810e3c2`  |
| 617    | No file  | `cb430810e3c2`  |
| 615    | No file  | `cb430810e3c2`  |
| 606    | No file  | `cb430810e3c2`  |
| 599    | No file  | `cb430810e3c2`  |
| 592    | No file  | `cb430810e3c2`  |
| 586    | No file  | `cb430810e3c2`  |
| 577    | No file  | `cb430810e3c2`  |
| 569    | No file  | `cb430810e3c2`  |
| 561    | No file  | `cb430810e3c2`  |
| 554    | No file  | `cb430810e3c2`  |
| 542    | No file  | `cb430810e3c2`  |
| 532    | No file  | `cb430810e3c2`  |
| 531    | No file  | `cb430810e3c2`  |
| 526    | No file  | `cb430810e3c2`  |
| 521    | No file  | `cb430810e3c2`  |
| 517    | No file  | `cb430810e3c2`  |
| 510    | No file  | `cb430810e3c2`  |
| 508    | No file  | `cb430810e3c2`  |
| 504    | No file  | `cb430810e3c2`  |
| 497    | No file  | `cb430810e3c2`  |
| 491    | No file  | `cb430810e3c2`  |
| 485    | No file  | `cb430810e3c2`  |
| 478    | No file  | `cb430810e3c2`  |
| 472    | No file  | `cb430810e3c2`  |
| 466    | No file  | `cb430810e3c2`  |
| 457    | No file  | `cb430810e3c2`  |
| 452    | No file  | `cb430810e3c2`  |
| 449    | No file  | `cb430810e3c2`  |
| 435    | No file  | `cb430810e3c2`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (9 bytes)

| Offset  | Type     | Field      | Notes                                                                                   |
| ------- | -------- | ---------- | --------------------------------------------------------------------------------------- |
| `+0x00` | bytes[3] | map_color  | Region map colour, stored blue, green, red; unique per row. See Map Colours             |
| `+0x03` | u8       | unknown_03 | Always `0`                                                                              |
| `+0x04` | bytes[3] | unknown_04 | Equals `map_color` on every row                                                         |
| `+0x07` | u8       | unknown_07 | Always `0`                                                                              |
| `+0x08` | u8       | unknown_08 | `0` to `4`; several rows share a value. See Open Questions                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Map Colours

`map_color` read as `rrggbb`, with `unknown_08`, in file order (client
3474). The `.rid` order is the order of the region map's palette file.

| `map_color` | `unknown_08` | Position in `hardcorechannelmap.bmp.rid` |
| ----------- | ------------ | ---------------------------------------- |
| `ff14ff`    | `3`          | 4                                        |
| `14ff14`    | `3`          | 9                                        |
| `ffff14`    | `3`          | 12                                       |
| `14ffff`    | `3`          | 13                                       |
| `c800ff`    | `4`          | 11                                       |
| `6414ff`    | `3`          | 6                                        |
| `1464ff`    | `3`          | 10                                       |
| `c80000`    | `4`          | 8                                        |
| `c8c800`    | `4`          | 5                                        |
| `00c8ff`    | `4`          | 14                                       |
| `000096`    | `4`          | 3                                        |
| `009696`    | `4`          | 7                                        |
| `6464ff`    | `2`          | 15                                       |
| `181be8`    | `1`          | 2                                        |
| `100d10`    | `0`          | 1                                        |

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. `map_color` follows the region map files.
The client has one `<name>map.bmp.bkd` and `<name>map.bmp.rid` pair per
region map in `ui_texture/minimap/area/`, and each `.rid` is a PABR file
holding a u32 count and that many 4-byte colours (the 3 colour bytes and a
zero byte, in this file's byte order). On client 3474 four `.rid` files list
exactly the colours of the four 9-byte-row tables:

| Map file                  | Colours | Table                                                  |
| ------------------------- | ------- | ------------------------------------------------------ |
| `hardcorechannelmap.bmp`  | 15      | `hardcorechannelinfo.bss`                              |
| `edaniaregionmap.bmp`     | 11      | [`edaniaregioninfo.bss`](edaniaregioninfo_bss.md)       |
| `elfwar_siegemap.bmp`     | 2       | [`rosewarinfo.bss`](rosewarinfo_bss.md) (the Rose War is `ElfWar` in the client's file names) |
| `snowboardcoursemap.bmp`  | 2       | [`snowboardcourseinfo.bss`](snowboardcourseinfo_bss.md) |

Every `.rid` lists `10 0D 10` first. This file, `rosewarinfo.bss` and
`snowboardcourseinfo.bss` give it the u8 `0`, `edaniaregioninfo.bss` the
`_Count` value `10` ("no Edania region").

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- The `rosewarinfo.bss` row `E8 1B 18` with `1` and the shared `10 0D 10`
  row with `0` are the last two rows here as well.
- Only `000096` equals a `regioninfo.bss` `color`, that of region 264
  (Epheria Valley).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/hardcore_tables.py`:
  `map_color` as `rrggbb`.

## Open Questions

### The Value of Each Colour

What `unknown_08` stands for. The client Lua of client 3474 checks the
player's area with `ToClient_HardCoreSelfplayerRegionCheck(__eHardCoreChannelRegionSafe)`
(`ui_widget_skillcommand.luac`), so the value may be an
`__eHardCoreChannelRegion*` area type, but `Safe` is the only member the Lua
names and none of the values. Five rows hold `3`, seven `4`, one each `0`,
`1` and `2`.

### Why the Colour Is Stored Twice

`unknown_04` equals `map_color` on every row, as the second copy does in
the three other 9-byte-row tables, and `unknown_03` and `unknown_07` are
always `0`. No source names the copy.
