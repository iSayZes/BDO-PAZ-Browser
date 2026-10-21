# `olviaacademyseasonss.bss` Format

## Purpose

The current Olvia Academy class (season): its number, four Unix times, the
enrollment and graduation quests and the class title. The file holds one
class only, the one running on the client it ships with: class 3 on client
3474 (2026-07-30 to 2026-11-12), class 1 on client 3251. It has no PABR
magic and no string table. The quest lists of the same academy are in
[`olviaacademy*questlist.bss`](olviaacademyquestlist_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ------- | --------- |
| 1      | 3251 and later | 3474    | `olviaacademyseasonss.bss` | 48    | -       | -         |

| Layout | File                       | Known         | Unknown    |
| ------ | -------------------------- | ------------- | ---------- |
| 1      | `olviaacademyseasonss.bss` | 48 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | No file  |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names both quests with their LOC type 18 titles and the
title with its LOC type 1 name from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type | Field            | Notes                                                                     |
| ------- | ---- | ---------------- | ------------------------------------------------------------------------- |
| `+0x00` | u32  | season_no        | Class number; `3` on client 3474, `1` on client 3251                      |
| `+0x04` | u64  | start_time       | Unix seconds; enrollment opens, `2026-07-30 09:00 UTC` on client 3474     |
| `+0x0c` | u64  | graduation_time  | Unix seconds; graduation opens, `2026-11-05 09:00 UTC` on client 3474     |
| `+0x14` | u64  | close_time       | Unix seconds; enrollment closes, `2026-08-20 09:00 UTC` on client 3474    |
| `+0x1c` | u64  | end_time         | Unix seconds; graduation and the class end, `2026-11-12 09:00 UTC` on client 3474 |
| `+0x24` | u32  | enter_quest      | Packed quest ID `(quest_id << 16) \| quest_chain_id`; `2308/1` "[Olvia Academy] Your First Steps In" |
| `+0x28` | u32  | graduation_quest | Packed quest ID; `2309/1` "[Olvia Academy] Graduation with Honor"         |
| `+0x2c` | u32  | title_id         | Class title, LOC type 1; `3687` "Olvia Academy Class 3" on client 3474    |

The fields fill the 48-byte file exactly.

## Field Names

No reference source has the file: it first appears on client 3251 (absent
on client 3002), and a private server's `DataSheets.bexcel` on client 1784
has no sheet with `Olvia` or `Academy` in its name. The names come from the
client Lua and LOC of client 3474:

- `season_no`: the Lua reads `ToClient_GetOlviaAcademyCurrentSeasonNo()`
  into `seasonNo` for the invitation letter (`LUA_OLVIAACADEMY_INVITATION_MESSAGE`,
  "Class {seasonNo} Enrollment Period"), the pass window and
  `panel_widget_localquestalert_1.luac` (`olviaAcademySeasonNo`). The value
  matches `title_id` on both clients: `1` with title `3685` "Olvia Academy
  Class 1" on client 3251, `3` with title `3687` "Olvia Academy Class 3" on
  client 3474 (title `3686` is "Olvia Academy Class 2").
- The four times: `panel_window_olviaacademy_main_all_1.luac` reads
  `ToClient_GetOlviaAcademyStartTime()`, `...CloseTime()`,
  `...GraduateTime()` and `...EndTime()` and fills
  `LUA_OLVIA_ACADEMY_MAINPAGE_SEASON_ENTER` ("Enrolled: {starttime} after
  maintenance - {closetime} before maintenance") and
  `LUA_OLVIA_ACADEMY_MAINPAGE_SEASON_GRADUATION` ("Graduation:
  {gradutiontime} after maintenance - {endtime} before maintenance").
  Enrollment closes before graduation opens, so the four times order as
  `start_time` <= `close_time` < `graduation_time` <= `end_time`. That order
  fits the stored values one way only on both clients: `+0x04` is the
  earliest (`start_time`), `+0x14` the second (`close_time`), `+0x0c` the
  third (`graduation_time`) and `+0x1c` the latest (`end_time`). The file
  stores them as start, graduation, close, end.
- `enter_quest`: `PaGlobalFunc_OlviaAcademy_Main_Open`
  (`panel_window_olviaacademy_main_all_2.luac`) reads
  `ToClient_GetOlviaAcademyEnterQuestNo()` and opens the window only when
  that quest is cleared. The LOC text of quest 4472/1 says to "complete
  "[Olvia Academy] Your First Steps In" to enroll", which is `2308/1`.
- `graduation_quest`: no Lua reads it. Its quest `2309/1` is "[Olvia
  Academy] Graduation with Honor" ("attend the graduation ceremony, and
  claim your glorious diploma").

## Notes

- Raw bytes on client 3474: `03 00 00 00 90 12 6B 6A 00 00 00 00 90 45 EC 6A
  00 00 00 00 10 C2 86 6A 00 00 00 00 10 80 F5 6A 00 00 00 00 04 09 01 00
  05 09 01 00 67 0E 00 00`.
- Client 3251 holds class 1 in the same 48 bytes: `start_time`
  `2026-01-22`, `graduation_time` `2026-04-09`, `close_time` `2026-02-12`,
  `end_time` `2026-04-16` (all 09:00 UTC), the same two quests and title
  `3685`. On both clients every time is a Thursday at 09:00 UTC,
  enrollment runs 3 weeks and graduation the last week. Class 1 runs 12
  weeks, class 3 runs 15.
- The two quests are the only quests of chains 2308 and 2309 in
  `olviaacademycurriculumquestlist.bss`.
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`. It shows the times as UTC date and time and the quests as
  `chain/quest` with their titles; the record keeps the stored values.
- Siblings without a doc yet: `olviaacademycurriculumss.bss` and
  `olviaacademypassstaticstatusmanager.bss`.

