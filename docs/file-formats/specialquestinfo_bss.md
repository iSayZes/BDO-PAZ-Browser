# `specialquestinfo.bss` Format

## Purpose

Special quest groups: each group key lists packed quest IDs. The `quest.dbss` action script call `alreadyclearspecialquest(group)` names a group by its key, and each quest that calls it asks for the content the group lists: quest 4464 / 12 `[Suggested] Complete [Pet] Lauren's Fluffy` calls group 2, which lists four `[Pet] Lauren's Fluffy` quests of chain 21416, and quest 4464 / 18 `[Succession/Awakening] Continue to Grow Strong After Succession/Awakening` calls group 4, which lists one awakening, succession or ascension quest per class. The plain PABR file holds the groups, then an empty string table.

Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, as in [`allquestlist.bss`](allquestlist_bss.md) and [`specialquestlist.bss`](specialquestlist_bss.md), and is the `packed_quest_id` of a [`quest.dbss`](quest_dbss.md) record.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records  | Row bytes                |
| ------ | -------------- | ---------------------- | ----- | -------- | ------------------------ |
| 1      | 1717 and later | `specialquestinfo.bss` | 1,556 | 36 Group | 12 to 140, 43 on average |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `specialquestinfo.bss` | 1,556 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `59de010f8dd4`  |
| 3482   | Layout 1 | `59de010f8dd4`  |
| 3474   | Layout 1 | `59de010f8dd4`  |
| 3473   | Layout 1 | `59de010f8dd4`  |
| 3464   | Layout 1 | `59de010f8dd4`  |
| 3458   | Layout 1 | `59de010f8dd4`  |
| 3454   | Layout 1 | `59de010f8dd4`  |
| 3444   | Layout 1 | `59de010f8dd4`  |
| 3435   | Layout 1 | `59de010f8dd4`  |
| 3426   | Layout 1 | `59de010f8dd4`  |
| 3418   | Layout 1 | `59de010f8dd4`  |
| 3412   | Layout 1 | `59de010f8dd4`  |
| 3402   | Layout 1 | `59de010f8dd4`  |
| 3396   | Layout 1 | `59de010f8dd4`  |
| 3387   | Layout 1 | `59de010f8dd4`  |
| 3381   | Layout 1 | `59de010f8dd4`  |
| 3373   | Layout 1 | `59de010f8dd4`  |
| 3364   | Layout 1 | `59de010f8dd4`  |
| 3356   | Layout 1 | `59de010f8dd4`  |
| 3349   | Layout 1 | `59de010f8dd4`  |
| 3342   | Layout 1 | `59de010f8dd4`  |
| 3335   | Layout 1 | `59de010f8dd4`  |
| 3326   | Layout 1 | `59de010f8dd4`  |
| 3321   | Layout 1 | `59de010f8dd4`  |
| 3314   | Layout 1 | `59de010f8dd4`  |
| 3303   | Layout 1 | `59de010f8dd4`  |
| 3302   | Layout 1 | `59de010f8dd4`  |
| 3293   | Layout 1 | `59de010f8dd4`  |
| 3283   | Layout 1 | `59de010f8dd4`  |
| 3275   | Layout 1 | `59de010f8dd4`  |
| 3267   | Layout 1 | `59de010f8dd4`  |
| 3258   | Layout 1 | `59de010f8dd4`  |
| 3251   | Layout 1 | `59de010f8dd4`  |
| 3242   | Layout 1 | `59de010f8dd4`  |
| 3235   | Layout 1 | `59de010f8dd4`  |
| 3229   | Layout 1 | `59de010f8dd4`  |
| 3212   | Layout 1 | `59de010f8dd4`  |
| 3203   | Layout 1 | `59de010f8dd4`  |
| 3193   | Layout 1 | `59de010f8dd4`  |
| 3186   | Layout 1 | `59de010f8dd4`  |
| 3177   | Layout 1 | `59de010f8dd4`  |
| 3169   | Layout 1 | `59de010f8dd4`  |
| 3158   | Layout 1 | `59de010f8dd4`  |
| 3151   | Layout 1 | `59de010f8dd4`  |
| 3144   | Layout 1 | `59de010f8dd4`  |
| 3133   | Layout 1 | `59de010f8dd4`  |
| 3125   | Layout 1 | `59de010f8dd4`  |
| 3118   | Layout 1 | `59de010f8dd4`  |
| 3111   | Layout 1 | `59de010f8dd4`  |
| 3103   | Layout 1 | `59de010f8dd4`  |
| 3095   | Layout 1 | `59de010f8dd4`  |
| 3086   | Layout 1 | `59de010f8dd4`  |
| 3072   | Layout 1 | `59de010f8dd4`  |
| 3062   | Layout 1 | `59de010f8dd4`  |
| 3052   | Layout 1 | `59de010f8dd4`  |
| 3045   | Layout 1 | `59de010f8dd4`  |
| 3037   | Layout 1 | `59de010f8dd4`  |
| 3030   | Layout 1 | `59de010f8dd4`  |
| 3021   | Layout 1 | `59de010f8dd4`  |
| 3012   | Layout 1 | `59de010f8dd4`  |
| 3002   | Layout 1 | `59de010f8dd4`  |
| 2995   | Layout 1 | `59de010f8dd4`  |
| 2987   | Layout 1 | `59de010f8dd4`  |
| 2978   | Layout 1 | `59de010f8dd4`  |
| 2970   | Layout 1 | `59de010f8dd4`  |
| 2959   | Layout 1 | `59de010f8dd4`  |
| 2951   | Layout 1 | `59de010f8dd4`  |
| 2942   | Layout 1 | `59de010f8dd4`  |
| 2935   | Layout 1 | `59de010f8dd4`  |
| 2932   | Layout 1 | `59de010f8dd4`  |
| 2923   | Layout 1 | `59de010f8dd4`  |
| 2919   | Layout 1 | `59de010f8dd4`  |
| 2907   | Layout 1 | `59de010f8dd4`  |
| 2900   | Layout 1 | `59de010f8dd4`  |
| 2891   | Layout 1 | `59de010f8dd4`  |
| 2882   | Layout 1 | `59de010f8dd4`  |
| 2872   | Layout 1 | `59de010f8dd4`  |
| 2863   | Layout 1 | `59de010f8dd4`  |
| 2855   | Layout 1 | `59de010f8dd4`  |
| 2849   | Layout 1 | `59de010f8dd4`  |
| 2844   | Layout 1 | `59de010f8dd4`  |
| 2834   | Layout 1 | `59de010f8dd4`  |
| 2825   | Layout 1 | `59de010f8dd4`  |
| 2819   | Layout 1 | `59de010f8dd4`  |
| 2811   | Layout 1 | `59de010f8dd4`  |
| 2803   | Layout 1 | `59de010f8dd4`  |
| 2794   | Layout 1 | `59de010f8dd4`  |
| 2783   | Layout 1 | `59de010f8dd4`  |
| 2774   | Layout 1 | `59de010f8dd4`  |
| 2765   | Layout 1 | `59de010f8dd4`  |
| 2756   | Layout 1 | `59de010f8dd4`  |
| 2750   | Layout 1 | `59de010f8dd4`  |
| 2743   | Layout 1 | `59de010f8dd4`  |
| 2736   | Layout 1 | `59de010f8dd4`  |
| 2726   | Layout 1 | `59de010f8dd4`  |
| 2717   | Layout 1 | `59de010f8dd4`  |
| 2709   | Layout 1 | `59de010f8dd4`  |
| 2703   | Layout 1 | `59de010f8dd4`  |
| 2695   | Layout 1 | `59de010f8dd4`  |
| 2684   | Layout 1 | `59de010f8dd4`  |
| 2672   | Layout 1 | `59de010f8dd4`  |
| 2665   | Layout 1 | `59de010f8dd4`  |
| 2657   | Layout 1 | `59de010f8dd4`  |
| 2649   | Layout 1 | `59de010f8dd4`  |
| 2644   | Layout 1 | `59de010f8dd4`  |
| 2637   | Layout 1 | `59de010f8dd4`  |
| 2629   | Layout 1 | `59de010f8dd4`  |
| 2619   | Layout 1 | `59de010f8dd4`  |
| 2612   | Layout 1 | `59de010f8dd4`  |
| 2606   | Layout 1 | `59de010f8dd4`  |
| 2602   | Layout 1 | `59de010f8dd4`  |
| 2601   | Layout 1 | `59de010f8dd4`  |
| 2592   | Layout 1 | `59de010f8dd4`  |
| 2583   | Layout 1 | `59de010f8dd4`  |
| 2575   | Layout 1 | `59de010f8dd4`  |
| 2567   | Layout 1 | `59de010f8dd4`  |
| 2560   | Layout 1 | `59de010f8dd4`  |
| 2553   | Layout 1 | `59de010f8dd4`  |
| 2545   | Layout 1 | `59de010f8dd4`  |
| 2538   | Layout 1 | `59de010f8dd4`  |
| 2529   | Layout 1 | `59de010f8dd4`  |
| 2519   | Layout 1 | `59de010f8dd4`  |
| 2513   | Layout 1 | `59de010f8dd4`  |
| 2510   | Layout 1 | `59de010f8dd4`  |
| 2507   | Layout 1 | `59de010f8dd4`  |
| 2503   | Layout 1 | `59de010f8dd4`  |
| 2498   | Layout 1 | `59de010f8dd4`  |
| 2492   | Layout 1 | `59de010f8dd4`  |
| 2487   | Layout 1 | `59de010f8dd4`  |
| 2480   | Layout 1 | `59de010f8dd4`  |
| 2474   | Layout 1 | `59de010f8dd4`  |
| 2468   | Layout 1 | `59de010f8dd4`  |
| 2460   | Layout 1 | `59de010f8dd4`  |
| 2453   | Layout 1 | `59de010f8dd4`  |
| 2444   | Layout 1 | `59de010f8dd4`  |
| 2438   | Layout 1 | `59de010f8dd4`  |
| 2434   | Layout 1 | `59de010f8dd4`  |
| 2429   | Layout 1 | `59de010f8dd4`  |
| 2421   | Layout 1 | `59de010f8dd4`  |
| 2414   | Layout 1 | `59de010f8dd4`  |
| 2407   | Layout 1 | `59de010f8dd4`  |
| 2401   | Layout 1 | `59de010f8dd4`  |
| 2397   | Layout 1 | `59de010f8dd4`  |
| 2393   | Layout 1 | `59de010f8dd4`  |
| 2384   | Layout 1 | `59de010f8dd4`  |
| 2378   | Layout 1 | `59de010f8dd4`  |
| 2372   | Layout 1 | `59de010f8dd4`  |
| 2358   | Layout 1 | `59de010f8dd4`  |
| 2352   | Layout 1 | `59de010f8dd4`  |
| 2347   | Layout 1 | `59de010f8dd4`  |
| 2343   | Layout 1 | `59de010f8dd4`  |
| 2335   | Layout 1 | `59de010f8dd4`  |
| 2327   | Layout 1 | `59de010f8dd4`  |
| 2324   | Layout 1 | `59de010f8dd4`  |
| 2319   | Layout 1 | `59de010f8dd4`  |
| 2313   | Layout 1 | `59de010f8dd4`  |
| 2308   | Layout 1 | `59de010f8dd4`  |
| 2302   | Layout 1 | `59de010f8dd4`  |
| 2295   | Layout 1 | `59de010f8dd4`  |
| 2290   | Layout 1 | `59de010f8dd4`  |
| 2284   | Layout 1 | `59de010f8dd4`  |
| 2276   | Layout 1 | `59de010f8dd4`  |
| 2269   | Layout 1 | `59de010f8dd4`  |
| 2259   | Layout 1 | `59de010f8dd4`  |
| 2250   | Layout 1 | `59de010f8dd4`  |
| 2243   | Layout 1 | `59de010f8dd4`  |
| 2235   | Layout 1 | `59de010f8dd4`  |
| 2229   | Layout 1 | `59de010f8dd4`  |
| 2224   | Layout 1 | `59de010f8dd4`  |
| 2218   | Layout 1 | `59de010f8dd4`  |
| 2215   | Layout 1 | `59de010f8dd4`  |
| 2207   | Layout 1 | `59de010f8dd4`  |
| 2203   | Layout 1 | `59de010f8dd4`  |
| 2196   | Layout 1 | `59de010f8dd4`  |
| 2192   | Layout 1 | `59de010f8dd4`  |
| 2189   | Layout 1 | `59de010f8dd4`  |
| 2183   | Layout 1 | `59de010f8dd4`  |
| 2179   | Layout 1 | `59de010f8dd4`  |
| 2171   | Layout 1 | `59de010f8dd4`  |
| 2163   | Layout 1 | `59de010f8dd4`  |
| 2156   | Layout 1 | `59de010f8dd4`  |
| 2151   | Layout 1 | `59de010f8dd4`  |
| 2147   | Layout 1 | `59de010f8dd4`  |
| 2142   | Layout 1 | `59de010f8dd4`  |
| 2138   | Layout 1 | `59de010f8dd4`  |
| 2134   | Layout 1 | `59de010f8dd4`  |
| 2130   | Layout 1 | `59de010f8dd4`  |
| 2122   | Layout 1 | `59de010f8dd4`  |
| 2107   | Layout 1 | `59de010f8dd4`  |
| 2098   | Layout 1 | `59de010f8dd4`  |
| 2089   | Layout 1 | `59de010f8dd4`  |
| 2081   | Layout 1 | `59de010f8dd4`  |
| 2073   | Layout 1 | `59de010f8dd4`  |
| 2067   | Layout 1 | `59de010f8dd4`  |
| 2063   | Layout 1 | `59de010f8dd4`  |
| 2059   | Layout 1 | `59de010f8dd4`  |
| 2052   | Layout 1 | `59de010f8dd4`  |
| 2044   | Layout 1 | `59de010f8dd4`  |
| 2039   | Layout 1 | `59de010f8dd4`  |
| 2032   | Layout 1 | `59de010f8dd4`  |
| 2025   | Layout 1 | `59de010f8dd4`  |
| 2011   | Layout 1 | `59de010f8dd4`  |
| 2005   | Layout 1 | `59de010f8dd4`  |
| 2000   | Layout 1 | `59de010f8dd4`  |
| 1996   | Layout 1 | `59de010f8dd4`  |
| 1991   | Layout 1 | `59de010f8dd4`  |
| 1985   | Layout 1 | `59de010f8dd4`  |
| 1980   | Layout 1 | `59de010f8dd4`  |
| 1969   | Layout 1 | `59de010f8dd4`  |
| 1964   | Layout 1 | `59de010f8dd4`  |
| 1958   | Layout 1 | `59de010f8dd4`  |
| 1950   | Layout 1 | `59de010f8dd4`  |
| 1945   | Layout 1 | `59de010f8dd4`  |
| 1937   | Layout 1 | `59de010f8dd4`  |
| 1933   | Layout 1 | `59de010f8dd4`  |
| 1927   | Layout 1 | `59de010f8dd4`  |
| 1921   | Layout 1 | `59de010f8dd4`  |
| 1914   | Layout 1 | `59de010f8dd4`  |
| 1908   | Layout 1 | `59de010f8dd4`  |
| 1897   | Layout 1 | `59de010f8dd4`  |
| 1892   | Layout 1 | `59de010f8dd4`  |
| 1886   | Layout 1 | `59de010f8dd4`  |
| 1881   | Layout 1 | `59de010f8dd4`  |
| 1871   | Layout 1 | `59de010f8dd4`  |
| 1866   | Layout 1 | `59de010f8dd4`  |
| 1862   | Layout 1 | `59de010f8dd4`  |
| 1854   | Layout 1 | `59de010f8dd4`  |
| 1846   | Layout 1 | `59de010f8dd4`  |
| 1838   | Layout 1 | `59de010f8dd4`  |
| 1832   | Layout 1 | `59de010f8dd4`  |
| 1826   | Layout 1 | `59de010f8dd4`  |
| 1822   | Layout 1 | `59de010f8dd4`  |
| 1818   | Layout 1 | `59de010f8dd4`  |
| 1804   | Layout 1 | `59de010f8dd4`  |
| 1794   | Layout 1 | `59de010f8dd4`  |
| 1790   | Layout 1 | `59de010f8dd4`  |
| 1784   | Layout 1 | `59de010f8dd4`  |
| 1774   | Layout 1 | `59de010f8dd4`  |
| 1771   | Layout 1 | `59de010f8dd4`  |
| 1762   | Layout 1 | `59de010f8dd4`  |
| 1759   | Layout 1 | `59de010f8dd4`  |
| 1754   | Layout 1 | `59de010f8dd4`  |
| 1749   | Layout 1 | `59de010f8dd4`  |
| 1743   | Layout 1 | `59de010f8dd4`  |
| 1737   | Layout 1 | `59de010f8dd4`  |
| 1731   | Layout 1 | `59de010f8dd4`  |
| 1725   | Layout 1 | `59de010f8dd4`  |
| 1717   | Layout 1 | `59de010f8dd4`  |
| 1710   | No file  | `59de010f8dd4`  |
| 1704   | No file  | `59de010f8dd4`  |
| 1698   | No file  | `59de010f8dd4`  |
| 1690   | No file  | `59de010f8dd4`  |
| 1685   | No file  | `59de010f8dd4`  |
| 1680   | No file  | `59de010f8dd4`  |
| 1674   | No file  | `59de010f8dd4`  |
| 1668   | No file  | `59de010f8dd4`  |
| 1659   | No file  | `59de010f8dd4`  |
| 1649   | No file  | `59de010f8dd4`  |
| 1642   | No file  | `59de010f8dd4`  |
| 1636   | No file  | `59de010f8dd4`  |
| 1628   | No file  | `59de010f8dd4`  |
| 1622   | No file  | `59de010f8dd4`  |
| 1614   | No file  | `59de010f8dd4`  |
| 1608   | No file  | `59de010f8dd4`  |
| 1602   | No file  | `59de010f8dd4`  |
| 1598   | No file  | `59de010f8dd4`  |
| 1594   | No file  | `59de010f8dd4`  |
| 1590   | No file  | `59de010f8dd4`  |
| 1587   | No file  | `59de010f8dd4`  |
| 1584   | No file  | `59de010f8dd4`  |
| 1579   | No file  | `59de010f8dd4`  |
| 1572   | No file  | `59de010f8dd4`  |
| 1565   | No file  | `59de010f8dd4`  |
| 1559   | No file  | `59de010f8dd4`  |
| 1554   | No file  | `59de010f8dd4`  |
| 1547   | No file  | `59de010f8dd4`  |
| 1537   | No file  | `59de010f8dd4`  |
| 1529   | No file  | `59de010f8dd4`  |
| 1524   | No file  | `59de010f8dd4`  |
| 1519   | No file  | `59de010f8dd4`  |
| 1509   | No file  | `59de010f8dd4`  |
| 1506   | No file  | `59de010f8dd4`  |
| 1504   | No file  | `59de010f8dd4`  |
| 1500   | No file  | `59de010f8dd4`  |
| 1493   | No file  | `59de010f8dd4`  |
| 1489   | No file  | `59de010f8dd4`  |
| 1485   | No file  | `59de010f8dd4`  |
| 1481   | No file  | `59de010f8dd4`  |
| 1474   | No file  | `59de010f8dd4`  |
| 1466   | No file  | `59de010f8dd4`  |
| 1462   | No file  | `59de010f8dd4`  |
| 1459   | No file  | `59de010f8dd4`  |
| 1453   | No file  | `59de010f8dd4`  |
| 1450   | No file  | `59de010f8dd4`  |
| 1445   | No file  | `59de010f8dd4`  |
| 1439   | No file  | `59de010f8dd4`  |
| 1433   | No file  | `59de010f8dd4`  |
| 1430   | No file  | `59de010f8dd4`  |
| 1426   | No file  | `59de010f8dd4`  |
| 1421   | No file  | `59de010f8dd4`  |
| 1417   | No file  | `59de010f8dd4`  |
| 1416   | No file  | `59de010f8dd4`  |
| 1409   | No file  | `59de010f8dd4`  |
| 1405   | No file  | `59de010f8dd4`  |
| 1401   | No file  | `59de010f8dd4`  |
| 1396   | No file  | `59de010f8dd4`  |
| 1391   | No file  | `59de010f8dd4`  |
| 1390   | No file  | `59de010f8dd4`  |
| 1386   | No file  | `59de010f8dd4`  |
| 1381   | No file  | `59de010f8dd4`  |
| 1379   | No file  | `59de010f8dd4`  |
| 1372   | No file  | `59de010f8dd4`  |
| 1366   | No file  | `59de010f8dd4`  |
| 1364   | No file  | `59de010f8dd4`  |
| 1363   | No file  | `59de010f8dd4`  |
| 1360   | No file  | `59de010f8dd4`  |
| 1358   | No file  | `59de010f8dd4`  |
| 1355   | No file  | `59de010f8dd4`  |
| 1351   | No file  | `59de010f8dd4`  |
| 1348   | No file  | `59de010f8dd4`  |
| 1346   | No file  | `59de010f8dd4`  |
| 1341   | No file  | `59de010f8dd4`  |
| 1340   | No file  | `59de010f8dd4`  |
| 1338   | No file  | `59de010f8dd4`  |
| 1335   | No file  | `59de010f8dd4`  |
| 1333   | No file  | `59de010f8dd4`  |
| 1329   | No file  | `59de010f8dd4`  |
| 1327   | No file  | `59de010f8dd4`  |
| 1324   | No file  | `59de010f8dd4`  |
| 1321   | No file  | `59de010f8dd4`  |
| 1319   | No file  | `59de010f8dd4`  |
| 1318   | No file  | `59de010f8dd4`  |
| 1316   | No file  | `59de010f8dd4`  |
| 1313   | No file  | `59de010f8dd4`  |
| 1311   | No file  | `59de010f8dd4`  |
| 1309   | No file  | `59de010f8dd4`  |
| 1304   | No file  | `59de010f8dd4`  |
| 1292   | No file  | `59de010f8dd4`  |
| 1286   | No file  | `59de010f8dd4`  |
| 1280   | No file  | `59de010f8dd4`  |
| 1276   | No file  | `59de010f8dd4`  |
| 1267   | No file  | `59de010f8dd4`  |
| 1261   | No file  | `59de010f8dd4`  |
| 1256   | No file  | `59de010f8dd4`  |
| 1250   | No file  | `59de010f8dd4`  |
| 1246   | No file  | `59de010f8dd4`  |
| 1239   | No file  | `59de010f8dd4`  |
| 1230   | No file  | `59de010f8dd4`  |
| 1226   | No file  | `59de010f8dd4`  |
| 1220   | No file  | `59de010f8dd4`  |
| 1217   | No file  | `59de010f8dd4`  |
| 1211   | No file  | `59de010f8dd4`  |
| 1210   | No file  | `59de010f8dd4`  |
| 1208   | No file  | `59de010f8dd4`  |
| 1203   | No file  | `59de010f8dd4`  |
| 1197   | No file  | `59de010f8dd4`  |
| 1194   | No file  | `59de010f8dd4`  |
| 1192   | No file  | `59de010f8dd4`  |
| 1187   | No file  | `59de010f8dd4`  |
| 1183   | No file  | `59de010f8dd4`  |
| 1177   | No file  | `59de010f8dd4`  |
| 1173   | No file  | `59de010f8dd4`  |
| 1167   | No file  | `59de010f8dd4`  |
| 1164   | No file  | `59de010f8dd4`  |
| 1156   | No file  | `59de010f8dd4`  |
| 1149   | No file  | `59de010f8dd4`  |
| 1144   | No file  | `59de010f8dd4`  |
| 1137   | No file  | `59de010f8dd4`  |
| 1132   | No file  | `59de010f8dd4`  |
| 1127   | No file  | `59de010f8dd4`  |
| 1122   | No file  | `59de010f8dd4`  |
| 1118   | No file  | `59de010f8dd4`  |
| 1114   | No file  | `59de010f8dd4`  |
| 1109   | No file  | `59de010f8dd4`  |
| 1102   | No file  | `59de010f8dd4`  |
| 1096   | No file  | `59de010f8dd4`  |
| 1088   | No file  | `59de010f8dd4`  |
| 1081   | No file  | `59de010f8dd4`  |
| 1076   | No file  | `59de010f8dd4`  |
| 1069   | No file  | `59de010f8dd4`  |
| 1064   | No file  | `59de010f8dd4`  |
| 1058   | No file  | `59de010f8dd4`  |
| 1051   | No file  | `59de010f8dd4`  |
| 1044   | No file  | `59de010f8dd4`  |
| 1036   | No file  | `59de010f8dd4`  |
| 1026   | No file  | `59de010f8dd4`  |
| 1016   | No file  | `59de010f8dd4`  |
| 1009   | No file  | `59de010f8dd4`  |
| 1005   | No file  | `59de010f8dd4`  |
| 1000   | No file  | `59de010f8dd4`  |
| 998    | No file  | `59de010f8dd4`  |
| 990    | No file  | `59de010f8dd4`  |
| 979    | No file  | `59de010f8dd4`  |
| 972    | No file  | `59de010f8dd4`  |
| 963    | No file  | `59de010f8dd4`  |
| 955    | No file  | `59de010f8dd4`  |
| 946    | No file  | `59de010f8dd4`  |
| 938    | No file  | `59de010f8dd4`  |
| 927    | No file  | `59de010f8dd4`  |
| 911    | No file  | `59de010f8dd4`  |
| 904    | No file  | `59de010f8dd4`  |
| 899    | No file  | `59de010f8dd4`  |
| 894    | No file  | `59de010f8dd4`  |
| 885    | No file  | `59de010f8dd4`  |
| 879    | No file  | `59de010f8dd4`  |
| 872    | No file  | `59de010f8dd4`  |
| 864    | No file  | `59de010f8dd4`  |
| 855    | No file  | `59de010f8dd4`  |
| 853    | No file  | `59de010f8dd4`  |
| 845    | No file  | `59de010f8dd4`  |
| 837    | No file  | `59de010f8dd4`  |
| 829    | No file  | `59de010f8dd4`  |
| 822    | No file  | `59de010f8dd4`  |
| 814    | No file  | `59de010f8dd4`  |
| 805    | No file  | `59de010f8dd4`  |
| 794    | No file  | `59de010f8dd4`  |
| 787    | No file  | `59de010f8dd4`  |
| 780    | No file  | `59de010f8dd4`  |
| 771    | No file  | `59de010f8dd4`  |
| 760    | No file  | `59de010f8dd4`  |
| 748    | No file  | `59de010f8dd4`  |
| 741    | No file  | `59de010f8dd4`  |
| 736    | No file  | `59de010f8dd4`  |
| 731    | No file  | `59de010f8dd4`  |
| 723    | No file  | `59de010f8dd4`  |
| 711    | No file  | `59de010f8dd4`  |
| 707    | No file  | `59de010f8dd4`  |
| 697    | No file  | `59de010f8dd4`  |
| 689    | No file  | `59de010f8dd4`  |
| 683    | No file  | `59de010f8dd4`  |
| 678    | No file  | `59de010f8dd4`  |
| 670    | No file  | `59de010f8dd4`  |
| 661    | No file  | `59de010f8dd4`  |
| 656    | No file  | `59de010f8dd4`  |
| 652    | No file  | `59de010f8dd4`  |
| 643    | No file  | `59de010f8dd4`  |
| 637    | No file  | `59de010f8dd4`  |
| 630    | No file  | `59de010f8dd4`  |
| 627    | No file  | `59de010f8dd4`  |
| 621    | No file  | `59de010f8dd4`  |
| 617    | No file  | `59de010f8dd4`  |
| 615    | No file  | `59de010f8dd4`  |
| 606    | No file  | `59de010f8dd4`  |
| 599    | No file  | `59de010f8dd4`  |
| 592    | No file  | `59de010f8dd4`  |
| 586    | No file  | `59de010f8dd4`  |
| 577    | No file  | `59de010f8dd4`  |
| 569    | No file  | `59de010f8dd4`  |
| 561    | No file  | `59de010f8dd4`  |
| 554    | No file  | `59de010f8dd4`  |
| 542    | No file  | `59de010f8dd4`  |
| 532    | No file  | `59de010f8dd4`  |
| 531    | No file  | `59de010f8dd4`  |
| 526    | No file  | `59de010f8dd4`  |
| 521    | No file  | `59de010f8dd4`  |
| 517    | No file  | `59de010f8dd4`  |
| 510    | No file  | `59de010f8dd4`  |
| 508    | No file  | `59de010f8dd4`  |
| 504    | No file  | `59de010f8dd4`  |
| 497    | No file  | `59de010f8dd4`  |
| 491    | No file  | `59de010f8dd4`  |
| 485    | No file  | `59de010f8dd4`  |
| 478    | No file  | `59de010f8dd4`  |
| 472    | No file  | `59de010f8dd4`  |
| 466    | No file  | `59de010f8dd4`  |
| 457    | No file  | `59de010f8dd4`  |
| 452    | No file  | `59de010f8dd4`  |
| 449    | No file  | `59de010f8dd4`  |
| 435    | No file  | `59de010f8dd4`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                             |
| --------------------- | -------- | ---------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 at `str_id1=quest_chain_id`, `str_id2=quest_id` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                          |
| ------------------- | ------------ | ------------------ | ---------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                   |
| `+0x04`             | u32          | count              | Number of groups                               |
| `+0x08`             | Group[count] | groups             | Variable-size groups, back to back; see Group  |
| `groups+0x00`       | String Table | string_table       | See String Table                               |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the groups end |
| `string_table+0x04` | u32          | zero               | Always `0`                                     |

The string table has the shape `itemequipgroup.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Walking `count` groups ends exactly at `string_table_start`.

### Group (variable: 12 bytes + quests)

| Offset  | Type             | Field            | Notes                                                                  |
| ------- | ---------------- | ---------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32              | group_key        | Unique; the argument of `alreadyclearspecialquest`                     |
| `+0x04` | u64              | quest_count      | Number of quests; `0` on groups 11 and 24 (client 3474)                |
| `+0x0C` | u32[quest_count] | packed_quest_ids | `(quest_id << 16) \| quest_chain_id`, a `quest.dbss` `packed_quest_id` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No group reads a string                        |

## Script Use

`alreadyclearspecialquest(group)` sits alone in the `action_script` of the quests that call it, except for quest 50032 / 1, which adds `clearQuest(50031,1)`. No `condition_script`, no `detail_dialog.dbss` script and no client Lua file (`luacscript/`) names the call or the file; `specialQuestInfo` in `panel_window_achievement.luac` is a local holding an Adventure Log page quest. On client 3474, 37 `quest.dbss` quests call it with 29 of the 36 group keys; groups 11, 12, 14, 19, 24, 34 and 36 have no caller.

Callers and groups on client 3474, grouped by what the group lists:

| Group Keys | Group Lists                                                          | Called By                                                                                   |
| ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 2, 3, 20, 21, 31 | `[Pet]` quests of chain 21416, one pet each                    | 4464 / 11 to 15, `[Suggested] Complete [Pet] ...` for the same pet                           |
| 4          | Awakening, succession or ascension quests, one per class (32)        | 4464 / 18; 50032 / 1, 50129 / 1 and 50150 to 50152 `A Whole New Me`                         |
| 7, 8       | `Old Moon's Resplendent` armor (chains 41005 to 41008) and weapon (41009 to 41011) quests | 4471 / 12 and 4471 / 3, the boss gear exchange quests                   |
| 26 to 30   | The Calamity 1 to 5 boss quests of chains 897 to 901                 | 897 / 10 to 901 / 10, `Calamity N Boss - Footsteps of Conquest`                              |
| 18         | Pages 1 to 3 of Igor Bartali's Adventures Vol. I (chain 748)         | 4464 / 17, `[Adventure Log] Complete Igor Bartali's Adventures Vol. I`                       |

## Field Names

The `Quest_Special_Group` sheet of a private server's `DataSheets.bexcel` on client 1784 has two compiled columns: `Group_Index` (`group_key`) and `QuestNoList` (`packed_quest_ids`, as `(chain,quest);` pairs). It matches the client 1784 file in all 17 groups, quest for quest and in order. A `#참조` note column (not compiled) names each group after its quest; group 2 is `로렌의 토실이` (Lauren's Fluffy), the pet of the quests it lists and of its caller 4464 / 12. The server executable of that private server names the record type `SpecialQuestInfoStaticStatus`, its manager `SpecialQuestInfoStaticStatusManager` and the script function `AlreadyClearSpecialQuest`. The 2016 PDB has no `SpecialQuest` symbol.

On client 3474, 10 of the 17 shared groups still match the sheet. Groups 1 and 4 append quests and group 10 adds quest 41013 / 1 in front. Groups 2 and 16 drop quest 21416 / 23 and add other `[Pet]` quests of chain 21416. Group 11 is empty, and group 14 lists quest 40022 / 5 in place of the three quests of chain 21119. Groups 18 to 36 are newer than the sheet.

## Notes

- On client 3474 the file is `1,560` bytes: 36 groups with keys 1 to 36 in key order, 277 quest entries, 237 distinct. No group lists a quest twice; groups 23 and 25 list the same two quests, and groups 16 and 34 differ only by quest 40022 / 12 at the end of group 34.
- Every packed quest ID is a `quest.dbss` record on client 3474. 65 of the 277 entries (60 distinct quests) are Adventure Log pages of `specialquestlist.bss` (`quest_category` 11), in groups 18, 19, 26 to 30 and 32.
- Client 1784 has the same layout: `852` bytes, 17 groups with keys 1 to 17 and 157 quest entries.

## Open Questions

### Any or Every Quest of the Group

The call name says the player has already cleared a special quest, but nothing in the data says whether one quest of the group is enough or every quest is needed. Group 4 lists one awakening, succession or ascension quest per class, and a character clears only its own class's, so it points to one quest being enough; groups 26 to 30 list the ten bosses of one Calamity level, where every quest reads just as well.
