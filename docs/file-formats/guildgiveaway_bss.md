# `guildgiveaway.bss` Format

## Purpose

The items of each Guild Giveaway, the Pearl Shop gift a player buys for
their guild (Button_GuildPearlReward in the guild window): one row per
giveaway key with the items each guild member can collect. On client 3474
the file has 3 rows, keys `10`, `9` and `8`, each with one box
(`[Kind Gesture] Blacksmith's Workshop Box`, `[Kind Gesture] Hero's
Blessing Box` and `Choose Your Spotlight Dance Box`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `guildgiveaway.bss` | 80    | 3 Item, 3 Row | 12        |

| Layout | File                | Known         | Unknown    |
| ------ | ------------------- | ------------- | ---------- |
| 1      | `guildgiveaway.bss` | 80 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                       |
| --------------------- | -------- | -------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `0` on clients 1784 to 3002   |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 8 bytes + items)

| Offset  | Type                   | Field        | Notes                                                       |
| ------- | ---------------------- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32                    | giveaway_key | Row key; the `getKeyRaw()` of a giveaway in the Lua          |
| `+0x04` | u32                    | entry_count  | Number of items; `1` on every row (client 3474)              |
| `+0x08` | Item[entry_count]      | items        | See Item                                                    |

### Item (12 bytes)

| Offset  | Type | Field       | Notes                                                                       |
| ------- | ---- | ----------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key    | `enchant_level << 24 \| item_id`, the key of [itemenchant](itemenchant_dbss.md); every level is `0` (client 3474) |
| `+0x04` | u64  | item_count  | Number of items; `1` on every row (client 3474)                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 covers
the file; client 1784 ships it with 0 rows. The names follow the client Lua
of client 3474 (`panel_ingamecashshop_guildgiveaway_all_1.luac`): a
giveaway reads its row with `dataWrapper:getKeyRaw()`, then
`ToClient_getGuildGiveawaySelectedListSize(keyRaw)`, and per entry
`ToClient_getGuildGiveawaySelectedItemEnchantKey(keyRaw, i)` (passed to
`getItemEnchantStaticStatus`, so an item key with its level) and
`ToClient_getGuildGiveawaySelectedItemCount(keyRaw, i)`, a 64-bit count.
The window shows one item when the list holds one entry and a list
otherwise.

## Notes

- Client 1784, 2107, 2519 and 3002 ship the file with 0 rows (20 bytes);
  client 3251 has one row (key `8`, Choose Your Spotlight Dance Box), client
  3474 three.
- The giveaway window shows only with the `_ContentsGroup_GuildGiveaway`
  content flag, and says `LUA_GUILDGIVEAWAY_NO_REWARD` when the guild has
  no giveaway to collect.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`: the key and each item with its name
  and count.
