# `dynamicbssoption.bss` Format

## Purpose

One on/off byte per static status table type (items, characters, cash
products, dialogs, ...), at the type's index. The client Lua asks
`ToClient_isUseDynamicBSS(__eDynamicBSSType_CashProduct)` before it builds
the cash shop filter lists, and `IsUseDynamicBSS()` before it reads NPC
data for the NPC navigation, so the byte says whether that table type uses
the dynamic BSS path. The values fill the PABR body up to the string table
with no count: 109 bytes on client 3482, 88 of them `1`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records   | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | --------- | --------- |
| 1      | 1250 and later | 3483    | `dynamicbssoption.bss` | 125   | 109 Entry | 1         |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `dynamicbssoption.bss` | 125 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `b82c20ac01be`  |
| 3482   | Layout 1 | `b82c20ac01be`  |
| 3474   | Layout 1 | `b82c20ac01be`  |
| 3473   | Layout 1 | `b82c20ac01be`  |
| 3464   | Layout 1 | `b82c20ac01be`  |
| 3458   | Layout 1 | `b82c20ac01be`  |
| 3454   | Layout 1 | `b82c20ac01be`  |
| 3444   | Layout 1 | `b82c20ac01be`  |
| 3435   | Layout 1 | `b82c20ac01be`  |
| 3426   | Layout 1 | `b82c20ac01be`  |
| 3418   | Layout 1 | `b82c20ac01be`  |
| 3412   | Layout 1 | `b82c20ac01be`  |
| 3402   | Layout 1 | `b82c20ac01be`  |
| 3396   | Layout 1 | `b82c20ac01be`  |
| 3387   | Layout 1 | `b82c20ac01be`  |
| 3381   | Layout 1 | `b82c20ac01be`  |
| 3373   | Layout 1 | `b82c20ac01be`  |
| 3364   | Layout 1 | `b82c20ac01be`  |
| 3356   | Layout 1 | `b82c20ac01be`  |
| 3349   | Layout 1 | `b82c20ac01be`  |
| 3342   | Layout 1 | `b82c20ac01be`  |
| 3335   | Layout 1 | `b82c20ac01be`  |
| 3326   | Layout 1 | `b82c20ac01be`  |
| 3321   | Layout 1 | `b82c20ac01be`  |
| 3314   | Layout 1 | `b82c20ac01be`  |
| 3303   | Layout 1 | `b82c20ac01be`  |
| 3302   | Layout 1 | `b82c20ac01be`  |
| 3293   | Layout 1 | `b82c20ac01be`  |
| 3283   | Layout 1 | `b82c20ac01be`  |
| 3275   | Layout 1 | `b82c20ac01be`  |
| 3267   | Layout 1 | `b82c20ac01be`  |
| 3258   | Layout 1 | `b82c20ac01be`  |
| 3251   | Layout 1 | `b82c20ac01be`  |
| 3242   | Layout 1 | `b82c20ac01be`  |
| 3235   | Layout 1 | `b82c20ac01be`  |
| 3229   | Layout 1 | `b82c20ac01be`  |
| 3212   | Layout 1 | `b82c20ac01be`  |
| 3203   | Layout 1 | `b82c20ac01be`  |
| 3193   | Layout 1 | `b82c20ac01be`  |
| 3186   | Layout 1 | `b82c20ac01be`  |
| 3177   | Layout 1 | `b82c20ac01be`  |
| 3169   | Layout 1 | `b82c20ac01be`  |
| 3158   | Layout 1 | `b82c20ac01be`  |
| 3151   | Layout 1 | `b82c20ac01be`  |
| 3144   | Layout 1 | `b82c20ac01be`  |
| 3133   | Layout 1 | `b82c20ac01be`  |
| 3125   | Layout 1 | `b82c20ac01be`  |
| 3118   | Layout 1 | `b82c20ac01be`  |
| 3111   | Layout 1 | `b82c20ac01be`  |
| 3103   | Layout 1 | `b82c20ac01be`  |
| 3095   | Layout 1 | `b82c20ac01be`  |
| 3086   | Layout 1 | `b82c20ac01be`  |
| 3072   | Layout 1 | `b82c20ac01be`  |
| 3062   | Layout 1 | `b82c20ac01be`  |
| 3052   | Layout 1 | `b82c20ac01be`  |
| 3045   | Layout 1 | `b82c20ac01be`  |
| 3037   | Layout 1 | `b82c20ac01be`  |
| 3030   | Layout 1 | `b82c20ac01be`  |
| 3021   | Layout 1 | `b82c20ac01be`  |
| 3012   | Layout 1 | `b82c20ac01be`  |
| 3002   | Layout 1 | `b82c20ac01be`  |
| 2995   | Layout 1 | `b82c20ac01be`  |
| 2987   | Layout 1 | `b82c20ac01be`  |
| 2978   | Layout 1 | `b82c20ac01be`  |
| 2970   | Layout 1 | `b82c20ac01be`  |
| 2959   | Layout 1 | `b82c20ac01be`  |
| 2951   | Layout 1 | `b82c20ac01be`  |
| 2942   | Layout 1 | `b82c20ac01be`  |
| 2935   | Layout 1 | `b82c20ac01be`  |
| 2932   | Layout 1 | `b82c20ac01be`  |
| 2923   | Layout 1 | `b82c20ac01be`  |
| 2919   | Layout 1 | `b82c20ac01be`  |
| 2907   | Layout 1 | `b82c20ac01be`  |
| 2900   | Layout 1 | `b82c20ac01be`  |
| 2891   | Layout 1 | `b82c20ac01be`  |
| 2882   | Layout 1 | `b82c20ac01be`  |
| 2872   | Layout 1 | `b82c20ac01be`  |
| 2863   | Layout 1 | `b82c20ac01be`  |
| 2855   | Layout 1 | `b82c20ac01be`  |
| 2849   | Layout 1 | `b82c20ac01be`  |
| 2844   | Layout 1 | `b82c20ac01be`  |
| 2834   | Layout 1 | `b82c20ac01be`  |
| 2825   | Layout 1 | `b82c20ac01be`  |
| 2819   | Layout 1 | `b82c20ac01be`  |
| 2811   | Layout 1 | `b82c20ac01be`  |
| 2803   | Layout 1 | `b82c20ac01be`  |
| 2794   | Layout 1 | `b82c20ac01be`  |
| 2783   | Layout 1 | `b82c20ac01be`  |
| 2774   | Layout 1 | `b82c20ac01be`  |
| 2765   | Layout 1 | `b82c20ac01be`  |
| 2756   | Layout 1 | `b82c20ac01be`  |
| 2750   | Layout 1 | `b82c20ac01be`  |
| 2743   | Layout 1 | `b82c20ac01be`  |
| 2736   | Layout 1 | `b82c20ac01be`  |
| 2726   | Layout 1 | `b82c20ac01be`  |
| 2717   | Layout 1 | `b82c20ac01be`  |
| 2709   | Layout 1 | `b82c20ac01be`  |
| 2703   | Layout 1 | `b82c20ac01be`  |
| 2695   | Layout 1 | `b82c20ac01be`  |
| 2684   | Layout 1 | `b82c20ac01be`  |
| 2672   | Layout 1 | `b82c20ac01be`  |
| 2665   | Layout 1 | `b82c20ac01be`  |
| 2657   | Layout 1 | `b82c20ac01be`  |
| 2649   | Layout 1 | `b82c20ac01be`  |
| 2644   | Layout 1 | `b82c20ac01be`  |
| 2637   | Layout 1 | `b82c20ac01be`  |
| 2629   | Layout 1 | `b82c20ac01be`  |
| 2619   | Layout 1 | `b82c20ac01be`  |
| 2612   | Layout 1 | `b82c20ac01be`  |
| 2606   | Layout 1 | `b82c20ac01be`  |
| 2602   | Layout 1 | `b82c20ac01be`  |
| 2601   | Layout 1 | `b82c20ac01be`  |
| 2592   | Layout 1 | `b82c20ac01be`  |
| 2583   | Layout 1 | `b82c20ac01be`  |
| 2575   | Layout 1 | `b82c20ac01be`  |
| 2567   | Layout 1 | `b82c20ac01be`  |
| 2560   | Layout 1 | `b82c20ac01be`  |
| 2553   | Layout 1 | `b82c20ac01be`  |
| 2545   | Layout 1 | `b82c20ac01be`  |
| 2538   | Layout 1 | `b82c20ac01be`  |
| 2529   | Layout 1 | `b82c20ac01be`  |
| 2519   | Layout 1 | `b82c20ac01be`  |
| 2513   | Layout 1 | `b82c20ac01be`  |
| 2510   | Layout 1 | `b82c20ac01be`  |
| 2507   | Layout 1 | `b82c20ac01be`  |
| 2503   | Layout 1 | `b82c20ac01be`  |
| 2498   | Layout 1 | `b82c20ac01be`  |
| 2492   | Layout 1 | `b82c20ac01be`  |
| 2487   | Layout 1 | `b82c20ac01be`  |
| 2480   | Layout 1 | `b82c20ac01be`  |
| 2474   | Layout 1 | `b82c20ac01be`  |
| 2468   | Layout 1 | `b82c20ac01be`  |
| 2460   | Layout 1 | `b82c20ac01be`  |
| 2453   | Layout 1 | `b82c20ac01be`  |
| 2444   | Layout 1 | `b82c20ac01be`  |
| 2438   | Layout 1 | `b82c20ac01be`  |
| 2434   | Layout 1 | `b82c20ac01be`  |
| 2429   | Layout 1 | `b82c20ac01be`  |
| 2421   | Layout 1 | `b82c20ac01be`  |
| 2414   | Layout 1 | `b82c20ac01be`  |
| 2407   | Layout 1 | `b82c20ac01be`  |
| 2401   | Layout 1 | `b82c20ac01be`  |
| 2397   | Layout 1 | `b82c20ac01be`  |
| 2393   | Layout 1 | `b82c20ac01be`  |
| 2384   | Layout 1 | `b82c20ac01be`  |
| 2378   | Layout 1 | `b82c20ac01be`  |
| 2372   | Layout 1 | `b82c20ac01be`  |
| 2358   | Layout 1 | `b82c20ac01be`  |
| 2352   | Layout 1 | `b82c20ac01be`  |
| 2347   | Layout 1 | `b82c20ac01be`  |
| 2343   | Layout 1 | `b82c20ac01be`  |
| 2335   | Layout 1 | `b82c20ac01be`  |
| 2327   | Layout 1 | `b82c20ac01be`  |
| 2324   | Layout 1 | `b82c20ac01be`  |
| 2319   | Layout 1 | `b82c20ac01be`  |
| 2313   | Layout 1 | `b82c20ac01be`  |
| 2308   | Layout 1 | `b82c20ac01be`  |
| 2302   | Layout 1 | `b82c20ac01be`  |
| 2295   | Layout 1 | `b82c20ac01be`  |
| 2290   | Layout 1 | `b82c20ac01be`  |
| 2284   | Layout 1 | `b82c20ac01be`  |
| 2276   | Layout 1 | `b82c20ac01be`  |
| 2269   | Layout 1 | `b82c20ac01be`  |
| 2259   | Layout 1 | `b82c20ac01be`  |
| 2250   | Layout 1 | `b82c20ac01be`  |
| 2243   | Layout 1 | `b82c20ac01be`  |
| 2235   | Layout 1 | `b82c20ac01be`  |
| 2229   | Layout 1 | `b82c20ac01be`  |
| 2224   | Layout 1 | `b82c20ac01be`  |
| 2218   | Layout 1 | `b82c20ac01be`  |
| 2215   | Layout 1 | `b82c20ac01be`  |
| 2207   | Layout 1 | `b82c20ac01be`  |
| 2203   | Layout 1 | `b82c20ac01be`  |
| 2196   | Layout 1 | `b82c20ac01be`  |
| 2192   | Layout 1 | `b82c20ac01be`  |
| 2189   | Layout 1 | `b82c20ac01be`  |
| 2183   | Layout 1 | `b82c20ac01be`  |
| 2179   | Layout 1 | `b82c20ac01be`  |
| 2171   | Layout 1 | `b82c20ac01be`  |
| 2163   | Layout 1 | `b82c20ac01be`  |
| 2156   | Layout 1 | `b82c20ac01be`  |
| 2151   | Layout 1 | `b82c20ac01be`  |
| 2147   | Layout 1 | `b82c20ac01be`  |
| 2142   | Layout 1 | `b82c20ac01be`  |
| 2138   | Layout 1 | `b82c20ac01be`  |
| 2134   | Layout 1 | `b82c20ac01be`  |
| 2130   | Layout 1 | `b82c20ac01be`  |
| 2122   | Layout 1 | `b82c20ac01be`  |
| 2107   | Layout 1 | `b82c20ac01be`  |
| 2098   | Layout 1 | `b82c20ac01be`  |
| 2089   | Layout 1 | `b82c20ac01be`  |
| 2081   | Layout 1 | `b82c20ac01be`  |
| 2073   | Layout 1 | `b82c20ac01be`  |
| 2067   | Layout 1 | `b82c20ac01be`  |
| 2063   | Layout 1 | `b82c20ac01be`  |
| 2059   | Layout 1 | `b82c20ac01be`  |
| 2052   | Layout 1 | `b82c20ac01be`  |
| 2044   | Layout 1 | `b82c20ac01be`  |
| 2039   | Layout 1 | `b82c20ac01be`  |
| 2032   | Layout 1 | `b82c20ac01be`  |
| 2025   | Layout 1 | `b82c20ac01be`  |
| 2011   | Layout 1 | `b82c20ac01be`  |
| 2005   | Layout 1 | `b82c20ac01be`  |
| 2000   | Layout 1 | `b82c20ac01be`  |
| 1996   | Layout 1 | `b82c20ac01be`  |
| 1991   | Layout 1 | `b82c20ac01be`  |
| 1985   | Layout 1 | `b82c20ac01be`  |
| 1980   | Layout 1 | `b82c20ac01be`  |
| 1969   | Layout 1 | `b82c20ac01be`  |
| 1964   | Layout 1 | `b82c20ac01be`  |
| 1958   | Layout 1 | `b82c20ac01be`  |
| 1950   | Layout 1 | `b82c20ac01be`  |
| 1945   | Layout 1 | `b82c20ac01be`  |
| 1937   | Layout 1 | `b82c20ac01be`  |
| 1933   | Layout 1 | `b82c20ac01be`  |
| 1927   | Layout 1 | `b82c20ac01be`  |
| 1921   | Layout 1 | `b82c20ac01be`  |
| 1914   | Layout 1 | `b82c20ac01be`  |
| 1908   | Layout 1 | `b82c20ac01be`  |
| 1897   | Layout 1 | `b82c20ac01be`  |
| 1892   | Layout 1 | `b82c20ac01be`  |
| 1886   | Layout 1 | `b82c20ac01be`  |
| 1881   | Layout 1 | `b82c20ac01be`  |
| 1871   | Layout 1 | `b82c20ac01be`  |
| 1866   | Layout 1 | `b82c20ac01be`  |
| 1862   | Layout 1 | `b82c20ac01be`  |
| 1854   | Layout 1 | `b82c20ac01be`  |
| 1846   | Layout 1 | `b82c20ac01be`  |
| 1838   | Layout 1 | `b82c20ac01be`  |
| 1832   | Layout 1 | `b82c20ac01be`  |
| 1826   | Layout 1 | `b82c20ac01be`  |
| 1822   | Layout 1 | `b82c20ac01be`  |
| 1818   | Layout 1 | `b82c20ac01be`  |
| 1804   | Layout 1 | `b82c20ac01be`  |
| 1794   | Layout 1 | `b82c20ac01be`  |
| 1790   | Layout 1 | `b82c20ac01be`  |
| 1784   | Layout 1 | `b82c20ac01be`  |
| 1774   | Layout 1 | `b82c20ac01be`  |
| 1771   | Layout 1 | `b82c20ac01be`  |
| 1762   | Layout 1 | `b82c20ac01be`  |
| 1759   | Layout 1 | `b82c20ac01be`  |
| 1754   | Layout 1 | `b82c20ac01be`  |
| 1749   | Layout 1 | `b82c20ac01be`  |
| 1743   | Layout 1 | `b82c20ac01be`  |
| 1737   | Layout 1 | `b82c20ac01be`  |
| 1731   | Layout 1 | `b82c20ac01be`  |
| 1725   | Layout 1 | `b82c20ac01be`  |
| 1717   | Layout 1 | `b82c20ac01be`  |
| 1710   | Layout 1 | `b82c20ac01be`  |
| 1704   | Layout 1 | `b82c20ac01be`  |
| 1698   | Layout 1 | `b82c20ac01be`  |
| 1690   | Layout 1 | `b82c20ac01be`  |
| 1685   | Layout 1 | `b82c20ac01be`  |
| 1680   | Layout 1 | `b82c20ac01be`  |
| 1674   | Layout 1 | `b82c20ac01be`  |
| 1668   | Layout 1 | `b82c20ac01be`  |
| 1659   | Layout 1 | `b82c20ac01be`  |
| 1649   | Layout 1 | `b82c20ac01be`  |
| 1642   | Layout 1 | `b82c20ac01be`  |
| 1636   | Layout 1 | `b82c20ac01be`  |
| 1628   | Layout 1 | `b82c20ac01be`  |
| 1622   | Layout 1 | `b82c20ac01be`  |
| 1614   | Layout 1 | `b82c20ac01be`  |
| 1608   | Layout 1 | `b82c20ac01be`  |
| 1602   | Layout 1 | `b82c20ac01be`  |
| 1598   | Layout 1 | `b82c20ac01be`  |
| 1594   | Layout 1 | `b82c20ac01be`  |
| 1590   | Layout 1 | `b82c20ac01be`  |
| 1587   | Layout 1 | `b82c20ac01be`  |
| 1584   | Layout 1 | `b82c20ac01be`  |
| 1579   | Layout 1 | `b82c20ac01be`  |
| 1572   | Layout 1 | `b82c20ac01be`  |
| 1565   | Layout 1 | `b82c20ac01be`  |
| 1559   | Layout 1 | `b82c20ac01be`  |
| 1554   | Layout 1 | `b82c20ac01be`  |
| 1547   | Layout 1 | `b82c20ac01be`  |
| 1537   | Layout 1 | `b82c20ac01be`  |
| 1529   | Layout 1 | `b82c20ac01be`  |
| 1524   | Layout 1 | `b82c20ac01be`  |
| 1519   | Layout 1 | `b82c20ac01be`  |
| 1509   | Layout 1 | `b82c20ac01be`  |
| 1506   | Layout 1 | `b82c20ac01be`  |
| 1504   | Layout 1 | `b82c20ac01be`  |
| 1500   | Layout 1 | `b82c20ac01be`  |
| 1493   | Layout 1 | `b82c20ac01be`  |
| 1489   | Layout 1 | `b82c20ac01be`  |
| 1485   | Layout 1 | `b82c20ac01be`  |
| 1481   | Layout 1 | `b82c20ac01be`  |
| 1474   | Layout 1 | `b82c20ac01be`  |
| 1466   | Layout 1 | `b82c20ac01be`  |
| 1462   | Layout 1 | `b82c20ac01be`  |
| 1459   | Layout 1 | `b82c20ac01be`  |
| 1453   | Layout 1 | `b82c20ac01be`  |
| 1450   | Layout 1 | `b82c20ac01be`  |
| 1445   | Layout 1 | `b82c20ac01be`  |
| 1439   | Layout 1 | `b82c20ac01be`  |
| 1433   | Layout 1 | `b82c20ac01be`  |
| 1430   | Layout 1 | `b82c20ac01be`  |
| 1426   | Layout 1 | `b82c20ac01be`  |
| 1421   | Layout 1 | `b82c20ac01be`  |
| 1417   | Layout 1 | `b82c20ac01be`  |
| 1416   | Layout 1 | `b82c20ac01be`  |
| 1409   | Layout 1 | `b82c20ac01be`  |
| 1405   | Layout 1 | `b82c20ac01be`  |
| 1401   | Layout 1 | `b82c20ac01be`  |
| 1396   | Layout 1 | `b82c20ac01be`  |
| 1391   | Layout 1 | `b82c20ac01be`  |
| 1390   | Layout 1 | `b82c20ac01be`  |
| 1386   | Layout 1 | `b82c20ac01be`  |
| 1381   | Layout 1 | `b82c20ac01be`  |
| 1379   | Layout 1 | `b82c20ac01be`  |
| 1372   | Layout 1 | `b82c20ac01be`  |
| 1366   | Layout 1 | `b82c20ac01be`  |
| 1364   | Layout 1 | `b82c20ac01be`  |
| 1363   | Layout 1 | `b82c20ac01be`  |
| 1360   | Layout 1 | `b82c20ac01be`  |
| 1358   | Layout 1 | `b82c20ac01be`  |
| 1355   | Layout 1 | `b82c20ac01be`  |
| 1351   | Layout 1 | `b82c20ac01be`  |
| 1348   | Layout 1 | `b82c20ac01be`  |
| 1346   | Layout 1 | `b82c20ac01be`  |
| 1341   | Layout 1 | `b82c20ac01be`  |
| 1340   | Layout 1 | `b82c20ac01be`  |
| 1338   | Layout 1 | `b82c20ac01be`  |
| 1335   | Layout 1 | `b82c20ac01be`  |
| 1333   | Layout 1 | `b82c20ac01be`  |
| 1329   | Layout 1 | `b82c20ac01be`  |
| 1327   | Layout 1 | `b82c20ac01be`  |
| 1324   | Layout 1 | `b82c20ac01be`  |
| 1321   | Layout 1 | `b82c20ac01be`  |
| 1319   | Layout 1 | `b82c20ac01be`  |
| 1318   | Layout 1 | `b82c20ac01be`  |
| 1316   | Layout 1 | `b82c20ac01be`  |
| 1313   | Layout 1 | `b82c20ac01be`  |
| 1311   | Layout 1 | `b82c20ac01be`  |
| 1309   | Layout 1 | `b82c20ac01be`  |
| 1304   | Layout 1 | `b82c20ac01be`  |
| 1292   | Layout 1 | `b82c20ac01be`  |
| 1286   | Layout 1 | `b82c20ac01be`  |
| 1280   | Layout 1 | `b82c20ac01be`  |
| 1276   | Layout 1 | `b82c20ac01be`  |
| 1267   | Layout 1 | `b82c20ac01be`  |
| 1261   | Layout 1 | `b82c20ac01be`  |
| 1256   | Layout 1 | `b82c20ac01be`  |
| 1250   | Layout 1 | `b82c20ac01be`  |
| 1246   | No file  | `b82c20ac01be`  |
| 1239   | No file  | `b82c20ac01be`  |
| 1230   | No file  | `b82c20ac01be`  |
| 1226   | No file  | `b82c20ac01be`  |
| 1220   | No file  | `b82c20ac01be`  |
| 1217   | No file  | `b82c20ac01be`  |
| 1211   | No file  | `b82c20ac01be`  |
| 1210   | No file  | `b82c20ac01be`  |
| 1208   | No file  | `b82c20ac01be`  |
| 1203   | No file  | `b82c20ac01be`  |
| 1197   | No file  | `b82c20ac01be`  |
| 1194   | No file  | `b82c20ac01be`  |
| 1192   | No file  | `b82c20ac01be`  |
| 1187   | No file  | `b82c20ac01be`  |
| 1183   | No file  | `b82c20ac01be`  |
| 1177   | No file  | `b82c20ac01be`  |
| 1173   | No file  | `b82c20ac01be`  |
| 1167   | No file  | `b82c20ac01be`  |
| 1164   | No file  | `b82c20ac01be`  |
| 1156   | No file  | `b82c20ac01be`  |
| 1149   | No file  | `b82c20ac01be`  |
| 1144   | No file  | `b82c20ac01be`  |
| 1137   | No file  | `b82c20ac01be`  |
| 1132   | No file  | `b82c20ac01be`  |
| 1127   | No file  | `b82c20ac01be`  |
| 1122   | No file  | `b82c20ac01be`  |
| 1118   | No file  | `b82c20ac01be`  |
| 1114   | No file  | `b82c20ac01be`  |
| 1109   | No file  | `b82c20ac01be`  |
| 1102   | No file  | `b82c20ac01be`  |
| 1096   | No file  | `b82c20ac01be`  |
| 1088   | No file  | `b82c20ac01be`  |
| 1081   | No file  | `b82c20ac01be`  |
| 1076   | No file  | `b82c20ac01be`  |
| 1069   | No file  | `b82c20ac01be`  |
| 1064   | No file  | `b82c20ac01be`  |
| 1058   | No file  | `b82c20ac01be`  |
| 1051   | No file  | `b82c20ac01be`  |
| 1044   | No file  | `b82c20ac01be`  |
| 1036   | No file  | `b82c20ac01be`  |
| 1026   | No file  | `b82c20ac01be`  |
| 1016   | No file  | `b82c20ac01be`  |
| 1009   | No file  | `b82c20ac01be`  |
| 1005   | No file  | `b82c20ac01be`  |
| 1000   | No file  | `b82c20ac01be`  |
| 998    | No file  | `b82c20ac01be`  |
| 990    | No file  | `b82c20ac01be`  |
| 979    | No file  | `b82c20ac01be`  |
| 972    | No file  | `b82c20ac01be`  |
| 963    | No file  | `b82c20ac01be`  |
| 955    | No file  | `b82c20ac01be`  |
| 946    | No file  | `b82c20ac01be`  |
| 938    | No file  | `b82c20ac01be`  |
| 927    | No file  | `b82c20ac01be`  |
| 911    | No file  | `b82c20ac01be`  |
| 904    | No file  | `b82c20ac01be`  |
| 899    | No file  | `b82c20ac01be`  |
| 894    | No file  | `b82c20ac01be`  |
| 885    | No file  | `b82c20ac01be`  |
| 879    | No file  | `b82c20ac01be`  |
| 872    | No file  | `b82c20ac01be`  |
| 864    | No file  | `b82c20ac01be`  |
| 855    | No file  | `b82c20ac01be`  |
| 853    | No file  | `b82c20ac01be`  |
| 845    | No file  | `b82c20ac01be`  |
| 837    | No file  | `b82c20ac01be`  |
| 829    | No file  | `b82c20ac01be`  |
| 822    | No file  | `b82c20ac01be`  |
| 814    | No file  | `b82c20ac01be`  |
| 805    | No file  | `b82c20ac01be`  |
| 794    | No file  | `b82c20ac01be`  |
| 787    | No file  | `b82c20ac01be`  |
| 780    | No file  | `b82c20ac01be`  |
| 771    | No file  | `b82c20ac01be`  |
| 760    | No file  | `b82c20ac01be`  |
| 748    | No file  | `b82c20ac01be`  |
| 741    | No file  | `b82c20ac01be`  |
| 736    | No file  | `b82c20ac01be`  |
| 731    | No file  | `b82c20ac01be`  |
| 723    | No file  | `b82c20ac01be`  |
| 711    | No file  | `b82c20ac01be`  |
| 707    | No file  | `b82c20ac01be`  |
| 697    | No file  | `b82c20ac01be`  |
| 689    | No file  | `b82c20ac01be`  |
| 683    | No file  | `b82c20ac01be`  |
| 678    | No file  | `b82c20ac01be`  |
| 670    | No file  | `b82c20ac01be`  |
| 661    | No file  | `b82c20ac01be`  |
| 656    | No file  | `b82c20ac01be`  |
| 652    | No file  | `b82c20ac01be`  |
| 643    | No file  | `b82c20ac01be`  |
| 637    | No file  | `b82c20ac01be`  |
| 630    | No file  | `b82c20ac01be`  |
| 627    | No file  | `b82c20ac01be`  |
| 621    | No file  | `b82c20ac01be`  |
| 617    | No file  | `b82c20ac01be`  |
| 615    | No file  | `b82c20ac01be`  |
| 606    | No file  | `b82c20ac01be`  |
| 599    | No file  | `b82c20ac01be`  |
| 592    | No file  | `b82c20ac01be`  |
| 586    | No file  | `b82c20ac01be`  |
| 577    | No file  | `b82c20ac01be`  |
| 569    | No file  | `b82c20ac01be`  |
| 561    | No file  | `b82c20ac01be`  |
| 554    | No file  | `b82c20ac01be`  |
| 542    | No file  | `b82c20ac01be`  |
| 532    | No file  | `b82c20ac01be`  |
| 531    | No file  | `b82c20ac01be`  |
| 526    | No file  | `b82c20ac01be`  |
| 521    | No file  | `b82c20ac01be`  |
| 517    | No file  | `b82c20ac01be`  |
| 510    | No file  | `b82c20ac01be`  |
| 508    | No file  | `b82c20ac01be`  |
| 504    | No file  | `b82c20ac01be`  |
| 497    | No file  | `b82c20ac01be`  |
| 491    | No file  | `b82c20ac01be`  |
| 485    | No file  | `b82c20ac01be`  |
| 478    | No file  | `b82c20ac01be`  |
| 472    | No file  | `b82c20ac01be`  |
| 466    | No file  | `b82c20ac01be`  |
| 457    | No file  | `b82c20ac01be`  |
| 452    | No file  | `b82c20ac01be`  |
| 449    | No file  | `b82c20ac01be`  |
| 435    | No file  | `b82c20ac01be`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                 | Field        | Notes                                            |
| ------------------- | -------------------- | ------------ | ------------------------------------------------ |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                     |
| `+0x04`             | Entry[..table_start] | entries      | See Entry; entry N is static status type N       |
| `entries+0x00`      | String Table         | string_table | See String Table                                 |
| `EOF-0x08`          | u32                  | table_start  | Offset of the string table, where `entries` ends |
| `EOF-0x04`          | u32                  | zero         | Always `0`                                       |

The entry count is `table_start - 4`.

### Entry (1 byte)

| Offset  | Type | Field | Notes                                                            |
| ------- | ---- | ----- | ---------------------------------------------------------------- |
| `+0x00` | u8   | real  | `1` when the type at this index uses dynamic BSS, `0` when not   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `DynamicBSSOption_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has one row per `Index` (`0` to `106`)
and one 0/1 column per service: `DEV`, `GT_REAL`, `KR_REAL`, `REAL`,
`XB_REAL`, `CS_REAL` and `PS_REAL`. The client 1784 file holds 114 bytes;
byte N equals the `REAL` value of index N on 114 of 114 bytes, with the
seven bytes past index `106` read as `0`. `GT_REAL` and `KR_REAL` hold the
same values as `REAL` on that sheet, `DEV` matches 109 of 114 and the
three console columns 103 of 114, so the byte is named `real` after the
PC service column. The index is not stored; it is the byte's position.

The sheet's `#StaticStatusName` note column (in the server's
`datasheet_dynamicbsstable.xlsm`) names each index: `0` `Item`, `1`
`Character`, `2` `CashProduct`, `3` `Servant`, `4` `Dialog`, `5`
`MentalCard`, `6` `Quest`, ... `106` `ChinaSpawn`. The client 3482 Lua
names three members of the matching enum, `__eDynamicBSSType_Character`,
`__eDynamicBSSType_Dialog` and `__eDynamicBSSType_CashProduct`.

## Notes

- Client 1784 and client 3482 differ at eight indices: client 3482 has
  `0` where client 1784 has `1` at `22` (`SupportPointExperience` on the
  client 1784 sheet), `51` (`FamilySkill`), `97` and `99` to `103`. Its
  bytes `99` to `108` are all `0`.
- On client 1784 the zero bytes below index `104` are `0`, `6`, `16`, `17`,
  `38`, `41`, `44` and `47`; the sheet notes of `41` (`Stat`), `44`
  (`Training`) and `47` (`Tax`) say the work was rolled back because the
  table is close to the server and small in memory.
- The game option `DataOptimize` reads `isUseDynamicBSS()` in the client
  3482 Lua.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/server_tables.py`, with
  each entry's index as the first column.

## Open Questions

### The Type of Each Index on the Live Client

The client 1784 sheet names every index, but client 3482 has 109 bytes
against 114 on client 1784, so types may have been added or removed since.
The Lua uses the enum members by name only, so which index each of them
has on client 3482 is open.
