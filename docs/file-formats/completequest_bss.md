# `completequest.bss` Format

## Purpose

The NPC dialog that takes each quest (the turn-in): one 8-byte row per quest with the quest key, the NPC's character key and the dialog index. `dialog_index << 16 | npc_id` is the `detail_dialog.dbss` key of the dialog, and the same value is `complete_dialog_key` at `+0x04` of the quest's `quest.dbss` record. The layout is that of [acceptquest_bss.md](acceptquest_bss.md), which holds the dialog that gives the quest.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes   | Records                   | Row bytes |
| ------ | -------------- | ------- | ------------------- | ------- | ------------------------- | --------- |
| 1      | 1109 and later | 3483    | `completequest.bss` | 151,948 | 18,991 Complete Quest Row | 8         |

| Layout | File                | Known              | Unknown    |
| ------ | ------------------- | ------------------ | ---------- |
| 1      | `completequest.bss` | 151,948 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `3554275c1096`  |
| 3482   | Layout 1 | `3554275c1096`  |
| 3474   | Layout 1 | `3554275c1096`  |
| 3473   | Layout 1 | `3554275c1096`  |
| 3464   | Layout 1 | `3554275c1096`  |
| 3458   | Layout 1 | `3554275c1096`  |
| 3454   | Layout 1 | `3554275c1096`  |
| 3444   | Layout 1 | `3554275c1096`  |
| 3435   | Layout 1 | `3554275c1096`  |
| 3426   | Layout 1 | `3554275c1096`  |
| 3418   | Layout 1 | `3554275c1096`  |
| 3412   | Layout 1 | `3554275c1096`  |
| 3402   | Layout 1 | `3554275c1096`  |
| 3396   | Layout 1 | `3554275c1096`  |
| 3387   | Layout 1 | `3554275c1096`  |
| 3381   | Layout 1 | `3554275c1096`  |
| 3373   | Layout 1 | `3554275c1096`  |
| 3364   | Layout 1 | `3554275c1096`  |
| 3356   | Layout 1 | `3554275c1096`  |
| 3349   | Layout 1 | `3554275c1096`  |
| 3342   | Layout 1 | `3554275c1096`  |
| 3335   | Layout 1 | `3554275c1096`  |
| 3326   | Layout 1 | `3554275c1096`  |
| 3321   | Layout 1 | `3554275c1096`  |
| 3314   | Layout 1 | `3554275c1096`  |
| 3303   | Layout 1 | `3554275c1096`  |
| 3302   | Layout 1 | `3554275c1096`  |
| 3293   | Layout 1 | `3554275c1096`  |
| 3283   | Layout 1 | `3554275c1096`  |
| 3275   | Layout 1 | `3554275c1096`  |
| 3267   | Layout 1 | `3554275c1096`  |
| 3258   | Layout 1 | `3554275c1096`  |
| 3251   | Layout 1 | `3554275c1096`  |
| 3242   | Layout 1 | `3554275c1096`  |
| 3235   | Layout 1 | `3554275c1096`  |
| 3229   | Layout 1 | `3554275c1096`  |
| 3212   | Layout 1 | `3554275c1096`  |
| 3203   | Layout 1 | `3554275c1096`  |
| 3193   | Layout 1 | `3554275c1096`  |
| 3186   | Layout 1 | `3554275c1096`  |
| 3177   | Layout 1 | `3554275c1096`  |
| 3169   | Layout 1 | `3554275c1096`  |
| 3158   | Layout 1 | `3554275c1096`  |
| 3151   | Layout 1 | `3554275c1096`  |
| 3144   | Layout 1 | `3554275c1096`  |
| 3133   | Layout 1 | `3554275c1096`  |
| 3125   | Layout 1 | `3554275c1096`  |
| 3118   | Layout 1 | `3554275c1096`  |
| 3111   | Layout 1 | `3554275c1096`  |
| 3103   | Layout 1 | `3554275c1096`  |
| 3095   | Layout 1 | `3554275c1096`  |
| 3086   | Layout 1 | `3554275c1096`  |
| 3072   | Layout 1 | `3554275c1096`  |
| 3062   | Layout 1 | `3554275c1096`  |
| 3052   | Layout 1 | `3554275c1096`  |
| 3045   | Layout 1 | `3554275c1096`  |
| 3037   | Layout 1 | `3554275c1096`  |
| 3030   | Layout 1 | `3554275c1096`  |
| 3021   | Layout 1 | `3554275c1096`  |
| 3012   | Layout 1 | `3554275c1096`  |
| 3002   | Layout 1 | `3554275c1096`  |
| 2995   | Layout 1 | `3554275c1096`  |
| 2987   | Layout 1 | `3554275c1096`  |
| 2978   | Layout 1 | `3554275c1096`  |
| 2970   | Layout 1 | `3554275c1096`  |
| 2959   | Layout 1 | `3554275c1096`  |
| 2951   | Layout 1 | `3554275c1096`  |
| 2942   | Layout 1 | `3554275c1096`  |
| 2935   | Layout 1 | `3554275c1096`  |
| 2932   | Layout 1 | `3554275c1096`  |
| 2923   | Layout 1 | `3554275c1096`  |
| 2919   | Layout 1 | `3554275c1096`  |
| 2907   | Layout 1 | `3554275c1096`  |
| 2900   | Layout 1 | `3554275c1096`  |
| 2891   | Layout 1 | `3554275c1096`  |
| 2882   | Layout 1 | `3554275c1096`  |
| 2872   | Layout 1 | `3554275c1096`  |
| 2863   | Layout 1 | `3554275c1096`  |
| 2855   | Layout 1 | `3554275c1096`  |
| 2849   | Layout 1 | `3554275c1096`  |
| 2844   | Layout 1 | `3554275c1096`  |
| 2834   | Layout 1 | `3554275c1096`  |
| 2825   | Layout 1 | `3554275c1096`  |
| 2819   | Layout 1 | `3554275c1096`  |
| 2811   | Layout 1 | `3554275c1096`  |
| 2803   | Layout 1 | `3554275c1096`  |
| 2794   | Layout 1 | `3554275c1096`  |
| 2783   | Layout 1 | `3554275c1096`  |
| 2774   | Layout 1 | `3554275c1096`  |
| 2765   | Layout 1 | `3554275c1096`  |
| 2756   | Layout 1 | `3554275c1096`  |
| 2750   | Layout 1 | `3554275c1096`  |
| 2743   | Layout 1 | `3554275c1096`  |
| 2736   | Layout 1 | `3554275c1096`  |
| 2726   | Layout 1 | `3554275c1096`  |
| 2717   | Layout 1 | `3554275c1096`  |
| 2709   | Layout 1 | `3554275c1096`  |
| 2703   | Layout 1 | `3554275c1096`  |
| 2695   | Layout 1 | `3554275c1096`  |
| 2684   | Layout 1 | `3554275c1096`  |
| 2672   | Layout 1 | `3554275c1096`  |
| 2665   | Layout 1 | `3554275c1096`  |
| 2657   | Layout 1 | `3554275c1096`  |
| 2649   | Layout 1 | `3554275c1096`  |
| 2644   | Layout 1 | `3554275c1096`  |
| 2637   | Layout 1 | `3554275c1096`  |
| 2629   | Layout 1 | `3554275c1096`  |
| 2619   | Layout 1 | `3554275c1096`  |
| 2612   | Layout 1 | `3554275c1096`  |
| 2606   | Layout 1 | `3554275c1096`  |
| 2602   | Layout 1 | `3554275c1096`  |
| 2601   | Layout 1 | `3554275c1096`  |
| 2592   | Layout 1 | `3554275c1096`  |
| 2583   | Layout 1 | `3554275c1096`  |
| 2575   | Layout 1 | `3554275c1096`  |
| 2567   | Layout 1 | `3554275c1096`  |
| 2560   | Layout 1 | `3554275c1096`  |
| 2553   | Layout 1 | `3554275c1096`  |
| 2545   | Layout 1 | `3554275c1096`  |
| 2538   | Layout 1 | `3554275c1096`  |
| 2529   | Layout 1 | `3554275c1096`  |
| 2519   | Layout 1 | `3554275c1096`  |
| 2513   | Layout 1 | `3554275c1096`  |
| 2510   | Layout 1 | `3554275c1096`  |
| 2507   | Layout 1 | `3554275c1096`  |
| 2503   | Layout 1 | `3554275c1096`  |
| 2498   | Layout 1 | `3554275c1096`  |
| 2492   | Layout 1 | `3554275c1096`  |
| 2487   | Layout 1 | `3554275c1096`  |
| 2480   | Layout 1 | `3554275c1096`  |
| 2474   | Layout 1 | `3554275c1096`  |
| 2468   | Layout 1 | `3554275c1096`  |
| 2460   | Layout 1 | `3554275c1096`  |
| 2453   | Layout 1 | `3554275c1096`  |
| 2444   | Layout 1 | `3554275c1096`  |
| 2438   | Layout 1 | `3554275c1096`  |
| 2434   | Layout 1 | `3554275c1096`  |
| 2429   | Layout 1 | `3554275c1096`  |
| 2421   | Layout 1 | `3554275c1096`  |
| 2414   | Layout 1 | `3554275c1096`  |
| 2407   | Layout 1 | `3554275c1096`  |
| 2401   | Layout 1 | `3554275c1096`  |
| 2397   | Layout 1 | `3554275c1096`  |
| 2393   | Layout 1 | `3554275c1096`  |
| 2384   | Layout 1 | `3554275c1096`  |
| 2378   | Layout 1 | `3554275c1096`  |
| 2372   | Layout 1 | `3554275c1096`  |
| 2358   | Layout 1 | `3554275c1096`  |
| 2352   | Layout 1 | `3554275c1096`  |
| 2347   | Layout 1 | `3554275c1096`  |
| 2343   | Layout 1 | `3554275c1096`  |
| 2335   | Layout 1 | `3554275c1096`  |
| 2327   | Layout 1 | `3554275c1096`  |
| 2324   | Layout 1 | `3554275c1096`  |
| 2319   | Layout 1 | `3554275c1096`  |
| 2313   | Layout 1 | `3554275c1096`  |
| 2308   | Layout 1 | `3554275c1096`  |
| 2302   | Layout 1 | `3554275c1096`  |
| 2295   | Layout 1 | `3554275c1096`  |
| 2290   | Layout 1 | `3554275c1096`  |
| 2284   | Layout 1 | `3554275c1096`  |
| 2276   | Layout 1 | `3554275c1096`  |
| 2269   | Layout 1 | `3554275c1096`  |
| 2259   | Layout 1 | `3554275c1096`  |
| 2250   | Layout 1 | `3554275c1096`  |
| 2243   | Layout 1 | `3554275c1096`  |
| 2235   | Layout 1 | `3554275c1096`  |
| 2229   | Layout 1 | `3554275c1096`  |
| 2224   | Layout 1 | `3554275c1096`  |
| 2218   | Layout 1 | `3554275c1096`  |
| 2215   | Layout 1 | `3554275c1096`  |
| 2207   | Layout 1 | `3554275c1096`  |
| 2203   | Layout 1 | `3554275c1096`  |
| 2196   | Layout 1 | `3554275c1096`  |
| 2192   | Layout 1 | `3554275c1096`  |
| 2189   | Layout 1 | `3554275c1096`  |
| 2183   | Layout 1 | `3554275c1096`  |
| 2179   | Layout 1 | `3554275c1096`  |
| 2171   | Layout 1 | `3554275c1096`  |
| 2163   | Layout 1 | `3554275c1096`  |
| 2156   | Layout 1 | `3554275c1096`  |
| 2151   | Layout 1 | `3554275c1096`  |
| 2147   | Layout 1 | `3554275c1096`  |
| 2142   | Layout 1 | `3554275c1096`  |
| 2138   | Layout 1 | `3554275c1096`  |
| 2134   | Layout 1 | `3554275c1096`  |
| 2130   | Layout 1 | `3554275c1096`  |
| 2122   | Layout 1 | `3554275c1096`  |
| 2107   | Layout 1 | `3554275c1096`  |
| 2098   | Layout 1 | `3554275c1096`  |
| 2089   | Layout 1 | `3554275c1096`  |
| 2081   | Layout 1 | `3554275c1096`  |
| 2073   | Layout 1 | `3554275c1096`  |
| 2067   | Layout 1 | `3554275c1096`  |
| 2063   | Layout 1 | `3554275c1096`  |
| 2059   | Layout 1 | `3554275c1096`  |
| 2052   | Layout 1 | `3554275c1096`  |
| 2044   | Layout 1 | `3554275c1096`  |
| 2039   | Layout 1 | `3554275c1096`  |
| 2032   | Layout 1 | `3554275c1096`  |
| 2025   | Layout 1 | `3554275c1096`  |
| 2011   | Layout 1 | `3554275c1096`  |
| 2005   | Layout 1 | `3554275c1096`  |
| 2000   | Layout 1 | `3554275c1096`  |
| 1996   | Layout 1 | `3554275c1096`  |
| 1991   | Layout 1 | `3554275c1096`  |
| 1985   | Layout 1 | `3554275c1096`  |
| 1980   | Layout 1 | `3554275c1096`  |
| 1969   | Layout 1 | `3554275c1096`  |
| 1964   | Layout 1 | `3554275c1096`  |
| 1958   | Layout 1 | `3554275c1096`  |
| 1950   | Layout 1 | `3554275c1096`  |
| 1945   | Layout 1 | `3554275c1096`  |
| 1937   | Layout 1 | `3554275c1096`  |
| 1933   | Layout 1 | `3554275c1096`  |
| 1927   | Layout 1 | `3554275c1096`  |
| 1921   | Layout 1 | `3554275c1096`  |
| 1914   | Layout 1 | `3554275c1096`  |
| 1908   | Layout 1 | `3554275c1096`  |
| 1897   | Layout 1 | `3554275c1096`  |
| 1892   | Layout 1 | `3554275c1096`  |
| 1886   | Layout 1 | `3554275c1096`  |
| 1881   | Layout 1 | `3554275c1096`  |
| 1871   | Layout 1 | `3554275c1096`  |
| 1866   | Layout 1 | `3554275c1096`  |
| 1862   | Layout 1 | `3554275c1096`  |
| 1854   | Layout 1 | `3554275c1096`  |
| 1846   | Layout 1 | `3554275c1096`  |
| 1838   | Layout 1 | `3554275c1096`  |
| 1832   | Layout 1 | `3554275c1096`  |
| 1826   | Layout 1 | `3554275c1096`  |
| 1822   | Layout 1 | `3554275c1096`  |
| 1818   | Layout 1 | `3554275c1096`  |
| 1804   | Layout 1 | `3554275c1096`  |
| 1794   | Layout 1 | `3554275c1096`  |
| 1790   | Layout 1 | `3554275c1096`  |
| 1784   | Layout 1 | `3554275c1096`  |
| 1774   | Layout 1 | `3554275c1096`  |
| 1771   | Layout 1 | `3554275c1096`  |
| 1762   | Layout 1 | `3554275c1096`  |
| 1759   | Layout 1 | `3554275c1096`  |
| 1754   | Layout 1 | `3554275c1096`  |
| 1749   | Layout 1 | `3554275c1096`  |
| 1743   | Layout 1 | `3554275c1096`  |
| 1737   | Layout 1 | `3554275c1096`  |
| 1731   | Layout 1 | `3554275c1096`  |
| 1725   | Layout 1 | `3554275c1096`  |
| 1717   | Layout 1 | `3554275c1096`  |
| 1710   | Layout 1 | `3554275c1096`  |
| 1704   | Layout 1 | `3554275c1096`  |
| 1698   | Layout 1 | `3554275c1096`  |
| 1690   | Layout 1 | `3554275c1096`  |
| 1685   | Layout 1 | `3554275c1096`  |
| 1680   | Layout 1 | `3554275c1096`  |
| 1674   | Layout 1 | `3554275c1096`  |
| 1668   | Layout 1 | `3554275c1096`  |
| 1659   | Layout 1 | `3554275c1096`  |
| 1649   | Layout 1 | `3554275c1096`  |
| 1642   | Layout 1 | `3554275c1096`  |
| 1636   | Layout 1 | `3554275c1096`  |
| 1628   | Layout 1 | `3554275c1096`  |
| 1622   | Layout 1 | `3554275c1096`  |
| 1614   | Layout 1 | `3554275c1096`  |
| 1608   | Layout 1 | `3554275c1096`  |
| 1602   | Layout 1 | `3554275c1096`  |
| 1598   | Layout 1 | `3554275c1096`  |
| 1594   | Layout 1 | `3554275c1096`  |
| 1590   | Layout 1 | `3554275c1096`  |
| 1587   | Layout 1 | `3554275c1096`  |
| 1584   | Layout 1 | `3554275c1096`  |
| 1579   | Layout 1 | `3554275c1096`  |
| 1572   | Layout 1 | `3554275c1096`  |
| 1565   | Layout 1 | `3554275c1096`  |
| 1559   | Layout 1 | `3554275c1096`  |
| 1554   | Layout 1 | `3554275c1096`  |
| 1547   | Layout 1 | `3554275c1096`  |
| 1537   | Layout 1 | `3554275c1096`  |
| 1529   | Layout 1 | `3554275c1096`  |
| 1524   | Layout 1 | `3554275c1096`  |
| 1519   | Layout 1 | `3554275c1096`  |
| 1509   | Layout 1 | `3554275c1096`  |
| 1506   | Layout 1 | `3554275c1096`  |
| 1504   | Layout 1 | `3554275c1096`  |
| 1500   | Layout 1 | `3554275c1096`  |
| 1493   | Layout 1 | `3554275c1096`  |
| 1489   | Layout 1 | `3554275c1096`  |
| 1485   | Layout 1 | `3554275c1096`  |
| 1481   | Layout 1 | `3554275c1096`  |
| 1474   | Layout 1 | `3554275c1096`  |
| 1466   | Layout 1 | `3554275c1096`  |
| 1462   | Layout 1 | `3554275c1096`  |
| 1459   | Layout 1 | `3554275c1096`  |
| 1453   | Layout 1 | `3554275c1096`  |
| 1450   | Layout 1 | `3554275c1096`  |
| 1445   | Layout 1 | `3554275c1096`  |
| 1439   | Layout 1 | `3554275c1096`  |
| 1433   | Layout 1 | `3554275c1096`  |
| 1430   | Layout 1 | `3554275c1096`  |
| 1426   | Layout 1 | `3554275c1096`  |
| 1421   | Layout 1 | `3554275c1096`  |
| 1417   | Layout 1 | `3554275c1096`  |
| 1416   | Layout 1 | `3554275c1096`  |
| 1409   | Layout 1 | `3554275c1096`  |
| 1405   | Layout 1 | `3554275c1096`  |
| 1401   | Layout 1 | `3554275c1096`  |
| 1396   | Layout 1 | `3554275c1096`  |
| 1391   | Layout 1 | `3554275c1096`  |
| 1390   | Layout 1 | `3554275c1096`  |
| 1386   | Layout 1 | `3554275c1096`  |
| 1381   | Layout 1 | `3554275c1096`  |
| 1379   | Layout 1 | `3554275c1096`  |
| 1372   | Layout 1 | `3554275c1096`  |
| 1366   | Layout 1 | `3554275c1096`  |
| 1364   | Layout 1 | `3554275c1096`  |
| 1363   | Layout 1 | `3554275c1096`  |
| 1360   | Layout 1 | `3554275c1096`  |
| 1358   | Layout 1 | `3554275c1096`  |
| 1355   | Layout 1 | `3554275c1096`  |
| 1351   | Layout 1 | `3554275c1096`  |
| 1348   | Layout 1 | `3554275c1096`  |
| 1346   | Layout 1 | `3554275c1096`  |
| 1341   | Layout 1 | `3554275c1096`  |
| 1340   | Layout 1 | `3554275c1096`  |
| 1338   | Layout 1 | `3554275c1096`  |
| 1335   | Layout 1 | `3554275c1096`  |
| 1333   | Layout 1 | `3554275c1096`  |
| 1329   | Layout 1 | `3554275c1096`  |
| 1327   | Layout 1 | `3554275c1096`  |
| 1324   | Layout 1 | `3554275c1096`  |
| 1321   | Layout 1 | `3554275c1096`  |
| 1319   | Layout 1 | `3554275c1096`  |
| 1318   | Layout 1 | `3554275c1096`  |
| 1316   | Layout 1 | `3554275c1096`  |
| 1313   | Layout 1 | `3554275c1096`  |
| 1311   | Layout 1 | `3554275c1096`  |
| 1309   | Layout 1 | `3554275c1096`  |
| 1304   | Layout 1 | `3554275c1096`  |
| 1292   | Layout 1 | `3554275c1096`  |
| 1286   | Layout 1 | `3554275c1096`  |
| 1280   | Layout 1 | `3554275c1096`  |
| 1276   | Layout 1 | `3554275c1096`  |
| 1267   | Layout 1 | `3554275c1096`  |
| 1261   | Layout 1 | `3554275c1096`  |
| 1256   | Layout 1 | `3554275c1096`  |
| 1250   | Layout 1 | `3554275c1096`  |
| 1246   | No file  | `3554275c1096`  |
| 1239   | No file  | `3554275c1096`  |
| 1230   | No file  | `3554275c1096`  |
| 1226   | No file  | `3554275c1096`  |
| 1220   | No file  | `3554275c1096`  |
| 1217   | No file  | `3554275c1096`  |
| 1211   | No file  | `3554275c1096`  |
| 1210   | No file  | `3554275c1096`  |
| 1208   | No file  | `3554275c1096`  |
| 1203   | No file  | `3554275c1096`  |
| 1197   | No file  | `3554275c1096`  |
| 1194   | No file  | `3554275c1096`  |
| 1192   | No file  | `3554275c1096`  |
| 1187   | No file  | `3554275c1096`  |
| 1183   | No file  | `3554275c1096`  |
| 1177   | No file  | `3554275c1096`  |
| 1173   | No file  | `3554275c1096`  |
| 1167   | No file  | `3554275c1096`  |
| 1164   | No file  | `3554275c1096`  |
| 1156   | No file  | `3554275c1096`  |
| 1149   | No file  | `3554275c1096`  |
| 1144   | Layout 1 | `3554275c1096`  |
| 1137   | Layout 1 | `3554275c1096`  |
| 1132   | Layout 1 | `3554275c1096`  |
| 1127   | Layout 1 | `3554275c1096`  |
| 1122   | Layout 1 | `3554275c1096`  |
| 1118   | Layout 1 | `3554275c1096`  |
| 1114   | Layout 1 | `3554275c1096`  |
| 1109   | Layout 1 | `3554275c1096`  |
| 1102   | No file  | `3554275c1096`  |
| 1096   | No file  | `3554275c1096`  |
| 1088   | No file  | `3554275c1096`  |
| 1081   | No file  | `3554275c1096`  |
| 1076   | No file  | `3554275c1096`  |
| 1069   | No file  | `3554275c1096`  |
| 1064   | No file  | `3554275c1096`  |
| 1058   | No file  | `3554275c1096`  |
| 1051   | No file  | `3554275c1096`  |
| 1044   | No file  | `3554275c1096`  |
| 1036   | No file  | `3554275c1096`  |
| 1026   | No file  | `3554275c1096`  |
| 1016   | No file  | `3554275c1096`  |
| 1009   | No file  | `3554275c1096`  |
| 1005   | No file  | `3554275c1096`  |
| 1000   | No file  | `3554275c1096`  |
| 998    | No file  | `3554275c1096`  |
| 990    | No file  | `3554275c1096`  |
| 979    | No file  | `3554275c1096`  |
| 972    | No file  | `3554275c1096`  |
| 963    | No file  | `3554275c1096`  |
| 955    | No file  | `3554275c1096`  |
| 946    | No file  | `3554275c1096`  |
| 938    | No file  | `3554275c1096`  |
| 927    | No file  | `3554275c1096`  |
| 911    | No file  | `3554275c1096`  |
| 904    | No file  | `3554275c1096`  |
| 899    | No file  | `3554275c1096`  |
| 894    | No file  | `3554275c1096`  |
| 885    | No file  | `3554275c1096`  |
| 879    | No file  | `3554275c1096`  |
| 872    | No file  | `3554275c1096`  |
| 864    | No file  | `3554275c1096`  |
| 855    | No file  | `3554275c1096`  |
| 853    | No file  | `3554275c1096`  |
| 845    | No file  | `3554275c1096`  |
| 837    | No file  | `3554275c1096`  |
| 829    | No file  | `3554275c1096`  |
| 822    | No file  | `3554275c1096`  |
| 814    | No file  | `3554275c1096`  |
| 805    | No file  | `3554275c1096`  |
| 794    | No file  | `3554275c1096`  |
| 787    | No file  | `3554275c1096`  |
| 780    | No file  | `3554275c1096`  |
| 771    | No file  | `3554275c1096`  |
| 760    | No file  | `3554275c1096`  |
| 748    | No file  | `3554275c1096`  |
| 741    | No file  | `3554275c1096`  |
| 736    | No file  | `3554275c1096`  |
| 731    | No file  | `3554275c1096`  |
| 723    | No file  | `3554275c1096`  |
| 711    | No file  | `3554275c1096`  |
| 707    | No file  | `3554275c1096`  |
| 697    | No file  | `3554275c1096`  |
| 689    | No file  | `3554275c1096`  |
| 683    | No file  | `3554275c1096`  |
| 678    | No file  | `3554275c1096`  |
| 670    | No file  | `3554275c1096`  |
| 661    | No file  | `3554275c1096`  |
| 656    | No file  | `3554275c1096`  |
| 652    | No file  | `3554275c1096`  |
| 643    | No file  | `3554275c1096`  |
| 637    | No file  | `3554275c1096`  |
| 630    | No file  | `3554275c1096`  |
| 627    | No file  | `3554275c1096`  |
| 621    | No file  | `3554275c1096`  |
| 617    | No file  | `3554275c1096`  |
| 615    | No file  | `3554275c1096`  |
| 606    | No file  | `3554275c1096`  |
| 599    | No file  | `3554275c1096`  |
| 592    | No file  | `3554275c1096`  |
| 586    | No file  | `3554275c1096`  |
| 577    | No file  | `3554275c1096`  |
| 569    | No file  | `3554275c1096`  |
| 561    | No file  | `3554275c1096`  |
| 554    | No file  | `3554275c1096`  |
| 542    | No file  | `3554275c1096`  |
| 532    | No file  | `3554275c1096`  |
| 531    | No file  | `3554275c1096`  |
| 526    | No file  | `3554275c1096`  |
| 521    | No file  | `3554275c1096`  |
| 517    | No file  | `3554275c1096`  |
| 510    | No file  | `3554275c1096`  |
| 508    | No file  | `3554275c1096`  |
| 504    | No file  | `3554275c1096`  |
| 497    | No file  | `3554275c1096`  |
| 491    | No file  | `3554275c1096`  |
| 485    | No file  | `3554275c1096`  |
| 478    | No file  | `3554275c1096`  |
| 472    | No file  | `3554275c1096`  |
| 466    | No file  | `3554275c1096`  |
| 457    | No file  | `3554275c1096`  |
| 452    | No file  | `3554275c1096`  |
| 449    | No file  | `3554275c1096`  |
| 435    | No file  | `3554275c1096`  |

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
| `+0x08`             | Complete Quest Row[count] | rows         | See Complete Quest Row |
| `rows+0x00`         | String Table           | string_table | The PABR string table of `exploration.bss`, here with no strings |
| `string_table+0x00` | u32                    | rows_end     | `8 + count * 8`, where the rows end (`154,144` on client 3464) |
| `string_table+0x04` | u32                    | zero         | Always `0` |

The file is `8 + count * 8 + 12` bytes (`154,156` on client 3464).

The rows are grouped by NPC: every NPC's rows form one run, and the rows without an NPC form one more. On client 3464 that is 2,024 runs for 2,023 NPCs plus the no-NPC run.

### Complete Quest Row (8 bytes)

| Offset  | Type | Field          | Notes |
| ------- | ---- | -------------- | ----- |
| `+0x00` | u16  | npc_id         | Character key (`characterstatic.dbss`) of the NPC who takes the quest; `0` when the quest names none |
| `+0x02` | u16  | quest_chain_id | LOC type 18 `str_id1` |
| `+0x04` | u16  | quest_id       | LOC type 18 `str_id2` |
| `+0x06` | u16  | dialog_index   | The NPC's dialog: `dialog_index << 16 \| npc_id` is a `detail_dialog.dbss` and `base_dialog.dbss` key. `0` (the Black Spirit) or `1` when `npc_id` is `0`, except one row with `12` |

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
| 1001 / 49             | Dins, Spoiling for a Fight    | 544    | Villager          | 326          | Vigilante             |
| 8500 / 4              | [LoML] Emma's Invitation      | 59875  | Quest NPC         | 73           | Igor Bartali          |

## Notes

Figures from client 3464.

- Each packed quest ID of `allquestlist.bss` appears exactly once, in a different order from `allquestlist.bss` and from `acceptquest.bss`.
- `npc_id` is nonzero on 15,728 rows, and every one of those values is a `characterstatic.dbss` key. The other 3,539 rows have no NPC; their `dialog_index` is `0` on 2,507, `1` on 1,031 and `12` on one (quest 21420 / 7, a key `detail_dialog.dbss` does not hold). Dialogs `0` and `1` of NPC `0` are those of `acceptquest.bss`: `0` is the Black Spirit.
- 15,672 of the 15,728 NPC rows give a `detail_dialog.dbss` key. On the 5,971 rows whose NPC has more than one dialog, 5,931 name one of that NPC's dialog indexes, where always taking the NPC's lowest index would match 561.
- The LOC type 38 dialog name differs from the LOC type 6 name on 4,557 rows. The generic Quest NPC character `59875` speaks as Igor Bartali, Dolswe, Yibang and others, one name per dialog.
- `quest.dbss` stores `dialog_index << 16 | npc_id` of this file as its `complete_dialog_key` (`+0x04`) for all 19,267 quests.
- Quest scripts call `meet(npc_id, dialog_index)` with the same pair (see `quest_dbss.md`): 3,196 rows of this file hold their exact pair in a `meet()` call of their own quest, against 403 rows of `acceptquest.bss`.

## Open Questions

### Dialogs the Client Lacks

56 NPC rows (client 3464) give a `dialog_index << 16 | npc_id` key that `detail_dialog.dbss` does not hold, as in `acceptquest.bss`. The largest groups are character `59725` (18 rows) and the Villager character `35695` (14 rows).
