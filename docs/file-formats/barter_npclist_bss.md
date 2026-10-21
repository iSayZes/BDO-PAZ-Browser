# `barter_npclist.bss` Format

## Purpose

Lists the barter NPCs of the Great Ocean: one row per barter region (the island, port or ship where the barter happens) with the NPC who trades there. The barter windows key everything by that region key (`ToClient_barterWrapper(RegionKey(regionKey))` in `panel_window_barterinfosearch_2.luac`), so this table is what ties a barter region to its NPC.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 1485 and later | 3474    | `barter_npclist.bss` | 384   | 91 Row  | 4         |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 1      | `barter_npclist.bss` | 384 B (100.0%) | 0 B (0.0%) |

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

| File                  | Required | Role                                          |
| --------------------- | -------- | --------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names (type 17) and NPC names (type 6) |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                                                    |
| ------------------- | ----------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                           |
| `+0x04`             | u32               | record_count       | `91` on client 3464                                      |
| `+0x08`             | Row[record_count] | records            | See Row                                                  |
| `records+0x00`      | String Table      | string_table       | The PABR string table, present but empty                 |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 4 × count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                               |

The file is `8 + 4 × 91 + 12 = 384` bytes on client 3464. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (4 bytes)

| Offset  | Type | Field             | Notes                                                                 |
| ------- | ---- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | barter_region_key | `regioninfo.bss` region key; unique                                   |
| `+0x02` | u16  | character_id      | The barter NPC; unique, and its `characterfunction.dbss` record has a Maritime Trade button |

Rows are in neither key nor character order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Notes

- On client 3464 the `maritime_trade` slot of [`characterfunction.dbss`](characterfunction_dbss.md) stores the same key as `barter_region_key` for all 91 characters, and those 91 are the only characters with a non-zero `barter_region_key`.
- The regions (client 3464): 70 islands, Arehaza, 8 coastal ports (Olvia Coast, Epheria Sentry Post, Sausan Garrison Wharf, Grándiha, Starry Midnight Port, Sanctuary Coastal Outpost, Dallae Pier, Crow's Nest) and 12 ship regions. Lema Island, Iliya Island and Arehaza are `MinorTown`, the others `Hunting`. The ship regions belong to characters 50814 to 50827 (Crow Merchants' Vessel, Old Moon Guild's Carrack, Wandering Merchant's Ship, Cholace Chico's Pirate Union and eight wrecks and rafts). The 12 ship regions are the only ones with `regioninfo.bss` `is_ocean` set.
- The other barter tables are [barter_normal](barter_normal_bss.md), [barter_special](barter_special_bss.md), [bartersubgroup](bartersubgroup_bss.md), [barterlifelevelinfo](barterlifelevelinfo_bss.md) and [barterresetoption](barterresetoption_bss.md). Both region lists of `barter_normal.bss` hold the 91 region keys of this file (client 3474).
