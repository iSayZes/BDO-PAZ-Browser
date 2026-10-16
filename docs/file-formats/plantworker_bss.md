# `plantworker.bss` Format

## Purpose

Worker definition table. The file stores one fixed-size record per worker type/grade, with worker IDs, LOC-backed display names, basic worker stats, upgrade links, and a shared DDS icon path table.

Example rows:

```text
worker 8047 -> Dokkebi Worker, next 8048, move 350, stamina 8, luck 50000
worker 7502 -> Giant Worker, next 7551, move 200, stamina 25, luck 50000
worker 7504 -> Goblin Worker, next 7552, move 350, stamina 8, luck 50000
```

## Companion Files

| File                  | Required | Role                                                        |
| --------------------- | -------- | ----------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Provides worker display names via LOC type `6`, `str_id4=0` |

All multi-byte values are little-endian.

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

## Record Structure

### Worker Record (`0x390` bytes)

| Offset   | Type | Field           | Notes                                              |
| -------- | ---- | --------------- | -------------------------------------------------- |
| `+0x00`  | u16  | worker_id       | Worker/NPC ID; LOC type `6` name key               |
| `+0x02`  | u16  | next_worker_id  | Next-grade/linked worker ID, or `0`                |
| `+0x04`  | u16  | reserved_a      | Observed `0`                                       |
| `+0x06`  | u32  | grade_class     | Grade the game colors the name by, see Grade Class |
| `+0x0A`  | u32  | unknown_0a      | Always `grade_class + 5`; meaning unresolved       |
| `+0x0E`  | u32  | move_speed      | Move speed × 100 (`200` is 2.00 in game)            |
| `+0x12`  | u32  | stamina         | Worker stamina                                     |
| `+0x16`  | u32  | luck            | Luck × 10,000 (`50000` is 5.00 in game)             |
| `+0x1B`  | u32  | icon_index      | Zero-based index into the trailing icon path table |
| `+0x16F` | u32  | base_work_speed | Work speed × 1,000,000 (`30000000` is 30.00)        |

Remaining bytes contain many stat/progression values that are not fully named yet.

Earlier versions of this doc called `grade_class` `unknown_06`, and before that `unknown_loc_a`; `unknown_0a` was `unknown_loc_b`.

### Grade Class

`grade_class` takes five values, one per name color in game (checked against the worker names on 2026-09-28):

| `grade_class` | Grade          | Color  | Workers (2026-09-27 client)                                      |
| ------------- | -------------- | ------ | ---------------------------------------------------------------- |
| `28023`       | Base or Naive  | green, white for Naive | 27: every plain `... Worker`, every `Naive ...` and the dev workers |
| `28024`       | Skilled        | blue   | 15, including `Demibeast Worker` (`8007`), which is white         |
| `28025`       | Professional   | yellow | 15                                                                |
| `28026`       | Artisan        | red    | 20, including the 115 WS Torres, Darifu, Zobadi and Afuaru        |
| `28027`       | Named          | yellow | 29 named workers such as Acher, Tirol and Tiny Nose               |

Naive and base workers share `28023`, and no other field in the record tells them apart, so inside that class the handler checks the English name for `Naive`. The five dev workers (`7996` QA Worker: Time, `7997` QA Worker: Luck, `7998` Grand Chamberlain, `7999` Temporary Laborer, `8000` QA Super Worker) are also `28023` but white in game, and `Demibeast Worker` (`8007`) is `28024` but white too: it is an unused worker with a goblin icon that upgrades into `Artisan Fadus Worker` (`8006`), per [BDO Codex](https://bdocodex.com/us/npc/8007/). The handler lists these six by ID. The values are not LOC keys: LOC type 6 rows with these IDs are unrelated monsters (`28023` Goblin Thrower).

Derived fields:

```text
name = LOC type 6, str_id1=worker_id, str_id4=0
icon_path = icon_paths[icon_index]
```

## Reference Rows

| Slot | Worker ID | Name           | Next Tier | Move | Stamina | Luck  | Icon Index | Base Work Speed |
| ---- | --------- | -------------- | --------- | ---- | ------- | ----- | ---------- | --------------- |
| 0    | `8047`    | Dokkebi Worker | `8048`    | 350  | 8       | 50000 | 0          | 60000000        |
| 100  | `7502`    | Giant Worker   | `7551`    | 200  | 25      | 50000 | 10         | 30000000        |
| 105  | `7504`    | Goblin Worker  | `7552`    | 350  | 8       | 50000 | 2          | 60000000        |

## Notes

- Observed decompressed size is `99,484` bytes, byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.
- File size matches `8 + (106 * 0x390) + 4 + encoded icon path table`.
- The trailing icon table contains `38` DDS paths under `New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/`.

## Open Questions

### Remaining Progression/Stat Arrays

The arrays between `+0x20` and `+0x38F` are not fully identified.

### `unknown_0a` Meaning

`unknown_0a` is always `grade_class + 5` (`28028` to `28032`). It resolves to unrelated LOC rows, and no other worker file references either value.
