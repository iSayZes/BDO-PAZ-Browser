# `growthpasslinkdata.bss` Format

## Purpose

The guide links on the quest cells of the Growth Pass window: per quest, one
entry per service resource type (the client's language build) with up to three
web links and the name of each link's author. `panel_window_growthpass_1.luac`
shows the buttons `Button_GuideLink1` to `Button_GuideLink3` on a quest cell
of [`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md) for
`questWrapper:getNoteLinkSize(getGameServiceResType())` links, and
`PaGlobalFunc_GrowthPass_AdventurerNotes(questGroup, questId, idx)` in
`panel_window_growthpass_2.luac` opens link `idx`
(`questWrapper:getNoteLink(idx, gameServiceResType)`) in the in-game web
browser. The file is the client build of the developers' `GrowthPass_Link`
sheet (see [Field Names](#field-names)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records                        | Row bytes |
| ------ | -------------- | ------------------------ | ----- | ------------------------------ | --------- |
| 1      | 2059 and later | `growthpasslinkdata.bss` | 3,992 | 145 Link, 145 Entry, 37 Record | 8         |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `growthpasslinkdata.bss` | 3,992 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `bc5d9ce24351`  |
| 3482   | Layout 1 | `bc5d9ce24351`  |
| 3474   | Layout 1 | `bc5d9ce24351`  |
| 3473   | Layout 1 | `bc5d9ce24351`  |
| 3464   | Layout 1 | `bc5d9ce24351`  |
| 3458   | Layout 1 | `bc5d9ce24351`  |
| 3454   | Layout 1 | `bc5d9ce24351`  |
| 3444   | Layout 1 | `bc5d9ce24351`  |
| 3435   | Layout 1 | `bc5d9ce24351`  |
| 3426   | Layout 1 | `bc5d9ce24351`  |
| 3418   | Layout 1 | `bc5d9ce24351`  |
| 3412   | Layout 1 | `bc5d9ce24351`  |
| 3402   | Layout 1 | `bc5d9ce24351`  |
| 3396   | Layout 1 | `bc5d9ce24351`  |
| 3387   | Layout 1 | `bc5d9ce24351`  |
| 3381   | Layout 1 | `bc5d9ce24351`  |
| 3373   | Layout 1 | `bc5d9ce24351`  |
| 3364   | Layout 1 | `bc5d9ce24351`  |
| 3356   | Layout 1 | `bc5d9ce24351`  |
| 3349   | Layout 1 | `bc5d9ce24351`  |
| 3342   | Layout 1 | `bc5d9ce24351`  |
| 3335   | Layout 1 | `bc5d9ce24351`  |
| 3326   | Layout 1 | `bc5d9ce24351`  |
| 3321   | Layout 1 | `bc5d9ce24351`  |
| 3314   | Layout 1 | `bc5d9ce24351`  |
| 3303   | Layout 1 | `bc5d9ce24351`  |
| 3302   | Layout 1 | `bc5d9ce24351`  |
| 3293   | Layout 1 | `bc5d9ce24351`  |
| 3283   | Layout 1 | `bc5d9ce24351`  |
| 3275   | Layout 1 | `bc5d9ce24351`  |
| 3267   | Layout 1 | `bc5d9ce24351`  |
| 3258   | Layout 1 | `bc5d9ce24351`  |
| 3251   | Layout 1 | `bc5d9ce24351`  |
| 3242   | Layout 1 | `bc5d9ce24351`  |
| 3235   | Layout 1 | `bc5d9ce24351`  |
| 3229   | Layout 1 | `bc5d9ce24351`  |
| 3212   | Layout 1 | `bc5d9ce24351`  |
| 3203   | Layout 1 | `bc5d9ce24351`  |
| 3193   | Layout 1 | `bc5d9ce24351`  |
| 3186   | Layout 1 | `bc5d9ce24351`  |
| 3177   | Layout 1 | `bc5d9ce24351`  |
| 3169   | Layout 1 | `bc5d9ce24351`  |
| 3158   | Layout 1 | `bc5d9ce24351`  |
| 3151   | Layout 1 | `bc5d9ce24351`  |
| 3144   | Layout 1 | `bc5d9ce24351`  |
| 3133   | Layout 1 | `bc5d9ce24351`  |
| 3125   | Layout 1 | `bc5d9ce24351`  |
| 3118   | Layout 1 | `bc5d9ce24351`  |
| 3111   | Layout 1 | `bc5d9ce24351`  |
| 3103   | Layout 1 | `bc5d9ce24351`  |
| 3095   | Layout 1 | `bc5d9ce24351`  |
| 3086   | Layout 1 | `bc5d9ce24351`  |
| 3072   | Layout 1 | `bc5d9ce24351`  |
| 3062   | Layout 1 | `bc5d9ce24351`  |
| 3052   | Layout 1 | `bc5d9ce24351`  |
| 3045   | Layout 1 | `bc5d9ce24351`  |
| 3037   | Layout 1 | `bc5d9ce24351`  |
| 3030   | Layout 1 | `bc5d9ce24351`  |
| 3021   | Layout 1 | `bc5d9ce24351`  |
| 3012   | Layout 1 | `bc5d9ce24351`  |
| 3002   | Layout 1 | `bc5d9ce24351`  |
| 2995   | Layout 1 | `bc5d9ce24351`  |
| 2987   | Layout 1 | `bc5d9ce24351`  |
| 2978   | Layout 1 | `bc5d9ce24351`  |
| 2970   | Layout 1 | `bc5d9ce24351`  |
| 2959   | Layout 1 | `bc5d9ce24351`  |
| 2951   | Layout 1 | `bc5d9ce24351`  |
| 2942   | Layout 1 | `bc5d9ce24351`  |
| 2935   | Layout 1 | `bc5d9ce24351`  |
| 2932   | Layout 1 | `bc5d9ce24351`  |
| 2923   | Layout 1 | `bc5d9ce24351`  |
| 2919   | Layout 1 | `bc5d9ce24351`  |
| 2907   | Layout 1 | `bc5d9ce24351`  |
| 2900   | Layout 1 | `bc5d9ce24351`  |
| 2891   | Layout 1 | `bc5d9ce24351`  |
| 2882   | Layout 1 | `bc5d9ce24351`  |
| 2872   | Layout 1 | `bc5d9ce24351`  |
| 2863   | Layout 1 | `bc5d9ce24351`  |
| 2855   | Layout 1 | `bc5d9ce24351`  |
| 2849   | Layout 1 | `bc5d9ce24351`  |
| 2844   | Layout 1 | `bc5d9ce24351`  |
| 2834   | Layout 1 | `bc5d9ce24351`  |
| 2825   | Layout 1 | `bc5d9ce24351`  |
| 2819   | Layout 1 | `bc5d9ce24351`  |
| 2811   | Layout 1 | `bc5d9ce24351`  |
| 2803   | Layout 1 | `bc5d9ce24351`  |
| 2794   | Layout 1 | `bc5d9ce24351`  |
| 2783   | Layout 1 | `bc5d9ce24351`  |
| 2774   | Layout 1 | `bc5d9ce24351`  |
| 2765   | Layout 1 | `bc5d9ce24351`  |
| 2756   | Layout 1 | `bc5d9ce24351`  |
| 2750   | Layout 1 | `bc5d9ce24351`  |
| 2743   | Layout 1 | `bc5d9ce24351`  |
| 2736   | Layout 1 | `bc5d9ce24351`  |
| 2726   | Layout 1 | `bc5d9ce24351`  |
| 2717   | Layout 1 | `bc5d9ce24351`  |
| 2709   | Layout 1 | `bc5d9ce24351`  |
| 2703   | Layout 1 | `bc5d9ce24351`  |
| 2695   | Layout 1 | `bc5d9ce24351`  |
| 2684   | Layout 1 | `bc5d9ce24351`  |
| 2672   | Layout 1 | `bc5d9ce24351`  |
| 2665   | Layout 1 | `bc5d9ce24351`  |
| 2657   | Layout 1 | `bc5d9ce24351`  |
| 2649   | Layout 1 | `bc5d9ce24351`  |
| 2644   | Layout 1 | `bc5d9ce24351`  |
| 2637   | Layout 1 | `bc5d9ce24351`  |
| 2629   | Layout 1 | `bc5d9ce24351`  |
| 2619   | Layout 1 | `bc5d9ce24351`  |
| 2612   | Layout 1 | `bc5d9ce24351`  |
| 2606   | Layout 1 | `bc5d9ce24351`  |
| 2602   | Layout 1 | `bc5d9ce24351`  |
| 2601   | Layout 1 | `bc5d9ce24351`  |
| 2592   | Layout 1 | `bc5d9ce24351`  |
| 2583   | Layout 1 | `bc5d9ce24351`  |
| 2575   | Layout 1 | `bc5d9ce24351`  |
| 2567   | Layout 1 | `bc5d9ce24351`  |
| 2560   | Layout 1 | `bc5d9ce24351`  |
| 2553   | Layout 1 | `bc5d9ce24351`  |
| 2545   | Layout 1 | `bc5d9ce24351`  |
| 2538   | Layout 1 | `bc5d9ce24351`  |
| 2529   | Layout 1 | `bc5d9ce24351`  |
| 2519   | Layout 1 | `bc5d9ce24351`  |
| 2513   | Layout 1 | `bc5d9ce24351`  |
| 2510   | Layout 1 | `bc5d9ce24351`  |
| 2507   | Layout 1 | `bc5d9ce24351`  |
| 2503   | Layout 1 | `bc5d9ce24351`  |
| 2498   | Layout 1 | `bc5d9ce24351`  |
| 2492   | Layout 1 | `bc5d9ce24351`  |
| 2487   | Layout 1 | `bc5d9ce24351`  |
| 2480   | Layout 1 | `bc5d9ce24351`  |
| 2474   | Layout 1 | `bc5d9ce24351`  |
| 2468   | Layout 1 | `bc5d9ce24351`  |
| 2460   | Layout 1 | `bc5d9ce24351`  |
| 2453   | Layout 1 | `bc5d9ce24351`  |
| 2444   | Layout 1 | `bc5d9ce24351`  |
| 2438   | Layout 1 | `bc5d9ce24351`  |
| 2434   | Layout 1 | `bc5d9ce24351`  |
| 2429   | Layout 1 | `bc5d9ce24351`  |
| 2421   | Layout 1 | `bc5d9ce24351`  |
| 2414   | Layout 1 | `bc5d9ce24351`  |
| 2407   | Layout 1 | `bc5d9ce24351`  |
| 2401   | Layout 1 | `bc5d9ce24351`  |
| 2397   | Layout 1 | `bc5d9ce24351`  |
| 2393   | Layout 1 | `bc5d9ce24351`  |
| 2384   | Layout 1 | `bc5d9ce24351`  |
| 2378   | Layout 1 | `bc5d9ce24351`  |
| 2372   | Layout 1 | `bc5d9ce24351`  |
| 2358   | Layout 1 | `bc5d9ce24351`  |
| 2352   | Layout 1 | `bc5d9ce24351`  |
| 2347   | Layout 1 | `bc5d9ce24351`  |
| 2343   | Layout 1 | `bc5d9ce24351`  |
| 2335   | Layout 1 | `bc5d9ce24351`  |
| 2327   | Layout 1 | `bc5d9ce24351`  |
| 2324   | Layout 1 | `bc5d9ce24351`  |
| 2319   | Layout 1 | `bc5d9ce24351`  |
| 2313   | Layout 1 | `bc5d9ce24351`  |
| 2308   | Layout 1 | `bc5d9ce24351`  |
| 2302   | Layout 1 | `bc5d9ce24351`  |
| 2295   | Layout 1 | `bc5d9ce24351`  |
| 2290   | Layout 1 | `bc5d9ce24351`  |
| 2284   | Layout 1 | `bc5d9ce24351`  |
| 2276   | Layout 1 | `bc5d9ce24351`  |
| 2269   | Layout 1 | `bc5d9ce24351`  |
| 2259   | Layout 1 | `bc5d9ce24351`  |
| 2250   | Layout 1 | `bc5d9ce24351`  |
| 2243   | Layout 1 | `bc5d9ce24351`  |
| 2235   | Layout 1 | `bc5d9ce24351`  |
| 2229   | Layout 1 | `bc5d9ce24351`  |
| 2224   | Layout 1 | `bc5d9ce24351`  |
| 2218   | Layout 1 | `bc5d9ce24351`  |
| 2215   | Layout 1 | `bc5d9ce24351`  |
| 2207   | Layout 1 | `bc5d9ce24351`  |
| 2203   | Layout 1 | `bc5d9ce24351`  |
| 2196   | Layout 1 | `bc5d9ce24351`  |
| 2192   | Layout 1 | `bc5d9ce24351`  |
| 2189   | Layout 1 | `bc5d9ce24351`  |
| 2183   | Layout 1 | `bc5d9ce24351`  |
| 2179   | Layout 1 | `bc5d9ce24351`  |
| 2171   | Layout 1 | `bc5d9ce24351`  |
| 2163   | Layout 1 | `bc5d9ce24351`  |
| 2156   | Layout 1 | `bc5d9ce24351`  |
| 2151   | Layout 1 | `bc5d9ce24351`  |
| 2147   | Layout 1 | `bc5d9ce24351`  |
| 2142   | Layout 1 | `bc5d9ce24351`  |
| 2138   | Layout 1 | `bc5d9ce24351`  |
| 2134   | Layout 1 | `bc5d9ce24351`  |
| 2130   | Layout 1 | `bc5d9ce24351`  |
| 2122   | Layout 1 | `bc5d9ce24351`  |
| 2107   | Layout 1 | `bc5d9ce24351`  |
| 2098   | Layout 1 | `bc5d9ce24351`  |
| 2089   | Layout 1 | `bc5d9ce24351`  |
| 2081   | Layout 1 | `bc5d9ce24351`  |
| 2073   | Layout 1 | `bc5d9ce24351`  |
| 2067   | Layout 1 | `bc5d9ce24351`  |
| 2063   | Layout 1 | `bc5d9ce24351`  |
| 2059   | Layout 1 | `bc5d9ce24351`  |
| 2052   | No file  | `bc5d9ce24351`  |
| 2044   | No file  | `bc5d9ce24351`  |
| 2039   | No file  | `bc5d9ce24351`  |
| 2032   | No file  | `bc5d9ce24351`  |
| 2025   | No file  | `bc5d9ce24351`  |
| 2011   | No file  | `bc5d9ce24351`  |
| 2005   | No file  | `bc5d9ce24351`  |
| 2000   | No file  | `bc5d9ce24351`  |
| 1996   | No file  | `bc5d9ce24351`  |
| 1991   | No file  | `bc5d9ce24351`  |
| 1985   | No file  | `bc5d9ce24351`  |
| 1980   | No file  | `bc5d9ce24351`  |
| 1969   | No file  | `bc5d9ce24351`  |
| 1964   | No file  | `bc5d9ce24351`  |
| 1958   | No file  | `bc5d9ce24351`  |
| 1950   | No file  | `bc5d9ce24351`  |
| 1945   | No file  | `bc5d9ce24351`  |
| 1937   | No file  | `bc5d9ce24351`  |
| 1933   | No file  | `bc5d9ce24351`  |
| 1927   | No file  | `bc5d9ce24351`  |
| 1921   | No file  | `bc5d9ce24351`  |
| 1914   | No file  | `bc5d9ce24351`  |
| 1908   | No file  | `bc5d9ce24351`  |
| 1897   | No file  | `bc5d9ce24351`  |
| 1892   | No file  | `bc5d9ce24351`  |
| 1886   | No file  | `bc5d9ce24351`  |
| 1881   | No file  | `bc5d9ce24351`  |
| 1871   | No file  | `bc5d9ce24351`  |
| 1866   | No file  | `bc5d9ce24351`  |
| 1862   | No file  | `bc5d9ce24351`  |
| 1854   | No file  | `bc5d9ce24351`  |
| 1846   | No file  | `bc5d9ce24351`  |
| 1838   | No file  | `bc5d9ce24351`  |
| 1832   | No file  | `bc5d9ce24351`  |
| 1826   | No file  | `bc5d9ce24351`  |
| 1822   | No file  | `bc5d9ce24351`  |
| 1818   | No file  | `bc5d9ce24351`  |
| 1804   | No file  | `bc5d9ce24351`  |
| 1794   | No file  | `bc5d9ce24351`  |
| 1790   | No file  | `bc5d9ce24351`  |
| 1784   | No file  | `bc5d9ce24351`  |
| 1774   | No file  | `bc5d9ce24351`  |
| 1771   | No file  | `bc5d9ce24351`  |
| 1762   | No file  | `bc5d9ce24351`  |
| 1759   | No file  | `bc5d9ce24351`  |
| 1754   | No file  | `bc5d9ce24351`  |
| 1749   | No file  | `bc5d9ce24351`  |
| 1743   | No file  | `bc5d9ce24351`  |
| 1737   | No file  | `bc5d9ce24351`  |
| 1731   | No file  | `bc5d9ce24351`  |
| 1725   | No file  | `bc5d9ce24351`  |
| 1717   | No file  | `bc5d9ce24351`  |
| 1710   | No file  | `bc5d9ce24351`  |
| 1704   | No file  | `bc5d9ce24351`  |
| 1698   | No file  | `bc5d9ce24351`  |
| 1690   | No file  | `bc5d9ce24351`  |
| 1685   | No file  | `bc5d9ce24351`  |
| 1680   | No file  | `bc5d9ce24351`  |
| 1674   | No file  | `bc5d9ce24351`  |
| 1668   | No file  | `bc5d9ce24351`  |
| 1659   | No file  | `bc5d9ce24351`  |
| 1649   | No file  | `bc5d9ce24351`  |
| 1642   | No file  | `bc5d9ce24351`  |
| 1636   | No file  | `bc5d9ce24351`  |
| 1628   | No file  | `bc5d9ce24351`  |
| 1622   | No file  | `bc5d9ce24351`  |
| 1614   | No file  | `bc5d9ce24351`  |
| 1608   | No file  | `bc5d9ce24351`  |
| 1602   | No file  | `bc5d9ce24351`  |
| 1598   | No file  | `bc5d9ce24351`  |
| 1594   | No file  | `bc5d9ce24351`  |
| 1590   | No file  | `bc5d9ce24351`  |
| 1587   | No file  | `bc5d9ce24351`  |
| 1584   | No file  | `bc5d9ce24351`  |
| 1579   | No file  | `bc5d9ce24351`  |
| 1572   | No file  | `bc5d9ce24351`  |
| 1565   | No file  | `bc5d9ce24351`  |
| 1559   | No file  | `bc5d9ce24351`  |
| 1554   | No file  | `bc5d9ce24351`  |
| 1547   | No file  | `bc5d9ce24351`  |
| 1537   | No file  | `bc5d9ce24351`  |
| 1529   | No file  | `bc5d9ce24351`  |
| 1524   | No file  | `bc5d9ce24351`  |
| 1519   | No file  | `bc5d9ce24351`  |
| 1509   | No file  | `bc5d9ce24351`  |
| 1506   | No file  | `bc5d9ce24351`  |
| 1504   | No file  | `bc5d9ce24351`  |
| 1500   | No file  | `bc5d9ce24351`  |
| 1493   | No file  | `bc5d9ce24351`  |
| 1489   | No file  | `bc5d9ce24351`  |
| 1485   | No file  | `bc5d9ce24351`  |
| 1481   | No file  | `bc5d9ce24351`  |
| 1474   | No file  | `bc5d9ce24351`  |
| 1466   | No file  | `bc5d9ce24351`  |
| 1462   | No file  | `bc5d9ce24351`  |
| 1459   | No file  | `bc5d9ce24351`  |
| 1453   | No file  | `bc5d9ce24351`  |
| 1450   | No file  | `bc5d9ce24351`  |
| 1445   | No file  | `bc5d9ce24351`  |
| 1439   | No file  | `bc5d9ce24351`  |
| 1433   | No file  | `bc5d9ce24351`  |
| 1430   | No file  | `bc5d9ce24351`  |
| 1426   | No file  | `bc5d9ce24351`  |
| 1421   | No file  | `bc5d9ce24351`  |
| 1417   | No file  | `bc5d9ce24351`  |
| 1416   | No file  | `bc5d9ce24351`  |
| 1409   | No file  | `bc5d9ce24351`  |
| 1405   | No file  | `bc5d9ce24351`  |
| 1401   | No file  | `bc5d9ce24351`  |
| 1396   | No file  | `bc5d9ce24351`  |
| 1391   | No file  | `bc5d9ce24351`  |
| 1390   | No file  | `bc5d9ce24351`  |
| 1386   | No file  | `bc5d9ce24351`  |
| 1381   | No file  | `bc5d9ce24351`  |
| 1379   | No file  | `bc5d9ce24351`  |
| 1372   | No file  | `bc5d9ce24351`  |
| 1366   | No file  | `bc5d9ce24351`  |
| 1364   | No file  | `bc5d9ce24351`  |
| 1363   | No file  | `bc5d9ce24351`  |
| 1360   | No file  | `bc5d9ce24351`  |
| 1358   | No file  | `bc5d9ce24351`  |
| 1355   | No file  | `bc5d9ce24351`  |
| 1351   | No file  | `bc5d9ce24351`  |
| 1348   | No file  | `bc5d9ce24351`  |
| 1346   | No file  | `bc5d9ce24351`  |
| 1341   | No file  | `bc5d9ce24351`  |
| 1340   | No file  | `bc5d9ce24351`  |
| 1338   | No file  | `bc5d9ce24351`  |
| 1335   | No file  | `bc5d9ce24351`  |
| 1333   | No file  | `bc5d9ce24351`  |
| 1329   | No file  | `bc5d9ce24351`  |
| 1327   | No file  | `bc5d9ce24351`  |
| 1324   | No file  | `bc5d9ce24351`  |
| 1321   | No file  | `bc5d9ce24351`  |
| 1319   | No file  | `bc5d9ce24351`  |
| 1318   | No file  | `bc5d9ce24351`  |
| 1316   | No file  | `bc5d9ce24351`  |
| 1313   | No file  | `bc5d9ce24351`  |
| 1311   | No file  | `bc5d9ce24351`  |
| 1309   | No file  | `bc5d9ce24351`  |
| 1304   | No file  | `bc5d9ce24351`  |
| 1292   | No file  | `bc5d9ce24351`  |
| 1286   | No file  | `bc5d9ce24351`  |
| 1280   | No file  | `bc5d9ce24351`  |
| 1276   | No file  | `bc5d9ce24351`  |
| 1267   | No file  | `bc5d9ce24351`  |
| 1261   | No file  | `bc5d9ce24351`  |
| 1256   | No file  | `bc5d9ce24351`  |
| 1250   | No file  | `bc5d9ce24351`  |
| 1246   | No file  | `bc5d9ce24351`  |
| 1239   | No file  | `bc5d9ce24351`  |
| 1230   | No file  | `bc5d9ce24351`  |
| 1226   | No file  | `bc5d9ce24351`  |
| 1220   | No file  | `bc5d9ce24351`  |
| 1217   | No file  | `bc5d9ce24351`  |
| 1211   | No file  | `bc5d9ce24351`  |
| 1210   | No file  | `bc5d9ce24351`  |
| 1208   | No file  | `bc5d9ce24351`  |
| 1203   | No file  | `bc5d9ce24351`  |
| 1197   | No file  | `bc5d9ce24351`  |
| 1194   | No file  | `bc5d9ce24351`  |
| 1192   | No file  | `bc5d9ce24351`  |
| 1187   | No file  | `bc5d9ce24351`  |
| 1183   | No file  | `bc5d9ce24351`  |
| 1177   | No file  | `bc5d9ce24351`  |
| 1173   | No file  | `bc5d9ce24351`  |
| 1167   | No file  | `bc5d9ce24351`  |
| 1164   | No file  | `bc5d9ce24351`  |
| 1156   | No file  | `bc5d9ce24351`  |
| 1149   | No file  | `bc5d9ce24351`  |
| 1144   | No file  | `bc5d9ce24351`  |
| 1137   | No file  | `bc5d9ce24351`  |
| 1132   | No file  | `bc5d9ce24351`  |
| 1127   | No file  | `bc5d9ce24351`  |
| 1122   | No file  | `bc5d9ce24351`  |
| 1118   | No file  | `bc5d9ce24351`  |
| 1114   | No file  | `bc5d9ce24351`  |
| 1109   | No file  | `bc5d9ce24351`  |
| 1102   | No file  | `bc5d9ce24351`  |
| 1096   | No file  | `bc5d9ce24351`  |
| 1088   | No file  | `bc5d9ce24351`  |
| 1081   | No file  | `bc5d9ce24351`  |
| 1076   | No file  | `bc5d9ce24351`  |
| 1069   | No file  | `bc5d9ce24351`  |
| 1064   | No file  | `bc5d9ce24351`  |
| 1058   | No file  | `bc5d9ce24351`  |
| 1051   | No file  | `bc5d9ce24351`  |
| 1044   | No file  | `bc5d9ce24351`  |
| 1036   | No file  | `bc5d9ce24351`  |
| 1026   | No file  | `bc5d9ce24351`  |
| 1016   | No file  | `bc5d9ce24351`  |
| 1009   | No file  | `bc5d9ce24351`  |
| 1005   | No file  | `bc5d9ce24351`  |
| 1000   | No file  | `bc5d9ce24351`  |
| 998    | No file  | `bc5d9ce24351`  |
| 990    | No file  | `bc5d9ce24351`  |
| 979    | No file  | `bc5d9ce24351`  |
| 972    | No file  | `bc5d9ce24351`  |
| 963    | No file  | `bc5d9ce24351`  |
| 955    | No file  | `bc5d9ce24351`  |
| 946    | No file  | `bc5d9ce24351`  |
| 938    | No file  | `bc5d9ce24351`  |
| 927    | No file  | `bc5d9ce24351`  |
| 911    | No file  | `bc5d9ce24351`  |
| 904    | No file  | `bc5d9ce24351`  |
| 899    | No file  | `bc5d9ce24351`  |
| 894    | No file  | `bc5d9ce24351`  |
| 885    | No file  | `bc5d9ce24351`  |
| 879    | No file  | `bc5d9ce24351`  |
| 872    | No file  | `bc5d9ce24351`  |
| 864    | No file  | `bc5d9ce24351`  |
| 855    | No file  | `bc5d9ce24351`  |
| 853    | No file  | `bc5d9ce24351`  |
| 845    | No file  | `bc5d9ce24351`  |
| 837    | No file  | `bc5d9ce24351`  |
| 829    | No file  | `bc5d9ce24351`  |
| 822    | No file  | `bc5d9ce24351`  |
| 814    | No file  | `bc5d9ce24351`  |
| 805    | No file  | `bc5d9ce24351`  |
| 794    | No file  | `bc5d9ce24351`  |
| 787    | No file  | `bc5d9ce24351`  |
| 780    | No file  | `bc5d9ce24351`  |
| 771    | No file  | `bc5d9ce24351`  |
| 760    | No file  | `bc5d9ce24351`  |
| 748    | No file  | `bc5d9ce24351`  |
| 741    | No file  | `bc5d9ce24351`  |
| 736    | No file  | `bc5d9ce24351`  |
| 731    | No file  | `bc5d9ce24351`  |
| 723    | No file  | `bc5d9ce24351`  |
| 711    | No file  | `bc5d9ce24351`  |
| 707    | No file  | `bc5d9ce24351`  |
| 697    | No file  | `bc5d9ce24351`  |
| 689    | No file  | `bc5d9ce24351`  |
| 683    | No file  | `bc5d9ce24351`  |
| 678    | No file  | `bc5d9ce24351`  |
| 670    | No file  | `bc5d9ce24351`  |
| 661    | No file  | `bc5d9ce24351`  |
| 656    | No file  | `bc5d9ce24351`  |
| 652    | No file  | `bc5d9ce24351`  |
| 643    | No file  | `bc5d9ce24351`  |
| 637    | No file  | `bc5d9ce24351`  |
| 630    | No file  | `bc5d9ce24351`  |
| 627    | No file  | `bc5d9ce24351`  |
| 621    | No file  | `bc5d9ce24351`  |
| 617    | No file  | `bc5d9ce24351`  |
| 615    | No file  | `bc5d9ce24351`  |
| 606    | No file  | `bc5d9ce24351`  |
| 599    | No file  | `bc5d9ce24351`  |
| 592    | No file  | `bc5d9ce24351`  |
| 586    | No file  | `bc5d9ce24351`  |
| 577    | No file  | `bc5d9ce24351`  |
| 569    | No file  | `bc5d9ce24351`  |
| 561    | No file  | `bc5d9ce24351`  |
| 554    | No file  | `bc5d9ce24351`  |
| 542    | No file  | `bc5d9ce24351`  |
| 532    | No file  | `bc5d9ce24351`  |
| 531    | No file  | `bc5d9ce24351`  |
| 526    | No file  | `bc5d9ce24351`  |
| 521    | No file  | `bc5d9ce24351`  |
| 517    | No file  | `bc5d9ce24351`  |
| 510    | No file  | `bc5d9ce24351`  |
| 508    | No file  | `bc5d9ce24351`  |
| 504    | No file  | `bc5d9ce24351`  |
| 497    | No file  | `bc5d9ce24351`  |
| 491    | No file  | `bc5d9ce24351`  |
| 485    | No file  | `bc5d9ce24351`  |
| 478    | No file  | `bc5d9ce24351`  |
| 472    | No file  | `bc5d9ce24351`  |
| 466    | No file  | `bc5d9ce24351`  |
| 457    | No file  | `bc5d9ce24351`  |
| 452    | No file  | `bc5d9ce24351`  |
| 449    | No file  | `bc5d9ce24351`  |
| 435    | No file  | `bc5d9ce24351`  |

<!-- versions:end -->

## Companion Files

None. Each quest key is a quest cell of
[`uigrowthpasslayout.bss`](uigrowthpasslayout_bss.md), whose view loads this
file for its Links column.

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with variable records and the counted string table of
`regionmapinfo.bss` (`_common/pabr_strings.py`).

| Offset              | Type                 | Field              | Notes                                                        |
| ------------------- | -------------------- | ------------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]              | magic              | `PABR` (ASCII)                                               |
| `+0x04`             | u32                  | record_count       | Number of quests; `37` on client 3482                        |
| `+0x08`             | Record[record_count] | records            | See Record; in sheet row order, which is not always sorted   |
| `records+0x00`      | String Table         | string_table       | See String Table                                             |
| `string_table+0x00` | u32                  | string_table_start | Absolute offset of `string_count`, where the records end     |
| `string_table+0x04` | u32                  | zero               | Always `0`                                                   |

The parser rejects a file whose records do not end at `string_table_start`.

### Record (variable: 8 bytes + entries)

| Offset  | Type                | Field          | Notes |
| ------- | ------------------- | -------------- | ----- |
| `+0x00` | u16                 | quest_chain_id | `getQuestGroup()` of the quest cell; the sheet's `QuestGroup` modulo 65,536 (sheet `70006` is `4470`) |
| `+0x02` | u16                 | quest_id       | `getQuestId()` of the quest cell                          |
| `+0x04` | u32                 | entry_count    | `4` on 36 records and `1` on quest 4472 / 1 (client 3482); `1`, `2` or `4` on client 3251 |
| `+0x08` | Entry[entry_count]  | entries        | See Entry; one per service resource type, none repeated   |

### Entry (variable: 5 bytes + links)

| Offset  | Type             | Field                 | Notes |
| ------- | ---------------- | --------------------- | ----- |
| `+0x00` | u8               | service_resource_type | `CppEnums.ServiceResourceType`, see [Service Resource Types](#service-resource-types) |
| `+0x01` | u32              | link_count            | The value `getNoteLinkSize()` returns; the Lua shows up to three buttons; `1` on every entry of every client read |
| `+0x05` | Link[link_count] | links                 | See Link; button `idx` 0 to 2 in order |

### Link (8 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u32  | link_ref   | String-table index of the web address (`https://www.naeu.playblackdesert.com/en-US/Wiki?wikiNo=25`) |
| `+0x04` | u32  | author_ref | String-table index of the author name (`모험가 노트`, `GM Note`) |

The parser stores the two strings under `link` and `author`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `30` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | Indexed from `0`, each text once, in the order the links first use them; the addresses are UTF-8 (`is_wide` 0), the author names UTF-16LE (`1`) |

## Service Resource Types

`service_resource_type` holds a `CppEnums.ServiceResourceType` value from
`global_define_cpp_enum.luac`; `getGameServiceResType()` returns the one of
the running client, and only that type's entry is shown. The NA/EU client
holds four:

| Value | Lua name                   | Links on client 3482 |
| ----- | -------------------------- | -------------------- |
| `2`   | `eServiceResourceType_EN`  | 37 quests            |
| `6`   | `eServiceResourceType_FR`  | 36 quests            |
| `7`   | `eServiceResourceType_DE`  | 36 quests            |
| `18`  | `eServiceResourceType_SP`  | 36 quests            |

The other members are `Dev` (0), `KR` (1), `JP` (3), `CN` (4), `RU` (5),
`ES` (8), `TW` (9), `SA` (10), `PT` (11), `TH` (12), `ID` (13) and `TR`
(14).

## Field Names

The record is the `GrowthPass_Link` sheet of a private server's
`DataSheets.bexcel` on client 1784 (288 rows; columns
`PA_GAME_SERVICE_TYPE`, `PA_SERVICE_RESOURCE_TYPE`, `QuestGroup`, `QuestID`,
then `AdventurerNotesLink1` / `AdventurerNotesAuthor1` to
`AdventurerNotesLink3` / `AdventurerNotesAuthor3`). The client 1784 test
client has no `growthpasslinkdata.bss`; clients 2107 to 3251 hold one file,
byte for byte the same, built from the sheet's 51 rows with `PA_GAME_SERVICE_TYPE` `12`. Over
those rows, keyed by `QuestGroup` modulo 65,536, `QuestID` and
`PA_SERVICE_RESOURCE_TYPE`:

| Field                   | Sheet column                     | Match (client 2107) |
| ----------------------- | -------------------------------- | ------------------- |
| `quest_chain_id`        | `QuestGroup`                     | 51 of 51 entries    |
| `quest_id`              | `QuestID`                        | 51 of 51            |
| `service_resource_type` | `PA_SERVICE_RESOURCE_TYPE`       | 51 of 51            |
| `link_count`            | filled `AdventurerNotesLink*` columns | 51 of 51 (`1`) |
| `link`                  | `AdventurerNotesLink1`           | 51 of 51            |
| `author`                | `AdventurerNotesAuthor1`         | 51 of 51            |

The file groups the sheet rows by quest in sheet order: quest 4469 / 14
comes before 4469 / 12 on client 3251, as in the sheet. `PA_GAME_SERVICE_TYPE`
(the service region) is not in the file; each region's client gets its own
rows.

## Notes

- Decompressed size on client 3482: `3,992` bytes; the records end at
  `0x88D`, the offset in the trailer. Every link of quest chain 4470 points
  at a `naeu.playblackdesert.com` Wiki page by `모험가 노트` (Adventurer
  Notes), the same address for all four service types; quest 4472 / 1 has
  one English link to a `News/Detail` page by `GM Note`.
- Clients 2107 to 3251 link to `InGame/AdventurerNotes/CommunityDetail`
  pages written by players, often for one service type only (25 quests, 43
  strings).
- `isGameTypeCH()` clients open the link with `ToClient_OpenRailBrowser`, the
  others in the Adventurer's Guide web window
  (`PaGlobal_ExpirienceWiki_All_SetDirectLink`).

## Open Questions

### Links After the First

Every entry of every client read holds one link, so the order of the pairs
for a `link_count` of 2 or 3 is unconfirmed. The sheet's columns pair each
`AdventurerNotesLink<n>` with its `AdventurerNotesAuthor<n>`, and one Korean
row (`70000` / 28) fills all three, so the layout above reads them as
`link_count` (link, author) pairs; a client whose file has such a row would
confirm it.
