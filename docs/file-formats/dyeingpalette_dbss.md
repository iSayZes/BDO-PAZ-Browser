# `dyeingpalette.dbss` Format

## Purpose

The colours of every dye palette: one row per palette type, each a list of
colours with an environment and a specular value. A dye item in
[`itempalette.dbss`](itempalette_dbss.md) points at one colour by palette
type and index. Types `1` to `8` are the eight tabs of the dye window
(Basic Dye, then the seven town dyes from Olvian to Valencian Dye); type
`100` holds six lantern colours. Companion `dyeingpaletteoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records            | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ------ | ------------------ | --------- |
| 1      | 1346 and later | 3483    | `dyeingpalette.dbss`       | 14,026 | 1,161 Color, 9 Row | 12        |
| 1      | 1346 and later | 3483    | `dyeingpaletteoffset.dbss` | 85     | 9 Offset Row       | 9         |

| Layout | File                       | Known            | Unknown    |
| ------ | -------------------------- | ---------------- | ---------- |
| 1      | `dyeingpalette.dbss`       | 14,017 B (99.9%) | 9 B (0.1%) |
| 1      | `dyeingpaletteoffset.dbss` | 85 B (100.0%)    | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `608399cdd257`  |
| 3482   | Layout 1             | `608399cdd257`  |
| 3474   | Layout 1             | `608399cdd257`  |
| 3473   | Layout 1             | `608399cdd257`  |
| 3464   | Layout 1             | `608399cdd257`  |
| 3458   | Layout 1             | `608399cdd257`  |
| 3454   | Layout 1             | `608399cdd257`  |
| 3444   | Layout 1             | `608399cdd257`  |
| 3435   | Layout 1             | `608399cdd257`  |
| 3426   | Layout 1             | `608399cdd257`  |
| 3418   | Layout 1             | `608399cdd257`  |
| 3412   | Layout 1             | `608399cdd257`  |
| 3402   | Layout 1             | `608399cdd257`  |
| 3396   | Layout 1             | `608399cdd257`  |
| 3387   | Layout 1             | `608399cdd257`  |
| 3381   | Layout 1             | `608399cdd257`  |
| 3373   | Layout 1             | `608399cdd257`  |
| 3364   | Layout 1             | `608399cdd257`  |
| 3356   | Layout 1             | `608399cdd257`  |
| 3349   | Layout 1             | `608399cdd257`  |
| 3342   | Layout 1             | `608399cdd257`  |
| 3335   | Layout 1             | `608399cdd257`  |
| 3326   | Layout 1             | `608399cdd257`  |
| 3321   | Layout 1             | `608399cdd257`  |
| 3314   | Layout 1             | `608399cdd257`  |
| 3303   | Layout 1             | `608399cdd257`  |
| 3302   | Layout 1             | `608399cdd257`  |
| 3293   | Layout 1             | `608399cdd257`  |
| 3283   | Layout 1             | `608399cdd257`  |
| 3275   | Layout 1             | `608399cdd257`  |
| 3267   | Layout 1             | `608399cdd257`  |
| 3258   | Layout 1             | `608399cdd257`  |
| 3251   | Layout 1             | `608399cdd257`  |
| 3242   | Layout 1             | `608399cdd257`  |
| 3235   | Layout 1             | `608399cdd257`  |
| 3229   | Layout 1             | `608399cdd257`  |
| 3212   | Layout 1             | `608399cdd257`  |
| 3203   | Layout 1             | `608399cdd257`  |
| 3193   | Layout 1             | `608399cdd257`  |
| 3186   | Layout 1             | `608399cdd257`  |
| 3177   | Layout 1             | `608399cdd257`  |
| 3169   | Layout 1             | `608399cdd257`  |
| 3158   | Layout 1             | `608399cdd257`  |
| 3151   | Layout 1             | `608399cdd257`  |
| 3144   | Layout 1             | `608399cdd257`  |
| 3133   | Layout 1             | `608399cdd257`  |
| 3125   | Layout 1             | `608399cdd257`  |
| 3118   | Layout 1             | `608399cdd257`  |
| 3111   | Layout 1             | `608399cdd257`  |
| 3103   | Layout 1             | `608399cdd257`  |
| 3095   | Layout 1             | `608399cdd257`  |
| 3086   | Layout 1             | `608399cdd257`  |
| 3072   | Layout 1             | `608399cdd257`  |
| 3062   | Layout 1             | `608399cdd257`  |
| 3052   | Layout 1             | `608399cdd257`  |
| 3045   | Layout 1             | `608399cdd257`  |
| 3037   | Layout 1             | `608399cdd257`  |
| 3030   | Layout 1             | `608399cdd257`  |
| 3021   | Layout 1             | `608399cdd257`  |
| 3012   | Layout 1             | `608399cdd257`  |
| 3002   | Layout 1             | `608399cdd257`  |
| 2995   | Layout 1             | `608399cdd257`  |
| 2987   | Layout 1             | `608399cdd257`  |
| 2978   | Layout 1             | `608399cdd257`  |
| 2970   | Layout 1             | `608399cdd257`  |
| 2959   | Layout 1             | `608399cdd257`  |
| 2951   | Layout 1             | `608399cdd257`  |
| 2942   | Layout 1             | `608399cdd257`  |
| 2935   | Layout 1             | `608399cdd257`  |
| 2932   | Layout 1             | `608399cdd257`  |
| 2923   | Layout 1             | `608399cdd257`  |
| 2919   | Layout 1             | `608399cdd257`  |
| 2907   | Layout 1             | `608399cdd257`  |
| 2900   | Layout 1             | `608399cdd257`  |
| 2891   | Layout 1             | `608399cdd257`  |
| 2882   | Layout 1             | `608399cdd257`  |
| 2872   | Layout 1             | `608399cdd257`  |
| 2863   | Layout 1             | `608399cdd257`  |
| 2855   | Layout 1             | `608399cdd257`  |
| 2849   | Layout 1             | `608399cdd257`  |
| 2844   | Layout 1             | `608399cdd257`  |
| 2834   | Layout 1             | `608399cdd257`  |
| 2825   | Layout 1             | `608399cdd257`  |
| 2819   | Layout 1             | `608399cdd257`  |
| 2811   | Layout 1             | `608399cdd257`  |
| 2803   | Layout 1             | `608399cdd257`  |
| 2794   | Layout 1             | `608399cdd257`  |
| 2783   | Layout 1             | `608399cdd257`  |
| 2774   | Layout 1             | `608399cdd257`  |
| 2765   | Layout 1             | `608399cdd257`  |
| 2756   | Layout 1             | `608399cdd257`  |
| 2750   | Layout 1             | `608399cdd257`  |
| 2743   | Layout 1             | `608399cdd257`  |
| 2736   | Layout 1             | `608399cdd257`  |
| 2726   | Layout 1             | `608399cdd257`  |
| 2717   | Layout 1             | `608399cdd257`  |
| 2709   | Layout 1             | `608399cdd257`  |
| 2703   | Layout 1             | `608399cdd257`  |
| 2695   | Layout 1             | `608399cdd257`  |
| 2684   | Layout 1             | `608399cdd257`  |
| 2672   | Layout 1             | `608399cdd257`  |
| 2665   | Layout 1             | `608399cdd257`  |
| 2657   | Layout 1             | `608399cdd257`  |
| 2649   | Layout 1             | `608399cdd257`  |
| 2644   | Layout 1             | `608399cdd257`  |
| 2637   | Layout 1             | `608399cdd257`  |
| 2629   | Layout 1             | `608399cdd257`  |
| 2619   | Layout 1             | `608399cdd257`  |
| 2612   | Layout 1             | `608399cdd257`  |
| 2606   | Layout 1             | `608399cdd257`  |
| 2602   | Layout 1             | `608399cdd257`  |
| 2601   | Layout 1             | `608399cdd257`  |
| 2592   | Layout 1             | `608399cdd257`  |
| 2583   | Layout 1             | `608399cdd257`  |
| 2575   | Layout 1             | `608399cdd257`  |
| 2567   | Layout 1             | `608399cdd257`  |
| 2560   | Layout 1             | `608399cdd257`  |
| 2553   | Layout 1             | `608399cdd257`  |
| 2545   | Layout 1             | `608399cdd257`  |
| 2538   | Layout 1             | `608399cdd257`  |
| 2529   | Layout 1             | `608399cdd257`  |
| 2519   | Layout 1             | `608399cdd257`  |
| 2513   | Layout 1             | `608399cdd257`  |
| 2510   | Layout 1             | `608399cdd257`  |
| 2507   | Layout 1             | `608399cdd257`  |
| 2503   | Layout 1             | `608399cdd257`  |
| 2498   | Layout 1             | `608399cdd257`  |
| 2492   | Layout 1             | `608399cdd257`  |
| 2487   | Layout 1             | `608399cdd257`  |
| 2480   | Layout 1             | `608399cdd257`  |
| 2474   | Layout 1             | `608399cdd257`  |
| 2468   | Layout 1             | `608399cdd257`  |
| 2460   | Layout 1             | `608399cdd257`  |
| 2453   | Layout 1             | `608399cdd257`  |
| 2444   | Layout 1             | `608399cdd257`  |
| 2438   | Layout 1             | `608399cdd257`  |
| 2434   | Layout 1             | `608399cdd257`  |
| 2429   | Layout 1             | `608399cdd257`  |
| 2421   | Layout 1             | `608399cdd257`  |
| 2414   | Layout 1             | `608399cdd257`  |
| 2407   | Layout 1             | `608399cdd257`  |
| 2401   | Layout 1             | `608399cdd257`  |
| 2397   | Layout 1             | `608399cdd257`  |
| 2393   | Layout 1             | `608399cdd257`  |
| 2384   | Layout 1             | `608399cdd257`  |
| 2378   | Layout 1             | `608399cdd257`  |
| 2372   | Layout 1             | `608399cdd257`  |
| 2358   | Layout 1             | `608399cdd257`  |
| 2352   | Layout 1             | `608399cdd257`  |
| 2347   | Layout 1             | `608399cdd257`  |
| 2343   | Layout 1             | `608399cdd257`  |
| 2335   | Layout 1             | `608399cdd257`  |
| 2327   | Layout 1             | `608399cdd257`  |
| 2324   | Layout 1             | `608399cdd257`  |
| 2319   | Layout 1             | `608399cdd257`  |
| 2313   | Layout 1             | `608399cdd257`  |
| 2308   | Layout 1             | `608399cdd257`  |
| 2302   | Layout 1             | `608399cdd257`  |
| 2295   | Layout 1             | `608399cdd257`  |
| 2290   | Layout 1             | `608399cdd257`  |
| 2284   | Layout 1             | `608399cdd257`  |
| 2276   | Layout 1             | `608399cdd257`  |
| 2269   | Layout 1             | `608399cdd257`  |
| 2259   | Layout 1             | `608399cdd257`  |
| 2250   | Layout 1             | `608399cdd257`  |
| 2243   | Layout 1             | `608399cdd257`  |
| 2235   | Layout 1             | `608399cdd257`  |
| 2229   | Layout 1             | `608399cdd257`  |
| 2224   | Layout 1             | `608399cdd257`  |
| 2218   | Layout 1             | `608399cdd257`  |
| 2215   | Layout 1             | `608399cdd257`  |
| 2207   | Layout 1             | `608399cdd257`  |
| 2203   | Layout 1             | `608399cdd257`  |
| 2196   | Layout 1             | `608399cdd257`  |
| 2192   | Layout 1             | `608399cdd257`  |
| 2189   | Layout 1             | `608399cdd257`  |
| 2183   | Layout 1             | `608399cdd257`  |
| 2179   | Layout 1             | `608399cdd257`  |
| 2171   | Layout 1             | `608399cdd257`  |
| 2163   | Layout 1             | `608399cdd257`  |
| 2156   | Layout 1             | `608399cdd257`  |
| 2151   | Layout 1             | `608399cdd257`  |
| 2147   | Layout 1             | `608399cdd257`  |
| 2142   | Layout 1             | `608399cdd257`  |
| 2138   | Layout 1             | `608399cdd257`  |
| 2134   | Layout 1             | `608399cdd257`  |
| 2130   | Layout 1             | `608399cdd257`  |
| 2122   | Layout 1             | `608399cdd257`  |
| 2107   | Layout 1             | `608399cdd257`  |
| 2098   | Layout 1             | `608399cdd257`  |
| 2089   | Layout 1             | `608399cdd257`  |
| 2081   | Layout 1             | `608399cdd257`  |
| 2073   | Layout 1             | `608399cdd257`  |
| 2067   | Layout 1             | `608399cdd257`  |
| 2063   | Layout 1             | `608399cdd257`  |
| 2059   | Layout 1             | `608399cdd257`  |
| 2052   | Layout 1             | `608399cdd257`  |
| 2044   | Layout 1             | `608399cdd257`  |
| 2039   | Layout 1             | `608399cdd257`  |
| 2032   | Layout 1             | `608399cdd257`  |
| 2025   | Layout 1             | `608399cdd257`  |
| 2011   | Layout 1             | `608399cdd257`  |
| 2005   | Layout 1             | `608399cdd257`  |
| 2000   | Layout 1             | `608399cdd257`  |
| 1996   | Layout 1             | `608399cdd257`  |
| 1991   | Layout 1             | `608399cdd257`  |
| 1985   | Layout 1             | `608399cdd257`  |
| 1980   | Layout 1             | `608399cdd257`  |
| 1969   | Layout 1             | `608399cdd257`  |
| 1964   | Layout 1             | `608399cdd257`  |
| 1958   | Layout 1             | `608399cdd257`  |
| 1950   | Layout 1             | `608399cdd257`  |
| 1945   | Layout 1             | `608399cdd257`  |
| 1937   | Layout 1             | `608399cdd257`  |
| 1933   | Layout 1             | `608399cdd257`  |
| 1927   | Layout 1             | `608399cdd257`  |
| 1921   | Layout 1             | `608399cdd257`  |
| 1914   | Layout 1             | `608399cdd257`  |
| 1908   | Layout 1             | `608399cdd257`  |
| 1897   | Layout 1             | `608399cdd257`  |
| 1892   | Layout 1             | `608399cdd257`  |
| 1886   | Layout 1             | `608399cdd257`  |
| 1881   | Layout 1             | `608399cdd257`  |
| 1871   | Layout 1             | `608399cdd257`  |
| 1866   | Layout 1             | `608399cdd257`  |
| 1862   | Layout 1             | `608399cdd257`  |
| 1854   | Layout 1             | `608399cdd257`  |
| 1846   | Layout 1             | `608399cdd257`  |
| 1838   | Layout 1             | `608399cdd257`  |
| 1832   | Layout 1             | `608399cdd257`  |
| 1826   | Layout 1             | `608399cdd257`  |
| 1822   | Layout 1             | `608399cdd257`  |
| 1818   | Layout 1             | `608399cdd257`  |
| 1804   | Layout 1             | `608399cdd257`  |
| 1794   | Layout 1             | `608399cdd257`  |
| 1790   | Layout 1             | `608399cdd257`  |
| 1784   | Layout 1             | `608399cdd257`  |
| 1774   | Layout 1             | `608399cdd257`  |
| 1771   | Layout 1             | `608399cdd257`  |
| 1762   | Layout 1             | `608399cdd257`  |
| 1759   | Layout 1             | `608399cdd257`  |
| 1754   | Layout 1             | `608399cdd257`  |
| 1749   | Layout 1             | `608399cdd257`  |
| 1743   | Layout 1             | `608399cdd257`  |
| 1737   | Layout 1             | `608399cdd257`  |
| 1731   | Layout 1             | `608399cdd257`  |
| 1725   | Layout 1             | `608399cdd257`  |
| 1717   | Layout 1             | `608399cdd257`  |
| 1710   | Layout 1             | `608399cdd257`  |
| 1704   | Layout 1             | `608399cdd257`  |
| 1698   | Layout 1             | `608399cdd257`  |
| 1690   | Layout 1             | `608399cdd257`  |
| 1685   | Layout 1             | `608399cdd257`  |
| 1680   | Layout 1             | `608399cdd257`  |
| 1674   | Layout 1             | `608399cdd257`  |
| 1668   | Layout 1             | `608399cdd257`  |
| 1659   | Layout 1             | `608399cdd257`  |
| 1649   | Layout 1             | `608399cdd257`  |
| 1642   | Layout 1             | `608399cdd257`  |
| 1636   | Layout 1             | `608399cdd257`  |
| 1628   | Layout 1             | `608399cdd257`  |
| 1622   | Layout 1             | `608399cdd257`  |
| 1614   | Layout 1             | `608399cdd257`  |
| 1608   | Layout 1             | `608399cdd257`  |
| 1602   | Layout 1             | `608399cdd257`  |
| 1598   | Layout 1             | `608399cdd257`  |
| 1594   | Layout 1             | `608399cdd257`  |
| 1590   | Layout 1             | `608399cdd257`  |
| 1587   | Layout 1             | `608399cdd257`  |
| 1584   | Layout 1             | `608399cdd257`  |
| 1579   | Layout 1             | `608399cdd257`  |
| 1572   | Layout 1             | `608399cdd257`  |
| 1565   | Layout 1             | `608399cdd257`  |
| 1559   | Layout 1             | `608399cdd257`  |
| 1554   | Layout 1             | `608399cdd257`  |
| 1547   | Layout 1             | `608399cdd257`  |
| 1537   | Layout 1             | `608399cdd257`  |
| 1529   | Layout 1             | `608399cdd257`  |
| 1524   | Layout 1             | `608399cdd257`  |
| 1519   | Layout 1             | `608399cdd257`  |
| 1509   | Layout 1             | `608399cdd257`  |
| 1506   | Layout 1             | `608399cdd257`  |
| 1504   | Layout 1             | `608399cdd257`  |
| 1500   | Layout 1             | `608399cdd257`  |
| 1493   | Layout 1             | `608399cdd257`  |
| 1489   | Layout 1             | `608399cdd257`  |
| 1485   | Layout 1             | `608399cdd257`  |
| 1481   | Layout 1             | `608399cdd257`  |
| 1474   | Layout 1             | `608399cdd257`  |
| 1466   | Layout 1             | `608399cdd257`  |
| 1462   | Layout 1             | `608399cdd257`  |
| 1459   | Layout 1             | `608399cdd257`  |
| 1453   | Layout 1             | `608399cdd257`  |
| 1450   | Layout 1             | `608399cdd257`  |
| 1445   | Layout 1             | `608399cdd257`  |
| 1439   | Layout 1             | `608399cdd257`  |
| 1433   | Layout 1             | `608399cdd257`  |
| 1430   | Layout 1             | `608399cdd257`  |
| 1426   | Layout 1             | `608399cdd257`  |
| 1421   | Layout 1             | `608399cdd257`  |
| 1417   | Layout 1             | `608399cdd257`  |
| 1416   | Layout 1             | `608399cdd257`  |
| 1409   | Layout 1             | `608399cdd257`  |
| 1405   | Layout 1             | `608399cdd257`  |
| 1401   | Layout 1             | `608399cdd257`  |
| 1396   | Layout 1             | `608399cdd257`  |
| 1391   | Layout 1             | `608399cdd257`  |
| 1390   | Layout 1             | `608399cdd257`  |
| 1386   | Layout 1             | `608399cdd257`  |
| 1381   | Layout 1             | `608399cdd257`  |
| 1379   | Layout 1             | `608399cdd257`  |
| 1372   | Layout 1             | `608399cdd257`  |
| 1366   | Layout 1             | `608399cdd257`  |
| 1364   | Layout 1             | `608399cdd257`  |
| 1363   | Layout 1             | `608399cdd257`  |
| 1360   | Layout 1             | `608399cdd257`  |
| 1358   | Layout 1             | `608399cdd257`  |
| 1355   | Layout 1             | `608399cdd257`  |
| 1351   | Layout 1             | `608399cdd257`  |
| 1348   | Layout 1             | `608399cdd257`  |
| 1346   | Layout 1             | `608399cdd257`  |
| 1341   | No documented layout | `608399cdd257`  |
| 1340   | No documented layout | `608399cdd257`  |
| 1338   | No documented layout | `608399cdd257`  |
| 1335   | No documented layout | `608399cdd257`  |
| 1333   | No documented layout | `608399cdd257`  |
| 1329   | No documented layout | `608399cdd257`  |
| 1327   | No documented layout | `608399cdd257`  |
| 1324   | No documented layout | `608399cdd257`  |
| 1321   | No documented layout | `608399cdd257`  |
| 1319   | No documented layout | `608399cdd257`  |
| 1318   | No documented layout | `608399cdd257`  |
| 1316   | No documented layout | `608399cdd257`  |
| 1313   | No documented layout | `608399cdd257`  |
| 1311   | No documented layout | `608399cdd257`  |
| 1309   | No documented layout | `608399cdd257`  |
| 1304   | No documented layout | `608399cdd257`  |
| 1292   | No documented layout | `608399cdd257`  |
| 1286   | No documented layout | `608399cdd257`  |
| 1280   | No documented layout | `608399cdd257`  |
| 1276   | No documented layout | `608399cdd257`  |
| 1267   | No file              | `608399cdd257`  |
| 1261   | No file              | `608399cdd257`  |
| 1256   | No file              | `608399cdd257`  |
| 1250   | No file              | `608399cdd257`  |
| 1246   | No file              | `608399cdd257`  |
| 1239   | No file              | `608399cdd257`  |
| 1230   | No file              | `608399cdd257`  |
| 1226   | No file              | `608399cdd257`  |
| 1220   | No file              | `608399cdd257`  |
| 1217   | No file              | `608399cdd257`  |
| 1211   | No file              | `608399cdd257`  |
| 1210   | No file              | `608399cdd257`  |
| 1208   | No file              | `608399cdd257`  |
| 1203   | No file              | `608399cdd257`  |
| 1197   | No file              | `608399cdd257`  |
| 1194   | No file              | `608399cdd257`  |
| 1192   | No file              | `608399cdd257`  |
| 1187   | No file              | `608399cdd257`  |
| 1183   | No file              | `608399cdd257`  |
| 1177   | No file              | `608399cdd257`  |
| 1173   | No file              | `608399cdd257`  |
| 1167   | No file              | `608399cdd257`  |
| 1164   | No file              | `608399cdd257`  |
| 1156   | No file              | `608399cdd257`  |
| 1149   | No file              | `608399cdd257`  |
| 1144   | No file              | `608399cdd257`  |
| 1137   | No file              | `608399cdd257`  |
| 1132   | No file              | `608399cdd257`  |
| 1127   | No file              | `608399cdd257`  |
| 1122   | No file              | `608399cdd257`  |
| 1118   | No file              | `608399cdd257`  |
| 1114   | No file              | `608399cdd257`  |
| 1109   | No file              | `608399cdd257`  |
| 1102   | No file              | `608399cdd257`  |
| 1096   | No file              | `608399cdd257`  |
| 1088   | No file              | `608399cdd257`  |
| 1081   | No file              | `608399cdd257`  |
| 1076   | No file              | `608399cdd257`  |
| 1069   | No file              | `608399cdd257`  |
| 1064   | No file              | `608399cdd257`  |
| 1058   | No file              | `608399cdd257`  |
| 1051   | No file              | `608399cdd257`  |
| 1044   | No file              | `608399cdd257`  |
| 1036   | No file              | `608399cdd257`  |
| 1026   | No file              | `608399cdd257`  |
| 1016   | No file              | `608399cdd257`  |
| 1009   | No file              | `608399cdd257`  |
| 1005   | No file              | `608399cdd257`  |
| 1000   | No file              | `608399cdd257`  |
| 998    | No file              | `608399cdd257`  |
| 990    | No file              | `608399cdd257`  |
| 979    | No file              | `608399cdd257`  |
| 972    | No file              | `608399cdd257`  |
| 963    | No file              | `608399cdd257`  |
| 955    | No file              | `608399cdd257`  |
| 946    | No file              | `608399cdd257`  |
| 938    | No file              | `608399cdd257`  |
| 927    | No file              | `608399cdd257`  |
| 911    | No file              | `608399cdd257`  |
| 904    | No file              | `608399cdd257`  |
| 899    | No file              | `608399cdd257`  |
| 894    | No file              | `608399cdd257`  |
| 885    | No file              | `608399cdd257`  |
| 879    | No file              | `608399cdd257`  |
| 872    | No file              | `608399cdd257`  |
| 864    | No file              | `608399cdd257`  |
| 855    | No file              | `608399cdd257`  |
| 853    | No file              | `608399cdd257`  |
| 845    | No file              | `608399cdd257`  |
| 837    | No file              | `608399cdd257`  |
| 829    | No file              | `608399cdd257`  |
| 822    | No file              | `608399cdd257`  |
| 814    | No file              | `608399cdd257`  |
| 805    | No file              | `608399cdd257`  |
| 794    | No file              | `608399cdd257`  |
| 787    | No file              | `608399cdd257`  |
| 780    | No file              | `608399cdd257`  |
| 771    | No file              | `608399cdd257`  |
| 760    | No file              | `608399cdd257`  |
| 748    | No file              | `608399cdd257`  |
| 741    | No file              | `608399cdd257`  |
| 736    | No file              | `608399cdd257`  |
| 731    | No file              | `608399cdd257`  |
| 723    | No file              | `608399cdd257`  |
| 711    | No file              | `608399cdd257`  |
| 707    | No file              | `608399cdd257`  |
| 697    | No file              | `608399cdd257`  |
| 689    | No file              | `608399cdd257`  |
| 683    | No file              | `608399cdd257`  |
| 678    | No file              | `608399cdd257`  |
| 670    | No file              | `608399cdd257`  |
| 661    | No file              | `608399cdd257`  |
| 656    | No file              | `608399cdd257`  |
| 652    | No file              | `608399cdd257`  |
| 643    | No file              | `608399cdd257`  |
| 637    | No file              | `608399cdd257`  |
| 630    | No file              | `608399cdd257`  |
| 627    | No file              | `608399cdd257`  |
| 621    | No file              | `608399cdd257`  |
| 617    | No file              | `608399cdd257`  |
| 615    | No file              | `608399cdd257`  |
| 606    | No file              | `608399cdd257`  |
| 599    | No file              | `608399cdd257`  |
| 592    | No file              | `608399cdd257`  |
| 586    | No file              | `608399cdd257`  |
| 577    | No file              | `608399cdd257`  |
| 569    | No file              | `608399cdd257`  |
| 561    | No file              | `608399cdd257`  |
| 554    | No file              | `608399cdd257`  |
| 542    | No file              | `608399cdd257`  |
| 532    | No file              | `608399cdd257`  |
| 531    | No file              | `608399cdd257`  |
| 526    | No file              | `608399cdd257`  |
| 521    | No file              | `608399cdd257`  |
| 517    | No file              | `608399cdd257`  |
| 510    | No file              | `608399cdd257`  |
| 508    | No file              | `608399cdd257`  |
| 504    | No file              | `608399cdd257`  |
| 497    | No file              | `608399cdd257`  |
| 491    | No file              | `608399cdd257`  |
| 485    | No file              | `608399cdd257`  |
| 478    | No file              | `608399cdd257`  |
| 472    | No file              | `608399cdd257`  |
| 466    | No file              | `608399cdd257`  |
| 457    | No file              | `608399cdd257`  |
| 452    | No file              | `608399cdd257`  |
| 449    | No file              | `608399cdd257`  |
| 435    | No file              | `608399cdd257`  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                                          |
| -------------------------- | -------- | ----------------------------------------------------------------------------- |
| `dyeingpaletteoffset.dbss` | Optional | `palette_type -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `itempalette.dbss`         | Optional | The dye items of each colour, for the Dye Items column                         |
| `languagedata_en.loc`      | Optional | Item names (type `0`) and the dye window's tab names (type `37`)               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `9` on client 3474      |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 10 bytes + colors)

| Offset  | Type               | Field        | Notes                                                                 |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u8                 | palette_type | Row key, the `palette_type` of `itempalette.dbss`                      |
| `+0x01` | u8                 | unknown_01   | `0` on every row (clients 1784 and 3474); the offset index points here |
| `+0x02` | u64                | color_count  | Number of colours                                                      |
| `+0x0A` | Color[color_count] | colors       | See Color; a colour's position is its `palette_index`                  |

### Color (12 bytes)

The 2016 `gc::DyeingPaletteValue`: a `pa::Color` (blue, green, red, alpha)
and two floats.

| Offset  | Type | Field       | Notes                                                               |
| ------- | ---- | ----------- | ------------------------------------------------------------------- |
| `+0x00` | u8   | color_b     | Blue                                                                |
| `+0x01` | u8   | color_g     | Green                                                               |
| `+0x02` | u8   | color_r     | Red                                                                 |
| `+0x03` | u8   | color_a     | Alpha of the `pa::Color`; `0` on every colour (clients 1784 and 3474) |
| `+0x04` | f32  | environment | One value per palette type, see Palette Types                       |
| `+0x08` | f32  | specular    | One value per palette type, see Palette Types                       |

### `dyeingpaletteoffset.dbss`

Bare offset table into `dyeingpalette.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `dyeingpalette.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                        |

### Offset Row (9 bytes)

| Offset  | Type | Field        | Notes                                                       |
| ------- | ---- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u8   | palette_type | Key of the row it points at                                  |
| `+0x01` | u32  | data_offset  | Row start + 1, at `unknown_01`                               |
| `+0x05` | u32  | data_size    | The row size - 1: `9 + 12 x color_count`                     |

Read by `parse_bare_u8_offset_rows()` in `_common/pabr_offset.py`. The
index lists type `100` between types `3` and `4`; the main file stores the
rows by type. On clients 1784 and 3474 every index row points at the row
with its key.

## Palette Types

On client 3474 (the same on client 1784):

| Type | Dye window tab (LOC English) | Colours | Environment | Specular |
| ---- | ---------------------------- | ------- | ----------- | -------- |
| 1    | Basic Dye                    | 224     | `-1`        | `-1`     |
| 2    | Olvian Dye                   | 133     | `0`         | `0.02`   |
| 3    | Velian Dye                   | 133     | `0`         | `0.8`    |
| 4    | Heidelian Dye                | 133     | `0.63`      | `0.02`   |
| 5    | Keplanian Dye                | 133     | `0.94`      | `0.39`   |
| 6    | Calpheonian Dye              | 133     | `0.51`      | `0.63`   |
| 7    | Mediahn Dye                  | 133     | `0.57`      | `0.91`   |
| 8    | Valencian Dye                | 133     | `0.94`      | `0.97`   |
| 100  | none                         | 6       | `0`         | `0`      |

The tab names are `LUA_PALETTE_TAB_MATERIAL_0` to `_7` of the dye window
(`panel_window_dyeingpalette_renew.luac`), and the dye items of type N are
the dyes of tab N - 1 (see [`itempalette.dbss`](itempalette_dbss.md)). The
tab descriptions (`LUA_PALETTE_TAB_MATERIAL_DESC_0` to `_7`) name a
material per tab: any material for Basic Dye, then cloth, glossy cloth,
silk, leather, glossy leather, metal and shiny metal.

## Field Names

The `DyeingPalette_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Type`, `Env`, `Specular`, `ColorR`, `ColorG`
and `ColorB`, one sheet row per colour in file order. Its 1,161 rows match
all 1,161 colours of the file on all six columns, on client 1784 and on
client 3474: `Type` is `palette_type`, the colour's position among the rows
of its type is `palette_index`. The 2016 client's debug symbols name the
colour `gc::DyeingPaletteValue` (`_color`, `_environment`, `_specular`, the
`pa::Color` with the members `b`, `g`, `r`, `a`) and the row
`gc::DyeingPaletteStaticStauts` (sic) with `_dyeingPaletteValueList` and a
u8 `_type`, held in a map by u8 type. The developer workbook
(`datasheet_itemdatatable_cash.xlsm`) adds the note columns `#참조 -Index`
(the palette index), `#참조 -RGB색상표` (the colour as `#867e7e`) and
`#참조-색상명` with the colour's name: `염색약 - 탁한 빨강 #1` ("dye - dull
red #1") in type 1, `Type1 스노우 레드` ("Type1 snow red") in type 2, and
`노란색 랜턴` ("yellow lantern") to `아타니스 반딧불` ("Atanis firefly")
in type 100.

## Notes

- The colour is stored as blue, green, red, alpha, the byte order of
  `pa::Color`; the sheet has no alpha column.

## Open Questions

### What `unknown_01` Holds

The byte after the palette type is `0` in all 9 rows of clients 1784 and
3474, and the offset index points at it, so the index sees it as the
first byte of the record. The 2016 struct has a u8 `_type` after the
colour list, which the file does not store there; whether this byte is a
second type byte, a flag, or the high byte of a u16 key is not in the
client data.

### What Reads Palette Type 100

Type `100` holds six lantern colours (the workbook notes name them) and
no `itempalette.dbss` row points at it. The dye window's Lua
(`panel_window_dyeingpalette_renew.luac`) has tabs for types 1 to 8 only;
which feature offers the lantern colours is not in the client data
checked so far.
