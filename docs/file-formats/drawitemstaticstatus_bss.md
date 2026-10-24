# `drawitemstaticstatus.bss` Format

## Purpose

The prizes of the event ticket shop (`panel_event_ticketshop_all`, shown
while `_ContentsGroup_drawEvent` is on): one 26-byte row per prize with
the prize item and count, the coin item a draw costs and the item a lost
draw gives. Each event rewrites the file. On client 3483 the 8 rows are
the `[Event] Agent's Adventures` logs (Subjugation, Gathering, Fishing,
Barter, Training, Hunting, Cooking, Alchemy), drawn with `[Event] Agent's
Adventures` and with `[Event] Agent's Seal` as the lose item; the draw
prompt `LUA_EVENT_TICKETSHOP_POPUP_DESC` reads "There is a chance to
instantly obtain [Event] Agent's Seal".

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ------- | --------- |
| 1      | 1818 and later | 3483    | `drawitemstaticstatus.bss` | 228   | 8 Row   | 26        |

| Layout | File                       | Known         | Unknown      |
| ------ | -------------------------- | ------------- | ------------ |
| 1      | `drawitemstaticstatus.bss` | 148 B (64.9%) | 80 B (35.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `b4a3e852d75d`  |
| 3482   | Layout 1 | `b4a3e852d75d`  |
| 3474   | Layout 1 | `b4a3e852d75d`  |
| 3473   | Layout 1 | `b4a3e852d75d`  |
| 3464   | Layout 1 | `b4a3e852d75d`  |
| 3458   | Layout 1 | `b4a3e852d75d`  |
| 3454   | Layout 1 | `b4a3e852d75d`  |
| 3444   | Layout 1 | `b4a3e852d75d`  |
| 3435   | Layout 1 | `b4a3e852d75d`  |
| 3426   | Layout 1 | `b4a3e852d75d`  |
| 3418   | Layout 1 | `b4a3e852d75d`  |
| 3412   | Layout 1 | `b4a3e852d75d`  |
| 3402   | Layout 1 | `b4a3e852d75d`  |
| 3396   | Layout 1 | `b4a3e852d75d`  |
| 3387   | Layout 1 | `b4a3e852d75d`  |
| 3381   | Layout 1 | `b4a3e852d75d`  |
| 3373   | Layout 1 | `b4a3e852d75d`  |
| 3364   | Layout 1 | `b4a3e852d75d`  |
| 3356   | Layout 1 | `b4a3e852d75d`  |
| 3349   | Layout 1 | `b4a3e852d75d`  |
| 3342   | Layout 1 | `b4a3e852d75d`  |
| 3335   | Layout 1 | `b4a3e852d75d`  |
| 3326   | Layout 1 | `b4a3e852d75d`  |
| 3321   | Layout 1 | `b4a3e852d75d`  |
| 3314   | Layout 1 | `b4a3e852d75d`  |
| 3303   | Layout 1 | `b4a3e852d75d`  |
| 3302   | Layout 1 | `b4a3e852d75d`  |
| 3293   | Layout 1 | `b4a3e852d75d`  |
| 3283   | Layout 1 | `b4a3e852d75d`  |
| 3275   | Layout 1 | `b4a3e852d75d`  |
| 3267   | Layout 1 | `b4a3e852d75d`  |
| 3258   | Layout 1 | `b4a3e852d75d`  |
| 3251   | Layout 1 | `b4a3e852d75d`  |
| 3242   | Layout 1 | `b4a3e852d75d`  |
| 3235   | Layout 1 | `b4a3e852d75d`  |
| 3229   | Layout 1 | `b4a3e852d75d`  |
| 3212   | Layout 1 | `b4a3e852d75d`  |
| 3203   | Layout 1 | `b4a3e852d75d`  |
| 3193   | Layout 1 | `b4a3e852d75d`  |
| 3186   | Layout 1 | `b4a3e852d75d`  |
| 3177   | Layout 1 | `b4a3e852d75d`  |
| 3169   | Layout 1 | `b4a3e852d75d`  |
| 3158   | Layout 1 | `b4a3e852d75d`  |
| 3151   | Layout 1 | `b4a3e852d75d`  |
| 3144   | Layout 1 | `b4a3e852d75d`  |
| 3133   | Layout 1 | `b4a3e852d75d`  |
| 3125   | Layout 1 | `b4a3e852d75d`  |
| 3118   | Layout 1 | `b4a3e852d75d`  |
| 3111   | Layout 1 | `b4a3e852d75d`  |
| 3103   | Layout 1 | `b4a3e852d75d`  |
| 3095   | Layout 1 | `b4a3e852d75d`  |
| 3086   | Layout 1 | `b4a3e852d75d`  |
| 3072   | Layout 1 | `b4a3e852d75d`  |
| 3062   | Layout 1 | `b4a3e852d75d`  |
| 3052   | Layout 1 | `b4a3e852d75d`  |
| 3045   | Layout 1 | `b4a3e852d75d`  |
| 3037   | Layout 1 | `b4a3e852d75d`  |
| 3030   | Layout 1 | `b4a3e852d75d`  |
| 3021   | Layout 1 | `b4a3e852d75d`  |
| 3012   | Layout 1 | `b4a3e852d75d`  |
| 3002   | Layout 1 | `b4a3e852d75d`  |
| 2995   | Layout 1 | `b4a3e852d75d`  |
| 2987   | Layout 1 | `b4a3e852d75d`  |
| 2978   | Layout 1 | `b4a3e852d75d`  |
| 2970   | Layout 1 | `b4a3e852d75d`  |
| 2959   | Layout 1 | `b4a3e852d75d`  |
| 2951   | Layout 1 | `b4a3e852d75d`  |
| 2942   | Layout 1 | `b4a3e852d75d`  |
| 2935   | Layout 1 | `b4a3e852d75d`  |
| 2932   | Layout 1 | `b4a3e852d75d`  |
| 2923   | Layout 1 | `b4a3e852d75d`  |
| 2919   | Layout 1 | `b4a3e852d75d`  |
| 2907   | Layout 1 | `b4a3e852d75d`  |
| 2900   | Layout 1 | `b4a3e852d75d`  |
| 2891   | Layout 1 | `b4a3e852d75d`  |
| 2882   | Layout 1 | `b4a3e852d75d`  |
| 2872   | Layout 1 | `b4a3e852d75d`  |
| 2863   | Layout 1 | `b4a3e852d75d`  |
| 2855   | Layout 1 | `b4a3e852d75d`  |
| 2849   | Layout 1 | `b4a3e852d75d`  |
| 2844   | Layout 1 | `b4a3e852d75d`  |
| 2834   | Layout 1 | `b4a3e852d75d`  |
| 2825   | Layout 1 | `b4a3e852d75d`  |
| 2819   | Layout 1 | `b4a3e852d75d`  |
| 2811   | Layout 1 | `b4a3e852d75d`  |
| 2803   | Layout 1 | `b4a3e852d75d`  |
| 2794   | Layout 1 | `b4a3e852d75d`  |
| 2783   | Layout 1 | `b4a3e852d75d`  |
| 2774   | Layout 1 | `b4a3e852d75d`  |
| 2765   | Layout 1 | `b4a3e852d75d`  |
| 2756   | Layout 1 | `b4a3e852d75d`  |
| 2750   | Layout 1 | `b4a3e852d75d`  |
| 2743   | Layout 1 | `b4a3e852d75d`  |
| 2736   | Layout 1 | `b4a3e852d75d`  |
| 2726   | Layout 1 | `b4a3e852d75d`  |
| 2717   | Layout 1 | `b4a3e852d75d`  |
| 2709   | Layout 1 | `b4a3e852d75d`  |
| 2703   | Layout 1 | `b4a3e852d75d`  |
| 2695   | Layout 1 | `b4a3e852d75d`  |
| 2684   | Layout 1 | `b4a3e852d75d`  |
| 2672   | Layout 1 | `b4a3e852d75d`  |
| 2665   | Layout 1 | `b4a3e852d75d`  |
| 2657   | Layout 1 | `b4a3e852d75d`  |
| 2649   | Layout 1 | `b4a3e852d75d`  |
| 2644   | Layout 1 | `b4a3e852d75d`  |
| 2637   | Layout 1 | `b4a3e852d75d`  |
| 2629   | Layout 1 | `b4a3e852d75d`  |
| 2619   | Layout 1 | `b4a3e852d75d`  |
| 2612   | Layout 1 | `b4a3e852d75d`  |
| 2606   | Layout 1 | `b4a3e852d75d`  |
| 2602   | Layout 1 | `b4a3e852d75d`  |
| 2601   | Layout 1 | `b4a3e852d75d`  |
| 2592   | Layout 1 | `b4a3e852d75d`  |
| 2583   | Layout 1 | `b4a3e852d75d`  |
| 2575   | Layout 1 | `b4a3e852d75d`  |
| 2567   | Layout 1 | `b4a3e852d75d`  |
| 2560   | Layout 1 | `b4a3e852d75d`  |
| 2553   | Layout 1 | `b4a3e852d75d`  |
| 2545   | Layout 1 | `b4a3e852d75d`  |
| 2538   | Layout 1 | `b4a3e852d75d`  |
| 2529   | Layout 1 | `b4a3e852d75d`  |
| 2519   | Layout 1 | `b4a3e852d75d`  |
| 2513   | Layout 1 | `b4a3e852d75d`  |
| 2510   | Layout 1 | `b4a3e852d75d`  |
| 2507   | Layout 1 | `b4a3e852d75d`  |
| 2503   | Layout 1 | `b4a3e852d75d`  |
| 2498   | Layout 1 | `b4a3e852d75d`  |
| 2492   | Layout 1 | `b4a3e852d75d`  |
| 2487   | Layout 1 | `b4a3e852d75d`  |
| 2480   | Layout 1 | `b4a3e852d75d`  |
| 2474   | Layout 1 | `b4a3e852d75d`  |
| 2468   | Layout 1 | `b4a3e852d75d`  |
| 2460   | Layout 1 | `b4a3e852d75d`  |
| 2453   | Layout 1 | `b4a3e852d75d`  |
| 2444   | Layout 1 | `b4a3e852d75d`  |
| 2438   | Layout 1 | `b4a3e852d75d`  |
| 2434   | Layout 1 | `b4a3e852d75d`  |
| 2429   | Layout 1 | `b4a3e852d75d`  |
| 2421   | Layout 1 | `b4a3e852d75d`  |
| 2414   | Layout 1 | `b4a3e852d75d`  |
| 2407   | Layout 1 | `b4a3e852d75d`  |
| 2401   | Layout 1 | `b4a3e852d75d`  |
| 2397   | Layout 1 | `b4a3e852d75d`  |
| 2393   | Layout 1 | `b4a3e852d75d`  |
| 2384   | Layout 1 | `b4a3e852d75d`  |
| 2378   | Layout 1 | `b4a3e852d75d`  |
| 2372   | Layout 1 | `b4a3e852d75d`  |
| 2358   | Layout 1 | `b4a3e852d75d`  |
| 2352   | Layout 1 | `b4a3e852d75d`  |
| 2347   | Layout 1 | `b4a3e852d75d`  |
| 2343   | Layout 1 | `b4a3e852d75d`  |
| 2335   | Layout 1 | `b4a3e852d75d`  |
| 2327   | Layout 1 | `b4a3e852d75d`  |
| 2324   | Layout 1 | `b4a3e852d75d`  |
| 2319   | Layout 1 | `b4a3e852d75d`  |
| 2313   | Layout 1 | `b4a3e852d75d`  |
| 2308   | Layout 1 | `b4a3e852d75d`  |
| 2302   | Layout 1 | `b4a3e852d75d`  |
| 2295   | Layout 1 | `b4a3e852d75d`  |
| 2290   | Layout 1 | `b4a3e852d75d`  |
| 2284   | Layout 1 | `b4a3e852d75d`  |
| 2276   | Layout 1 | `b4a3e852d75d`  |
| 2269   | Layout 1 | `b4a3e852d75d`  |
| 2259   | Layout 1 | `b4a3e852d75d`  |
| 2250   | Layout 1 | `b4a3e852d75d`  |
| 2243   | Layout 1 | `b4a3e852d75d`  |
| 2235   | Layout 1 | `b4a3e852d75d`  |
| 2229   | Layout 1 | `b4a3e852d75d`  |
| 2224   | Layout 1 | `b4a3e852d75d`  |
| 2218   | Layout 1 | `b4a3e852d75d`  |
| 2215   | Layout 1 | `b4a3e852d75d`  |
| 2207   | Layout 1 | `b4a3e852d75d`  |
| 2203   | Layout 1 | `b4a3e852d75d`  |
| 2196   | Layout 1 | `b4a3e852d75d`  |
| 2192   | Layout 1 | `b4a3e852d75d`  |
| 2189   | Layout 1 | `b4a3e852d75d`  |
| 2183   | Layout 1 | `b4a3e852d75d`  |
| 2179   | Layout 1 | `b4a3e852d75d`  |
| 2171   | Layout 1 | `b4a3e852d75d`  |
| 2163   | Layout 1 | `b4a3e852d75d`  |
| 2156   | Layout 1 | `b4a3e852d75d`  |
| 2151   | Layout 1 | `b4a3e852d75d`  |
| 2147   | Layout 1 | `b4a3e852d75d`  |
| 2142   | Layout 1 | `b4a3e852d75d`  |
| 2138   | Layout 1 | `b4a3e852d75d`  |
| 2134   | Layout 1 | `b4a3e852d75d`  |
| 2130   | Layout 1 | `b4a3e852d75d`  |
| 2122   | Layout 1 | `b4a3e852d75d`  |
| 2107   | Layout 1 | `b4a3e852d75d`  |
| 2098   | Layout 1 | `b4a3e852d75d`  |
| 2089   | Layout 1 | `b4a3e852d75d`  |
| 2081   | Layout 1 | `b4a3e852d75d`  |
| 2073   | Layout 1 | `b4a3e852d75d`  |
| 2067   | Layout 1 | `b4a3e852d75d`  |
| 2063   | Layout 1 | `b4a3e852d75d`  |
| 2059   | Layout 1 | `b4a3e852d75d`  |
| 2052   | Layout 1 | `b4a3e852d75d`  |
| 2044   | Layout 1 | `b4a3e852d75d`  |
| 2039   | Layout 1 | `b4a3e852d75d`  |
| 2032   | Layout 1 | `b4a3e852d75d`  |
| 2025   | Layout 1 | `b4a3e852d75d`  |
| 2011   | Layout 1 | `b4a3e852d75d`  |
| 2005   | Layout 1 | `b4a3e852d75d`  |
| 2000   | Layout 1 | `b4a3e852d75d`  |
| 1996   | Layout 1 | `b4a3e852d75d`  |
| 1991   | Layout 1 | `b4a3e852d75d`  |
| 1985   | Layout 1 | `b4a3e852d75d`  |
| 1980   | Layout 1 | `b4a3e852d75d`  |
| 1969   | Layout 1 | `b4a3e852d75d`  |
| 1964   | Layout 1 | `b4a3e852d75d`  |
| 1958   | Layout 1 | `b4a3e852d75d`  |
| 1950   | Layout 1 | `b4a3e852d75d`  |
| 1945   | Layout 1 | `b4a3e852d75d`  |
| 1937   | Layout 1 | `b4a3e852d75d`  |
| 1933   | Layout 1 | `b4a3e852d75d`  |
| 1927   | Layout 1 | `b4a3e852d75d`  |
| 1921   | Layout 1 | `b4a3e852d75d`  |
| 1914   | Layout 1 | `b4a3e852d75d`  |
| 1908   | Layout 1 | `b4a3e852d75d`  |
| 1897   | Layout 1 | `b4a3e852d75d`  |
| 1892   | Layout 1 | `b4a3e852d75d`  |
| 1886   | Layout 1 | `b4a3e852d75d`  |
| 1881   | Layout 1 | `b4a3e852d75d`  |
| 1871   | Layout 1 | `b4a3e852d75d`  |
| 1866   | Layout 1 | `b4a3e852d75d`  |
| 1862   | Layout 1 | `b4a3e852d75d`  |
| 1854   | Layout 1 | `b4a3e852d75d`  |
| 1846   | Layout 1 | `b4a3e852d75d`  |
| 1838   | Layout 1 | `b4a3e852d75d`  |
| 1832   | Layout 1 | `b4a3e852d75d`  |
| 1826   | Layout 1 | `b4a3e852d75d`  |
| 1822   | Layout 1 | `b4a3e852d75d`  |
| 1818   | Layout 1 | `b4a3e852d75d`  |
| 1804   | No file  | `b4a3e852d75d`  |
| 1794   | No file  | `b4a3e852d75d`  |
| 1790   | No file  | `b4a3e852d75d`  |
| 1784   | No file  | `b4a3e852d75d`  |
| 1774   | No file  | `b4a3e852d75d`  |
| 1771   | No file  | `b4a3e852d75d`  |
| 1762   | No file  | `b4a3e852d75d`  |
| 1759   | No file  | `b4a3e852d75d`  |
| 1754   | No file  | `b4a3e852d75d`  |
| 1749   | No file  | `b4a3e852d75d`  |
| 1743   | No file  | `b4a3e852d75d`  |
| 1737   | No file  | `b4a3e852d75d`  |
| 1731   | No file  | `b4a3e852d75d`  |
| 1725   | No file  | `b4a3e852d75d`  |
| 1717   | No file  | `b4a3e852d75d`  |
| 1710   | No file  | `b4a3e852d75d`  |
| 1704   | No file  | `b4a3e852d75d`  |
| 1698   | No file  | `b4a3e852d75d`  |
| 1690   | No file  | `b4a3e852d75d`  |
| 1685   | No file  | `b4a3e852d75d`  |
| 1680   | No file  | `b4a3e852d75d`  |
| 1674   | No file  | `b4a3e852d75d`  |
| 1668   | No file  | `b4a3e852d75d`  |
| 1659   | No file  | `b4a3e852d75d`  |
| 1649   | No file  | `b4a3e852d75d`  |
| 1642   | No file  | `b4a3e852d75d`  |
| 1636   | No file  | `b4a3e852d75d`  |
| 1628   | No file  | `b4a3e852d75d`  |
| 1622   | No file  | `b4a3e852d75d`  |
| 1614   | No file  | `b4a3e852d75d`  |
| 1608   | No file  | `b4a3e852d75d`  |
| 1602   | No file  | `b4a3e852d75d`  |
| 1598   | No file  | `b4a3e852d75d`  |
| 1594   | No file  | `b4a3e852d75d`  |
| 1590   | No file  | `b4a3e852d75d`  |
| 1587   | No file  | `b4a3e852d75d`  |
| 1584   | No file  | `b4a3e852d75d`  |
| 1579   | No file  | `b4a3e852d75d`  |
| 1572   | No file  | `b4a3e852d75d`  |
| 1565   | No file  | `b4a3e852d75d`  |
| 1559   | No file  | `b4a3e852d75d`  |
| 1554   | No file  | `b4a3e852d75d`  |
| 1547   | No file  | `b4a3e852d75d`  |
| 1537   | No file  | `b4a3e852d75d`  |
| 1529   | No file  | `b4a3e852d75d`  |
| 1524   | No file  | `b4a3e852d75d`  |
| 1519   | No file  | `b4a3e852d75d`  |
| 1509   | No file  | `b4a3e852d75d`  |
| 1506   | No file  | `b4a3e852d75d`  |
| 1504   | No file  | `b4a3e852d75d`  |
| 1500   | No file  | `b4a3e852d75d`  |
| 1493   | No file  | `b4a3e852d75d`  |
| 1489   | No file  | `b4a3e852d75d`  |
| 1485   | No file  | `b4a3e852d75d`  |
| 1481   | No file  | `b4a3e852d75d`  |
| 1474   | No file  | `b4a3e852d75d`  |
| 1466   | No file  | `b4a3e852d75d`  |
| 1462   | No file  | `b4a3e852d75d`  |
| 1459   | No file  | `b4a3e852d75d`  |
| 1453   | No file  | `b4a3e852d75d`  |
| 1450   | No file  | `b4a3e852d75d`  |
| 1445   | No file  | `b4a3e852d75d`  |
| 1439   | No file  | `b4a3e852d75d`  |
| 1433   | No file  | `b4a3e852d75d`  |
| 1430   | No file  | `b4a3e852d75d`  |
| 1426   | No file  | `b4a3e852d75d`  |
| 1421   | No file  | `b4a3e852d75d`  |
| 1417   | No file  | `b4a3e852d75d`  |
| 1416   | No file  | `b4a3e852d75d`  |
| 1409   | No file  | `b4a3e852d75d`  |
| 1405   | No file  | `b4a3e852d75d`  |
| 1401   | No file  | `b4a3e852d75d`  |
| 1396   | No file  | `b4a3e852d75d`  |
| 1391   | No file  | `b4a3e852d75d`  |
| 1390   | No file  | `b4a3e852d75d`  |
| 1386   | No file  | `b4a3e852d75d`  |
| 1381   | No file  | `b4a3e852d75d`  |
| 1379   | No file  | `b4a3e852d75d`  |
| 1372   | No file  | `b4a3e852d75d`  |
| 1366   | No file  | `b4a3e852d75d`  |
| 1364   | No file  | `b4a3e852d75d`  |
| 1363   | No file  | `b4a3e852d75d`  |
| 1360   | No file  | `b4a3e852d75d`  |
| 1358   | No file  | `b4a3e852d75d`  |
| 1355   | No file  | `b4a3e852d75d`  |
| 1351   | No file  | `b4a3e852d75d`  |
| 1348   | No file  | `b4a3e852d75d`  |
| 1346   | No file  | `b4a3e852d75d`  |
| 1341   | No file  | `b4a3e852d75d`  |
| 1340   | No file  | `b4a3e852d75d`  |
| 1338   | No file  | `b4a3e852d75d`  |
| 1335   | No file  | `b4a3e852d75d`  |
| 1333   | No file  | `b4a3e852d75d`  |
| 1329   | No file  | `b4a3e852d75d`  |
| 1327   | No file  | `b4a3e852d75d`  |
| 1324   | No file  | `b4a3e852d75d`  |
| 1321   | No file  | `b4a3e852d75d`  |
| 1319   | No file  | `b4a3e852d75d`  |
| 1318   | No file  | `b4a3e852d75d`  |
| 1316   | No file  | `b4a3e852d75d`  |
| 1313   | No file  | `b4a3e852d75d`  |
| 1311   | No file  | `b4a3e852d75d`  |
| 1309   | No file  | `b4a3e852d75d`  |
| 1304   | No file  | `b4a3e852d75d`  |
| 1292   | No file  | `b4a3e852d75d`  |
| 1286   | No file  | `b4a3e852d75d`  |
| 1280   | No file  | `b4a3e852d75d`  |
| 1276   | No file  | `b4a3e852d75d`  |
| 1267   | No file  | `b4a3e852d75d`  |
| 1261   | No file  | `b4a3e852d75d`  |
| 1256   | No file  | `b4a3e852d75d`  |
| 1250   | No file  | `b4a3e852d75d`  |
| 1246   | No file  | `b4a3e852d75d`  |
| 1239   | No file  | `b4a3e852d75d`  |
| 1230   | No file  | `b4a3e852d75d`  |
| 1226   | No file  | `b4a3e852d75d`  |
| 1220   | No file  | `b4a3e852d75d`  |
| 1217   | No file  | `b4a3e852d75d`  |
| 1211   | No file  | `b4a3e852d75d`  |
| 1210   | No file  | `b4a3e852d75d`  |
| 1208   | No file  | `b4a3e852d75d`  |
| 1203   | No file  | `b4a3e852d75d`  |
| 1197   | No file  | `b4a3e852d75d`  |
| 1194   | No file  | `b4a3e852d75d`  |
| 1192   | No file  | `b4a3e852d75d`  |
| 1187   | No file  | `b4a3e852d75d`  |
| 1183   | No file  | `b4a3e852d75d`  |
| 1177   | No file  | `b4a3e852d75d`  |
| 1173   | No file  | `b4a3e852d75d`  |
| 1167   | No file  | `b4a3e852d75d`  |
| 1164   | No file  | `b4a3e852d75d`  |
| 1156   | No file  | `b4a3e852d75d`  |
| 1149   | No file  | `b4a3e852d75d`  |
| 1144   | No file  | `b4a3e852d75d`  |
| 1137   | No file  | `b4a3e852d75d`  |
| 1132   | No file  | `b4a3e852d75d`  |
| 1127   | No file  | `b4a3e852d75d`  |
| 1122   | No file  | `b4a3e852d75d`  |
| 1118   | No file  | `b4a3e852d75d`  |
| 1114   | No file  | `b4a3e852d75d`  |
| 1109   | No file  | `b4a3e852d75d`  |
| 1102   | No file  | `b4a3e852d75d`  |
| 1096   | No file  | `b4a3e852d75d`  |
| 1088   | No file  | `b4a3e852d75d`  |
| 1081   | No file  | `b4a3e852d75d`  |
| 1076   | No file  | `b4a3e852d75d`  |
| 1069   | No file  | `b4a3e852d75d`  |
| 1064   | No file  | `b4a3e852d75d`  |
| 1058   | No file  | `b4a3e852d75d`  |
| 1051   | No file  | `b4a3e852d75d`  |
| 1044   | No file  | `b4a3e852d75d`  |
| 1036   | No file  | `b4a3e852d75d`  |
| 1026   | No file  | `b4a3e852d75d`  |
| 1016   | No file  | `b4a3e852d75d`  |
| 1009   | No file  | `b4a3e852d75d`  |
| 1005   | No file  | `b4a3e852d75d`  |
| 1000   | No file  | `b4a3e852d75d`  |
| 998    | No file  | `b4a3e852d75d`  |
| 990    | No file  | `b4a3e852d75d`  |
| 979    | No file  | `b4a3e852d75d`  |
| 972    | No file  | `b4a3e852d75d`  |
| 963    | No file  | `b4a3e852d75d`  |
| 955    | No file  | `b4a3e852d75d`  |
| 946    | No file  | `b4a3e852d75d`  |
| 938    | No file  | `b4a3e852d75d`  |
| 927    | No file  | `b4a3e852d75d`  |
| 911    | No file  | `b4a3e852d75d`  |
| 904    | No file  | `b4a3e852d75d`  |
| 899    | No file  | `b4a3e852d75d`  |
| 894    | No file  | `b4a3e852d75d`  |
| 885    | No file  | `b4a3e852d75d`  |
| 879    | No file  | `b4a3e852d75d`  |
| 872    | No file  | `b4a3e852d75d`  |
| 864    | No file  | `b4a3e852d75d`  |
| 855    | No file  | `b4a3e852d75d`  |
| 853    | No file  | `b4a3e852d75d`  |
| 845    | No file  | `b4a3e852d75d`  |
| 837    | No file  | `b4a3e852d75d`  |
| 829    | No file  | `b4a3e852d75d`  |
| 822    | No file  | `b4a3e852d75d`  |
| 814    | No file  | `b4a3e852d75d`  |
| 805    | No file  | `b4a3e852d75d`  |
| 794    | No file  | `b4a3e852d75d`  |
| 787    | No file  | `b4a3e852d75d`  |
| 780    | No file  | `b4a3e852d75d`  |
| 771    | No file  | `b4a3e852d75d`  |
| 760    | No file  | `b4a3e852d75d`  |
| 748    | No file  | `b4a3e852d75d`  |
| 741    | No file  | `b4a3e852d75d`  |
| 736    | No file  | `b4a3e852d75d`  |
| 731    | No file  | `b4a3e852d75d`  |
| 723    | No file  | `b4a3e852d75d`  |
| 711    | No file  | `b4a3e852d75d`  |
| 707    | No file  | `b4a3e852d75d`  |
| 697    | No file  | `b4a3e852d75d`  |
| 689    | No file  | `b4a3e852d75d`  |
| 683    | No file  | `b4a3e852d75d`  |
| 678    | No file  | `b4a3e852d75d`  |
| 670    | No file  | `b4a3e852d75d`  |
| 661    | No file  | `b4a3e852d75d`  |
| 656    | No file  | `b4a3e852d75d`  |
| 652    | No file  | `b4a3e852d75d`  |
| 643    | No file  | `b4a3e852d75d`  |
| 637    | No file  | `b4a3e852d75d`  |
| 630    | No file  | `b4a3e852d75d`  |
| 627    | No file  | `b4a3e852d75d`  |
| 621    | No file  | `b4a3e852d75d`  |
| 617    | No file  | `b4a3e852d75d`  |
| 615    | No file  | `b4a3e852d75d`  |
| 606    | No file  | `b4a3e852d75d`  |
| 599    | No file  | `b4a3e852d75d`  |
| 592    | No file  | `b4a3e852d75d`  |
| 586    | No file  | `b4a3e852d75d`  |
| 577    | No file  | `b4a3e852d75d`  |
| 569    | No file  | `b4a3e852d75d`  |
| 561    | No file  | `b4a3e852d75d`  |
| 554    | No file  | `b4a3e852d75d`  |
| 542    | No file  | `b4a3e852d75d`  |
| 532    | No file  | `b4a3e852d75d`  |
| 531    | No file  | `b4a3e852d75d`  |
| 526    | No file  | `b4a3e852d75d`  |
| 521    | No file  | `b4a3e852d75d`  |
| 517    | No file  | `b4a3e852d75d`  |
| 510    | No file  | `b4a3e852d75d`  |
| 508    | No file  | `b4a3e852d75d`  |
| 504    | No file  | `b4a3e852d75d`  |
| 497    | No file  | `b4a3e852d75d`  |
| 491    | No file  | `b4a3e852d75d`  |
| 485    | No file  | `b4a3e852d75d`  |
| 478    | No file  | `b4a3e852d75d`  |
| 472    | No file  | `b4a3e852d75d`  |
| 466    | No file  | `b4a3e852d75d`  |
| 457    | No file  | `b4a3e852d75d`  |
| 452    | No file  | `b4a3e852d75d`  |
| 449    | No file  | `b4a3e852d75d`  |
| 435    | No file  | `b4a3e852d75d`  |

<!-- versions:end -->

## Companion Files

None. The handler names each item with LOC type 0 from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of prizes; `0` between events          |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (26 bytes)

| Offset  | Type | Field         | Notes                                                                  |
| ------- | ---- | ------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | item_key      | The prize: `enchant_level << 24 \| item_id`                            |
| `+0x04` | u32  | coin_item_key | The item a draw costs; the same on every row                           |
| `+0x08` | u32  | lose_item_key | The item a lost draw gives; the same on every row                      |
| `+0x0C` | u32  | unknown_0c    | `0` on every row of every client checked                               |
| `+0x10` | u16  | index         | `1` to `row_count`, unique; the draw number `ToClient_RequestDrawItem` takes |
| `+0x12` | u16  | item_count    | Count of the prize                                                     |
| `+0x14` | u16  | unknown_14    | See Open Questions                                                     |
| `+0x16` | u16  | unknown_16    | See Open Questions                                                     |
| `+0x18` | u8   | unknown_18    | `0` or `1`; see Open Questions                                         |
| `+0x19` | u8   | unknown_19    | `0` or `1`; see Open Questions                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Events

The coin and lose items of four clients, with the prize count and the
values of `unknown_14` and `unknown_16`.

| Client | Prizes | `coin_item_key`                                  | `lose_item_key`                              | `unknown_14`       | `unknown_16`       |
| ------ | ------ | ------------------------------------------------ | -------------------------------------------- | ------------------ | ------------------ |
| 2276   | 16     | 752218 [Event] Box Full O' Love                  | 752219 [Event] Sweet Chocolate               | 10 to 50           | equal to `unknown_14` |
| 2583   | 12     | 752669 [Event] Old Moon ADV Lesson Ticket        | 752649 [Event] Jetina's Certificate Seal     | 10, 12 on one row  | 1                  |
| 3242   | 10     | 1000572 [Event] Exciting 10th Anniversary ADV Ticket | 1000571 [Event] Decade-Infused Pearl     | 3500               | 1                  |
| 3483   | 8      | 1000807 [Event] Agent's Adventures               | 1000808 [Event] Agent's Seal                 | 300                | 1                  |

The rows are not in `index` order. Clients 3103, 3169, 3303 and 3364 hold
an empty file (`row_count` `0`). One prize of client 2276 is Caphras Stone
with `item_count` `5000`; every other prize of the four clients has
`item_count` `1`.

## Field Names

The file is not in the archives of client 1784, and no sheet of a private
server's `DataSheets.bexcel` on that client has `Draw` in its name. The
names follow the draw wrapper getters of the client Lua (client 3482,
`panel_event_ticketshop_all_1` and `_2`):

- `getItemkey()` and `getItemCount()` fill the prize slot; the prize varies
  per row, which leaves `item_key` at `+0x00`, and `item_count` is `5000`
  on the Caphras Stone prize of client 2276.
- `getCoinItemKey()` and `getLoseItemKey()` name the two currency tooltips.
  `lose_item_key` is the item the draw prompt says a draw may give
  (`[Event] Agent's Seal`, `1000808`); `coin_item_key` is the event ticket
  the event's challenges hand out (`1000807`, "Use it to choose from
  various adventures").
- `getIndex()` is the number `ToClient_RequestDrawItem` and
  `ToClient_CheckCanDrawItem` take; `index` is the only field that runs
  from `1` to `row_count`.

The Lua reads five more values per prize: `getCoinCount()` (the `{ticket}`
count of the draw prompt), `getLoseCoinCount()`, `getDrawMaxCount()` and
`getDrawMinCount()` (a prize shows sold out when max minus min is `0` or
less), and `getIsSpecialItem()`. They are the leads for the five unnamed
fields.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/enchantshop_tables.py`:
  the index, the prize with its icon and LOC name, the coin and lose items
  and the prize count.

## Open Questions

### Which of `unknown_14` and `unknown_16` Is the Coin Count

One of the two is likely `getCoinCount()` and the other
`getLoseCoinCount()`. `unknown_16` is `1` on every event since client 2583,
and the client 3483 coin item is a single log a player uses to start one
adventure, which fits a cost of one coin per draw. `unknown_14` (`300` on
client 3483) equals the `[Event] Agent's Seal x300` each Agent's
Adventures quest rewards, which fits the lose count. On client 2276 both
fields hold the same value on every row, so that client cannot split them.

### What `unknown_18` and `unknown_19` Flag

On client 2276 `unknown_18` is `1` on 5 of 16 prizes: the TET (IV) Black
Distortion Earring (`67120717`, Black Distortion Earring at level 4), the
Choose Your Ship License: Epheria Carrack Box, Choose Your TET (IV)
Blackstar Weapon Box, Choose Your TET (IV) Manos Accessory Box and Choose
Your Horse Emblem: Dream Horse Box. These are the highest prizes, a lead
for `getIsSpecialItem()`. `unknown_19` is `1` on 14 of 16 prizes and `0`
on the Combat/Skill EXP Exchange Coupon and the Weapon Exchange Coupon
Box. Both bytes are `0` on every later event checked.

### What `unknown_0c` Holds

`unknown_0c` is `0` on every row of clients 2276, 2583, 2765, 3030, 3242
and 3483. With `getDrawMaxCount()` and `getDrawMinCount()` both unplaced,
it may be one of them.
