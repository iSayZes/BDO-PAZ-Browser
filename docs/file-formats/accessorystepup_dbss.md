# `accessorystepup.dbss` Format

## Purpose

The accessory step-up: an accessory that grows from base to PEN in five
steps, each step paid with four materials and the accessory at its current
level. One row per accessory choice, with its group and the materials of
all five steps. The step-up window
(`panel_window_accessory_stepup_all_*.luac`) reads it through
`ToClient_getAccessoryStepUpItemKey(accessoryIndex)`,
`ToClient_getAccessoryStepUpMaterialItemEnchantKey(accessoryIndex,
enchantLevel, materialIndex)` and
`ToClient_getAccessoryStepUpMaterialNeedCount` with the same arguments.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records                      | Row bytes |
| ------ | -------------- | ---------------------- | ----- | ---------------------------- | --------- |
| 1      | 2434 and later | `accessorystepup.dbss` | 1,840 | 150 Material, 30 Step, 6 Row | 12        |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `accessorystepup.dbss` | 1,840 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `ba45f2203e2d`  |
| 3482   | Layout 1 | `ba45f2203e2d`  |
| 3474   | Layout 1 | `ba45f2203e2d`  |
| 3473   | Layout 1 | `ba45f2203e2d`  |
| 3464   | Layout 1 | `ba45f2203e2d`  |
| 3458   | Layout 1 | `ba45f2203e2d`  |
| 3454   | Layout 1 | `ba45f2203e2d`  |
| 3444   | Layout 1 | `ba45f2203e2d`  |
| 3435   | Layout 1 | `ba45f2203e2d`  |
| 3426   | Layout 1 | `ba45f2203e2d`  |
| 3418   | Layout 1 | `ba45f2203e2d`  |
| 3412   | Layout 1 | `ba45f2203e2d`  |
| 3402   | Layout 1 | `ba45f2203e2d`  |
| 3396   | Layout 1 | `ba45f2203e2d`  |
| 3387   | Layout 1 | `ba45f2203e2d`  |
| 3381   | Layout 1 | `ba45f2203e2d`  |
| 3373   | Layout 1 | `ba45f2203e2d`  |
| 3364   | Layout 1 | `ba45f2203e2d`  |
| 3356   | Layout 1 | `ba45f2203e2d`  |
| 3349   | Layout 1 | `ba45f2203e2d`  |
| 3342   | Layout 1 | `ba45f2203e2d`  |
| 3335   | Layout 1 | `ba45f2203e2d`  |
| 3326   | Layout 1 | `ba45f2203e2d`  |
| 3321   | Layout 1 | `ba45f2203e2d`  |
| 3314   | Layout 1 | `ba45f2203e2d`  |
| 3303   | Layout 1 | `ba45f2203e2d`  |
| 3302   | Layout 1 | `ba45f2203e2d`  |
| 3293   | Layout 1 | `ba45f2203e2d`  |
| 3283   | Layout 1 | `ba45f2203e2d`  |
| 3275   | Layout 1 | `ba45f2203e2d`  |
| 3267   | Layout 1 | `ba45f2203e2d`  |
| 3258   | Layout 1 | `ba45f2203e2d`  |
| 3251   | Layout 1 | `ba45f2203e2d`  |
| 3242   | Layout 1 | `ba45f2203e2d`  |
| 3235   | Layout 1 | `ba45f2203e2d`  |
| 3229   | Layout 1 | `ba45f2203e2d`  |
| 3212   | Layout 1 | `ba45f2203e2d`  |
| 3203   | Layout 1 | `ba45f2203e2d`  |
| 3193   | Layout 1 | `ba45f2203e2d`  |
| 3186   | Layout 1 | `ba45f2203e2d`  |
| 3177   | Layout 1 | `ba45f2203e2d`  |
| 3169   | Layout 1 | `ba45f2203e2d`  |
| 3158   | Layout 1 | `ba45f2203e2d`  |
| 3151   | Layout 1 | `ba45f2203e2d`  |
| 3144   | Layout 1 | `ba45f2203e2d`  |
| 3133   | Layout 1 | `ba45f2203e2d`  |
| 3125   | Layout 1 | `ba45f2203e2d`  |
| 3118   | Layout 1 | `ba45f2203e2d`  |
| 3111   | Layout 1 | `ba45f2203e2d`  |
| 3103   | Layout 1 | `ba45f2203e2d`  |
| 3095   | Layout 1 | `ba45f2203e2d`  |
| 3086   | Layout 1 | `ba45f2203e2d`  |
| 3072   | Layout 1 | `ba45f2203e2d`  |
| 3062   | Layout 1 | `ba45f2203e2d`  |
| 3052   | Layout 1 | `ba45f2203e2d`  |
| 3045   | Layout 1 | `ba45f2203e2d`  |
| 3037   | Layout 1 | `ba45f2203e2d`  |
| 3030   | Layout 1 | `ba45f2203e2d`  |
| 3021   | Layout 1 | `ba45f2203e2d`  |
| 3012   | Layout 1 | `ba45f2203e2d`  |
| 3002   | Layout 1 | `ba45f2203e2d`  |
| 2995   | Layout 1 | `ba45f2203e2d`  |
| 2987   | Layout 1 | `ba45f2203e2d`  |
| 2978   | Layout 1 | `ba45f2203e2d`  |
| 2970   | Layout 1 | `ba45f2203e2d`  |
| 2959   | Layout 1 | `ba45f2203e2d`  |
| 2951   | Layout 1 | `ba45f2203e2d`  |
| 2942   | Layout 1 | `ba45f2203e2d`  |
| 2935   | Layout 1 | `ba45f2203e2d`  |
| 2932   | Layout 1 | `ba45f2203e2d`  |
| 2923   | Layout 1 | `ba45f2203e2d`  |
| 2919   | Layout 1 | `ba45f2203e2d`  |
| 2907   | Layout 1 | `ba45f2203e2d`  |
| 2900   | Layout 1 | `ba45f2203e2d`  |
| 2891   | Layout 1 | `ba45f2203e2d`  |
| 2882   | Layout 1 | `ba45f2203e2d`  |
| 2872   | Layout 1 | `ba45f2203e2d`  |
| 2863   | Layout 1 | `ba45f2203e2d`  |
| 2855   | Layout 1 | `ba45f2203e2d`  |
| 2849   | Layout 1 | `ba45f2203e2d`  |
| 2844   | Layout 1 | `ba45f2203e2d`  |
| 2834   | Layout 1 | `ba45f2203e2d`  |
| 2825   | Layout 1 | `ba45f2203e2d`  |
| 2819   | Layout 1 | `ba45f2203e2d`  |
| 2811   | Layout 1 | `ba45f2203e2d`  |
| 2803   | Layout 1 | `ba45f2203e2d`  |
| 2794   | Layout 1 | `ba45f2203e2d`  |
| 2783   | Layout 1 | `ba45f2203e2d`  |
| 2774   | Layout 1 | `ba45f2203e2d`  |
| 2765   | Layout 1 | `ba45f2203e2d`  |
| 2756   | Layout 1 | `ba45f2203e2d`  |
| 2750   | Layout 1 | `ba45f2203e2d`  |
| 2743   | Layout 1 | `ba45f2203e2d`  |
| 2736   | Layout 1 | `ba45f2203e2d`  |
| 2726   | Layout 1 | `ba45f2203e2d`  |
| 2717   | Layout 1 | `ba45f2203e2d`  |
| 2709   | Layout 1 | `ba45f2203e2d`  |
| 2703   | Layout 1 | `ba45f2203e2d`  |
| 2695   | Layout 1 | `ba45f2203e2d`  |
| 2684   | Layout 1 | `ba45f2203e2d`  |
| 2672   | Layout 1 | `ba45f2203e2d`  |
| 2665   | Layout 1 | `ba45f2203e2d`  |
| 2657   | Layout 1 | `ba45f2203e2d`  |
| 2649   | Layout 1 | `ba45f2203e2d`  |
| 2644   | Layout 1 | `ba45f2203e2d`  |
| 2637   | Layout 1 | `ba45f2203e2d`  |
| 2629   | Layout 1 | `ba45f2203e2d`  |
| 2619   | Layout 1 | `ba45f2203e2d`  |
| 2612   | Layout 1 | `ba45f2203e2d`  |
| 2606   | Layout 1 | `ba45f2203e2d`  |
| 2602   | Layout 1 | `ba45f2203e2d`  |
| 2601   | Layout 1 | `ba45f2203e2d`  |
| 2592   | Layout 1 | `ba45f2203e2d`  |
| 2583   | Layout 1 | `ba45f2203e2d`  |
| 2575   | Layout 1 | `ba45f2203e2d`  |
| 2567   | Layout 1 | `ba45f2203e2d`  |
| 2560   | Layout 1 | `ba45f2203e2d`  |
| 2553   | Layout 1 | `ba45f2203e2d`  |
| 2545   | Layout 1 | `ba45f2203e2d`  |
| 2538   | Layout 1 | `ba45f2203e2d`  |
| 2529   | Layout 1 | `ba45f2203e2d`  |
| 2519   | Layout 1 | `ba45f2203e2d`  |
| 2513   | Layout 1 | `ba45f2203e2d`  |
| 2510   | Layout 1 | `ba45f2203e2d`  |
| 2507   | Layout 1 | `ba45f2203e2d`  |
| 2503   | Layout 1 | `ba45f2203e2d`  |
| 2498   | Layout 1 | `ba45f2203e2d`  |
| 2492   | Layout 1 | `ba45f2203e2d`  |
| 2487   | Layout 1 | `ba45f2203e2d`  |
| 2480   | Layout 1 | `ba45f2203e2d`  |
| 2474   | Layout 1 | `ba45f2203e2d`  |
| 2468   | Layout 1 | `ba45f2203e2d`  |
| 2460   | Layout 1 | `ba45f2203e2d`  |
| 2453   | Layout 1 | `ba45f2203e2d`  |
| 2444   | Layout 1 | `ba45f2203e2d`  |
| 2438   | Layout 1 | `ba45f2203e2d`  |
| 2434   | Layout 1 | `ba45f2203e2d`  |
| 2429   | No file  | `ba45f2203e2d`  |
| 2421   | No file  | `ba45f2203e2d`  |
| 2414   | No file  | `ba45f2203e2d`  |
| 2407   | No file  | `ba45f2203e2d`  |
| 2401   | No file  | `ba45f2203e2d`  |
| 2397   | No file  | `ba45f2203e2d`  |
| 2393   | No file  | `ba45f2203e2d`  |
| 2384   | No file  | `ba45f2203e2d`  |
| 2378   | No file  | `ba45f2203e2d`  |
| 2372   | No file  | `ba45f2203e2d`  |
| 2358   | No file  | `ba45f2203e2d`  |
| 2352   | No file  | `ba45f2203e2d`  |
| 2347   | No file  | `ba45f2203e2d`  |
| 2343   | No file  | `ba45f2203e2d`  |
| 2335   | No file  | `ba45f2203e2d`  |
| 2327   | No file  | `ba45f2203e2d`  |
| 2324   | No file  | `ba45f2203e2d`  |
| 2319   | No file  | `ba45f2203e2d`  |
| 2313   | No file  | `ba45f2203e2d`  |
| 2308   | No file  | `ba45f2203e2d`  |
| 2302   | No file  | `ba45f2203e2d`  |
| 2295   | No file  | `ba45f2203e2d`  |
| 2290   | No file  | `ba45f2203e2d`  |
| 2284   | No file  | `ba45f2203e2d`  |
| 2276   | No file  | `ba45f2203e2d`  |
| 2269   | No file  | `ba45f2203e2d`  |
| 2259   | No file  | `ba45f2203e2d`  |
| 2250   | No file  | `ba45f2203e2d`  |
| 2243   | No file  | `ba45f2203e2d`  |
| 2235   | No file  | `ba45f2203e2d`  |
| 2229   | No file  | `ba45f2203e2d`  |
| 2224   | No file  | `ba45f2203e2d`  |
| 2218   | No file  | `ba45f2203e2d`  |
| 2215   | No file  | `ba45f2203e2d`  |
| 2207   | No file  | `ba45f2203e2d`  |
| 2203   | No file  | `ba45f2203e2d`  |
| 2196   | No file  | `ba45f2203e2d`  |
| 2192   | No file  | `ba45f2203e2d`  |
| 2189   | No file  | `ba45f2203e2d`  |
| 2183   | No file  | `ba45f2203e2d`  |
| 2179   | No file  | `ba45f2203e2d`  |
| 2171   | No file  | `ba45f2203e2d`  |
| 2163   | No file  | `ba45f2203e2d`  |
| 2156   | No file  | `ba45f2203e2d`  |
| 2151   | No file  | `ba45f2203e2d`  |
| 2147   | No file  | `ba45f2203e2d`  |
| 2142   | No file  | `ba45f2203e2d`  |
| 2138   | No file  | `ba45f2203e2d`  |
| 2134   | No file  | `ba45f2203e2d`  |
| 2130   | No file  | `ba45f2203e2d`  |
| 2122   | No file  | `ba45f2203e2d`  |
| 2107   | No file  | `ba45f2203e2d`  |
| 2098   | No file  | `ba45f2203e2d`  |
| 2089   | No file  | `ba45f2203e2d`  |
| 2081   | No file  | `ba45f2203e2d`  |
| 2073   | No file  | `ba45f2203e2d`  |
| 2067   | No file  | `ba45f2203e2d`  |
| 2063   | No file  | `ba45f2203e2d`  |
| 2059   | No file  | `ba45f2203e2d`  |
| 2052   | No file  | `ba45f2203e2d`  |
| 2044   | No file  | `ba45f2203e2d`  |
| 2039   | No file  | `ba45f2203e2d`  |
| 2032   | No file  | `ba45f2203e2d`  |
| 2025   | No file  | `ba45f2203e2d`  |
| 2011   | No file  | `ba45f2203e2d`  |
| 2005   | No file  | `ba45f2203e2d`  |
| 2000   | No file  | `ba45f2203e2d`  |
| 1996   | No file  | `ba45f2203e2d`  |
| 1991   | No file  | `ba45f2203e2d`  |
| 1985   | No file  | `ba45f2203e2d`  |
| 1980   | No file  | `ba45f2203e2d`  |
| 1969   | No file  | `ba45f2203e2d`  |
| 1964   | No file  | `ba45f2203e2d`  |
| 1958   | No file  | `ba45f2203e2d`  |
| 1950   | No file  | `ba45f2203e2d`  |
| 1945   | No file  | `ba45f2203e2d`  |
| 1937   | No file  | `ba45f2203e2d`  |
| 1933   | No file  | `ba45f2203e2d`  |
| 1927   | No file  | `ba45f2203e2d`  |
| 1921   | No file  | `ba45f2203e2d`  |
| 1914   | No file  | `ba45f2203e2d`  |
| 1908   | No file  | `ba45f2203e2d`  |
| 1897   | No file  | `ba45f2203e2d`  |
| 1892   | No file  | `ba45f2203e2d`  |
| 1886   | No file  | `ba45f2203e2d`  |
| 1881   | No file  | `ba45f2203e2d`  |
| 1871   | No file  | `ba45f2203e2d`  |
| 1866   | No file  | `ba45f2203e2d`  |
| 1862   | No file  | `ba45f2203e2d`  |
| 1854   | No file  | `ba45f2203e2d`  |
| 1846   | No file  | `ba45f2203e2d`  |
| 1838   | No file  | `ba45f2203e2d`  |
| 1832   | No file  | `ba45f2203e2d`  |
| 1826   | No file  | `ba45f2203e2d`  |
| 1822   | No file  | `ba45f2203e2d`  |
| 1818   | No file  | `ba45f2203e2d`  |
| 1804   | No file  | `ba45f2203e2d`  |
| 1794   | No file  | `ba45f2203e2d`  |
| 1790   | No file  | `ba45f2203e2d`  |
| 1784   | No file  | `ba45f2203e2d`  |
| 1774   | No file  | `ba45f2203e2d`  |
| 1771   | No file  | `ba45f2203e2d`  |
| 1762   | No file  | `ba45f2203e2d`  |
| 1759   | No file  | `ba45f2203e2d`  |
| 1754   | No file  | `ba45f2203e2d`  |
| 1749   | No file  | `ba45f2203e2d`  |
| 1743   | No file  | `ba45f2203e2d`  |
| 1737   | No file  | `ba45f2203e2d`  |
| 1731   | No file  | `ba45f2203e2d`  |
| 1725   | No file  | `ba45f2203e2d`  |
| 1717   | No file  | `ba45f2203e2d`  |
| 1710   | No file  | `ba45f2203e2d`  |
| 1704   | No file  | `ba45f2203e2d`  |
| 1698   | No file  | `ba45f2203e2d`  |
| 1690   | No file  | `ba45f2203e2d`  |
| 1685   | No file  | `ba45f2203e2d`  |
| 1680   | No file  | `ba45f2203e2d`  |
| 1674   | No file  | `ba45f2203e2d`  |
| 1668   | No file  | `ba45f2203e2d`  |
| 1659   | No file  | `ba45f2203e2d`  |
| 1649   | No file  | `ba45f2203e2d`  |
| 1642   | No file  | `ba45f2203e2d`  |
| 1636   | No file  | `ba45f2203e2d`  |
| 1628   | No file  | `ba45f2203e2d`  |
| 1622   | No file  | `ba45f2203e2d`  |
| 1614   | No file  | `ba45f2203e2d`  |
| 1608   | No file  | `ba45f2203e2d`  |
| 1602   | No file  | `ba45f2203e2d`  |
| 1598   | No file  | `ba45f2203e2d`  |
| 1594   | No file  | `ba45f2203e2d`  |
| 1590   | No file  | `ba45f2203e2d`  |
| 1587   | No file  | `ba45f2203e2d`  |
| 1584   | No file  | `ba45f2203e2d`  |
| 1579   | No file  | `ba45f2203e2d`  |
| 1572   | No file  | `ba45f2203e2d`  |
| 1565   | No file  | `ba45f2203e2d`  |
| 1559   | No file  | `ba45f2203e2d`  |
| 1554   | No file  | `ba45f2203e2d`  |
| 1547   | No file  | `ba45f2203e2d`  |
| 1537   | No file  | `ba45f2203e2d`  |
| 1529   | No file  | `ba45f2203e2d`  |
| 1524   | No file  | `ba45f2203e2d`  |
| 1519   | No file  | `ba45f2203e2d`  |
| 1509   | No file  | `ba45f2203e2d`  |
| 1506   | No file  | `ba45f2203e2d`  |
| 1504   | No file  | `ba45f2203e2d`  |
| 1500   | No file  | `ba45f2203e2d`  |
| 1493   | No file  | `ba45f2203e2d`  |
| 1489   | No file  | `ba45f2203e2d`  |
| 1485   | No file  | `ba45f2203e2d`  |
| 1481   | No file  | `ba45f2203e2d`  |
| 1474   | No file  | `ba45f2203e2d`  |
| 1466   | No file  | `ba45f2203e2d`  |
| 1462   | No file  | `ba45f2203e2d`  |
| 1459   | No file  | `ba45f2203e2d`  |
| 1453   | No file  | `ba45f2203e2d`  |
| 1450   | No file  | `ba45f2203e2d`  |
| 1445   | No file  | `ba45f2203e2d`  |
| 1439   | No file  | `ba45f2203e2d`  |
| 1433   | No file  | `ba45f2203e2d`  |
| 1430   | No file  | `ba45f2203e2d`  |
| 1426   | No file  | `ba45f2203e2d`  |
| 1421   | No file  | `ba45f2203e2d`  |
| 1417   | No file  | `ba45f2203e2d`  |
| 1416   | No file  | `ba45f2203e2d`  |
| 1409   | No file  | `ba45f2203e2d`  |
| 1405   | No file  | `ba45f2203e2d`  |
| 1401   | No file  | `ba45f2203e2d`  |
| 1396   | No file  | `ba45f2203e2d`  |
| 1391   | No file  | `ba45f2203e2d`  |
| 1390   | No file  | `ba45f2203e2d`  |
| 1386   | No file  | `ba45f2203e2d`  |
| 1381   | No file  | `ba45f2203e2d`  |
| 1379   | No file  | `ba45f2203e2d`  |
| 1372   | No file  | `ba45f2203e2d`  |
| 1366   | No file  | `ba45f2203e2d`  |
| 1364   | No file  | `ba45f2203e2d`  |
| 1363   | No file  | `ba45f2203e2d`  |
| 1360   | No file  | `ba45f2203e2d`  |
| 1358   | No file  | `ba45f2203e2d`  |
| 1355   | No file  | `ba45f2203e2d`  |
| 1351   | No file  | `ba45f2203e2d`  |
| 1348   | No file  | `ba45f2203e2d`  |
| 1346   | No file  | `ba45f2203e2d`  |
| 1341   | No file  | `ba45f2203e2d`  |
| 1340   | No file  | `ba45f2203e2d`  |
| 1338   | No file  | `ba45f2203e2d`  |
| 1335   | No file  | `ba45f2203e2d`  |
| 1333   | No file  | `ba45f2203e2d`  |
| 1329   | No file  | `ba45f2203e2d`  |
| 1327   | No file  | `ba45f2203e2d`  |
| 1324   | No file  | `ba45f2203e2d`  |
| 1321   | No file  | `ba45f2203e2d`  |
| 1319   | No file  | `ba45f2203e2d`  |
| 1318   | No file  | `ba45f2203e2d`  |
| 1316   | No file  | `ba45f2203e2d`  |
| 1313   | No file  | `ba45f2203e2d`  |
| 1311   | No file  | `ba45f2203e2d`  |
| 1309   | No file  | `ba45f2203e2d`  |
| 1304   | No file  | `ba45f2203e2d`  |
| 1292   | No file  | `ba45f2203e2d`  |
| 1286   | No file  | `ba45f2203e2d`  |
| 1280   | No file  | `ba45f2203e2d`  |
| 1276   | No file  | `ba45f2203e2d`  |
| 1267   | No file  | `ba45f2203e2d`  |
| 1261   | No file  | `ba45f2203e2d`  |
| 1256   | No file  | `ba45f2203e2d`  |
| 1250   | No file  | `ba45f2203e2d`  |
| 1246   | No file  | `ba45f2203e2d`  |
| 1239   | No file  | `ba45f2203e2d`  |
| 1230   | No file  | `ba45f2203e2d`  |
| 1226   | No file  | `ba45f2203e2d`  |
| 1220   | No file  | `ba45f2203e2d`  |
| 1217   | No file  | `ba45f2203e2d`  |
| 1211   | No file  | `ba45f2203e2d`  |
| 1210   | No file  | `ba45f2203e2d`  |
| 1208   | No file  | `ba45f2203e2d`  |
| 1203   | No file  | `ba45f2203e2d`  |
| 1197   | No file  | `ba45f2203e2d`  |
| 1194   | No file  | `ba45f2203e2d`  |
| 1192   | No file  | `ba45f2203e2d`  |
| 1187   | No file  | `ba45f2203e2d`  |
| 1183   | No file  | `ba45f2203e2d`  |
| 1177   | No file  | `ba45f2203e2d`  |
| 1173   | No file  | `ba45f2203e2d`  |
| 1167   | No file  | `ba45f2203e2d`  |
| 1164   | No file  | `ba45f2203e2d`  |
| 1156   | No file  | `ba45f2203e2d`  |
| 1149   | No file  | `ba45f2203e2d`  |
| 1144   | No file  | `ba45f2203e2d`  |
| 1137   | No file  | `ba45f2203e2d`  |
| 1132   | No file  | `ba45f2203e2d`  |
| 1127   | No file  | `ba45f2203e2d`  |
| 1122   | No file  | `ba45f2203e2d`  |
| 1118   | No file  | `ba45f2203e2d`  |
| 1114   | No file  | `ba45f2203e2d`  |
| 1109   | No file  | `ba45f2203e2d`  |
| 1102   | No file  | `ba45f2203e2d`  |
| 1096   | No file  | `ba45f2203e2d`  |
| 1088   | No file  | `ba45f2203e2d`  |
| 1081   | No file  | `ba45f2203e2d`  |
| 1076   | No file  | `ba45f2203e2d`  |
| 1069   | No file  | `ba45f2203e2d`  |
| 1064   | No file  | `ba45f2203e2d`  |
| 1058   | No file  | `ba45f2203e2d`  |
| 1051   | No file  | `ba45f2203e2d`  |
| 1044   | No file  | `ba45f2203e2d`  |
| 1036   | No file  | `ba45f2203e2d`  |
| 1026   | No file  | `ba45f2203e2d`  |
| 1016   | No file  | `ba45f2203e2d`  |
| 1009   | No file  | `ba45f2203e2d`  |
| 1005   | No file  | `ba45f2203e2d`  |
| 1000   | No file  | `ba45f2203e2d`  |
| 998    | No file  | `ba45f2203e2d`  |
| 990    | No file  | `ba45f2203e2d`  |
| 979    | No file  | `ba45f2203e2d`  |
| 972    | No file  | `ba45f2203e2d`  |
| 963    | No file  | `ba45f2203e2d`  |
| 955    | No file  | `ba45f2203e2d`  |
| 946    | No file  | `ba45f2203e2d`  |
| 938    | No file  | `ba45f2203e2d`  |
| 927    | No file  | `ba45f2203e2d`  |
| 911    | No file  | `ba45f2203e2d`  |
| 904    | No file  | `ba45f2203e2d`  |
| 899    | No file  | `ba45f2203e2d`  |
| 894    | No file  | `ba45f2203e2d`  |
| 885    | No file  | `ba45f2203e2d`  |
| 879    | No file  | `ba45f2203e2d`  |
| 872    | No file  | `ba45f2203e2d`  |
| 864    | No file  | `ba45f2203e2d`  |
| 855    | No file  | `ba45f2203e2d`  |
| 853    | No file  | `ba45f2203e2d`  |
| 845    | No file  | `ba45f2203e2d`  |
| 837    | No file  | `ba45f2203e2d`  |
| 829    | No file  | `ba45f2203e2d`  |
| 822    | No file  | `ba45f2203e2d`  |
| 814    | No file  | `ba45f2203e2d`  |
| 805    | No file  | `ba45f2203e2d`  |
| 794    | No file  | `ba45f2203e2d`  |
| 787    | No file  | `ba45f2203e2d`  |
| 780    | No file  | `ba45f2203e2d`  |
| 771    | No file  | `ba45f2203e2d`  |
| 760    | No file  | `ba45f2203e2d`  |
| 748    | No file  | `ba45f2203e2d`  |
| 741    | No file  | `ba45f2203e2d`  |
| 736    | No file  | `ba45f2203e2d`  |
| 731    | No file  | `ba45f2203e2d`  |
| 723    | No file  | `ba45f2203e2d`  |
| 711    | No file  | `ba45f2203e2d`  |
| 707    | No file  | `ba45f2203e2d`  |
| 697    | No file  | `ba45f2203e2d`  |
| 689    | No file  | `ba45f2203e2d`  |
| 683    | No file  | `ba45f2203e2d`  |
| 678    | No file  | `ba45f2203e2d`  |
| 670    | No file  | `ba45f2203e2d`  |
| 661    | No file  | `ba45f2203e2d`  |
| 656    | No file  | `ba45f2203e2d`  |
| 652    | No file  | `ba45f2203e2d`  |
| 643    | No file  | `ba45f2203e2d`  |
| 637    | No file  | `ba45f2203e2d`  |
| 630    | No file  | `ba45f2203e2d`  |
| 627    | No file  | `ba45f2203e2d`  |
| 621    | No file  | `ba45f2203e2d`  |
| 617    | No file  | `ba45f2203e2d`  |
| 615    | No file  | `ba45f2203e2d`  |
| 606    | No file  | `ba45f2203e2d`  |
| 599    | No file  | `ba45f2203e2d`  |
| 592    | No file  | `ba45f2203e2d`  |
| 586    | No file  | `ba45f2203e2d`  |
| 577    | No file  | `ba45f2203e2d`  |
| 569    | No file  | `ba45f2203e2d`  |
| 561    | No file  | `ba45f2203e2d`  |
| 554    | No file  | `ba45f2203e2d`  |
| 542    | No file  | `ba45f2203e2d`  |
| 532    | No file  | `ba45f2203e2d`  |
| 531    | No file  | `ba45f2203e2d`  |
| 526    | No file  | `ba45f2203e2d`  |
| 521    | No file  | `ba45f2203e2d`  |
| 517    | No file  | `ba45f2203e2d`  |
| 510    | No file  | `ba45f2203e2d`  |
| 508    | No file  | `ba45f2203e2d`  |
| 504    | No file  | `ba45f2203e2d`  |
| 497    | No file  | `ba45f2203e2d`  |
| 491    | No file  | `ba45f2203e2d`  |
| 485    | No file  | `ba45f2203e2d`  |
| 478    | No file  | `ba45f2203e2d`  |
| 472    | No file  | `ba45f2203e2d`  |
| 466    | No file  | `ba45f2203e2d`  |
| 457    | No file  | `ba45f2203e2d`  |
| 452    | No file  | `ba45f2203e2d`  |
| 449    | No file  | `ba45f2203e2d`  |
| 435    | No file  | `ba45f2203e2d`  |

<!-- versions:end -->

## Companion Files

None; the file has no `*offset.dbss` index. The handler names the items
through LOC type 0 and the item icon index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 6 x 306 = 1,840 bytes.

### Row (306 bytes)

| Offset  | Type    | Field           | Notes                                                                  |
| ------- | ------- | --------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32     | item_key        | The accessory, an item enchant key at level `0`                        |
| `+0x04` | u8      | group_no        | Group of the choice, `1` or `2` on client 3474                         |
| `+0x05` | u8      | accessory_index | Choice number from `1`, the `accessoryIndex` of the getters; unique    |
| `+0x06` | Step[5] | steps           | Step N (from 0) enhances the accessory to level N + 1, see Step        |

The rows are in descending `accessory_index` order (6 to 1 on client 3474).

### Step (60 bytes)

| Offset  | Type        | Field     | Notes                                      |
| ------- | ----------- | --------- | ------------------------------------------ |
| `+0x00` | Material[5] | materials | The materials of the step, see Material    |

### Material (12 bytes)

| Offset  | Type | Field      | Notes                                                                |
| ------- | ---- | ---------- | -------------------------------------------------------------------- |
| `+0x00` | u32  | item_key   | Material item, an item enchant key (`enchant_level << 24 \| item_id`) |
| `+0x04` | u64  | need_count | How many the step needs                                              |

The fifth material of step N is the row's accessory at level N, count `1`.
The window greys it out until the other four are in
(`materialIndex == __eMaxAccessoryStepUpMaterialCount - 1`).

## Steps and Groups

The window draws `__eMaxAccessoryStepUpEnchantLevel` steps
(`Static_Step_1` onward) of `__eMaxAccessoryStepUpMaterialCount` materials
(`Static_MaterialItem_L1`, `R1`, `L2`, `R2`, `L3`), five of each, which is
the `Step[5]` and `Material[5]` the row holds. The step of a material is the
`enchantLevel` argument, from 0, and the window names it
`accessoryEnchantLevel = enchantLevel + 1`.

`ToClient_getAccessoryMaxGroupIndex(groupNo)` gives the last
`accessory_index` of a group; the window lists the choices of the player's
current group. On client 3474 both groups hold the same three accessories:

| `accessory_index` | `group_no` | Accessory                        |
| ----------------- | ---------- | -------------------------------- |
| 1, 4              | 1, 2       | 550801 Ring of Crescent Guardian |
| 2, 5              | 1, 2       | 550802 Narc Ear Accessory        |
| 3, 6              | 1, 2       | 550803 Tungrad Earring           |

Every row of client 3474 asks for the same four materials per step: 44350
Yona's Fragment, 4918 Magical Shard, 16001 Black Stone and 45162 Old Moon
Alchemy Catalyst.

## Field Names

Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
1784 has the table, and the client 1784 PAZ has no `accessorystepup.dbss`
(clients 2519 to 3474 have it). The names follow the Lua getters above and
`getAccessoryStepUpManager()`, whose `getAccessoryGroupNo()` and
`getAccessoryIndex()` pick a row; `need_count` is the value of
`ToClient_getAccessoryStepUpMaterialNeedCount`.

## Notes

- Client 2519 has the same rows with larger counts in the last step (for
  example 110 Yona's Fragment where client 3474 asks for 100).
