# `dropuihuntinggroundinfo.bss` Format

## Purpose

The hunting grounds of the drop item window (Monster Zone Info): one
variable-length row per zone with its region tab, filter categories, Korean
name, monsters, repeat and sudden quests, drop items, tags, regions, titles,
navigation position, recommended and Total Stat AP / DP, node and the Max AP
Limit. LOC type 116 names the zones by key.

Example:

```text
hunting ground 117, region tab 13 (Inner Edania), categories 3 (Marni's Realm), 8 (Allan Serbin's Landscape)
  name     Lv.74 아레시온 신전 -> "Lv. 74 Aresion Temple" (LOC 116)
  AP / DP  recommended 415 / 495, Total Stat 2455 / 850
  Max AP   2485 (5%)
  node     2110 Aresion Temple (LOC 29)
  weekly   [Weekly] War in Aresion (chain 9327, quest 4)
```

`worldmapmonster.dbss` points at these keys from its hunting zone markers (see
[`worldmapmonster_dbss.md`](worldmapmonster_dbss.md) Notes).

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

## File Layout

PABR block with variable-length rows, followed by the same counted string
table and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-pool)
(`_common/pabr_strings.py`).

| Offset  | Type    | Field              | Notes                                                  |
| ------- | ------- | ------------------ | ------------------------------------------------------ |
| `+0x00` | char[4] | magic              | ASCII `PABR`                                           |
| `+0x04` | u32     | count              | Number of rows; 112 on client 3458                     |
| `+0x08` | row[]   | rows               | Variable-length rows, read in order                    |
| ...     | table   | string_table       | 112 wide strings, one Korean name per row              |
| EOF - 8 | u32     | string_table_start | Where the rows end (`0x5FD8` on client 3458)           |
| EOF - 4 | u32     | zero               | Always `0`                                             |

Rows are sorted by key, which runs from 0 to 119 with gaps (2, 4, 7, 8, 14,
15, 16 and 49 are missing).

## Record Structure

### Hunting Ground Row (variable size)

A list is a u32 count followed by that many values.

| Order | Type        | Field                    | Notes                                                                 |
| ----- | ----------- | ------------------------ | --------------------------------------------------------------------- |
| 1     | u32         | key                      | Hunting ground key; LOC type 116 `str_id1`                            |
| 2     | u32         | main_category_key        | Region tab, 1 to 13, a `dropuimaincategoryinfo.bss` key               |
| 3     | u32 list    | sub_category_keys        | Filter categories (`dropuisubcategoryinfo.bss` keys, LOC type 115); empty on 13 rows |
| 4     | u32         | name_ref                 | String table index of the Korean name; unique per row                  |
| 5     | u16 list    | monster_ids              | Character IDs (LOC type 6), 1 to 17 per row                           |
| 6     | u32 list    | repeat_quest_keys        | Packed quest keys: low u16 quest chain, high u16 quest (LOC type 18 `str_id1` / `str_id2`), as in `allquestlist.bss`; repeat, daily and weekly quests |
| 7     | u32 list    | sudden_quest_keys        | Packed like `repeat_quest_keys`; subjugation and season quests, on 27 rows (13 of them in Valencia) |
| 8     | u32 list    | drop_item_ids            | Item IDs (LOC type 0), plain IDs with no enchant level, in the window's display order |
| 9     | u32 list    | tag_keys                 | Tag keys, LOC type 117 (`#LotsOfMobs`, `#CombatEXP`)                   |
| 10    | u16 list    | region_keys              | Region keys, LOC type 17; a zone can span several regions (Mansha Forest: 289 and 523) |
| 11    | u32 list    | title_keys               | Titles earned in the zone, LOC type 1 (`Mansha Slayer`)                |
| 12    | f32 x 3     | position                 | World position for the navigation guide; `0, 0, 0` on 21 rows          |
| 13    | f32         | recommended_ap           | The "Recommended AP" of the worldmap marker label                       |
| 14    | f32         | recommended_dp           | Recommended DP                                                          |
| 15    | u32         | node_key                 | `exploration.bss` node key (LOC type 29); `0` on 6 rows                 |
| 16    | f32         | total_ap                 | The "AP (Total Stat)" of the worldmap marker label                      |
| 17    | f32         | total_dp                 | Recommended DP (Total Stat)                                             |
| 18    | u32         | limited_ap               | Max AP Limit                                                            |
| 19    | u32         | limited_ap_apply_percent | Percent of the AP above `limited_ap` that still applies; `0` on 13 rows |
| 20    | u8          | tribe_type               | Monster species, 0 to 4; see `tribe_type` Values                       |

All 112 rows walk to exactly `string_table_start` with this layout on client
3458.

### `tribe_type` Values

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

## Suggested UI Layout

| Column      | Type | Notes                                                                       |
| ----------- | ---- | --------------------------------------------------------------------------- |
| Key         | num  | `key`; right-aligned                                                        |
| Name        | text | LOC type 116, falling back to the Korean name                               |
| Region      | text | Tab territory name (LOC type 12 `str_id4` 1), falling back to the tab key; sorts in tab order (`main_category_key`) |
| Categories  | text | LOC type 115 names, falling back to the keys                                |
| AP          | num  | `recommended_ap`                                                            |
| DP          | num  | `recommended_dp`                                                            |
| Total AP    | num  | `total_ap`                                                                  |
| Total DP    | num  | `total_dp`                                                                  |
| Max AP      | text | `limited_ap`, with `(n%)` when `limited_ap_apply_percent` is not 0           |
| Node        | text | `node_key` name (LOC type 29); dash when 0                                  |
| Monsters    | text | Monster names (LOC type 6)                                                  |
| Items       | text | Icon and name (LOC type 0) of each item in its grade colour (`ITEM_GRADE`), through `item_key_list_cell()` |
| Quests      | text | Repeat and sudden quest titles (LOC type 18)                                |
| Tags        | text | Tag names (LOC type 117), each a pill in its `dropuitaginfo.bss` colours as in game; plain names without that file |
| Titles      | text | Title names (LOC type 1)                                                    |
| Species     | text | `tribe_type` as `{value} {label}` (`1 Demihumans`); the label from LOC type 37, falling back to the enum name (`1 NonHuman`) |

The position and region keys stay on the record but out of the table.

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
