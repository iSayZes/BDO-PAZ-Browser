# `guildhouseinfo.dbss` Format

## Purpose

The guild houses: one variable-length row per guild house with its town,
its worldmap node and its uses (a [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md)
receipe and the highest level the house reaches with it), the house's
character key after them. The client Lua reads a row through
`ToClient_GetGuildHouseInfoStaticStatusWrapper(houseKey)`. The node houses
are in [`houseinfo.bss`](houseinfo_bss.md), whose row ends in the same
`Craft` entries. Companion `guildhouseinfooffset.dbss` lists where every row
sits.

On client 3482 the 23 rows cover eight towns: Velia, Olvia, Heidel,
Calpheon City, Altinova, Tarif, Valencia City and Marzana's Villa (town
`650`, the four Valencia guild houses on Shakatu, Taphtar Plain, Pujiya
Canyon and Cadry Ruins). The file is byte for byte the same on clients 1784
and 3482.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | ---------------- | --------- |
| 1      | 1348 and later | 3482    | `guildhouseinfo.dbss`       | 974   | 81 Craft, 23 Row | 8         |
| 1      | 1348 and later | 3482    | `guildhouseinfooffset.dbss` | 234   | 23 Offset Row    | 10        |

| Layout | File                        | Known          | Unknown     |
| ------ | --------------------------- | -------------- | ----------- |
| 1      | `guildhouseinfo.dbss`       | 928 B (95.3%)  | 46 B (4.7%) |
| 1      | `guildhouseinfooffset.dbss` | 234 B (100.0%) | 0 B (0.0%)  |

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

| File                         | Required | Role                                                                                      |
| ---------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `guildhouseinfooffset.dbss`  | Optional | `character_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `houseinforeceipe.dbss`      | Optional | Korean receipe names for the uses when LOC has none                                        |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a house key without a row shows as plain text          |
| `languagedata_en.loc`        | Optional | House names (type 6), town names (type 17), node names (type 29), receipe names (type 16)  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3482 the file is 974 bytes: 12 rows of four uses (46 bytes) and
11 of three (38 bytes).

### Row (variable: 14 bytes + crafts)

| Offset        | Type               | Field             | Notes                                                                                   |
| ------------- | ------------------ | ----------------- | --------------------------------------------------------------------------------------- |
| `+0x00`       | u16                | affiliated_town   | Town the house belongs to, a `regioninfo.bss` region key (LOC type 17: `5` Velia, `229` Valencia City) |
| `+0x02`       | u32                | parent_node_key   | Worldmap node of the house (LOC type 29); `getParentNodeKey()`                          |
| `+0x06`       | u32                | craft_count       | Number of `crafts`; `getReceipeCount()`                                                  |
| `+0x0A`       | Craft[craft_count] | crafts            | The uses the house can be set to; see Craft                                             |
| `crafts+0x00` | u16                | character_key     | Row key: the house's `characterstatic.dbss` character                                    |
| `crafts+0x02` | u16                | unknown_crafts_02 | `0xFFFF` on every row (clients 1784 and 3482); see Open Questions                        |

### Craft (8 bytes)

| Offset  | Type | Field       | Notes                                                                       |
| ------- | ---- | ----------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | receipe_key | [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) receipe key; `getHouseCraftWrapperByIndex(i):getReceipeKeyRaw()` |
| `+0x04` | u32  | level       | Highest level of the use in this house; `getMaxLevel(receipeKey)`            |

Every row (client 3482) ends with receipe `1610` (Mount Part Workshop) at
level 1, `2` (Storage) at level 5 and `50001` (Guild Storage level 2) at
level 3. The four-use rows open with `1601` (Guild Shipyard) or `1602`
(Elephant Nursery) at level 2.

### `guildhouseinfooffset.dbss`

Bare offset table into `guildhouseinfo.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `guildhouseinfo.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                           |
| ------- | ---- | ------------- | --------------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                                     |
| `+0x02` | u32  | data_offset   | Absolute offset of the row in `guildhouseinfo.dbss`, at `affiliated_town` |
| `+0x06` | u32  | data_size     | The whole row: `46` or `38` bytes                               |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3482 every
index row points at a row whose `character_key` is its key.

## Field Names

The `GuildHouseInfo` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CharacterKey`, `AffiliatedTown`, `ParentNode`
and `CraftList` (`1601:2, 1610:1, 2:5, 50001:3`). The 2016
`gc::GuildHouseInfoStaticStatus` holds `_affiliatedTownKey`,
`_parentNodeKey`, `_houseCraftList` (`gc::HouseInfoCraft`: `_receipeKey`,
`_level`) and `_key`, in the file's order.

| Field           | Column           | Same value (client 1784) |
| --------------- | ---------------- | ------------------------ |
| character_key   | `CharacterKey`   | 23 of 23                 |
| affiliated_town | `AffiliatedTown` | 23 of 23                 |
| parent_node_key | `ParentNode`     | 23 of 23                 |
| crafts          | `CraftList`      | 23 of 23                 |

## Notes

- The guild house Lua (`worldmap_grand_guildcraft.luac`,
  `worldmap_grand_guildhousecontrol.luac`,
  `panel_worldmap_guildhousemanagement_renew.luac`) calls `getHouseName()`,
  `getParentNodeKey()`, `getReceipeCount()`,
  `getHouseCraftWrapperByIndex(index)`, `getHouseCraftWrapperByKeyRaw(key)`
  and `getMaxLevel(receipeKey)` on the wrapper.
- Guild houses of one town share a node: the seven Calpheon City guild
  houses (`2427` to `2704`) node `601`, the four Valencia City houses
  `3355` to `3358` node `1301`. The houses `3351` to `3354` of town `650`
  sit on four different nodes.
- Grána (`3520`) and O'draxxia (`3806`) Guild Houses are house characters of
  [`householdlist.bss`](householdlist_bss.md) with no row here.

## Open Questions

### What `unknown_crafts_02` Holds

The u16 after the key is `0xFFFF` on all 23 rows of clients 1784 and 3482,
as `unknown_0a` after the key of [`houseinfo.bss`](houseinfo_bss.md). The
2016 `gc::GuildHouseInfoStaticStatus` follows `_key` with
`bool _isBlockedNpcWork` and `KeyType<short,-1> _territoryKey`, whose unset
value is `-1`; no sheet column fills it, so the field is not named.
