# `itemtradegrouptonpc.dbss` Format

## Purpose

Trade goods per trade NPC. The file holds one group per character key of
[`itemtrade.dbss`](itemtrade_dbss.md) (the same 126 keys on client 3464, in another order), and
each group lists items with their trade category. On client 3464 every group
holds one item except 40075 Fish Dad, whose group holds 1,501: trash loot,
fish, trade crates and the old regional trade goods.

```text
40010  Bahar     810442  Fragrant Grape Wine   Luxury
40075  Fish Dad    8201  Mudskipper            Seafood
40075  Fish Dad   55001  Ancient Gold Coin     Relic
```

## Companion Files

None. The handler walks the groups in file order and does not need
`itemtradegrouptonpcoffset.dbss` (see below). NPC names come from LOC type `6`
(`_common/character.py`), item names from LOC type `0`, and the category
names from LOC type `37` under the `RESOURCE` sheet keys listed in
[Commerce Types](#commerce-types).

All multi-byte values are little-endian.

## File Layout

No `PABR` magic and no string table. The groups fill the file to its last
byte.

| Offset  | Type    | Field  | Notes                                     |
| ------- | ------- | ------ | ----------------------------------------- |
| `+0x00` | u32     | count  | Number of groups; `126` on client 3464    |
| `+0x04` | group[] | groups | `count` groups of variable size           |

### Group (6 + 127 * `item_count` bytes)

| Offset  | Type    | Field        | Notes                                  |
| ------- | ------- | ------------ | -------------------------------------- |
| `+0x00` | u16     | character_id | Character key, LOC type `6`            |
| `+0x02` | u32     | item_count   | Number of item entries                 |
| `+0x06` | entry[] | entries      | `item_count` entries of 127 bytes      |

### Item Entry (127 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | character_id  | Repeats the group key                                        |
| `+0x02` | u32  | item_id       | Item key, LOC type `0`; the top byte is `0` in every entry   |
| `+0x06` | u8[] | padding       | 48 bytes, all `0` on client 3464                             |
| `+0x36` | u8   | trade_group_type | `1`, `2`, `3` or `99`, see [Trade Group Types](#trade-group-types) |
| `+0x37` | u8   | unknown_37    | `1` in every entry on client 3464                            |
| `+0x38` | u8[] | padding       | 51 bytes, all `0` on client 3464                             |
| `+0x6B` | u16  | unknown_6b    | `0` or a three-digit code, see Open Questions                |
| `+0x6D` | u8[] | padding       | 15 bytes, all `0` on client 3464                             |
| `+0x7C` | u8   | unknown_7c    | `0`, `3`, `4` or `5`, see Open Questions                     |
| `+0x7D` | u8   | commerce_type | Trade category, see [Commerce Types](#commerce-types)        |
| `+0x7E` | u8   | padding       | `0`                                                          |

### Commerce Types

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

### Trade Group Types

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

## `itemtradegrouptonpcoffset.dbss`

The bare u16 index layout of `petexpoffset.dbss`, read by
`parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type  | Field | Notes                                        |
| ------- | ----- | ----- | -------------------------------------------- |
| `+0x00` | u32   | count | Equals the `itemtradegrouptonpc.dbss` count  |
| `+0x04` | row[] | rows  | `count` 10-byte rows, no trailer             |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                               |
| ------- | ---- | ------------ | --------------------------------------------------- |
| `+0x00` | u16  | character_id | Group key                                           |
| `+0x02` | u32  | offset       | Start of the group header in the data file          |
| `+0x06` | u32  | size         | Whole group: `6 + 127 * item_count`                 |

The index rows are in neither key nor file order; each points at its own
group (`test_every_offset_row_points_at_its_group`).

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
- `itemtradegroupfromnpc.dbss` and its offset table ship empty (see
  [empty](empty_dbss.md)).

## Open Questions

### What unknown_6b Holds

A decimal code: `0`, or hundreds `0` to `7` with the last two digits `11` to
`15` (`11`, `111`, `213`, `515`, `714`). An NPC group and the Fish Dad goods
of the same town share a code: 40010 Bahar (Velia) and Velian Smoked
Chicken, Velian Wine and Velian Plank carry `111`; 41090 Larc and the Fogan
and Glish goods carry `213`. On client 3464, 70 of the 125 one-item groups
carry a code (19 of them `515`) and 142 of the 1,501 Fish Dad entries.
Whether the code is a region, a node or a trade route key is open.

### What unknown_7c Holds

`0` on every one-item group. On the Fish Dad group (client 3464): `3` on the
54 Imperial cooking and alchemy boxes (9801 to 9871), `4` on 108 fish such as
8202 Tuna, and `5` on the six `[Guild]` trade crates. It reads like a
delivery kind (Imperial delivery, Imperial fishing delivery, guild trade),
but no client Lua names the values.

### Why Fish Dad Holds the Shared List

40075 Fish Dad has no `characterfunction.dbss` or `npcsimply.bss` record (see
the `itemtrade.dbss` notes), yet its group holds the trash loot, fish and
crates trade managers take. Whether the client applies this group to every
trade NPC, and whether the one-item groups list goods the NPC buys or sells,
is open.
