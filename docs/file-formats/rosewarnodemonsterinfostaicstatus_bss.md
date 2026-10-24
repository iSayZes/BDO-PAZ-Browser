# `rosewarnodemonsterinfostaicstatus.bss` Format

## Purpose

The images of the Rose War sanctum characters: one row per character key
with two string-table indexes, the sanctum image and the tooltip image. On
client 3474 the file has 62 rows, every character of
[`rosewarfiercebattlemonsterstaticstatus.bss`](rosewarfiercebattlemonsterstaticstatus_bss.md):
the 20 neutral Faded Relics, the 40 team guardians and the two Mysterious
Statues.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ------- | --------- |
| 1      | 2545 and later | 3483    | `rosewarnodemonsterinfostaicstatus.bss` | 3,724 | 62 Row  | 10        |

| Layout | File                                    | Known            | Unknown    |
| ------ | --------------------------------------- | ---------------- | ---------- |
| 1      | `rosewarnodemonsterinfostaicstatus.bss` | 3,724 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d498f9a40450`  |
| 3482   | Layout 1 | `d498f9a40450`  |
| 3474   | Layout 1 | `d498f9a40450`  |
| 3473   | Layout 1 | `d498f9a40450`  |
| 3464   | Layout 1 | `d498f9a40450`  |
| 3458   | Layout 1 | `d498f9a40450`  |
| 3454   | Layout 1 | `d498f9a40450`  |
| 3444   | Layout 1 | `d498f9a40450`  |
| 3435   | Layout 1 | `d498f9a40450`  |
| 3426   | Layout 1 | `d498f9a40450`  |
| 3418   | Layout 1 | `d498f9a40450`  |
| 3412   | Layout 1 | `d498f9a40450`  |
| 3402   | Layout 1 | `d498f9a40450`  |
| 3396   | Layout 1 | `d498f9a40450`  |
| 3387   | Layout 1 | `d498f9a40450`  |
| 3381   | Layout 1 | `d498f9a40450`  |
| 3373   | Layout 1 | `d498f9a40450`  |
| 3364   | Layout 1 | `d498f9a40450`  |
| 3356   | Layout 1 | `d498f9a40450`  |
| 3349   | Layout 1 | `d498f9a40450`  |
| 3342   | Layout 1 | `d498f9a40450`  |
| 3335   | Layout 1 | `d498f9a40450`  |
| 3326   | Layout 1 | `d498f9a40450`  |
| 3321   | Layout 1 | `d498f9a40450`  |
| 3314   | Layout 1 | `d498f9a40450`  |
| 3303   | Layout 1 | `d498f9a40450`  |
| 3302   | Layout 1 | `d498f9a40450`  |
| 3293   | Layout 1 | `d498f9a40450`  |
| 3283   | Layout 1 | `d498f9a40450`  |
| 3275   | Layout 1 | `d498f9a40450`  |
| 3267   | Layout 1 | `d498f9a40450`  |
| 3258   | Layout 1 | `d498f9a40450`  |
| 3251   | Layout 1 | `d498f9a40450`  |
| 3242   | Layout 1 | `d498f9a40450`  |
| 3235   | Layout 1 | `d498f9a40450`  |
| 3229   | Layout 1 | `d498f9a40450`  |
| 3212   | Layout 1 | `d498f9a40450`  |
| 3203   | Layout 1 | `d498f9a40450`  |
| 3193   | Layout 1 | `d498f9a40450`  |
| 3186   | Layout 1 | `d498f9a40450`  |
| 3177   | Layout 1 | `d498f9a40450`  |
| 3169   | Layout 1 | `d498f9a40450`  |
| 3158   | Layout 1 | `d498f9a40450`  |
| 3151   | Layout 1 | `d498f9a40450`  |
| 3144   | Layout 1 | `d498f9a40450`  |
| 3133   | Layout 1 | `d498f9a40450`  |
| 3125   | Layout 1 | `d498f9a40450`  |
| 3118   | Layout 1 | `d498f9a40450`  |
| 3111   | Layout 1 | `d498f9a40450`  |
| 3103   | Layout 1 | `d498f9a40450`  |
| 3095   | Layout 1 | `d498f9a40450`  |
| 3086   | Layout 1 | `d498f9a40450`  |
| 3072   | Layout 1 | `d498f9a40450`  |
| 3062   | Layout 1 | `d498f9a40450`  |
| 3052   | Layout 1 | `d498f9a40450`  |
| 3045   | Layout 1 | `d498f9a40450`  |
| 3037   | Layout 1 | `d498f9a40450`  |
| 3030   | Layout 1 | `d498f9a40450`  |
| 3021   | Layout 1 | `d498f9a40450`  |
| 3012   | Layout 1 | `d498f9a40450`  |
| 3002   | Layout 1 | `d498f9a40450`  |
| 2995   | Layout 1 | `d498f9a40450`  |
| 2987   | Layout 1 | `d498f9a40450`  |
| 2978   | Layout 1 | `d498f9a40450`  |
| 2970   | Layout 1 | `d498f9a40450`  |
| 2959   | Layout 1 | `d498f9a40450`  |
| 2951   | Layout 1 | `d498f9a40450`  |
| 2942   | Layout 1 | `d498f9a40450`  |
| 2935   | Layout 1 | `d498f9a40450`  |
| 2932   | Layout 1 | `d498f9a40450`  |
| 2923   | Layout 1 | `d498f9a40450`  |
| 2919   | Layout 1 | `d498f9a40450`  |
| 2907   | Layout 1 | `d498f9a40450`  |
| 2900   | Layout 1 | `d498f9a40450`  |
| 2891   | Layout 1 | `d498f9a40450`  |
| 2882   | Layout 1 | `d498f9a40450`  |
| 2872   | Layout 1 | `d498f9a40450`  |
| 2863   | Layout 1 | `d498f9a40450`  |
| 2855   | Layout 1 | `d498f9a40450`  |
| 2849   | Layout 1 | `d498f9a40450`  |
| 2844   | Layout 1 | `d498f9a40450`  |
| 2834   | Layout 1 | `d498f9a40450`  |
| 2825   | Layout 1 | `d498f9a40450`  |
| 2819   | Layout 1 | `d498f9a40450`  |
| 2811   | Layout 1 | `d498f9a40450`  |
| 2803   | Layout 1 | `d498f9a40450`  |
| 2794   | Layout 1 | `d498f9a40450`  |
| 2783   | Layout 1 | `d498f9a40450`  |
| 2774   | Layout 1 | `d498f9a40450`  |
| 2765   | Layout 1 | `d498f9a40450`  |
| 2756   | Layout 1 | `d498f9a40450`  |
| 2750   | Layout 1 | `d498f9a40450`  |
| 2743   | Layout 1 | `d498f9a40450`  |
| 2736   | Layout 1 | `d498f9a40450`  |
| 2726   | Layout 1 | `d498f9a40450`  |
| 2717   | Layout 1 | `d498f9a40450`  |
| 2709   | Layout 1 | `d498f9a40450`  |
| 2703   | Layout 1 | `d498f9a40450`  |
| 2695   | Layout 1 | `d498f9a40450`  |
| 2684   | Layout 1 | `d498f9a40450`  |
| 2672   | Layout 1 | `d498f9a40450`  |
| 2665   | Layout 1 | `d498f9a40450`  |
| 2657   | Layout 1 | `d498f9a40450`  |
| 2649   | Layout 1 | `d498f9a40450`  |
| 2644   | Layout 1 | `d498f9a40450`  |
| 2637   | Layout 1 | `d498f9a40450`  |
| 2629   | Layout 1 | `d498f9a40450`  |
| 2619   | Layout 1 | `d498f9a40450`  |
| 2612   | Layout 1 | `d498f9a40450`  |
| 2606   | Layout 1 | `d498f9a40450`  |
| 2602   | Layout 1 | `d498f9a40450`  |
| 2601   | Layout 1 | `d498f9a40450`  |
| 2592   | Layout 1 | `d498f9a40450`  |
| 2583   | Layout 1 | `d498f9a40450`  |
| 2575   | Layout 1 | `d498f9a40450`  |
| 2567   | Layout 1 | `d498f9a40450`  |
| 2560   | Layout 1 | `d498f9a40450`  |
| 2553   | Layout 1 | `d498f9a40450`  |
| 2545   | Layout 1 | `d498f9a40450`  |
| 2538   | No file  | `d498f9a40450`  |
| 2529   | No file  | `d498f9a40450`  |
| 2519   | No file  | `d498f9a40450`  |
| 2513   | No file  | `d498f9a40450`  |
| 2510   | No file  | `d498f9a40450`  |
| 2507   | No file  | `d498f9a40450`  |
| 2503   | No file  | `d498f9a40450`  |
| 2498   | No file  | `d498f9a40450`  |
| 2492   | No file  | `d498f9a40450`  |
| 2487   | No file  | `d498f9a40450`  |
| 2480   | No file  | `d498f9a40450`  |
| 2474   | No file  | `d498f9a40450`  |
| 2468   | No file  | `d498f9a40450`  |
| 2460   | No file  | `d498f9a40450`  |
| 2453   | No file  | `d498f9a40450`  |
| 2444   | No file  | `d498f9a40450`  |
| 2438   | No file  | `d498f9a40450`  |
| 2434   | No file  | `d498f9a40450`  |
| 2429   | No file  | `d498f9a40450`  |
| 2421   | No file  | `d498f9a40450`  |
| 2414   | No file  | `d498f9a40450`  |
| 2407   | No file  | `d498f9a40450`  |
| 2401   | No file  | `d498f9a40450`  |
| 2397   | No file  | `d498f9a40450`  |
| 2393   | No file  | `d498f9a40450`  |
| 2384   | No file  | `d498f9a40450`  |
| 2378   | No file  | `d498f9a40450`  |
| 2372   | No file  | `d498f9a40450`  |
| 2358   | No file  | `d498f9a40450`  |
| 2352   | No file  | `d498f9a40450`  |
| 2347   | No file  | `d498f9a40450`  |
| 2343   | No file  | `d498f9a40450`  |
| 2335   | No file  | `d498f9a40450`  |
| 2327   | No file  | `d498f9a40450`  |
| 2324   | No file  | `d498f9a40450`  |
| 2319   | No file  | `d498f9a40450`  |
| 2313   | No file  | `d498f9a40450`  |
| 2308   | No file  | `d498f9a40450`  |
| 2302   | No file  | `d498f9a40450`  |
| 2295   | No file  | `d498f9a40450`  |
| 2290   | No file  | `d498f9a40450`  |
| 2284   | No file  | `d498f9a40450`  |
| 2276   | No file  | `d498f9a40450`  |
| 2269   | No file  | `d498f9a40450`  |
| 2259   | No file  | `d498f9a40450`  |
| 2250   | No file  | `d498f9a40450`  |
| 2243   | No file  | `d498f9a40450`  |
| 2235   | No file  | `d498f9a40450`  |
| 2229   | No file  | `d498f9a40450`  |
| 2224   | No file  | `d498f9a40450`  |
| 2218   | No file  | `d498f9a40450`  |
| 2215   | No file  | `d498f9a40450`  |
| 2207   | No file  | `d498f9a40450`  |
| 2203   | No file  | `d498f9a40450`  |
| 2196   | No file  | `d498f9a40450`  |
| 2192   | No file  | `d498f9a40450`  |
| 2189   | No file  | `d498f9a40450`  |
| 2183   | No file  | `d498f9a40450`  |
| 2179   | No file  | `d498f9a40450`  |
| 2171   | No file  | `d498f9a40450`  |
| 2163   | No file  | `d498f9a40450`  |
| 2156   | No file  | `d498f9a40450`  |
| 2151   | No file  | `d498f9a40450`  |
| 2147   | No file  | `d498f9a40450`  |
| 2142   | No file  | `d498f9a40450`  |
| 2138   | No file  | `d498f9a40450`  |
| 2134   | No file  | `d498f9a40450`  |
| 2130   | No file  | `d498f9a40450`  |
| 2122   | No file  | `d498f9a40450`  |
| 2107   | No file  | `d498f9a40450`  |
| 2098   | No file  | `d498f9a40450`  |
| 2089   | No file  | `d498f9a40450`  |
| 2081   | No file  | `d498f9a40450`  |
| 2073   | No file  | `d498f9a40450`  |
| 2067   | No file  | `d498f9a40450`  |
| 2063   | No file  | `d498f9a40450`  |
| 2059   | No file  | `d498f9a40450`  |
| 2052   | No file  | `d498f9a40450`  |
| 2044   | No file  | `d498f9a40450`  |
| 2039   | No file  | `d498f9a40450`  |
| 2032   | No file  | `d498f9a40450`  |
| 2025   | No file  | `d498f9a40450`  |
| 2011   | No file  | `d498f9a40450`  |
| 2005   | No file  | `d498f9a40450`  |
| 2000   | No file  | `d498f9a40450`  |
| 1996   | No file  | `d498f9a40450`  |
| 1991   | No file  | `d498f9a40450`  |
| 1985   | No file  | `d498f9a40450`  |
| 1980   | No file  | `d498f9a40450`  |
| 1969   | No file  | `d498f9a40450`  |
| 1964   | No file  | `d498f9a40450`  |
| 1958   | No file  | `d498f9a40450`  |
| 1950   | No file  | `d498f9a40450`  |
| 1945   | No file  | `d498f9a40450`  |
| 1937   | No file  | `d498f9a40450`  |
| 1933   | No file  | `d498f9a40450`  |
| 1927   | No file  | `d498f9a40450`  |
| 1921   | No file  | `d498f9a40450`  |
| 1914   | No file  | `d498f9a40450`  |
| 1908   | No file  | `d498f9a40450`  |
| 1897   | No file  | `d498f9a40450`  |
| 1892   | No file  | `d498f9a40450`  |
| 1886   | No file  | `d498f9a40450`  |
| 1881   | No file  | `d498f9a40450`  |
| 1871   | No file  | `d498f9a40450`  |
| 1866   | No file  | `d498f9a40450`  |
| 1862   | No file  | `d498f9a40450`  |
| 1854   | No file  | `d498f9a40450`  |
| 1846   | No file  | `d498f9a40450`  |
| 1838   | No file  | `d498f9a40450`  |
| 1832   | No file  | `d498f9a40450`  |
| 1826   | No file  | `d498f9a40450`  |
| 1822   | No file  | `d498f9a40450`  |
| 1818   | No file  | `d498f9a40450`  |
| 1804   | No file  | `d498f9a40450`  |
| 1794   | No file  | `d498f9a40450`  |
| 1790   | No file  | `d498f9a40450`  |
| 1784   | No file  | `d498f9a40450`  |
| 1774   | No file  | `d498f9a40450`  |
| 1771   | No file  | `d498f9a40450`  |
| 1762   | No file  | `d498f9a40450`  |
| 1759   | No file  | `d498f9a40450`  |
| 1754   | No file  | `d498f9a40450`  |
| 1749   | No file  | `d498f9a40450`  |
| 1743   | No file  | `d498f9a40450`  |
| 1737   | No file  | `d498f9a40450`  |
| 1731   | No file  | `d498f9a40450`  |
| 1725   | No file  | `d498f9a40450`  |
| 1717   | No file  | `d498f9a40450`  |
| 1710   | No file  | `d498f9a40450`  |
| 1704   | No file  | `d498f9a40450`  |
| 1698   | No file  | `d498f9a40450`  |
| 1690   | No file  | `d498f9a40450`  |
| 1685   | No file  | `d498f9a40450`  |
| 1680   | No file  | `d498f9a40450`  |
| 1674   | No file  | `d498f9a40450`  |
| 1668   | No file  | `d498f9a40450`  |
| 1659   | No file  | `d498f9a40450`  |
| 1649   | No file  | `d498f9a40450`  |
| 1642   | No file  | `d498f9a40450`  |
| 1636   | No file  | `d498f9a40450`  |
| 1628   | No file  | `d498f9a40450`  |
| 1622   | No file  | `d498f9a40450`  |
| 1614   | No file  | `d498f9a40450`  |
| 1608   | No file  | `d498f9a40450`  |
| 1602   | No file  | `d498f9a40450`  |
| 1598   | No file  | `d498f9a40450`  |
| 1594   | No file  | `d498f9a40450`  |
| 1590   | No file  | `d498f9a40450`  |
| 1587   | No file  | `d498f9a40450`  |
| 1584   | No file  | `d498f9a40450`  |
| 1579   | No file  | `d498f9a40450`  |
| 1572   | No file  | `d498f9a40450`  |
| 1565   | No file  | `d498f9a40450`  |
| 1559   | No file  | `d498f9a40450`  |
| 1554   | No file  | `d498f9a40450`  |
| 1547   | No file  | `d498f9a40450`  |
| 1537   | No file  | `d498f9a40450`  |
| 1529   | No file  | `d498f9a40450`  |
| 1524   | No file  | `d498f9a40450`  |
| 1519   | No file  | `d498f9a40450`  |
| 1509   | No file  | `d498f9a40450`  |
| 1506   | No file  | `d498f9a40450`  |
| 1504   | No file  | `d498f9a40450`  |
| 1500   | No file  | `d498f9a40450`  |
| 1493   | No file  | `d498f9a40450`  |
| 1489   | No file  | `d498f9a40450`  |
| 1485   | No file  | `d498f9a40450`  |
| 1481   | No file  | `d498f9a40450`  |
| 1474   | No file  | `d498f9a40450`  |
| 1466   | No file  | `d498f9a40450`  |
| 1462   | No file  | `d498f9a40450`  |
| 1459   | No file  | `d498f9a40450`  |
| 1453   | No file  | `d498f9a40450`  |
| 1450   | No file  | `d498f9a40450`  |
| 1445   | No file  | `d498f9a40450`  |
| 1439   | No file  | `d498f9a40450`  |
| 1433   | No file  | `d498f9a40450`  |
| 1430   | No file  | `d498f9a40450`  |
| 1426   | No file  | `d498f9a40450`  |
| 1421   | No file  | `d498f9a40450`  |
| 1417   | No file  | `d498f9a40450`  |
| 1416   | No file  | `d498f9a40450`  |
| 1409   | No file  | `d498f9a40450`  |
| 1405   | No file  | `d498f9a40450`  |
| 1401   | No file  | `d498f9a40450`  |
| 1396   | No file  | `d498f9a40450`  |
| 1391   | No file  | `d498f9a40450`  |
| 1390   | No file  | `d498f9a40450`  |
| 1386   | No file  | `d498f9a40450`  |
| 1381   | No file  | `d498f9a40450`  |
| 1379   | No file  | `d498f9a40450`  |
| 1372   | No file  | `d498f9a40450`  |
| 1366   | No file  | `d498f9a40450`  |
| 1364   | No file  | `d498f9a40450`  |
| 1363   | No file  | `d498f9a40450`  |
| 1360   | No file  | `d498f9a40450`  |
| 1358   | No file  | `d498f9a40450`  |
| 1355   | No file  | `d498f9a40450`  |
| 1351   | No file  | `d498f9a40450`  |
| 1348   | No file  | `d498f9a40450`  |
| 1346   | No file  | `d498f9a40450`  |
| 1341   | No file  | `d498f9a40450`  |
| 1340   | No file  | `d498f9a40450`  |
| 1338   | No file  | `d498f9a40450`  |
| 1335   | No file  | `d498f9a40450`  |
| 1333   | No file  | `d498f9a40450`  |
| 1329   | No file  | `d498f9a40450`  |
| 1327   | No file  | `d498f9a40450`  |
| 1324   | No file  | `d498f9a40450`  |
| 1321   | No file  | `d498f9a40450`  |
| 1319   | No file  | `d498f9a40450`  |
| 1318   | No file  | `d498f9a40450`  |
| 1316   | No file  | `d498f9a40450`  |
| 1313   | No file  | `d498f9a40450`  |
| 1311   | No file  | `d498f9a40450`  |
| 1309   | No file  | `d498f9a40450`  |
| 1304   | No file  | `d498f9a40450`  |
| 1292   | No file  | `d498f9a40450`  |
| 1286   | No file  | `d498f9a40450`  |
| 1280   | No file  | `d498f9a40450`  |
| 1276   | No file  | `d498f9a40450`  |
| 1267   | No file  | `d498f9a40450`  |
| 1261   | No file  | `d498f9a40450`  |
| 1256   | No file  | `d498f9a40450`  |
| 1250   | No file  | `d498f9a40450`  |
| 1246   | No file  | `d498f9a40450`  |
| 1239   | No file  | `d498f9a40450`  |
| 1230   | No file  | `d498f9a40450`  |
| 1226   | No file  | `d498f9a40450`  |
| 1220   | No file  | `d498f9a40450`  |
| 1217   | No file  | `d498f9a40450`  |
| 1211   | No file  | `d498f9a40450`  |
| 1210   | No file  | `d498f9a40450`  |
| 1208   | No file  | `d498f9a40450`  |
| 1203   | No file  | `d498f9a40450`  |
| 1197   | No file  | `d498f9a40450`  |
| 1194   | No file  | `d498f9a40450`  |
| 1192   | No file  | `d498f9a40450`  |
| 1187   | No file  | `d498f9a40450`  |
| 1183   | No file  | `d498f9a40450`  |
| 1177   | No file  | `d498f9a40450`  |
| 1173   | No file  | `d498f9a40450`  |
| 1167   | No file  | `d498f9a40450`  |
| 1164   | No file  | `d498f9a40450`  |
| 1156   | No file  | `d498f9a40450`  |
| 1149   | No file  | `d498f9a40450`  |
| 1144   | No file  | `d498f9a40450`  |
| 1137   | No file  | `d498f9a40450`  |
| 1132   | No file  | `d498f9a40450`  |
| 1127   | No file  | `d498f9a40450`  |
| 1122   | No file  | `d498f9a40450`  |
| 1118   | No file  | `d498f9a40450`  |
| 1114   | No file  | `d498f9a40450`  |
| 1109   | No file  | `d498f9a40450`  |
| 1102   | No file  | `d498f9a40450`  |
| 1096   | No file  | `d498f9a40450`  |
| 1088   | No file  | `d498f9a40450`  |
| 1081   | No file  | `d498f9a40450`  |
| 1076   | No file  | `d498f9a40450`  |
| 1069   | No file  | `d498f9a40450`  |
| 1064   | No file  | `d498f9a40450`  |
| 1058   | No file  | `d498f9a40450`  |
| 1051   | No file  | `d498f9a40450`  |
| 1044   | No file  | `d498f9a40450`  |
| 1036   | No file  | `d498f9a40450`  |
| 1026   | No file  | `d498f9a40450`  |
| 1016   | No file  | `d498f9a40450`  |
| 1009   | No file  | `d498f9a40450`  |
| 1005   | No file  | `d498f9a40450`  |
| 1000   | No file  | `d498f9a40450`  |
| 998    | No file  | `d498f9a40450`  |
| 990    | No file  | `d498f9a40450`  |
| 979    | No file  | `d498f9a40450`  |
| 972    | No file  | `d498f9a40450`  |
| 963    | No file  | `d498f9a40450`  |
| 955    | No file  | `d498f9a40450`  |
| 946    | No file  | `d498f9a40450`  |
| 938    | No file  | `d498f9a40450`  |
| 927    | No file  | `d498f9a40450`  |
| 911    | No file  | `d498f9a40450`  |
| 904    | No file  | `d498f9a40450`  |
| 899    | No file  | `d498f9a40450`  |
| 894    | No file  | `d498f9a40450`  |
| 885    | No file  | `d498f9a40450`  |
| 879    | No file  | `d498f9a40450`  |
| 872    | No file  | `d498f9a40450`  |
| 864    | No file  | `d498f9a40450`  |
| 855    | No file  | `d498f9a40450`  |
| 853    | No file  | `d498f9a40450`  |
| 845    | No file  | `d498f9a40450`  |
| 837    | No file  | `d498f9a40450`  |
| 829    | No file  | `d498f9a40450`  |
| 822    | No file  | `d498f9a40450`  |
| 814    | No file  | `d498f9a40450`  |
| 805    | No file  | `d498f9a40450`  |
| 794    | No file  | `d498f9a40450`  |
| 787    | No file  | `d498f9a40450`  |
| 780    | No file  | `d498f9a40450`  |
| 771    | No file  | `d498f9a40450`  |
| 760    | No file  | `d498f9a40450`  |
| 748    | No file  | `d498f9a40450`  |
| 741    | No file  | `d498f9a40450`  |
| 736    | No file  | `d498f9a40450`  |
| 731    | No file  | `d498f9a40450`  |
| 723    | No file  | `d498f9a40450`  |
| 711    | No file  | `d498f9a40450`  |
| 707    | No file  | `d498f9a40450`  |
| 697    | No file  | `d498f9a40450`  |
| 689    | No file  | `d498f9a40450`  |
| 683    | No file  | `d498f9a40450`  |
| 678    | No file  | `d498f9a40450`  |
| 670    | No file  | `d498f9a40450`  |
| 661    | No file  | `d498f9a40450`  |
| 656    | No file  | `d498f9a40450`  |
| 652    | No file  | `d498f9a40450`  |
| 643    | No file  | `d498f9a40450`  |
| 637    | No file  | `d498f9a40450`  |
| 630    | No file  | `d498f9a40450`  |
| 627    | No file  | `d498f9a40450`  |
| 621    | No file  | `d498f9a40450`  |
| 617    | No file  | `d498f9a40450`  |
| 615    | No file  | `d498f9a40450`  |
| 606    | No file  | `d498f9a40450`  |
| 599    | No file  | `d498f9a40450`  |
| 592    | No file  | `d498f9a40450`  |
| 586    | No file  | `d498f9a40450`  |
| 577    | No file  | `d498f9a40450`  |
| 569    | No file  | `d498f9a40450`  |
| 561    | No file  | `d498f9a40450`  |
| 554    | No file  | `d498f9a40450`  |
| 542    | No file  | `d498f9a40450`  |
| 532    | No file  | `d498f9a40450`  |
| 531    | No file  | `d498f9a40450`  |
| 526    | No file  | `d498f9a40450`  |
| 521    | No file  | `d498f9a40450`  |
| 517    | No file  | `d498f9a40450`  |
| 510    | No file  | `d498f9a40450`  |
| 508    | No file  | `d498f9a40450`  |
| 504    | No file  | `d498f9a40450`  |
| 497    | No file  | `d498f9a40450`  |
| 491    | No file  | `d498f9a40450`  |
| 485    | No file  | `d498f9a40450`  |
| 478    | No file  | `d498f9a40450`  |
| 472    | No file  | `d498f9a40450`  |
| 466    | No file  | `d498f9a40450`  |
| 457    | No file  | `d498f9a40450`  |
| 452    | No file  | `d498f9a40450`  |
| 449    | No file  | `d498f9a40450`  |
| 435    | No file  | `d498f9a40450`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6     |

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

### Row (10 bytes)

| Offset  | Type | Field             | Notes                                                                        |
| ------- | ---- | ----------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | character_key     | `characterstatic.dbss` key; the handler shows its LOC type 6 name            |
| `+0x02` | u32  | image_ref         | String table index of the sanctum image (`UI_Artwork/ElfWar_Kama_N1.dds`)    |
| `+0x06` | u32  | tooltip_image_ref | String table index of the tooltip image (`UI_Artwork/ElfWar_Kama_Neutral_Tooltip.dds`) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `40` on client 3474                   |
| `+0x04` | pstr[string_count] | strings      | Wide `.dds` paths, each stored once in first-use order   |

## Images

Client 3474. A character shares the sanctum image of the sanctum it
guards, so `image_ref` names the sanctum and `tooltip_image_ref` the
character:

| Characters                                   | `image_path`                           | `tooltip_image_path`                                          |
| -------------------------------------------- | -------------------------------------- | ------------------------------------------------------------- |
| Faded Relic `21811` to `21820`               | `ElfWar_Kama_N1` to `N10`              | `ElfWar_Kama_Neutral_Tooltip`                                 |
| Faded Relic `21821` to `21830`               | `ElfWar_Odyl_S1` to `S10`              | `ElfWar_Odyl_Neutral_Tooltip`                                 |
| Kamasylvia guardians `21831` to `21850`      | the image of the sanctum they guard    | `ElfWar_Kama_Boss_Urugon_Tooltip`, `ElfWar_Kama_Fadus_Bow_Tooltip` and others |
| O'dyllita guardians `21851` to `21870`       | the image of the sanctum they guard    | `ElfWar_Odyl_Salun_Wolf_Tooltip`, `ElfWar_Odyl_Khalk_Tooltip` and others |
| Mysterious Statue `21699`, `21700`           | `IC_00749`                             | `IC_00749_Tooltip`                                            |

All paths start with `UI_Artwork/` and end in `.dds`.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. Every key resolves to a LOC
type 6 character name, and every key is a character of the monster table.
The two index fields are named by the strings they point to: the second
one's paths all end in `_Tooltip.dds`.

## Notes

- The file is 3,724 bytes on clients 3002, 3251 and 3474. Client 3002
  has the same characters and paths, but three O'dyllita guardians sit on
  other sanctum images: Ulutuka (`21862`) on `S6` in place of `S5`, Turo
  Berserker (`21866`) on `S7` in place of `S6`, and Ahib Salun Wolf
  Spearmaiden (`21869`) on `S5` in place of `S7`. The file is not in the
  archives of client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  with both paths as text.
