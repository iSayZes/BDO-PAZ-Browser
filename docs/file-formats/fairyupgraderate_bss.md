# `fairyupgraderate.bss` Format

## Purpose

Defines the **Sprouting** success rates for fairies. Sprouting is the attempt to
raise a max-level fairy into the next grade, and it consumes fairy-growth wine.
Each wine consumed adds a fixed slice of success chance, so the file stores, per
grade transition and per usable item, the chance contributed by **one** item and
the item count that reaches a guaranteed 100%.

Example:

```text
step 2 (Brilliant -> Radiant): Sweet Honey Wine          0.2500% per item, 400 for 100%
                               Ornette's Dark Honey Wine 4.0000% per item,  25 for 100%
```

## Graph

### Tags

- file format
- bss
- fairy
- sprouting
- upgrade
- probability

### Connections

- [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md) — establishes the four fairy grades and the same parts-per-million convention; skills are rerolled from it after a successful Sprout
- [fairyequipskill.bss](fairyequipskill_bss.md) — fairy skill catalog rolled after Sprouting
- [fairyskillchange.dbss](fairyskillchange_dbss.md) — fairy skill reroll cost, the other fairy-side cost table
- [languagedata_en.loc](languagedata_loc.md) — English item names for `item_id`

---

## Companion Files

The format is self-contained — there is no `fairyupgraderateoffset.dbss`.

| File                    | Required | Role                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| `languagedata_en.loc`   | Optional | Item name for `item_id` (`str_type=0`, `str_id1=item_id`)    |
| `fairyfeedingitem.dbss` | Optional | Full fairy feeding item list; contains both `item_id` values |

All multi-byte values are little-endian.

---

## File Layout

| Offset  | Type  | Field   | Notes                                         |
| ------- | ----- | ------- | --------------------------------------------- |
| `+0x00` | u8[4] | magic   | `PABR` (ASCII)                                |
| `+0x04` | u32   | count   | Number of records; observed 3                 |
| `+0x08` | —     | records | `count` variable-length records, back to back |
| end-12  | —     | trailer | 12-byte file trailer                          |

Observed file size is 143 bytes: 8-byte header, 3 × 41-byte records, 12-byte trailer.

### Record (9 bytes + `entry_count` × 16)

One record per grade transition, in ascending grade order.

| Offset  | Type | Field            | Observed | Notes                                        |
| ------- | ---- | ---------------- | -------- | -------------------------------------------- |
| `+0x00` | u8   | unknown_lead     | 0        | Zero in all three records                    |
| `+0x01` | u32  | success_cap_ppm  | 1000000  | 100% success, and the cap on accumulated rate |
| `+0x05` | u32  | entry_count      | 2        | Number of item entries that follow           |
| `+0x09` | —    | entries          |          | `entry_count` × 16-byte entries              |

Records carry no explicit key — the upgrade step is the record index.

### Entry (16 bytes, repeated `entry_count` times)

One entry per item type that can be used for this Sprouting step. Only one item
type may be used per attempt — the entries are alternatives, not a combined pool.

| Offset  | Type | Field         | Notes                                                              |
| ------- | ---- | ------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_id       | Fairy-growth item consumed; LOC `str_type=0`, `str_id1=item_id`    |
| `+0x04` | u32  | rate_ppm      | Success chance added by **one** item, out of `success_cap_ppm`     |
| `+0x08` | u32  | items_for_max | Item count that reaches the 100% cap; also the per-attempt maximum |
| `+0x0C` | u32  | reserved      | Zero in all observed entries                                       |

Success chance for `n` items is `min(n × rate_ppm, success_cap_ppm)`, with `n`
capped at `items_for_max`.

### Trailer (12 bytes)

Follows the last record — the same trailer shape used by
[zodiacsignindex.bss](zodiacsignindex_bss.md).

| Offset  | Type | Field          | Observed | Notes                                 |
| ------- | ---- | -------------- | -------- | ------------------------------------- |
| `+0x00` | u32  | reserved_a     | 0        | Always zero                           |
| `+0x04` | u32  | end_of_records | 131      | Byte offset just past the last record |
| `+0x08` | u32  | reserved_b     | 0        | Always zero                           |

`end_of_records` is authoritative for where the record stream stops; parse
records until that offset rather than assuming a fixed record size.

---

## Item IDs

| item_id | English name              |
| ------- | ------------------------- |
| 18448   | Ornette's Dark Honey Wine |
| 54030   | Sweet Honey Wine          |

These are the only two items in `languagedata_en.loc` whose tooltip says the
item can be used to _grow your Fairy_, and both appear in `fairyfeedingitem.dbss`.

Item icons are derived from the item ID as
`ui_texture/icon/new_icon/product_icon_png/web_{item_id:08d}.png`. Each item also
has a `.dds` icon, but those sit in per-category folders that differ per item
(`03_etc/09_petitem/` for 54030, `09_cash/` for 18448) and are not derivable from
the ID. In `product_icon_png` the unprefixed `{item_id:08d}.png` exists for 54030
but not for 18448, so the `web_` variant is the form usable for both.

---

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

---

## Suggested UI Layout

| Column        | Type | Notes                                                    |
| ------------- | ---- | -------------------------------------------------------- |
| Step          | num  | Record index, 0-based                                    |
| Upgrade       | text | Grade transition label derived from the record index     |
| Icon          | text | Item icon, `product_icon_png/web_{item_id:08d}.png`      |
| Item          | text | LOC name for `item_id`, falls back to the raw ID         |
| Item ID       | num  | Raw `item_id`                                            |
| Chance / Item | num  | `rate_ppm / success_cap_ppm` as a percentage             |
| Rate (ppm)    | num  | Raw `rate_ppm`                                           |
| Items for Max | num  | Raw `items_for_max`                                      |

---

## Notes

- Sprouting may only be attempted once per fairy unless a rebirth is used, and a
  successful Sprout resets the fairy's skills — which are then rerolled from
  `fairyequipskillaquire.dbss` at the new grade.
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
- `fairyfeedenchantfailcount.bss` sits next to this file in the PAZ tree and is
  likely a related fail-counter table, but it is not yet decoded or documented.

---

## Open Questions

### `unknown_lead`

The first byte of every record is zero. It may be a record type tag, a grade key
that happens to be zero-based, or padding carried from the writer. Only a file
where it varies would distinguish these.

### Rebirth Interaction

Sprouting can be retried after a rebirth, but nothing in this file encodes a
retry allowance, a rebirth cost, or a changed rate on a retry. Those values live
elsewhere — `fairyfeedenchantfailcount.bss` and the fairy potion tables are the
nearest undecoded candidates.
