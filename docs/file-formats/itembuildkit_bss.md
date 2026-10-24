# `itembuildkit.bss` Format

## Purpose

The siege build kits: per kit item the structures it can place in a Node
or Conquest War (fences, barricades, the fort and command post annexes),
each with the condition script that allows it, a contents event, its icon
and its Korean description. Clients 1784 and 3482 have one kit, item 59791
`[Guild] Node/Conquest War Annex Assembly Tool`. The siege installation
window (`panel_house_installationmode_siege_all_1.luac`) lists the
structures with `ToClient_getSiegeInstallableListSize()` and
`ToClient_getSiegeInstallableListByIndex(index)` and places one with
`ToClient_requestSiegeInstallationStart(itemEnchantKey, characterKey)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records   | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | --------- | --------- |
| 3      | 2507 and later | 3483    | `itembuildkit.bss` | 41,439 | 103 Entry | 35        |
| 2      | 1704 to 2503   | 2503    | `itembuildkit.bss` | 56,950 | 56 Entry  | 26        |
| 1      | 1680 to 1698   | 1698    | `itembuildkit.bss` | 2,770  | 56 Entry  | 22        |

| Layout | File               | Known             | Unknown      |
| ------ | ------------------ | ----------------- | ------------ |
| 3      | `itembuildkit.bss` | 40,512 B (97.8%)  | 927 B (2.2%) |
| 2      | `itembuildkit.bss` | 56,950 B (100.0%) | 0 B (0.0%)   |
| 1      | `itembuildkit.bss` | 2,770 B (100.0%)  | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `a3d7411f9eee`  |
| 3482   | Layout 3 | `a3d7411f9eee`  |
| 3474   | Layout 3 | `a3d7411f9eee`  |
| 3473   | Layout 3 | `a3d7411f9eee`  |
| 3464   | Layout 3 | `a3d7411f9eee`  |
| 3458   | Layout 3 | `a3d7411f9eee`  |
| 3454   | Layout 3 | `a3d7411f9eee`  |
| 3444   | Layout 3 | `a3d7411f9eee`  |
| 3435   | Layout 3 | `a3d7411f9eee`  |
| 3426   | Layout 3 | `a3d7411f9eee`  |
| 3418   | Layout 3 | `a3d7411f9eee`  |
| 3412   | Layout 3 | `a3d7411f9eee`  |
| 3402   | Layout 3 | `a3d7411f9eee`  |
| 3396   | Layout 3 | `a3d7411f9eee`  |
| 3387   | Layout 3 | `a3d7411f9eee`  |
| 3381   | Layout 3 | `a3d7411f9eee`  |
| 3373   | Layout 3 | `a3d7411f9eee`  |
| 3364   | Layout 3 | `a3d7411f9eee`  |
| 3356   | Layout 3 | `a3d7411f9eee`  |
| 3349   | Layout 3 | `a3d7411f9eee`  |
| 3342   | Layout 3 | `a3d7411f9eee`  |
| 3335   | Layout 3 | `a3d7411f9eee`  |
| 3326   | Layout 3 | `a3d7411f9eee`  |
| 3321   | Layout 3 | `a3d7411f9eee`  |
| 3314   | Layout 3 | `a3d7411f9eee`  |
| 3303   | Layout 3 | `a3d7411f9eee`  |
| 3302   | Layout 3 | `a3d7411f9eee`  |
| 3293   | Layout 3 | `a3d7411f9eee`  |
| 3283   | Layout 3 | `a3d7411f9eee`  |
| 3275   | Layout 3 | `a3d7411f9eee`  |
| 3267   | Layout 3 | `a3d7411f9eee`  |
| 3258   | Layout 3 | `a3d7411f9eee`  |
| 3251   | Layout 3 | `a3d7411f9eee`  |
| 3242   | Layout 3 | `a3d7411f9eee`  |
| 3235   | Layout 3 | `a3d7411f9eee`  |
| 3229   | Layout 3 | `a3d7411f9eee`  |
| 3212   | Layout 3 | `a3d7411f9eee`  |
| 3203   | Layout 3 | `a3d7411f9eee`  |
| 3193   | Layout 3 | `a3d7411f9eee`  |
| 3186   | Layout 3 | `a3d7411f9eee`  |
| 3177   | Layout 3 | `a3d7411f9eee`  |
| 3169   | Layout 3 | `a3d7411f9eee`  |
| 3158   | Layout 3 | `a3d7411f9eee`  |
| 3151   | Layout 3 | `a3d7411f9eee`  |
| 3144   | Layout 3 | `a3d7411f9eee`  |
| 3133   | Layout 3 | `a3d7411f9eee`  |
| 3125   | Layout 3 | `a3d7411f9eee`  |
| 3118   | Layout 3 | `a3d7411f9eee`  |
| 3111   | Layout 3 | `a3d7411f9eee`  |
| 3103   | Layout 3 | `a3d7411f9eee`  |
| 3095   | Layout 3 | `a3d7411f9eee`  |
| 3086   | Layout 3 | `a3d7411f9eee`  |
| 3072   | Layout 3 | `a3d7411f9eee`  |
| 3062   | Layout 3 | `a3d7411f9eee`  |
| 3052   | Layout 3 | `a3d7411f9eee`  |
| 3045   | Layout 3 | `a3d7411f9eee`  |
| 3037   | Layout 3 | `a3d7411f9eee`  |
| 3030   | Layout 3 | `a3d7411f9eee`  |
| 3021   | Layout 3 | `a3d7411f9eee`  |
| 3012   | Layout 3 | `a3d7411f9eee`  |
| 3002   | Layout 3 | `a3d7411f9eee`  |
| 2995   | Layout 3 | `a3d7411f9eee`  |
| 2987   | Layout 3 | `a3d7411f9eee`  |
| 2978   | Layout 3 | `a3d7411f9eee`  |
| 2970   | Layout 3 | `a3d7411f9eee`  |
| 2959   | Layout 3 | `a3d7411f9eee`  |
| 2951   | Layout 3 | `a3d7411f9eee`  |
| 2942   | Layout 3 | `a3d7411f9eee`  |
| 2935   | Layout 3 | `a3d7411f9eee`  |
| 2932   | Layout 3 | `a3d7411f9eee`  |
| 2923   | Layout 3 | `a3d7411f9eee`  |
| 2919   | Layout 3 | `a3d7411f9eee`  |
| 2907   | Layout 3 | `a3d7411f9eee`  |
| 2900   | Layout 3 | `a3d7411f9eee`  |
| 2891   | Layout 3 | `a3d7411f9eee`  |
| 2882   | Layout 3 | `a3d7411f9eee`  |
| 2872   | Layout 3 | `a3d7411f9eee`  |
| 2863   | Layout 3 | `a3d7411f9eee`  |
| 2855   | Layout 3 | `a3d7411f9eee`  |
| 2849   | Layout 3 | `a3d7411f9eee`  |
| 2844   | Layout 3 | `a3d7411f9eee`  |
| 2834   | Layout 3 | `a3d7411f9eee`  |
| 2825   | Layout 3 | `a3d7411f9eee`  |
| 2819   | Layout 3 | `a3d7411f9eee`  |
| 2811   | Layout 3 | `a3d7411f9eee`  |
| 2803   | Layout 3 | `a3d7411f9eee`  |
| 2794   | Layout 3 | `a3d7411f9eee`  |
| 2783   | Layout 3 | `a3d7411f9eee`  |
| 2774   | Layout 3 | `a3d7411f9eee`  |
| 2765   | Layout 3 | `a3d7411f9eee`  |
| 2756   | Layout 3 | `a3d7411f9eee`  |
| 2750   | Layout 3 | `a3d7411f9eee`  |
| 2743   | Layout 3 | `a3d7411f9eee`  |
| 2736   | Layout 3 | `a3d7411f9eee`  |
| 2726   | Layout 3 | `a3d7411f9eee`  |
| 2717   | Layout 3 | `a3d7411f9eee`  |
| 2709   | Layout 3 | `a3d7411f9eee`  |
| 2703   | Layout 3 | `a3d7411f9eee`  |
| 2695   | Layout 3 | `a3d7411f9eee`  |
| 2684   | Layout 3 | `a3d7411f9eee`  |
| 2672   | Layout 3 | `a3d7411f9eee`  |
| 2665   | Layout 3 | `a3d7411f9eee`  |
| 2657   | Layout 3 | `a3d7411f9eee`  |
| 2649   | Layout 3 | `a3d7411f9eee`  |
| 2644   | Layout 3 | `a3d7411f9eee`  |
| 2637   | Layout 3 | `a3d7411f9eee`  |
| 2629   | Layout 3 | `a3d7411f9eee`  |
| 2619   | Layout 3 | `a3d7411f9eee`  |
| 2612   | Layout 3 | `a3d7411f9eee`  |
| 2606   | Layout 3 | `a3d7411f9eee`  |
| 2602   | Layout 3 | `a3d7411f9eee`  |
| 2601   | Layout 3 | `a3d7411f9eee`  |
| 2592   | Layout 3 | `a3d7411f9eee`  |
| 2583   | Layout 3 | `a3d7411f9eee`  |
| 2575   | Layout 3 | `a3d7411f9eee`  |
| 2567   | Layout 3 | `a3d7411f9eee`  |
| 2560   | Layout 3 | `a3d7411f9eee`  |
| 2553   | Layout 3 | `a3d7411f9eee`  |
| 2545   | Layout 3 | `a3d7411f9eee`  |
| 2538   | Layout 3 | `a3d7411f9eee`  |
| 2529   | Layout 3 | `a3d7411f9eee`  |
| 2519   | Layout 3 | `a3d7411f9eee`  |
| 2513   | Layout 3 | `a3d7411f9eee`  |
| 2510   | Layout 3 | `a3d7411f9eee`  |
| 2507   | Layout 3 | `a3d7411f9eee`  |
| 2503   | Layout 2 | `a3d7411f9eee`  |
| 2498   | Layout 2 | `a3d7411f9eee`  |
| 2492   | Layout 2 | `a3d7411f9eee`  |
| 2487   | Layout 2 | `a3d7411f9eee`  |
| 2480   | Layout 2 | `a3d7411f9eee`  |
| 2474   | Layout 2 | `a3d7411f9eee`  |
| 2468   | Layout 2 | `a3d7411f9eee`  |
| 2460   | Layout 2 | `a3d7411f9eee`  |
| 2453   | Layout 2 | `a3d7411f9eee`  |
| 2444   | Layout 2 | `a3d7411f9eee`  |
| 2438   | Layout 2 | `a3d7411f9eee`  |
| 2434   | Layout 2 | `a3d7411f9eee`  |
| 2429   | Layout 2 | `a3d7411f9eee`  |
| 2421   | Layout 2 | `a3d7411f9eee`  |
| 2414   | Layout 2 | `a3d7411f9eee`  |
| 2407   | Layout 2 | `a3d7411f9eee`  |
| 2401   | Layout 2 | `a3d7411f9eee`  |
| 2397   | Layout 2 | `a3d7411f9eee`  |
| 2393   | Layout 2 | `a3d7411f9eee`  |
| 2384   | Layout 2 | `a3d7411f9eee`  |
| 2378   | Layout 2 | `a3d7411f9eee`  |
| 2372   | Layout 2 | `a3d7411f9eee`  |
| 2358   | Layout 2 | `a3d7411f9eee`  |
| 2352   | Layout 2 | `a3d7411f9eee`  |
| 2347   | Layout 2 | `a3d7411f9eee`  |
| 2343   | Layout 2 | `a3d7411f9eee`  |
| 2335   | Layout 2 | `a3d7411f9eee`  |
| 2327   | Layout 2 | `a3d7411f9eee`  |
| 2324   | Layout 2 | `a3d7411f9eee`  |
| 2319   | Layout 2 | `a3d7411f9eee`  |
| 2313   | Layout 2 | `a3d7411f9eee`  |
| 2308   | Layout 2 | `a3d7411f9eee`  |
| 2302   | Layout 2 | `a3d7411f9eee`  |
| 2295   | Layout 2 | `a3d7411f9eee`  |
| 2290   | Layout 2 | `a3d7411f9eee`  |
| 2284   | Layout 2 | `a3d7411f9eee`  |
| 2276   | Layout 2 | `a3d7411f9eee`  |
| 2269   | Layout 2 | `a3d7411f9eee`  |
| 2259   | Layout 2 | `a3d7411f9eee`  |
| 2250   | Layout 2 | `a3d7411f9eee`  |
| 2243   | Layout 2 | `a3d7411f9eee`  |
| 2235   | Layout 2 | `a3d7411f9eee`  |
| 2229   | Layout 2 | `a3d7411f9eee`  |
| 2224   | Layout 2 | `a3d7411f9eee`  |
| 2218   | Layout 2 | `a3d7411f9eee`  |
| 2215   | Layout 2 | `a3d7411f9eee`  |
| 2207   | Layout 2 | `a3d7411f9eee`  |
| 2203   | Layout 2 | `a3d7411f9eee`  |
| 2196   | Layout 2 | `a3d7411f9eee`  |
| 2192   | Layout 2 | `a3d7411f9eee`  |
| 2189   | Layout 2 | `a3d7411f9eee`  |
| 2183   | Layout 2 | `a3d7411f9eee`  |
| 2179   | Layout 2 | `a3d7411f9eee`  |
| 2171   | Layout 2 | `a3d7411f9eee`  |
| 2163   | Layout 2 | `a3d7411f9eee`  |
| 2156   | Layout 2 | `a3d7411f9eee`  |
| 2151   | Layout 2 | `a3d7411f9eee`  |
| 2147   | Layout 2 | `a3d7411f9eee`  |
| 2142   | Layout 2 | `a3d7411f9eee`  |
| 2138   | Layout 2 | `a3d7411f9eee`  |
| 2134   | Layout 2 | `a3d7411f9eee`  |
| 2130   | Layout 2 | `a3d7411f9eee`  |
| 2122   | Layout 2 | `a3d7411f9eee`  |
| 2107   | Layout 2 | `a3d7411f9eee`  |
| 2098   | Layout 2 | `a3d7411f9eee`  |
| 2089   | Layout 2 | `a3d7411f9eee`  |
| 2081   | Layout 2 | `a3d7411f9eee`  |
| 2073   | Layout 2 | `a3d7411f9eee`  |
| 2067   | Layout 2 | `a3d7411f9eee`  |
| 2063   | Layout 2 | `a3d7411f9eee`  |
| 2059   | Layout 2 | `a3d7411f9eee`  |
| 2052   | Layout 2 | `a3d7411f9eee`  |
| 2044   | Layout 2 | `a3d7411f9eee`  |
| 2039   | Layout 2 | `a3d7411f9eee`  |
| 2032   | Layout 2 | `a3d7411f9eee`  |
| 2025   | Layout 2 | `a3d7411f9eee`  |
| 2011   | Layout 2 | `a3d7411f9eee`  |
| 2005   | Layout 2 | `a3d7411f9eee`  |
| 2000   | Layout 2 | `a3d7411f9eee`  |
| 1996   | Layout 2 | `a3d7411f9eee`  |
| 1991   | Layout 2 | `a3d7411f9eee`  |
| 1985   | Layout 2 | `a3d7411f9eee`  |
| 1980   | Layout 2 | `a3d7411f9eee`  |
| 1969   | Layout 2 | `a3d7411f9eee`  |
| 1964   | Layout 2 | `a3d7411f9eee`  |
| 1958   | Layout 2 | `a3d7411f9eee`  |
| 1950   | Layout 2 | `a3d7411f9eee`  |
| 1945   | Layout 2 | `a3d7411f9eee`  |
| 1937   | Layout 2 | `a3d7411f9eee`  |
| 1933   | Layout 2 | `a3d7411f9eee`  |
| 1927   | Layout 2 | `a3d7411f9eee`  |
| 1921   | Layout 2 | `a3d7411f9eee`  |
| 1914   | Layout 2 | `a3d7411f9eee`  |
| 1908   | Layout 2 | `a3d7411f9eee`  |
| 1897   | Layout 2 | `a3d7411f9eee`  |
| 1892   | Layout 2 | `a3d7411f9eee`  |
| 1886   | Layout 2 | `a3d7411f9eee`  |
| 1881   | Layout 2 | `a3d7411f9eee`  |
| 1871   | Layout 2 | `a3d7411f9eee`  |
| 1866   | Layout 2 | `a3d7411f9eee`  |
| 1862   | Layout 2 | `a3d7411f9eee`  |
| 1854   | Layout 2 | `a3d7411f9eee`  |
| 1846   | Layout 2 | `a3d7411f9eee`  |
| 1838   | Layout 2 | `a3d7411f9eee`  |
| 1832   | Layout 2 | `a3d7411f9eee`  |
| 1826   | Layout 2 | `a3d7411f9eee`  |
| 1822   | Layout 2 | `a3d7411f9eee`  |
| 1818   | Layout 2 | `a3d7411f9eee`  |
| 1804   | Layout 2 | `a3d7411f9eee`  |
| 1794   | Layout 2 | `a3d7411f9eee`  |
| 1790   | Layout 2 | `a3d7411f9eee`  |
| 1784   | Layout 2 | `a3d7411f9eee`  |
| 1774   | Layout 2 | `a3d7411f9eee`  |
| 1771   | Layout 2 | `a3d7411f9eee`  |
| 1762   | Layout 2 | `a3d7411f9eee`  |
| 1759   | Layout 2 | `a3d7411f9eee`  |
| 1754   | Layout 2 | `a3d7411f9eee`  |
| 1749   | Layout 2 | `a3d7411f9eee`  |
| 1743   | Layout 2 | `a3d7411f9eee`  |
| 1737   | Layout 2 | `a3d7411f9eee`  |
| 1731   | Layout 2 | `a3d7411f9eee`  |
| 1725   | Layout 2 | `a3d7411f9eee`  |
| 1717   | Layout 2 | `a3d7411f9eee`  |
| 1710   | Layout 2 | `a3d7411f9eee`  |
| 1704   | Layout 2 | `a3d7411f9eee`  |
| 1698   | Layout 1 | `a3d7411f9eee`  |
| 1690   | Layout 1 | `a3d7411f9eee`  |
| 1685   | Layout 1 | `a3d7411f9eee`  |
| 1680   | Layout 1 | `a3d7411f9eee`  |
| 1674   | No file  | `a3d7411f9eee`  |
| 1668   | No file  | `a3d7411f9eee`  |
| 1659   | No file  | `a3d7411f9eee`  |
| 1649   | No file  | `a3d7411f9eee`  |
| 1642   | No file  | `a3d7411f9eee`  |
| 1636   | No file  | `a3d7411f9eee`  |
| 1628   | No file  | `a3d7411f9eee`  |
| 1622   | No file  | `a3d7411f9eee`  |
| 1614   | No file  | `a3d7411f9eee`  |
| 1608   | No file  | `a3d7411f9eee`  |
| 1602   | No file  | `a3d7411f9eee`  |
| 1598   | No file  | `a3d7411f9eee`  |
| 1594   | No file  | `a3d7411f9eee`  |
| 1590   | No file  | `a3d7411f9eee`  |
| 1587   | No file  | `a3d7411f9eee`  |
| 1584   | No file  | `a3d7411f9eee`  |
| 1579   | No file  | `a3d7411f9eee`  |
| 1572   | No file  | `a3d7411f9eee`  |
| 1565   | No file  | `a3d7411f9eee`  |
| 1559   | No file  | `a3d7411f9eee`  |
| 1554   | No file  | `a3d7411f9eee`  |
| 1547   | No file  | `a3d7411f9eee`  |
| 1537   | No file  | `a3d7411f9eee`  |
| 1529   | No file  | `a3d7411f9eee`  |
| 1524   | No file  | `a3d7411f9eee`  |
| 1519   | No file  | `a3d7411f9eee`  |
| 1509   | No file  | `a3d7411f9eee`  |
| 1506   | No file  | `a3d7411f9eee`  |
| 1504   | No file  | `a3d7411f9eee`  |
| 1500   | No file  | `a3d7411f9eee`  |
| 1493   | No file  | `a3d7411f9eee`  |
| 1489   | No file  | `a3d7411f9eee`  |
| 1485   | No file  | `a3d7411f9eee`  |
| 1481   | No file  | `a3d7411f9eee`  |
| 1474   | No file  | `a3d7411f9eee`  |
| 1466   | No file  | `a3d7411f9eee`  |
| 1462   | No file  | `a3d7411f9eee`  |
| 1459   | No file  | `a3d7411f9eee`  |
| 1453   | No file  | `a3d7411f9eee`  |
| 1450   | No file  | `a3d7411f9eee`  |
| 1445   | No file  | `a3d7411f9eee`  |
| 1439   | No file  | `a3d7411f9eee`  |
| 1433   | No file  | `a3d7411f9eee`  |
| 1430   | No file  | `a3d7411f9eee`  |
| 1426   | No file  | `a3d7411f9eee`  |
| 1421   | No file  | `a3d7411f9eee`  |
| 1417   | No file  | `a3d7411f9eee`  |
| 1416   | No file  | `a3d7411f9eee`  |
| 1409   | No file  | `a3d7411f9eee`  |
| 1405   | No file  | `a3d7411f9eee`  |
| 1401   | No file  | `a3d7411f9eee`  |
| 1396   | No file  | `a3d7411f9eee`  |
| 1391   | No file  | `a3d7411f9eee`  |
| 1390   | No file  | `a3d7411f9eee`  |
| 1386   | No file  | `a3d7411f9eee`  |
| 1381   | No file  | `a3d7411f9eee`  |
| 1379   | No file  | `a3d7411f9eee`  |
| 1372   | No file  | `a3d7411f9eee`  |
| 1366   | No file  | `a3d7411f9eee`  |
| 1364   | No file  | `a3d7411f9eee`  |
| 1363   | No file  | `a3d7411f9eee`  |
| 1360   | No file  | `a3d7411f9eee`  |
| 1358   | No file  | `a3d7411f9eee`  |
| 1355   | No file  | `a3d7411f9eee`  |
| 1351   | No file  | `a3d7411f9eee`  |
| 1348   | No file  | `a3d7411f9eee`  |
| 1346   | No file  | `a3d7411f9eee`  |
| 1341   | No file  | `a3d7411f9eee`  |
| 1340   | No file  | `a3d7411f9eee`  |
| 1338   | No file  | `a3d7411f9eee`  |
| 1335   | No file  | `a3d7411f9eee`  |
| 1333   | No file  | `a3d7411f9eee`  |
| 1329   | No file  | `a3d7411f9eee`  |
| 1327   | No file  | `a3d7411f9eee`  |
| 1324   | No file  | `a3d7411f9eee`  |
| 1321   | No file  | `a3d7411f9eee`  |
| 1319   | No file  | `a3d7411f9eee`  |
| 1318   | No file  | `a3d7411f9eee`  |
| 1316   | No file  | `a3d7411f9eee`  |
| 1313   | No file  | `a3d7411f9eee`  |
| 1311   | No file  | `a3d7411f9eee`  |
| 1309   | No file  | `a3d7411f9eee`  |
| 1304   | No file  | `a3d7411f9eee`  |
| 1292   | No file  | `a3d7411f9eee`  |
| 1286   | No file  | `a3d7411f9eee`  |
| 1280   | No file  | `a3d7411f9eee`  |
| 1276   | No file  | `a3d7411f9eee`  |
| 1267   | No file  | `a3d7411f9eee`  |
| 1261   | No file  | `a3d7411f9eee`  |
| 1256   | No file  | `a3d7411f9eee`  |
| 1250   | No file  | `a3d7411f9eee`  |
| 1246   | No file  | `a3d7411f9eee`  |
| 1239   | No file  | `a3d7411f9eee`  |
| 1230   | No file  | `a3d7411f9eee`  |
| 1226   | No file  | `a3d7411f9eee`  |
| 1220   | No file  | `a3d7411f9eee`  |
| 1217   | No file  | `a3d7411f9eee`  |
| 1211   | No file  | `a3d7411f9eee`  |
| 1210   | No file  | `a3d7411f9eee`  |
| 1208   | No file  | `a3d7411f9eee`  |
| 1203   | No file  | `a3d7411f9eee`  |
| 1197   | No file  | `a3d7411f9eee`  |
| 1194   | No file  | `a3d7411f9eee`  |
| 1192   | No file  | `a3d7411f9eee`  |
| 1187   | No file  | `a3d7411f9eee`  |
| 1183   | No file  | `a3d7411f9eee`  |
| 1177   | No file  | `a3d7411f9eee`  |
| 1173   | No file  | `a3d7411f9eee`  |
| 1167   | No file  | `a3d7411f9eee`  |
| 1164   | No file  | `a3d7411f9eee`  |
| 1156   | No file  | `a3d7411f9eee`  |
| 1149   | No file  | `a3d7411f9eee`  |
| 1144   | No file  | `a3d7411f9eee`  |
| 1137   | No file  | `a3d7411f9eee`  |
| 1132   | No file  | `a3d7411f9eee`  |
| 1127   | No file  | `a3d7411f9eee`  |
| 1122   | No file  | `a3d7411f9eee`  |
| 1118   | No file  | `a3d7411f9eee`  |
| 1114   | No file  | `a3d7411f9eee`  |
| 1109   | No file  | `a3d7411f9eee`  |
| 1102   | No file  | `a3d7411f9eee`  |
| 1096   | No file  | `a3d7411f9eee`  |
| 1088   | No file  | `a3d7411f9eee`  |
| 1081   | No file  | `a3d7411f9eee`  |
| 1076   | No file  | `a3d7411f9eee`  |
| 1069   | No file  | `a3d7411f9eee`  |
| 1064   | No file  | `a3d7411f9eee`  |
| 1058   | No file  | `a3d7411f9eee`  |
| 1051   | No file  | `a3d7411f9eee`  |
| 1044   | No file  | `a3d7411f9eee`  |
| 1036   | No file  | `a3d7411f9eee`  |
| 1026   | No file  | `a3d7411f9eee`  |
| 1016   | No file  | `a3d7411f9eee`  |
| 1009   | No file  | `a3d7411f9eee`  |
| 1005   | No file  | `a3d7411f9eee`  |
| 1000   | No file  | `a3d7411f9eee`  |
| 998    | No file  | `a3d7411f9eee`  |
| 990    | No file  | `a3d7411f9eee`  |
| 979    | No file  | `a3d7411f9eee`  |
| 972    | No file  | `a3d7411f9eee`  |
| 963    | No file  | `a3d7411f9eee`  |
| 955    | No file  | `a3d7411f9eee`  |
| 946    | No file  | `a3d7411f9eee`  |
| 938    | No file  | `a3d7411f9eee`  |
| 927    | No file  | `a3d7411f9eee`  |
| 911    | No file  | `a3d7411f9eee`  |
| 904    | No file  | `a3d7411f9eee`  |
| 899    | No file  | `a3d7411f9eee`  |
| 894    | No file  | `a3d7411f9eee`  |
| 885    | No file  | `a3d7411f9eee`  |
| 879    | No file  | `a3d7411f9eee`  |
| 872    | No file  | `a3d7411f9eee`  |
| 864    | No file  | `a3d7411f9eee`  |
| 855    | No file  | `a3d7411f9eee`  |
| 853    | No file  | `a3d7411f9eee`  |
| 845    | No file  | `a3d7411f9eee`  |
| 837    | No file  | `a3d7411f9eee`  |
| 829    | No file  | `a3d7411f9eee`  |
| 822    | No file  | `a3d7411f9eee`  |
| 814    | No file  | `a3d7411f9eee`  |
| 805    | No file  | `a3d7411f9eee`  |
| 794    | No file  | `a3d7411f9eee`  |
| 787    | No file  | `a3d7411f9eee`  |
| 780    | No file  | `a3d7411f9eee`  |
| 771    | No file  | `a3d7411f9eee`  |
| 760    | No file  | `a3d7411f9eee`  |
| 748    | No file  | `a3d7411f9eee`  |
| 741    | No file  | `a3d7411f9eee`  |
| 736    | No file  | `a3d7411f9eee`  |
| 731    | No file  | `a3d7411f9eee`  |
| 723    | No file  | `a3d7411f9eee`  |
| 711    | No file  | `a3d7411f9eee`  |
| 707    | No file  | `a3d7411f9eee`  |
| 697    | No file  | `a3d7411f9eee`  |
| 689    | No file  | `a3d7411f9eee`  |
| 683    | No file  | `a3d7411f9eee`  |
| 678    | No file  | `a3d7411f9eee`  |
| 670    | No file  | `a3d7411f9eee`  |
| 661    | No file  | `a3d7411f9eee`  |
| 656    | No file  | `a3d7411f9eee`  |
| 652    | No file  | `a3d7411f9eee`  |
| 643    | No file  | `a3d7411f9eee`  |
| 637    | No file  | `a3d7411f9eee`  |
| 630    | No file  | `a3d7411f9eee`  |
| 627    | No file  | `a3d7411f9eee`  |
| 621    | No file  | `a3d7411f9eee`  |
| 617    | No file  | `a3d7411f9eee`  |
| 615    | No file  | `a3d7411f9eee`  |
| 606    | No file  | `a3d7411f9eee`  |
| 599    | No file  | `a3d7411f9eee`  |
| 592    | No file  | `a3d7411f9eee`  |
| 586    | No file  | `a3d7411f9eee`  |
| 577    | No file  | `a3d7411f9eee`  |
| 569    | No file  | `a3d7411f9eee`  |
| 561    | No file  | `a3d7411f9eee`  |
| 554    | No file  | `a3d7411f9eee`  |
| 542    | No file  | `a3d7411f9eee`  |
| 532    | No file  | `a3d7411f9eee`  |
| 531    | No file  | `a3d7411f9eee`  |
| 526    | No file  | `a3d7411f9eee`  |
| 521    | No file  | `a3d7411f9eee`  |
| 517    | No file  | `a3d7411f9eee`  |
| 510    | No file  | `a3d7411f9eee`  |
| 508    | No file  | `a3d7411f9eee`  |
| 504    | No file  | `a3d7411f9eee`  |
| 497    | No file  | `a3d7411f9eee`  |
| 491    | No file  | `a3d7411f9eee`  |
| 485    | No file  | `a3d7411f9eee`  |
| 478    | No file  | `a3d7411f9eee`  |
| 472    | No file  | `a3d7411f9eee`  |
| 466    | No file  | `a3d7411f9eee`  |
| 457    | No file  | `a3d7411f9eee`  |
| 452    | No file  | `a3d7411f9eee`  |
| 449    | No file  | `a3d7411f9eee`  |
| 435    | No file  | `a3d7411f9eee`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                      |
| ---------------------------- | -------- | ------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a structure without a row shows as plain text |
| `languagedata_en.loc`        | Optional | Item names (LOC type 0) and structure names (LOC type 6)                  |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field        | Notes                                        |
| ------------------- | -------------- | ------------ | -------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                 |
| `+0x04`             | u32            | kit_count    | Number of kits; `1` on clients 1784 and 3482 |
| `+0x08`             | Kit[kit_count] | kits         | See Kit                                      |
| `kits+0x00`         | String Table   | string_table | See String Table                             |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `kits` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                   |

### Kit (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                       |
| ------- | ------------------ | ----------- | ------------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; 103 on client 3482     |
| `+0x04` | Entry[entry_count] | entries     | See Entry; one per structure the kit places |

### Entry (35 bytes)

| Offset  | Type | Field                 | Notes                                                                                     |
| ------- | ---- | --------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key              | The kit, a packed item key; the same in every entry of a kit                               |
| `+0x04` | u16  | character_key         | The structure placed (`2046` Wooden Fence, `12606` Barricade); unique within a kit          |
| `+0x06` | u32  | use_condition         | Index into `strings`: the condition script (`checksiegetower(0);checkInstallTentLevel(5);`) |
| `+0x0A` | u32  | contents_event_type   | `1` on every entry of clients 1784 and 3482                                                |
| `+0x0E` | u32  | contents_event_param1 | `15000` on every entry of client 1784, `5000` on client 3482                               |
| `+0x12` | u32  | icon_image_file       | Index into `strings`: the icon path (`New_Icon/03_ETC/06_Housing/00056071.dds`)            |
| `+0x16` | u32  | description           | Index into `strings`: the Korean description, with `<PAColor>` tags and `\n` escapes        |
| `+0x1A` | u32  | unknown_1a            | `0`, `30000000` or `50000000` on client 3482; see Open Questions                           |
| `+0x1E` | u32  | unknown_1e            | `0` on every entry of client 3482                                                          |
| `+0x22` | u8   | unknown_22            | `0`, `1` or `2` on client 3482; see Open Questions                                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                       |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; 73 on client 3482                                        |
| `+0x04` | pstr[string_count] | strings      | Condition scripts and descriptions UTF-16LE (`is_wide` 1), icon paths UTF-8; each text stored once |

## Layout 2

The entry ends after `description`. Only the Entry differs from Layout 3.

### Entry (26 bytes)

| Offset  | Type | Field                 | Notes |
| ------- | ---- | --------------------- | ----- |
| `+0x00` | u32  | item_key              |       |
| `+0x04` | u16  | character_key         |       |
| `+0x06` | u32  | use_condition         |       |
| `+0x0A` | u32  | contents_event_type   |       |
| `+0x0E` | u32  | contents_event_param1 |       |
| `+0x12` | u32  | icon_image_file       |       |
| `+0x16` | u32  | description           |       |

## Layout 1

The entry ends after `icon_image_file`: no description. Only the Entry
differs from Layout 2.

### Entry (22 bytes)

| Offset  | Type | Field                 | Notes |
| ------- | ---- | --------------------- | ----- |
| `+0x00` | u32  | item_key              |       |
| `+0x04` | u16  | character_key         |       |
| `+0x06` | u32  | use_condition         |       |
| `+0x0A` | u32  | contents_event_type   |       |
| `+0x0E` | u32  | contents_event_param1 |       |
| `+0x12` | u32  | icon_image_file       |       |

## Field Names

The `SiegeItemInstallation` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `ItemKey`, `CharacterKey`, `UseCondition`,
`ContentsEventType`, `ContentsEventParam1`, `IconImageFile` and
`Description`, one sheet row per entry, in another order than the file.
Matched on (`ItemKey`, `CharacterKey`):

| Field                 | Column                | Same value (client 1784) | Same value (client 3482) |
| --------------------- | --------------------- | ------------------------ | ------------------------ |
| item_key              | `ItemKey`             | 56 of 56                 | 52 of 103                |
| character_key         | `CharacterKey`        | 56 of 56                 | 52 of 52                 |
| use_condition         | `UseCondition`        | 56 of 56                 | 28 of 52                 |
| contents_event_type   | `ContentsEventType`   | 56 of 56                 | 52 of 52                 |
| contents_event_param1 | `ContentsEventParam1` | 56 of 56                 | 0 of 52                  |
| icon_image_file       | `IconImageFile`       | 56 of 56                 | 52 of 52                 |
| description           | `Description`         | 56 of 56                 | 5 of 52                  |

The client 3482 misses are changed conditions and descriptions and the
parameter `5000` in place of `15000`. The sheet has no column for the three
fields Layout 3 adds.

## Notes

- `use_condition` calls `checksiegetower`, `checksiegetowercharacter`,
  `checkInstallTentLevel`, `checkiskingguild` and, on client 3482,
  `checksiege2024groupno`.
- On client 3482, `unknown_1a` is `30000000` on 6 entries and `50000000` on
  9, all of them with `unknown_22` `1`; these 15 entries (characters `12759`
  to `12790`) are the ones whose condition calls `checksiege2024groupno`.
- The handler (`_bss/itembuildkit/`) shows one row per entry: the kit, the
  structure with its name, the condition, the contents event, the icon and
  the description.

## Open Questions

### What the Three Fields Layout 3 Adds Hold

`unknown_1a` (`0`, `30000000`, `50000000`), `unknown_1e` (`0`) and
`unknown_22` (`0`, `1`, `2`) are new on client 2519 and match no sheet
column. `unknown_1a` may be a Silver cost of the 15 newer structures; the
client 3482 Lua reads no cost from the installable list.
