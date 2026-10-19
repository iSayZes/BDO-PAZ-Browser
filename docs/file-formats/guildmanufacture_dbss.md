# `guildmanufacture.dbss` Format

## Purpose

The Guild Crafting recipes: one row per product item a guild can craft in
the Guild Crafting window, with its `itemexchangesource.bss` key, the six
required item slots and their counts, the product window category, the guild
houses that can craft it and the guild skill it needs. The client Lua reads
a row through `ToClient_GetGuildManufactureStaticStatusWrapper(itemEnchantKey)`
with the product item key. `guildmanufactureoffset.dbss` is the index into
it, keyed by the product item key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records       | Row bytes                  |
| ------ | -------------- | ------- | ----------------------------- | ----- | ------------- | -------------------------- |
| 2      | 3474 and later | 3474    | `guildmanufacture.dbss`       | 2,120 | 16 Row        | 125 to 163, 132 on average |
| 2      | 3474 and later | 3474    | `guildmanufactureoffset.dbss` | 196   | 16 Offset Row | 12                         |
| 1      | 1784           | 1784    | `guildmanufacture.dbss`       | 2,251 | 17 Row        | 123 to 161, 132 on average |
| 1      | 1784           | 1784    | `guildmanufactureoffset.dbss` | 208   | 17 Offset Row | 12                         |

| Layout | File                          | Known            | Unknown    |
| ------ | ----------------------------- | ---------------- | ---------- |
| 2      | `guildmanufacture.dbss`       | 2,120 B (100.0%) | 0 B (0.0%) |
| 2      | `guildmanufactureoffset.dbss` | 196 B (100.0%)   | 0 B (0.0%) |
| 1      | `guildmanufacture.dbss`       | 2,251 B (100.0%) | 0 B (0.0%) |
| 1      | `guildmanufactureoffset.dbss` | 208 B (100.0%)   | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                 |
| ----------------------------- | -------- | -------------------------------------------------------------------- |
| `guildmanufactureoffset.dbss` | Optional | `product_item_key -> (data_offset, data_size)` index; the rows carry their own counts and can be walked without it |
| `languagedata_en.loc`         | Optional | Item names (type `0`), guild skill names (type `10`), guild house names (type `6`), exchange names (type `24`) and the category titles (type `37`, `GAME` sheet) |
| `itemexchangesource.bss`      | Optional | The exchange each row names. The handler reads the exchange name from the `EXCHANGE_NAME_KR` lookup index (see `docs/handler.md`), shows `[Guild] Ship License: Galley (7901)` in the Exchange Key column and links it to the exchange's row; it does not open the file |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `16` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 117 bytes + guild house keys)

| Offset                  | Type                   | Field                | Notes                                                        |
| ----------------------- | ---------------------- | -------------------- | ------------------------------------------------------------ |
| `+0x00`                 | u32                    | product_item_key     | Item key (`enchant_level << 24 \| item_id`) of the product; the index key, unique per row |
| `+0x04`                 | u32                    | exchange_item_key    | [`itemexchangesource.bss`](itemexchangesource_bss.md) key the product slot's tooltip reads (`getExchangeKey()`); `7901` to `7932` and `9773` to `9776` on client 3474, all 16 `exchange_type` 8 (GuildHouseLargeCraft) rows |
| `+0x08`                 | u32                    | product_item_key_dup | Equal to `product_item_key` in every row                     |
| `+0x0C`                 | u64                    | time                 | `43200`, `72000` or `86400` on client 3474; the unit is an In-Game Check |
| `+0x14`                 | u64                    | price                | `10000` in every row of clients 1784 and 3474; see Open Questions |
| `+0x1C`                 | u64                    | product_item_limit   | `1` or `2` on client 3474                                    |
| `+0x24`                 | u32[6]                 | required_item_keys   | Item keys of the six material slots (`getRequiredItemEnchantKey(i)`); filled from slot 0, `0` for an empty slot |
| `+0x3C`                 | u64[6]                 | required_item_counts | Count per slot for one product (`getRequiredItemCount(i)`); `0` for an empty slot |
| `+0x6C`                 | u8                     | category             | Product window category, see Categories                     |
| `+0x6D`                 | u32                    | guild_house_count    | Number of `guild_house_keys`; `4`, `8` or `23` on client 3474 |
| `+0x71`                 | u16[guild_house_count] | guild_house_keys     | Character keys of the guild houses that can craft the product, ascending |
| `guild_house_keys+0x00` | u32                    | skill_key            | Guild skill the guild needs, `skill_no << 16 \| level`; level `1` in every row |

The rows are not sorted by key.

### `guildmanufactureoffset.dbss`

| Offset  | Type              | Field | Notes                                     |
| ------- | ----------------- | ----- | ----------------------------------------- |
| `+0x00` | u32               | count | Equals the `guildmanufacture.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row      |

### Offset Row (12 bytes)

| Offset  | Type | Field            | Notes                                                    |
| ------- | ---- | ---------------- | -------------------------------------------------------- |
| `+0x00` | u32  | product_item_key | `product_item_key` of the row                            |
| `+0x04` | u32  | data_offset      | Row start + 4, at `exchange_item_key`                    |
| `+0x08` | u32  | data_size        | Row size - 4: `117 + 2 * guild_house_count - 4`          |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key and covers the rest of it.

## Layout 1

### Row (variable: 115 bytes + guild house keys)

| Offset                  | Type                   | Field                | Notes                                  |
| ----------------------- | ---------------------- | -------------------- | -------------------------------------- |
| `+0x00`                 | u32                    | product_item_key     |                                        |
| `+0x04`                 | u16                    | exchange_item_key    | Two bytes here, four in Layout 2       |
| `+0x06`                 | u32                    | product_item_key_dup |                                        |
| `+0x0A`                 | u64                    | time                 |                                        |
| `+0x12`                 | u64                    | price                |                                        |
| `+0x1A`                 | u64                    | product_item_limit   |                                        |
| `+0x22`                 | u32[6]                 | required_item_keys   |                                        |
| `+0x3A`                 | u64[6]                 | required_item_counts |                                        |
| `+0x6A`                 | u8                     | category             |                                        |
| `+0x6B`                 | u32                    | guild_house_count    |                                        |
| `+0x6F`                 | u16[guild_house_count] | guild_house_keys     |                                        |
| `guild_house_keys+0x00` | u32                    | skill_key            |                                        |

Every row is 2 bytes shorter than in Layout 2, and the index's `data_size`
is `115 + 2 * guild_house_count - 4`. Client 1784 has 17 rows. Client 3474
drops `50007` ([Guild] Registration: Valencia Elephant) and the four "for
Combat" elephant items `59002`, `59102`, `59202` and `59302` (Steel Mask,
Steel Armor, Silk Saddle, Silk Stirrups), and adds the four Improved Galley
parts `49794` to `49797`.

## Categories

The product window (`panel_guild_manufactureselect_all.luac`) groups the
products by `getCategoryNo()` and titles each group with a `GAME` sheet key.
The fourth group exists only when the client's `_ContentsGroup_SummonGuildDrill`
is set, and its key skips `CATEGORY3`.

| Value | `GAME` key                               | Title (client 3474)      | Rows (client 3474) |
| ----- | ---------------------------------------- | ------------------------ | ------------------ |
| `0`   | `LUA_GUILD_MANUFACTURE_SELECT_CATEGORY0` | License and Registration | 2                  |
| `1`   | `LUA_GUILD_MANUFACTURE_SELECT_CATEGORY1` | Mount Equipment          | 12                 |
| `2`   | `LUA_GUILD_MANUFACTURE_SELECT_CATEGORY2` | Mount Recovery           | 2                  |
| `3`   | `LUA_GUILD_MANUFACTURE_SELECT_CATEGORY4` | Resource Gathering Tool  | 0                  |

## Field Names

The row is the `GuildManufactureInfo` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched by `ProductItemNo`. The 2016
client has no guild crafting structure, so the names come from the sheet
columns and the Lua getters.

| Field                | Column                       | Same value (client 1784) | Same value (client 3474) |
| -------------------- | ---------------------------- | ------------------------ | ------------------------ |
| product_item_key     | `ProductItemNo`              | 17 of 17 rows            | 12 of 16 rows            |
| exchange_item_key    | `ExchangeItemKey`            | 17 of 17                 | 12 of 12                 |
| category             | `CategoryNo`                 | 17 of 17                 | 12 of 12                 |
| guild_house_keys     | `GuildHouse`                 | 17 of 17, as a set       | 12 of 12, as a set       |
| skill_key            | `SkillNo1` (the skill_no half) | 17 of 17               | 12 of 12                 |
| required_item_keys   | `RequiredItemNo0` to `5`     | 17 of 17                 | 6 of 12                  |
| required_item_counts | `RequiredItemCount0` to `5`  | 17 of 17                 | 2 of 12                  |
| time                 | `Time`                       | 17 of 17                 | 12 of 12                 |
| price                | `Price`                      | 17 of 17                 | 12 of 12                 |
| product_item_limit   | `ProductItemLimit`           | 17 of 17                 | 12 of 12                 |

The four Improved Galley rows of client 3474 (`49794` to `49797`) are not
in the sheet. Of the 12 shared rows, five dropped their last material
(`54026` and the galley parts `49709` to `49712`), `50119` needs `9916` in
place of `50007` in slot 1, and the four Capotia rows keep their items with
new counts. The sheet lists `GuildHouse` with `2569` after
`2691`; the file stores the keys ascending. An empty sheet cell is `0` in
the file. The sheet's `ContentsOption` column has no field: the 13 sheet
rows missing from client 1784 are the rows whose option is `1000`, `1449` or
`1636`.

## Notes

- The Guild Crafting window (`panel_guild_manufacture_all_1.luac`) shows
  `__eGuildManufactureRequiredItemCount` material slots per product. For a
  slot it reads the key from the guild's current crafting job and the count
  of one product from this file, multiplied by the job's product count.
- The guide text `LUA_GUILD_MANUFACTURE_NOTICE_INFORMATION` says a guild
  needs a guild house that can craft the item, won at the guild house
  auction, and the guild skill needed for it; these are `guild_house_keys`
  and `skill_key`.
- On client 3474 the guild house lists are three sets: `2110`, `2140`,
  `2880`, `2905` (Velia, Olvia, Altinova Guild House 1 and 2) for the galley
  rows, `3351` to `3358` (Cadry, Pujiya and the other Valencia guild houses)
  for the elephant rows, and all 23 for the two Mount Recovery rows.
- The guild skills on client 3474 are `65042` and `65043` (Building Boat Lv.
  1 and 2), `65052` and `65053` (Monstrous Force Lv. 1 and 2) and `65059`
  (Fully Prepared). The level in the skill name belongs to the skill number;
  the key's level half is `1`.
- No decompiled guild crafting Lua reads `product_item_limit`. The `GAME`
  key `LUA_GUILD_MANUFACTURE_COUNT_LIMIT` reads "Daily Crafting Limit:
  {itemLimit}" on client 3474.

## Open Questions

### What price Is

`price` is `10000` in every row of both clients and matches the sheet's
`Price` column. The Complete Now cost the window shows
(`FromClient_Guild_Manufacture_All_CompletePrice`) comes from the server as
`price_s64`, so the Lua does not show whether this is the start cost, the
Complete Now cost or something else.

## In-Game Checks

### Unit of time

Needs item: the materials of [[Guild] Galley: Cloud Breeze Sail](https://bdocodex.com/us/item/49712/)

Needs zone: a Velia, Olvia or Altinova guild house that your guild holds

Needs skill: guild skill Building Boat Lv. 2

1. Open the Guild Crafting window of that guild house.
2. Select [Guild] Galley: Cloud Breeze Sail and start crafting.
3. Read the finish time the window shows (Processing will finish on ...).

A finish time 20 hours after the start means `time` is seconds (`72000`).

### Daily Crafting Limit

Needs zone: a guild house with a Guild Crafting window that your guild holds

1. Open the Guild Crafting window of that guild house.
2. Select each item in the list and read the "Daily Crafting Limit" line.

A limit equal to the row's `product_item_limit` (`1` or `2` on client 3474)
confirms the field name.
