# `instancedungeonskillstatic.dbss` Format

## Purpose

A keyed table whose name points at skill data for instance dungeons. On
client 3473 the file holds no records: it is a u32 count of `0`, and so is
its offset file. On client 1784 it holds 157 records, each a key and a
Korean text with `<PAColor0x...>` tags.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes  | Records                 | Row bytes                |
| ------ | -------------- | ------- | --------------------------------------- | ------ | ----------------------- | ------------------------ |
| 2      | 3473 and later | 3474    | `instancedungeonskillstatic.dbss`       | 4      | -                       | -                        |
| 2      | 3473 and later | 3474    | `instancedungeonskillstaticoffset.dbss` | 4      | -                       | -                        |
| 1      | 1784           | 1784    | `instancedungeonskillstatic.dbss`       | 13,984 | 157 Skill Static Record | 20 to 166, 89 on average |
| 1      | 1784           | 1784    | `instancedungeonskillstaticoffset.dbss` | 1,888  | 157 Index Row           | 12                       |

| Layout | File                                    | Known            | Unknown          |
| ------ | --------------------------------------- | ---------------- | ---------------- |
| 2      | `instancedungeonskillstatic.dbss`       | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `instancedungeonskillstaticoffset.dbss` | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `instancedungeonskillstatic.dbss`       | 632 B (4.5%)     | 13,352 B (95.5%) |
| 1      | `instancedungeonskillstaticoffset.dbss` | 1,888 B (100.0%) | 0 B (0.0%)       |

<!-- versions:end -->

## Companion Files

None. `instancedungeonskillstaticoffset.dbss` is the offset file of this
table; the PAZ Browser reads both with the Layout 1 records, so client 3473
shows an empty table and client 1784 its 157 records.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type | Field | Notes                                 |
| ------- | ---- | ----- | ------------------------------------- |
| `+0x00` | u32  | count | Number of records; `0` on client 3473 |

### `instancedungeonskillstaticoffset.dbss`

| Offset  | Type | Field | Notes                                              |
| ------- | ---- | ----- | -------------------------------------------------- |
| `+0x00` | u32  | count | Equals the `instancedungeonskillstatic.dbss` count |

## Layout 1

On client 1784 the table holds 157 records, each with an index row in
`instancedungeonskillstaticoffset.dbss`.

### File Layout

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

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u32  | key    | The record's `key`                                       |
| `+0x04` | u32  | offset | Start of the record in the main file plus 4, after `key` |
| `+0x08` | u32  | size   | Record length minus the 4-byte `key`                     |

## Open Questions

### Current Record Layout

Client 3473 ships no records, so whether a filled table would still read
as the client 1784 Skill Static Record is unknown. The handler reads
a filled table as Layout 1 and raises an error when the bytes do not fit it.

### What the Key and Text Hold

The key reads as two u16, `1` and a number such as `17581` (client 1784).
Whether that number is a skill key, and whether `unknown_04` is a skill name
or a tooltip line, is open.
