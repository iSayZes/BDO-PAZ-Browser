# `rosewarinfo.bss` Format

## Purpose

The two colours of the Rose War region map
(`ui_texture/minimap/area/elfwar_siegemap.bmp`; the Rose War is `ElfWar` in
the client's file names), one 9-byte row each. A u32 count follows the PABR
magic. Each row has the shape of an
[`edaniaregioninfo.bss`](edaniaregioninfo_bss.md) row: the colour and a
zero byte twice, then a u8. On client 3474 the rows are `10 0D 10` with `0`
and `E8 1B 18` with `1`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------- | ----- | ------- | --------- |
| 1      | 2612 and later | 3483    | `rosewarinfo.bss` | 38    | 2 Row   | 9         |

| Layout | File              | Known        | Unknown      |
| ------ | ----------------- | ------------ | ------------ |
| 1      | `rosewarinfo.bss` | 26 B (68.4%) | 12 B (31.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `384a14af8529`  |
| 3482   | Layout 1 | `384a14af8529`  |
| 3474   | Layout 1 | `384a14af8529`  |
| 3473   | Layout 1 | `384a14af8529`  |
| 3464   | Layout 1 | `384a14af8529`  |
| 3458   | Layout 1 | `384a14af8529`  |
| 3454   | Layout 1 | `384a14af8529`  |
| 3444   | Layout 1 | `384a14af8529`  |
| 3435   | Layout 1 | `384a14af8529`  |
| 3426   | Layout 1 | `384a14af8529`  |
| 3418   | Layout 1 | `384a14af8529`  |
| 3412   | Layout 1 | `384a14af8529`  |
| 3402   | Layout 1 | `384a14af8529`  |
| 3396   | Layout 1 | `384a14af8529`  |
| 3387   | Layout 1 | `384a14af8529`  |
| 3381   | Layout 1 | `384a14af8529`  |
| 3373   | Layout 1 | `384a14af8529`  |
| 3364   | Layout 1 | `384a14af8529`  |
| 3356   | Layout 1 | `384a14af8529`  |
| 3349   | Layout 1 | `384a14af8529`  |
| 3342   | Layout 1 | `384a14af8529`  |
| 3335   | Layout 1 | `384a14af8529`  |
| 3326   | Layout 1 | `384a14af8529`  |
| 3321   | Layout 1 | `384a14af8529`  |
| 3314   | Layout 1 | `384a14af8529`  |
| 3303   | Layout 1 | `384a14af8529`  |
| 3302   | Layout 1 | `384a14af8529`  |
| 3293   | Layout 1 | `384a14af8529`  |
| 3283   | Layout 1 | `384a14af8529`  |
| 3275   | Layout 1 | `384a14af8529`  |
| 3267   | Layout 1 | `384a14af8529`  |
| 3258   | Layout 1 | `384a14af8529`  |
| 3251   | Layout 1 | `384a14af8529`  |
| 3242   | Layout 1 | `384a14af8529`  |
| 3235   | Layout 1 | `384a14af8529`  |
| 3229   | Layout 1 | `384a14af8529`  |
| 3212   | Layout 1 | `384a14af8529`  |
| 3203   | Layout 1 | `384a14af8529`  |
| 3193   | Layout 1 | `384a14af8529`  |
| 3186   | Layout 1 | `384a14af8529`  |
| 3177   | Layout 1 | `384a14af8529`  |
| 3169   | Layout 1 | `384a14af8529`  |
| 3158   | Layout 1 | `384a14af8529`  |
| 3151   | Layout 1 | `384a14af8529`  |
| 3144   | Layout 1 | `384a14af8529`  |
| 3133   | Layout 1 | `384a14af8529`  |
| 3125   | Layout 1 | `384a14af8529`  |
| 3118   | Layout 1 | `384a14af8529`  |
| 3111   | Layout 1 | `384a14af8529`  |
| 3103   | Layout 1 | `384a14af8529`  |
| 3095   | Layout 1 | `384a14af8529`  |
| 3086   | Layout 1 | `384a14af8529`  |
| 3072   | Layout 1 | `384a14af8529`  |
| 3062   | Layout 1 | `384a14af8529`  |
| 3052   | Layout 1 | `384a14af8529`  |
| 3045   | Layout 1 | `384a14af8529`  |
| 3037   | Layout 1 | `384a14af8529`  |
| 3030   | Layout 1 | `384a14af8529`  |
| 3021   | Layout 1 | `384a14af8529`  |
| 3012   | Layout 1 | `384a14af8529`  |
| 3002   | Layout 1 | `384a14af8529`  |
| 2995   | Layout 1 | `384a14af8529`  |
| 2987   | Layout 1 | `384a14af8529`  |
| 2978   | Layout 1 | `384a14af8529`  |
| 2970   | Layout 1 | `384a14af8529`  |
| 2959   | Layout 1 | `384a14af8529`  |
| 2951   | Layout 1 | `384a14af8529`  |
| 2942   | Layout 1 | `384a14af8529`  |
| 2935   | Layout 1 | `384a14af8529`  |
| 2932   | Layout 1 | `384a14af8529`  |
| 2923   | Layout 1 | `384a14af8529`  |
| 2919   | Layout 1 | `384a14af8529`  |
| 2907   | Layout 1 | `384a14af8529`  |
| 2900   | Layout 1 | `384a14af8529`  |
| 2891   | Layout 1 | `384a14af8529`  |
| 2882   | Layout 1 | `384a14af8529`  |
| 2872   | Layout 1 | `384a14af8529`  |
| 2863   | Layout 1 | `384a14af8529`  |
| 2855   | Layout 1 | `384a14af8529`  |
| 2849   | Layout 1 | `384a14af8529`  |
| 2844   | Layout 1 | `384a14af8529`  |
| 2834   | Layout 1 | `384a14af8529`  |
| 2825   | Layout 1 | `384a14af8529`  |
| 2819   | Layout 1 | `384a14af8529`  |
| 2811   | Layout 1 | `384a14af8529`  |
| 2803   | Layout 1 | `384a14af8529`  |
| 2794   | Layout 1 | `384a14af8529`  |
| 2783   | Layout 1 | `384a14af8529`  |
| 2774   | Layout 1 | `384a14af8529`  |
| 2765   | Layout 1 | `384a14af8529`  |
| 2756   | Layout 1 | `384a14af8529`  |
| 2750   | Layout 1 | `384a14af8529`  |
| 2743   | Layout 1 | `384a14af8529`  |
| 2736   | Layout 1 | `384a14af8529`  |
| 2726   | Layout 1 | `384a14af8529`  |
| 2717   | Layout 1 | `384a14af8529`  |
| 2709   | Layout 1 | `384a14af8529`  |
| 2703   | Layout 1 | `384a14af8529`  |
| 2695   | Layout 1 | `384a14af8529`  |
| 2684   | Layout 1 | `384a14af8529`  |
| 2672   | Layout 1 | `384a14af8529`  |
| 2665   | Layout 1 | `384a14af8529`  |
| 2657   | Layout 1 | `384a14af8529`  |
| 2649   | Layout 1 | `384a14af8529`  |
| 2644   | Layout 1 | `384a14af8529`  |
| 2637   | Layout 1 | `384a14af8529`  |
| 2629   | Layout 1 | `384a14af8529`  |
| 2619   | Layout 1 | `384a14af8529`  |
| 2612   | Layout 1 | `384a14af8529`  |
| 2606   | No file  | `384a14af8529`  |
| 2602   | No file  | `384a14af8529`  |
| 2601   | No file  | `384a14af8529`  |
| 2592   | No file  | `384a14af8529`  |
| 2583   | No file  | `384a14af8529`  |
| 2575   | No file  | `384a14af8529`  |
| 2567   | No file  | `384a14af8529`  |
| 2560   | No file  | `384a14af8529`  |
| 2553   | No file  | `384a14af8529`  |
| 2545   | No file  | `384a14af8529`  |
| 2538   | No file  | `384a14af8529`  |
| 2529   | No file  | `384a14af8529`  |
| 2519   | No file  | `384a14af8529`  |
| 2513   | No file  | `384a14af8529`  |
| 2510   | No file  | `384a14af8529`  |
| 2507   | No file  | `384a14af8529`  |
| 2503   | No file  | `384a14af8529`  |
| 2498   | No file  | `384a14af8529`  |
| 2492   | No file  | `384a14af8529`  |
| 2487   | No file  | `384a14af8529`  |
| 2480   | No file  | `384a14af8529`  |
| 2474   | No file  | `384a14af8529`  |
| 2468   | No file  | `384a14af8529`  |
| 2460   | No file  | `384a14af8529`  |
| 2453   | No file  | `384a14af8529`  |
| 2444   | No file  | `384a14af8529`  |
| 2438   | No file  | `384a14af8529`  |
| 2434   | No file  | `384a14af8529`  |
| 2429   | No file  | `384a14af8529`  |
| 2421   | No file  | `384a14af8529`  |
| 2414   | No file  | `384a14af8529`  |
| 2407   | No file  | `384a14af8529`  |
| 2401   | No file  | `384a14af8529`  |
| 2397   | No file  | `384a14af8529`  |
| 2393   | No file  | `384a14af8529`  |
| 2384   | No file  | `384a14af8529`  |
| 2378   | No file  | `384a14af8529`  |
| 2372   | No file  | `384a14af8529`  |
| 2358   | No file  | `384a14af8529`  |
| 2352   | No file  | `384a14af8529`  |
| 2347   | No file  | `384a14af8529`  |
| 2343   | No file  | `384a14af8529`  |
| 2335   | No file  | `384a14af8529`  |
| 2327   | No file  | `384a14af8529`  |
| 2324   | No file  | `384a14af8529`  |
| 2319   | No file  | `384a14af8529`  |
| 2313   | No file  | `384a14af8529`  |
| 2308   | No file  | `384a14af8529`  |
| 2302   | No file  | `384a14af8529`  |
| 2295   | No file  | `384a14af8529`  |
| 2290   | No file  | `384a14af8529`  |
| 2284   | No file  | `384a14af8529`  |
| 2276   | No file  | `384a14af8529`  |
| 2269   | No file  | `384a14af8529`  |
| 2259   | No file  | `384a14af8529`  |
| 2250   | No file  | `384a14af8529`  |
| 2243   | No file  | `384a14af8529`  |
| 2235   | No file  | `384a14af8529`  |
| 2229   | No file  | `384a14af8529`  |
| 2224   | No file  | `384a14af8529`  |
| 2218   | No file  | `384a14af8529`  |
| 2215   | No file  | `384a14af8529`  |
| 2207   | No file  | `384a14af8529`  |
| 2203   | No file  | `384a14af8529`  |
| 2196   | No file  | `384a14af8529`  |
| 2192   | No file  | `384a14af8529`  |
| 2189   | No file  | `384a14af8529`  |
| 2183   | No file  | `384a14af8529`  |
| 2179   | No file  | `384a14af8529`  |
| 2171   | No file  | `384a14af8529`  |
| 2163   | No file  | `384a14af8529`  |
| 2156   | No file  | `384a14af8529`  |
| 2151   | No file  | `384a14af8529`  |
| 2147   | No file  | `384a14af8529`  |
| 2142   | No file  | `384a14af8529`  |
| 2138   | No file  | `384a14af8529`  |
| 2134   | No file  | `384a14af8529`  |
| 2130   | No file  | `384a14af8529`  |
| 2122   | No file  | `384a14af8529`  |
| 2107   | No file  | `384a14af8529`  |
| 2098   | No file  | `384a14af8529`  |
| 2089   | No file  | `384a14af8529`  |
| 2081   | No file  | `384a14af8529`  |
| 2073   | No file  | `384a14af8529`  |
| 2067   | No file  | `384a14af8529`  |
| 2063   | No file  | `384a14af8529`  |
| 2059   | No file  | `384a14af8529`  |
| 2052   | No file  | `384a14af8529`  |
| 2044   | No file  | `384a14af8529`  |
| 2039   | No file  | `384a14af8529`  |
| 2032   | No file  | `384a14af8529`  |
| 2025   | No file  | `384a14af8529`  |
| 2011   | No file  | `384a14af8529`  |
| 2005   | No file  | `384a14af8529`  |
| 2000   | No file  | `384a14af8529`  |
| 1996   | No file  | `384a14af8529`  |
| 1991   | No file  | `384a14af8529`  |
| 1985   | No file  | `384a14af8529`  |
| 1980   | No file  | `384a14af8529`  |
| 1969   | No file  | `384a14af8529`  |
| 1964   | No file  | `384a14af8529`  |
| 1958   | No file  | `384a14af8529`  |
| 1950   | No file  | `384a14af8529`  |
| 1945   | No file  | `384a14af8529`  |
| 1937   | No file  | `384a14af8529`  |
| 1933   | No file  | `384a14af8529`  |
| 1927   | No file  | `384a14af8529`  |
| 1921   | No file  | `384a14af8529`  |
| 1914   | No file  | `384a14af8529`  |
| 1908   | No file  | `384a14af8529`  |
| 1897   | No file  | `384a14af8529`  |
| 1892   | No file  | `384a14af8529`  |
| 1886   | No file  | `384a14af8529`  |
| 1881   | No file  | `384a14af8529`  |
| 1871   | No file  | `384a14af8529`  |
| 1866   | No file  | `384a14af8529`  |
| 1862   | No file  | `384a14af8529`  |
| 1854   | No file  | `384a14af8529`  |
| 1846   | No file  | `384a14af8529`  |
| 1838   | No file  | `384a14af8529`  |
| 1832   | No file  | `384a14af8529`  |
| 1826   | No file  | `384a14af8529`  |
| 1822   | No file  | `384a14af8529`  |
| 1818   | No file  | `384a14af8529`  |
| 1804   | No file  | `384a14af8529`  |
| 1794   | No file  | `384a14af8529`  |
| 1790   | No file  | `384a14af8529`  |
| 1784   | No file  | `384a14af8529`  |
| 1774   | No file  | `384a14af8529`  |
| 1771   | No file  | `384a14af8529`  |
| 1762   | No file  | `384a14af8529`  |
| 1759   | No file  | `384a14af8529`  |
| 1754   | No file  | `384a14af8529`  |
| 1749   | No file  | `384a14af8529`  |
| 1743   | No file  | `384a14af8529`  |
| 1737   | No file  | `384a14af8529`  |
| 1731   | No file  | `384a14af8529`  |
| 1725   | No file  | `384a14af8529`  |
| 1717   | No file  | `384a14af8529`  |
| 1710   | No file  | `384a14af8529`  |
| 1704   | No file  | `384a14af8529`  |
| 1698   | No file  | `384a14af8529`  |
| 1690   | No file  | `384a14af8529`  |
| 1685   | No file  | `384a14af8529`  |
| 1680   | No file  | `384a14af8529`  |
| 1674   | No file  | `384a14af8529`  |
| 1668   | No file  | `384a14af8529`  |
| 1659   | No file  | `384a14af8529`  |
| 1649   | No file  | `384a14af8529`  |
| 1642   | No file  | `384a14af8529`  |
| 1636   | No file  | `384a14af8529`  |
| 1628   | No file  | `384a14af8529`  |
| 1622   | No file  | `384a14af8529`  |
| 1614   | No file  | `384a14af8529`  |
| 1608   | No file  | `384a14af8529`  |
| 1602   | No file  | `384a14af8529`  |
| 1598   | No file  | `384a14af8529`  |
| 1594   | No file  | `384a14af8529`  |
| 1590   | No file  | `384a14af8529`  |
| 1587   | No file  | `384a14af8529`  |
| 1584   | No file  | `384a14af8529`  |
| 1579   | No file  | `384a14af8529`  |
| 1572   | No file  | `384a14af8529`  |
| 1565   | No file  | `384a14af8529`  |
| 1559   | No file  | `384a14af8529`  |
| 1554   | No file  | `384a14af8529`  |
| 1547   | No file  | `384a14af8529`  |
| 1537   | No file  | `384a14af8529`  |
| 1529   | No file  | `384a14af8529`  |
| 1524   | No file  | `384a14af8529`  |
| 1519   | No file  | `384a14af8529`  |
| 1509   | No file  | `384a14af8529`  |
| 1506   | No file  | `384a14af8529`  |
| 1504   | No file  | `384a14af8529`  |
| 1500   | No file  | `384a14af8529`  |
| 1493   | No file  | `384a14af8529`  |
| 1489   | No file  | `384a14af8529`  |
| 1485   | No file  | `384a14af8529`  |
| 1481   | No file  | `384a14af8529`  |
| 1474   | No file  | `384a14af8529`  |
| 1466   | No file  | `384a14af8529`  |
| 1462   | No file  | `384a14af8529`  |
| 1459   | No file  | `384a14af8529`  |
| 1453   | No file  | `384a14af8529`  |
| 1450   | No file  | `384a14af8529`  |
| 1445   | No file  | `384a14af8529`  |
| 1439   | No file  | `384a14af8529`  |
| 1433   | No file  | `384a14af8529`  |
| 1430   | No file  | `384a14af8529`  |
| 1426   | No file  | `384a14af8529`  |
| 1421   | No file  | `384a14af8529`  |
| 1417   | No file  | `384a14af8529`  |
| 1416   | No file  | `384a14af8529`  |
| 1409   | No file  | `384a14af8529`  |
| 1405   | No file  | `384a14af8529`  |
| 1401   | No file  | `384a14af8529`  |
| 1396   | No file  | `384a14af8529`  |
| 1391   | No file  | `384a14af8529`  |
| 1390   | No file  | `384a14af8529`  |
| 1386   | No file  | `384a14af8529`  |
| 1381   | No file  | `384a14af8529`  |
| 1379   | No file  | `384a14af8529`  |
| 1372   | No file  | `384a14af8529`  |
| 1366   | No file  | `384a14af8529`  |
| 1364   | No file  | `384a14af8529`  |
| 1363   | No file  | `384a14af8529`  |
| 1360   | No file  | `384a14af8529`  |
| 1358   | No file  | `384a14af8529`  |
| 1355   | No file  | `384a14af8529`  |
| 1351   | No file  | `384a14af8529`  |
| 1348   | No file  | `384a14af8529`  |
| 1346   | No file  | `384a14af8529`  |
| 1341   | No file  | `384a14af8529`  |
| 1340   | No file  | `384a14af8529`  |
| 1338   | No file  | `384a14af8529`  |
| 1335   | No file  | `384a14af8529`  |
| 1333   | No file  | `384a14af8529`  |
| 1329   | No file  | `384a14af8529`  |
| 1327   | No file  | `384a14af8529`  |
| 1324   | No file  | `384a14af8529`  |
| 1321   | No file  | `384a14af8529`  |
| 1319   | No file  | `384a14af8529`  |
| 1318   | No file  | `384a14af8529`  |
| 1316   | No file  | `384a14af8529`  |
| 1313   | No file  | `384a14af8529`  |
| 1311   | No file  | `384a14af8529`  |
| 1309   | No file  | `384a14af8529`  |
| 1304   | No file  | `384a14af8529`  |
| 1292   | No file  | `384a14af8529`  |
| 1286   | No file  | `384a14af8529`  |
| 1280   | No file  | `384a14af8529`  |
| 1276   | No file  | `384a14af8529`  |
| 1267   | No file  | `384a14af8529`  |
| 1261   | No file  | `384a14af8529`  |
| 1256   | No file  | `384a14af8529`  |
| 1250   | No file  | `384a14af8529`  |
| 1246   | No file  | `384a14af8529`  |
| 1239   | No file  | `384a14af8529`  |
| 1230   | No file  | `384a14af8529`  |
| 1226   | No file  | `384a14af8529`  |
| 1220   | No file  | `384a14af8529`  |
| 1217   | No file  | `384a14af8529`  |
| 1211   | No file  | `384a14af8529`  |
| 1210   | No file  | `384a14af8529`  |
| 1208   | No file  | `384a14af8529`  |
| 1203   | No file  | `384a14af8529`  |
| 1197   | No file  | `384a14af8529`  |
| 1194   | No file  | `384a14af8529`  |
| 1192   | No file  | `384a14af8529`  |
| 1187   | No file  | `384a14af8529`  |
| 1183   | No file  | `384a14af8529`  |
| 1177   | No file  | `384a14af8529`  |
| 1173   | No file  | `384a14af8529`  |
| 1167   | No file  | `384a14af8529`  |
| 1164   | No file  | `384a14af8529`  |
| 1156   | No file  | `384a14af8529`  |
| 1149   | No file  | `384a14af8529`  |
| 1144   | No file  | `384a14af8529`  |
| 1137   | No file  | `384a14af8529`  |
| 1132   | No file  | `384a14af8529`  |
| 1127   | No file  | `384a14af8529`  |
| 1122   | No file  | `384a14af8529`  |
| 1118   | No file  | `384a14af8529`  |
| 1114   | No file  | `384a14af8529`  |
| 1109   | No file  | `384a14af8529`  |
| 1102   | No file  | `384a14af8529`  |
| 1096   | No file  | `384a14af8529`  |
| 1088   | No file  | `384a14af8529`  |
| 1081   | No file  | `384a14af8529`  |
| 1076   | No file  | `384a14af8529`  |
| 1069   | No file  | `384a14af8529`  |
| 1064   | No file  | `384a14af8529`  |
| 1058   | No file  | `384a14af8529`  |
| 1051   | No file  | `384a14af8529`  |
| 1044   | No file  | `384a14af8529`  |
| 1036   | No file  | `384a14af8529`  |
| 1026   | No file  | `384a14af8529`  |
| 1016   | No file  | `384a14af8529`  |
| 1009   | No file  | `384a14af8529`  |
| 1005   | No file  | `384a14af8529`  |
| 1000   | No file  | `384a14af8529`  |
| 998    | No file  | `384a14af8529`  |
| 990    | No file  | `384a14af8529`  |
| 979    | No file  | `384a14af8529`  |
| 972    | No file  | `384a14af8529`  |
| 963    | No file  | `384a14af8529`  |
| 955    | No file  | `384a14af8529`  |
| 946    | No file  | `384a14af8529`  |
| 938    | No file  | `384a14af8529`  |
| 927    | No file  | `384a14af8529`  |
| 911    | No file  | `384a14af8529`  |
| 904    | No file  | `384a14af8529`  |
| 899    | No file  | `384a14af8529`  |
| 894    | No file  | `384a14af8529`  |
| 885    | No file  | `384a14af8529`  |
| 879    | No file  | `384a14af8529`  |
| 872    | No file  | `384a14af8529`  |
| 864    | No file  | `384a14af8529`  |
| 855    | No file  | `384a14af8529`  |
| 853    | No file  | `384a14af8529`  |
| 845    | No file  | `384a14af8529`  |
| 837    | No file  | `384a14af8529`  |
| 829    | No file  | `384a14af8529`  |
| 822    | No file  | `384a14af8529`  |
| 814    | No file  | `384a14af8529`  |
| 805    | No file  | `384a14af8529`  |
| 794    | No file  | `384a14af8529`  |
| 787    | No file  | `384a14af8529`  |
| 780    | No file  | `384a14af8529`  |
| 771    | No file  | `384a14af8529`  |
| 760    | No file  | `384a14af8529`  |
| 748    | No file  | `384a14af8529`  |
| 741    | No file  | `384a14af8529`  |
| 736    | No file  | `384a14af8529`  |
| 731    | No file  | `384a14af8529`  |
| 723    | No file  | `384a14af8529`  |
| 711    | No file  | `384a14af8529`  |
| 707    | No file  | `384a14af8529`  |
| 697    | No file  | `384a14af8529`  |
| 689    | No file  | `384a14af8529`  |
| 683    | No file  | `384a14af8529`  |
| 678    | No file  | `384a14af8529`  |
| 670    | No file  | `384a14af8529`  |
| 661    | No file  | `384a14af8529`  |
| 656    | No file  | `384a14af8529`  |
| 652    | No file  | `384a14af8529`  |
| 643    | No file  | `384a14af8529`  |
| 637    | No file  | `384a14af8529`  |
| 630    | No file  | `384a14af8529`  |
| 627    | No file  | `384a14af8529`  |
| 621    | No file  | `384a14af8529`  |
| 617    | No file  | `384a14af8529`  |
| 615    | No file  | `384a14af8529`  |
| 606    | No file  | `384a14af8529`  |
| 599    | No file  | `384a14af8529`  |
| 592    | No file  | `384a14af8529`  |
| 586    | No file  | `384a14af8529`  |
| 577    | No file  | `384a14af8529`  |
| 569    | No file  | `384a14af8529`  |
| 561    | No file  | `384a14af8529`  |
| 554    | No file  | `384a14af8529`  |
| 542    | No file  | `384a14af8529`  |
| 532    | No file  | `384a14af8529`  |
| 531    | No file  | `384a14af8529`  |
| 526    | No file  | `384a14af8529`  |
| 521    | No file  | `384a14af8529`  |
| 517    | No file  | `384a14af8529`  |
| 510    | No file  | `384a14af8529`  |
| 508    | No file  | `384a14af8529`  |
| 504    | No file  | `384a14af8529`  |
| 497    | No file  | `384a14af8529`  |
| 491    | No file  | `384a14af8529`  |
| 485    | No file  | `384a14af8529`  |
| 478    | No file  | `384a14af8529`  |
| 472    | No file  | `384a14af8529`  |
| 466    | No file  | `384a14af8529`  |
| 457    | No file  | `384a14af8529`  |
| 452    | No file  | `384a14af8529`  |
| 449    | No file  | `384a14af8529`  |
| 435    | No file  | `384a14af8529`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field        | Notes                                                      |
| ------------------- | --------------- | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32             | row_count    | Number of rows                                             |
| `+0x08`             | Row[row_count]  | rows         | See Row; byte-packed                                       |
| `rows+0x00`         | String Table    | string_table | See String Table                                           |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where `rows` ends              |
| `string_table+0x04` | u32             | zero         | Always `0`                                                 |

### Row (9 bytes)

| Offset  | Type     | Field      | Notes                                                              |
| ------- | -------- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | bytes[3] | map_color  | Region map colour, stored blue, green, red; `10 0D 10` and `E8 1B 18` on client 3474 |
| `+0x03` | u8       | unknown_03 | Always `0`                                                         |
| `+0x04` | bytes[3] | unknown_04 | Equals `map_color` on every row                                    |
| `+0x07` | u8       | unknown_07 | Always `0`                                                         |
| `+0x08` | u8       | unknown_08 | `0` and `1`, one per row                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 02 00 00 00 10 0D 10 00 10 0D 10 00 00 E8 1B 18 00 E8 1B 18 00 01 00 00 00 00 1A 00 00 00 00 00 00 00`
  (38 bytes). The file is not in the archives of clients 794 to 2519.
- The same two rows close `hardcorechannelinfo.bss` on client 3474, a
  15-row file of this row shape: `E8 1B 18` with `1`, then `10 0D 10`
  with `0`. `10 0D 10` is also the colour of the `_Count` row of
  `edaniaregioninfo.bss`.
- `map_color` follows `ui_texture/minimap/area/elfwar_siegemap.bmp.rid`, the
  palette of the Rose War region map, which lists exactly these two colours
  (`100d10` first) on client 3474; the same holds for the region maps of
  three other tables of this row shape
  ([`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md#field-names)
  Field Names). Read as `rrggbb` the rows are `100d10` (near black) and
  `181be8` (blue).
- The file is newer than client 1784: no sheet of a private server's
  `DataSheets.bexcel` on that client and no string of its server dump has
  `RoseWar` in the name.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`:
  `map_color` as `rrggbb`.

## Open Questions

### The Value of Each Colour

What `unknown_08` stands for, and what the second copy of the colour is
for. The Rose War region map has one colour besides the `100d10` that
every region map palette lists first, so `unknown_08` (`1` for it, `0` for
`100d10`) marks the one area and does not pick between the Kamasylvia and
O'dyllita teams of
[`rosewarteamnostaticstatus.bss`](rosewarteamnostaticstatus_bss.md). The
client 3474 Lua has `getRoseWarTeamNo` and the two `__eRoseWarTeam_*`
names, and no call that returns a colour.
