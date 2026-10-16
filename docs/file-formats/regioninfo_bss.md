# `regioninfo.bss` Format

## Purpose

Stores every world region: towns, hunting grounds, castles, arenas, caves and sea areas. The primary key is a region key that resolves through LOC `str_type=17` (the region name). Each record also carries the region type, the node war day, the territory and its capital, the region group, the worldmap node the region belongs to, the zone flags (safe zone, sea, desert, prison and others), the region buff skills by day and night, the return point and, for 20 port regions, the Guild Wharf Manager NPC.

The layout follows [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, section 11). I walked it against the client 3458 file: every record tiles exactly up to the string table and every span it calls reserved is zero in all 1594 records. One tail field is split wrongly there (see Region Tail). Field meanings marked confirmed below were checked against LOC, the client's Lua enums and the linked tables; the extractor's other names stay `unknown_*` here.

Most of the zone flags and keys are named from two more sources (see Field Names below): the 2016 client's debug symbols, whose `gc::RegionInfo` lists its members in the order this record stores them, and the server-side `Region_Table` of a private server on client 519, whose columns match these offsets value for value. Five more of the extractor's names turned out wrong that way (`+0x0E`, `+0x10`, `+0x11`, `+0x1B`, `+0x66`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes   | Records                                            | Row bytes |
| ------ | -------------- | ------- | ---------------- | ------- | -------------------------------------------------- | --------- |
| 1      | 3473 and later | 3473    | `regioninfo.bss` | 643,669 | 1,595 Region Head, 1,595 Region Tail, 1,595 Region | 210       |

| Layout | File             | Known             | Unknown           |
| ------ | ---------------- | ----------------- | ----------------- |
| 1      | `regioninfo.bss` | 241,279 B (37.5%) | 402,390 B (62.5%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                       |
| --------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Region names (type 17), territory names (type 12), node names (type 29), NPC names (type 6) |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type                 | Field              | Notes                                                          |
| ------------------- | -------------------- | ------------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]              | magic              | `PABR` (ASCII)                                                 |
| `+0x04`             | u32                  | record_count       | Observed `1594` (client 3458; the extractor documents `1572`)  |
| `+0x08`             | Region[record_count] | records            | Variable records packed back-to-back with no alignment; see Region |
| `records+0x00`      | String Table         | string_table       | Korean strings (shared `pabr_strings` layout); see String Table |
| `string_table+0x00` | u32                  | string_table_start | Absolute file offset of `string_table.count`; observed `623714` |
| `string_table+0x04` | u32                  | zero               | Observed `0`                                                   |

A record is a 210-byte head, two counted lists and a 171-byte tail, so its size is `389 + 2 * key_count + 12 * vector_count`. The walk ends exactly at `string_table_start`; the parser raises an error when it does not.

### Region (variable: 389 bytes + key and vector lists)

| Offset                    | Type                     | Field              | Notes |
| ------------------------- | ------------------------ | ------------------ | ----- |
| `+0x00`                   | Region Head              | head               | See Region Head |
| `+0xD2`                   | u32                      | key_count          | |
| `+0xD6`                   | u16[key_count]           | unknown_d2_keys    | Region keys; set on 58 town regions and always includes the region itself. Extractor: warehouse group. Velia's list holds the mainland towns from Velia to Muzgar; Hakinza Sanctuary's holds Altinova, Asparkan, Shakatu, Sand Grain Bazaar, Muzgar, Velandir, Aal's Revelation and Angavu Outpost |
| `unknown_d2_keys+0x00`    | u32                      | vector_count       | |
| `unknown_d2_keys+0x04`    | f32[vector_count][3]     | unknown_d2_vectors | World positions; only The Great Desert of Valencia (region 230) has any (3) |
| `unknown_d2_vectors+0x00` | Region Tail              | tail               | See Region Tail |

### Region Head (210 bytes)

Offsets are hex; the extractor's decimal offset is in the notes where it named the field.

| Offset  | Type      | Field              | Notes |
| ------- | --------- | ------------------ | ----- |
| `+0x00` | u16       | region_key         | LOC `str_type=17`, `str_id1=region_key`; unique; all 1594 resolve |
| `+0x02` | u8[3]     | color              | Region colour stored blue, green, red; the parser returns `rrggbb` (Velia `820000`). `edaniaregioninfo.bss` stores the same value for the five first-group Edania castles |
| `+0x05` | u8        | color_alpha        | Always `0`; the alpha byte of `color`, which the 2016 PDB types as a 4-byte `pa::Color` (`_colorKey`) |
| `+0x06` | u8        | region_type        | `CppEnums.RegionType`; see Enum Values |
| `+0x07` | u8        | node_war_day       | `CppEnums.VillageSiegeType`, Sunday `0` to Saturday `6`; `7` (the enum's `_Count`) for no node war |
| `+0x08` | bytes[3]  | unknown_08         | Always `0` |
| `+0x0B` | u8        | unknown_0b         | Values `0`, `1`, `3`, `4`; `3` on Velia, Heidel, Altinova and Valencia City, `4` on the Margoria islands |
| `+0x0C` | u8        | is_safe_zone       | Set on 318 regions, among them Velia, Glish, Ossuary, Heidel Castle and Lake Flondor |
| `+0x0D` | u8        | is_arena_zone      | Set on the 9 arena regions. Named from the 2016 member order (`_isArenaZone` between `_isSafeZone` and `_isSea`); the client Lua reads `isArenaZone` |
| `+0x0E` | u8        | is_sea             | Set on 199 regions, mostly islands and sea. The extractor calls it `ocean` |
| `+0x0F` | u8        | is_desert          | Set on 43 regions, all in Valencia (territory 4): the Great Desert, the sand dunes, Pilgrim's Sanctums, Cantusa, Aakman |
| `+0x10` | u8        | is_not_dig         | Set on 8 desert regions: Aakman Temple, Scarlet Sand Chamber, Ibellab Oasis, Hystria Ruins, Roud Sulfur Mine, Pila Ku Jail, Muiquun, Jail. The extractor calls it `prison`. Likely turns off Shabby Shovel digging, see Notes |
| `+0x11` | u8        | is_ocean           | Set on 62 regions: Sea, Margoria, Oquilla's Eye, Crow Merchants' Vessel. The extractor calls it `sea`; the client Lua has `isOceanZone` next to the sea checks |
| `+0x12` | u8        | is_prison          | Set on Jail (697) only |
| `+0x13` | u8        | unknown_13         | Several mirror `region_type` (`0x13` = Siege or CastleInSiege, `0x14` = Fortress, `0x18` = MainTown, `0x19` = MinorTown, `0x1A` = either town); see Open Questions |
| `+0x14` | u8        | unknown_14         | Mirrors `region_type` Fortress; see `unknown_13` |
| `+0x15` | u8        | unknown_15         | See `unknown_13` |
| `+0x16` | u8        | unknown_16         | See `unknown_13` |
| `+0x17` | u8        | unknown_17         | See `unknown_13` |
| `+0x18` | u8        | unknown_18         | Mirrors `region_type` MainTown; see `unknown_13` |
| `+0x19` | u8        | unknown_19         | Mirrors `region_type` MinorTown; see `unknown_13` |
| `+0x1A` | u8        | unknown_1a         | Set on either town type; see `unknown_13` |
| `+0x1B` | u8        | is_accessible_area | Set on 1514 regions. The extractor calls it `locator`; the client Lua reads `isAccessibleArea` |
| `+0x1C` | u8        | is_node_access     | Set on 118 regions |
| `+0x1D` | u16       | unknown_1d         | |
| `+0x1F` | u8        | unknown_1f         | Set on 54 regions (Rameda Island, Altar of Agris, Western Guard Camp) |
| `+0x20` | u32       | unknown_20         | `22950` in every record (the extractor saw `19950`), so it changes between patches |
| `+0x24` | u8        | unknown_24         | Always `0` |
| `+0x25` | u8        | is_locator         | |
| `+0x26` | u32       | villain_respawn_node_key | Exploration node key where an outlaw respawns. Set on 204 records, all exploration node keys (Muiquun for several desert regions) |
| `+0x2A` | f32[3]    | villain_respawn_position | The position paired with `villain_respawn_node_key`. Named from the 2016 member order (`_villainRespawnPosition` follows the key); no server column to check it against |
| `+0x36` | u8        | is_ancient_dungeon | Set on Aakman Temple (688) and Hystria Ruins (689) |
| `+0x37` | u8        | is_escape          | Set on most regions; clear on Atoraxion, the arenas and battlefields, Oquilla's Eye, Kamasylvia, Duvencrune, Muiquun and a few caves |
| `+0x38` | u8        | is_special_zone    | Set on Atoraxion, the arenas and battlefields, Sea Palace, Mountain of Eternal Winter, Pit of the Undying, Aakman Temple, Hystria Ruins, Ruins of Tzol |
| `+0x39` | u8        | is_vehicle_dead_zone | Set only on `is_special_zone` regions |
| `+0x3A` | u8        | unknown_3a         | |
| `+0x3B` | u8        | unknown_3b         | Always `0` |
| `+0x3C` | u16       | skill_no           | Region buff skill by day; see Notes |
| `+0x3E` | u32       | skill_apply_rate   | Apply rate of `skill_no` |
| `+0x42` | u8        | unknown_42         | |
| `+0x43` | u8        | unknown_43         | Always `0` |
| `+0x44` | u16       | skill_no_2         | A second region skill; set on the Margoria regions only |
| `+0x46` | u32       | skill_apply_rate_2 | Apply rate of `skill_no_2` |
| `+0x4A` | bytes[8]  | unknown_4a         | Always `0` |
| `+0x52` | u8        | unknown_52         | |
| `+0x53` | u8        | unknown_53         | Always `0` |
| `+0x54` | u16       | night_skill_no     | Region buff skill at night; see Notes |
| `+0x56` | u32       | night_skill_apply_rate | Apply rate of `night_skill_no` |
| `+0x5A` | u8        | territory_key      | Territory 0 to 13; LOC `str_type=12`, `str_id4=1` names it (Balenos, Serendia ... Inner Edania). The key of `territoryinfo.bss` |
| `+0x5B` | u8        | unknown_5b         | Always `0` |
| `+0x5C` | u32       | name_index         | Index into `string_table`; the region's Korean name (`벨리아 마을` for Velia) |
| `+0x60` | u32       | return_position_name | Index into `string_table`; the Korean name of the region's return point, see Notes. The extractor calls it the capital's name, which it is not |
| `+0x64` | u16       | capital_region_key | Region key of the territory capital: the same in every region of a territory and always that territory's `MainTown` (Velia, Heidel, Calpheon City ... Angavu Outpost) |
| `+0x66` | u16       | trade_origin_region_key | A region key: the trade origin (`getTradeOriginRegion` in the client Lua). The extractor calls it the affiliated town. Often the region itself or a nearby town, but also non-town regions (Evergart Falls points to 417) |
| `+0x68` | u16       | region_group_key   | Key of `regiongroupinfo.bss`: the file has 250 records and this field 250 distinct values (`0` on 32 regions) |
| `+0x6A` | u8        | unknown_6a         | Always `0` |
| `+0x6B` | u16       | waypoint_key       | Non-zero on 628 records; equals `node_key` on 873 (zero included) |
| `+0x6D` | bytes[2]  | unknown_6d         | Always `0` |
| `+0x6F` | u16       | node_key           | `exploration.bss` node key; non-zero on 1331 records and every one is a node. The node that covers the region (Lumbering 1 -> Trent) |
| `+0x71` | bytes[2]  | unknown_71         | Always `0` |
| `+0x73` | u8        | region_attribute_type | `1` on Velia (5) and Velia Beach (444), `0` elsewhere (client 3464) |
| `+0x74` | bytes[3]  | unknown_74         | Always `0` |
| `+0x77` | f32[3]    | unknown_77         | Extractor: waypoint position. Zero on 1580 records |
| `+0x83` | f32[3]    | return_position    | The return point's world position, shared by many regions; pairs with `return_position_name`, see Notes. The extractor calls it the region position, which it is not |
| `+0x8F` | bytes[4]  | unknown_8f         | Always `0` |
| `+0x93` | u8        | exploration_point  | `1` except on Velia (1), Sea (2), Deep Sea (175) and Valencia City (229) (client 3464) |
| `+0x94` | u8        | unknown_94         | Always `0` |
| `+0x95` | u32       | unknown_95         | |
| `+0x99` | f32[5]    | unknown_99         | Velia: `45, 38, 0, 55, 0.6` |
| `+0xAD` | u32       | unknown_ad         | |
| `+0xB1` | u32       | unknown_b1         | |
| `+0xB5` | u32       | unknown_b5         | `0xFFFFFFFF` in every record |
| `+0xB9` | u32[6]    | unknown_b9         | Set mainly on towns; Velia `105580, 105554, 105551, 105607, 105547, 105580` |
| `+0xD1` | u8        | is_free_revival_area | The client Lua reads `isFreeRevivalArea` |

### Region Tail (171 bytes)

Offsets are relative to the start of the tail. The parser keeps every field that is not zero in all records; the unconfirmed ones are `unknown_tail_<offset>`, kept on the record for search and CSV export but not shown in the table.

I walked the extractor's tail list (`unknownTail1` to `unknownTail162`, 46 values once its arrays are counted out) against client 3458. Its reserved spans at tail `+0x00`, `+0x50`, `+0x8A` (7 bytes), `+0x92` (8 bytes) and `+0xA6` (3 bytes) are zero in every record, and five of its fields are too (`+0x16`, `+0x31`, `+0x41`, `+0x87`, `+0x9E`), so they are listed as reserved here. One split is wrong: the extractor reads `+0x4D` as a u16, a u8 (`unknownTail79`, which looks like a tier 1 to 4 or 15) and a reserved byte, but the four bytes are one u32 (`70000`, `140000`, `220000`, `280000`, `1000000`); the "tier" byte is just its third byte.

`FLT_MAX` and `0x7FFFFFFF` mean "no value" in several fields below. They are set on every region except a group of 67: the 63 node war regions (`node_war_day` 0 to 6) and the territory capitals Velia, Heidel, Altinova and Valencia City. I call this group the siege regions below.

| Offset  | Type      | Field                   | Notes |
| ------- | --------- | ----------------------- | ----- |
| `+0x00` | u8        | unknown_tail_00         | Always `0` |
| `+0x01` | u16       | unknown_tail_01         | `0xFFFF` in every record |
| `+0x03` | u16       | max_participants        | Node war participant cap: `0` except on the siege regions, `30` to `80` on node war regions, `100` on the four capitals. Matches the published per-node participant table on all 24 Calpheon, Ulukita, Valencia and Edania nodes; the game can override it (City of the Dead: `35` here and in that table, `40` in its tooltip) |
| `+0x05` | f32       | siege_ap_limit          | Node war AP limit; `FLT_MAX` (no limit) except on the siege regions. See Notes for the five sets |
| `+0x09` | f32       | siege_dr_limit          | Node war damage reduction (DP) limit |
| `+0x0D` | f32       | siege_evasion_limit     | Node war evasion limit |
| `+0x11` | u32       | unknown_tail_11         | `0x7FFFFFFF` except on the siege regions: `150000`, `200000` or `1000000`, `0` on Velia and Heidel. The accuracy rate or the evasion rate limit; always equal to `unknown_tail_55`, so which is which is open |
| `+0x15` | u8        | unknown_tail_15         | `3` on the 63 node war regions, `5` elsewhere. Possibly the max war heroes, which the node tooltip shows as 3 |
| `+0x16` | u8        | unknown_tail_16         | Always `0` |
| `+0x17` | u8        | unknown_tail_17         | `3` in every record |
| `+0x18` | u8        | is_world_boss_reward    | Set on Margoria (Vell's Realm) (871) only |
| `+0x19` | f32[6]    | unknown_tail_19         | Two world positions, set on 117 regions; on 84 both are the same point, on 31 the second is zero (Pit of the Undying among them), on 2 they differ |
| `+0x31` | u64       | unknown_tail_31         | Always `0` |
| `+0x39` | f32       | unknown_tail_39         | `FLT_MAX`, or on the siege regions the same value as `siege_ap_limit` |
| `+0x3D` | f32       | unknown_tail_3d         | `FLT_MAX`, or `100000000` on the siege regions |
| `+0x41` | u32       | unknown_tail_41         | Always `0` |
| `+0x45` | u8        | unknown_tail_45         | Set on exactly the region type 7 records (Pit of the Undying 950 and 1070) |
| `+0x46` | u8        | unknown_tail_46         | Set on exactly the region type 8 record (Battle Arena 1072) |
| `+0x47` | u32       | unknown_tail_47         | `10011` on the 63 node war regions, `0` elsewhere |
| `+0x4B` | u16       | unknown_tail_4b         | `0xFFFF` except on the 40 Atoraxion regions: `151` on Vaha's areas, `153` on Syca's, `155` on Yolu's, `157` on Orze's; two dungeon regions break the pattern (Sycrakea `151`, Orzekea `153`) |
| `+0x4D` | u32       | siege_dr_rate_limit     | Node war damage reduction rate limit, `1000000` = 100%. `658` on every other region |
| `+0x51` | f32       | siege_accuracy_limit    | Node war accuracy limit |
| `+0x55` | u32       | unknown_tail_55         | The other one of the accuracy rate and evasion rate limits, see `unknown_tail_11` |
| `+0x59` | u32[4]    | siege_resistance_limits | Node war resistance limits, `1000000` = 100%; the four values are equal in every record (likely stun, grapple, knockdown and knockback, order unconfirmed) |
| `+0x69` | u32       | unknown_tail_69         | `0x7FFFFFFF`, or `0` on the siege regions |
| `+0x6D` | u8        | unknown_tail_6d         | Set on 7 separated PvP areas: both Battle Arenas of type 6 (436, 437), Battle Arena 1072, Arena of Arsha, Battlefield of Honor, The Red Battlefield, Undiscovered Area (435) |
| `+0x6E` | f32[3]    | unknown_tail_6e         | A world position on 49 instance regions: all Atoraxion regions point to Velia's `(-1226, -7012, 81647)`, the Oquilla's Eye regions and the Land of the Morning Light houses to their own town |
| `+0x7A` | f32[3]    | unknown_tail_7a         | A distinct world position on 36 node war regions, Altinova and Valencia City |
| `+0x86` | u8        | unknown_tail_86         | On the siege regions only: `100` on the capitals; on node war regions `0`, `5` or `15` |
| `+0x87` | u8        | unknown_tail_87         | Always `0` |
| `+0x88` | u8        | unknown_tail_88         | Set on the 63 node war regions |
| `+0x89` | u8        | unknown_tail_89         | `10` on the 63 node war regions |
| `+0x8A` | bytes[7]  | unknown_tail_8a         | Always `0` |
| `+0x91` | u8        | unknown_tail_91         | `49` on the 63 node war regions |
| `+0x92` | bytes[8]  | unknown_tail_92         | Always `0` |
| `+0x9A` | u32       | unknown_tail_9a         | On the siege regions only; node war regions `15625000` to `39062500`, the capitals `117187500` to `234375000`. Multiples of `1953125` (`10^9 / 512`) |
| `+0x9E` | u32       | unknown_tail_9e         | Always `0` |
| `+0xA2` | u32       | unknown_tail_a2         | On the siege regions only; always `unknown_tail_9a + 7812500` on node war regions, `+39062500` on the capitals |
| `+0xA6` | bytes[3]  | unknown_tail_a6         | Always `0` |
| `+0xA9` | u16       | guild_wharf_manager_key | NPC character key; set on 20 regions and every NPC is titled `<Guild Wharf Manager>` in LOC (Robert in Velia, Sebastian in Port Epheria, Elro in Oquilla's Eye) |


### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | Observed `1108` entries |
| `+0x04` | pstr[string_count] | strings      | Korean strings |

## Field Names

Two sources name most of the head fields:

- The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::RegionInfo` lists the members `_regionKey`, `_colorKey`, `_regionType`, `_isSafeZone`, `_isArenaZone`, `_isSea`, `_isDesert`, `_isPrison`, seven town and war flags, `_accessibleArea`, `_villageTaxLevel`, `_dropGroupRerollCountOfSieger`, `_isLocator`, `_villainRespawnExploreKey`, `_villainRespawnPosition`, `_isAncientDungeon`, `_isEscape`, the day and night region skills, `_territoryKey`, `_areaName`, `_returnRegionName`, `_tradeOriginRegionKey`, `_regionGroupKey`, `_waypointKey`, `_exploreKey`, `_regionAttributeType`, `_returnPosition`, `_explorationPoint` ... `_isFreeRevivalArea` in this order. Today's record stores them in the same order without padding or pointers, with newer fields in between. Its loader, `GameCommonParameterLoaderFromExcel::LoadRegionInformation`, reads them from the columns of `Region_Table`.
- A private server on client 519 ships the developers' `Region_Table` with its original column names and values. I matched every column against every head and tail offset over the 896 region keys it shares with the client file.

Matches on client 3464 (896 shared region keys). The mismatches are regions changed since 2021:

| Offset      | Field                     | `Region_Table` column      | Matching regions |
| ----------- | ------------------------- | -------------------------- | ---------------- |
| `+0x02`     | color                     | `B`, `G`, `R`              | 895              |
| `+0x0C`     | is_safe_zone              | `IsSafe`                   | 889              |
| `+0x0E`     | is_sea                    | `IsSea`                    | 893              |
| `+0x0F`     | is_desert                 | `IsDesert`                 | 896              |
| `+0x10`     | is_not_dig                | `IsNotDig`                 | 896              |
| `+0x11`     | is_ocean                  | `IsOcean`                  | 895              |
| `+0x12`     | is_prison                 | `IsPrison`                 | 896              |
| `+0x1B`     | is_accessible_area        | `AccessibleArea`           | 867              |
| `+0x1C`     | is_node_access            | `isNodeAccess`             | 891              |
| `+0x25`     | is_locator                | `Locator`                  | 894              |
| `+0x26`     | villain_respawn_node_key  | `VillainRespawnExploreKey` | 822              |
| `+0x36`     | is_ancient_dungeon        | `IsAncientDungeon`         | 896              |
| `+0x37`     | is_escape                 | `Isescape`                 | 895              |
| `+0x38`     | is_special_zone           | `IsSpecialZone`            | 896              |
| `+0x39`     | is_vehicle_dead_zone      | `VehicleDeadZone`          | 896              |
| `+0x3C`     | skill_no                  | `SkillNo`                  | 896              |
| `+0x3E`     | skill_apply_rate          | `SkillApplyRate`           | 896              |
| `+0x44`     | skill_no_2                | `SkillNo2`                 | 896              |
| `+0x46`     | skill_apply_rate_2        | `SkillApplyRate2`          | 896              |
| `+0x54`     | night_skill_no            | `NightSkillNo`             | 896              |
| `+0x56`     | night_skill_apply_rate    | `NightSkillApplyRate`      | 896              |
| `+0x5A`     | territory_key             | `TerritoryKey`             | 886              |
| `+0x5C`     | name_index                | `AreaName`                 | 838              |
| `+0x60`     | return_position_name      | `ReturnPositionName`       | 752              |
| `+0x66`     | trade_origin_region_key   | `TradeOriginRegion`        | 868              |
| `+0x68`     | region_group_key          | `RegionGroupKey`           | 890              |
| `+0x6B`     | waypoint_key              | `WaypointKey`              | 890              |
| `+0x6F`     | node_key                  | `ExploreKey`               | 889              |
| `+0x73`     | region_attribute_type     | `RegionAttributeType`      | 896              |
| `+0x83`     | return_position           | `ReturnPositionX`, `Y`     | 838              |
| `+0x93`     | exploration_point         | `ExplorationPoint`         | 896              |
| `+0xD1`     | is_free_revival_area      | `FreeRevivalArea`          | 884              |
| tail `+0x18`| is_world_boss_reward      | `WorldBossReward`          | 896              |

`villain_respawn_node_key` matches less often because the node keys were renumbered: the server's `1001` is `1727` here. The server's `ReturnPositionZ` column holds place-name text, so only X and Y were compared. Columns with no match in this file: the music columns (`BankNo_*`, `MusicIdx_*`), `Temperature`, `Humility`, `WindDir`, `OilRate`, `WaterRate` (constant on the server), `VillageTaxLevel`, `IsChallengeSiege`, `LimitMemberAtSiege`, `MonsterGroupForTotem` and the node war day (`VillageSiegeType`, changed since 2021; `node_war_day` stays on the client Lua enum).

`is_arena_zone` (`+0x0D`) and `villain_respawn_position` (`+0x2A`) have no column; they are named from their place in the 2016 member order between two matched fields.

## Enum Values

### `region_type` (`CppEnums.RegionType`)

Names from `global_define_cpp_enum.luac`, without the `eRegionType_` prefix. The enum ends with `_Count` = 7, but the file also uses 7 and 8; no client Lua names them, so the table shows the number (see Open Questions).

| ID  | Name          | Records | Examples |
| --- | ------------- | ------- | -------- |
| 0   | MinorTown     | 45      | Glish, Olvia, Keplan, Port Epheria, Western Guard Camp |
| 1   | MainTown      | 14      | The territory capitals: Velia, Heidel, Calpheon City ... Angavu Outpost |
| 2   | Hunting       | 1489    | Every field region |
| 3   | Siege         | 14      | Calpheon Castle Site, Lake Kaia, Mediah Shore, Treant Forest |
| 4   | Fortress      | 8       | Balenos Forest, Southern Neutral Zone, Naga Marsh |
| 5   | CastleInSiege | 13      | Calpheon Castle, Mediah Castle, Kamasylvia Castle, Duvencrune |
| 6   | Arena         | 8       | Velia Duel Arena, Battle Arena, Valencia Arena |
| 7   | (not in enum) | 2       | Pit of the Undying (950, 1070); `unknown_tail_45` is set on exactly these |
| 8   | (not in enum) | 1       | Battle Arena (1072); `unknown_tail_46` is set on exactly this one |

### `node_war_day` (`CppEnums.VillageSiegeType`)

`0` Sunday, `1` Monday, `2` Tuesday, `3` Wednesday, `4` Thursday, `5` Friday, `6` Saturday, `7` none. Client 3458 has 6 regions on each day from Sunday to Thursday, 33 on Friday (most of them Margoria islands) and none on Saturday, the conquest war day.

## Notes

- **LOC type 17 is the region name.** All 1594 region keys resolve in LOC type 17, which has 1658 IDs; the other 64 (750, 807 to 809, 821, 1177, 1178, 1417 ...) have no region in this client and look like retired regions. The `plantworkerselect.bss` selection IDs are region keys too: all 31 are towns of type `MainTown` or `MinorTown`. So both readings hold: type 17 names regions, and the worker-selection towns are regions; the `buff.dbss` town keys name towns through the same type. [`languagedata_loc.md`](languagedata_loc.md) says so.
- **`region_info.xml`** (`gamecommondata/`) keys its boxes by the same region key: `<box region_index=...>` matches `region_key`, and every one of its 183 region keys exists here. It is not a box per region: it holds 721 boxes (AABB plus an oriented box, `fieldNo="1"` on all) for 183 regions, nearly all caves, interiors and other small enclosed regions (Ossuary, Coastal Cave, Imp Cave, Secret Cave, Basement Cellar). Each box has a `property_index` into a 187-entry `propertyArray` of `WeatherTable`/`WeatherTime` values, and a `binArray` of 10626 grid cells indexes the boxes spatially. The `return_position` falls inside the region's own boxes for only 18 of the 183, so it is not the region position.
- **The return point.** `return_position_name` and `return_position` are `Region_Table`'s `ReturnPositionName` and `ReturnPositionX/Y/Z` (`_returnRegionName` and `_returnPosition` in the 2016 client). Grouping the records by the position gives 230 groups, and 214 of them share a single name: 90 regions point to `벨리아 마을` (Velia) at `(-1226, -7012, 81647)`, 107 to `하킨자 성전` (Hakinza Sanctuary), 81 to `알티노바` (Altinova). The name is often the territory capital or the `trade_origin_region_key` region, but matches neither consistently (463 and 470 of 1594, client 3458).
- The node war regions are field regions plus a few castles and towns: each day from Sunday to Thursday lists one region from each of six territories, for example Sunday holds Forest of Plunder, Orc Camp, Quint Hill, Valencia Castle, Neruda Plain and Neftak Outpost.
- Several flag bytes repeat `region_type` (see `unknown_13` .. `unknown_1a`), so they may be the client's per-type properties expanded into the record. The tail does the same for the two types past the enum: `unknown_tail_45` marks type 7 and `unknown_tail_46` type 8.
- **Region buff skills.** `skill_no` applies by day and `night_skill_no` at night, each with its apply rate. On client 3464 the set records are: the Valencia desert regions with `40338` Debuff Desert Morning (rate `50000`) by day and `40339` Debuff Desert Evening (`45000`) at night; Mountain of Eternal Winter with `41517` (no LOC skill name) by day and `40339` at night; the Margoria regions and the Crow Merchants' Vessel with `40434` Summon Phantom Ship by day and night, plus `40452` Summon Margoria Grim Reaper in `skill_no_2`. The scale of the apply rates is not known.
- **`is_not_dig` and the Shabby Shovel.** The Shabby Shovel (item `16139`, sold by the Valencia material vendors) says "You can dig the sand with this in the desert" and yields a Bag of Muddy Water (`6657`). Every `is_not_dig` region also has `is_desert` set, and all eight are enclosed or special spots inside the desert (temples, ruins, a mine, two jails, the Ibellab Oasis, Muiquun). So the flag likely turns off shovel digging where `is_desert` would allow it. Neither the client Lua nor the server code reads it, so this rests on the region list; see In-Game Checks.
- **The siege block in the tail.** `max_participants`, the `siege_*` limits and `unknown_tail_11`, `_39`, `_3d`, `_55`, `_86`, `_9a` and `_a2` are filled only on the 63 node war regions and the four capitals Velia, Heidel, Altinova and Valencia City; every other region carries `FLT_MAX`, `0x7FFFFFFF` or `0` there, and `+0x4D` holds `658`; the parser leaves every `siege_*` limit `None` where `max_participants` is 0. The client reads the same limits per region through `ToClient_getLimitSiegeDDByRegionKey`, `...HitByRegionKey`, `...DVByRegionKey`, `...PVByRegionKey`, `...DVRateByRegionKey`, `...HitRateByRegionKey` and `...StunResistByRegionKey` (`panel_worldmap_nodetooltip_villagewar_all_1.luac`, `new_worldmap_territorytooltip.luac`), and the participant cap through `getMaxMemberAtSiege`.
- **How the limit fields were mapped.** The node war regions use five fixed limit sets:

  | AP   | DR   | Evasion | Accuracy | DR rate | Acc. / eva. rate | Resistance |
  | ---- | ---- | ------- | -------- | ------- | ---------------- | ---------- |
  | 245  | 223  | 741     | 645      | 7%      | 15% / 15%        | 20%        |
  | 362  | 327  | 847     | 715      | 14%     | 15% / 15%        | 30%        |
  | 485  | 365  | 913     | 781      | 22%     | 20% / 20%        | 50%        |
  | 540  | 407  | 966     | 824      | 28%     | 100% / 100%      | 100%       |
  | 9999 | 9999 | 9999    | 9999     | 100%    | 100% / 100%      | 100%       |

  Black Desert Foundry's node war guide lists the old Tier 1 Beginner limits as AP 245, damage reduction 223, accuracy 645, evasion 741, damage reduction rate 7%, accuracy and evasion rate 15% and resistance 20%: the first set, field for field. Its Tier 1 Intermediate rates (14%, 15%, 15%, 30%) match the second set, whose flat values have been raised since. The `9999` set is the uncapped one. Velia (`560 / 410 / 768 / 680`) and Heidel (`680 / 530 / 908 / 820`) have their own. The sets no longer follow today's node tiers (Hexe Sanctuary and Longleaf Tree Sentry Post are both Tier 4 but use the 485 and 362 sets), and neither the tier nor the 550 / 720 gear score limit of the construction mode node wars is stored in this file.
- **The capital records hold the live limits.** In game, Trina Fort (Calpheon) and City of the Dead (Ulukita) both show AP limit 680, damage reduction 530, evasion 908, accuracy 820 and damage reduction rate 30%: exactly Heidel's record, not their own `9999` and `540` sets. So the four capital records look like the limit sets per territory pair of the construction mode node wars: Heidel for Calpheon and Ulukita (gear score limit 720, confirmed by both nodes), Altinova and Valencia City (`9999`, uncapped) for Valencia and Edania (no gear score limit, consistent but not checked in game), Velia (`560` set) unconfirmed. The per-node sets in the table above look like leftovers from the older tier system. Both tooltips also show an HP limit of 11,000, which this file has no field for.
- **Occupation mode overrides these values.** Balenos and Serendia run their node wars in occupation mode, and there the in-game node tooltip ignores this file: Castle Ruins, Glish Swamp, Orc Camp and Wolf Hills all show AP limit 395, evasion 738, damage reduction 335, damage reduction rate 20%, accuracy 650, 25 max participants and 3 max war heroes, while this file gives them four different limit sets and 55, 45, 65 and 80 participants. None of the extracted client tables holds 395 / 335 / 738 / 650, so the occupation mode limits are likely server-side. The tooltip also lists limits this file has no field for (critical hit rate and damage, back / down / air attack damage at 20%, HP 6,500, HP recovery 5, Black Spirit's Rage 100% and its recovery 0.15%, stamina 2,100).
- `unknown_tail_86` (`0`, `5`, `15`) follows the territory pairs of the construction mode node wars on the land nodes: `0` on Balenos and Serendia (gear score limit 550), `5` on Calpheon and Ulukita (720), `15` on Valencia and Edania (no limit). The island nodes carry `0` in every territory.
- `unknown_tail_9a` and `unknown_tail_a2` hold silver-sized amounts on the siege regions (node war regions `15.6M` to `46.9M`, capitals up to `273.4M`), always a fixed step apart; they may be the node war participation fee or reward, but nothing in the client names them.
- Related files out of scope here: `regionclientdata.xml` and its per-service variants (`regionclientdata_<code>_.xml`) place NPCs and monsters per region and key them by `<RegionInfo Key=...>`, the same region key.
- [`regioninfo_linkandcheckvalid2.bss`](regioninfo_linkandcheckvalid2_bss.md) stores `unknown_d2_keys` again, one record per region; its lists equal this file's in every record of client 3458, and the links are mutual (when A lists B, B lists A).

## Open Questions

### Where the live node war values come from

Several values the node tooltip shows are not in this file, or differ from it:

- **Occupation mode limits.** The Balenos and Serendia nodes show one shared set (AP 395, evasion 738, damage reduction 335, accuracy 650, 25 participants) that is not in this file (see Notes).
- **Participant cap.** City of the Dead shows 40 max participants in game, while `max_participants` and the published construction mode table both say 35. Something overrides the cap per node.
- **Limits with no field here.** HP (6,500 in occupation mode, 11,000 on Calpheon and Ulukita nodes), HP recovery, critical hit rate and damage, back / down / air attack damage, Black Spirit's Rage and its recovery, and stamina.

None of these values turns up in the extracted client tables. If a client table holds them, it is one I have not extracted yet; otherwise the server sends them.

### Max war heroes

Every node tooltip shows 3 max war heroes. `unknown_tail_15` is `3` on every node war region and `5` elsewhere, which makes it the only candidate, but a node with a different hero count is needed to confirm it.

### Accuracy rate or evasion rate

`unknown_tail_11` and `unknown_tail_55` are the accuracy rate and evasion rate limits, but they hold the same value in every set, so which offset is which cannot be told from the data. A patch that gives the two different values, checked against a node tooltip, would settle it.

### Other tail fields

`unknown_tail_47` (`10011`), `unknown_tail_89` (`10`) and `unknown_tail_91` (`49`) are constant across the node war regions; `unknown_tail_86` (`0`, `5`, `15`) follows the territory pairs (see Notes) and `unknown_tail_9a` / `unknown_tail_a2` (silver-sized amounts) vary by node. `unknown_tail_39` repeats `siege_ap_limit` and `unknown_tail_3d` is `100000000` on every siege region; both may be limits the current node wars do not use. `unknown_tail_4b` groups the Atoraxion regions, `unknown_tail_6d` the separated PvP areas, `unknown_tail_6e` points instance regions to a town (all of Atoraxion to Velia), and `unknown_tail_19` / `unknown_tail_7a` are world positions. None of these has a name in the client yet.

### Meaning of `unknown_d2_keys`

The list holds town region keys and includes the owning region; the extractor calls it a warehouse group. Velia's list covers the mainland towns but not Valencia City or Shakatu. It is not the transport network: in game, Velia's transport window sends to Valencia City (and every other town with a storage), though Valencia City is not in Velia's list. The same question is open for [`regioninfo_linkandcheckvalid2.bss`](regioninfo_linkandcheckvalid2_bss.md).

### Town and War Flags

`unknown_13` .. `unknown_1a` have no `Region_Table` column. The 2016 `gc::RegionInfo` has seven computed flags at this place: `_isKingWarZoneOnly`, `_isLordWarZoneOnly`, `_isVillageWarZone`, `_isKingOrLordWarZone`, `_isMainTown`, `_isMinorTown` and `_isMainOrMinorTown`. That fits what the bytes hold (`0x13` on Siege and CastleInSiege, `0x14` on Fortress, `0x18` to `0x1A` on the towns), but this file has eight bytes for the seven, so which one is new is open. The client Lua reads `isVillageWarZone` and `isKingOrLordWarZone`.

### Remaining Unknown Head Fields

`unknown_0b`, `unknown_1d`, `unknown_1f`, `unknown_20`, `unknown_3a`, `unknown_42`, `unknown_52`, `unknown_77`, `unknown_95`, `unknown_99`, `unknown_ad`, `unknown_b1`, `unknown_b5` and `unknown_b9` match no `Region_Table` column. `unknown_0b` (`3` on the capitals) does not match `VillageTaxLevel` either.

## In-Game Checks

### Shabby Shovel in a No-Dig Region

This checks whether `is_not_dig` turns off desert digging.

1. Buy a Shabby Shovel from a material vendor in Valencia.
2. Use it in the open desert, for example in the Great Desert of Valencia. Note that you get a Bag of Muddy Water.
3. Go to Ibellab Oasis or Roud Sulfur Mine (both have `is_not_dig` set) and use it again.

Expected result: the shovel works in step 2 and is refused or yields nothing in step 3. If it works in step 3 too, the flag does something else.

### Region Types 7 and 8

Needs zone (all):

- Pit of the Undying (`950` or `1070`, type 7)
- Battle Arena (`1072`, type 8)

`CppEnums.RegionType` ends at Arena (6) with `_Count` = 7, but Pit of the Undying (950, 1070) has type 7 and one Battle Arena (1072) type 8. I searched all 3060 client Lua scripts: no `eRegionType_` value past Arena exists, and the only scripts that touch region types compare against `Siege`, `Fortress` and `MinorTown`.

What the client does have are region getters that fit the two types: `isPVEArenaZone` (used by the death message, game exit, manufacture and Morning Land boss panels) next to `isArenaZone` and `isArenaArea`. Pit of the Undying is a PvE arena, so type 7 is probably a PvE arena. `is_arena_zone` is set on every type 6 arena and on 1072, not on Pit of the Undying. Type 8 is a third Battle Arena on Rema Island next to 436 and 437 (type 6); the only differences from 436 in the record are the type, the colour and `unknown_tail_46` (437 also sets `is_safe_zone`), so I cannot tell what sets it apart. Possibly the Battle Arena that Trial Characters are locked into.

Enter both and note the death message and the exit prompt. If Pit of the Undying shows the PvE arena handling that `isPVEArenaZone` drives, type 7 is the PvE arena. If 1072 shows the same as Battle Arena 436, the difference of type 8 is not visible there; anything else (for example a Trial Character notice) names it.

### Node War Limits Outside Calpheon and Ulukita

Needs zone (any one):

- a node war node in Valencia
- a node war node in Edania

Heidel's limit set is what Calpheon and Ulukita nodes show in game (see Notes). Read the node tooltip of one Valencia or Edania node. The expected result is the uncapped set of Altinova and Valencia City (`9999`). That would confirm the capital records as the limits per territory pair, and `unknown_tail_86` (`5` on Calpheon and Ulukita, `15` on Valencia and Edania) as the key that picks which capital's set a node uses. Velia's set (AP 560, damage reduction 410, evasion 768, accuracy 680, damage reduction rate 20%) matches no node seen so far: the occupation mode nodes of Balenos and Serendia show other values. Note any node that shows it.
