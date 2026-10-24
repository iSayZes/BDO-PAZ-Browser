# `itemgroupingstaticstatus.bss` Format

## Purpose

The item group types of the high-end gear lines: per group type the items
of one line and slot kind, such as the 50 Blackstar main weapons or the 93
Sovereign awakening weapons. The client Lua asks for an item's type with
`ToClient_getItemKeyGroupTypeByTItemKey(itemKey)` and compares it with the
`__eItemGroupType_*` values: the Sovereign weapon creation window
(`panel_makegoonwang_all.luac`) filters its material slots by type, the dye
window (`panel_widget_dye_all_2.luac`) offers the glow dyes of
[`itemeffectgroupstaticstatus.bss`](itemeffectgroupstaticstatus_bss.md)
by it, and the item tooltip (`panel_tooltip_item.luac`) hides the dye lines
of the Sovereign types.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records  | Row bytes                 |
| ------ | -------------- | ------- | ------------------------------ | ----- | -------- | ------------------------- |
| 1      | 3169 and later | 3483    | `itemgroupingstaticstatus.bss` | 2,612 | 12 Group | 21 to 377, 217 on average |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 1      | `itemgroupingstaticstatus.bss` | 2,612 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `58d9fff4cf04`  |
| 3482   | Layout 1 | `58d9fff4cf04`  |
| 3474   | Layout 1 | `58d9fff4cf04`  |
| 3473   | Layout 1 | `58d9fff4cf04`  |
| 3464   | Layout 1 | `58d9fff4cf04`  |
| 3458   | Layout 1 | `58d9fff4cf04`  |
| 3454   | Layout 1 | `58d9fff4cf04`  |
| 3444   | Layout 1 | `58d9fff4cf04`  |
| 3435   | Layout 1 | `58d9fff4cf04`  |
| 3426   | Layout 1 | `58d9fff4cf04`  |
| 3418   | Layout 1 | `58d9fff4cf04`  |
| 3412   | Layout 1 | `58d9fff4cf04`  |
| 3402   | Layout 1 | `58d9fff4cf04`  |
| 3396   | Layout 1 | `58d9fff4cf04`  |
| 3387   | Layout 1 | `58d9fff4cf04`  |
| 3381   | Layout 1 | `58d9fff4cf04`  |
| 3373   | Layout 1 | `58d9fff4cf04`  |
| 3364   | Layout 1 | `58d9fff4cf04`  |
| 3356   | Layout 1 | `58d9fff4cf04`  |
| 3349   | Layout 1 | `58d9fff4cf04`  |
| 3342   | Layout 1 | `58d9fff4cf04`  |
| 3335   | Layout 1 | `58d9fff4cf04`  |
| 3326   | Layout 1 | `58d9fff4cf04`  |
| 3321   | Layout 1 | `58d9fff4cf04`  |
| 3314   | Layout 1 | `58d9fff4cf04`  |
| 3303   | Layout 1 | `58d9fff4cf04`  |
| 3302   | Layout 1 | `58d9fff4cf04`  |
| 3293   | Layout 1 | `58d9fff4cf04`  |
| 3283   | Layout 1 | `58d9fff4cf04`  |
| 3275   | Layout 1 | `58d9fff4cf04`  |
| 3267   | Layout 1 | `58d9fff4cf04`  |
| 3258   | Layout 1 | `58d9fff4cf04`  |
| 3251   | Layout 1 | `58d9fff4cf04`  |
| 3242   | Layout 1 | `58d9fff4cf04`  |
| 3235   | Layout 1 | `58d9fff4cf04`  |
| 3229   | Layout 1 | `58d9fff4cf04`  |
| 3212   | Layout 1 | `58d9fff4cf04`  |
| 3203   | Layout 1 | `58d9fff4cf04`  |
| 3193   | Layout 1 | `58d9fff4cf04`  |
| 3186   | Layout 1 | `58d9fff4cf04`  |
| 3177   | Layout 1 | `58d9fff4cf04`  |
| 3169   | Layout 1 | `58d9fff4cf04`  |
| 3158   | No file  | `58d9fff4cf04`  |
| 3151   | No file  | `58d9fff4cf04`  |
| 3144   | No file  | `58d9fff4cf04`  |
| 3133   | No file  | `58d9fff4cf04`  |
| 3125   | No file  | `58d9fff4cf04`  |
| 3118   | No file  | `58d9fff4cf04`  |
| 3111   | No file  | `58d9fff4cf04`  |
| 3103   | No file  | `58d9fff4cf04`  |
| 3095   | No file  | `58d9fff4cf04`  |
| 3086   | No file  | `58d9fff4cf04`  |
| 3072   | No file  | `58d9fff4cf04`  |
| 3062   | No file  | `58d9fff4cf04`  |
| 3052   | No file  | `58d9fff4cf04`  |
| 3045   | No file  | `58d9fff4cf04`  |
| 3037   | No file  | `58d9fff4cf04`  |
| 3030   | No file  | `58d9fff4cf04`  |
| 3021   | No file  | `58d9fff4cf04`  |
| 3012   | No file  | `58d9fff4cf04`  |
| 3002   | No file  | `58d9fff4cf04`  |
| 2995   | No file  | `58d9fff4cf04`  |
| 2987   | No file  | `58d9fff4cf04`  |
| 2978   | No file  | `58d9fff4cf04`  |
| 2970   | No file  | `58d9fff4cf04`  |
| 2959   | No file  | `58d9fff4cf04`  |
| 2951   | No file  | `58d9fff4cf04`  |
| 2942   | No file  | `58d9fff4cf04`  |
| 2935   | No file  | `58d9fff4cf04`  |
| 2932   | No file  | `58d9fff4cf04`  |
| 2923   | No file  | `58d9fff4cf04`  |
| 2919   | No file  | `58d9fff4cf04`  |
| 2907   | No file  | `58d9fff4cf04`  |
| 2900   | No file  | `58d9fff4cf04`  |
| 2891   | No file  | `58d9fff4cf04`  |
| 2882   | No file  | `58d9fff4cf04`  |
| 2872   | No file  | `58d9fff4cf04`  |
| 2863   | No file  | `58d9fff4cf04`  |
| 2855   | No file  | `58d9fff4cf04`  |
| 2849   | No file  | `58d9fff4cf04`  |
| 2844   | No file  | `58d9fff4cf04`  |
| 2834   | No file  | `58d9fff4cf04`  |
| 2825   | No file  | `58d9fff4cf04`  |
| 2819   | No file  | `58d9fff4cf04`  |
| 2811   | No file  | `58d9fff4cf04`  |
| 2803   | No file  | `58d9fff4cf04`  |
| 2794   | No file  | `58d9fff4cf04`  |
| 2783   | No file  | `58d9fff4cf04`  |
| 2774   | No file  | `58d9fff4cf04`  |
| 2765   | No file  | `58d9fff4cf04`  |
| 2756   | No file  | `58d9fff4cf04`  |
| 2750   | No file  | `58d9fff4cf04`  |
| 2743   | No file  | `58d9fff4cf04`  |
| 2736   | No file  | `58d9fff4cf04`  |
| 2726   | No file  | `58d9fff4cf04`  |
| 2717   | No file  | `58d9fff4cf04`  |
| 2709   | No file  | `58d9fff4cf04`  |
| 2703   | No file  | `58d9fff4cf04`  |
| 2695   | No file  | `58d9fff4cf04`  |
| 2684   | No file  | `58d9fff4cf04`  |
| 2672   | No file  | `58d9fff4cf04`  |
| 2665   | No file  | `58d9fff4cf04`  |
| 2657   | No file  | `58d9fff4cf04`  |
| 2649   | No file  | `58d9fff4cf04`  |
| 2644   | No file  | `58d9fff4cf04`  |
| 2637   | No file  | `58d9fff4cf04`  |
| 2629   | No file  | `58d9fff4cf04`  |
| 2619   | No file  | `58d9fff4cf04`  |
| 2612   | No file  | `58d9fff4cf04`  |
| 2606   | No file  | `58d9fff4cf04`  |
| 2602   | No file  | `58d9fff4cf04`  |
| 2601   | No file  | `58d9fff4cf04`  |
| 2592   | No file  | `58d9fff4cf04`  |
| 2583   | No file  | `58d9fff4cf04`  |
| 2575   | No file  | `58d9fff4cf04`  |
| 2567   | No file  | `58d9fff4cf04`  |
| 2560   | No file  | `58d9fff4cf04`  |
| 2553   | No file  | `58d9fff4cf04`  |
| 2545   | No file  | `58d9fff4cf04`  |
| 2538   | No file  | `58d9fff4cf04`  |
| 2529   | No file  | `58d9fff4cf04`  |
| 2519   | No file  | `58d9fff4cf04`  |
| 2513   | No file  | `58d9fff4cf04`  |
| 2510   | No file  | `58d9fff4cf04`  |
| 2507   | No file  | `58d9fff4cf04`  |
| 2503   | No file  | `58d9fff4cf04`  |
| 2498   | No file  | `58d9fff4cf04`  |
| 2492   | No file  | `58d9fff4cf04`  |
| 2487   | No file  | `58d9fff4cf04`  |
| 2480   | No file  | `58d9fff4cf04`  |
| 2474   | No file  | `58d9fff4cf04`  |
| 2468   | No file  | `58d9fff4cf04`  |
| 2460   | No file  | `58d9fff4cf04`  |
| 2453   | No file  | `58d9fff4cf04`  |
| 2444   | No file  | `58d9fff4cf04`  |
| 2438   | No file  | `58d9fff4cf04`  |
| 2434   | No file  | `58d9fff4cf04`  |
| 2429   | No file  | `58d9fff4cf04`  |
| 2421   | No file  | `58d9fff4cf04`  |
| 2414   | No file  | `58d9fff4cf04`  |
| 2407   | No file  | `58d9fff4cf04`  |
| 2401   | No file  | `58d9fff4cf04`  |
| 2397   | No file  | `58d9fff4cf04`  |
| 2393   | No file  | `58d9fff4cf04`  |
| 2384   | No file  | `58d9fff4cf04`  |
| 2378   | No file  | `58d9fff4cf04`  |
| 2372   | No file  | `58d9fff4cf04`  |
| 2358   | No file  | `58d9fff4cf04`  |
| 2352   | No file  | `58d9fff4cf04`  |
| 2347   | No file  | `58d9fff4cf04`  |
| 2343   | No file  | `58d9fff4cf04`  |
| 2335   | No file  | `58d9fff4cf04`  |
| 2327   | No file  | `58d9fff4cf04`  |
| 2324   | No file  | `58d9fff4cf04`  |
| 2319   | No file  | `58d9fff4cf04`  |
| 2313   | No file  | `58d9fff4cf04`  |
| 2308   | No file  | `58d9fff4cf04`  |
| 2302   | No file  | `58d9fff4cf04`  |
| 2295   | No file  | `58d9fff4cf04`  |
| 2290   | No file  | `58d9fff4cf04`  |
| 2284   | No file  | `58d9fff4cf04`  |
| 2276   | No file  | `58d9fff4cf04`  |
| 2269   | No file  | `58d9fff4cf04`  |
| 2259   | No file  | `58d9fff4cf04`  |
| 2250   | No file  | `58d9fff4cf04`  |
| 2243   | No file  | `58d9fff4cf04`  |
| 2235   | No file  | `58d9fff4cf04`  |
| 2229   | No file  | `58d9fff4cf04`  |
| 2224   | No file  | `58d9fff4cf04`  |
| 2218   | No file  | `58d9fff4cf04`  |
| 2215   | No file  | `58d9fff4cf04`  |
| 2207   | No file  | `58d9fff4cf04`  |
| 2203   | No file  | `58d9fff4cf04`  |
| 2196   | No file  | `58d9fff4cf04`  |
| 2192   | No file  | `58d9fff4cf04`  |
| 2189   | No file  | `58d9fff4cf04`  |
| 2183   | No file  | `58d9fff4cf04`  |
| 2179   | No file  | `58d9fff4cf04`  |
| 2171   | No file  | `58d9fff4cf04`  |
| 2163   | No file  | `58d9fff4cf04`  |
| 2156   | No file  | `58d9fff4cf04`  |
| 2151   | No file  | `58d9fff4cf04`  |
| 2147   | No file  | `58d9fff4cf04`  |
| 2142   | No file  | `58d9fff4cf04`  |
| 2138   | No file  | `58d9fff4cf04`  |
| 2134   | No file  | `58d9fff4cf04`  |
| 2130   | No file  | `58d9fff4cf04`  |
| 2122   | No file  | `58d9fff4cf04`  |
| 2107   | No file  | `58d9fff4cf04`  |
| 2098   | No file  | `58d9fff4cf04`  |
| 2089   | No file  | `58d9fff4cf04`  |
| 2081   | No file  | `58d9fff4cf04`  |
| 2073   | No file  | `58d9fff4cf04`  |
| 2067   | No file  | `58d9fff4cf04`  |
| 2063   | No file  | `58d9fff4cf04`  |
| 2059   | No file  | `58d9fff4cf04`  |
| 2052   | No file  | `58d9fff4cf04`  |
| 2044   | No file  | `58d9fff4cf04`  |
| 2039   | No file  | `58d9fff4cf04`  |
| 2032   | No file  | `58d9fff4cf04`  |
| 2025   | No file  | `58d9fff4cf04`  |
| 2011   | No file  | `58d9fff4cf04`  |
| 2005   | No file  | `58d9fff4cf04`  |
| 2000   | No file  | `58d9fff4cf04`  |
| 1996   | No file  | `58d9fff4cf04`  |
| 1991   | No file  | `58d9fff4cf04`  |
| 1985   | No file  | `58d9fff4cf04`  |
| 1980   | No file  | `58d9fff4cf04`  |
| 1969   | No file  | `58d9fff4cf04`  |
| 1964   | No file  | `58d9fff4cf04`  |
| 1958   | No file  | `58d9fff4cf04`  |
| 1950   | No file  | `58d9fff4cf04`  |
| 1945   | No file  | `58d9fff4cf04`  |
| 1937   | No file  | `58d9fff4cf04`  |
| 1933   | No file  | `58d9fff4cf04`  |
| 1927   | No file  | `58d9fff4cf04`  |
| 1921   | No file  | `58d9fff4cf04`  |
| 1914   | No file  | `58d9fff4cf04`  |
| 1908   | No file  | `58d9fff4cf04`  |
| 1897   | No file  | `58d9fff4cf04`  |
| 1892   | No file  | `58d9fff4cf04`  |
| 1886   | No file  | `58d9fff4cf04`  |
| 1881   | No file  | `58d9fff4cf04`  |
| 1871   | No file  | `58d9fff4cf04`  |
| 1866   | No file  | `58d9fff4cf04`  |
| 1862   | No file  | `58d9fff4cf04`  |
| 1854   | No file  | `58d9fff4cf04`  |
| 1846   | No file  | `58d9fff4cf04`  |
| 1838   | No file  | `58d9fff4cf04`  |
| 1832   | No file  | `58d9fff4cf04`  |
| 1826   | No file  | `58d9fff4cf04`  |
| 1822   | No file  | `58d9fff4cf04`  |
| 1818   | No file  | `58d9fff4cf04`  |
| 1804   | No file  | `58d9fff4cf04`  |
| 1794   | No file  | `58d9fff4cf04`  |
| 1790   | No file  | `58d9fff4cf04`  |
| 1784   | No file  | `58d9fff4cf04`  |
| 1774   | No file  | `58d9fff4cf04`  |
| 1771   | No file  | `58d9fff4cf04`  |
| 1762   | No file  | `58d9fff4cf04`  |
| 1759   | No file  | `58d9fff4cf04`  |
| 1754   | No file  | `58d9fff4cf04`  |
| 1749   | No file  | `58d9fff4cf04`  |
| 1743   | No file  | `58d9fff4cf04`  |
| 1737   | No file  | `58d9fff4cf04`  |
| 1731   | No file  | `58d9fff4cf04`  |
| 1725   | No file  | `58d9fff4cf04`  |
| 1717   | No file  | `58d9fff4cf04`  |
| 1710   | No file  | `58d9fff4cf04`  |
| 1704   | No file  | `58d9fff4cf04`  |
| 1698   | No file  | `58d9fff4cf04`  |
| 1690   | No file  | `58d9fff4cf04`  |
| 1685   | No file  | `58d9fff4cf04`  |
| 1680   | No file  | `58d9fff4cf04`  |
| 1674   | No file  | `58d9fff4cf04`  |
| 1668   | No file  | `58d9fff4cf04`  |
| 1659   | No file  | `58d9fff4cf04`  |
| 1649   | No file  | `58d9fff4cf04`  |
| 1642   | No file  | `58d9fff4cf04`  |
| 1636   | No file  | `58d9fff4cf04`  |
| 1628   | No file  | `58d9fff4cf04`  |
| 1622   | No file  | `58d9fff4cf04`  |
| 1614   | No file  | `58d9fff4cf04`  |
| 1608   | No file  | `58d9fff4cf04`  |
| 1602   | No file  | `58d9fff4cf04`  |
| 1598   | No file  | `58d9fff4cf04`  |
| 1594   | No file  | `58d9fff4cf04`  |
| 1590   | No file  | `58d9fff4cf04`  |
| 1587   | No file  | `58d9fff4cf04`  |
| 1584   | No file  | `58d9fff4cf04`  |
| 1579   | No file  | `58d9fff4cf04`  |
| 1572   | No file  | `58d9fff4cf04`  |
| 1565   | No file  | `58d9fff4cf04`  |
| 1559   | No file  | `58d9fff4cf04`  |
| 1554   | No file  | `58d9fff4cf04`  |
| 1547   | No file  | `58d9fff4cf04`  |
| 1537   | No file  | `58d9fff4cf04`  |
| 1529   | No file  | `58d9fff4cf04`  |
| 1524   | No file  | `58d9fff4cf04`  |
| 1519   | No file  | `58d9fff4cf04`  |
| 1509   | No file  | `58d9fff4cf04`  |
| 1506   | No file  | `58d9fff4cf04`  |
| 1504   | No file  | `58d9fff4cf04`  |
| 1500   | No file  | `58d9fff4cf04`  |
| 1493   | No file  | `58d9fff4cf04`  |
| 1489   | No file  | `58d9fff4cf04`  |
| 1485   | No file  | `58d9fff4cf04`  |
| 1481   | No file  | `58d9fff4cf04`  |
| 1474   | No file  | `58d9fff4cf04`  |
| 1466   | No file  | `58d9fff4cf04`  |
| 1462   | No file  | `58d9fff4cf04`  |
| 1459   | No file  | `58d9fff4cf04`  |
| 1453   | No file  | `58d9fff4cf04`  |
| 1450   | No file  | `58d9fff4cf04`  |
| 1445   | No file  | `58d9fff4cf04`  |
| 1439   | No file  | `58d9fff4cf04`  |
| 1433   | No file  | `58d9fff4cf04`  |
| 1430   | No file  | `58d9fff4cf04`  |
| 1426   | No file  | `58d9fff4cf04`  |
| 1421   | No file  | `58d9fff4cf04`  |
| 1417   | No file  | `58d9fff4cf04`  |
| 1416   | No file  | `58d9fff4cf04`  |
| 1409   | No file  | `58d9fff4cf04`  |
| 1405   | No file  | `58d9fff4cf04`  |
| 1401   | No file  | `58d9fff4cf04`  |
| 1396   | No file  | `58d9fff4cf04`  |
| 1391   | No file  | `58d9fff4cf04`  |
| 1390   | No file  | `58d9fff4cf04`  |
| 1386   | No file  | `58d9fff4cf04`  |
| 1381   | No file  | `58d9fff4cf04`  |
| 1379   | No file  | `58d9fff4cf04`  |
| 1372   | No file  | `58d9fff4cf04`  |
| 1366   | No file  | `58d9fff4cf04`  |
| 1364   | No file  | `58d9fff4cf04`  |
| 1363   | No file  | `58d9fff4cf04`  |
| 1360   | No file  | `58d9fff4cf04`  |
| 1358   | No file  | `58d9fff4cf04`  |
| 1355   | No file  | `58d9fff4cf04`  |
| 1351   | No file  | `58d9fff4cf04`  |
| 1348   | No file  | `58d9fff4cf04`  |
| 1346   | No file  | `58d9fff4cf04`  |
| 1341   | No file  | `58d9fff4cf04`  |
| 1340   | No file  | `58d9fff4cf04`  |
| 1338   | No file  | `58d9fff4cf04`  |
| 1335   | No file  | `58d9fff4cf04`  |
| 1333   | No file  | `58d9fff4cf04`  |
| 1329   | No file  | `58d9fff4cf04`  |
| 1327   | No file  | `58d9fff4cf04`  |
| 1324   | No file  | `58d9fff4cf04`  |
| 1321   | No file  | `58d9fff4cf04`  |
| 1319   | No file  | `58d9fff4cf04`  |
| 1318   | No file  | `58d9fff4cf04`  |
| 1316   | No file  | `58d9fff4cf04`  |
| 1313   | No file  | `58d9fff4cf04`  |
| 1311   | No file  | `58d9fff4cf04`  |
| 1309   | No file  | `58d9fff4cf04`  |
| 1304   | No file  | `58d9fff4cf04`  |
| 1292   | No file  | `58d9fff4cf04`  |
| 1286   | No file  | `58d9fff4cf04`  |
| 1280   | No file  | `58d9fff4cf04`  |
| 1276   | No file  | `58d9fff4cf04`  |
| 1267   | No file  | `58d9fff4cf04`  |
| 1261   | No file  | `58d9fff4cf04`  |
| 1256   | No file  | `58d9fff4cf04`  |
| 1250   | No file  | `58d9fff4cf04`  |
| 1246   | No file  | `58d9fff4cf04`  |
| 1239   | No file  | `58d9fff4cf04`  |
| 1230   | No file  | `58d9fff4cf04`  |
| 1226   | No file  | `58d9fff4cf04`  |
| 1220   | No file  | `58d9fff4cf04`  |
| 1217   | No file  | `58d9fff4cf04`  |
| 1211   | No file  | `58d9fff4cf04`  |
| 1210   | No file  | `58d9fff4cf04`  |
| 1208   | No file  | `58d9fff4cf04`  |
| 1203   | No file  | `58d9fff4cf04`  |
| 1197   | No file  | `58d9fff4cf04`  |
| 1194   | No file  | `58d9fff4cf04`  |
| 1192   | No file  | `58d9fff4cf04`  |
| 1187   | No file  | `58d9fff4cf04`  |
| 1183   | No file  | `58d9fff4cf04`  |
| 1177   | No file  | `58d9fff4cf04`  |
| 1173   | No file  | `58d9fff4cf04`  |
| 1167   | No file  | `58d9fff4cf04`  |
| 1164   | No file  | `58d9fff4cf04`  |
| 1156   | No file  | `58d9fff4cf04`  |
| 1149   | No file  | `58d9fff4cf04`  |
| 1144   | No file  | `58d9fff4cf04`  |
| 1137   | No file  | `58d9fff4cf04`  |
| 1132   | No file  | `58d9fff4cf04`  |
| 1127   | No file  | `58d9fff4cf04`  |
| 1122   | No file  | `58d9fff4cf04`  |
| 1118   | No file  | `58d9fff4cf04`  |
| 1114   | No file  | `58d9fff4cf04`  |
| 1109   | No file  | `58d9fff4cf04`  |
| 1102   | No file  | `58d9fff4cf04`  |
| 1096   | No file  | `58d9fff4cf04`  |
| 1088   | No file  | `58d9fff4cf04`  |
| 1081   | No file  | `58d9fff4cf04`  |
| 1076   | No file  | `58d9fff4cf04`  |
| 1069   | No file  | `58d9fff4cf04`  |
| 1064   | No file  | `58d9fff4cf04`  |
| 1058   | No file  | `58d9fff4cf04`  |
| 1051   | No file  | `58d9fff4cf04`  |
| 1044   | No file  | `58d9fff4cf04`  |
| 1036   | No file  | `58d9fff4cf04`  |
| 1026   | No file  | `58d9fff4cf04`  |
| 1016   | No file  | `58d9fff4cf04`  |
| 1009   | No file  | `58d9fff4cf04`  |
| 1005   | No file  | `58d9fff4cf04`  |
| 1000   | No file  | `58d9fff4cf04`  |
| 998    | No file  | `58d9fff4cf04`  |
| 990    | No file  | `58d9fff4cf04`  |
| 979    | No file  | `58d9fff4cf04`  |
| 972    | No file  | `58d9fff4cf04`  |
| 963    | No file  | `58d9fff4cf04`  |
| 955    | No file  | `58d9fff4cf04`  |
| 946    | No file  | `58d9fff4cf04`  |
| 938    | No file  | `58d9fff4cf04`  |
| 927    | No file  | `58d9fff4cf04`  |
| 911    | No file  | `58d9fff4cf04`  |
| 904    | No file  | `58d9fff4cf04`  |
| 899    | No file  | `58d9fff4cf04`  |
| 894    | No file  | `58d9fff4cf04`  |
| 885    | No file  | `58d9fff4cf04`  |
| 879    | No file  | `58d9fff4cf04`  |
| 872    | No file  | `58d9fff4cf04`  |
| 864    | No file  | `58d9fff4cf04`  |
| 855    | No file  | `58d9fff4cf04`  |
| 853    | No file  | `58d9fff4cf04`  |
| 845    | No file  | `58d9fff4cf04`  |
| 837    | No file  | `58d9fff4cf04`  |
| 829    | No file  | `58d9fff4cf04`  |
| 822    | No file  | `58d9fff4cf04`  |
| 814    | No file  | `58d9fff4cf04`  |
| 805    | No file  | `58d9fff4cf04`  |
| 794    | No file  | `58d9fff4cf04`  |
| 787    | No file  | `58d9fff4cf04`  |
| 780    | No file  | `58d9fff4cf04`  |
| 771    | No file  | `58d9fff4cf04`  |
| 760    | No file  | `58d9fff4cf04`  |
| 748    | No file  | `58d9fff4cf04`  |
| 741    | No file  | `58d9fff4cf04`  |
| 736    | No file  | `58d9fff4cf04`  |
| 731    | No file  | `58d9fff4cf04`  |
| 723    | No file  | `58d9fff4cf04`  |
| 711    | No file  | `58d9fff4cf04`  |
| 707    | No file  | `58d9fff4cf04`  |
| 697    | No file  | `58d9fff4cf04`  |
| 689    | No file  | `58d9fff4cf04`  |
| 683    | No file  | `58d9fff4cf04`  |
| 678    | No file  | `58d9fff4cf04`  |
| 670    | No file  | `58d9fff4cf04`  |
| 661    | No file  | `58d9fff4cf04`  |
| 656    | No file  | `58d9fff4cf04`  |
| 652    | No file  | `58d9fff4cf04`  |
| 643    | No file  | `58d9fff4cf04`  |
| 637    | No file  | `58d9fff4cf04`  |
| 630    | No file  | `58d9fff4cf04`  |
| 627    | No file  | `58d9fff4cf04`  |
| 621    | No file  | `58d9fff4cf04`  |
| 617    | No file  | `58d9fff4cf04`  |
| 615    | No file  | `58d9fff4cf04`  |
| 606    | No file  | `58d9fff4cf04`  |
| 599    | No file  | `58d9fff4cf04`  |
| 592    | No file  | `58d9fff4cf04`  |
| 586    | No file  | `58d9fff4cf04`  |
| 577    | No file  | `58d9fff4cf04`  |
| 569    | No file  | `58d9fff4cf04`  |
| 561    | No file  | `58d9fff4cf04`  |
| 554    | No file  | `58d9fff4cf04`  |
| 542    | No file  | `58d9fff4cf04`  |
| 532    | No file  | `58d9fff4cf04`  |
| 531    | No file  | `58d9fff4cf04`  |
| 526    | No file  | `58d9fff4cf04`  |
| 521    | No file  | `58d9fff4cf04`  |
| 517    | No file  | `58d9fff4cf04`  |
| 510    | No file  | `58d9fff4cf04`  |
| 508    | No file  | `58d9fff4cf04`  |
| 504    | No file  | `58d9fff4cf04`  |
| 497    | No file  | `58d9fff4cf04`  |
| 491    | No file  | `58d9fff4cf04`  |
| 485    | No file  | `58d9fff4cf04`  |
| 478    | No file  | `58d9fff4cf04`  |
| 472    | No file  | `58d9fff4cf04`  |
| 466    | No file  | `58d9fff4cf04`  |
| 457    | No file  | `58d9fff4cf04`  |
| 452    | No file  | `58d9fff4cf04`  |
| 449    | No file  | `58d9fff4cf04`  |
| 435    | No file  | `58d9fff4cf04`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field       | Notes                                            |
| ------- | ------------------ | ----------- | ------------------------------------------------ |
| `+0x00` | u32                | group_count | Number of groups; no PABR magic, no string table |
| `+0x04` | Group[group_count] | groups      | See Group; from the highest type down            |

### Group (variable: 5 bytes + item IDs)

| Offset  | Type             | Field           | Notes                                                    |
| ------- | ---------------- | --------------- | -------------------------------------------------------- |
| `+0x00` | u8               | item_group_type | Group type, `0` to `11` on client 3482; see Group Types  |
| `+0x01` | u32              | item_count      | Number of `item_ids`                                     |
| `+0x05` | u32[item_count]  | item_ids        | Item IDs (enhancement level `0` in the high byte on every entry of client 3482) |

## Group Types

The items of each group on client 3482, and the `__eItemGroupType_*` name
of the client 3482 Lua whose use fits them (see Open Questions).

| Type | Items (client 3482)                                       | Lua name that fits       |
| ---- | --------------------------------------------------------- | ------------------------ |
| 0    | 50 Blackstar main weapons (Blackstar Longsword)           | `BlackStarMain`          |
| 1    | 50 Kzarka main weapons                                    | `KzakaMain`              |
| 2    | 50 Offin Tett's Radiant main weapons                      | `OpinMain`               |
| 3    | 62 Blackstar awakening weapons                            | `BlackStarAwaken`        |
| 4    | 62 Dandelion awakening weapons                            | `DandelionAwaken`        |
| 5    | 48 Blackstar sub-weapons                                  | `BlackStarSub`           |
| 6    | 48 Nouver sub-weapons                                     | `NuverSub`               |
| 7    | 48 Kutum sub-weapons                                      | `KutumSub`               |
| 8    | 50 Sovereign main weapons, Fiery Sovereign included       | `GoonWangMain`           |
| 9    | 72 Sovereign sub-weapons, Fiery Sovereign included        | `GoonWangSub`            |
| 10   | 93 Sovereign awakening weapons, Storm Devoured included   | `GoonWangAwaken`         |
| 11   | 4 Edana armor items (Edana - Heavensmite, Abyssveil, Oathgrip, Furystride) | `EdanaArmor` |

## Notes

- Types `8` to `11` are the group keys of
  [`itemeffectgroupstaticstatus.bss`](itemeffectgroupstaticstatus_bss.md),
  the item groups that take a glow dye; the dye window checks for
  `GoonWangMain`, `GoonWangSub`, `GoonWangAwaken` and `EdanaArmor`.
- The file is not in the client 1784 PAZ.
- The handler (`_bss/itemgroupingstaticstatus/`) shows one row per group
  with its items.

## Open Questions

### Which `__eItemGroupType_` Value Each Type Is

The client Lua uses the `__eItemGroupType_*` names but never their numbers,
which come from the game client. The order of the Group Types table puts
each Lua name on the group whose items it names; no Lua or file value
confirms the numbers.
