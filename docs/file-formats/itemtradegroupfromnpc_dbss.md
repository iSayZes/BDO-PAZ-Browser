# `itemtradegroupfromnpc.dbss` Format

## Purpose

Item groups per NPC, the counterpart by name of
[`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md). On client 3473
the file holds no records: it is a u32 count of `0`, and so is its offset
file. On client 1784 it holds 129 groups of item entries with a trade
category, keyed by character key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes  | Records                   | Row bytes                  |
| ------ | -------------- | ------- | ---------------------------------- | ------ | ------------------------- | -------------------------- |
| 2      | 3473 and later | 3474    | `itemtradegroupfromnpc.dbss`       | 4      | -                         | -                          |
| 2      | 3473 and later | 3474    | `itemtradegroupfromnpcoffset.dbss` | 4      | -                         | -                          |
| 1      | 1784           | 1784    | `itemtradegroupfromnpc.dbss`       | 68,899 | 459 Item Entry, 129 Group | 123 to 159, 148 on average |
| 1      | 1784           | 1784    | `itemtradegroupfromnpcoffset.dbss` | 1,294  | 129 Index Row             | 10                         |

| Layout | File                               | Known            | Unknown          |
| ------ | ---------------------------------- | ---------------- | ---------------- |
| 2      | `itemtradegroupfromnpc.dbss`       | 4 B (100.0%)     | 0 B (0.0%)       |
| 2      | `itemtradegroupfromnpcoffset.dbss` | 4 B (100.0%)     | 0 B (0.0%)       |
| 1      | `itemtradegroupfromnpc.dbss`       | 4,450 B (6.5%)   | 64,449 B (93.5%) |
| 1      | `itemtradegroupfromnpcoffset.dbss` | 1,294 B (100.0%) | 0 B (0.0%)       |

<!-- versions:end -->

## Companion Files

None. `itemtradegroupfromnpcoffset.dbss` is the offset file of this table;
the PAZ Browser reads both with the Layout 1 groups and the
`itemtradegrouptonpc.dbss` columns, so client 3473 shows an empty table and
client 1784 its 459 item entries.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type | Field | Notes                                |
| ------- | ---- | ----- | ------------------------------------ |
| `+0x00` | u32  | count | Number of groups; `0` on client 3473 |

### `itemtradegroupfromnpcoffset.dbss`

| Offset  | Type | Field | Notes                                         |
| ------- | ---- | ----- | --------------------------------------------- |
| `+0x00` | u32  | count | Equals the `itemtradegroupfromnpc.dbss` count |

## Layout 1

The structures below match the Layout 1 structures of
[`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md#layout-1): groups
of item entries that open with a counted condition string.

### File Layout

| Offset  | Type         | Field  | Notes                |
| ------- | ------------ | ------ | -------------------- |
| `+0x00` | u32          | count  | `129` on client 1784 |
| `+0x04` | Group[count] | groups | See Group            |

### Group (variable: 6 bytes + item entries)

| Offset  | Type                   | Field        | Notes                       |
| ------- | ---------------------- | ------------ | --------------------------- |
| `+0x00` | u16                    | character_id | Character key, LOC type `6` |
| `+0x02` | u32                    | item_count   | Number of item entries      |
| `+0x06` | Item Entry[item_count] | entries      | See Item Entry              |

### Item Entry (variable: 123 bytes + condition text)

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

| Offset  | Type             | Field | Notes                                         |
| ------- | ---------------- | ----- | --------------------------------------------- |
| `+0x00` | u32              | count | Equals the `itemtradegroupfromnpc.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row                                 |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                     |
| ------- | ---- | ------------ | ------------------------- |
| `+0x00` | u16  | character_id | Group key                 |
| `+0x02` | u32  | offset       | Start of the group header |
| `+0x06` | u32  | size         | Length of the whole group |

## Open Questions

### Current Record Layout

Client 3473 ships no records, so whether a filled table would read as
the client 1784 groups or as the 127-byte Item Entry of
`itemtradegrouptonpc.dbss` Layout 2 is unknown. The handler reads
a filled table as Layout 1 and raises an error when the bytes do not fit it.
