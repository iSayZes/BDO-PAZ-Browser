# `skillexperience.dbss` Format

## Purpose

EXP table of the combat skill points: the Skill EXP a character needs to go from one skill point level to the next, from level 0 to the max level in [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md). Companion `skillexperienceoffset.dbss` lists where every row sits. [guildskillexperience](guildskillexperience_dbss.md) (guild points) and [productexperience](productexperience_dbss.md) (life skill points) use the same container with other rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ------ | ---------------- | --------- |
| 1      | 1276 and later | 3483    | `skillexperience.dbss`       | 32,020 | 2,001 Level Row  | 16        |
| 1      | 1276 and later | 3483    | `skillexperienceoffset.dbss` | 20,014 | 2,001 Offset Row | 10        |

| Layout | File                         | Known             | Unknown    |
| ------ | ---------------------------- | ----------------- | ---------- |
| 1      | `skillexperience.dbss`       | 32,020 B (100.0%) | 0 B (0.0%) |
| 1      | `skillexperienceoffset.dbss` | 20,014 B (100.0%) | 0 B (0.0%) |

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
| 2774   | Layout 1 |
| 2765   | Layout 1 |
| 2756   | Layout 1 |
| 2750   | Layout 1 |
| 2743   | Layout 1 |
| 2736   | Layout 1 |
| 2726   | Layout 1 |
| 2717   | Layout 1 |
| 2709   | Layout 1 |
| 2703   | Layout 1 |
| 2695   | Layout 1 |
| 2684   | Layout 1 |
| 2672   | Layout 1 |
| 2665   | Layout 1 |
| 2657   | Layout 1 |
| 2649   | Layout 1 |
| 2644   | Layout 1 |
| 2637   | Layout 1 |
| 2629   | Layout 1 |
| 2619   | Layout 1 |
| 2612   | Layout 1 |
| 2606   | Layout 1 |
| 2602   | Layout 1 |
| 2601   | Layout 1 |
| 2592   | Layout 1 |
| 2583   | Layout 1 |
| 2575   | Layout 1 |
| 2567   | Layout 1 |
| 2560   | Layout 1 |
| 2553   | Layout 1 |
| 2545   | Layout 1 |
| 2538   | Layout 1 |
| 2529   | Layout 1 |
| 2519   | Layout 1 |
| 2513   | Layout 1 |
| 2510   | Layout 1 |
| 2507   | Layout 1 |
| 2503   | Layout 1 |
| 2498   | Layout 1 |
| 2492   | Layout 1 |
| 2487   | Layout 1 |
| 2480   | Layout 1 |
| 2474   | Layout 1 |
| 2468   | Layout 1 |
| 2460   | Layout 1 |
| 2453   | Layout 1 |
| 2444   | Layout 1 |
| 2438   | Layout 1 |
| 2434   | Layout 1 |
| 2429   | Layout 1 |
| 2421   | Layout 1 |
| 2414   | Layout 1 |
| 2407   | Layout 1 |
| 2401   | Layout 1 |
| 2397   | Layout 1 |
| 2393   | Layout 1 |
| 2384   | Layout 1 |
| 2378   | Layout 1 |
| 2372   | Layout 1 |
| 2358   | Layout 1 |
| 2352   | Layout 1 |
| 2347   | Layout 1 |
| 2343   | Layout 1 |
| 2335   | Layout 1 |
| 2327   | Layout 1 |
| 2324   | Layout 1 |
| 2319   | Layout 1 |
| 2313   | Layout 1 |
| 2308   | Layout 1 |
| 2302   | Layout 1 |
| 2295   | Layout 1 |
| 2290   | Layout 1 |
| 2284   | Layout 1 |
| 2276   | Layout 1 |
| 2269   | Layout 1 |
| 2259   | Layout 1 |
| 2250   | Layout 1 |
| 2243   | Layout 1 |
| 2235   | Layout 1 |
| 2229   | Layout 1 |
| 2224   | Layout 1 |
| 2218   | Layout 1 |
| 2215   | Layout 1 |
| 2207   | Layout 1 |
| 2203   | Layout 1 |
| 2196   | Layout 1 |
| 2192   | Layout 1 |
| 2189   | Layout 1 |
| 2183   | Layout 1 |
| 2179   | Layout 1 |
| 2171   | Layout 1 |
| 2163   | Layout 1 |
| 2156   | Layout 1 |
| 2151   | Layout 1 |
| 2147   | Layout 1 |
| 2142   | Layout 1 |
| 2138   | Layout 1 |
| 2134   | Layout 1 |
| 2130   | Layout 1 |
| 2122   | Layout 1 |
| 2107   | Layout 1 |
| 2098   | Layout 1 |
| 2089   | Layout 1 |
| 2081   | Layout 1 |
| 2073   | Layout 1 |
| 2067   | Layout 1 |
| 2063   | Layout 1 |
| 2059   | Layout 1 |
| 2052   | Layout 1 |
| 2044   | Layout 1 |
| 2039   | Layout 1 |
| 2032   | Layout 1 |
| 2025   | Layout 1 |
| 2011   | Layout 1 |
| 2005   | Layout 1 |
| 2000   | Layout 1 |
| 1996   | Layout 1 |
| 1991   | Layout 1 |
| 1985   | Layout 1 |
| 1980   | Layout 1 |
| 1969   | Layout 1 |
| 1964   | Layout 1 |
| 1958   | Layout 1 |
| 1950   | Layout 1 |
| 1945   | Layout 1 |
| 1937   | Layout 1 |
| 1933   | Layout 1 |
| 1927   | Layout 1 |
| 1921   | Layout 1 |
| 1914   | Layout 1 |
| 1908   | Layout 1 |
| 1897   | Layout 1 |
| 1892   | Layout 1 |
| 1886   | Layout 1 |
| 1881   | Layout 1 |
| 1871   | Layout 1 |
| 1866   | Layout 1 |
| 1862   | Layout 1 |
| 1854   | Layout 1 |
| 1846   | Layout 1 |
| 1838   | Layout 1 |
| 1832   | Layout 1 |
| 1826   | Layout 1 |
| 1822   | Layout 1 |
| 1818   | Layout 1 |
| 1804   | Layout 1 |
| 1794   | Layout 1 |
| 1790   | Layout 1 |
| 1784   | Layout 1 |
| 1774   | Layout 1 |
| 1771   | Layout 1 |
| 1762   | Layout 1 |
| 1759   | Layout 1 |
| 1754   | Layout 1 |
| 1749   | Layout 1 |
| 1743   | Layout 1 |
| 1737   | Layout 1 |
| 1731   | Layout 1 |
| 1725   | Layout 1 |
| 1717   | Layout 1 |
| 1710   | Layout 1 |
| 1704   | Layout 1 |
| 1698   | Layout 1 |
| 1690   | Layout 1 |
| 1685   | Layout 1 |
| 1680   | Layout 1 |
| 1674   | Layout 1 |
| 1668   | Layout 1 |
| 1659   | Layout 1 |
| 1649   | Layout 1 |
| 1642   | Layout 1 |
| 1636   | Layout 1 |
| 1628   | Layout 1 |
| 1622   | Layout 1 |
| 1614   | Layout 1 |
| 1608   | Layout 1 |
| 1602   | Layout 1 |
| 1598   | Layout 1 |
| 1594   | Layout 1 |
| 1590   | Layout 1 |
| 1587   | Layout 1 |
| 1584   | Layout 1 |
| 1579   | Layout 1 |
| 1572   | Layout 1 |
| 1565   | Layout 1 |
| 1559   | Layout 1 |
| 1554   | Layout 1 |
| 1547   | Layout 1 |
| 1537   | Layout 1 |
| 1529   | Layout 1 |
| 1524   | Layout 1 |
| 1519   | Layout 1 |
| 1509   | Layout 1 |
| 1506   | Layout 1 |
| 1504   | Layout 1 |
| 1500   | Layout 1 |
| 1493   | Layout 1 |
| 1489   | Layout 1 |
| 1485   | Layout 1 |
| 1481   | Layout 1 |
| 1474   | Layout 1 |
| 1466   | Layout 1 |
| 1462   | Layout 1 |
| 1459   | Layout 1 |
| 1453   | Layout 1 |
| 1450   | Layout 1 |
| 1445   | Layout 1 |
| 1439   | Layout 1 |
| 1433   | Layout 1 |
| 1430   | Layout 1 |
| 1426   | Layout 1 |
| 1421   | Layout 1 |
| 1417   | Layout 1 |
| 1416   | Layout 1 |
| 1409   | Layout 1 |
| 1405   | Layout 1 |
| 1401   | Layout 1 |
| 1396   | Layout 1 |
| 1391   | Layout 1 |
| 1390   | Layout 1 |
| 1386   | Layout 1 |
| 1381   | Layout 1 |
| 1379   | Layout 1 |
| 1372   | Layout 1 |
| 1366   | Layout 1 |
| 1364   | Layout 1 |
| 1363   | Layout 1 |
| 1360   | Layout 1 |
| 1358   | Layout 1 |
| 1355   | Layout 1 |
| 1351   | Layout 1 |
| 1348   | Layout 1 |
| 1346   | Layout 1 |
| 1341   | Layout 1 |
| 1340   | Layout 1 |
| 1338   | Layout 1 |
| 1335   | Layout 1 |
| 1333   | Layout 1 |
| 1329   | Layout 1 |
| 1327   | Layout 1 |
| 1324   | Layout 1 |
| 1321   | Layout 1 |
| 1319   | Layout 1 |
| 1318   | Layout 1 |
| 1316   | Layout 1 |
| 1313   | Layout 1 |
| 1311   | Layout 1 |
| 1309   | Layout 1 |
| 1304   | Layout 1 |
| 1292   | Layout 1 |
| 1286   | Layout 1 |
| 1280   | Layout 1 |
| 1276   | Layout 1 |
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

| File                          | Required | Role                                                                         |
| ----------------------------- | -------- | ---------------------------------------------------------------------------- |
| `skillexperienceoffset.dbss`  | Required | `level -> (offset, size)` of every row                                       |
| `skillexperiencemaxlevel.bss` | Optional | Max level, see [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md)     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                 | Field     | Notes                                                |
| ------- | -------------------- | --------- | ---------------------------------------------------- |
| `+0x00` | u32                  | row_count | Number of rows; 2,001 (levels 0 to 2000) on client 3464 |
| `+0x04` | Level Row[row_count] | rows      | `row_count` rows of 16 bytes, not in level order     |

The rows fill the file exactly: 4 + 2,001 x 16 = 32,020 bytes on client 3464.

### Level Row (16 bytes)

| Offset  | Type | Field                   | Notes                                                    |
| ------- | ---- | ----------------------- | -------------------------------------------------------- |
| `+0x00` | u16  | level                   | Skill point level; equals the offset row's key           |
| `+0x02` | u16  | acquired_point          | `0` on every row (client 3474)                           |
| `+0x04` | u32  | exp                     | EXP to go from `level` to `level + 1` (Notes)            |
| `+0x08` | u32  | require_exp_limit       | `0` on every row (client 3474)                           |
| `+0x0C` | u32  | quest_require_exp_limit | `0` on every row (client 3474)                           |

The server rejects a row whose `exp`, `require_exp_limit` or `quest_require_exp_limit` is below 0 (Field Names), so the three fit an i32.

### `skillexperienceoffset.dbss`

Index into `skillexperience.dbss`: the bare u16 offset table of `_common/pabr_offset.py` (`parse_bare_offset_rows`), with no `PABR` magic and no trailer.

| Offset  | Type                  | Field     | Notes                                         |
| ------- | --------------------- | --------- | --------------------------------------------- |
| `+0x00` | u32                   | row_count | Equals the `skillexperience.dbss` row count   |
| `+0x04` | Offset Row[row_count] | rows      | `row_count` rows of 10 bytes                  |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                             |
| ------- | ---- | ----------- | ----------------------------------------------------------------- |
| `+0x00` | u16  | level       | Level of the row it points at                                     |
| `+0x02` | u32  | data_offset | Absolute byte offset of the row's `level` in `skillexperience.dbss` |
| `+0x06` | u32  | data_size   | Always 16                                                         |

Neither file keeps level order: the offset rows start with levels 0, 399, 1052, and the first data row (`0x04`) is level 1052. The parser reads every row through the offset table, checks that the row's `level` matches the offset row's key, and returns the rows sorted by level.

## Field Names

The names come from the server dump of a private server on client 1784 (`Instance_dumpFull.exe`). It loads the row twice into one static status: from the client's `skillexperience.dbss` (row reader at VA `0x140c84990`) and from the `SkillPointEXP_Table_New` developer sheet (column reads at VA `0x1408c2c87` to `0x1408c2d39`). Both write the same members:

| Field                     | Member  | Read from the file | Sheet column           |
| ------------------------- | ------- | ------------------ | ---------------------- |
| `level`                   | `+0x00` | u16                | `Index`                |
| `acquired_point`          | `+0x02` | u16                | `AquiredPoint`         |
| `exp`                     | `+0x04` | u32                | `RequireEXP`           |
| `require_exp_limit`       | `+0x08` | u32                | `RequireSkillExpLimit` |
| `quest_require_exp_limit` | `+0x0C` | u32                | `QuestRequireExpLimit` |

The row check (from VA `0x140c84702`) stores the key, then tests the three EXP members in member order and logs, for the first one below 0, "skill point level key(%#): (%#) EXP is not defined", "... the current level's max (%#) EXP is not defined" or "... the current level's quest max (%#) EXP is not defined". Only a row that passes gets a flag at member `+0x10`, which the file does not store. [guildskillexperience](guildskillexperience_dbss.md) and [productexperience](productexperience_dbss.md) store that flag as their last byte (`is_exp_defined`).

The sheet and the private server's own `skillexperience.dbss` hold the same 2,001 rows as client 3474: `exp` matches on every level, and `AquiredPoint`, `RequireSkillExpLimit` and `QuestRequireExpLimit` are `0` on every row of all three. Earlier versions of this doc read `+0x00` as a u32 level and `+0x04` as a u64 EXP; with those zero fields the values are the same, so only the field bounds changed.

## Notes

- The client has three skill point pools, numbered by `ToClient_getSkillPointInfo(type)`: `0` combat skill points (`panel_window_skillgroup_all_1.luac`), `2` life skill points (`panel_selfplayerexpgage.luac`) and `3` guild points (`panel_guildskill_all_1.luac`). `acquire.luac` names the matching level-up notices `GainCombatSkillPoint`, `GainProductSkillPoint` and `GainGuildSkillPoint`, shown with the `GAME` keys `ACQUIRE_OBJECTMESSAGE_2` ("Combat Skill Points Obtained"), `_1` ("Life Skill Points Obtained") and `_3` ("Guild Points Obtained"). The file stems follow the same names: `skillexperience`, `productexperience`, `guildskillexperience`.
- The skill window draws the bar as `getSkillPointExperience() / getSkillPointNeedExperience()`, and the guild window as `_currentExp / _nextLevelExp`, so the EXP restarts at 0 on every level, as in [lifeexp](lifeexp_dbss.md). The row direction (row N is the EXP from N to N + 1) follows `lifeexp.dbss`, where a packet capture confirmed it; a capture of the Skill EXP message against this table would flip it if the client divides by the level N + 1 row instead.
- Quest rewards of type `__eRewardSkillExp` give `_skillExperience` (`panel_dialog_quest_all_1.luac`), shown as "Skill EXP" (`LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP`).
- Curve on client 3464: level N needs 430 + 1,120 x N x (N + 1) EXP up to level 249 (69,720,430), then 557,760 more per level up to level 500 (209,718,190). Levels 501 to 1501 hold that same 209,718,190, and levels 1502 to 2000 ten times it, 2,097,181,900.
- Unlike `lifeexp.dbss` the file has no blocks and the rows open with a u16 level instead of a type byte; the offset table is the bare 10-byte layout that `petexpoffset.dbss` also uses.

## Open Questions

### What the Two EXP Limits Cap

`require_exp_limit` and `quest_require_exp_limit` are `0` on every row of client 3474 and of the 1784 sheet, and the skill window Lua reads only the current and needed EXP (`getSkillPointExperience()`, `getSkillPointNeedExperience()`). The Korean check messages call them the current level's max EXP and quest max EXP; what a non-zero value would cap needs a client where one is set.
