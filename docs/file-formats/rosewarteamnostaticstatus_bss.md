# `rosewarteamnostaticstatus.bss` Format

## Purpose

The Rose War team of each team character: one row per character key with
its team number. On client 3474 the file has 31 rows: 15 on team `0`
(the Lemoria units, Sylineo, Sylane, Sylana and Syluna, Light of
Kamasylvia, Narchillan's Blessing and four siege objects) and 16 on team
`1` (the Ahib units, Deleneo, Delane, Delana and Delura, Darkness of
O'dyllita, Sephir's Blessing and four siege objects).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `rosewarteamnostaticstatus.bss` | 206   | 31 Row  | 6         |

| Layout | File                            | Known          | Unknown    |
| ------ | ------------------------------- | -------------- | ---------- |
| 1      | `rosewarteamnostaticstatus.bss` | 206 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                              |
| ------- | ---- | ------------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | character_key | `characterstatic.dbss` key; the handler shows its LOC type 6 name  |
| `+0x02` | u32  | team_no       | `0` Kamasylvia, `1` O'dyllita; see Teams                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Teams

The client Lua names the teams `__eRoseWarTeam_Kamasylvia`,
`__eRoseWarTeam_Odyllita` and `__eRoseWarTeam_Neutral` without their
values, and reads a player's team with `getRoseWarTeamNo()`. The rows fix
the two numbers this file uses (client 3474):

| `team_no` | Characters (LOC type 6)                                                                 | Team       |
| --------- | --------------------------------------------------------------------------------------- | ---------- |
| `0`       | Lemoria Guards, Defenders, Honor Guard(s) and Ranger; Sylineo, Sylane, Sylana, Syluna; Light of Kamasylvia; Narchillan's Blessing | Kamasylvia |
| `1`       | Ahib Spearmaiden, Assassin, Great Blader, Protectors, Dark Mage and Grand Shaman; Deleneo, Delane, Delana, Delura; Darkness of O'dyllita; Sephir's Blessing | O'dyllita  |

Both teams also list Abandoned Cannon, Ancient Chariot, Elephant and
Ballista, one character key each per team (`31117` to `31124`, odd keys on
team `0`, even keys on team `1`).

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. Every key resolves to a LOC
type 6 character name. `team_no` follows the `getRoseWarTeamNo()` Lua
name; the Lemoria are the elves of Kamasylvia and the Ahib those of
O'dyllita, which fixes `0` and `1`. The upper three bytes of `team_no` are
`0` on every row, so the width is the reading, not a confirmed fact.

## Notes

- The file is the same on clients 3002, 3251 and 3474, 206 bytes. It is
  not in the archives of client 1784.
- [`rosewarinfo.bss`](rosewarinfo_bss.md) has one row per team with the
  same `0` and `1` in its `unknown_08`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  with the character name and the team's Lua name.
