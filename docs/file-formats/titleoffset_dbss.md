# titleoffset.dbss

ID-keyed index into `title.dbss`. Each record maps a title ID to the byte
offset and block size of the corresponding record in the main file.

Companion file: `title.dbss` — the main title data file this index addresses.

---

## Structure

### Header (4 bytes)

| Offset | Type | Field | Notes                    |
| ------ | ---- | ----- | ------------------------ |
| 0x00   | u32  | count | Number of offset records |

### Offset Record (12 bytes, repeated `count` times)

| Offset | Type | Field    | Notes                                          |
| ------ | ---- | -------- | ---------------------------------------------- |
| 0x00   | u32  | title_id | Unique title identifier                        |
| 0x04   | u32  | offset   | Byte offset into `title.dbss`                  |
| 0x08   | u32  | size     | Byte count of the record block in `title.dbss` |

To read a title record: seek to `offset` in `title.dbss` and read `size` bytes.

---

## Notes

- Little-endian throughout.
- Parsed by the shared `parse_offset_table` helper in `_dbss/common/binary.py`,
  which is also used by other `*offset.dbss` companion files.
