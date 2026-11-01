# `abyssoneequipmentpreset.bss` Format

## Purpose

The gear the Magnus (`AbyssOne`) hands out, per equipment slot: a list of
presets, each a class type, an item key and a coin price. The armor and
accessory slots hold one item for every class, the weapon slots one item
per class type, and four armor slots and the weapon slots end with a
Magic Crystal for every class. The file has no PABR magic. The client
reads it through `ToClient_GetAbyssOnePresetStaticStatus(equipSlotNo,
classType, presetLevel, isSocket)`, whose result gives
`getEquipItemKey()` and `getAbyssCoin()` (`panel_abyssone_equippresetlist.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes | Records            | Row bytes |
| ------ | -------------- | ----------------------------- | ----- | ------------------ | --------- |
| 1      | 2011 and later | `abyssoneequipmentpreset.bss` | 2,221 | 113 Preset, 14 Row | 19        |

| Layout | File                          | Known           | Unknown       |
| ------ | ----------------------------- | --------------- | ------------- |
| 1      | `abyssoneequipmentpreset.bss` | 1,543 B (69.5%) | 678 B (30.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `513714d2457c`  |
| 3482   | Layout 1             | `513714d2457c`  |
| 3474   | Layout 1             | `513714d2457c`  |
| 3473   | Layout 1             | `513714d2457c`  |
| 3464   | Layout 1             | `513714d2457c`  |
| 3458   | Layout 1             | `513714d2457c`  |
| 3454   | Layout 1             | `513714d2457c`  |
| 3444   | Layout 1             | `513714d2457c`  |
| 3435   | Layout 1             | `513714d2457c`  |
| 3426   | Layout 1             | `513714d2457c`  |
| 3418   | Layout 1             | `513714d2457c`  |
| 3412   | Layout 1             | `513714d2457c`  |
| 3402   | Layout 1             | `513714d2457c`  |
| 3396   | Layout 1             | `513714d2457c`  |
| 3387   | Layout 1             | `513714d2457c`  |
| 3381   | Layout 1             | `513714d2457c`  |
| 3373   | Layout 1             | `513714d2457c`  |
| 3364   | Layout 1             | `513714d2457c`  |
| 3356   | Layout 1             | `513714d2457c`  |
| 3349   | Layout 1             | `513714d2457c`  |
| 3342   | Layout 1             | `513714d2457c`  |
| 3335   | Layout 1             | `513714d2457c`  |
| 3326   | Layout 1             | `513714d2457c`  |
| 3321   | Layout 1             | `513714d2457c`  |
| 3314   | Layout 1             | `513714d2457c`  |
| 3303   | Layout 1             | `513714d2457c`  |
| 3302   | Layout 1             | `513714d2457c`  |
| 3293   | Layout 1             | `513714d2457c`  |
| 3283   | Layout 1             | `513714d2457c`  |
| 3275   | Layout 1             | `513714d2457c`  |
| 3267   | Layout 1             | `513714d2457c`  |
| 3258   | Layout 1             | `513714d2457c`  |
| 3251   | Layout 1             | `513714d2457c`  |
| 3242   | Layout 1             | `513714d2457c`  |
| 3235   | Layout 1             | `513714d2457c`  |
| 3229   | Layout 1             | `513714d2457c`  |
| 3212   | Layout 1             | `513714d2457c`  |
| 3203   | Layout 1             | `513714d2457c`  |
| 3193   | Layout 1             | `513714d2457c`  |
| 3186   | Layout 1             | `513714d2457c`  |
| 3177   | Layout 1             | `513714d2457c`  |
| 3169   | Layout 1             | `513714d2457c`  |
| 3158   | Layout 1             | `513714d2457c`  |
| 3151   | Layout 1             | `513714d2457c`  |
| 3144   | Layout 1             | `513714d2457c`  |
| 3133   | Layout 1             | `513714d2457c`  |
| 3125   | Layout 1             | `513714d2457c`  |
| 3118   | Layout 1             | `513714d2457c`  |
| 3111   | Layout 1             | `513714d2457c`  |
| 3103   | Layout 1             | `513714d2457c`  |
| 3095   | Layout 1             | `513714d2457c`  |
| 3086   | Layout 1             | `513714d2457c`  |
| 3072   | Layout 1             | `513714d2457c`  |
| 3062   | Layout 1             | `513714d2457c`  |
| 3052   | Layout 1             | `513714d2457c`  |
| 3045   | Layout 1             | `513714d2457c`  |
| 3037   | Layout 1             | `513714d2457c`  |
| 3030   | Layout 1             | `513714d2457c`  |
| 3021   | Layout 1             | `513714d2457c`  |
| 3012   | Layout 1             | `513714d2457c`  |
| 3002   | Layout 1             | `513714d2457c`  |
| 2995   | Layout 1             | `513714d2457c`  |
| 2987   | Layout 1             | `513714d2457c`  |
| 2978   | Layout 1             | `513714d2457c`  |
| 2970   | Layout 1             | `513714d2457c`  |
| 2959   | Layout 1             | `513714d2457c`  |
| 2951   | Layout 1             | `513714d2457c`  |
| 2942   | Layout 1             | `513714d2457c`  |
| 2935   | Layout 1             | `513714d2457c`  |
| 2932   | Layout 1             | `513714d2457c`  |
| 2923   | Layout 1             | `513714d2457c`  |
| 2919   | Layout 1             | `513714d2457c`  |
| 2907   | Layout 1             | `513714d2457c`  |
| 2900   | Layout 1             | `513714d2457c`  |
| 2891   | Layout 1             | `513714d2457c`  |
| 2882   | Layout 1             | `513714d2457c`  |
| 2872   | Layout 1             | `513714d2457c`  |
| 2863   | Layout 1             | `513714d2457c`  |
| 2855   | Layout 1             | `513714d2457c`  |
| 2849   | Layout 1             | `513714d2457c`  |
| 2844   | Layout 1             | `513714d2457c`  |
| 2834   | Layout 1             | `513714d2457c`  |
| 2825   | Layout 1             | `513714d2457c`  |
| 2819   | Layout 1             | `513714d2457c`  |
| 2811   | Layout 1             | `513714d2457c`  |
| 2803   | Layout 1             | `513714d2457c`  |
| 2794   | Layout 1             | `513714d2457c`  |
| 2783   | Layout 1             | `513714d2457c`  |
| 2774   | Layout 1             | `513714d2457c`  |
| 2765   | Layout 1             | `513714d2457c`  |
| 2756   | Layout 1             | `513714d2457c`  |
| 2750   | Layout 1             | `513714d2457c`  |
| 2743   | Layout 1             | `513714d2457c`  |
| 2736   | Layout 1             | `513714d2457c`  |
| 2726   | Layout 1             | `513714d2457c`  |
| 2717   | Layout 1             | `513714d2457c`  |
| 2709   | Layout 1             | `513714d2457c`  |
| 2703   | Layout 1             | `513714d2457c`  |
| 2695   | Layout 1             | `513714d2457c`  |
| 2684   | Layout 1             | `513714d2457c`  |
| 2672   | Layout 1             | `513714d2457c`  |
| 2665   | Layout 1             | `513714d2457c`  |
| 2657   | Layout 1             | `513714d2457c`  |
| 2649   | Layout 1             | `513714d2457c`  |
| 2644   | Layout 1             | `513714d2457c`  |
| 2637   | Layout 1             | `513714d2457c`  |
| 2629   | Layout 1             | `513714d2457c`  |
| 2619   | Layout 1             | `513714d2457c`  |
| 2612   | Layout 1             | `513714d2457c`  |
| 2606   | Layout 1             | `513714d2457c`  |
| 2602   | Layout 1             | `513714d2457c`  |
| 2601   | Layout 1             | `513714d2457c`  |
| 2592   | Layout 1             | `513714d2457c`  |
| 2583   | Layout 1             | `513714d2457c`  |
| 2575   | Layout 1             | `513714d2457c`  |
| 2567   | Layout 1             | `513714d2457c`  |
| 2560   | Layout 1             | `513714d2457c`  |
| 2553   | Layout 1             | `513714d2457c`  |
| 2545   | Layout 1             | `513714d2457c`  |
| 2538   | Layout 1             | `513714d2457c`  |
| 2529   | Layout 1             | `513714d2457c`  |
| 2519   | Layout 1             | `513714d2457c`  |
| 2513   | Layout 1             | `513714d2457c`  |
| 2510   | Layout 1             | `513714d2457c`  |
| 2507   | Layout 1             | `513714d2457c`  |
| 2503   | Layout 1             | `513714d2457c`  |
| 2498   | Layout 1             | `513714d2457c`  |
| 2492   | Layout 1             | `513714d2457c`  |
| 2487   | Layout 1             | `513714d2457c`  |
| 2480   | Layout 1             | `513714d2457c`  |
| 2474   | Layout 1             | `513714d2457c`  |
| 2468   | Layout 1             | `513714d2457c`  |
| 2460   | Layout 1             | `513714d2457c`  |
| 2453   | Layout 1             | `513714d2457c`  |
| 2444   | Layout 1             | `513714d2457c`  |
| 2438   | Layout 1             | `513714d2457c`  |
| 2434   | Layout 1             | `513714d2457c`  |
| 2429   | Layout 1             | `513714d2457c`  |
| 2421   | Layout 1             | `513714d2457c`  |
| 2414   | Layout 1             | `513714d2457c`  |
| 2407   | Layout 1             | `513714d2457c`  |
| 2401   | Layout 1             | `513714d2457c`  |
| 2397   | Layout 1             | `513714d2457c`  |
| 2393   | Layout 1             | `513714d2457c`  |
| 2384   | Layout 1             | `513714d2457c`  |
| 2378   | Layout 1             | `513714d2457c`  |
| 2372   | Layout 1             | `513714d2457c`  |
| 2358   | Layout 1             | `513714d2457c`  |
| 2352   | Layout 1             | `513714d2457c`  |
| 2347   | Layout 1             | `513714d2457c`  |
| 2343   | Layout 1             | `513714d2457c`  |
| 2335   | Layout 1             | `513714d2457c`  |
| 2327   | Layout 1             | `513714d2457c`  |
| 2324   | Layout 1             | `513714d2457c`  |
| 2319   | Layout 1             | `513714d2457c`  |
| 2313   | Layout 1             | `513714d2457c`  |
| 2308   | Layout 1             | `513714d2457c`  |
| 2302   | Layout 1             | `513714d2457c`  |
| 2295   | Layout 1             | `513714d2457c`  |
| 2290   | Layout 1             | `513714d2457c`  |
| 2284   | Layout 1             | `513714d2457c`  |
| 2276   | Layout 1             | `513714d2457c`  |
| 2269   | Layout 1             | `513714d2457c`  |
| 2259   | Layout 1             | `513714d2457c`  |
| 2250   | Layout 1             | `513714d2457c`  |
| 2243   | Layout 1             | `513714d2457c`  |
| 2235   | Layout 1             | `513714d2457c`  |
| 2229   | Layout 1             | `513714d2457c`  |
| 2224   | Layout 1             | `513714d2457c`  |
| 2218   | Layout 1             | `513714d2457c`  |
| 2215   | Layout 1             | `513714d2457c`  |
| 2207   | Layout 1             | `513714d2457c`  |
| 2203   | Layout 1             | `513714d2457c`  |
| 2196   | Layout 1             | `513714d2457c`  |
| 2192   | Layout 1             | `513714d2457c`  |
| 2189   | Layout 1             | `513714d2457c`  |
| 2183   | Layout 1             | `513714d2457c`  |
| 2179   | Layout 1             | `513714d2457c`  |
| 2171   | Layout 1             | `513714d2457c`  |
| 2163   | Layout 1             | `513714d2457c`  |
| 2156   | Layout 1             | `513714d2457c`  |
| 2151   | Layout 1             | `513714d2457c`  |
| 2147   | Layout 1             | `513714d2457c`  |
| 2142   | Layout 1             | `513714d2457c`  |
| 2138   | Layout 1             | `513714d2457c`  |
| 2134   | Layout 1             | `513714d2457c`  |
| 2130   | Layout 1             | `513714d2457c`  |
| 2122   | Layout 1             | `513714d2457c`  |
| 2107   | Layout 1             | `513714d2457c`  |
| 2098   | Layout 1             | `513714d2457c`  |
| 2089   | Layout 1             | `513714d2457c`  |
| 2081   | Layout 1             | `513714d2457c`  |
| 2073   | Layout 1             | `513714d2457c`  |
| 2067   | Layout 1             | `513714d2457c`  |
| 2063   | Layout 1             | `513714d2457c`  |
| 2059   | Layout 1             | `513714d2457c`  |
| 2052   | Layout 1             | `513714d2457c`  |
| 2044   | Layout 1             | `513714d2457c`  |
| 2039   | Layout 1             | `513714d2457c`  |
| 2032   | Layout 1             | `513714d2457c`  |
| 2025   | Layout 1             | `513714d2457c`  |
| 2011   | Layout 1             | `513714d2457c`  |
| 2005   | No documented layout | `513714d2457c`  |
| 2000   | No file              | `513714d2457c`  |
| 1996   | No file              | `513714d2457c`  |
| 1991   | No file              | `513714d2457c`  |
| 1985   | No file              | `513714d2457c`  |
| 1980   | No file              | `513714d2457c`  |
| 1969   | No file              | `513714d2457c`  |
| 1964   | No file              | `513714d2457c`  |
| 1958   | No file              | `513714d2457c`  |
| 1950   | No file              | `513714d2457c`  |
| 1945   | No file              | `513714d2457c`  |
| 1937   | No file              | `513714d2457c`  |
| 1933   | No file              | `513714d2457c`  |
| 1927   | No file              | `513714d2457c`  |
| 1921   | No file              | `513714d2457c`  |
| 1914   | No file              | `513714d2457c`  |
| 1908   | No file              | `513714d2457c`  |
| 1897   | No file              | `513714d2457c`  |
| 1892   | No file              | `513714d2457c`  |
| 1886   | No file              | `513714d2457c`  |
| 1881   | No file              | `513714d2457c`  |
| 1871   | No file              | `513714d2457c`  |
| 1866   | No file              | `513714d2457c`  |
| 1862   | No file              | `513714d2457c`  |
| 1854   | No file              | `513714d2457c`  |
| 1846   | No file              | `513714d2457c`  |
| 1838   | No file              | `513714d2457c`  |
| 1832   | No file              | `513714d2457c`  |
| 1826   | No file              | `513714d2457c`  |
| 1822   | No file              | `513714d2457c`  |
| 1818   | No file              | `513714d2457c`  |
| 1804   | No file              | `513714d2457c`  |
| 1794   | No file              | `513714d2457c`  |
| 1790   | No file              | `513714d2457c`  |
| 1784   | No file              | `513714d2457c`  |
| 1774   | No file              | `513714d2457c`  |
| 1771   | No file              | `513714d2457c`  |
| 1762   | No file              | `513714d2457c`  |
| 1759   | No file              | `513714d2457c`  |
| 1754   | No file              | `513714d2457c`  |
| 1749   | No file              | `513714d2457c`  |
| 1743   | No file              | `513714d2457c`  |
| 1737   | No file              | `513714d2457c`  |
| 1731   | No file              | `513714d2457c`  |
| 1725   | No file              | `513714d2457c`  |
| 1717   | No file              | `513714d2457c`  |
| 1710   | No file              | `513714d2457c`  |
| 1704   | No file              | `513714d2457c`  |
| 1698   | No file              | `513714d2457c`  |
| 1690   | No file              | `513714d2457c`  |
| 1685   | No file              | `513714d2457c`  |
| 1680   | No file              | `513714d2457c`  |
| 1674   | No file              | `513714d2457c`  |
| 1668   | No file              | `513714d2457c`  |
| 1659   | No file              | `513714d2457c`  |
| 1649   | No file              | `513714d2457c`  |
| 1642   | No file              | `513714d2457c`  |
| 1636   | No file              | `513714d2457c`  |
| 1628   | No file              | `513714d2457c`  |
| 1622   | No file              | `513714d2457c`  |
| 1614   | No file              | `513714d2457c`  |
| 1608   | No file              | `513714d2457c`  |
| 1602   | No file              | `513714d2457c`  |
| 1598   | No file              | `513714d2457c`  |
| 1594   | No file              | `513714d2457c`  |
| 1590   | No file              | `513714d2457c`  |
| 1587   | No file              | `513714d2457c`  |
| 1584   | No file              | `513714d2457c`  |
| 1579   | No file              | `513714d2457c`  |
| 1572   | No file              | `513714d2457c`  |
| 1565   | No file              | `513714d2457c`  |
| 1559   | No file              | `513714d2457c`  |
| 1554   | No file              | `513714d2457c`  |
| 1547   | No file              | `513714d2457c`  |
| 1537   | No file              | `513714d2457c`  |
| 1529   | No file              | `513714d2457c`  |
| 1524   | No file              | `513714d2457c`  |
| 1519   | No file              | `513714d2457c`  |
| 1509   | No file              | `513714d2457c`  |
| 1506   | No file              | `513714d2457c`  |
| 1504   | No file              | `513714d2457c`  |
| 1500   | No file              | `513714d2457c`  |
| 1493   | No file              | `513714d2457c`  |
| 1489   | No file              | `513714d2457c`  |
| 1485   | No file              | `513714d2457c`  |
| 1481   | No file              | `513714d2457c`  |
| 1474   | No file              | `513714d2457c`  |
| 1466   | No file              | `513714d2457c`  |
| 1462   | No file              | `513714d2457c`  |
| 1459   | No file              | `513714d2457c`  |
| 1453   | No file              | `513714d2457c`  |
| 1450   | No file              | `513714d2457c`  |
| 1445   | No file              | `513714d2457c`  |
| 1439   | No file              | `513714d2457c`  |
| 1433   | No file              | `513714d2457c`  |
| 1430   | No file              | `513714d2457c`  |
| 1426   | No file              | `513714d2457c`  |
| 1421   | No file              | `513714d2457c`  |
| 1417   | No file              | `513714d2457c`  |
| 1416   | No file              | `513714d2457c`  |
| 1409   | No file              | `513714d2457c`  |
| 1405   | No file              | `513714d2457c`  |
| 1401   | No file              | `513714d2457c`  |
| 1396   | No file              | `513714d2457c`  |
| 1391   | No file              | `513714d2457c`  |
| 1390   | No file              | `513714d2457c`  |
| 1386   | No file              | `513714d2457c`  |
| 1381   | No file              | `513714d2457c`  |
| 1379   | No file              | `513714d2457c`  |
| 1372   | No file              | `513714d2457c`  |
| 1366   | No file              | `513714d2457c`  |
| 1364   | No file              | `513714d2457c`  |
| 1363   | No file              | `513714d2457c`  |
| 1360   | No file              | `513714d2457c`  |
| 1358   | No file              | `513714d2457c`  |
| 1355   | No file              | `513714d2457c`  |
| 1351   | No file              | `513714d2457c`  |
| 1348   | No file              | `513714d2457c`  |
| 1346   | No file              | `513714d2457c`  |
| 1341   | No file              | `513714d2457c`  |
| 1340   | No file              | `513714d2457c`  |
| 1338   | No file              | `513714d2457c`  |
| 1335   | No file              | `513714d2457c`  |
| 1333   | No file              | `513714d2457c`  |
| 1329   | No file              | `513714d2457c`  |
| 1327   | No file              | `513714d2457c`  |
| 1324   | No file              | `513714d2457c`  |
| 1321   | No file              | `513714d2457c`  |
| 1319   | No file              | `513714d2457c`  |
| 1318   | No file              | `513714d2457c`  |
| 1316   | No file              | `513714d2457c`  |
| 1313   | No file              | `513714d2457c`  |
| 1311   | No file              | `513714d2457c`  |
| 1309   | No file              | `513714d2457c`  |
| 1304   | No file              | `513714d2457c`  |
| 1292   | No file              | `513714d2457c`  |
| 1286   | No file              | `513714d2457c`  |
| 1280   | No file              | `513714d2457c`  |
| 1276   | No file              | `513714d2457c`  |
| 1267   | No file              | `513714d2457c`  |
| 1261   | No file              | `513714d2457c`  |
| 1256   | No file              | `513714d2457c`  |
| 1250   | No file              | `513714d2457c`  |
| 1246   | No file              | `513714d2457c`  |
| 1239   | No file              | `513714d2457c`  |
| 1230   | No file              | `513714d2457c`  |
| 1226   | No file              | `513714d2457c`  |
| 1220   | No file              | `513714d2457c`  |
| 1217   | No file              | `513714d2457c`  |
| 1211   | No file              | `513714d2457c`  |
| 1210   | No file              | `513714d2457c`  |
| 1208   | No file              | `513714d2457c`  |
| 1203   | No file              | `513714d2457c`  |
| 1197   | No file              | `513714d2457c`  |
| 1194   | No file              | `513714d2457c`  |
| 1192   | No file              | `513714d2457c`  |
| 1187   | No file              | `513714d2457c`  |
| 1183   | No file              | `513714d2457c`  |
| 1177   | No file              | `513714d2457c`  |
| 1173   | No file              | `513714d2457c`  |
| 1167   | No file              | `513714d2457c`  |
| 1164   | No file              | `513714d2457c`  |
| 1156   | No file              | `513714d2457c`  |
| 1149   | No file              | `513714d2457c`  |
| 1144   | No file              | `513714d2457c`  |
| 1137   | No file              | `513714d2457c`  |
| 1132   | No file              | `513714d2457c`  |
| 1127   | No file              | `513714d2457c`  |
| 1122   | No file              | `513714d2457c`  |
| 1118   | No file              | `513714d2457c`  |
| 1114   | No file              | `513714d2457c`  |
| 1109   | No file              | `513714d2457c`  |
| 1102   | No file              | `513714d2457c`  |
| 1096   | No file              | `513714d2457c`  |
| 1088   | No file              | `513714d2457c`  |
| 1081   | No file              | `513714d2457c`  |
| 1076   | No file              | `513714d2457c`  |
| 1069   | No file              | `513714d2457c`  |
| 1064   | No file              | `513714d2457c`  |
| 1058   | No file              | `513714d2457c`  |
| 1051   | No file              | `513714d2457c`  |
| 1044   | No file              | `513714d2457c`  |
| 1036   | No file              | `513714d2457c`  |
| 1026   | No file              | `513714d2457c`  |
| 1016   | No file              | `513714d2457c`  |
| 1009   | No file              | `513714d2457c`  |
| 1005   | No file              | `513714d2457c`  |
| 1000   | No file              | `513714d2457c`  |
| 998    | No file              | `513714d2457c`  |
| 990    | No file              | `513714d2457c`  |
| 979    | No file              | `513714d2457c`  |
| 972    | No file              | `513714d2457c`  |
| 963    | No file              | `513714d2457c`  |
| 955    | No file              | `513714d2457c`  |
| 946    | No file              | `513714d2457c`  |
| 938    | No file              | `513714d2457c`  |
| 927    | No file              | `513714d2457c`  |
| 911    | No file              | `513714d2457c`  |
| 904    | No file              | `513714d2457c`  |
| 899    | No file              | `513714d2457c`  |
| 894    | No file              | `513714d2457c`  |
| 885    | No file              | `513714d2457c`  |
| 879    | No file              | `513714d2457c`  |
| 872    | No file              | `513714d2457c`  |
| 864    | No file              | `513714d2457c`  |
| 855    | No file              | `513714d2457c`  |
| 853    | No file              | `513714d2457c`  |
| 845    | No file              | `513714d2457c`  |
| 837    | No file              | `513714d2457c`  |
| 829    | No file              | `513714d2457c`  |
| 822    | No file              | `513714d2457c`  |
| 814    | No file              | `513714d2457c`  |
| 805    | No file              | `513714d2457c`  |
| 794    | No file              | `513714d2457c`  |
| 787    | No file              | `513714d2457c`  |
| 780    | No file              | `513714d2457c`  |
| 771    | No file              | `513714d2457c`  |
| 760    | No file              | `513714d2457c`  |
| 748    | No file              | `513714d2457c`  |
| 741    | No file              | `513714d2457c`  |
| 736    | No file              | `513714d2457c`  |
| 731    | No file              | `513714d2457c`  |
| 723    | No file              | `513714d2457c`  |
| 711    | No file              | `513714d2457c`  |
| 707    | No file              | `513714d2457c`  |
| 697    | No file              | `513714d2457c`  |
| 689    | No file              | `513714d2457c`  |
| 683    | No file              | `513714d2457c`  |
| 678    | No file              | `513714d2457c`  |
| 670    | No file              | `513714d2457c`  |
| 661    | No file              | `513714d2457c`  |
| 656    | No file              | `513714d2457c`  |
| 652    | No file              | `513714d2457c`  |
| 643    | No file              | `513714d2457c`  |
| 637    | No file              | `513714d2457c`  |
| 630    | No file              | `513714d2457c`  |
| 627    | No file              | `513714d2457c`  |
| 621    | No file              | `513714d2457c`  |
| 617    | No file              | `513714d2457c`  |
| 615    | No file              | `513714d2457c`  |
| 606    | No file              | `513714d2457c`  |
| 599    | No file              | `513714d2457c`  |
| 592    | No file              | `513714d2457c`  |
| 586    | No file              | `513714d2457c`  |
| 577    | No file              | `513714d2457c`  |
| 569    | No file              | `513714d2457c`  |
| 561    | No file              | `513714d2457c`  |
| 554    | No file              | `513714d2457c`  |
| 542    | No file              | `513714d2457c`  |
| 532    | No file              | `513714d2457c`  |
| 531    | No file              | `513714d2457c`  |
| 526    | No file              | `513714d2457c`  |
| 521    | No file              | `513714d2457c`  |
| 517    | No file              | `513714d2457c`  |
| 510    | No file              | `513714d2457c`  |
| 508    | No file              | `513714d2457c`  |
| 504    | No file              | `513714d2457c`  |
| 497    | No file              | `513714d2457c`  |
| 491    | No file              | `513714d2457c`  |
| 485    | No file              | `513714d2457c`  |
| 478    | No file              | `513714d2457c`  |
| 472    | No file              | `513714d2457c`  |
| 466    | No file              | `513714d2457c`  |
| 457    | No file              | `513714d2457c`  |
| 452    | No file              | `513714d2457c`  |
| 449    | No file              | `513714d2457c`  |
| 435    | No file              | `513714d2457c`  |

<!-- versions:end -->

## Companion Files

None. The handler names the equipment slot with its item tooltip label
and each item with its LOC type 0 name from `languagedata_*.loc` when it
is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

### Row (variable: 5 bytes + presets)

| Offset  | Type                   | Field        | Notes                                                                      |
| ------- | ---------------------- | ------------ | -------------------------------------------------------------------------- |
| `+0x00` | u8                     | equip_slot   | `__eEquipSlotNo*` value, the `equip_slot` of `itemenchant.dbss`; unique per row |
| `+0x01` | u32                    | preset_count | Number of `presets`                                                        |
| `+0x05` | Preset[preset_count]   | presets      | See Preset                                                                 |

### Preset (19 bytes)

| Offset  | Type | Field          | Notes                                                                       |
| ------- | ---- | -------------- | --------------------------------------------------------------------------- |
| `+0x00` | u8   | class_type     | Class type (`0` Warrior, LOC type 21), or `101` on the presets for every class |
| `+0x01` | u8   | unknown_01     | Equals the row's `equip_slot` on every preset; see Open Questions          |
| `+0x02` | u8   | unknown_02     | `0` on every client checked                                                 |
| `+0x03` | u32  | item_key       | Item key: `enchant_level << 24 \| item_id`; level `0` on every preset        |
| `+0x07` | i32  | unknown_07     | `-1` on every client checked                                                |
| `+0x0B` | u64  | abyss_coin     | Coin price of the preset; `0` on every client checked                       |

## Slots

Client 3482, in file order: each slot's item tooltip label and its
presets.

| `equip_slot` | Slot             | Presets                                                                      |
| ------------ | ---------------- | ---------------------------------------------------------------------------- |
| 12           | Belt             | `101` Belt of Instinct                                                       |
| 11, 10       | Earring          | `101` Earring of Change                                                      |
| 9, 8         | Ring             | `101` Ring of Fate                                                           |
| 7            | Necklace         | `101` Necklace of Spacetime                                                  |
| 6            | Helmet           | `101` Helmet of Reverie, `101` HAN Combined Magic Crystal - Hoom             |
| 5            | Shoes            | `101` Shoes of Flight, `101` Ancient Magic Crystal of Nature - Adamantine    |
| 4            | Gloves           | `101` Gloves of Resolve, `101` JIN Magic Crystal - Viper                     |
| 3            | Armor            | `101` Armor of Balance, `101` Magic Crystal of Infinity - Max HP             |
| 1            | Sub-weapon       | 32 class types (Shield of Harmony for Warrior), then `101` Magic Crystal of Infinity - Critical Hit |
| 0            | Main Weapon      | 32 class types (Longsword of the Challenger for Warrior), then `101` Crystal of Elkarr |
| 29           | Awakening Weapon | 31 class types (Greatsword of Serenity for Warrior), then `101` HAN Combined Magic Crystal - Hoom |
| 27           | Alchemy Stone    | `101` Rift's Alchemy Stone                                                   |

## Field Names

The Magnus is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`Abyss` in its name. The names come from the client Lua (client 3482):
`ToClient_GetAbyssOnePresetStaticStatus` takes the equip slot, the class
type and the preset's index, and the Lua shows the item of
`getEquipItemKey()` (an item key it passes to
`getItemEnchantStaticStatus`) and the price of `getAbyssCoin()`, an s64
that the u64 `abyss_coin` holds; a price of `0` marks a basic item there
(`isBasicItem = needCoin_s64 <= 0`). `equip_slot` values match the
tooltip slot of each item (Belt `12`, Helmet `6`, Main Weapon `0`). On
client 3482 the `class_type` values of the main and sub-weapon slots are
the 32 class types `0` to `35` without `13`, `14`, `18` and `22`, each
with its own weapon; the awakening weapon slot lacks `35`.

## Notes

- The Lua passes `__eClassType_Count` as the class type for every slot
  except the main, sub and awakening weapons, where it passes the
  player's class; the file stores `101` exactly on those slots and on the
  crystals that close the weapon lists.
- The weapon lists grow with the clients as classes were added: 26, 26
  and 25 presets on client 2107, 33, 33 and 32 on client 3474.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/abyssone_tables.py`: the
  slot with its label, then each preset as class, item name and item ID,
  with the coin price when it is not `0`.

## Open Questions

### How the Client Tells Crystals From Gear

`ToClient_GetAbyssOnePresetStaticStatus` takes an `isSocket` flag, but no
preset field marks a crystal: the Magic Crystals sit in the same lists as
the gear with the same `unknown_07` `-1` and class `101`. The item type
of the item key may decide it; `unknown_07` is `-1` on every preset of
every client checked.

### Why Each Preset Repeats Its Slot

`unknown_01` equals the row's `equip_slot` on every preset of every
client checked, and `unknown_02` after it is always `0`. The two bytes may
be one u16 slot number of the preset; the Lua reads neither.
