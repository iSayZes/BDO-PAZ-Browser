# `uiguildskilltreelayout.bss` Format

## Purpose

The guild skill window as one grid of cells: each cell is blank, a guild
skill, or a piece of the line that links the skills. The guild window
(`panel_guildskill_all_1.luac`) builds its skill page from it through
`getGuildSkillTree()`. On client 3482 the grid is 17 columns by 46 rows and
places 58 skills.

Seven more files use this layout, each one grid:
[`uifusionskilltreelayout.bss`](uifusionskilltreelayout_bss.md),
[`uiproductskilltreelayout.bss`](uiproductskilltreelayout_bss.md) and the
five [`ui_territorypolicyskilltree_*.bss`](ui_territorypolicyskilltree_bss.md)
files. One handler reads all eight. The cell is the one
[`uipracticeskilltreelayout.bss`](uipracticeskilltreelayout_bss.md) uses,
without that file's class header.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                         | Bytes | Records  | Row bytes |
| ------ | ------------- | ------- | ---------------------------- | ----- | -------- | --------- |
| 2      | 805 and later | 3483    | `uiguildskilltreelayout.bss` | 3,152 | 782 Cell | 4         |
| 1      | 457 to 794    | 794     | `uiguildskilltreelayout.bss` | 1,844 | 459 Cell | 4         |

| Layout | File                         | Known            | Unknown    |
| ------ | ---------------------------- | ---------------- | ---------- |
| 2      | `uiguildskilltreelayout.bss` | 3,152 B (100.0%) | 0 B (0.0%) |
| 1      | `uiguildskilltreelayout.bss` | 1,844 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3464   | Layout 2 |
| 3458   | Layout 2 |
| 3454   | Layout 2 |
| 3444   | Layout 2 |
| 3435   | Layout 2 |
| 3426   | Layout 2 |
| 3418   | Layout 2 |
| 3412   | Layout 2 |
| 3402   | Layout 2 |
| 3396   | Layout 2 |
| 3387   | Layout 2 |
| 3381   | Layout 2 |
| 3373   | Layout 2 |
| 3364   | Layout 2 |
| 3356   | Layout 2 |
| 3349   | Layout 2 |
| 3342   | Layout 2 |
| 3335   | Layout 2 |
| 3326   | Layout 2 |
| 3321   | Layout 2 |
| 3314   | Layout 2 |
| 3303   | Layout 2 |
| 3302   | Layout 2 |
| 3293   | Layout 2 |
| 3283   | Layout 2 |
| 3275   | Layout 2 |
| 3267   | Layout 2 |
| 3258   | Layout 2 |
| 3251   | Layout 2 |
| 3242   | Layout 2 |
| 3235   | Layout 2 |
| 3229   | Layout 2 |
| 3212   | Layout 2 |
| 3203   | Layout 2 |
| 3193   | Layout 2 |
| 3186   | Layout 2 |
| 3177   | Layout 2 |
| 3169   | Layout 2 |
| 3158   | Layout 2 |
| 3151   | Layout 2 |
| 3144   | Layout 2 |
| 3133   | Layout 2 |
| 3125   | Layout 2 |
| 3118   | Layout 2 |
| 3111   | Layout 2 |
| 3103   | Layout 2 |
| 3095   | Layout 2 |
| 3086   | Layout 2 |
| 3072   | Layout 2 |
| 3062   | Layout 2 |
| 3052   | Layout 2 |
| 3045   | Layout 2 |
| 3037   | Layout 2 |
| 3030   | Layout 2 |
| 3021   | Layout 2 |
| 3012   | Layout 2 |
| 3002   | Layout 2 |
| 2995   | Layout 2 |
| 2987   | Layout 2 |
| 2978   | Layout 2 |
| 2970   | Layout 2 |
| 2959   | Layout 2 |
| 2951   | Layout 2 |
| 2942   | Layout 2 |
| 2935   | Layout 2 |
| 2932   | Layout 2 |
| 2923   | Layout 2 |
| 2919   | Layout 2 |
| 2907   | Layout 2 |
| 2900   | Layout 2 |
| 2891   | Layout 2 |
| 2882   | Layout 2 |
| 2872   | Layout 2 |
| 2863   | Layout 2 |
| 2855   | Layout 2 |
| 2849   | Layout 2 |
| 2844   | Layout 2 |
| 2834   | Layout 2 |
| 2825   | Layout 2 |
| 2819   | Layout 2 |
| 2811   | Layout 2 |
| 2803   | Layout 2 |
| 2794   | Layout 2 |
| 2783   | Layout 2 |
| 2774   | Layout 2 |
| 2765   | Layout 2 |
| 2756   | Layout 2 |
| 2750   | Layout 2 |
| 2743   | Layout 2 |
| 2736   | Layout 2 |
| 2726   | Layout 2 |
| 2717   | Layout 2 |
| 2709   | Layout 2 |
| 2703   | Layout 2 |
| 2695   | Layout 2 |
| 2684   | Layout 2 |
| 2672   | Layout 2 |
| 2665   | Layout 2 |
| 2657   | Layout 2 |
| 2649   | Layout 2 |
| 2644   | Layout 2 |
| 2637   | Layout 2 |
| 2629   | Layout 2 |
| 2619   | Layout 2 |
| 2612   | Layout 2 |
| 2606   | Layout 2 |
| 2602   | Layout 2 |
| 2601   | Layout 2 |
| 2592   | Layout 2 |
| 2583   | Layout 2 |
| 2575   | Layout 2 |
| 2567   | Layout 2 |
| 2560   | Layout 2 |
| 2553   | Layout 2 |
| 2545   | Layout 2 |
| 2538   | Layout 2 |
| 2529   | Layout 2 |
| 2519   | Layout 2 |
| 2513   | Layout 2 |
| 2510   | Layout 2 |
| 2507   | Layout 2 |
| 2503   | Layout 2 |
| 2498   | Layout 2 |
| 2492   | Layout 2 |
| 2487   | Layout 2 |
| 2480   | Layout 2 |
| 2474   | Layout 2 |
| 2468   | Layout 2 |
| 2460   | Layout 2 |
| 2453   | Layout 2 |
| 2444   | Layout 2 |
| 2438   | Layout 2 |
| 2434   | Layout 2 |
| 2429   | Layout 2 |
| 2421   | Layout 2 |
| 2414   | Layout 2 |
| 2407   | Layout 2 |
| 2401   | Layout 2 |
| 2397   | Layout 2 |
| 2393   | Layout 2 |
| 2384   | Layout 2 |
| 2378   | Layout 2 |
| 2372   | Layout 2 |
| 2358   | Layout 2 |
| 2352   | Layout 2 |
| 2347   | Layout 2 |
| 2343   | Layout 2 |
| 2335   | Layout 2 |
| 2327   | Layout 2 |
| 2324   | Layout 2 |
| 2319   | Layout 2 |
| 2313   | Layout 2 |
| 2308   | Layout 2 |
| 2302   | Layout 2 |
| 2295   | Layout 2 |
| 2290   | Layout 2 |
| 2284   | Layout 2 |
| 2276   | Layout 2 |
| 2269   | Layout 2 |
| 2259   | Layout 2 |
| 2250   | Layout 2 |
| 2243   | Layout 2 |
| 2235   | Layout 2 |
| 2229   | Layout 2 |
| 2224   | Layout 2 |
| 2218   | Layout 2 |
| 2215   | Layout 2 |
| 2207   | Layout 2 |
| 2203   | Layout 2 |
| 2196   | Layout 2 |
| 2192   | Layout 2 |
| 2189   | Layout 2 |
| 2183   | Layout 2 |
| 2179   | Layout 2 |
| 2171   | Layout 2 |
| 2163   | Layout 2 |
| 2156   | Layout 2 |
| 2151   | Layout 2 |
| 2147   | Layout 2 |
| 2142   | Layout 2 |
| 2138   | Layout 2 |
| 2134   | Layout 2 |
| 2130   | Layout 2 |
| 2122   | Layout 2 |
| 2107   | Layout 2 |
| 2098   | Layout 2 |
| 2089   | Layout 2 |
| 2081   | Layout 2 |
| 2073   | Layout 2 |
| 2067   | Layout 2 |
| 2063   | Layout 2 |
| 2059   | Layout 2 |
| 2052   | Layout 2 |
| 2044   | Layout 2 |
| 2039   | Layout 2 |
| 2032   | Layout 2 |
| 2025   | Layout 2 |
| 2011   | Layout 2 |
| 2005   | Layout 2 |
| 2000   | Layout 2 |
| 1996   | Layout 2 |
| 1991   | Layout 2 |
| 1985   | Layout 2 |
| 1980   | Layout 2 |
| 1969   | Layout 2 |
| 1964   | Layout 2 |
| 1958   | Layout 2 |
| 1950   | Layout 2 |
| 1945   | Layout 2 |
| 1937   | Layout 2 |
| 1933   | Layout 2 |
| 1927   | Layout 2 |
| 1921   | Layout 2 |
| 1914   | Layout 2 |
| 1908   | Layout 2 |
| 1897   | Layout 2 |
| 1892   | Layout 2 |
| 1886   | Layout 2 |
| 1881   | Layout 2 |
| 1871   | Layout 2 |
| 1866   | Layout 2 |
| 1862   | Layout 2 |
| 1854   | Layout 2 |
| 1846   | Layout 2 |
| 1838   | Layout 2 |
| 1832   | Layout 2 |
| 1826   | Layout 2 |
| 1822   | Layout 2 |
| 1818   | Layout 2 |
| 1804   | Layout 2 |
| 1794   | Layout 2 |
| 1790   | Layout 2 |
| 1784   | Layout 2 |
| 1774   | Layout 2 |
| 1771   | Layout 2 |
| 1762   | Layout 2 |
| 1759   | Layout 2 |
| 1754   | Layout 2 |
| 1749   | Layout 2 |
| 1743   | Layout 2 |
| 1737   | Layout 2 |
| 1731   | Layout 2 |
| 1725   | Layout 2 |
| 1717   | Layout 2 |
| 1710   | Layout 2 |
| 1704   | Layout 2 |
| 1698   | Layout 2 |
| 1690   | Layout 2 |
| 1685   | Layout 2 |
| 1680   | Layout 2 |
| 1674   | Layout 2 |
| 1668   | Layout 2 |
| 1659   | Layout 2 |
| 1649   | Layout 2 |
| 1642   | Layout 2 |
| 1636   | Layout 2 |
| 1628   | Layout 2 |
| 1622   | Layout 2 |
| 1614   | Layout 2 |
| 1608   | Layout 2 |
| 1602   | Layout 2 |
| 1598   | Layout 2 |
| 1594   | Layout 2 |
| 1590   | Layout 2 |
| 1587   | Layout 2 |
| 1584   | Layout 2 |
| 1579   | Layout 2 |
| 1572   | Layout 2 |
| 1565   | Layout 2 |
| 1559   | Layout 2 |
| 1554   | Layout 2 |
| 1547   | Layout 2 |
| 1537   | Layout 2 |
| 1529   | Layout 2 |
| 1524   | Layout 2 |
| 1519   | Layout 2 |
| 1509   | Layout 2 |
| 1506   | Layout 2 |
| 1504   | Layout 2 |
| 1500   | Layout 2 |
| 1493   | Layout 2 |
| 1489   | Layout 2 |
| 1485   | Layout 2 |
| 1481   | Layout 2 |
| 1474   | Layout 2 |
| 1466   | Layout 2 |
| 1462   | Layout 2 |
| 1459   | Layout 2 |
| 1453   | Layout 2 |
| 1450   | Layout 2 |
| 1445   | Layout 2 |
| 1439   | Layout 2 |
| 1433   | Layout 2 |
| 1430   | Layout 2 |
| 1426   | Layout 2 |
| 1421   | Layout 2 |
| 1417   | Layout 2 |
| 1416   | Layout 2 |
| 1409   | Layout 2 |
| 1405   | Layout 2 |
| 1401   | Layout 2 |
| 1396   | Layout 2 |
| 1391   | Layout 2 |
| 1390   | Layout 2 |
| 1386   | Layout 2 |
| 1381   | Layout 2 |
| 1379   | Layout 2 |
| 1372   | Layout 2 |
| 1366   | Layout 2 |
| 1364   | Layout 2 |
| 1363   | Layout 2 |
| 1360   | Layout 2 |
| 1358   | Layout 2 |
| 1355   | Layout 2 |
| 1351   | Layout 2 |
| 1348   | Layout 2 |
| 1346   | Layout 2 |
| 1341   | Layout 2 |
| 1340   | Layout 2 |
| 1338   | Layout 2 |
| 1335   | Layout 2 |
| 1333   | Layout 2 |
| 1329   | Layout 2 |
| 1327   | Layout 2 |
| 1324   | Layout 2 |
| 1321   | Layout 2 |
| 1319   | Layout 2 |
| 1318   | Layout 2 |
| 1316   | Layout 2 |
| 1313   | Layout 2 |
| 1311   | Layout 2 |
| 1309   | Layout 2 |
| 1304   | Layout 2 |
| 1292   | Layout 2 |
| 1286   | Layout 2 |
| 1280   | Layout 2 |
| 1276   | Layout 2 |
| 1267   | Layout 2 |
| 1261   | Layout 2 |
| 1256   | Layout 2 |
| 1250   | Layout 2 |
| 1246   | Layout 2 |
| 1239   | Layout 2 |
| 1230   | Layout 2 |
| 1226   | Layout 2 |
| 1220   | Layout 2 |
| 1217   | Layout 2 |
| 1211   | Layout 2 |
| 1210   | Layout 2 |
| 1208   | Layout 2 |
| 1203   | Layout 2 |
| 1197   | Layout 2 |
| 1194   | Layout 2 |
| 1192   | Layout 2 |
| 1187   | Layout 2 |
| 1183   | Layout 2 |
| 1177   | Layout 2 |
| 1173   | Layout 2 |
| 1167   | Layout 2 |
| 1164   | Layout 2 |
| 1156   | Layout 2 |
| 1149   | Layout 2 |
| 1144   | Layout 2 |
| 1137   | Layout 2 |
| 1132   | Layout 2 |
| 1127   | Layout 2 |
| 1122   | Layout 2 |
| 1118   | Layout 2 |
| 1114   | Layout 2 |
| 1109   | Layout 2 |
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
| 829    | Layout 2 |
| 822    | Layout 2 |
| 814    | Layout 2 |
| 805    | Layout 2 |
| 794    | Layout 1 |
| 787    | Layout 1 |
| 780    | Layout 1 |
| 771    | Layout 1 |
| 760    | Layout 1 |
| 748    | Layout 1 |
| 741    | Layout 1 |
| 736    | Layout 1 |
| 731    | Layout 1 |
| 723    | Layout 1 |
| 711    | Layout 1 |
| 707    | Layout 1 |
| 697    | Layout 1 |
| 689    | Layout 1 |
| 683    | Layout 1 |
| 678    | Layout 1 |
| 670    | Layout 1 |
| 661    | Layout 1 |
| 656    | Layout 1 |
| 652    | Layout 1 |
| 643    | Layout 1 |
| 637    | Layout 1 |
| 630    | Layout 1 |
| 627    | Layout 1 |
| 621    | Layout 1 |
| 617    | Layout 1 |
| 615    | Layout 1 |
| 606    | Layout 1 |
| 599    | Layout 1 |
| 592    | Layout 1 |
| 586    | Layout 1 |
| 577    | Layout 1 |
| 569    | Layout 1 |
| 561    | Layout 1 |
| 554    | Layout 1 |
| 542    | Layout 1 |
| 532    | Layout 1 |
| 531    | Layout 1 |
| 526    | Layout 1 |
| 521    | Layout 1 |
| 517    | Layout 1 |
| 510    | Layout 1 |
| 508    | Layout 1 |
| 504    | Layout 1 |
| 497    | Layout 1 |
| 491    | Layout 1 |
| 485    | Layout 1 |
| 478    | Layout 1 |
| 472    | Layout 1 |
| 466    | Layout 1 |
| 457    | Layout 1 |
| 452    | No file  |
| 449    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. Skill names come from LOC type 10, and each skill number opens its
[`skill.dbss`](skill_dbss.md) row.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type                | Field        | Notes                                                   |
| ------------------- | ------------------- | ------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]             | magic        | `PABR`                                                  |
| `+0x04`             | u32                 | width        | Sheet columns, `capacityX()` in the Lua; `17`           |
| `+0x08`             | u32                 | height       | Sheet rows, `capacityY()` in the Lua; `46` on client 3482 |
| `+0x0C`             | Cell[width][height] | cells        | `width * height` cells, column by column: cell `column * height + row` |
| `cells+0x00`        | String Table        | string_table | See String Table                                        |
| `string_table+0x00` | u32                 | table_start  | Offset of the string table, where `cells` ends          |
| `string_table+0x04` | u32                 | zero         | Always `0`                                              |

### Cell (4 bytes)

| Offset  | Type | Field      | Notes                                                        |
| ------- | ---- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8   | cell_type  | See Cell Types; `_cellType` in the Lua                       |
| `+0x01` | u8   | arrow_type | See Arrow Types; `0` on every cell of clients 1784 and 3482  |
| `+0x02` | u16  | skill_no   | `_skillNo` in the Lua: the skill when `cell_type` is `2`, else `0` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                  |
| ------- | ------------------ | ------------ | -------------------------------------- |
| `+0x00` | u32                | string_count | `0` in all eight files                 |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                |

## Layout 1

The file before it became a PABR file: no magic, no string table and no
trailer. Client 794 has a 17 by 27 guild grid, 1,844 bytes.

### File Layout

| Offset  | Type                | Field  | Notes                                                    |
| ------- | ------------------- | ------ | -------------------------------------------------------- |
| `+0x00` | u32                 | width  | Sheet columns                                            |
| `+0x04` | u32                 | height | Sheet rows                                               |
| `+0x08` | Cell[width][height] | cells  | `width * height` cells; the file ends after the last cell |

## Cell Types

The values of the
[`ui_skillgroup_*.bss` Cell Types](ui_skillgroup_bss.md#cell-types): `1`
Blank, `2` Skill, `3` to `11` the corner and junction pieces `LT` to `RB`,
`12` Hori, `13` Vert. On client 3482 the grid holds 705 Blank, 58 Skill, 18
Hori and 1 Vert cells; client 1784 also had the pieces `4`, `5`, `10` and
`11` once each.

## Arrow Types

`ge::UISkillTreeLayout_CellValueArrowType` of the 2016 PDB, as in
[`uipracticeskilltreelayout.bss`](uipracticeskilltreelayout_bss.md#arrow-types):
`0` None, `1` Left, `2` Right, `3` Top, `4` Bottom.

## Client Use

`PaGlobal_GuildSkill_All:initSkillTreeControl()` in
`panel_guildskill_all_1.luac` (client 3482) walks the grid row by row,
`cellTable:atPointer(col, row)` for every `col` below `capacityX()` and
`row` below `capacityY()`:

- A cell with `isSkillType()` becomes a skill slot for `_skillNo`, unless
  `getSkillTypeStaticStatus(skillNo):isValidLocalizing()` fails; then the
  slot stays empty and `hideInvalidateLine()` hides the lines that lead to it.
- A cell with `isLineType()` draws the line piece of its `_cellType` from the
  `Static_TypeS_*` controls (`LB`, `CB`, `RB`, `HORI`, `VERTI` and the rest).
- Even rows and columns are slot rows and columns, odd ones the narrow gaps
  between them. Every skill cell of the eight files sits on an even column
  and an even row (clients 1784 and 3482).

## Field Names

The cell is the 2016 `ge::UISkillTreeLayout_CellValue`, 4 bytes: u8
`_cellType`, u8 `_arrowType`, u16 `_skillNo`, in that order. The current Lua
still reads `_cellType` and `_skillNo` by those names.

A private server on client 1784 ships the sheets the eight files are built
from, under `DataSheet/reboot_datasheet/uiskilltree/`. Each is a grid
sheet with no column headers: `END` in the first row and in column A mark
its right and bottom edges, a cell holds a skill number or one line
character (`─ │ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘`), and the templates beside the grid
list the line pieces and the arrows `← → ↑ ↓`. The sheet's note says blue
cells take a skill number or `─` only and gray cells any line piece but no
skill number. Read column by column, with a number as type `2`, a line
character as its type and an empty cell as type `1`, the sheets match the
1784 files on every cell:

| Workbook                                | Sheet                 | File                                      | Grid    | Cells match |
| --------------------------------------- | --------------------- | ----------------------------------------- | ------- | ----------- |
| `uiguildskilltreelayout.xlsm`           | `GuildSkill`          | `uiguildskilltreelayout.bss`              | 17 x 44 | 748 of 748  |
| `uifusionskilltreelayout.xlsm`          | `FusionSkill`         | `uifusionskilltreelayout.bss`             | 5 x 2   | 10 of 10    |
| `uiproductskilltreelayout.xlsm`         | `ProductSkill`        | `uiproductskilltreelayout.bss`            | 21 x 15 | 315 of 315  |
| `uiterritorypolicyskilltreelayout.xlsm` | `BalenosPolicySkill`  | `ui_territorypolicyskilltree_balenos.bss` | 21 x 25 | 525 of 525  |
| `uiterritorypolicyskilltreelayout.xlsm` | `SerendiaPolicySkill` | `ui_territorypolicyskilltree_serendia.bss` | 21 x 33 | 693 of 693 |
| `uiterritorypolicyskilltreelayout.xlsm` | `CalpheonPolicySkill` | `ui_territorypolicyskilltree_calpheon.bss` | 21 x 33 | 693 of 693 |
| `uiterritorypolicyskilltreelayout.xlsm` | `MediaPolicySkill`    | `ui_territorypolicyskilltree_media.bss`   | 21 x 31 | 651 of 651  |
| `uiterritorypolicyskilltreelayout.xlsm` | `ValenciaPolicySkill` | `ui_territorypolicyskilltree_valencia.bss` | 21 x 31 | 651 of 651 |

The fusion grid fixes the cell order: its sheet holds skills in A1, C1 and
E1, the file has them at cells `0`, `4` and `8`, which is `column * 2 + row`
for columns 0, 2 and 4. Row by row they would be A1, E1 and D2. The older
copy of the guild workbook under `DataSheet/skilldatasheet/uiskilltree/` has
a 40-row sheet that lacks the skills `65123` to `65126`.

## Notes

- The guild grid changed between clients 1784 (17 by 44, 102 skills, skill
  numbers `65001` to `65332`) and 3482 (17 by 46, 58 skills, `62844` to
  `65332`). On client 3482 all 58 are rows of
  [`skill.dbss`](skill_dbss.md) and of [`guildskill.bss`](guildskill_bss.md).
- No arrow appears in any grid of the eight files on clients 1784 and
  3482: the arrows exist only in the sheet templates.
