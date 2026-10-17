# `edaniaregioninfo.bss` Format

## Purpose

Holds one row per Edania region, the ten castle domains that guilds hold in Edania (Aetherion to Voidekaia), plus a row for the "no region" value. Each row stores the client's `__eEdaniaRegion` value and two 3-byte values that equal the `regioninfo.bss` `color` of the region's castle where that castle has a region of its own.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------- | --------- |
| 1      | 3473 and later | 3474    | `edaniaregioninfo.bss` | 119   | 11 Row  | 9         |

| Layout | File                   | Known        | Unknown      |
| ------ | ---------------------- | ------------ | ------------ |
| 1      | `edaniaregioninfo.bss` | 31 B (26.1%) | 88 B (73.9%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                               |
| --------------------- | -------- | ---------------------------------------------------------------------------------- |
| `stringtable.bss`     | Optional | Hash of the castle name keys `LUA_EDANIA_SYSTEM_CASTLE_NAME_<n>` (GAME sheet)      |
| `languagedata_en.loc` | Optional | Castle name text (LOC type 37, keyed by that hash)                                 |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                                                   |
| ------------------- | ----------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                          |
| `+0x04`             | u32               | record_count       | Observed `11`                                           |
| `+0x08`             | Row[record_count] | records            | See Row; byte-packed                                    |
| `records+0x00`      | String Table      | string_table       | The PABR string table, present but empty                |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 9 × count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                              |

The file is `8 + 9 × 11 + 12 = 119` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (9 bytes)

| Offset  | Type     | Field         | Notes                                                                                                   |
| ------- | -------- | ------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | bytes[3] | unknown_00    | Stored blue, green, red like the `regioninfo.bss` `color`; the parser returns `rrggbb`. See Notes        |
| `+0x03` | u8       | unknown_03    | Always `0`                                                                                              |
| `+0x04` | bytes[3] | unknown_04    | Equals `unknown_00` on every row                                                                        |
| `+0x07` | u8       | unknown_07    | Always `0`                                                                                              |
| `+0x08` | u8       | edania_region | `__eEdaniaRegion` value, unique; `0` to `9` for the regions, `10` for `__eEdaniaRegion_Count`. Rows are not in key order |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Enum Values

`edania_region` is the client's `__eEdaniaRegion` enum. The Lua lists the names in this order (`panel_characternametag.luac`, `panel_widget_chatmain_2.luac`, `panel_window_edania_contents_all.luac`) and loops `0` to `Zephyros` for the first Edana group and `Aphrodon` to `Count - 1` for the second (`panel_characterinfo_cashbuff_all_1.luac`). The castle name key is the one the Edania window gives each region.

| Value | Enum name   | Castle name key                   | English castle name |
| ----- | ----------- | --------------------------------- | ------------------- |
| `0`   | Aetherion   | `LUA_EDANIA_SYSTEM_CASTLE_NAME_1`  | Aetherion Castle    |
| `1`   | Nymphamare  | `LUA_EDANIA_SYSTEM_CASTLE_NAME_2`  | Nymphamaré Castle   |
| `2`   | Orbita      | `LUA_EDANIA_SYSTEM_CASTLE_NAME_4`  | Orbita Castle       |
| `3`   | Tenebraum   | `LUA_EDANIA_SYSTEM_CASTLE_NAME_3`  | Tenebraum Castle    |
| `4`   | Zephyros    | `LUA_EDANIA_SYSTEM_CASTLE_NAME_5`  | Zephyros Castle     |
| `5`   | Aphrodon    | `LUA_EDANIA_SYSTEM_CASTLE_NAME_6`  | Aphrodon Temple     |
| `6`   | Hermesia    | `LUA_EDANIA_SYSTEM_CASTLE_NAME_7`  | Hermesia Castle     |
| `7`   | Magaia      | `LUA_EDANIA_SYSTEM_CASTLE_NAME_8`  | Magaia Temple       |
| `8`   | Aresion     | `LUA_EDANIA_SYSTEM_CASTLE_NAME_9`  | Aresion Temple      |
| `9`   | Voidekaia   | `LUA_EDANIA_SYSTEM_CASTLE_NAME_10` | Event Horizon       |
| `10`  | _Count      |                                   | none                |

Orbita and Tenebraum swap key numbers 3 and 4. The file confirms the values of the first five: their `unknown_00` matches the `regioninfo.bss` `color` of exactly one region each, and that region is the castle of the same name (1581 Aetherion Castle, 1621 Nymphamaré Castle, 1571 Orbita Castle, 1611 Tenebraum Castle, 1596 Zephyros Castle).

## Notes

- The client reads a player's Edania region with `ToClient_GetEdaniaRegion(userNo)` and picks the faction icon on the name tag and in chat from it (`Combine_Etc_EdaniaIcon_Jordain_Normal` for Aetherion ... `Combine_Etc_EdaniaIcon_Hadum_Normal` for Voidekaia). `_Count` is the "no Edania region" answer.
- `regioninfo.bss` has regions named after the second-group castles too (Aphrodon Temple, Hermesia Outer and Inner Castle, Magaia Temple, Aresion Temple), but none of them has the colour stored here, so only the first five rows link to a region.
- `blizzardregioninfo.bss` is the other small region-variant table. It does not share this layout (26-byte rows keyed by a region key), so the two files have separate parsers.

## Open Questions

### Why the Value Is Stored Twice

`unknown_04` equals `unknown_00` on every row. Whether the two are fill and
border, or two map layers, and what the `_Count` row's `100d10` is used for
are not known. The In-Game Check below only settles what the value is.

## In-Game Checks

### Edania Overlay Colours

Needs zone: Edania

This checks whether `unknown_00` is the colour of each Edania domain on the world map.

For the five first-group castles `unknown_00` equals the `regioninfo.bss` `color` of the castle's region, and `regioninfo.bss` stores that colour blue, green, red (its `R`, `G` and `B` match the server-side `Region_Table` on 895 of 896 regions, client 3464). Read the same way, the rows here are Aetherion `0a1cf5` (blue), Orbita `905037` (brown-red) and Event Horizon (Voidekaia) `770868` (purple).

1. Open the world map over Edania.
2. Switch the Edania area overlay on (`ToClient_ToggleEdaniaArea`).
3. Note the colour of the Aetherion, Orbita and Event Horizon domains.

Expected result: the three domains show those colours. A domain colour that matches no row means the overlay takes its colour from somewhere else.
