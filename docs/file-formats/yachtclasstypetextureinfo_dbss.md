# `yachtclasstypetextureinfo.dbss` Format

## Purpose

The Yar! player portraits: each row maps a class type to the texture ID of
the profile icon the match window shows for a player of that class.
`yachtclasstypetextureinfooffset.dbss` is the index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                   | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | -------------------------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `yachtclasstypetextureinfo.dbss`       | 1,876 | 36 Row        | 52        |
| 1      | 1784 and later | 3474    | `yachtclasstypetextureinfooffset.dbss` | 436   | 36 Offset Row | 12        |

| Layout | File                                   | Known            | Unknown    |
| ------ | -------------------------------------- | ---------------- | ---------- |
| 1      | `yachtclasstypetextureinfo.dbss`       | 1,876 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtclasstypetextureinfooffset.dbss` | 436 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                                   | Required | Role                                                                     |
| -------------------------------------- | -------- | ------------------------------------------------------------------------ |
| `yachtclasstypetextureinfooffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows can be walked without it |
| `languagedata_en.loc`                  | Optional | Class names (LOC type 21, `str_id1=class_type`)                          |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `36` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 16 bytes + texture ID)

| Offset  | Type | Field          | Notes                                                           |
| ------- | ---- | -------------- | --------------------------------------------------------------- |
| `+0x00` | u32  | class_type     | Class type (`0` Warrior, `4` Ranger); unique per row            |
| `+0x04` | u32  | class_type_dup | Equal to `class_type` in every row; the offset file points here |
| `+0x08` | str8 | texture_id     | Texture ID of the profile icon (`Combine_Etc_Minigame_Icon_Profile_03`) |

The rows run from class type 35 down to 32, then from 15 down to 0, then
from 31 down to 16 (client 3474).

### `yachtclasstypetextureinfooffset.dbss`

| Offset  | Type              | Field | Notes                                             |
| ------- | ----------------- | ----- | ------------------------------------------------- |
| `+0x00` | u32               | count | Equals the `yachtclasstypetextureinfo.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | key         | Class type of the row it points at                       |
| `+0x04` | u32  | data_offset | Row start + 4, at `class_type_dup`                       |
| `+0x08` | u32  | data_size   | The row without its leading key: `48` on client 3474     |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order, and every index row points at the row with
its key (clients 1784 and 3474).

## Class Types

On client 3474 the file holds class types 0 to 35, each once, client 1784
0 to 31. Class types without a playable class (13, 14, 18, 22) have a row
too. On client 3474 class types 12 to 14 share `Profile_06`, 17 and 18
`Profile_17`, 20 and 22 `Profile_08`; every other class type has its own
icon.

## Field Names

The `ClassTypeTextureInfo` sheet of a private server's
`datasheet_minigame.xlsm` on client 1784 has the columns `ClassType`
(`class_type`) and `TextureId` (`texture_id`), and a note column `#설명`
with the Korean class name. Its 32 rows match the 32 rows of client 1784
in both columns. On client 3474, 27 of the 32 sheet rows keep the sheet's
texture: class types 3, 6, 7, 15 and 30 (Wukong, Scholar, Drakania, Maegu,
Woosa), which the sheet gives the Warrior, Ranger, Berserker or Kunoichi
icon, have their own (`Profile_31`, `28`, `25`, `27`, `26`), and class
types 32 to 35 are new rows. The file writes the class type twice: once as
the index key, once inside the row.

## Notes

- The match window reads a player's icon through `getIconPath()` on
  `ToClient_getMyYachtUserDataWrapper()` and
  `ToClient_getEnemyYachtUserDataWrapper()`
  (`panel_window_minigame_yachtdice_1.luac`); no Lua call names this table.
