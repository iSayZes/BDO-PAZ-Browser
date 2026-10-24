# `acceptquest.bss` Format

## Purpose

The NPC dialog that gives each quest: one 8-byte row per quest with the quest key, the NPC's character key and the dialog index. `dialog_index << 16 | npc_id` is the `detail_dialog.dbss` key of the dialog, and the same value is `accept_dialog_key` at `+0x00` of the quest's `quest.dbss` record. [completequest_bss.md](completequest_bss.md) has the same layout for the dialog that takes the quest.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes   | Records                 | Row bytes |
| ------ | -------------- | ------- | ----------------- | ------- | ----------------------- | --------- |
| 1      | 1109 and later | 3483    | `acceptquest.bss` | 151,948 | 18,991 Accept Quest Row | 8         |

| Layout | File              | Known              | Unknown    |
| ------ | ----------------- | ------------------ | ---------- |
| 1      | `acceptquest.bss` | 151,948 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `2b3b09a245be`  |
| 3482   | Layout 1 | `2b3b09a245be`  |
| 3474   | Layout 1 | `2b3b09a245be`  |
| 3473   | Layout 1 | `2b3b09a245be`  |
| 3464   | Layout 1 | `2b3b09a245be`  |
| 3458   | Layout 1 | `2b3b09a245be`  |
| 3454   | Layout 1 | `2b3b09a245be`  |
| 3444   | Layout 1 | `2b3b09a245be`  |
| 3435   | Layout 1 | `2b3b09a245be`  |
| 3426   | Layout 1 | `2b3b09a245be`  |
| 3418   | Layout 1 | `2b3b09a245be`  |
| 3412   | Layout 1 | `2b3b09a245be`  |
| 3402   | Layout 1 | `2b3b09a245be`  |
| 3396   | Layout 1 | `2b3b09a245be`  |
| 3387   | Layout 1 | `2b3b09a245be`  |
| 3381   | Layout 1 | `2b3b09a245be`  |
| 3373   | Layout 1 | `2b3b09a245be`  |
| 3364   | Layout 1 | `2b3b09a245be`  |
| 3356   | Layout 1 | `2b3b09a245be`  |
| 3349   | Layout 1 | `2b3b09a245be`  |
| 3342   | Layout 1 | `2b3b09a245be`  |
| 3335   | Layout 1 | `2b3b09a245be`  |
| 3326   | Layout 1 | `2b3b09a245be`  |
| 3321   | Layout 1 | `2b3b09a245be`  |
| 3314   | Layout 1 | `2b3b09a245be`  |
| 3303   | Layout 1 | `2b3b09a245be`  |
| 3302   | Layout 1 | `2b3b09a245be`  |
| 3293   | Layout 1 | `2b3b09a245be`  |
| 3283   | Layout 1 | `2b3b09a245be`  |
| 3275   | Layout 1 | `2b3b09a245be`  |
| 3267   | Layout 1 | `2b3b09a245be`  |
| 3258   | Layout 1 | `2b3b09a245be`  |
| 3251   | Layout 1 | `2b3b09a245be`  |
| 3242   | Layout 1 | `2b3b09a245be`  |
| 3235   | Layout 1 | `2b3b09a245be`  |
| 3229   | Layout 1 | `2b3b09a245be`  |
| 3212   | Layout 1 | `2b3b09a245be`  |
| 3203   | Layout 1 | `2b3b09a245be`  |
| 3193   | Layout 1 | `2b3b09a245be`  |
| 3186   | Layout 1 | `2b3b09a245be`  |
| 3177   | Layout 1 | `2b3b09a245be`  |
| 3169   | Layout 1 | `2b3b09a245be`  |
| 3158   | Layout 1 | `2b3b09a245be`  |
| 3151   | Layout 1 | `2b3b09a245be`  |
| 3144   | Layout 1 | `2b3b09a245be`  |
| 3133   | Layout 1 | `2b3b09a245be`  |
| 3125   | Layout 1 | `2b3b09a245be`  |
| 3118   | Layout 1 | `2b3b09a245be`  |
| 3111   | Layout 1 | `2b3b09a245be`  |
| 3103   | Layout 1 | `2b3b09a245be`  |
| 3095   | Layout 1 | `2b3b09a245be`  |
| 3086   | Layout 1 | `2b3b09a245be`  |
| 3072   | Layout 1 | `2b3b09a245be`  |
| 3062   | Layout 1 | `2b3b09a245be`  |
| 3052   | Layout 1 | `2b3b09a245be`  |
| 3045   | Layout 1 | `2b3b09a245be`  |
| 3037   | Layout 1 | `2b3b09a245be`  |
| 3030   | Layout 1 | `2b3b09a245be`  |
| 3021   | Layout 1 | `2b3b09a245be`  |
| 3012   | Layout 1 | `2b3b09a245be`  |
| 3002   | Layout 1 | `2b3b09a245be`  |
| 2995   | Layout 1 | `2b3b09a245be`  |
| 2987   | Layout 1 | `2b3b09a245be`  |
| 2978   | Layout 1 | `2b3b09a245be`  |
| 2970   | Layout 1 | `2b3b09a245be`  |
| 2959   | Layout 1 | `2b3b09a245be`  |
| 2951   | Layout 1 | `2b3b09a245be`  |
| 2942   | Layout 1 | `2b3b09a245be`  |
| 2935   | Layout 1 | `2b3b09a245be`  |
| 2932   | Layout 1 | `2b3b09a245be`  |
| 2923   | Layout 1 | `2b3b09a245be`  |
| 2919   | Layout 1 | `2b3b09a245be`  |
| 2907   | Layout 1 | `2b3b09a245be`  |
| 2900   | Layout 1 | `2b3b09a245be`  |
| 2891   | Layout 1 | `2b3b09a245be`  |
| 2882   | Layout 1 | `2b3b09a245be`  |
| 2872   | Layout 1 | `2b3b09a245be`  |
| 2863   | Layout 1 | `2b3b09a245be`  |
| 2855   | Layout 1 | `2b3b09a245be`  |
| 2849   | Layout 1 | `2b3b09a245be`  |
| 2844   | Layout 1 | `2b3b09a245be`  |
| 2834   | Layout 1 | `2b3b09a245be`  |
| 2825   | Layout 1 | `2b3b09a245be`  |
| 2819   | Layout 1 | `2b3b09a245be`  |
| 2811   | Layout 1 | `2b3b09a245be`  |
| 2803   | Layout 1 | `2b3b09a245be`  |
| 2794   | Layout 1 | `2b3b09a245be`  |
| 2783   | Layout 1 | `2b3b09a245be`  |
| 2774   | Layout 1 | `2b3b09a245be`  |
| 2765   | Layout 1 | `2b3b09a245be`  |
| 2756   | Layout 1 | `2b3b09a245be`  |
| 2750   | Layout 1 | `2b3b09a245be`  |
| 2743   | Layout 1 | `2b3b09a245be`  |
| 2736   | Layout 1 | `2b3b09a245be`  |
| 2726   | Layout 1 | `2b3b09a245be`  |
| 2717   | Layout 1 | `2b3b09a245be`  |
| 2709   | Layout 1 | `2b3b09a245be`  |
| 2703   | Layout 1 | `2b3b09a245be`  |
| 2695   | Layout 1 | `2b3b09a245be`  |
| 2684   | Layout 1 | `2b3b09a245be`  |
| 2672   | Layout 1 | `2b3b09a245be`  |
| 2665   | Layout 1 | `2b3b09a245be`  |
| 2657   | Layout 1 | `2b3b09a245be`  |
| 2649   | Layout 1 | `2b3b09a245be`  |
| 2644   | Layout 1 | `2b3b09a245be`  |
| 2637   | Layout 1 | `2b3b09a245be`  |
| 2629   | Layout 1 | `2b3b09a245be`  |
| 2619   | Layout 1 | `2b3b09a245be`  |
| 2612   | Layout 1 | `2b3b09a245be`  |
| 2606   | Layout 1 | `2b3b09a245be`  |
| 2602   | Layout 1 | `2b3b09a245be`  |
| 2601   | Layout 1 | `2b3b09a245be`  |
| 2592   | Layout 1 | `2b3b09a245be`  |
| 2583   | Layout 1 | `2b3b09a245be`  |
| 2575   | Layout 1 | `2b3b09a245be`  |
| 2567   | Layout 1 | `2b3b09a245be`  |
| 2560   | Layout 1 | `2b3b09a245be`  |
| 2553   | Layout 1 | `2b3b09a245be`  |
| 2545   | Layout 1 | `2b3b09a245be`  |
| 2538   | Layout 1 | `2b3b09a245be`  |
| 2529   | Layout 1 | `2b3b09a245be`  |
| 2519   | Layout 1 | `2b3b09a245be`  |
| 2513   | Layout 1 | `2b3b09a245be`  |
| 2510   | Layout 1 | `2b3b09a245be`  |
| 2507   | Layout 1 | `2b3b09a245be`  |
| 2503   | Layout 1 | `2b3b09a245be`  |
| 2498   | Layout 1 | `2b3b09a245be`  |
| 2492   | Layout 1 | `2b3b09a245be`  |
| 2487   | Layout 1 | `2b3b09a245be`  |
| 2480   | Layout 1 | `2b3b09a245be`  |
| 2474   | Layout 1 | `2b3b09a245be`  |
| 2468   | Layout 1 | `2b3b09a245be`  |
| 2460   | Layout 1 | `2b3b09a245be`  |
| 2453   | Layout 1 | `2b3b09a245be`  |
| 2444   | Layout 1 | `2b3b09a245be`  |
| 2438   | Layout 1 | `2b3b09a245be`  |
| 2434   | Layout 1 | `2b3b09a245be`  |
| 2429   | Layout 1 | `2b3b09a245be`  |
| 2421   | Layout 1 | `2b3b09a245be`  |
| 2414   | Layout 1 | `2b3b09a245be`  |
| 2407   | Layout 1 | `2b3b09a245be`  |
| 2401   | Layout 1 | `2b3b09a245be`  |
| 2397   | Layout 1 | `2b3b09a245be`  |
| 2393   | Layout 1 | `2b3b09a245be`  |
| 2384   | Layout 1 | `2b3b09a245be`  |
| 2378   | Layout 1 | `2b3b09a245be`  |
| 2372   | Layout 1 | `2b3b09a245be`  |
| 2358   | Layout 1 | `2b3b09a245be`  |
| 2352   | Layout 1 | `2b3b09a245be`  |
| 2347   | Layout 1 | `2b3b09a245be`  |
| 2343   | Layout 1 | `2b3b09a245be`  |
| 2335   | Layout 1 | `2b3b09a245be`  |
| 2327   | Layout 1 | `2b3b09a245be`  |
| 2324   | Layout 1 | `2b3b09a245be`  |
| 2319   | Layout 1 | `2b3b09a245be`  |
| 2313   | Layout 1 | `2b3b09a245be`  |
| 2308   | Layout 1 | `2b3b09a245be`  |
| 2302   | Layout 1 | `2b3b09a245be`  |
| 2295   | Layout 1 | `2b3b09a245be`  |
| 2290   | Layout 1 | `2b3b09a245be`  |
| 2284   | Layout 1 | `2b3b09a245be`  |
| 2276   | Layout 1 | `2b3b09a245be`  |
| 2269   | Layout 1 | `2b3b09a245be`  |
| 2259   | Layout 1 | `2b3b09a245be`  |
| 2250   | Layout 1 | `2b3b09a245be`  |
| 2243   | Layout 1 | `2b3b09a245be`  |
| 2235   | Layout 1 | `2b3b09a245be`  |
| 2229   | Layout 1 | `2b3b09a245be`  |
| 2224   | Layout 1 | `2b3b09a245be`  |
| 2218   | Layout 1 | `2b3b09a245be`  |
| 2215   | Layout 1 | `2b3b09a245be`  |
| 2207   | Layout 1 | `2b3b09a245be`  |
| 2203   | Layout 1 | `2b3b09a245be`  |
| 2196   | Layout 1 | `2b3b09a245be`  |
| 2192   | Layout 1 | `2b3b09a245be`  |
| 2189   | Layout 1 | `2b3b09a245be`  |
| 2183   | Layout 1 | `2b3b09a245be`  |
| 2179   | Layout 1 | `2b3b09a245be`  |
| 2171   | Layout 1 | `2b3b09a245be`  |
| 2163   | Layout 1 | `2b3b09a245be`  |
| 2156   | Layout 1 | `2b3b09a245be`  |
| 2151   | Layout 1 | `2b3b09a245be`  |
| 2147   | Layout 1 | `2b3b09a245be`  |
| 2142   | Layout 1 | `2b3b09a245be`  |
| 2138   | Layout 1 | `2b3b09a245be`  |
| 2134   | Layout 1 | `2b3b09a245be`  |
| 2130   | Layout 1 | `2b3b09a245be`  |
| 2122   | Layout 1 | `2b3b09a245be`  |
| 2107   | Layout 1 | `2b3b09a245be`  |
| 2098   | Layout 1 | `2b3b09a245be`  |
| 2089   | Layout 1 | `2b3b09a245be`  |
| 2081   | Layout 1 | `2b3b09a245be`  |
| 2073   | Layout 1 | `2b3b09a245be`  |
| 2067   | Layout 1 | `2b3b09a245be`  |
| 2063   | Layout 1 | `2b3b09a245be`  |
| 2059   | Layout 1 | `2b3b09a245be`  |
| 2052   | Layout 1 | `2b3b09a245be`  |
| 2044   | Layout 1 | `2b3b09a245be`  |
| 2039   | Layout 1 | `2b3b09a245be`  |
| 2032   | Layout 1 | `2b3b09a245be`  |
| 2025   | Layout 1 | `2b3b09a245be`  |
| 2011   | Layout 1 | `2b3b09a245be`  |
| 2005   | Layout 1 | `2b3b09a245be`  |
| 2000   | Layout 1 | `2b3b09a245be`  |
| 1996   | Layout 1 | `2b3b09a245be`  |
| 1991   | Layout 1 | `2b3b09a245be`  |
| 1985   | Layout 1 | `2b3b09a245be`  |
| 1980   | Layout 1 | `2b3b09a245be`  |
| 1969   | Layout 1 | `2b3b09a245be`  |
| 1964   | Layout 1 | `2b3b09a245be`  |
| 1958   | Layout 1 | `2b3b09a245be`  |
| 1950   | Layout 1 | `2b3b09a245be`  |
| 1945   | Layout 1 | `2b3b09a245be`  |
| 1937   | Layout 1 | `2b3b09a245be`  |
| 1933   | Layout 1 | `2b3b09a245be`  |
| 1927   | Layout 1 | `2b3b09a245be`  |
| 1921   | Layout 1 | `2b3b09a245be`  |
| 1914   | Layout 1 | `2b3b09a245be`  |
| 1908   | Layout 1 | `2b3b09a245be`  |
| 1897   | Layout 1 | `2b3b09a245be`  |
| 1892   | Layout 1 | `2b3b09a245be`  |
| 1886   | Layout 1 | `2b3b09a245be`  |
| 1881   | Layout 1 | `2b3b09a245be`  |
| 1871   | Layout 1 | `2b3b09a245be`  |
| 1866   | Layout 1 | `2b3b09a245be`  |
| 1862   | Layout 1 | `2b3b09a245be`  |
| 1854   | Layout 1 | `2b3b09a245be`  |
| 1846   | Layout 1 | `2b3b09a245be`  |
| 1838   | Layout 1 | `2b3b09a245be`  |
| 1832   | Layout 1 | `2b3b09a245be`  |
| 1826   | Layout 1 | `2b3b09a245be`  |
| 1822   | Layout 1 | `2b3b09a245be`  |
| 1818   | Layout 1 | `2b3b09a245be`  |
| 1804   | Layout 1 | `2b3b09a245be`  |
| 1794   | Layout 1 | `2b3b09a245be`  |
| 1790   | Layout 1 | `2b3b09a245be`  |
| 1784   | Layout 1 | `2b3b09a245be`  |
| 1774   | Layout 1 | `2b3b09a245be`  |
| 1771   | Layout 1 | `2b3b09a245be`  |
| 1762   | Layout 1 | `2b3b09a245be`  |
| 1759   | Layout 1 | `2b3b09a245be`  |
| 1754   | Layout 1 | `2b3b09a245be`  |
| 1749   | Layout 1 | `2b3b09a245be`  |
| 1743   | Layout 1 | `2b3b09a245be`  |
| 1737   | Layout 1 | `2b3b09a245be`  |
| 1731   | Layout 1 | `2b3b09a245be`  |
| 1725   | Layout 1 | `2b3b09a245be`  |
| 1717   | Layout 1 | `2b3b09a245be`  |
| 1710   | Layout 1 | `2b3b09a245be`  |
| 1704   | Layout 1 | `2b3b09a245be`  |
| 1698   | Layout 1 | `2b3b09a245be`  |
| 1690   | Layout 1 | `2b3b09a245be`  |
| 1685   | Layout 1 | `2b3b09a245be`  |
| 1680   | Layout 1 | `2b3b09a245be`  |
| 1674   | Layout 1 | `2b3b09a245be`  |
| 1668   | Layout 1 | `2b3b09a245be`  |
| 1659   | Layout 1 | `2b3b09a245be`  |
| 1649   | Layout 1 | `2b3b09a245be`  |
| 1642   | Layout 1 | `2b3b09a245be`  |
| 1636   | Layout 1 | `2b3b09a245be`  |
| 1628   | Layout 1 | `2b3b09a245be`  |
| 1622   | Layout 1 | `2b3b09a245be`  |
| 1614   | Layout 1 | `2b3b09a245be`  |
| 1608   | Layout 1 | `2b3b09a245be`  |
| 1602   | Layout 1 | `2b3b09a245be`  |
| 1598   | Layout 1 | `2b3b09a245be`  |
| 1594   | Layout 1 | `2b3b09a245be`  |
| 1590   | Layout 1 | `2b3b09a245be`  |
| 1587   | Layout 1 | `2b3b09a245be`  |
| 1584   | Layout 1 | `2b3b09a245be`  |
| 1579   | Layout 1 | `2b3b09a245be`  |
| 1572   | Layout 1 | `2b3b09a245be`  |
| 1565   | Layout 1 | `2b3b09a245be`  |
| 1559   | Layout 1 | `2b3b09a245be`  |
| 1554   | Layout 1 | `2b3b09a245be`  |
| 1547   | Layout 1 | `2b3b09a245be`  |
| 1537   | Layout 1 | `2b3b09a245be`  |
| 1529   | Layout 1 | `2b3b09a245be`  |
| 1524   | Layout 1 | `2b3b09a245be`  |
| 1519   | Layout 1 | `2b3b09a245be`  |
| 1509   | Layout 1 | `2b3b09a245be`  |
| 1506   | Layout 1 | `2b3b09a245be`  |
| 1504   | Layout 1 | `2b3b09a245be`  |
| 1500   | Layout 1 | `2b3b09a245be`  |
| 1493   | Layout 1 | `2b3b09a245be`  |
| 1489   | Layout 1 | `2b3b09a245be`  |
| 1485   | Layout 1 | `2b3b09a245be`  |
| 1481   | Layout 1 | `2b3b09a245be`  |
| 1474   | Layout 1 | `2b3b09a245be`  |
| 1466   | Layout 1 | `2b3b09a245be`  |
| 1462   | Layout 1 | `2b3b09a245be`  |
| 1459   | Layout 1 | `2b3b09a245be`  |
| 1453   | Layout 1 | `2b3b09a245be`  |
| 1450   | Layout 1 | `2b3b09a245be`  |
| 1445   | Layout 1 | `2b3b09a245be`  |
| 1439   | Layout 1 | `2b3b09a245be`  |
| 1433   | Layout 1 | `2b3b09a245be`  |
| 1430   | Layout 1 | `2b3b09a245be`  |
| 1426   | Layout 1 | `2b3b09a245be`  |
| 1421   | Layout 1 | `2b3b09a245be`  |
| 1417   | Layout 1 | `2b3b09a245be`  |
| 1416   | Layout 1 | `2b3b09a245be`  |
| 1409   | Layout 1 | `2b3b09a245be`  |
| 1405   | Layout 1 | `2b3b09a245be`  |
| 1401   | Layout 1 | `2b3b09a245be`  |
| 1396   | Layout 1 | `2b3b09a245be`  |
| 1391   | Layout 1 | `2b3b09a245be`  |
| 1390   | Layout 1 | `2b3b09a245be`  |
| 1386   | Layout 1 | `2b3b09a245be`  |
| 1381   | Layout 1 | `2b3b09a245be`  |
| 1379   | Layout 1 | `2b3b09a245be`  |
| 1372   | Layout 1 | `2b3b09a245be`  |
| 1366   | Layout 1 | `2b3b09a245be`  |
| 1364   | Layout 1 | `2b3b09a245be`  |
| 1363   | Layout 1 | `2b3b09a245be`  |
| 1360   | Layout 1 | `2b3b09a245be`  |
| 1358   | Layout 1 | `2b3b09a245be`  |
| 1355   | Layout 1 | `2b3b09a245be`  |
| 1351   | Layout 1 | `2b3b09a245be`  |
| 1348   | Layout 1 | `2b3b09a245be`  |
| 1346   | Layout 1 | `2b3b09a245be`  |
| 1341   | Layout 1 | `2b3b09a245be`  |
| 1340   | Layout 1 | `2b3b09a245be`  |
| 1338   | Layout 1 | `2b3b09a245be`  |
| 1335   | Layout 1 | `2b3b09a245be`  |
| 1333   | Layout 1 | `2b3b09a245be`  |
| 1329   | Layout 1 | `2b3b09a245be`  |
| 1327   | Layout 1 | `2b3b09a245be`  |
| 1324   | Layout 1 | `2b3b09a245be`  |
| 1321   | Layout 1 | `2b3b09a245be`  |
| 1319   | Layout 1 | `2b3b09a245be`  |
| 1318   | Layout 1 | `2b3b09a245be`  |
| 1316   | Layout 1 | `2b3b09a245be`  |
| 1313   | Layout 1 | `2b3b09a245be`  |
| 1311   | Layout 1 | `2b3b09a245be`  |
| 1309   | Layout 1 | `2b3b09a245be`  |
| 1304   | Layout 1 | `2b3b09a245be`  |
| 1292   | Layout 1 | `2b3b09a245be`  |
| 1286   | Layout 1 | `2b3b09a245be`  |
| 1280   | Layout 1 | `2b3b09a245be`  |
| 1276   | Layout 1 | `2b3b09a245be`  |
| 1267   | Layout 1 | `2b3b09a245be`  |
| 1261   | Layout 1 | `2b3b09a245be`  |
| 1256   | Layout 1 | `2b3b09a245be`  |
| 1250   | Layout 1 | `2b3b09a245be`  |
| 1246   | No file  | `2b3b09a245be`  |
| 1239   | No file  | `2b3b09a245be`  |
| 1230   | No file  | `2b3b09a245be`  |
| 1226   | No file  | `2b3b09a245be`  |
| 1220   | No file  | `2b3b09a245be`  |
| 1217   | No file  | `2b3b09a245be`  |
| 1211   | No file  | `2b3b09a245be`  |
| 1210   | No file  | `2b3b09a245be`  |
| 1208   | No file  | `2b3b09a245be`  |
| 1203   | No file  | `2b3b09a245be`  |
| 1197   | No file  | `2b3b09a245be`  |
| 1194   | No file  | `2b3b09a245be`  |
| 1192   | No file  | `2b3b09a245be`  |
| 1187   | No file  | `2b3b09a245be`  |
| 1183   | No file  | `2b3b09a245be`  |
| 1177   | No file  | `2b3b09a245be`  |
| 1173   | No file  | `2b3b09a245be`  |
| 1167   | No file  | `2b3b09a245be`  |
| 1164   | No file  | `2b3b09a245be`  |
| 1156   | No file  | `2b3b09a245be`  |
| 1149   | No file  | `2b3b09a245be`  |
| 1144   | Layout 1 | `2b3b09a245be`  |
| 1137   | Layout 1 | `2b3b09a245be`  |
| 1132   | Layout 1 | `2b3b09a245be`  |
| 1127   | Layout 1 | `2b3b09a245be`  |
| 1122   | Layout 1 | `2b3b09a245be`  |
| 1118   | Layout 1 | `2b3b09a245be`  |
| 1114   | Layout 1 | `2b3b09a245be`  |
| 1109   | Layout 1 | `2b3b09a245be`  |
| 1102   | No file  | `2b3b09a245be`  |
| 1096   | No file  | `2b3b09a245be`  |
| 1088   | No file  | `2b3b09a245be`  |
| 1081   | No file  | `2b3b09a245be`  |
| 1076   | No file  | `2b3b09a245be`  |
| 1069   | No file  | `2b3b09a245be`  |
| 1064   | No file  | `2b3b09a245be`  |
| 1058   | No file  | `2b3b09a245be`  |
| 1051   | No file  | `2b3b09a245be`  |
| 1044   | No file  | `2b3b09a245be`  |
| 1036   | No file  | `2b3b09a245be`  |
| 1026   | No file  | `2b3b09a245be`  |
| 1016   | No file  | `2b3b09a245be`  |
| 1009   | No file  | `2b3b09a245be`  |
| 1005   | No file  | `2b3b09a245be`  |
| 1000   | No file  | `2b3b09a245be`  |
| 998    | No file  | `2b3b09a245be`  |
| 990    | No file  | `2b3b09a245be`  |
| 979    | No file  | `2b3b09a245be`  |
| 972    | No file  | `2b3b09a245be`  |
| 963    | No file  | `2b3b09a245be`  |
| 955    | No file  | `2b3b09a245be`  |
| 946    | No file  | `2b3b09a245be`  |
| 938    | No file  | `2b3b09a245be`  |
| 927    | No file  | `2b3b09a245be`  |
| 911    | No file  | `2b3b09a245be`  |
| 904    | No file  | `2b3b09a245be`  |
| 899    | No file  | `2b3b09a245be`  |
| 894    | No file  | `2b3b09a245be`  |
| 885    | No file  | `2b3b09a245be`  |
| 879    | No file  | `2b3b09a245be`  |
| 872    | No file  | `2b3b09a245be`  |
| 864    | No file  | `2b3b09a245be`  |
| 855    | No file  | `2b3b09a245be`  |
| 853    | No file  | `2b3b09a245be`  |
| 845    | No file  | `2b3b09a245be`  |
| 837    | No file  | `2b3b09a245be`  |
| 829    | No file  | `2b3b09a245be`  |
| 822    | No file  | `2b3b09a245be`  |
| 814    | No file  | `2b3b09a245be`  |
| 805    | No file  | `2b3b09a245be`  |
| 794    | No file  | `2b3b09a245be`  |
| 787    | No file  | `2b3b09a245be`  |
| 780    | No file  | `2b3b09a245be`  |
| 771    | No file  | `2b3b09a245be`  |
| 760    | No file  | `2b3b09a245be`  |
| 748    | No file  | `2b3b09a245be`  |
| 741    | No file  | `2b3b09a245be`  |
| 736    | No file  | `2b3b09a245be`  |
| 731    | No file  | `2b3b09a245be`  |
| 723    | No file  | `2b3b09a245be`  |
| 711    | No file  | `2b3b09a245be`  |
| 707    | No file  | `2b3b09a245be`  |
| 697    | No file  | `2b3b09a245be`  |
| 689    | No file  | `2b3b09a245be`  |
| 683    | No file  | `2b3b09a245be`  |
| 678    | No file  | `2b3b09a245be`  |
| 670    | No file  | `2b3b09a245be`  |
| 661    | No file  | `2b3b09a245be`  |
| 656    | No file  | `2b3b09a245be`  |
| 652    | No file  | `2b3b09a245be`  |
| 643    | No file  | `2b3b09a245be`  |
| 637    | No file  | `2b3b09a245be`  |
| 630    | No file  | `2b3b09a245be`  |
| 627    | No file  | `2b3b09a245be`  |
| 621    | No file  | `2b3b09a245be`  |
| 617    | No file  | `2b3b09a245be`  |
| 615    | No file  | `2b3b09a245be`  |
| 606    | No file  | `2b3b09a245be`  |
| 599    | No file  | `2b3b09a245be`  |
| 592    | No file  | `2b3b09a245be`  |
| 586    | No file  | `2b3b09a245be`  |
| 577    | No file  | `2b3b09a245be`  |
| 569    | No file  | `2b3b09a245be`  |
| 561    | No file  | `2b3b09a245be`  |
| 554    | No file  | `2b3b09a245be`  |
| 542    | No file  | `2b3b09a245be`  |
| 532    | No file  | `2b3b09a245be`  |
| 531    | No file  | `2b3b09a245be`  |
| 526    | No file  | `2b3b09a245be`  |
| 521    | No file  | `2b3b09a245be`  |
| 517    | No file  | `2b3b09a245be`  |
| 510    | No file  | `2b3b09a245be`  |
| 508    | No file  | `2b3b09a245be`  |
| 504    | No file  | `2b3b09a245be`  |
| 497    | No file  | `2b3b09a245be`  |
| 491    | No file  | `2b3b09a245be`  |
| 485    | No file  | `2b3b09a245be`  |
| 478    | No file  | `2b3b09a245be`  |
| 472    | No file  | `2b3b09a245be`  |
| 466    | No file  | `2b3b09a245be`  |
| 457    | No file  | `2b3b09a245be`  |
| 452    | No file  | `2b3b09a245be`  |
| 449    | No file  | `2b3b09a245be`  |
| 435    | No file  | `2b3b09a245be`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `languagedata_*.loc`  | Optional | Quest titles (type `18`), NPC names (type `6`) and the name the NPC shows in the dialog (type `38`, keyed `npc_id`, `dialog_index`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                   | Field        | Notes |
| ------------------- | ---------------------- | ------------ | ----- |
| `+0x00`             | char[4]                | magic        | ASCII `PABR` |
| `+0x04`             | u32                    | count        | Number of rows; `19,267` on client 3464, the count of `allquestlist.bss` |
| `+0x08`             | Accept Quest Row[count] | rows         | See Accept Quest Row |
| `rows+0x00`         | String Table           | string_table | The PABR string table of `exploration.bss`, here with no strings |
| `string_table+0x00` | u32                    | rows_end     | `8 + count * 8`, where the rows end (`154,144` on client 3464) |
| `string_table+0x04` | u32                    | zero         | Always `0` |

The file is `8 + count * 8 + 12` bytes (`154,156` on client 3464).

The rows are grouped by NPC: every NPC's rows form one run, and the rows without an NPC form one more. On client 3464 that is 1,986 runs for 1,985 NPCs plus the no-NPC run. The runs follow no sorted order of NPC or quest key.

### Accept Quest Row (8 bytes)

| Offset  | Type | Field          | Notes |
| ------- | ---- | -------------- | ----- |
| `+0x00` | u16  | npc_id         | Character key (`characterstatic.dbss`) of the NPC who gives the quest; `0` when the quest names none |
| `+0x02` | u16  | quest_chain_id | LOC type 18 `str_id1` |
| `+0x04` | u16  | quest_id       | LOC type 18 `str_id2` |
| `+0x06` | u16  | dialog_index   | The NPC's dialog: `dialog_index << 16 \| npc_id` is a `detail_dialog.dbss` and `base_dialog.dbss` key. `0` (the Black Spirit) or `1` when `npc_id` is `0` |

Derived packed quest ID, as in `allquestlist.bss`:

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Reference Rows

Client 3464, names from `languagedata_en.loc`:

| Quest (Chain / Quest) | Title                         | npc_id | NPC Name (type 6) | dialog_index | Dialog Name (type 38) |
| --------------------- | ----------------------------- | -----: | ----------------- | -----------: | --------------------- |
| 1001 / 4              | Cat on the Roof               | 40066  | Mariano           | 1            | Mariano               |
| 1001 / 49             | Dins, Spoiling for a Fight    | 544    | Villager          | 430          | Dins                  |
| 1001 / 55             | Meutt's Sand Castle           | 544    | Villager          | 417          | Neutt                 |
| 8500 / 4              | [LoML] Emma's Invitation      | 0      | -                 | 0            | -                     |

## Notes

Figures from client 3464.

- Each packed quest ID of `allquestlist.bss` appears exactly once. The rows are in a different order from `allquestlist.bss`.
- `npc_id` is nonzero on 14,274 rows, and every one of those values is a `characterstatic.dbss` key. The other 4,993 rows have no NPC; their `dialog_index` is `0` on 2,532 and `1` on 2,461.
- `npc_id` `0` has dialogs of its own: `detail_dialog.dbss` holds keys `0` and `65536` (dialogs `0` and `1` of NPC `0`). Key `0` is the Black Spirit's dialog: LOC type 38 names (`0`, `0`) `Black Spirit`, and its greeting and options are the Black Spirit's lines. Key `65536` has no LOC name. On client 3464 the dialog `0` rows are dailies and story quests (`[Daily] Bolero's Helm Subjugation Request`, `Battle Against the Bashims`), the dialog `1` rows pass and guide quests (`Hands-On Sailing! 10.`, `Enhancing Tuvala Adventure Gear 2`); see Open Questions.
- 14,198 of the 14,274 NPC rows give a `detail_dialog.dbss` key. The test that this is the dialog index and not a count: on the 5,282 rows whose NPC has more than one dialog, 5,212 name one of that NPC's dialog indexes, where always taking the NPC's lowest index would match 521. The other 76 rows name a dialog the client does not have: 24 on the Villager character `35695`, 21 on the Quest NPC character `59878`, and the `[Ulukita]` quests of character `59981` with indexes `300` to `310`.
- Generic characters speak through many dialogs, so the dialog name tells more than the NPC name: the Villager character `544` gives "Dins, Spoiling for a Fight" as Dins (dialog `430`). The LOC type 38 dialog name differs from the LOC type 6 name on 3,923 rows.
- `quest.dbss` stores `dialog_index << 16 | npc_id` of this file as its `accept_dialog_key` (`+0x00`) for all 19,267 quests, so this file is an index of that field, grouped by NPC.
- Quest scripts call `meet(npc_id, dialog_index)` with the same pair (see `quest_dbss.md`); only 403 rows of this file hold their pair in a `meet()` call of their own quest, against 3,196 rows of `completequest.bss`.
- `completequest.bss` has the same size, header, row width and trailer, and holds the same quest set.

## Open Questions

### No-NPC Dialog `1`

Rows with `npc_id` `0` and `dialog_index` `1` point at `detail_dialog.dbss` key `65536`, a record with no LOC name and a stock social greeting. Whether it means the quest is given or taken without a dialog (automatically) is not confirmed.

### Dialogs the Client Lacks

76 NPC rows (client 3464) give a `dialog_index << 16 | npc_id` key that `detail_dialog.dbss` does not hold, among them `[Ulukita]` quests and `[Test]` quests. Whether these quests are cut content or open a dialog from another source is not known.
