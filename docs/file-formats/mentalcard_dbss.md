# mentalcard.dbss + mentalcardoffset.dbss

## Overview

Maps knowledge entry IDs to their UI node (category) IDs. Used to build
knowledge trees and place entries within the knowledge UI.

---

## File Pair

### mentalcardoffset.dbss

- 12-byte header — content unknown, skipped by parser
- Repeating 12-byte records:

| Offset | Type | Name        | Description                              |
| ------ | ---- | ----------- | ---------------------------------------- |
| +0x00  | u32  | offset      | Byte offset into `mentalcard.dbss`       |
| +0x04  | u32  | size        | Block size at that offset                |
| +0x08  | u32  | internal_id | Row identifier from the offset file      |

---

### mentalcard.dbss

Each record (8 bytes, pointed to by offset file):

| Offset | Type | Name     | Description                              |
| ------ | ---- | -------- | ---------------------------------------- |
| +0x00  | u32  | entry_id | Knowledge entry ID — primary lookup key  |
| +0x04  | u32  | node_id  | UI node / category ID                    |

---

## Relationships

- `entry_id` → LOC `str_type=34`, `str_id1=entry_id` → knowledge entry name
- `node_id` → LOC `str_type=9`, `str_id1=node_id` → knowledge category name

---

## Notes

- `internal_id` (offset file) and `entry_id` (data file) are distinct fields — they may coincide but are read from separate positions
- Fixed-size records, no embedded strings
- Requires `.loc` for human-readable names

---

## Open Questions

- What are the 12 header bytes in `mentalcardoffset.dbss`?
- Does `internal_id` always equal `entry_id`, or does it serve a different purpose?
