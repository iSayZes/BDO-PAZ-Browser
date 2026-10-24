# `maidactoroption.bss` Format

## Purpose

Options of the maid actor system (`_ContentsGroup_MaidActorSystem` in the
client Lua): two bytes in the slot where a PABR table keeps its record
count, then an empty string table. On client 3474 the bytes are `1` and
`10`; no source confirms what either holds.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | -------------- | --------- |
| 1      | 3086 and later | 3483    | `maidactoroption.bss` | 18    | 1 String Table | 4         |

| Layout | File                  | Known        | Unknown     |
| ------ | --------------------- | ------------ | ----------- |
| 1      | `maidactoroption.bss` | 16 B (88.9%) | 2 B (11.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `935868e72e77`  |
| 3482   | Layout 1 | `935868e72e77`  |
| 3474   | Layout 1 | `935868e72e77`  |
| 3473   | Layout 1 | `935868e72e77`  |
| 3464   | Layout 1 | `935868e72e77`  |
| 3458   | Layout 1 | `935868e72e77`  |
| 3454   | Layout 1 | `935868e72e77`  |
| 3444   | Layout 1 | `935868e72e77`  |
| 3435   | Layout 1 | `935868e72e77`  |
| 3426   | Layout 1 | `935868e72e77`  |
| 3418   | Layout 1 | `935868e72e77`  |
| 3412   | Layout 1 | `935868e72e77`  |
| 3402   | Layout 1 | `935868e72e77`  |
| 3396   | Layout 1 | `935868e72e77`  |
| 3387   | Layout 1 | `935868e72e77`  |
| 3381   | Layout 1 | `935868e72e77`  |
| 3373   | Layout 1 | `935868e72e77`  |
| 3364   | Layout 1 | `935868e72e77`  |
| 3356   | Layout 1 | `935868e72e77`  |
| 3349   | Layout 1 | `935868e72e77`  |
| 3342   | Layout 1 | `935868e72e77`  |
| 3335   | Layout 1 | `935868e72e77`  |
| 3326   | Layout 1 | `935868e72e77`  |
| 3321   | Layout 1 | `935868e72e77`  |
| 3314   | Layout 1 | `935868e72e77`  |
| 3303   | Layout 1 | `935868e72e77`  |
| 3302   | Layout 1 | `935868e72e77`  |
| 3293   | Layout 1 | `935868e72e77`  |
| 3283   | Layout 1 | `935868e72e77`  |
| 3275   | Layout 1 | `935868e72e77`  |
| 3267   | Layout 1 | `935868e72e77`  |
| 3258   | Layout 1 | `935868e72e77`  |
| 3251   | Layout 1 | `935868e72e77`  |
| 3242   | Layout 1 | `935868e72e77`  |
| 3235   | Layout 1 | `935868e72e77`  |
| 3229   | Layout 1 | `935868e72e77`  |
| 3212   | Layout 1 | `935868e72e77`  |
| 3203   | Layout 1 | `935868e72e77`  |
| 3193   | Layout 1 | `935868e72e77`  |
| 3186   | Layout 1 | `935868e72e77`  |
| 3177   | Layout 1 | `935868e72e77`  |
| 3169   | Layout 1 | `935868e72e77`  |
| 3158   | Layout 1 | `935868e72e77`  |
| 3151   | Layout 1 | `935868e72e77`  |
| 3144   | Layout 1 | `935868e72e77`  |
| 3133   | Layout 1 | `935868e72e77`  |
| 3125   | Layout 1 | `935868e72e77`  |
| 3118   | Layout 1 | `935868e72e77`  |
| 3111   | Layout 1 | `935868e72e77`  |
| 3103   | Layout 1 | `935868e72e77`  |
| 3095   | Layout 1 | `935868e72e77`  |
| 3086   | Layout 1 | `935868e72e77`  |
| 3072   | No file  | `935868e72e77`  |
| 3062   | No file  | `935868e72e77`  |
| 3052   | No file  | `935868e72e77`  |
| 3045   | No file  | `935868e72e77`  |
| 3037   | No file  | `935868e72e77`  |
| 3030   | No file  | `935868e72e77`  |
| 3021   | No file  | `935868e72e77`  |
| 3012   | No file  | `935868e72e77`  |
| 3002   | No file  | `935868e72e77`  |
| 2995   | No file  | `935868e72e77`  |
| 2987   | No file  | `935868e72e77`  |
| 2978   | No file  | `935868e72e77`  |
| 2970   | No file  | `935868e72e77`  |
| 2959   | No file  | `935868e72e77`  |
| 2951   | No file  | `935868e72e77`  |
| 2942   | No file  | `935868e72e77`  |
| 2935   | No file  | `935868e72e77`  |
| 2932   | No file  | `935868e72e77`  |
| 2923   | No file  | `935868e72e77`  |
| 2919   | No file  | `935868e72e77`  |
| 2907   | No file  | `935868e72e77`  |
| 2900   | No file  | `935868e72e77`  |
| 2891   | No file  | `935868e72e77`  |
| 2882   | No file  | `935868e72e77`  |
| 2872   | No file  | `935868e72e77`  |
| 2863   | No file  | `935868e72e77`  |
| 2855   | No file  | `935868e72e77`  |
| 2849   | No file  | `935868e72e77`  |
| 2844   | No file  | `935868e72e77`  |
| 2834   | No file  | `935868e72e77`  |
| 2825   | No file  | `935868e72e77`  |
| 2819   | No file  | `935868e72e77`  |
| 2811   | No file  | `935868e72e77`  |
| 2803   | No file  | `935868e72e77`  |
| 2794   | No file  | `935868e72e77`  |
| 2783   | No file  | `935868e72e77`  |
| 2774   | No file  | `935868e72e77`  |
| 2765   | No file  | `935868e72e77`  |
| 2756   | No file  | `935868e72e77`  |
| 2750   | No file  | `935868e72e77`  |
| 2743   | No file  | `935868e72e77`  |
| 2736   | No file  | `935868e72e77`  |
| 2726   | No file  | `935868e72e77`  |
| 2717   | No file  | `935868e72e77`  |
| 2709   | No file  | `935868e72e77`  |
| 2703   | No file  | `935868e72e77`  |
| 2695   | No file  | `935868e72e77`  |
| 2684   | No file  | `935868e72e77`  |
| 2672   | No file  | `935868e72e77`  |
| 2665   | No file  | `935868e72e77`  |
| 2657   | No file  | `935868e72e77`  |
| 2649   | No file  | `935868e72e77`  |
| 2644   | No file  | `935868e72e77`  |
| 2637   | No file  | `935868e72e77`  |
| 2629   | No file  | `935868e72e77`  |
| 2619   | No file  | `935868e72e77`  |
| 2612   | No file  | `935868e72e77`  |
| 2606   | No file  | `935868e72e77`  |
| 2602   | No file  | `935868e72e77`  |
| 2601   | No file  | `935868e72e77`  |
| 2592   | No file  | `935868e72e77`  |
| 2583   | No file  | `935868e72e77`  |
| 2575   | No file  | `935868e72e77`  |
| 2567   | No file  | `935868e72e77`  |
| 2560   | No file  | `935868e72e77`  |
| 2553   | No file  | `935868e72e77`  |
| 2545   | No file  | `935868e72e77`  |
| 2538   | No file  | `935868e72e77`  |
| 2529   | No file  | `935868e72e77`  |
| 2519   | No file  | `935868e72e77`  |
| 2513   | No file  | `935868e72e77`  |
| 2510   | No file  | `935868e72e77`  |
| 2507   | No file  | `935868e72e77`  |
| 2503   | No file  | `935868e72e77`  |
| 2498   | No file  | `935868e72e77`  |
| 2492   | No file  | `935868e72e77`  |
| 2487   | No file  | `935868e72e77`  |
| 2480   | No file  | `935868e72e77`  |
| 2474   | No file  | `935868e72e77`  |
| 2468   | No file  | `935868e72e77`  |
| 2460   | No file  | `935868e72e77`  |
| 2453   | No file  | `935868e72e77`  |
| 2444   | No file  | `935868e72e77`  |
| 2438   | No file  | `935868e72e77`  |
| 2434   | No file  | `935868e72e77`  |
| 2429   | No file  | `935868e72e77`  |
| 2421   | No file  | `935868e72e77`  |
| 2414   | No file  | `935868e72e77`  |
| 2407   | No file  | `935868e72e77`  |
| 2401   | No file  | `935868e72e77`  |
| 2397   | No file  | `935868e72e77`  |
| 2393   | No file  | `935868e72e77`  |
| 2384   | No file  | `935868e72e77`  |
| 2378   | No file  | `935868e72e77`  |
| 2372   | No file  | `935868e72e77`  |
| 2358   | No file  | `935868e72e77`  |
| 2352   | No file  | `935868e72e77`  |
| 2347   | No file  | `935868e72e77`  |
| 2343   | No file  | `935868e72e77`  |
| 2335   | No file  | `935868e72e77`  |
| 2327   | No file  | `935868e72e77`  |
| 2324   | No file  | `935868e72e77`  |
| 2319   | No file  | `935868e72e77`  |
| 2313   | No file  | `935868e72e77`  |
| 2308   | No file  | `935868e72e77`  |
| 2302   | No file  | `935868e72e77`  |
| 2295   | No file  | `935868e72e77`  |
| 2290   | No file  | `935868e72e77`  |
| 2284   | No file  | `935868e72e77`  |
| 2276   | No file  | `935868e72e77`  |
| 2269   | No file  | `935868e72e77`  |
| 2259   | No file  | `935868e72e77`  |
| 2250   | No file  | `935868e72e77`  |
| 2243   | No file  | `935868e72e77`  |
| 2235   | No file  | `935868e72e77`  |
| 2229   | No file  | `935868e72e77`  |
| 2224   | No file  | `935868e72e77`  |
| 2218   | No file  | `935868e72e77`  |
| 2215   | No file  | `935868e72e77`  |
| 2207   | No file  | `935868e72e77`  |
| 2203   | No file  | `935868e72e77`  |
| 2196   | No file  | `935868e72e77`  |
| 2192   | No file  | `935868e72e77`  |
| 2189   | No file  | `935868e72e77`  |
| 2183   | No file  | `935868e72e77`  |
| 2179   | No file  | `935868e72e77`  |
| 2171   | No file  | `935868e72e77`  |
| 2163   | No file  | `935868e72e77`  |
| 2156   | No file  | `935868e72e77`  |
| 2151   | No file  | `935868e72e77`  |
| 2147   | No file  | `935868e72e77`  |
| 2142   | No file  | `935868e72e77`  |
| 2138   | No file  | `935868e72e77`  |
| 2134   | No file  | `935868e72e77`  |
| 2130   | No file  | `935868e72e77`  |
| 2122   | No file  | `935868e72e77`  |
| 2107   | No file  | `935868e72e77`  |
| 2098   | No file  | `935868e72e77`  |
| 2089   | No file  | `935868e72e77`  |
| 2081   | No file  | `935868e72e77`  |
| 2073   | No file  | `935868e72e77`  |
| 2067   | No file  | `935868e72e77`  |
| 2063   | No file  | `935868e72e77`  |
| 2059   | No file  | `935868e72e77`  |
| 2052   | No file  | `935868e72e77`  |
| 2044   | No file  | `935868e72e77`  |
| 2039   | No file  | `935868e72e77`  |
| 2032   | No file  | `935868e72e77`  |
| 2025   | No file  | `935868e72e77`  |
| 2011   | No file  | `935868e72e77`  |
| 2005   | No file  | `935868e72e77`  |
| 2000   | No file  | `935868e72e77`  |
| 1996   | No file  | `935868e72e77`  |
| 1991   | No file  | `935868e72e77`  |
| 1985   | No file  | `935868e72e77`  |
| 1980   | No file  | `935868e72e77`  |
| 1969   | No file  | `935868e72e77`  |
| 1964   | No file  | `935868e72e77`  |
| 1958   | No file  | `935868e72e77`  |
| 1950   | No file  | `935868e72e77`  |
| 1945   | No file  | `935868e72e77`  |
| 1937   | No file  | `935868e72e77`  |
| 1933   | No file  | `935868e72e77`  |
| 1927   | No file  | `935868e72e77`  |
| 1921   | No file  | `935868e72e77`  |
| 1914   | No file  | `935868e72e77`  |
| 1908   | No file  | `935868e72e77`  |
| 1897   | No file  | `935868e72e77`  |
| 1892   | No file  | `935868e72e77`  |
| 1886   | No file  | `935868e72e77`  |
| 1881   | No file  | `935868e72e77`  |
| 1871   | No file  | `935868e72e77`  |
| 1866   | No file  | `935868e72e77`  |
| 1862   | No file  | `935868e72e77`  |
| 1854   | No file  | `935868e72e77`  |
| 1846   | No file  | `935868e72e77`  |
| 1838   | No file  | `935868e72e77`  |
| 1832   | No file  | `935868e72e77`  |
| 1826   | No file  | `935868e72e77`  |
| 1822   | No file  | `935868e72e77`  |
| 1818   | No file  | `935868e72e77`  |
| 1804   | No file  | `935868e72e77`  |
| 1794   | No file  | `935868e72e77`  |
| 1790   | No file  | `935868e72e77`  |
| 1784   | No file  | `935868e72e77`  |
| 1774   | No file  | `935868e72e77`  |
| 1771   | No file  | `935868e72e77`  |
| 1762   | No file  | `935868e72e77`  |
| 1759   | No file  | `935868e72e77`  |
| 1754   | No file  | `935868e72e77`  |
| 1749   | No file  | `935868e72e77`  |
| 1743   | No file  | `935868e72e77`  |
| 1737   | No file  | `935868e72e77`  |
| 1731   | No file  | `935868e72e77`  |
| 1725   | No file  | `935868e72e77`  |
| 1717   | No file  | `935868e72e77`  |
| 1710   | No file  | `935868e72e77`  |
| 1704   | No file  | `935868e72e77`  |
| 1698   | No file  | `935868e72e77`  |
| 1690   | No file  | `935868e72e77`  |
| 1685   | No file  | `935868e72e77`  |
| 1680   | No file  | `935868e72e77`  |
| 1674   | No file  | `935868e72e77`  |
| 1668   | No file  | `935868e72e77`  |
| 1659   | No file  | `935868e72e77`  |
| 1649   | No file  | `935868e72e77`  |
| 1642   | No file  | `935868e72e77`  |
| 1636   | No file  | `935868e72e77`  |
| 1628   | No file  | `935868e72e77`  |
| 1622   | No file  | `935868e72e77`  |
| 1614   | No file  | `935868e72e77`  |
| 1608   | No file  | `935868e72e77`  |
| 1602   | No file  | `935868e72e77`  |
| 1598   | No file  | `935868e72e77`  |
| 1594   | No file  | `935868e72e77`  |
| 1590   | No file  | `935868e72e77`  |
| 1587   | No file  | `935868e72e77`  |
| 1584   | No file  | `935868e72e77`  |
| 1579   | No file  | `935868e72e77`  |
| 1572   | No file  | `935868e72e77`  |
| 1565   | No file  | `935868e72e77`  |
| 1559   | No file  | `935868e72e77`  |
| 1554   | No file  | `935868e72e77`  |
| 1547   | No file  | `935868e72e77`  |
| 1537   | No file  | `935868e72e77`  |
| 1529   | No file  | `935868e72e77`  |
| 1524   | No file  | `935868e72e77`  |
| 1519   | No file  | `935868e72e77`  |
| 1509   | No file  | `935868e72e77`  |
| 1506   | No file  | `935868e72e77`  |
| 1504   | No file  | `935868e72e77`  |
| 1500   | No file  | `935868e72e77`  |
| 1493   | No file  | `935868e72e77`  |
| 1489   | No file  | `935868e72e77`  |
| 1485   | No file  | `935868e72e77`  |
| 1481   | No file  | `935868e72e77`  |
| 1474   | No file  | `935868e72e77`  |
| 1466   | No file  | `935868e72e77`  |
| 1462   | No file  | `935868e72e77`  |
| 1459   | No file  | `935868e72e77`  |
| 1453   | No file  | `935868e72e77`  |
| 1450   | No file  | `935868e72e77`  |
| 1445   | No file  | `935868e72e77`  |
| 1439   | No file  | `935868e72e77`  |
| 1433   | No file  | `935868e72e77`  |
| 1430   | No file  | `935868e72e77`  |
| 1426   | No file  | `935868e72e77`  |
| 1421   | No file  | `935868e72e77`  |
| 1417   | No file  | `935868e72e77`  |
| 1416   | No file  | `935868e72e77`  |
| 1409   | No file  | `935868e72e77`  |
| 1405   | No file  | `935868e72e77`  |
| 1401   | No file  | `935868e72e77`  |
| 1396   | No file  | `935868e72e77`  |
| 1391   | No file  | `935868e72e77`  |
| 1390   | No file  | `935868e72e77`  |
| 1386   | No file  | `935868e72e77`  |
| 1381   | No file  | `935868e72e77`  |
| 1379   | No file  | `935868e72e77`  |
| 1372   | No file  | `935868e72e77`  |
| 1366   | No file  | `935868e72e77`  |
| 1364   | No file  | `935868e72e77`  |
| 1363   | No file  | `935868e72e77`  |
| 1360   | No file  | `935868e72e77`  |
| 1358   | No file  | `935868e72e77`  |
| 1355   | No file  | `935868e72e77`  |
| 1351   | No file  | `935868e72e77`  |
| 1348   | No file  | `935868e72e77`  |
| 1346   | No file  | `935868e72e77`  |
| 1341   | No file  | `935868e72e77`  |
| 1340   | No file  | `935868e72e77`  |
| 1338   | No file  | `935868e72e77`  |
| 1335   | No file  | `935868e72e77`  |
| 1333   | No file  | `935868e72e77`  |
| 1329   | No file  | `935868e72e77`  |
| 1327   | No file  | `935868e72e77`  |
| 1324   | No file  | `935868e72e77`  |
| 1321   | No file  | `935868e72e77`  |
| 1319   | No file  | `935868e72e77`  |
| 1318   | No file  | `935868e72e77`  |
| 1316   | No file  | `935868e72e77`  |
| 1313   | No file  | `935868e72e77`  |
| 1311   | No file  | `935868e72e77`  |
| 1309   | No file  | `935868e72e77`  |
| 1304   | No file  | `935868e72e77`  |
| 1292   | No file  | `935868e72e77`  |
| 1286   | No file  | `935868e72e77`  |
| 1280   | No file  | `935868e72e77`  |
| 1276   | No file  | `935868e72e77`  |
| 1267   | No file  | `935868e72e77`  |
| 1261   | No file  | `935868e72e77`  |
| 1256   | No file  | `935868e72e77`  |
| 1250   | No file  | `935868e72e77`  |
| 1246   | No file  | `935868e72e77`  |
| 1239   | No file  | `935868e72e77`  |
| 1230   | No file  | `935868e72e77`  |
| 1226   | No file  | `935868e72e77`  |
| 1220   | No file  | `935868e72e77`  |
| 1217   | No file  | `935868e72e77`  |
| 1211   | No file  | `935868e72e77`  |
| 1210   | No file  | `935868e72e77`  |
| 1208   | No file  | `935868e72e77`  |
| 1203   | No file  | `935868e72e77`  |
| 1197   | No file  | `935868e72e77`  |
| 1194   | No file  | `935868e72e77`  |
| 1192   | No file  | `935868e72e77`  |
| 1187   | No file  | `935868e72e77`  |
| 1183   | No file  | `935868e72e77`  |
| 1177   | No file  | `935868e72e77`  |
| 1173   | No file  | `935868e72e77`  |
| 1167   | No file  | `935868e72e77`  |
| 1164   | No file  | `935868e72e77`  |
| 1156   | No file  | `935868e72e77`  |
| 1149   | No file  | `935868e72e77`  |
| 1144   | No file  | `935868e72e77`  |
| 1137   | No file  | `935868e72e77`  |
| 1132   | No file  | `935868e72e77`  |
| 1127   | No file  | `935868e72e77`  |
| 1122   | No file  | `935868e72e77`  |
| 1118   | No file  | `935868e72e77`  |
| 1114   | No file  | `935868e72e77`  |
| 1109   | No file  | `935868e72e77`  |
| 1102   | No file  | `935868e72e77`  |
| 1096   | No file  | `935868e72e77`  |
| 1088   | No file  | `935868e72e77`  |
| 1081   | No file  | `935868e72e77`  |
| 1076   | No file  | `935868e72e77`  |
| 1069   | No file  | `935868e72e77`  |
| 1064   | No file  | `935868e72e77`  |
| 1058   | No file  | `935868e72e77`  |
| 1051   | No file  | `935868e72e77`  |
| 1044   | No file  | `935868e72e77`  |
| 1036   | No file  | `935868e72e77`  |
| 1026   | No file  | `935868e72e77`  |
| 1016   | No file  | `935868e72e77`  |
| 1009   | No file  | `935868e72e77`  |
| 1005   | No file  | `935868e72e77`  |
| 1000   | No file  | `935868e72e77`  |
| 998    | No file  | `935868e72e77`  |
| 990    | No file  | `935868e72e77`  |
| 979    | No file  | `935868e72e77`  |
| 972    | No file  | `935868e72e77`  |
| 963    | No file  | `935868e72e77`  |
| 955    | No file  | `935868e72e77`  |
| 946    | No file  | `935868e72e77`  |
| 938    | No file  | `935868e72e77`  |
| 927    | No file  | `935868e72e77`  |
| 911    | No file  | `935868e72e77`  |
| 904    | No file  | `935868e72e77`  |
| 899    | No file  | `935868e72e77`  |
| 894    | No file  | `935868e72e77`  |
| 885    | No file  | `935868e72e77`  |
| 879    | No file  | `935868e72e77`  |
| 872    | No file  | `935868e72e77`  |
| 864    | No file  | `935868e72e77`  |
| 855    | No file  | `935868e72e77`  |
| 853    | No file  | `935868e72e77`  |
| 845    | No file  | `935868e72e77`  |
| 837    | No file  | `935868e72e77`  |
| 829    | No file  | `935868e72e77`  |
| 822    | No file  | `935868e72e77`  |
| 814    | No file  | `935868e72e77`  |
| 805    | No file  | `935868e72e77`  |
| 794    | No file  | `935868e72e77`  |
| 787    | No file  | `935868e72e77`  |
| 780    | No file  | `935868e72e77`  |
| 771    | No file  | `935868e72e77`  |
| 760    | No file  | `935868e72e77`  |
| 748    | No file  | `935868e72e77`  |
| 741    | No file  | `935868e72e77`  |
| 736    | No file  | `935868e72e77`  |
| 731    | No file  | `935868e72e77`  |
| 723    | No file  | `935868e72e77`  |
| 711    | No file  | `935868e72e77`  |
| 707    | No file  | `935868e72e77`  |
| 697    | No file  | `935868e72e77`  |
| 689    | No file  | `935868e72e77`  |
| 683    | No file  | `935868e72e77`  |
| 678    | No file  | `935868e72e77`  |
| 670    | No file  | `935868e72e77`  |
| 661    | No file  | `935868e72e77`  |
| 656    | No file  | `935868e72e77`  |
| 652    | No file  | `935868e72e77`  |
| 643    | No file  | `935868e72e77`  |
| 637    | No file  | `935868e72e77`  |
| 630    | No file  | `935868e72e77`  |
| 627    | No file  | `935868e72e77`  |
| 621    | No file  | `935868e72e77`  |
| 617    | No file  | `935868e72e77`  |
| 615    | No file  | `935868e72e77`  |
| 606    | No file  | `935868e72e77`  |
| 599    | No file  | `935868e72e77`  |
| 592    | No file  | `935868e72e77`  |
| 586    | No file  | `935868e72e77`  |
| 577    | No file  | `935868e72e77`  |
| 569    | No file  | `935868e72e77`  |
| 561    | No file  | `935868e72e77`  |
| 554    | No file  | `935868e72e77`  |
| 542    | No file  | `935868e72e77`  |
| 532    | No file  | `935868e72e77`  |
| 531    | No file  | `935868e72e77`  |
| 526    | No file  | `935868e72e77`  |
| 521    | No file  | `935868e72e77`  |
| 517    | No file  | `935868e72e77`  |
| 510    | No file  | `935868e72e77`  |
| 508    | No file  | `935868e72e77`  |
| 504    | No file  | `935868e72e77`  |
| 497    | No file  | `935868e72e77`  |
| 491    | No file  | `935868e72e77`  |
| 485    | No file  | `935868e72e77`  |
| 478    | No file  | `935868e72e77`  |
| 472    | No file  | `935868e72e77`  |
| 466    | No file  | `935868e72e77`  |
| 457    | No file  | `935868e72e77`  |
| 452    | No file  | `935868e72e77`  |
| 449    | No file  | `935868e72e77`  |
| 435    | No file  | `935868e72e77`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                                                      |
| ------------------- | ------------ | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic        | ASCII `PABR`                                               |
| `+0x04`             | u8           | unknown_04   | `1` on clients 3251 and 3474                               |
| `+0x05`             | u8           | unknown_05   | `10` on clients 3251 and 3474                              |
| `+0x06`             | String Table | string_table | See String Table                                           |
| `string_table+0x00` | u32          | table_start  | Offset of the string table; `0x06` on every client checked |
| `string_table+0x04` | u32          | zero         | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 3251 and 3474:
  `50 41 42 52 01 0A 00 00 00 00 06 00 00 00 00 00 00 00` (18 bytes).
- The file is not in the archives of clients 1784, 2107, 2519 and 3002.
- Two u8 fields are a reading of the bytes; one u16 (`2561`) fits them too.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`. With no
  confirmed field, the preview shows the raw value bytes.

## Open Questions

### Maid Actor Limits

The client Lua (client 3474) reads several maid actor numbers from the
client: `ToClient_GetMaidActorNameLengthMax()`,
`ToClient_GetMaidActorSlotCount()`,
`ToClient_GetNeedItemCountForChangeClothForMaidActor()` and
`ToClient_getUsableMaidCountByType()`. Any of them could return `1` or
`10`, and none of them is shown to read this file. Which one, if any, does
is unknown. The name length and the outfit item count are on screen, see
In-Game Checks.

## In-Game Checks

### Maid Actor Name Length and Outfit Item Count

Needs: a character that can make a custom maid from its own appearance (the
`Panel_Window_MaidActorRegist_All` window).

The client Lua shows two of the candidate numbers on screen. This check tests
whether they are the `10` and the `1` of this file.

1. Open the custom maid creation window, or the rename window of a custom
   maid you already have.
2. Read the description line, which names the minimum and maximum name
   length, and type a long name to see where input stops.
3. Open the custom maid outfit change window and pick an outfit item.
4. Read the count after the required item's name, shown as `(needed/owned)`.

A maximum name length of `10` means `unknown_05` is the name length limit
(`ToClient_GetMaidActorNameLengthMax()`). A needed count of `1` means
`unknown_04` is the outfit change item count
(`ToClient_GetNeedItemCountForChangeClothForMaidActor()`). Other numbers
rule both readings out.
