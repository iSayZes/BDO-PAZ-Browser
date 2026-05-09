# `completequest.bss` Format

## Purpose

Lists quest IDs in completion-related order with two small per-row side fields. The middle two fields in every row form a quest key that matches `allquestlist.bss` exactly once.

Example:

```text
row 0 -> quest 8500 / 4 -> [LoML] Emma's Invitation
```

## Graph

### Tags

- file format
- bss
- quest
- index

### Connections

- [allquestlist.bss](allquestlist_bss.md) - contains the same 19,599 packed quest IDs, but in canonical/display order
- [acceptquest.bss](acceptquest_bss.md) - same row width and quest key scheme, but acceptance-related order and side fields
- [quest.dbss](quest_dbss.md) - quest definitions and LOC mapping use the same `(quest_id << 16) | quest_chain_id` packed ID scheme
- [languagedata_en.loc](languagedata_loc.md) - English quest text keyed by LOC type 18 with `str_id1=quest_chain_id` and `str_id2=quest_id`

---

## File Layout

All multi-byte values are little-endian.

### Header (8 bytes)

| Offset  | Type    | Field | Notes                             |
| ------- | ------- | ----- | --------------------------------- |
| `+0x00` | char[4] | magic | `PABR` (ASCII)                    |
| `+0x04` | u32     | count | Number of rows; observed `19,599` |

### Row Stream

Rows start immediately after the header at `+0x08`.

| Offset  | Type | Field          | Notes                                                                   |
| ------- | ---- | -------------- | ----------------------------------------------------------------------- |
| `+0x00` | u16  | unknown_a      | Completion-side value; observed range `0..64535`                       |
| `+0x02` | u16  | quest_chain_id | LOC type 18 `str_id1`; combines with `quest_id` to form quest key       |
| `+0x04` | u16  | quest_id       | LOC type 18 `str_id2`; combines with `quest_chain_id` to form quest key |
| `+0x06` | u16  | unknown_b      | Completion-side value; observed range `0..20314`                       |

Derived packed quest ID:

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

### Trailer (12 bytes)

Follows the last row.

| Offset  | Type | Field          | Observed | Notes                                               |
| ------- | ---- | -------------- | -------- | --------------------------------------------------- |
| `+0x00` | u32  | reserved_a     | `0`      | Observed zero                                       |
| `+0x04` | u32  | end_of_rows    | `156800` | Byte offset immediately after rows; `8 + count * 8` |
| `+0x08` | u32  | reserved_b     | `0`      | Observed zero                                       |

---

## Record Structure

### Complete Quest Row (8 bytes, repeated `count` times)

| Offset  | Type | Field          | Notes                     |
| ------- | ---- | -------------- | ------------------------- |
| `+0x00` | u16  | unknown_a      | Not part of the quest key |
| `+0x02` | u16  | quest_chain_id | Main quest key part       |
| `+0x04` | u16  | quest_id       | Sub quest key part        |
| `+0x06` | u16  | unknown_b      | Not part of the quest key |

---

## Reference Rows

| Row | unknown_a | Quest Chain ID | Quest ID | unknown_b | Example LOC Title             |
| --: | --------: | -------------: | -------: | --------: | ----------------------------- |
| 0   | `59875`   | `8500`         | `4`      | `73`      | `[LoML] Emma's Invitation`    |
| 1   | `59875`   | `8500`         | `5`      | `73`      | `[LoML] Time is Cruel`        |
| 3   | `59875`   | `8501`         | `2`      | `1`       | LOC type 18 title when available |
| 11  | `59875`   | `8502`         | `1`      | `8`       | LOC type 18 title when available |

---

## Suggested UI Layout

| Column    | Type | Notes                                                            |
| --------- | ---- | ---------------------------------------------------------------- |
| Main ID   | num  | `quest_chain_id`; LOC type 18 `str_id1`                          |
| Sub ID    | num  | `quest_id`; LOC type 18 `str_id2`                                |
| Title     | text | Prefer LOC type 18 row with matching main/sub ID and `str_id4=0` |
| Unknown A | num  | Raw `unknown_a`                                                  |
| Unknown B | num  | Raw `unknown_b`                                                  |

---

## Notes

- Observed decompressed size is `156,812` bytes.
- File size matches `8 + (19599 * 8) + 12`.
- Trailer `end_of_rows` is `156,800` decimal, equal to `8 + count * 8`.
- The `(quest_chain_id, quest_id)` pair resolves to the same 19,599 packed quest IDs as `allquestlist.bss`. The sets are identical, but row order is almost entirely different from `allquestlist.bss`.
- `completequest.bss` and `acceptquest.bss` have the same size, header, row width, and trailer shape. Both use the middle two `u16` fields as the quest key, but the side fields differ.

---

## Open Questions

### unknown_a and unknown_b

The two side fields are not confirmed. They likely encode completion-related grouping, flags, rewards, routing, or ordering data, but current local evidence only confirms their boundaries and relationship to quest keys.
