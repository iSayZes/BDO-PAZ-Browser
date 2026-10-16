# `plantupgraderesource.bss` Format

## Purpose

Upgrade costs of the worker system: one entry per level group and level with the time, contribution points, silver and up to three items the upgrade to that level takes. Towns in [planttown.bss](planttown_bss.md) use level group 1.

Example:

```text
group 1 level 13  need_time 600  need_point 10  need_money 0  no items
group 4 level 13  need_time 600  need_point 50  need_money 0  no items
```

All multi-byte values are little-endian.

## File Layout

### Header (8 bytes)

| Offset  | Type    | Field | Notes |
| ------- | ------- | ----- | ----- |
| `+0x00` | char[4] | magic | `PABR` |
| `+0x04` | u32     | count | Number of entries; `76` on client 3473 |

### Entry (58 bytes, repeated `count` times)

| Offset  | Type      | Field       | Notes |
| ------- | --------- | ----------- | ----- |
| `+0x00` | u16       | group       | Map key: level group, see Level Groups |
| `+0x02` | i16       | level       | Map key: level, from 1 |
| `+0x04` | u16       | key_group   | Equals `group` in every entry |
| `+0x06` | i16       | key_level   | Equals `level` in every entry |
| `+0x08` | i32       | need_time   | `600` in every entry; the unit is not confirmed |
| `+0x0C` | 3 × item  | need_items  | Three slots of a u32 item ID and an i64 count, below |
| `+0x30` | i16       | need_point  | Contribution points: `10` in group 1, `5` in group 2, `50` in groups 3 and 4 |
| `+0x32` | i64       | need_money  | `0` in every entry |

Each `need_items` slot (12 bytes):

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | u32  | item_id | `0` in every slot on client 3473 |
| `+0x04` | i64  | count   | `0` in every slot on client 3473 |

### Trailer (12 bytes)

| Offset  | Type | Field    | Notes |
| ------- | ---- | -------- | ----- |
| `+0x00` | u32  | -        | `0` |
| `+0x04` | u32  | data_end | `8 + count × 58`, the offset of the trailer |
| `+0x08` | u32  | -        | `0` |

## Level Groups

The groups on client 3473. The names translate the developer comments of the private server's sheet (see Field Names).

| Group | Levels | Name | Referenced by |
| ----: | -----: | ---- | ------------- |
| 1 | 1 to 16 | Town, common | `planttown.bss` `upgrade_resource_key` |
| 2 | 1 to 10 | Farm, small | The `UpgradeResource` column of the `PlantZone_Table` sheet; `plantzone.dbss` has no field for it |
| 3 | 1 to 20 | Farm, medium | - |
| 4 | 1 to 30 | Farm, large | - |

## Notes

- Total size is `8 + count × 58 + 12`: 4,428 bytes on client 3473.
- The entries are in neither key nor level order (`(4, 13)`, `(3, 13)`, `(1, 13)`, `(4, 12)` ...). The 2016 client loads the table into a `pa::BinaryUnorderedMap` keyed by (group, level).
- No client Lua names this table; the only plant upgrade names in Lua are the `CppEnums.PlantLevelType` values (`ePlantLevelType_PlantTown`, `ePlantLevelType_PlantZoneEfficiency` and three more) in `global_define_cpp_enum.luac`.

## Field Names

The names follow the 2016 `gc::PlantUpgradeResourceStaticStatus` (`_key` as `PlantUpgradeResourceLevelKey` of a u16 key and a short level, `_needTime`, `_needItems` as three `NeedItem` of an `ItemEnchantKey` and an `__int64` count, `_needPoint` as a short, `_needMoney` as an `__int64`) and the `PlantUpgradeLevel_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (columns `LevelGoup`, `Level`, `NeedTime`, `NeedExplorePoint`, `NeedMoney`, `NeedItem1` to `NeedItemCount3`). Matched by (group, level) over the 76 entries both hold: every column equals its field on 76 of 76 (client 3473), `NeedExplorePoint` included, the one column whose values vary. The 2016 `_isBlockedNpcWork` bool has no byte in the record.

## Open Questions

### `need_time` Unit

`need_time` is `600` in every entry and in the sheet. Seconds would make every town and farm upgrade take 10 minutes, and no client Lua reads it. The 2016 loader (`GameCommonParameterLoaderFromExcel::LoadPlantUpgradeResourceInformation`) reads the `NeedTime` column with `pa::setValueFromExcel<int>` straight into `_needTime`, with no scaling, so the file holds the sheet's number. No other 2016 function names the table: its `StaticStatusManager::get` is one shared body with the `planttown.bss` manager's, so its callers cannot be told apart, and the code that turns `_needTime` into a duration is not found.
