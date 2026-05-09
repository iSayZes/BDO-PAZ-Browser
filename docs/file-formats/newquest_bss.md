# `newquest.bss` Format

## Purpose

Defines "new quest" / quest-notice UI sequence data. The decoded first section groups quest IDs into 224 blocks and stores 1,255 quest reference rows. A later payload contains UTF-16-LE Korean text, PA markup, and date strings used by the same UI surface.

Example:

```text
group 0 -> quest 11059 / 9 -> [Event] Love for Pets
group 4 -> quest 6809 / 1 -> LOC type 18 title when available
```

## Graph

### Tags

- file format
- bss
- quest
- new quest
- ui
- index

### Connections

- [allquestlist.bss](allquestlist_bss.md) - decoded quest references use the same packed quest ID scheme
- [mainquest.bss](mainquest_bss.md) - same 17-byte quest reference row shape, but different group count and UI purpose
- [quest.dbss](quest_dbss.md) - quest definitions and LOC mapping use the same `(quest_id << 16) | quest_chain_id` packed ID scheme
- [languagedata_en.loc](languagedata_loc.md) - English quest text keyed by LOC type 18 with `str_id1=quest_chain_id` and `str_id2=quest_id`

---

## File Layout

All multi-byte values are little-endian unless noted otherwise.

### Header (8 bytes)

| Offset  | Type    | Field       | Notes                                      |
| ------- | ------- | ----------- | ------------------------------------------ |
| `+0x00` | char[4] | magic       | `PABR` (ASCII)                             |
| `+0x04` | u32     | group_count | Number of decoded quest groups; observed `224` |

### Quest Group Stream

Starts at `+0x08` and runs through file offset `0x00006771` in the observed data. It contains 224 groups and 1,255 quest reference rows.

The first group uses a shorter 10-byte header. Groups 1 through 223 use a 23-byte header immediately before their quest reference rows. Header fields are only partially decoded.

#### First Group Header (10 bytes)

| Offset  | Type | Field           | Observed | Notes                    |
| ------- | ---- | --------------- | -------- | ------------------------ |
| `+0x00` | u32  | group_key       | `1`      | Meaning not confirmed    |
| `+0x04` | u8[3] | padding        | `00 00 00` | Observed zero          |
| `+0x07` | u8   | quest_ref_count | `2`      | Number of following rows |
| `+0x08` | u16  | padding         | `0`      | Observed zero            |

#### Later Group Header (23 bytes)

| Offset  | Type | Field           | Observed / Notes                            |
| ------- | ---- | --------------- | ------------------------------------------- |
| `+0x00` | u8   | header_flag     | Observed `0` in sampled headers             |
| `+0x01` | u32  | unknown_a       | Group/sequence value; meaning unknown       |
| `+0x05` | u32  | unknown_b       | Group/sequence value; meaning unknown       |
| `+0x09` | u32  | unknown_c       | Observed `0` in sampled headers             |
| `+0x0D` | u16  | group_key_a     | Group key / sequence value; meaning unknown |
| `+0x0F` | u32  | group_key_b     | Group key / sequence value; meaning unknown |
| `+0x13` | u8   | unknown_d       | Small flag or category byte; meaning unknown |
| `+0x14` | u16  | quest_ref_count | Number of following rows                    |
| `+0x16` | u8   | padding         | Observed zero in sampled headers            |

### Quest Reference Row (17 bytes, repeated `quest_ref_count` times)

| Offset  | Type | Field          | Notes                                                                   |
| ------- | ---- | -------------- | ----------------------------------------------------------------------- |
| `+0x00` | u8   | flags          | Observed `0` in all decoded rows                                        |
| `+0x01` | u16  | quest_chain_id | LOC type 18 `str_id1`; combines with `quest_id` to form quest key       |
| `+0x03` | u16  | quest_id       | LOC type 18 `str_id2`; combines with `quest_chain_id` to form quest key |
| `+0x05` | u32  | sequence_a     | Observed range `1..1795`; likely ordering/index data                    |
| `+0x09` | u32  | sequence_b     | Commonly `2`; other small sequence values appear                        |
| `+0x0D` | u32  | sequence_c     | Observed range `2..1788`; likely parent/next/index data                 |

Derived packed quest ID:

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

### Text / Markup Payload

Starts immediately after the decoded quest reference stream at file offset `0x00006772`. The payload contains UTF-16-LE Korean text, PA markup, and date/time strings such as `2018-10-3 10:00` and `2026-05-28 07:00`.

The first payload bytes resemble another small header followed by UTF-16 text, but record lengths and relationships to quest groups are not fully confirmed.

---

## Reference Rows

| Group | Row | flags | Quest Chain ID | Quest ID | sequence_a | sequence_b | sequence_c | Example LOC Title |
| ----: | --: | ----: | -------------: | -------: | ---------: | ---------: | ---------: | ----------------- |
| 0     | 0   | `0`   | `11059`        | `9`      | `1`        | `2`        | `2`        | `[Event] Love for Pets` |
| 0     | 1   | `0`   | `11059`        | `10`     | `1`        | `2`        | `2`        | `[Event] Savory Good Feed` |
| 1     | 0   | `0`   | `2035`         | `6`      | `6`        | `2`        | `7`        | LOC type 18 title when available |
| 4     | 0   | `0`   | `6809`         | `1`      | `30`       | `2`        | `2`        | LOC type 18 title when available |
| 223   | 0   | `0`   | `11593`        | `1`      | `899`      | `2`        | `2`        | LOC type 18 title when available |

---

## Suggested UI Layout

| Column       | Type | Notes                                                            |
| ------------ | ---- | ---------------------------------------------------------------- |
| Group        | num  | Decoded group index `0..223`                                     |
| Main ID      | num  | `quest_chain_id`; LOC type 18 `str_id1`                          |
| Sub ID       | num  | `quest_id`; LOC type 18 `str_id2`                                |
| Title        | text | Prefer LOC type 18 row with matching main/sub ID and `str_id4=0` |
| Sequence A   | num  | Raw `sequence_a`                                                 |
| Sequence B   | num  | Raw `sequence_b`                                                 |
| Sequence C   | num  | Raw `sequence_c`                                                 |

---

## Notes

- Observed decompressed size is `816,761` bytes.
- The decoded quest reference stream contains 224 groups and 1,255 rows.
- The 1,255 decoded rows contain 1,226 unique quest IDs; 29 quest IDs appear twice.
- Decoded quest reference rows use the same 17-byte shape as `mainquest.bss`.
- The decoded quest reference stream ends at offset `0x00006772`; the rest of the file is mostly UTF-16-LE text/markup payload.

---

## Open Questions

### Group Header Fields

The meaning of `group_key`, `group_key_a`, `group_key_b`, `unknown_*`, and `header_flag` fields is not confirmed.

### Sequence Fields

`sequence_a`, `sequence_b`, and `sequence_c` look like order, parent, or link indexes, but their exact UI behavior is not confirmed.

### Duplicate Quest References

29 packed quest IDs appear twice in the decoded quest reference stream. Their UI reason is not confirmed.

### Text Payload Boundaries

The UTF-16 text/markup section after `0x00006772` is confirmed as text payload, but its record lengths and mapping back to quest groups still need decoding.
