# `groupcameradata.bss` Format

## Purpose

The summaries shown when a story cutscene is skipped: one fixed 28-byte row per
cutscene with its title, a short recap, a quoted line and a region symbol icon,
all as indices into a shared string table. The Korean text is the source; LOC
type 97 holds the translations.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes  | Records                                 | Row bytes |
| ------ | -------------- | ------- | --------------------- | ------ | --------------------------------------- | --------- |
| 2      | 3473 and later | 3473    | `groupcameradata.bss` | 25,147 | 92 Cutscene Row                         | 28        |
| 1      | 1784           | 1784    | `groupcameradata.bss` | 12,760 | 6 Cutscene Row, 170 Line, 12 Line Group | 16        |

| Layout | File                  | Known            | Unknown         |
| ------ | --------------------- | ---------------- | --------------- |
| 2      | `groupcameradata.bss` | 24,411 B (97.1%) | 736 B (2.9%)    |
| 1      | `groupcameradata.bss` | 11,400 B (89.3%) | 1,360 B (10.7%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                   |
| --------------------- | -------- | ---------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | LOC type 97, `str_id1` = `scene_id`, `str_id4` 0 / 1 / 2 = title / description / quote |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset              | Type                | Field        | Notes                                          |
| ------------------- | ------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]             | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                 | count        | Number of rows; 92 on client 3458              |
| `+0x08`             | Cutscene Row[count] | rows         | See Cutscene Row                               |
| `rows+0x00`         | String Table        | string_table | See String Table                               |
| `string_table+0x00` | u32                 | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                 | zero         | Always 0                                       |

Rows are not sorted by ID (the first three are 65, 66 and 2).

### Cutscene Row (28 bytes)

| Offset  | Type     | Field           | Notes                                                             |
| ------- | -------- | --------------- | ----------------------------------------------------------------- |
| `+0x00` | u32      | scene_id        | Unique; 2 to 260 on client 3458, with gaps                        |
| `+0x04` | u32      | title_ref       | String table index of the Korean title                            |
| `+0x08` | u32      | description_ref | String table index of the Korean recap, with stored line breaks   |
| `+0x0C` | u32      | quote_ref       | String table index of the Korean quoted line                      |
| `+0x10` | u32      | icon_ref        | String table index of the region symbol, relative to `ui_texture/` |
| `+0x14` | bytes[8] | unknown_14      | Always `0`                                                        |

### String Table (variable: 4 bytes + strings)

251 strings on client 3458, all referenced. Scenes that repeat a summary
share its entries: 43 to 47, 197 and 198, and 253 to 256 share their title,
recap and quote, 248 and 249 their title and quote, and 257 to 260 their
title. The four icons are stored once each.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 251 on client 3458  |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Layout 1

Client 1784 rows are 20 bytes, without `unknown_14`, and a second table of
timed voice lines follows the rows, before the string table. Only the File
Layout and the Cutscene Row differ from Layout 2; Line Group and Line exist
only here. The parser reads only Layout 2.

### File Layout

| Offset             | Type                         | Field            | Notes                                                 |
| ------------------ | ---------------------------- | ---------------- | ----------------------------------------------------- |
| `+0x00`            | char[4]                      | magic            | ASCII `PABR`                                          |
| `+0x04`            | u32                          | count            | Number of rows; 6 on client 1784                      |
| `+0x08`            | Cutscene Row[count]          | rows             | See Cutscene Row                                      |
| `rows+0x00`        | u32                          | line_group_count | 12 on client 1784                                     |
| `rows+0x04`        | Line Group[line_group_count] | line_groups      | See Line Group                                        |
| `line_groups+0x00` | String Table                 | string_table     | See String Table                                      |
| `EOF-0x08`         | u32                          | table_start      | Offset of the string table, where the line groups end |
| `EOF-0x04`         | u32                          | zero             | Always 0                                              |

### Line Group (variable: 4 bytes + lines)

2 to 36 lines per group on client 1784.

| Offset  | Type             | Field      | Notes            |
| ------- | ---------------- | ---------- | ---------------- |
| `+0x00` | u32              | line_count | Number of lines  |
| `+0x04` | Line[line_count] | lines      | See Line         |

### Line (16 bytes)

| Offset  | Type | Field      | Notes                                                                                           |
| ------- | ---- | ---------- | ----------------------------------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00 | 1 to 15 on client 1784, the same value in every line of a group and unique per group; 1 to 5 and 14 are also `scene_id` values of the rows |
| `+0x04` | u32  | unknown_04 | Rises within a group in steps of thousands (0 to 165000), a time in milliseconds by its values  |
| `+0x08` | u32  | voice_ref  | String table index of a voice key (`QUEST_VCE_NEW_9027_43_1_Illezra`, `NPC_VCE_NEW_0_0_Mute_1`) |
| `+0x0C` | u32  | line_ref   | String table index of the Korean line spoken                                                    |

### Cutscene Row (20 bytes)

| Offset  | Type | Field           | Notes |
| ------- | ---- | --------------- | ----- |
| `+0x00` | u32  | scene_id        |       |
| `+0x04` | u32  | title_ref       |       |
| `+0x08` | u32  | description_ref |       |
| `+0x0C` | u32  | quote_ref       |       |
| `+0x10` | u32  | icon_ref        | String table index of the icon path; on client 1784 also quest icons (`Icon/Quest/405_1.dds`) |

## Notes

- The cutscene skip panel (`window/cutscene/panel_window_cutsceneskip_1`)
  opens in `eRenderMode_GroupCamera` and fills its title, main text, sub text
  and territory icon from `getTitle`, `getMainDescription`,
  `getSubDescription` and `getIconPath`, the four strings of a row.
- The icons mark the story region. On client 3458:
  `SymbolIcon_SnowMountain.dds` (Drieghan, 40 scenes),
  `SymbolIcon_AbyssOne.dds` (The Magnus, 19), `SymbolIcon_Valenos.dds`
  (Balenos, 18) and `SymbolIcon_Feather.dds` (Atoraxxion, 15). All four
  exist under `ui_texture/combine/icon/symbolicon/`.
- The app indexes the region icons by scene ID (`IndexKind.CUTSCENE_ICON`,
  read through `IconKind.CUTSCENE`).
