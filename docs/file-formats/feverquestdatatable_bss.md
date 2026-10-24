# `feverquestdatatable.bss` Format

## Purpose

The Agris Fever quests: one 8-byte row per quest with the Agris Fever
points that accepting it costs. On client 3474 the file lists the eleven
quests of chain 9026 (`Agris: Challenging the Bashims` to `Agris: Tensions
at the Sulfur Mine`), each at `15000`. The quest window and the world map
quest widget show the cost as `Consume {point} Agris Point(s)`. The plain
PABR file holds the rows, then an empty string table. The drop skills that
Agris Fever applies are in [`fevertimeskill.bss`](fevertimeskill_bss.md),
next to this file in the same PAZ.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------------ | --------- |
| 1      | 1565 and later | 3483    | `feverquestdatatable.bss` | 108   | 11 Fever Quest Row | 8         |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 1      | `feverquestdatatable.bss` | 108 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `87e577fdc58a`  |
| 3482   | Layout 1 | `87e577fdc58a`  |
| 3474   | Layout 1 | `87e577fdc58a`  |
| 3473   | Layout 1 | `87e577fdc58a`  |
| 3464   | Layout 1 | `87e577fdc58a`  |
| 3458   | Layout 1 | `87e577fdc58a`  |
| 3454   | Layout 1 | `87e577fdc58a`  |
| 3444   | Layout 1 | `87e577fdc58a`  |
| 3435   | Layout 1 | `87e577fdc58a`  |
| 3426   | Layout 1 | `87e577fdc58a`  |
| 3418   | Layout 1 | `87e577fdc58a`  |
| 3412   | Layout 1 | `87e577fdc58a`  |
| 3402   | Layout 1 | `87e577fdc58a`  |
| 3396   | Layout 1 | `87e577fdc58a`  |
| 3387   | Layout 1 | `87e577fdc58a`  |
| 3381   | Layout 1 | `87e577fdc58a`  |
| 3373   | Layout 1 | `87e577fdc58a`  |
| 3364   | Layout 1 | `87e577fdc58a`  |
| 3356   | Layout 1 | `87e577fdc58a`  |
| 3349   | Layout 1 | `87e577fdc58a`  |
| 3342   | Layout 1 | `87e577fdc58a`  |
| 3335   | Layout 1 | `87e577fdc58a`  |
| 3326   | Layout 1 | `87e577fdc58a`  |
| 3321   | Layout 1 | `87e577fdc58a`  |
| 3314   | Layout 1 | `87e577fdc58a`  |
| 3303   | Layout 1 | `87e577fdc58a`  |
| 3302   | Layout 1 | `87e577fdc58a`  |
| 3293   | Layout 1 | `87e577fdc58a`  |
| 3283   | Layout 1 | `87e577fdc58a`  |
| 3275   | Layout 1 | `87e577fdc58a`  |
| 3267   | Layout 1 | `87e577fdc58a`  |
| 3258   | Layout 1 | `87e577fdc58a`  |
| 3251   | Layout 1 | `87e577fdc58a`  |
| 3242   | Layout 1 | `87e577fdc58a`  |
| 3235   | Layout 1 | `87e577fdc58a`  |
| 3229   | Layout 1 | `87e577fdc58a`  |
| 3212   | Layout 1 | `87e577fdc58a`  |
| 3203   | Layout 1 | `87e577fdc58a`  |
| 3193   | Layout 1 | `87e577fdc58a`  |
| 3186   | Layout 1 | `87e577fdc58a`  |
| 3177   | Layout 1 | `87e577fdc58a`  |
| 3169   | Layout 1 | `87e577fdc58a`  |
| 3158   | Layout 1 | `87e577fdc58a`  |
| 3151   | Layout 1 | `87e577fdc58a`  |
| 3144   | Layout 1 | `87e577fdc58a`  |
| 3133   | Layout 1 | `87e577fdc58a`  |
| 3125   | Layout 1 | `87e577fdc58a`  |
| 3118   | Layout 1 | `87e577fdc58a`  |
| 3111   | Layout 1 | `87e577fdc58a`  |
| 3103   | Layout 1 | `87e577fdc58a`  |
| 3095   | Layout 1 | `87e577fdc58a`  |
| 3086   | Layout 1 | `87e577fdc58a`  |
| 3072   | Layout 1 | `87e577fdc58a`  |
| 3062   | Layout 1 | `87e577fdc58a`  |
| 3052   | Layout 1 | `87e577fdc58a`  |
| 3045   | Layout 1 | `87e577fdc58a`  |
| 3037   | Layout 1 | `87e577fdc58a`  |
| 3030   | Layout 1 | `87e577fdc58a`  |
| 3021   | Layout 1 | `87e577fdc58a`  |
| 3012   | Layout 1 | `87e577fdc58a`  |
| 3002   | Layout 1 | `87e577fdc58a`  |
| 2995   | Layout 1 | `87e577fdc58a`  |
| 2987   | Layout 1 | `87e577fdc58a`  |
| 2978   | Layout 1 | `87e577fdc58a`  |
| 2970   | Layout 1 | `87e577fdc58a`  |
| 2959   | Layout 1 | `87e577fdc58a`  |
| 2951   | Layout 1 | `87e577fdc58a`  |
| 2942   | Layout 1 | `87e577fdc58a`  |
| 2935   | Layout 1 | `87e577fdc58a`  |
| 2932   | Layout 1 | `87e577fdc58a`  |
| 2923   | Layout 1 | `87e577fdc58a`  |
| 2919   | Layout 1 | `87e577fdc58a`  |
| 2907   | Layout 1 | `87e577fdc58a`  |
| 2900   | Layout 1 | `87e577fdc58a`  |
| 2891   | Layout 1 | `87e577fdc58a`  |
| 2882   | Layout 1 | `87e577fdc58a`  |
| 2872   | Layout 1 | `87e577fdc58a`  |
| 2863   | Layout 1 | `87e577fdc58a`  |
| 2855   | Layout 1 | `87e577fdc58a`  |
| 2849   | Layout 1 | `87e577fdc58a`  |
| 2844   | Layout 1 | `87e577fdc58a`  |
| 2834   | Layout 1 | `87e577fdc58a`  |
| 2825   | Layout 1 | `87e577fdc58a`  |
| 2819   | Layout 1 | `87e577fdc58a`  |
| 2811   | Layout 1 | `87e577fdc58a`  |
| 2803   | Layout 1 | `87e577fdc58a`  |
| 2794   | Layout 1 | `87e577fdc58a`  |
| 2783   | Layout 1 | `87e577fdc58a`  |
| 2774   | Layout 1 | `87e577fdc58a`  |
| 2765   | Layout 1 | `87e577fdc58a`  |
| 2756   | Layout 1 | `87e577fdc58a`  |
| 2750   | Layout 1 | `87e577fdc58a`  |
| 2743   | Layout 1 | `87e577fdc58a`  |
| 2736   | Layout 1 | `87e577fdc58a`  |
| 2726   | Layout 1 | `87e577fdc58a`  |
| 2717   | Layout 1 | `87e577fdc58a`  |
| 2709   | Layout 1 | `87e577fdc58a`  |
| 2703   | Layout 1 | `87e577fdc58a`  |
| 2695   | Layout 1 | `87e577fdc58a`  |
| 2684   | Layout 1 | `87e577fdc58a`  |
| 2672   | Layout 1 | `87e577fdc58a`  |
| 2665   | Layout 1 | `87e577fdc58a`  |
| 2657   | Layout 1 | `87e577fdc58a`  |
| 2649   | Layout 1 | `87e577fdc58a`  |
| 2644   | Layout 1 | `87e577fdc58a`  |
| 2637   | Layout 1 | `87e577fdc58a`  |
| 2629   | Layout 1 | `87e577fdc58a`  |
| 2619   | Layout 1 | `87e577fdc58a`  |
| 2612   | Layout 1 | `87e577fdc58a`  |
| 2606   | Layout 1 | `87e577fdc58a`  |
| 2602   | Layout 1 | `87e577fdc58a`  |
| 2601   | Layout 1 | `87e577fdc58a`  |
| 2592   | Layout 1 | `87e577fdc58a`  |
| 2583   | Layout 1 | `87e577fdc58a`  |
| 2575   | Layout 1 | `87e577fdc58a`  |
| 2567   | Layout 1 | `87e577fdc58a`  |
| 2560   | Layout 1 | `87e577fdc58a`  |
| 2553   | Layout 1 | `87e577fdc58a`  |
| 2545   | Layout 1 | `87e577fdc58a`  |
| 2538   | Layout 1 | `87e577fdc58a`  |
| 2529   | Layout 1 | `87e577fdc58a`  |
| 2519   | Layout 1 | `87e577fdc58a`  |
| 2513   | Layout 1 | `87e577fdc58a`  |
| 2510   | Layout 1 | `87e577fdc58a`  |
| 2507   | Layout 1 | `87e577fdc58a`  |
| 2503   | Layout 1 | `87e577fdc58a`  |
| 2498   | Layout 1 | `87e577fdc58a`  |
| 2492   | Layout 1 | `87e577fdc58a`  |
| 2487   | Layout 1 | `87e577fdc58a`  |
| 2480   | Layout 1 | `87e577fdc58a`  |
| 2474   | Layout 1 | `87e577fdc58a`  |
| 2468   | Layout 1 | `87e577fdc58a`  |
| 2460   | Layout 1 | `87e577fdc58a`  |
| 2453   | Layout 1 | `87e577fdc58a`  |
| 2444   | Layout 1 | `87e577fdc58a`  |
| 2438   | Layout 1 | `87e577fdc58a`  |
| 2434   | Layout 1 | `87e577fdc58a`  |
| 2429   | Layout 1 | `87e577fdc58a`  |
| 2421   | Layout 1 | `87e577fdc58a`  |
| 2414   | Layout 1 | `87e577fdc58a`  |
| 2407   | Layout 1 | `87e577fdc58a`  |
| 2401   | Layout 1 | `87e577fdc58a`  |
| 2397   | Layout 1 | `87e577fdc58a`  |
| 2393   | Layout 1 | `87e577fdc58a`  |
| 2384   | Layout 1 | `87e577fdc58a`  |
| 2378   | Layout 1 | `87e577fdc58a`  |
| 2372   | Layout 1 | `87e577fdc58a`  |
| 2358   | Layout 1 | `87e577fdc58a`  |
| 2352   | Layout 1 | `87e577fdc58a`  |
| 2347   | Layout 1 | `87e577fdc58a`  |
| 2343   | Layout 1 | `87e577fdc58a`  |
| 2335   | Layout 1 | `87e577fdc58a`  |
| 2327   | Layout 1 | `87e577fdc58a`  |
| 2324   | Layout 1 | `87e577fdc58a`  |
| 2319   | Layout 1 | `87e577fdc58a`  |
| 2313   | Layout 1 | `87e577fdc58a`  |
| 2308   | Layout 1 | `87e577fdc58a`  |
| 2302   | Layout 1 | `87e577fdc58a`  |
| 2295   | Layout 1 | `87e577fdc58a`  |
| 2290   | Layout 1 | `87e577fdc58a`  |
| 2284   | Layout 1 | `87e577fdc58a`  |
| 2276   | Layout 1 | `87e577fdc58a`  |
| 2269   | Layout 1 | `87e577fdc58a`  |
| 2259   | Layout 1 | `87e577fdc58a`  |
| 2250   | Layout 1 | `87e577fdc58a`  |
| 2243   | Layout 1 | `87e577fdc58a`  |
| 2235   | Layout 1 | `87e577fdc58a`  |
| 2229   | Layout 1 | `87e577fdc58a`  |
| 2224   | Layout 1 | `87e577fdc58a`  |
| 2218   | Layout 1 | `87e577fdc58a`  |
| 2215   | Layout 1 | `87e577fdc58a`  |
| 2207   | Layout 1 | `87e577fdc58a`  |
| 2203   | Layout 1 | `87e577fdc58a`  |
| 2196   | Layout 1 | `87e577fdc58a`  |
| 2192   | Layout 1 | `87e577fdc58a`  |
| 2189   | Layout 1 | `87e577fdc58a`  |
| 2183   | Layout 1 | `87e577fdc58a`  |
| 2179   | Layout 1 | `87e577fdc58a`  |
| 2171   | Layout 1 | `87e577fdc58a`  |
| 2163   | Layout 1 | `87e577fdc58a`  |
| 2156   | Layout 1 | `87e577fdc58a`  |
| 2151   | Layout 1 | `87e577fdc58a`  |
| 2147   | Layout 1 | `87e577fdc58a`  |
| 2142   | Layout 1 | `87e577fdc58a`  |
| 2138   | Layout 1 | `87e577fdc58a`  |
| 2134   | Layout 1 | `87e577fdc58a`  |
| 2130   | Layout 1 | `87e577fdc58a`  |
| 2122   | Layout 1 | `87e577fdc58a`  |
| 2107   | Layout 1 | `87e577fdc58a`  |
| 2098   | Layout 1 | `87e577fdc58a`  |
| 2089   | Layout 1 | `87e577fdc58a`  |
| 2081   | Layout 1 | `87e577fdc58a`  |
| 2073   | Layout 1 | `87e577fdc58a`  |
| 2067   | Layout 1 | `87e577fdc58a`  |
| 2063   | Layout 1 | `87e577fdc58a`  |
| 2059   | Layout 1 | `87e577fdc58a`  |
| 2052   | Layout 1 | `87e577fdc58a`  |
| 2044   | Layout 1 | `87e577fdc58a`  |
| 2039   | Layout 1 | `87e577fdc58a`  |
| 2032   | Layout 1 | `87e577fdc58a`  |
| 2025   | Layout 1 | `87e577fdc58a`  |
| 2011   | Layout 1 | `87e577fdc58a`  |
| 2005   | Layout 1 | `87e577fdc58a`  |
| 2000   | Layout 1 | `87e577fdc58a`  |
| 1996   | Layout 1 | `87e577fdc58a`  |
| 1991   | Layout 1 | `87e577fdc58a`  |
| 1985   | Layout 1 | `87e577fdc58a`  |
| 1980   | Layout 1 | `87e577fdc58a`  |
| 1969   | Layout 1 | `87e577fdc58a`  |
| 1964   | Layout 1 | `87e577fdc58a`  |
| 1958   | Layout 1 | `87e577fdc58a`  |
| 1950   | Layout 1 | `87e577fdc58a`  |
| 1945   | Layout 1 | `87e577fdc58a`  |
| 1937   | Layout 1 | `87e577fdc58a`  |
| 1933   | Layout 1 | `87e577fdc58a`  |
| 1927   | Layout 1 | `87e577fdc58a`  |
| 1921   | Layout 1 | `87e577fdc58a`  |
| 1914   | Layout 1 | `87e577fdc58a`  |
| 1908   | Layout 1 | `87e577fdc58a`  |
| 1897   | Layout 1 | `87e577fdc58a`  |
| 1892   | Layout 1 | `87e577fdc58a`  |
| 1886   | Layout 1 | `87e577fdc58a`  |
| 1881   | Layout 1 | `87e577fdc58a`  |
| 1871   | Layout 1 | `87e577fdc58a`  |
| 1866   | Layout 1 | `87e577fdc58a`  |
| 1862   | Layout 1 | `87e577fdc58a`  |
| 1854   | Layout 1 | `87e577fdc58a`  |
| 1846   | Layout 1 | `87e577fdc58a`  |
| 1838   | Layout 1 | `87e577fdc58a`  |
| 1832   | Layout 1 | `87e577fdc58a`  |
| 1826   | Layout 1 | `87e577fdc58a`  |
| 1822   | Layout 1 | `87e577fdc58a`  |
| 1818   | Layout 1 | `87e577fdc58a`  |
| 1804   | Layout 1 | `87e577fdc58a`  |
| 1794   | Layout 1 | `87e577fdc58a`  |
| 1790   | Layout 1 | `87e577fdc58a`  |
| 1784   | Layout 1 | `87e577fdc58a`  |
| 1774   | Layout 1 | `87e577fdc58a`  |
| 1771   | Layout 1 | `87e577fdc58a`  |
| 1762   | Layout 1 | `87e577fdc58a`  |
| 1759   | Layout 1 | `87e577fdc58a`  |
| 1754   | Layout 1 | `87e577fdc58a`  |
| 1749   | Layout 1 | `87e577fdc58a`  |
| 1743   | Layout 1 | `87e577fdc58a`  |
| 1737   | Layout 1 | `87e577fdc58a`  |
| 1731   | Layout 1 | `87e577fdc58a`  |
| 1725   | Layout 1 | `87e577fdc58a`  |
| 1717   | Layout 1 | `87e577fdc58a`  |
| 1710   | Layout 1 | `87e577fdc58a`  |
| 1704   | Layout 1 | `87e577fdc58a`  |
| 1698   | Layout 1 | `87e577fdc58a`  |
| 1690   | Layout 1 | `87e577fdc58a`  |
| 1685   | Layout 1 | `87e577fdc58a`  |
| 1680   | Layout 1 | `87e577fdc58a`  |
| 1674   | Layout 1 | `87e577fdc58a`  |
| 1668   | Layout 1 | `87e577fdc58a`  |
| 1659   | Layout 1 | `87e577fdc58a`  |
| 1649   | Layout 1 | `87e577fdc58a`  |
| 1642   | Layout 1 | `87e577fdc58a`  |
| 1636   | Layout 1 | `87e577fdc58a`  |
| 1628   | Layout 1 | `87e577fdc58a`  |
| 1622   | Layout 1 | `87e577fdc58a`  |
| 1614   | Layout 1 | `87e577fdc58a`  |
| 1608   | Layout 1 | `87e577fdc58a`  |
| 1602   | Layout 1 | `87e577fdc58a`  |
| 1598   | Layout 1 | `87e577fdc58a`  |
| 1594   | Layout 1 | `87e577fdc58a`  |
| 1590   | Layout 1 | `87e577fdc58a`  |
| 1587   | Layout 1 | `87e577fdc58a`  |
| 1584   | Layout 1 | `87e577fdc58a`  |
| 1579   | Layout 1 | `87e577fdc58a`  |
| 1572   | Layout 1 | `87e577fdc58a`  |
| 1565   | Layout 1 | `87e577fdc58a`  |
| 1559   | No file  | `87e577fdc58a`  |
| 1554   | No file  | `87e577fdc58a`  |
| 1547   | No file  | `87e577fdc58a`  |
| 1537   | No file  | `87e577fdc58a`  |
| 1529   | No file  | `87e577fdc58a`  |
| 1524   | No file  | `87e577fdc58a`  |
| 1519   | No file  | `87e577fdc58a`  |
| 1509   | No file  | `87e577fdc58a`  |
| 1506   | No file  | `87e577fdc58a`  |
| 1504   | No file  | `87e577fdc58a`  |
| 1500   | No file  | `87e577fdc58a`  |
| 1493   | No file  | `87e577fdc58a`  |
| 1489   | No file  | `87e577fdc58a`  |
| 1485   | No file  | `87e577fdc58a`  |
| 1481   | No file  | `87e577fdc58a`  |
| 1474   | No file  | `87e577fdc58a`  |
| 1466   | No file  | `87e577fdc58a`  |
| 1462   | No file  | `87e577fdc58a`  |
| 1459   | No file  | `87e577fdc58a`  |
| 1453   | No file  | `87e577fdc58a`  |
| 1450   | No file  | `87e577fdc58a`  |
| 1445   | No file  | `87e577fdc58a`  |
| 1439   | No file  | `87e577fdc58a`  |
| 1433   | No file  | `87e577fdc58a`  |
| 1430   | No file  | `87e577fdc58a`  |
| 1426   | No file  | `87e577fdc58a`  |
| 1421   | No file  | `87e577fdc58a`  |
| 1417   | No file  | `87e577fdc58a`  |
| 1416   | No file  | `87e577fdc58a`  |
| 1409   | No file  | `87e577fdc58a`  |
| 1405   | No file  | `87e577fdc58a`  |
| 1401   | No file  | `87e577fdc58a`  |
| 1396   | No file  | `87e577fdc58a`  |
| 1391   | No file  | `87e577fdc58a`  |
| 1390   | No file  | `87e577fdc58a`  |
| 1386   | No file  | `87e577fdc58a`  |
| 1381   | No file  | `87e577fdc58a`  |
| 1379   | No file  | `87e577fdc58a`  |
| 1372   | No file  | `87e577fdc58a`  |
| 1366   | No file  | `87e577fdc58a`  |
| 1364   | No file  | `87e577fdc58a`  |
| 1363   | No file  | `87e577fdc58a`  |
| 1360   | No file  | `87e577fdc58a`  |
| 1358   | No file  | `87e577fdc58a`  |
| 1355   | No file  | `87e577fdc58a`  |
| 1351   | No file  | `87e577fdc58a`  |
| 1348   | No file  | `87e577fdc58a`  |
| 1346   | No file  | `87e577fdc58a`  |
| 1341   | No file  | `87e577fdc58a`  |
| 1340   | No file  | `87e577fdc58a`  |
| 1338   | No file  | `87e577fdc58a`  |
| 1335   | No file  | `87e577fdc58a`  |
| 1333   | No file  | `87e577fdc58a`  |
| 1329   | No file  | `87e577fdc58a`  |
| 1327   | No file  | `87e577fdc58a`  |
| 1324   | No file  | `87e577fdc58a`  |
| 1321   | No file  | `87e577fdc58a`  |
| 1319   | No file  | `87e577fdc58a`  |
| 1318   | No file  | `87e577fdc58a`  |
| 1316   | No file  | `87e577fdc58a`  |
| 1313   | No file  | `87e577fdc58a`  |
| 1311   | No file  | `87e577fdc58a`  |
| 1309   | No file  | `87e577fdc58a`  |
| 1304   | No file  | `87e577fdc58a`  |
| 1292   | No file  | `87e577fdc58a`  |
| 1286   | No file  | `87e577fdc58a`  |
| 1280   | No file  | `87e577fdc58a`  |
| 1276   | No file  | `87e577fdc58a`  |
| 1267   | No file  | `87e577fdc58a`  |
| 1261   | No file  | `87e577fdc58a`  |
| 1256   | No file  | `87e577fdc58a`  |
| 1250   | No file  | `87e577fdc58a`  |
| 1246   | No file  | `87e577fdc58a`  |
| 1239   | No file  | `87e577fdc58a`  |
| 1230   | No file  | `87e577fdc58a`  |
| 1226   | No file  | `87e577fdc58a`  |
| 1220   | No file  | `87e577fdc58a`  |
| 1217   | No file  | `87e577fdc58a`  |
| 1211   | No file  | `87e577fdc58a`  |
| 1210   | No file  | `87e577fdc58a`  |
| 1208   | No file  | `87e577fdc58a`  |
| 1203   | No file  | `87e577fdc58a`  |
| 1197   | No file  | `87e577fdc58a`  |
| 1194   | No file  | `87e577fdc58a`  |
| 1192   | No file  | `87e577fdc58a`  |
| 1187   | No file  | `87e577fdc58a`  |
| 1183   | No file  | `87e577fdc58a`  |
| 1177   | No file  | `87e577fdc58a`  |
| 1173   | No file  | `87e577fdc58a`  |
| 1167   | No file  | `87e577fdc58a`  |
| 1164   | No file  | `87e577fdc58a`  |
| 1156   | No file  | `87e577fdc58a`  |
| 1149   | No file  | `87e577fdc58a`  |
| 1144   | No file  | `87e577fdc58a`  |
| 1137   | No file  | `87e577fdc58a`  |
| 1132   | No file  | `87e577fdc58a`  |
| 1127   | No file  | `87e577fdc58a`  |
| 1122   | No file  | `87e577fdc58a`  |
| 1118   | No file  | `87e577fdc58a`  |
| 1114   | No file  | `87e577fdc58a`  |
| 1109   | No file  | `87e577fdc58a`  |
| 1102   | No file  | `87e577fdc58a`  |
| 1096   | No file  | `87e577fdc58a`  |
| 1088   | No file  | `87e577fdc58a`  |
| 1081   | No file  | `87e577fdc58a`  |
| 1076   | No file  | `87e577fdc58a`  |
| 1069   | No file  | `87e577fdc58a`  |
| 1064   | No file  | `87e577fdc58a`  |
| 1058   | No file  | `87e577fdc58a`  |
| 1051   | No file  | `87e577fdc58a`  |
| 1044   | No file  | `87e577fdc58a`  |
| 1036   | No file  | `87e577fdc58a`  |
| 1026   | No file  | `87e577fdc58a`  |
| 1016   | No file  | `87e577fdc58a`  |
| 1009   | No file  | `87e577fdc58a`  |
| 1005   | No file  | `87e577fdc58a`  |
| 1000   | No file  | `87e577fdc58a`  |
| 998    | No file  | `87e577fdc58a`  |
| 990    | No file  | `87e577fdc58a`  |
| 979    | No file  | `87e577fdc58a`  |
| 972    | No file  | `87e577fdc58a`  |
| 963    | No file  | `87e577fdc58a`  |
| 955    | No file  | `87e577fdc58a`  |
| 946    | No file  | `87e577fdc58a`  |
| 938    | No file  | `87e577fdc58a`  |
| 927    | No file  | `87e577fdc58a`  |
| 911    | No file  | `87e577fdc58a`  |
| 904    | No file  | `87e577fdc58a`  |
| 899    | No file  | `87e577fdc58a`  |
| 894    | No file  | `87e577fdc58a`  |
| 885    | No file  | `87e577fdc58a`  |
| 879    | No file  | `87e577fdc58a`  |
| 872    | No file  | `87e577fdc58a`  |
| 864    | No file  | `87e577fdc58a`  |
| 855    | No file  | `87e577fdc58a`  |
| 853    | No file  | `87e577fdc58a`  |
| 845    | No file  | `87e577fdc58a`  |
| 837    | No file  | `87e577fdc58a`  |
| 829    | No file  | `87e577fdc58a`  |
| 822    | No file  | `87e577fdc58a`  |
| 814    | No file  | `87e577fdc58a`  |
| 805    | No file  | `87e577fdc58a`  |
| 794    | No file  | `87e577fdc58a`  |
| 787    | No file  | `87e577fdc58a`  |
| 780    | No file  | `87e577fdc58a`  |
| 771    | No file  | `87e577fdc58a`  |
| 760    | No file  | `87e577fdc58a`  |
| 748    | No file  | `87e577fdc58a`  |
| 741    | No file  | `87e577fdc58a`  |
| 736    | No file  | `87e577fdc58a`  |
| 731    | No file  | `87e577fdc58a`  |
| 723    | No file  | `87e577fdc58a`  |
| 711    | No file  | `87e577fdc58a`  |
| 707    | No file  | `87e577fdc58a`  |
| 697    | No file  | `87e577fdc58a`  |
| 689    | No file  | `87e577fdc58a`  |
| 683    | No file  | `87e577fdc58a`  |
| 678    | No file  | `87e577fdc58a`  |
| 670    | No file  | `87e577fdc58a`  |
| 661    | No file  | `87e577fdc58a`  |
| 656    | No file  | `87e577fdc58a`  |
| 652    | No file  | `87e577fdc58a`  |
| 643    | No file  | `87e577fdc58a`  |
| 637    | No file  | `87e577fdc58a`  |
| 630    | No file  | `87e577fdc58a`  |
| 627    | No file  | `87e577fdc58a`  |
| 621    | No file  | `87e577fdc58a`  |
| 617    | No file  | `87e577fdc58a`  |
| 615    | No file  | `87e577fdc58a`  |
| 606    | No file  | `87e577fdc58a`  |
| 599    | No file  | `87e577fdc58a`  |
| 592    | No file  | `87e577fdc58a`  |
| 586    | No file  | `87e577fdc58a`  |
| 577    | No file  | `87e577fdc58a`  |
| 569    | No file  | `87e577fdc58a`  |
| 561    | No file  | `87e577fdc58a`  |
| 554    | No file  | `87e577fdc58a`  |
| 542    | No file  | `87e577fdc58a`  |
| 532    | No file  | `87e577fdc58a`  |
| 531    | No file  | `87e577fdc58a`  |
| 526    | No file  | `87e577fdc58a`  |
| 521    | No file  | `87e577fdc58a`  |
| 517    | No file  | `87e577fdc58a`  |
| 510    | No file  | `87e577fdc58a`  |
| 508    | No file  | `87e577fdc58a`  |
| 504    | No file  | `87e577fdc58a`  |
| 497    | No file  | `87e577fdc58a`  |
| 491    | No file  | `87e577fdc58a`  |
| 485    | No file  | `87e577fdc58a`  |
| 478    | No file  | `87e577fdc58a`  |
| 472    | No file  | `87e577fdc58a`  |
| 466    | No file  | `87e577fdc58a`  |
| 457    | No file  | `87e577fdc58a`  |
| 452    | No file  | `87e577fdc58a`  |
| 449    | No file  | `87e577fdc58a`  |
| 435    | No file  | `87e577fdc58a`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                      |
| --------------------- | -------- | ------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 at `str_id1=quest_chain_id`, `str_id2=quest_id` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                   | Field              | Notes                                        |
| ------------------- | ---------------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]                | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32                    | count              | Number of rows                               |
| `+0x08`             | Fever Quest Row[count] | rows               | 8-byte rows repeated `count` times           |
| `rows+0x00`         | String Table           | string_table       | See String Table                             |
| `string_table+0x00` | u32                    | string_table_start | Offset of `string_count`, where the rows end |
| `string_table+0x04` | u32                    | zero               | Always `0`                                   |

The string table has the shape `specialquestinfo.bss` and
`questjournalvideoinfo.bss` use (`_common/pabr_strings.py`). The rows are in
quest order, chain first.

### Fever Quest Row (8 bytes)

| Offset  | Type | Field                   | Notes                                                                    |
| ------- | ---- | ----------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | quest_chain_id          | Quest chain (main ID); `quest_id << 16 \| quest_chain_id` is the `packed_quest_id` of a `quest.dbss` record |
| `+0x02` | u16  | quest_id                | Quest within the chain (sub ID)                                          |
| `+0x04` | u32  | consumption_fever_point | Agris Fever points that accepting the quest costs                        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Field Names

The `FeverQuest` sheet of a private server's `DataSheets.bexcel` on client
1784 has three columns: `QuestGroup` (`quest_chain_id`, the name the other
quest tables use), `QuestID` (`quest_id`) and `ConsumptionFeverPoint`
(`consumption_fever_point`). Its 18 rows match the client 1784 file in all
18 rows, in order. The client 3474 file keeps the first 11 of them (chain
9026) with the same values. The server executable of that private server
names the record type `FeverQuestStaticStatus` and its manager
`FeverQuestStaticStatusManager`, which links each row to a quest by
`QuestNo`. The 2016 PDB has no `Fever` symbol.

## Notes

- On client 3474 the file is `108` bytes: 11 rows for quests 9026 / 1 to
  9026 / 11, each at `15000`. Every row is a `quest.dbss` record of category
  9 (Event), and each of them has `checkFeverPoint()>14999` in its
  `condition_script`, the same threshold as the row's cost. No other
  `quest.dbss` record calls `checkFeverPoint`; quests 4465 / 2 and 50041 / 1
  spend points through `checkusefeverpoint(N)` in their action script and
  have no row here.
- Client 1784 has the same layout: `164` bytes, 18 rows. The 7 rows the
  live file dropped are 9030 / 3 to 9030 / 5 (the Vaha weekly quests) and
  9035 / 1 to 9035 / 4 (the Sycrakea weekly chests), each at `20000`. On
  client 3474 those quests are in `quest.dbss` with `getLevel()>99` as their
  only condition, while the item texts of the Vaha quest items (LOC type 0,
  `757175` and `757188`) still say they need 10,000 Agris Fever points.
- The client Lua reads the cost per quest as
  `questStaticInfo:getQuestFeverPoint()`. `panel_window_questinfo_all_1.luac`
  and `panel_widget_randomquestinfo_all_1.luac` show it with the string
  `LUA_WINDOW_QUEST_AGRISDESC` (`Consume {point} Agris Point(s)`) when it is
  above `0`; on the world map the quest window gets an accept button that
  calls `ToClient_AcceptQuest`. Both need contents group `1651`
  (`_ContentsGroup_FeverQuest`), the world map widget also `1654`
  (`_ContentsGroup_WorldmapFeverQuest`). No Lua file names this table.
