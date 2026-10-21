# `skillexperience.dbss` Format

## Purpose

EXP table of the combat skill points: the Skill EXP a character needs to go from one skill point level to the next, from level 0 to the max level in [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md). Companion `skillexperienceoffset.dbss` lists where every row sits. [guildskillexperience](guildskillexperience_dbss.md) (guild points) and [productexperience](productexperience_dbss.md) (life skill points) use the same container with other rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ------ | ---------------- | --------- |
| 1      | 1485 and later | 3474    | `skillexperience.dbss`       | 32,020 | 2,001 Level Row  | 16        |
| 1      | 1485 and later | 3474    | `skillexperienceoffset.dbss` | 20,014 | 2,001 Offset Row | 10        |

| Layout | File                         | Known             | Unknown    |
| ------ | ---------------------------- | ----------------- | ---------- |
| 1      | `skillexperience.dbss`       | 32,020 B (100.0%) | 0 B (0.0%) |
| 1      | `skillexperienceoffset.dbss` | 20,014 B (100.0%) | 0 B (0.0%) |

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

| Offset  | Type | Field                   | Notes                                                    |
| ------- | ---- | ----------------------- | -------------------------------------------------------- |
| `+0x00` | u16  | level                   | Skill point level; equals the offset row's key           |
| `+0x02` | u16  | acquired_point          | `0` on every row (client 3474)                           |
| `+0x04` | u32  | exp                     | EXP to go from `level` to `level + 1` (Notes)            |
| `+0x08` | u32  | require_exp_limit       | `0` on every row (client 3474)                           |
| `+0x0C` | u32  | quest_require_exp_limit | `0` on every row (client 3474)                           |

The server rejects a row whose `exp`, `require_exp_limit` or `quest_require_exp_limit` is below 0 (Field Names), so the three fit an i32.

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

## Field Names

The names come from the server dump of a private server on client 1784 (`Instance_dumpFull.exe`). It loads the row twice into one static status: from the client's `skillexperience.dbss` (row reader at VA `0x140c84990`) and from the `SkillPointEXP_Table_New` developer sheet (column reads at VA `0x1408c2c87` to `0x1408c2d39`). Both write the same members:

| Field                     | Member  | Read from the file | Sheet column           |
| ------------------------- | ------- | ------------------ | ---------------------- |
| `level`                   | `+0x00` | u16                | `Index`                |
| `acquired_point`          | `+0x02` | u16                | `AquiredPoint`         |
| `exp`                     | `+0x04` | u32                | `RequireEXP`           |
| `require_exp_limit`       | `+0x08` | u32                | `RequireSkillExpLimit` |
| `quest_require_exp_limit` | `+0x0C` | u32                | `QuestRequireExpLimit` |

The row check (from VA `0x140c84702`) stores the key, then tests the three EXP members in member order and logs, for the first one below 0, "skill point level key(%#): (%#) EXP is not defined", "... the current level's max (%#) EXP is not defined" or "... the current level's quest max (%#) EXP is not defined". Only a row that passes gets a flag at member `+0x10`, which the file does not store. [guildskillexperience](guildskillexperience_dbss.md) and [productexperience](productexperience_dbss.md) store that flag as their last byte (`is_exp_defined`).

The sheet and the private server's own `skillexperience.dbss` hold the same 2,001 rows as client 3474: `exp` matches on every level, and `AquiredPoint`, `RequireSkillExpLimit` and `QuestRequireExpLimit` are `0` on every row of all three. Earlier versions of this doc read `+0x00` as a u32 level and `+0x04` as a u64 EXP; with those zero fields the values are the same, so only the field bounds changed.

## Notes

- The client has three skill point pools, numbered by `ToClient_getSkillPointInfo(type)`: `0` combat skill points (`panel_window_skillgroup_all_1.luac`), `2` life skill points (`panel_selfplayerexpgage.luac`) and `3` guild points (`panel_guildskill_all_1.luac`). `acquire.luac` names the matching level-up notices `GainCombatSkillPoint`, `GainProductSkillPoint` and `GainGuildSkillPoint`, shown with the `GAME` keys `ACQUIRE_OBJECTMESSAGE_2` ("Combat Skill Points Obtained"), `_1` ("Life Skill Points Obtained") and `_3` ("Guild Points Obtained"). The file stems follow the same names: `skillexperience`, `productexperience`, `guildskillexperience`.
- The skill window draws the bar as `getSkillPointExperience() / getSkillPointNeedExperience()`, and the guild window as `_currentExp / _nextLevelExp`, so the EXP restarts at 0 on every level, as in [lifeexp](lifeexp_dbss.md). The row direction (row N is the EXP from N to N + 1) follows `lifeexp.dbss`, where a packet capture confirmed it; a capture of the Skill EXP message against this table would flip it if the client divides by the level N + 1 row instead.
- Quest rewards of type `__eRewardSkillExp` give `_skillExperience` (`panel_dialog_quest_all_1.luac`), shown as "Skill EXP" (`LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP`).
- Curve on client 3464: level N needs 430 + 1,120 x N x (N + 1) EXP up to level 249 (69,720,430), then 557,760 more per level up to level 500 (209,718,190). Levels 501 to 1501 hold that same 209,718,190, and levels 1502 to 2000 ten times it, 2,097,181,900.
- Unlike `lifeexp.dbss` the file has no blocks and the rows open with a u16 level instead of a type byte; the offset table is the bare 10-byte layout that `petexpoffset.dbss` also uses.

## Open Questions

### What the Two EXP Limits Cap

`require_exp_limit` and `quest_require_exp_limit` are `0` on every row of client 3474 and of the 1784 sheet, and the skill window Lua reads only the current and needed EXP (`getSkillPointExperience()`, `getSkillPointNeedExperience()`). The Korean check messages call them the current level's max EXP and quest max EXP; what a non-zero value would cap needs a client where one is set.
