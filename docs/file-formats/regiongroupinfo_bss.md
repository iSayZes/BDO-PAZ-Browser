# `regiongroupinfo.bss` Format

## Purpose

Lists the region groups that map regions belong to. Every region in `regioninfo.bss` carries a `regionGroupKey` (`+104` of its record head) that joins one row here, and each row here is used by at least one region. A row names the worldmap node of the group's main town or area and stores a world position near it.

Example:

```text
region_group_key=1   -> node 1 Velia          (regions 5 Velia, 4, 16, 17, 18, 23 ...)
region_group_key=31  -> node 601 Calpheon     (regions 77 Calpheon, 131, 257, 258 ...)
region_group_key=202 -> node 1301 Valencia City
```

The region group key is the value the client reads with `getRegionGroupKey()` on a region (`panel_lobby_characterselect_all_2.luac`, where it picks the login queue of the character's region). bdo-data-extractor ([iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor), `FORMATS.md`, section 11) documents only the `regionGroupKey` join on the `regioninfo.bss` side; the layout below is my own reading of this file.

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Node names (LOC type 29, keyed by `node_key`)         |

All multi-byte values are little-endian unless noted otherwise.

## File Layout

| Offset  | Type    | Field              | Notes                                                          |
| ------- | ------- | ------------------ | -------------------------------------------------------------- |
| `+0x00` | char[4] | magic              | `PABR` (ASCII)                                                 |
| `+0x04` | u32     | record_count       | Observed `250`                                                 |
| `+0x08` | row[]   | records            | `record_count` rows of 51 bytes, byte-packed                   |
| varies  | u32     | string_count       | Always `0`: the PABR string table is present but empty         |
| EOF-8   | u32     | string_table_start | Absolute offset of `string_count`; equals `8 + 51 × count`     |
| EOF-4   | u32     | zero_trailer       | Always `0`                                                     |

The file is `8 + 51 × 250 + 12 = 12770` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

## Record Structure

### Row (51 bytes, repeated `record_count` times)

| Offset  | Type   | Field            | Notes                                                                                              |
| ------- | ------ | ---------------- | -------------------------------------------------------------------------------------------------- |
| `+0x00` | u16    | region_group_key | Unique; joins `regionGroupKey` of `regioninfo.bss`; `0` to `302`, with gaps, not in key order      |
| `+0x02` | u8     | padding          | Always `0`                                                                                         |
| `+0x03` | u16    | unknown_03       | `500` (148 rows), `999` (49), `1000` (41), `2000` (8), `1300` (2), `3000` (Velia), `10000` (key 0) |
| `+0x05` | u16    | node_key         | Worldmap node (`exploration.bss` key, LOC type 29); `0` on 19 rows                                 |
| `+0x07` | u16    | padding          | Always `0`                                                                                         |
| `+0x09` | u8     | unknown_09       | `0` or `1`; `0` on 20 rows, nearly all without a node or position                                  |
| `+0x0A` | u8     | unknown_0a       | Equals `unknown_09` on every row                                                                   |
| `+0x0B` | u8     | unknown_0b       | `1` on 14 rows, all main towns; see Open Questions                                                 |
| `+0x0C` | f32[3] | position         | World `x, y, z`; all zero on 19 rows                                                               |
| `+0x18` | u8     | padding          | Always `0`                                                                                         |
| `+0x19` | u32    | unknown_19       | Always `1000000`                                                                                   |
| `+0x1D` | u32    | unknown_1d       | Always `1000000`                                                                                   |
| `+0x21` | u32    | unknown_21       | Always `1000000`                                                                                   |
| `+0x25` | u8[12] | padding          | Always `0`                                                                                         |
| `+0x31` | u8     | unknown_31       | Always `1`                                                                                         |
| `+0x32` | u8     | padding          | Always `0`                                                                                         |

The parser stores `node_key` as `None` when it is `0`, and `pos_x`, `pos_y`, `pos_z` as `None` when all three are `0`.

## Suggested UI Layout

| Column       | Type | Notes                                                                      |
| ------------ | ---- | -------------------------------------------------------------------------- |
| Region Group | num  | `region_group_key`                                                         |
| Node Key     | num  | `node_key`; dash when the group has none                                   |
| Node Name    | text | LOC type 29 name of `node_key` (with its parent for a sub-node), else dash |
| X            | num  | `pos_x`, whole number; dash when the position is unset                     |
| Y            | num  | `pos_y`, whole number                                                      |
| Z            | num  | `pos_z`, whole number                                                      |

The `unknown_*` fields stay on the record for search and CSV but out of the table.

## Notes

- Joining `regioninfo.bss` on `regionGroupKey` (record head `+104`) uses every one of the 250 keys and no other: no region points at a missing group and no group is unused.
- `node_key` is the `explorationKey` (`regioninfo.bss` head `+111`) of one of the group's own regions on 218 of the 231 groups that have a node. The other 13 are group `101` (node `1024`) and the open-sea groups `181` to `192` (nodes `1721` to `1733`, which have no LOC name), whose regions point at other sea nodes.
- The node is the group's main town or area: group 1 is Velia (node 1) and holds region 5 Velia (a town region), group 11 is Heidel (node 301) for Serendia, group 31 is Calpheon (node 601), group 55 Altinova (node 1101), group 202 Valencia City (node 1301).
- `position` is near the node but is not the node's position from `mapdata_realexplore2.bwp`: the distance is usually 5,000 to 50,000 units (Velia: group `7542, -6548, 72626`, node `13800, -6715, 76996`). Groups 160 to 176 and 194 to 198 share one position (`-127640, 8789, -446513`) although their nodes lie far apart, and groups 215 to 220 share another.
- The file has no strings of its own and the client has no LOC type for region group names, so a group is shown by its node.
- The client Lua uses the group key in only three places: the login queue (`getRegionGroupKey`, `getTicketCountByRegion`), the NPC navigator filter (`regionGroup`) and a worker `RegionWork` result (`regionGroupInfo`). None of them reads a field of this file by name.

## Open Questions

### unknown_03

A u16 that takes a handful of round values: `10000` on group 0, `3000` on Velia, `2000` on eight groups (Heidel, Calpheon, Calpheon Castle, Behr, Mediah Shore, Loopy Tree Forest, Valencia City and the node-less group 40), `1300` on Olvia and Olvia Academy, `999` across most of Mediah (Altinova included), Valencia and the open sea, `1000` across Kamasylvia, Drieghan and the newer regions, and `500` elsewhere. The character select screen asks for the login queue of a character's region group, so this could be a population or queue limit per group, but the mix of cities and field areas at `2000` does not fit that cleanly, and nothing in the client names it. A server-side or client function that reads it would settle it.

### unknown_09 and unknown_0a

Two flags that are always equal. They are `0` on the 19 groups without a node except group 302 (node 2113 Oceanus Sea, no position), and also `0` on groups 40 and 41, which have a position but no node, and group 177 (node 1746 Crow's Nest, no position). They look like an "in use" switch, but that reading is not confirmed.

### unknown_0b

Set on 14 groups: Velia, Heidel, Glish, Calpheon, Trent, Keplan, Altinova, Olvia, Valencia City, Shakatu, Sand Grain Bazaar, Duvencrune, O'draxxia and Olvia Academy. These are all main towns, but other main towns such as Iliya Island, Tarif, Port Epheria, Grána and Arehaza are missing, so it is not just "is a town". It may mark towns with a certain service (guild house, node war base or similar); the in-game feature it drives is unknown.

### unknown_19, unknown_1d, unknown_21 and unknown_31

Three u32 values of `1000000` and a u8 of `1` on every row. A constant cannot be told apart from the data alone; they may be rates or caps that only a patch would change.

## In-Game Checks

### Respawn at the Group Position

Needs zone: region group 160 (node 1692, O'dyllita Castle)

The position is a world point near the group's node, and several groups share one exact point: groups 160 to 176 and 194 to 198 all hold `-127640, 8789, -446513`. It could be the respawn or return point for the group, or the anchor of a map label. Die in group 160 and revive at the nearest town. If the character lands at `-127640, 8789, -446513`, the position is the group's respawn point; a different spot leaves the map label reading.
