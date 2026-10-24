# `barter_npclist.bss` Format

## Purpose

Lists the barter NPCs of the Great Ocean: one row per barter region (the island, port or ship where the barter happens) with the NPC who trades there. The barter windows key everything by that region key (`ToClient_barterWrapper(RegionKey(regionKey))` in `panel_window_barterinfosearch_2.luac`), so this table is what ties a barter region to its NPC.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 1239 and later | 3483    | `barter_npclist.bss` | 384   | 91 Row  | 4         |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 1      | `barter_npclist.bss` | 384 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `3e18b202cc33`  |
| 3482   | Layout 1 | `3e18b202cc33`  |
| 3474   | Layout 1 | `3e18b202cc33`  |
| 3473   | Layout 1 | `3e18b202cc33`  |
| 3464   | Layout 1 | `3e18b202cc33`  |
| 3458   | Layout 1 | `3e18b202cc33`  |
| 3454   | Layout 1 | `3e18b202cc33`  |
| 3444   | Layout 1 | `3e18b202cc33`  |
| 3435   | Layout 1 | `3e18b202cc33`  |
| 3426   | Layout 1 | `3e18b202cc33`  |
| 3418   | Layout 1 | `3e18b202cc33`  |
| 3412   | Layout 1 | `3e18b202cc33`  |
| 3402   | Layout 1 | `3e18b202cc33`  |
| 3396   | Layout 1 | `3e18b202cc33`  |
| 3387   | Layout 1 | `3e18b202cc33`  |
| 3381   | Layout 1 | `3e18b202cc33`  |
| 3373   | Layout 1 | `3e18b202cc33`  |
| 3364   | Layout 1 | `3e18b202cc33`  |
| 3356   | Layout 1 | `3e18b202cc33`  |
| 3349   | Layout 1 | `3e18b202cc33`  |
| 3342   | Layout 1 | `3e18b202cc33`  |
| 3335   | Layout 1 | `3e18b202cc33`  |
| 3326   | Layout 1 | `3e18b202cc33`  |
| 3321   | Layout 1 | `3e18b202cc33`  |
| 3314   | Layout 1 | `3e18b202cc33`  |
| 3303   | Layout 1 | `3e18b202cc33`  |
| 3302   | Layout 1 | `3e18b202cc33`  |
| 3293   | Layout 1 | `3e18b202cc33`  |
| 3283   | Layout 1 | `3e18b202cc33`  |
| 3275   | Layout 1 | `3e18b202cc33`  |
| 3267   | Layout 1 | `3e18b202cc33`  |
| 3258   | Layout 1 | `3e18b202cc33`  |
| 3251   | Layout 1 | `3e18b202cc33`  |
| 3242   | Layout 1 | `3e18b202cc33`  |
| 3235   | Layout 1 | `3e18b202cc33`  |
| 3229   | Layout 1 | `3e18b202cc33`  |
| 3212   | Layout 1 | `3e18b202cc33`  |
| 3203   | Layout 1 | `3e18b202cc33`  |
| 3193   | Layout 1 | `3e18b202cc33`  |
| 3186   | Layout 1 | `3e18b202cc33`  |
| 3177   | Layout 1 | `3e18b202cc33`  |
| 3169   | Layout 1 | `3e18b202cc33`  |
| 3158   | Layout 1 | `3e18b202cc33`  |
| 3151   | Layout 1 | `3e18b202cc33`  |
| 3144   | Layout 1 | `3e18b202cc33`  |
| 3133   | Layout 1 | `3e18b202cc33`  |
| 3125   | Layout 1 | `3e18b202cc33`  |
| 3118   | Layout 1 | `3e18b202cc33`  |
| 3111   | Layout 1 | `3e18b202cc33`  |
| 3103   | Layout 1 | `3e18b202cc33`  |
| 3095   | Layout 1 | `3e18b202cc33`  |
| 3086   | Layout 1 | `3e18b202cc33`  |
| 3072   | Layout 1 | `3e18b202cc33`  |
| 3062   | Layout 1 | `3e18b202cc33`  |
| 3052   | Layout 1 | `3e18b202cc33`  |
| 3045   | Layout 1 | `3e18b202cc33`  |
| 3037   | Layout 1 | `3e18b202cc33`  |
| 3030   | Layout 1 | `3e18b202cc33`  |
| 3021   | Layout 1 | `3e18b202cc33`  |
| 3012   | Layout 1 | `3e18b202cc33`  |
| 3002   | Layout 1 | `3e18b202cc33`  |
| 2995   | Layout 1 | `3e18b202cc33`  |
| 2987   | Layout 1 | `3e18b202cc33`  |
| 2978   | Layout 1 | `3e18b202cc33`  |
| 2970   | Layout 1 | `3e18b202cc33`  |
| 2959   | Layout 1 | `3e18b202cc33`  |
| 2951   | Layout 1 | `3e18b202cc33`  |
| 2942   | Layout 1 | `3e18b202cc33`  |
| 2935   | Layout 1 | `3e18b202cc33`  |
| 2932   | Layout 1 | `3e18b202cc33`  |
| 2923   | Layout 1 | `3e18b202cc33`  |
| 2919   | Layout 1 | `3e18b202cc33`  |
| 2907   | Layout 1 | `3e18b202cc33`  |
| 2900   | Layout 1 | `3e18b202cc33`  |
| 2891   | Layout 1 | `3e18b202cc33`  |
| 2882   | Layout 1 | `3e18b202cc33`  |
| 2872   | Layout 1 | `3e18b202cc33`  |
| 2863   | Layout 1 | `3e18b202cc33`  |
| 2855   | Layout 1 | `3e18b202cc33`  |
| 2849   | Layout 1 | `3e18b202cc33`  |
| 2844   | Layout 1 | `3e18b202cc33`  |
| 2834   | Layout 1 | `3e18b202cc33`  |
| 2825   | Layout 1 | `3e18b202cc33`  |
| 2819   | Layout 1 | `3e18b202cc33`  |
| 2811   | Layout 1 | `3e18b202cc33`  |
| 2803   | Layout 1 | `3e18b202cc33`  |
| 2794   | Layout 1 | `3e18b202cc33`  |
| 2783   | Layout 1 | `3e18b202cc33`  |
| 2774   | Layout 1 | `3e18b202cc33`  |
| 2765   | Layout 1 | `3e18b202cc33`  |
| 2756   | Layout 1 | `3e18b202cc33`  |
| 2750   | Layout 1 | `3e18b202cc33`  |
| 2743   | Layout 1 | `3e18b202cc33`  |
| 2736   | Layout 1 | `3e18b202cc33`  |
| 2726   | Layout 1 | `3e18b202cc33`  |
| 2717   | Layout 1 | `3e18b202cc33`  |
| 2709   | Layout 1 | `3e18b202cc33`  |
| 2703   | Layout 1 | `3e18b202cc33`  |
| 2695   | Layout 1 | `3e18b202cc33`  |
| 2684   | Layout 1 | `3e18b202cc33`  |
| 2672   | Layout 1 | `3e18b202cc33`  |
| 2665   | Layout 1 | `3e18b202cc33`  |
| 2657   | Layout 1 | `3e18b202cc33`  |
| 2649   | Layout 1 | `3e18b202cc33`  |
| 2644   | Layout 1 | `3e18b202cc33`  |
| 2637   | Layout 1 | `3e18b202cc33`  |
| 2629   | Layout 1 | `3e18b202cc33`  |
| 2619   | Layout 1 | `3e18b202cc33`  |
| 2612   | Layout 1 | `3e18b202cc33`  |
| 2606   | Layout 1 | `3e18b202cc33`  |
| 2602   | Layout 1 | `3e18b202cc33`  |
| 2601   | Layout 1 | `3e18b202cc33`  |
| 2592   | Layout 1 | `3e18b202cc33`  |
| 2583   | Layout 1 | `3e18b202cc33`  |
| 2575   | Layout 1 | `3e18b202cc33`  |
| 2567   | Layout 1 | `3e18b202cc33`  |
| 2560   | Layout 1 | `3e18b202cc33`  |
| 2553   | Layout 1 | `3e18b202cc33`  |
| 2545   | Layout 1 | `3e18b202cc33`  |
| 2538   | Layout 1 | `3e18b202cc33`  |
| 2529   | Layout 1 | `3e18b202cc33`  |
| 2519   | Layout 1 | `3e18b202cc33`  |
| 2513   | Layout 1 | `3e18b202cc33`  |
| 2510   | Layout 1 | `3e18b202cc33`  |
| 2507   | Layout 1 | `3e18b202cc33`  |
| 2503   | Layout 1 | `3e18b202cc33`  |
| 2498   | Layout 1 | `3e18b202cc33`  |
| 2492   | Layout 1 | `3e18b202cc33`  |
| 2487   | Layout 1 | `3e18b202cc33`  |
| 2480   | Layout 1 | `3e18b202cc33`  |
| 2474   | Layout 1 | `3e18b202cc33`  |
| 2468   | Layout 1 | `3e18b202cc33`  |
| 2460   | Layout 1 | `3e18b202cc33`  |
| 2453   | Layout 1 | `3e18b202cc33`  |
| 2444   | Layout 1 | `3e18b202cc33`  |
| 2438   | Layout 1 | `3e18b202cc33`  |
| 2434   | Layout 1 | `3e18b202cc33`  |
| 2429   | Layout 1 | `3e18b202cc33`  |
| 2421   | Layout 1 | `3e18b202cc33`  |
| 2414   | Layout 1 | `3e18b202cc33`  |
| 2407   | Layout 1 | `3e18b202cc33`  |
| 2401   | Layout 1 | `3e18b202cc33`  |
| 2397   | Layout 1 | `3e18b202cc33`  |
| 2393   | Layout 1 | `3e18b202cc33`  |
| 2384   | Layout 1 | `3e18b202cc33`  |
| 2378   | Layout 1 | `3e18b202cc33`  |
| 2372   | Layout 1 | `3e18b202cc33`  |
| 2358   | Layout 1 | `3e18b202cc33`  |
| 2352   | Layout 1 | `3e18b202cc33`  |
| 2347   | Layout 1 | `3e18b202cc33`  |
| 2343   | Layout 1 | `3e18b202cc33`  |
| 2335   | Layout 1 | `3e18b202cc33`  |
| 2327   | Layout 1 | `3e18b202cc33`  |
| 2324   | Layout 1 | `3e18b202cc33`  |
| 2319   | Layout 1 | `3e18b202cc33`  |
| 2313   | Layout 1 | `3e18b202cc33`  |
| 2308   | Layout 1 | `3e18b202cc33`  |
| 2302   | Layout 1 | `3e18b202cc33`  |
| 2295   | Layout 1 | `3e18b202cc33`  |
| 2290   | Layout 1 | `3e18b202cc33`  |
| 2284   | Layout 1 | `3e18b202cc33`  |
| 2276   | Layout 1 | `3e18b202cc33`  |
| 2269   | Layout 1 | `3e18b202cc33`  |
| 2259   | Layout 1 | `3e18b202cc33`  |
| 2250   | Layout 1 | `3e18b202cc33`  |
| 2243   | Layout 1 | `3e18b202cc33`  |
| 2235   | Layout 1 | `3e18b202cc33`  |
| 2229   | Layout 1 | `3e18b202cc33`  |
| 2224   | Layout 1 | `3e18b202cc33`  |
| 2218   | Layout 1 | `3e18b202cc33`  |
| 2215   | Layout 1 | `3e18b202cc33`  |
| 2207   | Layout 1 | `3e18b202cc33`  |
| 2203   | Layout 1 | `3e18b202cc33`  |
| 2196   | Layout 1 | `3e18b202cc33`  |
| 2192   | Layout 1 | `3e18b202cc33`  |
| 2189   | Layout 1 | `3e18b202cc33`  |
| 2183   | Layout 1 | `3e18b202cc33`  |
| 2179   | Layout 1 | `3e18b202cc33`  |
| 2171   | Layout 1 | `3e18b202cc33`  |
| 2163   | Layout 1 | `3e18b202cc33`  |
| 2156   | Layout 1 | `3e18b202cc33`  |
| 2151   | Layout 1 | `3e18b202cc33`  |
| 2147   | Layout 1 | `3e18b202cc33`  |
| 2142   | Layout 1 | `3e18b202cc33`  |
| 2138   | Layout 1 | `3e18b202cc33`  |
| 2134   | Layout 1 | `3e18b202cc33`  |
| 2130   | Layout 1 | `3e18b202cc33`  |
| 2122   | Layout 1 | `3e18b202cc33`  |
| 2107   | Layout 1 | `3e18b202cc33`  |
| 2098   | Layout 1 | `3e18b202cc33`  |
| 2089   | Layout 1 | `3e18b202cc33`  |
| 2081   | Layout 1 | `3e18b202cc33`  |
| 2073   | Layout 1 | `3e18b202cc33`  |
| 2067   | Layout 1 | `3e18b202cc33`  |
| 2063   | Layout 1 | `3e18b202cc33`  |
| 2059   | Layout 1 | `3e18b202cc33`  |
| 2052   | Layout 1 | `3e18b202cc33`  |
| 2044   | Layout 1 | `3e18b202cc33`  |
| 2039   | Layout 1 | `3e18b202cc33`  |
| 2032   | Layout 1 | `3e18b202cc33`  |
| 2025   | Layout 1 | `3e18b202cc33`  |
| 2011   | Layout 1 | `3e18b202cc33`  |
| 2005   | Layout 1 | `3e18b202cc33`  |
| 2000   | Layout 1 | `3e18b202cc33`  |
| 1996   | Layout 1 | `3e18b202cc33`  |
| 1991   | Layout 1 | `3e18b202cc33`  |
| 1985   | Layout 1 | `3e18b202cc33`  |
| 1980   | Layout 1 | `3e18b202cc33`  |
| 1969   | Layout 1 | `3e18b202cc33`  |
| 1964   | Layout 1 | `3e18b202cc33`  |
| 1958   | Layout 1 | `3e18b202cc33`  |
| 1950   | Layout 1 | `3e18b202cc33`  |
| 1945   | Layout 1 | `3e18b202cc33`  |
| 1937   | Layout 1 | `3e18b202cc33`  |
| 1933   | Layout 1 | `3e18b202cc33`  |
| 1927   | Layout 1 | `3e18b202cc33`  |
| 1921   | Layout 1 | `3e18b202cc33`  |
| 1914   | Layout 1 | `3e18b202cc33`  |
| 1908   | Layout 1 | `3e18b202cc33`  |
| 1897   | Layout 1 | `3e18b202cc33`  |
| 1892   | Layout 1 | `3e18b202cc33`  |
| 1886   | Layout 1 | `3e18b202cc33`  |
| 1881   | Layout 1 | `3e18b202cc33`  |
| 1871   | Layout 1 | `3e18b202cc33`  |
| 1866   | Layout 1 | `3e18b202cc33`  |
| 1862   | Layout 1 | `3e18b202cc33`  |
| 1854   | Layout 1 | `3e18b202cc33`  |
| 1846   | Layout 1 | `3e18b202cc33`  |
| 1838   | Layout 1 | `3e18b202cc33`  |
| 1832   | Layout 1 | `3e18b202cc33`  |
| 1826   | Layout 1 | `3e18b202cc33`  |
| 1822   | Layout 1 | `3e18b202cc33`  |
| 1818   | Layout 1 | `3e18b202cc33`  |
| 1804   | Layout 1 | `3e18b202cc33`  |
| 1794   | Layout 1 | `3e18b202cc33`  |
| 1790   | Layout 1 | `3e18b202cc33`  |
| 1784   | Layout 1 | `3e18b202cc33`  |
| 1774   | Layout 1 | `3e18b202cc33`  |
| 1771   | Layout 1 | `3e18b202cc33`  |
| 1762   | Layout 1 | `3e18b202cc33`  |
| 1759   | Layout 1 | `3e18b202cc33`  |
| 1754   | Layout 1 | `3e18b202cc33`  |
| 1749   | Layout 1 | `3e18b202cc33`  |
| 1743   | Layout 1 | `3e18b202cc33`  |
| 1737   | Layout 1 | `3e18b202cc33`  |
| 1731   | Layout 1 | `3e18b202cc33`  |
| 1725   | Layout 1 | `3e18b202cc33`  |
| 1717   | Layout 1 | `3e18b202cc33`  |
| 1710   | Layout 1 | `3e18b202cc33`  |
| 1704   | Layout 1 | `3e18b202cc33`  |
| 1698   | Layout 1 | `3e18b202cc33`  |
| 1690   | Layout 1 | `3e18b202cc33`  |
| 1685   | Layout 1 | `3e18b202cc33`  |
| 1680   | Layout 1 | `3e18b202cc33`  |
| 1674   | Layout 1 | `3e18b202cc33`  |
| 1668   | Layout 1 | `3e18b202cc33`  |
| 1659   | Layout 1 | `3e18b202cc33`  |
| 1649   | Layout 1 | `3e18b202cc33`  |
| 1642   | Layout 1 | `3e18b202cc33`  |
| 1636   | Layout 1 | `3e18b202cc33`  |
| 1628   | Layout 1 | `3e18b202cc33`  |
| 1622   | Layout 1 | `3e18b202cc33`  |
| 1614   | Layout 1 | `3e18b202cc33`  |
| 1608   | Layout 1 | `3e18b202cc33`  |
| 1602   | Layout 1 | `3e18b202cc33`  |
| 1598   | Layout 1 | `3e18b202cc33`  |
| 1594   | Layout 1 | `3e18b202cc33`  |
| 1590   | Layout 1 | `3e18b202cc33`  |
| 1587   | Layout 1 | `3e18b202cc33`  |
| 1584   | Layout 1 | `3e18b202cc33`  |
| 1579   | Layout 1 | `3e18b202cc33`  |
| 1572   | Layout 1 | `3e18b202cc33`  |
| 1565   | Layout 1 | `3e18b202cc33`  |
| 1559   | Layout 1 | `3e18b202cc33`  |
| 1554   | Layout 1 | `3e18b202cc33`  |
| 1547   | Layout 1 | `3e18b202cc33`  |
| 1537   | Layout 1 | `3e18b202cc33`  |
| 1529   | Layout 1 | `3e18b202cc33`  |
| 1524   | Layout 1 | `3e18b202cc33`  |
| 1519   | Layout 1 | `3e18b202cc33`  |
| 1509   | Layout 1 | `3e18b202cc33`  |
| 1506   | Layout 1 | `3e18b202cc33`  |
| 1504   | Layout 1 | `3e18b202cc33`  |
| 1500   | Layout 1 | `3e18b202cc33`  |
| 1493   | Layout 1 | `3e18b202cc33`  |
| 1489   | Layout 1 | `3e18b202cc33`  |
| 1485   | Layout 1 | `3e18b202cc33`  |
| 1481   | Layout 1 | `3e18b202cc33`  |
| 1474   | Layout 1 | `3e18b202cc33`  |
| 1466   | Layout 1 | `3e18b202cc33`  |
| 1462   | Layout 1 | `3e18b202cc33`  |
| 1459   | Layout 1 | `3e18b202cc33`  |
| 1453   | Layout 1 | `3e18b202cc33`  |
| 1450   | Layout 1 | `3e18b202cc33`  |
| 1445   | Layout 1 | `3e18b202cc33`  |
| 1439   | Layout 1 | `3e18b202cc33`  |
| 1433   | Layout 1 | `3e18b202cc33`  |
| 1430   | Layout 1 | `3e18b202cc33`  |
| 1426   | Layout 1 | `3e18b202cc33`  |
| 1421   | Layout 1 | `3e18b202cc33`  |
| 1417   | Layout 1 | `3e18b202cc33`  |
| 1416   | Layout 1 | `3e18b202cc33`  |
| 1409   | Layout 1 | `3e18b202cc33`  |
| 1405   | Layout 1 | `3e18b202cc33`  |
| 1401   | Layout 1 | `3e18b202cc33`  |
| 1396   | Layout 1 | `3e18b202cc33`  |
| 1391   | Layout 1 | `3e18b202cc33`  |
| 1390   | Layout 1 | `3e18b202cc33`  |
| 1386   | Layout 1 | `3e18b202cc33`  |
| 1381   | Layout 1 | `3e18b202cc33`  |
| 1379   | Layout 1 | `3e18b202cc33`  |
| 1372   | Layout 1 | `3e18b202cc33`  |
| 1366   | Layout 1 | `3e18b202cc33`  |
| 1364   | Layout 1 | `3e18b202cc33`  |
| 1363   | Layout 1 | `3e18b202cc33`  |
| 1360   | Layout 1 | `3e18b202cc33`  |
| 1358   | Layout 1 | `3e18b202cc33`  |
| 1355   | Layout 1 | `3e18b202cc33`  |
| 1351   | Layout 1 | `3e18b202cc33`  |
| 1348   | Layout 1 | `3e18b202cc33`  |
| 1346   | Layout 1 | `3e18b202cc33`  |
| 1341   | Layout 1 | `3e18b202cc33`  |
| 1340   | Layout 1 | `3e18b202cc33`  |
| 1338   | Layout 1 | `3e18b202cc33`  |
| 1335   | Layout 1 | `3e18b202cc33`  |
| 1333   | Layout 1 | `3e18b202cc33`  |
| 1329   | Layout 1 | `3e18b202cc33`  |
| 1327   | Layout 1 | `3e18b202cc33`  |
| 1324   | Layout 1 | `3e18b202cc33`  |
| 1321   | Layout 1 | `3e18b202cc33`  |
| 1319   | Layout 1 | `3e18b202cc33`  |
| 1318   | Layout 1 | `3e18b202cc33`  |
| 1316   | Layout 1 | `3e18b202cc33`  |
| 1313   | Layout 1 | `3e18b202cc33`  |
| 1311   | Layout 1 | `3e18b202cc33`  |
| 1309   | Layout 1 | `3e18b202cc33`  |
| 1304   | Layout 1 | `3e18b202cc33`  |
| 1292   | Layout 1 | `3e18b202cc33`  |
| 1286   | Layout 1 | `3e18b202cc33`  |
| 1280   | Layout 1 | `3e18b202cc33`  |
| 1276   | Layout 1 | `3e18b202cc33`  |
| 1267   | Layout 1 | `3e18b202cc33`  |
| 1261   | Layout 1 | `3e18b202cc33`  |
| 1256   | Layout 1 | `3e18b202cc33`  |
| 1250   | Layout 1 | `3e18b202cc33`  |
| 1246   | Layout 1 | `3e18b202cc33`  |
| 1239   | Layout 1 | `3e18b202cc33`  |
| 1230   | No file  | `3e18b202cc33`  |
| 1226   | No file  | `3e18b202cc33`  |
| 1220   | No file  | `3e18b202cc33`  |
| 1217   | No file  | `3e18b202cc33`  |
| 1211   | No file  | `3e18b202cc33`  |
| 1210   | No file  | `3e18b202cc33`  |
| 1208   | No file  | `3e18b202cc33`  |
| 1203   | No file  | `3e18b202cc33`  |
| 1197   | No file  | `3e18b202cc33`  |
| 1194   | No file  | `3e18b202cc33`  |
| 1192   | No file  | `3e18b202cc33`  |
| 1187   | No file  | `3e18b202cc33`  |
| 1183   | No file  | `3e18b202cc33`  |
| 1177   | No file  | `3e18b202cc33`  |
| 1173   | No file  | `3e18b202cc33`  |
| 1167   | No file  | `3e18b202cc33`  |
| 1164   | No file  | `3e18b202cc33`  |
| 1156   | No file  | `3e18b202cc33`  |
| 1149   | No file  | `3e18b202cc33`  |
| 1144   | No file  | `3e18b202cc33`  |
| 1137   | No file  | `3e18b202cc33`  |
| 1132   | No file  | `3e18b202cc33`  |
| 1127   | No file  | `3e18b202cc33`  |
| 1122   | No file  | `3e18b202cc33`  |
| 1118   | No file  | `3e18b202cc33`  |
| 1114   | No file  | `3e18b202cc33`  |
| 1109   | No file  | `3e18b202cc33`  |
| 1102   | No file  | `3e18b202cc33`  |
| 1096   | No file  | `3e18b202cc33`  |
| 1088   | No file  | `3e18b202cc33`  |
| 1081   | No file  | `3e18b202cc33`  |
| 1076   | No file  | `3e18b202cc33`  |
| 1069   | No file  | `3e18b202cc33`  |
| 1064   | No file  | `3e18b202cc33`  |
| 1058   | No file  | `3e18b202cc33`  |
| 1051   | No file  | `3e18b202cc33`  |
| 1044   | No file  | `3e18b202cc33`  |
| 1036   | No file  | `3e18b202cc33`  |
| 1026   | No file  | `3e18b202cc33`  |
| 1016   | No file  | `3e18b202cc33`  |
| 1009   | No file  | `3e18b202cc33`  |
| 1005   | No file  | `3e18b202cc33`  |
| 1000   | No file  | `3e18b202cc33`  |
| 998    | No file  | `3e18b202cc33`  |
| 990    | No file  | `3e18b202cc33`  |
| 979    | No file  | `3e18b202cc33`  |
| 972    | No file  | `3e18b202cc33`  |
| 963    | No file  | `3e18b202cc33`  |
| 955    | No file  | `3e18b202cc33`  |
| 946    | No file  | `3e18b202cc33`  |
| 938    | No file  | `3e18b202cc33`  |
| 927    | No file  | `3e18b202cc33`  |
| 911    | No file  | `3e18b202cc33`  |
| 904    | No file  | `3e18b202cc33`  |
| 899    | No file  | `3e18b202cc33`  |
| 894    | No file  | `3e18b202cc33`  |
| 885    | No file  | `3e18b202cc33`  |
| 879    | No file  | `3e18b202cc33`  |
| 872    | No file  | `3e18b202cc33`  |
| 864    | No file  | `3e18b202cc33`  |
| 855    | No file  | `3e18b202cc33`  |
| 853    | No file  | `3e18b202cc33`  |
| 845    | No file  | `3e18b202cc33`  |
| 837    | No file  | `3e18b202cc33`  |
| 829    | No file  | `3e18b202cc33`  |
| 822    | No file  | `3e18b202cc33`  |
| 814    | No file  | `3e18b202cc33`  |
| 805    | No file  | `3e18b202cc33`  |
| 794    | No file  | `3e18b202cc33`  |
| 787    | No file  | `3e18b202cc33`  |
| 780    | No file  | `3e18b202cc33`  |
| 771    | No file  | `3e18b202cc33`  |
| 760    | No file  | `3e18b202cc33`  |
| 748    | No file  | `3e18b202cc33`  |
| 741    | No file  | `3e18b202cc33`  |
| 736    | No file  | `3e18b202cc33`  |
| 731    | No file  | `3e18b202cc33`  |
| 723    | No file  | `3e18b202cc33`  |
| 711    | No file  | `3e18b202cc33`  |
| 707    | No file  | `3e18b202cc33`  |
| 697    | No file  | `3e18b202cc33`  |
| 689    | No file  | `3e18b202cc33`  |
| 683    | No file  | `3e18b202cc33`  |
| 678    | No file  | `3e18b202cc33`  |
| 670    | No file  | `3e18b202cc33`  |
| 661    | No file  | `3e18b202cc33`  |
| 656    | No file  | `3e18b202cc33`  |
| 652    | No file  | `3e18b202cc33`  |
| 643    | No file  | `3e18b202cc33`  |
| 637    | No file  | `3e18b202cc33`  |
| 630    | No file  | `3e18b202cc33`  |
| 627    | No file  | `3e18b202cc33`  |
| 621    | No file  | `3e18b202cc33`  |
| 617    | No file  | `3e18b202cc33`  |
| 615    | No file  | `3e18b202cc33`  |
| 606    | No file  | `3e18b202cc33`  |
| 599    | No file  | `3e18b202cc33`  |
| 592    | No file  | `3e18b202cc33`  |
| 586    | No file  | `3e18b202cc33`  |
| 577    | No file  | `3e18b202cc33`  |
| 569    | No file  | `3e18b202cc33`  |
| 561    | No file  | `3e18b202cc33`  |
| 554    | No file  | `3e18b202cc33`  |
| 542    | No file  | `3e18b202cc33`  |
| 532    | No file  | `3e18b202cc33`  |
| 531    | No file  | `3e18b202cc33`  |
| 526    | No file  | `3e18b202cc33`  |
| 521    | No file  | `3e18b202cc33`  |
| 517    | No file  | `3e18b202cc33`  |
| 510    | No file  | `3e18b202cc33`  |
| 508    | No file  | `3e18b202cc33`  |
| 504    | No file  | `3e18b202cc33`  |
| 497    | No file  | `3e18b202cc33`  |
| 491    | No file  | `3e18b202cc33`  |
| 485    | No file  | `3e18b202cc33`  |
| 478    | No file  | `3e18b202cc33`  |
| 472    | No file  | `3e18b202cc33`  |
| 466    | No file  | `3e18b202cc33`  |
| 457    | No file  | `3e18b202cc33`  |
| 452    | No file  | `3e18b202cc33`  |
| 449    | No file  | `3e18b202cc33`  |
| 435    | No file  | `3e18b202cc33`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                          |
| --------------------- | -------- | --------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names (type 17) and NPC names (type 6) |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                                                    |
| ------------------- | ----------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                           |
| `+0x04`             | u32               | record_count       | `91` on client 3464                                      |
| `+0x08`             | Row[record_count] | records            | See Row                                                  |
| `records+0x00`      | String Table      | string_table       | The PABR string table, present but empty                 |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 4 × count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                               |

The file is `8 + 4 × 91 + 12 = 384` bytes on client 3464. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (4 bytes)

| Offset  | Type | Field             | Notes                                                                 |
| ------- | ---- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | barter_region_key | `regioninfo.bss` region key; unique                                   |
| `+0x02` | u16  | character_id      | The barter NPC; unique, and its `characterfunction.dbss` record has a Maritime Trade button |

Rows are in neither key nor character order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Notes

- On client 3464 the `maritime_trade` slot of [`characterfunction.dbss`](characterfunction_dbss.md) stores the same key as `barter_region_key` for all 91 characters, and those 91 are the only characters with a non-zero `barter_region_key`.
- The regions (client 3464): 70 islands, Arehaza, 8 coastal ports (Olvia Coast, Epheria Sentry Post, Sausan Garrison Wharf, Grándiha, Starry Midnight Port, Sanctuary Coastal Outpost, Dallae Pier, Crow's Nest) and 12 ship regions. Lema Island, Iliya Island and Arehaza are `MinorTown`, the others `Hunting`. The ship regions belong to characters 50814 to 50827 (Crow Merchants' Vessel, Old Moon Guild's Carrack, Wandering Merchant's Ship, Cholace Chico's Pirate Union and eight wrecks and rafts). The 12 ship regions are the only ones with `regioninfo.bss` `is_ocean` set.
- The other barter tables are [barter_normal](barter_normal_bss.md), [barter_special](barter_special_bss.md), [bartersubgroup](bartersubgroup_bss.md), [barterlifelevelinfo](barterlifelevelinfo_bss.md) and [barterresetoption](barterresetoption_bss.md). Both region lists of `barter_normal.bss` hold the 91 region keys of this file (client 3474).
