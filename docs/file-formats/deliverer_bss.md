# `deliverer.bss` Format

## Purpose

The wagons and ships that carry goods between towns for the Transport
window and drive along their routes on the world map: one row per carrier
character with its route number, load, fee, world map model, the names of
up to 20 route waypoints and its `CppEnums.DelivererType`. The world map
Lua (`new_worldmap_actortooltip.luac`) reads the type from a carrier icon
through `FromClient_getDelivererType()` and opens no cargo window for a
`WagonForPerson` or `OfferingCarrier`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------- | ----- | ------- | --------- |
| 2      | 2519 and later | 3482    | `deliverer.bss` | 7,497 | 27 Row  | 106       |
| 1      | 1230 to 2313   | 2313    | `deliverer.bss` | 6,473 | 23 Row  | 104       |

| Layout | File            | Known            | Unknown     |
| ------ | --------------- | ---------------- | ----------- |
| 2      | `deliverer.bss` | 7,470 B (99.6%)  | 27 B (0.4%) |
| 1      | `deliverer.bss` | 6,473 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3251   | Layout 2             |
| 3002   | Layout 2             |
| 2765   | Layout 2             |
| 2519   | Layout 2             |
| 2313   | Layout 1             |
| 2107   | Layout 1             |
| 1937   | Layout 1             |
| 1784   | Layout 1             |
| 1636   | Layout 1             |
| 1485   | Layout 1             |
| 1348   | Layout 1             |
| 1230   | Layout 1             |
| 1058   | No file              |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                            |
| ---------------------------- | -------- | ------------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a carrier key without a row shows as plain text |
| `languagedata_en.loc`        | Optional | Carrier names, LOC type 6                                                       |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of carriers                            |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (106 bytes)

| Offset  | Type    | Field                 | Notes                                                                                     |
| ------- | ------- | --------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16     | character_key         | Carrier character (LOC type 6 name, `522` Velia Freight Wagon); the rows are in no key order |
| `+0x02` | u16     | character_key_dup     | Equals `character_key` on every row                                                       |
| `+0x04` | u32     | delivery_route        | Route number, `1` to `34` on client 3482; the Altinova (`791`) and O'dyllita (`809`) Freight Wagons share `25` |
| `+0x08` | u32     | load_age              | `30` on every row of clients 1784 and 3482                                                |
| `+0x0C` | i64     | fee                   | `10` on every row of clients 1784 and 3482                                                |
| `+0x14` | u32     | object_file_index     | Index into `strings`: the world map model (`WorldMap/WorldMap_Cart.pam`)                  |
| `+0x18` | u32[20] | waypoint_name_indexes | Indexes into `strings`: waypoint names along the route (`loopline_1`); an unused slot points at an empty string |
| `+0x68` | u8      | deliverer_type        | `CppEnums.DelivererType`; see Deliverer Type                                              |
| `+0x69` | u8      | unknown_69            | `0` on every row of client 3482                                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                   |
| ------- | ------------------ | ------------ | ----------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                       |
| `+0x04` | pstr[string_count] | strings      | Model paths and waypoint names, UTF-16LE; a string several rows use is stored once |

## Layout 1

No `deliverer_type` and `unknown_69` at the end of the row. Only the Row
differs from Layout 2.

### Row (104 bytes)

| Offset  | Type    | Field                 | Notes |
| ------- | ------- | --------------------- | ----- |
| `+0x00` | u16     | character_key         |       |
| `+0x02` | u16     | character_key_dup     |       |
| `+0x04` | u32     | delivery_route        |       |
| `+0x08` | u32     | load_age              |       |
| `+0x0C` | i64     | fee                   |       |
| `+0x14` | u32     | object_file_index     |       |
| `+0x18` | u32[20] | waypoint_name_indexes |       |

## Deliverer Type

`CppEnums.DelivererType` of the client 3482 Lua
(`global_define_cpp_enum.luac`). Rows on client 3482 in the last column;
the type follows the model on every row but two `WoodenBoat_small` ships.

| Value | Name            | Models (client 3482)                                  | Rows (client 3482) |
| ----- | --------------- | ----------------------------------------------------- | ------------------ |
| 0     | NotDeliverer    |                                                       | 0                  |
| 1     | Wagon           | `WorldMap_Cart.pam`                                   | 13                 |
| 2     | TransportShip   | `WorldMap_WoodenBoat_small.pam`                       | 2                  |
| 3     | TradingShip     | `WorldMap_SailingShip.pam`, `Worldmap_R0001_ShipM.pam`, `WorldMap_WoodenBoat_small.pam` | 10 |
| 4     | WagonForPerson  |                                                       | 0                  |
| 5     | OfferingCarrier | `WorldMap_Cartgold.pam` (the Velia and Heidel Tribute Wagons) | 2          |

## Field Names

The 2016 `gc::DelivererStaticStatus` holds `_characterKey`,
`_deliveryRoute`, `_loadAge`, `_fee`, `_waypointNameList` (20 strings),
`_waypointList` (resolved, not stored) and `_objectFile`; the file stores
the object file before the waypoint names. The `Carriage_Table` sheet of a
private server's `DataSheets.bexcel` on client 1784 has the columns
`CharacterKey`, `Loadage`, `Price`, `MoveSpeed`, `Way Index`,
`WaypointName0` to `WaypointName19`, `Waypoint0` to `Waypoint19`,
`ObjectName` and `ContentsGroupKey`, 23 rows. `MoveSpeed`, the waypoint
numbers and the contents groups have no field.

| Field                 | Column                      | Same value (client 1784) | Same value (client 3482) |
| --------------------- | --------------------------- | ------------------------ | ------------------------ |
| character_key         | `CharacterKey`              | 20 of 20                 | 21 of 21                 |
| delivery_route        | `Way Index`                 | 20 of 20                 | 21 of 21                 |
| load_age              | `Loadage`                   | 20 of 20                 | 21 of 21                 |
| fee                   | `Price`                     | 20 of 20                 | 21 of 21                 |
| object_file_index     | `ObjectName`                | 20 of 20                 | 21 of 21                 |
| waypoint_name_indexes | `WaypointName0` to `19`     | 20 of 20                 | 20 of 21                 |

The string columns compare the strings the indexes point at, the waypoint
names as one list. On client 3482 the Port Ratt Freight Ship (`729`) has
`LotWay_001` and `LotWay_118` where the sheet has `LotWay_0001` and
`LotWay_0153`. Client 3482 adds six carriers the sheet lacks (`730`, `731`,
`50987`, `59898`, `59902`, `62095`); the sheet's `714` and `9106` are not
in either file.

## Notes

- The waypoint names are named waypoints of the world map route graph; the
  wagons and ships move between them on the world map.

## Open Questions

### What the Byte After the Type Holds

`unknown_69` is `0` on every row of client 3482 and has no column or Lua
getter. `deliverer_type` and `unknown_69` may be one u16 field.
