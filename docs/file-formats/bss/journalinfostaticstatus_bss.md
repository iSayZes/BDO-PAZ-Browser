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
| 3      | 3473 and later | `journalinfostaticstatus.bss` | 22,717 | 49 Book Quest, 57 Ed Texture, 41 Journal, 2 Journal List, 2 Texture Info                   | 10        |
| 2      | 3052 to 3464   | `journalinfostaticstatus.bss` | 22,635 | 49 Book Quest, 57 Ed Texture, 41 Journal, 2 Journal List, 2 Texture Info                   | 10        |
| 1      | 3002 to 3045   | `journalinfostaticstatus.bss` | 17,673 | 42 Book Quest, 50 Ed Texture, 34 Journal, 2 Journal List, 2 Select Texture, 2 Texture Info | 10        |

| Layout | File                          | Known            | Unknown      |
| ------ | ----------------------------- | ---------------- | ------------ |
| 3      | `journalinfostaticstatus.bss` | 22,095 B (97.3%) | 622 B (2.7%) |
| 2      | `journalinfostaticstatus.bss` | 22,095 B (97.6%) | 540 B (2.4%) |
| 1      | `journalinfostaticstatus.bss` | 17,217 B (97.4%) | 456 B (2.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 3             | `d6697c04ee27`  |
| 3482   | Layout 3             | `d6697c04ee27`  |
| 3474   | Layout 3             | `d6697c04ee27`  |
| 3473   | Layout 3             | `d6697c04ee27`  |
| 3464   | Layout 2             | `d6697c04ee27`  |
| 3458   | Layout 2             | `d6697c04ee27`  |
| 3454   | Layout 2             | `d6697c04ee27`  |
| 3444   | Layout 2             | `d6697c04ee27`  |
| 3435   | Layout 2             | `d6697c04ee27`  |
| 3426   | Layout 2             | `d6697c04ee27`  |
| 3418   | Layout 2             | `d6697c04ee27`  |
| 3412   | Layout 2             | `d6697c04ee27`  |
| 3402   | Layout 2             | `d6697c04ee27`  |
| 3396   | Layout 2             | `d6697c04ee27`  |
| 3387   | Layout 2             | `d6697c04ee27`  |
| 3381   | Layout 2             | `d6697c04ee27`  |
| 3373   | Layout 2             | `d6697c04ee27`  |
| 3364   | Layout 2             | `d6697c04ee27`  |
| 3356   | Layout 2             | `d6697c04ee27`  |
| 3349   | Layout 2             | `d6697c04ee27`  |
| 3342   | Layout 2             | `d6697c04ee27`  |
| 3335   | Layout 2             | `d6697c04ee27`  |
| 3326   | Layout 2             | `d6697c04ee27`  |
| 3321   | Layout 2             | `d6697c04ee27`  |
| 3314   | Layout 2             | `d6697c04ee27`  |
| 3303   | Layout 2             | `d6697c04ee27`  |
| 3302   | Layout 2             | `d6697c04ee27`  |
| 3293   | Layout 2             | `d6697c04ee27`  |
| 3283   | Layout 2             | `d6697c04ee27`  |
| 3275   | Layout 2             | `d6697c04ee27`  |
| 3267   | Layout 2             | `d6697c04ee27`  |
| 3258   | Layout 2             | `d6697c04ee27`  |
| 3251   | Layout 2             | `d6697c04ee27`  |
| 3242   | Layout 2             | `d6697c04ee27`  |
| 3235   | Layout 2             | `d6697c04ee27`  |
| 3229   | Layout 2             | `d6697c04ee27`  |
| 3212   | Layout 2             | `d6697c04ee27`  |
| 3203   | Layout 2             | `d6697c04ee27`  |
| 3193   | Layout 2             | `d6697c04ee27`  |
| 3186   | Layout 2             | `d6697c04ee27`  |
| 3177   | Layout 2             | `d6697c04ee27`  |
| 3169   | Layout 2             | `d6697c04ee27`  |
| 3158   | Layout 2             | `d6697c04ee27`  |
| 3151   | Layout 2             | `d6697c04ee27`  |
| 3144   | Layout 2             | `d6697c04ee27`  |
| 3133   | Layout 2             | `d6697c04ee27`  |
| 3125   | Layout 2             | `d6697c04ee27`  |
| 3118   | Layout 2             | `d6697c04ee27`  |
| 3111   | Layout 2             | `d6697c04ee27`  |
| 3103   | Layout 2             | `d6697c04ee27`  |
| 3095   | Layout 2             | `d6697c04ee27`  |
| 3086   | Layout 2             | `d6697c04ee27`  |
| 3072   | Layout 2             | `d6697c04ee27`  |
| 3062   | Layout 2             | `d6697c04ee27`  |
| 3052   | Layout 2             | `d6697c04ee27`  |
| 3045   | Layout 1             | `d6697c04ee27`  |
| 3037   | Layout 1             | `d6697c04ee27`  |
| 3030   | Layout 1             | `d6697c04ee27`  |
| 3021   | Layout 1             | `d6697c04ee27`  |
| 3012   | Layout 1             | `d6697c04ee27`  |
| 3002   | Layout 1             | `d6697c04ee27`  |
| 2995   | No documented layout | `d6697c04ee27`  |
| 2987   | No file              | `d6697c04ee27`  |
| 2978   | No file              | `d6697c04ee27`  |
| 2970   | No file              | `d6697c04ee27`  |
| 2959   | No file              | `d6697c04ee27`  |
| 2951   | No file              | `d6697c04ee27`  |
| 2942   | No file              | `d6697c04ee27`  |
| 2935   | No file              | `d6697c04ee27`  |
| 2932   | No file              | `d6697c04ee27`  |
| 2923   | No file              | `d6697c04ee27`  |
| 2919   | No file              | `d6697c04ee27`  |
| 2907   | No file              | `d6697c04ee27`  |
| 2900   | No file              | `d6697c04ee27`  |
| 2891   | No file              | `d6697c04ee27`  |
| 2882   | No file              | `d6697c04ee27`  |
| 2872   | No file              | `d6697c04ee27`  |
| 2863   | No file              | `d6697c04ee27`  |
| 2855   | No file              | `d6697c04ee27`  |
| 2849   | No file              | `d6697c04ee27`  |
| 2844   | No file              | `d6697c04ee27`  |
| 2834   | No file              | `d6697c04ee27`  |
| 2825   | No file              | `d6697c04ee27`  |
| 2819   | No file              | `d6697c04ee27`  |
| 2811   | No file              | `d6697c04ee27`  |
| 2803   | No file              | `d6697c04ee27`  |
| 2794   | No file              | `d6697c04ee27`  |
| 2783   | No file              | `d6697c04ee27`  |
| 2774   | No file              | `d6697c04ee27`  |
| 2765   | No file              | `d6697c04ee27`  |
| 2756   | No file              | `d6697c04ee27`  |
| 2750   | No file              | `d6697c04ee27`  |
| 2743   | No file              | `d6697c04ee27`  |
| 2736   | No file              | `d6697c04ee27`  |
| 2726   | No file              | `d6697c04ee27`  |
| 2717   | No file              | `d6697c04ee27`  |
| 2709   | No file              | `d6697c04ee27`  |
| 2703   | No file              | `d6697c04ee27`  |
| 2695   | No file              | `d6697c04ee27`  |
| 2684   | No file              | `d6697c04ee27`  |
| 2672   | No file              | `d6697c04ee27`  |
| 2665   | No file              | `d6697c04ee27`  |
| 2657   | No file              | `d6697c04ee27`  |
| 2649   | No file              | `d6697c04ee27`  |
| 2644   | No file              | `d6697c04ee27`  |
| 2637   | No file              | `d6697c04ee27`  |
| 2629   | No file              | `d6697c04ee27`  |
| 2619   | No file              | `d6697c04ee27`  |
| 2612   | No file              | `d6697c04ee27`  |
| 2606   | No file              | `d6697c04ee27`  |
| 2602   | No file              | `d6697c04ee27`  |
| 2601   | No file              | `d6697c04ee27`  |
| 2592   | No file              | `d6697c04ee27`  |
| 2583   | No file              | `d6697c04ee27`  |
| 2575   | No file              | `d6697c04ee27`  |
| 2567   | No file              | `d6697c04ee27`  |
| 2560   | No file              | `d6697c04ee27`  |
| 2553   | No file              | `d6697c04ee27`  |
| 2545   | No file              | `d6697c04ee27`  |
| 2538   | No file              | `d6697c04ee27`  |
| 2529   | No file              | `d6697c04ee27`  |
| 2519   | No file              | `d6697c04ee27`  |
| 2513   | No file              | `d6697c04ee27`  |
| 2510   | No file              | `d6697c04ee27`  |
| 2507   | No file              | `d6697c04ee27`  |
| 2503   | No file              | `d6697c04ee27`  |
| 2498   | No file              | `d6697c04ee27`  |
| 2492   | No file              | `d6697c04ee27`  |
| 2487   | No file              | `d6697c04ee27`  |
| 2480   | No file              | `d6697c04ee27`  |
| 2474   | No file              | `d6697c04ee27`  |
| 2468   | No file              | `d6697c04ee27`  |
| 2460   | No file              | `d6697c04ee27`  |
| 2453   | No file              | `d6697c04ee27`  |
| 2444   | No file              | `d6697c04ee27`  |
| 2438   | No file              | `d6697c04ee27`  |
| 2434   | No file              | `d6697c04ee27`  |
| 2429   | No file              | `d6697c04ee27`  |
| 2421   | No file              | `d6697c04ee27`  |
| 2414   | No file              | `d6697c04ee27`  |
| 2407   | No file              | `d6697c04ee27`  |
| 2401   | No file              | `d6697c04ee27`  |
| 2397   | No file              | `d6697c04ee27`  |
| 2393   | No file              | `d6697c04ee27`  |
| 2384   | No file              | `d6697c04ee27`  |
| 2378   | No file              | `d6697c04ee27`  |
| 2372   | No file              | `d6697c04ee27`  |
| 2358   | No file              | `d6697c04ee27`  |
| 2352   | No file              | `d6697c04ee27`  |
| 2347   | No file              | `d6697c04ee27`  |
| 2343   | No file              | `d6697c04ee27`  |
| 2335   | No file              | `d6697c04ee27`  |
| 2327   | No file              | `d6697c04ee27`  |
| 2324   | No file              | `d6697c04ee27`  |
| 2319   | No file              | `d6697c04ee27`  |
| 2313   | No file              | `d6697c04ee27`  |
| 2308   | No file              | `d6697c04ee27`  |
| 2302   | No file              | `d6697c04ee27`  |
| 2295   | No file              | `d6697c04ee27`  |
| 2290   | No file              | `d6697c04ee27`  |
| 2284   | No file              | `d6697c04ee27`  |
| 2276   | No file              | `d6697c04ee27`  |
| 2269   | No file              | `d6697c04ee27`  |
| 2259   | No file              | `d6697c04ee27`  |
| 2250   | No file              | `d6697c04ee27`  |
| 2243   | No file              | `d6697c04ee27`  |
| 2235   | No file              | `d6697c04ee27`  |
| 2229   | No file              | `d6697c04ee27`  |
| 2224   | No file              | `d6697c04ee27`  |
| 2218   | No file              | `d6697c04ee27`  |
| 2215   | No file              | `d6697c04ee27`  |
| 2207   | No file              | `d6697c04ee27`  |
| 2203   | No file              | `d6697c04ee27`  |
| 2196   | No file              | `d6697c04ee27`  |
| 2192   | No file              | `d6697c04ee27`  |
| 2189   | No file              | `d6697c04ee27`  |
| 2183   | No file              | `d6697c04ee27`  |
| 2179   | No file              | `d6697c04ee27`  |
| 2171   | No file              | `d6697c04ee27`  |
| 2163   | No file              | `d6697c04ee27`  |
| 2156   | No file              | `d6697c04ee27`  |
| 2151   | No file              | `d6697c04ee27`  |
| 2147   | No file              | `d6697c04ee27`  |
| 2142   | No file              | `d6697c04ee27`  |
| 2138   | No file              | `d6697c04ee27`  |
| 2134   | No file              | `d6697c04ee27`  |
| 2130   | No file              | `d6697c04ee27`  |
| 2122   | No file              | `d6697c04ee27`  |
| 2107   | No file              | `d6697c04ee27`  |
| 2098   | No file              | `d6697c04ee27`  |
| 2089   | No file              | `d6697c04ee27`  |
| 2081   | No file              | `d6697c04ee27`  |
| 2073   | No file              | `d6697c04ee27`  |
| 2067   | No file              | `d6697c04ee27`  |
| 2063   | No file              | `d6697c04ee27`  |
| 2059   | No file              | `d6697c04ee27`  |
| 2052   | No file              | `d6697c04ee27`  |
| 2044   | No file              | `d6697c04ee27`  |
| 2039   | No file              | `d6697c04ee27`  |
| 2032   | No file              | `d6697c04ee27`  |
| 2025   | No file              | `d6697c04ee27`  |
| 2011   | No file              | `d6697c04ee27`  |
| 2005   | No file              | `d6697c04ee27`  |
| 2000   | No file              | `d6697c04ee27`  |
| 1996   | No file              | `d6697c04ee27`  |
| 1991   | No file              | `d6697c04ee27`  |
| 1985   | No file              | `d6697c04ee27`  |
| 1980   | No file              | `d6697c04ee27`  |
| 1969   | No file              | `d6697c04ee27`  |
| 1964   | No file              | `d6697c04ee27`  |
| 1958   | No file              | `d6697c04ee27`  |
| 1950   | No file              | `d6697c04ee27`  |
| 1945   | No file              | `d6697c04ee27`  |
| 1937   | No file              | `d6697c04ee27`  |
| 1933   | No file              | `d6697c04ee27`  |
| 1927   | No file              | `d6697c04ee27`  |
| 1921   | No file              | `d6697c04ee27`  |
| 1914   | No file              | `d6697c04ee27`  |
| 1908   | No file              | `d6697c04ee27`  |
| 1897   | No file              | `d6697c04ee27`  |
| 1892   | No file              | `d6697c04ee27`  |
| 1886   | No file              | `d6697c04ee27`  |
| 1881   | No file              | `d6697c04ee27`  |
| 1871   | No file              | `d6697c04ee27`  |
| 1866   | No file              | `d6697c04ee27`  |
| 1862   | No file              | `d6697c04ee27`  |
| 1854   | No file              | `d6697c04ee27`  |
| 1846   | No file              | `d6697c04ee27`  |
| 1838   | No file              | `d6697c04ee27`  |
| 1832   | No file              | `d6697c04ee27`  |
| 1826   | No file              | `d6697c04ee27`  |
| 1822   | No file              | `d6697c04ee27`  |
| 1818   | No file              | `d6697c04ee27`  |
| 1804   | No file              | `d6697c04ee27`  |
| 1794   | No file              | `d6697c04ee27`  |
| 1790   | No file              | `d6697c04ee27`  |
| 1784   | No file              | `d6697c04ee27`  |
| 1774   | No file              | `d6697c04ee27`  |
| 1771   | No file              | `d6697c04ee27`  |
| 1762   | No file              | `d6697c04ee27`  |
| 1759   | No file              | `d6697c04ee27`  |
| 1754   | No file              | `d6697c04ee27`  |
| 1749   | No file              | `d6697c04ee27`  |
| 1743   | No file              | `d6697c04ee27`  |
| 1737   | No file              | `d6697c04ee27`  |
| 1731   | No file              | `d6697c04ee27`  |
| 1725   | No file              | `d6697c04ee27`  |
| 1717   | No file              | `d6697c04ee27`  |
| 1710   | No file              | `d6697c04ee27`  |
| 1704   | No file              | `d6697c04ee27`  |
| 1698   | No file              | `d6697c04ee27`  |
| 1690   | No file              | `d6697c04ee27`  |
| 1685   | No file              | `d6697c04ee27`  |
| 1680   | No file              | `d6697c04ee27`  |
| 1674   | No file              | `d6697c04ee27`  |
| 1668   | No file              | `d6697c04ee27`  |
| 1659   | No file              | `d6697c04ee27`  |
| 1649   | No file              | `d6697c04ee27`  |
| 1642   | No file              | `d6697c04ee27`  |
| 1636   | No file              | `d6697c04ee27`  |
| 1628   | No file              | `d6697c04ee27`  |
| 1622   | No file              | `d6697c04ee27`  |
| 1614   | No file              | `d6697c04ee27`  |
| 1608   | No file              | `d6697c04ee27`  |
| 1602   | No file              | `d6697c04ee27`  |
| 1598   | No file              | `d6697c04ee27`  |
| 1594   | No file              | `d6697c04ee27`  |
| 1590   | No file              | `d6697c04ee27`  |
| 1587   | No file              | `d6697c04ee27`  |
| 1584   | No file              | `d6697c04ee27`  |
| 1579   | No file              | `d6697c04ee27`  |
| 1572   | No file              | `d6697c04ee27`  |
| 1565   | No file              | `d6697c04ee27`  |
| 1559   | No file              | `d6697c04ee27`  |
| 1554   | No file              | `d6697c04ee27`  |
| 1547   | No file              | `d6697c04ee27`  |
| 1537   | No file              | `d6697c04ee27`  |
| 1529   | No file              | `d6697c04ee27`  |
| 1524   | No file              | `d6697c04ee27`  |
| 1519   | No file              | `d6697c04ee27`  |
| 1509   | No file              | `d6697c04ee27`  |
| 1506   | No file              | `d6697c04ee27`  |
| 1504   | No file              | `d6697c04ee27`  |
| 1500   | No file              | `d6697c04ee27`  |
| 1493   | No file              | `d6697c04ee27`  |
| 1489   | No file              | `d6697c04ee27`  |
| 1485   | No file              | `d6697c04ee27`  |
| 1481   | No file              | `d6697c04ee27`  |
| 1474   | No file              | `d6697c04ee27`  |
| 1466   | No file              | `d6697c04ee27`  |
| 1462   | No file              | `d6697c04ee27`  |
| 1459   | No file              | `d6697c04ee27`  |
| 1453   | No file              | `d6697c04ee27`  |
| 1450   | No file              | `d6697c04ee27`  |
| 1445   | No file              | `d6697c04ee27`  |
| 1439   | No file              | `d6697c04ee27`  |
| 1433   | No file              | `d6697c04ee27`  |
| 1430   | No file              | `d6697c04ee27`  |
| 1426   | No file              | `d6697c04ee27`  |
| 1421   | No file              | `d6697c04ee27`  |
| 1417   | No file              | `d6697c04ee27`  |
| 1416   | No file              | `d6697c04ee27`  |
| 1409   | No file              | `d6697c04ee27`  |
| 1405   | No file              | `d6697c04ee27`  |
| 1401   | No file              | `d6697c04ee27`  |
| 1396   | No file              | `d6697c04ee27`  |
| 1391   | No file              | `d6697c04ee27`  |
| 1390   | No file              | `d6697c04ee27`  |
| 1386   | No file              | `d6697c04ee27`  |
| 1381   | No file              | `d6697c04ee27`  |
| 1379   | No file              | `d6697c04ee27`  |
| 1372   | No file              | `d6697c04ee27`  |
| 1366   | No file              | `d6697c04ee27`  |
| 1364   | No file              | `d6697c04ee27`  |
| 1363   | No file              | `d6697c04ee27`  |
| 1360   | No file              | `d6697c04ee27`  |
| 1358   | No file              | `d6697c04ee27`  |
| 1355   | No file              | `d6697c04ee27`  |
| 1351   | No file              | `d6697c04ee27`  |
| 1348   | No file              | `d6697c04ee27`  |
| 1346   | No file              | `d6697c04ee27`  |
| 1341   | No file              | `d6697c04ee27`  |
| 1340   | No file              | `d6697c04ee27`  |
| 1338   | No file              | `d6697c04ee27`  |
| 1335   | No file              | `d6697c04ee27`  |
| 1333   | No file              | `d6697c04ee27`  |
| 1329   | No file              | `d6697c04ee27`  |
| 1327   | No file              | `d6697c04ee27`  |
| 1324   | No file              | `d6697c04ee27`  |
| 1321   | No file              | `d6697c04ee27`  |
| 1319   | No file              | `d6697c04ee27`  |
| 1318   | No file              | `d6697c04ee27`  |
| 1316   | No file              | `d6697c04ee27`  |
| 1313   | No file              | `d6697c04ee27`  |
| 1311   | No file              | `d6697c04ee27`  |
| 1309   | No file              | `d6697c04ee27`  |
| 1304   | No file              | `d6697c04ee27`  |
| 1292   | No file              | `d6697c04ee27`  |
| 1286   | No file              | `d6697c04ee27`  |
| 1280   | No file              | `d6697c04ee27`  |
| 1276   | No file              | `d6697c04ee27`  |
| 1267   | No file              | `d6697c04ee27`  |
| 1261   | No file              | `d6697c04ee27`  |
| 1256   | No file              | `d6697c04ee27`  |
| 1250   | No file              | `d6697c04ee27`  |
| 1246   | No file              | `d6697c04ee27`  |
| 1239   | No file              | `d6697c04ee27`  |
| 1230   | No file              | `d6697c04ee27`  |
| 1226   | No file              | `d6697c04ee27`  |
| 1220   | No file              | `d6697c04ee27`  |
| 1217   | No file              | `d6697c04ee27`  |
| 1211   | No file              | `d6697c04ee27`  |
| 1210   | No file              | `d6697c04ee27`  |
| 1208   | No file              | `d6697c04ee27`  |
| 1203   | No file              | `d6697c04ee27`  |
| 1197   | No file              | `d6697c04ee27`  |
| 1194   | No file              | `d6697c04ee27`  |
| 1192   | No file              | `d6697c04ee27`  |
| 1187   | No file              | `d6697c04ee27`  |
| 1183   | No file              | `d6697c04ee27`  |
| 1177   | No file              | `d6697c04ee27`  |
| 1173   | No file              | `d6697c04ee27`  |
| 1167   | No file              | `d6697c04ee27`  |
| 1164   | No file              | `d6697c04ee27`  |
| 1156   | No file              | `d6697c04ee27`  |
| 1149   | No file              | `d6697c04ee27`  |
| 1144   | No file              | `d6697c04ee27`  |
| 1137   | No file              | `d6697c04ee27`  |
| 1132   | No file              | `d6697c04ee27`  |
| 1127   | No file              | `d6697c04ee27`  |
| 1122   | No file              | `d6697c04ee27`  |
| 1118   | No file              | `d6697c04ee27`  |
| 1114   | No file              | `d6697c04ee27`  |
| 1109   | No file              | `d6697c04ee27`  |
| 1102   | No file              | `d6697c04ee27`  |
| 1096   | No file              | `d6697c04ee27`  |
| 1088   | No file              | `d6697c04ee27`  |
| 1081   | No file              | `d6697c04ee27`  |
| 1076   | No file              | `d6697c04ee27`  |
| 1069   | No file              | `d6697c04ee27`  |
| 1064   | No file              | `d6697c04ee27`  |
| 1058   | No file              | `d6697c04ee27`  |
| 1051   | No file              | `d6697c04ee27`  |
| 1044   | No file              | `d6697c04ee27`  |
| 1036   | No file              | `d6697c04ee27`  |
| 1026   | No file              | `d6697c04ee27`  |
| 1016   | No file              | `d6697c04ee27`  |
| 1009   | No file              | `d6697c04ee27`  |
| 1005   | No file              | `d6697c04ee27`  |
| 1000   | No file              | `d6697c04ee27`  |
| 998    | No file              | `d6697c04ee27`  |
| 990    | No file              | `d6697c04ee27`  |
| 979    | No file              | `d6697c04ee27`  |
| 972    | No file              | `d6697c04ee27`  |
| 963    | No file              | `d6697c04ee27`  |
| 955    | No file              | `d6697c04ee27`  |
| 946    | No file              | `d6697c04ee27`  |
| 938    | No file              | `d6697c04ee27`  |
| 927    | No file              | `d6697c04ee27`  |
| 911    | No file              | `d6697c04ee27`  |
| 904    | No file              | `d6697c04ee27`  |
| 899    | No file              | `d6697c04ee27`  |
| 894    | No file              | `d6697c04ee27`  |
| 885    | No file              | `d6697c04ee27`  |
| 879    | No file              | `d6697c04ee27`  |
| 872    | No file              | `d6697c04ee27`  |
| 864    | No file              | `d6697c04ee27`  |
| 855    | No file              | `d6697c04ee27`  |
| 853    | No file              | `d6697c04ee27`  |
| 845    | No file              | `d6697c04ee27`  |
| 837    | No file              | `d6697c04ee27`  |
| 829    | No file              | `d6697c04ee27`  |
| 822    | No file              | `d6697c04ee27`  |
| 814    | No file              | `d6697c04ee27`  |
| 805    | No file              | `d6697c04ee27`  |
| 794    | No file              | `d6697c04ee27`  |
| 787    | No file              | `d6697c04ee27`  |
| 780    | No file              | `d6697c04ee27`  |
| 771    | No file              | `d6697c04ee27`  |
| 760    | No file              | `d6697c04ee27`  |
| 748    | No file              | `d6697c04ee27`  |
| 741    | No file              | `d6697c04ee27`  |
| 736    | No file              | `d6697c04ee27`  |
| 731    | No file              | `d6697c04ee27`  |
| 723    | No file              | `d6697c04ee27`  |
| 711    | No file              | `d6697c04ee27`  |
| 707    | No file              | `d6697c04ee27`  |
| 697    | No file              | `d6697c04ee27`  |
| 689    | No file              | `d6697c04ee27`  |
| 683    | No file              | `d6697c04ee27`  |
| 678    | No file              | `d6697c04ee27`  |
| 670    | No file              | `d6697c04ee27`  |
| 661    | No file              | `d6697c04ee27`  |
| 656    | No file              | `d6697c04ee27`  |
| 652    | No file              | `d6697c04ee27`  |
| 643    | No file              | `d6697c04ee27`  |
| 637    | No file              | `d6697c04ee27`  |
| 630    | No file              | `d6697c04ee27`  |
| 627    | No file              | `d6697c04ee27`  |
| 621    | No file              | `d6697c04ee27`  |
| 617    | No file              | `d6697c04ee27`  |
| 615    | No file              | `d6697c04ee27`  |
| 606    | No file              | `d6697c04ee27`  |
| 599    | No file              | `d6697c04ee27`  |
| 592    | No file              | `d6697c04ee27`  |
| 586    | No file              | `d6697c04ee27`  |
| 577    | No file              | `d6697c04ee27`  |
| 569    | No file              | `d6697c04ee27`  |
| 561    | No file              | `d6697c04ee27`  |
| 554    | No file              | `d6697c04ee27`  |
| 542    | No file              | `d6697c04ee27`  |
| 532    | No file              | `d6697c04ee27`  |
| 531    | No file              | `d6697c04ee27`  |
| 526    | No file              | `d6697c04ee27`  |
| 521    | No file              | `d6697c04ee27`  |
| 517    | No file              | `d6697c04ee27`  |
| 510    | No file              | `d6697c04ee27`  |
| 508    | No file              | `d6697c04ee27`  |
| 504    | No file              | `d6697c04ee27`  |
| 497    | No file              | `d6697c04ee27`  |
| 491    | No file              | `d6697c04ee27`  |
| 485    | No file              | `d6697c04ee27`  |
| 478    | No file              | `d6697c04ee27`  |
| 472    | No file              | `d6697c04ee27`  |
| 466    | No file              | `d6697c04ee27`  |
| 457    | No file              | `d6697c04ee27`  |
| 452    | No file              | `d6697c04ee27`  |
| 449    | No file              | `d6697c04ee27`  |
| 435    | No file              | `d6697c04ee27`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `stringtable.bss`     | Optional | Key hashes of the `GAME` sheet keys, for their LOC type 37 text |
| `languagedata_en.loc` | Optional | LOC type 37 text of the chapter, title and story keys |

All multi-byte values are little-endian.

## Layout 3

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

## Layout 2

Layout 3 without `unknown_36`.

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

## Layout 1

The list textures are two lists: the three select button textures (slots
`0` to `2` of Layout 3), then four slots (`3` to `6`) per journal list.

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
| `+0x00` | u32[4] | texture_info_refs | Slots `3` to `6` of Layout 3: frame, bar, title key, text key |

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
highest quest ID of the chain in `quest.dbss`. Layouts 1 and 2 have no `unknown_36`.
