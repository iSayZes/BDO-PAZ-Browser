# `fairyfeedenchantfailcount.bss` Format

## Purpose

A small `PABR` lookup table on the fairy feeding/enchant path, keyed by a group
ID from 1 to 7. Each group holds one or two entries carrying a sub-key and two
numeric values. The binary layout is fully resolved; the gameplay meaning of the
values is not confirmed, so field names are deliberately neutral.

Example:

```text
group 1: sub_key 19 -> (0, 200), sub_key 20 -> (0, 300)
group 7: sub_key 0  -> (300, 350)
```

## Graph

### Tags

- file format
- bss
- fairy
- config

### Connections

- [fairyupgraderate.bss](fairyupgraderate_bss.md) — fairy Sprouting success rates, the other fairy enchant-side table
- [fairyequipskill.bss](fairyequipskill_bss.md) — fairy skill catalog rerolled after a successful Sprout
- [fairyskillchange.dbss](fairyskillchange_dbss.md) — fairy skill reroll cost

---

## Companion Files

The format is self-contained — there is no `fairyfeedenchantfailcountoffset.dbss`,
and no companion is needed to parse it.

All multi-byte values are little-endian.

---

## File Layout

| Offset  | Type  | Field   | Notes                                         |
| ------- | ----- | ------- | --------------------------------------------- |
| `+0x00` | u8[4] | magic   | `PABR` (ASCII)                                |
| `+0x04` | u32   | count   | Number of records; observed 7                 |
| `+0x08` | —     | records | `count` variable-length records, back to back |
| end-12  | —     | trailer | 12-byte file trailer                          |

Observed file size is 147 bytes: 8-byte header, 127 bytes of records, 12-byte
trailer.

### Record (4 bytes + `entry_count` × 11)

| Offset  | Type | Field       | Observed | Notes                              |
| ------- | ---- | ----------- | -------- | ---------------------------------- |
| `+0x00` | u32  | entry_count | 1 or 2   | Number of entries that follow      |
| `+0x04` | —    | entries     |          | `entry_count` × 11-byte entries    |

Records have no key of their own. Every entry in a record repeats the same
`group_id`, and that ID equals the record index plus one across all seven
records.

### Entry (11 bytes, repeated `entry_count` times)

| Offset  | Type | Field    | Notes                                              |
| ------- | ---- | -------- | -------------------------------------------------- |
| `+0x00` | u16  | group_id | 1–7; identical for every entry in the same record  |
| `+0x02` | u8   | sub_key  | 19 or 20 in groups 1–2, otherwise 0                |
| `+0x03` | u32  | value_a  | 0 whenever `sub_key` is non-zero                   |
| `+0x07` | u32  | value_b  | 200, 300, or 350                                   |

The 11-byte entry is unaligned — `value_a` starts at an odd offset — so a parser
must read the two u32 fields at `+0x03` and `+0x07` rather than assume 4-byte
alignment.

### Trailer (12 bytes)

The same trailer shape used by [fairyupgraderate.bss](fairyupgraderate_bss.md)
and [zodiacsignindex.bss](zodiacsignindex_bss.md).

| Offset  | Type | Field          | Observed | Notes                                 |
| ------- | ---- | -------------- | -------- | ------------------------------------- |
| `+0x00` | u32  | reserved_a     | 0        | Always zero                           |
| `+0x04` | u32  | end_of_records | 135      | Byte offset just past the last record |
| `+0x08` | u32  | reserved_b     | 0        | Always zero                           |

---

## Decoded Table

All nine entries in the observed file:

| Record | group_id | sub_key | value_a | value_b |
| ------ | -------- | ------- | ------- | ------- |
| 0      | 1        | 19      | 0       | 200     |
| 0      | 1        | 20      | 0       | 300     |
| 1      | 2        | 19      | 0       | 200     |
| 1      | 2        | 20      | 0       | 300     |
| 2      | 3        | 0       | 100     | 300     |
| 3      | 4        | 0       | 100     | 300     |
| 4      | 5        | 0       | 100     | 300     |
| 5      | 6        | 0       | 100     | 300     |
| 6      | 7        | 0       | 300     | 350     |

The table splits cleanly in two. Groups 1–2 carry two entries each, keyed by
`sub_key` 19 and 20, with `value_a` zero. Groups 3–7 carry one entry with
`sub_key` zero and a non-zero `value_a`.

---

## Suggested UI Layout

| Column   | Type | Notes                                   |
| -------- | ---- | --------------------------------------- |
| Group ID | num  | `group_id`                              |
| Sub Key  | num  | `sub_key`; `—` when zero                |
| Value A  | num  | `value_a`                               |
| Value B  | num  | `value_b`                               |

---

## Notes

- The record stream lands exactly on `end_of_records`: `7 × 4 + 9 × 11 = 127`
  bytes of records after the 8-byte header. That exact fit is what confirms the
  4-byte `entry_count` prefix and the 11-byte entry size.
- Records are variable length, so a parser must follow `entry_count` rather than
  assume the 15-byte or 26-byte sizes seen in this file.
- `group_id` is redundant with the record index in the observed data, but it is
  stored per entry rather than per record, so it is read from the entry.
- The filename suggests this sits on the fairy feeding and enchant path, which
  is the same system documented in `fairyupgraderate.bss`. Nothing in this file
  or in `languagedata_en.loc` confirms that link, so it is not asserted here.
- No LOC lookup applies: every field is a small integer, and none of the values
  match a localization key.
- A community fairy guide covering growth, Sprouting, skill changes, rebirth, and
  the Laila's Petal exchange describes no failure-count mechanic and lists no
  value of 100, 200, 300, or 350 on any of those paths. Player-facing
  documentation is therefore unlikely to resolve this file.

---

## Open Questions

### Value Semantics

`value_a` and `value_b` are unidentified. The filename points at a failure
counter, and the pairs read plausibly as bounds (`0..200`, `100..300`,
`300..350`), but nothing in the file confirms that they are a range rather than
two independent settings such as a threshold and a cap.

A Sprouting failure counter is the reading the filename invites, and it is the
one the game rules argue against: a fairy gets a single Sprout attempt, and
failing it ends that fairy's tier-up permanently short of a cash-shop Rebirth.
There is no repeated attempt for a counter reaching 100 or 350 to accumulate
over. That points the `enchant` in the filename at the feeding and growth path
instead, or at a counter kept across fairies rather than within one.

### `group_id` Meaning

`group_id` runs 1–7. It is not the four fairy grades and not the three Sprouting
steps, so it indexes something else on the feeding path. A file that keys the
same 1–7 range would identify it.

### `sub_key` 19 and 20

Only groups 1 and 2 split into two entries, distinguished by `sub_key` 19 and
20, and only those entries have `value_a` of zero. The values are too small to
be item IDs and do not match the fairy-growth item IDs used by
`fairyupgraderate.bss`. Fairy levels are the strongest candidate, since the tier
level caps are 10, 20, 30, and 50, putting 19 and 20 exactly at the Glimmering
cap boundary — but no file read so far keys anything by level 19 or 20, so this
stays unconfirmed.
