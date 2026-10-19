# `nodeexperience.bss` Format

## Purpose

EXP table of the node levels: the EXP a node needs to go from one node level to the next. Players raise a node's level on the world map by investing Energy ("Energy can be consumed to increase a Node's level."). One 15-byte row per level, levels 0 to 20 on client 3464.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------------ | --------- |
| 1      | 1784 and later | 3474    | `nodeexperience.bss` | 335   | 21 Level Row | 15        |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 1      | `nodeexperience.bss` | 335 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

`PABR` magic, a u32 row count, the rows, then the 12-byte PABR trailer. 335 bytes on client 3464 (21 rows).

| Offset     | Type                 | Field        | Notes                                  |
| ---------- | -------------------- | ------------ | -------------------------------------- |
| `+0x00`    | char[4]              | magic        | `PABR` (ASCII)                         |
| `+0x04`    | u32                  | row_count    | 21 on client 3464                      |
| `+0x08`    | Level Row[row_count] | rows         | `row_count` rows of 15 bytes, level 0 first |
| `EOF-0x0C` | u32                  | string_count | `0`: the empty PABR string table       |
| `EOF-0x08` | u32                  | end_of_data  | Byte offset right after the last row (`0x143` on client 3464) |
| `EOF-0x04` | u32                  | zero         | `0`                                    |

The parser checks that `8 + row_count x 15` equals `end_of_data` and that the trailer closes the file.

### Level Row (15 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u8   | is_integrity  | `0` on the level 0 row, `1` on every other row; see Field Names |
| `+0x01` | u32  | node_exp_type | `0` on every row (client 3474); see Field Names              |
| `+0x05` | i16  | level         | Node level; equals the row index                             |
| `+0x07` | i64  | exp           | EXP to go from `level` to `level + 1` (Notes)                |

## Field Names

The 2016 client with debug symbols holds the row as
`gc::NodeExperienceStaticStatus` (24 bytes): bool `_isIntegrity` at `+0`,
int `_nodeExpType` at `+4`, short `_nodeLevel` at `+8` and `__int64`
`_requiredExperience` at `+0x10`. The file stores the four members in that
order without the padding. A private server on client 1784 loads the same
struct from its `NodeEXP_Table` sheet (loader at VA `0x1408c20e0`): `Level`
into `_nodeLevel`, `RequireEXP` into `_requiredExperience` and `Type` into
`_nodeExpType` (setter VA `0x140bb0a7d`); the register step indexes the
manager's per-type lists by `_nodeExpType`. Its own `nodeexperience.bss`
matches the sheet on all 11 rows.

`_isIntegrity` has no sheet column. The setter writes `0`, and the
integrity pass (VA `0x140bb1050`) sets it to `1` on every row after the
first while it checks that the needed EXP never falls ("required EXP cannot
be smaller than the previous level's"). That is the `0` on level 0 and `1`
on every other row of both clients. The loader also rejects a row with a
needed EXP below 1, which is why level 0 holds `1`.

## Notes

- The world map node menu (`grand_worldmap_nodemenu.luac`, decompiled with unluac) draws the node level bar as `ToClient_GetNodeExperience_s64(nodeKey) / ToClient_GetNeedExperienceToNextNodeLevel_s64(nodeKey)` and shows `Lv. <level>/<ToClient_GetNodeMaxLevel()>`, so the EXP restarts at 0 on every level, as in [skillexperience](skillexperience_dbss.md). Both getters return s64, which matches the i64 `exp`.
- The row direction (row N is the EXP from N to N + 1) follows `skillexperience.dbss` and `lifeexp.dbss`. The values are not cumulative totals: levels 19 and 20 both hold 200,000, which as totals would make level 20 free.
- `panel_personalicon_left_remaster.luac` counts a node as invested only when `0 < ToClient_GetNodeLevel(wayPointKey)`, so level 0 is a node with no investment. The level 0 row needs 1 EXP and is the only row with `is_integrity` `0`. The node menu never shows level 0 in game; a node shows level 1 as its lowest level.
- The node menu invests Energy in steps of 10: `InvestNodeLevelExecute` multiplies the number pad value by 10 and sends it with `ToClient_RequestIncreaseExperienceNodeByCharacterIndex`; the number pad max is `floor(character Energy / 10)`. The server turns Energy into node EXP; no client Lua or data file holds the rate. The client 1784 server dump sets `100` in the `gc::NodeExperienceStaticStatusManager` constructor (VA `0x1401c032b`), in the member the 2016 PDB names `const __int64 _increasePerWP`.
- 1 Energy = 100 node EXP, so a level needs `exp / 100` Energy. Checked in game on three levels: level 1 to 2 took 100 Energy (10,000 EXP), level 2 to 3 took 200 (20,000) and level 3 to 4 took 400 (40,000). Level 1 to 20 is 2,070,000 EXP, or 20,700 Energy.
- Curve on client 3464: level 0 needs 1, level 1 needs 10,000 and level 2 needs 20,000; from level 3 each level needs 40,000 + 10,000 x (N - 3), up to 200,000 at level 19. Level 20, the last row, holds 200,000 again.
- The node menu shows `Lv. N/20` in game, so `ToClient_GetNodeMaxLevel()` returns 20 and the level 20 row is the cap; its 200,000 is never needed.
- The trailer is the one of [skillexperiencemaxlevel](skillexperiencemaxlevel_bss.md) and [fitnessmaxlevel](fitnessmaxlevel_bss.md).
