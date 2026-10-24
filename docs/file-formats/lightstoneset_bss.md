# `lightstoneset.bss` Format

## Purpose

The Lightstone sets: each row names three or four Lightstones that, slotted
into Artifacts together, apply a set effect. A row holds the set ID, the
passive skill that carries the effect, the member Lightstone item IDs and the
Korean name and effect text. A table after the rows lists which Lightstone
items count as which member, so an Amplified Lightstone completes a set like
its base Lightstone.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes  | Records                         | Row bytes               |
| ------ | -------------- | ------- | ------------------- | ------ | ------------------------------- | ----------------------- |
| 1      | 2970 and later | 3483    | `lightstoneset.bss` | 30,209 | 165 Set Row, 105 Substitute Row | 26 to 30, 29 on average |

| Layout | File                | Known             | Unknown    |
| ------ | ------------------- | ----------------- | ---------- |
| 1      | `lightstoneset.bss` | 30,209 B (100.0%) | 0 B (0.0%) |

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
| 2825   | No documented layout |
| 2819   | No documented layout |
| 2811   | No documented layout |
| 2803   | No documented layout |
| 2794   | No documented layout |
| 2783   | No documented layout |
| 2774   | No documented layout |
| 2765   | No documented layout |
| 2756   | No documented layout |
| 2750   | No documented layout |
| 2743   | No documented layout |
| 2736   | No documented layout |
| 2726   | No documented layout |
| 2717   | No documented layout |
| 2709   | No documented layout |
| 2703   | No documented layout |
| 2695   | No documented layout |
| 2684   | No documented layout |
| 2672   | No documented layout |
| 2665   | No documented layout |
| 2657   | No documented layout |
| 2649   | No documented layout |
| 2644   | No documented layout |
| 2637   | No documented layout |
| 2629   | No documented layout |
| 2619   | No documented layout |
| 2612   | No documented layout |
| 2606   | No documented layout |
| 2602   | No documented layout |
| 2601   | No documented layout |
| 2592   | No documented layout |
| 2583   | No documented layout |
| 2575   | No documented layout |
| 2567   | No documented layout |
| 2560   | No documented layout |
| 2553   | No documented layout |
| 2545   | No documented layout |
| 2538   | No documented layout |
| 2529   | No documented layout |
| 2519   | No documented layout |
| 2513   | No documented layout |
| 2510   | No documented layout |
| 2507   | No documented layout |
| 2503   | No documented layout |
| 2498   | No documented layout |
| 2492   | No documented layout |
| 2487   | No documented layout |
| 2480   | No documented layout |
| 2474   | No documented layout |
| 2468   | No documented layout |
| 2460   | No documented layout |
| 2453   | No documented layout |
| 2444   | No documented layout |
| 2438   | No documented layout |
| 2434   | No documented layout |
| 2429   | No documented layout |
| 2421   | No documented layout |
| 2414   | No documented layout |
| 2407   | No documented layout |
| 2401   | No documented layout |
| 2397   | No documented layout |
| 2393   | No documented layout |
| 2384   | No documented layout |
| 2378   | No documented layout |
| 2372   | No documented layout |
| 2358   | No documented layout |
| 2352   | No documented layout |
| 2347   | No documented layout |
| 2343   | No documented layout |
| 2335   | No documented layout |
| 2327   | No documented layout |
| 2324   | No documented layout |
| 2319   | No documented layout |
| 2313   | No documented layout |
| 2308   | No documented layout |
| 2302   | No documented layout |
| 2295   | No documented layout |
| 2290   | No documented layout |
| 2284   | No documented layout |
| 2276   | No documented layout |
| 2269   | No documented layout |
| 2259   | No documented layout |
| 2250   | No documented layout |
| 2243   | No documented layout |
| 2235   | No documented layout |
| 2229   | No documented layout |
| 2224   | No documented layout |
| 2218   | No documented layout |
| 2215   | No documented layout |
| 2207   | No documented layout |
| 2203   | No documented layout |
| 2196   | No documented layout |
| 2192   | No documented layout |
| 2189   | No documented layout |
| 2183   | No documented layout |
| 2179   | No documented layout |
| 2171   | No documented layout |
| 2163   | No documented layout |
| 2156   | No documented layout |
| 2151   | No documented layout |
| 2147   | No documented layout |
| 2142   | No documented layout |
| 2138   | No documented layout |
| 2134   | No documented layout |
| 2130   | No documented layout |
| 2122   | No documented layout |
| 2107   | No documented layout |
| 2098   | No documented layout |
| 2089   | No documented layout |
| 2081   | No documented layout |
| 2073   | No documented layout |
| 2067   | No documented layout |
| 2063   | No documented layout |
| 2059   | No documented layout |
| 2052   | No documented layout |
| 2044   | No documented layout |
| 2039   | No documented layout |
| 2032   | No documented layout |
| 2025   | No documented layout |
| 2011   | No documented layout |
| 2005   | No documented layout |
| 2000   | No documented layout |
| 1996   | No documented layout |
| 1991   | No documented layout |
| 1985   | No documented layout |
| 1980   | No documented layout |
| 1969   | No documented layout |
| 1964   | No documented layout |
| 1958   | No documented layout |
| 1950   | No documented layout |
| 1945   | No documented layout |
| 1937   | No documented layout |
| 1933   | No documented layout |
| 1927   | No documented layout |
| 1921   | No documented layout |
| 1914   | No documented layout |
| 1908   | No documented layout |
| 1897   | No documented layout |
| 1892   | No documented layout |
| 1886   | No documented layout |
| 1881   | No documented layout |
| 1871   | No documented layout |
| 1866   | No documented layout |
| 1862   | No documented layout |
| 1854   | No documented layout |
| 1846   | No documented layout |
| 1838   | No documented layout |
| 1832   | No documented layout |
| 1826   | No documented layout |
| 1822   | No documented layout |
| 1818   | No documented layout |
| 1804   | No documented layout |
| 1794   | No documented layout |
| 1790   | No documented layout |
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

The file is self-contained. The handler reads these through shared lookups:

| File                  | Required | Role                                                                    |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Set name and effect (LOC type 113, `str_id1` = set ID), item names (type 0) |
| `skill.dbss`          | Optional | The buffs of the set skill at level 1 (`SKILL_BUFFS` lookup index)      |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The PABR string table layout of `buffsimply.bss` (`_common/pabr_strings.py`),
with variable-size rows and a second table between the rows and the strings.

| Offset              | Type                 | Field        | Notes                                                       |
| ------------------- | -------------------- | ------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                                |
| `+0x04`             | u32                  | count        | Number of sets; 165 on client 3464                          |
| `+0x08`             | Set Row[count]       | sets         | See Set Row                                                 |
| `sets+0x00`         | Substitute Table     | substitutes  | See Substitute Table                                        |
| `substitutes+0x00`  | String Table         | string_table | See String Table                                            |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where the substitute table ends |
| `string_table+0x04` | u32                  | zero         | Always 0                                                    |

On client 3464 the walk over 165 sets and 105 substitute rows ends at
`0x162A`, the stored `table_start`.

### Set Row (variable: 14 bytes + member IDs)

Fields are unaligned.

| Offset            | Type              | Field        | Notes                                                                  |
| ----------------- | ----------------- | ------------ | ---------------------------------------------------------------------- |
| `+0x00`           | u32               | set_id       | Unique; LOC type 113 `str_id1`, and the number in the skill name       |
| `+0x04`           | u16               | skill_no     | Passive skill of the set effect; unique                                |
| `+0x06`           | u32               | member_count | `3` or `4` on client 3464                                              |
| `+0x0A`           | u32[member_count] | member_ids   | Lightstone item IDs, ascending; a stone may repeat                     |
| `member_ids+0x00` | u32               | text_ref     | String table index of the Korean name and effect; equals the row index |

The skill confirms the set ID: LOC type 10 names skill `55078` "Set 2 -
[Well-prepared]" and skill `47521` "Set 182 - [The Wild: Edania]", and
`skill.dbss` gives skill `55078` level 1 the three buffs whose LOC type 5
first lines are the three effect lines of set 2. On client 3464 the level 1
rank of every set skill has one buff per effect line.

The text is the Korean source of the LOC type 113 row:
`<PAColor0xffd2ffad>[준비된 자]<PAOldColor>\n전투 경험치 획득량 +50%\n...`.
The first line is the name in brackets and colour, each further line one
effect. Line breaks are stored as the two characters `\` and `n`
(`_common/inline_text.py`).

### Substitute Table (variable: 4 bytes + rows)

| Offset  | Type                  | Field | Notes                         |
| ------- | --------------------- | ----- | ----------------------------- |
| `+0x00` | u32                   | count | Number of substitute rows     |
| `+0x04` | Substitute Row[count] | rows  | See Substitute Row            |

### Substitute Row (8 bytes)

| Offset  | Type | Field     | Notes                                                       |
| ------- | ---- | --------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_id   | A Lightstone item ID; unique                                |
| `+0x04` | u32  | member_id | The member item ID it counts as in `member_ids`             |

On client 3464 there are 105 rows: 53 map every member item to itself, and
52 map an Amplified Lightstone (`member_id + 200`, such as `758203`
Amplified Lightstone of Fire: Predation) to its base Lightstone. The rows are
in no sorted order. Garmoth's Lightstone sets page lists each member as "Any
of" the base and the Amplified Lightstone, which matches these rows.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Notes

- The sets with four members come first, then the sets with three, each
  group in ascending `set_id`.
- Set IDs run from 1 to 182 with 17 gaps (30, 51 to 55, 64, 66, 70, 72, 73,
  77 to 80, 164, 173). LOC type 113 still has a row for each gap
  (`[Blacksmith's Blessing]`, `[Brown Bear]`), so these are sets the client
  no longer has.
- The 21 substitute rows from `764201` to `764221` (Lightstone of Flora
  `+200`) name items with no LOC type 0 name and no item icon on client 3464;
  In-Game Checks has a test for whether they exist.
- Iridescent Lightstone (`766101`) is a member of 50 sets, always as the
  last stone.
- The `LIGHTSTONE_SETS` lookup index (`build_lightstone_set_index()` in
  `parser.py`) maps each member and substitute item ID to the sets it counts
  toward, so the [itemenchant.dbss](itemenchant_dbss.md) Lightstone Sets
  column lists them without opening this file.
- The LOC type 113 name of set 96 repeats itself: `[Drills: Blight-Fallen]
  [Drills: Blight-Fallen]`, while the skill name is `Set 96 - [Drills:
  Blight-Fallen]`.
- Cross-check against Garmoth's Lightstone sets page (combat sets only): all
  83 sets it lists have the same members, and the first effect tier values
  equal the LOC type 113 values. Its two further columns, "Including
  Lightstone Effects" and "Including Amplified Lightstone Effects", hold
  values this file does not have.
- The Artifact window and tooltip Lua (`panel_window_artifacts_all`,
  `panel_equiment_artifactstooltip`) get the active set through
  `ToClient_getLightStoneSet`, `ToClient_getLightStoneSetByInvenSlotNo` and
  `ToClient_getLightStoneSetByFromLifeEquipSlotNo` and write it to the set
  option text.

## In-Game Checks

### Amplified Lightstones of Flora

Needs item (all):

- [Lightstone of Flora: Wildlife](https://bdocodex.com/us/item/764001/), or any other Lightstone of Flora (`764001` to `764021`)
- [Crystallized Energy of Endtimes](https://bdocodex.com/us/item/821252/) x30
- [Magical Shard](https://bdocodex.com/us/item/4918/) x50
- [Magical Lightstone Crystal](https://bdocodex.com/us/item/766108/) x100

The LOC description of Crystallized Energy of Endtimes gives the Amplified
Lightstone recipe: Heating "Lightstone (any type) x1" with the three
materials above. Heat a Lightstone of Flora with them. If it gives an
Amplified Lightstone of Flora (item `764001` + 200 = `764201` for Wildlife),
the 21 substitute rows from `764201` to `764221` are live items whose name
and icon the client lacks. If Heating rejects a Flora Lightstone, they are
rows for items the game does not hand out.
