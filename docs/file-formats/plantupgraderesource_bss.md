# `plantupgraderesource.bss` Format

## Purpose

Upgrade costs of the worker system: one entry per level group and level with the time, contribution points, silver and up to three items the upgrade to that level takes. Towns in [planttown.bss](planttown_bss.md) use level group 1.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records                 | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ----------------------- | --------- |
| 1      | 1784 and later | 3474    | `plantupgraderesource.bss` | 4,428 | 228 Need Item, 76 Entry | 12        |

| Layout | File                       | Known            | Unknown    |
| ------ | -------------------------- | ---------------- | ---------- |
| 1      | `plantupgraderesource.bss` | 4,428 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes |
| ------------------- | ------------ | ------------ | ----- |
| `+0x00`             | char[4]      | magic        | `PABR` |
| `+0x04`             | u32          | count        | Number of entries; `76` on client 3473 |
| `+0x08`             | Entry[count] | entries      | See Entry |
| `entries+0x00`      | String Table | string_table | See String Table |
| `string_table+0x00` | u32          | data_end     | `8 + count × 58`, the offset of the trailer |
| `string_table+0x04` | u32          | zero         | `0` |

### Entry (58 bytes)

| Offset  | Type         | Field       | Notes |
| ------- | ------------ | ----------- | ----- |
| `+0x00` | u16          | group       | Map key: level group, see Level Groups |
| `+0x02` | i16          | level       | Map key: level, from 1 |
| `+0x04` | u16          | key_group   | Equals `group` in every entry |
| `+0x06` | i16          | key_level   | Equals `level` in every entry |
| `+0x08` | i32          | need_time   | `600` in every entry; the unit is not confirmed |
| `+0x0C` | Need Item[3] | need_items  | Three slots of a u32 item ID and an i64 count, see Need Item |
| `+0x30` | i16          | need_point  | Contribution points: `10` in group 1, `5` in group 2, `50` in groups 3 and 4 |
| `+0x32` | i64          | need_money  | `0` in every entry |

### Need Item (12 bytes)

Each `need_items` slot.

| Offset  | Type | Field   | Notes |
| ------- | ---- | ------- | ----- |
| `+0x00` | u32  | item_id | `0` in every slot on client 3473 |
| `+0x04` | i64  | count   | `0` in every slot on client 3473 |

### String Table (variable: 4 bytes + strings)

The PABR string table, here with no strings.

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` |
| `+0x04` | pstr[string_count] | strings      | Empty |

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
