# `petequipskill.bss` Format

## Purpose

Defines two pet skill catalogs, both keyed by `equip_skill_id`. 116 skill entries span two sections: Section 1 (the equip skills a pet rolls, IDs 0–42) and Section 2 (the base skills, IDs 15–111, keyed by `base_skill_id` in [pet.dbss](pet_dbss.md)). Each entry records the skill's type group, an unknown byte (`unknown_08`), and a localization ID that resolves to the in-game skill name and pet equip-skill icon number.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes | Records                  | Row bytes               |
| ------ | -------------- | ------------------- | ----- | ------------------------ | ----------------------- |
| 2      | 1921 and later | `petequipskill.bss` | 3,772 | 43 Equip Skill, 200 Slot | 16 to 20, 16 on average |
| 1      | 805 to 1914    | `petequipskill.bss` | 2,164 | 43 Equip Skill, 136 Slot | 12                      |

| Layout | File                | Known            | Unknown       |
| ------ | ------------------- | ---------------- | ------------- |
| 2      | `petequipskill.bss` | 2,932 B (77.7%)  | 840 B (22.3%) |
| 1      | `petequipskill.bss` | 2,164 B (100.0%) | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `ad4916824c2a`  |
| 3482   | Layout 2             | `ad4916824c2a`  |
| 3474   | Layout 2             | `ad4916824c2a`  |
| 3473   | Layout 2             | `ad4916824c2a`  |
| 3464   | Layout 2             | `ad4916824c2a`  |
| 3458   | Layout 2             | `ad4916824c2a`  |
| 3454   | Layout 2             | `ad4916824c2a`  |
| 3444   | Layout 2             | `ad4916824c2a`  |
| 3435   | Layout 2             | `ad4916824c2a`  |
| 3426   | Layout 2             | `ad4916824c2a`  |
| 3418   | Layout 2             | `ad4916824c2a`  |
| 3412   | Layout 2             | `ad4916824c2a`  |
| 3402   | Layout 2             | `ad4916824c2a`  |
| 3396   | Layout 2             | `ad4916824c2a`  |
| 3387   | Layout 2             | `ad4916824c2a`  |
| 3381   | Layout 2             | `ad4916824c2a`  |
| 3373   | Layout 2             | `ad4916824c2a`  |
| 3364   | Layout 2             | `ad4916824c2a`  |
| 3356   | Layout 2             | `ad4916824c2a`  |
| 3349   | Layout 2             | `ad4916824c2a`  |
| 3342   | Layout 2             | `ad4916824c2a`  |
| 3335   | Layout 2             | `ad4916824c2a`  |
| 3326   | Layout 2             | `ad4916824c2a`  |
| 3321   | Layout 2             | `ad4916824c2a`  |
| 3314   | Layout 2             | `ad4916824c2a`  |
| 3303   | Layout 2             | `ad4916824c2a`  |
| 3302   | Layout 2             | `ad4916824c2a`  |
| 3293   | Layout 2             | `ad4916824c2a`  |
| 3283   | Layout 2             | `ad4916824c2a`  |
| 3275   | Layout 2             | `ad4916824c2a`  |
| 3267   | Layout 2             | `ad4916824c2a`  |
| 3258   | Layout 2             | `ad4916824c2a`  |
| 3251   | Layout 2             | `ad4916824c2a`  |
| 3242   | Layout 2             | `ad4916824c2a`  |
| 3235   | Layout 2             | `ad4916824c2a`  |
| 3229   | Layout 2             | `ad4916824c2a`  |
| 3212   | Layout 2             | `ad4916824c2a`  |
| 3203   | Layout 2             | `ad4916824c2a`  |
| 3193   | Layout 2             | `ad4916824c2a`  |
| 3186   | Layout 2             | `ad4916824c2a`  |
| 3177   | Layout 2             | `ad4916824c2a`  |
| 3169   | Layout 2             | `ad4916824c2a`  |
| 3158   | Layout 2             | `ad4916824c2a`  |
| 3151   | Layout 2             | `ad4916824c2a`  |
| 3144   | Layout 2             | `ad4916824c2a`  |
| 3133   | Layout 2             | `ad4916824c2a`  |
| 3125   | Layout 2             | `ad4916824c2a`  |
| 3118   | Layout 2             | `ad4916824c2a`  |
| 3111   | Layout 2             | `ad4916824c2a`  |
| 3103   | Layout 2             | `ad4916824c2a`  |
| 3095   | Layout 2             | `ad4916824c2a`  |
| 3086   | Layout 2             | `ad4916824c2a`  |
| 3072   | Layout 2             | `ad4916824c2a`  |
| 3062   | Layout 2             | `ad4916824c2a`  |
| 3052   | Layout 2             | `ad4916824c2a`  |
| 3045   | Layout 2             | `ad4916824c2a`  |
| 3037   | Layout 2             | `ad4916824c2a`  |
| 3030   | Layout 2             | `ad4916824c2a`  |
| 3021   | Layout 2             | `ad4916824c2a`  |
| 3012   | Layout 2             | `ad4916824c2a`  |
| 3002   | Layout 2             | `ad4916824c2a`  |
| 2995   | Layout 2             | `ad4916824c2a`  |
| 2987   | Layout 2             | `ad4916824c2a`  |
| 2978   | Layout 2             | `ad4916824c2a`  |
| 2970   | Layout 2             | `ad4916824c2a`  |
| 2959   | Layout 2             | `ad4916824c2a`  |
| 2951   | Layout 2             | `ad4916824c2a`  |
| 2942   | Layout 2             | `ad4916824c2a`  |
| 2935   | Layout 2             | `ad4916824c2a`  |
| 2932   | Layout 2             | `ad4916824c2a`  |
| 2923   | Layout 2             | `ad4916824c2a`  |
| 2919   | Layout 2             | `ad4916824c2a`  |
| 2907   | Layout 2             | `ad4916824c2a`  |
| 2900   | Layout 2             | `ad4916824c2a`  |
| 2891   | Layout 2             | `ad4916824c2a`  |
| 2882   | Layout 2             | `ad4916824c2a`  |
| 2872   | Layout 2             | `ad4916824c2a`  |
| 2863   | Layout 2             | `ad4916824c2a`  |
| 2855   | Layout 2             | `ad4916824c2a`  |
| 2849   | Layout 2             | `ad4916824c2a`  |
| 2844   | Layout 2             | `ad4916824c2a`  |
| 2834   | Layout 2             | `ad4916824c2a`  |
| 2825   | Layout 2             | `ad4916824c2a`  |
| 2819   | Layout 2             | `ad4916824c2a`  |
| 2811   | Layout 2             | `ad4916824c2a`  |
| 2803   | Layout 2             | `ad4916824c2a`  |
| 2794   | Layout 2             | `ad4916824c2a`  |
| 2783   | Layout 2             | `ad4916824c2a`  |
| 2774   | Layout 2             | `ad4916824c2a`  |
| 2765   | Layout 2             | `ad4916824c2a`  |
| 2756   | Layout 2             | `ad4916824c2a`  |
| 2750   | Layout 2             | `ad4916824c2a`  |
| 2743   | Layout 2             | `ad4916824c2a`  |
| 2736   | Layout 2             | `ad4916824c2a`  |
| 2726   | Layout 2             | `ad4916824c2a`  |
| 2717   | Layout 2             | `ad4916824c2a`  |
| 2709   | Layout 2             | `ad4916824c2a`  |
| 2703   | Layout 2             | `ad4916824c2a`  |
| 2695   | Layout 2             | `ad4916824c2a`  |
| 2684   | Layout 2             | `ad4916824c2a`  |
| 2672   | Layout 2             | `ad4916824c2a`  |
| 2665   | Layout 2             | `ad4916824c2a`  |
| 2657   | Layout 2             | `ad4916824c2a`  |
| 2649   | Layout 2             | `ad4916824c2a`  |
| 2644   | Layout 2             | `ad4916824c2a`  |
| 2637   | Layout 2             | `ad4916824c2a`  |
| 2629   | Layout 2             | `ad4916824c2a`  |
| 2619   | Layout 2             | `ad4916824c2a`  |
| 2612   | Layout 2             | `ad4916824c2a`  |
| 2606   | Layout 2             | `ad4916824c2a`  |
| 2602   | Layout 2             | `ad4916824c2a`  |
| 2601   | Layout 2             | `ad4916824c2a`  |
| 2592   | Layout 2             | `ad4916824c2a`  |
| 2583   | Layout 2             | `ad4916824c2a`  |
| 2575   | Layout 2             | `ad4916824c2a`  |
| 2567   | Layout 2             | `ad4916824c2a`  |
| 2560   | Layout 2             | `ad4916824c2a`  |
| 2553   | Layout 2             | `ad4916824c2a`  |
| 2545   | Layout 2             | `ad4916824c2a`  |
| 2538   | Layout 2             | `ad4916824c2a`  |
| 2529   | Layout 2             | `ad4916824c2a`  |
| 2519   | Layout 2             | `ad4916824c2a`  |
| 2513   | Layout 2             | `ad4916824c2a`  |
| 2510   | Layout 2             | `ad4916824c2a`  |
| 2507   | Layout 2             | `ad4916824c2a`  |
| 2503   | Layout 2             | `ad4916824c2a`  |
| 2498   | Layout 2             | `ad4916824c2a`  |
| 2492   | Layout 2             | `ad4916824c2a`  |
| 2487   | Layout 2             | `ad4916824c2a`  |
| 2480   | Layout 2             | `ad4916824c2a`  |
| 2474   | Layout 2             | `ad4916824c2a`  |
| 2468   | Layout 2             | `ad4916824c2a`  |
| 2460   | Layout 2             | `ad4916824c2a`  |
| 2453   | Layout 2             | `ad4916824c2a`  |
| 2444   | Layout 2             | `ad4916824c2a`  |
| 2438   | Layout 2             | `ad4916824c2a`  |
| 2434   | Layout 2             | `ad4916824c2a`  |
| 2429   | Layout 2             | `ad4916824c2a`  |
| 2421   | Layout 2             | `ad4916824c2a`  |
| 2414   | Layout 2             | `ad4916824c2a`  |
| 2407   | Layout 2             | `ad4916824c2a`  |
| 2401   | Layout 2             | `ad4916824c2a`  |
| 2397   | Layout 2             | `ad4916824c2a`  |
| 2393   | Layout 2             | `ad4916824c2a`  |
| 2384   | Layout 2             | `ad4916824c2a`  |
| 2378   | Layout 2             | `ad4916824c2a`  |
| 2372   | Layout 2             | `ad4916824c2a`  |
| 2358   | Layout 2             | `ad4916824c2a`  |
| 2352   | Layout 2             | `ad4916824c2a`  |
| 2347   | Layout 2             | `ad4916824c2a`  |
| 2343   | Layout 2             | `ad4916824c2a`  |
| 2335   | Layout 2             | `ad4916824c2a`  |
| 2327   | Layout 2             | `ad4916824c2a`  |
| 2324   | Layout 2             | `ad4916824c2a`  |
| 2319   | Layout 2             | `ad4916824c2a`  |
| 2313   | Layout 2             | `ad4916824c2a`  |
| 2308   | Layout 2             | `ad4916824c2a`  |
| 2302   | Layout 2             | `ad4916824c2a`  |
| 2295   | Layout 2             | `ad4916824c2a`  |
| 2290   | Layout 2             | `ad4916824c2a`  |
| 2284   | Layout 2             | `ad4916824c2a`  |
| 2276   | Layout 2             | `ad4916824c2a`  |
| 2269   | Layout 2             | `ad4916824c2a`  |
| 2259   | Layout 2             | `ad4916824c2a`  |
| 2250   | Layout 2             | `ad4916824c2a`  |
| 2243   | Layout 2             | `ad4916824c2a`  |
| 2235   | Layout 2             | `ad4916824c2a`  |
| 2229   | Layout 2             | `ad4916824c2a`  |
| 2224   | Layout 2             | `ad4916824c2a`  |
| 2218   | Layout 2             | `ad4916824c2a`  |
| 2215   | Layout 2             | `ad4916824c2a`  |
| 2207   | Layout 2             | `ad4916824c2a`  |
| 2203   | Layout 2             | `ad4916824c2a`  |
| 2196   | Layout 2             | `ad4916824c2a`  |
| 2192   | Layout 2             | `ad4916824c2a`  |
| 2189   | Layout 2             | `ad4916824c2a`  |
| 2183   | Layout 2             | `ad4916824c2a`  |
| 2179   | Layout 2             | `ad4916824c2a`  |
| 2171   | Layout 2             | `ad4916824c2a`  |
| 2163   | Layout 2             | `ad4916824c2a`  |
| 2156   | Layout 2             | `ad4916824c2a`  |
| 2151   | Layout 2             | `ad4916824c2a`  |
| 2147   | Layout 2             | `ad4916824c2a`  |
| 2142   | Layout 2             | `ad4916824c2a`  |
| 2138   | Layout 2             | `ad4916824c2a`  |
| 2134   | Layout 2             | `ad4916824c2a`  |
| 2130   | Layout 2             | `ad4916824c2a`  |
| 2122   | Layout 2             | `ad4916824c2a`  |
| 2107   | Layout 2             | `ad4916824c2a`  |
| 2098   | Layout 2             | `ad4916824c2a`  |
| 2089   | Layout 2             | `ad4916824c2a`  |
| 2081   | Layout 2             | `ad4916824c2a`  |
| 2073   | Layout 2             | `ad4916824c2a`  |
| 2067   | Layout 2             | `ad4916824c2a`  |
| 2063   | Layout 2             | `ad4916824c2a`  |
| 2059   | Layout 2             | `ad4916824c2a`  |
| 2052   | Layout 2             | `ad4916824c2a`  |
| 2044   | Layout 2             | `ad4916824c2a`  |
| 2039   | Layout 2             | `ad4916824c2a`  |
| 2032   | Layout 2             | `ad4916824c2a`  |
| 2025   | Layout 2             | `ad4916824c2a`  |
| 2011   | Layout 2             | `ad4916824c2a`  |
| 2005   | Layout 2             | `ad4916824c2a`  |
| 2000   | Layout 2             | `ad4916824c2a`  |
| 1996   | Layout 2             | `ad4916824c2a`  |
| 1991   | Layout 2             | `ad4916824c2a`  |
| 1985   | Layout 2             | `ad4916824c2a`  |
| 1980   | Layout 2             | `ad4916824c2a`  |
| 1969   | Layout 2             | `ad4916824c2a`  |
| 1964   | Layout 2             | `ad4916824c2a`  |
| 1958   | Layout 2             | `ad4916824c2a`  |
| 1950   | Layout 2             | `ad4916824c2a`  |
| 1945   | Layout 2             | `ad4916824c2a`  |
| 1937   | Layout 2             | `ad4916824c2a`  |
| 1933   | Layout 2             | `ad4916824c2a`  |
| 1927   | Layout 2             | `ad4916824c2a`  |
| 1921   | Layout 2             | `ad4916824c2a`  |
| 1914   | Layout 1             | `ad4916824c2a`  |
| 1908   | Layout 1             | `ad4916824c2a`  |
| 1897   | Layout 1             | `ad4916824c2a`  |
| 1892   | Layout 1             | `ad4916824c2a`  |
| 1886   | Layout 1             | `ad4916824c2a`  |
| 1881   | Layout 1             | `ad4916824c2a`  |
| 1871   | Layout 1             | `ad4916824c2a`  |
| 1866   | Layout 1             | `ad4916824c2a`  |
| 1862   | Layout 1             | `ad4916824c2a`  |
| 1854   | Layout 1             | `ad4916824c2a`  |
| 1846   | Layout 1             | `ad4916824c2a`  |
| 1838   | Layout 1             | `ad4916824c2a`  |
| 1832   | Layout 1             | `ad4916824c2a`  |
| 1826   | Layout 1             | `ad4916824c2a`  |
| 1822   | Layout 1             | `ad4916824c2a`  |
| 1818   | Layout 1             | `ad4916824c2a`  |
| 1804   | Layout 1             | `ad4916824c2a`  |
| 1794   | Layout 1             | `ad4916824c2a`  |
| 1790   | Layout 1             | `ad4916824c2a`  |
| 1784   | Layout 1             | `ad4916824c2a`  |
| 1774   | Layout 1             | `ad4916824c2a`  |
| 1771   | Layout 1             | `ad4916824c2a`  |
| 1762   | Layout 1             | `ad4916824c2a`  |
| 1759   | Layout 1             | `ad4916824c2a`  |
| 1754   | Layout 1             | `ad4916824c2a`  |
| 1749   | Layout 1             | `ad4916824c2a`  |
| 1743   | Layout 1             | `ad4916824c2a`  |
| 1737   | Layout 1             | `ad4916824c2a`  |
| 1731   | Layout 1             | `ad4916824c2a`  |
| 1725   | Layout 1             | `ad4916824c2a`  |
| 1717   | Layout 1             | `ad4916824c2a`  |
| 1710   | Layout 1             | `ad4916824c2a`  |
| 1704   | Layout 1             | `ad4916824c2a`  |
| 1698   | Layout 1             | `ad4916824c2a`  |
| 1690   | Layout 1             | `ad4916824c2a`  |
| 1685   | Layout 1             | `ad4916824c2a`  |
| 1680   | Layout 1             | `ad4916824c2a`  |
| 1674   | Layout 1             | `ad4916824c2a`  |
| 1668   | Layout 1             | `ad4916824c2a`  |
| 1659   | Layout 1             | `ad4916824c2a`  |
| 1649   | Layout 1             | `ad4916824c2a`  |
| 1642   | Layout 1             | `ad4916824c2a`  |
| 1636   | Layout 1             | `ad4916824c2a`  |
| 1628   | Layout 1             | `ad4916824c2a`  |
| 1622   | Layout 1             | `ad4916824c2a`  |
| 1614   | Layout 1             | `ad4916824c2a`  |
| 1608   | Layout 1             | `ad4916824c2a`  |
| 1602   | Layout 1             | `ad4916824c2a`  |
| 1598   | Layout 1             | `ad4916824c2a`  |
| 1594   | Layout 1             | `ad4916824c2a`  |
| 1590   | Layout 1             | `ad4916824c2a`  |
| 1587   | Layout 1             | `ad4916824c2a`  |
| 1584   | Layout 1             | `ad4916824c2a`  |
| 1579   | Layout 1             | `ad4916824c2a`  |
| 1572   | Layout 1             | `ad4916824c2a`  |
| 1565   | Layout 1             | `ad4916824c2a`  |
| 1559   | Layout 1             | `ad4916824c2a`  |
| 1554   | Layout 1             | `ad4916824c2a`  |
| 1547   | Layout 1             | `ad4916824c2a`  |
| 1537   | Layout 1             | `ad4916824c2a`  |
| 1529   | Layout 1             | `ad4916824c2a`  |
| 1524   | Layout 1             | `ad4916824c2a`  |
| 1519   | Layout 1             | `ad4916824c2a`  |
| 1509   | Layout 1             | `ad4916824c2a`  |
| 1506   | Layout 1             | `ad4916824c2a`  |
| 1504   | Layout 1             | `ad4916824c2a`  |
| 1500   | Layout 1             | `ad4916824c2a`  |
| 1493   | Layout 1             | `ad4916824c2a`  |
| 1489   | Layout 1             | `ad4916824c2a`  |
| 1485   | Layout 1             | `ad4916824c2a`  |
| 1481   | Layout 1             | `ad4916824c2a`  |
| 1474   | Layout 1             | `ad4916824c2a`  |
| 1466   | Layout 1             | `ad4916824c2a`  |
| 1462   | Layout 1             | `ad4916824c2a`  |
| 1459   | Layout 1             | `ad4916824c2a`  |
| 1453   | Layout 1             | `ad4916824c2a`  |
| 1450   | Layout 1             | `ad4916824c2a`  |
| 1445   | Layout 1             | `ad4916824c2a`  |
| 1439   | Layout 1             | `ad4916824c2a`  |
| 1433   | Layout 1             | `ad4916824c2a`  |
| 1430   | Layout 1             | `ad4916824c2a`  |
| 1426   | Layout 1             | `ad4916824c2a`  |
| 1421   | Layout 1             | `ad4916824c2a`  |
| 1417   | Layout 1             | `ad4916824c2a`  |
| 1416   | Layout 1             | `ad4916824c2a`  |
| 1409   | Layout 1             | `ad4916824c2a`  |
| 1405   | Layout 1             | `ad4916824c2a`  |
| 1401   | Layout 1             | `ad4916824c2a`  |
| 1396   | Layout 1             | `ad4916824c2a`  |
| 1391   | Layout 1             | `ad4916824c2a`  |
| 1390   | Layout 1             | `ad4916824c2a`  |
| 1386   | Layout 1             | `ad4916824c2a`  |
| 1381   | Layout 1             | `ad4916824c2a`  |
| 1379   | Layout 1             | `ad4916824c2a`  |
| 1372   | Layout 1             | `ad4916824c2a`  |
| 1366   | Layout 1             | `ad4916824c2a`  |
| 1364   | Layout 1             | `ad4916824c2a`  |
| 1363   | Layout 1             | `ad4916824c2a`  |
| 1360   | Layout 1             | `ad4916824c2a`  |
| 1358   | Layout 1             | `ad4916824c2a`  |
| 1355   | Layout 1             | `ad4916824c2a`  |
| 1351   | Layout 1             | `ad4916824c2a`  |
| 1348   | Layout 1             | `ad4916824c2a`  |
| 1346   | Layout 1             | `ad4916824c2a`  |
| 1341   | Layout 1             | `ad4916824c2a`  |
| 1340   | Layout 1             | `ad4916824c2a`  |
| 1338   | Layout 1             | `ad4916824c2a`  |
| 1335   | Layout 1             | `ad4916824c2a`  |
| 1333   | Layout 1             | `ad4916824c2a`  |
| 1329   | Layout 1             | `ad4916824c2a`  |
| 1327   | Layout 1             | `ad4916824c2a`  |
| 1324   | Layout 1             | `ad4916824c2a`  |
| 1321   | Layout 1             | `ad4916824c2a`  |
| 1319   | Layout 1             | `ad4916824c2a`  |
| 1318   | Layout 1             | `ad4916824c2a`  |
| 1316   | Layout 1             | `ad4916824c2a`  |
| 1313   | Layout 1             | `ad4916824c2a`  |
| 1311   | Layout 1             | `ad4916824c2a`  |
| 1309   | Layout 1             | `ad4916824c2a`  |
| 1304   | Layout 1             | `ad4916824c2a`  |
| 1292   | Layout 1             | `ad4916824c2a`  |
| 1286   | Layout 1             | `ad4916824c2a`  |
| 1280   | Layout 1             | `ad4916824c2a`  |
| 1276   | Layout 1             | `ad4916824c2a`  |
| 1267   | Layout 1             | `ad4916824c2a`  |
| 1261   | Layout 1             | `ad4916824c2a`  |
| 1256   | Layout 1             | `ad4916824c2a`  |
| 1250   | Layout 1             | `ad4916824c2a`  |
| 1246   | Layout 1             | `ad4916824c2a`  |
| 1239   | Layout 1             | `ad4916824c2a`  |
| 1230   | Layout 1             | `ad4916824c2a`  |
| 1226   | Layout 1             | `ad4916824c2a`  |
| 1220   | Layout 1             | `ad4916824c2a`  |
| 1217   | Layout 1             | `ad4916824c2a`  |
| 1211   | Layout 1             | `ad4916824c2a`  |
| 1210   | Layout 1             | `ad4916824c2a`  |
| 1208   | Layout 1             | `ad4916824c2a`  |
| 1203   | Layout 1             | `ad4916824c2a`  |
| 1197   | Layout 1             | `ad4916824c2a`  |
| 1194   | Layout 1             | `ad4916824c2a`  |
| 1192   | Layout 1             | `ad4916824c2a`  |
| 1187   | Layout 1             | `ad4916824c2a`  |
| 1183   | Layout 1             | `ad4916824c2a`  |
| 1177   | Layout 1             | `ad4916824c2a`  |
| 1173   | Layout 1             | `ad4916824c2a`  |
| 1167   | Layout 1             | `ad4916824c2a`  |
| 1164   | Layout 1             | `ad4916824c2a`  |
| 1156   | Layout 1             | `ad4916824c2a`  |
| 1149   | Layout 1             | `ad4916824c2a`  |
| 1144   | Layout 1             | `ad4916824c2a`  |
| 1137   | Layout 1             | `ad4916824c2a`  |
| 1132   | Layout 1             | `ad4916824c2a`  |
| 1127   | Layout 1             | `ad4916824c2a`  |
| 1122   | Layout 1             | `ad4916824c2a`  |
| 1118   | Layout 1             | `ad4916824c2a`  |
| 1114   | Layout 1             | `ad4916824c2a`  |
| 1109   | Layout 1             | `ad4916824c2a`  |
| 1102   | No file              | `ad4916824c2a`  |
| 1096   | No file              | `ad4916824c2a`  |
| 1088   | No file              | `ad4916824c2a`  |
| 1081   | No file              | `ad4916824c2a`  |
| 1076   | No file              | `ad4916824c2a`  |
| 1069   | No file              | `ad4916824c2a`  |
| 1064   | No file              | `ad4916824c2a`  |
| 1058   | No file              | `ad4916824c2a`  |
| 1051   | No file              | `ad4916824c2a`  |
| 1044   | No file              | `ad4916824c2a`  |
| 1036   | No file              | `ad4916824c2a`  |
| 1026   | No file              | `ad4916824c2a`  |
| 1016   | No file              | `ad4916824c2a`  |
| 1009   | No file              | `ad4916824c2a`  |
| 1005   | No file              | `ad4916824c2a`  |
| 1000   | No file              | `ad4916824c2a`  |
| 998    | No file              | `ad4916824c2a`  |
| 990    | No file              | `ad4916824c2a`  |
| 979    | No file              | `ad4916824c2a`  |
| 972    | No file              | `ad4916824c2a`  |
| 963    | No file              | `ad4916824c2a`  |
| 955    | No file              | `ad4916824c2a`  |
| 946    | No file              | `ad4916824c2a`  |
| 938    | No file              | `ad4916824c2a`  |
| 927    | No file              | `ad4916824c2a`  |
| 911    | No file              | `ad4916824c2a`  |
| 904    | No file              | `ad4916824c2a`  |
| 899    | No file              | `ad4916824c2a`  |
| 894    | No file              | `ad4916824c2a`  |
| 885    | No file              | `ad4916824c2a`  |
| 879    | No file              | `ad4916824c2a`  |
| 872    | No file              | `ad4916824c2a`  |
| 864    | No file              | `ad4916824c2a`  |
| 855    | No file              | `ad4916824c2a`  |
| 853    | No file              | `ad4916824c2a`  |
| 845    | No file              | `ad4916824c2a`  |
| 837    | No file              | `ad4916824c2a`  |
| 829    | Layout 1             | `ad4916824c2a`  |
| 822    | Layout 1             | `ad4916824c2a`  |
| 814    | Layout 1             | `ad4916824c2a`  |
| 805    | Layout 1             | `ad4916824c2a`  |
| 794    | No documented layout | `ad4916824c2a`  |
| 787    | No documented layout | `ad4916824c2a`  |
| 780    | No documented layout | `ad4916824c2a`  |
| 771    | No documented layout | `ad4916824c2a`  |
| 760    | No documented layout | `ad4916824c2a`  |
| 748    | No documented layout | `ad4916824c2a`  |
| 741    | No documented layout | `ad4916824c2a`  |
| 736    | No documented layout | `ad4916824c2a`  |
| 731    | No documented layout | `ad4916824c2a`  |
| 723    | No documented layout | `ad4916824c2a`  |
| 711    | No documented layout | `ad4916824c2a`  |
| 707    | No documented layout | `ad4916824c2a`  |
| 697    | No documented layout | `ad4916824c2a`  |
| 689    | No documented layout | `ad4916824c2a`  |
| 683    | No documented layout | `ad4916824c2a`  |
| 678    | No documented layout | `ad4916824c2a`  |
| 670    | No documented layout | `ad4916824c2a`  |
| 661    | No documented layout | `ad4916824c2a`  |
| 656    | No documented layout | `ad4916824c2a`  |
| 652    | No documented layout | `ad4916824c2a`  |
| 643    | No documented layout | `ad4916824c2a`  |
| 637    | No documented layout | `ad4916824c2a`  |
| 630    | No documented layout | `ad4916824c2a`  |
| 627    | No documented layout | `ad4916824c2a`  |
| 621    | No documented layout | `ad4916824c2a`  |
| 617    | No documented layout | `ad4916824c2a`  |
| 615    | No documented layout | `ad4916824c2a`  |
| 606    | No documented layout | `ad4916824c2a`  |
| 599    | No documented layout | `ad4916824c2a`  |
| 592    | No documented layout | `ad4916824c2a`  |
| 586    | No documented layout | `ad4916824c2a`  |
| 577    | No documented layout | `ad4916824c2a`  |
| 569    | No documented layout | `ad4916824c2a`  |
| 561    | No documented layout | `ad4916824c2a`  |
| 554    | No documented layout | `ad4916824c2a`  |
| 542    | No documented layout | `ad4916824c2a`  |
| 532    | No documented layout | `ad4916824c2a`  |
| 531    | No documented layout | `ad4916824c2a`  |
| 526    | No documented layout | `ad4916824c2a`  |
| 521    | No documented layout | `ad4916824c2a`  |
| 517    | No documented layout | `ad4916824c2a`  |
| 510    | No documented layout | `ad4916824c2a`  |
| 508    | No documented layout | `ad4916824c2a`  |
| 504    | No documented layout | `ad4916824c2a`  |
| 497    | No documented layout | `ad4916824c2a`  |
| 491    | No documented layout | `ad4916824c2a`  |
| 485    | No documented layout | `ad4916824c2a`  |
| 478    | No documented layout | `ad4916824c2a`  |
| 472    | No documented layout | `ad4916824c2a`  |
| 466    | No documented layout | `ad4916824c2a`  |
| 457    | No documented layout | `ad4916824c2a`  |
| 452    | No documented layout | `ad4916824c2a`  |
| 449    | No documented layout | `ad4916824c2a`  |
| 435    | No documented layout | `ad4916824c2a`  |

<!-- versions:end -->

## Companion Files

None; `petequipskill.bss` is a standalone catalog with no offset index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

Records begin immediately at `+0x04`.

| Offset              | Type                                     | Field         | Notes                                                           |
| ------------------- | ---------------------------------------- | ------------- | --------------------------------------------------------------- |
| `+0x00`             | char[4]                                  | magic         | `PABR` (ASCII)                                                  |
| `+0x04`             | Equip Skill[while equip_skill_id != 200] | equip_skills  | Section 1, 43 x 12 bytes, `+0x004` to `+0x208`                  |
| `equip_skills+0x00` | Slot[..data_end]                         | slots         | Null block and Section 2, 200 slots from `+0x208` to `data_end` |
| `EOF-0x0C` | u32 | string_count | `0`: the PABR string table, here with no strings; `data_end` points at it |
| `EOF-0x08` | u32 | data_end | `0x0EB0` = `file_size - 12`, the offset of `string_count` |
| `EOF-0x04` | u32 | zero | Always `0` |

### Equip Skill (12 bytes)

Section 1, Equip Skills. Covers `equip_skill_id` 0 to 42 (regular pets). Stride = 12 bytes. The file stores no count: record `n` holds `equip_skill_id = n`, so the section ends at the first record whose ID is not its index, which is the first null placeholder (ID 200) of the slot table below. The parser finds the end this way, so a patch that adds Section 1 skills moves the null block and Section 2 without breaking the walk.

| Offset  | Type | Field          | Notes                                    |
| ------- | ---- | -------------- | ---------------------------------------- |
| `+0x00` | u32  | equip_skill_id | Unique skill record key (0 to 42)        |
| `+0x04` | u32  | skill_type     | Skill group (1 to 20; see Skill Types table) |
| `+0x08` | u16  | skill_level    | Skill level of the `gc::SkillKey`; always `1` |
| `+0x0A` | u16  | skill_no       | Skill number (`SkillNo`); keys the LOC type 10 name |

### Slot (variable: 16 bytes + unknown_10)

Null Block (15 x 16 bytes, offset `0x208`): fifteen placeholder records, the first 15 slots of the 200-slot table that continues as Section 2, so they are the slots for IDs 0 to 14 (see Section 2). Earlier versions of this doc read them as IDs 43 to 57. Each record = `[u32=200][u32=0][u32=0][u32=0]`. The value 200 signals a null/unused entry.

Section 2, Base Skills (variable stream, offset `0x2F8`): covers `equip_skill_id` 15 to 111, the base skills `pet.dbss` keys with `base_skill_id`; IDs 15 to 42 also exist in Section 1 as different skills. Base stride = 16 bytes. Records with `equip_skill_id = 200` are null placeholders. Records with `unknown_0c = 1` carry an additional u32 after the base record.

| Offset  | Type              | Field          | Notes                                            |
| ------- | ----------------- | -------------- | ------------------------------------------------ |
| `+0x00` | u32               | equip_skill_id | Unique skill record key (15 to 111, or 200 = null) |
| `+0x04` | u32               | skill_type     | Skill group (different numbering from Section 1) |
| `+0x08` | u16               | skill_level    | Skill level of the `gc::SkillKey`; always `1`    |
| `+0x0A` | u16               | skill_no       | Skill number (`SkillNo`); keys the LOC type 10 name |
| `+0x0C` | u32               | unknown_0c     | `0` or `1`; `1` means an extra u32 follows       |
| `+0x10` | u32 if unknown_0c = 1 | unknown_10 | Present only when `unknown_0c = 1`               |

Earlier versions of this doc called `skill_level` `tier`, `unknown_0c` `extra_flag` and `unknown_10` `extra_value`. `unknown_0c` and `unknown_10` are not in the client 1784 build (12-byte slots, Layout 1), so no source names them; on client 3474 `unknown_0c` is `1` on 10 of 73 live slots (IDs 65 to 68, 79 to 82, 104, 107) and `unknown_10` equals that record's `skill_type` on all 10.

The null block and Section 2 together are exactly 200 slots, from `0x208` up to the trailer's `data_end`, and every live Section 2 record sits at the slot whose index equals its `equip_skill_id` (slots `0` to `14` are the null block). Reading one extra u32 after each `unknown_0c = 1` record is what keeps that alignment and lands the last slot exactly on `data_end`. The parser walks the null block and Section 2 as one table starting right after Section 1, and its `slot` field is the table index, so every record in both sections has `slot = equip_skill_id`.

Within each section, skills of the same `skill_type` form a tier group (e.g., all Karma Recovery entries share type 1 in S1). The type numbering is section-local and the mapping from type ID to skill category name is derived empirically from skill numbers. No authoritative mapping table has been found. The grouping itself holds for all 116 records: every record of one `skill_type` in a section resolves to the same effect name through LOC, which is why the field keeps its name while only the type-to-name table is open.

## Field Names

The client 1784 private server loads `Pet_EquipSkill_Table` and `Pet_BaseSkill_Table` into one 24-byte entry per
record: `Index` (`equip_skill_id`) at `+0x00`, `GroupNo` (`skill_type`) at
`+0x04`, a runtime skill pointer at `+0x08` and a `gc::SkillKey` at `+0x10`.
The loader (VA `0x14086beaf` to `0x14086bebc`, and `0x14086c434` for the base skills) writes the key as `(SkillNo << 16) | 1`, so its low u16
is the skill level (always `1`) and its high u16 the sheet's `SkillNo`. The
2016 client's `gc::SkillKey` is one `unsigned int _value` whose `getLevel()`
reads the low u16 and `getSkillNo()` the high u16, which places
`skill_level` at `+0x08` and `skill_no` at `+0x0A`. The server has no reader
for this file; the record is that entry in loader order without the pointer
and the padding. After loading, it looks up every key in the skill table and
logs "펫 착용 스킬에 알수 없는 스킬(%#)의 데이터가 있습니다!" ("pet equip
skill has data for an unknown skill (%#)!") for a missing one.
`petequipskill.bss` and `fairyequipskill.bss` share the entry, the loader
shape and the per-entry checks.

The client 1784 build's own file matches `Pet_EquipSkill_Table` on all
43 equip records and `Pet_BaseSkill_Table` on all 60 base records (Index,
GroupNo, level `1`, SkillNo). Unused entries hold `equip_skill_id` `100`
there, the size of the base array (`200` on client 3474).

LOC type 10 keys the skill name by `skill_no`
([`languagedata_loc.md`](languagedata_loc.md)). Earlier versions of this doc
read `+0x08` as two u8 fields (`unknown_08`, `unknown_09`) and named `+0x0A`
`loc_id`.

## Layout 1

On client 1784 the null-entry sentinel was `100`, not `200`, and every Slot
was 12 bytes: Section 2 records had no `unknown_0c` and no `unknown_10`. The
File Layout and the Slot differ from Layout 2; the Equip Skill is the same.
On client 1784 the file holds 43 Equip Skills and 100 Slots, and every live
Section 2 record still sits at the slot whose index equals its
`equip_skill_id`.

### File Layout

| Offset              | Type                                     | Field        | Notes                                                    |
| ------------------- | ---------------------------------------- | ------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]                                  | magic        | `PABR` (ASCII)                                           |
| `+0x04`             | Equip Skill[while equip_skill_id != 100] | equip_skills | Section 1, ends at the first record whose ID is `100`    |
| `equip_skills+0x00` | Slot[..data_end]                         | slots        | Null block and Section 2, 12-byte slots up to `data_end` |
| `EOF-0x0C`          | u32                                      | string_count | `0`: the PABR string table, here with no strings         |
| `EOF-0x08`          | u32                                      | data_end     | `file_size - 12`, the offset of `string_count`           |
| `EOF-0x04`          | u32                                      | zero         | Always `0`                                               |

### Slot (12 bytes)

| Offset  | Type | Field          | Notes                                          |
| ------- | ---- | -------------- | ---------------------------------------------- |
| `+0x00` | u32  | equip_skill_id | Skill record key, or `100` = null              |
| `+0x04` | u32  | skill_type     | Skill group; `0` in a null slot                |
| `+0x08` | u16  | skill_level    | `1` in a live record, `0` in a null slot       |
| `+0x0A` | u16  | skill_no       | Skill number; `0` in a null slot               |
