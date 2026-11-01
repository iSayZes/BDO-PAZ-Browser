# `sequencetutorial_equipment.bss` and `cutscenetutorial_equipment.bss` Format

## Purpose

Costume items per class for tutorial sequences and cutscenes: per
sequence or cutscene file, and per class type, the item IDs of six
outfit pieces (main weapon, sub-weapon, helmet, armor, gloves, shoes).
The items are appearance costumes (`600118` [Warrior] Cornelius
Longsword, "Changes the appearance of your character's longsword").
Two files share the format:

| File                             | Rows name                                                     |
| -------------------------------- | ------------------------------------------------------------- |
| `sequencetutorial_equipment.bss` | Sequences under `sequence/` (`CS_Tutorial_Illezra_00.pas`, `CS_OVAC_03_Admission.pas`) |
| `cutscenetutorial_equipment.bss` | Cutscenes under `character/cutscene/` (`CS_Tutorial_00_Illezra_0000.pas`, `CS_Yolunakea_01_Protokea_0000.pas`) |

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                             | Bytes | Records                     | Row bytes |
| ------ | -------------- | -------------------------------- | ----- | --------------------------- | --------- |
| 1      | 1866 and later | `cutscenetutorial_equipment.bss` | 9,356 | 352 Class Equipment, 11 Row | 25        |
| 1      | 2401 and later | `sequencetutorial_equipment.bss` | 3,389 | 128 Class Equipment, 4 Row  | 25        |

| Layout | File                             | Known            | Unknown    |
| ------ | -------------------------------- | ---------------- | ---------- |
| 1      | `cutscenetutorial_equipment.bss` | 9,356 B (100.0%) | 0 B (0.0%) |
| 1      | `sequencetutorial_equipment.bss` | 3,389 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `691ba0d1a983`  |
| 3482   | Layout 1 | `691ba0d1a983`  |
| 3474   | Layout 1 | `691ba0d1a983`  |
| 3473   | Layout 1 | `691ba0d1a983`  |
| 3464   | Layout 1 | `691ba0d1a983`  |
| 3458   | Layout 1 | `691ba0d1a983`  |
| 3454   | Layout 1 | `691ba0d1a983`  |
| 3444   | Layout 1 | `691ba0d1a983`  |
| 3435   | Layout 1 | `691ba0d1a983`  |
| 3426   | Layout 1 | `691ba0d1a983`  |
| 3418   | Layout 1 | `691ba0d1a983`  |
| 3412   | Layout 1 | `691ba0d1a983`  |
| 3402   | Layout 1 | `691ba0d1a983`  |
| 3396   | Layout 1 | `691ba0d1a983`  |
| 3387   | Layout 1 | `691ba0d1a983`  |
| 3381   | Layout 1 | `691ba0d1a983`  |
| 3373   | Layout 1 | `691ba0d1a983`  |
| 3364   | Layout 1 | `691ba0d1a983`  |
| 3356   | Layout 1 | `691ba0d1a983`  |
| 3349   | Layout 1 | `691ba0d1a983`  |
| 3342   | Layout 1 | `691ba0d1a983`  |
| 3335   | Layout 1 | `691ba0d1a983`  |
| 3326   | Layout 1 | `691ba0d1a983`  |
| 3321   | Layout 1 | `691ba0d1a983`  |
| 3314   | Layout 1 | `691ba0d1a983`  |
| 3303   | Layout 1 | `691ba0d1a983`  |
| 3302   | Layout 1 | `691ba0d1a983`  |
| 3293   | Layout 1 | `691ba0d1a983`  |
| 3283   | Layout 1 | `691ba0d1a983`  |
| 3275   | Layout 1 | `691ba0d1a983`  |
| 3267   | Layout 1 | `691ba0d1a983`  |
| 3258   | Layout 1 | `691ba0d1a983`  |
| 3251   | Layout 1 | `691ba0d1a983`  |
| 3242   | Layout 1 | `691ba0d1a983`  |
| 3235   | Layout 1 | `691ba0d1a983`  |
| 3229   | Layout 1 | `691ba0d1a983`  |
| 3212   | Layout 1 | `691ba0d1a983`  |
| 3203   | Layout 1 | `691ba0d1a983`  |
| 3193   | Layout 1 | `691ba0d1a983`  |
| 3186   | Layout 1 | `691ba0d1a983`  |
| 3177   | Layout 1 | `691ba0d1a983`  |
| 3169   | Layout 1 | `691ba0d1a983`  |
| 3158   | Layout 1 | `691ba0d1a983`  |
| 3151   | Layout 1 | `691ba0d1a983`  |
| 3144   | Layout 1 | `691ba0d1a983`  |
| 3133   | Layout 1 | `691ba0d1a983`  |
| 3125   | Layout 1 | `691ba0d1a983`  |
| 3118   | Layout 1 | `691ba0d1a983`  |
| 3111   | Layout 1 | `691ba0d1a983`  |
| 3103   | Layout 1 | `691ba0d1a983`  |
| 3095   | Layout 1 | `691ba0d1a983`  |
| 3086   | Layout 1 | `691ba0d1a983`  |
| 3072   | Layout 1 | `691ba0d1a983`  |
| 3062   | Layout 1 | `691ba0d1a983`  |
| 3052   | Layout 1 | `691ba0d1a983`  |
| 3045   | Layout 1 | `691ba0d1a983`  |
| 3037   | Layout 1 | `691ba0d1a983`  |
| 3030   | Layout 1 | `691ba0d1a983`  |
| 3021   | Layout 1 | `691ba0d1a983`  |
| 3012   | Layout 1 | `691ba0d1a983`  |
| 3002   | Layout 1 | `691ba0d1a983`  |
| 2995   | Layout 1 | `691ba0d1a983`  |
| 2987   | Layout 1 | `691ba0d1a983`  |
| 2978   | Layout 1 | `691ba0d1a983`  |
| 2970   | Layout 1 | `691ba0d1a983`  |
| 2959   | Layout 1 | `691ba0d1a983`  |
| 2951   | Layout 1 | `691ba0d1a983`  |
| 2942   | Layout 1 | `691ba0d1a983`  |
| 2935   | Layout 1 | `691ba0d1a983`  |
| 2932   | Layout 1 | `691ba0d1a983`  |
| 2923   | Layout 1 | `691ba0d1a983`  |
| 2919   | Layout 1 | `691ba0d1a983`  |
| 2907   | Layout 1 | `691ba0d1a983`  |
| 2900   | Layout 1 | `691ba0d1a983`  |
| 2891   | Layout 1 | `691ba0d1a983`  |
| 2882   | Layout 1 | `691ba0d1a983`  |
| 2872   | Layout 1 | `691ba0d1a983`  |
| 2863   | Layout 1 | `691ba0d1a983`  |
| 2855   | Layout 1 | `691ba0d1a983`  |
| 2849   | Layout 1 | `691ba0d1a983`  |
| 2844   | Layout 1 | `691ba0d1a983`  |
| 2834   | Layout 1 | `691ba0d1a983`  |
| 2825   | Layout 1 | `691ba0d1a983`  |
| 2819   | Layout 1 | `691ba0d1a983`  |
| 2811   | Layout 1 | `691ba0d1a983`  |
| 2803   | Layout 1 | `691ba0d1a983`  |
| 2794   | Layout 1 | `691ba0d1a983`  |
| 2783   | Layout 1 | `691ba0d1a983`  |
| 2774   | Layout 1 | `691ba0d1a983`  |
| 2765   | Layout 1 | `691ba0d1a983`  |
| 2756   | Layout 1 | `691ba0d1a983`  |
| 2750   | Layout 1 | `691ba0d1a983`  |
| 2743   | Layout 1 | `691ba0d1a983`  |
| 2736   | Layout 1 | `691ba0d1a983`  |
| 2726   | Layout 1 | `691ba0d1a983`  |
| 2717   | Layout 1 | `691ba0d1a983`  |
| 2709   | Layout 1 | `691ba0d1a983`  |
| 2703   | Layout 1 | `691ba0d1a983`  |
| 2695   | Layout 1 | `691ba0d1a983`  |
| 2684   | Layout 1 | `691ba0d1a983`  |
| 2672   | Layout 1 | `691ba0d1a983`  |
| 2665   | Layout 1 | `691ba0d1a983`  |
| 2657   | Layout 1 | `691ba0d1a983`  |
| 2649   | Layout 1 | `691ba0d1a983`  |
| 2644   | Layout 1 | `691ba0d1a983`  |
| 2637   | Layout 1 | `691ba0d1a983`  |
| 2629   | Layout 1 | `691ba0d1a983`  |
| 2619   | Layout 1 | `691ba0d1a983`  |
| 2612   | Layout 1 | `691ba0d1a983`  |
| 2606   | Layout 1 | `691ba0d1a983`  |
| 2602   | Layout 1 | `691ba0d1a983`  |
| 2601   | Layout 1 | `691ba0d1a983`  |
| 2592   | Layout 1 | `691ba0d1a983`  |
| 2583   | Layout 1 | `691ba0d1a983`  |
| 2575   | Layout 1 | `691ba0d1a983`  |
| 2567   | Layout 1 | `691ba0d1a983`  |
| 2560   | Layout 1 | `691ba0d1a983`  |
| 2553   | Layout 1 | `691ba0d1a983`  |
| 2545   | Layout 1 | `691ba0d1a983`  |
| 2538   | Layout 1 | `691ba0d1a983`  |
| 2529   | Layout 1 | `691ba0d1a983`  |
| 2519   | Layout 1 | `691ba0d1a983`  |
| 2513   | Layout 1 | `691ba0d1a983`  |
| 2510   | Layout 1 | `691ba0d1a983`  |
| 2507   | Layout 1 | `691ba0d1a983`  |
| 2503   | Layout 1 | `691ba0d1a983`  |
| 2498   | Layout 1 | `691ba0d1a983`  |
| 2492   | Layout 1 | `691ba0d1a983`  |
| 2487   | Layout 1 | `691ba0d1a983`  |
| 2480   | Layout 1 | `691ba0d1a983`  |
| 2474   | Layout 1 | `691ba0d1a983`  |
| 2468   | Layout 1 | `691ba0d1a983`  |
| 2460   | Layout 1 | `691ba0d1a983`  |
| 2453   | Layout 1 | `691ba0d1a983`  |
| 2444   | Layout 1 | `691ba0d1a983`  |
| 2438   | Layout 1 | `691ba0d1a983`  |
| 2434   | Layout 1 | `691ba0d1a983`  |
| 2429   | Layout 1 | `691ba0d1a983`  |
| 2421   | Layout 1 | `691ba0d1a983`  |
| 2414   | Layout 1 | `691ba0d1a983`  |
| 2407   | Layout 1 | `691ba0d1a983`  |
| 2401   | Layout 1 | `691ba0d1a983`  |
| 2397   | Layout 1 | `691ba0d1a983`  |
| 2393   | Layout 1 | `691ba0d1a983`  |
| 2384   | Layout 1 | `691ba0d1a983`  |
| 2378   | Layout 1 | `691ba0d1a983`  |
| 2372   | Layout 1 | `691ba0d1a983`  |
| 2358   | Layout 1 | `691ba0d1a983`  |
| 2352   | Layout 1 | `691ba0d1a983`  |
| 2347   | Layout 1 | `691ba0d1a983`  |
| 2343   | Layout 1 | `691ba0d1a983`  |
| 2335   | Layout 1 | `691ba0d1a983`  |
| 2327   | Layout 1 | `691ba0d1a983`  |
| 2324   | Layout 1 | `691ba0d1a983`  |
| 2319   | Layout 1 | `691ba0d1a983`  |
| 2313   | Layout 1 | `691ba0d1a983`  |
| 2308   | Layout 1 | `691ba0d1a983`  |
| 2302   | Layout 1 | `691ba0d1a983`  |
| 2295   | Layout 1 | `691ba0d1a983`  |
| 2290   | Layout 1 | `691ba0d1a983`  |
| 2284   | Layout 1 | `691ba0d1a983`  |
| 2276   | Layout 1 | `691ba0d1a983`  |
| 2269   | Layout 1 | `691ba0d1a983`  |
| 2259   | Layout 1 | `691ba0d1a983`  |
| 2250   | Layout 1 | `691ba0d1a983`  |
| 2243   | Layout 1 | `691ba0d1a983`  |
| 2235   | Layout 1 | `691ba0d1a983`  |
| 2229   | Layout 1 | `691ba0d1a983`  |
| 2224   | Layout 1 | `691ba0d1a983`  |
| 2218   | Layout 1 | `691ba0d1a983`  |
| 2215   | Layout 1 | `691ba0d1a983`  |
| 2207   | Layout 1 | `691ba0d1a983`  |
| 2203   | Layout 1 | `691ba0d1a983`  |
| 2196   | Layout 1 | `691ba0d1a983`  |
| 2192   | Layout 1 | `691ba0d1a983`  |
| 2189   | Layout 1 | `691ba0d1a983`  |
| 2183   | Layout 1 | `691ba0d1a983`  |
| 2179   | Layout 1 | `691ba0d1a983`  |
| 2171   | Layout 1 | `691ba0d1a983`  |
| 2163   | Layout 1 | `691ba0d1a983`  |
| 2156   | Layout 1 | `691ba0d1a983`  |
| 2151   | Layout 1 | `691ba0d1a983`  |
| 2147   | Layout 1 | `691ba0d1a983`  |
| 2142   | Layout 1 | `691ba0d1a983`  |
| 2138   | Layout 1 | `691ba0d1a983`  |
| 2134   | Layout 1 | `691ba0d1a983`  |
| 2130   | Layout 1 | `691ba0d1a983`  |
| 2122   | Layout 1 | `691ba0d1a983`  |
| 2107   | Layout 1 | `691ba0d1a983`  |
| 2098   | Layout 1 | `691ba0d1a983`  |
| 2089   | Layout 1 | `691ba0d1a983`  |
| 2081   | Layout 1 | `691ba0d1a983`  |
| 2073   | Layout 1 | `691ba0d1a983`  |
| 2067   | Layout 1 | `691ba0d1a983`  |
| 2063   | Layout 1 | `691ba0d1a983`  |
| 2059   | Layout 1 | `691ba0d1a983`  |
| 2052   | Layout 1 | `691ba0d1a983`  |
| 2044   | Layout 1 | `691ba0d1a983`  |
| 2039   | Layout 1 | `691ba0d1a983`  |
| 2032   | Layout 1 | `691ba0d1a983`  |
| 2025   | Layout 1 | `691ba0d1a983`  |
| 2011   | Layout 1 | `691ba0d1a983`  |
| 2005   | Layout 1 | `691ba0d1a983`  |
| 2000   | Layout 1 | `691ba0d1a983`  |
| 1996   | Layout 1 | `691ba0d1a983`  |
| 1991   | Layout 1 | `691ba0d1a983`  |
| 1985   | Layout 1 | `691ba0d1a983`  |
| 1980   | Layout 1 | `691ba0d1a983`  |
| 1969   | Layout 1 | `691ba0d1a983`  |
| 1964   | Layout 1 | `691ba0d1a983`  |
| 1958   | Layout 1 | `691ba0d1a983`  |
| 1950   | Layout 1 | `691ba0d1a983`  |
| 1945   | Layout 1 | `691ba0d1a983`  |
| 1937   | Layout 1 | `691ba0d1a983`  |
| 1933   | Layout 1 | `691ba0d1a983`  |
| 1927   | Layout 1 | `691ba0d1a983`  |
| 1921   | Layout 1 | `691ba0d1a983`  |
| 1914   | Layout 1 | `691ba0d1a983`  |
| 1908   | Layout 1 | `691ba0d1a983`  |
| 1897   | Layout 1 | `691ba0d1a983`  |
| 1892   | Layout 1 | `691ba0d1a983`  |
| 1886   | Layout 1 | `691ba0d1a983`  |
| 1881   | Layout 1 | `691ba0d1a983`  |
| 1871   | Layout 1 | `691ba0d1a983`  |
| 1866   | Layout 1 | `691ba0d1a983`  |
| 1862   | No file  | `691ba0d1a983`  |
| 1854   | No file  | `691ba0d1a983`  |
| 1846   | No file  | `691ba0d1a983`  |
| 1838   | No file  | `691ba0d1a983`  |
| 1832   | No file  | `691ba0d1a983`  |
| 1826   | No file  | `691ba0d1a983`  |
| 1822   | No file  | `691ba0d1a983`  |
| 1818   | No file  | `691ba0d1a983`  |
| 1804   | No file  | `691ba0d1a983`  |
| 1794   | No file  | `691ba0d1a983`  |
| 1790   | No file  | `691ba0d1a983`  |
| 1784   | No file  | `691ba0d1a983`  |
| 1774   | No file  | `691ba0d1a983`  |
| 1771   | No file  | `691ba0d1a983`  |
| 1762   | No file  | `691ba0d1a983`  |
| 1759   | No file  | `691ba0d1a983`  |
| 1754   | No file  | `691ba0d1a983`  |
| 1749   | No file  | `691ba0d1a983`  |
| 1743   | No file  | `691ba0d1a983`  |
| 1737   | No file  | `691ba0d1a983`  |
| 1731   | No file  | `691ba0d1a983`  |
| 1725   | No file  | `691ba0d1a983`  |
| 1717   | No file  | `691ba0d1a983`  |
| 1710   | No file  | `691ba0d1a983`  |
| 1704   | No file  | `691ba0d1a983`  |
| 1698   | No file  | `691ba0d1a983`  |
| 1690   | No file  | `691ba0d1a983`  |
| 1685   | No file  | `691ba0d1a983`  |
| 1680   | No file  | `691ba0d1a983`  |
| 1674   | No file  | `691ba0d1a983`  |
| 1668   | No file  | `691ba0d1a983`  |
| 1659   | No file  | `691ba0d1a983`  |
| 1649   | No file  | `691ba0d1a983`  |
| 1642   | No file  | `691ba0d1a983`  |
| 1636   | No file  | `691ba0d1a983`  |
| 1628   | No file  | `691ba0d1a983`  |
| 1622   | No file  | `691ba0d1a983`  |
| 1614   | No file  | `691ba0d1a983`  |
| 1608   | No file  | `691ba0d1a983`  |
| 1602   | No file  | `691ba0d1a983`  |
| 1598   | No file  | `691ba0d1a983`  |
| 1594   | No file  | `691ba0d1a983`  |
| 1590   | No file  | `691ba0d1a983`  |
| 1587   | No file  | `691ba0d1a983`  |
| 1584   | No file  | `691ba0d1a983`  |
| 1579   | No file  | `691ba0d1a983`  |
| 1572   | No file  | `691ba0d1a983`  |
| 1565   | No file  | `691ba0d1a983`  |
| 1559   | No file  | `691ba0d1a983`  |
| 1554   | No file  | `691ba0d1a983`  |
| 1547   | No file  | `691ba0d1a983`  |
| 1537   | No file  | `691ba0d1a983`  |
| 1529   | No file  | `691ba0d1a983`  |
| 1524   | No file  | `691ba0d1a983`  |
| 1519   | No file  | `691ba0d1a983`  |
| 1509   | No file  | `691ba0d1a983`  |
| 1506   | No file  | `691ba0d1a983`  |
| 1504   | No file  | `691ba0d1a983`  |
| 1500   | No file  | `691ba0d1a983`  |
| 1493   | No file  | `691ba0d1a983`  |
| 1489   | No file  | `691ba0d1a983`  |
| 1485   | No file  | `691ba0d1a983`  |
| 1481   | No file  | `691ba0d1a983`  |
| 1474   | No file  | `691ba0d1a983`  |
| 1466   | No file  | `691ba0d1a983`  |
| 1462   | No file  | `691ba0d1a983`  |
| 1459   | No file  | `691ba0d1a983`  |
| 1453   | No file  | `691ba0d1a983`  |
| 1450   | No file  | `691ba0d1a983`  |
| 1445   | No file  | `691ba0d1a983`  |
| 1439   | No file  | `691ba0d1a983`  |
| 1433   | No file  | `691ba0d1a983`  |
| 1430   | No file  | `691ba0d1a983`  |
| 1426   | No file  | `691ba0d1a983`  |
| 1421   | No file  | `691ba0d1a983`  |
| 1417   | No file  | `691ba0d1a983`  |
| 1416   | No file  | `691ba0d1a983`  |
| 1409   | No file  | `691ba0d1a983`  |
| 1405   | No file  | `691ba0d1a983`  |
| 1401   | No file  | `691ba0d1a983`  |
| 1396   | No file  | `691ba0d1a983`  |
| 1391   | No file  | `691ba0d1a983`  |
| 1390   | No file  | `691ba0d1a983`  |
| 1386   | No file  | `691ba0d1a983`  |
| 1381   | No file  | `691ba0d1a983`  |
| 1379   | No file  | `691ba0d1a983`  |
| 1372   | No file  | `691ba0d1a983`  |
| 1366   | No file  | `691ba0d1a983`  |
| 1364   | No file  | `691ba0d1a983`  |
| 1363   | No file  | `691ba0d1a983`  |
| 1360   | No file  | `691ba0d1a983`  |
| 1358   | No file  | `691ba0d1a983`  |
| 1355   | No file  | `691ba0d1a983`  |
| 1351   | No file  | `691ba0d1a983`  |
| 1348   | No file  | `691ba0d1a983`  |
| 1346   | No file  | `691ba0d1a983`  |
| 1341   | No file  | `691ba0d1a983`  |
| 1340   | No file  | `691ba0d1a983`  |
| 1338   | No file  | `691ba0d1a983`  |
| 1335   | No file  | `691ba0d1a983`  |
| 1333   | No file  | `691ba0d1a983`  |
| 1329   | No file  | `691ba0d1a983`  |
| 1327   | No file  | `691ba0d1a983`  |
| 1324   | No file  | `691ba0d1a983`  |
| 1321   | No file  | `691ba0d1a983`  |
| 1319   | No file  | `691ba0d1a983`  |
| 1318   | No file  | `691ba0d1a983`  |
| 1316   | No file  | `691ba0d1a983`  |
| 1313   | No file  | `691ba0d1a983`  |
| 1311   | No file  | `691ba0d1a983`  |
| 1309   | No file  | `691ba0d1a983`  |
| 1304   | No file  | `691ba0d1a983`  |
| 1292   | No file  | `691ba0d1a983`  |
| 1286   | No file  | `691ba0d1a983`  |
| 1280   | No file  | `691ba0d1a983`  |
| 1276   | No file  | `691ba0d1a983`  |
| 1267   | No file  | `691ba0d1a983`  |
| 1261   | No file  | `691ba0d1a983`  |
| 1256   | No file  | `691ba0d1a983`  |
| 1250   | No file  | `691ba0d1a983`  |
| 1246   | No file  | `691ba0d1a983`  |
| 1239   | No file  | `691ba0d1a983`  |
| 1230   | No file  | `691ba0d1a983`  |
| 1226   | No file  | `691ba0d1a983`  |
| 1220   | No file  | `691ba0d1a983`  |
| 1217   | No file  | `691ba0d1a983`  |
| 1211   | No file  | `691ba0d1a983`  |
| 1210   | No file  | `691ba0d1a983`  |
| 1208   | No file  | `691ba0d1a983`  |
| 1203   | No file  | `691ba0d1a983`  |
| 1197   | No file  | `691ba0d1a983`  |
| 1194   | No file  | `691ba0d1a983`  |
| 1192   | No file  | `691ba0d1a983`  |
| 1187   | No file  | `691ba0d1a983`  |
| 1183   | No file  | `691ba0d1a983`  |
| 1177   | No file  | `691ba0d1a983`  |
| 1173   | No file  | `691ba0d1a983`  |
| 1167   | No file  | `691ba0d1a983`  |
| 1164   | No file  | `691ba0d1a983`  |
| 1156   | No file  | `691ba0d1a983`  |
| 1149   | No file  | `691ba0d1a983`  |
| 1144   | No file  | `691ba0d1a983`  |
| 1137   | No file  | `691ba0d1a983`  |
| 1132   | No file  | `691ba0d1a983`  |
| 1127   | No file  | `691ba0d1a983`  |
| 1122   | No file  | `691ba0d1a983`  |
| 1118   | No file  | `691ba0d1a983`  |
| 1114   | No file  | `691ba0d1a983`  |
| 1109   | No file  | `691ba0d1a983`  |
| 1102   | No file  | `691ba0d1a983`  |
| 1096   | No file  | `691ba0d1a983`  |
| 1088   | No file  | `691ba0d1a983`  |
| 1081   | No file  | `691ba0d1a983`  |
| 1076   | No file  | `691ba0d1a983`  |
| 1069   | No file  | `691ba0d1a983`  |
| 1064   | No file  | `691ba0d1a983`  |
| 1058   | No file  | `691ba0d1a983`  |
| 1051   | No file  | `691ba0d1a983`  |
| 1044   | No file  | `691ba0d1a983`  |
| 1036   | No file  | `691ba0d1a983`  |
| 1026   | No file  | `691ba0d1a983`  |
| 1016   | No file  | `691ba0d1a983`  |
| 1009   | No file  | `691ba0d1a983`  |
| 1005   | No file  | `691ba0d1a983`  |
| 1000   | No file  | `691ba0d1a983`  |
| 998    | No file  | `691ba0d1a983`  |
| 990    | No file  | `691ba0d1a983`  |
| 979    | No file  | `691ba0d1a983`  |
| 972    | No file  | `691ba0d1a983`  |
| 963    | No file  | `691ba0d1a983`  |
| 955    | No file  | `691ba0d1a983`  |
| 946    | No file  | `691ba0d1a983`  |
| 938    | No file  | `691ba0d1a983`  |
| 927    | No file  | `691ba0d1a983`  |
| 911    | No file  | `691ba0d1a983`  |
| 904    | No file  | `691ba0d1a983`  |
| 899    | No file  | `691ba0d1a983`  |
| 894    | No file  | `691ba0d1a983`  |
| 885    | No file  | `691ba0d1a983`  |
| 879    | No file  | `691ba0d1a983`  |
| 872    | No file  | `691ba0d1a983`  |
| 864    | No file  | `691ba0d1a983`  |
| 855    | No file  | `691ba0d1a983`  |
| 853    | No file  | `691ba0d1a983`  |
| 845    | No file  | `691ba0d1a983`  |
| 837    | No file  | `691ba0d1a983`  |
| 829    | No file  | `691ba0d1a983`  |
| 822    | No file  | `691ba0d1a983`  |
| 814    | No file  | `691ba0d1a983`  |
| 805    | No file  | `691ba0d1a983`  |
| 794    | No file  | `691ba0d1a983`  |
| 787    | No file  | `691ba0d1a983`  |
| 780    | No file  | `691ba0d1a983`  |
| 771    | No file  | `691ba0d1a983`  |
| 760    | No file  | `691ba0d1a983`  |
| 748    | No file  | `691ba0d1a983`  |
| 741    | No file  | `691ba0d1a983`  |
| 736    | No file  | `691ba0d1a983`  |
| 731    | No file  | `691ba0d1a983`  |
| 723    | No file  | `691ba0d1a983`  |
| 711    | No file  | `691ba0d1a983`  |
| 707    | No file  | `691ba0d1a983`  |
| 697    | No file  | `691ba0d1a983`  |
| 689    | No file  | `691ba0d1a983`  |
| 683    | No file  | `691ba0d1a983`  |
| 678    | No file  | `691ba0d1a983`  |
| 670    | No file  | `691ba0d1a983`  |
| 661    | No file  | `691ba0d1a983`  |
| 656    | No file  | `691ba0d1a983`  |
| 652    | No file  | `691ba0d1a983`  |
| 643    | No file  | `691ba0d1a983`  |
| 637    | No file  | `691ba0d1a983`  |
| 630    | No file  | `691ba0d1a983`  |
| 627    | No file  | `691ba0d1a983`  |
| 621    | No file  | `691ba0d1a983`  |
| 617    | No file  | `691ba0d1a983`  |
| 615    | No file  | `691ba0d1a983`  |
| 606    | No file  | `691ba0d1a983`  |
| 599    | No file  | `691ba0d1a983`  |
| 592    | No file  | `691ba0d1a983`  |
| 586    | No file  | `691ba0d1a983`  |
| 577    | No file  | `691ba0d1a983`  |
| 569    | No file  | `691ba0d1a983`  |
| 561    | No file  | `691ba0d1a983`  |
| 554    | No file  | `691ba0d1a983`  |
| 542    | No file  | `691ba0d1a983`  |
| 532    | No file  | `691ba0d1a983`  |
| 531    | No file  | `691ba0d1a983`  |
| 526    | No file  | `691ba0d1a983`  |
| 521    | No file  | `691ba0d1a983`  |
| 517    | No file  | `691ba0d1a983`  |
| 510    | No file  | `691ba0d1a983`  |
| 508    | No file  | `691ba0d1a983`  |
| 504    | No file  | `691ba0d1a983`  |
| 497    | No file  | `691ba0d1a983`  |
| 491    | No file  | `691ba0d1a983`  |
| 485    | No file  | `691ba0d1a983`  |
| 478    | No file  | `691ba0d1a983`  |
| 472    | No file  | `691ba0d1a983`  |
| 466    | No file  | `691ba0d1a983`  |
| 457    | No file  | `691ba0d1a983`  |
| 452    | No file  | `691ba0d1a983`  |
| 449    | No file  | `691ba0d1a983`  |
| 435    | No file  | `691ba0d1a983`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                                                         |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------------------------ |
| `sequencetriggerdata.bss` | Optional | For `sequencetutorial_equipment.bss`: the sequence folder and file name by hash ([format](sequencetriggerdata_bss.md)) |
| `languagedata_*.loc`      | Optional | Class names (type `21`) and item names (type `0`), else the Korean item name                                 |

`sequencetutorial_equipment.bss` shows a Sequence File column next to
the stored name: the folder and file name of the `sequencetriggerdata.bss`
row with the same `file_name_hash`, joined with `/`
(`IllezraTutorial/CS_Tutorial_Illezra_00` for `CS_Tutorial_Illezra_00.pas`).
A hash the trigger table does not hold, or a trigger table the handler
cannot read, leaves the column empty. Cutscenes have no trigger row, so
`cutscenetutorial_equipment.bss` reads no companion. The names stay
names: the `.pas` cutscenes and the `sequence/` files have no handler.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of rows                                |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (variable: 12 bytes + class entries)

| Offset  | Type                          | Field              | Notes                                                                                               |
| ------- | ----------------------------- | ------------------ | --------------------------------------------------------------------------------------------------- |
| `+0x00` | u32                           | file_name_hash     | ASCII key hash (lookup3, seed `0xC5EDE`) of `cutscene_file_name` without `.pas`; matches on every row |
| `+0x04` | u32                           | cutscene_file_name | Index into `strings`: the sequence or cutscene file with `.pas`; unique                             |
| `+0x08` | u32                           | class_count        | Number of `classes`                                                                                 |
| `+0x0C` | Class Equipment[class_count]  | classes            | See Class Equipment                                                                                 |

### Class Equipment (25 bytes)

| Offset  | Type | Field               | Notes                                                    |
| ------- | ---- | ------------------- | -------------------------------------------------------- |
| `+0x00` | u8   | class_type          | Class type (`0` Warrior, LOC type 21); once per row      |
| `+0x01` | u32  | main_weapon_item_id | Item ID of the main weapon costume; `0` for none         |
| `+0x05` | u32  | sub_weapon_item_id  | Item ID of the sub-weapon costume; `0` for none          |
| `+0x09` | u32  | helmet_item_id      | Item ID of the helmet costume; `0` for none              |
| `+0x0D` | u32  | armor_item_id       | Item ID of the armor costume; `0` for none               |
| `+0x11` | u32  | gloves_item_id      | Item ID of the gloves costume; `0` for none              |
| `+0x15` | u32  | shoes_item_id       | Item ID of the shoes costume; `0` for none               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                         |
| `+0x04` | pstr[string_count] | strings      | UTF-8 file names, one per row             |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
these tables, and neither file is in that client. The slot names come
from the items: on client 3482 the 32 `main_weapon_item_id` items are
main weapons (Longsword, Shamshir, Kyve), the 32 `sub_weapon_item_id`
items sub-weapons (Shield, Haladie, Dagger), and the helmet, armor,
gloves and shoes fields hold only items of that piece (Helmet, Headpiece
or Hat; Armor, Clothes or Robe; Gloves; Shoes), counted over both files.
Each item's `[Class]` name prefix matches the LOC type 21 name of the
entry's `class_type`; only the two development items below have no
prefix.

## Notes

- On client 3482 `sequencetutorial_equipment.bss` has 4 rows and
  `cutscenetutorial_equipment.bss` 11, each with the same 32 class types
  (`0` to `35` without `13`, `14`, `18` and `22`).
- Rows of one story share their outfits: the two Illezra sequences, and
  the three Illezra cutscenes, hold one costume set per class, the two
  Olvia Academy sequences (`CS_OVAC_*`) the Academia set with no weapons.
  The 8 `CS_Yolunakea_*` rows differ from the Illezra cutscenes only in
  class type `2` (Sage): no weapons, the armor `830046` on all 8 and the
  helmet `830049` on 5. Neither item has a LOC name; the item table names
  them 개발용 갑옷 and 개발용 투구 (development armor, development helmet).
- On client 3482 all 4 `sequencetutorial_equipment.bss` rows key a
  `sequencetriggerdata.bss` sequence of the same name
  (`IllezraTutorial/CS_Tutorial_Illezra_00`, `IllezraTutorial/CS_Tutorial_Illezra_01`,
  `OVAC/CS_OVAC_03_Admission`, `OVAC/CS_OVAC_04_Graduation`). The stored
  name ends in `.pas` although the sequence file under `sequence/` is a
  `.paseqfe`.
- The `sequence_skill.bss` and `cutscene_skill.bss` rows key the same
  files by `file_name_hash` alone. Their handler takes the cutscene names
  from `cutscenetutorial_equipment.bss` and the sequence names from
  `sequencetriggerdata.bss`.

## Open Questions

### When the Client Puts the Costumes On

The client Lua names neither file and no call that reads them. Whether
the costumes replace the player's own outfit only while the sequence or
cutscene plays, or also stay on after it, is open.
