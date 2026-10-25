# `hardcorerandomspawncharacterstaticstatusmanager.bss` Format

## Purpose

The characters that spawn at random on the Hardcore channel, one 19-byte
row each: the character, five string-table references (world map icon,
boss icon, notice background and two notice keys) and a random spawn key.
Two key lists follow the rows, the bosses and the NPCs, then a list of
string-table indexes. On client 3474 the 12 rows are four Wandering
Merchants and six Lights of Offering on the NPC list, and the bosses
Laytenn and Ancient Puturum. The characters are
[`characterstatic.dbss`](characterstatic_dbss.md) keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                                  | Bytes | Records | Row bytes |
| ------ | -------------- | ----------------------------------------------------- | ----- | ------- | --------- |
| 1      | 2849 and later | `hardcorerandomspawncharacterstaticstatusmanager.bss` | 1,620 | 12 Row  | 19        |

| Layout | File                                                  | Known           | Unknown      |
| ------ | ----------------------------------------------------- | --------------- | ------------ |
| 1      | `hardcorerandomspawncharacterstaticstatusmanager.bss` | 1,516 B (93.6%) | 104 B (6.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `38f151638b7b`  |
| 3482   | Layout 1             | `38f151638b7b`  |
| 3474   | Layout 1             | `38f151638b7b`  |
| 3473   | Layout 1             | `38f151638b7b`  |
| 3464   | Layout 1             | `38f151638b7b`  |
| 3458   | Layout 1             | `38f151638b7b`  |
| 3454   | Layout 1             | `38f151638b7b`  |
| 3444   | Layout 1             | `38f151638b7b`  |
| 3435   | Layout 1             | `38f151638b7b`  |
| 3426   | Layout 1             | `38f151638b7b`  |
| 3418   | Layout 1             | `38f151638b7b`  |
| 3412   | Layout 1             | `38f151638b7b`  |
| 3402   | Layout 1             | `38f151638b7b`  |
| 3396   | Layout 1             | `38f151638b7b`  |
| 3387   | Layout 1             | `38f151638b7b`  |
| 3381   | Layout 1             | `38f151638b7b`  |
| 3373   | Layout 1             | `38f151638b7b`  |
| 3364   | Layout 1             | `38f151638b7b`  |
| 3356   | Layout 1             | `38f151638b7b`  |
| 3349   | Layout 1             | `38f151638b7b`  |
| 3342   | Layout 1             | `38f151638b7b`  |
| 3335   | Layout 1             | `38f151638b7b`  |
| 3326   | Layout 1             | `38f151638b7b`  |
| 3321   | Layout 1             | `38f151638b7b`  |
| 3314   | Layout 1             | `38f151638b7b`  |
| 3303   | Layout 1             | `38f151638b7b`  |
| 3302   | Layout 1             | `38f151638b7b`  |
| 3293   | Layout 1             | `38f151638b7b`  |
| 3283   | Layout 1             | `38f151638b7b`  |
| 3275   | Layout 1             | `38f151638b7b`  |
| 3267   | Layout 1             | `38f151638b7b`  |
| 3258   | Layout 1             | `38f151638b7b`  |
| 3251   | Layout 1             | `38f151638b7b`  |
| 3242   | Layout 1             | `38f151638b7b`  |
| 3235   | Layout 1             | `38f151638b7b`  |
| 3229   | Layout 1             | `38f151638b7b`  |
| 3212   | Layout 1             | `38f151638b7b`  |
| 3203   | Layout 1             | `38f151638b7b`  |
| 3193   | Layout 1             | `38f151638b7b`  |
| 3186   | Layout 1             | `38f151638b7b`  |
| 3177   | Layout 1             | `38f151638b7b`  |
| 3169   | Layout 1             | `38f151638b7b`  |
| 3158   | Layout 1             | `38f151638b7b`  |
| 3151   | Layout 1             | `38f151638b7b`  |
| 3144   | Layout 1             | `38f151638b7b`  |
| 3133   | Layout 1             | `38f151638b7b`  |
| 3125   | Layout 1             | `38f151638b7b`  |
| 3118   | Layout 1             | `38f151638b7b`  |
| 3111   | Layout 1             | `38f151638b7b`  |
| 3103   | Layout 1             | `38f151638b7b`  |
| 3095   | Layout 1             | `38f151638b7b`  |
| 3086   | Layout 1             | `38f151638b7b`  |
| 3072   | Layout 1             | `38f151638b7b`  |
| 3062   | Layout 1             | `38f151638b7b`  |
| 3052   | Layout 1             | `38f151638b7b`  |
| 3045   | Layout 1             | `38f151638b7b`  |
| 3037   | Layout 1             | `38f151638b7b`  |
| 3030   | Layout 1             | `38f151638b7b`  |
| 3021   | Layout 1             | `38f151638b7b`  |
| 3012   | Layout 1             | `38f151638b7b`  |
| 3002   | Layout 1             | `38f151638b7b`  |
| 2995   | Layout 1             | `38f151638b7b`  |
| 2987   | Layout 1             | `38f151638b7b`  |
| 2978   | Layout 1             | `38f151638b7b`  |
| 2970   | Layout 1             | `38f151638b7b`  |
| 2959   | Layout 1             | `38f151638b7b`  |
| 2951   | Layout 1             | `38f151638b7b`  |
| 2942   | Layout 1             | `38f151638b7b`  |
| 2935   | Layout 1             | `38f151638b7b`  |
| 2932   | Layout 1             | `38f151638b7b`  |
| 2923   | Layout 1             | `38f151638b7b`  |
| 2919   | Layout 1             | `38f151638b7b`  |
| 2907   | Layout 1             | `38f151638b7b`  |
| 2900   | Layout 1             | `38f151638b7b`  |
| 2891   | Layout 1             | `38f151638b7b`  |
| 2882   | Layout 1             | `38f151638b7b`  |
| 2872   | Layout 1             | `38f151638b7b`  |
| 2863   | Layout 1             | `38f151638b7b`  |
| 2855   | Layout 1             | `38f151638b7b`  |
| 2849   | Layout 1             | `38f151638b7b`  |
| 2844   | No documented layout | `38f151638b7b`  |
| 2834   | No documented layout | `38f151638b7b`  |
| 2825   | No file              | `38f151638b7b`  |
| 2819   | No file              | `38f151638b7b`  |
| 2811   | No file              | `38f151638b7b`  |
| 2803   | No file              | `38f151638b7b`  |
| 2794   | No file              | `38f151638b7b`  |
| 2783   | No file              | `38f151638b7b`  |
| 2774   | No file              | `38f151638b7b`  |
| 2765   | No file              | `38f151638b7b`  |
| 2756   | No file              | `38f151638b7b`  |
| 2750   | No file              | `38f151638b7b`  |
| 2743   | No file              | `38f151638b7b`  |
| 2736   | No file              | `38f151638b7b`  |
| 2726   | No file              | `38f151638b7b`  |
| 2717   | No file              | `38f151638b7b`  |
| 2709   | No file              | `38f151638b7b`  |
| 2703   | No file              | `38f151638b7b`  |
| 2695   | No file              | `38f151638b7b`  |
| 2684   | No file              | `38f151638b7b`  |
| 2672   | No file              | `38f151638b7b`  |
| 2665   | No file              | `38f151638b7b`  |
| 2657   | No file              | `38f151638b7b`  |
| 2649   | No file              | `38f151638b7b`  |
| 2644   | No file              | `38f151638b7b`  |
| 2637   | No file              | `38f151638b7b`  |
| 2629   | No file              | `38f151638b7b`  |
| 2619   | No file              | `38f151638b7b`  |
| 2612   | No file              | `38f151638b7b`  |
| 2606   | No file              | `38f151638b7b`  |
| 2602   | No file              | `38f151638b7b`  |
| 2601   | No file              | `38f151638b7b`  |
| 2592   | No file              | `38f151638b7b`  |
| 2583   | No file              | `38f151638b7b`  |
| 2575   | No file              | `38f151638b7b`  |
| 2567   | No file              | `38f151638b7b`  |
| 2560   | No file              | `38f151638b7b`  |
| 2553   | No file              | `38f151638b7b`  |
| 2545   | No file              | `38f151638b7b`  |
| 2538   | No file              | `38f151638b7b`  |
| 2529   | No file              | `38f151638b7b`  |
| 2519   | No file              | `38f151638b7b`  |
| 2513   | No file              | `38f151638b7b`  |
| 2510   | No file              | `38f151638b7b`  |
| 2507   | No file              | `38f151638b7b`  |
| 2503   | No file              | `38f151638b7b`  |
| 2498   | No file              | `38f151638b7b`  |
| 2492   | No file              | `38f151638b7b`  |
| 2487   | No file              | `38f151638b7b`  |
| 2480   | No file              | `38f151638b7b`  |
| 2474   | No file              | `38f151638b7b`  |
| 2468   | No file              | `38f151638b7b`  |
| 2460   | No file              | `38f151638b7b`  |
| 2453   | No file              | `38f151638b7b`  |
| 2444   | No file              | `38f151638b7b`  |
| 2438   | No file              | `38f151638b7b`  |
| 2434   | No file              | `38f151638b7b`  |
| 2429   | No file              | `38f151638b7b`  |
| 2421   | No file              | `38f151638b7b`  |
| 2414   | No file              | `38f151638b7b`  |
| 2407   | No file              | `38f151638b7b`  |
| 2401   | No file              | `38f151638b7b`  |
| 2397   | No file              | `38f151638b7b`  |
| 2393   | No file              | `38f151638b7b`  |
| 2384   | No file              | `38f151638b7b`  |
| 2378   | No file              | `38f151638b7b`  |
| 2372   | No file              | `38f151638b7b`  |
| 2358   | No file              | `38f151638b7b`  |
| 2352   | No file              | `38f151638b7b`  |
| 2347   | No file              | `38f151638b7b`  |
| 2343   | No file              | `38f151638b7b`  |
| 2335   | No file              | `38f151638b7b`  |
| 2327   | No file              | `38f151638b7b`  |
| 2324   | No file              | `38f151638b7b`  |
| 2319   | No file              | `38f151638b7b`  |
| 2313   | No file              | `38f151638b7b`  |
| 2308   | No file              | `38f151638b7b`  |
| 2302   | No file              | `38f151638b7b`  |
| 2295   | No file              | `38f151638b7b`  |
| 2290   | No file              | `38f151638b7b`  |
| 2284   | No file              | `38f151638b7b`  |
| 2276   | No file              | `38f151638b7b`  |
| 2269   | No file              | `38f151638b7b`  |
| 2259   | No file              | `38f151638b7b`  |
| 2250   | No file              | `38f151638b7b`  |
| 2243   | No file              | `38f151638b7b`  |
| 2235   | No file              | `38f151638b7b`  |
| 2229   | No file              | `38f151638b7b`  |
| 2224   | No file              | `38f151638b7b`  |
| 2218   | No file              | `38f151638b7b`  |
| 2215   | No file              | `38f151638b7b`  |
| 2207   | No file              | `38f151638b7b`  |
| 2203   | No file              | `38f151638b7b`  |
| 2196   | No file              | `38f151638b7b`  |
| 2192   | No file              | `38f151638b7b`  |
| 2189   | No file              | `38f151638b7b`  |
| 2183   | No file              | `38f151638b7b`  |
| 2179   | No file              | `38f151638b7b`  |
| 2171   | No file              | `38f151638b7b`  |
| 2163   | No file              | `38f151638b7b`  |
| 2156   | No file              | `38f151638b7b`  |
| 2151   | No file              | `38f151638b7b`  |
| 2147   | No file              | `38f151638b7b`  |
| 2142   | No file              | `38f151638b7b`  |
| 2138   | No file              | `38f151638b7b`  |
| 2134   | No file              | `38f151638b7b`  |
| 2130   | No file              | `38f151638b7b`  |
| 2122   | No file              | `38f151638b7b`  |
| 2107   | No file              | `38f151638b7b`  |
| 2098   | No file              | `38f151638b7b`  |
| 2089   | No file              | `38f151638b7b`  |
| 2081   | No file              | `38f151638b7b`  |
| 2073   | No file              | `38f151638b7b`  |
| 2067   | No file              | `38f151638b7b`  |
| 2063   | No file              | `38f151638b7b`  |
| 2059   | No file              | `38f151638b7b`  |
| 2052   | No file              | `38f151638b7b`  |
| 2044   | No file              | `38f151638b7b`  |
| 2039   | No file              | `38f151638b7b`  |
| 2032   | No file              | `38f151638b7b`  |
| 2025   | No file              | `38f151638b7b`  |
| 2011   | No file              | `38f151638b7b`  |
| 2005   | No file              | `38f151638b7b`  |
| 2000   | No file              | `38f151638b7b`  |
| 1996   | No file              | `38f151638b7b`  |
| 1991   | No file              | `38f151638b7b`  |
| 1985   | No file              | `38f151638b7b`  |
| 1980   | No file              | `38f151638b7b`  |
| 1969   | No file              | `38f151638b7b`  |
| 1964   | No file              | `38f151638b7b`  |
| 1958   | No file              | `38f151638b7b`  |
| 1950   | No file              | `38f151638b7b`  |
| 1945   | No file              | `38f151638b7b`  |
| 1937   | No file              | `38f151638b7b`  |
| 1933   | No file              | `38f151638b7b`  |
| 1927   | No file              | `38f151638b7b`  |
| 1921   | No file              | `38f151638b7b`  |
| 1914   | No file              | `38f151638b7b`  |
| 1908   | No file              | `38f151638b7b`  |
| 1897   | No file              | `38f151638b7b`  |
| 1892   | No file              | `38f151638b7b`  |
| 1886   | No file              | `38f151638b7b`  |
| 1881   | No file              | `38f151638b7b`  |
| 1871   | No file              | `38f151638b7b`  |
| 1866   | No file              | `38f151638b7b`  |
| 1862   | No file              | `38f151638b7b`  |
| 1854   | No file              | `38f151638b7b`  |
| 1846   | No file              | `38f151638b7b`  |
| 1838   | No file              | `38f151638b7b`  |
| 1832   | No file              | `38f151638b7b`  |
| 1826   | No file              | `38f151638b7b`  |
| 1822   | No file              | `38f151638b7b`  |
| 1818   | No file              | `38f151638b7b`  |
| 1804   | No file              | `38f151638b7b`  |
| 1794   | No file              | `38f151638b7b`  |
| 1790   | No file              | `38f151638b7b`  |
| 1784   | No file              | `38f151638b7b`  |
| 1774   | No file              | `38f151638b7b`  |
| 1771   | No file              | `38f151638b7b`  |
| 1762   | No file              | `38f151638b7b`  |
| 1759   | No file              | `38f151638b7b`  |
| 1754   | No file              | `38f151638b7b`  |
| 1749   | No file              | `38f151638b7b`  |
| 1743   | No file              | `38f151638b7b`  |
| 1737   | No file              | `38f151638b7b`  |
| 1731   | No file              | `38f151638b7b`  |
| 1725   | No file              | `38f151638b7b`  |
| 1717   | No file              | `38f151638b7b`  |
| 1710   | No file              | `38f151638b7b`  |
| 1704   | No file              | `38f151638b7b`  |
| 1698   | No file              | `38f151638b7b`  |
| 1690   | No file              | `38f151638b7b`  |
| 1685   | No file              | `38f151638b7b`  |
| 1680   | No file              | `38f151638b7b`  |
| 1674   | No file              | `38f151638b7b`  |
| 1668   | No file              | `38f151638b7b`  |
| 1659   | No file              | `38f151638b7b`  |
| 1649   | No file              | `38f151638b7b`  |
| 1642   | No file              | `38f151638b7b`  |
| 1636   | No file              | `38f151638b7b`  |
| 1628   | No file              | `38f151638b7b`  |
| 1622   | No file              | `38f151638b7b`  |
| 1614   | No file              | `38f151638b7b`  |
| 1608   | No file              | `38f151638b7b`  |
| 1602   | No file              | `38f151638b7b`  |
| 1598   | No file              | `38f151638b7b`  |
| 1594   | No file              | `38f151638b7b`  |
| 1590   | No file              | `38f151638b7b`  |
| 1587   | No file              | `38f151638b7b`  |
| 1584   | No file              | `38f151638b7b`  |
| 1579   | No file              | `38f151638b7b`  |
| 1572   | No file              | `38f151638b7b`  |
| 1565   | No file              | `38f151638b7b`  |
| 1559   | No file              | `38f151638b7b`  |
| 1554   | No file              | `38f151638b7b`  |
| 1547   | No file              | `38f151638b7b`  |
| 1537   | No file              | `38f151638b7b`  |
| 1529   | No file              | `38f151638b7b`  |
| 1524   | No file              | `38f151638b7b`  |
| 1519   | No file              | `38f151638b7b`  |
| 1509   | No file              | `38f151638b7b`  |
| 1506   | No file              | `38f151638b7b`  |
| 1504   | No file              | `38f151638b7b`  |
| 1500   | No file              | `38f151638b7b`  |
| 1493   | No file              | `38f151638b7b`  |
| 1489   | No file              | `38f151638b7b`  |
| 1485   | No file              | `38f151638b7b`  |
| 1481   | No file              | `38f151638b7b`  |
| 1474   | No file              | `38f151638b7b`  |
| 1466   | No file              | `38f151638b7b`  |
| 1462   | No file              | `38f151638b7b`  |
| 1459   | No file              | `38f151638b7b`  |
| 1453   | No file              | `38f151638b7b`  |
| 1450   | No file              | `38f151638b7b`  |
| 1445   | No file              | `38f151638b7b`  |
| 1439   | No file              | `38f151638b7b`  |
| 1433   | No file              | `38f151638b7b`  |
| 1430   | No file              | `38f151638b7b`  |
| 1426   | No file              | `38f151638b7b`  |
| 1421   | No file              | `38f151638b7b`  |
| 1417   | No file              | `38f151638b7b`  |
| 1416   | No file              | `38f151638b7b`  |
| 1409   | No file              | `38f151638b7b`  |
| 1405   | No file              | `38f151638b7b`  |
| 1401   | No file              | `38f151638b7b`  |
| 1396   | No file              | `38f151638b7b`  |
| 1391   | No file              | `38f151638b7b`  |
| 1390   | No file              | `38f151638b7b`  |
| 1386   | No file              | `38f151638b7b`  |
| 1381   | No file              | `38f151638b7b`  |
| 1379   | No file              | `38f151638b7b`  |
| 1372   | No file              | `38f151638b7b`  |
| 1366   | No file              | `38f151638b7b`  |
| 1364   | No file              | `38f151638b7b`  |
| 1363   | No file              | `38f151638b7b`  |
| 1360   | No file              | `38f151638b7b`  |
| 1358   | No file              | `38f151638b7b`  |
| 1355   | No file              | `38f151638b7b`  |
| 1351   | No file              | `38f151638b7b`  |
| 1348   | No file              | `38f151638b7b`  |
| 1346   | No file              | `38f151638b7b`  |
| 1341   | No file              | `38f151638b7b`  |
| 1340   | No file              | `38f151638b7b`  |
| 1338   | No file              | `38f151638b7b`  |
| 1335   | No file              | `38f151638b7b`  |
| 1333   | No file              | `38f151638b7b`  |
| 1329   | No file              | `38f151638b7b`  |
| 1327   | No file              | `38f151638b7b`  |
| 1324   | No file              | `38f151638b7b`  |
| 1321   | No file              | `38f151638b7b`  |
| 1319   | No file              | `38f151638b7b`  |
| 1318   | No file              | `38f151638b7b`  |
| 1316   | No file              | `38f151638b7b`  |
| 1313   | No file              | `38f151638b7b`  |
| 1311   | No file              | `38f151638b7b`  |
| 1309   | No file              | `38f151638b7b`  |
| 1304   | No file              | `38f151638b7b`  |
| 1292   | No file              | `38f151638b7b`  |
| 1286   | No file              | `38f151638b7b`  |
| 1280   | No file              | `38f151638b7b`  |
| 1276   | No file              | `38f151638b7b`  |
| 1267   | No file              | `38f151638b7b`  |
| 1261   | No file              | `38f151638b7b`  |
| 1256   | No file              | `38f151638b7b`  |
| 1250   | No file              | `38f151638b7b`  |
| 1246   | No file              | `38f151638b7b`  |
| 1239   | No file              | `38f151638b7b`  |
| 1230   | No file              | `38f151638b7b`  |
| 1226   | No file              | `38f151638b7b`  |
| 1220   | No file              | `38f151638b7b`  |
| 1217   | No file              | `38f151638b7b`  |
| 1211   | No file              | `38f151638b7b`  |
| 1210   | No file              | `38f151638b7b`  |
| 1208   | No file              | `38f151638b7b`  |
| 1203   | No file              | `38f151638b7b`  |
| 1197   | No file              | `38f151638b7b`  |
| 1194   | No file              | `38f151638b7b`  |
| 1192   | No file              | `38f151638b7b`  |
| 1187   | No file              | `38f151638b7b`  |
| 1183   | No file              | `38f151638b7b`  |
| 1177   | No file              | `38f151638b7b`  |
| 1173   | No file              | `38f151638b7b`  |
| 1167   | No file              | `38f151638b7b`  |
| 1164   | No file              | `38f151638b7b`  |
| 1156   | No file              | `38f151638b7b`  |
| 1149   | No file              | `38f151638b7b`  |
| 1144   | No file              | `38f151638b7b`  |
| 1137   | No file              | `38f151638b7b`  |
| 1132   | No file              | `38f151638b7b`  |
| 1127   | No file              | `38f151638b7b`  |
| 1122   | No file              | `38f151638b7b`  |
| 1118   | No file              | `38f151638b7b`  |
| 1114   | No file              | `38f151638b7b`  |
| 1109   | No file              | `38f151638b7b`  |
| 1102   | No file              | `38f151638b7b`  |
| 1096   | No file              | `38f151638b7b`  |
| 1088   | No file              | `38f151638b7b`  |
| 1081   | No file              | `38f151638b7b`  |
| 1076   | No file              | `38f151638b7b`  |
| 1069   | No file              | `38f151638b7b`  |
| 1064   | No file              | `38f151638b7b`  |
| 1058   | No file              | `38f151638b7b`  |
| 1051   | No file              | `38f151638b7b`  |
| 1044   | No file              | `38f151638b7b`  |
| 1036   | No file              | `38f151638b7b`  |
| 1026   | No file              | `38f151638b7b`  |
| 1016   | No file              | `38f151638b7b`  |
| 1009   | No file              | `38f151638b7b`  |
| 1005   | No file              | `38f151638b7b`  |
| 1000   | No file              | `38f151638b7b`  |
| 998    | No file              | `38f151638b7b`  |
| 990    | No file              | `38f151638b7b`  |
| 979    | No file              | `38f151638b7b`  |
| 972    | No file              | `38f151638b7b`  |
| 963    | No file              | `38f151638b7b`  |
| 955    | No file              | `38f151638b7b`  |
| 946    | No file              | `38f151638b7b`  |
| 938    | No file              | `38f151638b7b`  |
| 927    | No file              | `38f151638b7b`  |
| 911    | No file              | `38f151638b7b`  |
| 904    | No file              | `38f151638b7b`  |
| 899    | No file              | `38f151638b7b`  |
| 894    | No file              | `38f151638b7b`  |
| 885    | No file              | `38f151638b7b`  |
| 879    | No file              | `38f151638b7b`  |
| 872    | No file              | `38f151638b7b`  |
| 864    | No file              | `38f151638b7b`  |
| 855    | No file              | `38f151638b7b`  |
| 853    | No file              | `38f151638b7b`  |
| 845    | No file              | `38f151638b7b`  |
| 837    | No file              | `38f151638b7b`  |
| 829    | No file              | `38f151638b7b`  |
| 822    | No file              | `38f151638b7b`  |
| 814    | No file              | `38f151638b7b`  |
| 805    | No file              | `38f151638b7b`  |
| 794    | No file              | `38f151638b7b`  |
| 787    | No file              | `38f151638b7b`  |
| 780    | No file              | `38f151638b7b`  |
| 771    | No file              | `38f151638b7b`  |
| 760    | No file              | `38f151638b7b`  |
| 748    | No file              | `38f151638b7b`  |
| 741    | No file              | `38f151638b7b`  |
| 736    | No file              | `38f151638b7b`  |
| 731    | No file              | `38f151638b7b`  |
| 723    | No file              | `38f151638b7b`  |
| 711    | No file              | `38f151638b7b`  |
| 707    | No file              | `38f151638b7b`  |
| 697    | No file              | `38f151638b7b`  |
| 689    | No file              | `38f151638b7b`  |
| 683    | No file              | `38f151638b7b`  |
| 678    | No file              | `38f151638b7b`  |
| 670    | No file              | `38f151638b7b`  |
| 661    | No file              | `38f151638b7b`  |
| 656    | No file              | `38f151638b7b`  |
| 652    | No file              | `38f151638b7b`  |
| 643    | No file              | `38f151638b7b`  |
| 637    | No file              | `38f151638b7b`  |
| 630    | No file              | `38f151638b7b`  |
| 627    | No file              | `38f151638b7b`  |
| 621    | No file              | `38f151638b7b`  |
| 617    | No file              | `38f151638b7b`  |
| 615    | No file              | `38f151638b7b`  |
| 606    | No file              | `38f151638b7b`  |
| 599    | No file              | `38f151638b7b`  |
| 592    | No file              | `38f151638b7b`  |
| 586    | No file              | `38f151638b7b`  |
| 577    | No file              | `38f151638b7b`  |
| 569    | No file              | `38f151638b7b`  |
| 561    | No file              | `38f151638b7b`  |
| 554    | No file              | `38f151638b7b`  |
| 542    | No file              | `38f151638b7b`  |
| 532    | No file              | `38f151638b7b`  |
| 531    | No file              | `38f151638b7b`  |
| 526    | No file              | `38f151638b7b`  |
| 521    | No file              | `38f151638b7b`  |
| 517    | No file              | `38f151638b7b`  |
| 510    | No file              | `38f151638b7b`  |
| 508    | No file              | `38f151638b7b`  |
| 504    | No file              | `38f151638b7b`  |
| 497    | No file              | `38f151638b7b`  |
| 491    | No file              | `38f151638b7b`  |
| 485    | No file              | `38f151638b7b`  |
| 478    | No file              | `38f151638b7b`  |
| 472    | No file              | `38f151638b7b`  |
| 466    | No file              | `38f151638b7b`  |
| 457    | No file              | `38f151638b7b`  |
| 452    | No file              | `38f151638b7b`  |
| 449    | No file              | `38f151638b7b`  |
| 435    | No file              | `38f151638b7b`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                    |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Character names (LOC type 6); notice text, LOC type 37 under the RESOURCE sheet key hash |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                   | Type                          | Field                 | Notes                                                                |
| ------------------------ | ----------------------------- | --------------------- | -------------------------------------------------------------------- |
| `+0x00`                  | char[4]                       | magic                 | ASCII `PABR`                                                         |
| `+0x04`                  | u32                           | row_count             | Number of rows                                                       |
| `+0x08`                  | Row[row_count]                | rows                  | See Row; byte-packed                                                 |
| `rows+0x00`              | u32                           | boss_count            | Number of `boss_keys`                                                |
| `rows+0x04`              | u16[boss_count]               | boss_keys             | `random_spawn_key` of each boss row; `ToClient_getHardCoreBossKeyByIndex` |
| `boss_keys+0x00`         | u32                           | npc_count             | Number of `npc_keys`                                                 |
| `boss_keys+0x04`         | u16[npc_count]                | npc_keys              | `random_spawn_key` of each NPC row                                   |
| `npc_keys+0x00`          | u32                           | unknown_str_ref_count | Number of `unknown_str_refs`; equals `string_count` on client 3474   |
| `npc_keys+0x04`          | u32[unknown_str_ref_count]    | unknown_str_refs      | String-table indexes `0` to `15` in order on client 3474             |
| `unknown_str_refs+0x00`  | String Table                  | string_table          | See String Table                                                     |
| `string_table+0x00`      | u32                           | table_start           | Offset of the string table, where `unknown_str_refs` ends            |
| `string_table+0x04`      | u32                           | zero                  | Always `0`                                                           |

### Row (19 bytes)

| Offset  | Type | Field                 | Notes                                                                                                    |
| ------- | ---- | --------------------- | -------------------------------------------------------------------------------------------------------- |
| `+0x00` | u16  | character_key         | [`characterstatic.dbss`](characterstatic_dbss.md) key; `ToClient_getHardCoreCharaterKeyByRandomSpawnCharaterKey` |
| `+0x02` | i16  | world_map_icon_ref    | String-table index of the world map icon texture (`Combine_WorldMap_HardcoreServer_*`)                   |
| `+0x04` | i16  | boss_icon_ref         | String-table index of the boss info icon texture, `-1` on the NPC rows; `ToClient_getHardCoreBossUIIconTextureID` |
| `+0x06` | i16  | notice_background_ref | String-table index of the notice background texture (`Combine_Etc_HardcoreServer_*_NakBG`)                |
| `+0x08` | i16  | notice_ref            | String-table index of the RESOURCE sheet key of the spawn notice (`PANEL_BIGNAK_HARDCOREMESSAGE_<n>`)     |
| `+0x0A` | i16  | reveal_notice_ref     | String-table index of the RESOURCE sheet key of the "World Map location revealed" notice, `-1` on the NPC rows |
| `+0x0C` | u8   | unknown_0c            | `1` on the NPC rows, `0` on the boss rows                                                                |
| `+0x0D` | u32  | random_spawn_key      | Random spawn key, unique; the key the two lists hold                                                     |
| `+0x11` | u16  | unknown_11            | Always `0`                                                                                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                  |
| ------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `16` on client 3474                 |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE texture IDs and RESOURCE sheet keys            |

## Random Spawns

Client 3474, with the notice text of LOC type 37:

| `random_spawn_key` | Character (key)            | List | Spawn notice                              | Reveal notice                 |
| ------------------ | -------------------------- | ---- | ----------------------------------------- | ----------------------------- |
| `1` to `4`         | Wandering Merchant (62223 to 62226) | NPC  | The Wandering Merchant Visits     |                               |
| `11` to `16`       | Light of Offering (62200)  | NPC  | Light of Offering                         |                               |
| `21`               | Laytenn (29496)            | Boss | Laytenn, the Ancient Destroyer (World Map reveal in 5 min.) | World Map location revealed |
| `22`               | Ancient Puturum (29497)    | Boss | Frenzied Ancient Puturum (World Map reveal in 5 min.) | World Map location revealed |

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. The world map of client 3474
(`grand_worldmap_mainpanel.luac`, `PaGlobalFunc_UpdateHardCoreBossListUI`)
walks the bosses with `ToClient_getHardCoreBossKeyByIndex(index)`, turns
each random spawn key into a character with
`ToClient_getHardCoreCharaterKeyByRandomSpawnCharaterKey(key)` and that
character's `getName()`, and sets the boss image with
`ToClient_getHardCoreBossUIIconTextureID(key)`. The boss list holds the
`random_spawn_key` of the two boss rows, and those rows' `boss_icon_ref`
strings are the `..._Map_BossInfoIcon_Raiten` and `..._Puturum` textures.
The other refs are named by their strings: a world map icon, a notice
background (`NakBG`, "big nak" being the client's name for its large
centre-screen notice) and two `PANEL_BIGNAK_HARDCOREMESSAGE_<n>` keys,
whose LOC text announces the spawn and, for a boss, the reveal on the world
map.

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- The row refs index the string table directly, and `unknown_str_refs` maps
  every index to itself, so both readings give the same string on client
  3474.
- The compass widget (`panel_widget_compass_hardcore_1.luac`) builds one
  icon per `ToClient_getHardCoreMaxRandomNpcCount()` and per
  `ToClient_getHardCoreMaxBossCount()`; the NPC and boss lists hold 10 and
  2 keys on client 3474.
- The parser is `_bss/hardcorerandomspawncharacterstaticstatusmanager/parser.py`.
  The preview shows each row with its character name, its list, the four
  texture and key strings and the LOC text of both notices.

## Open Questions

### Row Flag and String Index List

What `unknown_0c` and `unknown_str_refs` are. `unknown_0c` is `1` exactly
on the rows of the NPC list, so it may be the list a row goes on, which the
two lists also give. `unknown_str_refs` lists each string once in table
order; whether the row refs go through it or straight to the table cannot
be told while it maps every index to itself.
