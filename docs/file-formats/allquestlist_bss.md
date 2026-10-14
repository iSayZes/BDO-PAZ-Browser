# `allquestlist.bss` Format

## Purpose

Quest order list. The file is a compact `PABR` table of packed quest IDs, one per `quest.dbss` record and in the same physical order as the records in `quest.dbss`. The IDs line up with LOC quest title keys and use the packed ID scheme of `quest.dbss`.

Example:

```text
slot 0 -> packed_quest_id 795132 -> chain 8700, quest 12 -> quest.dbss record 0
slot 1 -> packed_quest_id 138172 -> chain 7100, quest 2  -> quest.dbss record 1
slot 2 -> packed_quest_id 196891 -> chain 283, quest 3   -> quest.dbss record 2
```

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `quest.dbss`          | Optional | Quest records, stored in the same order as this list                 |
| `acceptquest.bss`     | Optional | The NPC dialog that gives each quest of this list                     |
| `completequest.bss`   | Optional | The NPC dialog that takes each quest of this list                     |
| `mainquest.bss`       | Optional | Provides main-quest UI sequence groups for a subset of quest IDs      |
| `newquest.bss`        | Optional | Provides new-quest UI sequence groups for a subset of quest IDs       |
| `languagedata_en.loc` | Optional | Provides quest title/objective text for display via LOC type `18`    |

All multi-byte values are little-endian.

## File Layout

### Header (8 bytes)

| Offset  | Type  | Field | Notes                                           |
| ------- | ----- | ----- | ----------------------------------------------- |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)                                  |
| `+0x04` | u32   | count | Number of entries; `19,327` after the 2026-09-27 client update, `18,988` before it, `19,599` fixture |

### Entry (4 bytes, repeated `count` times)

| Offset  | Type | Field           | Notes                                                     |
| ------- | ---- | --------------- | --------------------------------------------------------- |
| `+0x00` | u32  | packed_quest_id | Packed as `(quest_id << 16) \| quest_chain_id`            |

### Trailer (12 bytes)

Follows the last entry.

| Offset  | Type | Field          | Notes                                                              |
| ------- | ---- | -------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | reserved_a     | Observed `0`                                                       |
| `+0x04` | u32  | end_of_entries | Byte offset immediately after entries, `8 + count × 4`             |
| `+0x08` | u32  | reserved_b     | Observed `0`                                                       |

## Record Structure

### Quest List Entry (4 bytes)

| Offset  | Type | Field           | Notes                                          |
| ------- | ---- | --------------- | ---------------------------------------------- |
| `+0x00` | u32  | packed_quest_id | Split into `quest_chain_id` and `quest_id`     |

Derived fields:

```text
quest_chain_id = packed_quest_id & 0xFFFF
quest_id       = packed_quest_id >> 16
```

## Reference Rows

Current client data (`files/allquestlist.bss`):

| Slot  | Packed Quest ID | Chain ID | Quest ID | LOC Title (type 18, `id4=0`)                                     |
| ----- | --------------- | -------- | -------- | ---------------------------------------------------------------- |
| 0     | `795132`        | `8700`   | `12`     | `[Storybook] Tale of the Mudang Wraith`                          |
| 1     | `138172`        | `7100`   | `2`      | `[Processing] The Beauty of Planks`                              |
| 2     | `196891`        | `283`    | `3`      | `Exalted Character III`                                          |
| 18987 | `181218`        | `50146`  | `2`      | `A Whole New Experience Presented by Fughar! (Black Spirit Pass)` |

The older fixture starts with `1050655` (chain `2079`, quest `16`, `[Elvia Weekly] Gigagord`) and also ends with `181218`.

## Suggested UI Layout

| Column  | Type | Notes                                                                 |
| ------- | ---- | --------------------------------------------------------------------- |
| Main ID | num  | `packed_quest_id & 0xFFFF`; LOC type 18 `str_id1`                     |
| Sub ID  | num  | `packed_quest_id >> 16`; LOC type 18 `str_id2`                        |
| Icon    | text | Quest icon resolved from `packed_quest_id` through the quest icon index |
| Title   | text | Prefer LOC type 18 row with matching main/sub ID and `str_id4=0`, in its game colours |

## Notes

- Current file: `75,972` bytes, `18,988` entries, `end_of_entries = 75,960`. After the 2026-09-27 update: `77,328` bytes, `19,327` entries, `end_of_entries = 77,316`. Fixture: `78,416` bytes, `19,599` entries, `end_of_entries = 78,404` (`0x13244`). All three match `8 + count × 4 + 12`.
- `count` equals the `quest.dbss` header count in all three versions, and all entries are distinct.
- Physical order: walking `quest.dbss` sequentially, record `i` carries packed quest ID `entry[i]` at the start of its fixed block (after its objective text) and again in its trailing echo. The walk succeeds for all `18,988` current, `19,327` updated and `19,599` fixture records, so this list is the record-order index for `quest.dbss` (as stated by [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)). See [quest_dbss.md](quest_dbss.md) for the record layout.
- The list is not a byte offset table; it stores IDs only, so record offsets still have to be found by walking `quest.dbss`.
- The entry encoding matches the packed quest ID relationship documented in `questgroup.dbss`.
- [`growthpassquestlist.bss`](growthpassquestlist_bss.md) and the three [Black Spirit Pass lists](seasonpassquestlist_bss.md) use this layout and handler.
- All 827 adventure-journal page quests from `journalquest.dbss` are in the current list.
- LOC coverage: `18,961` of `18,988` current entries (fixture: `19,455` of `19,599`) have a LOC type `18`, `str_id4=0` title row keyed by `(quest_chain_id, quest_id)`.
