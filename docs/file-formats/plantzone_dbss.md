# `plantzone.dbss` Format

## Purpose

Defines worker production zones. Each record belongs to one worldmap production sub-node (`record_id` is an `exploration.bss` node key, named through LOC type 29), stores the worker's work animation type, links to a production key in `plantexchangegroup.bss` with a capacity level, and lists a set of worker species per zone (not a worker lock; its use is unknown, see Open Questions). `plantzoneoffset.dbss` is required to address the variable-length records.

Observed records: 394 in the pre-2026-09-27 fixture, 439 in the 2026-09-27 client (45 more 37-byte zones). Record payloads are 32, 34, or 37 bytes depending on the worker-species list length.

The production-key reading and the worker-species field boundaries follow [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, "Worker-production item tables"), checked against the current client files below.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes  | Records               | Row bytes               |
| ------ | -------------- | ------- | ---------------------- | ------ | --------------------- | ----------------------- |
| 2      | 2519 and later | 3474    | `plantzone.dbss`       | 16,111 | 439 Plant Zone Record | 32 to 37, 37 on average |
| 2      | 2519 and later | 3474    | `plantzoneoffset.dbss` | 5,272  | 439 Offset Row        | 12                      |
| 1      | 1485 to 2107   | 2107    | `plantzone.dbss`       | 8,725  | 323 Plant Zone Record | 27                      |
| 1      | 1485 to 2107   | 2107    | `plantzoneoffset.dbss` | 3,880  | 323 Offset Row        | 12                      |

| Layout | File                   | Known            | Unknown         |
| ------ | ---------------------- | ---------------- | --------------- |
| 2      | `plantzone.dbss`       | 11,721 B (72.8%) | 4,390 B (27.2%) |
| 2      | `plantzoneoffset.dbss` | 4,394 B (83.3%)  | 878 B (16.7%)   |
| 1      | `plantzone.dbss`       | 5,495 B (63.0%)  | 3,230 B (37.0%) |
| 1      | `plantzoneoffset.dbss` | 3,234 B (83.4%)  | 646 B (16.6%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 2 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                   |
| ---------------------- | -------- | ------------------------------------------------------ |
| `plantzoneoffset.dbss` | Required | Maps `record_id` to byte offset and payload byte count |

All multi-byte values are little-endian unless noted otherwise.

## Layout 2

### File Layout

| Offset  | Type                             | Field         | Notes                                      |
| ------- | -------------------------------- | ------------- | ------------------------------------------ |
| `+0x00` | u32                              | record_count  | Number of records; observed `394` (2026-09-27 client: `439`) |
| `+0x04` | Plant Zone Record[record_count]  | record_stream | Variable-length records, packed back-to-back |

`(file_size - 4) / record_count` is not integral, so records must be sliced with `plantzoneoffset.dbss`.

### Plant Zone Record (variable: 31 bytes + species)

32, 34, or 37 bytes on the observed clients.

| Offset  | Type | Field                | Notes                                                                    |
| ------- | ---- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | record_id            | `exploration.bss` node key; matches `record_id` in `plantzoneoffset.dbss` |
| `+0x04` | u32  | unknown_04           | Always observed as `2`; see Open Questions                               |
| `+0x08` | u32  | unknown_08           | Always observed as `0`; see Open Questions                               |
| `+0x0C` | u16  | unknown_0c           | Always observed as `2`; see Open Questions                               |
| `+0x0E` | u8   | work_ani_type        | `gc::EWorkAniType`, see below                                            |
| `+0x0F` | u16  | productivity_upgrade_group_index | `PlantUpgradeParam_Table` index; always observed as `101`; note unaligned offset |
| `+0x11` | u16  | luck_productivity_upgrade_group_index | `PlantUpgradeParam_Table` index; always observed as `201`; note unaligned offset |
| `+0x13` | u32  | production_count     | Number of (`production_key`, `max_capacity_level`) pairs; always observed as `1`; note unaligned offset |
| `+0x17` | u16  | production_key       | `plantexchangegroup.bss` key; note unaligned offset                      |
| `+0x19` | u16  | max_capacity_level   | The sheet's `MaxCapacityLevel` minus 1; usually `0`, see below           |
| `+0x1B` | u32  | worker_species_count | Number of trailing `worker_species`; observed `1`, `3`, or `6`           |
| `+0x1F` | u8[worker_species_count] | worker_species | Worker species values, `worker_species_count` bytes; not a worker lock   |

`+0x13` to `+0x1A` is a list: the 2016 client keeps `_productionList`, a map from the exchange group key to a `ProductionInfo` with `_maxCountLevel`. Every zone lists one pair, so the offsets after it are fixed; the parser raises an error on a zone with another count. Earlier versions of this doc read `+0x17` as one u32 `production_key` with an unexplained high word; that high word is `max_capacity_level`. Earlier versions also called `work_ani_type` `variant` and `unknown_0e`.

Observed record-size distribution:

| Size | Count | `worker_species_count` | `worker_species`    | Zones                                     |
| ---- | ----- | ---------------------- | ------------------- | ----------------------------------------- |
| 32   | 2     | 1                      | `06`                | Dokkebi Forest excavation (1807, 1808)    |
| 34   | 42    | 3                      | `06 07 08`          | Land of the Morning Light production nodes |
| 37   | 350   | 6                      | `00 01 02 03 04 05` | All other zones                           |

### `plantzoneoffset.dbss`

Provides the byte ranges for records in `plantzone.dbss`.

| Offset  | Type                     | Field        | Notes                             |
| ------- | ------------------------ | ------------ | --------------------------------- |
| `+0x00` | u32                      | record_count | Must equal `plantzone.dbss` count |
| `+0x04` | Offset Row[record_count] | rows         | 12-byte rows repeated `count` times |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                             |
| ------- | ---- | ----------- | ------------------------------------------------- |
| `+0x00` | u16  | record_id   | Matches `plantzone.dbss` record `+0x00`           |
| `+0x02` | u16  | unknown_02  | Always `0`                                        |
| `+0x04` | u32  | data_offset | Absolute byte offset into `plantzone.dbss`        |
| `+0x08` | u32  | data_size   | Record payload byte count: `32`, `34`, or `37`    |

Offset rows are not sorted by `data_offset`, but sorted rows cover every byte from `plantzone.dbss +0x04` through EOF with no gaps or overlaps. The parser reads `record_id` and `unknown_02` as one u32 (`parse_bare_u32_offset_rows()`).

## Layout 1

On client 1784 a Plant Zone Record was 27 bytes: it ended after
`max_capacity_level`, without `worker_species_count` and `worker_species`.
Only the Plant Zone Record differs from Layout 2; every offset row's
`data_size` is `27`. On client 1784 the file holds 309 records.

### Plant Zone Record (27 bytes)

| Offset  | Type | Field                                 | Notes |
| ------- | ---- | ------------------------------------- | ----- |
| `+0x00` | u32  | record_id                             |       |
| `+0x04` | u32  | unknown_04                            |       |
| `+0x08` | u32  | unknown_08                            |       |
| `+0x0C` | u16  | unknown_0c                            |       |
| `+0x0E` | u8   | work_ani_type                         |       |
| `+0x0F` | u16  | productivity_upgrade_group_index      |       |
| `+0x11` | u16  | luck_productivity_upgrade_group_index |       |
| `+0x13` | u32  | production_count                      |       |
| `+0x17` | u16  | production_key                        |       |
| `+0x19` | u16  | max_capacity_level                    |       |

## `worker_species` Values

The same byte is the last byte (`+0x38F`) of every `plantworker.bss` record. Names below come from the LOC type 6 names of the workers carrying each value; the client enum for this byte was not found in `global_define_cpp_enum.luac`.

| Value | Workers                                                  |
| ----- | -------------------------------------------------------- |
| 0     | Goblin workers (plus named special workers such as Torres, Darifu) |
| 1     | Human workers (plus Demibeast workers)                   |
| 2     | Giant workers                                            |
| 3     | Papu workers                                             |
| 4     | Fadus workers                                            |
| 5     | Dwarf workers                                            |
| 6     | Dokkebi workers                                          |
| 7     | Dolswe workers                                           |
| 8     | Shellfolk workers                                        |

## `work_ani_type` Values

Names from `gc::EWorkAniType` of the 2016 client's debug symbols. On client 3473 the zones use `0` to `4`; the `exploration.bss` `node_kind` of each zone's node, counted per value:

| Value | Name         | Zones | Node kinds |
| ----- | ------------ | ----- | ---------- |
| 0     | Mining       | 84    | Quarry 79, MonopolyFarm 3, Excavation 1, Logging 1 |
| 1     | Gather       | 80    | Collect 46, Farm 15, Excavation 12, MonopolyFarm 4, Logging 2, Craft 1 |
| 2     | Cultivation  | 63    | Farm 35, Collect 13, MonopolyFarm 11, Quarry 2, Logging 2 |
| 3     | Logging      | 77    | Logging 73, Excavation 3, Quarry 1 |
| 4     | Making       | 135   | FishTrap 41, Excavation 34, MonopolyFarm 25, Finance 24, Craft 7, MinorFinance 2, Logging 1, Quarry 1 |
| 5     | Architecture | 0     | |
| 6     | Hide         | 0     | |
| 7     | HouseParty   | 0     | |
| 8     | Breeding     | 0     | |

The value does not follow the node kind: Farm nodes split between Gather and Cultivation, and Excavation nodes fall under four of the five.

## `max_capacity_level` Values

On client 3473, `max_capacity_level` is `0` on 420 zones and `1` to `7` on 19 (`node_kind` MonopolyFarm 15, Quarry 2, Collect 1, Excavation 1):

| `max_capacity_level` | Zones |
| -------------------- | ----- |
| `0`                  | 420   |
| `1`                  | 3     |
| `2`                  | 6     |
| `3`                  | 2     |
| `4`                  | 2     |
| `5`                  | 2     |
| `6`                  | 2     |
| `7`                  | 2     |

It counts up across consecutive Specialties (MonopolyFarm) node keys: 104-110 (Balenos farms such as Bartali, Finto and Wale Farm) carry `1`-`7`, and 613-619 (Calpheon farms such as Falres Dirt and Dias Farm) carry `1`-`7` again. All `production_key` values are `plantexchangegroup.bss` keys; read together with `max_capacity_level` as a u32, the 19 non-zero ones are not.

## Production Item Chain

```text
production_key -> plantexchangegroup.bss production_key (+0x00)
plantexchangegroup.bss exchange_key (+0x06) -> itemexchangesource.bss key
itemexchangesource.bss product_drop_key, luck_drop_key -> itemmaingroup.bss group_id
itemmaingroup.bss subgroup keys -> itemsubgroup.dbss entries -> item_key & 0xFFFFFF -> item name (LOC type 0)
```

The tables are documented in [plantexchangegroup_bss.md](plantexchangegroup_bss.md), [itemexchangesource_bss.md](itemexchangesource_bss.md), [itemmaingroup_bss.md](itemmaingroup_bss.md) and [itemsubgroup_dbss.md](itemsubgroup_dbss.md); row counts for the chain are in [`plantexchangegroup.bss` Field Names](plantexchangegroup_bss.md#field-names). The Produced Items column shows the product drop group, read from the `PRODUCTION_ITEMS` lookup index (see `docs/handler.md`), and the Luck Drops column the luck drop group, read from `PRODUCTION_LUCK_ITEMS`.

Example: zone 2050 (Lumbering) -> production key 1928 -> exchange 42356 -> product group 42356 -> subgroup 42356 -> Elder Tree Timber, Bloody Tree Knot, Elder Tree Sap. On client 3474 all 439 zones resolve to items, and 370 of them also have a luck drop group with items.

Earlier versions of the handler read `+0x06` as an `itemsubgroup.dbss` key, which left 36 zones without items: their exchange key has no subgroup of the same number. All 36 resolve through the exchange. Zone 2051 `Fish Drying Yard` (production key 1929, exchange 45018) is one of them: the exchange drops group 44064 (4 items) with luck group 41165 (2 items), the 4 items plus 2 lucky drops the zone produces in game.

## Field Names

The names of `work_ani_type`, `productivity_upgrade_group_index`, `luck_productivity_upgrade_group_index`, `production_key` and `max_capacity_level` follow the `PlantZone_Table` and `PlantZoneWorking_Table` sheets of a private server's `DataSheets.bexcel` on client 1784 (columns `WorkAniType`, `ProductivityUpgradeGroupIndex`, `LuckProductivityUpgradeGroupIndex`, `ExchangeGroupIndex`, `MaxCapacityLevel`) and the same tables of a second private server on client 519. Matched by value over the zone keys (`WaypointKey`) each shares with client 3473:

| Column | Field | Equal (client 1784, 304 keys) | Equal (client 519, 288 keys) |
| ------ | ----- | ------------------------ | ------------------------ |
| `WorkAniType` | `work_ani_type` | 303 | 273 |
| `ExchangeGroupIndex` | `production_key` | 293 | 277 |
| `MaxCapacityLevel` | `max_capacity_level` + 1 | 304 | 288 |

Both sheets store `101` and `201` in the two upgrade-group columns on every row, and `PlantUpgradeParam_Table` has rows with index `101` and `201`. The client Lua enum `CppEnums.PlantZoneLevelType` (`global_define_cpp_enum.luac`) has the two matching levels, `ePlantZoneLevelType_GeneralEfficiency` (`0`) and `ePlantZoneLevelType_LuckEfficiency` (`1`); no other Lua file uses it. The 2016 client (build of 2016-01-11) ships with debug symbols: `gc::PlantZoneStaticStatus` holds `_productCategory`, `_workAniType`, `_productivityParamKey`, `_luckProductivityParamKey` and `_productionList` in this order, the order of `+0x0E` to `+0x1A` here; `GameCommonParameterLoaderFromExcel::LoadPlantZoneStaticInformation` reads `WorkAniType` into `_workAniType` and the two upgrade-group columns into the two param keys. `_productionList` maps the exchange group key to `_maxCountLevel`, filled from `PlantZoneWorking_Table`.

The file has no field for `ContentsGroupKey` (10 distinct values in the bexcel). The private server's own `plantzone.dbss` (client 1784) has 309 zones of 27 bytes each: the same fields up to `max_capacity_level`, with no worker species list.

## Notes

- `plantzone.dbss` and `plantzoneoffset.dbss` both report `394` records.
- The offset table's `record_id` equals the record payload's first u32 for all records.
- `worker_species_count` always equals the number of trailing bytes.
- Every `record_id` is an `exploration.bss` sub-node (`is_sub_node=1`) of a production kind; only three production sub-nodes have no plant zone (1564 Specialties and the disabled `UnKnown` records 1831 and 1839).
- The reference project reports 425 plant zones with 389 resolving to items; reading `+0x06` of `plantexchangegroup.bss` as a subgroup key, the client file had 394 zones with 358 resolving, and the same 36 unresolved. The exchange chain resolves all of them (see Production Item Chain).
- Worker output quantities are not identified in these tables. The luck bonus drops are the luck drop group of the production key's exchange (see Production Item Chain).

## Open Questions

### The Constant Block at `+0x04`

`unknown_04` (`2`), `unknown_08` (`0`) and `unknown_0c` (`2`) are constant on clients 1784 and 3473, and so are the sheet columns that have no field yet: `PlantObjectKind` (`2`, the 2016 `_productCategory`, where `2` is `ProductCategory_Farm`), `UpgradeResource` (`2`, `_upgradeResourceKey`), `MaxLevel` (`_maxLevel`), `WorkableCount` (`_workableCountMax`) and `isRandomRecipeLevel` (all `0`). The 10 bytes do not follow the 2016 member order, where `_productCategory` sits right before `_workAniType` (`+0x0D`, always `0` here), so neither value nor order tells which column each byte holds.

### What `max_capacity_level` Controls

It is `1` to `7` only on 19 zones, mostly consecutive Specialties nodes. The client 519 private server loads `MaxCapacityLevel` into `PlantZoneWorkingT` but never reads it back, and the client Lua has no getter for it.

### What `worker_species` Controls

It is not a per-zone worker lock. In game, which worker types can be hired is
set per town, and any hired worker can work any node connected to its town
(I checked in game, 2026-09-27). The list still differs by region: 350
zones list the six base species (Goblin to Dwarf), the 42 Land of the Morning
Light zones only Dokkebi, Dolswe and Shellfolk, and the two Dokkebi Forest
excavation zones only Dokkebi. The values match the `plantworker.bss` species
byte, but what the client uses the list for (a bonus, a default, a leftover
restriction) is unknown.
