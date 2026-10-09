# `edaniaregioninfo.bss` Format

## Purpose

Holds one row per Edania region, the ten castle domains that guilds hold in Edania (Aetherion to Voidekaia), plus a row for the "no region" value. Each row stores the client's `__eEdaniaRegion` value and two 3-byte values that equal the `regioninfo.bss` `unknown_02` colour of the region's castle where that castle has a region of its own.

Example:

```text
edania_region=0  -> Aetherion Castle   (f51c0a, the unknown_02 of region 1581 Aetherion Castle)
edania_region=2  -> Orbita Castle      (375090, the unknown_02 of region 1571 Orbita Castle)
edania_region=9  -> Event Horizon      (680877, no matching region)
edania_region=10 -> none (_Count)      (100d10)
```

## Companion Files

| File                  | Required | Role                                                                               |
| --------------------- | -------- | ---------------------------------------------------------------------------------- |
| `stringtable.bss`     | Optional | Hash of the castle name keys `LUA_EDANIA_SYSTEM_CASTLE_NAME_<n>` (GAME sheet)      |
| `languagedata_en.loc` | Optional | Castle name text (LOC type 37, keyed by that hash)                                 |

All multi-byte values are little-endian unless noted otherwise.

## File Layout

| Offset  | Type    | Field              | Notes                                                   |
| ------- | ------- | ------------------ | ------------------------------------------------------- |
| `+0x00` | char[4] | magic              | `PABR` (ASCII)                                          |
| `+0x04` | u32     | record_count       | Observed `11`                                           |
| `+0x08` | row[]   | records            | `record_count` rows of 9 bytes, byte-packed             |
| varies  | u32     | string_count       | Always `0`: the PABR string table is present but empty  |
| EOF-8   | u32     | string_table_start | Absolute offset of `string_count`; equals `8 + 9 × count` |
| EOF-4   | u32     | zero_trailer       | Always `0`                                              |

The file is `8 + 9 × 11 + 12 = 119` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

## Record Structure

### Row (9 bytes, repeated `record_count` times)

| Offset  | Type  | Field         | Notes                                                                                                   |
| ------- | ----- | ------------- | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | u8[3] | unknown_00    | Kept as a hex string in file order, as `regioninfo.bss` keeps `unknown_02`; see Notes                   |
| `+0x03` | u8    | reserved      | Always `0`                                                                                              |
| `+0x04` | u8[3] | unknown_04    | Equals `unknown_00` on every row                                                                        |
| `+0x07` | u8    | reserved      | Always `0`                                                                                              |
| `+0x08` | u8    | edania_region | `__eEdaniaRegion` value, unique; `0` to `9` for the regions, `10` for `__eEdaniaRegion_Count`. Rows are not in key order |

### Enum Values

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

Orbita and Tenebraum swap key numbers 3 and 4. The file confirms the values of the first five: their `unknown_00` matches the `regioninfo.bss` `unknown_02` of exactly one region each, and that region is the castle of the same name (1581 Aetherion Castle, 1621 Nymphamaré Castle, 1571 Orbita Castle, 1611 Tenebraum Castle, 1596 Zephyros Castle).

## Suggested UI Layout

| Column        | Type | Notes                                                                                     |
| ------------- | ---- | ----------------------------------------------------------------------------------------- |
| Edania Region | num  | `edania_region`                                                                           |
| Castle        | text | `castle_name`: the castle name key's LOC text, else the enum name; a dash for `_Count`    |

The `unknown_*` fields stay on the record for search and CSV but out of the table.

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

`unknown_00` and `unknown_04` are two equal 3-byte values per row. For the
five first-group castles each equals the `regioninfo.bss` `unknown_02` of the
castle's region, which bdo-data-extractor reads as the region's world-map
colour, so these are likely the colour of each Edania domain, for instance on
the world map overlay that `ToClient_ToggleEdaniaArea` switches.

Open the world map over Edania, switch the Edania area overlay on and compare
each domain's colour with its row: Aetherion `f51c0a`, Orbita `375090`,
Event Horizon (Voidekaia) `680877`. Matching colours confirm the field as the
domain colour. Read in file order the values are RGB (`f51c0a` red-orange);
if Aetherion shows blue instead, the bytes are BGR (`0a1cf5`). A domain
overlay that matches no row means the colour comes from somewhere else.
