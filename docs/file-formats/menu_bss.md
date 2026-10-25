# `menu.bss` Format

## Purpose

The categories of the main menu (Esc menu): one fixed 40-byte row per category
with its hotkey, its title as a UI string key and its icon as a region of a
shared sprite sheet. The entries of each category are in
[`submenu.bss`](submenu_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File       | Bytes | Records         | Row bytes |
| ------ | -------------- | ---------- | ----- | --------------- | --------- |
| 1      | 1466 and later | `menu.bss` | 1,083 | 12 Category Row | 40        |

| Layout | File       | Known            | Unknown    |
| ------ | ---------- | ---------------- | ---------- |
| 1      | `menu.bss` | 1,083 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a03086672fc0`  |
| 3482   | Layout 1 | `a03086672fc0`  |
| 3474   | Layout 1 | `a03086672fc0`  |
| 3473   | Layout 1 | `a03086672fc0`  |
| 3464   | Layout 1 | `a03086672fc0`  |
| 3458   | Layout 1 | `a03086672fc0`  |
| 3454   | Layout 1 | `a03086672fc0`  |
| 3444   | Layout 1 | `a03086672fc0`  |
| 3435   | Layout 1 | `a03086672fc0`  |
| 3426   | Layout 1 | `a03086672fc0`  |
| 3418   | Layout 1 | `a03086672fc0`  |
| 3412   | Layout 1 | `a03086672fc0`  |
| 3402   | Layout 1 | `a03086672fc0`  |
| 3396   | Layout 1 | `a03086672fc0`  |
| 3387   | Layout 1 | `a03086672fc0`  |
| 3381   | Layout 1 | `a03086672fc0`  |
| 3373   | Layout 1 | `a03086672fc0`  |
| 3364   | Layout 1 | `a03086672fc0`  |
| 3356   | Layout 1 | `a03086672fc0`  |
| 3349   | Layout 1 | `a03086672fc0`  |
| 3342   | Layout 1 | `a03086672fc0`  |
| 3335   | Layout 1 | `a03086672fc0`  |
| 3326   | Layout 1 | `a03086672fc0`  |
| 3321   | Layout 1 | `a03086672fc0`  |
| 3314   | Layout 1 | `a03086672fc0`  |
| 3303   | Layout 1 | `a03086672fc0`  |
| 3302   | Layout 1 | `a03086672fc0`  |
| 3293   | Layout 1 | `a03086672fc0`  |
| 3283   | Layout 1 | `a03086672fc0`  |
| 3275   | Layout 1 | `a03086672fc0`  |
| 3267   | Layout 1 | `a03086672fc0`  |
| 3258   | Layout 1 | `a03086672fc0`  |
| 3251   | Layout 1 | `a03086672fc0`  |
| 3242   | Layout 1 | `a03086672fc0`  |
| 3235   | Layout 1 | `a03086672fc0`  |
| 3229   | Layout 1 | `a03086672fc0`  |
| 3212   | Layout 1 | `a03086672fc0`  |
| 3203   | Layout 1 | `a03086672fc0`  |
| 3193   | Layout 1 | `a03086672fc0`  |
| 3186   | Layout 1 | `a03086672fc0`  |
| 3177   | Layout 1 | `a03086672fc0`  |
| 3169   | Layout 1 | `a03086672fc0`  |
| 3158   | Layout 1 | `a03086672fc0`  |
| 3151   | Layout 1 | `a03086672fc0`  |
| 3144   | Layout 1 | `a03086672fc0`  |
| 3133   | Layout 1 | `a03086672fc0`  |
| 3125   | Layout 1 | `a03086672fc0`  |
| 3118   | Layout 1 | `a03086672fc0`  |
| 3111   | Layout 1 | `a03086672fc0`  |
| 3103   | Layout 1 | `a03086672fc0`  |
| 3095   | Layout 1 | `a03086672fc0`  |
| 3086   | Layout 1 | `a03086672fc0`  |
| 3072   | Layout 1 | `a03086672fc0`  |
| 3062   | Layout 1 | `a03086672fc0`  |
| 3052   | Layout 1 | `a03086672fc0`  |
| 3045   | Layout 1 | `a03086672fc0`  |
| 3037   | Layout 1 | `a03086672fc0`  |
| 3030   | Layout 1 | `a03086672fc0`  |
| 3021   | Layout 1 | `a03086672fc0`  |
| 3012   | Layout 1 | `a03086672fc0`  |
| 3002   | Layout 1 | `a03086672fc0`  |
| 2995   | Layout 1 | `a03086672fc0`  |
| 2987   | Layout 1 | `a03086672fc0`  |
| 2978   | Layout 1 | `a03086672fc0`  |
| 2970   | Layout 1 | `a03086672fc0`  |
| 2959   | Layout 1 | `a03086672fc0`  |
| 2951   | Layout 1 | `a03086672fc0`  |
| 2942   | Layout 1 | `a03086672fc0`  |
| 2935   | Layout 1 | `a03086672fc0`  |
| 2932   | Layout 1 | `a03086672fc0`  |
| 2923   | Layout 1 | `a03086672fc0`  |
| 2919   | Layout 1 | `a03086672fc0`  |
| 2907   | Layout 1 | `a03086672fc0`  |
| 2900   | Layout 1 | `a03086672fc0`  |
| 2891   | Layout 1 | `a03086672fc0`  |
| 2882   | Layout 1 | `a03086672fc0`  |
| 2872   | Layout 1 | `a03086672fc0`  |
| 2863   | Layout 1 | `a03086672fc0`  |
| 2855   | Layout 1 | `a03086672fc0`  |
| 2849   | Layout 1 | `a03086672fc0`  |
| 2844   | Layout 1 | `a03086672fc0`  |
| 2834   | Layout 1 | `a03086672fc0`  |
| 2825   | Layout 1 | `a03086672fc0`  |
| 2819   | Layout 1 | `a03086672fc0`  |
| 2811   | Layout 1 | `a03086672fc0`  |
| 2803   | Layout 1 | `a03086672fc0`  |
| 2794   | Layout 1 | `a03086672fc0`  |
| 2783   | Layout 1 | `a03086672fc0`  |
| 2774   | Layout 1 | `a03086672fc0`  |
| 2765   | Layout 1 | `a03086672fc0`  |
| 2756   | Layout 1 | `a03086672fc0`  |
| 2750   | Layout 1 | `a03086672fc0`  |
| 2743   | Layout 1 | `a03086672fc0`  |
| 2736   | Layout 1 | `a03086672fc0`  |
| 2726   | Layout 1 | `a03086672fc0`  |
| 2717   | Layout 1 | `a03086672fc0`  |
| 2709   | Layout 1 | `a03086672fc0`  |
| 2703   | Layout 1 | `a03086672fc0`  |
| 2695   | Layout 1 | `a03086672fc0`  |
| 2684   | Layout 1 | `a03086672fc0`  |
| 2672   | Layout 1 | `a03086672fc0`  |
| 2665   | Layout 1 | `a03086672fc0`  |
| 2657   | Layout 1 | `a03086672fc0`  |
| 2649   | Layout 1 | `a03086672fc0`  |
| 2644   | Layout 1 | `a03086672fc0`  |
| 2637   | Layout 1 | `a03086672fc0`  |
| 2629   | Layout 1 | `a03086672fc0`  |
| 2619   | Layout 1 | `a03086672fc0`  |
| 2612   | Layout 1 | `a03086672fc0`  |
| 2606   | Layout 1 | `a03086672fc0`  |
| 2602   | Layout 1 | `a03086672fc0`  |
| 2601   | Layout 1 | `a03086672fc0`  |
| 2592   | Layout 1 | `a03086672fc0`  |
| 2583   | Layout 1 | `a03086672fc0`  |
| 2575   | Layout 1 | `a03086672fc0`  |
| 2567   | Layout 1 | `a03086672fc0`  |
| 2560   | Layout 1 | `a03086672fc0`  |
| 2553   | Layout 1 | `a03086672fc0`  |
| 2545   | Layout 1 | `a03086672fc0`  |
| 2538   | Layout 1 | `a03086672fc0`  |
| 2529   | Layout 1 | `a03086672fc0`  |
| 2519   | Layout 1 | `a03086672fc0`  |
| 2513   | Layout 1 | `a03086672fc0`  |
| 2510   | Layout 1 | `a03086672fc0`  |
| 2507   | Layout 1 | `a03086672fc0`  |
| 2503   | Layout 1 | `a03086672fc0`  |
| 2498   | Layout 1 | `a03086672fc0`  |
| 2492   | Layout 1 | `a03086672fc0`  |
| 2487   | Layout 1 | `a03086672fc0`  |
| 2480   | Layout 1 | `a03086672fc0`  |
| 2474   | Layout 1 | `a03086672fc0`  |
| 2468   | Layout 1 | `a03086672fc0`  |
| 2460   | Layout 1 | `a03086672fc0`  |
| 2453   | Layout 1 | `a03086672fc0`  |
| 2444   | Layout 1 | `a03086672fc0`  |
| 2438   | Layout 1 | `a03086672fc0`  |
| 2434   | Layout 1 | `a03086672fc0`  |
| 2429   | Layout 1 | `a03086672fc0`  |
| 2421   | Layout 1 | `a03086672fc0`  |
| 2414   | Layout 1 | `a03086672fc0`  |
| 2407   | Layout 1 | `a03086672fc0`  |
| 2401   | Layout 1 | `a03086672fc0`  |
| 2397   | Layout 1 | `a03086672fc0`  |
| 2393   | Layout 1 | `a03086672fc0`  |
| 2384   | Layout 1 | `a03086672fc0`  |
| 2378   | Layout 1 | `a03086672fc0`  |
| 2372   | Layout 1 | `a03086672fc0`  |
| 2358   | Layout 1 | `a03086672fc0`  |
| 2352   | Layout 1 | `a03086672fc0`  |
| 2347   | Layout 1 | `a03086672fc0`  |
| 2343   | Layout 1 | `a03086672fc0`  |
| 2335   | Layout 1 | `a03086672fc0`  |
| 2327   | Layout 1 | `a03086672fc0`  |
| 2324   | Layout 1 | `a03086672fc0`  |
| 2319   | Layout 1 | `a03086672fc0`  |
| 2313   | Layout 1 | `a03086672fc0`  |
| 2308   | Layout 1 | `a03086672fc0`  |
| 2302   | Layout 1 | `a03086672fc0`  |
| 2295   | Layout 1 | `a03086672fc0`  |
| 2290   | Layout 1 | `a03086672fc0`  |
| 2284   | Layout 1 | `a03086672fc0`  |
| 2276   | Layout 1 | `a03086672fc0`  |
| 2269   | Layout 1 | `a03086672fc0`  |
| 2259   | Layout 1 | `a03086672fc0`  |
| 2250   | Layout 1 | `a03086672fc0`  |
| 2243   | Layout 1 | `a03086672fc0`  |
| 2235   | Layout 1 | `a03086672fc0`  |
| 2229   | Layout 1 | `a03086672fc0`  |
| 2224   | Layout 1 | `a03086672fc0`  |
| 2218   | Layout 1 | `a03086672fc0`  |
| 2215   | Layout 1 | `a03086672fc0`  |
| 2207   | Layout 1 | `a03086672fc0`  |
| 2203   | Layout 1 | `a03086672fc0`  |
| 2196   | Layout 1 | `a03086672fc0`  |
| 2192   | Layout 1 | `a03086672fc0`  |
| 2189   | Layout 1 | `a03086672fc0`  |
| 2183   | Layout 1 | `a03086672fc0`  |
| 2179   | Layout 1 | `a03086672fc0`  |
| 2171   | Layout 1 | `a03086672fc0`  |
| 2163   | Layout 1 | `a03086672fc0`  |
| 2156   | Layout 1 | `a03086672fc0`  |
| 2151   | Layout 1 | `a03086672fc0`  |
| 2147   | Layout 1 | `a03086672fc0`  |
| 2142   | Layout 1 | `a03086672fc0`  |
| 2138   | Layout 1 | `a03086672fc0`  |
| 2134   | Layout 1 | `a03086672fc0`  |
| 2130   | Layout 1 | `a03086672fc0`  |
| 2122   | Layout 1 | `a03086672fc0`  |
| 2107   | Layout 1 | `a03086672fc0`  |
| 2098   | Layout 1 | `a03086672fc0`  |
| 2089   | Layout 1 | `a03086672fc0`  |
| 2081   | Layout 1 | `a03086672fc0`  |
| 2073   | Layout 1 | `a03086672fc0`  |
| 2067   | Layout 1 | `a03086672fc0`  |
| 2063   | Layout 1 | `a03086672fc0`  |
| 2059   | Layout 1 | `a03086672fc0`  |
| 2052   | Layout 1 | `a03086672fc0`  |
| 2044   | Layout 1 | `a03086672fc0`  |
| 2039   | Layout 1 | `a03086672fc0`  |
| 2032   | Layout 1 | `a03086672fc0`  |
| 2025   | Layout 1 | `a03086672fc0`  |
| 2011   | Layout 1 | `a03086672fc0`  |
| 2005   | Layout 1 | `a03086672fc0`  |
| 2000   | Layout 1 | `a03086672fc0`  |
| 1996   | Layout 1 | `a03086672fc0`  |
| 1991   | Layout 1 | `a03086672fc0`  |
| 1985   | Layout 1 | `a03086672fc0`  |
| 1980   | Layout 1 | `a03086672fc0`  |
| 1969   | Layout 1 | `a03086672fc0`  |
| 1964   | Layout 1 | `a03086672fc0`  |
| 1958   | Layout 1 | `a03086672fc0`  |
| 1950   | Layout 1 | `a03086672fc0`  |
| 1945   | Layout 1 | `a03086672fc0`  |
| 1937   | Layout 1 | `a03086672fc0`  |
| 1933   | Layout 1 | `a03086672fc0`  |
| 1927   | Layout 1 | `a03086672fc0`  |
| 1921   | Layout 1 | `a03086672fc0`  |
| 1914   | Layout 1 | `a03086672fc0`  |
| 1908   | Layout 1 | `a03086672fc0`  |
| 1897   | Layout 1 | `a03086672fc0`  |
| 1892   | Layout 1 | `a03086672fc0`  |
| 1886   | Layout 1 | `a03086672fc0`  |
| 1881   | Layout 1 | `a03086672fc0`  |
| 1871   | Layout 1 | `a03086672fc0`  |
| 1866   | Layout 1 | `a03086672fc0`  |
| 1862   | Layout 1 | `a03086672fc0`  |
| 1854   | Layout 1 | `a03086672fc0`  |
| 1846   | Layout 1 | `a03086672fc0`  |
| 1838   | Layout 1 | `a03086672fc0`  |
| 1832   | Layout 1 | `a03086672fc0`  |
| 1826   | Layout 1 | `a03086672fc0`  |
| 1822   | Layout 1 | `a03086672fc0`  |
| 1818   | Layout 1 | `a03086672fc0`  |
| 1804   | Layout 1 | `a03086672fc0`  |
| 1794   | Layout 1 | `a03086672fc0`  |
| 1790   | Layout 1 | `a03086672fc0`  |
| 1784   | Layout 1 | `a03086672fc0`  |
| 1774   | Layout 1 | `a03086672fc0`  |
| 1771   | Layout 1 | `a03086672fc0`  |
| 1762   | Layout 1 | `a03086672fc0`  |
| 1759   | Layout 1 | `a03086672fc0`  |
| 1754   | Layout 1 | `a03086672fc0`  |
| 1749   | Layout 1 | `a03086672fc0`  |
| 1743   | Layout 1 | `a03086672fc0`  |
| 1737   | Layout 1 | `a03086672fc0`  |
| 1731   | Layout 1 | `a03086672fc0`  |
| 1725   | Layout 1 | `a03086672fc0`  |
| 1717   | Layout 1 | `a03086672fc0`  |
| 1710   | Layout 1 | `a03086672fc0`  |
| 1704   | Layout 1 | `a03086672fc0`  |
| 1698   | Layout 1 | `a03086672fc0`  |
| 1690   | Layout 1 | `a03086672fc0`  |
| 1685   | Layout 1 | `a03086672fc0`  |
| 1680   | Layout 1 | `a03086672fc0`  |
| 1674   | Layout 1 | `a03086672fc0`  |
| 1668   | Layout 1 | `a03086672fc0`  |
| 1659   | Layout 1 | `a03086672fc0`  |
| 1649   | Layout 1 | `a03086672fc0`  |
| 1642   | Layout 1 | `a03086672fc0`  |
| 1636   | Layout 1 | `a03086672fc0`  |
| 1628   | Layout 1 | `a03086672fc0`  |
| 1622   | Layout 1 | `a03086672fc0`  |
| 1614   | Layout 1 | `a03086672fc0`  |
| 1608   | Layout 1 | `a03086672fc0`  |
| 1602   | Layout 1 | `a03086672fc0`  |
| 1598   | Layout 1 | `a03086672fc0`  |
| 1594   | Layout 1 | `a03086672fc0`  |
| 1590   | Layout 1 | `a03086672fc0`  |
| 1587   | Layout 1 | `a03086672fc0`  |
| 1584   | Layout 1 | `a03086672fc0`  |
| 1579   | Layout 1 | `a03086672fc0`  |
| 1572   | Layout 1 | `a03086672fc0`  |
| 1565   | Layout 1 | `a03086672fc0`  |
| 1559   | Layout 1 | `a03086672fc0`  |
| 1554   | Layout 1 | `a03086672fc0`  |
| 1547   | Layout 1 | `a03086672fc0`  |
| 1537   | Layout 1 | `a03086672fc0`  |
| 1529   | Layout 1 | `a03086672fc0`  |
| 1524   | Layout 1 | `a03086672fc0`  |
| 1519   | Layout 1 | `a03086672fc0`  |
| 1509   | Layout 1 | `a03086672fc0`  |
| 1506   | Layout 1 | `a03086672fc0`  |
| 1504   | Layout 1 | `a03086672fc0`  |
| 1500   | Layout 1 | `a03086672fc0`  |
| 1493   | Layout 1 | `a03086672fc0`  |
| 1489   | Layout 1 | `a03086672fc0`  |
| 1485   | Layout 1 | `a03086672fc0`  |
| 1481   | Layout 1 | `a03086672fc0`  |
| 1474   | Layout 1 | `a03086672fc0`  |
| 1466   | Layout 1 | `a03086672fc0`  |
| 1462   | No file  | `a03086672fc0`  |
| 1459   | No file  | `a03086672fc0`  |
| 1453   | No file  | `a03086672fc0`  |
| 1450   | No file  | `a03086672fc0`  |
| 1445   | No file  | `a03086672fc0`  |
| 1439   | No file  | `a03086672fc0`  |
| 1433   | No file  | `a03086672fc0`  |
| 1430   | No file  | `a03086672fc0`  |
| 1426   | No file  | `a03086672fc0`  |
| 1421   | No file  | `a03086672fc0`  |
| 1417   | No file  | `a03086672fc0`  |
| 1416   | No file  | `a03086672fc0`  |
| 1409   | No file  | `a03086672fc0`  |
| 1405   | No file  | `a03086672fc0`  |
| 1401   | No file  | `a03086672fc0`  |
| 1396   | No file  | `a03086672fc0`  |
| 1391   | No file  | `a03086672fc0`  |
| 1390   | No file  | `a03086672fc0`  |
| 1386   | No file  | `a03086672fc0`  |
| 1381   | No file  | `a03086672fc0`  |
| 1379   | No file  | `a03086672fc0`  |
| 1372   | No file  | `a03086672fc0`  |
| 1366   | No file  | `a03086672fc0`  |
| 1364   | No file  | `a03086672fc0`  |
| 1363   | No file  | `a03086672fc0`  |
| 1360   | No file  | `a03086672fc0`  |
| 1358   | No file  | `a03086672fc0`  |
| 1355   | No file  | `a03086672fc0`  |
| 1351   | No file  | `a03086672fc0`  |
| 1348   | No file  | `a03086672fc0`  |
| 1346   | No file  | `a03086672fc0`  |
| 1341   | No file  | `a03086672fc0`  |
| 1340   | No file  | `a03086672fc0`  |
| 1338   | No file  | `a03086672fc0`  |
| 1335   | No file  | `a03086672fc0`  |
| 1333   | No file  | `a03086672fc0`  |
| 1329   | No file  | `a03086672fc0`  |
| 1327   | No file  | `a03086672fc0`  |
| 1324   | No file  | `a03086672fc0`  |
| 1321   | No file  | `a03086672fc0`  |
| 1319   | No file  | `a03086672fc0`  |
| 1318   | No file  | `a03086672fc0`  |
| 1316   | No file  | `a03086672fc0`  |
| 1313   | No file  | `a03086672fc0`  |
| 1311   | No file  | `a03086672fc0`  |
| 1309   | No file  | `a03086672fc0`  |
| 1304   | No file  | `a03086672fc0`  |
| 1292   | No file  | `a03086672fc0`  |
| 1286   | No file  | `a03086672fc0`  |
| 1280   | No file  | `a03086672fc0`  |
| 1276   | No file  | `a03086672fc0`  |
| 1267   | No file  | `a03086672fc0`  |
| 1261   | No file  | `a03086672fc0`  |
| 1256   | No file  | `a03086672fc0`  |
| 1250   | No file  | `a03086672fc0`  |
| 1246   | No file  | `a03086672fc0`  |
| 1239   | No file  | `a03086672fc0`  |
| 1230   | No file  | `a03086672fc0`  |
| 1226   | No file  | `a03086672fc0`  |
| 1220   | No file  | `a03086672fc0`  |
| 1217   | No file  | `a03086672fc0`  |
| 1211   | No file  | `a03086672fc0`  |
| 1210   | No file  | `a03086672fc0`  |
| 1208   | No file  | `a03086672fc0`  |
| 1203   | No file  | `a03086672fc0`  |
| 1197   | No file  | `a03086672fc0`  |
| 1194   | No file  | `a03086672fc0`  |
| 1192   | No file  | `a03086672fc0`  |
| 1187   | No file  | `a03086672fc0`  |
| 1183   | No file  | `a03086672fc0`  |
| 1177   | No file  | `a03086672fc0`  |
| 1173   | No file  | `a03086672fc0`  |
| 1167   | No file  | `a03086672fc0`  |
| 1164   | No file  | `a03086672fc0`  |
| 1156   | No file  | `a03086672fc0`  |
| 1149   | No file  | `a03086672fc0`  |
| 1144   | No file  | `a03086672fc0`  |
| 1137   | No file  | `a03086672fc0`  |
| 1132   | No file  | `a03086672fc0`  |
| 1127   | No file  | `a03086672fc0`  |
| 1122   | No file  | `a03086672fc0`  |
| 1118   | No file  | `a03086672fc0`  |
| 1114   | No file  | `a03086672fc0`  |
| 1109   | No file  | `a03086672fc0`  |
| 1102   | No file  | `a03086672fc0`  |
| 1096   | No file  | `a03086672fc0`  |
| 1088   | No file  | `a03086672fc0`  |
| 1081   | No file  | `a03086672fc0`  |
| 1076   | No file  | `a03086672fc0`  |
| 1069   | No file  | `a03086672fc0`  |
| 1064   | No file  | `a03086672fc0`  |
| 1058   | No file  | `a03086672fc0`  |
| 1051   | No file  | `a03086672fc0`  |
| 1044   | No file  | `a03086672fc0`  |
| 1036   | No file  | `a03086672fc0`  |
| 1026   | No file  | `a03086672fc0`  |
| 1016   | No file  | `a03086672fc0`  |
| 1009   | No file  | `a03086672fc0`  |
| 1005   | No file  | `a03086672fc0`  |
| 1000   | No file  | `a03086672fc0`  |
| 998    | No file  | `a03086672fc0`  |
| 990    | No file  | `a03086672fc0`  |
| 979    | No file  | `a03086672fc0`  |
| 972    | No file  | `a03086672fc0`  |
| 963    | No file  | `a03086672fc0`  |
| 955    | No file  | `a03086672fc0`  |
| 946    | No file  | `a03086672fc0`  |
| 938    | No file  | `a03086672fc0`  |
| 927    | No file  | `a03086672fc0`  |
| 911    | No file  | `a03086672fc0`  |
| 904    | No file  | `a03086672fc0`  |
| 899    | No file  | `a03086672fc0`  |
| 894    | No file  | `a03086672fc0`  |
| 885    | No file  | `a03086672fc0`  |
| 879    | No file  | `a03086672fc0`  |
| 872    | No file  | `a03086672fc0`  |
| 864    | No file  | `a03086672fc0`  |
| 855    | No file  | `a03086672fc0`  |
| 853    | No file  | `a03086672fc0`  |
| 845    | No file  | `a03086672fc0`  |
| 837    | No file  | `a03086672fc0`  |
| 829    | No file  | `a03086672fc0`  |
| 822    | No file  | `a03086672fc0`  |
| 814    | No file  | `a03086672fc0`  |
| 805    | No file  | `a03086672fc0`  |
| 794    | No file  | `a03086672fc0`  |
| 787    | No file  | `a03086672fc0`  |
| 780    | No file  | `a03086672fc0`  |
| 771    | No file  | `a03086672fc0`  |
| 760    | No file  | `a03086672fc0`  |
| 748    | No file  | `a03086672fc0`  |
| 741    | No file  | `a03086672fc0`  |
| 736    | No file  | `a03086672fc0`  |
| 731    | No file  | `a03086672fc0`  |
| 723    | No file  | `a03086672fc0`  |
| 711    | No file  | `a03086672fc0`  |
| 707    | No file  | `a03086672fc0`  |
| 697    | No file  | `a03086672fc0`  |
| 689    | No file  | `a03086672fc0`  |
| 683    | No file  | `a03086672fc0`  |
| 678    | No file  | `a03086672fc0`  |
| 670    | No file  | `a03086672fc0`  |
| 661    | No file  | `a03086672fc0`  |
| 656    | No file  | `a03086672fc0`  |
| 652    | No file  | `a03086672fc0`  |
| 643    | No file  | `a03086672fc0`  |
| 637    | No file  | `a03086672fc0`  |
| 630    | No file  | `a03086672fc0`  |
| 627    | No file  | `a03086672fc0`  |
| 621    | No file  | `a03086672fc0`  |
| 617    | No file  | `a03086672fc0`  |
| 615    | No file  | `a03086672fc0`  |
| 606    | No file  | `a03086672fc0`  |
| 599    | No file  | `a03086672fc0`  |
| 592    | No file  | `a03086672fc0`  |
| 586    | No file  | `a03086672fc0`  |
| 577    | No file  | `a03086672fc0`  |
| 569    | No file  | `a03086672fc0`  |
| 561    | No file  | `a03086672fc0`  |
| 554    | No file  | `a03086672fc0`  |
| 542    | No file  | `a03086672fc0`  |
| 532    | No file  | `a03086672fc0`  |
| 531    | No file  | `a03086672fc0`  |
| 526    | No file  | `a03086672fc0`  |
| 521    | No file  | `a03086672fc0`  |
| 517    | No file  | `a03086672fc0`  |
| 510    | No file  | `a03086672fc0`  |
| 508    | No file  | `a03086672fc0`  |
| 504    | No file  | `a03086672fc0`  |
| 497    | No file  | `a03086672fc0`  |
| 491    | No file  | `a03086672fc0`  |
| 485    | No file  | `a03086672fc0`  |
| 478    | No file  | `a03086672fc0`  |
| 472    | No file  | `a03086672fc0`  |
| 466    | No file  | `a03086672fc0`  |
| 457    | No file  | `a03086672fc0`  |
| 452    | No file  | `a03086672fc0`  |
| 449    | No file  | `a03086672fc0`  |
| 435    | No file  | `a03086672fc0`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                     |
| --------------------- | -------- | ------------------------------------------------------------------------ |
| `stringtable.bss`     | Optional | Hash of the title key in its sheet, for the LOC lookup                   |
| `languagedata_en.loc` | Optional | Title text, LOC type 37 (`str_id1` = key hash, `str_id2` = sheet)        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset              | Type                | Field        | Notes                                          |
| ------------------- | ------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]             | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                 | count        | Number of rows; 12 on client 3458              |
| `+0x08`             | Category Row[count] | rows         | See Category Row                               |
| `rows+0x00`         | String Table        | string_table | See String Table                               |
| `string_table+0x00` | u32                 | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                 | zero         | Always 0                                       |

### Category Row (40 bytes)

| Offset  | Type | Field         | Notes                                                                  |
| ------- | ---- | ------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | menu_id       | 1 to 12, in row order; `submenu.bss` entries name it                   |
| `+0x04` | u32  | icon_x1       | Left edge of the icon region in the sheet, in pixels                   |
| `+0x08` | u32  | icon_y1       | Top edge                                                               |
| `+0x0C` | u32  | icon_x2       | Right edge; every region is 55 x 55 on client 3458                     |
| `+0x10` | u32  | icon_y2       | Bottom edge                                                            |
| `+0x14` | u32  | icon_ref      | String table index of the sprite sheet, relative to `ui_texture/`      |
| `+0x18` | u32  | hotkey_ref    | String table index of the hotkey label (`F1` to `F12`), UTF-16         |
| `+0x1C` | u32  | sheet_ref     | String table index of the title key's sheet (`GAME`)                   |
| `+0x20` | u32  | key_ref       | String table index of the title key (`LUA_MENU_REMAKE_CATEGORY_1`)     |
| `+0x24` | u32  | submenu_count | Number of entries in the category's `submenu.bss` group                |

### String Table (variable: 4 bytes + strings)

27 strings on client 3458: the two sprite sheets
`Combine/Icon/Combine_Title_Icon_00.dds` and `_01.dds`, the twelve hotkeys,
`GAME` and the twelve title keys.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 27 on client 3458   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Notes

- On client 3458 the categories are Recently Used (F12, no entries: the
  client fills it), Information, Character, Reward, Shop, Adventure, Life,
  War, Function, Community, Settings and Adventurer Support (F11). The title
  keys are not in row order: F3 Reward is `LUA_MENU_REMAKE_CATEGORY_5`.
- `submenu_count` equals the entry count of the matching `submenu.bss` group
  in every row.
- The icons are 55 x 55 regions of two 1.5 MB, 632 x 632 sprite sheets, both
  shipped under `ui_texture/combine/icon/`. The table shows a sprite
  placeholder; a click opens the sprite and its place on the sheet.
- The app indexes the icons by menu ID as a sprite kind: `IndexKind.MENU_ICON`
  holds the sheet path and `IndexKind.MENU_ICON_REGION` the
  `(x1, y1, x2, y2)` region, read through `icon_path()` and `icon_region()`
  with `IconKind.MENU`.
