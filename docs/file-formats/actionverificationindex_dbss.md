# `actionverificationindex.dbss` Format

## Purpose

The class types that have an action verification list: one record per class
type, keyed by the class type. On clients 1784 and 3474 the file holds 12
records, class types `52`, `53`, `55`, `58`, `60`, `61`, `63`, `65`, `69`,
`71`, `81` and `87`, which LOC type 21 names Jordine, Peony, Ahon Kirus,
Povios, Syaki, Sanmyoung, Nelydormin, Elgriffin, Orwen, `[PH] 12`, `[PH] 22`
and `[PH] 28`. The source sheets (see Field Names) also give each class type
a list of action names with an index; every list is empty in the client 1784
sheets, and the client 1784 and 3474 files hold no list data past the class
type. Companion `actionverificationindexoffset.dbss` lists where every record
sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                 | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | ------------------------------------ | ----- | --------------------- | --------- |
| 1      | 1485 and later | 3474    | `actionverificationindex.dbss`       | 112   | 12 Payload, 12 Record | 8         |
| 1      | 1485 and later | 3474    | `actionverificationindexoffset.dbss` | 148   | 12 Offset Row         | 12        |

| Layout | File                                 | Known          | Unknown      |
| ------ | ------------------------------------ | -------------- | ------------ |
| 1      | `actionverificationindex.dbss`       | 28 B (25.0%)   | 84 B (75.0%) |
| 1      | `actionverificationindexoffset.dbss` | 148 B (100.0%) | 0 B (0.0%)   |

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

| File                                  | Required | Role                                            |
| ------------------------------------- | -------- | ----------------------------------------------- |
| `actionverificationindexoffset.dbss`  | Required | `class_type -> (offset, size)` of every record  |
| `languagedata_en.loc`                 | Optional | Class names (LOC type 21, `str_id1` = class type, `str_id4` = `0`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no trailer.

| Offset  | Type          | Field   | Notes                                                    |
| ------- | ------------- | ------- | -------------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `12` on clients 1784 and 3474         |
| `+0x04` | Record[count] | records | See Record                                               |

The records fill the file exactly: 4 + 12 x 9 = 112 bytes on client 3474.
They are in ascending order of `class_type XOR 0xDEADBEEF` (`71`, `69`,
`65`, `87`, `81`, `63`, `61`, `60`, `58`, `55`, `53`, `52`), the order of
the server's sorted class type map (see Field Names).

### Record (9 bytes)

| Offset  | Type    | Field      | Notes                                                        |
| ------- | ------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8      | key_prefix | Copy of the class type; the offset row points past it        |
| `+0x01` | Payload | payload    | See Payload; the offset row points here                      |

### Payload (8 bytes)

| Offset  | Type     | Field      | Notes                                                                   |
| ------- | -------- | ---------- | ----------------------------------------------------------------------- |
| `+0x00` | u8       | class_type | Class type, the number `getClassType()` returns; the record key          |
| `+0x01` | bytes[7] | unknown_01 | Every byte `0` on clients 1784 and 3474; see Open Questions             |

### `actionverificationindexoffset.dbss`

Bare offset table into `actionverificationindex.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                              |
| ------- | ----------------- | ----- | -------------------------------------------------- |
| `+0x00` | u32               | count | Number of offset rows; equals the main file count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                     |

The rows fill the file exactly: 4 + 12 x 12 = 148 bytes on client 3474.
Their order differs from the main file's (`63`, `87`, `71`, `61`, `69`,
`81`, `65`, `60`, `58`, `55`, `53`, `52` on client 3474).

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                       |
| ------- | ---- | ----------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | class_type  | Key of the record it points at                                              |
| `+0x04` | u32  | data_offset | Absolute byte offset of the Payload in `actionverificationindex.dbss`, past its `key_prefix` |
| `+0x08` | u32  | data_size   | `8`, the Payload size                                                       |

The first record's Payload sits at `5`, after the count and its
`key_prefix`. The parser reads the main file through these rows and checks
that each record's `key_prefix` and `class_type` equal the offset row's key.

## Field Names

The names follow the `VerificationClassType` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`DataSheet_VerificationDataTable_Shadow.xlsm`. The sheet has the columns
`Index` (`1` to `12`, in ascending class type order) and `ClassType`. Its
12 class types are the 12 keys of the client 1784 file and of the live
file (12 of 12, client 3474). The file stores no `Index`.

The same workbook has one sheet per class type, named after it (`52` to
`87`), each with the columns `ClassType`, `Index` and `ActionName` and no
rows, and the `ActionVerification_Table` sheet (`CharacterKey`,
`ActionName`, `AbleCallTime`) that
[`actionverification.bss`](actionverification_bss.md) is compiled from.
Its character keys `65002` and up are the same heroes in LOC type 6
(`65002` Jordine, `65003` Peony).

The client 1784 server dump of the same private server names the type
`gc::ActionVerificationIndexStaticStatus` and keeps the records in a
`StaticStatusManager` keyed by `gc::ClassType` (RTTI). Its loader reads
the `ClassType` column of `VerificationClassType` as text, opens the sheet
of that name, and takes the class type from the sheet name. From each row
of that sheet it reads `ClassType` and `Index` as ints and hashes
`ActionName` to a u32, and adds `ActionName` hash -> `Index` to a map in
the record. A check after each row logs an error for an `Index` of `0` or
less or a class type of `101` or more. The record is 80 bytes in memory: an
8-byte field the loader sets to `0`, the action map and the class type as
one byte. A second check walks the class type list, binary-searching each
class type in the manager's map sorted by `class_type XOR 0xDEADBEEF`, and
logs an error for a missing one.

The 2016 PDB has no action verification type, the client 519 tables have no
such table, and no client Lua file (client 3474) names it.

## Notes

- The client 1784 and 3474 files are byte for byte the same, in both the
  main file and the offset file.
- LOC type 21 gives every one of the 12 class types a name with `str_id4`
  `0`; `[PH] 12`, `[PH] 22` and `[PH] 28` are placeholders.
- Nine of the 12 class types plus `64950` are the hero character keys of
  [`actionverification.bss`](actionverification_bss.md) (`52` and
  `65002` Jordine); `61`, `65` and `71` have no character there.

## Open Questions

### What `unknown_01` Holds

The 7 bytes after `class_type` are `0` in every record of clients 1784 and
3474. The server loader gives each record a map of `ActionName` hash ->
`Index` from the class type's own sheet, and every such sheet is empty on
client 1784, so a u32 entry count of `0` would fit, as in
[`actionverification.bss`](actionverification_bss.md), which stores each
action map as a u32 count and (hash, value) pairs. With no record that has actions, the split of the 7
bytes (a count, its width, padding) and the shape of a list entry stay
unknown.
