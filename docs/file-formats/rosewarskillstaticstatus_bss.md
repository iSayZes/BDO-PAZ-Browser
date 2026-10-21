# `rosewarskillstaticstatus.bss` Format

## Purpose

The Rose War team skills the commander uses from the team skill panel: one
row per `__eRoseWarSkillType_*` value with the skill number for each team.
On client 3474 the file has 7 rows, skill types `1` to `7`, and the two
teams share every skill but Bombard (Powerful Attack), which summons King
Griffon for Kamasylvia and Fugitive Khalk for O'dyllita.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `rosewarskillstaticstatus.bss` | 76    | 7 Row   | 8         |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `rosewarskillstaticstatus.bss` | 76 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (8 bytes)

| Offset  | Type | Field               | Notes                                                                 |
| ------- | ---- | ------------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | skill_type          | `__eRoseWarSkillType_*` value; see Skill Types                        |
| `+0x04` | u16  | kamasylvia_skill_no | `skill.dbss` skill number for team `0` (Kamasylvia); LOC type 10 name |
| `+0x06` | u16  | odyllita_skill_no   | Skill number for team `1` (O'dyllita)                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Skill Types

`panel_rosewar_teamskill.luac` (client 3474) lists the skill types in this
order, and the Lua reads each skill with `ToClient_GetRoseWarSkillKey(skillType)`
and `getSkillStaticStatus(skillNo, 1)`. The Lua holds the names only; the
values are the list position from `1`, and each value's skill text (LOC type
10, `str_id4` 1) matches its name:

| `skill_type` | Lua name                                 | Skills on client 3474 | Name (LOC type 10)                       |
| ------------ | ---------------------------------------- | --------------------- | ---------------------------------------- |
| `1`          | `__eRoseWarSkillType_Scan`               | `15280`               | Enhance Vision                           |
| `2`          | `__eRoseWarSkillType_Recall`             | `15281`               | Rally Forces (teleports a platoon)       |
| `3`          | `__eRoseWarSkillType_Bombard`            | `15282`, `15286`      | Powerful Attack (King Griffon, Fugitive Khalk) |
| `4`          | `__eRoseWarSkillType_Summon`             | `15283`               | Summon Ogre                              |
| `5`          | `__eRoseWarSkillType_Conceal`            | `15284`               | Obscure Vision                           |
| `6`          | `__eRoseWarSkillType_Zonya`              | `15285`               | Immobilize Guardians                     |
| `7`          | `__eRoseWarSkillType_FixedResurrection`  | `15287`               | Strategic Revival                        |

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it; the names come from the client
Lua and LOC. Both skill numbers resolve to LOC type 10 skill names. The team
split follows the Bombard row: `15282` summons King Griffon, which LOC places
in the Ash Forest of Kamasylvia (item `42545`), and `15286` summons Fugitive
Khalk, and the Khalk attack alongside the Ahib in the Ahib Conflict Zone
quests (LOC type 18 `7200`, `7211`). Team `0` is Kamasylvia and team `1`
O'dyllita in [`rosewarteamnostaticstatus.bss`](rosewarteamnostaticstatus_bss.md).

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 07 00 00 00 01 00 00 00 B0 3B B0 3B 02 00 00 00 B1 3B B1 3B 03 00 00 00 B2 3B B6 3B 04 00 00 00 B3 3B B3 3B 05 00 00 00 B4 3B B4 3B 06 00 00 00 B5 3B B5 3B 07 00 00 00 B7 3B B7 3B 00 00 00 00 40 00 00 00 00 00 00 00`
  (76 bytes). The file is not in the archives of client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  with the skill type's Lua name and both skill names.
