# `titlecategory.bss` Format

## Purpose

Lists the title IDs of each title category. A `PABR` file holding one counted list of `title.dbss` title IDs per category, in category order, followed by the usual `PABR` trailer.

Example:

```text
category 0 (World)  -> title_id 211, 212, 213, ...
category 1 (Combat) -> title_id 1, 2, 3, ...
```

## File Layout

All multi-byte values are little-endian.

### Header (8 bytes)

| Offset  | Type    | Field          | Notes                                  |
| ------- | ------- | -------------- | -------------------------------------- |
| `+0x00` | char[4] | magic          | `PABR` (ASCII)                         |
| `+0x04` | u32     | category_count | Number of category lists; observed `4` |

### Category List (repeated `category_count` times)

The list's position is its `category_id`, starting at `0`.

| Offset  | Type       | Field       | Notes                                   |
| ------- | ---------- | ----------- | --------------------------------------- |
| `+0x00` | u32        | title_count | Number of title IDs in this category    |
| `+0x04` | u32[count] | title_ids   | `title.dbss` title IDs                  |

### Trailer (12 bytes)

| Offset  | Type | Field          | Notes                                                    |
| ------- | ---- | -------------- | -------------------------------------------------------- |
| `+0x00` | u32  | unknown_00     | Observed `0`                                             |
| `+0x04` | u32  | end_of_entries | Byte offset right after the last list; `file_size - 12`  |
| `+0x08` | u32  | unknown_08     | Observed `0`                                             |

The number of listed titles follows from the header and trailer alone: `(end_of_entries - 8) / 4 - category_count`.

## Enum Values

### Category IDs

| ID  | Name       |
| --- | ---------- |
| 0   | World      |
| 1   | Combat     |
| 2   | Life Skill |
| 3   | Fishing    |

## Notes

- Observed lists (World, Combat, Life Skill, Fishing): `1,243`, `853`, `195`, `757` titles (`3,048` in all, `12,228` bytes) in the pre-2026-09-27 fixture; `1,316`, `900`, `197`, `759` (`3,172`, `12,724` bytes) in the 2026-09-27 client.
- Checked against `title.dbss` in both files: every title appears in exactly one list, the lists cover every `title.dbss` title, and each title's list matches the category `title.dbss` stores inline.
- Only the Combat list is sorted by title ID; the others start at `211` (World), `597` (Life Skill) and `218` (Fishing) and are not sorted.
- `title.dbss` carries the category inline, so `titlecategory.bss` is not needed for category display.
- Earlier versions of this doc, and of the handler, read the file as headerless 8-byte `(title_id, category_id)` pairs. That reading made the `PABR` magic the first title ID and paired unrelated title IDs after it.
