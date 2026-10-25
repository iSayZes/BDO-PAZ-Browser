# `charactersimply.bss` Format

## Purpose

Stores one fixed 119-byte row per character template (player classes, NPCs, monsters, mounts, objects): the character ID, its kind, grade, level and group, spawn hours, body size and height, HP, vehicle settings, display and interaction flags, and string-table indexes for the model path, the voice bank, the Korean name and title, the action script and the interaction condition. It holds the same 24,553 characters as [characterstatic.dbss](../dbss/characterstatic_dbss.md) (client 3474), and every field it shares with that file holds the same value; see [Field Names](#field-names). Names and titles in the user's language come from LOC type `6`, keyed by `character_id`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                  | Bytes     | Records    | Row bytes |
| ------ | -------------- | --------------------- | --------- | ---------- | --------- |
| 2      | 3464 and later | `charactersimply.bss` | 3,849,053 | 24,445 Row | 119       |
| 1      | 1762 to 2553   | `charactersimply.bss` | 3,367,224 | 21,220 Row | 121       |

| Layout | File                  | Known               | Unknown           |
| ------ | --------------------- | ------------------- | ----------------- |
| 2      | `charactersimply.bss` | 3,286,818 B (85.4%) | 562,235 B (14.6%) |
| 1      | `charactersimply.bss` | 2,836,724 B (84.2%) | 530,500 B (15.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `5bfba18001de`  |
| 3482   | Layout 2             | `5bfba18001de`  |
| 3474   | Layout 2             | `5bfba18001de`  |
| 3473   | Layout 2             | `5bfba18001de`  |
| 3464   | Layout 2             | `5bfba18001de`  |
| 3458   | No documented layout | `5bfba18001de`  |
| 3454   | No documented layout | `5bfba18001de`  |
| 3444   | No documented layout | `5bfba18001de`  |
| 3435   | No documented layout | `5bfba18001de`  |
| 3426   | No documented layout | `5bfba18001de`  |
| 3418   | No documented layout | `5bfba18001de`  |
| 3412   | No documented layout | `5bfba18001de`  |
| 3402   | No documented layout | `5bfba18001de`  |
| 3396   | No documented layout | `5bfba18001de`  |
| 3387   | No documented layout | `5bfba18001de`  |
| 3381   | No documented layout | `5bfba18001de`  |
| 3373   | No documented layout | `5bfba18001de`  |
| 3364   | No documented layout | `5bfba18001de`  |
| 3356   | No documented layout | `5bfba18001de`  |
| 3349   | No documented layout | `5bfba18001de`  |
| 3342   | No documented layout | `5bfba18001de`  |
| 3335   | No documented layout | `5bfba18001de`  |
| 3326   | No documented layout | `5bfba18001de`  |
| 3321   | No documented layout | `5bfba18001de`  |
| 3314   | No documented layout | `5bfba18001de`  |
| 3303   | No documented layout | `5bfba18001de`  |
| 3302   | No documented layout | `5bfba18001de`  |
| 3293   | No documented layout | `5bfba18001de`  |
| 3283   | No documented layout | `5bfba18001de`  |
| 3275   | No documented layout | `5bfba18001de`  |
| 3267   | No documented layout | `5bfba18001de`  |
| 3258   | No documented layout | `5bfba18001de`  |
| 3251   | No documented layout | `5bfba18001de`  |
| 3242   | No documented layout | `5bfba18001de`  |
| 3235   | No documented layout | `5bfba18001de`  |
| 3229   | No documented layout | `5bfba18001de`  |
| 3212   | No documented layout | `5bfba18001de`  |
| 3203   | No documented layout | `5bfba18001de`  |
| 3193   | No documented layout | `5bfba18001de`  |
| 3186   | No documented layout | `5bfba18001de`  |
| 3177   | No documented layout | `5bfba18001de`  |
| 3169   | No documented layout | `5bfba18001de`  |
| 3158   | No documented layout | `5bfba18001de`  |
| 3151   | No documented layout | `5bfba18001de`  |
| 3144   | No documented layout | `5bfba18001de`  |
| 3133   | No documented layout | `5bfba18001de`  |
| 3125   | No documented layout | `5bfba18001de`  |
| 3118   | No documented layout | `5bfba18001de`  |
| 3111   | No documented layout | `5bfba18001de`  |
| 3103   | No documented layout | `5bfba18001de`  |
| 3095   | No documented layout | `5bfba18001de`  |
| 3086   | No documented layout | `5bfba18001de`  |
| 3072   | No documented layout | `5bfba18001de`  |
| 3062   | No documented layout | `5bfba18001de`  |
| 3052   | No documented layout | `5bfba18001de`  |
| 3045   | No documented layout | `5bfba18001de`  |
| 3037   | No documented layout | `5bfba18001de`  |
| 3030   | No documented layout | `5bfba18001de`  |
| 3021   | No documented layout | `5bfba18001de`  |
| 3012   | No documented layout | `5bfba18001de`  |
| 3002   | No documented layout | `5bfba18001de`  |
| 2995   | No documented layout | `5bfba18001de`  |
| 2987   | No documented layout | `5bfba18001de`  |
| 2978   | No documented layout | `5bfba18001de`  |
| 2970   | No documented layout | `5bfba18001de`  |
| 2959   | No documented layout | `5bfba18001de`  |
| 2951   | No documented layout | `5bfba18001de`  |
| 2942   | No documented layout | `5bfba18001de`  |
| 2935   | No documented layout | `5bfba18001de`  |
| 2932   | No documented layout | `5bfba18001de`  |
| 2923   | No documented layout | `5bfba18001de`  |
| 2919   | No documented layout | `5bfba18001de`  |
| 2907   | No documented layout | `5bfba18001de`  |
| 2900   | No documented layout | `5bfba18001de`  |
| 2891   | No documented layout | `5bfba18001de`  |
| 2882   | No documented layout | `5bfba18001de`  |
| 2872   | No documented layout | `5bfba18001de`  |
| 2863   | No documented layout | `5bfba18001de`  |
| 2855   | No documented layout | `5bfba18001de`  |
| 2849   | No documented layout | `5bfba18001de`  |
| 2844   | No documented layout | `5bfba18001de`  |
| 2834   | No documented layout | `5bfba18001de`  |
| 2825   | No documented layout | `5bfba18001de`  |
| 2819   | No documented layout | `5bfba18001de`  |
| 2811   | No documented layout | `5bfba18001de`  |
| 2803   | No documented layout | `5bfba18001de`  |
| 2794   | No documented layout | `5bfba18001de`  |
| 2783   | No documented layout | `5bfba18001de`  |
| 2774   | No documented layout | `5bfba18001de`  |
| 2765   | No documented layout | `5bfba18001de`  |
| 2756   | No documented layout | `5bfba18001de`  |
| 2750   | No documented layout | `5bfba18001de`  |
| 2743   | No documented layout | `5bfba18001de`  |
| 2736   | No documented layout | `5bfba18001de`  |
| 2726   | No documented layout | `5bfba18001de`  |
| 2717   | No documented layout | `5bfba18001de`  |
| 2709   | No documented layout | `5bfba18001de`  |
| 2703   | No documented layout | `5bfba18001de`  |
| 2695   | No documented layout | `5bfba18001de`  |
| 2684   | No documented layout | `5bfba18001de`  |
| 2672   | No documented layout | `5bfba18001de`  |
| 2665   | No documented layout | `5bfba18001de`  |
| 2657   | No documented layout | `5bfba18001de`  |
| 2649   | No documented layout | `5bfba18001de`  |
| 2644   | No documented layout | `5bfba18001de`  |
| 2637   | No documented layout | `5bfba18001de`  |
| 2629   | No documented layout | `5bfba18001de`  |
| 2619   | No documented layout | `5bfba18001de`  |
| 2612   | No documented layout | `5bfba18001de`  |
| 2606   | No documented layout | `5bfba18001de`  |
| 2602   | No documented layout | `5bfba18001de`  |
| 2601   | No documented layout | `5bfba18001de`  |
| 2592   | No documented layout | `5bfba18001de`  |
| 2583   | No documented layout | `5bfba18001de`  |
| 2575   | No documented layout | `5bfba18001de`  |
| 2567   | No documented layout | `5bfba18001de`  |
| 2560   | No documented layout | `5bfba18001de`  |
| 2553   | Layout 1             | `5bfba18001de`  |
| 2545   | Layout 1             | `5bfba18001de`  |
| 2538   | Layout 1             | `5bfba18001de`  |
| 2529   | Layout 1             | `5bfba18001de`  |
| 2519   | Layout 1             | `5bfba18001de`  |
| 2513   | Layout 1             | `5bfba18001de`  |
| 2510   | Layout 1             | `5bfba18001de`  |
| 2507   | Layout 1             | `5bfba18001de`  |
| 2503   | Layout 1             | `5bfba18001de`  |
| 2498   | Layout 1             | `5bfba18001de`  |
| 2492   | Layout 1             | `5bfba18001de`  |
| 2487   | Layout 1             | `5bfba18001de`  |
| 2480   | Layout 1             | `5bfba18001de`  |
| 2474   | Layout 1             | `5bfba18001de`  |
| 2468   | Layout 1             | `5bfba18001de`  |
| 2460   | Layout 1             | `5bfba18001de`  |
| 2453   | Layout 1             | `5bfba18001de`  |
| 2444   | Layout 1             | `5bfba18001de`  |
| 2438   | Layout 1             | `5bfba18001de`  |
| 2434   | Layout 1             | `5bfba18001de`  |
| 2429   | Layout 1             | `5bfba18001de`  |
| 2421   | Layout 1             | `5bfba18001de`  |
| 2414   | Layout 1             | `5bfba18001de`  |
| 2407   | Layout 1             | `5bfba18001de`  |
| 2401   | Layout 1             | `5bfba18001de`  |
| 2397   | Layout 1             | `5bfba18001de`  |
| 2393   | Layout 1             | `5bfba18001de`  |
| 2384   | Layout 1             | `5bfba18001de`  |
| 2378   | Layout 1             | `5bfba18001de`  |
| 2372   | Layout 1             | `5bfba18001de`  |
| 2358   | Layout 1             | `5bfba18001de`  |
| 2352   | Layout 1             | `5bfba18001de`  |
| 2347   | Layout 1             | `5bfba18001de`  |
| 2343   | Layout 1             | `5bfba18001de`  |
| 2335   | Layout 1             | `5bfba18001de`  |
| 2327   | Layout 1             | `5bfba18001de`  |
| 2324   | Layout 1             | `5bfba18001de`  |
| 2319   | Layout 1             | `5bfba18001de`  |
| 2313   | Layout 1             | `5bfba18001de`  |
| 2308   | Layout 1             | `5bfba18001de`  |
| 2302   | Layout 1             | `5bfba18001de`  |
| 2295   | Layout 1             | `5bfba18001de`  |
| 2290   | Layout 1             | `5bfba18001de`  |
| 2284   | Layout 1             | `5bfba18001de`  |
| 2276   | Layout 1             | `5bfba18001de`  |
| 2269   | Layout 1             | `5bfba18001de`  |
| 2259   | Layout 1             | `5bfba18001de`  |
| 2250   | Layout 1             | `5bfba18001de`  |
| 2243   | Layout 1             | `5bfba18001de`  |
| 2235   | Layout 1             | `5bfba18001de`  |
| 2229   | Layout 1             | `5bfba18001de`  |
| 2224   | Layout 1             | `5bfba18001de`  |
| 2218   | Layout 1             | `5bfba18001de`  |
| 2215   | Layout 1             | `5bfba18001de`  |
| 2207   | Layout 1             | `5bfba18001de`  |
| 2203   | Layout 1             | `5bfba18001de`  |
| 2196   | Layout 1             | `5bfba18001de`  |
| 2192   | Layout 1             | `5bfba18001de`  |
| 2189   | Layout 1             | `5bfba18001de`  |
| 2183   | Layout 1             | `5bfba18001de`  |
| 2179   | Layout 1             | `5bfba18001de`  |
| 2171   | Layout 1             | `5bfba18001de`  |
| 2163   | Layout 1             | `5bfba18001de`  |
| 2156   | Layout 1             | `5bfba18001de`  |
| 2151   | Layout 1             | `5bfba18001de`  |
| 2147   | Layout 1             | `5bfba18001de`  |
| 2142   | Layout 1             | `5bfba18001de`  |
| 2138   | Layout 1             | `5bfba18001de`  |
| 2134   | Layout 1             | `5bfba18001de`  |
| 2130   | Layout 1             | `5bfba18001de`  |
| 2122   | Layout 1             | `5bfba18001de`  |
| 2107   | Layout 1             | `5bfba18001de`  |
| 2098   | Layout 1             | `5bfba18001de`  |
| 2089   | Layout 1             | `5bfba18001de`  |
| 2081   | Layout 1             | `5bfba18001de`  |
| 2073   | Layout 1             | `5bfba18001de`  |
| 2067   | Layout 1             | `5bfba18001de`  |
| 2063   | Layout 1             | `5bfba18001de`  |
| 2059   | Layout 1             | `5bfba18001de`  |
| 2052   | Layout 1             | `5bfba18001de`  |
| 2044   | Layout 1             | `5bfba18001de`  |
| 2039   | Layout 1             | `5bfba18001de`  |
| 2032   | Layout 1             | `5bfba18001de`  |
| 2025   | Layout 1             | `5bfba18001de`  |
| 2011   | Layout 1             | `5bfba18001de`  |
| 2005   | Layout 1             | `5bfba18001de`  |
| 2000   | Layout 1             | `5bfba18001de`  |
| 1996   | Layout 1             | `5bfba18001de`  |
| 1991   | Layout 1             | `5bfba18001de`  |
| 1985   | Layout 1             | `5bfba18001de`  |
| 1980   | Layout 1             | `5bfba18001de`  |
| 1969   | Layout 1             | `5bfba18001de`  |
| 1964   | Layout 1             | `5bfba18001de`  |
| 1958   | Layout 1             | `5bfba18001de`  |
| 1950   | Layout 1             | `5bfba18001de`  |
| 1945   | Layout 1             | `5bfba18001de`  |
| 1937   | Layout 1             | `5bfba18001de`  |
| 1933   | Layout 1             | `5bfba18001de`  |
| 1927   | Layout 1             | `5bfba18001de`  |
| 1921   | Layout 1             | `5bfba18001de`  |
| 1914   | Layout 1             | `5bfba18001de`  |
| 1908   | Layout 1             | `5bfba18001de`  |
| 1897   | Layout 1             | `5bfba18001de`  |
| 1892   | Layout 1             | `5bfba18001de`  |
| 1886   | Layout 1             | `5bfba18001de`  |
| 1881   | Layout 1             | `5bfba18001de`  |
| 1871   | Layout 1             | `5bfba18001de`  |
| 1866   | Layout 1             | `5bfba18001de`  |
| 1862   | Layout 1             | `5bfba18001de`  |
| 1854   | Layout 1             | `5bfba18001de`  |
| 1846   | Layout 1             | `5bfba18001de`  |
| 1838   | Layout 1             | `5bfba18001de`  |
| 1832   | Layout 1             | `5bfba18001de`  |
| 1826   | Layout 1             | `5bfba18001de`  |
| 1822   | Layout 1             | `5bfba18001de`  |
| 1818   | Layout 1             | `5bfba18001de`  |
| 1804   | Layout 1             | `5bfba18001de`  |
| 1794   | Layout 1             | `5bfba18001de`  |
| 1790   | Layout 1             | `5bfba18001de`  |
| 1784   | Layout 1             | `5bfba18001de`  |
| 1774   | Layout 1             | `5bfba18001de`  |
| 1771   | Layout 1             | `5bfba18001de`  |
| 1762   | Layout 1             | `5bfba18001de`  |
| 1759   | No documented layout | `5bfba18001de`  |
| 1754   | No documented layout | `5bfba18001de`  |
| 1749   | No documented layout | `5bfba18001de`  |
| 1743   | No documented layout | `5bfba18001de`  |
| 1737   | No documented layout | `5bfba18001de`  |
| 1731   | No documented layout | `5bfba18001de`  |
| 1725   | No documented layout | `5bfba18001de`  |
| 1717   | No documented layout | `5bfba18001de`  |
| 1710   | No documented layout | `5bfba18001de`  |
| 1704   | No documented layout | `5bfba18001de`  |
| 1698   | No documented layout | `5bfba18001de`  |
| 1690   | No documented layout | `5bfba18001de`  |
| 1685   | No documented layout | `5bfba18001de`  |
| 1680   | No documented layout | `5bfba18001de`  |
| 1674   | No documented layout | `5bfba18001de`  |
| 1668   | No documented layout | `5bfba18001de`  |
| 1659   | No documented layout | `5bfba18001de`  |
| 1649   | No documented layout | `5bfba18001de`  |
| 1642   | No documented layout | `5bfba18001de`  |
| 1636   | No documented layout | `5bfba18001de`  |
| 1628   | No documented layout | `5bfba18001de`  |
| 1622   | No documented layout | `5bfba18001de`  |
| 1614   | No documented layout | `5bfba18001de`  |
| 1608   | No documented layout | `5bfba18001de`  |
| 1602   | No documented layout | `5bfba18001de`  |
| 1598   | No documented layout | `5bfba18001de`  |
| 1594   | No documented layout | `5bfba18001de`  |
| 1590   | No documented layout | `5bfba18001de`  |
| 1587   | No documented layout | `5bfba18001de`  |
| 1584   | No documented layout | `5bfba18001de`  |
| 1579   | No documented layout | `5bfba18001de`  |
| 1572   | No documented layout | `5bfba18001de`  |
| 1565   | No documented layout | `5bfba18001de`  |
| 1559   | No documented layout | `5bfba18001de`  |
| 1554   | No documented layout | `5bfba18001de`  |
| 1547   | No documented layout | `5bfba18001de`  |
| 1537   | No documented layout | `5bfba18001de`  |
| 1529   | No documented layout | `5bfba18001de`  |
| 1524   | No documented layout | `5bfba18001de`  |
| 1519   | No documented layout | `5bfba18001de`  |
| 1509   | No documented layout | `5bfba18001de`  |
| 1506   | No documented layout | `5bfba18001de`  |
| 1504   | No documented layout | `5bfba18001de`  |
| 1500   | No documented layout | `5bfba18001de`  |
| 1493   | No documented layout | `5bfba18001de`  |
| 1489   | No documented layout | `5bfba18001de`  |
| 1485   | No documented layout | `5bfba18001de`  |
| 1481   | No documented layout | `5bfba18001de`  |
| 1474   | No documented layout | `5bfba18001de`  |
| 1466   | No documented layout | `5bfba18001de`  |
| 1462   | No documented layout | `5bfba18001de`  |
| 1459   | No documented layout | `5bfba18001de`  |
| 1453   | No documented layout | `5bfba18001de`  |
| 1450   | No documented layout | `5bfba18001de`  |
| 1445   | No documented layout | `5bfba18001de`  |
| 1439   | No documented layout | `5bfba18001de`  |
| 1433   | No documented layout | `5bfba18001de`  |
| 1430   | No documented layout | `5bfba18001de`  |
| 1426   | No documented layout | `5bfba18001de`  |
| 1421   | No documented layout | `5bfba18001de`  |
| 1417   | No documented layout | `5bfba18001de`  |
| 1416   | No documented layout | `5bfba18001de`  |
| 1409   | No documented layout | `5bfba18001de`  |
| 1405   | No documented layout | `5bfba18001de`  |
| 1401   | No documented layout | `5bfba18001de`  |
| 1396   | No documented layout | `5bfba18001de`  |
| 1391   | No documented layout | `5bfba18001de`  |
| 1390   | No documented layout | `5bfba18001de`  |
| 1386   | No documented layout | `5bfba18001de`  |
| 1381   | No documented layout | `5bfba18001de`  |
| 1379   | No documented layout | `5bfba18001de`  |
| 1372   | No documented layout | `5bfba18001de`  |
| 1366   | No documented layout | `5bfba18001de`  |
| 1364   | No documented layout | `5bfba18001de`  |
| 1363   | No documented layout | `5bfba18001de`  |
| 1360   | No documented layout | `5bfba18001de`  |
| 1358   | No documented layout | `5bfba18001de`  |
| 1355   | No documented layout | `5bfba18001de`  |
| 1351   | No documented layout | `5bfba18001de`  |
| 1348   | No documented layout | `5bfba18001de`  |
| 1346   | No documented layout | `5bfba18001de`  |
| 1341   | No documented layout | `5bfba18001de`  |
| 1340   | No documented layout | `5bfba18001de`  |
| 1338   | No documented layout | `5bfba18001de`  |
| 1335   | No documented layout | `5bfba18001de`  |
| 1333   | No documented layout | `5bfba18001de`  |
| 1329   | No documented layout | `5bfba18001de`  |
| 1327   | No documented layout | `5bfba18001de`  |
| 1324   | No documented layout | `5bfba18001de`  |
| 1321   | No documented layout | `5bfba18001de`  |
| 1319   | No documented layout | `5bfba18001de`  |
| 1318   | No documented layout | `5bfba18001de`  |
| 1316   | No documented layout | `5bfba18001de`  |
| 1313   | No documented layout | `5bfba18001de`  |
| 1311   | No documented layout | `5bfba18001de`  |
| 1309   | No documented layout | `5bfba18001de`  |
| 1304   | No documented layout | `5bfba18001de`  |
| 1292   | No documented layout | `5bfba18001de`  |
| 1286   | No documented layout | `5bfba18001de`  |
| 1280   | No documented layout | `5bfba18001de`  |
| 1276   | No documented layout | `5bfba18001de`  |
| 1267   | No documented layout | `5bfba18001de`  |
| 1261   | No documented layout | `5bfba18001de`  |
| 1256   | No documented layout | `5bfba18001de`  |
| 1250   | No documented layout | `5bfba18001de`  |
| 1246   | No documented layout | `5bfba18001de`  |
| 1239   | No documented layout | `5bfba18001de`  |
| 1230   | No documented layout | `5bfba18001de`  |
| 1226   | No documented layout | `5bfba18001de`  |
| 1220   | No documented layout | `5bfba18001de`  |
| 1217   | No file              | `5bfba18001de`  |
| 1211   | No file              | `5bfba18001de`  |
| 1210   | No file              | `5bfba18001de`  |
| 1208   | No file              | `5bfba18001de`  |
| 1203   | No file              | `5bfba18001de`  |
| 1197   | No file              | `5bfba18001de`  |
| 1194   | No file              | `5bfba18001de`  |
| 1192   | No file              | `5bfba18001de`  |
| 1187   | No file              | `5bfba18001de`  |
| 1183   | No file              | `5bfba18001de`  |
| 1177   | No file              | `5bfba18001de`  |
| 1173   | No file              | `5bfba18001de`  |
| 1167   | No file              | `5bfba18001de`  |
| 1164   | No file              | `5bfba18001de`  |
| 1156   | No file              | `5bfba18001de`  |
| 1149   | No file              | `5bfba18001de`  |
| 1144   | No file              | `5bfba18001de`  |
| 1137   | No file              | `5bfba18001de`  |
| 1132   | No file              | `5bfba18001de`  |
| 1127   | No file              | `5bfba18001de`  |
| 1122   | No file              | `5bfba18001de`  |
| 1118   | No file              | `5bfba18001de`  |
| 1114   | No file              | `5bfba18001de`  |
| 1109   | No file              | `5bfba18001de`  |
| 1102   | No file              | `5bfba18001de`  |
| 1096   | No file              | `5bfba18001de`  |
| 1088   | No file              | `5bfba18001de`  |
| 1081   | No file              | `5bfba18001de`  |
| 1076   | No file              | `5bfba18001de`  |
| 1069   | No file              | `5bfba18001de`  |
| 1064   | No file              | `5bfba18001de`  |
| 1058   | No file              | `5bfba18001de`  |
| 1051   | No file              | `5bfba18001de`  |
| 1044   | No file              | `5bfba18001de`  |
| 1036   | No file              | `5bfba18001de`  |
| 1026   | No file              | `5bfba18001de`  |
| 1016   | No file              | `5bfba18001de`  |
| 1009   | No file              | `5bfba18001de`  |
| 1005   | No file              | `5bfba18001de`  |
| 1000   | No file              | `5bfba18001de`  |
| 998    | No file              | `5bfba18001de`  |
| 990    | No file              | `5bfba18001de`  |
| 979    | No file              | `5bfba18001de`  |
| 972    | No file              | `5bfba18001de`  |
| 963    | No file              | `5bfba18001de`  |
| 955    | No file              | `5bfba18001de`  |
| 946    | No file              | `5bfba18001de`  |
| 938    | No file              | `5bfba18001de`  |
| 927    | No file              | `5bfba18001de`  |
| 911    | No file              | `5bfba18001de`  |
| 904    | No file              | `5bfba18001de`  |
| 899    | No file              | `5bfba18001de`  |
| 894    | No file              | `5bfba18001de`  |
| 885    | No file              | `5bfba18001de`  |
| 879    | No file              | `5bfba18001de`  |
| 872    | No file              | `5bfba18001de`  |
| 864    | No file              | `5bfba18001de`  |
| 855    | No file              | `5bfba18001de`  |
| 853    | No file              | `5bfba18001de`  |
| 845    | No file              | `5bfba18001de`  |
| 837    | No file              | `5bfba18001de`  |
| 829    | No file              | `5bfba18001de`  |
| 822    | No file              | `5bfba18001de`  |
| 814    | No file              | `5bfba18001de`  |
| 805    | No file              | `5bfba18001de`  |
| 794    | No file              | `5bfba18001de`  |
| 787    | No file              | `5bfba18001de`  |
| 780    | No file              | `5bfba18001de`  |
| 771    | No file              | `5bfba18001de`  |
| 760    | No file              | `5bfba18001de`  |
| 748    | No file              | `5bfba18001de`  |
| 741    | No file              | `5bfba18001de`  |
| 736    | No file              | `5bfba18001de`  |
| 731    | No file              | `5bfba18001de`  |
| 723    | No file              | `5bfba18001de`  |
| 711    | No file              | `5bfba18001de`  |
| 707    | No file              | `5bfba18001de`  |
| 697    | No file              | `5bfba18001de`  |
| 689    | No file              | `5bfba18001de`  |
| 683    | No file              | `5bfba18001de`  |
| 678    | No file              | `5bfba18001de`  |
| 670    | No file              | `5bfba18001de`  |
| 661    | No file              | `5bfba18001de`  |
| 656    | No file              | `5bfba18001de`  |
| 652    | No file              | `5bfba18001de`  |
| 643    | No file              | `5bfba18001de`  |
| 637    | No file              | `5bfba18001de`  |
| 630    | No file              | `5bfba18001de`  |
| 627    | No file              | `5bfba18001de`  |
| 621    | No file              | `5bfba18001de`  |
| 617    | No file              | `5bfba18001de`  |
| 615    | No file              | `5bfba18001de`  |
| 606    | No file              | `5bfba18001de`  |
| 599    | No file              | `5bfba18001de`  |
| 592    | No file              | `5bfba18001de`  |
| 586    | No file              | `5bfba18001de`  |
| 577    | No file              | `5bfba18001de`  |
| 569    | No file              | `5bfba18001de`  |
| 561    | No file              | `5bfba18001de`  |
| 554    | No file              | `5bfba18001de`  |
| 542    | No file              | `5bfba18001de`  |
| 532    | No file              | `5bfba18001de`  |
| 531    | No file              | `5bfba18001de`  |
| 526    | No file              | `5bfba18001de`  |
| 521    | No file              | `5bfba18001de`  |
| 517    | No file              | `5bfba18001de`  |
| 510    | No file              | `5bfba18001de`  |
| 508    | No file              | `5bfba18001de`  |
| 504    | No file              | `5bfba18001de`  |
| 497    | No file              | `5bfba18001de`  |
| 491    | No file              | `5bfba18001de`  |
| 485    | No file              | `5bfba18001de`  |
| 478    | No file              | `5bfba18001de`  |
| 472    | No file              | `5bfba18001de`  |
| 466    | No file              | `5bfba18001de`  |
| 457    | No file              | `5bfba18001de`  |
| 452    | No file              | `5bfba18001de`  |
| 449    | No file              | `5bfba18001de`  |
| 435    | No file              | `5bfba18001de`  |

<!-- versions:end -->

## Companion Files

None. Names and titles in the user's language come from LOC type `6` (see Purpose).

All multi-byte values are little-endian.

## Layout 2

### File Layout

PABR block: a fixed-width row table, then the counted string table the rows index into, then the 8-byte trailer.

| Offset              | Type          | Field        | Notes |
| ------------------- | ------------- | ------------ | ----- |
| `+0x00`             | char[4]       | magic        | ASCII `PABR` |
| `+0x04`             | u32           | count        | Number of rows; `24553` on client 3474 |
| `+0x08`             | Row[count]    | rows         | See Row |
| `rows+0x00`         | String Table  | string_table | See String Table |
| `string_table+0x00` | u32           | table_start  | Equals `0x08 + count * 119`, where the rows end |
| `string_table+0x04` | u32           | zero         | Always `0` |

### Row (119 bytes)

Counts on client 3474. A field named as in `characterstatic.dbss` holds that file's value for the same character on every row.

| Offset  | Type     | Field                     | Notes |
| ------- | -------- | ------------------------- | ----- |
| `+0x00` | u16      | character_id              | Same key as `characterstatic.dbss`; both files hold the same 24,553 IDs |
| `+0x02` | u8       | is_giant                  | `2` on 992 rows, `1` on 421 |
| `+0x03` | i16      | spawn_start_hour          | `-1` on 24,478 rows |
| `+0x05` | i16      | spawn_end_hour            | `-1` on 24,478 rows |
| `+0x07` | u8       | is_fixed                  | `1` on 4,534 rows |
| `+0x08` | u16      | collect_drop_id           | Non-zero on 886 rows |
| `+0x0A` | u8       | unknown_0a                | `1` on 45 rows, all `npc_kind` `7` (node forts, Field HQ, Command Post); see Open Questions |
| `+0x0B` | u8       | unknown_0b                | `1` on 193 rows, all `npc_kind` `9` (fences, barricades, siege installations); see Open Questions |
| `+0x0C` | u8       | is_client_ai              | `1` on 3,582 rows |
| `+0x0D` | u32      | model_path_ref            | String-table index of `model_path`, the action-chart path |
| `+0x11` | u32      | model_path_hash           | Hash of `model_path` |
| `+0x15` | u8       | npc_kind                  | `gc::CharacterKind`; see [`npc_kind` Values](../dbss/characterstatic_dbss.md#npc_kind-values) |
| `+0x16` | u8       | class_type                | `101` on every row that is not a player character |
| `+0x17` | f32      | body_height               | |
| `+0x1B` | f32      | body_size                 | |
| `+0x1F` | f32      | max_hp                    | `10000.0` on Ehren (`47791`) |
| `+0x23` | u64      | attribute_type_mask       | Bit `n` set for each `AttributeType` value `n` |
| `+0x2B` | u8       | unknown_2b                | `1` on 4,860 rows: all 3,296 of `npc_kind` `3`, 902 of `2`, 563 of `4`; see Open Questions |
| `+0x2C` | u8       | unknown_2c                | `1` on 5,725 rows; `characterstatic.dbss` `unknown_b5`; see Open Questions |
| `+0x2D` | u8       | is_tamable                | `1` on 11 rows |
| `+0x2E` | u8       | is_opti_monster           | `1` on 54 rows, `2` on 13 |
| `+0x2F` | bytes[3] | unknown_2f                | Always `0` |
| `+0x32` | u8       | is_render_shadow          | `1` on 22,103 rows |
| `+0x33` | u8       | use_default_audio         | `1` on 12,462 rows |
| `+0x34` | u32      | voice_bank_ref            | String-table index of `voice_bank` (`NPC_VCE_47343`); the empty string on 14,408 rows |
| `+0x38` | u8       | unknown_38                | `1` on 87 rows: 66 of `npc_kind` `3`, 19 of `2`, 2 of `1`; see Open Questions |
| `+0x39` | u8       | is_carrier                | `1` on 368 rows |
| `+0x3A` | u8       | vehicle_type              | `CppEnums.VehicleType`; `65` when the character is not a vehicle |
| `+0x3B` | i16      | team_no                   | `-1` on 567 rows, `1` to `7` on 306 |
| `+0x3D` | u8       | unknown_3d                | `1` on 59 rows; `characterstatic.dbss` `unknown_a1` |
| `+0x3E` | u8       | is_hidden_name            | `1` on 10,373 rows |
| `+0x3F` | i32      | is_live_collect           | `-1` on 4 rows, `1` on 3, else `0`; see [Field Names](#field-names) |
| `+0x43` | u8       | unknown_43                | Always `1` |
| `+0x44` | u32      | name_kr_ref               | String-table index of `name_kr`, the Korean name |
| `+0x48` | u32      | title_kr_ref              | String-table index of `title_kr`, the Korean title; the empty string on 18,311 rows |
| `+0x4C` | u8       | unknown_4c                | `1` on 399 rows; see Open Questions |
| `+0x4D` | u8       | grade                     | `CppEnums.CharacterGradeType` |
| `+0x4E` | u8       | is_hidden_hp              | `1` on 4,054 rows |
| `+0x4F` | u32      | level                     | `1` on 9,628 rows, `99` on 5,531 |
| `+0x53` | i16      | character_group           | Non-zero on 2,450 rows |
| `+0x55` | u32      | fusion_group_key          | `1` on `530` (Aal's Breath) only; see [Field Names](#field-names) |
| `+0x59` | u8       | unknown_59                | `1` on 133 rows; `characterstatic.dbss` `unknown_b7` |
| `+0x5A` | u8       | unknown_5a                | `2` on 24,419 rows, `0` on 132, `1` on 2; `characterstatic.dbss` `unknown_b2` |
| `+0x5B` | u8       | unknown_5b                | `1` on 77 rows; `characterstatic.dbss` `unknown_a2` |
| `+0x5C` | u8       | unknown_5c                | Always `0x15`, as `characterstatic.dbss` `unknown_08` |
| `+0x5D` | u32      | action_script_ref         | String-table index of `action_script`; `getknowledge(<id>);` on most of the 5,687 non-empty rows |
| `+0x61` | u16      | steal_drop_id             | Non-zero on 526 rows |
| `+0x63` | u16      | unknown_63                | Always `0` |
| `+0x65` | u8       | inventory_max             | Non-zero on 507 rows |
| `+0x66` | u8       | absolute_interaction      | `1` on 692 rows |
| `+0x67` | u8       | is_attacked_pvp_mode_only | `1` on 1,290 rows |
| `+0x68` | u8       | vehicle_driver_ridable    | `1` on 3,303 rows |
| `+0x69` | u8       | vehicle_seat_count        | `1` on 3,034 rows, up to `15` |
| `+0x6A` | u32      | condition_script_ref      | String-table index of `condition_script`, the interaction condition; non-empty on 402 rows |
| `+0x6E` | u8       | vehicle_sub_type          | Non-zero on 100 rows (`1` to `4`) |
| `+0x6F` | u8       | is_guild_vehicle          | `1` on 85 rows |
| `+0x70` | u8       | unknown_70                | `10` on 24,112 rows; `characterstatic.dbss` `unknown_c2` |
| `+0x71` | u8       | carriage_type             | Non-zero on 30 rows (`1` to `5`); a u32 in `characterstatic.dbss` |
| `+0x72` | bytes[4] | unknown_72                | Always `0` |
| `+0x76` | u8       | unknown_76                | `1` on 2,418 rows; `characterstatic.dbss` `unknown_contents_group_hashes_17` |

The six `*_ref` fields index the string table from `0`. The parser stores each string under the field name without `_ref` (`model_path`, `voice_bank`, `name_kr`, `title_kr`, `action_script`, `condition_script`).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `31277` on client 3474 |
| `+0x04` | pstr[string_count] | strings      | Counted entries, indexed from `0` |

The entry layout is the one [npcsimply.bss](npcsimply_bss.md) uses: a u8 `is_wide` (`1` for UTF-16LE, `0` for UTF-8), a u32 byte length and the text, with no terminator. On client 3474, 17,566 entries are UTF-16LE (the scripts and the Korean texts) and 13,711 UTF-8 (model paths and voice banks). Index `1` is the empty string. The last entry ends at the trailer.

## Layout 1

The client 1784 file (15,704 rows of 121 bytes). It has 4 more bytes after `model_path_hash` and a zero byte after `absolute_interaction`, and lacks `unknown_63` and `unknown_76`. Only Row differs from Layout 2. The parser reads only Layout 2.

### Row (121 bytes)

| Offset  | Type     | Field                                | Notes |
| ------- | -------- | ------------------------------------ | ----- |
| `+0x00` | u16      | character_id                         | |
| `+0x02` | u8       | is_giant                             | |
| `+0x03` | i16      | spawn_start_hour                     | |
| `+0x05` | i16      | spawn_end_hour                       | |
| `+0x07` | u8       | is_fixed                             | |
| `+0x08` | u16      | collect_drop_id                      | |
| `+0x0A` | u8       | unknown_0a                           | |
| `+0x0B` | u8       | unknown_0b                           | |
| `+0x0C` | u8       | is_client_ai                         | |
| `+0x0D` | u32      | model_path_ref                       | |
| `+0x11` | u32      | model_path_hash                      | |
| `+0x15` | u32      | unknown_after_model_path_hash        | Non-zero on 96 rows; 28 of them hold `3171023435` |
| `+0x19` | u8       | npc_kind                             | |
| `+0x1A` | u8       | class_type                           | |
| `+0x1B` | f32      | body_height                          | |
| `+0x1F` | f32      | body_size                            | |
| `+0x23` | f32      | max_hp                               | |
| `+0x27` | u64      | attribute_type_mask                  | |
| `+0x2F` | u8       | unknown_2b                           | |
| `+0x30` | u8       | unknown_2c                           | |
| `+0x31` | u8       | is_tamable                           | |
| `+0x32` | u8       | is_opti_monster                      | |
| `+0x33` | bytes[3] | unknown_2f                           | |
| `+0x36` | u8       | is_render_shadow                     | |
| `+0x37` | u8       | use_default_audio                    | |
| `+0x38` | u32      | voice_bank_ref                       | |
| `+0x3C` | u8       | unknown_38                           | |
| `+0x3D` | u8       | is_carrier                           | |
| `+0x3E` | u8       | vehicle_type                         | |
| `+0x3F` | i16      | team_no                              | |
| `+0x41` | u8       | unknown_3d                           | |
| `+0x42` | u8       | is_hidden_name                       | |
| `+0x43` | i32      | is_live_collect                      | |
| `+0x47` | u8       | unknown_43                           | |
| `+0x48` | u32      | name_kr_ref                          | |
| `+0x4C` | u32      | title_kr_ref                         | |
| `+0x50` | u8       | unknown_4c                           | |
| `+0x51` | u8       | grade                                | |
| `+0x52` | u8       | is_hidden_hp                         | |
| `+0x53` | u32      | level                                | |
| `+0x57` | i16      | character_group                      | |
| `+0x59` | u32      | fusion_group_key                     | |
| `+0x5D` | u8       | unknown_59                           | |
| `+0x5E` | u8       | unknown_5a                           | |
| `+0x5F` | u8       | unknown_5b                           | |
| `+0x60` | u8       | unknown_5c                           | |
| `+0x61` | u32      | action_script_ref                    | |
| `+0x65` | u16      | steal_drop_id                        | |
| `+0x67` | u8       | inventory_max                        | |
| `+0x68` | u8       | absolute_interaction                 | |
| `+0x69` | u8       | unknown_after_absolute_interaction   | Always `0` |
| `+0x6A` | u8       | is_attacked_pvp_mode_only            | |
| `+0x6B` | u8       | vehicle_driver_ridable               | |
| `+0x6C` | u8       | vehicle_seat_count                   | |
| `+0x6D` | u32      | condition_script_ref                 | |
| `+0x71` | u8       | vehicle_sub_type                     | |
| `+0x72` | u8       | is_guild_vehicle                     | |
| `+0x73` | u8       | unknown_70                           | |
| `+0x74` | u8       | carriage_type                        | |
| `+0x75` | bytes[4] | unknown_72                           | Always `0` |

## Field Names

Every named field except `is_live_collect` and `fusion_group_key` carries the name of the [characterstatic.dbss](../dbss/characterstatic_dbss.md) field it equals, and each `*_ref` the name of the string it points at: on client 3474 all 24,553 rows hold the same value as that file's field for the same character, the six strings included. `characterstatic.dbss` takes those names from the `Character_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (see its [Field Names](../dbss/characterstatic_dbss.md#field-names)).

The other two match a `Character_Table` column by value on every row that shares a key with the sheet:

| Field | `Character_Table` column | Rows that agree, client 1784 | Rows that agree, client 3474 |
| ----- | ------------------------ | ---------------------------- | ---------------------------- |
| `is_live_collect` | `IsLiveCollect` | 15,704 of 15,704 | 16,058 of 16,058 |
| `fusion_group_key` | `FusionGroupKey` | 15,704 of 15,704 | 16,058 of 16,058 |

Both fields sit where `characterstatic.dbss` has `is_live_collect` and `unknown_1b`, and hold the same values. `fusion_group_key` is non-zero on one row in both clients (`1` on character `530`, Aal's Breath), so its match rests on that row and the zeros.

## Notes

- `characterstatic.dbss` gained `unknown_contents_group_hashes_17` in client 3464, and `unknown_76` holds the same value here. The client 1784 row has no such byte.
- The row stores the fields in another order than `characterstatic.dbss`: `team_no`, `carriage_type`, `steal_drop_id` and `attribute_type_mask` sit after the strings there and in the fixed row here.
- [Attribute Types](../dbss/characterstatic_dbss.md#attribute-types) and [`npc_kind` Values](../dbss/characterstatic_dbss.md#npc_kind-values) in the `characterstatic.dbss` doc apply to this file unchanged.

## Open Questions

### What do `unknown_0a` and `unknown_0b` mark?

`unknown_0a` is `1` on 45 rows, all `npc_kind` `7`: the node forts, the Field HQ (`12821`) and the Command Post (`12820`). On every row that shares a key with the private server's `Character_Table` it is `1` exactly where `MoraleValue` is non-zero (`500000`): 19 of 16,058 rows on client 3474, 21 of 15,704 on client 1784. It looks like a "has morale" flag for siege structures, but the sheet column holds the amount, not a flag, so the field stays `unknown_0a`. `unknown_0b` is `1` on 193 rows, all `npc_kind` `9` (`12842` Flimsy Wooden Fence, `12841` Flimsy Barricade, `12839` Indomitable Flag Factory), and matches no sheet column.

Checked on client 3474, without a name for either byte:

| Source | Result |
| ------ | ------ |
| `characterstatic.dbss` | No byte is non-zero on exactly the same rows. The closest is `repair_resources`: `3` on 42 of the 45 `unknown_0a` rows, but also on 23 rows without it |
| `Character_Table` of a private server on client 519 | `unknown_0a` agrees with `MoraleValue` non-zero on all 12,008 shared rows (9 flagged). `unknown_0b` matches none of its 171 columns |
| 2016 `gc::CharacterStaticStatus` | No morale member. Its `gc::ObjectStaticStatus` holds two adjacent bools, `_isSiegeTent` and `_isSiegeOrFortressTent`, but `unknown_0b` sits on fences and barricades, which are not tents |
| Client Lua | `isBarricade()`, `isSiegeTower()` and the other siege checks are called on `getObjectStaticStatus()`, the installation type, not on a character flag; no Lua reads a morale value from the character |

The client 1784 server binary has a `CharacterSimplyStaticStatusManager` (`link` and `relinkAndCheckValid` error strings); the code that fills it would name both bytes.

### What is `unknown_2c`?

It equals `characterstatic.dbss` `unknown_b5` on every row. On client 1784 it is `1` exactly where `Character_Table` `TalkAble` is non-zero (`1`, `2` or `3`) on all 15,704 rows; on client 3474 the same holds on 16,051 of 16,058 rows. The column holds a talk type rather than a flag, so the field stays unknown until the client is shown to read it as "can talk".

### What do `unknown_2b`, `unknown_38` and `unknown_4c` hold?

None of them has a counterpart in `characterstatic.dbss` or a matching `Character_Table` column. `unknown_2b` is set on every `npc_kind` `3` row and on 1,564 others; its best sheet match, `IsClientAI`, agrees on only 15,085 of 16,058 rows. `unknown_38` is set on 87 rows, among them `37065` Ancient Teleporter and `35636` Galley under Construction. `unknown_4c` is `1` exactly where `condition_script` is non-empty, except on three rows (`23751` Mirumok Watcher Offin, `23767`, `23810`) whose condition is `getitemcount(40414,0)>0;`; on client 1784 it agrees with a non-empty `InteractionCondition` on all 15,704 rows.
