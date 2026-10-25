# `journalinfostaticstatus.bss` Format

## Purpose

The main quest boards of `Panel_Window_Journal_All`: on client 3482 two
journal lists, Morning Land (27 journals) and Edania (14). Each journal is
one boss or castle card of a board page: its chapter tab, its UI type and
place on the page, the quest chain it tracks, the `GAME` sheet keys of its
chapter, title and story text, its card and button textures, the
bookshelf quest it opens once cleared (chosen by condition), and the
textures it switches to as its quests are cleared. After the lists come 21
texture IDs and string keys per list for the board frame, the page and the
book view. The Lua reads a journal with
`ToClient_getJournalInfo(list, chapter, uiTypeIndex, journal)` and the list
textures with `ToClient_getJournalTextureInfo(list, slot)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes  | Records                                                                                    | Row bytes |
| ------ | -------------- | ----------------------------- | ------ | ------------------------------------------------------------------------------------------ | --------- |
| 4      | 3473 and later | `journalinfostaticstatus.bss` | 22,717 | 49 Book Quest, 57 Ed Texture, 41 Journal, 2 Journal List, 2 Texture Info                   | 10        |
| 3      | 3052 to 3464   | `journalinfostaticstatus.bss` | 22,635 | 49 Book Quest, 57 Ed Texture, 41 Journal, 2 Journal List, 2 Texture Info                   | 10        |
| 2      | 3002 to 3045   | `journalinfostaticstatus.bss` | 17,673 | 42 Book Quest, 50 Ed Texture, 34 Journal, 2 Journal List, 2 Select Texture, 2 Texture Info | 10        |
| 1      | 2995           | `journalinfostaticstatus.bss` | 4,547  | 27 Book Quest, 43 Ed Texture, 27 Journal                                                   | 12        |

| Layout | File                          | Known            | Unknown         |
| ------ | ----------------------------- | ---------------- | --------------- |
| 4      | `journalinfostaticstatus.bss` | 22,095 B (97.3%) | 622 B (2.7%)    |
| 3      | `journalinfostaticstatus.bss` | 22,095 B (97.6%) | 540 B (2.4%)    |
| 2      | `journalinfostaticstatus.bss` | 17,217 B (97.4%) | 456 B (2.6%)    |
| 1      | `journalinfostaticstatus.bss` | 2,681 B (59.0%)  | 1,866 B (41.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 4 | `897423e44850`  |
| 3482   | Layout 4 | `897423e44850`  |
| 3474   | Layout 4 | `897423e44850`  |
| 3473   | Layout 4 | `897423e44850`  |
| 3464   | Layout 3 | `897423e44850`  |
| 3458   | Layout 3 | `897423e44850`  |
| 3454   | Layout 3 | `897423e44850`  |
| 3444   | Layout 3 | `897423e44850`  |
| 3435   | Layout 3 | `897423e44850`  |
| 3426   | Layout 3 | `897423e44850`  |
| 3418   | Layout 3 | `897423e44850`  |
| 3412   | Layout 3 | `897423e44850`  |
| 3402   | Layout 3 | `897423e44850`  |
| 3396   | Layout 3 | `897423e44850`  |
| 3387   | Layout 3 | `897423e44850`  |
| 3381   | Layout 3 | `897423e44850`  |
| 3373   | Layout 3 | `897423e44850`  |
| 3364   | Layout 3 | `897423e44850`  |
| 3356   | Layout 3 | `897423e44850`  |
| 3349   | Layout 3 | `897423e44850`  |
| 3342   | Layout 3 | `897423e44850`  |
| 3335   | Layout 3 | `897423e44850`  |
| 3326   | Layout 3 | `897423e44850`  |
| 3321   | Layout 3 | `897423e44850`  |
| 3314   | Layout 3 | `897423e44850`  |
| 3303   | Layout 3 | `897423e44850`  |
| 3302   | Layout 3 | `897423e44850`  |
| 3293   | Layout 3 | `897423e44850`  |
| 3283   | Layout 3 | `897423e44850`  |
| 3275   | Layout 3 | `897423e44850`  |
| 3267   | Layout 3 | `897423e44850`  |
| 3258   | Layout 3 | `897423e44850`  |
| 3251   | Layout 3 | `897423e44850`  |
| 3242   | Layout 3 | `897423e44850`  |
| 3235   | Layout 3 | `897423e44850`  |
| 3229   | Layout 3 | `897423e44850`  |
| 3212   | Layout 3 | `897423e44850`  |
| 3203   | Layout 3 | `897423e44850`  |
| 3193   | Layout 3 | `897423e44850`  |
| 3186   | Layout 3 | `897423e44850`  |
| 3177   | Layout 3 | `897423e44850`  |
| 3169   | Layout 3 | `897423e44850`  |
| 3158   | Layout 3 | `897423e44850`  |
| 3151   | Layout 3 | `897423e44850`  |
| 3144   | Layout 3 | `897423e44850`  |
| 3133   | Layout 3 | `897423e44850`  |
| 3125   | Layout 3 | `897423e44850`  |
| 3118   | Layout 3 | `897423e44850`  |
| 3111   | Layout 3 | `897423e44850`  |
| 3103   | Layout 3 | `897423e44850`  |
| 3095   | Layout 3 | `897423e44850`  |
| 3086   | Layout 3 | `897423e44850`  |
| 3072   | Layout 3 | `897423e44850`  |
| 3062   | Layout 3 | `897423e44850`  |
| 3052   | Layout 3 | `897423e44850`  |
| 3045   | Layout 2 | `897423e44850`  |
| 3037   | Layout 2 | `897423e44850`  |
| 3030   | Layout 2 | `897423e44850`  |
| 3021   | Layout 2 | `897423e44850`  |
| 3012   | Layout 2 | `897423e44850`  |
| 3002   | Layout 2 | `897423e44850`  |
| 2995   | Layout 1 | `897423e44850`  |
| 2987   | No file  | `897423e44850`  |
| 2978   | No file  | `897423e44850`  |
| 2970   | No file  | `897423e44850`  |
| 2959   | No file  | `897423e44850`  |
| 2951   | No file  | `897423e44850`  |
| 2942   | No file  | `897423e44850`  |
| 2935   | No file  | `897423e44850`  |
| 2932   | No file  | `897423e44850`  |
| 2923   | No file  | `897423e44850`  |
| 2919   | No file  | `897423e44850`  |
| 2907   | No file  | `897423e44850`  |
| 2900   | No file  | `897423e44850`  |
| 2891   | No file  | `897423e44850`  |
| 2882   | No file  | `897423e44850`  |
| 2872   | No file  | `897423e44850`  |
| 2863   | No file  | `897423e44850`  |
| 2855   | No file  | `897423e44850`  |
| 2849   | No file  | `897423e44850`  |
| 2844   | No file  | `897423e44850`  |
| 2834   | No file  | `897423e44850`  |
| 2825   | No file  | `897423e44850`  |
| 2819   | No file  | `897423e44850`  |
| 2811   | No file  | `897423e44850`  |
| 2803   | No file  | `897423e44850`  |
| 2794   | No file  | `897423e44850`  |
| 2783   | No file  | `897423e44850`  |
| 2774   | No file  | `897423e44850`  |
| 2765   | No file  | `897423e44850`  |
| 2756   | No file  | `897423e44850`  |
| 2750   | No file  | `897423e44850`  |
| 2743   | No file  | `897423e44850`  |
| 2736   | No file  | `897423e44850`  |
| 2726   | No file  | `897423e44850`  |
| 2717   | No file  | `897423e44850`  |
| 2709   | No file  | `897423e44850`  |
| 2703   | No file  | `897423e44850`  |
| 2695   | No file  | `897423e44850`  |
| 2684   | No file  | `897423e44850`  |
| 2672   | No file  | `897423e44850`  |
| 2665   | No file  | `897423e44850`  |
| 2657   | No file  | `897423e44850`  |
| 2649   | No file  | `897423e44850`  |
| 2644   | No file  | `897423e44850`  |
| 2637   | No file  | `897423e44850`  |
| 2629   | No file  | `897423e44850`  |
| 2619   | No file  | `897423e44850`  |
| 2612   | No file  | `897423e44850`  |
| 2606   | No file  | `897423e44850`  |
| 2602   | No file  | `897423e44850`  |
| 2601   | No file  | `897423e44850`  |
| 2592   | No file  | `897423e44850`  |
| 2583   | No file  | `897423e44850`  |
| 2575   | No file  | `897423e44850`  |
| 2567   | No file  | `897423e44850`  |
| 2560   | No file  | `897423e44850`  |
| 2553   | No file  | `897423e44850`  |
| 2545   | No file  | `897423e44850`  |
| 2538   | No file  | `897423e44850`  |
| 2529   | No file  | `897423e44850`  |
| 2519   | No file  | `897423e44850`  |
| 2513   | No file  | `897423e44850`  |
| 2510   | No file  | `897423e44850`  |
| 2507   | No file  | `897423e44850`  |
| 2503   | No file  | `897423e44850`  |
| 2498   | No file  | `897423e44850`  |
| 2492   | No file  | `897423e44850`  |
| 2487   | No file  | `897423e44850`  |
| 2480   | No file  | `897423e44850`  |
| 2474   | No file  | `897423e44850`  |
| 2468   | No file  | `897423e44850`  |
| 2460   | No file  | `897423e44850`  |
| 2453   | No file  | `897423e44850`  |
| 2444   | No file  | `897423e44850`  |
| 2438   | No file  | `897423e44850`  |
| 2434   | No file  | `897423e44850`  |
| 2429   | No file  | `897423e44850`  |
| 2421   | No file  | `897423e44850`  |
| 2414   | No file  | `897423e44850`  |
| 2407   | No file  | `897423e44850`  |
| 2401   | No file  | `897423e44850`  |
| 2397   | No file  | `897423e44850`  |
| 2393   | No file  | `897423e44850`  |
| 2384   | No file  | `897423e44850`  |
| 2378   | No file  | `897423e44850`  |
| 2372   | No file  | `897423e44850`  |
| 2358   | No file  | `897423e44850`  |
| 2352   | No file  | `897423e44850`  |
| 2347   | No file  | `897423e44850`  |
| 2343   | No file  | `897423e44850`  |
| 2335   | No file  | `897423e44850`  |
| 2327   | No file  | `897423e44850`  |
| 2324   | No file  | `897423e44850`  |
| 2319   | No file  | `897423e44850`  |
| 2313   | No file  | `897423e44850`  |
| 2308   | No file  | `897423e44850`  |
| 2302   | No file  | `897423e44850`  |
| 2295   | No file  | `897423e44850`  |
| 2290   | No file  | `897423e44850`  |
| 2284   | No file  | `897423e44850`  |
| 2276   | No file  | `897423e44850`  |
| 2269   | No file  | `897423e44850`  |
| 2259   | No file  | `897423e44850`  |
| 2250   | No file  | `897423e44850`  |
| 2243   | No file  | `897423e44850`  |
| 2235   | No file  | `897423e44850`  |
| 2229   | No file  | `897423e44850`  |
| 2224   | No file  | `897423e44850`  |
| 2218   | No file  | `897423e44850`  |
| 2215   | No file  | `897423e44850`  |
| 2207   | No file  | `897423e44850`  |
| 2203   | No file  | `897423e44850`  |
| 2196   | No file  | `897423e44850`  |
| 2192   | No file  | `897423e44850`  |
| 2189   | No file  | `897423e44850`  |
| 2183   | No file  | `897423e44850`  |
| 2179   | No file  | `897423e44850`  |
| 2171   | No file  | `897423e44850`  |
| 2163   | No file  | `897423e44850`  |
| 2156   | No file  | `897423e44850`  |
| 2151   | No file  | `897423e44850`  |
| 2147   | No file  | `897423e44850`  |
| 2142   | No file  | `897423e44850`  |
| 2138   | No file  | `897423e44850`  |
| 2134   | No file  | `897423e44850`  |
| 2130   | No file  | `897423e44850`  |
| 2122   | No file  | `897423e44850`  |
| 2107   | No file  | `897423e44850`  |
| 2098   | No file  | `897423e44850`  |
| 2089   | No file  | `897423e44850`  |
| 2081   | No file  | `897423e44850`  |
| 2073   | No file  | `897423e44850`  |
| 2067   | No file  | `897423e44850`  |
| 2063   | No file  | `897423e44850`  |
| 2059   | No file  | `897423e44850`  |
| 2052   | No file  | `897423e44850`  |
| 2044   | No file  | `897423e44850`  |
| 2039   | No file  | `897423e44850`  |
| 2032   | No file  | `897423e44850`  |
| 2025   | No file  | `897423e44850`  |
| 2011   | No file  | `897423e44850`  |
| 2005   | No file  | `897423e44850`  |
| 2000   | No file  | `897423e44850`  |
| 1996   | No file  | `897423e44850`  |
| 1991   | No file  | `897423e44850`  |
| 1985   | No file  | `897423e44850`  |
| 1980   | No file  | `897423e44850`  |
| 1969   | No file  | `897423e44850`  |
| 1964   | No file  | `897423e44850`  |
| 1958   | No file  | `897423e44850`  |
| 1950   | No file  | `897423e44850`  |
| 1945   | No file  | `897423e44850`  |
| 1937   | No file  | `897423e44850`  |
| 1933   | No file  | `897423e44850`  |
| 1927   | No file  | `897423e44850`  |
| 1921   | No file  | `897423e44850`  |
| 1914   | No file  | `897423e44850`  |
| 1908   | No file  | `897423e44850`  |
| 1897   | No file  | `897423e44850`  |
| 1892   | No file  | `897423e44850`  |
| 1886   | No file  | `897423e44850`  |
| 1881   | No file  | `897423e44850`  |
| 1871   | No file  | `897423e44850`  |
| 1866   | No file  | `897423e44850`  |
| 1862   | No file  | `897423e44850`  |
| 1854   | No file  | `897423e44850`  |
| 1846   | No file  | `897423e44850`  |
| 1838   | No file  | `897423e44850`  |
| 1832   | No file  | `897423e44850`  |
| 1826   | No file  | `897423e44850`  |
| 1822   | No file  | `897423e44850`  |
| 1818   | No file  | `897423e44850`  |
| 1804   | No file  | `897423e44850`  |
| 1794   | No file  | `897423e44850`  |
| 1790   | No file  | `897423e44850`  |
| 1784   | No file  | `897423e44850`  |
| 1774   | No file  | `897423e44850`  |
| 1771   | No file  | `897423e44850`  |
| 1762   | No file  | `897423e44850`  |
| 1759   | No file  | `897423e44850`  |
| 1754   | No file  | `897423e44850`  |
| 1749   | No file  | `897423e44850`  |
| 1743   | No file  | `897423e44850`  |
| 1737   | No file  | `897423e44850`  |
| 1731   | No file  | `897423e44850`  |
| 1725   | No file  | `897423e44850`  |
| 1717   | No file  | `897423e44850`  |
| 1710   | No file  | `897423e44850`  |
| 1704   | No file  | `897423e44850`  |
| 1698   | No file  | `897423e44850`  |
| 1690   | No file  | `897423e44850`  |
| 1685   | No file  | `897423e44850`  |
| 1680   | No file  | `897423e44850`  |
| 1674   | No file  | `897423e44850`  |
| 1668   | No file  | `897423e44850`  |
| 1659   | No file  | `897423e44850`  |
| 1649   | No file  | `897423e44850`  |
| 1642   | No file  | `897423e44850`  |
| 1636   | No file  | `897423e44850`  |
| 1628   | No file  | `897423e44850`  |
| 1622   | No file  | `897423e44850`  |
| 1614   | No file  | `897423e44850`  |
| 1608   | No file  | `897423e44850`  |
| 1602   | No file  | `897423e44850`  |
| 1598   | No file  | `897423e44850`  |
| 1594   | No file  | `897423e44850`  |
| 1590   | No file  | `897423e44850`  |
| 1587   | No file  | `897423e44850`  |
| 1584   | No file  | `897423e44850`  |
| 1579   | No file  | `897423e44850`  |
| 1572   | No file  | `897423e44850`  |
| 1565   | No file  | `897423e44850`  |
| 1559   | No file  | `897423e44850`  |
| 1554   | No file  | `897423e44850`  |
| 1547   | No file  | `897423e44850`  |
| 1537   | No file  | `897423e44850`  |
| 1529   | No file  | `897423e44850`  |
| 1524   | No file  | `897423e44850`  |
| 1519   | No file  | `897423e44850`  |
| 1509   | No file  | `897423e44850`  |
| 1506   | No file  | `897423e44850`  |
| 1504   | No file  | `897423e44850`  |
| 1500   | No file  | `897423e44850`  |
| 1493   | No file  | `897423e44850`  |
| 1489   | No file  | `897423e44850`  |
| 1485   | No file  | `897423e44850`  |
| 1481   | No file  | `897423e44850`  |
| 1474   | No file  | `897423e44850`  |
| 1466   | No file  | `897423e44850`  |
| 1462   | No file  | `897423e44850`  |
| 1459   | No file  | `897423e44850`  |
| 1453   | No file  | `897423e44850`  |
| 1450   | No file  | `897423e44850`  |
| 1445   | No file  | `897423e44850`  |
| 1439   | No file  | `897423e44850`  |
| 1433   | No file  | `897423e44850`  |
| 1430   | No file  | `897423e44850`  |
| 1426   | No file  | `897423e44850`  |
| 1421   | No file  | `897423e44850`  |
| 1417   | No file  | `897423e44850`  |
| 1416   | No file  | `897423e44850`  |
| 1409   | No file  | `897423e44850`  |
| 1405   | No file  | `897423e44850`  |
| 1401   | No file  | `897423e44850`  |
| 1396   | No file  | `897423e44850`  |
| 1391   | No file  | `897423e44850`  |
| 1390   | No file  | `897423e44850`  |
| 1386   | No file  | `897423e44850`  |
| 1381   | No file  | `897423e44850`  |
| 1379   | No file  | `897423e44850`  |
| 1372   | No file  | `897423e44850`  |
| 1366   | No file  | `897423e44850`  |
| 1364   | No file  | `897423e44850`  |
| 1363   | No file  | `897423e44850`  |
| 1360   | No file  | `897423e44850`  |
| 1358   | No file  | `897423e44850`  |
| 1355   | No file  | `897423e44850`  |
| 1351   | No file  | `897423e44850`  |
| 1348   | No file  | `897423e44850`  |
| 1346   | No file  | `897423e44850`  |
| 1341   | No file  | `897423e44850`  |
| 1340   | No file  | `897423e44850`  |
| 1338   | No file  | `897423e44850`  |
| 1335   | No file  | `897423e44850`  |
| 1333   | No file  | `897423e44850`  |
| 1329   | No file  | `897423e44850`  |
| 1327   | No file  | `897423e44850`  |
| 1324   | No file  | `897423e44850`  |
| 1321   | No file  | `897423e44850`  |
| 1319   | No file  | `897423e44850`  |
| 1318   | No file  | `897423e44850`  |
| 1316   | No file  | `897423e44850`  |
| 1313   | No file  | `897423e44850`  |
| 1311   | No file  | `897423e44850`  |
| 1309   | No file  | `897423e44850`  |
| 1304   | No file  | `897423e44850`  |
| 1292   | No file  | `897423e44850`  |
| 1286   | No file  | `897423e44850`  |
| 1280   | No file  | `897423e44850`  |
| 1276   | No file  | `897423e44850`  |
| 1267   | No file  | `897423e44850`  |
| 1261   | No file  | `897423e44850`  |
| 1256   | No file  | `897423e44850`  |
| 1250   | No file  | `897423e44850`  |
| 1246   | No file  | `897423e44850`  |
| 1239   | No file  | `897423e44850`  |
| 1230   | No file  | `897423e44850`  |
| 1226   | No file  | `897423e44850`  |
| 1220   | No file  | `897423e44850`  |
| 1217   | No file  | `897423e44850`  |
| 1211   | No file  | `897423e44850`  |
| 1210   | No file  | `897423e44850`  |
| 1208   | No file  | `897423e44850`  |
| 1203   | No file  | `897423e44850`  |
| 1197   | No file  | `897423e44850`  |
| 1194   | No file  | `897423e44850`  |
| 1192   | No file  | `897423e44850`  |
| 1187   | No file  | `897423e44850`  |
| 1183   | No file  | `897423e44850`  |
| 1177   | No file  | `897423e44850`  |
| 1173   | No file  | `897423e44850`  |
| 1167   | No file  | `897423e44850`  |
| 1164   | No file  | `897423e44850`  |
| 1156   | No file  | `897423e44850`  |
| 1149   | No file  | `897423e44850`  |
| 1144   | No file  | `897423e44850`  |
| 1137   | No file  | `897423e44850`  |
| 1132   | No file  | `897423e44850`  |
| 1127   | No file  | `897423e44850`  |
| 1122   | No file  | `897423e44850`  |
| 1118   | No file  | `897423e44850`  |
| 1114   | No file  | `897423e44850`  |
| 1109   | No file  | `897423e44850`  |
| 1102   | No file  | `897423e44850`  |
| 1096   | No file  | `897423e44850`  |
| 1088   | No file  | `897423e44850`  |
| 1081   | No file  | `897423e44850`  |
| 1076   | No file  | `897423e44850`  |
| 1069   | No file  | `897423e44850`  |
| 1064   | No file  | `897423e44850`  |
| 1058   | No file  | `897423e44850`  |
| 1051   | No file  | `897423e44850`  |
| 1044   | No file  | `897423e44850`  |
| 1036   | No file  | `897423e44850`  |
| 1026   | No file  | `897423e44850`  |
| 1016   | No file  | `897423e44850`  |
| 1009   | No file  | `897423e44850`  |
| 1005   | No file  | `897423e44850`  |
| 1000   | No file  | `897423e44850`  |
| 998    | No file  | `897423e44850`  |
| 990    | No file  | `897423e44850`  |
| 979    | No file  | `897423e44850`  |
| 972    | No file  | `897423e44850`  |
| 963    | No file  | `897423e44850`  |
| 955    | No file  | `897423e44850`  |
| 946    | No file  | `897423e44850`  |
| 938    | No file  | `897423e44850`  |
| 927    | No file  | `897423e44850`  |
| 911    | No file  | `897423e44850`  |
| 904    | No file  | `897423e44850`  |
| 899    | No file  | `897423e44850`  |
| 894    | No file  | `897423e44850`  |
| 885    | No file  | `897423e44850`  |
| 879    | No file  | `897423e44850`  |
| 872    | No file  | `897423e44850`  |
| 864    | No file  | `897423e44850`  |
| 855    | No file  | `897423e44850`  |
| 853    | No file  | `897423e44850`  |
| 845    | No file  | `897423e44850`  |
| 837    | No file  | `897423e44850`  |
| 829    | No file  | `897423e44850`  |
| 822    | No file  | `897423e44850`  |
| 814    | No file  | `897423e44850`  |
| 805    | No file  | `897423e44850`  |
| 794    | No file  | `897423e44850`  |
| 787    | No file  | `897423e44850`  |
| 780    | No file  | `897423e44850`  |
| 771    | No file  | `897423e44850`  |
| 760    | No file  | `897423e44850`  |
| 748    | No file  | `897423e44850`  |
| 741    | No file  | `897423e44850`  |
| 736    | No file  | `897423e44850`  |
| 731    | No file  | `897423e44850`  |
| 723    | No file  | `897423e44850`  |
| 711    | No file  | `897423e44850`  |
| 707    | No file  | `897423e44850`  |
| 697    | No file  | `897423e44850`  |
| 689    | No file  | `897423e44850`  |
| 683    | No file  | `897423e44850`  |
| 678    | No file  | `897423e44850`  |
| 670    | No file  | `897423e44850`  |
| 661    | No file  | `897423e44850`  |
| 656    | No file  | `897423e44850`  |
| 652    | No file  | `897423e44850`  |
| 643    | No file  | `897423e44850`  |
| 637    | No file  | `897423e44850`  |
| 630    | No file  | `897423e44850`  |
| 627    | No file  | `897423e44850`  |
| 621    | No file  | `897423e44850`  |
| 617    | No file  | `897423e44850`  |
| 615    | No file  | `897423e44850`  |
| 606    | No file  | `897423e44850`  |
| 599    | No file  | `897423e44850`  |
| 592    | No file  | `897423e44850`  |
| 586    | No file  | `897423e44850`  |
| 577    | No file  | `897423e44850`  |
| 569    | No file  | `897423e44850`  |
| 561    | No file  | `897423e44850`  |
| 554    | No file  | `897423e44850`  |
| 542    | No file  | `897423e44850`  |
| 532    | No file  | `897423e44850`  |
| 531    | No file  | `897423e44850`  |
| 526    | No file  | `897423e44850`  |
| 521    | No file  | `897423e44850`  |
| 517    | No file  | `897423e44850`  |
| 510    | No file  | `897423e44850`  |
| 508    | No file  | `897423e44850`  |
| 504    | No file  | `897423e44850`  |
| 497    | No file  | `897423e44850`  |
| 491    | No file  | `897423e44850`  |
| 485    | No file  | `897423e44850`  |
| 478    | No file  | `897423e44850`  |
| 472    | No file  | `897423e44850`  |
| 466    | No file  | `897423e44850`  |
| 457    | No file  | `897423e44850`  |
| 452    | No file  | `897423e44850`  |
| 449    | No file  | `897423e44850`  |
| 435    | No file  | `897423e44850`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `stringtable.bss`     | Optional | Key hashes of the `GAME` sheet keys, for their LOC type 37 text |
| `languagedata_en.loc` | Optional | LOC type 37 text of the chapter, title and story keys |

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset                | Type                                  | Field              | Notes                                         |
| --------------------- | ------------------------------------- | ------------------ | --------------------------------------------- |
| `+0x00`               | char[4]                               | magic              | ASCII `PABR`                                  |
| `+0x04`               | u32                                   | journal_list_count | Number of journal lists; `2` on client 3482   |
| `+0x08`               | Journal List[journal_list_count]      | journal_lists      | See Journal List; list `0` is Morning Land, `1` Edania |
| `journal_lists+0x00`  | u32                                   | texture_info_count | Equals `journal_list_count`                   |
| `journal_lists+0x04`  | Texture Info[texture_info_count]      | texture_infos      | One per journal list, in list order           |
| `texture_infos+0x00`  | String Table                          | string_table       | See String Table                              |
| `string_table+0x00`   | u32                                   | table_start        | Offset of the string table, where `texture_infos` ends |
| `string_table+0x04`   | u32                                   | zero               | Always `0`                                    |

### Journal List (variable: 4 bytes + journals)

| Offset  | Type                    | Field         | Notes                       |
| ------- | ----------------------- | ------------- | --------------------------- |
| `+0x00` | u32                     | journal_count | `27` and `14` on client 3482 |
| `+0x04` | Journal[journal_count]  | journals      | See Journal                 |

### Journal (variable: 64 bytes + book quests and ed textures)

Every `*_ref` field and `unknown_22` is an index into `strings`.

| Offset              | Type                          | Field                      | Notes |
| ------------------- | ----------------------------- | -------------------------- | ----- |
| `+0x00`             | u16                           | chapter_index              | `_chapterIndex`: chapter tab, from `1` (`1` and `2` in both lists) |
| `+0x02`             | u16                           | ui_type                    | `ToClient_getJournalUIType()`: `0` a boss card with normal and over textures, `1` a visual card (`Static_QuestVisual`) |
| `+0x04`             | u16                           | ui_type_index              | `_uiTypeIndex`: page of the chapter, from `1`; `1` holds the type `0` cards, `2` the type `1` cards |
| `+0x06`             | u16                           | journal_index              | `_journalIndex`: card on the page, from `1` |
| `+0x08`             | u16                           | quest_group_no             | `_questGroupNo`: the quest chain the card tracks; a `quest.dbss` chain on all 41 journals of client 3482 |
| `+0x0A`             | u16                           | unknown_0a                 | `2` to `39`; at most the highest quest ID of the chain on all 41 journals. See Open Questions |
| `+0x0C`             | u32                           | chapter_string_ref         | `getChapterString()`: `GAME` key of the chapter tab (`LUA_MORNINGLAND_QUESTBOARD_TAB1`) |
| `+0x10`             | u32                           | scenario_desc_ref          | `getScenarioDesc()`: `GAME` key of the story text (`LUA_MORNING_QUESTBOARD_DESC_1`) |
| `+0x14`             | u32                           | title_string_ref           | `getTitleString()`: `GAME` key of the boss or chapter title (`LUA_MORNINGMAINPROGRESS_TITLE_01`) |
| `+0x18`             | u16                           | unknown_18                 | `0` on every journal |
| `+0x1A`             | u32                           | texture_normal_ref         | `ToClient_getJournalInfoTextureID(info, 0)`: card texture ID (`Combine_Etc_MorningLand_MainQuest_Boss_05_Normal`) |
| `+0x1E`             | u32                           | texture_over_ref           | `ToClient_getJournalInfoTextureID(info, 1)`: mouse-over texture ID; the same as `texture_normal_ref` on the type `1` cards |
| `+0x22`             | u32                           | unknown_22                 | Condition script: empty on Morning Land, a `clearquest(...)` of the chain before on every Edania journal (`clearquest(9100,5)`) |
| `+0x26`             | u32[3]                        | detail_btn_texture_id_refs | `getDetailBtnTextureId(0)` to `(2)`: texture IDs of the detail button |
| `+0x32`             | u32                           | detail_btn_string_ref      | `getDetailBtnString()`: `GAME` key shown as the boss name on Edania (`LUA_EDANIA_JOURNAL_1`); empty on Morning Land |
| `+0x36`             | u16                           | unknown_36                 | `0` on 37 journals; `305`, `131`, `123`, `104` on chains `9303` to `9306`, the highest quest ID of each chain on client 3482 |
| `+0x38`             | u32                           | book_quest_count           | `1` or `2`                    |
| `+0x3C`             | Book Quest[book_quest_count]  | book_quests                | See Book Quest                |
| `book_quests+0x00`  | u32                           | ed_texture_count           | `1` or `2`                    |
| `book_quests+0x04`  | Ed Texture[ed_texture_count]  | ed_textures                | See Ed Texture                |

### Book Quest (10 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u32  | condition_ref    | Condition script: empty on 33 entries, else `clearquest(8504,21);` or a class check (`checkClass(15);<or>checkClass(30);`) |
| `+0x04` | u16  | book_quest_group | `getBookQuestNo()._group`: chain of the bookshelf quest the cleared card opens (`8542` to `8554`, `8700` to `8714`, `9131` to `9137`, `9331` to `9337`) |
| `+0x06` | u16  | book_quest_id    | `getBookQuestNo()._quest`; `book_quest_group`, `book_quest_id` is a `quest.dbss` quest on 49 of 49 entries |
| `+0x08` | u16  | unknown_08       | `2` to `41`; see Open Questions |

### Ed Texture (10 bytes)

| Offset  | Type | Field              | Notes |
| ------- | ---- | ------------------ | ----- |
| `+0x00` | u32  | texture_normal_ref | Texture ID ending in `_ed`, `_ed_S_Normal` or `_ed_H_Normal` |
| `+0x04` | u32  | texture_over_ref   | The matching over texture ID |
| `+0x08` | u16  | unknown_08         | A quest ID of `quest_group_no`; on chains `8504` to `8507` and `8512`, `8513` the two values are the quest IDs of the two `clearquest` conditions |

### Texture Info (84 bytes)

| Offset  | Type    | Field             | Notes |
| ------- | ------- | ----------------- | ----- |
| `+0x00` | u32[21] | texture_info_refs | Slot `n` is `ToClient_getJournalTextureInfo(list, n)`; see [Texture Info Slots](#texture-info-slots) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                  |
| ------- | ------------------ | ------------ | -------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `342` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | Each text is stored once               |

## Layout 3

Layout 4 without `unknown_36`.

### Journal (variable: 62 bytes + book quests and ed textures)

| Offset              | Type                          | Field                      | Notes |
| ------------------- | ----------------------------- | -------------------------- | ----- |
| `+0x00`             | u16                           | chapter_index              |       |
| `+0x02`             | u16                           | ui_type                    |       |
| `+0x04`             | u16                           | ui_type_index              |       |
| `+0x06`             | u16                           | journal_index              |       |
| `+0x08`             | u16                           | quest_group_no             |       |
| `+0x0A`             | u16                           | unknown_0a                 |       |
| `+0x0C`             | u32                           | chapter_string_ref         |       |
| `+0x10`             | u32                           | scenario_desc_ref          |       |
| `+0x14`             | u32                           | title_string_ref           |       |
| `+0x18`             | u16                           | unknown_18                 |       |
| `+0x1A`             | u32                           | texture_normal_ref         |       |
| `+0x1E`             | u32                           | texture_over_ref           |       |
| `+0x22`             | u32                           | unknown_22                 |       |
| `+0x26`             | u32[3]                        | detail_btn_texture_id_refs |       |
| `+0x32`             | u32                           | detail_btn_string_ref      |       |
| `+0x36`             | u32                           | book_quest_count           |       |
| `+0x3A`             | Book Quest[book_quest_count]  | book_quests                |       |
| `book_quests+0x00`  | u32                           | ed_texture_count           |       |
| `book_quests+0x04`  | Ed Texture[ed_texture_count]  | ed_textures                |       |

## Layout 2

The list textures are two lists: the three select button textures (slots
`0` to `2` of Layout 4), then four slots (`3` to `6`) per journal list.

### File Layout

| Offset                   | Type                                  | Field                 | Notes                                         |
| ------------------------ | ------------------------------------- | --------------------- | --------------------------------------------- |
| `+0x00`                  | char[4]                               | magic                 | ASCII `PABR`                                  |
| `+0x04`                  | u32                                   | journal_list_count    | Number of journal lists                       |
| `+0x08`                  | Journal List[journal_list_count]      | journal_lists         | See Journal List                              |
| `journal_lists+0x00`     | u32                                   | select_texture_count  | Equals `journal_list_count`                   |
| `journal_lists+0x04`     | Select Texture[select_texture_count]  | select_textures       | See Select Texture                            |
| `select_textures+0x00`   | u32                                   | texture_info_count    | Equals `journal_list_count`                   |
| `select_textures+0x04`   | Texture Info[texture_info_count]      | texture_infos         | See Texture Info                              |
| `texture_infos+0x00`     | String Table                          | string_table          | See String Table                              |
| `string_table+0x00`      | u32                                   | table_start           | Offset of the string table                    |
| `string_table+0x04`      | u32                                   | zero                  | Always `0`                                    |

### Select Texture (12 bytes)

| Offset  | Type   | Field               | Notes                                                        |
| ------- | ------ | ------------------- | ------------------------------------------------------------ |
| `+0x00` | u32[3] | select_texture_refs | Base, over and click texture of the board select button      |

### Texture Info (16 bytes)

| Offset  | Type   | Field             | Notes                                                 |
| ------- | ------ | ----------------- | ----------------------------------------------------- |
| `+0x00` | u32[4] | texture_info_refs | Slots `3` to `6` of Layout 4: frame, bar, title key, text key |

## Layout 1

Client 2995 has one journal list (the 27 Morning Land journals) and no
texture names: its strings are the 27 title keys and one select texture
text. A journal holds the title key as its only string; the texture fields
hold the numbers `3610` to `3613` on every journal. After the list comes
one select texture per list and no texture info.

### File Layout

| Offset                 | Type                                 | Field                | Notes                                   |
| ---------------------- | ------------------------------------ | -------------------- | --------------------------------------- |
| `+0x00`                | char[4]                              | magic                | ASCII `PABR`                            |
| `+0x04`                | u32                                  | journal_list_count   | Number of journal lists; `1` on client 2995 |
| `+0x08`                | Journal List[journal_list_count]     | journal_lists        | See Journal List                        |
| `journal_lists+0x00`   | u32                                  | select_texture_count | Equals `journal_list_count`             |
| `journal_lists+0x04`   | Select Texture[select_texture_count] | select_textures      | See Select Texture                      |
| `select_textures+0x00` | String Table                         | string_table         | See String Table                        |
| `string_table+0x00`    | u32                                  | table_start          | Offset of the string table              |
| `string_table+0x04`    | u32                                  | zero                 | Always `0`                              |

### Journal (variable: 36 bytes + book quests and ed textures)

The four index fields, `quest_group_no`, `title_string_ref` and the book
quest group and ID hold the same values as on client 3002 (Layout 2) on all
27 journals.

| Offset             | Type                         | Field              | Notes |
| ------------------ | ---------------------------- | ------------------ | ----- |
| `+0x00`            | u16                          | chapter_index      |       |
| `+0x02`            | u16                          | ui_type            |       |
| `+0x04`            | u16                          | ui_type_index      |       |
| `+0x06`            | u16                          | journal_index      |       |
| `+0x08`            | u16                          | quest_group_no     |       |
| `+0x0A`            | u16                          | unknown_0a         | `2` to `39` |
| `+0x0C`            | u32                          | title_string_ref   | `LUA_MORNINGMAINPROGRESS_TITLE_01` to `_14` and `_01_1` to `_13_1` |
| `+0x10`            | u16                          | unknown_18         | `0` on every journal, as `unknown_18` of Layout 2 between the title and the textures |
| `+0x12`            | u16                          | unknown_12         | Eight values, `0xccc7` on 14 of 27 journals |
| `+0x14`            | u32[2]                       | unknown_14         | `3610` and `3611` on every journal; numbers where Layout 2 has `texture_normal_ref` and `texture_over_ref` |
| `+0x1C`            | u32                          | book_quest_count   | `1` on every journal |
| `+0x20`            | Book Quest[book_quest_count] | book_quests        | See Book Quest |
| `book_quests+0x00` | u32                          | ed_texture_count   | `1` or `2` |
| `book_quests+0x04` | Ed Texture[ed_texture_count] | ed_textures        | See Ed Texture |

### Book Quest (40 bytes)

| Offset  | Type      | Field            | Notes |
| ------- | --------- | ---------------- | ----- |
| `+0x00` | bytes[28] | unknown_00       | All zero on every entry |
| `+0x1C` | u16       | unknown_08       | Equals a client 3002 book quest's `unknown_08` on 16 of 27 journals |
| `+0x1E` | u16       | unknown_1e       | `0`; `51` on chain `8506` |
| `+0x20` | u16       | book_quest_group | `8700` to `8714` and `8542` to `8554` |
| `+0x22` | u16       | book_quest_id    |       |
| `+0x24` | u16       | unknown_24       | `0`, `389` or `390` |
| `+0x26` | u16       | unknown_26       | `0` on every entry |

### Ed Texture (12 bytes)

| Offset  | Type   | Field      | Notes |
| ------- | ------ | ---------- | ----- |
| `+0x00` | u16    | unknown_08 | A quest ID of `quest_group_no`; equals client 3002's `unknown_08` on all 43 entries |
| `+0x02` | u16    | unknown_02 | `0`, or `60304` on the first entry of 25 journals |
| `+0x04` | u32[2] | unknown_04 | `3612` and `3613` on every entry; numbers where Layout 2 has the two texture refs |

### Select Texture (4 bytes)

| Offset  | Type   | Field               | Notes |
| ------- | ------ | ------------------- | ----- |
| `+0x00` | u32[1] | select_texture_refs | String `일지 선택할 Texture ID` ("texture ID to select the journal"), the text that stands where Layout 2 has the three button textures |

## Texture Info Slots

The Lua reads the slots with `ToClient_getJournalTextureInfo(list, n)`; the
values are those of list `0` on client 3482.

| Slot | Lua use                                                    | List `0` value |
| ---- | ---------------------------------------------------------- | -------------- |
| 0    | Board select button, base (`panel_window_journal_select_all`) | `Combine_Etc_StartMap_01_Btn_03_Normal_2` |
| 1    | Board select button, over                                  | `Combine_Etc_StartMap_01_Btn_03_Over_2` |
| 2    | Board select button, click                                 | `Combine_Etc_StartMap_01_Btn_03_Click_2` |
| 3    | Board frame texture                                        | `Combine_Etc_MorningLand_MainQuest_Frame` |
| 4    | Line on the type `0` pages                                 | `Etc_MorningLand_MainQuest_Center_Bar` |
| 5    | `GAME` key of the board title                              | `LUA_EDANIA_JOURNAL_TITLE_NAME1` |
| 6    | `GAME` key of the board text                               | `LUA_EDANIA_JOURNAL_TITLE_DESC1` |
| 7    | Story page background                                      | `Combine_Etc_MorningLand_MainQuest_07_SubPopup_BG` |
| 8    | Story page button, base                                    | `Combine_Etc_MorningLand_MainQuest_07_SubPopup_Btn_Normal` |
| 9    | Story page button, over                                    | `Combine_Etc_MorningLand_MainQuest_07_SubPopup_Btn_Over` |
| 10   | Story page button, click                                   | `Combine_Etc_MorningLand_MainQuest_07_SubPopup_Btn_Click` |
| 11   | Book background                                            | `Combine_Etc_Morning_Book_BG` |
| 12   | Book left button, base                                     | `Combine_Etc_Morning_Book_01_Btn_L_Normal` |
| 13   | Book left button, over                                     | `Combine_Etc_Morning_Book_01_Btn_L_Over` |
| 14   | Book left button, click                                    | `Combine_Etc_Morning_Book_01_Btn_L_Click` |
| 15   | Book right button, base                                    | `Combine_Etc_Morning_Book_01_Btn_R_Normal` |
| 16   | Book right button, over                                    | `Combine_Etc_Morning_Book_01_Btn_R_Over` |
| 17   | Book right button, click                                   | `Combine_Etc_Morning_Book_01_Btn_R_Click` |
| 18   | Hidden book page                                           | `Combine_Etc_Morning_Book_Image_Secret_02` |
| 19   | Left page effect                                           | `UI_Book_02B` |
| 20   | Right page effect                                          | `UI_Book_02A` |

## Field Names

The names follow `panel_window_journal_all_1.luac`,
`panel_window_journal_page_all.luac`, `panel_window_journal_book_all.luac`
and `panel_window_journal_select_all.luac` (client 3482): the members
`_chapterIndex`, `_uiTypeIndex`, `_journalIndex` and `_questGroupNo` of the
journal info, its getters `getChapterString()`, `getScenarioDesc()`,
`getTitleString()`, `getDetailBtnTextureId(i)`, `getDetailBtnString()` and
`getBookQuestNo()`, and `ToClient_getJournalUIType()`,
`ToClient_getJournalInfoTextureID(info, i)` and
`ToClient_getJournalTextureInfo(list, n)`. The chapter and page fields are
told apart by their ranges: `ui_type` is `0` or `1` and `ui_type_index`
`1` or `2`, and every type `1` card sits on page `2`. Client 1784 has no
file and no matching sheet.

Client 2995 ships no journal script, so Layout 1 takes its names from the
same journals on client 3002, matched by the four index fields:
`quest_group_no`, `title_string_ref`, `book_quest_group`, `book_quest_id`
and the Ed Texture `unknown_08` hold the client 3002 values on every
journal, and `unknown_18` is the zero u16 after the title in both.

## Notes

- The strings are not in walk order: the texture info strings come last
  (`300` to `341` on client 3482).
- The `GAME` keys resolve through `stringtable.bss` and LOC type 37; the
  Lua passes them to `PAGetString(Defines.StringSheet_GAME, ...)`.

## Open Questions

### Quest Counts of a Journal

`unknown_0a` and the `unknown_08` of a book quest look like quest counts of
the chain. On client 3482 `unknown_08` equals the highest quest ID of
`quest_group_no` on 17 of the 33 single book quests (`8503`: 30, `8524`:
22), and `unknown_0a` is at most that ID on all 41 journals. The Lua
divides `ToClient_getJournalInfoClearQuestCount(info)` by
`_totalQuestCount`, but no getter shows which field that is.

### Highest Quest ID on Four Edania Journals

`unknown_36` is `0` except on chains `9303` to `9306`, where it equals the
highest quest ID of the chain in `quest.dbss`. Layouts 1 to 3 have no `unknown_36`.

### Book Quest Count and Texture Numbers on Client 2995

Layout 1 reads the u32 before each 40-byte book quest as
`book_quest_count`, the shape of the later layouts, but it is `1` on all
27 journals, so the file cannot tell a count from a fixed field. The
numbers `3610` to `3613` sit where Layout 2 has its texture refs, normal
before over, and the over number is the normal number plus 1; client 2995
has no script that reads them. `unknown_12`, `unknown_24` and the `60304`
in `unknown_02` follow no journal field.
