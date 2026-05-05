# `titlecategory.bss` Format

## Purpose

Maps title IDs to their category. A flat array of fixed-size records with no file header; record count is derived from file size.

Example:

```text
title_id: 44  →  category: 1 (Combat)
title_id: 218 →  category: 0 (World)
```

## Graph

### Tags

- file format
- bss
- title
- title category

### Connections

- [title.dbss](title_dbss.md) — title data file; also carries category inline after requirement text

---

## Record Structure

All multi-byte values are little-endian.

### Record (8 bytes, repeated for each entry)

| Offset  | Type | Field       | Notes                          |
| ------- | ---- | ----------- | ------------------------------ |
| `+0x00` | u32  | title_id    | Unique title identifier        |
| `+0x04` | u32  | category_id | Category code (see enum below) |

Record count = `file_size / 8`.

---

## Enum Values

### Category IDs

| ID  | Name       |
| --- | ---------- |
| 0   | World      |
| 1   | Combat     |
| 2   | Life Skill |
| 3   | Fishing    |

---

## Notes

- Little-endian throughout.
- No file header — parsing relies solely on file size being a multiple of 8.
- Category IDs outside 0–3 are decoded as `Unknown (N)` by the preview handler.
- `title.dbss` also carries the category field inline after requirement text; `titlecategory.bss` is not needed for category display.
- WIP: handler output is currently inaccurate.
