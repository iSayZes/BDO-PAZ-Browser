# `fairyfeedenchantfailcount.bss` Format

## Purpose

A small `PABR` lookup table on the fairy feeding/enchant path. Each record
holds one or two 11-byte entries of four integer fields. The binary layout is
fully resolved; the meaning of every entry field is not confirmed, so all four
are named by their offset (`unknown_00`, `unknown_02`, `unknown_03`,
`unknown_07`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | ----------------- | --------- |
| 1      | 3473 and later | 3474    | `fairyfeedenchantfailcount.bss` | 147   | 9 Entry, 7 Record | 11        |

| Layout | File                            | Known        | Unknown      |
| ------ | ------------------------------- | ------------ | ------------ |
| 1      | `fairyfeedenchantfailcount.bss` | 48 B (32.7%) | 99 B (67.3%) |

<!-- versions:end -->

## Companion Files

The format is self-contained: there is no `fairyfeedenchantfailcountoffset.dbss`,
and no companion is needed to parse it.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type          | Field          | Notes                                        |
| ------------------- | ------------- | -------------- | -------------------------------------------- |
| `+0x00`             | char[4]       | magic          | `PABR` (ASCII)                               |
| `+0x04`             | u32           | count          | Number of records; observed 7 (see Notes)    |
| `+0x08`             | Record[count] | records        | Variable-length records, back to back        |
| `records+0x00`      | String Table  | string_table   | The PABR string table, here with no strings  |
| `string_table+0x00` | u32           | end_of_records | Byte offset just past the last record; observed 135 |
| `string_table+0x04` | u32           | zero           | Always `0`                                   |

Observed file size is 147 bytes: 8-byte header, 127 bytes of records, 12-byte
trailer.

The 12-byte trailer (`string_table`, `end_of_records`, `zero`) is the same
trailer shape used by [fairyupgraderate.bss](fairyupgraderate_bss.md) and
[zodiacsignindex.bss](zodiacsignindex_bss.md).

### Record (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Observed | Notes                              |
| ------- | ------------------ | ----------- | -------- | ---------------------------------- |
| `+0x00` | u32                | entry_count | 1 or 2   | Number of entries that follow      |
| `+0x04` | Entry[entry_count] | entries     |          | `entry_count` × 11-byte entries    |

Records have no key of their own. Every entry in a record repeats the same
`unknown_00`, and that value equals the record index plus one across all seven
records.

### Entry (11 bytes)

| Offset  | Type | Field      | Notes                                                   |
| ------- | ---- | ---------- | ------------------------------------------------------- |
| `+0x00` | u16  | unknown_00 | 1–7; identical for every entry in the same record       |
| `+0x02` | u8   | unknown_02 | 19 or 20 where `unknown_00` is 1–2, otherwise 0         |
| `+0x03` | u32  | unknown_03 | 0 whenever `unknown_02` is non-zero                     |
| `+0x07` | u32  | unknown_07 | 200, 300, or 350                                        |

Earlier versions of this doc called `unknown_00` `group_id`, `unknown_02`
`sub_key`, `unknown_03` `value_a` and `unknown_07` `value_b`.

The 11-byte entry is unaligned: `unknown_03` starts at an odd offset, so a parser
must read the two u32 fields at `+0x03` and `+0x07` rather than assume 4-byte
alignment.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Observed | Notes                       |
| ------- | ------------------ | ------------ | -------- | --------------------------- |
| `+0x00` | u32                | string_count | 0        | Always zero                 |
| `+0x04` | pstr[string_count] | strings      |          | Empty                       |

Earlier versions of this doc called `string_count` the trailer's `unknown_00`
and `zero` its `unknown_08`.

## Decoded Table

All nine entries in the observed file:

| Record | unknown_00 | unknown_02 | unknown_03 | unknown_07 |
| ------ | ---------- | ---------- | ---------- | ---------- |
| 0      | 1        | 19      | 0       | 200     |
| 0      | 1        | 20      | 0       | 300     |
| 1      | 2        | 19      | 0       | 200     |
| 1      | 2        | 20      | 0       | 300     |
| 2      | 3        | 0       | 100     | 300     |
| 3      | 4        | 0       | 100     | 300     |
| 4      | 5        | 0       | 100     | 300     |
| 5      | 6        | 0       | 100     | 300     |
| 6      | 7        | 0       | 300     | 350     |

The table splits cleanly in two. Records 0–1 carry two entries each, told apart
by `unknown_02` 19 and 20, with `unknown_03` zero. Records 2–6 carry one entry
with `unknown_02` zero and a non-zero `unknown_03`.

## Notes

- The record stream lands exactly on `end_of_records`: `7 × 4 + 9 × 11 = 127`
  bytes of records after the 8-byte header. That exact fit is what confirms the
  4-byte `entry_count` prefix and the 11-byte entry size.
- Records are variable length, so a parser must follow `entry_count` rather than
  assume the 15-byte or 26-byte sizes seen in this file.
- `unknown_00` is redundant with the record index in the observed data, but it
  is stored per entry rather than per record, so it is read from the entry.
- Observed: 7 records and 9 entries in the pre-2026-09-27 fixture and in the
  2026-09-27 client; the file is byte-identical between the two.
- The filename suggests this sits on the fairy feeding and enchant path, which
  is the same system documented in `fairyupgraderate.bss`. Nothing in this file
  or in `languagedata_en.loc` confirms that link, so it is not asserted here.
- No LOC lookup applies: every field is a small integer, and none of the values
  match a localization key.
- A community fairy guide covering growth, Sprouting, skill changes, rebirth, and
  the Laila's Petal exchange describes no failure-count mechanic and lists no
  value of 100, 200, 300, or 350 on any of those paths. Player-facing
  documentation is therefore unlikely to resolve this file.

## Open Questions

### `unknown_03` and `unknown_07` Meaning

`unknown_03` and `unknown_07` are unidentified. The filename points at a failure
counter, and the pairs read plausibly as bounds (`0..200`, `100..300`,
`300..350`), but nothing in the file confirms that they are a range rather than
two independent settings such as a threshold and a cap.

A Sprouting failure counter is the reading the filename invites, and it is the
one the game rules argue against: a fairy gets a single Sprout attempt, and
failing it ends that fairy's tier-up permanently short of a cash-shop Rebirth.
There is no repeated attempt for a counter reaching 100 or 350 to accumulate
over. That points the `enchant` in the filename at the feeding and growth path
instead, or at a counter kept across fairies rather than within one.

### `unknown_00` Meaning

`unknown_00` runs 1–7. It is not the four fairy grades and not the three Sprouting
steps, so it indexes something else on the feeding path. A file that keys the
same 1–7 range would identify it.

### `unknown_02` 19 and 20

Only records 0 and 1 split into two entries, distinguished by `unknown_02` 19
and 20, and only those entries have `unknown_03` of zero. The values are too small to
be item IDs and do not match the fairy-growth item IDs used by
`fairyupgraderate.bss`. Fairy levels are the strongest candidate, since the tier
level caps are 10, 20, 30, and 50, putting 19 and 20 exactly at the Glimmering
cap boundary, but no file read so far keys anything by level 19 or 20, so this
stays unconfirmed.
