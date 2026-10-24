# `npcsimply.bss` Format

## Purpose

Stores a compact identity table for service and story NPCs. Each row maps a character ID to its primary NPC service role, inline Korean display strings and, for most rows, a `getknowledge(<id>);` action script that links the NPC to a knowledge ID. Names and roles in the user's language come from LOC type `6`, keyed by the same character ID: `str_id4` 0 is the name and 1 the role.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes   | Records          | Row bytes |
| ------ | -------------- | ------- | --------------- | ------- | ---------------- | --------- |
| 1      | 1250 and later | 3483    | `npcsimply.bss` | 210,479 | 2,239 NPC Record | 33        |

| Layout | File            | Known             | Unknown         |
| ------ | --------------- | ----------------- | --------------- |
| 1      | `npcsimply.bss` | 192,567 B (91.5%) | 17,912 B (8.5%) |

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
| 1267   | Layout 1 |
| 1261   | Layout 1 |
| 1256   | Layout 1 |
| 1250   | Layout 1 |
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

None. Names and roles in the user's language come from LOC type `6` (see Purpose).

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

Top-level PABR block with a fixed-width record table followed by an inline string table.

| Offset             | Type              | Field              | Notes                                      |
| ------------------ | ----------------- | ------------------ | ------------------------------------------ |
| `+0x00`            | char[4]           | magic              | ASCII `PABR`                               |
| `+0x04`            | u32               | count              | Number of NPC records (observed: 2,169 in an older extraction, 2,237 in the pre-2026-09-27 fixture, 2,238 in the 2026-09-27 client) |
| `+0x08`            | NPC Record[count] | records            | See NPC Record                             |
| `records+0x00`     | String Table      | string_table       | Counted string table referenced by records |
| `string_table+0x00` | u32               | string_pool_offset | Equals `0x08 + count * 33` (`0x12065`)     |
| `string_table+0x04` | u32               | zero               | Always 0                                   |

The last two fields are the 8-byte trailer. This is the same `[string table][u32 rows_end][u32 0]` tail that `playercharacterstatic.bss` and `characterstaticoffset.dbss` carry after their rows.

### NPC Record (33 bytes)

| Offset  | Type | Field             | Notes                                                                 |
| ------- | ---- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_id      | Character-template key; all 2237 exist in `characterstatic.dbss`; all 2238 have a LOC type `6` name in client 3458, see Notes |
| `+0x02` | u8   | unknown_02        | `1` on 2074 rows; runs of sequential values on related NPCs, see Open Questions |
| `+0x03` | u8   | unknown_03        | Always `0`                                                            |
| `+0x04` | u32  | kind              | Primary `SpawnType` role; 23 observed values in the range 1-40         |
| `+0x08` | u32  | script_ref        | String-pool index of the action script; `getknowledge(...)` on 2161 rows (one spelled `getKnowledge`), the empty string on 76 |
| `+0x0C` | u32  | lease_item_id     | Usually 0; on 58 rows the item key (LOC type `0`) of the `[CP]` item the NPC leases, see Notes |
| `+0x10` | u16  | lease_cost        | Usually 0; the lease cost in contribution points on the same 58 rows as `lease_item_id` |
| `+0x12` | u16  | unknown_12        | Usually `0xFFFF`; 0 on the same 58 rows as `lease_item_id`             |
| `+0x14` | u8   | has_lease_condition | `1` when the NPC's lease dialog option has a condition script (32 of the 58 lease rows), see Notes |
| `+0x15` | u32  | name_ref          | String-pool index for the Korean display name                          |
| `+0x19` | u32  | role_ref          | String-pool index for Korean role/title text; points at the empty string when absent |
| `+0x1D` | u32  | unknown_1d        | Always 0                                                              |

An earlier version of this doc read `+0x00` as a u32 `npc_id`. The high half is `unknown_02`: as a u32 only 20 of 2237 values resolve through LOC, as a u16 all of them do. Earlier versions of this doc also called `lease_item_id` `unknown_id` and then `unknown_0c`, `lease_cost` `unknown_value` and then `unknown_10`, `unknown_12` `sentinel` and `has_lease_condition` `unknown_flag` and then `unknown_14`.

`script_ref`, `name_ref`, and `role_ref` are unaligned u32 values inside the 33-byte row. bdo-data-extractor ([iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)) reads the same references as aligned u32s at `+0x14` and `+0x18` shifted right by 8 (`packedNameRef`, `packedTitleRef`); both readings give the same index on every row, because the byte after each unaligned reference is always 0. `name_ref` is usually `script_ref + 1` (2045 rows).

The `script_ref` string equals the `characterstatic.dbss` action script of the same character on all 2237 rows.

### String Table (variable: 4 bytes + strings)

The string table begins immediately after the fixed record table, at
`string_pool_offset = 0x08 + count * 33`. Observed `string_pool_offset` is
`0x12065` (older extraction: `0x117A1`).

| Offset  | Type               | Field        | Notes                           |
| ------- | ------------------ | ------------ | ------------------------------- |
| `+0x00` | u32                | string_count | Observed: 4746                  |
| `+0x04` | pstr[string_count] | strings      | Counted entries, indexed from 0 |

Every `pstr` entry has a one-byte encoding flag `is_wide` (`1` for UTF-16LE,
`0` for UTF-8) and a u32 byte length, then the payload. There is no
terminator: the next entry starts right after the payload, and the last one
ends exactly at the trailer.

An earlier version of this doc read the flag as an optional marker and the
next entry's `0` flag as a terminator; both readings split the pool the same
way. `exploration.bss` uses the same entry layout, and the parser shares one
reader for both (`handlers/_common/pabr_strings.py`).

Observed pool contents: 2636 UTF-8 strings and 2110 UTF-16LE strings. The pool is not purely 8-bit: every script entry is UTF-16LE. One entry is the empty string (index 34 in the current file, index 0 in the older extraction); absent scripts and roles point at it.

## `kind` Values

`kind` is a `CppEnums.SpawnType` value, the same enum as the 46 role flags in `characterspawntype.dbss`. For all 2237 rows, the `characterspawntype.dbss` flag at index `kind` is set for the same character, so `kind` picks one primary role from that character's flags. Most common values:

| Value | Rows | SpawnType | Typical role text |
| ----- | ---- | --------- | ----------------- |
| 4     | 1197 | `ImportantNpc` | `<탐험 거점 관리>`, `<물물교환원>`, empty |
| 3     | 226  | `ShopMerchant` | `<창고지기>`, `<약초상인>` |
| 5     | 121  | `TradeMerchant` | `<무역 관리>` |
| 2     | 105  | `ItemRepairer` | `<대장장이>`, `<무기상인>` |
| 16    | 97   | `Potion` | `<잡화상인>` |
| 7     | 87   | `Stable` | `<마구간지기>` |
| 20    | 55   | `Collect` | `<재료상인>` |
| 1     | 46   | `SkillTrainer` | `<기술교관>` |
| 8     | 38   | `Wharf` | `<나루터지기>` |
| 25    | 22   | `ItemMarket` | `<거래소장>` |

## Notes

- The record table size is exactly `count * 33` bytes; fixed records end at `0x12065` (`0x12086` in the 2026-09-27 client), and the string table parses exactly up to the 8-byte trailer.
- `script_ref` points to a `getknowledge(<id>);` UTF-16LE string for 2161 of 2237 records.
- `name_ref` and `role_ref` point to Korean UTF-8 strings in the same pool. Role strings are often bracketed labels such as `<과일상인>` or `<거점관리인>`. LOC type `6` `str_id4=1` holds the same role in the user's language on all 1998 rows with a role (`<과일상인>` is `<Fruit Vendor>`), and `<null>` on the 240 rows whose `role_ref` is empty (client 3458).
- Every row's character has `npc_kind` `2` (NPC) in `characterstatic.dbss`.
- `lease_item_id` is the `[CP]` item the NPC leases for contribution points. In client 3458 every one of the 58 values resolves through LOC type `0` to a `[CP]` item: `3001` [CP] Container on the Storage Keepers (and Basquean Ljurik, Bank of Hope), `58008` to `58012` the [CP] fences on Material Vendors, node managers and Old Moon Managers, `16142` [CP] Practice Matchlock, `16143` [CP] Flute, and single items such as `23004` [CP] Kaia Longsword on Kanobas, `693901` [CP] Leight's Hoe on Norma Leight and `45601` / `45602` the Licensed / Acknowledged Adventurer's Seal. `lease_cost` is the same for every NPC with the same item: Container `10`, Strong Fence `10`, Plain Fence `6`, Small Fence `3`, Practice Matchlock `2`, Flute `1`, the Kaia and Nesser gear and Leight's Hoe `50`, Licensed Seal `20`, Acknowledged Seal `60`. Checked in game (2026-09-28): Delorence (`47008`, `3001` / `10`) is a Storage Keeper who leases a [CP] Container for 10 CP.
- The lease itself is an NPC dialog option in `detail_dialog.dbss` (records keyed `1 << 16 | character_id`). Each option stores a condition script, a title such as `[대여] 작은 울타리` ("[Lease] Small Fence"), the dialog text and the action `buyItemByPoint(item, 0, 1, 5, cost)`. `lease_item_id` and `lease_cost` repeat the item and cost of the NPC's first lease option: the item matches on all 58 rows and the cost on 57. Merio (`43501`) is the exception, `2` here and `1` in his dialog; in game his Matchlock lease costs 2 (checked 2026-09-28), the same as the other Matchlock NPCs, so the charged cost follows `lease_cost` and the dialog's `1` is stale. NPCs with several lease options keep only the first here (Kanobas `23004` of his 25 Kaia weapons, Basquean Ljurik the Container and not the Excellent Adventurer's Seal `45603` at 100 CP), and Wale (`40605`) has a Small Fence lease in his dialog but no lease item here.
- `has_lease_condition` is `1` exactly when that option has a condition script, on all 58 lease rows (client 3458). The Containers, Flutes and Matchlocks check that you do not own one yet (`!getitemcount(3001,0)>0;`), the Kaia and Nesser gear add a level, quest and class check, and the fences of Martina Finto (`40024`) and Mercianne Moretti (`41085`) are quest-gated: Martina's reads `!iscontentsgroupopen(0,4017);<or>iscontentsgroupopen(0,4017);!clearquest(21125,64);<or>iscontentsgroupopen(0,4017);clearquest(21125,64);clearquest(21125,74);`, which item databases show as "Not finished quest: Tracking Giath, or finished Tracking Giath and Sands of Time". The fence NPCs with `0` (Zaaira `40002` and the others) have an empty condition.
- Every character has a LOC type `6` name in client 3458. Older clients missed 39 (`47623`, `47753`, `47772` to `47807` and `61267`); the handler shows the Korean `name_ref` for such a row.

## Open Questions

### What does `unknown_02` encode?

It is `1` on 2074 rows (every NPC of the older towns, Velia, Heidel and Calpheon included), `0` on 20 (mostly The Magnus entrances) and `2` on 18 (lore NPCs such as the Kalis Councilors and the Nesser family). In client 3458 the remaining 126 rows form numbered runs on the newer groups, roughly in character ID order:

- the Edania town NPCs `47742` to `47770` hold `5` to `33` (Alustin `5`, Bakora `6`, ... Resh `27`, Zario `29`, ... Clorince `33`), and the node managers `47773` to `47795` continue with `35` to `57`
- the node managers `47675` to `47704` hold `34` to `63`, and the five Thrones `47705` to `47709` `64` to `68`
- the Olvia Academy staff `62480` to `62502` hold `10` to `27`, and its bulletin board `62521` holds `99`. Here the ID order breaks once: Cliff (`62484`) holds `13` and Eileen (`62483`) `14`
- smaller runs: the Vestiges `47801` to `47807` (`100` to `108`) and the stable and wharf managers `50981` to `50989` (`144` to `151`)

The ranges overlap between groups (`35` is Abene in one run and Erhan in another), so it looks like an order within a group. It is not the knowledge order: in all four runs it follows neither the NPCs' card IDs nor their card order in the `mentaltheme.dbss` entry lists, which is the Knowledge window order (in game the Olvia Academy category lists Eileen before Cliff) (the Edania town NPCs are split over themes `355` and `356` while the values run through both). Two readings remain. It may be a sort key for an NPC list: `0` sits only on things never picked from a list (The Magnus entrance wells, the Referees, a Swing), `1` is the default of the older towns, and explicit numbers exist only in newer content. Or it is the authoring order with no visible effect, which would explain how closely it tracks the character IDs. Olvia Academy separates the two: an NPC list (not the Knowledge window) that shows Cliff before Eileen sorts by this value. The world map search for "Cliff" lists the Olvia Academy Cliff (`62484`, value `13`) before the Western Guard Camp Captain Cliff (`40029`, value `1`) (2026-09-28). The search for "Emma Bartali" lists the Olvia Academy Head Administrator (`62481`, value `11`), then the Food Vendor at the farm (`47763`, value `26`), then Node Management at the outpost (`40025`, value `1`). Both searches follow character ID from high to low, and neither follows this value. It is not a code per title (Wharf Manager holds `16`, `25` and `146` to `149`, Stable Keeper `14`, `144` and `145`), but inside a group it reads as a job ranking: Olvia Academy runs Headmaster `10`, Head Administrator `11`, Deputy Headmaster `12`, the professors from Combat `13` and Alchemy `14` on, then the staff; the Edania town runs Secret Guard, Blacksmith, Skill Instructor, Storage Keeper, Central Market, Trade Manager and Work Supervisor (`5` to `11`), then the priest, stable and wharf, the guild and imperial delivery NPCs, and the vendors last (`23` to `33`). The Knowledge window and the map search are both ruled out, and the NPC search only finds one NPC at a time, so no list I can check in game shows the order (2026-09-28). It is most likely the authoring order and stays `unknown_02`.

### What is `unknown_12`?

It is `0` on the 58 rows with a lease item and `0xFFFF` on every other row, never anything else. It is probably the index of the lease option in the NPC's dialog (`0` the first, which is the one `lease_item_id` repeats; `0xFFFF` none) and has no visible effect.

### How does the client choose `kind` among several role flags?

`kind` is always one of the character's `characterspawntype.dbss` flags, but characters often have several (for example `Stable` and `Mating`). Whether `kind` drives the map icon, the NPC list filter or something else is not confirmed.
