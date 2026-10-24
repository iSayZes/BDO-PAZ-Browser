# `ui_territorypolicyskilltree_*.bss` Format

## Purpose

The territory policy skill trees, one grid per territory. Each skill is a
guild skill for one territory or hunting ground, such as
`62101` Protty Cave - Item Drop Rate +2% or `62241` Balenos - Combat EXP
+10%, and a run of skills along a grid row is the levels of one policy. Five
files share the format; the counts are from client 3482, where every file
is byte for byte the one of client 1784:

| File                                       | Territory | Grid    | Skills | Skill numbers      |
| ------------------------------------------ | --------- | ------- | ------ | ------------------ |
| `ui_territorypolicyskilltree_balenos.bss`  | Balenos   | 21 x 25 | 91     | `62101` to `62805` |
| `ui_territorypolicyskilltree_serendia.bss` | Serendia  | 21 x 33 | 117    | `62116` to `62806` |
| `ui_territorypolicyskilltree_calpheon.bss` | Calpheon  | 21 x 33 | 122    | `62151` to `62807` |
| `ui_territorypolicyskilltree_media.bss`    | Mediah    | 21 x 31 | 112    | `62186` to `62808` |
| `ui_territorypolicyskilltree_valencia.bss` | Valencia  | 21 x 31 | 107    | `62196` to `62809` |

All 549 skills are rows of [`skill.dbss`](skill_dbss.md) and of
[`guildskill.bss`](guildskill_bss.md) on client 3482.

Same layout as [`uiguildskilltreelayout.bss`](uiguildskilltreelayout_bss.md), read by the same handler: a `PABR` header with the grid's width and height, `width * height` 4-byte cells column by column, an empty string table and the 8-byte trailer.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                       | Bytes | Records  | Row bytes |
| ------ | -------------- | ------- | ------------------------------------------ | ----- | -------- | --------- |
| 2      | 1584 and later | 3483    | `ui_territorypolicyskilltree_balenos.bss`  | 2,124 | 525 Cell | 4         |
| 2      | 1584 and later | 3483    | `ui_territorypolicyskilltree_calpheon.bss` | 2,796 | 693 Cell | 4         |
| 2      | 1584 and later | 3483    | `ui_territorypolicyskilltree_media.bss`    | 2,628 | 651 Cell | 4         |
| 2      | 1584 and later | 3483    | `ui_territorypolicyskilltree_serendia.bss` | 2,796 | 693 Cell | 4         |
| 2      | 1584 and later | 3483    | `ui_territorypolicyskilltree_valencia.bss` | 2,628 | 651 Cell | 4         |

| Layout | File                                       | Known            | Unknown    |
| ------ | ------------------------------------------ | ---------------- | ---------- |
| 2      | `ui_territorypolicyskilltree_balenos.bss`  | 2,124 B (100.0%) | 0 B (0.0%) |
| 2      | `ui_territorypolicyskilltree_calpheon.bss` | 2,796 B (100.0%) | 0 B (0.0%) |
| 2      | `ui_territorypolicyskilltree_media.bss`    | 2,628 B (100.0%) | 0 B (0.0%) |
| 2      | `ui_territorypolicyskilltree_serendia.bss` | 2,796 B (100.0%) | 0 B (0.0%) |
| 2      | `ui_territorypolicyskilltree_valencia.bss` | 2,628 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `260c1d36ff48`  |
| 3482   | Layout 2 | `260c1d36ff48`  |
| 3474   | Layout 2 | `260c1d36ff48`  |
| 3473   | Layout 2 | `260c1d36ff48`  |
| 3464   | Layout 2 | `260c1d36ff48`  |
| 3458   | Layout 2 | `260c1d36ff48`  |
| 3454   | Layout 2 | `260c1d36ff48`  |
| 3444   | Layout 2 | `260c1d36ff48`  |
| 3435   | Layout 2 | `260c1d36ff48`  |
| 3426   | Layout 2 | `260c1d36ff48`  |
| 3418   | Layout 2 | `260c1d36ff48`  |
| 3412   | Layout 2 | `260c1d36ff48`  |
| 3402   | Layout 2 | `260c1d36ff48`  |
| 3396   | Layout 2 | `260c1d36ff48`  |
| 3387   | Layout 2 | `260c1d36ff48`  |
| 3381   | Layout 2 | `260c1d36ff48`  |
| 3373   | Layout 2 | `260c1d36ff48`  |
| 3364   | Layout 2 | `260c1d36ff48`  |
| 3356   | Layout 2 | `260c1d36ff48`  |
| 3349   | Layout 2 | `260c1d36ff48`  |
| 3342   | Layout 2 | `260c1d36ff48`  |
| 3335   | Layout 2 | `260c1d36ff48`  |
| 3326   | Layout 2 | `260c1d36ff48`  |
| 3321   | Layout 2 | `260c1d36ff48`  |
| 3314   | Layout 2 | `260c1d36ff48`  |
| 3303   | Layout 2 | `260c1d36ff48`  |
| 3302   | Layout 2 | `260c1d36ff48`  |
| 3293   | Layout 2 | `260c1d36ff48`  |
| 3283   | Layout 2 | `260c1d36ff48`  |
| 3275   | Layout 2 | `260c1d36ff48`  |
| 3267   | Layout 2 | `260c1d36ff48`  |
| 3258   | Layout 2 | `260c1d36ff48`  |
| 3251   | Layout 2 | `260c1d36ff48`  |
| 3242   | Layout 2 | `260c1d36ff48`  |
| 3235   | Layout 2 | `260c1d36ff48`  |
| 3229   | Layout 2 | `260c1d36ff48`  |
| 3212   | Layout 2 | `260c1d36ff48`  |
| 3203   | Layout 2 | `260c1d36ff48`  |
| 3193   | Layout 2 | `260c1d36ff48`  |
| 3186   | Layout 2 | `260c1d36ff48`  |
| 3177   | Layout 2 | `260c1d36ff48`  |
| 3169   | Layout 2 | `260c1d36ff48`  |
| 3158   | Layout 2 | `260c1d36ff48`  |
| 3151   | Layout 2 | `260c1d36ff48`  |
| 3144   | Layout 2 | `260c1d36ff48`  |
| 3133   | Layout 2 | `260c1d36ff48`  |
| 3125   | Layout 2 | `260c1d36ff48`  |
| 3118   | Layout 2 | `260c1d36ff48`  |
| 3111   | Layout 2 | `260c1d36ff48`  |
| 3103   | Layout 2 | `260c1d36ff48`  |
| 3095   | Layout 2 | `260c1d36ff48`  |
| 3086   | Layout 2 | `260c1d36ff48`  |
| 3072   | Layout 2 | `260c1d36ff48`  |
| 3062   | Layout 2 | `260c1d36ff48`  |
| 3052   | Layout 2 | `260c1d36ff48`  |
| 3045   | Layout 2 | `260c1d36ff48`  |
| 3037   | Layout 2 | `260c1d36ff48`  |
| 3030   | Layout 2 | `260c1d36ff48`  |
| 3021   | Layout 2 | `260c1d36ff48`  |
| 3012   | Layout 2 | `260c1d36ff48`  |
| 3002   | Layout 2 | `260c1d36ff48`  |
| 2995   | Layout 2 | `260c1d36ff48`  |
| 2987   | Layout 2 | `260c1d36ff48`  |
| 2978   | Layout 2 | `260c1d36ff48`  |
| 2970   | Layout 2 | `260c1d36ff48`  |
| 2959   | Layout 2 | `260c1d36ff48`  |
| 2951   | Layout 2 | `260c1d36ff48`  |
| 2942   | Layout 2 | `260c1d36ff48`  |
| 2935   | Layout 2 | `260c1d36ff48`  |
| 2932   | Layout 2 | `260c1d36ff48`  |
| 2923   | Layout 2 | `260c1d36ff48`  |
| 2919   | Layout 2 | `260c1d36ff48`  |
| 2907   | Layout 2 | `260c1d36ff48`  |
| 2900   | Layout 2 | `260c1d36ff48`  |
| 2891   | Layout 2 | `260c1d36ff48`  |
| 2882   | Layout 2 | `260c1d36ff48`  |
| 2872   | Layout 2 | `260c1d36ff48`  |
| 2863   | Layout 2 | `260c1d36ff48`  |
| 2855   | Layout 2 | `260c1d36ff48`  |
| 2849   | Layout 2 | `260c1d36ff48`  |
| 2844   | Layout 2 | `260c1d36ff48`  |
| 2834   | Layout 2 | `260c1d36ff48`  |
| 2825   | Layout 2 | `260c1d36ff48`  |
| 2819   | Layout 2 | `260c1d36ff48`  |
| 2811   | Layout 2 | `260c1d36ff48`  |
| 2803   | Layout 2 | `260c1d36ff48`  |
| 2794   | Layout 2 | `260c1d36ff48`  |
| 2783   | Layout 2 | `260c1d36ff48`  |
| 2774   | Layout 2 | `260c1d36ff48`  |
| 2765   | Layout 2 | `260c1d36ff48`  |
| 2756   | Layout 2 | `260c1d36ff48`  |
| 2750   | Layout 2 | `260c1d36ff48`  |
| 2743   | Layout 2 | `260c1d36ff48`  |
| 2736   | Layout 2 | `260c1d36ff48`  |
| 2726   | Layout 2 | `260c1d36ff48`  |
| 2717   | Layout 2 | `260c1d36ff48`  |
| 2709   | Layout 2 | `260c1d36ff48`  |
| 2703   | Layout 2 | `260c1d36ff48`  |
| 2695   | Layout 2 | `260c1d36ff48`  |
| 2684   | Layout 2 | `260c1d36ff48`  |
| 2672   | Layout 2 | `260c1d36ff48`  |
| 2665   | Layout 2 | `260c1d36ff48`  |
| 2657   | Layout 2 | `260c1d36ff48`  |
| 2649   | Layout 2 | `260c1d36ff48`  |
| 2644   | Layout 2 | `260c1d36ff48`  |
| 2637   | Layout 2 | `260c1d36ff48`  |
| 2629   | Layout 2 | `260c1d36ff48`  |
| 2619   | Layout 2 | `260c1d36ff48`  |
| 2612   | Layout 2 | `260c1d36ff48`  |
| 2606   | Layout 2 | `260c1d36ff48`  |
| 2602   | Layout 2 | `260c1d36ff48`  |
| 2601   | Layout 2 | `260c1d36ff48`  |
| 2592   | Layout 2 | `260c1d36ff48`  |
| 2583   | Layout 2 | `260c1d36ff48`  |
| 2575   | Layout 2 | `260c1d36ff48`  |
| 2567   | Layout 2 | `260c1d36ff48`  |
| 2560   | Layout 2 | `260c1d36ff48`  |
| 2553   | Layout 2 | `260c1d36ff48`  |
| 2545   | Layout 2 | `260c1d36ff48`  |
| 2538   | Layout 2 | `260c1d36ff48`  |
| 2529   | Layout 2 | `260c1d36ff48`  |
| 2519   | Layout 2 | `260c1d36ff48`  |
| 2513   | Layout 2 | `260c1d36ff48`  |
| 2510   | Layout 2 | `260c1d36ff48`  |
| 2507   | Layout 2 | `260c1d36ff48`  |
| 2503   | Layout 2 | `260c1d36ff48`  |
| 2498   | Layout 2 | `260c1d36ff48`  |
| 2492   | Layout 2 | `260c1d36ff48`  |
| 2487   | Layout 2 | `260c1d36ff48`  |
| 2480   | Layout 2 | `260c1d36ff48`  |
| 2474   | Layout 2 | `260c1d36ff48`  |
| 2468   | Layout 2 | `260c1d36ff48`  |
| 2460   | Layout 2 | `260c1d36ff48`  |
| 2453   | Layout 2 | `260c1d36ff48`  |
| 2444   | Layout 2 | `260c1d36ff48`  |
| 2438   | Layout 2 | `260c1d36ff48`  |
| 2434   | Layout 2 | `260c1d36ff48`  |
| 2429   | Layout 2 | `260c1d36ff48`  |
| 2421   | Layout 2 | `260c1d36ff48`  |
| 2414   | Layout 2 | `260c1d36ff48`  |
| 2407   | Layout 2 | `260c1d36ff48`  |
| 2401   | Layout 2 | `260c1d36ff48`  |
| 2397   | Layout 2 | `260c1d36ff48`  |
| 2393   | Layout 2 | `260c1d36ff48`  |
| 2384   | Layout 2 | `260c1d36ff48`  |
| 2378   | Layout 2 | `260c1d36ff48`  |
| 2372   | Layout 2 | `260c1d36ff48`  |
| 2358   | Layout 2 | `260c1d36ff48`  |
| 2352   | Layout 2 | `260c1d36ff48`  |
| 2347   | Layout 2 | `260c1d36ff48`  |
| 2343   | Layout 2 | `260c1d36ff48`  |
| 2335   | Layout 2 | `260c1d36ff48`  |
| 2327   | Layout 2 | `260c1d36ff48`  |
| 2324   | Layout 2 | `260c1d36ff48`  |
| 2319   | Layout 2 | `260c1d36ff48`  |
| 2313   | Layout 2 | `260c1d36ff48`  |
| 2308   | Layout 2 | `260c1d36ff48`  |
| 2302   | Layout 2 | `260c1d36ff48`  |
| 2295   | Layout 2 | `260c1d36ff48`  |
| 2290   | Layout 2 | `260c1d36ff48`  |
| 2284   | Layout 2 | `260c1d36ff48`  |
| 2276   | Layout 2 | `260c1d36ff48`  |
| 2269   | Layout 2 | `260c1d36ff48`  |
| 2259   | Layout 2 | `260c1d36ff48`  |
| 2250   | Layout 2 | `260c1d36ff48`  |
| 2243   | Layout 2 | `260c1d36ff48`  |
| 2235   | Layout 2 | `260c1d36ff48`  |
| 2229   | Layout 2 | `260c1d36ff48`  |
| 2224   | Layout 2 | `260c1d36ff48`  |
| 2218   | Layout 2 | `260c1d36ff48`  |
| 2215   | Layout 2 | `260c1d36ff48`  |
| 2207   | Layout 2 | `260c1d36ff48`  |
| 2203   | Layout 2 | `260c1d36ff48`  |
| 2196   | Layout 2 | `260c1d36ff48`  |
| 2192   | Layout 2 | `260c1d36ff48`  |
| 2189   | Layout 2 | `260c1d36ff48`  |
| 2183   | Layout 2 | `260c1d36ff48`  |
| 2179   | Layout 2 | `260c1d36ff48`  |
| 2171   | Layout 2 | `260c1d36ff48`  |
| 2163   | Layout 2 | `260c1d36ff48`  |
| 2156   | Layout 2 | `260c1d36ff48`  |
| 2151   | Layout 2 | `260c1d36ff48`  |
| 2147   | Layout 2 | `260c1d36ff48`  |
| 2142   | Layout 2 | `260c1d36ff48`  |
| 2138   | Layout 2 | `260c1d36ff48`  |
| 2134   | Layout 2 | `260c1d36ff48`  |
| 2130   | Layout 2 | `260c1d36ff48`  |
| 2122   | Layout 2 | `260c1d36ff48`  |
| 2107   | Layout 2 | `260c1d36ff48`  |
| 2098   | Layout 2 | `260c1d36ff48`  |
| 2089   | Layout 2 | `260c1d36ff48`  |
| 2081   | Layout 2 | `260c1d36ff48`  |
| 2073   | Layout 2 | `260c1d36ff48`  |
| 2067   | Layout 2 | `260c1d36ff48`  |
| 2063   | Layout 2 | `260c1d36ff48`  |
| 2059   | Layout 2 | `260c1d36ff48`  |
| 2052   | Layout 2 | `260c1d36ff48`  |
| 2044   | Layout 2 | `260c1d36ff48`  |
| 2039   | Layout 2 | `260c1d36ff48`  |
| 2032   | Layout 2 | `260c1d36ff48`  |
| 2025   | Layout 2 | `260c1d36ff48`  |
| 2011   | Layout 2 | `260c1d36ff48`  |
| 2005   | Layout 2 | `260c1d36ff48`  |
| 2000   | Layout 2 | `260c1d36ff48`  |
| 1996   | Layout 2 | `260c1d36ff48`  |
| 1991   | Layout 2 | `260c1d36ff48`  |
| 1985   | Layout 2 | `260c1d36ff48`  |
| 1980   | Layout 2 | `260c1d36ff48`  |
| 1969   | Layout 2 | `260c1d36ff48`  |
| 1964   | Layout 2 | `260c1d36ff48`  |
| 1958   | Layout 2 | `260c1d36ff48`  |
| 1950   | Layout 2 | `260c1d36ff48`  |
| 1945   | Layout 2 | `260c1d36ff48`  |
| 1937   | Layout 2 | `260c1d36ff48`  |
| 1933   | Layout 2 | `260c1d36ff48`  |
| 1927   | Layout 2 | `260c1d36ff48`  |
| 1921   | Layout 2 | `260c1d36ff48`  |
| 1914   | Layout 2 | `260c1d36ff48`  |
| 1908   | Layout 2 | `260c1d36ff48`  |
| 1897   | Layout 2 | `260c1d36ff48`  |
| 1892   | Layout 2 | `260c1d36ff48`  |
| 1886   | Layout 2 | `260c1d36ff48`  |
| 1881   | Layout 2 | `260c1d36ff48`  |
| 1871   | Layout 2 | `260c1d36ff48`  |
| 1866   | Layout 2 | `260c1d36ff48`  |
| 1862   | Layout 2 | `260c1d36ff48`  |
| 1854   | Layout 2 | `260c1d36ff48`  |
| 1846   | Layout 2 | `260c1d36ff48`  |
| 1838   | Layout 2 | `260c1d36ff48`  |
| 1832   | Layout 2 | `260c1d36ff48`  |
| 1826   | Layout 2 | `260c1d36ff48`  |
| 1822   | Layout 2 | `260c1d36ff48`  |
| 1818   | Layout 2 | `260c1d36ff48`  |
| 1804   | Layout 2 | `260c1d36ff48`  |
| 1794   | Layout 2 | `260c1d36ff48`  |
| 1790   | Layout 2 | `260c1d36ff48`  |
| 1784   | Layout 2 | `260c1d36ff48`  |
| 1774   | Layout 2 | `260c1d36ff48`  |
| 1771   | Layout 2 | `260c1d36ff48`  |
| 1762   | Layout 2 | `260c1d36ff48`  |
| 1759   | Layout 2 | `260c1d36ff48`  |
| 1754   | Layout 2 | `260c1d36ff48`  |
| 1749   | Layout 2 | `260c1d36ff48`  |
| 1743   | Layout 2 | `260c1d36ff48`  |
| 1737   | Layout 2 | `260c1d36ff48`  |
| 1731   | Layout 2 | `260c1d36ff48`  |
| 1725   | Layout 2 | `260c1d36ff48`  |
| 1717   | Layout 2 | `260c1d36ff48`  |
| 1710   | Layout 2 | `260c1d36ff48`  |
| 1704   | Layout 2 | `260c1d36ff48`  |
| 1698   | Layout 2 | `260c1d36ff48`  |
| 1690   | Layout 2 | `260c1d36ff48`  |
| 1685   | Layout 2 | `260c1d36ff48`  |
| 1680   | Layout 2 | `260c1d36ff48`  |
| 1674   | Layout 2 | `260c1d36ff48`  |
| 1668   | Layout 2 | `260c1d36ff48`  |
| 1659   | Layout 2 | `260c1d36ff48`  |
| 1649   | Layout 2 | `260c1d36ff48`  |
| 1642   | Layout 2 | `260c1d36ff48`  |
| 1636   | Layout 2 | `260c1d36ff48`  |
| 1628   | Layout 2 | `260c1d36ff48`  |
| 1622   | Layout 2 | `260c1d36ff48`  |
| 1614   | Layout 2 | `260c1d36ff48`  |
| 1608   | Layout 2 | `260c1d36ff48`  |
| 1602   | Layout 2 | `260c1d36ff48`  |
| 1598   | Layout 2 | `260c1d36ff48`  |
| 1594   | Layout 2 | `260c1d36ff48`  |
| 1590   | Layout 2 | `260c1d36ff48`  |
| 1587   | Layout 2 | `260c1d36ff48`  |
| 1584   | Layout 2 | `260c1d36ff48`  |
| 1579   | No file  | `260c1d36ff48`  |
| 1572   | No file  | `260c1d36ff48`  |
| 1565   | No file  | `260c1d36ff48`  |
| 1559   | No file  | `260c1d36ff48`  |
| 1554   | No file  | `260c1d36ff48`  |
| 1547   | No file  | `260c1d36ff48`  |
| 1537   | No file  | `260c1d36ff48`  |
| 1529   | No file  | `260c1d36ff48`  |
| 1524   | No file  | `260c1d36ff48`  |
| 1519   | No file  | `260c1d36ff48`  |
| 1509   | No file  | `260c1d36ff48`  |
| 1506   | No file  | `260c1d36ff48`  |
| 1504   | No file  | `260c1d36ff48`  |
| 1500   | No file  | `260c1d36ff48`  |
| 1493   | No file  | `260c1d36ff48`  |
| 1489   | No file  | `260c1d36ff48`  |
| 1485   | No file  | `260c1d36ff48`  |
| 1481   | No file  | `260c1d36ff48`  |
| 1474   | No file  | `260c1d36ff48`  |
| 1466   | No file  | `260c1d36ff48`  |
| 1462   | No file  | `260c1d36ff48`  |
| 1459   | No file  | `260c1d36ff48`  |
| 1453   | No file  | `260c1d36ff48`  |
| 1450   | No file  | `260c1d36ff48`  |
| 1445   | No file  | `260c1d36ff48`  |
| 1439   | No file  | `260c1d36ff48`  |
| 1433   | No file  | `260c1d36ff48`  |
| 1430   | No file  | `260c1d36ff48`  |
| 1426   | No file  | `260c1d36ff48`  |
| 1421   | No file  | `260c1d36ff48`  |
| 1417   | No file  | `260c1d36ff48`  |
| 1416   | No file  | `260c1d36ff48`  |
| 1409   | No file  | `260c1d36ff48`  |
| 1405   | No file  | `260c1d36ff48`  |
| 1401   | No file  | `260c1d36ff48`  |
| 1396   | No file  | `260c1d36ff48`  |
| 1391   | No file  | `260c1d36ff48`  |
| 1390   | No file  | `260c1d36ff48`  |
| 1386   | No file  | `260c1d36ff48`  |
| 1381   | No file  | `260c1d36ff48`  |
| 1379   | No file  | `260c1d36ff48`  |
| 1372   | No file  | `260c1d36ff48`  |
| 1366   | No file  | `260c1d36ff48`  |
| 1364   | No file  | `260c1d36ff48`  |
| 1363   | No file  | `260c1d36ff48`  |
| 1360   | No file  | `260c1d36ff48`  |
| 1358   | No file  | `260c1d36ff48`  |
| 1355   | No file  | `260c1d36ff48`  |
| 1351   | No file  | `260c1d36ff48`  |
| 1348   | No file  | `260c1d36ff48`  |
| 1346   | No file  | `260c1d36ff48`  |
| 1341   | No file  | `260c1d36ff48`  |
| 1340   | No file  | `260c1d36ff48`  |
| 1338   | No file  | `260c1d36ff48`  |
| 1335   | No file  | `260c1d36ff48`  |
| 1333   | No file  | `260c1d36ff48`  |
| 1329   | No file  | `260c1d36ff48`  |
| 1327   | No file  | `260c1d36ff48`  |
| 1324   | No file  | `260c1d36ff48`  |
| 1321   | No file  | `260c1d36ff48`  |
| 1319   | No file  | `260c1d36ff48`  |
| 1318   | No file  | `260c1d36ff48`  |
| 1316   | No file  | `260c1d36ff48`  |
| 1313   | No file  | `260c1d36ff48`  |
| 1311   | No file  | `260c1d36ff48`  |
| 1309   | No file  | `260c1d36ff48`  |
| 1304   | No file  | `260c1d36ff48`  |
| 1292   | No file  | `260c1d36ff48`  |
| 1286   | No file  | `260c1d36ff48`  |
| 1280   | No file  | `260c1d36ff48`  |
| 1276   | No file  | `260c1d36ff48`  |
| 1267   | No file  | `260c1d36ff48`  |
| 1261   | No file  | `260c1d36ff48`  |
| 1256   | No file  | `260c1d36ff48`  |
| 1250   | No file  | `260c1d36ff48`  |
| 1246   | No file  | `260c1d36ff48`  |
| 1239   | No file  | `260c1d36ff48`  |
| 1230   | No file  | `260c1d36ff48`  |
| 1226   | No file  | `260c1d36ff48`  |
| 1220   | No file  | `260c1d36ff48`  |
| 1217   | No file  | `260c1d36ff48`  |
| 1211   | No file  | `260c1d36ff48`  |
| 1210   | No file  | `260c1d36ff48`  |
| 1208   | No file  | `260c1d36ff48`  |
| 1203   | No file  | `260c1d36ff48`  |
| 1197   | No file  | `260c1d36ff48`  |
| 1194   | No file  | `260c1d36ff48`  |
| 1192   | No file  | `260c1d36ff48`  |
| 1187   | No file  | `260c1d36ff48`  |
| 1183   | No file  | `260c1d36ff48`  |
| 1177   | No file  | `260c1d36ff48`  |
| 1173   | No file  | `260c1d36ff48`  |
| 1167   | No file  | `260c1d36ff48`  |
| 1164   | No file  | `260c1d36ff48`  |
| 1156   | No file  | `260c1d36ff48`  |
| 1149   | No file  | `260c1d36ff48`  |
| 1144   | No file  | `260c1d36ff48`  |
| 1137   | No file  | `260c1d36ff48`  |
| 1132   | No file  | `260c1d36ff48`  |
| 1127   | No file  | `260c1d36ff48`  |
| 1122   | No file  | `260c1d36ff48`  |
| 1118   | No file  | `260c1d36ff48`  |
| 1114   | No file  | `260c1d36ff48`  |
| 1109   | No file  | `260c1d36ff48`  |
| 1102   | No file  | `260c1d36ff48`  |
| 1096   | No file  | `260c1d36ff48`  |
| 1088   | No file  | `260c1d36ff48`  |
| 1081   | No file  | `260c1d36ff48`  |
| 1076   | No file  | `260c1d36ff48`  |
| 1069   | No file  | `260c1d36ff48`  |
| 1064   | No file  | `260c1d36ff48`  |
| 1058   | No file  | `260c1d36ff48`  |
| 1051   | No file  | `260c1d36ff48`  |
| 1044   | No file  | `260c1d36ff48`  |
| 1036   | No file  | `260c1d36ff48`  |
| 1026   | No file  | `260c1d36ff48`  |
| 1016   | No file  | `260c1d36ff48`  |
| 1009   | No file  | `260c1d36ff48`  |
| 1005   | No file  | `260c1d36ff48`  |
| 1000   | No file  | `260c1d36ff48`  |
| 998    | No file  | `260c1d36ff48`  |
| 990    | No file  | `260c1d36ff48`  |
| 979    | No file  | `260c1d36ff48`  |
| 972    | No file  | `260c1d36ff48`  |
| 963    | No file  | `260c1d36ff48`  |
| 955    | No file  | `260c1d36ff48`  |
| 946    | No file  | `260c1d36ff48`  |
| 938    | No file  | `260c1d36ff48`  |
| 927    | No file  | `260c1d36ff48`  |
| 911    | No file  | `260c1d36ff48`  |
| 904    | No file  | `260c1d36ff48`  |
| 899    | No file  | `260c1d36ff48`  |
| 894    | No file  | `260c1d36ff48`  |
| 885    | No file  | `260c1d36ff48`  |
| 879    | No file  | `260c1d36ff48`  |
| 872    | No file  | `260c1d36ff48`  |
| 864    | No file  | `260c1d36ff48`  |
| 855    | No file  | `260c1d36ff48`  |
| 853    | No file  | `260c1d36ff48`  |
| 845    | No file  | `260c1d36ff48`  |
| 837    | No file  | `260c1d36ff48`  |
| 829    | No file  | `260c1d36ff48`  |
| 822    | No file  | `260c1d36ff48`  |
| 814    | No file  | `260c1d36ff48`  |
| 805    | No file  | `260c1d36ff48`  |
| 794    | No file  | `260c1d36ff48`  |
| 787    | No file  | `260c1d36ff48`  |
| 780    | No file  | `260c1d36ff48`  |
| 771    | No file  | `260c1d36ff48`  |
| 760    | No file  | `260c1d36ff48`  |
| 748    | No file  | `260c1d36ff48`  |
| 741    | No file  | `260c1d36ff48`  |
| 736    | No file  | `260c1d36ff48`  |
| 731    | No file  | `260c1d36ff48`  |
| 723    | No file  | `260c1d36ff48`  |
| 711    | No file  | `260c1d36ff48`  |
| 707    | No file  | `260c1d36ff48`  |
| 697    | No file  | `260c1d36ff48`  |
| 689    | No file  | `260c1d36ff48`  |
| 683    | No file  | `260c1d36ff48`  |
| 678    | No file  | `260c1d36ff48`  |
| 670    | No file  | `260c1d36ff48`  |
| 661    | No file  | `260c1d36ff48`  |
| 656    | No file  | `260c1d36ff48`  |
| 652    | No file  | `260c1d36ff48`  |
| 643    | No file  | `260c1d36ff48`  |
| 637    | No file  | `260c1d36ff48`  |
| 630    | No file  | `260c1d36ff48`  |
| 627    | No file  | `260c1d36ff48`  |
| 621    | No file  | `260c1d36ff48`  |
| 617    | No file  | `260c1d36ff48`  |
| 615    | No file  | `260c1d36ff48`  |
| 606    | No file  | `260c1d36ff48`  |
| 599    | No file  | `260c1d36ff48`  |
| 592    | No file  | `260c1d36ff48`  |
| 586    | No file  | `260c1d36ff48`  |
| 577    | No file  | `260c1d36ff48`  |
| 569    | No file  | `260c1d36ff48`  |
| 561    | No file  | `260c1d36ff48`  |
| 554    | No file  | `260c1d36ff48`  |
| 542    | No file  | `260c1d36ff48`  |
| 532    | No file  | `260c1d36ff48`  |
| 531    | No file  | `260c1d36ff48`  |
| 526    | No file  | `260c1d36ff48`  |
| 521    | No file  | `260c1d36ff48`  |
| 517    | No file  | `260c1d36ff48`  |
| 510    | No file  | `260c1d36ff48`  |
| 508    | No file  | `260c1d36ff48`  |
| 504    | No file  | `260c1d36ff48`  |
| 497    | No file  | `260c1d36ff48`  |
| 491    | No file  | `260c1d36ff48`  |
| 485    | No file  | `260c1d36ff48`  |
| 478    | No file  | `260c1d36ff48`  |
| 472    | No file  | `260c1d36ff48`  |
| 466    | No file  | `260c1d36ff48`  |
| 457    | No file  | `260c1d36ff48`  |
| 452    | No file  | `260c1d36ff48`  |
| 449    | No file  | `260c1d36ff48`  |
| 435    | No file  | `260c1d36ff48`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Policy Sheet

The `SiegeTerritoryPolicy` sheet of a private server's `DataSheets.bexcel`
on client 1784 has 117 rows with the columns `key`, `PolicyType`,
`PolicySkillType`, `LevelType`, `UITreePolicyLevelSkillNo`, `TerritoryKey`,
`Value` and `ContentsGroupKey`. `UITreePolicyLevelSkillNo` lists the skills
of one policy, for example `62101, 62102, 62103, 62104, 62105` (key `1`,
Protty Cave - Item Drop Rate +2% to +10%). Against the five 1784 files:

- Every one of the 549 skills in the lists is placed on a grid, and every
  placed skill is in a list.
- Each file's skills carry one `TerritoryKey`: `0` Balenos, `1` Serendia,
  `2` Calpheon, `3` Mediah, `4` Valencia.
- Each grid row holds up to two runs of skills, one in columns `0` to `8`
  and one in `12` to `20`; 109 of the 113 runs are one complete list. The
  other four are the top rows of Serendia, Calpheon, Mediah and Valencia,
  which hold two one-skill policies each (`62801` to `62809`). The top row
  of Balenos holds one, `62805` Balenos - Abundant Fishing Resources.

Each grid is a sheet of the private server's
`uiterritorypolicyskilltreelayout.xlsm` (see
[`uiguildskilltreelayout.bss` Field Names](uiguildskilltreelayout_bss.md#field-names)).

## Notes

- No client Lua of 3482 reads a territory policy tree: the only tree
  getters are `getCombatSkillTree`, `getAwakeningWeaponSkillTree`,
  `getSuccessionSkillTree`, `getFusionSkillTree` and `getGuildSkillTree`.
- Client 3482 has no `siegeterritorypolicy.bss`, the file the sheet's name
  points to.

## Open Questions

### Where the Policy Trees Show

The guild skills of the trees are still in `skill.dbss` and
`guildskill.bss`, but no Lua of client 3482 builds a window from these
grids. Whether a territory policy window still exists, or the trees are
left over from a removed lord feature, is open.
