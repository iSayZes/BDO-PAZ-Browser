# `stringtable.bss` Format

## Purpose

The Korean source of the client's keyed UI strings. Each row pairs a string key
(`LUA_WIDGET_TOWNNPCNAVI_NPCTYPETEXT_6`) with its Korean text and a 32-bit key
hash. The hash is the LOC type `37` `str_id1`, so this file is how a key the
client scripts use turns into the translated text in `languagedata_*.loc`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                       |
| --------------------- | -------- | ---------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Translated text, type `37` keyed by the row hash and sheet |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

A PABR file of eight sheets, followed by the same counted string table and
8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings). Every
string in the table is UTF-16LE (`is_wide=1`).

| Offset              | Type               | Field              | Notes                                                |
| ------------------- | ------------------ | ------------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]            | magic              | ASCII `PABR`                                         |
| `+0x04`             | u32                | sheet_count        | `8` on client 3458                                   |
| `+0x08`             | Sheet[sheet_count] | sheets             | Sheets back to back, see Sheet                       |
| `sheets+0x00`       | String Table       | string_table       | See String Table                                     |
| `string_table+0x00` | u32                | string_table_start | Where the last sheet ends (`0xC6DD8` on client 3458) |
| `string_table+0x04` | u32                | zero               | Always `0`                                           |

### Sheet (variable: 12 bytes + rows)

A 12-byte sheet header, then the sheet's rows.

| Offset  | Type                  | Field      | Notes                                                          |
| ------- | --------------------- | ---------- | -------------------------------------------------------------- |
| `+0x00` | u32                   | sheet_hash | Key hash of the sheet name (see Key Hash)                      |
| `+0x04` | u32                   | name_ref   | String table index of the sheet name (`GAME`, `RESOURCE`, ...) |
| `+0x08` | u32                   | row_count  | Number of 16-byte rows that follow                             |
| `+0x0C` | String Row[row_count] | rows       | See String Row                                                 |

### String Row (16 bytes)

| Offset  | Type | Field      | Notes                                                                  |
| ------- | ---- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | key_hash   | Key hash of the key string (see Key Hash); the LOC type `37` `str_id1` |
| `+0x04` | u32  | key_ref    | String table index of the key, e.g. `NPCSHOP_BUY`                      |
| `+0x08` | u32  | value_ref  | String table index of the Korean text; never empty, 7 are one space    |
| `+0x0C` | u32  | unknown_0c | Always `0`                                                             |

Rows are not sorted by hash or key. The string table is interned: each string
is stored once, in the order the sheets first use it (sheet name, then key
and value of each row), and later uses point back. No key repeats within a
sheet; 6,553 values reuse an earlier text such as `"확인"`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `95,195` strings on client 3458       |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries, all UTF-16LE     |

## Key Hash

`key_hash` and `sheet_hash` are Bob Jenkins' lookup3 `hashlittle()` over the
UTF-16LE string without a terminator, seed `0xC5EDE`:
`LUA_GROWTHPASS_WIDGET_ICON_NOTICE_NEW_DESC` -> `1517777731`, `GAME` ->
`3183609639`. It matches all 50,992 key hashes and all 8 sheet hashes on
client 3464 (`test_every_key_hash_is_the_key_hash_of_its_key` and
`test_every_sheet_hash_is_the_key_hash_of_its_name`). The same function keys
the LOC type 59 TextBind texts (see `languagedata_loc.md`, Type 59). The
browser computes it with `key_hash()` in `_common/string_hash.py`.

## Sheets

The sheet order is fixed on client 3458. `loc str_id2` is the LOC type `37`
`str_id2` that every LOC row of that sheet's keys carries.

| # | Name          | Hash         | Rows   | `loc str_id2` | Holds                                                      |
| - | ------------- | ------------ | ------ | ------------- | ---------------------------------------------------------- |
| 0 | `GAME`        | `0xBDC20727` | 22,936 | `1`           | Lua UI strings (`LUA_*`, `WEBHELPER_*`), labels and tooltips |
| 1 | `SymbolNo`    | `0xA9B8EA3C` | 4,529  | `6`           | Server error and result messages (`eErrNo*`)               |
| 2 | `IMAGESLIDE`  | `0x8AD0A01B` | 204    | `7`           | Image slide subtitles (`SEQUENCE_SUBTITLE_IMAGE_SLIDE_*`)  |
| 3 | `ACTIONCHART` | `0x138A8C63` | 2,000  | `3`           | Speech bubbles and action lines (`Bubble_*`, `Trade_*`)     |
| 4 | `RESOURCE`    | `0x9C44332D` | 9,525  | `2`           | UI panel resources (`PANEL_*`)                             |
| 5 | `CUTSCENE`    | `0x08342431` | 8,564  | `0`           | Cutscene subtitles (`CS_*`)                                |
| 6 | `TOOL`        | `0xE09F9402` | 785    | `4`           | Enum labels (`eSymNo*`), e.g. chat types, log reasons      |
| 7 | `WEB`         | `0xA5AA1B9E` | 2,360  | `5`           | In-game web page strings (`WEB_*`)                         |

This settles which LOC type `37` `str_id2` is which sheet (the old
"Type 37 sheet names" question in
[`languagedata_loc.md`](languagedata_loc.md)).

## LOC Join

Look up a key's translated text as LOC type `37`, `str_id1 = key_hash`,
`str_id2 = ` the sheet's `loc str_id2`, `str_id3 = 0`, `str_id4 = 0`.

- 50,779 of the 50,903 rows have a LOC row on client 3458. The other 124
  (62 `GAME`, 33 `CUTSCENE`, 17 `RESOURCE`, 12 `SymbolNo`) have Korean text
  only; they read like newer content not yet translated, so fall back to
  the Korean `value_ref` text.
- 44 keys sit in two sheets (`NPCSHOP_BUY` in `GAME` and `RESOURCE`). Both
  rows carry the same hash and share the key string, and LOC keeps them
  apart by `str_id2`, which can hold different text (`ALCHEMY_MANUFACTURE_BTN_MANUFACTURE`:
  `GAME` "Start", `RESOURCE` "Start Crafting"). So the hash depends on the
  key alone, not on the sheet.
- 3,027 LOC type `37` `str_id1` values have no row here; keys dropped from
  the client whose translations LOC still carries.
- 352 LOC rows use `str_id3 = 1` as a second variant of a key, mostly
  regional URLs (`WEBHELPER_*_EN`) and date lines (`*_GMT`, `*_UTC`). 164 keys
  have only the `str_id3 = 1` row, so a lookup should try `str_id3 = 0` first
  and then `1`. `str_id4` is always `0`.

### Town NPC Navigation Types

The `GAME` sheet holds the town NPC navigation labels as
`LUA_WIDGET_TOWNNPCNAVI_NPCTYPETEXT_1` to `_39`, one per number with no gaps.
The client picks them by `SpawnType`, and the suffix is not always the
`SpawnType` value; the full mapping is the Navi label column of
[`characterspawntype.dbss` SpawnType](characterspawntype_dbss.md#spawntype).
A few, as the English LOC text:

| Key suffix | Korean        | English (LOC)              | SpawnType          |
| ---------- | ------------- | -------------------------- | ------------------ |
| `_1`       | 기술 교관     | Skill Instructor           | `SkillTrainer` (1) |
| `_6`       | 창고          | Storage                    | `WareHouse` (6)    |
| `_25`      | 아이템 거래소 | Central Market             | `ItemMarket` (25)  |
| `_35`      | 악기 상인     | Instruments                | `Instrument` (40)  |
| `_39`      | 황실제작 납품 | Imperial Crafting Delivery | `SupplyShop` (33)  |

The client reads these through `PAGetString(Defines.StringSheet_GAME, key)`,
so a script's `StringSheet_<name>` picks the sheet and with it the LOC
`str_id2`.

## Notes

- Seven `GAME` values are a single space (`LUA_JOIN_LOCALWAR_RULE7`,
  `LUA_LOCALWARINFO_DESC_RULETEXT_9` and others on client 3458), unused rule
  and condition lines; the table shows them as a dash when LOC has no text.
- Some values forward to another text rather than holding it, e.g.
  `ALCHEMY_COOK_TEXT_DESCRPITION` = `{TextBind:TEXTBIND_ALCHEMY_COOK_TEXT_DESCRPITION}`,
  and the LOC text keeps the same placeholder. The text it names is LOC type
  59, keyed by the key hash of the name (`languagedata_loc.md`, Type 59), or
  the Korean `textbind.dbss` record of that key. The Text column shows it
  filled; the Korean column keeps the value as stored. 460 values hold a
  placeholder on client 3464. Values also carry `<PAColor...>` tags and
  `{name}` placeholders.
- bdo-data-extractor names the sheets `GAME`, `RESOURCE`, `ACTIONCHART` and
  others; the names are stored in this file, so that part is now confirmed.

## Open Questions

### `str_id3 = 1` Variants

352 LOC type `37` rows use `str_id3 = 1`. Most look like a second,
region-specific text of the key (a newer URL, a UTC instead of GMT date line),
but some keys have only the `str_id3 = 1` row. Which condition makes the client
pick variant `1` is not known.
