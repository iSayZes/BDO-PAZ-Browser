# `groupcameradata.bss` Format

## Purpose

The summaries shown when a story cutscene is skipped: one fixed 28-byte row per
cutscene with its title, a short recap, a quoted line and a region symbol icon,
all as indices into a shared string table. The Korean text is the source; LOC
type 97 holds the translations.

Example:

```text
scene 65, SymbolIcon_Valenos.dds
  title        환송                -> "Send Off"
  description  엠마는 벨리아 ...    -> "Emma stood by the old wharf in Velia ..."
  quote        "저... 모험가님 ..." -> "\"Adventurer... if it's alright with you, ...\""
```

## Companion Files

| File                  | Required | Role                                                                   |
| --------------------- | -------- | ---------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | LOC type 97, `str_id1` = `scene_id`, `str_id4` 0 / 1 / 2 = title / description / quote |

All multi-byte values are little-endian.

## File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset           | Type    | Field        | Notes                                                            |
| ---------------- | ------- | ------------ | ---------------------------------------------------------------- |
| `+0x00`          | char[4] | magic        | ASCII `PABR`                                                     |
| `+0x04`          | u32     | count        | Number of rows; 92 on client 3458                                |
| `+0x08`          | row[]   | rows         | 28-byte rows repeated `count` times                              |
| `8 + count * 28` | table   | string_table | u32 count, then `count` x (u8 is_wide, u32 byte length, payload) |
| EOF - 8          | u32     | table_start  | Offset of the string table, where the rows end                   |
| EOF - 4          | u32     | zero         | Always 0                                                         |

Rows are not sorted by ID (the first three are 65, 66 and 2).

## Record Structure

### Cutscene Row (28 bytes, repeated `count` times)

| Offset  | Type  | Field           | Notes                                                             |
| ------- | ----- | --------------- | ----------------------------------------------------------------- |
| `+0x00` | u32   | scene_id        | Unique; 2 to 260 on client 3458, with gaps                        |
| `+0x04` | u32   | title_ref       | String table index of the Korean title                            |
| `+0x08` | u32   | description_ref | String table index of the Korean recap, with stored line breaks   |
| `+0x0C` | u32   | quote_ref       | String table index of the Korean quoted line                      |
| `+0x10` | u32   | icon_ref        | String table index of the region symbol, relative to `ui_texture/` |
| `+0x14` | u8[8] | unknown_14      | Always `0`                                                        |

### String Table

251 strings on client 3458, all referenced. Scenes that repeat a summary
share its entries: 43 to 47, 197 and 198, and 253 to 256 share their title,
recap and quote, 248 and 249 their title and quote, and 257 to 260 their
title. The four icons are stored once each.

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
