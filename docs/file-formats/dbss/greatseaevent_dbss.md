# `greatseaevent.dbss` Format

## Purpose

The result lines of the Great Ocean sea events
(`panel_widget_greatseaevent`): per event group the events a ship's crew
can meet, each with a Korean result text ("선원이 낡은 상자를
건져올렸습니다!", "a sailor fished up an old box!") and an icon path. When
the server sends `FromClient_GreatSeaEvent(type, ..., groupKey,
selectIndex, regionKey, groupEventType)`, the window shows
`ToClient_getGreatSeaEventResultString(groupKey, selectIndex)` and
`ToClient_getGreatSeaEventImagePath(groupKey, selectIndex)` above the
food, loyalty, HP, item or quest result. On client 3474 the file holds 5
groups and 101 events. Companion `greatseaeventoffset.dbss` lists where
every event sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes  | Records                        | Row bytes                  |
| ------ | -------------- | -------------------------- | ------ | ------------------------------ | -------------------------- |
| 1      | 1346 and later | `greatseaevent.dbss`       | 15,299 | 101 Event, 5 Group             | 139 to 181, 151 on average |
| 1      | 1346 and later | `greatseaeventoffset.dbss` | 1,246  | 101 Offset Row, 5 Offset Group | 12                         |

| Layout | File                       | Known            | Unknown      |
| ------ | -------------------------- | ---------------- | ------------ |
| 1      | `greatseaevent.dbss`       | 14,895 B (97.4%) | 404 B (2.6%) |
| 1      | `greatseaeventoffset.dbss` | 1,246 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `94288eef0861`  |
| 3482   | Layout 1             | `94288eef0861`  |
| 3474   | Layout 1             | `94288eef0861`  |
| 3473   | Layout 1             | `94288eef0861`  |
| 3464   | Layout 1             | `94288eef0861`  |
| 3458   | Layout 1             | `94288eef0861`  |
| 3454   | Layout 1             | `94288eef0861`  |
| 3444   | Layout 1             | `94288eef0861`  |
| 3435   | Layout 1             | `94288eef0861`  |
| 3426   | Layout 1             | `94288eef0861`  |
| 3418   | Layout 1             | `94288eef0861`  |
| 3412   | Layout 1             | `94288eef0861`  |
| 3402   | Layout 1             | `94288eef0861`  |
| 3396   | Layout 1             | `94288eef0861`  |
| 3387   | Layout 1             | `94288eef0861`  |
| 3381   | Layout 1             | `94288eef0861`  |
| 3373   | Layout 1             | `94288eef0861`  |
| 3364   | Layout 1             | `94288eef0861`  |
| 3356   | Layout 1             | `94288eef0861`  |
| 3349   | Layout 1             | `94288eef0861`  |
| 3342   | Layout 1             | `94288eef0861`  |
| 3335   | Layout 1             | `94288eef0861`  |
| 3326   | Layout 1             | `94288eef0861`  |
| 3321   | Layout 1             | `94288eef0861`  |
| 3314   | Layout 1             | `94288eef0861`  |
| 3303   | Layout 1             | `94288eef0861`  |
| 3302   | Layout 1             | `94288eef0861`  |
| 3293   | Layout 1             | `94288eef0861`  |
| 3283   | Layout 1             | `94288eef0861`  |
| 3275   | Layout 1             | `94288eef0861`  |
| 3267   | Layout 1             | `94288eef0861`  |
| 3258   | Layout 1             | `94288eef0861`  |
| 3251   | Layout 1             | `94288eef0861`  |
| 3242   | Layout 1             | `94288eef0861`  |
| 3235   | Layout 1             | `94288eef0861`  |
| 3229   | Layout 1             | `94288eef0861`  |
| 3212   | Layout 1             | `94288eef0861`  |
| 3203   | Layout 1             | `94288eef0861`  |
| 3193   | Layout 1             | `94288eef0861`  |
| 3186   | Layout 1             | `94288eef0861`  |
| 3177   | Layout 1             | `94288eef0861`  |
| 3169   | Layout 1             | `94288eef0861`  |
| 3158   | Layout 1             | `94288eef0861`  |
| 3151   | Layout 1             | `94288eef0861`  |
| 3144   | Layout 1             | `94288eef0861`  |
| 3133   | Layout 1             | `94288eef0861`  |
| 3125   | Layout 1             | `94288eef0861`  |
| 3118   | Layout 1             | `94288eef0861`  |
| 3111   | Layout 1             | `94288eef0861`  |
| 3103   | Layout 1             | `94288eef0861`  |
| 3095   | Layout 1             | `94288eef0861`  |
| 3086   | Layout 1             | `94288eef0861`  |
| 3072   | Layout 1             | `94288eef0861`  |
| 3062   | Layout 1             | `94288eef0861`  |
| 3052   | Layout 1             | `94288eef0861`  |
| 3045   | Layout 1             | `94288eef0861`  |
| 3037   | Layout 1             | `94288eef0861`  |
| 3030   | Layout 1             | `94288eef0861`  |
| 3021   | Layout 1             | `94288eef0861`  |
| 3012   | Layout 1             | `94288eef0861`  |
| 3002   | Layout 1             | `94288eef0861`  |
| 2995   | Layout 1             | `94288eef0861`  |
| 2987   | Layout 1             | `94288eef0861`  |
| 2978   | Layout 1             | `94288eef0861`  |
| 2970   | Layout 1             | `94288eef0861`  |
| 2959   | Layout 1             | `94288eef0861`  |
| 2951   | Layout 1             | `94288eef0861`  |
| 2942   | Layout 1             | `94288eef0861`  |
| 2935   | Layout 1             | `94288eef0861`  |
| 2932   | Layout 1             | `94288eef0861`  |
| 2923   | Layout 1             | `94288eef0861`  |
| 2919   | Layout 1             | `94288eef0861`  |
| 2907   | Layout 1             | `94288eef0861`  |
| 2900   | Layout 1             | `94288eef0861`  |
| 2891   | Layout 1             | `94288eef0861`  |
| 2882   | Layout 1             | `94288eef0861`  |
| 2872   | Layout 1             | `94288eef0861`  |
| 2863   | Layout 1             | `94288eef0861`  |
| 2855   | Layout 1             | `94288eef0861`  |
| 2849   | Layout 1             | `94288eef0861`  |
| 2844   | Layout 1             | `94288eef0861`  |
| 2834   | Layout 1             | `94288eef0861`  |
| 2825   | Layout 1             | `94288eef0861`  |
| 2819   | Layout 1             | `94288eef0861`  |
| 2811   | Layout 1             | `94288eef0861`  |
| 2803   | Layout 1             | `94288eef0861`  |
| 2794   | Layout 1             | `94288eef0861`  |
| 2783   | Layout 1             | `94288eef0861`  |
| 2774   | Layout 1             | `94288eef0861`  |
| 2765   | Layout 1             | `94288eef0861`  |
| 2756   | Layout 1             | `94288eef0861`  |
| 2750   | Layout 1             | `94288eef0861`  |
| 2743   | Layout 1             | `94288eef0861`  |
| 2736   | Layout 1             | `94288eef0861`  |
| 2726   | Layout 1             | `94288eef0861`  |
| 2717   | Layout 1             | `94288eef0861`  |
| 2709   | Layout 1             | `94288eef0861`  |
| 2703   | Layout 1             | `94288eef0861`  |
| 2695   | Layout 1             | `94288eef0861`  |
| 2684   | Layout 1             | `94288eef0861`  |
| 2672   | Layout 1             | `94288eef0861`  |
| 2665   | Layout 1             | `94288eef0861`  |
| 2657   | Layout 1             | `94288eef0861`  |
| 2649   | Layout 1             | `94288eef0861`  |
| 2644   | Layout 1             | `94288eef0861`  |
| 2637   | Layout 1             | `94288eef0861`  |
| 2629   | Layout 1             | `94288eef0861`  |
| 2619   | Layout 1             | `94288eef0861`  |
| 2612   | Layout 1             | `94288eef0861`  |
| 2606   | Layout 1             | `94288eef0861`  |
| 2602   | Layout 1             | `94288eef0861`  |
| 2601   | Layout 1             | `94288eef0861`  |
| 2592   | Layout 1             | `94288eef0861`  |
| 2583   | Layout 1             | `94288eef0861`  |
| 2575   | Layout 1             | `94288eef0861`  |
| 2567   | Layout 1             | `94288eef0861`  |
| 2560   | Layout 1             | `94288eef0861`  |
| 2553   | Layout 1             | `94288eef0861`  |
| 2545   | Layout 1             | `94288eef0861`  |
| 2538   | Layout 1             | `94288eef0861`  |
| 2529   | Layout 1             | `94288eef0861`  |
| 2519   | Layout 1             | `94288eef0861`  |
| 2513   | Layout 1             | `94288eef0861`  |
| 2510   | Layout 1             | `94288eef0861`  |
| 2507   | Layout 1             | `94288eef0861`  |
| 2503   | Layout 1             | `94288eef0861`  |
| 2498   | Layout 1             | `94288eef0861`  |
| 2492   | Layout 1             | `94288eef0861`  |
| 2487   | Layout 1             | `94288eef0861`  |
| 2480   | Layout 1             | `94288eef0861`  |
| 2474   | Layout 1             | `94288eef0861`  |
| 2468   | Layout 1             | `94288eef0861`  |
| 2460   | Layout 1             | `94288eef0861`  |
| 2453   | Layout 1             | `94288eef0861`  |
| 2444   | Layout 1             | `94288eef0861`  |
| 2438   | Layout 1             | `94288eef0861`  |
| 2434   | Layout 1             | `94288eef0861`  |
| 2429   | Layout 1             | `94288eef0861`  |
| 2421   | Layout 1             | `94288eef0861`  |
| 2414   | Layout 1             | `94288eef0861`  |
| 2407   | Layout 1             | `94288eef0861`  |
| 2401   | Layout 1             | `94288eef0861`  |
| 2397   | Layout 1             | `94288eef0861`  |
| 2393   | Layout 1             | `94288eef0861`  |
| 2384   | Layout 1             | `94288eef0861`  |
| 2378   | Layout 1             | `94288eef0861`  |
| 2372   | Layout 1             | `94288eef0861`  |
| 2358   | Layout 1             | `94288eef0861`  |
| 2352   | Layout 1             | `94288eef0861`  |
| 2347   | Layout 1             | `94288eef0861`  |
| 2343   | Layout 1             | `94288eef0861`  |
| 2335   | Layout 1             | `94288eef0861`  |
| 2327   | Layout 1             | `94288eef0861`  |
| 2324   | Layout 1             | `94288eef0861`  |
| 2319   | Layout 1             | `94288eef0861`  |
| 2313   | Layout 1             | `94288eef0861`  |
| 2308   | Layout 1             | `94288eef0861`  |
| 2302   | Layout 1             | `94288eef0861`  |
| 2295   | Layout 1             | `94288eef0861`  |
| 2290   | Layout 1             | `94288eef0861`  |
| 2284   | Layout 1             | `94288eef0861`  |
| 2276   | Layout 1             | `94288eef0861`  |
| 2269   | Layout 1             | `94288eef0861`  |
| 2259   | Layout 1             | `94288eef0861`  |
| 2250   | Layout 1             | `94288eef0861`  |
| 2243   | Layout 1             | `94288eef0861`  |
| 2235   | Layout 1             | `94288eef0861`  |
| 2229   | Layout 1             | `94288eef0861`  |
| 2224   | Layout 1             | `94288eef0861`  |
| 2218   | Layout 1             | `94288eef0861`  |
| 2215   | Layout 1             | `94288eef0861`  |
| 2207   | Layout 1             | `94288eef0861`  |
| 2203   | Layout 1             | `94288eef0861`  |
| 2196   | Layout 1             | `94288eef0861`  |
| 2192   | Layout 1             | `94288eef0861`  |
| 2189   | Layout 1             | `94288eef0861`  |
| 2183   | Layout 1             | `94288eef0861`  |
| 2179   | Layout 1             | `94288eef0861`  |
| 2171   | Layout 1             | `94288eef0861`  |
| 2163   | Layout 1             | `94288eef0861`  |
| 2156   | Layout 1             | `94288eef0861`  |
| 2151   | Layout 1             | `94288eef0861`  |
| 2147   | Layout 1             | `94288eef0861`  |
| 2142   | Layout 1             | `94288eef0861`  |
| 2138   | Layout 1             | `94288eef0861`  |
| 2134   | Layout 1             | `94288eef0861`  |
| 2130   | Layout 1             | `94288eef0861`  |
| 2122   | Layout 1             | `94288eef0861`  |
| 2107   | Layout 1             | `94288eef0861`  |
| 2098   | Layout 1             | `94288eef0861`  |
| 2089   | Layout 1             | `94288eef0861`  |
| 2081   | Layout 1             | `94288eef0861`  |
| 2073   | Layout 1             | `94288eef0861`  |
| 2067   | Layout 1             | `94288eef0861`  |
| 2063   | Layout 1             | `94288eef0861`  |
| 2059   | Layout 1             | `94288eef0861`  |
| 2052   | Layout 1             | `94288eef0861`  |
| 2044   | Layout 1             | `94288eef0861`  |
| 2039   | Layout 1             | `94288eef0861`  |
| 2032   | Layout 1             | `94288eef0861`  |
| 2025   | Layout 1             | `94288eef0861`  |
| 2011   | Layout 1             | `94288eef0861`  |
| 2005   | Layout 1             | `94288eef0861`  |
| 2000   | Layout 1             | `94288eef0861`  |
| 1996   | Layout 1             | `94288eef0861`  |
| 1991   | Layout 1             | `94288eef0861`  |
| 1985   | Layout 1             | `94288eef0861`  |
| 1980   | Layout 1             | `94288eef0861`  |
| 1969   | Layout 1             | `94288eef0861`  |
| 1964   | Layout 1             | `94288eef0861`  |
| 1958   | Layout 1             | `94288eef0861`  |
| 1950   | Layout 1             | `94288eef0861`  |
| 1945   | Layout 1             | `94288eef0861`  |
| 1937   | Layout 1             | `94288eef0861`  |
| 1933   | Layout 1             | `94288eef0861`  |
| 1927   | Layout 1             | `94288eef0861`  |
| 1921   | Layout 1             | `94288eef0861`  |
| 1914   | Layout 1             | `94288eef0861`  |
| 1908   | Layout 1             | `94288eef0861`  |
| 1897   | Layout 1             | `94288eef0861`  |
| 1892   | Layout 1             | `94288eef0861`  |
| 1886   | Layout 1             | `94288eef0861`  |
| 1881   | Layout 1             | `94288eef0861`  |
| 1871   | Layout 1             | `94288eef0861`  |
| 1866   | Layout 1             | `94288eef0861`  |
| 1862   | Layout 1             | `94288eef0861`  |
| 1854   | Layout 1             | `94288eef0861`  |
| 1846   | Layout 1             | `94288eef0861`  |
| 1838   | Layout 1             | `94288eef0861`  |
| 1832   | Layout 1             | `94288eef0861`  |
| 1826   | Layout 1             | `94288eef0861`  |
| 1822   | Layout 1             | `94288eef0861`  |
| 1818   | Layout 1             | `94288eef0861`  |
| 1804   | Layout 1             | `94288eef0861`  |
| 1794   | Layout 1             | `94288eef0861`  |
| 1790   | Layout 1             | `94288eef0861`  |
| 1784   | Layout 1             | `94288eef0861`  |
| 1774   | Layout 1             | `94288eef0861`  |
| 1771   | Layout 1             | `94288eef0861`  |
| 1762   | Layout 1             | `94288eef0861`  |
| 1759   | Layout 1             | `94288eef0861`  |
| 1754   | Layout 1             | `94288eef0861`  |
| 1749   | Layout 1             | `94288eef0861`  |
| 1743   | Layout 1             | `94288eef0861`  |
| 1737   | Layout 1             | `94288eef0861`  |
| 1731   | Layout 1             | `94288eef0861`  |
| 1725   | Layout 1             | `94288eef0861`  |
| 1717   | Layout 1             | `94288eef0861`  |
| 1710   | Layout 1             | `94288eef0861`  |
| 1704   | Layout 1             | `94288eef0861`  |
| 1698   | Layout 1             | `94288eef0861`  |
| 1690   | Layout 1             | `94288eef0861`  |
| 1685   | Layout 1             | `94288eef0861`  |
| 1680   | Layout 1             | `94288eef0861`  |
| 1674   | Layout 1             | `94288eef0861`  |
| 1668   | Layout 1             | `94288eef0861`  |
| 1659   | Layout 1             | `94288eef0861`  |
| 1649   | Layout 1             | `94288eef0861`  |
| 1642   | Layout 1             | `94288eef0861`  |
| 1636   | Layout 1             | `94288eef0861`  |
| 1628   | Layout 1             | `94288eef0861`  |
| 1622   | Layout 1             | `94288eef0861`  |
| 1614   | Layout 1             | `94288eef0861`  |
| 1608   | Layout 1             | `94288eef0861`  |
| 1602   | Layout 1             | `94288eef0861`  |
| 1598   | Layout 1             | `94288eef0861`  |
| 1594   | Layout 1             | `94288eef0861`  |
| 1590   | Layout 1             | `94288eef0861`  |
| 1587   | Layout 1             | `94288eef0861`  |
| 1584   | Layout 1             | `94288eef0861`  |
| 1579   | Layout 1             | `94288eef0861`  |
| 1572   | Layout 1             | `94288eef0861`  |
| 1565   | Layout 1             | `94288eef0861`  |
| 1559   | Layout 1             | `94288eef0861`  |
| 1554   | Layout 1             | `94288eef0861`  |
| 1547   | Layout 1             | `94288eef0861`  |
| 1537   | Layout 1             | `94288eef0861`  |
| 1529   | Layout 1             | `94288eef0861`  |
| 1524   | Layout 1             | `94288eef0861`  |
| 1519   | Layout 1             | `94288eef0861`  |
| 1509   | Layout 1             | `94288eef0861`  |
| 1506   | Layout 1             | `94288eef0861`  |
| 1504   | Layout 1             | `94288eef0861`  |
| 1500   | Layout 1             | `94288eef0861`  |
| 1493   | Layout 1             | `94288eef0861`  |
| 1489   | Layout 1             | `94288eef0861`  |
| 1485   | Layout 1             | `94288eef0861`  |
| 1481   | Layout 1             | `94288eef0861`  |
| 1474   | Layout 1             | `94288eef0861`  |
| 1466   | Layout 1             | `94288eef0861`  |
| 1462   | Layout 1             | `94288eef0861`  |
| 1459   | Layout 1             | `94288eef0861`  |
| 1453   | Layout 1             | `94288eef0861`  |
| 1450   | Layout 1             | `94288eef0861`  |
| 1445   | Layout 1             | `94288eef0861`  |
| 1439   | Layout 1             | `94288eef0861`  |
| 1433   | Layout 1             | `94288eef0861`  |
| 1430   | Layout 1             | `94288eef0861`  |
| 1426   | Layout 1             | `94288eef0861`  |
| 1421   | Layout 1             | `94288eef0861`  |
| 1417   | Layout 1             | `94288eef0861`  |
| 1416   | Layout 1             | `94288eef0861`  |
| 1409   | Layout 1             | `94288eef0861`  |
| 1405   | Layout 1             | `94288eef0861`  |
| 1401   | Layout 1             | `94288eef0861`  |
| 1396   | Layout 1             | `94288eef0861`  |
| 1391   | Layout 1             | `94288eef0861`  |
| 1390   | Layout 1             | `94288eef0861`  |
| 1386   | Layout 1             | `94288eef0861`  |
| 1381   | Layout 1             | `94288eef0861`  |
| 1379   | Layout 1             | `94288eef0861`  |
| 1372   | Layout 1             | `94288eef0861`  |
| 1366   | Layout 1             | `94288eef0861`  |
| 1364   | Layout 1             | `94288eef0861`  |
| 1363   | Layout 1             | `94288eef0861`  |
| 1360   | Layout 1             | `94288eef0861`  |
| 1358   | Layout 1             | `94288eef0861`  |
| 1355   | Layout 1             | `94288eef0861`  |
| 1351   | Layout 1             | `94288eef0861`  |
| 1348   | Layout 1             | `94288eef0861`  |
| 1346   | Layout 1             | `94288eef0861`  |
| 1341   | No documented layout | `94288eef0861`  |
| 1340   | No documented layout | `94288eef0861`  |
| 1338   | No documented layout | `94288eef0861`  |
| 1335   | No documented layout | `94288eef0861`  |
| 1333   | No documented layout | `94288eef0861`  |
| 1329   | No documented layout | `94288eef0861`  |
| 1327   | No documented layout | `94288eef0861`  |
| 1324   | No documented layout | `94288eef0861`  |
| 1321   | No documented layout | `94288eef0861`  |
| 1319   | No documented layout | `94288eef0861`  |
| 1318   | No documented layout | `94288eef0861`  |
| 1316   | No documented layout | `94288eef0861`  |
| 1313   | No documented layout | `94288eef0861`  |
| 1311   | No documented layout | `94288eef0861`  |
| 1309   | No documented layout | `94288eef0861`  |
| 1304   | No documented layout | `94288eef0861`  |
| 1292   | No documented layout | `94288eef0861`  |
| 1286   | No documented layout | `94288eef0861`  |
| 1280   | No file              | `94288eef0861`  |
| 1276   | No file              | `94288eef0861`  |
| 1267   | No file              | `94288eef0861`  |
| 1261   | No file              | `94288eef0861`  |
| 1256   | No file              | `94288eef0861`  |
| 1250   | No file              | `94288eef0861`  |
| 1246   | No file              | `94288eef0861`  |
| 1239   | No file              | `94288eef0861`  |
| 1230   | No file              | `94288eef0861`  |
| 1226   | No file              | `94288eef0861`  |
| 1220   | No file              | `94288eef0861`  |
| 1217   | No file              | `94288eef0861`  |
| 1211   | No file              | `94288eef0861`  |
| 1210   | No file              | `94288eef0861`  |
| 1208   | No file              | `94288eef0861`  |
| 1203   | No file              | `94288eef0861`  |
| 1197   | No file              | `94288eef0861`  |
| 1194   | No file              | `94288eef0861`  |
| 1192   | No file              | `94288eef0861`  |
| 1187   | No file              | `94288eef0861`  |
| 1183   | No file              | `94288eef0861`  |
| 1177   | No file              | `94288eef0861`  |
| 1173   | No file              | `94288eef0861`  |
| 1167   | No file              | `94288eef0861`  |
| 1164   | No file              | `94288eef0861`  |
| 1156   | No file              | `94288eef0861`  |
| 1149   | No file              | `94288eef0861`  |
| 1144   | No file              | `94288eef0861`  |
| 1137   | No file              | `94288eef0861`  |
| 1132   | No file              | `94288eef0861`  |
| 1127   | No file              | `94288eef0861`  |
| 1122   | No file              | `94288eef0861`  |
| 1118   | No file              | `94288eef0861`  |
| 1114   | No file              | `94288eef0861`  |
| 1109   | No file              | `94288eef0861`  |
| 1102   | No file              | `94288eef0861`  |
| 1096   | No file              | `94288eef0861`  |
| 1088   | No file              | `94288eef0861`  |
| 1081   | No file              | `94288eef0861`  |
| 1076   | No file              | `94288eef0861`  |
| 1069   | No file              | `94288eef0861`  |
| 1064   | No file              | `94288eef0861`  |
| 1058   | No file              | `94288eef0861`  |
| 1051   | No file              | `94288eef0861`  |
| 1044   | No file              | `94288eef0861`  |
| 1036   | No file              | `94288eef0861`  |
| 1026   | No file              | `94288eef0861`  |
| 1016   | No file              | `94288eef0861`  |
| 1009   | No file              | `94288eef0861`  |
| 1005   | No file              | `94288eef0861`  |
| 1000   | No file              | `94288eef0861`  |
| 998    | No file              | `94288eef0861`  |
| 990    | No file              | `94288eef0861`  |
| 979    | No file              | `94288eef0861`  |
| 972    | No file              | `94288eef0861`  |
| 963    | No file              | `94288eef0861`  |
| 955    | No file              | `94288eef0861`  |
| 946    | No file              | `94288eef0861`  |
| 938    | No file              | `94288eef0861`  |
| 927    | No file              | `94288eef0861`  |
| 911    | No file              | `94288eef0861`  |
| 904    | No file              | `94288eef0861`  |
| 899    | No file              | `94288eef0861`  |
| 894    | No file              | `94288eef0861`  |
| 885    | No file              | `94288eef0861`  |
| 879    | No file              | `94288eef0861`  |
| 872    | No file              | `94288eef0861`  |
| 864    | No file              | `94288eef0861`  |
| 855    | No file              | `94288eef0861`  |
| 853    | No file              | `94288eef0861`  |
| 845    | No file              | `94288eef0861`  |
| 837    | No file              | `94288eef0861`  |
| 829    | No file              | `94288eef0861`  |
| 822    | No file              | `94288eef0861`  |
| 814    | No file              | `94288eef0861`  |
| 805    | No file              | `94288eef0861`  |
| 794    | No file              | `94288eef0861`  |
| 787    | No file              | `94288eef0861`  |
| 780    | No file              | `94288eef0861`  |
| 771    | No file              | `94288eef0861`  |
| 760    | No file              | `94288eef0861`  |
| 748    | No file              | `94288eef0861`  |
| 741    | No file              | `94288eef0861`  |
| 736    | No file              | `94288eef0861`  |
| 731    | No file              | `94288eef0861`  |
| 723    | No file              | `94288eef0861`  |
| 711    | No file              | `94288eef0861`  |
| 707    | No file              | `94288eef0861`  |
| 697    | No file              | `94288eef0861`  |
| 689    | No file              | `94288eef0861`  |
| 683    | No file              | `94288eef0861`  |
| 678    | No file              | `94288eef0861`  |
| 670    | No file              | `94288eef0861`  |
| 661    | No file              | `94288eef0861`  |
| 656    | No file              | `94288eef0861`  |
| 652    | No file              | `94288eef0861`  |
| 643    | No file              | `94288eef0861`  |
| 637    | No file              | `94288eef0861`  |
| 630    | No file              | `94288eef0861`  |
| 627    | No file              | `94288eef0861`  |
| 621    | No file              | `94288eef0861`  |
| 617    | No file              | `94288eef0861`  |
| 615    | No file              | `94288eef0861`  |
| 606    | No file              | `94288eef0861`  |
| 599    | No file              | `94288eef0861`  |
| 592    | No file              | `94288eef0861`  |
| 586    | No file              | `94288eef0861`  |
| 577    | No file              | `94288eef0861`  |
| 569    | No file              | `94288eef0861`  |
| 561    | No file              | `94288eef0861`  |
| 554    | No file              | `94288eef0861`  |
| 542    | No file              | `94288eef0861`  |
| 532    | No file              | `94288eef0861`  |
| 531    | No file              | `94288eef0861`  |
| 526    | No file              | `94288eef0861`  |
| 521    | No file              | `94288eef0861`  |
| 517    | No file              | `94288eef0861`  |
| 510    | No file              | `94288eef0861`  |
| 508    | No file              | `94288eef0861`  |
| 504    | No file              | `94288eef0861`  |
| 497    | No file              | `94288eef0861`  |
| 491    | No file              | `94288eef0861`  |
| 485    | No file              | `94288eef0861`  |
| 478    | No file              | `94288eef0861`  |
| 472    | No file              | `94288eef0861`  |
| 466    | No file              | `94288eef0861`  |
| 457    | No file              | `94288eef0861`  |
| 452    | No file              | `94288eef0861`  |
| 449    | No file              | `94288eef0861`  |
| 435    | No file              | `94288eef0861`  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                                   |
| -------------------------- | -------- | ---------------------------------------------------------------------- |
| `greatseaeventoffset.dbss` | Optional | `(group_key, select_index) -> (data_offset, data_size)` of every event; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field       | Notes                                |
| ------- | ------------------ | ----------- | ------------------------------------ |
| `+0x00` | u32                | group_count | Number of groups                     |
| `+0x04` | Group[group_count] | groups      | See Group; in group key order        |

### Group (variable: 4 bytes + events)

| Offset  | Type                | Field       | Notes     |
| ------- | ------------------- | ----------- | --------- |
| `+0x00` | u32                 | event_count | Number of events |
| `+0x04` | Event[event_count]  | events      | See Event |

### Event (variable: 23 bytes + result text and image path)

| Offset              | Type  | Field                 | Notes                                                          |
| ------------------- | ----- | --------------------- | -------------------------------------------------------------- |
| `+0x00`             | u16   | group_key             | The group's key, the same on every event of a group; `1` to `5` on client 3474 |
| `+0x02`             | u8    | select_index          | `0` to `event_count - 1` within the group                      |
| `+0x03`             | str16 | result_string_kr      | Korean result text; no LOC row holds it                        |
| `result_string_kr+0x00` | str16 | image_path        | Icon path such as `Icon/New_Icon/11_Employee/Explore_0004.dds` |
| `image_path+0x00`   | u32   | unknown_image_path_00 | `0` on every event of clients 1784 and 3474                    |

### `greatseaeventoffset.dbss`

Bare offset table into `greatseaevent.dbss`, in the same groups.

| Offset  | Type                      | Field       | Notes                                      |
| ------- | ------------------------- | ----------- | ------------------------------------------ |
| `+0x00` | u32                       | group_count | Equals the `greatseaevent.dbss` group count |
| `+0x04` | Offset Group[group_count] | groups      | See Offset Group                           |

### Offset Group (variable: 6 bytes + rows)

| Offset  | Type              | Field     | Notes                                   |
| ------- | ----------------- | --------- | --------------------------------------- |
| `+0x00` | u16               | group_key | The group's key                         |
| `+0x02` | u32               | count     | Equals the group's `event_count`        |
| `+0x06` | Offset Row[count] | rows      | See Offset Row                          |

### Offset Row (12 bytes)

| Offset  | Type | Field        | Notes                                        |
| ------- | ---- | ------------ | -------------------------------------------- |
| `+0x00` | u32  | select_index | The event's `select_index`                   |
| `+0x04` | u32  | data_offset  | Event start, at its `group_key`              |
| `+0x08` | u32  | data_size    | The whole event                              |

On clients 1784 and 3474 the index lists the events in file order, and
every row points at the event with its group key and index.

## Groups

The events on client 3474, by group:

| Group | Events | Different texts | Result texts                                                       |
| ----- | ------ | --------------- | ------------------------------------------------------------------ |
| 1     | 27     | 18              | Crew finds, weather and sea events, scurvy, a Cox Pirates attack   |
| 2     | 7      | 6               | Food from islanders, fish, a feast with the Sea Otters             |
| 3     | 7      | 6               | The same six texts as group 2                                      |
| 4     | 30     | 10              | Treasure chests, a whale attack, guards and beasts, island children asking for help, shipwreck materials |
| 5     | 30     | 10              | The same ten texts as group 4                                      |

The 101 events use 34 different texts and 17 icons. Client 1784 has the
same groups with 33 events in groups 4 and 5.

## Field Names

`group_key` and `select_index` are the arguments of
`ToClient_getGreatSeaEventResultString(groupKey, selectIndex)` and
`ToClient_getGreatSeaEventImagePath(groupKey, selectIndex)`, which return
the two texts (`panel_widget_greatseaevent_2.luac`). The client 1784
server dump (`Instance_dumpFull.exe`) names the table
`GreatSeaEventStaticStatus` and logs `GreatSeaGroupKey(%#), Index(%#),
textNo(%#)` for a missing text, and "이미지 경로가 없습니다" ("no image path").

## Notes

- `FromClient_GreatSeaEvent` types are `__eGreatSeaEvent_Food`, `_Loyalty`,
  `_Hp`, `_Item` and `_Quest`; their amounts, items and quests come from the
  server, not from this file.
- Client 1784 has the same layout; its file is 16,221 bytes.

## Open Questions

### unknown_image_path_00

The u32 after the image path is `0` on all 101 events of client 3474 and
all 107 of client 1784. The server dump's checks name a sign ("부호는 0
혹은 1입니다", "the sign is 0 or 1"), a type and an item key for
`GreatSeaEventStaticStatus`; whether the u32 is one of them is open.
