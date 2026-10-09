# `dropuitaginfo.bss` Format

## Purpose

The tags of the drop item window hunting grounds: one fixed row per tag with
its Korean name and tooltip, the Dehkia's Lantern guide image and the tag's
background and text colours.
[`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) lists the
tag keys of each zone (`tag_keys`). LOC type 117 names the tags by key.

Example:

```text
tag 20 #FixedLanternSpot
  colours  0xFF5384D5 / 0xFFA6C0EA
  guide    Combine_Etc_DekiaLanterns_GroundTooltip_01
  zones    Lv. 63 Thornwood Forest [Dehkia's Lantern]
```

## Companion Files

| File                          | Required | Role                                                                    |
| ----------------------------- | -------- | ----------------------------------------------------------------------- |
| `dropuihuntinggroundinfo.bss` | Optional | Hunting grounds per tag, for the Hunting Grounds column                 |
| `languagedata_en.loc`         | Optional | Tag names and tooltips (117), hunting ground names (116)                |

All multi-byte values are little-endian.

## File Layout

PABR block of 45 fixed 32-byte rows, followed by the same counted string
table and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-pool)
(`_common/pabr_strings.py`). The string table holds 118 strings: the Korean
names and tooltips, the guide image names and the colours as hex text.

| Offset  | Type    | Field              | Notes                                   |
| ------- | ------- | ------------------ | --------------------------------------- |
| `+0x00` | char[4] | magic              | ASCII `PABR`                            |
| `+0x04` | u32     | count              | Number of rows; 45 on client 3458       |
| `+0x08` | row[]   | rows               | 32 bytes each                           |
| ...     | table   | string_table       | 118 wide strings                        |
| EOF - 8 | u32     | string_table_start | Where the rows end                      |
| EOF - 4 | u32     | zero               | Always `0`                              |

Rows are sorted by key, 1 to 45 with no gaps.

## Record Structure

### Tag Row (32 bytes)

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

Some colours are shared: `0xFF63B6E6` on `#NoItemCollectGauge`,
`#NoAgrisFever`, both Golden Pig Caves, Atoraxxion and Orzekea, and
`0xFFCB6768` on `#TreasurePieces`, `#RedArtifacts` and `#HighestTier`.

### Guide Images

`guide_texture_ref` is set only on the 13 `#FixedLanternSpot` rows, one image
per zone (`Combine_Etc_DekiaLanterns_GroundTooltip_01` to `_13`): a map of
where the Dehkia's Lantern can be summoned, shown when the tag is clicked.
Each name is a whole texture of the same name, lower-cased, in the folder its
first two parts name: `ui_texture/combine/etc/combine_etc_dekialanterns_groundtooltip_01.dds`.
All 13 exist on client 3458 (717.8 KB each).

## Suggested UI Layout

| Column          | Type  | Notes                                                                      |
| --------------- | ----- | -------------------------------------------------------------------------- |
| Key             | num   | `key`; right-aligned                                                       |
| Name            | text  | LOC type 117 `str_id4` 0, falling back to the Korean name; drawn as the tag pill in its two colours, as on the hunting grounds |
| Guide Image     | image | The guide image texture; dash on rows without one; sorts by the texture name |
| Colours         | text  | `texture_color / font_color` as `0xFF5384D5 / 0xFFA6C0EA`; sorts by `texture_color` |
| Description     | text  | LOC type 117 `str_id4` 1 in its `<PAColor>` colours (`pa_fields`), falling back to the Korean tooltip; one line, cut after 120 characters |
| Hunting Grounds | text  | Names (LOC type 116, falling back to the Korean name) of the `dropuihuntinggroundinfo.bss` rows whose `tag_keys` hold the tag, in file order; dash without that file |

The two hex colour strings stay out of the record, since they repeat the ARGB
values.

## Notes

- The Korean tooltips store a line break as the two characters `\n`, where
  LOC has a real newline.
- Only tag 17 (`#PartyOf4`) is on no hunting ground on client 3458; LOC type
  117 names all 45 plus a key 46 with the same `#DivineAuthority` text as 45.
- The drop item window Lua (`window/dropitem/panel_window_renewdropitem_all_1`)
  draws each tag through `ToClient_getDropUITagStaticStatusWrapper`:
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
