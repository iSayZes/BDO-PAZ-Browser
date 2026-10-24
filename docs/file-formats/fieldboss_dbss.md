# `fieldboss.dbss` Format

## Purpose

A list of character IDs, one per row, under the name "field boss". On client
3464 the 694 rows are world bosses (Garmoth, Karanda, Vell), field, node and
guild boss variants, event bosses, Atoraxion and Hadum bosses, and a few
characters that are not bosses by name: the GM war summons (`8996` Shadow
Knight, `8997` Ogre, `8998` Muraka) and `59670` Military Supply Wagon. Every
ID exists in `characterstatic.dbss`. Besides the ID, a row holds only two
bytes that are `1` on every row.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes  | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ------ | ------------- | --------- |
| 2      | 2726 and later | 3483    | `fieldboss.dbss`       | 22,906 | 694 Row       | 33        |
| 2      | 2726 and later | 3483    | `fieldbossoffset.dbss` | 6,944  | 694 Index Row | 10        |
| 1      | 1636 to 2717   | 2717    | `fieldboss.dbss`       | 20,588 | 664 Row       | 31        |
| 1      | 1636 to 2717   | 2717    | `fieldbossoffset.dbss` | 6,644  | 664 Index Row | 10        |

| Layout | File                   | Known            | Unknown          |
| ------ | ---------------------- | ---------------- | ---------------- |
| 2      | `fieldboss.dbss`       | 2,780 B (12.1%)  | 20,126 B (87.9%) |
| 2      | `fieldbossoffset.dbss` | 6,944 B (100.0%) | 0 B (0.0%)       |
| 1      | `fieldboss.dbss`       | 2,660 B (12.9%)  | 17,928 B (87.1%) |
| 1      | `fieldbossoffset.dbss` | 6,644 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `cb96527605f9`  |
| 3482   | Layout 2             | `cb96527605f9`  |
| 3474   | Layout 2             | `cb96527605f9`  |
| 3473   | Layout 2             | `cb96527605f9`  |
| 3464   | Layout 2             | `cb96527605f9`  |
| 3458   | Layout 2             | `cb96527605f9`  |
| 3454   | Layout 2             | `cb96527605f9`  |
| 3444   | Layout 2             | `cb96527605f9`  |
| 3435   | Layout 2             | `cb96527605f9`  |
| 3426   | Layout 2             | `cb96527605f9`  |
| 3418   | Layout 2             | `cb96527605f9`  |
| 3412   | Layout 2             | `cb96527605f9`  |
| 3402   | Layout 2             | `cb96527605f9`  |
| 3396   | Layout 2             | `cb96527605f9`  |
| 3387   | Layout 2             | `cb96527605f9`  |
| 3381   | Layout 2             | `cb96527605f9`  |
| 3373   | Layout 2             | `cb96527605f9`  |
| 3364   | Layout 2             | `cb96527605f9`  |
| 3356   | Layout 2             | `cb96527605f9`  |
| 3349   | Layout 2             | `cb96527605f9`  |
| 3342   | Layout 2             | `cb96527605f9`  |
| 3335   | Layout 2             | `cb96527605f9`  |
| 3326   | Layout 2             | `cb96527605f9`  |
| 3321   | Layout 2             | `cb96527605f9`  |
| 3314   | Layout 2             | `cb96527605f9`  |
| 3303   | Layout 2             | `cb96527605f9`  |
| 3302   | Layout 2             | `cb96527605f9`  |
| 3293   | Layout 2             | `cb96527605f9`  |
| 3283   | Layout 2             | `cb96527605f9`  |
| 3275   | Layout 2             | `cb96527605f9`  |
| 3267   | Layout 2             | `cb96527605f9`  |
| 3258   | Layout 2             | `cb96527605f9`  |
| 3251   | Layout 2             | `cb96527605f9`  |
| 3242   | Layout 2             | `cb96527605f9`  |
| 3235   | Layout 2             | `cb96527605f9`  |
| 3229   | Layout 2             | `cb96527605f9`  |
| 3212   | Layout 2             | `cb96527605f9`  |
| 3203   | Layout 2             | `cb96527605f9`  |
| 3193   | Layout 2             | `cb96527605f9`  |
| 3186   | Layout 2             | `cb96527605f9`  |
| 3177   | Layout 2             | `cb96527605f9`  |
| 3169   | Layout 2             | `cb96527605f9`  |
| 3158   | Layout 2             | `cb96527605f9`  |
| 3151   | Layout 2             | `cb96527605f9`  |
| 3144   | Layout 2             | `cb96527605f9`  |
| 3133   | Layout 2             | `cb96527605f9`  |
| 3125   | Layout 2             | `cb96527605f9`  |
| 3118   | Layout 2             | `cb96527605f9`  |
| 3111   | Layout 2             | `cb96527605f9`  |
| 3103   | Layout 2             | `cb96527605f9`  |
| 3095   | Layout 2             | `cb96527605f9`  |
| 3086   | Layout 2             | `cb96527605f9`  |
| 3072   | Layout 2             | `cb96527605f9`  |
| 3062   | Layout 2             | `cb96527605f9`  |
| 3052   | Layout 2             | `cb96527605f9`  |
| 3045   | Layout 2             | `cb96527605f9`  |
| 3037   | Layout 2             | `cb96527605f9`  |
| 3030   | Layout 2             | `cb96527605f9`  |
| 3021   | Layout 2             | `cb96527605f9`  |
| 3012   | Layout 2             | `cb96527605f9`  |
| 3002   | Layout 2             | `cb96527605f9`  |
| 2995   | Layout 2             | `cb96527605f9`  |
| 2987   | Layout 2             | `cb96527605f9`  |
| 2978   | Layout 2             | `cb96527605f9`  |
| 2970   | Layout 2             | `cb96527605f9`  |
| 2959   | Layout 2             | `cb96527605f9`  |
| 2951   | Layout 2             | `cb96527605f9`  |
| 2942   | Layout 2             | `cb96527605f9`  |
| 2935   | Layout 2             | `cb96527605f9`  |
| 2932   | Layout 2             | `cb96527605f9`  |
| 2923   | Layout 2             | `cb96527605f9`  |
| 2919   | Layout 2             | `cb96527605f9`  |
| 2907   | Layout 2             | `cb96527605f9`  |
| 2900   | Layout 2             | `cb96527605f9`  |
| 2891   | Layout 2             | `cb96527605f9`  |
| 2882   | Layout 2             | `cb96527605f9`  |
| 2872   | Layout 2             | `cb96527605f9`  |
| 2863   | Layout 2             | `cb96527605f9`  |
| 2855   | Layout 2             | `cb96527605f9`  |
| 2849   | Layout 2             | `cb96527605f9`  |
| 2844   | Layout 2             | `cb96527605f9`  |
| 2834   | Layout 2             | `cb96527605f9`  |
| 2825   | Layout 2             | `cb96527605f9`  |
| 2819   | Layout 2             | `cb96527605f9`  |
| 2811   | Layout 2             | `cb96527605f9`  |
| 2803   | Layout 2             | `cb96527605f9`  |
| 2794   | Layout 2             | `cb96527605f9`  |
| 2783   | Layout 2             | `cb96527605f9`  |
| 2774   | Layout 2             | `cb96527605f9`  |
| 2765   | Layout 2             | `cb96527605f9`  |
| 2756   | Layout 2             | `cb96527605f9`  |
| 2750   | Layout 2             | `cb96527605f9`  |
| 2743   | Layout 2             | `cb96527605f9`  |
| 2736   | Layout 2             | `cb96527605f9`  |
| 2726   | Layout 2             | `cb96527605f9`  |
| 2717   | Layout 1             | `cb96527605f9`  |
| 2709   | Layout 1             | `cb96527605f9`  |
| 2703   | Layout 1             | `cb96527605f9`  |
| 2695   | Layout 1             | `cb96527605f9`  |
| 2684   | Layout 1             | `cb96527605f9`  |
| 2672   | Layout 1             | `cb96527605f9`  |
| 2665   | Layout 1             | `cb96527605f9`  |
| 2657   | Layout 1             | `cb96527605f9`  |
| 2649   | Layout 1             | `cb96527605f9`  |
| 2644   | Layout 1             | `cb96527605f9`  |
| 2637   | Layout 1             | `cb96527605f9`  |
| 2629   | Layout 1             | `cb96527605f9`  |
| 2619   | Layout 1             | `cb96527605f9`  |
| 2612   | Layout 1             | `cb96527605f9`  |
| 2606   | Layout 1             | `cb96527605f9`  |
| 2602   | Layout 1             | `cb96527605f9`  |
| 2601   | Layout 1             | `cb96527605f9`  |
| 2592   | Layout 1             | `cb96527605f9`  |
| 2583   | Layout 1             | `cb96527605f9`  |
| 2575   | Layout 1             | `cb96527605f9`  |
| 2567   | Layout 1             | `cb96527605f9`  |
| 2560   | Layout 1             | `cb96527605f9`  |
| 2553   | Layout 1             | `cb96527605f9`  |
| 2545   | Layout 1             | `cb96527605f9`  |
| 2538   | Layout 1             | `cb96527605f9`  |
| 2529   | Layout 1             | `cb96527605f9`  |
| 2519   | Layout 1             | `cb96527605f9`  |
| 2513   | Layout 1             | `cb96527605f9`  |
| 2510   | Layout 1             | `cb96527605f9`  |
| 2507   | Layout 1             | `cb96527605f9`  |
| 2503   | Layout 1             | `cb96527605f9`  |
| 2498   | Layout 1             | `cb96527605f9`  |
| 2492   | Layout 1             | `cb96527605f9`  |
| 2487   | Layout 1             | `cb96527605f9`  |
| 2480   | Layout 1             | `cb96527605f9`  |
| 2474   | Layout 1             | `cb96527605f9`  |
| 2468   | Layout 1             | `cb96527605f9`  |
| 2460   | Layout 1             | `cb96527605f9`  |
| 2453   | Layout 1             | `cb96527605f9`  |
| 2444   | Layout 1             | `cb96527605f9`  |
| 2438   | Layout 1             | `cb96527605f9`  |
| 2434   | Layout 1             | `cb96527605f9`  |
| 2429   | Layout 1             | `cb96527605f9`  |
| 2421   | Layout 1             | `cb96527605f9`  |
| 2414   | Layout 1             | `cb96527605f9`  |
| 2407   | Layout 1             | `cb96527605f9`  |
| 2401   | Layout 1             | `cb96527605f9`  |
| 2397   | Layout 1             | `cb96527605f9`  |
| 2393   | Layout 1             | `cb96527605f9`  |
| 2384   | Layout 1             | `cb96527605f9`  |
| 2378   | Layout 1             | `cb96527605f9`  |
| 2372   | Layout 1             | `cb96527605f9`  |
| 2358   | Layout 1             | `cb96527605f9`  |
| 2352   | Layout 1             | `cb96527605f9`  |
| 2347   | Layout 1             | `cb96527605f9`  |
| 2343   | Layout 1             | `cb96527605f9`  |
| 2335   | Layout 1             | `cb96527605f9`  |
| 2327   | Layout 1             | `cb96527605f9`  |
| 2324   | Layout 1             | `cb96527605f9`  |
| 2319   | Layout 1             | `cb96527605f9`  |
| 2313   | Layout 1             | `cb96527605f9`  |
| 2308   | Layout 1             | `cb96527605f9`  |
| 2302   | Layout 1             | `cb96527605f9`  |
| 2295   | Layout 1             | `cb96527605f9`  |
| 2290   | Layout 1             | `cb96527605f9`  |
| 2284   | Layout 1             | `cb96527605f9`  |
| 2276   | Layout 1             | `cb96527605f9`  |
| 2269   | Layout 1             | `cb96527605f9`  |
| 2259   | Layout 1             | `cb96527605f9`  |
| 2250   | Layout 1             | `cb96527605f9`  |
| 2243   | Layout 1             | `cb96527605f9`  |
| 2235   | Layout 1             | `cb96527605f9`  |
| 2229   | Layout 1             | `cb96527605f9`  |
| 2224   | Layout 1             | `cb96527605f9`  |
| 2218   | Layout 1             | `cb96527605f9`  |
| 2215   | Layout 1             | `cb96527605f9`  |
| 2207   | Layout 1             | `cb96527605f9`  |
| 2203   | Layout 1             | `cb96527605f9`  |
| 2196   | Layout 1             | `cb96527605f9`  |
| 2192   | Layout 1             | `cb96527605f9`  |
| 2189   | Layout 1             | `cb96527605f9`  |
| 2183   | Layout 1             | `cb96527605f9`  |
| 2179   | Layout 1             | `cb96527605f9`  |
| 2171   | Layout 1             | `cb96527605f9`  |
| 2163   | Layout 1             | `cb96527605f9`  |
| 2156   | Layout 1             | `cb96527605f9`  |
| 2151   | Layout 1             | `cb96527605f9`  |
| 2147   | Layout 1             | `cb96527605f9`  |
| 2142   | Layout 1             | `cb96527605f9`  |
| 2138   | Layout 1             | `cb96527605f9`  |
| 2134   | Layout 1             | `cb96527605f9`  |
| 2130   | Layout 1             | `cb96527605f9`  |
| 2122   | Layout 1             | `cb96527605f9`  |
| 2107   | Layout 1             | `cb96527605f9`  |
| 2098   | Layout 1             | `cb96527605f9`  |
| 2089   | Layout 1             | `cb96527605f9`  |
| 2081   | Layout 1             | `cb96527605f9`  |
| 2073   | Layout 1             | `cb96527605f9`  |
| 2067   | Layout 1             | `cb96527605f9`  |
| 2063   | Layout 1             | `cb96527605f9`  |
| 2059   | Layout 1             | `cb96527605f9`  |
| 2052   | Layout 1             | `cb96527605f9`  |
| 2044   | Layout 1             | `cb96527605f9`  |
| 2039   | Layout 1             | `cb96527605f9`  |
| 2032   | Layout 1             | `cb96527605f9`  |
| 2025   | Layout 1             | `cb96527605f9`  |
| 2011   | Layout 1             | `cb96527605f9`  |
| 2005   | Layout 1             | `cb96527605f9`  |
| 2000   | Layout 1             | `cb96527605f9`  |
| 1996   | Layout 1             | `cb96527605f9`  |
| 1991   | Layout 1             | `cb96527605f9`  |
| 1985   | Layout 1             | `cb96527605f9`  |
| 1980   | Layout 1             | `cb96527605f9`  |
| 1969   | Layout 1             | `cb96527605f9`  |
| 1964   | Layout 1             | `cb96527605f9`  |
| 1958   | Layout 1             | `cb96527605f9`  |
| 1950   | Layout 1             | `cb96527605f9`  |
| 1945   | Layout 1             | `cb96527605f9`  |
| 1937   | Layout 1             | `cb96527605f9`  |
| 1933   | Layout 1             | `cb96527605f9`  |
| 1927   | Layout 1             | `cb96527605f9`  |
| 1921   | Layout 1             | `cb96527605f9`  |
| 1914   | Layout 1             | `cb96527605f9`  |
| 1908   | Layout 1             | `cb96527605f9`  |
| 1897   | Layout 1             | `cb96527605f9`  |
| 1892   | Layout 1             | `cb96527605f9`  |
| 1886   | Layout 1             | `cb96527605f9`  |
| 1881   | Layout 1             | `cb96527605f9`  |
| 1871   | Layout 1             | `cb96527605f9`  |
| 1866   | Layout 1             | `cb96527605f9`  |
| 1862   | Layout 1             | `cb96527605f9`  |
| 1854   | Layout 1             | `cb96527605f9`  |
| 1846   | Layout 1             | `cb96527605f9`  |
| 1838   | Layout 1             | `cb96527605f9`  |
| 1832   | Layout 1             | `cb96527605f9`  |
| 1826   | Layout 1             | `cb96527605f9`  |
| 1822   | Layout 1             | `cb96527605f9`  |
| 1818   | Layout 1             | `cb96527605f9`  |
| 1804   | Layout 1             | `cb96527605f9`  |
| 1794   | Layout 1             | `cb96527605f9`  |
| 1790   | Layout 1             | `cb96527605f9`  |
| 1784   | Layout 1             | `cb96527605f9`  |
| 1774   | Layout 1             | `cb96527605f9`  |
| 1771   | Layout 1             | `cb96527605f9`  |
| 1762   | Layout 1             | `cb96527605f9`  |
| 1759   | Layout 1             | `cb96527605f9`  |
| 1754   | Layout 1             | `cb96527605f9`  |
| 1749   | Layout 1             | `cb96527605f9`  |
| 1743   | Layout 1             | `cb96527605f9`  |
| 1737   | Layout 1             | `cb96527605f9`  |
| 1731   | Layout 1             | `cb96527605f9`  |
| 1725   | Layout 1             | `cb96527605f9`  |
| 1717   | Layout 1             | `cb96527605f9`  |
| 1710   | Layout 1             | `cb96527605f9`  |
| 1704   | Layout 1             | `cb96527605f9`  |
| 1698   | Layout 1             | `cb96527605f9`  |
| 1690   | Layout 1             | `cb96527605f9`  |
| 1685   | Layout 1             | `cb96527605f9`  |
| 1680   | Layout 1             | `cb96527605f9`  |
| 1674   | Layout 1             | `cb96527605f9`  |
| 1668   | Layout 1             | `cb96527605f9`  |
| 1659   | Layout 1             | `cb96527605f9`  |
| 1649   | Layout 1             | `cb96527605f9`  |
| 1642   | Layout 1             | `cb96527605f9`  |
| 1636   | Layout 1             | `cb96527605f9`  |
| 1628   | No documented layout | `cb96527605f9`  |
| 1622   | No documented layout | `cb96527605f9`  |
| 1614   | No documented layout | `cb96527605f9`  |
| 1608   | No documented layout | `cb96527605f9`  |
| 1602   | No documented layout | `cb96527605f9`  |
| 1598   | No documented layout | `cb96527605f9`  |
| 1594   | No documented layout | `cb96527605f9`  |
| 1590   | No documented layout | `cb96527605f9`  |
| 1587   | No documented layout | `cb96527605f9`  |
| 1584   | No documented layout | `cb96527605f9`  |
| 1579   | No documented layout | `cb96527605f9`  |
| 1572   | No documented layout | `cb96527605f9`  |
| 1565   | No documented layout | `cb96527605f9`  |
| 1559   | No documented layout | `cb96527605f9`  |
| 1554   | No documented layout | `cb96527605f9`  |
| 1547   | No documented layout | `cb96527605f9`  |
| 1537   | No documented layout | `cb96527605f9`  |
| 1529   | No documented layout | `cb96527605f9`  |
| 1524   | No documented layout | `cb96527605f9`  |
| 1519   | No documented layout | `cb96527605f9`  |
| 1509   | No documented layout | `cb96527605f9`  |
| 1506   | No documented layout | `cb96527605f9`  |
| 1504   | No documented layout | `cb96527605f9`  |
| 1500   | No documented layout | `cb96527605f9`  |
| 1493   | No documented layout | `cb96527605f9`  |
| 1489   | No documented layout | `cb96527605f9`  |
| 1485   | No documented layout | `cb96527605f9`  |
| 1481   | No documented layout | `cb96527605f9`  |
| 1474   | No documented layout | `cb96527605f9`  |
| 1466   | No documented layout | `cb96527605f9`  |
| 1462   | No documented layout | `cb96527605f9`  |
| 1459   | No documented layout | `cb96527605f9`  |
| 1453   | No documented layout | `cb96527605f9`  |
| 1450   | No documented layout | `cb96527605f9`  |
| 1445   | No documented layout | `cb96527605f9`  |
| 1439   | No documented layout | `cb96527605f9`  |
| 1433   | No documented layout | `cb96527605f9`  |
| 1430   | No documented layout | `cb96527605f9`  |
| 1426   | No documented layout | `cb96527605f9`  |
| 1421   | No documented layout | `cb96527605f9`  |
| 1417   | No documented layout | `cb96527605f9`  |
| 1416   | No documented layout | `cb96527605f9`  |
| 1409   | No documented layout | `cb96527605f9`  |
| 1405   | No documented layout | `cb96527605f9`  |
| 1401   | No documented layout | `cb96527605f9`  |
| 1396   | No documented layout | `cb96527605f9`  |
| 1391   | No documented layout | `cb96527605f9`  |
| 1390   | No documented layout | `cb96527605f9`  |
| 1386   | No documented layout | `cb96527605f9`  |
| 1381   | No documented layout | `cb96527605f9`  |
| 1379   | No documented layout | `cb96527605f9`  |
| 1372   | No documented layout | `cb96527605f9`  |
| 1366   | No documented layout | `cb96527605f9`  |
| 1364   | No documented layout | `cb96527605f9`  |
| 1363   | No documented layout | `cb96527605f9`  |
| 1360   | No documented layout | `cb96527605f9`  |
| 1358   | No documented layout | `cb96527605f9`  |
| 1355   | No documented layout | `cb96527605f9`  |
| 1351   | No documented layout | `cb96527605f9`  |
| 1348   | No documented layout | `cb96527605f9`  |
| 1346   | No documented layout | `cb96527605f9`  |
| 1341   | No documented layout | `cb96527605f9`  |
| 1340   | No documented layout | `cb96527605f9`  |
| 1338   | No documented layout | `cb96527605f9`  |
| 1335   | No documented layout | `cb96527605f9`  |
| 1333   | No documented layout | `cb96527605f9`  |
| 1329   | No documented layout | `cb96527605f9`  |
| 1327   | No documented layout | `cb96527605f9`  |
| 1324   | No documented layout | `cb96527605f9`  |
| 1321   | No documented layout | `cb96527605f9`  |
| 1319   | No documented layout | `cb96527605f9`  |
| 1318   | No documented layout | `cb96527605f9`  |
| 1316   | No documented layout | `cb96527605f9`  |
| 1313   | No documented layout | `cb96527605f9`  |
| 1311   | No documented layout | `cb96527605f9`  |
| 1309   | No documented layout | `cb96527605f9`  |
| 1304   | No documented layout | `cb96527605f9`  |
| 1292   | No documented layout | `cb96527605f9`  |
| 1286   | No documented layout | `cb96527605f9`  |
| 1280   | No documented layout | `cb96527605f9`  |
| 1276   | No documented layout | `cb96527605f9`  |
| 1267   | No file              | `cb96527605f9`  |
| 1261   | No file              | `cb96527605f9`  |
| 1256   | No file              | `cb96527605f9`  |
| 1250   | No file              | `cb96527605f9`  |
| 1246   | No file              | `cb96527605f9`  |
| 1239   | No file              | `cb96527605f9`  |
| 1230   | No file              | `cb96527605f9`  |
| 1226   | No file              | `cb96527605f9`  |
| 1220   | No file              | `cb96527605f9`  |
| 1217   | No file              | `cb96527605f9`  |
| 1211   | No file              | `cb96527605f9`  |
| 1210   | No file              | `cb96527605f9`  |
| 1208   | No file              | `cb96527605f9`  |
| 1203   | No file              | `cb96527605f9`  |
| 1197   | No file              | `cb96527605f9`  |
| 1194   | No file              | `cb96527605f9`  |
| 1192   | No file              | `cb96527605f9`  |
| 1187   | No file              | `cb96527605f9`  |
| 1183   | No file              | `cb96527605f9`  |
| 1177   | No file              | `cb96527605f9`  |
| 1173   | No file              | `cb96527605f9`  |
| 1167   | No file              | `cb96527605f9`  |
| 1164   | No file              | `cb96527605f9`  |
| 1156   | No file              | `cb96527605f9`  |
| 1149   | No file              | `cb96527605f9`  |
| 1144   | No file              | `cb96527605f9`  |
| 1137   | No file              | `cb96527605f9`  |
| 1132   | No file              | `cb96527605f9`  |
| 1127   | No file              | `cb96527605f9`  |
| 1122   | No file              | `cb96527605f9`  |
| 1118   | No file              | `cb96527605f9`  |
| 1114   | No file              | `cb96527605f9`  |
| 1109   | No file              | `cb96527605f9`  |
| 1102   | No file              | `cb96527605f9`  |
| 1096   | No file              | `cb96527605f9`  |
| 1088   | No file              | `cb96527605f9`  |
| 1081   | No file              | `cb96527605f9`  |
| 1076   | No file              | `cb96527605f9`  |
| 1069   | No file              | `cb96527605f9`  |
| 1064   | No file              | `cb96527605f9`  |
| 1058   | No file              | `cb96527605f9`  |
| 1051   | No file              | `cb96527605f9`  |
| 1044   | No file              | `cb96527605f9`  |
| 1036   | No file              | `cb96527605f9`  |
| 1026   | No file              | `cb96527605f9`  |
| 1016   | No file              | `cb96527605f9`  |
| 1009   | No file              | `cb96527605f9`  |
| 1005   | No file              | `cb96527605f9`  |
| 1000   | No file              | `cb96527605f9`  |
| 998    | No file              | `cb96527605f9`  |
| 990    | No file              | `cb96527605f9`  |
| 979    | No file              | `cb96527605f9`  |
| 972    | No file              | `cb96527605f9`  |
| 963    | No file              | `cb96527605f9`  |
| 955    | No file              | `cb96527605f9`  |
| 946    | No file              | `cb96527605f9`  |
| 938    | No file              | `cb96527605f9`  |
| 927    | No file              | `cb96527605f9`  |
| 911    | No file              | `cb96527605f9`  |
| 904    | No file              | `cb96527605f9`  |
| 899    | No file              | `cb96527605f9`  |
| 894    | No file              | `cb96527605f9`  |
| 885    | No file              | `cb96527605f9`  |
| 879    | No file              | `cb96527605f9`  |
| 872    | No file              | `cb96527605f9`  |
| 864    | No file              | `cb96527605f9`  |
| 855    | No file              | `cb96527605f9`  |
| 853    | No file              | `cb96527605f9`  |
| 845    | No file              | `cb96527605f9`  |
| 837    | No file              | `cb96527605f9`  |
| 829    | No file              | `cb96527605f9`  |
| 822    | No file              | `cb96527605f9`  |
| 814    | No file              | `cb96527605f9`  |
| 805    | No file              | `cb96527605f9`  |
| 794    | No file              | `cb96527605f9`  |
| 787    | No file              | `cb96527605f9`  |
| 780    | No file              | `cb96527605f9`  |
| 771    | No file              | `cb96527605f9`  |
| 760    | No file              | `cb96527605f9`  |
| 748    | No file              | `cb96527605f9`  |
| 741    | No file              | `cb96527605f9`  |
| 736    | No file              | `cb96527605f9`  |
| 731    | No file              | `cb96527605f9`  |
| 723    | No file              | `cb96527605f9`  |
| 711    | No file              | `cb96527605f9`  |
| 707    | No file              | `cb96527605f9`  |
| 697    | No file              | `cb96527605f9`  |
| 689    | No file              | `cb96527605f9`  |
| 683    | No file              | `cb96527605f9`  |
| 678    | No file              | `cb96527605f9`  |
| 670    | No file              | `cb96527605f9`  |
| 661    | No file              | `cb96527605f9`  |
| 656    | No file              | `cb96527605f9`  |
| 652    | No file              | `cb96527605f9`  |
| 643    | No file              | `cb96527605f9`  |
| 637    | No file              | `cb96527605f9`  |
| 630    | No file              | `cb96527605f9`  |
| 627    | No file              | `cb96527605f9`  |
| 621    | No file              | `cb96527605f9`  |
| 617    | No file              | `cb96527605f9`  |
| 615    | No file              | `cb96527605f9`  |
| 606    | No file              | `cb96527605f9`  |
| 599    | No file              | `cb96527605f9`  |
| 592    | No file              | `cb96527605f9`  |
| 586    | No file              | `cb96527605f9`  |
| 577    | No file              | `cb96527605f9`  |
| 569    | No file              | `cb96527605f9`  |
| 561    | No file              | `cb96527605f9`  |
| 554    | No file              | `cb96527605f9`  |
| 542    | No file              | `cb96527605f9`  |
| 532    | No file              | `cb96527605f9`  |
| 531    | No file              | `cb96527605f9`  |
| 526    | No file              | `cb96527605f9`  |
| 521    | No file              | `cb96527605f9`  |
| 517    | No file              | `cb96527605f9`  |
| 510    | No file              | `cb96527605f9`  |
| 508    | No file              | `cb96527605f9`  |
| 504    | No file              | `cb96527605f9`  |
| 497    | No file              | `cb96527605f9`  |
| 491    | No file              | `cb96527605f9`  |
| 485    | No file              | `cb96527605f9`  |
| 478    | No file              | `cb96527605f9`  |
| 472    | No file              | `cb96527605f9`  |
| 466    | No file              | `cb96527605f9`  |
| 457    | No file              | `cb96527605f9`  |
| 452    | No file              | `cb96527605f9`  |
| 449    | No file              | `cb96527605f9`  |
| 435    | No file              | `cb96527605f9`  |

<!-- versions:end -->

## Companion Files

None. The handler reads the rows in file order and does not need
`fieldbossoffset.dbss` (see below). Names and titles come from LOC type 6,
else the Korean `characterstatic.dbss` ones (`_common/character.py`).

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then 33-byte rows; the
file ends after the last row.

| Offset  | Type           | Field     | Notes                    |
| ------- | -------------- | --------- | ------------------------ |
| `+0x00` | u32            | row_count | `694` on client 3464     |
| `+0x04` | Row[row_count] | rows      | See Row                  |

### Row (33 bytes)

| Offset  | Type      | Field        | Notes                                              |
| ------- | --------- | ------------ | -------------------------------------------------- |
| `+0x00` | u16       | key          | Row key; equals `character_id` on every row        |
| `+0x02` | u8        | unknown_02   | `1` on every row                                   |
| `+0x03` | u16       | character_id | `characterstatic.dbss` character ID, LOC type 6    |
| `+0x05` | bytes[12] | unknown_05   | Zero on every row                                  |
| `+0x11` | u8        | unknown_11   | `1` on every row                                   |
| `+0x12` | bytes[15] | unknown_12   | Zero on every row                                  |

The `u8, u16 character_id, u16` head has the shape of the block after the
scripts in a `characterstatic.dbss` record (`unknown_p`, `character_id`,
`unknown_p3`), but the values differ: none of the 694 characters has
`unknown_p` set to `1` there.

### `fieldbossoffset.dbss`

A u32 row count (equal to the main file's), then 10-byte rows
(`parse_bare_offset_rows()`).

| Offset  | Type                 | Field     | Notes                              |
| ------- | -------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                      |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first one points at main row 0, the second
at main row 596).

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                                      |
| ------- | ---- | ------------ | ---------------------------------------------------------- |
| `+0x00` | u16  | character_id | Row key, the main row's `key`                              |
| `+0x02` | u32  | offset       | Start of the row in `fieldboss.dbss` plus 2, at `unknown_02` |
| `+0x06` | u32  | size         | Always `31`, the row size minus the 2-byte `key`           |

## Layout 1

On client 1784 the zero run at the end of the row is 13 bytes where Layout 2
has 15, so the row is 31 bytes and the index `size` is `29`. Only the Row
differs from Layout 2.

### Row (31 bytes)

| Offset  | Type      | Field        | Notes                          |
| ------- | --------- | ------------ | ------------------------------ |
| `+0x00` | u16       | key          |                                |
| `+0x02` | u8        | unknown_02   | `1` on every row (client 1784) |
| `+0x03` | u16       | character_id |                                |
| `+0x05` | bytes[12] | unknown_05   | Zero on every row (client 1784) |
| `+0x11` | u8        | unknown_11   | `1` on every row (client 1784) |
| `+0x12` | bytes[13] | unknown_12   | Zero on every row (client 1784) |

## Notes

- The client Lua never names this file. Its only field boss reference is the
  chat notice type `CppEnums.EChatNoticeType.FieldBoss = 13`
  (`global_define_cpp_enum`), which `noticealert` turns into a
  `__eNakMessage_FieldBoss` message.
- The list is not what the Boss Info window shows. That window
  (`panel_worldmap_bosslist_all`) reads each boss through
  `ToClient_getBossStaticStatus(index)` (character key, textures, position,
  next spawn time, reward items), which matches the records of
  [`bossinfostaicstatusmanager.bss`](bossinfostaicstatusmanager_bss.md), not
  this file. The five bosses of its
  Field tab (23069 Dastard Bheg, 23061 Red Nose, 23056 Dim Tree Spirit,
  23055 Giant Mudster, 23144 Katzvariak) are all on this list, but so are
  689 other characters, and 23809 Mirumok Destroyer Offin from the Boss
  Info file is not.
- The list is not every boss: `characterstatic.dbss` has 1,877 characters
  with `boss` in the model path on client 3464, and 319 of them are here.
  375 of the 694 rows have no `boss` in the model path, among them event
  monsters such as `29862` Mischievous Jack.

## Open Questions

### What the List Selects

The client code that reads the file is not in Lua, so it is not known what
being on the list does: a boss HP bar, the field boss chat notice, loot or
contribution rules, or something else. The GM summons and the Military Supply
Wagon rule out "named world and field bosses" as the whole answer, and the
Boss Info window's Field tab comes from another file (see Notes).

### unknown_02 and unknown_11

Both bytes are `1` on every row, so the data cannot tell flags from
constants. A future client with a `0` in either would show which.
