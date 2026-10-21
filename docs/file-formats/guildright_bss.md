# `guildright.bss` Format

## Purpose

Which guild member grades hold each guild right: one row per right index
with one flag per member grade. On client 3474 the file has 55 rows,
indexes `0` to `54`, and 11 flags per row. The client Lua checks a right
with `ToClient_IsCheckGuildRightType(eRightType)` for the
`__eGuildRightType_*` rights once `_ContentsGroup_GuildRightInfo` is on.
[guildspecialskillright](guildspecialskillright_bss.md) holds the same
flags per guild skill, and
[guildrightnewstaticstatus](guildrightnewstaticstatus_bss.md) the
newer rights of the guild authority window.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `guildright.bss` | 900   | 55 Row  | 16        |

| Layout | File             | Known          | Unknown    |
| ------ | ---------------- | -------------- | ---------- |
| 1      | `guildright.bss` | 900 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

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

### Row (variable: 5 bytes + flags)

| Offset  | Type              | Field       | Notes                                                                    |
| ------- | ----------------- | ----------- | ------------------------------------------------------------------------ |
| `+0x00` | u8                | index       | Right index, row key                                                     |
| `+0x01` | u32               | grade_count | Number of flags, one per member grade; `11` on client 3474, `8` on 1784  |
| `+0x05` | u8[grade_count]   | grade       | `1` when member grade `N` (the flag's position) holds the right; see Grades |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Grades

A flag's position is the member grade number. The 2016 `gc::GuildMemberGrade`
has three: `0` `eGuildMemberGradeMaster`, `1` `eGuildMemberGradeSubMaster`
and `2` `eGuildMemberGradeNormal`. The client Lua of client 3474 names 11
grades without their values: `__eGuildMemberGradeMaster`, `SubMaster`,
`Normal`, `Junior`, `SupplyOfficer`, `Adviser`, `Scribe`, `Gunner`,
`ChiefOfStaff`, `MissionOfficer` and `Volunteer`, the same number as the
flags. The flag count grew from 8 (clients 1784 and 2107) to 11 (client
2519 and later). The handler shows the numbers of the set flags
(`0, 1, 6, 8, 9`).

On client 3474, `0` is set on 52 of the 55 rows, which fits `0` as the
master. The other three are index `30` (`2, 5, 10`), `35` (`1, 6, 8, 9`)
and `49` (`2, 3, 7, 10`).

## Field Names

`index` and `grade` follow the `GuildRight_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784: its `Index` column is the row
key and its `Grade` column lists the grade numbers whose flag is set (50 of
50 rows match the client 1784 file). The sheet's third column,
`ContentsGroupKey` (`1503` on every row), is not in the file.

## Notes

- Client 1784 has 50 rows of 8 flags (670 bytes), client 2107 52 rows of
  8, clients 2519 to 3474 55 rows of 11 (900 bytes).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`.

## Open Questions

### Right Index Names

The Lua names 34 `__eGuildRightType_*` rights (`SetGuildMark`,
`GuildDestroy`, `Notice`, `QuestAccept`, ...) without their values, so
`index` cannot be tied to a name. The 1784 sheet has no name column.

### Grade Numbers Above 2

Which `__eGuildMemberGrade*` name each grade number from `3` to `10` has.
Grade `6` is set together with grade `0` on 45 of the 55 rows (client
3474), and every [guildspecialskillright](guildspecialskillright_bss.md) row sets
`0`, `6`, `8` and `9`.
