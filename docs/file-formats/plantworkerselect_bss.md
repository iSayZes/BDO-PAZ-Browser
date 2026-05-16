# `plantworkerselect.bss` Format

## Purpose

Worker selection table keyed by town/node LOC IDs. Each group lists workers that can appear for one town/node, plus the observed worker hire cost/price tier.

Example rows:

```text
Calpheon City -> Naive Worker, 1500
Velia -> Giant Worker, 3500
Grana -> Papu Worker, 3500
Bukpo -> Dokkebi Worker, 3500
```

## Graph

### Tags

- file format
- bss
- worker
- town

### Connections

- [plantworker.bss](plantworker_bss.md) - provides worker definitions, worker display names, stats, and icon paths
- [languagedata_en.loc](languagedata_loc.md) - resolves `selection_id` through LOC type `17` and `worker_id` through LOC type `6`
- `plantworkerpassiveskill.bss` - same-prefix worker skill data; related, not required to parse this file

---

## Companion Files

| File                  | Required | Role                                                |
| --------------------- | -------- | --------------------------------------------------- |
| `plantworker.bss`     | Optional | Resolves `worker_id` to worker stats and icon paths |
| `languagedata_en.loc` | Optional | Resolves town/node names and worker names           |

All multi-byte values are little-endian unless noted otherwise.

---

## File Layout

| Offset  | Type | Field        | Notes                              |
| ------- | ---- | ------------ | ---------------------------------- |
| `+0x00` | u32  | group_count  | Number of selection groups; `30`   |
| `+0x04` | ...  | group_stream | `group_count` groups packed in row |

The file is fully consumed by `4 + sum(4 + entry_count * 0x10)`.

---

## Record Structure

### Selection Group

| Offset  | Type | Field       | Notes                                           |
| ------- | ---- | ----------- | ----------------------------------------------- |
| `+0x00` | u32  | entry_count | Number of entries in this group: 8, 12, or 13   |
| `+0x04` | ...  | entries     | `entry_count` 16-byte selection entries         |

Each group repeats one `selection_id` across all entries. Observed group sizes:

| Entry Count | Group Count |
| ----------- | ----------- |
| 8           | 2           |
| 12          | 8           |
| 13          | 20          |

### Selection Entry (`0x10` bytes)

| Offset  | Type | Field        | Notes                                                 |
| ------- | ---- | ------------ | ----------------------------------------------------- |
| `+0x00` | u16  | selection_id | Town/node LOC type `17` key; same value within group  |
| `+0x02` | u16  | worker_id    | Worker ID; matches `plantworker.bss` and LOC type `6` |
| `+0x04` | u32  | zero_a       | Always observed as `0`                                |
| `+0x08` | u32  | hire_cost    | Observed values: `1500`, `3500`, `10000`, `30000`, `90000` |
| `+0x0C` | u32  | zero_b       | Always observed as `0`                                |

Derived fields:

```text
selection_name = LOC type 17, str_id1=selection_id, str_id4=0
worker_name = LOC type 6, str_id1=worker_id, str_id4=0
```

---

## Selection IDs

| Selection ID | Name                   | Entry Count |
| ------------ | ---------------------- | ----------- |
| `5`          | Velia                  | 13          |
| `32`         | Heidel                 | 13          |
| `52`         | Glish                  | 13          |
| `77`         | Calpheon City          | 13          |
| `88`         | Olvia                  | 13          |
| `107`        | Keplan                 | 13          |
| `120`        | Port Epheria           | 13          |
| `126`        | Trent                  | 13          |
| `182`        | Iliya Island           | 13          |
| `202`        | Altinova               | 13          |
| `218`        | Asparkan               | 13          |
| `221`        | Tarif                  | 13          |
| `229`        | Valencia City          | 13          |
| `601`        | Shakatu                | 13          |
| `605`        | Sand Grain Bazaar      | 13          |
| `619`        | Ancado Inner Harbor    | 13          |
| `693`        | Arehaza                | 13          |
| `706`        | Old Wisdom Tree        | 8           |
| `735`        | Grana                  | 8           |
| `873`        | Duvencrune             | 13          |
| `955`        | O'draxxia              | 12          |
| `1124`       | Eilton                 | 12          |
| `1210`       | Dalbeol Village        | 12          |
| `1219`       | Nampo's Moodle Village | 12          |
| `1246`       | Nopsae's Byeot County  | 12          |
| `1375`       | Muzgar                 | 13          |
| `1420`       | Yukjo Street           | 12          |
| `1424`       | Godu Village           | 12          |
| `1444`       | Bukpo                  | 12          |
| `1553`       | Hakinza Sanctuary      | 13          |

---

## Reference Rows

| Group | Selection ID | Selection Name | Worker ID | Worker Name    | Hire Cost |
| ----- | ------------ | -------------- | --------- | -------------- | --------- |
| 0     | `77`         | Calpheon City  | `7501`    | Naive Worker   | `1500`    |
| 0     | `77`         | Calpheon City  | `7502`    | Giant Worker   | `3500`    |
| 0     | `77`         | Calpheon City  | `7571`    | Artisan Giant Worker | `90000` |
| 18    | `735`        | Grana          | `8001`    | Papu Worker    | `3500`    |
| 20    | `955`        | O'draxxia      | `8020`    | Dwarf Worker   | `3500`    |
| 21    | `1444`       | Bukpo          | `8047`    | Dokkebi Worker | `3500`    |

---

## Suggested UI Layout

| Column         | Type | Notes                                             |
| -------------- | ---- | ------------------------------------------------- |
| Selection ID   | num  | `selection_id`, right-aligned                     |
| Selection Name | text | Prefer LOC type `17`; fall back to `selection_id` |
| Worker ID      | num  | `worker_id`, right-aligned                        |
| Worker Name    | text | Prefer LOC type `6`; fall back to blank           |
| Hire Cost      | num  | `hire_cost`, right-aligned                        |

---

## Notes

- Observed file size is `6,076` bytes.
- There is no `PABR` magic; the file starts with the top-level group count.
- All `worker_id` values in this file exist in `plantworker.bss`.
- `zero_a` and `zero_b` are invariant zero fields across all observed entries.
- Worker costs map to a small fixed set: `1500`, `3500`, `10000`, `30000`, and `90000`.

## Open Questions

### `hire_cost` Semantics

The `+0x08` value behaves like a worker hire cost or price tier, but the exact in-game label has not been confirmed from UI evidence.
