# `photomodestaticstatus.bss` Format

## Purpose

The weather presets of the photo mode window, in the order its weather
picker shows them: per preset a u32 and the GAME sheet key of the preset's
name (`LUA_PHOTOMODE_WEATHER_DEFAULT` to `LUA_PHOTOMODE_WEATHER_LOCALWAR`).
`panel_widget_photomode_main_all_1.luac` (client 3482) has 15 weather
images (`_weatherRecommend = 15`), and the client calls
`FromClient_SetPhotoModeWeatherPresetIndex(weatherPresetIndex, weatherName)`
with the preset's position and its name key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | ------- | --------- |
| 1      | 1933 and later | 3483    | `photomodestaticstatus.bss` | 691   | 15 Row  | 8         |

| Layout | File                        | Known         | Unknown     |
| ------ | --------------------------- | ------------- | ----------- |
| 1      | `photomodestaticstatus.bss` | 631 B (91.3%) | 60 B (8.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6e9d2edeb5d7`  |
| 3482   | Layout 1 | `6e9d2edeb5d7`  |
| 3474   | Layout 1 | `6e9d2edeb5d7`  |
| 3473   | Layout 1 | `6e9d2edeb5d7`  |
| 3464   | Layout 1 | `6e9d2edeb5d7`  |
| 3458   | Layout 1 | `6e9d2edeb5d7`  |
| 3454   | Layout 1 | `6e9d2edeb5d7`  |
| 3444   | Layout 1 | `6e9d2edeb5d7`  |
| 3435   | Layout 1 | `6e9d2edeb5d7`  |
| 3426   | Layout 1 | `6e9d2edeb5d7`  |
| 3418   | Layout 1 | `6e9d2edeb5d7`  |
| 3412   | Layout 1 | `6e9d2edeb5d7`  |
| 3402   | Layout 1 | `6e9d2edeb5d7`  |
| 3396   | Layout 1 | `6e9d2edeb5d7`  |
| 3387   | Layout 1 | `6e9d2edeb5d7`  |
| 3381   | Layout 1 | `6e9d2edeb5d7`  |
| 3373   | Layout 1 | `6e9d2edeb5d7`  |
| 3364   | Layout 1 | `6e9d2edeb5d7`  |
| 3356   | Layout 1 | `6e9d2edeb5d7`  |
| 3349   | Layout 1 | `6e9d2edeb5d7`  |
| 3342   | Layout 1 | `6e9d2edeb5d7`  |
| 3335   | Layout 1 | `6e9d2edeb5d7`  |
| 3326   | Layout 1 | `6e9d2edeb5d7`  |
| 3321   | Layout 1 | `6e9d2edeb5d7`  |
| 3314   | Layout 1 | `6e9d2edeb5d7`  |
| 3303   | Layout 1 | `6e9d2edeb5d7`  |
| 3302   | Layout 1 | `6e9d2edeb5d7`  |
| 3293   | Layout 1 | `6e9d2edeb5d7`  |
| 3283   | Layout 1 | `6e9d2edeb5d7`  |
| 3275   | Layout 1 | `6e9d2edeb5d7`  |
| 3267   | Layout 1 | `6e9d2edeb5d7`  |
| 3258   | Layout 1 | `6e9d2edeb5d7`  |
| 3251   | Layout 1 | `6e9d2edeb5d7`  |
| 3242   | Layout 1 | `6e9d2edeb5d7`  |
| 3235   | Layout 1 | `6e9d2edeb5d7`  |
| 3229   | Layout 1 | `6e9d2edeb5d7`  |
| 3212   | Layout 1 | `6e9d2edeb5d7`  |
| 3203   | Layout 1 | `6e9d2edeb5d7`  |
| 3193   | Layout 1 | `6e9d2edeb5d7`  |
| 3186   | Layout 1 | `6e9d2edeb5d7`  |
| 3177   | Layout 1 | `6e9d2edeb5d7`  |
| 3169   | Layout 1 | `6e9d2edeb5d7`  |
| 3158   | Layout 1 | `6e9d2edeb5d7`  |
| 3151   | Layout 1 | `6e9d2edeb5d7`  |
| 3144   | Layout 1 | `6e9d2edeb5d7`  |
| 3133   | Layout 1 | `6e9d2edeb5d7`  |
| 3125   | Layout 1 | `6e9d2edeb5d7`  |
| 3118   | Layout 1 | `6e9d2edeb5d7`  |
| 3111   | Layout 1 | `6e9d2edeb5d7`  |
| 3103   | Layout 1 | `6e9d2edeb5d7`  |
| 3095   | Layout 1 | `6e9d2edeb5d7`  |
| 3086   | Layout 1 | `6e9d2edeb5d7`  |
| 3072   | Layout 1 | `6e9d2edeb5d7`  |
| 3062   | Layout 1 | `6e9d2edeb5d7`  |
| 3052   | Layout 1 | `6e9d2edeb5d7`  |
| 3045   | Layout 1 | `6e9d2edeb5d7`  |
| 3037   | Layout 1 | `6e9d2edeb5d7`  |
| 3030   | Layout 1 | `6e9d2edeb5d7`  |
| 3021   | Layout 1 | `6e9d2edeb5d7`  |
| 3012   | Layout 1 | `6e9d2edeb5d7`  |
| 3002   | Layout 1 | `6e9d2edeb5d7`  |
| 2995   | Layout 1 | `6e9d2edeb5d7`  |
| 2987   | Layout 1 | `6e9d2edeb5d7`  |
| 2978   | Layout 1 | `6e9d2edeb5d7`  |
| 2970   | Layout 1 | `6e9d2edeb5d7`  |
| 2959   | Layout 1 | `6e9d2edeb5d7`  |
| 2951   | Layout 1 | `6e9d2edeb5d7`  |
| 2942   | Layout 1 | `6e9d2edeb5d7`  |
| 2935   | Layout 1 | `6e9d2edeb5d7`  |
| 2932   | Layout 1 | `6e9d2edeb5d7`  |
| 2923   | Layout 1 | `6e9d2edeb5d7`  |
| 2919   | Layout 1 | `6e9d2edeb5d7`  |
| 2907   | Layout 1 | `6e9d2edeb5d7`  |
| 2900   | Layout 1 | `6e9d2edeb5d7`  |
| 2891   | Layout 1 | `6e9d2edeb5d7`  |
| 2882   | Layout 1 | `6e9d2edeb5d7`  |
| 2872   | Layout 1 | `6e9d2edeb5d7`  |
| 2863   | Layout 1 | `6e9d2edeb5d7`  |
| 2855   | Layout 1 | `6e9d2edeb5d7`  |
| 2849   | Layout 1 | `6e9d2edeb5d7`  |
| 2844   | Layout 1 | `6e9d2edeb5d7`  |
| 2834   | Layout 1 | `6e9d2edeb5d7`  |
| 2825   | Layout 1 | `6e9d2edeb5d7`  |
| 2819   | Layout 1 | `6e9d2edeb5d7`  |
| 2811   | Layout 1 | `6e9d2edeb5d7`  |
| 2803   | Layout 1 | `6e9d2edeb5d7`  |
| 2794   | Layout 1 | `6e9d2edeb5d7`  |
| 2783   | Layout 1 | `6e9d2edeb5d7`  |
| 2774   | Layout 1 | `6e9d2edeb5d7`  |
| 2765   | Layout 1 | `6e9d2edeb5d7`  |
| 2756   | Layout 1 | `6e9d2edeb5d7`  |
| 2750   | Layout 1 | `6e9d2edeb5d7`  |
| 2743   | Layout 1 | `6e9d2edeb5d7`  |
| 2736   | Layout 1 | `6e9d2edeb5d7`  |
| 2726   | Layout 1 | `6e9d2edeb5d7`  |
| 2717   | Layout 1 | `6e9d2edeb5d7`  |
| 2709   | Layout 1 | `6e9d2edeb5d7`  |
| 2703   | Layout 1 | `6e9d2edeb5d7`  |
| 2695   | Layout 1 | `6e9d2edeb5d7`  |
| 2684   | Layout 1 | `6e9d2edeb5d7`  |
| 2672   | Layout 1 | `6e9d2edeb5d7`  |
| 2665   | Layout 1 | `6e9d2edeb5d7`  |
| 2657   | Layout 1 | `6e9d2edeb5d7`  |
| 2649   | Layout 1 | `6e9d2edeb5d7`  |
| 2644   | Layout 1 | `6e9d2edeb5d7`  |
| 2637   | Layout 1 | `6e9d2edeb5d7`  |
| 2629   | Layout 1 | `6e9d2edeb5d7`  |
| 2619   | Layout 1 | `6e9d2edeb5d7`  |
| 2612   | Layout 1 | `6e9d2edeb5d7`  |
| 2606   | Layout 1 | `6e9d2edeb5d7`  |
| 2602   | Layout 1 | `6e9d2edeb5d7`  |
| 2601   | Layout 1 | `6e9d2edeb5d7`  |
| 2592   | Layout 1 | `6e9d2edeb5d7`  |
| 2583   | Layout 1 | `6e9d2edeb5d7`  |
| 2575   | Layout 1 | `6e9d2edeb5d7`  |
| 2567   | Layout 1 | `6e9d2edeb5d7`  |
| 2560   | Layout 1 | `6e9d2edeb5d7`  |
| 2553   | Layout 1 | `6e9d2edeb5d7`  |
| 2545   | Layout 1 | `6e9d2edeb5d7`  |
| 2538   | Layout 1 | `6e9d2edeb5d7`  |
| 2529   | Layout 1 | `6e9d2edeb5d7`  |
| 2519   | Layout 1 | `6e9d2edeb5d7`  |
| 2513   | Layout 1 | `6e9d2edeb5d7`  |
| 2510   | Layout 1 | `6e9d2edeb5d7`  |
| 2507   | Layout 1 | `6e9d2edeb5d7`  |
| 2503   | Layout 1 | `6e9d2edeb5d7`  |
| 2498   | Layout 1 | `6e9d2edeb5d7`  |
| 2492   | Layout 1 | `6e9d2edeb5d7`  |
| 2487   | Layout 1 | `6e9d2edeb5d7`  |
| 2480   | Layout 1 | `6e9d2edeb5d7`  |
| 2474   | Layout 1 | `6e9d2edeb5d7`  |
| 2468   | Layout 1 | `6e9d2edeb5d7`  |
| 2460   | Layout 1 | `6e9d2edeb5d7`  |
| 2453   | Layout 1 | `6e9d2edeb5d7`  |
| 2444   | Layout 1 | `6e9d2edeb5d7`  |
| 2438   | Layout 1 | `6e9d2edeb5d7`  |
| 2434   | Layout 1 | `6e9d2edeb5d7`  |
| 2429   | Layout 1 | `6e9d2edeb5d7`  |
| 2421   | Layout 1 | `6e9d2edeb5d7`  |
| 2414   | Layout 1 | `6e9d2edeb5d7`  |
| 2407   | Layout 1 | `6e9d2edeb5d7`  |
| 2401   | Layout 1 | `6e9d2edeb5d7`  |
| 2397   | Layout 1 | `6e9d2edeb5d7`  |
| 2393   | Layout 1 | `6e9d2edeb5d7`  |
| 2384   | Layout 1 | `6e9d2edeb5d7`  |
| 2378   | Layout 1 | `6e9d2edeb5d7`  |
| 2372   | Layout 1 | `6e9d2edeb5d7`  |
| 2358   | Layout 1 | `6e9d2edeb5d7`  |
| 2352   | Layout 1 | `6e9d2edeb5d7`  |
| 2347   | Layout 1 | `6e9d2edeb5d7`  |
| 2343   | Layout 1 | `6e9d2edeb5d7`  |
| 2335   | Layout 1 | `6e9d2edeb5d7`  |
| 2327   | Layout 1 | `6e9d2edeb5d7`  |
| 2324   | Layout 1 | `6e9d2edeb5d7`  |
| 2319   | Layout 1 | `6e9d2edeb5d7`  |
| 2313   | Layout 1 | `6e9d2edeb5d7`  |
| 2308   | Layout 1 | `6e9d2edeb5d7`  |
| 2302   | Layout 1 | `6e9d2edeb5d7`  |
| 2295   | Layout 1 | `6e9d2edeb5d7`  |
| 2290   | Layout 1 | `6e9d2edeb5d7`  |
| 2284   | Layout 1 | `6e9d2edeb5d7`  |
| 2276   | Layout 1 | `6e9d2edeb5d7`  |
| 2269   | Layout 1 | `6e9d2edeb5d7`  |
| 2259   | Layout 1 | `6e9d2edeb5d7`  |
| 2250   | Layout 1 | `6e9d2edeb5d7`  |
| 2243   | Layout 1 | `6e9d2edeb5d7`  |
| 2235   | Layout 1 | `6e9d2edeb5d7`  |
| 2229   | Layout 1 | `6e9d2edeb5d7`  |
| 2224   | Layout 1 | `6e9d2edeb5d7`  |
| 2218   | Layout 1 | `6e9d2edeb5d7`  |
| 2215   | Layout 1 | `6e9d2edeb5d7`  |
| 2207   | Layout 1 | `6e9d2edeb5d7`  |
| 2203   | Layout 1 | `6e9d2edeb5d7`  |
| 2196   | Layout 1 | `6e9d2edeb5d7`  |
| 2192   | Layout 1 | `6e9d2edeb5d7`  |
| 2189   | Layout 1 | `6e9d2edeb5d7`  |
| 2183   | Layout 1 | `6e9d2edeb5d7`  |
| 2179   | Layout 1 | `6e9d2edeb5d7`  |
| 2171   | Layout 1 | `6e9d2edeb5d7`  |
| 2163   | Layout 1 | `6e9d2edeb5d7`  |
| 2156   | Layout 1 | `6e9d2edeb5d7`  |
| 2151   | Layout 1 | `6e9d2edeb5d7`  |
| 2147   | Layout 1 | `6e9d2edeb5d7`  |
| 2142   | Layout 1 | `6e9d2edeb5d7`  |
| 2138   | Layout 1 | `6e9d2edeb5d7`  |
| 2134   | Layout 1 | `6e9d2edeb5d7`  |
| 2130   | Layout 1 | `6e9d2edeb5d7`  |
| 2122   | Layout 1 | `6e9d2edeb5d7`  |
| 2107   | Layout 1 | `6e9d2edeb5d7`  |
| 2098   | Layout 1 | `6e9d2edeb5d7`  |
| 2089   | Layout 1 | `6e9d2edeb5d7`  |
| 2081   | Layout 1 | `6e9d2edeb5d7`  |
| 2073   | Layout 1 | `6e9d2edeb5d7`  |
| 2067   | Layout 1 | `6e9d2edeb5d7`  |
| 2063   | Layout 1 | `6e9d2edeb5d7`  |
| 2059   | Layout 1 | `6e9d2edeb5d7`  |
| 2052   | Layout 1 | `6e9d2edeb5d7`  |
| 2044   | Layout 1 | `6e9d2edeb5d7`  |
| 2039   | Layout 1 | `6e9d2edeb5d7`  |
| 2032   | Layout 1 | `6e9d2edeb5d7`  |
| 2025   | Layout 1 | `6e9d2edeb5d7`  |
| 2011   | Layout 1 | `6e9d2edeb5d7`  |
| 2005   | Layout 1 | `6e9d2edeb5d7`  |
| 2000   | Layout 1 | `6e9d2edeb5d7`  |
| 1996   | Layout 1 | `6e9d2edeb5d7`  |
| 1991   | Layout 1 | `6e9d2edeb5d7`  |
| 1985   | Layout 1 | `6e9d2edeb5d7`  |
| 1980   | Layout 1 | `6e9d2edeb5d7`  |
| 1969   | Layout 1 | `6e9d2edeb5d7`  |
| 1964   | Layout 1 | `6e9d2edeb5d7`  |
| 1958   | Layout 1 | `6e9d2edeb5d7`  |
| 1950   | Layout 1 | `6e9d2edeb5d7`  |
| 1945   | Layout 1 | `6e9d2edeb5d7`  |
| 1937   | Layout 1 | `6e9d2edeb5d7`  |
| 1933   | Layout 1 | `6e9d2edeb5d7`  |
| 1927   | No file  | `6e9d2edeb5d7`  |
| 1921   | No file  | `6e9d2edeb5d7`  |
| 1914   | No file  | `6e9d2edeb5d7`  |
| 1908   | No file  | `6e9d2edeb5d7`  |
| 1897   | No file  | `6e9d2edeb5d7`  |
| 1892   | No file  | `6e9d2edeb5d7`  |
| 1886   | No file  | `6e9d2edeb5d7`  |
| 1881   | No file  | `6e9d2edeb5d7`  |
| 1871   | No file  | `6e9d2edeb5d7`  |
| 1866   | No file  | `6e9d2edeb5d7`  |
| 1862   | No file  | `6e9d2edeb5d7`  |
| 1854   | No file  | `6e9d2edeb5d7`  |
| 1846   | No file  | `6e9d2edeb5d7`  |
| 1838   | No file  | `6e9d2edeb5d7`  |
| 1832   | No file  | `6e9d2edeb5d7`  |
| 1826   | No file  | `6e9d2edeb5d7`  |
| 1822   | No file  | `6e9d2edeb5d7`  |
| 1818   | No file  | `6e9d2edeb5d7`  |
| 1804   | No file  | `6e9d2edeb5d7`  |
| 1794   | No file  | `6e9d2edeb5d7`  |
| 1790   | No file  | `6e9d2edeb5d7`  |
| 1784   | No file  | `6e9d2edeb5d7`  |
| 1774   | No file  | `6e9d2edeb5d7`  |
| 1771   | No file  | `6e9d2edeb5d7`  |
| 1762   | No file  | `6e9d2edeb5d7`  |
| 1759   | No file  | `6e9d2edeb5d7`  |
| 1754   | No file  | `6e9d2edeb5d7`  |
| 1749   | No file  | `6e9d2edeb5d7`  |
| 1743   | No file  | `6e9d2edeb5d7`  |
| 1737   | No file  | `6e9d2edeb5d7`  |
| 1731   | No file  | `6e9d2edeb5d7`  |
| 1725   | No file  | `6e9d2edeb5d7`  |
| 1717   | No file  | `6e9d2edeb5d7`  |
| 1710   | No file  | `6e9d2edeb5d7`  |
| 1704   | No file  | `6e9d2edeb5d7`  |
| 1698   | No file  | `6e9d2edeb5d7`  |
| 1690   | No file  | `6e9d2edeb5d7`  |
| 1685   | No file  | `6e9d2edeb5d7`  |
| 1680   | No file  | `6e9d2edeb5d7`  |
| 1674   | No file  | `6e9d2edeb5d7`  |
| 1668   | No file  | `6e9d2edeb5d7`  |
| 1659   | No file  | `6e9d2edeb5d7`  |
| 1649   | No file  | `6e9d2edeb5d7`  |
| 1642   | No file  | `6e9d2edeb5d7`  |
| 1636   | No file  | `6e9d2edeb5d7`  |
| 1628   | No file  | `6e9d2edeb5d7`  |
| 1622   | No file  | `6e9d2edeb5d7`  |
| 1614   | No file  | `6e9d2edeb5d7`  |
| 1608   | No file  | `6e9d2edeb5d7`  |
| 1602   | No file  | `6e9d2edeb5d7`  |
| 1598   | No file  | `6e9d2edeb5d7`  |
| 1594   | No file  | `6e9d2edeb5d7`  |
| 1590   | No file  | `6e9d2edeb5d7`  |
| 1587   | No file  | `6e9d2edeb5d7`  |
| 1584   | No file  | `6e9d2edeb5d7`  |
| 1579   | No file  | `6e9d2edeb5d7`  |
| 1572   | No file  | `6e9d2edeb5d7`  |
| 1565   | No file  | `6e9d2edeb5d7`  |
| 1559   | No file  | `6e9d2edeb5d7`  |
| 1554   | No file  | `6e9d2edeb5d7`  |
| 1547   | No file  | `6e9d2edeb5d7`  |
| 1537   | No file  | `6e9d2edeb5d7`  |
| 1529   | No file  | `6e9d2edeb5d7`  |
| 1524   | No file  | `6e9d2edeb5d7`  |
| 1519   | No file  | `6e9d2edeb5d7`  |
| 1509   | No file  | `6e9d2edeb5d7`  |
| 1506   | No file  | `6e9d2edeb5d7`  |
| 1504   | No file  | `6e9d2edeb5d7`  |
| 1500   | No file  | `6e9d2edeb5d7`  |
| 1493   | No file  | `6e9d2edeb5d7`  |
| 1489   | No file  | `6e9d2edeb5d7`  |
| 1485   | No file  | `6e9d2edeb5d7`  |
| 1481   | No file  | `6e9d2edeb5d7`  |
| 1474   | No file  | `6e9d2edeb5d7`  |
| 1466   | No file  | `6e9d2edeb5d7`  |
| 1462   | No file  | `6e9d2edeb5d7`  |
| 1459   | No file  | `6e9d2edeb5d7`  |
| 1453   | No file  | `6e9d2edeb5d7`  |
| 1450   | No file  | `6e9d2edeb5d7`  |
| 1445   | No file  | `6e9d2edeb5d7`  |
| 1439   | No file  | `6e9d2edeb5d7`  |
| 1433   | No file  | `6e9d2edeb5d7`  |
| 1430   | No file  | `6e9d2edeb5d7`  |
| 1426   | No file  | `6e9d2edeb5d7`  |
| 1421   | No file  | `6e9d2edeb5d7`  |
| 1417   | No file  | `6e9d2edeb5d7`  |
| 1416   | No file  | `6e9d2edeb5d7`  |
| 1409   | No file  | `6e9d2edeb5d7`  |
| 1405   | No file  | `6e9d2edeb5d7`  |
| 1401   | No file  | `6e9d2edeb5d7`  |
| 1396   | No file  | `6e9d2edeb5d7`  |
| 1391   | No file  | `6e9d2edeb5d7`  |
| 1390   | No file  | `6e9d2edeb5d7`  |
| 1386   | No file  | `6e9d2edeb5d7`  |
| 1381   | No file  | `6e9d2edeb5d7`  |
| 1379   | No file  | `6e9d2edeb5d7`  |
| 1372   | No file  | `6e9d2edeb5d7`  |
| 1366   | No file  | `6e9d2edeb5d7`  |
| 1364   | No file  | `6e9d2edeb5d7`  |
| 1363   | No file  | `6e9d2edeb5d7`  |
| 1360   | No file  | `6e9d2edeb5d7`  |
| 1358   | No file  | `6e9d2edeb5d7`  |
| 1355   | No file  | `6e9d2edeb5d7`  |
| 1351   | No file  | `6e9d2edeb5d7`  |
| 1348   | No file  | `6e9d2edeb5d7`  |
| 1346   | No file  | `6e9d2edeb5d7`  |
| 1341   | No file  | `6e9d2edeb5d7`  |
| 1340   | No file  | `6e9d2edeb5d7`  |
| 1338   | No file  | `6e9d2edeb5d7`  |
| 1335   | No file  | `6e9d2edeb5d7`  |
| 1333   | No file  | `6e9d2edeb5d7`  |
| 1329   | No file  | `6e9d2edeb5d7`  |
| 1327   | No file  | `6e9d2edeb5d7`  |
| 1324   | No file  | `6e9d2edeb5d7`  |
| 1321   | No file  | `6e9d2edeb5d7`  |
| 1319   | No file  | `6e9d2edeb5d7`  |
| 1318   | No file  | `6e9d2edeb5d7`  |
| 1316   | No file  | `6e9d2edeb5d7`  |
| 1313   | No file  | `6e9d2edeb5d7`  |
| 1311   | No file  | `6e9d2edeb5d7`  |
| 1309   | No file  | `6e9d2edeb5d7`  |
| 1304   | No file  | `6e9d2edeb5d7`  |
| 1292   | No file  | `6e9d2edeb5d7`  |
| 1286   | No file  | `6e9d2edeb5d7`  |
| 1280   | No file  | `6e9d2edeb5d7`  |
| 1276   | No file  | `6e9d2edeb5d7`  |
| 1267   | No file  | `6e9d2edeb5d7`  |
| 1261   | No file  | `6e9d2edeb5d7`  |
| 1256   | No file  | `6e9d2edeb5d7`  |
| 1250   | No file  | `6e9d2edeb5d7`  |
| 1246   | No file  | `6e9d2edeb5d7`  |
| 1239   | No file  | `6e9d2edeb5d7`  |
| 1230   | No file  | `6e9d2edeb5d7`  |
| 1226   | No file  | `6e9d2edeb5d7`  |
| 1220   | No file  | `6e9d2edeb5d7`  |
| 1217   | No file  | `6e9d2edeb5d7`  |
| 1211   | No file  | `6e9d2edeb5d7`  |
| 1210   | No file  | `6e9d2edeb5d7`  |
| 1208   | No file  | `6e9d2edeb5d7`  |
| 1203   | No file  | `6e9d2edeb5d7`  |
| 1197   | No file  | `6e9d2edeb5d7`  |
| 1194   | No file  | `6e9d2edeb5d7`  |
| 1192   | No file  | `6e9d2edeb5d7`  |
| 1187   | No file  | `6e9d2edeb5d7`  |
| 1183   | No file  | `6e9d2edeb5d7`  |
| 1177   | No file  | `6e9d2edeb5d7`  |
| 1173   | No file  | `6e9d2edeb5d7`  |
| 1167   | No file  | `6e9d2edeb5d7`  |
| 1164   | No file  | `6e9d2edeb5d7`  |
| 1156   | No file  | `6e9d2edeb5d7`  |
| 1149   | No file  | `6e9d2edeb5d7`  |
| 1144   | No file  | `6e9d2edeb5d7`  |
| 1137   | No file  | `6e9d2edeb5d7`  |
| 1132   | No file  | `6e9d2edeb5d7`  |
| 1127   | No file  | `6e9d2edeb5d7`  |
| 1122   | No file  | `6e9d2edeb5d7`  |
| 1118   | No file  | `6e9d2edeb5d7`  |
| 1114   | No file  | `6e9d2edeb5d7`  |
| 1109   | No file  | `6e9d2edeb5d7`  |
| 1102   | No file  | `6e9d2edeb5d7`  |
| 1096   | No file  | `6e9d2edeb5d7`  |
| 1088   | No file  | `6e9d2edeb5d7`  |
| 1081   | No file  | `6e9d2edeb5d7`  |
| 1076   | No file  | `6e9d2edeb5d7`  |
| 1069   | No file  | `6e9d2edeb5d7`  |
| 1064   | No file  | `6e9d2edeb5d7`  |
| 1058   | No file  | `6e9d2edeb5d7`  |
| 1051   | No file  | `6e9d2edeb5d7`  |
| 1044   | No file  | `6e9d2edeb5d7`  |
| 1036   | No file  | `6e9d2edeb5d7`  |
| 1026   | No file  | `6e9d2edeb5d7`  |
| 1016   | No file  | `6e9d2edeb5d7`  |
| 1009   | No file  | `6e9d2edeb5d7`  |
| 1005   | No file  | `6e9d2edeb5d7`  |
| 1000   | No file  | `6e9d2edeb5d7`  |
| 998    | No file  | `6e9d2edeb5d7`  |
| 990    | No file  | `6e9d2edeb5d7`  |
| 979    | No file  | `6e9d2edeb5d7`  |
| 972    | No file  | `6e9d2edeb5d7`  |
| 963    | No file  | `6e9d2edeb5d7`  |
| 955    | No file  | `6e9d2edeb5d7`  |
| 946    | No file  | `6e9d2edeb5d7`  |
| 938    | No file  | `6e9d2edeb5d7`  |
| 927    | No file  | `6e9d2edeb5d7`  |
| 911    | No file  | `6e9d2edeb5d7`  |
| 904    | No file  | `6e9d2edeb5d7`  |
| 899    | No file  | `6e9d2edeb5d7`  |
| 894    | No file  | `6e9d2edeb5d7`  |
| 885    | No file  | `6e9d2edeb5d7`  |
| 879    | No file  | `6e9d2edeb5d7`  |
| 872    | No file  | `6e9d2edeb5d7`  |
| 864    | No file  | `6e9d2edeb5d7`  |
| 855    | No file  | `6e9d2edeb5d7`  |
| 853    | No file  | `6e9d2edeb5d7`  |
| 845    | No file  | `6e9d2edeb5d7`  |
| 837    | No file  | `6e9d2edeb5d7`  |
| 829    | No file  | `6e9d2edeb5d7`  |
| 822    | No file  | `6e9d2edeb5d7`  |
| 814    | No file  | `6e9d2edeb5d7`  |
| 805    | No file  | `6e9d2edeb5d7`  |
| 794    | No file  | `6e9d2edeb5d7`  |
| 787    | No file  | `6e9d2edeb5d7`  |
| 780    | No file  | `6e9d2edeb5d7`  |
| 771    | No file  | `6e9d2edeb5d7`  |
| 760    | No file  | `6e9d2edeb5d7`  |
| 748    | No file  | `6e9d2edeb5d7`  |
| 741    | No file  | `6e9d2edeb5d7`  |
| 736    | No file  | `6e9d2edeb5d7`  |
| 731    | No file  | `6e9d2edeb5d7`  |
| 723    | No file  | `6e9d2edeb5d7`  |
| 711    | No file  | `6e9d2edeb5d7`  |
| 707    | No file  | `6e9d2edeb5d7`  |
| 697    | No file  | `6e9d2edeb5d7`  |
| 689    | No file  | `6e9d2edeb5d7`  |
| 683    | No file  | `6e9d2edeb5d7`  |
| 678    | No file  | `6e9d2edeb5d7`  |
| 670    | No file  | `6e9d2edeb5d7`  |
| 661    | No file  | `6e9d2edeb5d7`  |
| 656    | No file  | `6e9d2edeb5d7`  |
| 652    | No file  | `6e9d2edeb5d7`  |
| 643    | No file  | `6e9d2edeb5d7`  |
| 637    | No file  | `6e9d2edeb5d7`  |
| 630    | No file  | `6e9d2edeb5d7`  |
| 627    | No file  | `6e9d2edeb5d7`  |
| 621    | No file  | `6e9d2edeb5d7`  |
| 617    | No file  | `6e9d2edeb5d7`  |
| 615    | No file  | `6e9d2edeb5d7`  |
| 606    | No file  | `6e9d2edeb5d7`  |
| 599    | No file  | `6e9d2edeb5d7`  |
| 592    | No file  | `6e9d2edeb5d7`  |
| 586    | No file  | `6e9d2edeb5d7`  |
| 577    | No file  | `6e9d2edeb5d7`  |
| 569    | No file  | `6e9d2edeb5d7`  |
| 561    | No file  | `6e9d2edeb5d7`  |
| 554    | No file  | `6e9d2edeb5d7`  |
| 542    | No file  | `6e9d2edeb5d7`  |
| 532    | No file  | `6e9d2edeb5d7`  |
| 531    | No file  | `6e9d2edeb5d7`  |
| 526    | No file  | `6e9d2edeb5d7`  |
| 521    | No file  | `6e9d2edeb5d7`  |
| 517    | No file  | `6e9d2edeb5d7`  |
| 510    | No file  | `6e9d2edeb5d7`  |
| 508    | No file  | `6e9d2edeb5d7`  |
| 504    | No file  | `6e9d2edeb5d7`  |
| 497    | No file  | `6e9d2edeb5d7`  |
| 491    | No file  | `6e9d2edeb5d7`  |
| 485    | No file  | `6e9d2edeb5d7`  |
| 478    | No file  | `6e9d2edeb5d7`  |
| 472    | No file  | `6e9d2edeb5d7`  |
| 466    | No file  | `6e9d2edeb5d7`  |
| 457    | No file  | `6e9d2edeb5d7`  |
| 452    | No file  | `6e9d2edeb5d7`  |
| 449    | No file  | `6e9d2edeb5d7`  |
| 435    | No file  | `6e9d2edeb5d7`  |

<!-- versions:end -->

## Companion Files

None. The handler names each preset from the GAME sheet of
`stringtable.bss` and `languagedata_*.loc` when they are loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of weather presets                     |
| `+0x08`             | Row[row_count] | rows         | See Row; row `n` is `weatherPresetIndex` `n`  |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (8 bytes)

| Offset  | Type | Field            | Notes                                                        |
| ------- | ---- | ---------------- | ------------------------------------------------------------ |
| `+0x00` | u32  | unknown_00       | `0` to `31`, a different value on each row (client 3482)     |
| `+0x04` | u32  | weather_name_ref | String table index of the preset's GAME sheet name key       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                      |
| ------- | ------------------ | ------------ | ---------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; one per row on client 3482              |
| `+0x04` | pstr[string_count] | strings      | UTF-8 GAME sheet keys in row order; see Presets            |

## Presets

Client 3482, with the English text of each key:

| Preset | `unknown_00` | `weather_name_ref` string               | English                |
| ------ | ------------ | --------------------------------------- | ---------------------- |
| 0      | `0`          | `LUA_PHOTOMODE_WEATHER_DEFAULT`         | Town (Current)         |
| 1      | `1`          | `LUA_PHOTOMODE_WEATHER_CLOUDY`          | Town (Fog)             |
| 2      | `3`          | `LUA_PHOTOMODE_WEATHER_VALENCIA`        | Land of the Sun        |
| 3      | `4`          | `LUA_PHOTOMODE_WEATHER_VALENCIA_SAND`   | Great Desert           |
| 4      | `12`         | `LUA_PHOTOMODE_WEATHER_KAMASILVIA_POLY` | Ethereal Forest        |
| 5      | `13`         | `LUA_PHOTOMODE_WEATHER_KAMASILVIA_TREE` | Loopy Tree Forest      |
| 6      | `16`         | `LUA_PHOTOMODE_WEATHER_DRIGAN`          | Swamp Ruins            |
| 7      | `22`         | `LUA_PHOTOMODE_WEATHER_VEDIRTOWN`       | Ancient Kingdom        |
| 8      | `21`         | `LUA_PHOTOMODE_WEATHER_VEDIRFOREST`     | Thornwood Forest       |
| 9      | `23`         | `LUA_PHOTOMODE_WEATHER_SNOW`            | Everfrost              |
| 10     | `26`         | `LUA_PHOTOMODE_WEATHER_ATORAXION`       | Secret Fortress        |
| 11     | `17`         | `LUA_PHOTOMODE_WEATHER_DEEPSEA`         | Underwater Ruins       |
| 12     | `29`         | `LUA_PHOTOMODE_WEATHER_HADUM_SERENDIA`  | Foggy Sky              |
| 13     | `31`         | `LUA_PHOTOMODE_WEATHER_HADUM_CALPHEON`  | Crimson End            |
| 14     | `30`         | `LUA_PHOTOMODE_WEATHER_LOCALWAR`        | Battlefield of Shadows |

## Field Names

The file is not in client 1784, and a private server's
`DataSheets.bexcel` on client 1784 has no sheet with `Photo` in its name.
`weather_name_ref` follows the `weatherName` argument of
`FromClient_SetPhotoModeWeatherPresetIndex`, which the window passes to
`PAGetString(Defines.StringSheet_GAME, weatherName)`; every string of the
file is such a key.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/ui_tables.py`: one row
  per preset with its position, the name key and its LOC text.
  `unknown_00` gets no column.

## Open Questions

### What unknown_00 Is

Every `unknown_00` value of client 3482 has a weather colour table
`mapdata_common/baseweather_<n>.weathercolortablexml` (`0` the file
without a number), and the client has such tables for numbers the file
does not use (`2`, `5` to `11`, `14`, `15` and more, up to `39`). The value may pick the colour table of the
preset; neither the Lua nor the tables say so.
