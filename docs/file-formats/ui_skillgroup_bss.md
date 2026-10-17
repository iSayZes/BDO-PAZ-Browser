# `ui_skillgroup_*.bss` Format

## Purpose

The skill window layout of every class: one grid per class, cell by cell,
with the skill groups placed on it, the connecting lines between them, and the
tabs the skills are sorted into. Three files share the format:

| File                           | Window           | Classes on client 3458 |
| ------------------------------ | ---------------- | ---------------------- |
| `ui_skillgroup_combat.bss`     | Combat skills    | 32                     |
| `ui_skillgroup_awakening.bss`  | Awakening skills | 32                     |
| `ui_skillgroup_succession.bss` | Succession       | 0 (empty)              |

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes   | Records                                            | Row bytes             |
| ------ | -------------- | ------- | ------------------------------ | ------- | -------------------------------------------------- | --------------------- |
| 1      | 1784 and later | 3474    | `ui_skillgroup_awakening.bss`  | 69,380  | 7,552 Cell, 32 Class Grid, 68 Tab, 32 Class Tabs   | 9 to 11, 9 on average |
| 1      | 1784 and later | 3474    | `ui_skillgroup_combat.bss`     | 242,103 | 26,224 Cell, 32 Class Grid, 160 Tab, 32 Class Tabs | 9 to 11, 9 on average |
| 1      | 1784 and later | 3474    | `ui_skillgroup_succession.bss` | 230     | 1 String Table                                     | 4                     |

| Layout | File                           | Known             | Unknown          |
| ------ | ------------------------------ | ----------------- | ---------------- |
| 1      | `ui_skillgroup_awakening.bss`  | 61,498 B (88.6%)  | 7,882 B (11.4%)  |
| 1      | `ui_skillgroup_combat.bss`     | 215,549 B (89.0%) | 26,554 B (11.0%) |
| 1      | `ui_skillgroup_succession.bss` | 28 B (12.2%)      | 202 B (87.8%)    |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                              |
| --------------------- | -------- | ----------------------------------------------------------------- |
| `skillgroup.bss`      | Optional | The skills of each placed group, see [`skillgroup.bss`](skillgroup_bss.md) |
| `stringtable.bss`     | Optional | Hash of each tab name key, see [`stringtable.bss`](stringtable_bss.md) |
| `languagedata_en.loc` | Optional | Class names (type `21`) and tab names (type `37`, `GAME` sheet)   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file of class grids, then a tab directory and a class table, then the
shared counted string table and 8-byte trailer (see
[`npcsimply.bss` String Table](npcsimply_bss.md#string-table-variable-4-bytes--strings)).

| Offset                     | Type                         | Field               | Notes                                           |
| -------------------------- | ---------------------------- | ------------------- | ----------------------------------------------- |
| `+0x00`                    | char[4]                      | magic               | `PABR`                                          |
| `+0x04`                    | u32                          | class_count         | Number of class grids                           |
| `+0x08`                    | Class Grid[class_count]      | grids               | One per class, see Class Grid                   |
| `grids+0x00`               | u32                          | tab_class_count     | Number of tab entries, equal to `class_count`   |
| `grids+0x04`               | Class Tabs[tab_class_count]  | tabs                | One per class, see Class Tabs                   |
| `tabs+0x00`                | u32                          | class_slots         | Always `101`                                    |
| `tabs+0x04`                | u16[class_slots]             | unknown_class_table | Indexed by class type, see Open Questions       |
| `unknown_class_table+0x00` | String Table                 | string_table        | Tab name keys, e.g. `LUA_SKILLTREE_PANEL_NAME0` |
| `string_table+0x00`        | u32                          | string_table_start  | Where `unknown_class_table` ends                |
| `string_table+0x04`        | u32                          | zero                | Always `0`                                      |

`ui_skillgroup_succession.bss` has `class_count` `0`, no tabs, the class
table and an empty string table.

### Class Grid (variable: 9 bytes + cells)

| Offset  | Type                | Field      | Notes                                                                    |
| ------- | ------------------- | ---------- | ------------------------------------------------------------------------ |
| `+0x00` | u8                  | class_type | Class, LOC type `21` (`0` Warrior, `4` Ranger, `32` Seraph)              |
| `+0x01` | u32                 | width      | Grid columns; `8` on every class                                         |
| `+0x05` | u32                 | height     | Grid rows; `42` to `123` in the combat window, `21` to `38` in awakening |
| `+0x09` | Cell[height][width] | cells      | `width * height` cells, row by row                                       |

### Cell (variable: 8 bytes + types)

| Offset        | Type           | Field                  | Notes                                                         |
| ------------- | -------------- | ---------------------- | ------------------------------------------------------------- |
| `+0x00`       | u32            | type_count             | Number of drawing types                                       |
| `+0x04`       | u8[type_count] | types                  | Cell types, see Cell Types; `2` means the cell holds a skill group |
| `types+0x00`  | u16            | group_no               | `skillgroup.bss` group when `types` holds `2`                 |
| `types+0x02`  | u8             | unknown_after_group_no | `0` on every skill cell                                       |
| `types+0x03`  | u8             | subgroup               | The tab the skill is listed under, see Tabs                   |

### Class Tabs (variable: 9 bytes + tabs)

| Offset  | Type           | Field      | Notes                                |
| ------- | -------------- | ---------- | ------------------------------------ |
| `+0x00` | u8             | class_type | Same classes as the grids            |
| `+0x01` | u32            | tab_count  | `4` for every combat class; `1` to `4` in awakening |
| `+0x05` | u32            | unknown_05 | Always `0`                           |
| `+0x09` | Tab[tab_count] | tabs       | See Tab                              |

### Tab (5 bytes)

| Offset  | Type | Field        | Notes                                      |
| ------- | ---- | ------------ | ------------------------------------------ |
| `+0x00` | u32  | string_index | String table index of the tab name key     |
| `+0x04` | u8   | subgroup     | The `subgroup` the tab names               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Cell Types

The client enum is `__eSkillGroupCellType_*`. Its values are not in any Lua
file (the client defines them), but the skill window script
(`luacscript/x64/window/skill/panel_window_skillgroup_all_1.luac`) draws
every type from `3` up with the line sprite `type - 2`, and those sprites
(`Combine_Etc_Skill_LineA_01` to `_11` in `Combine_Etc_Skill_01.dds`) are
box-drawing pieces. The enum names follow a 3 by 3 grid of left, centre,
right and top, middle, bottom.

| Value | Enum         | Draws | Combat cells |
| ----- | ------------ | ----- | ------------ |
| 0     | `Undefined`  |       | 0            |
| 1     | `Blank`      | Nothing | 21,363     |
| 2     | `SkillGroup` | A skill group | 2,546 |
| 3     | `LT`         | ┌     | 0            |
| 4     | `CT`         | ┬     | 449          |
| 5     | `RT`         | ┐     | 61           |
| 6     | `LM`         | ├     | 80           |
| 7     | `CM`         | ┼     | 5            |
| 8     | `RM`         | ┤     | 0            |
| 9     | `LB`         | └     | 408          |
| 10    | `CB`         | ┴     | 4            |
| 11    | `RB`         | ┘     | 3            |
| 12    | `Hori`       | ─     | 4,013        |
| 13    | `Vert`       | │     | 590          |

`CT` and `RT` are the two names the script never uses; they are placed by
the grid naming. The script adds one extra vertical piece for `LM`, `CM`,
`RM`, `LB`, `CB`, `RB` and `Vert`, exactly the pieces whose line reaches the
top edge of the cell. `TypeCount` (14) ends the enum.

All 2,091 combat and 788 awakening groups placed on a grid are in
`skillgroup.bss`.

## Tabs

Each tab names a `subgroup` by a string table index. Every `subgroup` a
class's cells use is one of its tabs. The string is a `GAME` sheet key, so
the English tab name is LOC type `37` with the key's
[`stringtable.bss`](stringtable_bss.md) hash and `str_id2 = 1`:

| Key                              | English (LOC)                                   |
| -------------------------------- | ----------------------------------------------- |
| `LUA_SKILLTREE_PANEL_NAME0`      | Main Skills                                     |
| `LUA_SKILLTREE_PANEL_NAME3`      | Secondary Skills                                |
| `LUA_SKILLTREE_PANEL_NAME1`      | Passives                                        |
| `LUA_SKILLTREE_PANEL_NAME6`      | Ascension Skill                                 |
| `LUA_SKILLTREE_PANEL_NAME5`      | Selected Skills                                 |
| `LUA_SKILLTREE_PANEL_PJKD_NAME`  | Fighting Buddha Skills                          |
| `LUA_SKILLTREE_PANEL_PNYW_NAME`  | Flow Skills                                     |
| `LUA_SKILLTREE_PANEL_PQW_NAME`   | Dragonblood Skills - "Bloodbearer of the Skysoaring Dragon" |
| `LUA_SKILLTREE_PANEL_PQW_NAME2`  | Hexeblood Skills - "Bloodbearer of the Landroving Witch" |
| `LUA_SKILLTREE_PANEL_PDKL_NAME`  | Champion of the Holy Covenant                   |
| `LUA_SKILLTREE_PANEL_PDKL_NAME2` | Avatar of Condemnation                          |

The combat window uses the first four for every class, in the same order.
In the awakening window 27 classes have Main Skills and Selected Skills.
Wukong (3), Scholar (6), Drakania (7) and Seraph (32) add or swap in
class-specific tabs. Shai (17) has only Main Skills: her awakening is the
Sol talents, not an awakening weapon. Agent (35) has a grid and tabs but no
skill cells; Agent has no awakening weapon yet (2026-09-28).

In game the two windows are the Main and Awakening tabs of the skill
window, and each tab lists its sections by `subgroup` number, not in the
order of the tab entries. Checked 2026-09-29:

- Wizard (28), Main: Main Skills, Secondary Skills, Passives. Awakening:
  Main Skills, Selected Skills.
- Scholar (6), Awakening: Main Skills, Flow Skills, Selected Skills, with
  the skills the file places under each.
- Drakania (7), Awakening: Main Skills, Hexeblood Skills, Dragonblood
  Skills, Selected Skills. The tab entries run Main Skills (subgroup `0`),
  Dragonblood (`2`), Hexeblood (`1`), Selected Skills (`3`), so the window
  sorts by `subgroup`. The two blood tabs are separate skill groups: both
  have Tip of the Scale, Spiteful Soul, Sundering Roar, Crackling Flame,
  Savage Decree, Storm Piercer and Tectonic Slam; Hexeblood adds Extinction,
  Flow: Concealed Claw, Flow: Obliterate and Storm Maul; Dragonblood adds
  Flow: Cloud's Strife, Aerial Burst and Doombringer.

The window no longer draws the tree: each section is a list of skill cards
in three columns, and the grid is the three columns stacked: a cell's card
column is `row * 3 // height` (`0` left, `1` middle, `2` right). The skill
rows of every class in both windows fall in three runs split by two wide
blank gaps (at least three times any other gap), and the thirds rule puts
all 3,334 skill cells in the same run.

Drakania's Awakening grid is 38 rows, so its columns start at rows `0`,
`13` and `26` (checked 2026-09-29). Main Skills shows Burning Resolve, Fate
Beckons, Trion Training (row `0`) on the left, Legacy, Flow: Dragon Flight,
Impale (rows `14` and `15`) in the middle and Elvia: Edict Unbound (row
`28`) on the right. Over all four sections the three columns hold 13, 11
and 10 skills in game, exactly the file's skill cells per third. Inside a
column the cards follow the cells row by row. Hexeblood's middle column has an empty card slot after Extinction,
probably an empty grid cell between Extinction and Storm Piercer.

Elvia: Edict Unbound is usable only while the 10-minute Elvia weapon buff
from the Elvia realm is active, so the grid lists temporary skills too.

The Ascension Skill section holds skills that equipped items grant, the
same three on all 32 classes, each ranked PRI to PEN with the item's
enhancement level:

| Skill               | Item                      |
| ------------------- | ------------------------- |
| Blessing of Taebaek | Taebaek's Belt (`12282`)  |
| Blessing of Asadal  | Asadal Necklace (`11688`) |
| Fury of Asadal      | Asadal Belt (`12285`)     |

The skill window script tests `LUA_SKILLTREE_PANEL_NAME6` next to
`_isActiveItemGroup` and `PaGlobalFunc_SkillGroup_All_IsActiveItemSkill`,
and the section did not show on my Wizard, so it most likely appears only
while one of the items is equipped. Taebaek's Belt: see the GrumpyG guide
(grumpygreen.cricket/taebaeks-belt).

## Notes

- The grid and cell layout comes from bdo-data-extractor, which keeps the
  tab directory and class table as an opaque footer. Both are decoded here
  and walk exactly to the string table on all three files.
- The tab pairs read `u32 string_index` then `u8 subgroup`. In the combat
  window the two are equal for every tab, so only the awakening window (for
  example Scholar: strings `0`, `3`, `1` for subgroups `0`, `1`, `2`) shows
  the order. The game sorts the sections by `subgroup` (Drakania, see Tabs).

## Open Questions

### What is `unknown_class_table`?

101 u16 values, one per LOC type `21` class slot (types `0` to `100`). 26 are
non-zero, at the same indexes in both windows, and the values are close
between the windows (Warrior `596` and `563`, class `1` `10057` and `10045`).
They are not byte offsets of the class grids.
