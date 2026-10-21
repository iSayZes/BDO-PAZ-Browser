# `instancefieldcommonlimitentertime.bss` Format

## Purpose

Per game service type (`CppEnums.GameServiceType`: `KOR_REAL`, `NA_REAL`,
`CS_REAL`, ...) a set of entries, each with seven pairs of hour values
(`0` to `23`). The file name and the server class that loads it on client
1784, `InstanceFieldCommonLimitEnterTimeManager`, point at the times an
instance field can be entered; two entries carry the instance field keys
of `Yonggung` (`27`) and `PAPUCRIO_ARENA` (`30`). On client 3474 the file
has 26 rows and 232 entries. The file is a u32 count and variable rows,
with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ---------------------------- | --------- |
| 1      | 2107 and later | 3474    | `instancefieldcommonlimitentertime.bss` | 5,750 | 232 Entry, 122 Group, 26 Row | 20        |

| Layout | File                                    | Known         | Unknown         |
| ------ | --------------------------------------- | ------------- | --------------- |
| 1      | `instancefieldcommonlimitentertime.bss` | 622 B (10.8%) | 5,128 B (89.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The service names come from `CppEnums.GameServiceType` in
`global_define_cpp_enum.luac`.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 5 bytes + groups)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u8                 | service_type | `CppEnums.GameServiceType`; one row per value             |
| `+0x01` | u32                | group_count  | Number of groups: `5`, or `1` on `CS_ALPHA` and `CS_REAL` (client 3474) |
| `+0x05` | Group[group_count] | groups       | See Group                                                |

### Group (variable: 8 bytes + entries)

| Offset  | Type               | Field             | Notes                                            |
| ------- | ------------------ | ----------------- | ------------------------------------------------ |
| `+0x00` | u32                | unknown_group_key | `11`, `16`, `0`, `8` or `22`, in this order        |
| `+0x04` | u32                | entry_count       | Number of entries                                |
| `+0x08` | Entry[entry_count] | entries           | See Entry                                        |

### Entry (20 bytes)

| Offset  | Type      | Field      | Notes                                                              |
| ------- | --------- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u16       | unknown_00 | Equal to the group's `unknown_group_key`                            |
| `+0x02` | u16       | unknown_02 | `27` in group `16`, `30` in group `0`, else `65535`                  |
| `+0x04` | u8        | unknown_04 | Equal to the row's `service_type`                                   |
| `+0x05` | u8        | unknown_05 | `3`, or `0` to `2` on the rows with more entries; see Rows         |
| `+0x06` | u8[7][2]  | unknown_06 | Seven pairs of values `0` to `23`; see Hour Pairs                   |

## Rows

On client 3474 the 26 rows are the `ALPHA` and `REAL` values of 13
services; `0`, `1`, `4` and `23` to `26`, `29` to `32` have no row.

| Service types                       | Groups                    | Entries per group      | `unknown_05` | Row bytes |
| ----------------------------------- | ------------------------- | ---------------------- | ------------ | --------- |
| 22 rows (`KOR`, `JPN`, `RUS`, `KR2`, `TW`, `SA`, `TH`, `ID`, `TR`, `GT`, `ASIA`) | `11`, `16`, `0`, `8`, `22` | 1, 1, 1, 4, 1 | `3`          | 205       |
| `11` `NA_ALPHA`, `12` `NA_REAL`     | `11`, `16`, `0`, `8`, `22` | 2, 2, 2, 8, 2          | `0`, `1`     | 365       |
| `33` `CS_ALPHA`, `34` `CS_REAL`     | `8`                       | 12                     | `0`, `1`, `2` | 253       |

On the `NA` and `CS` rows the entries of a group cycle through the
`unknown_05` values (`0`, `1`, `0`, `1`, ... or `0`, `1`, `2`, ...).

## Hour Pairs

`unknown_06` holds seven pairs per entry. On client 3474 every value is
`0` to `23`. Where the pairs of an entry differ, the first and the
seventh pair differ from the five between them (`13, 1` on the first and
seventh, `17, 1` on the others), the shape of a week with Sunday first and
Saturday last. Examples on the `KOR_REAL` row:

| Group | Pairs (first to seventh)                                  |
| ----- | --------------------------------------------------------- |
| `11`  | `10, 1` on all seven                                      |
| `16`  | `14, 2`, the fifth `10, 2` (also on `KOR_ALPHA` and `KR2`) |
| `0`   | `14, 2` on all seven                                      |
| `8`   | `13, 1` / `17, 1` (weekend / weekdays) and `10, 1`, twice  |
| `22`  | `13, 1` / `17, 1`                                         |

On `NA_REAL` the `unknown_05` `0` and `1` entries of a group lie 7 to 9
apart: group `11` is `17, 8` and `10, 1`, group `16` `21, 9` and `12, 0`.
The `CS_REAL` entries of group `8` run `23, 5`, `16, 22` and `10, 16` for
`unknown_05` `0` to `2`.

## Field Names

`service_type` takes its name from the value set: the 26 keys are exactly
the `ALPHA` / `REAL` pairs of `CppEnums.GameServiceType` (`2` / `3`
`KOR`, `11` / `12` `NA`, `33` / `34` `CS`, `35` / `36` `ASIA`), and every
entry repeats its row's key. The file is not in client 1784. The client
1784 server dump (`Instance_dumpFull.exe`) names the loader
`loadInstanceFieldLimitEnterTime` and the manager
`InstanceFieldCommonLimitEnterTimeManager`, but no sheet of a private
server's `DataSheets.bexcel` on client 1784 holds the table, so no column
names are known.

## Notes

- `unknown_02` values `27` and `30` are the `instancefield.dbss` keys of
  `Yonggung` and `PAPUCRIO_ARENA`. The Lua knows instance contents types
  such as `__eInstanceContentsType_RedBattleField` (with
  `__eInstanceRedBattleField_PapuCrio`) and `_DragonDungeon`, but the
  client sets their values, so the group keys cannot be matched to them
  from the Lua.

## Open Questions

### What the Groups and Hour Pairs Are

The group keys (`0`, `8`, `11`, `16`, `22`) look like instance contents
types and the pairs like an open and a close hour per weekday, Sunday
first, with `unknown_05` a service region in another time zone (`NA`
with two, `CS` with three). None of the three is confirmed: no sheet or Lua names the
fields, and the pairs could also be a start hour and a duration.

### unknown_02

`27` and `30` match instance field keys, but only two values occur, each in
one group. Whether the field is an instance field key or another key with
these values is open.
