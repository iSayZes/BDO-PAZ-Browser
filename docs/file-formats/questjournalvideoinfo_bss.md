# `questjournalvideoinfo.bss` Format

## Purpose

The video pages of the Land of the Morning Light journal: one fixed 13-byte
row per quest with a Bink video name and a full-size artwork image, both as
indices into a shared string table. The journal book shows the artwork on the
quest's page and plays the video from it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records              | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | -------------------- | --------- |
| 1      | 2519 and later | 3474    | `questjournalvideoinfo.bss` | 7,687 | 80 Journal Video Row | 13        |

| Layout | File                        | Known           | Unknown     |
| ------ | --------------------------- | --------------- | ----------- |
| 1      | `questjournalvideoinfo.bss` | 7,607 B (99.0%) | 80 B (1.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 keyed by (`quest_chain_id`, `quest_id`)    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset              | Type                     | Field        | Notes                                          |
| ------------------- | ------------------------ | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]                  | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                      | count        | Number of rows; 80 on client 3458              |
| `+0x08`             | Journal Video Row[count] | rows         | 13-byte rows repeated `count` times            |
| `rows+0x00`         | String Table             | string_table | See String Table                               |
| `string_table+0x00` | u32                      | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                      | zero         | Always 0                                       |

The rows are grouped by quest chain but in no sorted order: chains 8700 to
8714 come first, then 8542 to 8554, and sub IDs run up in some chains and down
in others.

### Journal Video Row (13 bytes)

| Offset  | Type | Field          | Notes                                                                  |
| ------- | ---- | -------------- | ---------------------------------------------------------------------- |
| `+0x00` | u16  | quest_chain_id | Quest chain (main ID), 8542 to 8554 and 8700 to 8714 on client 3458    |
| `+0x02` | u16  | quest_id       | Quest within the chain (sub ID); `quest_id << 16 \| quest_chain_id` is the packed quest ID of `allquestlist.bss` |
| `+0x04` | u32  | video_ref      | String table index of the video name, relative to `ui_movie/pc/`, no extension |
| `+0x08` | u32  | artwork_ref    | String table index of the artwork path, relative to `ui_texture/`       |
| `+0x0C` | u8   | unknown_0c     | Always `1`                                                             |

### String Table (variable: 4 bytes + strings)

158 strings on client 3458, all referenced, never shared between a video and
an artwork entry. Two videos are used by two quests each
(`MorningLandPT2_Sub_8527_8_01` by 8550/4 and 8550/5,
`MorningLandPT2_Sub_8541_1_01` by 8554/2 and 8554/3); every artwork path is
used once.

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | 158 on client 3458                        |
| `+0x04` | pstr[string_count] | strings      | u8 is_wide, u32 byte length, then payload |

## Notes

- The journal book scripts (`window/achievement/panel_window_journal_book_all`
  and `panel_window_achievement_morningland_1`) ask
  `ToClient_IsExistJournalVideoData(questNo)` for a page's quest, mark it as a
  video page, and draw the artwork through
  `ToClient_ChangeQuestIconFromIconPath` into `_stc_artworkImage`.
- Every row's quest has a `quest.dbss` icon (`QUEST_ICON`), and in 74 of 80
  the artwork is that icon's full-size version: the same name with `_Full`
  added (`morningland_boss_03_02.dds` -> `MorningLand_Boss_03_02_Full.dds`).
  The other six use a different name (8551/3 shows `8551_4_Full.dds`;
  8543/9 has the icon `morninglandpt2_boss_8543_1.dds` but the artwork
  `MorningLandPT2_Boss_8534_1_Full.dds`). The app indexes the artwork by packed quest ID
  (`IndexKind.QUEST_ARTWORK_ICON`, read through `IconKind.QUEST_ARTWORK`),
  apart from the quest icons: it is a page illustration, not the quest's
  icon, so `QUEST_ICON` keeps its own paths.
- On client 3458 all 80 videos exist as `ui_movie/pc/<video>.bk2` (lowercased),
  each with a `.srt` subtitle file beside it and `_de_`, `_fr_` and `_sp_`
  subtitle variants; the voice banks are `sound2022/windows/<language>/bink_<name>.bnk`.
  All 80 artwork files exist.
- All 80 quests have a LOC type 18 title, all `[Storybook] ...`.

## Open Questions

### What does `unknown_0c` hold?

It is `1` in all 80 rows. It may be an "enabled" flag or a page kind for
the journal book, but with a single value on the current client nothing in
the file tells them apart. The client 1784 private server sources name
nothing here: its `binary/` folder has no `questjournalvideoinfo.bss`, its
server dump has no `Video` string, and its sheets have no video or artwork
sheet (`Quest_Journal` is the [`journalquest.dbss`](journalquest_dbss.md)
source).
