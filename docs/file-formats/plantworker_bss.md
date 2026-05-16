# `plantworker.bss` Format

## Purpose

Worker definition table. The file stores one fixed-size record per worker type/grade, with worker IDs, LOC-backed display names, basic worker stats, upgrade links, and a shared DDS icon path table.

Example rows:

```text
worker 8047 -> Dokkebi Worker, next 8048, move 350, stamina 8, luck 50000
worker 7502 -> Giant Worker, next 7551, move 200, stamina 25, luck 50000
worker 7504 -> Goblin Worker, next 7552, move 350, stamina 8, luck 50000
```

## Graph

### Tags

- file format
- bss
- worker
- icon

### Connections

- [languagedata_en.loc](languagedata_loc.md) - worker names resolve through LOC type `6`, keyed by `worker_id`
- `plantworkerpassiveskill.bss` - same-prefix worker skill data; related, not required by this handler
- `plantworkerselect.bss` - same-prefix worker selection data; related, not required by this handler

---

## Companion Files

| File                  | Required | Role                                                        |
| --------------------- | -------- | ----------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Provides worker display names via LOC type `6`, `str_id4=0` |

All multi-byte values are little-endian.

---

## File Layout

### Header (8 bytes)

| Offset  | Type  | Field | Notes                                    |
| ------- | ----- | ----- | ---------------------------------------- |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)                           |
| `+0x04` | u32   | count | Number of worker records; observed `106` |

### Worker Records

Records are fixed-size `0x390` byte structs. The first record begins at offset `0x08`, immediately after the header. The fixed block ends at `0x179A8` for the observed file, where the icon table begins.

### Icon Path Table

Follows the worker record block.

| Offset  | Type | Field | Notes                                      |
| ------- | ---- | ----- | ------------------------------------------ |
| `+0x00` | u32  | count | Number of icon path entries; observed `38` |

Each icon entry has one leading zero byte before the length:

| Offset  | Type       | Field | Notes                                |
| ------- | ---------- | ----- | ------------------------------------ |
| `+0x00` | u8         | zero  | Observed `0`                         |
| `+0x01` | u32        | size  | Byte count including trailing NUL    |
| `+0x05` | char[size] | path  | UTF-8/ASCII DDS path, NUL-terminated |

---

## Record Structure

### Worker Record (`0x390` bytes)

| Offset   | Type | Field           | Notes                                              |
| -------- | ---- | --------------- | -------------------------------------------------- |
| `+0x00`  | u16  | worker_id       | Worker/NPC ID; LOC type `6` name key               |
| `+0x02`  | u16  | next_worker_id  | Next-grade/linked worker ID, or `0`                |
| `+0x04`  | u16  | reserved_a      | Observed `0`                                       |
| `+0x06`  | u32  | unknown_loc_a   | LOC-like ID; meaning unresolved                    |
| `+0x0A`  | u32  | unknown_loc_b   | LOC-like ID; meaning unresolved                    |
| `+0x0E`  | u32  | move_speed      | Worker move stat as displayed in worker data       |
| `+0x12`  | u32  | stamina         | Worker stamina                                     |
| `+0x16`  | u32  | luck            | Worker luck                                        |
| `+0x1B`  | u32  | icon_index      | Zero-based index into the trailing icon path table |
| `+0x16F` | u32  | base_work_speed | Base work speed value                              |

Remaining bytes contain many stat/progression values that are not fully named yet.

Derived fields:

```text
name = LOC type 6, str_id1=worker_id, str_id4=0
icon_path = icon_paths[icon_index]
```

---

## Reference Rows

| Slot | Worker ID | Name           | Next Tier | Move | Stamina | Luck  | Icon Index | Base Work Speed |
| ---- | --------- | -------------- | --------- | ---- | ------- | ----- | ---------- | --------------- |
| 0    | `8047`    | Dokkebi Worker | `8048`    | 350  | 8       | 50000 | 0          | 60000000        |
| 100  | `7502`    | Giant Worker   | `7551`    | 200  | 25      | 50000 | 10         | 30000000        |
| 105  | `7504`    | Goblin Worker  | `7552`    | 350  | 8       | 50000 | 2          | 60000000        |

---

## Suggested UI Layout

| Column     | Type | Notes                                     |
| ---------- | ---- | ----------------------------------------- |
| Worker ID  | num  | `worker_id`                               |
| Icon       | text | Render `icon_path` with icon-cell preview |
| Name       | text | Prefer LOC type `6`; fall back to blank   |
| Next Tier  | num  | `next_worker_id`, blank when zero         |
| Move       | num  | `move_speed`                              |
| Stamina    | num  | `stamina`                                 |
| Luck       | num  | `luck`                                    |
| Work Speed | num  | `base_work_speed`                         |

---

## Notes

- Observed decompressed size is `99,484` bytes.
- File size matches `8 + (106 * 0x390) + 4 + encoded icon path table`.
- The trailing icon table contains `38` DDS paths under `New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/`.

## Open Questions

### Remaining Progression/Stat Arrays

The arrays between `+0x20` and `+0x38F` are not fully identified.

### unknown_loc_a and unknown_loc_b

Both fields resolve to unrelated LOC rows in current English data — their purpose is unconfirmed.
