# `specialquestlist.bss` Format

## Purpose

Quest list of the Adventure Log pages: every page quest of the books in [`journalquest.dbss`](journalquest_dbss.md), the quests the client Lua calls special quests. On client 3474 the list holds exactly the 896 `quest.dbss` records with `quest_category` 11, in `quest.dbss` record order, and they are the 896 page quests of the 118 books.

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, where the trailer starts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records   | Row bytes |
| ------ | -------------- | ---------------------- | ----- | --------- | --------- |
| 1      | 1109 and later | `specialquestlist.bss` | 3,604 | 896 Entry | 4         |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `specialquestlist.bss` | 3,604 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `366b3f3f8a2e`  |
| 3482   | Layout 1 | `366b3f3f8a2e`  |
| 3474   | Layout 1 | `366b3f3f8a2e`  |
| 3473   | Layout 1 | `366b3f3f8a2e`  |
| 3464   | Layout 1 | `366b3f3f8a2e`  |
| 3458   | Layout 1 | `366b3f3f8a2e`  |
| 3454   | Layout 1 | `366b3f3f8a2e`  |
| 3444   | Layout 1 | `366b3f3f8a2e`  |
| 3435   | Layout 1 | `366b3f3f8a2e`  |
| 3426   | Layout 1 | `366b3f3f8a2e`  |
| 3418   | Layout 1 | `366b3f3f8a2e`  |
| 3412   | Layout 1 | `366b3f3f8a2e`  |
| 3402   | Layout 1 | `366b3f3f8a2e`  |
| 3396   | Layout 1 | `366b3f3f8a2e`  |
| 3387   | Layout 1 | `366b3f3f8a2e`  |
| 3381   | Layout 1 | `366b3f3f8a2e`  |
| 3373   | Layout 1 | `366b3f3f8a2e`  |
| 3364   | Layout 1 | `366b3f3f8a2e`  |
| 3356   | Layout 1 | `366b3f3f8a2e`  |
| 3349   | Layout 1 | `366b3f3f8a2e`  |
| 3342   | Layout 1 | `366b3f3f8a2e`  |
| 3335   | Layout 1 | `366b3f3f8a2e`  |
| 3326   | Layout 1 | `366b3f3f8a2e`  |
| 3321   | Layout 1 | `366b3f3f8a2e`  |
| 3314   | Layout 1 | `366b3f3f8a2e`  |
| 3303   | Layout 1 | `366b3f3f8a2e`  |
| 3302   | Layout 1 | `366b3f3f8a2e`  |
| 3293   | Layout 1 | `366b3f3f8a2e`  |
| 3283   | Layout 1 | `366b3f3f8a2e`  |
| 3275   | Layout 1 | `366b3f3f8a2e`  |
| 3267   | Layout 1 | `366b3f3f8a2e`  |
| 3258   | Layout 1 | `366b3f3f8a2e`  |
| 3251   | Layout 1 | `366b3f3f8a2e`  |
| 3242   | Layout 1 | `366b3f3f8a2e`  |
| 3235   | Layout 1 | `366b3f3f8a2e`  |
| 3229   | Layout 1 | `366b3f3f8a2e`  |
| 3212   | Layout 1 | `366b3f3f8a2e`  |
| 3203   | Layout 1 | `366b3f3f8a2e`  |
| 3193   | Layout 1 | `366b3f3f8a2e`  |
| 3186   | Layout 1 | `366b3f3f8a2e`  |
| 3177   | Layout 1 | `366b3f3f8a2e`  |
| 3169   | Layout 1 | `366b3f3f8a2e`  |
| 3158   | Layout 1 | `366b3f3f8a2e`  |
| 3151   | Layout 1 | `366b3f3f8a2e`  |
| 3144   | Layout 1 | `366b3f3f8a2e`  |
| 3133   | Layout 1 | `366b3f3f8a2e`  |
| 3125   | Layout 1 | `366b3f3f8a2e`  |
| 3118   | Layout 1 | `366b3f3f8a2e`  |
| 3111   | Layout 1 | `366b3f3f8a2e`  |
| 3103   | Layout 1 | `366b3f3f8a2e`  |
| 3095   | Layout 1 | `366b3f3f8a2e`  |
| 3086   | Layout 1 | `366b3f3f8a2e`  |
| 3072   | Layout 1 | `366b3f3f8a2e`  |
| 3062   | Layout 1 | `366b3f3f8a2e`  |
| 3052   | Layout 1 | `366b3f3f8a2e`  |
| 3045   | Layout 1 | `366b3f3f8a2e`  |
| 3037   | Layout 1 | `366b3f3f8a2e`  |
| 3030   | Layout 1 | `366b3f3f8a2e`  |
| 3021   | Layout 1 | `366b3f3f8a2e`  |
| 3012   | Layout 1 | `366b3f3f8a2e`  |
| 3002   | Layout 1 | `366b3f3f8a2e`  |
| 2995   | Layout 1 | `366b3f3f8a2e`  |
| 2987   | Layout 1 | `366b3f3f8a2e`  |
| 2978   | Layout 1 | `366b3f3f8a2e`  |
| 2970   | Layout 1 | `366b3f3f8a2e`  |
| 2959   | Layout 1 | `366b3f3f8a2e`  |
| 2951   | Layout 1 | `366b3f3f8a2e`  |
| 2942   | Layout 1 | `366b3f3f8a2e`  |
| 2935   | Layout 1 | `366b3f3f8a2e`  |
| 2932   | Layout 1 | `366b3f3f8a2e`  |
| 2923   | Layout 1 | `366b3f3f8a2e`  |
| 2919   | Layout 1 | `366b3f3f8a2e`  |
| 2907   | Layout 1 | `366b3f3f8a2e`  |
| 2900   | Layout 1 | `366b3f3f8a2e`  |
| 2891   | Layout 1 | `366b3f3f8a2e`  |
| 2882   | Layout 1 | `366b3f3f8a2e`  |
| 2872   | Layout 1 | `366b3f3f8a2e`  |
| 2863   | Layout 1 | `366b3f3f8a2e`  |
| 2855   | Layout 1 | `366b3f3f8a2e`  |
| 2849   | Layout 1 | `366b3f3f8a2e`  |
| 2844   | Layout 1 | `366b3f3f8a2e`  |
| 2834   | Layout 1 | `366b3f3f8a2e`  |
| 2825   | Layout 1 | `366b3f3f8a2e`  |
| 2819   | Layout 1 | `366b3f3f8a2e`  |
| 2811   | Layout 1 | `366b3f3f8a2e`  |
| 2803   | Layout 1 | `366b3f3f8a2e`  |
| 2794   | Layout 1 | `366b3f3f8a2e`  |
| 2783   | Layout 1 | `366b3f3f8a2e`  |
| 2774   | Layout 1 | `366b3f3f8a2e`  |
| 2765   | Layout 1 | `366b3f3f8a2e`  |
| 2756   | Layout 1 | `366b3f3f8a2e`  |
| 2750   | Layout 1 | `366b3f3f8a2e`  |
| 2743   | Layout 1 | `366b3f3f8a2e`  |
| 2736   | Layout 1 | `366b3f3f8a2e`  |
| 2726   | Layout 1 | `366b3f3f8a2e`  |
| 2717   | Layout 1 | `366b3f3f8a2e`  |
| 2709   | Layout 1 | `366b3f3f8a2e`  |
| 2703   | Layout 1 | `366b3f3f8a2e`  |
| 2695   | Layout 1 | `366b3f3f8a2e`  |
| 2684   | Layout 1 | `366b3f3f8a2e`  |
| 2672   | Layout 1 | `366b3f3f8a2e`  |
| 2665   | Layout 1 | `366b3f3f8a2e`  |
| 2657   | Layout 1 | `366b3f3f8a2e`  |
| 2649   | Layout 1 | `366b3f3f8a2e`  |
| 2644   | Layout 1 | `366b3f3f8a2e`  |
| 2637   | Layout 1 | `366b3f3f8a2e`  |
| 2629   | Layout 1 | `366b3f3f8a2e`  |
| 2619   | Layout 1 | `366b3f3f8a2e`  |
| 2612   | Layout 1 | `366b3f3f8a2e`  |
| 2606   | Layout 1 | `366b3f3f8a2e`  |
| 2602   | Layout 1 | `366b3f3f8a2e`  |
| 2601   | Layout 1 | `366b3f3f8a2e`  |
| 2592   | Layout 1 | `366b3f3f8a2e`  |
| 2583   | Layout 1 | `366b3f3f8a2e`  |
| 2575   | Layout 1 | `366b3f3f8a2e`  |
| 2567   | Layout 1 | `366b3f3f8a2e`  |
| 2560   | Layout 1 | `366b3f3f8a2e`  |
| 2553   | Layout 1 | `366b3f3f8a2e`  |
| 2545   | Layout 1 | `366b3f3f8a2e`  |
| 2538   | Layout 1 | `366b3f3f8a2e`  |
| 2529   | Layout 1 | `366b3f3f8a2e`  |
| 2519   | Layout 1 | `366b3f3f8a2e`  |
| 2513   | Layout 1 | `366b3f3f8a2e`  |
| 2510   | Layout 1 | `366b3f3f8a2e`  |
| 2507   | Layout 1 | `366b3f3f8a2e`  |
| 2503   | Layout 1 | `366b3f3f8a2e`  |
| 2498   | Layout 1 | `366b3f3f8a2e`  |
| 2492   | Layout 1 | `366b3f3f8a2e`  |
| 2487   | Layout 1 | `366b3f3f8a2e`  |
| 2480   | Layout 1 | `366b3f3f8a2e`  |
| 2474   | Layout 1 | `366b3f3f8a2e`  |
| 2468   | Layout 1 | `366b3f3f8a2e`  |
| 2460   | Layout 1 | `366b3f3f8a2e`  |
| 2453   | Layout 1 | `366b3f3f8a2e`  |
| 2444   | Layout 1 | `366b3f3f8a2e`  |
| 2438   | Layout 1 | `366b3f3f8a2e`  |
| 2434   | Layout 1 | `366b3f3f8a2e`  |
| 2429   | Layout 1 | `366b3f3f8a2e`  |
| 2421   | Layout 1 | `366b3f3f8a2e`  |
| 2414   | Layout 1 | `366b3f3f8a2e`  |
| 2407   | Layout 1 | `366b3f3f8a2e`  |
| 2401   | Layout 1 | `366b3f3f8a2e`  |
| 2397   | Layout 1 | `366b3f3f8a2e`  |
| 2393   | Layout 1 | `366b3f3f8a2e`  |
| 2384   | Layout 1 | `366b3f3f8a2e`  |
| 2378   | Layout 1 | `366b3f3f8a2e`  |
| 2372   | Layout 1 | `366b3f3f8a2e`  |
| 2358   | Layout 1 | `366b3f3f8a2e`  |
| 2352   | Layout 1 | `366b3f3f8a2e`  |
| 2347   | Layout 1 | `366b3f3f8a2e`  |
| 2343   | Layout 1 | `366b3f3f8a2e`  |
| 2335   | Layout 1 | `366b3f3f8a2e`  |
| 2327   | Layout 1 | `366b3f3f8a2e`  |
| 2324   | Layout 1 | `366b3f3f8a2e`  |
| 2319   | Layout 1 | `366b3f3f8a2e`  |
| 2313   | Layout 1 | `366b3f3f8a2e`  |
| 2308   | Layout 1 | `366b3f3f8a2e`  |
| 2302   | Layout 1 | `366b3f3f8a2e`  |
| 2295   | Layout 1 | `366b3f3f8a2e`  |
| 2290   | Layout 1 | `366b3f3f8a2e`  |
| 2284   | Layout 1 | `366b3f3f8a2e`  |
| 2276   | Layout 1 | `366b3f3f8a2e`  |
| 2269   | Layout 1 | `366b3f3f8a2e`  |
| 2259   | Layout 1 | `366b3f3f8a2e`  |
| 2250   | Layout 1 | `366b3f3f8a2e`  |
| 2243   | Layout 1 | `366b3f3f8a2e`  |
| 2235   | Layout 1 | `366b3f3f8a2e`  |
| 2229   | Layout 1 | `366b3f3f8a2e`  |
| 2224   | Layout 1 | `366b3f3f8a2e`  |
| 2218   | Layout 1 | `366b3f3f8a2e`  |
| 2215   | Layout 1 | `366b3f3f8a2e`  |
| 2207   | Layout 1 | `366b3f3f8a2e`  |
| 2203   | Layout 1 | `366b3f3f8a2e`  |
| 2196   | Layout 1 | `366b3f3f8a2e`  |
| 2192   | Layout 1 | `366b3f3f8a2e`  |
| 2189   | Layout 1 | `366b3f3f8a2e`  |
| 2183   | Layout 1 | `366b3f3f8a2e`  |
| 2179   | Layout 1 | `366b3f3f8a2e`  |
| 2171   | Layout 1 | `366b3f3f8a2e`  |
| 2163   | Layout 1 | `366b3f3f8a2e`  |
| 2156   | Layout 1 | `366b3f3f8a2e`  |
| 2151   | Layout 1 | `366b3f3f8a2e`  |
| 2147   | Layout 1 | `366b3f3f8a2e`  |
| 2142   | Layout 1 | `366b3f3f8a2e`  |
| 2138   | Layout 1 | `366b3f3f8a2e`  |
| 2134   | Layout 1 | `366b3f3f8a2e`  |
| 2130   | Layout 1 | `366b3f3f8a2e`  |
| 2122   | Layout 1 | `366b3f3f8a2e`  |
| 2107   | Layout 1 | `366b3f3f8a2e`  |
| 2098   | Layout 1 | `366b3f3f8a2e`  |
| 2089   | Layout 1 | `366b3f3f8a2e`  |
| 2081   | Layout 1 | `366b3f3f8a2e`  |
| 2073   | Layout 1 | `366b3f3f8a2e`  |
| 2067   | Layout 1 | `366b3f3f8a2e`  |
| 2063   | Layout 1 | `366b3f3f8a2e`  |
| 2059   | Layout 1 | `366b3f3f8a2e`  |
| 2052   | Layout 1 | `366b3f3f8a2e`  |
| 2044   | Layout 1 | `366b3f3f8a2e`  |
| 2039   | Layout 1 | `366b3f3f8a2e`  |
| 2032   | Layout 1 | `366b3f3f8a2e`  |
| 2025   | Layout 1 | `366b3f3f8a2e`  |
| 2011   | Layout 1 | `366b3f3f8a2e`  |
| 2005   | Layout 1 | `366b3f3f8a2e`  |
| 2000   | Layout 1 | `366b3f3f8a2e`  |
| 1996   | Layout 1 | `366b3f3f8a2e`  |
| 1991   | Layout 1 | `366b3f3f8a2e`  |
| 1985   | Layout 1 | `366b3f3f8a2e`  |
| 1980   | Layout 1 | `366b3f3f8a2e`  |
| 1969   | Layout 1 | `366b3f3f8a2e`  |
| 1964   | Layout 1 | `366b3f3f8a2e`  |
| 1958   | Layout 1 | `366b3f3f8a2e`  |
| 1950   | Layout 1 | `366b3f3f8a2e`  |
| 1945   | Layout 1 | `366b3f3f8a2e`  |
| 1937   | Layout 1 | `366b3f3f8a2e`  |
| 1933   | Layout 1 | `366b3f3f8a2e`  |
| 1927   | Layout 1 | `366b3f3f8a2e`  |
| 1921   | Layout 1 | `366b3f3f8a2e`  |
| 1914   | Layout 1 | `366b3f3f8a2e`  |
| 1908   | Layout 1 | `366b3f3f8a2e`  |
| 1897   | Layout 1 | `366b3f3f8a2e`  |
| 1892   | Layout 1 | `366b3f3f8a2e`  |
| 1886   | Layout 1 | `366b3f3f8a2e`  |
| 1881   | Layout 1 | `366b3f3f8a2e`  |
| 1871   | Layout 1 | `366b3f3f8a2e`  |
| 1866   | Layout 1 | `366b3f3f8a2e`  |
| 1862   | Layout 1 | `366b3f3f8a2e`  |
| 1854   | Layout 1 | `366b3f3f8a2e`  |
| 1846   | Layout 1 | `366b3f3f8a2e`  |
| 1838   | Layout 1 | `366b3f3f8a2e`  |
| 1832   | Layout 1 | `366b3f3f8a2e`  |
| 1826   | Layout 1 | `366b3f3f8a2e`  |
| 1822   | Layout 1 | `366b3f3f8a2e`  |
| 1818   | Layout 1 | `366b3f3f8a2e`  |
| 1804   | Layout 1 | `366b3f3f8a2e`  |
| 1794   | Layout 1 | `366b3f3f8a2e`  |
| 1790   | Layout 1 | `366b3f3f8a2e`  |
| 1784   | Layout 1 | `366b3f3f8a2e`  |
| 1774   | Layout 1 | `366b3f3f8a2e`  |
| 1771   | Layout 1 | `366b3f3f8a2e`  |
| 1762   | Layout 1 | `366b3f3f8a2e`  |
| 1759   | Layout 1 | `366b3f3f8a2e`  |
| 1754   | Layout 1 | `366b3f3f8a2e`  |
| 1749   | Layout 1 | `366b3f3f8a2e`  |
| 1743   | Layout 1 | `366b3f3f8a2e`  |
| 1737   | Layout 1 | `366b3f3f8a2e`  |
| 1731   | Layout 1 | `366b3f3f8a2e`  |
| 1725   | Layout 1 | `366b3f3f8a2e`  |
| 1717   | Layout 1 | `366b3f3f8a2e`  |
| 1710   | Layout 1 | `366b3f3f8a2e`  |
| 1704   | Layout 1 | `366b3f3f8a2e`  |
| 1698   | Layout 1 | `366b3f3f8a2e`  |
| 1690   | Layout 1 | `366b3f3f8a2e`  |
| 1685   | Layout 1 | `366b3f3f8a2e`  |
| 1680   | Layout 1 | `366b3f3f8a2e`  |
| 1674   | Layout 1 | `366b3f3f8a2e`  |
| 1668   | Layout 1 | `366b3f3f8a2e`  |
| 1659   | Layout 1 | `366b3f3f8a2e`  |
| 1649   | Layout 1 | `366b3f3f8a2e`  |
| 1642   | Layout 1 | `366b3f3f8a2e`  |
| 1636   | Layout 1 | `366b3f3f8a2e`  |
| 1628   | Layout 1 | `366b3f3f8a2e`  |
| 1622   | Layout 1 | `366b3f3f8a2e`  |
| 1614   | Layout 1 | `366b3f3f8a2e`  |
| 1608   | Layout 1 | `366b3f3f8a2e`  |
| 1602   | Layout 1 | `366b3f3f8a2e`  |
| 1598   | Layout 1 | `366b3f3f8a2e`  |
| 1594   | Layout 1 | `366b3f3f8a2e`  |
| 1590   | Layout 1 | `366b3f3f8a2e`  |
| 1587   | Layout 1 | `366b3f3f8a2e`  |
| 1584   | Layout 1 | `366b3f3f8a2e`  |
| 1579   | Layout 1 | `366b3f3f8a2e`  |
| 1572   | Layout 1 | `366b3f3f8a2e`  |
| 1565   | Layout 1 | `366b3f3f8a2e`  |
| 1559   | Layout 1 | `366b3f3f8a2e`  |
| 1554   | Layout 1 | `366b3f3f8a2e`  |
| 1547   | Layout 1 | `366b3f3f8a2e`  |
| 1537   | Layout 1 | `366b3f3f8a2e`  |
| 1529   | Layout 1 | `366b3f3f8a2e`  |
| 1524   | Layout 1 | `366b3f3f8a2e`  |
| 1519   | Layout 1 | `366b3f3f8a2e`  |
| 1509   | Layout 1 | `366b3f3f8a2e`  |
| 1506   | Layout 1 | `366b3f3f8a2e`  |
| 1504   | Layout 1 | `366b3f3f8a2e`  |
| 1500   | Layout 1 | `366b3f3f8a2e`  |
| 1493   | Layout 1 | `366b3f3f8a2e`  |
| 1489   | Layout 1 | `366b3f3f8a2e`  |
| 1485   | Layout 1 | `366b3f3f8a2e`  |
| 1481   | Layout 1 | `366b3f3f8a2e`  |
| 1474   | Layout 1 | `366b3f3f8a2e`  |
| 1466   | Layout 1 | `366b3f3f8a2e`  |
| 1462   | Layout 1 | `366b3f3f8a2e`  |
| 1459   | Layout 1 | `366b3f3f8a2e`  |
| 1453   | Layout 1 | `366b3f3f8a2e`  |
| 1450   | Layout 1 | `366b3f3f8a2e`  |
| 1445   | Layout 1 | `366b3f3f8a2e`  |
| 1439   | Layout 1 | `366b3f3f8a2e`  |
| 1433   | Layout 1 | `366b3f3f8a2e`  |
| 1430   | Layout 1 | `366b3f3f8a2e`  |
| 1426   | Layout 1 | `366b3f3f8a2e`  |
| 1421   | Layout 1 | `366b3f3f8a2e`  |
| 1417   | Layout 1 | `366b3f3f8a2e`  |
| 1416   | Layout 1 | `366b3f3f8a2e`  |
| 1409   | Layout 1 | `366b3f3f8a2e`  |
| 1405   | Layout 1 | `366b3f3f8a2e`  |
| 1401   | Layout 1 | `366b3f3f8a2e`  |
| 1396   | Layout 1 | `366b3f3f8a2e`  |
| 1391   | Layout 1 | `366b3f3f8a2e`  |
| 1390   | Layout 1 | `366b3f3f8a2e`  |
| 1386   | Layout 1 | `366b3f3f8a2e`  |
| 1381   | Layout 1 | `366b3f3f8a2e`  |
| 1379   | Layout 1 | `366b3f3f8a2e`  |
| 1372   | Layout 1 | `366b3f3f8a2e`  |
| 1366   | Layout 1 | `366b3f3f8a2e`  |
| 1364   | Layout 1 | `366b3f3f8a2e`  |
| 1363   | Layout 1 | `366b3f3f8a2e`  |
| 1360   | Layout 1 | `366b3f3f8a2e`  |
| 1358   | Layout 1 | `366b3f3f8a2e`  |
| 1355   | Layout 1 | `366b3f3f8a2e`  |
| 1351   | Layout 1 | `366b3f3f8a2e`  |
| 1348   | Layout 1 | `366b3f3f8a2e`  |
| 1346   | Layout 1 | `366b3f3f8a2e`  |
| 1341   | Layout 1 | `366b3f3f8a2e`  |
| 1340   | Layout 1 | `366b3f3f8a2e`  |
| 1338   | Layout 1 | `366b3f3f8a2e`  |
| 1335   | Layout 1 | `366b3f3f8a2e`  |
| 1333   | Layout 1 | `366b3f3f8a2e`  |
| 1329   | Layout 1 | `366b3f3f8a2e`  |
| 1327   | Layout 1 | `366b3f3f8a2e`  |
| 1324   | Layout 1 | `366b3f3f8a2e`  |
| 1321   | Layout 1 | `366b3f3f8a2e`  |
| 1319   | Layout 1 | `366b3f3f8a2e`  |
| 1318   | Layout 1 | `366b3f3f8a2e`  |
| 1316   | Layout 1 | `366b3f3f8a2e`  |
| 1313   | Layout 1 | `366b3f3f8a2e`  |
| 1311   | Layout 1 | `366b3f3f8a2e`  |
| 1309   | Layout 1 | `366b3f3f8a2e`  |
| 1304   | Layout 1 | `366b3f3f8a2e`  |
| 1292   | Layout 1 | `366b3f3f8a2e`  |
| 1286   | Layout 1 | `366b3f3f8a2e`  |
| 1280   | Layout 1 | `366b3f3f8a2e`  |
| 1276   | Layout 1 | `366b3f3f8a2e`  |
| 1267   | Layout 1 | `366b3f3f8a2e`  |
| 1261   | Layout 1 | `366b3f3f8a2e`  |
| 1256   | Layout 1 | `366b3f3f8a2e`  |
| 1250   | Layout 1 | `366b3f3f8a2e`  |
| 1246   | No file  | `366b3f3f8a2e`  |
| 1239   | No file  | `366b3f3f8a2e`  |
| 1230   | No file  | `366b3f3f8a2e`  |
| 1226   | No file  | `366b3f3f8a2e`  |
| 1220   | No file  | `366b3f3f8a2e`  |
| 1217   | No file  | `366b3f3f8a2e`  |
| 1211   | No file  | `366b3f3f8a2e`  |
| 1210   | No file  | `366b3f3f8a2e`  |
| 1208   | No file  | `366b3f3f8a2e`  |
| 1203   | No file  | `366b3f3f8a2e`  |
| 1197   | No file  | `366b3f3f8a2e`  |
| 1194   | No file  | `366b3f3f8a2e`  |
| 1192   | No file  | `366b3f3f8a2e`  |
| 1187   | No file  | `366b3f3f8a2e`  |
| 1183   | No file  | `366b3f3f8a2e`  |
| 1177   | No file  | `366b3f3f8a2e`  |
| 1173   | No file  | `366b3f3f8a2e`  |
| 1167   | No file  | `366b3f3f8a2e`  |
| 1164   | No file  | `366b3f3f8a2e`  |
| 1156   | No file  | `366b3f3f8a2e`  |
| 1149   | No file  | `366b3f3f8a2e`  |
| 1144   | Layout 1 | `366b3f3f8a2e`  |
| 1137   | Layout 1 | `366b3f3f8a2e`  |
| 1132   | Layout 1 | `366b3f3f8a2e`  |
| 1127   | Layout 1 | `366b3f3f8a2e`  |
| 1122   | Layout 1 | `366b3f3f8a2e`  |
| 1118   | Layout 1 | `366b3f3f8a2e`  |
| 1114   | Layout 1 | `366b3f3f8a2e`  |
| 1109   | Layout 1 | `366b3f3f8a2e`  |
| 1102   | No file  | `366b3f3f8a2e`  |
| 1096   | No file  | `366b3f3f8a2e`  |
| 1088   | No file  | `366b3f3f8a2e`  |
| 1081   | No file  | `366b3f3f8a2e`  |
| 1076   | No file  | `366b3f3f8a2e`  |
| 1069   | No file  | `366b3f3f8a2e`  |
| 1064   | No file  | `366b3f3f8a2e`  |
| 1058   | No file  | `366b3f3f8a2e`  |
| 1051   | No file  | `366b3f3f8a2e`  |
| 1044   | No file  | `366b3f3f8a2e`  |
| 1036   | No file  | `366b3f3f8a2e`  |
| 1026   | No file  | `366b3f3f8a2e`  |
| 1016   | No file  | `366b3f3f8a2e`  |
| 1009   | No file  | `366b3f3f8a2e`  |
| 1005   | No file  | `366b3f3f8a2e`  |
| 1000   | No file  | `366b3f3f8a2e`  |
| 998    | No file  | `366b3f3f8a2e`  |
| 990    | No file  | `366b3f3f8a2e`  |
| 979    | No file  | `366b3f3f8a2e`  |
| 972    | No file  | `366b3f3f8a2e`  |
| 963    | No file  | `366b3f3f8a2e`  |
| 955    | No file  | `366b3f3f8a2e`  |
| 946    | No file  | `366b3f3f8a2e`  |
| 938    | No file  | `366b3f3f8a2e`  |
| 927    | No file  | `366b3f3f8a2e`  |
| 911    | No file  | `366b3f3f8a2e`  |
| 904    | No file  | `366b3f3f8a2e`  |
| 899    | No file  | `366b3f3f8a2e`  |
| 894    | No file  | `366b3f3f8a2e`  |
| 885    | No file  | `366b3f3f8a2e`  |
| 879    | No file  | `366b3f3f8a2e`  |
| 872    | No file  | `366b3f3f8a2e`  |
| 864    | No file  | `366b3f3f8a2e`  |
| 855    | No file  | `366b3f3f8a2e`  |
| 853    | No file  | `366b3f3f8a2e`  |
| 845    | No file  | `366b3f3f8a2e`  |
| 837    | No file  | `366b3f3f8a2e`  |
| 829    | No file  | `366b3f3f8a2e`  |
| 822    | No file  | `366b3f3f8a2e`  |
| 814    | No file  | `366b3f3f8a2e`  |
| 805    | No file  | `366b3f3f8a2e`  |
| 794    | No file  | `366b3f3f8a2e`  |
| 787    | No file  | `366b3f3f8a2e`  |
| 780    | No file  | `366b3f3f8a2e`  |
| 771    | No file  | `366b3f3f8a2e`  |
| 760    | No file  | `366b3f3f8a2e`  |
| 748    | No file  | `366b3f3f8a2e`  |
| 741    | No file  | `366b3f3f8a2e`  |
| 736    | No file  | `366b3f3f8a2e`  |
| 731    | No file  | `366b3f3f8a2e`  |
| 723    | No file  | `366b3f3f8a2e`  |
| 711    | No file  | `366b3f3f8a2e`  |
| 707    | No file  | `366b3f3f8a2e`  |
| 697    | No file  | `366b3f3f8a2e`  |
| 689    | No file  | `366b3f3f8a2e`  |
| 683    | No file  | `366b3f3f8a2e`  |
| 678    | No file  | `366b3f3f8a2e`  |
| 670    | No file  | `366b3f3f8a2e`  |
| 661    | No file  | `366b3f3f8a2e`  |
| 656    | No file  | `366b3f3f8a2e`  |
| 652    | No file  | `366b3f3f8a2e`  |
| 643    | No file  | `366b3f3f8a2e`  |
| 637    | No file  | `366b3f3f8a2e`  |
| 630    | No file  | `366b3f3f8a2e`  |
| 627    | No file  | `366b3f3f8a2e`  |
| 621    | No file  | `366b3f3f8a2e`  |
| 617    | No file  | `366b3f3f8a2e`  |
| 615    | No file  | `366b3f3f8a2e`  |
| 606    | No file  | `366b3f3f8a2e`  |
| 599    | No file  | `366b3f3f8a2e`  |
| 592    | No file  | `366b3f3f8a2e`  |
| 586    | No file  | `366b3f3f8a2e`  |
| 577    | No file  | `366b3f3f8a2e`  |
| 569    | No file  | `366b3f3f8a2e`  |
| 561    | No file  | `366b3f3f8a2e`  |
| 554    | No file  | `366b3f3f8a2e`  |
| 542    | No file  | `366b3f3f8a2e`  |
| 532    | No file  | `366b3f3f8a2e`  |
| 531    | No file  | `366b3f3f8a2e`  |
| 526    | No file  | `366b3f3f8a2e`  |
| 521    | No file  | `366b3f3f8a2e`  |
| 517    | No file  | `366b3f3f8a2e`  |
| 510    | No file  | `366b3f3f8a2e`  |
| 508    | No file  | `366b3f3f8a2e`  |
| 504    | No file  | `366b3f3f8a2e`  |
| 497    | No file  | `366b3f3f8a2e`  |
| 491    | No file  | `366b3f3f8a2e`  |
| 485    | No file  | `366b3f3f8a2e`  |
| 478    | No file  | `366b3f3f8a2e`  |
| 472    | No file  | `366b3f3f8a2e`  |
| 466    | No file  | `366b3f3f8a2e`  |
| 457    | No file  | `366b3f3f8a2e`  |
| 452    | No file  | `366b3f3f8a2e`  |
| 449    | No file  | `366b3f3f8a2e`  |
| 435    | No file  | `366b3f3f8a2e`  |

<!-- versions:end -->

## Companion Files

The same as [`allquestlist.bss`](allquestlist_bss.md).

All multi-byte values are little-endian.

## Quest Chains

Each book of `journalquest.dbss` is one quest chain (`journal_cat_id`), and its pages are that chain's quests. On client 3474 the 896 entries come from 118 chains, one per book, and every entry has a LOC type 18 title. Grouped by journal from `journalquest.dbss`, with the journal's English name from LOC type 63; Chains gives its lowest and highest book chain, not every chain in between:

| Journal Key | Journal                     | Books | Pages | Chains        |
| ----------: | --------------------------- | ----: | ----: | ------------- |
| 1           | Igor Bartali's Adventures   | 15    | 71    | 748 to 802    |
| 2           | Shakatu Merchants' Archive  | 11    | 51    | 826 to 30008  |
| 3           | Storybook - Morning Bosses  | 10    | 105   | 897 to 962    |
| 4           | Justin Bartali's Adventures | 1     | 17    | 2302          |
| 5           | Crow Merchants' Records     | 13    | 66    | 790 to 9007   |
| 6           | Event Logs                  | 6     | 39    | 9008 to 11551 |
| 7           | Storybook - Donghae         | 15    | 180   | 8700 to 8714  |
| 8           | Olvia Academy Journal       | 1     | 13    | 2326          |
| 9           | Old Moon Logs               | 10    | 53    | 792 to 841    |
| 10          | Outer Edania                | 7     | 44    | 9131 to 9137  |
| 11          | The Eyes of Adventure       | 9     | 45    | 8721 to 8729  |
| 12          | Storybook - Hwanghae        | 13    | 138   | 8542 to 8554  |
| 13          | Inner Edania                | 7     | 74    | 9331 to 9337  |

The list does not keep a book's pages together or in page order: on client 3474 the 118 chains form 331 runs, and in 38 chains the quest IDs are not ascending. The order is the `quest.dbss` record order.

## Client Use

The client Lua reads a list of the same name through the quest list object: `questList:getSpecialQuestCount()` and `questList:getSpecialQuestAt(i)`, each entry a quest number with `_group` (the chain) and `_quest`, and through the globals `ToClient_SpecialQuestCount()` and `ToClient_GetSpecialQuest(i)`, which return a quest wrapper.

- `panel_window_achievement.luac` (the Adventure Log book window, behind `_ContentsGroup_AchievementQuest`): `questSetting(groupNo)` walks `ToClient_GetSpecialQuest` and keeps the entries whose `_group` is the opened book's chain, then sorts them by `_quest`. The reward button looks up the quest's index in `getSpecialQuestAt` and sends it with `ToClient_RequestCompleteSpecialQuest(i)`, so the request carries the list position, not the quest number. The window registers `FromClient_notifyUpdateSpecialQuest` and refreshes when the updated quest is the shown page.
- `panel_widget_challengealert.luac`: `setProgressCount()` walks `getSpecialQuestAt` and stores the first demand's `_currentCount` of each special quest in progress, per chain. Its `FromClient_notifyUpdateSpecialQuest` handler runs only with `_ContentsGroup_AchievementQuest` and a character over level 60.

## Notes

- Decompressed size on client 3474: `3,604` bytes, `8 + 896 * 4 + 12`.
- On client 3474 `quest.dbss` has 896 records with `quest_category` 11, and they are this list in the same order. The same 896 quests are the page references of the 118 `journalquest.dbss` books, each once. `test_special_quest_list.py` checks the order and that every page is in the list.
- Client 3482 keeps the 896 entries but drops the book of chain 962 (the ten "Boss: Calamity 10" quests of the Black Shrine) from `journalquest.dbss`: 886 pages in 117 books, so chain 962 is in the list without a book.
- Client 1784 has 261 entries in 52 chains; its `journalquest.dbss` has 52 books. The 1784 list follows the 1784 `allquestlist.bss` order. 256 of the 261 entries are still in the client 3474 list; chain 11103 (5 quests) is gone. All 261 have `QuestType` 10 in the `Quest_Table` sheet of a private server's `DataSheets.bexcel` on client 1784; 219 other `QuestType` 10 rows of that sheet are not in the list. On the 256 keys that both clients share, `QuestType` 10 lines up with the live `quest_category` 11.
- [`specialquestinfo.bss`](specialquestinfo_bss.md) is a separate file with its own layout: the quest groups that `alreadyclearspecialquest(group)` action scripts name. On client 3474, 65 of its 277 quest entries are entries of this list.
