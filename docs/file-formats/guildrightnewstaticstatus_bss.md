# `guildrightnewstaticstatus.bss` Format

## Purpose

The rights of the guild authority window, in groups: per group its number
and Korean name, then each right with its number, Korean name and Korean
description, all three texts in the PABR string table. On client 3474 the
file has 4 groups (관리 management, 활동 activities, 전투 combat, 재정
finance) with 39 rights, numbers `1` to `41` without `9` and `20`. The
right numbers are the `__eGuildRightNew_*` values the Lua checks; right
`29` (길드 리그 신청) signs a guild up for the Guild League of
[guildmatchoption](guildmatchoption_bss.md), and right `14` (길드 하우스
제작) is guild house crafting, the skills of
[guildhousecraftskill](guildhousecraftskill_dbss.md). The older rights
per member grade are in [guildright](guildright_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | ----------------- | --------- |
| 1      | 3002 and later | 3474    | `guildrightnewstaticstatus.bss` | 4,880 | 39 Right, 4 Group | 12        |

| Layout | File                            | Known           | Unknown    |
| ------ | ------------------------------- | --------------- | ---------- |
| 1      | `guildrightnewstaticstatus.bss` | 4,876 B (99.9%) | 4 B (0.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type               | Field        | Notes                                           |
| ------------------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                    |
| `+0x04`             | u32                | group_count  | Number of groups                                |
| `+0x08`             | Group[group_count] | groups       | See Group; byte-packed                          |
| `groups+0x00`       | String Table       | string_table | See String Table                                |
| `string_table+0x00` | u32                | table_start  | Offset of the string table, where `groups` ends |
| `string_table+0x04` | u32                | zero         | Always `0`                                      |

### Group (variable: 10 bytes + rights)

| Offset  | Type               | Field          | Notes                                                        |
| ------- | ------------------ | -------------- | ------------------------------------------------------------ |
| `+0x00` | u8                 | group_no       | Group number, `1` to `group_count` in file order; `getGroupNo()` |
| `+0x01` | u8                 | unknown_01     | Equal to `group_no` on every group (clients 3002 to 3474)     |
| `+0x02` | u32                | group_name_ref | String-table index of the Korean group name; `getGroupName()` |
| `+0x06` | u32                | right_count    | Number of rights; `getRightCount()`                          |
| `+0x0A` | Right[right_count] | rights         | See Right                                                    |

### Right (12 bytes)

| Offset  | Type | Field           | Notes                                                              |
| ------- | ---- | --------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | right_no        | `__eGuildRightNew_*` value; `getRightNo()`; unique over the file    |
| `+0x04` | u32  | name_ref        | String-table index of the Korean right name; `getRightName()`      |
| `+0x08` | u32  | description_ref | String-table index of the Korean description; `getRightDesc()`     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                    |
| ------- | ------------------ | ------------ | ------------------------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings, one per group name and two per right; 82 on client 3474 |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE Korean text in file order: each group's name, then each right's name and description |

## Field Names

The guild authority window of client 3474
(`panel_guild_authorization_all_1.luac`) walks the file with
`ToClient_getGuildRightGroupCount()` and
`ToClient_GetGuildRightNewStaticStatus(ii)`, then reads `getGroupNo()`,
`getGroupName()` and `getRightCount()` per group and `getRightNo()`,
`getRightName()` and `getRightDesc()` per right; the fields take those
names. The rights it checks by name are `__eGuildRightNew_*` (29 names in
the Lua, such as `__eGuildRightNew_ChangeMemberRight`), compared with
`getRightNo()`. The Guild Authority window is newer than client 1784 and
2519, which do not ship the file, so no sheet of a private server's
`DataSheets.bexcel` covers it.

## Notes

- Clients 3002 and 3251 have 38 rights: right `20` (길드 보호 인원 설정,
  the guild's protected members) sits in group 3, and rights `40` (길드
  전략 가이드) and `41` (길드 명성 소모) are not there yet. Client 3474
  drops `20` and adds the other two.
- No LOC type holds the right names in English, so the handler shows the
  Korean text.
- The handler (`_bss/guildrightnewstaticstatus/`) shows one row per right,
  sorted by right number, with its group number and name and its
  description.

## Open Questions

### Right Number Names

The Lua names 29 `__eGuildRightNew_*` rights without their values, and the
file's Korean names fit many of them (`1` 가입/재계약 and `Join`, `36` 추방
and `Expel`), but no source ties a value to a name.

### Localised Texts

Whether an English client shows these Korean texts or other text; the
English LOC has no row with the right names, and the window fills its
list only when `_ContentsGroup_GuildAuthoritySeparation` is on
(`setData()`).
