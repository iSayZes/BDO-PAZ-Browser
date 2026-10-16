# `exploration.bss` Format

## Purpose

Stores the worldmap node network: one record per node (towns, connection nodes, danger zones and worker production sub-nodes). The primary key is a node key that resolves through LOC `str_type=29` (`str_id4=0` name, `str_id4=1` description) and matches the waypoint keys in `mapdata_realexplore2.bwp`. Each record also carries its node kind, contribution cost, manager and representative NPCs, and the knowledge entries tied to the node.

Field names for several head fields and the `ExplorationNodeType` mapping follow [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, section 12), checked against the bytes of the current client file below.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                  |
| --------------------- | -------- | --------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Resolves node names/descriptions (type 29) and NPC names (type 6)     |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type                      | Field              | Notes                                                           |
| ------------------- | ------------------------- | ------------------ | --------------------------------------------------------------- |
| `+0x00`             | char[4]                   | magic              | `PABR` (ASCII)                                                  |
| `+0x04`             | u32                       | record_count       | Observed `1003` (2026-09-27 client: `1080`)                     |
| `+0x08`             | Node Record[record_count] | records            | 117-byte head plus seven counted lists, packed back-to-back     |
| `records+0x00`      | Footer                    | footer             | `u32 count` plus `count` 6-byte rows; observed `111` rows       |
| `footer+0x00`       | String Table              | string_table       | `u32 count` plus Korean strings; observed `622` entries         |
| `string_table+0x00` | u32                       | string_table_start | Absolute file offset of `string_table.count`; observed `157953` |
| `string_table+0x04` | u32                       | zero               | Observed `0`                                                    |

Walking the records with this layout ends at `157283`, the footer ends at `157953` (equal to `string_table_start`) and the string table ends exactly at `EOF-8`, so the file tiles with no gaps.

### Node Record (variable: 117 bytes + lists)

| Offset  | Type      | Field | Notes                         |
| ------- | --------- | ----- | ----------------------------- |
| `+0x00` | Node Head | head  | See Node Head                 |
| `+0x75` | List[7]   | lists | Seven counted lists, see List |

### Node Head (117 bytes)

| Offset  | Type      | Field                 | Notes                                                                                                                                                 |
| ------- | --------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+0x00` | u16       | node_key              | LOC `str_type=29`, `str_id1=node_key`; unique; all 1003 resolve                                                                                       |
| `+0x02` | u16       | unknown_02            | Always `0`                                                                                                                                            |
| `+0x04` | u8        | enabled               | `1` on 999 records; `0` on 4 records whose name is `UnKnown` (1503, 1706, 1831, 1839)                                                                 |
| `+0x05` | u8        | node_kind             | Client `ExplorationNodeType`; see table below                                                                                                         |
| `+0x06` | u16       | node_key_copy         | Equals `node_key` in all 1003 records                                                                                                                 |
| `+0x08` | u16       | unknown_08            | Always `0`                                                                                                                                            |
| `+0x0A` | u16       | name_index            | Index into `string_table`; Korean node name (608 distinct)                                                                                            |
| `+0x0C` | u16       | unknown_0c            | Always `0`                                                                                                                                            |
| `+0x0E` | u8        | unknown_0e            | Always `1`                                                                                                                                            |
| `+0x0F` | u8        | unknown_0f            | Always `0`                                                                                                                                            |
| `+0x10` | u8        | has_contribution_cost | `1` exactly when `contribution > 0` (1003/1003); `0` on cities, towns, banks and some sea nodes                                                       |
| `+0x11` | u8        | is_main_alt           | Equals `is_main` except on Ossuary 133, Ossuary 134 and Velia Beach 1898                                                                              |
| `+0x12` | u8        | is_main               | Exact inverse of `is_sub_node` (1003/1003)                                                                                                            |
| `+0x13` | u8        | zone_index            | Sparse (51 nonzero, 48 distinct); meaning unconfirmed                                                                                                 |
| `+0x14` | u8        | zone_category         | Sparse; `1` islands, `2` Valencia nodes, `5` and `6` newer regions; see Open Questions                                                                |
| `+0x15` | u8        | grind_zone            | Sparse (25 nonzero); meaning unconfirmed                                                                                                              |
| `+0x16` | u8        | grind_tier            | `2` on 11 records, `3` on Star's End 1704; meaning unconfirmed                                                                                        |
| `+0x17` | u32       | sub_key               | Unique when nonzero (522 records, all main nodes); `0` on every sub-node                                                                              |
| `+0x1B` | u32       | sub_key_copy          | Equals `sub_key` or is `0` (40 main nodes, e.g. Velia, Heidel, Glish)                                                                                 |
| `+0x1F` | f32       | radius                | Examples `2700.0`, `9700.0`, `12700.0`; `0.0` only on Duvencrune 1651 (client 3464), a second Duvencrune far off the map that the Map view leaves out |
| `+0x23` | f32       | radius_squared        | `radius²` in all records                                                                                                                              |
| `+0x27` | u32       | description_index     | Index into `string_table`; 13 shared Korean descriptions, each maps 1:1 to LOC type 29 `str_id4=1`                                                    |
| `+0x2B` | u16       | manager_family_id     | Character ID (LOC type 6) shared by a main node and its production nodes; `0` on 120 records                                                          |
| `+0x2D` | u16       | representative_id     | Town ruler/representative character ID (LOC type 6); set on 20 town/city records only                                                                 |
| `+0x2F` | u32       | packed_index          | Bit 17 (`0x20000`) set in all records; low 17 bits `0` on 768 records, otherwise mostly unique                                                        |
| `+0x33` | u32       | packed_area           | Low 16 bits always `0`; high 16 bits take 44 distinct values                                                                                          |
| `+0x37` | bytes[39] | unknown_37            | Always `0`                                                                                                                                            |
| `+0x5E` | u8        | contribution          | Contribution-point cost, `0`-`3`                                                                                                                      |
| `+0x5F` | bytes[9]  | unknown_5f            | Always `0`                                                                                                                                            |
| `+0x68` | f32[3]    | position              | Label/exploration anchor; sub-nodes repeat their parent's position                                                                                    |
| `+0x74` | u8        | is_sub_node           | `0` main node (583), `1` sub-node (420)                                                                                                               |

### List (variable: 4 bytes + values)

Seven lists follow the head, each `[u32 count][count × u32]`.

| Offset  | Type       | Field  | Notes               |
| ------- | ---------- | ------ | ------------------- |
| `+0x00` | u32        | count  | Number of values    |
| `+0x04` | u32[count] | values | See the table below |

| List | Observed lengths | Content                                                                         |
| ---- | ---------------- | ------------------------------------------------------------------------------- |
| 0    | 1-3              | Regional grouping hash; 31 distinct values; 1 entry on 997 records               |
| 1-5  | 0-49             | Knowledge entry IDs (LOC `str_type=34`); all 1947 values are `mentalcard.dbss` entries |
| 6    | 0                | Always empty                                                                    |

Lists 2-5 are populated on only 41 records, mostly towns, cities, gates and hubs (for example Velia, Arehaza, Tarif, Heidel, Calpheon).

### Footer (variable: 4 bytes + rows)

| Offset  | Type              | Field | Notes          |
| ------- | ----------------- | ----- | -------------- |
| `+0x00` | u32               | count | Number of rows |
| `+0x04` | Footer Row[count] | rows  | See Footer Row |

### Footer Row (6 bytes)

| Offset  | Type | Field      | Notes                                                               |
| ------- | ---- | ---------- | ------------------------------------------------------------------- |
| `+0x00` | u16  | index      | 111 distinct values in `0`-`1454`; not sorted                       |
| `+0x02` | u16  | node_key   | Always a valid main node key; mostly Dangerous (53) and Normal (49) |
| `+0x04` | u16  | unknown_04 | Always `0`                                                          |

Some nodes appear twice (Castle Ruins 324 with index 21 and 153, Bloody Monastery 325 with 19 and 150).

### String Table (variable: 4 bytes + strings)

Each entry is a `pstr`: the u8 `is_wide` is `1` (UTF-16LE) on every entry but
the empty one (`0`, UTF-8), the u32 is the payload length in bytes with no
terminator, and the payload is Korean text.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Observed `622`      |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## `node_kind` Values

Names come from the client's `CppEnums.ExplorationNodeType` in `global_define_cpp_enum.luac` (member order `eExplorationNodeType_Normal` ... `eExplorationNodeType_Excavation`, then `_Count`=16; the client spells member 1 `Viliage`).

| Value | Enum         | Count | Examples                                           |
| ----- | ------------ | ----- | -------------------------------------------------- |
| 0     | Normal       | 436   | Wale Farm 65, Wolf Hills 66, Racid Island 1008      |
| 1     | Viliage      | 33    | Western Guard Camp 2, Shakatu 1314, Tarif 1141      |
| 2     | City         | 13    | Velia 1, Heidel 301, Calpheon 601, Altinova 1101    |
| 3     | Gate         | 51    | Western Gateway 4, Heidel Pass 6, Mediah Castle 1152 |
| 4     | Farm         | 50    | Potato Farming 131, Cinnamon Farming 1207           |
| 5     | Trade        | 5     | Bartali Farm 21, Alejandro Farm 321, Grándiha 1738  |
| 6     | Collect      | 61    | Gathering sub-nodes                                 |
| 7     | Quarry       | 68    | Mining sub-nodes                                    |
| 8     | Logging      | 64    | Lumbering sub-nodes                                 |
| 9     | Dangerous    | 68    | Cron Castle 3, Goblin Cave 23                       |
| 10    | Finance      | 24    | Investment Bank sub-nodes                           |
| 11    | FishTrap     | 41    | Fish Drying Yard sub-nodes                          |
| 12    | MinorFinance | 2     | Norma Leight 611 and Valentine 612 Investment Banks |
| 13    | MonopolyFarm | 44    | Specialties sub-nodes                               |
| 14    | Craft        | 7     | Chicken Meat Production 132, Honey Production 432   |
| 15    | Excavation   | 36    | Excavation sub-nodes, Chiro's Figurehead Workshop 1736 |

## Manager Families

`manager_family_id` groups 883 records into 494 families. Each family normally has exactly one main node plus its production sub-nodes (Wale 40605: Wale Farm 65, Specialties 109, Olives 204). Exceptions:

| Family                 | Shape                                                                 |
| ---------------------- | --------------------------------------------------------------------- |
| 47608 Jinwan           | Four Farm sub-nodes (1879-1882), no main node                         |
| 47278 Borabae          | Farm/Gathering sub-nodes (1826-1829), no main node                    |
| 40001 Islin Bartali    | Four Normal pseudo nodes (858, 961, 962, 963), all flagged sub-node   |
| 40025 Emma Bartali     | Bartali Farm 21 plus Ossuary 133 and 134 as extra main nodes          |
| 40026 Severo Loggia    | Loggia Farm 26 plus Velia Beach 1898 as an extra main node            |

Two main nodes have `contribution > 0` but no family: Duvencrune 1651 (1 CP, the live city is 1649) and `UnKnown` 1706 (3 CP).

## Notes

- Cross-checked against an independent node dataset (849 nodes, keyed by the same `node_key`): `contribution` matches the node's CP cost on all 849, `is_sub_node` matches on 847, and every node that dataset marks as a city has `node_kind` `1` or `2`. The exceptions are Mining site 156 and Fish Drying Yard 2 (1044), which the file flags as sub-nodes, and Oquilla's Eye 1727, which is kind `City` there but not a city in the dataset.
- The file has no same-stem companion in the current PAZ listing. The handler loads `waypoint_binary/mapdata_realexplore2.bwp` for the Connections columns.
- Counts in this doc are from the pre-2026-09-27 fixture. The 2026-09-27 client has 1080 records: 615 main nodes and 465 sub-nodes (was 583 and 420). Velia (`1`) lists 46 knowledge IDs in both.
- The reference project reports 1037 records, 494 families with 914 nodes and a third CP-without-manager record (2055); the current client file has 1003 records, 494 families with 883 nodes, and no node 2055.
- LOC type 34 also has entries for 987 of the 1003 keys, but they are unrelated knowledge entries (key 65 is `Cron Castle Altar` in type 34, while the inline Korean name `웨일 농장` matches type 29 `Wale Farm`).
- All 45 `planttown.bss` node IDs and all 394 `plantzone.dbss` record IDs are keys in this file; every plant zone is a sub-node.
- The node links are not in this file; they are in [`mapdata_realexplore2.bwp`](waypoint_bwp.md), keyed by the same node keys. There each plant zone has exactly one link, its parent node, which is not always the `manager_family_id` main node: Specialties 1563 links to Arehaza (1380), its family's main node is Areha Palm Forest (1379).
- On client 3458, 1,076 of the 1,080 nodes have links. The four without are Tiamat Sea (2114), Oceanus Sea (2113), Red Battlefield (1378) and Pit of the Undying (1745). Five links go to waypoints with no record here, for example Runn Gateway Intersection (1313) to 1320 and 1323 (`field(shakatu_area)`, `field(atumach)`); they have no LOC type 29 name either. The links match the in-game worldmap for the nodes I checked: Velia links to Bartali, Finto and Loggia Farms, Forest of Plunder, Coastal Cave, the two investment banks, Luivano Island and Velia Beach; Western Guard Camp to Western Gateway, Bandit's Den Byway, Imp Cave and Toscani Farm.
- The record anchor used by older tooling (`node_key` repeated at `+0x06`) still finds the correct 1003 offsets, but the exact layout above makes the scan unnecessary.

## Open Questions

### Sub Key Target

`sub_key` (`+0x17`) is unique per main node and absent on sub-nodes. The reference project calls it a waypoint-space key, but only 80 of the 522 values appear as keys in `mapdata_realexplore2.bwp`, whose keys are node keys. No LOC type covers the values either. Why `sub_key_copy` is zero on 40 main nodes (mostly newer regions plus Velia, Heidel and Glish) is also open.

### Zone Category Labels

The reference project labels `zone_category` as `1` island, `2` coastal, `5` inland/desert and `6` battlefield/ocean. In this file `1` covers 15 islands plus Wolf Hills and Longleaf Tree Sentry Post, `2` covers only Valencia nodes (Ancado Coast, Rakshan Observatory, Valencia Castle), and `5`/`6` cover newer regions (Tungrad Ruins, Atessahra, Great Red Spot). The values look like a content or region class rather than terrain.

### Grind Zone Fields

`zone_index`, `grind_zone` and `grind_tier` are sparse. The reference project describes `grind_zone` as a Marni/Elvia grind-zone index and `grind_tier` as a recommended-AP tier; neither is confirmed by another file. The tier looks doubtful: the 11 nodes with `2` include non-grind places such as Polly's Forest (1624) and Tooth Fairy Forest (1619) next to Gyfin Rhasia Temple (1626) and Desert Naga Temple (1322), and only Star's End (1704) has `3`. `grind_zone` equals `zone_index` on only 6 of its 25 nonzero records.

Open: what the 11 nodes with `grind_tier` `2` share. They are Roud Sulfur
Mine, Ash Forest, Gyfin Rhasia Temple, Polly's Forest, Tooth Fairy Forest,
Mirumok Ruins, Manshaum Forest, Navarn Steppe, Ancado Coast, Pilgrim's
Sanctum: Obedience and Desert Naga Temple; Star's End is the only `3`.

### Packed Index and Area

The `0x20000` flag in `packed_index` is constant, but the low 17 bits are zero on 768 records and non-unique elsewhere, so the reference project's "node enumeration" reading does not hold as stated. Cities carry round values (Velia 1, Heidel 101, Calpheon 301, Valencia City 1201). The target of `packed_area`'s high word (44 values) is not confirmed.

### Footer Index

The footer `index` values and why some nodes appear twice are not mapped to any other table.

### Knowledge List Roles

Lists 1-5 all hold knowledge entry IDs, but what separates list 1 from lists 2-5 (populated on 41 mostly town and hub records) is not confirmed. List 0's hash is not linked to another table.
