# `tutorial.bss` Format

## Purpose

The steps of the Black Spirit guide tutorials that `Panel_Widget_Tutorial_GuideUI`
plays: on client 3482 four pet tutorials (first meeting, summon and seal,
feeding, groups) with 21 steps. A step is keyed by tutorial type and index;
it has a start condition, the condition script that completes it, the
`tutorial_startevent.bss` events it starts (black and white highlight
boxes), the Black Spirit title and text, an optional artwork image, and
where the text box sits. When a step completes, the Lua asks for the step
with the next index of the same type and ends the tutorial when there is
none.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File           | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | -------------- | ----- | ------- | ----------------------- |
| 1      | 1725 and later | 3483    | `tutorial.bss` | 7,919 | 21 Row  | 69 to 73, 72 on average |

| Layout | File           | Known           | Unknown      |
| ------ | -------------- | --------------- | ------------ |
| 1      | `tutorial.bss` | 7,688 B (97.1%) | 231 B (2.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `ab29c4943e86`  |
| 3482   | Layout 1             | `ab29c4943e86`  |
| 3474   | Layout 1             | `ab29c4943e86`  |
| 3473   | Layout 1             | `ab29c4943e86`  |
| 3464   | Layout 1             | `ab29c4943e86`  |
| 3458   | Layout 1             | `ab29c4943e86`  |
| 3454   | Layout 1             | `ab29c4943e86`  |
| 3444   | Layout 1             | `ab29c4943e86`  |
| 3435   | Layout 1             | `ab29c4943e86`  |
| 3426   | Layout 1             | `ab29c4943e86`  |
| 3418   | Layout 1             | `ab29c4943e86`  |
| 3412   | Layout 1             | `ab29c4943e86`  |
| 3402   | Layout 1             | `ab29c4943e86`  |
| 3396   | Layout 1             | `ab29c4943e86`  |
| 3387   | Layout 1             | `ab29c4943e86`  |
| 3381   | Layout 1             | `ab29c4943e86`  |
| 3373   | Layout 1             | `ab29c4943e86`  |
| 3364   | Layout 1             | `ab29c4943e86`  |
| 3356   | Layout 1             | `ab29c4943e86`  |
| 3349   | Layout 1             | `ab29c4943e86`  |
| 3342   | Layout 1             | `ab29c4943e86`  |
| 3335   | Layout 1             | `ab29c4943e86`  |
| 3326   | Layout 1             | `ab29c4943e86`  |
| 3321   | Layout 1             | `ab29c4943e86`  |
| 3314   | Layout 1             | `ab29c4943e86`  |
| 3303   | Layout 1             | `ab29c4943e86`  |
| 3302   | Layout 1             | `ab29c4943e86`  |
| 3293   | Layout 1             | `ab29c4943e86`  |
| 3283   | Layout 1             | `ab29c4943e86`  |
| 3275   | Layout 1             | `ab29c4943e86`  |
| 3267   | Layout 1             | `ab29c4943e86`  |
| 3258   | Layout 1             | `ab29c4943e86`  |
| 3251   | Layout 1             | `ab29c4943e86`  |
| 3242   | Layout 1             | `ab29c4943e86`  |
| 3235   | Layout 1             | `ab29c4943e86`  |
| 3229   | Layout 1             | `ab29c4943e86`  |
| 3212   | Layout 1             | `ab29c4943e86`  |
| 3203   | Layout 1             | `ab29c4943e86`  |
| 3193   | Layout 1             | `ab29c4943e86`  |
| 3186   | Layout 1             | `ab29c4943e86`  |
| 3177   | Layout 1             | `ab29c4943e86`  |
| 3169   | Layout 1             | `ab29c4943e86`  |
| 3158   | Layout 1             | `ab29c4943e86`  |
| 3151   | Layout 1             | `ab29c4943e86`  |
| 3144   | Layout 1             | `ab29c4943e86`  |
| 3133   | Layout 1             | `ab29c4943e86`  |
| 3125   | Layout 1             | `ab29c4943e86`  |
| 3118   | Layout 1             | `ab29c4943e86`  |
| 3111   | Layout 1             | `ab29c4943e86`  |
| 3103   | Layout 1             | `ab29c4943e86`  |
| 3095   | Layout 1             | `ab29c4943e86`  |
| 3086   | Layout 1             | `ab29c4943e86`  |
| 3072   | Layout 1             | `ab29c4943e86`  |
| 3062   | Layout 1             | `ab29c4943e86`  |
| 3052   | Layout 1             | `ab29c4943e86`  |
| 3045   | Layout 1             | `ab29c4943e86`  |
| 3037   | Layout 1             | `ab29c4943e86`  |
| 3030   | Layout 1             | `ab29c4943e86`  |
| 3021   | Layout 1             | `ab29c4943e86`  |
| 3012   | Layout 1             | `ab29c4943e86`  |
| 3002   | Layout 1             | `ab29c4943e86`  |
| 2995   | Layout 1             | `ab29c4943e86`  |
| 2987   | Layout 1             | `ab29c4943e86`  |
| 2978   | Layout 1             | `ab29c4943e86`  |
| 2970   | Layout 1             | `ab29c4943e86`  |
| 2959   | Layout 1             | `ab29c4943e86`  |
| 2951   | Layout 1             | `ab29c4943e86`  |
| 2942   | Layout 1             | `ab29c4943e86`  |
| 2935   | Layout 1             | `ab29c4943e86`  |
| 2932   | Layout 1             | `ab29c4943e86`  |
| 2923   | Layout 1             | `ab29c4943e86`  |
| 2919   | Layout 1             | `ab29c4943e86`  |
| 2907   | Layout 1             | `ab29c4943e86`  |
| 2900   | Layout 1             | `ab29c4943e86`  |
| 2891   | Layout 1             | `ab29c4943e86`  |
| 2882   | Layout 1             | `ab29c4943e86`  |
| 2872   | Layout 1             | `ab29c4943e86`  |
| 2863   | Layout 1             | `ab29c4943e86`  |
| 2855   | Layout 1             | `ab29c4943e86`  |
| 2849   | Layout 1             | `ab29c4943e86`  |
| 2844   | Layout 1             | `ab29c4943e86`  |
| 2834   | Layout 1             | `ab29c4943e86`  |
| 2825   | Layout 1             | `ab29c4943e86`  |
| 2819   | Layout 1             | `ab29c4943e86`  |
| 2811   | Layout 1             | `ab29c4943e86`  |
| 2803   | Layout 1             | `ab29c4943e86`  |
| 2794   | Layout 1             | `ab29c4943e86`  |
| 2783   | Layout 1             | `ab29c4943e86`  |
| 2774   | Layout 1             | `ab29c4943e86`  |
| 2765   | Layout 1             | `ab29c4943e86`  |
| 2756   | Layout 1             | `ab29c4943e86`  |
| 2750   | Layout 1             | `ab29c4943e86`  |
| 2743   | Layout 1             | `ab29c4943e86`  |
| 2736   | Layout 1             | `ab29c4943e86`  |
| 2726   | Layout 1             | `ab29c4943e86`  |
| 2717   | Layout 1             | `ab29c4943e86`  |
| 2709   | Layout 1             | `ab29c4943e86`  |
| 2703   | Layout 1             | `ab29c4943e86`  |
| 2695   | Layout 1             | `ab29c4943e86`  |
| 2684   | Layout 1             | `ab29c4943e86`  |
| 2672   | Layout 1             | `ab29c4943e86`  |
| 2665   | Layout 1             | `ab29c4943e86`  |
| 2657   | Layout 1             | `ab29c4943e86`  |
| 2649   | Layout 1             | `ab29c4943e86`  |
| 2644   | Layout 1             | `ab29c4943e86`  |
| 2637   | Layout 1             | `ab29c4943e86`  |
| 2629   | Layout 1             | `ab29c4943e86`  |
| 2619   | Layout 1             | `ab29c4943e86`  |
| 2612   | Layout 1             | `ab29c4943e86`  |
| 2606   | Layout 1             | `ab29c4943e86`  |
| 2602   | Layout 1             | `ab29c4943e86`  |
| 2601   | Layout 1             | `ab29c4943e86`  |
| 2592   | Layout 1             | `ab29c4943e86`  |
| 2583   | Layout 1             | `ab29c4943e86`  |
| 2575   | Layout 1             | `ab29c4943e86`  |
| 2567   | Layout 1             | `ab29c4943e86`  |
| 2560   | Layout 1             | `ab29c4943e86`  |
| 2553   | Layout 1             | `ab29c4943e86`  |
| 2545   | Layout 1             | `ab29c4943e86`  |
| 2538   | Layout 1             | `ab29c4943e86`  |
| 2529   | Layout 1             | `ab29c4943e86`  |
| 2519   | Layout 1             | `ab29c4943e86`  |
| 2513   | Layout 1             | `ab29c4943e86`  |
| 2510   | Layout 1             | `ab29c4943e86`  |
| 2507   | Layout 1             | `ab29c4943e86`  |
| 2503   | Layout 1             | `ab29c4943e86`  |
| 2498   | Layout 1             | `ab29c4943e86`  |
| 2492   | Layout 1             | `ab29c4943e86`  |
| 2487   | Layout 1             | `ab29c4943e86`  |
| 2480   | Layout 1             | `ab29c4943e86`  |
| 2474   | Layout 1             | `ab29c4943e86`  |
| 2468   | Layout 1             | `ab29c4943e86`  |
| 2460   | Layout 1             | `ab29c4943e86`  |
| 2453   | Layout 1             | `ab29c4943e86`  |
| 2444   | Layout 1             | `ab29c4943e86`  |
| 2438   | Layout 1             | `ab29c4943e86`  |
| 2434   | Layout 1             | `ab29c4943e86`  |
| 2429   | Layout 1             | `ab29c4943e86`  |
| 2421   | Layout 1             | `ab29c4943e86`  |
| 2414   | Layout 1             | `ab29c4943e86`  |
| 2407   | Layout 1             | `ab29c4943e86`  |
| 2401   | Layout 1             | `ab29c4943e86`  |
| 2397   | Layout 1             | `ab29c4943e86`  |
| 2393   | Layout 1             | `ab29c4943e86`  |
| 2384   | Layout 1             | `ab29c4943e86`  |
| 2378   | Layout 1             | `ab29c4943e86`  |
| 2372   | Layout 1             | `ab29c4943e86`  |
| 2358   | Layout 1             | `ab29c4943e86`  |
| 2352   | Layout 1             | `ab29c4943e86`  |
| 2347   | Layout 1             | `ab29c4943e86`  |
| 2343   | Layout 1             | `ab29c4943e86`  |
| 2335   | Layout 1             | `ab29c4943e86`  |
| 2327   | Layout 1             | `ab29c4943e86`  |
| 2324   | Layout 1             | `ab29c4943e86`  |
| 2319   | Layout 1             | `ab29c4943e86`  |
| 2313   | Layout 1             | `ab29c4943e86`  |
| 2308   | Layout 1             | `ab29c4943e86`  |
| 2302   | Layout 1             | `ab29c4943e86`  |
| 2295   | Layout 1             | `ab29c4943e86`  |
| 2290   | Layout 1             | `ab29c4943e86`  |
| 2284   | Layout 1             | `ab29c4943e86`  |
| 2276   | Layout 1             | `ab29c4943e86`  |
| 2269   | Layout 1             | `ab29c4943e86`  |
| 2259   | Layout 1             | `ab29c4943e86`  |
| 2250   | Layout 1             | `ab29c4943e86`  |
| 2243   | Layout 1             | `ab29c4943e86`  |
| 2235   | Layout 1             | `ab29c4943e86`  |
| 2229   | Layout 1             | `ab29c4943e86`  |
| 2224   | Layout 1             | `ab29c4943e86`  |
| 2218   | Layout 1             | `ab29c4943e86`  |
| 2215   | Layout 1             | `ab29c4943e86`  |
| 2207   | Layout 1             | `ab29c4943e86`  |
| 2203   | Layout 1             | `ab29c4943e86`  |
| 2196   | Layout 1             | `ab29c4943e86`  |
| 2192   | Layout 1             | `ab29c4943e86`  |
| 2189   | Layout 1             | `ab29c4943e86`  |
| 2183   | Layout 1             | `ab29c4943e86`  |
| 2179   | Layout 1             | `ab29c4943e86`  |
| 2171   | Layout 1             | `ab29c4943e86`  |
| 2163   | Layout 1             | `ab29c4943e86`  |
| 2156   | Layout 1             | `ab29c4943e86`  |
| 2151   | Layout 1             | `ab29c4943e86`  |
| 2147   | Layout 1             | `ab29c4943e86`  |
| 2142   | Layout 1             | `ab29c4943e86`  |
| 2138   | Layout 1             | `ab29c4943e86`  |
| 2134   | Layout 1             | `ab29c4943e86`  |
| 2130   | Layout 1             | `ab29c4943e86`  |
| 2122   | Layout 1             | `ab29c4943e86`  |
| 2107   | Layout 1             | `ab29c4943e86`  |
| 2098   | Layout 1             | `ab29c4943e86`  |
| 2089   | Layout 1             | `ab29c4943e86`  |
| 2081   | Layout 1             | `ab29c4943e86`  |
| 2073   | Layout 1             | `ab29c4943e86`  |
| 2067   | Layout 1             | `ab29c4943e86`  |
| 2063   | Layout 1             | `ab29c4943e86`  |
| 2059   | Layout 1             | `ab29c4943e86`  |
| 2052   | Layout 1             | `ab29c4943e86`  |
| 2044   | Layout 1             | `ab29c4943e86`  |
| 2039   | Layout 1             | `ab29c4943e86`  |
| 2032   | Layout 1             | `ab29c4943e86`  |
| 2025   | Layout 1             | `ab29c4943e86`  |
| 2011   | Layout 1             | `ab29c4943e86`  |
| 2005   | Layout 1             | `ab29c4943e86`  |
| 2000   | Layout 1             | `ab29c4943e86`  |
| 1996   | Layout 1             | `ab29c4943e86`  |
| 1991   | Layout 1             | `ab29c4943e86`  |
| 1985   | Layout 1             | `ab29c4943e86`  |
| 1980   | Layout 1             | `ab29c4943e86`  |
| 1969   | Layout 1             | `ab29c4943e86`  |
| 1964   | Layout 1             | `ab29c4943e86`  |
| 1958   | Layout 1             | `ab29c4943e86`  |
| 1950   | Layout 1             | `ab29c4943e86`  |
| 1945   | Layout 1             | `ab29c4943e86`  |
| 1937   | Layout 1             | `ab29c4943e86`  |
| 1933   | Layout 1             | `ab29c4943e86`  |
| 1927   | Layout 1             | `ab29c4943e86`  |
| 1921   | Layout 1             | `ab29c4943e86`  |
| 1914   | Layout 1             | `ab29c4943e86`  |
| 1908   | Layout 1             | `ab29c4943e86`  |
| 1897   | Layout 1             | `ab29c4943e86`  |
| 1892   | Layout 1             | `ab29c4943e86`  |
| 1886   | Layout 1             | `ab29c4943e86`  |
| 1881   | Layout 1             | `ab29c4943e86`  |
| 1871   | Layout 1             | `ab29c4943e86`  |
| 1866   | Layout 1             | `ab29c4943e86`  |
| 1862   | Layout 1             | `ab29c4943e86`  |
| 1854   | Layout 1             | `ab29c4943e86`  |
| 1846   | Layout 1             | `ab29c4943e86`  |
| 1838   | Layout 1             | `ab29c4943e86`  |
| 1832   | Layout 1             | `ab29c4943e86`  |
| 1826   | Layout 1             | `ab29c4943e86`  |
| 1822   | Layout 1             | `ab29c4943e86`  |
| 1818   | Layout 1             | `ab29c4943e86`  |
| 1804   | Layout 1             | `ab29c4943e86`  |
| 1794   | Layout 1             | `ab29c4943e86`  |
| 1790   | Layout 1             | `ab29c4943e86`  |
| 1784   | Layout 1             | `ab29c4943e86`  |
| 1774   | Layout 1             | `ab29c4943e86`  |
| 1771   | Layout 1             | `ab29c4943e86`  |
| 1762   | Layout 1             | `ab29c4943e86`  |
| 1759   | Layout 1             | `ab29c4943e86`  |
| 1754   | Layout 1             | `ab29c4943e86`  |
| 1749   | Layout 1             | `ab29c4943e86`  |
| 1743   | Layout 1             | `ab29c4943e86`  |
| 1737   | Layout 1             | `ab29c4943e86`  |
| 1731   | Layout 1             | `ab29c4943e86`  |
| 1725   | Layout 1             | `ab29c4943e86`  |
| 1717   | No documented layout | `ab29c4943e86`  |
| 1710   | No documented layout | `ab29c4943e86`  |
| 1704   | No documented layout | `ab29c4943e86`  |
| 1698   | No file              | `ab29c4943e86`  |
| 1690   | No file              | `ab29c4943e86`  |
| 1685   | No file              | `ab29c4943e86`  |
| 1680   | No file              | `ab29c4943e86`  |
| 1674   | No file              | `ab29c4943e86`  |
| 1668   | No file              | `ab29c4943e86`  |
| 1659   | No file              | `ab29c4943e86`  |
| 1649   | No file              | `ab29c4943e86`  |
| 1642   | No file              | `ab29c4943e86`  |
| 1636   | No file              | `ab29c4943e86`  |
| 1628   | No file              | `ab29c4943e86`  |
| 1622   | No file              | `ab29c4943e86`  |
| 1614   | No file              | `ab29c4943e86`  |
| 1608   | No file              | `ab29c4943e86`  |
| 1602   | No file              | `ab29c4943e86`  |
| 1598   | No file              | `ab29c4943e86`  |
| 1594   | No file              | `ab29c4943e86`  |
| 1590   | No file              | `ab29c4943e86`  |
| 1587   | No file              | `ab29c4943e86`  |
| 1584   | No file              | `ab29c4943e86`  |
| 1579   | No file              | `ab29c4943e86`  |
| 1572   | No file              | `ab29c4943e86`  |
| 1565   | No file              | `ab29c4943e86`  |
| 1559   | No file              | `ab29c4943e86`  |
| 1554   | No file              | `ab29c4943e86`  |
| 1547   | No file              | `ab29c4943e86`  |
| 1537   | No file              | `ab29c4943e86`  |
| 1529   | No file              | `ab29c4943e86`  |
| 1524   | No file              | `ab29c4943e86`  |
| 1519   | No file              | `ab29c4943e86`  |
| 1509   | No file              | `ab29c4943e86`  |
| 1506   | No file              | `ab29c4943e86`  |
| 1504   | No file              | `ab29c4943e86`  |
| 1500   | No file              | `ab29c4943e86`  |
| 1493   | No file              | `ab29c4943e86`  |
| 1489   | No file              | `ab29c4943e86`  |
| 1485   | No file              | `ab29c4943e86`  |
| 1481   | No file              | `ab29c4943e86`  |
| 1474   | No file              | `ab29c4943e86`  |
| 1466   | No file              | `ab29c4943e86`  |
| 1462   | No file              | `ab29c4943e86`  |
| 1459   | No file              | `ab29c4943e86`  |
| 1453   | No file              | `ab29c4943e86`  |
| 1450   | No file              | `ab29c4943e86`  |
| 1445   | No file              | `ab29c4943e86`  |
| 1439   | No file              | `ab29c4943e86`  |
| 1433   | No file              | `ab29c4943e86`  |
| 1430   | No file              | `ab29c4943e86`  |
| 1426   | No file              | `ab29c4943e86`  |
| 1421   | No file              | `ab29c4943e86`  |
| 1417   | No file              | `ab29c4943e86`  |
| 1416   | No file              | `ab29c4943e86`  |
| 1409   | No file              | `ab29c4943e86`  |
| 1405   | No file              | `ab29c4943e86`  |
| 1401   | No file              | `ab29c4943e86`  |
| 1396   | No file              | `ab29c4943e86`  |
| 1391   | No file              | `ab29c4943e86`  |
| 1390   | No file              | `ab29c4943e86`  |
| 1386   | No file              | `ab29c4943e86`  |
| 1381   | No file              | `ab29c4943e86`  |
| 1379   | No file              | `ab29c4943e86`  |
| 1372   | No file              | `ab29c4943e86`  |
| 1366   | No file              | `ab29c4943e86`  |
| 1364   | No file              | `ab29c4943e86`  |
| 1363   | No file              | `ab29c4943e86`  |
| 1360   | No file              | `ab29c4943e86`  |
| 1358   | No file              | `ab29c4943e86`  |
| 1355   | No file              | `ab29c4943e86`  |
| 1351   | No file              | `ab29c4943e86`  |
| 1348   | No file              | `ab29c4943e86`  |
| 1346   | No file              | `ab29c4943e86`  |
| 1341   | No file              | `ab29c4943e86`  |
| 1340   | No file              | `ab29c4943e86`  |
| 1338   | No file              | `ab29c4943e86`  |
| 1335   | No file              | `ab29c4943e86`  |
| 1333   | No file              | `ab29c4943e86`  |
| 1329   | No file              | `ab29c4943e86`  |
| 1327   | No file              | `ab29c4943e86`  |
| 1324   | No file              | `ab29c4943e86`  |
| 1321   | No file              | `ab29c4943e86`  |
| 1319   | No file              | `ab29c4943e86`  |
| 1318   | No file              | `ab29c4943e86`  |
| 1316   | No file              | `ab29c4943e86`  |
| 1313   | No file              | `ab29c4943e86`  |
| 1311   | No file              | `ab29c4943e86`  |
| 1309   | No file              | `ab29c4943e86`  |
| 1304   | No file              | `ab29c4943e86`  |
| 1292   | No file              | `ab29c4943e86`  |
| 1286   | No file              | `ab29c4943e86`  |
| 1280   | No file              | `ab29c4943e86`  |
| 1276   | No file              | `ab29c4943e86`  |
| 1267   | No file              | `ab29c4943e86`  |
| 1261   | No file              | `ab29c4943e86`  |
| 1256   | No file              | `ab29c4943e86`  |
| 1250   | No file              | `ab29c4943e86`  |
| 1246   | No file              | `ab29c4943e86`  |
| 1239   | No file              | `ab29c4943e86`  |
| 1230   | No file              | `ab29c4943e86`  |
| 1226   | No file              | `ab29c4943e86`  |
| 1220   | No file              | `ab29c4943e86`  |
| 1217   | No file              | `ab29c4943e86`  |
| 1211   | No file              | `ab29c4943e86`  |
| 1210   | No file              | `ab29c4943e86`  |
| 1208   | No file              | `ab29c4943e86`  |
| 1203   | No file              | `ab29c4943e86`  |
| 1197   | No file              | `ab29c4943e86`  |
| 1194   | No file              | `ab29c4943e86`  |
| 1192   | No file              | `ab29c4943e86`  |
| 1187   | No file              | `ab29c4943e86`  |
| 1183   | No file              | `ab29c4943e86`  |
| 1177   | No file              | `ab29c4943e86`  |
| 1173   | No file              | `ab29c4943e86`  |
| 1167   | No file              | `ab29c4943e86`  |
| 1164   | No file              | `ab29c4943e86`  |
| 1156   | No file              | `ab29c4943e86`  |
| 1149   | No file              | `ab29c4943e86`  |
| 1144   | No file              | `ab29c4943e86`  |
| 1137   | No file              | `ab29c4943e86`  |
| 1132   | No file              | `ab29c4943e86`  |
| 1127   | No file              | `ab29c4943e86`  |
| 1122   | No file              | `ab29c4943e86`  |
| 1118   | No file              | `ab29c4943e86`  |
| 1114   | No file              | `ab29c4943e86`  |
| 1109   | No file              | `ab29c4943e86`  |
| 1102   | No file              | `ab29c4943e86`  |
| 1096   | No file              | `ab29c4943e86`  |
| 1088   | No file              | `ab29c4943e86`  |
| 1081   | No file              | `ab29c4943e86`  |
| 1076   | No file              | `ab29c4943e86`  |
| 1069   | No file              | `ab29c4943e86`  |
| 1064   | No file              | `ab29c4943e86`  |
| 1058   | No file              | `ab29c4943e86`  |
| 1051   | No file              | `ab29c4943e86`  |
| 1044   | No file              | `ab29c4943e86`  |
| 1036   | No file              | `ab29c4943e86`  |
| 1026   | No file              | `ab29c4943e86`  |
| 1016   | No file              | `ab29c4943e86`  |
| 1009   | No file              | `ab29c4943e86`  |
| 1005   | No file              | `ab29c4943e86`  |
| 1000   | No file              | `ab29c4943e86`  |
| 998    | No file              | `ab29c4943e86`  |
| 990    | No file              | `ab29c4943e86`  |
| 979    | No file              | `ab29c4943e86`  |
| 972    | No file              | `ab29c4943e86`  |
| 963    | No file              | `ab29c4943e86`  |
| 955    | No file              | `ab29c4943e86`  |
| 946    | No file              | `ab29c4943e86`  |
| 938    | No file              | `ab29c4943e86`  |
| 927    | No file              | `ab29c4943e86`  |
| 911    | No file              | `ab29c4943e86`  |
| 904    | No file              | `ab29c4943e86`  |
| 899    | No file              | `ab29c4943e86`  |
| 894    | No file              | `ab29c4943e86`  |
| 885    | No file              | `ab29c4943e86`  |
| 879    | No file              | `ab29c4943e86`  |
| 872    | No file              | `ab29c4943e86`  |
| 864    | No file              | `ab29c4943e86`  |
| 855    | No file              | `ab29c4943e86`  |
| 853    | No file              | `ab29c4943e86`  |
| 845    | No file              | `ab29c4943e86`  |
| 837    | No file              | `ab29c4943e86`  |
| 829    | No file              | `ab29c4943e86`  |
| 822    | No file              | `ab29c4943e86`  |
| 814    | No file              | `ab29c4943e86`  |
| 805    | No file              | `ab29c4943e86`  |
| 794    | No file              | `ab29c4943e86`  |
| 787    | No file              | `ab29c4943e86`  |
| 780    | No file              | `ab29c4943e86`  |
| 771    | No file              | `ab29c4943e86`  |
| 760    | No file              | `ab29c4943e86`  |
| 748    | No file              | `ab29c4943e86`  |
| 741    | No file              | `ab29c4943e86`  |
| 736    | No file              | `ab29c4943e86`  |
| 731    | No file              | `ab29c4943e86`  |
| 723    | No file              | `ab29c4943e86`  |
| 711    | No file              | `ab29c4943e86`  |
| 707    | No file              | `ab29c4943e86`  |
| 697    | No file              | `ab29c4943e86`  |
| 689    | No file              | `ab29c4943e86`  |
| 683    | No file              | `ab29c4943e86`  |
| 678    | No file              | `ab29c4943e86`  |
| 670    | No file              | `ab29c4943e86`  |
| 661    | No file              | `ab29c4943e86`  |
| 656    | No file              | `ab29c4943e86`  |
| 652    | No file              | `ab29c4943e86`  |
| 643    | No file              | `ab29c4943e86`  |
| 637    | No file              | `ab29c4943e86`  |
| 630    | No file              | `ab29c4943e86`  |
| 627    | No file              | `ab29c4943e86`  |
| 621    | No file              | `ab29c4943e86`  |
| 617    | No file              | `ab29c4943e86`  |
| 615    | No file              | `ab29c4943e86`  |
| 606    | No file              | `ab29c4943e86`  |
| 599    | No file              | `ab29c4943e86`  |
| 592    | No file              | `ab29c4943e86`  |
| 586    | No file              | `ab29c4943e86`  |
| 577    | No file              | `ab29c4943e86`  |
| 569    | No file              | `ab29c4943e86`  |
| 561    | No file              | `ab29c4943e86`  |
| 554    | No file              | `ab29c4943e86`  |
| 542    | No file              | `ab29c4943e86`  |
| 532    | No file              | `ab29c4943e86`  |
| 531    | No file              | `ab29c4943e86`  |
| 526    | No file              | `ab29c4943e86`  |
| 521    | No file              | `ab29c4943e86`  |
| 517    | No file              | `ab29c4943e86`  |
| 510    | No file              | `ab29c4943e86`  |
| 508    | No file              | `ab29c4943e86`  |
| 504    | No file              | `ab29c4943e86`  |
| 497    | No file              | `ab29c4943e86`  |
| 491    | No file              | `ab29c4943e86`  |
| 485    | No file              | `ab29c4943e86`  |
| 478    | No file              | `ab29c4943e86`  |
| 472    | No file              | `ab29c4943e86`  |
| 466    | No file              | `ab29c4943e86`  |
| 457    | No file              | `ab29c4943e86`  |
| 452    | No file              | `ab29c4943e86`  |
| 449    | No file              | `ab29c4943e86`  |
| 435    | No file              | `ab29c4943e86`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone. Each of a step's
`start_event_keys` links to its
[`tutorial_startevent.bss`](tutorial_startevent_bss.md) row, and that
view links each start event back to the steps that list it.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of steps                               |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 69 bytes + start event keys)

Every `*_ref` field is an index into `strings`.

| Offset                  | Type                      | Field                        | Notes |
| ----------------------- | ------------------------- | ---------------------------- | ----- |
| `+0x00`                 | u16                       | tutorial_index               | Step number within its tutorial, from `0`; `TutorialKey:getIndex()` |
| `+0x02`                 | u16                       | tutorial_type                | Tutorial the step belongs to; `TutorialKey:getType()`, `1` to `4` on client 3482 |
| `+0x04`                 | u32                       | start_condition_ref          | Condition script that must hold before the step starts (`getItemCount(331059,0)>0;`); empty on 19 of 21 steps |
| `+0x08`                 | u32                       | complete_condition_ref       | Event that completes the step: `anyinput()`, `useitem(331059)`, `setshowpanel(Panel_Window_PetList_All, 1)` or `uiinputevent(<panel>, <control>, Mouse_LUp)` |
| `+0x0C`                 | u64                       | start_event_count            | `getStartEventCount()`; `0` or `1`                                  |
| `+0x14`                 | u32[start_event_count]    | start_event_keys             | `getStartEventKey(i)`: `tutorial_startevent.bss` keys, `1` to `17` |
| `start_event_keys+0x00` | u32                       | title_ref                    | `getTitle()`: Korean tutorial title, the same on every step of a type |
| `start_event_keys+0x04` | u32                       | desc_ref                     | `getDesc()`: Korean Black Spirit text with `<PAColor>` tags and `\n` escapes |
| `start_event_keys+0x08` | u32                       | image_path_ref               | `getImagePath()`: artwork shown under the text (`UI_Artwork/Tutorial_Pet_00.dds`); empty on 19 steps |
| `start_event_keys+0x0C` | u32                       | base_pos_panel_hash          | `getBasePosPanelID()`: `ascii_key_hash()` of the panel the text box is placed against (`Panel_Window_Inventory_All`, `Panel_Window_PetList_All`); `0` places it against the screen |
| `start_event_keys+0x10` | f32[2]                    | pos                          | `getPos()`: x and y used when `attr` has no flag for that axis      |
| `start_event_keys+0x18` | f32[2]                    | pan                          | `getPan()`: x and y offset from the aligned edge when `attr` has a flag for that axis |
| `start_event_keys+0x20` | u32                       | attr                         | `isAttr()` flags, see [Position Flags](#position-flags)             |
| `start_event_keys+0x24` | u8                        | unknown_start_event_keys_24  | `1` on every step; see Open Questions                               |
| `start_event_keys+0x25` | u8                        | accept_tutorial_type         | `2` on step `1.4` and `3` on step `2.4`, the last steps of types 1 and 2; else `0` |
| `start_event_keys+0x26` | bytes[10]                 | unknown_start_event_keys_26  | All zero on every step; see Open Questions                          |
| `start_event_keys+0x30` | u8                        | use_popup                    | `1` on the first steps of tutorials 1 and 4, else `0`               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                  |
| ------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `46` on client 3482                 |
| `+0x04` | pstr[string_count] | strings      | String `0` is empty; each text is stored once          |

## Position Flags

`attr` against the `Pos` column of the `Tutorial_Table` sheet (21 of 21
steps, client 3482):

| `attr`    | Sheet `Pos`      | Flags                     |
| --------- | ---------------- | ------------------------- |
| `0x10001` | `left, middle`   | `0x1` left, `0x10000` middle |
| `0x10010` | `center, middle` | `0x10` center, `0x10000` middle |
| `0`       | `-700, 0`        | none: `pos` holds the sheet value |

The Lua also tests `__eTutorialAttrPos_Right`, `_Top` and `_Bottom`; no
step uses them, so their bits are not known.

## Field Names

The `Tutorial_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has 21 rows, and the file is the same from client 1784 to
client 3482. Matched on all 21 rows: `Type` and `Index` (the key),
`StartCondition`, `CompleteCondition`, `StartEventKeyList`, `Title`,
`Desc`, `ImagePath`, `BasePosPanel` (hashed), `Pos` (as `pos` or as
`attr`), `Pan`, `AcceptTutorialType` and `UsePopup`. The Lua getters in
`panel_widget_tutorial_guideui_1.luac` name the same fields
(`getStartEventKey`, `getBasePosPanelID`, `getPan`, `getPos`, `isAttr`,
`getImagePath`, `isUseSkip`).

## Notes

- The rows are not in key order: type 4 comes first, its steps from index
  3 down to 0.
- `complete_condition_ref` and `start_condition_ref` hold the step scripts
  as text; the `uiinputevent` panel and control names are the client's UI
  names.

## Open Questions

### Skip, No Translate and Not Input

The sheet's `UseSkip` and `DoNotTranslate` are `1` and `NotInput` is `0`
on all 21 rows, and `AllowKey` is empty. `unknown_start_event_keys_24` is
`1` on every step, so it is `UseSkip` (`isUseSkip()`) or
`DoNotTranslate`; the ten zero bytes of `unknown_start_event_keys_26` hold
`NotInput` (`isNotInput()` of the running tutorial) and the `AllowKey` list somewhere. No client
from 1784 on changes a byte of the file, so the data cannot place them.
