# `titleoffset.dbss` Format

## Purpose

ID-keyed index into `title.dbss`. Maps each title ID to the byte offset and block size of the corresponding record in the main data file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records             | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | ------------------- | --------- |
| 1      | 1485 and later | 3474    | `titleoffset.dbss` | 38,128 | 3,177 Offset Record | 12        |

| Layout | File               | Known             | Unknown    |
| ------ | ------------------ | ----------------- | ---------- |
| 1      | `titleoffset.dbss` | 38,128 B (100.0%) | 0 B (0.0%) |

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

## Layout 1

All multi-byte values are little-endian.

### File Layout

| Offset  | Type                 | Field   | Notes                    |
| ------- | -------------------- | ------- | ------------------------ |
| `+0x00` | u32                  | count   | Number of offset records; `3,048` in the pre-2026-09-27 fixture, `3,172` in the 2026-09-27 client |
| `+0x04` | Offset Record[count] | records | See Offset Record        |

### Offset Record (12 bytes)

| Offset  | Type | Field    | Notes                                          |
| ------- | ---- | -------- | ---------------------------------------------- |
| `+0x00` | u32  | title_id | Unique title identifier                        |
| `+0x04` | u32  | offset   | Byte offset into `title.dbss`                  |
| `+0x08` | u32  | size     | Byte count of the record block in `title.dbss` |

To read a title record: seek to `offset` in `title.dbss` and read `size` bytes.

## Notes

- Parsed by the shared `parse_offset_table` helper in `_common/binary.py`, also used by other `*offset.dbss` companion files.
- The file is exactly `4 + count × 12` bytes in both files, and the lowest `offset` is `4`: the first title record follows the `title.dbss` u32 count.
