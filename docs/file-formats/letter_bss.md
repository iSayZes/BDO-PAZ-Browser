# `letter.bss` Format

## Purpose

The letter window an item opens: one row per letter item with the
`RESOURCE` string sheet key of the letter text, the background texture and
whether the text is centered. The letter Lua
(`panel_window_letterscroll_all_1.luac`) reads a row through
`getItemLetterStaticStatus(ItemEnchantKey(itemkey))` and the getters
`getItemLetterMainDescStringKey()`, `getItemLetterTexturePath()` and
`isItemLetterCenterAlignment()`, and shows the text with
`PAGetString(Defines.StringSheet_RESOURCE, key)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File         | Bytes | Records | Row bytes |
| ------ | -------------- | ------------ | ----- | ------- | --------- |
| 2      | 1504 and later | `letter.bss` | 5,408 | 53 Row  | 13        |
| 1      | 1524 to 1685   | `letter.bss` | 1,651 | 13 Row  | 12        |

| Layout | File         | Known            | Unknown    |
| ------ | ------------ | ---------------- | ---------- |
| 2      | `letter.bss` | 5,408 B (100.0%) | 0 B (0.0%) |
| 1      | `letter.bss` | 1,651 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `2fee90e21355`  |
| 3482   | Layout 2 | `2fee90e21355`  |
| 3474   | Layout 2 | `2fee90e21355`  |
| 3473   | Layout 2 | `2fee90e21355`  |
| 3464   | Layout 2 | `2fee90e21355`  |
| 3458   | Layout 2 | `2fee90e21355`  |
| 3454   | Layout 2 | `2fee90e21355`  |
| 3444   | Layout 2 | `2fee90e21355`  |
| 3435   | Layout 2 | `2fee90e21355`  |
| 3426   | Layout 2 | `2fee90e21355`  |
| 3418   | Layout 2 | `2fee90e21355`  |
| 3412   | Layout 2 | `2fee90e21355`  |
| 3402   | Layout 2 | `2fee90e21355`  |
| 3396   | Layout 2 | `2fee90e21355`  |
| 3387   | Layout 2 | `2fee90e21355`  |
| 3381   | Layout 2 | `2fee90e21355`  |
| 3373   | Layout 2 | `2fee90e21355`  |
| 3364   | Layout 2 | `2fee90e21355`  |
| 3356   | Layout 2 | `2fee90e21355`  |
| 3349   | Layout 2 | `2fee90e21355`  |
| 3342   | Layout 2 | `2fee90e21355`  |
| 3335   | Layout 2 | `2fee90e21355`  |
| 3326   | Layout 2 | `2fee90e21355`  |
| 3321   | Layout 2 | `2fee90e21355`  |
| 3314   | Layout 2 | `2fee90e21355`  |
| 3303   | Layout 2 | `2fee90e21355`  |
| 3302   | Layout 2 | `2fee90e21355`  |
| 3293   | Layout 2 | `2fee90e21355`  |
| 3283   | Layout 2 | `2fee90e21355`  |
| 3275   | Layout 2 | `2fee90e21355`  |
| 3267   | Layout 2 | `2fee90e21355`  |
| 3258   | Layout 2 | `2fee90e21355`  |
| 3251   | Layout 2 | `2fee90e21355`  |
| 3242   | Layout 2 | `2fee90e21355`  |
| 3235   | Layout 2 | `2fee90e21355`  |
| 3229   | Layout 2 | `2fee90e21355`  |
| 3212   | Layout 2 | `2fee90e21355`  |
| 3203   | Layout 2 | `2fee90e21355`  |
| 3193   | Layout 2 | `2fee90e21355`  |
| 3186   | Layout 2 | `2fee90e21355`  |
| 3177   | Layout 2 | `2fee90e21355`  |
| 3169   | Layout 2 | `2fee90e21355`  |
| 3158   | Layout 2 | `2fee90e21355`  |
| 3151   | Layout 2 | `2fee90e21355`  |
| 3144   | Layout 2 | `2fee90e21355`  |
| 3133   | Layout 2 | `2fee90e21355`  |
| 3125   | Layout 2 | `2fee90e21355`  |
| 3118   | Layout 2 | `2fee90e21355`  |
| 3111   | Layout 2 | `2fee90e21355`  |
| 3103   | Layout 2 | `2fee90e21355`  |
| 3095   | Layout 2 | `2fee90e21355`  |
| 3086   | Layout 2 | `2fee90e21355`  |
| 3072   | Layout 2 | `2fee90e21355`  |
| 3062   | Layout 2 | `2fee90e21355`  |
| 3052   | Layout 2 | `2fee90e21355`  |
| 3045   | Layout 2 | `2fee90e21355`  |
| 3037   | Layout 2 | `2fee90e21355`  |
| 3030   | Layout 2 | `2fee90e21355`  |
| 3021   | Layout 2 | `2fee90e21355`  |
| 3012   | Layout 2 | `2fee90e21355`  |
| 3002   | Layout 2 | `2fee90e21355`  |
| 2995   | Layout 2 | `2fee90e21355`  |
| 2987   | Layout 2 | `2fee90e21355`  |
| 2978   | Layout 2 | `2fee90e21355`  |
| 2970   | Layout 2 | `2fee90e21355`  |
| 2959   | Layout 2 | `2fee90e21355`  |
| 2951   | Layout 2 | `2fee90e21355`  |
| 2942   | Layout 2 | `2fee90e21355`  |
| 2935   | Layout 2 | `2fee90e21355`  |
| 2932   | Layout 2 | `2fee90e21355`  |
| 2923   | Layout 2 | `2fee90e21355`  |
| 2919   | Layout 2 | `2fee90e21355`  |
| 2907   | Layout 2 | `2fee90e21355`  |
| 2900   | Layout 2 | `2fee90e21355`  |
| 2891   | Layout 2 | `2fee90e21355`  |
| 2882   | Layout 2 | `2fee90e21355`  |
| 2872   | Layout 2 | `2fee90e21355`  |
| 2863   | Layout 2 | `2fee90e21355`  |
| 2855   | Layout 2 | `2fee90e21355`  |
| 2849   | Layout 2 | `2fee90e21355`  |
| 2844   | Layout 2 | `2fee90e21355`  |
| 2834   | Layout 2 | `2fee90e21355`  |
| 2825   | Layout 2 | `2fee90e21355`  |
| 2819   | Layout 2 | `2fee90e21355`  |
| 2811   | Layout 2 | `2fee90e21355`  |
| 2803   | Layout 2 | `2fee90e21355`  |
| 2794   | Layout 2 | `2fee90e21355`  |
| 2783   | Layout 2 | `2fee90e21355`  |
| 2774   | Layout 2 | `2fee90e21355`  |
| 2765   | Layout 2 | `2fee90e21355`  |
| 2756   | Layout 2 | `2fee90e21355`  |
| 2750   | Layout 2 | `2fee90e21355`  |
| 2743   | Layout 2 | `2fee90e21355`  |
| 2736   | Layout 2 | `2fee90e21355`  |
| 2726   | Layout 2 | `2fee90e21355`  |
| 2717   | Layout 2 | `2fee90e21355`  |
| 2709   | Layout 2 | `2fee90e21355`  |
| 2703   | Layout 2 | `2fee90e21355`  |
| 2695   | Layout 2 | `2fee90e21355`  |
| 2684   | Layout 2 | `2fee90e21355`  |
| 2672   | Layout 2 | `2fee90e21355`  |
| 2665   | Layout 2 | `2fee90e21355`  |
| 2657   | Layout 2 | `2fee90e21355`  |
| 2649   | Layout 2 | `2fee90e21355`  |
| 2644   | Layout 2 | `2fee90e21355`  |
| 2637   | Layout 2 | `2fee90e21355`  |
| 2629   | Layout 2 | `2fee90e21355`  |
| 2619   | Layout 2 | `2fee90e21355`  |
| 2612   | Layout 2 | `2fee90e21355`  |
| 2606   | Layout 2 | `2fee90e21355`  |
| 2602   | Layout 2 | `2fee90e21355`  |
| 2601   | Layout 2 | `2fee90e21355`  |
| 2592   | Layout 2 | `2fee90e21355`  |
| 2583   | Layout 2 | `2fee90e21355`  |
| 2575   | Layout 2 | `2fee90e21355`  |
| 2567   | Layout 2 | `2fee90e21355`  |
| 2560   | Layout 2 | `2fee90e21355`  |
| 2553   | Layout 2 | `2fee90e21355`  |
| 2545   | Layout 2 | `2fee90e21355`  |
| 2538   | Layout 2 | `2fee90e21355`  |
| 2529   | Layout 2 | `2fee90e21355`  |
| 2519   | Layout 2 | `2fee90e21355`  |
| 2513   | Layout 2 | `2fee90e21355`  |
| 2510   | Layout 2 | `2fee90e21355`  |
| 2507   | Layout 2 | `2fee90e21355`  |
| 2503   | Layout 2 | `2fee90e21355`  |
| 2498   | Layout 2 | `2fee90e21355`  |
| 2492   | Layout 2 | `2fee90e21355`  |
| 2487   | Layout 2 | `2fee90e21355`  |
| 2480   | Layout 2 | `2fee90e21355`  |
| 2474   | Layout 2 | `2fee90e21355`  |
| 2468   | Layout 2 | `2fee90e21355`  |
| 2460   | Layout 2 | `2fee90e21355`  |
| 2453   | Layout 2 | `2fee90e21355`  |
| 2444   | Layout 2 | `2fee90e21355`  |
| 2438   | Layout 2 | `2fee90e21355`  |
| 2434   | Layout 2 | `2fee90e21355`  |
| 2429   | Layout 2 | `2fee90e21355`  |
| 2421   | Layout 2 | `2fee90e21355`  |
| 2414   | Layout 2 | `2fee90e21355`  |
| 2407   | Layout 2 | `2fee90e21355`  |
| 2401   | Layout 2 | `2fee90e21355`  |
| 2397   | Layout 2 | `2fee90e21355`  |
| 2393   | Layout 2 | `2fee90e21355`  |
| 2384   | Layout 2 | `2fee90e21355`  |
| 2378   | Layout 2 | `2fee90e21355`  |
| 2372   | Layout 2 | `2fee90e21355`  |
| 2358   | Layout 2 | `2fee90e21355`  |
| 2352   | Layout 2 | `2fee90e21355`  |
| 2347   | Layout 2 | `2fee90e21355`  |
| 2343   | Layout 2 | `2fee90e21355`  |
| 2335   | Layout 2 | `2fee90e21355`  |
| 2327   | Layout 2 | `2fee90e21355`  |
| 2324   | Layout 2 | `2fee90e21355`  |
| 2319   | Layout 2 | `2fee90e21355`  |
| 2313   | Layout 2 | `2fee90e21355`  |
| 2308   | Layout 2 | `2fee90e21355`  |
| 2302   | Layout 2 | `2fee90e21355`  |
| 2295   | Layout 2 | `2fee90e21355`  |
| 2290   | Layout 2 | `2fee90e21355`  |
| 2284   | Layout 2 | `2fee90e21355`  |
| 2276   | Layout 2 | `2fee90e21355`  |
| 2269   | Layout 2 | `2fee90e21355`  |
| 2259   | Layout 2 | `2fee90e21355`  |
| 2250   | Layout 2 | `2fee90e21355`  |
| 2243   | Layout 2 | `2fee90e21355`  |
| 2235   | Layout 2 | `2fee90e21355`  |
| 2229   | Layout 2 | `2fee90e21355`  |
| 2224   | Layout 2 | `2fee90e21355`  |
| 2218   | Layout 2 | `2fee90e21355`  |
| 2215   | Layout 2 | `2fee90e21355`  |
| 2207   | Layout 2 | `2fee90e21355`  |
| 2203   | Layout 2 | `2fee90e21355`  |
| 2196   | Layout 2 | `2fee90e21355`  |
| 2192   | Layout 2 | `2fee90e21355`  |
| 2189   | Layout 2 | `2fee90e21355`  |
| 2183   | Layout 2 | `2fee90e21355`  |
| 2179   | Layout 2 | `2fee90e21355`  |
| 2171   | Layout 2 | `2fee90e21355`  |
| 2163   | Layout 2 | `2fee90e21355`  |
| 2156   | Layout 2 | `2fee90e21355`  |
| 2151   | Layout 2 | `2fee90e21355`  |
| 2147   | Layout 2 | `2fee90e21355`  |
| 2142   | Layout 2 | `2fee90e21355`  |
| 2138   | Layout 2 | `2fee90e21355`  |
| 2134   | Layout 2 | `2fee90e21355`  |
| 2130   | Layout 2 | `2fee90e21355`  |
| 2122   | Layout 2 | `2fee90e21355`  |
| 2107   | Layout 2 | `2fee90e21355`  |
| 2098   | Layout 2 | `2fee90e21355`  |
| 2089   | Layout 2 | `2fee90e21355`  |
| 2081   | Layout 2 | `2fee90e21355`  |
| 2073   | Layout 2 | `2fee90e21355`  |
| 2067   | Layout 2 | `2fee90e21355`  |
| 2063   | Layout 2 | `2fee90e21355`  |
| 2059   | Layout 2 | `2fee90e21355`  |
| 2052   | Layout 2 | `2fee90e21355`  |
| 2044   | Layout 2 | `2fee90e21355`  |
| 2039   | Layout 2 | `2fee90e21355`  |
| 2032   | Layout 2 | `2fee90e21355`  |
| 2025   | Layout 2 | `2fee90e21355`  |
| 2011   | Layout 2 | `2fee90e21355`  |
| 2005   | Layout 2 | `2fee90e21355`  |
| 2000   | Layout 2 | `2fee90e21355`  |
| 1996   | Layout 2 | `2fee90e21355`  |
| 1991   | Layout 2 | `2fee90e21355`  |
| 1985   | Layout 2 | `2fee90e21355`  |
| 1980   | Layout 2 | `2fee90e21355`  |
| 1969   | Layout 2 | `2fee90e21355`  |
| 1964   | Layout 2 | `2fee90e21355`  |
| 1958   | Layout 2 | `2fee90e21355`  |
| 1950   | Layout 2 | `2fee90e21355`  |
| 1945   | Layout 2 | `2fee90e21355`  |
| 1937   | Layout 2 | `2fee90e21355`  |
| 1933   | Layout 2 | `2fee90e21355`  |
| 1927   | Layout 2 | `2fee90e21355`  |
| 1921   | Layout 2 | `2fee90e21355`  |
| 1914   | Layout 2 | `2fee90e21355`  |
| 1908   | Layout 2 | `2fee90e21355`  |
| 1897   | Layout 2 | `2fee90e21355`  |
| 1892   | Layout 2 | `2fee90e21355`  |
| 1886   | Layout 2 | `2fee90e21355`  |
| 1881   | Layout 2 | `2fee90e21355`  |
| 1871   | Layout 2 | `2fee90e21355`  |
| 1866   | Layout 2 | `2fee90e21355`  |
| 1862   | Layout 2 | `2fee90e21355`  |
| 1854   | Layout 2 | `2fee90e21355`  |
| 1846   | Layout 2 | `2fee90e21355`  |
| 1838   | Layout 2 | `2fee90e21355`  |
| 1832   | Layout 2 | `2fee90e21355`  |
| 1826   | Layout 2 | `2fee90e21355`  |
| 1822   | Layout 2 | `2fee90e21355`  |
| 1818   | Layout 2 | `2fee90e21355`  |
| 1804   | Layout 2 | `2fee90e21355`  |
| 1794   | Layout 2 | `2fee90e21355`  |
| 1790   | Layout 2 | `2fee90e21355`  |
| 1784   | Layout 2 | `2fee90e21355`  |
| 1774   | Layout 2 | `2fee90e21355`  |
| 1771   | Layout 2 | `2fee90e21355`  |
| 1762   | Layout 2 | `2fee90e21355`  |
| 1759   | Layout 2 | `2fee90e21355`  |
| 1754   | Layout 2 | `2fee90e21355`  |
| 1749   | Layout 2 | `2fee90e21355`  |
| 1743   | Layout 2 | `2fee90e21355`  |
| 1737   | Layout 2 | `2fee90e21355`  |
| 1731   | Layout 2 | `2fee90e21355`  |
| 1725   | Layout 2 | `2fee90e21355`  |
| 1717   | Layout 2 | `2fee90e21355`  |
| 1710   | Layout 2 | `2fee90e21355`  |
| 1704   | Layout 2 | `2fee90e21355`  |
| 1698   | Layout 2 | `2fee90e21355`  |
| 1690   | Layout 2 | `2fee90e21355`  |
| 1685   | Layout 1 | `2fee90e21355`  |
| 1680   | Layout 1 | `2fee90e21355`  |
| 1674   | Layout 1 | `2fee90e21355`  |
| 1668   | Layout 1 | `2fee90e21355`  |
| 1659   | Layout 1 | `2fee90e21355`  |
| 1649   | Layout 1 | `2fee90e21355`  |
| 1642   | Layout 1 | `2fee90e21355`  |
| 1636   | Layout 1 | `2fee90e21355`  |
| 1628   | Layout 1 | `2fee90e21355`  |
| 1622   | Layout 1 | `2fee90e21355`  |
| 1614   | Layout 1 | `2fee90e21355`  |
| 1608   | Layout 1 | `2fee90e21355`  |
| 1602   | Layout 1 | `2fee90e21355`  |
| 1598   | Layout 1 | `2fee90e21355`  |
| 1594   | Layout 1 | `2fee90e21355`  |
| 1590   | Layout 1 | `2fee90e21355`  |
| 1587   | Layout 1 | `2fee90e21355`  |
| 1584   | Layout 1 | `2fee90e21355`  |
| 1579   | Layout 1 | `2fee90e21355`  |
| 1572   | Layout 1 | `2fee90e21355`  |
| 1565   | Layout 1 | `2fee90e21355`  |
| 1559   | Layout 1 | `2fee90e21355`  |
| 1554   | Layout 1 | `2fee90e21355`  |
| 1547   | Layout 1 | `2fee90e21355`  |
| 1537   | Layout 1 | `2fee90e21355`  |
| 1529   | Layout 1 | `2fee90e21355`  |
| 1524   | Layout 1 | `2fee90e21355`  |
| 1519   | Layout 2 | `2fee90e21355`  |
| 1509   | Layout 2 | `2fee90e21355`  |
| 1506   | Layout 2 | `2fee90e21355`  |
| 1504   | Layout 2 | `2fee90e21355`  |
| 1500   | No file  | `2fee90e21355`  |
| 1493   | No file  | `2fee90e21355`  |
| 1489   | No file  | `2fee90e21355`  |
| 1485   | No file  | `2fee90e21355`  |
| 1481   | No file  | `2fee90e21355`  |
| 1474   | No file  | `2fee90e21355`  |
| 1466   | No file  | `2fee90e21355`  |
| 1462   | No file  | `2fee90e21355`  |
| 1459   | No file  | `2fee90e21355`  |
| 1453   | No file  | `2fee90e21355`  |
| 1450   | No file  | `2fee90e21355`  |
| 1445   | No file  | `2fee90e21355`  |
| 1439   | No file  | `2fee90e21355`  |
| 1433   | No file  | `2fee90e21355`  |
| 1430   | No file  | `2fee90e21355`  |
| 1426   | No file  | `2fee90e21355`  |
| 1421   | No file  | `2fee90e21355`  |
| 1417   | No file  | `2fee90e21355`  |
| 1416   | No file  | `2fee90e21355`  |
| 1409   | No file  | `2fee90e21355`  |
| 1405   | No file  | `2fee90e21355`  |
| 1401   | No file  | `2fee90e21355`  |
| 1396   | No file  | `2fee90e21355`  |
| 1391   | No file  | `2fee90e21355`  |
| 1390   | No file  | `2fee90e21355`  |
| 1386   | No file  | `2fee90e21355`  |
| 1381   | No file  | `2fee90e21355`  |
| 1379   | No file  | `2fee90e21355`  |
| 1372   | No file  | `2fee90e21355`  |
| 1366   | No file  | `2fee90e21355`  |
| 1364   | No file  | `2fee90e21355`  |
| 1363   | No file  | `2fee90e21355`  |
| 1360   | No file  | `2fee90e21355`  |
| 1358   | No file  | `2fee90e21355`  |
| 1355   | No file  | `2fee90e21355`  |
| 1351   | No file  | `2fee90e21355`  |
| 1348   | No file  | `2fee90e21355`  |
| 1346   | No file  | `2fee90e21355`  |
| 1341   | No file  | `2fee90e21355`  |
| 1340   | No file  | `2fee90e21355`  |
| 1338   | No file  | `2fee90e21355`  |
| 1335   | No file  | `2fee90e21355`  |
| 1333   | No file  | `2fee90e21355`  |
| 1329   | No file  | `2fee90e21355`  |
| 1327   | No file  | `2fee90e21355`  |
| 1324   | No file  | `2fee90e21355`  |
| 1321   | No file  | `2fee90e21355`  |
| 1319   | No file  | `2fee90e21355`  |
| 1318   | No file  | `2fee90e21355`  |
| 1316   | No file  | `2fee90e21355`  |
| 1313   | No file  | `2fee90e21355`  |
| 1311   | No file  | `2fee90e21355`  |
| 1309   | No file  | `2fee90e21355`  |
| 1304   | No file  | `2fee90e21355`  |
| 1292   | No file  | `2fee90e21355`  |
| 1286   | No file  | `2fee90e21355`  |
| 1280   | No file  | `2fee90e21355`  |
| 1276   | No file  | `2fee90e21355`  |
| 1267   | No file  | `2fee90e21355`  |
| 1261   | No file  | `2fee90e21355`  |
| 1256   | No file  | `2fee90e21355`  |
| 1250   | No file  | `2fee90e21355`  |
| 1246   | No file  | `2fee90e21355`  |
| 1239   | No file  | `2fee90e21355`  |
| 1230   | No file  | `2fee90e21355`  |
| 1226   | No file  | `2fee90e21355`  |
| 1220   | No file  | `2fee90e21355`  |
| 1217   | No file  | `2fee90e21355`  |
| 1211   | No file  | `2fee90e21355`  |
| 1210   | No file  | `2fee90e21355`  |
| 1208   | No file  | `2fee90e21355`  |
| 1203   | No file  | `2fee90e21355`  |
| 1197   | No file  | `2fee90e21355`  |
| 1194   | No file  | `2fee90e21355`  |
| 1192   | No file  | `2fee90e21355`  |
| 1187   | No file  | `2fee90e21355`  |
| 1183   | No file  | `2fee90e21355`  |
| 1177   | No file  | `2fee90e21355`  |
| 1173   | No file  | `2fee90e21355`  |
| 1167   | No file  | `2fee90e21355`  |
| 1164   | No file  | `2fee90e21355`  |
| 1156   | No file  | `2fee90e21355`  |
| 1149   | No file  | `2fee90e21355`  |
| 1144   | No file  | `2fee90e21355`  |
| 1137   | No file  | `2fee90e21355`  |
| 1132   | No file  | `2fee90e21355`  |
| 1127   | No file  | `2fee90e21355`  |
| 1122   | No file  | `2fee90e21355`  |
| 1118   | No file  | `2fee90e21355`  |
| 1114   | No file  | `2fee90e21355`  |
| 1109   | No file  | `2fee90e21355`  |
| 1102   | No file  | `2fee90e21355`  |
| 1096   | No file  | `2fee90e21355`  |
| 1088   | No file  | `2fee90e21355`  |
| 1081   | No file  | `2fee90e21355`  |
| 1076   | No file  | `2fee90e21355`  |
| 1069   | No file  | `2fee90e21355`  |
| 1064   | No file  | `2fee90e21355`  |
| 1058   | No file  | `2fee90e21355`  |
| 1051   | No file  | `2fee90e21355`  |
| 1044   | No file  | `2fee90e21355`  |
| 1036   | No file  | `2fee90e21355`  |
| 1026   | No file  | `2fee90e21355`  |
| 1016   | No file  | `2fee90e21355`  |
| 1009   | No file  | `2fee90e21355`  |
| 1005   | No file  | `2fee90e21355`  |
| 1000   | No file  | `2fee90e21355`  |
| 998    | No file  | `2fee90e21355`  |
| 990    | No file  | `2fee90e21355`  |
| 979    | No file  | `2fee90e21355`  |
| 972    | No file  | `2fee90e21355`  |
| 963    | No file  | `2fee90e21355`  |
| 955    | No file  | `2fee90e21355`  |
| 946    | No file  | `2fee90e21355`  |
| 938    | No file  | `2fee90e21355`  |
| 927    | No file  | `2fee90e21355`  |
| 911    | No file  | `2fee90e21355`  |
| 904    | No file  | `2fee90e21355`  |
| 899    | No file  | `2fee90e21355`  |
| 894    | No file  | `2fee90e21355`  |
| 885    | No file  | `2fee90e21355`  |
| 879    | No file  | `2fee90e21355`  |
| 872    | No file  | `2fee90e21355`  |
| 864    | No file  | `2fee90e21355`  |
| 855    | No file  | `2fee90e21355`  |
| 853    | No file  | `2fee90e21355`  |
| 845    | No file  | `2fee90e21355`  |
| 837    | No file  | `2fee90e21355`  |
| 829    | No file  | `2fee90e21355`  |
| 822    | No file  | `2fee90e21355`  |
| 814    | No file  | `2fee90e21355`  |
| 805    | No file  | `2fee90e21355`  |
| 794    | No file  | `2fee90e21355`  |
| 787    | No file  | `2fee90e21355`  |
| 780    | No file  | `2fee90e21355`  |
| 771    | No file  | `2fee90e21355`  |
| 760    | No file  | `2fee90e21355`  |
| 748    | No file  | `2fee90e21355`  |
| 741    | No file  | `2fee90e21355`  |
| 736    | No file  | `2fee90e21355`  |
| 731    | No file  | `2fee90e21355`  |
| 723    | No file  | `2fee90e21355`  |
| 711    | No file  | `2fee90e21355`  |
| 707    | No file  | `2fee90e21355`  |
| 697    | No file  | `2fee90e21355`  |
| 689    | No file  | `2fee90e21355`  |
| 683    | No file  | `2fee90e21355`  |
| 678    | No file  | `2fee90e21355`  |
| 670    | No file  | `2fee90e21355`  |
| 661    | No file  | `2fee90e21355`  |
| 656    | No file  | `2fee90e21355`  |
| 652    | No file  | `2fee90e21355`  |
| 643    | No file  | `2fee90e21355`  |
| 637    | No file  | `2fee90e21355`  |
| 630    | No file  | `2fee90e21355`  |
| 627    | No file  | `2fee90e21355`  |
| 621    | No file  | `2fee90e21355`  |
| 617    | No file  | `2fee90e21355`  |
| 615    | No file  | `2fee90e21355`  |
| 606    | No file  | `2fee90e21355`  |
| 599    | No file  | `2fee90e21355`  |
| 592    | No file  | `2fee90e21355`  |
| 586    | No file  | `2fee90e21355`  |
| 577    | No file  | `2fee90e21355`  |
| 569    | No file  | `2fee90e21355`  |
| 561    | No file  | `2fee90e21355`  |
| 554    | No file  | `2fee90e21355`  |
| 542    | No file  | `2fee90e21355`  |
| 532    | No file  | `2fee90e21355`  |
| 531    | No file  | `2fee90e21355`  |
| 526    | No file  | `2fee90e21355`  |
| 521    | No file  | `2fee90e21355`  |
| 517    | No file  | `2fee90e21355`  |
| 510    | No file  | `2fee90e21355`  |
| 508    | No file  | `2fee90e21355`  |
| 504    | No file  | `2fee90e21355`  |
| 497    | No file  | `2fee90e21355`  |
| 491    | No file  | `2fee90e21355`  |
| 485    | No file  | `2fee90e21355`  |
| 478    | No file  | `2fee90e21355`  |
| 472    | No file  | `2fee90e21355`  |
| 466    | No file  | `2fee90e21355`  |
| 457    | No file  | `2fee90e21355`  |
| 452    | No file  | `2fee90e21355`  |
| 449    | No file  | `2fee90e21355`  |
| 435    | No file  | `2fee90e21355`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                 |
| --------------------- | -------- | ---------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0) and the letter texts (type 37)   |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of letters                             |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (13 bytes)

| Offset  | Type | Field                  | Notes                                                                                  |
| ------- | ---- | ---------------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key               | The letter item (LOC type 0 name); the rows are in no key order                        |
| `+0x04` | u32  | main_desc_string_index | Index into `strings`: the `RESOURCE` sheet key of the text (`PANEL_LETTER_BADEIN_1`)   |
| `+0x08` | u32  | texture_path_index     | Index into `strings`: the background under `ui_texture/` (`Combine/ETC/Combine_Etc_FugarCheering.dds`) |
| `+0x0C` | u8   | is_center_alignment    | `1` centers the text; `1` on 17 of 53 rows of client 3482                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                      |
| ------- | ------------------ | ------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                          |
| `+0x04` | pstr[string_count] | strings      | The keys and texture paths, UTF-16LE; a texture several rows share is stored once |

## Layout 1

No `is_center_alignment` byte: a row is 12 bytes. Only the Row differs from
Layout 2.

### Row (12 bytes)

| Offset  | Type | Field                  | Notes |
| ------- | ---- | ---------------------- | ----- |
| `+0x00` | u32  | item_key               |       |
| `+0x04` | u32  | main_desc_string_index |       |
| `+0x08` | u32  | texture_path_index     |       |

## Field Names

The `Letter` sheet of a private server's `DataSheets.bexcel` on client 1784
has the columns `itemkey`, `mainDescStringKey`, `texturePath` and
`CenterAlignment` (`1` or empty), 26 rows.

| Field                  | Column              | Same value (client 1784) | Same value (client 3482) |
| ---------------------- | ------------------- | ------------------------ | ------------------------ |
| item_key               | `itemkey`           | 26 of 26                 | 26 of 26                 |
| main_desc_string_index | `mainDescStringKey` | 26 of 26                 | 24 of 26                 |
| texture_path_index     | `texturePath`       | 26 of 26                 | 26 of 26                 |
| is_center_alignment    | `CenterAlignment`   | 26 of 26                 | 26 of 26                 |

The string columns compare the string an index points at. On client 3482
items `8199` and `8200` point at `PANEL_LETTER_SEASON_FINISH_DESC_NEW_1`
and `_NEW_2` where the sheet has `PANEL_LETTER_SEASON_FINISH_DESC4` and
`DESC5`.

## Notes

- The letter text is LOC type 37 under `key_hash()` of the key and the
  `RESOURCE` sheet's `str_id2`, as for the other `RESOURCE` keys of
  [`stringtable.bss`](stringtable_bss.md).
