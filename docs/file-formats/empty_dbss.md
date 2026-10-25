# Empty DBSS Tables Format

## Purpose

DBSS tables the client ships with no records. Each file below is a u32 count
of `0` and nothing else, on every client checked (1784 and 3473):

| Main file               | Offset companion              |
| ----------------------- | ----------------------------- |
| `alchemystatus.dbss`    | `alchemystatusoffset.dbss`    |
| `buffcondition.dbss`    | `buffconditionoffset.dbss`    |
| `cashforui.dbss`        | `cashforuioffset.dbss`        |
| `chinaspawnoption.dbss` | `chinaspawnoptionoffset.dbss` |
| `grenadedata.dbss`      | `grenadedataoffset.dbss`      |
| `installation.dbss`     | `installationoffset.dbss`     |
| `petmarketsetting.dbss` | `petmarketsettingoffset.dbss` |
| `petset.dbss`           | `petsetoffset.dbss`           |
| `servantcategory.dbss`  | `servantcategoryoffset.dbss`  |
| `worldquest.dbss`       | none in the archive           |

`itemcouponreward.dbss` also declares zero records but has 12 bytes after the
count; see [itemcouponreward](itemcouponreward_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes | Records | Row bytes |
| ------ | -------------- | ----------------------------- | ----- | ------- | --------- |
| 1      | 1256 and later | `alchemystatus.dbss`          | 4     | -       | -         |
| 1      | 1256 and later | `alchemystatusoffset.dbss`    | 4     | -       | -         |
| 1      | 1239 and later | `buffcondition.dbss`          | 4     | -       | -         |
| 1      | 1239 and later | `buffconditionoffset.dbss`    | 4     | -       | -         |
| 1      | 1286 and later | `cashforui.dbss`              | 4     | -       | -         |
| 1      | 1286 and later | `cashforuioffset.dbss`        | 4     | -       | -         |
| 1      | 1346 and later | `chinaspawnoption.dbss`       | 4     | -       | -         |
| 1      | 1346 and later | `chinaspawnoptionoffset.dbss` | 4     | -       | -         |
| 1      | 1267 and later | `grenadedata.dbss`            | 4     | -       | -         |
| 1      | 1267 and later | `grenadedataoffset.dbss`      | 4     | -       | -         |
| 1      | 1267 and later | `installation.dbss`           | 4     | -       | -         |
| 1      | 1267 and later | `installationoffset.dbss`     | 4     | -       | -         |
| 1      | 1261 and later | `petmarketsetting.dbss`       | 4     | -       | -         |
| 1      | 1261 and later | `petmarketsettingoffset.dbss` | 4     | -       | -         |
| 1      | 1313 and later | `petset.dbss`                 | 4     | -       | -         |
| 1      | 1313 and later | `petsetoffset.dbss`           | 4     | -       | -         |
| 1      | 1774 and later | `servantcategory.dbss`        | 4     | -       | -         |
| 1      | 1774 and later | `servantcategoryoffset.dbss`  | 4     | -       | -         |
| 1      | 1774 and later | `worldquest.dbss`             | 4     | -       | -         |

| Layout | File                          | Known        | Unknown    |
| ------ | ----------------------------- | ------------ | ---------- |
| 1      | `alchemystatus.dbss`          | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `alchemystatusoffset.dbss`    | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `buffcondition.dbss`          | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `buffconditionoffset.dbss`    | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `cashforui.dbss`              | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `cashforuioffset.dbss`        | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `chinaspawnoption.dbss`       | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `chinaspawnoptionoffset.dbss` | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `grenadedata.dbss`            | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `grenadedataoffset.dbss`      | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `installation.dbss`           | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `installationoffset.dbss`     | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `petmarketsetting.dbss`       | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `petmarketsettingoffset.dbss` | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `petset.dbss`                 | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `petsetoffset.dbss`           | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `servantcategory.dbss`        | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `servantcategoryoffset.dbss`  | 4 B (100.0%) | 0 B (0.0%) |
| 1      | `worldquest.dbss`             | 4 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `43d82b22b58b`  |
| 3482   | Layout 1             | `43d82b22b58b`  |
| 3474   | Layout 1             | `43d82b22b58b`  |
| 3473   | Layout 1             | `43d82b22b58b`  |
| 3464   | Layout 1             | `43d82b22b58b`  |
| 3458   | Layout 1             | `43d82b22b58b`  |
| 3454   | Layout 1             | `43d82b22b58b`  |
| 3444   | Layout 1             | `43d82b22b58b`  |
| 3435   | Layout 1             | `43d82b22b58b`  |
| 3426   | Layout 1             | `43d82b22b58b`  |
| 3418   | Layout 1             | `43d82b22b58b`  |
| 3412   | Layout 1             | `43d82b22b58b`  |
| 3402   | Layout 1             | `43d82b22b58b`  |
| 3396   | Layout 1             | `43d82b22b58b`  |
| 3387   | Layout 1             | `43d82b22b58b`  |
| 3381   | Layout 1             | `43d82b22b58b`  |
| 3373   | Layout 1             | `43d82b22b58b`  |
| 3364   | Layout 1             | `43d82b22b58b`  |
| 3356   | Layout 1             | `43d82b22b58b`  |
| 3349   | Layout 1             | `43d82b22b58b`  |
| 3342   | Layout 1             | `43d82b22b58b`  |
| 3335   | Layout 1             | `43d82b22b58b`  |
| 3326   | Layout 1             | `43d82b22b58b`  |
| 3321   | Layout 1             | `43d82b22b58b`  |
| 3314   | Layout 1             | `43d82b22b58b`  |
| 3303   | Layout 1             | `43d82b22b58b`  |
| 3302   | Layout 1             | `43d82b22b58b`  |
| 3293   | Layout 1             | `43d82b22b58b`  |
| 3283   | Layout 1             | `43d82b22b58b`  |
| 3275   | Layout 1             | `43d82b22b58b`  |
| 3267   | Layout 1             | `43d82b22b58b`  |
| 3258   | Layout 1             | `43d82b22b58b`  |
| 3251   | Layout 1             | `43d82b22b58b`  |
| 3242   | Layout 1             | `43d82b22b58b`  |
| 3235   | Layout 1             | `43d82b22b58b`  |
| 3229   | Layout 1             | `43d82b22b58b`  |
| 3212   | Layout 1             | `43d82b22b58b`  |
| 3203   | Layout 1             | `43d82b22b58b`  |
| 3193   | Layout 1             | `43d82b22b58b`  |
| 3186   | Layout 1             | `43d82b22b58b`  |
| 3177   | Layout 1             | `43d82b22b58b`  |
| 3169   | Layout 1             | `43d82b22b58b`  |
| 3158   | Layout 1             | `43d82b22b58b`  |
| 3151   | Layout 1             | `43d82b22b58b`  |
| 3144   | Layout 1             | `43d82b22b58b`  |
| 3133   | Layout 1             | `43d82b22b58b`  |
| 3125   | Layout 1             | `43d82b22b58b`  |
| 3118   | Layout 1             | `43d82b22b58b`  |
| 3111   | Layout 1             | `43d82b22b58b`  |
| 3103   | Layout 1             | `43d82b22b58b`  |
| 3095   | Layout 1             | `43d82b22b58b`  |
| 3086   | Layout 1             | `43d82b22b58b`  |
| 3072   | Layout 1             | `43d82b22b58b`  |
| 3062   | Layout 1             | `43d82b22b58b`  |
| 3052   | Layout 1             | `43d82b22b58b`  |
| 3045   | Layout 1             | `43d82b22b58b`  |
| 3037   | Layout 1             | `43d82b22b58b`  |
| 3030   | Layout 1             | `43d82b22b58b`  |
| 3021   | Layout 1             | `43d82b22b58b`  |
| 3012   | Layout 1             | `43d82b22b58b`  |
| 3002   | Layout 1             | `43d82b22b58b`  |
| 2995   | Layout 1             | `43d82b22b58b`  |
| 2987   | Layout 1             | `43d82b22b58b`  |
| 2978   | Layout 1             | `43d82b22b58b`  |
| 2970   | Layout 1             | `43d82b22b58b`  |
| 2959   | Layout 1             | `43d82b22b58b`  |
| 2951   | Layout 1             | `43d82b22b58b`  |
| 2942   | Layout 1             | `43d82b22b58b`  |
| 2935   | Layout 1             | `43d82b22b58b`  |
| 2932   | Layout 1             | `43d82b22b58b`  |
| 2923   | Layout 1             | `43d82b22b58b`  |
| 2919   | Layout 1             | `43d82b22b58b`  |
| 2907   | Layout 1             | `43d82b22b58b`  |
| 2900   | Layout 1             | `43d82b22b58b`  |
| 2891   | Layout 1             | `43d82b22b58b`  |
| 2882   | Layout 1             | `43d82b22b58b`  |
| 2872   | Layout 1             | `43d82b22b58b`  |
| 2863   | Layout 1             | `43d82b22b58b`  |
| 2855   | Layout 1             | `43d82b22b58b`  |
| 2849   | Layout 1             | `43d82b22b58b`  |
| 2844   | Layout 1             | `43d82b22b58b`  |
| 2834   | Layout 1             | `43d82b22b58b`  |
| 2825   | Layout 1             | `43d82b22b58b`  |
| 2819   | Layout 1             | `43d82b22b58b`  |
| 2811   | Layout 1             | `43d82b22b58b`  |
| 2803   | Layout 1             | `43d82b22b58b`  |
| 2794   | Layout 1             | `43d82b22b58b`  |
| 2783   | Layout 1             | `43d82b22b58b`  |
| 2774   | Layout 1             | `43d82b22b58b`  |
| 2765   | Layout 1             | `43d82b22b58b`  |
| 2756   | Layout 1             | `43d82b22b58b`  |
| 2750   | Layout 1             | `43d82b22b58b`  |
| 2743   | Layout 1             | `43d82b22b58b`  |
| 2736   | Layout 1             | `43d82b22b58b`  |
| 2726   | Layout 1             | `43d82b22b58b`  |
| 2717   | Layout 1             | `43d82b22b58b`  |
| 2709   | Layout 1             | `43d82b22b58b`  |
| 2703   | Layout 1             | `43d82b22b58b`  |
| 2695   | Layout 1             | `43d82b22b58b`  |
| 2684   | Layout 1             | `43d82b22b58b`  |
| 2672   | Layout 1             | `43d82b22b58b`  |
| 2665   | Layout 1             | `43d82b22b58b`  |
| 2657   | Layout 1             | `43d82b22b58b`  |
| 2649   | Layout 1             | `43d82b22b58b`  |
| 2644   | Layout 1             | `43d82b22b58b`  |
| 2637   | Layout 1             | `43d82b22b58b`  |
| 2629   | Layout 1             | `43d82b22b58b`  |
| 2619   | Layout 1             | `43d82b22b58b`  |
| 2612   | Layout 1             | `43d82b22b58b`  |
| 2606   | Layout 1             | `43d82b22b58b`  |
| 2602   | Layout 1             | `43d82b22b58b`  |
| 2601   | Layout 1             | `43d82b22b58b`  |
| 2592   | Layout 1             | `43d82b22b58b`  |
| 2583   | Layout 1             | `43d82b22b58b`  |
| 2575   | Layout 1             | `43d82b22b58b`  |
| 2567   | Layout 1             | `43d82b22b58b`  |
| 2560   | Layout 1             | `43d82b22b58b`  |
| 2553   | Layout 1             | `43d82b22b58b`  |
| 2545   | Layout 1             | `43d82b22b58b`  |
| 2538   | Layout 1             | `43d82b22b58b`  |
| 2529   | Layout 1             | `43d82b22b58b`  |
| 2519   | Layout 1             | `43d82b22b58b`  |
| 2513   | Layout 1             | `43d82b22b58b`  |
| 2510   | Layout 1             | `43d82b22b58b`  |
| 2507   | Layout 1             | `43d82b22b58b`  |
| 2503   | Layout 1             | `43d82b22b58b`  |
| 2498   | Layout 1             | `43d82b22b58b`  |
| 2492   | Layout 1             | `43d82b22b58b`  |
| 2487   | Layout 1             | `43d82b22b58b`  |
| 2480   | Layout 1             | `43d82b22b58b`  |
| 2474   | Layout 1             | `43d82b22b58b`  |
| 2468   | Layout 1             | `43d82b22b58b`  |
| 2460   | Layout 1             | `43d82b22b58b`  |
| 2453   | Layout 1             | `43d82b22b58b`  |
| 2444   | Layout 1             | `43d82b22b58b`  |
| 2438   | Layout 1             | `43d82b22b58b`  |
| 2434   | Layout 1             | `43d82b22b58b`  |
| 2429   | Layout 1             | `43d82b22b58b`  |
| 2421   | Layout 1             | `43d82b22b58b`  |
| 2414   | Layout 1             | `43d82b22b58b`  |
| 2407   | Layout 1             | `43d82b22b58b`  |
| 2401   | Layout 1             | `43d82b22b58b`  |
| 2397   | Layout 1             | `43d82b22b58b`  |
| 2393   | Layout 1             | `43d82b22b58b`  |
| 2384   | Layout 1             | `43d82b22b58b`  |
| 2378   | Layout 1             | `43d82b22b58b`  |
| 2372   | Layout 1             | `43d82b22b58b`  |
| 2358   | Layout 1             | `43d82b22b58b`  |
| 2352   | Layout 1             | `43d82b22b58b`  |
| 2347   | Layout 1             | `43d82b22b58b`  |
| 2343   | Layout 1             | `43d82b22b58b`  |
| 2335   | Layout 1             | `43d82b22b58b`  |
| 2327   | Layout 1             | `43d82b22b58b`  |
| 2324   | Layout 1             | `43d82b22b58b`  |
| 2319   | Layout 1             | `43d82b22b58b`  |
| 2313   | Layout 1             | `43d82b22b58b`  |
| 2308   | Layout 1             | `43d82b22b58b`  |
| 2302   | Layout 1             | `43d82b22b58b`  |
| 2295   | Layout 1             | `43d82b22b58b`  |
| 2290   | Layout 1             | `43d82b22b58b`  |
| 2284   | Layout 1             | `43d82b22b58b`  |
| 2276   | Layout 1             | `43d82b22b58b`  |
| 2269   | Layout 1             | `43d82b22b58b`  |
| 2259   | Layout 1             | `43d82b22b58b`  |
| 2250   | Layout 1             | `43d82b22b58b`  |
| 2243   | Layout 1             | `43d82b22b58b`  |
| 2235   | Layout 1             | `43d82b22b58b`  |
| 2229   | Layout 1             | `43d82b22b58b`  |
| 2224   | Layout 1             | `43d82b22b58b`  |
| 2218   | Layout 1             | `43d82b22b58b`  |
| 2215   | Layout 1             | `43d82b22b58b`  |
| 2207   | Layout 1             | `43d82b22b58b`  |
| 2203   | Layout 1             | `43d82b22b58b`  |
| 2196   | Layout 1             | `43d82b22b58b`  |
| 2192   | Layout 1             | `43d82b22b58b`  |
| 2189   | Layout 1             | `43d82b22b58b`  |
| 2183   | Layout 1             | `43d82b22b58b`  |
| 2179   | Layout 1             | `43d82b22b58b`  |
| 2171   | Layout 1             | `43d82b22b58b`  |
| 2163   | Layout 1             | `43d82b22b58b`  |
| 2156   | Layout 1             | `43d82b22b58b`  |
| 2151   | Layout 1             | `43d82b22b58b`  |
| 2147   | Layout 1             | `43d82b22b58b`  |
| 2142   | Layout 1             | `43d82b22b58b`  |
| 2138   | Layout 1             | `43d82b22b58b`  |
| 2134   | Layout 1             | `43d82b22b58b`  |
| 2130   | Layout 1             | `43d82b22b58b`  |
| 2122   | Layout 1             | `43d82b22b58b`  |
| 2107   | Layout 1             | `43d82b22b58b`  |
| 2098   | Layout 1             | `43d82b22b58b`  |
| 2089   | Layout 1             | `43d82b22b58b`  |
| 2081   | Layout 1             | `43d82b22b58b`  |
| 2073   | Layout 1             | `43d82b22b58b`  |
| 2067   | Layout 1             | `43d82b22b58b`  |
| 2063   | Layout 1             | `43d82b22b58b`  |
| 2059   | Layout 1             | `43d82b22b58b`  |
| 2052   | Layout 1             | `43d82b22b58b`  |
| 2044   | Layout 1             | `43d82b22b58b`  |
| 2039   | Layout 1             | `43d82b22b58b`  |
| 2032   | Layout 1             | `43d82b22b58b`  |
| 2025   | Layout 1             | `43d82b22b58b`  |
| 2011   | Layout 1             | `43d82b22b58b`  |
| 2005   | Layout 1             | `43d82b22b58b`  |
| 2000   | Layout 1             | `43d82b22b58b`  |
| 1996   | Layout 1             | `43d82b22b58b`  |
| 1991   | Layout 1             | `43d82b22b58b`  |
| 1985   | Layout 1             | `43d82b22b58b`  |
| 1980   | Layout 1             | `43d82b22b58b`  |
| 1969   | Layout 1             | `43d82b22b58b`  |
| 1964   | Layout 1             | `43d82b22b58b`  |
| 1958   | Layout 1             | `43d82b22b58b`  |
| 1950   | Layout 1             | `43d82b22b58b`  |
| 1945   | Layout 1             | `43d82b22b58b`  |
| 1937   | Layout 1             | `43d82b22b58b`  |
| 1933   | Layout 1             | `43d82b22b58b`  |
| 1927   | Layout 1             | `43d82b22b58b`  |
| 1921   | Layout 1             | `43d82b22b58b`  |
| 1914   | Layout 1             | `43d82b22b58b`  |
| 1908   | Layout 1             | `43d82b22b58b`  |
| 1897   | Layout 1             | `43d82b22b58b`  |
| 1892   | Layout 1             | `43d82b22b58b`  |
| 1886   | Layout 1             | `43d82b22b58b`  |
| 1881   | Layout 1             | `43d82b22b58b`  |
| 1871   | Layout 1             | `43d82b22b58b`  |
| 1866   | Layout 1             | `43d82b22b58b`  |
| 1862   | Layout 1             | `43d82b22b58b`  |
| 1854   | Layout 1             | `43d82b22b58b`  |
| 1846   | Layout 1             | `43d82b22b58b`  |
| 1838   | Layout 1             | `43d82b22b58b`  |
| 1832   | Layout 1             | `43d82b22b58b`  |
| 1826   | Layout 1             | `43d82b22b58b`  |
| 1822   | Layout 1             | `43d82b22b58b`  |
| 1818   | Layout 1             | `43d82b22b58b`  |
| 1804   | Layout 1             | `43d82b22b58b`  |
| 1794   | Layout 1             | `43d82b22b58b`  |
| 1790   | Layout 1             | `43d82b22b58b`  |
| 1784   | Layout 1             | `43d82b22b58b`  |
| 1774   | Layout 1             | `43d82b22b58b`  |
| 1771   | No documented layout | `43d82b22b58b`  |
| 1762   | No documented layout | `43d82b22b58b`  |
| 1759   | No documented layout | `43d82b22b58b`  |
| 1754   | No documented layout | `43d82b22b58b`  |
| 1749   | No documented layout | `43d82b22b58b`  |
| 1743   | No documented layout | `43d82b22b58b`  |
| 1737   | No documented layout | `43d82b22b58b`  |
| 1731   | No documented layout | `43d82b22b58b`  |
| 1725   | No documented layout | `43d82b22b58b`  |
| 1717   | No documented layout | `43d82b22b58b`  |
| 1710   | No documented layout | `43d82b22b58b`  |
| 1704   | No documented layout | `43d82b22b58b`  |
| 1698   | No documented layout | `43d82b22b58b`  |
| 1690   | No documented layout | `43d82b22b58b`  |
| 1685   | No documented layout | `43d82b22b58b`  |
| 1680   | No documented layout | `43d82b22b58b`  |
| 1674   | No documented layout | `43d82b22b58b`  |
| 1668   | No documented layout | `43d82b22b58b`  |
| 1659   | No documented layout | `43d82b22b58b`  |
| 1649   | No documented layout | `43d82b22b58b`  |
| 1642   | No documented layout | `43d82b22b58b`  |
| 1636   | No documented layout | `43d82b22b58b`  |
| 1628   | No documented layout | `43d82b22b58b`  |
| 1622   | No documented layout | `43d82b22b58b`  |
| 1614   | No documented layout | `43d82b22b58b`  |
| 1608   | No documented layout | `43d82b22b58b`  |
| 1602   | No documented layout | `43d82b22b58b`  |
| 1598   | No documented layout | `43d82b22b58b`  |
| 1594   | No documented layout | `43d82b22b58b`  |
| 1590   | No documented layout | `43d82b22b58b`  |
| 1587   | No documented layout | `43d82b22b58b`  |
| 1584   | No documented layout | `43d82b22b58b`  |
| 1579   | No documented layout | `43d82b22b58b`  |
| 1572   | No documented layout | `43d82b22b58b`  |
| 1565   | No documented layout | `43d82b22b58b`  |
| 1559   | No documented layout | `43d82b22b58b`  |
| 1554   | No documented layout | `43d82b22b58b`  |
| 1547   | No documented layout | `43d82b22b58b`  |
| 1537   | No documented layout | `43d82b22b58b`  |
| 1529   | No documented layout | `43d82b22b58b`  |
| 1524   | No documented layout | `43d82b22b58b`  |
| 1519   | No documented layout | `43d82b22b58b`  |
| 1509   | No documented layout | `43d82b22b58b`  |
| 1506   | No documented layout | `43d82b22b58b`  |
| 1504   | No documented layout | `43d82b22b58b`  |
| 1500   | No documented layout | `43d82b22b58b`  |
| 1493   | No documented layout | `43d82b22b58b`  |
| 1489   | No documented layout | `43d82b22b58b`  |
| 1485   | No documented layout | `43d82b22b58b`  |
| 1481   | No documented layout | `43d82b22b58b`  |
| 1474   | No documented layout | `43d82b22b58b`  |
| 1466   | No documented layout | `43d82b22b58b`  |
| 1462   | No documented layout | `43d82b22b58b`  |
| 1459   | No documented layout | `43d82b22b58b`  |
| 1453   | No documented layout | `43d82b22b58b`  |
| 1450   | No documented layout | `43d82b22b58b`  |
| 1445   | No documented layout | `43d82b22b58b`  |
| 1439   | No documented layout | `43d82b22b58b`  |
| 1433   | No documented layout | `43d82b22b58b`  |
| 1430   | No documented layout | `43d82b22b58b`  |
| 1426   | No documented layout | `43d82b22b58b`  |
| 1421   | No documented layout | `43d82b22b58b`  |
| 1417   | No documented layout | `43d82b22b58b`  |
| 1416   | No documented layout | `43d82b22b58b`  |
| 1409   | No documented layout | `43d82b22b58b`  |
| 1405   | No documented layout | `43d82b22b58b`  |
| 1401   | No documented layout | `43d82b22b58b`  |
| 1396   | No documented layout | `43d82b22b58b`  |
| 1391   | No documented layout | `43d82b22b58b`  |
| 1390   | No documented layout | `43d82b22b58b`  |
| 1386   | No documented layout | `43d82b22b58b`  |
| 1381   | No documented layout | `43d82b22b58b`  |
| 1379   | No documented layout | `43d82b22b58b`  |
| 1372   | No documented layout | `43d82b22b58b`  |
| 1366   | No documented layout | `43d82b22b58b`  |
| 1364   | No documented layout | `43d82b22b58b`  |
| 1363   | No documented layout | `43d82b22b58b`  |
| 1360   | No documented layout | `43d82b22b58b`  |
| 1358   | No documented layout | `43d82b22b58b`  |
| 1355   | No documented layout | `43d82b22b58b`  |
| 1351   | No documented layout | `43d82b22b58b`  |
| 1348   | Layout 1             | `43d82b22b58b`  |
| 1346   | Layout 1             | `43d82b22b58b`  |
| 1341   | Layout 1             | `43d82b22b58b`  |
| 1340   | Layout 1             | `43d82b22b58b`  |
| 1338   | Layout 1             | `43d82b22b58b`  |
| 1335   | Layout 1             | `43d82b22b58b`  |
| 1333   | Layout 1             | `43d82b22b58b`  |
| 1329   | Layout 1             | `43d82b22b58b`  |
| 1327   | Layout 1             | `43d82b22b58b`  |
| 1324   | Layout 1             | `43d82b22b58b`  |
| 1321   | Layout 1             | `43d82b22b58b`  |
| 1319   | Layout 1             | `43d82b22b58b`  |
| 1318   | Layout 1             | `43d82b22b58b`  |
| 1316   | Layout 1             | `43d82b22b58b`  |
| 1313   | Layout 1             | `43d82b22b58b`  |
| 1311   | Layout 1             | `43d82b22b58b`  |
| 1309   | Layout 1             | `43d82b22b58b`  |
| 1304   | Layout 1             | `43d82b22b58b`  |
| 1292   | Layout 1             | `43d82b22b58b`  |
| 1286   | Layout 1             | `43d82b22b58b`  |
| 1280   | Layout 1             | `43d82b22b58b`  |
| 1276   | Layout 1             | `43d82b22b58b`  |
| 1267   | Layout 1             | `43d82b22b58b`  |
| 1261   | Layout 1             | `43d82b22b58b`  |
| 1256   | Layout 1             | `43d82b22b58b`  |
| 1250   | Layout 1             | `43d82b22b58b`  |
| 1246   | Layout 1             | `43d82b22b58b`  |
| 1239   | Layout 1             | `43d82b22b58b`  |
| 1230   | No file              | `43d82b22b58b`  |
| 1226   | No file              | `43d82b22b58b`  |
| 1220   | No file              | `43d82b22b58b`  |
| 1217   | No file              | `43d82b22b58b`  |
| 1211   | No file              | `43d82b22b58b`  |
| 1210   | No file              | `43d82b22b58b`  |
| 1208   | No file              | `43d82b22b58b`  |
| 1203   | No file              | `43d82b22b58b`  |
| 1197   | No file              | `43d82b22b58b`  |
| 1194   | No file              | `43d82b22b58b`  |
| 1192   | No file              | `43d82b22b58b`  |
| 1187   | No file              | `43d82b22b58b`  |
| 1183   | No file              | `43d82b22b58b`  |
| 1177   | No file              | `43d82b22b58b`  |
| 1173   | No file              | `43d82b22b58b`  |
| 1167   | No file              | `43d82b22b58b`  |
| 1164   | No file              | `43d82b22b58b`  |
| 1156   | No file              | `43d82b22b58b`  |
| 1149   | No file              | `43d82b22b58b`  |
| 1144   | No file              | `43d82b22b58b`  |
| 1137   | No file              | `43d82b22b58b`  |
| 1132   | No file              | `43d82b22b58b`  |
| 1127   | No file              | `43d82b22b58b`  |
| 1122   | No file              | `43d82b22b58b`  |
| 1118   | No file              | `43d82b22b58b`  |
| 1114   | No file              | `43d82b22b58b`  |
| 1109   | No file              | `43d82b22b58b`  |
| 1102   | No file              | `43d82b22b58b`  |
| 1096   | No file              | `43d82b22b58b`  |
| 1088   | No file              | `43d82b22b58b`  |
| 1081   | No file              | `43d82b22b58b`  |
| 1076   | No file              | `43d82b22b58b`  |
| 1069   | No file              | `43d82b22b58b`  |
| 1064   | No file              | `43d82b22b58b`  |
| 1058   | No file              | `43d82b22b58b`  |
| 1051   | No file              | `43d82b22b58b`  |
| 1044   | No file              | `43d82b22b58b`  |
| 1036   | No file              | `43d82b22b58b`  |
| 1026   | No file              | `43d82b22b58b`  |
| 1016   | No file              | `43d82b22b58b`  |
| 1009   | No file              | `43d82b22b58b`  |
| 1005   | No file              | `43d82b22b58b`  |
| 1000   | No file              | `43d82b22b58b`  |
| 998    | No file              | `43d82b22b58b`  |
| 990    | No file              | `43d82b22b58b`  |
| 979    | No file              | `43d82b22b58b`  |
| 972    | No file              | `43d82b22b58b`  |
| 963    | No file              | `43d82b22b58b`  |
| 955    | No file              | `43d82b22b58b`  |
| 946    | No file              | `43d82b22b58b`  |
| 938    | No file              | `43d82b22b58b`  |
| 927    | No file              | `43d82b22b58b`  |
| 911    | No file              | `43d82b22b58b`  |
| 904    | No file              | `43d82b22b58b`  |
| 899    | No file              | `43d82b22b58b`  |
| 894    | No file              | `43d82b22b58b`  |
| 885    | No file              | `43d82b22b58b`  |
| 879    | No file              | `43d82b22b58b`  |
| 872    | No file              | `43d82b22b58b`  |
| 864    | No file              | `43d82b22b58b`  |
| 855    | No file              | `43d82b22b58b`  |
| 853    | No file              | `43d82b22b58b`  |
| 845    | No file              | `43d82b22b58b`  |
| 837    | No file              | `43d82b22b58b`  |
| 829    | No file              | `43d82b22b58b`  |
| 822    | No file              | `43d82b22b58b`  |
| 814    | No file              | `43d82b22b58b`  |
| 805    | No file              | `43d82b22b58b`  |
| 794    | No file              | `43d82b22b58b`  |
| 787    | No file              | `43d82b22b58b`  |
| 780    | No file              | `43d82b22b58b`  |
| 771    | No file              | `43d82b22b58b`  |
| 760    | No file              | `43d82b22b58b`  |
| 748    | No file              | `43d82b22b58b`  |
| 741    | No file              | `43d82b22b58b`  |
| 736    | No file              | `43d82b22b58b`  |
| 731    | No file              | `43d82b22b58b`  |
| 723    | No file              | `43d82b22b58b`  |
| 711    | No file              | `43d82b22b58b`  |
| 707    | No file              | `43d82b22b58b`  |
| 697    | No file              | `43d82b22b58b`  |
| 689    | No file              | `43d82b22b58b`  |
| 683    | No file              | `43d82b22b58b`  |
| 678    | No file              | `43d82b22b58b`  |
| 670    | No file              | `43d82b22b58b`  |
| 661    | No file              | `43d82b22b58b`  |
| 656    | No file              | `43d82b22b58b`  |
| 652    | No file              | `43d82b22b58b`  |
| 643    | No file              | `43d82b22b58b`  |
| 637    | No file              | `43d82b22b58b`  |
| 630    | No file              | `43d82b22b58b`  |
| 627    | No file              | `43d82b22b58b`  |
| 621    | No file              | `43d82b22b58b`  |
| 617    | No file              | `43d82b22b58b`  |
| 615    | No file              | `43d82b22b58b`  |
| 606    | No file              | `43d82b22b58b`  |
| 599    | No file              | `43d82b22b58b`  |
| 592    | No file              | `43d82b22b58b`  |
| 586    | No file              | `43d82b22b58b`  |
| 577    | No file              | `43d82b22b58b`  |
| 569    | No file              | `43d82b22b58b`  |
| 561    | No file              | `43d82b22b58b`  |
| 554    | No file              | `43d82b22b58b`  |
| 542    | No file              | `43d82b22b58b`  |
| 532    | No file              | `43d82b22b58b`  |
| 531    | No file              | `43d82b22b58b`  |
| 526    | No file              | `43d82b22b58b`  |
| 521    | No file              | `43d82b22b58b`  |
| 517    | No file              | `43d82b22b58b`  |
| 510    | No file              | `43d82b22b58b`  |
| 508    | No file              | `43d82b22b58b`  |
| 504    | No file              | `43d82b22b58b`  |
| 497    | No file              | `43d82b22b58b`  |
| 491    | No file              | `43d82b22b58b`  |
| 485    | No file              | `43d82b22b58b`  |
| 478    | No file              | `43d82b22b58b`  |
| 472    | No file              | `43d82b22b58b`  |
| 466    | No file              | `43d82b22b58b`  |
| 457    | No file              | `43d82b22b58b`  |
| 452    | No file              | `43d82b22b58b`  |
| 449    | No file              | `43d82b22b58b`  |
| 435    | No file              | `43d82b22b58b`  |

<!-- versions:end -->

## Companion Files

None. Each offset companion in the table above is a file of its own with
the same layout as its main file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

Main files and offset companions share one layout. No record structure can
be inferred because the files hold no records.

| Offset  | Type | Field | Notes                                  |
| ------- | ---- | ----- | -------------------------------------- |
| `+0x00` | u32  | count | Number of records; `0` in every file   |

## Notes

- Raw bytes of every file: `00 00 00 00`.
- The list comes from a scan of every file under `gamecommondata/binary/` for
  files of at most 8 bytes that are all zero.
- One handler class (`EmptyTableHandler`, `_common/empty_table.py`) previews
  every file in `_dbss/empty_tables/tables.py`. A file whose count is not `0`
  raises an error, so a client that fills one of these tables shows up as a
  parse error and in the tests.
- `worldquest.dbss` had the same 4 bytes before the 2026-09-27 client update.
- `growthpasspointshop.dbss`, `instancedungeonskillstatic.dbss` and
  `itemtradegroupfromnpc.dbss` are a count of `0` on client 3473 but hold
  records on client 1784, so each has a doc and a handler of its own:
  [growthpasspointshop](growthpasspointshop_dbss.md),
  [instancedungeonskillstatic](instancedungeonskillstatic_dbss.md) and
  [itemtradegroupfromnpc](itemtradegroupfromnpc_dbss.md).

## Open Questions

### Non-Empty Layout

No file has a record on client 1784 or client 3473, so every record layout
is unknown. When a client ships `count > 0` for one of these tables, it
moves to its own doc and handler, with records starting at `+0x04`.
