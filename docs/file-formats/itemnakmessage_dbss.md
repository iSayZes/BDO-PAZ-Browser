# `itemnakmessage.dbss` Format

## Purpose

The screen-wide message shown when someone obtains one of a few rare items
(Rich Merchant's Ring, Archaeologist's Map, Ornette's and Odore's Spirit
Essence, Krogdalo's Sanctuary and others): per item key a main line and a sub line, both stored as
`GAME` sheet keys of [`stringtable.bss`](stringtable_bss.md). The main line
holds `{playerName}` and `{itemName}` placeholders. Companion
`itemnakmessageoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | ------------- | --------- |
| 1      | 1430 and later | 3483    | `itemnakmessage.dbss`       | 1,412 | 11 Row        | 128       |
| 1      | 1430 and later | 3483    | `itemnakmessageoffset.dbss` | 152   | 11 Offset Row | 12        |

| Layout | File                        | Known            | Unknown    |
| ------ | --------------------------- | ---------------- | ---------- |
| 1      | `itemnakmessage.dbss`       | 1,412 B (100.0%) | 0 B (0.0%) |
| 1      | `itemnakmessageoffset.dbss` | 152 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a12ca6313920`  |
| 3482   | Layout 1 | `a12ca6313920`  |
| 3474   | Layout 1 | `a12ca6313920`  |
| 3473   | Layout 1 | `a12ca6313920`  |
| 3464   | Layout 1 | `a12ca6313920`  |
| 3458   | Layout 1 | `a12ca6313920`  |
| 3454   | Layout 1 | `a12ca6313920`  |
| 3444   | Layout 1 | `a12ca6313920`  |
| 3435   | Layout 1 | `a12ca6313920`  |
| 3426   | Layout 1 | `a12ca6313920`  |
| 3418   | Layout 1 | `a12ca6313920`  |
| 3412   | Layout 1 | `a12ca6313920`  |
| 3402   | Layout 1 | `a12ca6313920`  |
| 3396   | Layout 1 | `a12ca6313920`  |
| 3387   | Layout 1 | `a12ca6313920`  |
| 3381   | Layout 1 | `a12ca6313920`  |
| 3373   | Layout 1 | `a12ca6313920`  |
| 3364   | Layout 1 | `a12ca6313920`  |
| 3356   | Layout 1 | `a12ca6313920`  |
| 3349   | Layout 1 | `a12ca6313920`  |
| 3342   | Layout 1 | `a12ca6313920`  |
| 3335   | Layout 1 | `a12ca6313920`  |
| 3326   | Layout 1 | `a12ca6313920`  |
| 3321   | Layout 1 | `a12ca6313920`  |
| 3314   | Layout 1 | `a12ca6313920`  |
| 3303   | Layout 1 | `a12ca6313920`  |
| 3302   | Layout 1 | `a12ca6313920`  |
| 3293   | Layout 1 | `a12ca6313920`  |
| 3283   | Layout 1 | `a12ca6313920`  |
| 3275   | Layout 1 | `a12ca6313920`  |
| 3267   | Layout 1 | `a12ca6313920`  |
| 3258   | Layout 1 | `a12ca6313920`  |
| 3251   | Layout 1 | `a12ca6313920`  |
| 3242   | Layout 1 | `a12ca6313920`  |
| 3235   | Layout 1 | `a12ca6313920`  |
| 3229   | Layout 1 | `a12ca6313920`  |
| 3212   | Layout 1 | `a12ca6313920`  |
| 3203   | Layout 1 | `a12ca6313920`  |
| 3193   | Layout 1 | `a12ca6313920`  |
| 3186   | Layout 1 | `a12ca6313920`  |
| 3177   | Layout 1 | `a12ca6313920`  |
| 3169   | Layout 1 | `a12ca6313920`  |
| 3158   | Layout 1 | `a12ca6313920`  |
| 3151   | Layout 1 | `a12ca6313920`  |
| 3144   | Layout 1 | `a12ca6313920`  |
| 3133   | Layout 1 | `a12ca6313920`  |
| 3125   | Layout 1 | `a12ca6313920`  |
| 3118   | Layout 1 | `a12ca6313920`  |
| 3111   | Layout 1 | `a12ca6313920`  |
| 3103   | Layout 1 | `a12ca6313920`  |
| 3095   | Layout 1 | `a12ca6313920`  |
| 3086   | Layout 1 | `a12ca6313920`  |
| 3072   | Layout 1 | `a12ca6313920`  |
| 3062   | Layout 1 | `a12ca6313920`  |
| 3052   | Layout 1 | `a12ca6313920`  |
| 3045   | Layout 1 | `a12ca6313920`  |
| 3037   | Layout 1 | `a12ca6313920`  |
| 3030   | Layout 1 | `a12ca6313920`  |
| 3021   | Layout 1 | `a12ca6313920`  |
| 3012   | Layout 1 | `a12ca6313920`  |
| 3002   | Layout 1 | `a12ca6313920`  |
| 2995   | Layout 1 | `a12ca6313920`  |
| 2987   | Layout 1 | `a12ca6313920`  |
| 2978   | Layout 1 | `a12ca6313920`  |
| 2970   | Layout 1 | `a12ca6313920`  |
| 2959   | Layout 1 | `a12ca6313920`  |
| 2951   | Layout 1 | `a12ca6313920`  |
| 2942   | Layout 1 | `a12ca6313920`  |
| 2935   | Layout 1 | `a12ca6313920`  |
| 2932   | Layout 1 | `a12ca6313920`  |
| 2923   | Layout 1 | `a12ca6313920`  |
| 2919   | Layout 1 | `a12ca6313920`  |
| 2907   | Layout 1 | `a12ca6313920`  |
| 2900   | Layout 1 | `a12ca6313920`  |
| 2891   | Layout 1 | `a12ca6313920`  |
| 2882   | Layout 1 | `a12ca6313920`  |
| 2872   | Layout 1 | `a12ca6313920`  |
| 2863   | Layout 1 | `a12ca6313920`  |
| 2855   | Layout 1 | `a12ca6313920`  |
| 2849   | Layout 1 | `a12ca6313920`  |
| 2844   | Layout 1 | `a12ca6313920`  |
| 2834   | Layout 1 | `a12ca6313920`  |
| 2825   | Layout 1 | `a12ca6313920`  |
| 2819   | Layout 1 | `a12ca6313920`  |
| 2811   | Layout 1 | `a12ca6313920`  |
| 2803   | Layout 1 | `a12ca6313920`  |
| 2794   | Layout 1 | `a12ca6313920`  |
| 2783   | Layout 1 | `a12ca6313920`  |
| 2774   | Layout 1 | `a12ca6313920`  |
| 2765   | Layout 1 | `a12ca6313920`  |
| 2756   | Layout 1 | `a12ca6313920`  |
| 2750   | Layout 1 | `a12ca6313920`  |
| 2743   | Layout 1 | `a12ca6313920`  |
| 2736   | Layout 1 | `a12ca6313920`  |
| 2726   | Layout 1 | `a12ca6313920`  |
| 2717   | Layout 1 | `a12ca6313920`  |
| 2709   | Layout 1 | `a12ca6313920`  |
| 2703   | Layout 1 | `a12ca6313920`  |
| 2695   | Layout 1 | `a12ca6313920`  |
| 2684   | Layout 1 | `a12ca6313920`  |
| 2672   | Layout 1 | `a12ca6313920`  |
| 2665   | Layout 1 | `a12ca6313920`  |
| 2657   | Layout 1 | `a12ca6313920`  |
| 2649   | Layout 1 | `a12ca6313920`  |
| 2644   | Layout 1 | `a12ca6313920`  |
| 2637   | Layout 1 | `a12ca6313920`  |
| 2629   | Layout 1 | `a12ca6313920`  |
| 2619   | Layout 1 | `a12ca6313920`  |
| 2612   | Layout 1 | `a12ca6313920`  |
| 2606   | Layout 1 | `a12ca6313920`  |
| 2602   | Layout 1 | `a12ca6313920`  |
| 2601   | Layout 1 | `a12ca6313920`  |
| 2592   | Layout 1 | `a12ca6313920`  |
| 2583   | Layout 1 | `a12ca6313920`  |
| 2575   | Layout 1 | `a12ca6313920`  |
| 2567   | Layout 1 | `a12ca6313920`  |
| 2560   | Layout 1 | `a12ca6313920`  |
| 2553   | Layout 1 | `a12ca6313920`  |
| 2545   | Layout 1 | `a12ca6313920`  |
| 2538   | Layout 1 | `a12ca6313920`  |
| 2529   | Layout 1 | `a12ca6313920`  |
| 2519   | Layout 1 | `a12ca6313920`  |
| 2513   | Layout 1 | `a12ca6313920`  |
| 2510   | Layout 1 | `a12ca6313920`  |
| 2507   | Layout 1 | `a12ca6313920`  |
| 2503   | Layout 1 | `a12ca6313920`  |
| 2498   | Layout 1 | `a12ca6313920`  |
| 2492   | Layout 1 | `a12ca6313920`  |
| 2487   | Layout 1 | `a12ca6313920`  |
| 2480   | Layout 1 | `a12ca6313920`  |
| 2474   | Layout 1 | `a12ca6313920`  |
| 2468   | Layout 1 | `a12ca6313920`  |
| 2460   | Layout 1 | `a12ca6313920`  |
| 2453   | Layout 1 | `a12ca6313920`  |
| 2444   | Layout 1 | `a12ca6313920`  |
| 2438   | Layout 1 | `a12ca6313920`  |
| 2434   | Layout 1 | `a12ca6313920`  |
| 2429   | Layout 1 | `a12ca6313920`  |
| 2421   | Layout 1 | `a12ca6313920`  |
| 2414   | Layout 1 | `a12ca6313920`  |
| 2407   | Layout 1 | `a12ca6313920`  |
| 2401   | Layout 1 | `a12ca6313920`  |
| 2397   | Layout 1 | `a12ca6313920`  |
| 2393   | Layout 1 | `a12ca6313920`  |
| 2384   | Layout 1 | `a12ca6313920`  |
| 2378   | Layout 1 | `a12ca6313920`  |
| 2372   | Layout 1 | `a12ca6313920`  |
| 2358   | Layout 1 | `a12ca6313920`  |
| 2352   | Layout 1 | `a12ca6313920`  |
| 2347   | Layout 1 | `a12ca6313920`  |
| 2343   | Layout 1 | `a12ca6313920`  |
| 2335   | Layout 1 | `a12ca6313920`  |
| 2327   | Layout 1 | `a12ca6313920`  |
| 2324   | Layout 1 | `a12ca6313920`  |
| 2319   | Layout 1 | `a12ca6313920`  |
| 2313   | Layout 1 | `a12ca6313920`  |
| 2308   | Layout 1 | `a12ca6313920`  |
| 2302   | Layout 1 | `a12ca6313920`  |
| 2295   | Layout 1 | `a12ca6313920`  |
| 2290   | Layout 1 | `a12ca6313920`  |
| 2284   | Layout 1 | `a12ca6313920`  |
| 2276   | Layout 1 | `a12ca6313920`  |
| 2269   | Layout 1 | `a12ca6313920`  |
| 2259   | Layout 1 | `a12ca6313920`  |
| 2250   | Layout 1 | `a12ca6313920`  |
| 2243   | Layout 1 | `a12ca6313920`  |
| 2235   | Layout 1 | `a12ca6313920`  |
| 2229   | Layout 1 | `a12ca6313920`  |
| 2224   | Layout 1 | `a12ca6313920`  |
| 2218   | Layout 1 | `a12ca6313920`  |
| 2215   | Layout 1 | `a12ca6313920`  |
| 2207   | Layout 1 | `a12ca6313920`  |
| 2203   | Layout 1 | `a12ca6313920`  |
| 2196   | Layout 1 | `a12ca6313920`  |
| 2192   | Layout 1 | `a12ca6313920`  |
| 2189   | Layout 1 | `a12ca6313920`  |
| 2183   | Layout 1 | `a12ca6313920`  |
| 2179   | Layout 1 | `a12ca6313920`  |
| 2171   | Layout 1 | `a12ca6313920`  |
| 2163   | Layout 1 | `a12ca6313920`  |
| 2156   | Layout 1 | `a12ca6313920`  |
| 2151   | Layout 1 | `a12ca6313920`  |
| 2147   | Layout 1 | `a12ca6313920`  |
| 2142   | Layout 1 | `a12ca6313920`  |
| 2138   | Layout 1 | `a12ca6313920`  |
| 2134   | Layout 1 | `a12ca6313920`  |
| 2130   | Layout 1 | `a12ca6313920`  |
| 2122   | Layout 1 | `a12ca6313920`  |
| 2107   | Layout 1 | `a12ca6313920`  |
| 2098   | Layout 1 | `a12ca6313920`  |
| 2089   | Layout 1 | `a12ca6313920`  |
| 2081   | Layout 1 | `a12ca6313920`  |
| 2073   | Layout 1 | `a12ca6313920`  |
| 2067   | Layout 1 | `a12ca6313920`  |
| 2063   | Layout 1 | `a12ca6313920`  |
| 2059   | Layout 1 | `a12ca6313920`  |
| 2052   | Layout 1 | `a12ca6313920`  |
| 2044   | Layout 1 | `a12ca6313920`  |
| 2039   | Layout 1 | `a12ca6313920`  |
| 2032   | Layout 1 | `a12ca6313920`  |
| 2025   | Layout 1 | `a12ca6313920`  |
| 2011   | Layout 1 | `a12ca6313920`  |
| 2005   | Layout 1 | `a12ca6313920`  |
| 2000   | Layout 1 | `a12ca6313920`  |
| 1996   | Layout 1 | `a12ca6313920`  |
| 1991   | Layout 1 | `a12ca6313920`  |
| 1985   | Layout 1 | `a12ca6313920`  |
| 1980   | Layout 1 | `a12ca6313920`  |
| 1969   | Layout 1 | `a12ca6313920`  |
| 1964   | Layout 1 | `a12ca6313920`  |
| 1958   | Layout 1 | `a12ca6313920`  |
| 1950   | Layout 1 | `a12ca6313920`  |
| 1945   | Layout 1 | `a12ca6313920`  |
| 1937   | Layout 1 | `a12ca6313920`  |
| 1933   | Layout 1 | `a12ca6313920`  |
| 1927   | Layout 1 | `a12ca6313920`  |
| 1921   | Layout 1 | `a12ca6313920`  |
| 1914   | Layout 1 | `a12ca6313920`  |
| 1908   | Layout 1 | `a12ca6313920`  |
| 1897   | Layout 1 | `a12ca6313920`  |
| 1892   | Layout 1 | `a12ca6313920`  |
| 1886   | Layout 1 | `a12ca6313920`  |
| 1881   | Layout 1 | `a12ca6313920`  |
| 1871   | Layout 1 | `a12ca6313920`  |
| 1866   | Layout 1 | `a12ca6313920`  |
| 1862   | Layout 1 | `a12ca6313920`  |
| 1854   | Layout 1 | `a12ca6313920`  |
| 1846   | Layout 1 | `a12ca6313920`  |
| 1838   | Layout 1 | `a12ca6313920`  |
| 1832   | Layout 1 | `a12ca6313920`  |
| 1826   | Layout 1 | `a12ca6313920`  |
| 1822   | Layout 1 | `a12ca6313920`  |
| 1818   | Layout 1 | `a12ca6313920`  |
| 1804   | Layout 1 | `a12ca6313920`  |
| 1794   | Layout 1 | `a12ca6313920`  |
| 1790   | Layout 1 | `a12ca6313920`  |
| 1784   | Layout 1 | `a12ca6313920`  |
| 1774   | Layout 1 | `a12ca6313920`  |
| 1771   | Layout 1 | `a12ca6313920`  |
| 1762   | Layout 1 | `a12ca6313920`  |
| 1759   | Layout 1 | `a12ca6313920`  |
| 1754   | Layout 1 | `a12ca6313920`  |
| 1749   | Layout 1 | `a12ca6313920`  |
| 1743   | Layout 1 | `a12ca6313920`  |
| 1737   | Layout 1 | `a12ca6313920`  |
| 1731   | Layout 1 | `a12ca6313920`  |
| 1725   | Layout 1 | `a12ca6313920`  |
| 1717   | Layout 1 | `a12ca6313920`  |
| 1710   | Layout 1 | `a12ca6313920`  |
| 1704   | Layout 1 | `a12ca6313920`  |
| 1698   | Layout 1 | `a12ca6313920`  |
| 1690   | Layout 1 | `a12ca6313920`  |
| 1685   | Layout 1 | `a12ca6313920`  |
| 1680   | Layout 1 | `a12ca6313920`  |
| 1674   | Layout 1 | `a12ca6313920`  |
| 1668   | Layout 1 | `a12ca6313920`  |
| 1659   | Layout 1 | `a12ca6313920`  |
| 1649   | Layout 1 | `a12ca6313920`  |
| 1642   | Layout 1 | `a12ca6313920`  |
| 1636   | Layout 1 | `a12ca6313920`  |
| 1628   | Layout 1 | `a12ca6313920`  |
| 1622   | Layout 1 | `a12ca6313920`  |
| 1614   | Layout 1 | `a12ca6313920`  |
| 1608   | Layout 1 | `a12ca6313920`  |
| 1602   | Layout 1 | `a12ca6313920`  |
| 1598   | Layout 1 | `a12ca6313920`  |
| 1594   | Layout 1 | `a12ca6313920`  |
| 1590   | Layout 1 | `a12ca6313920`  |
| 1587   | Layout 1 | `a12ca6313920`  |
| 1584   | Layout 1 | `a12ca6313920`  |
| 1579   | Layout 1 | `a12ca6313920`  |
| 1572   | Layout 1 | `a12ca6313920`  |
| 1565   | Layout 1 | `a12ca6313920`  |
| 1559   | Layout 1 | `a12ca6313920`  |
| 1554   | Layout 1 | `a12ca6313920`  |
| 1547   | Layout 1 | `a12ca6313920`  |
| 1537   | Layout 1 | `a12ca6313920`  |
| 1529   | Layout 1 | `a12ca6313920`  |
| 1524   | Layout 1 | `a12ca6313920`  |
| 1519   | Layout 1 | `a12ca6313920`  |
| 1509   | Layout 1 | `a12ca6313920`  |
| 1506   | Layout 1 | `a12ca6313920`  |
| 1504   | Layout 1 | `a12ca6313920`  |
| 1500   | Layout 1 | `a12ca6313920`  |
| 1493   | Layout 1 | `a12ca6313920`  |
| 1489   | Layout 1 | `a12ca6313920`  |
| 1485   | Layout 1 | `a12ca6313920`  |
| 1481   | Layout 1 | `a12ca6313920`  |
| 1474   | Layout 1 | `a12ca6313920`  |
| 1466   | Layout 1 | `a12ca6313920`  |
| 1462   | Layout 1 | `a12ca6313920`  |
| 1459   | Layout 1 | `a12ca6313920`  |
| 1453   | Layout 1 | `a12ca6313920`  |
| 1450   | Layout 1 | `a12ca6313920`  |
| 1445   | Layout 1 | `a12ca6313920`  |
| 1439   | Layout 1 | `a12ca6313920`  |
| 1433   | Layout 1 | `a12ca6313920`  |
| 1430   | Layout 1 | `a12ca6313920`  |
| 1426   | No file  | `a12ca6313920`  |
| 1421   | No file  | `a12ca6313920`  |
| 1417   | No file  | `a12ca6313920`  |
| 1416   | No file  | `a12ca6313920`  |
| 1409   | No file  | `a12ca6313920`  |
| 1405   | No file  | `a12ca6313920`  |
| 1401   | No file  | `a12ca6313920`  |
| 1396   | No file  | `a12ca6313920`  |
| 1391   | No file  | `a12ca6313920`  |
| 1390   | No file  | `a12ca6313920`  |
| 1386   | No file  | `a12ca6313920`  |
| 1381   | No file  | `a12ca6313920`  |
| 1379   | No file  | `a12ca6313920`  |
| 1372   | No file  | `a12ca6313920`  |
| 1366   | No file  | `a12ca6313920`  |
| 1364   | No file  | `a12ca6313920`  |
| 1363   | No file  | `a12ca6313920`  |
| 1360   | No file  | `a12ca6313920`  |
| 1358   | No file  | `a12ca6313920`  |
| 1355   | No file  | `a12ca6313920`  |
| 1351   | No file  | `a12ca6313920`  |
| 1348   | No file  | `a12ca6313920`  |
| 1346   | No file  | `a12ca6313920`  |
| 1341   | No file  | `a12ca6313920`  |
| 1340   | No file  | `a12ca6313920`  |
| 1338   | No file  | `a12ca6313920`  |
| 1335   | No file  | `a12ca6313920`  |
| 1333   | No file  | `a12ca6313920`  |
| 1329   | No file  | `a12ca6313920`  |
| 1327   | No file  | `a12ca6313920`  |
| 1324   | No file  | `a12ca6313920`  |
| 1321   | No file  | `a12ca6313920`  |
| 1319   | No file  | `a12ca6313920`  |
| 1318   | No file  | `a12ca6313920`  |
| 1316   | No file  | `a12ca6313920`  |
| 1313   | No file  | `a12ca6313920`  |
| 1311   | No file  | `a12ca6313920`  |
| 1309   | No file  | `a12ca6313920`  |
| 1304   | No file  | `a12ca6313920`  |
| 1292   | No file  | `a12ca6313920`  |
| 1286   | No file  | `a12ca6313920`  |
| 1280   | No file  | `a12ca6313920`  |
| 1276   | No file  | `a12ca6313920`  |
| 1267   | No file  | `a12ca6313920`  |
| 1261   | No file  | `a12ca6313920`  |
| 1256   | No file  | `a12ca6313920`  |
| 1250   | No file  | `a12ca6313920`  |
| 1246   | No file  | `a12ca6313920`  |
| 1239   | No file  | `a12ca6313920`  |
| 1230   | No file  | `a12ca6313920`  |
| 1226   | No file  | `a12ca6313920`  |
| 1220   | No file  | `a12ca6313920`  |
| 1217   | No file  | `a12ca6313920`  |
| 1211   | No file  | `a12ca6313920`  |
| 1210   | No file  | `a12ca6313920`  |
| 1208   | No file  | `a12ca6313920`  |
| 1203   | No file  | `a12ca6313920`  |
| 1197   | No file  | `a12ca6313920`  |
| 1194   | No file  | `a12ca6313920`  |
| 1192   | No file  | `a12ca6313920`  |
| 1187   | No file  | `a12ca6313920`  |
| 1183   | No file  | `a12ca6313920`  |
| 1177   | No file  | `a12ca6313920`  |
| 1173   | No file  | `a12ca6313920`  |
| 1167   | No file  | `a12ca6313920`  |
| 1164   | No file  | `a12ca6313920`  |
| 1156   | No file  | `a12ca6313920`  |
| 1149   | No file  | `a12ca6313920`  |
| 1144   | No file  | `a12ca6313920`  |
| 1137   | No file  | `a12ca6313920`  |
| 1132   | No file  | `a12ca6313920`  |
| 1127   | No file  | `a12ca6313920`  |
| 1122   | No file  | `a12ca6313920`  |
| 1118   | No file  | `a12ca6313920`  |
| 1114   | No file  | `a12ca6313920`  |
| 1109   | No file  | `a12ca6313920`  |
| 1102   | No file  | `a12ca6313920`  |
| 1096   | No file  | `a12ca6313920`  |
| 1088   | No file  | `a12ca6313920`  |
| 1081   | No file  | `a12ca6313920`  |
| 1076   | No file  | `a12ca6313920`  |
| 1069   | No file  | `a12ca6313920`  |
| 1064   | No file  | `a12ca6313920`  |
| 1058   | No file  | `a12ca6313920`  |
| 1051   | No file  | `a12ca6313920`  |
| 1044   | No file  | `a12ca6313920`  |
| 1036   | No file  | `a12ca6313920`  |
| 1026   | No file  | `a12ca6313920`  |
| 1016   | No file  | `a12ca6313920`  |
| 1009   | No file  | `a12ca6313920`  |
| 1005   | No file  | `a12ca6313920`  |
| 1000   | No file  | `a12ca6313920`  |
| 998    | No file  | `a12ca6313920`  |
| 990    | No file  | `a12ca6313920`  |
| 979    | No file  | `a12ca6313920`  |
| 972    | No file  | `a12ca6313920`  |
| 963    | No file  | `a12ca6313920`  |
| 955    | No file  | `a12ca6313920`  |
| 946    | No file  | `a12ca6313920`  |
| 938    | No file  | `a12ca6313920`  |
| 927    | No file  | `a12ca6313920`  |
| 911    | No file  | `a12ca6313920`  |
| 904    | No file  | `a12ca6313920`  |
| 899    | No file  | `a12ca6313920`  |
| 894    | No file  | `a12ca6313920`  |
| 885    | No file  | `a12ca6313920`  |
| 879    | No file  | `a12ca6313920`  |
| 872    | No file  | `a12ca6313920`  |
| 864    | No file  | `a12ca6313920`  |
| 855    | No file  | `a12ca6313920`  |
| 853    | No file  | `a12ca6313920`  |
| 845    | No file  | `a12ca6313920`  |
| 837    | No file  | `a12ca6313920`  |
| 829    | No file  | `a12ca6313920`  |
| 822    | No file  | `a12ca6313920`  |
| 814    | No file  | `a12ca6313920`  |
| 805    | No file  | `a12ca6313920`  |
| 794    | No file  | `a12ca6313920`  |
| 787    | No file  | `a12ca6313920`  |
| 780    | No file  | `a12ca6313920`  |
| 771    | No file  | `a12ca6313920`  |
| 760    | No file  | `a12ca6313920`  |
| 748    | No file  | `a12ca6313920`  |
| 741    | No file  | `a12ca6313920`  |
| 736    | No file  | `a12ca6313920`  |
| 731    | No file  | `a12ca6313920`  |
| 723    | No file  | `a12ca6313920`  |
| 711    | No file  | `a12ca6313920`  |
| 707    | No file  | `a12ca6313920`  |
| 697    | No file  | `a12ca6313920`  |
| 689    | No file  | `a12ca6313920`  |
| 683    | No file  | `a12ca6313920`  |
| 678    | No file  | `a12ca6313920`  |
| 670    | No file  | `a12ca6313920`  |
| 661    | No file  | `a12ca6313920`  |
| 656    | No file  | `a12ca6313920`  |
| 652    | No file  | `a12ca6313920`  |
| 643    | No file  | `a12ca6313920`  |
| 637    | No file  | `a12ca6313920`  |
| 630    | No file  | `a12ca6313920`  |
| 627    | No file  | `a12ca6313920`  |
| 621    | No file  | `a12ca6313920`  |
| 617    | No file  | `a12ca6313920`  |
| 615    | No file  | `a12ca6313920`  |
| 606    | No file  | `a12ca6313920`  |
| 599    | No file  | `a12ca6313920`  |
| 592    | No file  | `a12ca6313920`  |
| 586    | No file  | `a12ca6313920`  |
| 577    | No file  | `a12ca6313920`  |
| 569    | No file  | `a12ca6313920`  |
| 561    | No file  | `a12ca6313920`  |
| 554    | No file  | `a12ca6313920`  |
| 542    | No file  | `a12ca6313920`  |
| 532    | No file  | `a12ca6313920`  |
| 531    | No file  | `a12ca6313920`  |
| 526    | No file  | `a12ca6313920`  |
| 521    | No file  | `a12ca6313920`  |
| 517    | No file  | `a12ca6313920`  |
| 510    | No file  | `a12ca6313920`  |
| 508    | No file  | `a12ca6313920`  |
| 504    | No file  | `a12ca6313920`  |
| 497    | No file  | `a12ca6313920`  |
| 491    | No file  | `a12ca6313920`  |
| 485    | No file  | `a12ca6313920`  |
| 478    | No file  | `a12ca6313920`  |
| 472    | No file  | `a12ca6313920`  |
| 466    | No file  | `a12ca6313920`  |
| 457    | No file  | `a12ca6313920`  |
| 452    | No file  | `a12ca6313920`  |
| 449    | No file  | `a12ca6313920`  |
| 435    | No file  | `a12ca6313920`  |

<!-- versions:end -->

## Companion Files

| File                        | Required | Role                                                                          |
| --------------------------- | -------- | ----------------------------------------------------------------------------- |
| `itemnakmessageoffset.dbss` | Optional | `item_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`       | Optional | Item names (type `0`) and the message text (type `37`)                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                               |
| ------- | ---------- | ----- | ----------------------------------- |
| `+0x00` | u32        | count | Number of rows; `11` on client 3474 |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 20 bytes + message keys)

| Offset                  | Type  | Field            | Notes                                                                |
| ----------------------- | ----- | ---------------- | -------------------------------------------------------------------- |
| `+0x00`                 | u32   | item_key         | The item, an item enchant key (`enchant_level << 24 \| item_id`); level `0` on every row of clients 1784 and 3474 |
| `+0x04`                 | str16 | main_message_key | `GAME` sheet key of the main line, `NAKMESSAGE_LUXURYFIND_MAIN` on every row of client 3474 |
| `main_message_key+0x00` | str16 | sub_message_key  | `GAME` sheet key of the sub line, `NAKMESSAGE_LUXURYFIND_SUB_01` to `_09` on client 3474 |

The rows are not sorted by key. On client 3474 every row is 128 bytes
long, since all keys there have the same length; on client 1784 the rows
are 138 and 140 bytes.

### `itemnakmessageoffset.dbss`

`PABR` index with 12-byte rows and a u32 key.

| Offset              | Type              | Field              | Notes                                         |
| ------------------- | ----------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]           | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32               | count              | Equals the `itemnakmessage.dbss` count        |
| `+0x08`             | Offset Row[count] | rows               | See Offset Row                                |
| `rows+0x00`         | String Table      | string_table       | The PABR string table, present but empty      |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 12 x count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                    |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u32  | item_key    | Key of the row it points at                                  |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `itemnakmessage.dbss`, at its `item_key` |
| `+0x08` | u32  | data_size   | The whole row                                                |

Read by `parse_pabr_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in another order than the file; on clients 1784 and 3474
every index row points at the row with its key.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Field Names

The `BigNakMessage` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `itemkey`, `mainMsg` and `subMsg`, and its 8
rows match the 8 rows of client 1784 on all three columns. Client 3474 has
the same 8 items and 3 more (`53803`, `59418`, `65299`), and new keys in
both columns: the 1784 keys `LUA_NAKMESSAGE_LUXURYFIND_MAIN`, `_MAIN2` and
`_MAIN3` (three wordings of the adventurer's title) and the shared
`LUA_NAKMESSAGE_LUXURYFIND_SUB` became one `NAKMESSAGE_LUXURYFIND_MAIN` and
one `NAKMESSAGE_LUXURYFIND_SUB_NN` per item. The developer workbook
(`datasheet_bignakmessage.xlsm`) adds the note column `#itemname` with the
Korean item name. The field names here add `_key`, since the values are
string keys.

## Notes

- Every key on client 3474 is a `GAME` sheet row of `stringtable.bss`; the
  handler shows its LOC type 37 text, found by the key's hash.
- No client Lua names the table or its keys; the message window
  (`nakmessage_renewel.luac`) has a separate `__eNakMessage_RichMerchantRing`
  type for the Rich Merchant's Ring reward.
