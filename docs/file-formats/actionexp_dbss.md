# `actionexp.dbss` Format

## Purpose

One row per class type and level with EXP amounts for action kinds: quests, gathering, processing, alchemy, fishing, horse taming, study, trade and farming on client 1784, where the client 3473 row has 8 bytes more. Every EXP byte is `0` on client 3473 and on client 1784, so the table holds the grid of class types and levels and nothing else. The 2016 client loads it into `gc::ActionExpStaticStatus` from the `ActionEXP_Table` sheet; no client Lua file names it. Companion `actionexpoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes   | Records                                             | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ------- | --------------------------------------------------- | --------- |
| 2      | 3473 and later | 3474    | `actionexp.dbss`       | 577,128 | 6,480 Level Row, 6,480 Level Entry, 102 Class Block | 85        |
| 2      | 3473 and later | 3474    | `actionexpoffset.dbss` | 78,164  | 6,480 Offset Row, 101 Offset Block                  | 12        |
| 1      | 1784           | 1784    | `actionexp.dbss`       | 263,658 | 3,250 Level Row, 3,250 Level Entry, 102 Class Block | 77        |
| 1      | 1784           | 1784    | `actionexpoffset.dbss` | 39,404  | 3,250 Offset Row, 101 Offset Block                  | 12        |

| Layout | File                   | Known              | Unknown           |
| ------ | ---------------------- | ------------------ | ----------------- |
| 2      | `actionexp.dbss`       | 58,728 B (10.2%)   | 518,400 B (89.8%) |
| 2      | `actionexpoffset.dbss` | 78,164 B (100.0%)  | 0 B (0.0%)        |
| 1      | `actionexp.dbss`       | 263,658 B (100.0%) | 0 B (0.0%)        |
| 1      | `actionexpoffset.dbss` | 39,404 B (100.0%)  | 0 B (0.0%)        |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                               |
| ---------------------- | -------- | -------------------------------------------------- |
| `actionexpoffset.dbss` | Required | `(class type, level) -> (offset, size)` of every row |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type               | Field  | Notes                                                  |
| ------- | ------------------ | ------ | ------------------------------------------------------ |
| `+0x00` | Class Block[..end] | blocks | One block per class type, from class type 0 up; see Class Block |

The file stores no block count. On client 3473 it holds 102 blocks: 36 with 180 rows (class types 0 to 36 without 18) and 66 empty ones (class type 18 and 37 to 101), 36 x (4 + 180 x 89) + 66 x 4 = 577,128 bytes.

### Class Block (variable: 4 bytes + entries)

| Offset  | Type                     | Field       | Notes                                              |
| ------- | ------------------------ | ----------- | -------------------------------------------------- |
| `+0x00` | u32                      | level_count | Rows in this block; `180` or `0` on client 3473    |
| `+0x04` | Level Entry[level_count] | entries     | See Level Entry                                    |

### Level Entry (89 bytes)

| Offset  | Type      | Field      | Notes                                         |
| ------- | --------- | ---------- | --------------------------------------------- |
| `+0x00` | u32       | key_prefix | Equals `level` of the row after it            |
| `+0x04` | Level Row | row        | See Level Row; the offset file points here    |

### Level Row (85 bytes)

| Offset  | Type      | Field      | Notes                                                        |
| ------- | --------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8        | class_type | Class type, the number `getClassType()` returns; equals the block index |
| `+0x01` | u32       | level      | `1` to `level_count`, ascending inside a block               |
| `+0x05` | bytes[80] | unknown_05 | Every byte `0` on client 3473; see Open Questions            |

### `actionexpoffset.dbss`

Index into `actionexp.dbss`, with the same block shape as the main file.

| Offset  | Type                | Field  | Notes                                     |
| ------- | ------------------- | ------ | ----------------------------------------- |
| `+0x00` | Offset Block[..end] | blocks | Blocks repeated until the end of the file |

The block index is the class type; the file stores no class type field. On client 3473 it holds 101 blocks (class types 0 to 100), one fewer than the main file: 36 x (4 + 180 x 12) + 65 x 4 = 78,164 bytes.

### Offset Block (variable: 4 bytes + rows)

| Offset  | Type                    | Field       | Notes                                       |
| ------- | ----------------------- | ----------- | ------------------------------------------- |
| `+0x00` | u32                     | level_count | Equals the main file block's `level_count`  |
| `+0x04` | Offset Row[level_count] | rows        | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | level       | Level of the row it points at                                      |
| `+0x04` | u32  | data_offset | Absolute byte offset of the Level Row in `actionexp.dbss`, just past its `key_prefix` |
| `+0x08` | u32  | data_size   | Always the Level Row size, `85` on client 3473                     |

The first row of class type 0 sits at `0x08`, after its block's `level_count` and the row's `key_prefix`. The parser reads the main file through these rows and checks that each row's `key_prefix`, `class_type` and `level` match the offset row's level and block.

## Layout 1

On client 1784 the Level Row holds nine i64 EXP fields (72 bytes) where Layout 2 has 80 bytes. The blocks keep their shape: 102 in the main file and 101 in `actionexpoffset.dbss`, 28 of them with 130 rows (class types 0 to 5, 7 to 12, 15 to 17 and 19 to 31), and `data_size` is `77`.

### Level Entry (81 bytes)

| Offset  | Type      | Field      | Notes                                         |
| ------- | --------- | ---------- | --------------------------------------------- |
| `+0x00` | u32       | key_prefix | Equals `level` of the row after it            |
| `+0x04` | Level Row | row        | See Level Row; the offset file points here    |

### Level Row (77 bytes)

| Offset  | Type | Field            | Notes                        |
| ------- | ---- | ---------------- | ---------------------------- |
| `+0x00` | u8   | class_type       | Equals the block index       |
| `+0x01` | u32  | level            | `1` to `130`                 |
| `+0x05` | i64  | quest_exp        | `0` on every row (client 1784) |
| `+0x0D` | i64  | collect_exp      | `0` on every row (client 1784) |
| `+0x15` | i64  | manufacture_exp  | `0` on every row (client 1784) |
| `+0x1D` | i64  | alchemy_exp      | `0` on every row (client 1784) |
| `+0x25` | i64  | fishing_exp      | `0` on every row (client 1784) |
| `+0x2D` | i64  | horse_taming_exp | `0` on every row (client 1784) |
| `+0x35` | i64  | study_exp        | `0` on every row (client 1784) |
| `+0x3D` | i64  | trade_exp        | `0` on every row (client 1784) |
| `+0x45` | i64  | farming_exp      | `0` on every row (client 1784) |

## Field Names

The 2016 `gc::ActionExpStaticStatus` (80 bytes in memory) holds `_class` (`gc::ClassType`, 1 byte), 3 bytes of alignment, `int _level` and nine `__int64` members `_questExp`, `_collectExp`, `_manufactureExp`, `_alchemytExp` (spelled so), `_fishingExp`, `_horseTamingExp`, `_studyExp`, `_tradeExp` and `_farmingExp`. The file packs these members without the alignment: 1 + 4 + 9 x 8 = 77 bytes, the client 1784 row size. The `ActionEXP_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 has the columns `Class`, `Level`, `Quest`, `Collect`, `Manufacture`, `Alchemy`, `Fishing`, `HorseTaming`, `Study`, `Trade` and `Farming` in the same order, and 3,640 rows (28 classes x 130 levels), as many as the client 1784 file.

Every EXP value is `0` in the sheet and in both client files, so the values cannot tell the slots apart; the Layout 1 names rest on the slot count and the member order. The sheet's class set differs from the client file's (it has classes 6 and 18 and lacks 7 and 15), a private server edit.

## Enum Values

### Class Type

`class_type` and the block index are class types, named by LOC type 21 (`str_id1` = class type, `str_id4` = `0`). On client 3473 the main file has rows for class types 0 to 36 except 18 (`Shai Male`), including types no character can pick: 13 and 36 (`PBM`), 14 (`Ain (No Use)`) and 22 (`Temp Maehwa`). LOC type 21 numbers class types 0 to 100, the 101 blocks of `actionexpoffset.dbss`.

## Notes

- The level range follows the life skill levels of [lifeexp](lifeexp_dbss.md): levels 1 to 130 here and 0 to 130 there on client 1784, 1 to 180 here and 0 to 180 there on client 3473.
- The main file ends with one more empty block than the offset file on both clients (102 against 101). The parser reads the main file only through the offset rows, so the extra `level_count` of `0` is never read.
- The 2016 client keeps the rows in `gc::ActionExpStaticStatusManager` as an array of 32 maps, one per class type, keyed by level. Its loader is `GameCommonParameterLoaderFromExcel::LoadActionExpStaticInformation`.
- [lifeexp](lifeexp_dbss.md) and [fitnesslevel](fitnesslevel_dbss.md) use the same block shape, but their offset rows point at the row itself; here each row has a u32 `key_prefix` before it.

## Open Questions

### Which EXP Slot Is New in the 80-Byte Payload

The Layout 2 row has 80 bytes after `level`, 8 more than the nine i64 fields of client 1784, the size of one more i64 EXP slot. Every byte is `0` on client 3473, and no newer struct or sheet than client 1784 names the columns, so neither the new slot's position nor its action kind is known. The nine old fields stay unnamed in Layout 2 until a client fills a value or a newer source lists the columns.
