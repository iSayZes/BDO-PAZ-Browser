# `fairyfeedingitem.dbss` Format

## Purpose

The list of items a fairy accepts in the Growth window, with the fairy EXP one
item grants. Each record keys one item ID. `fairyfeedingitemoffset.dbss` is the
item-keyed index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ------ | ---------------- | --------- |
| 1      | 1784 and later | 3474    | `fairyfeedingitem.dbss`       | 62,892 | 2,246 Record     | 28        |
| 1      | 1784 and later | 3474    | `fairyfeedingitemoffset.dbss` | 26,956 | 2,246 Offset Row | 12        |

| Layout | File                          | Known             | Unknown          |
| ------ | ----------------------------- | ----------------- | ---------------- |
| 1      | `fairyfeedingitem.dbss`       | 26,956 B (42.9%)  | 35,936 B (57.1%) |
| 1      | `fairyfeedingitemoffset.dbss` | 26,956 B (100.0%) | 0 B (0.0%)       |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                     |
| ----------------------------- | -------- | -------------------------------------------------------- |
| `fairyfeedingitemoffset.dbss` | Optional | `item_id -> (data_offset, data_size)` index              |
| `languagedata_en.loc`         | Optional | Item name for `item_id` (`str_type=0`, `str_id1=item_id`) |

The main file has a fixed record stride and a count in its header, so the
handler reads it without the offset companion.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                             |
| ------- | ------------- | ------- | --------------------------------- |
| `+0x00` | u32           | count   | Number of records                 |
| `+0x04` | Record[count] | records | See Record                        |

On client 3464 the file is 62,892 bytes: 4 + 2,246 records of 28 bytes.

### Record (28 bytes)

| Offset  | Type      | Field      | Notes                                                      |
| ------- | --------- | ---------- | ---------------------------------------------------------- |
| `+0x00` | u32       | key        | Record key; equals `item_id` in every record               |
| `+0x04` | u32       | item_id    | Item fed to the fairy                                      |
| `+0x08` | u32       | unknown_08 | `576` on all but one record (see Open Questions)           |
| `+0x0C` | u32       | exp        | Fairy EXP granted per item                                 |
| `+0x10` | bytes[12] | unknown_10 | Zero in every record                                       |

The offset companion points at `record_start + 4`, so the addressable payload
is the 24 bytes after the key.

`item_id` has a zero top byte in every record, so it reads the same as an item
key with enhancement level 0 (`item_key = enchant_level << 24 | item_id`, see
`_common/item_key.py`).

### `fairyfeedingitemoffset.dbss`

| Offset  | Type              | Field | Notes                                        |
| ------- | ----------------- | ----- | -------------------------------------------- |
| `+0x00` | u32               | count | Equals the `fairyfeedingitem.dbss` count     |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                               |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                 |
| ------- | ---- | ----------- | ----------------------------------------------------- |
| `+0x00` | u32  | item_id     | Record key                                            |
| `+0x04` | u32  | data_offset | Absolute offset in the main file, past the 4-byte key |
| `+0x08` | u32  | data_size   | Always `24` (`28 - 4-byte key prefix`)                |

Every row points at the record with the same key, and every main-file record
has one row. Neither file is sorted by item ID, and the row order differs
from the record order: on client 3464 the third and fourth rows point at the
fourth and third records. Recover the full record with
`record_start = data_offset - 4`.

## EXP Values

The EXP field is confirmed against the client's own tooltip. The English item
description of Ornette's Dark Honey Wine (LOC `str_type=0`, `str_id1=18448`,
`str_id4=1`) says one wine takes a Faint, Glimmering or Radiant fairy from
Lv. 1 (0.00%) to Lv. 5 (98.84%), and a Brilliant fairy to Lv. 6 (58.36%).
Spending this file's `13,300` (client 3464) on the [petexp.dbss](petexp_dbss.md) curves
gives Lv. 5 at 98.836% on tables 6, 7 and 9 (10, 20 and 50 levels) and Lv. 6
at 58.363% on table 8 (30 levels).

On client 3464 `exp` runs from `12` (Styd Crossbow) to `375,000` (109 items,
all named `Fiery ...`), over 121 distinct values. The two growth wines
that [fairyupgraderate.bss](fairyupgraderate_bss.md) also uses are in the list:
Sweet Honey Wine (`2,000`) and Ornette's Dark Honey Wine (`13,300`).

The [Garmoth fairy guide](https://garmoth.com/guides/post/fairy-laila-companion)
lists rounded values for the same items (client 3464 values in brackets):
boss armor 47,500 (`47,499`), Liverto weapons 3,000 (`2,999`), Ultimate
awakening weapons 13,000 (`12,999`), Lemoria armor 3,300, Black Spirit's
Claw 1,500 and Fiery Kutum / Nouver 375,000 (Garmoth calls them "Blazing").
It gives Ornette's Dark Honey Wine as 13,000; this file and the client
tooltip above give `13,300`.

## Notes

- The Growth window (`panel_window_fairy_all_3.luac`,
  `PaGlobal_FairyGrowth_All`) lists inventory items for which
  `itemWrapper:isFairyFeedItem()` is true, skips item 54030, and shows Sweet
  Honey Wine (54030) and Ornette's Dark Honey Wine (18448) as two fixed slots
  instead. The EXP preview comes from `ToClient_CalculateUpgradeExp` and the
  feed itself from `ToClient_FairyFeedingRequest`; both take an item enchant
  key, so the Lua never reads this file's fields directly.
- On client 3464 every `item_id` has an English LOC item name.
- Keys are base item IDs: the enhancement byte (`item_key >> 24`) is `0` on
  every record, and there is one row per item instead of one per level as in
  `itemenchant.dbss`. Whether enhanced gear can be fed is decided outside this
  file. The [Dottz Gaming beginner fairy guide](https://dottzgaming.com/other-games/bdo-beginner-fairy-guide/)
  says the Growth window takes unenhanced equipment only; the Growth window Lua
  checks no enhancement level itself (it asks the client's
  `isFairyFeedItem()`), and no English LOC string states the rule.
- The value `576` appears in no fairy Lua script as a constant; the only client
  Lua files holding a `576` constant are a minigame, the fishing widget and a
  QA script.

## Open Questions

### `unknown_08` Meaning

On client 3464, 2,245 of the 2,246 records hold `576` (`0x240`) and one holds
`0`: Agerian Helmet (item 10809, 168 EXP). Nothing in the fairy Lua or the
other fairy tables uses `576`, so it is not known whether it is a flag set, a
count limit or an ID, or why the Agerian Helmet differs.
