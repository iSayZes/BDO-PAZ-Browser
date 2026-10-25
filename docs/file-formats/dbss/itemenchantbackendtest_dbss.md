# `itemenchantbackendtest.dbss` Format

## Purpose

The front part of every [`itemenchant.dbss`](itemenchant_dbss.md) block:
for each (item, enchant level) the block from its packed key to
`life_restrict_type`, `0x2A` bytes into the Message Tail. Everything after
that, from Message Tail `+0x2B` to the crystal group at the block end, is in
[`itemenchantbackend.dbss`](itemenchantbackend_dbss.md). On client 3483
each of the 169,345 `itemenchant.dbss` blocks is, byte for byte, the block
of this file followed by the `itemenchantbackend.dbss` block of the same
key, and the file sizes add up: 76,122,866 + 126,919,140 bytes is the
203,042,002 of `itemenchant.dbss` plus one 4-byte count.

Unlike its two siblings, this file has no offset index: the blocks follow
each other in the order of `itemenchantoffset.dbss`, and a reader finds the
end of a block by walking its lists and strings.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes      | Records                                                                     | Row bytes |
| ------ | -------------- | ----------------------------- | ---------- | --------------------------------------------------------------------------- | --------- |
| 2      | 3435 and later | `itemenchantbackendtest.dbss` | 76,122,866 | 276,167 Class Entry, 169,345 Icon Tail, 169,345 Message Tail, 169,345 Block | 5         |
| 1      | 3426           | `itemenchantbackendtest.dbss` | 76,474,847 | 293,909 Class Entry, 169,255 Icon Tail, 169,255 Message Tail, 169,255 Block | 5         |

| Layout | File                          | Known                | Unknown              |
| ------ | ----------------------------- | -------------------- | -------------------- |
| 2      | `itemenchantbackendtest.dbss` | 58,866,318 B (77.3%) | 17,256,548 B (22.7%) |
| 1      | `itemenchantbackendtest.dbss` | 58,719,534 B (76.8%) | 17,755,313 B (23.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `9230ddc2971f`  |
| 3482   | Layout 2             | `9230ddc2971f`  |
| 3474   | Layout 2             | `9230ddc2971f`  |
| 3473   | Layout 2             | `9230ddc2971f`  |
| 3464   | Layout 2             | `9230ddc2971f`  |
| 3458   | Layout 2             | `9230ddc2971f`  |
| 3454   | Layout 2             | `9230ddc2971f`  |
| 3444   | Layout 2             | `9230ddc2971f`  |
| 3435   | Layout 2             | `9230ddc2971f`  |
| 3426   | Layout 1             | `9230ddc2971f`  |
| 3418   | No documented layout | `9230ddc2971f`  |
| 3412   | No documented layout | `9230ddc2971f`  |
| 3402   | No documented layout | `9230ddc2971f`  |
| 3396   | No documented layout | `9230ddc2971f`  |
| 3387   | No documented layout | `9230ddc2971f`  |
| 3381   | No documented layout | `9230ddc2971f`  |
| 3373   | No documented layout | `9230ddc2971f`  |
| 3364   | No documented layout | `9230ddc2971f`  |
| 3356   | No documented layout | `9230ddc2971f`  |
| 3349   | No documented layout | `9230ddc2971f`  |
| 3342   | No documented layout | `9230ddc2971f`  |
| 3335   | No documented layout | `9230ddc2971f`  |
| 3326   | No documented layout | `9230ddc2971f`  |
| 3321   | No documented layout | `9230ddc2971f`  |
| 3314   | No documented layout | `9230ddc2971f`  |
| 3303   | No documented layout | `9230ddc2971f`  |
| 3302   | No documented layout | `9230ddc2971f`  |
| 3293   | No documented layout | `9230ddc2971f`  |
| 3283   | No documented layout | `9230ddc2971f`  |
| 3275   | No documented layout | `9230ddc2971f`  |
| 3267   | No documented layout | `9230ddc2971f`  |
| 3258   | No documented layout | `9230ddc2971f`  |
| 3251   | No documented layout | `9230ddc2971f`  |
| 3242   | No documented layout | `9230ddc2971f`  |
| 3235   | No documented layout | `9230ddc2971f`  |
| 3229   | No documented layout | `9230ddc2971f`  |
| 3212   | No documented layout | `9230ddc2971f`  |
| 3203   | No documented layout | `9230ddc2971f`  |
| 3193   | No documented layout | `9230ddc2971f`  |
| 3186   | No documented layout | `9230ddc2971f`  |
| 3177   | No documented layout | `9230ddc2971f`  |
| 3169   | No documented layout | `9230ddc2971f`  |
| 3158   | No documented layout | `9230ddc2971f`  |
| 3151   | No documented layout | `9230ddc2971f`  |
| 3144   | No documented layout | `9230ddc2971f`  |
| 3133   | No documented layout | `9230ddc2971f`  |
| 3125   | No documented layout | `9230ddc2971f`  |
| 3118   | No documented layout | `9230ddc2971f`  |
| 3111   | No documented layout | `9230ddc2971f`  |
| 3103   | No documented layout | `9230ddc2971f`  |
| 3095   | No documented layout | `9230ddc2971f`  |
| 3086   | No documented layout | `9230ddc2971f`  |
| 3072   | No documented layout | `9230ddc2971f`  |
| 3062   | No documented layout | `9230ddc2971f`  |
| 3052   | No documented layout | `9230ddc2971f`  |
| 3045   | No documented layout | `9230ddc2971f`  |
| 3037   | No documented layout | `9230ddc2971f`  |
| 3030   | No documented layout | `9230ddc2971f`  |
| 3021   | No documented layout | `9230ddc2971f`  |
| 3012   | No documented layout | `9230ddc2971f`  |
| 3002   | No documented layout | `9230ddc2971f`  |
| 2995   | No documented layout | `9230ddc2971f`  |
| 2987   | No documented layout | `9230ddc2971f`  |
| 2978   | No documented layout | `9230ddc2971f`  |
| 2970   | No documented layout | `9230ddc2971f`  |
| 2959   | No documented layout | `9230ddc2971f`  |
| 2951   | No documented layout | `9230ddc2971f`  |
| 2942   | No documented layout | `9230ddc2971f`  |
| 2935   | No documented layout | `9230ddc2971f`  |
| 2932   | No documented layout | `9230ddc2971f`  |
| 2923   | No documented layout | `9230ddc2971f`  |
| 2919   | No documented layout | `9230ddc2971f`  |
| 2907   | No documented layout | `9230ddc2971f`  |
| 2900   | No documented layout | `9230ddc2971f`  |
| 2891   | No documented layout | `9230ddc2971f`  |
| 2882   | No documented layout | `9230ddc2971f`  |
| 2872   | No documented layout | `9230ddc2971f`  |
| 2863   | No documented layout | `9230ddc2971f`  |
| 2855   | No documented layout | `9230ddc2971f`  |
| 2849   | No documented layout | `9230ddc2971f`  |
| 2844   | No documented layout | `9230ddc2971f`  |
| 2834   | No documented layout | `9230ddc2971f`  |
| 2825   | No documented layout | `9230ddc2971f`  |
| 2819   | No documented layout | `9230ddc2971f`  |
| 2811   | No documented layout | `9230ddc2971f`  |
| 2803   | No documented layout | `9230ddc2971f`  |
| 2794   | No documented layout | `9230ddc2971f`  |
| 2783   | No documented layout | `9230ddc2971f`  |
| 2774   | No documented layout | `9230ddc2971f`  |
| 2765   | No documented layout | `9230ddc2971f`  |
| 2756   | No documented layout | `9230ddc2971f`  |
| 2750   | No documented layout | `9230ddc2971f`  |
| 2743   | No documented layout | `9230ddc2971f`  |
| 2736   | No documented layout | `9230ddc2971f`  |
| 2726   | No documented layout | `9230ddc2971f`  |
| 2717   | No documented layout | `9230ddc2971f`  |
| 2709   | No documented layout | `9230ddc2971f`  |
| 2703   | No documented layout | `9230ddc2971f`  |
| 2695   | No documented layout | `9230ddc2971f`  |
| 2684   | No documented layout | `9230ddc2971f`  |
| 2672   | No documented layout | `9230ddc2971f`  |
| 2665   | No documented layout | `9230ddc2971f`  |
| 2657   | No documented layout | `9230ddc2971f`  |
| 2649   | No documented layout | `9230ddc2971f`  |
| 2644   | No documented layout | `9230ddc2971f`  |
| 2637   | No documented layout | `9230ddc2971f`  |
| 2629   | No documented layout | `9230ddc2971f`  |
| 2619   | No documented layout | `9230ddc2971f`  |
| 2612   | No documented layout | `9230ddc2971f`  |
| 2606   | No documented layout | `9230ddc2971f`  |
| 2602   | No documented layout | `9230ddc2971f`  |
| 2601   | No documented layout | `9230ddc2971f`  |
| 2592   | No documented layout | `9230ddc2971f`  |
| 2583   | No documented layout | `9230ddc2971f`  |
| 2575   | No documented layout | `9230ddc2971f`  |
| 2567   | No documented layout | `9230ddc2971f`  |
| 2560   | No documented layout | `9230ddc2971f`  |
| 2553   | No documented layout | `9230ddc2971f`  |
| 2545   | No documented layout | `9230ddc2971f`  |
| 2538   | No documented layout | `9230ddc2971f`  |
| 2529   | No documented layout | `9230ddc2971f`  |
| 2519   | No documented layout | `9230ddc2971f`  |
| 2513   | No documented layout | `9230ddc2971f`  |
| 2510   | No documented layout | `9230ddc2971f`  |
| 2507   | No documented layout | `9230ddc2971f`  |
| 2503   | No documented layout | `9230ddc2971f`  |
| 2498   | No documented layout | `9230ddc2971f`  |
| 2492   | No documented layout | `9230ddc2971f`  |
| 2487   | No documented layout | `9230ddc2971f`  |
| 2480   | No documented layout | `9230ddc2971f`  |
| 2474   | No documented layout | `9230ddc2971f`  |
| 2468   | No documented layout | `9230ddc2971f`  |
| 2460   | No documented layout | `9230ddc2971f`  |
| 2453   | No documented layout | `9230ddc2971f`  |
| 2444   | No documented layout | `9230ddc2971f`  |
| 2438   | No documented layout | `9230ddc2971f`  |
| 2434   | No documented layout | `9230ddc2971f`  |
| 2429   | No documented layout | `9230ddc2971f`  |
| 2421   | No documented layout | `9230ddc2971f`  |
| 2414   | No documented layout | `9230ddc2971f`  |
| 2407   | No documented layout | `9230ddc2971f`  |
| 2401   | No documented layout | `9230ddc2971f`  |
| 2397   | No documented layout | `9230ddc2971f`  |
| 2393   | No documented layout | `9230ddc2971f`  |
| 2384   | No documented layout | `9230ddc2971f`  |
| 2378   | No documented layout | `9230ddc2971f`  |
| 2372   | No documented layout | `9230ddc2971f`  |
| 2358   | No documented layout | `9230ddc2971f`  |
| 2352   | No documented layout | `9230ddc2971f`  |
| 2347   | No documented layout | `9230ddc2971f`  |
| 2343   | No documented layout | `9230ddc2971f`  |
| 2335   | No documented layout | `9230ddc2971f`  |
| 2327   | No documented layout | `9230ddc2971f`  |
| 2324   | No documented layout | `9230ddc2971f`  |
| 2319   | No documented layout | `9230ddc2971f`  |
| 2313   | No documented layout | `9230ddc2971f`  |
| 2308   | No documented layout | `9230ddc2971f`  |
| 2302   | No documented layout | `9230ddc2971f`  |
| 2295   | No documented layout | `9230ddc2971f`  |
| 2290   | No documented layout | `9230ddc2971f`  |
| 2284   | No documented layout | `9230ddc2971f`  |
| 2276   | No documented layout | `9230ddc2971f`  |
| 2269   | No documented layout | `9230ddc2971f`  |
| 2259   | No documented layout | `9230ddc2971f`  |
| 2250   | No documented layout | `9230ddc2971f`  |
| 2243   | No documented layout | `9230ddc2971f`  |
| 2235   | No documented layout | `9230ddc2971f`  |
| 2229   | No documented layout | `9230ddc2971f`  |
| 2224   | No documented layout | `9230ddc2971f`  |
| 2218   | No documented layout | `9230ddc2971f`  |
| 2215   | No documented layout | `9230ddc2971f`  |
| 2207   | No documented layout | `9230ddc2971f`  |
| 2203   | No documented layout | `9230ddc2971f`  |
| 2196   | No documented layout | `9230ddc2971f`  |
| 2192   | No documented layout | `9230ddc2971f`  |
| 2189   | No documented layout | `9230ddc2971f`  |
| 2183   | No documented layout | `9230ddc2971f`  |
| 2179   | No documented layout | `9230ddc2971f`  |
| 2171   | No documented layout | `9230ddc2971f`  |
| 2163   | No documented layout | `9230ddc2971f`  |
| 2156   | No documented layout | `9230ddc2971f`  |
| 2151   | No documented layout | `9230ddc2971f`  |
| 2147   | No documented layout | `9230ddc2971f`  |
| 2142   | No documented layout | `9230ddc2971f`  |
| 2138   | No documented layout | `9230ddc2971f`  |
| 2134   | No documented layout | `9230ddc2971f`  |
| 2130   | No documented layout | `9230ddc2971f`  |
| 2122   | No documented layout | `9230ddc2971f`  |
| 2107   | No documented layout | `9230ddc2971f`  |
| 2098   | No documented layout | `9230ddc2971f`  |
| 2089   | No documented layout | `9230ddc2971f`  |
| 2081   | No documented layout | `9230ddc2971f`  |
| 2073   | No documented layout | `9230ddc2971f`  |
| 2067   | No documented layout | `9230ddc2971f`  |
| 2063   | No documented layout | `9230ddc2971f`  |
| 2059   | No documented layout | `9230ddc2971f`  |
| 2052   | No documented layout | `9230ddc2971f`  |
| 2044   | No documented layout | `9230ddc2971f`  |
| 2039   | No documented layout | `9230ddc2971f`  |
| 2032   | No documented layout | `9230ddc2971f`  |
| 2025   | No documented layout | `9230ddc2971f`  |
| 2011   | No documented layout | `9230ddc2971f`  |
| 2005   | No documented layout | `9230ddc2971f`  |
| 2000   | No documented layout | `9230ddc2971f`  |
| 1996   | No documented layout | `9230ddc2971f`  |
| 1991   | No documented layout | `9230ddc2971f`  |
| 1985   | No documented layout | `9230ddc2971f`  |
| 1980   | No documented layout | `9230ddc2971f`  |
| 1969   | No file              | `9230ddc2971f`  |
| 1964   | No file              | `9230ddc2971f`  |
| 1958   | No file              | `9230ddc2971f`  |
| 1950   | No file              | `9230ddc2971f`  |
| 1945   | No file              | `9230ddc2971f`  |
| 1937   | No file              | `9230ddc2971f`  |
| 1933   | No file              | `9230ddc2971f`  |
| 1927   | No file              | `9230ddc2971f`  |
| 1921   | No file              | `9230ddc2971f`  |
| 1914   | No file              | `9230ddc2971f`  |
| 1908   | No file              | `9230ddc2971f`  |
| 1897   | No file              | `9230ddc2971f`  |
| 1892   | No file              | `9230ddc2971f`  |
| 1886   | No file              | `9230ddc2971f`  |
| 1881   | No file              | `9230ddc2971f`  |
| 1871   | No file              | `9230ddc2971f`  |
| 1866   | No file              | `9230ddc2971f`  |
| 1862   | No file              | `9230ddc2971f`  |
| 1854   | No file              | `9230ddc2971f`  |
| 1846   | No file              | `9230ddc2971f`  |
| 1838   | No file              | `9230ddc2971f`  |
| 1832   | No file              | `9230ddc2971f`  |
| 1826   | No file              | `9230ddc2971f`  |
| 1822   | No file              | `9230ddc2971f`  |
| 1818   | No file              | `9230ddc2971f`  |
| 1804   | No file              | `9230ddc2971f`  |
| 1794   | No file              | `9230ddc2971f`  |
| 1790   | No file              | `9230ddc2971f`  |
| 1784   | No file              | `9230ddc2971f`  |
| 1774   | No file              | `9230ddc2971f`  |
| 1771   | No file              | `9230ddc2971f`  |
| 1762   | No file              | `9230ddc2971f`  |
| 1759   | No file              | `9230ddc2971f`  |
| 1754   | No file              | `9230ddc2971f`  |
| 1749   | No file              | `9230ddc2971f`  |
| 1743   | No file              | `9230ddc2971f`  |
| 1737   | No file              | `9230ddc2971f`  |
| 1731   | No file              | `9230ddc2971f`  |
| 1725   | No file              | `9230ddc2971f`  |
| 1717   | No file              | `9230ddc2971f`  |
| 1710   | No file              | `9230ddc2971f`  |
| 1704   | No file              | `9230ddc2971f`  |
| 1698   | No file              | `9230ddc2971f`  |
| 1690   | No file              | `9230ddc2971f`  |
| 1685   | No file              | `9230ddc2971f`  |
| 1680   | No file              | `9230ddc2971f`  |
| 1674   | No file              | `9230ddc2971f`  |
| 1668   | No file              | `9230ddc2971f`  |
| 1659   | No file              | `9230ddc2971f`  |
| 1649   | No file              | `9230ddc2971f`  |
| 1642   | No file              | `9230ddc2971f`  |
| 1636   | No file              | `9230ddc2971f`  |
| 1628   | No file              | `9230ddc2971f`  |
| 1622   | No file              | `9230ddc2971f`  |
| 1614   | No file              | `9230ddc2971f`  |
| 1608   | No file              | `9230ddc2971f`  |
| 1602   | No file              | `9230ddc2971f`  |
| 1598   | No file              | `9230ddc2971f`  |
| 1594   | No file              | `9230ddc2971f`  |
| 1590   | No file              | `9230ddc2971f`  |
| 1587   | No file              | `9230ddc2971f`  |
| 1584   | No file              | `9230ddc2971f`  |
| 1579   | No file              | `9230ddc2971f`  |
| 1572   | No file              | `9230ddc2971f`  |
| 1565   | No file              | `9230ddc2971f`  |
| 1559   | No file              | `9230ddc2971f`  |
| 1554   | No file              | `9230ddc2971f`  |
| 1547   | No file              | `9230ddc2971f`  |
| 1537   | No file              | `9230ddc2971f`  |
| 1529   | No file              | `9230ddc2971f`  |
| 1524   | No file              | `9230ddc2971f`  |
| 1519   | No file              | `9230ddc2971f`  |
| 1509   | No file              | `9230ddc2971f`  |
| 1506   | No file              | `9230ddc2971f`  |
| 1504   | No file              | `9230ddc2971f`  |
| 1500   | No file              | `9230ddc2971f`  |
| 1493   | No file              | `9230ddc2971f`  |
| 1489   | No file              | `9230ddc2971f`  |
| 1485   | No file              | `9230ddc2971f`  |
| 1481   | No file              | `9230ddc2971f`  |
| 1474   | No file              | `9230ddc2971f`  |
| 1466   | No file              | `9230ddc2971f`  |
| 1462   | No file              | `9230ddc2971f`  |
| 1459   | No file              | `9230ddc2971f`  |
| 1453   | No file              | `9230ddc2971f`  |
| 1450   | No file              | `9230ddc2971f`  |
| 1445   | No file              | `9230ddc2971f`  |
| 1439   | No file              | `9230ddc2971f`  |
| 1433   | No file              | `9230ddc2971f`  |
| 1430   | No file              | `9230ddc2971f`  |
| 1426   | No file              | `9230ddc2971f`  |
| 1421   | No file              | `9230ddc2971f`  |
| 1417   | No file              | `9230ddc2971f`  |
| 1416   | No file              | `9230ddc2971f`  |
| 1409   | No file              | `9230ddc2971f`  |
| 1405   | No file              | `9230ddc2971f`  |
| 1401   | No file              | `9230ddc2971f`  |
| 1396   | No file              | `9230ddc2971f`  |
| 1391   | No file              | `9230ddc2971f`  |
| 1390   | No file              | `9230ddc2971f`  |
| 1386   | No file              | `9230ddc2971f`  |
| 1381   | No file              | `9230ddc2971f`  |
| 1379   | No file              | `9230ddc2971f`  |
| 1372   | No file              | `9230ddc2971f`  |
| 1366   | No file              | `9230ddc2971f`  |
| 1364   | No file              | `9230ddc2971f`  |
| 1363   | No file              | `9230ddc2971f`  |
| 1360   | No file              | `9230ddc2971f`  |
| 1358   | No file              | `9230ddc2971f`  |
| 1355   | No file              | `9230ddc2971f`  |
| 1351   | No file              | `9230ddc2971f`  |
| 1348   | No file              | `9230ddc2971f`  |
| 1346   | No file              | `9230ddc2971f`  |
| 1341   | No file              | `9230ddc2971f`  |
| 1340   | No file              | `9230ddc2971f`  |
| 1338   | No file              | `9230ddc2971f`  |
| 1335   | No file              | `9230ddc2971f`  |
| 1333   | No file              | `9230ddc2971f`  |
| 1329   | No file              | `9230ddc2971f`  |
| 1327   | No file              | `9230ddc2971f`  |
| 1324   | No file              | `9230ddc2971f`  |
| 1321   | No file              | `9230ddc2971f`  |
| 1319   | No file              | `9230ddc2971f`  |
| 1318   | No file              | `9230ddc2971f`  |
| 1316   | No file              | `9230ddc2971f`  |
| 1313   | No file              | `9230ddc2971f`  |
| 1311   | No file              | `9230ddc2971f`  |
| 1309   | No file              | `9230ddc2971f`  |
| 1304   | No file              | `9230ddc2971f`  |
| 1292   | No file              | `9230ddc2971f`  |
| 1286   | No file              | `9230ddc2971f`  |
| 1280   | No file              | `9230ddc2971f`  |
| 1276   | No file              | `9230ddc2971f`  |
| 1267   | No file              | `9230ddc2971f`  |
| 1261   | No file              | `9230ddc2971f`  |
| 1256   | No file              | `9230ddc2971f`  |
| 1250   | No file              | `9230ddc2971f`  |
| 1246   | No file              | `9230ddc2971f`  |
| 1239   | No file              | `9230ddc2971f`  |
| 1230   | No file              | `9230ddc2971f`  |
| 1226   | No file              | `9230ddc2971f`  |
| 1220   | No file              | `9230ddc2971f`  |
| 1217   | No file              | `9230ddc2971f`  |
| 1211   | No file              | `9230ddc2971f`  |
| 1210   | No file              | `9230ddc2971f`  |
| 1208   | No file              | `9230ddc2971f`  |
| 1203   | No file              | `9230ddc2971f`  |
| 1197   | No file              | `9230ddc2971f`  |
| 1194   | No file              | `9230ddc2971f`  |
| 1192   | No file              | `9230ddc2971f`  |
| 1187   | No file              | `9230ddc2971f`  |
| 1183   | No file              | `9230ddc2971f`  |
| 1177   | No file              | `9230ddc2971f`  |
| 1173   | No file              | `9230ddc2971f`  |
| 1167   | No file              | `9230ddc2971f`  |
| 1164   | No file              | `9230ddc2971f`  |
| 1156   | No file              | `9230ddc2971f`  |
| 1149   | No file              | `9230ddc2971f`  |
| 1144   | No file              | `9230ddc2971f`  |
| 1137   | No file              | `9230ddc2971f`  |
| 1132   | No file              | `9230ddc2971f`  |
| 1127   | No file              | `9230ddc2971f`  |
| 1122   | No file              | `9230ddc2971f`  |
| 1118   | No file              | `9230ddc2971f`  |
| 1114   | No file              | `9230ddc2971f`  |
| 1109   | No file              | `9230ddc2971f`  |
| 1102   | No file              | `9230ddc2971f`  |
| 1096   | No file              | `9230ddc2971f`  |
| 1088   | No file              | `9230ddc2971f`  |
| 1081   | No file              | `9230ddc2971f`  |
| 1076   | No file              | `9230ddc2971f`  |
| 1069   | No file              | `9230ddc2971f`  |
| 1064   | No file              | `9230ddc2971f`  |
| 1058   | No file              | `9230ddc2971f`  |
| 1051   | No file              | `9230ddc2971f`  |
| 1044   | No file              | `9230ddc2971f`  |
| 1036   | No file              | `9230ddc2971f`  |
| 1026   | No file              | `9230ddc2971f`  |
| 1016   | No file              | `9230ddc2971f`  |
| 1009   | No file              | `9230ddc2971f`  |
| 1005   | No file              | `9230ddc2971f`  |
| 1000   | No file              | `9230ddc2971f`  |
| 998    | No file              | `9230ddc2971f`  |
| 990    | No file              | `9230ddc2971f`  |
| 979    | No file              | `9230ddc2971f`  |
| 972    | No file              | `9230ddc2971f`  |
| 963    | No file              | `9230ddc2971f`  |
| 955    | No file              | `9230ddc2971f`  |
| 946    | No file              | `9230ddc2971f`  |
| 938    | No file              | `9230ddc2971f`  |
| 927    | No file              | `9230ddc2971f`  |
| 911    | No file              | `9230ddc2971f`  |
| 904    | No file              | `9230ddc2971f`  |
| 899    | No file              | `9230ddc2971f`  |
| 894    | No file              | `9230ddc2971f`  |
| 885    | No file              | `9230ddc2971f`  |
| 879    | No file              | `9230ddc2971f`  |
| 872    | No file              | `9230ddc2971f`  |
| 864    | No file              | `9230ddc2971f`  |
| 855    | No file              | `9230ddc2971f`  |
| 853    | No file              | `9230ddc2971f`  |
| 845    | No file              | `9230ddc2971f`  |
| 837    | No file              | `9230ddc2971f`  |
| 829    | No file              | `9230ddc2971f`  |
| 822    | No file              | `9230ddc2971f`  |
| 814    | No file              | `9230ddc2971f`  |
| 805    | No file              | `9230ddc2971f`  |
| 794    | No file              | `9230ddc2971f`  |
| 787    | No file              | `9230ddc2971f`  |
| 780    | No file              | `9230ddc2971f`  |
| 771    | No file              | `9230ddc2971f`  |
| 760    | No file              | `9230ddc2971f`  |
| 748    | No file              | `9230ddc2971f`  |
| 741    | No file              | `9230ddc2971f`  |
| 736    | No file              | `9230ddc2971f`  |
| 731    | No file              | `9230ddc2971f`  |
| 723    | No file              | `9230ddc2971f`  |
| 711    | No file              | `9230ddc2971f`  |
| 707    | No file              | `9230ddc2971f`  |
| 697    | No file              | `9230ddc2971f`  |
| 689    | No file              | `9230ddc2971f`  |
| 683    | No file              | `9230ddc2971f`  |
| 678    | No file              | `9230ddc2971f`  |
| 670    | No file              | `9230ddc2971f`  |
| 661    | No file              | `9230ddc2971f`  |
| 656    | No file              | `9230ddc2971f`  |
| 652    | No file              | `9230ddc2971f`  |
| 643    | No file              | `9230ddc2971f`  |
| 637    | No file              | `9230ddc2971f`  |
| 630    | No file              | `9230ddc2971f`  |
| 627    | No file              | `9230ddc2971f`  |
| 621    | No file              | `9230ddc2971f`  |
| 617    | No file              | `9230ddc2971f`  |
| 615    | No file              | `9230ddc2971f`  |
| 606    | No file              | `9230ddc2971f`  |
| 599    | No file              | `9230ddc2971f`  |
| 592    | No file              | `9230ddc2971f`  |
| 586    | No file              | `9230ddc2971f`  |
| 577    | No file              | `9230ddc2971f`  |
| 569    | No file              | `9230ddc2971f`  |
| 561    | No file              | `9230ddc2971f`  |
| 554    | No file              | `9230ddc2971f`  |
| 542    | No file              | `9230ddc2971f`  |
| 532    | No file              | `9230ddc2971f`  |
| 531    | No file              | `9230ddc2971f`  |
| 526    | No file              | `9230ddc2971f`  |
| 521    | No file              | `9230ddc2971f`  |
| 517    | No file              | `9230ddc2971f`  |
| 510    | No file              | `9230ddc2971f`  |
| 508    | No file              | `9230ddc2971f`  |
| 504    | No file              | `9230ddc2971f`  |
| 497    | No file              | `9230ddc2971f`  |
| 491    | No file              | `9230ddc2971f`  |
| 485    | No file              | `9230ddc2971f`  |
| 478    | No file              | `9230ddc2971f`  |
| 472    | No file              | `9230ddc2971f`  |
| 466    | No file              | `9230ddc2971f`  |
| 457    | No file              | `9230ddc2971f`  |
| 452    | No file              | `9230ddc2971f`  |
| 449    | No file              | `9230ddc2971f`  |
| 435    | No file              | `9230ddc2971f`  |

<!-- versions:end -->

## Companion Files

The blocks need no companion: the walk gives each block's size. The handler
reads the same optional data as the `itemenchant.dbss` one, minus the
crystal groups, which this file does not store.

| File                  | Required | Role                                                                                 |
| --------------------- | -------- | ------------------------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Item name and description for the item ID (`str_type=0`, `str_id4` 0 and 1)         |
| `skill.dbss`          | Optional | The buffs of `skill_key_1` and `skill_key_2`, through the `SKILL_BUFFS` lookup index  |
| `lightstoneset.bss`   | Optional | The Lightstone sets an item counts toward, through the `LIGHTSTONE_SETS` lookup index |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type         | Field  | Notes |
| ------- | ------------ | ------ | ----- |
| `+0x00` | u32          | count  | Block count, the row count of `itemenchantoffset.dbss` |
| `+0x04` | Block[count] | blocks | Contiguous, in the order of `itemenchantoffset.dbss`; the last block ends at the end of the file |

### Block (variable: 309 bytes + lists and strings)

Every field has the offset, type and name it has in the Block of
[`itemenchant.dbss`](itemenchant_dbss.md), and the meanings, value counts
and evidence are there. As there, the header fields after `unknown_61` move
by its count `unknown_5d`, and the hex in their `unknown_<hex>` names is the
offset in a block whose count is `0`.

| Offset               | Type                           | Field                       | Notes |
| -------------------- | ------------------------------ | --------------------------- | ----- |
| `+0x00`              | u32                            | key                         | Packed item ID and enchant level, `enchant_level << 24 \| item_id` |
| `+0x04`              | u8                             | item_type                   |       |
| `+0x05`              | u8                             | category                    |       |
| `+0x06`              | u8                             | grade                       |       |
| `+0x07`              | u8                             | equip_type                  |       |
| `+0x08`              | bytes[6]                       | unknown_08                  |       |
| `+0x0E`              | u8                             | equip_slot                  |       |
| `+0x0F`              | u8                             | unknown_0f                  |       |
| `+0x10`              | u8[46]                         | extended_slots              |       |
| `+0x3E`              | u8                             | item_material               |       |
| `+0x3F`              | i32                            | weight                      |       |
| `+0x43`              | u8                             | stackable                   |       |
| `+0x44`              | u8                             | do_apply_directly           |       |
| `+0x45`              | u32                            | expiration_minutes          |       |
| `+0x49`              | u8                             | vested_type                 |       |
| `+0x4A`              | u8                             | family_bound                |       |
| `+0x4B`              | u8                             | for_trade                   |       |
| `+0x4C`              | u8                             | trade_type                  |       |
| `+0x4D`              | u64                            | class_mask                  |       |
| `+0x55`              | u32                            | servant_kinds               |       |
| `+0x59`              | bytes[4]                       | unknown_59                  |       |
| `+0x5D`              | u32                            | unknown_5d                  | Count of `unknown_61`; `0` except on mount and ship gear |
| `+0x61`              | bytes[unknown_5d]              | unknown_61                  |       |
| `unknown_61+0x00`    | i32                            | required_level              |       |
| `unknown_61+0x04`    | i32                            | max_level                   |       |
| `unknown_61+0x08`    | u8                             | life_exp_type               |       |
| `unknown_61+0x09`    | i32                            | life_min_level              |       |
| `unknown_61+0x0D`    | i64                            | buy_price                   |       |
| `unknown_61+0x15`    | i64                            | sell_price                  |       |
| `unknown_61+0x1D`    | i64                            | repair_price                |       |
| `unknown_61+0x25`    | u16                            | contents_event_type         |       |
| `unknown_61+0x27`    | i64                            | contents_event_param1       |       |
| `unknown_61+0x2F`    | i64                            | contents_event_param2       |       |
| `unknown_61+0x37`    | bytes[8]                       | unknown_98                  |       |
| `unknown_61+0x3F`    | u8                             | commerce_type               |       |
| `unknown_61+0x40`    | u16                            | item_action_number          |       |
| `unknown_61+0x42`    | u8                             | hide_from_note              |       |
| `unknown_61+0x43`    | u8                             | is_cash                     |       |
| `unknown_61+0x44`    | u8                             | unknown_a5                  |       |
| `unknown_61+0x45`    | u8                             | is_term                     |       |
| `unknown_61+0x46`    | u8                             | guild_stock_level           |       |
| `unknown_61+0x47`    | u8                             | dyeable                     |       |
| `unknown_61+0x48`    | u8                             | is_target_alive             |       |
| `unknown_61+0x49`    | u16                            | character_id                |       |
| `unknown_61+0x4B`    | u8                             | repair_endurance_count      |       |
| `unknown_61+0x4C`    | u8                             | unknown_ad                  |       |
| `unknown_61+0x4D`    | bytes[22]                      | unknown_ae                  |       |
| `unknown_61+0x63`    | u8                             | personal_trade              |       |
| `unknown_61+0x64`    | u16                            | max_durability              |       |
| `unknown_61+0x66`    | u8                             | is_client_use               |       |
| `unknown_61+0x67`    | u8                             | market_category             |       |
| `unknown_61+0x68`    | u8                             | market_sub_category         |       |
| `unknown_61+0x69`    | u8                             | node_free_trade             |       |
| `unknown_61+0x6A`    | u8                             | unknown_cb                  |       |
| `unknown_61+0x6B`    | u32                            | skill_key_1                 |       |
| `unknown_61+0x6F`    | u32                            | skill_key_2                 |       |
| `unknown_61+0x73`    | u32                            | class_entry_count           |       |
| `unknown_61+0x77`    | Class Entry[class_entry_count] | class_entries               |       |
| `class_entries+0x00` | u32                            | unknown_list2_count         |       |
| `class_entries+0x04` | u8[unknown_list2_count][5]     | unknown_list2               |       |
| `unknown_list2+0x00` | bytes[4]                       | unknown_after_unknown_list2 |       |
| `unknown_list2+0x04` | u32                            | unknown_list3_count         |       |
| `unknown_list2+0x08` | u32[unknown_list3_count]       | unknown_list3               |       |
| `unknown_list3+0x00` | u32                            | enchant_key                 |       |
| `unknown_list3+0x04` | str16                          | name_kr                     | Korean item name |
| `name_kr+0x00`       | str8                           | icon                        | Icon path, relative to `ui_texture/icon/` |
| `icon+0x00`          | Icon Tail                      | icon_tail                   | See Icon Tail |
| `icon+0x12`          | str16[3]                       | messages_kr                 |       |
| `messages_kr+0x00`   | Message Tail                   | message_tail                | See Message Tail; the block ends with it |

### Class Entry (5 bytes)

| Offset  | Type | Field         | Notes |
| ------- | ---- | ------------- | ----- |
| `+0x00` | u8   | class_type    |       |
| `+0x01` | u32  | item_mesh_key | The key of [`itemeffectchange.dbss`](itemeffectchange_dbss.md) |

### Icon Tail (18 bytes)

| Offset  | Type      | Field            | Notes |
| ------- | --------- | ---------------- | ----- |
| `+0x00` | u8        | marketable       |       |
| `+0x01` | u8        | karma_type       |       |
| `+0x02` | bytes[11] | unknown_02       |       |
| `+0x0D` | u8        | family_inventory |       |
| `+0x0E` | u8        | unknown_0e       |       |
| `+0x0F` | u8        | season_item_type |       |
| `+0x10` | bytes[2]  | unknown_10       |       |

### Message Tail (43 bytes)

The first `0x2B` bytes of the `itemenchant.dbss` Message Tail, with the same
offsets and names; its `unknown_2b` and `item_access_level` are the first
fields of an `itemenchantbackend.dbss` block.

| Offset  | Type     | Field                  | Notes |
| ------- | -------- | ---------------------- | ----- |
| `+0x00` | i64      | unknown_limit          |       |
| `+0x08` | u8       | unknown_08             |       |
| `+0x09` | u32      | enhancement_group      |       |
| `+0x0D` | u32      | enhancement_type       |       |
| `+0x11` | u8       | is_removable           |       |
| `+0x12` | bytes[4] | unknown_12             |       |
| `+0x16` | u8       | cron_enchant_control   |       |
| `+0x17` | u8       | unknown_17             |       |
| `+0x18` | u8       | is_notice_world_market |       |
| `+0x19` | bytes[2] | unknown_19             |       |
| `+0x1B` | u8       | barter_type            |       |
| `+0x1C` | bytes[6] | unknown_1c             |       |
| `+0x22` | u8       | is_dropable            |       |
| `+0x23` | u8       | is_exchange_item       |       |
| `+0x24` | u8       | is_navigation          |       |
| `+0x25` | bytes[4] | unknown_25             |       |
| `+0x29` | u8       | life_equip_type        |       |
| `+0x2A` | u8       | life_restrict_type     |       |

## Layout 1

Older clients store `life_equip_type` with three more bytes after it, so
the Message Tail this file keeps is 46 bytes. On client 3426 no block has
`item_type` 20, and `life_equip_type` is `36` in all of them, where Layout 2
stores `37` on every item that is not Life Skill gear. On client 3426 each block here is
again the front of its `itemenchant.dbss` block, 3 bytes longer than on
client 3483, and the `itemenchantbackend.dbss` blocks are the same length.

### Message Tail (46 bytes)

| Offset  | Type     | Field                          | Notes |
| ------- | -------- | ------------------------------ | ----- |
| `+0x00` | i64      | unknown_limit                  |       |
| `+0x08` | u8       | unknown_08                     |       |
| `+0x09` | u32      | enhancement_group              |       |
| `+0x0D` | u32      | enhancement_type               |       |
| `+0x11` | u8       | is_removable                   |       |
| `+0x12` | bytes[4] | unknown_12                     |       |
| `+0x16` | u8       | cron_enchant_control           |       |
| `+0x17` | u8       | unknown_17                     |       |
| `+0x18` | u8       | is_notice_world_market         |       |
| `+0x19` | bytes[2] | unknown_19                     |       |
| `+0x1B` | u8       | barter_type                    |       |
| `+0x1C` | bytes[6] | unknown_1c                     |       |
| `+0x22` | u8       | is_dropable                    |       |
| `+0x23` | u8       | is_exchange_item               |       |
| `+0x24` | u8       | is_navigation                  |       |
| `+0x25` | bytes[4] | unknown_25                     |       |
| `+0x29` | u8       | life_equip_type                | `36` in every block of client 3426 |
| `+0x2A` | bytes[3] | unknown_after_life_equip_type  | `0` in every block of client 3426 |
| `+0x2D` | u8       | life_restrict_type             |       |

## Notes

- I checked the split on client 3483 by walking all three files: for all
  169,345 keys the first bytes of the `itemenchant.dbss` block equal the
  block of this file, the rest equals the `itemenchantbackend.dbss` block,
  and the blocks of this file tile it from byte `4` to the end. The parsed
  fields of the 70,826 base items match the `itemenchant.dbss` parse.
- The fields this file leaves out are the ones the `itemenchant.dbss` doc
  places after Message Tail `+0x2A`: `item_access_level`, `second_string`,
  `key_dup` and `crystal_group`, and the undecoded remainder between them.
- The file first appears on client 1980, two test clients after
  `itemenchantbackend.dbss` (1964). Versions gives the clients that fit
  Layout 1; on the ones that fit neither layout the block holds other
  differences, as `itemenchant.dbss` does before client 3387.

## Open Questions

### Which File the Client Reads

The client data holds the whole blocks in `itemenchant.dbss` and the same
bytes again, split, in this file and `itemenchantbackend.dbss`. Whether the
client loads the split pair, the whole file or both, and what the `test` in
this file's name stands for, is open.
