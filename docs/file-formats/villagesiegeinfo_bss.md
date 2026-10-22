# `villagesiegeinfo.bss` Format

## Purpose

The areas of the Node War (village siege) region map, one row per colour
of `ui_texture/minimap/area/villagesiegemap_2024.bmp`: the colour, a copy
of it, the node war region the area covers and a u16 that numbers the
rows territory by territory. Client 3482 has 41 rows: 36 node war nodes,
the four capitals and the `0d0d0d` row with no region. The rows have the
shape of the [`oceansiegeinfo.bss`](oceansiegeinfo_bss.md) rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ---------------------- | ----- | ------- | ----------------------- |
| 2      | 3002 and later | 3482    | `villagesiegeinfo.bss` | 674   | 41 Row  | 14 to 16, 16 on average |
| 1      | 1348 to 2765   | 2765    | `villagesiegeinfo.bss` | 1,820 | 59 Row  | 22 to 24, 24 on average |

| Layout | File                   | Known           | Unknown       |
| ------ | ---------------------- | --------------- | ------------- |
| 2      | `villagesiegeinfo.bss` | 510 B (75.7%)   | 164 B (24.3%) |
| 1      | `villagesiegeinfo.bss` | 1,112 B (61.1%) | 708 B (38.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3251   | Layout 2             |
| 3002   | Layout 2             |
| 2765   | Layout 1             |
| 2519   | Layout 1             |
| 2313   | Layout 1             |
| 2107   | Layout 1             |
| 1937   | Layout 1             |
| 1784   | Layout 1             |
| 1636   | Layout 1             |
| 1485   | Layout 1             |
| 1348   | Layout 1             |
| 1230   | No documented layout |
| 1058   | No file              |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                   |
| --------------------- | -------- | ------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Region names, LOC type 17, for the `region_keys` cell |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 14 bytes + region keys)

| Offset             | Type                  | Field                  | Notes                                                                      |
| ------------------ | --------------------- | ---------------------- | -------------------------------------------------------------------------- |
| `+0x00`            | bytes[3]              | map_color              | Region map colour, stored blue, green, red; unique per row. See Map Colours |
| `+0x03`            | u8                    | unknown_03             | Always `0`                                                                 |
| `+0x04`            | bytes[3]              | map_color_dup          | Equals `map_color` on every row; see Field Names                           |
| `+0x07`            | u8                    | unknown_07             | Always `0`                                                                 |
| `+0x08`            | u32                   | region_key_count       | Number of `region_keys`; `0` or `1` on client 3482                         |
| `+0x0C`            | u16[region_key_count] | region_keys            | `regioninfo.bss` region keys, LOC type 17 names. See Map Colours           |
| `region_keys+0x00` | u16                   | unknown_region_keys_00 | `0` to `40` on client 3482, unique per row. See Open Questions             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3482, `27` on client 1784 |
| `+0x04` | pstr[string_count] | strings      | Read by `unknown_str_ref` in Layout 1 only                |

## Layout 1

### Row (variable: 22 bytes + region keys)

| Offset             | Type                  | Field                  | Notes                                                              |
| ------------------ | --------------------- | ---------------------- | ------------------------------------------------------------------ |
| `+0x00`            | bytes[3]              | map_color              |                                                                    |
| `+0x03`            | u8                    | unknown_03             |                                                                    |
| `+0x04`            | bytes[3]              | map_color_dup          |                                                                    |
| `+0x07`            | u8                    | unknown_07             |                                                                    |
| `+0x08`            | u32                   | region_key_count       |                                                                    |
| `+0x0C`            | u16[region_key_count] | region_keys            |                                                                    |
| `region_keys+0x00` | u32                   | unknown_str_ref        | Index into the string table: 27 Korean town names on client 1784   |
| `region_keys+0x04` | u16                   | unknown_region_keys_00 | `0` to `81` on client 1784, unique per row                         |
| `region_keys+0x06` | u32                   | unknown_region_keys_06 | `0` on every row of client 1784                                    |

## Map Colours

Client 3482, in file order: `map_color` read as `rrggbb`, the region,
its territory in `regioninfo.bss` and the u16 after the list. The `.rid`
position is the colour's place in `villagesiegemap_2024.bmp.rid` (2024),
or for the four capitals in `villagesiegemap.bmp.rid` (old map).

| `map_color` | `region_keys`                 | Territory    | `unknown_region_keys_00` | Position in `.rid` |
| ----------- | ----------------------------- | ------------ | ------------------------ | ------------------ |
| `3c784b`    | 1556 Great Red Spot           | Outer Edania | 39                       | 2024: 5            |
| `781ecd`    | 12 Forest of Plunder          | Balenos      | 2                        | 2024: 16           |
| `0d0d0d`    | none                          |              | 0                        | 2024: 1            |
| `1ecdcd`    | 16 Bartali Farm               | Balenos      | 3                        | 2024: 20           |
| `3cc8c8`    | 1574 Great White Spot         | Outer Edania | 36                       | 2024: 6            |
| `d5ffa4`    | 32 Heidel                     | Serendia     | 26                       | old map: 19        |
| `1e2dcd`    | 15 Cron Castle                | Balenos      | 1                        | 2024: 14           |
| `a573cd`    | 343 Wolf Hills                | Balenos      | 4                        | 2024: 15           |
| `9696fa`    | 186 Quint Hill                | Calpheon     | 17                       | 2024: 18           |
| `7878fa`    | 113 Hexe Sanctuary            | Calpheon     | 16                       | 2024: 31           |
| `e6e6fa`    | 290 Longleaf Tree Sentry Post | Calpheon     | 15                       | 2024: 30           |
| `782dcd`    | 7 Altar of Agris              | Balenos      | 5                        | 2024: 17           |
| `78787d`    | 73 Biraghi Den                | Serendia     | 7                        | 2024: 24           |
| `6464cd`    | 9 Western Guard Camp          | Balenos      | 6                        | 2024: 19           |
| `5680c1`    | 1349 City of the Dead         | Ulukita      | 34                       | 2024: 35           |
| `4b4b7d`    | 37 Glish Swamp                | Serendia     | 12                       | 2024: 25           |
| `a5a57d`    | 60 Alejandro Farm             | Serendia     | 8                        | 2024: 22           |
| `e1e17d`    | 67 Bloody Monastery           | Serendia     | 9                        | 2024: 29           |
| `b4b47d`    | 71 Castle Ruins               | Serendia     | 10                       | 2024: 26           |
| `ffe4f6`    | 5 Velia                       | Balenos      | 25                       | old map: 7         |
| `c8c87d`    | 74 Orc Camp                   | Serendia     | 11                       | 2024: 27           |
| `b4b4fa`    | 198 Khuruto Cave              | Calpheon     | 13                       | 2024: 21           |
| `8c2323`    | 638 Altas Farmland            | Valencia     | 24                       | 2024: 9            |
| `fafafa`    | 247 Calpheon Castle Site      | Calpheon     | 14                       | 2024: 23           |
| `e1e1fa`    | 127 Trina Fort                | Calpheon     | 18                       | 2024: 28           |
| `8ce6e6`    | 616 Rakshan Observatory       | Valencia     | 23                       | 2024: 11           |
| `8c9696`    | 692 Areha Palm Forest         | Valencia     | 19                       | 2024: 12           |
| `8c5050`    | 682 Ancado Coast              | Valencia     | 20                       | 2024: 8            |
| `8ca5a5`    | 615 Pilgrim's Sanctum: Fast   | Valencia     | 21                       | 2024: 13           |
| `561e0c`    | 1379 Karasi Canyon            | Ulukita      | 32                       | 2024: 36           |
| `8cfafa`    | 617 Valencia Castle           | Valencia     | 22                       | 2024: 10           |
| `fefec7`    | 202 Altinova                  | Mediah       | 27                       | old map: 12        |
| `ffc8ff`    | 229 Valencia City             | Valencia     | 28                       | old map: 2         |
| `560032`    | 1347 Atessahra                | Ulukita      | 30                       | 2024: 32           |
| `563c96`    | 1367 Neruda Plain             | Ulukita      | 29                       | 2024: 33           |
| `5600c8`    | 1350 Tungrad Ruins            | Ulukita      | 31                       | 2024: 34           |
| `561e70`    | 1381 Shakhtar Wilds           | Ulukita      | 33                       | 2024: 37           |
| `3ca032`    | 1559 Neftak Outpost           | Outer Edania | 35                       | 2024: 4            |
| `3c6464`    | 1563 Escar Mountains          | Outer Edania | 37                       | 2024: 7            |
| `3cf0d2`    | 1599 Crossroads of Defiance   | Outer Edania | 38                       | 2024: 3            |
| `3cb4f0`    | 1584 Azure Battlefield        | Outer Edania | 40                       | 2024: 2            |

## Field Names

The 2016 `gc::VillageSiegeInfo` holds `pa::Color _colorKey` (members `b`,
`g`, `r`, `a`) and `gc::KeyType<unsigned short> _regionKey`. The row is
the colour the table is keyed by, then the struct's own `_colorKey`
(`map_color_dup`, with `unknown_07` its `a` byte), then the region keys,
now a u32-counted list. `map_color` follows
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md), Field Names: on
client 3482 `villagesiegemap_2024.bmp.rid` lists 37 colours, and all 37
are `map_color` values of this file; the other four rows are the capitals
Velia, Heidel, Altinova and Valencia City, whose colours
`villagesiegemap.bmp.rid` lists. `villagesiegemap_2024.bmp` is the map
`fieldinfo.bss` names in `unknown_73` (`regionmapinfo.bss` key 12).
`region_keys` are `regioninfo.bss` keys: on client 3482 all 40 are regions
with a `max_participants` above `0`, the node war regions and the four
capitals.

The `VillageSiege_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 (`VillageSiegeKey`, `R`, `G`, `B`, `RegionKey`,
`RegionName`) holds 33 rows with up to six region keys each, while the
client 1784 file has 82 rows with one region each; the sheet does not
match the file and names no field here.

## Notes

- Layout 1 (clients 1348 to 2765) adds a u32 string-table index and a u32 that is
  always `0` around the u16, and its string table holds 27 Korean town
  names (`타리프 마을`, `벨리아 마을`, `알티노바`, ...). Layout 2 drops
  both and the strings.
- The `0d0d0d` row, first in the 2024 palette, has no region and
  `unknown_region_keys_00` `0`, as the shared first-palette row of the
  other map colour tables.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: `map_color` as `rrggbb` and the
  region keys with their names.

## Open Questions

### The u16 After the Region List

`unknown_region_keys_00` numbers the rows territory by territory on client
3482: `1` to `6` the Balenos nodes, `7` to `12` Serendia, `13` to `18`
Calpheon, `19` to `24` Valencia, `25` to `28` the capitals Velia, Heidel,
Altinova and Valencia City, `29` to `34` Ulukita and `35` to `40` Outer
Edania. The sheet's `VillageSiegeKey` column is a lead, but its client
1784 values do not match the file's. What reads the number is open.

### The Town Names of Client 1784

In Layout 1, `unknown_str_ref` points 82 rows at 27 town names. Which
town a node gets (the nearest town, its supply town or its tax town) is
open, and so is why Layout 2 dropped it.
