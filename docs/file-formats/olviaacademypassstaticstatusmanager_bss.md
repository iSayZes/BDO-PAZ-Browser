# `olviaacademypassstaticstatusmanager.bss` Format

## Purpose

The steps of the nine Olvia Academy Pass tabs
(`panel_window_olviaacademy_pass_all*.luac`). Per tab the file holds a step
count and per step the base quest and the pass quest, both packed quest IDs
`(quest_id << 16) | quest_chain_id` of
[`olviaacademypassquestlist.bss`](olviaacademyquestlist_bss.md). The tabs
have no key and no count: they follow the PABR magic one after the other, in
the order of the `__eOlviaAcademyPassType_*` values, up to the string table.
The curricula of the same academy are in
[`olviaacademycurriculumss.bss`](olviaacademycurriculumss_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                      | Bytes | Records         | Row bytes |
| ------ | -------------- | ------- | ----------------------------------------- | ----- | --------------- | --------- |
| 1      | 3186 and later | 3482    | `olviaacademypassstaticstatusmanager.bss` | 772   | 90 Step, 9 Pass | 8         |

| Layout | File                                      | Known          | Unknown    |
| ------ | ----------------------------------------- | -------------- | ---------- |
| 1      | `olviaacademypassstaticstatusmanager.bss` | 772 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
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
| 3177   | No file  |
| 3169   | No file  |
| 3158   | No file  |
| 3151   | No file  |
| 3144   | No file  |
| 3133   | No file  |
| 3125   | No file  |
| 3118   | No file  |
| 3111   | No file  |
| 3103   | No file  |
| 3095   | No file  |
| 3086   | No file  |
| 3072   | No file  |
| 3062   | No file  |
| 3052   | No file  |
| 3045   | No file  |
| 3037   | No file  |
| 3030   | No file  |
| 3021   | No file  |
| 3012   | No file  |
| 3002   | No file  |
| 2995   | No file  |
| 2987   | No file  |
| 2978   | No file  |
| 2970   | No file  |
| 2959   | No file  |
| 2951   | No file  |
| 2942   | No file  |
| 2935   | No file  |
| 2932   | No file  |
| 2923   | No file  |
| 2919   | No file  |
| 2907   | No file  |
| 2900   | No file  |
| 2891   | No file  |
| 2882   | No file  |
| 2872   | No file  |
| 2863   | No file  |
| 2855   | No file  |
| 2849   | No file  |
| 2844   | No file  |
| 2834   | No file  |
| 2825   | No file  |
| 2819   | No file  |
| 2811   | No file  |
| 2803   | No file  |
| 2794   | No file  |
| 2783   | No file  |
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

None. The handler names each quest with its LOC type 18 title from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                | Field        | Notes                                                       |
| ------------------- | ------------------- | ------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]             | magic        | ASCII `PABR`                                                |
| `+0x04`             | Pass[..table_start] | passes       | One per pass type, `__eOlviaAcademyPassType_Collect` first; see Pass Types |
| `passes+0x00`       | String Table        | string_table | See String Table                                            |
| `EOF-0x08`          | u32                 | table_start  | Offset of the string table, where `passes` ends             |
| `EOF-0x04`          | u32                 | zero         | Always `0`                                                  |

### Pass (variable: 4 bytes + steps)

| Offset  | Type             | Field     | Notes                                                       |
| ------- | ---------------- | --------- | ----------------------------------------------------------- |
| `+0x00` | u32              | pass_size | `ToClient_GetOlviaAcademyPassSize(passType)`; `10` on every pass (client 3482) |
| `+0x04` | Step[pass_size]  | steps     | `questIndex` from `0`                                       |

### Step (8 bytes)

| Offset  | Type | Field      | Notes                                                               |
| ------- | ---- | ---------- | ------------------------------------------------------------------- |
| `+0x00` | u32  | base_quest | `ToClient_GetOlviaAcademyQuest(passType, questIndex, __eOlviaAcademyPassQuestType_Base)`; packed quest ID |
| `+0x04` | u32  | pass_quest | The same with `__eOlviaAcademyPassQuestType_Pass`; packed quest ID  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3482     |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                   |

## Pass Types

`panel_window_olviaacademy_pass_all_1.luac` walks the passes with
`for passType = __eOlviaAcademyPassType_Collect, __eOlviaAcademyPassType_Count - 1`,
and `panel_window_olviaacademy_pass_all.luac` lists the nine values in this
order. On client 3482 every step of pass `n` (from `0`) is chain 2324 with
`base_quest` at sub ID `(n + 1) * 100 + 2 * questIndex + 1` and
`pass_quest` at the next sub ID, so the file order is the value order:

| Pass | Pass type (Lua)                    | Base quests (sub IDs)  | Title          |
| ---- | ---------------------------------- | ---------------------- | -------------- |
| 0    | `__eOlviaAcademyPassType_Collect`  | 101, 103, ... 119      | Gathering Time! `n`. |
| 1    | `__eOlviaAcademyPassType_Fish`     | 201, 203, ... 219      | Hands-On Fishing! `n`. |
| 2    | `__eOlviaAcademyPassType_Hunt`     | 301, 303, ... 319      | Happy Hunting! `n`. |
| 3    | `__eOlviaAcademyPassType_Cook`     | 401, 403, ... 419      | Win Them Over with Cooking! `n`. |
| 4    | `__eOlviaAcademyPassType_Alchemy`  | 501, 503, ... 519      | Hands-On Alchemy! `n`. |
| 5    | `__eOlviaAcademyPassType_Work`     | 601, 603, ... 619      | Processing in Progress! `n`. |
| 6    | `__eOlviaAcademyPassType_Train`    | 701, 703, ... 719      | Hands-On Training! `n`. |
| 7    | `__eOlviaAcademyPassType_Farm`     | 801, 803, ... 819      | Fantastic Farming! `n`. |
| 8    | `__eOlviaAcademyPassType_Ship`     | 901, 903, ... 919      | Hands-On Sailing! `n`. |

## Field Names

No reference source has the file: it first appears on client 3186
(absent on client 3177), and a private server's `DataSheets.bexcel` on
client 1784 has no sheet with `Olvia` or `Academy` in its name. The
names come from the client Lua of client 3482:
`panel_window_olviaacademy_pass_all_1.luac` reads `passSize` from
`ToClient_GetOlviaAcademyPassSize(passType)` and asks for each step with
`ToClient_GetOlviaAcademyQuest(passType, questIndex, __eOlviaAcademyPassQuestType_Base)`
and `..._Pass`. The base quest of every step is the quest whose title the
tab shows, the pass quest is that title with `(Olvia Academy Pass)`, whose
reward stays locked while `ToClient_HasOlviaAcademyPass(passType)` is false.

## Notes

- Decompressed size on client 3482: `772` bytes, 9 passes of 10 steps.
- The 180 quests of the 90 steps are exactly the quests of
  `olviaacademypassquestlist.bss` (client 3482), whose file order is not
  the step order.
- On every step `pass_quest` is `base_quest` plus `1 << 16`: the same chain,
  the next sub ID.
- The handler shows one row per step with its pass type, `questIndex + 1`
  as the step number and both quests with their titles; each quest links to
  its row in `olviaacademypassquestlist.bss`, and the pass quest list view
  links each quest back to its step.

## Open Questions

### A Pass With No Steps

The passes have no key: the reading takes the pass type from the position
in the file. Whether a pass type with no steps keeps a block with a
`pass_size` of `0`, so that every later pass keeps its position, is open;
every pass on client 3482 has 10 steps.
