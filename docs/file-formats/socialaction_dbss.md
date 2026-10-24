# `socialaction.dbss` Format

## Purpose

The social actions (emotes) of the Social Actions window: one row per action
with its Korean name, the condition script that unlocks it, the chat
command and keywords that play it, the action chart name, the icon, the
Korean condition message and its contents groups. The window
(`panel_socialaction.luac`) reads the rows through
`ToClient_getSocialActionInfoList()`, `ToClient_getSocialActionInfoByIndex()`
and `ToClient_getSocialActionStaticStatusByKey()` and their getters
`getName()`, `getCommand()`, `getKeywordBuffer()`, `getIconPath()` and
`getConditionMessage()`. Companion `socialactionoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records       | Row bytes                    |
| ------ | -------------- | ------- | ------------------------- | ------ | ------------- | ---------------------------- |
| 2      | 3072 and later | 3483    | `socialaction.dbss`       | 82,933 | 86 Row        | 199 to 3,888, 964 on average |
| 2      | 3072 and later | 3483    | `socialactionoffset.dbss` | 864    | 86 Offset Row | 10                           |
| 1      | 1346 to 3062   | 3062    | `socialaction.dbss`       | 49,041 | 73 Row        | 198 to 3,771, 672 on average |
| 1      | 1346 to 3062   | 3062    | `socialactionoffset.dbss` | 734    | 73 Offset Row | 10                           |

| Layout | File                      | Known            | Unknown      |
| ------ | ------------------------- | ---------------- | ------------ |
| 2      | `socialaction.dbss`       | 82,503 B (99.5%) | 430 B (0.5%) |
| 2      | `socialactionoffset.dbss` | 864 B (100.0%)   | 0 B (0.0%)   |
| 1      | `socialaction.dbss`       | 48,749 B (99.4%) | 292 B (0.6%) |
| 1      | `socialactionoffset.dbss` | 734 B (100.0%)   | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `7bd42dce2b00`  |
| 3482   | Layout 2             | `7bd42dce2b00`  |
| 3474   | Layout 2             | `7bd42dce2b00`  |
| 3473   | Layout 2             | `7bd42dce2b00`  |
| 3464   | Layout 2             | `7bd42dce2b00`  |
| 3458   | Layout 2             | `7bd42dce2b00`  |
| 3454   | Layout 2             | `7bd42dce2b00`  |
| 3444   | Layout 2             | `7bd42dce2b00`  |
| 3435   | Layout 2             | `7bd42dce2b00`  |
| 3426   | Layout 2             | `7bd42dce2b00`  |
| 3418   | Layout 2             | `7bd42dce2b00`  |
| 3412   | Layout 2             | `7bd42dce2b00`  |
| 3402   | Layout 2             | `7bd42dce2b00`  |
| 3396   | Layout 2             | `7bd42dce2b00`  |
| 3387   | Layout 2             | `7bd42dce2b00`  |
| 3381   | Layout 2             | `7bd42dce2b00`  |
| 3373   | Layout 2             | `7bd42dce2b00`  |
| 3364   | Layout 2             | `7bd42dce2b00`  |
| 3356   | Layout 2             | `7bd42dce2b00`  |
| 3349   | Layout 2             | `7bd42dce2b00`  |
| 3342   | Layout 2             | `7bd42dce2b00`  |
| 3335   | Layout 2             | `7bd42dce2b00`  |
| 3326   | Layout 2             | `7bd42dce2b00`  |
| 3321   | Layout 2             | `7bd42dce2b00`  |
| 3314   | Layout 2             | `7bd42dce2b00`  |
| 3303   | Layout 2             | `7bd42dce2b00`  |
| 3302   | Layout 2             | `7bd42dce2b00`  |
| 3293   | Layout 2             | `7bd42dce2b00`  |
| 3283   | Layout 2             | `7bd42dce2b00`  |
| 3275   | Layout 2             | `7bd42dce2b00`  |
| 3267   | Layout 2             | `7bd42dce2b00`  |
| 3258   | Layout 2             | `7bd42dce2b00`  |
| 3251   | Layout 2             | `7bd42dce2b00`  |
| 3242   | Layout 2             | `7bd42dce2b00`  |
| 3235   | Layout 2             | `7bd42dce2b00`  |
| 3229   | Layout 2             | `7bd42dce2b00`  |
| 3212   | Layout 2             | `7bd42dce2b00`  |
| 3203   | Layout 2             | `7bd42dce2b00`  |
| 3193   | Layout 2             | `7bd42dce2b00`  |
| 3186   | Layout 2             | `7bd42dce2b00`  |
| 3177   | Layout 2             | `7bd42dce2b00`  |
| 3169   | Layout 2             | `7bd42dce2b00`  |
| 3158   | Layout 2             | `7bd42dce2b00`  |
| 3151   | Layout 2             | `7bd42dce2b00`  |
| 3144   | Layout 2             | `7bd42dce2b00`  |
| 3133   | Layout 2             | `7bd42dce2b00`  |
| 3125   | Layout 2             | `7bd42dce2b00`  |
| 3118   | Layout 2             | `7bd42dce2b00`  |
| 3111   | Layout 2             | `7bd42dce2b00`  |
| 3103   | Layout 2             | `7bd42dce2b00`  |
| 3095   | Layout 2             | `7bd42dce2b00`  |
| 3086   | Layout 2             | `7bd42dce2b00`  |
| 3072   | Layout 2             | `7bd42dce2b00`  |
| 3062   | Layout 1             | `7bd42dce2b00`  |
| 3052   | Layout 1             | `7bd42dce2b00`  |
| 3045   | Layout 1             | `7bd42dce2b00`  |
| 3037   | Layout 1             | `7bd42dce2b00`  |
| 3030   | Layout 1             | `7bd42dce2b00`  |
| 3021   | Layout 1             | `7bd42dce2b00`  |
| 3012   | Layout 1             | `7bd42dce2b00`  |
| 3002   | Layout 1             | `7bd42dce2b00`  |
| 2995   | Layout 1             | `7bd42dce2b00`  |
| 2987   | Layout 1             | `7bd42dce2b00`  |
| 2978   | Layout 1             | `7bd42dce2b00`  |
| 2970   | Layout 1             | `7bd42dce2b00`  |
| 2959   | Layout 1             | `7bd42dce2b00`  |
| 2951   | Layout 1             | `7bd42dce2b00`  |
| 2942   | Layout 1             | `7bd42dce2b00`  |
| 2935   | Layout 1             | `7bd42dce2b00`  |
| 2932   | Layout 1             | `7bd42dce2b00`  |
| 2923   | Layout 1             | `7bd42dce2b00`  |
| 2919   | Layout 1             | `7bd42dce2b00`  |
| 2907   | Layout 1             | `7bd42dce2b00`  |
| 2900   | Layout 1             | `7bd42dce2b00`  |
| 2891   | Layout 1             | `7bd42dce2b00`  |
| 2882   | Layout 1             | `7bd42dce2b00`  |
| 2872   | Layout 1             | `7bd42dce2b00`  |
| 2863   | Layout 1             | `7bd42dce2b00`  |
| 2855   | Layout 1             | `7bd42dce2b00`  |
| 2849   | Layout 1             | `7bd42dce2b00`  |
| 2844   | Layout 1             | `7bd42dce2b00`  |
| 2834   | Layout 1             | `7bd42dce2b00`  |
| 2825   | Layout 1             | `7bd42dce2b00`  |
| 2819   | Layout 1             | `7bd42dce2b00`  |
| 2811   | Layout 1             | `7bd42dce2b00`  |
| 2803   | Layout 1             | `7bd42dce2b00`  |
| 2794   | Layout 1             | `7bd42dce2b00`  |
| 2783   | Layout 1             | `7bd42dce2b00`  |
| 2774   | Layout 1             | `7bd42dce2b00`  |
| 2765   | Layout 1             | `7bd42dce2b00`  |
| 2756   | Layout 1             | `7bd42dce2b00`  |
| 2750   | Layout 1             | `7bd42dce2b00`  |
| 2743   | Layout 1             | `7bd42dce2b00`  |
| 2736   | Layout 1             | `7bd42dce2b00`  |
| 2726   | Layout 1             | `7bd42dce2b00`  |
| 2717   | Layout 1             | `7bd42dce2b00`  |
| 2709   | Layout 1             | `7bd42dce2b00`  |
| 2703   | Layout 1             | `7bd42dce2b00`  |
| 2695   | Layout 1             | `7bd42dce2b00`  |
| 2684   | Layout 1             | `7bd42dce2b00`  |
| 2672   | Layout 1             | `7bd42dce2b00`  |
| 2665   | Layout 1             | `7bd42dce2b00`  |
| 2657   | Layout 1             | `7bd42dce2b00`  |
| 2649   | Layout 1             | `7bd42dce2b00`  |
| 2644   | Layout 1             | `7bd42dce2b00`  |
| 2637   | Layout 1             | `7bd42dce2b00`  |
| 2629   | Layout 1             | `7bd42dce2b00`  |
| 2619   | Layout 1             | `7bd42dce2b00`  |
| 2612   | Layout 1             | `7bd42dce2b00`  |
| 2606   | Layout 1             | `7bd42dce2b00`  |
| 2602   | Layout 1             | `7bd42dce2b00`  |
| 2601   | Layout 1             | `7bd42dce2b00`  |
| 2592   | Layout 1             | `7bd42dce2b00`  |
| 2583   | Layout 1             | `7bd42dce2b00`  |
| 2575   | Layout 1             | `7bd42dce2b00`  |
| 2567   | Layout 1             | `7bd42dce2b00`  |
| 2560   | Layout 1             | `7bd42dce2b00`  |
| 2553   | Layout 1             | `7bd42dce2b00`  |
| 2545   | Layout 1             | `7bd42dce2b00`  |
| 2538   | Layout 1             | `7bd42dce2b00`  |
| 2529   | Layout 1             | `7bd42dce2b00`  |
| 2519   | Layout 1             | `7bd42dce2b00`  |
| 2513   | Layout 1             | `7bd42dce2b00`  |
| 2510   | Layout 1             | `7bd42dce2b00`  |
| 2507   | Layout 1             | `7bd42dce2b00`  |
| 2503   | Layout 1             | `7bd42dce2b00`  |
| 2498   | Layout 1             | `7bd42dce2b00`  |
| 2492   | Layout 1             | `7bd42dce2b00`  |
| 2487   | Layout 1             | `7bd42dce2b00`  |
| 2480   | Layout 1             | `7bd42dce2b00`  |
| 2474   | Layout 1             | `7bd42dce2b00`  |
| 2468   | Layout 1             | `7bd42dce2b00`  |
| 2460   | Layout 1             | `7bd42dce2b00`  |
| 2453   | Layout 1             | `7bd42dce2b00`  |
| 2444   | Layout 1             | `7bd42dce2b00`  |
| 2438   | Layout 1             | `7bd42dce2b00`  |
| 2434   | Layout 1             | `7bd42dce2b00`  |
| 2429   | Layout 1             | `7bd42dce2b00`  |
| 2421   | Layout 1             | `7bd42dce2b00`  |
| 2414   | Layout 1             | `7bd42dce2b00`  |
| 2407   | Layout 1             | `7bd42dce2b00`  |
| 2401   | Layout 1             | `7bd42dce2b00`  |
| 2397   | Layout 1             | `7bd42dce2b00`  |
| 2393   | Layout 1             | `7bd42dce2b00`  |
| 2384   | Layout 1             | `7bd42dce2b00`  |
| 2378   | Layout 1             | `7bd42dce2b00`  |
| 2372   | Layout 1             | `7bd42dce2b00`  |
| 2358   | Layout 1             | `7bd42dce2b00`  |
| 2352   | Layout 1             | `7bd42dce2b00`  |
| 2347   | Layout 1             | `7bd42dce2b00`  |
| 2343   | Layout 1             | `7bd42dce2b00`  |
| 2335   | Layout 1             | `7bd42dce2b00`  |
| 2327   | Layout 1             | `7bd42dce2b00`  |
| 2324   | Layout 1             | `7bd42dce2b00`  |
| 2319   | Layout 1             | `7bd42dce2b00`  |
| 2313   | Layout 1             | `7bd42dce2b00`  |
| 2308   | Layout 1             | `7bd42dce2b00`  |
| 2302   | Layout 1             | `7bd42dce2b00`  |
| 2295   | Layout 1             | `7bd42dce2b00`  |
| 2290   | Layout 1             | `7bd42dce2b00`  |
| 2284   | Layout 1             | `7bd42dce2b00`  |
| 2276   | Layout 1             | `7bd42dce2b00`  |
| 2269   | Layout 1             | `7bd42dce2b00`  |
| 2259   | Layout 1             | `7bd42dce2b00`  |
| 2250   | Layout 1             | `7bd42dce2b00`  |
| 2243   | Layout 1             | `7bd42dce2b00`  |
| 2235   | Layout 1             | `7bd42dce2b00`  |
| 2229   | Layout 1             | `7bd42dce2b00`  |
| 2224   | Layout 1             | `7bd42dce2b00`  |
| 2218   | Layout 1             | `7bd42dce2b00`  |
| 2215   | Layout 1             | `7bd42dce2b00`  |
| 2207   | Layout 1             | `7bd42dce2b00`  |
| 2203   | Layout 1             | `7bd42dce2b00`  |
| 2196   | Layout 1             | `7bd42dce2b00`  |
| 2192   | Layout 1             | `7bd42dce2b00`  |
| 2189   | Layout 1             | `7bd42dce2b00`  |
| 2183   | Layout 1             | `7bd42dce2b00`  |
| 2179   | Layout 1             | `7bd42dce2b00`  |
| 2171   | Layout 1             | `7bd42dce2b00`  |
| 2163   | Layout 1             | `7bd42dce2b00`  |
| 2156   | Layout 1             | `7bd42dce2b00`  |
| 2151   | Layout 1             | `7bd42dce2b00`  |
| 2147   | Layout 1             | `7bd42dce2b00`  |
| 2142   | Layout 1             | `7bd42dce2b00`  |
| 2138   | Layout 1             | `7bd42dce2b00`  |
| 2134   | Layout 1             | `7bd42dce2b00`  |
| 2130   | Layout 1             | `7bd42dce2b00`  |
| 2122   | Layout 1             | `7bd42dce2b00`  |
| 2107   | Layout 1             | `7bd42dce2b00`  |
| 2098   | Layout 1             | `7bd42dce2b00`  |
| 2089   | Layout 1             | `7bd42dce2b00`  |
| 2081   | Layout 1             | `7bd42dce2b00`  |
| 2073   | Layout 1             | `7bd42dce2b00`  |
| 2067   | Layout 1             | `7bd42dce2b00`  |
| 2063   | Layout 1             | `7bd42dce2b00`  |
| 2059   | Layout 1             | `7bd42dce2b00`  |
| 2052   | Layout 1             | `7bd42dce2b00`  |
| 2044   | Layout 1             | `7bd42dce2b00`  |
| 2039   | Layout 1             | `7bd42dce2b00`  |
| 2032   | Layout 1             | `7bd42dce2b00`  |
| 2025   | Layout 1             | `7bd42dce2b00`  |
| 2011   | Layout 1             | `7bd42dce2b00`  |
| 2005   | Layout 1             | `7bd42dce2b00`  |
| 2000   | Layout 1             | `7bd42dce2b00`  |
| 1996   | Layout 1             | `7bd42dce2b00`  |
| 1991   | Layout 1             | `7bd42dce2b00`  |
| 1985   | Layout 1             | `7bd42dce2b00`  |
| 1980   | Layout 1             | `7bd42dce2b00`  |
| 1969   | Layout 1             | `7bd42dce2b00`  |
| 1964   | Layout 1             | `7bd42dce2b00`  |
| 1958   | Layout 1             | `7bd42dce2b00`  |
| 1950   | Layout 1             | `7bd42dce2b00`  |
| 1945   | Layout 1             | `7bd42dce2b00`  |
| 1937   | Layout 1             | `7bd42dce2b00`  |
| 1933   | Layout 1             | `7bd42dce2b00`  |
| 1927   | Layout 1             | `7bd42dce2b00`  |
| 1921   | Layout 1             | `7bd42dce2b00`  |
| 1914   | Layout 1             | `7bd42dce2b00`  |
| 1908   | Layout 1             | `7bd42dce2b00`  |
| 1897   | Layout 1             | `7bd42dce2b00`  |
| 1892   | Layout 1             | `7bd42dce2b00`  |
| 1886   | Layout 1             | `7bd42dce2b00`  |
| 1881   | Layout 1             | `7bd42dce2b00`  |
| 1871   | Layout 1             | `7bd42dce2b00`  |
| 1866   | Layout 1             | `7bd42dce2b00`  |
| 1862   | Layout 1             | `7bd42dce2b00`  |
| 1854   | Layout 1             | `7bd42dce2b00`  |
| 1846   | Layout 1             | `7bd42dce2b00`  |
| 1838   | Layout 1             | `7bd42dce2b00`  |
| 1832   | Layout 1             | `7bd42dce2b00`  |
| 1826   | Layout 1             | `7bd42dce2b00`  |
| 1822   | Layout 1             | `7bd42dce2b00`  |
| 1818   | Layout 1             | `7bd42dce2b00`  |
| 1804   | Layout 1             | `7bd42dce2b00`  |
| 1794   | Layout 1             | `7bd42dce2b00`  |
| 1790   | Layout 1             | `7bd42dce2b00`  |
| 1784   | Layout 1             | `7bd42dce2b00`  |
| 1774   | Layout 1             | `7bd42dce2b00`  |
| 1771   | Layout 1             | `7bd42dce2b00`  |
| 1762   | Layout 1             | `7bd42dce2b00`  |
| 1759   | Layout 1             | `7bd42dce2b00`  |
| 1754   | Layout 1             | `7bd42dce2b00`  |
| 1749   | Layout 1             | `7bd42dce2b00`  |
| 1743   | Layout 1             | `7bd42dce2b00`  |
| 1737   | Layout 1             | `7bd42dce2b00`  |
| 1731   | Layout 1             | `7bd42dce2b00`  |
| 1725   | Layout 1             | `7bd42dce2b00`  |
| 1717   | Layout 1             | `7bd42dce2b00`  |
| 1710   | Layout 1             | `7bd42dce2b00`  |
| 1704   | Layout 1             | `7bd42dce2b00`  |
| 1698   | Layout 1             | `7bd42dce2b00`  |
| 1690   | Layout 1             | `7bd42dce2b00`  |
| 1685   | Layout 1             | `7bd42dce2b00`  |
| 1680   | Layout 1             | `7bd42dce2b00`  |
| 1674   | Layout 1             | `7bd42dce2b00`  |
| 1668   | Layout 1             | `7bd42dce2b00`  |
| 1659   | Layout 1             | `7bd42dce2b00`  |
| 1649   | Layout 1             | `7bd42dce2b00`  |
| 1642   | Layout 1             | `7bd42dce2b00`  |
| 1636   | Layout 1             | `7bd42dce2b00`  |
| 1628   | Layout 1             | `7bd42dce2b00`  |
| 1622   | Layout 1             | `7bd42dce2b00`  |
| 1614   | Layout 1             | `7bd42dce2b00`  |
| 1608   | Layout 1             | `7bd42dce2b00`  |
| 1602   | Layout 1             | `7bd42dce2b00`  |
| 1598   | Layout 1             | `7bd42dce2b00`  |
| 1594   | Layout 1             | `7bd42dce2b00`  |
| 1590   | Layout 1             | `7bd42dce2b00`  |
| 1587   | Layout 1             | `7bd42dce2b00`  |
| 1584   | Layout 1             | `7bd42dce2b00`  |
| 1579   | Layout 1             | `7bd42dce2b00`  |
| 1572   | Layout 1             | `7bd42dce2b00`  |
| 1565   | Layout 1             | `7bd42dce2b00`  |
| 1559   | Layout 1             | `7bd42dce2b00`  |
| 1554   | Layout 1             | `7bd42dce2b00`  |
| 1547   | Layout 1             | `7bd42dce2b00`  |
| 1537   | Layout 1             | `7bd42dce2b00`  |
| 1529   | Layout 1             | `7bd42dce2b00`  |
| 1524   | Layout 1             | `7bd42dce2b00`  |
| 1519   | Layout 1             | `7bd42dce2b00`  |
| 1509   | Layout 1             | `7bd42dce2b00`  |
| 1506   | Layout 1             | `7bd42dce2b00`  |
| 1504   | Layout 1             | `7bd42dce2b00`  |
| 1500   | Layout 1             | `7bd42dce2b00`  |
| 1493   | Layout 1             | `7bd42dce2b00`  |
| 1489   | Layout 1             | `7bd42dce2b00`  |
| 1485   | Layout 1             | `7bd42dce2b00`  |
| 1481   | Layout 1             | `7bd42dce2b00`  |
| 1474   | Layout 1             | `7bd42dce2b00`  |
| 1466   | Layout 1             | `7bd42dce2b00`  |
| 1462   | Layout 1             | `7bd42dce2b00`  |
| 1459   | Layout 1             | `7bd42dce2b00`  |
| 1453   | Layout 1             | `7bd42dce2b00`  |
| 1450   | Layout 1             | `7bd42dce2b00`  |
| 1445   | Layout 1             | `7bd42dce2b00`  |
| 1439   | Layout 1             | `7bd42dce2b00`  |
| 1433   | Layout 1             | `7bd42dce2b00`  |
| 1430   | Layout 1             | `7bd42dce2b00`  |
| 1426   | Layout 1             | `7bd42dce2b00`  |
| 1421   | Layout 1             | `7bd42dce2b00`  |
| 1417   | Layout 1             | `7bd42dce2b00`  |
| 1416   | Layout 1             | `7bd42dce2b00`  |
| 1409   | Layout 1             | `7bd42dce2b00`  |
| 1405   | Layout 1             | `7bd42dce2b00`  |
| 1401   | Layout 1             | `7bd42dce2b00`  |
| 1396   | Layout 1             | `7bd42dce2b00`  |
| 1391   | Layout 1             | `7bd42dce2b00`  |
| 1390   | Layout 1             | `7bd42dce2b00`  |
| 1386   | Layout 1             | `7bd42dce2b00`  |
| 1381   | Layout 1             | `7bd42dce2b00`  |
| 1379   | Layout 1             | `7bd42dce2b00`  |
| 1372   | Layout 1             | `7bd42dce2b00`  |
| 1366   | Layout 1             | `7bd42dce2b00`  |
| 1364   | Layout 1             | `7bd42dce2b00`  |
| 1363   | Layout 1             | `7bd42dce2b00`  |
| 1360   | Layout 1             | `7bd42dce2b00`  |
| 1358   | Layout 1             | `7bd42dce2b00`  |
| 1355   | Layout 1             | `7bd42dce2b00`  |
| 1351   | Layout 1             | `7bd42dce2b00`  |
| 1348   | Layout 1             | `7bd42dce2b00`  |
| 1346   | Layout 1             | `7bd42dce2b00`  |
| 1341   | No documented layout | `7bd42dce2b00`  |
| 1340   | No documented layout | `7bd42dce2b00`  |
| 1338   | No documented layout | `7bd42dce2b00`  |
| 1335   | No documented layout | `7bd42dce2b00`  |
| 1333   | No documented layout | `7bd42dce2b00`  |
| 1329   | No documented layout | `7bd42dce2b00`  |
| 1327   | No documented layout | `7bd42dce2b00`  |
| 1324   | No documented layout | `7bd42dce2b00`  |
| 1321   | No documented layout | `7bd42dce2b00`  |
| 1319   | No documented layout | `7bd42dce2b00`  |
| 1318   | No documented layout | `7bd42dce2b00`  |
| 1316   | No documented layout | `7bd42dce2b00`  |
| 1313   | No documented layout | `7bd42dce2b00`  |
| 1311   | No documented layout | `7bd42dce2b00`  |
| 1309   | No documented layout | `7bd42dce2b00`  |
| 1304   | No documented layout | `7bd42dce2b00`  |
| 1292   | No documented layout | `7bd42dce2b00`  |
| 1286   | No documented layout | `7bd42dce2b00`  |
| 1280   | No documented layout | `7bd42dce2b00`  |
| 1276   | No documented layout | `7bd42dce2b00`  |
| 1267   | No documented layout | `7bd42dce2b00`  |
| 1261   | No documented layout | `7bd42dce2b00`  |
| 1256   | No documented layout | `7bd42dce2b00`  |
| 1250   | No file              | `7bd42dce2b00`  |
| 1246   | No file              | `7bd42dce2b00`  |
| 1239   | No file              | `7bd42dce2b00`  |
| 1230   | No file              | `7bd42dce2b00`  |
| 1226   | No file              | `7bd42dce2b00`  |
| 1220   | No file              | `7bd42dce2b00`  |
| 1217   | No file              | `7bd42dce2b00`  |
| 1211   | No file              | `7bd42dce2b00`  |
| 1210   | No file              | `7bd42dce2b00`  |
| 1208   | No file              | `7bd42dce2b00`  |
| 1203   | No file              | `7bd42dce2b00`  |
| 1197   | No file              | `7bd42dce2b00`  |
| 1194   | No file              | `7bd42dce2b00`  |
| 1192   | No file              | `7bd42dce2b00`  |
| 1187   | No file              | `7bd42dce2b00`  |
| 1183   | No file              | `7bd42dce2b00`  |
| 1177   | No file              | `7bd42dce2b00`  |
| 1173   | No file              | `7bd42dce2b00`  |
| 1167   | No file              | `7bd42dce2b00`  |
| 1164   | No file              | `7bd42dce2b00`  |
| 1156   | No file              | `7bd42dce2b00`  |
| 1149   | No file              | `7bd42dce2b00`  |
| 1144   | No file              | `7bd42dce2b00`  |
| 1137   | No file              | `7bd42dce2b00`  |
| 1132   | No file              | `7bd42dce2b00`  |
| 1127   | No file              | `7bd42dce2b00`  |
| 1122   | No file              | `7bd42dce2b00`  |
| 1118   | No file              | `7bd42dce2b00`  |
| 1114   | No file              | `7bd42dce2b00`  |
| 1109   | No file              | `7bd42dce2b00`  |
| 1102   | No file              | `7bd42dce2b00`  |
| 1096   | No file              | `7bd42dce2b00`  |
| 1088   | No file              | `7bd42dce2b00`  |
| 1081   | No file              | `7bd42dce2b00`  |
| 1076   | No file              | `7bd42dce2b00`  |
| 1069   | No file              | `7bd42dce2b00`  |
| 1064   | No file              | `7bd42dce2b00`  |
| 1058   | No file              | `7bd42dce2b00`  |
| 1051   | No file              | `7bd42dce2b00`  |
| 1044   | No file              | `7bd42dce2b00`  |
| 1036   | No file              | `7bd42dce2b00`  |
| 1026   | No file              | `7bd42dce2b00`  |
| 1016   | No file              | `7bd42dce2b00`  |
| 1009   | No file              | `7bd42dce2b00`  |
| 1005   | No file              | `7bd42dce2b00`  |
| 1000   | No file              | `7bd42dce2b00`  |
| 998    | No file              | `7bd42dce2b00`  |
| 990    | No file              | `7bd42dce2b00`  |
| 979    | No file              | `7bd42dce2b00`  |
| 972    | No file              | `7bd42dce2b00`  |
| 963    | No file              | `7bd42dce2b00`  |
| 955    | No file              | `7bd42dce2b00`  |
| 946    | No file              | `7bd42dce2b00`  |
| 938    | No file              | `7bd42dce2b00`  |
| 927    | No file              | `7bd42dce2b00`  |
| 911    | No file              | `7bd42dce2b00`  |
| 904    | No file              | `7bd42dce2b00`  |
| 899    | No file              | `7bd42dce2b00`  |
| 894    | No file              | `7bd42dce2b00`  |
| 885    | No file              | `7bd42dce2b00`  |
| 879    | No file              | `7bd42dce2b00`  |
| 872    | No file              | `7bd42dce2b00`  |
| 864    | No file              | `7bd42dce2b00`  |
| 855    | No file              | `7bd42dce2b00`  |
| 853    | No file              | `7bd42dce2b00`  |
| 845    | No file              | `7bd42dce2b00`  |
| 837    | No file              | `7bd42dce2b00`  |
| 829    | No file              | `7bd42dce2b00`  |
| 822    | No file              | `7bd42dce2b00`  |
| 814    | No file              | `7bd42dce2b00`  |
| 805    | No file              | `7bd42dce2b00`  |
| 794    | No file              | `7bd42dce2b00`  |
| 787    | No file              | `7bd42dce2b00`  |
| 780    | No file              | `7bd42dce2b00`  |
| 771    | No file              | `7bd42dce2b00`  |
| 760    | No file              | `7bd42dce2b00`  |
| 748    | No file              | `7bd42dce2b00`  |
| 741    | No file              | `7bd42dce2b00`  |
| 736    | No file              | `7bd42dce2b00`  |
| 731    | No file              | `7bd42dce2b00`  |
| 723    | No file              | `7bd42dce2b00`  |
| 711    | No file              | `7bd42dce2b00`  |
| 707    | No file              | `7bd42dce2b00`  |
| 697    | No file              | `7bd42dce2b00`  |
| 689    | No file              | `7bd42dce2b00`  |
| 683    | No file              | `7bd42dce2b00`  |
| 678    | No file              | `7bd42dce2b00`  |
| 670    | No file              | `7bd42dce2b00`  |
| 661    | No file              | `7bd42dce2b00`  |
| 656    | No file              | `7bd42dce2b00`  |
| 652    | No file              | `7bd42dce2b00`  |
| 643    | No file              | `7bd42dce2b00`  |
| 637    | No file              | `7bd42dce2b00`  |
| 630    | No file              | `7bd42dce2b00`  |
| 627    | No file              | `7bd42dce2b00`  |
| 621    | No file              | `7bd42dce2b00`  |
| 617    | No file              | `7bd42dce2b00`  |
| 615    | No file              | `7bd42dce2b00`  |
| 606    | No file              | `7bd42dce2b00`  |
| 599    | No file              | `7bd42dce2b00`  |
| 592    | No file              | `7bd42dce2b00`  |
| 586    | No file              | `7bd42dce2b00`  |
| 577    | No file              | `7bd42dce2b00`  |
| 569    | No file              | `7bd42dce2b00`  |
| 561    | No file              | `7bd42dce2b00`  |
| 554    | No file              | `7bd42dce2b00`  |
| 542    | No file              | `7bd42dce2b00`  |
| 532    | No file              | `7bd42dce2b00`  |
| 531    | No file              | `7bd42dce2b00`  |
| 526    | No file              | `7bd42dce2b00`  |
| 521    | No file              | `7bd42dce2b00`  |
| 517    | No file              | `7bd42dce2b00`  |
| 510    | No file              | `7bd42dce2b00`  |
| 508    | No file              | `7bd42dce2b00`  |
| 504    | No file              | `7bd42dce2b00`  |
| 497    | No file              | `7bd42dce2b00`  |
| 491    | No file              | `7bd42dce2b00`  |
| 485    | No file              | `7bd42dce2b00`  |
| 478    | No file              | `7bd42dce2b00`  |
| 472    | No file              | `7bd42dce2b00`  |
| 466    | No file              | `7bd42dce2b00`  |
| 457    | No file              | `7bd42dce2b00`  |
| 452    | No file              | `7bd42dce2b00`  |
| 449    | No file              | `7bd42dce2b00`  |
| 435    | No file              | `7bd42dce2b00`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                                       |
| ------------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `socialactionoffset.dbss` | Optional | `social_action_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`     | Optional | LOC type 15, `str_id1` = `social_action_key`: `str_id4` `0` name, `1` chat command, `2` keywords, `3` condition message |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 77 bytes + texts and contents groups)

| Offset                       | Type                        | Field                           | Notes                                                                                           |
| ---------------------------- | --------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------- |
| `+0x00`                      | u16                         | social_action_key               | Row key; the rows are in no key order (client 3482 opens with 96, 79, 78)                       |
| `+0x02`                      | u16                         | social_action_key_dup           | Equals `social_action_key` on every row; the index points here                                 |
| `+0x04`                      | str16                       | name_kr                         | Korean name (`손 흔들기`, Wave)                                                                  |
| `name_kr+0x00`               | str16                       | condition                       | Unlock script (`checksocialaction(96);checkclass(0);<or>...`, `getLevel()>9`); empty on 15 rows of client 3482 |
| `condition+0x00`             | str16                       | chatting_command_kr             | Korean chat command (`손`)                                                                       |
| `chatting_command_kr+0x00`   | u32                         | chatting_command_hash           | `key_hash()` of the lower-cased command; 86 of 86 rows on client 3482                           |
| `chatting_command_kr+0x04`   | str16                       | chatting_keywords_kr            | Korean chat keywords, `;`-separated (`하이;ㅎㅇ`)                                                |
| `chatting_keywords_kr+0x00`  | str8                        | action_name                     | Action chart name (`SOCIAL_Bye`)                                                                |
| `action_name+0x00`           | u32                         | action_hash                     | `ascii_key_hash()` of `action_name`; 86 of 86 rows on client 3482                               |
| `action_name+0x04`           | str16                       | icon_path                       | Icon under `ui_texture/icon/` (`New_Icon/10_SocialAction/SocialAction0006.dds`)                 |
| `icon_path+0x00`             | str16                       | condition_message_kr            | Korean text the window shows for a locked action; empty on 28 rows of client 3482               |
| `condition_message_kr+0x00`  | u32                         | contents_group_count            | Number of `contents_group_hashes`, `1` to `3` on client 3482                                    |
| `condition_message_kr+0x04`  | u32[contents_group_count]   | contents_group_hashes           | Contents groups as `key_hash()` of their decimal key; group `0` is `0x6016CFF7`                 |
| `contents_group_hashes+0x00` | u32                         | unknown_contents_group_hashes_00 | `0` on every row of clients 1784 and 3482                                                      |
| `contents_group_hashes+0x04` | u8                          | unknown_contents_group_hashes_04 | `0`, `1` or `2`; see Open Questions                                                            |

The hash functions are in `_common/string_hash.py`; the contents group keys
behind the hashes come from `_common/contents_group.py`, and all 100 hashes
of client 3482 resolve.

### `socialactionoffset.dbss`

Bare offset table into `socialaction.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `socialaction.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (10 bytes)

| Offset  | Type | Field             | Notes                                                                               |
| ------- | ---- | ----------------- | ----------------------------------------------------------------------------------- |
| `+0x00` | u16  | social_action_key | Key of the row it points at                                                         |
| `+0x02` | u32  | data_offset       | Absolute offset in `socialaction.dbss` of the row's `social_action_key_dup`, 2 bytes past the row start |
| `+0x06` | u32  | data_size         | The row without its leading `social_action_key`                                     |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on client 3482 every index row points at the row
with its key.

## Layout 1

No `unknown_contents_group_hashes_04` byte at the end of the row. Only the
Row differs from Layout 2.

### Row (variable: 76 bytes + texts and contents groups)

| Offset                       | Type                        | Field                            | Notes                       |
| ---------------------------- | --------------------------- | -------------------------------- | --------------------------- |
| `+0x00`                      | u16                         | social_action_key                |                             |
| `+0x02`                      | u16                         | social_action_key_dup            |                             |
| `+0x04`                      | str16                       | name_kr                          |                             |
| `name_kr+0x00`               | str16                       | condition                        |                             |
| `condition+0x00`             | str16                       | chatting_command_kr              |                             |
| `chatting_command_kr+0x00`   | u32                         | chatting_command_hash            |                             |
| `chatting_command_kr+0x04`   | str16                       | chatting_keywords_kr             |                             |
| `chatting_keywords_kr+0x00`  | str8                        | action_name                      |                             |
| `action_name+0x00`           | u32                         | action_hash                      |                             |
| `action_name+0x04`           | str16                       | icon_path                        |                             |
| `icon_path+0x00`             | str16                       | condition_message_kr             |                             |
| `condition_message_kr+0x00`  | u32                         | contents_group_count             |                             |
| `condition_message_kr+0x04`  | u32[contents_group_count]   | contents_group_hashes            |                             |
| `contents_group_hashes+0x00` | u32                         | unknown_contents_group_hashes_00 | `0` on every row (client 1784) |

## Field Names

The 2016 `gc::SocialActionStaticStatus` holds `_key`, `_name`,
`_conditionString`, `_conditions` (parsed, not stored), `_chattingCommand`,
`_chattingCommandHash`, `_chattingKeywordBuffer`, `_actionName`,
`_actionHashKey`, `_iconPath` and `_conditionMessage` in the file's order.
The `SocialAction_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Index`, `SocialActionName`, `UseCondition`,
`ChattingCommand`, `ChattingKeyword`, `ActionName`, `ActionName_Mount`,
`IconImage`, `ConditionMessage` and `ContentsGroupKey` (a comma list), 64
rows; client 3482 shares 56 keys with it.

| Field                 | Column             | Same value (client 3482) |
| --------------------- | ------------------ | ------------------------ |
| social_action_key     | `Index`            | 56 of 56                 |
| name_kr               | `SocialActionName` | 56 of 56                 |
| condition             | `UseCondition`     | 16 of 56                 |
| chatting_command_kr   | `ChattingCommand`  | 56 of 56                 |
| chatting_keywords_kr  | `ChattingKeyword`  | 56 of 56                 |
| action_name           | `ActionName`       | 56 of 56                 |
| icon_path             | `IconImage`        | 56 of 56                 |
| condition_message_kr  | `ConditionMessage` | 52 of 56                 |
| contents_group_hashes | `ContentsGroupKey` | 39 of 56                 |

The `condition` misses are level and quest checks client 3482 has where the
sheet column is empty (`getLevel()>9` on key `15`); the struct member
`_conditionString` names the field. The contents group misses drop a group
the sheet lists (`3,27,111` against `3,27` on key `30`). `ActionName_Mount`
is empty on every sheet row and has no field.

## Notes

- LOC type 15 holds the English text by `social_action_key`: `str_id4` `0`
  name (`Wave`), `1` chat command (`Hand`), `2` keywords (`What's up;Yo`),
  `3` condition message.
- Keys `61` and `62` have the commands `O` and `X`; their hashes are of `o`
  and `x`, so the client lower-cases a command before hashing it.

## Open Questions

### What the Last Byte Selects

`unknown_contents_group_hashes_04` is `2` on 20 rows of client 3482 (keys
`73` to `90`, `94` and `96`; most of their condition messages name the
Pearl Shop or an event), `0` on keys `54`, `60` and `92` (sweeping while
moving, the graduation cap throw and the snowboard) and `1` on the other
63. Client 1784 has no such byte. No Lua getter reads it.

### What the Zero After the Contents Groups Holds

`unknown_contents_group_hashes_00` is `0` on every row of clients 1784 and
3482. It may be the count of a second, always empty list, or the hash of
the empty `ActionName_Mount` column.
