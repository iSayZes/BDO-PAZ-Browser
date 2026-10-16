# `barter_npclist.bss` Format

## Purpose

Lists the barter NPCs of the Great Ocean: one row per barter region (the island, port or ship where the barter happens) with the NPC who trades there. The barter windows key everything by that region key (`ToClient_barterWrapper(RegionKey(regionKey))` in `panel_window_barterinfosearch_2.luac`), so this table is what ties a barter region to its NPC.

Example:

```text
region 572  Portanen Island     -> NPC 58947 Supio
region 181  Lema Island         -> NPC 58954 Chikao
region 998  Crow Merchants' Vessel -> NPC 50818 Olcia Viano
```

## Companion Files

| File                  | Required | Role                                          |
| --------------------- | -------- | --------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names (type 17) and NPC names (type 6) |

All multi-byte values are little-endian unless noted otherwise.

## File Layout

| Offset  | Type    | Field              | Notes                                                    |
| ------- | ------- | ------------------ | -------------------------------------------------------- |
| `+0x00` | char[4] | magic              | `PABR` (ASCII)                                           |
| `+0x04` | u32     | record_count       | `91` on client 3464                                      |
| `+0x08` | row[]   | records            | `record_count` rows of 4 bytes                           |
| varies  | u32     | string_count       | Always `0`: the PABR string table is present but empty   |
| EOF-8   | u32     | string_table_start | Absolute offset of `string_count`; equals `8 + 4 × count` |
| EOF-4   | u32     | zero_trailer       | Always `0`                                               |

The file is `8 + 4 × 91 + 12 = 384` bytes on client 3464. The parser rejects a file whose rows do not end exactly at `string_table_start`.

## Record Structure

### Row (4 bytes, repeated `record_count` times)

| Offset  | Type | Field             | Notes                                                                 |
| ------- | ---- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | barter_region_key | `regioninfo.bss` region key; unique                                   |
| `+0x02` | u16  | character_id      | The barter NPC; unique, and its `characterfunction.dbss` record has a Maritime Trade button |

Rows are in neither key nor character order.

## Notes

- On client 3464 the `maritime_trade` slot of [`characterfunction.dbss`](characterfunction_dbss.md) stores the same key as `barter_region_key` for all 91 characters, and those 91 are the only characters with a non-zero `barter_region_key`.
- The regions (client 3464): 70 islands, Arehaza, 8 coastal ports (Olvia Coast, Epheria Sentry Post, Sausan Garrison Wharf, Grándiha, Starry Midnight Port, Sanctuary Coastal Outpost, Dallae Pier, Crow's Nest) and 12 ship regions. Lema Island, Iliya Island and Arehaza are `MinorTown`, the others `Hunting`. The ship regions belong to characters 50814 to 50827 (Crow Merchants' Vessel, Old Moon Guild's Carrack, Wandering Merchant's Ship, Cholace Chico's Pirate Union and eight wrecks and rafts). The 12 ship regions are the only ones with `regioninfo.bss` `is_ocean` set.
- The other barter tables (`barter_normal.bss`, `barter_special.bss`, `bartersubgroup.bss`, `barterlifelevelinfo.bss`, `barterresetoption.bss`) are not documented yet.
