# `employeeloyalismitem.dbss` Format

## Purpose

Items that restore a sailor's condition. The file names and the client code call sailors "employees" and their condition "loyalism" or "loyalty" (`충성도` in the sheet comments); the English client text says "Sailor Condition". Each row is one item, whether it restores condition points or cures a sick sailor, and how much it restores. The sailor management window at a Wharf Manager lists these items when you restore a sailor. Companion `employeeloyalismitemoffset.dbss` lists where every row sits.

On client 3474 the file has 4 rows: Chowder (`+100` condition), Raisin Bread (`+1`), Elixir of Regeneration and Tears of the Star (cure a sick sailor, condition to 100%).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `employeeloyalismitem.dbss`       | 40    | 4 Row        | 9         |
| 1      | 1485 and later | 3474    | `employeeloyalismitemoffset.dbss` | 52    | 4 Offset Row | 12        |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `employeeloyalismitem.dbss`       | 40 B (100.0%) | 0 B (0.0%) |
| 1      | `employeeloyalismitemoffset.dbss` | 52 B (100.0%) | 0 B (0.0%) |

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

| File                              | Required | Role                                           |
| --------------------------------- | -------- | ---------------------------------------------- |
| `employeeloyalismitemoffset.dbss` | Required | `item_id -> (offset, size)` of every row       |
| `languagedata_en.loc`             | Optional | Item names (LOC type 0, `str_id1` = `item_id`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                 |
| ------- | ---------- | ----- | --------------------- |
| `+0x00` | u32        | count | Number of rows        |
| `+0x04` | Row[count] | rows  | See Row               |

The rows fill the file exactly: 4 + 4 x 9 = 40 bytes on client 3474.

### Row (9 bytes)

| Offset  | Type | Field          | Notes                                                                        |
| ------- | ---- | -------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u8   | loyalism_type  | `0` restores condition points, `1` cures a sick sailor; see Loyalism Type    |
| `+0x01` | u32  | item_id        | The item used; row key                                                       |
| `+0x05` | u32  | recovery_value | Type `0`: condition points. Type `1`: rate on the 1,000,000 = 100% scale     |

### `employeeloyalismitemoffset.dbss`

Bare offset table into `employeeloyalismitem.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                             |
| ------- | ----------------- | ----- | ------------------------------------------------- |
| `+0x00` | u32               | count | Number of offset rows; equals the main file count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                    |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                      |
| ------- | ---- | ----------- | -------------------------------------------------------------------------- |
| `+0x00` | u32  | item_id     | Key of the row it points at                                                |
| `+0x04` | u32  | data_offset | Absolute byte offset in `employeeloyalismitem.dbss` of the row's first byte (`loyalism_type`) |
| `+0x08` | u32  | data_size   | Always 9                                                                   |

The offset points at `loyalism_type`, so the key the row repeats sits at `data_offset + 1`. The parser reads the main file through these rows and checks that every row holds the key of the offset row that points at it.

## Loyalism Type

`loyalism_type` is the client's `__eEmployeeLoyalismType`. The client Lua names its two members, and the developer comment on the sheet's `Type` column (see Field Names) gives the numbers: `0 : 일반 회복` ("normal recovery") and `1 : 탈주한 선원 회복` ("recovery of a deserted sailor").

| Value | Lua name                                | Effect                                                               |
| ----- | --------------------------------------- | -------------------------------------------------------------------- |
| 0     | `__eEmployeeLoyalismType_Loyalty`       | Adds `recovery_value` condition points                               |
| 1     | `__eEmployeeLoyalismType_resurrection`  | Cures a sick sailor and sets condition to `recovery_value` (a rate)  |

In `panel_window_sailormanager_all_1.luac` the Restore button of a sailor in the `__eEmployeeState_Escape` state opens the item list with `__eEmployeeLoyalismType_resurrection`, every other sailor with `__eEmployeeLoyalismType_Loyalty`. `panel_window_sailormanager_all_2.luac` shows the `+N` value (`ToClient_getRecoveryValue(type, itemKey)`) on the item slot only for `Loyalty`, and the bulk restore in `panel_window_sailormanager_all_4.luac` uses `Loyalty` and skips sailors in the escape state. The English client calls the escape state sick: "Sick sailors cannot recover their health."

## Field Names

The names follow the `Employee_Loyalism` sheet of a private server's `DataSheets.bexcel` on client 1784 (`Type`, `RecoveryItemKey`, `RecoveryCount`, in this order). Its 4 rows equal the 4 rows of the live file value by value (client 3474), and the client 1784 file is byte for byte the same as the client 3474 file.

| Column            | Field            | Developer comment (sheet in the private server's `DataSheet_EmployeeDataTable.xlsx`) |
| ----------------- | ---------------- | ------------------------------------------------------------------------------------- |
| `Type`            | `loyalism_type`  | `선원의 충성도 회복 타입` ("sailor condition recovery type"), see Loyalism Type        |
| `RecoveryItemKey` | `item_id`        | `선원 충성도 회복 아이템키 설정` ("sailor condition recovery item key")                |
| `RecoveryCount`   | `recovery_value` | `타입 0 : 절대값` ("type 0: absolute value"), `타입 1 : 10000 ~ 1000000입력하며, 1 (%)` ("type 1: enter 10000 to 1000000, 1%" per 10000) |

`recovery_value` keeps the meaning, not the sheet's word "count": the Lua reads it through `ToClient_getRecoveryValue`.

## Notes

- The item texts agree with the values (LOC type 0, `str_id4` 1, client 3474): Chowder (6394, `100`) "Recover 100 Sailor Condition", Raisin Bread (6398, `1`) "Recover 1 Sailor Condition", Elixir of Regeneration (6395, `1000000`) "Cures one sailor, Recovers condition to 100%", Tears of the Star (320083, `1000000`) "Recover 1 Sick Sailor, Recover Sailor Condition to 100%".
- The 2016 PDB has no `Loyalism` names; sailors came to the game later.
- `employeeloyalismitemetc.bss` (32 bytes, PABR) shares the stem but has its own layout, see [employeeloyalismitemetc](employeeloyalismitemetc_bss.md).
