# `mansionpartinfo.bss` Format

## Purpose

The part pictures of the manors whose parts can be changed in installation
mode: one fixed 12-byte row per manor part with the manor's ID, the part index
and the picture path as a string table index. Each picture is a blueprint of
the whole building, an overhead cutaway render with that part highlighted in
magenta. The rows name buildings, not characters, although the manor ID is the
building's key in `characterstatic.dbss`, where houses are records like NPCs.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Manor names, LOC type 6 keyed by `character_id`       |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset              | Type                  | Field        | Notes                                          |
| ------------------- | --------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]               | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                   | count        | Number of rows; 9 on client 3458               |
| `+0x08`             | Manor Part Row[count] | rows         | See Manor Part Row                             |
| `rows+0x00`         | String Table          | string_table | See String Table                               |
| `string_table+0x00` | u32                   | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                   | zero         | Always 0                                       |

Rows are sorted by `character_id`, then `part_index`.

### Manor Part Row (12 bytes)

| Offset  | Type | Field           | Notes                                                                 |
| ------- | ---- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_id    | The manor building's key in `characterstatic.dbss` (its house record) |
| `+0x02` | u8   | unknown_02      | Always `1`                                                            |
| `+0x03` | u8   | part_index      | Sub-mesh part of the manor, from 0                                    |
| `+0x04` | u32  | icon_ref        | String table index of the part icon, relative to `ui_texture/`        |
| `+0x08` | u32  | unknown_str_ref | String table index; always `1`, the empty string                      |

### String Table (variable: 4 bytes + strings)

10 strings on client 3458: the nine icon paths and, at index 1, an empty
string that every `unknown_str_ref` points at.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

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
