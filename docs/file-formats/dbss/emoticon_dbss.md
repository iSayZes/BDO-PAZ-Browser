# `emoticon.dbss` Format

## Purpose

The chat emoticons (emoji): one row per emoticon with its icon, the
animated sequence sheet the chat window plays, the chat keyword that inserts
it (`(Angry)`) and its Korean name. Row `1` is the item link icon sheet of
the chat window. The chat Lua reads the rows through
`ToClient_getEmoticonInfoList()`, `ToClient_getEmoticonInfoByIndex()` and
`ToClient_getEmoticonInfoByKey()` and their getters `getIconPath()`,
`getSequenceImagePath()`, `getName()` and `getKeyword()`
(`panel_chat_emoticon.luac`, `panel_widget_chatmain_2.luac`). Which
emoticons a player can use comes from
[`emoticonpackage.dbss`](emoticonpackage_dbss.md). Companion
`emoticonoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes  | Records       | Row bytes                  |
| ------ | -------------- | --------------------- | ------ | ------------- | -------------------------- |
| 1      | 1280 and later | `emoticon.dbss`       | 26,336 | 87 Row        | 140 to 342, 303 on average |
| 1      | 1280 and later | `emoticonoffset.dbss` | 1,396  | 87 Offset Row | 16                         |

| Layout | File                  | Known            | Unknown       |
| ------ | --------------------- | ---------------- | ------------- |
| 1      | `emoticon.dbss`       | 25,640 B (97.4%) | 696 B (2.6%)  |
| 1      | `emoticonoffset.dbss` | 1,048 B (75.1%)  | 348 B (24.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `228354c5913f`  |
| 3482   | Layout 1 | `228354c5913f`  |
| 3474   | Layout 1 | `228354c5913f`  |
| 3473   | Layout 1 | `228354c5913f`  |
| 3464   | Layout 1 | `228354c5913f`  |
| 3458   | Layout 1 | `228354c5913f`  |
| 3454   | Layout 1 | `228354c5913f`  |
| 3444   | Layout 1 | `228354c5913f`  |
| 3435   | Layout 1 | `228354c5913f`  |
| 3426   | Layout 1 | `228354c5913f`  |
| 3418   | Layout 1 | `228354c5913f`  |
| 3412   | Layout 1 | `228354c5913f`  |
| 3402   | Layout 1 | `228354c5913f`  |
| 3396   | Layout 1 | `228354c5913f`  |
| 3387   | Layout 1 | `228354c5913f`  |
| 3381   | Layout 1 | `228354c5913f`  |
| 3373   | Layout 1 | `228354c5913f`  |
| 3364   | Layout 1 | `228354c5913f`  |
| 3356   | Layout 1 | `228354c5913f`  |
| 3349   | Layout 1 | `228354c5913f`  |
| 3342   | Layout 1 | `228354c5913f`  |
| 3335   | Layout 1 | `228354c5913f`  |
| 3326   | Layout 1 | `228354c5913f`  |
| 3321   | Layout 1 | `228354c5913f`  |
| 3314   | Layout 1 | `228354c5913f`  |
| 3303   | Layout 1 | `228354c5913f`  |
| 3302   | Layout 1 | `228354c5913f`  |
| 3293   | Layout 1 | `228354c5913f`  |
| 3283   | Layout 1 | `228354c5913f`  |
| 3275   | Layout 1 | `228354c5913f`  |
| 3267   | Layout 1 | `228354c5913f`  |
| 3258   | Layout 1 | `228354c5913f`  |
| 3251   | Layout 1 | `228354c5913f`  |
| 3242   | Layout 1 | `228354c5913f`  |
| 3235   | Layout 1 | `228354c5913f`  |
| 3229   | Layout 1 | `228354c5913f`  |
| 3212   | Layout 1 | `228354c5913f`  |
| 3203   | Layout 1 | `228354c5913f`  |
| 3193   | Layout 1 | `228354c5913f`  |
| 3186   | Layout 1 | `228354c5913f`  |
| 3177   | Layout 1 | `228354c5913f`  |
| 3169   | Layout 1 | `228354c5913f`  |
| 3158   | Layout 1 | `228354c5913f`  |
| 3151   | Layout 1 | `228354c5913f`  |
| 3144   | Layout 1 | `228354c5913f`  |
| 3133   | Layout 1 | `228354c5913f`  |
| 3125   | Layout 1 | `228354c5913f`  |
| 3118   | Layout 1 | `228354c5913f`  |
| 3111   | Layout 1 | `228354c5913f`  |
| 3103   | Layout 1 | `228354c5913f`  |
| 3095   | Layout 1 | `228354c5913f`  |
| 3086   | Layout 1 | `228354c5913f`  |
| 3072   | Layout 1 | `228354c5913f`  |
| 3062   | Layout 1 | `228354c5913f`  |
| 3052   | Layout 1 | `228354c5913f`  |
| 3045   | Layout 1 | `228354c5913f`  |
| 3037   | Layout 1 | `228354c5913f`  |
| 3030   | Layout 1 | `228354c5913f`  |
| 3021   | Layout 1 | `228354c5913f`  |
| 3012   | Layout 1 | `228354c5913f`  |
| 3002   | Layout 1 | `228354c5913f`  |
| 2995   | Layout 1 | `228354c5913f`  |
| 2987   | Layout 1 | `228354c5913f`  |
| 2978   | Layout 1 | `228354c5913f`  |
| 2970   | Layout 1 | `228354c5913f`  |
| 2959   | Layout 1 | `228354c5913f`  |
| 2951   | Layout 1 | `228354c5913f`  |
| 2942   | Layout 1 | `228354c5913f`  |
| 2935   | Layout 1 | `228354c5913f`  |
| 2932   | Layout 1 | `228354c5913f`  |
| 2923   | Layout 1 | `228354c5913f`  |
| 2919   | Layout 1 | `228354c5913f`  |
| 2907   | Layout 1 | `228354c5913f`  |
| 2900   | Layout 1 | `228354c5913f`  |
| 2891   | Layout 1 | `228354c5913f`  |
| 2882   | Layout 1 | `228354c5913f`  |
| 2872   | Layout 1 | `228354c5913f`  |
| 2863   | Layout 1 | `228354c5913f`  |
| 2855   | Layout 1 | `228354c5913f`  |
| 2849   | Layout 1 | `228354c5913f`  |
| 2844   | Layout 1 | `228354c5913f`  |
| 2834   | Layout 1 | `228354c5913f`  |
| 2825   | Layout 1 | `228354c5913f`  |
| 2819   | Layout 1 | `228354c5913f`  |
| 2811   | Layout 1 | `228354c5913f`  |
| 2803   | Layout 1 | `228354c5913f`  |
| 2794   | Layout 1 | `228354c5913f`  |
| 2783   | Layout 1 | `228354c5913f`  |
| 2774   | Layout 1 | `228354c5913f`  |
| 2765   | Layout 1 | `228354c5913f`  |
| 2756   | Layout 1 | `228354c5913f`  |
| 2750   | Layout 1 | `228354c5913f`  |
| 2743   | Layout 1 | `228354c5913f`  |
| 2736   | Layout 1 | `228354c5913f`  |
| 2726   | Layout 1 | `228354c5913f`  |
| 2717   | Layout 1 | `228354c5913f`  |
| 2709   | Layout 1 | `228354c5913f`  |
| 2703   | Layout 1 | `228354c5913f`  |
| 2695   | Layout 1 | `228354c5913f`  |
| 2684   | Layout 1 | `228354c5913f`  |
| 2672   | Layout 1 | `228354c5913f`  |
| 2665   | Layout 1 | `228354c5913f`  |
| 2657   | Layout 1 | `228354c5913f`  |
| 2649   | Layout 1 | `228354c5913f`  |
| 2644   | Layout 1 | `228354c5913f`  |
| 2637   | Layout 1 | `228354c5913f`  |
| 2629   | Layout 1 | `228354c5913f`  |
| 2619   | Layout 1 | `228354c5913f`  |
| 2612   | Layout 1 | `228354c5913f`  |
| 2606   | Layout 1 | `228354c5913f`  |
| 2602   | Layout 1 | `228354c5913f`  |
| 2601   | Layout 1 | `228354c5913f`  |
| 2592   | Layout 1 | `228354c5913f`  |
| 2583   | Layout 1 | `228354c5913f`  |
| 2575   | Layout 1 | `228354c5913f`  |
| 2567   | Layout 1 | `228354c5913f`  |
| 2560   | Layout 1 | `228354c5913f`  |
| 2553   | Layout 1 | `228354c5913f`  |
| 2545   | Layout 1 | `228354c5913f`  |
| 2538   | Layout 1 | `228354c5913f`  |
| 2529   | Layout 1 | `228354c5913f`  |
| 2519   | Layout 1 | `228354c5913f`  |
| 2513   | Layout 1 | `228354c5913f`  |
| 2510   | Layout 1 | `228354c5913f`  |
| 2507   | Layout 1 | `228354c5913f`  |
| 2503   | Layout 1 | `228354c5913f`  |
| 2498   | Layout 1 | `228354c5913f`  |
| 2492   | Layout 1 | `228354c5913f`  |
| 2487   | Layout 1 | `228354c5913f`  |
| 2480   | Layout 1 | `228354c5913f`  |
| 2474   | Layout 1 | `228354c5913f`  |
| 2468   | Layout 1 | `228354c5913f`  |
| 2460   | Layout 1 | `228354c5913f`  |
| 2453   | Layout 1 | `228354c5913f`  |
| 2444   | Layout 1 | `228354c5913f`  |
| 2438   | Layout 1 | `228354c5913f`  |
| 2434   | Layout 1 | `228354c5913f`  |
| 2429   | Layout 1 | `228354c5913f`  |
| 2421   | Layout 1 | `228354c5913f`  |
| 2414   | Layout 1 | `228354c5913f`  |
| 2407   | Layout 1 | `228354c5913f`  |
| 2401   | Layout 1 | `228354c5913f`  |
| 2397   | Layout 1 | `228354c5913f`  |
| 2393   | Layout 1 | `228354c5913f`  |
| 2384   | Layout 1 | `228354c5913f`  |
| 2378   | Layout 1 | `228354c5913f`  |
| 2372   | Layout 1 | `228354c5913f`  |
| 2358   | Layout 1 | `228354c5913f`  |
| 2352   | Layout 1 | `228354c5913f`  |
| 2347   | Layout 1 | `228354c5913f`  |
| 2343   | Layout 1 | `228354c5913f`  |
| 2335   | Layout 1 | `228354c5913f`  |
| 2327   | Layout 1 | `228354c5913f`  |
| 2324   | Layout 1 | `228354c5913f`  |
| 2319   | Layout 1 | `228354c5913f`  |
| 2313   | Layout 1 | `228354c5913f`  |
| 2308   | Layout 1 | `228354c5913f`  |
| 2302   | Layout 1 | `228354c5913f`  |
| 2295   | Layout 1 | `228354c5913f`  |
| 2290   | Layout 1 | `228354c5913f`  |
| 2284   | Layout 1 | `228354c5913f`  |
| 2276   | Layout 1 | `228354c5913f`  |
| 2269   | Layout 1 | `228354c5913f`  |
| 2259   | Layout 1 | `228354c5913f`  |
| 2250   | Layout 1 | `228354c5913f`  |
| 2243   | Layout 1 | `228354c5913f`  |
| 2235   | Layout 1 | `228354c5913f`  |
| 2229   | Layout 1 | `228354c5913f`  |
| 2224   | Layout 1 | `228354c5913f`  |
| 2218   | Layout 1 | `228354c5913f`  |
| 2215   | Layout 1 | `228354c5913f`  |
| 2207   | Layout 1 | `228354c5913f`  |
| 2203   | Layout 1 | `228354c5913f`  |
| 2196   | Layout 1 | `228354c5913f`  |
| 2192   | Layout 1 | `228354c5913f`  |
| 2189   | Layout 1 | `228354c5913f`  |
| 2183   | Layout 1 | `228354c5913f`  |
| 2179   | Layout 1 | `228354c5913f`  |
| 2171   | Layout 1 | `228354c5913f`  |
| 2163   | Layout 1 | `228354c5913f`  |
| 2156   | Layout 1 | `228354c5913f`  |
| 2151   | Layout 1 | `228354c5913f`  |
| 2147   | Layout 1 | `228354c5913f`  |
| 2142   | Layout 1 | `228354c5913f`  |
| 2138   | Layout 1 | `228354c5913f`  |
| 2134   | Layout 1 | `228354c5913f`  |
| 2130   | Layout 1 | `228354c5913f`  |
| 2122   | Layout 1 | `228354c5913f`  |
| 2107   | Layout 1 | `228354c5913f`  |
| 2098   | Layout 1 | `228354c5913f`  |
| 2089   | Layout 1 | `228354c5913f`  |
| 2081   | Layout 1 | `228354c5913f`  |
| 2073   | Layout 1 | `228354c5913f`  |
| 2067   | Layout 1 | `228354c5913f`  |
| 2063   | Layout 1 | `228354c5913f`  |
| 2059   | Layout 1 | `228354c5913f`  |
| 2052   | Layout 1 | `228354c5913f`  |
| 2044   | Layout 1 | `228354c5913f`  |
| 2039   | Layout 1 | `228354c5913f`  |
| 2032   | Layout 1 | `228354c5913f`  |
| 2025   | Layout 1 | `228354c5913f`  |
| 2011   | Layout 1 | `228354c5913f`  |
| 2005   | Layout 1 | `228354c5913f`  |
| 2000   | Layout 1 | `228354c5913f`  |
| 1996   | Layout 1 | `228354c5913f`  |
| 1991   | Layout 1 | `228354c5913f`  |
| 1985   | Layout 1 | `228354c5913f`  |
| 1980   | Layout 1 | `228354c5913f`  |
| 1969   | Layout 1 | `228354c5913f`  |
| 1964   | Layout 1 | `228354c5913f`  |
| 1958   | Layout 1 | `228354c5913f`  |
| 1950   | Layout 1 | `228354c5913f`  |
| 1945   | Layout 1 | `228354c5913f`  |
| 1937   | Layout 1 | `228354c5913f`  |
| 1933   | Layout 1 | `228354c5913f`  |
| 1927   | Layout 1 | `228354c5913f`  |
| 1921   | Layout 1 | `228354c5913f`  |
| 1914   | Layout 1 | `228354c5913f`  |
| 1908   | Layout 1 | `228354c5913f`  |
| 1897   | Layout 1 | `228354c5913f`  |
| 1892   | Layout 1 | `228354c5913f`  |
| 1886   | Layout 1 | `228354c5913f`  |
| 1881   | Layout 1 | `228354c5913f`  |
| 1871   | Layout 1 | `228354c5913f`  |
| 1866   | Layout 1 | `228354c5913f`  |
| 1862   | Layout 1 | `228354c5913f`  |
| 1854   | Layout 1 | `228354c5913f`  |
| 1846   | Layout 1 | `228354c5913f`  |
| 1838   | Layout 1 | `228354c5913f`  |
| 1832   | Layout 1 | `228354c5913f`  |
| 1826   | Layout 1 | `228354c5913f`  |
| 1822   | Layout 1 | `228354c5913f`  |
| 1818   | Layout 1 | `228354c5913f`  |
| 1804   | Layout 1 | `228354c5913f`  |
| 1794   | Layout 1 | `228354c5913f`  |
| 1790   | Layout 1 | `228354c5913f`  |
| 1784   | Layout 1 | `228354c5913f`  |
| 1774   | Layout 1 | `228354c5913f`  |
| 1771   | Layout 1 | `228354c5913f`  |
| 1762   | Layout 1 | `228354c5913f`  |
| 1759   | Layout 1 | `228354c5913f`  |
| 1754   | Layout 1 | `228354c5913f`  |
| 1749   | Layout 1 | `228354c5913f`  |
| 1743   | Layout 1 | `228354c5913f`  |
| 1737   | Layout 1 | `228354c5913f`  |
| 1731   | Layout 1 | `228354c5913f`  |
| 1725   | Layout 1 | `228354c5913f`  |
| 1717   | Layout 1 | `228354c5913f`  |
| 1710   | Layout 1 | `228354c5913f`  |
| 1704   | Layout 1 | `228354c5913f`  |
| 1698   | Layout 1 | `228354c5913f`  |
| 1690   | Layout 1 | `228354c5913f`  |
| 1685   | Layout 1 | `228354c5913f`  |
| 1680   | Layout 1 | `228354c5913f`  |
| 1674   | Layout 1 | `228354c5913f`  |
| 1668   | Layout 1 | `228354c5913f`  |
| 1659   | Layout 1 | `228354c5913f`  |
| 1649   | Layout 1 | `228354c5913f`  |
| 1642   | Layout 1 | `228354c5913f`  |
| 1636   | Layout 1 | `228354c5913f`  |
| 1628   | Layout 1 | `228354c5913f`  |
| 1622   | Layout 1 | `228354c5913f`  |
| 1614   | Layout 1 | `228354c5913f`  |
| 1608   | Layout 1 | `228354c5913f`  |
| 1602   | Layout 1 | `228354c5913f`  |
| 1598   | Layout 1 | `228354c5913f`  |
| 1594   | Layout 1 | `228354c5913f`  |
| 1590   | Layout 1 | `228354c5913f`  |
| 1587   | Layout 1 | `228354c5913f`  |
| 1584   | Layout 1 | `228354c5913f`  |
| 1579   | Layout 1 | `228354c5913f`  |
| 1572   | Layout 1 | `228354c5913f`  |
| 1565   | Layout 1 | `228354c5913f`  |
| 1559   | Layout 1 | `228354c5913f`  |
| 1554   | Layout 1 | `228354c5913f`  |
| 1547   | Layout 1 | `228354c5913f`  |
| 1537   | Layout 1 | `228354c5913f`  |
| 1529   | Layout 1 | `228354c5913f`  |
| 1524   | Layout 1 | `228354c5913f`  |
| 1519   | Layout 1 | `228354c5913f`  |
| 1509   | Layout 1 | `228354c5913f`  |
| 1506   | Layout 1 | `228354c5913f`  |
| 1504   | Layout 1 | `228354c5913f`  |
| 1500   | Layout 1 | `228354c5913f`  |
| 1493   | Layout 1 | `228354c5913f`  |
| 1489   | Layout 1 | `228354c5913f`  |
| 1485   | Layout 1 | `228354c5913f`  |
| 1481   | Layout 1 | `228354c5913f`  |
| 1474   | Layout 1 | `228354c5913f`  |
| 1466   | Layout 1 | `228354c5913f`  |
| 1462   | Layout 1 | `228354c5913f`  |
| 1459   | Layout 1 | `228354c5913f`  |
| 1453   | Layout 1 | `228354c5913f`  |
| 1450   | Layout 1 | `228354c5913f`  |
| 1445   | Layout 1 | `228354c5913f`  |
| 1439   | Layout 1 | `228354c5913f`  |
| 1433   | Layout 1 | `228354c5913f`  |
| 1430   | Layout 1 | `228354c5913f`  |
| 1426   | Layout 1 | `228354c5913f`  |
| 1421   | Layout 1 | `228354c5913f`  |
| 1417   | Layout 1 | `228354c5913f`  |
| 1416   | Layout 1 | `228354c5913f`  |
| 1409   | Layout 1 | `228354c5913f`  |
| 1405   | Layout 1 | `228354c5913f`  |
| 1401   | Layout 1 | `228354c5913f`  |
| 1396   | Layout 1 | `228354c5913f`  |
| 1391   | Layout 1 | `228354c5913f`  |
| 1390   | Layout 1 | `228354c5913f`  |
| 1386   | Layout 1 | `228354c5913f`  |
| 1381   | Layout 1 | `228354c5913f`  |
| 1379   | Layout 1 | `228354c5913f`  |
| 1372   | Layout 1 | `228354c5913f`  |
| 1366   | Layout 1 | `228354c5913f`  |
| 1364   | Layout 1 | `228354c5913f`  |
| 1363   | Layout 1 | `228354c5913f`  |
| 1360   | Layout 1 | `228354c5913f`  |
| 1358   | Layout 1 | `228354c5913f`  |
| 1355   | Layout 1 | `228354c5913f`  |
| 1351   | Layout 1 | `228354c5913f`  |
| 1348   | Layout 1 | `228354c5913f`  |
| 1346   | Layout 1 | `228354c5913f`  |
| 1341   | Layout 1 | `228354c5913f`  |
| 1340   | Layout 1 | `228354c5913f`  |
| 1338   | Layout 1 | `228354c5913f`  |
| 1335   | Layout 1 | `228354c5913f`  |
| 1333   | Layout 1 | `228354c5913f`  |
| 1329   | Layout 1 | `228354c5913f`  |
| 1327   | Layout 1 | `228354c5913f`  |
| 1324   | Layout 1 | `228354c5913f`  |
| 1321   | Layout 1 | `228354c5913f`  |
| 1319   | Layout 1 | `228354c5913f`  |
| 1318   | Layout 1 | `228354c5913f`  |
| 1316   | Layout 1 | `228354c5913f`  |
| 1313   | Layout 1 | `228354c5913f`  |
| 1311   | Layout 1 | `228354c5913f`  |
| 1309   | Layout 1 | `228354c5913f`  |
| 1304   | Layout 1 | `228354c5913f`  |
| 1292   | Layout 1 | `228354c5913f`  |
| 1286   | Layout 1 | `228354c5913f`  |
| 1280   | Layout 1 | `228354c5913f`  |
| 1276   | No file  | `228354c5913f`  |
| 1267   | No file  | `228354c5913f`  |
| 1261   | No file  | `228354c5913f`  |
| 1256   | No file  | `228354c5913f`  |
| 1250   | No file  | `228354c5913f`  |
| 1246   | No file  | `228354c5913f`  |
| 1239   | No file  | `228354c5913f`  |
| 1230   | No file  | `228354c5913f`  |
| 1226   | No file  | `228354c5913f`  |
| 1220   | No file  | `228354c5913f`  |
| 1217   | No file  | `228354c5913f`  |
| 1211   | No file  | `228354c5913f`  |
| 1210   | No file  | `228354c5913f`  |
| 1208   | No file  | `228354c5913f`  |
| 1203   | No file  | `228354c5913f`  |
| 1197   | No file  | `228354c5913f`  |
| 1194   | No file  | `228354c5913f`  |
| 1192   | No file  | `228354c5913f`  |
| 1187   | No file  | `228354c5913f`  |
| 1183   | No file  | `228354c5913f`  |
| 1177   | No file  | `228354c5913f`  |
| 1173   | No file  | `228354c5913f`  |
| 1167   | No file  | `228354c5913f`  |
| 1164   | No file  | `228354c5913f`  |
| 1156   | No file  | `228354c5913f`  |
| 1149   | No file  | `228354c5913f`  |
| 1144   | No file  | `228354c5913f`  |
| 1137   | No file  | `228354c5913f`  |
| 1132   | No file  | `228354c5913f`  |
| 1127   | No file  | `228354c5913f`  |
| 1122   | No file  | `228354c5913f`  |
| 1118   | No file  | `228354c5913f`  |
| 1114   | No file  | `228354c5913f`  |
| 1109   | No file  | `228354c5913f`  |
| 1102   | No file  | `228354c5913f`  |
| 1096   | No file  | `228354c5913f`  |
| 1088   | No file  | `228354c5913f`  |
| 1081   | No file  | `228354c5913f`  |
| 1076   | No file  | `228354c5913f`  |
| 1069   | No file  | `228354c5913f`  |
| 1064   | No file  | `228354c5913f`  |
| 1058   | No file  | `228354c5913f`  |
| 1051   | No file  | `228354c5913f`  |
| 1044   | No file  | `228354c5913f`  |
| 1036   | No file  | `228354c5913f`  |
| 1026   | No file  | `228354c5913f`  |
| 1016   | No file  | `228354c5913f`  |
| 1009   | No file  | `228354c5913f`  |
| 1005   | No file  | `228354c5913f`  |
| 1000   | No file  | `228354c5913f`  |
| 998    | No file  | `228354c5913f`  |
| 990    | No file  | `228354c5913f`  |
| 979    | No file  | `228354c5913f`  |
| 972    | No file  | `228354c5913f`  |
| 963    | No file  | `228354c5913f`  |
| 955    | No file  | `228354c5913f`  |
| 946    | No file  | `228354c5913f`  |
| 938    | No file  | `228354c5913f`  |
| 927    | No file  | `228354c5913f`  |
| 911    | No file  | `228354c5913f`  |
| 904    | No file  | `228354c5913f`  |
| 899    | No file  | `228354c5913f`  |
| 894    | No file  | `228354c5913f`  |
| 885    | No file  | `228354c5913f`  |
| 879    | No file  | `228354c5913f`  |
| 872    | No file  | `228354c5913f`  |
| 864    | No file  | `228354c5913f`  |
| 855    | No file  | `228354c5913f`  |
| 853    | No file  | `228354c5913f`  |
| 845    | No file  | `228354c5913f`  |
| 837    | No file  | `228354c5913f`  |
| 829    | No file  | `228354c5913f`  |
| 822    | No file  | `228354c5913f`  |
| 814    | No file  | `228354c5913f`  |
| 805    | No file  | `228354c5913f`  |
| 794    | No file  | `228354c5913f`  |
| 787    | No file  | `228354c5913f`  |
| 780    | No file  | `228354c5913f`  |
| 771    | No file  | `228354c5913f`  |
| 760    | No file  | `228354c5913f`  |
| 748    | No file  | `228354c5913f`  |
| 741    | No file  | `228354c5913f`  |
| 736    | No file  | `228354c5913f`  |
| 731    | No file  | `228354c5913f`  |
| 723    | No file  | `228354c5913f`  |
| 711    | No file  | `228354c5913f`  |
| 707    | No file  | `228354c5913f`  |
| 697    | No file  | `228354c5913f`  |
| 689    | No file  | `228354c5913f`  |
| 683    | No file  | `228354c5913f`  |
| 678    | No file  | `228354c5913f`  |
| 670    | No file  | `228354c5913f`  |
| 661    | No file  | `228354c5913f`  |
| 656    | No file  | `228354c5913f`  |
| 652    | No file  | `228354c5913f`  |
| 643    | No file  | `228354c5913f`  |
| 637    | No file  | `228354c5913f`  |
| 630    | No file  | `228354c5913f`  |
| 627    | No file  | `228354c5913f`  |
| 621    | No file  | `228354c5913f`  |
| 617    | No file  | `228354c5913f`  |
| 615    | No file  | `228354c5913f`  |
| 606    | No file  | `228354c5913f`  |
| 599    | No file  | `228354c5913f`  |
| 592    | No file  | `228354c5913f`  |
| 586    | No file  | `228354c5913f`  |
| 577    | No file  | `228354c5913f`  |
| 569    | No file  | `228354c5913f`  |
| 561    | No file  | `228354c5913f`  |
| 554    | No file  | `228354c5913f`  |
| 542    | No file  | `228354c5913f`  |
| 532    | No file  | `228354c5913f`  |
| 531    | No file  | `228354c5913f`  |
| 526    | No file  | `228354c5913f`  |
| 521    | No file  | `228354c5913f`  |
| 517    | No file  | `228354c5913f`  |
| 510    | No file  | `228354c5913f`  |
| 508    | No file  | `228354c5913f`  |
| 504    | No file  | `228354c5913f`  |
| 497    | No file  | `228354c5913f`  |
| 491    | No file  | `228354c5913f`  |
| 485    | No file  | `228354c5913f`  |
| 478    | No file  | `228354c5913f`  |
| 472    | No file  | `228354c5913f`  |
| 466    | No file  | `228354c5913f`  |
| 457    | No file  | `228354c5913f`  |
| 452    | No file  | `228354c5913f`  |
| 449    | No file  | `228354c5913f`  |
| 435    | No file  | `228354c5913f`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                       |
| --------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `emoticonoffset.dbss` | Optional | `emoticon_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc` | Optional | Emoticon names and keywords: LOC type 60, `str_id1` = `emoticon_key`, `str_id4` `0` name, `1` keyword |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 54 bytes + paths, keyword and name)

| Offset               | Type  | Field              | Notes                                                                                                   |
| -------------------- | ----- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| `+0x00`              | u32   | emoticon_key       | Row key, `1` to `87` in file order on client 3482                                                       |
| `+0x04`              | u32   | unknown_04         | `0` on every row; the index rows carry it after the key too                                             |
| `+0x08`              | str16 | icon_path          | Icon under `ui_texture/`: `Combine/Sequence/Combine_Sequence_imojiMini_Papu.dds`; row `1` stores `Emoticon\Emoticon_Item.dds` with a backslash |
| `icon_path+0x00`     | u8    | icon_count         | Icons on the sheet: `18` on row `1`, `1` on every other row                                             |
| `icon_path+0x01`     | u32   | row_count          | Icon rows on the sheet: `5` on row `1`, `1` on every other row                                          |
| `icon_path+0x05`     | u32   | column_count       | Icon columns on the sheet: `5` on row `1`, `1` on every other row                                       |
| `icon_path+0x09`     | str16 | keyword_kr         | Korean chat keyword (`화남`); the chat inserts it as `(keyword)`. Row `1` stores the text `<NULL>`      |
| `keyword_kr+0x00`    | str16 | sequence_path      | Animated sequence sheet under `ui_texture/` (`Renewal/Sequence/PC_Sequence_imoji_Angry.dds`); row `1` stores `<NULL>` |
| `sequence_path+0x00` | u8    | group              | `0` on row `1`, `1` on every other row                                                                  |
| `sequence_path+0x01` | str16 | name_kr            | Korean name (`화난 흑정령`, Angry Black Spirit)                                                          |
| `name_kr+0x00`       | u32   | unknown_name_kr_00 | `0` on every row                                                                                        |

### `emoticonoffset.dbss`

Bare offset table into `emoticon.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                            |
| ------- | ----------------- | ----- | -------------------------------- |
| `+0x00` | u32               | count | Equals the `emoticon.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                   |

### Offset Row (16 bytes)

| Offset  | Type | Field        | Notes                                                        |
| ------- | ---- | ------------ | ------------------------------------------------------------ |
| `+0x00` | u32  | emoticon_key | Key of the row it points at                                  |
| `+0x04` | u32  | unknown_04   | `0` on every row, as the row's `unknown_04`                  |
| `+0x08` | u32  | data_offset  | Absolute offset of the row in `emoticon.dbss`, at `emoticon_key` |
| `+0x0C` | u32  | data_size    | The whole row, `unknown_name_kr_00` included                 |

The index rows are in file order; on clients 1784 and 3482 every index row
points at the row with its key.

## Field Names

The `Emoticon_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `key`, `name`, `RowCol`, `count`, `filepath`,
`sequenceFilePath`, `keyWord` and `group`, 16 rows. Every column matches
the file by value on the 16 shared keys, on client 1784 (16 rows) and on
client 3482 (87 rows). `RowCol` holds both grid sizes as `5,5`; row and
column order follows the column name.

| Field                     | Column             | Same value (client 1784) | Same value (client 3482) |
| ------------------------- | ------------------ | ------------------------ | ------------------------ |
| emoticon_key              | `key`              | 16 of 16                 | 16 of 16                 |
| icon_path                 | `filepath`         | 16 of 16                 | 16 of 16                 |
| icon_count                | `count`            | 16 of 16                 | 16 of 16                 |
| row_count, column_count   | `RowCol`           | 16 of 16                 | 16 of 16                 |
| keyword_kr                | `keyWord`          | 16 of 16                 | 16 of 16                 |
| sequence_path             | `sequenceFilePath` | 16 of 16                 | 16 of 16                 |
| group                     | `group`            | 16 of 16                 | 16 of 16                 |
| name_kr                   | `name`             | 16 of 16                 | 16 of 16                 |

## Notes

- LOC type 60 holds the English name (`str_id4` `0`, `Angry Black Spirit`)
  and keyword (`str_id4` `1`, `Angry`) of each emoticon by its key; key `1`
  has the name `Item Link` only.
- The item description of an emoticon item names the emoticon it registers
  (`- Curious Papu`, emoticon `14`), not its key.

## Open Questions

### What the Zero Fields Hold

`unknown_04` (after the key, in the row and the index row) and
`unknown_name_kr_00` (after the name) are `0` on every row of clients 1784
and 3482. The pair of key and `unknown_04` may be one 8-byte key; no Lua
getter or sheet column reads either field.

### What `group` Selects

`group` is `0` on the item link row and `1` on every emoticon, on clients
1784 and 3482; no Lua call reads it, so whether other values exist or what
they change is open.
