# `midiinstrument.bss` Format

## Purpose

The instruments of the music composer and the instrument play: per
instrument its Wwise bank and event, the in-game name key, the
articulations it can play, the start, end and loop actions of the playing
character, the composer tab it sits on and whether every player owns it.
The composer Lua (`panel_window_selectinstruments_all_1.luac`,
`panel_window_myinstruments_all_1.luac`) reads it through
`Toclient_MidiInstrumentTrackCount()`, `Toclient_getInstrumentByIndex()`,
`ToClient_getAdvancedTypeByIndex()` and
`ToClient_getInstrumentIsOpenedByIndex()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | ----------------------- |
| 4      | 1846 and later | 3483    | `midiinstrument.bss` | 5,242 | 38 Row  | 56 to 69, 63 on average |
| 3      | 1547 to 3482   | 3482    | `midiinstrument.bss` | 5,242 | 38 Row  | 56 to 69, 63 on average |
| 2      | 1504 to 3482   | 3482    | `midiinstrument.bss` | 5,242 | 38 Row  | 56 to 69, 63 on average |
| 1      | 1409 to 1838   | 1838    | `midiinstrument.bss` | 1,833 | 15 Row  | 53 to 61, 55 on average |

| Layout | File                 | Known            | Unknown      |
| ------ | -------------------- | ---------------- | ------------ |
| 4      | `midiinstrument.bss` | 5,128 B (97.8%)  | 114 B (2.2%) |
| 3      | `midiinstrument.bss` | 5,128 B (97.8%)  | 114 B (2.2%) |
| 2      | `midiinstrument.bss` | 5,128 B (97.8%)  | 114 B (2.2%) |
| 1      | `midiinstrument.bss` | 1,833 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 4             | `f68d5351602e`  |
| 3482   | Layout 4             | `f68d5351602e`  |
| 3474   | Layout 4             | `f68d5351602e`  |
| 3473   | Layout 4             | `f68d5351602e`  |
| 3464   | Layout 4             | `f68d5351602e`  |
| 3458   | Layout 4             | `f68d5351602e`  |
| 3454   | Layout 4             | `f68d5351602e`  |
| 3444   | Layout 4             | `f68d5351602e`  |
| 3435   | Layout 4             | `f68d5351602e`  |
| 3426   | Layout 4             | `f68d5351602e`  |
| 3418   | Layout 4             | `f68d5351602e`  |
| 3412   | Layout 4             | `f68d5351602e`  |
| 3402   | Layout 4             | `f68d5351602e`  |
| 3396   | Layout 4             | `f68d5351602e`  |
| 3387   | Layout 4             | `f68d5351602e`  |
| 3381   | Layout 4             | `f68d5351602e`  |
| 3373   | Layout 4             | `f68d5351602e`  |
| 3364   | Layout 4             | `f68d5351602e`  |
| 3356   | Layout 4             | `f68d5351602e`  |
| 3349   | Layout 4             | `f68d5351602e`  |
| 3342   | Layout 4             | `f68d5351602e`  |
| 3335   | Layout 4             | `f68d5351602e`  |
| 3326   | Layout 4             | `f68d5351602e`  |
| 3321   | Layout 4             | `f68d5351602e`  |
| 3314   | Layout 4             | `f68d5351602e`  |
| 3303   | Layout 4             | `f68d5351602e`  |
| 3302   | Layout 4             | `f68d5351602e`  |
| 3293   | Layout 4             | `f68d5351602e`  |
| 3283   | Layout 4             | `f68d5351602e`  |
| 3275   | Layout 4             | `f68d5351602e`  |
| 3267   | Layout 4             | `f68d5351602e`  |
| 3258   | Layout 4             | `f68d5351602e`  |
| 3251   | Layout 4             | `f68d5351602e`  |
| 3242   | Layout 4             | `f68d5351602e`  |
| 3235   | Layout 4             | `f68d5351602e`  |
| 3229   | Layout 4             | `f68d5351602e`  |
| 3212   | Layout 4             | `f68d5351602e`  |
| 3203   | Layout 4             | `f68d5351602e`  |
| 3193   | Layout 4             | `f68d5351602e`  |
| 3186   | Layout 4             | `f68d5351602e`  |
| 3177   | Layout 4             | `f68d5351602e`  |
| 3169   | Layout 4             | `f68d5351602e`  |
| 3158   | Layout 4             | `f68d5351602e`  |
| 3151   | Layout 4             | `f68d5351602e`  |
| 3144   | Layout 4             | `f68d5351602e`  |
| 3133   | Layout 4             | `f68d5351602e`  |
| 3125   | Layout 4             | `f68d5351602e`  |
| 3118   | Layout 4             | `f68d5351602e`  |
| 3111   | Layout 4             | `f68d5351602e`  |
| 3103   | Layout 4             | `f68d5351602e`  |
| 3095   | Layout 4             | `f68d5351602e`  |
| 3086   | Layout 4             | `f68d5351602e`  |
| 3072   | Layout 4             | `f68d5351602e`  |
| 3062   | Layout 4             | `f68d5351602e`  |
| 3052   | Layout 4             | `f68d5351602e`  |
| 3045   | Layout 4             | `f68d5351602e`  |
| 3037   | Layout 4             | `f68d5351602e`  |
| 3030   | Layout 4             | `f68d5351602e`  |
| 3021   | Layout 4             | `f68d5351602e`  |
| 3012   | Layout 4             | `f68d5351602e`  |
| 3002   | Layout 4             | `f68d5351602e`  |
| 2995   | Layout 4             | `f68d5351602e`  |
| 2987   | Layout 4             | `f68d5351602e`  |
| 2978   | Layout 4             | `f68d5351602e`  |
| 2970   | Layout 4             | `f68d5351602e`  |
| 2959   | Layout 4             | `f68d5351602e`  |
| 2951   | Layout 4             | `f68d5351602e`  |
| 2942   | Layout 4             | `f68d5351602e`  |
| 2935   | Layout 4             | `f68d5351602e`  |
| 2932   | Layout 4             | `f68d5351602e`  |
| 2923   | Layout 4             | `f68d5351602e`  |
| 2919   | Layout 4             | `f68d5351602e`  |
| 2907   | Layout 4             | `f68d5351602e`  |
| 2900   | Layout 4             | `f68d5351602e`  |
| 2891   | Layout 4             | `f68d5351602e`  |
| 2882   | Layout 4             | `f68d5351602e`  |
| 2872   | Layout 4             | `f68d5351602e`  |
| 2863   | Layout 4             | `f68d5351602e`  |
| 2855   | Layout 4             | `f68d5351602e`  |
| 2849   | Layout 4             | `f68d5351602e`  |
| 2844   | Layout 4             | `f68d5351602e`  |
| 2834   | Layout 4             | `f68d5351602e`  |
| 2825   | Layout 4             | `f68d5351602e`  |
| 2819   | Layout 4             | `f68d5351602e`  |
| 2811   | Layout 4             | `f68d5351602e`  |
| 2803   | Layout 4             | `f68d5351602e`  |
| 2794   | Layout 4             | `f68d5351602e`  |
| 2783   | Layout 4             | `f68d5351602e`  |
| 2774   | Layout 4             | `f68d5351602e`  |
| 2765   | Layout 4             | `f68d5351602e`  |
| 2756   | Layout 4             | `f68d5351602e`  |
| 2750   | Layout 4             | `f68d5351602e`  |
| 2743   | Layout 4             | `f68d5351602e`  |
| 2736   | Layout 4             | `f68d5351602e`  |
| 2726   | Layout 4             | `f68d5351602e`  |
| 2717   | Layout 4             | `f68d5351602e`  |
| 2709   | Layout 4             | `f68d5351602e`  |
| 2703   | Layout 4             | `f68d5351602e`  |
| 2695   | Layout 4             | `f68d5351602e`  |
| 2684   | Layout 4             | `f68d5351602e`  |
| 2672   | Layout 4             | `f68d5351602e`  |
| 2665   | Layout 4             | `f68d5351602e`  |
| 2657   | Layout 4             | `f68d5351602e`  |
| 2649   | Layout 4             | `f68d5351602e`  |
| 2644   | Layout 4             | `f68d5351602e`  |
| 2637   | Layout 4             | `f68d5351602e`  |
| 2629   | Layout 4             | `f68d5351602e`  |
| 2619   | Layout 4             | `f68d5351602e`  |
| 2612   | Layout 4             | `f68d5351602e`  |
| 2606   | Layout 4             | `f68d5351602e`  |
| 2602   | Layout 4             | `f68d5351602e`  |
| 2601   | Layout 4             | `f68d5351602e`  |
| 2592   | Layout 4             | `f68d5351602e`  |
| 2583   | Layout 4             | `f68d5351602e`  |
| 2575   | Layout 4             | `f68d5351602e`  |
| 2567   | Layout 4             | `f68d5351602e`  |
| 2560   | Layout 4             | `f68d5351602e`  |
| 2553   | Layout 4             | `f68d5351602e`  |
| 2545   | Layout 4             | `f68d5351602e`  |
| 2538   | Layout 4             | `f68d5351602e`  |
| 2529   | Layout 4             | `f68d5351602e`  |
| 2519   | Layout 4             | `f68d5351602e`  |
| 2513   | Layout 4             | `f68d5351602e`  |
| 2510   | Layout 4             | `f68d5351602e`  |
| 2507   | Layout 4             | `f68d5351602e`  |
| 2503   | Layout 4             | `f68d5351602e`  |
| 2498   | Layout 4             | `f68d5351602e`  |
| 2492   | Layout 4             | `f68d5351602e`  |
| 2487   | Layout 4             | `f68d5351602e`  |
| 2480   | Layout 4             | `f68d5351602e`  |
| 2474   | Layout 4             | `f68d5351602e`  |
| 2468   | Layout 4             | `f68d5351602e`  |
| 2460   | Layout 4             | `f68d5351602e`  |
| 2453   | Layout 4             | `f68d5351602e`  |
| 2444   | Layout 4             | `f68d5351602e`  |
| 2438   | Layout 4             | `f68d5351602e`  |
| 2434   | Layout 4             | `f68d5351602e`  |
| 2429   | Layout 4             | `f68d5351602e`  |
| 2421   | Layout 4             | `f68d5351602e`  |
| 2414   | Layout 4             | `f68d5351602e`  |
| 2407   | Layout 4             | `f68d5351602e`  |
| 2401   | Layout 4             | `f68d5351602e`  |
| 2397   | Layout 4             | `f68d5351602e`  |
| 2393   | Layout 4             | `f68d5351602e`  |
| 2384   | Layout 4             | `f68d5351602e`  |
| 2378   | Layout 4             | `f68d5351602e`  |
| 2372   | Layout 4             | `f68d5351602e`  |
| 2358   | Layout 4             | `f68d5351602e`  |
| 2352   | Layout 4             | `f68d5351602e`  |
| 2347   | Layout 4             | `f68d5351602e`  |
| 2343   | Layout 4             | `f68d5351602e`  |
| 2335   | Layout 4             | `f68d5351602e`  |
| 2327   | Layout 4             | `f68d5351602e`  |
| 2324   | Layout 4             | `f68d5351602e`  |
| 2319   | Layout 4             | `f68d5351602e`  |
| 2313   | Layout 4             | `f68d5351602e`  |
| 2308   | Layout 4             | `f68d5351602e`  |
| 2302   | Layout 4             | `f68d5351602e`  |
| 2295   | Layout 4             | `f68d5351602e`  |
| 2290   | Layout 4             | `f68d5351602e`  |
| 2284   | Layout 4             | `f68d5351602e`  |
| 2276   | Layout 4             | `f68d5351602e`  |
| 2269   | Layout 4             | `f68d5351602e`  |
| 2259   | Layout 4             | `f68d5351602e`  |
| 2250   | Layout 4             | `f68d5351602e`  |
| 2243   | Layout 4             | `f68d5351602e`  |
| 2235   | Layout 4             | `f68d5351602e`  |
| 2229   | Layout 4             | `f68d5351602e`  |
| 2224   | Layout 4             | `f68d5351602e`  |
| 2218   | Layout 4             | `f68d5351602e`  |
| 2215   | Layout 4             | `f68d5351602e`  |
| 2207   | Layout 4             | `f68d5351602e`  |
| 2203   | Layout 4             | `f68d5351602e`  |
| 2196   | Layout 4             | `f68d5351602e`  |
| 2192   | Layout 4             | `f68d5351602e`  |
| 2189   | Layout 4             | `f68d5351602e`  |
| 2183   | Layout 4             | `f68d5351602e`  |
| 2179   | Layout 4             | `f68d5351602e`  |
| 2171   | Layout 4             | `f68d5351602e`  |
| 2163   | Layout 4             | `f68d5351602e`  |
| 2156   | Layout 4             | `f68d5351602e`  |
| 2151   | Layout 4             | `f68d5351602e`  |
| 2147   | Layout 4             | `f68d5351602e`  |
| 2142   | Layout 4             | `f68d5351602e`  |
| 2138   | Layout 4             | `f68d5351602e`  |
| 2134   | Layout 4             | `f68d5351602e`  |
| 2130   | Layout 4             | `f68d5351602e`  |
| 2122   | Layout 4             | `f68d5351602e`  |
| 2107   | Layout 4             | `f68d5351602e`  |
| 2098   | Layout 4             | `f68d5351602e`  |
| 2089   | Layout 4             | `f68d5351602e`  |
| 2081   | Layout 4             | `f68d5351602e`  |
| 2073   | Layout 4             | `f68d5351602e`  |
| 2067   | Layout 4             | `f68d5351602e`  |
| 2063   | Layout 4             | `f68d5351602e`  |
| 2059   | Layout 4             | `f68d5351602e`  |
| 2052   | Layout 4             | `f68d5351602e`  |
| 2044   | Layout 4             | `f68d5351602e`  |
| 2039   | Layout 4             | `f68d5351602e`  |
| 2032   | Layout 4             | `f68d5351602e`  |
| 2025   | Layout 4             | `f68d5351602e`  |
| 2011   | Layout 4             | `f68d5351602e`  |
| 2005   | Layout 4             | `f68d5351602e`  |
| 2000   | Layout 4             | `f68d5351602e`  |
| 1996   | Layout 4             | `f68d5351602e`  |
| 1991   | Layout 4             | `f68d5351602e`  |
| 1985   | Layout 4             | `f68d5351602e`  |
| 1980   | Layout 4             | `f68d5351602e`  |
| 1969   | Layout 4             | `f68d5351602e`  |
| 1964   | Layout 4             | `f68d5351602e`  |
| 1958   | Layout 4             | `f68d5351602e`  |
| 1950   | Layout 4             | `f68d5351602e`  |
| 1945   | Layout 4             | `f68d5351602e`  |
| 1937   | Layout 4             | `f68d5351602e`  |
| 1933   | Layout 4             | `f68d5351602e`  |
| 1927   | Layout 4             | `f68d5351602e`  |
| 1921   | Layout 4             | `f68d5351602e`  |
| 1914   | Layout 4             | `f68d5351602e`  |
| 1908   | Layout 4             | `f68d5351602e`  |
| 1897   | Layout 4             | `f68d5351602e`  |
| 1892   | Layout 4             | `f68d5351602e`  |
| 1886   | Layout 4             | `f68d5351602e`  |
| 1881   | Layout 4             | `f68d5351602e`  |
| 1871   | Layout 4             | `f68d5351602e`  |
| 1866   | Layout 4             | `f68d5351602e`  |
| 1862   | Layout 4             | `f68d5351602e`  |
| 1854   | Layout 4             | `f68d5351602e`  |
| 1846   | Layout 4             | `f68d5351602e`  |
| 1838   | Layout 3             | `f68d5351602e`  |
| 1832   | Layout 3             | `f68d5351602e`  |
| 1826   | Layout 3             | `f68d5351602e`  |
| 1822   | Layout 3             | `f68d5351602e`  |
| 1818   | Layout 3             | `f68d5351602e`  |
| 1804   | Layout 3             | `f68d5351602e`  |
| 1794   | Layout 3             | `f68d5351602e`  |
| 1790   | Layout 3             | `f68d5351602e`  |
| 1784   | Layout 3             | `f68d5351602e`  |
| 1774   | Layout 3             | `f68d5351602e`  |
| 1771   | Layout 3             | `f68d5351602e`  |
| 1762   | Layout 3             | `f68d5351602e`  |
| 1759   | Layout 3             | `f68d5351602e`  |
| 1754   | Layout 3             | `f68d5351602e`  |
| 1749   | Layout 3             | `f68d5351602e`  |
| 1743   | Layout 3             | `f68d5351602e`  |
| 1737   | Layout 3             | `f68d5351602e`  |
| 1731   | Layout 3             | `f68d5351602e`  |
| 1725   | Layout 3             | `f68d5351602e`  |
| 1717   | Layout 3             | `f68d5351602e`  |
| 1710   | Layout 3             | `f68d5351602e`  |
| 1704   | Layout 3             | `f68d5351602e`  |
| 1698   | Layout 3             | `f68d5351602e`  |
| 1690   | Layout 3             | `f68d5351602e`  |
| 1685   | Layout 3             | `f68d5351602e`  |
| 1680   | Layout 3             | `f68d5351602e`  |
| 1674   | Layout 3             | `f68d5351602e`  |
| 1668   | Layout 3             | `f68d5351602e`  |
| 1659   | Layout 3             | `f68d5351602e`  |
| 1649   | Layout 3             | `f68d5351602e`  |
| 1642   | Layout 3             | `f68d5351602e`  |
| 1636   | Layout 3             | `f68d5351602e`  |
| 1628   | Layout 3             | `f68d5351602e`  |
| 1622   | Layout 3             | `f68d5351602e`  |
| 1614   | Layout 3             | `f68d5351602e`  |
| 1608   | Layout 3             | `f68d5351602e`  |
| 1602   | Layout 3             | `f68d5351602e`  |
| 1598   | Layout 3             | `f68d5351602e`  |
| 1594   | Layout 3             | `f68d5351602e`  |
| 1590   | Layout 3             | `f68d5351602e`  |
| 1587   | Layout 3             | `f68d5351602e`  |
| 1584   | Layout 3             | `f68d5351602e`  |
| 1579   | Layout 3             | `f68d5351602e`  |
| 1572   | Layout 3             | `f68d5351602e`  |
| 1565   | Layout 3             | `f68d5351602e`  |
| 1559   | Layout 3             | `f68d5351602e`  |
| 1554   | Layout 3             | `f68d5351602e`  |
| 1547   | Layout 3             | `f68d5351602e`  |
| 1537   | Layout 2             | `f68d5351602e`  |
| 1529   | Layout 2             | `f68d5351602e`  |
| 1524   | Layout 2             | `f68d5351602e`  |
| 1519   | Layout 2             | `f68d5351602e`  |
| 1509   | Layout 2             | `f68d5351602e`  |
| 1506   | Layout 2             | `f68d5351602e`  |
| 1504   | Layout 2             | `f68d5351602e`  |
| 1500   | Layout 1             | `f68d5351602e`  |
| 1493   | Layout 1             | `f68d5351602e`  |
| 1489   | Layout 1             | `f68d5351602e`  |
| 1485   | Layout 1             | `f68d5351602e`  |
| 1481   | Layout 1             | `f68d5351602e`  |
| 1474   | Layout 1             | `f68d5351602e`  |
| 1466   | Layout 1             | `f68d5351602e`  |
| 1462   | Layout 1             | `f68d5351602e`  |
| 1459   | Layout 1             | `f68d5351602e`  |
| 1453   | Layout 1             | `f68d5351602e`  |
| 1450   | Layout 1             | `f68d5351602e`  |
| 1445   | Layout 1             | `f68d5351602e`  |
| 1439   | Layout 1             | `f68d5351602e`  |
| 1433   | Layout 1             | `f68d5351602e`  |
| 1430   | Layout 1             | `f68d5351602e`  |
| 1426   | Layout 1             | `f68d5351602e`  |
| 1421   | Layout 1             | `f68d5351602e`  |
| 1417   | Layout 1             | `f68d5351602e`  |
| 1416   | Layout 1             | `f68d5351602e`  |
| 1409   | Layout 1             | `f68d5351602e`  |
| 1405   | No documented layout | `f68d5351602e`  |
| 1401   | No documented layout | `f68d5351602e`  |
| 1396   | No documented layout | `f68d5351602e`  |
| 1391   | No documented layout | `f68d5351602e`  |
| 1390   | No documented layout | `f68d5351602e`  |
| 1386   | No documented layout | `f68d5351602e`  |
| 1381   | No documented layout | `f68d5351602e`  |
| 1379   | No documented layout | `f68d5351602e`  |
| 1372   | No documented layout | `f68d5351602e`  |
| 1366   | No documented layout | `f68d5351602e`  |
| 1364   | No documented layout | `f68d5351602e`  |
| 1363   | No documented layout | `f68d5351602e`  |
| 1360   | No documented layout | `f68d5351602e`  |
| 1358   | No documented layout | `f68d5351602e`  |
| 1355   | No documented layout | `f68d5351602e`  |
| 1351   | No documented layout | `f68d5351602e`  |
| 1348   | No documented layout | `f68d5351602e`  |
| 1346   | No documented layout | `f68d5351602e`  |
| 1341   | No documented layout | `f68d5351602e`  |
| 1340   | No documented layout | `f68d5351602e`  |
| 1338   | No documented layout | `f68d5351602e`  |
| 1335   | No documented layout | `f68d5351602e`  |
| 1333   | No documented layout | `f68d5351602e`  |
| 1329   | No documented layout | `f68d5351602e`  |
| 1327   | No documented layout | `f68d5351602e`  |
| 1324   | No documented layout | `f68d5351602e`  |
| 1321   | No documented layout | `f68d5351602e`  |
| 1319   | No documented layout | `f68d5351602e`  |
| 1318   | No documented layout | `f68d5351602e`  |
| 1316   | No documented layout | `f68d5351602e`  |
| 1313   | No documented layout | `f68d5351602e`  |
| 1311   | No documented layout | `f68d5351602e`  |
| 1309   | No documented layout | `f68d5351602e`  |
| 1304   | No documented layout | `f68d5351602e`  |
| 1292   | No documented layout | `f68d5351602e`  |
| 1286   | No documented layout | `f68d5351602e`  |
| 1280   | No documented layout | `f68d5351602e`  |
| 1276   | No documented layout | `f68d5351602e`  |
| 1267   | No documented layout | `f68d5351602e`  |
| 1261   | No documented layout | `f68d5351602e`  |
| 1256   | No documented layout | `f68d5351602e`  |
| 1250   | No documented layout | `f68d5351602e`  |
| 1246   | No file              | `f68d5351602e`  |
| 1239   | No file              | `f68d5351602e`  |
| 1230   | No file              | `f68d5351602e`  |
| 1226   | No file              | `f68d5351602e`  |
| 1220   | No file              | `f68d5351602e`  |
| 1217   | No file              | `f68d5351602e`  |
| 1211   | No file              | `f68d5351602e`  |
| 1210   | No file              | `f68d5351602e`  |
| 1208   | No file              | `f68d5351602e`  |
| 1203   | No file              | `f68d5351602e`  |
| 1197   | No file              | `f68d5351602e`  |
| 1194   | No file              | `f68d5351602e`  |
| 1192   | No file              | `f68d5351602e`  |
| 1187   | No file              | `f68d5351602e`  |
| 1183   | No file              | `f68d5351602e`  |
| 1177   | No file              | `f68d5351602e`  |
| 1173   | No file              | `f68d5351602e`  |
| 1167   | No file              | `f68d5351602e`  |
| 1164   | No file              | `f68d5351602e`  |
| 1156   | No file              | `f68d5351602e`  |
| 1149   | No file              | `f68d5351602e`  |
| 1144   | No file              | `f68d5351602e`  |
| 1137   | No file              | `f68d5351602e`  |
| 1132   | No file              | `f68d5351602e`  |
| 1127   | No file              | `f68d5351602e`  |
| 1122   | No file              | `f68d5351602e`  |
| 1118   | No file              | `f68d5351602e`  |
| 1114   | No file              | `f68d5351602e`  |
| 1109   | No file              | `f68d5351602e`  |
| 1102   | No file              | `f68d5351602e`  |
| 1096   | No file              | `f68d5351602e`  |
| 1088   | No file              | `f68d5351602e`  |
| 1081   | No file              | `f68d5351602e`  |
| 1076   | No file              | `f68d5351602e`  |
| 1069   | No file              | `f68d5351602e`  |
| 1064   | No file              | `f68d5351602e`  |
| 1058   | No file              | `f68d5351602e`  |
| 1051   | No file              | `f68d5351602e`  |
| 1044   | No file              | `f68d5351602e`  |
| 1036   | No file              | `f68d5351602e`  |
| 1026   | No file              | `f68d5351602e`  |
| 1016   | No file              | `f68d5351602e`  |
| 1009   | No file              | `f68d5351602e`  |
| 1005   | No file              | `f68d5351602e`  |
| 1000   | No file              | `f68d5351602e`  |
| 998    | No file              | `f68d5351602e`  |
| 990    | No file              | `f68d5351602e`  |
| 979    | No file              | `f68d5351602e`  |
| 972    | No file              | `f68d5351602e`  |
| 963    | No file              | `f68d5351602e`  |
| 955    | No file              | `f68d5351602e`  |
| 946    | No file              | `f68d5351602e`  |
| 938    | No file              | `f68d5351602e`  |
| 927    | No file              | `f68d5351602e`  |
| 911    | No file              | `f68d5351602e`  |
| 904    | No file              | `f68d5351602e`  |
| 899    | No file              | `f68d5351602e`  |
| 894    | No file              | `f68d5351602e`  |
| 885    | No file              | `f68d5351602e`  |
| 879    | No file              | `f68d5351602e`  |
| 872    | No file              | `f68d5351602e`  |
| 864    | No file              | `f68d5351602e`  |
| 855    | No file              | `f68d5351602e`  |
| 853    | No file              | `f68d5351602e`  |
| 845    | No file              | `f68d5351602e`  |
| 837    | No file              | `f68d5351602e`  |
| 829    | No file              | `f68d5351602e`  |
| 822    | No file              | `f68d5351602e`  |
| 814    | No file              | `f68d5351602e`  |
| 805    | No file              | `f68d5351602e`  |
| 794    | No file              | `f68d5351602e`  |
| 787    | No file              | `f68d5351602e`  |
| 780    | No file              | `f68d5351602e`  |
| 771    | No file              | `f68d5351602e`  |
| 760    | No file              | `f68d5351602e`  |
| 748    | No file              | `f68d5351602e`  |
| 741    | No file              | `f68d5351602e`  |
| 736    | No file              | `f68d5351602e`  |
| 731    | No file              | `f68d5351602e`  |
| 723    | No file              | `f68d5351602e`  |
| 711    | No file              | `f68d5351602e`  |
| 707    | No file              | `f68d5351602e`  |
| 697    | No file              | `f68d5351602e`  |
| 689    | No file              | `f68d5351602e`  |
| 683    | No file              | `f68d5351602e`  |
| 678    | No file              | `f68d5351602e`  |
| 670    | No file              | `f68d5351602e`  |
| 661    | No file              | `f68d5351602e`  |
| 656    | No file              | `f68d5351602e`  |
| 652    | No file              | `f68d5351602e`  |
| 643    | No file              | `f68d5351602e`  |
| 637    | No file              | `f68d5351602e`  |
| 630    | No file              | `f68d5351602e`  |
| 627    | No file              | `f68d5351602e`  |
| 621    | No file              | `f68d5351602e`  |
| 617    | No file              | `f68d5351602e`  |
| 615    | No file              | `f68d5351602e`  |
| 606    | No file              | `f68d5351602e`  |
| 599    | No file              | `f68d5351602e`  |
| 592    | No file              | `f68d5351602e`  |
| 586    | No file              | `f68d5351602e`  |
| 577    | No file              | `f68d5351602e`  |
| 569    | No file              | `f68d5351602e`  |
| 561    | No file              | `f68d5351602e`  |
| 554    | No file              | `f68d5351602e`  |
| 542    | No file              | `f68d5351602e`  |
| 532    | No file              | `f68d5351602e`  |
| 531    | No file              | `f68d5351602e`  |
| 526    | No file              | `f68d5351602e`  |
| 521    | No file              | `f68d5351602e`  |
| 517    | No file              | `f68d5351602e`  |
| 510    | No file              | `f68d5351602e`  |
| 508    | No file              | `f68d5351602e`  |
| 504    | No file              | `f68d5351602e`  |
| 497    | No file              | `f68d5351602e`  |
| 491    | No file              | `f68d5351602e`  |
| 485    | No file              | `f68d5351602e`  |
| 478    | No file              | `f68d5351602e`  |
| 472    | No file              | `f68d5351602e`  |
| 466    | No file              | `f68d5351602e`  |
| 457    | No file              | `f68d5351602e`  |
| 452    | No file              | `f68d5351602e`  |
| 449    | No file              | `f68d5351602e`  |
| 435    | No file              | `f68d5351602e`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset                       | Type                     | Field              | Notes                                         |
| ---------------------------- | ------------------------ | ------------------ | --------------------------------------------- |
| `+0x00`                      | char[4]                  | magic              | ASCII `PABR`                                  |
| `+0x04`                      | u32                      | row_count          | Number of instruments                         |
| `+0x08`                      | Row[row_count]           | rows               | See Row                                       |
| `rows+0x00`                  | u32                      | action_hash_count  | Number of `action_hashes`                     |
| `rows+0x04`                  | u32[action_hash_count]   | action_hashes      | Every distinct start and loop action hash of the rows, each once; see Notes |
| `action_hashes+0x00`         | String Table             | string_table       | See String Table                              |
| `string_table+0x00`          | u32                      | string_table_start | Offset of the string table, where `action_hashes` ends |
| `string_table+0x04`          | u32                      | zero               | `0`                                           |

### Row (variable: 43 bytes + articulations and loop actions)

| Offset                     | Type                     | Field                        | Notes                                                                                       |
| -------------------------- | ------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------- |
| `+0x00`                    | u8                       | index                        | Row key, `0` to `40` with gaps on client 3482; the number in `bank_name` for `0` to `19`    |
| `+0x01`                    | u32                      | bank_name                    | Index into `strings`: the Wwise bank (`MIDI_Instrument_00_AcousticGuitar`)                  |
| `+0x05`                    | u32                      | event_name                   | Index into `strings`: the Wwise event; the same string as `bank_name` on every row          |
| `+0x09`                    | u32                      | ingame_name                  | Index into `strings`: the name key (`AcousticGuitar`, `Advanced_Piano`)                     |
| `+0x0D`                    | u64                      | articulation_count           | Number of `articulations`                                                                   |
| `+0x15`                    | u8[articulation_count]   | articulations                | Articulation numbers; `99` alone for an instrument with one way to play                     |
| `articulations+0x00`       | u32                      | start_action_hash            | `ascii_key_hash` of the start action name (`SHY_MusicStart_Guitar` on client 1784)          |
| `articulations+0x04`       | u32                      | end_action_hash              | `ascii_key_hash` of the end action name                                                     |
| `articulations+0x08`       | u8                       | advanced_type                | Composer tab; see Advanced Type                                                             |
| `articulations+0x09`       | u32                      | instrument_name_type         | Index into `strings`: the tab name key (`AUDIO_MIDI_TAB_NOVICE`), UTF-16LE                  |
| `articulations+0x0D`       | u8                       | is_opened                    | `1` on every row                                                                            |
| `articulations+0x0E`       | u32                      | ing_action_count             | Number of `ing_action_hashes`; `3` on every row                                             |
| `articulations+0x12`       | u32[ing_action_count]    | ing_action_hashes            | `ascii_key_hash` of the loop action names (`SHY_MusicIng_Guitar` to `SHY_MusicIng3_Guitar`) |
| `ing_action_hashes+0x00`   | u8                       | is_provided                  | `1` for the instruments every character owns (Acoustic Guitar, Flute, Hand Drum on client 1784) |
| `ing_action_hashes+0x01`   | u8                       | unknown_ing_action_hashes_01 | `0` to `3`; see Open Questions                                                              |
| `ing_action_hashes+0x02`   | u8                       | unknown_ing_action_hashes_02 | The bank number in `bank_name` (`24` for `MIDI_Instrument_24_ProGuitarElectricClean`); `20` to `23` for the sine, triangle, square and saw synths |
| `ing_action_hashes+0x03`   | u8                       | unknown_ing_action_hashes_03 | `0` to `3` for the synth variants Basic, Stereo, Super and SuperOct; `0` on every other row |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                  |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                      |
| `+0x04` | pstr[string_count] | strings      | Bank, name and tab keys; a string several rows use is stored once; the tab keys are UTF-16LE (`is_wide` `1`), the rest UTF-8 |

## Layout 3

The row ends with `is_provided`: the three bytes after it do not exist yet.
Only the Row differs from Layout 4.

### Row (variable: 40 bytes + articulations and loop actions)

| Offset                     | Type                     | Field                | Notes                                                    |
| -------------------------- | ------------------------ | -------------------- | -------------------------------------------------------- |
| `+0x00`                    | u8                       | index                | Row key, `0` to `19` with gaps on client 1784            |
| `+0x01`                    | u32                      | bank_name            | Index into `strings`                                     |
| `+0x05`                    | u32                      | event_name           | Index into `strings`                                     |
| `+0x09`                    | u32                      | ingame_name          | Index into `strings`                                     |
| `+0x0D`                    | u64                      | articulation_count   | Number of `articulations`                                |
| `+0x15`                    | u8[articulation_count]   | articulations        | Articulation numbers                                     |
| `articulations+0x00`       | u32                      | start_action_hash    | `ascii_key_hash` of the start action name                |
| `articulations+0x04`       | u32                      | end_action_hash      | `ascii_key_hash` of the end action name                  |
| `articulations+0x08`       | u8                       | advanced_type        | Composer tab; see Advanced Type                          |
| `articulations+0x09`       | u32                      | instrument_name_type | Index into `strings`                                     |
| `articulations+0x0D`       | u8                       | is_opened            | `1` on every row                                         |
| `articulations+0x0E`       | u32                      | ing_action_count     | Number of `ing_action_hashes`                            |
| `articulations+0x12`       | u32[ing_action_count]    | ing_action_hashes    | `ascii_key_hash` of the loop action names                |
| `ing_action_hashes+0x00`   | u8                       | is_provided          | `1` for the instruments every character owns             |

## Layout 2

No `is_opened` byte after `instrument_name_type`, and the row ends with
`is_provided` as in Layout 3. Only the Row differs from Layout 3.

### Row (variable: 39 bytes + articulations and loop actions)

| Offset                     | Type                     | Field                | Notes                                                    |
| -------------------------- | ------------------------ | -------------------- | -------------------------------------------------------- |
| `+0x00`                    | u8                       | index                | Row key, `0` to `8` with gaps on client 1537             |
| `+0x01`                    | u32                      | bank_name            | Index into `strings`                                     |
| `+0x05`                    | u32                      | event_name           | Index into `strings`                                     |
| `+0x09`                    | u32                      | ingame_name          | Index into `strings`                                     |
| `+0x0D`                    | u64                      | articulation_count   | Number of `articulations`                                |
| `+0x15`                    | u8[articulation_count]   | articulations        | Articulation numbers                                     |
| `articulations+0x00`       | u32                      | start_action_hash    | `ascii_key_hash` of the start action name                |
| `articulations+0x04`       | u32                      | end_action_hash      | `ascii_key_hash` of the end action name                  |
| `articulations+0x08`       | u8                       | advanced_type        | Composer tab; see Advanced Type                          |
| `articulations+0x09`       | u32                      | instrument_name_type | Index into `strings`                                     |
| `articulations+0x0D`       | u32                      | ing_action_count     | Number of `ing_action_hashes`                            |
| `articulations+0x11`       | u32[ing_action_count]    | ing_action_hashes    | `ascii_key_hash` of the loop action names                |
| `ing_action_hashes+0x00`   | u8                       | is_provided          | `1` for the instruments every character owns             |

## Layout 1

No composer tab: the row has no `advanced_type`, `instrument_name_type` or
`is_opened`, and the loop actions follow the end action. Only the Row
differs from Layout 2.

### Row (variable: 34 bytes + articulations and loop actions)

| Offset                     | Type                     | Field              | Notes                                                    |
| -------------------------- | ------------------------ | ------------------ | -------------------------------------------------------- |
| `+0x00`                    | u8                       | index              | Row key, `0` to `8` with gaps on client 1485             |
| `+0x01`                    | u32                      | bank_name          | Index into `strings`                                     |
| `+0x05`                    | u32                      | event_name         | Index into `strings`                                     |
| `+0x09`                    | u32                      | ingame_name        | Index into `strings`                                     |
| `+0x0D`                    | u64                      | articulation_count | Number of `articulations`                                |
| `+0x15`                    | u8[articulation_count]   | articulations      | Articulation numbers                                     |
| `articulations+0x00`       | u32                      | start_action_hash  | `ascii_key_hash` of the start action name                |
| `articulations+0x04`       | u32                      | end_action_hash    | `ascii_key_hash` of the end action name                  |
| `articulations+0x08`       | u32                      | ing_action_count   | Number of `ing_action_hashes`                            |
| `articulations+0x0C`       | u32[ing_action_count]    | ing_action_hashes  | `ascii_key_hash` of the loop action names                |
| `ing_action_hashes+0x00`   | u8                       | is_provided        | `1` for the instruments every character owns             |

## Advanced Type

| Value | Tab key (`instrument_name_type`)        | Instruments on client 3482                                  |
| ----- | --------------------------------------- | ----------------------------------------------------------- |
| 0     | `AUDIO_MIDI_TAB_NOVICE`                 | Acoustic Guitar to Violin, the beginner instruments          |
| 1     | `AUDIO_MIDI_TAB_ADVANCED`               | The Marnian instruments (`Advanced_*`) without the electric ones |
| 2     | `AUDIO_MIDI_TAB_ADVANCED_ELECTRONIC`    | Electric bass and guitars, the 16 synths                     |

The composer Lua names `__eInstrumentAdvancedType_Novice`,
`__eInstrumentAdvancedType_Advanced`, `__eeInstrumentAdvancedType_Synth`
(sic) and `__eInstrumentAdvancedType_Count`.

## Field Names

The `MidiInstrument_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Index`, `BankName`, `EventName`,
`ArticulationList`, `IngameName`, `IsOpened`, `ContentsGroupKey`,
`StartAction`, `EndAction`, `IsProvided`, `IngAction`, `SoundEffector`,
`AdvancedType`, `InstrumentNameType` and `InstrumentName`, 20 rows. The
client file holds the 15 rows with `IsOpened` `1`; the five with `0` are
not compiled. On those 15 rows every named field matches its column (15 of
15, client 1784); the action hashes are `ascii_key_hash` of the
`StartAction`, `EndAction` and `IngAction` names. `SoundEffector` holds the
same values as `AdvancedType` on all 20 rows; the field is named after
`AdvancedType`, which sits before `InstrumentNameType` in the sheet as the
field does in the row, and the electronic tab rows of client 3482 hold `2`
there. `ContentsGroupKey` and `InstrumentName`
(`AUDIO_MIDI_INSTRUMENT_0`) are not in the client file.

## Notes

- On client 3482 the start, end and loop action hashes match none of the
  client 1784 action names: the actions were renamed. Rows that share an
  instrument model (Acoustic Guitar and Marnian Acoustic Guitar, the four
  variants of one synth) share their hashes.
- `action_hashes` lists every distinct `start_action_hash` and
  `ing_action_hash` of the rows, each once and in no sorted order; no
  `end_action_hash` is in it (clients 1784 and 3482).

## Open Questions

### Instrument Family Byte

`unknown_ing_action_hashes_01` groups the instruments on client 3482: `0`
piano and the synths, `1` flute, recorder, clarinet and horn, `2` the
string instruments (guitars, harp, violin, basses), `3` the drums, cymbals
and hand pan. No sheet column of client 1784 holds it; the composer may
pick the play animation or the score clef with it.

### Rows Before Client 1409

Clients 1256 to 1390 hold another row (client 1256: two instruments in
144 bytes) that breaks every layout at `articulation_count`. No layout
reads these files yet.
