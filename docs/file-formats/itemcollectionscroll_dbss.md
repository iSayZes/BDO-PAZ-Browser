# `itemcollectionscroll.dbss` Format

## Purpose

The levels of the Item Collection Increase gauge. Item Collection Increase
Scrolls charge time into a family gauge, and the player switches it between
Lv. 0 (off), Lv. 1 and Lv. 2 in the gauge widget
(`panel_widget_hopegaugeonoff_1.luac`). One 16-byte row per level: the
level, the Item Drop Rate and Item Drop Amount bonuses it gives and how fast
it uses the charged time, all three on the 1,000,000 = 100% scale. Lv. 0 has
no row. Companion `itemcollectionscrolloffset.dbss` lists where every row
sits.

| Level | Item Drop Rate | Item Drop Amount | Time use |
| ----- | -------------- | ---------------- | -------- |
| `1`   | 100%           | 50%              | 100%     |
| `2`   | 100%           | 100%             | 200%     |

Values from clients 1784 and 3474. The scroll's TextBind description
(`ItemDropIncrease_Scroll`, LOC type 59, client 3474) gives the same
numbers: Lv. 1 "Item Drop Rate +100%, Item Drop Amount +50%", Lv. 2 "Item
Drop Rate +100%, Item Drop Amount +100%" and "Activating Lv. 2 consumes time
twice as fast".

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------ | --------- |
| 1      | 1445 and later | 3483    | `itemcollectionscroll.dbss`       | 36    | 2 Row        | 16        |
| 1      | 1445 and later | 3483    | `itemcollectionscrolloffset.dbss` | 28    | 2 Offset Row | 12        |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `itemcollectionscroll.dbss`       | 36 B (100.0%) | 0 B (0.0%) |
| 1      | `itemcollectionscrolloffset.dbss` | 28 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `727b196ce1ea`  |
| 3482   | Layout 1             | `727b196ce1ea`  |
| 3474   | Layout 1             | `727b196ce1ea`  |
| 3473   | Layout 1             | `727b196ce1ea`  |
| 3464   | Layout 1             | `727b196ce1ea`  |
| 3458   | Layout 1             | `727b196ce1ea`  |
| 3454   | Layout 1             | `727b196ce1ea`  |
| 3444   | Layout 1             | `727b196ce1ea`  |
| 3435   | Layout 1             | `727b196ce1ea`  |
| 3426   | Layout 1             | `727b196ce1ea`  |
| 3418   | Layout 1             | `727b196ce1ea`  |
| 3412   | Layout 1             | `727b196ce1ea`  |
| 3402   | Layout 1             | `727b196ce1ea`  |
| 3396   | Layout 1             | `727b196ce1ea`  |
| 3387   | Layout 1             | `727b196ce1ea`  |
| 3381   | Layout 1             | `727b196ce1ea`  |
| 3373   | Layout 1             | `727b196ce1ea`  |
| 3364   | Layout 1             | `727b196ce1ea`  |
| 3356   | Layout 1             | `727b196ce1ea`  |
| 3349   | Layout 1             | `727b196ce1ea`  |
| 3342   | Layout 1             | `727b196ce1ea`  |
| 3335   | Layout 1             | `727b196ce1ea`  |
| 3326   | Layout 1             | `727b196ce1ea`  |
| 3321   | Layout 1             | `727b196ce1ea`  |
| 3314   | Layout 1             | `727b196ce1ea`  |
| 3303   | Layout 1             | `727b196ce1ea`  |
| 3302   | Layout 1             | `727b196ce1ea`  |
| 3293   | Layout 1             | `727b196ce1ea`  |
| 3283   | Layout 1             | `727b196ce1ea`  |
| 3275   | Layout 1             | `727b196ce1ea`  |
| 3267   | Layout 1             | `727b196ce1ea`  |
| 3258   | Layout 1             | `727b196ce1ea`  |
| 3251   | Layout 1             | `727b196ce1ea`  |
| 3242   | Layout 1             | `727b196ce1ea`  |
| 3235   | Layout 1             | `727b196ce1ea`  |
| 3229   | Layout 1             | `727b196ce1ea`  |
| 3212   | Layout 1             | `727b196ce1ea`  |
| 3203   | Layout 1             | `727b196ce1ea`  |
| 3193   | Layout 1             | `727b196ce1ea`  |
| 3186   | Layout 1             | `727b196ce1ea`  |
| 3177   | Layout 1             | `727b196ce1ea`  |
| 3169   | Layout 1             | `727b196ce1ea`  |
| 3158   | Layout 1             | `727b196ce1ea`  |
| 3151   | Layout 1             | `727b196ce1ea`  |
| 3144   | Layout 1             | `727b196ce1ea`  |
| 3133   | Layout 1             | `727b196ce1ea`  |
| 3125   | Layout 1             | `727b196ce1ea`  |
| 3118   | Layout 1             | `727b196ce1ea`  |
| 3111   | Layout 1             | `727b196ce1ea`  |
| 3103   | Layout 1             | `727b196ce1ea`  |
| 3095   | Layout 1             | `727b196ce1ea`  |
| 3086   | Layout 1             | `727b196ce1ea`  |
| 3072   | Layout 1             | `727b196ce1ea`  |
| 3062   | Layout 1             | `727b196ce1ea`  |
| 3052   | Layout 1             | `727b196ce1ea`  |
| 3045   | Layout 1             | `727b196ce1ea`  |
| 3037   | Layout 1             | `727b196ce1ea`  |
| 3030   | Layout 1             | `727b196ce1ea`  |
| 3021   | Layout 1             | `727b196ce1ea`  |
| 3012   | Layout 1             | `727b196ce1ea`  |
| 3002   | Layout 1             | `727b196ce1ea`  |
| 2995   | Layout 1             | `727b196ce1ea`  |
| 2987   | Layout 1             | `727b196ce1ea`  |
| 2978   | Layout 1             | `727b196ce1ea`  |
| 2970   | Layout 1             | `727b196ce1ea`  |
| 2959   | Layout 1             | `727b196ce1ea`  |
| 2951   | Layout 1             | `727b196ce1ea`  |
| 2942   | Layout 1             | `727b196ce1ea`  |
| 2935   | Layout 1             | `727b196ce1ea`  |
| 2932   | Layout 1             | `727b196ce1ea`  |
| 2923   | Layout 1             | `727b196ce1ea`  |
| 2919   | Layout 1             | `727b196ce1ea`  |
| 2907   | Layout 1             | `727b196ce1ea`  |
| 2900   | Layout 1             | `727b196ce1ea`  |
| 2891   | Layout 1             | `727b196ce1ea`  |
| 2882   | Layout 1             | `727b196ce1ea`  |
| 2872   | Layout 1             | `727b196ce1ea`  |
| 2863   | Layout 1             | `727b196ce1ea`  |
| 2855   | Layout 1             | `727b196ce1ea`  |
| 2849   | Layout 1             | `727b196ce1ea`  |
| 2844   | Layout 1             | `727b196ce1ea`  |
| 2834   | Layout 1             | `727b196ce1ea`  |
| 2825   | Layout 1             | `727b196ce1ea`  |
| 2819   | Layout 1             | `727b196ce1ea`  |
| 2811   | Layout 1             | `727b196ce1ea`  |
| 2803   | Layout 1             | `727b196ce1ea`  |
| 2794   | Layout 1             | `727b196ce1ea`  |
| 2783   | Layout 1             | `727b196ce1ea`  |
| 2774   | Layout 1             | `727b196ce1ea`  |
| 2765   | Layout 1             | `727b196ce1ea`  |
| 2756   | Layout 1             | `727b196ce1ea`  |
| 2750   | Layout 1             | `727b196ce1ea`  |
| 2743   | Layout 1             | `727b196ce1ea`  |
| 2736   | Layout 1             | `727b196ce1ea`  |
| 2726   | Layout 1             | `727b196ce1ea`  |
| 2717   | Layout 1             | `727b196ce1ea`  |
| 2709   | Layout 1             | `727b196ce1ea`  |
| 2703   | Layout 1             | `727b196ce1ea`  |
| 2695   | Layout 1             | `727b196ce1ea`  |
| 2684   | Layout 1             | `727b196ce1ea`  |
| 2672   | Layout 1             | `727b196ce1ea`  |
| 2665   | Layout 1             | `727b196ce1ea`  |
| 2657   | Layout 1             | `727b196ce1ea`  |
| 2649   | Layout 1             | `727b196ce1ea`  |
| 2644   | Layout 1             | `727b196ce1ea`  |
| 2637   | Layout 1             | `727b196ce1ea`  |
| 2629   | Layout 1             | `727b196ce1ea`  |
| 2619   | Layout 1             | `727b196ce1ea`  |
| 2612   | Layout 1             | `727b196ce1ea`  |
| 2606   | Layout 1             | `727b196ce1ea`  |
| 2602   | Layout 1             | `727b196ce1ea`  |
| 2601   | Layout 1             | `727b196ce1ea`  |
| 2592   | Layout 1             | `727b196ce1ea`  |
| 2583   | Layout 1             | `727b196ce1ea`  |
| 2575   | Layout 1             | `727b196ce1ea`  |
| 2567   | Layout 1             | `727b196ce1ea`  |
| 2560   | Layout 1             | `727b196ce1ea`  |
| 2553   | Layout 1             | `727b196ce1ea`  |
| 2545   | Layout 1             | `727b196ce1ea`  |
| 2538   | Layout 1             | `727b196ce1ea`  |
| 2529   | Layout 1             | `727b196ce1ea`  |
| 2519   | Layout 1             | `727b196ce1ea`  |
| 2513   | Layout 1             | `727b196ce1ea`  |
| 2510   | Layout 1             | `727b196ce1ea`  |
| 2507   | Layout 1             | `727b196ce1ea`  |
| 2503   | Layout 1             | `727b196ce1ea`  |
| 2498   | Layout 1             | `727b196ce1ea`  |
| 2492   | Layout 1             | `727b196ce1ea`  |
| 2487   | Layout 1             | `727b196ce1ea`  |
| 2480   | Layout 1             | `727b196ce1ea`  |
| 2474   | Layout 1             | `727b196ce1ea`  |
| 2468   | Layout 1             | `727b196ce1ea`  |
| 2460   | Layout 1             | `727b196ce1ea`  |
| 2453   | Layout 1             | `727b196ce1ea`  |
| 2444   | Layout 1             | `727b196ce1ea`  |
| 2438   | Layout 1             | `727b196ce1ea`  |
| 2434   | Layout 1             | `727b196ce1ea`  |
| 2429   | Layout 1             | `727b196ce1ea`  |
| 2421   | Layout 1             | `727b196ce1ea`  |
| 2414   | Layout 1             | `727b196ce1ea`  |
| 2407   | Layout 1             | `727b196ce1ea`  |
| 2401   | Layout 1             | `727b196ce1ea`  |
| 2397   | Layout 1             | `727b196ce1ea`  |
| 2393   | Layout 1             | `727b196ce1ea`  |
| 2384   | Layout 1             | `727b196ce1ea`  |
| 2378   | Layout 1             | `727b196ce1ea`  |
| 2372   | Layout 1             | `727b196ce1ea`  |
| 2358   | Layout 1             | `727b196ce1ea`  |
| 2352   | Layout 1             | `727b196ce1ea`  |
| 2347   | Layout 1             | `727b196ce1ea`  |
| 2343   | Layout 1             | `727b196ce1ea`  |
| 2335   | Layout 1             | `727b196ce1ea`  |
| 2327   | Layout 1             | `727b196ce1ea`  |
| 2324   | Layout 1             | `727b196ce1ea`  |
| 2319   | Layout 1             | `727b196ce1ea`  |
| 2313   | Layout 1             | `727b196ce1ea`  |
| 2308   | Layout 1             | `727b196ce1ea`  |
| 2302   | Layout 1             | `727b196ce1ea`  |
| 2295   | Layout 1             | `727b196ce1ea`  |
| 2290   | Layout 1             | `727b196ce1ea`  |
| 2284   | Layout 1             | `727b196ce1ea`  |
| 2276   | Layout 1             | `727b196ce1ea`  |
| 2269   | Layout 1             | `727b196ce1ea`  |
| 2259   | Layout 1             | `727b196ce1ea`  |
| 2250   | Layout 1             | `727b196ce1ea`  |
| 2243   | Layout 1             | `727b196ce1ea`  |
| 2235   | Layout 1             | `727b196ce1ea`  |
| 2229   | Layout 1             | `727b196ce1ea`  |
| 2224   | Layout 1             | `727b196ce1ea`  |
| 2218   | Layout 1             | `727b196ce1ea`  |
| 2215   | Layout 1             | `727b196ce1ea`  |
| 2207   | Layout 1             | `727b196ce1ea`  |
| 2203   | Layout 1             | `727b196ce1ea`  |
| 2196   | Layout 1             | `727b196ce1ea`  |
| 2192   | Layout 1             | `727b196ce1ea`  |
| 2189   | Layout 1             | `727b196ce1ea`  |
| 2183   | Layout 1             | `727b196ce1ea`  |
| 2179   | Layout 1             | `727b196ce1ea`  |
| 2171   | Layout 1             | `727b196ce1ea`  |
| 2163   | Layout 1             | `727b196ce1ea`  |
| 2156   | Layout 1             | `727b196ce1ea`  |
| 2151   | Layout 1             | `727b196ce1ea`  |
| 2147   | Layout 1             | `727b196ce1ea`  |
| 2142   | Layout 1             | `727b196ce1ea`  |
| 2138   | Layout 1             | `727b196ce1ea`  |
| 2134   | Layout 1             | `727b196ce1ea`  |
| 2130   | Layout 1             | `727b196ce1ea`  |
| 2122   | Layout 1             | `727b196ce1ea`  |
| 2107   | Layout 1             | `727b196ce1ea`  |
| 2098   | Layout 1             | `727b196ce1ea`  |
| 2089   | Layout 1             | `727b196ce1ea`  |
| 2081   | Layout 1             | `727b196ce1ea`  |
| 2073   | Layout 1             | `727b196ce1ea`  |
| 2067   | Layout 1             | `727b196ce1ea`  |
| 2063   | Layout 1             | `727b196ce1ea`  |
| 2059   | Layout 1             | `727b196ce1ea`  |
| 2052   | Layout 1             | `727b196ce1ea`  |
| 2044   | Layout 1             | `727b196ce1ea`  |
| 2039   | Layout 1             | `727b196ce1ea`  |
| 2032   | Layout 1             | `727b196ce1ea`  |
| 2025   | Layout 1             | `727b196ce1ea`  |
| 2011   | Layout 1             | `727b196ce1ea`  |
| 2005   | Layout 1             | `727b196ce1ea`  |
| 2000   | Layout 1             | `727b196ce1ea`  |
| 1996   | Layout 1             | `727b196ce1ea`  |
| 1991   | Layout 1             | `727b196ce1ea`  |
| 1985   | Layout 1             | `727b196ce1ea`  |
| 1980   | Layout 1             | `727b196ce1ea`  |
| 1969   | Layout 1             | `727b196ce1ea`  |
| 1964   | Layout 1             | `727b196ce1ea`  |
| 1958   | Layout 1             | `727b196ce1ea`  |
| 1950   | Layout 1             | `727b196ce1ea`  |
| 1945   | Layout 1             | `727b196ce1ea`  |
| 1937   | Layout 1             | `727b196ce1ea`  |
| 1933   | Layout 1             | `727b196ce1ea`  |
| 1927   | Layout 1             | `727b196ce1ea`  |
| 1921   | Layout 1             | `727b196ce1ea`  |
| 1914   | Layout 1             | `727b196ce1ea`  |
| 1908   | Layout 1             | `727b196ce1ea`  |
| 1897   | Layout 1             | `727b196ce1ea`  |
| 1892   | Layout 1             | `727b196ce1ea`  |
| 1886   | Layout 1             | `727b196ce1ea`  |
| 1881   | Layout 1             | `727b196ce1ea`  |
| 1871   | Layout 1             | `727b196ce1ea`  |
| 1866   | Layout 1             | `727b196ce1ea`  |
| 1862   | Layout 1             | `727b196ce1ea`  |
| 1854   | Layout 1             | `727b196ce1ea`  |
| 1846   | Layout 1             | `727b196ce1ea`  |
| 1838   | Layout 1             | `727b196ce1ea`  |
| 1832   | Layout 1             | `727b196ce1ea`  |
| 1826   | Layout 1             | `727b196ce1ea`  |
| 1822   | Layout 1             | `727b196ce1ea`  |
| 1818   | Layout 1             | `727b196ce1ea`  |
| 1804   | Layout 1             | `727b196ce1ea`  |
| 1794   | Layout 1             | `727b196ce1ea`  |
| 1790   | Layout 1             | `727b196ce1ea`  |
| 1784   | Layout 1             | `727b196ce1ea`  |
| 1774   | Layout 1             | `727b196ce1ea`  |
| 1771   | Layout 1             | `727b196ce1ea`  |
| 1762   | Layout 1             | `727b196ce1ea`  |
| 1759   | Layout 1             | `727b196ce1ea`  |
| 1754   | Layout 1             | `727b196ce1ea`  |
| 1749   | Layout 1             | `727b196ce1ea`  |
| 1743   | Layout 1             | `727b196ce1ea`  |
| 1737   | Layout 1             | `727b196ce1ea`  |
| 1731   | Layout 1             | `727b196ce1ea`  |
| 1725   | Layout 1             | `727b196ce1ea`  |
| 1717   | Layout 1             | `727b196ce1ea`  |
| 1710   | Layout 1             | `727b196ce1ea`  |
| 1704   | Layout 1             | `727b196ce1ea`  |
| 1698   | Layout 1             | `727b196ce1ea`  |
| 1690   | Layout 1             | `727b196ce1ea`  |
| 1685   | Layout 1             | `727b196ce1ea`  |
| 1680   | Layout 1             | `727b196ce1ea`  |
| 1674   | Layout 1             | `727b196ce1ea`  |
| 1668   | Layout 1             | `727b196ce1ea`  |
| 1659   | Layout 1             | `727b196ce1ea`  |
| 1649   | Layout 1             | `727b196ce1ea`  |
| 1642   | Layout 1             | `727b196ce1ea`  |
| 1636   | Layout 1             | `727b196ce1ea`  |
| 1628   | Layout 1             | `727b196ce1ea`  |
| 1622   | Layout 1             | `727b196ce1ea`  |
| 1614   | Layout 1             | `727b196ce1ea`  |
| 1608   | Layout 1             | `727b196ce1ea`  |
| 1602   | Layout 1             | `727b196ce1ea`  |
| 1598   | Layout 1             | `727b196ce1ea`  |
| 1594   | Layout 1             | `727b196ce1ea`  |
| 1590   | Layout 1             | `727b196ce1ea`  |
| 1587   | Layout 1             | `727b196ce1ea`  |
| 1584   | Layout 1             | `727b196ce1ea`  |
| 1579   | Layout 1             | `727b196ce1ea`  |
| 1572   | Layout 1             | `727b196ce1ea`  |
| 1565   | Layout 1             | `727b196ce1ea`  |
| 1559   | Layout 1             | `727b196ce1ea`  |
| 1554   | Layout 1             | `727b196ce1ea`  |
| 1547   | Layout 1             | `727b196ce1ea`  |
| 1537   | Layout 1             | `727b196ce1ea`  |
| 1529   | Layout 1             | `727b196ce1ea`  |
| 1524   | Layout 1             | `727b196ce1ea`  |
| 1519   | Layout 1             | `727b196ce1ea`  |
| 1509   | Layout 1             | `727b196ce1ea`  |
| 1506   | Layout 1             | `727b196ce1ea`  |
| 1504   | Layout 1             | `727b196ce1ea`  |
| 1500   | Layout 1             | `727b196ce1ea`  |
| 1493   | Layout 1             | `727b196ce1ea`  |
| 1489   | Layout 1             | `727b196ce1ea`  |
| 1485   | Layout 1             | `727b196ce1ea`  |
| 1481   | Layout 1             | `727b196ce1ea`  |
| 1474   | Layout 1             | `727b196ce1ea`  |
| 1466   | Layout 1             | `727b196ce1ea`  |
| 1462   | Layout 1             | `727b196ce1ea`  |
| 1459   | Layout 1             | `727b196ce1ea`  |
| 1453   | Layout 1             | `727b196ce1ea`  |
| 1450   | Layout 1             | `727b196ce1ea`  |
| 1445   | Layout 1             | `727b196ce1ea`  |
| 1439   | No documented layout | `727b196ce1ea`  |
| 1433   | No file              | `727b196ce1ea`  |
| 1430   | No file              | `727b196ce1ea`  |
| 1426   | No file              | `727b196ce1ea`  |
| 1421   | No file              | `727b196ce1ea`  |
| 1417   | No file              | `727b196ce1ea`  |
| 1416   | No file              | `727b196ce1ea`  |
| 1409   | No file              | `727b196ce1ea`  |
| 1405   | No file              | `727b196ce1ea`  |
| 1401   | No file              | `727b196ce1ea`  |
| 1396   | No file              | `727b196ce1ea`  |
| 1391   | No file              | `727b196ce1ea`  |
| 1390   | No file              | `727b196ce1ea`  |
| 1386   | No file              | `727b196ce1ea`  |
| 1381   | No file              | `727b196ce1ea`  |
| 1379   | No file              | `727b196ce1ea`  |
| 1372   | No file              | `727b196ce1ea`  |
| 1366   | No file              | `727b196ce1ea`  |
| 1364   | No file              | `727b196ce1ea`  |
| 1363   | No file              | `727b196ce1ea`  |
| 1360   | No file              | `727b196ce1ea`  |
| 1358   | No file              | `727b196ce1ea`  |
| 1355   | No file              | `727b196ce1ea`  |
| 1351   | No file              | `727b196ce1ea`  |
| 1348   | No file              | `727b196ce1ea`  |
| 1346   | No file              | `727b196ce1ea`  |
| 1341   | No file              | `727b196ce1ea`  |
| 1340   | No file              | `727b196ce1ea`  |
| 1338   | No file              | `727b196ce1ea`  |
| 1335   | No file              | `727b196ce1ea`  |
| 1333   | No file              | `727b196ce1ea`  |
| 1329   | No file              | `727b196ce1ea`  |
| 1327   | No file              | `727b196ce1ea`  |
| 1324   | No file              | `727b196ce1ea`  |
| 1321   | No file              | `727b196ce1ea`  |
| 1319   | No file              | `727b196ce1ea`  |
| 1318   | No file              | `727b196ce1ea`  |
| 1316   | No file              | `727b196ce1ea`  |
| 1313   | No file              | `727b196ce1ea`  |
| 1311   | No file              | `727b196ce1ea`  |
| 1309   | No file              | `727b196ce1ea`  |
| 1304   | No file              | `727b196ce1ea`  |
| 1292   | No file              | `727b196ce1ea`  |
| 1286   | No file              | `727b196ce1ea`  |
| 1280   | No file              | `727b196ce1ea`  |
| 1276   | No file              | `727b196ce1ea`  |
| 1267   | No file              | `727b196ce1ea`  |
| 1261   | No file              | `727b196ce1ea`  |
| 1256   | No file              | `727b196ce1ea`  |
| 1250   | No file              | `727b196ce1ea`  |
| 1246   | No file              | `727b196ce1ea`  |
| 1239   | No file              | `727b196ce1ea`  |
| 1230   | No file              | `727b196ce1ea`  |
| 1226   | No file              | `727b196ce1ea`  |
| 1220   | No file              | `727b196ce1ea`  |
| 1217   | No file              | `727b196ce1ea`  |
| 1211   | No file              | `727b196ce1ea`  |
| 1210   | No file              | `727b196ce1ea`  |
| 1208   | No file              | `727b196ce1ea`  |
| 1203   | No file              | `727b196ce1ea`  |
| 1197   | No file              | `727b196ce1ea`  |
| 1194   | No file              | `727b196ce1ea`  |
| 1192   | No file              | `727b196ce1ea`  |
| 1187   | No file              | `727b196ce1ea`  |
| 1183   | No file              | `727b196ce1ea`  |
| 1177   | No file              | `727b196ce1ea`  |
| 1173   | No file              | `727b196ce1ea`  |
| 1167   | No file              | `727b196ce1ea`  |
| 1164   | No file              | `727b196ce1ea`  |
| 1156   | No file              | `727b196ce1ea`  |
| 1149   | No file              | `727b196ce1ea`  |
| 1144   | No file              | `727b196ce1ea`  |
| 1137   | No file              | `727b196ce1ea`  |
| 1132   | No file              | `727b196ce1ea`  |
| 1127   | No file              | `727b196ce1ea`  |
| 1122   | No file              | `727b196ce1ea`  |
| 1118   | No file              | `727b196ce1ea`  |
| 1114   | No file              | `727b196ce1ea`  |
| 1109   | No file              | `727b196ce1ea`  |
| 1102   | No file              | `727b196ce1ea`  |
| 1096   | No file              | `727b196ce1ea`  |
| 1088   | No file              | `727b196ce1ea`  |
| 1081   | No file              | `727b196ce1ea`  |
| 1076   | No file              | `727b196ce1ea`  |
| 1069   | No file              | `727b196ce1ea`  |
| 1064   | No file              | `727b196ce1ea`  |
| 1058   | No file              | `727b196ce1ea`  |
| 1051   | No file              | `727b196ce1ea`  |
| 1044   | No file              | `727b196ce1ea`  |
| 1036   | No file              | `727b196ce1ea`  |
| 1026   | No file              | `727b196ce1ea`  |
| 1016   | No file              | `727b196ce1ea`  |
| 1009   | No file              | `727b196ce1ea`  |
| 1005   | No file              | `727b196ce1ea`  |
| 1000   | No file              | `727b196ce1ea`  |
| 998    | No file              | `727b196ce1ea`  |
| 990    | No file              | `727b196ce1ea`  |
| 979    | No file              | `727b196ce1ea`  |
| 972    | No file              | `727b196ce1ea`  |
| 963    | No file              | `727b196ce1ea`  |
| 955    | No file              | `727b196ce1ea`  |
| 946    | No file              | `727b196ce1ea`  |
| 938    | No file              | `727b196ce1ea`  |
| 927    | No file              | `727b196ce1ea`  |
| 911    | No file              | `727b196ce1ea`  |
| 904    | No file              | `727b196ce1ea`  |
| 899    | No file              | `727b196ce1ea`  |
| 894    | No file              | `727b196ce1ea`  |
| 885    | No file              | `727b196ce1ea`  |
| 879    | No file              | `727b196ce1ea`  |
| 872    | No file              | `727b196ce1ea`  |
| 864    | No file              | `727b196ce1ea`  |
| 855    | No file              | `727b196ce1ea`  |
| 853    | No file              | `727b196ce1ea`  |
| 845    | No file              | `727b196ce1ea`  |
| 837    | No file              | `727b196ce1ea`  |
| 829    | No file              | `727b196ce1ea`  |
| 822    | No file              | `727b196ce1ea`  |
| 814    | No file              | `727b196ce1ea`  |
| 805    | No file              | `727b196ce1ea`  |
| 794    | No file              | `727b196ce1ea`  |
| 787    | No file              | `727b196ce1ea`  |
| 780    | No file              | `727b196ce1ea`  |
| 771    | No file              | `727b196ce1ea`  |
| 760    | No file              | `727b196ce1ea`  |
| 748    | No file              | `727b196ce1ea`  |
| 741    | No file              | `727b196ce1ea`  |
| 736    | No file              | `727b196ce1ea`  |
| 731    | No file              | `727b196ce1ea`  |
| 723    | No file              | `727b196ce1ea`  |
| 711    | No file              | `727b196ce1ea`  |
| 707    | No file              | `727b196ce1ea`  |
| 697    | No file              | `727b196ce1ea`  |
| 689    | No file              | `727b196ce1ea`  |
| 683    | No file              | `727b196ce1ea`  |
| 678    | No file              | `727b196ce1ea`  |
| 670    | No file              | `727b196ce1ea`  |
| 661    | No file              | `727b196ce1ea`  |
| 656    | No file              | `727b196ce1ea`  |
| 652    | No file              | `727b196ce1ea`  |
| 643    | No file              | `727b196ce1ea`  |
| 637    | No file              | `727b196ce1ea`  |
| 630    | No file              | `727b196ce1ea`  |
| 627    | No file              | `727b196ce1ea`  |
| 621    | No file              | `727b196ce1ea`  |
| 617    | No file              | `727b196ce1ea`  |
| 615    | No file              | `727b196ce1ea`  |
| 606    | No file              | `727b196ce1ea`  |
| 599    | No file              | `727b196ce1ea`  |
| 592    | No file              | `727b196ce1ea`  |
| 586    | No file              | `727b196ce1ea`  |
| 577    | No file              | `727b196ce1ea`  |
| 569    | No file              | `727b196ce1ea`  |
| 561    | No file              | `727b196ce1ea`  |
| 554    | No file              | `727b196ce1ea`  |
| 542    | No file              | `727b196ce1ea`  |
| 532    | No file              | `727b196ce1ea`  |
| 531    | No file              | `727b196ce1ea`  |
| 526    | No file              | `727b196ce1ea`  |
| 521    | No file              | `727b196ce1ea`  |
| 517    | No file              | `727b196ce1ea`  |
| 510    | No file              | `727b196ce1ea`  |
| 508    | No file              | `727b196ce1ea`  |
| 504    | No file              | `727b196ce1ea`  |
| 497    | No file              | `727b196ce1ea`  |
| 491    | No file              | `727b196ce1ea`  |
| 485    | No file              | `727b196ce1ea`  |
| 478    | No file              | `727b196ce1ea`  |
| 472    | No file              | `727b196ce1ea`  |
| 466    | No file              | `727b196ce1ea`  |
| 457    | No file              | `727b196ce1ea`  |
| 452    | No file              | `727b196ce1ea`  |
| 449    | No file              | `727b196ce1ea`  |
| 435    | No file              | `727b196ce1ea`  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                 |
| --------------------------------- | -------- | -------------------------------------------------------------------- |
| `itemcollectionscrolloffset.dbss` | Optional | `grade -> (data_offset, data_size)` of every row; the rows are fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                              |
| ------- | ---------- | ----- | ---------------------------------- |
| `+0x00` | u32        | count | Number of rows; `2` on client 3474 |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (16 bytes)

| Offset  | Type | Field        | Notes                                                                 |
| ------- | ---- | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32  | grade        | Gauge level, `1` or `2`; unique per row, the index key                |
| `+0x04` | i32  | drop_rate    | Item Drop Rate bonus, 1,000,000 = 100%                                |
| `+0x08` | i32  | count_rate   | Item Drop Amount bonus, 1,000,000 = 100%                              |
| `+0x0C` | i32  | cost_percent | Charged time used per real second, 1,000,000 = 1 second (100%)        |

### `itemcollectionscrolloffset.dbss`

| Offset  | Type              | Field | Notes                                        |
| ------- | ----------------- | ----- | -------------------------------------------- |
| `+0x00` | u32               | count | Equals the `itemcollectionscroll.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row         |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                               |
| ------- | ---- | ----------- | ----------------------------------- |
| `+0x00` | u32  | grade       | Key of the row it points at         |
| `+0x04` | u32  | data_offset | Start of the row, at its `grade`    |
| `+0x08` | u32  | data_size   | `16`, the whole row                 |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. On
clients 1784 and 3474 the index lists level `2` first and level `1` second,
in the order of the main file, and every index row points at the row with
its key.

## Field Names

The names are the columns of the `ItemDropIncrease_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784: `Index`, `CoutRate` (sic),
`DropRate`, `CostPercent` and `SkillNo`. Its two rows, (`1`, `500000`,
`1000000`, `1000000`, `52597`) and (`2`, `1000000`, `1000000`, `2000000`,
`52598`), match the file on 2 of 2 keys on clients 1784 and 3474, and the
values place each column: only `CoutRate` holds `500000` and only
`CostPercent` holds `2000000`. The 1784 and 3474 files are byte for byte the
same.

The client 1784 server dump of the same private server loads the sheet in
`GameCommonParameterLoaderFromExcel::loadMain(loadItemCollectionScroll)`
into `ItemCollectionScrollBuffManager`. The loader reads `Index`, `CoutRate`,
`DropRate` and `CostPercent` as ints, stores them as `Index`, `DropRate`,
`CoutRate`, `CostPercent` (the order of this file) and logs a bad row as
`%#:grade(%#) : ErrNo(%#)`. It does not read `SkillNo`, which is not in
the file. `Index` is named `grade` here after that message and the client
Lua, which reads the level with `getItemCollectionScrollGrade()` and the two
bonuses with `ToClient_GetHopeDropByGrade(grade)` and
`ToClient_GetHopeCountByGrade(grade)`. The 2016 PDB has no item collection
struct.

## Notes

- The level `2` tooltip `LUA_HOPEGAUGE_TOOLTIP_DESC2` (client 3474) says
  "Consumes double Level 1 time", and `LUA_HOPE_GRADE_ON2` says "Consumes 2
  sec of charged time per 1 real sec", which is `cost_percent` `2000000`.
- The sheet's `SkillNo` values are skills of client 3474's `skill.dbss`:
  `52597` Item Collection Increase Function Rework (buffs `52349` and
  `52350`) and `52598` Item Collection Increase Function Rework Advanced
  (buffs `52351` and `52352`). In [`buff.dbss`](buff_dbss.md) `52349` and
  `52351` are effect type `57` (Item Drop Rate) with `param_1` `1000000`,
  `52350` and `52352` effect type `112` (Item Drop Amount) with `param_1`
  `500000` and `1000000`: the `drop_rate` and `count_rate` of levels 1 and 2.
- The gauge cap and the 5-minute change cooldown are not in this file. The
  client 1784 bexcel holds them in the `EtcOption` sheet
  (`ItemDropIncreasePointLimit`, `ItemDropIncreaseCoolTime`,
  `ItemDropIncreaseWarning`); the Lua reads them with
  `ToClient_ItemCollectionPointLimit()`, `ToClient_getItemCollectionScrollCoolTime()`
  and `ToClient_getHopeGaugeAlert()`.
- `LUA_HOPE_CHARGE_INFO` (client 3474) lists what each scroll charges:
  1,800 seconds for the 30-minute scroll, 3,600 for the 60-minute scroll and
  7,200 for the Advanced scroll, up to 10 hours. The charge per scroll is
  the item's `getContentsEventParam1()` in `panel_widget_hopegauge_1.luac`,
  not a field of this file.
