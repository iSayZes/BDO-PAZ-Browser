# `regionmonsterkillquestlist.bss` Format

## Purpose

Quest list of the region monster kill quests: zone subjugation quests (`Magaia Subjugation I`, `[Subjugation] Pluck Those Manshaum Fangs`), weekly loot quests (`[Weekly] Looting Garmoth I`) and the `[Season]` hunting quests. On client 3474 the list holds exactly the 180 `quest.dbss` records with `quest_category` 12, in `quest.dbss` record order.

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, where the trailer starts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes | Records   | Row bytes |
| ------ | -------------- | -------------------------------- | ----- | --------- | --------- |
| 1      | 1064 and later | `regionmonsterkillquestlist.bss` | 740   | 180 Entry | 4         |

| Layout | File                             | Known          | Unknown    |
| ------ | -------------------------------- | -------------- | ---------- |
| 1      | `regionmonsterkillquestlist.bss` | 740 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `62325168d5d3`  |
| 3482   | Layout 1 | `62325168d5d3`  |
| 3474   | Layout 1 | `62325168d5d3`  |
| 3473   | Layout 1 | `62325168d5d3`  |
| 3464   | Layout 1 | `62325168d5d3`  |
| 3458   | Layout 1 | `62325168d5d3`  |
| 3454   | Layout 1 | `62325168d5d3`  |
| 3444   | Layout 1 | `62325168d5d3`  |
| 3435   | Layout 1 | `62325168d5d3`  |
| 3426   | Layout 1 | `62325168d5d3`  |
| 3418   | Layout 1 | `62325168d5d3`  |
| 3412   | Layout 1 | `62325168d5d3`  |
| 3402   | Layout 1 | `62325168d5d3`  |
| 3396   | Layout 1 | `62325168d5d3`  |
| 3387   | Layout 1 | `62325168d5d3`  |
| 3381   | Layout 1 | `62325168d5d3`  |
| 3373   | Layout 1 | `62325168d5d3`  |
| 3364   | Layout 1 | `62325168d5d3`  |
| 3356   | Layout 1 | `62325168d5d3`  |
| 3349   | Layout 1 | `62325168d5d3`  |
| 3342   | Layout 1 | `62325168d5d3`  |
| 3335   | Layout 1 | `62325168d5d3`  |
| 3326   | Layout 1 | `62325168d5d3`  |
| 3321   | Layout 1 | `62325168d5d3`  |
| 3314   | Layout 1 | `62325168d5d3`  |
| 3303   | Layout 1 | `62325168d5d3`  |
| 3302   | Layout 1 | `62325168d5d3`  |
| 3293   | Layout 1 | `62325168d5d3`  |
| 3283   | Layout 1 | `62325168d5d3`  |
| 3275   | Layout 1 | `62325168d5d3`  |
| 3267   | Layout 1 | `62325168d5d3`  |
| 3258   | Layout 1 | `62325168d5d3`  |
| 3251   | Layout 1 | `62325168d5d3`  |
| 3242   | Layout 1 | `62325168d5d3`  |
| 3235   | Layout 1 | `62325168d5d3`  |
| 3229   | Layout 1 | `62325168d5d3`  |
| 3212   | Layout 1 | `62325168d5d3`  |
| 3203   | Layout 1 | `62325168d5d3`  |
| 3193   | Layout 1 | `62325168d5d3`  |
| 3186   | Layout 1 | `62325168d5d3`  |
| 3177   | Layout 1 | `62325168d5d3`  |
| 3169   | Layout 1 | `62325168d5d3`  |
| 3158   | Layout 1 | `62325168d5d3`  |
| 3151   | Layout 1 | `62325168d5d3`  |
| 3144   | Layout 1 | `62325168d5d3`  |
| 3133   | Layout 1 | `62325168d5d3`  |
| 3125   | Layout 1 | `62325168d5d3`  |
| 3118   | Layout 1 | `62325168d5d3`  |
| 3111   | Layout 1 | `62325168d5d3`  |
| 3103   | Layout 1 | `62325168d5d3`  |
| 3095   | Layout 1 | `62325168d5d3`  |
| 3086   | Layout 1 | `62325168d5d3`  |
| 3072   | Layout 1 | `62325168d5d3`  |
| 3062   | Layout 1 | `62325168d5d3`  |
| 3052   | Layout 1 | `62325168d5d3`  |
| 3045   | Layout 1 | `62325168d5d3`  |
| 3037   | Layout 1 | `62325168d5d3`  |
| 3030   | Layout 1 | `62325168d5d3`  |
| 3021   | Layout 1 | `62325168d5d3`  |
| 3012   | Layout 1 | `62325168d5d3`  |
| 3002   | Layout 1 | `62325168d5d3`  |
| 2995   | Layout 1 | `62325168d5d3`  |
| 2987   | Layout 1 | `62325168d5d3`  |
| 2978   | Layout 1 | `62325168d5d3`  |
| 2970   | Layout 1 | `62325168d5d3`  |
| 2959   | Layout 1 | `62325168d5d3`  |
| 2951   | Layout 1 | `62325168d5d3`  |
| 2942   | Layout 1 | `62325168d5d3`  |
| 2935   | Layout 1 | `62325168d5d3`  |
| 2932   | Layout 1 | `62325168d5d3`  |
| 2923   | Layout 1 | `62325168d5d3`  |
| 2919   | Layout 1 | `62325168d5d3`  |
| 2907   | Layout 1 | `62325168d5d3`  |
| 2900   | Layout 1 | `62325168d5d3`  |
| 2891   | Layout 1 | `62325168d5d3`  |
| 2882   | Layout 1 | `62325168d5d3`  |
| 2872   | Layout 1 | `62325168d5d3`  |
| 2863   | Layout 1 | `62325168d5d3`  |
| 2855   | Layout 1 | `62325168d5d3`  |
| 2849   | Layout 1 | `62325168d5d3`  |
| 2844   | Layout 1 | `62325168d5d3`  |
| 2834   | Layout 1 | `62325168d5d3`  |
| 2825   | Layout 1 | `62325168d5d3`  |
| 2819   | Layout 1 | `62325168d5d3`  |
| 2811   | Layout 1 | `62325168d5d3`  |
| 2803   | Layout 1 | `62325168d5d3`  |
| 2794   | Layout 1 | `62325168d5d3`  |
| 2783   | Layout 1 | `62325168d5d3`  |
| 2774   | Layout 1 | `62325168d5d3`  |
| 2765   | Layout 1 | `62325168d5d3`  |
| 2756   | Layout 1 | `62325168d5d3`  |
| 2750   | Layout 1 | `62325168d5d3`  |
| 2743   | Layout 1 | `62325168d5d3`  |
| 2736   | Layout 1 | `62325168d5d3`  |
| 2726   | Layout 1 | `62325168d5d3`  |
| 2717   | Layout 1 | `62325168d5d3`  |
| 2709   | Layout 1 | `62325168d5d3`  |
| 2703   | Layout 1 | `62325168d5d3`  |
| 2695   | Layout 1 | `62325168d5d3`  |
| 2684   | Layout 1 | `62325168d5d3`  |
| 2672   | Layout 1 | `62325168d5d3`  |
| 2665   | Layout 1 | `62325168d5d3`  |
| 2657   | Layout 1 | `62325168d5d3`  |
| 2649   | Layout 1 | `62325168d5d3`  |
| 2644   | Layout 1 | `62325168d5d3`  |
| 2637   | Layout 1 | `62325168d5d3`  |
| 2629   | Layout 1 | `62325168d5d3`  |
| 2619   | Layout 1 | `62325168d5d3`  |
| 2612   | Layout 1 | `62325168d5d3`  |
| 2606   | Layout 1 | `62325168d5d3`  |
| 2602   | Layout 1 | `62325168d5d3`  |
| 2601   | Layout 1 | `62325168d5d3`  |
| 2592   | Layout 1 | `62325168d5d3`  |
| 2583   | Layout 1 | `62325168d5d3`  |
| 2575   | Layout 1 | `62325168d5d3`  |
| 2567   | Layout 1 | `62325168d5d3`  |
| 2560   | Layout 1 | `62325168d5d3`  |
| 2553   | Layout 1 | `62325168d5d3`  |
| 2545   | Layout 1 | `62325168d5d3`  |
| 2538   | Layout 1 | `62325168d5d3`  |
| 2529   | Layout 1 | `62325168d5d3`  |
| 2519   | Layout 1 | `62325168d5d3`  |
| 2513   | Layout 1 | `62325168d5d3`  |
| 2510   | Layout 1 | `62325168d5d3`  |
| 2507   | Layout 1 | `62325168d5d3`  |
| 2503   | Layout 1 | `62325168d5d3`  |
| 2498   | Layout 1 | `62325168d5d3`  |
| 2492   | Layout 1 | `62325168d5d3`  |
| 2487   | Layout 1 | `62325168d5d3`  |
| 2480   | Layout 1 | `62325168d5d3`  |
| 2474   | Layout 1 | `62325168d5d3`  |
| 2468   | Layout 1 | `62325168d5d3`  |
| 2460   | Layout 1 | `62325168d5d3`  |
| 2453   | Layout 1 | `62325168d5d3`  |
| 2444   | Layout 1 | `62325168d5d3`  |
| 2438   | Layout 1 | `62325168d5d3`  |
| 2434   | Layout 1 | `62325168d5d3`  |
| 2429   | Layout 1 | `62325168d5d3`  |
| 2421   | Layout 1 | `62325168d5d3`  |
| 2414   | Layout 1 | `62325168d5d3`  |
| 2407   | Layout 1 | `62325168d5d3`  |
| 2401   | Layout 1 | `62325168d5d3`  |
| 2397   | Layout 1 | `62325168d5d3`  |
| 2393   | Layout 1 | `62325168d5d3`  |
| 2384   | Layout 1 | `62325168d5d3`  |
| 2378   | Layout 1 | `62325168d5d3`  |
| 2372   | Layout 1 | `62325168d5d3`  |
| 2358   | Layout 1 | `62325168d5d3`  |
| 2352   | Layout 1 | `62325168d5d3`  |
| 2347   | Layout 1 | `62325168d5d3`  |
| 2343   | Layout 1 | `62325168d5d3`  |
| 2335   | Layout 1 | `62325168d5d3`  |
| 2327   | Layout 1 | `62325168d5d3`  |
| 2324   | Layout 1 | `62325168d5d3`  |
| 2319   | Layout 1 | `62325168d5d3`  |
| 2313   | Layout 1 | `62325168d5d3`  |
| 2308   | Layout 1 | `62325168d5d3`  |
| 2302   | Layout 1 | `62325168d5d3`  |
| 2295   | Layout 1 | `62325168d5d3`  |
| 2290   | Layout 1 | `62325168d5d3`  |
| 2284   | Layout 1 | `62325168d5d3`  |
| 2276   | Layout 1 | `62325168d5d3`  |
| 2269   | Layout 1 | `62325168d5d3`  |
| 2259   | Layout 1 | `62325168d5d3`  |
| 2250   | Layout 1 | `62325168d5d3`  |
| 2243   | Layout 1 | `62325168d5d3`  |
| 2235   | Layout 1 | `62325168d5d3`  |
| 2229   | Layout 1 | `62325168d5d3`  |
| 2224   | Layout 1 | `62325168d5d3`  |
| 2218   | Layout 1 | `62325168d5d3`  |
| 2215   | Layout 1 | `62325168d5d3`  |
| 2207   | Layout 1 | `62325168d5d3`  |
| 2203   | Layout 1 | `62325168d5d3`  |
| 2196   | Layout 1 | `62325168d5d3`  |
| 2192   | Layout 1 | `62325168d5d3`  |
| 2189   | Layout 1 | `62325168d5d3`  |
| 2183   | Layout 1 | `62325168d5d3`  |
| 2179   | Layout 1 | `62325168d5d3`  |
| 2171   | Layout 1 | `62325168d5d3`  |
| 2163   | Layout 1 | `62325168d5d3`  |
| 2156   | Layout 1 | `62325168d5d3`  |
| 2151   | Layout 1 | `62325168d5d3`  |
| 2147   | Layout 1 | `62325168d5d3`  |
| 2142   | Layout 1 | `62325168d5d3`  |
| 2138   | Layout 1 | `62325168d5d3`  |
| 2134   | Layout 1 | `62325168d5d3`  |
| 2130   | Layout 1 | `62325168d5d3`  |
| 2122   | Layout 1 | `62325168d5d3`  |
| 2107   | Layout 1 | `62325168d5d3`  |
| 2098   | Layout 1 | `62325168d5d3`  |
| 2089   | Layout 1 | `62325168d5d3`  |
| 2081   | Layout 1 | `62325168d5d3`  |
| 2073   | Layout 1 | `62325168d5d3`  |
| 2067   | Layout 1 | `62325168d5d3`  |
| 2063   | Layout 1 | `62325168d5d3`  |
| 2059   | Layout 1 | `62325168d5d3`  |
| 2052   | Layout 1 | `62325168d5d3`  |
| 2044   | Layout 1 | `62325168d5d3`  |
| 2039   | Layout 1 | `62325168d5d3`  |
| 2032   | Layout 1 | `62325168d5d3`  |
| 2025   | Layout 1 | `62325168d5d3`  |
| 2011   | Layout 1 | `62325168d5d3`  |
| 2005   | Layout 1 | `62325168d5d3`  |
| 2000   | Layout 1 | `62325168d5d3`  |
| 1996   | Layout 1 | `62325168d5d3`  |
| 1991   | Layout 1 | `62325168d5d3`  |
| 1985   | Layout 1 | `62325168d5d3`  |
| 1980   | Layout 1 | `62325168d5d3`  |
| 1969   | Layout 1 | `62325168d5d3`  |
| 1964   | Layout 1 | `62325168d5d3`  |
| 1958   | Layout 1 | `62325168d5d3`  |
| 1950   | Layout 1 | `62325168d5d3`  |
| 1945   | Layout 1 | `62325168d5d3`  |
| 1937   | Layout 1 | `62325168d5d3`  |
| 1933   | Layout 1 | `62325168d5d3`  |
| 1927   | Layout 1 | `62325168d5d3`  |
| 1921   | Layout 1 | `62325168d5d3`  |
| 1914   | Layout 1 | `62325168d5d3`  |
| 1908   | Layout 1 | `62325168d5d3`  |
| 1897   | Layout 1 | `62325168d5d3`  |
| 1892   | Layout 1 | `62325168d5d3`  |
| 1886   | Layout 1 | `62325168d5d3`  |
| 1881   | Layout 1 | `62325168d5d3`  |
| 1871   | Layout 1 | `62325168d5d3`  |
| 1866   | Layout 1 | `62325168d5d3`  |
| 1862   | Layout 1 | `62325168d5d3`  |
| 1854   | Layout 1 | `62325168d5d3`  |
| 1846   | Layout 1 | `62325168d5d3`  |
| 1838   | Layout 1 | `62325168d5d3`  |
| 1832   | Layout 1 | `62325168d5d3`  |
| 1826   | Layout 1 | `62325168d5d3`  |
| 1822   | Layout 1 | `62325168d5d3`  |
| 1818   | Layout 1 | `62325168d5d3`  |
| 1804   | Layout 1 | `62325168d5d3`  |
| 1794   | Layout 1 | `62325168d5d3`  |
| 1790   | Layout 1 | `62325168d5d3`  |
| 1784   | Layout 1 | `62325168d5d3`  |
| 1774   | Layout 1 | `62325168d5d3`  |
| 1771   | Layout 1 | `62325168d5d3`  |
| 1762   | Layout 1 | `62325168d5d3`  |
| 1759   | Layout 1 | `62325168d5d3`  |
| 1754   | Layout 1 | `62325168d5d3`  |
| 1749   | Layout 1 | `62325168d5d3`  |
| 1743   | Layout 1 | `62325168d5d3`  |
| 1737   | Layout 1 | `62325168d5d3`  |
| 1731   | Layout 1 | `62325168d5d3`  |
| 1725   | Layout 1 | `62325168d5d3`  |
| 1717   | Layout 1 | `62325168d5d3`  |
| 1710   | Layout 1 | `62325168d5d3`  |
| 1704   | Layout 1 | `62325168d5d3`  |
| 1698   | Layout 1 | `62325168d5d3`  |
| 1690   | Layout 1 | `62325168d5d3`  |
| 1685   | Layout 1 | `62325168d5d3`  |
| 1680   | Layout 1 | `62325168d5d3`  |
| 1674   | Layout 1 | `62325168d5d3`  |
| 1668   | Layout 1 | `62325168d5d3`  |
| 1659   | Layout 1 | `62325168d5d3`  |
| 1649   | Layout 1 | `62325168d5d3`  |
| 1642   | Layout 1 | `62325168d5d3`  |
| 1636   | Layout 1 | `62325168d5d3`  |
| 1628   | Layout 1 | `62325168d5d3`  |
| 1622   | Layout 1 | `62325168d5d3`  |
| 1614   | Layout 1 | `62325168d5d3`  |
| 1608   | Layout 1 | `62325168d5d3`  |
| 1602   | Layout 1 | `62325168d5d3`  |
| 1598   | Layout 1 | `62325168d5d3`  |
| 1594   | Layout 1 | `62325168d5d3`  |
| 1590   | Layout 1 | `62325168d5d3`  |
| 1587   | Layout 1 | `62325168d5d3`  |
| 1584   | Layout 1 | `62325168d5d3`  |
| 1579   | Layout 1 | `62325168d5d3`  |
| 1572   | Layout 1 | `62325168d5d3`  |
| 1565   | Layout 1 | `62325168d5d3`  |
| 1559   | Layout 1 | `62325168d5d3`  |
| 1554   | Layout 1 | `62325168d5d3`  |
| 1547   | Layout 1 | `62325168d5d3`  |
| 1537   | Layout 1 | `62325168d5d3`  |
| 1529   | Layout 1 | `62325168d5d3`  |
| 1524   | Layout 1 | `62325168d5d3`  |
| 1519   | Layout 1 | `62325168d5d3`  |
| 1509   | Layout 1 | `62325168d5d3`  |
| 1506   | Layout 1 | `62325168d5d3`  |
| 1504   | Layout 1 | `62325168d5d3`  |
| 1500   | Layout 1 | `62325168d5d3`  |
| 1493   | Layout 1 | `62325168d5d3`  |
| 1489   | Layout 1 | `62325168d5d3`  |
| 1485   | Layout 1 | `62325168d5d3`  |
| 1481   | Layout 1 | `62325168d5d3`  |
| 1474   | Layout 1 | `62325168d5d3`  |
| 1466   | Layout 1 | `62325168d5d3`  |
| 1462   | Layout 1 | `62325168d5d3`  |
| 1459   | Layout 1 | `62325168d5d3`  |
| 1453   | Layout 1 | `62325168d5d3`  |
| 1450   | Layout 1 | `62325168d5d3`  |
| 1445   | Layout 1 | `62325168d5d3`  |
| 1439   | Layout 1 | `62325168d5d3`  |
| 1433   | Layout 1 | `62325168d5d3`  |
| 1430   | Layout 1 | `62325168d5d3`  |
| 1426   | Layout 1 | `62325168d5d3`  |
| 1421   | Layout 1 | `62325168d5d3`  |
| 1417   | Layout 1 | `62325168d5d3`  |
| 1416   | Layout 1 | `62325168d5d3`  |
| 1409   | Layout 1 | `62325168d5d3`  |
| 1405   | Layout 1 | `62325168d5d3`  |
| 1401   | Layout 1 | `62325168d5d3`  |
| 1396   | Layout 1 | `62325168d5d3`  |
| 1391   | Layout 1 | `62325168d5d3`  |
| 1390   | Layout 1 | `62325168d5d3`  |
| 1386   | Layout 1 | `62325168d5d3`  |
| 1381   | Layout 1 | `62325168d5d3`  |
| 1379   | Layout 1 | `62325168d5d3`  |
| 1372   | Layout 1 | `62325168d5d3`  |
| 1366   | Layout 1 | `62325168d5d3`  |
| 1364   | Layout 1 | `62325168d5d3`  |
| 1363   | Layout 1 | `62325168d5d3`  |
| 1360   | Layout 1 | `62325168d5d3`  |
| 1358   | Layout 1 | `62325168d5d3`  |
| 1355   | Layout 1 | `62325168d5d3`  |
| 1351   | Layout 1 | `62325168d5d3`  |
| 1348   | Layout 1 | `62325168d5d3`  |
| 1346   | Layout 1 | `62325168d5d3`  |
| 1341   | Layout 1 | `62325168d5d3`  |
| 1340   | Layout 1 | `62325168d5d3`  |
| 1338   | Layout 1 | `62325168d5d3`  |
| 1335   | Layout 1 | `62325168d5d3`  |
| 1333   | Layout 1 | `62325168d5d3`  |
| 1329   | Layout 1 | `62325168d5d3`  |
| 1327   | Layout 1 | `62325168d5d3`  |
| 1324   | Layout 1 | `62325168d5d3`  |
| 1321   | Layout 1 | `62325168d5d3`  |
| 1319   | Layout 1 | `62325168d5d3`  |
| 1318   | Layout 1 | `62325168d5d3`  |
| 1316   | Layout 1 | `62325168d5d3`  |
| 1313   | Layout 1 | `62325168d5d3`  |
| 1311   | Layout 1 | `62325168d5d3`  |
| 1309   | Layout 1 | `62325168d5d3`  |
| 1304   | Layout 1 | `62325168d5d3`  |
| 1292   | Layout 1 | `62325168d5d3`  |
| 1286   | Layout 1 | `62325168d5d3`  |
| 1280   | Layout 1 | `62325168d5d3`  |
| 1276   | Layout 1 | `62325168d5d3`  |
| 1267   | Layout 1 | `62325168d5d3`  |
| 1261   | Layout 1 | `62325168d5d3`  |
| 1256   | Layout 1 | `62325168d5d3`  |
| 1250   | Layout 1 | `62325168d5d3`  |
| 1246   | Layout 1 | `62325168d5d3`  |
| 1239   | Layout 1 | `62325168d5d3`  |
| 1230   | Layout 1 | `62325168d5d3`  |
| 1226   | Layout 1 | `62325168d5d3`  |
| 1220   | Layout 1 | `62325168d5d3`  |
| 1217   | Layout 1 | `62325168d5d3`  |
| 1211   | Layout 1 | `62325168d5d3`  |
| 1210   | Layout 1 | `62325168d5d3`  |
| 1208   | Layout 1 | `62325168d5d3`  |
| 1203   | Layout 1 | `62325168d5d3`  |
| 1197   | Layout 1 | `62325168d5d3`  |
| 1194   | Layout 1 | `62325168d5d3`  |
| 1192   | Layout 1 | `62325168d5d3`  |
| 1187   | Layout 1 | `62325168d5d3`  |
| 1183   | Layout 1 | `62325168d5d3`  |
| 1177   | Layout 1 | `62325168d5d3`  |
| 1173   | Layout 1 | `62325168d5d3`  |
| 1167   | Layout 1 | `62325168d5d3`  |
| 1164   | Layout 1 | `62325168d5d3`  |
| 1156   | Layout 1 | `62325168d5d3`  |
| 1149   | Layout 1 | `62325168d5d3`  |
| 1144   | Layout 1 | `62325168d5d3`  |
| 1137   | Layout 1 | `62325168d5d3`  |
| 1132   | Layout 1 | `62325168d5d3`  |
| 1127   | Layout 1 | `62325168d5d3`  |
| 1122   | Layout 1 | `62325168d5d3`  |
| 1118   | Layout 1 | `62325168d5d3`  |
| 1114   | Layout 1 | `62325168d5d3`  |
| 1109   | Layout 1 | `62325168d5d3`  |
| 1102   | Layout 1 | `62325168d5d3`  |
| 1096   | Layout 1 | `62325168d5d3`  |
| 1088   | Layout 1 | `62325168d5d3`  |
| 1081   | Layout 1 | `62325168d5d3`  |
| 1076   | Layout 1 | `62325168d5d3`  |
| 1069   | Layout 1 | `62325168d5d3`  |
| 1064   | Layout 1 | `62325168d5d3`  |
| 1058   | No file  | `62325168d5d3`  |
| 1051   | No file  | `62325168d5d3`  |
| 1044   | No file  | `62325168d5d3`  |
| 1036   | No file  | `62325168d5d3`  |
| 1026   | No file  | `62325168d5d3`  |
| 1016   | No file  | `62325168d5d3`  |
| 1009   | No file  | `62325168d5d3`  |
| 1005   | No file  | `62325168d5d3`  |
| 1000   | No file  | `62325168d5d3`  |
| 998    | No file  | `62325168d5d3`  |
| 990    | No file  | `62325168d5d3`  |
| 979    | No file  | `62325168d5d3`  |
| 972    | No file  | `62325168d5d3`  |
| 963    | No file  | `62325168d5d3`  |
| 955    | No file  | `62325168d5d3`  |
| 946    | No file  | `62325168d5d3`  |
| 938    | No file  | `62325168d5d3`  |
| 927    | No file  | `62325168d5d3`  |
| 911    | No file  | `62325168d5d3`  |
| 904    | No file  | `62325168d5d3`  |
| 899    | No file  | `62325168d5d3`  |
| 894    | No file  | `62325168d5d3`  |
| 885    | No file  | `62325168d5d3`  |
| 879    | No file  | `62325168d5d3`  |
| 872    | No file  | `62325168d5d3`  |
| 864    | No file  | `62325168d5d3`  |
| 855    | No file  | `62325168d5d3`  |
| 853    | No file  | `62325168d5d3`  |
| 845    | No file  | `62325168d5d3`  |
| 837    | No file  | `62325168d5d3`  |
| 829    | No file  | `62325168d5d3`  |
| 822    | No file  | `62325168d5d3`  |
| 814    | No file  | `62325168d5d3`  |
| 805    | No file  | `62325168d5d3`  |
| 794    | No file  | `62325168d5d3`  |
| 787    | No file  | `62325168d5d3`  |
| 780    | No file  | `62325168d5d3`  |
| 771    | No file  | `62325168d5d3`  |
| 760    | No file  | `62325168d5d3`  |
| 748    | No file  | `62325168d5d3`  |
| 741    | No file  | `62325168d5d3`  |
| 736    | No file  | `62325168d5d3`  |
| 731    | No file  | `62325168d5d3`  |
| 723    | No file  | `62325168d5d3`  |
| 711    | No file  | `62325168d5d3`  |
| 707    | No file  | `62325168d5d3`  |
| 697    | No file  | `62325168d5d3`  |
| 689    | No file  | `62325168d5d3`  |
| 683    | No file  | `62325168d5d3`  |
| 678    | No file  | `62325168d5d3`  |
| 670    | No file  | `62325168d5d3`  |
| 661    | No file  | `62325168d5d3`  |
| 656    | No file  | `62325168d5d3`  |
| 652    | No file  | `62325168d5d3`  |
| 643    | No file  | `62325168d5d3`  |
| 637    | No file  | `62325168d5d3`  |
| 630    | No file  | `62325168d5d3`  |
| 627    | No file  | `62325168d5d3`  |
| 621    | No file  | `62325168d5d3`  |
| 617    | No file  | `62325168d5d3`  |
| 615    | No file  | `62325168d5d3`  |
| 606    | No file  | `62325168d5d3`  |
| 599    | No file  | `62325168d5d3`  |
| 592    | No file  | `62325168d5d3`  |
| 586    | No file  | `62325168d5d3`  |
| 577    | No file  | `62325168d5d3`  |
| 569    | No file  | `62325168d5d3`  |
| 561    | No file  | `62325168d5d3`  |
| 554    | No file  | `62325168d5d3`  |
| 542    | No file  | `62325168d5d3`  |
| 532    | No file  | `62325168d5d3`  |
| 531    | No file  | `62325168d5d3`  |
| 526    | No file  | `62325168d5d3`  |
| 521    | No file  | `62325168d5d3`  |
| 517    | No file  | `62325168d5d3`  |
| 510    | No file  | `62325168d5d3`  |
| 508    | No file  | `62325168d5d3`  |
| 504    | No file  | `62325168d5d3`  |
| 497    | No file  | `62325168d5d3`  |
| 491    | No file  | `62325168d5d3`  |
| 485    | No file  | `62325168d5d3`  |
| 478    | No file  | `62325168d5d3`  |
| 472    | No file  | `62325168d5d3`  |
| 466    | No file  | `62325168d5d3`  |
| 457    | No file  | `62325168d5d3`  |
| 452    | No file  | `62325168d5d3`  |
| 449    | No file  | `62325168d5d3`  |
| 435    | No file  | `62325168d5d3`  |

<!-- versions:end -->

## Companion Files

The same as [`allquestlist.bss`](allquestlist_bss.md).

All multi-byte values are little-endian.

## Quest Chains

On client 3474 the 180 quests come from 27 quest chains. Every entry has a LOC type 18 title.

| Chains                       | Quests | Example title                                     |
| ---------------------------- | -----: | ------------------------------------------------- |
| 769                          | 3      | Accessory Filled with the Witch's Power - Part I  |
| 785, 894                     | 29     | [Subjugation] Pluck Those Manshaum Fangs          |
| 3724, 3733, 3734             | 23     | Saltwater Crocodile's Treasure I                  |
| 9035, 9037, 9051, 9083       | 4      | [Weekly] Sycrakea: Abyssal Chest                  |
| 9121 to 9125, 9322 to 9326   | 30     | Magaia Subjugation I                              |
| 11491, 15501                 | 6      | [Weekly] Looting Garmoth I                        |
| 12022                        | 9      | Defend the Delphe Knights Castle!                 |
| 12023, 12024, 40015, 40032   | 76     | [Season] Settling Down at the Bashim Base         |

The completion scripts (`action_script` in `quest.dbss`) on client 3474: 151 `killmonstergroup` (any case), 16 `killmonster`, 3 `KillMonsterTogether` and 10 `checkLooting`. Other categories hold kill quests too: 702 of the 853 quests with a `killmonstergroup` script (any case) are not in this list. The first argument of `killmonstergroup` is a `character_group` key of [`characterstatic.dbss`](../dbss/characterstatic_dbss.md#character-group); all 167 keys of these 853 quests have characters on client 3474.

## Client Use

The client Lua reads a list of the same name through the quest list object: `questList:getRegionMonsterKillQuestCount()` and `questList:getRegionMonsterKillQuestAt(i)`, each entry a quest number with `_group` (the chain) and `_quest`. The only caller in the client Lua is the alert widget (`panel_widget_alertarea_renew.luac`): a checked quest that is satisfied and completes at the Black Spirit raises the Black Spirit alert only when it is not in this list. `panel_widget_accesoryquest.luac` registers the event `FromClient_notifyUpdateRegionMonsterKillQuest` with an empty function; that widget shows the current region's quest from `getSuddenQuestWrapperOnCurrentRegion()` with its kill counter and a complete button.

## Notes

- Decompressed size on client 3474: `740` bytes, `8 + 180 * 4 + 12`.
- On client 3474 `quest.dbss` has 180 records with `quest_category` 12, and they are this list in the same order. `test_region_monster_kill_list.py` checks the match.
- Client 1784 has 114 entries in 8 chains (769, 785, 3724, 12022, 12023, 12024, 40015, 40032). 110 of them are still in the client 3474 list; 40015 / 17 to 20 are gone. All 114 have `QuestType` 11 in the `Quest_Table` sheet of a private server's `DataSheets.bexcel` on client 1784; the one other `QuestType` 11 row of that sheet (3431 / 1, `killMonsterGroup(116,300);`) is not in the list. On the 110 keys that both clients share, `QuestType` 11 lines up with the live `quest_category` 12.