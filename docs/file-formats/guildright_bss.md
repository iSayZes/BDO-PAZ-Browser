# `guildright.bss` Format

## Purpose

Which guild member grades hold each guild right: one row per right index
with one flag per member grade. On client 3474 the file has 55 rows,
indexes `0` to `54`, and 11 flags per row. The client Lua checks a right
with `ToClient_IsCheckGuildRightType(eRightType)` for the
`__eGuildRightType_*` rights once `_ContentsGroup_GuildRightInfo` is on.
[guildspecialskillright](guildspecialskillright_bss.md) holds the same
flags per guild skill, and
[guildrightnewstaticstatus](guildrightnewstaticstatus_bss.md) the
newer rights of the guild authority window.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------- | --------- |
| 1      | 1421 and later | 3483    | `guildright.bss` | 900   | 55 Row  | 16        |

| Layout | File             | Known          | Unknown    |
| ------ | ---------------- | -------------- | ---------- |
| 1      | `guildright.bss` | 900 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `8b5219491974`  |
| 3482   | Layout 1 | `8b5219491974`  |
| 3474   | Layout 1 | `8b5219491974`  |
| 3473   | Layout 1 | `8b5219491974`  |
| 3464   | Layout 1 | `8b5219491974`  |
| 3458   | Layout 1 | `8b5219491974`  |
| 3454   | Layout 1 | `8b5219491974`  |
| 3444   | Layout 1 | `8b5219491974`  |
| 3435   | Layout 1 | `8b5219491974`  |
| 3426   | Layout 1 | `8b5219491974`  |
| 3418   | Layout 1 | `8b5219491974`  |
| 3412   | Layout 1 | `8b5219491974`  |
| 3402   | Layout 1 | `8b5219491974`  |
| 3396   | Layout 1 | `8b5219491974`  |
| 3387   | Layout 1 | `8b5219491974`  |
| 3381   | Layout 1 | `8b5219491974`  |
| 3373   | Layout 1 | `8b5219491974`  |
| 3364   | Layout 1 | `8b5219491974`  |
| 3356   | Layout 1 | `8b5219491974`  |
| 3349   | Layout 1 | `8b5219491974`  |
| 3342   | Layout 1 | `8b5219491974`  |
| 3335   | Layout 1 | `8b5219491974`  |
| 3326   | Layout 1 | `8b5219491974`  |
| 3321   | Layout 1 | `8b5219491974`  |
| 3314   | Layout 1 | `8b5219491974`  |
| 3303   | Layout 1 | `8b5219491974`  |
| 3302   | Layout 1 | `8b5219491974`  |
| 3293   | Layout 1 | `8b5219491974`  |
| 3283   | Layout 1 | `8b5219491974`  |
| 3275   | Layout 1 | `8b5219491974`  |
| 3267   | Layout 1 | `8b5219491974`  |
| 3258   | Layout 1 | `8b5219491974`  |
| 3251   | Layout 1 | `8b5219491974`  |
| 3242   | Layout 1 | `8b5219491974`  |
| 3235   | Layout 1 | `8b5219491974`  |
| 3229   | Layout 1 | `8b5219491974`  |
| 3212   | Layout 1 | `8b5219491974`  |
| 3203   | Layout 1 | `8b5219491974`  |
| 3193   | Layout 1 | `8b5219491974`  |
| 3186   | Layout 1 | `8b5219491974`  |
| 3177   | Layout 1 | `8b5219491974`  |
| 3169   | Layout 1 | `8b5219491974`  |
| 3158   | Layout 1 | `8b5219491974`  |
| 3151   | Layout 1 | `8b5219491974`  |
| 3144   | Layout 1 | `8b5219491974`  |
| 3133   | Layout 1 | `8b5219491974`  |
| 3125   | Layout 1 | `8b5219491974`  |
| 3118   | Layout 1 | `8b5219491974`  |
| 3111   | Layout 1 | `8b5219491974`  |
| 3103   | Layout 1 | `8b5219491974`  |
| 3095   | Layout 1 | `8b5219491974`  |
| 3086   | Layout 1 | `8b5219491974`  |
| 3072   | Layout 1 | `8b5219491974`  |
| 3062   | Layout 1 | `8b5219491974`  |
| 3052   | Layout 1 | `8b5219491974`  |
| 3045   | Layout 1 | `8b5219491974`  |
| 3037   | Layout 1 | `8b5219491974`  |
| 3030   | Layout 1 | `8b5219491974`  |
| 3021   | Layout 1 | `8b5219491974`  |
| 3012   | Layout 1 | `8b5219491974`  |
| 3002   | Layout 1 | `8b5219491974`  |
| 2995   | Layout 1 | `8b5219491974`  |
| 2987   | Layout 1 | `8b5219491974`  |
| 2978   | Layout 1 | `8b5219491974`  |
| 2970   | Layout 1 | `8b5219491974`  |
| 2959   | Layout 1 | `8b5219491974`  |
| 2951   | Layout 1 | `8b5219491974`  |
| 2942   | Layout 1 | `8b5219491974`  |
| 2935   | Layout 1 | `8b5219491974`  |
| 2932   | Layout 1 | `8b5219491974`  |
| 2923   | Layout 1 | `8b5219491974`  |
| 2919   | Layout 1 | `8b5219491974`  |
| 2907   | Layout 1 | `8b5219491974`  |
| 2900   | Layout 1 | `8b5219491974`  |
| 2891   | Layout 1 | `8b5219491974`  |
| 2882   | Layout 1 | `8b5219491974`  |
| 2872   | Layout 1 | `8b5219491974`  |
| 2863   | Layout 1 | `8b5219491974`  |
| 2855   | Layout 1 | `8b5219491974`  |
| 2849   | Layout 1 | `8b5219491974`  |
| 2844   | Layout 1 | `8b5219491974`  |
| 2834   | Layout 1 | `8b5219491974`  |
| 2825   | Layout 1 | `8b5219491974`  |
| 2819   | Layout 1 | `8b5219491974`  |
| 2811   | Layout 1 | `8b5219491974`  |
| 2803   | Layout 1 | `8b5219491974`  |
| 2794   | Layout 1 | `8b5219491974`  |
| 2783   | Layout 1 | `8b5219491974`  |
| 2774   | Layout 1 | `8b5219491974`  |
| 2765   | Layout 1 | `8b5219491974`  |
| 2756   | Layout 1 | `8b5219491974`  |
| 2750   | Layout 1 | `8b5219491974`  |
| 2743   | Layout 1 | `8b5219491974`  |
| 2736   | Layout 1 | `8b5219491974`  |
| 2726   | Layout 1 | `8b5219491974`  |
| 2717   | Layout 1 | `8b5219491974`  |
| 2709   | Layout 1 | `8b5219491974`  |
| 2703   | Layout 1 | `8b5219491974`  |
| 2695   | Layout 1 | `8b5219491974`  |
| 2684   | Layout 1 | `8b5219491974`  |
| 2672   | Layout 1 | `8b5219491974`  |
| 2665   | Layout 1 | `8b5219491974`  |
| 2657   | Layout 1 | `8b5219491974`  |
| 2649   | Layout 1 | `8b5219491974`  |
| 2644   | Layout 1 | `8b5219491974`  |
| 2637   | Layout 1 | `8b5219491974`  |
| 2629   | Layout 1 | `8b5219491974`  |
| 2619   | Layout 1 | `8b5219491974`  |
| 2612   | Layout 1 | `8b5219491974`  |
| 2606   | Layout 1 | `8b5219491974`  |
| 2602   | Layout 1 | `8b5219491974`  |
| 2601   | Layout 1 | `8b5219491974`  |
| 2592   | Layout 1 | `8b5219491974`  |
| 2583   | Layout 1 | `8b5219491974`  |
| 2575   | Layout 1 | `8b5219491974`  |
| 2567   | Layout 1 | `8b5219491974`  |
| 2560   | Layout 1 | `8b5219491974`  |
| 2553   | Layout 1 | `8b5219491974`  |
| 2545   | Layout 1 | `8b5219491974`  |
| 2538   | Layout 1 | `8b5219491974`  |
| 2529   | Layout 1 | `8b5219491974`  |
| 2519   | Layout 1 | `8b5219491974`  |
| 2513   | Layout 1 | `8b5219491974`  |
| 2510   | Layout 1 | `8b5219491974`  |
| 2507   | Layout 1 | `8b5219491974`  |
| 2503   | Layout 1 | `8b5219491974`  |
| 2498   | Layout 1 | `8b5219491974`  |
| 2492   | Layout 1 | `8b5219491974`  |
| 2487   | Layout 1 | `8b5219491974`  |
| 2480   | Layout 1 | `8b5219491974`  |
| 2474   | Layout 1 | `8b5219491974`  |
| 2468   | Layout 1 | `8b5219491974`  |
| 2460   | Layout 1 | `8b5219491974`  |
| 2453   | Layout 1 | `8b5219491974`  |
| 2444   | Layout 1 | `8b5219491974`  |
| 2438   | Layout 1 | `8b5219491974`  |
| 2434   | Layout 1 | `8b5219491974`  |
| 2429   | Layout 1 | `8b5219491974`  |
| 2421   | Layout 1 | `8b5219491974`  |
| 2414   | Layout 1 | `8b5219491974`  |
| 2407   | Layout 1 | `8b5219491974`  |
| 2401   | Layout 1 | `8b5219491974`  |
| 2397   | Layout 1 | `8b5219491974`  |
| 2393   | Layout 1 | `8b5219491974`  |
| 2384   | Layout 1 | `8b5219491974`  |
| 2378   | Layout 1 | `8b5219491974`  |
| 2372   | Layout 1 | `8b5219491974`  |
| 2358   | Layout 1 | `8b5219491974`  |
| 2352   | Layout 1 | `8b5219491974`  |
| 2347   | Layout 1 | `8b5219491974`  |
| 2343   | Layout 1 | `8b5219491974`  |
| 2335   | Layout 1 | `8b5219491974`  |
| 2327   | Layout 1 | `8b5219491974`  |
| 2324   | Layout 1 | `8b5219491974`  |
| 2319   | Layout 1 | `8b5219491974`  |
| 2313   | Layout 1 | `8b5219491974`  |
| 2308   | Layout 1 | `8b5219491974`  |
| 2302   | Layout 1 | `8b5219491974`  |
| 2295   | Layout 1 | `8b5219491974`  |
| 2290   | Layout 1 | `8b5219491974`  |
| 2284   | Layout 1 | `8b5219491974`  |
| 2276   | Layout 1 | `8b5219491974`  |
| 2269   | Layout 1 | `8b5219491974`  |
| 2259   | Layout 1 | `8b5219491974`  |
| 2250   | Layout 1 | `8b5219491974`  |
| 2243   | Layout 1 | `8b5219491974`  |
| 2235   | Layout 1 | `8b5219491974`  |
| 2229   | Layout 1 | `8b5219491974`  |
| 2224   | Layout 1 | `8b5219491974`  |
| 2218   | Layout 1 | `8b5219491974`  |
| 2215   | Layout 1 | `8b5219491974`  |
| 2207   | Layout 1 | `8b5219491974`  |
| 2203   | Layout 1 | `8b5219491974`  |
| 2196   | Layout 1 | `8b5219491974`  |
| 2192   | Layout 1 | `8b5219491974`  |
| 2189   | Layout 1 | `8b5219491974`  |
| 2183   | Layout 1 | `8b5219491974`  |
| 2179   | Layout 1 | `8b5219491974`  |
| 2171   | Layout 1 | `8b5219491974`  |
| 2163   | Layout 1 | `8b5219491974`  |
| 2156   | Layout 1 | `8b5219491974`  |
| 2151   | Layout 1 | `8b5219491974`  |
| 2147   | Layout 1 | `8b5219491974`  |
| 2142   | Layout 1 | `8b5219491974`  |
| 2138   | Layout 1 | `8b5219491974`  |
| 2134   | Layout 1 | `8b5219491974`  |
| 2130   | Layout 1 | `8b5219491974`  |
| 2122   | Layout 1 | `8b5219491974`  |
| 2107   | Layout 1 | `8b5219491974`  |
| 2098   | Layout 1 | `8b5219491974`  |
| 2089   | Layout 1 | `8b5219491974`  |
| 2081   | Layout 1 | `8b5219491974`  |
| 2073   | Layout 1 | `8b5219491974`  |
| 2067   | Layout 1 | `8b5219491974`  |
| 2063   | Layout 1 | `8b5219491974`  |
| 2059   | Layout 1 | `8b5219491974`  |
| 2052   | Layout 1 | `8b5219491974`  |
| 2044   | Layout 1 | `8b5219491974`  |
| 2039   | Layout 1 | `8b5219491974`  |
| 2032   | Layout 1 | `8b5219491974`  |
| 2025   | Layout 1 | `8b5219491974`  |
| 2011   | Layout 1 | `8b5219491974`  |
| 2005   | Layout 1 | `8b5219491974`  |
| 2000   | Layout 1 | `8b5219491974`  |
| 1996   | Layout 1 | `8b5219491974`  |
| 1991   | Layout 1 | `8b5219491974`  |
| 1985   | Layout 1 | `8b5219491974`  |
| 1980   | Layout 1 | `8b5219491974`  |
| 1969   | Layout 1 | `8b5219491974`  |
| 1964   | Layout 1 | `8b5219491974`  |
| 1958   | Layout 1 | `8b5219491974`  |
| 1950   | Layout 1 | `8b5219491974`  |
| 1945   | Layout 1 | `8b5219491974`  |
| 1937   | Layout 1 | `8b5219491974`  |
| 1933   | Layout 1 | `8b5219491974`  |
| 1927   | Layout 1 | `8b5219491974`  |
| 1921   | Layout 1 | `8b5219491974`  |
| 1914   | Layout 1 | `8b5219491974`  |
| 1908   | Layout 1 | `8b5219491974`  |
| 1897   | Layout 1 | `8b5219491974`  |
| 1892   | Layout 1 | `8b5219491974`  |
| 1886   | Layout 1 | `8b5219491974`  |
| 1881   | Layout 1 | `8b5219491974`  |
| 1871   | Layout 1 | `8b5219491974`  |
| 1866   | Layout 1 | `8b5219491974`  |
| 1862   | Layout 1 | `8b5219491974`  |
| 1854   | Layout 1 | `8b5219491974`  |
| 1846   | Layout 1 | `8b5219491974`  |
| 1838   | Layout 1 | `8b5219491974`  |
| 1832   | Layout 1 | `8b5219491974`  |
| 1826   | Layout 1 | `8b5219491974`  |
| 1822   | Layout 1 | `8b5219491974`  |
| 1818   | Layout 1 | `8b5219491974`  |
| 1804   | Layout 1 | `8b5219491974`  |
| 1794   | Layout 1 | `8b5219491974`  |
| 1790   | Layout 1 | `8b5219491974`  |
| 1784   | Layout 1 | `8b5219491974`  |
| 1774   | Layout 1 | `8b5219491974`  |
| 1771   | Layout 1 | `8b5219491974`  |
| 1762   | Layout 1 | `8b5219491974`  |
| 1759   | Layout 1 | `8b5219491974`  |
| 1754   | Layout 1 | `8b5219491974`  |
| 1749   | Layout 1 | `8b5219491974`  |
| 1743   | Layout 1 | `8b5219491974`  |
| 1737   | Layout 1 | `8b5219491974`  |
| 1731   | Layout 1 | `8b5219491974`  |
| 1725   | Layout 1 | `8b5219491974`  |
| 1717   | Layout 1 | `8b5219491974`  |
| 1710   | Layout 1 | `8b5219491974`  |
| 1704   | Layout 1 | `8b5219491974`  |
| 1698   | Layout 1 | `8b5219491974`  |
| 1690   | Layout 1 | `8b5219491974`  |
| 1685   | Layout 1 | `8b5219491974`  |
| 1680   | Layout 1 | `8b5219491974`  |
| 1674   | Layout 1 | `8b5219491974`  |
| 1668   | Layout 1 | `8b5219491974`  |
| 1659   | Layout 1 | `8b5219491974`  |
| 1649   | Layout 1 | `8b5219491974`  |
| 1642   | Layout 1 | `8b5219491974`  |
| 1636   | Layout 1 | `8b5219491974`  |
| 1628   | Layout 1 | `8b5219491974`  |
| 1622   | Layout 1 | `8b5219491974`  |
| 1614   | Layout 1 | `8b5219491974`  |
| 1608   | Layout 1 | `8b5219491974`  |
| 1602   | Layout 1 | `8b5219491974`  |
| 1598   | Layout 1 | `8b5219491974`  |
| 1594   | Layout 1 | `8b5219491974`  |
| 1590   | Layout 1 | `8b5219491974`  |
| 1587   | Layout 1 | `8b5219491974`  |
| 1584   | Layout 1 | `8b5219491974`  |
| 1579   | Layout 1 | `8b5219491974`  |
| 1572   | Layout 1 | `8b5219491974`  |
| 1565   | Layout 1 | `8b5219491974`  |
| 1559   | Layout 1 | `8b5219491974`  |
| 1554   | Layout 1 | `8b5219491974`  |
| 1547   | Layout 1 | `8b5219491974`  |
| 1537   | Layout 1 | `8b5219491974`  |
| 1529   | Layout 1 | `8b5219491974`  |
| 1524   | Layout 1 | `8b5219491974`  |
| 1519   | Layout 1 | `8b5219491974`  |
| 1509   | Layout 1 | `8b5219491974`  |
| 1506   | Layout 1 | `8b5219491974`  |
| 1504   | Layout 1 | `8b5219491974`  |
| 1500   | Layout 1 | `8b5219491974`  |
| 1493   | Layout 1 | `8b5219491974`  |
| 1489   | Layout 1 | `8b5219491974`  |
| 1485   | Layout 1 | `8b5219491974`  |
| 1481   | Layout 1 | `8b5219491974`  |
| 1474   | Layout 1 | `8b5219491974`  |
| 1466   | Layout 1 | `8b5219491974`  |
| 1462   | Layout 1 | `8b5219491974`  |
| 1459   | Layout 1 | `8b5219491974`  |
| 1453   | Layout 1 | `8b5219491974`  |
| 1450   | Layout 1 | `8b5219491974`  |
| 1445   | Layout 1 | `8b5219491974`  |
| 1439   | Layout 1 | `8b5219491974`  |
| 1433   | Layout 1 | `8b5219491974`  |
| 1430   | Layout 1 | `8b5219491974`  |
| 1426   | Layout 1 | `8b5219491974`  |
| 1421   | Layout 1 | `8b5219491974`  |
| 1417   | No file  | `8b5219491974`  |
| 1416   | No file  | `8b5219491974`  |
| 1409   | No file  | `8b5219491974`  |
| 1405   | No file  | `8b5219491974`  |
| 1401   | No file  | `8b5219491974`  |
| 1396   | No file  | `8b5219491974`  |
| 1391   | No file  | `8b5219491974`  |
| 1390   | No file  | `8b5219491974`  |
| 1386   | No file  | `8b5219491974`  |
| 1381   | No file  | `8b5219491974`  |
| 1379   | No file  | `8b5219491974`  |
| 1372   | No file  | `8b5219491974`  |
| 1366   | No file  | `8b5219491974`  |
| 1364   | No file  | `8b5219491974`  |
| 1363   | No file  | `8b5219491974`  |
| 1360   | No file  | `8b5219491974`  |
| 1358   | No file  | `8b5219491974`  |
| 1355   | No file  | `8b5219491974`  |
| 1351   | No file  | `8b5219491974`  |
| 1348   | No file  | `8b5219491974`  |
| 1346   | No file  | `8b5219491974`  |
| 1341   | No file  | `8b5219491974`  |
| 1340   | No file  | `8b5219491974`  |
| 1338   | No file  | `8b5219491974`  |
| 1335   | No file  | `8b5219491974`  |
| 1333   | No file  | `8b5219491974`  |
| 1329   | No file  | `8b5219491974`  |
| 1327   | No file  | `8b5219491974`  |
| 1324   | No file  | `8b5219491974`  |
| 1321   | No file  | `8b5219491974`  |
| 1319   | No file  | `8b5219491974`  |
| 1318   | No file  | `8b5219491974`  |
| 1316   | No file  | `8b5219491974`  |
| 1313   | No file  | `8b5219491974`  |
| 1311   | No file  | `8b5219491974`  |
| 1309   | No file  | `8b5219491974`  |
| 1304   | No file  | `8b5219491974`  |
| 1292   | No file  | `8b5219491974`  |
| 1286   | No file  | `8b5219491974`  |
| 1280   | No file  | `8b5219491974`  |
| 1276   | No file  | `8b5219491974`  |
| 1267   | No file  | `8b5219491974`  |
| 1261   | No file  | `8b5219491974`  |
| 1256   | No file  | `8b5219491974`  |
| 1250   | No file  | `8b5219491974`  |
| 1246   | No file  | `8b5219491974`  |
| 1239   | No file  | `8b5219491974`  |
| 1230   | No file  | `8b5219491974`  |
| 1226   | No file  | `8b5219491974`  |
| 1220   | No file  | `8b5219491974`  |
| 1217   | No file  | `8b5219491974`  |
| 1211   | No file  | `8b5219491974`  |
| 1210   | No file  | `8b5219491974`  |
| 1208   | No file  | `8b5219491974`  |
| 1203   | No file  | `8b5219491974`  |
| 1197   | No file  | `8b5219491974`  |
| 1194   | No file  | `8b5219491974`  |
| 1192   | No file  | `8b5219491974`  |
| 1187   | No file  | `8b5219491974`  |
| 1183   | No file  | `8b5219491974`  |
| 1177   | No file  | `8b5219491974`  |
| 1173   | No file  | `8b5219491974`  |
| 1167   | No file  | `8b5219491974`  |
| 1164   | No file  | `8b5219491974`  |
| 1156   | No file  | `8b5219491974`  |
| 1149   | No file  | `8b5219491974`  |
| 1144   | No file  | `8b5219491974`  |
| 1137   | No file  | `8b5219491974`  |
| 1132   | No file  | `8b5219491974`  |
| 1127   | No file  | `8b5219491974`  |
| 1122   | No file  | `8b5219491974`  |
| 1118   | No file  | `8b5219491974`  |
| 1114   | No file  | `8b5219491974`  |
| 1109   | No file  | `8b5219491974`  |
| 1102   | No file  | `8b5219491974`  |
| 1096   | No file  | `8b5219491974`  |
| 1088   | No file  | `8b5219491974`  |
| 1081   | No file  | `8b5219491974`  |
| 1076   | No file  | `8b5219491974`  |
| 1069   | No file  | `8b5219491974`  |
| 1064   | No file  | `8b5219491974`  |
| 1058   | No file  | `8b5219491974`  |
| 1051   | No file  | `8b5219491974`  |
| 1044   | No file  | `8b5219491974`  |
| 1036   | No file  | `8b5219491974`  |
| 1026   | No file  | `8b5219491974`  |
| 1016   | No file  | `8b5219491974`  |
| 1009   | No file  | `8b5219491974`  |
| 1005   | No file  | `8b5219491974`  |
| 1000   | No file  | `8b5219491974`  |
| 998    | No file  | `8b5219491974`  |
| 990    | No file  | `8b5219491974`  |
| 979    | No file  | `8b5219491974`  |
| 972    | No file  | `8b5219491974`  |
| 963    | No file  | `8b5219491974`  |
| 955    | No file  | `8b5219491974`  |
| 946    | No file  | `8b5219491974`  |
| 938    | No file  | `8b5219491974`  |
| 927    | No file  | `8b5219491974`  |
| 911    | No file  | `8b5219491974`  |
| 904    | No file  | `8b5219491974`  |
| 899    | No file  | `8b5219491974`  |
| 894    | No file  | `8b5219491974`  |
| 885    | No file  | `8b5219491974`  |
| 879    | No file  | `8b5219491974`  |
| 872    | No file  | `8b5219491974`  |
| 864    | No file  | `8b5219491974`  |
| 855    | No file  | `8b5219491974`  |
| 853    | No file  | `8b5219491974`  |
| 845    | No file  | `8b5219491974`  |
| 837    | No file  | `8b5219491974`  |
| 829    | No file  | `8b5219491974`  |
| 822    | No file  | `8b5219491974`  |
| 814    | No file  | `8b5219491974`  |
| 805    | No file  | `8b5219491974`  |
| 794    | No file  | `8b5219491974`  |
| 787    | No file  | `8b5219491974`  |
| 780    | No file  | `8b5219491974`  |
| 771    | No file  | `8b5219491974`  |
| 760    | No file  | `8b5219491974`  |
| 748    | No file  | `8b5219491974`  |
| 741    | No file  | `8b5219491974`  |
| 736    | No file  | `8b5219491974`  |
| 731    | No file  | `8b5219491974`  |
| 723    | No file  | `8b5219491974`  |
| 711    | No file  | `8b5219491974`  |
| 707    | No file  | `8b5219491974`  |
| 697    | No file  | `8b5219491974`  |
| 689    | No file  | `8b5219491974`  |
| 683    | No file  | `8b5219491974`  |
| 678    | No file  | `8b5219491974`  |
| 670    | No file  | `8b5219491974`  |
| 661    | No file  | `8b5219491974`  |
| 656    | No file  | `8b5219491974`  |
| 652    | No file  | `8b5219491974`  |
| 643    | No file  | `8b5219491974`  |
| 637    | No file  | `8b5219491974`  |
| 630    | No file  | `8b5219491974`  |
| 627    | No file  | `8b5219491974`  |
| 621    | No file  | `8b5219491974`  |
| 617    | No file  | `8b5219491974`  |
| 615    | No file  | `8b5219491974`  |
| 606    | No file  | `8b5219491974`  |
| 599    | No file  | `8b5219491974`  |
| 592    | No file  | `8b5219491974`  |
| 586    | No file  | `8b5219491974`  |
| 577    | No file  | `8b5219491974`  |
| 569    | No file  | `8b5219491974`  |
| 561    | No file  | `8b5219491974`  |
| 554    | No file  | `8b5219491974`  |
| 542    | No file  | `8b5219491974`  |
| 532    | No file  | `8b5219491974`  |
| 531    | No file  | `8b5219491974`  |
| 526    | No file  | `8b5219491974`  |
| 521    | No file  | `8b5219491974`  |
| 517    | No file  | `8b5219491974`  |
| 510    | No file  | `8b5219491974`  |
| 508    | No file  | `8b5219491974`  |
| 504    | No file  | `8b5219491974`  |
| 497    | No file  | `8b5219491974`  |
| 491    | No file  | `8b5219491974`  |
| 485    | No file  | `8b5219491974`  |
| 478    | No file  | `8b5219491974`  |
| 472    | No file  | `8b5219491974`  |
| 466    | No file  | `8b5219491974`  |
| 457    | No file  | `8b5219491974`  |
| 452    | No file  | `8b5219491974`  |
| 449    | No file  | `8b5219491974`  |
| 435    | No file  | `8b5219491974`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 5 bytes + flags)

| Offset  | Type              | Field       | Notes                                                                    |
| ------- | ----------------- | ----------- | ------------------------------------------------------------------------ |
| `+0x00` | u8                | index       | Right index, row key                                                     |
| `+0x01` | u32               | grade_count | Number of flags, one per member grade; `11` on client 3474, `8` on 1784  |
| `+0x05` | u8[grade_count]   | grade       | `1` when member grade `N` (the flag's position) holds the right; see Grades |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Grades

A flag's position is the member grade number. The 2016 `gc::GuildMemberGrade`
has three: `0` `eGuildMemberGradeMaster`, `1` `eGuildMemberGradeSubMaster`
and `2` `eGuildMemberGradeNormal`. The client Lua of client 3474 names 11
grades without their values: `__eGuildMemberGradeMaster`, `SubMaster`,
`Normal`, `Junior`, `SupplyOfficer`, `Adviser`, `Scribe`, `Gunner`,
`ChiefOfStaff`, `MissionOfficer` and `Volunteer`, the same number as the
flags. The flag count grew from 8 (clients 1784 and 2107) to 11 (client
2519 and later). The handler shows the numbers of the set flags
(`0, 1, 6, 8, 9`).

On client 3474, `0` is set on 52 of the 55 rows, which fits `0` as the
master. The other three are index `30` (`2, 5, 10`), `35` (`1, 6, 8, 9`)
and `49` (`2, 3, 7, 10`).

## Field Names

`index` and `grade` follow the `GuildRight_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784: its `Index` column is the row
key and its `Grade` column lists the grade numbers whose flag is set (50 of
50 rows match the client 1784 file). The sheet's third column,
`ContentsGroupKey` (`1503` on every row), is not in the file.

## Notes

- Client 1784 has 50 rows of 8 flags (670 bytes), client 2107 52 rows of
  8, clients 2519 to 3474 55 rows of 11 (900 bytes).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`.

## Open Questions

### Right Index Names

The Lua names 34 `__eGuildRightType_*` rights (`SetGuildMark`,
`GuildDestroy`, `Notice`, `QuestAccept`, ...) without their values, so
`index` cannot be tied to a name. The 1784 sheet has no name column.

### Grade Numbers Above 2

Which `__eGuildMemberGrade*` name each grade number from `3` to `10` has.
Grade `6` is set together with grade `0` on 45 of the 55 rows (client
3474), and every [guildspecialskillright](guildspecialskillright_bss.md) row sets
`0`, `6`, `8` and `9`.
