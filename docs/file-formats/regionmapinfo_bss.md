# `regionmapinfo.bss` Format

## Purpose

The bitmaps the game looks a world position up in (its region, siege area
or audio zone): one row per map with its key, its map type, the sector
rectangle the image covers and the image file name. The image is
`ui_texture/minimap/area/<image_path>.bkd` in lower case with its `.rid`
palette (`RegionMap_New.bmp` is `regionmap_new.bmp.bkd`).
[fieldinfo.bss](fieldinfo_bss.md) stores these keys in its
`*_map_index` fields (see its Map Index Fields). The file is the client copy
of the developers' `RegionMap_Table` sheet (see
[Field Names](#field-names)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | ----------------------- |
| 2      | 1230 and later | 3482    | `regionmapinfo.bss` | 896   | 13 Row  | 25                      |
| 1      | 794            | 794     | `regionmapinfo.bss` | 240   | 4 Row   | 53 to 67, 59 on average |

| Layout | File                | Known          | Unknown    |
| ------ | ------------------- | -------------- | ---------- |
| 2      | `regionmapinfo.bss` | 896 B (100.0%) | 0 B (0.0%) |
| 1      | `regionmapinfo.bss` | 240 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2765   | Layout 2 |
| 2519   | Layout 2 |
| 2107   | Layout 2 |
| 1784   | Layout 2 |
| 1636   | Layout 2 |
| 1485   | Layout 2 |
| 1348   | Layout 2 |
| 1230   | Layout 2 |
| 1058   | No file  |
| 794    | Layout 1 |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

A PABR file with fixed rows and the counted string table that
`fieldinfo.bss` also ends with (`_common/pabr_strings.py`).

| Offset              | Type              | Field              | Notes                                                       |
| ------------------- | ----------------- | ------------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                              |
| `+0x04`             | u32               | record_count       | Number of rows; `13` on client 3482                         |
| `+0x08`             | Row[record_count] | records            | See Row; not sorted by `map_index`                          |
| `records+0x00`      | String Table      | string_table       | See String Table                                            |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 25 x count`  |
| `string_table+0x04` | u32               | zero               | Always `0`                                                  |

The parser rejects a file whose rows do not end at `string_table_start`.

### Row (25 bytes)

| Offset  | Type | Field          | Notes |
| ------- | ---- | -------------- | ----- |
| `+0x00` | u16  | map_index      | Unique; the value of the `fieldinfo.bss` `*_map_index` fields |
| `+0x02` | u8   | map_type       | See [Map Types](#map-types) |
| `+0x03` | u16  | map_index_dup  | Equals `map_index` on every row of every client read (794 to 3482); the parser rejects a row where it differs |
| `+0x05` | i32  | sector_start_x | Left edge of the image, in 12,800-unit sectors; `-160` on every row |
| `+0x09` | i32  | sector_end_y   | Top edge; `160` on every row |
| `+0x0D` | i32  | sector_end_x   | Right edge; `112` on every row |
| `+0x11` | i32  | sector_start_y | Bottom edge; `-88` on every row |
| `+0x15` | u32  | image_path_ref | String-table index of `image_path`, the map image file name (`RegionMap_New.bmp`) |

The map's Y axis is the world's Z axis (north). The rectangle is one sector
wider on every side than the box of `fieldinfo.bss` field `1`, the open
world (X `-159` to `111`, Z `-87` to `159` on client 3482), as the sheet
comment asks: a field is written one sector smaller than its map. The
parser stores `image_path_ref` as the string under `image_path`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | Equals `record_count` on every client read               |
| `+0x04` | pstr[string_count] | strings      | Counted entries, indexed from `0`; one image name per row, in row order |

## Layout 1

The client 794 file (in `gamecommondata/binary/en/`) has no PABR header
and no string table: a u32 row count, then rows that hold the image name
inline as a `str16`. The row fields before it are those of Layout 2.

### File Layout

| Offset  | Type              | Field        | Notes                   |
| ------- | ----------------- | ------------ | ----------------------- |
| `+0x00` | u32               | record_count | `4` on client 794       |
| `+0x04` | Row[record_count] | records      | See Row                 |

### Row (variable: 29 bytes + image name)

| Offset  | Type  | Field          | Notes |
| ------- | ----- | -------------- | ----- |
| `+0x00` | u16   | map_index      | |
| `+0x02` | u8    | map_type       | `0`, `3`, `4` and `6` on client 794 |
| `+0x03` | u16   | map_index_dup  | |
| `+0x05` | i32   | sector_start_x | |
| `+0x09` | i32   | sector_end_y   | |
| `+0x0D` | i32   | sector_end_x   | |
| `+0x11` | i32   | sector_start_y | |
| `+0x15` | str16 | image_path     | `AudioMap.bmp`, `VillageSiegemap.bmp`, `Siegemap.bmp`, `RegionMap_New.bmp` |

## Map Types

`map_type` is the 2016 client's `gc::BitmapMapInfoType` (a u8 enum), the
value `gc::BitmapMapInfo::getBitmapMapInfo()` returns for each map class.
The 2016 enum ends at `5`; the later values have no name there. Every map
except the village siege maps has `map_type` = `map_index - 1`.

| Value | 2016 name                        | Maps (key) on client 3482 |
| ----- | -------------------------------- | ------------------------- |
| `0`   | `BitmapMapInfoType_Region`       | `RegionMap_New.bmp` (1)   |
| `1`   | `BitmapMapInfoType_Fishing`      | none                      |
| `2`   | `BitmapMapInfoType_Water`        | none                      |
| `3`   | `BitmapMapInfoType_Siege`        | `Siegemap.bmp` (4)        |
| `4`   | `BitmapMapInfoType_VillageSiege` | none                      |
| `5`   | `BitmapMapInfoType_Underground`  | none                      |
| `6`   | none                             | `AudioMap.bmp` (7)        |
| `7`   | none                             | `GreatSeaMap.bmp` (8)     |
| `8`   | none                             | `HorseRaceCourseMap.bmp` (9) |
| `10`  | none                             | `ElfWar_SiegeMap.bmp` (11) |
| `11`  | none                             | `VillageSiegemap.bmp` (5), `VillageSiegemap_New.bmp` (10), `VillageSiegemap_2024.bmp` (12) |
| `13`  | none                             | `HardCoreChannelMap.bmp` (14) |
| `14`  | none                             | `SnowBoardCourseMap.bmp` (15) |
| `15`  | none                             | `EdaniaRegionMap.bmp` (16) |
| `16`  | none                             | `OceanSiegemap.bmp` (17)  |

The village siege maps share one value, and it moved between clients:

| Clients      | `map_type` of the village siege maps | Village siege maps (key)   |
| ------------ | ------------------------------------ | -------------------------- |
| 794 to 1485  | `4` (`BitmapMapInfoType_VillageSiege`) | 5                        |
| 1636         | `4`                                  | 5, 10                      |
| 1784, 2107   | `9`                                  | 5, 10                      |
| 2519 to 3482 | `11`                                 | 5, 10, 12                  |

## Field Names

The row is the `RegionMap_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (10 rows, developer workbook
`datasheet_regiondatatable.xlsm`). The `regionmapinfo.bss` of the client
1784 test client is byte for byte the private server's build of that sheet:
7 rows, the sheet without keys 2 (`FishingMap.bmp`), 3 (`WaterMap.bmp`) and
6 (`Undergroundmap.bmp`). Over the 7 shared keys:

| Field                      | Sheet column                     | Match                       |
| -------------------------- | -------------------------------- | --------------------------- |
| `map_index`                | `Index`                          | 7 of 7                      |
| `sector_start_x`           | `MapSectorStartX`                | 7 of 7 (`-160`)             |
| `sector_end_y`             | `MapSectorEndY`                  | 7 of 7 (`160`)              |
| `sector_end_x`             | `MapSectorEndX`                  | 7 of 7 (`112`)              |
| `sector_start_y`           | `MapSectorStartY`                | 7 of 7 (`-88`)              |
| `image_path`               | `ImagePath`                      | 7 of 7                      |
| `map_type`                 | `Type`                           | `Type - 1` on 5 of 7; keys 5 and 10 hold `9`, the sheet `5` and `10` |

The four sector values differ from each other, so their match places each
field. The 2016 client's `gc::BitmapMapInfo` holds `_key` (a u16),
`m_sector` (a `CRect`: `left`, `top`, `right`, `bottom`) and
`m_strImagePath`, the row order with `map_type` and `map_index_dup` between
the key and the rectangle. `map_type` takes its name from
`gc::BitmapMapInfoType`: on clients 794 to 1636 the region map holds `0`
(`Region`), the siege map `3` (`Siege`) and the village siege maps `4`
(`VillageSiege`). The sheet's `Description` (Korean notes, `월드 지도`
"world map") is not in the file; its comment says the game does not use it.

## Notes

- The 1784 sheet comments: `Index` counts from `1` and must be unique;
  `ImagePath` is relative to the UI folder, and a `*` after the name loads
  every file with that name. No row on any client read uses `*`.
- The 2016 client has a map class for each named type (`RegionMapInfo`,
  `FishingMapInfo`, `WaterMapInfo`, `SiegeMapInfo`, `VillageSiegeMapInfo`,
  `UndergroundMapInfo`). The server build of a private server on client 1784
  adds `AudioMapInfo`, `GreatSeaMapInfo` and `HorseRaceMapInfo`.
- Client 2107 also has six `_Morning` maps keyed `10000` plus the key of the
  map they copy (`10000` `RegionMap_Morning.bmp` to `10009`
  `VillageSiegemap_New_Morning.bmp`), each with the `map_type` of that map.
  Client 2519 and later have no `_Morning` rows, though the client 3482
  folder still has `regionmap_morning.bmp.bkd` and the other `_morning`
  images.
- Keys `2`, `3` and `6` (fishing, water and underground maps) are in no
  client read; `fieldinfo.bss` still stores them in `fishing_map_index`,
  `water_info_map_index` and `underground_map_index`.
- Client 1058 ships the table as `#na#regionmapinfo.bss`: four
  Layout 2 rows (keys 1, 4, 5 and 7), so the doc check finds no
  `regionmapinfo.bss` there. Client 794 has the same four maps in Layout 1,
  under `gamecommondata/binary/en/`.

## Open Questions

### Why the Village Siege Maps Moved to a Later Map Type

The village siege maps hold `4`, the 2016 `VillageSiege` value, up to client
1636, then `9` on clients 1784 and 2107 and `11` from client 2519, each time
the key of the newest village siege map minus one. Every other map keeps
`map_index - 1`. Whether the enum was renumbered or the newest village siege
class reads all three images is open; no client 3482 `.luac` file names a
map type.
