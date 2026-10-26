# `*.pcm` Simple Mesh Format

## Purpose

A triangle mesh with positions only: no materials, texture names or UVs. On client 3483, 14,281 of the 14,319 `.pcm` files sit next to a [`*.pam`](mesh_pam.md) of the same path under `object/`, and 14,156 of 14,280 of those hold fewer triangles than their `.pam`. sibercat/PAZ-Unpacker reads them as collision hulls; that use is not confirmed here. The Model tab of the browser draws them untextured (`PAZ-Parser/par_mesh.py`). Byte `0x04` of the `PAR ` header is `0x11`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | -------------------- | ----- | ------- | --------- |
| 1      | 3483 and later | `ex_ogremine_01.pcm` | 2,004 | -       | -         |

| Layout | File                 | Known           | Unknown     |
| ------ | -------------------- | --------------- | ----------- |
| 1      | `ex_ogremine_01.pcm` | 1,994 B (99.5%) | 10 B (0.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6d252fa3b696`  |
| 3482   | No file  | `6d252fa3b696`  |
| 3474   | No file  | `6d252fa3b696`  |
| 3473   | No file  | `6d252fa3b696`  |
| 3464   | No file  | `6d252fa3b696`  |
| 3458   | No file  | `6d252fa3b696`  |
| 3454   | No file  | `6d252fa3b696`  |
| 3444   | No file  | `6d252fa3b696`  |
| 3435   | No file  | `6d252fa3b696`  |
| 3426   | No file  | `6d252fa3b696`  |
| 3418   | No file  | `6d252fa3b696`  |
| 3412   | No file  | `6d252fa3b696`  |
| 3402   | No file  | `6d252fa3b696`  |
| 3396   | No file  | `6d252fa3b696`  |
| 3387   | No file  | `6d252fa3b696`  |
| 3381   | No file  | `6d252fa3b696`  |
| 3373   | No file  | `6d252fa3b696`  |
| 3364   | No file  | `6d252fa3b696`  |
| 3356   | No file  | `6d252fa3b696`  |
| 3349   | No file  | `6d252fa3b696`  |
| 3342   | No file  | `6d252fa3b696`  |
| 3335   | No file  | `6d252fa3b696`  |
| 3326   | No file  | `6d252fa3b696`  |
| 3321   | No file  | `6d252fa3b696`  |
| 3314   | No file  | `6d252fa3b696`  |
| 3303   | No file  | `6d252fa3b696`  |
| 3302   | No file  | `6d252fa3b696`  |
| 3293   | No file  | `6d252fa3b696`  |
| 3283   | No file  | `6d252fa3b696`  |
| 3275   | No file  | `6d252fa3b696`  |
| 3267   | No file  | `6d252fa3b696`  |
| 3258   | No file  | `6d252fa3b696`  |
| 3251   | No file  | `6d252fa3b696`  |
| 3242   | No file  | `6d252fa3b696`  |
| 3235   | No file  | `6d252fa3b696`  |
| 3229   | No file  | `6d252fa3b696`  |
| 3212   | No file  | `6d252fa3b696`  |
| 3203   | No file  | `6d252fa3b696`  |
| 3193   | No file  | `6d252fa3b696`  |
| 3186   | No file  | `6d252fa3b696`  |
| 3177   | No file  | `6d252fa3b696`  |
| 3169   | No file  | `6d252fa3b696`  |
| 3158   | No file  | `6d252fa3b696`  |
| 3151   | No file  | `6d252fa3b696`  |
| 3144   | No file  | `6d252fa3b696`  |
| 3133   | No file  | `6d252fa3b696`  |
| 3125   | No file  | `6d252fa3b696`  |
| 3118   | No file  | `6d252fa3b696`  |
| 3111   | No file  | `6d252fa3b696`  |
| 3103   | No file  | `6d252fa3b696`  |
| 3095   | No file  | `6d252fa3b696`  |
| 3086   | No file  | `6d252fa3b696`  |
| 3072   | No file  | `6d252fa3b696`  |
| 3062   | No file  | `6d252fa3b696`  |
| 3052   | No file  | `6d252fa3b696`  |
| 3045   | No file  | `6d252fa3b696`  |
| 3037   | No file  | `6d252fa3b696`  |
| 3030   | No file  | `6d252fa3b696`  |
| 3021   | No file  | `6d252fa3b696`  |
| 3012   | No file  | `6d252fa3b696`  |
| 3002   | No file  | `6d252fa3b696`  |
| 2995   | No file  | `6d252fa3b696`  |
| 2987   | No file  | `6d252fa3b696`  |
| 2978   | No file  | `6d252fa3b696`  |
| 2970   | No file  | `6d252fa3b696`  |
| 2959   | No file  | `6d252fa3b696`  |
| 2951   | No file  | `6d252fa3b696`  |
| 2942   | No file  | `6d252fa3b696`  |
| 2935   | No file  | `6d252fa3b696`  |
| 2932   | No file  | `6d252fa3b696`  |
| 2923   | No file  | `6d252fa3b696`  |
| 2919   | No file  | `6d252fa3b696`  |
| 2907   | No file  | `6d252fa3b696`  |
| 2900   | No file  | `6d252fa3b696`  |
| 2891   | No file  | `6d252fa3b696`  |
| 2882   | No file  | `6d252fa3b696`  |
| 2872   | No file  | `6d252fa3b696`  |
| 2863   | No file  | `6d252fa3b696`  |
| 2855   | No file  | `6d252fa3b696`  |
| 2849   | No file  | `6d252fa3b696`  |
| 2844   | No file  | `6d252fa3b696`  |
| 2834   | No file  | `6d252fa3b696`  |
| 2825   | No file  | `6d252fa3b696`  |
| 2819   | No file  | `6d252fa3b696`  |
| 2811   | No file  | `6d252fa3b696`  |
| 2803   | No file  | `6d252fa3b696`  |
| 2794   | No file  | `6d252fa3b696`  |
| 2783   | No file  | `6d252fa3b696`  |
| 2774   | No file  | `6d252fa3b696`  |
| 2765   | No file  | `6d252fa3b696`  |
| 2756   | No file  | `6d252fa3b696`  |
| 2750   | No file  | `6d252fa3b696`  |
| 2743   | No file  | `6d252fa3b696`  |
| 2736   | No file  | `6d252fa3b696`  |
| 2726   | No file  | `6d252fa3b696`  |
| 2717   | No file  | `6d252fa3b696`  |
| 2709   | No file  | `6d252fa3b696`  |
| 2703   | No file  | `6d252fa3b696`  |
| 2695   | No file  | `6d252fa3b696`  |
| 2684   | No file  | `6d252fa3b696`  |
| 2672   | No file  | `6d252fa3b696`  |
| 2665   | No file  | `6d252fa3b696`  |
| 2657   | No file  | `6d252fa3b696`  |
| 2649   | No file  | `6d252fa3b696`  |
| 2644   | No file  | `6d252fa3b696`  |
| 2637   | No file  | `6d252fa3b696`  |
| 2629   | No file  | `6d252fa3b696`  |
| 2619   | No file  | `6d252fa3b696`  |
| 2612   | No file  | `6d252fa3b696`  |
| 2606   | No file  | `6d252fa3b696`  |
| 2602   | No file  | `6d252fa3b696`  |
| 2601   | No file  | `6d252fa3b696`  |
| 2592   | No file  | `6d252fa3b696`  |
| 2583   | No file  | `6d252fa3b696`  |
| 2575   | No file  | `6d252fa3b696`  |
| 2567   | No file  | `6d252fa3b696`  |
| 2560   | No file  | `6d252fa3b696`  |
| 2553   | No file  | `6d252fa3b696`  |
| 2545   | No file  | `6d252fa3b696`  |
| 2538   | No file  | `6d252fa3b696`  |
| 2529   | No file  | `6d252fa3b696`  |
| 2519   | No file  | `6d252fa3b696`  |
| 2513   | No file  | `6d252fa3b696`  |
| 2510   | No file  | `6d252fa3b696`  |
| 2507   | No file  | `6d252fa3b696`  |
| 2503   | No file  | `6d252fa3b696`  |
| 2498   | No file  | `6d252fa3b696`  |
| 2492   | No file  | `6d252fa3b696`  |
| 2487   | No file  | `6d252fa3b696`  |
| 2480   | No file  | `6d252fa3b696`  |
| 2474   | No file  | `6d252fa3b696`  |
| 2468   | No file  | `6d252fa3b696`  |
| 2460   | No file  | `6d252fa3b696`  |
| 2453   | No file  | `6d252fa3b696`  |
| 2444   | No file  | `6d252fa3b696`  |
| 2438   | No file  | `6d252fa3b696`  |
| 2434   | No file  | `6d252fa3b696`  |
| 2429   | No file  | `6d252fa3b696`  |
| 2421   | No file  | `6d252fa3b696`  |
| 2414   | No file  | `6d252fa3b696`  |
| 2407   | No file  | `6d252fa3b696`  |
| 2401   | No file  | `6d252fa3b696`  |
| 2397   | No file  | `6d252fa3b696`  |
| 2393   | No file  | `6d252fa3b696`  |
| 2384   | No file  | `6d252fa3b696`  |
| 2378   | No file  | `6d252fa3b696`  |
| 2372   | No file  | `6d252fa3b696`  |
| 2358   | No file  | `6d252fa3b696`  |
| 2352   | No file  | `6d252fa3b696`  |
| 2347   | No file  | `6d252fa3b696`  |
| 2343   | No file  | `6d252fa3b696`  |
| 2335   | No file  | `6d252fa3b696`  |
| 2327   | No file  | `6d252fa3b696`  |
| 2324   | No file  | `6d252fa3b696`  |
| 2319   | No file  | `6d252fa3b696`  |
| 2313   | No file  | `6d252fa3b696`  |
| 2308   | No file  | `6d252fa3b696`  |
| 2302   | No file  | `6d252fa3b696`  |
| 2295   | No file  | `6d252fa3b696`  |
| 2290   | No file  | `6d252fa3b696`  |
| 2284   | No file  | `6d252fa3b696`  |
| 2276   | No file  | `6d252fa3b696`  |
| 2269   | No file  | `6d252fa3b696`  |
| 2259   | No file  | `6d252fa3b696`  |
| 2250   | No file  | `6d252fa3b696`  |
| 2243   | No file  | `6d252fa3b696`  |
| 2235   | No file  | `6d252fa3b696`  |
| 2229   | No file  | `6d252fa3b696`  |
| 2224   | No file  | `6d252fa3b696`  |
| 2218   | No file  | `6d252fa3b696`  |
| 2215   | No file  | `6d252fa3b696`  |
| 2207   | No file  | `6d252fa3b696`  |
| 2203   | No file  | `6d252fa3b696`  |
| 2196   | No file  | `6d252fa3b696`  |
| 2192   | No file  | `6d252fa3b696`  |
| 2189   | No file  | `6d252fa3b696`  |
| 2183   | No file  | `6d252fa3b696`  |
| 2179   | No file  | `6d252fa3b696`  |
| 2171   | No file  | `6d252fa3b696`  |
| 2163   | No file  | `6d252fa3b696`  |
| 2156   | No file  | `6d252fa3b696`  |
| 2151   | No file  | `6d252fa3b696`  |
| 2147   | No file  | `6d252fa3b696`  |
| 2142   | No file  | `6d252fa3b696`  |
| 2138   | No file  | `6d252fa3b696`  |
| 2134   | No file  | `6d252fa3b696`  |
| 2130   | No file  | `6d252fa3b696`  |
| 2122   | No file  | `6d252fa3b696`  |
| 2107   | No file  | `6d252fa3b696`  |
| 2098   | No file  | `6d252fa3b696`  |
| 2089   | No file  | `6d252fa3b696`  |
| 2081   | No file  | `6d252fa3b696`  |
| 2073   | No file  | `6d252fa3b696`  |
| 2067   | No file  | `6d252fa3b696`  |
| 2063   | No file  | `6d252fa3b696`  |
| 2059   | No file  | `6d252fa3b696`  |
| 2052   | No file  | `6d252fa3b696`  |
| 2044   | No file  | `6d252fa3b696`  |
| 2039   | No file  | `6d252fa3b696`  |
| 2032   | No file  | `6d252fa3b696`  |
| 2025   | No file  | `6d252fa3b696`  |
| 2011   | No file  | `6d252fa3b696`  |
| 2005   | No file  | `6d252fa3b696`  |
| 2000   | No file  | `6d252fa3b696`  |
| 1996   | No file  | `6d252fa3b696`  |
| 1991   | No file  | `6d252fa3b696`  |
| 1985   | No file  | `6d252fa3b696`  |
| 1980   | No file  | `6d252fa3b696`  |
| 1969   | No file  | `6d252fa3b696`  |
| 1964   | No file  | `6d252fa3b696`  |
| 1958   | No file  | `6d252fa3b696`  |
| 1950   | No file  | `6d252fa3b696`  |
| 1945   | No file  | `6d252fa3b696`  |
| 1937   | No file  | `6d252fa3b696`  |
| 1933   | No file  | `6d252fa3b696`  |
| 1927   | No file  | `6d252fa3b696`  |
| 1921   | No file  | `6d252fa3b696`  |
| 1914   | No file  | `6d252fa3b696`  |
| 1908   | No file  | `6d252fa3b696`  |
| 1897   | No file  | `6d252fa3b696`  |
| 1892   | No file  | `6d252fa3b696`  |
| 1886   | No file  | `6d252fa3b696`  |
| 1881   | No file  | `6d252fa3b696`  |
| 1871   | No file  | `6d252fa3b696`  |
| 1866   | No file  | `6d252fa3b696`  |
| 1862   | No file  | `6d252fa3b696`  |
| 1854   | No file  | `6d252fa3b696`  |
| 1846   | No file  | `6d252fa3b696`  |
| 1838   | No file  | `6d252fa3b696`  |
| 1832   | No file  | `6d252fa3b696`  |
| 1826   | No file  | `6d252fa3b696`  |
| 1822   | No file  | `6d252fa3b696`  |
| 1818   | No file  | `6d252fa3b696`  |
| 1804   | No file  | `6d252fa3b696`  |
| 1794   | No file  | `6d252fa3b696`  |
| 1790   | No file  | `6d252fa3b696`  |
| 1784   | No file  | `6d252fa3b696`  |
| 1774   | No file  | `6d252fa3b696`  |
| 1771   | No file  | `6d252fa3b696`  |
| 1762   | No file  | `6d252fa3b696`  |
| 1759   | No file  | `6d252fa3b696`  |
| 1754   | No file  | `6d252fa3b696`  |
| 1749   | No file  | `6d252fa3b696`  |
| 1743   | No file  | `6d252fa3b696`  |
| 1737   | No file  | `6d252fa3b696`  |
| 1731   | No file  | `6d252fa3b696`  |
| 1725   | No file  | `6d252fa3b696`  |
| 1717   | No file  | `6d252fa3b696`  |
| 1710   | No file  | `6d252fa3b696`  |
| 1704   | No file  | `6d252fa3b696`  |
| 1698   | No file  | `6d252fa3b696`  |
| 1690   | No file  | `6d252fa3b696`  |
| 1685   | No file  | `6d252fa3b696`  |
| 1680   | No file  | `6d252fa3b696`  |
| 1674   | No file  | `6d252fa3b696`  |
| 1668   | No file  | `6d252fa3b696`  |
| 1659   | No file  | `6d252fa3b696`  |
| 1649   | No file  | `6d252fa3b696`  |
| 1642   | No file  | `6d252fa3b696`  |
| 1636   | No file  | `6d252fa3b696`  |
| 1628   | No file  | `6d252fa3b696`  |
| 1622   | No file  | `6d252fa3b696`  |
| 1614   | No file  | `6d252fa3b696`  |
| 1608   | No file  | `6d252fa3b696`  |
| 1602   | No file  | `6d252fa3b696`  |
| 1598   | No file  | `6d252fa3b696`  |
| 1594   | No file  | `6d252fa3b696`  |
| 1590   | No file  | `6d252fa3b696`  |
| 1587   | No file  | `6d252fa3b696`  |
| 1584   | No file  | `6d252fa3b696`  |
| 1579   | No file  | `6d252fa3b696`  |
| 1572   | No file  | `6d252fa3b696`  |
| 1565   | No file  | `6d252fa3b696`  |
| 1559   | No file  | `6d252fa3b696`  |
| 1554   | No file  | `6d252fa3b696`  |
| 1547   | No file  | `6d252fa3b696`  |
| 1537   | No file  | `6d252fa3b696`  |
| 1529   | No file  | `6d252fa3b696`  |
| 1524   | No file  | `6d252fa3b696`  |
| 1519   | No file  | `6d252fa3b696`  |
| 1509   | No file  | `6d252fa3b696`  |
| 1506   | No file  | `6d252fa3b696`  |
| 1504   | No file  | `6d252fa3b696`  |
| 1500   | No file  | `6d252fa3b696`  |
| 1493   | No file  | `6d252fa3b696`  |
| 1489   | No file  | `6d252fa3b696`  |
| 1485   | No file  | `6d252fa3b696`  |
| 1481   | No file  | `6d252fa3b696`  |
| 1474   | No file  | `6d252fa3b696`  |
| 1466   | No file  | `6d252fa3b696`  |
| 1462   | No file  | `6d252fa3b696`  |
| 1459   | No file  | `6d252fa3b696`  |
| 1453   | No file  | `6d252fa3b696`  |
| 1450   | No file  | `6d252fa3b696`  |
| 1445   | No file  | `6d252fa3b696`  |
| 1439   | No file  | `6d252fa3b696`  |
| 1433   | No file  | `6d252fa3b696`  |
| 1430   | No file  | `6d252fa3b696`  |
| 1426   | No file  | `6d252fa3b696`  |
| 1421   | No file  | `6d252fa3b696`  |
| 1417   | No file  | `6d252fa3b696`  |
| 1416   | No file  | `6d252fa3b696`  |
| 1409   | No file  | `6d252fa3b696`  |
| 1405   | No file  | `6d252fa3b696`  |
| 1401   | No file  | `6d252fa3b696`  |
| 1396   | No file  | `6d252fa3b696`  |
| 1391   | No file  | `6d252fa3b696`  |
| 1390   | No file  | `6d252fa3b696`  |
| 1386   | No file  | `6d252fa3b696`  |
| 1381   | No file  | `6d252fa3b696`  |
| 1379   | No file  | `6d252fa3b696`  |
| 1372   | No file  | `6d252fa3b696`  |
| 1366   | No file  | `6d252fa3b696`  |
| 1364   | No file  | `6d252fa3b696`  |
| 1363   | No file  | `6d252fa3b696`  |
| 1360   | No file  | `6d252fa3b696`  |
| 1358   | No file  | `6d252fa3b696`  |
| 1355   | No file  | `6d252fa3b696`  |
| 1351   | No file  | `6d252fa3b696`  |
| 1348   | No file  | `6d252fa3b696`  |
| 1346   | No file  | `6d252fa3b696`  |
| 1341   | No file  | `6d252fa3b696`  |
| 1340   | No file  | `6d252fa3b696`  |
| 1338   | No file  | `6d252fa3b696`  |
| 1335   | No file  | `6d252fa3b696`  |
| 1333   | No file  | `6d252fa3b696`  |
| 1329   | No file  | `6d252fa3b696`  |
| 1327   | No file  | `6d252fa3b696`  |
| 1324   | No file  | `6d252fa3b696`  |
| 1321   | No file  | `6d252fa3b696`  |
| 1319   | No file  | `6d252fa3b696`  |
| 1318   | No file  | `6d252fa3b696`  |
| 1316   | No file  | `6d252fa3b696`  |
| 1313   | No file  | `6d252fa3b696`  |
| 1311   | No file  | `6d252fa3b696`  |
| 1309   | No file  | `6d252fa3b696`  |
| 1304   | No file  | `6d252fa3b696`  |
| 1292   | No file  | `6d252fa3b696`  |
| 1286   | No file  | `6d252fa3b696`  |
| 1280   | No file  | `6d252fa3b696`  |
| 1276   | No file  | `6d252fa3b696`  |
| 1267   | No file  | `6d252fa3b696`  |
| 1261   | No file  | `6d252fa3b696`  |
| 1256   | No file  | `6d252fa3b696`  |
| 1250   | No file  | `6d252fa3b696`  |
| 1246   | No file  | `6d252fa3b696`  |
| 1239   | No file  | `6d252fa3b696`  |
| 1230   | No file  | `6d252fa3b696`  |
| 1226   | No file  | `6d252fa3b696`  |
| 1220   | No file  | `6d252fa3b696`  |
| 1217   | No file  | `6d252fa3b696`  |
| 1211   | No file  | `6d252fa3b696`  |
| 1210   | No file  | `6d252fa3b696`  |
| 1208   | No file  | `6d252fa3b696`  |
| 1203   | No file  | `6d252fa3b696`  |
| 1197   | No file  | `6d252fa3b696`  |
| 1194   | No file  | `6d252fa3b696`  |
| 1192   | No file  | `6d252fa3b696`  |
| 1187   | No file  | `6d252fa3b696`  |
| 1183   | No file  | `6d252fa3b696`  |
| 1177   | No file  | `6d252fa3b696`  |
| 1173   | No file  | `6d252fa3b696`  |
| 1167   | No file  | `6d252fa3b696`  |
| 1164   | No file  | `6d252fa3b696`  |
| 1156   | No file  | `6d252fa3b696`  |
| 1149   | No file  | `6d252fa3b696`  |
| 1144   | No file  | `6d252fa3b696`  |
| 1137   | No file  | `6d252fa3b696`  |
| 1132   | No file  | `6d252fa3b696`  |
| 1127   | No file  | `6d252fa3b696`  |
| 1122   | No file  | `6d252fa3b696`  |
| 1118   | No file  | `6d252fa3b696`  |
| 1114   | No file  | `6d252fa3b696`  |
| 1109   | No file  | `6d252fa3b696`  |
| 1102   | No file  | `6d252fa3b696`  |
| 1096   | No file  | `6d252fa3b696`  |
| 1088   | No file  | `6d252fa3b696`  |
| 1081   | No file  | `6d252fa3b696`  |
| 1076   | No file  | `6d252fa3b696`  |
| 1069   | No file  | `6d252fa3b696`  |
| 1064   | No file  | `6d252fa3b696`  |
| 1058   | No file  | `6d252fa3b696`  |
| 1051   | No file  | `6d252fa3b696`  |
| 1044   | No file  | `6d252fa3b696`  |
| 1036   | No file  | `6d252fa3b696`  |
| 1026   | No file  | `6d252fa3b696`  |
| 1016   | No file  | `6d252fa3b696`  |
| 1009   | No file  | `6d252fa3b696`  |
| 1005   | No file  | `6d252fa3b696`  |
| 1000   | No file  | `6d252fa3b696`  |
| 998    | No file  | `6d252fa3b696`  |
| 990    | No file  | `6d252fa3b696`  |
| 979    | No file  | `6d252fa3b696`  |
| 972    | No file  | `6d252fa3b696`  |
| 963    | No file  | `6d252fa3b696`  |
| 955    | No file  | `6d252fa3b696`  |
| 946    | No file  | `6d252fa3b696`  |
| 938    | No file  | `6d252fa3b696`  |
| 927    | No file  | `6d252fa3b696`  |
| 911    | No file  | `6d252fa3b696`  |
| 904    | No file  | `6d252fa3b696`  |
| 899    | No file  | `6d252fa3b696`  |
| 894    | No file  | `6d252fa3b696`  |
| 885    | No file  | `6d252fa3b696`  |
| 879    | No file  | `6d252fa3b696`  |
| 872    | No file  | `6d252fa3b696`  |
| 864    | No file  | `6d252fa3b696`  |
| 855    | No file  | `6d252fa3b696`  |
| 853    | No file  | `6d252fa3b696`  |
| 845    | No file  | `6d252fa3b696`  |
| 837    | No file  | `6d252fa3b696`  |
| 829    | No file  | `6d252fa3b696`  |
| 822    | No file  | `6d252fa3b696`  |
| 814    | No file  | `6d252fa3b696`  |
| 805    | No file  | `6d252fa3b696`  |
| 794    | No file  | `6d252fa3b696`  |
| 787    | No file  | `6d252fa3b696`  |
| 780    | No file  | `6d252fa3b696`  |
| 771    | No file  | `6d252fa3b696`  |
| 760    | No file  | `6d252fa3b696`  |
| 748    | No file  | `6d252fa3b696`  |
| 741    | No file  | `6d252fa3b696`  |
| 736    | No file  | `6d252fa3b696`  |
| 731    | No file  | `6d252fa3b696`  |
| 723    | No file  | `6d252fa3b696`  |
| 711    | No file  | `6d252fa3b696`  |
| 707    | No file  | `6d252fa3b696`  |
| 697    | No file  | `6d252fa3b696`  |
| 689    | No file  | `6d252fa3b696`  |
| 683    | No file  | `6d252fa3b696`  |
| 678    | No file  | `6d252fa3b696`  |
| 670    | No file  | `6d252fa3b696`  |
| 661    | No file  | `6d252fa3b696`  |
| 656    | No file  | `6d252fa3b696`  |
| 652    | No file  | `6d252fa3b696`  |
| 643    | No file  | `6d252fa3b696`  |
| 637    | No file  | `6d252fa3b696`  |
| 630    | No file  | `6d252fa3b696`  |
| 627    | No file  | `6d252fa3b696`  |
| 621    | No file  | `6d252fa3b696`  |
| 617    | No file  | `6d252fa3b696`  |
| 615    | No file  | `6d252fa3b696`  |
| 606    | No file  | `6d252fa3b696`  |
| 599    | No file  | `6d252fa3b696`  |
| 592    | No file  | `6d252fa3b696`  |
| 586    | No file  | `6d252fa3b696`  |
| 577    | No file  | `6d252fa3b696`  |
| 569    | No file  | `6d252fa3b696`  |
| 561    | No file  | `6d252fa3b696`  |
| 554    | No file  | `6d252fa3b696`  |
| 542    | No file  | `6d252fa3b696`  |
| 532    | No file  | `6d252fa3b696`  |
| 531    | No file  | `6d252fa3b696`  |
| 526    | No file  | `6d252fa3b696`  |
| 521    | No file  | `6d252fa3b696`  |
| 517    | No file  | `6d252fa3b696`  |
| 510    | No file  | `6d252fa3b696`  |
| 508    | No file  | `6d252fa3b696`  |
| 504    | No file  | `6d252fa3b696`  |
| 497    | No file  | `6d252fa3b696`  |
| 491    | No file  | `6d252fa3b696`  |
| 485    | No file  | `6d252fa3b696`  |
| 478    | No file  | `6d252fa3b696`  |
| 472    | No file  | `6d252fa3b696`  |
| 466    | No file  | `6d252fa3b696`  |
| 457    | No file  | `6d252fa3b696`  |
| 452    | No file  | `6d252fa3b696`  |
| 449    | No file  | `6d252fa3b696`  |
| 435    | No file  | `6d252fa3b696`  |

<!-- versions:end -->

## Companion Files

None.

## Layout 1

### File Layout

| Offset           | Type                      | Field        | Notes |
| ---------------- | ------------------------- | ------------ | ----- |
| `+0x00`          | char[4]                   | magic        | ASCII `PAR ` |
| `+0x04`          | u8                        | kind         | `0x11` on every `.pcm` |
| `+0x05`          | u8                        | version      | `2` on all 14,319 files (client 3483) |
| `+0x06`          | bytes[10]                 | unknown_06   | `00 01 02 03 04 05 06 07 08 09` on 998 of 1,000 sampled files; `00 00 01 02 03 04 05 06 07 08` on 2 |
| `+0x10`          | u32                       | vertex_count |  |
| `+0x14`          | f32[vertex_count][3]      | positions    | x, y, z in centimetres per vertex, y up |
| `positions+0x00` | u32                       | index_count  | A multiple of 3 |
| `positions+0x04` | u16[index_count]          | indices      | Three per triangle, each below `vertex_count` |

## Notes

- Every `.pcm` on client 3483 walks to its last byte by this layout (14,319 files, checked with `par_mesh.py`).
- 11,979 of the 14,280 `.pcm` files with a non-empty `.pam` next to them lie inside that mesh's box widened by 5 cm on each side.

## Open Questions

### What the Game Uses `.pcm` For

The geometry is a reduced copy of the `.pam` beside it in most files, which fits a collision or occlusion hull. The client Lua or the files that place objects (`.ipam`, `.object`) may name the `.pcm` and its role.
