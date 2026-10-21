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
| 1      | 1485 and later | 3474    | `fairyfeedingitem.dbss`       | 62,892 | 2,246 Record     | 28        |
| 1      | 1485 and later | 3474    | `fairyfeedingitemoffset.dbss` | 26,956 | 2,246 Offset Row | 12        |

| Layout | File                          | Known             | Unknown          |
| ------ | ----------------------------- | ----------------- | ---------------- |
| 1      | `fairyfeedingitem.dbss`       | 44,924 B (71.4%)  | 17,968 B (28.6%) |
| 1      | `fairyfeedingitemoffset.dbss` | 26,956 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

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

| Offset  | Type     | Field      | Notes                                                      |
| ------- | -------- | ---------- | ---------------------------------------------------------- |
| `+0x00` | u32      | key        | Record key; equals `item_id` in every record               |
| `+0x04` | u32      | item_id    | Item fed to the fairy                                      |
| `+0x08` | bytes[4] | padding_08 | Aligns `exp` to 8 bytes, never written; see Notes          |
| `+0x0C` | u64      | exp        | Fairy EXP granted per item                                 |
| `+0x14` | u64      | unknown_14 | `0` in every record (clients 1784 and 3474)                |

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

## Field Names

The record is the `Fairy_FeedingItem_Table` sheet of a private server on
client 1784, with the columns `ItemKey` and `Exp`. That server's dump
(`Instance_dumpFull.exe`) reads the client file by copying the 24 bytes
after the key into a `FairyItemInfo` in one block (VA `0x140bd35b3`), so the
payload is that struct's memory image. Its sheet loader builds the same
struct in `set()` (VA `0x140bd3810`): a u32 `ItemKey` at `+0`, an 8-byte
`Exp` at `+8` and a literal 8-byte `0` at `+0x10`. Nothing writes `+4` to
`+7`.

| Field        | Struct member | Sheet column |
| ------------ | ------------- | ------------ |
| `item_id`    | u32 `+0x00`   | `ItemKey`    |
| `padding_08` | `+0x04`       | none         |
| `exp`        | u64 `+0x08`   | `Exp`        |
| `unknown_14` | u64 `+0x10`   | none         |

`padding_08` is the gap the compiler leaves before the 8-byte `exp`. Its
bytes are what the builder's stack held: `576` (`0x240`) on all but one
record of client 3464, `0x200` or `0x201` on client 3474 and `2` on client
1784, with the Agerian Helmet (item 10809), the sheet's first row, as the
odd one out on all three. `unknown_14` has no sheet column, `set()` writes
`0`, and no code in the dump names it.

The sheet and the private server's own file hold the same 1,864 items. On
all of them `item_id` equals `ItemKey` and `exp` equals `Exp` with its
fraction dropped (`176.75` becomes `176`); client 3474 has the same `exp` on
the 1,864 items it shares. Earlier versions of this doc read `exp` as a u32
and the 12 bytes after it as one zero field; the upper half of `exp` is `0`
on every record, so every EXP reads as before.

## Notes

- `padding_08` is alignment filler: in the client 1784 server dump the
  record is a `FairyItemInfo` with a u32 item key at `+0` and an 8-byte
  `exp` at `+8`, so `+4` to `+7` align `exp` to 8 bytes, and the struct's
  builder `set()` (VA `0x140bd3810`) never writes them (Field Names).
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
