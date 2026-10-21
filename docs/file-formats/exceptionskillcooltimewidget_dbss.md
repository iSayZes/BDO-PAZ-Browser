# `exceptionskillcooltimewidget.dbss` Format

## Purpose

The skills the skill cooldown window lists under another skill's name. The
window (`panel_window_skill_cooltimeslot.luac`,
`panel_window_skillgroup_cooltimeslot_1.luac`) walks the class's skill trees
and asks each usable skill with a cooldown for
`getExceptionSkillCoolTime()`. A non-zero answer is a skill number, and the
slot then shows that skill's name and number in place of its own. A row maps
one skill to the skill shown for it, for the classes in its class mask,
together with a third skill the sheet calls `SkillLearnCheckNo`.

On client 3474 the 6 rows are:

| Skill                         | Class     | Shown skill                                | Learn check skill                          |
| ----------------------------- | --------- | ------------------------------------------ | ------------------------------------------ |
| `5764` Absolute: Vengeful Star | Nova      | `5973` Succession: Vengeful Star          | `5939` Succession: Ancient Pact            |
| `5831` Quoratum's Opening     | Nova      | `5997` Succession: Quoratum's Opening      | `5939` Succession: Ancient Pact            |
| `2902` Absolute: Weakling Hunt | Berserker | `5459` Succession: Weakling Hunt          | `5410` Succession: Feral Roar              |
| `1209` Imminent Doom          | Sorceress | `4859` Succession: Imminent Doom           | `4569` Prime: Dream of Doom I              |
| `1401` Twisting Wind          | Ranger    | `7153` Succession: Twisting Wind           | `4107` Succession: Feathers of Lemoria     |
| `94` Ultimate: Dark Flame     | Sorceress | `4840` Succession: Ultimate: Dark Flame    | `4594` Prime: Dark Flame                   |

The names are LOC type 10. On client 3474 each shown skill is the
Succession version of its skill, and on every client below each learn check
skill is a Succession or Prime skill of the row's class. Client 1784 has 7 rows: the `5831`, `1209` and `94` rows above,
unchanged, a Maehwa row (`3229` Absolute: Maehwa's Will to `6793`, check
`4170`) and three Valkyrie rows (`736` to `738`, Shield Chase I to III, to
`5325`, `4857` and `4858`, check `4135` Succession: Valkyrie's Vow).
Client 1485 has 5 of those rows: `1209`, the three Valkyrie rows and `94`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                      | Bytes | Records     | Row bytes |
| ------ | -------------- | ------- | ----------------------------------------- | ----- | ----------- | --------- |
| 1      | 1485 and later | 3474    | `exceptionskillcooltimewidget.dbss`       | 140   | 6 Row       | 20        |
| 1      | 1485 and later | 3474    | `exceptionskillcooltimewidgetoffset.dbss` | 76    | 6 Index Row | 12        |

| Layout | File                                      | Known          | Unknown    |
| ------ | ----------------------------------------- | -------------- | ---------- |
| 1      | `exceptionskillcooltimewidget.dbss`       | 140 B (100.0%) | 0 B (0.0%) |
| 1      | `exceptionskillcooltimewidgetoffset.dbss` | 76 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The rows have a fixed size and are read in file order;
`exceptionskillcooltimewidgetoffset.dbss` (below) is not needed. Skill
names come from LOC type 10 and class names from LOC type 21.

The skill key is the one shared by the whole skill cluster; see
[`skill.dbss` Skill Keys](skill_dbss.md#skill-keys). All multi-byte values
are little-endian.

## Layout 1

### File Layout

A `PABR` table of fixed rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset      | Type       | Field        | Notes                                       |
| ----------- | ---------- | ------------ | ------------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                      |
| `+0x04`     | u32        | count        | Number of rows                              |
| `+0x08`     | Row[count] | rows         | See Row                                     |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table            |
| `rows+0x04` | u32        | table_start  | End of the rows (`8 + 20 * count`)          |
| `rows+0x08` | u32        | zero         | Always `0`                                  |

### Row (20 bytes)

| Offset  | Type | Field                 | Notes                                                                    |
| ------- | ---- | --------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | skill_key_from        | `SkillNoFrom << 16 \| 1`: the skill whose slot is replaced; unique       |
| `+0x04` | u64  | class_mask            | Bit `n` set for class type `n` of the `ClassType` list                   |
| `+0x0C` | u32  | skill_key_to          | `SkillNoTo << 16 \| 1`: the skill shown in the slot                      |
| `+0x10` | u32  | skill_learn_check_key | `SkillLearnCheckNo << 16 \| 1`                                           |

Every key on clients 1784 and 3474 has level `1`, and every class mask one
bit: `0x10` Ranger, `0x100` Sorceress, `0x200` Nova, `0x1000` Berserker,
`0x200000` Maehwa, `0x1000000` Valkyrie.

### `exceptionskillcooltimewidgetoffset.dbss`

A bare index: no `PABR` magic and no trailer. Read by
`parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type             | Field | Notes                                          |
| ------- | ---------------- | ----- | ---------------------------------------------- |
| `+0x00` | u32              | count | Equals the main file's `count`                 |
| `+0x04` | Index Row[count] | rows  | See Index Row                                  |

### Index Row (12 bytes)

| Offset  | Type | Field          | Notes                                                       |
| ------- | ---- | -------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | skill_key_from | Key of the row it points at                                 |
| `+0x04` | u32  | offset         | Start of that row in the main file, at its `skill_key_from` |
| `+0x08` | u32  | size           | `20`, the whole row                                         |

On clients 1784 and 3474 the index rows run in reverse file order and each
points at the row with its key.

## Field Names

The names are the columns of the `SetCoolTimeWidget` sheet of a private
server's `DataSheets.bexcel` on client 1784: `ClassType`, `SkillNoFrom`,
`SkillNoTo`, `SkillLearnCheckNo` and `ContentsOption`. Its 7 rows match the
7 rows of the official client 1784 file in every stored column, and client
3474 shares 3 of them (`5831`, `1209`, `94`) unchanged; its other 3 rows are
new. The server dump of the same private server holds the RTTI names
`ExceptionSkillCoolTimeWidgetStaticStatus` and
`ExceptionSkillCoolTimeWidgetStaticStatusManager`.

Its loader, `Load_SetCoolTimeWidget` (VA `0x140a21df0`), fixes the widths
and the order:

- `SkillNoFrom`, `SkillNoTo` and `SkillLearnCheckNo` are read as int64 and
  each stored as the u16 skill number above a u16 level `1`, the skill key.
- `ClassType` is a delimited list. Each value is parsed as u32 and, when
  below `0x33`, sets bit `value` of a 64-bit mask.
- `ContentsOption` is a list of contents option values (`1369` to `1475`
  in the sheet). The loader skips a row whose list fails its contents
  option check; the file has no column for them.

The client 519 tables of a private server and the 2016 PDB have no such
table.

## Notes

- `ToClient_checkExceptionSkillSetting()` runs before the window fills its
  list, and the Lua reads the shown skill through
  `getSkillStaticStatus(skillNo, 1):getExceptionSkillCoolTime()`, the level 1
  skill that `skill_key_from` names. The Lua never reads the class mask or
  the learn check skill; the client checks them before it answers.
- The 1784 rows the 3474 file drops are the Maehwa and Valkyrie rows; their
  `ContentsOption` values in the sheet are `1373` and `1374`.

## Open Questions

### What the Learn Check Skill Gates

The column name says the client checks whether `SkillLearnCheckNo` is
learned, and every such skill is a Succession or Prime skill of the row's
class. Whether the swap happens only with that skill learned, or the skill
is checked for another reason, is not in the Lua; the check is inside
`ToClient_checkExceptionSkillSetting()` or `getExceptionSkillCoolTime()`
in the client.
