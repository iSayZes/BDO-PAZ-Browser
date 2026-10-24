# `guildhouseinfo.dbss` Format

## Purpose

The guild houses: one variable-length row per guild house with its town,
its worldmap node and its uses (a [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md)
receipe and the highest level the house reaches with it), the house's
character key after them. The client Lua reads a row through
`ToClient_GetGuildHouseInfoStaticStatusWrapper(houseKey)`. The node houses
are in [`houseinfo.bss`](houseinfo_bss.md), whose row ends in the same
`Craft` entries. Companion `guildhouseinfooffset.dbss` lists where every row
sits.

On client 3482 the 23 rows cover eight towns: Velia, Olvia, Heidel,
Calpheon City, Altinova, Tarif, Valencia City and Marzana's Villa (town
`650`, the four Valencia guild houses on Shakatu, Taphtar Plain, Pujiya
Canyon and Cadry Ruins). The file is byte for byte the same on clients 1784
and 3482.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | ---------------- | --------- |
| 1      | 1346 and later | 3483    | `guildhouseinfo.dbss`       | 974   | 81 Craft, 23 Row | 8         |
| 1      | 1346 and later | 3483    | `guildhouseinfooffset.dbss` | 234   | 23 Offset Row    | 10        |

| Layout | File                        | Known          | Unknown     |
| ------ | --------------------------- | -------------- | ----------- |
| 1      | `guildhouseinfo.dbss`       | 928 B (95.3%)  | 46 B (4.7%) |
| 1      | `guildhouseinfooffset.dbss` | 234 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `a835520d0037`  |
| 3482   | Layout 1             | `a835520d0037`  |
| 3474   | Layout 1             | `a835520d0037`  |
| 3473   | Layout 1             | `a835520d0037`  |
| 3464   | Layout 1             | `a835520d0037`  |
| 3458   | Layout 1             | `a835520d0037`  |
| 3454   | Layout 1             | `a835520d0037`  |
| 3444   | Layout 1             | `a835520d0037`  |
| 3435   | Layout 1             | `a835520d0037`  |
| 3426   | Layout 1             | `a835520d0037`  |
| 3418   | Layout 1             | `a835520d0037`  |
| 3412   | Layout 1             | `a835520d0037`  |
| 3402   | Layout 1             | `a835520d0037`  |
| 3396   | Layout 1             | `a835520d0037`  |
| 3387   | Layout 1             | `a835520d0037`  |
| 3381   | Layout 1             | `a835520d0037`  |
| 3373   | Layout 1             | `a835520d0037`  |
| 3364   | Layout 1             | `a835520d0037`  |
| 3356   | Layout 1             | `a835520d0037`  |
| 3349   | Layout 1             | `a835520d0037`  |
| 3342   | Layout 1             | `a835520d0037`  |
| 3335   | Layout 1             | `a835520d0037`  |
| 3326   | Layout 1             | `a835520d0037`  |
| 3321   | Layout 1             | `a835520d0037`  |
| 3314   | Layout 1             | `a835520d0037`  |
| 3303   | Layout 1             | `a835520d0037`  |
| 3302   | Layout 1             | `a835520d0037`  |
| 3293   | Layout 1             | `a835520d0037`  |
| 3283   | Layout 1             | `a835520d0037`  |
| 3275   | Layout 1             | `a835520d0037`  |
| 3267   | Layout 1             | `a835520d0037`  |
| 3258   | Layout 1             | `a835520d0037`  |
| 3251   | Layout 1             | `a835520d0037`  |
| 3242   | Layout 1             | `a835520d0037`  |
| 3235   | Layout 1             | `a835520d0037`  |
| 3229   | Layout 1             | `a835520d0037`  |
| 3212   | Layout 1             | `a835520d0037`  |
| 3203   | Layout 1             | `a835520d0037`  |
| 3193   | Layout 1             | `a835520d0037`  |
| 3186   | Layout 1             | `a835520d0037`  |
| 3177   | Layout 1             | `a835520d0037`  |
| 3169   | Layout 1             | `a835520d0037`  |
| 3158   | Layout 1             | `a835520d0037`  |
| 3151   | Layout 1             | `a835520d0037`  |
| 3144   | Layout 1             | `a835520d0037`  |
| 3133   | Layout 1             | `a835520d0037`  |
| 3125   | Layout 1             | `a835520d0037`  |
| 3118   | Layout 1             | `a835520d0037`  |
| 3111   | Layout 1             | `a835520d0037`  |
| 3103   | Layout 1             | `a835520d0037`  |
| 3095   | Layout 1             | `a835520d0037`  |
| 3086   | Layout 1             | `a835520d0037`  |
| 3072   | Layout 1             | `a835520d0037`  |
| 3062   | Layout 1             | `a835520d0037`  |
| 3052   | Layout 1             | `a835520d0037`  |
| 3045   | Layout 1             | `a835520d0037`  |
| 3037   | Layout 1             | `a835520d0037`  |
| 3030   | Layout 1             | `a835520d0037`  |
| 3021   | Layout 1             | `a835520d0037`  |
| 3012   | Layout 1             | `a835520d0037`  |
| 3002   | Layout 1             | `a835520d0037`  |
| 2995   | Layout 1             | `a835520d0037`  |
| 2987   | Layout 1             | `a835520d0037`  |
| 2978   | Layout 1             | `a835520d0037`  |
| 2970   | Layout 1             | `a835520d0037`  |
| 2959   | Layout 1             | `a835520d0037`  |
| 2951   | Layout 1             | `a835520d0037`  |
| 2942   | Layout 1             | `a835520d0037`  |
| 2935   | Layout 1             | `a835520d0037`  |
| 2932   | Layout 1             | `a835520d0037`  |
| 2923   | Layout 1             | `a835520d0037`  |
| 2919   | Layout 1             | `a835520d0037`  |
| 2907   | Layout 1             | `a835520d0037`  |
| 2900   | Layout 1             | `a835520d0037`  |
| 2891   | Layout 1             | `a835520d0037`  |
| 2882   | Layout 1             | `a835520d0037`  |
| 2872   | Layout 1             | `a835520d0037`  |
| 2863   | Layout 1             | `a835520d0037`  |
| 2855   | Layout 1             | `a835520d0037`  |
| 2849   | Layout 1             | `a835520d0037`  |
| 2844   | Layout 1             | `a835520d0037`  |
| 2834   | Layout 1             | `a835520d0037`  |
| 2825   | Layout 1             | `a835520d0037`  |
| 2819   | Layout 1             | `a835520d0037`  |
| 2811   | Layout 1             | `a835520d0037`  |
| 2803   | Layout 1             | `a835520d0037`  |
| 2794   | Layout 1             | `a835520d0037`  |
| 2783   | Layout 1             | `a835520d0037`  |
| 2774   | Layout 1             | `a835520d0037`  |
| 2765   | Layout 1             | `a835520d0037`  |
| 2756   | Layout 1             | `a835520d0037`  |
| 2750   | Layout 1             | `a835520d0037`  |
| 2743   | Layout 1             | `a835520d0037`  |
| 2736   | Layout 1             | `a835520d0037`  |
| 2726   | Layout 1             | `a835520d0037`  |
| 2717   | Layout 1             | `a835520d0037`  |
| 2709   | Layout 1             | `a835520d0037`  |
| 2703   | Layout 1             | `a835520d0037`  |
| 2695   | Layout 1             | `a835520d0037`  |
| 2684   | Layout 1             | `a835520d0037`  |
| 2672   | Layout 1             | `a835520d0037`  |
| 2665   | Layout 1             | `a835520d0037`  |
| 2657   | Layout 1             | `a835520d0037`  |
| 2649   | Layout 1             | `a835520d0037`  |
| 2644   | Layout 1             | `a835520d0037`  |
| 2637   | Layout 1             | `a835520d0037`  |
| 2629   | Layout 1             | `a835520d0037`  |
| 2619   | Layout 1             | `a835520d0037`  |
| 2612   | Layout 1             | `a835520d0037`  |
| 2606   | Layout 1             | `a835520d0037`  |
| 2602   | Layout 1             | `a835520d0037`  |
| 2601   | Layout 1             | `a835520d0037`  |
| 2592   | Layout 1             | `a835520d0037`  |
| 2583   | Layout 1             | `a835520d0037`  |
| 2575   | Layout 1             | `a835520d0037`  |
| 2567   | Layout 1             | `a835520d0037`  |
| 2560   | Layout 1             | `a835520d0037`  |
| 2553   | Layout 1             | `a835520d0037`  |
| 2545   | Layout 1             | `a835520d0037`  |
| 2538   | Layout 1             | `a835520d0037`  |
| 2529   | Layout 1             | `a835520d0037`  |
| 2519   | Layout 1             | `a835520d0037`  |
| 2513   | Layout 1             | `a835520d0037`  |
| 2510   | Layout 1             | `a835520d0037`  |
| 2507   | Layout 1             | `a835520d0037`  |
| 2503   | Layout 1             | `a835520d0037`  |
| 2498   | Layout 1             | `a835520d0037`  |
| 2492   | Layout 1             | `a835520d0037`  |
| 2487   | Layout 1             | `a835520d0037`  |
| 2480   | Layout 1             | `a835520d0037`  |
| 2474   | Layout 1             | `a835520d0037`  |
| 2468   | Layout 1             | `a835520d0037`  |
| 2460   | Layout 1             | `a835520d0037`  |
| 2453   | Layout 1             | `a835520d0037`  |
| 2444   | Layout 1             | `a835520d0037`  |
| 2438   | Layout 1             | `a835520d0037`  |
| 2434   | Layout 1             | `a835520d0037`  |
| 2429   | Layout 1             | `a835520d0037`  |
| 2421   | Layout 1             | `a835520d0037`  |
| 2414   | Layout 1             | `a835520d0037`  |
| 2407   | Layout 1             | `a835520d0037`  |
| 2401   | Layout 1             | `a835520d0037`  |
| 2397   | Layout 1             | `a835520d0037`  |
| 2393   | Layout 1             | `a835520d0037`  |
| 2384   | Layout 1             | `a835520d0037`  |
| 2378   | Layout 1             | `a835520d0037`  |
| 2372   | Layout 1             | `a835520d0037`  |
| 2358   | Layout 1             | `a835520d0037`  |
| 2352   | Layout 1             | `a835520d0037`  |
| 2347   | Layout 1             | `a835520d0037`  |
| 2343   | Layout 1             | `a835520d0037`  |
| 2335   | Layout 1             | `a835520d0037`  |
| 2327   | Layout 1             | `a835520d0037`  |
| 2324   | Layout 1             | `a835520d0037`  |
| 2319   | Layout 1             | `a835520d0037`  |
| 2313   | Layout 1             | `a835520d0037`  |
| 2308   | Layout 1             | `a835520d0037`  |
| 2302   | Layout 1             | `a835520d0037`  |
| 2295   | Layout 1             | `a835520d0037`  |
| 2290   | Layout 1             | `a835520d0037`  |
| 2284   | Layout 1             | `a835520d0037`  |
| 2276   | Layout 1             | `a835520d0037`  |
| 2269   | Layout 1             | `a835520d0037`  |
| 2259   | Layout 1             | `a835520d0037`  |
| 2250   | Layout 1             | `a835520d0037`  |
| 2243   | Layout 1             | `a835520d0037`  |
| 2235   | Layout 1             | `a835520d0037`  |
| 2229   | Layout 1             | `a835520d0037`  |
| 2224   | Layout 1             | `a835520d0037`  |
| 2218   | Layout 1             | `a835520d0037`  |
| 2215   | Layout 1             | `a835520d0037`  |
| 2207   | Layout 1             | `a835520d0037`  |
| 2203   | Layout 1             | `a835520d0037`  |
| 2196   | Layout 1             | `a835520d0037`  |
| 2192   | Layout 1             | `a835520d0037`  |
| 2189   | Layout 1             | `a835520d0037`  |
| 2183   | Layout 1             | `a835520d0037`  |
| 2179   | Layout 1             | `a835520d0037`  |
| 2171   | Layout 1             | `a835520d0037`  |
| 2163   | Layout 1             | `a835520d0037`  |
| 2156   | Layout 1             | `a835520d0037`  |
| 2151   | Layout 1             | `a835520d0037`  |
| 2147   | Layout 1             | `a835520d0037`  |
| 2142   | Layout 1             | `a835520d0037`  |
| 2138   | Layout 1             | `a835520d0037`  |
| 2134   | Layout 1             | `a835520d0037`  |
| 2130   | Layout 1             | `a835520d0037`  |
| 2122   | Layout 1             | `a835520d0037`  |
| 2107   | Layout 1             | `a835520d0037`  |
| 2098   | Layout 1             | `a835520d0037`  |
| 2089   | Layout 1             | `a835520d0037`  |
| 2081   | Layout 1             | `a835520d0037`  |
| 2073   | Layout 1             | `a835520d0037`  |
| 2067   | Layout 1             | `a835520d0037`  |
| 2063   | Layout 1             | `a835520d0037`  |
| 2059   | Layout 1             | `a835520d0037`  |
| 2052   | Layout 1             | `a835520d0037`  |
| 2044   | Layout 1             | `a835520d0037`  |
| 2039   | Layout 1             | `a835520d0037`  |
| 2032   | Layout 1             | `a835520d0037`  |
| 2025   | Layout 1             | `a835520d0037`  |
| 2011   | Layout 1             | `a835520d0037`  |
| 2005   | Layout 1             | `a835520d0037`  |
| 2000   | Layout 1             | `a835520d0037`  |
| 1996   | Layout 1             | `a835520d0037`  |
| 1991   | Layout 1             | `a835520d0037`  |
| 1985   | Layout 1             | `a835520d0037`  |
| 1980   | Layout 1             | `a835520d0037`  |
| 1969   | Layout 1             | `a835520d0037`  |
| 1964   | Layout 1             | `a835520d0037`  |
| 1958   | Layout 1             | `a835520d0037`  |
| 1950   | Layout 1             | `a835520d0037`  |
| 1945   | Layout 1             | `a835520d0037`  |
| 1937   | Layout 1             | `a835520d0037`  |
| 1933   | Layout 1             | `a835520d0037`  |
| 1927   | Layout 1             | `a835520d0037`  |
| 1921   | Layout 1             | `a835520d0037`  |
| 1914   | Layout 1             | `a835520d0037`  |
| 1908   | Layout 1             | `a835520d0037`  |
| 1897   | Layout 1             | `a835520d0037`  |
| 1892   | Layout 1             | `a835520d0037`  |
| 1886   | Layout 1             | `a835520d0037`  |
| 1881   | Layout 1             | `a835520d0037`  |
| 1871   | Layout 1             | `a835520d0037`  |
| 1866   | Layout 1             | `a835520d0037`  |
| 1862   | Layout 1             | `a835520d0037`  |
| 1854   | Layout 1             | `a835520d0037`  |
| 1846   | Layout 1             | `a835520d0037`  |
| 1838   | Layout 1             | `a835520d0037`  |
| 1832   | Layout 1             | `a835520d0037`  |
| 1826   | Layout 1             | `a835520d0037`  |
| 1822   | Layout 1             | `a835520d0037`  |
| 1818   | Layout 1             | `a835520d0037`  |
| 1804   | Layout 1             | `a835520d0037`  |
| 1794   | Layout 1             | `a835520d0037`  |
| 1790   | Layout 1             | `a835520d0037`  |
| 1784   | Layout 1             | `a835520d0037`  |
| 1774   | Layout 1             | `a835520d0037`  |
| 1771   | Layout 1             | `a835520d0037`  |
| 1762   | Layout 1             | `a835520d0037`  |
| 1759   | Layout 1             | `a835520d0037`  |
| 1754   | Layout 1             | `a835520d0037`  |
| 1749   | Layout 1             | `a835520d0037`  |
| 1743   | Layout 1             | `a835520d0037`  |
| 1737   | Layout 1             | `a835520d0037`  |
| 1731   | Layout 1             | `a835520d0037`  |
| 1725   | Layout 1             | `a835520d0037`  |
| 1717   | Layout 1             | `a835520d0037`  |
| 1710   | Layout 1             | `a835520d0037`  |
| 1704   | Layout 1             | `a835520d0037`  |
| 1698   | Layout 1             | `a835520d0037`  |
| 1690   | Layout 1             | `a835520d0037`  |
| 1685   | Layout 1             | `a835520d0037`  |
| 1680   | Layout 1             | `a835520d0037`  |
| 1674   | Layout 1             | `a835520d0037`  |
| 1668   | Layout 1             | `a835520d0037`  |
| 1659   | Layout 1             | `a835520d0037`  |
| 1649   | Layout 1             | `a835520d0037`  |
| 1642   | Layout 1             | `a835520d0037`  |
| 1636   | Layout 1             | `a835520d0037`  |
| 1628   | Layout 1             | `a835520d0037`  |
| 1622   | Layout 1             | `a835520d0037`  |
| 1614   | Layout 1             | `a835520d0037`  |
| 1608   | Layout 1             | `a835520d0037`  |
| 1602   | Layout 1             | `a835520d0037`  |
| 1598   | Layout 1             | `a835520d0037`  |
| 1594   | Layout 1             | `a835520d0037`  |
| 1590   | Layout 1             | `a835520d0037`  |
| 1587   | Layout 1             | `a835520d0037`  |
| 1584   | Layout 1             | `a835520d0037`  |
| 1579   | Layout 1             | `a835520d0037`  |
| 1572   | Layout 1             | `a835520d0037`  |
| 1565   | Layout 1             | `a835520d0037`  |
| 1559   | Layout 1             | `a835520d0037`  |
| 1554   | Layout 1             | `a835520d0037`  |
| 1547   | Layout 1             | `a835520d0037`  |
| 1537   | Layout 1             | `a835520d0037`  |
| 1529   | Layout 1             | `a835520d0037`  |
| 1524   | Layout 1             | `a835520d0037`  |
| 1519   | Layout 1             | `a835520d0037`  |
| 1509   | Layout 1             | `a835520d0037`  |
| 1506   | Layout 1             | `a835520d0037`  |
| 1504   | Layout 1             | `a835520d0037`  |
| 1500   | Layout 1             | `a835520d0037`  |
| 1493   | Layout 1             | `a835520d0037`  |
| 1489   | Layout 1             | `a835520d0037`  |
| 1485   | Layout 1             | `a835520d0037`  |
| 1481   | Layout 1             | `a835520d0037`  |
| 1474   | Layout 1             | `a835520d0037`  |
| 1466   | Layout 1             | `a835520d0037`  |
| 1462   | Layout 1             | `a835520d0037`  |
| 1459   | Layout 1             | `a835520d0037`  |
| 1453   | Layout 1             | `a835520d0037`  |
| 1450   | Layout 1             | `a835520d0037`  |
| 1445   | Layout 1             | `a835520d0037`  |
| 1439   | Layout 1             | `a835520d0037`  |
| 1433   | Layout 1             | `a835520d0037`  |
| 1430   | Layout 1             | `a835520d0037`  |
| 1426   | Layout 1             | `a835520d0037`  |
| 1421   | Layout 1             | `a835520d0037`  |
| 1417   | Layout 1             | `a835520d0037`  |
| 1416   | Layout 1             | `a835520d0037`  |
| 1409   | Layout 1             | `a835520d0037`  |
| 1405   | Layout 1             | `a835520d0037`  |
| 1401   | Layout 1             | `a835520d0037`  |
| 1396   | Layout 1             | `a835520d0037`  |
| 1391   | Layout 1             | `a835520d0037`  |
| 1390   | Layout 1             | `a835520d0037`  |
| 1386   | Layout 1             | `a835520d0037`  |
| 1381   | Layout 1             | `a835520d0037`  |
| 1379   | Layout 1             | `a835520d0037`  |
| 1372   | Layout 1             | `a835520d0037`  |
| 1366   | Layout 1             | `a835520d0037`  |
| 1364   | Layout 1             | `a835520d0037`  |
| 1363   | Layout 1             | `a835520d0037`  |
| 1360   | Layout 1             | `a835520d0037`  |
| 1358   | Layout 1             | `a835520d0037`  |
| 1355   | Layout 1             | `a835520d0037`  |
| 1351   | Layout 1             | `a835520d0037`  |
| 1348   | Layout 1             | `a835520d0037`  |
| 1346   | Layout 1             | `a835520d0037`  |
| 1341   | No documented layout | `a835520d0037`  |
| 1340   | No documented layout | `a835520d0037`  |
| 1338   | No documented layout | `a835520d0037`  |
| 1335   | No documented layout | `a835520d0037`  |
| 1333   | No documented layout | `a835520d0037`  |
| 1329   | No documented layout | `a835520d0037`  |
| 1327   | No documented layout | `a835520d0037`  |
| 1324   | No documented layout | `a835520d0037`  |
| 1321   | No documented layout | `a835520d0037`  |
| 1319   | No documented layout | `a835520d0037`  |
| 1318   | No documented layout | `a835520d0037`  |
| 1316   | No documented layout | `a835520d0037`  |
| 1313   | No documented layout | `a835520d0037`  |
| 1311   | No documented layout | `a835520d0037`  |
| 1309   | No documented layout | `a835520d0037`  |
| 1304   | No documented layout | `a835520d0037`  |
| 1292   | No documented layout | `a835520d0037`  |
| 1286   | No file              | `a835520d0037`  |
| 1280   | No file              | `a835520d0037`  |
| 1276   | No file              | `a835520d0037`  |
| 1267   | No file              | `a835520d0037`  |
| 1261   | No file              | `a835520d0037`  |
| 1256   | No file              | `a835520d0037`  |
| 1250   | No file              | `a835520d0037`  |
| 1246   | No file              | `a835520d0037`  |
| 1239   | No file              | `a835520d0037`  |
| 1230   | No file              | `a835520d0037`  |
| 1226   | No file              | `a835520d0037`  |
| 1220   | No file              | `a835520d0037`  |
| 1217   | No file              | `a835520d0037`  |
| 1211   | No file              | `a835520d0037`  |
| 1210   | No file              | `a835520d0037`  |
| 1208   | No file              | `a835520d0037`  |
| 1203   | No file              | `a835520d0037`  |
| 1197   | No file              | `a835520d0037`  |
| 1194   | No file              | `a835520d0037`  |
| 1192   | No file              | `a835520d0037`  |
| 1187   | No file              | `a835520d0037`  |
| 1183   | No file              | `a835520d0037`  |
| 1177   | No file              | `a835520d0037`  |
| 1173   | No file              | `a835520d0037`  |
| 1167   | No file              | `a835520d0037`  |
| 1164   | No file              | `a835520d0037`  |
| 1156   | No file              | `a835520d0037`  |
| 1149   | No file              | `a835520d0037`  |
| 1144   | No file              | `a835520d0037`  |
| 1137   | No file              | `a835520d0037`  |
| 1132   | No file              | `a835520d0037`  |
| 1127   | No file              | `a835520d0037`  |
| 1122   | No file              | `a835520d0037`  |
| 1118   | No file              | `a835520d0037`  |
| 1114   | No file              | `a835520d0037`  |
| 1109   | No file              | `a835520d0037`  |
| 1102   | No file              | `a835520d0037`  |
| 1096   | No file              | `a835520d0037`  |
| 1088   | No file              | `a835520d0037`  |
| 1081   | No file              | `a835520d0037`  |
| 1076   | No file              | `a835520d0037`  |
| 1069   | No file              | `a835520d0037`  |
| 1064   | No file              | `a835520d0037`  |
| 1058   | No file              | `a835520d0037`  |
| 1051   | No file              | `a835520d0037`  |
| 1044   | No file              | `a835520d0037`  |
| 1036   | No file              | `a835520d0037`  |
| 1026   | No file              | `a835520d0037`  |
| 1016   | No file              | `a835520d0037`  |
| 1009   | No file              | `a835520d0037`  |
| 1005   | No file              | `a835520d0037`  |
| 1000   | No file              | `a835520d0037`  |
| 998    | No file              | `a835520d0037`  |
| 990    | No file              | `a835520d0037`  |
| 979    | No file              | `a835520d0037`  |
| 972    | No file              | `a835520d0037`  |
| 963    | No file              | `a835520d0037`  |
| 955    | No file              | `a835520d0037`  |
| 946    | No file              | `a835520d0037`  |
| 938    | No file              | `a835520d0037`  |
| 927    | No file              | `a835520d0037`  |
| 911    | No file              | `a835520d0037`  |
| 904    | No file              | `a835520d0037`  |
| 899    | No file              | `a835520d0037`  |
| 894    | No file              | `a835520d0037`  |
| 885    | No file              | `a835520d0037`  |
| 879    | No file              | `a835520d0037`  |
| 872    | No file              | `a835520d0037`  |
| 864    | No file              | `a835520d0037`  |
| 855    | No file              | `a835520d0037`  |
| 853    | No file              | `a835520d0037`  |
| 845    | No file              | `a835520d0037`  |
| 837    | No file              | `a835520d0037`  |
| 829    | No file              | `a835520d0037`  |
| 822    | No file              | `a835520d0037`  |
| 814    | No file              | `a835520d0037`  |
| 805    | No file              | `a835520d0037`  |
| 794    | No file              | `a835520d0037`  |
| 787    | No file              | `a835520d0037`  |
| 780    | No file              | `a835520d0037`  |
| 771    | No file              | `a835520d0037`  |
| 760    | No file              | `a835520d0037`  |
| 748    | No file              | `a835520d0037`  |
| 741    | No file              | `a835520d0037`  |
| 736    | No file              | `a835520d0037`  |
| 731    | No file              | `a835520d0037`  |
| 723    | No file              | `a835520d0037`  |
| 711    | No file              | `a835520d0037`  |
| 707    | No file              | `a835520d0037`  |
| 697    | No file              | `a835520d0037`  |
| 689    | No file              | `a835520d0037`  |
| 683    | No file              | `a835520d0037`  |
| 678    | No file              | `a835520d0037`  |
| 670    | No file              | `a835520d0037`  |
| 661    | No file              | `a835520d0037`  |
| 656    | No file              | `a835520d0037`  |
| 652    | No file              | `a835520d0037`  |
| 643    | No file              | `a835520d0037`  |
| 637    | No file              | `a835520d0037`  |
| 630    | No file              | `a835520d0037`  |
| 627    | No file              | `a835520d0037`  |
| 621    | No file              | `a835520d0037`  |
| 617    | No file              | `a835520d0037`  |
| 615    | No file              | `a835520d0037`  |
| 606    | No file              | `a835520d0037`  |
| 599    | No file              | `a835520d0037`  |
| 592    | No file              | `a835520d0037`  |
| 586    | No file              | `a835520d0037`  |
| 577    | No file              | `a835520d0037`  |
| 569    | No file              | `a835520d0037`  |
| 561    | No file              | `a835520d0037`  |
| 554    | No file              | `a835520d0037`  |
| 542    | No file              | `a835520d0037`  |
| 532    | No file              | `a835520d0037`  |
| 531    | No file              | `a835520d0037`  |
| 526    | No file              | `a835520d0037`  |
| 521    | No file              | `a835520d0037`  |
| 517    | No file              | `a835520d0037`  |
| 510    | No file              | `a835520d0037`  |
| 508    | No file              | `a835520d0037`  |
| 504    | No file              | `a835520d0037`  |
| 497    | No file              | `a835520d0037`  |
| 491    | No file              | `a835520d0037`  |
| 485    | No file              | `a835520d0037`  |
| 478    | No file              | `a835520d0037`  |
| 472    | No file              | `a835520d0037`  |
| 466    | No file              | `a835520d0037`  |
| 457    | No file              | `a835520d0037`  |
| 452    | No file              | `a835520d0037`  |
| 449    | No file              | `a835520d0037`  |
| 435    | No file              | `a835520d0037`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                      |
| ---------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `guildhouseinfooffset.dbss`  | Optional | `character_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `houseinforeceipe.dbss`      | Optional | Korean receipe names for the uses when LOC has none                                        |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a house key without a row shows as plain text          |
| `languagedata_en.loc`        | Optional | House names (type 6), town names (type 17), node names (type 29), receipe names (type 16)  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3482 the file is 974 bytes: 12 rows of four uses (46 bytes) and
11 of three (38 bytes).

### Row (variable: 14 bytes + crafts)

| Offset        | Type               | Field             | Notes                                                                                   |
| ------------- | ------------------ | ----------------- | --------------------------------------------------------------------------------------- |
| `+0x00`       | u16                | affiliated_town   | Town the house belongs to, a `regioninfo.bss` region key (LOC type 17: `5` Velia, `229` Valencia City) |
| `+0x02`       | u32                | parent_node_key   | Worldmap node of the house (LOC type 29); `getParentNodeKey()`                          |
| `+0x06`       | u32                | craft_count       | Number of `crafts`; `getReceipeCount()`                                                  |
| `+0x0A`       | Craft[craft_count] | crafts            | The uses the house can be set to; see Craft                                             |
| `crafts+0x00` | u16                | character_key     | Row key: the house's `characterstatic.dbss` character                                    |
| `crafts+0x02` | u16                | unknown_crafts_02 | `0xFFFF` on every row (clients 1784 and 3482); see Open Questions                        |

### Craft (8 bytes)

| Offset  | Type | Field       | Notes                                                                       |
| ------- | ---- | ----------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | receipe_key | [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) receipe key; `getHouseCraftWrapperByIndex(i):getReceipeKeyRaw()` |
| `+0x04` | u32  | level       | Highest level of the use in this house; `getMaxLevel(receipeKey)`            |

Every row (client 3482) ends with receipe `1610` (Mount Part Workshop) at
level 1, `2` (Storage) at level 5 and `50001` (Guild Storage level 2) at
level 3. The four-use rows open with `1601` (Guild Shipyard) or `1602`
(Elephant Nursery) at level 2.

### `guildhouseinfooffset.dbss`

Bare offset table into `guildhouseinfo.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `guildhouseinfo.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                           |
| ------- | ---- | ------------- | --------------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                                     |
| `+0x02` | u32  | data_offset   | Absolute offset of the row in `guildhouseinfo.dbss`, at `affiliated_town` |
| `+0x06` | u32  | data_size     | The whole row: `46` or `38` bytes                               |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3482 every
index row points at a row whose `character_key` is its key.

## Field Names

The `GuildHouseInfo` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CharacterKey`, `AffiliatedTown`, `ParentNode`
and `CraftList` (`1601:2, 1610:1, 2:5, 50001:3`). The 2016
`gc::GuildHouseInfoStaticStatus` holds `_affiliatedTownKey`,
`_parentNodeKey`, `_houseCraftList` (`gc::HouseInfoCraft`: `_receipeKey`,
`_level`) and `_key`, in the file's order.

| Field           | Column           | Same value (client 1784) |
| --------------- | ---------------- | ------------------------ |
| character_key   | `CharacterKey`   | 23 of 23                 |
| affiliated_town | `AffiliatedTown` | 23 of 23                 |
| parent_node_key | `ParentNode`     | 23 of 23                 |
| crafts          | `CraftList`      | 23 of 23                 |

## Notes

- The guild house Lua (`worldmap_grand_guildcraft.luac`,
  `worldmap_grand_guildhousecontrol.luac`,
  `panel_worldmap_guildhousemanagement_renew.luac`) calls `getHouseName()`,
  `getParentNodeKey()`, `getReceipeCount()`,
  `getHouseCraftWrapperByIndex(index)`, `getHouseCraftWrapperByKeyRaw(key)`
  and `getMaxLevel(receipeKey)` on the wrapper.
- Guild houses of one town share a node: the seven Calpheon City guild
  houses (`2427` to `2704`) node `601`, the four Valencia City houses
  `3355` to `3358` node `1301`. The houses `3351` to `3354` of town `650`
  sit on four different nodes.
- Grána (`3520`) and O'draxxia (`3806`) Guild Houses are house characters of
  [`householdlist.bss`](householdlist_bss.md) with no row here.

## Open Questions

### What `unknown_crafts_02` Holds

The u16 after the key is `0xFFFF` on all 23 rows of clients 1784 and 3482,
as `unknown_0a` after the key of [`houseinfo.bss`](houseinfo_bss.md). The
2016 `gc::GuildHouseInfoStaticStatus` follows `_key` with
`bool _isBlockedNpcWork` and `KeyType<short,-1> _territoryKey`, whose unset
value is `-1`; no sheet column fills it, so the field is not named.
