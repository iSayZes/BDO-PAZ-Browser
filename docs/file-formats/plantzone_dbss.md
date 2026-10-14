# `plantzone.dbss` Format

## Purpose

Defines worker production zones. Each record belongs to one worldmap production sub-node (`record_id` is an `exploration.bss` node key, named through LOC type 29), carries several invariant control fields and one unknown byte that tracks the production type, links to a production key in `plantexchangegroup.bss`, and lists a set of worker species per zone (not a worker lock; its use is unknown, see Open Questions). `plantzoneoffset.dbss` is required to address the variable-length records.

```text
Observed records: 394 in the pre-2026-09-27 fixture, 439 in the 2026-09-27 client (45 more 37-byte zones). Record payloads are 32, 34, or 37 bytes depending on the worker-species list length.
record_id=1539 -> Teff, production key 1539 -> item subgroup 40189 -> Teff
```

The production-key reading and the worker-species field boundaries follow [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, "Worker-production item tables"), checked against the current client files below.

## Companion Files

| File                   | Required | Role                                                   |
| ---------------------- | -------- | ------------------------------------------------------ |
| `plantzoneoffset.dbss` | Required | Maps `record_id` to byte offset and payload byte count |

All multi-byte values are little-endian unless noted otherwise.

## File Layout

| Offset  | Type | Field         | Notes                                      |
| ------- | ---- | ------------- | ------------------------------------------ |
| `+0x00` | u32  | record_count  | Number of records; observed `394` (2026-09-27 client: `439`) |
| `+0x04` | ...  | record_stream | Variable-length records, packed back-to-back |

`(file_size - 4) / record_count` is not integral, so records must be sliced with `plantzoneoffset.dbss`.

## Record Structure

### Plant Zone Record (32, 34, or 37 bytes)

| Offset  | Type | Field                | Notes                                                                    |
| ------- | ---- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | record_id            | `exploration.bss` node key; matches `record_id` in `plantzoneoffset.dbss` |
| `+0x04` | u32  | unknown_04           | Always observed as `2`                                                   |
| `+0x08` | u32  | unknown_08           | Always observed as `0`                                                   |
| `+0x0C` | u16  | unknown_0c           | Always observed as `2`                                                   |
| `+0x0E` | u8   | unknown_0e           | Observed range `0`-`4`; correlates with node kind, see below             |
| `+0x0F` | u16  | unknown_0f           | Always observed as `101`; note unaligned offset                          |
| `+0x11` | u16  | unknown_11           | Always observed as `201`; note unaligned offset                          |
| `+0x13` | u32  | unknown_13           | Always observed as `1`; note unaligned offset                            |
| `+0x17` | u16  | production_key       | `plantexchangegroup.bss` key; note unaligned offset                      |
| `+0x19` | u16  | unknown_19           | Usually `0`; counts up across Specialties nodes, see below               |
| `+0x1B` | u32  | worker_species_count | Number of trailing `worker_species`; observed `1`, `3`, or `6`           |
| `+0x1F` | u8[] | worker_species       | Worker species values, `worker_species_count` bytes; not a worker lock   |

Earlier versions of this doc read `+0x17` as one u32 `production_key` with an unexplained high word; that high word is `unknown_19`. Earlier versions also called `unknown_0e` `variant`.

Observed record-size distribution:

| Size | Count | `worker_species_count` | `worker_species`    | Zones                                     |
| ---- | ----- | ---------------------- | ------------------- | ----------------------------------------- |
| 32   | 2     | 1                      | `06`                | Dokkebi Forest excavation (1807, 1808)    |
| 34   | 42    | 3                      | `06 07 08`          | Land of the Morning Light production nodes |
| 37   | 350   | 6                      | `00 01 02 03 04 05` | All other zones                           |

### `worker_species` Values

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

### `unknown_0e` by Node Kind

`exploration.bss` `node_kind` of the zone's node, counted per `unknown_0e`:

| `unknown_0e` | Dominant kinds                                              |
| --------- | -------------------------------------------------------------- |
| 0         | Quarry 66, MonopolyFarm 3, Logging 1, Excavation 1             |
| 1         | Collect 48, Farm 15, Excavation 6, MonopolyFarm 4, Craft 1     |
| 2         | Farm 35, Collect 13, MonopolyFarm 11                           |
| 3         | Logging 62, Excavation 3, Quarry 1                             |
| 4         | FishTrap 41, MonopolyFarm 25, Finance 24, Excavation 24, Craft 6, MinorFinance 2, Quarry 1, Logging 1 |

### `unknown_19` Values

`unknown_19` is `0` on 375 records. Nineteen records (15 Specialties, 2 Mining, 1 Gathering, 1 Excavation) have a non-zero value:

| `unknown_19` | Count | `production_key` range |
| ------------ | ----- | ---------------- |
| `0`          | 375   | `1`-`2044`       |
| `1`          | 3     | `960`-`1235`     |
| `2`          | 6     | `23`-`1213`      |
| `3`          | 2     | `962`-`970`      |
| `4`          | 2     | `963`-`971`      |
| `5`          | 2     | `972`-`975`      |
| `6`          | 2     | `973`-`976`      |
| `7`          | 2     | `974`-`977`      |

It counts up across consecutive Specialties node keys: 104-110 (Balenos farms such as Bartali, Finto and Wale Farm) carry `1`-`7`, and 613-619 (Calpheon farms such as Falres Dirt and Dias Farm) carry `1`-`7` again. All 394 `production_key` values are `plantexchangegroup.bss` keys; read together with `unknown_19` as a u32, only 375 are.

### Production Item Chain

```text
production_key -> plantexchangegroup.bss production_key (+0x00)
plantexchangegroup.bss item_subgroup_key (+0x06) -> itemsubgroup.dbss subgroup_key
itemsubgroup.dbss entries -> item_key & 0xFFFFFF -> item name (LOC type 0)
```

Both tables are documented in [plantexchangegroup_bss.md](plantexchangegroup_bss.md) and [itemsubgroup_dbss.md](itemsubgroup_dbss.md). The client goes one step further: `+0x06` is an item exchange key, and the items come from that exchange's drop group in [`itemmaingroup.bss`](itemmaingroup_bss.md) (chain and row counts in [`plantexchangegroup.bss` Field Names](plantexchangegroup_bss.md#field-names)). The subgroup reading above matches the client on most zones because the three keys often share one number.

Example: zone 2050 (Lumbering) -> production key 1928 -> subgroup 42356 -> Elder Tree Timber, Bloody Tree Knot, Elder Tree Sap. On the 2026-09-27 client 403 of the 439 zones resolve to items; the other 36 reference subgroup keys that are absent from `itemsubgroupoffset.dbss` (358 of 394 in the older fixture, the same 36 unresolved).

## `plantzoneoffset.dbss`

Provides the byte ranges for records in `plantzone.dbss`.

| Offset  | Type | Field        | Notes                             |
| ------- | ---- | ------------ | --------------------------------- |
| `+0x00` | u32  | record_count | Must equal `plantzone.dbss` count |
| `+0x04` | ...  | rows         | 12-byte rows repeated `count` times |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                             |
| ------- | ---- | ----------- | ------------------------------------------------- |
| `+0x00` | u16  | record_id   | Matches `plantzone.dbss` record `+0x00`           |
| `+0x02` | u16  | zero        | Always observed as `0`                            |
| `+0x04` | u32  | data_offset | Absolute byte offset into `plantzone.dbss`        |
| `+0x08` | u32  | data_size   | Record payload byte count: `32`, `34`, or `37`    |

Offset rows are not sorted by `data_offset`, but sorted rows cover every byte from `plantzone.dbss +0x04` through EOF with no gaps or overlaps. The parser reads `record_id` and `zero` as one u32 (`parse_bare_u32_offset_rows()`).

## Suggested UI Layout

| Column         | Type | Notes                                               |
| -------------- | ---- | --------------------------------------------------- |
| Zone ID        | num  | `record_id`                                         |
| Node Name      | text | LOC type 29, `str_id1=record_id`, `str_id4=0`       |
| Production Key | num  | `production_key`                                    |
| Produced Items | text | Icon and LOC type 0 name of each item in its grade colour (`ITEM_GRADE`) through the Production Item Chain, read from the `PRODUCTION_ITEMS` lookup index; a dash for the 36 unresolved zones |

The table meta line counts the zones that resolve to items (403 of 439 on client 3458). The preview needs no `plantexchangegroup.bss` or `itemsubgroup.dbss` companion: `production_item_fields()` in `_common/production_items.py` gives the item keys and names, the same helper the `plantexchangegroup.bss` Items column uses, and `item_key_list_cell()` in `_common/item_key.py` draws both columns.

## Notes

- `plantzone.dbss` and `plantzoneoffset.dbss` both report `394` records.
- The offset table's `record_id` equals the record payload's first u32 for all records.
- `worker_species_count` always equals the number of trailing bytes.
- Every `record_id` is an `exploration.bss` sub-node (`is_sub_node=1`) of a production kind; only three production sub-nodes have no plant zone (1564 Specialties and the disabled `UnKnown` records 1831 and 1839).
- The reference project reports 425 plant zones with 389 resolving to items; the current client file has 394 zones with 358 resolving, and the same 36 unresolved.
- Worker output quantities and luck bonus drops are not identified in these tables.

## Open Questions

### `unknown_0e` Meaning

`unknown_0e` tracks the production type (Quarry is mostly `0`, Logging `3`, Fish Drying/Finance `4`) but Farm, Collect, MonopolyFarm and Excavation nodes are split across several values, so it is not simply the node kind. It may be a worker-stat or work-type class; the client enum was not identified.

### `unknown_19` Meaning

`unknown_19` counts up across consecutive Specialties node keys on 19 records. Whether the client uses it (for example as a display order or unlock step) is not confirmed.

### Unresolved Subgroups

36 zones point at production keys whose subgroup key is missing from `itemsubgroupoffset.dbss`. They are not empty: in game zone 2051 `Fish Drying Yard` (production key 1929, subgroup 45018) produces 4 items plus 2 lucky drops. The key is an item exchange key, and on client 3464 all 36 resolve through the exchange's drop group in `itemmaingroup.bss` (1929: exchange 45018 drops group 44064). The handler resolves them once `itemexchangesource.bss` has a reader; see [`plantexchangegroup.bss` Field Names](plantexchangegroup_bss.md#field-names).

### What `worker_species` Controls

It is not a per-zone worker lock. In game, which worker types can be hired is
set per town, and any hired worker can work any node connected to its town
(I checked in game, 2026-09-27). The list still differs by region: 350
zones list the six base species (Goblin to Dwarf), the 42 Land of the Morning
Light zones only Dokkebi, Dolswe and Shellfolk, and the two Dokkebi Forest
excavation zones only Dokkebi. The values match the `plantworker.bss` species
byte, but what the client uses the list for (a bonus, a default, a leftover
restriction) is unknown.
