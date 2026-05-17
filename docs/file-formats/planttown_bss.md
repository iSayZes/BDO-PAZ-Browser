# `planttown.bss` Format

## Purpose

Town/node lookup table for worker and plant systems. The file stores a compact ordered list of node IDs that resolve through LOC type `29`; most rows are towns, villages, guard posts, islands, or trade-zone nodes.

Example rows:

```text
row 0  -> node 1785 -> Nampo's Moodle Village
row 8  -> node 1623 -> Grána
row 25 -> node 1301 -> Valencia City
row 42 -> node 1    -> Velia
```

## Graph

### Tags

- file format
- bss
- plant
- town
- node

### Connections

- [plantworkerselect.bss](plantworkerselect_bss.md) - uses a related town/worker selection concept, but stores separate selection IDs
- [plantworker.bss](plantworker_bss.md) - worker definitions used by town worker systems
- [plantzone.dbss](plantzone_dbss.md) - same plant-domain data family
- [languagedata_en.loc](languagedata_loc.md) - resolves node display names with LOC type `29`

---

## Companion Files

| File                  | Required | Role                                           |
| --------------------- | -------- | ---------------------------------------------- |
| `languagedata_en.loc` | Optional | Resolves `node_id` display names via type `29` |

All multi-byte values are little-endian.

---

## File Layout

### Header (8 bytes)

| Offset  | Type  | Field | Notes                         |
| ------- | ----- | ----- | ----------------------------- |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)                |
| `+0x04` | u32   | count | Number of rows; observed `45` |

### Row Stream

Rows start immediately after the header at `+0x08`. The observed file is fully described by:

```text
8-byte header + (45 * 12-byte rows) + 12-byte trailer = 560 bytes
```

### Trailer (12 bytes)

Follows the last row.

| Offset  | Type | Field       | Observed | Notes                                                |
| ------- | ---- | ----------- | -------- | ---------------------------------------------------- |
| `+0x00` | u32  | reserved_a  | `0`      | Observed zero                                        |
| `+0x04` | u32  | end_of_rows | `548`    | Byte offset immediately after rows; `8 + count * 12` |
| `+0x08` | u32  | reserved_b  | `0`      | Observed zero                                        |

---

## Record Structure

### Plant Town Row (12 bytes, repeated `count` times)

| Offset  | Type | Field     | Notes                                         |
| ------- | ---- | --------- | --------------------------------------------- |
| `+0x00` | u32  | node_id   | LOC type `29`, `str_id1=node_id`, `str_id4=0` |
| `+0x04` | u16  | unknown_a | Always observed as `1`                        |
| `+0x06` | u16  | unknown_b | Always observed as `2`                        |
| `+0x08` | u16  | unknown_c | Always observed as `10`                       |
| `+0x0A` | u16  | unknown_d | Always observed as `1`                        |

Derived field:

```text
node_name = LOC type 29, str_id1=node_id, str_id4=0
```

---

## Reference Rows

| Row | Node ID | Node Name              | unknown_a | unknown_b | unknown_c | unknown_d |
| --: | ------: | ---------------------- | --------: | --------: | --------: | --------: |
|   0 |  `1785` | Nampo's Moodle Village |       `1` |       `2` |      `10` |       `1` |
|   1 |  `1781` | Dalbeol Village        |       `1` |       `2` |      `10` |       `1` |
|   8 |  `1623` | Grána                  |       `1` |       `2` |      `10` |       `1` |
|  18 |  `1141` | Tarif                  |       `1` |       `2` |      `10` |       `1` |
|  25 |  `1301` | Valencia City          |       `1` |       `2` |      `10` |       `1` |
|  32 |   `601` | Calpheon               |       `1` |       `2` |      `10` |       `1` |
|  42 |     `1` | Velia                  |       `1` |       `2` |      `10` |       `1` |
|  44 |   `301` | Heidel                 |       `1` |       `2` |      `10` |       `1` |

---

## Suggested UI Layout

| Column    | Type | Notes                                            |
| --------- | ---- | ------------------------------------------------ |
| Node ID   | num  | `node_id`, right-aligned                         |
| Node Name | text | Prefer LOC type `29`; fall back to raw `node_id` |

---

## Notes

- Observed decompressed size is `560` bytes.
- `planttown.bss` has no same-stem companion file in the PAZ listing.
- All 45 `node_id` values resolve through LOC type `29` with `str_id4=0`.
- The row order is not numeric. It appears to be a curated display or processing order grouped roughly by newer/high-ID regions first and older towns later.
- `plantworkerselect.bss` uses related town selection data, but its IDs are not a direct match for this file; for example `planttown.bss` uses node `601` for Calpheon, while `plantworkerselect.bss` uses selection ID `77` for Calpheon City.

## Open Questions

### Constant Field Semantics

The four side fields are invariant across all observed rows (`1`, `2`, `10`, `1`). Their byte layout is confirmed, but their exact gameplay meaning is not identifiable from local cross-references.

### Row Order Meaning

The row order is stable and curated, but the exact consumer behavior is unknown. It may be a UI order, worker-system processing order, or region-order list.
