# `territoryinfo.bss` Format

## Purpose

The world's territories (Balenos, Serendia, Calpheon, ...) in game order: one
row per territory with its Korean territory and nation names, world map mark
icons, the booty items its lord receives (a conquest crown and armor), its
siege positions and its territory supply keys. The row key is the LOC type 12
ID, so the English territory and nation names come from that type.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records          | Row bytes                  |
| ------ | -------------- | ------- | ------------------- | ----- | ---------------- | -------------------------- |
| 2      | 3002 and later | 3474    | `territoryinfo.bss` | 4,730 | 14 Territory Row | 88 to 92, 89 on average    |
| 1      | 1485 to 2107   | 2107    | `territoryinfo.bss` | 3,847 | 10 Territory Row | 120 to 140, 131 on average |

| Layout | File                | Known           | Unknown     |
| ------ | ------------------- | --------------- | ----------- |
| 2      | `territoryinfo.bss` | 4,674 B (98.8%) | 56 B (1.2%) |
| 1      | `territoryinfo.bss` | 3,807 B (99.0%) | 40 B (1.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3251   | Layout 2             |
| 3002   | Layout 2             |
| 2519   | No documented layout |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | No documented layout |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                     |
| --------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | LOC type 12, `str_id1` = `territory_key`, `str_id4` 0 / 1 = nation or realm / territory name |
| `languagedata_en.loc` | Optional | LOC type 0 names of the booty items                                                      |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout (`_common/pabr_strings.py`).

| Offset              | Type                 | Field        | Notes                                          |
| ------------------- | -------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                  | count        | Number of rows; 14 on client 3458              |
| `+0x08`             | Territory Row[count] | rows         | Byte-packed; see Territory Row                 |
| `rows+0x00`         | String Table         | string_table | See String Table                               |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                  | zero         | Always 0                                       |

A row is `80 + 4 * (booty_item_count + territory_supply_key_count)` bytes.
The rows tile `[0x08, table_start)` exactly (12 rows of 88 bytes and 2 of 92
on client 3458), so a parser walks them in order and fails when they do not
end at `table_start`.

### Territory Row (variable: 80 bytes + lists)

| Offset                       | Type                              | Field                      | Notes                                                                                  |
| ---------------------------- | --------------------------------- | -------------------------- | -------------------------------------------------------------------------------------- |
| `+0x00`                      | u16                               | territory_key              | 0 to 13, equal to the row index; LOC type 12 `str_id1`                                 |
| `+0x02`                      | u8                                | is_king_territory_only     | `1` on Calpheon to Outer Edania, `0` on Balenos, Serendia and Inner Edania             |
| `+0x03`                      | u8                                | is_lord_territory_only     | `1` on Balenos and Serendia only, the two names ending in 자치령 (autonomous territory) |
| `+0x04`                      | f32[3]                            | occupying_tent_position    | World `x, y, z` of the occupying tent; all zero when unused |
| `+0x10`                      | f32[3]                            | volunteer_attack_position  | World `x, y, z` of the militia attack respawn point; all zero when unused |
| `+0x1C`                      | f32[3]                            | volunteer_defense_position | World `x, y, z` of the militia defense respawn point; all zero when unused |
| `+0x28`                      | u32                               | national_key               | Same value on every territory of one nation, different between nations |
| `+0x2C`                      | u32                               | nation_ref                 | String table index of the Korean nation or realm name                                  |
| `+0x30`                      | u32                               | name_ref                   | String table index of the Korean territory name                                        |
| `+0x34`                      | u32                               | icon_large_ref             | String table index of the large world map mark, relative to `ui_texture/`              |
| `+0x38`                      | u32                               | icon_small_ref             | String table index of the small world map mark, relative to `ui_texture/`              |
| `+0x3C`                      | u64                               | booty_item_count           | Entries in `booty_item_ids`; `2` on every row on client 3473                           |
| `+0x44`                      | u32[booty_item_count]             | booty_item_ids             | Items the territory's lord receives (LOC type 0): the conquest crown, then its armor   |
| `booty_item_ids+0x00`        | u64                               | territory_supply_key_count | Entries in `territory_supply_keys`; `1` on Serendia and Mediah, `0` elsewhere on client 3473 |
| `booty_item_ids+0x08`        | u32[territory_supply_key_count]   | territory_supply_keys      | Territory supply group keys: `114` on Serendia, `312` on Mediah on client 3473         |
| `territory_supply_keys+0x00` | u32                               | unknown_tail               | `0` on every row                                                                       |

Positions on client 3458: Calpheon, Mediah and Valencia fill all three,
Kamasylvia and O'dyllita only the first, the rest none. The occupying tent
and the militia defense position lie within about 20,000 units of a castle
node in `mapdata_realexplore2.bwp`: `calpheon_castle` (702), `mediacastle`
(1152), `valencia_castle` (1342) and `othilita_castle` (1692). Valencia's
militia attack position sits next to `ruins of castle valencia` (1374).

Booty items: Balenos to Mediah each have their own crown and armor (Silver
Mane, Blue Lion, Golden Eagle, Asula); Valencia and every later territory
store the Crown of Aal (23385) and Armor of Aal (23390).

### String Table (variable: 4 bytes + strings)

46 strings on client 3458, all referenced. The territories of one nation
share its nation entry (Republic of Calpheon, Alyaelli), and where nation and
territory names match (The Great Ocean, Kamasylvia and the other single
territory realms) both refs point at one entry. The Great Ocean (territory 5) stores Valencia's marks under
`New_UI_Common_forLua/Widget/WorldMap/territory/`; every other icon is under
`Renewal/ETC/WordMap/`. Paths keep mixed case, so the handler lowercases them.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 46 on client 3458   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Layout 1

On client 1784 a Territory Row held five positions instead of three, which
moved `national_key` to `+0x40`, and a u16 list of territory trade keys before
the territory supply keys, which were u16 values too. Only the
Territory Row differs from Layout 2. On client 1784 the file holds 10 rows;
Balenos to Mediah have 5 trade keys and the rest none, and every territory
has 0 to 5 supply keys.

### Territory Row (variable: 112 bytes + lists)

| Offset                       | Type                            | Field                      | Notes                                                          |
| ---------------------------- | ------------------------------- | -------------------------- | -------------------------------------------------------------- |
| `+0x00`                      | u16                             | territory_key              |                                                                |
| `+0x02`                      | u8                              | is_king_territory_only     |                                                                |
| `+0x03`                      | u8                              | is_lord_territory_only     |  |
| `+0x04`                      | f32[3]                          | occupying_tent_position    |  |
| `+0x10`                      | f32[3]                          | volunteer_attack_position  |  |
| `+0x1C`                      | f32[3]                          | volunteer_defense_position |  |
| `+0x28`                      | f32[3]                          | plunder_attack_position    | World `x, y, z` of the plunder war attack respawn point |
| `+0x34`                      | f32[3]                          | plunder_defense_position   | World `x, y, z` of the plunder war defense respawn point |
| `+0x40`                      | u32                             | national_key               |  |
| `+0x44`                      | u32                             | nation_ref                 |                                                                |
| `+0x48`                      | u32                             | name_ref                   |                                                                |
| `+0x4C`                      | u32                             | icon_large_ref             |                                                                |
| `+0x50`                      | u32                             | icon_small_ref             |                                                                |
| `+0x54`                      | u64                             | booty_item_count           |                                                                |
| `+0x5C`                      | u32[booty_item_count]           | booty_item_ids             |                                                                |
| `booty_item_ids+0x00`        | u64                             | territory_trade_key_count  | Entries in `territory_trade_keys`                              |
| `booty_item_ids+0x08`        | u16[territory_trade_key_count]  | territory_trade_keys       | Territory trade group keys: Balenos holds `5` to `1`, Serendia `105` to `101` |
| `territory_trade_keys+0x00`  | u64                             | territory_supply_key_count |                                                                |
| `territory_trade_keys+0x08`  | u16[territory_supply_key_count] | territory_supply_keys      | Balenos holds `11` to `15`, Serendia `113`, `112`, `111`, `114`, `115` |
| `territory_supply_keys+0x00` | u32                             | unknown_tail               | `0` on every row on client 1784                                |

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its
`gc::TerritoryInfo` holds `_territoryKey` (i16), `_isKingTerritoryOnly`,
`_isLordTerritoryOnly`, `_occupyingTentPosition`, three members filled at
load time (`_mainTownRegion`, `_capitalTownRegion`, `_affliatedRegionGroups`),
`_nationalKey` (u32), `_nationalName`, `_territoryName`, `_territoryImage`,
`_territorySmallImage`, `_bootyItemKeyList` (a vector of i32),
`_bootyItemList` (a vector of `gc::Item`), and four vectors of u16 keys:
`_territoryTradeList`, `_territorySupplyList`, `_territoryTradeKeyList` and
`_territorySupplyKeyList`. Layout 1 stores `_territoryKey` to
`_occupyingTentPosition`, `_nationalKey` to `_territorySmallImage`,
`_bootyItemKeyList`, `_territoryTradeKeyList` and `_territorySupplyKeyList`
in this order, with five positions where the 2016 struct has one.

`Territory_Table` in a private server's `DataSheets.bexcel` on client 1784
(and the same sheet in its `.xlsm`, and in a second private server's database
on client 519) has the columns `TerritoryKey`, `NationalName`,
`TerritoryName`, `TerritoryImage`, `TerritorySmallImage`,
`OccupyingTentPositionX` to `Z`, `BootyItem`, `WorldMapColor`,
`VolunteerAttackX` to `Z`, `VolunteerDefenseX` to `Z`, `PlunderAttackX` to
`Z` and `PlunderDefenseX` to `Z`. The sheet shares territory keys 0 to 9 with
both clients:

| Column | Field | Equal (client 1784, 10 keys) | Equal (client 3473, 10 keys) |
| ------ | ----- | ---------------------------- | ---------------------------- |
| `OccupyingTentPositionX` to `Z` | `occupying_tent_position` | 10 | 8 |
| `VolunteerAttackX` to `Z` | `volunteer_attack_position` | 10 | 10 |
| `VolunteerDefenseX` to `Z` | `volunteer_defense_position` | 10 | 10 |
| `PlunderAttackX` to `Z` | `plunder_attack_position` | 10 | |
| `PlunderDefenseX` to `Z` | `plunder_defense_position` | 10 | |
| `BootyItem` | `booty_item_ids` | 10 | 10 |

Calpheon, Mediah and Valencia fill every position column; the other rows
are zero in both. The two client 3473 tent mismatches are Kamasylvia and
O'dyllita, which the sheet leaves at zero. The
sheet comments call the volunteer columns the militia (민병대) siege attack
and defense respawn points, the plunder columns the plunder war (약탈전)
respawn points, and `BootyItem` the items given to the occupying lord, at
enchant level 0 and count 1. `WorldMapColor` has no bytes in either layout.

The two lists come from `TerritoryTradeItemList_Table` (columns
`TerritoryKey`, `ItemGroupKeyType`, `ItemMainGruopKey`, `TerritoryGroupKey`).
Its comment gives `ItemGroupKeyType` `0` as territory trade (영지 무역) and
`1` as territory supply (영지 납품). On client 1784 each list holds the
`TerritoryGroupKey` values of the territory's rows of one type, in sheet
order: the first list type `0` on 4 of the 4 territories that have such
rows, the second type `1` on 6 of the 9. Valencia and The Great Ocean keep
their first 4 of 5 and 6 rows, and O'dyllita stores none of its one row
(`415`, `515`, `516` and `811` are missing). Neither list holds `ItemMainGruopKey` values, so the names follow the 2016
`_territoryTradeKeyList` and `_territorySupplyKeyList`. Client 3473 has one
list, and its keys `114` (Serendia) and `312` (Mediah) are type `1` rows of
those territories. `TerritorySupply` is the NPC role the client labels
Imperial Delivery (see [characterspawntype](characterspawntype_dbss.md)).

`is_king_territory_only` has no sheet column and is named from its place in
the 2016 member order, between the matched `territory_key` and the occupying
tent position. The client Lua calls `siegeWrapper:isKingTerritoryOnly()` in
`panel_window_lordmenu_all_1.luac`, where `isKing()` and
`isKingTerritoryOnly()` together decide whether the lord menu shows its
first two local tax sliders. The next 2016 bool, `_isLordTerritoryOnly`, is
`is_lord_territory_only`, set on the two autonomous territories. `national_key` is the 2016
`_nationalKey`; the sheet has no column for it. The position fields take the
sheet's column names; the 2016 struct has only `_occupyingTentPosition`.

## Notes

- iDevelopThings' [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  documents the same layout (FORMATS.md, section 10), with
  `is_king_territory_only` as a primary-territory flag and the positions as
  world map marks.
- bdo-data-extractor reads a territory index in each `regioninfo.bss` region
  that joins this file and LOC type 12.
- The `territory_key` of `dropuimaincategoryinfo.bss` (see
  [dropuihuntinggroundinfo](dropuihuntinggroundinfo_bss.md)) is the same LOC
  type 12 key.
- A territory supply key is the territory key times 100 plus 11 to 16 in the
  sheet; the trade keys are the territory key times 100 plus 1 to 5.
- The handler's Lord Territory and King Territory column labels are my own
  translations of the 2016 `_isLordTerritoryOnly` and `_isKingTerritoryOnly`,
  in every language. The client LOC has no term for either flag: the English
  territory names are plain ("Balenos", "Serendia"), and the only English LOC
  string with "autonomous" is "Drieghan Autonomous Region". The Korean names
  of the two lord territories end in 자치령 (autonomous territory), which the
  English client does not show, so the column does not use that word.

## Open Questions

### What `unknown_tail` Holds

Both layouts end a row with a u32 that is `0` on every row of clients 1784
and 3473. The 2016
`gc::TerritoryInfo` ends with `_territorySupplyKeyList`, and no
`Territory_Table` column is left over except `WorldMapColor`, whose RGBA
values are not zero.
