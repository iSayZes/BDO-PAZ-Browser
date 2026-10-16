# `growthpasspointshop.dbss` Format

## Purpose

A keyed table whose name points at a Growth Pass point shop. On client 3473
the file holds no records: it is a u32 count of `0`, and so is its offset
file. On client 1784 it holds 15 fixed-size 28-byte records; what their
fields mean is not known.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records              | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ----- | -------------------- | --------- |
| 2      | 3473 and later | 3473    | `growthpasspointshop.dbss`       | 4     | -                    | -         |
| 2      | 3473 and later | 3473    | `growthpasspointshopoffset.dbss` | 4     | -                    | -         |
| 1      | 1784           | 1784    | `growthpasspointshop.dbss`       | 424   | 15 Point Shop Record | 28        |
| 1      | 1784           | 1784    | `growthpasspointshopoffset.dbss` | 184   | 15 Index Row         | 12        |

| Layout | File                             | Known          | Unknown       |
| ------ | -------------------------------- | -------------- | ------------- |
| 2      | `growthpasspointshop.dbss`       | 4 B (100.0%)   | 0 B (0.0%)    |
| 2      | `growthpasspointshopoffset.dbss` | 4 B (100.0%)   | 0 B (0.0%)    |
| 1      | `growthpasspointshop.dbss`       | 124 B (29.2%)  | 300 B (70.8%) |
| 1      | `growthpasspointshopoffset.dbss` | 184 B (100.0%) | 0 B (0.0%)    |

<!-- versions:end -->

## Companion Files

None. `growthpasspointshopoffset.dbss` is the offset file of this table; the
PAZ Browser reads both with the Layout 1 records, so client 3473 shows an
empty table and client 1784 its 15 records.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type | Field | Notes                                 |
| ------- | ---- | ----- | ------------------------------------- |
| `+0x00` | u32  | count | Number of records; `0` on client 3473 |

### `growthpasspointshopoffset.dbss`

| Offset  | Type | Field | Notes                                       |
| ------- | ---- | ----- | ------------------------------------------- |
| `+0x00` | u32  | count | Equals the `growthpasspointshop.dbss` count |

## Layout 1

On client 1784 the table holds 15 records, each with an index row in
`growthpasspointshopoffset.dbss`.

### File Layout

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

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u32  | key    | The record's `key`                                       |
| `+0x04` | u32  | offset | Start of the record in the main file plus 4, after `key` |
| `+0x08` | u32  | size   | Record length minus the 4-byte `key`                     |

## Open Questions

### Current Record Layout

Client 3473 ships no records, so whether a filled table would still read
as the client 1784 Point Shop Record is unknown. The handler reads
a filled table as Layout 1 and raises an error when the bytes do not fit it.

### What the Point Shop Record Fields Hold

`unknown_08` to `unknown_18` have no name in client data. Only `unknown_14`
and `unknown_18` vary per record (client 1784); what they count is open.
