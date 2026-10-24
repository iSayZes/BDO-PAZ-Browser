# `intimacyinfo.bss` Format

## Purpose

The amity list of the NPC dialog window: per NPC character the entries it
unlocks at an amity value, each a quest, a shop, a knowledge or a talk. The
dialog Lua (`panel_dialog_intimacy_all_1.luac`) reads them through
`getIntimacyInformationCount(characterKey)` and
`getIntimacyInformation(characterKey, index)` and the getters
`getIntimacy()`, `getTypeIndex()`, `getOperatorType()`, `getQuestNo()`,
`getMentalCardKeyRaw()` and `getDialogIndex()`, and shows each entry as
`<type name> : <description> (<operator> <amity>)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records           | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | ----------------- | --------- |
| 1      | 1109 and later | 3483    | `intimacyinfo.bss` | 22,028 | 765 Info, 353 Row | 26        |

| Layout | File               | Known            | Unknown         |
| ------ | ------------------ | ---------------- | --------------- |
| 1      | `intimacyinfo.bss` | 18,968 B (86.1%) | 3,060 B (13.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `b222d466e128`  |
| 3482   | Layout 1             | `b222d466e128`  |
| 3474   | Layout 1             | `b222d466e128`  |
| 3473   | Layout 1             | `b222d466e128`  |
| 3464   | Layout 1             | `b222d466e128`  |
| 3458   | Layout 1             | `b222d466e128`  |
| 3454   | Layout 1             | `b222d466e128`  |
| 3444   | Layout 1             | `b222d466e128`  |
| 3435   | Layout 1             | `b222d466e128`  |
| 3426   | Layout 1             | `b222d466e128`  |
| 3418   | Layout 1             | `b222d466e128`  |
| 3412   | Layout 1             | `b222d466e128`  |
| 3402   | Layout 1             | `b222d466e128`  |
| 3396   | Layout 1             | `b222d466e128`  |
| 3387   | Layout 1             | `b222d466e128`  |
| 3381   | Layout 1             | `b222d466e128`  |
| 3373   | Layout 1             | `b222d466e128`  |
| 3364   | Layout 1             | `b222d466e128`  |
| 3356   | Layout 1             | `b222d466e128`  |
| 3349   | Layout 1             | `b222d466e128`  |
| 3342   | Layout 1             | `b222d466e128`  |
| 3335   | Layout 1             | `b222d466e128`  |
| 3326   | Layout 1             | `b222d466e128`  |
| 3321   | Layout 1             | `b222d466e128`  |
| 3314   | Layout 1             | `b222d466e128`  |
| 3303   | Layout 1             | `b222d466e128`  |
| 3302   | Layout 1             | `b222d466e128`  |
| 3293   | Layout 1             | `b222d466e128`  |
| 3283   | Layout 1             | `b222d466e128`  |
| 3275   | Layout 1             | `b222d466e128`  |
| 3267   | Layout 1             | `b222d466e128`  |
| 3258   | Layout 1             | `b222d466e128`  |
| 3251   | Layout 1             | `b222d466e128`  |
| 3242   | Layout 1             | `b222d466e128`  |
| 3235   | Layout 1             | `b222d466e128`  |
| 3229   | Layout 1             | `b222d466e128`  |
| 3212   | Layout 1             | `b222d466e128`  |
| 3203   | Layout 1             | `b222d466e128`  |
| 3193   | Layout 1             | `b222d466e128`  |
| 3186   | Layout 1             | `b222d466e128`  |
| 3177   | Layout 1             | `b222d466e128`  |
| 3169   | Layout 1             | `b222d466e128`  |
| 3158   | Layout 1             | `b222d466e128`  |
| 3151   | Layout 1             | `b222d466e128`  |
| 3144   | Layout 1             | `b222d466e128`  |
| 3133   | Layout 1             | `b222d466e128`  |
| 3125   | Layout 1             | `b222d466e128`  |
| 3118   | Layout 1             | `b222d466e128`  |
| 3111   | Layout 1             | `b222d466e128`  |
| 3103   | Layout 1             | `b222d466e128`  |
| 3095   | Layout 1             | `b222d466e128`  |
| 3086   | Layout 1             | `b222d466e128`  |
| 3072   | Layout 1             | `b222d466e128`  |
| 3062   | Layout 1             | `b222d466e128`  |
| 3052   | Layout 1             | `b222d466e128`  |
| 3045   | Layout 1             | `b222d466e128`  |
| 3037   | Layout 1             | `b222d466e128`  |
| 3030   | Layout 1             | `b222d466e128`  |
| 3021   | Layout 1             | `b222d466e128`  |
| 3012   | Layout 1             | `b222d466e128`  |
| 3002   | Layout 1             | `b222d466e128`  |
| 2995   | Layout 1             | `b222d466e128`  |
| 2987   | Layout 1             | `b222d466e128`  |
| 2978   | Layout 1             | `b222d466e128`  |
| 2970   | Layout 1             | `b222d466e128`  |
| 2959   | Layout 1             | `b222d466e128`  |
| 2951   | Layout 1             | `b222d466e128`  |
| 2942   | Layout 1             | `b222d466e128`  |
| 2935   | Layout 1             | `b222d466e128`  |
| 2932   | Layout 1             | `b222d466e128`  |
| 2923   | Layout 1             | `b222d466e128`  |
| 2919   | Layout 1             | `b222d466e128`  |
| 2907   | Layout 1             | `b222d466e128`  |
| 2900   | Layout 1             | `b222d466e128`  |
| 2891   | Layout 1             | `b222d466e128`  |
| 2882   | Layout 1             | `b222d466e128`  |
| 2872   | Layout 1             | `b222d466e128`  |
| 2863   | Layout 1             | `b222d466e128`  |
| 2855   | Layout 1             | `b222d466e128`  |
| 2849   | Layout 1             | `b222d466e128`  |
| 2844   | Layout 1             | `b222d466e128`  |
| 2834   | Layout 1             | `b222d466e128`  |
| 2825   | Layout 1             | `b222d466e128`  |
| 2819   | Layout 1             | `b222d466e128`  |
| 2811   | Layout 1             | `b222d466e128`  |
| 2803   | Layout 1             | `b222d466e128`  |
| 2794   | Layout 1             | `b222d466e128`  |
| 2783   | Layout 1             | `b222d466e128`  |
| 2774   | Layout 1             | `b222d466e128`  |
| 2765   | Layout 1             | `b222d466e128`  |
| 2756   | Layout 1             | `b222d466e128`  |
| 2750   | Layout 1             | `b222d466e128`  |
| 2743   | Layout 1             | `b222d466e128`  |
| 2736   | Layout 1             | `b222d466e128`  |
| 2726   | Layout 1             | `b222d466e128`  |
| 2717   | Layout 1             | `b222d466e128`  |
| 2709   | Layout 1             | `b222d466e128`  |
| 2703   | Layout 1             | `b222d466e128`  |
| 2695   | Layout 1             | `b222d466e128`  |
| 2684   | Layout 1             | `b222d466e128`  |
| 2672   | Layout 1             | `b222d466e128`  |
| 2665   | Layout 1             | `b222d466e128`  |
| 2657   | Layout 1             | `b222d466e128`  |
| 2649   | Layout 1             | `b222d466e128`  |
| 2644   | Layout 1             | `b222d466e128`  |
| 2637   | Layout 1             | `b222d466e128`  |
| 2629   | Layout 1             | `b222d466e128`  |
| 2619   | Layout 1             | `b222d466e128`  |
| 2612   | Layout 1             | `b222d466e128`  |
| 2606   | Layout 1             | `b222d466e128`  |
| 2602   | Layout 1             | `b222d466e128`  |
| 2601   | Layout 1             | `b222d466e128`  |
| 2592   | Layout 1             | `b222d466e128`  |
| 2583   | Layout 1             | `b222d466e128`  |
| 2575   | Layout 1             | `b222d466e128`  |
| 2567   | Layout 1             | `b222d466e128`  |
| 2560   | Layout 1             | `b222d466e128`  |
| 2553   | Layout 1             | `b222d466e128`  |
| 2545   | Layout 1             | `b222d466e128`  |
| 2538   | Layout 1             | `b222d466e128`  |
| 2529   | Layout 1             | `b222d466e128`  |
| 2519   | Layout 1             | `b222d466e128`  |
| 2513   | Layout 1             | `b222d466e128`  |
| 2510   | Layout 1             | `b222d466e128`  |
| 2507   | Layout 1             | `b222d466e128`  |
| 2503   | Layout 1             | `b222d466e128`  |
| 2498   | Layout 1             | `b222d466e128`  |
| 2492   | Layout 1             | `b222d466e128`  |
| 2487   | Layout 1             | `b222d466e128`  |
| 2480   | Layout 1             | `b222d466e128`  |
| 2474   | Layout 1             | `b222d466e128`  |
| 2468   | Layout 1             | `b222d466e128`  |
| 2460   | Layout 1             | `b222d466e128`  |
| 2453   | Layout 1             | `b222d466e128`  |
| 2444   | Layout 1             | `b222d466e128`  |
| 2438   | Layout 1             | `b222d466e128`  |
| 2434   | Layout 1             | `b222d466e128`  |
| 2429   | Layout 1             | `b222d466e128`  |
| 2421   | Layout 1             | `b222d466e128`  |
| 2414   | Layout 1             | `b222d466e128`  |
| 2407   | Layout 1             | `b222d466e128`  |
| 2401   | Layout 1             | `b222d466e128`  |
| 2397   | Layout 1             | `b222d466e128`  |
| 2393   | Layout 1             | `b222d466e128`  |
| 2384   | Layout 1             | `b222d466e128`  |
| 2378   | Layout 1             | `b222d466e128`  |
| 2372   | Layout 1             | `b222d466e128`  |
| 2358   | Layout 1             | `b222d466e128`  |
| 2352   | Layout 1             | `b222d466e128`  |
| 2347   | Layout 1             | `b222d466e128`  |
| 2343   | Layout 1             | `b222d466e128`  |
| 2335   | Layout 1             | `b222d466e128`  |
| 2327   | Layout 1             | `b222d466e128`  |
| 2324   | Layout 1             | `b222d466e128`  |
| 2319   | Layout 1             | `b222d466e128`  |
| 2313   | Layout 1             | `b222d466e128`  |
| 2308   | Layout 1             | `b222d466e128`  |
| 2302   | Layout 1             | `b222d466e128`  |
| 2295   | Layout 1             | `b222d466e128`  |
| 2290   | Layout 1             | `b222d466e128`  |
| 2284   | Layout 1             | `b222d466e128`  |
| 2276   | Layout 1             | `b222d466e128`  |
| 2269   | Layout 1             | `b222d466e128`  |
| 2259   | Layout 1             | `b222d466e128`  |
| 2250   | Layout 1             | `b222d466e128`  |
| 2243   | Layout 1             | `b222d466e128`  |
| 2235   | Layout 1             | `b222d466e128`  |
| 2229   | Layout 1             | `b222d466e128`  |
| 2224   | Layout 1             | `b222d466e128`  |
| 2218   | Layout 1             | `b222d466e128`  |
| 2215   | Layout 1             | `b222d466e128`  |
| 2207   | Layout 1             | `b222d466e128`  |
| 2203   | Layout 1             | `b222d466e128`  |
| 2196   | Layout 1             | `b222d466e128`  |
| 2192   | Layout 1             | `b222d466e128`  |
| 2189   | Layout 1             | `b222d466e128`  |
| 2183   | Layout 1             | `b222d466e128`  |
| 2179   | Layout 1             | `b222d466e128`  |
| 2171   | Layout 1             | `b222d466e128`  |
| 2163   | Layout 1             | `b222d466e128`  |
| 2156   | Layout 1             | `b222d466e128`  |
| 2151   | Layout 1             | `b222d466e128`  |
| 2147   | Layout 1             | `b222d466e128`  |
| 2142   | Layout 1             | `b222d466e128`  |
| 2138   | Layout 1             | `b222d466e128`  |
| 2134   | Layout 1             | `b222d466e128`  |
| 2130   | Layout 1             | `b222d466e128`  |
| 2122   | Layout 1             | `b222d466e128`  |
| 2107   | Layout 1             | `b222d466e128`  |
| 2098   | Layout 1             | `b222d466e128`  |
| 2089   | Layout 1             | `b222d466e128`  |
| 2081   | Layout 1             | `b222d466e128`  |
| 2073   | Layout 1             | `b222d466e128`  |
| 2067   | Layout 1             | `b222d466e128`  |
| 2063   | Layout 1             | `b222d466e128`  |
| 2059   | Layout 1             | `b222d466e128`  |
| 2052   | Layout 1             | `b222d466e128`  |
| 2044   | Layout 1             | `b222d466e128`  |
| 2039   | Layout 1             | `b222d466e128`  |
| 2032   | Layout 1             | `b222d466e128`  |
| 2025   | Layout 1             | `b222d466e128`  |
| 2011   | Layout 1             | `b222d466e128`  |
| 2005   | Layout 1             | `b222d466e128`  |
| 2000   | Layout 1             | `b222d466e128`  |
| 1996   | Layout 1             | `b222d466e128`  |
| 1991   | Layout 1             | `b222d466e128`  |
| 1985   | Layout 1             | `b222d466e128`  |
| 1980   | Layout 1             | `b222d466e128`  |
| 1969   | Layout 1             | `b222d466e128`  |
| 1964   | Layout 1             | `b222d466e128`  |
| 1958   | Layout 1             | `b222d466e128`  |
| 1950   | Layout 1             | `b222d466e128`  |
| 1945   | Layout 1             | `b222d466e128`  |
| 1937   | Layout 1             | `b222d466e128`  |
| 1933   | Layout 1             | `b222d466e128`  |
| 1927   | Layout 1             | `b222d466e128`  |
| 1921   | Layout 1             | `b222d466e128`  |
| 1914   | Layout 1             | `b222d466e128`  |
| 1908   | Layout 1             | `b222d466e128`  |
| 1897   | Layout 1             | `b222d466e128`  |
| 1892   | Layout 1             | `b222d466e128`  |
| 1886   | Layout 1             | `b222d466e128`  |
| 1881   | Layout 1             | `b222d466e128`  |
| 1871   | Layout 1             | `b222d466e128`  |
| 1866   | Layout 1             | `b222d466e128`  |
| 1862   | Layout 1             | `b222d466e128`  |
| 1854   | Layout 1             | `b222d466e128`  |
| 1846   | Layout 1             | `b222d466e128`  |
| 1838   | Layout 1             | `b222d466e128`  |
| 1832   | Layout 1             | `b222d466e128`  |
| 1826   | Layout 1             | `b222d466e128`  |
| 1822   | Layout 1             | `b222d466e128`  |
| 1818   | Layout 1             | `b222d466e128`  |
| 1804   | Layout 1             | `b222d466e128`  |
| 1794   | Layout 1             | `b222d466e128`  |
| 1790   | Layout 1             | `b222d466e128`  |
| 1784   | Layout 1             | `b222d466e128`  |
| 1774   | Layout 1             | `b222d466e128`  |
| 1771   | Layout 1             | `b222d466e128`  |
| 1762   | Layout 1             | `b222d466e128`  |
| 1759   | Layout 1             | `b222d466e128`  |
| 1754   | Layout 1             | `b222d466e128`  |
| 1749   | Layout 1             | `b222d466e128`  |
| 1743   | Layout 1             | `b222d466e128`  |
| 1737   | Layout 1             | `b222d466e128`  |
| 1731   | Layout 1             | `b222d466e128`  |
| 1725   | Layout 1             | `b222d466e128`  |
| 1717   | Layout 1             | `b222d466e128`  |
| 1710   | Layout 1             | `b222d466e128`  |
| 1704   | Layout 1             | `b222d466e128`  |
| 1698   | Layout 1             | `b222d466e128`  |
| 1690   | Layout 1             | `b222d466e128`  |
| 1685   | Layout 1             | `b222d466e128`  |
| 1680   | Layout 1             | `b222d466e128`  |
| 1674   | Layout 1             | `b222d466e128`  |
| 1668   | Layout 1             | `b222d466e128`  |
| 1659   | Layout 1             | `b222d466e128`  |
| 1649   | Layout 1             | `b222d466e128`  |
| 1642   | Layout 1             | `b222d466e128`  |
| 1636   | Layout 1             | `b222d466e128`  |
| 1628   | Layout 1             | `b222d466e128`  |
| 1622   | Layout 1             | `b222d466e128`  |
| 1614   | Layout 1             | `b222d466e128`  |
| 1608   | Layout 1             | `b222d466e128`  |
| 1602   | Layout 1             | `b222d466e128`  |
| 1598   | Layout 1             | `b222d466e128`  |
| 1594   | Layout 1             | `b222d466e128`  |
| 1590   | Layout 1             | `b222d466e128`  |
| 1587   | Layout 1             | `b222d466e128`  |
| 1584   | Layout 1             | `b222d466e128`  |
| 1579   | Layout 1             | `b222d466e128`  |
| 1572   | Layout 1             | `b222d466e128`  |
| 1565   | Layout 1             | `b222d466e128`  |
| 1559   | Layout 1             | `b222d466e128`  |
| 1554   | Layout 1             | `b222d466e128`  |
| 1547   | Layout 1             | `b222d466e128`  |
| 1537   | Layout 1             | `b222d466e128`  |
| 1529   | Layout 1             | `b222d466e128`  |
| 1524   | Layout 1             | `b222d466e128`  |
| 1519   | Layout 1             | `b222d466e128`  |
| 1509   | Layout 1             | `b222d466e128`  |
| 1506   | Layout 1             | `b222d466e128`  |
| 1504   | Layout 1             | `b222d466e128`  |
| 1500   | Layout 1             | `b222d466e128`  |
| 1493   | Layout 1             | `b222d466e128`  |
| 1489   | Layout 1             | `b222d466e128`  |
| 1485   | Layout 1             | `b222d466e128`  |
| 1481   | Layout 1             | `b222d466e128`  |
| 1474   | Layout 1             | `b222d466e128`  |
| 1466   | Layout 1             | `b222d466e128`  |
| 1462   | Layout 1             | `b222d466e128`  |
| 1459   | Layout 1             | `b222d466e128`  |
| 1453   | Layout 1             | `b222d466e128`  |
| 1450   | Layout 1             | `b222d466e128`  |
| 1445   | Layout 1             | `b222d466e128`  |
| 1439   | Layout 1             | `b222d466e128`  |
| 1433   | Layout 1             | `b222d466e128`  |
| 1430   | Layout 1             | `b222d466e128`  |
| 1426   | Layout 1             | `b222d466e128`  |
| 1421   | Layout 1             | `b222d466e128`  |
| 1417   | Layout 1             | `b222d466e128`  |
| 1416   | Layout 1             | `b222d466e128`  |
| 1409   | Layout 1             | `b222d466e128`  |
| 1405   | Layout 1             | `b222d466e128`  |
| 1401   | Layout 1             | `b222d466e128`  |
| 1396   | Layout 1             | `b222d466e128`  |
| 1391   | Layout 1             | `b222d466e128`  |
| 1390   | Layout 1             | `b222d466e128`  |
| 1386   | Layout 1             | `b222d466e128`  |
| 1381   | Layout 1             | `b222d466e128`  |
| 1379   | Layout 1             | `b222d466e128`  |
| 1372   | Layout 1             | `b222d466e128`  |
| 1366   | Layout 1             | `b222d466e128`  |
| 1364   | Layout 1             | `b222d466e128`  |
| 1363   | Layout 1             | `b222d466e128`  |
| 1360   | Layout 1             | `b222d466e128`  |
| 1358   | Layout 1             | `b222d466e128`  |
| 1355   | Layout 1             | `b222d466e128`  |
| 1351   | Layout 1             | `b222d466e128`  |
| 1348   | Layout 1             | `b222d466e128`  |
| 1346   | Layout 1             | `b222d466e128`  |
| 1341   | Layout 1             | `b222d466e128`  |
| 1340   | Layout 1             | `b222d466e128`  |
| 1338   | Layout 1             | `b222d466e128`  |
| 1335   | Layout 1             | `b222d466e128`  |
| 1333   | Layout 1             | `b222d466e128`  |
| 1329   | Layout 1             | `b222d466e128`  |
| 1327   | Layout 1             | `b222d466e128`  |
| 1324   | Layout 1             | `b222d466e128`  |
| 1321   | Layout 1             | `b222d466e128`  |
| 1319   | Layout 1             | `b222d466e128`  |
| 1318   | Layout 1             | `b222d466e128`  |
| 1316   | Layout 1             | `b222d466e128`  |
| 1313   | Layout 1             | `b222d466e128`  |
| 1311   | Layout 1             | `b222d466e128`  |
| 1309   | Layout 1             | `b222d466e128`  |
| 1304   | Layout 1             | `b222d466e128`  |
| 1292   | Layout 1             | `b222d466e128`  |
| 1286   | Layout 1             | `b222d466e128`  |
| 1280   | Layout 1             | `b222d466e128`  |
| 1276   | Layout 1             | `b222d466e128`  |
| 1267   | Layout 1             | `b222d466e128`  |
| 1261   | Layout 1             | `b222d466e128`  |
| 1256   | Layout 1             | `b222d466e128`  |
| 1250   | Layout 1             | `b222d466e128`  |
| 1246   | Layout 1             | `b222d466e128`  |
| 1239   | Layout 1             | `b222d466e128`  |
| 1230   | Layout 1             | `b222d466e128`  |
| 1226   | Layout 1             | `b222d466e128`  |
| 1220   | Layout 1             | `b222d466e128`  |
| 1217   | Layout 1             | `b222d466e128`  |
| 1211   | Layout 1             | `b222d466e128`  |
| 1210   | Layout 1             | `b222d466e128`  |
| 1208   | Layout 1             | `b222d466e128`  |
| 1203   | Layout 1             | `b222d466e128`  |
| 1197   | Layout 1             | `b222d466e128`  |
| 1194   | Layout 1             | `b222d466e128`  |
| 1192   | Layout 1             | `b222d466e128`  |
| 1187   | Layout 1             | `b222d466e128`  |
| 1183   | Layout 1             | `b222d466e128`  |
| 1177   | Layout 1             | `b222d466e128`  |
| 1173   | Layout 1             | `b222d466e128`  |
| 1167   | Layout 1             | `b222d466e128`  |
| 1164   | Layout 1             | `b222d466e128`  |
| 1156   | Layout 1             | `b222d466e128`  |
| 1149   | Layout 1             | `b222d466e128`  |
| 1144   | Layout 1             | `b222d466e128`  |
| 1137   | Layout 1             | `b222d466e128`  |
| 1132   | Layout 1             | `b222d466e128`  |
| 1127   | Layout 1             | `b222d466e128`  |
| 1122   | Layout 1             | `b222d466e128`  |
| 1118   | Layout 1             | `b222d466e128`  |
| 1114   | Layout 1             | `b222d466e128`  |
| 1109   | Layout 1             | `b222d466e128`  |
| 1102   | No file              | `b222d466e128`  |
| 1096   | No file              | `b222d466e128`  |
| 1088   | No file              | `b222d466e128`  |
| 1081   | No file              | `b222d466e128`  |
| 1076   | No file              | `b222d466e128`  |
| 1069   | No file              | `b222d466e128`  |
| 1064   | No file              | `b222d466e128`  |
| 1058   | No file              | `b222d466e128`  |
| 1051   | No file              | `b222d466e128`  |
| 1044   | No file              | `b222d466e128`  |
| 1036   | No file              | `b222d466e128`  |
| 1026   | No file              | `b222d466e128`  |
| 1016   | No file              | `b222d466e128`  |
| 1009   | No file              | `b222d466e128`  |
| 1005   | No file              | `b222d466e128`  |
| 1000   | No file              | `b222d466e128`  |
| 998    | No file              | `b222d466e128`  |
| 990    | No file              | `b222d466e128`  |
| 979    | No file              | `b222d466e128`  |
| 972    | No file              | `b222d466e128`  |
| 963    | No file              | `b222d466e128`  |
| 955    | No file              | `b222d466e128`  |
| 946    | No file              | `b222d466e128`  |
| 938    | No file              | `b222d466e128`  |
| 927    | No file              | `b222d466e128`  |
| 911    | No file              | `b222d466e128`  |
| 904    | No file              | `b222d466e128`  |
| 899    | No file              | `b222d466e128`  |
| 894    | No file              | `b222d466e128`  |
| 885    | No file              | `b222d466e128`  |
| 879    | No file              | `b222d466e128`  |
| 872    | No file              | `b222d466e128`  |
| 864    | No file              | `b222d466e128`  |
| 855    | No file              | `b222d466e128`  |
| 853    | No file              | `b222d466e128`  |
| 845    | No file              | `b222d466e128`  |
| 837    | No file              | `b222d466e128`  |
| 829    | No file              | `b222d466e128`  |
| 822    | No file              | `b222d466e128`  |
| 814    | No file              | `b222d466e128`  |
| 805    | No file              | `b222d466e128`  |
| 794    | No documented layout | `b222d466e128`  |
| 787    | No documented layout | `b222d466e128`  |
| 780    | No documented layout | `b222d466e128`  |
| 771    | No documented layout | `b222d466e128`  |
| 760    | No documented layout | `b222d466e128`  |
| 748    | No documented layout | `b222d466e128`  |
| 741    | No documented layout | `b222d466e128`  |
| 736    | No documented layout | `b222d466e128`  |
| 731    | No documented layout | `b222d466e128`  |
| 723    | No documented layout | `b222d466e128`  |
| 711    | No documented layout | `b222d466e128`  |
| 707    | No documented layout | `b222d466e128`  |
| 697    | No documented layout | `b222d466e128`  |
| 689    | No documented layout | `b222d466e128`  |
| 683    | No documented layout | `b222d466e128`  |
| 678    | No documented layout | `b222d466e128`  |
| 670    | No documented layout | `b222d466e128`  |
| 661    | No documented layout | `b222d466e128`  |
| 656    | No documented layout | `b222d466e128`  |
| 652    | No documented layout | `b222d466e128`  |
| 643    | No documented layout | `b222d466e128`  |
| 637    | No documented layout | `b222d466e128`  |
| 630    | No documented layout | `b222d466e128`  |
| 627    | No documented layout | `b222d466e128`  |
| 621    | No documented layout | `b222d466e128`  |
| 617    | No documented layout | `b222d466e128`  |
| 615    | No documented layout | `b222d466e128`  |
| 606    | No documented layout | `b222d466e128`  |
| 599    | No documented layout | `b222d466e128`  |
| 592    | No documented layout | `b222d466e128`  |
| 586    | No documented layout | `b222d466e128`  |
| 577    | No documented layout | `b222d466e128`  |
| 569    | No documented layout | `b222d466e128`  |
| 561    | No documented layout | `b222d466e128`  |
| 554    | No documented layout | `b222d466e128`  |
| 542    | No documented layout | `b222d466e128`  |
| 532    | No documented layout | `b222d466e128`  |
| 531    | No documented layout | `b222d466e128`  |
| 526    | No documented layout | `b222d466e128`  |
| 521    | No documented layout | `b222d466e128`  |
| 517    | No documented layout | `b222d466e128`  |
| 510    | No documented layout | `b222d466e128`  |
| 508    | No documented layout | `b222d466e128`  |
| 504    | No documented layout | `b222d466e128`  |
| 497    | No documented layout | `b222d466e128`  |
| 491    | No documented layout | `b222d466e128`  |
| 485    | No documented layout | `b222d466e128`  |
| 478    | No documented layout | `b222d466e128`  |
| 472    | No documented layout | `b222d466e128`  |
| 466    | No documented layout | `b222d466e128`  |
| 457    | No documented layout | `b222d466e128`  |
| 452    | No documented layout | `b222d466e128`  |
| 449    | No documented layout | `b222d466e128`  |
| 435    | No documented layout | `b222d466e128`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                              |
| ---------------------------- | -------- | --------------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so an NPC key without a row shows as plain text   |
| `languagedata_en.loc`        | Optional | NPC names (type 6), quest titles (type 18), knowledge names (type 34) and dialog names (type 38) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of NPCs                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 6 bytes + entries)

| Offset  | Type             | Field         | Notes                                                                           |
| ------- | ---------------- | ------------- | ------------------------------------------------------------------------------- |
| `+0x00` | u16              | character_key | NPC character key (LOC type 6); the rows are in ascending key order, `507` first on client 3482 |
| `+0x02` | u32              | info_count    | Number of `infos`; `1` to `5` on 350 of 353 rows of client 3482, `78` at most  |
| `+0x06` | Info[info_count] | infos         | See Info                                                                        |

### Info (variable: 24 bytes + quest group or dialog index)

| Offset             | Type                   | Field               | Notes                                                                                   |
| ------------------ | ---------------------- | ------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`            | u16                    | character_key       | Equals the row's `character_key` on every entry                                         |
| `+0x02`            | i32                    | intimacy            | Amity value the entry compares against, `0` to `2000` on client 3482; the window shows it out of 1,000 |
| `+0x06`            | u32                    | type_index          | `CppEnums.IntimacyInformationTypeInfo`; see Type Index                                  |
| `+0x0A`            | u32                    | operator_type       | `CppEnums.DlgCommonConditionOperatorType`: `0` Equal, `1` Large (▲), `2` Small (▼)      |
| `+0x0E`            | u32                    | knowledge_key       | `mentalcard.dbss` knowledge key on type `3` (Knowledge), `0` on the others              |
| `+0x12`            | u16 if type_index = 0  | quest_group         | Quest group of the quest (`getQuestNo()._group`)                                        |
| `quest_group+0x00` | u16 if type_index != 0 | dialog_index        | The NPC's dialog index on types `3` and `4` (`getDialogIndex()`), `0` on type `1`       |
| `dialog_index+0x00` | u16                   | quest_id            | Quest number in its group on type `0`; `0` on the others                                |
| `dialog_index+0x02` | u32                   | unknown_quest_id_02 | `0` on type `0`; see Open Questions                                                     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Type Index

`CppEnums.IntimacyInformationTypeInfo` of the client 3482 Lua
(`global_define_cpp_enum.luac`). Entries on client 3482 in the last column.

| Value | Name      | What the entry links             | Entries (client 3482) |
| ----- | --------- | -------------------------------- | --------------------- |
| 0     | Quest     | `quest_group`, `quest_id`        | 145                   |
| 1     | Shop      | Nothing; `unknown_quest_id_02`   | 175                   |
| 2     | Buff      |                                  | 0                     |
| 3     | Knowledge | `knowledge_key`, `dialog_index`  | 363                   |
| 4     | Talk      | `dialog_index`                   | 82                    |
| 5     | Item      |                                  | 0                     |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
these rows; `DataSheet_IntimacyDataTable.xlsm` holds the NPC to NPC amity
table instead. The 2016 `gc::IntimacyInformation` holds `_characterKey`,
`_intimacy`, `_typeIndex` (`gc::IntimacyInformationTypeInfo`),
`_operatorType` (`gc::DlgCommonCondition::OperatorType`), `_typeDescription`
and a condition list pointer, in that order. The names after
`operator_type` follow the client 3482 Lua getters and the data:

| Field          | Evidence (client 3482)                                                                 |
| -------------- | -------------------------------------------------------------------------------------- |
| knowledge_key  | 363 of 363 type `3` entries have a LOC type 34 knowledge name (`3001` Velia)           |
| quest_group, quest_id | 145 of 145 type `0` entries have a LOC type 18 quest title                      |
| dialog_index   | 445 of 445 type `3` and `4` entries name a dialog with a LOC type 38 dialog name, keyed `(character_key, dialog_index)`; the Lua skips a knowledge entry whose `getDialogIndex()` is not the open dialog's |

## Notes

- Every entry of client 3482 has `knowledge_key` `0` unless its type is
  `3`, and `quest_id` `0` unless its type is `0`.
- The window marks a knowledge entry as learned or not from
  `ToClinet_getMentalCardStaticStatus(getMentalCardKeyRaw()):isHasCard()`
  (the Lua spells the function `ToClinet`).
- The `CppEnums.IntimacyInformationTypeInfo` values `2` (Buff) and `5`
  (Item) have no entry on client 3482.

## Open Questions

### What the Last Field Holds

`unknown_quest_id_02` is `0` on every quest entry. On shop entries it is
`0`, `1`, `2`, `3` or `0xFFFFFFFF` (3, 61, 46, 31 and 34 entries on client
3482), on knowledge entries `0` to `281` and rising within an NPC (Igor
Bartali `162` to `166`), on talk entries `0` to `75`. The 2016 struct stored a
`_typeDescription` string here; the window's description text
(`getTypeDescription()`) may come from a string this value selects, but no
LOC type keyed by NPC and this value holds it on client 3482.
