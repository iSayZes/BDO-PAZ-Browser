# knowledgelearning.dbss + knowledgelearningoffset.dbss

## Overview

Defines how knowledge entries are obtained. Parsing is driven by
`knowledgelearningoffset.dbss`, which maps each entry to its offset in
`knowledgelearning.dbss` and supplies the entry's kind and an index ID.

---

## File Pair

### knowledgelearningoffset.dbss

- 12-byte header (skipped)
- Repeating 12-byte records:

| Offset | Type | Name    | Description                                      |
| ------ | ---- | ------- | ------------------------------------------------ |
| +0x00  | u32  | offset  | Byte offset into `knowledgelearning.dbss`        |
| +0x04  | u32  | kind    | Unlock trigger type (see Known Kinds below)      |
| +0x08  | u32  | idx_id  | Index ID — meaning depends on kind               |

---

### knowledgelearning.dbss

Records are accessed by absolute byte offset from the offset file.
Only one field is currently parsed:

| Offset | Type | Name         | Description                              |
| ------ | ---- | ------------ | ---------------------------------------- |
| +0x00  | ?    | unknown      | 9 bytes — layout not yet documented      |
| +0x09  | u32  | knowledge_id | Knowledge entry ID (matches LOC str_type=34 and `mentalcard.dbss`) |

---

## Known Kinds

| Value | Meaning                        |
| ----- | ------------------------------ |
| 13    | Knowledge via mob kill         |
| other | Unknown — other unlock triggers |

---

## Relationships

- `knowledge_id` → LOC `str_type=34`, `str_id1=knowledge_id` → knowledge entry name
- `knowledge_id` → `mentalcard.dbss` entry_id → node/category

---

## Open Questions

- What are the 9 bytes at +0x00 in `knowledgelearning.dbss`? (kind 13 speculation: mob ID at +0x00)
- What does `idx_id` encode for each kind?
- Are there other parsed fields in non-kind-13 records?
