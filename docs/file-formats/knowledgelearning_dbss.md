# `knowledgelearning.dbss` Format

## Purpose

Defines how knowledge entries are obtained. Records map knowledge IDs to their unlock trigger type and an associated index ID. Parsing is driven by `knowledgelearningoffset.dbss`, which provides each entry's byte offset, kind, and index ID.

Example:

```text
kind: 13 (mob kill)  →  knowledge_id: 4521  →  "Imp Captain"
```

## Graph

### Tags

- file format
- dbss
- knowledge

### Connections

- [mentalcard.dbss](mentalcard_dbss.md) — maps the same knowledge_id to its UI node/category
- [languagedata_en.loc](languagedata_loc.md) — English entry names (str_type=34, str_id1=knowledge_id)

---

## Companion Files

| File                           | Required | Role                                                     |
| ------------------------------ | -------- | -------------------------------------------------------- |
| `knowledgelearningoffset.dbss` | Required | Provides byte offsets, kind, and index ID for each entry |

All multi-byte values are little-endian.

---

## File Layout

### knowledgelearningoffset.dbss

- 12-byte header (content unknown, skipped)
- Repeating 12-byte records:

| Offset  | Type | Name   | Description                                 |
| ------- | ---- | ------ | ------------------------------------------- |
| `+0x00` | u32  | offset | Byte offset into `knowledgelearning.dbss`   |
| `+0x04` | u32  | kind   | Unlock trigger type (see Enum Values below) |
| `+0x08` | u32  | idx_id | Index ID — meaning depends on kind          |

### knowledgelearning.dbss

Records are accessed by absolute byte offset from the offset file. Only one field is currently parsed:

| Offset  | Type | Name         | Description                                                        |
| ------- | ---- | ------------ | ------------------------------------------------------------------ |
| `+0x00` | ?    | unknown      | 9 bytes — layout not yet documented                                |
| `+0x09` | u32  | knowledge_id | Knowledge entry ID (matches LOC str_type=34 and `mentalcard.dbss`) |

---

## Enum Values

### Known `kind` Values

| Value | Meaning                         |
| ----- | ------------------------------- |
| 13    | Knowledge via mob kill          |
| other | Unknown — other unlock triggers |

---

## Open Questions

### Unknown Header (knowledgelearningoffset.dbss)

The 12-byte header at the start of the offset file has unknown content.

### First 9 Bytes of Each Record

What are the 9 bytes at `+0x00` in `knowledgelearning.dbss`? For kind 13, speculation: mob ID at `+0x00`.

### idx_id Semantics

What does `idx_id` encode for each kind value?

### Non-kind-13 Record Fields

Are there additional parsed fields in records with kinds other than 13?
