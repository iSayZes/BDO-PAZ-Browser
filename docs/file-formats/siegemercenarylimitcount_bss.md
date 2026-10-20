# `siegemercenarylimitcount.bss` Format

## Purpose

How many War Heroes (hired guild mercenaries, `전장의 영웅`) a guild can
bring into a Node War or Conquest War, one u32 per siege stage. The seven
values sit in the slot where a PABR table keeps its record count, followed
by an empty string table. On client 3474 they are `0, 0, 0, 3, 3, 3, 5`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `siegemercenarylimitcount.bss` | 44    | 1 String Table | 4         |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `siegemercenarylimitcount.bss` | 44 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field         | Notes                                                      |
| ------------------- | ------------ | ------------- | ---------------------------------------------------------- |
| `+0x00`             | char[4]      | magic         | ASCII `PABR`                                               |
| `+0x04`             | u32          | siege_stage_0 | War Hero limit of stage 0; see Siege Stages                |
| `+0x08`             | u32          | siege_stage_1 | War Hero limit of stage 1                                  |
| `+0x0C`             | u32          | siege_stage_2 | War Hero limit of stage 2                                  |
| `+0x10`             | u32          | siege_stage_3 | War Hero limit of stage 3                                  |
| `+0x14`             | u32          | siege_stage_4 | War Hero limit of stage 4                                  |
| `+0x18`             | u32          | siege_stage_5 | War Hero limit of stage 5                                  |
| `+0x1C`             | u32          | siege_stage_6 | War Hero limit of stage 6                                  |
| `+0x20`             | String Table | string_table  | See String Table                                           |
| `string_table+0x00` | u32          | table_start   | Offset of the string table; `0x20` on every client checked |
| `string_table+0x04` | u32          | zero          | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Siege Stages

The stage of each field comes from the developer comments on the
`SiegeStage_0` to `SiegeStage_6` columns of the `SiegeMercenaryLimitCount`
sheet in a private server's `datasheet_siegedatatable.xlsm` on client 1784.
Each comment reads "the number of War Heroes (mercenaries) that can take
part, per Node War stage and in the Conquest War; a guild can hire more,
but no more than this number can join the war". The client's English word
for `단계` is "Tier" (`LUA_NODEGRADE_1`, `2단계`, is "Tier 2"). The preview
labels its columns with these client 1784 stages.

| Field           | Stage on client 1784 (comment)  | Client 1784 to 2519 | Clients 3002 to 3474 |
| --------------- | ------------------------------- | ------------------- | -------------------- |
| `siege_stage_0` | Node War Tier 1 Beginner (`거점전 1단계 초급`) | `0` | `0` |
| `siege_stage_1` | Node War Tier 1 Intermediate (`거점전 1단계 중급`) | `0` | `0` |
| `siege_stage_2` | Node War Tier 1 Advanced (`거점전 1단계 상급`) | `0` | `0` |
| `siege_stage_3` | Node War Tier 2 (`거점전 2단계`) | `3` | `3` |
| `siege_stage_4` | Node War Tier 3 (`거점전 3단계`) | `4` | `3` |
| `siege_stage_5` | Node War Tier 4 (`거점전 4단계`) | `5` | `3` |
| `siege_stage_6` | Conquest War (`점령전`)         | `5` | `5` |

## Field Names

The field names are the `SiegeStage_0` to `SiegeStage_6` columns of the
`SiegeMercenaryLimitCount` sheet in a private server's `DataSheets.bexcel`
on client 1784. The sheet has one row per `PA_GAME_SERVICE_TYPE`; every row
with values (JPN, RUS, NA, TW, SA, TH, ID, TR, GT and CS) holds
`<null>, <null>, <null>, 3, 4, 5, 5`, and a `<null>` compiles to `0`. All 7
of 7 columns match the client 1784 file by value, and that client's file is
byte for byte the private server's compiled `binary/siegemercenarylimitcount.bss`.
The server dump on client 1784 has the sheet name `SiegeMercenaryLimitCount`
and the column format `SiegeStage_%d` as UTF-16 strings.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 03 00 00 00 03 00 00 00 05 00 00 00 00 00 00 00 20 00 00 00 00 00 00 00`
  (44 bytes).
- Clients 1784, 2107 and 2519 hold `0, 0, 0, 3, 4, 5, 5`; clients 3002, 3251
  and 3474 hold `0, 0, 0, 3, 3, 3, 5`. The file is not in the archives of
  clients 794, 1230 and 1485.
- The node tooltip on client 3474 (`panel_worldmap_nodetooltip_villagewar_all_1.luac`,
  `new_worldmap_actortooltip.luac`) shows "Max War Heroes: {count}"
  (`LUA_WORLDMAP_ACTORTOOLTIP_GUILDMAXMECENARY`) from
  `siegeTerritoryOptionWrapper._limitVolunteerCount` or
  `regionWrapper:getSiegeGuildVolunteerLimitCount()`. The second is a per
  region value: `SiegeGuildVolunteerLimitCount` is a column of the
  `SiegeOptionByRegion` and `SiegeOptionRegion` sheets on client 1784, not
  of this file.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`.

## Open Questions

### Stages on the Live Client

The stage of each field comes from the client 1784 sheet comments. The
client 3474 string table has Node War tiers `LUA_NODEGRADE_0` to
`LUA_NODEGRADE_4` ("Tier 1" to "Tier 5") and Conquest tiers
`LUA_NODEGRADE2_1` to `LUA_NODEGRADE2_3`, and no client Lua function on
client 3474 has `SiegeStage` or `MercenaryLimit` in its name. Whether `siege_stage_0` to `siege_stage_6`
still stand for the same seven stages on client 3474 is unknown.
