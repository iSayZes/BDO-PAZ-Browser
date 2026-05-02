# knowledgelearning.dbss + knowledgelearningoffset.dbss

## Overview

Defines how knowledge entries are obtained. Contains multiple kinds of unlock
triggers — not only mob kills. Kind 13 is the mob-kill variant; other kinds
exist but their semantics are not yet fully documented.

---

## File Pair

### knowledgelearningoffset.dbss

Structure:

- 12-byte header
- Repeating 12-byte records:

| Offset | Type | Meaning |
|--------|------|---------|
| +0x00  | u32  | Offset into `knowledgelearning.dbss` |
| +0x04  | u32  | Kind |
| +0x08  | u32  | Index ID (meaning depends on kind) |

---

### knowledgelearning.dbss

Observed layout for kind 13 records:

| Offset | Type | Meaning |
|--------|------|---------|
| +0x00  | u32  | Field A (mob ID for kind 13) |
| +0x09  | u32  | Knowledge ID |

Layout for other kinds is not yet documented.

---

## Known Kinds

| Value | Meaning |
|-------|---------|
| 13    | Knowledge via mob kill |
| other | Unknown — other unlock triggers |

---

## Relationships

knowledge_id → loc (str_type=34) → knowledge entry name

---

## Notes

- Offset file drives parsing
- DBSS layout at +0x09 is observed for kind 13, not guaranteed for other kinds

---

## Usage

- Map unlock triggers to knowledge entries
- Build knowledge acquisition systems
