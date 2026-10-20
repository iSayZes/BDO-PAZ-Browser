# `trainingvehicle.dbss` Format

## Purpose

The training dummies of Black Spirit's Training: one row per character of
vehicle type `51` (`Training` in [`characterstatic.dbss`](characterstatic_dbss.md)),
with its grade. On client 3474 the file has 3 rows: Scarecrow (`31506`) and
Advanced Scarecrow (`31508`), both with AI script `TrainingMonster`, and
Sandbag (`31511`) with `TrainingMonsterHouse`. These three are every
character of vehicle type `51` on that client. Companion
`trainingvehicleoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ------------ | --------- |
| 1      | 1784 and later | 3474    | `trainingvehicle.dbss`       | 28    | 3 Row        | 8         |
| 1      | 1784 and later | 3474    | `trainingvehicleoffset.dbss` | 34    | 3 Offset Row | 10        |

| Layout | File                         | Known         | Unknown    |
| ------ | ---------------------------- | ------------- | ---------- |
| 1      | `trainingvehicle.dbss`       | 28 B (100.0%) | 0 B (0.0%) |
| 1      | `trainingvehicleoffset.dbss` | 34 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                 |
| ---------------------------- | -------- | -------------------------------------------------------------------- |
| `trainingvehicleoffset.dbss` | Optional | `character_key -> (offset, size)` of every row; the main file can be walked without it |
| `characterstaticoffset.dbss` | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key link |
| `languagedata_en.loc`        | Optional | Character names (LOC type 6)                                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (8 bytes)

| Offset  | Type | Field             | Notes                                                                 |
| ------- | ---- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key     | Training dummy character; unique, and every key has a `characterstatic.dbss` row (client 3474) |
| `+0x02` | u16  | character_key_dup | Equal to `character_key` in every row; the offset file points here    |
| `+0x04` | i32  | grade             | `1` for Scarecrow and Sandbag, `2` for Advanced Scarecrow (clients 1784 and 3474) |

### `trainingvehicleoffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `trainingvehicle.dbss` count     |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                    |
| ------- | ---- | ------------- | -------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                              |
| `+0x02` | u32  | offset        | Row start + 2, at `character_key_dup`                    |
| `+0x06` | u32  | size          | The row without its leading `character_key`: always `6`  |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in main file order.

## Field Names

The names follow the `TrainingVehicle_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 and the same sheet in its
`datasheet_characterdatatable.xlsm`, columns `^Index`, `Grade`, `%ExpRate`
and `ContentsGroupKey`. The sheet has 5 rows; the 3 with `ContentsGroupKey`
`0` match the file by key and `grade` on clients 1784 and 3474 (3 of 3). The
other 2, Cart (`31551`) and Rowboat (`31552`) with contents group `1520`, are
missing from the file on both clients and have no `characterstatic.dbss` row
on client 3474. `%ExpRate` is a server-only column and `ContentsGroupKey` is
not in the file either.

The client 1784 server dump names the static status
`gc::TrainingVehicleStaticStatus`, keyed by a `KeyType<unsigned short>`, with
the members `_key`, `_grade` and `_expRate` (from its check messages). Its
sheet loader reads `Grade` with `ReadCellInt` into a 4-byte member at `+0x04`,
after the u16 key, and `ExpRate` as a float at `+0x08`. The file holds the key
and the 4-byte grade, so `grade` is an `i32`. The `TrainingVehicle_Table` of a
private server on client 519 has the same 3 rows with the same grades.

## Notes

- Client 1784 has the same 28-byte file, byte for byte.
- The file is not sorted by key: Sandbag (`31511`) comes first, Scarecrow
  (`31506`) last.
- The description of Book of Training - Skill (3 Days) (item `17999`, client
  3474) says it lets a player train "with the training scarecrows which can be
  found in any town" for Skill EXP, "when using Black Spirit's Training". Item
  `18815` on client 3474 is Black Spirit's Training Sandbag Installment.

## Open Questions

### What Grade Changes

Advanced Scarecrow has `grade` `2`, the other two `1`. No client Lua reads the
table: none of the 3,073 `.luac` files of client 3474 holds the text
`TrainingVehicle`. The AI scripts `TrainingMonster` and `TrainingMonsterHouse` do not
use a grade. Whether the grade scales the training EXP on the server, picks
which Books of Training work, or something else, is open. In the client 1784
sheet the server-only `%ExpRate` is `1.5` on the grade `2` row and `1` on the
others, but those values come from a private server and are not evidence.
