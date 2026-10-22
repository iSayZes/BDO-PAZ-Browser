# `edanacastleinfostaicstatusmanager.bss` Format

## Purpose

The world map marks of the Edania castles: one row per castle with the
texture of its territory mark, a world map position and the castle's node.
The rows follow the `__eEdaniaRegion` order (Aetherion to Voidekaia). No
client Lua calls read this file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3482    | `edanacastleinfostaicstatusmanager.bss` | 748   | 10 Row  | 16        |

| Layout | File                                    | Known          | Unknown    |
| ------ | --------------------------------------- | -------------- | ---------- |
| 1      | `edanacastleinfostaicstatusmanager.bss` | 748 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | No file  |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                      |
| --------------------- | -------- | ----------------------------------------- |
| `languagedata_en.loc` | Optional | Node names, LOC type 29                   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset      | Type               | Field        | Notes                                         |
| ----------- | ------------------ | ------------ | --------------------------------------------- |
| `+0x00`     | char[4]            | magic        | ASCII `PABR`                                  |
| `+0x04`     | Row[..table_start] | rows         | See Row; no row count                         |
| `rows+0x00` | String Table       | string_table | See String Table                              |
| `EOF-0x08`  | u32                | table_start  | Offset of the string table, where `rows` ends |
| `EOF-0x04`  | u32                | zero         | Always `0`                                    |

### Row (16 bytes)

| Offset  | Type | Field            | Notes                                                                                   |
| ------- | ---- | ---------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | mark_texture_ref | String-table index of the mark texture name; equals the row number on every client checked |
| `+0x04` | f32  | x                | World X of the mark                                                                     |
| `+0x08` | f32  | z                | World Z of the mark                                                                     |
| `+0x0C` | u32  | node_key         | The castle's node; `2002` Aetherion Castle to `2112` Event Horizon                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                      |
| ------- | ------------------ | ------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; one per row                                             |
| `+0x04` | pstr[string_count] | strings      | UTF-16 texture names, `territorymark_Jordine_large` to `territorymark_Hadum_large` |

## Castles

The rows on client 3482, with the node's LOC name. Each texture is a
`ui_texture/renewal/etc/wordmap/<name>.dds` file, named after the castle's
god; the same gods name the faction icons the client draws for each
`__eEdaniaRegion` value (`Combine_Etc_EdaniaIcon_Jordain_Normal` for
Aetherion, see [`edaniaregioninfo.bss`](edaniaregioninfo_bss.md#notes)).

| Row | `mark_texture`                   | `node_key` | Node                  |
| --- | -------------------------------- | ---------- | --------------------- |
| 0   | `territorymark_Jordine_large`    | `2002`     | Aetherion Castle      |
| 1   | `territorymark_Rusalka_large`    | `2006`     | Nymphamaré Castle     |
| 2   | `territorymark_Enslar_large`     | `2003`     | Orbita Castle         |
| 3   | `territorymark_Cartian_large`    | `2005`     | Tenebraum Castle      |
| 4   | `territorymark_Caphras_large`    | `2004`     | Zephyros Castle       |
| 5   | `territorymark_Agris_large`      | `2111`     | Aphrodon Temple       |
| 6   | `territorymark_Marctanan_large`  | `2109`     | Hermesia Inner Castle |
| 7   | `territorymark_Alien_large`      | `2108`     | Magaia Temple         |
| 8   | `territorymark_Aal_large`        | `2110`     | Aresion Temple        |
| 9   | `territorymark_Hadum_large`      | `2112`     | Event Horizon         |

## Field Names

Edania is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers this file, and no Lua call reads
it. The names come from the values:

- `mark_texture_ref` indexes the string table, which holds one texture
  name per row in row order. Each name is a world map territory mark
  (`territorymark_<god>_large.dds`, next to `territorymark_edania_large.dds`
  in `ui_texture/renewal/etc/wordmap/`). The official Throne of Edana
  page of the NA/EU game wiki (wikiNo 457) pairs each castle with the same
  god: "Aetherion Castle (Jordine)", "Nymphamaré Castle (Rusalka)" through
  "Zephyros Castle (Caphras)".
- `node_key` is a node key: each value has a LOC type 29 node name, the
  castle of the same row. The node order matches the `__eEdaniaRegion`
  order of [`edaniaregioninfo.bss`](edaniaregioninfo_bss.md#enum-values).
- `x` and `z` lie 3,700 to 20,400 units from the castle node's own world
  position on client 3482 (Aetherion: `559141, 573692` against the node's
  `566128, 570954`), so they read as world X and Z.

## Notes

- Clients 3002 and 3251 hold the first five rows (Aetherion to Zephyros),
  client 3474 all ten. The file is not in the archives of client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/edania_tables.py`: the node key and name, the mark
  texture and the position.
