# `itemeffectchange.dbss` Format

## Purpose

The model an equipment mesh switches to at each enhancement level. A group
holds one item mesh key and one entry per level from `0` up, and each entry
names the `.pac` model the mesh uses at that level. Most groups keep the base
model for the low levels and switch to a `_01`/`_02` or `_ef1`/`_ef2` model at
the top levels.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes   | Records                          | Row bytes               |
| ------ | -------------- | ------- | ----------------------------- | ------- | -------------------------------- | ----------------------- |
| 2      | 3474 and later | 3482    | `itemeffectchange.dbss`       | 385,623 | 6,141 Entry, 596 Group           | 57 to 78, 62 on average |
| 2      | 3474 and later | 3482    | `itemeffectchangeoffset.dbss` | 78,464  | 6,141 Index Row, 596 Index Group | 12                      |
| 1      | 1348 to 3251   | 3251    | `itemeffectchange.dbss`       | 365,245 | 6,009 Entry, 584 Group           | 55 to 76, 60 on average |
| 1      | 1348 to 3251   | 3251    | `itemeffectchangeoffset.dbss` | 75,616  | 6,009 Index Row, 584 Index Group | 12                      |

| Layout | File                          | Known              | Unknown    |
| ------ | ----------------------------- | ------------------ | ---------- |
| 2      | `itemeffectchange.dbss`       | 385,623 B (100.0%) | 0 B (0.0%) |
| 2      | `itemeffectchangeoffset.dbss` | 78,464 B (100.0%)  | 0 B (0.0%) |
| 1      | `itemeffectchange.dbss`       | 365,245 B (100.0%) | 0 B (0.0%) |
| 1      | `itemeffectchangeoffset.dbss` | 75,616 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                   |
| ----------------------------- | -------- | ------------------------------------------------------ |
| `itemeffectchangeoffset.dbss` | No       | Index of every entry by mesh key and level; the handler reads the groups in file order and does not need it |
| `itemenchant.dbss`            | No       | The items that wear each mesh, for the Items column; the handler reads them from the `MESH_KEY_ITEMS` lookup index, not as a companion |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A group count, then the groups back to
back; the file ends after the last group.

| Offset  | Type               | Field       | Notes                                   |
| ------- | ------------------ | ----------- | --------------------------------------- |
| `+0x00` | u32                | group_count | One group per mesh key                  |
| `+0x04` | Group[group_count] | groups      | See Group                               |

### Group (variable: 4 bytes + entries)

| Offset  | Type                 | Field       | Notes                                              |
| ------- | -------------------- | ----------- | -------------------------------------------------- |
| `+0x00` | u32                  | entry_count | `6`, `11` or `21` on client 3482; never `0`        |
| `+0x04` | Entry[entry_count]   | entries     | Levels `0` to `entry_count - 1` in order; see Entry |

### Entry (variable: 13 bytes + mesh file)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | mesh_key      | Item mesh key; the same in every entry of a group, unique per group    |
| `+0x04` | u8   | enchant_level | Enhancement level, equal to the entry's index in its group            |
| `+0x05` | str8 | mesh_file     | Lowercase `.pac` path under `character/model/`, e.g. `1_pc/1_phm/weapon/1_onehandsword/phm_01_ohs_0017_r.pac` |

### `itemeffectchangeoffset.dbss`

The same grouped walk with the mesh key moved into the group head. The groups
are in another order than in the main file, so a reader matches them by
`offset`, not by position.

| Offset  | Type                     | Field       | Notes                                |
| ------- | ------------------------ | ----------- | ------------------------------------ |
| `+0x00` | u32                      | group_count | Equals the main file's `group_count` |
| `+0x04` | Index Group[group_count] | groups      | See Index Group                      |

### Index Group (variable: 8 bytes + rows)

| Offset  | Type                 | Field     | Notes                                          |
| ------- | -------------------- | --------- | ---------------------------------------------- |
| `+0x00` | u32                  | row_count | Equals the `entry_count` of the main group with this mesh key |
| `+0x04` | u32                  | mesh_key  | The mesh key of every entry the rows point at  |
| `+0x08` | Index Row[row_count] | rows      | See Index Row                                  |

### Index Row (12 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | enchant_level | The entry's `enchant_level`                                  |
| `+0x04` | u32  | offset        | Start of the entry in `itemeffectchange.dbss`, at its `mesh_key` |
| `+0x08` | u32  | size          | Entry size: 13 plus the `mesh_file` length                   |

On client 3482 every one of the 6,141 index rows points at the main entry
with its mesh key and level and gives that entry's size, and the rows cover
every entry once. The first row of a group points 4 bytes past the main
group's start, after its `entry_count`.

## Layout 1

The mesh key is a u16 in both files. Only the Entry and the Index Group
differ from Layout 2.

### Entry (variable: 11 bytes + mesh file)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | mesh_key      | Item mesh key, the low 16 bits of the sheet's key (see Field Names) |
| `+0x02` | u8   | enchant_level | Enhancement level, equal to the entry's index in its group  |
| `+0x03` | str8 | mesh_file     | Lowercase `.pac` path                                       |

### Index Group (variable: 6 bytes + rows)

| Offset  | Type                 | Field     | Notes                                          |
| ------- | -------------------- | --------- | ---------------------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main group's `entry_count`          |
| `+0x04` | u16                  | mesh_key  | The mesh key of every entry the rows point at  |
| `+0x06` | Index Row[row_count] | rows      | See Index Row; `size` is 11 plus the `mesh_file` length |

## Field Names

The names come from the `EffectsChange` sheet of a private server's
`DataSheets.bexcel` on client 1784 (columns `Index`, `EnchantLevel`,
`UseMeshFile`, `IsDevelopingContents`). The sheet's `UseMeshFile` keeps its
capitals; the files store it lowercase.

| Field           | Column         | Match                                                                 |
| --------------- | -------------- | --------------------------------------------------------------------- |
| `mesh_key`      | `Index`        | Key of each sheet row                                                 |
| `enchant_level` | `EnchantLevel` | Second key of each sheet row                                          |
| `mesh_file`     | `UseMeshFile`  | 2,205 of the 2,205 (key, level) pairs the sheet shares with client 3482; 1,083 of 1,083 on client 1784, with the sheet key cut to 16 bits |

- `Index` is an item mesh key: all 215 keys of the sheet are an `Index` of
  the same workbook's `Item_Mesh_Table`, and they are 215 of the 220 rows
  there with `EffectsChangeType` `1`. On 142 of the 215 the level `0` model
  is the mesh table's own `UseMeshFile`.
- The sheet's keys reach 336,075, past 16 bits. The client 1784 file stores
  336000 as 8320 (`0x52080` cut to `0x2080`), and no two sheet keys share
  their low 16 bits, so Layout 1 holds the low half of the same key. Layout
  2 stores the full key.
- `IsDevelopingContents` is `0` on every sheet row and has no field.
- The sheet has 150 rows client 3482 does not: mesh keys 42952 to 42976 with
  six levels each. Client 3482 has 3,936 rows the sheet lacks.

## Level Groups

On client 3482 the groups come in three lengths, and within each length the
model switches at the same levels:

| entry_count | Levels    | Groups (client 3482) | Model switches at                                              |
| ----------- | --------- | -------------------- | -------------------------------------------------------------- |
| `21`        | 0 to 20   | 97, all weapons      | 19 and 20 in all 97 (`_01`, then `_02`)                         |
| `11`        | 0 to 10   | 222                  | 5 and 8 in all 222 (`_ef1`, then `_ef2`)                       |
| `6`         | 0 to 5    | 277                  | 4 and 5 in 126, 5 only in 93, never in 58                      |

Levels 19 and 20 of a 21-entry group are TET and PEN on the item scale of
`+1` to `+15` then PRI to DEC (the LOC type 79 level names, see
[`specialenchantitem.bss`](specialenchantitem_bss.md)). The scale follows
the items that wear the mesh (see Items): on client 3482 the items behind the
6-entry groups enhance to level 5 (Labreska's Helmet, Dahn's Gloves), those
behind the 11-entry groups to level 10 (Sovereign Kibelius, Edana -
Heavensmite) and those behind the 21-entry groups to level 20 (Blackstar
Longsword). The other items on these meshes are appearance and temporary
versions with no or one level, such as the Edana appearance pieces and the
(Temp) Blackstar weapons.

## Items

The item that wears a mesh is in [`itemenchant.dbss`](itemenchant_dbss.md):
its Class Entry list names an `item_mesh_key` per class type, and those keys
are the `mesh_key` of this file (Item Mesh Keys there). On client 3482, 471
of the 596 groups are named by 739 base items, and in all 1,482 of those
class entries the class type matches the class folder of the group's level
`0` model (class type `0` and `1_pc/1_phm/`, for one). Mesh `336000` is worn
by Blackstar Longsword (715001) and three more items. The `MESH_KEY_ITEMS`
lookup index turns the list around, and the Items column shows the items of
each entry's mesh.

## Notes

- All 6,141 paths on client 3482 start with `1_pc/` and end with `.pac`.
  6,129 are files under `character/model/`. The other 12, every level of
  mesh keys 43080 and 48100, name
  `1_pc/8_pwm/armor/12_foot/pwm_02_foot_0013.pac`, which client 3482 does
  not ship.
- The main groups follow neither key order nor the index's group order:
  client 3482 starts with 336000, 64640, 336001, 64641, 48066.
- The client Lua (client 3482) has no name with `EffectChange` or
  `EffectsChange` in it; the file has no Lua getter.
- The 2016 client's PDB has no `EffectsChange` or `ItemEffectChange` type.
- `itemeffectgroupstaticstatus.bss` shares the `itemeffect` prefix but is a
  different table.

## Open Questions

### Meshes Without an Item

On client 3482, 125 of the 596 mesh keys are in no `itemenchant.dbss` class
entry: 122 six-entry groups and three 21-entry groups, 95 with a weapon model
and 30 with armour, among them 17255 and 336071 to 336075. 103 of them are an `Index` of
the `Item_Mesh_Table` sheet in the private server's client 1784 workbook
(Field Names). Which item, if any, uses them is
open.
