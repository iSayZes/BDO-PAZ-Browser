# `itemsubgroup.dbss` Format

## Purpose

Item subgroups: named lists of items that other tables hand out as a group. Each record is one subgroup key followed by its item entries. Worker production uses it through [`plantexchangegroup.bss`](plantexchangegroup_bss.md) (`item_subgroup_key`); NPC shops and trade managers reach theirs through [`itemmaingroup.bss`](itemmaingroup_bss.md) groups; the other subgroups belong to tables not decoded yet (drops, boxes, trade goods). `itemsubgroupoffset.dbss` is required to address the variable-length records.

```text
subgroup 42356 -> Elder Tree Timber (4611), Bloody Tree Knot (5005), Elder Tree Sap (5014)
subgroup 40189 -> Teff (7022)
```

The record header and the item ID position match [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, "Worker-production item tables"), which leaves the rest of each 135-byte entry unmapped. Their "0-100 items" range does not hold: subgroup 52001 has 11,560 entries.

## Companion Files

| File                      | Required | Role                                                  |
| ------------------------- | -------- | ----------------------------------------------------- |
| `itemsubgroupoffset.dbss` | Required | Maps subgroup key to byte offset and record byte count |
| `languagedata_en.loc`     | Optional | Item names, LOC type 0 at `str_id1=item_id`           |

All multi-byte values are little-endian unless noted otherwise.

## File Layout

| Offset  | Type | Field         | Notes                                                  |
| ------- | ---- | ------------- | ------------------------------------------------------ |
| `+0x00` | u32  | record_count  | Number of subgroups; `16,690` on the 2026-09-27 client |
| `+0x04` | ...  | record_stream | Variable-length records, packed back-to-back           |

Sorted by `data_offset`, the offset rows cover every byte from `+0x04` to EOF with no gaps or overlaps.

## Record Structure

### Subgroup Record (`18 + 135 * entry_count` bytes)

| Offset  | Type    | Field       | Notes                                                          |
| ------- | ------- | ----------- | -------------------------------------------------------------- |
| `+0x00` | u32     | subgroup_key | Equals the offset row `record_id` on every record; observed `1309`-`65535` |
| `+0x04` | u8[10]  | unknown_04  | Always all zero                                                |
| `+0x0E` | u32     | entry_count | Number of entries; `1`-`11,560`, never `0`; unaligned           |
| `+0x12` | entry[] | entries     | 135-byte entries repeated `entry_count` times                  |

`18 + 135 * entry_count` equals the offset row `data_size` on all 16,690 records.

### Item Entry (135 bytes)

97,808 entries in total. Most set only `item_key` and `select_rate`; every offset not listed is zero on every entry.

| Offset  | Type    | Field      | Notes                                                                  |
| ------- | ------- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | u32     | item_key   | `(enchant_level << 24) \| item_id`, the same packing as the `itemenchant.dbss` key; see below |
| `+0x10` | u8      | unknown_10 | `1` on one entry, else `0`                                             |
| `+0x11` | u8      | unknown_11 | `1` on the 247 entries of subgroups 54001 and 55000, else `0`          |
| `+0x12` | i64     | min_count  | `-1` on 21,168 entries (subgroup bands 32xxx, 50xxx-52xxx, 55xxx), else `0`; see Field Names |
| `+0x1A` | i64     | max_count  | Same as `min_count` on every entry                                     |
| `+0x22` | i32     | intimacy_variation | `0` on 96,887 entries; negative on 921 (`-200` on 426, then `-370`, `-470`, `-50`, `-25`, `-100`, `-500`, `-300` and a few others) |
| `+0x26` | u8      | unknown_26 | `2` or `4` on the 247 entries of subgroups 54001 and 55000, else `0`; in 55000 `4` is every packaged dried fish, `2` everything else |
| `+0x2E` | u8      | is_apply_random_price | `1` on 794 entries, else `0`                                |
| `+0x2F` | u8      | rent_time  | `1`, `2` or `3` on three entries, else `0`                             |
| `+0x33` | u32     | select_rate | Selection weight; `1,000,000` on 96,952 entries; `0` on the 247 entries that set `unknown_83`; 226 below and 383 above one million (up to `9,000,000`); unaligned |
| `+0x37` | u8      | unknown_37 | `1` on the 247 entries of subgroups 54001 and 55000, else `0`          |
| `+0x38` | u8      | unknown_38 | Same as `unknown_37`                                                   |
| `+0x3B` | i64     | unknown_3b | Set on the same 247 entries, e.g. `1800` for Pepper Crate; the other price-like fields are fixed shares of it |
| `+0x43` | i64     | unknown_43 | Same entries; exactly 30%, 65%, 75%, 85% or 95% of `unknown_3b` (`1350` for Pepper Crate) |
| `+0x4B` | i64     | unknown_4b | Same entries; exactly 130% of `unknown_3b` on all of them (`2340` for Pepper Crate) |
| `+0x53` | i64     | unknown_53 | Same entries; its size is a fixed share of `unknown_3b` per floor group (65% floor: 6%, 75%: 6.5%, 85%: 7.5%, 95%: 5.8%; the 30% group mixes 6%-9%); the sign alternates +, - down the entries sorted by item ID |
| `+0x5B` | u8      | unknown_5b | Same entries; exactly 1% of `unknown_3b` (`18` for `1800`)             |
| `+0x83` | u32     | unknown_83 | Same entries; roughly inverse to `unknown_3b` (`unknown_3b x unknown_83` mostly 900-1,200 million), capped at `1,000,000` on all 119 entries with `unknown_3b = 900`; unaligned |

### `item_key` Packing

```text
item_id = item_key & 0xFFFFFF
enchant_level = item_key >> 24
```

`enchant_level` is `0` on 95,166 entries and `1`-`20` on the other 2,642: the entry hands out the item at that enhancement level. All 2,642 non-zero keys exist as `itemenchant.dbss` keys, and the levels fit the items: Manos Necklace at `1`-`5` (PRI to PEN), Kzarka Longsword at `15`, Blackstar Helmet at `19` (TET), Dim Tree Spirit's Armor at `20` (PEN).

## `itemsubgroupoffset.dbss`

Standard PABR offset companion with 10-byte rows, read by `parse_pabr_offset_rows` (`handlers/_common/pabr_offset.py`).

| Offset             | Type    | Field        | Notes                                  |
| ------------------ | ------- | ------------ | -------------------------------------- |
| `+0x00`            | char[4] | magic        | ASCII `PABR`                           |
| `+0x04`            | u32     | record_count | Equals `itemsubgroup.dbss` `record_count` |
| `+0x08`            | row[]   | rows         | 10-byte rows repeated `record_count` times |
| EOF - 12           | u32     | unknown_trailer_00 | Always `0`                             |
| EOF - 8            | u32     | end_of_rows  | Equals `8 + count * 10` (`166,908`)    |
| EOF - 4            | u32     | unknown_trailer_08 | Always `0`                             |

The 12-byte trailer is the same shape as the `itemenchantoffset.dbss` one.

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                               |
| ------- | ---- | ----------- | --------------------------------------------------- |
| `+0x00` | u16  | record_id   | Subgroup key; equals the record's `subgroup_key`    |
| `+0x02` | u32  | data_offset | Absolute offset of the record, at its inline key    |
| `+0x06` | u32  | data_size   | Record byte count, `18 + 135 * entry_count`         |

Subgroup keys are u16 in the index, so no key above `65535` exists.

## Notes

- Worker production subgroups use one entry shape only: `enchant_level=0`, `select_rate=1,000,000`, every other field zero (815 entries in 364 subgroups). 278 of their 281 distinct item IDs have an English LOC type 0 name; 4016, 4017 and 4415 have none.
- Subgroup 55000 (246 entries) lists trade goods: crates such as Pepper Crate (7401) and Garlic Crate (7402), packaged dried fish such as Packaged Dried Dace (55947), and items such as Mansha Goblin Mask (55026), and 54001 holds one entry (item 55151). They are the only subgroups that set `unknown_37` to `unknown_83`; the i64 fields look like a price range (`unknown_43 < unknown_3b < unknown_4b`), but that is not confirmed.
- The largest subgroups are 52001 (11,560 entries), 32001 (707) and 52003 (391).
- The 36 subgroup keys that `plantzone.dbss` zones reach but this index lacks (41208-41212, 43183-43195, 44059, 44060, 44860-44874, 45018) have no record in `bartersubgroup.bss` or `limiteditemsubgroup.bss` either (45018 matches bytes in `limiteditemsubgroup.bss` only inside unrelated rows). They are item exchange keys, not subgroup keys: each exchange's drop key is an [`itemmaingroup.bss`](itemmaingroup_bss.md) group, which lists the subgroups (see [`plantexchangegroup.bss` Field Names](plantexchangegroup_bss.md#field-names)). 44059 and 44060 are also group IDs themselves, pointing at subgroups 42339 and 42340 (client 3464).

## Field Names

The entry fields are named from two sources. The 2016 client (build of 2016-01-11) ships with debug symbols, and its `gc::ItemGroupValue` holds `_itemKey`, `_selectRate`, a condition, `_isPetAddDrop`, `_minCount` (i64), `_maxCount` (i64), `_intimacy`, `_explorationExperience`, `_isApplyRandomPrice`, four more flags, nine i64 stock fields (`_needAmountForStock`, `_minRemainAmountForStock`, `_maxRemainAmountForStock`, `_variedAmountPerTickForStock`, `_tradingCountUnitForStock`, `_maxCountOfBuyFromNpcForStock`, `_reverseAmountForStock`, `_minSteadyAmountForStock`, `_maxSteadyAmountForStock`) and `_experience`. Its `gc::ItemSubGroupStaticStatus` keeps a `_totalPercent` next to the entry list, which is why `select_rate` reads as a weight against the subgroup's total. The server-side `ItemSubGroup_Table` of a private server on client 519 has one row per subgroup, item and enchant level; 23,750 of them match an entry of client 3464:

| Field                 | `ItemSubGroup_Table` column | Matching rows                                    |
| --------------------- | --------------------------- | ------------------------------------------------ |
| `item_key` low 24 bits, high byte | `ItemKey`, `EnchantLevel` | the join key                             |
| select_rate           | `SelectRate_0`              | 17,594 of 23,730 non-zero; the server also stores weights above one million (up to `3,000,000` on 1,648 rows) |
| intimacy_variation    | `IntimacyVariation`         | 964 of 964 non-zero                              |
| is_apply_random_price | `ApplyRandomPrice`          | 18 of 18 non-zero                                |
| rent_time             | `RentTime`                  | 3 of 3 non-zero                                  |
| min_count, max_count  | `MinCount_0`, `MaxCount_0`  | 6,720 rows where the server has `-1`; where the server has a count (`1`, `20` to `40` ...) this file stores `0` |

`min_count` and `max_count` sit where the 2016 struct has `_minCount` and `_maxCount`, just before `_intimacy`, and hold the server's `-1`. The server's counts above zero are not in the client file.

## Open Questions

### Subgroup 55000 Fields

The trade goods entries set a block of i64 values that behave like a price band around `unknown_3b`: the top is always 130%, the floor is one of five shares per item group (Ancient coins 30%; Garlic, Onion, Grape crates and most dried fish 65%; Pepper, Strawberry crates 75%; Potato, Barley, Wheat crates 85%; Witch's Poison Herb and some dried fish 95%), and `unknown_5b` is a 1% step. The trade sell price is `Base Value x Distance Bonus x Trading Bonus x Bargain - Material Cost`, so `unknown_3b` would be the original Base Value and the band the range the current Base Value moves in; In-Game Checks has the test. What `unknown_53`, `unknown_26` and `unknown_83` control is open. `unknown_53` looks like a price swing size with a direction set per row. These entries leave `select_rate` at `0` and set `unknown_83` instead, so `unknown_83` may play the same role: a per-item weight, higher for cheaper goods. The 2016 stock fields (see Field Names) are nine i64 values in the same part of the entry; `unknown_3b`, `unknown_43`, `unknown_4b` and `unknown_53` may be the first four (need amount, minimum and maximum remain amount, varied amount per tick), but no server column holds them, so they keep their offsets.

## In-Game Checks

### Subgroup 55000 Price Band

Needs item (all):

- [Pepper Crate](https://bdocodex.com/us/item/7401/)
- [Ancient Gold Coin](https://bdocodex.com/us/item/55001/)

Needs NPC: any Trade Manager

Pepper Crate stores `unknown_3b` 1,800, `unknown_43` 1,350 (75%) and `unknown_4b` 2,340 (130%); Ancient Gold Coin stores 900, 270 (30%) and 1,170. Read the current Base Value the Trade Manager shows for both over several days. If Pepper Crate stays between 1,350 and 2,340 and Ancient Gold Coin drops below 585 (65% of 900), `unknown_3b` is the original Base Value and `unknown_43` and `unknown_4b` are the floor and ceiling of the current one. A Pepper Crate price outside 1,350 to 2,340 rules the band out.
