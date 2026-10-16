# `mansionpartinfo.bss` Format

## Purpose

The part pictures of the manors whose parts can be changed in installation
mode: one fixed 12-byte row per manor part with the manor's ID, the part index
and the picture path as a string table index. Each picture is a blueprint of
the whole building, an overhead cutaway render with that part highlighted in
magenta. The rows name buildings, not characters, although the manor ID is the
building's key in `characterstatic.dbss`, where houses are records like NPCs.

Example:

```text
manor 3842 (Shimhyangje), part 0
  icon_ref -> Icon/New_Icon/03_ETC/06_Housing/Mantion_Morning1_Wall.dds
              (the building with its walls highlighted)
```

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Manor names, LOC type 6 keyed by `character_id`       |

All multi-byte values are little-endian.

## File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset           | Type    | Field        | Notes                                                            |
| ---------------- | ------- | ------------ | ---------------------------------------------------------------- |
| `+0x00`          | char[4] | magic        | ASCII `PABR`                                                     |
| `+0x04`          | u32     | count        | Number of rows; 9 on client 3458                                 |
| `+0x08`          | row[]   | rows         | 12-byte rows repeated `count` times                              |
| `8 + count * 12` | table   | string_table | u32 count, then `count` x (u8 is_wide, u32 byte length, payload) |
| EOF - 8          | u32     | table_start  | Offset of the string table, where the rows end                   |
| EOF - 4          | u32     | zero         | Always 0                                                         |

Rows are sorted by `character_id`, then `part_index`.

## Record Structure

### Manor Part Row (12 bytes, repeated `count` times)

| Offset  | Type | Field           | Notes                                                                 |
| ------- | ---- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_id    | The manor building's key in `characterstatic.dbss` (its house record) |
| `+0x02` | u8   | unknown_02      | Always `1`                                                            |
| `+0x03` | u8   | part_index      | Sub-mesh part of the manor, from 0                                    |
| `+0x04` | u32  | icon_ref        | String table index of the part icon, relative to `ui_texture/`        |
| `+0x08` | u32  | unknown_str_ref | String table index; always `1`, the empty string                      |

### String Table

10 strings on client 3458: the nine icon paths and, at index 1, an empty
string that every `unknown_str_ref` points at.

## Notes

- The installation mode list (`window/housing/panel_house_installationmode_list_all_1`)
  shows these icons on its "BaseMaterial" tab when the visited house is a
  manor: it reads the manor from `ToClient_VisitHouseHoldCharacterKey`, the
  number of parts from `ToClient_GetSubMeshCount`, and each part slot's icon
  from `ToClient_getPartIconPath(characterKey, partIndex)`.
- Client 3458 lists four manors: Blue Maned Lion's Manor (3815, parts 0 to 2,
  `Mantion_In1` to `Mantion_In3`) and the three Land of the Morning Light
  houses Shimhyangje (3842), Solbaram Neowa House (3844) and Hyeollokdang
  (3848), each with a wall and a floor picture. The part order is not fixed
  by kind: Shimhyangje's part 0 is its wall, the other two start with the
  floor. Blue Maned Lion's Manor highlights one wing per picture instead.
- All nine icons exist once resolved under `ui_texture/` and lowercased.
- The app indexes the part icons (`IndexKind.MANOR_PART_ICON`, read through
  `IconKind.MANOR_PART`) by `manor_part_key()`, `part_index << 16 |
  character_id`. They are blueprints of a part, so they never replace the
  manor's own `characterstatic.dbss` icon.

## Open Questions

### What do `unknown_02` and `unknown_str_ref` hold?

`unknown_02` is `1` and `unknown_str_ref` points at the empty string in all
nine rows. The string may be a part name the client never fills; with one
value each on the current client nothing tells their meaning apart.
