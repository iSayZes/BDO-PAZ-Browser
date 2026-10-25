# `magnuseasyteleport.bss` Format

## Purpose

The destinations of the Magnus teleport map
(`panel_window_magnuseasyteleportmap.luac`): one row per destination with
its waypoint, a world position, a GAME sheet key of the territory name,
the knowledge that unlocks the button and a region. On client 3482 it
holds 16 destinations, from Velia (Balenos) to Angavu Outpost (Inner
Edania); the map shows button `CheckButton_<index + 1>` for row `index`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------ | ----- | ------- | --------- |
| 2      | 3144 and later | `magnuseasyteleport.bss` | 1,099 | 16 Row  | 32        |
| 1      | 2421 to 3133   | `magnuseasyteleport.bss` | 967   | 15 Row  | 28        |

| Layout | File                     | Known         | Unknown       |
| ------ | ------------------------ | ------------- | ------------- |
| 2      | `magnuseasyteleport.bss` | 971 B (88.4%) | 128 B (11.6%) |
| 1      | `magnuseasyteleport.bss` | 847 B (87.6%) | 120 B (12.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `ecd6a8377794`  |
| 3482   | Layout 2 | `ecd6a8377794`  |
| 3474   | Layout 2 | `ecd6a8377794`  |
| 3473   | Layout 2 | `ecd6a8377794`  |
| 3464   | Layout 2 | `ecd6a8377794`  |
| 3458   | Layout 2 | `ecd6a8377794`  |
| 3454   | Layout 2 | `ecd6a8377794`  |
| 3444   | Layout 2 | `ecd6a8377794`  |
| 3435   | Layout 2 | `ecd6a8377794`  |
| 3426   | Layout 2 | `ecd6a8377794`  |
| 3418   | Layout 2 | `ecd6a8377794`  |
| 3412   | Layout 2 | `ecd6a8377794`  |
| 3402   | Layout 2 | `ecd6a8377794`  |
| 3396   | Layout 2 | `ecd6a8377794`  |
| 3387   | Layout 2 | `ecd6a8377794`  |
| 3381   | Layout 2 | `ecd6a8377794`  |
| 3373   | Layout 2 | `ecd6a8377794`  |
| 3364   | Layout 2 | `ecd6a8377794`  |
| 3356   | Layout 2 | `ecd6a8377794`  |
| 3349   | Layout 2 | `ecd6a8377794`  |
| 3342   | Layout 2 | `ecd6a8377794`  |
| 3335   | Layout 2 | `ecd6a8377794`  |
| 3326   | Layout 2 | `ecd6a8377794`  |
| 3321   | Layout 2 | `ecd6a8377794`  |
| 3314   | Layout 2 | `ecd6a8377794`  |
| 3303   | Layout 2 | `ecd6a8377794`  |
| 3302   | Layout 2 | `ecd6a8377794`  |
| 3293   | Layout 2 | `ecd6a8377794`  |
| 3283   | Layout 2 | `ecd6a8377794`  |
| 3275   | Layout 2 | `ecd6a8377794`  |
| 3267   | Layout 2 | `ecd6a8377794`  |
| 3258   | Layout 2 | `ecd6a8377794`  |
| 3251   | Layout 2 | `ecd6a8377794`  |
| 3242   | Layout 2 | `ecd6a8377794`  |
| 3235   | Layout 2 | `ecd6a8377794`  |
| 3229   | Layout 2 | `ecd6a8377794`  |
| 3212   | Layout 2 | `ecd6a8377794`  |
| 3203   | Layout 2 | `ecd6a8377794`  |
| 3193   | Layout 2 | `ecd6a8377794`  |
| 3186   | Layout 2 | `ecd6a8377794`  |
| 3177   | Layout 2 | `ecd6a8377794`  |
| 3169   | Layout 2 | `ecd6a8377794`  |
| 3158   | Layout 2 | `ecd6a8377794`  |
| 3151   | Layout 2 | `ecd6a8377794`  |
| 3144   | Layout 2 | `ecd6a8377794`  |
| 3133   | Layout 1 | `ecd6a8377794`  |
| 3125   | Layout 1 | `ecd6a8377794`  |
| 3118   | Layout 1 | `ecd6a8377794`  |
| 3111   | Layout 1 | `ecd6a8377794`  |
| 3103   | Layout 1 | `ecd6a8377794`  |
| 3095   | Layout 1 | `ecd6a8377794`  |
| 3086   | Layout 1 | `ecd6a8377794`  |
| 3072   | Layout 1 | `ecd6a8377794`  |
| 3062   | Layout 1 | `ecd6a8377794`  |
| 3052   | Layout 1 | `ecd6a8377794`  |
| 3045   | Layout 1 | `ecd6a8377794`  |
| 3037   | Layout 1 | `ecd6a8377794`  |
| 3030   | Layout 1 | `ecd6a8377794`  |
| 3021   | Layout 1 | `ecd6a8377794`  |
| 3012   | Layout 1 | `ecd6a8377794`  |
| 3002   | Layout 1 | `ecd6a8377794`  |
| 2995   | Layout 1 | `ecd6a8377794`  |
| 2987   | Layout 1 | `ecd6a8377794`  |
| 2978   | Layout 1 | `ecd6a8377794`  |
| 2970   | Layout 1 | `ecd6a8377794`  |
| 2959   | Layout 1 | `ecd6a8377794`  |
| 2951   | Layout 1 | `ecd6a8377794`  |
| 2942   | Layout 1 | `ecd6a8377794`  |
| 2935   | Layout 1 | `ecd6a8377794`  |
| 2932   | Layout 1 | `ecd6a8377794`  |
| 2923   | Layout 1 | `ecd6a8377794`  |
| 2919   | Layout 1 | `ecd6a8377794`  |
| 2907   | Layout 1 | `ecd6a8377794`  |
| 2900   | Layout 1 | `ecd6a8377794`  |
| 2891   | Layout 1 | `ecd6a8377794`  |
| 2882   | Layout 1 | `ecd6a8377794`  |
| 2872   | Layout 1 | `ecd6a8377794`  |
| 2863   | Layout 1 | `ecd6a8377794`  |
| 2855   | Layout 1 | `ecd6a8377794`  |
| 2849   | Layout 1 | `ecd6a8377794`  |
| 2844   | Layout 1 | `ecd6a8377794`  |
| 2834   | Layout 1 | `ecd6a8377794`  |
| 2825   | Layout 1 | `ecd6a8377794`  |
| 2819   | Layout 1 | `ecd6a8377794`  |
| 2811   | Layout 1 | `ecd6a8377794`  |
| 2803   | Layout 1 | `ecd6a8377794`  |
| 2794   | Layout 1 | `ecd6a8377794`  |
| 2783   | Layout 1 | `ecd6a8377794`  |
| 2774   | Layout 1 | `ecd6a8377794`  |
| 2765   | Layout 1 | `ecd6a8377794`  |
| 2756   | Layout 1 | `ecd6a8377794`  |
| 2750   | Layout 1 | `ecd6a8377794`  |
| 2743   | Layout 1 | `ecd6a8377794`  |
| 2736   | Layout 1 | `ecd6a8377794`  |
| 2726   | Layout 1 | `ecd6a8377794`  |
| 2717   | Layout 1 | `ecd6a8377794`  |
| 2709   | Layout 1 | `ecd6a8377794`  |
| 2703   | Layout 1 | `ecd6a8377794`  |
| 2695   | Layout 1 | `ecd6a8377794`  |
| 2684   | Layout 1 | `ecd6a8377794`  |
| 2672   | Layout 1 | `ecd6a8377794`  |
| 2665   | Layout 1 | `ecd6a8377794`  |
| 2657   | Layout 1 | `ecd6a8377794`  |
| 2649   | Layout 1 | `ecd6a8377794`  |
| 2644   | Layout 1 | `ecd6a8377794`  |
| 2637   | Layout 1 | `ecd6a8377794`  |
| 2629   | Layout 1 | `ecd6a8377794`  |
| 2619   | Layout 1 | `ecd6a8377794`  |
| 2612   | Layout 1 | `ecd6a8377794`  |
| 2606   | Layout 1 | `ecd6a8377794`  |
| 2602   | Layout 1 | `ecd6a8377794`  |
| 2601   | Layout 1 | `ecd6a8377794`  |
| 2592   | Layout 1 | `ecd6a8377794`  |
| 2583   | Layout 1 | `ecd6a8377794`  |
| 2575   | Layout 1 | `ecd6a8377794`  |
| 2567   | Layout 1 | `ecd6a8377794`  |
| 2560   | Layout 1 | `ecd6a8377794`  |
| 2553   | Layout 1 | `ecd6a8377794`  |
| 2545   | Layout 1 | `ecd6a8377794`  |
| 2538   | Layout 1 | `ecd6a8377794`  |
| 2529   | Layout 1 | `ecd6a8377794`  |
| 2519   | Layout 1 | `ecd6a8377794`  |
| 2513   | Layout 1 | `ecd6a8377794`  |
| 2510   | Layout 1 | `ecd6a8377794`  |
| 2507   | Layout 1 | `ecd6a8377794`  |
| 2503   | Layout 1 | `ecd6a8377794`  |
| 2498   | Layout 1 | `ecd6a8377794`  |
| 2492   | Layout 1 | `ecd6a8377794`  |
| 2487   | Layout 1 | `ecd6a8377794`  |
| 2480   | Layout 1 | `ecd6a8377794`  |
| 2474   | Layout 1 | `ecd6a8377794`  |
| 2468   | Layout 1 | `ecd6a8377794`  |
| 2460   | Layout 1 | `ecd6a8377794`  |
| 2453   | Layout 1 | `ecd6a8377794`  |
| 2444   | Layout 1 | `ecd6a8377794`  |
| 2438   | Layout 1 | `ecd6a8377794`  |
| 2434   | Layout 1 | `ecd6a8377794`  |
| 2429   | Layout 1 | `ecd6a8377794`  |
| 2421   | Layout 1 | `ecd6a8377794`  |
| 2414   | No file  | `ecd6a8377794`  |
| 2407   | No file  | `ecd6a8377794`  |
| 2401   | No file  | `ecd6a8377794`  |
| 2397   | No file  | `ecd6a8377794`  |
| 2393   | No file  | `ecd6a8377794`  |
| 2384   | No file  | `ecd6a8377794`  |
| 2378   | No file  | `ecd6a8377794`  |
| 2372   | No file  | `ecd6a8377794`  |
| 2358   | No file  | `ecd6a8377794`  |
| 2352   | No file  | `ecd6a8377794`  |
| 2347   | No file  | `ecd6a8377794`  |
| 2343   | No file  | `ecd6a8377794`  |
| 2335   | No file  | `ecd6a8377794`  |
| 2327   | No file  | `ecd6a8377794`  |
| 2324   | No file  | `ecd6a8377794`  |
| 2319   | No file  | `ecd6a8377794`  |
| 2313   | No file  | `ecd6a8377794`  |
| 2308   | No file  | `ecd6a8377794`  |
| 2302   | No file  | `ecd6a8377794`  |
| 2295   | No file  | `ecd6a8377794`  |
| 2290   | No file  | `ecd6a8377794`  |
| 2284   | No file  | `ecd6a8377794`  |
| 2276   | No file  | `ecd6a8377794`  |
| 2269   | No file  | `ecd6a8377794`  |
| 2259   | No file  | `ecd6a8377794`  |
| 2250   | No file  | `ecd6a8377794`  |
| 2243   | No file  | `ecd6a8377794`  |
| 2235   | No file  | `ecd6a8377794`  |
| 2229   | No file  | `ecd6a8377794`  |
| 2224   | No file  | `ecd6a8377794`  |
| 2218   | No file  | `ecd6a8377794`  |
| 2215   | No file  | `ecd6a8377794`  |
| 2207   | No file  | `ecd6a8377794`  |
| 2203   | No file  | `ecd6a8377794`  |
| 2196   | No file  | `ecd6a8377794`  |
| 2192   | No file  | `ecd6a8377794`  |
| 2189   | No file  | `ecd6a8377794`  |
| 2183   | No file  | `ecd6a8377794`  |
| 2179   | No file  | `ecd6a8377794`  |
| 2171   | No file  | `ecd6a8377794`  |
| 2163   | No file  | `ecd6a8377794`  |
| 2156   | No file  | `ecd6a8377794`  |
| 2151   | No file  | `ecd6a8377794`  |
| 2147   | No file  | `ecd6a8377794`  |
| 2142   | No file  | `ecd6a8377794`  |
| 2138   | No file  | `ecd6a8377794`  |
| 2134   | No file  | `ecd6a8377794`  |
| 2130   | No file  | `ecd6a8377794`  |
| 2122   | No file  | `ecd6a8377794`  |
| 2107   | No file  | `ecd6a8377794`  |
| 2098   | No file  | `ecd6a8377794`  |
| 2089   | No file  | `ecd6a8377794`  |
| 2081   | No file  | `ecd6a8377794`  |
| 2073   | No file  | `ecd6a8377794`  |
| 2067   | No file  | `ecd6a8377794`  |
| 2063   | No file  | `ecd6a8377794`  |
| 2059   | No file  | `ecd6a8377794`  |
| 2052   | No file  | `ecd6a8377794`  |
| 2044   | No file  | `ecd6a8377794`  |
| 2039   | No file  | `ecd6a8377794`  |
| 2032   | No file  | `ecd6a8377794`  |
| 2025   | No file  | `ecd6a8377794`  |
| 2011   | No file  | `ecd6a8377794`  |
| 2005   | No file  | `ecd6a8377794`  |
| 2000   | No file  | `ecd6a8377794`  |
| 1996   | No file  | `ecd6a8377794`  |
| 1991   | No file  | `ecd6a8377794`  |
| 1985   | No file  | `ecd6a8377794`  |
| 1980   | No file  | `ecd6a8377794`  |
| 1969   | No file  | `ecd6a8377794`  |
| 1964   | No file  | `ecd6a8377794`  |
| 1958   | No file  | `ecd6a8377794`  |
| 1950   | No file  | `ecd6a8377794`  |
| 1945   | No file  | `ecd6a8377794`  |
| 1937   | No file  | `ecd6a8377794`  |
| 1933   | No file  | `ecd6a8377794`  |
| 1927   | No file  | `ecd6a8377794`  |
| 1921   | No file  | `ecd6a8377794`  |
| 1914   | No file  | `ecd6a8377794`  |
| 1908   | No file  | `ecd6a8377794`  |
| 1897   | No file  | `ecd6a8377794`  |
| 1892   | No file  | `ecd6a8377794`  |
| 1886   | No file  | `ecd6a8377794`  |
| 1881   | No file  | `ecd6a8377794`  |
| 1871   | No file  | `ecd6a8377794`  |
| 1866   | No file  | `ecd6a8377794`  |
| 1862   | No file  | `ecd6a8377794`  |
| 1854   | No file  | `ecd6a8377794`  |
| 1846   | No file  | `ecd6a8377794`  |
| 1838   | No file  | `ecd6a8377794`  |
| 1832   | No file  | `ecd6a8377794`  |
| 1826   | No file  | `ecd6a8377794`  |
| 1822   | No file  | `ecd6a8377794`  |
| 1818   | No file  | `ecd6a8377794`  |
| 1804   | No file  | `ecd6a8377794`  |
| 1794   | No file  | `ecd6a8377794`  |
| 1790   | No file  | `ecd6a8377794`  |
| 1784   | No file  | `ecd6a8377794`  |
| 1774   | No file  | `ecd6a8377794`  |
| 1771   | No file  | `ecd6a8377794`  |
| 1762   | No file  | `ecd6a8377794`  |
| 1759   | No file  | `ecd6a8377794`  |
| 1754   | No file  | `ecd6a8377794`  |
| 1749   | No file  | `ecd6a8377794`  |
| 1743   | No file  | `ecd6a8377794`  |
| 1737   | No file  | `ecd6a8377794`  |
| 1731   | No file  | `ecd6a8377794`  |
| 1725   | No file  | `ecd6a8377794`  |
| 1717   | No file  | `ecd6a8377794`  |
| 1710   | No file  | `ecd6a8377794`  |
| 1704   | No file  | `ecd6a8377794`  |
| 1698   | No file  | `ecd6a8377794`  |
| 1690   | No file  | `ecd6a8377794`  |
| 1685   | No file  | `ecd6a8377794`  |
| 1680   | No file  | `ecd6a8377794`  |
| 1674   | No file  | `ecd6a8377794`  |
| 1668   | No file  | `ecd6a8377794`  |
| 1659   | No file  | `ecd6a8377794`  |
| 1649   | No file  | `ecd6a8377794`  |
| 1642   | No file  | `ecd6a8377794`  |
| 1636   | No file  | `ecd6a8377794`  |
| 1628   | No file  | `ecd6a8377794`  |
| 1622   | No file  | `ecd6a8377794`  |
| 1614   | No file  | `ecd6a8377794`  |
| 1608   | No file  | `ecd6a8377794`  |
| 1602   | No file  | `ecd6a8377794`  |
| 1598   | No file  | `ecd6a8377794`  |
| 1594   | No file  | `ecd6a8377794`  |
| 1590   | No file  | `ecd6a8377794`  |
| 1587   | No file  | `ecd6a8377794`  |
| 1584   | No file  | `ecd6a8377794`  |
| 1579   | No file  | `ecd6a8377794`  |
| 1572   | No file  | `ecd6a8377794`  |
| 1565   | No file  | `ecd6a8377794`  |
| 1559   | No file  | `ecd6a8377794`  |
| 1554   | No file  | `ecd6a8377794`  |
| 1547   | No file  | `ecd6a8377794`  |
| 1537   | No file  | `ecd6a8377794`  |
| 1529   | No file  | `ecd6a8377794`  |
| 1524   | No file  | `ecd6a8377794`  |
| 1519   | No file  | `ecd6a8377794`  |
| 1509   | No file  | `ecd6a8377794`  |
| 1506   | No file  | `ecd6a8377794`  |
| 1504   | No file  | `ecd6a8377794`  |
| 1500   | No file  | `ecd6a8377794`  |
| 1493   | No file  | `ecd6a8377794`  |
| 1489   | No file  | `ecd6a8377794`  |
| 1485   | No file  | `ecd6a8377794`  |
| 1481   | No file  | `ecd6a8377794`  |
| 1474   | No file  | `ecd6a8377794`  |
| 1466   | No file  | `ecd6a8377794`  |
| 1462   | No file  | `ecd6a8377794`  |
| 1459   | No file  | `ecd6a8377794`  |
| 1453   | No file  | `ecd6a8377794`  |
| 1450   | No file  | `ecd6a8377794`  |
| 1445   | No file  | `ecd6a8377794`  |
| 1439   | No file  | `ecd6a8377794`  |
| 1433   | No file  | `ecd6a8377794`  |
| 1430   | No file  | `ecd6a8377794`  |
| 1426   | No file  | `ecd6a8377794`  |
| 1421   | No file  | `ecd6a8377794`  |
| 1417   | No file  | `ecd6a8377794`  |
| 1416   | No file  | `ecd6a8377794`  |
| 1409   | No file  | `ecd6a8377794`  |
| 1405   | No file  | `ecd6a8377794`  |
| 1401   | No file  | `ecd6a8377794`  |
| 1396   | No file  | `ecd6a8377794`  |
| 1391   | No file  | `ecd6a8377794`  |
| 1390   | No file  | `ecd6a8377794`  |
| 1386   | No file  | `ecd6a8377794`  |
| 1381   | No file  | `ecd6a8377794`  |
| 1379   | No file  | `ecd6a8377794`  |
| 1372   | No file  | `ecd6a8377794`  |
| 1366   | No file  | `ecd6a8377794`  |
| 1364   | No file  | `ecd6a8377794`  |
| 1363   | No file  | `ecd6a8377794`  |
| 1360   | No file  | `ecd6a8377794`  |
| 1358   | No file  | `ecd6a8377794`  |
| 1355   | No file  | `ecd6a8377794`  |
| 1351   | No file  | `ecd6a8377794`  |
| 1348   | No file  | `ecd6a8377794`  |
| 1346   | No file  | `ecd6a8377794`  |
| 1341   | No file  | `ecd6a8377794`  |
| 1340   | No file  | `ecd6a8377794`  |
| 1338   | No file  | `ecd6a8377794`  |
| 1335   | No file  | `ecd6a8377794`  |
| 1333   | No file  | `ecd6a8377794`  |
| 1329   | No file  | `ecd6a8377794`  |
| 1327   | No file  | `ecd6a8377794`  |
| 1324   | No file  | `ecd6a8377794`  |
| 1321   | No file  | `ecd6a8377794`  |
| 1319   | No file  | `ecd6a8377794`  |
| 1318   | No file  | `ecd6a8377794`  |
| 1316   | No file  | `ecd6a8377794`  |
| 1313   | No file  | `ecd6a8377794`  |
| 1311   | No file  | `ecd6a8377794`  |
| 1309   | No file  | `ecd6a8377794`  |
| 1304   | No file  | `ecd6a8377794`  |
| 1292   | No file  | `ecd6a8377794`  |
| 1286   | No file  | `ecd6a8377794`  |
| 1280   | No file  | `ecd6a8377794`  |
| 1276   | No file  | `ecd6a8377794`  |
| 1267   | No file  | `ecd6a8377794`  |
| 1261   | No file  | `ecd6a8377794`  |
| 1256   | No file  | `ecd6a8377794`  |
| 1250   | No file  | `ecd6a8377794`  |
| 1246   | No file  | `ecd6a8377794`  |
| 1239   | No file  | `ecd6a8377794`  |
| 1230   | No file  | `ecd6a8377794`  |
| 1226   | No file  | `ecd6a8377794`  |
| 1220   | No file  | `ecd6a8377794`  |
| 1217   | No file  | `ecd6a8377794`  |
| 1211   | No file  | `ecd6a8377794`  |
| 1210   | No file  | `ecd6a8377794`  |
| 1208   | No file  | `ecd6a8377794`  |
| 1203   | No file  | `ecd6a8377794`  |
| 1197   | No file  | `ecd6a8377794`  |
| 1194   | No file  | `ecd6a8377794`  |
| 1192   | No file  | `ecd6a8377794`  |
| 1187   | No file  | `ecd6a8377794`  |
| 1183   | No file  | `ecd6a8377794`  |
| 1177   | No file  | `ecd6a8377794`  |
| 1173   | No file  | `ecd6a8377794`  |
| 1167   | No file  | `ecd6a8377794`  |
| 1164   | No file  | `ecd6a8377794`  |
| 1156   | No file  | `ecd6a8377794`  |
| 1149   | No file  | `ecd6a8377794`  |
| 1144   | No file  | `ecd6a8377794`  |
| 1137   | No file  | `ecd6a8377794`  |
| 1132   | No file  | `ecd6a8377794`  |
| 1127   | No file  | `ecd6a8377794`  |
| 1122   | No file  | `ecd6a8377794`  |
| 1118   | No file  | `ecd6a8377794`  |
| 1114   | No file  | `ecd6a8377794`  |
| 1109   | No file  | `ecd6a8377794`  |
| 1102   | No file  | `ecd6a8377794`  |
| 1096   | No file  | `ecd6a8377794`  |
| 1088   | No file  | `ecd6a8377794`  |
| 1081   | No file  | `ecd6a8377794`  |
| 1076   | No file  | `ecd6a8377794`  |
| 1069   | No file  | `ecd6a8377794`  |
| 1064   | No file  | `ecd6a8377794`  |
| 1058   | No file  | `ecd6a8377794`  |
| 1051   | No file  | `ecd6a8377794`  |
| 1044   | No file  | `ecd6a8377794`  |
| 1036   | No file  | `ecd6a8377794`  |
| 1026   | No file  | `ecd6a8377794`  |
| 1016   | No file  | `ecd6a8377794`  |
| 1009   | No file  | `ecd6a8377794`  |
| 1005   | No file  | `ecd6a8377794`  |
| 1000   | No file  | `ecd6a8377794`  |
| 998    | No file  | `ecd6a8377794`  |
| 990    | No file  | `ecd6a8377794`  |
| 979    | No file  | `ecd6a8377794`  |
| 972    | No file  | `ecd6a8377794`  |
| 963    | No file  | `ecd6a8377794`  |
| 955    | No file  | `ecd6a8377794`  |
| 946    | No file  | `ecd6a8377794`  |
| 938    | No file  | `ecd6a8377794`  |
| 927    | No file  | `ecd6a8377794`  |
| 911    | No file  | `ecd6a8377794`  |
| 904    | No file  | `ecd6a8377794`  |
| 899    | No file  | `ecd6a8377794`  |
| 894    | No file  | `ecd6a8377794`  |
| 885    | No file  | `ecd6a8377794`  |
| 879    | No file  | `ecd6a8377794`  |
| 872    | No file  | `ecd6a8377794`  |
| 864    | No file  | `ecd6a8377794`  |
| 855    | No file  | `ecd6a8377794`  |
| 853    | No file  | `ecd6a8377794`  |
| 845    | No file  | `ecd6a8377794`  |
| 837    | No file  | `ecd6a8377794`  |
| 829    | No file  | `ecd6a8377794`  |
| 822    | No file  | `ecd6a8377794`  |
| 814    | No file  | `ecd6a8377794`  |
| 805    | No file  | `ecd6a8377794`  |
| 794    | No file  | `ecd6a8377794`  |
| 787    | No file  | `ecd6a8377794`  |
| 780    | No file  | `ecd6a8377794`  |
| 771    | No file  | `ecd6a8377794`  |
| 760    | No file  | `ecd6a8377794`  |
| 748    | No file  | `ecd6a8377794`  |
| 741    | No file  | `ecd6a8377794`  |
| 736    | No file  | `ecd6a8377794`  |
| 731    | No file  | `ecd6a8377794`  |
| 723    | No file  | `ecd6a8377794`  |
| 711    | No file  | `ecd6a8377794`  |
| 707    | No file  | `ecd6a8377794`  |
| 697    | No file  | `ecd6a8377794`  |
| 689    | No file  | `ecd6a8377794`  |
| 683    | No file  | `ecd6a8377794`  |
| 678    | No file  | `ecd6a8377794`  |
| 670    | No file  | `ecd6a8377794`  |
| 661    | No file  | `ecd6a8377794`  |
| 656    | No file  | `ecd6a8377794`  |
| 652    | No file  | `ecd6a8377794`  |
| 643    | No file  | `ecd6a8377794`  |
| 637    | No file  | `ecd6a8377794`  |
| 630    | No file  | `ecd6a8377794`  |
| 627    | No file  | `ecd6a8377794`  |
| 621    | No file  | `ecd6a8377794`  |
| 617    | No file  | `ecd6a8377794`  |
| 615    | No file  | `ecd6a8377794`  |
| 606    | No file  | `ecd6a8377794`  |
| 599    | No file  | `ecd6a8377794`  |
| 592    | No file  | `ecd6a8377794`  |
| 586    | No file  | `ecd6a8377794`  |
| 577    | No file  | `ecd6a8377794`  |
| 569    | No file  | `ecd6a8377794`  |
| 561    | No file  | `ecd6a8377794`  |
| 554    | No file  | `ecd6a8377794`  |
| 542    | No file  | `ecd6a8377794`  |
| 532    | No file  | `ecd6a8377794`  |
| 531    | No file  | `ecd6a8377794`  |
| 526    | No file  | `ecd6a8377794`  |
| 521    | No file  | `ecd6a8377794`  |
| 517    | No file  | `ecd6a8377794`  |
| 510    | No file  | `ecd6a8377794`  |
| 508    | No file  | `ecd6a8377794`  |
| 504    | No file  | `ecd6a8377794`  |
| 497    | No file  | `ecd6a8377794`  |
| 491    | No file  | `ecd6a8377794`  |
| 485    | No file  | `ecd6a8377794`  |
| 478    | No file  | `ecd6a8377794`  |
| 472    | No file  | `ecd6a8377794`  |
| 466    | No file  | `ecd6a8377794`  |
| 457    | No file  | `ecd6a8377794`  |
| 452    | No file  | `ecd6a8377794`  |
| 449    | No file  | `ecd6a8377794`  |
| 435    | No file  | `ecd6a8377794`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                              |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Node names (LOC type 29), knowledge names (LOC type 34), region names (LOC type 17), territory names (LOC type 37 under the GAME sheet key hash) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of destinations; `ToClient_GetMagnusEasyTeleportInfoCount()` |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (32 bytes)

| Offset  | Type | Field           | Notes                                                                                   |
| ------- | ---- | --------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u16  | waypoint_key    | Node key (LOC type 29 name) near the destination                                       |
| `+0x02` | f32  | x               | World X of the destination                                                              |
| `+0x06` | f32  | y               | World Y (height)                                                                        |
| `+0x0A` | f32  | z               | World Z                                                                                 |
| `+0x0E` | u32  | name_ref        | String-table index of the GAME sheet key of the button text; `getName()`                |
| `+0x12` | u32  | mental_card_key | `getMentalCardKeyRaw()`, the knowledge (LOC type 34) whose card shows the button        |
| `+0x16` | u64  | unknown_16      | `1` on every row of client 3482                                                         |
| `+0x1E` | u16  | region_key      | `regioninfo.bss` region key (LOC type 17); see Field Names                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                           |
| ------- | ------------------ | ------------ | --------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; one per row                                  |
| `+0x04` | pstr[string_count] | strings      | UTF-8 GAME sheet keys (`LUA_WORLDMAP_TERRITORYSTRING_0`), in row order |

## Layout 1

### Row (28 bytes)

| Offset  | Type | Field        | Notes                                                        |
| ------- | ---- | ------------ | ------------------------------------------------------------ |
| `+0x00` | u16  | waypoint_key | Node key near the destination                                |
| `+0x02` | f32  | x            | World X of the destination                                   |
| `+0x06` | f32  | y            | World Y (height)                                             |
| `+0x0A` | f32  | z            | World Z                                                      |
| `+0x0E` | u32  | name_ref     | String-table index of the GAME sheet key of the button text  |
| `+0x12` | u64  | unknown_16   | `1` on every row; no `mental_card_key` before it             |
| `+0x1A` | u16  | region_key   | `regioninfo.bss` region key                                  |

## Destinations

Client 3482, in file order, with the LOC names.

| Row | `waypoint_key`              | `name_ref` text                     | `mental_card_key`              | `region_key`               |
| --- | --------------------------- | ----------------------------------- | ------------------------------ | -------------------------- |
| 0   | 1 Velia                     | Balenos                             | 3001 Velia                     | 16 Bartali Farm            |
| 1   | 308 Eastern Border          | Serendia                            | 3058 Heidel, Serendia          | 318 Moretti Plantation     |
| 2   | 661 Falres Dirt Farm        | Calpheon                            | 3177 Calpheon                  | 300 Gabino Farm            |
| 3   | 1147 Stonebeak Shore        | Mediah                              | 3188 Altinova                  | 236 Altinova Gateway       |
| 4   | 1356 Fohalam Farm           | Valencia                            | 3364 Valencia City             | 639 Erdal Farm             |
| 5   | 1622 Lake Flondor           | Kamasylvia                          | 3454 Grána                     | 735 Grána                  |
| 6   | 1741 Salanar Pond           | O'dyllita                           | 3494 O'draxxia                 | 1023 Delmira Plantation    |
| 7   | 1649 Duvencrune             | Drieghan                            | 3472 Duvencrune                | 903 Marak Farm             |
| 8   | 1762 Zvier Highlands        | Mountain of Eternal Winter          | 3537 Eilton                    | 1121 Erethea's Belt        |
| 9   | 1785 Nampo's Moodle Village | Land of the Morning Light - Nampo   | 3573 Nampo's Moodle Village    | 1319 Chief's Home          |
| 10  | 1843 Muzgar                 | Ulukita                             | 3594 Muzgar                    | 1375 Muzgar                |
| 11  | 1727 Oquilla's Eye          | Oquilla's Eye                       | 3001 Velia                     | 1000 Oquilla's Eye         |
| 12  | 1853 Yukjo Street           | Land of the Morning Light - Seoul   | 3626 Seoul                     | 1420 Yukjo Street          |
| 13  | 2001 Hakinza Sanctuary      | Outer Edania                        | 14195 Hakinza Sanctuary        | 1553 Hakinza Sanctuary     |
| 14  | 2052 Olvia Academy          | Olvia Academy                       | 14691 Olvia Academy            | 1677 Olvia Academy Grounds |
| 15  | 2057 Angavu Outpost         | Inner Edania                        | 15127 Angavu Outpost           | 1733 Angavu Outpost        |

## Field Names

The Magnus is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers this file. The client 3482 Lua
reads each row with `ToClient_GetMagnusEasyTeleportInfoByIndex(idx)` and
three getters, `getName()`, `getMentalCardKeyRaw()` and
`getRegionKeyRaw()`:

- `name_ref`: `PAGetString(Defines.StringSheet_GAME, info:getName())`
  sets the button text, and every string is a GAME sheet key.
- `mental_card_key`: `ToClinet_getMentalCardStaticStatus(mentalCardKeyRaw):isHasCard()`
  shows the button; every value has a LOC type 34 knowledge name, on 15
  of 16 rows the city of the destination (row 11, Oquilla's Eye, holds
  Velia `3001`, as row 0 does).
- `waypoint_key`: every value has a LOC type 29 node name, and the node's
  world position in `exploration.bss` lies near `x` and `z` (Velia node
  `1` at `13800, 76996` against `-4222, 75613`; Eastern Border `308` at
  `99370, -39348` against `100689, -38203`).
- `region_key`: every value has a LOC type 17 region name, and the 16
  values are the 16 `region_key_1` values of
  [`abyssmovecost.bss`](abyssmovecost_bss.md#free-moves), the Magnus move
  regions.
- `x`, `y` and `z` read as a world position by the node distances above.

`getRegionKeyRaw()` goes to `ToClient_getRegionInfoWrapperByWaypoint`,
which takes a waypoint key; whether it returns `waypoint_key` or
`region_key` is open (see Open Questions).

## Notes

- Layout 1 (clients 2438 to 3103) has no `mental_card_key`; client 3103
  lists 14 destinations.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`.

## Open Questions

### Which Key getRegionKeyRaw Returns

The Lua passes `getRegionKeyRaw()` to
`ToClient_getRegionInfoWrapperByWaypoint` and skips the row when no
region comes back. `waypoint_key` holds node keys, which that call takes;
`region_key` holds region keys, which match the getter's name. `unknown_16`
is `1` on every row and is the only other unnamed field.
