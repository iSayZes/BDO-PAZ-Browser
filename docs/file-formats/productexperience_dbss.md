# `productexperience.dbss` Format

## Purpose

Level table of the life skill points (skill point pool `2`, the client's "product" skill points): one row per level from 0 to 2000. On client 3474 every row holds its level, an `exp` of `0` and the flag `1`, and the client's life skill point gauge is never updated (Notes). Companion `productexperienceoffset.dbss` lists where every row sits. The container and offset table are the ones of [skillexperience](skillexperience_dbss.md); only the row differs. No `productexperiencemaxlevel.bss` exists.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ------ | ---------------- | --------- |
| 1      | 1784 and later | 3474    | `productexperience.dbss`       | 14,011 | 2,001 Level Row  | 7         |
| 1      | 1784 and later | 3474    | `productexperienceoffset.dbss` | 20,014 | 2,001 Offset Row | 10        |

| Layout | File                           | Known             | Unknown    |
| ------ | ------------------------------ | ----------------- | ---------- |
| 1      | `productexperience.dbss`       | 14,011 B (100.0%) | 0 B (0.0%) |
| 1      | `productexperienceoffset.dbss` | 20,014 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                   |
| ------------------------------- | -------- | -------------------------------------- |
| `productexperienceoffset.dbss`  | Required | `level -> (offset, size)` of every row |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                 | Field     | Notes                                                   |
| ------- | -------------------- | --------- | ------------------------------------------------------- |
| `+0x00` | u32                  | row_count | Number of rows; 2,001 (levels 0 to 2000) on client 3464 |
| `+0x04` | Level Row[row_count] | rows      | `row_count` rows of 7 bytes, not in level order         |

The rows fill the file exactly: 4 + 2,001 x 7 = 14,011 bytes on client 3464.

### Level Row (7 bytes)

| Offset  | Type | Field          | Notes                                               |
| ------- | ---- | -------------- | --------------------------------------------------- |
| `+0x00` | u16  | level          | Life skill point level; equals the offset row's key |
| `+0x02` | u32  | exp            | `0` on every row (client 3474)                      |
| `+0x06` | u8   | is_exp_defined | `1` on every row (client 3474); see Field Names     |

### `productexperienceoffset.dbss`

The layout of `skillexperienceoffset.dbss` (see [skillexperience](skillexperience_dbss.md)): a u32 row count equal to the main file's, then 10-byte [u16 level][u32 data_offset][u32 data_size] rows with no magic and no trailer. `data_size` is always 7, and `data_offset` points at the row's `level`. The rows are not in level order (399, 1052, 0, ...); the parser returns the main rows sorted by level.

| Offset  | Type                  | Field     | Notes                                         |
| ------- | --------------------- | --------- | --------------------------------------------- |
| `+0x00` | u32                   | row_count | Equals the `productexperience.dbss` row count |
| `+0x04` | Offset Row[row_count] | rows      | `row_count` rows of 10 bytes                  |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                 |
| ------- | ---- | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | level       | Level of the row it points at                                         |
| `+0x02` | u32  | data_offset | Absolute byte offset of the row's `level` in `productexperience.dbss` |
| `+0x06` | u32  | data_size   | Always 7                                                              |

## Field Names

The row is the `ProductExp_Table` sheet of a private server on client 1784, read the way its server dump (`Instance_dumpFull.exe`) reads it. The dump fills one static status from the client's `productexperience.dbss` (row reader at VA `0x140bf39a0`) and from the sheet (column reads at VA `0x1408dbeaf` to `0x1408dbf10`):

| Field            | Member  | Read from the file | Sheet column        |
| ---------------- | ------- | ------------------ | ------------------- |
| `level`          | `+0x00` | u16                | `Index`             |
| `exp`            | `+0x04` | u32                | `ProductRequireEXP` |
| `is_exp_defined` | `+0x08` | u8                 | none                |

The sheet loader writes `1` to `is_exp_defined` for every row it loads and logs "skill point key(%#): EXP is not defined" for a row it rejects, the same flag [guildskillexperience](guildskillexperience_dbss.md) stores. `ProductRequireEXP` is `0` on all 2,001 sheet rows, as `exp` is on client 3474, and the sheet's note calls it "the EXP a production skill needs". So the row does have an EXP field, empty on every level. Earlier versions of this doc read the row as a u32 level, a u16 `unknown_04` and a u8 `unknown_06`; with the zero bytes the values are the same.

## Notes

- "Product" is the client's word for the life skill point pool. `panel_selfplayerexpgage.luac` defines `Panel_User_ProductSkillPoint_Update`, which reads `ToClient_getSkillPointInfo(2)` into the `StaticText_SkillPoint_p` / `CircularProgress_SkillExp_p` gauge, and `acquire.luac` announces a new point as `GainProductSkillPoint` with `ACQUIRE_OBJECTMESSAGE_1` ("Life Skill Points Obtained"). No client Lua script calls `Panel_User_ProductSkillPoint_Update` or registers it for an event on client 3464.
- Quest rewards of type `__eRewardLifeExp` give `_productExperience` / `getProductExperience()` (`panel_dialog_quest_all_1.luac`, `panel_window_questinfo_all_1.luac`), shown as "Production EXP" (`LUA_QUESTREWARD_SIMPLE_TOOLTIP_PRODUCTEXP`). Whether that reward feeds this pool or the per-skill tables in [lifeexp](lifeexp_dbss.md) is not visible in the Lua.
- See the [skillexperience](skillexperience_dbss.md) Notes for the three skill point pools.
