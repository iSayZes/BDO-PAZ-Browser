# `skillpiece.dbss` Format

## Purpose

Set effect tiers. A record belongs to one set skill: each equipped piece of
the set applies a [`buff.dbss`](buff_dbss.md) type 48 buff that adds points
to that skill, and once the points reach a tier's threshold the skill runs at
the tier's level. A tier also carries the Korean tooltip text: the set title,
the threshold label and the bonus lines.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes  | Records              | Row bytes                 |
| ------ | -------------- | ------- | ----------------------- | ------ | -------------------- | ------------------------- |
| 1      | 1346 and later | 3483    | `skillpiece.dbss`       | 31,628 | 168 Tier, 100 Record | 30 to 534, 180 on average |
| 1      | 1346 and later | 3483    | `skillpieceoffset.dbss` | 1,004  | 100 Index Row        | 10                        |

| Layout | File                    | Known            | Unknown      |
| ------ | ----------------------- | ---------------- | ------------ |
| 1      | `skillpiece.dbss`       | 31,228 B (98.7%) | 400 B (1.3%) |
| 1      | `skillpieceoffset.dbss` | 1,004 B (100.0%) | 0 B (0.0%)   |

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
| 1286   | No documented layout |
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No documented layout |
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

| File                  | Required | Role                                                               |
| --------------------- | -------- | ------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Tier text in the user's language, LOC type 52, see [`languagedata_*.loc`](languagedata_loc.md#type-52-item-set-bonus-text-skillpiecedbss); set skill name, LOC type 10 |

The handler walks the records from the start of the file and does not read
`skillpieceoffset.dbss` (see below). The buffs of each tier's
[`skill.dbss`](skill_dbss.md) rank come from the `SKILL_BUFFS` lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                     |
| ------- | ------------- | ------- | ----------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `100` on client 3464   |
| `+0x04` | Record[count] | records | `count` variable-size records, back to back to the end of the file |

### Record (variable: 14 bytes + tiers)

| Offset       | Type             | Field          | Notes                                                        |
| ------------ | ---------------- | -------------- | ------------------------------------------------------------ |
| `+0x00`      | u16              | key_prefix     | Equals `skill_no`; the index's `data_offset` points past it  |
| `+0x02`      | u16              | skill_no       | The set skill, a `skill.dbss` skill number                   |
| `+0x04`      | u16              | skill_property | `0` in every record (client 3474); see Field Names           |
| `+0x06`      | u32              | tier_count     | Number of tiers; `1` to `13`                                 |
| `+0x0A`      | Tier[tier_count] | tiers          | `tier_count` tiers                                           |
| `tiers+0x00` | u32              | unknown_end    | `0` in every record                                          |

### Tier (variable: 30 bytes + text)

| Offset                | Type  | Field           | Notes                                                       |
| --------------------- | ----- | --------------- | ----------------------------------------------------------- |
| `+0x00`               | u32   | point           | Set points needed; rises from tier to tier; Lua `getPoint()` |
| `+0x04`               | u16   | level           | `skill.dbss` rank of the set skill; `1` to `tier_count` in order |
| `+0x06`               | str16 | group_title_kr  | Set title, `아그리스 세트 효과` ("Agris Set Effect"); the same in every tier of a record; Lua `getGroupTitle()` |
| `group_title_kr+0x00` | str16 | desc_title_kr   | Threshold label: `2부위` ("2 Parts"), `2개` ("x2"), `세트`, `6 포인트`, `목걸이, 허리띠 부위`; Lua `getDescTitle()` |
| `desc_title_kr+0x00`  | str16 | desc_kr         | Bonus lines, values in `<PAColor0xffe9bd23>` tags; Lua `getDesc()` |

A string is a u32 character count, a u32 `0` and that many UTF-16LE code
units with no terminator (`_common/record_reader.py` reads it with a u64
count). A line break is stored as the two characters `\n` (99 times on client
3464) or as a real newline (10 times); the parser turns both into a newline
with `decode_inline_text()`. All three strings are empty in every tier of 13 records (client 3464):
the Ancient Magic Crystal activation conditions `50047` to `50055`, the
matching boss weapons `50060` to `50068`, Serenity `50198`, and the Pearl Shop
outfits `44953` and `44954`.

### `skillpieceoffset.dbss`

| Offset  | Type             | Field | Notes                                     |
| ------- | ---------------- | ----- | ----------------------------------------- |
| `+0x00` | u32              | count | Equals the `skillpiece.dbss` count        |
| `+0x04` | Index Row[count] | rows  | `count` 10-byte rows; no magic, no trailer |

### Index Row (10 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u16  | skill_no    | Record key                                               |
| `+0x02` | u32  | data_offset | Record start + 2, past `key_prefix`                      |
| `+0x06` | u32  | data_size   | Record size - 2                                          |

The rows are in neither key nor file order (the first row is `51128`, the
second record). `parse_bare_offset_rows` (`_common/pabr_offset.py`) reads
them, and on client 3464 every row matches the record walked from the start
of the file. `test_every_offset_row_points_past_its_records_key_prefix` in the
handler tests checks this against the installed client.

## Field Names

The record is the `PointSkill_Table` sheet of a private server on client
1784 (`SkillNo`, `SkillProperty`, `Point`, `SkillLevel`, `GroupNo`,
`GroupTitle`, `Title`, `Description`). That server's dump
(`Instance_dumpFull.exe`) reads the client record from `+0x02` (row reader
at VA `0x140c85c00`) as a u16 into `SkillPieceStaticStatus` `+0x00`, a u16
into `+0x02`, the tier count and tiers, then a u32 into `+0x28`. The sheet
loader writes `SkillNo` to `+0x00` and `SkillProperty` to `+0x02` (VA
`0x140c866f6` and `0x140c866fa`), so `skill_no` is a u16 and the next u16 is
`skill_property`. Each tier's `Point` and `SkillLevel` are `point` and
`level`, and its three texts are `GroupTitle`, `Title` and `Description`.

The private server's own file holds 269 of the sheet's 270 set skills; a
sheet `SkillNo` above 65,535 (79223 to 79403) is stored as its low 16
bits (13687 to 13867). `SkillProperty` is `0` on all 315 sheet rows and
`skill_property` on every record of that file and of client 3474. The
struct starts it at `5` before the sheet sets it, and one dump function
uses it as an index into a u32 array; what the values mean is open.

`unknown_end` has no sheet column. The sheet loader sets `+0x28` to `0`,
the reader loads it from the file, and none of the five callers of the
record getter reads it. It is `0` on every record of both clients.

## Notes

- The set effect tooltip Lua (`panel_equiment_seteffecttooltip`) reads one
  entry per tier from `ToClient_GetSkillPieceInfo()` through `getSkillNo()`,
  `getPoint()`, `getGroupTitle()`, `getDescTitle()`, `getDesc()` and
  `getApply()`. The field names here follow those getters. `getApply()` is
  whether the character has the tier active: the Lua stores it as `isApplied`
  and keeps the highest `point` among applied tiers. A stored `level`, `1` or
  more, would mark every tier as applied.
- `level` is the skill rank: all 168 tiers (client 3464) have a
  `skill.dbss` rank `skill_no << 16 | level`, and no record's skill has a rank
  past its last tier. The ranks carry the buffs; the strings here are only the
  tooltip. No getter in the tooltip Lua returns it.
- `point` is the threshold, not a piece count. The type 48 buff of a piece
  adds `param_2` points: `1` on 107 of the 123 buffs (client 3464), `2` to
  `4` on buffs of 7 set skills, most of them Pearl Shop outfits (`59184`
  takes `1` to `4` and one `-4`), and `10` on the one buff of `50049`. A
  label such as `세트` or `6 포인트` stands for a points total. 99 of the 100
  keys are the `param_1` of at least one type 48 buff; `50589` ("[Set] Black
  Eye Skill Activation Requirements") is not. The items that apply those
  buffs are the set's pieces.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  reads the same layout (`internal/tables/skillpiece.go`) with two other
  readings: `pieces` for `point`, the equipped-piece threshold, and `apply` for
  `level`, "the tier ordinal exposed by Lua as `getApply()`". The tooltip Lua
  above uses `getApply()` as the active flag, and the outfit pieces of `59184`
  add up to `4` points each.
- LOC type 52 keys a tier by `str_id1 = skill_no` and `str_id2 = level`. On
  client 3464 the 87 records with Korean text have LOC rows for every tier, and
  the 13 records without text have none. `56050` has LOC rows for levels 3 and
  4 (`x8`, `x10`) that its record and `skill.dbss` lack.
- The English text can differ from the Korean values: `59184` reads `Combat
  EXP +10%` in LOC and `+50%` in `desc_kr`.

## Open Questions

### `unknown_end`

The u32 after the tiers is `0` in all 100 records (client 3474) and in all
269 of client 1784. No sheet column fills it and no code in the client 1784
server dump reads it (Field Names). No field elsewhere points at it.

### Black Eye set points

`50589` has a record (3 points, level 1, `검은눈 효과`) but no type 48 buff
adds points to it, so it is open how the Black Eye pieces count toward it.
