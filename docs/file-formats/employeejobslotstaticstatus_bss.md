# `employeejobslotstaticstatus.bss` Format

## Purpose

Sailor preset job slots per ship: for each ship character eight slot
counts, one per preset job of the Sailor Preset window (the
`__eEmployeePresetJob_*` jobs `ViceCaptain`, `Sail`, `Helmsman`,
`CannonSlot`, `Deck`, `Cook`, `Cabin` and `Fishing`; their order in the
row is an open question). After the ships follows a table of 41 entries, keys `0` to
`40`, with values `1` to `8`. On client 3482 the file lists 15 ships, from
the Epheria Sailboat to the four Epheria Carrack types.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ---------------- | --------- |
| 1      | 2825 and later | 3483    | `employeejobslotstaticstatus.bss` | 413   | 15 Row, 41 Entry | 3         |

| Layout | File                              | Known         | Unknown       |
| ------ | --------------------------------- | ------------- | ------------- |
| 1      | `employeejobslotstaticstatus.bss` | 290 B (70.2%) | 123 B (29.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fcbe2e1ec28e`  |
| 3482   | Layout 1 | `fcbe2e1ec28e`  |
| 3474   | Layout 1 | `fcbe2e1ec28e`  |
| 3473   | Layout 1 | `fcbe2e1ec28e`  |
| 3464   | Layout 1 | `fcbe2e1ec28e`  |
| 3458   | Layout 1 | `fcbe2e1ec28e`  |
| 3454   | Layout 1 | `fcbe2e1ec28e`  |
| 3444   | Layout 1 | `fcbe2e1ec28e`  |
| 3435   | Layout 1 | `fcbe2e1ec28e`  |
| 3426   | Layout 1 | `fcbe2e1ec28e`  |
| 3418   | Layout 1 | `fcbe2e1ec28e`  |
| 3412   | Layout 1 | `fcbe2e1ec28e`  |
| 3402   | Layout 1 | `fcbe2e1ec28e`  |
| 3396   | Layout 1 | `fcbe2e1ec28e`  |
| 3387   | Layout 1 | `fcbe2e1ec28e`  |
| 3381   | Layout 1 | `fcbe2e1ec28e`  |
| 3373   | Layout 1 | `fcbe2e1ec28e`  |
| 3364   | Layout 1 | `fcbe2e1ec28e`  |
| 3356   | Layout 1 | `fcbe2e1ec28e`  |
| 3349   | Layout 1 | `fcbe2e1ec28e`  |
| 3342   | Layout 1 | `fcbe2e1ec28e`  |
| 3335   | Layout 1 | `fcbe2e1ec28e`  |
| 3326   | Layout 1 | `fcbe2e1ec28e`  |
| 3321   | Layout 1 | `fcbe2e1ec28e`  |
| 3314   | Layout 1 | `fcbe2e1ec28e`  |
| 3303   | Layout 1 | `fcbe2e1ec28e`  |
| 3302   | Layout 1 | `fcbe2e1ec28e`  |
| 3293   | Layout 1 | `fcbe2e1ec28e`  |
| 3283   | Layout 1 | `fcbe2e1ec28e`  |
| 3275   | Layout 1 | `fcbe2e1ec28e`  |
| 3267   | Layout 1 | `fcbe2e1ec28e`  |
| 3258   | Layout 1 | `fcbe2e1ec28e`  |
| 3251   | Layout 1 | `fcbe2e1ec28e`  |
| 3242   | Layout 1 | `fcbe2e1ec28e`  |
| 3235   | Layout 1 | `fcbe2e1ec28e`  |
| 3229   | Layout 1 | `fcbe2e1ec28e`  |
| 3212   | Layout 1 | `fcbe2e1ec28e`  |
| 3203   | Layout 1 | `fcbe2e1ec28e`  |
| 3193   | Layout 1 | `fcbe2e1ec28e`  |
| 3186   | Layout 1 | `fcbe2e1ec28e`  |
| 3177   | Layout 1 | `fcbe2e1ec28e`  |
| 3169   | Layout 1 | `fcbe2e1ec28e`  |
| 3158   | Layout 1 | `fcbe2e1ec28e`  |
| 3151   | Layout 1 | `fcbe2e1ec28e`  |
| 3144   | Layout 1 | `fcbe2e1ec28e`  |
| 3133   | Layout 1 | `fcbe2e1ec28e`  |
| 3125   | Layout 1 | `fcbe2e1ec28e`  |
| 3118   | Layout 1 | `fcbe2e1ec28e`  |
| 3111   | Layout 1 | `fcbe2e1ec28e`  |
| 3103   | Layout 1 | `fcbe2e1ec28e`  |
| 3095   | Layout 1 | `fcbe2e1ec28e`  |
| 3086   | Layout 1 | `fcbe2e1ec28e`  |
| 3072   | Layout 1 | `fcbe2e1ec28e`  |
| 3062   | Layout 1 | `fcbe2e1ec28e`  |
| 3052   | Layout 1 | `fcbe2e1ec28e`  |
| 3045   | Layout 1 | `fcbe2e1ec28e`  |
| 3037   | Layout 1 | `fcbe2e1ec28e`  |
| 3030   | Layout 1 | `fcbe2e1ec28e`  |
| 3021   | Layout 1 | `fcbe2e1ec28e`  |
| 3012   | Layout 1 | `fcbe2e1ec28e`  |
| 3002   | Layout 1 | `fcbe2e1ec28e`  |
| 2995   | Layout 1 | `fcbe2e1ec28e`  |
| 2987   | Layout 1 | `fcbe2e1ec28e`  |
| 2978   | Layout 1 | `fcbe2e1ec28e`  |
| 2970   | Layout 1 | `fcbe2e1ec28e`  |
| 2959   | Layout 1 | `fcbe2e1ec28e`  |
| 2951   | Layout 1 | `fcbe2e1ec28e`  |
| 2942   | Layout 1 | `fcbe2e1ec28e`  |
| 2935   | Layout 1 | `fcbe2e1ec28e`  |
| 2932   | Layout 1 | `fcbe2e1ec28e`  |
| 2923   | Layout 1 | `fcbe2e1ec28e`  |
| 2919   | Layout 1 | `fcbe2e1ec28e`  |
| 2907   | Layout 1 | `fcbe2e1ec28e`  |
| 2900   | Layout 1 | `fcbe2e1ec28e`  |
| 2891   | Layout 1 | `fcbe2e1ec28e`  |
| 2882   | Layout 1 | `fcbe2e1ec28e`  |
| 2872   | Layout 1 | `fcbe2e1ec28e`  |
| 2863   | Layout 1 | `fcbe2e1ec28e`  |
| 2855   | Layout 1 | `fcbe2e1ec28e`  |
| 2849   | Layout 1 | `fcbe2e1ec28e`  |
| 2844   | Layout 1 | `fcbe2e1ec28e`  |
| 2834   | Layout 1 | `fcbe2e1ec28e`  |
| 2825   | Layout 1 | `fcbe2e1ec28e`  |
| 2819   | No file  | `fcbe2e1ec28e`  |
| 2811   | No file  | `fcbe2e1ec28e`  |
| 2803   | No file  | `fcbe2e1ec28e`  |
| 2794   | No file  | `fcbe2e1ec28e`  |
| 2783   | No file  | `fcbe2e1ec28e`  |
| 2774   | No file  | `fcbe2e1ec28e`  |
| 2765   | No file  | `fcbe2e1ec28e`  |
| 2756   | No file  | `fcbe2e1ec28e`  |
| 2750   | No file  | `fcbe2e1ec28e`  |
| 2743   | No file  | `fcbe2e1ec28e`  |
| 2736   | No file  | `fcbe2e1ec28e`  |
| 2726   | No file  | `fcbe2e1ec28e`  |
| 2717   | No file  | `fcbe2e1ec28e`  |
| 2709   | No file  | `fcbe2e1ec28e`  |
| 2703   | No file  | `fcbe2e1ec28e`  |
| 2695   | No file  | `fcbe2e1ec28e`  |
| 2684   | No file  | `fcbe2e1ec28e`  |
| 2672   | No file  | `fcbe2e1ec28e`  |
| 2665   | No file  | `fcbe2e1ec28e`  |
| 2657   | No file  | `fcbe2e1ec28e`  |
| 2649   | No file  | `fcbe2e1ec28e`  |
| 2644   | No file  | `fcbe2e1ec28e`  |
| 2637   | No file  | `fcbe2e1ec28e`  |
| 2629   | No file  | `fcbe2e1ec28e`  |
| 2619   | No file  | `fcbe2e1ec28e`  |
| 2612   | No file  | `fcbe2e1ec28e`  |
| 2606   | No file  | `fcbe2e1ec28e`  |
| 2602   | No file  | `fcbe2e1ec28e`  |
| 2601   | No file  | `fcbe2e1ec28e`  |
| 2592   | No file  | `fcbe2e1ec28e`  |
| 2583   | No file  | `fcbe2e1ec28e`  |
| 2575   | No file  | `fcbe2e1ec28e`  |
| 2567   | No file  | `fcbe2e1ec28e`  |
| 2560   | No file  | `fcbe2e1ec28e`  |
| 2553   | No file  | `fcbe2e1ec28e`  |
| 2545   | No file  | `fcbe2e1ec28e`  |
| 2538   | No file  | `fcbe2e1ec28e`  |
| 2529   | No file  | `fcbe2e1ec28e`  |
| 2519   | No file  | `fcbe2e1ec28e`  |
| 2513   | No file  | `fcbe2e1ec28e`  |
| 2510   | No file  | `fcbe2e1ec28e`  |
| 2507   | No file  | `fcbe2e1ec28e`  |
| 2503   | No file  | `fcbe2e1ec28e`  |
| 2498   | No file  | `fcbe2e1ec28e`  |
| 2492   | No file  | `fcbe2e1ec28e`  |
| 2487   | No file  | `fcbe2e1ec28e`  |
| 2480   | No file  | `fcbe2e1ec28e`  |
| 2474   | No file  | `fcbe2e1ec28e`  |
| 2468   | No file  | `fcbe2e1ec28e`  |
| 2460   | No file  | `fcbe2e1ec28e`  |
| 2453   | No file  | `fcbe2e1ec28e`  |
| 2444   | No file  | `fcbe2e1ec28e`  |
| 2438   | No file  | `fcbe2e1ec28e`  |
| 2434   | No file  | `fcbe2e1ec28e`  |
| 2429   | No file  | `fcbe2e1ec28e`  |
| 2421   | No file  | `fcbe2e1ec28e`  |
| 2414   | No file  | `fcbe2e1ec28e`  |
| 2407   | No file  | `fcbe2e1ec28e`  |
| 2401   | No file  | `fcbe2e1ec28e`  |
| 2397   | No file  | `fcbe2e1ec28e`  |
| 2393   | No file  | `fcbe2e1ec28e`  |
| 2384   | No file  | `fcbe2e1ec28e`  |
| 2378   | No file  | `fcbe2e1ec28e`  |
| 2372   | No file  | `fcbe2e1ec28e`  |
| 2358   | No file  | `fcbe2e1ec28e`  |
| 2352   | No file  | `fcbe2e1ec28e`  |
| 2347   | No file  | `fcbe2e1ec28e`  |
| 2343   | No file  | `fcbe2e1ec28e`  |
| 2335   | No file  | `fcbe2e1ec28e`  |
| 2327   | No file  | `fcbe2e1ec28e`  |
| 2324   | No file  | `fcbe2e1ec28e`  |
| 2319   | No file  | `fcbe2e1ec28e`  |
| 2313   | No file  | `fcbe2e1ec28e`  |
| 2308   | No file  | `fcbe2e1ec28e`  |
| 2302   | No file  | `fcbe2e1ec28e`  |
| 2295   | No file  | `fcbe2e1ec28e`  |
| 2290   | No file  | `fcbe2e1ec28e`  |
| 2284   | No file  | `fcbe2e1ec28e`  |
| 2276   | No file  | `fcbe2e1ec28e`  |
| 2269   | No file  | `fcbe2e1ec28e`  |
| 2259   | No file  | `fcbe2e1ec28e`  |
| 2250   | No file  | `fcbe2e1ec28e`  |
| 2243   | No file  | `fcbe2e1ec28e`  |
| 2235   | No file  | `fcbe2e1ec28e`  |
| 2229   | No file  | `fcbe2e1ec28e`  |
| 2224   | No file  | `fcbe2e1ec28e`  |
| 2218   | No file  | `fcbe2e1ec28e`  |
| 2215   | No file  | `fcbe2e1ec28e`  |
| 2207   | No file  | `fcbe2e1ec28e`  |
| 2203   | No file  | `fcbe2e1ec28e`  |
| 2196   | No file  | `fcbe2e1ec28e`  |
| 2192   | No file  | `fcbe2e1ec28e`  |
| 2189   | No file  | `fcbe2e1ec28e`  |
| 2183   | No file  | `fcbe2e1ec28e`  |
| 2179   | No file  | `fcbe2e1ec28e`  |
| 2171   | No file  | `fcbe2e1ec28e`  |
| 2163   | No file  | `fcbe2e1ec28e`  |
| 2156   | No file  | `fcbe2e1ec28e`  |
| 2151   | No file  | `fcbe2e1ec28e`  |
| 2147   | No file  | `fcbe2e1ec28e`  |
| 2142   | No file  | `fcbe2e1ec28e`  |
| 2138   | No file  | `fcbe2e1ec28e`  |
| 2134   | No file  | `fcbe2e1ec28e`  |
| 2130   | No file  | `fcbe2e1ec28e`  |
| 2122   | No file  | `fcbe2e1ec28e`  |
| 2107   | No file  | `fcbe2e1ec28e`  |
| 2098   | No file  | `fcbe2e1ec28e`  |
| 2089   | No file  | `fcbe2e1ec28e`  |
| 2081   | No file  | `fcbe2e1ec28e`  |
| 2073   | No file  | `fcbe2e1ec28e`  |
| 2067   | No file  | `fcbe2e1ec28e`  |
| 2063   | No file  | `fcbe2e1ec28e`  |
| 2059   | No file  | `fcbe2e1ec28e`  |
| 2052   | No file  | `fcbe2e1ec28e`  |
| 2044   | No file  | `fcbe2e1ec28e`  |
| 2039   | No file  | `fcbe2e1ec28e`  |
| 2032   | No file  | `fcbe2e1ec28e`  |
| 2025   | No file  | `fcbe2e1ec28e`  |
| 2011   | No file  | `fcbe2e1ec28e`  |
| 2005   | No file  | `fcbe2e1ec28e`  |
| 2000   | No file  | `fcbe2e1ec28e`  |
| 1996   | No file  | `fcbe2e1ec28e`  |
| 1991   | No file  | `fcbe2e1ec28e`  |
| 1985   | No file  | `fcbe2e1ec28e`  |
| 1980   | No file  | `fcbe2e1ec28e`  |
| 1969   | No file  | `fcbe2e1ec28e`  |
| 1964   | No file  | `fcbe2e1ec28e`  |
| 1958   | No file  | `fcbe2e1ec28e`  |
| 1950   | No file  | `fcbe2e1ec28e`  |
| 1945   | No file  | `fcbe2e1ec28e`  |
| 1937   | No file  | `fcbe2e1ec28e`  |
| 1933   | No file  | `fcbe2e1ec28e`  |
| 1927   | No file  | `fcbe2e1ec28e`  |
| 1921   | No file  | `fcbe2e1ec28e`  |
| 1914   | No file  | `fcbe2e1ec28e`  |
| 1908   | No file  | `fcbe2e1ec28e`  |
| 1897   | No file  | `fcbe2e1ec28e`  |
| 1892   | No file  | `fcbe2e1ec28e`  |
| 1886   | No file  | `fcbe2e1ec28e`  |
| 1881   | No file  | `fcbe2e1ec28e`  |
| 1871   | No file  | `fcbe2e1ec28e`  |
| 1866   | No file  | `fcbe2e1ec28e`  |
| 1862   | No file  | `fcbe2e1ec28e`  |
| 1854   | No file  | `fcbe2e1ec28e`  |
| 1846   | No file  | `fcbe2e1ec28e`  |
| 1838   | No file  | `fcbe2e1ec28e`  |
| 1832   | No file  | `fcbe2e1ec28e`  |
| 1826   | No file  | `fcbe2e1ec28e`  |
| 1822   | No file  | `fcbe2e1ec28e`  |
| 1818   | No file  | `fcbe2e1ec28e`  |
| 1804   | No file  | `fcbe2e1ec28e`  |
| 1794   | No file  | `fcbe2e1ec28e`  |
| 1790   | No file  | `fcbe2e1ec28e`  |
| 1784   | No file  | `fcbe2e1ec28e`  |
| 1774   | No file  | `fcbe2e1ec28e`  |
| 1771   | No file  | `fcbe2e1ec28e`  |
| 1762   | No file  | `fcbe2e1ec28e`  |
| 1759   | No file  | `fcbe2e1ec28e`  |
| 1754   | No file  | `fcbe2e1ec28e`  |
| 1749   | No file  | `fcbe2e1ec28e`  |
| 1743   | No file  | `fcbe2e1ec28e`  |
| 1737   | No file  | `fcbe2e1ec28e`  |
| 1731   | No file  | `fcbe2e1ec28e`  |
| 1725   | No file  | `fcbe2e1ec28e`  |
| 1717   | No file  | `fcbe2e1ec28e`  |
| 1710   | No file  | `fcbe2e1ec28e`  |
| 1704   | No file  | `fcbe2e1ec28e`  |
| 1698   | No file  | `fcbe2e1ec28e`  |
| 1690   | No file  | `fcbe2e1ec28e`  |
| 1685   | No file  | `fcbe2e1ec28e`  |
| 1680   | No file  | `fcbe2e1ec28e`  |
| 1674   | No file  | `fcbe2e1ec28e`  |
| 1668   | No file  | `fcbe2e1ec28e`  |
| 1659   | No file  | `fcbe2e1ec28e`  |
| 1649   | No file  | `fcbe2e1ec28e`  |
| 1642   | No file  | `fcbe2e1ec28e`  |
| 1636   | No file  | `fcbe2e1ec28e`  |
| 1628   | No file  | `fcbe2e1ec28e`  |
| 1622   | No file  | `fcbe2e1ec28e`  |
| 1614   | No file  | `fcbe2e1ec28e`  |
| 1608   | No file  | `fcbe2e1ec28e`  |
| 1602   | No file  | `fcbe2e1ec28e`  |
| 1598   | No file  | `fcbe2e1ec28e`  |
| 1594   | No file  | `fcbe2e1ec28e`  |
| 1590   | No file  | `fcbe2e1ec28e`  |
| 1587   | No file  | `fcbe2e1ec28e`  |
| 1584   | No file  | `fcbe2e1ec28e`  |
| 1579   | No file  | `fcbe2e1ec28e`  |
| 1572   | No file  | `fcbe2e1ec28e`  |
| 1565   | No file  | `fcbe2e1ec28e`  |
| 1559   | No file  | `fcbe2e1ec28e`  |
| 1554   | No file  | `fcbe2e1ec28e`  |
| 1547   | No file  | `fcbe2e1ec28e`  |
| 1537   | No file  | `fcbe2e1ec28e`  |
| 1529   | No file  | `fcbe2e1ec28e`  |
| 1524   | No file  | `fcbe2e1ec28e`  |
| 1519   | No file  | `fcbe2e1ec28e`  |
| 1509   | No file  | `fcbe2e1ec28e`  |
| 1506   | No file  | `fcbe2e1ec28e`  |
| 1504   | No file  | `fcbe2e1ec28e`  |
| 1500   | No file  | `fcbe2e1ec28e`  |
| 1493   | No file  | `fcbe2e1ec28e`  |
| 1489   | No file  | `fcbe2e1ec28e`  |
| 1485   | No file  | `fcbe2e1ec28e`  |
| 1481   | No file  | `fcbe2e1ec28e`  |
| 1474   | No file  | `fcbe2e1ec28e`  |
| 1466   | No file  | `fcbe2e1ec28e`  |
| 1462   | No file  | `fcbe2e1ec28e`  |
| 1459   | No file  | `fcbe2e1ec28e`  |
| 1453   | No file  | `fcbe2e1ec28e`  |
| 1450   | No file  | `fcbe2e1ec28e`  |
| 1445   | No file  | `fcbe2e1ec28e`  |
| 1439   | No file  | `fcbe2e1ec28e`  |
| 1433   | No file  | `fcbe2e1ec28e`  |
| 1430   | No file  | `fcbe2e1ec28e`  |
| 1426   | No file  | `fcbe2e1ec28e`  |
| 1421   | No file  | `fcbe2e1ec28e`  |
| 1417   | No file  | `fcbe2e1ec28e`  |
| 1416   | No file  | `fcbe2e1ec28e`  |
| 1409   | No file  | `fcbe2e1ec28e`  |
| 1405   | No file  | `fcbe2e1ec28e`  |
| 1401   | No file  | `fcbe2e1ec28e`  |
| 1396   | No file  | `fcbe2e1ec28e`  |
| 1391   | No file  | `fcbe2e1ec28e`  |
| 1390   | No file  | `fcbe2e1ec28e`  |
| 1386   | No file  | `fcbe2e1ec28e`  |
| 1381   | No file  | `fcbe2e1ec28e`  |
| 1379   | No file  | `fcbe2e1ec28e`  |
| 1372   | No file  | `fcbe2e1ec28e`  |
| 1366   | No file  | `fcbe2e1ec28e`  |
| 1364   | No file  | `fcbe2e1ec28e`  |
| 1363   | No file  | `fcbe2e1ec28e`  |
| 1360   | No file  | `fcbe2e1ec28e`  |
| 1358   | No file  | `fcbe2e1ec28e`  |
| 1355   | No file  | `fcbe2e1ec28e`  |
| 1351   | No file  | `fcbe2e1ec28e`  |
| 1348   | No file  | `fcbe2e1ec28e`  |
| 1346   | No file  | `fcbe2e1ec28e`  |
| 1341   | No file  | `fcbe2e1ec28e`  |
| 1340   | No file  | `fcbe2e1ec28e`  |
| 1338   | No file  | `fcbe2e1ec28e`  |
| 1335   | No file  | `fcbe2e1ec28e`  |
| 1333   | No file  | `fcbe2e1ec28e`  |
| 1329   | No file  | `fcbe2e1ec28e`  |
| 1327   | No file  | `fcbe2e1ec28e`  |
| 1324   | No file  | `fcbe2e1ec28e`  |
| 1321   | No file  | `fcbe2e1ec28e`  |
| 1319   | No file  | `fcbe2e1ec28e`  |
| 1318   | No file  | `fcbe2e1ec28e`  |
| 1316   | No file  | `fcbe2e1ec28e`  |
| 1313   | No file  | `fcbe2e1ec28e`  |
| 1311   | No file  | `fcbe2e1ec28e`  |
| 1309   | No file  | `fcbe2e1ec28e`  |
| 1304   | No file  | `fcbe2e1ec28e`  |
| 1292   | No file  | `fcbe2e1ec28e`  |
| 1286   | No file  | `fcbe2e1ec28e`  |
| 1280   | No file  | `fcbe2e1ec28e`  |
| 1276   | No file  | `fcbe2e1ec28e`  |
| 1267   | No file  | `fcbe2e1ec28e`  |
| 1261   | No file  | `fcbe2e1ec28e`  |
| 1256   | No file  | `fcbe2e1ec28e`  |
| 1250   | No file  | `fcbe2e1ec28e`  |
| 1246   | No file  | `fcbe2e1ec28e`  |
| 1239   | No file  | `fcbe2e1ec28e`  |
| 1230   | No file  | `fcbe2e1ec28e`  |
| 1226   | No file  | `fcbe2e1ec28e`  |
| 1220   | No file  | `fcbe2e1ec28e`  |
| 1217   | No file  | `fcbe2e1ec28e`  |
| 1211   | No file  | `fcbe2e1ec28e`  |
| 1210   | No file  | `fcbe2e1ec28e`  |
| 1208   | No file  | `fcbe2e1ec28e`  |
| 1203   | No file  | `fcbe2e1ec28e`  |
| 1197   | No file  | `fcbe2e1ec28e`  |
| 1194   | No file  | `fcbe2e1ec28e`  |
| 1192   | No file  | `fcbe2e1ec28e`  |
| 1187   | No file  | `fcbe2e1ec28e`  |
| 1183   | No file  | `fcbe2e1ec28e`  |
| 1177   | No file  | `fcbe2e1ec28e`  |
| 1173   | No file  | `fcbe2e1ec28e`  |
| 1167   | No file  | `fcbe2e1ec28e`  |
| 1164   | No file  | `fcbe2e1ec28e`  |
| 1156   | No file  | `fcbe2e1ec28e`  |
| 1149   | No file  | `fcbe2e1ec28e`  |
| 1144   | No file  | `fcbe2e1ec28e`  |
| 1137   | No file  | `fcbe2e1ec28e`  |
| 1132   | No file  | `fcbe2e1ec28e`  |
| 1127   | No file  | `fcbe2e1ec28e`  |
| 1122   | No file  | `fcbe2e1ec28e`  |
| 1118   | No file  | `fcbe2e1ec28e`  |
| 1114   | No file  | `fcbe2e1ec28e`  |
| 1109   | No file  | `fcbe2e1ec28e`  |
| 1102   | No file  | `fcbe2e1ec28e`  |
| 1096   | No file  | `fcbe2e1ec28e`  |
| 1088   | No file  | `fcbe2e1ec28e`  |
| 1081   | No file  | `fcbe2e1ec28e`  |
| 1076   | No file  | `fcbe2e1ec28e`  |
| 1069   | No file  | `fcbe2e1ec28e`  |
| 1064   | No file  | `fcbe2e1ec28e`  |
| 1058   | No file  | `fcbe2e1ec28e`  |
| 1051   | No file  | `fcbe2e1ec28e`  |
| 1044   | No file  | `fcbe2e1ec28e`  |
| 1036   | No file  | `fcbe2e1ec28e`  |
| 1026   | No file  | `fcbe2e1ec28e`  |
| 1016   | No file  | `fcbe2e1ec28e`  |
| 1009   | No file  | `fcbe2e1ec28e`  |
| 1005   | No file  | `fcbe2e1ec28e`  |
| 1000   | No file  | `fcbe2e1ec28e`  |
| 998    | No file  | `fcbe2e1ec28e`  |
| 990    | No file  | `fcbe2e1ec28e`  |
| 979    | No file  | `fcbe2e1ec28e`  |
| 972    | No file  | `fcbe2e1ec28e`  |
| 963    | No file  | `fcbe2e1ec28e`  |
| 955    | No file  | `fcbe2e1ec28e`  |
| 946    | No file  | `fcbe2e1ec28e`  |
| 938    | No file  | `fcbe2e1ec28e`  |
| 927    | No file  | `fcbe2e1ec28e`  |
| 911    | No file  | `fcbe2e1ec28e`  |
| 904    | No file  | `fcbe2e1ec28e`  |
| 899    | No file  | `fcbe2e1ec28e`  |
| 894    | No file  | `fcbe2e1ec28e`  |
| 885    | No file  | `fcbe2e1ec28e`  |
| 879    | No file  | `fcbe2e1ec28e`  |
| 872    | No file  | `fcbe2e1ec28e`  |
| 864    | No file  | `fcbe2e1ec28e`  |
| 855    | No file  | `fcbe2e1ec28e`  |
| 853    | No file  | `fcbe2e1ec28e`  |
| 845    | No file  | `fcbe2e1ec28e`  |
| 837    | No file  | `fcbe2e1ec28e`  |
| 829    | No file  | `fcbe2e1ec28e`  |
| 822    | No file  | `fcbe2e1ec28e`  |
| 814    | No file  | `fcbe2e1ec28e`  |
| 805    | No file  | `fcbe2e1ec28e`  |
| 794    | No file  | `fcbe2e1ec28e`  |
| 787    | No file  | `fcbe2e1ec28e`  |
| 780    | No file  | `fcbe2e1ec28e`  |
| 771    | No file  | `fcbe2e1ec28e`  |
| 760    | No file  | `fcbe2e1ec28e`  |
| 748    | No file  | `fcbe2e1ec28e`  |
| 741    | No file  | `fcbe2e1ec28e`  |
| 736    | No file  | `fcbe2e1ec28e`  |
| 731    | No file  | `fcbe2e1ec28e`  |
| 723    | No file  | `fcbe2e1ec28e`  |
| 711    | No file  | `fcbe2e1ec28e`  |
| 707    | No file  | `fcbe2e1ec28e`  |
| 697    | No file  | `fcbe2e1ec28e`  |
| 689    | No file  | `fcbe2e1ec28e`  |
| 683    | No file  | `fcbe2e1ec28e`  |
| 678    | No file  | `fcbe2e1ec28e`  |
| 670    | No file  | `fcbe2e1ec28e`  |
| 661    | No file  | `fcbe2e1ec28e`  |
| 656    | No file  | `fcbe2e1ec28e`  |
| 652    | No file  | `fcbe2e1ec28e`  |
| 643    | No file  | `fcbe2e1ec28e`  |
| 637    | No file  | `fcbe2e1ec28e`  |
| 630    | No file  | `fcbe2e1ec28e`  |
| 627    | No file  | `fcbe2e1ec28e`  |
| 621    | No file  | `fcbe2e1ec28e`  |
| 617    | No file  | `fcbe2e1ec28e`  |
| 615    | No file  | `fcbe2e1ec28e`  |
| 606    | No file  | `fcbe2e1ec28e`  |
| 599    | No file  | `fcbe2e1ec28e`  |
| 592    | No file  | `fcbe2e1ec28e`  |
| 586    | No file  | `fcbe2e1ec28e`  |
| 577    | No file  | `fcbe2e1ec28e`  |
| 569    | No file  | `fcbe2e1ec28e`  |
| 561    | No file  | `fcbe2e1ec28e`  |
| 554    | No file  | `fcbe2e1ec28e`  |
| 542    | No file  | `fcbe2e1ec28e`  |
| 532    | No file  | `fcbe2e1ec28e`  |
| 531    | No file  | `fcbe2e1ec28e`  |
| 526    | No file  | `fcbe2e1ec28e`  |
| 521    | No file  | `fcbe2e1ec28e`  |
| 517    | No file  | `fcbe2e1ec28e`  |
| 510    | No file  | `fcbe2e1ec28e`  |
| 508    | No file  | `fcbe2e1ec28e`  |
| 504    | No file  | `fcbe2e1ec28e`  |
| 497    | No file  | `fcbe2e1ec28e`  |
| 491    | No file  | `fcbe2e1ec28e`  |
| 485    | No file  | `fcbe2e1ec28e`  |
| 478    | No file  | `fcbe2e1ec28e`  |
| 472    | No file  | `fcbe2e1ec28e`  |
| 466    | No file  | `fcbe2e1ec28e`  |
| 457    | No file  | `fcbe2e1ec28e`  |
| 452    | No file  | `fcbe2e1ec28e`  |
| 449    | No file  | `fcbe2e1ec28e`  |
| 435    | No file  | `fcbe2e1ec28e`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | Ship names (LOC type 6) |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a ship without a row shows as plain text instead of a link |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The PABR layout of [`bdoservanttitless.bss`](bdoservanttitless_bss.md)
with a second table between the rows and the empty string table; no count
gives its length, it runs up to `table_start`.

| Offset         | Type                  | Field        | Notes |
| -------------- | --------------------- | ------------ | ----- |
| `+0x00`        | char[4]               | magic        | `PABR` |
| `+0x04`        | u32                   | record_count | Number of ships |
| `+0x08`        | Row[record_count]     | records      | See Row |
| `records+0x00` | Entry[..table_start]  | entries      | See Entry |
| `EOF-0x0C`     | u32                   | string_count | Always `0`; the empty PABR string table |
| `EOF-0x08`     | u32                   | table_start  | Offset of `string_count`, where the entries end |
| `EOF-0x04`     | u32                   | zero         | Always `0` |

### Row (18 bytes)

| Offset  | Type   | Field           | Notes |
| ------- | ------ | --------------- | ----- |
| `+0x00` | u16    | character_key   | Ship character key (`31001` Epheria Sailboat, `31045` Epheria Carrack); unique |
| `+0x02` | u16[8] | job_slot_counts | Slots per preset job; see [Job Slots](#job-slots-client-3482) |

### Entry (3 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u16  | unknown_00 | `0` to `40`, one entry each, in this order |
| `+0x02` | u8   | unknown_02 | `1` to `8`, never falling from one entry to the next |

## Job Slots (Client 3482)

| Ships | `job_slot_counts` |
| ----- | ----------------- |
| Epheria Sailboat `31001`, Epheria Frigate `31003`, Bartali Sailboat `31053`, Improved Epheria Sailboat `31058`, Improved Epheria Frigate `31059` | `0, 0, 0, 0, 0, 0, 2, 0` |
| Epheria Caravel `31048`, Epheria Galleass `31049` | `0, 0, 0, 0, 0, 0, 6, 0` |
| Epheria Carrack `31045`, Epheria Carrack: Valor `31085` | `1, 1, 1, 1, 2, 1, 20, 0` |
| Panokseon `31025` | `1, 1, 1, 1, 3, 1, 30, 0` |
| Epheria Carrack: Advance `31054` | `1, 1, 1, 1, 1, 2, 20, 1` |
| Epheria Carrack: Balance `31055`, Epheria Carrack: Volante `31056` | `1, 2, 1, 1, 1, 1, 20, 1` |
| Epheria Carrack: Valor `31057`, GM: Epheria Carrack `31084` | `1, 1, 1, 1, 2, 1, 20, 1` |

The entries rise as `0:1, 1:2, 2:2, 3:3, 4:4, 5:5, 6:5, 7:5, 8:6, 9:6,
10:7, 11:8` and stay at `8` from key `11` to `40`.

## Field Names

`ToClient_getEmployeePresetJobCount(shipCharacterKey, job)` in
`panel_window_sailorpresetmanager_all_1.luac` (client 3482) gives the
number of slots of one preset job on a ship, for `job` from `1` to
`__eEmployeePresetJob_Count - 1`, and hides a job whose count is `0`.
The row is a ship character key and eight counts, the eight preset jobs
of that window (`ViceCaptain`, `Sail`, `Deck`, `Helmsman`, `CannonSlot`,
`Cook`, `Fishing`, `Cabin`), so the array is named `job_slot_counts`. The
file is not in client 1784 and has no sheet in a private server's
`DataSheets.bexcel` on client 1784.

## Notes

- The file is in client 2834 and later; clients 3002 to 3482 hold the
  same bytes.
- The largest count (`2` to `30`) is the seventh. The Sailor Preset window
  pages its Cabin slots (`_currentCabinPageCount`), which fits a job with
  many slots.

## Open Questions

### Order of the Preset Jobs

The Lua names the jobs but not their numbers, which the client sets.
The tooltip texts of the window are numbered `LUA_SAILOR_PRESET_SLOT_01`
(`ViceCaptain`), `_02` (`Sail`), `_03` (`Helmsman`), `_04` (`CannonSlot`),
`_05` (`Deck`), `_06` (`Cook`), `_07` (`Cabin`) and `_08` (`Fishing`).
Read in that order, the seventh count is `Cabin` (`2` to `30`), the
eighth `Fishing` (`1` on Epheria Carrack: Advance, Balance, Volante,
Valor `31057` and the GM carrack only), and Epheria Carrack: Balance and
Volante get two `Sail` slots. Whether the array follows that numbering is
not confirmed.

### What the Entries Are

41 entries with keys `0` to `40` and values `1` to `8`. Sailors reach
level 10 (`employeeexp.bss`), so the key is not a sailor level; the top
value `8` equals the number of preset jobs. What the key counts is open.
