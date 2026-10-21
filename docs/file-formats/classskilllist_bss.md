# `classskilllist.bss` Format

## Purpose

The skill list of each playable class for the Skill Guide widget: one
row per class type with the skill numbers whose key commands it can show.
The server of client 1784 loads the same data in
`GameCommonParameterLoaderFromExcel::loadMain(LoadClassSkillCommandList)`,
which logs `ClassType(%#):ClassSkillCommandList`, right before
`LoadSkillCommandList`. Every skill number in the file is a key of
`skillcommand.dbss` (517 of 517 distinct numbers, client 3473), the table of
skill command records.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records      | Row bytes               |
| ------ | -------------- | ------- | -------------------- | ----- | ------------ | ----------------------- |
| 1      | 1230 and later | 3474    | `classskilllist.bss` | 1,372 | 32 Class Row | 25 to 53, 42 on average |

| Layout | File                 | Known            | Unknown    |
| ------ | -------------------- | ---------------- | ---------- |
| 1      | `classskilllist.bss` | 1,372 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | Layout 1             |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

The file is self-contained. The handler reads names through the shared LOC
lookup:

| File                  | Required | Role                                                              |
| --------------------- | -------- | ----------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Class names (LOC type `21`, `str_id1` = class type) and skill names (LOC type `10`, `str_id1` = skill number) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                  | Field              | Notes                                                        |
| ------------------- | --------------------- | ------------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]               | magic              | `PABR` (ASCII)                                               |
| `+0x04`             | u32                   | class_count        | Number of rows; `32` on client 3473                          |
| `+0x08`             | Class Row[class_count] | rows              | See Class Row                                                |
| `rows+0x00`         | String Table          | string_table       | The PABR string table, present but empty                     |
| `string_table+0x00` | u32                   | string_table_start | Absolute offset of `string_count`, where the rows end        |
| `string_table+0x04` | u32                   | zero               | Always `0`                                                   |

On client 3473 the 32 rows end at `0x550`, the stored `string_table_start`,
and the file is 1,372 bytes. The parser rejects a file whose rows do not end
there.

### Class Row (variable: 9 bytes + skill numbers)

| Offset  | Type             | Field       | Notes                                                                   |
| ------- | ---------------- | ----------- | ----------------------------------------------------------------------- |
| `+0x00` | u8               | class_type  | The class type `getClassType()` returns, LOC type `21` names it; unique |
| `+0x01` | u64              | skill_count | Number of skill numbers that follow; `8` to `22` on client 3473          |
| `+0x09` | u16[skill_count] | skill_nos   | Skill numbers (`skill_key >> 16`), LOC type `10` names them             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Notes

- On client 3473 the 32 rows cover every playable class type from `0` to
  `35` except the unused `13`, `14`, `18` and `22`. They are not sorted:
  `34` (Deadeye) comes before `32` (Seraph) and `35` (Agent).
- Each row lists skills of its own class by LOC name: row `0` (Warrior)
  starts with `216` Ground Roar, `1021` Spinning Slash and `1022` Charging
  Thrust. Wizard (`28`) and Witch (`31`) share their first 8 numbers
  (Fireball, Lightning, Meteor Shower and others), Kunoichi (`25`) and Ninja
  (`26`) share 5.
- A row can list a number twice: on client 3473 the Guardian row (`5`)
  holds `5011` Fierce Disdain and `5082` Mutilation twice each. No other
  row repeats a number.
- The client Lua of the Skill Guide (`ui_widget_skillcommand.luac`)
  calls `ToClient_RequestCommandList()` and receives one
  `FromClient_SkillCommandList(skillNo, isAwaken)` call per skill. The
  `isAwaken` flag is not stored in this file.
- The `binary/classskilllist.bss` of a private server on client 1784 has the
  same layout with 24 rows.
- Checked in game on client 3474 with a Wizard: the Skill Guide (Edit UI,
  hidden in safe zones) lists the Wizard row in file order. The main
  weapon shows the eight main weapon numbers and the awakening weapon the
  five awakening ones (`2212` Lava Field to `2232` Cataclysm). Each line
  shows the highest learned rank (`ToClient_GetTopLevelLearnActiveSkillNo`
  in the Lua), so `818` Fireball I and `819` Fireball II share the one
  "Absolute: Fireball" line.
