# `petset.dbss` Format

## Purpose

Empty pet set table placeholder. Current game data contains no pet set records; both
the main file and offset companion consist only of a zero row count.

Example:

```text
count: 0
```

## Graph

### Tags

- file format
- dbss
- pet
- placeholder

### Connections

- [petsetoffset.dbss](petset_dbss.md) - empty offset companion for this table
- [pet.dbss](pet_dbss.md) - active per-pet definition table

---

## Companion Files

| File                 | Required | Role                                                      |
| -------------------- | -------- | --------------------------------------------------------- |
| `petsetoffset.dbss`  | Optional | Empty offset companion; currently mirrors zero row count  |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                       |
| ------- | ---- | ----- | --------------------------- |
| `+0x00` | u32  | count | Number of records; observed 0 |

No record stream follows when `count = 0`.

---

## `petsetoffset.dbss`

### Header (4 bytes)

| Offset  | Type | Field | Notes                       |
| ------- | ---- | ----- | --------------------------- |
| `+0x00` | u32  | count | Number of offset records; observed 0 |

No offset records follow when `count = 0`.

---

## Suggested UI Layout

No table columns are needed while the file remains empty. A parsed preview may show
an empty-state message with the zero count.

---

## Notes

- `petset.dbss` size: 4 bytes (`00 00 00 00`).
- `petsetoffset.dbss` size: 4 bytes (`00 00 00 00`).
- `tools/binary_probe.py` classifies both files as high-confidence empty DBSS files.
- The file name suggests a pet grouping or set feature, but no current records are available to infer a record structure.
