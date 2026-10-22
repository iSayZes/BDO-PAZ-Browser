# `houseworking.dbss` Format

## Purpose

The work a worker can do at a crafting tool installed in a house: one row
per tool installation character (Metal Processing Tool `1001`,
Intermediate Cooking Utensil `1032`) with a list of item exchanges and a
unit production for each. On client 3482 the 17 rows each hold one entry,
exchange `5001` with unit production `3`. Companion `houseworkingoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records         | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | --------------- | --------- |
| 2      | 2765 and later | 3482    | `houseworking.dbss`       | 242   | 17 Work, 17 Row | 8         |
| 2      | 2765 and later | 3482    | `houseworkingoffset.dbss` | 174   | 17 Offset Row   | 10        |
| 1      | 1348 to 2519   | 2519    | `houseworking.dbss`       | 208   | 17 Work, 17 Row | 6         |
| 1      | 1348 to 2519   | 2519    | `houseworkingoffset.dbss` | 174   | 17 Offset Row   | 10        |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 2      | `houseworking.dbss`       | 242 B (100.0%) | 0 B (0.0%) |
| 2      | `houseworkingoffset.dbss` | 174 B (100.0%) | 0 B (0.0%) |
| 1      | `houseworking.dbss`       | 208 B (100.0%) | 0 B (0.0%) |
| 1      | `houseworkingoffset.dbss` | 174 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2765   | Layout 2 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                      |
| ---------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `houseworkingoffset.dbss`    | Optional | `install_object_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a tool key without a row shows as plain text           |
| `languagedata_en.loc`        | Optional | Tool names (type 6) and exchange names (type 24)                                           |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3482 the file is 4 + 17 x 14 = 242 bytes.

### Row (variable: 6 bytes + works)

| Offset       | Type             | Field              | Notes                                                                 |
| ------------ | ---------------- | ------------------ | --------------------------------------------------------------------- |
| `+0x00`      | u32              | work_count         | Number of `works`; `1` on every row (clients 1784 and 3482)           |
| `+0x04`      | Work[work_count] | works              | See Work                                                              |
| `works+0x00` | u16              | install_object_key | Row key: the tool installation, a `characterstatic.dbss` character     |

The rows are in no key order; client 3482 opens with 1032, 1028, 1025.

### Work (8 bytes)

| Offset  | Type | Field           | Notes                                                                                   |
| ------- | ---- | --------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | exchange_key    | An [`itemexchangesource.bss`](itemexchangesource_bss.md) key; `5001` (Veid Longsword) on every row |
| `+0x04` | u32  | unit_production | `3` on every row                                                                        |

### `houseworkingoffset.dbss`

Bare offset table into `houseworking.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `houseworking.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (10 bytes)

| Offset  | Type | Field              | Notes                                                      |
| ------- | ---- | ------------------ | ---------------------------------------------------------- |
| `+0x00` | u16  | install_object_key | Key of the row it points at                                |
| `+0x02` | u32  | data_offset        | Absolute offset of the row in `houseworking.dbss`, at `work_count` |
| `+0x06` | u32  | data_size          | The whole row: `14` on every row of client 3482            |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on clients 1784 and 3482 every index row points at
the row whose `install_object_key` is its key.

## Layout 1

The exchange key is a u16, so a work entry is 6 bytes and a row 12
(`data_size` `12`). Only the Work differs from Layout 2.

### Work (6 bytes)

| Offset  | Type | Field           | Notes                                    |
| ------- | ---- | --------------- | ---------------------------------------- |
| `+0x00` | u16  | exchange_key    | `5001` on every row (client 1784)        |
| `+0x02` | u32  | unit_production | `3` on every row (client 1784)           |

## Field Names

The `PlantHouseWorking_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `InstallObjectKey`,
`ExchangeKey` and `UnitProduction`, 17 rows. The 2016
`gc::HouseWorkingStaticStatus` holds `_key` (u16) and `_availableWorkList`,
a map of u16 exchange key to `gc::PlantWorking` (`_key`, `_unitProduction`);
the client file stores the map as `work_count` and its entries, before the
key.

| Field              | Column             | Same value (client 1784) | Same value (client 3482) |
| ------------------ | ------------------ | ------------------------ | ------------------------ |
| install_object_key | `InstallObjectKey` | 17 of 17                 | 17 of 17                 |
| exchange_key       | `ExchangeKey`      | 17 of 17                 | 17 of 17                 |
| unit_production    | `UnitProduction`   | 17 of 17                 | 17 of 17                 |

## Notes

- The 17 keys are tool installations (LOC type 6): Metal Processing Tool
  (`1001`) to Furniture Crafting Tool (`1008`), Crafting Tool (`1025`),
  Cooking Utensil (`1028`), Intermediate Cooking Utensil (`1032`) and
  `1521` to `1525` and `1527`, Weapon Refining Tool (Metal) to Masonry Tool.
- Exchange `5001` is the Veid Longsword exchange of
  [`itemexchangesource.bss`](itemexchangesource_bss.md); every row of
  clients 1784 and 3482 holds it.
- The worker Lua (`new_worldmap_household.luac`,
  `panel_worldmap_housemanagement_renew.luac` and four more) lists the
  workers of a house through `ToClient_getHouseWorkingWorkerList(houseInfo)`
  and `ToClient_getHouseWorkingWorkerByIndex(houseInfo, index)`; those calls
  take a house, not a tool key, and no Lua call names this table's fields.
