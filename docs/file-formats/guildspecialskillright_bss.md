# `guildspecialskillright.bss` Format

## Purpose

Which guild member grades may use each special guild skill: one row per
guild skill number with one flag per member grade, the flags of
[guildright](guildright_bss.md). On client 3474 the file has 8 rows:
Command to Gather, Battle Command to Gather, Breath of Life, Blessing of
Battle and the four skills Admiral's Rally, BreezyVoyage, Seaforge
Blessing and Seawatch Pulse, each with grades `0`, `6`, `8` and `9` set.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `guildspecialskillright.bss` | 156   | 8 Row   | 17        |

| Layout | File                         | Known          | Unknown    |
| ------ | ---------------------------- | -------------- | ---------- |
| 1      | `guildspecialskillright.bss` | 156 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                       |
| --------------------- | -------- | -------------------------- |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10   |

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

### Row (variable: 6 bytes + flags)

| Offset  | Type            | Field          | Notes                                                                                  |
| ------- | --------------- | -------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u16             | guild_skill_no | Skill number of a [guildskill](guildskill_bss.md) row; the handler shows its LOC type 10 name |
| `+0x02` | u32             | grade_count    | Number of flags, one per member grade; `11` on client 3474, `8` on 1784                |
| `+0x06` | u8[grade_count] | grade          | `1` when member grade `N` (the flag's position) may use the skill; see [guildright](guildright_bss.md#grades) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names follow the `GuildSpecialSkillRight_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784: `GuildSkillNo` and `Grade`, the
grade numbers whose flag is set (4 of 4 rows match the client 1784 file).
The sheet's third column, `ContentsGroupKey` (`1503` and `1648`), is not in
the file. Every skill number is a guild skill: all 8 are rows of
[guildskill](guildskill_bss.md) on client 3474.

## Notes

- Client 1784 has the first four skills with grades `0` and `6` (8 flags).
  Client 3002 sets `0`, `6`, `8` and `9` of 11 flags on the same four, and
  client 3251 adds the other four (62845 to 62848).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`: the skill, its name and the set
  grade numbers.
