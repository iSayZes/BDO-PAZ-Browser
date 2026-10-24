# `skilltype.dbss` Format

## Purpose

The presentation record of every skill: the Korean skill name, its family
name, whether it is active or passive, the skill icon, and a long action
configuration (animation, targeting and combat behaviour) that is not decoded.
This is where a skill's icon comes from.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes     | Records                       | Row bytes                    |
| ------ | -------------- | ------- | ---------------------- | --------- | ----------------------------- | ---------------------------- |
| 1      | 1346 and later | 3483    | `skilltype.dbss`       | 8,685,956 | 30,475 Payload, 30,475 Record | 153 to 1,041, 281 on average |
| 1      | 1346 and later | 3483    | `skilltypeoffset.dbss` | 365,720   | 30,475 Index Row              | 12                           |

| Layout | File                   | Known                | Unknown    |
| ------ | ---------------------- | -------------------- | ---------- |
| 1      | `skilltype.dbss`       | 8,685,956 B (100.0%) | 0 B (0.0%) |
| 1      | `skilltypeoffset.dbss` | 365,720 B (100.0%)   | 0 B (0.0%) |

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
| 3118   | Layout 1             |
| 3111   | Layout 1             |
| 3103   | Layout 1             |
| 3095   | Layout 1             |
| 3086   | Layout 1             |
| 3072   | Layout 1             |
| 3062   | Layout 1             |
| 3052   | Layout 1             |
| 3045   | Layout 1             |
| 3037   | Layout 1             |
| 3030   | Layout 1             |
| 3021   | Layout 1             |
| 3012   | Layout 1             |
| 3002   | Layout 1             |
| 2995   | Layout 1             |
| 2987   | Layout 1             |
| 2978   | Layout 1             |
| 2970   | Layout 1             |
| 2959   | Layout 1             |
| 2951   | Layout 1             |
| 2942   | Layout 1             |
| 2935   | Layout 1             |
| 2932   | Layout 1             |
| 2923   | Layout 1             |
| 2919   | Layout 1             |
| 2907   | Layout 1             |
| 2900   | Layout 1             |
| 2891   | Layout 1             |
| 2882   | Layout 1             |
| 2872   | Layout 1             |
| 2863   | Layout 1             |
| 2855   | Layout 1             |
| 2849   | Layout 1             |
| 2844   | Layout 1             |
| 2834   | Layout 1             |
| 2825   | Layout 1             |
| 2819   | Layout 1             |
| 2811   | Layout 1             |
| 2803   | Layout 1             |
| 2794   | Layout 1             |
| 2783   | Layout 1             |
| 2774   | Layout 1             |
| 2765   | Layout 1             |
| 2756   | Layout 1             |
| 2750   | Layout 1             |
| 2743   | Layout 1             |
| 2736   | Layout 1             |
| 2726   | Layout 1             |
| 2717   | Layout 1             |
| 2709   | Layout 1             |
| 2703   | Layout 1             |
| 2695   | Layout 1             |
| 2684   | Layout 1             |
| 2672   | Layout 1             |
| 2665   | Layout 1             |
| 2657   | Layout 1             |
| 2649   | Layout 1             |
| 2644   | Layout 1             |
| 2637   | Layout 1             |
| 2629   | Layout 1             |
| 2619   | Layout 1             |
| 2612   | Layout 1             |
| 2606   | Layout 1             |
| 2602   | Layout 1             |
| 2601   | Layout 1             |
| 2592   | Layout 1             |
| 2583   | Layout 1             |
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

| File                   | Required | Role                                                             |
| ---------------------- | -------- | ---------------------------------------------------------------- |
| `skilltypeoffset.dbss` | Required | `skill_key → (offset, size)` index into this file                |
| `languagedata_en.loc`  | Optional | English names, LOC type `10`, `str_id1 = skill_no`               |

The skill key is the one shared by the whole skill cluster; see
[`skill.dbss` Skill Keys](skill_dbss.md#skill-keys). All multi-byte values are
little-endian.

## Layout 1

### File Layout

The records tile the file like `skill.dbss`: each starts 4 bytes after the
previous one ends, the first at `8`, and the last ends at end of file. Strings
are a `u64` count followed by UTF-16LE units (text) or ASCII bytes (paths).

Every key is level `1`. 30,342 of the 30,352 keys are also in `skill.dbss`;
the 82 `skill.dbss` keys above level 1 have no record here.

| Offset  | Type          | Field   | Notes                                      |
| ------- | ------------- | ------- | ------------------------------------------ |
| `+0x00` | u32           | count   | Number of records; matches the offset file |
| `+0x04` | Record[count] | records | See Record                                 |

### Record (variable: 4 bytes + payload)

| Offset  | Type    | Field      | Notes                                                       |
| ------- | ------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32     | key_prefix | Each record is preceded by a repeated copy of its key       |
| `+0x04` | Payload | payload    | `size` bytes; the index row's `offset` points at this field |

### Payload (variable: 24 bytes + names and config, size from `skilltypeoffset.dbss`)

| Offset            | Type        | Field      | Notes                                                    |
| ----------------- | ----------- | ---------- | -------------------------------------------------------- |
| `+0x00`           | u32         | skill_key  | Equals the index key                                     |
| `+0x04`           | str16       | name       | Korean skill name, e.g. `거대한 진노 III`                 |
| `name+0x00`       | str16       | group_name | Korean family name, see [`group_name`](#group_name)      |
| `group_name+0x00` | u32         | kind       | `0` other, `1` active, `2` passive; see [`kind`](#kind)  |
| `group_name+0x04` | bytes[rest] | config     | Action configuration, not decoded; holds `icon_path`, see [`icon_path`](#icon_path) |

### `skilltypeoffset.dbss`

The layout of [`skilloffset.dbss`](skill_dbss.md#skilloffsetdbss). Read it with
`parse_pabr_u32_offset_rows()`.

| Offset              | Type             | Field        | Notes                                    |
| ------------------- | ---------------- | ------------ | ---------------------------------------- |
| `+0x00`             | char[4]          | magic        | ASCII `PABR`                             |
| `+0x04`             | u32              | count        | Number of index rows; `30352` on client 3458 |
| `+0x08`             | Index Row[count] | rows         | See Index Row                            |
| `rows+0x00`         | String Table     | string_table | Empty: `string_count` is `0`             |
| `string_table+0x00` | u32              | table_start  | End of the rows, `8 + 12 * count`        |
| `string_table+0x04` | u32              | zero         | Always 0                                 |

### Index Row (12 bytes)

| Offset  | Type | Field     | Notes                                                  |
| ------- | ---- | --------- | ------------------------------------------------------ |
| `+0x00` | u32  | skill_key | `skill_no << 16 \| level`                              |
| `+0x04` | u32  | offset    | Byte offset of the record's `payload` in `skilltype.dbss` |
| `+0x08` | u32  | size      | Payload size in bytes                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes            |
| ------- | ------------------ | ------------ | ---------------- |
| `+0x00` | u32                | string_count | `0`              |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none here |

## `group_name`

Equal to `name` on 16,847 records. On the other 13,505 it is the name without
the rank or a qualifier: `거대한 진노 III` -> `거대한 진노`, `탈것 속도 증가 1.0%`
-> `속도 +1.0%`. Some are cut mid-phrase (`극 : 매화의 정신` -> `극 : 매화의`), so it
reads like a short label rather than a clean family name.

## `kind`

| Value | Meaning | Records | Example                                  |
| ----- | ------- | ------- | ---------------------------------------- |
| 0     | Other   | 14,382  | Item and event skills, "[Event] Energy of Happiness" (57005) |
| 1     | Active  | 10,219  | "Seismic Strike", "Fist Fury I"          |
| 2     | Passive | 5,751   | "Mountain Aura IX" to "XVI"              |

## `icon_path`

The skill icon is the first length-prefixed ASCII string in `config`, a `.dds`
path relative to `ui_texture/icon/`. `find_prefixed_ascii()` finds it, as for
`itemenchant.dbss`. Its position is not fixed: it follows a variable part of
the configuration, 49 to 69 bytes after `kind`.

| Kind    | With icon | Without |
| ------- | --------- | ------- |
| Other   | 186       | 14,196  |
| Active  | 7,654     | 2,565   |
| Passive | 1,562     | 4,189   |

9,402 records have an icon, never more than one, over 3,530 distinct paths.
Lower-cased under `ui_texture/icon/`, 3,452 of those paths exist in the
client's PAZ files on client 3458; the other 78 point at missing files
(for example `new_icon/04_pc_skill/01_pc_skill/31_prsa_skill/prsa_skill_8827.dds`).

`config` also holds 7,355 `.png` paths such as
`Real_ETC/Scroll/Icon_ETC_Scroll_00000000.png`; what they are for is not
known.

## Notes

- The first keys (`0xDEAD0001`, `0xDEAC0001`) look like sentinels but are
  real skills; see [`skill.dbss` Skill Keys](skill_dbss.md#skill-keys).
- The record layout of the first four fields and the `kind` meaning come from
  bdo-data-extractor; the counts, the icon rule and the `group_name` reading
  were checked against client 3458.
- LOC type `10` covers 28,343 of its 29,398 IDs with a skill number from this
  table or `skill.dbss`; 2,009 skill numbers have no type `10` row and 1,055
  type `10` IDs have no skill.

## Open Questions

### How is `config` laid out?

The configuration opens with small counts and lists (a run of `ff ff ff ff ff
7f`, the skill key again, and skill numbers and keys on class skills) before
the icon, which is why the icon moves between 49 and 69 bytes after `kind`.
Decoding it would give the icon a fixed place and expose the animation and
targeting fields, but nothing that is needed so far depends on it.
