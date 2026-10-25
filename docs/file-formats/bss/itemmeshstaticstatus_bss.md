# `itemmeshstaticstatus.bss` Format

## Purpose

The item mesh table: per mesh key the `.pac` model an equipped item shows,
with its weapon and armor material, its age rating and whether
[`itemeffectchange.dbss`](../dbss/itemeffectchange_dbss.md) switches the model by
enhancement level. The mesh keys are the `item_mesh_key` values of the
[`itemenchant.dbss`](../dbss/itemenchant_dbss.md) Class Entry list, which name one
mesh per class type for each item.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes     | Records    | Row bytes                |
| ------ | -------------- | -------------------------- | --------- | ---------- | ------------------------ |
| 2      | 3387 and later | `itemmeshstaticstatus.bss` | 2,104,179 | 25,749 Row | 71 to 108, 82 on average |
| 1      | 3052 to 3381   | `itemmeshstaticstatus.bss` | 1,951,696 | 24,466 Row | 69 to 106, 80 on average |

| Layout | File                       | Known               | Unknown           |
| ------ | -------------------------- | ------------------- | ----------------- |
| 2      | `itemmeshstaticstatus.bss` | 1,872,438 B (89.0%) | 231,741 B (11.0%) |
| 1      | `itemmeshstaticstatus.bss` | 1,755,968 B (90.0%) | 195,728 B (10.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `557604698418`  |
| 3482   | Layout 2 | `557604698418`  |
| 3474   | Layout 2 | `557604698418`  |
| 3473   | Layout 2 | `557604698418`  |
| 3464   | Layout 2 | `557604698418`  |
| 3458   | Layout 2 | `557604698418`  |
| 3454   | Layout 2 | `557604698418`  |
| 3444   | Layout 2 | `557604698418`  |
| 3435   | Layout 2 | `557604698418`  |
| 3426   | Layout 2 | `557604698418`  |
| 3418   | Layout 2 | `557604698418`  |
| 3412   | Layout 2 | `557604698418`  |
| 3402   | Layout 2 | `557604698418`  |
| 3396   | Layout 2 | `557604698418`  |
| 3387   | Layout 2 | `557604698418`  |
| 3381   | Layout 1 | `557604698418`  |
| 3373   | Layout 1 | `557604698418`  |
| 3364   | Layout 1 | `557604698418`  |
| 3356   | Layout 1 | `557604698418`  |
| 3349   | Layout 1 | `557604698418`  |
| 3342   | Layout 1 | `557604698418`  |
| 3335   | Layout 1 | `557604698418`  |
| 3326   | Layout 1 | `557604698418`  |
| 3321   | Layout 1 | `557604698418`  |
| 3314   | Layout 1 | `557604698418`  |
| 3303   | Layout 1 | `557604698418`  |
| 3302   | Layout 1 | `557604698418`  |
| 3293   | Layout 1 | `557604698418`  |
| 3283   | Layout 1 | `557604698418`  |
| 3275   | Layout 1 | `557604698418`  |
| 3267   | Layout 1 | `557604698418`  |
| 3258   | Layout 1 | `557604698418`  |
| 3251   | Layout 1 | `557604698418`  |
| 3242   | Layout 1 | `557604698418`  |
| 3235   | Layout 1 | `557604698418`  |
| 3229   | Layout 1 | `557604698418`  |
| 3212   | Layout 1 | `557604698418`  |
| 3203   | Layout 1 | `557604698418`  |
| 3193   | Layout 1 | `557604698418`  |
| 3186   | Layout 1 | `557604698418`  |
| 3177   | Layout 1 | `557604698418`  |
| 3169   | Layout 1 | `557604698418`  |
| 3158   | Layout 1 | `557604698418`  |
| 3151   | Layout 1 | `557604698418`  |
| 3144   | Layout 1 | `557604698418`  |
| 3133   | Layout 1 | `557604698418`  |
| 3125   | Layout 1 | `557604698418`  |
| 3118   | Layout 1 | `557604698418`  |
| 3111   | Layout 1 | `557604698418`  |
| 3103   | Layout 1 | `557604698418`  |
| 3095   | Layout 1 | `557604698418`  |
| 3086   | Layout 1 | `557604698418`  |
| 3072   | Layout 1 | `557604698418`  |
| 3062   | Layout 1 | `557604698418`  |
| 3052   | Layout 1 | `557604698418`  |
| 3045   | No file  | `557604698418`  |
| 3037   | No file  | `557604698418`  |
| 3030   | No file  | `557604698418`  |
| 3021   | No file  | `557604698418`  |
| 3012   | No file  | `557604698418`  |
| 3002   | No file  | `557604698418`  |
| 2995   | No file  | `557604698418`  |
| 2987   | No file  | `557604698418`  |
| 2978   | No file  | `557604698418`  |
| 2970   | No file  | `557604698418`  |
| 2959   | No file  | `557604698418`  |
| 2951   | No file  | `557604698418`  |
| 2942   | No file  | `557604698418`  |
| 2935   | No file  | `557604698418`  |
| 2932   | No file  | `557604698418`  |
| 2923   | No file  | `557604698418`  |
| 2919   | No file  | `557604698418`  |
| 2907   | No file  | `557604698418`  |
| 2900   | No file  | `557604698418`  |
| 2891   | No file  | `557604698418`  |
| 2882   | No file  | `557604698418`  |
| 2872   | No file  | `557604698418`  |
| 2863   | No file  | `557604698418`  |
| 2855   | No file  | `557604698418`  |
| 2849   | No file  | `557604698418`  |
| 2844   | No file  | `557604698418`  |
| 2834   | No file  | `557604698418`  |
| 2825   | No file  | `557604698418`  |
| 2819   | No file  | `557604698418`  |
| 2811   | No file  | `557604698418`  |
| 2803   | No file  | `557604698418`  |
| 2794   | No file  | `557604698418`  |
| 2783   | No file  | `557604698418`  |
| 2774   | No file  | `557604698418`  |
| 2765   | No file  | `557604698418`  |
| 2756   | No file  | `557604698418`  |
| 2750   | No file  | `557604698418`  |
| 2743   | No file  | `557604698418`  |
| 2736   | No file  | `557604698418`  |
| 2726   | No file  | `557604698418`  |
| 2717   | No file  | `557604698418`  |
| 2709   | No file  | `557604698418`  |
| 2703   | No file  | `557604698418`  |
| 2695   | No file  | `557604698418`  |
| 2684   | No file  | `557604698418`  |
| 2672   | No file  | `557604698418`  |
| 2665   | No file  | `557604698418`  |
| 2657   | No file  | `557604698418`  |
| 2649   | No file  | `557604698418`  |
| 2644   | No file  | `557604698418`  |
| 2637   | No file  | `557604698418`  |
| 2629   | No file  | `557604698418`  |
| 2619   | No file  | `557604698418`  |
| 2612   | No file  | `557604698418`  |
| 2606   | No file  | `557604698418`  |
| 2602   | No file  | `557604698418`  |
| 2601   | No file  | `557604698418`  |
| 2592   | No file  | `557604698418`  |
| 2583   | No file  | `557604698418`  |
| 2575   | No file  | `557604698418`  |
| 2567   | No file  | `557604698418`  |
| 2560   | No file  | `557604698418`  |
| 2553   | No file  | `557604698418`  |
| 2545   | No file  | `557604698418`  |
| 2538   | No file  | `557604698418`  |
| 2529   | No file  | `557604698418`  |
| 2519   | No file  | `557604698418`  |
| 2513   | No file  | `557604698418`  |
| 2510   | No file  | `557604698418`  |
| 2507   | No file  | `557604698418`  |
| 2503   | No file  | `557604698418`  |
| 2498   | No file  | `557604698418`  |
| 2492   | No file  | `557604698418`  |
| 2487   | No file  | `557604698418`  |
| 2480   | No file  | `557604698418`  |
| 2474   | No file  | `557604698418`  |
| 2468   | No file  | `557604698418`  |
| 2460   | No file  | `557604698418`  |
| 2453   | No file  | `557604698418`  |
| 2444   | No file  | `557604698418`  |
| 2438   | No file  | `557604698418`  |
| 2434   | No file  | `557604698418`  |
| 2429   | No file  | `557604698418`  |
| 2421   | No file  | `557604698418`  |
| 2414   | No file  | `557604698418`  |
| 2407   | No file  | `557604698418`  |
| 2401   | No file  | `557604698418`  |
| 2397   | No file  | `557604698418`  |
| 2393   | No file  | `557604698418`  |
| 2384   | No file  | `557604698418`  |
| 2378   | No file  | `557604698418`  |
| 2372   | No file  | `557604698418`  |
| 2358   | No file  | `557604698418`  |
| 2352   | No file  | `557604698418`  |
| 2347   | No file  | `557604698418`  |
| 2343   | No file  | `557604698418`  |
| 2335   | No file  | `557604698418`  |
| 2327   | No file  | `557604698418`  |
| 2324   | No file  | `557604698418`  |
| 2319   | No file  | `557604698418`  |
| 2313   | No file  | `557604698418`  |
| 2308   | No file  | `557604698418`  |
| 2302   | No file  | `557604698418`  |
| 2295   | No file  | `557604698418`  |
| 2290   | No file  | `557604698418`  |
| 2284   | No file  | `557604698418`  |
| 2276   | No file  | `557604698418`  |
| 2269   | No file  | `557604698418`  |
| 2259   | No file  | `557604698418`  |
| 2250   | No file  | `557604698418`  |
| 2243   | No file  | `557604698418`  |
| 2235   | No file  | `557604698418`  |
| 2229   | No file  | `557604698418`  |
| 2224   | No file  | `557604698418`  |
| 2218   | No file  | `557604698418`  |
| 2215   | No file  | `557604698418`  |
| 2207   | No file  | `557604698418`  |
| 2203   | No file  | `557604698418`  |
| 2196   | No file  | `557604698418`  |
| 2192   | No file  | `557604698418`  |
| 2189   | No file  | `557604698418`  |
| 2183   | No file  | `557604698418`  |
| 2179   | No file  | `557604698418`  |
| 2171   | No file  | `557604698418`  |
| 2163   | No file  | `557604698418`  |
| 2156   | No file  | `557604698418`  |
| 2151   | No file  | `557604698418`  |
| 2147   | No file  | `557604698418`  |
| 2142   | No file  | `557604698418`  |
| 2138   | No file  | `557604698418`  |
| 2134   | No file  | `557604698418`  |
| 2130   | No file  | `557604698418`  |
| 2122   | No file  | `557604698418`  |
| 2107   | No file  | `557604698418`  |
| 2098   | No file  | `557604698418`  |
| 2089   | No file  | `557604698418`  |
| 2081   | No file  | `557604698418`  |
| 2073   | No file  | `557604698418`  |
| 2067   | No file  | `557604698418`  |
| 2063   | No file  | `557604698418`  |
| 2059   | No file  | `557604698418`  |
| 2052   | No file  | `557604698418`  |
| 2044   | No file  | `557604698418`  |
| 2039   | No file  | `557604698418`  |
| 2032   | No file  | `557604698418`  |
| 2025   | No file  | `557604698418`  |
| 2011   | No file  | `557604698418`  |
| 2005   | No file  | `557604698418`  |
| 2000   | No file  | `557604698418`  |
| 1996   | No file  | `557604698418`  |
| 1991   | No file  | `557604698418`  |
| 1985   | No file  | `557604698418`  |
| 1980   | No file  | `557604698418`  |
| 1969   | No file  | `557604698418`  |
| 1964   | No file  | `557604698418`  |
| 1958   | No file  | `557604698418`  |
| 1950   | No file  | `557604698418`  |
| 1945   | No file  | `557604698418`  |
| 1937   | No file  | `557604698418`  |
| 1933   | No file  | `557604698418`  |
| 1927   | No file  | `557604698418`  |
| 1921   | No file  | `557604698418`  |
| 1914   | No file  | `557604698418`  |
| 1908   | No file  | `557604698418`  |
| 1897   | No file  | `557604698418`  |
| 1892   | No file  | `557604698418`  |
| 1886   | No file  | `557604698418`  |
| 1881   | No file  | `557604698418`  |
| 1871   | No file  | `557604698418`  |
| 1866   | No file  | `557604698418`  |
| 1862   | No file  | `557604698418`  |
| 1854   | No file  | `557604698418`  |
| 1846   | No file  | `557604698418`  |
| 1838   | No file  | `557604698418`  |
| 1832   | No file  | `557604698418`  |
| 1826   | No file  | `557604698418`  |
| 1822   | No file  | `557604698418`  |
| 1818   | No file  | `557604698418`  |
| 1804   | No file  | `557604698418`  |
| 1794   | No file  | `557604698418`  |
| 1790   | No file  | `557604698418`  |
| 1784   | No file  | `557604698418`  |
| 1774   | No file  | `557604698418`  |
| 1771   | No file  | `557604698418`  |
| 1762   | No file  | `557604698418`  |
| 1759   | No file  | `557604698418`  |
| 1754   | No file  | `557604698418`  |
| 1749   | No file  | `557604698418`  |
| 1743   | No file  | `557604698418`  |
| 1737   | No file  | `557604698418`  |
| 1731   | No file  | `557604698418`  |
| 1725   | No file  | `557604698418`  |
| 1717   | No file  | `557604698418`  |
| 1710   | No file  | `557604698418`  |
| 1704   | No file  | `557604698418`  |
| 1698   | No file  | `557604698418`  |
| 1690   | No file  | `557604698418`  |
| 1685   | No file  | `557604698418`  |
| 1680   | No file  | `557604698418`  |
| 1674   | No file  | `557604698418`  |
| 1668   | No file  | `557604698418`  |
| 1659   | No file  | `557604698418`  |
| 1649   | No file  | `557604698418`  |
| 1642   | No file  | `557604698418`  |
| 1636   | No file  | `557604698418`  |
| 1628   | No file  | `557604698418`  |
| 1622   | No file  | `557604698418`  |
| 1614   | No file  | `557604698418`  |
| 1608   | No file  | `557604698418`  |
| 1602   | No file  | `557604698418`  |
| 1598   | No file  | `557604698418`  |
| 1594   | No file  | `557604698418`  |
| 1590   | No file  | `557604698418`  |
| 1587   | No file  | `557604698418`  |
| 1584   | No file  | `557604698418`  |
| 1579   | No file  | `557604698418`  |
| 1572   | No file  | `557604698418`  |
| 1565   | No file  | `557604698418`  |
| 1559   | No file  | `557604698418`  |
| 1554   | No file  | `557604698418`  |
| 1547   | No file  | `557604698418`  |
| 1537   | No file  | `557604698418`  |
| 1529   | No file  | `557604698418`  |
| 1524   | No file  | `557604698418`  |
| 1519   | No file  | `557604698418`  |
| 1509   | No file  | `557604698418`  |
| 1506   | No file  | `557604698418`  |
| 1504   | No file  | `557604698418`  |
| 1500   | No file  | `557604698418`  |
| 1493   | No file  | `557604698418`  |
| 1489   | No file  | `557604698418`  |
| 1485   | No file  | `557604698418`  |
| 1481   | No file  | `557604698418`  |
| 1474   | No file  | `557604698418`  |
| 1466   | No file  | `557604698418`  |
| 1462   | No file  | `557604698418`  |
| 1459   | No file  | `557604698418`  |
| 1453   | No file  | `557604698418`  |
| 1450   | No file  | `557604698418`  |
| 1445   | No file  | `557604698418`  |
| 1439   | No file  | `557604698418`  |
| 1433   | No file  | `557604698418`  |
| 1430   | No file  | `557604698418`  |
| 1426   | No file  | `557604698418`  |
| 1421   | No file  | `557604698418`  |
| 1417   | No file  | `557604698418`  |
| 1416   | No file  | `557604698418`  |
| 1409   | No file  | `557604698418`  |
| 1405   | No file  | `557604698418`  |
| 1401   | No file  | `557604698418`  |
| 1396   | No file  | `557604698418`  |
| 1391   | No file  | `557604698418`  |
| 1390   | No file  | `557604698418`  |
| 1386   | No file  | `557604698418`  |
| 1381   | No file  | `557604698418`  |
| 1379   | No file  | `557604698418`  |
| 1372   | No file  | `557604698418`  |
| 1366   | No file  | `557604698418`  |
| 1364   | No file  | `557604698418`  |
| 1363   | No file  | `557604698418`  |
| 1360   | No file  | `557604698418`  |
| 1358   | No file  | `557604698418`  |
| 1355   | No file  | `557604698418`  |
| 1351   | No file  | `557604698418`  |
| 1348   | No file  | `557604698418`  |
| 1346   | No file  | `557604698418`  |
| 1341   | No file  | `557604698418`  |
| 1340   | No file  | `557604698418`  |
| 1338   | No file  | `557604698418`  |
| 1335   | No file  | `557604698418`  |
| 1333   | No file  | `557604698418`  |
| 1329   | No file  | `557604698418`  |
| 1327   | No file  | `557604698418`  |
| 1324   | No file  | `557604698418`  |
| 1321   | No file  | `557604698418`  |
| 1319   | No file  | `557604698418`  |
| 1318   | No file  | `557604698418`  |
| 1316   | No file  | `557604698418`  |
| 1313   | No file  | `557604698418`  |
| 1311   | No file  | `557604698418`  |
| 1309   | No file  | `557604698418`  |
| 1304   | No file  | `557604698418`  |
| 1292   | No file  | `557604698418`  |
| 1286   | No file  | `557604698418`  |
| 1280   | No file  | `557604698418`  |
| 1276   | No file  | `557604698418`  |
| 1267   | No file  | `557604698418`  |
| 1261   | No file  | `557604698418`  |
| 1256   | No file  | `557604698418`  |
| 1250   | No file  | `557604698418`  |
| 1246   | No file  | `557604698418`  |
| 1239   | No file  | `557604698418`  |
| 1230   | No file  | `557604698418`  |
| 1226   | No file  | `557604698418`  |
| 1220   | No file  | `557604698418`  |
| 1217   | No file  | `557604698418`  |
| 1211   | No file  | `557604698418`  |
| 1210   | No file  | `557604698418`  |
| 1208   | No file  | `557604698418`  |
| 1203   | No file  | `557604698418`  |
| 1197   | No file  | `557604698418`  |
| 1194   | No file  | `557604698418`  |
| 1192   | No file  | `557604698418`  |
| 1187   | No file  | `557604698418`  |
| 1183   | No file  | `557604698418`  |
| 1177   | No file  | `557604698418`  |
| 1173   | No file  | `557604698418`  |
| 1167   | No file  | `557604698418`  |
| 1164   | No file  | `557604698418`  |
| 1156   | No file  | `557604698418`  |
| 1149   | No file  | `557604698418`  |
| 1144   | No file  | `557604698418`  |
| 1137   | No file  | `557604698418`  |
| 1132   | No file  | `557604698418`  |
| 1127   | No file  | `557604698418`  |
| 1122   | No file  | `557604698418`  |
| 1118   | No file  | `557604698418`  |
| 1114   | No file  | `557604698418`  |
| 1109   | No file  | `557604698418`  |
| 1102   | No file  | `557604698418`  |
| 1096   | No file  | `557604698418`  |
| 1088   | No file  | `557604698418`  |
| 1081   | No file  | `557604698418`  |
| 1076   | No file  | `557604698418`  |
| 1069   | No file  | `557604698418`  |
| 1064   | No file  | `557604698418`  |
| 1058   | No file  | `557604698418`  |
| 1051   | No file  | `557604698418`  |
| 1044   | No file  | `557604698418`  |
| 1036   | No file  | `557604698418`  |
| 1026   | No file  | `557604698418`  |
| 1016   | No file  | `557604698418`  |
| 1009   | No file  | `557604698418`  |
| 1005   | No file  | `557604698418`  |
| 1000   | No file  | `557604698418`  |
| 998    | No file  | `557604698418`  |
| 990    | No file  | `557604698418`  |
| 979    | No file  | `557604698418`  |
| 972    | No file  | `557604698418`  |
| 963    | No file  | `557604698418`  |
| 955    | No file  | `557604698418`  |
| 946    | No file  | `557604698418`  |
| 938    | No file  | `557604698418`  |
| 927    | No file  | `557604698418`  |
| 911    | No file  | `557604698418`  |
| 904    | No file  | `557604698418`  |
| 899    | No file  | `557604698418`  |
| 894    | No file  | `557604698418`  |
| 885    | No file  | `557604698418`  |
| 879    | No file  | `557604698418`  |
| 872    | No file  | `557604698418`  |
| 864    | No file  | `557604698418`  |
| 855    | No file  | `557604698418`  |
| 853    | No file  | `557604698418`  |
| 845    | No file  | `557604698418`  |
| 837    | No file  | `557604698418`  |
| 829    | No file  | `557604698418`  |
| 822    | No file  | `557604698418`  |
| 814    | No file  | `557604698418`  |
| 805    | No file  | `557604698418`  |
| 794    | No file  | `557604698418`  |
| 787    | No file  | `557604698418`  |
| 780    | No file  | `557604698418`  |
| 771    | No file  | `557604698418`  |
| 760    | No file  | `557604698418`  |
| 748    | No file  | `557604698418`  |
| 741    | No file  | `557604698418`  |
| 736    | No file  | `557604698418`  |
| 731    | No file  | `557604698418`  |
| 723    | No file  | `557604698418`  |
| 711    | No file  | `557604698418`  |
| 707    | No file  | `557604698418`  |
| 697    | No file  | `557604698418`  |
| 689    | No file  | `557604698418`  |
| 683    | No file  | `557604698418`  |
| 678    | No file  | `557604698418`  |
| 670    | No file  | `557604698418`  |
| 661    | No file  | `557604698418`  |
| 656    | No file  | `557604698418`  |
| 652    | No file  | `557604698418`  |
| 643    | No file  | `557604698418`  |
| 637    | No file  | `557604698418`  |
| 630    | No file  | `557604698418`  |
| 627    | No file  | `557604698418`  |
| 621    | No file  | `557604698418`  |
| 617    | No file  | `557604698418`  |
| 615    | No file  | `557604698418`  |
| 606    | No file  | `557604698418`  |
| 599    | No file  | `557604698418`  |
| 592    | No file  | `557604698418`  |
| 586    | No file  | `557604698418`  |
| 577    | No file  | `557604698418`  |
| 569    | No file  | `557604698418`  |
| 561    | No file  | `557604698418`  |
| 554    | No file  | `557604698418`  |
| 542    | No file  | `557604698418`  |
| 532    | No file  | `557604698418`  |
| 531    | No file  | `557604698418`  |
| 526    | No file  | `557604698418`  |
| 521    | No file  | `557604698418`  |
| 517    | No file  | `557604698418`  |
| 510    | No file  | `557604698418`  |
| 508    | No file  | `557604698418`  |
| 504    | No file  | `557604698418`  |
| 497    | No file  | `557604698418`  |
| 491    | No file  | `557604698418`  |
| 485    | No file  | `557604698418`  |
| 478    | No file  | `557604698418`  |
| 472    | No file  | `557604698418`  |
| 466    | No file  | `557604698418`  |
| 457    | No file  | `557604698418`  |
| 452    | No file  | `557604698418`  |
| 449    | No file  | `557604698418`  |
| 435    | No file  | `557604698418`  |

<!-- versions:end -->

## Companion Files

None. The handler reads the `MESH_KEY_ITEMS` lookup index, built from
`itemenchant.dbss` and `itemenchantoffset.dbss`, for the items that wear
each mesh.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type           | Field     | Notes                                               |
| ------- | -------------- | --------- | --------------------------------------------------- |
| `+0x00` | u32            | row_count | Number of meshes; no PABR magic, no string table    |
| `+0x04` | Row[row_count] | rows      | See Row; in no key order, the last row ends the file |

### Row (variable: 33 bytes + mesh and effect file text)

| Offset                 | Type | Field                  | Notes                                                                                     |
| ---------------------- | ---- | ---------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00`                | str8 | mesh_file              | Lowercase `.pac` path under `character/model/`, e.g. `1_pc/1_phm/weapon/1_onehandsword/phm_01_ohs_0017_r.pac` |
| `mesh_file+0x00`       | str8 | effect_file            | Empty on most rows; `0` on 542 mount, wagon, ship and tent meshes (`4_riding/`) and 3 others, `O_FishingRod_01A` and similar on 212 fishing rods and floats (`weapon/0_com/`) |
| `effect_file+0x00`     | u64  | unknown_effect_file_00 | `0` on every row (client 3483)                                                            |
| `effect_file+0x08`     | u32  | mesh_key               | Item mesh key, unique per row; the `item_mesh_key` of `itemenchant.dbss`                  |
| `effect_file+0x0C`     | u8   | weapon_material        | Weapon material; set only on `weapon/` meshes (see Materials)                             |
| `effect_file+0x0D`     | u8   | unknown_effect_file_0d | `1` on 11 rows, `0` on the rest (client 3483)                                             |
| `effect_file+0x0E`     | u8   | armor_material         | Armor material; also set on shields (see Materials)                                       |
| `effect_file+0x0F`     | u8   | adult                  | Age rating: `0` all ages, `1` age 19 and over (see Field Names)                           |
| `effect_file+0x10`     | u8   | effects_change_type    | `1` when `itemeffectchange.dbss` has a model per enhancement level for the mesh, else `0` |

## Layout 1

The row has no `weapon_material` and no `unknown_effect_file_0d`. Only the
Row differs from Layout 2.

### Row (variable: 31 bytes + mesh and effect file text)

| Offset             | Type | Field                  | Notes |
| ------------------ | ---- | ---------------------- | ----- |
| `+0x00`            | str8 | mesh_file              |       |
| `mesh_file+0x00`   | str8 | effect_file            |       |
| `effect_file+0x00` | u64  | unknown_effect_file_00 | `0` on every row of clients 3052 and 3381 |
| `effect_file+0x08` | u32  | mesh_key               |       |
| `effect_file+0x0C` | u8   | armor_material         |       |
| `effect_file+0x0D` | u8   | adult                  |       |
| `effect_file+0x0E` | u8   | effects_change_type    |       |

## Field Names

The names come from the `Item_Mesh_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched by `Index` against
`mesh_key`. The sheet shares 14,593 of its 14,599 keys with the 25,749
rows of client 3483:

| Field                 | Column              | Same value on                    |
| --------------------- | ------------------- | -------------------------------- |
| `mesh_key`            | `Index`             | 14,593 shared keys               |
| `mesh_file`           | `UseMeshFile`       | 14,093 (compared in lower case)  |
| `effect_file`         | `UseEffectFile`     | 14,587 (`<null>` read as empty)  |
| `weapon_material`     | `WeaponMaterial`    | 14,517                           |
| `armor_material`      | `ArmorMaterial`     | 14,396                           |
| `adult`               | `Adult`             | 14,563                           |
| `effects_change_type` | `EffectsChangeType` | 14,462                           |

Most misses are reworked rows: all 76 `weapon_material` misses and 174 of
the 197 `armor_material` misses sit on rows whose `mesh_file` changed
since the sheet (`phm_02_hand_0012.pac` became `phm_02_hand_0013.pac`
on key 48035). The 2016 `gc::ItemMeshStaticStatus` has the members
`_key`, `_useMeshFile`, `_weaponMaterial`, `_armorMaterial` and
`_useEffectFile`, which fit the same names.

The developer comments on the sheet give the meanings: `Adult` is `0` for
all ages, `1` for age 19 and over, `2` for 15 to under 19 and `3` for 15
and over; client 3483 uses `0` and `1` only, with `1` on 842 rows, all
under `armor/38_underwear/`. `EffectsChangeType` says whether the mesh
gets an effect per enhancement level, which then needs a row in the
`EffectsChange` sheet, the source of `itemeffectchange.dbss`. On client
3483 `effects_change_type` is `1` on 617 rows: the 596 mesh keys of
`itemeffectchange.dbss` and 21 more.

The sheet has two more string columns, `BoneName` and `BoneFileName`
(`Bip_Weapon_R_Attach_In` and `1_PC/0_Item/Bip_Weapon.pab` on weapons),
and two more numbers, `WeaponMaterialConvertKey` and
`IsDevelopingContents`, both `0` on every sheet row. Neither bone column
has a non-empty match in the file.

## Materials

The values of client 3483, with the model folders that hold most of each.
No 2016 enum names them.

| `weapon_material` | Rows | Folders                                                         |
| ----------------- | ---- | --------------------------------------------------------------- |
| 2                 | 288  | `32_dagger`, `55_shuriken`, `99_dagger`, `56_darts`             |
| 3                 | 665  | `30_elblade`, `1_onehandsword`, `35_blade`, `80_ironmace`       |
| 8                 | 153  | `36_shotbow`, `31_onehandbow`, `77_crossbow`                    |
| 13                | 182  | `8_shield`, `93_ncl`, `81_towershield`, `96_cos`                |
| 14                | 106  | `28_enchantarm`, `66_armlet`, `65_gauntlet`                     |
| 15                | 446  | `6_staff`, `98_staff`, `59_orb`, `65_gauntlet`, `77_crossbow`   |
| 18                | 136  | `29_doubleax`, `89_onehandaxe`, `90_polearm`, `86_shamshir`     |
| 21                | 132  | `38_scythe`, `57_chakram`, `94_czo`, `100_kjm`                  |
| 29                | 73   | `43_twinsword`, `58_katana`, `64_darksword`                     |
| 36                | 129  | `69_kusarigama`, `70_shotblade`, `86_shamshir`, `87_vajra`      |

Values `11`, `12`, `17`, `22`, `23`, `30` to `33` and `57` hold fewer
than 50 rows each. `0` holds the other 23,204 rows: every armor, costume
and `4_riding/` mesh and 1,746 of the 4,291 `weapon/` meshes.

| `armor_material` | Rows  | Folders                                                    |
| ---------------- | ----- | ---------------------------------------------------------- |
| 1                | 3,433 | `armor/9_upperbody`, `armor/39_earring`, `armor/40_glasses`, `armor/13_hel` |
| 2                | 856   | `armor/9_upperbody`, `event_costume`                       |
| 4                | 799   | `armor/9_upperbody`, `armor/10_lowerbody`, `armor/12_foot` |
| 18 to 20         | 212   | `weapon/8_shield`, `weapon/93_ncl`, `weapon/81_towershield` |
| 46 to 48         | 59    | `armor/9_upperbody`                                        |

`0` holds the other 20,390 rows.

## Notes

- 25,125 of the 25,749 `mesh_file` paths are files under
  `character/model/` in the client 3483 PAZ; the other 624 (617 under
  `1_pc/`, 7 under `4_riding/`) are not. 1,350 rows repeat a path another
  row holds.
- `mesh_key` runs from `101` to `336075`. All 22,859 distinct
  `item_mesh_key` values of `itemenchant.dbss` on client 3483 are keys
  here; 2,890 keys are worn by no item.
- Layout 1 and Layout 2 agree on every shared key: on the 19,935 keys
  clients 3381 and 3483 share, `mesh_file`, `effect_file`,
  `armor_material`, `adult` and `effects_change_type` are the same. 4,531
  keys of client 3381 are gone on client 3483, and each of their paths is
  there under another key (`4465` became `70001`); client 3381 keys run up
  to `16821877`.
- Client 1784 has no `itemmeshstaticstatus.bss`. It holds the table as
  `itemmesh.dbss` with the index `itemmeshoffset.dbss`: a u16 key before
  the path, `weapon_material`, a byte that is `0` on every row,
  `armor_material`, the `effect_file` string, `adult` and
  `effects_change_type`. It has no `unknown_effect_file_00`.
- The handler (`_bss/itemmeshstaticstatus/`) shows one row per mesh: the
  key, the items that wear it (from the `MESH_KEY_ITEMS` lookup index), the
  model path, the effect file and the four numbers.

## Open Questions

### What `unknown_effect_file_00` Holds

The eight bytes after `effect_file` are `0` on every row of clients 3052,
3381 and 3483, and client 1784's `itemmesh.dbss` has nothing in their
place. They may be the u64 count of a third string, such as one of the sheet's `BoneName` or
`BoneFileName` columns left empty in the client build; a row with a
non-zero value would tell.

### What `unknown_effect_file_0d` Holds

The byte between `weapon_material` and `armor_material` is `1` on the 11
upper-body meshes with keys `44622` to `44661` (`pkow_00_ub_0267.pac`,
`pqw_10_ub_0007.pac` and others) and `0` on every other row. Client 1784
has a byte in the same place that is `0` on every row. The sheet columns
that are not matched yet, `WeaponMaterialConvertKey` (the developer comment
calls it the key of the weapon draw sound) and `IsDevelopingContents`
(`1` hides content still in development), are both `0` on every sheet
row, so neither can be matched by value.
