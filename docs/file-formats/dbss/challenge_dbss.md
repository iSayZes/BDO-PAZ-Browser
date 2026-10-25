# `challenge.dbss` Format

## Purpose

The challenges of the character window (`panel_characterinfo_challenge_all`):
per challenge key its type, Korean title and description, the server
progress condition and the reward condition scripts, the completion type
with two parameters, the reset rule, the base and selectable rewards in the
178-byte reward entries of [`quest.dbss`](quest_dbss.md#reward-entry-178-bytes),
and the reward flags. `challengeoffset.dbss` indexes the rows by key. The
reward items of all challenges are listed again in
[`challengerewardlist.bss`](../bss/challengerewardlist_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes     | Records                                     | Row bytes |
| ------ | -------------- | ---------------------- | --------- | ------------------------------------------- | --------- |
| 2      | 2923 and later | `challenge.dbss`       | 1,432,422 | 3,723 Reward Entry, 1,779 Row, 1,779 Record | 178       |
| 2      | 2923 and later | `challengeoffset.dbss` | 17,794    | 1,779 Offset Row                            | 10        |
| 1      | 1598 to 2250   | `challenge.dbss`       | 1,192,444 | 3,125 Reward Entry, 1,430 Row, 1,430 Record | 188       |
| 1      | 1598 to 2250   | `challengeoffset.dbss` | 14,304    | 1,430 Offset Row                            | 10        |

| Layout | File                   | Known               | Unknown           |
| ------ | ---------------------- | ------------------- | ----------------- |
| 2      | `challenge.dbss`       | 1,178,799 B (82.3%) | 253,623 B (17.7%) |
| 2      | `challengeoffset.dbss` | 17,794 B (100.0%)   | 0 B (0.0%)        |
| 1      | `challenge.dbss`       | 949,384 B (79.6%)   | 243,060 B (20.4%) |
| 1      | `challengeoffset.dbss` | 14,304 B (100.0%)   | 0 B (0.0%)        |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `ba364580032e`  |
| 3482   | Layout 2             | `ba364580032e`  |
| 3474   | Layout 2             | `ba364580032e`  |
| 3473   | Layout 2             | `ba364580032e`  |
| 3464   | Layout 2             | `ba364580032e`  |
| 3458   | Layout 2             | `ba364580032e`  |
| 3454   | Layout 2             | `ba364580032e`  |
| 3444   | Layout 2             | `ba364580032e`  |
| 3435   | Layout 2             | `ba364580032e`  |
| 3426   | Layout 2             | `ba364580032e`  |
| 3418   | Layout 2             | `ba364580032e`  |
| 3412   | Layout 2             | `ba364580032e`  |
| 3402   | Layout 2             | `ba364580032e`  |
| 3396   | Layout 2             | `ba364580032e`  |
| 3387   | Layout 2             | `ba364580032e`  |
| 3381   | Layout 2             | `ba364580032e`  |
| 3373   | Layout 2             | `ba364580032e`  |
| 3364   | Layout 2             | `ba364580032e`  |
| 3356   | Layout 2             | `ba364580032e`  |
| 3349   | Layout 2             | `ba364580032e`  |
| 3342   | Layout 2             | `ba364580032e`  |
| 3335   | Layout 2             | `ba364580032e`  |
| 3326   | Layout 2             | `ba364580032e`  |
| 3321   | Layout 2             | `ba364580032e`  |
| 3314   | Layout 2             | `ba364580032e`  |
| 3303   | Layout 2             | `ba364580032e`  |
| 3302   | Layout 2             | `ba364580032e`  |
| 3293   | Layout 2             | `ba364580032e`  |
| 3283   | Layout 2             | `ba364580032e`  |
| 3275   | Layout 2             | `ba364580032e`  |
| 3267   | Layout 2             | `ba364580032e`  |
| 3258   | Layout 2             | `ba364580032e`  |
| 3251   | Layout 2             | `ba364580032e`  |
| 3242   | Layout 2             | `ba364580032e`  |
| 3235   | Layout 2             | `ba364580032e`  |
| 3229   | Layout 2             | `ba364580032e`  |
| 3212   | Layout 2             | `ba364580032e`  |
| 3203   | Layout 2             | `ba364580032e`  |
| 3193   | Layout 2             | `ba364580032e`  |
| 3186   | Layout 2             | `ba364580032e`  |
| 3177   | Layout 2             | `ba364580032e`  |
| 3169   | Layout 2             | `ba364580032e`  |
| 3158   | Layout 2             | `ba364580032e`  |
| 3151   | Layout 2             | `ba364580032e`  |
| 3144   | Layout 2             | `ba364580032e`  |
| 3133   | Layout 2             | `ba364580032e`  |
| 3125   | Layout 2             | `ba364580032e`  |
| 3118   | Layout 2             | `ba364580032e`  |
| 3111   | Layout 2             | `ba364580032e`  |
| 3103   | Layout 2             | `ba364580032e`  |
| 3095   | Layout 2             | `ba364580032e`  |
| 3086   | Layout 2             | `ba364580032e`  |
| 3072   | Layout 2             | `ba364580032e`  |
| 3062   | Layout 2             | `ba364580032e`  |
| 3052   | Layout 2             | `ba364580032e`  |
| 3045   | Layout 2             | `ba364580032e`  |
| 3037   | Layout 2             | `ba364580032e`  |
| 3030   | Layout 2             | `ba364580032e`  |
| 3021   | Layout 2             | `ba364580032e`  |
| 3012   | Layout 2             | `ba364580032e`  |
| 3002   | Layout 2             | `ba364580032e`  |
| 2995   | Layout 2             | `ba364580032e`  |
| 2987   | Layout 2             | `ba364580032e`  |
| 2978   | Layout 2             | `ba364580032e`  |
| 2970   | Layout 2             | `ba364580032e`  |
| 2959   | Layout 2             | `ba364580032e`  |
| 2951   | Layout 2             | `ba364580032e`  |
| 2942   | Layout 2             | `ba364580032e`  |
| 2935   | Layout 2             | `ba364580032e`  |
| 2932   | Layout 2             | `ba364580032e`  |
| 2923   | Layout 2             | `ba364580032e`  |
| 2919   | No documented layout | `ba364580032e`  |
| 2907   | No documented layout | `ba364580032e`  |
| 2900   | No documented layout | `ba364580032e`  |
| 2891   | No documented layout | `ba364580032e`  |
| 2882   | No documented layout | `ba364580032e`  |
| 2872   | No documented layout | `ba364580032e`  |
| 2863   | No documented layout | `ba364580032e`  |
| 2855   | No documented layout | `ba364580032e`  |
| 2849   | No documented layout | `ba364580032e`  |
| 2844   | No documented layout | `ba364580032e`  |
| 2834   | No documented layout | `ba364580032e`  |
| 2825   | No documented layout | `ba364580032e`  |
| 2819   | No documented layout | `ba364580032e`  |
| 2811   | No documented layout | `ba364580032e`  |
| 2803   | No documented layout | `ba364580032e`  |
| 2794   | No documented layout | `ba364580032e`  |
| 2783   | No documented layout | `ba364580032e`  |
| 2774   | No documented layout | `ba364580032e`  |
| 2765   | No documented layout | `ba364580032e`  |
| 2756   | No documented layout | `ba364580032e`  |
| 2750   | No documented layout | `ba364580032e`  |
| 2743   | No documented layout | `ba364580032e`  |
| 2736   | No documented layout | `ba364580032e`  |
| 2726   | No documented layout | `ba364580032e`  |
| 2717   | No documented layout | `ba364580032e`  |
| 2709   | No documented layout | `ba364580032e`  |
| 2703   | No documented layout | `ba364580032e`  |
| 2695   | No documented layout | `ba364580032e`  |
| 2684   | No documented layout | `ba364580032e`  |
| 2672   | No documented layout | `ba364580032e`  |
| 2665   | No documented layout | `ba364580032e`  |
| 2657   | No documented layout | `ba364580032e`  |
| 2649   | No documented layout | `ba364580032e`  |
| 2644   | No documented layout | `ba364580032e`  |
| 2637   | No documented layout | `ba364580032e`  |
| 2629   | No documented layout | `ba364580032e`  |
| 2619   | No documented layout | `ba364580032e`  |
| 2612   | No documented layout | `ba364580032e`  |
| 2606   | No documented layout | `ba364580032e`  |
| 2602   | No documented layout | `ba364580032e`  |
| 2601   | No documented layout | `ba364580032e`  |
| 2592   | No documented layout | `ba364580032e`  |
| 2583   | No documented layout | `ba364580032e`  |
| 2575   | No documented layout | `ba364580032e`  |
| 2567   | No documented layout | `ba364580032e`  |
| 2560   | No documented layout | `ba364580032e`  |
| 2553   | No documented layout | `ba364580032e`  |
| 2545   | No documented layout | `ba364580032e`  |
| 2538   | No documented layout | `ba364580032e`  |
| 2529   | No documented layout | `ba364580032e`  |
| 2519   | No documented layout | `ba364580032e`  |
| 2513   | No documented layout | `ba364580032e`  |
| 2510   | No documented layout | `ba364580032e`  |
| 2507   | No documented layout | `ba364580032e`  |
| 2503   | No documented layout | `ba364580032e`  |
| 2498   | No documented layout | `ba364580032e`  |
| 2492   | No documented layout | `ba364580032e`  |
| 2487   | No documented layout | `ba364580032e`  |
| 2480   | No documented layout | `ba364580032e`  |
| 2474   | No documented layout | `ba364580032e`  |
| 2468   | No documented layout | `ba364580032e`  |
| 2460   | No documented layout | `ba364580032e`  |
| 2453   | No documented layout | `ba364580032e`  |
| 2444   | No documented layout | `ba364580032e`  |
| 2438   | No documented layout | `ba364580032e`  |
| 2434   | No documented layout | `ba364580032e`  |
| 2429   | No documented layout | `ba364580032e`  |
| 2421   | No documented layout | `ba364580032e`  |
| 2414   | No documented layout | `ba364580032e`  |
| 2407   | No documented layout | `ba364580032e`  |
| 2401   | No documented layout | `ba364580032e`  |
| 2397   | No documented layout | `ba364580032e`  |
| 2393   | No documented layout | `ba364580032e`  |
| 2384   | No documented layout | `ba364580032e`  |
| 2378   | No documented layout | `ba364580032e`  |
| 2372   | No documented layout | `ba364580032e`  |
| 2358   | No documented layout | `ba364580032e`  |
| 2352   | No documented layout | `ba364580032e`  |
| 2347   | No documented layout | `ba364580032e`  |
| 2343   | No documented layout | `ba364580032e`  |
| 2335   | No documented layout | `ba364580032e`  |
| 2327   | No documented layout | `ba364580032e`  |
| 2324   | No documented layout | `ba364580032e`  |
| 2319   | No documented layout | `ba364580032e`  |
| 2313   | No documented layout | `ba364580032e`  |
| 2308   | No documented layout | `ba364580032e`  |
| 2302   | No documented layout | `ba364580032e`  |
| 2295   | No documented layout | `ba364580032e`  |
| 2290   | No documented layout | `ba364580032e`  |
| 2284   | No documented layout | `ba364580032e`  |
| 2276   | No documented layout | `ba364580032e`  |
| 2269   | No documented layout | `ba364580032e`  |
| 2259   | No documented layout | `ba364580032e`  |
| 2250   | Layout 1             | `ba364580032e`  |
| 2243   | Layout 1             | `ba364580032e`  |
| 2235   | Layout 1             | `ba364580032e`  |
| 2229   | Layout 1             | `ba364580032e`  |
| 2224   | Layout 1             | `ba364580032e`  |
| 2218   | Layout 1             | `ba364580032e`  |
| 2215   | Layout 1             | `ba364580032e`  |
| 2207   | Layout 1             | `ba364580032e`  |
| 2203   | Layout 1             | `ba364580032e`  |
| 2196   | Layout 1             | `ba364580032e`  |
| 2192   | Layout 1             | `ba364580032e`  |
| 2189   | Layout 1             | `ba364580032e`  |
| 2183   | Layout 1             | `ba364580032e`  |
| 2179   | Layout 1             | `ba364580032e`  |
| 2171   | Layout 1             | `ba364580032e`  |
| 2163   | Layout 1             | `ba364580032e`  |
| 2156   | Layout 1             | `ba364580032e`  |
| 2151   | Layout 1             | `ba364580032e`  |
| 2147   | Layout 1             | `ba364580032e`  |
| 2142   | Layout 1             | `ba364580032e`  |
| 2138   | Layout 1             | `ba364580032e`  |
| 2134   | Layout 1             | `ba364580032e`  |
| 2130   | Layout 1             | `ba364580032e`  |
| 2122   | Layout 1             | `ba364580032e`  |
| 2107   | Layout 1             | `ba364580032e`  |
| 2098   | Layout 1             | `ba364580032e`  |
| 2089   | Layout 1             | `ba364580032e`  |
| 2081   | Layout 1             | `ba364580032e`  |
| 2073   | Layout 1             | `ba364580032e`  |
| 2067   | Layout 1             | `ba364580032e`  |
| 2063   | Layout 1             | `ba364580032e`  |
| 2059   | Layout 1             | `ba364580032e`  |
| 2052   | Layout 1             | `ba364580032e`  |
| 2044   | Layout 1             | `ba364580032e`  |
| 2039   | Layout 1             | `ba364580032e`  |
| 2032   | Layout 1             | `ba364580032e`  |
| 2025   | Layout 1             | `ba364580032e`  |
| 2011   | Layout 1             | `ba364580032e`  |
| 2005   | Layout 1             | `ba364580032e`  |
| 2000   | Layout 1             | `ba364580032e`  |
| 1996   | Layout 1             | `ba364580032e`  |
| 1991   | Layout 1             | `ba364580032e`  |
| 1985   | Layout 1             | `ba364580032e`  |
| 1980   | Layout 1             | `ba364580032e`  |
| 1969   | Layout 1             | `ba364580032e`  |
| 1964   | Layout 1             | `ba364580032e`  |
| 1958   | Layout 1             | `ba364580032e`  |
| 1950   | Layout 1             | `ba364580032e`  |
| 1945   | Layout 1             | `ba364580032e`  |
| 1937   | Layout 1             | `ba364580032e`  |
| 1933   | Layout 1             | `ba364580032e`  |
| 1927   | Layout 1             | `ba364580032e`  |
| 1921   | Layout 1             | `ba364580032e`  |
| 1914   | Layout 1             | `ba364580032e`  |
| 1908   | Layout 1             | `ba364580032e`  |
| 1897   | Layout 1             | `ba364580032e`  |
| 1892   | Layout 1             | `ba364580032e`  |
| 1886   | Layout 1             | `ba364580032e`  |
| 1881   | Layout 1             | `ba364580032e`  |
| 1871   | Layout 1             | `ba364580032e`  |
| 1866   | Layout 1             | `ba364580032e`  |
| 1862   | Layout 1             | `ba364580032e`  |
| 1854   | Layout 1             | `ba364580032e`  |
| 1846   | Layout 1             | `ba364580032e`  |
| 1838   | Layout 1             | `ba364580032e`  |
| 1832   | Layout 1             | `ba364580032e`  |
| 1826   | Layout 1             | `ba364580032e`  |
| 1822   | Layout 1             | `ba364580032e`  |
| 1818   | Layout 1             | `ba364580032e`  |
| 1804   | Layout 1             | `ba364580032e`  |
| 1794   | Layout 1             | `ba364580032e`  |
| 1790   | Layout 1             | `ba364580032e`  |
| 1784   | Layout 1             | `ba364580032e`  |
| 1774   | Layout 1             | `ba364580032e`  |
| 1771   | Layout 1             | `ba364580032e`  |
| 1762   | Layout 1             | `ba364580032e`  |
| 1759   | Layout 1             | `ba364580032e`  |
| 1754   | Layout 1             | `ba364580032e`  |
| 1749   | Layout 1             | `ba364580032e`  |
| 1743   | Layout 1             | `ba364580032e`  |
| 1737   | Layout 1             | `ba364580032e`  |
| 1731   | Layout 1             | `ba364580032e`  |
| 1725   | Layout 1             | `ba364580032e`  |
| 1717   | Layout 1             | `ba364580032e`  |
| 1710   | Layout 1             | `ba364580032e`  |
| 1704   | Layout 1             | `ba364580032e`  |
| 1698   | Layout 1             | `ba364580032e`  |
| 1690   | Layout 1             | `ba364580032e`  |
| 1685   | Layout 1             | `ba364580032e`  |
| 1680   | Layout 1             | `ba364580032e`  |
| 1674   | Layout 1             | `ba364580032e`  |
| 1668   | Layout 1             | `ba364580032e`  |
| 1659   | Layout 1             | `ba364580032e`  |
| 1649   | Layout 1             | `ba364580032e`  |
| 1642   | Layout 1             | `ba364580032e`  |
| 1636   | Layout 1             | `ba364580032e`  |
| 1628   | Layout 1             | `ba364580032e`  |
| 1622   | Layout 1             | `ba364580032e`  |
| 1614   | Layout 1             | `ba364580032e`  |
| 1608   | Layout 1             | `ba364580032e`  |
| 1602   | Layout 1             | `ba364580032e`  |
| 1598   | Layout 1             | `ba364580032e`  |
| 1594   | No documented layout | `ba364580032e`  |
| 1590   | No documented layout | `ba364580032e`  |
| 1587   | No documented layout | `ba364580032e`  |
| 1584   | No documented layout | `ba364580032e`  |
| 1579   | No documented layout | `ba364580032e`  |
| 1572   | No documented layout | `ba364580032e`  |
| 1565   | No documented layout | `ba364580032e`  |
| 1559   | No documented layout | `ba364580032e`  |
| 1554   | No documented layout | `ba364580032e`  |
| 1547   | No documented layout | `ba364580032e`  |
| 1537   | No documented layout | `ba364580032e`  |
| 1529   | No documented layout | `ba364580032e`  |
| 1524   | No documented layout | `ba364580032e`  |
| 1519   | No documented layout | `ba364580032e`  |
| 1509   | No documented layout | `ba364580032e`  |
| 1506   | No documented layout | `ba364580032e`  |
| 1504   | No documented layout | `ba364580032e`  |
| 1500   | No documented layout | `ba364580032e`  |
| 1493   | No documented layout | `ba364580032e`  |
| 1489   | No documented layout | `ba364580032e`  |
| 1485   | No documented layout | `ba364580032e`  |
| 1481   | No documented layout | `ba364580032e`  |
| 1474   | No documented layout | `ba364580032e`  |
| 1466   | No documented layout | `ba364580032e`  |
| 1462   | No documented layout | `ba364580032e`  |
| 1459   | No documented layout | `ba364580032e`  |
| 1453   | No documented layout | `ba364580032e`  |
| 1450   | No documented layout | `ba364580032e`  |
| 1445   | No documented layout | `ba364580032e`  |
| 1439   | No documented layout | `ba364580032e`  |
| 1433   | No documented layout | `ba364580032e`  |
| 1430   | No documented layout | `ba364580032e`  |
| 1426   | No documented layout | `ba364580032e`  |
| 1421   | No documented layout | `ba364580032e`  |
| 1417   | No documented layout | `ba364580032e`  |
| 1416   | No documented layout | `ba364580032e`  |
| 1409   | No documented layout | `ba364580032e`  |
| 1405   | No documented layout | `ba364580032e`  |
| 1401   | No documented layout | `ba364580032e`  |
| 1396   | No documented layout | `ba364580032e`  |
| 1391   | No documented layout | `ba364580032e`  |
| 1390   | No documented layout | `ba364580032e`  |
| 1386   | No documented layout | `ba364580032e`  |
| 1381   | No documented layout | `ba364580032e`  |
| 1379   | No documented layout | `ba364580032e`  |
| 1372   | No documented layout | `ba364580032e`  |
| 1366   | No documented layout | `ba364580032e`  |
| 1364   | No documented layout | `ba364580032e`  |
| 1363   | No documented layout | `ba364580032e`  |
| 1360   | No documented layout | `ba364580032e`  |
| 1358   | No documented layout | `ba364580032e`  |
| 1355   | No documented layout | `ba364580032e`  |
| 1351   | No documented layout | `ba364580032e`  |
| 1348   | No documented layout | `ba364580032e`  |
| 1346   | No documented layout | `ba364580032e`  |
| 1341   | No documented layout | `ba364580032e`  |
| 1340   | No documented layout | `ba364580032e`  |
| 1338   | No documented layout | `ba364580032e`  |
| 1335   | No documented layout | `ba364580032e`  |
| 1333   | No documented layout | `ba364580032e`  |
| 1329   | No documented layout | `ba364580032e`  |
| 1327   | No documented layout | `ba364580032e`  |
| 1324   | No documented layout | `ba364580032e`  |
| 1321   | No documented layout | `ba364580032e`  |
| 1319   | No documented layout | `ba364580032e`  |
| 1318   | No documented layout | `ba364580032e`  |
| 1316   | No documented layout | `ba364580032e`  |
| 1313   | No documented layout | `ba364580032e`  |
| 1311   | No documented layout | `ba364580032e`  |
| 1309   | No documented layout | `ba364580032e`  |
| 1304   | No documented layout | `ba364580032e`  |
| 1292   | No documented layout | `ba364580032e`  |
| 1286   | No documented layout | `ba364580032e`  |
| 1280   | No documented layout | `ba364580032e`  |
| 1276   | No documented layout | `ba364580032e`  |
| 1267   | No documented layout | `ba364580032e`  |
| 1261   | No documented layout | `ba364580032e`  |
| 1256   | No documented layout | `ba364580032e`  |
| 1250   | No documented layout | `ba364580032e`  |
| 1246   | No documented layout | `ba364580032e`  |
| 1239   | No documented layout | `ba364580032e`  |
| 1230   | No documented layout | `ba364580032e`  |
| 1226   | No documented layout | `ba364580032e`  |
| 1220   | No file              | `ba364580032e`  |
| 1217   | No file              | `ba364580032e`  |
| 1211   | No file              | `ba364580032e`  |
| 1210   | No file              | `ba364580032e`  |
| 1208   | No file              | `ba364580032e`  |
| 1203   | No file              | `ba364580032e`  |
| 1197   | No file              | `ba364580032e`  |
| 1194   | No file              | `ba364580032e`  |
| 1192   | No file              | `ba364580032e`  |
| 1187   | No file              | `ba364580032e`  |
| 1183   | No file              | `ba364580032e`  |
| 1177   | No file              | `ba364580032e`  |
| 1173   | No file              | `ba364580032e`  |
| 1167   | No file              | `ba364580032e`  |
| 1164   | No file              | `ba364580032e`  |
| 1156   | No file              | `ba364580032e`  |
| 1149   | No file              | `ba364580032e`  |
| 1144   | No file              | `ba364580032e`  |
| 1137   | No file              | `ba364580032e`  |
| 1132   | No file              | `ba364580032e`  |
| 1127   | No file              | `ba364580032e`  |
| 1122   | No file              | `ba364580032e`  |
| 1118   | No file              | `ba364580032e`  |
| 1114   | No file              | `ba364580032e`  |
| 1109   | No file              | `ba364580032e`  |
| 1102   | No file              | `ba364580032e`  |
| 1096   | No file              | `ba364580032e`  |
| 1088   | No file              | `ba364580032e`  |
| 1081   | No file              | `ba364580032e`  |
| 1076   | No file              | `ba364580032e`  |
| 1069   | No file              | `ba364580032e`  |
| 1064   | No file              | `ba364580032e`  |
| 1058   | No file              | `ba364580032e`  |
| 1051   | No file              | `ba364580032e`  |
| 1044   | No file              | `ba364580032e`  |
| 1036   | No file              | `ba364580032e`  |
| 1026   | No file              | `ba364580032e`  |
| 1016   | No file              | `ba364580032e`  |
| 1009   | No file              | `ba364580032e`  |
| 1005   | No file              | `ba364580032e`  |
| 1000   | No file              | `ba364580032e`  |
| 998    | No file              | `ba364580032e`  |
| 990    | No file              | `ba364580032e`  |
| 979    | No file              | `ba364580032e`  |
| 972    | No file              | `ba364580032e`  |
| 963    | No file              | `ba364580032e`  |
| 955    | No file              | `ba364580032e`  |
| 946    | No file              | `ba364580032e`  |
| 938    | No file              | `ba364580032e`  |
| 927    | No file              | `ba364580032e`  |
| 911    | No file              | `ba364580032e`  |
| 904    | No file              | `ba364580032e`  |
| 899    | No file              | `ba364580032e`  |
| 894    | No file              | `ba364580032e`  |
| 885    | No file              | `ba364580032e`  |
| 879    | No file              | `ba364580032e`  |
| 872    | No file              | `ba364580032e`  |
| 864    | No file              | `ba364580032e`  |
| 855    | No file              | `ba364580032e`  |
| 853    | No file              | `ba364580032e`  |
| 845    | No file              | `ba364580032e`  |
| 837    | No file              | `ba364580032e`  |
| 829    | No file              | `ba364580032e`  |
| 822    | No file              | `ba364580032e`  |
| 814    | No file              | `ba364580032e`  |
| 805    | No file              | `ba364580032e`  |
| 794    | No file              | `ba364580032e`  |
| 787    | No file              | `ba364580032e`  |
| 780    | No file              | `ba364580032e`  |
| 771    | No file              | `ba364580032e`  |
| 760    | No file              | `ba364580032e`  |
| 748    | No file              | `ba364580032e`  |
| 741    | No file              | `ba364580032e`  |
| 736    | No file              | `ba364580032e`  |
| 731    | No file              | `ba364580032e`  |
| 723    | No file              | `ba364580032e`  |
| 711    | No file              | `ba364580032e`  |
| 707    | No file              | `ba364580032e`  |
| 697    | No file              | `ba364580032e`  |
| 689    | No file              | `ba364580032e`  |
| 683    | No file              | `ba364580032e`  |
| 678    | No file              | `ba364580032e`  |
| 670    | No file              | `ba364580032e`  |
| 661    | No file              | `ba364580032e`  |
| 656    | No file              | `ba364580032e`  |
| 652    | No file              | `ba364580032e`  |
| 643    | No file              | `ba364580032e`  |
| 637    | No file              | `ba364580032e`  |
| 630    | No file              | `ba364580032e`  |
| 627    | No file              | `ba364580032e`  |
| 621    | No file              | `ba364580032e`  |
| 617    | No file              | `ba364580032e`  |
| 615    | No file              | `ba364580032e`  |
| 606    | No file              | `ba364580032e`  |
| 599    | No file              | `ba364580032e`  |
| 592    | No file              | `ba364580032e`  |
| 586    | No file              | `ba364580032e`  |
| 577    | No file              | `ba364580032e`  |
| 569    | No file              | `ba364580032e`  |
| 561    | No file              | `ba364580032e`  |
| 554    | No file              | `ba364580032e`  |
| 542    | No file              | `ba364580032e`  |
| 532    | No file              | `ba364580032e`  |
| 531    | No file              | `ba364580032e`  |
| 526    | No file              | `ba364580032e`  |
| 521    | No file              | `ba364580032e`  |
| 517    | No file              | `ba364580032e`  |
| 510    | No file              | `ba364580032e`  |
| 508    | No file              | `ba364580032e`  |
| 504    | No file              | `ba364580032e`  |
| 497    | No file              | `ba364580032e`  |
| 491    | No file              | `ba364580032e`  |
| 485    | No file              | `ba364580032e`  |
| 478    | No file              | `ba364580032e`  |
| 472    | No file              | `ba364580032e`  |
| 466    | No file              | `ba364580032e`  |
| 457    | No file              | `ba364580032e`  |
| 452    | No file              | `ba364580032e`  |
| 449    | No file              | `ba364580032e`  |
| 435    | No file              | `ba364580032e`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                                                 |
| ---------------------- | -------- | ------------------------------------------------------------------------------------ |
| `challengeoffset.dbss` | Optional | `challenge_key -> (offset, size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`  | Optional | Challenge titles and descriptions (type 48) and the reward item names (type 0)       |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A record count, then the records back
to back; the file ends after the last record.

| Offset  | Type          | Field   | Notes                                       |
| ------- | ------------- | ------- | ------------------------------------------- |
| `+0x00` | u32           | count   | Number of challenges; `1779` on client 3483 |
| `+0x04` | Record[count] | records | See Record                                  |

### Record (variable: 2 bytes + row)

| Offset  | Type | Field      | Notes                               |
| ------- | ---- | ---------- | ----------------------------------- |
| `+0x00` | u16  | key_prefix | Equals `challenge_key`              |
| `+0x02` | Row  | row        | The offset row points at this field |

### Row (variable: 90 bytes + texts and rewards)

Counts in the Notes column are from client 3483.

| Offset                      | Type                              | Field                     | Notes |
| --------------------------- | --------------------------------- | ------------------------- | ----- |
| `+0x00`                     | u16                               | challenge_key             | `2189` to `15156`; LOC type 48 `str_id1` |
| `+0x02`                     | u32                               | challenge_type            | See [Challenge Types](#challenge-types) |
| `+0x06`                     | str16                             | title_kr                  | Korean title; 106 carry PAColor tags |
| `title_kr+0x00`             | str16                             | description_kr            | Korean description with PAColor tags; line breaks are stored as the two characters `\n` |
| `description_kr+0x00`       | str16                             | progress_condition        | `0` on 1,695 rows, empty on 84; see Field Names |
| `progress_condition+0x00`   | str16                             | reward_condition          | Condition script: empty on 1,414 rows, else `checkClass(n);` (209), `checkPeriod(...)` (67), `checkseasoncharacter()` (47), `!checkSpecialCharacter();` (31), `getLevel()` (6) or `clearquest(...)` (5) first |
| `reward_condition+0x00`     | u32                               | complete_condition_type   | See [Completion Types](#completion-types) |
| `reward_condition+0x04`     | i32                               | condition_param1          | First parameter of the completion type |
| `reward_condition+0x08`     | i32                               | condition_param2          | Second parameter of the completion type |
| `reward_condition+0x0C`     | u32                               | reset_type                | See [Reset Types](#reset-types) |
| `reward_condition+0x10`     | i32                               | reset_value               | `0` on 1,739 rows, `1` on 40 |
| `reward_condition+0x14`     | u32                               | base_reward_count         | `1` to `11` |
| `reward_condition+0x18`     | Reward Entry[base_reward_count]   | base_rewards              | See Reward Entry; 3,304 items (`reward_type` `3`) and 11 coupons (`6`) |
| `base_rewards+0x00`         | u32                               | select_reward_count       | `0` on 1,648 rows, up to `7` |
| `base_rewards+0x04`         | Reward Entry[select_reward_count] | select_rewards            | The rewards the player picks one of; all 408 are items |
| `select_rewards+0x00`       | u32                               | unknown_select_rewards_00 | `0` on every row of clients 1784 and 3483 |
| `select_rewards+0x04`       | i64                               | unknown_select_rewards_04 | `0` on 1,197 rows; see Open Questions |
| `select_rewards+0x0C`       | u8                                | is_reward_overlapable     | `1` on 1,191 rows, `0` on 588 |
| `select_rewards+0x0D`       | u8                                | is_save_repository        | `1` on every row |
| `select_rewards+0x0E`       | u32                               | optional_type             | Reward group: `0` on 471 rows; see Notes |
| `select_rewards+0x12`       | u8                                | unknown_select_rewards_12 | `1` on 1,268 rows, `0` on 511; see Open Questions |
| `select_rewards+0x13`       | u8                                | is_show_icon              | `1` on 46 rows |
| `select_rewards+0x14`       | u32                               | unknown_select_rewards_14 | `0` on every row of clients 1784 and 3483; the row ends here |

### Reward Entry (178 bytes)

The entry of the [`quest.dbss` Reward Entry](quest_dbss.md#reward-entry-178-bytes),
read by the same reader (`_common/quest/reward_entry.py`). Challenges use
two reward types: items (`3`) and coupons (`6`).

| Offset  | Type      | Field                | Notes |
| ------- | --------- | -------------------- | ----- |
| `+0x00` | u32       | reward_type          | `3` item or `6` coupon; see Reward Types in [`quest.dbss`](quest_dbss.md#reward-types) |
| `+0x04` | i64       | experience           | `0` on every entry |
| `+0x0C` | i32       | skill_experience     | `0` on every entry |
| `+0x10` | i32       | product_experience   | `0` on every entry |
| `+0x14` | u8        | life_experience_type | `15` on every entry |
| `+0x15` | i32       | life_experience      | `0` on every entry |
| `+0x19` | u32       | item_key             | Item of type `3`, packed as `enchant_level << 24 \| item_id` |
| `+0x1D` | i64       | item_count           | Amount of `item_key` |
| `+0x25` | u16       | intimacy_character   | `0` on every entry |
| `+0x27` | i32       | intimacy_value       | `0` on every entry |
| `+0x2B` | i32       | mental_card_key      | `0` on every entry |
| `+0x2F` | bytes[2]  | unknown_2f           | The `coupon(n)` argument of a type `6` entry as a u16 (`5` to `109`); zero on every item; see Field Names |
| `+0x31` | u8        | exp_grade            | `0` on every entry |
| `+0x32` | bytes[4]  | unknown_32           | Zero on every entry |
| `+0x36` | bytes[49] | unknown_36           | u32 `16`, then 45 zero bytes, on every entry |
| `+0x67` | bytes[53] | family_stat          | The `quest.dbss` [Family Stat Union](quest_dbss.md#family-stat-union-53-bytes); `family_stat_type` `16` (no stat) on every entry |
| `+0x9C` | bytes[4]  | unknown_9c           | Zero on every entry |
| `+0xA0` | u32       | max_fever_point      | `0` on every entry |
| `+0xA4` | u32       | add_fever_point      | `0` on every entry |
| `+0xA8` | u8        | unknown_a8           | `0` on every entry |
| `+0xA9` | u8        | season_no            | `0` on every entry |
| `+0xAA` | i64       | explore_exp          | `0` on every entry |

### `challengeoffset.dbss`

Bare offset table into `challenge.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `challenge.dbss` count      |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | challenge_key | Key of the record it points at                                        |
| `+0x02` | u32  | data_offset   | Absolute offset in `challenge.dbss` of the row, past the key prefix   |
| `+0x06` | u32  | data_size     | Row size in bytes, without the key prefix                             |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. Neither the
index rows nor the records are sorted by key; read in offset order the
index rows cover the main file from `+0x04` to its end, each record's key
prefix included (clients 1784 and 3483).

## Layout 1

A reward entry is 10 bytes longer, and an i64 `expected_price` sits between
`is_save_repository` and `optional_type`.

### Row (variable: 98 bytes + texts and rewards)

| Offset                      | Type                              | Field                     | Notes |
| --------------------------- | --------------------------------- | ------------------------- | ----- |
| `+0x00`                     | u16                               | challenge_key             | |
| `+0x02`                     | u32                               | challenge_type            | |
| `+0x06`                     | str16                             | title_kr                  | |
| `title_kr+0x00`             | str16                             | description_kr            | |
| `description_kr+0x00`       | str16                             | progress_condition        | |
| `progress_condition+0x00`   | str16                             | reward_condition          | |
| `reward_condition+0x00`     | u32                               | complete_condition_type   | |
| `reward_condition+0x04`     | i32                               | condition_param1          | |
| `reward_condition+0x08`     | i32                               | condition_param2          | |
| `reward_condition+0x0C`     | u32                               | reset_type                | |
| `reward_condition+0x10`     | i32                               | reset_value               | |
| `reward_condition+0x14`     | u32                               | base_reward_count         | |
| `reward_condition+0x18`     | Reward Entry[base_reward_count]   | base_rewards              | |
| `base_rewards+0x00`         | u32                               | select_reward_count       | |
| `base_rewards+0x04`         | Reward Entry[select_reward_count] | select_rewards            | |
| `select_rewards+0x00`       | u32                               | unknown_select_rewards_00 | |
| `select_rewards+0x04`       | i64                               | unknown_select_rewards_04 | |
| `select_rewards+0x0C`       | u8                                | is_reward_overlapable     | |
| `select_rewards+0x0D`       | u8                                | is_save_repository        | |
| `select_rewards+0x0E`       | i64                               | expected_price            | `1` on every row of client 1784 |
| `select_rewards+0x16`       | u32                               | optional_type             | |
| `select_rewards+0x1A`       | u8                                | unknown_select_rewards_12 | |
| `select_rewards+0x1B`       | u8                                | is_show_icon              | |
| `select_rewards+0x1C`       | u32                               | unknown_select_rewards_14 | |

### Reward Entry (188 bytes)

The 10 extra bytes lie after `family_stat`, as in the client 1784 entries of
[`guildquest.dbss`](guildquest_dbss.md#reward-entry-188-bytes): `unknown_9c`
is 10 bytes long, and 4 zero bytes follow `season_no`.

| Offset  | Type      | Field                   | Notes |
| ------- | --------- | ----------------------- | ----- |
| `+0x00` | u32       | reward_type             | |
| `+0x04` | i64       | experience              | |
| `+0x0C` | i32       | skill_experience        | |
| `+0x10` | i32       | product_experience      | |
| `+0x14` | u8        | life_experience_type    | |
| `+0x15` | i32       | life_experience         | |
| `+0x19` | u32       | item_key                | |
| `+0x1D` | i64       | item_count              | |
| `+0x25` | u16       | intimacy_character      | |
| `+0x27` | i32       | intimacy_value          | |
| `+0x2B` | i32       | mental_card_key         | |
| `+0x2F` | bytes[2]  | unknown_2f              | |
| `+0x31` | u8        | exp_grade               | |
| `+0x32` | bytes[4]  | unknown_32              | |
| `+0x36` | bytes[49] | unknown_36              | |
| `+0x67` | bytes[53] | family_stat             | |
| `+0x9C` | bytes[10] | unknown_9c              | Zero on every entry |
| `+0xA6` | u32       | max_fever_point         | |
| `+0xAA` | u32       | add_fever_point         | |
| `+0xAE` | u8        | unknown_a8              | |
| `+0xAF` | u8        | season_no               | |
| `+0xB0` | bytes[4]  | unknown_after_season_no | Zero on every entry |
| `+0xB4` | i64       | explore_exp             | |

## Challenge Types

`challenge_type` names from `CppEnums.ChallengeType` of the client Lua
(`global_define_cpp_enum.luac`, client 3482); the 2016 `gc::ChallengeType`
has the first seven. Rows from client 3483.

| Value | Name                                   | Rows  |
| ----- | -------------------------------------- | ----- |
| `0`   | `eChallengeType_Benefit`               | 0     |
| `1`   | `eChallengeType_Event`                 | 125   |
| `2`   | `eChallengeType_ShortTerm`             | 81    |
| `3`   | `eChallengeType_LongTerm`              | 1,500 |
| `4`   | `eChallengeType_PcRoom`                | 0     |
| `5`   | `eChallengeType_EnchantPcRoomCount`    | 0     |
| `6`   | `eChallengeType_EnchantValuePackCount` | 0     |
| `7`   | `eChallengeType_PremiumPackage`        | 0     |
| `8`   | `eChallengeType_Coupon`                | 11    |
| `9`   | (`eChallengeType_Count` in the Lua)    | 62    |

The 11 type `8` rows are exactly the rows with a coupon reward. The 62 type
`9` rows are the Pearl spending challenges (`[이벤트] 5000펄 사용`,
completion type `10`); 33 of them are the grouped challenges of
[`pearlusedchallengegroup.bss`](../bss/pearlusedchallengegroup_bss.md).

## Completion Types

`complete_condition_type` names from the 2016 `gc::CompleteChallengeType`;
the parameter notes from the developer comment on the `CompleteConditionType`
column of the client 1784 challenge sheet. Values `8`, `10`, `16` and `17`
are not in the 2016 enum. Rows from client 3483.

| Value | Name                           | Rows | Parameters |
| ----- | ------------------------------ | ---- | ---------- |
| `0`   | `eCompleteType_PastMinute`     | 0    | `condition_param1` minutes after login, not accumulated |
| `1`   | `eCompleteType_Contact`        | 409  | None: done on login |
| `2`   | `eCompleteType_AchieveLevel`   | 413  | `condition_param1` level; `condition_param2` a class type on 230 rows, matching `checkClass(n);` in `reward_condition` on 197 |
| `3`   | `eCompleteType_FirstLogin`     | 40   | `condition_param1` first logins of a day |
| `4`   | `eCompleteType_AchieveLifeLevel` | 41 | `condition_param1` life skill type, `condition_param2` level |
| `5`   | `eCompleteType_PlayTime`       | 76   | Accumulated play time; the comment reads `condition_param1` `0` as family, `1` as character |
| `6`   | `eCompleteType_PcRoomPlayTime` | 0    | |
| `8`   |                                | 697  | `condition_param1` one less than the minutes in the title: `29`, `59`, `89`, `119` and `179` on 278 rows titled with a 30 to 180 minute reward (`60분 보상`); also `57`, `117`, `177` and more |
| `10`  |                                | 62   | `condition_param1` Pearls spent (`500` to `20,000`) |
| `16`  |                                | 21   | `condition_param1` wins in the Solare ranked match (`솔라레의 창 랭크 대전 1승 달성`) |
| `17`  |                                | 20   | `condition_param1` `340` and up, `condition_param2` `1` |

## Reset Types

`reset_type` names from the 2016 `gc::ChallengeResetType`; the comment on
the client 1784 `ResetType` column gives `reset_value` as days for `2` and
as minutes for `3`. Values `4` and `5` are not in the 2016 enum; all 62 of
them are completion type `10`. Rows from client 3483.

| Value | Name                              | Rows |
| ----- | --------------------------------- | ---- |
| `0`   | `eChallengeReset_None`            | 935  |
| `1`   | `eChallengeReset_Immediately`     | 0    |
| `2`   | `eChallengeReset_Day`             | 782  |
| `3`   | `eChallengeReset_CumulatedMinute` | 0    |
| `4`   |                                   | 20   |
| `5`   |                                   | 42   |

## Field Names

The 2016 `gc::ChallengeStaticStatus` holds, in this order, `_key` (u16),
`_challengeType`, `_title`, `_description` (wide strings), `_acceptConditions`
with `_acceptConditionsText`, `_completeType`, `_completeParam1`,
`_completeParam2`, `_resetType`, `_resetValue`, `_rewardGroup`
(`gc::QuestRewardGroup`: `_baseReward`, `_selectReward`, `_expectedPrice`),
`_isRewardOverlapable`, `_isSaveRepository` (bools) and `_expectedPrice`
(`__int64`). The `Challenge_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `Key`, `Type`, `Title`,
`Desc`, `ProgressCondition`, `RewardCondition`, `CompleteConditionType`,
`ConditionParam1`, `ConditionParam2`, `ResetType`, `ResetValue`,
`BaseReward`, `SelectReward`, `isRewardOverlapable`, `isSaveRepository`,
`ExpectedPrice`, `optionalType`, `isShowIcon` and `SeasonAutoClose`, 1,114
rows. Matched by `Key`, empty cells (`<null>`) as empty strings or `0`, the
reward columns as their `item(id,level,count);` and `coupon(n);` calls:

| Field                   | Column                  | Same value (client 1784) | Same value (client 3483) |
| ----------------------- | ----------------------- | ------------------------ | ------------------------ |
| challenge_key           | `Key`                   | 1,091 of 1,091           | 1,041 of 1,041           |
| challenge_type          | `Type`                  | 1,091 of 1,091           | 1,041 of 1,041           |
| title_kr                | `Title`                 | 1,091 of 1,091           | 1,031 of 1,041           |
| description_kr          | `Desc`                  | 1,091 of 1,091           | 851 of 1,041             |
| progress_condition      | `ProgressCondition`     | 1,091 of 1,091           | 1,032 of 1,041           |
| reward_condition        | `RewardCondition`       | 1,085 of 1,091           | 1,035 of 1,041           |
| complete_condition_type | `CompleteConditionType` | 1,091 of 1,091           | 1,041 of 1,041           |
| condition_param1        | `ConditionParam1`       | 1,091 of 1,091           | 1,041 of 1,041           |
| condition_param2        | `ConditionParam2`       | 1,091 of 1,091           | 1,041 of 1,041           |
| reset_type              | `ResetType`             | 1,091 of 1,091           | 1,041 of 1,041           |
| reset_value             | `ResetValue`            | 1,091 of 1,091           | 1,041 of 1,041           |
| base_rewards            | `BaseReward`            | 1,090 of 1,091           | 708 of 1,041             |
| select_rewards          | `SelectReward`          | 1,091 of 1,091           | 1,031 of 1,041           |
| is_reward_overlapable   | `isRewardOverlapable`   | 1,091 of 1,091           | 1,041 of 1,041           |
| is_save_repository      | `isSaveRepository`      | 1,091 of 1,091           | 1,041 of 1,041           |
| expected_price          | `ExpectedPrice`         | 1,091 of 1,091           | (Layout 2 has no field)  |
| optional_type           | `optionalType`          | 1,091 of 1,091           | 1,039 of 1,041           |
| is_show_icon            | `isShowIcon`            | 1,091 of 1,091           | 1,041 of 1,041           |

- The six client 1784 `reward_condition` misses hold
  `getLevel()>14;getLevel()<60;` where the sheet cell is empty; the
  `base_rewards` miss lacks the sheet's `item(750022,0,5);`, the one sheet
  item that [`challengerewardlist.bss`](../bss/challengerewardlist_bss.md) does not
  list either. The client 3483 misses are later edits.
- `isSaveRepository` and `ExpectedPrice` are `1` on every sheet row and
  every row of client 1784, so those two fields take their names from the
  column order, which matches the 2016 member order.
- In the `datasheet_challenge.xlsm` source of that sheet the column reads
  `%ProgressCondition`, the prefix of a server-only column, and its cells
  hold `checkPeriod(...)` scripts; the compiled column keeps `0` or empty.
- `coupon(n)` is the call of all 9 coupon rewards in the sheet; its argument
  equals the u16 at `+0x2F` of each type `6` entry on client 1784 (9 of 9).
  The shared reader keeps the field as `unknown_2f`, since `quest.dbss` and
  `guildquest.dbss` have no coupon entry.
- `SeasonAutoClose` (the season-end clean-up of a challenge's records,
  per its comment) is not compiled into this file; 22 rows set it.
- The xlsm comment on `isShowIcon`: shows an alert of how much longer the
  player must stay logged in to complete the challenge.

## Notes

- Rewards with the same non-zero `optional_type` form one row on the
  Rewards tab: `panel_characterinfo_challenge_all_1.luac` groups the
  rewards by `getOptionalType()` and counts a group with
  `ToClient_GetChallengeRewardCountByOptionalType()`. On client 3483, 33 of
  the 1,197 distinct non-zero values are shared by more than one challenge
  (144 rows), up to 12 challenges each (`465`, `848`).
- LOC type 48 holds each title under `(challenge_key, 0, 12, 0)` and each
  description under `(challenge_key, 0, 12, 1)`. On client 3483, 1,772 of
  the 1,779 keys have their row (`15150` to `15156` have none); 255 LOC
  keys have no row here, 144 with `str_id3` `12` and the 111 keys `10000`
  to `10167` with `str_id3` `28`.
- `unknown_select_rewards_04` scales with the reward items: on the rows
  whose only reward is one item, it is the item count times `1,000,000` for
  Gold Bar 100G (`3`), times `10,000,000` for Gold Bar 1,000G (`4`) and `0`
  on the 214 rows of `[Event] Reward Seal` (`752682`) (client 3483). It changed on 250
  of the 1,041 keys shared by clients 1784 and 3483.
- The client Lua reads the challenges through `ToClient_GetProgressChallengeAt()`,
  `ToClient_GetCompletedChallengeAt()` and `ToClient_GetChallengeRewardInfoWrapper()`;
  no Lua function names the file.

## Open Questions

### What `unknown_select_rewards_04` Holds

The 2016 `gc::QuestRewardGroup` ends with an `__int64 _expectedPrice`
right after `_selectReward`, the place of this i64. The value tracks the
reward items (see Notes), which reads as a price of the rewards computed at
build time, but the item prices it would sum are not checked against
[`itemenchant.dbss`](itemenchant_dbss.md). The same field of `quest.dbss`
and `guildquest.dbss` is unnamed too.

### What `unknown_select_rewards_12` Marks

The byte is `1` on 1,268 rows, all without selectable rewards, and `0` on
the 131 rows with them and on 380 more (client 3483); client 1784 shows the
same split. No sheet column of client 1784 matches it.
