# `intimacyrelation.dbss` Format

## Purpose

The first meeting with an NPC, per NPC character key: the line the NPC says
while its knowledge cannot be gained yet (`covered_dialog_kr`), the line
and cutscene when it is discovered, the knowledge the discovery grants
(`discover_function`, a `Pushknowledge(<knowledge>,0)` script) and up to
five more lines, each with a condition string. Every text is Korean;
LOC type 23 holds the user-language text under the NPC key. Companion
`intimacyrelationoffset.dbss` lists where every record sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes   | Records                 | Row bytes                    |
| ------ | -------------- | ------- | ----------------------------- | ------- | ----------------------- | ---------------------------- |
| 2      | 2583 and later | 3483    | `intimacyrelation.dbss`       | 748,525 | 2,206 Row, 2,206 Record | 136 to 1,504, 337 on average |
| 2      | 2583 and later | 3483    | `intimacyrelationoffset.dbss` | 22,064  | 2,206 Offset Row        | 10                           |
| 1      | 1346 to 2575   | 2575    | `intimacyrelation.dbss`       | 667,200 | 1,895 Row, 1,895 Record | 140 to 1,508, 350 on average |
| 1      | 1346 to 2575   | 2575    | `intimacyrelationoffset.dbss` | 18,954  | 1,895 Offset Row        | 10                           |

| Layout | File                          | Known             | Unknown        |
| ------ | ----------------------------- | ----------------- | -------------- |
| 2      | `intimacyrelation.dbss`       | 739,701 B (98.8%) | 8,824 B (1.2%) |
| 2      | `intimacyrelationoffset.dbss` | 22,064 B (100.0%) | 0 B (0.0%)     |
| 1      | `intimacyrelation.dbss`       | 659,620 B (98.9%) | 7,580 B (1.1%) |
| 1      | `intimacyrelationoffset.dbss` | 18,954 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 2             |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3464   | Layout 2             |
| 3458   | Layout 2             |
| 3454   | Layout 2             |
| 3444   | Layout 2             |
| 3435   | Layout 2             |
| 3426   | Layout 2             |
| 3418   | Layout 2             |
| 3412   | Layout 2             |
| 3402   | Layout 2             |
| 3396   | Layout 2             |
| 3387   | Layout 2             |
| 3381   | Layout 2             |
| 3373   | Layout 2             |
| 3364   | Layout 2             |
| 3356   | Layout 2             |
| 3349   | Layout 2             |
| 3342   | Layout 2             |
| 3335   | Layout 2             |
| 3326   | Layout 2             |
| 3321   | Layout 2             |
| 3314   | Layout 2             |
| 3303   | Layout 2             |
| 3302   | Layout 2             |
| 3293   | Layout 2             |
| 3283   | Layout 2             |
| 3275   | Layout 2             |
| 3267   | Layout 2             |
| 3258   | Layout 2             |
| 3251   | Layout 2             |
| 3242   | Layout 2             |
| 3235   | Layout 2             |
| 3229   | Layout 2             |
| 3212   | Layout 2             |
| 3203   | Layout 2             |
| 3193   | Layout 2             |
| 3186   | Layout 2             |
| 3177   | Layout 2             |
| 3169   | Layout 2             |
| 3158   | Layout 2             |
| 3151   | Layout 2             |
| 3144   | Layout 2             |
| 3133   | Layout 2             |
| 3125   | Layout 2             |
| 3118   | Layout 2             |
| 3111   | Layout 2             |
| 3103   | Layout 2             |
| 3095   | Layout 2             |
| 3086   | Layout 2             |
| 3072   | Layout 2             |
| 3062   | Layout 2             |
| 3052   | Layout 2             |
| 3045   | Layout 2             |
| 3037   | Layout 2             |
| 3030   | Layout 2             |
| 3021   | Layout 2             |
| 3012   | Layout 2             |
| 3002   | Layout 2             |
| 2995   | Layout 2             |
| 2987   | Layout 2             |
| 2978   | Layout 2             |
| 2970   | Layout 2             |
| 2959   | Layout 2             |
| 2951   | Layout 2             |
| 2942   | Layout 2             |
| 2935   | Layout 2             |
| 2932   | Layout 2             |
| 2923   | Layout 2             |
| 2919   | Layout 2             |
| 2907   | Layout 2             |
| 2900   | Layout 2             |
| 2891   | Layout 2             |
| 2882   | Layout 2             |
| 2872   | Layout 2             |
| 2863   | Layout 2             |
| 2855   | Layout 2             |
| 2849   | Layout 2             |
| 2844   | Layout 2             |
| 2834   | Layout 2             |
| 2825   | Layout 2             |
| 2819   | Layout 2             |
| 2811   | Layout 2             |
| 2803   | Layout 2             |
| 2794   | Layout 2             |
| 2783   | Layout 2             |
| 2774   | Layout 2             |
| 2765   | Layout 2             |
| 2756   | Layout 2             |
| 2750   | Layout 2             |
| 2743   | Layout 2             |
| 2736   | Layout 2             |
| 2726   | Layout 2             |
| 2717   | Layout 2             |
| 2709   | Layout 2             |
| 2703   | Layout 2             |
| 2695   | Layout 2             |
| 2684   | Layout 2             |
| 2672   | Layout 2             |
| 2665   | Layout 2             |
| 2657   | Layout 2             |
| 2649   | Layout 2             |
| 2644   | Layout 2             |
| 2637   | Layout 2             |
| 2629   | Layout 2             |
| 2619   | Layout 2             |
| 2612   | Layout 2             |
| 2606   | Layout 2             |
| 2602   | Layout 2             |
| 2601   | Layout 2             |
| 2592   | Layout 2             |
| 2583   | Layout 2             |
| 2575   | Layout 1             |
| 2567   | Layout 1             |
| 2560   | Layout 1             |
| 2553   | Layout 1             |
| 2545   | Layout 1             |
| 2538   | Layout 1             |
| 2529   | Layout 1             |
| 2519   | Layout 1             |
| 2513   | Layout 1             |
| 2510   | Layout 1             |
| 2507   | Layout 1             |
| 2503   | Layout 1             |
| 2498   | Layout 1             |
| 2492   | Layout 1             |
| 2487   | Layout 1             |
| 2480   | Layout 1             |
| 2474   | Layout 1             |
| 2468   | Layout 1             |
| 2460   | Layout 1             |
| 2453   | Layout 1             |
| 2444   | Layout 1             |
| 2438   | Layout 1             |
| 2434   | Layout 1             |
| 2429   | Layout 1             |
| 2421   | Layout 1             |
| 2414   | Layout 1             |
| 2407   | Layout 1             |
| 2401   | Layout 1             |
| 2397   | Layout 1             |
| 2393   | Layout 1             |
| 2384   | Layout 1             |
| 2378   | Layout 1             |
| 2372   | Layout 1             |
| 2358   | Layout 1             |
| 2352   | Layout 1             |
| 2347   | Layout 1             |
| 2343   | Layout 1             |
| 2335   | Layout 1             |
| 2327   | Layout 1             |
| 2324   | Layout 1             |
| 2319   | Layout 1             |
| 2313   | Layout 1             |
| 2308   | Layout 1             |
| 2302   | Layout 1             |
| 2295   | Layout 1             |
| 2290   | Layout 1             |
| 2284   | Layout 1             |
| 2276   | Layout 1             |
| 2269   | Layout 1             |
| 2259   | Layout 1             |
| 2250   | Layout 1             |
| 2243   | Layout 1             |
| 2235   | Layout 1             |
| 2229   | Layout 1             |
| 2224   | Layout 1             |
| 2218   | Layout 1             |
| 2215   | Layout 1             |
| 2207   | Layout 1             |
| 2203   | Layout 1             |
| 2196   | Layout 1             |
| 2192   | Layout 1             |
| 2189   | Layout 1             |
| 2183   | Layout 1             |
| 2179   | Layout 1             |
| 2171   | Layout 1             |
| 2163   | Layout 1             |
| 2156   | Layout 1             |
| 2151   | Layout 1             |
| 2147   | Layout 1             |
| 2142   | Layout 1             |
| 2138   | Layout 1             |
| 2134   | Layout 1             |
| 2130   | Layout 1             |
| 2122   | Layout 1             |
| 2107   | Layout 1             |
| 2098   | Layout 1             |
| 2089   | Layout 1             |
| 2081   | Layout 1             |
| 2073   | Layout 1             |
| 2067   | Layout 1             |
| 2063   | Layout 1             |
| 2059   | Layout 1             |
| 2052   | Layout 1             |
| 2044   | Layout 1             |
| 2039   | Layout 1             |
| 2032   | Layout 1             |
| 2025   | Layout 1             |
| 2011   | Layout 1             |
| 2005   | Layout 1             |
| 2000   | Layout 1             |
| 1996   | Layout 1             |
| 1991   | Layout 1             |
| 1985   | Layout 1             |
| 1980   | Layout 1             |
| 1969   | Layout 1             |
| 1964   | Layout 1             |
| 1958   | Layout 1             |
| 1950   | Layout 1             |
| 1945   | Layout 1             |
| 1937   | Layout 1             |
| 1933   | Layout 1             |
| 1927   | Layout 1             |
| 1921   | Layout 1             |
| 1914   | Layout 1             |
| 1908   | Layout 1             |
| 1897   | Layout 1             |
| 1892   | Layout 1             |
| 1886   | Layout 1             |
| 1881   | Layout 1             |
| 1871   | Layout 1             |
| 1866   | Layout 1             |
| 1862   | Layout 1             |
| 1854   | Layout 1             |
| 1846   | Layout 1             |
| 1838   | Layout 1             |
| 1832   | Layout 1             |
| 1826   | Layout 1             |
| 1822   | Layout 1             |
| 1818   | Layout 1             |
| 1804   | Layout 1             |
| 1794   | Layout 1             |
| 1790   | Layout 1             |
| 1784   | Layout 1             |
| 1774   | Layout 1             |
| 1771   | Layout 1             |
| 1762   | Layout 1             |
| 1759   | Layout 1             |
| 1754   | Layout 1             |
| 1749   | Layout 1             |
| 1743   | Layout 1             |
| 1737   | Layout 1             |
| 1731   | Layout 1             |
| 1725   | Layout 1             |
| 1717   | Layout 1             |
| 1710   | Layout 1             |
| 1704   | Layout 1             |
| 1698   | Layout 1             |
| 1690   | Layout 1             |
| 1685   | Layout 1             |
| 1680   | Layout 1             |
| 1674   | Layout 1             |
| 1668   | Layout 1             |
| 1659   | Layout 1             |
| 1649   | Layout 1             |
| 1642   | Layout 1             |
| 1636   | Layout 1             |
| 1628   | Layout 1             |
| 1622   | Layout 1             |
| 1614   | Layout 1             |
| 1608   | Layout 1             |
| 1602   | Layout 1             |
| 1598   | Layout 1             |
| 1594   | Layout 1             |
| 1590   | Layout 1             |
| 1587   | Layout 1             |
| 1584   | Layout 1             |
| 1579   | Layout 1             |
| 1572   | Layout 1             |
| 1565   | Layout 1             |
| 1559   | Layout 1             |
| 1554   | Layout 1             |
| 1547   | Layout 1             |
| 1537   | Layout 1             |
| 1529   | Layout 1             |
| 1524   | Layout 1             |
| 1519   | Layout 1             |
| 1509   | Layout 1             |
| 1506   | Layout 1             |
| 1504   | Layout 1             |
| 1500   | Layout 1             |
| 1493   | Layout 1             |
| 1489   | Layout 1             |
| 1485   | Layout 1             |
| 1481   | Layout 1             |
| 1474   | Layout 1             |
| 1466   | Layout 1             |
| 1462   | Layout 1             |
| 1459   | Layout 1             |
| 1453   | Layout 1             |
| 1450   | Layout 1             |
| 1445   | Layout 1             |
| 1439   | Layout 1             |
| 1433   | Layout 1             |
| 1430   | Layout 1             |
| 1426   | Layout 1             |
| 1421   | Layout 1             |
| 1417   | Layout 1             |
| 1416   | Layout 1             |
| 1409   | Layout 1             |
| 1405   | Layout 1             |
| 1401   | Layout 1             |
| 1396   | Layout 1             |
| 1391   | Layout 1             |
| 1390   | Layout 1             |
| 1386   | Layout 1             |
| 1381   | Layout 1             |
| 1379   | Layout 1             |
| 1372   | Layout 1             |
| 1366   | Layout 1             |
| 1364   | Layout 1             |
| 1363   | Layout 1             |
| 1360   | Layout 1             |
| 1358   | Layout 1             |
| 1355   | Layout 1             |
| 1351   | Layout 1             |
| 1348   | Layout 1             |
| 1346   | Layout 1             |
| 1341   | No documented layout |
| 1340   | No documented layout |
| 1338   | No documented layout |
| 1335   | No documented layout |
| 1333   | No documented layout |
| 1329   | No documented layout |
| 1327   | No documented layout |
| 1324   | No documented layout |
| 1321   | No documented layout |
| 1319   | No documented layout |
| 1318   | No documented layout |
| 1316   | No documented layout |
| 1313   | No documented layout |
| 1311   | No documented layout |
| 1309   | No documented layout |
| 1304   | No documented layout |
| 1292   | No documented layout |
| 1286   | No documented layout |
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
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

| File                              | Required | Role                                                                            |
| --------------------------------- | -------- | ------------------------------------------------------------------------------- |
| `intimacyrelationoffset.dbss`     | Optional | `npc_key -> (offset, size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`             | Optional | NPC names (type 6), knowledge names (type 34) and the record's texts (type 23)  |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A record count, then the records back
to back; the file ends after the last record.

| Offset  | Type          | Field   | Notes                                     |
| ------- | ------------- | ------- | ----------------------------------------- |
| `+0x00` | u32           | count   | Number of NPCs; `2206` on client 3483     |
| `+0x04` | Record[count] | records | See Record                                |

### Record (variable: 2 bytes + row)

| Offset  | Type | Field      | Notes                               |
| ------- | ---- | ---------- | ----------------------------------- |
| `+0x00` | u16  | key_prefix | Equals `npc_key`                    |
| `+0x02` | Row  | row        | The offset row points at this field |

### Row (variable: 38 bytes + texts)

| Offset                     | Type      | Field                          | Notes |
| -------------------------- | --------- | ------------------------------ | ----- |
| `+0x00`                    | u16       | npc_key                        | NPC character key (LOC type 6); every key has a LOC type 6 name on client 3483 |
| `+0x02`                    | str16     | covered_dialog_kr              | Korean line while the knowledge cannot be gained yet; LOC type 23 `(npc_key, 0)`. Lines that send the player to another NPC first open with `{Position(x, y, z)}` |
| `covered_dialog_kr+0x00`   | str8      | discover_cutscene              | `.pas` cutscene played on discovery (`CS_Velia_01_Lilia_0001.pas`); set on 16 of 2,206 rows of client 3483 |
| `discover_cutscene+0x00`   | str16     | discover_dialog_kr             | Korean line on discovery, often opening with `{AudioVoice(<voice>)}`; LOC type 23 `(npc_key, 1)` |
| `discover_dialog_kr+0x00`  | str16     | discover_function              | Script run on discovery: `Pushknowledge(<knowledge key>,0)` with an optional `;`, spelled in three cases; empty on 28 rows of client 3483 |
| `discover_function+0x00`   | str16[5]  | discover_conditions            | Condition string of each `discover_dialogs_kr` line: `0` where the line is set, empty where it is not (client 3483) |
| `discover_conditions+0x00` | str16[5]  | discover_dialogs_kr            | Five more Korean lines; line `n` (from 1) is LOC type 23 `(npc_key, n + 1)` |
| `discover_dialogs_kr+0x00` | u32       | unknown_discover_dialogs_kr_00 | `0` on every row of clients 1784 and 3483 |

The LOC type 23 key is `(npc_key, 0, 0, slot)`: slot `0` is
`covered_dialog_kr`, `1` is `discover_dialog_kr` and `2` to `6` are the five
`discover_dialogs_kr`. On client 3483 every non-empty text has its LOC row.

### `intimacyrelationoffset.dbss`

Bare offset table into `intimacyrelation.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                      |
| ------- | ----------------- | ----- | ------------------------------------------ |
| `+0x00` | u32               | count | Equals the `intimacyrelation.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                             |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                   |
| ------- | ---- | ----------- | ----------------------------------------------------------------------- |
| `+0x00` | u16  | npc_key     | Key of the record it points at                                          |
| `+0x02` | u32  | data_offset | Absolute offset in `intimacyrelation.dbss` of the row, past the key prefix |
| `+0x06` | u32  | data_size   | Row size in bytes, without the key prefix                               |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; read in offset order they cover the main file
from `+0x04` to its end, each record's key prefix included (clients 1784
and 3483).

## Layout 1

### Row (variable: 42 bytes + texts)

A u32 `npc_importance` sits between `discover_function` and
`discover_conditions`.

| Offset                     | Type     | Field                          | Notes |
| -------------------------- | -------- | ------------------------------ | ----- |
| `+0x00`                    | u16      | npc_key                        |       |
| `+0x02`                    | str16    | covered_dialog_kr              |       |
| `covered_dialog_kr+0x00`   | str8     | discover_cutscene              |       |
| `discover_cutscene+0x00`   | str16    | discover_dialog_kr             |       |
| `discover_dialog_kr+0x00`  | str16    | discover_function              |       |
| `discover_function+0x00`   | u32      | npc_importance                 | `100000` on 1,390 of 1,446 rows of client 1784, else `200000`, `300000` or `500000` |
| `discover_function+0x04`   | str16[5] | discover_conditions            |       |
| `discover_conditions+0x00` | str16[5] | discover_dialogs_kr            |       |
| `discover_dialogs_kr+0x00` | u32      | unknown_discover_dialogs_kr_00 |       |

## Field Names

The 2016 `gc::IntimacyRelationStaticStatus` holds `_conditionList` (five
`gc::DlgConditionList`), `_conditionStringList` and `_discoverDialogList`
(five wide strings each), `_coveredDialog` (wide), `_discoverCutScene`
(narrow, as the `str8` here), `_discoverDialog` (wide), `_discoverExecutes`
(a `gc::DlgCommonExecute` list), `_key` (u16) and `_supportPointPercent`
(i32). The `NpcRelation` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `NpcKey`, `NPC_Importance`, `NpcIcon`,
`CoveredDialog`, `DiscoverDialog`, `DiscoverFunction`, `DiscoverCutScene`
and `DiscoverCondition1` to `5` with `DiscoverDialog1` to `5`, 1,643 rows.
Matched by `NpcKey`, empty cells (`<null>`) as empty strings:

| Field               | Column                          | Same value (client 1784) | Same value (client 3483) |
| ------------------- | ------------------------------- | ------------------------ | ------------------------ |
| npc_key             | `NpcKey`                        | 1,446 of 1,446           | 1,592 of 1,592           |
| covered_dialog_kr   | `CoveredDialog`                 | 1,446 of 1,446           | 1,574 of 1,592           |
| discover_cutscene   | `DiscoverCutScene`              | 1,446 of 1,446           | 1,585 of 1,592           |
| discover_dialog_kr  | `DiscoverDialog`                | 1,446 of 1,446           | 1,525 of 1,592           |
| discover_function   | `DiscoverFunction`              | 1,446 of 1,446           | 1,584 of 1,592           |
| discover_conditions | `DiscoverCondition1` to `5`     | 1,446 of 1,446 each      | 1,577 to 1,584 of 1,592  |
| discover_dialogs_kr | `DiscoverDialog1` to `5`        | 1,443 to 1,446 of 1,446  | 1,562 to 1,584 of 1,592  |
| npc_importance      | `NPC_Importance`                | 1,446 of 1,446           | (Layout 2 has no field)  |

The client 3483 misses are edited texts and scripts (`Pushknowledge(372,0);`
where the sheet has no `;`). `NpcIcon` (`Icon/Quest/Messien.dds` on every
row) is not compiled. The client Lua of client 3483 reads nothing of this
table.

## Notes

- `discover_function` names a knowledge with a LOC type 34 name on 2,177
  of the 2,178 rows that set it; on 2,153 rows that name is the NPC's own
  LOC type 6 name (client 3483).
- LOC type 23 holds texts for 103 NPC keys with no row here (client 3483).
- The `covered_dialog_kr` lines that send the player to another NPC end
  with a note, in the English LOC of client 3483 (Zaaira, `40002`): "※ You
  must meet a certain requirement to obtain this NPC's knowledge. Visit the
  NPC marked on the world map, then return to acquire the knowledge." That
  is the line shown while the knowledge is covered.
- `discover_dialogs_kr` line 1 repeats `discover_dialog_kr` on 17 of the
  371 rows that set it (client 3483).

## Open Questions

### What the Last u32 Holds

`unknown_discover_dialogs_kr_00` is `0` on every row of clients 1784 and
3483. The 2016 struct has one i32 member, `_supportPointPercent`, and Layout
1 has two u32 fields: `npc_importance` (the `NPC_Importance` column by
value) and this one. Which of the two was `_supportPointPercent`, and what
the client does with it, is open.

### What a Condition String Selects

`discover_conditions` holds `0` exactly where its line is set. The 2016
struct parses each string into a `gc::DlgConditionList`; whether `0` means
"no condition" or a condition kind, and when the client shows each of the
five lines, is open.
