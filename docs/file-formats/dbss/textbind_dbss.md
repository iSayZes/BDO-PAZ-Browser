# `textbind.dbss` Format

## Purpose

The Korean text of every TextBind name. LOC and inline text can name a text
instead of holding it, as `{TextBind:NAME}` or
`{StringTableBind(TextBind:NAME)}` (see `languagedata_loc.md`, Type 59). Each
record holds the text of one name in four variants. The English and other
translations are LOC type 59 with the same key; this file is the Korean source
and the fallback without LOC.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes     | Records          | Row bytes                      |
| ------ | -------------- | --------------------- | --------- | ---------------- | ------------------------------ |
| 1      | 1584 and later | `textbind.dbss`       | 1,953,258 | 1,169 Record     | 64 to 12,716, 1,671 on average |
| 1      | 1584 and later | `textbindoffset.dbss` | 14,032    | 1,169 Offset Row | 12                             |

| Layout | File                  | Known               | Unknown        |
| ------ | --------------------- | ------------------- | -------------- |
| 1      | `textbind.dbss`       | 1,948,582 B (99.8%) | 4,676 B (0.2%) |
| 1      | `textbindoffset.dbss` | 14,032 B (100.0%)   | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `4552e8931946`  |
| 3482   | Layout 1             | `4552e8931946`  |
| 3474   | Layout 1             | `4552e8931946`  |
| 3473   | Layout 1             | `4552e8931946`  |
| 3464   | Layout 1             | `4552e8931946`  |
| 3458   | Layout 1             | `4552e8931946`  |
| 3454   | Layout 1             | `4552e8931946`  |
| 3444   | Layout 1             | `4552e8931946`  |
| 3435   | Layout 1             | `4552e8931946`  |
| 3426   | Layout 1             | `4552e8931946`  |
| 3418   | Layout 1             | `4552e8931946`  |
| 3412   | Layout 1             | `4552e8931946`  |
| 3402   | Layout 1             | `4552e8931946`  |
| 3396   | Layout 1             | `4552e8931946`  |
| 3387   | Layout 1             | `4552e8931946`  |
| 3381   | Layout 1             | `4552e8931946`  |
| 3373   | Layout 1             | `4552e8931946`  |
| 3364   | Layout 1             | `4552e8931946`  |
| 3356   | Layout 1             | `4552e8931946`  |
| 3349   | Layout 1             | `4552e8931946`  |
| 3342   | Layout 1             | `4552e8931946`  |
| 3335   | Layout 1             | `4552e8931946`  |
| 3326   | Layout 1             | `4552e8931946`  |
| 3321   | Layout 1             | `4552e8931946`  |
| 3314   | Layout 1             | `4552e8931946`  |
| 3303   | Layout 1             | `4552e8931946`  |
| 3302   | Layout 1             | `4552e8931946`  |
| 3293   | Layout 1             | `4552e8931946`  |
| 3283   | Layout 1             | `4552e8931946`  |
| 3275   | Layout 1             | `4552e8931946`  |
| 3267   | Layout 1             | `4552e8931946`  |
| 3258   | Layout 1             | `4552e8931946`  |
| 3251   | Layout 1             | `4552e8931946`  |
| 3242   | Layout 1             | `4552e8931946`  |
| 3235   | Layout 1             | `4552e8931946`  |
| 3229   | Layout 1             | `4552e8931946`  |
| 3212   | Layout 1             | `4552e8931946`  |
| 3203   | Layout 1             | `4552e8931946`  |
| 3193   | Layout 1             | `4552e8931946`  |
| 3186   | Layout 1             | `4552e8931946`  |
| 3177   | Layout 1             | `4552e8931946`  |
| 3169   | Layout 1             | `4552e8931946`  |
| 3158   | Layout 1             | `4552e8931946`  |
| 3151   | Layout 1             | `4552e8931946`  |
| 3144   | Layout 1             | `4552e8931946`  |
| 3133   | Layout 1             | `4552e8931946`  |
| 3125   | Layout 1             | `4552e8931946`  |
| 3118   | Layout 1             | `4552e8931946`  |
| 3111   | Layout 1             | `4552e8931946`  |
| 3103   | Layout 1             | `4552e8931946`  |
| 3095   | Layout 1             | `4552e8931946`  |
| 3086   | Layout 1             | `4552e8931946`  |
| 3072   | Layout 1             | `4552e8931946`  |
| 3062   | Layout 1             | `4552e8931946`  |
| 3052   | Layout 1             | `4552e8931946`  |
| 3045   | Layout 1             | `4552e8931946`  |
| 3037   | Layout 1             | `4552e8931946`  |
| 3030   | Layout 1             | `4552e8931946`  |
| 3021   | Layout 1             | `4552e8931946`  |
| 3012   | Layout 1             | `4552e8931946`  |
| 3002   | Layout 1             | `4552e8931946`  |
| 2995   | Layout 1             | `4552e8931946`  |
| 2987   | Layout 1             | `4552e8931946`  |
| 2978   | Layout 1             | `4552e8931946`  |
| 2970   | Layout 1             | `4552e8931946`  |
| 2959   | Layout 1             | `4552e8931946`  |
| 2951   | Layout 1             | `4552e8931946`  |
| 2942   | Layout 1             | `4552e8931946`  |
| 2935   | Layout 1             | `4552e8931946`  |
| 2932   | Layout 1             | `4552e8931946`  |
| 2923   | Layout 1             | `4552e8931946`  |
| 2919   | Layout 1             | `4552e8931946`  |
| 2907   | Layout 1             | `4552e8931946`  |
| 2900   | Layout 1             | `4552e8931946`  |
| 2891   | Layout 1             | `4552e8931946`  |
| 2882   | Layout 1             | `4552e8931946`  |
| 2872   | Layout 1             | `4552e8931946`  |
| 2863   | Layout 1             | `4552e8931946`  |
| 2855   | Layout 1             | `4552e8931946`  |
| 2849   | Layout 1             | `4552e8931946`  |
| 2844   | Layout 1             | `4552e8931946`  |
| 2834   | Layout 1             | `4552e8931946`  |
| 2825   | Layout 1             | `4552e8931946`  |
| 2819   | Layout 1             | `4552e8931946`  |
| 2811   | Layout 1             | `4552e8931946`  |
| 2803   | Layout 1             | `4552e8931946`  |
| 2794   | Layout 1             | `4552e8931946`  |
| 2783   | Layout 1             | `4552e8931946`  |
| 2774   | Layout 1             | `4552e8931946`  |
| 2765   | Layout 1             | `4552e8931946`  |
| 2756   | Layout 1             | `4552e8931946`  |
| 2750   | Layout 1             | `4552e8931946`  |
| 2743   | Layout 1             | `4552e8931946`  |
| 2736   | Layout 1             | `4552e8931946`  |
| 2726   | Layout 1             | `4552e8931946`  |
| 2717   | Layout 1             | `4552e8931946`  |
| 2709   | Layout 1             | `4552e8931946`  |
| 2703   | Layout 1             | `4552e8931946`  |
| 2695   | Layout 1             | `4552e8931946`  |
| 2684   | Layout 1             | `4552e8931946`  |
| 2672   | Layout 1             | `4552e8931946`  |
| 2665   | Layout 1             | `4552e8931946`  |
| 2657   | Layout 1             | `4552e8931946`  |
| 2649   | Layout 1             | `4552e8931946`  |
| 2644   | Layout 1             | `4552e8931946`  |
| 2637   | Layout 1             | `4552e8931946`  |
| 2629   | Layout 1             | `4552e8931946`  |
| 2619   | Layout 1             | `4552e8931946`  |
| 2612   | Layout 1             | `4552e8931946`  |
| 2606   | Layout 1             | `4552e8931946`  |
| 2602   | Layout 1             | `4552e8931946`  |
| 2601   | Layout 1             | `4552e8931946`  |
| 2592   | Layout 1             | `4552e8931946`  |
| 2583   | Layout 1             | `4552e8931946`  |
| 2575   | Layout 1             | `4552e8931946`  |
| 2567   | Layout 1             | `4552e8931946`  |
| 2560   | Layout 1             | `4552e8931946`  |
| 2553   | Layout 1             | `4552e8931946`  |
| 2545   | Layout 1             | `4552e8931946`  |
| 2538   | Layout 1             | `4552e8931946`  |
| 2529   | Layout 1             | `4552e8931946`  |
| 2519   | Layout 1             | `4552e8931946`  |
| 2513   | Layout 1             | `4552e8931946`  |
| 2510   | Layout 1             | `4552e8931946`  |
| 2507   | Layout 1             | `4552e8931946`  |
| 2503   | Layout 1             | `4552e8931946`  |
| 2498   | Layout 1             | `4552e8931946`  |
| 2492   | Layout 1             | `4552e8931946`  |
| 2487   | Layout 1             | `4552e8931946`  |
| 2480   | Layout 1             | `4552e8931946`  |
| 2474   | Layout 1             | `4552e8931946`  |
| 2468   | Layout 1             | `4552e8931946`  |
| 2460   | Layout 1             | `4552e8931946`  |
| 2453   | Layout 1             | `4552e8931946`  |
| 2444   | Layout 1             | `4552e8931946`  |
| 2438   | Layout 1             | `4552e8931946`  |
| 2434   | Layout 1             | `4552e8931946`  |
| 2429   | Layout 1             | `4552e8931946`  |
| 2421   | Layout 1             | `4552e8931946`  |
| 2414   | Layout 1             | `4552e8931946`  |
| 2407   | Layout 1             | `4552e8931946`  |
| 2401   | Layout 1             | `4552e8931946`  |
| 2397   | Layout 1             | `4552e8931946`  |
| 2393   | Layout 1             | `4552e8931946`  |
| 2384   | Layout 1             | `4552e8931946`  |
| 2378   | Layout 1             | `4552e8931946`  |
| 2372   | Layout 1             | `4552e8931946`  |
| 2358   | Layout 1             | `4552e8931946`  |
| 2352   | Layout 1             | `4552e8931946`  |
| 2347   | Layout 1             | `4552e8931946`  |
| 2343   | Layout 1             | `4552e8931946`  |
| 2335   | Layout 1             | `4552e8931946`  |
| 2327   | Layout 1             | `4552e8931946`  |
| 2324   | Layout 1             | `4552e8931946`  |
| 2319   | Layout 1             | `4552e8931946`  |
| 2313   | Layout 1             | `4552e8931946`  |
| 2308   | Layout 1             | `4552e8931946`  |
| 2302   | Layout 1             | `4552e8931946`  |
| 2295   | Layout 1             | `4552e8931946`  |
| 2290   | Layout 1             | `4552e8931946`  |
| 2284   | Layout 1             | `4552e8931946`  |
| 2276   | Layout 1             | `4552e8931946`  |
| 2269   | Layout 1             | `4552e8931946`  |
| 2259   | Layout 1             | `4552e8931946`  |
| 2250   | Layout 1             | `4552e8931946`  |
| 2243   | Layout 1             | `4552e8931946`  |
| 2235   | Layout 1             | `4552e8931946`  |
| 2229   | Layout 1             | `4552e8931946`  |
| 2224   | Layout 1             | `4552e8931946`  |
| 2218   | Layout 1             | `4552e8931946`  |
| 2215   | Layout 1             | `4552e8931946`  |
| 2207   | Layout 1             | `4552e8931946`  |
| 2203   | Layout 1             | `4552e8931946`  |
| 2196   | Layout 1             | `4552e8931946`  |
| 2192   | Layout 1             | `4552e8931946`  |
| 2189   | Layout 1             | `4552e8931946`  |
| 2183   | Layout 1             | `4552e8931946`  |
| 2179   | Layout 1             | `4552e8931946`  |
| 2171   | Layout 1             | `4552e8931946`  |
| 2163   | Layout 1             | `4552e8931946`  |
| 2156   | Layout 1             | `4552e8931946`  |
| 2151   | Layout 1             | `4552e8931946`  |
| 2147   | Layout 1             | `4552e8931946`  |
| 2142   | Layout 1             | `4552e8931946`  |
| 2138   | Layout 1             | `4552e8931946`  |
| 2134   | Layout 1             | `4552e8931946`  |
| 2130   | Layout 1             | `4552e8931946`  |
| 2122   | Layout 1             | `4552e8931946`  |
| 2107   | Layout 1             | `4552e8931946`  |
| 2098   | Layout 1             | `4552e8931946`  |
| 2089   | Layout 1             | `4552e8931946`  |
| 2081   | Layout 1             | `4552e8931946`  |
| 2073   | Layout 1             | `4552e8931946`  |
| 2067   | Layout 1             | `4552e8931946`  |
| 2063   | Layout 1             | `4552e8931946`  |
| 2059   | Layout 1             | `4552e8931946`  |
| 2052   | Layout 1             | `4552e8931946`  |
| 2044   | Layout 1             | `4552e8931946`  |
| 2039   | Layout 1             | `4552e8931946`  |
| 2032   | Layout 1             | `4552e8931946`  |
| 2025   | Layout 1             | `4552e8931946`  |
| 2011   | Layout 1             | `4552e8931946`  |
| 2005   | Layout 1             | `4552e8931946`  |
| 2000   | Layout 1             | `4552e8931946`  |
| 1996   | Layout 1             | `4552e8931946`  |
| 1991   | Layout 1             | `4552e8931946`  |
| 1985   | Layout 1             | `4552e8931946`  |
| 1980   | Layout 1             | `4552e8931946`  |
| 1969   | Layout 1             | `4552e8931946`  |
| 1964   | Layout 1             | `4552e8931946`  |
| 1958   | Layout 1             | `4552e8931946`  |
| 1950   | Layout 1             | `4552e8931946`  |
| 1945   | Layout 1             | `4552e8931946`  |
| 1937   | Layout 1             | `4552e8931946`  |
| 1933   | Layout 1             | `4552e8931946`  |
| 1927   | Layout 1             | `4552e8931946`  |
| 1921   | Layout 1             | `4552e8931946`  |
| 1914   | Layout 1             | `4552e8931946`  |
| 1908   | Layout 1             | `4552e8931946`  |
| 1897   | Layout 1             | `4552e8931946`  |
| 1892   | Layout 1             | `4552e8931946`  |
| 1886   | Layout 1             | `4552e8931946`  |
| 1881   | Layout 1             | `4552e8931946`  |
| 1871   | Layout 1             | `4552e8931946`  |
| 1866   | Layout 1             | `4552e8931946`  |
| 1862   | Layout 1             | `4552e8931946`  |
| 1854   | Layout 1             | `4552e8931946`  |
| 1846   | Layout 1             | `4552e8931946`  |
| 1838   | Layout 1             | `4552e8931946`  |
| 1832   | Layout 1             | `4552e8931946`  |
| 1826   | Layout 1             | `4552e8931946`  |
| 1822   | Layout 1             | `4552e8931946`  |
| 1818   | Layout 1             | `4552e8931946`  |
| 1804   | Layout 1             | `4552e8931946`  |
| 1794   | Layout 1             | `4552e8931946`  |
| 1790   | Layout 1             | `4552e8931946`  |
| 1784   | Layout 1             | `4552e8931946`  |
| 1774   | Layout 1             | `4552e8931946`  |
| 1771   | Layout 1             | `4552e8931946`  |
| 1762   | Layout 1             | `4552e8931946`  |
| 1759   | Layout 1             | `4552e8931946`  |
| 1754   | Layout 1             | `4552e8931946`  |
| 1749   | Layout 1             | `4552e8931946`  |
| 1743   | Layout 1             | `4552e8931946`  |
| 1737   | Layout 1             | `4552e8931946`  |
| 1731   | Layout 1             | `4552e8931946`  |
| 1725   | Layout 1             | `4552e8931946`  |
| 1717   | Layout 1             | `4552e8931946`  |
| 1710   | Layout 1             | `4552e8931946`  |
| 1704   | Layout 1             | `4552e8931946`  |
| 1698   | Layout 1             | `4552e8931946`  |
| 1690   | Layout 1             | `4552e8931946`  |
| 1685   | Layout 1             | `4552e8931946`  |
| 1680   | Layout 1             | `4552e8931946`  |
| 1674   | Layout 1             | `4552e8931946`  |
| 1668   | Layout 1             | `4552e8931946`  |
| 1659   | Layout 1             | `4552e8931946`  |
| 1649   | Layout 1             | `4552e8931946`  |
| 1642   | Layout 1             | `4552e8931946`  |
| 1636   | Layout 1             | `4552e8931946`  |
| 1628   | Layout 1             | `4552e8931946`  |
| 1622   | Layout 1             | `4552e8931946`  |
| 1614   | Layout 1             | `4552e8931946`  |
| 1608   | Layout 1             | `4552e8931946`  |
| 1602   | Layout 1             | `4552e8931946`  |
| 1598   | Layout 1             | `4552e8931946`  |
| 1594   | Layout 1             | `4552e8931946`  |
| 1590   | Layout 1             | `4552e8931946`  |
| 1587   | Layout 1             | `4552e8931946`  |
| 1584   | Layout 1             | `4552e8931946`  |
| 1579   | No documented layout | `4552e8931946`  |
| 1572   | No documented layout | `4552e8931946`  |
| 1565   | No documented layout | `4552e8931946`  |
| 1559   | No documented layout | `4552e8931946`  |
| 1554   | No documented layout | `4552e8931946`  |
| 1547   | No documented layout | `4552e8931946`  |
| 1537   | No documented layout | `4552e8931946`  |
| 1529   | No documented layout | `4552e8931946`  |
| 1524   | No documented layout | `4552e8931946`  |
| 1519   | No documented layout | `4552e8931946`  |
| 1509   | No documented layout | `4552e8931946`  |
| 1506   | No documented layout | `4552e8931946`  |
| 1504   | No documented layout | `4552e8931946`  |
| 1500   | No documented layout | `4552e8931946`  |
| 1493   | No documented layout | `4552e8931946`  |
| 1489   | No documented layout | `4552e8931946`  |
| 1485   | No documented layout | `4552e8931946`  |
| 1481   | No documented layout | `4552e8931946`  |
| 1474   | No documented layout | `4552e8931946`  |
| 1466   | No documented layout | `4552e8931946`  |
| 1462   | No documented layout | `4552e8931946`  |
| 1459   | No documented layout | `4552e8931946`  |
| 1453   | No documented layout | `4552e8931946`  |
| 1450   | No documented layout | `4552e8931946`  |
| 1445   | No documented layout | `4552e8931946`  |
| 1439   | No documented layout | `4552e8931946`  |
| 1433   | No documented layout | `4552e8931946`  |
| 1430   | No documented layout | `4552e8931946`  |
| 1426   | No documented layout | `4552e8931946`  |
| 1421   | No documented layout | `4552e8931946`  |
| 1417   | No documented layout | `4552e8931946`  |
| 1416   | No documented layout | `4552e8931946`  |
| 1409   | No documented layout | `4552e8931946`  |
| 1405   | No documented layout | `4552e8931946`  |
| 1401   | No documented layout | `4552e8931946`  |
| 1396   | No documented layout | `4552e8931946`  |
| 1391   | No documented layout | `4552e8931946`  |
| 1390   | No documented layout | `4552e8931946`  |
| 1386   | No documented layout | `4552e8931946`  |
| 1381   | No documented layout | `4552e8931946`  |
| 1379   | No documented layout | `4552e8931946`  |
| 1372   | No documented layout | `4552e8931946`  |
| 1366   | No documented layout | `4552e8931946`  |
| 1364   | No documented layout | `4552e8931946`  |
| 1363   | No documented layout | `4552e8931946`  |
| 1360   | No documented layout | `4552e8931946`  |
| 1358   | No documented layout | `4552e8931946`  |
| 1355   | No documented layout | `4552e8931946`  |
| 1351   | No documented layout | `4552e8931946`  |
| 1348   | No documented layout | `4552e8931946`  |
| 1346   | No documented layout | `4552e8931946`  |
| 1341   | No documented layout | `4552e8931946`  |
| 1340   | No documented layout | `4552e8931946`  |
| 1338   | No documented layout | `4552e8931946`  |
| 1335   | No documented layout | `4552e8931946`  |
| 1333   | No documented layout | `4552e8931946`  |
| 1329   | No documented layout | `4552e8931946`  |
| 1327   | No documented layout | `4552e8931946`  |
| 1324   | No documented layout | `4552e8931946`  |
| 1321   | No documented layout | `4552e8931946`  |
| 1319   | No documented layout | `4552e8931946`  |
| 1318   | No documented layout | `4552e8931946`  |
| 1316   | No documented layout | `4552e8931946`  |
| 1313   | No documented layout | `4552e8931946`  |
| 1311   | No documented layout | `4552e8931946`  |
| 1309   | No documented layout | `4552e8931946`  |
| 1304   | No documented layout | `4552e8931946`  |
| 1292   | No documented layout | `4552e8931946`  |
| 1286   | No documented layout | `4552e8931946`  |
| 1280   | No documented layout | `4552e8931946`  |
| 1276   | No documented layout | `4552e8931946`  |
| 1267   | No file              | `4552e8931946`  |
| 1261   | No file              | `4552e8931946`  |
| 1256   | No file              | `4552e8931946`  |
| 1250   | No file              | `4552e8931946`  |
| 1246   | No file              | `4552e8931946`  |
| 1239   | No file              | `4552e8931946`  |
| 1230   | No file              | `4552e8931946`  |
| 1226   | No file              | `4552e8931946`  |
| 1220   | No file              | `4552e8931946`  |
| 1217   | No file              | `4552e8931946`  |
| 1211   | No file              | `4552e8931946`  |
| 1210   | No file              | `4552e8931946`  |
| 1208   | No file              | `4552e8931946`  |
| 1203   | No file              | `4552e8931946`  |
| 1197   | No file              | `4552e8931946`  |
| 1194   | No file              | `4552e8931946`  |
| 1192   | No file              | `4552e8931946`  |
| 1187   | No file              | `4552e8931946`  |
| 1183   | No file              | `4552e8931946`  |
| 1177   | No file              | `4552e8931946`  |
| 1173   | No file              | `4552e8931946`  |
| 1167   | No file              | `4552e8931946`  |
| 1164   | No file              | `4552e8931946`  |
| 1156   | No file              | `4552e8931946`  |
| 1149   | No file              | `4552e8931946`  |
| 1144   | No file              | `4552e8931946`  |
| 1137   | No file              | `4552e8931946`  |
| 1132   | No file              | `4552e8931946`  |
| 1127   | No file              | `4552e8931946`  |
| 1122   | No file              | `4552e8931946`  |
| 1118   | No file              | `4552e8931946`  |
| 1114   | No file              | `4552e8931946`  |
| 1109   | No file              | `4552e8931946`  |
| 1102   | No file              | `4552e8931946`  |
| 1096   | No file              | `4552e8931946`  |
| 1088   | No file              | `4552e8931946`  |
| 1081   | No file              | `4552e8931946`  |
| 1076   | No file              | `4552e8931946`  |
| 1069   | No file              | `4552e8931946`  |
| 1064   | No file              | `4552e8931946`  |
| 1058   | No file              | `4552e8931946`  |
| 1051   | No file              | `4552e8931946`  |
| 1044   | No file              | `4552e8931946`  |
| 1036   | No file              | `4552e8931946`  |
| 1026   | No file              | `4552e8931946`  |
| 1016   | No file              | `4552e8931946`  |
| 1009   | No file              | `4552e8931946`  |
| 1005   | No file              | `4552e8931946`  |
| 1000   | No file              | `4552e8931946`  |
| 998    | No file              | `4552e8931946`  |
| 990    | No file              | `4552e8931946`  |
| 979    | No file              | `4552e8931946`  |
| 972    | No file              | `4552e8931946`  |
| 963    | No file              | `4552e8931946`  |
| 955    | No file              | `4552e8931946`  |
| 946    | No file              | `4552e8931946`  |
| 938    | No file              | `4552e8931946`  |
| 927    | No file              | `4552e8931946`  |
| 911    | No file              | `4552e8931946`  |
| 904    | No file              | `4552e8931946`  |
| 899    | No file              | `4552e8931946`  |
| 894    | No file              | `4552e8931946`  |
| 885    | No file              | `4552e8931946`  |
| 879    | No file              | `4552e8931946`  |
| 872    | No file              | `4552e8931946`  |
| 864    | No file              | `4552e8931946`  |
| 855    | No file              | `4552e8931946`  |
| 853    | No file              | `4552e8931946`  |
| 845    | No file              | `4552e8931946`  |
| 837    | No file              | `4552e8931946`  |
| 829    | No file              | `4552e8931946`  |
| 822    | No file              | `4552e8931946`  |
| 814    | No file              | `4552e8931946`  |
| 805    | No file              | `4552e8931946`  |
| 794    | No file              | `4552e8931946`  |
| 787    | No file              | `4552e8931946`  |
| 780    | No file              | `4552e8931946`  |
| 771    | No file              | `4552e8931946`  |
| 760    | No file              | `4552e8931946`  |
| 748    | No file              | `4552e8931946`  |
| 741    | No file              | `4552e8931946`  |
| 736    | No file              | `4552e8931946`  |
| 731    | No file              | `4552e8931946`  |
| 723    | No file              | `4552e8931946`  |
| 711    | No file              | `4552e8931946`  |
| 707    | No file              | `4552e8931946`  |
| 697    | No file              | `4552e8931946`  |
| 689    | No file              | `4552e8931946`  |
| 683    | No file              | `4552e8931946`  |
| 678    | No file              | `4552e8931946`  |
| 670    | No file              | `4552e8931946`  |
| 661    | No file              | `4552e8931946`  |
| 656    | No file              | `4552e8931946`  |
| 652    | No file              | `4552e8931946`  |
| 643    | No file              | `4552e8931946`  |
| 637    | No file              | `4552e8931946`  |
| 630    | No file              | `4552e8931946`  |
| 627    | No file              | `4552e8931946`  |
| 621    | No file              | `4552e8931946`  |
| 617    | No file              | `4552e8931946`  |
| 615    | No file              | `4552e8931946`  |
| 606    | No file              | `4552e8931946`  |
| 599    | No file              | `4552e8931946`  |
| 592    | No file              | `4552e8931946`  |
| 586    | No file              | `4552e8931946`  |
| 577    | No file              | `4552e8931946`  |
| 569    | No file              | `4552e8931946`  |
| 561    | No file              | `4552e8931946`  |
| 554    | No file              | `4552e8931946`  |
| 542    | No file              | `4552e8931946`  |
| 532    | No file              | `4552e8931946`  |
| 531    | No file              | `4552e8931946`  |
| 526    | No file              | `4552e8931946`  |
| 521    | No file              | `4552e8931946`  |
| 517    | No file              | `4552e8931946`  |
| 510    | No file              | `4552e8931946`  |
| 508    | No file              | `4552e8931946`  |
| 504    | No file              | `4552e8931946`  |
| 497    | No file              | `4552e8931946`  |
| 491    | No file              | `4552e8931946`  |
| 485    | No file              | `4552e8931946`  |
| 478    | No file              | `4552e8931946`  |
| 472    | No file              | `4552e8931946`  |
| 466    | No file              | `4552e8931946`  |
| 457    | No file              | `4552e8931946`  |
| 452    | No file              | `4552e8931946`  |
| 449    | No file              | `4552e8931946`  |
| 435    | No file              | `4552e8931946`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `textbindoffset.dbss` | Optional | `key -> (offset, size)` index; records also read in order without it |
| `languagedata_*.loc`  | Optional | Type 59: the same texts in the user language, `str_id4` = variant |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                |
| ------- | ------------- | ------- | ------------------------------------ |
| `+0x00` | u32           | count   | `1,166` on client 3464               |
| `+0x04` | Record[count] | records | Back to back, no padding; see Record |

The records tile the file: the first starts at `0x04` and the last ends at
the end of the file (1,951,374 bytes on client 3464).

### Record (variable: 40 bytes + texts)

| Offset           | Type  | Field                 | Notes |
| ---------------- | ----- | --------------------- | ----- |
| `+0x00`          | u32   | key                   | `key_hash()` of the TextBind name: lookup3 `hashlittle` over the UTF-16LE name, seed `0xC5EDE`, the `stringtable.bss` key hash. LOC type 59 `str_id1` |
| `+0x04`          | str16 | variant_0             | PC text, see Variants |
| `variant_0+0x00` | str16 | variant_1             | PlayStation text, see Variants |
| `variant_1+0x00` | str16 | variant_2             | Console text, see Variants |
| `variant_2+0x00` | u32   | unknown_pre_variant_3 | `0` on all 1,166 records (client 3464) |
| `variant_2+0x04` | str16 | variant_3             | See Variants |

Each string is a u64 length in UTF-16 code units followed by that many
UTF-16LE units, no terminator (`RecordReader.text(wide=True)`). The
`unknown_pre_variant_3` u32 has no fixed offset; it follows the end of
`variant_2`.

### `textbindoffset.dbss`

| Offset  | Type              | Field | Notes                         |
| ------- | ----------------- | ----- | ----------------------------- |
| `+0x00` | u32               | count | Same count as `textbind.dbss` |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                |

No PABR magic. The rows are not in file order or key order; sorted by
`offset` they tile `textbind.dbss` from `0x04` to its end. Read with
`parse_bare_u32_offset_rows()`.

### Offset Row (12 bytes)

| Offset  | Type | Field  | Notes                                        |
| ------- | ---- | ------ | -------------------------------------------- |
| `+0x00` | u32  | key    | Record key, repeated per row                 |
| `+0x04` | u32  | offset | Byte offset of the record in `textbind.dbss` |
| `+0x08` | u32  | size   | Byte size of the record                      |

## Variants

Counted on client 3464:

| Variant | Platform     | Evidence |
| ------- | ------------ | -------- |
| 0       | PC           | Key hints name the mouse actions (`{KeyBind:Attack1}` 235 times, `{KeyBind:Attack2}` 173, `{KeyBind:Confirm}` once). The `TextBind_Table` of a private server on client 519 has `Key`, `PC` and `Console` columns; its `PC` text equals variant 0 on 233 of the 258 names both hold, and the other 25 differ by later wording changes (`말` to `탑승물`) |
| 1       | PlayStation  | The only variant with `컨트롤러` (12 records, the others say `게임 패드`), `DUALSHOCK` and PlayStation names (4 records), and never `xbox` (variants 0, 2 and 3 have it in 11 records each). Key hints use `{KeyBind:Confirm}` 106 times |
| 2       | Console      | Differs from variant 1 in 82 records: it says `게임 패드` where variant 1 says `컨트롤러` or `DUALSHOCK™4`, and holds `xbox` in 11 records. Key hints use `{KeyBind:Confirm}` 104 times |
| 3       | Not known    | Equal to variant 0 in 1,010 records and to variant 1 in 777; see Open Questions |

All four variants are equal in 635 records. Every record has a non-empty
variant 0. 452 variants hold another TextBind placeholder.

## Notes

- The TextBind name is not stored; only its hash is. Names appear in the
  placeholders that use them, such as `GROWTHPASS_PC_CONSOLE_SEP1` in quest
  4470 / 3.
- LOC type 59 holds 1,203 names on client 3464: all 1,166 of this file and 37
  more with no Korean record.
- The `TEXT_BIND_KR` lookup index maps `key` to the Korean variant 0 text.
  `resolve_text_binds()` in `_common/loc.py` falls back to it when LOC is not
  loaded or has no type 59 text for a name.
- No client Lua script mentions TextBind or picks a variant; the game fills
  placeholders itself.

## Open Questions

### Variant 3

Variant 3 matches variant 0 in 1,010 records, but in 14 records it swaps the
mouse hints for pad buttons (`{KeyBind:Dash}+{KeyBind:Attack2}` becomes
`{KeyBind:Symbol_LT}+{KeyBind:Symbol_X}`), and the chat tip record says
`눌러보세요` ("press") where variant 0 says `클릭해보세요` ("click"). It may be the PC text
for a gamepad player, or the Xbox text with variant 2 being something else.

### `unknown_pre_variant_3`

The u32 between variants 2 and 3 is `0` on every record of client 3464, so
its meaning cannot be read from the data.
