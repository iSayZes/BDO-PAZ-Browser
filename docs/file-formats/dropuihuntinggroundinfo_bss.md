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

| File                          | Required | Role                                                                      |
| ----------------------------- | -------- | ------------------------------------------------------------------------- |
| `dropuimaincategoryinfo.bss`  | Optional | Region tabs: tab key -> territory and tab icon, see below                 |
| `dropuisubcategoryinfo.bss`   | Optional | Filter categories: Korean name and button icon, see below                 |
| `dropuitaginfo.bss`           | Optional | Tags: Korean name and tooltip, Dehkia's Lantern guide image, tag and text colours, see below |
| `languagedata_en.loc`         | Optional | Zone names (116), categories (115), tags (117), territories (12), monsters (6), items (0), quests (18), regions (17), titles (1), nodes (29) |

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

### `dropuimaincategoryinfo.bss`

PABR block of 13 fixed 10-byte rows plus the counted string table, which
holds only the 13 tab icon names (`Combine_Etc_DropItem_Icon_Tab_04`, ...).

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | key           | Region tab, 1 to 13                                         |
| `+0x04` | u16  | territory_key | LOC type 12 `str_id1`; `str_id4` 1 is the tab name           |
| `+0x06` | u32  | icon_ref      | String table index of the tab icon                          |

The tabs are Balenos, Serendia, Calpheon, Mediah, Valencia, Kamasylvia,
Drieghan, O'dyllita, Mountain of Eternal Winter, Ulukita, Land of the Morning
Light, Outer Edania and Inner Edania; the Great Ocean (territory 5) has no
tab, and tabs 10 and 11 swap the territory order.

### `dropuisubcategoryinfo.bss`

PABR block of 8 fixed 12-byte rows plus the counted string table (15
strings: the Korean names and the button icon names).

| Offset  | Type | Field    | Notes                                                    |
| ------- | ---- | -------- | -------------------------------------------------------- |
| `+0x00` | u32  | key      | Category, 1 to 8; LOC type 115 `str_id1`                  |
| `+0x04` | u32  | name_ref | String table index of the Korean name                    |
| `+0x08` | u32  | icon_ref | String table index of the button icon; 6 and 7 share one |

| Key | Korean            | LOC type 115              |
| --- | ----------------- | ------------------------- |
| 1   | 파티 사냥터       | Party Zones               |
| 2   | 엘비아의 영역     | Elvia Realm               |
| 3   | 마르니의 밀실     | Marni's Realm             |
| 4   | 지역 의뢰         | Region Quests             |
| 5   | 추천              | Suggested                 |
| 6   | 데키아의 등불     | Dehkia's Lantern          |
| 7   | 데키아의 등불 II  | Dehkia's Lantern II       |
| 8   | 알란 세르빈의 풍경 | Allan Serbin's Landscape |

No hunting ground stores 5 or 7.

### `dropuitaginfo.bss`

PABR block of 45 fixed 32-byte rows plus the counted string table (118
strings: the Korean names and tooltips, the guide image names and the colours
as hex text). Rows are sorted by key, 1 to 45 with no gaps.

| Offset  | Type | Field                 | Notes                                                                    |
| ------- | ---- | --------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | key                   | Tag key, as in `tag_keys`; LOC type 117 `str_id1`                         |
| `+0x04` | u32  | name_ref              | String table index of the Korean name (`#다수의 몬스터와 전투`); LOC `str_id4` 0 is the English one (`#LotsOfMobs`) |
| `+0x08` | u32  | guide_texture_ref     | String table index of the guide image name; the empty string on 32 rows   |
| `+0x0C` | u32  | desc_ref              | String table index of the Korean tooltip, with `<PAColor>` tags; LOC `str_id4` 1 is the English one |
| `+0x10` | u32  | texture_color_ref     | String table index of `texture_color` as hex text (`ffe1ba65`)           |
| `+0x14` | u32  | font_color_ref        | String table index of `font_color` as hex text                           |
| `+0x18` | u32  | texture_color         | Tag background colour, ARGB (`0xFFE1BA65`)                                |
| `+0x1C` | u32  | font_color            | Tag text colour, ARGB                                                     |

The two hex strings always equal the two ARGB values (case aside: `ffD2691E`,
`ff3CB371`), so the strings carry nothing extra. The colours are the same on
34 rows; the other 11 have a darker background and a lighter text:

| Keys                     | Tag                         | `texture_color` | `font_color` |
| ------------------------ | --------------------------- | --------------- | ------------ |
| 20, 21, 23, 25 to 32, 42, 43 | `#FixedLanternSpot`     | `0xFF5384D5`    | `0xFFA6C0EA` |
| 38, 39, 40               | Stun, knockdown, knockback  | `0xFFD2691E`    | `0xFFFFA500` |
| 41                       | `#AllanSerbinsLandscape`    | `0xFF3CB371`    | `0xFF98FB98` |

`guide_texture_ref` is set only on the 13 `#FixedLanternSpot` rows, one image
per zone (`Combine_Etc_DekiaLanterns_GroundTooltip_01` to `_13`): a map of
where the Dehkia's Lantern can be summoned, shown when the tag is clicked.
Each name is a whole texture of the same name, lower-cased, in the folder its
first two parts name: `ui_texture/combine/etc/combine_etc_dekialanterns_groundtooltip_01.dds`.
All 13 exist on client 3458 (717.8 KB each). The Korean tooltips store a line
break as the two characters `\n`, where LOC has a real newline.
Some colours are shared: `0xFF63B6E6` on `#NoItemCollectGauge`,
`#NoAgrisFever`, both Golden Pig Caves, Atoraxxion and Orzekea, and
`0xFFCB6768` on `#TreasurePieces`, `#RedArtifacts` and `#HighestTier`.

Only tag 17 (`#PartyOf4`) is on no hunting ground on client 3458; LOC type 117
names all 45 plus a key 46 with the same `#DivineAuthority` text as 45.

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

### `dropuitaginfo.bss`

| Column      | Type  | Notes                                                                      |
| ----------- | ----- | -------------------------------------------------------------------------- |
| Key         | num   | `key`; right-aligned                                                       |
| Name        | text  | LOC type 117 `str_id4` 0, falling back to the Korean name; drawn as the tag pill in its two colours, as on the hunting grounds |
| Guide Image | image | The guide image texture; dash on rows without one; sorts by the texture name |
| Colours     | text  | `texture_color / font_color` as `0xFF5384D5 / 0xFFA6C0EA`; sorts by `texture_color` |
| Description | text  | LOC type 117 `str_id4` 1 in its `<PAColor>` colours (`pa_fields`), falling back to the Korean tooltip; one line, cut after 120 characters |
| Hunting Grounds | text | Names (LOC type 116, falling back to the Korean name) of the `dropuihuntinggroundinfo.bss` rows whose `tag_keys` hold the tag, in file order; dash without that file |

The handler loads `dropuihuntinggroundinfo.bss` as an optional companion for
the Hunting Grounds column. The two hex colour strings stay out of the
record, since they repeat the ARGB values.

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
- The same Lua draws each tag through `ToClient_getDropUITagStaticStatusWrapper`:
  `tagControl:SetColor(getTextureColor())`, `SetFontColor(getFontColor())`,
  the text from `getTagString`, the tooltip from `getTagTooltipDescString`
  under the `LUA_DROPITEMUI_TOOLTIP_TAG_TITLE` heading, and on click the
  guide image from `getTagGuideTextureId` when `isExistGuideTextureId`.
- Which slot is which colour comes from
  [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  (`DecodeTags`: `+0x18` texture, `+0x1C` font) and fits the data: wherever
  the two differ, `+0x1C` is the lighter shade, as text on a tinted
  background would be. The getters alone do not show the order; the game
  confirms it: on Aakman, `#Knockdown/Bound` is orange text on a brown pill.
- The tag control's texture (`StaticText_Tag_Templete` in
  `ui_data/window/dropitem/panel_window_dropitem_all_renew.xml`) is
  `Combine_Etc_DropItem_Tag_BG`, a pill in `combine/etc/combine_etc_dropitem.dds`
  (UV 128,314 to 228,339) that is white at alpha 51. `SetColor` tints it, so
  the background shows `texture_color` at about 20% over the window, and a
  tag whose two colours are equal (34 of 45) still reads.

## Open Questions

### Where the Client Resolves a Guide Image Name

The window Lua hands `getTagGuideTextureId` to
`PaGlobalFunc_DropItemImageToolTip_Open` as a texture ID. I have not found the
table that maps such an ID to a file, so the handler takes the file of the
same name in the folder the first two name parts give. That holds for all 13
names on client 3458, but `Combine_Etc_DropItem_Tag_BG` is a sprite inside
`combine_etc_dropitem.dds`, so a later guide image could be a sprite too and
then show a dash.
