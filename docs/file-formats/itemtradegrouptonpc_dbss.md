# `itemtradegrouptonpc.dbss` Format

## Purpose

Trade goods per trade NPC: the goods players sell to the NPC, built from the
server's `SellingToNpc_Table` (see [Field Names](#field-names)). The file holds one group per character key of
[`itemtrade.dbss`](itemtrade_dbss.md) (the same 126 keys on client 3464, in another order), and
each group lists items with their trade category. On client 3464 every group
holds one item except 40075 Fish Dad, whose group holds 1,501: trash loot,
fish, trade crates and the old regional trade goods.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes   | Records                     | Row bytes                  |
| ------ | -------------- | ------- | -------------------------------- | ------- | --------------------------- | -------------------------- |
| 2      | 3473 and later | 3474    | `itemtradegrouptonpc.dbss`       | 207,262 | 1,626 Item Entry, 126 Group | 127                        |
| 2      | 3473 and later | 3474    | `itemtradegrouptonpcoffset.dbss` | 1,264   | 126 Index Row               | 10                         |
| 1      | 1784           | 1784    | `itemtradegrouptonpc.dbss`       | 142,270 | 1,140 Item Entry, 126 Group | 123 to 163, 124 on average |
| 1      | 1784           | 1784    | `itemtradegrouptonpcoffset.dbss` | 1,264   | 126 Index Row               | 10                         |

| Layout | File                             | Known              | Unknown          |
| ------ | -------------------------------- | ------------------ | ---------------- |
| 2      | `itemtradegrouptonpc.dbss`       | 182,872 B (88.2%)  | 24,390 B (11.8%) |
| 2      | `itemtradegrouptonpcoffset.dbss` | 1,264 B (100.0%)   | 0 B (0.0%)       |
| 1      | `itemtradegrouptonpc.dbss`       | 142,270 B (100.0%) | 0 B (0.0%)       |
| 1      | `itemtradegrouptonpcoffset.dbss` | 1,264 B (100.0%)   | 0 B (0.0%)       |

<!-- versions:end -->

## Companion Files

None. The handler walks the groups in file order and does not need
`itemtradegrouptonpcoffset.dbss` (see below). NPC names come from LOC type `6`
(`_common/character.py`), item names from LOC type `0`, and the category
names from LOC type `37` under the `RESOURCE` sheet keys listed in
[Commerce Types](#commerce-types).

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. The groups fill the file to its last
byte.

| Offset  | Type         | Field  | Notes                                  |
| ------- | ------------ | ------ | -------------------------------------- |
| `+0x00` | u32          | count  | Number of groups; `126` on client 3464 |
| `+0x04` | Group[count] | groups | See Group                              |

### Group (variable: 6 bytes + item entries)

| Offset  | Type                   | Field        | Notes                                  |
| ------- | ---------------------- | ------------ | -------------------------------------- |
| `+0x00` | u16                    | character_id | Character key, LOC type `6`            |
| `+0x02` | u32                    | item_count   | Number of item entries                 |
| `+0x06` | Item Entry[item_count] | entries      | See Item Entry                         |

### Item Entry (127 bytes)

| Offset  | Type      | Field                            | Notes                                                              |
| ------- | --------- | -------------------------------- | ------------------------------------------------------------------ |
| `+0x00` | u16       | character_id                     | Repeats the group key                                              |
| `+0x02` | u32       | item_id                          | Item key, LOC type `0`; the top byte is `0` in every entry         |
| `+0x06` | u64       | condition_length                 | `0` in every entry on client 3474: the count of the `condition` string of Layout 1, with no text after it |
| `+0x0E` | i32       | max_price_rate                   | `0` in every entry on client 3474, as is every field up to `trade_group_type` |
| `+0x12` | i32       | event_max_price_rate             |                                                                    |
| `+0x16` | i32       | min_price_rate                   |                                                                    |
| `+0x1A` | i32       | steady_price_rate                |                                                                    |
| `+0x1E` | i32       | vary_amount_rate_per_sell_or_buy |                                                                    |
| `+0x22` | i32       | vary_amount_rate_per_tick        |                                                                    |
| `+0x26` | i32       | event_price_rate_per_tick        |                                                                    |
| `+0x2A` | i32       | price_maintain_tick              |                                                                    |
| `+0x2E` | i64       | steady_price_tick_count          |                                                                    |
| `+0x36` | u8        | trade_group_type                 | `1`, `2`, `3` or `99`, see [Trade Group Types](#trade-group-types) |
| `+0x37` | u8        | is_sell_to_npc                   | `1` in every entry (`test_every_entry_is_sold_to_the_npc`)         |
| `+0x38` | i64       | min_price                        | `0` in every entry on client 3474, as is every field up to `territory_supply_no` |
| `+0x40` | i64       | max_price                        |                                                                    |
| `+0x48` | i64       | buyable_stock_amount_per_tick    |                                                                    |
| `+0x50` | i32       | intimacy_variation               |                                                                    |
| `+0x54` | u8        | is_individual                    |                                                                    |
| `+0x55` | i16       | exploration_point                |                                                                    |
| `+0x57` | i32       | get_exp_rate                     |                                                                    |
| `+0x5B` | i64       | min_stock_amount                 |                                                                    |
| `+0x63` | i64       | max_stock_amount                 |                                                                    |
| `+0x6B` | u16       | territory_supply_no              | `0` or a three-digit code, see Open Questions                      |
| `+0x6D` | bytes[15] | unknown_6d                       | All `0` on client 3474; Layout 1 has 11 bytes here, see [Field Names](#field-names) |
| `+0x7C` | u8        | trade_type                       | The item's `trade_type` in [`itemenchant.dbss`](itemenchant_dbss.md), `0` when it has none (`test_trade_type_is_the_item_trade_type`) |
| `+0x7D` | u8        | commerce_type                    | Trade category, see [Commerce Types](#commerce-types)              |
| `+0x7E` | u8        | price_type                       | The item's price type; `0` in every entry on client 3474           |

### `itemtradegrouptonpcoffset.dbss`

The bare u16 index layout of `petexpoffset.dbss`, read by
`parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type             | Field | Notes                                       |
| ------- | ---------------- | ----- | ------------------------------------------- |
| `+0x00` | u32              | count | Equals the `itemtradegrouptonpc.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row; no trailer                   |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                               |
| ------- | ---- | ------------ | --------------------------------------------------- |
| `+0x00` | u16  | character_id | Group key                                           |
| `+0x02` | u32  | offset       | Start of the group header in the data file          |
| `+0x06` | u32  | size         | Whole group: `6 + 127 * item_count`                 |

The index rows are in neither key nor file order; each points at its own
group (`test_every_offset_row_points_at_its_group`).

## Layout 1

Client 1784 item entries hold a `condition` string at `+0x06`, and the 11
bytes after `territory_supply_no` are 15 bytes on client 3473. On client
1784, 33 entries in 11 groups hold a condition such as
`!checkTerritory(229)`; the other 1,107 hold an empty one, the 8 zero bytes of
`condition_length` in Layout 2. Only the Item Entry differs from Layout 2.

### Item Entry (variable: 123 bytes + condition text)

| Offset           | Type  | Field                            | Notes                                                        |
| ---------------- | ----- | -------------------------------- | ------------------------------------------------------------ |
| `+0x00`          | u16   | character_id                     |                                                              |
| `+0x02`          | u32   | item_id                          |                                                              |
| `+0x06`          | str16 | condition                        | Empty, or `!checkTerritory(N)` with a territory key          |
| `condition+0x00` | i32   | max_price_rate                   | `0` in every entry on client 1784, as is every field up to `trade_group_type` |
| `condition+0x04` | i32   | event_max_price_rate             |                                                              |
| `condition+0x08` | i32   | min_price_rate                   |                                                              |
| `condition+0x0C` | i32   | steady_price_rate                |                                                              |
| `condition+0x10` | i32   | vary_amount_rate_per_sell_or_buy |                                                              |
| `condition+0x14` | i32   | vary_amount_rate_per_tick        |                                                              |
| `condition+0x18` | i32   | event_price_rate_per_tick        |                                                              |
| `condition+0x1C` | i32   | price_maintain_tick              |                                                              |
| `condition+0x20` | i64   | steady_price_tick_count          |                                                              |
| `condition+0x28` | u8    | trade_group_type                 |                                                              |
| `condition+0x29` | u8    | is_sell_to_npc                   | `1` in every entry                                           |
| `condition+0x2A` | i64   | min_price                        | `0` in every entry on client 1784, as is every field up to `territory_supply_no` |
| `condition+0x32` | i64   | max_price                        |                                                              |
| `condition+0x3A` | i64   | buyable_stock_amount_per_tick    |                                                              |
| `condition+0x42` | i32   | intimacy_variation               |                                                              |
| `condition+0x46` | u8    | is_individual                    |                                                              |
| `condition+0x47` | i16   | exploration_point                |                                                              |
| `condition+0x49` | i32   | get_exp_rate                     |                                                              |
| `condition+0x4D` | i64   | min_stock_amount                 |                                                              |
| `condition+0x55` | i64   | max_stock_amount                 |                                                              |
| `condition+0x5D` | u16   | territory_supply_no              |                                                              |
| `condition+0x5F` | u16   | territory_trade_no               | `0` in every entry on client 1784, as is every field up to `trade_type` |
| `condition+0x61` | i32   | get_selling_trade_exp_rate       |                                                              |
| `condition+0x65` | i32   | event_price_rate_per_sell        |                                                              |
| `condition+0x69` | u8    | is_for_magnate                   |                                                              |
| `condition+0x6A` | u8    | trade_type                       |                                                              |
| `condition+0x6B` | u8    | commerce_type                    |                                                              |
| `condition+0x6C` | u8    | price_type                       | `0` in every entry on client 1784                            |

## Field Names

The server dump of a private server on client 1784
(`Instance_dumpFull.exe`) reads the client file into
`ItemTradeGroupStaticStatus` rows of 184 bytes:
`ItemTradeGroupToNpcStaticStatusManager::readFromBinarybyDynamic()` (from VA
`0x140b80e30`) calls the group reader at VA `0x140b7ffa0`, which reads each
entry with the row reader at VA `0x140b7ea70`. The row reader copies the
fields above in file order into members `+0x00` to `+0xb7`. The 2016 client's
debug symbols (`BlackDesert64.pdb`) list the same members in the same order
as `gc::ItemTradeGroupValue` up to `_eventPriceRatePerSell`; that struct also
holds an item pointer and the parsed condition list. The sheet
loader at VA `0x1408b66c0` fills the members from the `SellingToNpc_Table`
sheet, or from `BuyingFromNpc_Table` when its flag argument is set:

| Field                              | Member  | 2016 member                    | Sheet column                 |
| ---------------------------------- | ------- | ------------------------------ | ---------------------------- |
| `character_id`                     | `+0x00` | `_npcKey`                      | `NPCKey`                     |
| `item_id`                          | `+0x04` | `_itemKey`                     | `ItemKey`                    |
| `condition`                        | `+0x08` | `_conditionString`             | `Condition`                  |
| `max_price_rate`                   | `+0x40` | `_maxPriceRate`                | `MaxPriceRate`               |
| `event_max_price_rate`             | `+0x44` | `_eventMaxPriceRate`           | `EvnetMaxPriceRate`          |
| `min_price_rate`                   | `+0x48` | `_minPriceRate`                | `MinPriceRate`               |
| `steady_price_rate`                | `+0x4c` | `_steadyPriceRate`             | `SteadyPriceRate`            |
| `vary_amount_rate_per_sell_or_buy` | `+0x50` | `_varyAmountRatePerSellOrBuy`  | `varyAmountRatePerSellOrBuy` |
| `vary_amount_rate_per_tick`        | `+0x54` | `_varyAmountRatePerTick`       | `varyAmountRatePerTick`      |
| `event_price_rate_per_tick`        | `+0x58` | `_eventvaryAmountRatePerTick`  | `EvnetPriceRatePerTick`      |
| `price_maintain_tick`              | `+0x5c` | `_priceMaintainTick`           | `PriceMaintainTick`          |
| `steady_price_tick_count`          | `+0x60` | `_steadyPriceTickCount`        | `SteadyPriceTickCount`       |
| `trade_group_type`                 | `+0x68` | `_tradeGroupType`              | `TradeGroupType`             |
| `is_sell_to_npc`                   | `+0x69` | `_isSellToNpc`                 | none                         |
| `min_price`                        | `+0x70` | `_minPrice`                    | none                         |
| `max_price`                        | `+0x78` | `_maxPrice`                    | none                         |
| `buyable_stock_amount_per_tick`    | `+0x80` | `_buyableStockAmountPerTick`   | `BuyableStockAmountPerTick`  |
| `intimacy_variation`               | `+0x88` | `_intimacyVariation`           | `IntimacyVariation`          |
| `is_individual`                    | `+0x8c` | `_isIndividual`                | none                         |
| `exploration_point`                | `+0x8e` | `_explorationPoint`            | `ExplorationPoint`           |
| `get_exp_rate`                     | `+0x90` | `_getExpRate`                  | `GetExpRate`                 |
| `min_stock_amount`                 | `+0x98` | `_minStockAmount`              | `MinStockAmount`             |
| `max_stock_amount`                 | `+0xa0` | `_maxStockAmount`              | `MaxStockAmount`             |
| `territory_supply_no`              | `+0xa8` | `_territorySupplyNo`           | `TerritorySupply_No`         |
| `territory_trade_no`               | `+0xaa` | `_territoryTradeNo`            | `TerritoryTrade_No`          |
| `get_selling_trade_exp_rate`       | `+0xac` | `_getSellingTradeExpRate`      | `GetSellingTradeExpRate`     |
| `event_price_rate_per_sell`        | `+0xb0` | `_eventPriceRatePerSell`       | `EventPriceRatePerSell`      |
| `is_for_magnate`                   | `+0xb4` | none                           | `IsForMagnate`               |
| `trade_type`                       | `+0xb5` | none                           | `Item_Table` `TradeType`     |
| `commerce_type`                    | `+0xb6` | none                           | `Item_Table` `CommerceType`  |
| `price_type`                       | `+0xb7` | none                           | `Item_Table` `PriceType`     |

The members without a sheet column are set in code:

- For `SellingToNpc_Table` the loader writes `1` to `is_sell_to_npc` after
  the last column (VA `0x1408b751f`). For both sheets it sets
  `is_individual` when `BuyableStockAmountPerTick` is above `0` (VA
  `0x1408b752d`).
- The loader reads `BuyableStockAmountPerTick`, `IntimacyVariation`,
  `TerritoryTrade_No` and `IsForMagnate` only from `BuyingFromNpc_Table`,
  and `EvnetMaxPriceRate`, `EventPriceRatePerSell`,
  `EvnetPriceRatePerTick`, `ExplorationPoint`, `GetExpRate`,
  `MinStockAmount`, `MaxStockAmount`, `TerritorySupply_No`,
  `GetSellingTradeExpRate` and `TradeGroupType` only from
  `SellingToNpc_Table`.
- After reading the file, the reader calls the function at VA
  `0x140b7f240`, which sets `min_price` and `max_price` from `MinPriceRate`
  and `MaxPriceRate` times the item's `OriginalPrice`, and copies three item
  members into `+0xb5` to `+0xb7`. The `Item_Table` loader writes
  `TradeType` to the item's `+0x40c` (VA `0x140897c4a`), `PriceType` to
  `+0x415` (VA `0x140897dd2`) and `CommerceType` to `+0x419` (VA
  `0x14089848a`). The loader does not read the `commerceType` column of
  `SellingToNpc_Table`.

The names that rest on values:

- `condition`, `trade_group_type` and `territory_supply_no` equal the
  `Condition`, `TradeGroupType` and `TerritorySupply_No` columns of that
  private server's `SellingToNpc_Table` on all 1,140 entries of the official
  client 1784 file, joined on `NPCKey` and `ItemKey`.
- `trade_type` and `commerce_type` equal `TradeType` and `CommerceType` of
  the entry's item in the server's `Item_Table` on all 1,140 entries. On
  client 3474, `trade_type` equals the item's `trade_type` in
  `itemenchant.dbss` on all 1,626 entries.
- `is_sell_to_npc` is `1` in every entry of this file on clients 1784 and
  3474. The same byte is `0` in every entry of the client 1784
  `itemtradegroupfromnpc.dbss`, the table the `BuyingFromNpc_Table` side
  fills.
- On client 3474, the 142 items that carry a `territory_supply_no` on both
  clients carry the same code as on client 1784.

The other fields are `0` in every entry of both clients, so their names rest
on the member order and widths of the row reader alone. Their columns in the
developer sheet (`datasheet_tradedatatable.xlsm`) are server-only (`%`), or
belong to `BuyingFromNpc_Table` only, or the member has no column. In Layout
2, every field up to `territory_supply_no` sits where Layout 1 has it after
an empty `condition`, and the last three bytes keep their order; the names of
the zero fields there rest on that order. Layout 2 has 4 more bytes in
`unknown_6d`, so where `territory_trade_no`, `get_selling_trade_exp_rate`,
`event_price_rate_per_sell` and `is_for_magnate` sit in it is open.

## Commerce Types

`panel_tooltip_item.luac` defines `enCommerceType` and names each value with a
`RESOURCE` sheet key of `stringtable.bss`; the item tooltip adds that name
after `Trade Item`, and the trade market tabs use the same keys. Every
`commerce_type` on client 3464 is `1` to `9`.

| Value | Enum name            | Key                                           | English          |
| ----- | -------------------- | --------------------------------------------- | ---------------- |
| 1     | Luxury_Miscellaneous | `TRADEMARKET_GRAPH_BTN_MISCELL`               | General Goods    |
| 2     | Luxury               | `TRADEMARKET_GRAPH_BTN_LUXURY`                | Luxury           |
| 3     | Grocery              | `TRADEMARKET_GRAPH_BTN_GROCERY`               | Food             |
| 4     | Medicine             | `TRADEMARKET_GRAPH_BTN_MEDICINE`              | Medicine         |
| 5     | MilitarySupplies     | `PANEL_TRADEMARKET_GRAPH_BTN_MILITARYSUPPLIES` | Military Supply  |
| 6     | ObjectSaint          | `TRADEMARKET_GRAPH_BTN_OBJECT`                | Relic            |
| 7     | Cloth                | `PANEL_TRADEMARKET_GRAPH_BTN_CLOTH`           | Clothes          |
| 8     | SeaFood              | `TRADEMARKET_GRAPH_BTN_SEAFOOD`               | Seafood          |
| 9     | RawMaterial          | `PANEL_TRADEMARKET_GRAPH_BTN_RAWMATERIAL`     | Raw Material     |

`10` is `enCommerceType_Max`. The handler stores the key hashes in
`commerce_types.py`, and `test_commerce_type_hashes_match_stringtable` checks
them against `stringtable.bss`.

## Trade Group Types

`trade_group_type` is the code that
[`itemtradeetc.bss`](itemtradeetc_bss.md) pairs for the desert trade buff:
the trade sell list (`panel_dialog_trade_mybasket_all_1.luac`) passes the
trade item's `getTradeGroupType()` and the trade NPC's to
`ToClient_TradeGroupFromToAddPercent` and `ToClient_TradeGroupFromToDistance`,
and `itemtradeetc.bss` holds pairs of exactly these four codes. The client
does not name the codes. On client 3464:

| Code | Entries (client 3464)                                                                    |
| ---- | ---------------------------------------------------------------------------------------- |
| 1    | 122 of the 125 one-item groups; 233 Fish Dad entries, the regional goods 55101 to 55402  |
| 2    | The groups of 45011 Yis Kunjamin and 45012 Burita Allon, the Valencia City trade managers |
| 3    | The group of 45209 Shuriar, the Ibellab Oasis trade manager                              |
| 99   | The other 1,268 Fish Dad entries, such as 55001 Ancient Gold Coin and 8201 Mudskipper    |

Valencia City and Ibellab Oasis are the two places the client's text gives
the desert trade bonus (see the `itemtradeetc.bss` notes).

The labels the tables show with each code (`1 Other Regions`,
`2 Valencia City`, `3 Ibellab Oasis`, `99 Shared Goods`) are our wording, not
the game's: the client has no name for any code. The place names use the
client's words for the two places; `Other Regions` and `Shared Goods` are
ours. The labels live in `_common/lang/` (`tradeGroups`).

## Notes

- On client 3464 the 125 one-item groups hold items from 810442 to 810559,
  and every one of their LOC descriptions ends `This item is currently
  unavailable.` Their names read as variants of the old regional goods in
  the Fish Dad group: 40010 Bahar has 810442 Fragrant Grape Wine, which
  shows the icon of 55102 Velian Wine. Some groups share an item: 810533
  Gem-Laden Dagger sits under 47747 Isobelle Encarotia, 47651 Roig Mills,
  62137 Kario and 45306 Sophia.
- The 40075 Fish Dad group on client 3464, by `commerce_type`: 159 General
  Goods, 75 Luxury, 664 Food, 89 Medicine, 22 Military Supply, 15 Relic, 25
  Clothes, 309 Seafood, 143 Raw Material. It holds 1,481 distinct items: the
  20 items 810560 to 810579 (`Packaged Dried Leaffish` to `Packaged Dried
  Redfin Anthias`) appear twice, byte for byte.
- Its items include 55001 Ancient Gold Coin, whose description reads
  `Trade Managers would buy this for a high price.`, fish such as 8201
  Mudskipper, the Imperial cooking and alchemy boxes (9801 to 9871) and the
  six `[Guild]` trade crates (9921 to 9925 and 9943).
- `trade_type` is `0` on every one-item group. On the Fish Dad group (client
  3464) it is `3` on the 54 Imperial cooking and alchemy boxes, `4` on 108
  fish such as 8202 Tuna and `5` on the six `[Guild]` trade crates; the
  [`itemenchant.dbss`](itemenchant_dbss.md) notes list what each value means.
- `itemtradegroupfromnpc.dbss` and its offset table are empty on client
  3473 and hold groups of this file's Layout 1 shape on client 1784 (see
  [itemtradegroupfromnpc](itemtradegroupfromnpc_dbss.md)).

## Open Questions

### What the territory_supply_no Code Means

The server names the field `TerritorySupply_No` (see
[Field Names](#field-names)). It is a decimal code: `0`, or hundreds `0` to
`7` with the last two digits `11` to `15` (`11`, `111`, `213`, `515`,
`714`). An NPC group and the Fish Dad goods of the same town share a code:
40010 Bahar (Velia) and Velian Smoked Chicken, Velian Wine and Velian Plank
carry `111`; 41090 Larc and the Fogan and Glish goods carry `213`. On client
3464, 70 of the 125 one-item groups carry a code (19 of them `515`) and 142
of the 1,501 Fish Dad entries. The server's `CharacterFunction_Table` names
the NPCs with a `TerritorySupplyName` "황실 납품" (Imperial Delivery) and gives
each a `TerritoryKeyForTerritorySupply` of `0` to `8`. Which territory or
delivery the hundreds digit and the last two digits select is open.

### Why Fish Dad Holds the Shared List

40075 Fish Dad has no `characterfunction.dbss` or `npcsimply.bss` record (see
the `itemtrade.dbss` notes), yet its group holds the trash loot, fish and
crates trade managers take. Whether the client applies this group to every
trade NPC is open.
