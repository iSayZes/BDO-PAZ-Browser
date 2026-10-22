# `fieldinfo.bss` Format

## Purpose

The fields the game runs: the open world (field `1`), the test and story
instance fields and the 66 `A1_` fields of The Magnus. Each row is keyed by
the field number that [instancefield.dbss](instancefield_dbss.md) and
[instancedungeoninfo.dbss](instancedungeoninfo_dbss.md) store as
`field_no`, and holds the field's world-editor name, its resource folder, a
spawn point, its area as a sector box (in three units), its field type, the
keys of the [regionmapinfo.bss](regionmapinfo_bss.md) maps it uses (see
[Map Index Fields](#map-index-fields)) and its entry rules (players,
mounts, item drop rate). The file is the client copy
of the developers' `Field_Table` sheet (see [Field Names](#field-names)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes  | Records | Row bytes |
| ------ | -------------- | ------- | --------------- | ------ | ------- | --------- |
| 2      | 3251 and later | 3482    | `fieldinfo.bss` | 23,620 | 122 Row | 157       |
| 1      | 1636 to 2107   | 2107    | `fieldinfo.bss` | 22,361 | 123 Row | 145       |

| Layout | File            | Known             | Unknown        |
| ------ | --------------- | ----------------- | -------------- |
| 2      | `fieldinfo.bss` | 22,156 B (93.8%)  | 1,464 B (6.2%) |
| 1      | `fieldinfo.bss` | 22,361 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3251   | Layout 2             |
| 3002   | No documented layout |
| 2765   | No documented layout |
| 2519   | No documented layout |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1636   | Layout 1             |
| 1485   | No documented layout |
| 1348   | No documented layout |
| 1230   | No documented layout |
| 1058   | No file              |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                | Required | Role                                                                 |
| ------------------- | -------- | -------------------------------------------------------------------- |
| `regionmapinfo.bss` | Optional | The image name of each map key (see [Map Index Fields](#map-index-fields)); without it the Maps column is empty |

The handler also reads two lookup indexes to name the `A1_` fields (see
Notes).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                                       |
| ------------------- | ----------------- | ------------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                              |
| `+0x04`             | u32               | record_count       | Number of rows; `122` on client 3474                        |
| `+0x08`             | Row[record_count] | records            | See Row; not sorted by `field_no`                           |
| `records+0x00`      | String Table      | string_table       | See String Table                                            |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 157 x count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                                  |

The parser rejects a file whose rows do not end at `string_table_start`.

### Row (157 bytes)

| Offset  | Type | Field                            | Notes |
| ------- | ---- | -------------------------------- | ----- |
| `+0x00` | u16  | field_no                         | Unique; the `field_no` of `instancefield.dbss` and `instancedungeoninfo.dbss` |
| `+0x02` | u32  | field_name_ref                   | String-table index of `field_name`, the name the world editor shows: Korean (`월드` "World", `칼페온 크자카 인던` "Calpheon Kzarka instance dungeon") or the instance field's internal name (`A1_001`) |
| `+0x06` | u32  | resource_name_ref                | String-table index of `resource_name`, the map resource folder: `_real`, `_empty` (field `0`) or `_instancedungeon/<field_no>` on the `A1_` fields |
| `+0x0A` | u32  | display_name_ref                 | String-table index of `display_name`; the empty string on every row of clients 1784 and 3474 |
| `+0x0E` | f32  | spawn_x                          | Spawn point, world X; `0` on the 51 rows of client 3474 whose sheet has no point |
| `+0x12` | f32  | spawn_y                          | Spawn point, world Y (height) |
| `+0x16` | f32  | spawn_z                          | Spawn point, world Z |
| `+0x1A` | i32  | sector_start_x                   | Field box, lower corner, in 12,800-unit sectors |
| `+0x1E` | i32  | sector_start_y                   | |
| `+0x22` | i32  | sector_start_z                   | |
| `+0x26` | i32  | sector_end_x                     | Field box, upper corner, inclusive; never below the matching start |
| `+0x2A` | i32  | sector_end_y                     | |
| `+0x2E` | i32  | sector_end_z                     | |
| `+0x32` | f32  | world_start_x                    | `sector_start_x x 12800` on every row |
| `+0x36` | f32  | world_start_y                    | `sector_start_y x 12800` |
| `+0x3A` | f32  | world_start_z                    | `sector_start_z x 12800` |
| `+0x3E` | f32  | world_end_x                      | `(sector_end_x + 1) x 12800` on every row: the far edge of the last sector |
| `+0x42` | f32  | world_end_y                      | `(sector_end_y + 1) x 12800` |
| `+0x46` | f32  | world_end_z                      | `(sector_end_z + 1) x 12800` |
| `+0x4A` | i32  | obstacle_precision               | `4` on every row; the sheet comment gives `1` = 128 m down to `128` = 1 m |
| `+0x4E` | i32  | server_sector_start_x            | `sector_start_x x 3` on every row |
| `+0x52` | i32  | server_sector_start_y            | `sector_start_y x 3` |
| `+0x56` | i32  | server_sector_start_z            | `sector_start_z x 3` |
| `+0x5A` | i32  | server_sector_end_x              | `sector_end_x x 3` on every row |
| `+0x5E` | i32  | server_sector_end_y              | `sector_end_y x 3` |
| `+0x62` | i32  | server_sector_end_z              | `sector_end_z x 3` |
| `+0x66` | u8   | field_type                       | See [Field Types](#field-types) |
| `+0x67` | u16  | region_map_index                 | `regionmapinfo.bss` key; see [Map Index Fields](#map-index-fields) |
| `+0x69` | u16  | fishing_map_index                | |
| `+0x6B` | u16  | water_info_map_index             | |
| `+0x6D` | u16  | siege_info_map_index             | |
| `+0x6F` | u16  | village_siege_info_map_index     | |
| `+0x71` | u16  | village_siege_info_map_index_new | |
| `+0x73` | u16  | unknown_73                       | `12` on every row, the `regionmapinfo.bss` key of `VillageSiegemap_2024.bmp`; not in the client 1784 row |
| `+0x75` | u16  | underground_map_index            | |
| `+0x77` | u16  | audio_map_index                  | |
| `+0x79` | u8   | is_save_complete                 | `0` on every row; the sheet comment: count dungeon clears, `0` false, `1` true |
| `+0x7A` | u32  | field_level                      | `0` on every row; the sheet comment: the level players are scaled to, `0` for none |
| `+0x7E` | u8   | is_ridable                       | `1` when a mount may be summoned in the field; fields 1, 700, 701, 1238 and 1239 on client 3474 |
| `+0x7F` | u16  | enter_enable_user_count          | Players who may enter: `2` on the `A1_` fields, `1` elsewhere (client 3474) |
| `+0x81` | u8   | use_range_spawn                  | `1` when the field spawns the world's spawns inside its sector box (the sheet comment names the tutorial); the `A1_` fields on client 3474 |
| `+0x82` | u8   | use_return_position              | `0` on every row; the sheet comment: `1` sends a player back to where they entered from |
| `+0x83` | i32  | item_drop_rate                   | Added item drop rate on the 1,000,000 = 100% scale: `-1000000` (no drops) on the `A1_` fields, `0` elsewhere (client 3474) |
| `+0x87` | u32  | bank_no_music                    | Music bank; `1` on the five rows that have `is_ridable` on client 3474 |
| `+0x8B` | u32  | bank_no_environment              | Ambient sound bank; `0` on every row |
| `+0x8F` | u16  | great_sea_map_index              | |
| `+0x91` | u16  | horse_race_course_map_index      | |
| `+0x93` | u16  | unknown_93                       | `11` on every row, the key of `ElfWar_SiegeMap.bmp` |
| `+0x95` | u16  | unknown_95                       | `14` on every row, the key of `HardCoreChannelMap.bmp` |
| `+0x97` | u16  | unknown_97                       | `15` on every row, the key of `SnowBoardCourseMap.bmp` |
| `+0x99` | u16  | unknown_99                       | `17` on every row, the key of `OceanSiegemap.bmp` |
| `+0x9B` | u16  | unknown_9b                       | `16` on every row, the key of `EdaniaRegionMap.bmp` |

The `*_ref` fields index the string table from `0`; the parser stores each
string under the field name without `_ref`. The value notes are from
client 3474 unless they name another client.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | `144` on client 3474                           |
| `+0x04` | pstr[string_count] | strings      | Counted entries, indexed from `0`; entry `2` is the empty string |

## Layout 1

The client 1784 row is 12 bytes shorter: it lacks `unknown_73` and the five
u16 fields after `horse_race_course_map_index`, so every field from
`underground_map_index` on sits 2 bytes earlier.

### Row (145 bytes)

| Offset  | Type | Field                            | Notes |
| ------- | ---- | -------------------------------- | ----- |
| `+0x00` | u16  | field_no                         | |
| `+0x02` | u32  | field_name_ref                   | |
| `+0x06` | u32  | resource_name_ref                | |
| `+0x0A` | u32  | display_name_ref                 | |
| `+0x0E` | f32  | spawn_x                          | |
| `+0x12` | f32  | spawn_y                          | |
| `+0x16` | f32  | spawn_z                          | |
| `+0x1A` | i32  | sector_start_x                   | |
| `+0x1E` | i32  | sector_start_y                   | |
| `+0x22` | i32  | sector_start_z                   | |
| `+0x26` | i32  | sector_end_x                     | |
| `+0x2A` | i32  | sector_end_y                     | |
| `+0x2E` | i32  | sector_end_z                     | |
| `+0x32` | f32  | world_start_x                    | |
| `+0x36` | f32  | world_start_y                    | |
| `+0x3A` | f32  | world_start_z                    | |
| `+0x3E` | f32  | world_end_x                      | |
| `+0x42` | f32  | world_end_y                      | |
| `+0x46` | f32  | world_end_z                      | |
| `+0x4A` | i32  | obstacle_precision               | |
| `+0x4E` | i32  | server_sector_start_x            | |
| `+0x52` | i32  | server_sector_start_y            | |
| `+0x56` | i32  | server_sector_start_z            | |
| `+0x5A` | i32  | server_sector_end_x              | |
| `+0x5E` | i32  | server_sector_end_y              | |
| `+0x62` | i32  | server_sector_end_z              | |
| `+0x66` | u8   | field_type                       | `0` to `5` on client 1784, see [Field Types](#field-types) |
| `+0x67` | u16  | region_map_index                 | |
| `+0x69` | u16  | fishing_map_index                | |
| `+0x6B` | u16  | water_info_map_index             | |
| `+0x6D` | u16  | siege_info_map_index             | |
| `+0x6F` | u16  | village_siege_info_map_index     | |
| `+0x71` | u16  | village_siege_info_map_index_new | |
| `+0x73` | u16  | underground_map_index            | |
| `+0x75` | u16  | audio_map_index                  | |
| `+0x77` | u8   | is_save_complete                 | |
| `+0x78` | u32  | field_level                      | `30` on 149 rows of client 1784 (102 of `field_type` `1`, 47 of `3`), `0` on the rest |
| `+0x7C` | u8   | is_ridable                       | |
| `+0x7D` | u16  | enter_enable_user_count          | |
| `+0x7F` | u8   | use_range_spawn                  | |
| `+0x80` | u8   | use_return_position              | |
| `+0x81` | i32  | item_drop_rate                   | |
| `+0x85` | u32  | bank_no_music                    | |
| `+0x89` | u32  | bank_no_environment              | |
| `+0x8D` | u16  | great_sea_map_index              | |
| `+0x8F` | u16  | horse_race_course_map_index      | |

## Field Types

`field_type` is the 2016 client's `gc::FieldInfo::FieldType` (a u8 enum).
The `Field_Table` sheet comment on client 1784 lists `0` to `3` with the
same meaning.

| Value | 2016 name              | Sheet comment (client 1784) | Rows on client 1784 | Rows on client 3474 |
| ----- | ---------------------- | --------------------------- | ------------------- | ------------------- |
| `0`   | `OpenField`            | 오픈필드 (open field)       | 2                   | 2 (`0` Empty, `1` 월드) |
| `1`   | `InstanceField`        | 인스턴스필드 (instance field) | 181               | 54                  |
| `2`   | `Nightmare`            | 나이트메어 (nightmare)      | 24                  | 0                   |
| `3`   | `InstanceDungeon`      | 인스턴스던전 (instance dungeon) | 63              | 0                   |
| `4`   | `ChannelInstanceField` | none                        | 1 (`20000`)         | 0                   |
| `5`   | none                   | none                        | 35 (`A1_001` to `A1_035`) | 66 (`A1_001` to `A1_066`) |

## Map Index Fields

The `*_map_index` fields and `unknown_73`, `unknown_93` to `unknown_9b`
hold the same value on every row of a client: the `map_index` of one map
in [regionmapinfo.bss](regionmapinfo_bss.md), which names its image.

The handler stores the image of each named map key field under the field
name with `_image` for `_index` (`region_map_index` 1 gives
`region_map_image` `RegionMap_New.bmp`), `''` for a key without a
`regionmapinfo.bss` row, and lists the images once each in the Maps column.
The `unknown_*` map keys get no image field.

| Field                              | Value | `regionmapinfo.bss` image (client 3474) |
| ---------------------------------- | ----- | --------------------------------------- |
| `region_map_index`                 | `1`   | `RegionMap_New.bmp`                     |
| `fishing_map_index`                | `2`   | none                                    |
| `water_info_map_index`             | `3`   | none                                    |
| `siege_info_map_index`             | `4`   | `Siegemap.bmp`                          |
| `village_siege_info_map_index`     | `5`   | `VillageSiegemap.bmp`                   |
| `village_siege_info_map_index_new` | `10`  | `VillageSiegemap_New.bmp`               |
| `unknown_73`                       | `12`  | `VillageSiegemap_2024.bmp`              |
| `underground_map_index`            | `6`   | none                                    |
| `audio_map_index`                  | `7`   | `AudioMap.bmp`                          |
| `great_sea_map_index`              | `8`   | `GreatSeaMap.bmp`                       |
| `horse_race_course_map_index`      | `9`   | `HorseRaceCourseMap.bmp`                |
| `unknown_93`                       | `11`  | `ElfWar_SiegeMap.bmp`                   |
| `unknown_95`                       | `14`  | `HardCoreChannelMap.bmp`                |
| `unknown_97`                       | `15`  | `SnowBoardCourseMap.bmp`                |
| `unknown_99`                       | `17`  | `OceanSiegemap.bmp`                     |
| `unknown_9b`                       | `16`  | `EdaniaRegionMap.bmp`                   |

On client 1784 the `RegionMap_Table` sheet of the same source lists keys
`1` to `10`: `2` is `FishingMap.bmp`, `3` `WaterMap.bmp` and `6`
`Undergroundmap.bmp`, three keys that no `regionmapinfo.bss` from client
1230 to 3482 holds.

## Field Names

The row is the `Field_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (306 rows, developer workbook
`datasheet_regiondatatable.xlsm`). The `fieldinfo.bss` of the client 1784
test client is byte for byte the private server's build of that sheet: 306
rows of Layout 1. Over its 306 field numbers every column below matches on
every row, except `ResourceName` on field `0` (`_empty` in the file,
`_real` in the sheet):

| Field                                  | Sheet column                                   |
| -------------------------------------- | ---------------------------------------------- |
| `field_no`                             | `FieldNo`                                      |
| `field_name`                           | `FieldName`                                    |
| `resource_name`                        | `ResourceName`                                 |
| `spawn_x`, `spawn_y`, `spawn_z`        | `StartPositionX`, `StartPositionY`, `StartPositionZ` |
| `sector_start_*`, `sector_end_*`       | `MapSectorStartX` to `MapSectorEndZ`           |
| `field_type`                           | `FieldType`                                    |
| `obstacle_precision`                   | `ObstaclePrecision`                            |
| `region_map_index` to `audio_map_index`, `great_sea_map_index`, `horse_race_course_map_index` | `RegionMapIndex`, `FishingMapIndex`, `WaterInfoMapIndex`, `SiegeInfoMapIndex`, `VillageSiegeInfoMapIndex`, `VillageSiegeInfoMapIndexNew`, `UndergroundMapIndex`, `AudioMapIndex`, `GreatSeaMapIndex`, `HorseRaceCourseMapIndex` |
| `is_save_complete`                     | `isSaveComplete`                               |
| `field_level`                          | `FieldLevel`                                   |
| `is_ridable`                           | `IsRidable`                                    |
| `enter_enable_user_count`              | `EnterEnableUserCount`                         |
| `use_range_spawn`                      | `UseRangeSpawn`                                |
| `use_return_position`                  | `UseReturnPosition`                            |
| `item_drop_rate`                       | `ItemDropRate`                                 |
| `bank_no_music`                        | `BankNo_Music`                                 |
| `bank_no_environment`                  | `BankNo_Environment`                           |

Several columns hold one value on all 306 rows (`ObstaclePrecision`,
`isSaveComplete`, `BankNo_Environment` and every map index), so their match
alone places nothing. The 2016 client's `gc::FieldInfo` places them: its
members run `_fieldNo`, `_fieldName`, `_resourceName`, `_displayName`,
`_spawnPosition`, `_startSector`, `_endSector`, `_startPosition`,
`_endPosition`, `_obstaclePrecision`, `_startSector_Server`,
`_endSector_Server`, `_fieldType`, `_regionMapID`, `_fishingMapID`,
`_waterInfoMapID`, `_siegeInfoMapID`, `_viliageSiegeInfoMapID`,
`_undergroundInfoMapID`, `_isSaveComplete`, `_fieldCorrectLevel`,
`_isRidable`, `_enterEnableUserCount`, `_useRangeSpawn`,
`_useReturnPosition`, `_addItemDropRate`, `_bankNo_Music`,
`_bankNo_Environment`, the row order with the later map indexes added.
`display_name`, `world_*` and `server_sector_*` have no sheet column and
take their names from those members. The sheet's `MiniMapIndex` (`1` on
every row) and `StartPositionDir` (7 values) are in neither the struct nor
the file.

On client 3474 the file shares 91 field numbers with the sheet. `field_no`,
`field_name`, the sector box, `field_type`, `is_ridable`,
`enter_enable_user_count`, `use_range_spawn`, `item_drop_rate` and
`bank_no_music` match on all 91, except `sector_end_y` of field `1`
(`6`, the sheet `5`). `resource_name` matches on all 91 without case: 34
`A1_` fields write `_instancedungeon/40NN` where the sheet has
`_InstanceDungeon/40NN`. The spawn point matches on 82; fields 4001, 4006,
4010, 4011, 4026, 4027, 4033, 4034 and 4035 have new points.

The sheet comments on client 1784 give the meaning of `FieldName` (the name
shown in the world editor), `ResourceName` (`real` for open fields and
dungeons that need no loading), `FieldType`, `ObstaclePrecision`,
`isSaveComplete`, `FieldLevel`, `IsRidable`, `EnterEnableUserCount`,
`UseRangeSpawn`, `UseReturnPosition` and `ItemDropRate` ("-100% to 200%",
`-1000000` to `2000000`), as the Row notes quote them.

## Notes

- The handler names an `A1_` field with the title of its
  [instancefieldmapinfo.bss](instancefieldmapinfo_bss.md) map, read in the
  loaded LOC language: `A1_001` reads `The Magnus: The Great Single Path
  (A1_001)`. It takes the title only when the `instancefield.dbss` record
  with the same key has the same name, which holds for the 66 `A1_` fields
  (key `40NN`, name `A1_0NN`, `field_no` `40NN`); field `1`, `월드`, is not
  instance field `1` (`Shadow_Ser_Main`). Every other field shows its
  `field_name`.
- The `FIELD_NAME` lookup index maps each `field_no` to its name, so the
  `instancefield.dbss` and `instancedungeoninfo.dbss` tables show a Field
  column without opening this file. On client 3474 every `field_no` of both
  tables has a row here: `1` and `4001` to `4066` in `instancefield.dbss`,
  `700`, `701`, `1238` and `1239` in `instancedungeoninfo.dbss`.
- Fields `700`, `701`, `1238` and `1239` copy field `1`: the same sector
  box, spawn point, `is_ridable` and `bank_no_music`, with `field_type` `1`.
- Field numbers `9001` to `9050` (client 3474) are named `테스트 인던`
  ("test instance dungeon", 10 rows), `자렛과 클리프` (20) and `조르다인
  이소벨` (20), all `field_type` `1` without a spawn point.
- The 66 `A1_` fields share the box `-3..3` on every axis, as their
  `instancefield.dbss` records do.

## Open Questions

### What Field Type 5 Is

The 2016 enum ends at `4` (`ChannelInstanceField`) and the client 1784
sheet comment at `3`. Type `5` is on every `A1_` field (35 on client 1784,
66 on client 3474) and on no other row, so it names the kind of field The
Magnus runs in. No string in the client 3474 `.luac` files names a field
type.

### Which Maps the Newer Map Index Fields Select

`unknown_73` and `unknown_93` to `unknown_9b` hold the `regionmapinfo.bss`
keys of the 2024 node war map, the Elf War siege map, the hardcore channel
map, the snowboard course map, the ocean siege map and the Edania region
map (see [Map Index Fields](#map-index-fields)). They have no sheet column
on client 1784, so their names and the order of the five trailing fields
are not confirmed.

### Why the Server Box Is Three Times the Sector Box

`server_sector_*` is the sector box times three on every row of clients
1784 and 3474, both corners included, so the server box ends two server
sectors before the field box's far edge. What the server divides a sector
into, and whether the end corner is exclusive there, is open.
