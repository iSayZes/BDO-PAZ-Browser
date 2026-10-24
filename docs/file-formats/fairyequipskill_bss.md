# `fairyequipskill.bss` Format

## Purpose

Defines the fairy skill catalog, the 35 skills a fairy can hold, grouped into 8 skill types with tier progressions (e.g. `Tingling Breath I`–`V`). Each record stores its skill type group and a `gc::SkillKey` (skill level and skill number); the skill number resolves to both the skill name and its effect description, and doubles as the icon filename number.

The remainder of the file is a 200-slot reserved block of null placeholders, so the catalog can grow without changing the layout.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records                   | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------------------------- | --------- |
| 2      | 1921 and later | 3483    | `fairyequipskill.bss` | 3,636 | 35 Skill Record, 200 Slot | 16        |
| 1      | 805 to 1871    | 1871    | `fairyequipskill.bss` | 1,576 | 30 Skill Record, 100 Slot | 12        |

| Layout | File                  | Known            | Unknown       |
| ------ | --------------------- | ---------------- | ------------- |
| 2      | `fairyequipskill.bss` | 2,836 B (78.0%)  | 800 B (22.0%) |
| 1      | `fairyequipskill.bss` | 1,576 B (100.0%) | 0 B (0.0%)    |

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
| 1914   | No documented layout |
| 1908   | No documented layout |
| 1897   | No documented layout |
| 1892   | No documented layout |
| 1886   | No documented layout |
| 1881   | No documented layout |
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
| 1341   | Layout 1             |
| 1340   | Layout 1             |
| 1338   | Layout 1             |
| 1335   | Layout 1             |
| 1333   | Layout 1             |
| 1329   | Layout 1             |
| 1327   | Layout 1             |
| 1324   | Layout 1             |
| 1321   | Layout 1             |
| 1319   | Layout 1             |
| 1318   | Layout 1             |
| 1316   | Layout 1             |
| 1313   | Layout 1             |
| 1311   | Layout 1             |
| 1309   | Layout 1             |
| 1304   | Layout 1             |
| 1292   | Layout 1             |
| 1286   | Layout 1             |
| 1280   | Layout 1             |
| 1276   | Layout 1             |
| 1267   | Layout 1             |
| 1261   | Layout 1             |
| 1256   | Layout 1             |
| 1250   | Layout 1             |
| 1246   | Layout 1             |
| 1239   | Layout 1             |
| 1230   | Layout 1             |
| 1226   | Layout 1             |
| 1220   | Layout 1             |
| 1217   | Layout 1             |
| 1211   | Layout 1             |
| 1210   | Layout 1             |
| 1208   | Layout 1             |
| 1203   | Layout 1             |
| 1197   | Layout 1             |
| 1194   | Layout 1             |
| 1192   | Layout 1             |
| 1187   | Layout 1             |
| 1183   | Layout 1             |
| 1177   | Layout 1             |
| 1173   | Layout 1             |
| 1167   | Layout 1             |
| 1164   | Layout 1             |
| 1156   | Layout 1             |
| 1149   | Layout 1             |
| 1144   | Layout 1             |
| 1137   | Layout 1             |
| 1132   | Layout 1             |
| 1127   | Layout 1             |
| 1122   | Layout 1             |
| 1118   | Layout 1             |
| 1114   | Layout 1             |
| 1109   | Layout 1             |
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
| 829    | Layout 1             |
| 822    | Layout 1             |
| 814    | Layout 1             |
| 805    | Layout 1             |
| 794    | No documented layout |
| 787    | No documented layout |
| 780    | No documented layout |
| 771    | No documented layout |
| 760    | No documented layout |
| 748    | No documented layout |
| 741    | No documented layout |
| 736    | No documented layout |
| 731    | No documented layout |
| 723    | No documented layout |
| 711    | No documented layout |
| 707    | No documented layout |
| 697    | No documented layout |
| 689    | No documented layout |
| 683    | No documented layout |
| 678    | No documented layout |
| 670    | No documented layout |
| 661    | No documented layout |
| 656    | No documented layout |
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

None. `fairyequipskill.bss` is a standalone catalog with no offset index.

| File                  | Required | Role                                             |
| --------------------- | -------- | ------------------------------------------------ |
| `languagedata_en.loc` | Optional | Skill names (`id4=0`) and descriptions (`id4=1`) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

Total file size: 3636 bytes = 4 (magic) + 420 (catalog) + 3200 (reserved block) + 12 (trailer).

Records begin immediately at `+0x04`. There is **no** record count field; the catalog is terminated by the first record whose `equip_skill_id` is `200`.

| Offset              | Type                                      | Field         | Notes                                                       |
| ------------------- | ----------------------------------------- | ------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]                                   | magic         | `PABR` (ASCII)                                              |
| `+0x04`             | Skill Record[while equip_skill_id != 200] | skill_records | 35 x 12-byte skill records, `+0x004` to `+0x1A8`            |
| `skill_records+0x00` | Slot[..data_end]                         | slots         | Reserved block: 200 x 16-byte null placeholders, `+0x1A8` to `+0xE28` |
| `EOF-0x0C` | u32 | string_count | `0`: the PABR string table, here with no strings; `data_end` points at it |
| `EOF-0x08` | u32 | data_end | `0x0E28` (3624) = `file_size - 12`, the offset of `string_count` |
| `EOF-0x04` | u32 | zero | Always `0` |

`petequipskill.bss` carries the identical trailer (`data_end = 0x0EB0 = file_size - 12`), so this is a shared PABR convention rather than a fairy-specific field.

### Skill Record (12 bytes)

| Offset  | Type | Field          | Notes                                                  |
| ------- | ---- | -------------- | ------------------------------------------------------ |
| `+0x00` | u32  | equip_skill_id | Sequential record key, `0` to `34`; `200` marks the end |
| `+0x04` | u32  | skill_type     | Skill group, `1` to `8` (see Skill Types)              |
| `+0x08` | u16  | skill_level    | Skill level of the `gc::SkillKey`; always `1`          |
| `+0x0A` | u16  | skill_no       | Skill number (`SkillNo`); keys the name, description and icon |

Earlier versions of this doc called `skill_level` `tier`.

### Slot (16 bytes)

Two hundred unused catalog slots. Every record is `[u32 200][u32 0][u32 0][u32 0]`, where `200` is the null-entry sentinel. Skip these when parsing.

The stride here is 16 bytes, not the 12 used by live records; it matches the wider Section 2 record shape in `petequipskill.bss`, whose extended catalog is fully populated. In `fairyequipskill.bss` that extended section is entirely null.

| Offset  | Type      | Field          | Notes                                                                                                   |
| ------- | --------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | u32       | equip_skill_id | Always `200`, the null-entry sentinel                                                                   |
| `+0x04` | u32       | skill_type     | Always `0`                                                                                              |
| `+0x08` | u16       | skill_level    | Always `0`                                                                                              |
| `+0x0A` | u16       | skill_no       | Always `0`                                                                                              |
| `+0x0C` | u32       | unknown_0c     | Always `0`; the `petequipskill.bss` Slot's `unknown_0c`, and no extra u32 follows                       |


## Field Names

The client 1784 private server loads `Fairy_EquipSkill_Table` into one 24-byte entry per
record: `Index` (`equip_skill_id`) at `+0x00`, `GroupNo` (`skill_type`) at
`+0x04`, a runtime skill pointer at `+0x08` and a `gc::SkillKey` at `+0x10`.
The loader (VA `0x1409c8f13` to `0x1409c8f19`) writes the key as `(SkillNo << 16) | 1`, so its low u16
is the skill level (always `1`) and its high u16 the sheet's `SkillNo`. The
2016 client's `gc::SkillKey` is one `unsigned int _value` whose `getLevel()`
reads the low u16 and `getSkillNo()` the high u16, which places
`skill_level` at `+0x08` and `skill_no` at `+0x0A`. The server has no reader
for this file; the record is that entry in loader order without the pointer
and the padding. After loading, it looks up every key in the skill table and
logs "펫 착용 스킬에 알수 없는 스킬(%#)의 데이터가 있습니다!" ("pet equip
skill has data for an unknown skill (%#)!") for a missing one.
`petequipskill.bss` and `fairyequipskill.bss` share the entry, the loader
shape and the per-entry checks, which is why the fairy check logs the pet message.

The client 1784 build's own file matches `Fairy_EquipSkill_Table` on all
30 records (Index, GroupNo, level `1`, SkillNo); client 3474 has level `1`
on all 35. The null slots are the same struct with every field `0`.

LOC type 10 keys the skill name by `skill_no`
([`languagedata_loc.md`](languagedata_loc.md)). Earlier versions of this doc
read `+0x08` as two u8 fields (`unknown_08`, `unknown_09`) and named `+0x0A`
`loc_id`.

## Layout 1

On client 1784 the null-entry sentinel was `100`, not `200`, and every
Slot was 12 bytes, the size of a Skill Record. The File Layout and the Slot
differ from Layout 2; the Skill Record is the same. On client 1784 the file
holds 30 Skill Records and 100 Slots.

### File Layout

| Offset               | Type                                      | Field         | Notes                                                          |
| -------------------- | ----------------------------------------- | ------------- | -------------------------------------------------------------- |
| `+0x00`              | char[4]                                   | magic         | `PABR` (ASCII)                                                 |
| `+0x04`              | Skill Record[while equip_skill_id != 100] | skill_records | Ends at the first record whose `equip_skill_id` is `100`       |
| `skill_records+0x00` | Slot[..data_end]                          | slots         | 12-byte null placeholders up to `data_end`                     |
| `EOF-0x0C`           | u32                                       | string_count  | `0`: the PABR string table, here with no strings               |
| `EOF-0x08`           | u32                                       | data_end      | `file_size - 12`, the offset of `string_count`                 |
| `EOF-0x04`           | u32                                       | zero          | Always `0`                                                     |

### Slot (12 bytes)

| Offset  | Type     | Field          | Notes                                 |
| ------- | -------- | -------------- | ------------------------------------- |
| `+0x00` | u32      | equip_skill_id | Always `100`, the null-entry sentinel |
| `+0x04` | u32      | skill_type     | Always `0`                            |
| `+0x08` | u16      | skill_level    | Always `0`                            |
| `+0x0A` | u16      | skill_no       | Always `0`                            |
