# `olviaacademy*questlist.bss` Format

## Purpose

Quest lists of the Olvia Academy windows (`panel_window_olviaacademy_main_all*.luac`, `panel_window_olviaacademy_pass_all*.luac`). Three files share one layout and one handler. Each holds exactly the [`quest.dbss`](quest_dbss.md) records of one `quest_category`, in `quest.dbss` record order:

| File                                  | quest_category | Holds                                                        |
| ------------------------------------- | -------------: | ------------------------------------------------------------ |
| `olviaacademycurriculumquestlist.bss` | `19`           | The course quests of the curriculum, chains 2308 to 2318 and 2325 |
| `olviaacademypassquestlist.bss`       | `17`           | The Olvia Academy Pass quests, chain 2324                    |
| `olviaacademyrewardquestlist.bss`     | `18`           | The family reward quests, chain 2323                         |

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, where the trailer starts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                  | Bytes | Records   | Row bytes |
| ------ | -------------- | ------- | ------------------------------------- | ----- | --------- | --------- |
| 1      | 3314 and later | 3483    | `olviaacademycurriculumquestlist.bss` | 692   | 168 Entry | 4         |
| 1      | 3144 and later | 3483    | `olviaacademypassquestlist.bss`       | 740   | 180 Entry | 4         |
| 1      | 3186 and later | 3483    | `olviaacademyrewardquestlist.bss`     | 360   | 85 Entry  | 4         |

| Layout | File                                  | Known          | Unknown    |
| ------ | ------------------------------------- | -------------- | ---------- |
| 1      | `olviaacademycurriculumquestlist.bss` | 692 B (100.0%) | 0 B (0.0%) |
| 1      | `olviaacademypassquestlist.bss`       | 740 B (100.0%) | 0 B (0.0%) |
| 1      | `olviaacademyrewardquestlist.bss`     | 360 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d126946b11e2`  |
| 3482   | Layout 1 | `d126946b11e2`  |
| 3474   | Layout 1 | `d126946b11e2`  |
| 3473   | Layout 1 | `d126946b11e2`  |
| 3464   | Layout 1 | `d126946b11e2`  |
| 3458   | Layout 1 | `d126946b11e2`  |
| 3454   | Layout 1 | `d126946b11e2`  |
| 3444   | Layout 1 | `d126946b11e2`  |
| 3435   | Layout 1 | `d126946b11e2`  |
| 3426   | Layout 1 | `d126946b11e2`  |
| 3418   | Layout 1 | `d126946b11e2`  |
| 3412   | Layout 1 | `d126946b11e2`  |
| 3402   | Layout 1 | `d126946b11e2`  |
| 3396   | Layout 1 | `d126946b11e2`  |
| 3387   | Layout 1 | `d126946b11e2`  |
| 3381   | Layout 1 | `d126946b11e2`  |
| 3373   | Layout 1 | `d126946b11e2`  |
| 3364   | Layout 1 | `d126946b11e2`  |
| 3356   | Layout 1 | `d126946b11e2`  |
| 3349   | Layout 1 | `d126946b11e2`  |
| 3342   | Layout 1 | `d126946b11e2`  |
| 3335   | Layout 1 | `d126946b11e2`  |
| 3326   | Layout 1 | `d126946b11e2`  |
| 3321   | Layout 1 | `d126946b11e2`  |
| 3314   | Layout 1 | `d126946b11e2`  |
| 3303   | Layout 1 | `d126946b11e2`  |
| 3302   | Layout 1 | `d126946b11e2`  |
| 3293   | Layout 1 | `d126946b11e2`  |
| 3283   | Layout 1 | `d126946b11e2`  |
| 3275   | Layout 1 | `d126946b11e2`  |
| 3267   | Layout 1 | `d126946b11e2`  |
| 3258   | Layout 1 | `d126946b11e2`  |
| 3251   | Layout 1 | `d126946b11e2`  |
| 3242   | Layout 1 | `d126946b11e2`  |
| 3235   | Layout 1 | `d126946b11e2`  |
| 3229   | Layout 1 | `d126946b11e2`  |
| 3212   | Layout 1 | `d126946b11e2`  |
| 3203   | Layout 1 | `d126946b11e2`  |
| 3193   | Layout 1 | `d126946b11e2`  |
| 3186   | Layout 1 | `d126946b11e2`  |
| 3177   | Layout 1 | `d126946b11e2`  |
| 3169   | Layout 1 | `d126946b11e2`  |
| 3158   | Layout 1 | `d126946b11e2`  |
| 3151   | Layout 1 | `d126946b11e2`  |
| 3144   | Layout 1 | `d126946b11e2`  |
| 3133   | No file  | `d126946b11e2`  |
| 3125   | No file  | `d126946b11e2`  |
| 3118   | No file  | `d126946b11e2`  |
| 3111   | No file  | `d126946b11e2`  |
| 3103   | No file  | `d126946b11e2`  |
| 3095   | No file  | `d126946b11e2`  |
| 3086   | No file  | `d126946b11e2`  |
| 3072   | No file  | `d126946b11e2`  |
| 3062   | No file  | `d126946b11e2`  |
| 3052   | No file  | `d126946b11e2`  |
| 3045   | No file  | `d126946b11e2`  |
| 3037   | No file  | `d126946b11e2`  |
| 3030   | No file  | `d126946b11e2`  |
| 3021   | No file  | `d126946b11e2`  |
| 3012   | No file  | `d126946b11e2`  |
| 3002   | No file  | `d126946b11e2`  |
| 2995   | No file  | `d126946b11e2`  |
| 2987   | No file  | `d126946b11e2`  |
| 2978   | No file  | `d126946b11e2`  |
| 2970   | No file  | `d126946b11e2`  |
| 2959   | No file  | `d126946b11e2`  |
| 2951   | No file  | `d126946b11e2`  |
| 2942   | No file  | `d126946b11e2`  |
| 2935   | No file  | `d126946b11e2`  |
| 2932   | No file  | `d126946b11e2`  |
| 2923   | No file  | `d126946b11e2`  |
| 2919   | No file  | `d126946b11e2`  |
| 2907   | No file  | `d126946b11e2`  |
| 2900   | No file  | `d126946b11e2`  |
| 2891   | No file  | `d126946b11e2`  |
| 2882   | No file  | `d126946b11e2`  |
| 2872   | No file  | `d126946b11e2`  |
| 2863   | No file  | `d126946b11e2`  |
| 2855   | No file  | `d126946b11e2`  |
| 2849   | No file  | `d126946b11e2`  |
| 2844   | No file  | `d126946b11e2`  |
| 2834   | No file  | `d126946b11e2`  |
| 2825   | No file  | `d126946b11e2`  |
| 2819   | No file  | `d126946b11e2`  |
| 2811   | No file  | `d126946b11e2`  |
| 2803   | No file  | `d126946b11e2`  |
| 2794   | No file  | `d126946b11e2`  |
| 2783   | No file  | `d126946b11e2`  |
| 2774   | No file  | `d126946b11e2`  |
| 2765   | No file  | `d126946b11e2`  |
| 2756   | No file  | `d126946b11e2`  |
| 2750   | No file  | `d126946b11e2`  |
| 2743   | No file  | `d126946b11e2`  |
| 2736   | No file  | `d126946b11e2`  |
| 2726   | No file  | `d126946b11e2`  |
| 2717   | No file  | `d126946b11e2`  |
| 2709   | No file  | `d126946b11e2`  |
| 2703   | No file  | `d126946b11e2`  |
| 2695   | No file  | `d126946b11e2`  |
| 2684   | No file  | `d126946b11e2`  |
| 2672   | No file  | `d126946b11e2`  |
| 2665   | No file  | `d126946b11e2`  |
| 2657   | No file  | `d126946b11e2`  |
| 2649   | No file  | `d126946b11e2`  |
| 2644   | No file  | `d126946b11e2`  |
| 2637   | No file  | `d126946b11e2`  |
| 2629   | No file  | `d126946b11e2`  |
| 2619   | No file  | `d126946b11e2`  |
| 2612   | No file  | `d126946b11e2`  |
| 2606   | No file  | `d126946b11e2`  |
| 2602   | No file  | `d126946b11e2`  |
| 2601   | No file  | `d126946b11e2`  |
| 2592   | No file  | `d126946b11e2`  |
| 2583   | No file  | `d126946b11e2`  |
| 2575   | No file  | `d126946b11e2`  |
| 2567   | No file  | `d126946b11e2`  |
| 2560   | No file  | `d126946b11e2`  |
| 2553   | No file  | `d126946b11e2`  |
| 2545   | No file  | `d126946b11e2`  |
| 2538   | No file  | `d126946b11e2`  |
| 2529   | No file  | `d126946b11e2`  |
| 2519   | No file  | `d126946b11e2`  |
| 2513   | No file  | `d126946b11e2`  |
| 2510   | No file  | `d126946b11e2`  |
| 2507   | No file  | `d126946b11e2`  |
| 2503   | No file  | `d126946b11e2`  |
| 2498   | No file  | `d126946b11e2`  |
| 2492   | No file  | `d126946b11e2`  |
| 2487   | No file  | `d126946b11e2`  |
| 2480   | No file  | `d126946b11e2`  |
| 2474   | No file  | `d126946b11e2`  |
| 2468   | No file  | `d126946b11e2`  |
| 2460   | No file  | `d126946b11e2`  |
| 2453   | No file  | `d126946b11e2`  |
| 2444   | No file  | `d126946b11e2`  |
| 2438   | No file  | `d126946b11e2`  |
| 2434   | No file  | `d126946b11e2`  |
| 2429   | No file  | `d126946b11e2`  |
| 2421   | No file  | `d126946b11e2`  |
| 2414   | No file  | `d126946b11e2`  |
| 2407   | No file  | `d126946b11e2`  |
| 2401   | No file  | `d126946b11e2`  |
| 2397   | No file  | `d126946b11e2`  |
| 2393   | No file  | `d126946b11e2`  |
| 2384   | No file  | `d126946b11e2`  |
| 2378   | No file  | `d126946b11e2`  |
| 2372   | No file  | `d126946b11e2`  |
| 2358   | No file  | `d126946b11e2`  |
| 2352   | No file  | `d126946b11e2`  |
| 2347   | No file  | `d126946b11e2`  |
| 2343   | No file  | `d126946b11e2`  |
| 2335   | No file  | `d126946b11e2`  |
| 2327   | No file  | `d126946b11e2`  |
| 2324   | No file  | `d126946b11e2`  |
| 2319   | No file  | `d126946b11e2`  |
| 2313   | No file  | `d126946b11e2`  |
| 2308   | No file  | `d126946b11e2`  |
| 2302   | No file  | `d126946b11e2`  |
| 2295   | No file  | `d126946b11e2`  |
| 2290   | No file  | `d126946b11e2`  |
| 2284   | No file  | `d126946b11e2`  |
| 2276   | No file  | `d126946b11e2`  |
| 2269   | No file  | `d126946b11e2`  |
| 2259   | No file  | `d126946b11e2`  |
| 2250   | No file  | `d126946b11e2`  |
| 2243   | No file  | `d126946b11e2`  |
| 2235   | No file  | `d126946b11e2`  |
| 2229   | No file  | `d126946b11e2`  |
| 2224   | No file  | `d126946b11e2`  |
| 2218   | No file  | `d126946b11e2`  |
| 2215   | No file  | `d126946b11e2`  |
| 2207   | No file  | `d126946b11e2`  |
| 2203   | No file  | `d126946b11e2`  |
| 2196   | No file  | `d126946b11e2`  |
| 2192   | No file  | `d126946b11e2`  |
| 2189   | No file  | `d126946b11e2`  |
| 2183   | No file  | `d126946b11e2`  |
| 2179   | No file  | `d126946b11e2`  |
| 2171   | No file  | `d126946b11e2`  |
| 2163   | No file  | `d126946b11e2`  |
| 2156   | No file  | `d126946b11e2`  |
| 2151   | No file  | `d126946b11e2`  |
| 2147   | No file  | `d126946b11e2`  |
| 2142   | No file  | `d126946b11e2`  |
| 2138   | No file  | `d126946b11e2`  |
| 2134   | No file  | `d126946b11e2`  |
| 2130   | No file  | `d126946b11e2`  |
| 2122   | No file  | `d126946b11e2`  |
| 2107   | No file  | `d126946b11e2`  |
| 2098   | No file  | `d126946b11e2`  |
| 2089   | No file  | `d126946b11e2`  |
| 2081   | No file  | `d126946b11e2`  |
| 2073   | No file  | `d126946b11e2`  |
| 2067   | No file  | `d126946b11e2`  |
| 2063   | No file  | `d126946b11e2`  |
| 2059   | No file  | `d126946b11e2`  |
| 2052   | No file  | `d126946b11e2`  |
| 2044   | No file  | `d126946b11e2`  |
| 2039   | No file  | `d126946b11e2`  |
| 2032   | No file  | `d126946b11e2`  |
| 2025   | No file  | `d126946b11e2`  |
| 2011   | No file  | `d126946b11e2`  |
| 2005   | No file  | `d126946b11e2`  |
| 2000   | No file  | `d126946b11e2`  |
| 1996   | No file  | `d126946b11e2`  |
| 1991   | No file  | `d126946b11e2`  |
| 1985   | No file  | `d126946b11e2`  |
| 1980   | No file  | `d126946b11e2`  |
| 1969   | No file  | `d126946b11e2`  |
| 1964   | No file  | `d126946b11e2`  |
| 1958   | No file  | `d126946b11e2`  |
| 1950   | No file  | `d126946b11e2`  |
| 1945   | No file  | `d126946b11e2`  |
| 1937   | No file  | `d126946b11e2`  |
| 1933   | No file  | `d126946b11e2`  |
| 1927   | No file  | `d126946b11e2`  |
| 1921   | No file  | `d126946b11e2`  |
| 1914   | No file  | `d126946b11e2`  |
| 1908   | No file  | `d126946b11e2`  |
| 1897   | No file  | `d126946b11e2`  |
| 1892   | No file  | `d126946b11e2`  |
| 1886   | No file  | `d126946b11e2`  |
| 1881   | No file  | `d126946b11e2`  |
| 1871   | No file  | `d126946b11e2`  |
| 1866   | No file  | `d126946b11e2`  |
| 1862   | No file  | `d126946b11e2`  |
| 1854   | No file  | `d126946b11e2`  |
| 1846   | No file  | `d126946b11e2`  |
| 1838   | No file  | `d126946b11e2`  |
| 1832   | No file  | `d126946b11e2`  |
| 1826   | No file  | `d126946b11e2`  |
| 1822   | No file  | `d126946b11e2`  |
| 1818   | No file  | `d126946b11e2`  |
| 1804   | No file  | `d126946b11e2`  |
| 1794   | No file  | `d126946b11e2`  |
| 1790   | No file  | `d126946b11e2`  |
| 1784   | No file  | `d126946b11e2`  |
| 1774   | No file  | `d126946b11e2`  |
| 1771   | No file  | `d126946b11e2`  |
| 1762   | No file  | `d126946b11e2`  |
| 1759   | No file  | `d126946b11e2`  |
| 1754   | No file  | `d126946b11e2`  |
| 1749   | No file  | `d126946b11e2`  |
| 1743   | No file  | `d126946b11e2`  |
| 1737   | No file  | `d126946b11e2`  |
| 1731   | No file  | `d126946b11e2`  |
| 1725   | No file  | `d126946b11e2`  |
| 1717   | No file  | `d126946b11e2`  |
| 1710   | No file  | `d126946b11e2`  |
| 1704   | No file  | `d126946b11e2`  |
| 1698   | No file  | `d126946b11e2`  |
| 1690   | No file  | `d126946b11e2`  |
| 1685   | No file  | `d126946b11e2`  |
| 1680   | No file  | `d126946b11e2`  |
| 1674   | No file  | `d126946b11e2`  |
| 1668   | No file  | `d126946b11e2`  |
| 1659   | No file  | `d126946b11e2`  |
| 1649   | No file  | `d126946b11e2`  |
| 1642   | No file  | `d126946b11e2`  |
| 1636   | No file  | `d126946b11e2`  |
| 1628   | No file  | `d126946b11e2`  |
| 1622   | No file  | `d126946b11e2`  |
| 1614   | No file  | `d126946b11e2`  |
| 1608   | No file  | `d126946b11e2`  |
| 1602   | No file  | `d126946b11e2`  |
| 1598   | No file  | `d126946b11e2`  |
| 1594   | No file  | `d126946b11e2`  |
| 1590   | No file  | `d126946b11e2`  |
| 1587   | No file  | `d126946b11e2`  |
| 1584   | No file  | `d126946b11e2`  |
| 1579   | No file  | `d126946b11e2`  |
| 1572   | No file  | `d126946b11e2`  |
| 1565   | No file  | `d126946b11e2`  |
| 1559   | No file  | `d126946b11e2`  |
| 1554   | No file  | `d126946b11e2`  |
| 1547   | No file  | `d126946b11e2`  |
| 1537   | No file  | `d126946b11e2`  |
| 1529   | No file  | `d126946b11e2`  |
| 1524   | No file  | `d126946b11e2`  |
| 1519   | No file  | `d126946b11e2`  |
| 1509   | No file  | `d126946b11e2`  |
| 1506   | No file  | `d126946b11e2`  |
| 1504   | No file  | `d126946b11e2`  |
| 1500   | No file  | `d126946b11e2`  |
| 1493   | No file  | `d126946b11e2`  |
| 1489   | No file  | `d126946b11e2`  |
| 1485   | No file  | `d126946b11e2`  |
| 1481   | No file  | `d126946b11e2`  |
| 1474   | No file  | `d126946b11e2`  |
| 1466   | No file  | `d126946b11e2`  |
| 1462   | No file  | `d126946b11e2`  |
| 1459   | No file  | `d126946b11e2`  |
| 1453   | No file  | `d126946b11e2`  |
| 1450   | No file  | `d126946b11e2`  |
| 1445   | No file  | `d126946b11e2`  |
| 1439   | No file  | `d126946b11e2`  |
| 1433   | No file  | `d126946b11e2`  |
| 1430   | No file  | `d126946b11e2`  |
| 1426   | No file  | `d126946b11e2`  |
| 1421   | No file  | `d126946b11e2`  |
| 1417   | No file  | `d126946b11e2`  |
| 1416   | No file  | `d126946b11e2`  |
| 1409   | No file  | `d126946b11e2`  |
| 1405   | No file  | `d126946b11e2`  |
| 1401   | No file  | `d126946b11e2`  |
| 1396   | No file  | `d126946b11e2`  |
| 1391   | No file  | `d126946b11e2`  |
| 1390   | No file  | `d126946b11e2`  |
| 1386   | No file  | `d126946b11e2`  |
| 1381   | No file  | `d126946b11e2`  |
| 1379   | No file  | `d126946b11e2`  |
| 1372   | No file  | `d126946b11e2`  |
| 1366   | No file  | `d126946b11e2`  |
| 1364   | No file  | `d126946b11e2`  |
| 1363   | No file  | `d126946b11e2`  |
| 1360   | No file  | `d126946b11e2`  |
| 1358   | No file  | `d126946b11e2`  |
| 1355   | No file  | `d126946b11e2`  |
| 1351   | No file  | `d126946b11e2`  |
| 1348   | No file  | `d126946b11e2`  |
| 1346   | No file  | `d126946b11e2`  |
| 1341   | No file  | `d126946b11e2`  |
| 1340   | No file  | `d126946b11e2`  |
| 1338   | No file  | `d126946b11e2`  |
| 1335   | No file  | `d126946b11e2`  |
| 1333   | No file  | `d126946b11e2`  |
| 1329   | No file  | `d126946b11e2`  |
| 1327   | No file  | `d126946b11e2`  |
| 1324   | No file  | `d126946b11e2`  |
| 1321   | No file  | `d126946b11e2`  |
| 1319   | No file  | `d126946b11e2`  |
| 1318   | No file  | `d126946b11e2`  |
| 1316   | No file  | `d126946b11e2`  |
| 1313   | No file  | `d126946b11e2`  |
| 1311   | No file  | `d126946b11e2`  |
| 1309   | No file  | `d126946b11e2`  |
| 1304   | No file  | `d126946b11e2`  |
| 1292   | No file  | `d126946b11e2`  |
| 1286   | No file  | `d126946b11e2`  |
| 1280   | No file  | `d126946b11e2`  |
| 1276   | No file  | `d126946b11e2`  |
| 1267   | No file  | `d126946b11e2`  |
| 1261   | No file  | `d126946b11e2`  |
| 1256   | No file  | `d126946b11e2`  |
| 1250   | No file  | `d126946b11e2`  |
| 1246   | No file  | `d126946b11e2`  |
| 1239   | No file  | `d126946b11e2`  |
| 1230   | No file  | `d126946b11e2`  |
| 1226   | No file  | `d126946b11e2`  |
| 1220   | No file  | `d126946b11e2`  |
| 1217   | No file  | `d126946b11e2`  |
| 1211   | No file  | `d126946b11e2`  |
| 1210   | No file  | `d126946b11e2`  |
| 1208   | No file  | `d126946b11e2`  |
| 1203   | No file  | `d126946b11e2`  |
| 1197   | No file  | `d126946b11e2`  |
| 1194   | No file  | `d126946b11e2`  |
| 1192   | No file  | `d126946b11e2`  |
| 1187   | No file  | `d126946b11e2`  |
| 1183   | No file  | `d126946b11e2`  |
| 1177   | No file  | `d126946b11e2`  |
| 1173   | No file  | `d126946b11e2`  |
| 1167   | No file  | `d126946b11e2`  |
| 1164   | No file  | `d126946b11e2`  |
| 1156   | No file  | `d126946b11e2`  |
| 1149   | No file  | `d126946b11e2`  |
| 1144   | No file  | `d126946b11e2`  |
| 1137   | No file  | `d126946b11e2`  |
| 1132   | No file  | `d126946b11e2`  |
| 1127   | No file  | `d126946b11e2`  |
| 1122   | No file  | `d126946b11e2`  |
| 1118   | No file  | `d126946b11e2`  |
| 1114   | No file  | `d126946b11e2`  |
| 1109   | No file  | `d126946b11e2`  |
| 1102   | No file  | `d126946b11e2`  |
| 1096   | No file  | `d126946b11e2`  |
| 1088   | No file  | `d126946b11e2`  |
| 1081   | No file  | `d126946b11e2`  |
| 1076   | No file  | `d126946b11e2`  |
| 1069   | No file  | `d126946b11e2`  |
| 1064   | No file  | `d126946b11e2`  |
| 1058   | No file  | `d126946b11e2`  |
| 1051   | No file  | `d126946b11e2`  |
| 1044   | No file  | `d126946b11e2`  |
| 1036   | No file  | `d126946b11e2`  |
| 1026   | No file  | `d126946b11e2`  |
| 1016   | No file  | `d126946b11e2`  |
| 1009   | No file  | `d126946b11e2`  |
| 1005   | No file  | `d126946b11e2`  |
| 1000   | No file  | `d126946b11e2`  |
| 998    | No file  | `d126946b11e2`  |
| 990    | No file  | `d126946b11e2`  |
| 979    | No file  | `d126946b11e2`  |
| 972    | No file  | `d126946b11e2`  |
| 963    | No file  | `d126946b11e2`  |
| 955    | No file  | `d126946b11e2`  |
| 946    | No file  | `d126946b11e2`  |
| 938    | No file  | `d126946b11e2`  |
| 927    | No file  | `d126946b11e2`  |
| 911    | No file  | `d126946b11e2`  |
| 904    | No file  | `d126946b11e2`  |
| 899    | No file  | `d126946b11e2`  |
| 894    | No file  | `d126946b11e2`  |
| 885    | No file  | `d126946b11e2`  |
| 879    | No file  | `d126946b11e2`  |
| 872    | No file  | `d126946b11e2`  |
| 864    | No file  | `d126946b11e2`  |
| 855    | No file  | `d126946b11e2`  |
| 853    | No file  | `d126946b11e2`  |
| 845    | No file  | `d126946b11e2`  |
| 837    | No file  | `d126946b11e2`  |
| 829    | No file  | `d126946b11e2`  |
| 822    | No file  | `d126946b11e2`  |
| 814    | No file  | `d126946b11e2`  |
| 805    | No file  | `d126946b11e2`  |
| 794    | No file  | `d126946b11e2`  |
| 787    | No file  | `d126946b11e2`  |
| 780    | No file  | `d126946b11e2`  |
| 771    | No file  | `d126946b11e2`  |
| 760    | No file  | `d126946b11e2`  |
| 748    | No file  | `d126946b11e2`  |
| 741    | No file  | `d126946b11e2`  |
| 736    | No file  | `d126946b11e2`  |
| 731    | No file  | `d126946b11e2`  |
| 723    | No file  | `d126946b11e2`  |
| 711    | No file  | `d126946b11e2`  |
| 707    | No file  | `d126946b11e2`  |
| 697    | No file  | `d126946b11e2`  |
| 689    | No file  | `d126946b11e2`  |
| 683    | No file  | `d126946b11e2`  |
| 678    | No file  | `d126946b11e2`  |
| 670    | No file  | `d126946b11e2`  |
| 661    | No file  | `d126946b11e2`  |
| 656    | No file  | `d126946b11e2`  |
| 652    | No file  | `d126946b11e2`  |
| 643    | No file  | `d126946b11e2`  |
| 637    | No file  | `d126946b11e2`  |
| 630    | No file  | `d126946b11e2`  |
| 627    | No file  | `d126946b11e2`  |
| 621    | No file  | `d126946b11e2`  |
| 617    | No file  | `d126946b11e2`  |
| 615    | No file  | `d126946b11e2`  |
| 606    | No file  | `d126946b11e2`  |
| 599    | No file  | `d126946b11e2`  |
| 592    | No file  | `d126946b11e2`  |
| 586    | No file  | `d126946b11e2`  |
| 577    | No file  | `d126946b11e2`  |
| 569    | No file  | `d126946b11e2`  |
| 561    | No file  | `d126946b11e2`  |
| 554    | No file  | `d126946b11e2`  |
| 542    | No file  | `d126946b11e2`  |
| 532    | No file  | `d126946b11e2`  |
| 531    | No file  | `d126946b11e2`  |
| 526    | No file  | `d126946b11e2`  |
| 521    | No file  | `d126946b11e2`  |
| 517    | No file  | `d126946b11e2`  |
| 510    | No file  | `d126946b11e2`  |
| 508    | No file  | `d126946b11e2`  |
| 504    | No file  | `d126946b11e2`  |
| 497    | No file  | `d126946b11e2`  |
| 491    | No file  | `d126946b11e2`  |
| 485    | No file  | `d126946b11e2`  |
| 478    | No file  | `d126946b11e2`  |
| 472    | No file  | `d126946b11e2`  |
| 466    | No file  | `d126946b11e2`  |
| 457    | No file  | `d126946b11e2`  |
| 452    | No file  | `d126946b11e2`  |
| 449    | No file  | `d126946b11e2`  |
| 435    | No file  | `d126946b11e2`  |

<!-- versions:end -->

## Companion Files

The same as [`allquestlist.bss`](allquestlist_bss.md).

All multi-byte values are little-endian.

## Curriculum Quests

`olviaacademycurriculumquestlist.bss` on client 3474: 168 quests in twelve chains. The title tag names the course. Each course runs from sub ID 1 (`Sign Up for ...`) to its `Course Completed` quest; the 24 `Material Support` and `Ship Support` quests sit at sub IDs 53 to 62.

| Chain | Title tag            | Quests | Sub IDs              |
| ----: | -------------------- | -----: | -------------------- |
| 2308  | `[Olvia Academy]`    | 1      | 1 (Your First Steps In) |
| 2309  | `[Olvia Academy]`    | 1      | 1 (Graduation with Honor) |
| 2310  | `[Combat Course]`    | 31     | 1 to 32, no 19       |
| 2311  | `[Alchemy Course]`   | 18     | 1 to 12, six from 54 to 61 |
| 2312  | `[Training Course]`  | 14     | 1 to 14              |
| 2313  | `[Cooking Course]`   | 19     | 1 to 13, six from 54 to 62 |
| 2314  | `[Hunting Course]`   | 14     | 1 to 13, 53          |
| 2315  | `[Sailing Course]`   | 15     | 1 to 13, 53, 56      |
| 2316  | `[Fishing Course]`   | 14     | 1 to 13, 53          |
| 2317  | `[Processing Course]`| 17     | 1 to 11, 53 to 58    |
| 2318  | `[Farming Course]`   | 14     | 1 to 12, 58, 60      |
| 2325  | `[Gathering Course]` | 10     | 1 to 10              |

Chains 2321 and 2322 (`[Academy] [Weekly ...]` quests, 38 in `allquestlist.bss`) are in none of the three lists.

## Pass Quests

`olviaacademypassquestlist.bss` on client 3474: 180 quests, all in chain 2324. The hundreds digit of the sub ID is the pass tab. Each tab has ten steps; step `n` is the base quest at sub ID `x00 + 2n - 1` and the pass quest at `x00 + 2n`. Every pass quest title ends in `(Olvia Academy Pass)` and no base quest title does. The tabs follow the order in which `panel_window_olviaacademy_pass_all.luac` lists the `__eOlviaAcademyPassType_*` values:

| Sub IDs    | Pass type (Lua)                    | Title          |
| ---------- | ---------------------------------- | -------------- |
| 101 to 120 | `__eOlviaAcademyPassType_Collect`  | Gathering Time! `n`. |
| 201 to 220 | `__eOlviaAcademyPassType_Fish`     | Hands-On Fishing! `n`. |
| 301 to 320 | `__eOlviaAcademyPassType_Hunt`     | Happy Hunting! `n`. |
| 401 to 420 | `__eOlviaAcademyPassType_Cook`     | Win Them Over with Cooking! `n`. |
| 501 to 520 | `__eOlviaAcademyPassType_Alchemy`  | Hands-On Alchemy! `n`. |
| 601 to 620 | `__eOlviaAcademyPassType_Work`     | Processing in Progress! `n`. |
| 701 to 720 | `__eOlviaAcademyPassType_Train`    | Hands-On Training! `n`. |
| 801 to 820 | `__eOlviaAcademyPassType_Farm`     | Fantastic Farming! `n`. |
| 901 to 920 | `__eOlviaAcademyPassType_Ship`     | Hands-On Sailing! `n`. |

`panel_window_olviaacademy_pass_all_1.luac` asks for each row with `ToClient_GetOlviaAcademyQuest(passType, questIndex, __eOlviaAcademyPassQuestType_Base)` and `..._Pass`, and shows the pass quest's reward as locked while `ToClient_HasOlviaAcademyPass(passType)` is false. The file order is not the step order.

## Family Reward Quests

`olviaacademyrewardquestlist.bss` on client 3474: 85 quests, all in chain 2323. Every title is `[Olvia Academy] <Family> Family Reward`, and each family has its own sub ID block:

| Sub IDs    | Title                     | Quests |
| ---------- | ------------------------- | -----: |
| 1 to 36    | Combat Family Reward      | 36     |
| 101 to 106 | Gathering Family Reward   | 6      |
| 111 to 116 | Cooking Family Reward     | 6      |
| 121 to 126 | Alchemy Family Reward     | 6      |
| 131 to 135 | Training Family Reward    | 5      |
| 141 to 145 | Hunting Family Reward     | 5      |
| 151 to 155 | Sailing Family Reward     | 5      |
| 161 to 166 | Fishing Family Reward     | 6      |
| 171 to 175 | Processing Family Reward  | 5      |
| 181 to 185 | Farming Family Reward     | 5      |

Quest 201 of chain 2323 (`Finest First Impression`) is `quest_category` 2 and not in the list.

## Notes

- Decompressed sizes on client 3474: `692` bytes for the curriculum list (168 quests), `740` for the pass list (180), `360` for the reward list (85); all match `8 + count * 4 + 12`.
- Every quest of the three lists is in `allquestlist.bss` and has a LOC type 18 title (client 3474).
- The test client 1784 has none of the three files.
- The pass step order is in
  [`olviaacademypassstaticstatusmanager.bss`](olviaacademypassstaticstatusmanager_bss.md):
  per pass tab the base and pass quest of each step. Its 180 quests are
  exactly the pass list (client 3482).
- The subjects and family reward groups are in
  [`olviaacademycurriculumss.bss`](olviaacademycurriculumss_bss.md). Its 142
  subject quests are all in the curriculum list, which holds 26 more
  (`2308/1`, `2309/1` and the 24 support quests); its 85 reward group quests
  are exactly the reward list (client 3482).
- The current class, its dates and its enrollment and graduation quests
  are in [`olviaacademyseasonss.bss`](olviaacademyseasonss_bss.md).
- The handler adds a place column to the three lists: the curriculum and
  subject (`Combat / Basic Tactics`) or family reward and group of each
  quest from `olviaacademycurriculumss.bss`, the pass type and step
  (`Collect / 1`) from `olviaacademypassstaticstatusmanager.bss`. The place
  links to its row there; a quest no academy table holds shows `-`.
- `test_olvia_academy_lists.py` asserts that each list is its `quest_category` in `quest.dbss` record order, that every pass base quest has its pass quest at sub ID + 1, and that every quest of a subject, reward group or pass step gets that place.

## Open Questions

### What Reads the Lists

No Lua reads the three lists by name. What the windows read matches the two academy tables getter for getter: the main window's curriculum, subject, reward and reward group getters are the fields of [`olviaacademycurriculumss.bss`](olviaacademycurriculumss_bss.md), and the pass window's `ToClient_GetOlviaAcademyPassSize(passType)` and `ToClient_GetOlviaAcademyQuest(passType, questIndex, ...)` those of [`olviaacademypassstaticstatusmanager.bss`](olviaacademypassstaticstatusmanager_bss.md). What the client uses the lists for is open; the curriculum list holds 26 quests no subject names, so it is not only a copy of the subjects.
