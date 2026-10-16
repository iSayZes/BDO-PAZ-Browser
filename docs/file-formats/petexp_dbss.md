# `petexp.dbss` Format

## Purpose

Defines pet experience curves keyed by EXP table ID. Each record stores a maximum pet level and per-level u64 EXP thresholds. Companion `petexpoffset.dbss` provides keyed lookup into this fixed-size record stream.

Example:

```text
exp_table_id: 9
max_level: 50
level_exp[1..5]: 2055, 2260, 2599, 2989, 3437
```

## Companion Files

| File                 | Required | Role                                                     |
| -------------------- | -------- | -------------------------------------------------------- |
| `petexpoffset.dbss`  | Required | `exp_table_id -> (data_offset, data_size)` lookup index |

All multi-byte values are little-endian.

## File Layout

### Header (6 bytes)

| Offset  | Type | Field            | Notes                                                                                 |
| ------- | ---- | ---------------- | ------------------------------------------------------------------------------------- |
| `+0x00` | u32  | count            | Number of EXP table records (observed: 9)                                             |
| `+0x04` | u16  | first_record_key | `exp_table_id` of the first record; this is record 0's key prefix, not header payload |

> Records begin immediately after the u32 count. The two bytes at `+0x04` are the first record's key prefix.

### Record (408 bytes in stream, repeated `count` times)

Each record is stored as `[u16 key_prefix][data_bytes]`. The companion offset points to `data_bytes`, so `record_start = data_offset - 2`.

| Offset  | Type | Field      | Notes                                               |
| ------- | ---- | ---------- | --------------------------------------------------- |
| `+0x00` | u16  | key_prefix | Equals `exp_table_id` in the following data payload |
| `+0x02` | u8[] | data_bytes | 406-byte payload; see below                         |

### Data Payload (406 bytes)

Offsets are relative to `data_offset` from `petexpoffset.dbss`.

| Offset  | Type     | Field        | Notes                                                                                  |
| ------- | -------- | ------------ | -------------------------------------------------------------------------------------- |
| `+0x00` | u16      | exp_table_id | Matches the 2-byte key prefix and the companion offset key                              |
| `+0x02` | u32      | max_level    | Number of valid EXP thresholds in `level_exp` (observed: 10, 20, 30, 50)               |
| `+0x06` | u64 x 50 | level_exp    | Fixed-capacity threshold array; only first `max_level` values are populated            |

Unused `level_exp` slots after `max_level` are zero-filled. Data size is always 406 bytes (`2 + 4 + 50 * 8`) even when `max_level` is less than 50.

## Observed Records

| EXP Table ID | Max Level | First EXP Values                       | Last Populated EXP Values |
| ------------ | --------- | -------------------------------------- | ------------------------- |
| 9            | 50        | 2055, 2260, 2599, 2989, 3437          | 13588, 13724, 13861       |
| 8            | 30        | 1746, 1921, 2209, 2541, 2922          | 9105, 9196, 9288          |
| 7            | 20        | 2055, 2260, 2599, 2989, 3437          | 9328, 9794, 10284         |
| 6            | 10        | 2055, 2260, 2599, 2989, 3437          | 5228, 6012, 6914          |
| 5            | 10        | 100, 300, 500, 700, 900               | 1500, 1700, 1900          |
| 4            | 10        | 300, 450, 660, 860, 860               | 1760, 2020, 3020          |
| 3            | 10        | 216, 324, 468, 612, 756               | 1260, 1440, 2160          |
| 2            | 10        | 144, 216, 312, 408, 504               | 840, 960, 1440            |
| 1            | 10        | 120, 180, 260, 340, 420               | 700, 800, 1200            |

Together the nine tables hold 160 level thresholds. Both files are byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.

## petexpoffset.dbss

Provides keyed lookup into `petexp.dbss`.

### Header (4 bytes)

| Offset  | Type | Field | Notes                         |
| ------- | ---- | ----- | ----------------------------- |
| `+0x00` | u32  | count | Must equal `petexp.dbss` count |

### Offset Record (10 bytes, repeated `count` times)

| Offset  | Type | Field        | Notes                                                                               |
| ------- | ---- | ------------ | ----------------------------------------------------------------------------------- |
| `+0x00` | u16  | exp_table_id | Matches `key_prefix` and data payload `exp_table_id`                                |
| `+0x02` | u32  | data_offset  | Absolute byte offset in `petexp.dbss` to the data payload, after the 2-byte prefix  |
| `+0x06` | u32  | data_size    | Size of data payload in bytes (observed: 406 for every record)                      |

Offset records are ordered by descending key: 9, 8, 7, 6, 5, 4, 3, 2, 1.

The rows are the same `[u16 id][u32 offset][u32 size]` rows as a PABR offset table, but the file has no `PABR` magic and no 12-byte trailer (94 bytes = 4 + 9 x 10). The parser reads it with `parse_bare_offset_rows` from `_common/pabr_offset.py`.

## Notes

- `pet.dbss` selects the table with `exp_key` (header `+0x0F`, the `Pet_Table` sheet's `RequireEXPType`): keys 1 to 4 for pets, 6 to 9 for Laila. Its `max_level` matches the table's `max_level` on every record.
- Tables 6 to 9 are the fairy curves: 6 Faint, 7 Glimmering, 8 Brilliant, 9 Radiant, matching the grade level caps 10, 20, 30 and 50 in [fairyskillchange.dbss](fairyskillchange_dbss.md). The Ornette's Dark Honey Wine tooltip confirms the split: its `13,300` EXP from [fairyfeedingitem.dbss](fairyfeedingitem_dbss.md) lands on Lv. 5 98.84% on tables 6, 7 and 9 (the tooltip's Faint, Glimmering and Radiant line) and on Lv. 6 58.36% on table 8 (its Brilliant line).
- Records are fixed-capacity, not variable length. `petexpoffset.dbss` still stores offsets and sizes, following the same keyed-index pattern as other DBSS companions.
- The first bytes after the main count (`09 00`) are the first record key prefix, so the apparent 6-byte header should be treated as u32 count plus record 0 prefix.
