# `petequipskillaquire.dbss` Format

## Purpose

Defines the cost table for pet equip skill acquisition, keyed by `acquire_type_id` from `pet.dbss`. 21 records cover all distinct acquire tiers: 5 groups (0–4, 101–104, 201–204, 301–304, 401–404) plus one null (key=0). Each record contains 14 × 3-field cost sub-entries whose semantic mapping is not fully confirmed.

Example:

```text
acquire_type_id: 304  →  group=3 (regular pet), tier=4 (grade 3–4)
sub[0].cost_a: 160000   sub[1].cost_a: 150000
```

## Graph

### Tags

- file format
- dbss
- pet
- equip skill

### Connections

- [pet.dbss](pet_dbss.md) — `acquire_type_id` field keys into this file
- [petequipskillaquireoffset.dbss](petequipskillaquire_dbss.md#petequipskillaquireoffsetdbss) — keyed offset index

---

## Companion Files

| File                              | Required | Role                                              |
| --------------------------------- | -------- | ------------------------------------------------- |
| `petequipskillaquireoffset.dbss`  | Required | `acquire_type_id → (data_offset, data_size)` index |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                           |
| ------- | ---- | ----- | ------------------------------- |
| `+0x00` | u32  | count | Number of records (observed: 21)|

### Record (176 bytes, repeated `count` times)

| Offset   | Type      | Field       | Notes                                              |
| -------- | --------- | ----------- | -------------------------------------------------- |
| `+0x00`  | u32       | packed_key  | `(acquire_type_id << 16) \| acquire_type_id`       |
| `+0x04`  | u32       | —           | Always 0; reserved                                 |
| `+0x08`  | entry[14] | cost_table  | 14 × 12-byte sub-entries (see below)               |

The `packed_key` field encodes `acquire_type_id` in both u16 halves: the low u16 is the 2-byte file key prefix; the high u16 is the first 2 bytes of the data payload.

#### Cost Sub-entry (12 bytes × 14)

Each sub-entry starts at `+0x08 + index × 12`:

| Offset  | Type | Field   | Notes                                              |
| ------- | ---- | ------- | -------------------------------------------------- |
| `+0x00` | u32  | cost_a  | Primary cost value; 0 if not applicable            |
| `+0x04` | u32  | cost_b  | Secondary cost value; 0 if not applicable          |
| `+0x08` | u32  | cost_c  | Tertiary cost value; 0 if not applicable           |

Sub-entries 12 and 13 are always all-zero in every record. Sub-entries 0–11 carry varying values (see Key Groups below).

---

## Key Groups

Keys follow the pattern `(group × 100) + tier`, where:

| Group prefix | Tier range | Applies to                                     |
| ------------ | ---------- | ---------------------------------------------- |
| 0 (keys 1–4) | 1–4        | Basic/starter pet acquire type                 |
| 1 (101–104)  | 1–4        | Mid-tier pet acquire type                      |
| 2 (201–204)  | 1–4        | Higher-tier acquire type (identical to group 3)|
| 3 (301–304)  | 1–4        | Regular pets (most common in pet.dbss)         |
| 4 (401–404)  | 1–4        | Premium/Airiss pet acquire type                |
| 0 (key 0)    | —          | Null record; all-zero (used when `acquire_type_id=0` in pet.dbss) |

Groups 2 and 3 produce **identical** sub-entry content for matching tiers (201==301, 202==302, 203==303, 204==304).

### Tier effect on sub[0].cost_a

| Tier suffix | Groups 0–3 sub[0].cost_a | Group 4 sub[0].cost_a |
| ----------- | ------------------------ | --------------------- |
| 1, 2        | 120000                   | 10000                 |
| 3, 4        | 160000                   | 10000                 |

Group 4 (Airiss) uses 50000 and 120000 where other groups use 30000 and 150000.

---

## petequipskillaquireoffset.dbss

### Header (4 bytes)

| Offset  | Type | Field | Notes                                              |
| ------- | ---- | ----- | -------------------------------------------------- |
| `+0x00` | u32  | count | Must equal `petequipskillaquire.dbss` count (21)   |

### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                                       |
| ------- | ---- | ----------- | --------------------------------------------------------------------------- |
| `+0x00` | u16  | key         | `acquire_type_id`                                                           |
| `+0x02` | u32  | data_offset | Absolute byte offset in main file past the 2-byte key prefix                |
| `+0x06` | u16  | data_size   | Always 174 (= 176 − 2-byte key prefix)                                      |
| `+0x08` | u16  | —           | Always 0; padding                                                           |

`record_start = data_offset - 2` gives the position of the full 176-byte record.

---

## Observed Values

All non-zero values in cost sub-entries are multiples of 10000:

| Value   | Groups seen in              |
| ------- | --------------------------- |
| 10000   | All groups                  |
| 30000   | Groups 0–3                  |
| 50000   | Group 4 only                |
| 120000  | Groups 0–3 (tiers 1–2); Group 4 (all tiers) |
| 150000  | Groups 0–3                  |
| 160000  | Groups 0–3 (tiers 3–4)      |

---

## Suggested UI Layout

| Column           | Type | Notes                                                           |
| ---------------- | ---- | --------------------------------------------------------------- |
| Acquire Type ID  | num  | `acquire_type_id` (right-aligned, hex and decimal)              |
| Group            | num  | `acquire_type_id // 100`                                        |
| Tier             | num  | `acquire_type_id % 100`                                         |
| Sub[0] Cost A    | num  | First sub-entry primary cost                                    |
| Sub[0] Cost C    | num  | First sub-entry tertiary cost                                   |

For a full cost breakdown, display all 12 active sub-entries with their three cost fields.

---

## Notes

- The null record (key=0) is all-zero; it corresponds to pets where `acquire_type_id=0` in `pet.dbss` (no acquire cost defined).
- Groups 2 and 3 are structurally identical per tier — confirmed by comparing all 14 sub-entries for 201↔301, 202↔302, 203↔303, 204↔304.
- Group 4 (Airiss type) is the only group where all four tiers share the same sub-entry content (401==402==403==404).
- The 2-byte key prefix and the first 2 bytes of data together form a single u32 `(key<<16)|key`. Reading the record as u32-aligned from the key prefix is cleaner than splitting at the data boundary.
- Sub-entries 12 and 13 (offsets +0x98 and +0xA4) are always zero in all 21 records.

---

## Open Questions

### Sub-entry semantic mapping

Each record has 14 sub-entries with 3 u32 cost fields. The index (0–13) and the meaning of cost_a / cost_b / cost_c are not confirmed. Candidates: slot number (pet has max 9 equip slots), skill level tier, or skill category. The 3 fields may encode (acquire cost, reacquire/reroll cost, removal cost) or three different resource types (silver, special items, stamps). Cross-referencing against the in-game pet stable UI cost display or `petequipskill.bss` would help.

### Key group semantics

Groups 0–4 map to distinct pet tiers, but which game concept each group prefix represents is not confirmed. Group 4 (Airiss) is identified by its unique cost values. Groups 0–3 likely correspond to regular pet quality tiers or species categories, but the exact mapping is unconfirmed.

### Tier suffix meaning

Tiers 1–4 within each group differ only at sub[0].cost_a (120000 vs 160000). The tier suffix likely tracks grade range (e.g., tiers 1–2 = grades 0–1, tiers 3–4 = grades 2–4), but the exact grade-to-tier mapping is unconfirmed.
