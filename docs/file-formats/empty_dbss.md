# Empty DBSS Tables Format

## Purpose

DBSS tables the client ships with no records. Each file below is a u32 count
of `0` and nothing else, on client 3464:

| Main file                         | Offset companion                        |
| --------------------------------- | --------------------------------------- |
| `alchemystatus.dbss`              | `alchemystatusoffset.dbss`              |
| `buffcondition.dbss`              | `buffconditionoffset.dbss`              |
| `cashforui.dbss`                  | `cashforuioffset.dbss`                  |
| `chinaspawnoption.dbss`           | `chinaspawnoptionoffset.dbss`           |
| `grenadedata.dbss`                | `grenadedataoffset.dbss`                |
| `growthpasspointshop.dbss`        | `growthpasspointshopoffset.dbss`        |
| `installation.dbss`               | `installationoffset.dbss`               |
| `instancedungeonskillstatic.dbss` | `instancedungeonskillstaticoffset.dbss` |
| `itemtradegroupfromnpc.dbss`      | `itemtradegroupfromnpcoffset.dbss`      |
| `petmarketsetting.dbss`           | `petmarketsettingoffset.dbss`           |
| `petset.dbss`                     | `petsetoffset.dbss`                     |
| `servantcategory.dbss`            | `servantcategoryoffset.dbss`            |
| `worldquest.dbss`                 | none in the archive                     |

`itemcouponreward.dbss` also declares zero records but has 12 bytes after the
count; see [itemcouponreward](itemcouponreward_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes  | Records                               | Row bytes                  |
| ------ | -------------- | ------- | --------------------------------------- | ------ | ------------------------------------- | -------------------------- |
| 2      | 3473 and later | 3473    | `alchemystatus.dbss`                    | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `alchemystatusoffset.dbss`              | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `buffcondition.dbss`                    | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `buffconditionoffset.dbss`              | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `cashforui.dbss`                        | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `cashforuioffset.dbss`                  | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `chinaspawnoption.dbss`                 | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `chinaspawnoptionoffset.dbss`           | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `grenadedata.dbss`                      | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `grenadedataoffset.dbss`                | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `growthpasspointshop.dbss`              | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `growthpasspointshopoffset.dbss`        | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `installation.dbss`                     | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `installationoffset.dbss`               | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `instancedungeonskillstatic.dbss`       | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `instancedungeonskillstaticoffset.dbss` | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `itemtradegroupfromnpc.dbss`            | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `itemtradegroupfromnpcoffset.dbss`      | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `petmarketsetting.dbss`                 | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `petmarketsettingoffset.dbss`           | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `petset.dbss`                           | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `petsetoffset.dbss`                     | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `servantcategory.dbss`                  | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `servantcategoryoffset.dbss`            | 4      | -                                     | -                          |
| 2      | 3473 and later | 3473    | `worldquest.dbss`                       | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `alchemystatus.dbss`                    | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `alchemystatusoffset.dbss`              | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `buffcondition.dbss`                    | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `buffconditionoffset.dbss`              | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `cashforui.dbss`                        | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `cashforuioffset.dbss`                  | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `chinaspawnoption.dbss`                 | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `chinaspawnoptionoffset.dbss`           | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `grenadedata.dbss`                      | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `grenadedataoffset.dbss`                | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `growthpasspointshop.dbss`              | 424    | 15 Point Shop Record                  | 28                         |
| 1      | 1784           | 1784    | `growthpasspointshopoffset.dbss`        | 184    | 15 Index Row                          | 12                         |
| 1      | 1784           | 1784    | `installation.dbss`                     | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `installationoffset.dbss`               | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `instancedungeonskillstatic.dbss`       | 13,984 | 157 Skill Static Record               | 20 to 166, 89 on average   |
| 1      | 1784           | 1784    | `instancedungeonskillstaticoffset.dbss` | 1,888  | 157 Index Row                         | 12                         |
| 1      | 1784           | 1784    | `itemtradegroupfromnpc.dbss`            | 68,899 | 459 Trade Item Entry, 129 Trade Group | 123 to 159, 148 on average |
| 1      | 1784           | 1784    | `itemtradegroupfromnpcoffset.dbss`      | 1,294  | 129 Trade Index Row                   | 10                         |
| 1      | 1784           | 1784    | `petmarketsetting.dbss`                 | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `petmarketsettingoffset.dbss`           | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `petset.dbss`                           | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `petsetoffset.dbss`                     | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `servantcategory.dbss`                  | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `servantcategoryoffset.dbss`            | 4      | -                                     | -                          |
| 1      | 1784           | 1784    | `worldquest.dbss`                       | 4      | -                                     | -                          |

| Layout | File                                    | Known            | Unknown          |
| ------ | --------------------------------------- | ---------------- | ---------------- |
| 2      | `alchemystatus.dbss`                    | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `alchemystatusoffset.dbss`              | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `buffcondition.dbss`                    | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `buffconditionoffset.dbss`              | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `cashforui.dbss`                        | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `cashforuioffset.dbss`                  | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `chinaspawnoption.dbss`                 | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `chinaspawnoptionoffset.dbss`           | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `grenadedata.dbss`                      | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `grenadedataoffset.dbss`                | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `growthpasspointshop.dbss`              | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `growthpasspointshopoffset.dbss`        | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `installation.dbss`                     | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `installationoffset.dbss`               | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `instancedungeonskillstatic.dbss`       | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `instancedungeonskillstaticoffset.dbss` | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `itemtradegroupfromnpc.dbss`            | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `itemtradegroupfromnpcoffset.dbss`      | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `petmarketsetting.dbss`                 | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `petmarketsettingoffset.dbss`           | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `petset.dbss`                           | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `petsetoffset.dbss`                     | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `servantcategory.dbss`                  | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `servantcategoryoffset.dbss`            | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `worldquest.dbss`                       | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `alchemystatus.dbss`                    | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `alchemystatusoffset.dbss`              | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `buffcondition.dbss`                    | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `buffconditionoffset.dbss`              | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `cashforui.dbss`                        | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `cashforuioffset.dbss`                  | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `chinaspawnoption.dbss`                 | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `chinaspawnoptionoffset.dbss`           | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `grenadedata.dbss`                      | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `grenadedataoffset.dbss`                | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `growthpasspointshop.dbss`              | 124 B (29.2%)    | 300 B (70.8%)    |
| 1      | `growthpasspointshopoffset.dbss`        | 184 B (100.0%)   | 0 B (0.0%)       |
| 1      | `installation.dbss`                     | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `installationoffset.dbss`               | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `instancedungeonskillstatic.dbss`       | 632 B (4.5%)     | 13,352 B (95.5%) |
| 1      | `instancedungeonskillstaticoffset.dbss` | 1,888 B (100.0%) | 0 B (0.0%)       |
| 1      | `itemtradegroupfromnpc.dbss`            | 4,450 B (6.5%)   | 64,449 B (93.5%) |
| 1      | `itemtradegroupfromnpcoffset.dbss`      | 1,294 B (100.0%) | 0 B (0.0%)       |
| 1      | `petmarketsetting.dbss`                 | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `petmarketsettingoffset.dbss`           | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `petset.dbss`                           | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `petsetoffset.dbss`                     | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `servantcategory.dbss`                  | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `servantcategoryoffset.dbss`            | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `worldquest.dbss`                       | 4 B (100.0%)     | 0 B (0.0%)       |

<!-- versions:end -->

## Companion Files

None. Each offset companion in the table above is a file of its own with
the same layout as its main file.

All multi-byte values are little-endian.

## Layout 2

### File Layout

Main files and offset companions share one layout. No record structure can
be inferred because the files hold no records.

| Offset  | Type | Field | Notes                                  |
| ------- | ---- | ----- | -------------------------------------- |
| `+0x00` | u32  | count | Number of records; `0` in every file   |

The six files Layout 1 gives records have the same count of `0`, as tables
of their own so that Layout 1 can replace them.

### `growthpasspointshop.dbss`

| Offset  | Type | Field | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | count | `0`   |

### `growthpasspointshopoffset.dbss`

| Offset  | Type | Field | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | count | `0`   |

### `instancedungeonskillstatic.dbss`

| Offset  | Type | Field | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | count | `0`   |

### `instancedungeonskillstaticoffset.dbss`

| Offset  | Type | Field | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | count | `0`   |

### `itemtradegroupfromnpc.dbss`

| Offset  | Type | Field | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | count | `0`   |

### `itemtradegroupfromnpcoffset.dbss`

| Offset  | Type | Field | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | count | `0`   |

## Layout 1

On client 1784 three of these tables hold records: `growthpasspointshop.dbss`
(15 records), `instancedungeonskillstatic.dbss` (157 records) and
`itemtradegroupfromnpc.dbss` (129 groups), each with its offset companion.
The other files are the Layout 2 count of `0`. The tables below are those
six files on client 1784.

### `growthpasspointshop.dbss`

| Offset  | Type                     | Field   | Notes                 |
| ------- | ------------------------ | ------- | --------------------- |
| `+0x00` | u32                      | count   | `15` on client 1784   |
| `+0x04` | Point Shop Record[count] | records | See Point Shop Record |

### Point Shop Record (28 bytes)

| Offset  | Type | Field      | Notes                                                    |
| ------- | ---- | ---------- | -------------------------------------------------------- |
| `+0x00` | u32  | key        | Record key, `15` down to `1`; equals the index row key   |
| `+0x04` | u32  | key_dup    | Repeats `key` on every record                            |
| `+0x08` | u32  | unknown_08 | `750367` on every record (client 1784)                   |
| `+0x0C` | u32  | unknown_0c | `2` on every record (client 1784)                        |
| `+0x10` | u32  | unknown_10 | `0` on every record (client 1784)                        |
| `+0x14` | u32  | unknown_14 | `1` to `100`; `10` on 10 of the 15 records (client 1784) |
| `+0x18` | u32  | unknown_18 | `1`, `2`, `5` or `10` (client 1784)                      |

### `growthpasspointshopoffset.dbss`

| Offset  | Type             | Field | Notes                                       |
| ------- | ---------------- | ----- | ------------------------------------------- |
| `+0x00` | u32              | count | Equals the `growthpasspointshop.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row                               |

### Index Row (12 bytes)

The index row of `growthpasspointshopoffset.dbss` and
`instancedungeonskillstaticoffset.dbss`.

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u32  | key    | The record's `key`                                       |
| `+0x04` | u32  | offset | Start of the record in the main file plus 4, after `key` |
| `+0x08` | u32  | size   | Record length minus the 4-byte `key`                     |

### `instancedungeonskillstatic.dbss`

| Offset  | Type                       | Field   | Notes                   |
| ------- | -------------------------- | ------- | ----------------------- |
| `+0x00` | u32                        | count   | `157` on client 1784    |
| `+0x04` | Skill Static Record[count] | records | See Skill Static Record |

### Skill Static Record (variable: 16 bytes + text)

| Offset            | Type  | Field         | Notes                                                                 |
| ----------------- | ----- | ------------- | --------------------------------------------------------------------- |
| `+0x00`           | u32   | key           | Record key, equals the index row key; read as two u16 it is `1`, then a number such as `17581` |
| `+0x04`           | str16 | unknown_04    | Korean text with `<PAColor0x...>` tags, such as `<PAColor0xffe9bd23>바운드<PAOldColor>` |
| `unknown_04+0x00` | u32   | unknown_04_00 | `0` on every record (client 1784)                                     |

### `instancedungeonskillstaticoffset.dbss`

| Offset  | Type             | Field | Notes                                              |
| ------- | ---------------- | ----- | -------------------------------------------------- |
| `+0x00` | u32              | count | Equals the `instancedungeonskillstatic.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row                                      |

### `itemtradegroupfromnpc.dbss`

The Layout 1 shape of [`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md):
groups of item entries that open with a counted condition string.

| Offset  | Type               | Field  | Notes                |
| ------- | ------------------ | ------ | -------------------- |
| `+0x00` | u32                | count  | `129` on client 1784 |
| `+0x04` | Trade Group[count] | groups | See Trade Group      |

### Trade Group (variable: 6 bytes + item entries)

| Offset  | Type                         | Field        | Notes                       |
| ------- | ---------------------------- | ------------ | --------------------------- |
| `+0x00` | u16                          | character_id | Character key, LOC type `6` |
| `+0x02` | u32                          | item_count   | Number of item entries      |
| `+0x06` | Trade Item Entry[item_count] | entries      | See Trade Item Entry        |

### Trade Item Entry (variable: 123 bytes + condition text)

| Offset                   | Type      | Field                | Notes                                                       |
| ------------------------ | --------- | -------------------- | ----------------------------------------------------------- |
| `+0x00`                  | u16       | character_id         | Repeats the group key                                       |
| `+0x02`                  | u32       | item_id              | Item key, LOC type `0`                                      |
| `+0x06`                  | str16     | unknown_condition    | Empty, or a condition such as `getlifeLevel(7)>41`; 324 of the 459 entries hold one (client 1784) |
| `unknown_condition+0x00` | bytes[40] | unknown_condition_00 | All `0` on client 1784                                      |
| `unknown_condition+0x28` | u8        | trade_group_type     | `0` on every entry (client 1784)                            |
| `unknown_condition+0x29` | u8        | unknown_37           | `0` on every entry (client 1784)                            |
| `unknown_condition+0x2A` | bytes[51] | unknown_38           |                                                             |
| `unknown_condition+0x5D` | u16       | unknown_6b           | `0` on every entry (client 1784)                            |
| `unknown_condition+0x5F` | bytes[11] | unknown_6d           | Bytes 2 to 5 are a u32 `1000000` on every entry (client 1784) |
| `unknown_condition+0x6A` | u8        | unknown_7c           | `0`, `1` or `2` (client 1784)                               |
| `unknown_condition+0x6B` | u8        | commerce_type        | `1` to `9` (client 1784)                                    |
| `unknown_condition+0x6C` | u8        | unknown_7e           | `0` on every entry (client 1784)                            |

### `itemtradegroupfromnpcoffset.dbss`

| Offset  | Type                   | Field | Notes                                         |
| ------- | ---------------------- | ----- | --------------------------------------------- |
| `+0x00` | u32                    | count | Equals the `itemtradegroupfromnpc.dbss` count |
| `+0x04` | Trade Index Row[count] | rows  | See Trade Index Row                           |

### Trade Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                    |
| ------- | ---- | ------------ | ---------------------------------------- |
| `+0x00` | u16  | character_id | Group key                                |
| `+0x02` | u32  | offset       | Start of the group header                |
| `+0x06` | u32  | size         | Length of the whole group                |

## Notes

- Raw bytes of every file: `00 00 00 00`.
- The list comes from a scan of every file under `gamecommondata/binary/` for
  files of at most 8 bytes that are all zero.
- One handler class (`EmptyTableHandler`, `_common/empty_table.py`) previews
  every file in `_dbss/empty_tables/tables.py`. A file whose count is not `0`
  raises an error, so a client that fills one of these tables shows up as a
  parse error and in the tests.
- `worldquest.dbss` had the same 4 bytes before the 2026-09-27 client update.

## Open Questions

### Non-Empty Layout

No file has a record on client 3473, so every current record layout is
unknown; Layout 1 holds the client 1784 records of three tables. When a client ships
`count > 0` for one of these tables, it moves to its own doc and handler, with
records starting at `+0x04`.
