# `itemexchangetoclassmapkey.bss` Format

## Purpose

The reverse of [`itemexchangetoclass.dbss`](itemexchangetoclass_dbss.md):
every item key a weapon exchange group lists, once, with the key of its
group. Item `695113` Tuvala Longsword maps to group `165`, the Tuvala main
weapons. The plain PABR file holds the entries, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes  | Records     | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ------ | ----------- | --------- |
| 1      | 1485 and later | 3474    | `itemexchangetoclassmapkey.bss` | 36,188 | 4,521 Entry | 8         |

| Layout | File                            | Known             | Unknown    |
| ------ | ------------------------------- | ----------------- | ---------- |
| 1      | `itemexchangetoclassmapkey.bss` | 36,188 B (100.0%) | 0 B (0.0%) |

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

| File                  | Required | Role                                                      |
| --------------------- | -------- | --------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item name (type `0`, `str_id1` = item ID)                 |

The handler links each `key` to its `itemexchangetoclass.dbss` row without
loading that file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                          |
| ------------------- | ------------ | ------------------ | ---------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                   |
| `+0x04`             | u32          | count              | Number of entries; `4521` on client 3474       |
| `+0x08`             | Entry[count] | entries            | See Entry                                      |
| `entries+0x00`      | String Table | string_table       | See String Table                               |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the entries end (`8 + 8 * count`) |
| `string_table+0x04` | u32          | zero               | Always `0`                                     |

The string table has the shape
[`guildhousecraftskillreverselinklist.bss`](guildhousecraftskillreverselinklist_bss.md)
and [`cutscenecharacterdata.bss`](cutscenecharacterdata_bss.md) use
(`_common/pabr_strings.py`).

### Entry (8 bytes)

| Offset  | Type | Field    | Notes                                                              |
| ------- | ---- | -------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | item_key | Item key (`enchant_level << 24 \| item_id`); unique                |
| `+0x04` | i32  | key      | Group, the `key` of an `itemexchangetoclass.dbss` row that lists `item_key` |

The entries follow neither the item keys nor the group rows: client 3474
starts with `745701` (group `203`), `737509` (`187`) and `930021` (`216`).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No entry reads a string                        |

## Field Names

The file is `_mapKeyFromItemKey` of the 2016
`gc::ItemExchangeToClassStaticStatusManager`, a
`pa_unordered_map<gc::ItemEnchantKey, gc::KeyType<int,0>>`: the map key is
the item, the value the i32 group key. `item_key` and `key` take their
names from [`itemexchangetoclass.dbss`](itemexchangetoclass_dbss.md)
(`_itemKey`, `_key`). No sheet of a private server's `DataSheets.bexcel` on
client 1784 names the file; it is built from the `Item_Exchange` sheet.

Inverting `itemexchangetoclass.dbss` (every filled `item_keys` slot gives
item and row key) gives exactly the items of this file, with no item
missing or extra, and every entry names a row that lists its item:

| Client | Entries | Distinct items in `itemexchangetoclass.dbss` | Items in two rows |
| ------ | ------- | -------------------------------------------- | ----------------- |
| 1784   | 2774    | 2774                                         | 0                 |
| 3474   | 4521    | 4521                                         | 2                 |

## Notes

- An item that two rows list maps to the row that comes first in
  `itemexchangetoclass.dbss`, which is also the higher key, on client 3474:
  `695193` Tuvala Pendant (rows `167` and `107`) maps to `167`, `931802`
  Ultimate Krea Clavis (rows `71` and `68`) to `71`.
- No item key carries an enhancement level on clients 1784 and 3474.
