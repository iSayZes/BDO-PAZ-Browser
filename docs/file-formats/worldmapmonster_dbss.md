# `worldmapmonster.dbss` Format

## Purpose

The monster markers of the world map: hunting zones, field and world bosses,
Black Shrine bosses, Abyssal Wells and the Pilgrim's Sanctum spots. One
variable-length record per marker with two Korean label lines and a name, the
world position, the marker illustration and an optional condition script.
LOC type 40 holds the translations.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes  | Records                       | Row bytes                  |
| ------ | -------------- | ------- | ---------------------------- | ------ | ----------------------------- | -------------------------- |
| 2      | 3473 and later | 3474    | `worldmapmonster.dbss`       | 42,876 | 230 Marker Record, 230 Record | 138 to 277, 184 on average |
| 2      | 3473 and later | 3474    | `worldmapmonsteroffset.dbss` | 2,304  | 230 Offset Row                | 10                         |
| 1      | 1784           | 1784    | `worldmapmonster.dbss`       | 20,586 | 127 Marker Record, 127 Record | 124 to 274, 160 on average |
| 1      | 1784           | 1784    | `worldmapmonsteroffset.dbss` | 1,274  | 127 Offset Row                | 10                         |

| Layout | File                         | Known            | Unknown        |
| ------ | ---------------------------- | ---------------- | -------------- |
| 2      | `worldmapmonster.dbss`       | 39,426 B (92.0%) | 3,450 B (8.0%) |
| 2      | `worldmapmonsteroffset.dbss` | 2,304 B (100.0%) | 0 B (0.0%)     |
| 1      | `worldmapmonster.dbss`       | 19,570 B (95.1%) | 1,016 B (4.9%) |
| 1      | `worldmapmonsteroffset.dbss` | 1,274 B (100.0%) | 0 B (0.0%)     |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                 |
| ---------------------------- | -------- | -------------------------------------------------------------------- |
| `worldmapmonsteroffset.dbss` | Required | Bare u16-keyed index: marker key -> record offset and size           |
| `languagedata_en.loc`        | Optional | LOC type 40, `str_id1` = key, `str_id4` 0 / 1 / 2 = name / line 1 / line 2 |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                          |
| ------- | ------------- | ------- | ------------------------------ |
| `+0x00` | u32           | count   | Same count as the offset table |
| `+0x04` | Record[count] | records | See Record                     |

### Record (variable: 2 bytes + marker text)

Each record is preceded by a copy of its u16 key. The offset of a row points
past that preceding copy, at the record's own key.

| Offset  | Type          | Field      | Notes                                                    |
| ------- | ------------- | ---------- | -------------------------------------------------------- |
| `+0x00` | u16           | key_prefix | Copy of the marker's `key`                               |
| `+0x02` | Marker Record | marker     | `size` bytes of the offset row; the offset row points here |

### Marker Record (variable: 69 bytes + text)

Strings are a u64 unit count followed by the text, with no terminator: UTF-16LE
for the wide ones, ASCII for the icon path (`RecordReader`).

| Offset             | Type   | Field        | Notes                                                                 |
| ------------------ | ------ | ------------ | --------------------------------------------------------------------- |
| `+0x00`            | u16    | key          | Same as the offset row                                                |
| `+0x02`            | str16  | line1_kr     | First label line: a level range (`Lv 12~15`), a recommended AP, or a category (`월드 우두머리`, world boss) |
| `line1_kr+0x00`    | str16  | line2_kr     | Second label line: the final AP, or the same text as line 1 (142 records) |
| `line2_kr+0x00`    | str16  | name_kr      | Zone or boss name                                                     |
| `name_kr+0x00`     | f32[3] | position     | World position; the second value is the height                        |
| `name_kr+0x0C`     | str8   | icon         | Marker illustration relative to `ui_texture/`; empty on the 16 Abyssal Wells |
| `icon+0x00`        | str16  | condition    | Condition script, empty on 165 records (`getknowledge(10497);`, `!checkFieldType(hadumField);`, `getlevel()>59;`) |
| `condition+0x00`   | str16  | unknown_str  | Always empty                                                          |
| `unknown_str+0x00` | i32    | unknown_ref  | `-1` on 120 records; on hunting zones the drop window hunting ground ID, see Notes |
| `unknown_str+0x04` | u8     | unknown_kind | 0 to 4, groups the markers; see Open Questions                        |
| `unknown_str+0x05` | u8     | unknown_flag | Always `1`                                                            |
| `unknown_str+0x06` | u8     | unknown_end  | Always `0`                                                            |

### `worldmapmonsteroffset.dbss`

No magic and no trailer (`parse_bare_offset_rows()`).

| Offset  | Type              | Field | Notes                              |
| ------- | ----------------- | ----- | ---------------------------------- |
| `+0x00` | u32               | count | Number of rows; 229 on client 3458 |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                     |

The rows are not in file order: they interleave the regular keys (1 to 249)
with the 20 keys from 10001 to 10020, both counting down.

### Offset Row (10 bytes)

| Offset  | Type | Field  | Notes                                                       |
| ------- | ---- | ------ | ----------------------------------------------------------- |
| `+0x00` | u16  | key    | Marker key                                                  |
| `+0x02` | u32  | offset | Start of the marker record in `worldmapmonster.dbss`, past the key copy |
| `+0x06` | u32  | size   | Length of the marker record, the key copy left out          |

## Layout 1

On client 1784 a Marker Record held one label line: the zone or boss name
followed `line1_kr` directly, without `line2_kr`, and the record ended after
`unknown_str`, without `unknown_ref`, `unknown_kind`, `unknown_flag` and
`unknown_end`. Only the Marker Record differs from Layout 2. On client 1784
the file holds 127 records.

### Marker Record (variable: 54 bytes + text)

| Offset           | Type   | Field       | Notes                             |
| ---------------- | ------ | ----------- | --------------------------------- |
| `+0x00`          | u16    | key         |                                   |
| `+0x02`          | str16  | line1_kr    |                                   |
| `line1_kr+0x00`  | str16  | name_kr     |                                   |
| `name_kr+0x00`   | f32[3] | position    |                                   |
| `name_kr+0x0C`   | str8   | icon        |                                   |
| `icon+0x00`      | str16  | condition   |                                   |
| `condition+0x00` | str16  | unknown_str | Empty on every record on client 1784 |

## Notes

- All 229 records walk to exactly their offset-table size with the layout
  above on client 3458.
- The markers are the world map monster icons the drop item window links to
  (`window/dropitem/panel_window_renewdropitem_all_1` registers
  `FromClient_Worldmap_LinkedDropUI_MouseOn` / `MouseOut` / `MouseClick` for
  them).
- LOC type 40 names all 229 markers and has both label lines for each.
- All 191 distinct icons exist once resolved under `ui_texture/` and
  lowercased: `combine/etc/worldmapboss/` for the zone and boss art,
  `combine/icon/` for the portal, sanctum, Griffon platform and Sea Palace
  markers, and
  `combine/etc/combine_etc_ocean_change02.dds` for the Margoria sea markers.
- The `unknown_kind` groups on client 3458: `0` hunting zones (161, the level
  and AP labels), `1` Abyssal Wells (16, no icon), `2` Black Shrine bosses
  (17), `3` the keys from 10001 (20, Pilgrim's Sanctum and the Offering Site
  markers, whose icons are named `Combine_WorldMap_HardcoreServer_*`; the drop
  item window checks `ToClient_HardCoreChannelWithContensOption`), `4` world, field and hunting field bosses (15).
- On hunting zones (`unknown_kind` 0) `unknown_ref` is the hunting ground ID
  of [`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md), the drop item window's hunting ground
  table. All 92 hunting zones that set it point at the row of the same place
  on client 3458: 87 by name (`바실리스크 소굴` -> hunting ground 35,
  `바실리스크 소굴`), the other five under another name for that place
  (`하스라 고대 유적` -> `하스라 절벽`, `트롤 서식지` -> `귄트 언덕 [엘비아]`,
  `시크라이아 해저 유적` -> `시크라이아 유적 상층부`, `카드리 무리` ->
  `카드리 폐허`, `외눈박이 거인` -> `외눈박이 땅 [데키아의 등불]`). The other 69
  hunting zones store `-1`: the older level-range markers that a newer AP
  marker replaced (Biraghi Den is key 8 with `-1` and key 115 with hunting
  ground 62), the sea zones (Margoria, sea monster habitats), the god and
  demonlord markers, and a few single zones such as Lyngbakr Habitat and the
  Griffon Stations. Field name kept as `unknown_ref` because it means something else
  on the Black Shrine markers (`unknown_kind` 2): `1` to `9` on the nine
  Black Shrine bosses and `0` on the eight Land of the Morning Light world
  and party bosses.
- The drop window groups those hunting grounds the way Garmoth's grind spot
  list does: a region tab per row (13 tabs, Balenos to Inner Edania) and the
  filters of `dropuisubcategoryinfo.bss` (`파티 사냥터` party, `엘비아의 영역`
  Elvia, `마르니의 밀실` Marni's Realm, `데키아의 등불` and `데키아의 등불 II`
  Dehkia, `추천` recommended, `지역 의뢰` regional requests). Every Garmoth
  grind spot found here by name (58 of its 95) is an `unknown_kind` 0 marker
  with a hunting ground.
- The app indexes the marker illustrations by key
  (`IndexKind.WORLDMAP_MARKER_ICON`, read through `IconKind.WORLDMAP_MARKER`);
  the 16 Abyssal Wells store none and are left out.

## Open Questions

### What does `unknown_ref` hold on Black Shrine markers?

On hunting zones it is the drop window hunting ground (see Notes). The 17
Black Shrine markers use `0` to `9` instead, `0` on the Land of the Morning
Light world and party bosses and `1` to `9` once each on the Black Shrine
bosses, which reads like a boss order or difficulty step; nothing names it.

### What names the `unknown_kind` values?

The five values line up with the marker groups in Notes, and `0` is at least
the hunting zones: every marker with a drop window hunting ground is `0`. No
Lua enum or string names the values, and the world map code that reads the
file is engine side. Garmoth's grind spot list only covers hunting zones, so
it names none of the others.
