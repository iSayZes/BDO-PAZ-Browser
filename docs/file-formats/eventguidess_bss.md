# `eventguidess.bss` Format

## Purpose

The events of the Event Guide window `Panel_EventGuide_Total`: on client
3482 162 events, from the current Halloween world boss back to the
Blackstar gift of 2023. Each event has a Korean title, page text and
period text, a list icon and a page background texture, its UTC start and
end, the keyword of its web page, an optional button that opens a UI
window, a Hot or New tag, its event key and the reward items it shows. The
Lua lists the events whose end is still ahead
(`eventGuideSS:isEnd(getServerUtc64())`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records | Row bytes                  |
| ------ | -------------- | ------- | ------------------ | ------ | ------- | -------------------------- |
| 2      | 3012 and later | 3483    | `eventguidess.bss` | 77,912 | 162 Row | 375 to 623, 481 on average |
| 1      | 3002           | 3002    | `eventguidess.bss` | 6,579  | 15 Row  | 388 to 504, 438 on average |

| Layout | File               | Known             | Unknown    |
| ------ | ------------------ | ----------------- | ---------- |
| 2      | `eventguidess.bss` | 77,912 B (100.0%) | 0 B (0.0%) |
| 1      | `eventguidess.bss` | 6,579 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `14362dc97a90`  |
| 3482   | Layout 2 | `14362dc97a90`  |
| 3474   | Layout 2 | `14362dc97a90`  |
| 3473   | Layout 2 | `14362dc97a90`  |
| 3464   | Layout 2 | `14362dc97a90`  |
| 3458   | Layout 2 | `14362dc97a90`  |
| 3454   | Layout 2 | `14362dc97a90`  |
| 3444   | Layout 2 | `14362dc97a90`  |
| 3435   | Layout 2 | `14362dc97a90`  |
| 3426   | Layout 2 | `14362dc97a90`  |
| 3418   | Layout 2 | `14362dc97a90`  |
| 3412   | Layout 2 | `14362dc97a90`  |
| 3402   | Layout 2 | `14362dc97a90`  |
| 3396   | Layout 2 | `14362dc97a90`  |
| 3387   | Layout 2 | `14362dc97a90`  |
| 3381   | Layout 2 | `14362dc97a90`  |
| 3373   | Layout 2 | `14362dc97a90`  |
| 3364   | Layout 2 | `14362dc97a90`  |
| 3356   | Layout 2 | `14362dc97a90`  |
| 3349   | Layout 2 | `14362dc97a90`  |
| 3342   | Layout 2 | `14362dc97a90`  |
| 3335   | Layout 2 | `14362dc97a90`  |
| 3326   | Layout 2 | `14362dc97a90`  |
| 3321   | Layout 2 | `14362dc97a90`  |
| 3314   | Layout 2 | `14362dc97a90`  |
| 3303   | Layout 2 | `14362dc97a90`  |
| 3302   | Layout 2 | `14362dc97a90`  |
| 3293   | Layout 2 | `14362dc97a90`  |
| 3283   | Layout 2 | `14362dc97a90`  |
| 3275   | Layout 2 | `14362dc97a90`  |
| 3267   | Layout 2 | `14362dc97a90`  |
| 3258   | Layout 2 | `14362dc97a90`  |
| 3251   | Layout 2 | `14362dc97a90`  |
| 3242   | Layout 2 | `14362dc97a90`  |
| 3235   | Layout 2 | `14362dc97a90`  |
| 3229   | Layout 2 | `14362dc97a90`  |
| 3212   | Layout 2 | `14362dc97a90`  |
| 3203   | Layout 2 | `14362dc97a90`  |
| 3193   | Layout 2 | `14362dc97a90`  |
| 3186   | Layout 2 | `14362dc97a90`  |
| 3177   | Layout 2 | `14362dc97a90`  |
| 3169   | Layout 2 | `14362dc97a90`  |
| 3158   | Layout 2 | `14362dc97a90`  |
| 3151   | Layout 2 | `14362dc97a90`  |
| 3144   | Layout 2 | `14362dc97a90`  |
| 3133   | Layout 2 | `14362dc97a90`  |
| 3125   | Layout 2 | `14362dc97a90`  |
| 3118   | Layout 2 | `14362dc97a90`  |
| 3111   | Layout 2 | `14362dc97a90`  |
| 3103   | Layout 2 | `14362dc97a90`  |
| 3095   | Layout 2 | `14362dc97a90`  |
| 3086   | Layout 2 | `14362dc97a90`  |
| 3072   | Layout 2 | `14362dc97a90`  |
| 3062   | Layout 2 | `14362dc97a90`  |
| 3052   | Layout 2 | `14362dc97a90`  |
| 3045   | Layout 2 | `14362dc97a90`  |
| 3037   | Layout 2 | `14362dc97a90`  |
| 3030   | Layout 2 | `14362dc97a90`  |
| 3021   | Layout 2 | `14362dc97a90`  |
| 3012   | Layout 2 | `14362dc97a90`  |
| 3002   | Layout 1 | `14362dc97a90`  |
| 2995   | No file  | `14362dc97a90`  |
| 2987   | No file  | `14362dc97a90`  |
| 2978   | No file  | `14362dc97a90`  |
| 2970   | No file  | `14362dc97a90`  |
| 2959   | No file  | `14362dc97a90`  |
| 2951   | No file  | `14362dc97a90`  |
| 2942   | No file  | `14362dc97a90`  |
| 2935   | No file  | `14362dc97a90`  |
| 2932   | No file  | `14362dc97a90`  |
| 2923   | No file  | `14362dc97a90`  |
| 2919   | No file  | `14362dc97a90`  |
| 2907   | No file  | `14362dc97a90`  |
| 2900   | No file  | `14362dc97a90`  |
| 2891   | No file  | `14362dc97a90`  |
| 2882   | No file  | `14362dc97a90`  |
| 2872   | No file  | `14362dc97a90`  |
| 2863   | No file  | `14362dc97a90`  |
| 2855   | No file  | `14362dc97a90`  |
| 2849   | No file  | `14362dc97a90`  |
| 2844   | No file  | `14362dc97a90`  |
| 2834   | No file  | `14362dc97a90`  |
| 2825   | No file  | `14362dc97a90`  |
| 2819   | No file  | `14362dc97a90`  |
| 2811   | No file  | `14362dc97a90`  |
| 2803   | No file  | `14362dc97a90`  |
| 2794   | No file  | `14362dc97a90`  |
| 2783   | No file  | `14362dc97a90`  |
| 2774   | No file  | `14362dc97a90`  |
| 2765   | No file  | `14362dc97a90`  |
| 2756   | No file  | `14362dc97a90`  |
| 2750   | No file  | `14362dc97a90`  |
| 2743   | No file  | `14362dc97a90`  |
| 2736   | No file  | `14362dc97a90`  |
| 2726   | No file  | `14362dc97a90`  |
| 2717   | No file  | `14362dc97a90`  |
| 2709   | No file  | `14362dc97a90`  |
| 2703   | No file  | `14362dc97a90`  |
| 2695   | No file  | `14362dc97a90`  |
| 2684   | No file  | `14362dc97a90`  |
| 2672   | No file  | `14362dc97a90`  |
| 2665   | No file  | `14362dc97a90`  |
| 2657   | No file  | `14362dc97a90`  |
| 2649   | No file  | `14362dc97a90`  |
| 2644   | No file  | `14362dc97a90`  |
| 2637   | No file  | `14362dc97a90`  |
| 2629   | No file  | `14362dc97a90`  |
| 2619   | No file  | `14362dc97a90`  |
| 2612   | No file  | `14362dc97a90`  |
| 2606   | No file  | `14362dc97a90`  |
| 2602   | No file  | `14362dc97a90`  |
| 2601   | No file  | `14362dc97a90`  |
| 2592   | No file  | `14362dc97a90`  |
| 2583   | No file  | `14362dc97a90`  |
| 2575   | No file  | `14362dc97a90`  |
| 2567   | No file  | `14362dc97a90`  |
| 2560   | No file  | `14362dc97a90`  |
| 2553   | No file  | `14362dc97a90`  |
| 2545   | No file  | `14362dc97a90`  |
| 2538   | No file  | `14362dc97a90`  |
| 2529   | No file  | `14362dc97a90`  |
| 2519   | No file  | `14362dc97a90`  |
| 2513   | No file  | `14362dc97a90`  |
| 2510   | No file  | `14362dc97a90`  |
| 2507   | No file  | `14362dc97a90`  |
| 2503   | No file  | `14362dc97a90`  |
| 2498   | No file  | `14362dc97a90`  |
| 2492   | No file  | `14362dc97a90`  |
| 2487   | No file  | `14362dc97a90`  |
| 2480   | No file  | `14362dc97a90`  |
| 2474   | No file  | `14362dc97a90`  |
| 2468   | No file  | `14362dc97a90`  |
| 2460   | No file  | `14362dc97a90`  |
| 2453   | No file  | `14362dc97a90`  |
| 2444   | No file  | `14362dc97a90`  |
| 2438   | No file  | `14362dc97a90`  |
| 2434   | No file  | `14362dc97a90`  |
| 2429   | No file  | `14362dc97a90`  |
| 2421   | No file  | `14362dc97a90`  |
| 2414   | No file  | `14362dc97a90`  |
| 2407   | No file  | `14362dc97a90`  |
| 2401   | No file  | `14362dc97a90`  |
| 2397   | No file  | `14362dc97a90`  |
| 2393   | No file  | `14362dc97a90`  |
| 2384   | No file  | `14362dc97a90`  |
| 2378   | No file  | `14362dc97a90`  |
| 2372   | No file  | `14362dc97a90`  |
| 2358   | No file  | `14362dc97a90`  |
| 2352   | No file  | `14362dc97a90`  |
| 2347   | No file  | `14362dc97a90`  |
| 2343   | No file  | `14362dc97a90`  |
| 2335   | No file  | `14362dc97a90`  |
| 2327   | No file  | `14362dc97a90`  |
| 2324   | No file  | `14362dc97a90`  |
| 2319   | No file  | `14362dc97a90`  |
| 2313   | No file  | `14362dc97a90`  |
| 2308   | No file  | `14362dc97a90`  |
| 2302   | No file  | `14362dc97a90`  |
| 2295   | No file  | `14362dc97a90`  |
| 2290   | No file  | `14362dc97a90`  |
| 2284   | No file  | `14362dc97a90`  |
| 2276   | No file  | `14362dc97a90`  |
| 2269   | No file  | `14362dc97a90`  |
| 2259   | No file  | `14362dc97a90`  |
| 2250   | No file  | `14362dc97a90`  |
| 2243   | No file  | `14362dc97a90`  |
| 2235   | No file  | `14362dc97a90`  |
| 2229   | No file  | `14362dc97a90`  |
| 2224   | No file  | `14362dc97a90`  |
| 2218   | No file  | `14362dc97a90`  |
| 2215   | No file  | `14362dc97a90`  |
| 2207   | No file  | `14362dc97a90`  |
| 2203   | No file  | `14362dc97a90`  |
| 2196   | No file  | `14362dc97a90`  |
| 2192   | No file  | `14362dc97a90`  |
| 2189   | No file  | `14362dc97a90`  |
| 2183   | No file  | `14362dc97a90`  |
| 2179   | No file  | `14362dc97a90`  |
| 2171   | No file  | `14362dc97a90`  |
| 2163   | No file  | `14362dc97a90`  |
| 2156   | No file  | `14362dc97a90`  |
| 2151   | No file  | `14362dc97a90`  |
| 2147   | No file  | `14362dc97a90`  |
| 2142   | No file  | `14362dc97a90`  |
| 2138   | No file  | `14362dc97a90`  |
| 2134   | No file  | `14362dc97a90`  |
| 2130   | No file  | `14362dc97a90`  |
| 2122   | No file  | `14362dc97a90`  |
| 2107   | No file  | `14362dc97a90`  |
| 2098   | No file  | `14362dc97a90`  |
| 2089   | No file  | `14362dc97a90`  |
| 2081   | No file  | `14362dc97a90`  |
| 2073   | No file  | `14362dc97a90`  |
| 2067   | No file  | `14362dc97a90`  |
| 2063   | No file  | `14362dc97a90`  |
| 2059   | No file  | `14362dc97a90`  |
| 2052   | No file  | `14362dc97a90`  |
| 2044   | No file  | `14362dc97a90`  |
| 2039   | No file  | `14362dc97a90`  |
| 2032   | No file  | `14362dc97a90`  |
| 2025   | No file  | `14362dc97a90`  |
| 2011   | No file  | `14362dc97a90`  |
| 2005   | No file  | `14362dc97a90`  |
| 2000   | No file  | `14362dc97a90`  |
| 1996   | No file  | `14362dc97a90`  |
| 1991   | No file  | `14362dc97a90`  |
| 1985   | No file  | `14362dc97a90`  |
| 1980   | No file  | `14362dc97a90`  |
| 1969   | No file  | `14362dc97a90`  |
| 1964   | No file  | `14362dc97a90`  |
| 1958   | No file  | `14362dc97a90`  |
| 1950   | No file  | `14362dc97a90`  |
| 1945   | No file  | `14362dc97a90`  |
| 1937   | No file  | `14362dc97a90`  |
| 1933   | No file  | `14362dc97a90`  |
| 1927   | No file  | `14362dc97a90`  |
| 1921   | No file  | `14362dc97a90`  |
| 1914   | No file  | `14362dc97a90`  |
| 1908   | No file  | `14362dc97a90`  |
| 1897   | No file  | `14362dc97a90`  |
| 1892   | No file  | `14362dc97a90`  |
| 1886   | No file  | `14362dc97a90`  |
| 1881   | No file  | `14362dc97a90`  |
| 1871   | No file  | `14362dc97a90`  |
| 1866   | No file  | `14362dc97a90`  |
| 1862   | No file  | `14362dc97a90`  |
| 1854   | No file  | `14362dc97a90`  |
| 1846   | No file  | `14362dc97a90`  |
| 1838   | No file  | `14362dc97a90`  |
| 1832   | No file  | `14362dc97a90`  |
| 1826   | No file  | `14362dc97a90`  |
| 1822   | No file  | `14362dc97a90`  |
| 1818   | No file  | `14362dc97a90`  |
| 1804   | No file  | `14362dc97a90`  |
| 1794   | No file  | `14362dc97a90`  |
| 1790   | No file  | `14362dc97a90`  |
| 1784   | No file  | `14362dc97a90`  |
| 1774   | No file  | `14362dc97a90`  |
| 1771   | No file  | `14362dc97a90`  |
| 1762   | No file  | `14362dc97a90`  |
| 1759   | No file  | `14362dc97a90`  |
| 1754   | No file  | `14362dc97a90`  |
| 1749   | No file  | `14362dc97a90`  |
| 1743   | No file  | `14362dc97a90`  |
| 1737   | No file  | `14362dc97a90`  |
| 1731   | No file  | `14362dc97a90`  |
| 1725   | No file  | `14362dc97a90`  |
| 1717   | No file  | `14362dc97a90`  |
| 1710   | No file  | `14362dc97a90`  |
| 1704   | No file  | `14362dc97a90`  |
| 1698   | No file  | `14362dc97a90`  |
| 1690   | No file  | `14362dc97a90`  |
| 1685   | No file  | `14362dc97a90`  |
| 1680   | No file  | `14362dc97a90`  |
| 1674   | No file  | `14362dc97a90`  |
| 1668   | No file  | `14362dc97a90`  |
| 1659   | No file  | `14362dc97a90`  |
| 1649   | No file  | `14362dc97a90`  |
| 1642   | No file  | `14362dc97a90`  |
| 1636   | No file  | `14362dc97a90`  |
| 1628   | No file  | `14362dc97a90`  |
| 1622   | No file  | `14362dc97a90`  |
| 1614   | No file  | `14362dc97a90`  |
| 1608   | No file  | `14362dc97a90`  |
| 1602   | No file  | `14362dc97a90`  |
| 1598   | No file  | `14362dc97a90`  |
| 1594   | No file  | `14362dc97a90`  |
| 1590   | No file  | `14362dc97a90`  |
| 1587   | No file  | `14362dc97a90`  |
| 1584   | No file  | `14362dc97a90`  |
| 1579   | No file  | `14362dc97a90`  |
| 1572   | No file  | `14362dc97a90`  |
| 1565   | No file  | `14362dc97a90`  |
| 1559   | No file  | `14362dc97a90`  |
| 1554   | No file  | `14362dc97a90`  |
| 1547   | No file  | `14362dc97a90`  |
| 1537   | No file  | `14362dc97a90`  |
| 1529   | No file  | `14362dc97a90`  |
| 1524   | No file  | `14362dc97a90`  |
| 1519   | No file  | `14362dc97a90`  |
| 1509   | No file  | `14362dc97a90`  |
| 1506   | No file  | `14362dc97a90`  |
| 1504   | No file  | `14362dc97a90`  |
| 1500   | No file  | `14362dc97a90`  |
| 1493   | No file  | `14362dc97a90`  |
| 1489   | No file  | `14362dc97a90`  |
| 1485   | No file  | `14362dc97a90`  |
| 1481   | No file  | `14362dc97a90`  |
| 1474   | No file  | `14362dc97a90`  |
| 1466   | No file  | `14362dc97a90`  |
| 1462   | No file  | `14362dc97a90`  |
| 1459   | No file  | `14362dc97a90`  |
| 1453   | No file  | `14362dc97a90`  |
| 1450   | No file  | `14362dc97a90`  |
| 1445   | No file  | `14362dc97a90`  |
| 1439   | No file  | `14362dc97a90`  |
| 1433   | No file  | `14362dc97a90`  |
| 1430   | No file  | `14362dc97a90`  |
| 1426   | No file  | `14362dc97a90`  |
| 1421   | No file  | `14362dc97a90`  |
| 1417   | No file  | `14362dc97a90`  |
| 1416   | No file  | `14362dc97a90`  |
| 1409   | No file  | `14362dc97a90`  |
| 1405   | No file  | `14362dc97a90`  |
| 1401   | No file  | `14362dc97a90`  |
| 1396   | No file  | `14362dc97a90`  |
| 1391   | No file  | `14362dc97a90`  |
| 1390   | No file  | `14362dc97a90`  |
| 1386   | No file  | `14362dc97a90`  |
| 1381   | No file  | `14362dc97a90`  |
| 1379   | No file  | `14362dc97a90`  |
| 1372   | No file  | `14362dc97a90`  |
| 1366   | No file  | `14362dc97a90`  |
| 1364   | No file  | `14362dc97a90`  |
| 1363   | No file  | `14362dc97a90`  |
| 1360   | No file  | `14362dc97a90`  |
| 1358   | No file  | `14362dc97a90`  |
| 1355   | No file  | `14362dc97a90`  |
| 1351   | No file  | `14362dc97a90`  |
| 1348   | No file  | `14362dc97a90`  |
| 1346   | No file  | `14362dc97a90`  |
| 1341   | No file  | `14362dc97a90`  |
| 1340   | No file  | `14362dc97a90`  |
| 1338   | No file  | `14362dc97a90`  |
| 1335   | No file  | `14362dc97a90`  |
| 1333   | No file  | `14362dc97a90`  |
| 1329   | No file  | `14362dc97a90`  |
| 1327   | No file  | `14362dc97a90`  |
| 1324   | No file  | `14362dc97a90`  |
| 1321   | No file  | `14362dc97a90`  |
| 1319   | No file  | `14362dc97a90`  |
| 1318   | No file  | `14362dc97a90`  |
| 1316   | No file  | `14362dc97a90`  |
| 1313   | No file  | `14362dc97a90`  |
| 1311   | No file  | `14362dc97a90`  |
| 1309   | No file  | `14362dc97a90`  |
| 1304   | No file  | `14362dc97a90`  |
| 1292   | No file  | `14362dc97a90`  |
| 1286   | No file  | `14362dc97a90`  |
| 1280   | No file  | `14362dc97a90`  |
| 1276   | No file  | `14362dc97a90`  |
| 1267   | No file  | `14362dc97a90`  |
| 1261   | No file  | `14362dc97a90`  |
| 1256   | No file  | `14362dc97a90`  |
| 1250   | No file  | `14362dc97a90`  |
| 1246   | No file  | `14362dc97a90`  |
| 1239   | No file  | `14362dc97a90`  |
| 1230   | No file  | `14362dc97a90`  |
| 1226   | No file  | `14362dc97a90`  |
| 1220   | No file  | `14362dc97a90`  |
| 1217   | No file  | `14362dc97a90`  |
| 1211   | No file  | `14362dc97a90`  |
| 1210   | No file  | `14362dc97a90`  |
| 1208   | No file  | `14362dc97a90`  |
| 1203   | No file  | `14362dc97a90`  |
| 1197   | No file  | `14362dc97a90`  |
| 1194   | No file  | `14362dc97a90`  |
| 1192   | No file  | `14362dc97a90`  |
| 1187   | No file  | `14362dc97a90`  |
| 1183   | No file  | `14362dc97a90`  |
| 1177   | No file  | `14362dc97a90`  |
| 1173   | No file  | `14362dc97a90`  |
| 1167   | No file  | `14362dc97a90`  |
| 1164   | No file  | `14362dc97a90`  |
| 1156   | No file  | `14362dc97a90`  |
| 1149   | No file  | `14362dc97a90`  |
| 1144   | No file  | `14362dc97a90`  |
| 1137   | No file  | `14362dc97a90`  |
| 1132   | No file  | `14362dc97a90`  |
| 1127   | No file  | `14362dc97a90`  |
| 1122   | No file  | `14362dc97a90`  |
| 1118   | No file  | `14362dc97a90`  |
| 1114   | No file  | `14362dc97a90`  |
| 1109   | No file  | `14362dc97a90`  |
| 1102   | No file  | `14362dc97a90`  |
| 1096   | No file  | `14362dc97a90`  |
| 1088   | No file  | `14362dc97a90`  |
| 1081   | No file  | `14362dc97a90`  |
| 1076   | No file  | `14362dc97a90`  |
| 1069   | No file  | `14362dc97a90`  |
| 1064   | No file  | `14362dc97a90`  |
| 1058   | No file  | `14362dc97a90`  |
| 1051   | No file  | `14362dc97a90`  |
| 1044   | No file  | `14362dc97a90`  |
| 1036   | No file  | `14362dc97a90`  |
| 1026   | No file  | `14362dc97a90`  |
| 1016   | No file  | `14362dc97a90`  |
| 1009   | No file  | `14362dc97a90`  |
| 1005   | No file  | `14362dc97a90`  |
| 1000   | No file  | `14362dc97a90`  |
| 998    | No file  | `14362dc97a90`  |
| 990    | No file  | `14362dc97a90`  |
| 979    | No file  | `14362dc97a90`  |
| 972    | No file  | `14362dc97a90`  |
| 963    | No file  | `14362dc97a90`  |
| 955    | No file  | `14362dc97a90`  |
| 946    | No file  | `14362dc97a90`  |
| 938    | No file  | `14362dc97a90`  |
| 927    | No file  | `14362dc97a90`  |
| 911    | No file  | `14362dc97a90`  |
| 904    | No file  | `14362dc97a90`  |
| 899    | No file  | `14362dc97a90`  |
| 894    | No file  | `14362dc97a90`  |
| 885    | No file  | `14362dc97a90`  |
| 879    | No file  | `14362dc97a90`  |
| 872    | No file  | `14362dc97a90`  |
| 864    | No file  | `14362dc97a90`  |
| 855    | No file  | `14362dc97a90`  |
| 853    | No file  | `14362dc97a90`  |
| 845    | No file  | `14362dc97a90`  |
| 837    | No file  | `14362dc97a90`  |
| 829    | No file  | `14362dc97a90`  |
| 822    | No file  | `14362dc97a90`  |
| 814    | No file  | `14362dc97a90`  |
| 805    | No file  | `14362dc97a90`  |
| 794    | No file  | `14362dc97a90`  |
| 787    | No file  | `14362dc97a90`  |
| 780    | No file  | `14362dc97a90`  |
| 771    | No file  | `14362dc97a90`  |
| 760    | No file  | `14362dc97a90`  |
| 748    | No file  | `14362dc97a90`  |
| 741    | No file  | `14362dc97a90`  |
| 736    | No file  | `14362dc97a90`  |
| 731    | No file  | `14362dc97a90`  |
| 723    | No file  | `14362dc97a90`  |
| 711    | No file  | `14362dc97a90`  |
| 707    | No file  | `14362dc97a90`  |
| 697    | No file  | `14362dc97a90`  |
| 689    | No file  | `14362dc97a90`  |
| 683    | No file  | `14362dc97a90`  |
| 678    | No file  | `14362dc97a90`  |
| 670    | No file  | `14362dc97a90`  |
| 661    | No file  | `14362dc97a90`  |
| 656    | No file  | `14362dc97a90`  |
| 652    | No file  | `14362dc97a90`  |
| 643    | No file  | `14362dc97a90`  |
| 637    | No file  | `14362dc97a90`  |
| 630    | No file  | `14362dc97a90`  |
| 627    | No file  | `14362dc97a90`  |
| 621    | No file  | `14362dc97a90`  |
| 617    | No file  | `14362dc97a90`  |
| 615    | No file  | `14362dc97a90`  |
| 606    | No file  | `14362dc97a90`  |
| 599    | No file  | `14362dc97a90`  |
| 592    | No file  | `14362dc97a90`  |
| 586    | No file  | `14362dc97a90`  |
| 577    | No file  | `14362dc97a90`  |
| 569    | No file  | `14362dc97a90`  |
| 561    | No file  | `14362dc97a90`  |
| 554    | No file  | `14362dc97a90`  |
| 542    | No file  | `14362dc97a90`  |
| 532    | No file  | `14362dc97a90`  |
| 531    | No file  | `14362dc97a90`  |
| 526    | No file  | `14362dc97a90`  |
| 521    | No file  | `14362dc97a90`  |
| 517    | No file  | `14362dc97a90`  |
| 510    | No file  | `14362dc97a90`  |
| 508    | No file  | `14362dc97a90`  |
| 504    | No file  | `14362dc97a90`  |
| 497    | No file  | `14362dc97a90`  |
| 491    | No file  | `14362dc97a90`  |
| 485    | No file  | `14362dc97a90`  |
| 478    | No file  | `14362dc97a90`  |
| 472    | No file  | `14362dc97a90`  |
| 466    | No file  | `14362dc97a90`  |
| 457    | No file  | `14362dc97a90`  |
| 452    | No file  | `14362dc97a90`  |
| 449    | No file  | `14362dc97a90`  |
| 435    | No file  | `14362dc97a90`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone; it shows the icon from
`texturestring_combine.xml` when that file is there.

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type       | Field | Notes                                  |
| ------- | ---------- | ----- | -------------------------------------- |
| `+0x00` | u32        | count | Number of events; `162` on client 3482 |
| `+0x04` | Row[count] | rows  | See Row                                |

### Row (variable: 105 bytes + texts and rewards)

| Offset                  | Type                 | Field            | Notes |
| ----------------------- | -------------------- | ---------------- | ----- |
| `+0x00`                 | str16                | main_title_kr    | `getMainTitle()`: Korean event name in the list |
| `main_title_kr+0x00`    | str16                | main_desc_kr     | `getMainDesc()`: Korean headline of the page; the same text as `main_title_kr` on all 162 rows. See Open Questions |
| `main_desc_kr+0x00`     | str16                | sub_desc_kr      | `getSubDesc()`: Korean page text |
| `sub_desc_kr+0x00`      | str16                | period_desc_kr   | `getPeriodDesc()`: Korean period text (`2026년 10월 22일(목) 정기점검 후 ~ ...`) |
| `period_desc_kr+0x00`   | str8                 | icon             | `getIcon()`: UI texture ID of the list icon (`Combine_Tab_Icon_Daily_Select`) |
| `icon+0x00`             | str8                 | texture_bg       | `getTextureBg()`: UI texture ID of the page background (`Combine_Etc_Event_Halloween12`) |
| `texture_bg+0x00`       | u64                  | start_time       | Event start, UTC Unix seconds |
| `texture_bg+0x08`       | u64                  | end_time         | Event end, UTC Unix seconds; `isEnd()` compares it with the server time. 2099-12-31 23:59 on 5 rows |
| `texture_bg+0x10`       | str8                 | web_keyword      | `getWebKeyword()`: web page keyword, the event's date and number (`2610210002`) |
| `web_keyword+0x00`      | str8                 | web_hash_id      | `getWebHashID()`; empty on all 162 rows |
| `web_hash_id+0x00`      | str8                 | function         | Script of the page button, `ToClient_RequestEventGuideFunctionAt()` (`openui(newquest)`, `openui(cashshop)`); empty on 58 rows, `isFunctionEmpty()` |
| `function+0x00`         | str16                | function_desc_kr | `getFunctionDesc()`: Korean button text (`신규 의뢰 바로가기`) |
| `function_desc_kr+0x00` | u8                   | tag              | `getTag()`: `__eEventGuideTag_Hot`, `__eEventGuideTag_New` or none; `0` on 154 rows, `1` on 1, `2` on 7 |
| `function_desc_kr+0x01` | u32                  | event_key        | Event key, unique; `1` to `230` on client 3482 |
| `function_desc_kr+0x05` | u32                  | reward_count     | `getRewardCount()`; `0` to `7` |
| `function_desc_kr+0x09` | u32[reward_count]    | rewards          | `getRewardAt(i)`: item keys |

## Layout 1

Layout 2 without `function_desc_kr`.

### Row (variable: 97 bytes + texts and rewards)

| Offset                | Type              | Field          | Notes |
| --------------------- | ----------------- | -------------- | ----- |
| `+0x00`               | str16             | main_title_kr  |       |
| `main_title_kr+0x00`  | str16             | main_desc_kr   |       |
| `main_desc_kr+0x00`   | str16             | sub_desc_kr    |       |
| `sub_desc_kr+0x00`    | str16             | period_desc_kr |       |
| `period_desc_kr+0x00` | str8              | icon           |       |
| `icon+0x00`           | str8              | texture_bg     |       |
| `texture_bg+0x00`     | u64               | start_time     |       |
| `texture_bg+0x08`     | u64               | end_time       |       |
| `texture_bg+0x10`     | str8              | web_keyword    |       |
| `web_keyword+0x00`    | str8              | web_hash_id    |       |
| `web_hash_id+0x00`    | str8              | function       |       |
| `function+0x00`       | u8                | tag            |       |
| `function+0x01`       | u32               | event_key      |       |
| `function+0x05`       | u32               | reward_count   |       |
| `function+0x09`       | u32[reward_count] | rewards        |       |

## Field Names

The names follow the getters `panel_eventguide_total_1.luac` and
`panel_eventguide_total_2.luac` (client 3482) call on
`ToClient_RequestEventGuideAt(index)`: `getMainTitle()`, `getMainDesc()`,
`getSubDesc()`, `getPeriodDesc()`, `getIcon()`, `getTextureBg()`,
`isEnd(time)`, `getWebKeyword()`, `getWebHashID()`, `isFunctionEmpty()`,
`getFunctionDesc()`, `getTag()`, `getRewardCount()` and `getRewardAt(i)`.
`start_time` and `end_time` are told apart by their order and by the
period text: the first row's `2026-10-22 09:00` to `2026-11-05 09:00`
UTC are the maintenance times its `period_desc_kr` names. Client 1784 has
no file and no matching sheet.

## Notes

- On client 3482 the first row holds event key `230` and the last key
  `1`; past events stay in the file and the Lua hides them.
- Some rows have a `function_desc_kr` and an empty `function`;
  `isFunctionEmpty()` hides their button.

## Open Questions

### Title and Main Description Order

`main_title_kr` and `main_desc_kr` hold the same text on every row of
clients 3251 and 3482, so the data does not show which of the two
`getMainTitle()` reads.

### Tag Values

`tag` is `1` on one row and `2` on seven. The Lua compares it with
`__eEventGuideTag_Hot` and `__eEventGuideTag_New`, whose values are set
by the client exe.
