# mentalcard.dbss + mentalcardoffset.dbss

## Overview

These files define a mapping between:

- Entry ID (knowledge / entity)
- Node ID (UI / category grouping)

Used for building knowledge trees or UI placement.

---

## File Pair

### mentalcardoffset.dbss

Structure:

- 12-byte header
- Repeating 12-byte records:

| Offset | Type | Meaning |
|--------|------|--------|
| +0x00  | u32  | Offset into `mentalcard.dbss` |
| +0x04  | u32  | Record size |
| +0x08  | u32  | Internal ID |

---

### mentalcard.dbss

Each record (pointed to by offset):

| Offset | Type | Meaning |
|--------|------|--------|
| +0x00  | u32  | Entry ID |
| +0x04  | u32  | Node ID |

---

## Relationships

offset → mentalcard.dbss record  
entry_id → loc (str_type=34) → knowledge entry name  
node_id → loc (str_type=9) → knowledge category name  

---

## Notes

- Fixed-size structure
- No embedded strings
- Requires .loc for names

---

## Usage

- Build knowledge UI trees
- Group knowledge entries
