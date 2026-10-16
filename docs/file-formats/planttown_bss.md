# `planttown.bss` Format

## Purpose

Town table of the worker system: one row per town node where workers can be hired, with the keys of its warehouse and worker capacity upgrades, its max upgrade level and its upgrade cost group. Node IDs resolve through LOC type `29`; most rows are towns, villages, guard posts, islands, or trade-zone nodes.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | --------------- | ----- | ----------------- | --------- |
| 1      | 3473 and later | 3473    | `planttown.bss` | 572   | 46 Plant Town Row | 12        |

| Layout | File            | Known          | Unknown    |
| ------ | --------------- | -------------- | ---------- |
| 1      | `planttown.bss` | 572 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                           |
| --------------------- | -------- | ---------------------------------------------- |
| `languagedata_en.loc` | Optional | Resolves `node_id` display names via type `29` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

Rows start immediately after the header at `+0x08`. The observed file is fully described by:

```text
8-byte header + (45 * 12-byte rows) + 12-byte trailer = 560 bytes
```

The 2026-09-27 client holds 46 rows in 572 bytes.

| Offset              | Type                   | Field        | Notes                                                |
| ------------------- | ---------------------- | ------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]                | magic        | `PABR` (ASCII)                                       |
| `+0x04`             | u32                    | count        | Number of rows; observed `45` in the pre-2026-09-27 fixture, `46` in the 2026-09-27 client |
| `+0x08`             | Plant Town Row[count]  | rows         | See Plant Town Row                                   |
| `rows+0x00`         | String Table           | string_table | The 12-byte trailer starts here; see String Table    |
| `string_table+0x00` | u32                    | end_of_rows  | Byte offset immediately after rows; `8 + count * 12`; observed `548` |
| `string_table+0x04` | u32                    | zero         | Observed zero                                        |

### Plant Town Row (12 bytes)

| Offset  | Type | Field                               | Notes                                         |
| ------- | ---- | ----------------------------------- | --------------------------------------------- |
| `+0x00` | u32  | node_id                             | LOC type `29`, `str_id1=node_id`, `str_id4=0` |
| `+0x04` | u16  | warehouse_upgrade_group_index       | Key into [plantupgradeparam.bss](plantupgradeparam_bss.md); `1` in every row |
| `+0x06` | u16  | worker_capacity_upgrade_group_index | Key into [plantupgradeparam.bss](plantupgradeparam_bss.md); `2` in every row |
| `+0x08` | i16  | max_level                           | Highest upgrade level; `10` in every row      |
| `+0x0A` | u16  | upgrade_resource_key                | Level group in [plantupgraderesource.bss](plantupgraderesource_bss.md); `1` in every row |

The constants hold on all 46 rows of client 3473. Earlier versions of this doc called the four fields `unknown_04` to `unknown_0a`, and before that `unknown_a` to `unknown_d`.

Derived field:

```text
node_name = LOC type 29, str_id1=node_id, str_id4=0
```

### String Table (variable: 4 bytes + strings)

The PABR string table, here with no strings.

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Observed zero           |
| `+0x04` | pstr[string_count] | strings      | Empty                   |

## Reference Rows

| Row | Node ID | Node Name              | Warehouse | Worker Capacity | Max Level | Upgrade Resource |
| --: | ------: | ---------------------- | --------: | --------------: | --------: | ---------------: |
|   0 |  `1785` | Nampo's Moodle Village |        `1` |        `2` |       `10` |        `1` |
|   1 |  `1781` | Dalbeol Village        |        `1` |        `2` |       `10` |        `1` |
|   8 |  `1623` | Grána                  |        `1` |        `2` |       `10` |        `1` |
|  18 |  `1141` | Tarif                  |        `1` |        `2` |       `10` |        `1` |
|  25 |  `1301` | Valencia City          |        `1` |        `2` |       `10` |        `1` |
|  32 |   `601` | Calpheon               |        `1` |        `2` |       `10` |        `1` |
|  42 |     `1` | Velia                  |        `1` |        `2` |       `10` |        `1` |
|  44 |   `301` | Heidel                 |        `1` |        `2` |       `10` |        `1` |

Row numbers are from the pre-2026-09-27 fixture. The 2026-09-27 client inserts Angavu Outpost (`2057`) as row 0, so every row above moves down by one.

## Notes

- Observed decompressed size is `560` bytes.
- `planttown.bss` has no same-stem companion file in the PAZ listing.
- All 45 `node_id` values resolve through LOC type `29` with `str_id4=0`.
- The row order follows neither the node IDs nor the sheet's row order, see Open Questions.
- `plantworkerselect.bss` uses related town selection data, but its IDs are not a direct match for this file; for example `planttown.bss` uses node `601` for Calpheon, while `plantworkerselect.bss` uses selection ID `77` for Calpheon City.

## Field Names

The names follow the `PlantTown_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (columns `WaypointKey`, `WarehouseUpgradeGroupIndex`, `WorkerCapacityUpgradeGroupIndex`, `MaxLevel`, `UpgradeResource`) and the 2016 `gc::PlantTownStaticStatus` member order (`_key`, `_isBlockedNpcWork`, `_warehouseParamKey`, `_workerCapacityParamKey`, `_maxLevel` as a short, `_upgradeResourceKey`). The sheet's 35 towns hold `1`, `2`, `10`, `1`, the values of the file's 34 shared rows, so the names rest on the column order and the 2016 member order, not on a value match. The 2016 `_isBlockedNpcWork` bool has no byte in the record. The client Lua enum `CppEnums.PlantTownLevelType` (`global_define_cpp_enum.luac`) lists the two town level types in the same order: `ePlantTownLevelType_Warehouse` (`0`) and `ePlantTownLevelType_WorkerCapacity` (`1`).

- `warehouse_upgrade_group_index` and `worker_capacity_upgrade_group_index` are keys of [plantupgradeparam.bss](plantupgradeparam_bss.md) (1 warehouse, 2 worker capacity).
- `upgrade_resource_key` is a level group of [plantupgraderesource.bss](plantupgraderesource_bss.md) (1, town, levels 1 to 16).

## Open Questions

### Row Order Meaning

The rows follow neither the node IDs nor the `PlantTown_Table` row order (the sheet starts Velia, Western Guard Camp, Olvia, Heidel, Glish; the file ends Olvia, Western Guard Camp, Velia, Glish, Heidel). The 2016 client loads the table into a `pa::BinaryUnorderedMap<gc::PlantKey, ...>`, a hash map keyed by node, so the order may only be that container's storage order. Whether any client code reads the rows in file order is not checked.
