# `skillcomboguide.bss` Format

## Purpose

The skill combos of the combo guide, per class: each combo is a chain of
two to seven skills with the key binding text of every step. The first
combo of client 3482 is Hashashin skill 5534 (`MoveBack` + `Kick`), then
5501 (`Attack1`), then 5524 (`Dash` + `Attack2`). The skill command widget
shows the learned combos of the current class above the skill command
list.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes  | Records                                | Row bytes |
| ------ | -------------- | ------- | --------------------- | ------ | -------------------------------------- | --------- |
| 1      | 1485 and later | 3482    | `skillcomboguide.bss` | 18,240 | 1,072 Step, 321 Combo, 26 Class Combos | 6         |

| Layout | File                  | Known             | Unknown    |
| ------ | --------------------- | ----------------- | ---------- |
| 1      | `skillcomboguide.bss` | 18,240 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | No file  |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                    |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| `stringtable.bss`     | Optional | Hash of each `[ComboSheet_CommonString_N]` key in a command, `GAME` sheet |
| `languagedata_en.loc` | Optional | Class names (type `21`), skill names (type `10`), command words (type `37`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                       | Field        | Notes                                         |
| ------------------- | -------------------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]                    | magic        | `PABR`                                        |
| `+0x04`             | u32                        | class_count  | Number of class lists                         |
| `+0x08`             | Class Combos[class_count]  | classes      | One per class, in no class order; see Class Combos |
| `classes+0x00`      | String Table               | string_table | The command texts                             |
| `string_table+0x00` | u32                        | table_start  | Offset of the string table, where `classes` ends |
| `string_table+0x04` | u32                        | zero         | Always `0`                                    |

### Class Combos (variable: 4 bytes + combos)

| Offset  | Type              | Field       | Notes                                              |
| ------- | ----------------- | ----------- | -------------------------------------------------- |
| `+0x00` | u32               | combo_count | Number of combos of the class                      |
| `+0x04` | Combo[combo_count]| combos      | Every combo holds the same `class_type`; see Combo |

### Combo (variable: 9 bytes + steps)

| Offset  | Type              | Field             | Notes                                                    |
| ------- | ----------------- | ----------------- | -------------------------------------------------------- |
| `+0x00` | u8                | class_type        | Class, LOC type `21` (`1` Hashashin)                     |
| `+0x01` | u32               | combo_skill_count | Number of skills in the combo; equal to `step_count` on every combo |
| `+0x05` | u32               | step_count        | Number of `steps`; `2` to `7` on client 3482             |
| `+0x09` | Step[step_count]  | steps             | The skills in order; see Step                            |

### Step (6 bytes)

| Offset  | Type | Field         | Notes                                                      |
| ------- | ---- | ------------- | ---------------------------------------------------------- |
| `+0x00` | u16  | skill_no      | Skill number, LOC type `10`                                |
| `+0x02` | u32  | command_index | String table index of the step's key binding text; see Commands |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; 83 on client 3482      |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries, each text stored once |

## Commands

A command is the key binding text of one step, the same text LOC type 2
holds for the skill (`str_id4` 1): `<{KeyBind:MoveBack}> + <{KeyBind:Kick}>`
for skill 5534, Sand Divider I. Each `{KeyBind:Name}` is a player action
whose key the game fills from the key settings, and the angle brackets
draw it as a key. Words between the keys are `GAME` sheet keys of
[`stringtable.bss`](stringtable_bss.md) in square brackets; the English is
LOC type 37 under the key's hash. Client 3482 uses these eight:

| Key                          | English (LOC)          |
| ---------------------------- | ---------------------- |
| `ComboSheet_CommonString_1`  | Directional Key        |
| `ComboSheet_CommonString_2`  | Maintain               |
| `ComboSheet_CommonString_3`  | Back                   |
| `ComboSheet_CommonString_4`  | Sprinting              |
| `ComboSheet_CommonString_5`  | While Jumping          |
| `ComboSheet_CommonString_6`  | Leaping laterally      |
| `ComboSheet_CommonString_7`  | Jumping in a direction |
| `ComboSheet_CommonString_8`  | While charging         |

`[/]` between two keys (`<{KeyBind:MoveLeft}> [/] <{KeyBind:MoveRight}>`)
is a literal "or".

## Field Names

The `Skill_Combo` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `ClassType`, `ComboSkillCount`, `ComboType`, then
`Combo1` to `Combo10` and `Command1` to `Command10`; the developer workbook
`datasheet_skillcomboguide.xlsm` adds the note columns `#ComboIndex`,
`#LimitLevel`, `#Reward` and `#Desc`. Its 280 rows match the file combo by
combo in class, position within the class, skills and command texts: 280
of 280 on client 1784 and 280 of 280 on client 3482.

| Field             | Column            |
| ----------------- | ----------------- |
| class_type        | `ClassType`       |
| combo_skill_count | `ComboSkillCount` |
| skill_no          | `Combo1` to `Combo10` |
| command_index     | `Command1` to `Command10`, stored once in the string table |

`ComboType` is `0` on every sheet row and has no byte in the file. The file
of client 1784 adds class 10 (290 combos, 23 classes); client 3482 adds
classes 7, 10, 15 and 30 (321 combos, 26 classes). The 2016 PDB has no
struct for the table.

## Notes

- `ui_widget_skillcommand.luac` (client 3482) reads the learned combos
  with `Toclient_getLearnSkillComboListCount()`,
  `Toclient_getSkillComboListCount(index)`,
  `Toclient_getLearnSkillComboListSkillNo(index, step)` and
  `Toclient_getLearnSkillComboListCommand(index, step)`, joins the commands
  with ` | ` and draws them while `_ContentsGroup_SkillComboGuide` is on.
  It skips combos whose `Toclient_getLearnSkillComboType(index)` differs
  from the current skill type of the player.
- The class lists follow no class order (`1`, `16`, ... on client 3482);
  inside a list the combos keep the sheet order.

## Open Questions

### Where the Combo Type Comes From

The widget compares `Toclient_getLearnSkillComboType()` with the player's
current skill type (`0` when the class has no Succession), but the file has
no type byte and the sheet's `ComboType` is `0` on every row. The client
may take it from the skills of the combo.
