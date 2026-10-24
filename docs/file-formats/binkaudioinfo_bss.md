# `binkaudioinfo.bss` Format

## Purpose

The sound of the Bink movies: per movie (`Goyen`,
`Balenos_Intro_EmmasDream`, the Morning Light cutscenes) the Wwise event
and sound bank that play its audio. The movie name is the stem of the
`.bk2` file under `ui_movie/`, the audio name a `Bink_<movie>` event and a
`bink_<movie>.bnk` bank under `sound2022/windows/<language>/`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes  | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ------ | ------- | --------- |
| 1      | 2073 and later | 3483    | `binkaudioinfo.bss` | 11,349 | 161 Row | 15        |

| Layout | File                | Known            | Unknown      |
| ------ | ------------------- | ---------------- | ------------ |
| 1      | `binkaudioinfo.bss` | 10,866 B (95.7%) | 483 B (4.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `bf2f6ffb4d39`  |
| 3482   | Layout 1             | `bf2f6ffb4d39`  |
| 3474   | Layout 1             | `bf2f6ffb4d39`  |
| 3473   | Layout 1             | `bf2f6ffb4d39`  |
| 3464   | Layout 1             | `bf2f6ffb4d39`  |
| 3458   | Layout 1             | `bf2f6ffb4d39`  |
| 3454   | Layout 1             | `bf2f6ffb4d39`  |
| 3444   | Layout 1             | `bf2f6ffb4d39`  |
| 3435   | Layout 1             | `bf2f6ffb4d39`  |
| 3426   | Layout 1             | `bf2f6ffb4d39`  |
| 3418   | Layout 1             | `bf2f6ffb4d39`  |
| 3412   | Layout 1             | `bf2f6ffb4d39`  |
| 3402   | Layout 1             | `bf2f6ffb4d39`  |
| 3396   | Layout 1             | `bf2f6ffb4d39`  |
| 3387   | Layout 1             | `bf2f6ffb4d39`  |
| 3381   | Layout 1             | `bf2f6ffb4d39`  |
| 3373   | Layout 1             | `bf2f6ffb4d39`  |
| 3364   | Layout 1             | `bf2f6ffb4d39`  |
| 3356   | Layout 1             | `bf2f6ffb4d39`  |
| 3349   | Layout 1             | `bf2f6ffb4d39`  |
| 3342   | Layout 1             | `bf2f6ffb4d39`  |
| 3335   | Layout 1             | `bf2f6ffb4d39`  |
| 3326   | Layout 1             | `bf2f6ffb4d39`  |
| 3321   | Layout 1             | `bf2f6ffb4d39`  |
| 3314   | Layout 1             | `bf2f6ffb4d39`  |
| 3303   | Layout 1             | `bf2f6ffb4d39`  |
| 3302   | Layout 1             | `bf2f6ffb4d39`  |
| 3293   | Layout 1             | `bf2f6ffb4d39`  |
| 3283   | Layout 1             | `bf2f6ffb4d39`  |
| 3275   | Layout 1             | `bf2f6ffb4d39`  |
| 3267   | Layout 1             | `bf2f6ffb4d39`  |
| 3258   | Layout 1             | `bf2f6ffb4d39`  |
| 3251   | Layout 1             | `bf2f6ffb4d39`  |
| 3242   | Layout 1             | `bf2f6ffb4d39`  |
| 3235   | Layout 1             | `bf2f6ffb4d39`  |
| 3229   | Layout 1             | `bf2f6ffb4d39`  |
| 3212   | Layout 1             | `bf2f6ffb4d39`  |
| 3203   | Layout 1             | `bf2f6ffb4d39`  |
| 3193   | Layout 1             | `bf2f6ffb4d39`  |
| 3186   | Layout 1             | `bf2f6ffb4d39`  |
| 3177   | Layout 1             | `bf2f6ffb4d39`  |
| 3169   | Layout 1             | `bf2f6ffb4d39`  |
| 3158   | Layout 1             | `bf2f6ffb4d39`  |
| 3151   | Layout 1             | `bf2f6ffb4d39`  |
| 3144   | Layout 1             | `bf2f6ffb4d39`  |
| 3133   | Layout 1             | `bf2f6ffb4d39`  |
| 3125   | Layout 1             | `bf2f6ffb4d39`  |
| 3118   | Layout 1             | `bf2f6ffb4d39`  |
| 3111   | Layout 1             | `bf2f6ffb4d39`  |
| 3103   | Layout 1             | `bf2f6ffb4d39`  |
| 3095   | Layout 1             | `bf2f6ffb4d39`  |
| 3086   | Layout 1             | `bf2f6ffb4d39`  |
| 3072   | Layout 1             | `bf2f6ffb4d39`  |
| 3062   | Layout 1             | `bf2f6ffb4d39`  |
| 3052   | Layout 1             | `bf2f6ffb4d39`  |
| 3045   | Layout 1             | `bf2f6ffb4d39`  |
| 3037   | Layout 1             | `bf2f6ffb4d39`  |
| 3030   | Layout 1             | `bf2f6ffb4d39`  |
| 3021   | Layout 1             | `bf2f6ffb4d39`  |
| 3012   | Layout 1             | `bf2f6ffb4d39`  |
| 3002   | Layout 1             | `bf2f6ffb4d39`  |
| 2995   | Layout 1             | `bf2f6ffb4d39`  |
| 2987   | Layout 1             | `bf2f6ffb4d39`  |
| 2978   | Layout 1             | `bf2f6ffb4d39`  |
| 2970   | Layout 1             | `bf2f6ffb4d39`  |
| 2959   | Layout 1             | `bf2f6ffb4d39`  |
| 2951   | Layout 1             | `bf2f6ffb4d39`  |
| 2942   | Layout 1             | `bf2f6ffb4d39`  |
| 2935   | Layout 1             | `bf2f6ffb4d39`  |
| 2932   | Layout 1             | `bf2f6ffb4d39`  |
| 2923   | Layout 1             | `bf2f6ffb4d39`  |
| 2919   | Layout 1             | `bf2f6ffb4d39`  |
| 2907   | Layout 1             | `bf2f6ffb4d39`  |
| 2900   | Layout 1             | `bf2f6ffb4d39`  |
| 2891   | Layout 1             | `bf2f6ffb4d39`  |
| 2882   | Layout 1             | `bf2f6ffb4d39`  |
| 2872   | Layout 1             | `bf2f6ffb4d39`  |
| 2863   | Layout 1             | `bf2f6ffb4d39`  |
| 2855   | Layout 1             | `bf2f6ffb4d39`  |
| 2849   | Layout 1             | `bf2f6ffb4d39`  |
| 2844   | Layout 1             | `bf2f6ffb4d39`  |
| 2834   | Layout 1             | `bf2f6ffb4d39`  |
| 2825   | Layout 1             | `bf2f6ffb4d39`  |
| 2819   | Layout 1             | `bf2f6ffb4d39`  |
| 2811   | Layout 1             | `bf2f6ffb4d39`  |
| 2803   | Layout 1             | `bf2f6ffb4d39`  |
| 2794   | Layout 1             | `bf2f6ffb4d39`  |
| 2783   | Layout 1             | `bf2f6ffb4d39`  |
| 2774   | Layout 1             | `bf2f6ffb4d39`  |
| 2765   | Layout 1             | `bf2f6ffb4d39`  |
| 2756   | Layout 1             | `bf2f6ffb4d39`  |
| 2750   | Layout 1             | `bf2f6ffb4d39`  |
| 2743   | Layout 1             | `bf2f6ffb4d39`  |
| 2736   | Layout 1             | `bf2f6ffb4d39`  |
| 2726   | Layout 1             | `bf2f6ffb4d39`  |
| 2717   | Layout 1             | `bf2f6ffb4d39`  |
| 2709   | Layout 1             | `bf2f6ffb4d39`  |
| 2703   | Layout 1             | `bf2f6ffb4d39`  |
| 2695   | Layout 1             | `bf2f6ffb4d39`  |
| 2684   | Layout 1             | `bf2f6ffb4d39`  |
| 2672   | Layout 1             | `bf2f6ffb4d39`  |
| 2665   | Layout 1             | `bf2f6ffb4d39`  |
| 2657   | Layout 1             | `bf2f6ffb4d39`  |
| 2649   | Layout 1             | `bf2f6ffb4d39`  |
| 2644   | Layout 1             | `bf2f6ffb4d39`  |
| 2637   | Layout 1             | `bf2f6ffb4d39`  |
| 2629   | Layout 1             | `bf2f6ffb4d39`  |
| 2619   | Layout 1             | `bf2f6ffb4d39`  |
| 2612   | Layout 1             | `bf2f6ffb4d39`  |
| 2606   | Layout 1             | `bf2f6ffb4d39`  |
| 2602   | Layout 1             | `bf2f6ffb4d39`  |
| 2601   | Layout 1             | `bf2f6ffb4d39`  |
| 2592   | Layout 1             | `bf2f6ffb4d39`  |
| 2583   | Layout 1             | `bf2f6ffb4d39`  |
| 2575   | Layout 1             | `bf2f6ffb4d39`  |
| 2567   | Layout 1             | `bf2f6ffb4d39`  |
| 2560   | Layout 1             | `bf2f6ffb4d39`  |
| 2553   | Layout 1             | `bf2f6ffb4d39`  |
| 2545   | Layout 1             | `bf2f6ffb4d39`  |
| 2538   | Layout 1             | `bf2f6ffb4d39`  |
| 2529   | Layout 1             | `bf2f6ffb4d39`  |
| 2519   | Layout 1             | `bf2f6ffb4d39`  |
| 2513   | Layout 1             | `bf2f6ffb4d39`  |
| 2510   | Layout 1             | `bf2f6ffb4d39`  |
| 2507   | Layout 1             | `bf2f6ffb4d39`  |
| 2503   | Layout 1             | `bf2f6ffb4d39`  |
| 2498   | Layout 1             | `bf2f6ffb4d39`  |
| 2492   | Layout 1             | `bf2f6ffb4d39`  |
| 2487   | Layout 1             | `bf2f6ffb4d39`  |
| 2480   | Layout 1             | `bf2f6ffb4d39`  |
| 2474   | Layout 1             | `bf2f6ffb4d39`  |
| 2468   | Layout 1             | `bf2f6ffb4d39`  |
| 2460   | Layout 1             | `bf2f6ffb4d39`  |
| 2453   | Layout 1             | `bf2f6ffb4d39`  |
| 2444   | Layout 1             | `bf2f6ffb4d39`  |
| 2438   | Layout 1             | `bf2f6ffb4d39`  |
| 2434   | Layout 1             | `bf2f6ffb4d39`  |
| 2429   | Layout 1             | `bf2f6ffb4d39`  |
| 2421   | Layout 1             | `bf2f6ffb4d39`  |
| 2414   | Layout 1             | `bf2f6ffb4d39`  |
| 2407   | Layout 1             | `bf2f6ffb4d39`  |
| 2401   | Layout 1             | `bf2f6ffb4d39`  |
| 2397   | Layout 1             | `bf2f6ffb4d39`  |
| 2393   | Layout 1             | `bf2f6ffb4d39`  |
| 2384   | Layout 1             | `bf2f6ffb4d39`  |
| 2378   | Layout 1             | `bf2f6ffb4d39`  |
| 2372   | Layout 1             | `bf2f6ffb4d39`  |
| 2358   | Layout 1             | `bf2f6ffb4d39`  |
| 2352   | Layout 1             | `bf2f6ffb4d39`  |
| 2347   | Layout 1             | `bf2f6ffb4d39`  |
| 2343   | Layout 1             | `bf2f6ffb4d39`  |
| 2335   | Layout 1             | `bf2f6ffb4d39`  |
| 2327   | Layout 1             | `bf2f6ffb4d39`  |
| 2324   | Layout 1             | `bf2f6ffb4d39`  |
| 2319   | Layout 1             | `bf2f6ffb4d39`  |
| 2313   | Layout 1             | `bf2f6ffb4d39`  |
| 2308   | Layout 1             | `bf2f6ffb4d39`  |
| 2302   | Layout 1             | `bf2f6ffb4d39`  |
| 2295   | Layout 1             | `bf2f6ffb4d39`  |
| 2290   | Layout 1             | `bf2f6ffb4d39`  |
| 2284   | Layout 1             | `bf2f6ffb4d39`  |
| 2276   | Layout 1             | `bf2f6ffb4d39`  |
| 2269   | Layout 1             | `bf2f6ffb4d39`  |
| 2259   | Layout 1             | `bf2f6ffb4d39`  |
| 2250   | Layout 1             | `bf2f6ffb4d39`  |
| 2243   | Layout 1             | `bf2f6ffb4d39`  |
| 2235   | Layout 1             | `bf2f6ffb4d39`  |
| 2229   | Layout 1             | `bf2f6ffb4d39`  |
| 2224   | Layout 1             | `bf2f6ffb4d39`  |
| 2218   | Layout 1             | `bf2f6ffb4d39`  |
| 2215   | Layout 1             | `bf2f6ffb4d39`  |
| 2207   | Layout 1             | `bf2f6ffb4d39`  |
| 2203   | Layout 1             | `bf2f6ffb4d39`  |
| 2196   | Layout 1             | `bf2f6ffb4d39`  |
| 2192   | Layout 1             | `bf2f6ffb4d39`  |
| 2189   | Layout 1             | `bf2f6ffb4d39`  |
| 2183   | Layout 1             | `bf2f6ffb4d39`  |
| 2179   | Layout 1             | `bf2f6ffb4d39`  |
| 2171   | Layout 1             | `bf2f6ffb4d39`  |
| 2163   | Layout 1             | `bf2f6ffb4d39`  |
| 2156   | Layout 1             | `bf2f6ffb4d39`  |
| 2151   | Layout 1             | `bf2f6ffb4d39`  |
| 2147   | Layout 1             | `bf2f6ffb4d39`  |
| 2142   | Layout 1             | `bf2f6ffb4d39`  |
| 2138   | Layout 1             | `bf2f6ffb4d39`  |
| 2134   | Layout 1             | `bf2f6ffb4d39`  |
| 2130   | Layout 1             | `bf2f6ffb4d39`  |
| 2122   | Layout 1             | `bf2f6ffb4d39`  |
| 2107   | Layout 1             | `bf2f6ffb4d39`  |
| 2098   | Layout 1             | `bf2f6ffb4d39`  |
| 2089   | Layout 1             | `bf2f6ffb4d39`  |
| 2081   | Layout 1             | `bf2f6ffb4d39`  |
| 2073   | Layout 1             | `bf2f6ffb4d39`  |
| 2067   | No documented layout | `bf2f6ffb4d39`  |
| 2063   | No documented layout | `bf2f6ffb4d39`  |
| 2059   | No file              | `bf2f6ffb4d39`  |
| 2052   | No file              | `bf2f6ffb4d39`  |
| 2044   | No file              | `bf2f6ffb4d39`  |
| 2039   | No file              | `bf2f6ffb4d39`  |
| 2032   | No file              | `bf2f6ffb4d39`  |
| 2025   | No file              | `bf2f6ffb4d39`  |
| 2011   | No file              | `bf2f6ffb4d39`  |
| 2005   | No file              | `bf2f6ffb4d39`  |
| 2000   | No file              | `bf2f6ffb4d39`  |
| 1996   | No file              | `bf2f6ffb4d39`  |
| 1991   | No file              | `bf2f6ffb4d39`  |
| 1985   | No file              | `bf2f6ffb4d39`  |
| 1980   | No file              | `bf2f6ffb4d39`  |
| 1969   | No file              | `bf2f6ffb4d39`  |
| 1964   | No file              | `bf2f6ffb4d39`  |
| 1958   | No file              | `bf2f6ffb4d39`  |
| 1950   | No file              | `bf2f6ffb4d39`  |
| 1945   | No file              | `bf2f6ffb4d39`  |
| 1937   | No file              | `bf2f6ffb4d39`  |
| 1933   | No file              | `bf2f6ffb4d39`  |
| 1927   | No file              | `bf2f6ffb4d39`  |
| 1921   | No file              | `bf2f6ffb4d39`  |
| 1914   | No file              | `bf2f6ffb4d39`  |
| 1908   | No file              | `bf2f6ffb4d39`  |
| 1897   | No file              | `bf2f6ffb4d39`  |
| 1892   | No file              | `bf2f6ffb4d39`  |
| 1886   | No file              | `bf2f6ffb4d39`  |
| 1881   | No file              | `bf2f6ffb4d39`  |
| 1871   | No file              | `bf2f6ffb4d39`  |
| 1866   | No file              | `bf2f6ffb4d39`  |
| 1862   | No file              | `bf2f6ffb4d39`  |
| 1854   | No file              | `bf2f6ffb4d39`  |
| 1846   | No file              | `bf2f6ffb4d39`  |
| 1838   | No file              | `bf2f6ffb4d39`  |
| 1832   | No file              | `bf2f6ffb4d39`  |
| 1826   | No file              | `bf2f6ffb4d39`  |
| 1822   | No file              | `bf2f6ffb4d39`  |
| 1818   | No file              | `bf2f6ffb4d39`  |
| 1804   | No file              | `bf2f6ffb4d39`  |
| 1794   | No file              | `bf2f6ffb4d39`  |
| 1790   | No file              | `bf2f6ffb4d39`  |
| 1784   | No file              | `bf2f6ffb4d39`  |
| 1774   | No file              | `bf2f6ffb4d39`  |
| 1771   | No file              | `bf2f6ffb4d39`  |
| 1762   | No file              | `bf2f6ffb4d39`  |
| 1759   | No file              | `bf2f6ffb4d39`  |
| 1754   | No file              | `bf2f6ffb4d39`  |
| 1749   | No file              | `bf2f6ffb4d39`  |
| 1743   | No file              | `bf2f6ffb4d39`  |
| 1737   | No file              | `bf2f6ffb4d39`  |
| 1731   | No file              | `bf2f6ffb4d39`  |
| 1725   | No file              | `bf2f6ffb4d39`  |
| 1717   | No file              | `bf2f6ffb4d39`  |
| 1710   | No file              | `bf2f6ffb4d39`  |
| 1704   | No file              | `bf2f6ffb4d39`  |
| 1698   | No file              | `bf2f6ffb4d39`  |
| 1690   | No file              | `bf2f6ffb4d39`  |
| 1685   | No file              | `bf2f6ffb4d39`  |
| 1680   | No file              | `bf2f6ffb4d39`  |
| 1674   | No file              | `bf2f6ffb4d39`  |
| 1668   | No file              | `bf2f6ffb4d39`  |
| 1659   | No file              | `bf2f6ffb4d39`  |
| 1649   | No file              | `bf2f6ffb4d39`  |
| 1642   | No file              | `bf2f6ffb4d39`  |
| 1636   | No file              | `bf2f6ffb4d39`  |
| 1628   | No file              | `bf2f6ffb4d39`  |
| 1622   | No file              | `bf2f6ffb4d39`  |
| 1614   | No file              | `bf2f6ffb4d39`  |
| 1608   | No file              | `bf2f6ffb4d39`  |
| 1602   | No file              | `bf2f6ffb4d39`  |
| 1598   | No file              | `bf2f6ffb4d39`  |
| 1594   | No file              | `bf2f6ffb4d39`  |
| 1590   | No file              | `bf2f6ffb4d39`  |
| 1587   | No file              | `bf2f6ffb4d39`  |
| 1584   | No file              | `bf2f6ffb4d39`  |
| 1579   | No file              | `bf2f6ffb4d39`  |
| 1572   | No file              | `bf2f6ffb4d39`  |
| 1565   | No file              | `bf2f6ffb4d39`  |
| 1559   | No file              | `bf2f6ffb4d39`  |
| 1554   | No file              | `bf2f6ffb4d39`  |
| 1547   | No file              | `bf2f6ffb4d39`  |
| 1537   | No file              | `bf2f6ffb4d39`  |
| 1529   | No file              | `bf2f6ffb4d39`  |
| 1524   | No file              | `bf2f6ffb4d39`  |
| 1519   | No file              | `bf2f6ffb4d39`  |
| 1509   | No file              | `bf2f6ffb4d39`  |
| 1506   | No file              | `bf2f6ffb4d39`  |
| 1504   | No file              | `bf2f6ffb4d39`  |
| 1500   | No file              | `bf2f6ffb4d39`  |
| 1493   | No file              | `bf2f6ffb4d39`  |
| 1489   | No file              | `bf2f6ffb4d39`  |
| 1485   | No file              | `bf2f6ffb4d39`  |
| 1481   | No file              | `bf2f6ffb4d39`  |
| 1474   | No file              | `bf2f6ffb4d39`  |
| 1466   | No file              | `bf2f6ffb4d39`  |
| 1462   | No file              | `bf2f6ffb4d39`  |
| 1459   | No file              | `bf2f6ffb4d39`  |
| 1453   | No file              | `bf2f6ffb4d39`  |
| 1450   | No file              | `bf2f6ffb4d39`  |
| 1445   | No file              | `bf2f6ffb4d39`  |
| 1439   | No file              | `bf2f6ffb4d39`  |
| 1433   | No file              | `bf2f6ffb4d39`  |
| 1430   | No file              | `bf2f6ffb4d39`  |
| 1426   | No file              | `bf2f6ffb4d39`  |
| 1421   | No file              | `bf2f6ffb4d39`  |
| 1417   | No file              | `bf2f6ffb4d39`  |
| 1416   | No file              | `bf2f6ffb4d39`  |
| 1409   | No file              | `bf2f6ffb4d39`  |
| 1405   | No file              | `bf2f6ffb4d39`  |
| 1401   | No file              | `bf2f6ffb4d39`  |
| 1396   | No file              | `bf2f6ffb4d39`  |
| 1391   | No file              | `bf2f6ffb4d39`  |
| 1390   | No file              | `bf2f6ffb4d39`  |
| 1386   | No file              | `bf2f6ffb4d39`  |
| 1381   | No file              | `bf2f6ffb4d39`  |
| 1379   | No file              | `bf2f6ffb4d39`  |
| 1372   | No file              | `bf2f6ffb4d39`  |
| 1366   | No file              | `bf2f6ffb4d39`  |
| 1364   | No file              | `bf2f6ffb4d39`  |
| 1363   | No file              | `bf2f6ffb4d39`  |
| 1360   | No file              | `bf2f6ffb4d39`  |
| 1358   | No file              | `bf2f6ffb4d39`  |
| 1355   | No file              | `bf2f6ffb4d39`  |
| 1351   | No file              | `bf2f6ffb4d39`  |
| 1348   | No file              | `bf2f6ffb4d39`  |
| 1346   | No file              | `bf2f6ffb4d39`  |
| 1341   | No file              | `bf2f6ffb4d39`  |
| 1340   | No file              | `bf2f6ffb4d39`  |
| 1338   | No file              | `bf2f6ffb4d39`  |
| 1335   | No file              | `bf2f6ffb4d39`  |
| 1333   | No file              | `bf2f6ffb4d39`  |
| 1329   | No file              | `bf2f6ffb4d39`  |
| 1327   | No file              | `bf2f6ffb4d39`  |
| 1324   | No file              | `bf2f6ffb4d39`  |
| 1321   | No file              | `bf2f6ffb4d39`  |
| 1319   | No file              | `bf2f6ffb4d39`  |
| 1318   | No file              | `bf2f6ffb4d39`  |
| 1316   | No file              | `bf2f6ffb4d39`  |
| 1313   | No file              | `bf2f6ffb4d39`  |
| 1311   | No file              | `bf2f6ffb4d39`  |
| 1309   | No file              | `bf2f6ffb4d39`  |
| 1304   | No file              | `bf2f6ffb4d39`  |
| 1292   | No file              | `bf2f6ffb4d39`  |
| 1286   | No file              | `bf2f6ffb4d39`  |
| 1280   | No file              | `bf2f6ffb4d39`  |
| 1276   | No file              | `bf2f6ffb4d39`  |
| 1267   | No file              | `bf2f6ffb4d39`  |
| 1261   | No file              | `bf2f6ffb4d39`  |
| 1256   | No file              | `bf2f6ffb4d39`  |
| 1250   | No file              | `bf2f6ffb4d39`  |
| 1246   | No file              | `bf2f6ffb4d39`  |
| 1239   | No file              | `bf2f6ffb4d39`  |
| 1230   | No file              | `bf2f6ffb4d39`  |
| 1226   | No file              | `bf2f6ffb4d39`  |
| 1220   | No file              | `bf2f6ffb4d39`  |
| 1217   | No file              | `bf2f6ffb4d39`  |
| 1211   | No file              | `bf2f6ffb4d39`  |
| 1210   | No file              | `bf2f6ffb4d39`  |
| 1208   | No file              | `bf2f6ffb4d39`  |
| 1203   | No file              | `bf2f6ffb4d39`  |
| 1197   | No file              | `bf2f6ffb4d39`  |
| 1194   | No file              | `bf2f6ffb4d39`  |
| 1192   | No file              | `bf2f6ffb4d39`  |
| 1187   | No file              | `bf2f6ffb4d39`  |
| 1183   | No file              | `bf2f6ffb4d39`  |
| 1177   | No file              | `bf2f6ffb4d39`  |
| 1173   | No file              | `bf2f6ffb4d39`  |
| 1167   | No file              | `bf2f6ffb4d39`  |
| 1164   | No file              | `bf2f6ffb4d39`  |
| 1156   | No file              | `bf2f6ffb4d39`  |
| 1149   | No file              | `bf2f6ffb4d39`  |
| 1144   | No file              | `bf2f6ffb4d39`  |
| 1137   | No file              | `bf2f6ffb4d39`  |
| 1132   | No file              | `bf2f6ffb4d39`  |
| 1127   | No file              | `bf2f6ffb4d39`  |
| 1122   | No file              | `bf2f6ffb4d39`  |
| 1118   | No file              | `bf2f6ffb4d39`  |
| 1114   | No file              | `bf2f6ffb4d39`  |
| 1109   | No file              | `bf2f6ffb4d39`  |
| 1102   | No file              | `bf2f6ffb4d39`  |
| 1096   | No file              | `bf2f6ffb4d39`  |
| 1088   | No file              | `bf2f6ffb4d39`  |
| 1081   | No file              | `bf2f6ffb4d39`  |
| 1076   | No file              | `bf2f6ffb4d39`  |
| 1069   | No file              | `bf2f6ffb4d39`  |
| 1064   | No file              | `bf2f6ffb4d39`  |
| 1058   | No file              | `bf2f6ffb4d39`  |
| 1051   | No file              | `bf2f6ffb4d39`  |
| 1044   | No file              | `bf2f6ffb4d39`  |
| 1036   | No file              | `bf2f6ffb4d39`  |
| 1026   | No file              | `bf2f6ffb4d39`  |
| 1016   | No file              | `bf2f6ffb4d39`  |
| 1009   | No file              | `bf2f6ffb4d39`  |
| 1005   | No file              | `bf2f6ffb4d39`  |
| 1000   | No file              | `bf2f6ffb4d39`  |
| 998    | No file              | `bf2f6ffb4d39`  |
| 990    | No file              | `bf2f6ffb4d39`  |
| 979    | No file              | `bf2f6ffb4d39`  |
| 972    | No file              | `bf2f6ffb4d39`  |
| 963    | No file              | `bf2f6ffb4d39`  |
| 955    | No file              | `bf2f6ffb4d39`  |
| 946    | No file              | `bf2f6ffb4d39`  |
| 938    | No file              | `bf2f6ffb4d39`  |
| 927    | No file              | `bf2f6ffb4d39`  |
| 911    | No file              | `bf2f6ffb4d39`  |
| 904    | No file              | `bf2f6ffb4d39`  |
| 899    | No file              | `bf2f6ffb4d39`  |
| 894    | No file              | `bf2f6ffb4d39`  |
| 885    | No file              | `bf2f6ffb4d39`  |
| 879    | No file              | `bf2f6ffb4d39`  |
| 872    | No file              | `bf2f6ffb4d39`  |
| 864    | No file              | `bf2f6ffb4d39`  |
| 855    | No file              | `bf2f6ffb4d39`  |
| 853    | No file              | `bf2f6ffb4d39`  |
| 845    | No file              | `bf2f6ffb4d39`  |
| 837    | No file              | `bf2f6ffb4d39`  |
| 829    | No file              | `bf2f6ffb4d39`  |
| 822    | No file              | `bf2f6ffb4d39`  |
| 814    | No file              | `bf2f6ffb4d39`  |
| 805    | No file              | `bf2f6ffb4d39`  |
| 794    | No file              | `bf2f6ffb4d39`  |
| 787    | No file              | `bf2f6ffb4d39`  |
| 780    | No file              | `bf2f6ffb4d39`  |
| 771    | No file              | `bf2f6ffb4d39`  |
| 760    | No file              | `bf2f6ffb4d39`  |
| 748    | No file              | `bf2f6ffb4d39`  |
| 741    | No file              | `bf2f6ffb4d39`  |
| 736    | No file              | `bf2f6ffb4d39`  |
| 731    | No file              | `bf2f6ffb4d39`  |
| 723    | No file              | `bf2f6ffb4d39`  |
| 711    | No file              | `bf2f6ffb4d39`  |
| 707    | No file              | `bf2f6ffb4d39`  |
| 697    | No file              | `bf2f6ffb4d39`  |
| 689    | No file              | `bf2f6ffb4d39`  |
| 683    | No file              | `bf2f6ffb4d39`  |
| 678    | No file              | `bf2f6ffb4d39`  |
| 670    | No file              | `bf2f6ffb4d39`  |
| 661    | No file              | `bf2f6ffb4d39`  |
| 656    | No file              | `bf2f6ffb4d39`  |
| 652    | No file              | `bf2f6ffb4d39`  |
| 643    | No file              | `bf2f6ffb4d39`  |
| 637    | No file              | `bf2f6ffb4d39`  |
| 630    | No file              | `bf2f6ffb4d39`  |
| 627    | No file              | `bf2f6ffb4d39`  |
| 621    | No file              | `bf2f6ffb4d39`  |
| 617    | No file              | `bf2f6ffb4d39`  |
| 615    | No file              | `bf2f6ffb4d39`  |
| 606    | No file              | `bf2f6ffb4d39`  |
| 599    | No file              | `bf2f6ffb4d39`  |
| 592    | No file              | `bf2f6ffb4d39`  |
| 586    | No file              | `bf2f6ffb4d39`  |
| 577    | No file              | `bf2f6ffb4d39`  |
| 569    | No file              | `bf2f6ffb4d39`  |
| 561    | No file              | `bf2f6ffb4d39`  |
| 554    | No file              | `bf2f6ffb4d39`  |
| 542    | No file              | `bf2f6ffb4d39`  |
| 532    | No file              | `bf2f6ffb4d39`  |
| 531    | No file              | `bf2f6ffb4d39`  |
| 526    | No file              | `bf2f6ffb4d39`  |
| 521    | No file              | `bf2f6ffb4d39`  |
| 517    | No file              | `bf2f6ffb4d39`  |
| 510    | No file              | `bf2f6ffb4d39`  |
| 508    | No file              | `bf2f6ffb4d39`  |
| 504    | No file              | `bf2f6ffb4d39`  |
| 497    | No file              | `bf2f6ffb4d39`  |
| 491    | No file              | `bf2f6ffb4d39`  |
| 485    | No file              | `bf2f6ffb4d39`  |
| 478    | No file              | `bf2f6ffb4d39`  |
| 472    | No file              | `bf2f6ffb4d39`  |
| 466    | No file              | `bf2f6ffb4d39`  |
| 457    | No file              | `bf2f6ffb4d39`  |
| 452    | No file              | `bf2f6ffb4d39`  |
| 449    | No file              | `bf2f6ffb4d39`  |
| 435    | No file              | `bf2f6ffb4d39`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of movies                              |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (15 bytes)

| Offset  | Type | Field          | Notes                                                                            |
| ------- | ---- | -------------- | -------------------------------------------------------------------------------- |
| `+0x00` | u32  | movie_name     | Index into `strings`: the movie (`Goyen` for `ui_movie/pc/cutscene/abyssstory/goyen/goyen.bk2`) |
| `+0x04` | u32  | audio_name     | Index into `strings`: the Wwise event and bank name (`Bink_Goyen`)               |
| `+0x08` | u32  | audio_name_dup | Equals `audio_name` on every row                                                 |
| `+0x0C` | u8   | unknown_0c     | `1` on every row of clients 2107 and 3482                                        |
| `+0x0D` | u8   | unknown_0d     | `1` on every row of clients 2107 and 3482                                        |
| `+0x0E` | u8   | unknown_0e     | `1` on every row of clients 2107 and 3482                                        |

The rows are in no name order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                            |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                |
| `+0x04` | pstr[string_count] | strings      | Movie and audio names, UTF-8, in row order: movie, then audio name |

## Field Names

No sheet of the client 1784 `DataSheets.bexcel` holds the file; client
2073 is the first test client that has it (client 2107: six movies). The names
follow the client files the strings point at (client 3482):

- `movie_name`: 159 of 161 are the stem of a `.bk2` file in the PAZ;
  `RoseWar_Kama_Ranger` and `MorningLand_TheEnd` are not.
- `audio_name`: 160 of 161 are both an event and a bank of
  `sound2022/wwise_ids.h`; `Bink_MorningLand_TheEnd` is neither. 154 have
  a `bink_<movie>.bnk` bank under `sound2022/windows/english(us)/`.

Which of `audio_name` and `audio_name_dup` is the event and which the bank
is not known: the two hold one string on every row.

## Open Questions

### Three Flags

`unknown_0c` to `unknown_0e` are `1` on every row. They may switch the
movie's audio per language or per sound channel; a row with a `0` would
tell.
