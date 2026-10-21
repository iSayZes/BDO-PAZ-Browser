# `guildskill.bss` Format

## Purpose

The list of guild skills: one row per skill key, every one at level `1`.
On client 3474 the file has 766 rows, skill numbers 62xxx (585), 65xxx
(177) and the four Giant Mudster boss summons 54414 to 54417. The rows are
the skills of [skill](skill_dbss.md) by their `skill_key`; guild skills cost
guild points, whose levels are in
[guildskillexperience](guildskillexperience_dbss.md).
[guildspecialskillright](guildspecialskillright_bss.md) sets which member
grades may use eight of them, and the 44 skill numbers of
[guildhousecraftskill](guildhousecraftskill_dbss.md) are all rows here
(client 3474).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `guildskill.bss` | 3,084 | 766 Row | 4         |

| Layout | File             | Known            | Unknown    |
| ------ | ---------------- | ---------------- | ---------- |
| 1      | `guildskill.bss` | 3,084 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10 at `str_id1=skill_no`        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; not in skill number order            |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (4 bytes)

| Offset  | Type | Field       | Notes                                                                                     |
| ------- | ---- | ----------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | skill_level | Skill level of the skill key; `1` on every row (client 3474)                               |
| `+0x02` | u16  | skill_no    | Skill number; keys the LOC type 10 name; `skill_no << 16 \| skill_level` is the `skill_key` of a [skill](skill_dbss.md) record |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 has this
shape; the guild skills are rows of its skill sheets
(`DataSheet_SkillDataTable_Guild.xlsm`). The two u16 are the halves of a
little-endian `skill_key` (`skill_no << 16 | level`, as in
[fevertimeskill](fevertimeskill_bss.md)), and every `skill_no` names a
skill in LOC type 10 or, for 34 variants such as `기습적인 행동A`, only in
the Korean skill name of `skilltype.dbss` (client 3474).

## Notes

- Client 1784 and 2107 have 724 rows, 2519 736, 3002 738, 3251 750 and
  3474 766. Seven skill numbers of client 1784 are gone by client 3474.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`: the skill number first, then its name
  and the level.
