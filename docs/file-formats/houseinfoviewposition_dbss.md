# `houseinfoviewposition.dbss` Format

## Purpose

A world position and a facing per house and house use type: one 32-byte
row for each pair of a house character and an `eHouseUseType` value (`3`
Ranch, `12` CannonWorkshop, `13` Shipyard, `14` CarriageWorkshop). The rows
cover node houses of [`houseinfo.bss`](houseinfo_bss.md) and guild houses of
[`guildhouseinfo.dbss`](guildhouseinfo_dbss.md); a guild house holds up to
two rows, one per use type. Companion `houseinfoviewpositionoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ----- | ------------- | --------- |
| 1      | 1348 and later | 3482    | `houseinfoviewposition.dbss`       | 2,708 | 84 Row        | 32        |
| 1      | 1348 and later | 3482    | `houseinfoviewpositionoffset.dbss` | 1,348 | 84 Offset Row | 16        |

| Layout | File                               | Known            | Unknown    |
| ------ | ---------------------------------- | ---------------- | ---------- |
| 1      | `houseinfoviewposition.dbss`       | 2,708 B (100.0%) | 0 B (0.0%) |
| 1      | `houseinfoviewpositionoffset.dbss` | 1,348 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
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

| File                               | Required | Role                                                                                 |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------------ |
| `houseinfoviewpositionoffset.dbss` | Optional | `(character_key, house_group_type) -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `houseinfo.bss`                    | Optional | The node house rows, for the House link and the Town column                          |
| `guildhouseinfo.dbss`              | Optional | The guild house rows, for the House link and the Town column                         |
| `languagedata_en.loc`              | Optional | House names (type 6) and town names (type 17)                                        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of fixed rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset      | Type       | Field        | Notes                                    |
| ----------- | ---------- | ------------ | ---------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                   |
| `+0x04`     | u32        | count        | Number of rows; 84 on client 3482        |
| `+0x08`     | Row[count] | rows         | See Row                                  |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table         |
| `rows+0x04` | u32        | table_start  | End of the rows (`8 + 32 * count`)       |
| `rows+0x08` | u32        | zero         | Always `0`                               |

### Row (32 bytes)

| Offset  | Type   | Field            | Notes                                                                       |
| ------- | ------ | ---------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16    | character_key    | The house, a `characterstatic.dbss` key; with `house_group_type` the row key |
| `+0x02` | i16    | padding_02       | The 2016 PDB key member `_reserve`; `0` on every row (clients 1784 and 3482) |
| `+0x04` | u32    | house_group_type | A `CppEnums.eHouseUseType` value; see House Use Types                       |
| `+0x08` | f32[3] | position         | World position x, y, z; `0, 0, 0` on the 19 Ranch rows (client 3482)       |
| `+0x14` | f32[3] | direction        | Facing as a unit vector `(-sin yaw, 0, -cos yaw)`, yaw in degrees           |

Every (`character_key`, `house_group_type`) pair is unique. The rows are
in no key order.

### `houseinfoviewpositionoffset.dbss`

Bare offset table into `houseinfoviewposition.dbss` (no PABR magic, no
trailer), keyed by the same 8 bytes the row starts with.

| Offset  | Type              | Field | Notes                                         |
| ------- | ----------------- | ----- | --------------------------------------------- |
| `+0x00` | u32               | count | Equals the `houseinfoviewposition.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                |

### Offset Row (16 bytes)

| Offset  | Type | Field            | Notes                                                       |
| ------- | ---- | ---------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key    | Key of the row it points at                                 |
| `+0x02` | i16  | padding_02       | The 2016 PDB key member `_reserve`; `0` on every row        |
| `+0x04` | u32  | house_group_type | Key of the row it points at                                 |
| `+0x08` | u32  | data_offset      | Absolute offset of the row in `houseinfoviewposition.dbss`, at `character_key` |
| `+0x0C` | u32  | data_size        | `32` on every row: the whole row                            |

The index rows are in another order than the file; on clients 1784 and 3482 every index row
points at the row with its key.

## House Use Types

`house_group_type` takes values of `CppEnums.eHouseUseType`
(`global_define_cpp_enum.luac`), the enum of the `house_use_type` field of
[`houseinforeceipe.dbss`](houseinforeceipe_dbss.md).

| Value | `eHouseUseType`    | Rows (client 3482) |
| ----- | ------------------ | ------------------ |
| `3`   | `Ranch`            | 19                 |
| `12`  | `CannonWorkshop`   | 11                 |
| `13`  | `Shipyard`         | 34                 |
| `14`  | `CarriageWorkshop` | 20                 |

On client 3482, 68 of the 84 rows belong to a house with a use of that
`house_use_type`: a Shipyard row (`13`) sits on a house with a Shipyard or
Guild Shipyard use, a CarriageWorkshop row (`14`) on a house with a Wagon
Workshop use. The other 16 are the 11 CannonWorkshop rows, the Ranch row of
house `2246` and the CarriageWorkshop rows of the four guild houses `2110`,
`2140`, `2880` and `2905`; none of those houses has a use of that type.

## Field Names

The `HouseViewPostion` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `TerritoryKey`, `HouseKey`, `HouseGroupType`,
`position` and `rotationYaw`. The 2016 `gc::HouseInfoViewPositionStaticStatus`
holds `_position`, `_direction` and the 8-byte key
`gc::HouseInfoViewPositionKey` (`_characterKey`, `_reserve`,
`_housegrouptype`); the client stores the key first.

| Field            | Column / member                          | Same value (client 1784) |
| ---------------- | ---------------------------------------- | ------------------------ |
| character_key    | `HouseKey`                               | 76 of 76                 |
| house_group_type | `HouseGroupType`                         | 76 of 76                 |
| position         | `position`                               | 76 of 76                 |
| direction        | `rotationYaw`, as `(-sin, 0, -cos)`      | 76 of 76                 |

`padding_02` is the 2016 key's `_reserve` member, `0` on every row.
`TerritoryKey` (`0` to `8`) has no field: the client file leaves it out.

## Notes

- The direction is the sheet's `rotationYaw` in degrees turned into a
  vector: yaw `84` gives `(-0.9945, 0, -0.1045)`, yaw `0` gives `(0, 0, -1)`.
  The view shows the yaw back in degrees.
- The four rows of each Valencia guild house group (`3355` to `3358`, and
  `3351` to `3354`) share one position and direction per use type.
- No Lua file of client 3482 calls a getter for this table.
