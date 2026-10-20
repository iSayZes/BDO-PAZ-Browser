# `buildingbuff.dbss` Format

## Purpose

The villa buffs a player buys with silver in the villa buff window
(`Panel_Window_BuildingBuff_All`, `panel_window_camp_villabuff_all_1.luac`).
Each row is one skill, `[Villa] Turning Gates (60 min)` for example, and its
silver cost. The rows sit in four lists; list `i` holds the rows whose
`Count_Villa` is `i + 1`, and only the first list has rows. Companion
`buildingbuffoffset.dbss` lists where every row sits.

On client 3474 the 10 rows are two buffs at five durations each:

| Skill                      | 60 min    | 90 min    | 120 min   | 180 min   | 300 min    |
| -------------------------- | --------- | --------- | --------- | --------- | ---------- |
| `[Villa] Turning Gates`    | 200,000   | 300,000   | 450,000   | 900,000   | 2,000,000  |
| `[Villa] Body Enhancement` | 1,000,000 | 1,500,000 | 2,250,000 | 4,500,000 | 10,000,000 |

Skill numbers in the same order: Turning Gates `55744`, `53657`, `55747`,
`53660`, `52906`; Body Enhancement `55746`, `53659`, `55749`, `53662`,
`52908`. LOC type 10 gives Turning Gates "Energy Recovery +1, Amity +10%,
Life EXP +10%" and Body Enhancement "All AP +10, All Damage Reduction +10,
Max HP +200, ...". Client 1784 has 12 rows: the 60 to 180 minute rows of both buffs
and a third buff, `[Villa] Skill and Experience` (`55745`, `53658`,
`55748`, `53661`), which client 3474 names "- Not in Use" and no longer
lists.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ---------------------------- | --------- |
| 1      | 1784 and later | 3474    | `buildingbuff.dbss`       | 140   | 10 Row, 4 Villa List         | 12        |
| 1      | 1784 and later | 3474    | `buildingbuffoffset.dbss` | 120   | 10 Offset Row, 4 Offset List | 10        |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 1      | `buildingbuff.dbss`       | 140 B (100.0%) | 0 B (0.0%) |
| 1      | `buildingbuffoffset.dbss` | 120 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                 |
| ------------------------- | -------- | -------------------------------------------------------------------- |
| `buildingbuffoffset.dbss` | Optional | `(list, buff_index) -> (offset, size)` of every row; the rows are fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A list count, then the lists back to
back; the file ends after the last list.

| Offset  | Type                   | Field      | Notes                                                       |
| ------- | ---------------------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32                    | list_count | `4` on clients 1784 and 3474                                |
| `+0x04` | Villa List[list_count] | lists      | List `i` holds `villa_count` `i + 1`; see Villa List        |

### Villa List (variable: 4 bytes + rows)

| Offset  | Type           | Field     | Notes                                                    |
| ------- | -------------- | --------- | -------------------------------------------------------- |
| `+0x00` | u32            | row_count | `0` for lists 1 to 3 on clients 1784 and 3474            |
| `+0x04` | Row[row_count] | rows      | See Row                                                  |

### Row (12 bytes)

| Offset  | Type | Field      | Notes                                                              |
| ------- | ---- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | buff_index | Position in the list, `0` up; the key within the list              |
| `+0x02` | u16  | skill_no   | The buff skill; LOC type 10 holds its name and effect text         |
| `+0x04` | i64  | cost       | Price in silver                                                    |

### `buildingbuffoffset.dbss`

The same list walk as the main file: a u32 list count, then per list a u32
row count and 10-byte rows. A row leaves out the list number; its list
stands for it.

| Offset  | Type                          | Field      | Notes                                       |
| ------- | ----------------------------- | ---------- | ------------------------------------------- |
| `+0x00` | u32                           | list_count | Equals the main file's `list_count`         |
| `+0x04` | Offset List[list_count]       | lists      | List `i` indexes main list `i`; see Offset List |

### Offset List (variable: 4 bytes + rows)

| Offset  | Type                  | Field     | Notes                                 |
| ------- | --------------------- | --------- | ------------------------------------- |
| `+0x00` | u32                   | row_count | Equals the main list's `row_count`    |
| `+0x04` | Offset Row[row_count] | rows      | See Offset Row                        |

### Offset Row (10 bytes)

| Offset  | Type | Field      | Notes                                                           |
| ------- | ---- | ---------- | --------------------------------------------------------------- |
| `+0x00` | u16  | buff_index | Key of the row it points at, together with the list             |
| `+0x02` | u32  | offset     | Start of the row's `skill_no` in `buildingbuff.dbss`, past its `buff_index` |
| `+0x06` | u32  | size       | `10`, `skill_no` and `cost`                                     |

On clients 1784 and 3474 every index row points at the row with its list
and `buff_index`.

## Field Names

The names are the columns of the `Villa_Skill` sheet: `SkillNo`,
`Count_Villa` and `Cost`. The sheet is in a private server's
`DataSheet_AuctionDataTable.xlsm` and `DataSheets.bexcel` on client 1784 and
in the `Villa_Skill` table of a private server on client 519.

| Source              | Rows | Shared skills with client 1784 | Shared skills with client 3474 |
| ------------------- | ---- | ------------------------------ | ------------------------------ |
| Client 519 table    | 6    | 6 of 6, same cost              | 4 of 4, same cost              |
| Client 1784 `.xlsm` | 8    | 3 of 3, same cost              | 2 of 2, same cost              |

The client 519 rows are skills `53657` to `53662` (90 and 180 minutes of
the three client 1784 buffs). The client 1784 sheet adds five private
server rows (`59790` to `59792`, `54132`, `56845`), and its compiled
`buildingbuff.dbss` holds the same eight rows in the same shape as this
layout. Every row of both sheets has `Count_Villa` `1`, and every file has
its rows in list 0.

The client 1784 server dump of the same private server loads the sheet into
`BuildingBuffStaticStatusManager`. Its loader reads `Count_Villa` as an int
and subtracts 1, logs "별채버프 인덱스는 최대 (%#)을 넘을 수 없습니다" (the
villa buff index cannot exceed %#) for a result above 3, reads `SkillNo` as
an int16 and `Cost` as an int64, and adds the row to the one of four maps
that result picks, keyed by that map's size before the insert. That is the
four lists, `buff_index` counting from 0 in each, and `villa_count` = list
number + 1. Its getter logs `getXXX villaCount : %#, index : %#`. The client
Lua reads the same pair: `ToClient_GetBuildingBuffCount()` lists, then
`ToClient_GetCountPerBuffKeyCount(keyCount)` rows each,
`ToClient_GetBuildingBuff(keyCount, buffIndex)` for the skill and
`ToClient_GetBuildingBuffCost(keyCount, buffIndex)` for the price. The 2016
PDB has no building buff struct.

## Notes

- The window groups the rows into one box per buff by skill name and puts
  each duration on a buy button: it cuts the name at `(` for the box title
  and takes the text between the brackets (`60 min`) as the button label,
  with the cost below it (`panel_window_camp_villabuff_all_1.luac`). The
  box icons are `WisdomOfLife_Up.dds` and `SkillAndExp_Up.dds`.
- Buying calls `ToClient_ApplyBuildingBuff(keyCount, buffIndex, true)` after
  the `LUA_CAMP_BUILDINGBUFF_MESSAGEBOX_DESC` confirmation.
  The window's footer, `LUA_BUILDINGBUFF_BOTTOMDESC`, says a Villa Scroll
  needs a Villa Invitation from the Villa Manager and an orange-grade tent
  equipped.
- The server dump's row object is 24 bytes: the skill number, the cost and
  an 8-byte field the loader sets to `0`. The file stores only the first two.
- The client 1784 and 3474 files differ only in their rows; the list count,
  the empty lists and the index shape are the same.

## Open Questions

### What `Count_Villa` Counts

Every known row, in the client 519 and 1784 sheets and in the client 1784
and 3474 files, has `Count_Villa` `1`, so lists 1 to 3 are always empty.
The server allows values 1 to 4, and the Lua calls the list number
`keyCount` and the client counts lists with `ToClient_GetBuildingBuffCount()`.
It may be the number of villa invitations (keys) a buff needs, but no row
uses a value above 1 to test that.
