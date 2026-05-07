# `allquestlist.bss` Format

## Purpose

Quest lookup list. The file is a compact `PABR` table of canonical/display packed quest identifiers that line up with LOC quest title keys and share the same packed ID scheme used by `quest.dbss`.

Example:

```text
slot 0 -> packed_quest_id 1050655 -> chain 2079, quest 16
slot 1 -> packed_quest_id 463223 -> chain 4471, quest 7
slot 2 -> packed_quest_id 6751209 -> chain 1001, quest 103
```

## Graph

### Tags

- file format
- bss
- quest
- index

### Connections

- [quest.dbss](quest_dbss.md) - quest definition table with the same declared count and packed quest ID form; current parser extracts `canonical_link` IDs that resolve strongly into this list
- [questgroup.dbss](questgroup_dbss.md) - confirms packed quest IDs are `(quest_id << 16) | quest_chain_id`
- [languagedata_en.loc](languagedata_loc.md) - English quest text keyed by LOC type 18 with `str_id1=quest_chain_id` and `str_id2=quest_id`

---

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `quest.dbss`          | Optional | Provides quest record payloads that use the same packed ID scheme    |
| `languagedata_en.loc` | Optional | Provides quest title/objective text for display via LOC type `18`    |

All multi-byte values are little-endian.

---

## File Layout

### Header (8 bytes)

| Offset  | Type  | Field | Notes                                           |
| ------- | ----- | ----- | ----------------------------------------------- |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)                                  |
| `+0x04` | u32   | count | Number of entries; observed `19599`             |

### Entry (4 bytes, repeated `count` times)

| Offset  | Type | Field           | Notes                                                     |
| ------- | ---- | --------------- | --------------------------------------------------------- |
| `+0x00` | u32  | packed_quest_id | Packed as `(quest_id << 16) \| quest_chain_id`            |

### Trailer (12 bytes)

Follows the last entry.

| Offset  | Type | Field          | Notes                                                              |
| ------- | ---- | -------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | reserved_a     | Observed `0`                                                       |
| `+0x04` | u32  | end_of_entries | Byte offset immediately after entries; observed `0x13244`          |
| `+0x08` | u32  | reserved_b     | Observed `0`                                                       |

---

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

---

## Reference Rows

| Slot | Packed Quest ID | Chain ID | Quest ID | Example LOC Title                         |
| ---- | --------------- | -------- | -------- | ----------------------------------------- |
| 0    | `1050655`       | `2079`   | `16`     | `[Elvia Weekly] Gigagord`                 |
| 1    | `463223`        | `4471`   | `7`      | LOC type 18 title when available          |
| 2    | `6751209`       | `1001`   | `103`    | LOC type 18 title when available          |
| 19598 | `181218`       | `50146`  | `2`      | LOC type 18 title when available          |

---

## Suggested UI Layout

| Column  | Type | Notes                                                                 |
| ------- | ---- | --------------------------------------------------------------------- |
| Main ID | num  | `packed_quest_id & 0xFFFF`; LOC type 18 `str_id1`                     |
| Sub ID  | num  | `packed_quest_id >> 16`; LOC type 18 `str_id2`                        |
| Title   | text | Prefer LOC type 18 row with matching main/sub ID and `str_id4=0`      |

---

## Notes

- Observed decompressed size is `78,416` bytes.
- File size matches `8 + (19599 * 4) + 12`.
- Trailer `end_of_entries` is `78,404` decimal (`0x13244`), equal to `8 + count * 4`.
- `count` matches the observed `quest.dbss` record count documented for the same client data.
- The entry encoding matches the packed quest ID relationship documented in `questgroup.dbss`.
- The list is not a byte offset table. It is a canonical display ID list: current `quest.dbss` parsing extracts `16,977` non-zero `canonical_link` IDs, with `16,976` present in this file.
- In the observed LOC cache, `19,455` of `19,599` entries have a matching LOC type `18`, `str_id4=0` title row keyed by `(quest_chain_id, quest_id)`.
