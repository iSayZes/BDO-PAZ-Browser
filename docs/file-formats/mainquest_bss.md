# `mainquest.bss` Format

## Purpose

Defines the main-quest UI sequence/index data. The first decoded section groups quest IDs into 112 main-quest chains and stores 3,089 quest references. A later payload contains UTF-16 text/markup used by the main quest UI, but its record boundaries are not fully decoded yet.

Example:

```text
group 0 -> quest 40022 / 1 -> [Special Growth] Birth of a Prestigious Family
group 1 -> quest 285 / 1 -> [Warrior Awakening] New Weapon
```

## Graph

### Tags

- file format
- bss
- quest
- main quest
- ui
- index

### Connections

- [allquestlist.bss](allquestlist_bss.md) - every decoded quest reference is a packed quest ID from the canonical quest list
- [newquest.bss](newquest_bss.md) - same 17-byte quest reference row shape, but different group count and UI purpose
- [quest.dbss](quest_dbss.md) - quest definitions and LOC mapping use the same `(quest_id << 16) | quest_chain_id` packed ID scheme
- [languagedata_en.loc](languagedata_loc.md) - English quest text keyed by LOC type 18 with `str_id1=quest_chain_id` and `str_id2=quest_id`

---

## File Layout

All multi-byte values are little-endian unless noted otherwise.

### Header (8 bytes)

| Offset  | Type    | Field       | Notes                                      |
| ------- | ------- | ----------- | ------------------------------------------ |
| `+0x00` | char[4] | magic       | `PABR` (ASCII)                             |
| `+0x04` | u32     | group_count | Number of decoded quest groups; observed `112` |

### Quest Group Stream

Starts at `+0x08` and runs through file offset `0x0000D72B` in the observed data. It contains 112 groups and 3,089 quest reference rows.

The first group uses a shorter 10-byte header. Groups 1 through 111 use a 22-byte header immediately before their quest reference rows. Header fields are only partially decoded.

#### First Group Header (10 bytes)

| Offset  | Type | Field            | Observed | Notes                    |
| ------- | ---- | ---------------- | -------- | ------------------------ |
| `+0x00` | u32  | group_key        | `104`    | Meaning not confirmed    |
| `+0x04` | u8[3] | padding         | `00 00 00` | Observed zero          |
| `+0x07` | u8   | quest_ref_count  | `14`     | Number of following rows |
| `+0x08` | u16  | padding          | `0`      | Observed zero            |

#### Later Group Header (22 bytes)

| Offset  | Type | Field            | Observed / Notes                           |
| ------- | ---- | ---------------- | ------------------------------------------ |
| `+0x00` | u32  | unknown_a        | Commonly `2`                               |
| `+0x04` | u32  | unknown_b        | Commonly `2`                               |
| `+0x08` | u32  | unknown_c        | Observed `0` in sampled headers            |
| `+0x0C` | u16  | group_key_a      | Group key / sequence value; meaning unknown |
| `+0x0E` | u32  | group_key_b      | Group key / sequence value; meaning unknown |
| `+0x12` | u16  | quest_ref_count  | Number of following rows                   |
| `+0x14` | u16  | padding          | Observed `0` in sampled headers            |

### Quest Reference Row (17 bytes, repeated `quest_ref_count` times)

| Offset  | Type | Field          | Notes                                                                 |
| ------- | ---- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u8   | flags          | Observed `0` for 3,082 rows and `1` for 7 rows                        |
| `+0x01` | u16  | quest_chain_id | LOC type 18 `str_id1`; combines with `quest_id` to form quest key     |
| `+0x03` | u16  | quest_id       | LOC type 18 `str_id2`; combines with `quest_chain_id` to form quest key |
| `+0x05` | u32  | sequence_a     | Observed range `1..3341`; likely ordering/index data                  |
| `+0x09` | u32  | sequence_b     | Commonly `2`; other values appear in later groups                     |
| `+0x0D` | u32  | sequence_c     | Observed range `2..3337`; likely parent/next/index data               |

Derived packed quest ID:

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

### Text / Markup Payload

Starts immediately after the decoded quest reference stream at file offset `0x0000D72C`. The payload contains UTF-16-LE Korean text and PA markup such as `<PAColor0xFFf3d900>` and `<PAOldColor>`.

The first payload bytes resemble another small header followed by UTF-16 text, but record lengths and relationships to the 112 quest groups are not fully confirmed.

---

## Reference Rows

| Group | Row | flags | Quest Chain ID | Quest ID | sequence_a | sequence_b | sequence_c | Example LOC Title |
| ----: | --: | ----: | -------------: | -------: | ---------: | ---------: | ---------: | ----------------- |
| 0     | 0   | `0`   | `40022`        | `1`      | `1`        | `2`        | `3`        | `[Special Growth] Birth of a Prestigious Family` |
| 0     | 13  | `0`   | `40022`        | `14`     | `17`       | `2`        | `5`        | `[Special Growth] Fughar's Memorandum - Chapter 11` |
| 1     | 0   | `0`   | `285`          | `1`      | `19`       | `2`        | `20`       | `[Warrior Awakening] New Weapon` |
| 111   | 0   | `0`   | `9107`         | `1`      | `3335`     | `2`        | `3337`     | `[Edania] King of Edana` |

---

## Suggested UI Layout

| Column       | Type | Notes                                                            |
| ------------ | ---- | ---------------------------------------------------------------- |
| Group        | num  | Decoded group index `0..111`                                     |
| Main ID      | num  | `quest_chain_id`; LOC type 18 `str_id1`                          |
| Sub ID       | num  | `quest_id`; LOC type 18 `str_id2`                                |
| Title        | text | Prefer LOC type 18 row with matching main/sub ID and `str_id4=0` |
| Flags        | num  | Raw `flags` byte                                                 |
| Sequence A   | num  | Raw `sequence_a`                                                 |
| Sequence B   | num  | Raw `sequence_b`                                                 |
| Sequence C   | num  | Raw `sequence_c`                                                 |

---

## Notes

- Observed decompressed size is `448,907` bytes.
- The decoded quest reference stream contains 112 groups and 3,089 unique quest IDs.
- All 3,089 decoded quest IDs exist in `allquestlist.bss`.
- Quest reference rows are fixed-width 17-byte records, but group headers are variable or special-cased: the first group has a shorter header than later groups.
- The decoded quest reference stream ends at offset `0x0000D72C`; the rest of the file is mostly UTF-16-LE text/markup payload.

---

## Open Questions

### Group Header Fields

The meaning of `group_key`, `group_key_a`, `group_key_b`, and the three `unknown_*` header fields is not confirmed.

### Sequence Fields

`sequence_a`, `sequence_b`, and `sequence_c` look like order, parent, or link indexes, but their exact UI behavior is not confirmed.

### Text Payload Boundaries

The UTF-16 text/markup section after `0x0000D72C` is confirmed as text payload, but its record lengths and mapping back to quest groups still need decoding.
