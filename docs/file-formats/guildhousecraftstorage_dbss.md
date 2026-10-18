# `guildhousecraftstorage.dbss` Format

## Purpose

A storage count per guild storage house use: one row per
[`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) receipe key, Storage
(`2`) and Guild Storage level 2 to 9 (`50001` to `50009`) only, each with
one u16 `storage_count`. Companion `guildhousecraftstorageoffset.dbss` lists
where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ----------------------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `guildhousecraftstorage.dbss`       | 104   | 10 Row        | 10        |
| 1      | 1784 and later | 3474    | `guildhousecraftstorageoffset.dbss` | 124   | 10 Offset Row | 12        |

| Layout | File                                | Known          | Unknown    |
| ------ | ----------------------------------- | -------------- | ---------- |
| 1      | `guildhousecraftstorage.dbss`       | 104 B (100.0%) | 0 B (0.0%) |
| 1      | `guildhousecraftstorageoffset.dbss` | 124 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                                | Required | Role                                                                 |
| ----------------------------------- | -------- | -------------------------------------------------------------------- |
| `guildhousecraftstorageoffset.dbss` | Optional | `receipe_key -> (data_offset, data_size)` of every row; the rows are 10 bytes each and can be walked without it |
| `languagedata_en.loc`               | Optional | House use name (type `16`, `str_id1` = `receipe_key`)                |

The handler links each `receipe_key` to its `houseinforeceipe.dbss` row
without loading that file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `10` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (10 bytes)

| Offset  | Type | Field           | Notes                                                            |
| ------- | ---- | --------------- | ---------------------------------------------------------------- |
| `+0x00` | i32  | receipe_key     | House use, a `houseinforeceipe.dbss` key; unique per row         |
| `+0x04` | i32  | receipe_key_dup | Equal to `receipe_key` in every row; the offset file points here |
| `+0x08` | u16  | storage_count   | See Storage Counts                                               |

The rows run `50002`, `2`, `50001`, then `50003` upward, to `50009` on
client 3474 and to `50006` on client 1784.

### `guildhousecraftstorageoffset.dbss`

| Offset  | Type              | Field | Notes                                          |
| ------- | ----------------- | ----- | ---------------------------------------------- |
| `+0x00` | u32               | count | Equals the `guildhousecraftstorage.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row           |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                           |
| ------- | ---- | ----------- | ----------------------------------------------- |
| `+0x00` | u32  | receipe_key | Key of the row it points at                     |
| `+0x04` | u32  | data_offset | Row start + 4, at `receipe_key_dup`             |
| `+0x08` | u32  | data_size   | `6`: the row without its leading `receipe_key`  |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
lists key `2` first, then the rows in file order; on clients 1784 and 3474
every index row points at the row with its key.

## Storage Counts

`storage_count` per row on both clients:

| Receipe key | House use             | Client 1784 | Client 3474 |
| ----------- | --------------------- | ----------- | ----------- |
| `2`         | Storage               | `2`         | `10`        |
| `50001`     | Guild Storage level 2 | `2`         | `10`        |
| `50002`     | Guild Storage level 3 | `3`         | `10`        |
| `50003`     | Guild Storage level 4 | `4`         | `10`        |
| `50004`     | Guild Storage level 5 | `5`         | `12`        |
| `50005`     | Guild Storage level 6 | `6`         | `6`         |
| `50006`     | Guild Storage level 7 | `7`         | `7`         |
| `50007`     | Guild Storage level 7 | none        | `7`         |
| `50008`     | Guild Storage level 8 | none        | `8`         |
| `50009`     | Guild Storage level 9 | none        | `9`         |

LOC type 16 names both `50006` and `50007` "Guild Storage level 7"
(client 3474), and so does the Korean `houseinforeceipe.dbss` name
(`길드 창고 7단계`).

## Field Names

The 2016 PDB has no guild house craft storage struct. The server dump of a
private server on client 1784 reads the table with
`loadHouseForGuildHouseCraftStorageCountInfo` and reports a missing row as
`GuildHouseCraftSkillStaticStatusManager::getXXX() GuildHouseCraftStorage
Open Failed.`, so the [`guildhousecraftskill.dbss`](guildhousecraftskill_dbss.md)
manager holds both tables.

The values match the `GuildHouseCraftStorageCount` sheet of a private
server's `DataSheets.bexcel` on client 1784 by `HouseInfoSkillNo`:

| Field         | Column             | Same value (client 1784) | Same value (client 3474) |
| ------------- | ------------------ | ------------------------ | ------------------------ |
| receipe_key   | `HouseInfoSkillNo` | 7 of 7 rows              | 7 of 7 shared rows       |
| storage_count | `StorageCount`     | 7 of 7                   | 2 of 7                   |

The row has one value field and the sheet one value column. Client 3474
raises the count of keys `2` and `50001` to `50004` (see Storage Counts)
and adds the rows `50007`, `50008` and `50009`, which the sheet and client
1784 do not have. The sheet's key column is named `HouseInfoSkillNo`, but
its values are receipe keys.

## Notes

- [`guildhousecraftskill.dbss`](guildhousecraftskill_dbss.md) has a row for
  every key of this file; there the same rows grant Ample Storage Lv. 1 to
  37.
- The guild house Lua (`worldmap_grand_guildhousecontrol.luac`,
  `panel_worldmap_guildhousemanagement_renew.luac`) skips Depot house uses
  (`CppEnums.eHouseUseType.Depot`) in its craft lists and reads no storage
  count. No `.luac` file of client 3474 holds the strings `CraftStorage` or
  `StorageCount`.

## Open Questions

### What `storage_count` Counts

On client 1784 `storage_count` equals the Guild Storage level of its row
(`2` for Storage and level 2). On client 3474 Storage and levels 2 to 4 hold
`10`, level 5 holds `12`, and levels 6 to 9 keep the level number again.
No client Lua reads the value, so whether it is a number of storage slots,
of guild storage pages or something else is open.
