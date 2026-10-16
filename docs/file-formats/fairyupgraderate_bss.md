# `fairyupgraderate.bss` Format

## Purpose

Defines the **Sprouting** success rates for fairies. Sprouting is the attempt to
raise a max-level fairy into the next grade, and it consumes fairy-growth wine.
Each wine consumed adds a fixed slice of success chance, so the file stores, per
grade transition and per usable item, the chance contributed by **one** item and
the item count that reaches a guaranteed 100%.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

The format is self-contained; there is no `fairyupgraderateoffset.dbss`.

| File                    | Required | Role                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| `languagedata_en.loc`   | Optional | Item name for `item_id` (`str_type=0`, `str_id1=item_id`)    |
| `fairyfeedingitem.dbss` | Optional | Full fairy feeding item list ([fairyfeedingitem](fairyfeedingitem_dbss.md)); contains both `item_id` values |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type          | Field          | Notes                                         |
| ------------------- | ------------- | -------------- | --------------------------------------------- |
| `+0x00`             | char[4]       | magic          | `PABR` (ASCII)                                |
| `+0x04`             | u32           | count          | Number of records; observed 3                 |
| `+0x08`             | Record[count] | records        | Variable-length records, back to back         |
| `records+0x00`      | String Table  | string_table   | The PABR string table, here with no strings   |
| `string_table+0x00` | u32           | end_of_records | Byte offset just past the last record; observed 131 |
| `string_table+0x04` | u32           | zero           | Always `0`                                    |

Observed file size is 143 bytes: 8-byte header, 3 × 41-byte records, 12-byte trailer.

The 12-byte trailer (`string_table`, `end_of_records`, `zero`) follows the
last record, the same trailer shape used by
[zodiacsignindex.bss](zodiacsignindex_bss.md).

`end_of_records` is authoritative for where the record stream stops; parse
records until that offset rather than assuming a fixed record size.

### Record (variable: 9 bytes + entries)

One record per grade transition, in ascending grade order.

| Offset  | Type               | Field            | Observed | Notes                                        |
| ------- | ------------------ | ---------------- | -------- | -------------------------------------------- |
| `+0x00` | u8                 | unknown_00       | 0        | Zero in all three records                    |
| `+0x01` | u32                | success_cap_ppm  | 1000000  | 100% success, and the cap on accumulated rate |
| `+0x05` | u32                | entry_count      | 2        | Number of item entries that follow           |
| `+0x09` | Entry[entry_count] | entries          |          | `entry_count` × 16-byte entries              |

Records carry no explicit key; the upgrade step is the record index.

Earlier versions of this doc called `unknown_00` `unknown_lead`.

### Entry (16 bytes)

One entry per item type that can be used for this Sprouting step. Only one item
type may be used per attempt; the entries are alternatives, not a combined pool.

| Offset  | Type | Field         | Notes                                                              |
| ------- | ---- | ------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_id       | Fairy-growth item consumed; LOC `str_type=0`, `str_id1=item_id`    |
| `+0x04` | u32  | rate_ppm      | Success chance added by **one** item, out of `success_cap_ppm`     |
| `+0x08` | u32  | items_for_max | Item count that reaches the 100% cap; also the per-attempt maximum |
| `+0x0C` | u32  | unknown_0c    | Zero in all observed entries                                       |

Success chance for `n` items is `min(n × rate_ppm, success_cap_ppm)`, with `n`
capped at `items_for_max`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Observed | Notes       |
| ------- | ------------------ | ------------ | -------- | ----------- |
| `+0x00` | u32                | string_count | 0        | Always zero |
| `+0x04` | pstr[string_count] | strings      |          | Empty       |

Earlier versions of this doc called `string_count` the trailer's `unknown_00`
and `zero` its `unknown_08`.

## Item IDs

| item_id | English name              |
| ------- | ------------------------- |
| 18448   | Ornette's Dark Honey Wine |
| 54030   | Sweet Honey Wine          |

These are the only two items in `languagedata_en.loc` whose tooltip says the
item can be used to _grow your Fairy_, and both appear in `fairyfeedingitem.dbss`.

Item icons are derived from the item ID as
`ui_texture/icon/new_icon/product_icon_png/{item_id:08d}.png`. Each item also has
a `.dds` icon, but those sit in per-category folders that differ per item
(`03_etc/09_petitem/` for 54030, `09_cash/` for 18448) and are not derivable from
the ID. Item 18448 has no unprefixed PNG, only a `web_`-prefixed one; the preview
icon resolver falls back to that sibling, so the canonical path is still correct.

## Decoded Table

Record index is the ascending grade transition, using the grade order
established in [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md)
(Faint → Glimmering → Brilliant → Radiant, tiers 1–4).

| Record | Upgrade step                     | Sweet Honey Wine         | Ornette's Dark Honey Wine |
| ------ | -------------------------------- | ------------------------ | ------------------------- |
| 0      | Faint → Glimmering (T1 → T2)     | 2.2222% each, 45 for max | 33.3333% each, 3 for max  |
| 1      | Glimmering → Brilliant (T2 → T3) | 0.6666% each, 150 for max | 10.0000% each, 10 for max |
| 2      | Brilliant → Radiant (T3 → T4)    | 0.2500% each, 400 for max | 4.0000% each, 25 for max  |

Record 2 matches the published Tier 3 → Tier 4 cost of 400 Sweet Honey Wine or
25 Ornette's Dark Honey Wine for a guaranteed Sprout, which fixes both the record
order and the meaning of `items_for_max`.

Ornette's Dark Honey Wine is worth exactly 15× Sweet Honey Wine at the first two
steps and 16× at the last.

## Notes

- Sprouting may only be attempted once per fairy unless a rebirth is used, and a
  successful Sprout resets the fairy's skills, which are then rerolled from
  `fairyequipskillaquire.dbss` at the new grade.
- A fairy can only Sprout at its tier's level cap, which community guides give as
  10 for Faint, 20 for Glimmering, 30 for Brilliant, and 50 for Radiant. Those
  caps are not stored in this file.
- A failed Sprout consumes the fairy's single attempt permanently; the only way
  back is a cash-shop Rebirth. That makes `items_for_max` the practically
  relevant column: players push to the 100% cost rather than gamble on
  `rate_ppm`, because there is no second roll to fall back on.
- `success_cap_ppm` is `1,000,000` in every record, the same parts-per-million
  convention already confirmed for `fairyequipskillaquire.dbss` and
  `petequipskillaquire.dbss`.
- Unlike the aquire tables, rates here do **not** sum to the cap across entries:
  the two entries are mutually exclusive item choices, each with its own
  per-item contribution.
- `items_for_max × rate_ppm` slightly undershoots the cap in three of six entries
  (`45 × 22222 = 999,990`, `150 × 6666 = 999,900`, `3 × 333333 = 999,999`), so
  `items_for_max` is a stored rounded-up count rather than an exact division.
  A parser should use the stored value, not a computed one.
- Records are self-describing through `entry_count`, so a parser must not assume
  the observed 41-byte record size.
- Framing check: leading-byte framing is the only one that fits. With a trailing
  byte per record the third record would end at 132, one byte past the
  `end_of_records` value of 131.
- [fairyfeedenchantfailcount.bss](fairyfeedenchantfailcount_bss.md) sits next to
  this file in the PAZ tree; its layout is decoded but no field meaning is
  confirmed, so a link to Sprouting is not established.
- Observed: 3 records and 6 entries in the pre-2026-09-27 fixture and in the
  2026-09-27 client; the file is byte-identical between the two.

## Open Questions

### `unknown_00` Meaning

The first byte of every record is zero. It may be a record type tag, a grade key
that happens to be zero-based, or padding carried from the writer. Only a file
where it varies would distinguish these.

### Rebirth Interaction

Sprouting can be retried after a rebirth, but nothing in this file encodes a
retry allowance, a rebirth cost, or a changed rate on a retry. Those values live
elsewhere; `fairyfeedenchantfailcount.bss` (layout decoded, meaning open) and the
fairy potion tables are the nearest candidates.
