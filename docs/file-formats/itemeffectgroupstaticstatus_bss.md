# `itemeffectgroupstaticstatus.bss` Format

## Purpose

The glow effects a dye can give the Sovereign weapons and the Edana armor:
per item group type of
[`itemgroupingstaticstatus.bss`](itemgroupingstaticstatus_bss.md) a list
of effects, each with its colour, its name and the Primordial Pigment item
that applies it (Turquoise Primordial Pigment - Sovereign). The dye window
(`panel_widget_dye_all_1.luac`) walks the effect indexes with
`ToClient_GetItemEffectInfoByIndex(effectIndex)`, draws each slot with
`info:getColor()`, names it with
`PAGetStringByStringHash(Defines.StringSheet_RESOURCE, info:getName())`
and counts the pigments with `ToClient_GetEquipItemEffectDyeItemCount`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                              | Bytes | Records            | Row bytes               |
| ------ | -------------- | --------------------------------- | ----- | ------------------ | ----------------------- |
| 4      | 3302 and later | `itemeffectgroupstaticstatus.bss` | 606   | 20 Effect, 4 Group | 24 to 30, 28 on average |
| 3      | 3186 to 3293   | `itemeffectgroupstaticstatus.bss` | 292   | 11 Effect, 4 Group | 20 to 26, 23 on average |
| 2      | 3169 to 3177   | `itemeffectgroupstaticstatus.bss` | 168   | 11 Effect, 4 Group | 12                      |
| 1      | 2503 to 3158   | `itemeffectgroupstaticstatus.bss` | 438   | 22 Effect, 2 Group | 19                      |

| Layout | File                              | Known         | Unknown       |
| ------ | --------------------------------- | ------------- | ------------- |
| 4      | `itemeffectgroupstaticstatus.bss` | 586 B (96.7%) | 20 B (3.3%)   |
| 3      | `itemeffectgroupstaticstatus.bss` | 281 B (96.2%) | 11 B (3.8%)   |
| 2      | `itemeffectgroupstaticstatus.bss` | 157 B (93.5%) | 11 B (6.5%)   |
| 1      | `itemeffectgroupstaticstatus.bss` | 262 B (59.8%) | 176 B (40.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 4 | `1ae4afef32ca`  |
| 3482   | Layout 4 | `1ae4afef32ca`  |
| 3474   | Layout 4 | `1ae4afef32ca`  |
| 3473   | Layout 4 | `1ae4afef32ca`  |
| 3464   | Layout 4 | `1ae4afef32ca`  |
| 3458   | Layout 4 | `1ae4afef32ca`  |
| 3454   | Layout 4 | `1ae4afef32ca`  |
| 3444   | Layout 4 | `1ae4afef32ca`  |
| 3435   | Layout 4 | `1ae4afef32ca`  |
| 3426   | Layout 4 | `1ae4afef32ca`  |
| 3418   | Layout 4 | `1ae4afef32ca`  |
| 3412   | Layout 4 | `1ae4afef32ca`  |
| 3402   | Layout 4 | `1ae4afef32ca`  |
| 3396   | Layout 4 | `1ae4afef32ca`  |
| 3387   | Layout 4 | `1ae4afef32ca`  |
| 3381   | Layout 4 | `1ae4afef32ca`  |
| 3373   | Layout 4 | `1ae4afef32ca`  |
| 3364   | Layout 4 | `1ae4afef32ca`  |
| 3356   | Layout 4 | `1ae4afef32ca`  |
| 3349   | Layout 4 | `1ae4afef32ca`  |
| 3342   | Layout 4 | `1ae4afef32ca`  |
| 3335   | Layout 4 | `1ae4afef32ca`  |
| 3326   | Layout 4 | `1ae4afef32ca`  |
| 3321   | Layout 4 | `1ae4afef32ca`  |
| 3314   | Layout 4 | `1ae4afef32ca`  |
| 3303   | Layout 4 | `1ae4afef32ca`  |
| 3302   | Layout 4 | `1ae4afef32ca`  |
| 3293   | Layout 3 | `1ae4afef32ca`  |
| 3283   | Layout 3 | `1ae4afef32ca`  |
| 3275   | Layout 3 | `1ae4afef32ca`  |
| 3267   | Layout 3 | `1ae4afef32ca`  |
| 3258   | Layout 3 | `1ae4afef32ca`  |
| 3251   | Layout 3 | `1ae4afef32ca`  |
| 3242   | Layout 3 | `1ae4afef32ca`  |
| 3235   | Layout 3 | `1ae4afef32ca`  |
| 3229   | Layout 3 | `1ae4afef32ca`  |
| 3212   | Layout 3 | `1ae4afef32ca`  |
| 3203   | Layout 3 | `1ae4afef32ca`  |
| 3193   | Layout 3 | `1ae4afef32ca`  |
| 3186   | Layout 3 | `1ae4afef32ca`  |
| 3177   | Layout 2 | `1ae4afef32ca`  |
| 3169   | Layout 2 | `1ae4afef32ca`  |
| 3158   | Layout 1 | `1ae4afef32ca`  |
| 3151   | Layout 1 | `1ae4afef32ca`  |
| 3144   | Layout 1 | `1ae4afef32ca`  |
| 3133   | Layout 1 | `1ae4afef32ca`  |
| 3125   | Layout 1 | `1ae4afef32ca`  |
| 3118   | Layout 1 | `1ae4afef32ca`  |
| 3111   | Layout 1 | `1ae4afef32ca`  |
| 3103   | Layout 1 | `1ae4afef32ca`  |
| 3095   | Layout 1 | `1ae4afef32ca`  |
| 3086   | Layout 1 | `1ae4afef32ca`  |
| 3072   | Layout 1 | `1ae4afef32ca`  |
| 3062   | Layout 1 | `1ae4afef32ca`  |
| 3052   | Layout 1 | `1ae4afef32ca`  |
| 3045   | Layout 1 | `1ae4afef32ca`  |
| 3037   | Layout 1 | `1ae4afef32ca`  |
| 3030   | Layout 1 | `1ae4afef32ca`  |
| 3021   | Layout 1 | `1ae4afef32ca`  |
| 3012   | Layout 1 | `1ae4afef32ca`  |
| 3002   | Layout 1 | `1ae4afef32ca`  |
| 2995   | Layout 1 | `1ae4afef32ca`  |
| 2987   | Layout 1 | `1ae4afef32ca`  |
| 2978   | Layout 1 | `1ae4afef32ca`  |
| 2970   | Layout 1 | `1ae4afef32ca`  |
| 2959   | Layout 1 | `1ae4afef32ca`  |
| 2951   | Layout 1 | `1ae4afef32ca`  |
| 2942   | Layout 1 | `1ae4afef32ca`  |
| 2935   | Layout 1 | `1ae4afef32ca`  |
| 2932   | Layout 1 | `1ae4afef32ca`  |
| 2923   | Layout 1 | `1ae4afef32ca`  |
| 2919   | Layout 1 | `1ae4afef32ca`  |
| 2907   | Layout 1 | `1ae4afef32ca`  |
| 2900   | Layout 1 | `1ae4afef32ca`  |
| 2891   | Layout 1 | `1ae4afef32ca`  |
| 2882   | Layout 1 | `1ae4afef32ca`  |
| 2872   | Layout 1 | `1ae4afef32ca`  |
| 2863   | Layout 1 | `1ae4afef32ca`  |
| 2855   | Layout 1 | `1ae4afef32ca`  |
| 2849   | Layout 1 | `1ae4afef32ca`  |
| 2844   | Layout 1 | `1ae4afef32ca`  |
| 2834   | Layout 1 | `1ae4afef32ca`  |
| 2825   | Layout 1 | `1ae4afef32ca`  |
| 2819   | Layout 1 | `1ae4afef32ca`  |
| 2811   | Layout 1 | `1ae4afef32ca`  |
| 2803   | Layout 1 | `1ae4afef32ca`  |
| 2794   | Layout 1 | `1ae4afef32ca`  |
| 2783   | Layout 1 | `1ae4afef32ca`  |
| 2774   | Layout 1 | `1ae4afef32ca`  |
| 2765   | Layout 1 | `1ae4afef32ca`  |
| 2756   | Layout 1 | `1ae4afef32ca`  |
| 2750   | Layout 1 | `1ae4afef32ca`  |
| 2743   | Layout 1 | `1ae4afef32ca`  |
| 2736   | Layout 1 | `1ae4afef32ca`  |
| 2726   | Layout 1 | `1ae4afef32ca`  |
| 2717   | Layout 1 | `1ae4afef32ca`  |
| 2709   | Layout 1 | `1ae4afef32ca`  |
| 2703   | Layout 1 | `1ae4afef32ca`  |
| 2695   | Layout 1 | `1ae4afef32ca`  |
| 2684   | Layout 1 | `1ae4afef32ca`  |
| 2672   | Layout 1 | `1ae4afef32ca`  |
| 2665   | Layout 1 | `1ae4afef32ca`  |
| 2657   | Layout 1 | `1ae4afef32ca`  |
| 2649   | Layout 1 | `1ae4afef32ca`  |
| 2644   | Layout 1 | `1ae4afef32ca`  |
| 2637   | Layout 1 | `1ae4afef32ca`  |
| 2629   | Layout 1 | `1ae4afef32ca`  |
| 2619   | Layout 1 | `1ae4afef32ca`  |
| 2612   | Layout 1 | `1ae4afef32ca`  |
| 2606   | Layout 1 | `1ae4afef32ca`  |
| 2602   | Layout 1 | `1ae4afef32ca`  |
| 2601   | Layout 1 | `1ae4afef32ca`  |
| 2592   | Layout 1 | `1ae4afef32ca`  |
| 2583   | Layout 1 | `1ae4afef32ca`  |
| 2575   | Layout 1 | `1ae4afef32ca`  |
| 2567   | Layout 1 | `1ae4afef32ca`  |
| 2560   | Layout 1 | `1ae4afef32ca`  |
| 2553   | Layout 1 | `1ae4afef32ca`  |
| 2545   | Layout 1 | `1ae4afef32ca`  |
| 2538   | Layout 1 | `1ae4afef32ca`  |
| 2529   | Layout 1 | `1ae4afef32ca`  |
| 2519   | Layout 1 | `1ae4afef32ca`  |
| 2513   | Layout 1 | `1ae4afef32ca`  |
| 2510   | Layout 1 | `1ae4afef32ca`  |
| 2507   | Layout 1 | `1ae4afef32ca`  |
| 2503   | Layout 1 | `1ae4afef32ca`  |
| 2498   | No file  | `1ae4afef32ca`  |
| 2492   | No file  | `1ae4afef32ca`  |
| 2487   | No file  | `1ae4afef32ca`  |
| 2480   | No file  | `1ae4afef32ca`  |
| 2474   | No file  | `1ae4afef32ca`  |
| 2468   | No file  | `1ae4afef32ca`  |
| 2460   | No file  | `1ae4afef32ca`  |
| 2453   | No file  | `1ae4afef32ca`  |
| 2444   | No file  | `1ae4afef32ca`  |
| 2438   | No file  | `1ae4afef32ca`  |
| 2434   | No file  | `1ae4afef32ca`  |
| 2429   | No file  | `1ae4afef32ca`  |
| 2421   | No file  | `1ae4afef32ca`  |
| 2414   | No file  | `1ae4afef32ca`  |
| 2407   | No file  | `1ae4afef32ca`  |
| 2401   | No file  | `1ae4afef32ca`  |
| 2397   | No file  | `1ae4afef32ca`  |
| 2393   | No file  | `1ae4afef32ca`  |
| 2384   | No file  | `1ae4afef32ca`  |
| 2378   | No file  | `1ae4afef32ca`  |
| 2372   | No file  | `1ae4afef32ca`  |
| 2358   | No file  | `1ae4afef32ca`  |
| 2352   | No file  | `1ae4afef32ca`  |
| 2347   | No file  | `1ae4afef32ca`  |
| 2343   | No file  | `1ae4afef32ca`  |
| 2335   | No file  | `1ae4afef32ca`  |
| 2327   | No file  | `1ae4afef32ca`  |
| 2324   | No file  | `1ae4afef32ca`  |
| 2319   | No file  | `1ae4afef32ca`  |
| 2313   | No file  | `1ae4afef32ca`  |
| 2308   | No file  | `1ae4afef32ca`  |
| 2302   | No file  | `1ae4afef32ca`  |
| 2295   | No file  | `1ae4afef32ca`  |
| 2290   | No file  | `1ae4afef32ca`  |
| 2284   | No file  | `1ae4afef32ca`  |
| 2276   | No file  | `1ae4afef32ca`  |
| 2269   | No file  | `1ae4afef32ca`  |
| 2259   | No file  | `1ae4afef32ca`  |
| 2250   | No file  | `1ae4afef32ca`  |
| 2243   | No file  | `1ae4afef32ca`  |
| 2235   | No file  | `1ae4afef32ca`  |
| 2229   | No file  | `1ae4afef32ca`  |
| 2224   | No file  | `1ae4afef32ca`  |
| 2218   | No file  | `1ae4afef32ca`  |
| 2215   | No file  | `1ae4afef32ca`  |
| 2207   | No file  | `1ae4afef32ca`  |
| 2203   | No file  | `1ae4afef32ca`  |
| 2196   | No file  | `1ae4afef32ca`  |
| 2192   | No file  | `1ae4afef32ca`  |
| 2189   | No file  | `1ae4afef32ca`  |
| 2183   | No file  | `1ae4afef32ca`  |
| 2179   | No file  | `1ae4afef32ca`  |
| 2171   | No file  | `1ae4afef32ca`  |
| 2163   | No file  | `1ae4afef32ca`  |
| 2156   | No file  | `1ae4afef32ca`  |
| 2151   | No file  | `1ae4afef32ca`  |
| 2147   | No file  | `1ae4afef32ca`  |
| 2142   | No file  | `1ae4afef32ca`  |
| 2138   | No file  | `1ae4afef32ca`  |
| 2134   | No file  | `1ae4afef32ca`  |
| 2130   | No file  | `1ae4afef32ca`  |
| 2122   | No file  | `1ae4afef32ca`  |
| 2107   | No file  | `1ae4afef32ca`  |
| 2098   | No file  | `1ae4afef32ca`  |
| 2089   | No file  | `1ae4afef32ca`  |
| 2081   | No file  | `1ae4afef32ca`  |
| 2073   | No file  | `1ae4afef32ca`  |
| 2067   | No file  | `1ae4afef32ca`  |
| 2063   | No file  | `1ae4afef32ca`  |
| 2059   | No file  | `1ae4afef32ca`  |
| 2052   | No file  | `1ae4afef32ca`  |
| 2044   | No file  | `1ae4afef32ca`  |
| 2039   | No file  | `1ae4afef32ca`  |
| 2032   | No file  | `1ae4afef32ca`  |
| 2025   | No file  | `1ae4afef32ca`  |
| 2011   | No file  | `1ae4afef32ca`  |
| 2005   | No file  | `1ae4afef32ca`  |
| 2000   | No file  | `1ae4afef32ca`  |
| 1996   | No file  | `1ae4afef32ca`  |
| 1991   | No file  | `1ae4afef32ca`  |
| 1985   | No file  | `1ae4afef32ca`  |
| 1980   | No file  | `1ae4afef32ca`  |
| 1969   | No file  | `1ae4afef32ca`  |
| 1964   | No file  | `1ae4afef32ca`  |
| 1958   | No file  | `1ae4afef32ca`  |
| 1950   | No file  | `1ae4afef32ca`  |
| 1945   | No file  | `1ae4afef32ca`  |
| 1937   | No file  | `1ae4afef32ca`  |
| 1933   | No file  | `1ae4afef32ca`  |
| 1927   | No file  | `1ae4afef32ca`  |
| 1921   | No file  | `1ae4afef32ca`  |
| 1914   | No file  | `1ae4afef32ca`  |
| 1908   | No file  | `1ae4afef32ca`  |
| 1897   | No file  | `1ae4afef32ca`  |
| 1892   | No file  | `1ae4afef32ca`  |
| 1886   | No file  | `1ae4afef32ca`  |
| 1881   | No file  | `1ae4afef32ca`  |
| 1871   | No file  | `1ae4afef32ca`  |
| 1866   | No file  | `1ae4afef32ca`  |
| 1862   | No file  | `1ae4afef32ca`  |
| 1854   | No file  | `1ae4afef32ca`  |
| 1846   | No file  | `1ae4afef32ca`  |
| 1838   | No file  | `1ae4afef32ca`  |
| 1832   | No file  | `1ae4afef32ca`  |
| 1826   | No file  | `1ae4afef32ca`  |
| 1822   | No file  | `1ae4afef32ca`  |
| 1818   | No file  | `1ae4afef32ca`  |
| 1804   | No file  | `1ae4afef32ca`  |
| 1794   | No file  | `1ae4afef32ca`  |
| 1790   | No file  | `1ae4afef32ca`  |
| 1784   | No file  | `1ae4afef32ca`  |
| 1774   | No file  | `1ae4afef32ca`  |
| 1771   | No file  | `1ae4afef32ca`  |
| 1762   | No file  | `1ae4afef32ca`  |
| 1759   | No file  | `1ae4afef32ca`  |
| 1754   | No file  | `1ae4afef32ca`  |
| 1749   | No file  | `1ae4afef32ca`  |
| 1743   | No file  | `1ae4afef32ca`  |
| 1737   | No file  | `1ae4afef32ca`  |
| 1731   | No file  | `1ae4afef32ca`  |
| 1725   | No file  | `1ae4afef32ca`  |
| 1717   | No file  | `1ae4afef32ca`  |
| 1710   | No file  | `1ae4afef32ca`  |
| 1704   | No file  | `1ae4afef32ca`  |
| 1698   | No file  | `1ae4afef32ca`  |
| 1690   | No file  | `1ae4afef32ca`  |
| 1685   | No file  | `1ae4afef32ca`  |
| 1680   | No file  | `1ae4afef32ca`  |
| 1674   | No file  | `1ae4afef32ca`  |
| 1668   | No file  | `1ae4afef32ca`  |
| 1659   | No file  | `1ae4afef32ca`  |
| 1649   | No file  | `1ae4afef32ca`  |
| 1642   | No file  | `1ae4afef32ca`  |
| 1636   | No file  | `1ae4afef32ca`  |
| 1628   | No file  | `1ae4afef32ca`  |
| 1622   | No file  | `1ae4afef32ca`  |
| 1614   | No file  | `1ae4afef32ca`  |
| 1608   | No file  | `1ae4afef32ca`  |
| 1602   | No file  | `1ae4afef32ca`  |
| 1598   | No file  | `1ae4afef32ca`  |
| 1594   | No file  | `1ae4afef32ca`  |
| 1590   | No file  | `1ae4afef32ca`  |
| 1587   | No file  | `1ae4afef32ca`  |
| 1584   | No file  | `1ae4afef32ca`  |
| 1579   | No file  | `1ae4afef32ca`  |
| 1572   | No file  | `1ae4afef32ca`  |
| 1565   | No file  | `1ae4afef32ca`  |
| 1559   | No file  | `1ae4afef32ca`  |
| 1554   | No file  | `1ae4afef32ca`  |
| 1547   | No file  | `1ae4afef32ca`  |
| 1537   | No file  | `1ae4afef32ca`  |
| 1529   | No file  | `1ae4afef32ca`  |
| 1524   | No file  | `1ae4afef32ca`  |
| 1519   | No file  | `1ae4afef32ca`  |
| 1509   | No file  | `1ae4afef32ca`  |
| 1506   | No file  | `1ae4afef32ca`  |
| 1504   | No file  | `1ae4afef32ca`  |
| 1500   | No file  | `1ae4afef32ca`  |
| 1493   | No file  | `1ae4afef32ca`  |
| 1489   | No file  | `1ae4afef32ca`  |
| 1485   | No file  | `1ae4afef32ca`  |
| 1481   | No file  | `1ae4afef32ca`  |
| 1474   | No file  | `1ae4afef32ca`  |
| 1466   | No file  | `1ae4afef32ca`  |
| 1462   | No file  | `1ae4afef32ca`  |
| 1459   | No file  | `1ae4afef32ca`  |
| 1453   | No file  | `1ae4afef32ca`  |
| 1450   | No file  | `1ae4afef32ca`  |
| 1445   | No file  | `1ae4afef32ca`  |
| 1439   | No file  | `1ae4afef32ca`  |
| 1433   | No file  | `1ae4afef32ca`  |
| 1430   | No file  | `1ae4afef32ca`  |
| 1426   | No file  | `1ae4afef32ca`  |
| 1421   | No file  | `1ae4afef32ca`  |
| 1417   | No file  | `1ae4afef32ca`  |
| 1416   | No file  | `1ae4afef32ca`  |
| 1409   | No file  | `1ae4afef32ca`  |
| 1405   | No file  | `1ae4afef32ca`  |
| 1401   | No file  | `1ae4afef32ca`  |
| 1396   | No file  | `1ae4afef32ca`  |
| 1391   | No file  | `1ae4afef32ca`  |
| 1390   | No file  | `1ae4afef32ca`  |
| 1386   | No file  | `1ae4afef32ca`  |
| 1381   | No file  | `1ae4afef32ca`  |
| 1379   | No file  | `1ae4afef32ca`  |
| 1372   | No file  | `1ae4afef32ca`  |
| 1366   | No file  | `1ae4afef32ca`  |
| 1364   | No file  | `1ae4afef32ca`  |
| 1363   | No file  | `1ae4afef32ca`  |
| 1360   | No file  | `1ae4afef32ca`  |
| 1358   | No file  | `1ae4afef32ca`  |
| 1355   | No file  | `1ae4afef32ca`  |
| 1351   | No file  | `1ae4afef32ca`  |
| 1348   | No file  | `1ae4afef32ca`  |
| 1346   | No file  | `1ae4afef32ca`  |
| 1341   | No file  | `1ae4afef32ca`  |
| 1340   | No file  | `1ae4afef32ca`  |
| 1338   | No file  | `1ae4afef32ca`  |
| 1335   | No file  | `1ae4afef32ca`  |
| 1333   | No file  | `1ae4afef32ca`  |
| 1329   | No file  | `1ae4afef32ca`  |
| 1327   | No file  | `1ae4afef32ca`  |
| 1324   | No file  | `1ae4afef32ca`  |
| 1321   | No file  | `1ae4afef32ca`  |
| 1319   | No file  | `1ae4afef32ca`  |
| 1318   | No file  | `1ae4afef32ca`  |
| 1316   | No file  | `1ae4afef32ca`  |
| 1313   | No file  | `1ae4afef32ca`  |
| 1311   | No file  | `1ae4afef32ca`  |
| 1309   | No file  | `1ae4afef32ca`  |
| 1304   | No file  | `1ae4afef32ca`  |
| 1292   | No file  | `1ae4afef32ca`  |
| 1286   | No file  | `1ae4afef32ca`  |
| 1280   | No file  | `1ae4afef32ca`  |
| 1276   | No file  | `1ae4afef32ca`  |
| 1267   | No file  | `1ae4afef32ca`  |
| 1261   | No file  | `1ae4afef32ca`  |
| 1256   | No file  | `1ae4afef32ca`  |
| 1250   | No file  | `1ae4afef32ca`  |
| 1246   | No file  | `1ae4afef32ca`  |
| 1239   | No file  | `1ae4afef32ca`  |
| 1230   | No file  | `1ae4afef32ca`  |
| 1226   | No file  | `1ae4afef32ca`  |
| 1220   | No file  | `1ae4afef32ca`  |
| 1217   | No file  | `1ae4afef32ca`  |
| 1211   | No file  | `1ae4afef32ca`  |
| 1210   | No file  | `1ae4afef32ca`  |
| 1208   | No file  | `1ae4afef32ca`  |
| 1203   | No file  | `1ae4afef32ca`  |
| 1197   | No file  | `1ae4afef32ca`  |
| 1194   | No file  | `1ae4afef32ca`  |
| 1192   | No file  | `1ae4afef32ca`  |
| 1187   | No file  | `1ae4afef32ca`  |
| 1183   | No file  | `1ae4afef32ca`  |
| 1177   | No file  | `1ae4afef32ca`  |
| 1173   | No file  | `1ae4afef32ca`  |
| 1167   | No file  | `1ae4afef32ca`  |
| 1164   | No file  | `1ae4afef32ca`  |
| 1156   | No file  | `1ae4afef32ca`  |
| 1149   | No file  | `1ae4afef32ca`  |
| 1144   | No file  | `1ae4afef32ca`  |
| 1137   | No file  | `1ae4afef32ca`  |
| 1132   | No file  | `1ae4afef32ca`  |
| 1127   | No file  | `1ae4afef32ca`  |
| 1122   | No file  | `1ae4afef32ca`  |
| 1118   | No file  | `1ae4afef32ca`  |
| 1114   | No file  | `1ae4afef32ca`  |
| 1109   | No file  | `1ae4afef32ca`  |
| 1102   | No file  | `1ae4afef32ca`  |
| 1096   | No file  | `1ae4afef32ca`  |
| 1088   | No file  | `1ae4afef32ca`  |
| 1081   | No file  | `1ae4afef32ca`  |
| 1076   | No file  | `1ae4afef32ca`  |
| 1069   | No file  | `1ae4afef32ca`  |
| 1064   | No file  | `1ae4afef32ca`  |
| 1058   | No file  | `1ae4afef32ca`  |
| 1051   | No file  | `1ae4afef32ca`  |
| 1044   | No file  | `1ae4afef32ca`  |
| 1036   | No file  | `1ae4afef32ca`  |
| 1026   | No file  | `1ae4afef32ca`  |
| 1016   | No file  | `1ae4afef32ca`  |
| 1009   | No file  | `1ae4afef32ca`  |
| 1005   | No file  | `1ae4afef32ca`  |
| 1000   | No file  | `1ae4afef32ca`  |
| 998    | No file  | `1ae4afef32ca`  |
| 990    | No file  | `1ae4afef32ca`  |
| 979    | No file  | `1ae4afef32ca`  |
| 972    | No file  | `1ae4afef32ca`  |
| 963    | No file  | `1ae4afef32ca`  |
| 955    | No file  | `1ae4afef32ca`  |
| 946    | No file  | `1ae4afef32ca`  |
| 938    | No file  | `1ae4afef32ca`  |
| 927    | No file  | `1ae4afef32ca`  |
| 911    | No file  | `1ae4afef32ca`  |
| 904    | No file  | `1ae4afef32ca`  |
| 899    | No file  | `1ae4afef32ca`  |
| 894    | No file  | `1ae4afef32ca`  |
| 885    | No file  | `1ae4afef32ca`  |
| 879    | No file  | `1ae4afef32ca`  |
| 872    | No file  | `1ae4afef32ca`  |
| 864    | No file  | `1ae4afef32ca`  |
| 855    | No file  | `1ae4afef32ca`  |
| 853    | No file  | `1ae4afef32ca`  |
| 845    | No file  | `1ae4afef32ca`  |
| 837    | No file  | `1ae4afef32ca`  |
| 829    | No file  | `1ae4afef32ca`  |
| 822    | No file  | `1ae4afef32ca`  |
| 814    | No file  | `1ae4afef32ca`  |
| 805    | No file  | `1ae4afef32ca`  |
| 794    | No file  | `1ae4afef32ca`  |
| 787    | No file  | `1ae4afef32ca`  |
| 780    | No file  | `1ae4afef32ca`  |
| 771    | No file  | `1ae4afef32ca`  |
| 760    | No file  | `1ae4afef32ca`  |
| 748    | No file  | `1ae4afef32ca`  |
| 741    | No file  | `1ae4afef32ca`  |
| 736    | No file  | `1ae4afef32ca`  |
| 731    | No file  | `1ae4afef32ca`  |
| 723    | No file  | `1ae4afef32ca`  |
| 711    | No file  | `1ae4afef32ca`  |
| 707    | No file  | `1ae4afef32ca`  |
| 697    | No file  | `1ae4afef32ca`  |
| 689    | No file  | `1ae4afef32ca`  |
| 683    | No file  | `1ae4afef32ca`  |
| 678    | No file  | `1ae4afef32ca`  |
| 670    | No file  | `1ae4afef32ca`  |
| 661    | No file  | `1ae4afef32ca`  |
| 656    | No file  | `1ae4afef32ca`  |
| 652    | No file  | `1ae4afef32ca`  |
| 643    | No file  | `1ae4afef32ca`  |
| 637    | No file  | `1ae4afef32ca`  |
| 630    | No file  | `1ae4afef32ca`  |
| 627    | No file  | `1ae4afef32ca`  |
| 621    | No file  | `1ae4afef32ca`  |
| 617    | No file  | `1ae4afef32ca`  |
| 615    | No file  | `1ae4afef32ca`  |
| 606    | No file  | `1ae4afef32ca`  |
| 599    | No file  | `1ae4afef32ca`  |
| 592    | No file  | `1ae4afef32ca`  |
| 586    | No file  | `1ae4afef32ca`  |
| 577    | No file  | `1ae4afef32ca`  |
| 569    | No file  | `1ae4afef32ca`  |
| 561    | No file  | `1ae4afef32ca`  |
| 554    | No file  | `1ae4afef32ca`  |
| 542    | No file  | `1ae4afef32ca`  |
| 532    | No file  | `1ae4afef32ca`  |
| 531    | No file  | `1ae4afef32ca`  |
| 526    | No file  | `1ae4afef32ca`  |
| 521    | No file  | `1ae4afef32ca`  |
| 517    | No file  | `1ae4afef32ca`  |
| 510    | No file  | `1ae4afef32ca`  |
| 508    | No file  | `1ae4afef32ca`  |
| 504    | No file  | `1ae4afef32ca`  |
| 497    | No file  | `1ae4afef32ca`  |
| 491    | No file  | `1ae4afef32ca`  |
| 485    | No file  | `1ae4afef32ca`  |
| 478    | No file  | `1ae4afef32ca`  |
| 472    | No file  | `1ae4afef32ca`  |
| 466    | No file  | `1ae4afef32ca`  |
| 457    | No file  | `1ae4afef32ca`  |
| 452    | No file  | `1ae4afef32ca`  |
| 449    | No file  | `1ae4afef32ca`  |
| 435    | No file  | `1ae4afef32ca`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                            |
| --------------------- | -------- | ------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Pigment item names (LOC type 0) and effect names (LOC type 37, `RESOURCE` sheet) |

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset  | Type               | Field       | Notes                                            |
| ------- | ------------------ | ----------- | ------------------------------------------------ |
| `+0x00` | u32                | group_count | Number of groups; no PABR magic, no string table |
| `+0x04` | Group[group_count] | groups      | See Group; from the highest type down            |

### Group (variable: 8 bytes + effects)

| Offset  | Type                 | Field           | Notes                                                                 |
| ------- | -------------------- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u32                  | item_group_type | An `itemgroupingstaticstatus.bss` group type: `8` to `11` on client 3482 |
| `+0x04` | u32                  | effect_count    | Number of `effects`; `5` in every group of client 3482                 |
| `+0x08` | Effect[effect_count] | effects         | See Effect                                                            |

### Effect (variable: 24 bytes + colour text)

| Offset         | Type     | Field            | Notes                                                                                   |
| -------------- | -------- | ---------------- | --------------------------------------------------------------------------------------- |
| `+0x00`        | u32      | effect_index     | `0` to `4` in order; the `effectIndex` the Lua passes                                    |
| `+0x04`        | u8       | unknown_04       | `1` on every effect of client 3482                                                       |
| `+0x05`        | str8     | color            | Colour as `RRGGBB` hex text (`1D3F48` for Turquoise); empty on 5 of the 20 effects        |
| `color+0x00`   | bytes[3] | color_rgb        | Colour as red, green and blue bytes; `00 00 00` after a colour text (see Notes)          |
| `color+0x03`   | u32      | name             | String hash of the effect name in the `RESOURCE` sheet (LOC type 37, `str_id2` 2)         |
| `color+0x07`   | u32      | dye_item_id      | The pigment item that applies the effect; `0` for effect `0` (`Default`)                 |

## Layout 3

The effect has no `dye_item_id`. Only the Effect differs from Layout 4.

### Effect (variable: 20 bytes + colour text)

| Offset       | Type     | Field        | Notes |
| ------------ | -------- | ------------ | ----- |
| `+0x00`      | u32      | effect_index |       |
| `+0x04`      | u8       | unknown_04   |       |
| `+0x05`      | str8     | color        |       |
| `color+0x00` | bytes[3] | color_rgb    |       |
| `color+0x03` | u32      | name         |       |

## Layout 2

The effect has no colour text and no `dye_item_id`. Only the Effect differs
from Layout 3.

### Effect (12 bytes)

| Offset  | Type     | Field        | Notes |
| ------- | -------- | ------------ | ----- |
| `+0x00` | u32      | effect_index |       |
| `+0x04` | u8       | unknown_04   |       |
| `+0x05` | bytes[3] | color_rgb    |       |
| `+0x08` | u32      | name         |       |

## Layout 1

The effect has no colour text and no `dye_item_id`; eight bytes after
`effect_index` take the place of `unknown_04`. Only the Effect differs from
Layout 2.

### Effect (19 bytes)

| Offset  | Type     | Field          | Notes                                                              |
| ------- | -------- | -------------- | ------------------------------------------------------------------ |
| `+0x00` | u32      | effect_index   | `0` to `10` on client 2519                                         |
| `+0x04` | u64      | unknown_old_04 | `0` on effect `0`, `750` on every other effect of client 2519      |
| `+0x0C` | bytes[3] | color_rgb      | The only colour of the effect (`00 00 ff` for `Blue`)              |
| `+0x0F` | u32      | name           |                                                                    |

## Effects

The effects of client 3482. Groups 8, 9 and 10 (the Sovereign main,
sub-weapon and awakening groups) list the same five; group 11 (Edana armor)
has its own.

| Group     | Index | Name (LOC)  | color    | color_rgb        | dye_item_id                                      |
| --------- | ----- | ----------- | -------- | ---------------- | ------------------------------------------------ |
| 8, 9, 10  | 0     | Default     |          | `ff ff 00`       | `0`                                              |
| 8, 9, 10  | 1     | Red         | `651414` | `00 00 00`       | 767293 Crimson Primordial Pigment - Sovereign    |
| 8, 9, 10  | 2     | Violet      | `31183C` | `00 00 00`       | 767294 Violet Primordial Pigment - Sovereign     |
| 8, 9, 10  | 3     | Turquoise   | `1D3F48` | `00 00 00`       | 767341 Turquoise Primordial Pigment - Sovereign  |
| 8, 9, 10  | 4     | White       | `9A9A9A` | `00 00 00`       | 767343 White Primordial Pigment - Sovereign      |
| 11        | 0     | Default     |          | `ff 00 00`       | `0`                                              |
| 11        | 1     | Violet      |          | `80 00 80`       | 767296 Violet Primordial Pigment - Edana         |
| 11        | 2     | Turquoise   | `1D3F48` | `00 00 00`       | 767342 Turquoise Primordial Pigment - Edana      |
| 11        | 3     | White       | `9A9A9A` | `00 00 00`       | 767344 White Primordial Pigment - Edana          |
| 11        | 4     | Yellow      | `D5952A` | `00 00 00`       | 767353 Sunset Primordial Pigment - Edana         |

## Notes

- `color_rgb` is the colour of the effect in red, green and blue: on client
  2519 (Layout 1) the eleven effects of a group are `Black (Basic)`
  `00 00 00`, `Yellow` `ff ff 00`, `Turquoise` `00 ff ff`, `Blue`
  `00 00 ff`, `Violet` `80 00 80` and `White` `ff ff ff` among others, and
  there is no colour text. From Layout 3 an effect with a colour text has
  `00 00 00` here; the ones without text (`Default`, the Edana `Violet`)
  keep their colour in these bytes. The handler shows the text, else these
  bytes.
- Client 2519 has two groups, `1` and `0`, with the same eleven effects;
  the group keys `8` to `11` appear with Layout 2.
- An effect name is the same hash in every group: both Violet effects store
  `1080916977`, which LOC type 37 (`str_id2` 2) names `Violet`. All six
  hashes have a LOC row on client 3482.
- The file is not in the client 1784 PAZ.
- The handler (`_bss/itemeffectgroupstaticstatus/`) shows one row per
  effect: the group, the index, the name, the colour and the pigment item.

## Open Questions

### What `unknown_04` and `unknown_old_04` Hold

The u8 after `effect_index` is `1` on every effect of client 3482. The u64
it replaces in Layout 1 is `0` on the first effect of a group and `750` on
the others; a price or a dye amount would fit, but no Lua getter reads it.
