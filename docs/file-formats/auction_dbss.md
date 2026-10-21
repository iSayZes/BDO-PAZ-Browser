# `auction.dbss` Format

## Purpose

The static auction table. Each row is one auction: its number, its goods type
(guild house, villa, item, worker and so on, the client's
`CppEnums.AuctionType`), two tick counts, a Korean description and the goods
the auction offers from the start. The guild house and villa auctions list
their houses by character key with a lower price; the masterpiece auctions
(`1001` to `1003`) have room for items with a price, an exhibitor name and a
description, but hold none on client 3474. `auctionoffset.dbss` indexes the
rows by auction number.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records                  | Row bytes                   |
| ------ | -------------- | ------- | -------------------- | ----- | ------------------------ | --------------------------- |
| 2      | 3002 and later | 3474    | `auction.dbss`       | 2,142 | 36 Row, 37 House         | 10                          |
| 2      | 3002 and later | 3474    | `auctionoffset.dbss` | 380   | 36 Index Row             | 10                          |
| 1      | 1485 to 2519   | 2519    | `auction.dbss`       | 7,086 | 7 Item, 40 Row, 37 House | 53 to 2,619, 177 on average |
| 1      | 1485 to 2519   | 2519    | `auctionoffset.dbss` | 420   | 40 Index Row             | 10                          |

| Layout | File                 | Known           | Unknown       |
| ------ | -------------------- | --------------- | ------------- |
| 2      | `auction.dbss`       | 1,854 B (86.6%) | 288 B (13.4%) |
| 2      | `auctionoffset.dbss` | 380 B (100.0%)  | 0 B (0.0%)    |
| 1      | `auction.dbss`       | 6,738 B (95.1%) | 348 B (4.9%)  |
| 1      | `auctionoffset.dbss` | 420 B (100.0%)  | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                          |
| ---------------------------- | -------- | ----------------------------------------------------------------------------- |
| `auctionoffset.dbss`         | Optional | Maps `auction_no` to its row; the main file can be walked without it          |
| `languagedata_en.loc`        | Optional | House names (LOC type 6, keyed by `character_key`) and item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                                   |
| ------- | ---------- | ----- | ------------------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; equals the `auctionoffset.dbss` count   |
| `+0x04` | Row[count] | rows  | See Row; the rows follow each other with no gap          |

### Row (variable: 43 bytes + description, houses and items)

| Offset         | Type               | Field               | Notes                                                                 |
| -------------- | ------------------ | ------------------- | --------------------------------------------------------------------- |
| `+0x00`        | u16                | auction_no          | Unique; equals the offset-table key                                   |
| `+0x02`        | u64                | start_tick_count    | `5,184,000,000` on the house, villa and masterpiece auctions, else `0` (client 3474) |
| `+0x0A`        | u64                | interval_tick_count | `7,776,000,000` where `start_tick_count` is set, else `0` (client 3474) |
| `+0x12`        | str16              | desc_kr             | Korean description, `발렌시아 고급 빌라`; empty on 23 of the 36 rows (client 3474) |
| `desc_kr+0x00` | u8                 | auction_type        | `CppEnums.AuctionType`; see Auction Types                             |
| `desc_kr+0x01` | u32                | unknown_desc_kr_01  | `0` on every row (client 3474); see Open Questions                    |
| `desc_kr+0x05` | u32                | house_count         | Houses the auction starts with; `0` outside types `2` and `6`         |
| `desc_kr+0x09` | House[house_count] | houses              | See House                                                             |
| `houses+0x00`  | u32                | item_count          | `0` on every row (client 3474)                                        |
| `houses+0x04`  | Item[item_count]   | items               | See Item                                                              |
| `items+0x00`   | u32                | unknown_items_00    | `0` on every row (client 3474)                                        |

### House (10 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | The house's character; LOC type 6 names it, `3371` Kunid's Villa      |
| `+0x02` | i64  | lower_price   | `100,000` on every guild house, `1,000,000` on every villa (client 3474) |

### Item (variable: 32 bytes + exhibitor and description text)

On client 3474 no row holds an item. The layout comes from the three items
of auction `1001` on client 1784 (Layout 1).

| Offset                | Type  | Field                     | Notes                                                   |
| --------------------- | ----- | ------------------------- | ------------------------------------------------------- |
| `+0x00`               | u32   | item_key                  | Item ID; `320009` on client 1784                        |
| `+0x04`               | i64   | price                     | `1,000,000,000` on all three items of client 1784       |
| `+0x0C`               | str16 | exhibitor_kr              | Korean exhibitor name, `리베 루쏘` on client 1784        |
| `exhibitor_kr+0x00`   | str16 | description_kr            | Korean item description with `<PAColor>` tags and stored `\n` escapes |
| `description_kr+0x00` | u32   | unknown_description_kr_00 | `0` on all three items of client 1784                   |

### `auctionoffset.dbss`

| Offset              | Type             | Field          | Notes                                               |
| ------------------- | ---------------- | -------------- | --------------------------------------------------- |
| `+0x00`             | char[4]          | magic          | `PABR` (ASCII)                                      |
| `+0x04`             | u32              | count          | Number of index rows; equals the main file's `count` |
| `+0x08`             | Index Row[count] | records        | See Index Row                                       |
| `records+0x00`      | String Table     | string_table   | The 12-byte trailer starts here; see String Table   |
| `string_table+0x00` | u32              | end_of_records | Byte offset of the end of `records` in this file    |
| `string_table+0x04` | u32              | zero           | Always `0`                                          |

### Index Row (10 bytes)

| Offset  | Type | Field      | Notes                                                           |
| ------- | ---- | ---------- | --------------------------------------------------------------- |
| `+0x00` | u16  | auction_no | Equals the row's own `auction_no`                               |
| `+0x02` | u32  | offset     | Byte offset of the row in `auction.dbss`, at its `auction_no`   |
| `+0x06` | u32  | size       | Row byte count, from `auction_no` to the end of `unknown_items_00` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 1

On client 1784 the row holds a territory trade good between `auction_type`
and `unknown_desc_kr_01`: a territory key and its lower price, 10 bytes. The
2016 `gc::AuctionStaticStatus` has the same pair as `_territoryTrade`
(`_territoryKey`, `_lowerPrice`). Only the Row differs from Layout 2.

### Row (variable: 53 bytes + description, houses and items)

| Offset         | Type               | Field                 | Notes                                                        |
| -------------- | ------------------ | --------------------- | ------------------------------------------------------------ |
| `+0x00`        | u16                | auction_no            |                                                              |
| `+0x02`        | u64                | start_tick_count      | `5,184,000,000` on the type `5` rows too                     |
| `+0x0A`        | u64                | interval_tick_count   | `518,400,000` on the type `5` rows                           |
| `+0x12`        | str16              | desc_kr               |                                                              |
| `desc_kr+0x00` | u8                 | auction_type          |                                                              |
| `desc_kr+0x01` | i16                | territory_key         | `0` to `3` on the four type `5` rows (`109`, `119`, `129`, `139`), `-1` on the others |
| `desc_kr+0x03` | i64                | territory_lower_price | `10,000` on the type `5` rows, `0` on the others             |
| `desc_kr+0x0B` | u32                | unknown_desc_kr_01    | `0` on every row                                             |
| `desc_kr+0x0F` | u32                | house_count           |                                                              |
| `desc_kr+0x13` | House[house_count] | houses                |                                                              |
| `houses+0x00`  | u32                | item_count            | `3` on auction `1001`, `0` on the others                     |
| `houses+0x04`  | Item[item_count]   | items                 | Items `320009`, `320010` and `320011` on auction `1001`      |
| `items+0x00`   | u32                | unknown_items_00      | `0` on every row                                             |

## Auction Types

`auction_type` is `CppEnums.AuctionType` in
`luacscript/x64/include/global_define_cpp_enum.luac` on client 3474. The
2016 `gc::AuctionGoodsType` has the same values to `7`, with `5` named
`AuctionGoods_TerritoryTrade`; client 3474 renamed it `AuctionGoods_Temp`
and has no type `5` row. Rows per type on client 3474:

| Value | Name (client 3474)          | Rows | Auctions                                        |
| ----: | --------------------------- | ---: | ----------------------------------------------- |
| 0     | `AuctionGoods_Item`         | 5    | `103`, `113`, `1001` to `1003`                  |
| 1     | `AuctionGoods_WorkerNpc`    | 1    | `140`                                           |
| 2     | `AuctionGoods_House`        | 8    | `101`, `102`, `112`, `122`, `131`, `132`, `141`, `143` |
| 3     | `AuctionGoods_ServantMating` | 10  | `104`, `106`, `114`, `116`, `124`, `126`, `134`, `144`, `154`, `164` |
| 4     | `AuctionGoods_ServantMarket` | 10  | `105`, `107`, `115`, `117`, `125`, `127`, `135`, `145`, `155`, `165` |
| 5     | `AuctionGoods_Temp`         | 0    | Client 1784: `109`, `119`, `129`, `139`         |
| 6     | `AuctionGoods_Villa`        | 1    | `142`                                           |
| 7     | `AuctionGoods_Pet`          | 1    | `207`                                           |
| 8     | `AuctionGoods_ServantRent`  | 0    |                                                 |
| 9     | `AuctionGoods_ServantReturn` | 0   |                                                 |

## Field Names

The names come from two sheets of a private server's `DataSheets.bexcel` on
client 1784, and from the 2016 `gc::AuctionStaticStatus`:

| Field                 | Sheet column                                       | 2016 member          |
| --------------------- | -------------------------------------------------- | -------------------- |
| `auction_no`          | `Auction_InfoTable` `AuctionNo`                    |                      |
| `auction_type`        | `Auction_InfoTable` `AuctionType`                  | `_auctionType`       |
| `start_tick_count`    | `Auction_InfoTable` `AuctionStartCumulatedTickCount` | `_startTickCount`  |
| `interval_tick_count` | `Auction_InfoTable` `AuctionInterval`              | `_intervalTickCount` |
| `desc_kr`             | `Auction_InfoTable` `AuctionDesc`                  | `_auctionDesc`       |
| `character_key`       | `Auction_Table` `Key`                              | `_houseList[]._character` |
| `lower_price`         | `Auction_Table` `Price`                            | `_houseList[]._lowerPrice` |
| `territory_key`       | `Auction_Table` `Key`                              | `_territoryTrade._territoryKey` |
| `territory_lower_price` | `Auction_Table` `Price`                          | `_territoryTrade._lowerPrice` |
| `item_key`, `price`, `exhibitor_kr`, `description_kr` | `Auction_Table` `Key`, `Price`, `Exhibitor`, `Description` | |

`Auction_InfoTable` has 38 rows. The client 1784 file holds the same 38
auctions, and all five columns match on every row. The client 3474 file
shares 34 of them and they match there too; it drops the four type `5` rows
and adds `1002` and `1003`, the two masterpiece auctions `카쿠오의 명품관` and
`파라푸라의 명품관`.

`Auction_Table` lists the goods per `AuctionNo`. Its 37 house and villa rows
are the `houses` of both clients, in the same order and with the same price.
Its four type `5` rows are the `territory_key` and `territory_lower_price` of
client 1784. Its item rows all belong to auction `1001` and carry a
`PA_GAME_SERVICE_TYPE`; client 1784 holds three of them, items `320009` to
`320011` with the exhibitor `리베 루쏘`, and client 3474 none.

## Notes

- Rows are not sorted by `auction_no` in either file, and the two files use
  different orders. Each index row's `offset` points at its row's
  `auction_no` and `size` covers the whole row, so the index rows tile the
  main file from byte 4 to its end.
- Every house `character_key` has a LOC type 6 name on client 3474: auction
  `143` holds the four Cadry guild houses `3351` to `3354`, auction `142` the
  14 Valencia villas `3371` to `3384`.
- The masterpiece auctions are type `0` and the client shows them in
  `panel_masterpiece_auction_all`; the guild house and villa auctions use
  `panel_guildhouse_auction_all` and `panel_villa_auction`, which label the
  house price `LUA_GUILDHOUSE_AUCTION_LOWPRICE`.

## Open Questions

### Tick Count Unit

`start_tick_count` and `interval_tick_count` are `5,184,000,000` and
`7,776,000,000`, which would be 60 and 90 days in milliseconds; the client
1784 type `5` interval `518,400,000` would be 6 days. Neither the unit nor
what the client counts the start from is in the file or the auction Lua.

### Worker List Count

The 2016 `gc::AuctionStaticStatus` holds `_workerList` (character key and
lower price, like a house) before `_houseList`. `unknown_desc_kr_01` sits in
that place and is `0` on every row of both clients, so it may be the worker
list count; with no row holding a worker, its entry layout cannot be read.

### Trailing u32 Fields

`unknown_items_00` after the items and `unknown_description_kr_00` after
each item are `0` wherever they occur. Neither sheet has a column left for
them: the item rows' `PA_GAME_SERVICE_TYPE` is non-zero on every row, so the
item field is not that column.
