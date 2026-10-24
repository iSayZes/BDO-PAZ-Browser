# `bdobatchsummonmonsterss.bss` Format

## Purpose

A PABR table of the party summon scrolls: the party leader (or a player
with no party) summons with `ToClient_RequestBatchSummonMonster(summonKey,
summonLevel)` in `panel_batchsummonmonster.luac`, which shows the level
with the Ancient Ruins raid party text `LUA_ANCIENT_RUINS_RAID_PARTY_LEVEL`.
Each row is one summon level of one scroll: the summoned monster and the
AP, damage reduction, evasion, accuracy and HP added to it. On client 3482
it holds 20 rows of six scrolls, among them the Ancient Relic Crystal
Summon Scroll (`41583`, levels 1 to 5), Cartian Spell (`41587`), Pila Fe
Scroll (`41595`), Manshaum Narc's Stone (`41619`), Ibedor's Scroll
(`65771`) and Rift's Echo (`721058`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | ------- | --------- |
| 3      | 2935 and later | 3483    | `bdobatchsummonmonsterss.bss` | 700   | 20 Row  | 34        |
| 2      | 1762 to 2932   | 2932    | `bdobatchsummonmonsterss.bss` | 780   | 20 Row  | 38        |
| 1      | 1743 to 1759   | 1759    | `bdobatchsummonmonsterss.bss` | 214   | 5 Row   | 38        |

| Layout | File                          | Known          | Unknown      |
| ------ | ----------------------------- | -------------- | ------------ |
| 3      | `bdobatchsummonmonsterss.bss` | 700 B (100.0%) | 0 B (0.0%)   |
| 2      | `bdobatchsummonmonsterss.bss` | 700 B (89.7%)  | 80 B (10.3%) |
| 1      | `bdobatchsummonmonsterss.bss` | 190 B (88.8%)  | 24 B (11.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `bd2fee4aba33`  |
| 3482   | Layout 3 | `bd2fee4aba33`  |
| 3474   | Layout 3 | `bd2fee4aba33`  |
| 3473   | Layout 3 | `bd2fee4aba33`  |
| 3464   | Layout 3 | `bd2fee4aba33`  |
| 3458   | Layout 3 | `bd2fee4aba33`  |
| 3454   | Layout 3 | `bd2fee4aba33`  |
| 3444   | Layout 3 | `bd2fee4aba33`  |
| 3435   | Layout 3 | `bd2fee4aba33`  |
| 3426   | Layout 3 | `bd2fee4aba33`  |
| 3418   | Layout 3 | `bd2fee4aba33`  |
| 3412   | Layout 3 | `bd2fee4aba33`  |
| 3402   | Layout 3 | `bd2fee4aba33`  |
| 3396   | Layout 3 | `bd2fee4aba33`  |
| 3387   | Layout 3 | `bd2fee4aba33`  |
| 3381   | Layout 3 | `bd2fee4aba33`  |
| 3373   | Layout 3 | `bd2fee4aba33`  |
| 3364   | Layout 3 | `bd2fee4aba33`  |
| 3356   | Layout 3 | `bd2fee4aba33`  |
| 3349   | Layout 3 | `bd2fee4aba33`  |
| 3342   | Layout 3 | `bd2fee4aba33`  |
| 3335   | Layout 3 | `bd2fee4aba33`  |
| 3326   | Layout 3 | `bd2fee4aba33`  |
| 3321   | Layout 3 | `bd2fee4aba33`  |
| 3314   | Layout 3 | `bd2fee4aba33`  |
| 3303   | Layout 3 | `bd2fee4aba33`  |
| 3302   | Layout 3 | `bd2fee4aba33`  |
| 3293   | Layout 3 | `bd2fee4aba33`  |
| 3283   | Layout 3 | `bd2fee4aba33`  |
| 3275   | Layout 3 | `bd2fee4aba33`  |
| 3267   | Layout 3 | `bd2fee4aba33`  |
| 3258   | Layout 3 | `bd2fee4aba33`  |
| 3251   | Layout 3 | `bd2fee4aba33`  |
| 3242   | Layout 3 | `bd2fee4aba33`  |
| 3235   | Layout 3 | `bd2fee4aba33`  |
| 3229   | Layout 3 | `bd2fee4aba33`  |
| 3212   | Layout 3 | `bd2fee4aba33`  |
| 3203   | Layout 3 | `bd2fee4aba33`  |
| 3193   | Layout 3 | `bd2fee4aba33`  |
| 3186   | Layout 3 | `bd2fee4aba33`  |
| 3177   | Layout 3 | `bd2fee4aba33`  |
| 3169   | Layout 3 | `bd2fee4aba33`  |
| 3158   | Layout 3 | `bd2fee4aba33`  |
| 3151   | Layout 3 | `bd2fee4aba33`  |
| 3144   | Layout 3 | `bd2fee4aba33`  |
| 3133   | Layout 3 | `bd2fee4aba33`  |
| 3125   | Layout 3 | `bd2fee4aba33`  |
| 3118   | Layout 3 | `bd2fee4aba33`  |
| 3111   | Layout 3 | `bd2fee4aba33`  |
| 3103   | Layout 3 | `bd2fee4aba33`  |
| 3095   | Layout 3 | `bd2fee4aba33`  |
| 3086   | Layout 3 | `bd2fee4aba33`  |
| 3072   | Layout 3 | `bd2fee4aba33`  |
| 3062   | Layout 3 | `bd2fee4aba33`  |
| 3052   | Layout 3 | `bd2fee4aba33`  |
| 3045   | Layout 3 | `bd2fee4aba33`  |
| 3037   | Layout 3 | `bd2fee4aba33`  |
| 3030   | Layout 3 | `bd2fee4aba33`  |
| 3021   | Layout 3 | `bd2fee4aba33`  |
| 3012   | Layout 3 | `bd2fee4aba33`  |
| 3002   | Layout 3 | `bd2fee4aba33`  |
| 2995   | Layout 3 | `bd2fee4aba33`  |
| 2987   | Layout 3 | `bd2fee4aba33`  |
| 2978   | Layout 3 | `bd2fee4aba33`  |
| 2970   | Layout 3 | `bd2fee4aba33`  |
| 2959   | Layout 3 | `bd2fee4aba33`  |
| 2951   | Layout 3 | `bd2fee4aba33`  |
| 2942   | Layout 3 | `bd2fee4aba33`  |
| 2935   | Layout 3 | `bd2fee4aba33`  |
| 2932   | Layout 2 | `bd2fee4aba33`  |
| 2923   | Layout 2 | `bd2fee4aba33`  |
| 2919   | Layout 2 | `bd2fee4aba33`  |
| 2907   | Layout 2 | `bd2fee4aba33`  |
| 2900   | Layout 2 | `bd2fee4aba33`  |
| 2891   | Layout 2 | `bd2fee4aba33`  |
| 2882   | Layout 2 | `bd2fee4aba33`  |
| 2872   | Layout 2 | `bd2fee4aba33`  |
| 2863   | Layout 2 | `bd2fee4aba33`  |
| 2855   | Layout 2 | `bd2fee4aba33`  |
| 2849   | Layout 2 | `bd2fee4aba33`  |
| 2844   | Layout 2 | `bd2fee4aba33`  |
| 2834   | Layout 2 | `bd2fee4aba33`  |
| 2825   | Layout 2 | `bd2fee4aba33`  |
| 2819   | Layout 2 | `bd2fee4aba33`  |
| 2811   | Layout 2 | `bd2fee4aba33`  |
| 2803   | Layout 2 | `bd2fee4aba33`  |
| 2794   | Layout 2 | `bd2fee4aba33`  |
| 2783   | Layout 2 | `bd2fee4aba33`  |
| 2774   | Layout 2 | `bd2fee4aba33`  |
| 2765   | Layout 2 | `bd2fee4aba33`  |
| 2756   | Layout 2 | `bd2fee4aba33`  |
| 2750   | Layout 2 | `bd2fee4aba33`  |
| 2743   | Layout 2 | `bd2fee4aba33`  |
| 2736   | Layout 2 | `bd2fee4aba33`  |
| 2726   | Layout 2 | `bd2fee4aba33`  |
| 2717   | Layout 2 | `bd2fee4aba33`  |
| 2709   | Layout 2 | `bd2fee4aba33`  |
| 2703   | Layout 2 | `bd2fee4aba33`  |
| 2695   | Layout 2 | `bd2fee4aba33`  |
| 2684   | Layout 2 | `bd2fee4aba33`  |
| 2672   | Layout 2 | `bd2fee4aba33`  |
| 2665   | Layout 2 | `bd2fee4aba33`  |
| 2657   | Layout 2 | `bd2fee4aba33`  |
| 2649   | Layout 2 | `bd2fee4aba33`  |
| 2644   | Layout 2 | `bd2fee4aba33`  |
| 2637   | Layout 2 | `bd2fee4aba33`  |
| 2629   | Layout 2 | `bd2fee4aba33`  |
| 2619   | Layout 2 | `bd2fee4aba33`  |
| 2612   | Layout 2 | `bd2fee4aba33`  |
| 2606   | Layout 2 | `bd2fee4aba33`  |
| 2602   | Layout 2 | `bd2fee4aba33`  |
| 2601   | Layout 2 | `bd2fee4aba33`  |
| 2592   | Layout 2 | `bd2fee4aba33`  |
| 2583   | Layout 2 | `bd2fee4aba33`  |
| 2575   | Layout 2 | `bd2fee4aba33`  |
| 2567   | Layout 2 | `bd2fee4aba33`  |
| 2560   | Layout 2 | `bd2fee4aba33`  |
| 2553   | Layout 2 | `bd2fee4aba33`  |
| 2545   | Layout 2 | `bd2fee4aba33`  |
| 2538   | Layout 2 | `bd2fee4aba33`  |
| 2529   | Layout 2 | `bd2fee4aba33`  |
| 2519   | Layout 2 | `bd2fee4aba33`  |
| 2513   | Layout 2 | `bd2fee4aba33`  |
| 2510   | Layout 2 | `bd2fee4aba33`  |
| 2507   | Layout 2 | `bd2fee4aba33`  |
| 2503   | Layout 2 | `bd2fee4aba33`  |
| 2498   | Layout 2 | `bd2fee4aba33`  |
| 2492   | Layout 2 | `bd2fee4aba33`  |
| 2487   | Layout 2 | `bd2fee4aba33`  |
| 2480   | Layout 2 | `bd2fee4aba33`  |
| 2474   | Layout 2 | `bd2fee4aba33`  |
| 2468   | Layout 2 | `bd2fee4aba33`  |
| 2460   | Layout 2 | `bd2fee4aba33`  |
| 2453   | Layout 2 | `bd2fee4aba33`  |
| 2444   | Layout 2 | `bd2fee4aba33`  |
| 2438   | Layout 2 | `bd2fee4aba33`  |
| 2434   | Layout 2 | `bd2fee4aba33`  |
| 2429   | Layout 2 | `bd2fee4aba33`  |
| 2421   | Layout 2 | `bd2fee4aba33`  |
| 2414   | Layout 2 | `bd2fee4aba33`  |
| 2407   | Layout 2 | `bd2fee4aba33`  |
| 2401   | Layout 2 | `bd2fee4aba33`  |
| 2397   | Layout 2 | `bd2fee4aba33`  |
| 2393   | Layout 2 | `bd2fee4aba33`  |
| 2384   | Layout 2 | `bd2fee4aba33`  |
| 2378   | Layout 2 | `bd2fee4aba33`  |
| 2372   | Layout 2 | `bd2fee4aba33`  |
| 2358   | Layout 2 | `bd2fee4aba33`  |
| 2352   | Layout 2 | `bd2fee4aba33`  |
| 2347   | Layout 2 | `bd2fee4aba33`  |
| 2343   | Layout 2 | `bd2fee4aba33`  |
| 2335   | Layout 2 | `bd2fee4aba33`  |
| 2327   | Layout 2 | `bd2fee4aba33`  |
| 2324   | Layout 2 | `bd2fee4aba33`  |
| 2319   | Layout 2 | `bd2fee4aba33`  |
| 2313   | Layout 2 | `bd2fee4aba33`  |
| 2308   | Layout 2 | `bd2fee4aba33`  |
| 2302   | Layout 2 | `bd2fee4aba33`  |
| 2295   | Layout 2 | `bd2fee4aba33`  |
| 2290   | Layout 2 | `bd2fee4aba33`  |
| 2284   | Layout 2 | `bd2fee4aba33`  |
| 2276   | Layout 2 | `bd2fee4aba33`  |
| 2269   | Layout 2 | `bd2fee4aba33`  |
| 2259   | Layout 2 | `bd2fee4aba33`  |
| 2250   | Layout 2 | `bd2fee4aba33`  |
| 2243   | Layout 2 | `bd2fee4aba33`  |
| 2235   | Layout 2 | `bd2fee4aba33`  |
| 2229   | Layout 2 | `bd2fee4aba33`  |
| 2224   | Layout 2 | `bd2fee4aba33`  |
| 2218   | Layout 2 | `bd2fee4aba33`  |
| 2215   | Layout 2 | `bd2fee4aba33`  |
| 2207   | Layout 2 | `bd2fee4aba33`  |
| 2203   | Layout 2 | `bd2fee4aba33`  |
| 2196   | Layout 2 | `bd2fee4aba33`  |
| 2192   | Layout 2 | `bd2fee4aba33`  |
| 2189   | Layout 2 | `bd2fee4aba33`  |
| 2183   | Layout 2 | `bd2fee4aba33`  |
| 2179   | Layout 2 | `bd2fee4aba33`  |
| 2171   | Layout 2 | `bd2fee4aba33`  |
| 2163   | Layout 2 | `bd2fee4aba33`  |
| 2156   | Layout 2 | `bd2fee4aba33`  |
| 2151   | Layout 2 | `bd2fee4aba33`  |
| 2147   | Layout 2 | `bd2fee4aba33`  |
| 2142   | Layout 2 | `bd2fee4aba33`  |
| 2138   | Layout 2 | `bd2fee4aba33`  |
| 2134   | Layout 2 | `bd2fee4aba33`  |
| 2130   | Layout 2 | `bd2fee4aba33`  |
| 2122   | Layout 2 | `bd2fee4aba33`  |
| 2107   | Layout 2 | `bd2fee4aba33`  |
| 2098   | Layout 2 | `bd2fee4aba33`  |
| 2089   | Layout 2 | `bd2fee4aba33`  |
| 2081   | Layout 2 | `bd2fee4aba33`  |
| 2073   | Layout 2 | `bd2fee4aba33`  |
| 2067   | Layout 2 | `bd2fee4aba33`  |
| 2063   | Layout 2 | `bd2fee4aba33`  |
| 2059   | Layout 2 | `bd2fee4aba33`  |
| 2052   | Layout 2 | `bd2fee4aba33`  |
| 2044   | Layout 2 | `bd2fee4aba33`  |
| 2039   | Layout 2 | `bd2fee4aba33`  |
| 2032   | Layout 2 | `bd2fee4aba33`  |
| 2025   | Layout 2 | `bd2fee4aba33`  |
| 2011   | Layout 2 | `bd2fee4aba33`  |
| 2005   | Layout 2 | `bd2fee4aba33`  |
| 2000   | Layout 2 | `bd2fee4aba33`  |
| 1996   | Layout 2 | `bd2fee4aba33`  |
| 1991   | Layout 2 | `bd2fee4aba33`  |
| 1985   | Layout 2 | `bd2fee4aba33`  |
| 1980   | Layout 2 | `bd2fee4aba33`  |
| 1969   | Layout 2 | `bd2fee4aba33`  |
| 1964   | Layout 2 | `bd2fee4aba33`  |
| 1958   | Layout 2 | `bd2fee4aba33`  |
| 1950   | Layout 2 | `bd2fee4aba33`  |
| 1945   | Layout 2 | `bd2fee4aba33`  |
| 1937   | Layout 2 | `bd2fee4aba33`  |
| 1933   | Layout 2 | `bd2fee4aba33`  |
| 1927   | Layout 2 | `bd2fee4aba33`  |
| 1921   | Layout 2 | `bd2fee4aba33`  |
| 1914   | Layout 2 | `bd2fee4aba33`  |
| 1908   | Layout 2 | `bd2fee4aba33`  |
| 1897   | Layout 2 | `bd2fee4aba33`  |
| 1892   | Layout 2 | `bd2fee4aba33`  |
| 1886   | Layout 2 | `bd2fee4aba33`  |
| 1881   | Layout 2 | `bd2fee4aba33`  |
| 1871   | Layout 2 | `bd2fee4aba33`  |
| 1866   | Layout 2 | `bd2fee4aba33`  |
| 1862   | Layout 2 | `bd2fee4aba33`  |
| 1854   | Layout 2 | `bd2fee4aba33`  |
| 1846   | Layout 2 | `bd2fee4aba33`  |
| 1838   | Layout 2 | `bd2fee4aba33`  |
| 1832   | Layout 2 | `bd2fee4aba33`  |
| 1826   | Layout 2 | `bd2fee4aba33`  |
| 1822   | Layout 2 | `bd2fee4aba33`  |
| 1818   | Layout 2 | `bd2fee4aba33`  |
| 1804   | Layout 2 | `bd2fee4aba33`  |
| 1794   | Layout 2 | `bd2fee4aba33`  |
| 1790   | Layout 2 | `bd2fee4aba33`  |
| 1784   | Layout 2 | `bd2fee4aba33`  |
| 1774   | Layout 2 | `bd2fee4aba33`  |
| 1771   | Layout 2 | `bd2fee4aba33`  |
| 1762   | Layout 2 | `bd2fee4aba33`  |
| 1759   | Layout 1 | `bd2fee4aba33`  |
| 1754   | Layout 1 | `bd2fee4aba33`  |
| 1749   | Layout 1 | `bd2fee4aba33`  |
| 1743   | Layout 1 | `bd2fee4aba33`  |
| 1737   | No file  | `bd2fee4aba33`  |
| 1731   | No file  | `bd2fee4aba33`  |
| 1725   | No file  | `bd2fee4aba33`  |
| 1717   | No file  | `bd2fee4aba33`  |
| 1710   | No file  | `bd2fee4aba33`  |
| 1704   | No file  | `bd2fee4aba33`  |
| 1698   | No file  | `bd2fee4aba33`  |
| 1690   | No file  | `bd2fee4aba33`  |
| 1685   | No file  | `bd2fee4aba33`  |
| 1680   | No file  | `bd2fee4aba33`  |
| 1674   | No file  | `bd2fee4aba33`  |
| 1668   | No file  | `bd2fee4aba33`  |
| 1659   | No file  | `bd2fee4aba33`  |
| 1649   | No file  | `bd2fee4aba33`  |
| 1642   | No file  | `bd2fee4aba33`  |
| 1636   | No file  | `bd2fee4aba33`  |
| 1628   | No file  | `bd2fee4aba33`  |
| 1622   | No file  | `bd2fee4aba33`  |
| 1614   | No file  | `bd2fee4aba33`  |
| 1608   | No file  | `bd2fee4aba33`  |
| 1602   | No file  | `bd2fee4aba33`  |
| 1598   | No file  | `bd2fee4aba33`  |
| 1594   | No file  | `bd2fee4aba33`  |
| 1590   | No file  | `bd2fee4aba33`  |
| 1587   | No file  | `bd2fee4aba33`  |
| 1584   | No file  | `bd2fee4aba33`  |
| 1579   | No file  | `bd2fee4aba33`  |
| 1572   | No file  | `bd2fee4aba33`  |
| 1565   | No file  | `bd2fee4aba33`  |
| 1559   | No file  | `bd2fee4aba33`  |
| 1554   | No file  | `bd2fee4aba33`  |
| 1547   | No file  | `bd2fee4aba33`  |
| 1537   | No file  | `bd2fee4aba33`  |
| 1529   | No file  | `bd2fee4aba33`  |
| 1524   | No file  | `bd2fee4aba33`  |
| 1519   | No file  | `bd2fee4aba33`  |
| 1509   | No file  | `bd2fee4aba33`  |
| 1506   | No file  | `bd2fee4aba33`  |
| 1504   | No file  | `bd2fee4aba33`  |
| 1500   | No file  | `bd2fee4aba33`  |
| 1493   | No file  | `bd2fee4aba33`  |
| 1489   | No file  | `bd2fee4aba33`  |
| 1485   | No file  | `bd2fee4aba33`  |
| 1481   | No file  | `bd2fee4aba33`  |
| 1474   | No file  | `bd2fee4aba33`  |
| 1466   | No file  | `bd2fee4aba33`  |
| 1462   | No file  | `bd2fee4aba33`  |
| 1459   | No file  | `bd2fee4aba33`  |
| 1453   | No file  | `bd2fee4aba33`  |
| 1450   | No file  | `bd2fee4aba33`  |
| 1445   | No file  | `bd2fee4aba33`  |
| 1439   | No file  | `bd2fee4aba33`  |
| 1433   | No file  | `bd2fee4aba33`  |
| 1430   | No file  | `bd2fee4aba33`  |
| 1426   | No file  | `bd2fee4aba33`  |
| 1421   | No file  | `bd2fee4aba33`  |
| 1417   | No file  | `bd2fee4aba33`  |
| 1416   | No file  | `bd2fee4aba33`  |
| 1409   | No file  | `bd2fee4aba33`  |
| 1405   | No file  | `bd2fee4aba33`  |
| 1401   | No file  | `bd2fee4aba33`  |
| 1396   | No file  | `bd2fee4aba33`  |
| 1391   | No file  | `bd2fee4aba33`  |
| 1390   | No file  | `bd2fee4aba33`  |
| 1386   | No file  | `bd2fee4aba33`  |
| 1381   | No file  | `bd2fee4aba33`  |
| 1379   | No file  | `bd2fee4aba33`  |
| 1372   | No file  | `bd2fee4aba33`  |
| 1366   | No file  | `bd2fee4aba33`  |
| 1364   | No file  | `bd2fee4aba33`  |
| 1363   | No file  | `bd2fee4aba33`  |
| 1360   | No file  | `bd2fee4aba33`  |
| 1358   | No file  | `bd2fee4aba33`  |
| 1355   | No file  | `bd2fee4aba33`  |
| 1351   | No file  | `bd2fee4aba33`  |
| 1348   | No file  | `bd2fee4aba33`  |
| 1346   | No file  | `bd2fee4aba33`  |
| 1341   | No file  | `bd2fee4aba33`  |
| 1340   | No file  | `bd2fee4aba33`  |
| 1338   | No file  | `bd2fee4aba33`  |
| 1335   | No file  | `bd2fee4aba33`  |
| 1333   | No file  | `bd2fee4aba33`  |
| 1329   | No file  | `bd2fee4aba33`  |
| 1327   | No file  | `bd2fee4aba33`  |
| 1324   | No file  | `bd2fee4aba33`  |
| 1321   | No file  | `bd2fee4aba33`  |
| 1319   | No file  | `bd2fee4aba33`  |
| 1318   | No file  | `bd2fee4aba33`  |
| 1316   | No file  | `bd2fee4aba33`  |
| 1313   | No file  | `bd2fee4aba33`  |
| 1311   | No file  | `bd2fee4aba33`  |
| 1309   | No file  | `bd2fee4aba33`  |
| 1304   | No file  | `bd2fee4aba33`  |
| 1292   | No file  | `bd2fee4aba33`  |
| 1286   | No file  | `bd2fee4aba33`  |
| 1280   | No file  | `bd2fee4aba33`  |
| 1276   | No file  | `bd2fee4aba33`  |
| 1267   | No file  | `bd2fee4aba33`  |
| 1261   | No file  | `bd2fee4aba33`  |
| 1256   | No file  | `bd2fee4aba33`  |
| 1250   | No file  | `bd2fee4aba33`  |
| 1246   | No file  | `bd2fee4aba33`  |
| 1239   | No file  | `bd2fee4aba33`  |
| 1230   | No file  | `bd2fee4aba33`  |
| 1226   | No file  | `bd2fee4aba33`  |
| 1220   | No file  | `bd2fee4aba33`  |
| 1217   | No file  | `bd2fee4aba33`  |
| 1211   | No file  | `bd2fee4aba33`  |
| 1210   | No file  | `bd2fee4aba33`  |
| 1208   | No file  | `bd2fee4aba33`  |
| 1203   | No file  | `bd2fee4aba33`  |
| 1197   | No file  | `bd2fee4aba33`  |
| 1194   | No file  | `bd2fee4aba33`  |
| 1192   | No file  | `bd2fee4aba33`  |
| 1187   | No file  | `bd2fee4aba33`  |
| 1183   | No file  | `bd2fee4aba33`  |
| 1177   | No file  | `bd2fee4aba33`  |
| 1173   | No file  | `bd2fee4aba33`  |
| 1167   | No file  | `bd2fee4aba33`  |
| 1164   | No file  | `bd2fee4aba33`  |
| 1156   | No file  | `bd2fee4aba33`  |
| 1149   | No file  | `bd2fee4aba33`  |
| 1144   | No file  | `bd2fee4aba33`  |
| 1137   | No file  | `bd2fee4aba33`  |
| 1132   | No file  | `bd2fee4aba33`  |
| 1127   | No file  | `bd2fee4aba33`  |
| 1122   | No file  | `bd2fee4aba33`  |
| 1118   | No file  | `bd2fee4aba33`  |
| 1114   | No file  | `bd2fee4aba33`  |
| 1109   | No file  | `bd2fee4aba33`  |
| 1102   | No file  | `bd2fee4aba33`  |
| 1096   | No file  | `bd2fee4aba33`  |
| 1088   | No file  | `bd2fee4aba33`  |
| 1081   | No file  | `bd2fee4aba33`  |
| 1076   | No file  | `bd2fee4aba33`  |
| 1069   | No file  | `bd2fee4aba33`  |
| 1064   | No file  | `bd2fee4aba33`  |
| 1058   | No file  | `bd2fee4aba33`  |
| 1051   | No file  | `bd2fee4aba33`  |
| 1044   | No file  | `bd2fee4aba33`  |
| 1036   | No file  | `bd2fee4aba33`  |
| 1026   | No file  | `bd2fee4aba33`  |
| 1016   | No file  | `bd2fee4aba33`  |
| 1009   | No file  | `bd2fee4aba33`  |
| 1005   | No file  | `bd2fee4aba33`  |
| 1000   | No file  | `bd2fee4aba33`  |
| 998    | No file  | `bd2fee4aba33`  |
| 990    | No file  | `bd2fee4aba33`  |
| 979    | No file  | `bd2fee4aba33`  |
| 972    | No file  | `bd2fee4aba33`  |
| 963    | No file  | `bd2fee4aba33`  |
| 955    | No file  | `bd2fee4aba33`  |
| 946    | No file  | `bd2fee4aba33`  |
| 938    | No file  | `bd2fee4aba33`  |
| 927    | No file  | `bd2fee4aba33`  |
| 911    | No file  | `bd2fee4aba33`  |
| 904    | No file  | `bd2fee4aba33`  |
| 899    | No file  | `bd2fee4aba33`  |
| 894    | No file  | `bd2fee4aba33`  |
| 885    | No file  | `bd2fee4aba33`  |
| 879    | No file  | `bd2fee4aba33`  |
| 872    | No file  | `bd2fee4aba33`  |
| 864    | No file  | `bd2fee4aba33`  |
| 855    | No file  | `bd2fee4aba33`  |
| 853    | No file  | `bd2fee4aba33`  |
| 845    | No file  | `bd2fee4aba33`  |
| 837    | No file  | `bd2fee4aba33`  |
| 829    | No file  | `bd2fee4aba33`  |
| 822    | No file  | `bd2fee4aba33`  |
| 814    | No file  | `bd2fee4aba33`  |
| 805    | No file  | `bd2fee4aba33`  |
| 794    | No file  | `bd2fee4aba33`  |
| 787    | No file  | `bd2fee4aba33`  |
| 780    | No file  | `bd2fee4aba33`  |
| 771    | No file  | `bd2fee4aba33`  |
| 760    | No file  | `bd2fee4aba33`  |
| 748    | No file  | `bd2fee4aba33`  |
| 741    | No file  | `bd2fee4aba33`  |
| 736    | No file  | `bd2fee4aba33`  |
| 731    | No file  | `bd2fee4aba33`  |
| 723    | No file  | `bd2fee4aba33`  |
| 711    | No file  | `bd2fee4aba33`  |
| 707    | No file  | `bd2fee4aba33`  |
| 697    | No file  | `bd2fee4aba33`  |
| 689    | No file  | `bd2fee4aba33`  |
| 683    | No file  | `bd2fee4aba33`  |
| 678    | No file  | `bd2fee4aba33`  |
| 670    | No file  | `bd2fee4aba33`  |
| 661    | No file  | `bd2fee4aba33`  |
| 656    | No file  | `bd2fee4aba33`  |
| 652    | No file  | `bd2fee4aba33`  |
| 643    | No file  | `bd2fee4aba33`  |
| 637    | No file  | `bd2fee4aba33`  |
| 630    | No file  | `bd2fee4aba33`  |
| 627    | No file  | `bd2fee4aba33`  |
| 621    | No file  | `bd2fee4aba33`  |
| 617    | No file  | `bd2fee4aba33`  |
| 615    | No file  | `bd2fee4aba33`  |
| 606    | No file  | `bd2fee4aba33`  |
| 599    | No file  | `bd2fee4aba33`  |
| 592    | No file  | `bd2fee4aba33`  |
| 586    | No file  | `bd2fee4aba33`  |
| 577    | No file  | `bd2fee4aba33`  |
| 569    | No file  | `bd2fee4aba33`  |
| 561    | No file  | `bd2fee4aba33`  |
| 554    | No file  | `bd2fee4aba33`  |
| 542    | No file  | `bd2fee4aba33`  |
| 532    | No file  | `bd2fee4aba33`  |
| 531    | No file  | `bd2fee4aba33`  |
| 526    | No file  | `bd2fee4aba33`  |
| 521    | No file  | `bd2fee4aba33`  |
| 517    | No file  | `bd2fee4aba33`  |
| 510    | No file  | `bd2fee4aba33`  |
| 508    | No file  | `bd2fee4aba33`  |
| 504    | No file  | `bd2fee4aba33`  |
| 497    | No file  | `bd2fee4aba33`  |
| 491    | No file  | `bd2fee4aba33`  |
| 485    | No file  | `bd2fee4aba33`  |
| 478    | No file  | `bd2fee4aba33`  |
| 472    | No file  | `bd2fee4aba33`  |
| 466    | No file  | `bd2fee4aba33`  |
| 457    | No file  | `bd2fee4aba33`  |
| 452    | No file  | `bd2fee4aba33`  |
| 449    | No file  | `bd2fee4aba33`  |
| 435    | No file  | `bd2fee4aba33`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                          |
| --------------------- | -------- | --------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) and character names (LOC type 6) |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (34 bytes)

| Offset  | Type | Field         | Notes                                                                    |
| ------- | ---- | ------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | summon_key    | Row key, `summon_level << 24 \| item_key`                                 |
| `+0x04` | u32  | item_key      | The summon scroll, an `itemenchant.dbss` item ID                         |
| `+0x08` | u32  | summon_level  | `1` to `5`                                                               |
| `+0x0C` | f32  | added_dd      | AP added to the summoned monster                                         |
| `+0x10` | f32  | added_pv      | Damage reduction added                                                   |
| `+0x14` | f32  | added_dv      | Evasion added; equal to `added_pv` on every row of client 3482           |
| `+0x18` | f32  | added_hit     | Accuracy added                                                           |
| `+0x1C` | f32  | added_hp      | HP added                                                                 |
| `+0x20` | u16  | character_key | The summoned monster, a `characterstatic.dbss` key (LOC type 6 name)     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 2

### Row (38 bytes)

| Offset  | Type | Field                  | Notes                                                       |
| ------- | ---- | ---------------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | summon_key             | Row key, `summon_level << 24 \| item_key`                    |
| `+0x04` | u32  | item_key               | The summon scroll                                           |
| `+0x08` | u32  | summon_level           | `1` to `5`                                                  |
| `+0x0C` | f32  | added_dd               | AP added                                                    |
| `+0x10` | f32  | added_pv               | Damage reduction added                                      |
| `+0x14` | f32  | added_dv               | Evasion added; `0` on every row of client 1784              |
| `+0x18` | f32  | added_hit              | Accuracy added                                              |
| `+0x1C` | f32  | added_hp               | HP added                                                    |
| `+0x20` | f32  | unknown_after_added_hp | `0` on every row of client 1784; Layout 3 drops it          |
| `+0x24` | u16  | character_key          | The summoned monster                                        |

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                                 |
| ------------------- | -------------- | ------------ | ----------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                          |
| `+0x04`             | u32            | unknown_04   | `5` on client 1749, equal to `row_count`              |
| `+0x08`             | u32            | row_count    | Number of rows                                        |
| `+0x0C`             | Row[row_count] | rows         | See Row                                               |
| `rows+0x00`         | String Table   | string_table | See String Table                                      |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends         |
| `string_table+0x04` | u32            | zero         | Always `0`                                            |

## Field Names

The names are the `BatchSummonMonsterStaticStatus` members that the
server dump of a private server on client 1784 names in its load checks
(`_addedDD`, `_addedPV`, `_addedDV`, `_addedHit`, `_addedHp`, `_itemKey`,
`_characterKey`, `_summonLevel`). The `BatchSpawnMonsterByItem` sheet of
that server's `DataSheets.bexcel` matches the client 1784 file by value on
6 of 6 rows: `TargetItemkey` is `item_key`, `SummonLevel` is
`summon_level`, `AddedDD`, `AddedPV`, `AddedHit` and `AddedHP` are the
fields of the same names, and `MonsterKey` is `character_key`. The live
file of client 3482 holds the same values for those 6 keys.

`AddedDV` and `AddedCri` are `0` on every sheet row, so the values do not
place them. `added_dv` is the f32 after `added_pv` by the member order of
the load checks (`_addedPV`, then `_addedDV`, then `_addedHit`), and
client 3482 sets it to the `added_pv` value. The f32 that Layout 2 holds
after `added_hp` is the one column left, `AddedCri`, but no client data
confirms it, so it stays `unknown_after_added_hp`. The sheet's
`MaxCount`, `DropGroupKey` and `GroupDrop0` to `GroupDrop4` columns are
not in the client file.

## Notes

- Layout 1 (client 1749, the first client with the file) stores a u32
  before `row_count` that equals it: 5 rows, levels 1 to 5 of `41583`.
- `summon_key` packs the level into the top byte of the item key, as
  [`elementalmonsterreward.bss`](elementalmonsterreward_bss.md) packs an
  enchant level: `0x0100A26F` is level 1 of item `41583`.
- The rows of one scroll can name different monsters per level: levels 1
  to 3 of `41583` summon Ancient Relic Crystal `22649`, levels 4 and 5 the
  Ancient Relic Crystal `22600`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`.

## Open Questions

### The Dropped Field of Layout 2

Layout 2 holds an f32 after `added_hp` that is `0` on every row of client
1784; it would be the sheet's `AddedCri` column, the one sheet stat with
no load check in the server dump. Layout 3 no longer has it.
