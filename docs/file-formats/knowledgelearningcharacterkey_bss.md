# `knowledgelearningcharacterkey.bss` Format

## Purpose

Lists, for each knowledge card that a character teaches, every character that teaches it. It is the reverse of `knowledgelearning.dbss` table 0 (character → card), grouped by card: same pairs, no extra data.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes  | Records          | Row bytes               |
| ------ | -------------- | ------- | ----------------------------------- | ------ | ---------------- | ----------------------- |
| 1      | 3473 and later | 3473    | `knowledgelearningcharacterkey.bss` | 16,860 | 1,458 Card Entry | 10 to 70, 12 on average |

| Layout | File                                | Known             | Unknown    |
| ------ | ----------------------------------- | ----------------- | ---------- |
| 1      | `knowledgelearningcharacterkey.bss` | 16,860 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                              |
| ------------------------ | -------- | ----------------------------------------------------------------- |
| `knowledgelearning.dbss` | Optional | Table 0 holds the same character → card pairs, one row per character |
| `mentalcard.dbss`        | Optional | Card details; `card_id` is its key                                |

All multi-byte values are little-endian.

## Layout 1

### File Layout

Plain binary: no `PABR` magic, no index file and no trailer. The file ends exactly after the last entry.

| Offset  | Type              | Field   | Notes                                  |
| ------- | ----------------- | ------- | -------------------------------------- |
| `+0x00` | u32               | count   | Number of cards; `1458` on client 3458 |
| `+0x04` | Card Entry[count] | entries | See Card Entry                         |

### Card Entry (variable: 8 bytes + character IDs)

| Offset  | Type                 | Field           | Notes                                                       |
| ------- | -------------------- | --------------- | ----------------------------------------------------------- |
| `+0x00` | u32                  | character_count | Characters that teach this card; `1` to `31` observed       |
| `+0x04` | u32                  | card_id         | Knowledge card; LOC `str_type=34`, key of `mentalcard.dbss` |
| `+0x08` | u16[character_count] | character_ids   | Character IDs; LOC `str_type=6`, keys of `characterstatic.dbss` |

## Confirmed Examples

| card_id | Card name (LOC)          | character_ids                     | Character names (LOC)                |
| ------- | ------------------------ | --------------------------------- | ------------------------------------ |
| `4686`  | Khuruto Chaser           | `20665`                           | Khuruto Chaser                       |
| `4174`  | Demibeast Bandit Warrior | `24444`, `20170`                  | Demibeast Bandit Warrior (both)      |
| `4750`  | Lightning Trumpeter      | `20733`                           | Lightning Trumpeter                  |
| `7364`  | Wild Herb                | `10263`, `10273`, ... (31 IDs)    | Wild Herb                            |

## Notes

- Checked against `knowledgelearning.dbss` on client 3458: the 1,458 cards are exactly the distinct `card_id` values of table 0, the 2,596 character IDs are exactly its `source_id` values, and every card lists its characters in table 0 row order. No character appears twice.
- Character IDs are u16 here and u32 in `knowledgelearning.dbss`; the largest observed is `35405`.
- `card_id` is unique, but the entries are not sorted by it and do not follow table 0's order. The order looks like a hash map dump and carries no meaning found so far.
- There is no item counterpart: no `knowledgelearningitemkey` file exists for table 1.
- The app does not read this file for the `mentalcard.dbss` Learned From column; it builds the same links from `knowledgelearning.dbss` (`KNOWLEDGE_LEARNING_CHARACTERS`), which also holds the item sources.
