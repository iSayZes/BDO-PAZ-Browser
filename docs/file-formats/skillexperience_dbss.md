# `skillexperience.dbss` Format

## Purpose

EXP table of the combat skill points: the Skill EXP a character needs to go from one skill point level to the next, from level 0 to the max level in [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md). Companion `skillexperienceoffset.dbss` lists where every row sits. [guildskillexperience](guildskillexperience_dbss.md) (guild points) and [productexperience](productexperience_dbss.md) (life skill points) use the same container with other rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ------ | ---------------- | --------- |
| 1      | 1784 and later | 3474    | `skillexperience.dbss`       | 32,020 | 2,001 Level Row  | 16        |
| 1      | 1784 and later | 3474    | `skillexperienceoffset.dbss` | 20,014 | 2,001 Offset Row | 10        |

| Layout | File                         | Known             | Unknown         |
| ------ | ---------------------------- | ----------------- | --------------- |
| 1      | `skillexperience.dbss`       | 24,016 B (75.0%)  | 8,004 B (25.0%) |
| 1      | `skillexperienceoffset.dbss` | 20,014 B (100.0%) | 0 B (0.0%)      |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                         |
| ----------------------------- | -------- | ---------------------------------------------------------------------------- |
| `skillexperienceoffset.dbss`  | Required | `level -> (offset, size)` of every row                                       |
| `skillexperiencemaxlevel.bss` | Optional | Max level, see [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md)     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                 | Field     | Notes                                                |
| ------- | -------------------- | --------- | ---------------------------------------------------- |
| `+0x00` | u32                  | row_count | Number of rows; 2,001 (levels 0 to 2000) on client 3464 |
| `+0x04` | Level Row[row_count] | rows      | `row_count` rows of 16 bytes, not in level order     |

The rows fill the file exactly: 4 + 2,001 x 16 = 32,020 bytes on client 3464.

### Level Row (16 bytes)

| Offset  | Type | Field      | Notes                                                                |
| ------- | ---- | ---------- | -------------------------------------------------------------------- |
| `+0x00` | u32  | level      | Skill point level; equals the offset row's key                       |
| `+0x04` | u64  | exp        | EXP to go from `level` to `level + 1` (Notes)                        |
| `+0x0C` | u32  | unknown_0c | `0` on every row (client 3464)                                       |

### `skillexperienceoffset.dbss`

Index into `skillexperience.dbss`: the bare u16 offset table of `_common/pabr_offset.py` (`parse_bare_offset_rows`), with no `PABR` magic and no trailer.

| Offset  | Type                  | Field     | Notes                                         |
| ------- | --------------------- | --------- | --------------------------------------------- |
| `+0x00` | u32                   | row_count | Equals the `skillexperience.dbss` row count   |
| `+0x04` | Offset Row[row_count] | rows      | `row_count` rows of 10 bytes                  |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                             |
| ------- | ---- | ----------- | ----------------------------------------------------------------- |
| `+0x00` | u16  | level       | Level of the row it points at                                     |
| `+0x02` | u32  | data_offset | Absolute byte offset of the row's `level` in `skillexperience.dbss` |
| `+0x06` | u32  | data_size   | Always 16                                                         |

Neither file keeps level order: the offset rows start with levels 0, 399, 1052, and the first data row (`0x04`) is level 1052. The parser reads every row through the offset table, checks that the row's `level` matches the offset row's key, and returns the rows sorted by level.

## Notes

- The client has three skill point pools, numbered by `ToClient_getSkillPointInfo(type)`: `0` combat skill points (`panel_window_skillgroup_all_1.luac`), `2` life skill points (`panel_selfplayerexpgage.luac`) and `3` guild points (`panel_guildskill_all_1.luac`). `acquire.luac` names the matching level-up notices `GainCombatSkillPoint`, `GainProductSkillPoint` and `GainGuildSkillPoint`, shown with the `GAME` keys `ACQUIRE_OBJECTMESSAGE_2` ("Combat Skill Points Obtained"), `_1` ("Life Skill Points Obtained") and `_3` ("Guild Points Obtained"). The file stems follow the same names: `skillexperience`, `productexperience`, `guildskillexperience`.
- The skill window draws the bar as `getSkillPointExperience() / getSkillPointNeedExperience()`, and the guild window as `_currentExp / _nextLevelExp`, so the EXP restarts at 0 on every level, as in [lifeexp](lifeexp_dbss.md). The row direction (row N is the EXP from N to N + 1) follows `lifeexp.dbss`, where a packet capture confirmed it; a capture of the Skill EXP message against this table would flip it if the client divides by the level N + 1 row instead.
- Quest rewards of type `__eRewardSkillExp` give `_skillExperience` (`panel_dialog_quest_all_1.luac`), shown as "Skill EXP" (`LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP`).
- Curve on client 3464: level N needs 430 + 1,120 x N x (N + 1) EXP up to level 249 (69,720,430), then 557,760 more per level up to level 500 (209,718,190). Levels 501 to 1501 hold that same 209,718,190, and levels 1502 to 2000 ten times it, 2,097,181,900.
- Unlike `lifeexp.dbss` the file has no blocks and the rows open with a u32 level instead of a type byte; the offset table is the bare 10-byte layout that `petexpoffset.dbss` also uses.

## Open Questions

### unknown_0c

The trailing u32 is `0` on all 2,001 rows of client 3464. The 13-byte rows of `guildskillexperience.dbss` end in a u8 `1` at the same offset instead, so the two tables do not share a reading for it, and the skill window Lua reads only the current and needed EXP.
