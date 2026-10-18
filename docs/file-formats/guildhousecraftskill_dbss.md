# `guildhousecraftskill.dbss` Format

## Purpose

The guild skills a guild house use grants: one row per house use (a
[`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) receipe key) with up to
five skill numbers. The Guild Shipyard grants Building Boat Lv. 1 and 2, the
specialty packing workshops Local Economy Revitalization, and Storage and
Guild Storage level 2 to 9 grant Ample Storage Lv. 1 to 37 between them.
Companion `guildhousecraftskilloffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `guildhousecraftskill.dbss`       | 384   | 19 Row        | 20        |
| 1      | 1784 and later | 3474    | `guildhousecraftskilloffset.dbss` | 232   | 19 Offset Row | 12        |

| Layout | File                              | Known          | Unknown     |
| ------ | --------------------------------- | -------------- | ----------- |
| 1      | `guildhousecraftskill.dbss`       | 346 B (90.1%)  | 38 B (9.9%) |
| 1      | `guildhousecraftskilloffset.dbss` | 232 B (100.0%) | 0 B (0.0%)  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                 |
| --------------------------------- | -------- | -------------------------------------------------------------------- |
| `guildhousecraftskilloffset.dbss` | Optional | `receipe_key -> (data_offset, data_size)` of every row; the rows are 20 bytes each and can be walked without it |
| `languagedata_en.loc`             | Optional | House use name (type `16`, `str_id1` = `receipe_key`) and skill name (type `10`, `str_id1` = skill number) |

The handler links each `receipe_key` to its `houseinforeceipe.dbss` row and
each skill number to its first `skill.dbss` row. It loads neither file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `19` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (20 bytes)

| Offset  | Type   | Field           | Notes                                                              |
| ------- | ------ | --------------- | ------------------------------------------------------------------ |
| `+0x00` | i32    | receipe_key     | House use, a `houseinforeceipe.dbss` key; unique per row           |
| `+0x04` | i32    | receipe_key_dup | Equal to `receipe_key` in every row; the offset file points here   |
| `+0x08` | u16    | unknown_08      | `0` on every row (clients 1784 and 3474); see Open Questions       |
| `+0x0A` | u16[5] | skill_nos       | Skill numbers in slot order, `0` in an unused slot; see Skill Slots |

The rows are sorted neither by key nor in index order: on client 3474 the
file runs 50009 down to 50001, 1610 down to 1604, 1602, 1601 and ends with
`2`.

### `guildhousecraftskilloffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `guildhousecraftskill.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                              |
| ------- | ---- | ----------- | -------------------------------------------------- |
| `+0x00` | u32  | receipe_key | Key of the row it points at                        |
| `+0x04` | u32  | data_offset | Row start + 4, at `receipe_key_dup`                |
| `+0x08` | u32  | data_size   | `16`: the row without its leading `receipe_key`    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
lists the rows in file order except key `2`, which sits between 1604 and
1602 (client 3474). On clients 1784 and 3474 every index row points at the
row with its key.

## Skill Slots

Each filled slot is a `skill.dbss` skill number, named by LOC type 10. The
slots fill from the first with no gap. On client 3474 the 19 rows fill 48
slots with 44 distinct skills:

| Receipe keys       | House use                                  | Skills (client 3474)                               |
| ------------------ | ------------------------------------------ | -------------------------------------------------- |
| `1601`             | Guild Shipyard                             | `65042`, `65043` Building Boat Lv. 1 and 2          |
| `1602`             | Elephant Nursery                           | `65052`, `65053` Monstrous Force Lv. 1 and 2        |
| `1604`             | Imperial Trade Packing                     | `65057` Imperial Calling                            |
| `1605` to `1609`   | Balenos to Valencia Specialties Packing    | `65058` Local Economy Revitalization, all five rows |
| `1610`             | Mount Part Workshop                        | `65059` Fully Prepared                              |
| `2`                | Storage                                    | Ample Storage Lv. 1 to 5                            |
| `50001` to `50009` | Guild Storage level 2 to 9                 | Ample Storage Lv. 6 to 37, 1 to 5 levels per row    |

## Field Names

The 2016 PDB has no guild house craft skill struct. The server dump of a
private server on client 1784 names the class
`gc::GuildHouseCraftSkillStaticStatus`, keyed by `gc::KeyType<int,-1>` (an
i32), loaded by `loadHouseForGuildHouseCraftSkillInfo`.

The values match the `GuildHouseCraftSkillInfo` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `HouseInfoReceipeKey`:

| Field          | Column                 | Same value (client 1784) | Same value (client 3474) |
| -------------- | ---------------------- | ------------------------ | ------------------------ |
| receipe_key    | `HouseInfoReceipeKey`  | 16 of 16 rows            | 16 of 16 shared rows     |
| skill_nos[0]   | `SkillNo_1`            | 16 of 16                 | 16 of 16                 |
| skill_nos[1]   | `SkillNo_2`            | 16 of 16                 | 16 of 16                 |
| skill_nos[2]   | `SkillNo_3`            | 16 of 16                 | 15 of 16                 |
| skill_nos[3]   | `SkillNo_4`            | 16 of 16                 | 15 of 16                 |
| skill_nos[4]   | `SkillNo_5`            | 16 of 16                 | 15 of 16                 |

The one miss on client 3474 is Guild Storage key `50006`, which adds
`65228`, `65229` and `65230` (Ample Storage Lv. 25 to 27) in slots 3 to 5
where the sheet and client 1784 have none. Client 3474 also adds the rows
`50007`, `50008` and `50009`, which neither has. The sheet has no column for
`unknown_08`.

## Notes

- [`guildhousecraftskillreverselinklist.bss`](guildhousecraftskillreverselinklist_bss.md)
  holds the reverse of this table: per skill number, the rows that list it as
  (`receipe_key`, slot) pairs, the slot counted from `1` for `skill_nos[0]`.
  Skill `65058` lists `1605` to `1609`, each at slot `1`.
- `guildhousecraftstorage.dbss` (not documented yet) is keyed by the same
  receipe keys, Storage and Guild Storage only; the private server sheet
  `GuildHouseCraftStorageCount` behind it has the columns `HouseInfoSkillNo`
  and `StorageCount`.
- The guild house Lua (`worldmap_grand_guildhousecontrol.luac`,
  `panel_worldmap_guildhousemanagement_renew.luac`) reads the house uses
  through `getGuildHouseCraftInfoManager()` and `getHouseCraftWrapperByIndex()`
  and reads no skill from this table.

## Open Questions

### What `unknown_08` Holds

The u16 between `receipe_key_dup` and `skill_nos` is `0` in all 19 rows on
client 3474 and all 16 on client 1784, and the source sheet has no column
for it. The reverse link list counts slots from `1`, so one reading is a
six-entry u16 array whose slot `0` is never used; nothing in the client
confirms it.
