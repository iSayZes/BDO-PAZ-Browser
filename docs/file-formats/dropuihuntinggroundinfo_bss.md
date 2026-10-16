# `dropuihuntinggroundinfo.bss` Format

## Purpose

The hunting grounds of the drop item window (Monster Zone Info): one
variable-length row per zone with its region tab, filter categories, Korean
name, monsters, repeat and sudden quests, drop items, tags, regions, titles,
navigation position, recommended and Total Stat AP / DP, node and the Max AP
Limit. LOC type 116 names the zones by key.

`worldmapmonster.dbss` points at these keys from its hunting zone markers (see
[`worldmapmonster_dbss.md`](worldmapmonster_dbss.md) Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                                                          | Required | Role                                                      |
| ------------------------------------------------------------- | -------- | --------------------------------------------------------- |
| [`dropuimaincategoryinfo.bss`](dropuimaincategoryinfo_bss.md) | Optional | Region tabs: tab key -> territory, for the Region column  |
| [`dropuitaginfo.bss`](dropuitaginfo_bss.md)                   | Optional | Tag pill colours for the Tags column                      |
| `languagedata_en.loc`                                         | Optional | Zone names (116), categories (115), tags (117), territories (12), monsters (6), items (0), quests (18), regions (17), titles (1), nodes (29) |

[`dropuisubcategoryinfo.bss`](dropuisubcategoryinfo_bss.md) holds the filter
categories of `sub_category_keys`; the handler names them from LOC type 115
alone.

`dropuiurlinfo.bss` (20 bytes) is an empty PABR block on client 3458 (count
0).

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block with variable-length rows, followed by the same counted string
table and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-pool)
(`_common/pabr_strings.py`).

| Offset              | Type                      | Field              | Notes                                        |
| ------------------- | ------------------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]                   | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32                       | count              | Number of rows; 112 on client 3458           |
| `+0x08`             | Hunting Ground Row[count] | rows               | Variable-length rows, read in order          |
| `rows+0x00`         | String Table              | string_table       | 112 wide strings, one Korean name per row    |
| `string_table+0x00` | u32                       | string_table_start | Where the rows end (`0x5FD8` on client 3458) |
| `string_table+0x04` | u32                       | zero               | Always `0`                                   |

Rows are sorted by key, which runs from 0 to 119 with gaps (2, 4, 7, 8, 14,
15, 16 and 49 are missing).

### Hunting Ground Row (variable: 85 bytes + lists)

A list is a u32 count followed by that many values.

| Offset                   | Type                        | Field                    | Notes                                                                 |
| ------------------------ | --------------------------- | ------------------------ | --------------------------------------------------------------------- |
| `+0x00`                  | u32                         | key                      | Hunting ground key; LOC type 116 `str_id1`                            |
| `+0x04`                  | u32                         | main_category_key        | Region tab, 1 to 13, a `dropuimaincategoryinfo.bss` key               |
| `+0x08`                  | u32                         | sub_category_key_count   | Number of `sub_category_keys`                                         |
| `+0x0C`                  | u32[sub_category_key_count] | sub_category_keys        | Filter categories (`dropuisubcategoryinfo.bss` keys, LOC type 115); empty on 13 rows |
| `sub_category_keys+0x00` | u32                         | name_ref                 | String table index of the Korean name; unique per row                 |
| `sub_category_keys+0x04` | u32                         | monster_id_count         | Number of `monster_ids`                                               |
| `sub_category_keys+0x08` | u16[monster_id_count]       | monster_ids              | Character IDs (LOC type 6), 1 to 17 per row                           |
| `monster_ids+0x00`       | u32                         | repeat_quest_key_count   | Number of `repeat_quest_keys`                                         |
| `monster_ids+0x04`       | u32[repeat_quest_key_count] | repeat_quest_keys        | Packed quest keys: low u16 quest chain, high u16 quest (LOC type 18 `str_id1` / `str_id2`), as in `allquestlist.bss`; repeat, daily and weekly quests |
| `repeat_quest_keys+0x00` | u32                         | sudden_quest_key_count   | Number of `sudden_quest_keys`                                         |
| `repeat_quest_keys+0x04` | u32[sudden_quest_key_count] | sudden_quest_keys        | Packed like `repeat_quest_keys`; subjugation and season quests, on 27 rows (13 of them in Valencia) |
| `sudden_quest_keys+0x00` | u32                         | drop_item_count          | Number of `drop_item_ids`                                             |
| `sudden_quest_keys+0x04` | u32[drop_item_count]        | drop_item_ids            | Item IDs (LOC type 0), plain IDs with no enchant level, in the window's display order |
| `drop_item_ids+0x00`     | u32                         | tag_key_count            | Number of `tag_keys`                                                  |
| `drop_item_ids+0x04`     | u32[tag_key_count]          | tag_keys                 | Tag keys, LOC type 117 (`#LotsOfMobs`, `#CombatEXP`)                  |
| `tag_keys+0x00`          | u32                         | region_key_count         | Number of `region_keys`                                               |
| `tag_keys+0x04`          | u16[region_key_count]       | region_keys              | Region keys, LOC type 17; a zone can span several regions (Mansha Forest: 289 and 523) |
| `region_keys+0x00`       | u32                         | title_key_count          | Number of `title_keys`                                                |
| `region_keys+0x04`       | u32[title_key_count]        | title_keys               | Titles earned in the zone, LOC type 1 (`Mansha Slayer`)               |
| `title_keys+0x00`        | f32[3]                      | position                 | World position for the navigation guide; `0, 0, 0` on 21 rows         |
| `title_keys+0x0C`        | f32                         | recommended_ap           | The "Recommended AP" of the worldmap marker label                     |
| `title_keys+0x10`        | f32                         | recommended_dp           | Recommended DP                                                        |
| `title_keys+0x14`        | u32                         | node_key                 | `exploration.bss` node key (LOC type 29); `0` on 6 rows               |
| `title_keys+0x18`        | f32                         | total_ap                 | The "AP (Total Stat)" of the worldmap marker label                    |
| `title_keys+0x1C`        | f32                         | total_dp                 | Recommended DP (Total Stat)                                           |
| `title_keys+0x20`        | u32                         | limited_ap               | Max AP Limit                                                          |
| `title_keys+0x24`        | u32                         | limited_ap_apply_percent | Percent of the AP above `limited_ap` that still applies; `0` on 13 rows |
| `title_keys+0x28`        | u8                          | tribe_type               | Monster species, 0 to 4; see `tribe_type` Values                      |

All 112 rows walk to exactly `string_table_start` with this layout on client
3458.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                      |
| ------- | ------------------ | ------------ | ------------------------------------------ |
| `+0x00` | u32                | string_count | 112 on client 3458                         |
| `+0x04` | pstr[string_count] | strings      | Korean zone names; `name_ref` indexes them |

## `tribe_type` Values

The client enum `__eNewTribeType_*`; the drop window labels each value with a
`GAME` sheet string (LOC type 37) and says which Extra AP applies
(`LUA_DROPITEM_<X>_TOOLTIP_DESC`).

| Value | Enum         | Label key                              | Label                 | Rows | Extra AP that applies             |
| ----- | ------------ | -------------------------------------- | --------------------- | ---- | --------------------------------- |
| 0     | `Human`      | `LUA_DROPITEM_HUMAN_TOOLTIP_NAME`      | Humans                | 21   | Extra AP Against Humans           |
| 1     | `NonHuman`   | `LUA_DROPITEM_AIN_TOOLTIP_NAME`        | Demihumans            | 34   | Extra AP Against Demihumans       |
| 2     | `Others`     | `LUA_DROPITEM_NORMAL_TOOLTIP_NAME`     | Normal                | 22   | Extra AP Against Monsters         |
| 3     | `Kamasilvia` | `LUA_DROPITEM_KAMASILVIA_TOOLTIP_NAME` | Kamasylvian Monsters  | 21   | Extra AP Against Kamasylvian Monsters |
| 4     | `Edania`     | `LUA_DROPITEM_EDANIA_TOOLTIP_NAME`     | Edanian Monsters      | 14   | Extra AP Against Edanian Monsters |

The Lua lists the five enum names with their label keys in this order, and the
zones match: `0` bandits, pirates, Abandoned Monastery and the Elvia human
zones; `1` Mansha Forest, Catfishman Camp, Rhutum Outstation; `2` Hexe
Sanctuary, Soldier's Grave, Cyclops Land; `3` Polly's Forest, Navarn Steppe,
Ash Forest, Olun's Valley; `4` Aetherion Castle to Scales of Judgment.

## Notes

- Since client 3464 every one of the 112 names opens with a level, in the
  Korean string table (`Lv.74 아레시온 신전`) and in LOC type 116
  (`Lv. 74 Aresion Temple`). The node names (LOC type 29) carry none. The
  handler shows the names as stored.
- The drop item window Lua (`window/dropitem/panel_window_renewdropitem_all_1`)
  reads the row through `ToClient_getDropUIHuntingGroundStaticStatusWrapper`;
  its getters match the fields: `getMainCategoryKey`,
  `getSubCategoryKeyByIndex`, `getName`, `getRepeatQuestNoByIndex`,
  `getSuddenQuestNoByIndex`, `getDropItemStaticStatusWrapper`,
  `getTagKeyByIndex`, `getRegionKeyRawByIndex`,
  `getDropTitleStaticStatusWrapper`, `getWayPointKey`, `getLimitedAP`,
  `getLAPApplyPercent` and `getTribeType`.
- The Max AP Limit text is `LUA_DROPINFO_MAXAP` (`{appoint}({appercent}%)`)
  or, when the percent is 0, `LUA_DROPINFO_MAXAP_NONE_PERCENT` (`{appoint}
  effective limit`); `LUA_DROPINFO_MAXAP_DESC` explains that only that share of
  the AP above the limit applies.
- The AP values equal the worldmap marker labels of the same zone: Aresion
  Temple stores 415 and 2455, and its marker reads "Recommended AP: 415" and
  "AP (Total Stat): 2455". `limited_ap` sits 30 above `total_ap` on 67 rows
  (2455 -> 2485, 2570 -> 2600).
- LOC type 116 names all 112 rows and has one more key, 49, with no row.
  Every monster, item, tag, region, title, node and quest ID in the file has
  LOC text on client 3458.
- `drop_item_ids` holds plain item IDs (`28` Prognyl Silver Bar, `721002`
  Ancient Spirit Dust), not the packed `itemenchant.dbss` key.
- bdo-viewer (built on bdo-data-extractor) counts 105 zones; the file holds
  112 rows.
