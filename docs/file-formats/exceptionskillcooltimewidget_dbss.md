# `exceptionskillcooltimewidget.dbss` Format

## Purpose

The skills the skill cooldown window lists under another skill's name. The
window (`panel_window_skill_cooltimeslot.luac`,
`panel_window_skillgroup_cooltimeslot_1.luac`) walks the class's skill trees
and asks each usable skill with a cooldown for
`getExceptionSkillCoolTime()`. A non-zero answer is a skill number, and the
slot then shows that skill's name and number in place of its own. A row maps
one skill to the skill shown for it, for the classes in its class mask,
together with a third skill the sheet calls `SkillLearnCheckNo`.

On client 3474 the 6 rows are:

| Skill                         | Class     | Shown skill                                | Learn check skill                          |
| ----------------------------- | --------- | ------------------------------------------ | ------------------------------------------ |
| `5764` Absolute: Vengeful Star | Nova      | `5973` Succession: Vengeful Star          | `5939` Succession: Ancient Pact            |
| `5831` Quoratum's Opening     | Nova      | `5997` Succession: Quoratum's Opening      | `5939` Succession: Ancient Pact            |
| `2902` Absolute: Weakling Hunt | Berserker | `5459` Succession: Weakling Hunt          | `5410` Succession: Feral Roar              |
| `1209` Imminent Doom          | Sorceress | `4859` Succession: Imminent Doom           | `4569` Prime: Dream of Doom I              |
| `1401` Twisting Wind          | Ranger    | `7153` Succession: Twisting Wind           | `4107` Succession: Feathers of Lemoria     |
| `94` Ultimate: Dark Flame     | Sorceress | `4840` Succession: Ultimate: Dark Flame    | `4594` Prime: Dark Flame                   |

The names are LOC type 10. On client 3474 each shown skill is the
Succession version of its skill, and on every client below each learn check
skill is a Succession or Prime skill of the row's class. Client 1784 has 7 rows: the `5831`, `1209` and `94` rows above,
unchanged, a Maehwa row (`3229` Absolute: Maehwa's Will to `6793`, check
`4170`) and three Valkyrie rows (`736` to `738`, Shield Chase I to III, to
`5325`, `4857` and `4858`, check `4135` Succession: Valkyrie's Vow).
Client 1485 has 5 of those rows: `1209`, the three Valkyrie rows and `94`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                      | Bytes | Records     | Row bytes |
| ------ | -------------- | ----------------------------------------- | ----- | ----------- | --------- |
| 1      | 1292 and later | `exceptionskillcooltimewidget.dbss`       | 140   | 6 Row       | 20        |
| 1      | 1292 and later | `exceptionskillcooltimewidgetoffset.dbss` | 76    | 6 Index Row | 12        |

| Layout | File                                      | Known          | Unknown    |
| ------ | ----------------------------------------- | -------------- | ---------- |
| 1      | `exceptionskillcooltimewidget.dbss`       | 140 B (100.0%) | 0 B (0.0%) |
| 1      | `exceptionskillcooltimewidgetoffset.dbss` | 76 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a1ca538dc20b`  |
| 3482   | Layout 1 | `a1ca538dc20b`  |
| 3474   | Layout 1 | `a1ca538dc20b`  |
| 3473   | Layout 1 | `a1ca538dc20b`  |
| 3464   | Layout 1 | `a1ca538dc20b`  |
| 3458   | Layout 1 | `a1ca538dc20b`  |
| 3454   | Layout 1 | `a1ca538dc20b`  |
| 3444   | Layout 1 | `a1ca538dc20b`  |
| 3435   | Layout 1 | `a1ca538dc20b`  |
| 3426   | Layout 1 | `a1ca538dc20b`  |
| 3418   | Layout 1 | `a1ca538dc20b`  |
| 3412   | Layout 1 | `a1ca538dc20b`  |
| 3402   | Layout 1 | `a1ca538dc20b`  |
| 3396   | Layout 1 | `a1ca538dc20b`  |
| 3387   | Layout 1 | `a1ca538dc20b`  |
| 3381   | Layout 1 | `a1ca538dc20b`  |
| 3373   | Layout 1 | `a1ca538dc20b`  |
| 3364   | Layout 1 | `a1ca538dc20b`  |
| 3356   | Layout 1 | `a1ca538dc20b`  |
| 3349   | Layout 1 | `a1ca538dc20b`  |
| 3342   | Layout 1 | `a1ca538dc20b`  |
| 3335   | Layout 1 | `a1ca538dc20b`  |
| 3326   | Layout 1 | `a1ca538dc20b`  |
| 3321   | Layout 1 | `a1ca538dc20b`  |
| 3314   | Layout 1 | `a1ca538dc20b`  |
| 3303   | Layout 1 | `a1ca538dc20b`  |
| 3302   | Layout 1 | `a1ca538dc20b`  |
| 3293   | Layout 1 | `a1ca538dc20b`  |
| 3283   | Layout 1 | `a1ca538dc20b`  |
| 3275   | Layout 1 | `a1ca538dc20b`  |
| 3267   | Layout 1 | `a1ca538dc20b`  |
| 3258   | Layout 1 | `a1ca538dc20b`  |
| 3251   | Layout 1 | `a1ca538dc20b`  |
| 3242   | Layout 1 | `a1ca538dc20b`  |
| 3235   | Layout 1 | `a1ca538dc20b`  |
| 3229   | Layout 1 | `a1ca538dc20b`  |
| 3212   | Layout 1 | `a1ca538dc20b`  |
| 3203   | Layout 1 | `a1ca538dc20b`  |
| 3193   | Layout 1 | `a1ca538dc20b`  |
| 3186   | Layout 1 | `a1ca538dc20b`  |
| 3177   | Layout 1 | `a1ca538dc20b`  |
| 3169   | Layout 1 | `a1ca538dc20b`  |
| 3158   | Layout 1 | `a1ca538dc20b`  |
| 3151   | Layout 1 | `a1ca538dc20b`  |
| 3144   | Layout 1 | `a1ca538dc20b`  |
| 3133   | Layout 1 | `a1ca538dc20b`  |
| 3125   | Layout 1 | `a1ca538dc20b`  |
| 3118   | Layout 1 | `a1ca538dc20b`  |
| 3111   | Layout 1 | `a1ca538dc20b`  |
| 3103   | Layout 1 | `a1ca538dc20b`  |
| 3095   | Layout 1 | `a1ca538dc20b`  |
| 3086   | Layout 1 | `a1ca538dc20b`  |
| 3072   | Layout 1 | `a1ca538dc20b`  |
| 3062   | Layout 1 | `a1ca538dc20b`  |
| 3052   | Layout 1 | `a1ca538dc20b`  |
| 3045   | Layout 1 | `a1ca538dc20b`  |
| 3037   | Layout 1 | `a1ca538dc20b`  |
| 3030   | Layout 1 | `a1ca538dc20b`  |
| 3021   | Layout 1 | `a1ca538dc20b`  |
| 3012   | Layout 1 | `a1ca538dc20b`  |
| 3002   | Layout 1 | `a1ca538dc20b`  |
| 2995   | Layout 1 | `a1ca538dc20b`  |
| 2987   | Layout 1 | `a1ca538dc20b`  |
| 2978   | Layout 1 | `a1ca538dc20b`  |
| 2970   | Layout 1 | `a1ca538dc20b`  |
| 2959   | Layout 1 | `a1ca538dc20b`  |
| 2951   | Layout 1 | `a1ca538dc20b`  |
| 2942   | Layout 1 | `a1ca538dc20b`  |
| 2935   | Layout 1 | `a1ca538dc20b`  |
| 2932   | Layout 1 | `a1ca538dc20b`  |
| 2923   | Layout 1 | `a1ca538dc20b`  |
| 2919   | Layout 1 | `a1ca538dc20b`  |
| 2907   | Layout 1 | `a1ca538dc20b`  |
| 2900   | Layout 1 | `a1ca538dc20b`  |
| 2891   | Layout 1 | `a1ca538dc20b`  |
| 2882   | Layout 1 | `a1ca538dc20b`  |
| 2872   | Layout 1 | `a1ca538dc20b`  |
| 2863   | Layout 1 | `a1ca538dc20b`  |
| 2855   | Layout 1 | `a1ca538dc20b`  |
| 2849   | Layout 1 | `a1ca538dc20b`  |
| 2844   | Layout 1 | `a1ca538dc20b`  |
| 2834   | Layout 1 | `a1ca538dc20b`  |
| 2825   | Layout 1 | `a1ca538dc20b`  |
| 2819   | Layout 1 | `a1ca538dc20b`  |
| 2811   | Layout 1 | `a1ca538dc20b`  |
| 2803   | Layout 1 | `a1ca538dc20b`  |
| 2794   | Layout 1 | `a1ca538dc20b`  |
| 2783   | Layout 1 | `a1ca538dc20b`  |
| 2774   | Layout 1 | `a1ca538dc20b`  |
| 2765   | Layout 1 | `a1ca538dc20b`  |
| 2756   | Layout 1 | `a1ca538dc20b`  |
| 2750   | Layout 1 | `a1ca538dc20b`  |
| 2743   | Layout 1 | `a1ca538dc20b`  |
| 2736   | Layout 1 | `a1ca538dc20b`  |
| 2726   | Layout 1 | `a1ca538dc20b`  |
| 2717   | Layout 1 | `a1ca538dc20b`  |
| 2709   | Layout 1 | `a1ca538dc20b`  |
| 2703   | Layout 1 | `a1ca538dc20b`  |
| 2695   | Layout 1 | `a1ca538dc20b`  |
| 2684   | Layout 1 | `a1ca538dc20b`  |
| 2672   | Layout 1 | `a1ca538dc20b`  |
| 2665   | Layout 1 | `a1ca538dc20b`  |
| 2657   | Layout 1 | `a1ca538dc20b`  |
| 2649   | Layout 1 | `a1ca538dc20b`  |
| 2644   | Layout 1 | `a1ca538dc20b`  |
| 2637   | Layout 1 | `a1ca538dc20b`  |
| 2629   | Layout 1 | `a1ca538dc20b`  |
| 2619   | Layout 1 | `a1ca538dc20b`  |
| 2612   | Layout 1 | `a1ca538dc20b`  |
| 2606   | Layout 1 | `a1ca538dc20b`  |
| 2602   | Layout 1 | `a1ca538dc20b`  |
| 2601   | Layout 1 | `a1ca538dc20b`  |
| 2592   | Layout 1 | `a1ca538dc20b`  |
| 2583   | Layout 1 | `a1ca538dc20b`  |
| 2575   | Layout 1 | `a1ca538dc20b`  |
| 2567   | Layout 1 | `a1ca538dc20b`  |
| 2560   | Layout 1 | `a1ca538dc20b`  |
| 2553   | Layout 1 | `a1ca538dc20b`  |
| 2545   | Layout 1 | `a1ca538dc20b`  |
| 2538   | Layout 1 | `a1ca538dc20b`  |
| 2529   | Layout 1 | `a1ca538dc20b`  |
| 2519   | Layout 1 | `a1ca538dc20b`  |
| 2513   | Layout 1 | `a1ca538dc20b`  |
| 2510   | Layout 1 | `a1ca538dc20b`  |
| 2507   | Layout 1 | `a1ca538dc20b`  |
| 2503   | Layout 1 | `a1ca538dc20b`  |
| 2498   | Layout 1 | `a1ca538dc20b`  |
| 2492   | Layout 1 | `a1ca538dc20b`  |
| 2487   | Layout 1 | `a1ca538dc20b`  |
| 2480   | Layout 1 | `a1ca538dc20b`  |
| 2474   | Layout 1 | `a1ca538dc20b`  |
| 2468   | Layout 1 | `a1ca538dc20b`  |
| 2460   | Layout 1 | `a1ca538dc20b`  |
| 2453   | Layout 1 | `a1ca538dc20b`  |
| 2444   | Layout 1 | `a1ca538dc20b`  |
| 2438   | Layout 1 | `a1ca538dc20b`  |
| 2434   | Layout 1 | `a1ca538dc20b`  |
| 2429   | Layout 1 | `a1ca538dc20b`  |
| 2421   | Layout 1 | `a1ca538dc20b`  |
| 2414   | Layout 1 | `a1ca538dc20b`  |
| 2407   | Layout 1 | `a1ca538dc20b`  |
| 2401   | Layout 1 | `a1ca538dc20b`  |
| 2397   | Layout 1 | `a1ca538dc20b`  |
| 2393   | Layout 1 | `a1ca538dc20b`  |
| 2384   | Layout 1 | `a1ca538dc20b`  |
| 2378   | Layout 1 | `a1ca538dc20b`  |
| 2372   | Layout 1 | `a1ca538dc20b`  |
| 2358   | Layout 1 | `a1ca538dc20b`  |
| 2352   | Layout 1 | `a1ca538dc20b`  |
| 2347   | Layout 1 | `a1ca538dc20b`  |
| 2343   | Layout 1 | `a1ca538dc20b`  |
| 2335   | Layout 1 | `a1ca538dc20b`  |
| 2327   | Layout 1 | `a1ca538dc20b`  |
| 2324   | Layout 1 | `a1ca538dc20b`  |
| 2319   | Layout 1 | `a1ca538dc20b`  |
| 2313   | Layout 1 | `a1ca538dc20b`  |
| 2308   | Layout 1 | `a1ca538dc20b`  |
| 2302   | Layout 1 | `a1ca538dc20b`  |
| 2295   | Layout 1 | `a1ca538dc20b`  |
| 2290   | Layout 1 | `a1ca538dc20b`  |
| 2284   | Layout 1 | `a1ca538dc20b`  |
| 2276   | Layout 1 | `a1ca538dc20b`  |
| 2269   | Layout 1 | `a1ca538dc20b`  |
| 2259   | Layout 1 | `a1ca538dc20b`  |
| 2250   | Layout 1 | `a1ca538dc20b`  |
| 2243   | Layout 1 | `a1ca538dc20b`  |
| 2235   | Layout 1 | `a1ca538dc20b`  |
| 2229   | Layout 1 | `a1ca538dc20b`  |
| 2224   | Layout 1 | `a1ca538dc20b`  |
| 2218   | Layout 1 | `a1ca538dc20b`  |
| 2215   | Layout 1 | `a1ca538dc20b`  |
| 2207   | Layout 1 | `a1ca538dc20b`  |
| 2203   | Layout 1 | `a1ca538dc20b`  |
| 2196   | Layout 1 | `a1ca538dc20b`  |
| 2192   | Layout 1 | `a1ca538dc20b`  |
| 2189   | Layout 1 | `a1ca538dc20b`  |
| 2183   | Layout 1 | `a1ca538dc20b`  |
| 2179   | Layout 1 | `a1ca538dc20b`  |
| 2171   | Layout 1 | `a1ca538dc20b`  |
| 2163   | Layout 1 | `a1ca538dc20b`  |
| 2156   | Layout 1 | `a1ca538dc20b`  |
| 2151   | Layout 1 | `a1ca538dc20b`  |
| 2147   | Layout 1 | `a1ca538dc20b`  |
| 2142   | Layout 1 | `a1ca538dc20b`  |
| 2138   | Layout 1 | `a1ca538dc20b`  |
| 2134   | Layout 1 | `a1ca538dc20b`  |
| 2130   | Layout 1 | `a1ca538dc20b`  |
| 2122   | Layout 1 | `a1ca538dc20b`  |
| 2107   | Layout 1 | `a1ca538dc20b`  |
| 2098   | Layout 1 | `a1ca538dc20b`  |
| 2089   | Layout 1 | `a1ca538dc20b`  |
| 2081   | Layout 1 | `a1ca538dc20b`  |
| 2073   | Layout 1 | `a1ca538dc20b`  |
| 2067   | Layout 1 | `a1ca538dc20b`  |
| 2063   | Layout 1 | `a1ca538dc20b`  |
| 2059   | Layout 1 | `a1ca538dc20b`  |
| 2052   | Layout 1 | `a1ca538dc20b`  |
| 2044   | Layout 1 | `a1ca538dc20b`  |
| 2039   | Layout 1 | `a1ca538dc20b`  |
| 2032   | Layout 1 | `a1ca538dc20b`  |
| 2025   | Layout 1 | `a1ca538dc20b`  |
| 2011   | Layout 1 | `a1ca538dc20b`  |
| 2005   | Layout 1 | `a1ca538dc20b`  |
| 2000   | Layout 1 | `a1ca538dc20b`  |
| 1996   | Layout 1 | `a1ca538dc20b`  |
| 1991   | Layout 1 | `a1ca538dc20b`  |
| 1985   | Layout 1 | `a1ca538dc20b`  |
| 1980   | Layout 1 | `a1ca538dc20b`  |
| 1969   | Layout 1 | `a1ca538dc20b`  |
| 1964   | Layout 1 | `a1ca538dc20b`  |
| 1958   | Layout 1 | `a1ca538dc20b`  |
| 1950   | Layout 1 | `a1ca538dc20b`  |
| 1945   | Layout 1 | `a1ca538dc20b`  |
| 1937   | Layout 1 | `a1ca538dc20b`  |
| 1933   | Layout 1 | `a1ca538dc20b`  |
| 1927   | Layout 1 | `a1ca538dc20b`  |
| 1921   | Layout 1 | `a1ca538dc20b`  |
| 1914   | Layout 1 | `a1ca538dc20b`  |
| 1908   | Layout 1 | `a1ca538dc20b`  |
| 1897   | Layout 1 | `a1ca538dc20b`  |
| 1892   | Layout 1 | `a1ca538dc20b`  |
| 1886   | Layout 1 | `a1ca538dc20b`  |
| 1881   | Layout 1 | `a1ca538dc20b`  |
| 1871   | Layout 1 | `a1ca538dc20b`  |
| 1866   | Layout 1 | `a1ca538dc20b`  |
| 1862   | Layout 1 | `a1ca538dc20b`  |
| 1854   | Layout 1 | `a1ca538dc20b`  |
| 1846   | Layout 1 | `a1ca538dc20b`  |
| 1838   | Layout 1 | `a1ca538dc20b`  |
| 1832   | Layout 1 | `a1ca538dc20b`  |
| 1826   | Layout 1 | `a1ca538dc20b`  |
| 1822   | Layout 1 | `a1ca538dc20b`  |
| 1818   | Layout 1 | `a1ca538dc20b`  |
| 1804   | Layout 1 | `a1ca538dc20b`  |
| 1794   | Layout 1 | `a1ca538dc20b`  |
| 1790   | Layout 1 | `a1ca538dc20b`  |
| 1784   | Layout 1 | `a1ca538dc20b`  |
| 1774   | Layout 1 | `a1ca538dc20b`  |
| 1771   | Layout 1 | `a1ca538dc20b`  |
| 1762   | Layout 1 | `a1ca538dc20b`  |
| 1759   | Layout 1 | `a1ca538dc20b`  |
| 1754   | Layout 1 | `a1ca538dc20b`  |
| 1749   | Layout 1 | `a1ca538dc20b`  |
| 1743   | Layout 1 | `a1ca538dc20b`  |
| 1737   | Layout 1 | `a1ca538dc20b`  |
| 1731   | Layout 1 | `a1ca538dc20b`  |
| 1725   | Layout 1 | `a1ca538dc20b`  |
| 1717   | Layout 1 | `a1ca538dc20b`  |
| 1710   | Layout 1 | `a1ca538dc20b`  |
| 1704   | Layout 1 | `a1ca538dc20b`  |
| 1698   | Layout 1 | `a1ca538dc20b`  |
| 1690   | Layout 1 | `a1ca538dc20b`  |
| 1685   | Layout 1 | `a1ca538dc20b`  |
| 1680   | Layout 1 | `a1ca538dc20b`  |
| 1674   | Layout 1 | `a1ca538dc20b`  |
| 1668   | Layout 1 | `a1ca538dc20b`  |
| 1659   | Layout 1 | `a1ca538dc20b`  |
| 1649   | Layout 1 | `a1ca538dc20b`  |
| 1642   | Layout 1 | `a1ca538dc20b`  |
| 1636   | Layout 1 | `a1ca538dc20b`  |
| 1628   | Layout 1 | `a1ca538dc20b`  |
| 1622   | Layout 1 | `a1ca538dc20b`  |
| 1614   | Layout 1 | `a1ca538dc20b`  |
| 1608   | Layout 1 | `a1ca538dc20b`  |
| 1602   | Layout 1 | `a1ca538dc20b`  |
| 1598   | Layout 1 | `a1ca538dc20b`  |
| 1594   | Layout 1 | `a1ca538dc20b`  |
| 1590   | Layout 1 | `a1ca538dc20b`  |
| 1587   | Layout 1 | `a1ca538dc20b`  |
| 1584   | Layout 1 | `a1ca538dc20b`  |
| 1579   | Layout 1 | `a1ca538dc20b`  |
| 1572   | Layout 1 | `a1ca538dc20b`  |
| 1565   | Layout 1 | `a1ca538dc20b`  |
| 1559   | Layout 1 | `a1ca538dc20b`  |
| 1554   | Layout 1 | `a1ca538dc20b`  |
| 1547   | Layout 1 | `a1ca538dc20b`  |
| 1537   | Layout 1 | `a1ca538dc20b`  |
| 1529   | Layout 1 | `a1ca538dc20b`  |
| 1524   | Layout 1 | `a1ca538dc20b`  |
| 1519   | Layout 1 | `a1ca538dc20b`  |
| 1509   | Layout 1 | `a1ca538dc20b`  |
| 1506   | Layout 1 | `a1ca538dc20b`  |
| 1504   | Layout 1 | `a1ca538dc20b`  |
| 1500   | Layout 1 | `a1ca538dc20b`  |
| 1493   | Layout 1 | `a1ca538dc20b`  |
| 1489   | Layout 1 | `a1ca538dc20b`  |
| 1485   | Layout 1 | `a1ca538dc20b`  |
| 1481   | Layout 1 | `a1ca538dc20b`  |
| 1474   | Layout 1 | `a1ca538dc20b`  |
| 1466   | Layout 1 | `a1ca538dc20b`  |
| 1462   | Layout 1 | `a1ca538dc20b`  |
| 1459   | Layout 1 | `a1ca538dc20b`  |
| 1453   | Layout 1 | `a1ca538dc20b`  |
| 1450   | Layout 1 | `a1ca538dc20b`  |
| 1445   | Layout 1 | `a1ca538dc20b`  |
| 1439   | Layout 1 | `a1ca538dc20b`  |
| 1433   | Layout 1 | `a1ca538dc20b`  |
| 1430   | Layout 1 | `a1ca538dc20b`  |
| 1426   | Layout 1 | `a1ca538dc20b`  |
| 1421   | Layout 1 | `a1ca538dc20b`  |
| 1417   | Layout 1 | `a1ca538dc20b`  |
| 1416   | Layout 1 | `a1ca538dc20b`  |
| 1409   | Layout 1 | `a1ca538dc20b`  |
| 1405   | Layout 1 | `a1ca538dc20b`  |
| 1401   | Layout 1 | `a1ca538dc20b`  |
| 1396   | Layout 1 | `a1ca538dc20b`  |
| 1391   | Layout 1 | `a1ca538dc20b`  |
| 1390   | Layout 1 | `a1ca538dc20b`  |
| 1386   | Layout 1 | `a1ca538dc20b`  |
| 1381   | Layout 1 | `a1ca538dc20b`  |
| 1379   | Layout 1 | `a1ca538dc20b`  |
| 1372   | Layout 1 | `a1ca538dc20b`  |
| 1366   | Layout 1 | `a1ca538dc20b`  |
| 1364   | Layout 1 | `a1ca538dc20b`  |
| 1363   | Layout 1 | `a1ca538dc20b`  |
| 1360   | Layout 1 | `a1ca538dc20b`  |
| 1358   | Layout 1 | `a1ca538dc20b`  |
| 1355   | Layout 1 | `a1ca538dc20b`  |
| 1351   | Layout 1 | `a1ca538dc20b`  |
| 1348   | Layout 1 | `a1ca538dc20b`  |
| 1346   | Layout 1 | `a1ca538dc20b`  |
| 1341   | Layout 1 | `a1ca538dc20b`  |
| 1340   | Layout 1 | `a1ca538dc20b`  |
| 1338   | Layout 1 | `a1ca538dc20b`  |
| 1335   | Layout 1 | `a1ca538dc20b`  |
| 1333   | Layout 1 | `a1ca538dc20b`  |
| 1329   | Layout 1 | `a1ca538dc20b`  |
| 1327   | Layout 1 | `a1ca538dc20b`  |
| 1324   | Layout 1 | `a1ca538dc20b`  |
| 1321   | Layout 1 | `a1ca538dc20b`  |
| 1319   | Layout 1 | `a1ca538dc20b`  |
| 1318   | Layout 1 | `a1ca538dc20b`  |
| 1316   | Layout 1 | `a1ca538dc20b`  |
| 1313   | Layout 1 | `a1ca538dc20b`  |
| 1311   | Layout 1 | `a1ca538dc20b`  |
| 1309   | Layout 1 | `a1ca538dc20b`  |
| 1304   | Layout 1 | `a1ca538dc20b`  |
| 1292   | Layout 1 | `a1ca538dc20b`  |
| 1286   | No file  | `a1ca538dc20b`  |
| 1280   | No file  | `a1ca538dc20b`  |
| 1276   | No file  | `a1ca538dc20b`  |
| 1267   | No file  | `a1ca538dc20b`  |
| 1261   | No file  | `a1ca538dc20b`  |
| 1256   | No file  | `a1ca538dc20b`  |
| 1250   | No file  | `a1ca538dc20b`  |
| 1246   | No file  | `a1ca538dc20b`  |
| 1239   | No file  | `a1ca538dc20b`  |
| 1230   | No file  | `a1ca538dc20b`  |
| 1226   | No file  | `a1ca538dc20b`  |
| 1220   | No file  | `a1ca538dc20b`  |
| 1217   | No file  | `a1ca538dc20b`  |
| 1211   | No file  | `a1ca538dc20b`  |
| 1210   | No file  | `a1ca538dc20b`  |
| 1208   | No file  | `a1ca538dc20b`  |
| 1203   | No file  | `a1ca538dc20b`  |
| 1197   | No file  | `a1ca538dc20b`  |
| 1194   | No file  | `a1ca538dc20b`  |
| 1192   | No file  | `a1ca538dc20b`  |
| 1187   | No file  | `a1ca538dc20b`  |
| 1183   | No file  | `a1ca538dc20b`  |
| 1177   | No file  | `a1ca538dc20b`  |
| 1173   | No file  | `a1ca538dc20b`  |
| 1167   | No file  | `a1ca538dc20b`  |
| 1164   | No file  | `a1ca538dc20b`  |
| 1156   | No file  | `a1ca538dc20b`  |
| 1149   | No file  | `a1ca538dc20b`  |
| 1144   | No file  | `a1ca538dc20b`  |
| 1137   | No file  | `a1ca538dc20b`  |
| 1132   | No file  | `a1ca538dc20b`  |
| 1127   | No file  | `a1ca538dc20b`  |
| 1122   | No file  | `a1ca538dc20b`  |
| 1118   | No file  | `a1ca538dc20b`  |
| 1114   | No file  | `a1ca538dc20b`  |
| 1109   | No file  | `a1ca538dc20b`  |
| 1102   | No file  | `a1ca538dc20b`  |
| 1096   | No file  | `a1ca538dc20b`  |
| 1088   | No file  | `a1ca538dc20b`  |
| 1081   | No file  | `a1ca538dc20b`  |
| 1076   | No file  | `a1ca538dc20b`  |
| 1069   | No file  | `a1ca538dc20b`  |
| 1064   | No file  | `a1ca538dc20b`  |
| 1058   | No file  | `a1ca538dc20b`  |
| 1051   | No file  | `a1ca538dc20b`  |
| 1044   | No file  | `a1ca538dc20b`  |
| 1036   | No file  | `a1ca538dc20b`  |
| 1026   | No file  | `a1ca538dc20b`  |
| 1016   | No file  | `a1ca538dc20b`  |
| 1009   | No file  | `a1ca538dc20b`  |
| 1005   | No file  | `a1ca538dc20b`  |
| 1000   | No file  | `a1ca538dc20b`  |
| 998    | No file  | `a1ca538dc20b`  |
| 990    | No file  | `a1ca538dc20b`  |
| 979    | No file  | `a1ca538dc20b`  |
| 972    | No file  | `a1ca538dc20b`  |
| 963    | No file  | `a1ca538dc20b`  |
| 955    | No file  | `a1ca538dc20b`  |
| 946    | No file  | `a1ca538dc20b`  |
| 938    | No file  | `a1ca538dc20b`  |
| 927    | No file  | `a1ca538dc20b`  |
| 911    | No file  | `a1ca538dc20b`  |
| 904    | No file  | `a1ca538dc20b`  |
| 899    | No file  | `a1ca538dc20b`  |
| 894    | No file  | `a1ca538dc20b`  |
| 885    | No file  | `a1ca538dc20b`  |
| 879    | No file  | `a1ca538dc20b`  |
| 872    | No file  | `a1ca538dc20b`  |
| 864    | No file  | `a1ca538dc20b`  |
| 855    | No file  | `a1ca538dc20b`  |
| 853    | No file  | `a1ca538dc20b`  |
| 845    | No file  | `a1ca538dc20b`  |
| 837    | No file  | `a1ca538dc20b`  |
| 829    | No file  | `a1ca538dc20b`  |
| 822    | No file  | `a1ca538dc20b`  |
| 814    | No file  | `a1ca538dc20b`  |
| 805    | No file  | `a1ca538dc20b`  |
| 794    | No file  | `a1ca538dc20b`  |
| 787    | No file  | `a1ca538dc20b`  |
| 780    | No file  | `a1ca538dc20b`  |
| 771    | No file  | `a1ca538dc20b`  |
| 760    | No file  | `a1ca538dc20b`  |
| 748    | No file  | `a1ca538dc20b`  |
| 741    | No file  | `a1ca538dc20b`  |
| 736    | No file  | `a1ca538dc20b`  |
| 731    | No file  | `a1ca538dc20b`  |
| 723    | No file  | `a1ca538dc20b`  |
| 711    | No file  | `a1ca538dc20b`  |
| 707    | No file  | `a1ca538dc20b`  |
| 697    | No file  | `a1ca538dc20b`  |
| 689    | No file  | `a1ca538dc20b`  |
| 683    | No file  | `a1ca538dc20b`  |
| 678    | No file  | `a1ca538dc20b`  |
| 670    | No file  | `a1ca538dc20b`  |
| 661    | No file  | `a1ca538dc20b`  |
| 656    | No file  | `a1ca538dc20b`  |
| 652    | No file  | `a1ca538dc20b`  |
| 643    | No file  | `a1ca538dc20b`  |
| 637    | No file  | `a1ca538dc20b`  |
| 630    | No file  | `a1ca538dc20b`  |
| 627    | No file  | `a1ca538dc20b`  |
| 621    | No file  | `a1ca538dc20b`  |
| 617    | No file  | `a1ca538dc20b`  |
| 615    | No file  | `a1ca538dc20b`  |
| 606    | No file  | `a1ca538dc20b`  |
| 599    | No file  | `a1ca538dc20b`  |
| 592    | No file  | `a1ca538dc20b`  |
| 586    | No file  | `a1ca538dc20b`  |
| 577    | No file  | `a1ca538dc20b`  |
| 569    | No file  | `a1ca538dc20b`  |
| 561    | No file  | `a1ca538dc20b`  |
| 554    | No file  | `a1ca538dc20b`  |
| 542    | No file  | `a1ca538dc20b`  |
| 532    | No file  | `a1ca538dc20b`  |
| 531    | No file  | `a1ca538dc20b`  |
| 526    | No file  | `a1ca538dc20b`  |
| 521    | No file  | `a1ca538dc20b`  |
| 517    | No file  | `a1ca538dc20b`  |
| 510    | No file  | `a1ca538dc20b`  |
| 508    | No file  | `a1ca538dc20b`  |
| 504    | No file  | `a1ca538dc20b`  |
| 497    | No file  | `a1ca538dc20b`  |
| 491    | No file  | `a1ca538dc20b`  |
| 485    | No file  | `a1ca538dc20b`  |
| 478    | No file  | `a1ca538dc20b`  |
| 472    | No file  | `a1ca538dc20b`  |
| 466    | No file  | `a1ca538dc20b`  |
| 457    | No file  | `a1ca538dc20b`  |
| 452    | No file  | `a1ca538dc20b`  |
| 449    | No file  | `a1ca538dc20b`  |
| 435    | No file  | `a1ca538dc20b`  |

<!-- versions:end -->

## Companion Files

None. The rows have a fixed size and are read in file order;
`exceptionskillcooltimewidgetoffset.dbss` (below) is not needed. Skill
names come from LOC type 10 and class names from LOC type 21.

The skill key is the one shared by the whole skill cluster; see
[`skill.dbss` Skill Keys](skill_dbss.md#skill-keys). All multi-byte values
are little-endian.

## Layout 1

### File Layout

A `PABR` table of fixed rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset      | Type       | Field        | Notes                                       |
| ----------- | ---------- | ------------ | ------------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                      |
| `+0x04`     | u32        | count        | Number of rows                              |
| `+0x08`     | Row[count] | rows         | See Row                                     |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table            |
| `rows+0x04` | u32        | table_start  | End of the rows (`8 + 20 * count`)          |
| `rows+0x08` | u32        | zero         | Always `0`                                  |

### Row (20 bytes)

| Offset  | Type | Field                 | Notes                                                                    |
| ------- | ---- | --------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | skill_key_from        | `SkillNoFrom << 16 \| 1`: the skill whose slot is replaced; unique       |
| `+0x04` | u64  | class_mask            | Bit `n` set for class type `n` of the `ClassType` list                   |
| `+0x0C` | u32  | skill_key_to          | `SkillNoTo << 16 \| 1`: the skill shown in the slot                      |
| `+0x10` | u32  | skill_learn_check_key | `SkillLearnCheckNo << 16 \| 1`                                           |

Every key on clients 1784 and 3474 has level `1`, and every class mask one
bit: `0x10` Ranger, `0x100` Sorceress, `0x200` Nova, `0x1000` Berserker,
`0x200000` Maehwa, `0x1000000` Valkyrie.

### `exceptionskillcooltimewidgetoffset.dbss`

A bare index: no `PABR` magic and no trailer. Read by
`parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type             | Field | Notes                                          |
| ------- | ---------------- | ----- | ---------------------------------------------- |
| `+0x00` | u32              | count | Equals the main file's `count`                 |
| `+0x04` | Index Row[count] | rows  | See Index Row                                  |

### Index Row (12 bytes)

| Offset  | Type | Field          | Notes                                                       |
| ------- | ---- | -------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | skill_key_from | Key of the row it points at                                 |
| `+0x04` | u32  | offset         | Start of that row in the main file, at its `skill_key_from` |
| `+0x08` | u32  | size           | `20`, the whole row                                         |

On clients 1784 and 3474 the index rows run in reverse file order and each
points at the row with its key.

## Field Names

The names are the columns of the `SetCoolTimeWidget` sheet of a private
server's `DataSheets.bexcel` on client 1784: `ClassType`, `SkillNoFrom`,
`SkillNoTo`, `SkillLearnCheckNo` and `ContentsOption`. Its 7 rows match the
7 rows of the official client 1784 file in every stored column, and client
3474 shares 3 of them (`5831`, `1209`, `94`) unchanged; its other 3 rows are
new. The server dump of the same private server holds the RTTI names
`ExceptionSkillCoolTimeWidgetStaticStatus` and
`ExceptionSkillCoolTimeWidgetStaticStatusManager`.

Its loader, `Load_SetCoolTimeWidget` (VA `0x140a21df0`), fixes the widths
and the order:

- `SkillNoFrom`, `SkillNoTo` and `SkillLearnCheckNo` are read as int64 and
  each stored as the u16 skill number above a u16 level `1`, the skill key.
- `ClassType` is a delimited list. Each value is parsed as u32 and, when
  below `0x33`, sets bit `value` of a 64-bit mask.
- `ContentsOption` is a list of contents option values (`1369` to `1475`
  in the sheet). The loader skips a row whose list fails its contents
  option check; the file has no column for them.

The client 519 tables of a private server and the 2016 PDB have no such
table.

## Notes

- `ToClient_checkExceptionSkillSetting()` runs before the window fills its
  list, and the Lua reads the shown skill through
  `getSkillStaticStatus(skillNo, 1):getExceptionSkillCoolTime()`, the level 1
  skill that `skill_key_from` names. The Lua never reads the class mask or
  the learn check skill; the client checks them before it answers.
- The 1784 rows the 3474 file drops are the Maehwa and Valkyrie rows; their
  `ContentsOption` values in the sheet are `1373` and `1374`.

## Open Questions

### What the Learn Check Skill Gates

The column name says the client checks whether `SkillLearnCheckNo` is
learned, and every such skill is a Succession or Prime skill of the row's
class. Whether the swap happens only with that skill learned, or the skill
is checked for another reason, is not in the Lua; the check is inside
`ToClient_checkExceptionSkillSetting()` or `getExceptionSkillCoolTime()`
in the client.
