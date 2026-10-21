# `barter_special.bss` Format

## Purpose

The special barter offers of the Great Ocean barters: one row per offer,
with the item the player hands over, the item the player gets and their
count ranges. The special barter window
(`panel_window_barterinfosearch_special_1.luac`) opens only for a player
with the Value Pack (`isApplyChargeSkill(__eUserChargeType_PremiumPackage)`)
and shows one offer from `ToClient_specialBarterWrapper()`: its from item
and count, its to item and count, and the region and NPC where it can be
traded, which the wrapper gives at run time.

On client 3474 the 105 rows hand over Gold Bars (`3` to `5`) or
`[Level 4]` trade items (`800043` to `800056`) and give Crow Coins (`10`),
Manos accessories, Vell's and Khan's Concentrated Magic, Garmoth's Heart,
crystals, Sethra's Artifacts and other items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | --------------------- | --------- |
| 3      | 3002 and later | 3474    | `barter_special.bss` | 7,370 | 105 Exchange, 105 Row | 56        |
| 2      | 1784 to 2519   | 2519    | `barter_special.bss` | 6,586 | 98 Exchange, 98 Row   | 56        |
| 1      | 1485           | 1485    | `barter_special.bss` | 9,788 | 148 Exchange, 148 Row | 56        |

| Layout | File                 | Known            | Unknown    |
| ------ | -------------------- | ---------------- | ---------- |
| 3      | `barter_special.bss` | 7,370 B (100.0%) | 0 B (0.0%) |
| 2      | `barter_special.bss` | 6,586 B (100.0%) | 0 B (0.0%) |
| 1      | `barter_special.bss` | 9,788 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 3 |
| 3251   | Layout 3 |
| 3002   | Layout 3 |
| 2519   | Layout 2 |
| 2107   | Layout 2 |
| 1784   | Layout 2 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                 | Required | Role                     |
| -------------------- | -------- | ------------------------ |
| `languagedata_*.loc` | Optional | Item names (type 0)      |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field              | Notes                                                   |
| ------------------- | -------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                            |
| `+0x04`             | u32            | row_count          | Number of `rows`; `105` on client 3474                  |
| `+0x08`             | Row[row_count] | rows               | See Row                                                 |
| `rows+0x00`         | String Table   | string_table       | The PABR string table, present but empty                |
| `string_table+0x00` | u32            | string_table_start | Absolute offset of `string_count`; equals `8 + 70 × row_count` |
| `string_table+0x04` | u32            | zero               | Always `0`                                              |

### Row (70 bytes)

The Entry of [`barter_normal.bss`](barter_normal_bss.md) has the same
layout; see Field Names for the three fields that are `0` here.

| Offset  | Type     | Field             | Notes                                                       |
| ------- | -------- | ----------------- | ----------------------------------------------------------- |
| `+0x00` | u16      | barter_region_key | `0` on every row (clients 1784 and 3474)                    |
| `+0x02` | u32      | select_rate       | `0` on every row (clients 1784 and 3474)                    |
| `+0x06` | Exchange | exchange          | See Exchange                                                |
| `+0x3e` | u32      | barter_sub_group  | `0` on every row (clients 1784 and 3474)                    |
| `+0x42` | u32      | barter_category   | Bit mask as in `bartersubgroup.bss`; `0` on every row (client 3474) |

### Exchange (56 bytes)

Same structure as the Exchange of
[`bartersubgroup.bss`](bartersubgroup_bss.md#exchange-56-bytes).

| Offset  | Type | Field              | Notes                                                              |
| ------- | ---- | ------------------ | ------------------------------------------------------------------ |
| `+0x00` | u32  | from_item_key      | The item the player hands over, `enchant_level << 24 \| item_id`; level `0` on every row (client 3474) |
| `+0x04` | u64  | from_min_count     | `1` to `10` (client 3474)                                          |
| `+0x0c` | u64  | from_max_count     | `1` to `10` (client 3474)                                          |
| `+0x14` | u32  | to_item_key        | The item the player gets; 20 rows give an enhanced item (client 3474) |
| `+0x18` | u64  | to_min_count       | `1` to `10000` (client 3474)                                       |
| `+0x20` | u64  | to_max_count       | `1` to `10000` (client 3474)                                       |
| `+0x28` | u32  | barter_need_point  | `0` on every row (clients 1784 and 3474)                           |
| `+0x2c` | u32  | exchange_max_count | `1` on every row (clients 1784 and 3474)                           |
| `+0x30` | u32  | exchange_min       | `1` on every row (client 3474), `15000` (client 1784)              |
| `+0x34` | u32  | exchange_max       | `1000000` on every row (client 3474)                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 2

### Row (67 bytes)

| Offset  | Type     | Field             | Notes                                              |
| ------- | -------- | ----------------- | -------------------------------------------------- |
| `+0x00` | u16      | barter_region_key |                                                    |
| `+0x02` | u32      | select_rate       |                                                    |
| `+0x06` | Exchange | exchange          |                                                    |
| `+0x3e` | u32      | barter_sub_group  |                                                    |
| `+0x42` | u8       | barter_category   | The category number; `8` on every row (client 1784), as on the material entries of `bartersubgroup.bss`, whose sheet has no category column either |

## Layout 1

The row ends after `barter_sub_group`: there is no `barter_category`.

### Row (66 bytes)

| Offset  | Type     | Field             | Notes |
| ------- | -------- | ----------------- | ----- |
| `+0x00` | u16      | barter_region_key |       |
| `+0x02` | u32      | select_rate       |       |
| `+0x06` | Exchange | exchange          |       |
| `+0x3e` | u32      | barter_sub_group  |       |

## Field Names

The row is the `SpecialBarterData` sheet of a private server's
`DataSheets.bexcel` on client 1784. The client 1784 file holds the 148
sheet rows in sheet order, and these columns match on all 148:
`SelectRate`, `GivedItemKey` with `GivedEnchantLevel` (one packed key),
`GivedMinCount`, `GivedMaxCount`, `TakedItemKey` with `TakedEnchantLevel`,
`TakedMinCount`, `TakedMaxCount`, `ExchangeMin` and `ExchangeMax`. The
sheet's `SpecialBarterIndex` (`1` to `148` in row order) is not stored;
`ContentsGroup` and `TradeEmployeeExp` are not in the file. The Exchange
field names and the `from` and `to` naming are explained in
[`bartersubgroup.bss`](bartersubgroup_bss.md#field-names).

The sheet has no column for `barter_region_key`, `barter_sub_group`,
`barter_category`, `barter_need_point` or `exchange_max_count`. The last two
are Exchange fields and take their names from `bartersubgroup.bss`. The
other three are named after the same slots of
[`barter_normal.bss`](barter_normal_bss.md#field-names), whose entries are
this 70-byte row (67 bytes on client 1784) grouped by region:

- `barter_region_key`: in `barter_normal.bss` the u16 equals the key of the
  region the entry sits in, on all 3,640 + 3,731 entries of client 3474.
- `barter_sub_group`: its values in `barter_normal.bss` are the
  `bartersubgroup.bss` keys, `1` to `197` in the trade item list and `1`
  to `5` in the material list (client 3474), and on client 1784 it matches
  the `BarterSubGroup` column of the `BarterData` and `MaterialBarterData`
  sheets on all 3,240 + 3,321 rows.
- `barter_category`: on client 1784 it matches the `BarterCategory` column
  of the `BarterData` sheet on the 2,958 rows without a sub group; on
  client 3474 it is the bit mask of
  [Barter Categories](bartersubgroup_bss.md#barter-categories).

## Notes

- The special barter window reads the region with
  `specialBarterWrapper:getRegionKey()`, but `barter_region_key` is `0` on
  every row, so the region is not taken from this file.
- The handler (`_bss/barter_special/`) shows one row per offer with its
  place in the file as the index, from `1`, the way the 1784 sheet
  numbers its rows. It reads the Exchange with the shared barter reader in
  `_bss/barter/`.
