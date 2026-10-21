# `regiongroupinfo.bss` Format

## Purpose

Lists the region groups that map regions belong to. Every region in `regioninfo.bss` carries a `regionGroupKey` (`+104` of its record head) that joins one row here, and each row here is used by at least one region. A row names the worldmap node of the group's main town or area, a concurrent user limit, three enable flags and a display position near the node.

The region group key is the value the client reads with `getRegionGroupKey()` on a region (`panel_lobby_characterselect_all_2.luac`, where it picks the login queue of the character's region). bdo-data-extractor ([iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor), `FORMATS.md`, section 11) documents only the `regionGroupKey` join on the `regioninfo.bss` side; the layout below is my own reading of this file, with field names from the sources in Field Names.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes  | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ------ | ------- | --------- |
| 2      | 2519 and later | 3474    | `regiongroupinfo.bss` | 12,770 | 250 Row | 51        |
| 1      | 1230 to 2107   | 2107    | `regiongroupinfo.bss` | 8,595  | 175 Row | 49        |

| Layout | File                  | Known            | Unknown      |
| ------ | --------------------- | ---------------- | ------------ |
| 2      | `regiongroupinfo.bss` | 12,270 B (96.1%) | 500 B (3.9%) |
| 1      | `regiongroupinfo.bss` | 8,595 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3251   | Layout 2             |
| 3002   | Layout 2             |
| 2519   | Layout 2             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | Layout 1             |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Node names (LOC type 29, keyed by `node_key`)         |

All multi-byte values are little-endian unless noted otherwise.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                                          |
| ------------------- | ----------------- | ------------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                                 |
| `+0x04`             | u32               | record_count       | Observed `250`                                                 |
| `+0x08`             | Row[record_count] | records            | `record_count` rows of 51 bytes, byte-packed                   |
| `records+0x00`      | String Table      | string_table       | Always empty: the PABR string table is present but empty       |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 51 × count`     |
| `string_table+0x04` | u32               | zero               | Always `0`                                                     |

The file is `8 + 51 × 250 + 12 = 12770` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (51 bytes)

| Offset  | Type   | Field            | Notes                                                                                              |
| ------- | ------ | ---------------- | -------------------------------------------------------------------------------------------------- |
| `+0x00` | u16    | region_group_key | Unique; joins `regionGroupKey` of `regioninfo.bss`; `0` to `302`, with gaps, not in key order      |
| `+0x02` | u8     | is_blocked_managing | Always `0`                                                                                      |
| `+0x03` | u16    | concurrent_playable_user_count | `500`, `999`, `1000`, `1300`, `2000`, `3000` (Velia) or `10000` (key 0), see below |
| `+0x05` | u32    | node_key         | Worldmap node (`exploration.bss` key, LOC type 29); `0` on 19 rows                                 |
| `+0x09` | u8     | enable_corp_productivity | `0` on 20 rows, nearly all without a node or position                                      |
| `+0x0A` | u8     | enable_fishing_productivity | Equals `enable_corp_productivity` on every row                                          |
| `+0x0B` | u8     | enable_loyalty   | `1` on 14 rows, all main towns, see below                                                          |
| `+0x0C` | f32[3] | display_graph_position | World `x, y, z`; all zero on 19 rows                                                         |
| `+0x18` | u8     | is_productivity_changed | Always `0`                                                                                  |
| `+0x19` | i32    | corp_productivity | Always `1000000`, the 2016 loader's default                                                       |
| `+0x1D` | i32    | fishing_productivity | Always `1000000`, the 2016 loader's default                                                    |
| `+0x21` | i32    | loyalty          | Always `1000000`, the 2016 loader's default                                                        |
| `+0x25` | i32[3] | varied_productivity | Always `0`: `_variedCorpProductivity`, `_variedFishingProductivity`, `_variedLoyalty`           |
| `+0x31` | u8     | unknown_31       | Always `1`; after the 2016 members, see Open Questions                                             |
| `+0x32` | u8     | unknown_32       | Always `0`                                                                                         |

Earlier versions of this doc read `+0x05` as a u16 with two bytes of padding and called the fields from `+0x03` to `+0x21` `unknown_03` to `unknown_21`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 1

On client 1784 a Row was 49 bytes: it ended after `varied_productivity`,
without `unknown_31` and `unknown_32`. Only the Row differs from Layout 2.
The file holds `170` rows on client 1784.

### Row (49 bytes)

| Offset  | Type   | Field                          | Notes |
| ------- | ------ | ------------------------------ | ----- |
| `+0x00` | u16    | region_group_key               |       |
| `+0x02` | u8     | is_blocked_managing            |       |
| `+0x03` | u16    | concurrent_playable_user_count |       |
| `+0x05` | u32    | node_key                       |       |
| `+0x09` | u8     | enable_corp_productivity       |       |
| `+0x0A` | u8     | enable_fishing_productivity    |       |
| `+0x0B` | u8     | enable_loyalty                 |       |
| `+0x0C` | f32[3] | display_graph_position         |       |
| `+0x18` | u8     | is_productivity_changed        |       |
| `+0x19` | i32    | corp_productivity              |       |
| `+0x1D` | i32    | fishing_productivity           |       |
| `+0x21` | i32    | loyalty                        |       |
| `+0x25` | i32[3] | varied_productivity            |       |

## Row Values

### `concurrent_playable_user_count` Values (client 3473)

| Value   | Rows | Groups |
| ------- | ---- | ------ |
| `10000` | 1    | Group 0 |
| `3000`  | 1    | Velia |
| `2000`  | 8    | Heidel, Calpheon, Calpheon Castle, Behr, Mediah Shore, Loopy Tree Forest, Valencia City and the node-less group 40 |
| `1300`  | 2    | Olvia and Olvia Academy |
| `1000`  | 41   | Kamasylvia, Drieghan and the newer regions |
| `999`   | 49   | Most of Mediah (Altinova included), Valencia and the open sea |
| `500`   | 148  | All other groups |

The character select screen asks for the login queue of a character's region group (`getTicketCountByRegion`), which fits a per-group user limit.

### `enable_loyalty` Groups

Set on 14 groups: Velia, Heidel, Glish, Calpheon, Trent, Keplan, Altinova, Olvia, Valencia City, Shakatu, Sand Grain Bazaar, Duvencrune, O'draxxia and Olvia Academy. Other main towns such as Iliya Island, Tarif, Port Epheria, Grána and Arehaza are not.

The parser stores `node_key` as `None` when it is `0`, and `display_graph_position` as `pos_x`, `pos_y`, `pos_z`, each `None` when all three are `0`. It keeps the fields with a value other than `0` and leaves out `is_blocked_managing`, `is_productivity_changed` and `varied_productivity`.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::RegionGroupInfo` holds `_key`, `_isBlockedManaging`, `_concurrentPlayableUserCount`, `_waypointKey` (i32), `_enableCorpProductivity`, `_enableFishingProductivity`, `_enableLoyalty`, `_regionPosition`, `_isProductivityChanged`, `_corpProductivity`, `_fishingProductivity`, `_loyalty`, `_variedCorpProductivity`, `_variedFishingProductivity` and `_variedLoyalty` (all i32), with pointers in between. The row stores them in this order without the pointers or padding, from `+0x00` to `+0x30`. `GameCommonParameterLoaderFromExcel::LoadRegionGroupInformation` reads `RegionGroupKey`, `WaypointKey`, `DisplayGraphPositionX` to `Z`, `CorpProductivity`, `FishingProductivity`, `Loyalty` (as bools) and `ConcurrentPlayableUserCount` from `RegionGroup_Table` into those members, and sets `_corpProductivity`, `_fishingProductivity` and `_loyalty` to `1000000` and the three varied values to `0` for every row: the values this file stores.

The `RegionGroup_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 and the same table of a second private server on client 519 match the file by value over the group keys each shares with client 3473:

| Column | Field | Equal (client 1784, 169 keys) | Equal (client 519, 150 keys) |
| ------ | ----- | ------------------------ | ------------------------ |
| `WaypointKey` | `node_key` | 168 | 148 |
| `CorpProductivity` | `enable_corp_productivity` | 168 | 149 |
| `FishingProductivity` | `enable_fishing_productivity` | 168 | 149 |
| `Loyalty` | `enable_loyalty` | 169 | 150 |
| `ConcurrentPlayableUserCount` | `concurrent_playable_user_count` | 139 | 118 |
| `DisplayGraphPositionX` to `Z` | `display_graph_position` | 168 | 149 |

The two productivity flags hold the same value on every row in all three sources, so they are told apart by the 2016 order alone. The other `ConcurrentPlayableUserCount` rows are raises (`500` to `1000` on 25 bexcel rows, `500` or `999` to `2000` on 5); the file and both tables use the same seven values. Group 179 has both productivity flags set here and clear in both tables. `is_blocked_managing` and `is_productivity_changed` have no column; they are named from their place in the 2016 member order.

## Notes

- Joining `regioninfo.bss` on `regionGroupKey` (record head `+104`) uses every one of the 250 keys and no other: no region points at a missing group and no group is unused.
- `node_key` is the `explorationKey` (`regioninfo.bss` head `+111`) of one of the group's own regions on 218 of the 231 groups that have a node. The other 13 are group `101` (node `1024`) and the open-sea groups `181` to `192` (nodes `1721` to `1733`, which have no LOC name), whose regions point at other sea nodes.
- The node is the group's main town or area: group 1 is Velia (node 1) and holds region 5 Velia (a town region), group 11 is Heidel (node 301) for Serendia, group 31 is Calpheon (node 601), group 55 Altinova (node 1101), group 202 Valencia City (node 1301).
- `display_graph_position` is near the node but is not the node's position from `mapdata_realexplore2.bwp`: the distance is usually 5,000 to 50,000 units (Velia: group `7542, -6548, 72626`, node `13800, -6715, 76996`). Groups 160 to 176 and 194 to 198 share one position (`-127640, 8789, -446513`) although their nodes lie far apart, and groups 215 to 220 share another. The sheet column is `DisplayGraphPosition` and the 2016 member `_regionPosition`.
- The file has no strings of its own and the client has no LOC type for region group names, so a group is shown by its node.
- The client Lua uses the group key in only three places: the login queue (`getRegionGroupKey`, `getTicketCountByRegion`), the NPC navigator filter (`regionGroup`) and a worker `RegionWork` result (`regionGroupInfo`). None of them reads a field of this file by name.
- The client 519 private server loads `CorpProductivity`, `FishingProductivity` and `Loyalty` but never reads them back. Every 15 minutes its `RegionProductivityService` picks a random value from 500,000 to 1,000,000 per group for each of `Loyalty`, `Farming` and `Fishing` and sends all groups in one packet, as fishing, farming, loyalty per group. It calls corp productivity "Farming", which is its own name and no client source confirms it.

## Open Questions

### What the Productivity and Loyalty Flags Drive

The client Lua reads none of the three enable flags or the productivity values. It registers `FromClient_NotifyChangeRegionProductivity`, which only refreshes the worker and node product windows (`new_worldmap_workmanager_plant.luac`, `panel_worldmap_nodeproduct_renew.luac`), so the server can change a region's productivity at run time. The 2016 `_varied*` members suggest it adjusts the `1000000` base per group; which game feature the corp, fishing and loyalty values stand for is unknown.

### unknown_31

A u8 of `1` on every row, after the last 2016 member. A constant cannot be told apart from the data alone, and no sheet column is left to match it.
