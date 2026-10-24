# `personalrelayoption.bss` Format

## Purpose

The personal relay fields, the mirror fields of
`__eMirrorFieldContentsKey_PersonalRelayField` in the client Lua. One row
per field: its Korean name in the string table, three points, two times,
the NPC and monster character keys, two item IDs and unnamed counts. On client 3474 the
file has 2 rows, 금돼지굴 (Golden Pig Cave) with Golden Pig and 금돼지굴(일반)
(Golden Pig Cave, normal) with Golden Pigs, both with the NPC Munsik
(title Golden Pig Cave Subjugation).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 2811 and later | 3483    | `personalrelayoption.bss` | 250   | 2 Row   | 98        |

| Layout | File                      | Known        | Unknown       |
| ------ | ------------------------- | ------------ | ------------- |
| 1      | `personalrelayoption.bss` | 86 B (34.4%) | 164 B (65.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `750353d48fa7`  |
| 3482   | Layout 1 | `750353d48fa7`  |
| 3474   | Layout 1 | `750353d48fa7`  |
| 3473   | Layout 1 | `750353d48fa7`  |
| 3464   | Layout 1 | `750353d48fa7`  |
| 3458   | Layout 1 | `750353d48fa7`  |
| 3454   | Layout 1 | `750353d48fa7`  |
| 3444   | Layout 1 | `750353d48fa7`  |
| 3435   | Layout 1 | `750353d48fa7`  |
| 3426   | Layout 1 | `750353d48fa7`  |
| 3418   | Layout 1 | `750353d48fa7`  |
| 3412   | Layout 1 | `750353d48fa7`  |
| 3402   | Layout 1 | `750353d48fa7`  |
| 3396   | Layout 1 | `750353d48fa7`  |
| 3387   | Layout 1 | `750353d48fa7`  |
| 3381   | Layout 1 | `750353d48fa7`  |
| 3373   | Layout 1 | `750353d48fa7`  |
| 3364   | Layout 1 | `750353d48fa7`  |
| 3356   | Layout 1 | `750353d48fa7`  |
| 3349   | Layout 1 | `750353d48fa7`  |
| 3342   | Layout 1 | `750353d48fa7`  |
| 3335   | Layout 1 | `750353d48fa7`  |
| 3326   | Layout 1 | `750353d48fa7`  |
| 3321   | Layout 1 | `750353d48fa7`  |
| 3314   | Layout 1 | `750353d48fa7`  |
| 3303   | Layout 1 | `750353d48fa7`  |
| 3302   | Layout 1 | `750353d48fa7`  |
| 3293   | Layout 1 | `750353d48fa7`  |
| 3283   | Layout 1 | `750353d48fa7`  |
| 3275   | Layout 1 | `750353d48fa7`  |
| 3267   | Layout 1 | `750353d48fa7`  |
| 3258   | Layout 1 | `750353d48fa7`  |
| 3251   | Layout 1 | `750353d48fa7`  |
| 3242   | Layout 1 | `750353d48fa7`  |
| 3235   | Layout 1 | `750353d48fa7`  |
| 3229   | Layout 1 | `750353d48fa7`  |
| 3212   | Layout 1 | `750353d48fa7`  |
| 3203   | Layout 1 | `750353d48fa7`  |
| 3193   | Layout 1 | `750353d48fa7`  |
| 3186   | Layout 1 | `750353d48fa7`  |
| 3177   | Layout 1 | `750353d48fa7`  |
| 3169   | Layout 1 | `750353d48fa7`  |
| 3158   | Layout 1 | `750353d48fa7`  |
| 3151   | Layout 1 | `750353d48fa7`  |
| 3144   | Layout 1 | `750353d48fa7`  |
| 3133   | Layout 1 | `750353d48fa7`  |
| 3125   | Layout 1 | `750353d48fa7`  |
| 3118   | Layout 1 | `750353d48fa7`  |
| 3111   | Layout 1 | `750353d48fa7`  |
| 3103   | Layout 1 | `750353d48fa7`  |
| 3095   | Layout 1 | `750353d48fa7`  |
| 3086   | Layout 1 | `750353d48fa7`  |
| 3072   | Layout 1 | `750353d48fa7`  |
| 3062   | Layout 1 | `750353d48fa7`  |
| 3052   | Layout 1 | `750353d48fa7`  |
| 3045   | Layout 1 | `750353d48fa7`  |
| 3037   | Layout 1 | `750353d48fa7`  |
| 3030   | Layout 1 | `750353d48fa7`  |
| 3021   | Layout 1 | `750353d48fa7`  |
| 3012   | Layout 1 | `750353d48fa7`  |
| 3002   | Layout 1 | `750353d48fa7`  |
| 2995   | Layout 1 | `750353d48fa7`  |
| 2987   | Layout 1 | `750353d48fa7`  |
| 2978   | Layout 1 | `750353d48fa7`  |
| 2970   | Layout 1 | `750353d48fa7`  |
| 2959   | Layout 1 | `750353d48fa7`  |
| 2951   | Layout 1 | `750353d48fa7`  |
| 2942   | Layout 1 | `750353d48fa7`  |
| 2935   | Layout 1 | `750353d48fa7`  |
| 2932   | Layout 1 | `750353d48fa7`  |
| 2923   | Layout 1 | `750353d48fa7`  |
| 2919   | Layout 1 | `750353d48fa7`  |
| 2907   | Layout 1 | `750353d48fa7`  |
| 2900   | Layout 1 | `750353d48fa7`  |
| 2891   | Layout 1 | `750353d48fa7`  |
| 2882   | Layout 1 | `750353d48fa7`  |
| 2872   | Layout 1 | `750353d48fa7`  |
| 2863   | Layout 1 | `750353d48fa7`  |
| 2855   | Layout 1 | `750353d48fa7`  |
| 2849   | Layout 1 | `750353d48fa7`  |
| 2844   | Layout 1 | `750353d48fa7`  |
| 2834   | Layout 1 | `750353d48fa7`  |
| 2825   | Layout 1 | `750353d48fa7`  |
| 2819   | Layout 1 | `750353d48fa7`  |
| 2811   | Layout 1 | `750353d48fa7`  |
| 2803   | No file  | `750353d48fa7`  |
| 2794   | No file  | `750353d48fa7`  |
| 2783   | No file  | `750353d48fa7`  |
| 2774   | No file  | `750353d48fa7`  |
| 2765   | No file  | `750353d48fa7`  |
| 2756   | No file  | `750353d48fa7`  |
| 2750   | No file  | `750353d48fa7`  |
| 2743   | No file  | `750353d48fa7`  |
| 2736   | No file  | `750353d48fa7`  |
| 2726   | No file  | `750353d48fa7`  |
| 2717   | No file  | `750353d48fa7`  |
| 2709   | No file  | `750353d48fa7`  |
| 2703   | No file  | `750353d48fa7`  |
| 2695   | No file  | `750353d48fa7`  |
| 2684   | No file  | `750353d48fa7`  |
| 2672   | No file  | `750353d48fa7`  |
| 2665   | No file  | `750353d48fa7`  |
| 2657   | No file  | `750353d48fa7`  |
| 2649   | No file  | `750353d48fa7`  |
| 2644   | No file  | `750353d48fa7`  |
| 2637   | No file  | `750353d48fa7`  |
| 2629   | No file  | `750353d48fa7`  |
| 2619   | No file  | `750353d48fa7`  |
| 2612   | No file  | `750353d48fa7`  |
| 2606   | No file  | `750353d48fa7`  |
| 2602   | No file  | `750353d48fa7`  |
| 2601   | No file  | `750353d48fa7`  |
| 2592   | No file  | `750353d48fa7`  |
| 2583   | No file  | `750353d48fa7`  |
| 2575   | No file  | `750353d48fa7`  |
| 2567   | No file  | `750353d48fa7`  |
| 2560   | No file  | `750353d48fa7`  |
| 2553   | No file  | `750353d48fa7`  |
| 2545   | No file  | `750353d48fa7`  |
| 2538   | No file  | `750353d48fa7`  |
| 2529   | No file  | `750353d48fa7`  |
| 2519   | No file  | `750353d48fa7`  |
| 2513   | No file  | `750353d48fa7`  |
| 2510   | No file  | `750353d48fa7`  |
| 2507   | No file  | `750353d48fa7`  |
| 2503   | No file  | `750353d48fa7`  |
| 2498   | No file  | `750353d48fa7`  |
| 2492   | No file  | `750353d48fa7`  |
| 2487   | No file  | `750353d48fa7`  |
| 2480   | No file  | `750353d48fa7`  |
| 2474   | No file  | `750353d48fa7`  |
| 2468   | No file  | `750353d48fa7`  |
| 2460   | No file  | `750353d48fa7`  |
| 2453   | No file  | `750353d48fa7`  |
| 2444   | No file  | `750353d48fa7`  |
| 2438   | No file  | `750353d48fa7`  |
| 2434   | No file  | `750353d48fa7`  |
| 2429   | No file  | `750353d48fa7`  |
| 2421   | No file  | `750353d48fa7`  |
| 2414   | No file  | `750353d48fa7`  |
| 2407   | No file  | `750353d48fa7`  |
| 2401   | No file  | `750353d48fa7`  |
| 2397   | No file  | `750353d48fa7`  |
| 2393   | No file  | `750353d48fa7`  |
| 2384   | No file  | `750353d48fa7`  |
| 2378   | No file  | `750353d48fa7`  |
| 2372   | No file  | `750353d48fa7`  |
| 2358   | No file  | `750353d48fa7`  |
| 2352   | No file  | `750353d48fa7`  |
| 2347   | No file  | `750353d48fa7`  |
| 2343   | No file  | `750353d48fa7`  |
| 2335   | No file  | `750353d48fa7`  |
| 2327   | No file  | `750353d48fa7`  |
| 2324   | No file  | `750353d48fa7`  |
| 2319   | No file  | `750353d48fa7`  |
| 2313   | No file  | `750353d48fa7`  |
| 2308   | No file  | `750353d48fa7`  |
| 2302   | No file  | `750353d48fa7`  |
| 2295   | No file  | `750353d48fa7`  |
| 2290   | No file  | `750353d48fa7`  |
| 2284   | No file  | `750353d48fa7`  |
| 2276   | No file  | `750353d48fa7`  |
| 2269   | No file  | `750353d48fa7`  |
| 2259   | No file  | `750353d48fa7`  |
| 2250   | No file  | `750353d48fa7`  |
| 2243   | No file  | `750353d48fa7`  |
| 2235   | No file  | `750353d48fa7`  |
| 2229   | No file  | `750353d48fa7`  |
| 2224   | No file  | `750353d48fa7`  |
| 2218   | No file  | `750353d48fa7`  |
| 2215   | No file  | `750353d48fa7`  |
| 2207   | No file  | `750353d48fa7`  |
| 2203   | No file  | `750353d48fa7`  |
| 2196   | No file  | `750353d48fa7`  |
| 2192   | No file  | `750353d48fa7`  |
| 2189   | No file  | `750353d48fa7`  |
| 2183   | No file  | `750353d48fa7`  |
| 2179   | No file  | `750353d48fa7`  |
| 2171   | No file  | `750353d48fa7`  |
| 2163   | No file  | `750353d48fa7`  |
| 2156   | No file  | `750353d48fa7`  |
| 2151   | No file  | `750353d48fa7`  |
| 2147   | No file  | `750353d48fa7`  |
| 2142   | No file  | `750353d48fa7`  |
| 2138   | No file  | `750353d48fa7`  |
| 2134   | No file  | `750353d48fa7`  |
| 2130   | No file  | `750353d48fa7`  |
| 2122   | No file  | `750353d48fa7`  |
| 2107   | No file  | `750353d48fa7`  |
| 2098   | No file  | `750353d48fa7`  |
| 2089   | No file  | `750353d48fa7`  |
| 2081   | No file  | `750353d48fa7`  |
| 2073   | No file  | `750353d48fa7`  |
| 2067   | No file  | `750353d48fa7`  |
| 2063   | No file  | `750353d48fa7`  |
| 2059   | No file  | `750353d48fa7`  |
| 2052   | No file  | `750353d48fa7`  |
| 2044   | No file  | `750353d48fa7`  |
| 2039   | No file  | `750353d48fa7`  |
| 2032   | No file  | `750353d48fa7`  |
| 2025   | No file  | `750353d48fa7`  |
| 2011   | No file  | `750353d48fa7`  |
| 2005   | No file  | `750353d48fa7`  |
| 2000   | No file  | `750353d48fa7`  |
| 1996   | No file  | `750353d48fa7`  |
| 1991   | No file  | `750353d48fa7`  |
| 1985   | No file  | `750353d48fa7`  |
| 1980   | No file  | `750353d48fa7`  |
| 1969   | No file  | `750353d48fa7`  |
| 1964   | No file  | `750353d48fa7`  |
| 1958   | No file  | `750353d48fa7`  |
| 1950   | No file  | `750353d48fa7`  |
| 1945   | No file  | `750353d48fa7`  |
| 1937   | No file  | `750353d48fa7`  |
| 1933   | No file  | `750353d48fa7`  |
| 1927   | No file  | `750353d48fa7`  |
| 1921   | No file  | `750353d48fa7`  |
| 1914   | No file  | `750353d48fa7`  |
| 1908   | No file  | `750353d48fa7`  |
| 1897   | No file  | `750353d48fa7`  |
| 1892   | No file  | `750353d48fa7`  |
| 1886   | No file  | `750353d48fa7`  |
| 1881   | No file  | `750353d48fa7`  |
| 1871   | No file  | `750353d48fa7`  |
| 1866   | No file  | `750353d48fa7`  |
| 1862   | No file  | `750353d48fa7`  |
| 1854   | No file  | `750353d48fa7`  |
| 1846   | No file  | `750353d48fa7`  |
| 1838   | No file  | `750353d48fa7`  |
| 1832   | No file  | `750353d48fa7`  |
| 1826   | No file  | `750353d48fa7`  |
| 1822   | No file  | `750353d48fa7`  |
| 1818   | No file  | `750353d48fa7`  |
| 1804   | No file  | `750353d48fa7`  |
| 1794   | No file  | `750353d48fa7`  |
| 1790   | No file  | `750353d48fa7`  |
| 1784   | No file  | `750353d48fa7`  |
| 1774   | No file  | `750353d48fa7`  |
| 1771   | No file  | `750353d48fa7`  |
| 1762   | No file  | `750353d48fa7`  |
| 1759   | No file  | `750353d48fa7`  |
| 1754   | No file  | `750353d48fa7`  |
| 1749   | No file  | `750353d48fa7`  |
| 1743   | No file  | `750353d48fa7`  |
| 1737   | No file  | `750353d48fa7`  |
| 1731   | No file  | `750353d48fa7`  |
| 1725   | No file  | `750353d48fa7`  |
| 1717   | No file  | `750353d48fa7`  |
| 1710   | No file  | `750353d48fa7`  |
| 1704   | No file  | `750353d48fa7`  |
| 1698   | No file  | `750353d48fa7`  |
| 1690   | No file  | `750353d48fa7`  |
| 1685   | No file  | `750353d48fa7`  |
| 1680   | No file  | `750353d48fa7`  |
| 1674   | No file  | `750353d48fa7`  |
| 1668   | No file  | `750353d48fa7`  |
| 1659   | No file  | `750353d48fa7`  |
| 1649   | No file  | `750353d48fa7`  |
| 1642   | No file  | `750353d48fa7`  |
| 1636   | No file  | `750353d48fa7`  |
| 1628   | No file  | `750353d48fa7`  |
| 1622   | No file  | `750353d48fa7`  |
| 1614   | No file  | `750353d48fa7`  |
| 1608   | No file  | `750353d48fa7`  |
| 1602   | No file  | `750353d48fa7`  |
| 1598   | No file  | `750353d48fa7`  |
| 1594   | No file  | `750353d48fa7`  |
| 1590   | No file  | `750353d48fa7`  |
| 1587   | No file  | `750353d48fa7`  |
| 1584   | No file  | `750353d48fa7`  |
| 1579   | No file  | `750353d48fa7`  |
| 1572   | No file  | `750353d48fa7`  |
| 1565   | No file  | `750353d48fa7`  |
| 1559   | No file  | `750353d48fa7`  |
| 1554   | No file  | `750353d48fa7`  |
| 1547   | No file  | `750353d48fa7`  |
| 1537   | No file  | `750353d48fa7`  |
| 1529   | No file  | `750353d48fa7`  |
| 1524   | No file  | `750353d48fa7`  |
| 1519   | No file  | `750353d48fa7`  |
| 1509   | No file  | `750353d48fa7`  |
| 1506   | No file  | `750353d48fa7`  |
| 1504   | No file  | `750353d48fa7`  |
| 1500   | No file  | `750353d48fa7`  |
| 1493   | No file  | `750353d48fa7`  |
| 1489   | No file  | `750353d48fa7`  |
| 1485   | No file  | `750353d48fa7`  |
| 1481   | No file  | `750353d48fa7`  |
| 1474   | No file  | `750353d48fa7`  |
| 1466   | No file  | `750353d48fa7`  |
| 1462   | No file  | `750353d48fa7`  |
| 1459   | No file  | `750353d48fa7`  |
| 1453   | No file  | `750353d48fa7`  |
| 1450   | No file  | `750353d48fa7`  |
| 1445   | No file  | `750353d48fa7`  |
| 1439   | No file  | `750353d48fa7`  |
| 1433   | No file  | `750353d48fa7`  |
| 1430   | No file  | `750353d48fa7`  |
| 1426   | No file  | `750353d48fa7`  |
| 1421   | No file  | `750353d48fa7`  |
| 1417   | No file  | `750353d48fa7`  |
| 1416   | No file  | `750353d48fa7`  |
| 1409   | No file  | `750353d48fa7`  |
| 1405   | No file  | `750353d48fa7`  |
| 1401   | No file  | `750353d48fa7`  |
| 1396   | No file  | `750353d48fa7`  |
| 1391   | No file  | `750353d48fa7`  |
| 1390   | No file  | `750353d48fa7`  |
| 1386   | No file  | `750353d48fa7`  |
| 1381   | No file  | `750353d48fa7`  |
| 1379   | No file  | `750353d48fa7`  |
| 1372   | No file  | `750353d48fa7`  |
| 1366   | No file  | `750353d48fa7`  |
| 1364   | No file  | `750353d48fa7`  |
| 1363   | No file  | `750353d48fa7`  |
| 1360   | No file  | `750353d48fa7`  |
| 1358   | No file  | `750353d48fa7`  |
| 1355   | No file  | `750353d48fa7`  |
| 1351   | No file  | `750353d48fa7`  |
| 1348   | No file  | `750353d48fa7`  |
| 1346   | No file  | `750353d48fa7`  |
| 1341   | No file  | `750353d48fa7`  |
| 1340   | No file  | `750353d48fa7`  |
| 1338   | No file  | `750353d48fa7`  |
| 1335   | No file  | `750353d48fa7`  |
| 1333   | No file  | `750353d48fa7`  |
| 1329   | No file  | `750353d48fa7`  |
| 1327   | No file  | `750353d48fa7`  |
| 1324   | No file  | `750353d48fa7`  |
| 1321   | No file  | `750353d48fa7`  |
| 1319   | No file  | `750353d48fa7`  |
| 1318   | No file  | `750353d48fa7`  |
| 1316   | No file  | `750353d48fa7`  |
| 1313   | No file  | `750353d48fa7`  |
| 1311   | No file  | `750353d48fa7`  |
| 1309   | No file  | `750353d48fa7`  |
| 1304   | No file  | `750353d48fa7`  |
| 1292   | No file  | `750353d48fa7`  |
| 1286   | No file  | `750353d48fa7`  |
| 1280   | No file  | `750353d48fa7`  |
| 1276   | No file  | `750353d48fa7`  |
| 1267   | No file  | `750353d48fa7`  |
| 1261   | No file  | `750353d48fa7`  |
| 1256   | No file  | `750353d48fa7`  |
| 1250   | No file  | `750353d48fa7`  |
| 1246   | No file  | `750353d48fa7`  |
| 1239   | No file  | `750353d48fa7`  |
| 1230   | No file  | `750353d48fa7`  |
| 1226   | No file  | `750353d48fa7`  |
| 1220   | No file  | `750353d48fa7`  |
| 1217   | No file  | `750353d48fa7`  |
| 1211   | No file  | `750353d48fa7`  |
| 1210   | No file  | `750353d48fa7`  |
| 1208   | No file  | `750353d48fa7`  |
| 1203   | No file  | `750353d48fa7`  |
| 1197   | No file  | `750353d48fa7`  |
| 1194   | No file  | `750353d48fa7`  |
| 1192   | No file  | `750353d48fa7`  |
| 1187   | No file  | `750353d48fa7`  |
| 1183   | No file  | `750353d48fa7`  |
| 1177   | No file  | `750353d48fa7`  |
| 1173   | No file  | `750353d48fa7`  |
| 1167   | No file  | `750353d48fa7`  |
| 1164   | No file  | `750353d48fa7`  |
| 1156   | No file  | `750353d48fa7`  |
| 1149   | No file  | `750353d48fa7`  |
| 1144   | No file  | `750353d48fa7`  |
| 1137   | No file  | `750353d48fa7`  |
| 1132   | No file  | `750353d48fa7`  |
| 1127   | No file  | `750353d48fa7`  |
| 1122   | No file  | `750353d48fa7`  |
| 1118   | No file  | `750353d48fa7`  |
| 1114   | No file  | `750353d48fa7`  |
| 1109   | No file  | `750353d48fa7`  |
| 1102   | No file  | `750353d48fa7`  |
| 1096   | No file  | `750353d48fa7`  |
| 1088   | No file  | `750353d48fa7`  |
| 1081   | No file  | `750353d48fa7`  |
| 1076   | No file  | `750353d48fa7`  |
| 1069   | No file  | `750353d48fa7`  |
| 1064   | No file  | `750353d48fa7`  |
| 1058   | No file  | `750353d48fa7`  |
| 1051   | No file  | `750353d48fa7`  |
| 1044   | No file  | `750353d48fa7`  |
| 1036   | No file  | `750353d48fa7`  |
| 1026   | No file  | `750353d48fa7`  |
| 1016   | No file  | `750353d48fa7`  |
| 1009   | No file  | `750353d48fa7`  |
| 1005   | No file  | `750353d48fa7`  |
| 1000   | No file  | `750353d48fa7`  |
| 998    | No file  | `750353d48fa7`  |
| 990    | No file  | `750353d48fa7`  |
| 979    | No file  | `750353d48fa7`  |
| 972    | No file  | `750353d48fa7`  |
| 963    | No file  | `750353d48fa7`  |
| 955    | No file  | `750353d48fa7`  |
| 946    | No file  | `750353d48fa7`  |
| 938    | No file  | `750353d48fa7`  |
| 927    | No file  | `750353d48fa7`  |
| 911    | No file  | `750353d48fa7`  |
| 904    | No file  | `750353d48fa7`  |
| 899    | No file  | `750353d48fa7`  |
| 894    | No file  | `750353d48fa7`  |
| 885    | No file  | `750353d48fa7`  |
| 879    | No file  | `750353d48fa7`  |
| 872    | No file  | `750353d48fa7`  |
| 864    | No file  | `750353d48fa7`  |
| 855    | No file  | `750353d48fa7`  |
| 853    | No file  | `750353d48fa7`  |
| 845    | No file  | `750353d48fa7`  |
| 837    | No file  | `750353d48fa7`  |
| 829    | No file  | `750353d48fa7`  |
| 822    | No file  | `750353d48fa7`  |
| 814    | No file  | `750353d48fa7`  |
| 805    | No file  | `750353d48fa7`  |
| 794    | No file  | `750353d48fa7`  |
| 787    | No file  | `750353d48fa7`  |
| 780    | No file  | `750353d48fa7`  |
| 771    | No file  | `750353d48fa7`  |
| 760    | No file  | `750353d48fa7`  |
| 748    | No file  | `750353d48fa7`  |
| 741    | No file  | `750353d48fa7`  |
| 736    | No file  | `750353d48fa7`  |
| 731    | No file  | `750353d48fa7`  |
| 723    | No file  | `750353d48fa7`  |
| 711    | No file  | `750353d48fa7`  |
| 707    | No file  | `750353d48fa7`  |
| 697    | No file  | `750353d48fa7`  |
| 689    | No file  | `750353d48fa7`  |
| 683    | No file  | `750353d48fa7`  |
| 678    | No file  | `750353d48fa7`  |
| 670    | No file  | `750353d48fa7`  |
| 661    | No file  | `750353d48fa7`  |
| 656    | No file  | `750353d48fa7`  |
| 652    | No file  | `750353d48fa7`  |
| 643    | No file  | `750353d48fa7`  |
| 637    | No file  | `750353d48fa7`  |
| 630    | No file  | `750353d48fa7`  |
| 627    | No file  | `750353d48fa7`  |
| 621    | No file  | `750353d48fa7`  |
| 617    | No file  | `750353d48fa7`  |
| 615    | No file  | `750353d48fa7`  |
| 606    | No file  | `750353d48fa7`  |
| 599    | No file  | `750353d48fa7`  |
| 592    | No file  | `750353d48fa7`  |
| 586    | No file  | `750353d48fa7`  |
| 577    | No file  | `750353d48fa7`  |
| 569    | No file  | `750353d48fa7`  |
| 561    | No file  | `750353d48fa7`  |
| 554    | No file  | `750353d48fa7`  |
| 542    | No file  | `750353d48fa7`  |
| 532    | No file  | `750353d48fa7`  |
| 531    | No file  | `750353d48fa7`  |
| 526    | No file  | `750353d48fa7`  |
| 521    | No file  | `750353d48fa7`  |
| 517    | No file  | `750353d48fa7`  |
| 510    | No file  | `750353d48fa7`  |
| 508    | No file  | `750353d48fa7`  |
| 504    | No file  | `750353d48fa7`  |
| 497    | No file  | `750353d48fa7`  |
| 491    | No file  | `750353d48fa7`  |
| 485    | No file  | `750353d48fa7`  |
| 478    | No file  | `750353d48fa7`  |
| 472    | No file  | `750353d48fa7`  |
| 466    | No file  | `750353d48fa7`  |
| 457    | No file  | `750353d48fa7`  |
| 452    | No file  | `750353d48fa7`  |
| 449    | No file  | `750353d48fa7`  |
| 435    | No file  | `750353d48fa7`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6; item names, LOC type 0 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (98 bytes)

| Offset  | Type | Field                 | Notes                                                                           |
| ------- | ---- | --------------------- | ------------------------------------------------------------------------------- |
| `+0x00` | u32  | name_ref              | String table index of the field's Korean name (`name_kr`)                       |
| `+0x04` | f32  | unknown_04            | `-1171716.125` on both rows (client 3474); with `unknown_08` and `unknown_0c` one x, y, z point |
| `+0x08` | f32  | unknown_08            | `3134.306` on both rows                                                         |
| `+0x0C` | f32  | unknown_0c            | `1172652.125` on both rows                                                      |
| `+0x10` | f32  | unknown_10            | `-1163441` on both rows; with `unknown_14` and `unknown_18` a second point      |
| `+0x14` | f32  | unknown_14            | `3322` on both rows                                                             |
| `+0x18` | f32  | unknown_18            | `1169000` on both rows                                                          |
| `+0x1C` | f32  | unknown_1c            | `-1172216` on both rows; with `unknown_20` and `unknown_24` a third point       |
| `+0x20` | f32  | unknown_20            | `2934` on both rows                                                             |
| `+0x24` | f32  | unknown_24            | `1171490` on both rows                                                          |
| `+0x28` | u64  | unknown_28            | `43200000` on both rows (12 hours in milliseconds)                              |
| `+0x30` | u64  | unknown_30            | `14400000` on both rows (4 hours in milliseconds)                               |
| `+0x38` | u16  | npc_character_key     | `characterstatic.dbss` key: `62194` Munsik on both rows                          |
| `+0x3A` | u16  | monster_character_key | `characterstatic.dbss` key: `21948` Golden Pig, `24711` Golden Pigs             |
| `+0x3C` | u32  | summon_item_id        | Item ID: `56336` Rare Treasures, `1` on the second row; see Field Names         |
| `+0x40` | u32  | token_item_id         | Item ID: `56335` Golden Pigs Subjugation Token, `1` on the second row           |
| `+0x44` | u32  | unknown_44            | `0` on both rows                                                                |
| `+0x48` | u16  | unknown_48            | `0` on both rows                                                                |
| `+0x4A` | u32  | unknown_4a            | `1`, `2`                                                                        |
| `+0x4E` | u32  | unknown_4e            | `1`, `0`                                                                        |
| `+0x52` | u32  | unknown_52            | `400`, `999`                                                                    |
| `+0x56` | u32  | unknown_56            | `650`, `999`                                                                    |
| `+0x5A` | u32  | unknown_5a            | `100` on both rows                                                              |
| `+0x5E` | f32  | unknown_5e            | `13000` on both rows                                                            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                 |
| ------- | ------------------ | ------------ | ----------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `2` on client 3474                 |
| `+0x04` | pstr[string_count] | strings      | Wide Korean field names, `금돼지굴`, `금돼지굴(일반)` |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 covers
the file, which clients 1784 to 2519 do not ship. `name_ref` points to the
field name the relay widget shows with
`ToClient_GetCurrentPersonalRelayFieldName()`
(`panel_widget_personalfield_all`). `npc_character_key` and
`monster_character_key` resolve to LOC type 6 names: `62194` is Munsik with
the title Golden Pig Cave Subjugation, `21948` Golden Pig and `24711`
Golden Pigs, the monsters of the cave.

`summon_item_id` and `token_item_id` follow the LOC type 0 item names and
descriptions of the first row (client 3474), which
[bdocodex](https://bdocodex.com/us/item/56336/) shows the same: `56336`
Rare Treasures, "A magical item that summons rare treasures", used for
Golden Pig Cave Rare Treasures Summon, and `56335` Golden Pigs Subjugation
Token, "A token for clearing out the Golden Pig Cave", obtained from
Golden Pig Cave Subjugation
([bdocodex](https://bdocodex.com/us/item/56335/)). The second row, the
normal field, holds `1` in both (as an item, Silver), so what the fields
mean there is open.

## Notes

- The file is 250 bytes and the same on clients 3002, 3251 and 3474.
- The three points lie near x -1.17 million, z 1.17 million, outside the
  world map; which is the entry, the spawn or the exit is not known.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`:
  the Korean name, the two characters and the two items with icons.

## Open Questions

### Items of the Normal Field

What `summon_item_id` and `token_item_id` mean on the second row, the
normal field, where both are `1`. As item IDs that is Silver; it may also
mark a field without a summon item and token.

### Times and Counts

What `unknown_28` and `unknown_30` (12 and 4 hours as milliseconds) and
`unknown_4a` to `unknown_5e` hold. The second row, the normal field, has
`999` where the first has `400` and `650`, which fits a cap that the normal
field does not apply.
