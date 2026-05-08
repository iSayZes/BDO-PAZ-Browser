# `journalquest.dbss` Format

## Purpose

Journal quest (adventure log) category and entry data. Defines the 12 journal log categories shown in the in-game Adventure Log UI (e.g., "Igor Batali's Adventure Log", "Shakatu Merchant Collection Log"), their volumes/entries, and per-entry metadata: journal category name, subtitle, page volume title, unlock condition (rich text with PAColor markup), 3D bookshelf scene references, and page references.

Example:

```text
Group 1 — Igor Batali's Adventure Log (cat_id=748)
  Entry 1 / Volume 1: unlock = "[Calpheon] territory main quest OR
      [Special Growth] Fughar's Memorandum Ch. 6 completion, Lv. 51"
  Pages: 3 (LOC type=18, id1=748, id2=1..3)
    "Hey There Big Fellow!" | "Irresistible Lure" | "The Divine Entity inside the Cave"

Group 2 — Shakatu Merchant Collection Log (cat_id=30006)
  Entry 1: unlock = ...
  Pages: 4 (LOC type=18, id1=30006, id2=1..4)
    "Accidental First Encounter" | "We Meet Again, Friend!" | ...
```

## Graph

### Tags

- file format
- dbss
- quest
- journal
- adventure log

### Connections

- [journalquestoffset.dbss](journalquestoffset_dbss.md) — index mapping `(group_id, entry_no)` to `(byte_offset, byte_size)` in this file
- [languagedata_en.loc](languagedata_loc.md) — journal page titles (`id4=0`) and story text (`id4=1`) via LOC `str_type=18`, `str_id1=journal_cat_id`, `str_id2=page_no`

---

## Companion Files

| File                         | Required | Role                                                                        |
| ---------------------------- | -------- | --------------------------------------------------------------------------- |
| `journalquestoffset.dbss`    | Required | Provides `(group_id, entry_no) → (byte_offset, byte_size)` record lookup   |
| `languagedata_en.loc`        | Optional | English journal metadata via LOC type=63; page titles and story text via LOC type=18 |

All multi-byte values are little-endian.

---

## File Layout

### Main File Header (8 bytes)

| Offset  | Type | Field         | Notes                                          |
| ------- | ---- | ------------- | ---------------------------------------------- |
| `+0x00` | u32  | group_count   | Total number of journal groups; observed `12`  |
| `+0x04` | u32  | unknown_1     | Observed `15`; meaning not confirmed           |

Records are not stored contiguously with a built-in index. Use `journalquestoffset.dbss` to locate each record.

### Offset File Header (4 bytes)

| Offset  | Type | Field         | Notes                                          |
| ------- | ---- | ------------- | ---------------------------------------------- |
| `+0x00` | u32  | group_count   | Number of journal groups; matches main file    |

Immediately followed by a logical stream of group index blocks (see below). The stream is stored in 120-byte physical chunks but should be parsed as a flat sequence of `u32` values.

### Offset File Group Block (variable length, repeated `group_count` times)

| Field          | Type              | Notes                                           |
| -------------- | ----------------- | ----------------------------------------------- |
| `group_id`     | u32               | Journal group number (1–12; ordering may differ from numeric order) |
| `entry_count`  | u32               | Number of entries in this group                 |
| entries        | entry_count × Entry | See below                                    |

### Offset File Entry Record (12 bytes)

| Offset  | Type | Field         | Notes                                             |
| ------- | ---- | ------------- | ------------------------------------------------- |
| `+0x00` | u32  | entry_no      | Entry number within the group (1-based)           |
| `+0x04` | u32  | byte_offset   | Byte offset of the record in the main file        |
| `+0x08` | u32  | byte_size     | Byte size of the record in the main file          |

---

## Record Structure

Records are variable length. Each record is accessed via the offset file.

### Record Header (variable, ~17 bytes before text)

| Offset  | Type | Field         | Notes                                                                  |
| ------- | ---- | ------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | group_id      | Journal group number                                                   |
| `+0x04` | u32  | entry_no      | Entry number within group (1-based)                                    |
| `+0x08` | u32  | unknown_08    | Varies per group; `0x00000d00`, `0x00000c00`, `0x00001401`, etc.       |
| `+0x0C` | u32  | unknown_0c    | Observed `0x00000000`                                                  |
| `+0x10` | u8   | unknown_10    | Observed `0x00`                                                        |

### Text Fields (variable, starts at +0x11, odd byte offset)

Beginning immediately at byte `+0x11` (odd-aligned), a sequence of null-terminated UTF-16LE strings separated by U+0000 terminators. Observed string fields in order:

| Field             | Encoding     | Notes                                                                   |
| ----------------- | ------------ | ----------------------------------------------------------------------- |
| `journal_title`   | utf16le + NUL | Journal category name (e.g., "이고르 바탈리의 모험일지 ")             |
| `subtitle`        | utf16le + NUL | One-line description of the journal category                            |
| `page_vol_title`  | utf16le + NUL | Volume/page title (e.g., "이고르 바탈리의 모험일지 1권")              |
| `unlock_condition`| utf16le + NUL | Rich text unlock requirement; may contain `<PAColor0xRRGGBBAA>` / `<PAOldColor>` markup |

Additional null separators (U+0000 pairs) may appear between fields. Exact field count per record is determined by the value at `unknown_08` (not yet confirmed).

### Model ID Fields (variable, ASCII NUL-terminated)

Two ASCII NUL-terminated strings appear near the tail of each record, separated by zero-padding:

| Field           | Example                                   | Notes                                             |
| --------------- | ----------------------------------------- | ------------------------------------------------- |
| `combine_model` | `Combine_Etc_Adventure_Bookshelf01"`      | Scene (combine/cutscene) asset ID for the bookshelf UI animation; trailing `"` is part of the stored string |
| `static_model`  | `Adventure_Bookshelf_Static_book_003`     | Static 3D mesh asset ID; suffix `001`–`005` varies per group |

### Page Reference Block (variable, at record tail)

N page reference `u32` values linking this entry to its journal pages via LOC type=18. Encoding varies by group type:

**Type A** — `(journal_cat_id << 16) | page_index` (groups 1, 4, 7, 11, 12):

| Field          | Notes                                                                                  |
| -------------- | -------------------------------------------------------------------------------------- |
| page_ref × N   | Each u32: hi16 = `journal_cat_id`, lo16 = page index (0-based)                        |
| `page_count`   | u32; count of page refs; follows the N values                                          |
| terminal       | u16 = `0x0000` (2 extra bytes; record size is not a multiple of 4 for these groups)   |

**Type B** — `(page_index << 16) | journal_cat_id` (groups 2, 3, 5, 6, 8, 9, 10):

| Field          | Notes                                                                                  |
| -------------- | -------------------------------------------------------------------------------------- |
| `page_count`   | u32; precedes the N values                                                             |
| page_ref × N   | Each u32: hi16 = page index (1-based), lo16 = `journal_cat_id`                        |
| terminal       | u32 = `0x00000000`                                                                     |

---

## Journal Group Table

Observed groups (12 total, offset-file order):

| Group ID | Entries | Journal Cat ID | Sample Page Titles (EN)                                                  |
| -------: | ------: | -------------: | ------------------------------------------------------------------------ |
|        1 |      15 |            748 | Hey There Big Fellow! / Irresistible Lure / The Divine Entity in the Cave |
|        2 |      11 |          30006 | Accidental First Encounter / We Meet Again, Friend! / Hard to Get But Easy to Spend |
|        3 |      10 |            897 | Boss: Calamity 1 Golden Pig King / Oduksini / Apex Changui …             |
|        4 |       1 |           2302 | At Port Epheria / In Calpheon / In Glish / At Heidel Castle …            |
|        5 |      13 |            790 | (LOC type=18, id1=790)                                                   |
|        6 |       7 |          11103 | (LOC type=18, id1=11103)                                                 |
|        7 |      15 |           8700 | (LOC type=18, id1=8700)                                                  |
|        8 |       1 |            896 | (empty/placeholder; no body text)                                        |
|        9 |      10 |            834 | (LOC type=18, id1=834)                                                   |
|       11 |       9 |           8721 | (LOC type=18, id1=8721)                                                  |
|       12 |      13 |           8542 | (LOC type=18, id1=8542)                                                  |
|       10 |       7 |           9131 | (LOC type=18, id1=9131)                                                  |

Note: Groups are stored in the offset file in the order shown above (group 10 appears last).

---

## Localization

Journal category metadata is in LOC `str_type=63`:

| LOC Field  | Value                       | Notes                                              |
| ---------- | --------------------------- | -------------------------------------------------- |
| `str_type` | `63`                        |                                                    |
| `str_id1`  | `group_id`                  | Journal group number                              |
| `str_id2`  | `entry_no`                  | Entry number within the group                     |
| `str_id4`  | `0` = category title, `1` = subtitle, `2` = unlock condition, `3` = volume title | Some groups have no `id4=2` unlock text |

Journal page titles and story text are in LOC `str_type=18`:

| LOC Field  | Value                       | Notes                                              |
| ---------- | --------------------------- | -------------------------------------------------- |
| `str_type` | `18`                        |                                                    |
| `str_id1`  | `journal_cat_id`            | From the page reference u32 (hi16 or lo16)         |
| `str_id2`  | page number (1-based)       | Corresponds to (page_ref lo16 or hi16) + offset    |
| `str_id4`  | `0` = page title, `1` = story text |                                             |

The inline `journal_title` / `subtitle` / `page_vol_title` fields in each record are Korean. English equivalents are in LOC type=63 for most entries. English page titles and story text are in LOC type=18.

---

## Suggested UI Layout

| Column              | Type | Notes                                                           |
| ------------------- | ---- | --------------------------------------------------------------- |
| Group               | num  | `group_id`                                                      |
| Entry               | num  | `entry_no`                                                      |
| Journal Category ID | num  | `journal_cat_id` from page ref u32                              |
| Title               | text | LOC type=63 `id4=0`, falling back to inline Korean `journal_title` |
| Subtitle            | text | LOC type=63 `id4=1`, falling back to inline Korean `subtitle`     |
| Volume              | text | LOC type=63 `id4=3`, falling back to inline Korean `page_vol_title` |
| Page Titles         | text | English LOC type=18 page titles resolved from page references    |
| Unlock Condition    | text | LOC type=63 `id4=2`, falling back to inline Korean `unlock_condition` with PAColor markup stripped |
| Pages               | num  | `page_count`                                                    |
| Combine Model       | text | `combine_model` (ASCII scene asset ID)                          |
| Static Model        | text | `static_model` (ASCII mesh asset ID)                            |

---

## Notes

- `journalquestoffset.dbss` has a 4-byte header (`count`) followed by data stored in 120-byte physical chunks; the logical structure (group_id, entry_count, entry triples) spans chunk boundaries and must be parsed as a flat `u32` stream.
- The main file has an 8-byte header; all records are accessed via the offset file. There is no inline offset table in the main file.
- Text fields start at odd byte offset `+0x0011` within each record. This is unusual for UTF-16LE and is an inherent quirk of the 9-byte prefix at `+0x0008`.
- Group 8 (1 entry, size=136) has no body text and appears to be a placeholder; the record consists almost entirely of zero bytes followed by model IDs and a single page reference.
- Group IDs in the offset file are not stored in numeric order: group 10 appears as the 12th (last) group in the offset file stream.
- Two page-reference encoding schemes exist (Type A and Type B); which a group uses appears to depend on the journal category and is not determined by a documented flag. Both encodings carry the same `(journal_cat_id, page_index)` pair.
- The `combine_model` ASCII string includes a trailing `"` character as part of the stored value (e.g., `Combine_Etc_Adventure_Bookshelf01"`). This is not a parsing artifact.
- Unlock condition text uses BDO's inline rich-text markup: `<PAColor0xAARRGGBB>` to set color, `<PAOldColor>` to reset, and backtick-delimited quest names.
- `(main_file_size - 8) / group_count` is not integral; records are variable length.
- PAColor tag format in this file uses `0x` followed by 8 hex digits (AARRGGBB order), e.g. `<PAColor0xFFf3d900>`.

---

## Open Questions

### `unknown_08` Field

The u32 at `+0x0008` in each record takes values such as `0x00000d00`, `0x00000c00`, `0x00001401`, `0x00000000` (empty entry). Its structure may encode two sub-fields (u8 flags at byte[8] and u8 count at byte[9]), but the meaning of either sub-field is not confirmed. It does not directly encode the title char count or entry count.

### Text Field Count and Boundary

The exact number of null-terminated UTF-16LE fields per record is not fully characterized. At least four fields are observed (title, subtitle, volume title, unlock condition), but some records may contain more. The field count may be encoded in `unknown_08`.

### Odd-Aligned Text Start

Text begins at byte `+0x0011` (odd byte offset) within each record, caused by the 9-byte block at `+0x0008..+0x0010`. The reason for a 9-byte block rather than an 8- or 12-byte block is not known.

### Page Index Base

Type A groups use lo16=0,1,2,… for page index (0-based), but LOC id2 appears to start at 1. Whether lo16=0 maps to LOC id2=1 (off-by-one) or lo16=0 is an unused/header page is not confirmed.

### English Journal Category Names

The inline `journal_title` field is Korean. A dedicated LOC type or table for English journal category names (as opposed to page titles) has not been identified.

### Main File `unknown_1` Header Field

The second u32 in the main file header (`+0x04`) is `15` in the observed data. Its role is unknown (possibly the maximum entry count across all groups, or an unrelated config value).
