# `oceansiegereviveposition.bss` Format

## Purpose

Where Blue Battlefield (ocean siege) players revive, per territory: each
row holds a territory key and groups of world positions, each position
with an f32 and a u8. On client 3482 Balenos and Calpheon each have a
group `0` of harbour positions and a group `1` of one position far out
at sea.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records                     | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | --------------------------- | --------- |
| 1      | 3125 and later | 3483    | `oceansiegereviveposition.bss` | 222   | 10 Position, 4 Group, 2 Row | 17        |

| Layout | File                           | Known         | Unknown      |
| ------ | ------------------------------ | ------------- | ------------ |
| 1      | `oceansiegereviveposition.bss` | 168 B (75.7%) | 54 B (24.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 1             |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3473   | Layout 1             |
| 3464   | Layout 1             |
| 3458   | Layout 1             |
| 3454   | Layout 1             |
| 3444   | Layout 1             |
| 3435   | Layout 1             |
| 3426   | Layout 1             |
| 3418   | Layout 1             |
| 3412   | Layout 1             |
| 3402   | Layout 1             |
| 3396   | Layout 1             |
| 3387   | Layout 1             |
| 3381   | Layout 1             |
| 3373   | Layout 1             |
| 3364   | Layout 1             |
| 3356   | Layout 1             |
| 3349   | Layout 1             |
| 3342   | Layout 1             |
| 3335   | Layout 1             |
| 3326   | Layout 1             |
| 3321   | Layout 1             |
| 3314   | Layout 1             |
| 3303   | Layout 1             |
| 3302   | Layout 1             |
| 3293   | Layout 1             |
| 3283   | Layout 1             |
| 3275   | Layout 1             |
| 3267   | Layout 1             |
| 3258   | Layout 1             |
| 3251   | Layout 1             |
| 3242   | Layout 1             |
| 3235   | Layout 1             |
| 3229   | Layout 1             |
| 3212   | Layout 1             |
| 3203   | Layout 1             |
| 3193   | Layout 1             |
| 3186   | Layout 1             |
| 3177   | Layout 1             |
| 3169   | Layout 1             |
| 3158   | Layout 1             |
| 3151   | Layout 1             |
| 3144   | Layout 1             |
| 3133   | Layout 1             |
| 3125   | Layout 1             |
| 3118   | No documented layout |
| 3111   | No documented layout |
| 3103   | No file              |
| 3095   | No file              |
| 3086   | No file              |
| 3072   | No file              |
| 3062   | No file              |
| 3052   | No file              |
| 3045   | No file              |
| 3037   | No file              |
| 3030   | No file              |
| 3021   | No file              |
| 3012   | No file              |
| 3002   | No file              |
| 2995   | No file              |
| 2987   | No file              |
| 2978   | No file              |
| 2970   | No file              |
| 2959   | No file              |
| 2951   | No file              |
| 2942   | No file              |
| 2935   | No file              |
| 2932   | No file              |
| 2923   | No file              |
| 2919   | No file              |
| 2907   | No file              |
| 2900   | No file              |
| 2891   | No file              |
| 2882   | No file              |
| 2872   | No file              |
| 2863   | No file              |
| 2855   | No file              |
| 2849   | No file              |
| 2844   | No file              |
| 2834   | No file              |
| 2825   | No file              |
| 2819   | No file              |
| 2811   | No file              |
| 2803   | No file              |
| 2794   | No file              |
| 2783   | No file              |
| 2774   | No file              |
| 2765   | No file              |
| 2756   | No file              |
| 2750   | No file              |
| 2743   | No file              |
| 2736   | No file              |
| 2726   | No file              |
| 2717   | No file              |
| 2709   | No file              |
| 2703   | No file              |
| 2695   | No file              |
| 2684   | No file              |
| 2672   | No file              |
| 2665   | No file              |
| 2657   | No file              |
| 2649   | No file              |
| 2644   | No file              |
| 2637   | No file              |
| 2629   | No file              |
| 2619   | No file              |
| 2612   | No file              |
| 2606   | No file              |
| 2602   | No file              |
| 2601   | No file              |
| 2592   | No file              |
| 2583   | No file              |
| 2575   | No file              |
| 2567   | No file              |
| 2560   | No file              |
| 2553   | No file              |
| 2545   | No file              |
| 2538   | No file              |
| 2529   | No file              |
| 2519   | No file              |
| 2513   | No file              |
| 2510   | No file              |
| 2507   | No file              |
| 2503   | No file              |
| 2498   | No file              |
| 2492   | No file              |
| 2487   | No file              |
| 2480   | No file              |
| 2474   | No file              |
| 2468   | No file              |
| 2460   | No file              |
| 2453   | No file              |
| 2444   | No file              |
| 2438   | No file              |
| 2434   | No file              |
| 2429   | No file              |
| 2421   | No file              |
| 2414   | No file              |
| 2407   | No file              |
| 2401   | No file              |
| 2397   | No file              |
| 2393   | No file              |
| 2384   | No file              |
| 2378   | No file              |
| 2372   | No file              |
| 2358   | No file              |
| 2352   | No file              |
| 2347   | No file              |
| 2343   | No file              |
| 2335   | No file              |
| 2327   | No file              |
| 2324   | No file              |
| 2319   | No file              |
| 2313   | No file              |
| 2308   | No file              |
| 2302   | No file              |
| 2295   | No file              |
| 2290   | No file              |
| 2284   | No file              |
| 2276   | No file              |
| 2269   | No file              |
| 2259   | No file              |
| 2250   | No file              |
| 2243   | No file              |
| 2235   | No file              |
| 2229   | No file              |
| 2224   | No file              |
| 2218   | No file              |
| 2215   | No file              |
| 2207   | No file              |
| 2203   | No file              |
| 2196   | No file              |
| 2192   | No file              |
| 2189   | No file              |
| 2183   | No file              |
| 2179   | No file              |
| 2171   | No file              |
| 2163   | No file              |
| 2156   | No file              |
| 2151   | No file              |
| 2147   | No file              |
| 2142   | No file              |
| 2138   | No file              |
| 2134   | No file              |
| 2130   | No file              |
| 2122   | No file              |
| 2107   | No file              |
| 2098   | No file              |
| 2089   | No file              |
| 2081   | No file              |
| 2073   | No file              |
| 2067   | No file              |
| 2063   | No file              |
| 2059   | No file              |
| 2052   | No file              |
| 2044   | No file              |
| 2039   | No file              |
| 2032   | No file              |
| 2025   | No file              |
| 2011   | No file              |
| 2005   | No file              |
| 2000   | No file              |
| 1996   | No file              |
| 1991   | No file              |
| 1985   | No file              |
| 1980   | No file              |
| 1969   | No file              |
| 1964   | No file              |
| 1958   | No file              |
| 1950   | No file              |
| 1945   | No file              |
| 1937   | No file              |
| 1933   | No file              |
| 1927   | No file              |
| 1921   | No file              |
| 1914   | No file              |
| 1908   | No file              |
| 1897   | No file              |
| 1892   | No file              |
| 1886   | No file              |
| 1881   | No file              |
| 1871   | No file              |
| 1866   | No file              |
| 1862   | No file              |
| 1854   | No file              |
| 1846   | No file              |
| 1838   | No file              |
| 1832   | No file              |
| 1826   | No file              |
| 1822   | No file              |
| 1818   | No file              |
| 1804   | No file              |
| 1794   | No file              |
| 1790   | No file              |
| 1784   | No file              |
| 1774   | No file              |
| 1771   | No file              |
| 1762   | No file              |
| 1759   | No file              |
| 1754   | No file              |
| 1749   | No file              |
| 1743   | No file              |
| 1737   | No file              |
| 1731   | No file              |
| 1725   | No file              |
| 1717   | No file              |
| 1710   | No file              |
| 1704   | No file              |
| 1698   | No file              |
| 1690   | No file              |
| 1685   | No file              |
| 1680   | No file              |
| 1674   | No file              |
| 1668   | No file              |
| 1659   | No file              |
| 1649   | No file              |
| 1642   | No file              |
| 1636   | No file              |
| 1628   | No file              |
| 1622   | No file              |
| 1614   | No file              |
| 1608   | No file              |
| 1602   | No file              |
| 1598   | No file              |
| 1594   | No file              |
| 1590   | No file              |
| 1587   | No file              |
| 1584   | No file              |
| 1579   | No file              |
| 1572   | No file              |
| 1565   | No file              |
| 1559   | No file              |
| 1554   | No file              |
| 1547   | No file              |
| 1537   | No file              |
| 1529   | No file              |
| 1524   | No file              |
| 1519   | No file              |
| 1509   | No file              |
| 1506   | No file              |
| 1504   | No file              |
| 1500   | No file              |
| 1493   | No file              |
| 1489   | No file              |
| 1485   | No file              |
| 1481   | No file              |
| 1474   | No file              |
| 1466   | No file              |
| 1462   | No file              |
| 1459   | No file              |
| 1453   | No file              |
| 1450   | No file              |
| 1445   | No file              |
| 1439   | No file              |
| 1433   | No file              |
| 1430   | No file              |
| 1426   | No file              |
| 1421   | No file              |
| 1417   | No file              |
| 1416   | No file              |
| 1409   | No file              |
| 1405   | No file              |
| 1401   | No file              |
| 1396   | No file              |
| 1391   | No file              |
| 1390   | No file              |
| 1386   | No file              |
| 1381   | No file              |
| 1379   | No file              |
| 1372   | No file              |
| 1366   | No file              |
| 1364   | No file              |
| 1363   | No file              |
| 1360   | No file              |
| 1358   | No file              |
| 1355   | No file              |
| 1351   | No file              |
| 1348   | No file              |
| 1346   | No file              |
| 1341   | No file              |
| 1340   | No file              |
| 1338   | No file              |
| 1335   | No file              |
| 1333   | No file              |
| 1329   | No file              |
| 1327   | No file              |
| 1324   | No file              |
| 1321   | No file              |
| 1319   | No file              |
| 1318   | No file              |
| 1316   | No file              |
| 1313   | No file              |
| 1311   | No file              |
| 1309   | No file              |
| 1304   | No file              |
| 1292   | No file              |
| 1286   | No file              |
| 1280   | No file              |
| 1276   | No file              |
| 1267   | No file              |
| 1261   | No file              |
| 1256   | No file              |
| 1250   | No file              |
| 1246   | No file              |
| 1239   | No file              |
| 1230   | No file              |
| 1226   | No file              |
| 1220   | No file              |
| 1217   | No file              |
| 1211   | No file              |
| 1210   | No file              |
| 1208   | No file              |
| 1203   | No file              |
| 1197   | No file              |
| 1194   | No file              |
| 1192   | No file              |
| 1187   | No file              |
| 1183   | No file              |
| 1177   | No file              |
| 1173   | No file              |
| 1167   | No file              |
| 1164   | No file              |
| 1156   | No file              |
| 1149   | No file              |
| 1144   | No file              |
| 1137   | No file              |
| 1132   | No file              |
| 1127   | No file              |
| 1122   | No file              |
| 1118   | No file              |
| 1114   | No file              |
| 1109   | No file              |
| 1102   | No file              |
| 1096   | No file              |
| 1088   | No file              |
| 1081   | No file              |
| 1076   | No file              |
| 1069   | No file              |
| 1064   | No file              |
| 1058   | No file              |
| 1051   | No file              |
| 1044   | No file              |
| 1036   | No file              |
| 1026   | No file              |
| 1016   | No file              |
| 1009   | No file              |
| 1005   | No file              |
| 1000   | No file              |
| 998    | No file              |
| 990    | No file              |
| 979    | No file              |
| 972    | No file              |
| 963    | No file              |
| 955    | No file              |
| 946    | No file              |
| 938    | No file              |
| 927    | No file              |
| 911    | No file              |
| 904    | No file              |
| 899    | No file              |
| 894    | No file              |
| 885    | No file              |
| 879    | No file              |
| 872    | No file              |
| 864    | No file              |
| 855    | No file              |
| 853    | No file              |
| 845    | No file              |
| 837    | No file              |
| 829    | No file              |
| 822    | No file              |
| 814    | No file              |
| 805    | No file              |
| 794    | No file              |
| 787    | No file              |
| 780    | No file              |
| 771    | No file              |
| 760    | No file              |
| 748    | No file              |
| 741    | No file              |
| 736    | No file              |
| 731    | No file              |
| 723    | No file              |
| 711    | No file              |
| 707    | No file              |
| 697    | No file              |
| 689    | No file              |
| 683    | No file              |
| 678    | No file              |
| 670    | No file              |
| 661    | No file              |
| 656    | No file              |
| 652    | No file              |
| 643    | No file              |
| 637    | No file              |
| 630    | No file              |
| 627    | No file              |
| 621    | No file              |
| 617    | No file              |
| 615    | No file              |
| 606    | No file              |
| 599    | No file              |
| 592    | No file              |
| 586    | No file              |
| 577    | No file              |
| 569    | No file              |
| 561    | No file              |
| 554    | No file              |
| 542    | No file              |
| 532    | No file              |
| 531    | No file              |
| 526    | No file              |
| 521    | No file              |
| 517    | No file              |
| 510    | No file              |
| 508    | No file              |
| 504    | No file              |
| 497    | No file              |
| 491    | No file              |
| 485    | No file              |
| 478    | No file              |
| 472    | No file              |
| 466    | No file              |
| 457    | No file              |
| 452    | No file              |
| 449    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows, one per territory             |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 6 bytes + groups)

| Offset  | Type               | Field         | Notes                                                                |
| ------- | ------------------ | ------------- | -------------------------------------------------------------------- |
| `+0x00` | u16                | territory_key | `territoryinfo.bss` key, LOC type 12 name; `0` Balenos, `2` Calpheon |
| `+0x02` | u32                | group_count   | Number of groups; `2` on client 3482                                 |
| `+0x06` | Group[group_count] | groups        | See Group                                                            |

### Group (variable: 5 bytes + positions)

| Offset  | Type                     | Field          | Notes                                              |
| ------- | ------------------------ | -------------- | -------------------------------------------------- |
| `+0x00` | u8                       | unknown_00     | `0` or `1`, in that order; see Open Questions      |
| `+0x01` | u32                      | position_count | Number of positions                                |
| `+0x05` | Position[position_count] | positions      | See Position                                       |

### Position (17 bytes)

| Offset  | Type | Field      | Notes                                                      |
| ------- | ---- | ---------- | ---------------------------------------------------------- |
| `+0x00` | f32  | x          | World x                                                    |
| `+0x04` | f32  | y          | Height, `-7777` to `-7315` on client 3482                  |
| `+0x08` | f32  | z          | World z                                                    |
| `+0x0C` | f32  | unknown_0c | `150` to `400`; see Open Questions                         |
| `+0x10` | u8   | unknown_10 | Equals its group's `unknown_00` on every position          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Positions

Client 3482, in file order, with the `regioninfo.bss` region whose return
point lies nearest.

| `territory_key` | Group | x, y, z                    | `unknown_0c` | Nearest return point                 |
| --------------- | ----- | -------------------------- | ------------ | ------------------------------------ |
| `0`             | `0`   | 6186, -7676, 93658         | 200          | Velia (14,114 units)                 |
| `0`             | `0`   | 152080, -7653, 291935      | 150          | Iliya Island (7,122)                 |
| `0`             | `0`   | -53614, -7658, 392395      | 400          | Crow Merchants' Vessel (5,740)       |
| `0`             | `0`   | -138892, -7500, 177043     | 250          | Olvia Academy Fountain (33,182)      |
| `0`             | `0`   | -74427, -7500, 127677      | 250          | Epheria Ridge (52,394)               |
| `0`             | `1`   | -339970, -7315, 374486     | 300          | none within 280,000                  |
| `2`             | `0`   | -358820, -7777, 38104      | 200          | Port Epheria (10,179)                |
| `2`             | `0`   | -451604, -7662, 30992      | 300          | Outpost Supply Port (4,703)          |
| `2`             | `0`   | -339970, -7315, 374486     | 300          | none within 280,000                  |
| `2`             | `1`   | -339970, -7315, 374486     | 300          | none within 280,000                  |

## Field Names

The Blue Battlefield is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client covers it, and no Lua function of client 3482 names it. `territory_key` holds `0`
and `2`, the two keys of `CppEnums.OceanSiegeTerritoryName`
(`global_define_cpp_enum.luac`, client 3482: Balenos and Calpheon), and
each row's harbour positions lie in that territory: Velia for `0`, Port
Epheria for `2`. The positions read as BDO world coordinates on the
scale of the `regioninfo.bss` return points, y the height near sea
level.

## Notes

- Client 3251 has the Balenos row only (104 bytes): the first three
  group `0` positions of client 3482 and a group `1` position at
  `(-339772, -7531, 373439)` with `unknown_0c` `400`. The file is not in
  the archives of client 1784.
- The handler (`_bss/oceansiegereviveposition/`) shows one row per
  position: the territory key and name and the position rounded to whole
  units, in file order. It previews
  [`siege2024revivepositionstaticstatus.bss`](siege2024revivepositionstaticstatus_bss.md)
  too, with that file's reader.

## Open Questions

### The Two Groups

Each territory has a group `0` of harbour positions and a group `1` of
one position, the same `(-339970, -7315, 374486)` for both territories,
which Calpheon's group `0` lists too. Attacker and defender sides, or
the positions before and after the battle, both fit; no Lua names a
`__eRespawnType` for the ocean siege.

### The f32 of Each Position

`unknown_0c` is `150` to `400`. A spread radius around the position fits,
as the f32 after the positions of
[`rosewarrevivepositionstaticstatus.bss`](rosewarrevivepositionstaticstatus_bss.md)
does, but nothing reads it.
