# `productexperience.dbss` Format

## Purpose

Level table of the life skill points (skill point pool `2`, the client's "product" skill points): one row per level from 0 to 2000. On client 3464 every row holds only its level, a u16 `0` and a u8 `1`; no row stores an EXP value, and the client's life skill point gauge is never updated (Notes). Companion `productexperienceoffset.dbss` lists where every row sits. The container and offset table are the ones of [skillexperience](skillexperience_dbss.md); only the row differs. No `productexperiencemaxlevel.bss` exists.

Example (client 3464):

```text
Lv 0     unknown_04 0   unknown_06 1
Lv 2000  unknown_04 0   unknown_06 1
```

## Companion Files

| File                            | Required | Role                                   |
| ------------------------------- | -------- | -------------------------------------- |
| `productexperienceoffset.dbss`  | Required | `level -> (offset, size)` of every row |

All multi-byte values are little-endian.

## File Layout

| Offset  | Type  | Field     | Notes                                                   |
| ------- | ----- | --------- | ------------------------------------------------------- |
| `+0x00` | u32   | row_count | Number of rows; 2,001 (levels 0 to 2000) on client 3464 |
| `+0x04` | row[] | rows      | `row_count` rows of 7 bytes, not in level order         |

The rows fill the file exactly: 4 + 2,001 x 7 = 14,011 bytes on client 3464.

## Record Structure

### Level Row (7 bytes)

| Offset  | Type | Field      | Notes                                              |
| ------- | ---- | ---------- | -------------------------------------------------- |
| `+0x00` | u32  | level      | Life skill point level; equals the offset row's key |
| `+0x04` | u16  | unknown_04 | `0` on every row (client 3464)                     |
| `+0x06` | u8   | unknown_06 | `1` on every row (client 3464)                     |

## productexperienceoffset.dbss

Same layout as `skillexperienceoffset.dbss` (see [skillexperience](skillexperience_dbss.md)): a u32 row count equal to the main file's, then 10-byte [u16 level][u32 data_offset][u32 data_size] rows with no magic and no trailer. `data_size` is always 7, and `data_offset` points at the row's `level`. The rows are not in level order (399, 1052, 0, ...); the parser returns the main rows sorted by level.

## Suggested UI Layout

### productexperience.dbss

| Column | Type | Notes   |
| ------ | ---- | ------- |
| Level  | num  | `level` |

`unknown_04` and `unknown_06` stay on the record for search and CSV export.

### productexperienceoffset.dbss

| Column      | Type | Notes                 |
| ----------- | ---- | --------------------- |
| Level       | num  | `level`               |
| Data Offset | num  | `data_offset`, as hex |
| Data Size   | num  | `data_size`           |

## Notes

- "Product" is the client's word for the life skill point pool. `panel_selfplayerexpgage.luac` defines `Panel_User_ProductSkillPoint_Update`, which reads `ToClient_getSkillPointInfo(2)` into the `StaticText_SkillPoint_p` / `CircularProgress_SkillExp_p` gauge, and `acquire.luac` announces a new point as `GainProductSkillPoint` with `ACQUIRE_OBJECTMESSAGE_1` ("Life Skill Points Obtained"). No client Lua script calls `Panel_User_ProductSkillPoint_Update` or registers it for an event on client 3464.
- Quest rewards of type `__eRewardLifeExp` give `_productExperience` / `getProductExperience()` (`panel_dialog_quest_all_1.luac`, `panel_window_questinfo_all_1.luac`), shown as "Production EXP" (`LUA_QUESTREWARD_SIMPLE_TOOLTIP_PRODUCTEXP`). Whether that reward feeds this pool or the per-skill tables in [lifeexp](lifeexp_dbss.md) is not visible in the Lua.
- See the [skillexperience](skillexperience_dbss.md) Notes for the three skill point pools.

## Open Questions

### Where Is the EXP Field

The combat skill point and guild point rows hold a u64 EXP at `+0x04`; this row holds a u16 there, `0` on every level, then a u8 `1` like the last byte of the `guildskillexperience.dbss` row. Whether `unknown_04` is a narrowed EXP field of an unused pool or something else cannot be told from all-zero data. A client where the values change would answer it.
