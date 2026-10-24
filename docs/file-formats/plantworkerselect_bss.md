# `plantworkerselect.bss` Format

## Purpose

Worker selection table keyed by town/node LOC IDs. Each group lists workers that can appear for one town/node, each with the silver price to hire that worker there (`hire_cost`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records                                 | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | --------------------------------------- | --------- |
| 1      | 2783 and later | 3483    | `plantworkerselect.bss` | 6,288 | 385 Selection Entry, 31 Selection Group | 16        |

| Layout | File                    | Known           | Unknown         |
| ------ | ----------------------- | --------------- | --------------- |
| 1      | `plantworkerselect.bss` | 3,208 B (51.0%) | 3,080 B (49.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3464   | Layout 1 |
| 3458   | Layout 1 |
| 3454   | Layout 1 |
| 3444   | Layout 1 |
| 3435   | Layout 1 |
| 3426   | Layout 1 |
| 3418   | Layout 1 |
| 3412   | Layout 1 |
| 3402   | Layout 1 |
| 3396   | Layout 1 |
| 3387   | Layout 1 |
| 3381   | Layout 1 |
| 3373   | Layout 1 |
| 3364   | Layout 1 |
| 3356   | Layout 1 |
| 3349   | Layout 1 |
| 3342   | Layout 1 |
| 3335   | Layout 1 |
| 3326   | Layout 1 |
| 3321   | Layout 1 |
| 3314   | Layout 1 |
| 3303   | Layout 1 |
| 3302   | Layout 1 |
| 3293   | Layout 1 |
| 3283   | Layout 1 |
| 3275   | Layout 1 |
| 3267   | Layout 1 |
| 3258   | Layout 1 |
| 3251   | Layout 1 |
| 3242   | Layout 1 |
| 3235   | Layout 1 |
| 3229   | Layout 1 |
| 3212   | Layout 1 |
| 3203   | Layout 1 |
| 3193   | Layout 1 |
| 3186   | Layout 1 |
| 3177   | Layout 1 |
| 3169   | Layout 1 |
| 3158   | Layout 1 |
| 3151   | Layout 1 |
| 3144   | Layout 1 |
| 3133   | Layout 1 |
| 3125   | Layout 1 |
| 3118   | Layout 1 |
| 3111   | Layout 1 |
| 3103   | Layout 1 |
| 3095   | Layout 1 |
| 3086   | Layout 1 |
| 3072   | Layout 1 |
| 3062   | Layout 1 |
| 3052   | Layout 1 |
| 3045   | Layout 1 |
| 3037   | Layout 1 |
| 3030   | Layout 1 |
| 3021   | Layout 1 |
| 3012   | Layout 1 |
| 3002   | Layout 1 |
| 2995   | Layout 1 |
| 2987   | Layout 1 |
| 2978   | Layout 1 |
| 2970   | Layout 1 |
| 2959   | Layout 1 |
| 2951   | Layout 1 |
| 2942   | Layout 1 |
| 2935   | Layout 1 |
| 2932   | Layout 1 |
| 2923   | Layout 1 |
| 2919   | Layout 1 |
| 2907   | Layout 1 |
| 2900   | Layout 1 |
| 2891   | Layout 1 |
| 2882   | Layout 1 |
| 2872   | Layout 1 |
| 2863   | Layout 1 |
| 2855   | Layout 1 |
| 2849   | Layout 1 |
| 2844   | Layout 1 |
| 2834   | Layout 1 |
| 2825   | Layout 1 |
| 2819   | Layout 1 |
| 2811   | Layout 1 |
| 2803   | Layout 1 |
| 2794   | Layout 1 |
| 2783   | Layout 1 |
| 2774   | No file  |
| 2765   | No file  |
| 2756   | No file  |
| 2750   | No file  |
| 2743   | No file  |
| 2736   | No file  |
| 2726   | No file  |
| 2717   | No file  |
| 2709   | No file  |
| 2703   | No file  |
| 2695   | No file  |
| 2684   | No file  |
| 2672   | No file  |
| 2665   | No file  |
| 2657   | No file  |
| 2649   | No file  |
| 2644   | No file  |
| 2637   | No file  |
| 2629   | No file  |
| 2619   | No file  |
| 2612   | No file  |
| 2606   | No file  |
| 2602   | No file  |
| 2601   | No file  |
| 2592   | No file  |
| 2583   | No file  |
| 2575   | No file  |
| 2567   | No file  |
| 2560   | No file  |
| 2553   | No file  |
| 2545   | No file  |
| 2538   | No file  |
| 2529   | No file  |
| 2519   | No file  |
| 2513   | No file  |
| 2510   | No file  |
| 2507   | No file  |
| 2503   | No file  |
| 2498   | No file  |
| 2492   | No file  |
| 2487   | No file  |
| 2480   | No file  |
| 2474   | No file  |
| 2468   | No file  |
| 2460   | No file  |
| 2453   | No file  |
| 2444   | No file  |
| 2438   | No file  |
| 2434   | No file  |
| 2429   | No file  |
| 2421   | No file  |
| 2414   | No file  |
| 2407   | No file  |
| 2401   | No file  |
| 2397   | No file  |
| 2393   | No file  |
| 2384   | No file  |
| 2378   | No file  |
| 2372   | No file  |
| 2358   | No file  |
| 2352   | No file  |
| 2347   | No file  |
| 2343   | No file  |
| 2335   | No file  |
| 2327   | No file  |
| 2324   | No file  |
| 2319   | No file  |
| 2313   | No file  |
| 2308   | No file  |
| 2302   | No file  |
| 2295   | No file  |
| 2290   | No file  |
| 2284   | No file  |
| 2276   | No file  |
| 2269   | No file  |
| 2259   | No file  |
| 2250   | No file  |
| 2243   | No file  |
| 2235   | No file  |
| 2229   | No file  |
| 2224   | No file  |
| 2218   | No file  |
| 2215   | No file  |
| 2207   | No file  |
| 2203   | No file  |
| 2196   | No file  |
| 2192   | No file  |
| 2189   | No file  |
| 2183   | No file  |
| 2179   | No file  |
| 2171   | No file  |
| 2163   | No file  |
| 2156   | No file  |
| 2151   | No file  |
| 2147   | No file  |
| 2142   | No file  |
| 2138   | No file  |
| 2134   | No file  |
| 2130   | No file  |
| 2122   | No file  |
| 2107   | No file  |
| 2098   | No file  |
| 2089   | No file  |
| 2081   | No file  |
| 2073   | No file  |
| 2067   | No file  |
| 2063   | No file  |
| 2059   | No file  |
| 2052   | No file  |
| 2044   | No file  |
| 2039   | No file  |
| 2032   | No file  |
| 2025   | No file  |
| 2011   | No file  |
| 2005   | No file  |
| 2000   | No file  |
| 1996   | No file  |
| 1991   | No file  |
| 1985   | No file  |
| 1980   | No file  |
| 1969   | No file  |
| 1964   | No file  |
| 1958   | No file  |
| 1950   | No file  |
| 1945   | No file  |
| 1937   | No file  |
| 1933   | No file  |
| 1927   | No file  |
| 1921   | No file  |
| 1914   | No file  |
| 1908   | No file  |
| 1897   | No file  |
| 1892   | No file  |
| 1886   | No file  |
| 1881   | No file  |
| 1871   | No file  |
| 1866   | No file  |
| 1862   | No file  |
| 1854   | No file  |
| 1846   | No file  |
| 1838   | No file  |
| 1832   | No file  |
| 1826   | No file  |
| 1822   | No file  |
| 1818   | No file  |
| 1804   | No file  |
| 1794   | No file  |
| 1790   | No file  |
| 1784   | No file  |
| 1774   | No file  |
| 1771   | No file  |
| 1762   | No file  |
| 1759   | No file  |
| 1754   | No file  |
| 1749   | No file  |
| 1743   | No file  |
| 1737   | No file  |
| 1731   | No file  |
| 1725   | No file  |
| 1717   | No file  |
| 1710   | No file  |
| 1704   | No file  |
| 1698   | No file  |
| 1690   | No file  |
| 1685   | No file  |
| 1680   | No file  |
| 1674   | No file  |
| 1668   | No file  |
| 1659   | No file  |
| 1649   | No file  |
| 1642   | No file  |
| 1636   | No file  |
| 1628   | No file  |
| 1622   | No file  |
| 1614   | No file  |
| 1608   | No file  |
| 1602   | No file  |
| 1598   | No file  |
| 1594   | No file  |
| 1590   | No file  |
| 1587   | No file  |
| 1584   | No file  |
| 1579   | No file  |
| 1572   | No file  |
| 1565   | No file  |
| 1559   | No file  |
| 1554   | No file  |
| 1547   | No file  |
| 1537   | No file  |
| 1529   | No file  |
| 1524   | No file  |
| 1519   | No file  |
| 1509   | No file  |
| 1506   | No file  |
| 1504   | No file  |
| 1500   | No file  |
| 1493   | No file  |
| 1489   | No file  |
| 1485   | No file  |
| 1481   | No file  |
| 1474   | No file  |
| 1466   | No file  |
| 1462   | No file  |
| 1459   | No file  |
| 1453   | No file  |
| 1450   | No file  |
| 1445   | No file  |
| 1439   | No file  |
| 1433   | No file  |
| 1430   | No file  |
| 1426   | No file  |
| 1421   | No file  |
| 1417   | No file  |
| 1416   | No file  |
| 1409   | No file  |
| 1405   | No file  |
| 1401   | No file  |
| 1396   | No file  |
| 1391   | No file  |
| 1390   | No file  |
| 1386   | No file  |
| 1381   | No file  |
| 1379   | No file  |
| 1372   | No file  |
| 1366   | No file  |
| 1364   | No file  |
| 1363   | No file  |
| 1360   | No file  |
| 1358   | No file  |
| 1355   | No file  |
| 1351   | No file  |
| 1348   | No file  |
| 1346   | No file  |
| 1341   | No file  |
| 1340   | No file  |
| 1338   | No file  |
| 1335   | No file  |
| 1333   | No file  |
| 1329   | No file  |
| 1327   | No file  |
| 1324   | No file  |
| 1321   | No file  |
| 1319   | No file  |
| 1318   | No file  |
| 1316   | No file  |
| 1313   | No file  |
| 1311   | No file  |
| 1309   | No file  |
| 1304   | No file  |
| 1292   | No file  |
| 1286   | No file  |
| 1280   | No file  |
| 1276   | No file  |
| 1267   | No file  |
| 1261   | No file  |
| 1256   | No file  |
| 1250   | No file  |
| 1246   | No file  |
| 1239   | No file  |
| 1230   | No file  |
| 1226   | No file  |
| 1220   | No file  |
| 1217   | No file  |
| 1211   | No file  |
| 1210   | No file  |
| 1208   | No file  |
| 1203   | No file  |
| 1197   | No file  |
| 1194   | No file  |
| 1192   | No file  |
| 1187   | No file  |
| 1183   | No file  |
| 1177   | No file  |
| 1173   | No file  |
| 1167   | No file  |
| 1164   | No file  |
| 1156   | No file  |
| 1149   | No file  |
| 1144   | No file  |
| 1137   | No file  |
| 1132   | No file  |
| 1127   | No file  |
| 1122   | No file  |
| 1118   | No file  |
| 1114   | No file  |
| 1109   | No file  |
| 1102   | No file  |
| 1096   | No file  |
| 1088   | No file  |
| 1081   | No file  |
| 1076   | No file  |
| 1069   | No file  |
| 1064   | No file  |
| 1058   | No file  |
| 1051   | No file  |
| 1044   | No file  |
| 1036   | No file  |
| 1026   | No file  |
| 1016   | No file  |
| 1009   | No file  |
| 1005   | No file  |
| 1000   | No file  |
| 998    | No file  |
| 990    | No file  |
| 979    | No file  |
| 972    | No file  |
| 963    | No file  |
| 955    | No file  |
| 946    | No file  |
| 938    | No file  |
| 927    | No file  |
| 911    | No file  |
| 904    | No file  |
| 899    | No file  |
| 894    | No file  |
| 885    | No file  |
| 879    | No file  |
| 872    | No file  |
| 864    | No file  |
| 855    | No file  |
| 853    | No file  |
| 845    | No file  |
| 837    | No file  |
| 829    | No file  |
| 822    | No file  |
| 814    | No file  |
| 805    | No file  |
| 794    | No file  |
| 787    | No file  |
| 780    | No file  |
| 771    | No file  |
| 760    | No file  |
| 748    | No file  |
| 741    | No file  |
| 736    | No file  |
| 731    | No file  |
| 723    | No file  |
| 711    | No file  |
| 707    | No file  |
| 697    | No file  |
| 689    | No file  |
| 683    | No file  |
| 678    | No file  |
| 670    | No file  |
| 661    | No file  |
| 656    | No file  |
| 652    | No file  |
| 643    | No file  |
| 637    | No file  |
| 630    | No file  |
| 627    | No file  |
| 621    | No file  |
| 617    | No file  |
| 615    | No file  |
| 606    | No file  |
| 599    | No file  |
| 592    | No file  |
| 586    | No file  |
| 577    | No file  |
| 569    | No file  |
| 561    | No file  |
| 554    | No file  |
| 542    | No file  |
| 532    | No file  |
| 531    | No file  |
| 526    | No file  |
| 521    | No file  |
| 517    | No file  |
| 510    | No file  |
| 508    | No file  |
| 504    | No file  |
| 497    | No file  |
| 491    | No file  |
| 485    | No file  |
| 478    | No file  |
| 472    | No file  |
| 466    | No file  |
| 457    | No file  |
| 452    | No file  |
| 449    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                |
| --------------------- | -------- | --------------------------------------------------- |
| `plantworker.bss`     | Optional | Resolves `worker_id` to worker stats and icon paths |
| `languagedata_en.loc` | Optional | Resolves town/node names and worker names           |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset  | Type                         | Field        | Notes                              |
| ------- | ---------------------------- | ------------ | ---------------------------------- |
| `+0x00` | u32                          | group_count  | Number of selection groups; observed `30` in the pre-2026-09-27 fixture, `31` in the 2026-09-27 client |
| `+0x04` | Selection Group[group_count] | group_stream | `group_count` groups packed in row |

The file is fully consumed by `4 + sum(4 + entry_count * 0x10)`.

### Selection Group (variable: 4 bytes + entries)

| Offset  | Type                          | Field       | Notes                                           |
| ------- | ----------------------------- | ----------- | ----------------------------------------------- |
| `+0x00` | u32                           | entry_count | Number of entries in this group: 8, 12, or 13   |
| `+0x04` | Selection Entry[entry_count]  | entries     | `entry_count` 16-byte selection entries         |

Each group repeats one `selection_id` across all entries. Observed group sizes:

| Entry Count | Group Count |
| ----------- | ----------- |
| 8           | 2           |
| 12          | 8           |
| 13          | 20          |

These are the pre-2026-09-27 fixture's 30 groups and 372 entries. The 2026-09-27 client adds Angavu Outpost (`1733`, 13 entries) as group 1, for 31 groups and 385 entries.

### Selection Entry (16 bytes)

| Offset  | Type | Field        | Notes                                                 |
| ------- | ---- | ------------ | ----------------------------------------------------- |
| `+0x00` | u16  | selection_id | Town region key (`regioninfo.bss`), LOC type `17`; same value within group |
| `+0x02` | u16  | worker_id    | Worker ID; matches `plantworker.bss` and LOC type `6` |
| `+0x04` | u32  | unknown_04   | Always observed as `0`                                |
| `+0x08` | u32  | hire_cost    | Hire price in silver; observed `1500`, `3500`, `10000`, `30000`, `90000` |
| `+0x0C` | u32  | unknown_0c   | Always observed as `0`                                |

Derived fields:

```text
selection_name = LOC type 17, str_id1=selection_id, str_id4=0
worker_name = LOC type 6, str_id1=worker_id, str_id4=0
```

## Selection IDs

| Selection ID | Name                   | Entry Count |
| ------------ | ---------------------- | ----------- |
| `5`          | Velia                  | 13          |
| `32`         | Heidel                 | 13          |
| `52`         | Glish                  | 13          |
| `77`         | Calpheon City          | 13          |
| `88`         | Olvia                  | 13          |
| `107`        | Keplan                 | 13          |
| `120`        | Port Epheria           | 13          |
| `126`        | Trent                  | 13          |
| `182`        | Iliya Island           | 13          |
| `202`        | Altinova               | 13          |
| `218`        | Asparkan               | 13          |
| `221`        | Tarif                  | 13          |
| `229`        | Valencia City          | 13          |
| `601`        | Shakatu                | 13          |
| `605`        | Sand Grain Bazaar      | 13          |
| `619`        | Ancado Inner Harbor    | 13          |
| `693`        | Arehaza                | 13          |
| `706`        | Old Wisdom Tree        | 8           |
| `735`        | Grana                  | 8           |
| `873`        | Duvencrune             | 13          |
| `955`        | O'draxxia              | 12          |
| `1124`       | Eilton                 | 12          |
| `1210`       | Dalbeol Village        | 12          |
| `1219`       | Nampo's Moodle Village | 12          |
| `1246`       | Nopsae's Byeot County  | 12          |
| `1375`       | Muzgar                 | 13          |
| `1420`       | Yukjo Street           | 12          |
| `1424`       | Godu Village           | 12          |
| `1444`       | Bukpo                  | 12          |
| `1553`       | Hakinza Sanctuary      | 13          |
| `1733`       | Angavu Outpost         | 13; 2026-09-27 client only |

## Reference Rows

| Group | Selection ID | Selection Name | Worker ID | Worker Name    | Hire Cost |
| ----- | ------------ | -------------- | --------- | -------------- | --------- |
| 0     | `77`         | Calpheon City  | `7501`    | Naive Worker   | `1500`     |
| 0     | `77`         | Calpheon City  | `7502`    | Giant Worker   | `3500`     |
| 0     | `77`         | Calpheon City  | `7571`    | Artisan Giant Worker | `90000`    |
| 18    | `735`        | Grana          | `8001`    | Papu Worker    | `3500`     |
| 20    | `955`        | O'draxxia      | `8020`    | Dwarf Worker   | `3500`     |
| 21    | `1444`       | Bukpo          | `8047`    | Dokkebi Worker | `3500`     |

Group numbers are from the pre-2026-09-27 fixture; in the 2026-09-27 client every group after `0` moves down by one.

## Notes

- Observed file size is `6,076` bytes in the pre-2026-09-27 fixture, `6,288` in the 2026-09-27 client.
- There is no `PABR` magic; the file starts with the top-level group count.
- All `worker_id` values in this file exist in `plantworker.bss`.
- `unknown_04` and `unknown_0c` are invariant zero fields across all observed entries.
- Hire costs map to a small fixed set: `1500`, `3500`, `10000`, `30000`, and `90000`. In most towns the price rises with grade (Naive `1500`, base `3500`, Skilled `10000`, Professional `30000`, Artisan `90000`).
- In game the five grades are colored white (Naive), green (base, e.g. `Papu Worker`), blue (Skilled), yellow (Professional) and red (Artisan); this file stores only the worker ID, the grade comes from `plantworker.bss`.
- Old Wisdom Tree (`706`) prices its Papu and Fadus grades in reverse: Artisan `3500`, Professional `10000`, Skilled `30000`, base `90000`.
- Checked in game on 2026-09-28: in Grána (`735`) a base worker costs 3,500, a Skilled 10,000 and a Professional 30,000; in Old Wisdom Tree an Artisan costs 3,500; in O'draxxia (`955`) a base Dwarf Worker (`8020`) costs 3,500; in Heidel (`32`) a Naive worker costs 1,500, a base 3,500, a Skilled 10,000 and an Artisan Goblin Worker (`7572`) 90,000. All nine match the stored `hire_cost` of that row, covering every price level.

## In-Game Checks

### Old Wisdom Tree Grades After the Event

Needs NPC: [Mathieu](https://bdocodex.com/us/npc/45593/)

Needs zone: Old Wisdom Tree

Old Wisdom Tree (`706`) lists all four Papu and Fadus grades, but on 2026-09-28 only Artisan Papu and Fadus workers came up there (3,500 silver, several rolls), most likely because of an event. Once it ends, roll workers at Mathieu a few times. If base, Skilled and Professional workers come up again, the list is the whole story and the reverse prices hold: a base worker costs 90,000. If only Artisans come up, something outside this file limits the grades there.
