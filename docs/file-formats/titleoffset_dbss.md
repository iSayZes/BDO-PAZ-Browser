# `titleoffset.dbss` Format

## Purpose

ID-keyed index into `title.dbss`. Maps each title ID to the byte offset and block size of the corresponding record in the main data file.

Example:

```text
title_id: 44  →  offset: 0x1A3C, size: 0x98
```

## Graph

### Tags

- file format
- dbss
- title
- offset index

### Connections

- [title.dbss](title_dbss.md) — main data file this index addresses

---

## File Layout

All multi-byte values are little-endian.

### Header (4 bytes)

| Offset  | Type | Field | Notes                    |
| ------- | ---- | ----- | ------------------------ |
| `+0x00` | u32  | count | Number of offset records |

### Offset Record (12 bytes, repeated `count` times)

| Offset  | Type | Field    | Notes                                          |
| ------- | ---- | -------- | ---------------------------------------------- |
| `+0x00` | u32  | title_id | Unique title identifier                        |
| `+0x04` | u32  | offset   | Byte offset into `title.dbss`                  |
| `+0x08` | u32  | size     | Byte count of the record block in `title.dbss` |

To read a title record: seek to `offset` in `title.dbss` and read `size` bytes.

---

## Notes

- Parsed by the shared `parse_offset_table` helper in `_dbss/common/binary.py`, also used by other `*offset.dbss` companion files.
