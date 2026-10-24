# `hardcorecharacterstatstaticstatus.bss` Format

## Purpose

One stat body per class type, in the layout of the
[experience.bss](experience_bss.md) level records. The name ties it to the
Hardcore server (`ToClient_isHardCoreCharacter` in the client Lua), which LOC
type 37 says needs a level 60+ character on a normal server. On client 3464
every row equals the `experience.bss` level 60 body: AP `+1` and DP `+1`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records              | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | -------------------- | --------- |
| 1      | 3326 and later | 3483    | `hardcorecharacterstatstaticstatus.bss` | 9,474 | 47 Stat Body, 47 Row | 200       |

| Layout | File                                    | Known           | Unknown         |
| ------ | --------------------------------------- | --------------- | --------------- |
| 1      | `hardcorecharacterstatstaticstatus.bss` | 2,142 B (22.6%) | 7,332 B (77.4%) |

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
| 3321   | No documented layout |
| 3314   | No documented layout |
| 3303   | No documented layout |
| 3302   | No documented layout |
| 3293   | No documented layout |
| 3283   | No documented layout |
| 3275   | No documented layout |
| 3267   | No documented layout |
| 3258   | No documented layout |
| 3251   | No documented layout |
| 3242   | No documented layout |
| 3235   | No documented layout |
| 3229   | No documented layout |
| 3212   | No documented layout |
| 3203   | No documented layout |
| 3193   | No documented layout |
| 3186   | No documented layout |
| 3177   | No documented layout |
| 3169   | No documented layout |
| 3158   | No documented layout |
| 3151   | No documented layout |
| 3144   | No documented layout |
| 3133   | No documented layout |
| 3125   | No documented layout |
| 3118   | No documented layout |
| 3111   | No documented layout |
| 3103   | No documented layout |
| 3095   | No documented layout |
| 3086   | No documented layout |
| 3072   | No documented layout |
| 3062   | No documented layout |
| 3052   | No documented layout |
| 3045   | No documented layout |
| 3037   | No documented layout |
| 3030   | No documented layout |
| 3021   | No documented layout |
| 3012   | No documented layout |
| 3002   | No documented layout |
| 2995   | No documented layout |
| 2987   | No documented layout |
| 2978   | No documented layout |
| 2970   | No documented layout |
| 2959   | No documented layout |
| 2951   | No documented layout |
| 2942   | No documented layout |
| 2935   | No documented layout |
| 2932   | No documented layout |
| 2923   | No documented layout |
| 2919   | No documented layout |
| 2907   | No documented layout |
| 2900   | No documented layout |
| 2891   | No documented layout |
| 2882   | No documented layout |
| 2872   | No documented layout |
| 2863   | No documented layout |
| 2855   | No documented layout |
| 2849   | No documented layout |
| 2844   | No documented layout |
| 2834   | No documented layout |
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

The file is self-contained. The handler reads class names through the shared
LOC lookup:

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Class names (LOC type 21, `str_id1` = class type) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with no row count after the magic: the rows start at `+0x04`
and fill the space up to the string table.

| Offset              | Type               | Field        | Notes                                                  |
| ------------------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                           |
| `+0x04`             | Row[..table_start] | rows         | 47 rows (class types 0 to 46) on client 3464; see Row  |
| `rows+0x00`         | String Table       | string_table | See String Table                                       |
| `EOF-0x08`          | u32                | table_start  | Offset of the string table, where the rows end         |
| `EOF-0x04`          | u32                | zero         | Always 0                                               |

On client 3464 the 47 rows end at `0x24EB`, the stored `table_start`. The
string table holds one wide string, `1D1`, as in `experience.bss`.

### Row (201 bytes)

Fields are unaligned.

| Offset  | Type      | Field      | Notes                                                        |
| ------- | --------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8        | class_type | Equals the row index; the class type `getClassType()` returns |
| `+0x01` | Stat Body | stats      | The [experience.bss](experience_bss.md) Stat Body            |

The body fields (`max_hp`, `max_mp`, the luck and speed limits, the
`unknown_*` fields, `ap_bonus` and `dp_bonus`) keep the names and the body-relative offsets of the
`experience.bss` Stat Body table; `max_hp` and `max_mp` hold the `1.0` and `1`
placeholders here too.

### Stat Body (200 bytes)

The [experience.bss](experience_bss.md) Stat Body, read by
`_bss/experience/stat_body.py`. Offsets are from the start of the body, `+0x01`
in a row.

| Offset  | Type      | Field               | Notes                                     |
| ------- | --------- | ------------------- | ----------------------------------------- |
| `+0x00` | bytes[4]  | unknown_00          | Always `0` (client 3464)                  |
| `+0x04` | f32       | max_hp              | `1.0` placeholder                         |
| `+0x08` | u32       | max_mp              | `1` placeholder                           |
| `+0x0C` | bytes[20] | unknown_0c          | Always `0` (client 3464)                  |
| `+0x20` | f32       | unknown_20          | `1.0` on every row (client 3464)          |
| `+0x24` | bytes[20] | unknown_24          | Always `0` (client 3464)                  |
| `+0x38` | u32       | max_critical_rate   | `0` on every row (client 3464)            |
| `+0x3C` | u32       | max_drop_item_luck  | `5` on every row (client 3464)            |
| `+0x40` | u32       | max_fishing_luck    | `5` on every row (client 3464)            |
| `+0x44` | u32       | max_collection_luck | `5` on every row (client 3464)            |
| `+0x48` | bytes[8]  | unknown_48          | Always `0` (client 3464)                  |
| `+0x50` | f32       | unknown_50          | `1.0` on every row (client 3464)          |
| `+0x54` | bytes[16] | unknown_54          | Always `0` (client 3464)                  |
| `+0x64` | u32[3]    | max_varied_speed    | Attack, movement and casting speed limits; `5, 5, 5` on every row (client 3464) |
| `+0x70` | f32       | unknown_70          | `1.0` on every row (client 3464)          |
| `+0x74` | f32       | ap_bonus            | AP `+1` on every row (client 3464)        |
| `+0x78` | f32       | dp_bonus            | DP `+1` on every row (client 3464)        |
| `+0x7C` | bytes[76] | unknown_7c          | Always `0` (client 3464)                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                  |
| ------- | ------------------ | ------------ | -------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                      |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries                    |

## Notes

- On client 3464 all 47 bodies are byte-identical and equal the
  `experience.bss` level 60 to 130 body, the one with both bonuses.
- The table has a row for every class type, while the LOC type 37 server
  text (id `970407542`) opens Hardcore characters to four classes: Warrior,
  Ranger, Sorceress and Berserker. The class list that
  `ToClient_getHardCorePossbieClassFromIndex()` returns in
  `panel_lobby_classselect_renew.lua` is the `possible_class_types` list of
  [`hardcorechanneletcoptionstaticstatus.bss`](hardcorechanneletcoptionstaticstatus_bss.md),
  29 class types on client 3474.
- The two `5, 5, 5` triads are the drop item, fishing and collection luck
  limits and `max_varied_speed`, named in the
  [experience.bss](experience_bss.md#field-names) Field Names.
- bdo-data-extractor describes the same 201-byte rows and the level 60
  match.
- The parser is `_bss/hardcorecharacterstatstaticstatus/parser.py`; it reads
  the body through `_bss/experience/stat_body.py`.

## Open Questions

### What Reads the Table

No client Lua names the file or a function that returns its values. The
Hardcore basic info panel (`panel_characterinfo_hardcore_basic_all_3.lua`,
`FromClient_CharInfoBasic_HardCore_All_BattleStatUpdate`) shows total AP and
DP through `ToClient_getOffence()` and `ToClient_getDefence()`, the same
getters the normal panel calls, so a Hardcore character's totals do not show
whether the server adds this row in place of the `experience.bss` record.
Garmoth's Hardcore PvP Server guide (pre-season, March 2025) lists a level 63
start and Combat EXP as unavailable. Level 63 falls in the `experience.bss`
level 60 to 130 range, whose body equals every row here, so both readings give
the same AP and DP. The client data holds no starting level: the lobby reads
the entry level from `ToClient_isHardCoreChannelEnterPossibleLevel()`.
