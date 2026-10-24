# `cutscenecharacterdata.bss` Format

## Purpose

The character keys set aside as cutscene actors: the player stand-ins
(`401` PC, `410` Player), the tutorial actors `411` to `430`, the
`Sequence_NPC_*` library from `62001` up, and story characters added later
(`29472` Kalqueesh, `25696` Bari). Each entry is one u16 key of
[`characterstatic.dbss`](characterstatic_dbss.md). The file holds the
`Index` column of the `Character_Table_CutScene` sheet, packed as a PABR
list with an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | -------------- | --------- |
| 1      | 1704 and later | 3483    | `cutscenecharacterdata.bss` | 264   | 1 String Table | 4         |

| Layout | File                        | Known          | Unknown    |
| ------ | --------------------------- | -------------- | ---------- |
| 1      | `cutscenecharacterdata.bss` | 264 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `b0f55ec4235a`  |
| 3482   | Layout 1 | `b0f55ec4235a`  |
| 3474   | Layout 1 | `b0f55ec4235a`  |
| 3473   | Layout 1 | `b0f55ec4235a`  |
| 3464   | Layout 1 | `b0f55ec4235a`  |
| 3458   | Layout 1 | `b0f55ec4235a`  |
| 3454   | Layout 1 | `b0f55ec4235a`  |
| 3444   | Layout 1 | `b0f55ec4235a`  |
| 3435   | Layout 1 | `b0f55ec4235a`  |
| 3426   | Layout 1 | `b0f55ec4235a`  |
| 3418   | Layout 1 | `b0f55ec4235a`  |
| 3412   | Layout 1 | `b0f55ec4235a`  |
| 3402   | Layout 1 | `b0f55ec4235a`  |
| 3396   | Layout 1 | `b0f55ec4235a`  |
| 3387   | Layout 1 | `b0f55ec4235a`  |
| 3381   | Layout 1 | `b0f55ec4235a`  |
| 3373   | Layout 1 | `b0f55ec4235a`  |
| 3364   | Layout 1 | `b0f55ec4235a`  |
| 3356   | Layout 1 | `b0f55ec4235a`  |
| 3349   | Layout 1 | `b0f55ec4235a`  |
| 3342   | Layout 1 | `b0f55ec4235a`  |
| 3335   | Layout 1 | `b0f55ec4235a`  |
| 3326   | Layout 1 | `b0f55ec4235a`  |
| 3321   | Layout 1 | `b0f55ec4235a`  |
| 3314   | Layout 1 | `b0f55ec4235a`  |
| 3303   | Layout 1 | `b0f55ec4235a`  |
| 3302   | Layout 1 | `b0f55ec4235a`  |
| 3293   | Layout 1 | `b0f55ec4235a`  |
| 3283   | Layout 1 | `b0f55ec4235a`  |
| 3275   | Layout 1 | `b0f55ec4235a`  |
| 3267   | Layout 1 | `b0f55ec4235a`  |
| 3258   | Layout 1 | `b0f55ec4235a`  |
| 3251   | Layout 1 | `b0f55ec4235a`  |
| 3242   | Layout 1 | `b0f55ec4235a`  |
| 3235   | Layout 1 | `b0f55ec4235a`  |
| 3229   | Layout 1 | `b0f55ec4235a`  |
| 3212   | Layout 1 | `b0f55ec4235a`  |
| 3203   | Layout 1 | `b0f55ec4235a`  |
| 3193   | Layout 1 | `b0f55ec4235a`  |
| 3186   | Layout 1 | `b0f55ec4235a`  |
| 3177   | Layout 1 | `b0f55ec4235a`  |
| 3169   | Layout 1 | `b0f55ec4235a`  |
| 3158   | Layout 1 | `b0f55ec4235a`  |
| 3151   | Layout 1 | `b0f55ec4235a`  |
| 3144   | Layout 1 | `b0f55ec4235a`  |
| 3133   | Layout 1 | `b0f55ec4235a`  |
| 3125   | Layout 1 | `b0f55ec4235a`  |
| 3118   | Layout 1 | `b0f55ec4235a`  |
| 3111   | Layout 1 | `b0f55ec4235a`  |
| 3103   | Layout 1 | `b0f55ec4235a`  |
| 3095   | Layout 1 | `b0f55ec4235a`  |
| 3086   | Layout 1 | `b0f55ec4235a`  |
| 3072   | Layout 1 | `b0f55ec4235a`  |
| 3062   | Layout 1 | `b0f55ec4235a`  |
| 3052   | Layout 1 | `b0f55ec4235a`  |
| 3045   | Layout 1 | `b0f55ec4235a`  |
| 3037   | Layout 1 | `b0f55ec4235a`  |
| 3030   | Layout 1 | `b0f55ec4235a`  |
| 3021   | Layout 1 | `b0f55ec4235a`  |
| 3012   | Layout 1 | `b0f55ec4235a`  |
| 3002   | Layout 1 | `b0f55ec4235a`  |
| 2995   | Layout 1 | `b0f55ec4235a`  |
| 2987   | Layout 1 | `b0f55ec4235a`  |
| 2978   | Layout 1 | `b0f55ec4235a`  |
| 2970   | Layout 1 | `b0f55ec4235a`  |
| 2959   | Layout 1 | `b0f55ec4235a`  |
| 2951   | Layout 1 | `b0f55ec4235a`  |
| 2942   | Layout 1 | `b0f55ec4235a`  |
| 2935   | Layout 1 | `b0f55ec4235a`  |
| 2932   | Layout 1 | `b0f55ec4235a`  |
| 2923   | Layout 1 | `b0f55ec4235a`  |
| 2919   | Layout 1 | `b0f55ec4235a`  |
| 2907   | Layout 1 | `b0f55ec4235a`  |
| 2900   | Layout 1 | `b0f55ec4235a`  |
| 2891   | Layout 1 | `b0f55ec4235a`  |
| 2882   | Layout 1 | `b0f55ec4235a`  |
| 2872   | Layout 1 | `b0f55ec4235a`  |
| 2863   | Layout 1 | `b0f55ec4235a`  |
| 2855   | Layout 1 | `b0f55ec4235a`  |
| 2849   | Layout 1 | `b0f55ec4235a`  |
| 2844   | Layout 1 | `b0f55ec4235a`  |
| 2834   | Layout 1 | `b0f55ec4235a`  |
| 2825   | Layout 1 | `b0f55ec4235a`  |
| 2819   | Layout 1 | `b0f55ec4235a`  |
| 2811   | Layout 1 | `b0f55ec4235a`  |
| 2803   | Layout 1 | `b0f55ec4235a`  |
| 2794   | Layout 1 | `b0f55ec4235a`  |
| 2783   | Layout 1 | `b0f55ec4235a`  |
| 2774   | Layout 1 | `b0f55ec4235a`  |
| 2765   | Layout 1 | `b0f55ec4235a`  |
| 2756   | Layout 1 | `b0f55ec4235a`  |
| 2750   | Layout 1 | `b0f55ec4235a`  |
| 2743   | Layout 1 | `b0f55ec4235a`  |
| 2736   | Layout 1 | `b0f55ec4235a`  |
| 2726   | Layout 1 | `b0f55ec4235a`  |
| 2717   | Layout 1 | `b0f55ec4235a`  |
| 2709   | Layout 1 | `b0f55ec4235a`  |
| 2703   | Layout 1 | `b0f55ec4235a`  |
| 2695   | Layout 1 | `b0f55ec4235a`  |
| 2684   | Layout 1 | `b0f55ec4235a`  |
| 2672   | Layout 1 | `b0f55ec4235a`  |
| 2665   | Layout 1 | `b0f55ec4235a`  |
| 2657   | Layout 1 | `b0f55ec4235a`  |
| 2649   | Layout 1 | `b0f55ec4235a`  |
| 2644   | Layout 1 | `b0f55ec4235a`  |
| 2637   | Layout 1 | `b0f55ec4235a`  |
| 2629   | Layout 1 | `b0f55ec4235a`  |
| 2619   | Layout 1 | `b0f55ec4235a`  |
| 2612   | Layout 1 | `b0f55ec4235a`  |
| 2606   | Layout 1 | `b0f55ec4235a`  |
| 2602   | Layout 1 | `b0f55ec4235a`  |
| 2601   | Layout 1 | `b0f55ec4235a`  |
| 2592   | Layout 1 | `b0f55ec4235a`  |
| 2583   | Layout 1 | `b0f55ec4235a`  |
| 2575   | Layout 1 | `b0f55ec4235a`  |
| 2567   | Layout 1 | `b0f55ec4235a`  |
| 2560   | Layout 1 | `b0f55ec4235a`  |
| 2553   | Layout 1 | `b0f55ec4235a`  |
| 2545   | Layout 1 | `b0f55ec4235a`  |
| 2538   | Layout 1 | `b0f55ec4235a`  |
| 2529   | Layout 1 | `b0f55ec4235a`  |
| 2519   | Layout 1 | `b0f55ec4235a`  |
| 2513   | Layout 1 | `b0f55ec4235a`  |
| 2510   | Layout 1 | `b0f55ec4235a`  |
| 2507   | Layout 1 | `b0f55ec4235a`  |
| 2503   | Layout 1 | `b0f55ec4235a`  |
| 2498   | Layout 1 | `b0f55ec4235a`  |
| 2492   | Layout 1 | `b0f55ec4235a`  |
| 2487   | Layout 1 | `b0f55ec4235a`  |
| 2480   | Layout 1 | `b0f55ec4235a`  |
| 2474   | Layout 1 | `b0f55ec4235a`  |
| 2468   | Layout 1 | `b0f55ec4235a`  |
| 2460   | Layout 1 | `b0f55ec4235a`  |
| 2453   | Layout 1 | `b0f55ec4235a`  |
| 2444   | Layout 1 | `b0f55ec4235a`  |
| 2438   | Layout 1 | `b0f55ec4235a`  |
| 2434   | Layout 1 | `b0f55ec4235a`  |
| 2429   | Layout 1 | `b0f55ec4235a`  |
| 2421   | Layout 1 | `b0f55ec4235a`  |
| 2414   | Layout 1 | `b0f55ec4235a`  |
| 2407   | Layout 1 | `b0f55ec4235a`  |
| 2401   | Layout 1 | `b0f55ec4235a`  |
| 2397   | Layout 1 | `b0f55ec4235a`  |
| 2393   | Layout 1 | `b0f55ec4235a`  |
| 2384   | Layout 1 | `b0f55ec4235a`  |
| 2378   | Layout 1 | `b0f55ec4235a`  |
| 2372   | Layout 1 | `b0f55ec4235a`  |
| 2358   | Layout 1 | `b0f55ec4235a`  |
| 2352   | Layout 1 | `b0f55ec4235a`  |
| 2347   | Layout 1 | `b0f55ec4235a`  |
| 2343   | Layout 1 | `b0f55ec4235a`  |
| 2335   | Layout 1 | `b0f55ec4235a`  |
| 2327   | Layout 1 | `b0f55ec4235a`  |
| 2324   | Layout 1 | `b0f55ec4235a`  |
| 2319   | Layout 1 | `b0f55ec4235a`  |
| 2313   | Layout 1 | `b0f55ec4235a`  |
| 2308   | Layout 1 | `b0f55ec4235a`  |
| 2302   | Layout 1 | `b0f55ec4235a`  |
| 2295   | Layout 1 | `b0f55ec4235a`  |
| 2290   | Layout 1 | `b0f55ec4235a`  |
| 2284   | Layout 1 | `b0f55ec4235a`  |
| 2276   | Layout 1 | `b0f55ec4235a`  |
| 2269   | Layout 1 | `b0f55ec4235a`  |
| 2259   | Layout 1 | `b0f55ec4235a`  |
| 2250   | Layout 1 | `b0f55ec4235a`  |
| 2243   | Layout 1 | `b0f55ec4235a`  |
| 2235   | Layout 1 | `b0f55ec4235a`  |
| 2229   | Layout 1 | `b0f55ec4235a`  |
| 2224   | Layout 1 | `b0f55ec4235a`  |
| 2218   | Layout 1 | `b0f55ec4235a`  |
| 2215   | Layout 1 | `b0f55ec4235a`  |
| 2207   | Layout 1 | `b0f55ec4235a`  |
| 2203   | Layout 1 | `b0f55ec4235a`  |
| 2196   | Layout 1 | `b0f55ec4235a`  |
| 2192   | Layout 1 | `b0f55ec4235a`  |
| 2189   | Layout 1 | `b0f55ec4235a`  |
| 2183   | Layout 1 | `b0f55ec4235a`  |
| 2179   | Layout 1 | `b0f55ec4235a`  |
| 2171   | Layout 1 | `b0f55ec4235a`  |
| 2163   | Layout 1 | `b0f55ec4235a`  |
| 2156   | Layout 1 | `b0f55ec4235a`  |
| 2151   | Layout 1 | `b0f55ec4235a`  |
| 2147   | Layout 1 | `b0f55ec4235a`  |
| 2142   | Layout 1 | `b0f55ec4235a`  |
| 2138   | Layout 1 | `b0f55ec4235a`  |
| 2134   | Layout 1 | `b0f55ec4235a`  |
| 2130   | Layout 1 | `b0f55ec4235a`  |
| 2122   | Layout 1 | `b0f55ec4235a`  |
| 2107   | Layout 1 | `b0f55ec4235a`  |
| 2098   | Layout 1 | `b0f55ec4235a`  |
| 2089   | Layout 1 | `b0f55ec4235a`  |
| 2081   | Layout 1 | `b0f55ec4235a`  |
| 2073   | Layout 1 | `b0f55ec4235a`  |
| 2067   | Layout 1 | `b0f55ec4235a`  |
| 2063   | Layout 1 | `b0f55ec4235a`  |
| 2059   | Layout 1 | `b0f55ec4235a`  |
| 2052   | Layout 1 | `b0f55ec4235a`  |
| 2044   | Layout 1 | `b0f55ec4235a`  |
| 2039   | Layout 1 | `b0f55ec4235a`  |
| 2032   | Layout 1 | `b0f55ec4235a`  |
| 2025   | Layout 1 | `b0f55ec4235a`  |
| 2011   | Layout 1 | `b0f55ec4235a`  |
| 2005   | Layout 1 | `b0f55ec4235a`  |
| 2000   | Layout 1 | `b0f55ec4235a`  |
| 1996   | Layout 1 | `b0f55ec4235a`  |
| 1991   | Layout 1 | `b0f55ec4235a`  |
| 1985   | Layout 1 | `b0f55ec4235a`  |
| 1980   | Layout 1 | `b0f55ec4235a`  |
| 1969   | Layout 1 | `b0f55ec4235a`  |
| 1964   | Layout 1 | `b0f55ec4235a`  |
| 1958   | Layout 1 | `b0f55ec4235a`  |
| 1950   | Layout 1 | `b0f55ec4235a`  |
| 1945   | Layout 1 | `b0f55ec4235a`  |
| 1937   | Layout 1 | `b0f55ec4235a`  |
| 1933   | Layout 1 | `b0f55ec4235a`  |
| 1927   | Layout 1 | `b0f55ec4235a`  |
| 1921   | Layout 1 | `b0f55ec4235a`  |
| 1914   | Layout 1 | `b0f55ec4235a`  |
| 1908   | Layout 1 | `b0f55ec4235a`  |
| 1897   | Layout 1 | `b0f55ec4235a`  |
| 1892   | Layout 1 | `b0f55ec4235a`  |
| 1886   | Layout 1 | `b0f55ec4235a`  |
| 1881   | Layout 1 | `b0f55ec4235a`  |
| 1871   | Layout 1 | `b0f55ec4235a`  |
| 1866   | Layout 1 | `b0f55ec4235a`  |
| 1862   | Layout 1 | `b0f55ec4235a`  |
| 1854   | Layout 1 | `b0f55ec4235a`  |
| 1846   | Layout 1 | `b0f55ec4235a`  |
| 1838   | Layout 1 | `b0f55ec4235a`  |
| 1832   | Layout 1 | `b0f55ec4235a`  |
| 1826   | Layout 1 | `b0f55ec4235a`  |
| 1822   | Layout 1 | `b0f55ec4235a`  |
| 1818   | Layout 1 | `b0f55ec4235a`  |
| 1804   | Layout 1 | `b0f55ec4235a`  |
| 1794   | Layout 1 | `b0f55ec4235a`  |
| 1790   | Layout 1 | `b0f55ec4235a`  |
| 1784   | Layout 1 | `b0f55ec4235a`  |
| 1774   | Layout 1 | `b0f55ec4235a`  |
| 1771   | Layout 1 | `b0f55ec4235a`  |
| 1762   | Layout 1 | `b0f55ec4235a`  |
| 1759   | Layout 1 | `b0f55ec4235a`  |
| 1754   | Layout 1 | `b0f55ec4235a`  |
| 1749   | Layout 1 | `b0f55ec4235a`  |
| 1743   | Layout 1 | `b0f55ec4235a`  |
| 1737   | Layout 1 | `b0f55ec4235a`  |
| 1731   | Layout 1 | `b0f55ec4235a`  |
| 1725   | Layout 1 | `b0f55ec4235a`  |
| 1717   | Layout 1 | `b0f55ec4235a`  |
| 1710   | Layout 1 | `b0f55ec4235a`  |
| 1704   | Layout 1 | `b0f55ec4235a`  |
| 1698   | No file  | `b0f55ec4235a`  |
| 1690   | No file  | `b0f55ec4235a`  |
| 1685   | No file  | `b0f55ec4235a`  |
| 1680   | No file  | `b0f55ec4235a`  |
| 1674   | No file  | `b0f55ec4235a`  |
| 1668   | No file  | `b0f55ec4235a`  |
| 1659   | No file  | `b0f55ec4235a`  |
| 1649   | No file  | `b0f55ec4235a`  |
| 1642   | No file  | `b0f55ec4235a`  |
| 1636   | No file  | `b0f55ec4235a`  |
| 1628   | No file  | `b0f55ec4235a`  |
| 1622   | No file  | `b0f55ec4235a`  |
| 1614   | No file  | `b0f55ec4235a`  |
| 1608   | No file  | `b0f55ec4235a`  |
| 1602   | No file  | `b0f55ec4235a`  |
| 1598   | No file  | `b0f55ec4235a`  |
| 1594   | No file  | `b0f55ec4235a`  |
| 1590   | No file  | `b0f55ec4235a`  |
| 1587   | No file  | `b0f55ec4235a`  |
| 1584   | No file  | `b0f55ec4235a`  |
| 1579   | No file  | `b0f55ec4235a`  |
| 1572   | No file  | `b0f55ec4235a`  |
| 1565   | No file  | `b0f55ec4235a`  |
| 1559   | No file  | `b0f55ec4235a`  |
| 1554   | No file  | `b0f55ec4235a`  |
| 1547   | No file  | `b0f55ec4235a`  |
| 1537   | No file  | `b0f55ec4235a`  |
| 1529   | No file  | `b0f55ec4235a`  |
| 1524   | No file  | `b0f55ec4235a`  |
| 1519   | No file  | `b0f55ec4235a`  |
| 1509   | No file  | `b0f55ec4235a`  |
| 1506   | No file  | `b0f55ec4235a`  |
| 1504   | No file  | `b0f55ec4235a`  |
| 1500   | No file  | `b0f55ec4235a`  |
| 1493   | No file  | `b0f55ec4235a`  |
| 1489   | No file  | `b0f55ec4235a`  |
| 1485   | No file  | `b0f55ec4235a`  |
| 1481   | No file  | `b0f55ec4235a`  |
| 1474   | No file  | `b0f55ec4235a`  |
| 1466   | No file  | `b0f55ec4235a`  |
| 1462   | No file  | `b0f55ec4235a`  |
| 1459   | No file  | `b0f55ec4235a`  |
| 1453   | No file  | `b0f55ec4235a`  |
| 1450   | No file  | `b0f55ec4235a`  |
| 1445   | No file  | `b0f55ec4235a`  |
| 1439   | No file  | `b0f55ec4235a`  |
| 1433   | No file  | `b0f55ec4235a`  |
| 1430   | No file  | `b0f55ec4235a`  |
| 1426   | No file  | `b0f55ec4235a`  |
| 1421   | No file  | `b0f55ec4235a`  |
| 1417   | No file  | `b0f55ec4235a`  |
| 1416   | No file  | `b0f55ec4235a`  |
| 1409   | No file  | `b0f55ec4235a`  |
| 1405   | No file  | `b0f55ec4235a`  |
| 1401   | No file  | `b0f55ec4235a`  |
| 1396   | No file  | `b0f55ec4235a`  |
| 1391   | No file  | `b0f55ec4235a`  |
| 1390   | No file  | `b0f55ec4235a`  |
| 1386   | No file  | `b0f55ec4235a`  |
| 1381   | No file  | `b0f55ec4235a`  |
| 1379   | No file  | `b0f55ec4235a`  |
| 1372   | No file  | `b0f55ec4235a`  |
| 1366   | No file  | `b0f55ec4235a`  |
| 1364   | No file  | `b0f55ec4235a`  |
| 1363   | No file  | `b0f55ec4235a`  |
| 1360   | No file  | `b0f55ec4235a`  |
| 1358   | No file  | `b0f55ec4235a`  |
| 1355   | No file  | `b0f55ec4235a`  |
| 1351   | No file  | `b0f55ec4235a`  |
| 1348   | No file  | `b0f55ec4235a`  |
| 1346   | No file  | `b0f55ec4235a`  |
| 1341   | No file  | `b0f55ec4235a`  |
| 1340   | No file  | `b0f55ec4235a`  |
| 1338   | No file  | `b0f55ec4235a`  |
| 1335   | No file  | `b0f55ec4235a`  |
| 1333   | No file  | `b0f55ec4235a`  |
| 1329   | No file  | `b0f55ec4235a`  |
| 1327   | No file  | `b0f55ec4235a`  |
| 1324   | No file  | `b0f55ec4235a`  |
| 1321   | No file  | `b0f55ec4235a`  |
| 1319   | No file  | `b0f55ec4235a`  |
| 1318   | No file  | `b0f55ec4235a`  |
| 1316   | No file  | `b0f55ec4235a`  |
| 1313   | No file  | `b0f55ec4235a`  |
| 1311   | No file  | `b0f55ec4235a`  |
| 1309   | No file  | `b0f55ec4235a`  |
| 1304   | No file  | `b0f55ec4235a`  |
| 1292   | No file  | `b0f55ec4235a`  |
| 1286   | No file  | `b0f55ec4235a`  |
| 1280   | No file  | `b0f55ec4235a`  |
| 1276   | No file  | `b0f55ec4235a`  |
| 1267   | No file  | `b0f55ec4235a`  |
| 1261   | No file  | `b0f55ec4235a`  |
| 1256   | No file  | `b0f55ec4235a`  |
| 1250   | No file  | `b0f55ec4235a`  |
| 1246   | No file  | `b0f55ec4235a`  |
| 1239   | No file  | `b0f55ec4235a`  |
| 1230   | No file  | `b0f55ec4235a`  |
| 1226   | No file  | `b0f55ec4235a`  |
| 1220   | No file  | `b0f55ec4235a`  |
| 1217   | No file  | `b0f55ec4235a`  |
| 1211   | No file  | `b0f55ec4235a`  |
| 1210   | No file  | `b0f55ec4235a`  |
| 1208   | No file  | `b0f55ec4235a`  |
| 1203   | No file  | `b0f55ec4235a`  |
| 1197   | No file  | `b0f55ec4235a`  |
| 1194   | No file  | `b0f55ec4235a`  |
| 1192   | No file  | `b0f55ec4235a`  |
| 1187   | No file  | `b0f55ec4235a`  |
| 1183   | No file  | `b0f55ec4235a`  |
| 1177   | No file  | `b0f55ec4235a`  |
| 1173   | No file  | `b0f55ec4235a`  |
| 1167   | No file  | `b0f55ec4235a`  |
| 1164   | No file  | `b0f55ec4235a`  |
| 1156   | No file  | `b0f55ec4235a`  |
| 1149   | No file  | `b0f55ec4235a`  |
| 1144   | No file  | `b0f55ec4235a`  |
| 1137   | No file  | `b0f55ec4235a`  |
| 1132   | No file  | `b0f55ec4235a`  |
| 1127   | No file  | `b0f55ec4235a`  |
| 1122   | No file  | `b0f55ec4235a`  |
| 1118   | No file  | `b0f55ec4235a`  |
| 1114   | No file  | `b0f55ec4235a`  |
| 1109   | No file  | `b0f55ec4235a`  |
| 1102   | No file  | `b0f55ec4235a`  |
| 1096   | No file  | `b0f55ec4235a`  |
| 1088   | No file  | `b0f55ec4235a`  |
| 1081   | No file  | `b0f55ec4235a`  |
| 1076   | No file  | `b0f55ec4235a`  |
| 1069   | No file  | `b0f55ec4235a`  |
| 1064   | No file  | `b0f55ec4235a`  |
| 1058   | No file  | `b0f55ec4235a`  |
| 1051   | No file  | `b0f55ec4235a`  |
| 1044   | No file  | `b0f55ec4235a`  |
| 1036   | No file  | `b0f55ec4235a`  |
| 1026   | No file  | `b0f55ec4235a`  |
| 1016   | No file  | `b0f55ec4235a`  |
| 1009   | No file  | `b0f55ec4235a`  |
| 1005   | No file  | `b0f55ec4235a`  |
| 1000   | No file  | `b0f55ec4235a`  |
| 998    | No file  | `b0f55ec4235a`  |
| 990    | No file  | `b0f55ec4235a`  |
| 979    | No file  | `b0f55ec4235a`  |
| 972    | No file  | `b0f55ec4235a`  |
| 963    | No file  | `b0f55ec4235a`  |
| 955    | No file  | `b0f55ec4235a`  |
| 946    | No file  | `b0f55ec4235a`  |
| 938    | No file  | `b0f55ec4235a`  |
| 927    | No file  | `b0f55ec4235a`  |
| 911    | No file  | `b0f55ec4235a`  |
| 904    | No file  | `b0f55ec4235a`  |
| 899    | No file  | `b0f55ec4235a`  |
| 894    | No file  | `b0f55ec4235a`  |
| 885    | No file  | `b0f55ec4235a`  |
| 879    | No file  | `b0f55ec4235a`  |
| 872    | No file  | `b0f55ec4235a`  |
| 864    | No file  | `b0f55ec4235a`  |
| 855    | No file  | `b0f55ec4235a`  |
| 853    | No file  | `b0f55ec4235a`  |
| 845    | No file  | `b0f55ec4235a`  |
| 837    | No file  | `b0f55ec4235a`  |
| 829    | No file  | `b0f55ec4235a`  |
| 822    | No file  | `b0f55ec4235a`  |
| 814    | No file  | `b0f55ec4235a`  |
| 805    | No file  | `b0f55ec4235a`  |
| 794    | No file  | `b0f55ec4235a`  |
| 787    | No file  | `b0f55ec4235a`  |
| 780    | No file  | `b0f55ec4235a`  |
| 771    | No file  | `b0f55ec4235a`  |
| 760    | No file  | `b0f55ec4235a`  |
| 748    | No file  | `b0f55ec4235a`  |
| 741    | No file  | `b0f55ec4235a`  |
| 736    | No file  | `b0f55ec4235a`  |
| 731    | No file  | `b0f55ec4235a`  |
| 723    | No file  | `b0f55ec4235a`  |
| 711    | No file  | `b0f55ec4235a`  |
| 707    | No file  | `b0f55ec4235a`  |
| 697    | No file  | `b0f55ec4235a`  |
| 689    | No file  | `b0f55ec4235a`  |
| 683    | No file  | `b0f55ec4235a`  |
| 678    | No file  | `b0f55ec4235a`  |
| 670    | No file  | `b0f55ec4235a`  |
| 661    | No file  | `b0f55ec4235a`  |
| 656    | No file  | `b0f55ec4235a`  |
| 652    | No file  | `b0f55ec4235a`  |
| 643    | No file  | `b0f55ec4235a`  |
| 637    | No file  | `b0f55ec4235a`  |
| 630    | No file  | `b0f55ec4235a`  |
| 627    | No file  | `b0f55ec4235a`  |
| 621    | No file  | `b0f55ec4235a`  |
| 617    | No file  | `b0f55ec4235a`  |
| 615    | No file  | `b0f55ec4235a`  |
| 606    | No file  | `b0f55ec4235a`  |
| 599    | No file  | `b0f55ec4235a`  |
| 592    | No file  | `b0f55ec4235a`  |
| 586    | No file  | `b0f55ec4235a`  |
| 577    | No file  | `b0f55ec4235a`  |
| 569    | No file  | `b0f55ec4235a`  |
| 561    | No file  | `b0f55ec4235a`  |
| 554    | No file  | `b0f55ec4235a`  |
| 542    | No file  | `b0f55ec4235a`  |
| 532    | No file  | `b0f55ec4235a`  |
| 531    | No file  | `b0f55ec4235a`  |
| 526    | No file  | `b0f55ec4235a`  |
| 521    | No file  | `b0f55ec4235a`  |
| 517    | No file  | `b0f55ec4235a`  |
| 510    | No file  | `b0f55ec4235a`  |
| 508    | No file  | `b0f55ec4235a`  |
| 504    | No file  | `b0f55ec4235a`  |
| 497    | No file  | `b0f55ec4235a`  |
| 491    | No file  | `b0f55ec4235a`  |
| 485    | No file  | `b0f55ec4235a`  |
| 478    | No file  | `b0f55ec4235a`  |
| 472    | No file  | `b0f55ec4235a`  |
| 466    | No file  | `b0f55ec4235a`  |
| 457    | No file  | `b0f55ec4235a`  |
| 452    | No file  | `b0f55ec4235a`  |
| 449    | No file  | `b0f55ec4235a`  |
| 435    | No file  | `b0f55ec4235a`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                          |
| ---------------------------- | -------- | ------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key; a key without a row shows as plain text instead of a link |
| `languagedata_en.loc`        | Optional | Character name (type `6`, `str_id1` = `character_key`)        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of u16 rows with an empty string table, the shape of
[`itemimprovementdefaultdisplaylist.bss`](itemimprovementdefaultdisplaylist_bss.md)
with u16 rows in place of u32.

| Offset              | Type         | Field              | Notes                                   |
| ------------------- | ------------ | ------------------ | --------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                            |
| `+0x04`             | u32          | count              | Number of keys; `122` on client 3474    |
| `+0x08`             | u16[count]   | character_keys     | `characterstatic.dbss` keys; unique     |
| `character_keys+0x00` | String Table | string_table     | Empty string table                      |
| `string_table+0x00` | u32          | string_table_start | End of the keys (`8 + 2 * count`)       |
| `string_table+0x04` | u32          | zero               | `0`                                     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Key Groups

Key ranges and the developer notes of the `Character_Table_CutScene` sheet
in a private server's `.xlsm` on client 1784; counts and LOC names from
client 3474.

| Keys             | Keys in file | Sheet note (translated)                     | LOC type 6 names                                   |
| ---------------- | ------------ | ------------------------------------------- | -------------------------------------------------- |
| `400` to `410`   | 10           | For cutscenes: PC, object, villagers of each region, boss | Object, PC, Villager, Player          |
| `411` to `430`   | 13           | Tutorial NPCs for staging                   | Tutorial_Illezra_Move, Everfrost_Rare_Fixed        |
| `61032`, `61989` to `61999` | 12 | Not in the sheet                          | A1 Sequence NPC, Sequence NPC                      |
| `44711` to `44714` | 4          | Not in the sheet                            | MediahSequence                                     |
| `62001` to `62047` | 47         | Sequence NPC library, `62001` to `62050`    | Human_Male_Adult_Normal, Other_Mount               |
| `62051` to `62071` | 21         | Sequence monster library, `62051` to `62100` | Monster_Ogre, Monster_Red Nose                    |
| `22914` to `29475` | 15         | Not in the sheet                            | Kalqueesh, Elten, Gumiho, Bari, Lee Duksoo         |

## Field Names

`character_keys` is the `Index` column of the `Character_Table_CutScene`
sheet in a private server's `DataSheets.bexcel` on client 1784, its only
compiled column: the 79 rows match the 79 keys of that client's file in
order, and all 79 are in the client 3474 file. The sheet's note columns
(`#참조1(캐릭터)`, character reference) name each row by its character.

## Notes

- Client 3474 holds the 79 keys of client 1784 plus 43 more. Client 1784
  lists them in ascending order; client 3474 does not (it starts `410`,
  `61990` to `61999`, `61989`, `61032`, `400`), and the order carries no
  meaning found so far.
- On client 3474, `62070` and `62071` have no `characterstatic.dbss` row
  and no LOC type 6 name; every other key has both.
- The server dump of a private server on client 1784 holds the error text
  `CutSceneCharacterStaticStatusManager - linkAndCheckValid` (UTF-16), so
  the server builds a manager over these keys and checks them against the
  character table.
- No client Lua file on client 3474 names the file, the sheet or a
  cutscene character function.

## Open Questions

### What the Client Reads the List For

The client Lua does not read the list, and nothing in the data shows what
membership changes for a character. The 2016 PDB names a function
`PACharacterScene::isCutsceneCharacter`; whether it reads this list is
unknown, since no loader in the PDB names the file.
