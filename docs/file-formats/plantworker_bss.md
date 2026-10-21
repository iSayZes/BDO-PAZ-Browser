# `plantworker.bss` Format

## Purpose

Worker definition table. The file stores one fixed-size record per worker type/grade, with worker IDs, LOC-backed display names, basic worker stats, upgrade links, and a shared DDS icon path table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes  | Records           | Row bytes |
| ------ | -------------- | ------- | ----------------- | ------ | ----------------- | --------- |
| 2      | 3002 and later | 3474    | `plantworker.bss` | 99,484 | 106 Worker Record | 912       |
| 1      | 1230 to 2107   | 2107    | `plantworker.bss` | 66,794 | 91 Worker Record  | 707       |

| Layout | File              | Known          | Unknown          |
| ------ | ----------------- | -------------- | ---------------- |
| 2      | `plantworker.bss` | 5,780 B (5.8%) | 93,704 B (94.2%) |
| 1      | `plantworker.bss` | 4,823 B (7.2%) | 61,971 B (92.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3251   | Layout 2             |
| 3002   | Layout 2             |
| 2519   | No documented layout |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | Layout 1             |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                        |
| --------------------- | -------- | ----------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Provides worker display names via LOC type `6`, `str_id4=0` |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout (`_common/pabr_strings.py`): the header,
the fixed-size worker records, the icon path table and the 8-byte trailer.

| Offset             | Type                  | Field       | Notes                                                  |
| ------------------ | --------------------- | ----------- | ------------------------------------------------------ |
| `+0x00`            | char[4]               | magic       | `PABR` (ASCII)                                         |
| `+0x04`            | u32                   | count       | Number of worker records; observed `106`               |
| `+0x08`            | Worker Record[count]  | records     | See Worker Record                                      |
| `records+0x00`     | Icon Path Table       | icon_paths  | See Icon Path Table                                    |
| `icon_paths+0x00`  | u32                   | table_start | Offset of the icon path table, where the records end   |
| `icon_paths+0x04`  | u32                   | zero        | Always 0                                               |

The first record begins at offset `0x08`, immediately after the header. The
fixed block ends at `0x179A8` for the observed file, where the icon table
begins.

### Icon Path Table (variable: 4 bytes + strings)

Follows the worker record block.

| Offset  | Type        | Field | Notes                                      |
| ------- | ----------- | ----- | ------------------------------------------ |
| `+0x00` | u32         | count | Number of icon path entries; observed `38` |
| `+0x04` | pstr[count] | paths | UTF-8/ASCII DDS paths                      |

Each icon entry has one leading zero byte before the length (the `is_wide`
byte of a `pstr`, observed `0`). The length is the byte count including the
trailing NUL.

### Worker Record (912 bytes)

| Offset   | Type       | Field           | Notes                                              |
| -------- | ---------- | --------------- | -------------------------------------------------- |
| `+0x00`  | u16        | worker_id       | Worker/NPC ID; LOC type `6` name key               |
| `+0x02`  | u16        | next_worker_id  | Next-grade/linked worker ID, or `0`                |
| `+0x04`  | u16        | unknown_04      | Non-zero on 34 of 106 records on client 3473 (1011, 2001 to 2018), `0` on the rest |
| `+0x06`  | u32        | grade_class     | Grade the game colors the name by, see Grade Class |
| `+0x0A`  | u32        | unknown_0a      | Always `grade_class + 5`; meaning unresolved       |
| `+0x0E`  | u32        | move_speed      | Move speed × 100 (`200` is 2.00 in game)            |
| `+0x12`  | u32        | stamina         | Worker stamina                                     |
| `+0x16`  | u32        | luck            | Luck × 10,000 (`50000` is 5.00 in game)             |
| `+0x1A`  | u8         | unknown_1a      |                                                    |
| `+0x1B`  | u32        | icon_index      | Zero-based index into the trailing icon path table |
| `+0x1F`  | bytes[336] | unknown_1f      | See Open Questions                                 |
| `+0x16F` | u32        | base_work_speed | Work speed × 1,000,000 (`30000000` is 30.00)        |
| `+0x173` | bytes[541] | unknown_173     | See Open Questions                                 |

Records are fixed-size `0x390` byte structs. Remaining bytes contain many stat/progression values that are not fully named yet.

Earlier versions of this doc called `grade_class` `unknown_06`, and before that `unknown_loc_a`; `unknown_0a` was `unknown_loc_b`.

## Layout 1

On client 1784 a Worker Record was 707 bytes: `grade_class` and
`unknown_0a` were u16, which moved every later field 4 bytes earlier, and
the two unknown blocks were shorter (`unknown_1f` 256 bytes instead of 336,
`unknown_173` 420 instead of 541). Only the Worker Record differs from
Layout 2. Field names keep Layout 2's offsets, so `icon_index` sits at
`+0x17` here. On client 1784 the file holds 89 records.

### Worker Record (707 bytes)

| Offset   | Type       | Field           | Notes |
| -------- | ---------- | --------------- | ----- |
| `+0x00`  | u16        | worker_id       |       |
| `+0x02`  | u16        | next_worker_id  |       |
| `+0x04`  | u16        | unknown_04      |       |
| `+0x06`  | u16        | grade_class     |       |
| `+0x08`  | u16        | unknown_0a      |       |
| `+0x0A`  | u32        | move_speed      |       |
| `+0x0E`  | u32        | stamina         |       |
| `+0x12`  | u32        | luck            |       |
| `+0x16`  | u8         | unknown_1a      |       |
| `+0x17`  | u32        | icon_index      |       |
| `+0x1B`  | bytes[256] | unknown_1f      |       |
| `+0x11B` | u32        | base_work_speed |       |
| `+0x11F` | bytes[420] | unknown_173     |       |

## Grade Class

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
