# `barter_normal.bss` Format

## Purpose

The barter slots of the Great Ocean barters, per barter region (the
island, port or ship of a [`barter_npclist.bss`](barter_npclist_bss.md)
row). The file holds two lists of regions: the trade item barters (the
`BarterData` sheet of client 1784) and the material barters (the
`MaterialBarterData` sheet). Every region of the first list has 40 slots
and every region of the second 41 (clients 1485 to 3474).

A slot is either an exchange of its own (the item the player hands over,
the item the player gets, their counts and the exchange limits) or a
reference to a sub group of [`bartersubgroup.bss`](bartersubgroup_bss.md)
in the same list, with its own exchange left zero. On client 3474 the two
lists hold 91 regions each, 3,640 and 3,731 slots; 511 trade item slots and
10 material slots name a sub group.

The barter windows read a region's exchanges at run time through
`ToClient_barterWrapper(RegionKey(regionKey))`
(`panel_window_barterinfosearch_2.luac`); see Open Questions.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes   | Records                                 | Row bytes |
| ------ | -------------- | ------- | ------------------- | ------- | --------------------------------------- | --------- |
| 3      | 3002 and later | 3474    | `barter_normal.bss` | 517,086 | 7,371 Exchange, 7,371 Entry, 182 Region | 56        |
| 2      | 1784 to 2519   | 2519    | `barter_normal.bss` | 440,583 | 6,561 Exchange, 6,561 Entry, 162 Region | 56        |
| 1      | 1485           | 1485    | `barter_normal.bss` | 434,022 | 6,561 Exchange, 6,561 Entry, 162 Region | 56        |

| Layout | File                | Known              | Unknown    |
| ------ | ------------------- | ------------------ | ---------- |
| 3      | `barter_normal.bss` | 517,086 B (100.0%) | 0 B (0.0%) |
| 2      | `barter_normal.bss` | 440,583 B (100.0%) | 0 B (0.0%) |
| 1      | `barter_normal.bss` | 434,022 B (100.0%) | 0 B (0.0%) |

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

| File                 | Required | Role                                                                    |
| -------------------- | -------- | ----------------------------------------------------------------------- |
| `barter_npclist.bss` | Optional | The barter NPC of each region key                                       |
| `languagedata_*.loc` | Optional | Region names (type 17), item names (type 0) and barter category names (type 37) |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset                  | Type                          | Field                 | Notes                                                        |
| ----------------------- | ----------------------------- | --------------------- | ------------------------------------------------------------ |
| `+0x00`                 | char[4]                       | magic                 | ASCII `PABR`                                                 |
| `+0x04`                 | u32                           | region_count          | Number of `regions`; `91` on client 3474                     |
| `+0x08`                 | Region[region_count]          | regions               | The trade item barter slots                                  |
| `regions+0x00`          | u32                           | material_region_count | Number of `material_regions`; `91` on client 3474            |
| `regions+0x04`          | Region[material_region_count] | material_regions      | The material barter slots                                    |
| `material_regions+0x00` | String Table                  | string_table          | The PABR string table, present but empty                     |
| `string_table+0x00`     | u32                           | string_table_start    | Absolute offset of `string_count`, where `material_regions` ends |
| `string_table+0x04`     | u32                           | zero                  | Always `0`                                                   |

Both lists hold the 91 region keys of `barter_npclist.bss` once each
(client 3474), in neither key order nor the order of that file, and the two
lists do not share one order.

### Region (variable: 6 bytes + entries)

| Offset  | Type               | Field       | Notes                                                       |
| ------- | ------------------ | ----------- | ----------------------------------------------------------- |
| `+0x00` | u16                | region_key  | `regioninfo.bss` region key; a `barter_npclist.bss` key     |
| `+0x02` | u32                | entry_count | Number of `entries`; `40` in `regions`, `41` in `material_regions` |
| `+0x06` | Entry[entry_count] | entries     | The region's slots; see Entry                               |

### Entry (70 bytes)

The row of [`barter_special.bss`](barter_special_bss.md) has the same
layout.

| Offset  | Type     | Field             | Notes                                                       |
| ------- | -------- | ----------------- | ----------------------------------------------------------- |
| `+0x00` | u16      | barter_region_key | Equals `region_key` on every entry (client 3474)            |
| `+0x02` | u32      | select_rate       | `0` on every sub group entry; see Open Questions            |
| `+0x06` | Exchange | exchange          | All `0` on every sub group entry; see Exchange              |
| `+0x3e` | u32      | barter_sub_group  | A `bartersubgroup.bss` group key in the same list, or `0` for an exchange of the slot's own |
| `+0x42` | u32      | barter_category   | Bit mask as in `bartersubgroup.bss`; `0` on every sub group entry and every material entry (client 3474) |

### Exchange (56 bytes)

Same structure as the Exchange of
[`bartersubgroup.bss`](bartersubgroup_bss.md#exchange-56-bytes). The notes
count the entries without a sub group (client 3474).

| Offset  | Type | Field              | Notes                                                              |
| ------- | ---- | ------------------ | ------------------------------------------------------------------ |
| `+0x00` | u32  | from_item_key      | The item the player hands over, `enchant_level << 24 \| item_id`; level `0` on every entry |
| `+0x04` | u64  | from_min_count     | Fewest of `from_item_key` the exchange asks for                    |
| `+0x0c` | u64  | from_max_count     | Equals `from_min_count` on every entry                             |
| `+0x14` | u32  | to_item_key        | The item the player gets, `enchant_level << 24 \| item_id`; level `0` on every entry |
| `+0x18` | u64  | to_min_count       | Fewest of `to_item_key` the exchange gives                         |
| `+0x20` | u64  | to_max_count       | Most of `to_item_key` the exchange gives                           |
| `+0x28` | u32  | barter_need_point  | `14286` or `21650` in the trade item list, `61430` or `29430` in the material list |
| `+0x2c` | u32  | exchange_max_count | `1` to `10` in the trade item list, `1` to `3` in the material list |
| `+0x30` | u32  | exchange_min       | `0` to `1000000`                                                   |
| `+0x34` | u32  | exchange_max       | `1000000`, or `0` on 410 material entries                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 2

`barter_category` is one byte that holds the category number itself.

### Entry (67 bytes)

| Offset  | Type     | Field             | Notes                                              |
| ------- | -------- | ----------------- | -------------------------------------------------- |
| `+0x00` | u16      | barter_region_key |                                                    |
| `+0x02` | u32      | select_rate       |                                                    |
| `+0x06` | Exchange | exchange          |                                                    |
| `+0x3e` | u32      | barter_sub_group  |                                                    |
| `+0x42` | u8       | barter_category   | The category number: `1` to `7` on the trade item entries without a sub group, `8` on every sub group entry and every material entry (client 1784) |

## Layout 1

The entry ends after `barter_sub_group`: there is no `barter_category`.

### Entry (66 bytes)

| Offset  | Type     | Field             | Notes |
| ------- | -------- | ----------------- | ----- |
| `+0x00` | u16      | barter_region_key |       |
| `+0x02` | u32      | select_rate       |       |
| `+0x06` | Exchange | exchange          |       |
| `+0x3e` | u32      | barter_sub_group  |       |

## Sub Group Entries

On client 3474 the 511 trade item entries with a `barter_sub_group` name
186 of the 197 trade item sub groups, keys `1` to `197`; 9 regions hold
only such entries. The 10 material entries with one sit at slots 6 and 11
of the ship regions `995`, `997`, `999`, `1002` and `1004` and name the
material sub groups `1` to `5`, one per region. A trade item entry names a
group of the first list of `bartersubgroup.bss`, a material entry one of
the second, and every key exists there.

## Field Names

The two lists are the `BarterData` and `MaterialBarterData` sheets of a
private server's `DataSheets.bexcel` on client 1784. Each list holds the
sheet's region keys (`RegionIndex`) once, 81 on client 1784, and a region's
entries are that region's sheet rows in sheet order: matched by region and
place in the region, all 3,240 and 3,321 rows line up. The regions
themselves are in another order than the sheet's.

On the 2,958 trade item rows and 3,316 material rows without a
`BarterSubGroup`, every column matches: `RegionIndex`, `SelectRate`,
`GivedItemKey` with `GivedEnchantLevel` (one packed key), `GivedMinCount`,
`GivedMaxCount`, `TakedItemKey` with `TakedEnchantLevel`, `TakedMinCount`,
`TakedMaxCount`, `BarterNeedPoint`, `ExchangeMaxCount`, `ExchangeMin`,
`ExchangeMax`, `BarterSubGroup` and, in the trade item list,
`BarterCategory`. On the 282 and 5 rows with a `BarterSubGroup`, the
`BarterSubGroup` matches and the file holds `0` in `select_rate` and the
whole Exchange and `8` in `barter_category`, where the sheet fills the
exchange on 120 and 5 of them and leaves `BarterCategory` empty on 162. The
sheet columns `BarterCost`, `ContentsGroup`, `TradeEmployeeExp` and
`BarterTradeExp` are not in the file.

`region_key` and `barter_region_key` both hold the row's `RegionIndex`;
`barter_region_key` takes its name from `barter_npclist.bss`, whose rows
key the same regions. The Exchange field names and the `from` and `to`
naming are explained in
[`bartersubgroup.bss`](bartersubgroup_bss.md#field-names), and the category
values in [Barter Categories](bartersubgroup_bss.md#barter-categories).

## Notes

- On client 3474 the trade item entries without a sub group have one
  category bit set on 2,742 entries and two on 387 (bits 7 and 8 on 369,
  bits 6 and 8 on 18); categories `1` to `9` occur, `10` does not.
- The handler (`_bss/barter_normal/`) shows one row per entry with its
  region's name, the region's NPC from `barter_npclist.bss` and the slot,
  the entry's place in its region from `1`. A sub group entry links to the
  first entry of its group in `bartersubgroup.bss`. The Exchange is read
  with the shared barter reader in `_bss/barter/`, which also walks the two
  lists of `bartersubgroup.bss`.

## Open Questions

### Slot Selection

A region has 40 trade item slots and 41 material slots. The barter windows
read a region's exchanges only through `ToClient_barterWrapper()` and
`ToClient_barterRegionList()`, so which slots a region offers at a time,
and how a sub group entry picks one of its group's exchanges, is not in the
client data read so far. `select_rate` is the lead: `1000000` on 3,084 of the
3,129 trade item slots with an exchange of their own, other values
(`1`, `10000` to `900000`) on 45, and `0` on 1,660 of the 3,721 material
slots with one (client 3474), the same reading as the `select_rate` of
`bartersubgroup.bss` (see its Open Questions).
