# `manufactureitemnaminginfo.bss` Format

## Purpose

The items that get a player's name stamped on them through processing
(manufacture). On client 3474 the list holds four Kamasylvia spirit
essences: Ornette's Spirit Essence (`40747`), Ancient Ornette's Spirit
Essence (`40748`), Odore's Spirit Essence (`40750`) and Ancient Odore's
Spirit Essence (`40751`).

For items other than equipment above +15 and enhanced accessories (those
have their own branch), the item tooltip (`panel_tooltip_item`) shows the stamped name when
`itemSSW:isNamingAbleItem()` is true and the item is not a cash item. The
line depends on the item type:

| Item type | Tooltip string key               | English text (LOC type 37, client 3474)                                          |
| --------- | -------------------------------- | -------------------------------------------------------------------------------- |
| Equip     | `LUA_TOOLTIP_ITEM_MAXENCHANTER`  | Equipment created by a great adventurer. Creator: `{name}`                       |
| Skill     | `LUA_TOOLTIP_RESTOREITEM_NAMING` | "A relic of the Kamasylve restored by a Great Adventurer." Restored by: `{name}` |
| Mapae     | `LUA_TOOLTIP_VEHICLE_NAMING`     | Built by: `{name}`                                                               |

The spirit essences are reusable items ("This item will not disappear after
being used"), which matches the Skill line.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                            | Bytes | Records        | Row bytes |
| ------ | -------------- | ------------------------------- | ----- | -------------- | --------- |
| 1      | 1698 and later | `manufactureitemnaminginfo.bss` | 36    | 1 String Table | 4         |

| Layout | File                            | Known         | Unknown    |
| ------ | ------------------------------- | ------------- | ---------- |
| 1      | `manufactureitemnaminginfo.bss` | 36 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e13a0b80297b`  |
| 3482   | Layout 1 | `e13a0b80297b`  |
| 3474   | Layout 1 | `e13a0b80297b`  |
| 3473   | Layout 1 | `e13a0b80297b`  |
| 3464   | Layout 1 | `e13a0b80297b`  |
| 3458   | Layout 1 | `e13a0b80297b`  |
| 3454   | Layout 1 | `e13a0b80297b`  |
| 3444   | Layout 1 | `e13a0b80297b`  |
| 3435   | Layout 1 | `e13a0b80297b`  |
| 3426   | Layout 1 | `e13a0b80297b`  |
| 3418   | Layout 1 | `e13a0b80297b`  |
| 3412   | Layout 1 | `e13a0b80297b`  |
| 3402   | Layout 1 | `e13a0b80297b`  |
| 3396   | Layout 1 | `e13a0b80297b`  |
| 3387   | Layout 1 | `e13a0b80297b`  |
| 3381   | Layout 1 | `e13a0b80297b`  |
| 3373   | Layout 1 | `e13a0b80297b`  |
| 3364   | Layout 1 | `e13a0b80297b`  |
| 3356   | Layout 1 | `e13a0b80297b`  |
| 3349   | Layout 1 | `e13a0b80297b`  |
| 3342   | Layout 1 | `e13a0b80297b`  |
| 3335   | Layout 1 | `e13a0b80297b`  |
| 3326   | Layout 1 | `e13a0b80297b`  |
| 3321   | Layout 1 | `e13a0b80297b`  |
| 3314   | Layout 1 | `e13a0b80297b`  |
| 3303   | Layout 1 | `e13a0b80297b`  |
| 3302   | Layout 1 | `e13a0b80297b`  |
| 3293   | Layout 1 | `e13a0b80297b`  |
| 3283   | Layout 1 | `e13a0b80297b`  |
| 3275   | Layout 1 | `e13a0b80297b`  |
| 3267   | Layout 1 | `e13a0b80297b`  |
| 3258   | Layout 1 | `e13a0b80297b`  |
| 3251   | Layout 1 | `e13a0b80297b`  |
| 3242   | Layout 1 | `e13a0b80297b`  |
| 3235   | Layout 1 | `e13a0b80297b`  |
| 3229   | Layout 1 | `e13a0b80297b`  |
| 3212   | Layout 1 | `e13a0b80297b`  |
| 3203   | Layout 1 | `e13a0b80297b`  |
| 3193   | Layout 1 | `e13a0b80297b`  |
| 3186   | Layout 1 | `e13a0b80297b`  |
| 3177   | Layout 1 | `e13a0b80297b`  |
| 3169   | Layout 1 | `e13a0b80297b`  |
| 3158   | Layout 1 | `e13a0b80297b`  |
| 3151   | Layout 1 | `e13a0b80297b`  |
| 3144   | Layout 1 | `e13a0b80297b`  |
| 3133   | Layout 1 | `e13a0b80297b`  |
| 3125   | Layout 1 | `e13a0b80297b`  |
| 3118   | Layout 1 | `e13a0b80297b`  |
| 3111   | Layout 1 | `e13a0b80297b`  |
| 3103   | Layout 1 | `e13a0b80297b`  |
| 3095   | Layout 1 | `e13a0b80297b`  |
| 3086   | Layout 1 | `e13a0b80297b`  |
| 3072   | Layout 1 | `e13a0b80297b`  |
| 3062   | Layout 1 | `e13a0b80297b`  |
| 3052   | Layout 1 | `e13a0b80297b`  |
| 3045   | Layout 1 | `e13a0b80297b`  |
| 3037   | Layout 1 | `e13a0b80297b`  |
| 3030   | Layout 1 | `e13a0b80297b`  |
| 3021   | Layout 1 | `e13a0b80297b`  |
| 3012   | Layout 1 | `e13a0b80297b`  |
| 3002   | Layout 1 | `e13a0b80297b`  |
| 2995   | Layout 1 | `e13a0b80297b`  |
| 2987   | Layout 1 | `e13a0b80297b`  |
| 2978   | Layout 1 | `e13a0b80297b`  |
| 2970   | Layout 1 | `e13a0b80297b`  |
| 2959   | Layout 1 | `e13a0b80297b`  |
| 2951   | Layout 1 | `e13a0b80297b`  |
| 2942   | Layout 1 | `e13a0b80297b`  |
| 2935   | Layout 1 | `e13a0b80297b`  |
| 2932   | Layout 1 | `e13a0b80297b`  |
| 2923   | Layout 1 | `e13a0b80297b`  |
| 2919   | Layout 1 | `e13a0b80297b`  |
| 2907   | Layout 1 | `e13a0b80297b`  |
| 2900   | Layout 1 | `e13a0b80297b`  |
| 2891   | Layout 1 | `e13a0b80297b`  |
| 2882   | Layout 1 | `e13a0b80297b`  |
| 2872   | Layout 1 | `e13a0b80297b`  |
| 2863   | Layout 1 | `e13a0b80297b`  |
| 2855   | Layout 1 | `e13a0b80297b`  |
| 2849   | Layout 1 | `e13a0b80297b`  |
| 2844   | Layout 1 | `e13a0b80297b`  |
| 2834   | Layout 1 | `e13a0b80297b`  |
| 2825   | Layout 1 | `e13a0b80297b`  |
| 2819   | Layout 1 | `e13a0b80297b`  |
| 2811   | Layout 1 | `e13a0b80297b`  |
| 2803   | Layout 1 | `e13a0b80297b`  |
| 2794   | Layout 1 | `e13a0b80297b`  |
| 2783   | Layout 1 | `e13a0b80297b`  |
| 2774   | Layout 1 | `e13a0b80297b`  |
| 2765   | Layout 1 | `e13a0b80297b`  |
| 2756   | Layout 1 | `e13a0b80297b`  |
| 2750   | Layout 1 | `e13a0b80297b`  |
| 2743   | Layout 1 | `e13a0b80297b`  |
| 2736   | Layout 1 | `e13a0b80297b`  |
| 2726   | Layout 1 | `e13a0b80297b`  |
| 2717   | Layout 1 | `e13a0b80297b`  |
| 2709   | Layout 1 | `e13a0b80297b`  |
| 2703   | Layout 1 | `e13a0b80297b`  |
| 2695   | Layout 1 | `e13a0b80297b`  |
| 2684   | Layout 1 | `e13a0b80297b`  |
| 2672   | Layout 1 | `e13a0b80297b`  |
| 2665   | Layout 1 | `e13a0b80297b`  |
| 2657   | Layout 1 | `e13a0b80297b`  |
| 2649   | Layout 1 | `e13a0b80297b`  |
| 2644   | Layout 1 | `e13a0b80297b`  |
| 2637   | Layout 1 | `e13a0b80297b`  |
| 2629   | Layout 1 | `e13a0b80297b`  |
| 2619   | Layout 1 | `e13a0b80297b`  |
| 2612   | Layout 1 | `e13a0b80297b`  |
| 2606   | Layout 1 | `e13a0b80297b`  |
| 2602   | Layout 1 | `e13a0b80297b`  |
| 2601   | Layout 1 | `e13a0b80297b`  |
| 2592   | Layout 1 | `e13a0b80297b`  |
| 2583   | Layout 1 | `e13a0b80297b`  |
| 2575   | Layout 1 | `e13a0b80297b`  |
| 2567   | Layout 1 | `e13a0b80297b`  |
| 2560   | Layout 1 | `e13a0b80297b`  |
| 2553   | Layout 1 | `e13a0b80297b`  |
| 2545   | Layout 1 | `e13a0b80297b`  |
| 2538   | Layout 1 | `e13a0b80297b`  |
| 2529   | Layout 1 | `e13a0b80297b`  |
| 2519   | Layout 1 | `e13a0b80297b`  |
| 2513   | Layout 1 | `e13a0b80297b`  |
| 2510   | Layout 1 | `e13a0b80297b`  |
| 2507   | Layout 1 | `e13a0b80297b`  |
| 2503   | Layout 1 | `e13a0b80297b`  |
| 2498   | Layout 1 | `e13a0b80297b`  |
| 2492   | Layout 1 | `e13a0b80297b`  |
| 2487   | Layout 1 | `e13a0b80297b`  |
| 2480   | Layout 1 | `e13a0b80297b`  |
| 2474   | Layout 1 | `e13a0b80297b`  |
| 2468   | Layout 1 | `e13a0b80297b`  |
| 2460   | Layout 1 | `e13a0b80297b`  |
| 2453   | Layout 1 | `e13a0b80297b`  |
| 2444   | Layout 1 | `e13a0b80297b`  |
| 2438   | Layout 1 | `e13a0b80297b`  |
| 2434   | Layout 1 | `e13a0b80297b`  |
| 2429   | Layout 1 | `e13a0b80297b`  |
| 2421   | Layout 1 | `e13a0b80297b`  |
| 2414   | Layout 1 | `e13a0b80297b`  |
| 2407   | Layout 1 | `e13a0b80297b`  |
| 2401   | Layout 1 | `e13a0b80297b`  |
| 2397   | Layout 1 | `e13a0b80297b`  |
| 2393   | Layout 1 | `e13a0b80297b`  |
| 2384   | Layout 1 | `e13a0b80297b`  |
| 2378   | Layout 1 | `e13a0b80297b`  |
| 2372   | Layout 1 | `e13a0b80297b`  |
| 2358   | Layout 1 | `e13a0b80297b`  |
| 2352   | Layout 1 | `e13a0b80297b`  |
| 2347   | Layout 1 | `e13a0b80297b`  |
| 2343   | Layout 1 | `e13a0b80297b`  |
| 2335   | Layout 1 | `e13a0b80297b`  |
| 2327   | Layout 1 | `e13a0b80297b`  |
| 2324   | Layout 1 | `e13a0b80297b`  |
| 2319   | Layout 1 | `e13a0b80297b`  |
| 2313   | Layout 1 | `e13a0b80297b`  |
| 2308   | Layout 1 | `e13a0b80297b`  |
| 2302   | Layout 1 | `e13a0b80297b`  |
| 2295   | Layout 1 | `e13a0b80297b`  |
| 2290   | Layout 1 | `e13a0b80297b`  |
| 2284   | Layout 1 | `e13a0b80297b`  |
| 2276   | Layout 1 | `e13a0b80297b`  |
| 2269   | Layout 1 | `e13a0b80297b`  |
| 2259   | Layout 1 | `e13a0b80297b`  |
| 2250   | Layout 1 | `e13a0b80297b`  |
| 2243   | Layout 1 | `e13a0b80297b`  |
| 2235   | Layout 1 | `e13a0b80297b`  |
| 2229   | Layout 1 | `e13a0b80297b`  |
| 2224   | Layout 1 | `e13a0b80297b`  |
| 2218   | Layout 1 | `e13a0b80297b`  |
| 2215   | Layout 1 | `e13a0b80297b`  |
| 2207   | Layout 1 | `e13a0b80297b`  |
| 2203   | Layout 1 | `e13a0b80297b`  |
| 2196   | Layout 1 | `e13a0b80297b`  |
| 2192   | Layout 1 | `e13a0b80297b`  |
| 2189   | Layout 1 | `e13a0b80297b`  |
| 2183   | Layout 1 | `e13a0b80297b`  |
| 2179   | Layout 1 | `e13a0b80297b`  |
| 2171   | Layout 1 | `e13a0b80297b`  |
| 2163   | Layout 1 | `e13a0b80297b`  |
| 2156   | Layout 1 | `e13a0b80297b`  |
| 2151   | Layout 1 | `e13a0b80297b`  |
| 2147   | Layout 1 | `e13a0b80297b`  |
| 2142   | Layout 1 | `e13a0b80297b`  |
| 2138   | Layout 1 | `e13a0b80297b`  |
| 2134   | Layout 1 | `e13a0b80297b`  |
| 2130   | Layout 1 | `e13a0b80297b`  |
| 2122   | Layout 1 | `e13a0b80297b`  |
| 2107   | Layout 1 | `e13a0b80297b`  |
| 2098   | Layout 1 | `e13a0b80297b`  |
| 2089   | Layout 1 | `e13a0b80297b`  |
| 2081   | Layout 1 | `e13a0b80297b`  |
| 2073   | Layout 1 | `e13a0b80297b`  |
| 2067   | Layout 1 | `e13a0b80297b`  |
| 2063   | Layout 1 | `e13a0b80297b`  |
| 2059   | Layout 1 | `e13a0b80297b`  |
| 2052   | Layout 1 | `e13a0b80297b`  |
| 2044   | Layout 1 | `e13a0b80297b`  |
| 2039   | Layout 1 | `e13a0b80297b`  |
| 2032   | Layout 1 | `e13a0b80297b`  |
| 2025   | Layout 1 | `e13a0b80297b`  |
| 2011   | Layout 1 | `e13a0b80297b`  |
| 2005   | Layout 1 | `e13a0b80297b`  |
| 2000   | Layout 1 | `e13a0b80297b`  |
| 1996   | Layout 1 | `e13a0b80297b`  |
| 1991   | Layout 1 | `e13a0b80297b`  |
| 1985   | Layout 1 | `e13a0b80297b`  |
| 1980   | Layout 1 | `e13a0b80297b`  |
| 1969   | Layout 1 | `e13a0b80297b`  |
| 1964   | Layout 1 | `e13a0b80297b`  |
| 1958   | Layout 1 | `e13a0b80297b`  |
| 1950   | Layout 1 | `e13a0b80297b`  |
| 1945   | Layout 1 | `e13a0b80297b`  |
| 1937   | Layout 1 | `e13a0b80297b`  |
| 1933   | Layout 1 | `e13a0b80297b`  |
| 1927   | Layout 1 | `e13a0b80297b`  |
| 1921   | Layout 1 | `e13a0b80297b`  |
| 1914   | Layout 1 | `e13a0b80297b`  |
| 1908   | Layout 1 | `e13a0b80297b`  |
| 1897   | Layout 1 | `e13a0b80297b`  |
| 1892   | Layout 1 | `e13a0b80297b`  |
| 1886   | Layout 1 | `e13a0b80297b`  |
| 1881   | Layout 1 | `e13a0b80297b`  |
| 1871   | Layout 1 | `e13a0b80297b`  |
| 1866   | Layout 1 | `e13a0b80297b`  |
| 1862   | Layout 1 | `e13a0b80297b`  |
| 1854   | Layout 1 | `e13a0b80297b`  |
| 1846   | Layout 1 | `e13a0b80297b`  |
| 1838   | Layout 1 | `e13a0b80297b`  |
| 1832   | Layout 1 | `e13a0b80297b`  |
| 1826   | Layout 1 | `e13a0b80297b`  |
| 1822   | Layout 1 | `e13a0b80297b`  |
| 1818   | Layout 1 | `e13a0b80297b`  |
| 1804   | Layout 1 | `e13a0b80297b`  |
| 1794   | Layout 1 | `e13a0b80297b`  |
| 1790   | Layout 1 | `e13a0b80297b`  |
| 1784   | Layout 1 | `e13a0b80297b`  |
| 1774   | Layout 1 | `e13a0b80297b`  |
| 1771   | Layout 1 | `e13a0b80297b`  |
| 1762   | Layout 1 | `e13a0b80297b`  |
| 1759   | Layout 1 | `e13a0b80297b`  |
| 1754   | Layout 1 | `e13a0b80297b`  |
| 1749   | Layout 1 | `e13a0b80297b`  |
| 1743   | Layout 1 | `e13a0b80297b`  |
| 1737   | Layout 1 | `e13a0b80297b`  |
| 1731   | Layout 1 | `e13a0b80297b`  |
| 1725   | Layout 1 | `e13a0b80297b`  |
| 1717   | Layout 1 | `e13a0b80297b`  |
| 1710   | Layout 1 | `e13a0b80297b`  |
| 1704   | Layout 1 | `e13a0b80297b`  |
| 1698   | Layout 1 | `e13a0b80297b`  |
| 1690   | No file  | `e13a0b80297b`  |
| 1685   | No file  | `e13a0b80297b`  |
| 1680   | No file  | `e13a0b80297b`  |
| 1674   | No file  | `e13a0b80297b`  |
| 1668   | No file  | `e13a0b80297b`  |
| 1659   | No file  | `e13a0b80297b`  |
| 1649   | No file  | `e13a0b80297b`  |
| 1642   | No file  | `e13a0b80297b`  |
| 1636   | No file  | `e13a0b80297b`  |
| 1628   | No file  | `e13a0b80297b`  |
| 1622   | No file  | `e13a0b80297b`  |
| 1614   | No file  | `e13a0b80297b`  |
| 1608   | No file  | `e13a0b80297b`  |
| 1602   | No file  | `e13a0b80297b`  |
| 1598   | No file  | `e13a0b80297b`  |
| 1594   | No file  | `e13a0b80297b`  |
| 1590   | No file  | `e13a0b80297b`  |
| 1587   | No file  | `e13a0b80297b`  |
| 1584   | No file  | `e13a0b80297b`  |
| 1579   | No file  | `e13a0b80297b`  |
| 1572   | No file  | `e13a0b80297b`  |
| 1565   | No file  | `e13a0b80297b`  |
| 1559   | No file  | `e13a0b80297b`  |
| 1554   | No file  | `e13a0b80297b`  |
| 1547   | No file  | `e13a0b80297b`  |
| 1537   | No file  | `e13a0b80297b`  |
| 1529   | No file  | `e13a0b80297b`  |
| 1524   | No file  | `e13a0b80297b`  |
| 1519   | No file  | `e13a0b80297b`  |
| 1509   | No file  | `e13a0b80297b`  |
| 1506   | No file  | `e13a0b80297b`  |
| 1504   | No file  | `e13a0b80297b`  |
| 1500   | No file  | `e13a0b80297b`  |
| 1493   | No file  | `e13a0b80297b`  |
| 1489   | No file  | `e13a0b80297b`  |
| 1485   | No file  | `e13a0b80297b`  |
| 1481   | No file  | `e13a0b80297b`  |
| 1474   | No file  | `e13a0b80297b`  |
| 1466   | No file  | `e13a0b80297b`  |
| 1462   | No file  | `e13a0b80297b`  |
| 1459   | No file  | `e13a0b80297b`  |
| 1453   | No file  | `e13a0b80297b`  |
| 1450   | No file  | `e13a0b80297b`  |
| 1445   | No file  | `e13a0b80297b`  |
| 1439   | No file  | `e13a0b80297b`  |
| 1433   | No file  | `e13a0b80297b`  |
| 1430   | No file  | `e13a0b80297b`  |
| 1426   | No file  | `e13a0b80297b`  |
| 1421   | No file  | `e13a0b80297b`  |
| 1417   | No file  | `e13a0b80297b`  |
| 1416   | No file  | `e13a0b80297b`  |
| 1409   | No file  | `e13a0b80297b`  |
| 1405   | No file  | `e13a0b80297b`  |
| 1401   | No file  | `e13a0b80297b`  |
| 1396   | No file  | `e13a0b80297b`  |
| 1391   | No file  | `e13a0b80297b`  |
| 1390   | No file  | `e13a0b80297b`  |
| 1386   | No file  | `e13a0b80297b`  |
| 1381   | No file  | `e13a0b80297b`  |
| 1379   | No file  | `e13a0b80297b`  |
| 1372   | No file  | `e13a0b80297b`  |
| 1366   | No file  | `e13a0b80297b`  |
| 1364   | No file  | `e13a0b80297b`  |
| 1363   | No file  | `e13a0b80297b`  |
| 1360   | No file  | `e13a0b80297b`  |
| 1358   | No file  | `e13a0b80297b`  |
| 1355   | No file  | `e13a0b80297b`  |
| 1351   | No file  | `e13a0b80297b`  |
| 1348   | No file  | `e13a0b80297b`  |
| 1346   | No file  | `e13a0b80297b`  |
| 1341   | No file  | `e13a0b80297b`  |
| 1340   | No file  | `e13a0b80297b`  |
| 1338   | No file  | `e13a0b80297b`  |
| 1335   | No file  | `e13a0b80297b`  |
| 1333   | No file  | `e13a0b80297b`  |
| 1329   | No file  | `e13a0b80297b`  |
| 1327   | No file  | `e13a0b80297b`  |
| 1324   | No file  | `e13a0b80297b`  |
| 1321   | No file  | `e13a0b80297b`  |
| 1319   | No file  | `e13a0b80297b`  |
| 1318   | No file  | `e13a0b80297b`  |
| 1316   | No file  | `e13a0b80297b`  |
| 1313   | No file  | `e13a0b80297b`  |
| 1311   | No file  | `e13a0b80297b`  |
| 1309   | No file  | `e13a0b80297b`  |
| 1304   | No file  | `e13a0b80297b`  |
| 1292   | No file  | `e13a0b80297b`  |
| 1286   | No file  | `e13a0b80297b`  |
| 1280   | No file  | `e13a0b80297b`  |
| 1276   | No file  | `e13a0b80297b`  |
| 1267   | No file  | `e13a0b80297b`  |
| 1261   | No file  | `e13a0b80297b`  |
| 1256   | No file  | `e13a0b80297b`  |
| 1250   | No file  | `e13a0b80297b`  |
| 1246   | No file  | `e13a0b80297b`  |
| 1239   | No file  | `e13a0b80297b`  |
| 1230   | No file  | `e13a0b80297b`  |
| 1226   | No file  | `e13a0b80297b`  |
| 1220   | No file  | `e13a0b80297b`  |
| 1217   | No file  | `e13a0b80297b`  |
| 1211   | No file  | `e13a0b80297b`  |
| 1210   | No file  | `e13a0b80297b`  |
| 1208   | No file  | `e13a0b80297b`  |
| 1203   | No file  | `e13a0b80297b`  |
| 1197   | No file  | `e13a0b80297b`  |
| 1194   | No file  | `e13a0b80297b`  |
| 1192   | No file  | `e13a0b80297b`  |
| 1187   | No file  | `e13a0b80297b`  |
| 1183   | No file  | `e13a0b80297b`  |
| 1177   | No file  | `e13a0b80297b`  |
| 1173   | No file  | `e13a0b80297b`  |
| 1167   | No file  | `e13a0b80297b`  |
| 1164   | No file  | `e13a0b80297b`  |
| 1156   | No file  | `e13a0b80297b`  |
| 1149   | No file  | `e13a0b80297b`  |
| 1144   | No file  | `e13a0b80297b`  |
| 1137   | No file  | `e13a0b80297b`  |
| 1132   | No file  | `e13a0b80297b`  |
| 1127   | No file  | `e13a0b80297b`  |
| 1122   | No file  | `e13a0b80297b`  |
| 1118   | No file  | `e13a0b80297b`  |
| 1114   | No file  | `e13a0b80297b`  |
| 1109   | No file  | `e13a0b80297b`  |
| 1102   | No file  | `e13a0b80297b`  |
| 1096   | No file  | `e13a0b80297b`  |
| 1088   | No file  | `e13a0b80297b`  |
| 1081   | No file  | `e13a0b80297b`  |
| 1076   | No file  | `e13a0b80297b`  |
| 1069   | No file  | `e13a0b80297b`  |
| 1064   | No file  | `e13a0b80297b`  |
| 1058   | No file  | `e13a0b80297b`  |
| 1051   | No file  | `e13a0b80297b`  |
| 1044   | No file  | `e13a0b80297b`  |
| 1036   | No file  | `e13a0b80297b`  |
| 1026   | No file  | `e13a0b80297b`  |
| 1016   | No file  | `e13a0b80297b`  |
| 1009   | No file  | `e13a0b80297b`  |
| 1005   | No file  | `e13a0b80297b`  |
| 1000   | No file  | `e13a0b80297b`  |
| 998    | No file  | `e13a0b80297b`  |
| 990    | No file  | `e13a0b80297b`  |
| 979    | No file  | `e13a0b80297b`  |
| 972    | No file  | `e13a0b80297b`  |
| 963    | No file  | `e13a0b80297b`  |
| 955    | No file  | `e13a0b80297b`  |
| 946    | No file  | `e13a0b80297b`  |
| 938    | No file  | `e13a0b80297b`  |
| 927    | No file  | `e13a0b80297b`  |
| 911    | No file  | `e13a0b80297b`  |
| 904    | No file  | `e13a0b80297b`  |
| 899    | No file  | `e13a0b80297b`  |
| 894    | No file  | `e13a0b80297b`  |
| 885    | No file  | `e13a0b80297b`  |
| 879    | No file  | `e13a0b80297b`  |
| 872    | No file  | `e13a0b80297b`  |
| 864    | No file  | `e13a0b80297b`  |
| 855    | No file  | `e13a0b80297b`  |
| 853    | No file  | `e13a0b80297b`  |
| 845    | No file  | `e13a0b80297b`  |
| 837    | No file  | `e13a0b80297b`  |
| 829    | No file  | `e13a0b80297b`  |
| 822    | No file  | `e13a0b80297b`  |
| 814    | No file  | `e13a0b80297b`  |
| 805    | No file  | `e13a0b80297b`  |
| 794    | No file  | `e13a0b80297b`  |
| 787    | No file  | `e13a0b80297b`  |
| 780    | No file  | `e13a0b80297b`  |
| 771    | No file  | `e13a0b80297b`  |
| 760    | No file  | `e13a0b80297b`  |
| 748    | No file  | `e13a0b80297b`  |
| 741    | No file  | `e13a0b80297b`  |
| 736    | No file  | `e13a0b80297b`  |
| 731    | No file  | `e13a0b80297b`  |
| 723    | No file  | `e13a0b80297b`  |
| 711    | No file  | `e13a0b80297b`  |
| 707    | No file  | `e13a0b80297b`  |
| 697    | No file  | `e13a0b80297b`  |
| 689    | No file  | `e13a0b80297b`  |
| 683    | No file  | `e13a0b80297b`  |
| 678    | No file  | `e13a0b80297b`  |
| 670    | No file  | `e13a0b80297b`  |
| 661    | No file  | `e13a0b80297b`  |
| 656    | No file  | `e13a0b80297b`  |
| 652    | No file  | `e13a0b80297b`  |
| 643    | No file  | `e13a0b80297b`  |
| 637    | No file  | `e13a0b80297b`  |
| 630    | No file  | `e13a0b80297b`  |
| 627    | No file  | `e13a0b80297b`  |
| 621    | No file  | `e13a0b80297b`  |
| 617    | No file  | `e13a0b80297b`  |
| 615    | No file  | `e13a0b80297b`  |
| 606    | No file  | `e13a0b80297b`  |
| 599    | No file  | `e13a0b80297b`  |
| 592    | No file  | `e13a0b80297b`  |
| 586    | No file  | `e13a0b80297b`  |
| 577    | No file  | `e13a0b80297b`  |
| 569    | No file  | `e13a0b80297b`  |
| 561    | No file  | `e13a0b80297b`  |
| 554    | No file  | `e13a0b80297b`  |
| 542    | No file  | `e13a0b80297b`  |
| 532    | No file  | `e13a0b80297b`  |
| 531    | No file  | `e13a0b80297b`  |
| 526    | No file  | `e13a0b80297b`  |
| 521    | No file  | `e13a0b80297b`  |
| 517    | No file  | `e13a0b80297b`  |
| 510    | No file  | `e13a0b80297b`  |
| 508    | No file  | `e13a0b80297b`  |
| 504    | No file  | `e13a0b80297b`  |
| 497    | No file  | `e13a0b80297b`  |
| 491    | No file  | `e13a0b80297b`  |
| 485    | No file  | `e13a0b80297b`  |
| 478    | No file  | `e13a0b80297b`  |
| 472    | No file  | `e13a0b80297b`  |
| 466    | No file  | `e13a0b80297b`  |
| 457    | No file  | `e13a0b80297b`  |
| 452    | No file  | `e13a0b80297b`  |
| 449    | No file  | `e13a0b80297b`  |
| 435    | No file  | `e13a0b80297b`  |

<!-- versions:end -->

## Companion Files

None. The handler names the items from LOC type 0.

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of u32 rows with an empty string table, read by
`u32_rows()` in `_common/pabr_strings.py`.

| Offset              | Type         | Field        | Notes                              |
| ------------------- | ------------ | ------------ | ---------------------------------- |
| `+0x00`             | char[4]      | magic        | `PABR`                             |
| `+0x04`             | u32          | count        | Number of items; `4` on client 3474 |
| `+0x08`             | u32[count]   | item_ids     | `count` item IDs (LOC type 0)      |
| `item_ids+0x00`     | String Table | string_table | Empty string table                 |
| `string_table+0x00` | u32          | table_start  | End of the rows (`8 + 4 * count`)  |
| `string_table+0x04` | u32          | zero         | `0`                                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Field Names

`item_ids` is the `ItemKey` column of the `ManufactureNaming_Table` sheet
of a private server's `DataSheets.bexcel` on client 1784: 4 of 4 keys match
client 3474, in the same order. The same sheet in the 1784
`datasheet_alchemydatatable.xlsm` has no developer comment beyond the
column name. The 1784 server binary loads the sheet in
`loadManufactureNamingInformation` into `ManufactureItemNamingStaticStatus`,
and keeps the stamped names per item in its database
(`uspRegistItemNaming`, `uspListItemNaming`).

## Notes

- All four items are materials of the Simple Alchemy recipes in
  [`manufacture.bss`](manufacture_bss.md) that combine one essence with a
  Fire Horn into the Central Market version. The other two essences those
  recipes take, Ornette's (`40712`) and Odore's (`40713`) Spirit Essence
  from the Dawnwish and Duskwish Petal quests, are not on the list.
- `panel_window_deletemaxenchantername` removes a stamped name through
  `ToClient_DeleteNamingItem`.

## Open Questions

### Which Recipe Stamps the Name

The list names the item, not the recipe. Recipes `19701` to `19704` of
`manufacture.bss` (Heating or Simple Alchemy of `40712` or `40713` with a
Dawnwish or Duskwish Petal) look like the ones that make the listed
essences, but their result groups are not in the client's
`itemmaingroup.bss`, and the 1784 sheets list no items for subgroups
`11311` to `11314`. Whether the name is stamped when a listed item is made,
or when it goes into the Fire Horn recipe, is open.

### Whether `isNamingAbleItem` Reads This List

The tooltip calls `itemSSW:isNamingAbleItem()` on the item's static status.
No client Lua reads this table directly, so the client may take the flag
from the item table instead.

## In-Game Checks

### Maker's Name on a Spirit Essence

Checks whether a listed item carries the name of the player who made it, and
at which step it is stamped. This answers both Open Questions.

Needs item (one of):

- [Ornette's Spirit Essence](https://bdocodex.com/us/item/40747/)
- [Odore's Spirit Essence](https://bdocodex.com/us/item/40750/)

1. Make one of the essences through processing.
2. Hover over it in the inventory and read the tooltip.
3. Expected: a line "A relic of the Kamasylve restored by a Great Adventurer.
   Restored by: {your family or character name}".
4. If the line is missing, use the essence in its Fire Horn Simple Alchemy
   recipe and read the tooltip of the result instead.
