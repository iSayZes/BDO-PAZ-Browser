# knowledgelearning.dbss + knowledgelearningoffset.dbss

## Overview

Defines how knowledge is obtained.

Primary use:
Mob kill → unlock knowledge entry

---

## File Pair

### knowledgelearningoffset.dbss

Structure:

- 12-byte header
- Repeating 12-byte records:

| Offset | Type | Meaning |
|--------|------|--------|
| +0x00  | u32  | Offset into `knowledgelearning.dbss` |
| +0x04  | u32  | Kind |
| +0x08  | u32  | Index ID (usually mob ID) |

---

### knowledgelearning.dbss

Observed layout:

| Offset | Type | Meaning |
|--------|------|--------|
| +0x00  | u32  | Mob ID |
| +0x09  | u32  | Knowledge ID |

---

## Key Concept

### kind

| Value | Meaning |
|------|--------|
| 13   | Knowledge via mob kill |

Only kind 13 is relevant for standard knowledge unlocks.

---

## Relationships

mob_id → loc → mob name  
knowledge_id → loc → knowledge entry name  

---

## Notes

- Offset file drives parsing
- DBSS layout is semi-structured
- +9 offset is observed, not guaranteed

---

## Usage

- Map mobs to knowledge entries
- Build knowledge acquisition systems
