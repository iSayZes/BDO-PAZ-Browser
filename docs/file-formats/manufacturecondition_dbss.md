# `manufacturecondition.dbss` Format

## Purpose

Processing actions: each record names one tab of the processing window
(`MANUFACTURE_HEAT`, `REPAIR_ITEM` and the rest) and holds two condition
scripts, one that decides whether the tab shows and one that decides whether
it can be used. The record key is the hash of the action name, the same
`action_hash` that [`manufacture.bss`](manufacture_bss.md) stores on each
recipe row.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records      | Row bytes                |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------ | ------------------------ |
| 1      | 1485 and later | 3474    | `manufacturecondition.dbss`       | 1,183 | 14 Record    | 72 to 123, 84 on average |
| 1      | 1485 and later | 3474    | `manufactureconditionoffset.dbss` | 172   | 14 Index Row | 12                       |

| Layout | File                              | Known            | Unknown    |
| ------ | --------------------------------- | ---------------- | ---------- |
| 1      | `manufacturecondition.dbss`       | 1,183 B (100.0%) | 0 B (0.0%) |
| 1      | `manufactureconditionoffset.dbss` | 172 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                                              |
| --------------------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `manufactureconditionoffset.dbss` | Optional | `action_hash -> (data_offset, data_size)` index, see below; the records can be walked without it   |
| `languagedata_en.loc`             | Optional | The window's name of each action (LOC type 37), as in [`manufacture.bss` Actions](manufacture_bss.md#actions) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                           |
| ------- | ------------- | ------- | ----------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `14` on client 3474          |
| `+0x04` | Record[count] | records | Back to back to the end of the file; see Record |

### Record (variable: 32 bytes + name and condition text)

| Offset                          | Type  | Field                   | Notes                                                                                   |
| ------------------------------- | ----- | ----------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`                         | u32   | action_hash             | lookup3 `hashlittle` of the `action_name` bytes with seed `0xC5EDE`; the index key      |
| `+0x04`                         | str8  | action_name             | The processing window's `actionName`; the index's `data_offset` points here             |
| `action_name+0x00`              | u32   | action_hash_dup         | Equal to `action_hash` in every record                                                  |
| `action_name+0x04`              | str16 | check_visible_condition | Script that decides whether the action's tab shows; empty on 2 records (client 3474)    |
| `check_visible_condition+0x00`  | str16 | check_enable_condition  | Script that decides whether the tab can be used; empty on 11 records (client 3474)      |

`action_hash` is the hash `manufacture.bss` documents under
[`action_hash`](manufacture_bss.md#action_hash): `_common/string_hash.py`'s
`hashlittle` over the ASCII name, so `MANUFACTURE_HEAT` hashes to
`0x1B6F02F1`. It matches all 14 records on clients 3474 and 1784.

### `manufactureconditionoffset.dbss`

| Offset  | Type             | Field | Notes                                         |
| ------- | ---------------- | ----- | --------------------------------------------- |
| `+0x00` | u32              | count | Equals the `manufacturecondition.dbss` count  |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row           |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | action_hash | Record key                              |
| `+0x04` | u32  | data_offset | Record start + 4, at `action_name`      |
| `+0x08` | u32  | data_size   | Record size - 4                         |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The rows
are not in file order; on client 3474 every row matches the record walked
from the start of the file.

## Field Names

The record is the `ManufactureCondition_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, with the columns `ActionName`,
`CheckVisibleCondition` and `CheckEnableCondition`. A `<null>` cell is
stored as an empty string (count `0`). The sheet's second column,
`가공 액션 명` (the action's Korean name), is not in the file.

| Field                   | Column                  | Shared names, same value                      |
| ----------------------- | ----------------------- | --------------------------------------------- |
| action_name             | `ActionName`            | 14 of 14 (client 1784), 14 of 14 (client 3474) |
| check_visible_condition | `CheckVisibleCondition` | 14 of 14 (client 1784), 14 of 14 (client 3474) |
| check_enable_condition  | `CheckEnableCondition`  | 14 of 14 (client 1784), 14 of 14 (client 3474) |

The client Lua uses the same split. `PaGlobal_Manufacture_All_UpdateVisibleRadioButton`
in `panel_window_manufacture_all_3.luac` shows each action tab by
`isVisibleManufactureAction(actionName)`, then sets each shown tab active or
grayed out (`SetMonoTone`) by `isEnableManufactureAction(actionName)`.

## Conditions

All five scripts in the file (client 3474):

| Script                                   | Field                   | Actions                                                       |
| ---------------------------------------- | ----------------------- | ------------------------------------------------------------- |
| `getlevel()>0`                           | check_visible_condition | 11: every action except Filtering, Drying and Collect rainwater |
| `getlevel()>99`                          | check_visible_condition | Collect rainwater (`MANUFACTURE_RAINWATER`)                   |
| `getKnowledge(6558)`                     | check_enable_condition  | Repair (`REPAIR_ITEM`); knowledge 6558 is Repair (LOC type 34) |
| `getWeatherFactor(WindForce,0)>300;`     | check_enable_condition  | Filtering (`MANUFACTURE_THINNING`)                            |
| `getWeatherFactor(RainAmount,0)<100000;` | check_enable_condition  | Drying (`MANUFACTURE_DRY`)                                    |

Filtering and Drying have an empty `check_visible_condition`; every other
action has an empty `check_enable_condition` except Repair. `getlevel()>99`
reads as a lock on the Collect rainwater tab, which the window still lists
in `MANUFACTURE_INFO` (`panel_window_manufacture_all.luac`).

The window adds checks of its own on top of the file: Repair also needs an
anvil nearby (`isNearInstallation(eType_Anvil)`), and contents groups `22`
and `285` hide the Imperial Cuisine, Imperial Alchemy and Manufacture tabs
when closed.

## Notes

- The 14 action names are the 12 of the `manufacture.bss` string table plus
  `REPAIR_ITEM` and `MANUFACTURE_RAINWATER`, which have no recipe rows. Every
  action a `manufacture.bss` row uses has a record here.
- The records are sorted by neither hash nor name, and not in the sheet's
  row order.
- Both files are byte for byte the same on clients 1784 and 3474.

## Open Questions

### Weather Factor Scale

Drying needs `getWeatherFactor(RainAmount,0)<100000` and Filtering needs
`getWeatherFactor(WindForce,0)>300`. The world map node window
(`panel_worldmap_nodeinfo_renew.luac`) reads rain through
`getWeatherInfoByWaypoint(eWSFT_RAIN_AMOUNT, ...)` as a fraction, with `0.3`
and `0.6` as its medium and heavy thresholds, so `100000` is on another
scale. No client Lua or data file shows the scale `getWeatherFactor` returns
or what its second argument `0` selects.
