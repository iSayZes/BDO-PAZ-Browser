# `guildrightnewstaticstatus.bss` Format

## Purpose

The rights of the guild authority window, in groups: per group its number
and Korean name, then each right with its number, Korean name and Korean
description, all three texts in the PABR string table. On client 3474 the
file has 4 groups (관리 management, 활동 activities, 전투 combat, 재정
finance) with 39 rights, numbers `1` to `41` without `9` and `20`. The
right numbers are the `__eGuildRightNew_*` values the Lua checks; right
`29` (길드 리그 신청) signs a guild up for the Guild League of
[guildmatchoption](guildmatchoption_bss.md), and right `14` (길드 하우스
제작) is guild house crafting, the skills of
[guildhousecraftskill](../dbss/guildhousecraftskill_dbss.md). The older rights
per member grade are in [guildright](guildright_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                            | Bytes | Records           | Row bytes |
| ------ | -------------- | ------------------------------- | ----- | ----------------- | --------- |
| 1      | 2538 and later | `guildrightnewstaticstatus.bss` | 4,880 | 39 Right, 4 Group | 12        |

| Layout | File                            | Known           | Unknown    |
| ------ | ------------------------------- | --------------- | ---------- |
| 1      | `guildrightnewstaticstatus.bss` | 4,876 B (99.9%) | 4 B (0.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `1c79d45515ee`  |
| 3482   | Layout 1 | `1c79d45515ee`  |
| 3474   | Layout 1 | `1c79d45515ee`  |
| 3473   | Layout 1 | `1c79d45515ee`  |
| 3464   | Layout 1 | `1c79d45515ee`  |
| 3458   | Layout 1 | `1c79d45515ee`  |
| 3454   | Layout 1 | `1c79d45515ee`  |
| 3444   | Layout 1 | `1c79d45515ee`  |
| 3435   | Layout 1 | `1c79d45515ee`  |
| 3426   | Layout 1 | `1c79d45515ee`  |
| 3418   | Layout 1 | `1c79d45515ee`  |
| 3412   | Layout 1 | `1c79d45515ee`  |
| 3402   | Layout 1 | `1c79d45515ee`  |
| 3396   | Layout 1 | `1c79d45515ee`  |
| 3387   | Layout 1 | `1c79d45515ee`  |
| 3381   | Layout 1 | `1c79d45515ee`  |
| 3373   | Layout 1 | `1c79d45515ee`  |
| 3364   | Layout 1 | `1c79d45515ee`  |
| 3356   | Layout 1 | `1c79d45515ee`  |
| 3349   | Layout 1 | `1c79d45515ee`  |
| 3342   | Layout 1 | `1c79d45515ee`  |
| 3335   | Layout 1 | `1c79d45515ee`  |
| 3326   | Layout 1 | `1c79d45515ee`  |
| 3321   | Layout 1 | `1c79d45515ee`  |
| 3314   | Layout 1 | `1c79d45515ee`  |
| 3303   | Layout 1 | `1c79d45515ee`  |
| 3302   | Layout 1 | `1c79d45515ee`  |
| 3293   | Layout 1 | `1c79d45515ee`  |
| 3283   | Layout 1 | `1c79d45515ee`  |
| 3275   | Layout 1 | `1c79d45515ee`  |
| 3267   | Layout 1 | `1c79d45515ee`  |
| 3258   | Layout 1 | `1c79d45515ee`  |
| 3251   | Layout 1 | `1c79d45515ee`  |
| 3242   | Layout 1 | `1c79d45515ee`  |
| 3235   | Layout 1 | `1c79d45515ee`  |
| 3229   | Layout 1 | `1c79d45515ee`  |
| 3212   | Layout 1 | `1c79d45515ee`  |
| 3203   | Layout 1 | `1c79d45515ee`  |
| 3193   | Layout 1 | `1c79d45515ee`  |
| 3186   | Layout 1 | `1c79d45515ee`  |
| 3177   | Layout 1 | `1c79d45515ee`  |
| 3169   | Layout 1 | `1c79d45515ee`  |
| 3158   | Layout 1 | `1c79d45515ee`  |
| 3151   | Layout 1 | `1c79d45515ee`  |
| 3144   | Layout 1 | `1c79d45515ee`  |
| 3133   | Layout 1 | `1c79d45515ee`  |
| 3125   | Layout 1 | `1c79d45515ee`  |
| 3118   | Layout 1 | `1c79d45515ee`  |
| 3111   | Layout 1 | `1c79d45515ee`  |
| 3103   | Layout 1 | `1c79d45515ee`  |
| 3095   | Layout 1 | `1c79d45515ee`  |
| 3086   | Layout 1 | `1c79d45515ee`  |
| 3072   | Layout 1 | `1c79d45515ee`  |
| 3062   | Layout 1 | `1c79d45515ee`  |
| 3052   | Layout 1 | `1c79d45515ee`  |
| 3045   | Layout 1 | `1c79d45515ee`  |
| 3037   | Layout 1 | `1c79d45515ee`  |
| 3030   | Layout 1 | `1c79d45515ee`  |
| 3021   | Layout 1 | `1c79d45515ee`  |
| 3012   | Layout 1 | `1c79d45515ee`  |
| 3002   | Layout 1 | `1c79d45515ee`  |
| 2995   | Layout 1 | `1c79d45515ee`  |
| 2987   | Layout 1 | `1c79d45515ee`  |
| 2978   | Layout 1 | `1c79d45515ee`  |
| 2970   | Layout 1 | `1c79d45515ee`  |
| 2959   | Layout 1 | `1c79d45515ee`  |
| 2951   | Layout 1 | `1c79d45515ee`  |
| 2942   | Layout 1 | `1c79d45515ee`  |
| 2935   | Layout 1 | `1c79d45515ee`  |
| 2932   | Layout 1 | `1c79d45515ee`  |
| 2923   | Layout 1 | `1c79d45515ee`  |
| 2919   | Layout 1 | `1c79d45515ee`  |
| 2907   | Layout 1 | `1c79d45515ee`  |
| 2900   | Layout 1 | `1c79d45515ee`  |
| 2891   | Layout 1 | `1c79d45515ee`  |
| 2882   | Layout 1 | `1c79d45515ee`  |
| 2872   | Layout 1 | `1c79d45515ee`  |
| 2863   | Layout 1 | `1c79d45515ee`  |
| 2855   | Layout 1 | `1c79d45515ee`  |
| 2849   | Layout 1 | `1c79d45515ee`  |
| 2844   | Layout 1 | `1c79d45515ee`  |
| 2834   | Layout 1 | `1c79d45515ee`  |
| 2825   | Layout 1 | `1c79d45515ee`  |
| 2819   | Layout 1 | `1c79d45515ee`  |
| 2811   | Layout 1 | `1c79d45515ee`  |
| 2803   | Layout 1 | `1c79d45515ee`  |
| 2794   | Layout 1 | `1c79d45515ee`  |
| 2783   | Layout 1 | `1c79d45515ee`  |
| 2774   | Layout 1 | `1c79d45515ee`  |
| 2765   | Layout 1 | `1c79d45515ee`  |
| 2756   | Layout 1 | `1c79d45515ee`  |
| 2750   | Layout 1 | `1c79d45515ee`  |
| 2743   | Layout 1 | `1c79d45515ee`  |
| 2736   | Layout 1 | `1c79d45515ee`  |
| 2726   | Layout 1 | `1c79d45515ee`  |
| 2717   | Layout 1 | `1c79d45515ee`  |
| 2709   | Layout 1 | `1c79d45515ee`  |
| 2703   | Layout 1 | `1c79d45515ee`  |
| 2695   | Layout 1 | `1c79d45515ee`  |
| 2684   | Layout 1 | `1c79d45515ee`  |
| 2672   | Layout 1 | `1c79d45515ee`  |
| 2665   | Layout 1 | `1c79d45515ee`  |
| 2657   | Layout 1 | `1c79d45515ee`  |
| 2649   | Layout 1 | `1c79d45515ee`  |
| 2644   | Layout 1 | `1c79d45515ee`  |
| 2637   | Layout 1 | `1c79d45515ee`  |
| 2629   | Layout 1 | `1c79d45515ee`  |
| 2619   | Layout 1 | `1c79d45515ee`  |
| 2612   | Layout 1 | `1c79d45515ee`  |
| 2606   | Layout 1 | `1c79d45515ee`  |
| 2602   | Layout 1 | `1c79d45515ee`  |
| 2601   | Layout 1 | `1c79d45515ee`  |
| 2592   | Layout 1 | `1c79d45515ee`  |
| 2583   | Layout 1 | `1c79d45515ee`  |
| 2575   | Layout 1 | `1c79d45515ee`  |
| 2567   | Layout 1 | `1c79d45515ee`  |
| 2560   | Layout 1 | `1c79d45515ee`  |
| 2553   | Layout 1 | `1c79d45515ee`  |
| 2545   | Layout 1 | `1c79d45515ee`  |
| 2538   | Layout 1 | `1c79d45515ee`  |
| 2529   | No file  | `1c79d45515ee`  |
| 2519   | No file  | `1c79d45515ee`  |
| 2513   | No file  | `1c79d45515ee`  |
| 2510   | No file  | `1c79d45515ee`  |
| 2507   | No file  | `1c79d45515ee`  |
| 2503   | No file  | `1c79d45515ee`  |
| 2498   | No file  | `1c79d45515ee`  |
| 2492   | No file  | `1c79d45515ee`  |
| 2487   | No file  | `1c79d45515ee`  |
| 2480   | No file  | `1c79d45515ee`  |
| 2474   | No file  | `1c79d45515ee`  |
| 2468   | No file  | `1c79d45515ee`  |
| 2460   | No file  | `1c79d45515ee`  |
| 2453   | No file  | `1c79d45515ee`  |
| 2444   | No file  | `1c79d45515ee`  |
| 2438   | No file  | `1c79d45515ee`  |
| 2434   | No file  | `1c79d45515ee`  |
| 2429   | No file  | `1c79d45515ee`  |
| 2421   | No file  | `1c79d45515ee`  |
| 2414   | No file  | `1c79d45515ee`  |
| 2407   | No file  | `1c79d45515ee`  |
| 2401   | No file  | `1c79d45515ee`  |
| 2397   | No file  | `1c79d45515ee`  |
| 2393   | No file  | `1c79d45515ee`  |
| 2384   | No file  | `1c79d45515ee`  |
| 2378   | No file  | `1c79d45515ee`  |
| 2372   | No file  | `1c79d45515ee`  |
| 2358   | No file  | `1c79d45515ee`  |
| 2352   | No file  | `1c79d45515ee`  |
| 2347   | No file  | `1c79d45515ee`  |
| 2343   | No file  | `1c79d45515ee`  |
| 2335   | No file  | `1c79d45515ee`  |
| 2327   | No file  | `1c79d45515ee`  |
| 2324   | No file  | `1c79d45515ee`  |
| 2319   | No file  | `1c79d45515ee`  |
| 2313   | No file  | `1c79d45515ee`  |
| 2308   | No file  | `1c79d45515ee`  |
| 2302   | No file  | `1c79d45515ee`  |
| 2295   | No file  | `1c79d45515ee`  |
| 2290   | No file  | `1c79d45515ee`  |
| 2284   | No file  | `1c79d45515ee`  |
| 2276   | No file  | `1c79d45515ee`  |
| 2269   | No file  | `1c79d45515ee`  |
| 2259   | No file  | `1c79d45515ee`  |
| 2250   | No file  | `1c79d45515ee`  |
| 2243   | No file  | `1c79d45515ee`  |
| 2235   | No file  | `1c79d45515ee`  |
| 2229   | No file  | `1c79d45515ee`  |
| 2224   | No file  | `1c79d45515ee`  |
| 2218   | No file  | `1c79d45515ee`  |
| 2215   | No file  | `1c79d45515ee`  |
| 2207   | No file  | `1c79d45515ee`  |
| 2203   | No file  | `1c79d45515ee`  |
| 2196   | No file  | `1c79d45515ee`  |
| 2192   | No file  | `1c79d45515ee`  |
| 2189   | No file  | `1c79d45515ee`  |
| 2183   | No file  | `1c79d45515ee`  |
| 2179   | No file  | `1c79d45515ee`  |
| 2171   | No file  | `1c79d45515ee`  |
| 2163   | No file  | `1c79d45515ee`  |
| 2156   | No file  | `1c79d45515ee`  |
| 2151   | No file  | `1c79d45515ee`  |
| 2147   | No file  | `1c79d45515ee`  |
| 2142   | No file  | `1c79d45515ee`  |
| 2138   | No file  | `1c79d45515ee`  |
| 2134   | No file  | `1c79d45515ee`  |
| 2130   | No file  | `1c79d45515ee`  |
| 2122   | No file  | `1c79d45515ee`  |
| 2107   | No file  | `1c79d45515ee`  |
| 2098   | No file  | `1c79d45515ee`  |
| 2089   | No file  | `1c79d45515ee`  |
| 2081   | No file  | `1c79d45515ee`  |
| 2073   | No file  | `1c79d45515ee`  |
| 2067   | No file  | `1c79d45515ee`  |
| 2063   | No file  | `1c79d45515ee`  |
| 2059   | No file  | `1c79d45515ee`  |
| 2052   | No file  | `1c79d45515ee`  |
| 2044   | No file  | `1c79d45515ee`  |
| 2039   | No file  | `1c79d45515ee`  |
| 2032   | No file  | `1c79d45515ee`  |
| 2025   | No file  | `1c79d45515ee`  |
| 2011   | No file  | `1c79d45515ee`  |
| 2005   | No file  | `1c79d45515ee`  |
| 2000   | No file  | `1c79d45515ee`  |
| 1996   | No file  | `1c79d45515ee`  |
| 1991   | No file  | `1c79d45515ee`  |
| 1985   | No file  | `1c79d45515ee`  |
| 1980   | No file  | `1c79d45515ee`  |
| 1969   | No file  | `1c79d45515ee`  |
| 1964   | No file  | `1c79d45515ee`  |
| 1958   | No file  | `1c79d45515ee`  |
| 1950   | No file  | `1c79d45515ee`  |
| 1945   | No file  | `1c79d45515ee`  |
| 1937   | No file  | `1c79d45515ee`  |
| 1933   | No file  | `1c79d45515ee`  |
| 1927   | No file  | `1c79d45515ee`  |
| 1921   | No file  | `1c79d45515ee`  |
| 1914   | No file  | `1c79d45515ee`  |
| 1908   | No file  | `1c79d45515ee`  |
| 1897   | No file  | `1c79d45515ee`  |
| 1892   | No file  | `1c79d45515ee`  |
| 1886   | No file  | `1c79d45515ee`  |
| 1881   | No file  | `1c79d45515ee`  |
| 1871   | No file  | `1c79d45515ee`  |
| 1866   | No file  | `1c79d45515ee`  |
| 1862   | No file  | `1c79d45515ee`  |
| 1854   | No file  | `1c79d45515ee`  |
| 1846   | No file  | `1c79d45515ee`  |
| 1838   | No file  | `1c79d45515ee`  |
| 1832   | No file  | `1c79d45515ee`  |
| 1826   | No file  | `1c79d45515ee`  |
| 1822   | No file  | `1c79d45515ee`  |
| 1818   | No file  | `1c79d45515ee`  |
| 1804   | No file  | `1c79d45515ee`  |
| 1794   | No file  | `1c79d45515ee`  |
| 1790   | No file  | `1c79d45515ee`  |
| 1784   | No file  | `1c79d45515ee`  |
| 1774   | No file  | `1c79d45515ee`  |
| 1771   | No file  | `1c79d45515ee`  |
| 1762   | No file  | `1c79d45515ee`  |
| 1759   | No file  | `1c79d45515ee`  |
| 1754   | No file  | `1c79d45515ee`  |
| 1749   | No file  | `1c79d45515ee`  |
| 1743   | No file  | `1c79d45515ee`  |
| 1737   | No file  | `1c79d45515ee`  |
| 1731   | No file  | `1c79d45515ee`  |
| 1725   | No file  | `1c79d45515ee`  |
| 1717   | No file  | `1c79d45515ee`  |
| 1710   | No file  | `1c79d45515ee`  |
| 1704   | No file  | `1c79d45515ee`  |
| 1698   | No file  | `1c79d45515ee`  |
| 1690   | No file  | `1c79d45515ee`  |
| 1685   | No file  | `1c79d45515ee`  |
| 1680   | No file  | `1c79d45515ee`  |
| 1674   | No file  | `1c79d45515ee`  |
| 1668   | No file  | `1c79d45515ee`  |
| 1659   | No file  | `1c79d45515ee`  |
| 1649   | No file  | `1c79d45515ee`  |
| 1642   | No file  | `1c79d45515ee`  |
| 1636   | No file  | `1c79d45515ee`  |
| 1628   | No file  | `1c79d45515ee`  |
| 1622   | No file  | `1c79d45515ee`  |
| 1614   | No file  | `1c79d45515ee`  |
| 1608   | No file  | `1c79d45515ee`  |
| 1602   | No file  | `1c79d45515ee`  |
| 1598   | No file  | `1c79d45515ee`  |
| 1594   | No file  | `1c79d45515ee`  |
| 1590   | No file  | `1c79d45515ee`  |
| 1587   | No file  | `1c79d45515ee`  |
| 1584   | No file  | `1c79d45515ee`  |
| 1579   | No file  | `1c79d45515ee`  |
| 1572   | No file  | `1c79d45515ee`  |
| 1565   | No file  | `1c79d45515ee`  |
| 1559   | No file  | `1c79d45515ee`  |
| 1554   | No file  | `1c79d45515ee`  |
| 1547   | No file  | `1c79d45515ee`  |
| 1537   | No file  | `1c79d45515ee`  |
| 1529   | No file  | `1c79d45515ee`  |
| 1524   | No file  | `1c79d45515ee`  |
| 1519   | No file  | `1c79d45515ee`  |
| 1509   | No file  | `1c79d45515ee`  |
| 1506   | No file  | `1c79d45515ee`  |
| 1504   | No file  | `1c79d45515ee`  |
| 1500   | No file  | `1c79d45515ee`  |
| 1493   | No file  | `1c79d45515ee`  |
| 1489   | No file  | `1c79d45515ee`  |
| 1485   | No file  | `1c79d45515ee`  |
| 1481   | No file  | `1c79d45515ee`  |
| 1474   | No file  | `1c79d45515ee`  |
| 1466   | No file  | `1c79d45515ee`  |
| 1462   | No file  | `1c79d45515ee`  |
| 1459   | No file  | `1c79d45515ee`  |
| 1453   | No file  | `1c79d45515ee`  |
| 1450   | No file  | `1c79d45515ee`  |
| 1445   | No file  | `1c79d45515ee`  |
| 1439   | No file  | `1c79d45515ee`  |
| 1433   | No file  | `1c79d45515ee`  |
| 1430   | No file  | `1c79d45515ee`  |
| 1426   | No file  | `1c79d45515ee`  |
| 1421   | No file  | `1c79d45515ee`  |
| 1417   | No file  | `1c79d45515ee`  |
| 1416   | No file  | `1c79d45515ee`  |
| 1409   | No file  | `1c79d45515ee`  |
| 1405   | No file  | `1c79d45515ee`  |
| 1401   | No file  | `1c79d45515ee`  |
| 1396   | No file  | `1c79d45515ee`  |
| 1391   | No file  | `1c79d45515ee`  |
| 1390   | No file  | `1c79d45515ee`  |
| 1386   | No file  | `1c79d45515ee`  |
| 1381   | No file  | `1c79d45515ee`  |
| 1379   | No file  | `1c79d45515ee`  |
| 1372   | No file  | `1c79d45515ee`  |
| 1366   | No file  | `1c79d45515ee`  |
| 1364   | No file  | `1c79d45515ee`  |
| 1363   | No file  | `1c79d45515ee`  |
| 1360   | No file  | `1c79d45515ee`  |
| 1358   | No file  | `1c79d45515ee`  |
| 1355   | No file  | `1c79d45515ee`  |
| 1351   | No file  | `1c79d45515ee`  |
| 1348   | No file  | `1c79d45515ee`  |
| 1346   | No file  | `1c79d45515ee`  |
| 1341   | No file  | `1c79d45515ee`  |
| 1340   | No file  | `1c79d45515ee`  |
| 1338   | No file  | `1c79d45515ee`  |
| 1335   | No file  | `1c79d45515ee`  |
| 1333   | No file  | `1c79d45515ee`  |
| 1329   | No file  | `1c79d45515ee`  |
| 1327   | No file  | `1c79d45515ee`  |
| 1324   | No file  | `1c79d45515ee`  |
| 1321   | No file  | `1c79d45515ee`  |
| 1319   | No file  | `1c79d45515ee`  |
| 1318   | No file  | `1c79d45515ee`  |
| 1316   | No file  | `1c79d45515ee`  |
| 1313   | No file  | `1c79d45515ee`  |
| 1311   | No file  | `1c79d45515ee`  |
| 1309   | No file  | `1c79d45515ee`  |
| 1304   | No file  | `1c79d45515ee`  |
| 1292   | No file  | `1c79d45515ee`  |
| 1286   | No file  | `1c79d45515ee`  |
| 1280   | No file  | `1c79d45515ee`  |
| 1276   | No file  | `1c79d45515ee`  |
| 1267   | No file  | `1c79d45515ee`  |
| 1261   | No file  | `1c79d45515ee`  |
| 1256   | No file  | `1c79d45515ee`  |
| 1250   | No file  | `1c79d45515ee`  |
| 1246   | No file  | `1c79d45515ee`  |
| 1239   | No file  | `1c79d45515ee`  |
| 1230   | No file  | `1c79d45515ee`  |
| 1226   | No file  | `1c79d45515ee`  |
| 1220   | No file  | `1c79d45515ee`  |
| 1217   | No file  | `1c79d45515ee`  |
| 1211   | No file  | `1c79d45515ee`  |
| 1210   | No file  | `1c79d45515ee`  |
| 1208   | No file  | `1c79d45515ee`  |
| 1203   | No file  | `1c79d45515ee`  |
| 1197   | No file  | `1c79d45515ee`  |
| 1194   | No file  | `1c79d45515ee`  |
| 1192   | No file  | `1c79d45515ee`  |
| 1187   | No file  | `1c79d45515ee`  |
| 1183   | No file  | `1c79d45515ee`  |
| 1177   | No file  | `1c79d45515ee`  |
| 1173   | No file  | `1c79d45515ee`  |
| 1167   | No file  | `1c79d45515ee`  |
| 1164   | No file  | `1c79d45515ee`  |
| 1156   | No file  | `1c79d45515ee`  |
| 1149   | No file  | `1c79d45515ee`  |
| 1144   | No file  | `1c79d45515ee`  |
| 1137   | No file  | `1c79d45515ee`  |
| 1132   | No file  | `1c79d45515ee`  |
| 1127   | No file  | `1c79d45515ee`  |
| 1122   | No file  | `1c79d45515ee`  |
| 1118   | No file  | `1c79d45515ee`  |
| 1114   | No file  | `1c79d45515ee`  |
| 1109   | No file  | `1c79d45515ee`  |
| 1102   | No file  | `1c79d45515ee`  |
| 1096   | No file  | `1c79d45515ee`  |
| 1088   | No file  | `1c79d45515ee`  |
| 1081   | No file  | `1c79d45515ee`  |
| 1076   | No file  | `1c79d45515ee`  |
| 1069   | No file  | `1c79d45515ee`  |
| 1064   | No file  | `1c79d45515ee`  |
| 1058   | No file  | `1c79d45515ee`  |
| 1051   | No file  | `1c79d45515ee`  |
| 1044   | No file  | `1c79d45515ee`  |
| 1036   | No file  | `1c79d45515ee`  |
| 1026   | No file  | `1c79d45515ee`  |
| 1016   | No file  | `1c79d45515ee`  |
| 1009   | No file  | `1c79d45515ee`  |
| 1005   | No file  | `1c79d45515ee`  |
| 1000   | No file  | `1c79d45515ee`  |
| 998    | No file  | `1c79d45515ee`  |
| 990    | No file  | `1c79d45515ee`  |
| 979    | No file  | `1c79d45515ee`  |
| 972    | No file  | `1c79d45515ee`  |
| 963    | No file  | `1c79d45515ee`  |
| 955    | No file  | `1c79d45515ee`  |
| 946    | No file  | `1c79d45515ee`  |
| 938    | No file  | `1c79d45515ee`  |
| 927    | No file  | `1c79d45515ee`  |
| 911    | No file  | `1c79d45515ee`  |
| 904    | No file  | `1c79d45515ee`  |
| 899    | No file  | `1c79d45515ee`  |
| 894    | No file  | `1c79d45515ee`  |
| 885    | No file  | `1c79d45515ee`  |
| 879    | No file  | `1c79d45515ee`  |
| 872    | No file  | `1c79d45515ee`  |
| 864    | No file  | `1c79d45515ee`  |
| 855    | No file  | `1c79d45515ee`  |
| 853    | No file  | `1c79d45515ee`  |
| 845    | No file  | `1c79d45515ee`  |
| 837    | No file  | `1c79d45515ee`  |
| 829    | No file  | `1c79d45515ee`  |
| 822    | No file  | `1c79d45515ee`  |
| 814    | No file  | `1c79d45515ee`  |
| 805    | No file  | `1c79d45515ee`  |
| 794    | No file  | `1c79d45515ee`  |
| 787    | No file  | `1c79d45515ee`  |
| 780    | No file  | `1c79d45515ee`  |
| 771    | No file  | `1c79d45515ee`  |
| 760    | No file  | `1c79d45515ee`  |
| 748    | No file  | `1c79d45515ee`  |
| 741    | No file  | `1c79d45515ee`  |
| 736    | No file  | `1c79d45515ee`  |
| 731    | No file  | `1c79d45515ee`  |
| 723    | No file  | `1c79d45515ee`  |
| 711    | No file  | `1c79d45515ee`  |
| 707    | No file  | `1c79d45515ee`  |
| 697    | No file  | `1c79d45515ee`  |
| 689    | No file  | `1c79d45515ee`  |
| 683    | No file  | `1c79d45515ee`  |
| 678    | No file  | `1c79d45515ee`  |
| 670    | No file  | `1c79d45515ee`  |
| 661    | No file  | `1c79d45515ee`  |
| 656    | No file  | `1c79d45515ee`  |
| 652    | No file  | `1c79d45515ee`  |
| 643    | No file  | `1c79d45515ee`  |
| 637    | No file  | `1c79d45515ee`  |
| 630    | No file  | `1c79d45515ee`  |
| 627    | No file  | `1c79d45515ee`  |
| 621    | No file  | `1c79d45515ee`  |
| 617    | No file  | `1c79d45515ee`  |
| 615    | No file  | `1c79d45515ee`  |
| 606    | No file  | `1c79d45515ee`  |
| 599    | No file  | `1c79d45515ee`  |
| 592    | No file  | `1c79d45515ee`  |
| 586    | No file  | `1c79d45515ee`  |
| 577    | No file  | `1c79d45515ee`  |
| 569    | No file  | `1c79d45515ee`  |
| 561    | No file  | `1c79d45515ee`  |
| 554    | No file  | `1c79d45515ee`  |
| 542    | No file  | `1c79d45515ee`  |
| 532    | No file  | `1c79d45515ee`  |
| 531    | No file  | `1c79d45515ee`  |
| 526    | No file  | `1c79d45515ee`  |
| 521    | No file  | `1c79d45515ee`  |
| 517    | No file  | `1c79d45515ee`  |
| 510    | No file  | `1c79d45515ee`  |
| 508    | No file  | `1c79d45515ee`  |
| 504    | No file  | `1c79d45515ee`  |
| 497    | No file  | `1c79d45515ee`  |
| 491    | No file  | `1c79d45515ee`  |
| 485    | No file  | `1c79d45515ee`  |
| 478    | No file  | `1c79d45515ee`  |
| 472    | No file  | `1c79d45515ee`  |
| 466    | No file  | `1c79d45515ee`  |
| 457    | No file  | `1c79d45515ee`  |
| 452    | No file  | `1c79d45515ee`  |
| 449    | No file  | `1c79d45515ee`  |
| 435    | No file  | `1c79d45515ee`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type               | Field        | Notes                                           |
| ------------------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                    |
| `+0x04`             | u32                | group_count  | Number of groups                                |
| `+0x08`             | Group[group_count] | groups       | See Group; byte-packed                          |
| `groups+0x00`       | String Table       | string_table | See String Table                                |
| `string_table+0x00` | u32                | table_start  | Offset of the string table, where `groups` ends |
| `string_table+0x04` | u32                | zero         | Always `0`                                      |

### Group (variable: 10 bytes + rights)

| Offset  | Type               | Field          | Notes                                                        |
| ------- | ------------------ | -------------- | ------------------------------------------------------------ |
| `+0x00` | u8                 | group_no       | Group number, `1` to `group_count` in file order; `getGroupNo()` |
| `+0x01` | u8                 | unknown_01     | Equal to `group_no` on every group (clients 3002 to 3474)     |
| `+0x02` | u32                | group_name_ref | String-table index of the Korean group name; `getGroupName()` |
| `+0x06` | u32                | right_count    | Number of rights; `getRightCount()`                          |
| `+0x0A` | Right[right_count] | rights         | See Right                                                    |

### Right (12 bytes)

| Offset  | Type | Field           | Notes                                                              |
| ------- | ---- | --------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | right_no        | `__eGuildRightNew_*` value; `getRightNo()`; unique over the file    |
| `+0x04` | u32  | name_ref        | String-table index of the Korean right name; `getRightName()`      |
| `+0x08` | u32  | description_ref | String-table index of the Korean description; `getRightDesc()`     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                    |
| ------- | ------------------ | ------------ | ------------------------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings, one per group name and two per right; 82 on client 3474 |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE Korean text in file order: each group's name, then each right's name and description |

## Field Names

The guild authority window of client 3474
(`panel_guild_authorization_all_1.luac`) walks the file with
`ToClient_getGuildRightGroupCount()` and
`ToClient_GetGuildRightNewStaticStatus(ii)`, then reads `getGroupNo()`,
`getGroupName()` and `getRightCount()` per group and `getRightNo()`,
`getRightName()` and `getRightDesc()` per right; the fields take those
names. The rights it checks by name are `__eGuildRightNew_*` (29 names in
the Lua, such as `__eGuildRightNew_ChangeMemberRight`), compared with
`getRightNo()`. The Guild Authority window is newer than client 1784 and
2519, which do not ship the file, so no sheet of a private server's
`DataSheets.bexcel` covers it.

## Notes

- Clients 3002 and 3251 have 38 rights: right `20` (길드 보호 인원 설정,
  the guild's protected members) sits in group 3, and rights `40` (길드
  전략 가이드) and `41` (길드 명성 소모) are not there yet. Client 3474
  drops `20` and adds the other two.
- No LOC type holds the right names in English, so the handler shows the
  Korean text.
- The handler (`_bss/guildrightnewstaticstatus/`) shows one row per right,
  sorted by right number, with its group number and name and its
  description.

## Open Questions

### Right Number Names

The Lua names 29 `__eGuildRightNew_*` rights without their values, and the
file's Korean names fit many of them (`1` 가입/재계약 and `Join`, `36` 추방
and `Expel`), but no source ties a value to a name.

### Localised Texts

Whether an English client shows these Korean texts or other text; the
English LOC has no row with the right names, and the window fills its
list only when `_ContentsGroup_GuildAuthoritySeparation` is on
(`setData()`).
