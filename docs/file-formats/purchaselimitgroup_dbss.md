# `purchaselimitgroup.dbss` Format

## Purpose

Purchase limits that several Pearl Shop products share. A product joins a
group through its `PurchaseGroupNo`, and the group's limit then counts the
purchases of every product in it together. One 9-byte row per group: the
group number, who the limit counts for (character or family) and how many
purchases it allows. Companion `purchaselimitgroupoffset.dbss` lists where
every row sits.

On client 1784 the `CashProduct_Table` sheet puts the four head maid and
butler contracts into the two groups: group `1` holds `[Head Storage
Butler] Sebastian` (`98225`) and `[Head Storage Maid] Cecilia` (`89412`),
group `2` holds `[Head Transaction Butler] Sebastian` (`89410`) and `[Head
Transaction Maid] Cecilia` (`89411`). Their English product descriptions
(LOC type 50) end with "Only one Head Storage Maid/Butler per Family" and
"Only one Head Transaction Maid/Butler per Family", which is what both rows
hold: one purchase per family.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | ------------ | --------- |
| 1      | 1649 and later | 3483    | `purchaselimitgroup.dbss`       | 22    | 2 Row        | 9         |
| 1      | 1649 and later | 3483    | `purchaselimitgroupoffset.dbss` | 28    | 2 Offset Row | 12        |

| Layout | File                            | Known         | Unknown    |
| ------ | ------------------------------- | ------------- | ---------- |
| 1      | `purchaselimitgroup.dbss`       | 22 B (100.0%) | 0 B (0.0%) |
| 1      | `purchaselimitgroupoffset.dbss` | 28 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `5b105d998e83`  |
| 3482   | Layout 1 | `5b105d998e83`  |
| 3474   | Layout 1 | `5b105d998e83`  |
| 3473   | Layout 1 | `5b105d998e83`  |
| 3464   | Layout 1 | `5b105d998e83`  |
| 3458   | Layout 1 | `5b105d998e83`  |
| 3454   | Layout 1 | `5b105d998e83`  |
| 3444   | Layout 1 | `5b105d998e83`  |
| 3435   | Layout 1 | `5b105d998e83`  |
| 3426   | Layout 1 | `5b105d998e83`  |
| 3418   | Layout 1 | `5b105d998e83`  |
| 3412   | Layout 1 | `5b105d998e83`  |
| 3402   | Layout 1 | `5b105d998e83`  |
| 3396   | Layout 1 | `5b105d998e83`  |
| 3387   | Layout 1 | `5b105d998e83`  |
| 3381   | Layout 1 | `5b105d998e83`  |
| 3373   | Layout 1 | `5b105d998e83`  |
| 3364   | Layout 1 | `5b105d998e83`  |
| 3356   | Layout 1 | `5b105d998e83`  |
| 3349   | Layout 1 | `5b105d998e83`  |
| 3342   | Layout 1 | `5b105d998e83`  |
| 3335   | Layout 1 | `5b105d998e83`  |
| 3326   | Layout 1 | `5b105d998e83`  |
| 3321   | Layout 1 | `5b105d998e83`  |
| 3314   | Layout 1 | `5b105d998e83`  |
| 3303   | Layout 1 | `5b105d998e83`  |
| 3302   | Layout 1 | `5b105d998e83`  |
| 3293   | Layout 1 | `5b105d998e83`  |
| 3283   | Layout 1 | `5b105d998e83`  |
| 3275   | Layout 1 | `5b105d998e83`  |
| 3267   | Layout 1 | `5b105d998e83`  |
| 3258   | Layout 1 | `5b105d998e83`  |
| 3251   | Layout 1 | `5b105d998e83`  |
| 3242   | Layout 1 | `5b105d998e83`  |
| 3235   | Layout 1 | `5b105d998e83`  |
| 3229   | Layout 1 | `5b105d998e83`  |
| 3212   | Layout 1 | `5b105d998e83`  |
| 3203   | Layout 1 | `5b105d998e83`  |
| 3193   | Layout 1 | `5b105d998e83`  |
| 3186   | Layout 1 | `5b105d998e83`  |
| 3177   | Layout 1 | `5b105d998e83`  |
| 3169   | Layout 1 | `5b105d998e83`  |
| 3158   | Layout 1 | `5b105d998e83`  |
| 3151   | Layout 1 | `5b105d998e83`  |
| 3144   | Layout 1 | `5b105d998e83`  |
| 3133   | Layout 1 | `5b105d998e83`  |
| 3125   | Layout 1 | `5b105d998e83`  |
| 3118   | Layout 1 | `5b105d998e83`  |
| 3111   | Layout 1 | `5b105d998e83`  |
| 3103   | Layout 1 | `5b105d998e83`  |
| 3095   | Layout 1 | `5b105d998e83`  |
| 3086   | Layout 1 | `5b105d998e83`  |
| 3072   | Layout 1 | `5b105d998e83`  |
| 3062   | Layout 1 | `5b105d998e83`  |
| 3052   | Layout 1 | `5b105d998e83`  |
| 3045   | Layout 1 | `5b105d998e83`  |
| 3037   | Layout 1 | `5b105d998e83`  |
| 3030   | Layout 1 | `5b105d998e83`  |
| 3021   | Layout 1 | `5b105d998e83`  |
| 3012   | Layout 1 | `5b105d998e83`  |
| 3002   | Layout 1 | `5b105d998e83`  |
| 2995   | Layout 1 | `5b105d998e83`  |
| 2987   | Layout 1 | `5b105d998e83`  |
| 2978   | Layout 1 | `5b105d998e83`  |
| 2970   | Layout 1 | `5b105d998e83`  |
| 2959   | Layout 1 | `5b105d998e83`  |
| 2951   | Layout 1 | `5b105d998e83`  |
| 2942   | Layout 1 | `5b105d998e83`  |
| 2935   | Layout 1 | `5b105d998e83`  |
| 2932   | Layout 1 | `5b105d998e83`  |
| 2923   | Layout 1 | `5b105d998e83`  |
| 2919   | Layout 1 | `5b105d998e83`  |
| 2907   | Layout 1 | `5b105d998e83`  |
| 2900   | Layout 1 | `5b105d998e83`  |
| 2891   | Layout 1 | `5b105d998e83`  |
| 2882   | Layout 1 | `5b105d998e83`  |
| 2872   | Layout 1 | `5b105d998e83`  |
| 2863   | Layout 1 | `5b105d998e83`  |
| 2855   | Layout 1 | `5b105d998e83`  |
| 2849   | Layout 1 | `5b105d998e83`  |
| 2844   | Layout 1 | `5b105d998e83`  |
| 2834   | Layout 1 | `5b105d998e83`  |
| 2825   | Layout 1 | `5b105d998e83`  |
| 2819   | Layout 1 | `5b105d998e83`  |
| 2811   | Layout 1 | `5b105d998e83`  |
| 2803   | Layout 1 | `5b105d998e83`  |
| 2794   | Layout 1 | `5b105d998e83`  |
| 2783   | Layout 1 | `5b105d998e83`  |
| 2774   | Layout 1 | `5b105d998e83`  |
| 2765   | Layout 1 | `5b105d998e83`  |
| 2756   | Layout 1 | `5b105d998e83`  |
| 2750   | Layout 1 | `5b105d998e83`  |
| 2743   | Layout 1 | `5b105d998e83`  |
| 2736   | Layout 1 | `5b105d998e83`  |
| 2726   | Layout 1 | `5b105d998e83`  |
| 2717   | Layout 1 | `5b105d998e83`  |
| 2709   | Layout 1 | `5b105d998e83`  |
| 2703   | Layout 1 | `5b105d998e83`  |
| 2695   | Layout 1 | `5b105d998e83`  |
| 2684   | Layout 1 | `5b105d998e83`  |
| 2672   | Layout 1 | `5b105d998e83`  |
| 2665   | Layout 1 | `5b105d998e83`  |
| 2657   | Layout 1 | `5b105d998e83`  |
| 2649   | Layout 1 | `5b105d998e83`  |
| 2644   | Layout 1 | `5b105d998e83`  |
| 2637   | Layout 1 | `5b105d998e83`  |
| 2629   | Layout 1 | `5b105d998e83`  |
| 2619   | Layout 1 | `5b105d998e83`  |
| 2612   | Layout 1 | `5b105d998e83`  |
| 2606   | Layout 1 | `5b105d998e83`  |
| 2602   | Layout 1 | `5b105d998e83`  |
| 2601   | Layout 1 | `5b105d998e83`  |
| 2592   | Layout 1 | `5b105d998e83`  |
| 2583   | Layout 1 | `5b105d998e83`  |
| 2575   | Layout 1 | `5b105d998e83`  |
| 2567   | Layout 1 | `5b105d998e83`  |
| 2560   | Layout 1 | `5b105d998e83`  |
| 2553   | Layout 1 | `5b105d998e83`  |
| 2545   | Layout 1 | `5b105d998e83`  |
| 2538   | Layout 1 | `5b105d998e83`  |
| 2529   | Layout 1 | `5b105d998e83`  |
| 2519   | Layout 1 | `5b105d998e83`  |
| 2513   | Layout 1 | `5b105d998e83`  |
| 2510   | Layout 1 | `5b105d998e83`  |
| 2507   | Layout 1 | `5b105d998e83`  |
| 2503   | Layout 1 | `5b105d998e83`  |
| 2498   | Layout 1 | `5b105d998e83`  |
| 2492   | Layout 1 | `5b105d998e83`  |
| 2487   | Layout 1 | `5b105d998e83`  |
| 2480   | Layout 1 | `5b105d998e83`  |
| 2474   | Layout 1 | `5b105d998e83`  |
| 2468   | Layout 1 | `5b105d998e83`  |
| 2460   | Layout 1 | `5b105d998e83`  |
| 2453   | Layout 1 | `5b105d998e83`  |
| 2444   | Layout 1 | `5b105d998e83`  |
| 2438   | Layout 1 | `5b105d998e83`  |
| 2434   | Layout 1 | `5b105d998e83`  |
| 2429   | Layout 1 | `5b105d998e83`  |
| 2421   | Layout 1 | `5b105d998e83`  |
| 2414   | Layout 1 | `5b105d998e83`  |
| 2407   | Layout 1 | `5b105d998e83`  |
| 2401   | Layout 1 | `5b105d998e83`  |
| 2397   | Layout 1 | `5b105d998e83`  |
| 2393   | Layout 1 | `5b105d998e83`  |
| 2384   | Layout 1 | `5b105d998e83`  |
| 2378   | Layout 1 | `5b105d998e83`  |
| 2372   | Layout 1 | `5b105d998e83`  |
| 2358   | Layout 1 | `5b105d998e83`  |
| 2352   | Layout 1 | `5b105d998e83`  |
| 2347   | Layout 1 | `5b105d998e83`  |
| 2343   | Layout 1 | `5b105d998e83`  |
| 2335   | Layout 1 | `5b105d998e83`  |
| 2327   | Layout 1 | `5b105d998e83`  |
| 2324   | Layout 1 | `5b105d998e83`  |
| 2319   | Layout 1 | `5b105d998e83`  |
| 2313   | Layout 1 | `5b105d998e83`  |
| 2308   | Layout 1 | `5b105d998e83`  |
| 2302   | Layout 1 | `5b105d998e83`  |
| 2295   | Layout 1 | `5b105d998e83`  |
| 2290   | Layout 1 | `5b105d998e83`  |
| 2284   | Layout 1 | `5b105d998e83`  |
| 2276   | Layout 1 | `5b105d998e83`  |
| 2269   | Layout 1 | `5b105d998e83`  |
| 2259   | Layout 1 | `5b105d998e83`  |
| 2250   | Layout 1 | `5b105d998e83`  |
| 2243   | Layout 1 | `5b105d998e83`  |
| 2235   | Layout 1 | `5b105d998e83`  |
| 2229   | Layout 1 | `5b105d998e83`  |
| 2224   | Layout 1 | `5b105d998e83`  |
| 2218   | Layout 1 | `5b105d998e83`  |
| 2215   | Layout 1 | `5b105d998e83`  |
| 2207   | Layout 1 | `5b105d998e83`  |
| 2203   | Layout 1 | `5b105d998e83`  |
| 2196   | Layout 1 | `5b105d998e83`  |
| 2192   | Layout 1 | `5b105d998e83`  |
| 2189   | Layout 1 | `5b105d998e83`  |
| 2183   | Layout 1 | `5b105d998e83`  |
| 2179   | Layout 1 | `5b105d998e83`  |
| 2171   | Layout 1 | `5b105d998e83`  |
| 2163   | Layout 1 | `5b105d998e83`  |
| 2156   | Layout 1 | `5b105d998e83`  |
| 2151   | Layout 1 | `5b105d998e83`  |
| 2147   | Layout 1 | `5b105d998e83`  |
| 2142   | Layout 1 | `5b105d998e83`  |
| 2138   | Layout 1 | `5b105d998e83`  |
| 2134   | Layout 1 | `5b105d998e83`  |
| 2130   | Layout 1 | `5b105d998e83`  |
| 2122   | Layout 1 | `5b105d998e83`  |
| 2107   | Layout 1 | `5b105d998e83`  |
| 2098   | Layout 1 | `5b105d998e83`  |
| 2089   | Layout 1 | `5b105d998e83`  |
| 2081   | Layout 1 | `5b105d998e83`  |
| 2073   | Layout 1 | `5b105d998e83`  |
| 2067   | Layout 1 | `5b105d998e83`  |
| 2063   | Layout 1 | `5b105d998e83`  |
| 2059   | Layout 1 | `5b105d998e83`  |
| 2052   | Layout 1 | `5b105d998e83`  |
| 2044   | Layout 1 | `5b105d998e83`  |
| 2039   | Layout 1 | `5b105d998e83`  |
| 2032   | Layout 1 | `5b105d998e83`  |
| 2025   | Layout 1 | `5b105d998e83`  |
| 2011   | Layout 1 | `5b105d998e83`  |
| 2005   | Layout 1 | `5b105d998e83`  |
| 2000   | Layout 1 | `5b105d998e83`  |
| 1996   | Layout 1 | `5b105d998e83`  |
| 1991   | Layout 1 | `5b105d998e83`  |
| 1985   | Layout 1 | `5b105d998e83`  |
| 1980   | Layout 1 | `5b105d998e83`  |
| 1969   | Layout 1 | `5b105d998e83`  |
| 1964   | Layout 1 | `5b105d998e83`  |
| 1958   | Layout 1 | `5b105d998e83`  |
| 1950   | Layout 1 | `5b105d998e83`  |
| 1945   | Layout 1 | `5b105d998e83`  |
| 1937   | Layout 1 | `5b105d998e83`  |
| 1933   | Layout 1 | `5b105d998e83`  |
| 1927   | Layout 1 | `5b105d998e83`  |
| 1921   | Layout 1 | `5b105d998e83`  |
| 1914   | Layout 1 | `5b105d998e83`  |
| 1908   | Layout 1 | `5b105d998e83`  |
| 1897   | Layout 1 | `5b105d998e83`  |
| 1892   | Layout 1 | `5b105d998e83`  |
| 1886   | Layout 1 | `5b105d998e83`  |
| 1881   | Layout 1 | `5b105d998e83`  |
| 1871   | Layout 1 | `5b105d998e83`  |
| 1866   | Layout 1 | `5b105d998e83`  |
| 1862   | Layout 1 | `5b105d998e83`  |
| 1854   | Layout 1 | `5b105d998e83`  |
| 1846   | Layout 1 | `5b105d998e83`  |
| 1838   | Layout 1 | `5b105d998e83`  |
| 1832   | Layout 1 | `5b105d998e83`  |
| 1826   | Layout 1 | `5b105d998e83`  |
| 1822   | Layout 1 | `5b105d998e83`  |
| 1818   | Layout 1 | `5b105d998e83`  |
| 1804   | Layout 1 | `5b105d998e83`  |
| 1794   | Layout 1 | `5b105d998e83`  |
| 1790   | Layout 1 | `5b105d998e83`  |
| 1784   | Layout 1 | `5b105d998e83`  |
| 1774   | Layout 1 | `5b105d998e83`  |
| 1771   | Layout 1 | `5b105d998e83`  |
| 1762   | Layout 1 | `5b105d998e83`  |
| 1759   | Layout 1 | `5b105d998e83`  |
| 1754   | Layout 1 | `5b105d998e83`  |
| 1749   | Layout 1 | `5b105d998e83`  |
| 1743   | Layout 1 | `5b105d998e83`  |
| 1737   | Layout 1 | `5b105d998e83`  |
| 1731   | Layout 1 | `5b105d998e83`  |
| 1725   | Layout 1 | `5b105d998e83`  |
| 1717   | Layout 1 | `5b105d998e83`  |
| 1710   | Layout 1 | `5b105d998e83`  |
| 1704   | Layout 1 | `5b105d998e83`  |
| 1698   | Layout 1 | `5b105d998e83`  |
| 1690   | Layout 1 | `5b105d998e83`  |
| 1685   | Layout 1 | `5b105d998e83`  |
| 1680   | Layout 1 | `5b105d998e83`  |
| 1674   | Layout 1 | `5b105d998e83`  |
| 1668   | Layout 1 | `5b105d998e83`  |
| 1659   | Layout 1 | `5b105d998e83`  |
| 1649   | Layout 1 | `5b105d998e83`  |
| 1642   | No file  | `5b105d998e83`  |
| 1636   | No file  | `5b105d998e83`  |
| 1628   | No file  | `5b105d998e83`  |
| 1622   | No file  | `5b105d998e83`  |
| 1614   | No file  | `5b105d998e83`  |
| 1608   | No file  | `5b105d998e83`  |
| 1602   | No file  | `5b105d998e83`  |
| 1598   | No file  | `5b105d998e83`  |
| 1594   | No file  | `5b105d998e83`  |
| 1590   | No file  | `5b105d998e83`  |
| 1587   | No file  | `5b105d998e83`  |
| 1584   | No file  | `5b105d998e83`  |
| 1579   | No file  | `5b105d998e83`  |
| 1572   | No file  | `5b105d998e83`  |
| 1565   | No file  | `5b105d998e83`  |
| 1559   | No file  | `5b105d998e83`  |
| 1554   | No file  | `5b105d998e83`  |
| 1547   | No file  | `5b105d998e83`  |
| 1537   | No file  | `5b105d998e83`  |
| 1529   | No file  | `5b105d998e83`  |
| 1524   | No file  | `5b105d998e83`  |
| 1519   | No file  | `5b105d998e83`  |
| 1509   | No file  | `5b105d998e83`  |
| 1506   | No file  | `5b105d998e83`  |
| 1504   | No file  | `5b105d998e83`  |
| 1500   | No file  | `5b105d998e83`  |
| 1493   | No file  | `5b105d998e83`  |
| 1489   | No file  | `5b105d998e83`  |
| 1485   | No file  | `5b105d998e83`  |
| 1481   | No file  | `5b105d998e83`  |
| 1474   | No file  | `5b105d998e83`  |
| 1466   | No file  | `5b105d998e83`  |
| 1462   | No file  | `5b105d998e83`  |
| 1459   | No file  | `5b105d998e83`  |
| 1453   | No file  | `5b105d998e83`  |
| 1450   | No file  | `5b105d998e83`  |
| 1445   | No file  | `5b105d998e83`  |
| 1439   | No file  | `5b105d998e83`  |
| 1433   | No file  | `5b105d998e83`  |
| 1430   | No file  | `5b105d998e83`  |
| 1426   | No file  | `5b105d998e83`  |
| 1421   | No file  | `5b105d998e83`  |
| 1417   | No file  | `5b105d998e83`  |
| 1416   | No file  | `5b105d998e83`  |
| 1409   | No file  | `5b105d998e83`  |
| 1405   | No file  | `5b105d998e83`  |
| 1401   | No file  | `5b105d998e83`  |
| 1396   | No file  | `5b105d998e83`  |
| 1391   | No file  | `5b105d998e83`  |
| 1390   | No file  | `5b105d998e83`  |
| 1386   | No file  | `5b105d998e83`  |
| 1381   | No file  | `5b105d998e83`  |
| 1379   | No file  | `5b105d998e83`  |
| 1372   | No file  | `5b105d998e83`  |
| 1366   | No file  | `5b105d998e83`  |
| 1364   | No file  | `5b105d998e83`  |
| 1363   | No file  | `5b105d998e83`  |
| 1360   | No file  | `5b105d998e83`  |
| 1358   | No file  | `5b105d998e83`  |
| 1355   | No file  | `5b105d998e83`  |
| 1351   | No file  | `5b105d998e83`  |
| 1348   | No file  | `5b105d998e83`  |
| 1346   | No file  | `5b105d998e83`  |
| 1341   | No file  | `5b105d998e83`  |
| 1340   | No file  | `5b105d998e83`  |
| 1338   | No file  | `5b105d998e83`  |
| 1335   | No file  | `5b105d998e83`  |
| 1333   | No file  | `5b105d998e83`  |
| 1329   | No file  | `5b105d998e83`  |
| 1327   | No file  | `5b105d998e83`  |
| 1324   | No file  | `5b105d998e83`  |
| 1321   | No file  | `5b105d998e83`  |
| 1319   | No file  | `5b105d998e83`  |
| 1318   | No file  | `5b105d998e83`  |
| 1316   | No file  | `5b105d998e83`  |
| 1313   | No file  | `5b105d998e83`  |
| 1311   | No file  | `5b105d998e83`  |
| 1309   | No file  | `5b105d998e83`  |
| 1304   | No file  | `5b105d998e83`  |
| 1292   | No file  | `5b105d998e83`  |
| 1286   | No file  | `5b105d998e83`  |
| 1280   | No file  | `5b105d998e83`  |
| 1276   | No file  | `5b105d998e83`  |
| 1267   | No file  | `5b105d998e83`  |
| 1261   | No file  | `5b105d998e83`  |
| 1256   | No file  | `5b105d998e83`  |
| 1250   | No file  | `5b105d998e83`  |
| 1246   | No file  | `5b105d998e83`  |
| 1239   | No file  | `5b105d998e83`  |
| 1230   | No file  | `5b105d998e83`  |
| 1226   | No file  | `5b105d998e83`  |
| 1220   | No file  | `5b105d998e83`  |
| 1217   | No file  | `5b105d998e83`  |
| 1211   | No file  | `5b105d998e83`  |
| 1210   | No file  | `5b105d998e83`  |
| 1208   | No file  | `5b105d998e83`  |
| 1203   | No file  | `5b105d998e83`  |
| 1197   | No file  | `5b105d998e83`  |
| 1194   | No file  | `5b105d998e83`  |
| 1192   | No file  | `5b105d998e83`  |
| 1187   | No file  | `5b105d998e83`  |
| 1183   | No file  | `5b105d998e83`  |
| 1177   | No file  | `5b105d998e83`  |
| 1173   | No file  | `5b105d998e83`  |
| 1167   | No file  | `5b105d998e83`  |
| 1164   | No file  | `5b105d998e83`  |
| 1156   | No file  | `5b105d998e83`  |
| 1149   | No file  | `5b105d998e83`  |
| 1144   | No file  | `5b105d998e83`  |
| 1137   | No file  | `5b105d998e83`  |
| 1132   | No file  | `5b105d998e83`  |
| 1127   | No file  | `5b105d998e83`  |
| 1122   | No file  | `5b105d998e83`  |
| 1118   | No file  | `5b105d998e83`  |
| 1114   | No file  | `5b105d998e83`  |
| 1109   | No file  | `5b105d998e83`  |
| 1102   | No file  | `5b105d998e83`  |
| 1096   | No file  | `5b105d998e83`  |
| 1088   | No file  | `5b105d998e83`  |
| 1081   | No file  | `5b105d998e83`  |
| 1076   | No file  | `5b105d998e83`  |
| 1069   | No file  | `5b105d998e83`  |
| 1064   | No file  | `5b105d998e83`  |
| 1058   | No file  | `5b105d998e83`  |
| 1051   | No file  | `5b105d998e83`  |
| 1044   | No file  | `5b105d998e83`  |
| 1036   | No file  | `5b105d998e83`  |
| 1026   | No file  | `5b105d998e83`  |
| 1016   | No file  | `5b105d998e83`  |
| 1009   | No file  | `5b105d998e83`  |
| 1005   | No file  | `5b105d998e83`  |
| 1000   | No file  | `5b105d998e83`  |
| 998    | No file  | `5b105d998e83`  |
| 990    | No file  | `5b105d998e83`  |
| 979    | No file  | `5b105d998e83`  |
| 972    | No file  | `5b105d998e83`  |
| 963    | No file  | `5b105d998e83`  |
| 955    | No file  | `5b105d998e83`  |
| 946    | No file  | `5b105d998e83`  |
| 938    | No file  | `5b105d998e83`  |
| 927    | No file  | `5b105d998e83`  |
| 911    | No file  | `5b105d998e83`  |
| 904    | No file  | `5b105d998e83`  |
| 899    | No file  | `5b105d998e83`  |
| 894    | No file  | `5b105d998e83`  |
| 885    | No file  | `5b105d998e83`  |
| 879    | No file  | `5b105d998e83`  |
| 872    | No file  | `5b105d998e83`  |
| 864    | No file  | `5b105d998e83`  |
| 855    | No file  | `5b105d998e83`  |
| 853    | No file  | `5b105d998e83`  |
| 845    | No file  | `5b105d998e83`  |
| 837    | No file  | `5b105d998e83`  |
| 829    | No file  | `5b105d998e83`  |
| 822    | No file  | `5b105d998e83`  |
| 814    | No file  | `5b105d998e83`  |
| 805    | No file  | `5b105d998e83`  |
| 794    | No file  | `5b105d998e83`  |
| 787    | No file  | `5b105d998e83`  |
| 780    | No file  | `5b105d998e83`  |
| 771    | No file  | `5b105d998e83`  |
| 760    | No file  | `5b105d998e83`  |
| 748    | No file  | `5b105d998e83`  |
| 741    | No file  | `5b105d998e83`  |
| 736    | No file  | `5b105d998e83`  |
| 731    | No file  | `5b105d998e83`  |
| 723    | No file  | `5b105d998e83`  |
| 711    | No file  | `5b105d998e83`  |
| 707    | No file  | `5b105d998e83`  |
| 697    | No file  | `5b105d998e83`  |
| 689    | No file  | `5b105d998e83`  |
| 683    | No file  | `5b105d998e83`  |
| 678    | No file  | `5b105d998e83`  |
| 670    | No file  | `5b105d998e83`  |
| 661    | No file  | `5b105d998e83`  |
| 656    | No file  | `5b105d998e83`  |
| 652    | No file  | `5b105d998e83`  |
| 643    | No file  | `5b105d998e83`  |
| 637    | No file  | `5b105d998e83`  |
| 630    | No file  | `5b105d998e83`  |
| 627    | No file  | `5b105d998e83`  |
| 621    | No file  | `5b105d998e83`  |
| 617    | No file  | `5b105d998e83`  |
| 615    | No file  | `5b105d998e83`  |
| 606    | No file  | `5b105d998e83`  |
| 599    | No file  | `5b105d998e83`  |
| 592    | No file  | `5b105d998e83`  |
| 586    | No file  | `5b105d998e83`  |
| 577    | No file  | `5b105d998e83`  |
| 569    | No file  | `5b105d998e83`  |
| 561    | No file  | `5b105d998e83`  |
| 554    | No file  | `5b105d998e83`  |
| 542    | No file  | `5b105d998e83`  |
| 532    | No file  | `5b105d998e83`  |
| 531    | No file  | `5b105d998e83`  |
| 526    | No file  | `5b105d998e83`  |
| 521    | No file  | `5b105d998e83`  |
| 517    | No file  | `5b105d998e83`  |
| 510    | No file  | `5b105d998e83`  |
| 508    | No file  | `5b105d998e83`  |
| 504    | No file  | `5b105d998e83`  |
| 497    | No file  | `5b105d998e83`  |
| 491    | No file  | `5b105d998e83`  |
| 485    | No file  | `5b105d998e83`  |
| 478    | No file  | `5b105d998e83`  |
| 472    | No file  | `5b105d998e83`  |
| 466    | No file  | `5b105d998e83`  |
| 457    | No file  | `5b105d998e83`  |
| 452    | No file  | `5b105d998e83`  |
| 449    | No file  | `5b105d998e83`  |
| 435    | No file  | `5b105d998e83`  |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                                  |
| ------------------------------- | -------- | --------------------------------------------------------------------- |
| `purchaselimitgroupoffset.dbss` | Optional | `group_no -> (data_offset, data_size)` of every row; the rows are fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                         |
| ------- | ---------- | ----- | --------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `2` on client 3474            |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row  |

### Row (9 bytes)

| Offset  | Type | Field          | Notes                                                                 |
| ------- | ---- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | group_no       | Group number, the `PurchaseGroupNo` of a product; unique per row, the index key |
| `+0x04` | u8   | purchase_type  | Who the limit counts for, a `CashPurchaseLimitType`; see Limit Types  |
| `+0x05` | i32  | purchase_count | Purchases the group allows                                            |

The rows are packed with no padding, so `purchase_count` sits at an odd
offset.

### `purchaselimitgroupoffset.dbss`

| Offset  | Type              | Field | Notes                                         |
| ------- | ----------------- | ----- | --------------------------------------------- |
| `+0x00` | u32               | count | Equals the `purchaselimitgroup.dbss` count    |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row          |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                  |
| ------- | ---- | ----------- | -------------------------------------- |
| `+0x00` | u32  | group_no    | Key of the row it points at            |
| `+0x04` | u32  | data_offset | Start of the row, at its `group_no`    |
| `+0x08` | u32  | data_size   | `9`, the whole row                     |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. On
clients 1784 and 3474 the index lists group `2` first and group `1` second,
in the order of the main file, and every index row points at the row with
its key.

## Limit Types

`purchase_type` takes the values of `CppEnums.CashPurchaseLimitType` in
`global_define_cpp_enum.luac`, the same enum (`gc::CashPurchaseLimitType`,
an `unsigned char`) as the 2016 PDB names:

| Value | Name          | Pearl Shop limit line (`panel_pearlshop.luac`)     |
| ----- | ------------- | -------------------------------------------------- |
| `0`   | `None`        | None shown                                         |
| `1`   | `AtCharacter` | `LUA_INGAMECASHSHOP_GOODSDETAILINFO_CHARACTER` (Character) |
| `2`   | `AtAccount`   | `LUA_INGAMECASHSHOP_GOODSDETAILINFO_FAMILY` (Family) |

Both rows hold `2` on clients 1784 and 3474.

## Field Names

The names are the columns of the `PurchaseGroup_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784 (`GroupNo`, `PurchaseType`,
`PurchaseCount`), a sheet of its `datasheet_cashproduct.xlsx` workbooks. The sheet's two rows (`1`, `2`, `1`) and (`2`, `2`, `1`) match the
file on 2 of 2 keys on clients 1784 and 3474. The 1784 and 3474 files are
byte for byte the same.

The server dump of the same private server checks the sheet with the
messages `PurchaseGroup_Table GroupNo(%#) : limitType` and `PurchaseGroup_Table
GroupNo(%#) : limitCount`, so `PurchaseType` is a limit type and
`PurchaseCount` a limit count. A product stores the same pair: the 2016
`gc::CashProductStaticStatus` has `_productCashPurchaseLimit`
(`gc::CashPurchaseLimitType`, 1 byte) and `_productCashPurchaseCount` (`int`,
4 bytes), the `PurchaseSubject` and `PurchaseCountLimit` columns of
`CashProduct_Table`, which is why `purchase_count` is read as an `i32`. The
2016 PDB has no purchase group struct.

## Open Questions

### Which Products Belong to a Group

The link from product to group is the `PurchaseGroupNo` column of
`CashProduct_Table`. `cashproduct.dbss` blocks are undecoded past the name
(see [`cashproduct.dbss`](cashproduct_dbss.md)), so the handler cannot list
a group's products. The four grouped products of client 1784 named in
Purpose come from the sheet, not from the client file.

### Group Limit and Product Limit Together

On client 1784 each of the four grouped products also has its own limit in
`CashProduct_Table` (`PurchaseSubject` `2`, `PurchaseCountLimit` `1`). No
client Lua reads the group: the Pearl Shop reads `getCashPurchaseLimitType()`
and `getCashPurchaseCount()` of the product and
`getRemainingLimitCount()` by product number, and no Lua file names a
purchase group.
Whether the server checks the group limit in place of the product limit or
on top of it is open.
