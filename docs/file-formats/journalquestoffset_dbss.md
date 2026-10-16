# `journalquestoffset.dbss` Format

## Purpose

Index file for `journalquest.dbss`. Maps each `(journal_key, book_key)` pair to a `(byte_offset, byte_size)` location within the main file. Field names follow [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor), re-verified against our files.

## Companion Files

| File                  | Required | Role                                          |
| --------------------- | -------- | --------------------------------------------- |
| `journalquest.dbss`   | Required | Contains the actual book records              |

All multi-byte values are little-endian.

## File Layout

### Header (4 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | group_count | Number of journal groups; observed `12` |

### Data Stream

Immediately after the header, `group_count` variable-length group blocks follow back to back:

```
for i in range(group_count):
    journal_key = read_u32()
    book_count  = read_u32()
    for j in range(book_count):
        book_key    = read_u32()
        byte_offset = read_u32()
        byte_size   = read_u32()
```

### Group Block (variable length)

| Field          | Type               | Notes                                                        |
| -------------- | ------------------ | ------------------------------------------------------------ |
| `journal_key`  | u32                | Journal group key (1 to 12; not in numeric order in file)    |
| `book_count`   | u32                | Number of books; equals the `book_count` word in the data file |
| books          | book_count × 12B   | Book index entries follow immediately                        |

### Book Index Entry (12 bytes)

| Offset  | Type | Field         | Notes                                                   |
| ------- | ---- | ------------- | ------------------------------------------------------- |
| `+0x00` | u32  | book_key      | Book key within the group; usually 1-based and contiguous, but journal 6 uses 1, 2, 10, 7, 8, 11, 12 |
| `+0x04` | u32  | byte_offset   | Absolute byte offset of the record in `journalquest.dbss` |
| `+0x08` | u32  | byte_size     | Exact byte size of the record                           |

## Notes

- File size is `4 + 8 × group_count + 12 × total_books`: `4 + 96 + 1,344 = 1,444` bytes for 12 groups and 112 books. The earlier reading of "120-byte physical chunks" was a coincidence (`1,440 = 12 × 120`); there is no chunking.
- Groups are stored in the order 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 10 (journal 10 last). This is also the physical group order in `journalquest.dbss`.
- `byte_offset` values are absolute offsets into `journalquest.dbss`. Every `byte_size` is exact: each record ends precisely on its `unknown_end` word, and the indexed records plus the 4-byte header and one 4-byte `book_count` per group tile the data file with no gaps (112 of 112 records, current file and fixture).
- Within a group, index order equals physical order except in journal 6, where books 2 and 10 are swapped physically.
- The current file and the older fixture are both `1,444` bytes with the same keys; only offsets and sizes differ.

## Display Order

[bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) states that the book index order is the UI order, independent of file order. It is neither: the journal shelf sorts books by `book_key`. The only journal where the file orders differ is journal 6 ("Event Logs"), which the offset file lists as 1, 2, 10, 7, 8, 11, 12 and the game shows as 1, 2, 7, 8, 10, 11, 12 (checked in game, 2026-09-28; see `journalquest_dbss.md`).
