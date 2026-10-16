# `knowledgelearning.dbss` Format

## Purpose

Defines how knowledge entries are obtained from characters and items. The file holds two tables: table 0 maps a character ID (a monster, NPC, gathering node or other `characterstatic.dbss` entry) to the knowledge card it teaches, and table 1 maps an item ID to the card it teaches. Parsing is driven by `knowledgelearningoffset.dbss`, which gives each record's source ID, byte offset and size.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                        |
| ------------------------------ | -------- | ----------------------------------------------------------- |
| `knowledgelearningoffset.dbss` | Required | Provides source ID, byte offset and size for each record    |
| `knowledgelearningcharacterkey.bss` | Optional | Table 0 grouped by card: each card with the characters that teach it ([doc](knowledgelearningcharacterkey_bss.md)) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The two tables follow each other; the file holds no table count of its own.

| Offset  | Type              | Field  | Notes                                                   |
| ------- | ----------------- | ------ | ------------------------------------------------------- |
| `+0x00` | Learning Table[2] | tables | Table 0 (characters), then table 1 (items); the offset file's `table_count` is `2` |

The index `data_offset` points past the lead, at the record itself. Table 0 starts at `0` and its records end at `44136` (`43065` in the pre-2026-09-27 fixture); table 1 starts there with its own count.

### Learning Table (variable: 4 bytes + entries)

| Offset  | Type                  | Field   | Notes                             |
| ------- | --------------------- | ------- | --------------------------------- |
| `+0x00` | u32                   | count   | Matches the index table's `count` |
| `+0x04` | Learning Entry[count] | entries | See Learning Entry                |

### Learning Entry (17 bytes)

| Offset  | Type            | Field      | Notes                                                          |
| ------- | --------------- | ---------- | -------------------------------------------------------------- |
| `+0x00` | u32             | key_prefix | Lead `source_id`, equal to the record's `source_id`            |
| `+0x04` | Learning Record | record     | See Learning Record; the index `data_offset` points here       |

### Learning Record (13 bytes)

| Offset  | Type | Field       | Notes                                                                  |
| ------- | ---- | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | source_id   | Character ID (table 0, LOC `str_type=6`) or item ID (table 1, LOC `str_type=0`) |
| `+0x04` | u32  | source_type | `0` in table 0, `1` in table 1                                         |
| `+0x08` | u8   | unknown_08  | Always `0`                                                             |
| `+0x09` | u32  | card_id     | Knowledge card taught; LOC `str_type=34`, key of `mentalcard.dbss`     |

### `knowledgelearningoffset.dbss`

No `PABR` magic and no trailer; the file ends exactly after the last table.

| Offset  | Type                     | Field       | Notes                                    |
| ------- | ------------------------ | ----------- | ---------------------------------------- |
| `+0x00` | u32                      | table_count | Observed `2`                             |
| `+0x04` | Index Table[table_count] | tables      | See Index Table                          |

### Index Table (variable: 4 bytes + rows)

| Offset  | Type             | Field | Notes                                         |
| ------- | ---------------- | ----- | --------------------------------------------- |
| `+0x00` | u32              | count | Rows in this table: `2596` and `2088` in the 2026-09-27 client, `2533` and `2070` in the pre-2026-09-27 fixture |
| `+0x04` | Index Row[count] | rows  | See Index Row                                 |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | source_id   | Equals `source_id` at the start of the record            |
| `+0x04` | u32  | data_offset | Absolute offset of the record in `knowledgelearning.dbss` |
| `+0x08` | u32  | size        | Record size in bytes; always `13`                        |

## Enum Values

### `source_type`

| Value | Meaning   | Rows  | Evidence                                                        |
| ----- | --------- | ----- | --------------------------------------------------------------- |
| 0     | Character | 2,596 | All 2,596 `source_id` values have an LOC `str_type=6` name      |
| 1     | Item      | 2,088 | All 2,088 `source_id` values have an LOC `str_type=0` name      |

## Confirmed Examples

| Table | source_id | Source name (LOC)       | card_id | Card name (LOC)          |
| ----- | --------- | ----------------------- | ------- | ------------------------ |
| 0     | `10004`   | Feldspar (str_type=6)   | `7302`  | Feldspar                 |
| 0     | `21207`   | Valencian Lion          | `4893`  | Valencian Lion           |
| 0     | `10480`   | Pistachio Tree          | `7836`  | Pistachio                |
| 1     | `8279`    | Gurnard (str_type=0)    | `8579`  | Gurnard                  |
| 1     | `9728`    | Blue Whale Molar        | `7765`  | Blue Whale Tooth         |

## Notes

- Every `card_id` in both tables is a `mentalcard.dbss` card.
- The app groups table 0 by card into the `KNOWLEDGE_LEARNING_CHARACTERS` lookup index and table 1 into `KNOWLEDGE_LEARNING_ITEMS`. The `mentalcard.dbss` Learned From and Learned From Items columns read them.
- The source name equals the card name on 2,504 of 2,596 character rows and 2,003 of 2,088 item rows. The rest are close variants (`Pistachio Tree` teaches `Pistachio`, several Magic Crystals teach `Low Grade Crystal Fusion`).
- Table 0 teaches 1,458 distinct cards, so several characters can teach one card (for example boss variants). Table 1 teaches 2,045 distinct cards.
- `source_id` is unique within each table. Read it with the right LOC type: in table 0, `10004` is the character Feldspar, while item `10004` is `Raell Longsword`.
- The earlier reading of this file skipped a 12-byte header and read rows as `offset, kind, idx_id`. That shifts every row by one field: `kind` was the record size (`13`) and `idx_id` was the next row's `source_id`. It also misreads table 1, whose rows start 4 bytes after table 0's last row.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) describes `knowledgelearning` as card-to-card learning prerequisites. Our files do not support that: `source_id` resolves as a character or item on every row, and only 272 of 2,596 character IDs are also card IDs.
- `knowledgelearningcharacterkey.bss` holds the same pairs as table 0, grouped by card in table 0 row order; see [its doc](knowledgelearningcharacterkey_bss.md). Table 1 has no such file.

## Open Questions

### Other Source Types

Only `source_type` 0 and 1 occur, one per table. It is not known whether the client supports other sources (quests, regions) through a third table.
