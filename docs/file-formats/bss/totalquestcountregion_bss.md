# `totalquestcountregion.bss` Format

## Purpose

Quest totals. `totalquestcountregion.bss` holds the number of quests per quest region (`CppEnums.QuestRegionType` in the client Lua) and `totalquestcounttype.bss` the number of quests per quest type (`__eQuestType`). Value N of a file counts the quests of enum value N; the files store no keys. Both files share this layout and one handler class. On client 3474 the type file's values are, value for value, how many `quest.dbss` records hold each `quest_category` (see [Quest Types](#quest-types)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                        | Bytes | Records        | Row bytes |
| ------ | ------------- | --------------------------- | ----- | -------------- | --------- |
| 1      | 972 and later | `totalquestcountregion.bss` | 88    | 1 String Table | 4         |
| 1      | 972 and later | `totalquestcounttype.bss`   | 96    | 1 String Table | 4         |

| Layout | File                        | Known         | Unknown    |
| ------ | --------------------------- | ------------- | ---------- |
| 1      | `totalquestcountregion.bss` | 88 B (100.0%) | 0 B (0.0%) |
| 1      | `totalquestcounttype.bss`   | 96 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `daaca0977a82`  |
| 3482   | Layout 1 | `daaca0977a82`  |
| 3474   | Layout 1 | `daaca0977a82`  |
| 3473   | Layout 1 | `daaca0977a82`  |
| 3464   | Layout 1 | `daaca0977a82`  |
| 3458   | Layout 1 | `daaca0977a82`  |
| 3454   | Layout 1 | `daaca0977a82`  |
| 3444   | Layout 1 | `daaca0977a82`  |
| 3435   | Layout 1 | `daaca0977a82`  |
| 3426   | Layout 1 | `daaca0977a82`  |
| 3418   | Layout 1 | `daaca0977a82`  |
| 3412   | Layout 1 | `daaca0977a82`  |
| 3402   | Layout 1 | `daaca0977a82`  |
| 3396   | Layout 1 | `daaca0977a82`  |
| 3387   | Layout 1 | `daaca0977a82`  |
| 3381   | Layout 1 | `daaca0977a82`  |
| 3373   | Layout 1 | `daaca0977a82`  |
| 3364   | Layout 1 | `daaca0977a82`  |
| 3356   | Layout 1 | `daaca0977a82`  |
| 3349   | Layout 1 | `daaca0977a82`  |
| 3342   | Layout 1 | `daaca0977a82`  |
| 3335   | Layout 1 | `daaca0977a82`  |
| 3326   | Layout 1 | `daaca0977a82`  |
| 3321   | Layout 1 | `daaca0977a82`  |
| 3314   | Layout 1 | `daaca0977a82`  |
| 3303   | Layout 1 | `daaca0977a82`  |
| 3302   | Layout 1 | `daaca0977a82`  |
| 3293   | Layout 1 | `daaca0977a82`  |
| 3283   | Layout 1 | `daaca0977a82`  |
| 3275   | Layout 1 | `daaca0977a82`  |
| 3267   | Layout 1 | `daaca0977a82`  |
| 3258   | Layout 1 | `daaca0977a82`  |
| 3251   | Layout 1 | `daaca0977a82`  |
| 3242   | Layout 1 | `daaca0977a82`  |
| 3235   | Layout 1 | `daaca0977a82`  |
| 3229   | Layout 1 | `daaca0977a82`  |
| 3212   | Layout 1 | `daaca0977a82`  |
| 3203   | Layout 1 | `daaca0977a82`  |
| 3193   | Layout 1 | `daaca0977a82`  |
| 3186   | Layout 1 | `daaca0977a82`  |
| 3177   | Layout 1 | `daaca0977a82`  |
| 3169   | Layout 1 | `daaca0977a82`  |
| 3158   | Layout 1 | `daaca0977a82`  |
| 3151   | Layout 1 | `daaca0977a82`  |
| 3144   | Layout 1 | `daaca0977a82`  |
| 3133   | Layout 1 | `daaca0977a82`  |
| 3125   | Layout 1 | `daaca0977a82`  |
| 3118   | Layout 1 | `daaca0977a82`  |
| 3111   | Layout 1 | `daaca0977a82`  |
| 3103   | Layout 1 | `daaca0977a82`  |
| 3095   | Layout 1 | `daaca0977a82`  |
| 3086   | Layout 1 | `daaca0977a82`  |
| 3072   | Layout 1 | `daaca0977a82`  |
| 3062   | Layout 1 | `daaca0977a82`  |
| 3052   | Layout 1 | `daaca0977a82`  |
| 3045   | Layout 1 | `daaca0977a82`  |
| 3037   | Layout 1 | `daaca0977a82`  |
| 3030   | Layout 1 | `daaca0977a82`  |
| 3021   | Layout 1 | `daaca0977a82`  |
| 3012   | Layout 1 | `daaca0977a82`  |
| 3002   | Layout 1 | `daaca0977a82`  |
| 2995   | Layout 1 | `daaca0977a82`  |
| 2987   | Layout 1 | `daaca0977a82`  |
| 2978   | Layout 1 | `daaca0977a82`  |
| 2970   | Layout 1 | `daaca0977a82`  |
| 2959   | Layout 1 | `daaca0977a82`  |
| 2951   | Layout 1 | `daaca0977a82`  |
| 2942   | Layout 1 | `daaca0977a82`  |
| 2935   | Layout 1 | `daaca0977a82`  |
| 2932   | Layout 1 | `daaca0977a82`  |
| 2923   | Layout 1 | `daaca0977a82`  |
| 2919   | Layout 1 | `daaca0977a82`  |
| 2907   | Layout 1 | `daaca0977a82`  |
| 2900   | Layout 1 | `daaca0977a82`  |
| 2891   | Layout 1 | `daaca0977a82`  |
| 2882   | Layout 1 | `daaca0977a82`  |
| 2872   | Layout 1 | `daaca0977a82`  |
| 2863   | Layout 1 | `daaca0977a82`  |
| 2855   | Layout 1 | `daaca0977a82`  |
| 2849   | Layout 1 | `daaca0977a82`  |
| 2844   | Layout 1 | `daaca0977a82`  |
| 2834   | Layout 1 | `daaca0977a82`  |
| 2825   | Layout 1 | `daaca0977a82`  |
| 2819   | Layout 1 | `daaca0977a82`  |
| 2811   | Layout 1 | `daaca0977a82`  |
| 2803   | Layout 1 | `daaca0977a82`  |
| 2794   | Layout 1 | `daaca0977a82`  |
| 2783   | Layout 1 | `daaca0977a82`  |
| 2774   | Layout 1 | `daaca0977a82`  |
| 2765   | Layout 1 | `daaca0977a82`  |
| 2756   | Layout 1 | `daaca0977a82`  |
| 2750   | Layout 1 | `daaca0977a82`  |
| 2743   | Layout 1 | `daaca0977a82`  |
| 2736   | Layout 1 | `daaca0977a82`  |
| 2726   | Layout 1 | `daaca0977a82`  |
| 2717   | Layout 1 | `daaca0977a82`  |
| 2709   | Layout 1 | `daaca0977a82`  |
| 2703   | Layout 1 | `daaca0977a82`  |
| 2695   | Layout 1 | `daaca0977a82`  |
| 2684   | Layout 1 | `daaca0977a82`  |
| 2672   | Layout 1 | `daaca0977a82`  |
| 2665   | Layout 1 | `daaca0977a82`  |
| 2657   | Layout 1 | `daaca0977a82`  |
| 2649   | Layout 1 | `daaca0977a82`  |
| 2644   | Layout 1 | `daaca0977a82`  |
| 2637   | Layout 1 | `daaca0977a82`  |
| 2629   | Layout 1 | `daaca0977a82`  |
| 2619   | Layout 1 | `daaca0977a82`  |
| 2612   | Layout 1 | `daaca0977a82`  |
| 2606   | Layout 1 | `daaca0977a82`  |
| 2602   | Layout 1 | `daaca0977a82`  |
| 2601   | Layout 1 | `daaca0977a82`  |
| 2592   | Layout 1 | `daaca0977a82`  |
| 2583   | Layout 1 | `daaca0977a82`  |
| 2575   | Layout 1 | `daaca0977a82`  |
| 2567   | Layout 1 | `daaca0977a82`  |
| 2560   | Layout 1 | `daaca0977a82`  |
| 2553   | Layout 1 | `daaca0977a82`  |
| 2545   | Layout 1 | `daaca0977a82`  |
| 2538   | Layout 1 | `daaca0977a82`  |
| 2529   | Layout 1 | `daaca0977a82`  |
| 2519   | Layout 1 | `daaca0977a82`  |
| 2513   | Layout 1 | `daaca0977a82`  |
| 2510   | Layout 1 | `daaca0977a82`  |
| 2507   | Layout 1 | `daaca0977a82`  |
| 2503   | Layout 1 | `daaca0977a82`  |
| 2498   | Layout 1 | `daaca0977a82`  |
| 2492   | Layout 1 | `daaca0977a82`  |
| 2487   | Layout 1 | `daaca0977a82`  |
| 2480   | Layout 1 | `daaca0977a82`  |
| 2474   | Layout 1 | `daaca0977a82`  |
| 2468   | Layout 1 | `daaca0977a82`  |
| 2460   | Layout 1 | `daaca0977a82`  |
| 2453   | Layout 1 | `daaca0977a82`  |
| 2444   | Layout 1 | `daaca0977a82`  |
| 2438   | Layout 1 | `daaca0977a82`  |
| 2434   | Layout 1 | `daaca0977a82`  |
| 2429   | Layout 1 | `daaca0977a82`  |
| 2421   | Layout 1 | `daaca0977a82`  |
| 2414   | Layout 1 | `daaca0977a82`  |
| 2407   | Layout 1 | `daaca0977a82`  |
| 2401   | Layout 1 | `daaca0977a82`  |
| 2397   | Layout 1 | `daaca0977a82`  |
| 2393   | Layout 1 | `daaca0977a82`  |
| 2384   | Layout 1 | `daaca0977a82`  |
| 2378   | Layout 1 | `daaca0977a82`  |
| 2372   | Layout 1 | `daaca0977a82`  |
| 2358   | Layout 1 | `daaca0977a82`  |
| 2352   | Layout 1 | `daaca0977a82`  |
| 2347   | Layout 1 | `daaca0977a82`  |
| 2343   | Layout 1 | `daaca0977a82`  |
| 2335   | Layout 1 | `daaca0977a82`  |
| 2327   | Layout 1 | `daaca0977a82`  |
| 2324   | Layout 1 | `daaca0977a82`  |
| 2319   | Layout 1 | `daaca0977a82`  |
| 2313   | Layout 1 | `daaca0977a82`  |
| 2308   | Layout 1 | `daaca0977a82`  |
| 2302   | Layout 1 | `daaca0977a82`  |
| 2295   | Layout 1 | `daaca0977a82`  |
| 2290   | Layout 1 | `daaca0977a82`  |
| 2284   | Layout 1 | `daaca0977a82`  |
| 2276   | Layout 1 | `daaca0977a82`  |
| 2269   | Layout 1 | `daaca0977a82`  |
| 2259   | Layout 1 | `daaca0977a82`  |
| 2250   | Layout 1 | `daaca0977a82`  |
| 2243   | Layout 1 | `daaca0977a82`  |
| 2235   | Layout 1 | `daaca0977a82`  |
| 2229   | Layout 1 | `daaca0977a82`  |
| 2224   | Layout 1 | `daaca0977a82`  |
| 2218   | Layout 1 | `daaca0977a82`  |
| 2215   | Layout 1 | `daaca0977a82`  |
| 2207   | Layout 1 | `daaca0977a82`  |
| 2203   | Layout 1 | `daaca0977a82`  |
| 2196   | Layout 1 | `daaca0977a82`  |
| 2192   | Layout 1 | `daaca0977a82`  |
| 2189   | Layout 1 | `daaca0977a82`  |
| 2183   | Layout 1 | `daaca0977a82`  |
| 2179   | Layout 1 | `daaca0977a82`  |
| 2171   | Layout 1 | `daaca0977a82`  |
| 2163   | Layout 1 | `daaca0977a82`  |
| 2156   | Layout 1 | `daaca0977a82`  |
| 2151   | Layout 1 | `daaca0977a82`  |
| 2147   | Layout 1 | `daaca0977a82`  |
| 2142   | Layout 1 | `daaca0977a82`  |
| 2138   | Layout 1 | `daaca0977a82`  |
| 2134   | Layout 1 | `daaca0977a82`  |
| 2130   | Layout 1 | `daaca0977a82`  |
| 2122   | Layout 1 | `daaca0977a82`  |
| 2107   | Layout 1 | `daaca0977a82`  |
| 2098   | Layout 1 | `daaca0977a82`  |
| 2089   | Layout 1 | `daaca0977a82`  |
| 2081   | Layout 1 | `daaca0977a82`  |
| 2073   | Layout 1 | `daaca0977a82`  |
| 2067   | Layout 1 | `daaca0977a82`  |
| 2063   | Layout 1 | `daaca0977a82`  |
| 2059   | Layout 1 | `daaca0977a82`  |
| 2052   | Layout 1 | `daaca0977a82`  |
| 2044   | Layout 1 | `daaca0977a82`  |
| 2039   | Layout 1 | `daaca0977a82`  |
| 2032   | Layout 1 | `daaca0977a82`  |
| 2025   | Layout 1 | `daaca0977a82`  |
| 2011   | Layout 1 | `daaca0977a82`  |
| 2005   | Layout 1 | `daaca0977a82`  |
| 2000   | Layout 1 | `daaca0977a82`  |
| 1996   | Layout 1 | `daaca0977a82`  |
| 1991   | Layout 1 | `daaca0977a82`  |
| 1985   | Layout 1 | `daaca0977a82`  |
| 1980   | Layout 1 | `daaca0977a82`  |
| 1969   | Layout 1 | `daaca0977a82`  |
| 1964   | Layout 1 | `daaca0977a82`  |
| 1958   | Layout 1 | `daaca0977a82`  |
| 1950   | Layout 1 | `daaca0977a82`  |
| 1945   | Layout 1 | `daaca0977a82`  |
| 1937   | Layout 1 | `daaca0977a82`  |
| 1933   | Layout 1 | `daaca0977a82`  |
| 1927   | Layout 1 | `daaca0977a82`  |
| 1921   | Layout 1 | `daaca0977a82`  |
| 1914   | Layout 1 | `daaca0977a82`  |
| 1908   | Layout 1 | `daaca0977a82`  |
| 1897   | Layout 1 | `daaca0977a82`  |
| 1892   | Layout 1 | `daaca0977a82`  |
| 1886   | Layout 1 | `daaca0977a82`  |
| 1881   | Layout 1 | `daaca0977a82`  |
| 1871   | Layout 1 | `daaca0977a82`  |
| 1866   | Layout 1 | `daaca0977a82`  |
| 1862   | Layout 1 | `daaca0977a82`  |
| 1854   | Layout 1 | `daaca0977a82`  |
| 1846   | Layout 1 | `daaca0977a82`  |
| 1838   | Layout 1 | `daaca0977a82`  |
| 1832   | Layout 1 | `daaca0977a82`  |
| 1826   | Layout 1 | `daaca0977a82`  |
| 1822   | Layout 1 | `daaca0977a82`  |
| 1818   | Layout 1 | `daaca0977a82`  |
| 1804   | Layout 1 | `daaca0977a82`  |
| 1794   | Layout 1 | `daaca0977a82`  |
| 1790   | Layout 1 | `daaca0977a82`  |
| 1784   | Layout 1 | `daaca0977a82`  |
| 1774   | Layout 1 | `daaca0977a82`  |
| 1771   | Layout 1 | `daaca0977a82`  |
| 1762   | Layout 1 | `daaca0977a82`  |
| 1759   | Layout 1 | `daaca0977a82`  |
| 1754   | Layout 1 | `daaca0977a82`  |
| 1749   | Layout 1 | `daaca0977a82`  |
| 1743   | Layout 1 | `daaca0977a82`  |
| 1737   | Layout 1 | `daaca0977a82`  |
| 1731   | Layout 1 | `daaca0977a82`  |
| 1725   | Layout 1 | `daaca0977a82`  |
| 1717   | Layout 1 | `daaca0977a82`  |
| 1710   | Layout 1 | `daaca0977a82`  |
| 1704   | Layout 1 | `daaca0977a82`  |
| 1698   | Layout 1 | `daaca0977a82`  |
| 1690   | Layout 1 | `daaca0977a82`  |
| 1685   | Layout 1 | `daaca0977a82`  |
| 1680   | Layout 1 | `daaca0977a82`  |
| 1674   | Layout 1 | `daaca0977a82`  |
| 1668   | Layout 1 | `daaca0977a82`  |
| 1659   | Layout 1 | `daaca0977a82`  |
| 1649   | Layout 1 | `daaca0977a82`  |
| 1642   | Layout 1 | `daaca0977a82`  |
| 1636   | Layout 1 | `daaca0977a82`  |
| 1628   | Layout 1 | `daaca0977a82`  |
| 1622   | Layout 1 | `daaca0977a82`  |
| 1614   | Layout 1 | `daaca0977a82`  |
| 1608   | Layout 1 | `daaca0977a82`  |
| 1602   | Layout 1 | `daaca0977a82`  |
| 1598   | Layout 1 | `daaca0977a82`  |
| 1594   | Layout 1 | `daaca0977a82`  |
| 1590   | Layout 1 | `daaca0977a82`  |
| 1587   | Layout 1 | `daaca0977a82`  |
| 1584   | Layout 1 | `daaca0977a82`  |
| 1579   | Layout 1 | `daaca0977a82`  |
| 1572   | Layout 1 | `daaca0977a82`  |
| 1565   | Layout 1 | `daaca0977a82`  |
| 1559   | Layout 1 | `daaca0977a82`  |
| 1554   | Layout 1 | `daaca0977a82`  |
| 1547   | Layout 1 | `daaca0977a82`  |
| 1537   | Layout 1 | `daaca0977a82`  |
| 1529   | Layout 1 | `daaca0977a82`  |
| 1524   | Layout 1 | `daaca0977a82`  |
| 1519   | Layout 1 | `daaca0977a82`  |
| 1509   | Layout 1 | `daaca0977a82`  |
| 1506   | Layout 1 | `daaca0977a82`  |
| 1504   | Layout 1 | `daaca0977a82`  |
| 1500   | Layout 1 | `daaca0977a82`  |
| 1493   | Layout 1 | `daaca0977a82`  |
| 1489   | Layout 1 | `daaca0977a82`  |
| 1485   | Layout 1 | `daaca0977a82`  |
| 1481   | Layout 1 | `daaca0977a82`  |
| 1474   | Layout 1 | `daaca0977a82`  |
| 1466   | Layout 1 | `daaca0977a82`  |
| 1462   | Layout 1 | `daaca0977a82`  |
| 1459   | Layout 1 | `daaca0977a82`  |
| 1453   | Layout 1 | `daaca0977a82`  |
| 1450   | Layout 1 | `daaca0977a82`  |
| 1445   | Layout 1 | `daaca0977a82`  |
| 1439   | Layout 1 | `daaca0977a82`  |
| 1433   | Layout 1 | `daaca0977a82`  |
| 1430   | Layout 1 | `daaca0977a82`  |
| 1426   | Layout 1 | `daaca0977a82`  |
| 1421   | Layout 1 | `daaca0977a82`  |
| 1417   | Layout 1 | `daaca0977a82`  |
| 1416   | Layout 1 | `daaca0977a82`  |
| 1409   | Layout 1 | `daaca0977a82`  |
| 1405   | Layout 1 | `daaca0977a82`  |
| 1401   | Layout 1 | `daaca0977a82`  |
| 1396   | Layout 1 | `daaca0977a82`  |
| 1391   | Layout 1 | `daaca0977a82`  |
| 1390   | Layout 1 | `daaca0977a82`  |
| 1386   | Layout 1 | `daaca0977a82`  |
| 1381   | Layout 1 | `daaca0977a82`  |
| 1379   | Layout 1 | `daaca0977a82`  |
| 1372   | Layout 1 | `daaca0977a82`  |
| 1366   | Layout 1 | `daaca0977a82`  |
| 1364   | Layout 1 | `daaca0977a82`  |
| 1363   | Layout 1 | `daaca0977a82`  |
| 1360   | Layout 1 | `daaca0977a82`  |
| 1358   | Layout 1 | `daaca0977a82`  |
| 1355   | Layout 1 | `daaca0977a82`  |
| 1351   | Layout 1 | `daaca0977a82`  |
| 1348   | Layout 1 | `daaca0977a82`  |
| 1346   | Layout 1 | `daaca0977a82`  |
| 1341   | Layout 1 | `daaca0977a82`  |
| 1340   | Layout 1 | `daaca0977a82`  |
| 1338   | Layout 1 | `daaca0977a82`  |
| 1335   | Layout 1 | `daaca0977a82`  |
| 1333   | Layout 1 | `daaca0977a82`  |
| 1329   | Layout 1 | `daaca0977a82`  |
| 1327   | Layout 1 | `daaca0977a82`  |
| 1324   | Layout 1 | `daaca0977a82`  |
| 1321   | Layout 1 | `daaca0977a82`  |
| 1319   | Layout 1 | `daaca0977a82`  |
| 1318   | Layout 1 | `daaca0977a82`  |
| 1316   | Layout 1 | `daaca0977a82`  |
| 1313   | Layout 1 | `daaca0977a82`  |
| 1311   | Layout 1 | `daaca0977a82`  |
| 1309   | Layout 1 | `daaca0977a82`  |
| 1304   | Layout 1 | `daaca0977a82`  |
| 1292   | Layout 1 | `daaca0977a82`  |
| 1286   | Layout 1 | `daaca0977a82`  |
| 1280   | Layout 1 | `daaca0977a82`  |
| 1276   | Layout 1 | `daaca0977a82`  |
| 1267   | Layout 1 | `daaca0977a82`  |
| 1261   | Layout 1 | `daaca0977a82`  |
| 1256   | Layout 1 | `daaca0977a82`  |
| 1250   | Layout 1 | `daaca0977a82`  |
| 1246   | Layout 1 | `daaca0977a82`  |
| 1239   | Layout 1 | `daaca0977a82`  |
| 1230   | Layout 1 | `daaca0977a82`  |
| 1226   | Layout 1 | `daaca0977a82`  |
| 1220   | Layout 1 | `daaca0977a82`  |
| 1217   | Layout 1 | `daaca0977a82`  |
| 1211   | Layout 1 | `daaca0977a82`  |
| 1210   | Layout 1 | `daaca0977a82`  |
| 1208   | Layout 1 | `daaca0977a82`  |
| 1203   | Layout 1 | `daaca0977a82`  |
| 1197   | Layout 1 | `daaca0977a82`  |
| 1194   | Layout 1 | `daaca0977a82`  |
| 1192   | Layout 1 | `daaca0977a82`  |
| 1187   | Layout 1 | `daaca0977a82`  |
| 1183   | Layout 1 | `daaca0977a82`  |
| 1177   | Layout 1 | `daaca0977a82`  |
| 1173   | Layout 1 | `daaca0977a82`  |
| 1167   | Layout 1 | `daaca0977a82`  |
| 1164   | Layout 1 | `daaca0977a82`  |
| 1156   | Layout 1 | `daaca0977a82`  |
| 1149   | Layout 1 | `daaca0977a82`  |
| 1144   | Layout 1 | `daaca0977a82`  |
| 1137   | Layout 1 | `daaca0977a82`  |
| 1132   | Layout 1 | `daaca0977a82`  |
| 1127   | Layout 1 | `daaca0977a82`  |
| 1122   | Layout 1 | `daaca0977a82`  |
| 1118   | Layout 1 | `daaca0977a82`  |
| 1114   | Layout 1 | `daaca0977a82`  |
| 1109   | Layout 1 | `daaca0977a82`  |
| 1102   | Layout 1 | `daaca0977a82`  |
| 1096   | Layout 1 | `daaca0977a82`  |
| 1088   | Layout 1 | `daaca0977a82`  |
| 1081   | Layout 1 | `daaca0977a82`  |
| 1076   | Layout 1 | `daaca0977a82`  |
| 1069   | Layout 1 | `daaca0977a82`  |
| 1064   | Layout 1 | `daaca0977a82`  |
| 1058   | Layout 1 | `daaca0977a82`  |
| 1051   | Layout 1 | `daaca0977a82`  |
| 1044   | Layout 1 | `daaca0977a82`  |
| 1036   | Layout 1 | `daaca0977a82`  |
| 1026   | Layout 1 | `daaca0977a82`  |
| 1016   | Layout 1 | `daaca0977a82`  |
| 1009   | Layout 1 | `daaca0977a82`  |
| 1005   | Layout 1 | `daaca0977a82`  |
| 1000   | Layout 1 | `daaca0977a82`  |
| 998    | Layout 1 | `daaca0977a82`  |
| 990    | Layout 1 | `daaca0977a82`  |
| 979    | Layout 1 | `daaca0977a82`  |
| 972    | Layout 1 | `daaca0977a82`  |
| 963    | No file  | `daaca0977a82`  |
| 955    | No file  | `daaca0977a82`  |
| 946    | No file  | `daaca0977a82`  |
| 938    | No file  | `daaca0977a82`  |
| 927    | No file  | `daaca0977a82`  |
| 911    | No file  | `daaca0977a82`  |
| 904    | No file  | `daaca0977a82`  |
| 899    | No file  | `daaca0977a82`  |
| 894    | No file  | `daaca0977a82`  |
| 885    | No file  | `daaca0977a82`  |
| 879    | No file  | `daaca0977a82`  |
| 872    | No file  | `daaca0977a82`  |
| 864    | No file  | `daaca0977a82`  |
| 855    | No file  | `daaca0977a82`  |
| 853    | No file  | `daaca0977a82`  |
| 845    | No file  | `daaca0977a82`  |
| 837    | No file  | `daaca0977a82`  |
| 829    | No file  | `daaca0977a82`  |
| 822    | No file  | `daaca0977a82`  |
| 814    | No file  | `daaca0977a82`  |
| 805    | No file  | `daaca0977a82`  |
| 794    | No file  | `daaca0977a82`  |
| 787    | No file  | `daaca0977a82`  |
| 780    | No file  | `daaca0977a82`  |
| 771    | No file  | `daaca0977a82`  |
| 760    | No file  | `daaca0977a82`  |
| 748    | No file  | `daaca0977a82`  |
| 741    | No file  | `daaca0977a82`  |
| 736    | No file  | `daaca0977a82`  |
| 731    | No file  | `daaca0977a82`  |
| 723    | No file  | `daaca0977a82`  |
| 711    | No file  | `daaca0977a82`  |
| 707    | No file  | `daaca0977a82`  |
| 697    | No file  | `daaca0977a82`  |
| 689    | No file  | `daaca0977a82`  |
| 683    | No file  | `daaca0977a82`  |
| 678    | No file  | `daaca0977a82`  |
| 670    | No file  | `daaca0977a82`  |
| 661    | No file  | `daaca0977a82`  |
| 656    | No file  | `daaca0977a82`  |
| 652    | No file  | `daaca0977a82`  |
| 643    | No file  | `daaca0977a82`  |
| 637    | No file  | `daaca0977a82`  |
| 630    | No file  | `daaca0977a82`  |
| 627    | No file  | `daaca0977a82`  |
| 621    | No file  | `daaca0977a82`  |
| 617    | No file  | `daaca0977a82`  |
| 615    | No file  | `daaca0977a82`  |
| 606    | No file  | `daaca0977a82`  |
| 599    | No file  | `daaca0977a82`  |
| 592    | No file  | `daaca0977a82`  |
| 586    | No file  | `daaca0977a82`  |
| 577    | No file  | `daaca0977a82`  |
| 569    | No file  | `daaca0977a82`  |
| 561    | No file  | `daaca0977a82`  |
| 554    | No file  | `daaca0977a82`  |
| 542    | No file  | `daaca0977a82`  |
| 532    | No file  | `daaca0977a82`  |
| 531    | No file  | `daaca0977a82`  |
| 526    | No file  | `daaca0977a82`  |
| 521    | No file  | `daaca0977a82`  |
| 517    | No file  | `daaca0977a82`  |
| 510    | No file  | `daaca0977a82`  |
| 508    | No file  | `daaca0977a82`  |
| 504    | No file  | `daaca0977a82`  |
| 497    | No file  | `daaca0977a82`  |
| 491    | No file  | `daaca0977a82`  |
| 485    | No file  | `daaca0977a82`  |
| 478    | No file  | `daaca0977a82`  |
| 472    | No file  | `daaca0977a82`  |
| 466    | No file  | `daaca0977a82`  |
| 457    | No file  | `daaca0977a82`  |
| 452    | No file  | `daaca0977a82`  |
| 449    | No file  | `daaca0977a82`  |
| 435    | No file  | `daaca0977a82`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                              |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `stringtable.bss`     | Optional | Hashes of the GAME sheet keys the quest window names regions and types with (see [stringtable](stringtable_bss.md)) |
| `languagedata_en.loc` | Optional | The text of those keys, LOC type 37                                                               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with no count after the magic: the values start at `+0x04` and fill the space up to the string table.

| Offset              | Type               | Field        | Notes                                                          |
| ------------------- | ------------------ | ------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                                   |
| `+0x04`             | u32[..table_start] | quest_count  | One per enum value, in value order; see Quest Regions and Quest Types |
| `quest_count+0x00`  | String Table       | string_table | See String Table                                               |
| `EOF-0x08`          | u32                | table_start  | Offset of the string table, where `quest_count` ends           |
| `EOF-0x04`          | u32                | zero         | Always `0`                                                     |

The parser takes the value count from the trailer: `(table_start - 4) / 4`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No value reads a string                        |

## Quest Regions

`totalquestcountregion.bss` value N is `CppEnums.QuestRegionType` N (`global_define_cpp_enum.luac`). The file has one value per enum value up to `eQuestRegionType_Count`: 18 on client 3474, 13 on client 1784, whose enum ends at `eQuestRegionType_MountainOfEternalWinter`. The name is the GAME sheet key that `_regionString` in `panel_window_quest_all.luac` gives the value, read through `stringtable.bss` and LOC type 37. The names below are the client 3474 order; the handler applies them only to a file with all 18 values (see Notes).

| Value | Enum name                 | GAME sheet key                         | Name (English LOC)                |
| ----- | ------------------------- | -------------------------------------- | --------------------------------- |
| 0     | `None`                    | `LUA_QUESTLIST_HISTORY_TXT_REGION_99`  | Etc.                              |
| 1     | `Balenos`                 | `LUA_QUESTLIST_HISTORY_TXT_REGION_1`   | Eastern Balenos                   |
| 2     | `Serendia`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_2`   | Serendia                          |
| 3     | `NorthCalpheon`           | `LUA_QUESTLIST_HISTORY_TXT_REGION_3`   | Northern Calpheon                 |
| 4     | `CalpheonBigCity`         | `LUA_QUESTLIST_HISTORY_TXT_REGION_4`   | Calpheon City                     |
| 5     | `Keplan`                  | `LUA_QUESTLIST_HISTORY_TXT_REGION_5`   | Keplan (Southeastern Calpheon)    |
| 6     | `SouthWestCalpheon`       | `LUA_QUESTLIST_HISTORY_TXT_REGION_6`   | Southwestern Calpheon             |
| 7     | `Media`                   | `LUA_QUESTLIST_HISTORY_TXT_REGION_7`   | Mediah                            |
| 8     | `Valencia`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_8`   | Valencia                          |
| 9     | `Kamasylvia`              | `LUA_QUESTLIST_HISTORY_TXT_REGION_9`   | Kamasylvia                        |
| 10    | `Drigan`                  | `LUA_QUESTLIST_HISTORY_TXT_REGION_10`  | Drieghan                          |
| 11    | `Odilita`                 | `LUA_QUESTLIST_HISTORY_TXT_REGION_11`  | O'dyllita                         |
| 12    | `MountainOfEternalWinter` | `LUA_QUESTLIST_HISTORY_TXT_REGION_12`  | Mountain of Eternal Winter        |
| 13    | `AbyssOne`                | `LUA_ABYSSONE_MSG_SERVERSELECT_TITLE`  | Abyss One                         |
| 14    | `MorningLand`             | `LUA_QUESTLIST_HISTORY_TXT_REGION_13`  | Land of the Morning Light - Nampo |
| 15    | `Ulukita`                 | `LUA_QUESTLIST_HISTORY_TXT_REGION_14`  | Ulukita                           |
| 16    | `Edania_1`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_17`  | Outer Edania                      |
| 17    | `Edania_2`                | `LUA_QUESTLIST_HISTORY_TXT_REGION_20`  | Inner Edania                      |

On client 1784 the 13 values add up to 12,361, the record count of that client's `quest.dbss`, and each equals the number of its records with that `quest_region` ([Layout 1](../dbss/quest_dbss.md#layout-1)). On client 3474 the 18 values add up to 18,980, 11 fewer than the 18,991 `quest.dbss` records (see Open Questions).

## Quest Types

`totalquestcounttype.bss` value N is `__eQuestType` N. The value order is the order in which `panel_window_quest_all.luac` lists the `__eQuestType_*` names, and the `_typeString` keys follow it: type N reads `LUA_QUESTLIST_HISTORY_TXT_TYPE_<N+1>`, except `DirectClear`, which reads `LUA_QUESTLIST_HISTORY_TXT_REGION_99`. On client 3474 the 20 values equal the per-category record counts of the `quest.dbss` [Quest Category](../dbss/quest_dbss.md#quest-category) table for every category `0` to `19` (`16` has no record and holds `0`) and add up to all 18,991 records, so `quest_category` is the quest type. The `Adventurer's Tome` type is category `11`, the journal pages, and `Region Bonus` is category `12`, the quests of `regionmonsterkillquestlist.bss`.

| Value | Enum name                | GAME sheet key                        | Name (English LOC) |
| ----- | ------------------------ | ------------------------------------- | ------------------ |
| 0     | `BlackSpirit`            | `LUA_QUESTLIST_HISTORY_TXT_TYPE_1`    | Black Spirit       |
| 1     | `Main`                   | `LUA_QUESTLIST_HISTORY_TXT_TYPE_2`    | Main               |
| 2     | `Sub`                    | `LUA_QUESTLIST_HISTORY_TXT_TYPE_3`    | General            |
| 3     | `Repeat`                 | `LUA_QUESTLIST_HISTORY_TXT_TYPE_4`    | Recurring          |
| 4     | `Adventure`              | `LUA_QUESTLIST_HISTORY_TXT_TYPE_5`    | Adventure          |
| 5     | `BaseLife`               | `LUA_QUESTLIST_HISTORY_TXT_TYPE_6`    | Life               |
| 6     | `OceanLife`              | `LUA_QUESTLIST_HISTORY_TXT_TYPE_7`    | Sailing            |
| 7     | `CraftLife`              | `LUA_QUESTLIST_HISTORY_TXT_TYPE_8`    | Production         |
| 8     | `Contents`               | `LUA_QUESTLIST_HISTORY_TXT_TYPE_9`    | Content            |
| 9     | `Event`                  | `LUA_QUESTLIST_HISTORY_TXT_TYPE_10`   | Event              |
| 10    | `Guild`                  | `LUA_QUESTLIST_HISTORY_TXT_TYPE_11`   | Guild              |
| 11    | `DirectAccept`           | `LUA_QUESTLIST_HISTORY_TXT_TYPE_12`   | Adventurer's Tome  |
| 12    | `Sudden`                 | `LUA_QUESTLIST_HISTORY_TXT_TYPE_13`   | Region Bonus       |
| 13    | `SeasonPass`             | `LUA_QUESTLIST_HISTORY_TXT_TYPE_14`   | Season Pass        |
| 14    | `GrowthPass`             | `LUA_QUESTLIST_HISTORY_TXT_TYPE_15`   | Progression Pass   |
| 15    | `DirectClear`            | `LUA_QUESTLIST_HISTORY_TXT_REGION_99` | Etc.               |
| 16    | `Journal`                | `LUA_QUESTLIST_HISTORY_TXT_TYPE_17`   | Journal            |
| 17    | `OlviaAcademyPass`       | none                                  | none               |
| 18    | `OlviaAcademyReward`     | none                                  | none               |
| 19    | `OlviaAcademyCurriculum` | none                                  | none               |

`_typeString` has no key for the three Olvia Academy types; the handler shows their enum names. `LUA_QUESTLIST_HISTORY_TXT_TYPE_16` reads "Instant Clear", but the quest window names `DirectClear` "Etc.".

The client 1784 file holds 17 values that add up to 12,361, the record count of that client's `quest.dbss`, and each equals the number of its records with that `quest_category` ([Layout 1](../dbss/quest_dbss.md#layout-1)). That client's Lua has another enum, `CppEnums.QuestType` (`BlackSpirit` `0` to `Guild` `7`, `Special` `10`, `RegionMonsterKill` `11`, `Production` `15`, `_Count` `16`), which is one value short of the file; the 1784 values are not named here (see Open Questions).

## Notes

- Decompressed sizes: `totalquestcountregion.bss` 88 bytes on client 3474 (`4 + 18 × 4 + 12`) and 68 bytes on client 1784; `totalquestcounttype.bss` 96 bytes on client 3474 (`4 + 20 × 4 + 12`) and 84 bytes on client 1784.
- The quest window (`panel_window_quest_all_2.luac`) shows a completion percentage per region or per type group in its progress tab: `ToClient_GetClearedQuestCountByQuestRegion(region) / ToClient_GetTotalQuestCountByQuestRegion(region) * 100`, and the same pair `ByQuestType` when the list is sorted by type. The totals these getters return have the shape of the two files.
- No sheet of a private server's `DataSheets.bexcel` on client 1784 has `TotalQuest` in its name or a column, while that server's `binary/` folder holds both files.
- The handler (`_bss/totalquestcount/`) gives each value its enum value as key (`quest_region` or `quest_type`), the quest window name next to it, and `quest_count`. It names the values only when the file holds at least as many values as the client 3474 enum (18 regions, 20 types); a shorter file, such as both client 1784 files, gets an empty name column, since its enum order is not checked against the client 3474 one. A value past the end of the enum, on a later client, also has no name.

## Open Questions

### Eleven Quests Without a Region Count

On client 3474 the region values add up to 18,980 and the type values to 18,991, the `quest.dbss` record count; on client 1784 both files add up to all 12,361 records. The 11 missing quests may carry a region value outside `QuestRegionType` (the enum has no value past `Edania_2` and `_Count` `18`), but the Layout 2 `quest.dbss` has no decoded region field to check which quests they are; Layout 1 of client 1784 has one, `quest_region`.

### What Fills the Getters

`ToClient_GetTotalQuestCountByQuestRegion` and `ToClient_GetTotalQuestCountByQuestType` take a region or type value and return a total, which is what these files store per value, but nothing in the client Lua names the files. The client could also count the totals from `quest.dbss` itself, which on client 3474 gives the same type totals.

### Client 1784 Quest Types

The client 1784 type file has 17 values, while that client's `global_define_cpp_enum.luac` defines `CppEnums.QuestType` as `BlackSpirit` `0`, `Story` `1`, `Town` `2`, `Adventure` `3`, `Trade` `4`, `Craft` `5`, `Repetition` `6`, `Guild` `7`, `Special` `10`, `RegionMonsterKill` `11`, `Production` `15` and `_Count` `16`. Only 2,765 of the 10,815 quests both clients have keep their `quest_category`, so the 3474 names do not carry over. The 1784 `quest.dbss` agrees with the 1784 names, and it fills two values the enum does not name:

| Value | `CppEnums.QuestType` | Quests (client 1784) | Same quests as |
| ----: | -------------------- | -------------------: | -------------- |
| `6`   | `Repetition`         | 1,879 | 1,743 of them have an `unknown_list_04` repeat time; no other type has more than 114 |
| `10`  | `Special`            | 261   | The 261 quests of `specialquestlist.bss` |
| `11`  | `RegionMonsterKill`  | 114   | The 114 quests of `regionmonsterkillquestlist.bss` |
| `13`  | none                 | 100   | The 100 quests of `seasonpassquestlist.bss` |
| `16`  | none (`_Count`)      | 211   | The 211 quests of `growthpassquestlist.bss` |

The `quest.dbss` handler names client 1784 quest types by this enum and the GAME sheet keys of that client's `_typeString` (`TYPE_1` to `TYPE_8` for `0` to `7`, `TYPE_10` and `TYPE_11` for `10` and `11`), and leaves `13` and `16` unnamed. The handler of this file still shows no names for the client 1784 files: its value count cannot tell the enums apart, since the type files of clients 2519, 2765, 2923 and 3002 also hold 17 values while their Lua has no `CppEnums.QuestType`, and clients 1286 and 1598 hold 13 and 15 with the same enum up to `RegionMonsterKill` `11`.
