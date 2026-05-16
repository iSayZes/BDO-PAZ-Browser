# `fairyequipskillaquire.dbss` Format

## Purpose

Defines fairy equip-skill acquisition cost tables keyed by acquire type IDs `501` through `504`. Each record stores 14 three-field cost sub-entries. `fairyequipskillaquireoffset.dbss` provides the keyed lookup into the main file.

Example:

```text
acquire_type_id: 504
sub[0]: 20000, 30000, 30000
sub[9]: 100000, 0, 10000
```

## Graph

### Tags

- file format
- dbss
- fairy
- equip skill

### Connections

- [fairyequipskillaquireoffset.dbss](#fairyequipskillaquireoffsetdbss) - keyed offset index
- `fairyequipskill.bss` - related fairy equip-skill table; no direct key relationship to acquire type IDs `501`-`504` was confirmed
- `fairyskillchange.dbss` - related fairy skill-change data; not required to parse this file

---

## Companion Files

| File                                 | Required | Role                                             |
| ------------------------------------ | -------- | ------------------------------------------------ |
| `fairyequipskillaquireoffset.dbss`   | Required | `acquire_type_id -> (data_offset, data_size)` index |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                            |
| ------- | ---- | ----- | -------------------------------- |
| `+0x00` | u32  | count | Number of records; observed `4`  |

### Record (176 bytes, repeated `count` times)

| Offset  | Type      | Field      | Notes                                        |
| ------- | --------- | ---------- | -------------------------------------------- |
| `+0x00` | u32       | packed_key | `(acquire_type_id << 16) \| acquire_type_id` |
| `+0x04` | u32       | reserved   | Always `0` in observed records               |
| `+0x08` | entry[14] | cost_table | 14 x 12-byte cost sub-entries                |

The first 2 bytes of each record are the file key prefix. The offset companion points to `record_start + 2`, so use `record_start = data_offset - 2` to read the full u32-aligned record.

#### Cost Sub-entry (12 bytes x 14)

Each sub-entry starts at `+0x08 + index * 12`:

| Offset  | Type | Field   | Notes                                   |
| ------- | ---- | ------- | --------------------------------------- |
| `+0x00` | u32  | cost_a  | Primary raw cost value; `0` if unused   |
| `+0x04` | u32  | cost_b  | Secondary raw cost value; `0` if unused |
| `+0x08` | u32  | cost_c  | Tertiary raw cost value; `0` if unused  |

Sub-entries 12 and 13 are all-zero in every observed record.

---

## Observed Records

| Acquire Type ID | Data Offset | Data Size | Non-zero Sub-entry Count | Notes                    |
| --------------- | ----------- | --------- | ------------------------ | ------------------------ |
| `504`           | `0x000006`  | `174`     | `12`                     | Most populated row       |
| `503`           | `0x0000B6`  | `174`     | `9`                      | Uses mostly `50000`      |
| `502`           | `0x000166`  | `174`     | `8`                      | Uses `70000`/`150000`    |
| `501`           | `0x000216`  | `174`     | `5`                      | Sparse highest-cost row  |

### Cost Matrix

Each cell is `(cost_a, cost_b, cost_c)`. Omitted sub-entries are `(0, 0, 0)`.

| Acquire Type ID | Sub-entry | Values                  |
| --------------- | --------- | ----------------------- |
| `504`           | `0`       | `(20000, 30000, 30000)` |
| `504`           | `1`       | `(30000, 10000, 20000)` |
| `504`           | `2`       | `(30000, 40000, 50000)` |
| `504`           | `3`       | `(20000, 30000, 40000)` |
| `504`           | `4`       | `(50000, 10000, 20000)` |
| `504`           | `5`       | `(30000, 30000, 40000)` |
| `504`           | `6`       | `(30000, 0, 0)`         |
| `504`           | `7`       | `(0, 0, 30000)`         |
| `504`           | `8`       | `(40000, 50000, 60000)` |
| `504`           | `9`       | `(100000, 0, 10000)`    |
| `504`           | `10`      | `(20000, 30000, 40000)` |
| `504`           | `11`      | `(50000, 0, 0)`         |
| `503`           | `0`       | `(50000, 50000, 0)`     |
| `503`           | `1`       | `(0, 50000, 50000)`     |
| `503`           | `2`       | `(50000, 0, 0)`         |
| `503`           | `3`       | `(50000, 50000, 50000)` |
| `503`           | `4`       | `(0, 50000, 50000)`     |
| `503`           | `5`       | `(50000, 50000, 0)`     |
| `503`           | `6`       | `(100000, 0, 0)`        |
| `503`           | `7`       | `(0, 0, 50000)`         |
| `503`           | `8`       | `(50000, 50000, 100000)` |
| `502`           | `0`       | `(70000, 0, 0)`         |
| `502`           | `1`       | `(0, 70000, 70000)`     |
| `502`           | `3`       | `(70000, 70000, 0)`     |
| `502`           | `4`       | `(0, 70000, 70000)`     |
| `502`           | `5`       | `(70000, 0, 0)`         |
| `502`           | `6`       | `(150000, 0, 0)`        |
| `502`           | `7`       | `(0, 0, 80000)`         |
| `502`           | `8`       | `(70000, 70000, 0)`     |
| `501`           | `1`       | `(0, 150000, 0)`        |
| `501`           | `3`       | `(150000, 0, 0)`        |
| `501`           | `4`       | `(0, 150000, 0)`        |
| `501`           | `6`       | `(250000, 0, 0)`        |
| `501`           | `7`       | `(0, 0, 150000)`        |

---

## `fairyequipskillaquireoffset.dbss`

### Header (4 bytes)

| Offset  | Type | Field | Notes                                              |
| ------- | ---- | ----- | -------------------------------------------------- |
| `+0x00` | u32  | count | Must equal `fairyequipskillaquire.dbss` count (`4`) |

### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u16  | key         | `acquire_type_id`; observed `504`, `503`, `502`, `501`       |
| `+0x02` | u32  | data_offset | Absolute byte offset in the main file past the 2-byte prefix |
| `+0x06` | u16  | data_size   | Always `174` (`176 - 2-byte key prefix`)                     |
| `+0x08` | u16  | padding     | Always `0`                                                   |

Rows are ordered descending by key and ascending by `data_offset`.

---

## Suggested UI Layout

| Column          | Type | Notes                                           |
| --------------- | ---- | ----------------------------------------------- |
| Acquire Type ID | num  | `acquire_type_id`; right-aligned numeric column |
| Active Entries  | num  | Count of sub-entries with any non-zero cost     |
| Max Cost        | num  | Maximum value across all cost fields            |
| Cost Table      | text | 14 sub-entries with three raw cost values each  |

For detailed views, show one row per `(acquire_type_id, sub_entry_index)` and omit all-zero sub-entries by default.

---

## Notes

- The format is structurally identical to `petequipskillaquire.dbss`, but with only 4 fairy acquire type records instead of 21 pet acquire type records.
- Extracted `fairyequipskill.bss` contains fairy skill IDs such as `49096`-`49129` and `49177`-`49181`; it did not contain acquire type IDs `501`-`504`.
- Extracted `fairyskillchange.dbss` and `fairyskillchangeoffset.dbss` are 50-row, 12-byte fixed tables. They are related to fairy skill changes, but are not needed for this acquire-cost table.
- LOC lookup for IDs `501`-`504` has many unrelated matches and no confirmed fairy acquire-type labels.

---

## Open Questions

### Acquire type semantics

IDs `501`-`504` likely identify fairy equip-skill acquisition tiers or fairy grades, but no extracted companion file confirmed the exact mapping.

### Sub-entry semantic mapping

The 14 sub-entry indices and the meanings of `cost_a`, `cost_b`, and `cost_c` are not confirmed. Candidate meanings include skill slot, fairy skill group, fairy tier, or distinct acquisition resources/cost phases.
