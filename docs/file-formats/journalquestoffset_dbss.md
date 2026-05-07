# `journalquestoffset.dbss` Format

## Purpose

Index file for `journalquest.dbss`. Maps each `(group_id, entry_no)` pair to a `(byte_offset, byte_size)` location within the main file. Must be parsed before reading any individual journal entry.

## Graph

### Tags

- file format
- dbss
- journal
- offset index

### Connections

- [journalquest.dbss](journalquest_dbss.md) — main data file; records are located using this index

---

## Companion Files

| File                  | Required | Role                                          |
| --------------------- | -------- | --------------------------------------------- |
| `journalquest.dbss`   | Required | Contains the actual journal entry records     |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field       | Notes                                |
| ------- | ---- | ----------- | ------------------------------------ |
| `+0x00` | u32  | group_count | Number of journal groups; observed `12` |

### Data Stream

Immediately after the header, a flat `u32` stream encodes all group index blocks. The stream is physically stored in 120-byte chunks (i.e., `(file_size - 4) / 12 == 120`), but the logical structure spans chunk boundaries and must be read as a continuous sequence of `u32` values.

Parse the stream as follows:

```
for i in range(group_count):
    group_id     = read_u32()
    entry_count  = read_u32()
    for j in range(entry_count):
        entry_no    = read_u32()
        byte_offset = read_u32()
        byte_size   = read_u32()
```

### Group Block (logical, variable length)

| Field          | Type              | Notes                                                         |
| -------------- | ----------------- | ------------------------------------------------------------- |
| `group_id`     | u32               | Journal group identifier (1–12; not in numeric order in file) |
| `entry_count`  | u32               | Number of entries in this group                               |
| entries        | entry_count × 12B | Entry records follow immediately                              |

### Entry Record (12 bytes)

| Offset  | Type | Field         | Notes                                             |
| ------- | ---- | ------------- | ------------------------------------------------- |
| `+0x00` | u32  | entry_no      | Entry number within the group (1-based)           |
| `+0x04` | u32  | byte_offset   | Byte offset of the record in `journalquest.dbss`  |
| `+0x08` | u32  | byte_size     | Byte size of the record in `journalquest.dbss`    |

---

## Notes

- File size: `4 + group_count × 120` bytes (120-byte chunks align only by coincidence with 12 groups; the 120-byte chunks are a physical storage artifact, not meaningful blocks).
- Groups are stored in the order: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 10 — group 10 appears last.
- Byte offsets are absolute offsets into `journalquest.dbss` starting from byte 0.
