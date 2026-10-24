# `olviaacademycurriculumss.bss` Format

## Purpose

The curricula and family rewards of the Olvia Academy main window
(`panel_window_olviaacademy_main_all*.luac`). A curriculum (Combat, Life
Skill) holds subjects; a subject holds its quest list, its start quest, its
texts and, for the Life Skill subjects, a preview page. A family reward
(Combat, Life Skill) holds reward groups of quests. Every title, description
and preview text is a key of the `RESOURCE` string sheet, every quest a
packed quest ID `(quest_id << 16) | quest_chain_id`. The file has no PABR
magic and no string table. The quests are those of
[`olviaacademycurriculumquestlist.bss` and `olviaacademyrewardquestlist.bss`](olviaacademyquestlist_bss.md);
the pass tabs are in
[`olviaacademypassstaticstatusmanager.bss`](olviaacademypassstaticstatusmanager_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records                                                                           | Row bytes               |
| ------ | -------------- | ------- | ------------------------------ | ------ | --------------------------------------------------------------------------------- | ----------------------- |
| 1      | 3186 and later | 3483    | `olviaacademycurriculumss.bss` | 17,166 | 142 Subject Quest, 11 Subject, 2 Curriculum, 9 Preview, 10 Reward Group, 2 Reward | 46 to 49, 47 on average |

| Layout | File                           | Known             | Unknown    |
| ------ | ------------------------------ | ----------------- | ---------- |
| 1      | `olviaacademycurriculumss.bss` | 17,166 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `ab33504368b8`  |
| 3482   | Layout 1 | `ab33504368b8`  |
| 3474   | Layout 1 | `ab33504368b8`  |
| 3473   | Layout 1 | `ab33504368b8`  |
| 3464   | Layout 1 | `ab33504368b8`  |
| 3458   | Layout 1 | `ab33504368b8`  |
| 3454   | Layout 1 | `ab33504368b8`  |
| 3444   | Layout 1 | `ab33504368b8`  |
| 3435   | Layout 1 | `ab33504368b8`  |
| 3426   | Layout 1 | `ab33504368b8`  |
| 3418   | Layout 1 | `ab33504368b8`  |
| 3412   | Layout 1 | `ab33504368b8`  |
| 3402   | Layout 1 | `ab33504368b8`  |
| 3396   | Layout 1 | `ab33504368b8`  |
| 3387   | Layout 1 | `ab33504368b8`  |
| 3381   | Layout 1 | `ab33504368b8`  |
| 3373   | Layout 1 | `ab33504368b8`  |
| 3364   | Layout 1 | `ab33504368b8`  |
| 3356   | Layout 1 | `ab33504368b8`  |
| 3349   | Layout 1 | `ab33504368b8`  |
| 3342   | Layout 1 | `ab33504368b8`  |
| 3335   | Layout 1 | `ab33504368b8`  |
| 3326   | Layout 1 | `ab33504368b8`  |
| 3321   | Layout 1 | `ab33504368b8`  |
| 3314   | Layout 1 | `ab33504368b8`  |
| 3303   | Layout 1 | `ab33504368b8`  |
| 3302   | Layout 1 | `ab33504368b8`  |
| 3293   | Layout 1 | `ab33504368b8`  |
| 3283   | Layout 1 | `ab33504368b8`  |
| 3275   | Layout 1 | `ab33504368b8`  |
| 3267   | Layout 1 | `ab33504368b8`  |
| 3258   | Layout 1 | `ab33504368b8`  |
| 3251   | Layout 1 | `ab33504368b8`  |
| 3242   | Layout 1 | `ab33504368b8`  |
| 3235   | Layout 1 | `ab33504368b8`  |
| 3229   | Layout 1 | `ab33504368b8`  |
| 3212   | Layout 1 | `ab33504368b8`  |
| 3203   | Layout 1 | `ab33504368b8`  |
| 3193   | Layout 1 | `ab33504368b8`  |
| 3186   | Layout 1 | `ab33504368b8`  |
| 3177   | No file  | `ab33504368b8`  |
| 3169   | No file  | `ab33504368b8`  |
| 3158   | No file  | `ab33504368b8`  |
| 3151   | No file  | `ab33504368b8`  |
| 3144   | No file  | `ab33504368b8`  |
| 3133   | No file  | `ab33504368b8`  |
| 3125   | No file  | `ab33504368b8`  |
| 3118   | No file  | `ab33504368b8`  |
| 3111   | No file  | `ab33504368b8`  |
| 3103   | No file  | `ab33504368b8`  |
| 3095   | No file  | `ab33504368b8`  |
| 3086   | No file  | `ab33504368b8`  |
| 3072   | No file  | `ab33504368b8`  |
| 3062   | No file  | `ab33504368b8`  |
| 3052   | No file  | `ab33504368b8`  |
| 3045   | No file  | `ab33504368b8`  |
| 3037   | No file  | `ab33504368b8`  |
| 3030   | No file  | `ab33504368b8`  |
| 3021   | No file  | `ab33504368b8`  |
| 3012   | No file  | `ab33504368b8`  |
| 3002   | No file  | `ab33504368b8`  |
| 2995   | No file  | `ab33504368b8`  |
| 2987   | No file  | `ab33504368b8`  |
| 2978   | No file  | `ab33504368b8`  |
| 2970   | No file  | `ab33504368b8`  |
| 2959   | No file  | `ab33504368b8`  |
| 2951   | No file  | `ab33504368b8`  |
| 2942   | No file  | `ab33504368b8`  |
| 2935   | No file  | `ab33504368b8`  |
| 2932   | No file  | `ab33504368b8`  |
| 2923   | No file  | `ab33504368b8`  |
| 2919   | No file  | `ab33504368b8`  |
| 2907   | No file  | `ab33504368b8`  |
| 2900   | No file  | `ab33504368b8`  |
| 2891   | No file  | `ab33504368b8`  |
| 2882   | No file  | `ab33504368b8`  |
| 2872   | No file  | `ab33504368b8`  |
| 2863   | No file  | `ab33504368b8`  |
| 2855   | No file  | `ab33504368b8`  |
| 2849   | No file  | `ab33504368b8`  |
| 2844   | No file  | `ab33504368b8`  |
| 2834   | No file  | `ab33504368b8`  |
| 2825   | No file  | `ab33504368b8`  |
| 2819   | No file  | `ab33504368b8`  |
| 2811   | No file  | `ab33504368b8`  |
| 2803   | No file  | `ab33504368b8`  |
| 2794   | No file  | `ab33504368b8`  |
| 2783   | No file  | `ab33504368b8`  |
| 2774   | No file  | `ab33504368b8`  |
| 2765   | No file  | `ab33504368b8`  |
| 2756   | No file  | `ab33504368b8`  |
| 2750   | No file  | `ab33504368b8`  |
| 2743   | No file  | `ab33504368b8`  |
| 2736   | No file  | `ab33504368b8`  |
| 2726   | No file  | `ab33504368b8`  |
| 2717   | No file  | `ab33504368b8`  |
| 2709   | No file  | `ab33504368b8`  |
| 2703   | No file  | `ab33504368b8`  |
| 2695   | No file  | `ab33504368b8`  |
| 2684   | No file  | `ab33504368b8`  |
| 2672   | No file  | `ab33504368b8`  |
| 2665   | No file  | `ab33504368b8`  |
| 2657   | No file  | `ab33504368b8`  |
| 2649   | No file  | `ab33504368b8`  |
| 2644   | No file  | `ab33504368b8`  |
| 2637   | No file  | `ab33504368b8`  |
| 2629   | No file  | `ab33504368b8`  |
| 2619   | No file  | `ab33504368b8`  |
| 2612   | No file  | `ab33504368b8`  |
| 2606   | No file  | `ab33504368b8`  |
| 2602   | No file  | `ab33504368b8`  |
| 2601   | No file  | `ab33504368b8`  |
| 2592   | No file  | `ab33504368b8`  |
| 2583   | No file  | `ab33504368b8`  |
| 2575   | No file  | `ab33504368b8`  |
| 2567   | No file  | `ab33504368b8`  |
| 2560   | No file  | `ab33504368b8`  |
| 2553   | No file  | `ab33504368b8`  |
| 2545   | No file  | `ab33504368b8`  |
| 2538   | No file  | `ab33504368b8`  |
| 2529   | No file  | `ab33504368b8`  |
| 2519   | No file  | `ab33504368b8`  |
| 2513   | No file  | `ab33504368b8`  |
| 2510   | No file  | `ab33504368b8`  |
| 2507   | No file  | `ab33504368b8`  |
| 2503   | No file  | `ab33504368b8`  |
| 2498   | No file  | `ab33504368b8`  |
| 2492   | No file  | `ab33504368b8`  |
| 2487   | No file  | `ab33504368b8`  |
| 2480   | No file  | `ab33504368b8`  |
| 2474   | No file  | `ab33504368b8`  |
| 2468   | No file  | `ab33504368b8`  |
| 2460   | No file  | `ab33504368b8`  |
| 2453   | No file  | `ab33504368b8`  |
| 2444   | No file  | `ab33504368b8`  |
| 2438   | No file  | `ab33504368b8`  |
| 2434   | No file  | `ab33504368b8`  |
| 2429   | No file  | `ab33504368b8`  |
| 2421   | No file  | `ab33504368b8`  |
| 2414   | No file  | `ab33504368b8`  |
| 2407   | No file  | `ab33504368b8`  |
| 2401   | No file  | `ab33504368b8`  |
| 2397   | No file  | `ab33504368b8`  |
| 2393   | No file  | `ab33504368b8`  |
| 2384   | No file  | `ab33504368b8`  |
| 2378   | No file  | `ab33504368b8`  |
| 2372   | No file  | `ab33504368b8`  |
| 2358   | No file  | `ab33504368b8`  |
| 2352   | No file  | `ab33504368b8`  |
| 2347   | No file  | `ab33504368b8`  |
| 2343   | No file  | `ab33504368b8`  |
| 2335   | No file  | `ab33504368b8`  |
| 2327   | No file  | `ab33504368b8`  |
| 2324   | No file  | `ab33504368b8`  |
| 2319   | No file  | `ab33504368b8`  |
| 2313   | No file  | `ab33504368b8`  |
| 2308   | No file  | `ab33504368b8`  |
| 2302   | No file  | `ab33504368b8`  |
| 2295   | No file  | `ab33504368b8`  |
| 2290   | No file  | `ab33504368b8`  |
| 2284   | No file  | `ab33504368b8`  |
| 2276   | No file  | `ab33504368b8`  |
| 2269   | No file  | `ab33504368b8`  |
| 2259   | No file  | `ab33504368b8`  |
| 2250   | No file  | `ab33504368b8`  |
| 2243   | No file  | `ab33504368b8`  |
| 2235   | No file  | `ab33504368b8`  |
| 2229   | No file  | `ab33504368b8`  |
| 2224   | No file  | `ab33504368b8`  |
| 2218   | No file  | `ab33504368b8`  |
| 2215   | No file  | `ab33504368b8`  |
| 2207   | No file  | `ab33504368b8`  |
| 2203   | No file  | `ab33504368b8`  |
| 2196   | No file  | `ab33504368b8`  |
| 2192   | No file  | `ab33504368b8`  |
| 2189   | No file  | `ab33504368b8`  |
| 2183   | No file  | `ab33504368b8`  |
| 2179   | No file  | `ab33504368b8`  |
| 2171   | No file  | `ab33504368b8`  |
| 2163   | No file  | `ab33504368b8`  |
| 2156   | No file  | `ab33504368b8`  |
| 2151   | No file  | `ab33504368b8`  |
| 2147   | No file  | `ab33504368b8`  |
| 2142   | No file  | `ab33504368b8`  |
| 2138   | No file  | `ab33504368b8`  |
| 2134   | No file  | `ab33504368b8`  |
| 2130   | No file  | `ab33504368b8`  |
| 2122   | No file  | `ab33504368b8`  |
| 2107   | No file  | `ab33504368b8`  |
| 2098   | No file  | `ab33504368b8`  |
| 2089   | No file  | `ab33504368b8`  |
| 2081   | No file  | `ab33504368b8`  |
| 2073   | No file  | `ab33504368b8`  |
| 2067   | No file  | `ab33504368b8`  |
| 2063   | No file  | `ab33504368b8`  |
| 2059   | No file  | `ab33504368b8`  |
| 2052   | No file  | `ab33504368b8`  |
| 2044   | No file  | `ab33504368b8`  |
| 2039   | No file  | `ab33504368b8`  |
| 2032   | No file  | `ab33504368b8`  |
| 2025   | No file  | `ab33504368b8`  |
| 2011   | No file  | `ab33504368b8`  |
| 2005   | No file  | `ab33504368b8`  |
| 2000   | No file  | `ab33504368b8`  |
| 1996   | No file  | `ab33504368b8`  |
| 1991   | No file  | `ab33504368b8`  |
| 1985   | No file  | `ab33504368b8`  |
| 1980   | No file  | `ab33504368b8`  |
| 1969   | No file  | `ab33504368b8`  |
| 1964   | No file  | `ab33504368b8`  |
| 1958   | No file  | `ab33504368b8`  |
| 1950   | No file  | `ab33504368b8`  |
| 1945   | No file  | `ab33504368b8`  |
| 1937   | No file  | `ab33504368b8`  |
| 1933   | No file  | `ab33504368b8`  |
| 1927   | No file  | `ab33504368b8`  |
| 1921   | No file  | `ab33504368b8`  |
| 1914   | No file  | `ab33504368b8`  |
| 1908   | No file  | `ab33504368b8`  |
| 1897   | No file  | `ab33504368b8`  |
| 1892   | No file  | `ab33504368b8`  |
| 1886   | No file  | `ab33504368b8`  |
| 1881   | No file  | `ab33504368b8`  |
| 1871   | No file  | `ab33504368b8`  |
| 1866   | No file  | `ab33504368b8`  |
| 1862   | No file  | `ab33504368b8`  |
| 1854   | No file  | `ab33504368b8`  |
| 1846   | No file  | `ab33504368b8`  |
| 1838   | No file  | `ab33504368b8`  |
| 1832   | No file  | `ab33504368b8`  |
| 1826   | No file  | `ab33504368b8`  |
| 1822   | No file  | `ab33504368b8`  |
| 1818   | No file  | `ab33504368b8`  |
| 1804   | No file  | `ab33504368b8`  |
| 1794   | No file  | `ab33504368b8`  |
| 1790   | No file  | `ab33504368b8`  |
| 1784   | No file  | `ab33504368b8`  |
| 1774   | No file  | `ab33504368b8`  |
| 1771   | No file  | `ab33504368b8`  |
| 1762   | No file  | `ab33504368b8`  |
| 1759   | No file  | `ab33504368b8`  |
| 1754   | No file  | `ab33504368b8`  |
| 1749   | No file  | `ab33504368b8`  |
| 1743   | No file  | `ab33504368b8`  |
| 1737   | No file  | `ab33504368b8`  |
| 1731   | No file  | `ab33504368b8`  |
| 1725   | No file  | `ab33504368b8`  |
| 1717   | No file  | `ab33504368b8`  |
| 1710   | No file  | `ab33504368b8`  |
| 1704   | No file  | `ab33504368b8`  |
| 1698   | No file  | `ab33504368b8`  |
| 1690   | No file  | `ab33504368b8`  |
| 1685   | No file  | `ab33504368b8`  |
| 1680   | No file  | `ab33504368b8`  |
| 1674   | No file  | `ab33504368b8`  |
| 1668   | No file  | `ab33504368b8`  |
| 1659   | No file  | `ab33504368b8`  |
| 1649   | No file  | `ab33504368b8`  |
| 1642   | No file  | `ab33504368b8`  |
| 1636   | No file  | `ab33504368b8`  |
| 1628   | No file  | `ab33504368b8`  |
| 1622   | No file  | `ab33504368b8`  |
| 1614   | No file  | `ab33504368b8`  |
| 1608   | No file  | `ab33504368b8`  |
| 1602   | No file  | `ab33504368b8`  |
| 1598   | No file  | `ab33504368b8`  |
| 1594   | No file  | `ab33504368b8`  |
| 1590   | No file  | `ab33504368b8`  |
| 1587   | No file  | `ab33504368b8`  |
| 1584   | No file  | `ab33504368b8`  |
| 1579   | No file  | `ab33504368b8`  |
| 1572   | No file  | `ab33504368b8`  |
| 1565   | No file  | `ab33504368b8`  |
| 1559   | No file  | `ab33504368b8`  |
| 1554   | No file  | `ab33504368b8`  |
| 1547   | No file  | `ab33504368b8`  |
| 1537   | No file  | `ab33504368b8`  |
| 1529   | No file  | `ab33504368b8`  |
| 1524   | No file  | `ab33504368b8`  |
| 1519   | No file  | `ab33504368b8`  |
| 1509   | No file  | `ab33504368b8`  |
| 1506   | No file  | `ab33504368b8`  |
| 1504   | No file  | `ab33504368b8`  |
| 1500   | No file  | `ab33504368b8`  |
| 1493   | No file  | `ab33504368b8`  |
| 1489   | No file  | `ab33504368b8`  |
| 1485   | No file  | `ab33504368b8`  |
| 1481   | No file  | `ab33504368b8`  |
| 1474   | No file  | `ab33504368b8`  |
| 1466   | No file  | `ab33504368b8`  |
| 1462   | No file  | `ab33504368b8`  |
| 1459   | No file  | `ab33504368b8`  |
| 1453   | No file  | `ab33504368b8`  |
| 1450   | No file  | `ab33504368b8`  |
| 1445   | No file  | `ab33504368b8`  |
| 1439   | No file  | `ab33504368b8`  |
| 1433   | No file  | `ab33504368b8`  |
| 1430   | No file  | `ab33504368b8`  |
| 1426   | No file  | `ab33504368b8`  |
| 1421   | No file  | `ab33504368b8`  |
| 1417   | No file  | `ab33504368b8`  |
| 1416   | No file  | `ab33504368b8`  |
| 1409   | No file  | `ab33504368b8`  |
| 1405   | No file  | `ab33504368b8`  |
| 1401   | No file  | `ab33504368b8`  |
| 1396   | No file  | `ab33504368b8`  |
| 1391   | No file  | `ab33504368b8`  |
| 1390   | No file  | `ab33504368b8`  |
| 1386   | No file  | `ab33504368b8`  |
| 1381   | No file  | `ab33504368b8`  |
| 1379   | No file  | `ab33504368b8`  |
| 1372   | No file  | `ab33504368b8`  |
| 1366   | No file  | `ab33504368b8`  |
| 1364   | No file  | `ab33504368b8`  |
| 1363   | No file  | `ab33504368b8`  |
| 1360   | No file  | `ab33504368b8`  |
| 1358   | No file  | `ab33504368b8`  |
| 1355   | No file  | `ab33504368b8`  |
| 1351   | No file  | `ab33504368b8`  |
| 1348   | No file  | `ab33504368b8`  |
| 1346   | No file  | `ab33504368b8`  |
| 1341   | No file  | `ab33504368b8`  |
| 1340   | No file  | `ab33504368b8`  |
| 1338   | No file  | `ab33504368b8`  |
| 1335   | No file  | `ab33504368b8`  |
| 1333   | No file  | `ab33504368b8`  |
| 1329   | No file  | `ab33504368b8`  |
| 1327   | No file  | `ab33504368b8`  |
| 1324   | No file  | `ab33504368b8`  |
| 1321   | No file  | `ab33504368b8`  |
| 1319   | No file  | `ab33504368b8`  |
| 1318   | No file  | `ab33504368b8`  |
| 1316   | No file  | `ab33504368b8`  |
| 1313   | No file  | `ab33504368b8`  |
| 1311   | No file  | `ab33504368b8`  |
| 1309   | No file  | `ab33504368b8`  |
| 1304   | No file  | `ab33504368b8`  |
| 1292   | No file  | `ab33504368b8`  |
| 1286   | No file  | `ab33504368b8`  |
| 1280   | No file  | `ab33504368b8`  |
| 1276   | No file  | `ab33504368b8`  |
| 1267   | No file  | `ab33504368b8`  |
| 1261   | No file  | `ab33504368b8`  |
| 1256   | No file  | `ab33504368b8`  |
| 1250   | No file  | `ab33504368b8`  |
| 1246   | No file  | `ab33504368b8`  |
| 1239   | No file  | `ab33504368b8`  |
| 1230   | No file  | `ab33504368b8`  |
| 1226   | No file  | `ab33504368b8`  |
| 1220   | No file  | `ab33504368b8`  |
| 1217   | No file  | `ab33504368b8`  |
| 1211   | No file  | `ab33504368b8`  |
| 1210   | No file  | `ab33504368b8`  |
| 1208   | No file  | `ab33504368b8`  |
| 1203   | No file  | `ab33504368b8`  |
| 1197   | No file  | `ab33504368b8`  |
| 1194   | No file  | `ab33504368b8`  |
| 1192   | No file  | `ab33504368b8`  |
| 1187   | No file  | `ab33504368b8`  |
| 1183   | No file  | `ab33504368b8`  |
| 1177   | No file  | `ab33504368b8`  |
| 1173   | No file  | `ab33504368b8`  |
| 1167   | No file  | `ab33504368b8`  |
| 1164   | No file  | `ab33504368b8`  |
| 1156   | No file  | `ab33504368b8`  |
| 1149   | No file  | `ab33504368b8`  |
| 1144   | No file  | `ab33504368b8`  |
| 1137   | No file  | `ab33504368b8`  |
| 1132   | No file  | `ab33504368b8`  |
| 1127   | No file  | `ab33504368b8`  |
| 1122   | No file  | `ab33504368b8`  |
| 1118   | No file  | `ab33504368b8`  |
| 1114   | No file  | `ab33504368b8`  |
| 1109   | No file  | `ab33504368b8`  |
| 1102   | No file  | `ab33504368b8`  |
| 1096   | No file  | `ab33504368b8`  |
| 1088   | No file  | `ab33504368b8`  |
| 1081   | No file  | `ab33504368b8`  |
| 1076   | No file  | `ab33504368b8`  |
| 1069   | No file  | `ab33504368b8`  |
| 1064   | No file  | `ab33504368b8`  |
| 1058   | No file  | `ab33504368b8`  |
| 1051   | No file  | `ab33504368b8`  |
| 1044   | No file  | `ab33504368b8`  |
| 1036   | No file  | `ab33504368b8`  |
| 1026   | No file  | `ab33504368b8`  |
| 1016   | No file  | `ab33504368b8`  |
| 1009   | No file  | `ab33504368b8`  |
| 1005   | No file  | `ab33504368b8`  |
| 1000   | No file  | `ab33504368b8`  |
| 998    | No file  | `ab33504368b8`  |
| 990    | No file  | `ab33504368b8`  |
| 979    | No file  | `ab33504368b8`  |
| 972    | No file  | `ab33504368b8`  |
| 963    | No file  | `ab33504368b8`  |
| 955    | No file  | `ab33504368b8`  |
| 946    | No file  | `ab33504368b8`  |
| 938    | No file  | `ab33504368b8`  |
| 927    | No file  | `ab33504368b8`  |
| 911    | No file  | `ab33504368b8`  |
| 904    | No file  | `ab33504368b8`  |
| 899    | No file  | `ab33504368b8`  |
| 894    | No file  | `ab33504368b8`  |
| 885    | No file  | `ab33504368b8`  |
| 879    | No file  | `ab33504368b8`  |
| 872    | No file  | `ab33504368b8`  |
| 864    | No file  | `ab33504368b8`  |
| 855    | No file  | `ab33504368b8`  |
| 853    | No file  | `ab33504368b8`  |
| 845    | No file  | `ab33504368b8`  |
| 837    | No file  | `ab33504368b8`  |
| 829    | No file  | `ab33504368b8`  |
| 822    | No file  | `ab33504368b8`  |
| 814    | No file  | `ab33504368b8`  |
| 805    | No file  | `ab33504368b8`  |
| 794    | No file  | `ab33504368b8`  |
| 787    | No file  | `ab33504368b8`  |
| 780    | No file  | `ab33504368b8`  |
| 771    | No file  | `ab33504368b8`  |
| 760    | No file  | `ab33504368b8`  |
| 748    | No file  | `ab33504368b8`  |
| 741    | No file  | `ab33504368b8`  |
| 736    | No file  | `ab33504368b8`  |
| 731    | No file  | `ab33504368b8`  |
| 723    | No file  | `ab33504368b8`  |
| 711    | No file  | `ab33504368b8`  |
| 707    | No file  | `ab33504368b8`  |
| 697    | No file  | `ab33504368b8`  |
| 689    | No file  | `ab33504368b8`  |
| 683    | No file  | `ab33504368b8`  |
| 678    | No file  | `ab33504368b8`  |
| 670    | No file  | `ab33504368b8`  |
| 661    | No file  | `ab33504368b8`  |
| 656    | No file  | `ab33504368b8`  |
| 652    | No file  | `ab33504368b8`  |
| 643    | No file  | `ab33504368b8`  |
| 637    | No file  | `ab33504368b8`  |
| 630    | No file  | `ab33504368b8`  |
| 627    | No file  | `ab33504368b8`  |
| 621    | No file  | `ab33504368b8`  |
| 617    | No file  | `ab33504368b8`  |
| 615    | No file  | `ab33504368b8`  |
| 606    | No file  | `ab33504368b8`  |
| 599    | No file  | `ab33504368b8`  |
| 592    | No file  | `ab33504368b8`  |
| 586    | No file  | `ab33504368b8`  |
| 577    | No file  | `ab33504368b8`  |
| 569    | No file  | `ab33504368b8`  |
| 561    | No file  | `ab33504368b8`  |
| 554    | No file  | `ab33504368b8`  |
| 542    | No file  | `ab33504368b8`  |
| 532    | No file  | `ab33504368b8`  |
| 531    | No file  | `ab33504368b8`  |
| 526    | No file  | `ab33504368b8`  |
| 521    | No file  | `ab33504368b8`  |
| 517    | No file  | `ab33504368b8`  |
| 510    | No file  | `ab33504368b8`  |
| 508    | No file  | `ab33504368b8`  |
| 504    | No file  | `ab33504368b8`  |
| 497    | No file  | `ab33504368b8`  |
| 491    | No file  | `ab33504368b8`  |
| 485    | No file  | `ab33504368b8`  |
| 478    | No file  | `ab33504368b8`  |
| 472    | No file  | `ab33504368b8`  |
| 466    | No file  | `ab33504368b8`  |
| 457    | No file  | `ab33504368b8`  |
| 452    | No file  | `ab33504368b8`  |
| 449    | No file  | `ab33504368b8`  |
| 435    | No file  | `ab33504368b8`  |

<!-- versions:end -->

## Companion Files

None. The handler names each `RESOURCE` key with its LOC type 37 text (the
key's hash, sheet `str_id2` 2) and each quest with its LOC type 18 title
from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset           | Type                         | Field            | Notes                                     |
| ---------------- | ---------------------------- | ---------------- | ----------------------------------------- |
| `+0x00`          | u32                          | curriculum_count | `ToClient_RequestOlviaAcademyCurriculumCount()` |
| `+0x04`          | Curriculum[curriculum_count] | curricula        | `ToClient_RequestOlviaAcademyCurriculumAt(index)`, index from `0` |
| `curricula+0x00` | u32                          | reward_count     | `ToClient_RequestOlviaAcademyRewardCount()` |
| `curricula+0x04` | Reward[reward_count]         | rewards          | `ToClient_RequestOlviaAcademyRewardAt(index)`, index from `0`; end at the last byte |

### Curriculum (variable: 20 bytes + texts and subjects)

| Offset                  | Type                   | Field            | Notes                                                       |
| ----------------------- | ---------------------- | ---------------- | ----------------------------------------------------------- |
| `+0x00`                 | str16                  | curriculum_title | `RESOURCE` key; `PANEL_OLVIA_ACADEMY_CURRICULM_BATTLE_TITLE` "Combat" |
| `curriculum_title+0x00` | str8                   | curriculum_icon  | Texture ID of the list icon (`Combine_Etc_OlviaSchoolAcademy_01_List_Icon_03_Normal`) |
| `curriculum_icon+0x00`  | u32                    | subject_count    | `getSubjectCount()`                                         |
| `curriculum_icon+0x04`  | Subject[subject_count] | subjects         | `getSubjectAt(index)`, index from `0`                       |

### Subject (variable: 28 bytes + texts and quests)

| Offset               | Type                                | Field              | Notes                                                       |
| -------------------- | ----------------------------------- | ------------------ | ----------------------------------------------------------- |
| `+0x00`              | u32                                 | preview_text_count | `getPreviewTextCount()`; `0` on the Combat subjects, `4` on the Life Skill subjects |
| `+0x04`              | str16[preview_text_count]           | preview_texts      | `getPreviewTextAt(index)`; `RESOURCE` keys (`PANEL_OLVIA_ACADEMY_SUBJECT_LIFE_PREVIEW_TEXT_1_01` "Key Point: ...") |
| `preview_texts+0x00` | Preview if preview_text_count != 0  | preview            | See Preview                                                 |
| `preview+0x00`       | u32                                 | start_quest        | `getStartQuestNo()`; packed quest ID, the first quest of `quests` on every subject |
| `preview+0x04`       | str16                               | subject_title      | `getSubjectTitle()`; `RESOURCE` key (`PANEL_OLVIA_ACADEMY_SUBJECT_LIFE_TITLE_1` "Gathering") |
| `subject_title+0x00` | str16                               | subject_desc       | `getSubjectDesc()`; `RESOURCE` key                          |
| `subject_desc+0x00`  | u32                                 | quest_count        | `getQuestCount()`                                           |
| `subject_desc+0x04`  | Subject Quest[quest_count]          | quests             | See Subject Quest                                           |

### Preview (variable: 24 bytes + texts)

The page the window opens before a subject's start quest is cleared
(`updateQuestInfoPage`); the window opens it only when
`getPreviewTextAt(0)` is not `nil`.

| Offset               | Type  | Field              | Notes                                                    |
| -------------------- | ----- | ------------------ | -------------------------------------------------------- |
| `+0x00`              | str16 | preview_title      | `getPreviewTitle()`; `RESOURCE` key (`PANEL_OLVIA_ACADEMY_SUBJECT_LIFE_PREVIEW_TITLE_1` "Nature's Goodies") |
| `preview_title+0x00` | str16 | preview_desc       | `getPreviewDesc()`; `RESOURCE` key                       |
| `preview_desc+0x00`  | str8  | preview_texture_id | `getPreviewTextureID()`; the page background (`Combine_Etc_OlviaSchoolAcademy_BG_11`) |

### Subject Quest (variable: 12 bytes + texture ID)

| Offset  | Type | Field            | Notes                                                              |
| ------- | ---- | ---------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | quest            | `getQuestNoAt(index)`; packed quest ID                             |
| `+0x04` | str8 | quest_texture_id | `getQuestTextureIDAt(index)`; the roadmap slot image, `OlviaSchoolAcademy_<Course>_Quest_<sub ID>` |

### Reward (variable: 36 bytes + texts and groups)

| Offset                  | Type                             | Field              | Notes                                                 |
| ----------------------- | -------------------------------- | ------------------ | ----------------------------------------------------- |
| `+0x00`                 | str16                            | reward_title       | `getRewardTitle()`; `RESOURCE` key (`PANEL_OLVIA_ACADEMY_FAMILYREWARD_TITLE_BATTLE` "Family Rewards - Combat") |
| `reward_title+0x00`     | str16                            | reward_sub_title   | `getRewardSubTitle()`; `RESOURCE` key                 |
| `reward_sub_title+0x00` | str16                            | reward_desc        | `getRewardDesc()`; `RESOURCE` key                     |
| `reward_desc+0x00`      | str8                             | reward_icon        | `getRewardIcon()`; texture ID of the tab icon         |
| `reward_icon+0x00`      | u32                              | reward_group_count | `getRewardGroupCount()`                               |
| `reward_icon+0x04`      | Reward Group[reward_group_count] | reward_groups      | `getRewardGroupAt(index)`, index from `0`             |

### Reward Group (variable: 12 bytes + title and quests)

| Offset                    | Type             | Field              | Notes                                                |
| ------------------------- | ---------------- | ------------------ | ---------------------------------------------------- |
| `+0x00`                   | str16            | reward_group_title | `getRewardGroupTitle()`; `RESOURCE` key, the Life Skill groups reuse the subject titles (`PANEL_OLVIA_ACADEMY_SUBJECT_LIFE_TITLE_1` "Gathering") |
| `reward_group_title+0x00` | u32              | quest_count        | `getQuestCount()`                                    |
| `reward_group_title+0x04` | u32[quest_count] | quests             | `getQuestNoAt(index)`; packed quest IDs              |

## Curricula and Rewards

On client 3482 the file holds two curricula with 2 and 9 subjects and two
family rewards with 1 and 9 groups. Every text resolves to an English LOC
type 37 text.

| Curriculum | Subject        | Quest chain | Quests | Preview texts |
| ---------- | -------------- | ----------: | -----: | ------------: |
| Combat     | Basic Tactics  | 2310        | 12     | 0             |
| Combat     | Field Tactics  | 2310        | 19     | 0             |
| Life Skill | Gathering      | 2325        | 10     | 4             |
| Life Skill | Fishing        | 2316        | 13     | 4             |
| Life Skill | Hunting        | 2314        | 13     | 4             |
| Life Skill | Cooking        | 2313        | 13     | 4             |
| Life Skill | Alchemy        | 2311        | 12     | 4             |
| Life Skill | Processing     | 2317        | 11     | 4             |
| Life Skill | Training       | 2312        | 14     | 4             |
| Life Skill | Farming        | 2318        | 12     | 4             |
| Life Skill | Sailing/Barter | 2315        | 13     | 4             |

| Reward                      | Group                    | Quests of chain 2323 |
| --------------------------- | ------------------------ | -------------------- |
| Family Rewards - Combat     | Combat                   | 1 to 36              |
| Family Rewards - Life Skill | Gathering                | 101 to 106           |
| Family Rewards - Life Skill | Fishing                  | 161 to 166           |
| Family Rewards - Life Skill | Hunting                  | 141 to 145           |
| Family Rewards - Life Skill | Cooking                  | 111 to 116           |
| Family Rewards - Life Skill | Alchemy                  | 121 to 126           |
| Family Rewards - Life Skill | Processing               | 171 to 175           |
| Family Rewards - Life Skill | Training                 | 131 to 135           |
| Family Rewards - Life Skill | Farming                  | 181 to 185           |
| Family Rewards - Life Skill | Sailing/Barter           | 151 to 155           |

## Field Names

No reference source has the file: it first appears on client 3186
(absent on client 3177), and a private server's `DataSheets.bexcel` on
client 1784 has no sheet with `Olvia` or `Academy` in its name. Every name
comes from the getter the client Lua (client 3482) calls on the object the
field belongs to: `panel_window_olviaacademy_main_all_1.luac` and
`_2.luac` call `getCurriculumTitle()`, `getCurriculumIcon()`,
`getSubjectCount()` and `getSubjectAt()` on a curriculum;
`getPreviewTextCount()`, `getPreviewTextAt()`, `getPreviewTitle()`,
`getPreviewDesc()`, `getPreviewTextureID()`, `getStartQuestNo()`,
`getSubjectTitle()`, `getSubjectDesc()`, `getQuestCount()`,
`getQuestNoAt()` and `getQuestTextureIDAt()` on a subject;
`getRewardTitle()`, `getRewardSubTitle()`, `getRewardDesc()`,
`getRewardIcon()`, `getRewardGroupCount()` and `getRewardGroupAt()` on a
reward; `getRewardGroupTitle()`, `getQuestCount()` and `getQuestNoAt()` on
a reward group. The texts go through `PAGetString(Defines.StringSheet_RESOURCE, ...)`
and the icons and textures through `ChangeTextureInfoTextureIDAsync()`,
which matches the `RESOURCE` keys and texture IDs the strings hold.

## Notes

- Decompressed size on client 3482: `17166` bytes; the walk ends at the
  last byte.
- The 142 subject quests are all in
  `olviaacademycurriculumquestlist.bss` (client 3482). The list holds 26
  more: `2308/1` and `2309/1` (the enrollment and graduation quests of
  [`olviaacademyseasonss.bss`](olviaacademyseasonss_bss.md)) and the 24
  `Material Support` and `Ship Support` quests at sub IDs 53 to 62, which
  no subject lists. Quest `2310/19` is in neither.
- The 85 reward group quests are exactly the quests of
  `olviaacademyrewardquestlist.bss` (client 3482).
- Each `quest_texture_id` ends in its quest's sub ID with two digits
  (`OlviaSchoolAcademy_Battle_Quest_13` on `2310/13`).
- The handler shows one row per subject and one per reward group, each
  with the fields of its curriculum or reward. The row key `row_ref`
  (`curriculum:1:0`, `reward:1:3`: section, then the two Lua indexes from
  `0`) is what the quest list views link to; each quest links to its row
  in the quest list file.

## Open Questions

### A Subject With Preview Texts but No Preview Page

The preview title, description and texture follow only when
`preview_text_count` is not `0`: the two Combat subjects store `0` and go
straight on to `start_quest`, the nine Life Skill subjects store `4` texts
and the three preview fields. Whether the client writes the three fields
for a subject on its own flag (and a subject could have a preview page with
no texts) or with the text list is open, since every subject on client 3482
has both or neither.
