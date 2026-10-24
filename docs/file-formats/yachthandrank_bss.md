# `yachthandrank.bss` Format

## Purpose

The hand ranks (scoring combinations) of Yar!, the card and dice minigame
of [`yachtnpcdiceinfo.bss`](yachtnpcdiceinfo_bss.md). Each row is one hand
rank: which cards it checks (an eye value, a count of equal cards, a
straight length, two pair or full house), whether it scores a fixed number
of points or the sum of the matching cards, and its icon texture, Korean
name and Korean description. `yachtnpcdiceinfo.bss` and
[`yachtgameboardinfo.bss`](yachtgameboardinfo_bss.md) list hand ranks by
key, and [`yachtautobubbletextinfo.bss`](yachtautobubbletextinfo_bss.md)
keys some lines to one. The plain PABR file holds the rows, then the string
table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 1754 and later | 3483    | `yachthandrank.bss` | 2,951 | 15 Row  | 49        |

| Layout | File                | Known           | Unknown      |
| ------ | ------------------- | --------------- | ------------ |
| 1      | `yachthandrank.bss` | 2,696 B (91.4%) | 255 B (8.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `cef694324793`  |
| 3482   | Layout 1 | `cef694324793`  |
| 3474   | Layout 1 | `cef694324793`  |
| 3473   | Layout 1 | `cef694324793`  |
| 3464   | Layout 1 | `cef694324793`  |
| 3458   | Layout 1 | `cef694324793`  |
| 3454   | Layout 1 | `cef694324793`  |
| 3444   | Layout 1 | `cef694324793`  |
| 3435   | Layout 1 | `cef694324793`  |
| 3426   | Layout 1 | `cef694324793`  |
| 3418   | Layout 1 | `cef694324793`  |
| 3412   | Layout 1 | `cef694324793`  |
| 3402   | Layout 1 | `cef694324793`  |
| 3396   | Layout 1 | `cef694324793`  |
| 3387   | Layout 1 | `cef694324793`  |
| 3381   | Layout 1 | `cef694324793`  |
| 3373   | Layout 1 | `cef694324793`  |
| 3364   | Layout 1 | `cef694324793`  |
| 3356   | Layout 1 | `cef694324793`  |
| 3349   | Layout 1 | `cef694324793`  |
| 3342   | Layout 1 | `cef694324793`  |
| 3335   | Layout 1 | `cef694324793`  |
| 3326   | Layout 1 | `cef694324793`  |
| 3321   | Layout 1 | `cef694324793`  |
| 3314   | Layout 1 | `cef694324793`  |
| 3303   | Layout 1 | `cef694324793`  |
| 3302   | Layout 1 | `cef694324793`  |
| 3293   | Layout 1 | `cef694324793`  |
| 3283   | Layout 1 | `cef694324793`  |
| 3275   | Layout 1 | `cef694324793`  |
| 3267   | Layout 1 | `cef694324793`  |
| 3258   | Layout 1 | `cef694324793`  |
| 3251   | Layout 1 | `cef694324793`  |
| 3242   | Layout 1 | `cef694324793`  |
| 3235   | Layout 1 | `cef694324793`  |
| 3229   | Layout 1 | `cef694324793`  |
| 3212   | Layout 1 | `cef694324793`  |
| 3203   | Layout 1 | `cef694324793`  |
| 3193   | Layout 1 | `cef694324793`  |
| 3186   | Layout 1 | `cef694324793`  |
| 3177   | Layout 1 | `cef694324793`  |
| 3169   | Layout 1 | `cef694324793`  |
| 3158   | Layout 1 | `cef694324793`  |
| 3151   | Layout 1 | `cef694324793`  |
| 3144   | Layout 1 | `cef694324793`  |
| 3133   | Layout 1 | `cef694324793`  |
| 3125   | Layout 1 | `cef694324793`  |
| 3118   | Layout 1 | `cef694324793`  |
| 3111   | Layout 1 | `cef694324793`  |
| 3103   | Layout 1 | `cef694324793`  |
| 3095   | Layout 1 | `cef694324793`  |
| 3086   | Layout 1 | `cef694324793`  |
| 3072   | Layout 1 | `cef694324793`  |
| 3062   | Layout 1 | `cef694324793`  |
| 3052   | Layout 1 | `cef694324793`  |
| 3045   | Layout 1 | `cef694324793`  |
| 3037   | Layout 1 | `cef694324793`  |
| 3030   | Layout 1 | `cef694324793`  |
| 3021   | Layout 1 | `cef694324793`  |
| 3012   | Layout 1 | `cef694324793`  |
| 3002   | Layout 1 | `cef694324793`  |
| 2995   | Layout 1 | `cef694324793`  |
| 2987   | Layout 1 | `cef694324793`  |
| 2978   | Layout 1 | `cef694324793`  |
| 2970   | Layout 1 | `cef694324793`  |
| 2959   | Layout 1 | `cef694324793`  |
| 2951   | Layout 1 | `cef694324793`  |
| 2942   | Layout 1 | `cef694324793`  |
| 2935   | Layout 1 | `cef694324793`  |
| 2932   | Layout 1 | `cef694324793`  |
| 2923   | Layout 1 | `cef694324793`  |
| 2919   | Layout 1 | `cef694324793`  |
| 2907   | Layout 1 | `cef694324793`  |
| 2900   | Layout 1 | `cef694324793`  |
| 2891   | Layout 1 | `cef694324793`  |
| 2882   | Layout 1 | `cef694324793`  |
| 2872   | Layout 1 | `cef694324793`  |
| 2863   | Layout 1 | `cef694324793`  |
| 2855   | Layout 1 | `cef694324793`  |
| 2849   | Layout 1 | `cef694324793`  |
| 2844   | Layout 1 | `cef694324793`  |
| 2834   | Layout 1 | `cef694324793`  |
| 2825   | Layout 1 | `cef694324793`  |
| 2819   | Layout 1 | `cef694324793`  |
| 2811   | Layout 1 | `cef694324793`  |
| 2803   | Layout 1 | `cef694324793`  |
| 2794   | Layout 1 | `cef694324793`  |
| 2783   | Layout 1 | `cef694324793`  |
| 2774   | Layout 1 | `cef694324793`  |
| 2765   | Layout 1 | `cef694324793`  |
| 2756   | Layout 1 | `cef694324793`  |
| 2750   | Layout 1 | `cef694324793`  |
| 2743   | Layout 1 | `cef694324793`  |
| 2736   | Layout 1 | `cef694324793`  |
| 2726   | Layout 1 | `cef694324793`  |
| 2717   | Layout 1 | `cef694324793`  |
| 2709   | Layout 1 | `cef694324793`  |
| 2703   | Layout 1 | `cef694324793`  |
| 2695   | Layout 1 | `cef694324793`  |
| 2684   | Layout 1 | `cef694324793`  |
| 2672   | Layout 1 | `cef694324793`  |
| 2665   | Layout 1 | `cef694324793`  |
| 2657   | Layout 1 | `cef694324793`  |
| 2649   | Layout 1 | `cef694324793`  |
| 2644   | Layout 1 | `cef694324793`  |
| 2637   | Layout 1 | `cef694324793`  |
| 2629   | Layout 1 | `cef694324793`  |
| 2619   | Layout 1 | `cef694324793`  |
| 2612   | Layout 1 | `cef694324793`  |
| 2606   | Layout 1 | `cef694324793`  |
| 2602   | Layout 1 | `cef694324793`  |
| 2601   | Layout 1 | `cef694324793`  |
| 2592   | Layout 1 | `cef694324793`  |
| 2583   | Layout 1 | `cef694324793`  |
| 2575   | Layout 1 | `cef694324793`  |
| 2567   | Layout 1 | `cef694324793`  |
| 2560   | Layout 1 | `cef694324793`  |
| 2553   | Layout 1 | `cef694324793`  |
| 2545   | Layout 1 | `cef694324793`  |
| 2538   | Layout 1 | `cef694324793`  |
| 2529   | Layout 1 | `cef694324793`  |
| 2519   | Layout 1 | `cef694324793`  |
| 2513   | Layout 1 | `cef694324793`  |
| 2510   | Layout 1 | `cef694324793`  |
| 2507   | Layout 1 | `cef694324793`  |
| 2503   | Layout 1 | `cef694324793`  |
| 2498   | Layout 1 | `cef694324793`  |
| 2492   | Layout 1 | `cef694324793`  |
| 2487   | Layout 1 | `cef694324793`  |
| 2480   | Layout 1 | `cef694324793`  |
| 2474   | Layout 1 | `cef694324793`  |
| 2468   | Layout 1 | `cef694324793`  |
| 2460   | Layout 1 | `cef694324793`  |
| 2453   | Layout 1 | `cef694324793`  |
| 2444   | Layout 1 | `cef694324793`  |
| 2438   | Layout 1 | `cef694324793`  |
| 2434   | Layout 1 | `cef694324793`  |
| 2429   | Layout 1 | `cef694324793`  |
| 2421   | Layout 1 | `cef694324793`  |
| 2414   | Layout 1 | `cef694324793`  |
| 2407   | Layout 1 | `cef694324793`  |
| 2401   | Layout 1 | `cef694324793`  |
| 2397   | Layout 1 | `cef694324793`  |
| 2393   | Layout 1 | `cef694324793`  |
| 2384   | Layout 1 | `cef694324793`  |
| 2378   | Layout 1 | `cef694324793`  |
| 2372   | Layout 1 | `cef694324793`  |
| 2358   | Layout 1 | `cef694324793`  |
| 2352   | Layout 1 | `cef694324793`  |
| 2347   | Layout 1 | `cef694324793`  |
| 2343   | Layout 1 | `cef694324793`  |
| 2335   | Layout 1 | `cef694324793`  |
| 2327   | Layout 1 | `cef694324793`  |
| 2324   | Layout 1 | `cef694324793`  |
| 2319   | Layout 1 | `cef694324793`  |
| 2313   | Layout 1 | `cef694324793`  |
| 2308   | Layout 1 | `cef694324793`  |
| 2302   | Layout 1 | `cef694324793`  |
| 2295   | Layout 1 | `cef694324793`  |
| 2290   | Layout 1 | `cef694324793`  |
| 2284   | Layout 1 | `cef694324793`  |
| 2276   | Layout 1 | `cef694324793`  |
| 2269   | Layout 1 | `cef694324793`  |
| 2259   | Layout 1 | `cef694324793`  |
| 2250   | Layout 1 | `cef694324793`  |
| 2243   | Layout 1 | `cef694324793`  |
| 2235   | Layout 1 | `cef694324793`  |
| 2229   | Layout 1 | `cef694324793`  |
| 2224   | Layout 1 | `cef694324793`  |
| 2218   | Layout 1 | `cef694324793`  |
| 2215   | Layout 1 | `cef694324793`  |
| 2207   | Layout 1 | `cef694324793`  |
| 2203   | Layout 1 | `cef694324793`  |
| 2196   | Layout 1 | `cef694324793`  |
| 2192   | Layout 1 | `cef694324793`  |
| 2189   | Layout 1 | `cef694324793`  |
| 2183   | Layout 1 | `cef694324793`  |
| 2179   | Layout 1 | `cef694324793`  |
| 2171   | Layout 1 | `cef694324793`  |
| 2163   | Layout 1 | `cef694324793`  |
| 2156   | Layout 1 | `cef694324793`  |
| 2151   | Layout 1 | `cef694324793`  |
| 2147   | Layout 1 | `cef694324793`  |
| 2142   | Layout 1 | `cef694324793`  |
| 2138   | Layout 1 | `cef694324793`  |
| 2134   | Layout 1 | `cef694324793`  |
| 2130   | Layout 1 | `cef694324793`  |
| 2122   | Layout 1 | `cef694324793`  |
| 2107   | Layout 1 | `cef694324793`  |
| 2098   | Layout 1 | `cef694324793`  |
| 2089   | Layout 1 | `cef694324793`  |
| 2081   | Layout 1 | `cef694324793`  |
| 2073   | Layout 1 | `cef694324793`  |
| 2067   | Layout 1 | `cef694324793`  |
| 2063   | Layout 1 | `cef694324793`  |
| 2059   | Layout 1 | `cef694324793`  |
| 2052   | Layout 1 | `cef694324793`  |
| 2044   | Layout 1 | `cef694324793`  |
| 2039   | Layout 1 | `cef694324793`  |
| 2032   | Layout 1 | `cef694324793`  |
| 2025   | Layout 1 | `cef694324793`  |
| 2011   | Layout 1 | `cef694324793`  |
| 2005   | Layout 1 | `cef694324793`  |
| 2000   | Layout 1 | `cef694324793`  |
| 1996   | Layout 1 | `cef694324793`  |
| 1991   | Layout 1 | `cef694324793`  |
| 1985   | Layout 1 | `cef694324793`  |
| 1980   | Layout 1 | `cef694324793`  |
| 1969   | Layout 1 | `cef694324793`  |
| 1964   | Layout 1 | `cef694324793`  |
| 1958   | Layout 1 | `cef694324793`  |
| 1950   | Layout 1 | `cef694324793`  |
| 1945   | Layout 1 | `cef694324793`  |
| 1937   | Layout 1 | `cef694324793`  |
| 1933   | Layout 1 | `cef694324793`  |
| 1927   | Layout 1 | `cef694324793`  |
| 1921   | Layout 1 | `cef694324793`  |
| 1914   | Layout 1 | `cef694324793`  |
| 1908   | Layout 1 | `cef694324793`  |
| 1897   | Layout 1 | `cef694324793`  |
| 1892   | Layout 1 | `cef694324793`  |
| 1886   | Layout 1 | `cef694324793`  |
| 1881   | Layout 1 | `cef694324793`  |
| 1871   | Layout 1 | `cef694324793`  |
| 1866   | Layout 1 | `cef694324793`  |
| 1862   | Layout 1 | `cef694324793`  |
| 1854   | Layout 1 | `cef694324793`  |
| 1846   | Layout 1 | `cef694324793`  |
| 1838   | Layout 1 | `cef694324793`  |
| 1832   | Layout 1 | `cef694324793`  |
| 1826   | Layout 1 | `cef694324793`  |
| 1822   | Layout 1 | `cef694324793`  |
| 1818   | Layout 1 | `cef694324793`  |
| 1804   | Layout 1 | `cef694324793`  |
| 1794   | Layout 1 | `cef694324793`  |
| 1790   | Layout 1 | `cef694324793`  |
| 1784   | Layout 1 | `cef694324793`  |
| 1774   | Layout 1 | `cef694324793`  |
| 1771   | Layout 1 | `cef694324793`  |
| 1762   | Layout 1 | `cef694324793`  |
| 1759   | Layout 1 | `cef694324793`  |
| 1754   | Layout 1 | `cef694324793`  |
| 1749   | No file  | `cef694324793`  |
| 1743   | No file  | `cef694324793`  |
| 1737   | No file  | `cef694324793`  |
| 1731   | No file  | `cef694324793`  |
| 1725   | No file  | `cef694324793`  |
| 1717   | No file  | `cef694324793`  |
| 1710   | No file  | `cef694324793`  |
| 1704   | No file  | `cef694324793`  |
| 1698   | No file  | `cef694324793`  |
| 1690   | No file  | `cef694324793`  |
| 1685   | No file  | `cef694324793`  |
| 1680   | No file  | `cef694324793`  |
| 1674   | No file  | `cef694324793`  |
| 1668   | No file  | `cef694324793`  |
| 1659   | No file  | `cef694324793`  |
| 1649   | No file  | `cef694324793`  |
| 1642   | No file  | `cef694324793`  |
| 1636   | No file  | `cef694324793`  |
| 1628   | No file  | `cef694324793`  |
| 1622   | No file  | `cef694324793`  |
| 1614   | No file  | `cef694324793`  |
| 1608   | No file  | `cef694324793`  |
| 1602   | No file  | `cef694324793`  |
| 1598   | No file  | `cef694324793`  |
| 1594   | No file  | `cef694324793`  |
| 1590   | No file  | `cef694324793`  |
| 1587   | No file  | `cef694324793`  |
| 1584   | No file  | `cef694324793`  |
| 1579   | No file  | `cef694324793`  |
| 1572   | No file  | `cef694324793`  |
| 1565   | No file  | `cef694324793`  |
| 1559   | No file  | `cef694324793`  |
| 1554   | No file  | `cef694324793`  |
| 1547   | No file  | `cef694324793`  |
| 1537   | No file  | `cef694324793`  |
| 1529   | No file  | `cef694324793`  |
| 1524   | No file  | `cef694324793`  |
| 1519   | No file  | `cef694324793`  |
| 1509   | No file  | `cef694324793`  |
| 1506   | No file  | `cef694324793`  |
| 1504   | No file  | `cef694324793`  |
| 1500   | No file  | `cef694324793`  |
| 1493   | No file  | `cef694324793`  |
| 1489   | No file  | `cef694324793`  |
| 1485   | No file  | `cef694324793`  |
| 1481   | No file  | `cef694324793`  |
| 1474   | No file  | `cef694324793`  |
| 1466   | No file  | `cef694324793`  |
| 1462   | No file  | `cef694324793`  |
| 1459   | No file  | `cef694324793`  |
| 1453   | No file  | `cef694324793`  |
| 1450   | No file  | `cef694324793`  |
| 1445   | No file  | `cef694324793`  |
| 1439   | No file  | `cef694324793`  |
| 1433   | No file  | `cef694324793`  |
| 1430   | No file  | `cef694324793`  |
| 1426   | No file  | `cef694324793`  |
| 1421   | No file  | `cef694324793`  |
| 1417   | No file  | `cef694324793`  |
| 1416   | No file  | `cef694324793`  |
| 1409   | No file  | `cef694324793`  |
| 1405   | No file  | `cef694324793`  |
| 1401   | No file  | `cef694324793`  |
| 1396   | No file  | `cef694324793`  |
| 1391   | No file  | `cef694324793`  |
| 1390   | No file  | `cef694324793`  |
| 1386   | No file  | `cef694324793`  |
| 1381   | No file  | `cef694324793`  |
| 1379   | No file  | `cef694324793`  |
| 1372   | No file  | `cef694324793`  |
| 1366   | No file  | `cef694324793`  |
| 1364   | No file  | `cef694324793`  |
| 1363   | No file  | `cef694324793`  |
| 1360   | No file  | `cef694324793`  |
| 1358   | No file  | `cef694324793`  |
| 1355   | No file  | `cef694324793`  |
| 1351   | No file  | `cef694324793`  |
| 1348   | No file  | `cef694324793`  |
| 1346   | No file  | `cef694324793`  |
| 1341   | No file  | `cef694324793`  |
| 1340   | No file  | `cef694324793`  |
| 1338   | No file  | `cef694324793`  |
| 1335   | No file  | `cef694324793`  |
| 1333   | No file  | `cef694324793`  |
| 1329   | No file  | `cef694324793`  |
| 1327   | No file  | `cef694324793`  |
| 1324   | No file  | `cef694324793`  |
| 1321   | No file  | `cef694324793`  |
| 1319   | No file  | `cef694324793`  |
| 1318   | No file  | `cef694324793`  |
| 1316   | No file  | `cef694324793`  |
| 1313   | No file  | `cef694324793`  |
| 1311   | No file  | `cef694324793`  |
| 1309   | No file  | `cef694324793`  |
| 1304   | No file  | `cef694324793`  |
| 1292   | No file  | `cef694324793`  |
| 1286   | No file  | `cef694324793`  |
| 1280   | No file  | `cef694324793`  |
| 1276   | No file  | `cef694324793`  |
| 1267   | No file  | `cef694324793`  |
| 1261   | No file  | `cef694324793`  |
| 1256   | No file  | `cef694324793`  |
| 1250   | No file  | `cef694324793`  |
| 1246   | No file  | `cef694324793`  |
| 1239   | No file  | `cef694324793`  |
| 1230   | No file  | `cef694324793`  |
| 1226   | No file  | `cef694324793`  |
| 1220   | No file  | `cef694324793`  |
| 1217   | No file  | `cef694324793`  |
| 1211   | No file  | `cef694324793`  |
| 1210   | No file  | `cef694324793`  |
| 1208   | No file  | `cef694324793`  |
| 1203   | No file  | `cef694324793`  |
| 1197   | No file  | `cef694324793`  |
| 1194   | No file  | `cef694324793`  |
| 1192   | No file  | `cef694324793`  |
| 1187   | No file  | `cef694324793`  |
| 1183   | No file  | `cef694324793`  |
| 1177   | No file  | `cef694324793`  |
| 1173   | No file  | `cef694324793`  |
| 1167   | No file  | `cef694324793`  |
| 1164   | No file  | `cef694324793`  |
| 1156   | No file  | `cef694324793`  |
| 1149   | No file  | `cef694324793`  |
| 1144   | No file  | `cef694324793`  |
| 1137   | No file  | `cef694324793`  |
| 1132   | No file  | `cef694324793`  |
| 1127   | No file  | `cef694324793`  |
| 1122   | No file  | `cef694324793`  |
| 1118   | No file  | `cef694324793`  |
| 1114   | No file  | `cef694324793`  |
| 1109   | No file  | `cef694324793`  |
| 1102   | No file  | `cef694324793`  |
| 1096   | No file  | `cef694324793`  |
| 1088   | No file  | `cef694324793`  |
| 1081   | No file  | `cef694324793`  |
| 1076   | No file  | `cef694324793`  |
| 1069   | No file  | `cef694324793`  |
| 1064   | No file  | `cef694324793`  |
| 1058   | No file  | `cef694324793`  |
| 1051   | No file  | `cef694324793`  |
| 1044   | No file  | `cef694324793`  |
| 1036   | No file  | `cef694324793`  |
| 1026   | No file  | `cef694324793`  |
| 1016   | No file  | `cef694324793`  |
| 1009   | No file  | `cef694324793`  |
| 1005   | No file  | `cef694324793`  |
| 1000   | No file  | `cef694324793`  |
| 998    | No file  | `cef694324793`  |
| 990    | No file  | `cef694324793`  |
| 979    | No file  | `cef694324793`  |
| 972    | No file  | `cef694324793`  |
| 963    | No file  | `cef694324793`  |
| 955    | No file  | `cef694324793`  |
| 946    | No file  | `cef694324793`  |
| 938    | No file  | `cef694324793`  |
| 927    | No file  | `cef694324793`  |
| 911    | No file  | `cef694324793`  |
| 904    | No file  | `cef694324793`  |
| 899    | No file  | `cef694324793`  |
| 894    | No file  | `cef694324793`  |
| 885    | No file  | `cef694324793`  |
| 879    | No file  | `cef694324793`  |
| 872    | No file  | `cef694324793`  |
| 864    | No file  | `cef694324793`  |
| 855    | No file  | `cef694324793`  |
| 853    | No file  | `cef694324793`  |
| 845    | No file  | `cef694324793`  |
| 837    | No file  | `cef694324793`  |
| 829    | No file  | `cef694324793`  |
| 822    | No file  | `cef694324793`  |
| 814    | No file  | `cef694324793`  |
| 805    | No file  | `cef694324793`  |
| 794    | No file  | `cef694324793`  |
| 787    | No file  | `cef694324793`  |
| 780    | No file  | `cef694324793`  |
| 771    | No file  | `cef694324793`  |
| 760    | No file  | `cef694324793`  |
| 748    | No file  | `cef694324793`  |
| 741    | No file  | `cef694324793`  |
| 736    | No file  | `cef694324793`  |
| 731    | No file  | `cef694324793`  |
| 723    | No file  | `cef694324793`  |
| 711    | No file  | `cef694324793`  |
| 707    | No file  | `cef694324793`  |
| 697    | No file  | `cef694324793`  |
| 689    | No file  | `cef694324793`  |
| 683    | No file  | `cef694324793`  |
| 678    | No file  | `cef694324793`  |
| 670    | No file  | `cef694324793`  |
| 661    | No file  | `cef694324793`  |
| 656    | No file  | `cef694324793`  |
| 652    | No file  | `cef694324793`  |
| 643    | No file  | `cef694324793`  |
| 637    | No file  | `cef694324793`  |
| 630    | No file  | `cef694324793`  |
| 627    | No file  | `cef694324793`  |
| 621    | No file  | `cef694324793`  |
| 617    | No file  | `cef694324793`  |
| 615    | No file  | `cef694324793`  |
| 606    | No file  | `cef694324793`  |
| 599    | No file  | `cef694324793`  |
| 592    | No file  | `cef694324793`  |
| 586    | No file  | `cef694324793`  |
| 577    | No file  | `cef694324793`  |
| 569    | No file  | `cef694324793`  |
| 561    | No file  | `cef694324793`  |
| 554    | No file  | `cef694324793`  |
| 542    | No file  | `cef694324793`  |
| 532    | No file  | `cef694324793`  |
| 531    | No file  | `cef694324793`  |
| 526    | No file  | `cef694324793`  |
| 521    | No file  | `cef694324793`  |
| 517    | No file  | `cef694324793`  |
| 510    | No file  | `cef694324793`  |
| 508    | No file  | `cef694324793`  |
| 504    | No file  | `cef694324793`  |
| 497    | No file  | `cef694324793`  |
| 491    | No file  | `cef694324793`  |
| 485    | No file  | `cef694324793`  |
| 478    | No file  | `cef694324793`  |
| 472    | No file  | `cef694324793`  |
| 466    | No file  | `cef694324793`  |
| 457    | No file  | `cef694324793`  |
| 452    | No file  | `cef694324793`  |
| 449    | No file  | `cef694324793`  |
| 435    | No file  | `cef694324793`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                               |
| --------------------- | -------- | -------------------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Hand rank names (LOC type 105, `str_id1=hand_rank_key`, `str_id4=0`) and descriptions (`str_id4=1`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                        |
| ------------------- | ------------ | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32          | count              | Number of rows                               |
| `+0x08`             | Row[count]   | rows               | Fixed-size rows, back to back; see Row       |
| `rows+0x00`         | String Table | string_table       | See String Table                             |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end |
| `string_table+0x04` | u32          | zero               | Always `0`                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). `count` rows of 49 bytes end exactly at
`string_table_start`.

### Row (49 bytes)

| Offset  | Type     | Field              | Notes                                                                      |
| ------- | -------- | ------------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32      | hand_rank_key      | Unique row key, LOC type 105 `str_id1`                                     |
| `+0x04` | bytes[9] | unknown_04         | `0` on every row (clients 1784 and 3474)                                   |
| `+0x0D` | u32      | unknown_0d         | `1` on every row (clients 1784 and 3474)                                   |
| `+0x11` | bytes[4] | unknown_11         | `0` on every row (clients 1784 and 3474)                                   |
| `+0x15` | u8       | target_eye         | Eye value the hand counts (`1` to `6`); `0` checks no eye                  |
| `+0x16` | u32      | target_count       | Number of equal cards the hand needs (`2` to `5`); `0` for none            |
| `+0x1A` | u32      | straight_count     | Length of the straight the hand needs (`4` or `5`); `0` for none           |
| `+0x1E` | u8       | is_full_house      | `1` on the full house hand (key 11)                                        |
| `+0x1F` | u8       | is_two_pair        | `1` on the two pair hand (key 10)                                          |
| `+0x20` | u32      | made_point         | Fixed points the hand scores; `0` when it scores the card sum              |
| `+0x24` | u8       | is_sum_point       | `1` when the hand scores the sum of its cards                              |
| `+0x25` | u32      | icon_texture_index | String table index of the icon's texture ID (`Combine_Etc_Minigame_Yatzee_Icon_Ones`) |
| `+0x29` | u32      | name_kr_index      | String table index of the Korean name                                      |
| `+0x2D` | u32      | desc_kr_index      | String table index of the Korean description                               |

No field is padded, so the u32 fields after `target_eye` are not 4-byte
aligned.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; three per row (45 on client 3474)     |
| `+0x04` | pstr[string_count] | strings      | Per row its icon texture ID (UTF-8), name and description (UTF-16) |

## Hand Ranks

On client 3474 the file holds 15 rows. Names are the LOC type 105 English text.

| Key | Name           | Checks                         | Points       |
| --- | -------------- | ------------------------------ | ------------ |
| 1   | Bit o' Ones    | Eye 1                          | Sum          |
| 2   | Bunch o' Twos  | Eye 2                          | Sum          |
| 3   | Lump o' Threes | Eye 3                          | Sum          |
| 4   | Nest o' Fours  | Eye 4                          | Sum          |
| 5   | Clump o' Fives | Eye 5                          | Sum          |
| 6   | Stack o' Sixes | Eye 6                          | Sum          |
| 7   | Mates          | 2 equal cards                  | Sum          |
| 8   | Peak           | 3 equal cards                  | Sum          |
| 9   | Dragon Claw    | 4 equal cards                  | Sum          |
| 10  | Double Trouble | Two pair                       | 15           |
| 11  | Den of Wolves  | Full house                     | 25           |
| 12  | Yar!           | 5 equal cards                  | 50           |
| 13  | Broken Arrow   | Straight of 4                  | 30           |
| 14  | Straight Shot  | Straight of 5                  | 40           |
| 15  | Chance         | None                           | Sum          |

On every row exactly one of `made_point` and `is_sum_point` is set.

## Field Names

The `HandRanking` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `HandRankKey` (`hand_rank_key`), `HandType`,
`TargetSymbol`, `TargetEye` (`target_eye`), `IsTwoPair` (`is_two_pair`),
`IsFullHouse` (`is_full_house`), `TargetCount` (`target_count`),
`StraightCount` (`straight_count`), `MadePoint` (`made_point`), `SumPoint`
(`is_sum_point`), `UI_Texture`, `~Name` and `~Desc`. Its 15 rows match the
15 rows of clients 1784 and 3474 in every named column and string, with
`<null>` stored as `0`; the file writes `IsFullHouse` before `IsTwoPair`.
The two files are byte for byte the same. The client Lua reads the strings
through `getIconTextureName()`, `getName()` and `getDesc()` on
`ToClient_getHandRankStaticStatusWrapper(key)`
(`panel_window_minigame_yachtdice_invite_1.luac`).

The `#참조` sheet of the same workbook notes the values: `HandType` `0`
checks the eye only, `1` the symbol only, `2` both; `TargetSymbol` is a
card symbol (`1` to `4`, see [`yachtbasecard.dbss`](yachtbasecard_dbss.md)).
Both are `0` or `<null>` on every sheet row, so the data cannot tell which
bytes of `unknown_04` to `unknown_11` hold them.

## Notes

- The LOC type 105 descriptions (`str_id4=1`) follow the Korean ones:
  "Gain the sum of all 1s in points.", "Two pairs. Gain 15 points."

## Open Questions

### Where `HandType` and `TargetSymbol` Sit

The sheet has two columns the named fields do not cover, `HandType` and
`TargetSymbol`, both `0` on every row, and the row has 17 bytes from `+0x04`
to `+0x14` that the named fields do not cover: 13 zero bytes and the u32
`unknown_0d`, `1` on every row. A hand rank with a symbol check would show
which bytes they are; no client has one. `unknown_0d` matches no sheet
column.
