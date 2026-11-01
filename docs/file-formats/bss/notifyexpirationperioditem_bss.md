# `notifyexpirationperioditem.bss` Format

## Purpose

The items whose expiry the client announces: one 8-byte row per item key
with its notice value. On client 3483 the 143 rows hold 24 `[Title]`
items (`757087` [Title] City Celebrity), 21 `[Event]` items, discount and
exchange coupons and items with a time in their name (`757013` Cliff's
Skill Add-on Guide (1 Day), Book of Combat (30 Days)), and every row
stores `1440`. The
notice window (`panel_window_expirationperioditem_2.luac`, client 3482)
lists the player's items from `ToClient_getExpirationPeriodItemCount()`
and `ToClient_getNotifyExpirationPeriodItemWrapper(index)`, with each
item's icon, name and `getLeftTime()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes | Records | Row bytes |
| ------ | -------------- | -------------------------------- | ----- | ------- | --------- |
| 1      | 1504 and later | `notifyexpirationperioditem.bss` | 1,164 | 143 Row | 8         |

| Layout | File                             | Known            | Unknown    |
| ------ | -------------------------------- | ---------------- | ---------- |
| 1      | `notifyexpirationperioditem.bss` | 1,164 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `69946c5724ef`  |
| 3482   | Layout 1 | `69946c5724ef`  |
| 3474   | Layout 1 | `69946c5724ef`  |
| 3473   | Layout 1 | `69946c5724ef`  |
| 3464   | Layout 1 | `69946c5724ef`  |
| 3458   | Layout 1 | `69946c5724ef`  |
| 3454   | Layout 1 | `69946c5724ef`  |
| 3444   | Layout 1 | `69946c5724ef`  |
| 3435   | Layout 1 | `69946c5724ef`  |
| 3426   | Layout 1 | `69946c5724ef`  |
| 3418   | Layout 1 | `69946c5724ef`  |
| 3412   | Layout 1 | `69946c5724ef`  |
| 3402   | Layout 1 | `69946c5724ef`  |
| 3396   | Layout 1 | `69946c5724ef`  |
| 3387   | Layout 1 | `69946c5724ef`  |
| 3381   | Layout 1 | `69946c5724ef`  |
| 3373   | Layout 1 | `69946c5724ef`  |
| 3364   | Layout 1 | `69946c5724ef`  |
| 3356   | Layout 1 | `69946c5724ef`  |
| 3349   | Layout 1 | `69946c5724ef`  |
| 3342   | Layout 1 | `69946c5724ef`  |
| 3335   | Layout 1 | `69946c5724ef`  |
| 3326   | Layout 1 | `69946c5724ef`  |
| 3321   | Layout 1 | `69946c5724ef`  |
| 3314   | Layout 1 | `69946c5724ef`  |
| 3303   | Layout 1 | `69946c5724ef`  |
| 3302   | Layout 1 | `69946c5724ef`  |
| 3293   | Layout 1 | `69946c5724ef`  |
| 3283   | Layout 1 | `69946c5724ef`  |
| 3275   | Layout 1 | `69946c5724ef`  |
| 3267   | Layout 1 | `69946c5724ef`  |
| 3258   | Layout 1 | `69946c5724ef`  |
| 3251   | Layout 1 | `69946c5724ef`  |
| 3242   | Layout 1 | `69946c5724ef`  |
| 3235   | Layout 1 | `69946c5724ef`  |
| 3229   | Layout 1 | `69946c5724ef`  |
| 3212   | Layout 1 | `69946c5724ef`  |
| 3203   | Layout 1 | `69946c5724ef`  |
| 3193   | Layout 1 | `69946c5724ef`  |
| 3186   | Layout 1 | `69946c5724ef`  |
| 3177   | Layout 1 | `69946c5724ef`  |
| 3169   | Layout 1 | `69946c5724ef`  |
| 3158   | Layout 1 | `69946c5724ef`  |
| 3151   | Layout 1 | `69946c5724ef`  |
| 3144   | Layout 1 | `69946c5724ef`  |
| 3133   | Layout 1 | `69946c5724ef`  |
| 3125   | Layout 1 | `69946c5724ef`  |
| 3118   | Layout 1 | `69946c5724ef`  |
| 3111   | Layout 1 | `69946c5724ef`  |
| 3103   | Layout 1 | `69946c5724ef`  |
| 3095   | Layout 1 | `69946c5724ef`  |
| 3086   | Layout 1 | `69946c5724ef`  |
| 3072   | Layout 1 | `69946c5724ef`  |
| 3062   | Layout 1 | `69946c5724ef`  |
| 3052   | Layout 1 | `69946c5724ef`  |
| 3045   | Layout 1 | `69946c5724ef`  |
| 3037   | Layout 1 | `69946c5724ef`  |
| 3030   | Layout 1 | `69946c5724ef`  |
| 3021   | Layout 1 | `69946c5724ef`  |
| 3012   | Layout 1 | `69946c5724ef`  |
| 3002   | Layout 1 | `69946c5724ef`  |
| 2995   | Layout 1 | `69946c5724ef`  |
| 2987   | Layout 1 | `69946c5724ef`  |
| 2978   | Layout 1 | `69946c5724ef`  |
| 2970   | Layout 1 | `69946c5724ef`  |
| 2959   | Layout 1 | `69946c5724ef`  |
| 2951   | Layout 1 | `69946c5724ef`  |
| 2942   | Layout 1 | `69946c5724ef`  |
| 2935   | Layout 1 | `69946c5724ef`  |
| 2932   | Layout 1 | `69946c5724ef`  |
| 2923   | Layout 1 | `69946c5724ef`  |
| 2919   | Layout 1 | `69946c5724ef`  |
| 2907   | Layout 1 | `69946c5724ef`  |
| 2900   | Layout 1 | `69946c5724ef`  |
| 2891   | Layout 1 | `69946c5724ef`  |
| 2882   | Layout 1 | `69946c5724ef`  |
| 2872   | Layout 1 | `69946c5724ef`  |
| 2863   | Layout 1 | `69946c5724ef`  |
| 2855   | Layout 1 | `69946c5724ef`  |
| 2849   | Layout 1 | `69946c5724ef`  |
| 2844   | Layout 1 | `69946c5724ef`  |
| 2834   | Layout 1 | `69946c5724ef`  |
| 2825   | Layout 1 | `69946c5724ef`  |
| 2819   | Layout 1 | `69946c5724ef`  |
| 2811   | Layout 1 | `69946c5724ef`  |
| 2803   | Layout 1 | `69946c5724ef`  |
| 2794   | Layout 1 | `69946c5724ef`  |
| 2783   | Layout 1 | `69946c5724ef`  |
| 2774   | Layout 1 | `69946c5724ef`  |
| 2765   | Layout 1 | `69946c5724ef`  |
| 2756   | Layout 1 | `69946c5724ef`  |
| 2750   | Layout 1 | `69946c5724ef`  |
| 2743   | Layout 1 | `69946c5724ef`  |
| 2736   | Layout 1 | `69946c5724ef`  |
| 2726   | Layout 1 | `69946c5724ef`  |
| 2717   | Layout 1 | `69946c5724ef`  |
| 2709   | Layout 1 | `69946c5724ef`  |
| 2703   | Layout 1 | `69946c5724ef`  |
| 2695   | Layout 1 | `69946c5724ef`  |
| 2684   | Layout 1 | `69946c5724ef`  |
| 2672   | Layout 1 | `69946c5724ef`  |
| 2665   | Layout 1 | `69946c5724ef`  |
| 2657   | Layout 1 | `69946c5724ef`  |
| 2649   | Layout 1 | `69946c5724ef`  |
| 2644   | Layout 1 | `69946c5724ef`  |
| 2637   | Layout 1 | `69946c5724ef`  |
| 2629   | Layout 1 | `69946c5724ef`  |
| 2619   | Layout 1 | `69946c5724ef`  |
| 2612   | Layout 1 | `69946c5724ef`  |
| 2606   | Layout 1 | `69946c5724ef`  |
| 2602   | Layout 1 | `69946c5724ef`  |
| 2601   | Layout 1 | `69946c5724ef`  |
| 2592   | Layout 1 | `69946c5724ef`  |
| 2583   | Layout 1 | `69946c5724ef`  |
| 2575   | Layout 1 | `69946c5724ef`  |
| 2567   | Layout 1 | `69946c5724ef`  |
| 2560   | Layout 1 | `69946c5724ef`  |
| 2553   | Layout 1 | `69946c5724ef`  |
| 2545   | Layout 1 | `69946c5724ef`  |
| 2538   | Layout 1 | `69946c5724ef`  |
| 2529   | Layout 1 | `69946c5724ef`  |
| 2519   | Layout 1 | `69946c5724ef`  |
| 2513   | Layout 1 | `69946c5724ef`  |
| 2510   | Layout 1 | `69946c5724ef`  |
| 2507   | Layout 1 | `69946c5724ef`  |
| 2503   | Layout 1 | `69946c5724ef`  |
| 2498   | Layout 1 | `69946c5724ef`  |
| 2492   | Layout 1 | `69946c5724ef`  |
| 2487   | Layout 1 | `69946c5724ef`  |
| 2480   | Layout 1 | `69946c5724ef`  |
| 2474   | Layout 1 | `69946c5724ef`  |
| 2468   | Layout 1 | `69946c5724ef`  |
| 2460   | Layout 1 | `69946c5724ef`  |
| 2453   | Layout 1 | `69946c5724ef`  |
| 2444   | Layout 1 | `69946c5724ef`  |
| 2438   | Layout 1 | `69946c5724ef`  |
| 2434   | Layout 1 | `69946c5724ef`  |
| 2429   | Layout 1 | `69946c5724ef`  |
| 2421   | Layout 1 | `69946c5724ef`  |
| 2414   | Layout 1 | `69946c5724ef`  |
| 2407   | Layout 1 | `69946c5724ef`  |
| 2401   | Layout 1 | `69946c5724ef`  |
| 2397   | Layout 1 | `69946c5724ef`  |
| 2393   | Layout 1 | `69946c5724ef`  |
| 2384   | Layout 1 | `69946c5724ef`  |
| 2378   | Layout 1 | `69946c5724ef`  |
| 2372   | Layout 1 | `69946c5724ef`  |
| 2358   | Layout 1 | `69946c5724ef`  |
| 2352   | Layout 1 | `69946c5724ef`  |
| 2347   | Layout 1 | `69946c5724ef`  |
| 2343   | Layout 1 | `69946c5724ef`  |
| 2335   | Layout 1 | `69946c5724ef`  |
| 2327   | Layout 1 | `69946c5724ef`  |
| 2324   | Layout 1 | `69946c5724ef`  |
| 2319   | Layout 1 | `69946c5724ef`  |
| 2313   | Layout 1 | `69946c5724ef`  |
| 2308   | Layout 1 | `69946c5724ef`  |
| 2302   | Layout 1 | `69946c5724ef`  |
| 2295   | Layout 1 | `69946c5724ef`  |
| 2290   | Layout 1 | `69946c5724ef`  |
| 2284   | Layout 1 | `69946c5724ef`  |
| 2276   | Layout 1 | `69946c5724ef`  |
| 2269   | Layout 1 | `69946c5724ef`  |
| 2259   | Layout 1 | `69946c5724ef`  |
| 2250   | Layout 1 | `69946c5724ef`  |
| 2243   | Layout 1 | `69946c5724ef`  |
| 2235   | Layout 1 | `69946c5724ef`  |
| 2229   | Layout 1 | `69946c5724ef`  |
| 2224   | Layout 1 | `69946c5724ef`  |
| 2218   | Layout 1 | `69946c5724ef`  |
| 2215   | Layout 1 | `69946c5724ef`  |
| 2207   | Layout 1 | `69946c5724ef`  |
| 2203   | Layout 1 | `69946c5724ef`  |
| 2196   | Layout 1 | `69946c5724ef`  |
| 2192   | Layout 1 | `69946c5724ef`  |
| 2189   | Layout 1 | `69946c5724ef`  |
| 2183   | Layout 1 | `69946c5724ef`  |
| 2179   | Layout 1 | `69946c5724ef`  |
| 2171   | Layout 1 | `69946c5724ef`  |
| 2163   | Layout 1 | `69946c5724ef`  |
| 2156   | Layout 1 | `69946c5724ef`  |
| 2151   | Layout 1 | `69946c5724ef`  |
| 2147   | Layout 1 | `69946c5724ef`  |
| 2142   | Layout 1 | `69946c5724ef`  |
| 2138   | Layout 1 | `69946c5724ef`  |
| 2134   | Layout 1 | `69946c5724ef`  |
| 2130   | Layout 1 | `69946c5724ef`  |
| 2122   | Layout 1 | `69946c5724ef`  |
| 2107   | Layout 1 | `69946c5724ef`  |
| 2098   | Layout 1 | `69946c5724ef`  |
| 2089   | Layout 1 | `69946c5724ef`  |
| 2081   | Layout 1 | `69946c5724ef`  |
| 2073   | Layout 1 | `69946c5724ef`  |
| 2067   | Layout 1 | `69946c5724ef`  |
| 2063   | Layout 1 | `69946c5724ef`  |
| 2059   | Layout 1 | `69946c5724ef`  |
| 2052   | Layout 1 | `69946c5724ef`  |
| 2044   | Layout 1 | `69946c5724ef`  |
| 2039   | Layout 1 | `69946c5724ef`  |
| 2032   | Layout 1 | `69946c5724ef`  |
| 2025   | Layout 1 | `69946c5724ef`  |
| 2011   | Layout 1 | `69946c5724ef`  |
| 2005   | Layout 1 | `69946c5724ef`  |
| 2000   | Layout 1 | `69946c5724ef`  |
| 1996   | Layout 1 | `69946c5724ef`  |
| 1991   | Layout 1 | `69946c5724ef`  |
| 1985   | Layout 1 | `69946c5724ef`  |
| 1980   | Layout 1 | `69946c5724ef`  |
| 1969   | Layout 1 | `69946c5724ef`  |
| 1964   | Layout 1 | `69946c5724ef`  |
| 1958   | Layout 1 | `69946c5724ef`  |
| 1950   | Layout 1 | `69946c5724ef`  |
| 1945   | Layout 1 | `69946c5724ef`  |
| 1937   | Layout 1 | `69946c5724ef`  |
| 1933   | Layout 1 | `69946c5724ef`  |
| 1927   | Layout 1 | `69946c5724ef`  |
| 1921   | Layout 1 | `69946c5724ef`  |
| 1914   | Layout 1 | `69946c5724ef`  |
| 1908   | Layout 1 | `69946c5724ef`  |
| 1897   | Layout 1 | `69946c5724ef`  |
| 1892   | Layout 1 | `69946c5724ef`  |
| 1886   | Layout 1 | `69946c5724ef`  |
| 1881   | Layout 1 | `69946c5724ef`  |
| 1871   | Layout 1 | `69946c5724ef`  |
| 1866   | Layout 1 | `69946c5724ef`  |
| 1862   | Layout 1 | `69946c5724ef`  |
| 1854   | Layout 1 | `69946c5724ef`  |
| 1846   | Layout 1 | `69946c5724ef`  |
| 1838   | Layout 1 | `69946c5724ef`  |
| 1832   | Layout 1 | `69946c5724ef`  |
| 1826   | Layout 1 | `69946c5724ef`  |
| 1822   | Layout 1 | `69946c5724ef`  |
| 1818   | Layout 1 | `69946c5724ef`  |
| 1804   | Layout 1 | `69946c5724ef`  |
| 1794   | Layout 1 | `69946c5724ef`  |
| 1790   | Layout 1 | `69946c5724ef`  |
| 1784   | Layout 1 | `69946c5724ef`  |
| 1774   | Layout 1 | `69946c5724ef`  |
| 1771   | Layout 1 | `69946c5724ef`  |
| 1762   | Layout 1 | `69946c5724ef`  |
| 1759   | Layout 1 | `69946c5724ef`  |
| 1754   | Layout 1 | `69946c5724ef`  |
| 1749   | Layout 1 | `69946c5724ef`  |
| 1743   | Layout 1 | `69946c5724ef`  |
| 1737   | Layout 1 | `69946c5724ef`  |
| 1731   | Layout 1 | `69946c5724ef`  |
| 1725   | Layout 1 | `69946c5724ef`  |
| 1717   | Layout 1 | `69946c5724ef`  |
| 1710   | Layout 1 | `69946c5724ef`  |
| 1704   | Layout 1 | `69946c5724ef`  |
| 1698   | Layout 1 | `69946c5724ef`  |
| 1690   | Layout 1 | `69946c5724ef`  |
| 1685   | Layout 1 | `69946c5724ef`  |
| 1680   | Layout 1 | `69946c5724ef`  |
| 1674   | Layout 1 | `69946c5724ef`  |
| 1668   | Layout 1 | `69946c5724ef`  |
| 1659   | Layout 1 | `69946c5724ef`  |
| 1649   | Layout 1 | `69946c5724ef`  |
| 1642   | Layout 1 | `69946c5724ef`  |
| 1636   | Layout 1 | `69946c5724ef`  |
| 1628   | Layout 1 | `69946c5724ef`  |
| 1622   | Layout 1 | `69946c5724ef`  |
| 1614   | Layout 1 | `69946c5724ef`  |
| 1608   | Layout 1 | `69946c5724ef`  |
| 1602   | Layout 1 | `69946c5724ef`  |
| 1598   | Layout 1 | `69946c5724ef`  |
| 1594   | Layout 1 | `69946c5724ef`  |
| 1590   | Layout 1 | `69946c5724ef`  |
| 1587   | Layout 1 | `69946c5724ef`  |
| 1584   | Layout 1 | `69946c5724ef`  |
| 1579   | Layout 1 | `69946c5724ef`  |
| 1572   | Layout 1 | `69946c5724ef`  |
| 1565   | Layout 1 | `69946c5724ef`  |
| 1559   | Layout 1 | `69946c5724ef`  |
| 1554   | Layout 1 | `69946c5724ef`  |
| 1547   | Layout 1 | `69946c5724ef`  |
| 1537   | Layout 1 | `69946c5724ef`  |
| 1529   | Layout 1 | `69946c5724ef`  |
| 1524   | Layout 1 | `69946c5724ef`  |
| 1519   | Layout 1 | `69946c5724ef`  |
| 1509   | Layout 1 | `69946c5724ef`  |
| 1506   | Layout 1 | `69946c5724ef`  |
| 1504   | Layout 1 | `69946c5724ef`  |
| 1500   | No file  | `69946c5724ef`  |
| 1493   | No file  | `69946c5724ef`  |
| 1489   | No file  | `69946c5724ef`  |
| 1485   | No file  | `69946c5724ef`  |
| 1481   | No file  | `69946c5724ef`  |
| 1474   | No file  | `69946c5724ef`  |
| 1466   | No file  | `69946c5724ef`  |
| 1462   | No file  | `69946c5724ef`  |
| 1459   | No file  | `69946c5724ef`  |
| 1453   | No file  | `69946c5724ef`  |
| 1450   | No file  | `69946c5724ef`  |
| 1445   | No file  | `69946c5724ef`  |
| 1439   | No file  | `69946c5724ef`  |
| 1433   | No file  | `69946c5724ef`  |
| 1430   | No file  | `69946c5724ef`  |
| 1426   | No file  | `69946c5724ef`  |
| 1421   | No file  | `69946c5724ef`  |
| 1417   | No file  | `69946c5724ef`  |
| 1416   | No file  | `69946c5724ef`  |
| 1409   | No file  | `69946c5724ef`  |
| 1405   | No file  | `69946c5724ef`  |
| 1401   | No file  | `69946c5724ef`  |
| 1396   | No file  | `69946c5724ef`  |
| 1391   | No file  | `69946c5724ef`  |
| 1390   | No file  | `69946c5724ef`  |
| 1386   | No file  | `69946c5724ef`  |
| 1381   | No file  | `69946c5724ef`  |
| 1379   | No file  | `69946c5724ef`  |
| 1372   | No file  | `69946c5724ef`  |
| 1366   | No file  | `69946c5724ef`  |
| 1364   | No file  | `69946c5724ef`  |
| 1363   | No file  | `69946c5724ef`  |
| 1360   | No file  | `69946c5724ef`  |
| 1358   | No file  | `69946c5724ef`  |
| 1355   | No file  | `69946c5724ef`  |
| 1351   | No file  | `69946c5724ef`  |
| 1348   | No file  | `69946c5724ef`  |
| 1346   | No file  | `69946c5724ef`  |
| 1341   | No file  | `69946c5724ef`  |
| 1340   | No file  | `69946c5724ef`  |
| 1338   | No file  | `69946c5724ef`  |
| 1335   | No file  | `69946c5724ef`  |
| 1333   | No file  | `69946c5724ef`  |
| 1329   | No file  | `69946c5724ef`  |
| 1327   | No file  | `69946c5724ef`  |
| 1324   | No file  | `69946c5724ef`  |
| 1321   | No file  | `69946c5724ef`  |
| 1319   | No file  | `69946c5724ef`  |
| 1318   | No file  | `69946c5724ef`  |
| 1316   | No file  | `69946c5724ef`  |
| 1313   | No file  | `69946c5724ef`  |
| 1311   | No file  | `69946c5724ef`  |
| 1309   | No file  | `69946c5724ef`  |
| 1304   | No file  | `69946c5724ef`  |
| 1292   | No file  | `69946c5724ef`  |
| 1286   | No file  | `69946c5724ef`  |
| 1280   | No file  | `69946c5724ef`  |
| 1276   | No file  | `69946c5724ef`  |
| 1267   | No file  | `69946c5724ef`  |
| 1261   | No file  | `69946c5724ef`  |
| 1256   | No file  | `69946c5724ef`  |
| 1250   | No file  | `69946c5724ef`  |
| 1246   | No file  | `69946c5724ef`  |
| 1239   | No file  | `69946c5724ef`  |
| 1230   | No file  | `69946c5724ef`  |
| 1226   | No file  | `69946c5724ef`  |
| 1220   | No file  | `69946c5724ef`  |
| 1217   | No file  | `69946c5724ef`  |
| 1211   | No file  | `69946c5724ef`  |
| 1210   | No file  | `69946c5724ef`  |
| 1208   | No file  | `69946c5724ef`  |
| 1203   | No file  | `69946c5724ef`  |
| 1197   | No file  | `69946c5724ef`  |
| 1194   | No file  | `69946c5724ef`  |
| 1192   | No file  | `69946c5724ef`  |
| 1187   | No file  | `69946c5724ef`  |
| 1183   | No file  | `69946c5724ef`  |
| 1177   | No file  | `69946c5724ef`  |
| 1173   | No file  | `69946c5724ef`  |
| 1167   | No file  | `69946c5724ef`  |
| 1164   | No file  | `69946c5724ef`  |
| 1156   | No file  | `69946c5724ef`  |
| 1149   | No file  | `69946c5724ef`  |
| 1144   | No file  | `69946c5724ef`  |
| 1137   | No file  | `69946c5724ef`  |
| 1132   | No file  | `69946c5724ef`  |
| 1127   | No file  | `69946c5724ef`  |
| 1122   | No file  | `69946c5724ef`  |
| 1118   | No file  | `69946c5724ef`  |
| 1114   | No file  | `69946c5724ef`  |
| 1109   | No file  | `69946c5724ef`  |
| 1102   | No file  | `69946c5724ef`  |
| 1096   | No file  | `69946c5724ef`  |
| 1088   | No file  | `69946c5724ef`  |
| 1081   | No file  | `69946c5724ef`  |
| 1076   | No file  | `69946c5724ef`  |
| 1069   | No file  | `69946c5724ef`  |
| 1064   | No file  | `69946c5724ef`  |
| 1058   | No file  | `69946c5724ef`  |
| 1051   | No file  | `69946c5724ef`  |
| 1044   | No file  | `69946c5724ef`  |
| 1036   | No file  | `69946c5724ef`  |
| 1026   | No file  | `69946c5724ef`  |
| 1016   | No file  | `69946c5724ef`  |
| 1009   | No file  | `69946c5724ef`  |
| 1005   | No file  | `69946c5724ef`  |
| 1000   | No file  | `69946c5724ef`  |
| 998    | No file  | `69946c5724ef`  |
| 990    | No file  | `69946c5724ef`  |
| 979    | No file  | `69946c5724ef`  |
| 972    | No file  | `69946c5724ef`  |
| 963    | No file  | `69946c5724ef`  |
| 955    | No file  | `69946c5724ef`  |
| 946    | No file  | `69946c5724ef`  |
| 938    | No file  | `69946c5724ef`  |
| 927    | No file  | `69946c5724ef`  |
| 911    | No file  | `69946c5724ef`  |
| 904    | No file  | `69946c5724ef`  |
| 899    | No file  | `69946c5724ef`  |
| 894    | No file  | `69946c5724ef`  |
| 885    | No file  | `69946c5724ef`  |
| 879    | No file  | `69946c5724ef`  |
| 872    | No file  | `69946c5724ef`  |
| 864    | No file  | `69946c5724ef`  |
| 855    | No file  | `69946c5724ef`  |
| 853    | No file  | `69946c5724ef`  |
| 845    | No file  | `69946c5724ef`  |
| 837    | No file  | `69946c5724ef`  |
| 829    | No file  | `69946c5724ef`  |
| 822    | No file  | `69946c5724ef`  |
| 814    | No file  | `69946c5724ef`  |
| 805    | No file  | `69946c5724ef`  |
| 794    | No file  | `69946c5724ef`  |
| 787    | No file  | `69946c5724ef`  |
| 780    | No file  | `69946c5724ef`  |
| 771    | No file  | `69946c5724ef`  |
| 760    | No file  | `69946c5724ef`  |
| 748    | No file  | `69946c5724ef`  |
| 741    | No file  | `69946c5724ef`  |
| 736    | No file  | `69946c5724ef`  |
| 731    | No file  | `69946c5724ef`  |
| 723    | No file  | `69946c5724ef`  |
| 711    | No file  | `69946c5724ef`  |
| 707    | No file  | `69946c5724ef`  |
| 697    | No file  | `69946c5724ef`  |
| 689    | No file  | `69946c5724ef`  |
| 683    | No file  | `69946c5724ef`  |
| 678    | No file  | `69946c5724ef`  |
| 670    | No file  | `69946c5724ef`  |
| 661    | No file  | `69946c5724ef`  |
| 656    | No file  | `69946c5724ef`  |
| 652    | No file  | `69946c5724ef`  |
| 643    | No file  | `69946c5724ef`  |
| 637    | No file  | `69946c5724ef`  |
| 630    | No file  | `69946c5724ef`  |
| 627    | No file  | `69946c5724ef`  |
| 621    | No file  | `69946c5724ef`  |
| 617    | No file  | `69946c5724ef`  |
| 615    | No file  | `69946c5724ef`  |
| 606    | No file  | `69946c5724ef`  |
| 599    | No file  | `69946c5724ef`  |
| 592    | No file  | `69946c5724ef`  |
| 586    | No file  | `69946c5724ef`  |
| 577    | No file  | `69946c5724ef`  |
| 569    | No file  | `69946c5724ef`  |
| 561    | No file  | `69946c5724ef`  |
| 554    | No file  | `69946c5724ef`  |
| 542    | No file  | `69946c5724ef`  |
| 532    | No file  | `69946c5724ef`  |
| 531    | No file  | `69946c5724ef`  |
| 526    | No file  | `69946c5724ef`  |
| 521    | No file  | `69946c5724ef`  |
| 517    | No file  | `69946c5724ef`  |
| 510    | No file  | `69946c5724ef`  |
| 508    | No file  | `69946c5724ef`  |
| 504    | No file  | `69946c5724ef`  |
| 497    | No file  | `69946c5724ef`  |
| 491    | No file  | `69946c5724ef`  |
| 485    | No file  | `69946c5724ef`  |
| 478    | No file  | `69946c5724ef`  |
| 472    | No file  | `69946c5724ef`  |
| 466    | No file  | `69946c5724ef`  |
| 457    | No file  | `69946c5724ef`  |
| 452    | No file  | `69946c5724ef`  |
| 449    | No file  | `69946c5724ef`  |
| 435    | No file  | `69946c5724ef`  |

<!-- versions:end -->

## Companion Files

None. The handler names each item with LOC type 0 from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of items                               |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (8 bytes)

| Offset  | Type | Field                    | Notes                                                       |
| ------- | ---- | ------------------------ | ----------------------------------------------------------- |
| `+0x00` | u32  | item_key                 | The item (LOC type 0 name); unique per file                 |
| `+0x04` | u32  | expiration_period_notify | `1440` on every row (clients 1784 and 3483); see Open Questions |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Field Names

The names follow the `Notice_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_itemdatatable_cash.xlsm`: columns `ItemKey`,
`ExpirationPeriodNotify` and `ContentsGroupKey`, 187 rows. All 153 rows of
the client 1784 file have their key in the sheet (153 of 153), and the
sheet's `ExpirationPeriodNotify` is `1440` on every row, as in the file.
`ContentsGroupKey` is not in the file; the xlsm's `#아이템 명` column (the
Korean item name) is not compiled.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/item_tables.py`: the item
  key, its icon and LOC name, and `expiration_period_notify`.

## Open Questions

### The Unit of `expiration_period_notify`

`1440` is the number of minutes in a day, and `itemenchant.dbss` stores an
item's expiry in minutes (`expiration_minutes`), so the value is likely
the time before expiry at which the notice starts. With one value on every
row of both clients, no data tells minutes from another unit.
