# `servanttransformdata.dbss` Format

## Purpose

The ship appearance changes a wharf offers: one row per change, from one
ship character to another. On client 3474 the file has 2 rows: form `1`
turns Epheria Sailboat (`31001`) into Epheria Galleon (`31020`), form `2`
turns Epheria Frigate (`31003`) into Panokseon (`31025`). The look change
window of `panel_dialog_servantlookchange_all_1.luac` and `_2.luac` reads
the table through `getServantTransformManager()` when it is opened at a
wharf (its confirm box uses `LUA_WHARFLIST_CHANGECONFIRM_TITLE`), and sends
the chosen form with `stable_servantTransform(slot, formIndex)`. Companion
`servanttransformdataoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------ | --------- |
| 1      | 1346 and later | 3483    | `servanttransformdata.dbss`       | 20    | 2 Row        | 8         |
| 1      | 1346 and later | 3483    | `servanttransformdataoffset.dbss` | 24    | 2 Offset Row | 10        |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `servanttransformdata.dbss`       | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `servanttransformdataoffset.dbss` | 24 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `62fdf537fd23`  |
| 3482   | Layout 1             | `62fdf537fd23`  |
| 3474   | Layout 1             | `62fdf537fd23`  |
| 3473   | Layout 1             | `62fdf537fd23`  |
| 3464   | Layout 1             | `62fdf537fd23`  |
| 3458   | Layout 1             | `62fdf537fd23`  |
| 3454   | Layout 1             | `62fdf537fd23`  |
| 3444   | Layout 1             | `62fdf537fd23`  |
| 3435   | Layout 1             | `62fdf537fd23`  |
| 3426   | Layout 1             | `62fdf537fd23`  |
| 3418   | Layout 1             | `62fdf537fd23`  |
| 3412   | Layout 1             | `62fdf537fd23`  |
| 3402   | Layout 1             | `62fdf537fd23`  |
| 3396   | Layout 1             | `62fdf537fd23`  |
| 3387   | Layout 1             | `62fdf537fd23`  |
| 3381   | Layout 1             | `62fdf537fd23`  |
| 3373   | Layout 1             | `62fdf537fd23`  |
| 3364   | Layout 1             | `62fdf537fd23`  |
| 3356   | Layout 1             | `62fdf537fd23`  |
| 3349   | Layout 1             | `62fdf537fd23`  |
| 3342   | Layout 1             | `62fdf537fd23`  |
| 3335   | Layout 1             | `62fdf537fd23`  |
| 3326   | Layout 1             | `62fdf537fd23`  |
| 3321   | Layout 1             | `62fdf537fd23`  |
| 3314   | Layout 1             | `62fdf537fd23`  |
| 3303   | Layout 1             | `62fdf537fd23`  |
| 3302   | Layout 1             | `62fdf537fd23`  |
| 3293   | Layout 1             | `62fdf537fd23`  |
| 3283   | Layout 1             | `62fdf537fd23`  |
| 3275   | Layout 1             | `62fdf537fd23`  |
| 3267   | Layout 1             | `62fdf537fd23`  |
| 3258   | Layout 1             | `62fdf537fd23`  |
| 3251   | Layout 1             | `62fdf537fd23`  |
| 3242   | Layout 1             | `62fdf537fd23`  |
| 3235   | Layout 1             | `62fdf537fd23`  |
| 3229   | Layout 1             | `62fdf537fd23`  |
| 3212   | Layout 1             | `62fdf537fd23`  |
| 3203   | Layout 1             | `62fdf537fd23`  |
| 3193   | Layout 1             | `62fdf537fd23`  |
| 3186   | Layout 1             | `62fdf537fd23`  |
| 3177   | Layout 1             | `62fdf537fd23`  |
| 3169   | Layout 1             | `62fdf537fd23`  |
| 3158   | Layout 1             | `62fdf537fd23`  |
| 3151   | Layout 1             | `62fdf537fd23`  |
| 3144   | Layout 1             | `62fdf537fd23`  |
| 3133   | Layout 1             | `62fdf537fd23`  |
| 3125   | Layout 1             | `62fdf537fd23`  |
| 3118   | Layout 1             | `62fdf537fd23`  |
| 3111   | Layout 1             | `62fdf537fd23`  |
| 3103   | Layout 1             | `62fdf537fd23`  |
| 3095   | Layout 1             | `62fdf537fd23`  |
| 3086   | Layout 1             | `62fdf537fd23`  |
| 3072   | Layout 1             | `62fdf537fd23`  |
| 3062   | Layout 1             | `62fdf537fd23`  |
| 3052   | Layout 1             | `62fdf537fd23`  |
| 3045   | Layout 1             | `62fdf537fd23`  |
| 3037   | Layout 1             | `62fdf537fd23`  |
| 3030   | Layout 1             | `62fdf537fd23`  |
| 3021   | Layout 1             | `62fdf537fd23`  |
| 3012   | Layout 1             | `62fdf537fd23`  |
| 3002   | Layout 1             | `62fdf537fd23`  |
| 2995   | Layout 1             | `62fdf537fd23`  |
| 2987   | Layout 1             | `62fdf537fd23`  |
| 2978   | Layout 1             | `62fdf537fd23`  |
| 2970   | Layout 1             | `62fdf537fd23`  |
| 2959   | Layout 1             | `62fdf537fd23`  |
| 2951   | Layout 1             | `62fdf537fd23`  |
| 2942   | Layout 1             | `62fdf537fd23`  |
| 2935   | Layout 1             | `62fdf537fd23`  |
| 2932   | Layout 1             | `62fdf537fd23`  |
| 2923   | Layout 1             | `62fdf537fd23`  |
| 2919   | Layout 1             | `62fdf537fd23`  |
| 2907   | Layout 1             | `62fdf537fd23`  |
| 2900   | Layout 1             | `62fdf537fd23`  |
| 2891   | Layout 1             | `62fdf537fd23`  |
| 2882   | Layout 1             | `62fdf537fd23`  |
| 2872   | Layout 1             | `62fdf537fd23`  |
| 2863   | Layout 1             | `62fdf537fd23`  |
| 2855   | Layout 1             | `62fdf537fd23`  |
| 2849   | Layout 1             | `62fdf537fd23`  |
| 2844   | Layout 1             | `62fdf537fd23`  |
| 2834   | Layout 1             | `62fdf537fd23`  |
| 2825   | Layout 1             | `62fdf537fd23`  |
| 2819   | Layout 1             | `62fdf537fd23`  |
| 2811   | Layout 1             | `62fdf537fd23`  |
| 2803   | Layout 1             | `62fdf537fd23`  |
| 2794   | Layout 1             | `62fdf537fd23`  |
| 2783   | Layout 1             | `62fdf537fd23`  |
| 2774   | Layout 1             | `62fdf537fd23`  |
| 2765   | Layout 1             | `62fdf537fd23`  |
| 2756   | Layout 1             | `62fdf537fd23`  |
| 2750   | Layout 1             | `62fdf537fd23`  |
| 2743   | Layout 1             | `62fdf537fd23`  |
| 2736   | Layout 1             | `62fdf537fd23`  |
| 2726   | Layout 1             | `62fdf537fd23`  |
| 2717   | Layout 1             | `62fdf537fd23`  |
| 2709   | Layout 1             | `62fdf537fd23`  |
| 2703   | Layout 1             | `62fdf537fd23`  |
| 2695   | Layout 1             | `62fdf537fd23`  |
| 2684   | Layout 1             | `62fdf537fd23`  |
| 2672   | Layout 1             | `62fdf537fd23`  |
| 2665   | Layout 1             | `62fdf537fd23`  |
| 2657   | Layout 1             | `62fdf537fd23`  |
| 2649   | Layout 1             | `62fdf537fd23`  |
| 2644   | Layout 1             | `62fdf537fd23`  |
| 2637   | Layout 1             | `62fdf537fd23`  |
| 2629   | Layout 1             | `62fdf537fd23`  |
| 2619   | Layout 1             | `62fdf537fd23`  |
| 2612   | Layout 1             | `62fdf537fd23`  |
| 2606   | Layout 1             | `62fdf537fd23`  |
| 2602   | Layout 1             | `62fdf537fd23`  |
| 2601   | Layout 1             | `62fdf537fd23`  |
| 2592   | Layout 1             | `62fdf537fd23`  |
| 2583   | Layout 1             | `62fdf537fd23`  |
| 2575   | Layout 1             | `62fdf537fd23`  |
| 2567   | Layout 1             | `62fdf537fd23`  |
| 2560   | Layout 1             | `62fdf537fd23`  |
| 2553   | Layout 1             | `62fdf537fd23`  |
| 2545   | Layout 1             | `62fdf537fd23`  |
| 2538   | Layout 1             | `62fdf537fd23`  |
| 2529   | Layout 1             | `62fdf537fd23`  |
| 2519   | Layout 1             | `62fdf537fd23`  |
| 2513   | Layout 1             | `62fdf537fd23`  |
| 2510   | Layout 1             | `62fdf537fd23`  |
| 2507   | Layout 1             | `62fdf537fd23`  |
| 2503   | Layout 1             | `62fdf537fd23`  |
| 2498   | Layout 1             | `62fdf537fd23`  |
| 2492   | Layout 1             | `62fdf537fd23`  |
| 2487   | Layout 1             | `62fdf537fd23`  |
| 2480   | Layout 1             | `62fdf537fd23`  |
| 2474   | Layout 1             | `62fdf537fd23`  |
| 2468   | Layout 1             | `62fdf537fd23`  |
| 2460   | Layout 1             | `62fdf537fd23`  |
| 2453   | Layout 1             | `62fdf537fd23`  |
| 2444   | Layout 1             | `62fdf537fd23`  |
| 2438   | Layout 1             | `62fdf537fd23`  |
| 2434   | Layout 1             | `62fdf537fd23`  |
| 2429   | Layout 1             | `62fdf537fd23`  |
| 2421   | Layout 1             | `62fdf537fd23`  |
| 2414   | Layout 1             | `62fdf537fd23`  |
| 2407   | Layout 1             | `62fdf537fd23`  |
| 2401   | Layout 1             | `62fdf537fd23`  |
| 2397   | Layout 1             | `62fdf537fd23`  |
| 2393   | Layout 1             | `62fdf537fd23`  |
| 2384   | Layout 1             | `62fdf537fd23`  |
| 2378   | Layout 1             | `62fdf537fd23`  |
| 2372   | Layout 1             | `62fdf537fd23`  |
| 2358   | Layout 1             | `62fdf537fd23`  |
| 2352   | Layout 1             | `62fdf537fd23`  |
| 2347   | Layout 1             | `62fdf537fd23`  |
| 2343   | Layout 1             | `62fdf537fd23`  |
| 2335   | Layout 1             | `62fdf537fd23`  |
| 2327   | Layout 1             | `62fdf537fd23`  |
| 2324   | Layout 1             | `62fdf537fd23`  |
| 2319   | Layout 1             | `62fdf537fd23`  |
| 2313   | Layout 1             | `62fdf537fd23`  |
| 2308   | Layout 1             | `62fdf537fd23`  |
| 2302   | Layout 1             | `62fdf537fd23`  |
| 2295   | Layout 1             | `62fdf537fd23`  |
| 2290   | Layout 1             | `62fdf537fd23`  |
| 2284   | Layout 1             | `62fdf537fd23`  |
| 2276   | Layout 1             | `62fdf537fd23`  |
| 2269   | Layout 1             | `62fdf537fd23`  |
| 2259   | Layout 1             | `62fdf537fd23`  |
| 2250   | Layout 1             | `62fdf537fd23`  |
| 2243   | Layout 1             | `62fdf537fd23`  |
| 2235   | Layout 1             | `62fdf537fd23`  |
| 2229   | Layout 1             | `62fdf537fd23`  |
| 2224   | Layout 1             | `62fdf537fd23`  |
| 2218   | Layout 1             | `62fdf537fd23`  |
| 2215   | Layout 1             | `62fdf537fd23`  |
| 2207   | Layout 1             | `62fdf537fd23`  |
| 2203   | Layout 1             | `62fdf537fd23`  |
| 2196   | Layout 1             | `62fdf537fd23`  |
| 2192   | Layout 1             | `62fdf537fd23`  |
| 2189   | Layout 1             | `62fdf537fd23`  |
| 2183   | Layout 1             | `62fdf537fd23`  |
| 2179   | Layout 1             | `62fdf537fd23`  |
| 2171   | Layout 1             | `62fdf537fd23`  |
| 2163   | Layout 1             | `62fdf537fd23`  |
| 2156   | Layout 1             | `62fdf537fd23`  |
| 2151   | Layout 1             | `62fdf537fd23`  |
| 2147   | Layout 1             | `62fdf537fd23`  |
| 2142   | Layout 1             | `62fdf537fd23`  |
| 2138   | Layout 1             | `62fdf537fd23`  |
| 2134   | Layout 1             | `62fdf537fd23`  |
| 2130   | Layout 1             | `62fdf537fd23`  |
| 2122   | Layout 1             | `62fdf537fd23`  |
| 2107   | Layout 1             | `62fdf537fd23`  |
| 2098   | Layout 1             | `62fdf537fd23`  |
| 2089   | Layout 1             | `62fdf537fd23`  |
| 2081   | Layout 1             | `62fdf537fd23`  |
| 2073   | Layout 1             | `62fdf537fd23`  |
| 2067   | Layout 1             | `62fdf537fd23`  |
| 2063   | Layout 1             | `62fdf537fd23`  |
| 2059   | Layout 1             | `62fdf537fd23`  |
| 2052   | Layout 1             | `62fdf537fd23`  |
| 2044   | Layout 1             | `62fdf537fd23`  |
| 2039   | Layout 1             | `62fdf537fd23`  |
| 2032   | Layout 1             | `62fdf537fd23`  |
| 2025   | Layout 1             | `62fdf537fd23`  |
| 2011   | Layout 1             | `62fdf537fd23`  |
| 2005   | Layout 1             | `62fdf537fd23`  |
| 2000   | Layout 1             | `62fdf537fd23`  |
| 1996   | Layout 1             | `62fdf537fd23`  |
| 1991   | Layout 1             | `62fdf537fd23`  |
| 1985   | Layout 1             | `62fdf537fd23`  |
| 1980   | Layout 1             | `62fdf537fd23`  |
| 1969   | Layout 1             | `62fdf537fd23`  |
| 1964   | Layout 1             | `62fdf537fd23`  |
| 1958   | Layout 1             | `62fdf537fd23`  |
| 1950   | Layout 1             | `62fdf537fd23`  |
| 1945   | Layout 1             | `62fdf537fd23`  |
| 1937   | Layout 1             | `62fdf537fd23`  |
| 1933   | Layout 1             | `62fdf537fd23`  |
| 1927   | Layout 1             | `62fdf537fd23`  |
| 1921   | Layout 1             | `62fdf537fd23`  |
| 1914   | Layout 1             | `62fdf537fd23`  |
| 1908   | Layout 1             | `62fdf537fd23`  |
| 1897   | Layout 1             | `62fdf537fd23`  |
| 1892   | Layout 1             | `62fdf537fd23`  |
| 1886   | Layout 1             | `62fdf537fd23`  |
| 1881   | Layout 1             | `62fdf537fd23`  |
| 1871   | Layout 1             | `62fdf537fd23`  |
| 1866   | Layout 1             | `62fdf537fd23`  |
| 1862   | Layout 1             | `62fdf537fd23`  |
| 1854   | Layout 1             | `62fdf537fd23`  |
| 1846   | Layout 1             | `62fdf537fd23`  |
| 1838   | Layout 1             | `62fdf537fd23`  |
| 1832   | Layout 1             | `62fdf537fd23`  |
| 1826   | Layout 1             | `62fdf537fd23`  |
| 1822   | Layout 1             | `62fdf537fd23`  |
| 1818   | Layout 1             | `62fdf537fd23`  |
| 1804   | Layout 1             | `62fdf537fd23`  |
| 1794   | Layout 1             | `62fdf537fd23`  |
| 1790   | Layout 1             | `62fdf537fd23`  |
| 1784   | Layout 1             | `62fdf537fd23`  |
| 1774   | Layout 1             | `62fdf537fd23`  |
| 1771   | Layout 1             | `62fdf537fd23`  |
| 1762   | Layout 1             | `62fdf537fd23`  |
| 1759   | Layout 1             | `62fdf537fd23`  |
| 1754   | Layout 1             | `62fdf537fd23`  |
| 1749   | Layout 1             | `62fdf537fd23`  |
| 1743   | Layout 1             | `62fdf537fd23`  |
| 1737   | Layout 1             | `62fdf537fd23`  |
| 1731   | Layout 1             | `62fdf537fd23`  |
| 1725   | Layout 1             | `62fdf537fd23`  |
| 1717   | Layout 1             | `62fdf537fd23`  |
| 1710   | Layout 1             | `62fdf537fd23`  |
| 1704   | Layout 1             | `62fdf537fd23`  |
| 1698   | Layout 1             | `62fdf537fd23`  |
| 1690   | Layout 1             | `62fdf537fd23`  |
| 1685   | Layout 1             | `62fdf537fd23`  |
| 1680   | Layout 1             | `62fdf537fd23`  |
| 1674   | Layout 1             | `62fdf537fd23`  |
| 1668   | Layout 1             | `62fdf537fd23`  |
| 1659   | Layout 1             | `62fdf537fd23`  |
| 1649   | Layout 1             | `62fdf537fd23`  |
| 1642   | Layout 1             | `62fdf537fd23`  |
| 1636   | Layout 1             | `62fdf537fd23`  |
| 1628   | Layout 1             | `62fdf537fd23`  |
| 1622   | Layout 1             | `62fdf537fd23`  |
| 1614   | Layout 1             | `62fdf537fd23`  |
| 1608   | Layout 1             | `62fdf537fd23`  |
| 1602   | Layout 1             | `62fdf537fd23`  |
| 1598   | Layout 1             | `62fdf537fd23`  |
| 1594   | Layout 1             | `62fdf537fd23`  |
| 1590   | Layout 1             | `62fdf537fd23`  |
| 1587   | Layout 1             | `62fdf537fd23`  |
| 1584   | Layout 1             | `62fdf537fd23`  |
| 1579   | Layout 1             | `62fdf537fd23`  |
| 1572   | Layout 1             | `62fdf537fd23`  |
| 1565   | Layout 1             | `62fdf537fd23`  |
| 1559   | Layout 1             | `62fdf537fd23`  |
| 1554   | Layout 1             | `62fdf537fd23`  |
| 1547   | Layout 1             | `62fdf537fd23`  |
| 1537   | Layout 1             | `62fdf537fd23`  |
| 1529   | Layout 1             | `62fdf537fd23`  |
| 1524   | Layout 1             | `62fdf537fd23`  |
| 1519   | Layout 1             | `62fdf537fd23`  |
| 1509   | Layout 1             | `62fdf537fd23`  |
| 1506   | Layout 1             | `62fdf537fd23`  |
| 1504   | Layout 1             | `62fdf537fd23`  |
| 1500   | Layout 1             | `62fdf537fd23`  |
| 1493   | Layout 1             | `62fdf537fd23`  |
| 1489   | Layout 1             | `62fdf537fd23`  |
| 1485   | Layout 1             | `62fdf537fd23`  |
| 1481   | Layout 1             | `62fdf537fd23`  |
| 1474   | Layout 1             | `62fdf537fd23`  |
| 1466   | Layout 1             | `62fdf537fd23`  |
| 1462   | Layout 1             | `62fdf537fd23`  |
| 1459   | Layout 1             | `62fdf537fd23`  |
| 1453   | Layout 1             | `62fdf537fd23`  |
| 1450   | Layout 1             | `62fdf537fd23`  |
| 1445   | Layout 1             | `62fdf537fd23`  |
| 1439   | Layout 1             | `62fdf537fd23`  |
| 1433   | Layout 1             | `62fdf537fd23`  |
| 1430   | Layout 1             | `62fdf537fd23`  |
| 1426   | Layout 1             | `62fdf537fd23`  |
| 1421   | Layout 1             | `62fdf537fd23`  |
| 1417   | Layout 1             | `62fdf537fd23`  |
| 1416   | Layout 1             | `62fdf537fd23`  |
| 1409   | Layout 1             | `62fdf537fd23`  |
| 1405   | Layout 1             | `62fdf537fd23`  |
| 1401   | Layout 1             | `62fdf537fd23`  |
| 1396   | Layout 1             | `62fdf537fd23`  |
| 1391   | Layout 1             | `62fdf537fd23`  |
| 1390   | Layout 1             | `62fdf537fd23`  |
| 1386   | Layout 1             | `62fdf537fd23`  |
| 1381   | Layout 1             | `62fdf537fd23`  |
| 1379   | Layout 1             | `62fdf537fd23`  |
| 1372   | Layout 1             | `62fdf537fd23`  |
| 1366   | Layout 1             | `62fdf537fd23`  |
| 1364   | Layout 1             | `62fdf537fd23`  |
| 1363   | Layout 1             | `62fdf537fd23`  |
| 1360   | Layout 1             | `62fdf537fd23`  |
| 1358   | Layout 1             | `62fdf537fd23`  |
| 1355   | Layout 1             | `62fdf537fd23`  |
| 1351   | Layout 1             | `62fdf537fd23`  |
| 1348   | Layout 1             | `62fdf537fd23`  |
| 1346   | Layout 1             | `62fdf537fd23`  |
| 1341   | No documented layout | `62fdf537fd23`  |
| 1340   | No documented layout | `62fdf537fd23`  |
| 1338   | No documented layout | `62fdf537fd23`  |
| 1335   | No documented layout | `62fdf537fd23`  |
| 1333   | No documented layout | `62fdf537fd23`  |
| 1329   | No documented layout | `62fdf537fd23`  |
| 1327   | No documented layout | `62fdf537fd23`  |
| 1324   | No documented layout | `62fdf537fd23`  |
| 1321   | No documented layout | `62fdf537fd23`  |
| 1319   | No documented layout | `62fdf537fd23`  |
| 1318   | No documented layout | `62fdf537fd23`  |
| 1316   | No documented layout | `62fdf537fd23`  |
| 1313   | No documented layout | `62fdf537fd23`  |
| 1311   | No documented layout | `62fdf537fd23`  |
| 1309   | No documented layout | `62fdf537fd23`  |
| 1304   | No documented layout | `62fdf537fd23`  |
| 1292   | No documented layout | `62fdf537fd23`  |
| 1286   | No documented layout | `62fdf537fd23`  |
| 1280   | No documented layout | `62fdf537fd23`  |
| 1276   | No documented layout | `62fdf537fd23`  |
| 1267   | No file              | `62fdf537fd23`  |
| 1261   | No file              | `62fdf537fd23`  |
| 1256   | No documented layout | `62fdf537fd23`  |
| 1250   | No file              | `62fdf537fd23`  |
| 1246   | No file              | `62fdf537fd23`  |
| 1239   | No file              | `62fdf537fd23`  |
| 1230   | No file              | `62fdf537fd23`  |
| 1226   | No file              | `62fdf537fd23`  |
| 1220   | No file              | `62fdf537fd23`  |
| 1217   | No file              | `62fdf537fd23`  |
| 1211   | No file              | `62fdf537fd23`  |
| 1210   | No file              | `62fdf537fd23`  |
| 1208   | No file              | `62fdf537fd23`  |
| 1203   | No file              | `62fdf537fd23`  |
| 1197   | No file              | `62fdf537fd23`  |
| 1194   | No file              | `62fdf537fd23`  |
| 1192   | No file              | `62fdf537fd23`  |
| 1187   | No file              | `62fdf537fd23`  |
| 1183   | No file              | `62fdf537fd23`  |
| 1177   | No file              | `62fdf537fd23`  |
| 1173   | No file              | `62fdf537fd23`  |
| 1167   | No file              | `62fdf537fd23`  |
| 1164   | No file              | `62fdf537fd23`  |
| 1156   | No file              | `62fdf537fd23`  |
| 1149   | No file              | `62fdf537fd23`  |
| 1144   | No file              | `62fdf537fd23`  |
| 1137   | No file              | `62fdf537fd23`  |
| 1132   | No file              | `62fdf537fd23`  |
| 1127   | No file              | `62fdf537fd23`  |
| 1122   | No file              | `62fdf537fd23`  |
| 1118   | No file              | `62fdf537fd23`  |
| 1114   | No file              | `62fdf537fd23`  |
| 1109   | No file              | `62fdf537fd23`  |
| 1102   | No file              | `62fdf537fd23`  |
| 1096   | No file              | `62fdf537fd23`  |
| 1088   | No file              | `62fdf537fd23`  |
| 1081   | No file              | `62fdf537fd23`  |
| 1076   | No file              | `62fdf537fd23`  |
| 1069   | No file              | `62fdf537fd23`  |
| 1064   | No file              | `62fdf537fd23`  |
| 1058   | No file              | `62fdf537fd23`  |
| 1051   | No file              | `62fdf537fd23`  |
| 1044   | No file              | `62fdf537fd23`  |
| 1036   | No file              | `62fdf537fd23`  |
| 1026   | No file              | `62fdf537fd23`  |
| 1016   | No file              | `62fdf537fd23`  |
| 1009   | No file              | `62fdf537fd23`  |
| 1005   | No file              | `62fdf537fd23`  |
| 1000   | No file              | `62fdf537fd23`  |
| 998    | No file              | `62fdf537fd23`  |
| 990    | No file              | `62fdf537fd23`  |
| 979    | No file              | `62fdf537fd23`  |
| 972    | No file              | `62fdf537fd23`  |
| 963    | No file              | `62fdf537fd23`  |
| 955    | No file              | `62fdf537fd23`  |
| 946    | No file              | `62fdf537fd23`  |
| 938    | No file              | `62fdf537fd23`  |
| 927    | No file              | `62fdf537fd23`  |
| 911    | No file              | `62fdf537fd23`  |
| 904    | No file              | `62fdf537fd23`  |
| 899    | No file              | `62fdf537fd23`  |
| 894    | No file              | `62fdf537fd23`  |
| 885    | No file              | `62fdf537fd23`  |
| 879    | No file              | `62fdf537fd23`  |
| 872    | No file              | `62fdf537fd23`  |
| 864    | No file              | `62fdf537fd23`  |
| 855    | No file              | `62fdf537fd23`  |
| 853    | No file              | `62fdf537fd23`  |
| 845    | No file              | `62fdf537fd23`  |
| 837    | No file              | `62fdf537fd23`  |
| 829    | No file              | `62fdf537fd23`  |
| 822    | No file              | `62fdf537fd23`  |
| 814    | No file              | `62fdf537fd23`  |
| 805    | No file              | `62fdf537fd23`  |
| 794    | No file              | `62fdf537fd23`  |
| 787    | No file              | `62fdf537fd23`  |
| 780    | No file              | `62fdf537fd23`  |
| 771    | No file              | `62fdf537fd23`  |
| 760    | No file              | `62fdf537fd23`  |
| 748    | No file              | `62fdf537fd23`  |
| 741    | No file              | `62fdf537fd23`  |
| 736    | No file              | `62fdf537fd23`  |
| 731    | No file              | `62fdf537fd23`  |
| 723    | No file              | `62fdf537fd23`  |
| 711    | No file              | `62fdf537fd23`  |
| 707    | No file              | `62fdf537fd23`  |
| 697    | No file              | `62fdf537fd23`  |
| 689    | No file              | `62fdf537fd23`  |
| 683    | No file              | `62fdf537fd23`  |
| 678    | No file              | `62fdf537fd23`  |
| 670    | No file              | `62fdf537fd23`  |
| 661    | No file              | `62fdf537fd23`  |
| 656    | No file              | `62fdf537fd23`  |
| 652    | No file              | `62fdf537fd23`  |
| 643    | No file              | `62fdf537fd23`  |
| 637    | No file              | `62fdf537fd23`  |
| 630    | No file              | `62fdf537fd23`  |
| 627    | No file              | `62fdf537fd23`  |
| 621    | No file              | `62fdf537fd23`  |
| 617    | No file              | `62fdf537fd23`  |
| 615    | No file              | `62fdf537fd23`  |
| 606    | No file              | `62fdf537fd23`  |
| 599    | No file              | `62fdf537fd23`  |
| 592    | No file              | `62fdf537fd23`  |
| 586    | No file              | `62fdf537fd23`  |
| 577    | No file              | `62fdf537fd23`  |
| 569    | No file              | `62fdf537fd23`  |
| 561    | No file              | `62fdf537fd23`  |
| 554    | No file              | `62fdf537fd23`  |
| 542    | No file              | `62fdf537fd23`  |
| 532    | No file              | `62fdf537fd23`  |
| 531    | No file              | `62fdf537fd23`  |
| 526    | No file              | `62fdf537fd23`  |
| 521    | No file              | `62fdf537fd23`  |
| 517    | No file              | `62fdf537fd23`  |
| 510    | No file              | `62fdf537fd23`  |
| 508    | No file              | `62fdf537fd23`  |
| 504    | No file              | `62fdf537fd23`  |
| 497    | No file              | `62fdf537fd23`  |
| 491    | No file              | `62fdf537fd23`  |
| 485    | No file              | `62fdf537fd23`  |
| 478    | No file              | `62fdf537fd23`  |
| 472    | No file              | `62fdf537fd23`  |
| 466    | No file              | `62fdf537fd23`  |
| 457    | No file              | `62fdf537fd23`  |
| 452    | No file              | `62fdf537fd23`  |
| 449    | No file              | `62fdf537fd23`  |
| 435    | No file              | `62fdf537fd23`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                 |
| --------------------------------- | -------- | -------------------------------------------------------------------- |
| `servanttransformdataoffset.dbss` | Optional | `form_key -> (offset, size)` of every row; the main file can be walked without it |
| `characterstaticoffset.dbss`      | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key links |
| `languagedata_en.loc`             | Optional | Character names (LOC type 6)                                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (8 bytes)

| Offset  | Type | Field              | Notes                                                              |
| ------- | ---- | ------------------ | ------------------------------------------------------------------ |
| `+0x00` | u16  | form_key           | Unique; the `formIndex` the Lua sends to `stable_servantTransform` |
| `+0x02` | u16  | form_key_dup       | Equal to `form_key` in every row; the offset file points here      |
| `+0x04` | u16  | from_character_key | Ship that changes; a [`servant.bss`](servant_bss.md) row (client 3474) |
| `+0x06` | u16  | to_character_key   | Ship it changes into; a `servant.bss` row (client 3474)            |

### `servanttransformdataoffset.dbss`

| Offset  | Type              | Field | Notes                                        |
| ------- | ----------------- | ----- | -------------------------------------------- |
| `+0x00` | u32               | count | Equals the `servanttransformdata.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row         |

### Offset Row (10 bytes)

| Offset  | Type | Field    | Notes                                                   |
| ------- | ---- | -------- | ------------------------------------------------------- |
| `+0x00` | u16  | form_key | Key of the row it points at                             |
| `+0x02` | u32  | offset   | Row start + 2, at `form_key_dup`                        |
| `+0x06` | u32  | size     | The row without its leading `form_key`: always `6`      |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in main file order.

## Field Names

The names follow the `ServantTransform_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 and the same sheet in its
`datasheet_formdatatable.xlsm` (next to `Form_Table`), columns `FormKey`,
`FromCharacterKey` and `ToCharacterKey`. Its 2 rows match the file by all
three values on clients 1784 and 3474 (2 of 2). The `ServantTransform_Table`
of a private server on client 519 holds the same 2 rows.

The client 1784 server dump names the static status
`gc::ServantTransformStaticStatus`, keyed by a `KeyType<unsigned short>`,
and its loader `LoadServantTransformStaticInformation`. Its check messages
call the key member `_transformIndex` and the table "Servant 외형변경 정보"
(servant appearance change info). The client Lua reads the same row with
`getTransformIndex()` and `getTransformCharacterKey()`.

## Notes

- Client 1784 has the same 20-byte file and the same 24-byte offset file,
  byte for byte.
- The file is not sorted by key: form `2` comes first.
- Neither change is a ship upgrade: [`servantupgrade.dbss`](servantupgrade_dbss.md)
  on client 3474 upgrades Epheria Sailboat into Improved Epheria Sailboat
  (`31058`) or Epheria Caravel (`31048`), and Epheria Frigate into Improved
  Epheria Frigate (`31059`) or Epheria Galleass (`31049`). No upgrade row
  leads to Epheria Galleon or Panokseon.
- The 1784 server dump rejects a row whose two character keys are equal,
  whose keys have no servant, or whose servants differ in `servantKind` or
  `servantKindSub`.
- `CppEnums.ContentsType_ServantTransform` is `67` in
  `global_define_cpp_enum.luac` (client 3474).

## Open Questions

### Servant Kinds of the Two Ships

The 1784 server check wants the same `servantKind` on both sides of a row,
but [`servant.bss`](servant_bss.md) on client 3474 gives Epheria Sailboat
kind `15` (`PersonalTradeShip`) and Epheria Galleon kind `21`
(`CashPersonalTradeShip`), Epheria Frigate `17` and Panokseon `22`. The
`RaceType` column of the client 1784 `ServantSet_Table` sheet, which matches
`servant_kind` on all 333 client 1784 records, has the same four kinds, so
they did not change after client 1784. Which kind the check compares is
open.

### Whether a Change Can Be Undone

The Lua lists the forms for the ship's current character key
(`getFormListSize(fromCharacterKey)`) and greys out the change button when
the picked form's `getTransformCharacterKey()` equals that key. The file
holds only one direction per form, so whether an Epheria Galleon is offered
form `1` back to Epheria Sailboat is open.
