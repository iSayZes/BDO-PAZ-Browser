# `fairyupgraderate.bss` Format

## Purpose

Defines the **Sprouting** success rates for fairies. Sprouting is the attempt to
raise a max-level fairy into the next grade, and it consumes fairy-growth wine.
Each wine consumed adds a fixed slice of success chance, so the file stores, per
grade transition and per usable item, the chance contributed by **one** item and
the item count that reaches a guaranteed 100%.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                   | Bytes | Records           | Row bytes |
| ------ | ------------- | ---------------------- | ----- | ----------------- | --------- |
| 1      | 805 and later | `fairyupgraderate.bss` | 143   | 6 Entry, 3 Record | 16        |

| Layout | File                   | Known         | Unknown      |
| ------ | ---------------------- | ------------- | ------------ |
| 1      | `fairyupgraderate.bss` | 116 B (81.1%) | 27 B (18.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `fb27c3083611`  |
| 3482   | Layout 1             | `fb27c3083611`  |
| 3474   | Layout 1             | `fb27c3083611`  |
| 3473   | Layout 1             | `fb27c3083611`  |
| 3464   | Layout 1             | `fb27c3083611`  |
| 3458   | Layout 1             | `fb27c3083611`  |
| 3454   | Layout 1             | `fb27c3083611`  |
| 3444   | Layout 1             | `fb27c3083611`  |
| 3435   | Layout 1             | `fb27c3083611`  |
| 3426   | Layout 1             | `fb27c3083611`  |
| 3418   | Layout 1             | `fb27c3083611`  |
| 3412   | Layout 1             | `fb27c3083611`  |
| 3402   | Layout 1             | `fb27c3083611`  |
| 3396   | Layout 1             | `fb27c3083611`  |
| 3387   | Layout 1             | `fb27c3083611`  |
| 3381   | Layout 1             | `fb27c3083611`  |
| 3373   | Layout 1             | `fb27c3083611`  |
| 3364   | Layout 1             | `fb27c3083611`  |
| 3356   | Layout 1             | `fb27c3083611`  |
| 3349   | Layout 1             | `fb27c3083611`  |
| 3342   | Layout 1             | `fb27c3083611`  |
| 3335   | Layout 1             | `fb27c3083611`  |
| 3326   | Layout 1             | `fb27c3083611`  |
| 3321   | Layout 1             | `fb27c3083611`  |
| 3314   | Layout 1             | `fb27c3083611`  |
| 3303   | Layout 1             | `fb27c3083611`  |
| 3302   | Layout 1             | `fb27c3083611`  |
| 3293   | Layout 1             | `fb27c3083611`  |
| 3283   | Layout 1             | `fb27c3083611`  |
| 3275   | Layout 1             | `fb27c3083611`  |
| 3267   | Layout 1             | `fb27c3083611`  |
| 3258   | Layout 1             | `fb27c3083611`  |
| 3251   | Layout 1             | `fb27c3083611`  |
| 3242   | Layout 1             | `fb27c3083611`  |
| 3235   | Layout 1             | `fb27c3083611`  |
| 3229   | Layout 1             | `fb27c3083611`  |
| 3212   | Layout 1             | `fb27c3083611`  |
| 3203   | Layout 1             | `fb27c3083611`  |
| 3193   | Layout 1             | `fb27c3083611`  |
| 3186   | Layout 1             | `fb27c3083611`  |
| 3177   | Layout 1             | `fb27c3083611`  |
| 3169   | Layout 1             | `fb27c3083611`  |
| 3158   | Layout 1             | `fb27c3083611`  |
| 3151   | Layout 1             | `fb27c3083611`  |
| 3144   | Layout 1             | `fb27c3083611`  |
| 3133   | Layout 1             | `fb27c3083611`  |
| 3125   | Layout 1             | `fb27c3083611`  |
| 3118   | Layout 1             | `fb27c3083611`  |
| 3111   | Layout 1             | `fb27c3083611`  |
| 3103   | Layout 1             | `fb27c3083611`  |
| 3095   | Layout 1             | `fb27c3083611`  |
| 3086   | Layout 1             | `fb27c3083611`  |
| 3072   | Layout 1             | `fb27c3083611`  |
| 3062   | Layout 1             | `fb27c3083611`  |
| 3052   | Layout 1             | `fb27c3083611`  |
| 3045   | Layout 1             | `fb27c3083611`  |
| 3037   | Layout 1             | `fb27c3083611`  |
| 3030   | Layout 1             | `fb27c3083611`  |
| 3021   | Layout 1             | `fb27c3083611`  |
| 3012   | Layout 1             | `fb27c3083611`  |
| 3002   | Layout 1             | `fb27c3083611`  |
| 2995   | Layout 1             | `fb27c3083611`  |
| 2987   | Layout 1             | `fb27c3083611`  |
| 2978   | Layout 1             | `fb27c3083611`  |
| 2970   | Layout 1             | `fb27c3083611`  |
| 2959   | Layout 1             | `fb27c3083611`  |
| 2951   | Layout 1             | `fb27c3083611`  |
| 2942   | Layout 1             | `fb27c3083611`  |
| 2935   | Layout 1             | `fb27c3083611`  |
| 2932   | Layout 1             | `fb27c3083611`  |
| 2923   | Layout 1             | `fb27c3083611`  |
| 2919   | Layout 1             | `fb27c3083611`  |
| 2907   | Layout 1             | `fb27c3083611`  |
| 2900   | Layout 1             | `fb27c3083611`  |
| 2891   | Layout 1             | `fb27c3083611`  |
| 2882   | Layout 1             | `fb27c3083611`  |
| 2872   | Layout 1             | `fb27c3083611`  |
| 2863   | Layout 1             | `fb27c3083611`  |
| 2855   | Layout 1             | `fb27c3083611`  |
| 2849   | Layout 1             | `fb27c3083611`  |
| 2844   | Layout 1             | `fb27c3083611`  |
| 2834   | Layout 1             | `fb27c3083611`  |
| 2825   | Layout 1             | `fb27c3083611`  |
| 2819   | Layout 1             | `fb27c3083611`  |
| 2811   | Layout 1             | `fb27c3083611`  |
| 2803   | Layout 1             | `fb27c3083611`  |
| 2794   | Layout 1             | `fb27c3083611`  |
| 2783   | Layout 1             | `fb27c3083611`  |
| 2774   | Layout 1             | `fb27c3083611`  |
| 2765   | Layout 1             | `fb27c3083611`  |
| 2756   | Layout 1             | `fb27c3083611`  |
| 2750   | Layout 1             | `fb27c3083611`  |
| 2743   | Layout 1             | `fb27c3083611`  |
| 2736   | Layout 1             | `fb27c3083611`  |
| 2726   | Layout 1             | `fb27c3083611`  |
| 2717   | Layout 1             | `fb27c3083611`  |
| 2709   | Layout 1             | `fb27c3083611`  |
| 2703   | Layout 1             | `fb27c3083611`  |
| 2695   | Layout 1             | `fb27c3083611`  |
| 2684   | Layout 1             | `fb27c3083611`  |
| 2672   | Layout 1             | `fb27c3083611`  |
| 2665   | Layout 1             | `fb27c3083611`  |
| 2657   | Layout 1             | `fb27c3083611`  |
| 2649   | Layout 1             | `fb27c3083611`  |
| 2644   | Layout 1             | `fb27c3083611`  |
| 2637   | Layout 1             | `fb27c3083611`  |
| 2629   | Layout 1             | `fb27c3083611`  |
| 2619   | Layout 1             | `fb27c3083611`  |
| 2612   | Layout 1             | `fb27c3083611`  |
| 2606   | Layout 1             | `fb27c3083611`  |
| 2602   | Layout 1             | `fb27c3083611`  |
| 2601   | Layout 1             | `fb27c3083611`  |
| 2592   | Layout 1             | `fb27c3083611`  |
| 2583   | Layout 1             | `fb27c3083611`  |
| 2575   | Layout 1             | `fb27c3083611`  |
| 2567   | Layout 1             | `fb27c3083611`  |
| 2560   | Layout 1             | `fb27c3083611`  |
| 2553   | Layout 1             | `fb27c3083611`  |
| 2545   | Layout 1             | `fb27c3083611`  |
| 2538   | Layout 1             | `fb27c3083611`  |
| 2529   | Layout 1             | `fb27c3083611`  |
| 2519   | Layout 1             | `fb27c3083611`  |
| 2513   | Layout 1             | `fb27c3083611`  |
| 2510   | Layout 1             | `fb27c3083611`  |
| 2507   | Layout 1             | `fb27c3083611`  |
| 2503   | Layout 1             | `fb27c3083611`  |
| 2498   | Layout 1             | `fb27c3083611`  |
| 2492   | Layout 1             | `fb27c3083611`  |
| 2487   | Layout 1             | `fb27c3083611`  |
| 2480   | Layout 1             | `fb27c3083611`  |
| 2474   | Layout 1             | `fb27c3083611`  |
| 2468   | Layout 1             | `fb27c3083611`  |
| 2460   | Layout 1             | `fb27c3083611`  |
| 2453   | Layout 1             | `fb27c3083611`  |
| 2444   | Layout 1             | `fb27c3083611`  |
| 2438   | Layout 1             | `fb27c3083611`  |
| 2434   | Layout 1             | `fb27c3083611`  |
| 2429   | Layout 1             | `fb27c3083611`  |
| 2421   | Layout 1             | `fb27c3083611`  |
| 2414   | Layout 1             | `fb27c3083611`  |
| 2407   | Layout 1             | `fb27c3083611`  |
| 2401   | Layout 1             | `fb27c3083611`  |
| 2397   | Layout 1             | `fb27c3083611`  |
| 2393   | Layout 1             | `fb27c3083611`  |
| 2384   | Layout 1             | `fb27c3083611`  |
| 2378   | Layout 1             | `fb27c3083611`  |
| 2372   | Layout 1             | `fb27c3083611`  |
| 2358   | Layout 1             | `fb27c3083611`  |
| 2352   | Layout 1             | `fb27c3083611`  |
| 2347   | Layout 1             | `fb27c3083611`  |
| 2343   | Layout 1             | `fb27c3083611`  |
| 2335   | Layout 1             | `fb27c3083611`  |
| 2327   | Layout 1             | `fb27c3083611`  |
| 2324   | Layout 1             | `fb27c3083611`  |
| 2319   | Layout 1             | `fb27c3083611`  |
| 2313   | Layout 1             | `fb27c3083611`  |
| 2308   | Layout 1             | `fb27c3083611`  |
| 2302   | Layout 1             | `fb27c3083611`  |
| 2295   | Layout 1             | `fb27c3083611`  |
| 2290   | Layout 1             | `fb27c3083611`  |
| 2284   | Layout 1             | `fb27c3083611`  |
| 2276   | Layout 1             | `fb27c3083611`  |
| 2269   | Layout 1             | `fb27c3083611`  |
| 2259   | Layout 1             | `fb27c3083611`  |
| 2250   | Layout 1             | `fb27c3083611`  |
| 2243   | Layout 1             | `fb27c3083611`  |
| 2235   | Layout 1             | `fb27c3083611`  |
| 2229   | Layout 1             | `fb27c3083611`  |
| 2224   | Layout 1             | `fb27c3083611`  |
| 2218   | Layout 1             | `fb27c3083611`  |
| 2215   | Layout 1             | `fb27c3083611`  |
| 2207   | Layout 1             | `fb27c3083611`  |
| 2203   | Layout 1             | `fb27c3083611`  |
| 2196   | Layout 1             | `fb27c3083611`  |
| 2192   | Layout 1             | `fb27c3083611`  |
| 2189   | Layout 1             | `fb27c3083611`  |
| 2183   | Layout 1             | `fb27c3083611`  |
| 2179   | Layout 1             | `fb27c3083611`  |
| 2171   | Layout 1             | `fb27c3083611`  |
| 2163   | Layout 1             | `fb27c3083611`  |
| 2156   | Layout 1             | `fb27c3083611`  |
| 2151   | Layout 1             | `fb27c3083611`  |
| 2147   | Layout 1             | `fb27c3083611`  |
| 2142   | Layout 1             | `fb27c3083611`  |
| 2138   | Layout 1             | `fb27c3083611`  |
| 2134   | Layout 1             | `fb27c3083611`  |
| 2130   | Layout 1             | `fb27c3083611`  |
| 2122   | Layout 1             | `fb27c3083611`  |
| 2107   | Layout 1             | `fb27c3083611`  |
| 2098   | Layout 1             | `fb27c3083611`  |
| 2089   | Layout 1             | `fb27c3083611`  |
| 2081   | Layout 1             | `fb27c3083611`  |
| 2073   | Layout 1             | `fb27c3083611`  |
| 2067   | Layout 1             | `fb27c3083611`  |
| 2063   | Layout 1             | `fb27c3083611`  |
| 2059   | Layout 1             | `fb27c3083611`  |
| 2052   | Layout 1             | `fb27c3083611`  |
| 2044   | Layout 1             | `fb27c3083611`  |
| 2039   | Layout 1             | `fb27c3083611`  |
| 2032   | Layout 1             | `fb27c3083611`  |
| 2025   | Layout 1             | `fb27c3083611`  |
| 2011   | Layout 1             | `fb27c3083611`  |
| 2005   | Layout 1             | `fb27c3083611`  |
| 2000   | Layout 1             | `fb27c3083611`  |
| 1996   | Layout 1             | `fb27c3083611`  |
| 1991   | Layout 1             | `fb27c3083611`  |
| 1985   | Layout 1             | `fb27c3083611`  |
| 1980   | Layout 1             | `fb27c3083611`  |
| 1969   | Layout 1             | `fb27c3083611`  |
| 1964   | Layout 1             | `fb27c3083611`  |
| 1958   | Layout 1             | `fb27c3083611`  |
| 1950   | Layout 1             | `fb27c3083611`  |
| 1945   | Layout 1             | `fb27c3083611`  |
| 1937   | Layout 1             | `fb27c3083611`  |
| 1933   | Layout 1             | `fb27c3083611`  |
| 1927   | Layout 1             | `fb27c3083611`  |
| 1921   | Layout 1             | `fb27c3083611`  |
| 1914   | Layout 1             | `fb27c3083611`  |
| 1908   | Layout 1             | `fb27c3083611`  |
| 1897   | Layout 1             | `fb27c3083611`  |
| 1892   | Layout 1             | `fb27c3083611`  |
| 1886   | Layout 1             | `fb27c3083611`  |
| 1881   | Layout 1             | `fb27c3083611`  |
| 1871   | Layout 1             | `fb27c3083611`  |
| 1866   | Layout 1             | `fb27c3083611`  |
| 1862   | Layout 1             | `fb27c3083611`  |
| 1854   | Layout 1             | `fb27c3083611`  |
| 1846   | Layout 1             | `fb27c3083611`  |
| 1838   | Layout 1             | `fb27c3083611`  |
| 1832   | Layout 1             | `fb27c3083611`  |
| 1826   | Layout 1             | `fb27c3083611`  |
| 1822   | Layout 1             | `fb27c3083611`  |
| 1818   | Layout 1             | `fb27c3083611`  |
| 1804   | Layout 1             | `fb27c3083611`  |
| 1794   | Layout 1             | `fb27c3083611`  |
| 1790   | Layout 1             | `fb27c3083611`  |
| 1784   | Layout 1             | `fb27c3083611`  |
| 1774   | Layout 1             | `fb27c3083611`  |
| 1771   | Layout 1             | `fb27c3083611`  |
| 1762   | Layout 1             | `fb27c3083611`  |
| 1759   | Layout 1             | `fb27c3083611`  |
| 1754   | Layout 1             | `fb27c3083611`  |
| 1749   | Layout 1             | `fb27c3083611`  |
| 1743   | Layout 1             | `fb27c3083611`  |
| 1737   | Layout 1             | `fb27c3083611`  |
| 1731   | Layout 1             | `fb27c3083611`  |
| 1725   | Layout 1             | `fb27c3083611`  |
| 1717   | Layout 1             | `fb27c3083611`  |
| 1710   | Layout 1             | `fb27c3083611`  |
| 1704   | Layout 1             | `fb27c3083611`  |
| 1698   | Layout 1             | `fb27c3083611`  |
| 1690   | Layout 1             | `fb27c3083611`  |
| 1685   | Layout 1             | `fb27c3083611`  |
| 1680   | Layout 1             | `fb27c3083611`  |
| 1674   | Layout 1             | `fb27c3083611`  |
| 1668   | Layout 1             | `fb27c3083611`  |
| 1659   | Layout 1             | `fb27c3083611`  |
| 1649   | Layout 1             | `fb27c3083611`  |
| 1642   | Layout 1             | `fb27c3083611`  |
| 1636   | Layout 1             | `fb27c3083611`  |
| 1628   | Layout 1             | `fb27c3083611`  |
| 1622   | Layout 1             | `fb27c3083611`  |
| 1614   | Layout 1             | `fb27c3083611`  |
| 1608   | Layout 1             | `fb27c3083611`  |
| 1602   | Layout 1             | `fb27c3083611`  |
| 1598   | Layout 1             | `fb27c3083611`  |
| 1594   | Layout 1             | `fb27c3083611`  |
| 1590   | Layout 1             | `fb27c3083611`  |
| 1587   | Layout 1             | `fb27c3083611`  |
| 1584   | Layout 1             | `fb27c3083611`  |
| 1579   | Layout 1             | `fb27c3083611`  |
| 1572   | Layout 1             | `fb27c3083611`  |
| 1565   | Layout 1             | `fb27c3083611`  |
| 1559   | Layout 1             | `fb27c3083611`  |
| 1554   | Layout 1             | `fb27c3083611`  |
| 1547   | Layout 1             | `fb27c3083611`  |
| 1537   | Layout 1             | `fb27c3083611`  |
| 1529   | Layout 1             | `fb27c3083611`  |
| 1524   | Layout 1             | `fb27c3083611`  |
| 1519   | Layout 1             | `fb27c3083611`  |
| 1509   | Layout 1             | `fb27c3083611`  |
| 1506   | Layout 1             | `fb27c3083611`  |
| 1504   | Layout 1             | `fb27c3083611`  |
| 1500   | Layout 1             | `fb27c3083611`  |
| 1493   | Layout 1             | `fb27c3083611`  |
| 1489   | Layout 1             | `fb27c3083611`  |
| 1485   | Layout 1             | `fb27c3083611`  |
| 1481   | Layout 1             | `fb27c3083611`  |
| 1474   | Layout 1             | `fb27c3083611`  |
| 1466   | Layout 1             | `fb27c3083611`  |
| 1462   | Layout 1             | `fb27c3083611`  |
| 1459   | Layout 1             | `fb27c3083611`  |
| 1453   | Layout 1             | `fb27c3083611`  |
| 1450   | Layout 1             | `fb27c3083611`  |
| 1445   | Layout 1             | `fb27c3083611`  |
| 1439   | Layout 1             | `fb27c3083611`  |
| 1433   | Layout 1             | `fb27c3083611`  |
| 1430   | Layout 1             | `fb27c3083611`  |
| 1426   | Layout 1             | `fb27c3083611`  |
| 1421   | Layout 1             | `fb27c3083611`  |
| 1417   | Layout 1             | `fb27c3083611`  |
| 1416   | Layout 1             | `fb27c3083611`  |
| 1409   | Layout 1             | `fb27c3083611`  |
| 1405   | Layout 1             | `fb27c3083611`  |
| 1401   | Layout 1             | `fb27c3083611`  |
| 1396   | Layout 1             | `fb27c3083611`  |
| 1391   | Layout 1             | `fb27c3083611`  |
| 1390   | Layout 1             | `fb27c3083611`  |
| 1386   | Layout 1             | `fb27c3083611`  |
| 1381   | Layout 1             | `fb27c3083611`  |
| 1379   | Layout 1             | `fb27c3083611`  |
| 1372   | Layout 1             | `fb27c3083611`  |
| 1366   | Layout 1             | `fb27c3083611`  |
| 1364   | Layout 1             | `fb27c3083611`  |
| 1363   | Layout 1             | `fb27c3083611`  |
| 1360   | Layout 1             | `fb27c3083611`  |
| 1358   | Layout 1             | `fb27c3083611`  |
| 1355   | Layout 1             | `fb27c3083611`  |
| 1351   | Layout 1             | `fb27c3083611`  |
| 1348   | Layout 1             | `fb27c3083611`  |
| 1346   | Layout 1             | `fb27c3083611`  |
| 1341   | Layout 1             | `fb27c3083611`  |
| 1340   | Layout 1             | `fb27c3083611`  |
| 1338   | Layout 1             | `fb27c3083611`  |
| 1335   | Layout 1             | `fb27c3083611`  |
| 1333   | Layout 1             | `fb27c3083611`  |
| 1329   | Layout 1             | `fb27c3083611`  |
| 1327   | Layout 1             | `fb27c3083611`  |
| 1324   | Layout 1             | `fb27c3083611`  |
| 1321   | Layout 1             | `fb27c3083611`  |
| 1319   | Layout 1             | `fb27c3083611`  |
| 1318   | Layout 1             | `fb27c3083611`  |
| 1316   | Layout 1             | `fb27c3083611`  |
| 1313   | Layout 1             | `fb27c3083611`  |
| 1311   | Layout 1             | `fb27c3083611`  |
| 1309   | Layout 1             | `fb27c3083611`  |
| 1304   | Layout 1             | `fb27c3083611`  |
| 1292   | Layout 1             | `fb27c3083611`  |
| 1286   | Layout 1             | `fb27c3083611`  |
| 1280   | Layout 1             | `fb27c3083611`  |
| 1276   | Layout 1             | `fb27c3083611`  |
| 1267   | Layout 1             | `fb27c3083611`  |
| 1261   | Layout 1             | `fb27c3083611`  |
| 1256   | Layout 1             | `fb27c3083611`  |
| 1250   | Layout 1             | `fb27c3083611`  |
| 1246   | Layout 1             | `fb27c3083611`  |
| 1239   | Layout 1             | `fb27c3083611`  |
| 1230   | Layout 1             | `fb27c3083611`  |
| 1226   | Layout 1             | `fb27c3083611`  |
| 1220   | Layout 1             | `fb27c3083611`  |
| 1217   | Layout 1             | `fb27c3083611`  |
| 1211   | Layout 1             | `fb27c3083611`  |
| 1210   | Layout 1             | `fb27c3083611`  |
| 1208   | Layout 1             | `fb27c3083611`  |
| 1203   | Layout 1             | `fb27c3083611`  |
| 1197   | Layout 1             | `fb27c3083611`  |
| 1194   | Layout 1             | `fb27c3083611`  |
| 1192   | Layout 1             | `fb27c3083611`  |
| 1187   | Layout 1             | `fb27c3083611`  |
| 1183   | Layout 1             | `fb27c3083611`  |
| 1177   | Layout 1             | `fb27c3083611`  |
| 1173   | Layout 1             | `fb27c3083611`  |
| 1167   | Layout 1             | `fb27c3083611`  |
| 1164   | Layout 1             | `fb27c3083611`  |
| 1156   | Layout 1             | `fb27c3083611`  |
| 1149   | Layout 1             | `fb27c3083611`  |
| 1144   | Layout 1             | `fb27c3083611`  |
| 1137   | Layout 1             | `fb27c3083611`  |
| 1132   | Layout 1             | `fb27c3083611`  |
| 1127   | Layout 1             | `fb27c3083611`  |
| 1122   | Layout 1             | `fb27c3083611`  |
| 1118   | Layout 1             | `fb27c3083611`  |
| 1114   | Layout 1             | `fb27c3083611`  |
| 1109   | Layout 1             | `fb27c3083611`  |
| 1102   | Layout 1             | `fb27c3083611`  |
| 1096   | Layout 1             | `fb27c3083611`  |
| 1088   | Layout 1             | `fb27c3083611`  |
| 1081   | Layout 1             | `fb27c3083611`  |
| 1076   | Layout 1             | `fb27c3083611`  |
| 1069   | Layout 1             | `fb27c3083611`  |
| 1064   | Layout 1             | `fb27c3083611`  |
| 1058   | Layout 1             | `fb27c3083611`  |
| 1051   | Layout 1             | `fb27c3083611`  |
| 1044   | Layout 1             | `fb27c3083611`  |
| 1036   | Layout 1             | `fb27c3083611`  |
| 1026   | Layout 1             | `fb27c3083611`  |
| 1016   | Layout 1             | `fb27c3083611`  |
| 1009   | Layout 1             | `fb27c3083611`  |
| 1005   | Layout 1             | `fb27c3083611`  |
| 1000   | Layout 1             | `fb27c3083611`  |
| 998    | Layout 1             | `fb27c3083611`  |
| 990    | Layout 1             | `fb27c3083611`  |
| 979    | Layout 1             | `fb27c3083611`  |
| 972    | Layout 1             | `fb27c3083611`  |
| 963    | Layout 1             | `fb27c3083611`  |
| 955    | Layout 1             | `fb27c3083611`  |
| 946    | Layout 1             | `fb27c3083611`  |
| 938    | Layout 1             | `fb27c3083611`  |
| 927    | Layout 1             | `fb27c3083611`  |
| 911    | Layout 1             | `fb27c3083611`  |
| 904    | Layout 1             | `fb27c3083611`  |
| 899    | Layout 1             | `fb27c3083611`  |
| 894    | Layout 1             | `fb27c3083611`  |
| 885    | Layout 1             | `fb27c3083611`  |
| 879    | Layout 1             | `fb27c3083611`  |
| 872    | Layout 1             | `fb27c3083611`  |
| 864    | Layout 1             | `fb27c3083611`  |
| 855    | Layout 1             | `fb27c3083611`  |
| 853    | Layout 1             | `fb27c3083611`  |
| 845    | Layout 1             | `fb27c3083611`  |
| 837    | Layout 1             | `fb27c3083611`  |
| 829    | Layout 1             | `fb27c3083611`  |
| 822    | Layout 1             | `fb27c3083611`  |
| 814    | Layout 1             | `fb27c3083611`  |
| 805    | Layout 1             | `fb27c3083611`  |
| 794    | No documented layout | `fb27c3083611`  |
| 787    | No documented layout | `fb27c3083611`  |
| 780    | No documented layout | `fb27c3083611`  |
| 771    | No documented layout | `fb27c3083611`  |
| 760    | No documented layout | `fb27c3083611`  |
| 748    | No documented layout | `fb27c3083611`  |
| 741    | No documented layout | `fb27c3083611`  |
| 736    | No documented layout | `fb27c3083611`  |
| 731    | No documented layout | `fb27c3083611`  |
| 723    | No documented layout | `fb27c3083611`  |
| 711    | No documented layout | `fb27c3083611`  |
| 707    | No documented layout | `fb27c3083611`  |
| 697    | No documented layout | `fb27c3083611`  |
| 689    | No documented layout | `fb27c3083611`  |
| 683    | No documented layout | `fb27c3083611`  |
| 678    | No file              | `fb27c3083611`  |
| 670    | No file              | `fb27c3083611`  |
| 661    | No file              | `fb27c3083611`  |
| 656    | No file              | `fb27c3083611`  |
| 652    | No file              | `fb27c3083611`  |
| 643    | No file              | `fb27c3083611`  |
| 637    | No file              | `fb27c3083611`  |
| 630    | No file              | `fb27c3083611`  |
| 627    | No file              | `fb27c3083611`  |
| 621    | No file              | `fb27c3083611`  |
| 617    | No file              | `fb27c3083611`  |
| 615    | No file              | `fb27c3083611`  |
| 606    | No file              | `fb27c3083611`  |
| 599    | No file              | `fb27c3083611`  |
| 592    | No file              | `fb27c3083611`  |
| 586    | No file              | `fb27c3083611`  |
| 577    | No file              | `fb27c3083611`  |
| 569    | No file              | `fb27c3083611`  |
| 561    | No file              | `fb27c3083611`  |
| 554    | No file              | `fb27c3083611`  |
| 542    | No file              | `fb27c3083611`  |
| 532    | No file              | `fb27c3083611`  |
| 531    | No file              | `fb27c3083611`  |
| 526    | No file              | `fb27c3083611`  |
| 521    | No file              | `fb27c3083611`  |
| 517    | No file              | `fb27c3083611`  |
| 510    | No file              | `fb27c3083611`  |
| 508    | No file              | `fb27c3083611`  |
| 504    | No file              | `fb27c3083611`  |
| 497    | No file              | `fb27c3083611`  |
| 491    | No file              | `fb27c3083611`  |
| 485    | No file              | `fb27c3083611`  |
| 478    | No file              | `fb27c3083611`  |
| 472    | No file              | `fb27c3083611`  |
| 466    | No file              | `fb27c3083611`  |
| 457    | No file              | `fb27c3083611`  |
| 452    | No file              | `fb27c3083611`  |
| 449    | No file              | `fb27c3083611`  |
| 435    | No file              | `fb27c3083611`  |

<!-- versions:end -->

## Companion Files

The format is self-contained; there is no `fairyupgraderateoffset.dbss`.

| File                    | Required | Role                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| `languagedata_en.loc`   | Optional | Item name for `item_id` (`str_type=0`, `str_id1=item_id`)    |
| `fairyfeedingitem.dbss` | Optional | Full fairy feeding item list ([fairyfeedingitem](../dbss/fairyfeedingitem_dbss.md)); contains both `item_id` values |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type          | Field          | Notes                                         |
| ------------------- | ------------- | -------------- | --------------------------------------------- |
| `+0x00`             | char[4]       | magic          | `PABR` (ASCII)                                |
| `+0x04`             | u32           | count          | Number of records; observed 3                 |
| `+0x08`             | Record[count] | records        | Variable-length records, back to back         |
| `records+0x00`      | String Table  | string_table   | The PABR string table, here with no strings   |
| `string_table+0x00` | u32           | end_of_records | Byte offset just past the last record; observed 131 |
| `string_table+0x04` | u32           | zero           | Always `0`                                    |

Observed file size is 143 bytes: 8-byte header, 3 × 41-byte records, 12-byte trailer.

The 12-byte trailer (`string_table`, `end_of_records`, `zero`) follows the
last record, the same trailer shape used by
[zodiacsignindex.bss](zodiacsignindex_bss.md).

`end_of_records` is authoritative for where the record stream stops; parse
records until that offset rather than assuming a fixed record size.

### Record (variable: 9 bytes + entries)

One record per grade transition, in ascending grade order.

| Offset  | Type               | Field            | Observed | Notes                                        |
| ------- | ------------------ | ---------------- | -------- | -------------------------------------------- |
| `+0x00` | u8                 | unknown_00       | 0        | Zero in all three records                    |
| `+0x01` | u32                | success_cap_ppm  | 1000000  | 100% success, and the cap on accumulated rate |
| `+0x05` | u32                | entry_count      | 2        | Number of item entries that follow           |
| `+0x09` | Entry[entry_count] | entries          |          | `entry_count` × 16-byte entries              |

Records carry no explicit key; the upgrade step is the record index.

Earlier versions of this doc called `unknown_00` `unknown_lead`.

### Entry (16 bytes)

One entry per item type that can be used for this Sprouting step. Only one item
type may be used per attempt; the entries are alternatives, not a combined pool.

| Offset  | Type | Field         | Notes                                                              |
| ------- | ---- | ------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_id       | Fairy-growth item consumed; LOC `str_type=0`, `str_id1=item_id`    |
| `+0x04` | u32  | rate_ppm      | Success chance added by **one** item, out of `success_cap_ppm`     |
| `+0x08` | u32  | items_for_max | Item count that reaches the 100% cap; also the per-attempt maximum |
| `+0x0C` | u32  | unknown_0c    | Zero in all observed entries                                       |

Success chance for `n` items is `min(n × rate_ppm, success_cap_ppm)`, with `n`
capped at `items_for_max`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Observed | Notes       |
| ------- | ------------------ | ------------ | -------- | ----------- |
| `+0x00` | u32                | string_count | 0        | Always zero |
| `+0x04` | pstr[string_count] | strings      |          | Empty       |

Earlier versions of this doc called `string_count` the trailer's `unknown_00`
and `zero` its `unknown_08`.

## Item IDs

| item_id | English name              |
| ------- | ------------------------- |
| 18448   | Ornette's Dark Honey Wine |
| 54030   | Sweet Honey Wine          |

These are the only two items in `languagedata_en.loc` whose tooltip says the
item can be used to _grow your Fairy_, and both appear in `fairyfeedingitem.dbss`.

Item icons are derived from the item ID as
`ui_texture/icon/new_icon/product_icon_png/{item_id:08d}.png`. Each item also has
a `.dds` icon, but those sit in per-category folders that differ per item
(`03_etc/09_petitem/` for 54030, `09_cash/` for 18448) and are not derivable from
the ID. Item 18448 has no unprefixed PNG, only a `web_`-prefixed one; the preview
icon resolver falls back to that sibling, so the canonical path is still correct.

## Decoded Table

Record index is the ascending grade transition, using the grade order
established in [fairyequipskillaquire.dbss](../dbss/fairyequipskillaquire_dbss.md)
(Faint → Glimmering → Brilliant → Radiant, tiers 1–4).

| Record | Upgrade step                     | Sweet Honey Wine         | Ornette's Dark Honey Wine |
| ------ | -------------------------------- | ------------------------ | ------------------------- |
| 0      | Faint → Glimmering (T1 → T2)     | 2.2222% each, 45 for max | 33.3333% each, 3 for max  |
| 1      | Glimmering → Brilliant (T2 → T3) | 0.6666% each, 150 for max | 10.0000% each, 10 for max |
| 2      | Brilliant → Radiant (T3 → T4)    | 0.2500% each, 400 for max | 4.0000% each, 25 for max  |

Record 2 matches the published Tier 3 → Tier 4 cost of 400 Sweet Honey Wine or
25 Ornette's Dark Honey Wine for a guaranteed Sprout, which fixes both the record
order and the meaning of `items_for_max`.

Ornette's Dark Honey Wine is worth exactly 15× Sweet Honey Wine at the first two
steps and 16× at the last.

## Notes

- Sprouting may only be attempted once per fairy unless a rebirth is used, and a
  successful Sprout resets the fairy's skills, which are then rerolled from
  `fairyequipskillaquire.dbss` at the new grade.
- A fairy can only Sprout at its tier's level cap, which community guides give as
  10 for Faint, 20 for Glimmering, 30 for Brilliant, and 50 for Radiant. Those
  caps are not stored in this file.
- A failed Sprout consumes the fairy's single attempt permanently; the only way
  back is a cash-shop Rebirth. That makes `items_for_max` the practically
  relevant column: players push to the 100% cost rather than gamble on
  `rate_ppm`, because there is no second roll to fall back on.
- `success_cap_ppm` is `1,000,000` in every record, the same parts-per-million
  convention already confirmed for `fairyequipskillaquire.dbss` and
  `petequipskillaquire.dbss`.
- Unlike the aquire tables, rates here do **not** sum to the cap across entries:
  the two entries are mutually exclusive item choices, each with its own
  per-item contribution.
- `items_for_max × rate_ppm` slightly undershoots the cap in three of six entries
  (`45 × 22222 = 999,990`, `150 × 6666 = 999,900`, `3 × 333333 = 999,999`), so
  `items_for_max` is a stored rounded-up count rather than an exact division.
  A parser should use the stored value, not a computed one.
- Records are self-describing through `entry_count`, so a parser must not assume
  the observed 41-byte record size.
- Framing check: leading-byte framing is the only one that fits. With a trailing
  byte per record the third record would end at 132, one byte past the
  `end_of_records` value of 131.
- [fairyfeedenchantfailcount.bss](fairyfeedenchantfailcount_bss.md) sits next to
  this file in the PAZ tree; its layout is decoded but no field meaning is
  confirmed, so a link to Sprouting is not established.
- Observed: 3 records and 6 entries in the pre-2026-09-27 fixture and in the
  2026-09-27 client; the file is byte-identical between the two.

## Open Questions

### `unknown_00` Meaning

The first byte of every record is zero. It may be a record type tag, a grade key
that happens to be zero-based, or padding carried from the writer. Only a file
where it varies would distinguish these.

### Rebirth Interaction

Sprouting can be retried after a rebirth, but nothing in this file encodes a
retry allowance, a rebirth cost, or a changed rate on a retry. Those values live
elsewhere; the fairy potion tables are the nearest candidate.
[fairyfeedenchantfailcount.bss](fairyfeedenchantfailcount_bss.md) is the
equipment feeding table of the `FairyFeed_Table` sheet and holds none of them.
