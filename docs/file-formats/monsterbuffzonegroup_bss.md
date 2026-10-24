# `monsterbuffzonegroup.bss` Format

## Purpose

Per region a list of structure monsters (totems, guard towers, statues,
altars) and for each one a list of up to five other character keys. On
client 3482 the file has 28 regions, all hunting grounds (Olun's Valley,
Tunkuta, Hystria Ruins, Aakman Temple, Gyfin Rhasia Temple, Roud Sulfur
Works and more); Olun's Golem `21249` in Olun's Valley lists `21250` and
`21253`, Cyclops Statue `21696` in Cyclops Land lists Cyclops `21693`. The
file name ties it to the monster buff zone of
[`monsterbuffzone.bss`](monsterbuffzone_bss.md). The file is a u32 count
and variable rows, with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ---------------- | --------- |
| 1      | 2243 and later | 3483    | `monsterbuffzonegroup.bss` | 1,026 | 34 Entry, 28 Row | 21        |

| Layout | File                       | Known         | Unknown       |
| ------ | -------------------------- | ------------- | ------------- |
| 1      | `monsterbuffzonegroup.bss` | 784 B (76.4%) | 242 B (23.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `c729ca81b12c`  |
| 3482   | Layout 1             | `c729ca81b12c`  |
| 3474   | Layout 1             | `c729ca81b12c`  |
| 3473   | Layout 1             | `c729ca81b12c`  |
| 3464   | Layout 1             | `c729ca81b12c`  |
| 3458   | Layout 1             | `c729ca81b12c`  |
| 3454   | Layout 1             | `c729ca81b12c`  |
| 3444   | Layout 1             | `c729ca81b12c`  |
| 3435   | Layout 1             | `c729ca81b12c`  |
| 3426   | Layout 1             | `c729ca81b12c`  |
| 3418   | Layout 1             | `c729ca81b12c`  |
| 3412   | Layout 1             | `c729ca81b12c`  |
| 3402   | Layout 1             | `c729ca81b12c`  |
| 3396   | Layout 1             | `c729ca81b12c`  |
| 3387   | Layout 1             | `c729ca81b12c`  |
| 3381   | Layout 1             | `c729ca81b12c`  |
| 3373   | Layout 1             | `c729ca81b12c`  |
| 3364   | Layout 1             | `c729ca81b12c`  |
| 3356   | Layout 1             | `c729ca81b12c`  |
| 3349   | Layout 1             | `c729ca81b12c`  |
| 3342   | Layout 1             | `c729ca81b12c`  |
| 3335   | Layout 1             | `c729ca81b12c`  |
| 3326   | Layout 1             | `c729ca81b12c`  |
| 3321   | Layout 1             | `c729ca81b12c`  |
| 3314   | Layout 1             | `c729ca81b12c`  |
| 3303   | Layout 1             | `c729ca81b12c`  |
| 3302   | Layout 1             | `c729ca81b12c`  |
| 3293   | Layout 1             | `c729ca81b12c`  |
| 3283   | Layout 1             | `c729ca81b12c`  |
| 3275   | Layout 1             | `c729ca81b12c`  |
| 3267   | Layout 1             | `c729ca81b12c`  |
| 3258   | Layout 1             | `c729ca81b12c`  |
| 3251   | Layout 1             | `c729ca81b12c`  |
| 3242   | Layout 1             | `c729ca81b12c`  |
| 3235   | Layout 1             | `c729ca81b12c`  |
| 3229   | Layout 1             | `c729ca81b12c`  |
| 3212   | Layout 1             | `c729ca81b12c`  |
| 3203   | Layout 1             | `c729ca81b12c`  |
| 3193   | Layout 1             | `c729ca81b12c`  |
| 3186   | Layout 1             | `c729ca81b12c`  |
| 3177   | Layout 1             | `c729ca81b12c`  |
| 3169   | Layout 1             | `c729ca81b12c`  |
| 3158   | Layout 1             | `c729ca81b12c`  |
| 3151   | Layout 1             | `c729ca81b12c`  |
| 3144   | Layout 1             | `c729ca81b12c`  |
| 3133   | Layout 1             | `c729ca81b12c`  |
| 3125   | Layout 1             | `c729ca81b12c`  |
| 3118   | Layout 1             | `c729ca81b12c`  |
| 3111   | Layout 1             | `c729ca81b12c`  |
| 3103   | Layout 1             | `c729ca81b12c`  |
| 3095   | Layout 1             | `c729ca81b12c`  |
| 3086   | Layout 1             | `c729ca81b12c`  |
| 3072   | Layout 1             | `c729ca81b12c`  |
| 3062   | Layout 1             | `c729ca81b12c`  |
| 3052   | Layout 1             | `c729ca81b12c`  |
| 3045   | Layout 1             | `c729ca81b12c`  |
| 3037   | Layout 1             | `c729ca81b12c`  |
| 3030   | Layout 1             | `c729ca81b12c`  |
| 3021   | Layout 1             | `c729ca81b12c`  |
| 3012   | Layout 1             | `c729ca81b12c`  |
| 3002   | Layout 1             | `c729ca81b12c`  |
| 2995   | Layout 1             | `c729ca81b12c`  |
| 2987   | Layout 1             | `c729ca81b12c`  |
| 2978   | Layout 1             | `c729ca81b12c`  |
| 2970   | Layout 1             | `c729ca81b12c`  |
| 2959   | Layout 1             | `c729ca81b12c`  |
| 2951   | Layout 1             | `c729ca81b12c`  |
| 2942   | Layout 1             | `c729ca81b12c`  |
| 2935   | Layout 1             | `c729ca81b12c`  |
| 2932   | Layout 1             | `c729ca81b12c`  |
| 2923   | Layout 1             | `c729ca81b12c`  |
| 2919   | Layout 1             | `c729ca81b12c`  |
| 2907   | Layout 1             | `c729ca81b12c`  |
| 2900   | Layout 1             | `c729ca81b12c`  |
| 2891   | Layout 1             | `c729ca81b12c`  |
| 2882   | Layout 1             | `c729ca81b12c`  |
| 2872   | Layout 1             | `c729ca81b12c`  |
| 2863   | Layout 1             | `c729ca81b12c`  |
| 2855   | Layout 1             | `c729ca81b12c`  |
| 2849   | Layout 1             | `c729ca81b12c`  |
| 2844   | Layout 1             | `c729ca81b12c`  |
| 2834   | Layout 1             | `c729ca81b12c`  |
| 2825   | Layout 1             | `c729ca81b12c`  |
| 2819   | Layout 1             | `c729ca81b12c`  |
| 2811   | Layout 1             | `c729ca81b12c`  |
| 2803   | Layout 1             | `c729ca81b12c`  |
| 2794   | Layout 1             | `c729ca81b12c`  |
| 2783   | Layout 1             | `c729ca81b12c`  |
| 2774   | Layout 1             | `c729ca81b12c`  |
| 2765   | Layout 1             | `c729ca81b12c`  |
| 2756   | Layout 1             | `c729ca81b12c`  |
| 2750   | Layout 1             | `c729ca81b12c`  |
| 2743   | Layout 1             | `c729ca81b12c`  |
| 2736   | Layout 1             | `c729ca81b12c`  |
| 2726   | Layout 1             | `c729ca81b12c`  |
| 2717   | Layout 1             | `c729ca81b12c`  |
| 2709   | Layout 1             | `c729ca81b12c`  |
| 2703   | Layout 1             | `c729ca81b12c`  |
| 2695   | Layout 1             | `c729ca81b12c`  |
| 2684   | Layout 1             | `c729ca81b12c`  |
| 2672   | Layout 1             | `c729ca81b12c`  |
| 2665   | Layout 1             | `c729ca81b12c`  |
| 2657   | Layout 1             | `c729ca81b12c`  |
| 2649   | Layout 1             | `c729ca81b12c`  |
| 2644   | Layout 1             | `c729ca81b12c`  |
| 2637   | Layout 1             | `c729ca81b12c`  |
| 2629   | Layout 1             | `c729ca81b12c`  |
| 2619   | Layout 1             | `c729ca81b12c`  |
| 2612   | Layout 1             | `c729ca81b12c`  |
| 2606   | Layout 1             | `c729ca81b12c`  |
| 2602   | Layout 1             | `c729ca81b12c`  |
| 2601   | Layout 1             | `c729ca81b12c`  |
| 2592   | Layout 1             | `c729ca81b12c`  |
| 2583   | Layout 1             | `c729ca81b12c`  |
| 2575   | Layout 1             | `c729ca81b12c`  |
| 2567   | Layout 1             | `c729ca81b12c`  |
| 2560   | Layout 1             | `c729ca81b12c`  |
| 2553   | Layout 1             | `c729ca81b12c`  |
| 2545   | Layout 1             | `c729ca81b12c`  |
| 2538   | Layout 1             | `c729ca81b12c`  |
| 2529   | Layout 1             | `c729ca81b12c`  |
| 2519   | Layout 1             | `c729ca81b12c`  |
| 2513   | Layout 1             | `c729ca81b12c`  |
| 2510   | Layout 1             | `c729ca81b12c`  |
| 2507   | Layout 1             | `c729ca81b12c`  |
| 2503   | Layout 1             | `c729ca81b12c`  |
| 2498   | Layout 1             | `c729ca81b12c`  |
| 2492   | Layout 1             | `c729ca81b12c`  |
| 2487   | Layout 1             | `c729ca81b12c`  |
| 2480   | Layout 1             | `c729ca81b12c`  |
| 2474   | Layout 1             | `c729ca81b12c`  |
| 2468   | Layout 1             | `c729ca81b12c`  |
| 2460   | Layout 1             | `c729ca81b12c`  |
| 2453   | Layout 1             | `c729ca81b12c`  |
| 2444   | Layout 1             | `c729ca81b12c`  |
| 2438   | Layout 1             | `c729ca81b12c`  |
| 2434   | Layout 1             | `c729ca81b12c`  |
| 2429   | Layout 1             | `c729ca81b12c`  |
| 2421   | Layout 1             | `c729ca81b12c`  |
| 2414   | Layout 1             | `c729ca81b12c`  |
| 2407   | Layout 1             | `c729ca81b12c`  |
| 2401   | Layout 1             | `c729ca81b12c`  |
| 2397   | Layout 1             | `c729ca81b12c`  |
| 2393   | Layout 1             | `c729ca81b12c`  |
| 2384   | Layout 1             | `c729ca81b12c`  |
| 2378   | Layout 1             | `c729ca81b12c`  |
| 2372   | Layout 1             | `c729ca81b12c`  |
| 2358   | Layout 1             | `c729ca81b12c`  |
| 2352   | Layout 1             | `c729ca81b12c`  |
| 2347   | Layout 1             | `c729ca81b12c`  |
| 2343   | Layout 1             | `c729ca81b12c`  |
| 2335   | Layout 1             | `c729ca81b12c`  |
| 2327   | Layout 1             | `c729ca81b12c`  |
| 2324   | Layout 1             | `c729ca81b12c`  |
| 2319   | Layout 1             | `c729ca81b12c`  |
| 2313   | Layout 1             | `c729ca81b12c`  |
| 2308   | Layout 1             | `c729ca81b12c`  |
| 2302   | Layout 1             | `c729ca81b12c`  |
| 2295   | Layout 1             | `c729ca81b12c`  |
| 2290   | Layout 1             | `c729ca81b12c`  |
| 2284   | Layout 1             | `c729ca81b12c`  |
| 2276   | Layout 1             | `c729ca81b12c`  |
| 2269   | Layout 1             | `c729ca81b12c`  |
| 2259   | No documented layout | `c729ca81b12c`  |
| 2250   | Layout 1             | `c729ca81b12c`  |
| 2243   | Layout 1             | `c729ca81b12c`  |
| 2235   | No file              | `c729ca81b12c`  |
| 2229   | No file              | `c729ca81b12c`  |
| 2224   | No file              | `c729ca81b12c`  |
| 2218   | No file              | `c729ca81b12c`  |
| 2215   | No file              | `c729ca81b12c`  |
| 2207   | No file              | `c729ca81b12c`  |
| 2203   | No file              | `c729ca81b12c`  |
| 2196   | No file              | `c729ca81b12c`  |
| 2192   | No file              | `c729ca81b12c`  |
| 2189   | No file              | `c729ca81b12c`  |
| 2183   | No file              | `c729ca81b12c`  |
| 2179   | No file              | `c729ca81b12c`  |
| 2171   | No file              | `c729ca81b12c`  |
| 2163   | No file              | `c729ca81b12c`  |
| 2156   | No file              | `c729ca81b12c`  |
| 2151   | No file              | `c729ca81b12c`  |
| 2147   | No file              | `c729ca81b12c`  |
| 2142   | No file              | `c729ca81b12c`  |
| 2138   | No file              | `c729ca81b12c`  |
| 2134   | No file              | `c729ca81b12c`  |
| 2130   | No file              | `c729ca81b12c`  |
| 2122   | No file              | `c729ca81b12c`  |
| 2107   | No file              | `c729ca81b12c`  |
| 2098   | No file              | `c729ca81b12c`  |
| 2089   | No file              | `c729ca81b12c`  |
| 2081   | No file              | `c729ca81b12c`  |
| 2073   | No file              | `c729ca81b12c`  |
| 2067   | No file              | `c729ca81b12c`  |
| 2063   | No file              | `c729ca81b12c`  |
| 2059   | No file              | `c729ca81b12c`  |
| 2052   | No file              | `c729ca81b12c`  |
| 2044   | No file              | `c729ca81b12c`  |
| 2039   | No file              | `c729ca81b12c`  |
| 2032   | No file              | `c729ca81b12c`  |
| 2025   | No file              | `c729ca81b12c`  |
| 2011   | No file              | `c729ca81b12c`  |
| 2005   | No file              | `c729ca81b12c`  |
| 2000   | No file              | `c729ca81b12c`  |
| 1996   | No file              | `c729ca81b12c`  |
| 1991   | No file              | `c729ca81b12c`  |
| 1985   | No file              | `c729ca81b12c`  |
| 1980   | No file              | `c729ca81b12c`  |
| 1969   | No file              | `c729ca81b12c`  |
| 1964   | No file              | `c729ca81b12c`  |
| 1958   | No file              | `c729ca81b12c`  |
| 1950   | No file              | `c729ca81b12c`  |
| 1945   | No file              | `c729ca81b12c`  |
| 1937   | No file              | `c729ca81b12c`  |
| 1933   | No file              | `c729ca81b12c`  |
| 1927   | No file              | `c729ca81b12c`  |
| 1921   | No file              | `c729ca81b12c`  |
| 1914   | No file              | `c729ca81b12c`  |
| 1908   | No file              | `c729ca81b12c`  |
| 1897   | No file              | `c729ca81b12c`  |
| 1892   | No file              | `c729ca81b12c`  |
| 1886   | No file              | `c729ca81b12c`  |
| 1881   | No file              | `c729ca81b12c`  |
| 1871   | No file              | `c729ca81b12c`  |
| 1866   | No file              | `c729ca81b12c`  |
| 1862   | No file              | `c729ca81b12c`  |
| 1854   | No file              | `c729ca81b12c`  |
| 1846   | No file              | `c729ca81b12c`  |
| 1838   | No file              | `c729ca81b12c`  |
| 1832   | No file              | `c729ca81b12c`  |
| 1826   | No file              | `c729ca81b12c`  |
| 1822   | No file              | `c729ca81b12c`  |
| 1818   | No file              | `c729ca81b12c`  |
| 1804   | No file              | `c729ca81b12c`  |
| 1794   | No file              | `c729ca81b12c`  |
| 1790   | No file              | `c729ca81b12c`  |
| 1784   | No file              | `c729ca81b12c`  |
| 1774   | No file              | `c729ca81b12c`  |
| 1771   | No file              | `c729ca81b12c`  |
| 1762   | No file              | `c729ca81b12c`  |
| 1759   | No file              | `c729ca81b12c`  |
| 1754   | No file              | `c729ca81b12c`  |
| 1749   | No file              | `c729ca81b12c`  |
| 1743   | No file              | `c729ca81b12c`  |
| 1737   | No file              | `c729ca81b12c`  |
| 1731   | No file              | `c729ca81b12c`  |
| 1725   | No file              | `c729ca81b12c`  |
| 1717   | No file              | `c729ca81b12c`  |
| 1710   | No file              | `c729ca81b12c`  |
| 1704   | No file              | `c729ca81b12c`  |
| 1698   | No file              | `c729ca81b12c`  |
| 1690   | No file              | `c729ca81b12c`  |
| 1685   | No file              | `c729ca81b12c`  |
| 1680   | No file              | `c729ca81b12c`  |
| 1674   | No file              | `c729ca81b12c`  |
| 1668   | No file              | `c729ca81b12c`  |
| 1659   | No file              | `c729ca81b12c`  |
| 1649   | No file              | `c729ca81b12c`  |
| 1642   | No file              | `c729ca81b12c`  |
| 1636   | No file              | `c729ca81b12c`  |
| 1628   | No file              | `c729ca81b12c`  |
| 1622   | No file              | `c729ca81b12c`  |
| 1614   | No file              | `c729ca81b12c`  |
| 1608   | No file              | `c729ca81b12c`  |
| 1602   | No file              | `c729ca81b12c`  |
| 1598   | No file              | `c729ca81b12c`  |
| 1594   | No file              | `c729ca81b12c`  |
| 1590   | No file              | `c729ca81b12c`  |
| 1587   | No file              | `c729ca81b12c`  |
| 1584   | No file              | `c729ca81b12c`  |
| 1579   | No file              | `c729ca81b12c`  |
| 1572   | No file              | `c729ca81b12c`  |
| 1565   | No file              | `c729ca81b12c`  |
| 1559   | No file              | `c729ca81b12c`  |
| 1554   | No file              | `c729ca81b12c`  |
| 1547   | No file              | `c729ca81b12c`  |
| 1537   | No file              | `c729ca81b12c`  |
| 1529   | No file              | `c729ca81b12c`  |
| 1524   | No file              | `c729ca81b12c`  |
| 1519   | No file              | `c729ca81b12c`  |
| 1509   | No file              | `c729ca81b12c`  |
| 1506   | No file              | `c729ca81b12c`  |
| 1504   | No file              | `c729ca81b12c`  |
| 1500   | No file              | `c729ca81b12c`  |
| 1493   | No file              | `c729ca81b12c`  |
| 1489   | No file              | `c729ca81b12c`  |
| 1485   | No file              | `c729ca81b12c`  |
| 1481   | No file              | `c729ca81b12c`  |
| 1474   | No file              | `c729ca81b12c`  |
| 1466   | No file              | `c729ca81b12c`  |
| 1462   | No file              | `c729ca81b12c`  |
| 1459   | No file              | `c729ca81b12c`  |
| 1453   | No file              | `c729ca81b12c`  |
| 1450   | No file              | `c729ca81b12c`  |
| 1445   | No file              | `c729ca81b12c`  |
| 1439   | No file              | `c729ca81b12c`  |
| 1433   | No file              | `c729ca81b12c`  |
| 1430   | No file              | `c729ca81b12c`  |
| 1426   | No file              | `c729ca81b12c`  |
| 1421   | No file              | `c729ca81b12c`  |
| 1417   | No file              | `c729ca81b12c`  |
| 1416   | No file              | `c729ca81b12c`  |
| 1409   | No file              | `c729ca81b12c`  |
| 1405   | No file              | `c729ca81b12c`  |
| 1401   | No file              | `c729ca81b12c`  |
| 1396   | No file              | `c729ca81b12c`  |
| 1391   | No file              | `c729ca81b12c`  |
| 1390   | No file              | `c729ca81b12c`  |
| 1386   | No file              | `c729ca81b12c`  |
| 1381   | No file              | `c729ca81b12c`  |
| 1379   | No file              | `c729ca81b12c`  |
| 1372   | No file              | `c729ca81b12c`  |
| 1366   | No file              | `c729ca81b12c`  |
| 1364   | No file              | `c729ca81b12c`  |
| 1363   | No file              | `c729ca81b12c`  |
| 1360   | No file              | `c729ca81b12c`  |
| 1358   | No file              | `c729ca81b12c`  |
| 1355   | No file              | `c729ca81b12c`  |
| 1351   | No file              | `c729ca81b12c`  |
| 1348   | No file              | `c729ca81b12c`  |
| 1346   | No file              | `c729ca81b12c`  |
| 1341   | No file              | `c729ca81b12c`  |
| 1340   | No file              | `c729ca81b12c`  |
| 1338   | No file              | `c729ca81b12c`  |
| 1335   | No file              | `c729ca81b12c`  |
| 1333   | No file              | `c729ca81b12c`  |
| 1329   | No file              | `c729ca81b12c`  |
| 1327   | No file              | `c729ca81b12c`  |
| 1324   | No file              | `c729ca81b12c`  |
| 1321   | No file              | `c729ca81b12c`  |
| 1319   | No file              | `c729ca81b12c`  |
| 1318   | No file              | `c729ca81b12c`  |
| 1316   | No file              | `c729ca81b12c`  |
| 1313   | No file              | `c729ca81b12c`  |
| 1311   | No file              | `c729ca81b12c`  |
| 1309   | No file              | `c729ca81b12c`  |
| 1304   | No file              | `c729ca81b12c`  |
| 1292   | No file              | `c729ca81b12c`  |
| 1286   | No file              | `c729ca81b12c`  |
| 1280   | No file              | `c729ca81b12c`  |
| 1276   | No file              | `c729ca81b12c`  |
| 1267   | No file              | `c729ca81b12c`  |
| 1261   | No file              | `c729ca81b12c`  |
| 1256   | No file              | `c729ca81b12c`  |
| 1250   | No file              | `c729ca81b12c`  |
| 1246   | No file              | `c729ca81b12c`  |
| 1239   | No file              | `c729ca81b12c`  |
| 1230   | No file              | `c729ca81b12c`  |
| 1226   | No file              | `c729ca81b12c`  |
| 1220   | No file              | `c729ca81b12c`  |
| 1217   | No file              | `c729ca81b12c`  |
| 1211   | No file              | `c729ca81b12c`  |
| 1210   | No file              | `c729ca81b12c`  |
| 1208   | No file              | `c729ca81b12c`  |
| 1203   | No file              | `c729ca81b12c`  |
| 1197   | No file              | `c729ca81b12c`  |
| 1194   | No file              | `c729ca81b12c`  |
| 1192   | No file              | `c729ca81b12c`  |
| 1187   | No file              | `c729ca81b12c`  |
| 1183   | No file              | `c729ca81b12c`  |
| 1177   | No file              | `c729ca81b12c`  |
| 1173   | No file              | `c729ca81b12c`  |
| 1167   | No file              | `c729ca81b12c`  |
| 1164   | No file              | `c729ca81b12c`  |
| 1156   | No file              | `c729ca81b12c`  |
| 1149   | No file              | `c729ca81b12c`  |
| 1144   | No file              | `c729ca81b12c`  |
| 1137   | No file              | `c729ca81b12c`  |
| 1132   | No file              | `c729ca81b12c`  |
| 1127   | No file              | `c729ca81b12c`  |
| 1122   | No file              | `c729ca81b12c`  |
| 1118   | No file              | `c729ca81b12c`  |
| 1114   | No file              | `c729ca81b12c`  |
| 1109   | No file              | `c729ca81b12c`  |
| 1102   | No file              | `c729ca81b12c`  |
| 1096   | No file              | `c729ca81b12c`  |
| 1088   | No file              | `c729ca81b12c`  |
| 1081   | No file              | `c729ca81b12c`  |
| 1076   | No file              | `c729ca81b12c`  |
| 1069   | No file              | `c729ca81b12c`  |
| 1064   | No file              | `c729ca81b12c`  |
| 1058   | No file              | `c729ca81b12c`  |
| 1051   | No file              | `c729ca81b12c`  |
| 1044   | No file              | `c729ca81b12c`  |
| 1036   | No file              | `c729ca81b12c`  |
| 1026   | No file              | `c729ca81b12c`  |
| 1016   | No file              | `c729ca81b12c`  |
| 1009   | No file              | `c729ca81b12c`  |
| 1005   | No file              | `c729ca81b12c`  |
| 1000   | No file              | `c729ca81b12c`  |
| 998    | No file              | `c729ca81b12c`  |
| 990    | No file              | `c729ca81b12c`  |
| 979    | No file              | `c729ca81b12c`  |
| 972    | No file              | `c729ca81b12c`  |
| 963    | No file              | `c729ca81b12c`  |
| 955    | No file              | `c729ca81b12c`  |
| 946    | No file              | `c729ca81b12c`  |
| 938    | No file              | `c729ca81b12c`  |
| 927    | No file              | `c729ca81b12c`  |
| 911    | No file              | `c729ca81b12c`  |
| 904    | No file              | `c729ca81b12c`  |
| 899    | No file              | `c729ca81b12c`  |
| 894    | No file              | `c729ca81b12c`  |
| 885    | No file              | `c729ca81b12c`  |
| 879    | No file              | `c729ca81b12c`  |
| 872    | No file              | `c729ca81b12c`  |
| 864    | No file              | `c729ca81b12c`  |
| 855    | No file              | `c729ca81b12c`  |
| 853    | No file              | `c729ca81b12c`  |
| 845    | No file              | `c729ca81b12c`  |
| 837    | No file              | `c729ca81b12c`  |
| 829    | No file              | `c729ca81b12c`  |
| 822    | No file              | `c729ca81b12c`  |
| 814    | No file              | `c729ca81b12c`  |
| 805    | No file              | `c729ca81b12c`  |
| 794    | No file              | `c729ca81b12c`  |
| 787    | No file              | `c729ca81b12c`  |
| 780    | No file              | `c729ca81b12c`  |
| 771    | No file              | `c729ca81b12c`  |
| 760    | No file              | `c729ca81b12c`  |
| 748    | No file              | `c729ca81b12c`  |
| 741    | No file              | `c729ca81b12c`  |
| 736    | No file              | `c729ca81b12c`  |
| 731    | No file              | `c729ca81b12c`  |
| 723    | No file              | `c729ca81b12c`  |
| 711    | No file              | `c729ca81b12c`  |
| 707    | No file              | `c729ca81b12c`  |
| 697    | No file              | `c729ca81b12c`  |
| 689    | No file              | `c729ca81b12c`  |
| 683    | No file              | `c729ca81b12c`  |
| 678    | No file              | `c729ca81b12c`  |
| 670    | No file              | `c729ca81b12c`  |
| 661    | No file              | `c729ca81b12c`  |
| 656    | No file              | `c729ca81b12c`  |
| 652    | No file              | `c729ca81b12c`  |
| 643    | No file              | `c729ca81b12c`  |
| 637    | No file              | `c729ca81b12c`  |
| 630    | No file              | `c729ca81b12c`  |
| 627    | No file              | `c729ca81b12c`  |
| 621    | No file              | `c729ca81b12c`  |
| 617    | No file              | `c729ca81b12c`  |
| 615    | No file              | `c729ca81b12c`  |
| 606    | No file              | `c729ca81b12c`  |
| 599    | No file              | `c729ca81b12c`  |
| 592    | No file              | `c729ca81b12c`  |
| 586    | No file              | `c729ca81b12c`  |
| 577    | No file              | `c729ca81b12c`  |
| 569    | No file              | `c729ca81b12c`  |
| 561    | No file              | `c729ca81b12c`  |
| 554    | No file              | `c729ca81b12c`  |
| 542    | No file              | `c729ca81b12c`  |
| 532    | No file              | `c729ca81b12c`  |
| 531    | No file              | `c729ca81b12c`  |
| 526    | No file              | `c729ca81b12c`  |
| 521    | No file              | `c729ca81b12c`  |
| 517    | No file              | `c729ca81b12c`  |
| 510    | No file              | `c729ca81b12c`  |
| 508    | No file              | `c729ca81b12c`  |
| 504    | No file              | `c729ca81b12c`  |
| 497    | No file              | `c729ca81b12c`  |
| 491    | No file              | `c729ca81b12c`  |
| 485    | No file              | `c729ca81b12c`  |
| 478    | No file              | `c729ca81b12c`  |
| 472    | No file              | `c729ca81b12c`  |
| 466    | No file              | `c729ca81b12c`  |
| 457    | No file              | `c729ca81b12c`  |
| 452    | No file              | `c729ca81b12c`  |
| 449    | No file              | `c729ca81b12c`  |
| 435    | No file              | `c729ca81b12c`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | Region names (LOC type 17) and character names (LOC type 6) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 11 bytes + entries)

| Offset  | Type               | Field       | Notes |
| ------- | ------------------ | ----------- | ----- |
| `+0x00` | u16                | region_key  | `regioninfo.bss` region key; unique, not sorted |
| `+0x02` | u32                | unknown_02  | `1` on every row (client 3482) |
| `+0x06` | u8                 | unknown_06  | `0` on every row |
| `+0x07` | u32                | entry_count | Number of entries, `1` or `2` |
| `+0x0B` | Entry[entry_count] | entries     | See Entry |

### Entry (variable: 11 bytes + list)

| Offset  | Type                   | Field             | Notes |
| ------- | ---------------------- | ----------------- | ----- |
| `+0x00` | u16                    | character_key     | `characterstatic.dbss` character key of a structure monster |
| `+0x02` | u8                     | unknown_02        | `0` on every entry |
| `+0x03` | u16                    | character_key_dup | Equals `character_key` on every entry |
| `+0x05` | u16                    | unknown_05        | Equals the row's `region_key` on every entry |
| `+0x07` | u32                    | character_count   | `5` on every entry |
| `+0x0B` | u16[character_count]   | character_keys    | Character keys, the unused slots `0` (client 3482) |

## Regions (Client 3482)

| Structure monster                  | Listed characters             | Regions |
| ---------------------------------- | ----------------------------- | ------- |
| Olun's Golem `21249`               | `21250`, `21253`              | 958, 1030, 1041, 1058 |
| Turo Totem `21618`, Turo Charm `21617` | `21500`, `21499`          | 965, 967, 1013, 1032, 1034, 1049 |
| Eye of Despair `20411`             | `21630`                       | 962, 1047, 1051 |
| Rift Seed `20000`                  | `21100`, `21105`              | 743 |
| Gyfin Rhasia Tower of Carnage `28470` | `28471`                    | 739, 740 |
| Mirumok Lookout `21634`            | `21635`                       | 729, 732 |
| Jail Alarm Device `22599`          | `22491`                       | 691 |
| Hystria Guard Tower `22489`        | `22598`                       | 689 |
| Aakman Illusion Statue `22595`     | `22597`                       | 688 |
| Argos Obsidian Altar `21141`       | `21140`                       | 622, 625 |
| Cadry Cannon `21660`               | `21666`                       | 579, 631 |
| Cyclops Statue `21696`             | Cyclops `21693`               | 249 |
| Lava Phlogiston Condenser `22896`  | `22493`                       | 418, 420 |

Every listed character has the name of its structure monster, except
Cyclops `21693`. The two Turo entries are always together.

## Field Names

`region_key` resolves to a LOC type 17 region name on all 28 rows, and the
regions hold the structure monsters of their entries (Turo Totem in
Tunkuta, Lava Phlogiston Condenser in Roud Sulfur Works). The character
keys resolve to LOC type 6 names. The file is not in client 1784, no sheet
of a private server's `DataSheets.bexcel` on client 1784 has a column
with `BuffZone` in its name, and no client Lua function on client 3482
reads the table, so the other fields keep `unknown_` names.

## Notes

- The file is in client 2250 and later. Client 2519 has 19 rows, and its
  `character_keys` hold five keys on every entry: the first key repeated
  (`22493` five times), or other keys (`21250, 21068, 21650, 21660,
  21669` for Olun's Golem, where client 2765 and later have `21250, 0, 0,
  0, 0`).

## Open Questions

### What the Listed Characters Are

The listed characters carry the structure monster's name (Olun's Golem
`21250` and `21253` for `21249`), except the Cyclops listed for the
Cyclops Statue. They could be the forms the structure takes while a
monster buff zone is active, or the monsters it summons; the file and
the Lua show neither.

### unknown_02 and unknown_06

`1` and `0` on every row of every client that has the file. Whether
`unknown_02` is a count of something with `unknown_06` its only entry is
open.
