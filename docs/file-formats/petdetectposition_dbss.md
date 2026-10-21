# `petdetectposition.dbss` Format

## Purpose

The world positions behind the pet Location Find skill (`skill_type` `4`,
`ePetSkill_DetectPosition`, in [`petskill.dbss`](petskill_dbss.md)): each
row is a position key, a world position and a position type. In the client
files every position reads `0, 0, 0`: the position columns are server-only in
the source sheet. Companion
`petdetectpositionoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `petdetectposition.dbss`       | 64    | 4 Row        | 15        |
| 1      | 1485 and later | 3474    | `petdetectpositionoffset.dbss` | 44    | 4 Offset Row | 10        |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `petdetectposition.dbss`       | 64 B (100.0%) | 0 B (0.0%) |
| 1      | `petdetectpositionoffset.dbss` | 44 B (100.0%) | 0 B (0.0%) |

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

| File                           | Required | Role                                                      |
| ------------------------------ | -------- | --------------------------------------------------------- |
| `petdetectpositionoffset.dbss` | Optional | `pet_detect_position_key -> (offset, size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 4 x 15 = 64 bytes on client 3474.

### Row (15 bytes)

| Offset  | Type | Field                    | Notes                                                        |
| ------- | ---- | ------------------------ | ------------------------------------------------------------ |
| `+0x00` | u16  | pet_detect_position_key  | Row key; `1` to `4` (client 3474)                            |
| `+0x02` | f32  | pos_x                    | World X; `0` on every row, see Field Names                   |
| `+0x06` | f32  | pos_y                    | World Y (height); `0` on every row                           |
| `+0x0A` | f32  | pos_z                    | World Z; `0` on every row                                    |
| `+0x0E` | u8   | pet_detect_position_type | `gc::PetDetectPositionType`; `0` (`None`) on every row        |

The rows have no padding: the 2016 struct is 20 bytes in memory with 2
bytes of padding after the key and 3 after the type byte, and the file packs
its members back to back.

### `petdetectpositionoffset.dbss`

Bare offset table into `petdetectposition.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                      |
| ------- | ----------------- | ----- | ------------------------------------------ |
| `+0x00` | u32               | count | Equals the `petdetectposition.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                             |

### Offset Row (10 bytes)

| Offset  | Type | Field                   | Notes                                                       |
| ------- | ---- | ----------------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | pet_detect_position_key | Key of the row it points at                                 |
| `+0x02` | u32  | offset                  | Absolute byte offset of the row in `petdetectposition.dbss`, at its `pet_detect_position_key` |
| `+0x06` | u32  | size                    | The whole row: always `15`                                  |

Both files list the keys in descending order, 4, 3, 2, 1. The offset
points at the row's own key; the rows of
[`guildboss.dbss`](guildboss_dbss.md) and [`petexp.dbss`](petexp_dbss.md)
start with a key copy that their offsets skip.

## Pet Detect Position Type

`pet_detect_position_type` is the 2016 enum `gc::PetDetectPositionType`
(`unsigned char`):

| Value | Name                           |
| ----: | ------------------------------ |
| 0     | `ePetDetectPositionType_None`  |
| 1     | `ePetDetectPositionType_Count` |

`Count` is the enum's end marker, so `None` is the only real value.

## Field Names

The 2016 client's debug symbols hold `gc::PetDetectPositionStaticStatus`
(20 bytes), keyed by a `KeyType<unsigned short>`, with the members
`_petDetectPositionKey` (u16 at `+0x00`), `_petDetectPosition` (a
`pa::float3` of `x`, `y`, `z` at `+0x04`) and `_petDetectPositionType`
(`gc::PetDetectPositionType`, one byte at `+0x10`). Packed in that order they
are the 15-byte row, and the loader is
`GameCommonParameterLoaderFromExcel::LoadPetDetectPositionStaticInformation`.
The position fields use the `pos_x`, `pos_y`, `pos_z` names of
[`employeespawnposition.dbss`](employeespawnposition_dbss.md).

The `Pet_DetectPosition` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `No`, `PositionX`, `PositionY` and `PositionZ`
and the keys 1 to 4, the same 4 of 4 keys as the file on clients 1784 and
3474. Its developer workbook (`datasheet_petdatatable.xlsm`) marks the three
position columns `%`, server-only, which is why the client files write `0`
in them. The private server's own compiled `petdetectposition.dbss` is the
same 64 bytes as the client files. The client 1784 server dump reads the
sheet in `Load_Pet_DetectPosition` (VA `0x140870f20`): `No` with
`ReadCellInt` into a u16 at `+0x00`, `PositionX`, `PositionY` and
`PositionZ` with `ReadColumnFloat` at `+0x04`, `+0x08` and `+0x0C`, and a
byte at `+0x10` it sets to `0` and never fills from the sheet, the 2016
layout. The `Pet_DetectPosition` table of a private server on client 519 has
the same 4 keys with `0` in all three positions.

## Notes

- Clients 1485, 1784, 2107, 2519, 3002, 3251 and 3474 have the same 64-byte
  file and 44-byte offset file, byte for byte.
- The `#Name` note column of the client 1784 developer workbook labels the
  four rows: 1 해안절벽 은밀한 동굴 (coastal cliff hidden cave), 2 해안절벽
  동굴 입구 (coastal cliff cave entrance), 3 해안동굴 보스 소환 위치 (coastal
  cave boss summon position), 4 고대인의 석실 입구 (entrance to the
  ancient ones' stone chamber). A `#` column is not compiled into the file.
- The 2016 client has an AI proxy class `ge::AiPetDetectPositionProxy` with
  a `getPosition` method that returns a `pa::float3`. The AI target types of
  a private server on client 519 include `PetDetectPosition` (`4194304`,
  bit 22).
- Pet skill `5` is the only Location Find skill in `petskill.dbss` (client
  3474). Nothing in its row points at a `pet_detect_position_key`.
- No client Lua reads the table: of the 3,073 `.luac` files of client 3474,
  only `global_define_cpp_enum` holds the text `DetectPosition`, as the
  `PetSkillType` enum value.

## Open Questions

### Which Position a Pet Finds

The rows carry no region, quest or pet key, and the client files hold no
coordinates. Whether a Location Find pet reacts to every row near the
player, or the server picks rows some other way, cannot be read from the
client data.
