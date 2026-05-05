# `<filename.ext>` Format

## Purpose

Describe what this file stores and what part of the game/tool it affects.

Example:

```text
Short example of the in-game meaning, UI display, or decoded output.
```

## Graph

### Tags

<!-- Tags describe the file's domain — use whatever fits, no fixed list. -->

- file format
- <!-- dbss | bss | loc | paz -->
- <!-- additional domain tags relevant to this file, e.g. npc, title, knowledge -->

### Connections

- [companion-file.ext](companion_file_ext.md) — brief role description
- [offset-file.ext](offset_file_ext.md) — brief role description

---

## Companion Files

List every file that must be read alongside this one. Omit this section if the
format is fully self-contained.

| File                  | Required | Role                                        |
| --------------------- | -------- | ------------------------------------------- |
| `companion.dbss`      | Required | Provides `id → (offset, size)` block lookup |
| `languagedata_en.loc` | Optional | English display strings                     |

All multi-byte values are little-endian unless noted otherwise.

---

## File Layout

Top-level structure of the file (compression, magic bytes, header).

| Offset  | Type | Field | Notes             |
| ------- | ---- | ----- | ----------------- |
| `+0x00` | u32  | count | Number of records |
| `+0x04` | ...  | data  | Record stream     |

---

## Record Structure

Repeat this sub-section once per logical record type. Use H3 headings.

### Header (N bytes)

| Offset  | Type | Field | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | id    |       |

### Row / Entry (N bytes, repeated `count` times)

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | u32  | field_a |       |
| `+0x04` | u32  | field_b |       |

Include observed value ranges or invariants inline as Notes cells.

---

## Enum Values

Document enumerations inline here or inside the section where they first appear.

| ID  | Name |
| --- | ---- |
| 0   | Name |
| 1   | Name |

---

## Suggested UI Layout

| Column | Type | Notes                            |
| ------ | ---- | -------------------------------- |
| ID     | num  | Primary key                      |
| Name   | text | LOC lookup fallback to raw value |

---

## Notes

- Bullet-point facts that don't fit neatly into a table.
- Cross-references to other confirmed behaviors.
- Disproven hypotheses worth recording so they aren't re-investigated.

---

## Open Questions

### Question Title

What is still unknown and why it matters. Include disproven candidates if any.
