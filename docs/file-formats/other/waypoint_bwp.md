# `*.bwp` Waypoint Graph Format

## Purpose

Waypoint graphs: named 3D points, the links between them, optional groups and optional routes. Every PABR `.bwp` under `gamecommondata/waypoint_binary/` shares this layout (1,287 files on client 3458). Each one is the binary form of the same-named Ocean tool export in `gamecommondata/waypoint/*.xml`. The worldmap node graph is `mapdata_realexplore2.bwp`: its waypoint keys are `exploration.bss` node keys, and a production sub-node's only link is its parent node.

```text
mapdata_realexplore2.bwp
  waypoint 1    town(velia)                 links 21, 22, 26, 43, 46, 102, 103, 1018, 1898
  waypoint 1880 hidden_field_goduvillage_2  links 1857 (field(goduvillage), Godu Village)
```

## Companion Files

None. The string table at the end holds the names.

All multi-byte values are little-endian unless noted otherwise.

## File Layout

Sections follow each other with no padding.

| Offset             | Type       | Field              | Notes                                                        |
| ------------------ | ---------- | ------------------ | ------------------------------------------------------------ |
| `+0x00`            | char[4]    | magic              | ASCII `PABR`                                                 |
| `+0x04`            | u32        | waypoint_count     | `1,101` in `mapdata_realexplore2.bwp`                        |
| `+0x08`            | waypoint[] | waypoints          | 23-byte rows repeated `waypoint_count` times                 |
|                    | u32        | link_count         | `2,498` in `mapdata_realexplore2.bwp`                        |
|                    | link[]     | links              | 8-byte rows repeated `link_count` times                      |
|                    | u8         | group_count        | Observed `0` or `1` only, see Open Questions                 |
|                    | group[]    | groups             | 8-byte rows repeated `group_count` times                     |
|                    | u32        | route_count        | `0` in every file but `mapdata_realnpc_route.bwp` (899)      |
|                    | route[]    | routes             | Variable-length, repeated `route_count` times                |
| `string_table_start` | table    | string_table       | Counted string table, see [`npcsimply.bss` String Table](../bss/npcsimply_bss.md#string-table-variable-4-bytes--strings); each string stored once |
| EOF - 8            | u32        | string_table_start | Equals the offset where the routes end, on all 1,287 files   |
| EOF - 4            | u32        | zero               | Always `0`                                                   |

866 of the files are empty: `waypoint_count`, `link_count`, `group_count` and `route_count` are all `0`.

## Record Structure

### Waypoint (23 bytes, repeated `waypoint_count` times)

| Offset  | Type | Field           | Notes                                                                 |
| ------- | ---- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | key             | Waypoint key, unique per file; `exploration.bss` node key in `mapdata_realexplore2.bwp` |
| `+0x04` | u32  | index           | Always the row number (`0`-based); also the string table index of the waypoint's name |
| `+0x08` | f32  | x               | World position                                                        |
| `+0x0C` | f32  | y               | Height                                                                |
| `+0x10` | f32  | z               | World position                                                        |
| `+0x14` | u8   | property        | Movement flags, see Property Values                                   |
| `+0x15` | u8   | is_sub_waypoint | `0` or `1` (`IsSubWaypoint`); `1` on 43 of 1,101 worldmap waypoints, not the same set as the `exploration.bss` sub-nodes |
| `+0x16` | u8   | is_escape       | `0` or `1` (`IsEscape`); `1` on 122 waypoints in all files, none in the worldmap |

### Link (8 bytes, repeated `link_count` times)

| Offset  | Type | Field      | Notes                        |
| ------- | ---- | ---------- | ---------------------------- |
| `+0x00` | u32  | source_key | A waypoint key of this file  |
| `+0x04` | u32  | target_key | A waypoint key of this file  |

Links are directed. `mapdata_realexplore2.bwp` stores each one both ways (1,249 pairs, no duplicates); patrol and NPC graphs also hold one-way links (83,638 over all files).

### Group (8 bytes, repeated `group_count` times)

| Offset  | Type | Field    | Notes                                                              |
| ------- | ---- | -------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | key      | Group key (`Group Key`)                                            |
| `+0x04` | u32  | name_ref | String table index of the group name; may reuse a waypoint name (`mapdata_realmonster_patrol___trollaporter_01.bwp`) |

### Route (`16 + 4 * point_count` bytes, repeated `route_count` times)

| Offset  | Type  | Field         | Notes                                           |
| ------- | ----- | ------------- | ----------------------------------------------- |
| `+0x00` | u32   | key           | Route key (`Route Key`)                         |
| `+0x04` | u32   | name_ref      | String table index of the route name            |
| `+0x08` | u32   | point_count   | Number of points                                |
| `+0x0C` | u32[] | waypoint_keys | Waypoint keys in route order, `point_count` of them |
| end     | u32   | unknown       | `0` on all 899 routes                           |

## Enum Values

### Property Values

Named after the XML `Property` attribute; they read as bit flags, with `all` setting every bit.

| Value  | Name   | Waypoints (all files) |
| ------ | ------ | --------------------- |
| `0x00` | none   | 14,284                |
| `0x01` | air    | 13,717                |
| `0x02` | wall   | 379                   |
| `0x10` | ground | 287,278               |
| `0x40` | water  | 7,023                 |
| `0xFF` | all    | 9,327                 |

## Notes

- Checked against the XML exports: in `mapdata_realexplore2`, every waypoint (key, name, position, property, both flags) and all 2,498 links match in file order; all 899 routes of `mapdata_realnpc_route` match (key, name, waypoint keys). The two one-waypoint graphs `mapdata_realexplore2___town(hausher)` and `mapdata_realexplore2___blazing_battlefield` each hold one group and match too.
- The `exploration.bss` Connections columns list each node's worldmap links from this graph, through `worldmap_links()` in `_bwp/waypoint/worldmap.py`.
- Every one of the 439 `plantzone.dbss` zones has exactly one link in `mapdata_realexplore2.bwp`, to a main node. `plantexchangegroup.bss` takes that node as the parent for its English names; it names zones the `exploration.bss` manager family misses (Godu Village 1879-1882, whose family has no main node) and corrects one it gets wrong (Specialties 1563 links to Arehaza 1380, as the Korean label says, not to Areha Palm Forest 1379 of its family).
- Checked in game 2026-09-29, all as the links say: the Specialties node that makes Box of Flesh-rich Coconuts (1563) hangs off Arehaza, the four Godu Village farms (1879-1882) off Godu Village, and four investment banks off Altinova (Zigmund 1189, Gulabi 1190, Quina 1191, Neruda Shen 1192).
- Every route ends in a u32 that is `0` on all 899 routes. The XML `Route` element has nothing besides `Key`, `Name` and `RouteWaypointList` that could map to it, so it stays `unknown`.
- The largest graphs are `mapdata_realexplore.bwp` (196,367 waypoints), `mapdata_realnpc.bwp` (18,550), `mapdata_realnpc_route.bwp` (9,383) and `mapdata_realmonster_patrol.bwp` (7,607).
- 12 `mapdata_instancedungeon*.bwp` templates (13, 46, 281 or 728 bytes) start with a small count (`00`, `01`, `04` or `0B 00 00 00`) instead of `PABR`. Their XML is empty too, so they are left unread: the preview shows an empty table that says so. A test records each one's size and fails when one grows or turns into a PABR graph, the signal to look at its layout again.

## Open Questions

### Width of `group_count`

The byte after the links is read as a u8 group count because a u32 would not fit the files with one group (`01 02 00 00 00 ...` for group key 2). No file has more than one group, so a u8 count and a one-byte "has group" flag cannot be told apart. A graph with two groups would settle it.
