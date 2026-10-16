# `plantupgradeparam.bss` Format

## Purpose

Upgrade parameter groups of the worker system: one entry per group with its highest upgrade level. Towns in [planttown.bss](planttown_bss.md) point at groups 1 (warehouse) and 2 (worker capacity), plant zones in [plantzone.dbss](plantzone_dbss.md) at 101 (base efficiency) and 201 (luck efficiency). The per-level values the groups stand for are not in the client file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field        | Notes                     |
| ------------------- | ------------ | ------------ | ------------------------- |
| `+0x00`             | char[4]      | magic        | `PABR`                    |
| `+0x04`             | u32          | count        | Number of entries; `4` on client 3473 |
| `+0x08`             | Entry[count] | entries      | See Entry                 |
| `entries+0x00`      | String Table | string_table | See String Table          |
| `string_table+0x00` | u32          | data_end     | `8 + count × 6`, the offset of the trailer |
| `string_table+0x04` | u32          | zero         | `0` |

### Entry (6 bytes)

| Offset  | Type | Field     | Notes |
| ------- | ---- | --------- | ----- |
| `+0x00` | u16  | key       | Map key |
| `+0x02` | u16  | param_key | Equals `key` in every entry |
| `+0x04` | i16  | max_level | Highest upgrade level |

### String Table (variable: 4 bytes + strings)

The PABR string table, here with no strings.

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Entries

The entries on client 3473, in file order. The use column follows the developer comments of the private server's sheet (see Field Names).

| Key | Max Level | Use | Referenced by |
| --: | --------: | --- | ------------- |
| 201 | 0 | Luck efficiency, levels 0 to 1: 100/120% | `plantzone.dbss` `luck_productivity_upgrade_group_index` |
| 101 | 0 | Base efficiency, levels 0 to 1: 100/120% | `plantzone.dbss` `productivity_upgrade_group_index` |
| 2   | 5 | Worker capacity, levels 0 to 5: 4/6/8/10/12/14 workers | `planttown.bss` `worker_capacity_upgrade_group_index` |
| 1   | 5 | Warehouse, levels 0 to 5: 40/50/60/70/80/90 slots | `planttown.bss` `warehouse_upgrade_group_index` |

## Notes

- Total size is `8 + count × 6 + 12`: 44 bytes on client 3473.
- `max_level` of groups 101 and 201 is `0` although their sheet comments list levels 0 to 1; only `Level0` is filled in the sheet for them.

## Field Names

The names follow the 2016 `gc::PlantUpgradeParamStaticStatus` (`_key`, `_param` as `int[6]`, `_maxLevel` as a short) and the `PlantUpgradeParam_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (columns `Index`, `Level0` to `Level5`). The sheet's four `Index` values are the file's four keys. Its note column `#참고용 Count` holds `5`, `5`, `0`, `0`, equal to `max_level` on all four entries, and the 2016 member order places `_maxLevel` after the key. The six `_param` values (`Level0` to `Level5`, 40 to 90 warehouse slots for key 1) have no bytes in the client file.

The client Lua enums in `global_define_cpp_enum.luac` name the two level types of each user: `CppEnums.PlantTownLevelType` (`ePlantTownLevelType_Warehouse` `0`, `ePlantTownLevelType_WorkerCapacity` `1`) for the town keys 1 and 2, and `CppEnums.PlantZoneLevelType` (`ePlantZoneLevelType_GeneralEfficiency` `0`, `ePlantZoneLevelType_LuckEfficiency` `1`) for the zone keys 101 and 201.
