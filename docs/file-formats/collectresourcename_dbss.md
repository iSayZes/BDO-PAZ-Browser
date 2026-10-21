# `collectresourcename.dbss` Format

## Purpose

Gathering models: each record names one world model (a rock, ore vein, tree,
herb or other plant) and the gathering character it stands for, a
`characterstatic.dbss` character with `npc_kind` Collect. Several models map
to one character: on client 3473, 30 models map to Red Coral (`10931`), 23
of them `01_nature/sea/nature_sea_coralreefs_*` and 7 SpeedTree corals
(`bush_seacoral_01`, `weed_seacoral_01` and their variants). The record key is the hash of
the model name.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes  | Records         | Row bytes               |
| ------ | -------------- | ------- | -------------------------------- | ------ | --------------- | ----------------------- |
| 1      | 1485 and later | 3474    | `collectresourcename.dbss`       | 52,109 | 1,112 Record    | 30 to 84, 47 on average |
| 1      | 1485 and later | 3474    | `collectresourcenameoffset.dbss` | 13,348 | 1,112 Index Row | 12                      |

| Layout | File                             | Known             | Unknown    |
| ------ | -------------------------------- | ----------------- | ---------- |
| 1      | `collectresourcename.dbss`       | 52,109 B (100.0%) | 0 B (0.0%) |
| 1      | `collectresourcenameoffset.dbss` | 13,348 B (100.0%) | 0 B (0.0%) |

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

| File                                 | Required | Role                                                                 |
| ------------------------------------ | -------- | -------------------------------------------------------------------- |
| `collectresourcenameoffset.dbss`     | Optional | `name_hash -> (data_offset, data_size)` index, see below; the records can be walked without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row |

Character names come from LOC type 6.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                                |
| ------- | ------------- | ------- | ---------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `1,112` on client 3473            |
| `+0x04` | Record[count] | records | Back to back to the end of the file; see Record      |

### Record (variable: 18 bytes + name text)

| Offset                    | Type | Field              | Notes                                                                  |
| ------------------------- | ---- | ------------------ | ---------------------------------------------------------------------- |
| `+0x00`                   | u32  | name_hash          | lookup3 `hashlittle` of the `resource_file_name` bytes with seed `0xC5EDE`; unique per record, the index key |
| `+0x04`                   | u32  | name_hash_dup      | Equal to `name_hash` in every record; the index's `data_offset` points here |
| `+0x08`                   | str8 | resource_file_name | Model name, lower case, no file extension; unique per record           |
| `resource_file_name+0x00` | u16  | character_key      | Gathering character, a `characterstatic.dbss` `character_id`           |

`name_hash` is the same hash `_common/string_hash.py` computes for
`stringtable.bss` keys, run over the ASCII name bytes instead of UTF-16LE:
`weed_seasphere_b_01` hashes to `0xDEA23636`. It matches all 1,112 records
on client 3473 and all 1,017 on client 1784. The records are not sorted by
hash, name or character.

### `collectresourcenameoffset.dbss`

| Offset  | Type             | Field | Notes                                      |
| ------- | ---------------- | ----- | ------------------------------------------ |
| `+0x00` | u32              | count | Equals the `collectresourcename.dbss` count |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row        |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                      |
| ------- | ---- | ----------- | ------------------------------------------ |
| `+0x00` | u32  | name_hash   | Record key                                 |
| `+0x04` | u32  | data_offset | Record start + 4, at `name_hash_dup`       |
| `+0x08` | u32  | data_size   | Record size - 4: `14` + the name length    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The rows
are not in file order; on client 3473 every row matches the record walked
from the start of the file.

## Field Names

The record is the `CollectResourceName_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, with the columns `ResourceFileName` and
`CharacterObjectIndex`. The compiled name is the sheet's `ResourceFileName`
in lower case, trimmed, with its last extension (`.pam`, `.srt`) cut off:
`00_Common/Lamp/Lamp_Stand_FirePot_01.On.pam` is stored as
`00_common/lamp/lamp_stand_firepot_01.on`, and the sheet's
`tree_alaskacedar_short_b_01.srt ` (with a trailing space) as
`tree_alaskacedar_short_b_01`.

| Field              | Column                 | Shared names, same value |
| ------------------ | ---------------------- | ------------------------ |
| resource_file_name | `ResourceFileName`     | 1,017 of 1,017 (client 1784), 1,011 of 1,011 (client 3473) |
| character_key      | `CharacterObjectIndex` | 1,017 of 1,017 (client 1784), 1,011 of 1,011 (client 3473) |

Client 3473 has 101 names the sheet lacks, and 6 of the sheet's names
(`collecting_mushroom_14_c` to `_17`, `08_dri_stone_set01_04`,
`drigan_yeti_jade_04`) are gone.

## Notes

- On client 3473 the 1,112 records name 561 distinct characters. Every one
  is a `characterstatic.dbss` character with `npc_kind` Collect, and every
  one is also the u16 key that starts a row of [`collect.dbss`](collect_dbss.md) (713 rows on
  client 3474). The character's `label_kr` is often one of its
  model names in another case (`Weed_Seasphere_01` for Agar `10369`, whose
  four models are `weed_seasphere_01`, `_02`, `_b_01` and `_c_01`).
- The name has two forms (client 3473). 423 names hold a folder and are a
  model path below `object/` without `.pam`: 394 of them exist as
  `object/<name>.pam`, the other 29 have no file. The 689 names without a
  folder are SpeedTree basenames: 662 exist as `speedtreedata/**/<name>.srt`,
  15 only as a `.pam` basename (`07_dri_stone_set*`, `collecting_oldtree_*`),
  12 have no file.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  lists this file with `collect.dbss` as "gatherable identity and internal
  mesh names; no yields or rates", which fits: the record holds no item,
  rate or position.
