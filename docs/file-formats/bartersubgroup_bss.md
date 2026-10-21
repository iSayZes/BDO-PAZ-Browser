# `bartersubgroup.bss` Format

## Purpose

The barter sub groups of the Great Ocean barters: numbered lists of
exchanges, each an item the player hands over, the item the player gets,
their counts, a cost and the exchange limits. An entry of
[`barter_normal.bss`](barter_normal_bss.md) names a sub group in its
`barter_sub_group` u32, the same field this file keys its entries by.

The file holds two lists of groups. The first is the trade item barter
list (the `BarterSubGroup` sheet of client 1784), the second the material
barter list (the `MaterialBarterSubGroup` sheet). On client 3474 the first
list has 197 groups with 731 entries, the second 5 groups with 85 entries;
on client 1784 125 groups with 443 entries and the same 5 groups with 85.
The same split runs through `barter_normal.bss` (two lists of regions) and
[`barterresetoption.bss`](barterresetoption_bss.md), whose
`MaterialBarter` list prices the ship material refreshes.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes  | Records                            | Row bytes |
| ------ | -------------- | ------- | -------------------- | ------ | ---------------------------------- | --------- |
| 3      | 3002 and later | 3474    | `bartersubgroup.bss` | 59,584 | 816 Exchange, 816 Entry, 202 Group | 56        |
| 2      | 1784 to 2519   | 2519    | `bartersubgroup.bss` | 36,976 | 528 Exchange, 528 Entry, 130 Group | 56        |
| 1      | 1485           | 1485    | `bartersubgroup.bss` | 36,448 | 528 Exchange, 528 Entry, 130 Group | 56        |

| Layout | File                 | Known             | Unknown    |
| ------ | -------------------- | ----------------- | ---------- |
| 3      | `bartersubgroup.bss` | 59,584 B (100.0%) | 0 B (0.0%) |
| 2      | `bartersubgroup.bss` | 36,976 B (100.0%) | 0 B (0.0%) |
| 1      | `bartersubgroup.bss` | 36,448 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                 | Required | Role                                                 |
| -------------------- | -------- | ---------------------------------------------------- |
| `languagedata_*.loc` | Optional | Item names (type 0) and barter category names (type 37) |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset                 | Type                         | Field                | Notes                                                          |
| ---------------------- | ---------------------------- | -------------------- | -------------------------------------------------------------- |
| `+0x00`                | char[4]                      | magic                | ASCII `PABR`                                                   |
| `+0x04`                | u32                          | group_count          | Number of `groups`; `197` on client 3474                       |
| `+0x08`                | Group[group_count]           | groups               | The trade item barter sub groups, keys `1` to `group_count` in order |
| `groups+0x00`          | u32                          | material_group_count | Number of `material_groups`; `5` on client 3474                |
| `groups+0x04`          | Group[material_group_count]  | material_groups      | The material barter sub groups, keys `1` to `material_group_count` in order |
| `material_groups+0x00` | String Table                 | string_table         | The PABR string table, present but empty                       |
| `string_table+0x00`    | u32                          | string_table_start   | Absolute offset of `string_count`, where `material_groups` ends |
| `string_table+0x04`    | u32                          | zero                 | Always `0`                                                     |

### Group (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                                    |
| ------- | ------------------ | ----------- | -------------------------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; `2` to `60` on client 3474          |
| `+0x04` | Entry[entry_count] | entries     | See Entry; every entry of a group holds the group's key  |

### Entry (72 bytes)

| Offset  | Type     | Field            | Notes                                                                 |
| ------- | -------- | ---------------- | --------------------------------------------------------------------- |
| `+0x00` | u32      | barter_sub_group | The group key: the group's place in its list, from `1`                |
| `+0x04` | u32      | select_rate      | `1000000` on every entry (client 3474)                                |
| `+0x08` | u32      | barter_cost      | `2` to `68` in the trade item list, `15` in the material list (client 3474) |
| `+0x0c` | Exchange | exchange         | See Exchange                                                          |
| `+0x44` | u32      | barter_category  | Bit mask, bit N set for category N of Barter Categories; `0` on every material entry |

### Exchange (56 bytes)

The part every barter row shares: the same 56 bytes sit in the rows of
[`barter_special.bss`](barter_special_bss.md) and the entries of
[`barter_normal.bss`](barter_normal_bss.md).

| Offset  | Type | Field              | Notes                                                                  |
| ------- | ---- | ------------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32  | from_item_key      | The item the player hands over, `enchant_level << 24 \| item_id`       |
| `+0x04` | u64  | from_min_count     | Fewest of `from_item_key` the exchange asks for                        |
| `+0x0c` | u64  | from_max_count     | Most of `from_item_key` the exchange asks for                          |
| `+0x14` | u32  | to_item_key        | The item the player gets, `enchant_level << 24 \| item_id`             |
| `+0x18` | u64  | to_min_count       | Fewest of `to_item_key` the exchange gives                             |
| `+0x20` | u64  | to_max_count       | Most of `to_item_key` the exchange gives                               |
| `+0x28` | u32  | barter_need_point  | `14286` or `21650` in the trade item list, `21650` or `29430` in the material list (client 3474) |
| `+0x2c` | u32  | exchange_max_count | How many times the exchange can be made; `1` to `6` (client 3474)      |
| `+0x30` | u32  | exchange_min       | `0` to `20471` in the trade item list, `0` in the material list (client 3474); see Open Questions |
| `+0x34` | u32  | exchange_max       | `1000000` on every entry (client 3474)                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 2

`barter_category` is one byte that holds the category number itself.

### Entry (69 bytes)

| Offset  | Type     | Field            | Notes                                                     |
| ------- | -------- | ---------------- | --------------------------------------------------------- |
| `+0x00` | u32      | barter_sub_group |                                                           |
| `+0x04` | u32      | select_rate      |                                                           |
| `+0x08` | u32      | barter_cost      |                                                           |
| `+0x0c` | Exchange | exchange         |                                                           |
| `+0x44` | u8       | barter_category  | The category number: `5`, `6` or `7` in the trade item list, `8` on every material entry (client 1784) |

## Layout 1

The entry ends after the Exchange: there is no `barter_category`.

### Entry (68 bytes)

| Offset  | Type     | Field            | Notes |
| ------- | -------- | ---------------- | ----- |
| `+0x00` | u32      | barter_sub_group |       |
| `+0x04` | u32      | select_rate      |       |
| `+0x08` | u32      | barter_cost      |       |
| `+0x0c` | Exchange | exchange         |       |

## Barter Categories

The Barter information window (`panel_window_barterinfosearch.luac`,
client 3474) filters by `__eBarterCategory_*`, labelled with the GAME sheet
keys `LUA_BARTER_NEW_FILTER_*`. The Lua names the values but not their
numbers; the numbers below follow from the window and the data:
`getSelectCategoryIndex()` in `panel_window_barterinfosearch_1.luac` returns
the drop-down index plus 1 for the first five entries and maps a pick past
`__eBarterCategory_Ocean` to `__eBarterCategory_Count` when the old list of
eight shows, so Ocean is `8`. The client 3474 masks confirm `5`, `6`, `7` and
`10` by their items: bit 5 entries trade `[Level 4]` items for `[Level 5]`
items, bit 6 entries trade trade items for other items (Tidal Black Stone,
Oquilla's Flower), bit 7 entries give Crow Coins (`10`), and bit 10 entries
trade `[Level 6]` items for `[Level 7]` items. On client 1784 the same
entries hold `5`, `6` and `7` as plain numbers.

| Value | Lua name                            | GAME key                   | English (client 3474) | Entries with the bit (client 3474) |
| ----- | ----------------------------------- | -------------------------- | --------------------- | ---------------------------------- |
| `1`   | `__eBarterCategory_NormalToLevel1`  | `LUA_BARTER_NEW_FILTER_1`  | Normal -> Lv. 1       | 0                                  |
| `2`   | `__eBarterCategory_Level1ToLevel2`  | `LUA_BARTER_NEW_FILTER_2`  | Lv. 1 -> Lv. 2        | 0                                  |
| `3`   | `__eBarterCategory_Level2ToLevel3`  | `LUA_BARTER_NEW_FILTER_3`  | Lv. 2 -> Lv. 3        | 0                                  |
| `4`   | `__eBarterCategory_Level3ToLevel4`  | `LUA_BARTER_NEW_FILTER_4`  | Lv. 3 -> Lv. 4        | 0                                  |
| `5`   | `__eBarterCategory_Level4ToLevel5`  | `LUA_BARTER_NEW_FILTER_5`  | Lv. 4 -> Lv. 5        | 120                                |
| `6`   | `__eBarterCategory_NormalBarter`    | `LUA_BARTER_NEW_FILTER_6`  | Normal Barter         | 197                                |
| `7`   | `__eBarterCategory_CrowCoin`        | `LUA_BARTER_NEW_FILTER_7`  | Crow Coin             | 126                                |
| `8`   | `__eBarterCategory_Ocean`           | `LUA_BARTER_NEW_FILTER_9`  | Ocean Barter          | 0                                  |
| `9`   | `__eBarterCategory_Level5ToLevel6`  | `LUA_BARTER_NEW_FILTER_10` | Lv. 5 -> Lv. 6        | 0                                  |
| `10`  | `__eBarterCategory_Level6ToLevel7`  | `LUA_BARTER_NEW_FILTER_11` | Lv. 6 -> Lv. 7        | 288                                |

`__eBarterCategory_Count` is the "All Barters" pick (`LUA_BARTER_NEW_FILTER_8`).
Every trade item entry of client 3474 has exactly one bit set.

## Field Names

The entry is the `BarterSubGroup` sheet of a private server's
`DataSheets.bexcel` on client 1784, and the material list its
`MaterialBarterSubGroup` sheet. The client 1784 file holds the 443 and 85
sheet rows in sheet order, and every column matches on all of them:
`BarterSubGroup`, `SelectRate`, `BarterCost`, `GivedItemKey` with
`GivedEnchantLevel` (one packed key), `GivedMinCount`, `GivedMaxCount`,
`TakedItemKey` with `TakedEnchantLevel`, `TakedMinCount`, `TakedMaxCount`,
`BarterNeedPoint`, `ExchangeMaxCount`, `ExchangeMin`, `ExchangeMax` and, in
the trade item list, `BarterCategory`. The material sheet has no
`BarterCategory` column; its entries hold `8` on client 1784 and `0` on
client 3474. The sheet columns `ContentsGroup`, `TradeEmployeeExp` and
`BarterTradeExp` are not in the file.

`SelectRate` and `ExchangeMax` are `1000000` on every row of the sheet, so
the sheet alone does not tell them apart. The `SpecialBarterData` sheet
does: there `SelectRate` is `0` and `ExchangeMax` holds two values, and they
match the u32 before the Exchange and the last u32 of the Exchange of
[`barter_special.bss`](barter_special_bss.md) on 148 of 148 rows.

On client 3474 the sheet rows that share a group key and place in the group
match as follows (443 rows of the first list, 85 of the second):

| Field              | Column             | Trade item list | Material list |
| ------------------ | ------------------ | --------------- | ------------- |
| barter_sub_group   | `BarterSubGroup`   | 443             | 85            |
| select_rate        | `SelectRate`       | 443             | 85            |
| barter_cost        | `BarterCost`       | 406             | 85            |
| from_item_key      | `GivedItemKey`     | 400             | 12            |
| from_min_count     | `GivedMinCount`    | 435             | 85            |
| from_max_count     | `GivedMaxCount`    | 435             | 85            |
| to_item_key        | `TakedItemKey`     | 392             | 85            |
| to_min_count       | `TakedMinCount`    | 392             | 12            |
| to_max_count       | `TakedMaxCount`    | 392             | 12            |
| barter_need_point  | `BarterNeedPoint`  | 443             | 18            |
| exchange_max_count | `ExchangeMaxCount` | 273             | 85            |
| exchange_min       | `ExchangeMin`      | 427             | 85            |
| exchange_max       | `ExchangeMax`      | 443             | 85            |

The material list has the sheet's group sizes, `10, 20, 15, 20, 20`, and
holds other items: client 3474 asks for `[Level 4]` items (Marine Knights'
Helm `800043` onwards) where the sheet asks for `[Level 5]` ones (`800057`
onwards), for 360 to 440 Crow Coins in place of 120 to 145.

`from_*` and `to_*` follow the client Lua: the barter windows read the
exchange with `getFromItemEnchantKey()`, `getFromItemCount()`,
`getToItemEnchantKey()` and `getToItemCount()`, and
`panel_window_barterinfosearch_special_1.luac` shows the from item under
`Static_MyItemBG` (the player's item) and the to item under
`Static_TakeItemBG`. The sheet's `Gived` is the from item and `Taked` the
to item: the 1784 special barter row `1` hands over Gold Bar 1,000G (`5`)
for item `45505`. `exchange_max_count` is the
`getExchangeMaxCount()` of the same wrappers.

## Notes

- The keys of the first list run `1` to `197` and those of the second `1`
  to `5` on client 3474; the entries of `barter_normal.bss` name keys `1`
  to `197` in its trade item list and `1` to `5` in its material list (see
  its [Sub Group Entries](barter_normal_bss.md#sub-group-entries)).
- Item keys pack the enhancement level like
  [`itemenchant.dbss`](itemenchant_dbss.md); the from items are level `0`
  on every entry (client 3474).
- The handler (`_bss/bartersubgroup/`) shows one row per entry, with a
  Material flag on the entries of the second list. It reads the Exchange
  and walks the two lists with the shared barter reader in `_bss/barter/`,
  which `barter_special.bss` and `barter_normal.bss` use too, and names the
  categories with their LOC type 37 GAME text. Each entry carries
  `sub_group_ref` (`trade:12`, `material:3`), the field the
  `barter_normal.bss` sub group links open it by.

## Open Questions

### Exchange Min and Max

`exchange_min` and `exchange_max` are the sheet's `ExchangeMin` and
`ExchangeMax`. `exchange_max` is `1000000` on every entry. On client 3474
220 of the 731 trade item entries hold an `exchange_min` of 10 times a
power of 2 less 9 (`11`, `31`, `71`, ... `2551`, `5111`, `10231`,
`20471`), 203 a round number (`6`, `10`, `20`, `100`, `3000`, `5000`,
`8000`, `10000`, `20000`) and 308 `0`. The doubling steps look like the
parley a barter costs, but the Lua
reads the parley through `getExchangeCountForTime()` and nothing in the
barter windows reads a minimum or maximum. What the two bound is not in the
client data read so far.

### Barter Need Point and Select Rate

`barter_need_point` (`14286`, `21650` or `29430`) and `select_rate`
(`1000000`) are read by no Lua function of the barter windows. A lead for
`select_rate`: a weight in millionths for picking one entry of the group,
as `CppDefine.e1Percent` is `10000` and `1000000` is then 100%.
