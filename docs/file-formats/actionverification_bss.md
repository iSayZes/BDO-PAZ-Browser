# `actionverification.bss` Format

## Purpose

A list of actions per character: each character key holds action name
hashes, each with an `AbleCallTime` value. On client 3474 the file holds 14
characters and 150 actions. Five are the player classes Warrior (`1`),
Ranger (`2`), Sorcerer (`3`), Tamer (`5`) and Musa (`21`), with one action
each (`BT_WAIT`, `BT_skill_SkyFall`, `BT_skill_ThrustAndSmash_AttQ1`). The
other nine are the hero characters `65002` to `65037` (Jordine, Peony,
Ahon Kirus, Povios, Syaki, Nelydormin, Orwen, Striker, Tamer in LOC type 6),
with 12 to 23 `SHADOW_*` and `BT_ROLL_*` actions each. Each hero key is
`64950` plus one of the class types in
[`actionverificationindex.dbss`](actionverificationindex_dbss.md) (see
Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------------------ | --------- |
| 2      | 1280 and later | 3483    | `actionverification.bss` | 1,304 | 150 Action, 14 Character | 8         |
| 1      | 1220 to 1230   | 1230    | `actionverification.bss` | 100   | 5 Row                    | 16        |

| Layout | File                     | Known            | Unknown      |
| ------ | ------------------------ | ---------------- | ------------ |
| 2      | `actionverification.bss` | 1,304 B (100.0%) | 0 B (0.0%)   |
| 1      | `actionverification.bss` | 60 B (60.0%)     | 40 B (40.0%) |

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
| 2575   | Layout 2             |
| 2567   | Layout 2             |
| 2560   | Layout 2             |
| 2553   | Layout 2             |
| 2545   | Layout 2             |
| 2538   | Layout 2             |
| 2529   | Layout 2             |
| 2519   | Layout 2             |
| 2513   | Layout 2             |
| 2510   | Layout 2             |
| 2507   | Layout 2             |
| 2503   | Layout 2             |
| 2498   | Layout 2             |
| 2492   | Layout 2             |
| 2487   | Layout 2             |
| 2480   | Layout 2             |
| 2474   | Layout 2             |
| 2468   | Layout 2             |
| 2460   | Layout 2             |
| 2453   | Layout 2             |
| 2444   | Layout 2             |
| 2438   | Layout 2             |
| 2434   | Layout 2             |
| 2429   | Layout 2             |
| 2421   | Layout 2             |
| 2414   | Layout 2             |
| 2407   | Layout 2             |
| 2401   | Layout 2             |
| 2397   | Layout 2             |
| 2393   | Layout 2             |
| 2384   | Layout 2             |
| 2378   | Layout 2             |
| 2372   | Layout 2             |
| 2358   | Layout 2             |
| 2352   | Layout 2             |
| 2347   | Layout 2             |
| 2343   | Layout 2             |
| 2335   | Layout 2             |
| 2327   | Layout 2             |
| 2324   | Layout 2             |
| 2319   | Layout 2             |
| 2313   | Layout 2             |
| 2308   | Layout 2             |
| 2302   | Layout 2             |
| 2295   | Layout 2             |
| 2290   | Layout 2             |
| 2284   | Layout 2             |
| 2276   | Layout 2             |
| 2269   | Layout 2             |
| 2259   | Layout 2             |
| 2250   | Layout 2             |
| 2243   | Layout 2             |
| 2235   | Layout 2             |
| 2229   | Layout 2             |
| 2224   | Layout 2             |
| 2218   | Layout 2             |
| 2215   | Layout 2             |
| 2207   | Layout 2             |
| 2203   | Layout 2             |
| 2196   | Layout 2             |
| 2192   | Layout 2             |
| 2189   | Layout 2             |
| 2183   | Layout 2             |
| 2179   | Layout 2             |
| 2171   | Layout 2             |
| 2163   | Layout 2             |
| 2156   | Layout 2             |
| 2151   | Layout 2             |
| 2147   | Layout 2             |
| 2142   | Layout 2             |
| 2138   | Layout 2             |
| 2134   | Layout 2             |
| 2130   | Layout 2             |
| 2122   | Layout 2             |
| 2107   | Layout 2             |
| 2098   | Layout 2             |
| 2089   | Layout 2             |
| 2081   | Layout 2             |
| 2073   | Layout 2             |
| 2067   | Layout 2             |
| 2063   | Layout 2             |
| 2059   | Layout 2             |
| 2052   | Layout 2             |
| 2044   | Layout 2             |
| 2039   | Layout 2             |
| 2032   | Layout 2             |
| 2025   | Layout 2             |
| 2011   | Layout 2             |
| 2005   | Layout 2             |
| 2000   | Layout 2             |
| 1996   | Layout 2             |
| 1991   | Layout 2             |
| 1985   | Layout 2             |
| 1980   | Layout 2             |
| 1969   | Layout 2             |
| 1964   | Layout 2             |
| 1958   | Layout 2             |
| 1950   | Layout 2             |
| 1945   | Layout 2             |
| 1937   | Layout 2             |
| 1933   | Layout 2             |
| 1927   | Layout 2             |
| 1921   | Layout 2             |
| 1914   | Layout 2             |
| 1908   | Layout 2             |
| 1897   | Layout 2             |
| 1892   | Layout 2             |
| 1886   | Layout 2             |
| 1881   | Layout 2             |
| 1871   | Layout 2             |
| 1866   | Layout 2             |
| 1862   | Layout 2             |
| 1854   | Layout 2             |
| 1846   | Layout 2             |
| 1838   | Layout 2             |
| 1832   | Layout 2             |
| 1826   | Layout 2             |
| 1822   | Layout 2             |
| 1818   | Layout 2             |
| 1804   | Layout 2             |
| 1794   | Layout 2             |
| 1790   | Layout 2             |
| 1784   | Layout 2             |
| 1774   | Layout 2             |
| 1771   | Layout 2             |
| 1762   | Layout 2             |
| 1759   | Layout 2             |
| 1754   | Layout 2             |
| 1749   | Layout 2             |
| 1743   | Layout 2             |
| 1737   | Layout 2             |
| 1731   | Layout 2             |
| 1725   | Layout 2             |
| 1717   | Layout 2             |
| 1710   | Layout 2             |
| 1704   | Layout 2             |
| 1698   | Layout 2             |
| 1690   | Layout 2             |
| 1685   | Layout 2             |
| 1680   | Layout 2             |
| 1674   | Layout 2             |
| 1668   | Layout 2             |
| 1659   | Layout 2             |
| 1649   | Layout 2             |
| 1642   | Layout 2             |
| 1636   | Layout 2             |
| 1628   | Layout 2             |
| 1622   | Layout 2             |
| 1614   | Layout 2             |
| 1608   | Layout 2             |
| 1602   | Layout 2             |
| 1598   | Layout 2             |
| 1594   | Layout 2             |
| 1590   | Layout 2             |
| 1587   | Layout 2             |
| 1584   | Layout 2             |
| 1579   | Layout 2             |
| 1572   | Layout 2             |
| 1565   | Layout 2             |
| 1559   | Layout 2             |
| 1554   | Layout 2             |
| 1547   | Layout 2             |
| 1537   | Layout 2             |
| 1529   | Layout 2             |
| 1524   | Layout 2             |
| 1519   | Layout 2             |
| 1509   | Layout 2             |
| 1506   | Layout 2             |
| 1504   | Layout 2             |
| 1500   | Layout 2             |
| 1493   | Layout 2             |
| 1489   | Layout 2             |
| 1485   | Layout 2             |
| 1481   | Layout 2             |
| 1474   | Layout 2             |
| 1466   | Layout 2             |
| 1462   | Layout 2             |
| 1459   | Layout 2             |
| 1453   | Layout 2             |
| 1450   | Layout 2             |
| 1445   | Layout 2             |
| 1439   | Layout 2             |
| 1433   | Layout 2             |
| 1430   | Layout 2             |
| 1426   | Layout 2             |
| 1421   | Layout 2             |
| 1417   | Layout 2             |
| 1416   | Layout 2             |
| 1409   | Layout 2             |
| 1405   | Layout 2             |
| 1401   | Layout 2             |
| 1396   | Layout 2             |
| 1391   | Layout 2             |
| 1390   | Layout 2             |
| 1386   | Layout 2             |
| 1381   | Layout 2             |
| 1379   | Layout 2             |
| 1372   | Layout 2             |
| 1366   | Layout 2             |
| 1364   | Layout 2             |
| 1363   | Layout 2             |
| 1360   | Layout 2             |
| 1358   | Layout 2             |
| 1355   | Layout 2             |
| 1351   | Layout 2             |
| 1348   | Layout 2             |
| 1346   | Layout 2             |
| 1341   | Layout 2             |
| 1340   | Layout 2             |
| 1338   | Layout 2             |
| 1335   | Layout 2             |
| 1333   | Layout 2             |
| 1329   | Layout 2             |
| 1327   | Layout 2             |
| 1324   | Layout 2             |
| 1321   | Layout 2             |
| 1319   | Layout 2             |
| 1318   | Layout 2             |
| 1316   | Layout 2             |
| 1313   | Layout 2             |
| 1311   | Layout 2             |
| 1309   | Layout 2             |
| 1304   | Layout 2             |
| 1292   | Layout 2             |
| 1286   | Layout 2             |
| 1280   | Layout 2             |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
| 1246   | No documented layout |
| 1239   | No documented layout |
| 1230   | Layout 1             |
| 1226   | Layout 1             |
| 1220   | Layout 1             |
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

| File                         | Required | Role                                                          |
| ---------------------------- | -------- | ------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | Character keys with a `characterstatic.dbss` row, for the link |
| `languagedata_en.loc`        | Optional | Character names (LOC type 6, `str_id1` = character key)       |

All multi-byte values are little-endian.

## Layout 2

### File Layout

A `PABR` table of variable-size character entries with an empty string
table.

| Offset                | Type             | Field              | Notes                                         |
| --------------------- | ---------------- | ------------------ | --------------------------------------------- |
| `+0x00`               | char[4]          | magic              | ASCII `PABR`                                  |
| `+0x04`               | u32              | count              | Number of characters; `14` on client 3474     |
| `+0x08`               | Character[count] | characters         | See Character                                 |
| `characters+0x00`     | String Table     | string_table       | Empty string table                            |
| `string_table+0x00`   | u32              | string_table_start | End of the characters, `1292` on client 3474  |
| `string_table+0x04`   | u32              | zero               | `0`                                           |

The characters are in neither key order nor sheet order (`1`, `65002`,
`2`, `65003`, `3`, `65005`, `21`, `5`, `65008` and up on client 3474).

### Character (variable: 6 bytes + actions)

| Offset  | Type                 | Field        | Notes                                              |
| ------- | -------------------- | ------------ | -------------------------------------------------- |
| `+0x00` | u16                  | character_key | Character key (LOC type 6 name); unique in the file; see Notes |
| `+0x02` | u32                  | action_count | Number of actions                                  |
| `+0x06` | Action[action_count] | actions      | See Action                                         |

### Action (8 bytes)

| Offset  | Type | Field          | Notes                                                                 |
| ------- | ---- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | action_hash    | `ascii_key_hash` of the action name (`_common/string_hash.py`); unique within a character |
| `+0x04` | u32  | able_call_time | `AbleCallTime`, the sheet value cut to a whole number (`598.290598` is stored as `598`) |

The actions of a character are not in sheet order either.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

Client 1230 has one action per character and no action hash: 5 rows for
the five player classes of Layout 2, in the same order, each with the same
`able_call_time` as its one Layout 2 action.

### File Layout

| Offset              | Type         | Field              | Notes                                   |
| ------------------- | ------------ | ------------------ | --------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                            |
| `+0x04`             | u32          | count              | Number of rows; `5` on client 1230      |
| `+0x08`             | Row[count]   | rows               | See Row                                 |
| `rows+0x00`         | String Table | string_table       | Empty string table                      |
| `string_table+0x00` | u32          | string_table_start | End of the rows, `88` on client 1230    |
| `string_table+0x04` | u32          | zero               | `0`                                     |

### Row (16 bytes)

| Offset  | Type | Field          | Notes                                    |
| ------- | ---- | -------------- | ---------------------------------------- |
| `+0x00` | u32  | unknown_00     | `8` in every row; see Open Questions     |
| `+0x04` | u32  | unknown_04     | `0` in every row                         |
| `+0x08` | u32  | character_key  | Player class character key               |
| `+0x0C` | u32  | able_call_time | As in Layout 2                           |

## Action Names

The client stores the names only as `action_hash`. The handler names an
action from the 29 action names of the client 1784 sheet (see Field
Names), each hashed with `ascii_key_hash`; an action whose hash is not one
of them shows as hex. On client 3474 all 150 action hashes are one of the
29.

| Character keys  | Action names                                                                 |
| --------------- | ---------------------------------------------------------------------------- |
| `1`, `2`, `5`   | `BT_WAIT`                                                                    |
| `3`             | `BT_skill_SkyFall`                                                           |
| `21`            | `BT_skill_ThrustAndSmash_AttQ1`                                              |
| `65002` to `65037` | `SHADOW_ATTACK_1` to `SHADOW_ATTACK_6`, `SHADOW_ATTACK_1_2`, `SHADOW_ATTACK_F_1` to `SHADOW_ATTACK_F_5`, `SHADOW_ATTACK_L_1` to `SHADOW_ATTACK_L_3`, `SHADOW_ATTACK_L_1_C`, `SHADOW_ATTACK_R_1` to `SHADOW_ATTACK_R_3`, `SHADOW_ATTACK_R_1_C`, `SHADOW_DASHATTACK_1`, `SHADOW_JUMP_ATTACK`, `SHADOW_DASHJUMP_ATTACK`, `BT_ROLL_L`, `BT_ROLL_R`, `BT_ROLL_B` |

## Field Names

The names follow the `ActionVerification_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784, columns `CharacterKey`,
`ActionName` and `AbleCallTime`. All 150 sheet rows are in the client 1784
and 3474 files: the `ascii_key_hash` of each `ActionName` is an
`action_hash` of the row's `CharacterKey`, and its `AbleCallTime`, cut to a
whole number, is the stored `able_call_time` (150 of 150 rows, client
3474). The server dump of the same private server reads the sheet in the
function at `0x1408f0b10`.

The 2016 PDB has no action verification type and the client 519 tables
have no such table.

## Notes

- The client 1784, 1485, 2107, 2519, 3002, 3251 and 3474 files are byte for
  byte the same. Client 794 has no `actionverification.bss`.
- Each hero character key is `64950` plus a class type of
  [`actionverificationindex.dbss`](actionverificationindex_dbss.md):
  `65002` Jordine is class type `52` Jordine, and the LOC names of the two
  agree for Peony, Ahon Kirus, Povios, Syaki, Nelydormin and Orwen as well.
  `65031` (Striker) and `65037` (Tamer) give `81` and `87`, which LOC type
  21 names `[PH] 22` and `[PH] 28`. Class types `61`, `65` and `71` have no
  character in this file.
- On client 3474 the five player class keys have a `characterstatic.dbss`
  row and the nine hero keys have none; every key has a LOC type 6 name.
- `BT_ROLL_L`, `BT_ROLL_R` and `BT_ROLL_B` hold `230` for every hero on
  client 3474 (`230.769231` in the sheet).

## Open Questions

### Unit of `able_call_time`

The sheet values are fractions such as `230.769231` (`3000 / 13`) and
`598.290598`; the stored values are whole numbers from `230` to `6300` on
client 3474. No client Lua file names `ActionVerification` or
`AbleCallTime`, so the unit (milliseconds or another time base) is not
confirmed.

### What the Layout 1 `unknown_00` Holds

Each client 1230 row starts with a u32 `8` and a u32 `0`. The `8` could
be the size of the `character_key` and `able_call_time` pair that follows,
or an action count of another meaning; with five identical rows the
reading cannot be told apart.
