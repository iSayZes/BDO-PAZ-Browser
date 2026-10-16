# `questjournalvideoinfo.bss` Format

## Purpose

The video pages of the Land of the Morning Light journal: one fixed 13-byte
row per quest with a Bink video name and a full-size artwork image, both as
indices into a shared string table. The journal book shows the artwork on the
quest's page and plays the video from it.

Example:

```text
quest 8700 / 11 ([Storybook] Tale of the Mudang Wraith)
  video_ref   -> MorningLand/MorningLand_Boss_03_02
                 ui_movie/pc/morningland/morningland_boss_03_02.bk2
  artwork_ref -> Icon/Quest/MorningLand_Boss_03_02_Full.dds
```

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest titles, LOC type 18 keyed by (`quest_chain_id`, `quest_id`)    |

All multi-byte values are little-endian.

## File Layout

The shared PABR string table layout of `buffsimply.bss` and
`specialenchantitem.bss` (`_common/pabr_strings.py`).

| Offset           | Type    | Field        | Notes                                                            |
| ---------------- | ------- | ------------ | ---------------------------------------------------------------- |
| `+0x00`          | char[4] | magic        | ASCII `PABR`                                                     |
| `+0x04`          | u32     | count        | Number of rows; 80 on client 3458                                |
| `+0x08`          | row[]   | rows         | 13-byte rows repeated `count` times                              |
| `8 + count * 13` | table   | string_table | u32 count, then `count` x (u8 is_wide, u32 byte length, payload) |
| EOF - 8          | u32     | table_start  | Offset of the string table, where the rows end                   |
| EOF - 4          | u32     | zero         | Always 0                                                         |

The rows are grouped by quest chain but in no sorted order: chains 8700 to
8714 come first, then 8542 to 8554, and sub IDs run up in some chains and down
in others.

## Record Structure

### Journal Video Row (13 bytes, repeated `count` times)

| Offset  | Type | Field          | Notes                                                                  |
| ------- | ---- | -------------- | ---------------------------------------------------------------------- |
| `+0x00` | u16  | quest_chain_id | Quest chain (main ID), 8542 to 8554 and 8700 to 8714 on client 3458    |
| `+0x02` | u16  | quest_id       | Quest within the chain (sub ID); `quest_id << 16 \| quest_chain_id` is the packed quest ID of `allquestlist.bss` |
| `+0x04` | u32  | video_ref      | String table index of the video name, relative to `ui_movie/pc/`, no extension |
| `+0x08` | u32  | artwork_ref    | String table index of the artwork path, relative to `ui_texture/`       |
| `+0x0C` | u8   | unknown_0c     | Always `1`                                                             |

### String Table

158 strings on client 3458, all referenced, never shared between a video and
an artwork entry. Two videos are used by two quests each
(`MorningLandPT2_Sub_8527_8_01` by 8550/4 and 8550/5,
`MorningLandPT2_Sub_8541_1_01` by 8554/2 and 8554/3); every artwork path is
used once.

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
the file tells them apart.
