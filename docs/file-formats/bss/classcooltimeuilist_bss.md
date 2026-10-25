# `classcooltimeuilist.bss` Format

## Purpose

The skills the skill cooldown slot window treats apart from the rest, per
class type: one list per class type with each skill's number and show
type. `panel_window_skillgroup_cooltimeslot_1.luac` (client 3482) reads
the list of the player's class with `ToClient_getSkillCoolTimeUIListCount()`,
`ToClient_getSkillCoolTimeUISkillNo(idx)` and
`ToClient_getSkillCoolTimeUIShowType(idx)`. A skill with
`__eSkillCoolTimeUITypeShow` joins the list of skills the window offers
even when it is not a learnable skill, and one with
`__eSkillCoolTimeUITypeHide` is left out of the window's search.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes | Records                   | Row bytes |
| ------ | -------------- | ------------------------- | ----- | ------------------------- | --------- |
| 1      | 1519 and later | `classcooltimeuilist.bss` | 2,260 | 101 Class List, 460 Skill | 4         |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `classcooltimeuilist.bss` | 2,260 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `37198c71f5de`  |
| 3482   | Layout 1 | `37198c71f5de`  |
| 3474   | Layout 1 | `37198c71f5de`  |
| 3473   | Layout 1 | `37198c71f5de`  |
| 3464   | Layout 1 | `37198c71f5de`  |
| 3458   | Layout 1 | `37198c71f5de`  |
| 3454   | Layout 1 | `37198c71f5de`  |
| 3444   | Layout 1 | `37198c71f5de`  |
| 3435   | Layout 1 | `37198c71f5de`  |
| 3426   | Layout 1 | `37198c71f5de`  |
| 3418   | Layout 1 | `37198c71f5de`  |
| 3412   | Layout 1 | `37198c71f5de`  |
| 3402   | Layout 1 | `37198c71f5de`  |
| 3396   | Layout 1 | `37198c71f5de`  |
| 3387   | Layout 1 | `37198c71f5de`  |
| 3381   | Layout 1 | `37198c71f5de`  |
| 3373   | Layout 1 | `37198c71f5de`  |
| 3364   | Layout 1 | `37198c71f5de`  |
| 3356   | Layout 1 | `37198c71f5de`  |
| 3349   | Layout 1 | `37198c71f5de`  |
| 3342   | Layout 1 | `37198c71f5de`  |
| 3335   | Layout 1 | `37198c71f5de`  |
| 3326   | Layout 1 | `37198c71f5de`  |
| 3321   | Layout 1 | `37198c71f5de`  |
| 3314   | Layout 1 | `37198c71f5de`  |
| 3303   | Layout 1 | `37198c71f5de`  |
| 3302   | Layout 1 | `37198c71f5de`  |
| 3293   | Layout 1 | `37198c71f5de`  |
| 3283   | Layout 1 | `37198c71f5de`  |
| 3275   | Layout 1 | `37198c71f5de`  |
| 3267   | Layout 1 | `37198c71f5de`  |
| 3258   | Layout 1 | `37198c71f5de`  |
| 3251   | Layout 1 | `37198c71f5de`  |
| 3242   | Layout 1 | `37198c71f5de`  |
| 3235   | Layout 1 | `37198c71f5de`  |
| 3229   | Layout 1 | `37198c71f5de`  |
| 3212   | Layout 1 | `37198c71f5de`  |
| 3203   | Layout 1 | `37198c71f5de`  |
| 3193   | Layout 1 | `37198c71f5de`  |
| 3186   | Layout 1 | `37198c71f5de`  |
| 3177   | Layout 1 | `37198c71f5de`  |
| 3169   | Layout 1 | `37198c71f5de`  |
| 3158   | Layout 1 | `37198c71f5de`  |
| 3151   | Layout 1 | `37198c71f5de`  |
| 3144   | Layout 1 | `37198c71f5de`  |
| 3133   | Layout 1 | `37198c71f5de`  |
| 3125   | Layout 1 | `37198c71f5de`  |
| 3118   | Layout 1 | `37198c71f5de`  |
| 3111   | Layout 1 | `37198c71f5de`  |
| 3103   | Layout 1 | `37198c71f5de`  |
| 3095   | Layout 1 | `37198c71f5de`  |
| 3086   | Layout 1 | `37198c71f5de`  |
| 3072   | Layout 1 | `37198c71f5de`  |
| 3062   | Layout 1 | `37198c71f5de`  |
| 3052   | Layout 1 | `37198c71f5de`  |
| 3045   | Layout 1 | `37198c71f5de`  |
| 3037   | Layout 1 | `37198c71f5de`  |
| 3030   | Layout 1 | `37198c71f5de`  |
| 3021   | Layout 1 | `37198c71f5de`  |
| 3012   | Layout 1 | `37198c71f5de`  |
| 3002   | Layout 1 | `37198c71f5de`  |
| 2995   | Layout 1 | `37198c71f5de`  |
| 2987   | Layout 1 | `37198c71f5de`  |
| 2978   | Layout 1 | `37198c71f5de`  |
| 2970   | Layout 1 | `37198c71f5de`  |
| 2959   | Layout 1 | `37198c71f5de`  |
| 2951   | Layout 1 | `37198c71f5de`  |
| 2942   | Layout 1 | `37198c71f5de`  |
| 2935   | Layout 1 | `37198c71f5de`  |
| 2932   | Layout 1 | `37198c71f5de`  |
| 2923   | Layout 1 | `37198c71f5de`  |
| 2919   | Layout 1 | `37198c71f5de`  |
| 2907   | Layout 1 | `37198c71f5de`  |
| 2900   | Layout 1 | `37198c71f5de`  |
| 2891   | Layout 1 | `37198c71f5de`  |
| 2882   | Layout 1 | `37198c71f5de`  |
| 2872   | Layout 1 | `37198c71f5de`  |
| 2863   | Layout 1 | `37198c71f5de`  |
| 2855   | Layout 1 | `37198c71f5de`  |
| 2849   | Layout 1 | `37198c71f5de`  |
| 2844   | Layout 1 | `37198c71f5de`  |
| 2834   | Layout 1 | `37198c71f5de`  |
| 2825   | Layout 1 | `37198c71f5de`  |
| 2819   | Layout 1 | `37198c71f5de`  |
| 2811   | Layout 1 | `37198c71f5de`  |
| 2803   | Layout 1 | `37198c71f5de`  |
| 2794   | Layout 1 | `37198c71f5de`  |
| 2783   | Layout 1 | `37198c71f5de`  |
| 2774   | Layout 1 | `37198c71f5de`  |
| 2765   | Layout 1 | `37198c71f5de`  |
| 2756   | Layout 1 | `37198c71f5de`  |
| 2750   | Layout 1 | `37198c71f5de`  |
| 2743   | Layout 1 | `37198c71f5de`  |
| 2736   | Layout 1 | `37198c71f5de`  |
| 2726   | Layout 1 | `37198c71f5de`  |
| 2717   | Layout 1 | `37198c71f5de`  |
| 2709   | Layout 1 | `37198c71f5de`  |
| 2703   | Layout 1 | `37198c71f5de`  |
| 2695   | Layout 1 | `37198c71f5de`  |
| 2684   | Layout 1 | `37198c71f5de`  |
| 2672   | Layout 1 | `37198c71f5de`  |
| 2665   | Layout 1 | `37198c71f5de`  |
| 2657   | Layout 1 | `37198c71f5de`  |
| 2649   | Layout 1 | `37198c71f5de`  |
| 2644   | Layout 1 | `37198c71f5de`  |
| 2637   | Layout 1 | `37198c71f5de`  |
| 2629   | Layout 1 | `37198c71f5de`  |
| 2619   | Layout 1 | `37198c71f5de`  |
| 2612   | Layout 1 | `37198c71f5de`  |
| 2606   | Layout 1 | `37198c71f5de`  |
| 2602   | Layout 1 | `37198c71f5de`  |
| 2601   | Layout 1 | `37198c71f5de`  |
| 2592   | Layout 1 | `37198c71f5de`  |
| 2583   | Layout 1 | `37198c71f5de`  |
| 2575   | Layout 1 | `37198c71f5de`  |
| 2567   | Layout 1 | `37198c71f5de`  |
| 2560   | Layout 1 | `37198c71f5de`  |
| 2553   | Layout 1 | `37198c71f5de`  |
| 2545   | Layout 1 | `37198c71f5de`  |
| 2538   | Layout 1 | `37198c71f5de`  |
| 2529   | Layout 1 | `37198c71f5de`  |
| 2519   | Layout 1 | `37198c71f5de`  |
| 2513   | Layout 1 | `37198c71f5de`  |
| 2510   | Layout 1 | `37198c71f5de`  |
| 2507   | Layout 1 | `37198c71f5de`  |
| 2503   | Layout 1 | `37198c71f5de`  |
| 2498   | Layout 1 | `37198c71f5de`  |
| 2492   | Layout 1 | `37198c71f5de`  |
| 2487   | Layout 1 | `37198c71f5de`  |
| 2480   | Layout 1 | `37198c71f5de`  |
| 2474   | Layout 1 | `37198c71f5de`  |
| 2468   | Layout 1 | `37198c71f5de`  |
| 2460   | Layout 1 | `37198c71f5de`  |
| 2453   | Layout 1 | `37198c71f5de`  |
| 2444   | Layout 1 | `37198c71f5de`  |
| 2438   | Layout 1 | `37198c71f5de`  |
| 2434   | Layout 1 | `37198c71f5de`  |
| 2429   | Layout 1 | `37198c71f5de`  |
| 2421   | Layout 1 | `37198c71f5de`  |
| 2414   | Layout 1 | `37198c71f5de`  |
| 2407   | Layout 1 | `37198c71f5de`  |
| 2401   | Layout 1 | `37198c71f5de`  |
| 2397   | Layout 1 | `37198c71f5de`  |
| 2393   | Layout 1 | `37198c71f5de`  |
| 2384   | Layout 1 | `37198c71f5de`  |
| 2378   | Layout 1 | `37198c71f5de`  |
| 2372   | Layout 1 | `37198c71f5de`  |
| 2358   | Layout 1 | `37198c71f5de`  |
| 2352   | Layout 1 | `37198c71f5de`  |
| 2347   | Layout 1 | `37198c71f5de`  |
| 2343   | Layout 1 | `37198c71f5de`  |
| 2335   | Layout 1 | `37198c71f5de`  |
| 2327   | Layout 1 | `37198c71f5de`  |
| 2324   | Layout 1 | `37198c71f5de`  |
| 2319   | Layout 1 | `37198c71f5de`  |
| 2313   | Layout 1 | `37198c71f5de`  |
| 2308   | Layout 1 | `37198c71f5de`  |
| 2302   | Layout 1 | `37198c71f5de`  |
| 2295   | Layout 1 | `37198c71f5de`  |
| 2290   | Layout 1 | `37198c71f5de`  |
| 2284   | Layout 1 | `37198c71f5de`  |
| 2276   | Layout 1 | `37198c71f5de`  |
| 2269   | Layout 1 | `37198c71f5de`  |
| 2259   | Layout 1 | `37198c71f5de`  |
| 2250   | Layout 1 | `37198c71f5de`  |
| 2243   | Layout 1 | `37198c71f5de`  |
| 2235   | Layout 1 | `37198c71f5de`  |
| 2229   | Layout 1 | `37198c71f5de`  |
| 2224   | Layout 1 | `37198c71f5de`  |
| 2218   | Layout 1 | `37198c71f5de`  |
| 2215   | Layout 1 | `37198c71f5de`  |
| 2207   | Layout 1 | `37198c71f5de`  |
| 2203   | Layout 1 | `37198c71f5de`  |
| 2196   | Layout 1 | `37198c71f5de`  |
| 2192   | Layout 1 | `37198c71f5de`  |
| 2189   | Layout 1 | `37198c71f5de`  |
| 2183   | Layout 1 | `37198c71f5de`  |
| 2179   | Layout 1 | `37198c71f5de`  |
| 2171   | Layout 1 | `37198c71f5de`  |
| 2163   | Layout 1 | `37198c71f5de`  |
| 2156   | Layout 1 | `37198c71f5de`  |
| 2151   | Layout 1 | `37198c71f5de`  |
| 2147   | Layout 1 | `37198c71f5de`  |
| 2142   | Layout 1 | `37198c71f5de`  |
| 2138   | Layout 1 | `37198c71f5de`  |
| 2134   | Layout 1 | `37198c71f5de`  |
| 2130   | Layout 1 | `37198c71f5de`  |
| 2122   | Layout 1 | `37198c71f5de`  |
| 2107   | Layout 1 | `37198c71f5de`  |
| 2098   | Layout 1 | `37198c71f5de`  |
| 2089   | Layout 1 | `37198c71f5de`  |
| 2081   | Layout 1 | `37198c71f5de`  |
| 2073   | Layout 1 | `37198c71f5de`  |
| 2067   | Layout 1 | `37198c71f5de`  |
| 2063   | Layout 1 | `37198c71f5de`  |
| 2059   | Layout 1 | `37198c71f5de`  |
| 2052   | Layout 1 | `37198c71f5de`  |
| 2044   | Layout 1 | `37198c71f5de`  |
| 2039   | Layout 1 | `37198c71f5de`  |
| 2032   | Layout 1 | `37198c71f5de`  |
| 2025   | Layout 1 | `37198c71f5de`  |
| 2011   | Layout 1 | `37198c71f5de`  |
| 2005   | Layout 1 | `37198c71f5de`  |
| 2000   | Layout 1 | `37198c71f5de`  |
| 1996   | Layout 1 | `37198c71f5de`  |
| 1991   | Layout 1 | `37198c71f5de`  |
| 1985   | Layout 1 | `37198c71f5de`  |
| 1980   | Layout 1 | `37198c71f5de`  |
| 1969   | Layout 1 | `37198c71f5de`  |
| 1964   | Layout 1 | `37198c71f5de`  |
| 1958   | Layout 1 | `37198c71f5de`  |
| 1950   | Layout 1 | `37198c71f5de`  |
| 1945   | Layout 1 | `37198c71f5de`  |
| 1937   | Layout 1 | `37198c71f5de`  |
| 1933   | Layout 1 | `37198c71f5de`  |
| 1927   | Layout 1 | `37198c71f5de`  |
| 1921   | Layout 1 | `37198c71f5de`  |
| 1914   | Layout 1 | `37198c71f5de`  |
| 1908   | Layout 1 | `37198c71f5de`  |
| 1897   | Layout 1 | `37198c71f5de`  |
| 1892   | Layout 1 | `37198c71f5de`  |
| 1886   | Layout 1 | `37198c71f5de`  |
| 1881   | Layout 1 | `37198c71f5de`  |
| 1871   | Layout 1 | `37198c71f5de`  |
| 1866   | Layout 1 | `37198c71f5de`  |
| 1862   | Layout 1 | `37198c71f5de`  |
| 1854   | Layout 1 | `37198c71f5de`  |
| 1846   | Layout 1 | `37198c71f5de`  |
| 1838   | Layout 1 | `37198c71f5de`  |
| 1832   | Layout 1 | `37198c71f5de`  |
| 1826   | Layout 1 | `37198c71f5de`  |
| 1822   | Layout 1 | `37198c71f5de`  |
| 1818   | Layout 1 | `37198c71f5de`  |
| 1804   | Layout 1 | `37198c71f5de`  |
| 1794   | Layout 1 | `37198c71f5de`  |
| 1790   | Layout 1 | `37198c71f5de`  |
| 1784   | Layout 1 | `37198c71f5de`  |
| 1774   | Layout 1 | `37198c71f5de`  |
| 1771   | Layout 1 | `37198c71f5de`  |
| 1762   | Layout 1 | `37198c71f5de`  |
| 1759   | Layout 1 | `37198c71f5de`  |
| 1754   | Layout 1 | `37198c71f5de`  |
| 1749   | Layout 1 | `37198c71f5de`  |
| 1743   | Layout 1 | `37198c71f5de`  |
| 1737   | Layout 1 | `37198c71f5de`  |
| 1731   | Layout 1 | `37198c71f5de`  |
| 1725   | Layout 1 | `37198c71f5de`  |
| 1717   | Layout 1 | `37198c71f5de`  |
| 1710   | Layout 1 | `37198c71f5de`  |
| 1704   | Layout 1 | `37198c71f5de`  |
| 1698   | Layout 1 | `37198c71f5de`  |
| 1690   | Layout 1 | `37198c71f5de`  |
| 1685   | Layout 1 | `37198c71f5de`  |
| 1680   | Layout 1 | `37198c71f5de`  |
| 1674   | Layout 1 | `37198c71f5de`  |
| 1668   | Layout 1 | `37198c71f5de`  |
| 1659   | Layout 1 | `37198c71f5de`  |
| 1649   | Layout 1 | `37198c71f5de`  |
| 1642   | Layout 1 | `37198c71f5de`  |
| 1636   | Layout 1 | `37198c71f5de`  |
| 1628   | Layout 1 | `37198c71f5de`  |
| 1622   | Layout 1 | `37198c71f5de`  |
| 1614   | Layout 1 | `37198c71f5de`  |
| 1608   | Layout 1 | `37198c71f5de`  |
| 1602   | Layout 1 | `37198c71f5de`  |
| 1598   | Layout 1 | `37198c71f5de`  |
| 1594   | Layout 1 | `37198c71f5de`  |
| 1590   | Layout 1 | `37198c71f5de`  |
| 1587   | Layout 1 | `37198c71f5de`  |
| 1584   | Layout 1 | `37198c71f5de`  |
| 1579   | Layout 1 | `37198c71f5de`  |
| 1572   | Layout 1 | `37198c71f5de`  |
| 1565   | Layout 1 | `37198c71f5de`  |
| 1559   | Layout 1 | `37198c71f5de`  |
| 1554   | Layout 1 | `37198c71f5de`  |
| 1547   | Layout 1 | `37198c71f5de`  |
| 1537   | Layout 1 | `37198c71f5de`  |
| 1529   | Layout 1 | `37198c71f5de`  |
| 1524   | Layout 1 | `37198c71f5de`  |
| 1519   | Layout 1 | `37198c71f5de`  |
| 1509   | No file  | `37198c71f5de`  |
| 1506   | No file  | `37198c71f5de`  |
| 1504   | No file  | `37198c71f5de`  |
| 1500   | No file  | `37198c71f5de`  |
| 1493   | No file  | `37198c71f5de`  |
| 1489   | No file  | `37198c71f5de`  |
| 1485   | No file  | `37198c71f5de`  |
| 1481   | No file  | `37198c71f5de`  |
| 1474   | No file  | `37198c71f5de`  |
| 1466   | No file  | `37198c71f5de`  |
| 1462   | No file  | `37198c71f5de`  |
| 1459   | No file  | `37198c71f5de`  |
| 1453   | No file  | `37198c71f5de`  |
| 1450   | No file  | `37198c71f5de`  |
| 1445   | No file  | `37198c71f5de`  |
| 1439   | No file  | `37198c71f5de`  |
| 1433   | No file  | `37198c71f5de`  |
| 1430   | No file  | `37198c71f5de`  |
| 1426   | No file  | `37198c71f5de`  |
| 1421   | No file  | `37198c71f5de`  |
| 1417   | No file  | `37198c71f5de`  |
| 1416   | No file  | `37198c71f5de`  |
| 1409   | No file  | `37198c71f5de`  |
| 1405   | No file  | `37198c71f5de`  |
| 1401   | No file  | `37198c71f5de`  |
| 1396   | No file  | `37198c71f5de`  |
| 1391   | No file  | `37198c71f5de`  |
| 1390   | No file  | `37198c71f5de`  |
| 1386   | No file  | `37198c71f5de`  |
| 1381   | No file  | `37198c71f5de`  |
| 1379   | No file  | `37198c71f5de`  |
| 1372   | No file  | `37198c71f5de`  |
| 1366   | No file  | `37198c71f5de`  |
| 1364   | No file  | `37198c71f5de`  |
| 1363   | No file  | `37198c71f5de`  |
| 1360   | No file  | `37198c71f5de`  |
| 1358   | No file  | `37198c71f5de`  |
| 1355   | No file  | `37198c71f5de`  |
| 1351   | No file  | `37198c71f5de`  |
| 1348   | No file  | `37198c71f5de`  |
| 1346   | No file  | `37198c71f5de`  |
| 1341   | No file  | `37198c71f5de`  |
| 1340   | No file  | `37198c71f5de`  |
| 1338   | No file  | `37198c71f5de`  |
| 1335   | No file  | `37198c71f5de`  |
| 1333   | No file  | `37198c71f5de`  |
| 1329   | No file  | `37198c71f5de`  |
| 1327   | No file  | `37198c71f5de`  |
| 1324   | No file  | `37198c71f5de`  |
| 1321   | No file  | `37198c71f5de`  |
| 1319   | No file  | `37198c71f5de`  |
| 1318   | No file  | `37198c71f5de`  |
| 1316   | No file  | `37198c71f5de`  |
| 1313   | No file  | `37198c71f5de`  |
| 1311   | No file  | `37198c71f5de`  |
| 1309   | No file  | `37198c71f5de`  |
| 1304   | No file  | `37198c71f5de`  |
| 1292   | No file  | `37198c71f5de`  |
| 1286   | No file  | `37198c71f5de`  |
| 1280   | No file  | `37198c71f5de`  |
| 1276   | No file  | `37198c71f5de`  |
| 1267   | No file  | `37198c71f5de`  |
| 1261   | No file  | `37198c71f5de`  |
| 1256   | No file  | `37198c71f5de`  |
| 1250   | No file  | `37198c71f5de`  |
| 1246   | No file  | `37198c71f5de`  |
| 1239   | No file  | `37198c71f5de`  |
| 1230   | No file  | `37198c71f5de`  |
| 1226   | No file  | `37198c71f5de`  |
| 1220   | No file  | `37198c71f5de`  |
| 1217   | No file  | `37198c71f5de`  |
| 1211   | No file  | `37198c71f5de`  |
| 1210   | No file  | `37198c71f5de`  |
| 1208   | No file  | `37198c71f5de`  |
| 1203   | No file  | `37198c71f5de`  |
| 1197   | No file  | `37198c71f5de`  |
| 1194   | No file  | `37198c71f5de`  |
| 1192   | No file  | `37198c71f5de`  |
| 1187   | No file  | `37198c71f5de`  |
| 1183   | No file  | `37198c71f5de`  |
| 1177   | No file  | `37198c71f5de`  |
| 1173   | No file  | `37198c71f5de`  |
| 1167   | No file  | `37198c71f5de`  |
| 1164   | No file  | `37198c71f5de`  |
| 1156   | No file  | `37198c71f5de`  |
| 1149   | No file  | `37198c71f5de`  |
| 1144   | No file  | `37198c71f5de`  |
| 1137   | No file  | `37198c71f5de`  |
| 1132   | No file  | `37198c71f5de`  |
| 1127   | No file  | `37198c71f5de`  |
| 1122   | No file  | `37198c71f5de`  |
| 1118   | No file  | `37198c71f5de`  |
| 1114   | No file  | `37198c71f5de`  |
| 1109   | No file  | `37198c71f5de`  |
| 1102   | No file  | `37198c71f5de`  |
| 1096   | No file  | `37198c71f5de`  |
| 1088   | No file  | `37198c71f5de`  |
| 1081   | No file  | `37198c71f5de`  |
| 1076   | No file  | `37198c71f5de`  |
| 1069   | No file  | `37198c71f5de`  |
| 1064   | No file  | `37198c71f5de`  |
| 1058   | No file  | `37198c71f5de`  |
| 1051   | No file  | `37198c71f5de`  |
| 1044   | No file  | `37198c71f5de`  |
| 1036   | No file  | `37198c71f5de`  |
| 1026   | No file  | `37198c71f5de`  |
| 1016   | No file  | `37198c71f5de`  |
| 1009   | No file  | `37198c71f5de`  |
| 1005   | No file  | `37198c71f5de`  |
| 1000   | No file  | `37198c71f5de`  |
| 998    | No file  | `37198c71f5de`  |
| 990    | No file  | `37198c71f5de`  |
| 979    | No file  | `37198c71f5de`  |
| 972    | No file  | `37198c71f5de`  |
| 963    | No file  | `37198c71f5de`  |
| 955    | No file  | `37198c71f5de`  |
| 946    | No file  | `37198c71f5de`  |
| 938    | No file  | `37198c71f5de`  |
| 927    | No file  | `37198c71f5de`  |
| 911    | No file  | `37198c71f5de`  |
| 904    | No file  | `37198c71f5de`  |
| 899    | No file  | `37198c71f5de`  |
| 894    | No file  | `37198c71f5de`  |
| 885    | No file  | `37198c71f5de`  |
| 879    | No file  | `37198c71f5de`  |
| 872    | No file  | `37198c71f5de`  |
| 864    | No file  | `37198c71f5de`  |
| 855    | No file  | `37198c71f5de`  |
| 853    | No file  | `37198c71f5de`  |
| 845    | No file  | `37198c71f5de`  |
| 837    | No file  | `37198c71f5de`  |
| 829    | No file  | `37198c71f5de`  |
| 822    | No file  | `37198c71f5de`  |
| 814    | No file  | `37198c71f5de`  |
| 805    | No file  | `37198c71f5de`  |
| 794    | No file  | `37198c71f5de`  |
| 787    | No file  | `37198c71f5de`  |
| 780    | No file  | `37198c71f5de`  |
| 771    | No file  | `37198c71f5de`  |
| 760    | No file  | `37198c71f5de`  |
| 748    | No file  | `37198c71f5de`  |
| 741    | No file  | `37198c71f5de`  |
| 736    | No file  | `37198c71f5de`  |
| 731    | No file  | `37198c71f5de`  |
| 723    | No file  | `37198c71f5de`  |
| 711    | No file  | `37198c71f5de`  |
| 707    | No file  | `37198c71f5de`  |
| 697    | No file  | `37198c71f5de`  |
| 689    | No file  | `37198c71f5de`  |
| 683    | No file  | `37198c71f5de`  |
| 678    | No file  | `37198c71f5de`  |
| 670    | No file  | `37198c71f5de`  |
| 661    | No file  | `37198c71f5de`  |
| 656    | No file  | `37198c71f5de`  |
| 652    | No file  | `37198c71f5de`  |
| 643    | No file  | `37198c71f5de`  |
| 637    | No file  | `37198c71f5de`  |
| 630    | No file  | `37198c71f5de`  |
| 627    | No file  | `37198c71f5de`  |
| 621    | No file  | `37198c71f5de`  |
| 617    | No file  | `37198c71f5de`  |
| 615    | No file  | `37198c71f5de`  |
| 606    | No file  | `37198c71f5de`  |
| 599    | No file  | `37198c71f5de`  |
| 592    | No file  | `37198c71f5de`  |
| 586    | No file  | `37198c71f5de`  |
| 577    | No file  | `37198c71f5de`  |
| 569    | No file  | `37198c71f5de`  |
| 561    | No file  | `37198c71f5de`  |
| 554    | No file  | `37198c71f5de`  |
| 542    | No file  | `37198c71f5de`  |
| 532    | No file  | `37198c71f5de`  |
| 531    | No file  | `37198c71f5de`  |
| 526    | No file  | `37198c71f5de`  |
| 521    | No file  | `37198c71f5de`  |
| 517    | No file  | `37198c71f5de`  |
| 510    | No file  | `37198c71f5de`  |
| 508    | No file  | `37198c71f5de`  |
| 504    | No file  | `37198c71f5de`  |
| 497    | No file  | `37198c71f5de`  |
| 491    | No file  | `37198c71f5de`  |
| 485    | No file  | `37198c71f5de`  |
| 478    | No file  | `37198c71f5de`  |
| 472    | No file  | `37198c71f5de`  |
| 466    | No file  | `37198c71f5de`  |
| 457    | No file  | `37198c71f5de`  |
| 452    | No file  | `37198c71f5de`  |
| 449    | No file  | `37198c71f5de`  |
| 435    | No file  | `37198c71f5de`  |

<!-- versions:end -->

## Companion Files

None. The handler names each class with LOC type 21 and each skill with
LOC type 10 from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                       | Field        | Notes                                                    |
| ------------------- | -------------------------- | ------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]                    | magic        | ASCII `PABR`                                             |
| `+0x04`             | Class List[..table_start]  | class_lists  | No count: list `n` is class type `n`; 101 lists on clients 1784 and 3482 |
| `class_lists+0x00`  | String Table               | string_table | See String Table                                         |
| `EOF-0x08`          | u32                        | table_start  | Offset of the string table, where `class_lists` ends     |
| `EOF-0x04`          | u32                        | zero         | Always `0`                                               |

### Class List (variable: 4 bytes + skills)

| Offset  | Type                | Field       | Notes                                                       |
| ------- | ------------------- | ----------- | ----------------------------------------------------------- |
| `+0x00` | u32                 | skill_count | `ToClient_getSkillCoolTimeUIListCount()`; `0` on 48 of the 101 lists (client 3482) |
| `+0x04` | Skill[skill_count]  | skills      | `idx` from `0`                                              |

### Skill (4 bytes)

| Offset  | Type | Field     | Notes                                                                   |
| ------- | ---- | --------- | ----------------------------------------------------------------------- |
| `+0x00` | u16  | show_type | `ToClient_getSkillCoolTimeUIShowType(idx)`; `1` on every skill (clients 1784 and 3482) |
| `+0x02` | u16  | skill_no  | `ToClient_getSkillCoolTimeUISkillNo(idx)`; LOC type 10 names it         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Lists

Read as a little-endian u32, a skill entry is `skill_no << 16 | 1`, the
form of a skill key at level `1`; the getters return the two halves as
the skill number and the show type. The lists on client 3482:

| Class types           | Skills                                                                   |
| --------------------- | ------------------------------------------------------------------------ |
| `9` Nova              | `7401` Accel: Frozen Ring, then `5879`, `5917`, `5912`, `5915`, `5914`, `5911`, `5910` (Accel: Twisted Orbit to Accel: Royal Fencing: Fleche) |
| `28` Wizard, `31` Witch | `4980` Succession: Magical Evasion                                     |
| `51` to `100`         | The 8 Nova skills, then `4980`                                           |
| Every other type      | None                                                                     |

On client 1784 the Nova list (`9`) holds the same skills without `7401`,
`4980` sits on class types `6`, `28` and `31` to `50`, and `51` to `100`
hold the 7 Nova skills and `4980`. Class types `51` to `100` are no
playable class: LOC type 21 names `51` to `69` after NPCs (`51` Cliff)
and `70` up `[PH]`. The
list count matches the 101 class types up to `__eClassType_Count`, the
value [`abyssoneequipmentpreset.bss`](abyssoneequipmentpreset_bss.md)
stores for every class.

## Field Names

`skill_count`, `show_type` and `skill_no` follow the three getters the
cooldown slot window calls (client 3482). The class type of a list is its
position: the getters take no class argument, so the client picks the
player's list. The 8 skills of the client 1784 file are exactly the 8 rows
of the `SkillType_Table_New` sheet of a private server's
`DataSheets.bexcel` on client 1784 whose `SkillCoolTimeUICheck` column is
set, each to `1`, the value every `show_type` holds.

## Notes

- The handler (`_bss/classcooltimeuilist/`) shows one row per skill with
  its class type and class name, the show type, and the skill number and
  name. Class types with an empty list get no row.

## Open Questions

### Which Value Is Show

`show_type` is `1` on every skill. The Lua compares it with
`__eSkillCoolTimeUITypeShow` and `__eSkillCoolTimeUITypeHide`, globals
the client sets, so their values are not in the Lua files. The sheet calls
the column `SkillCoolTimeUICheck`, which leans to `1` being Show, but a
file with a second value would settle it.
