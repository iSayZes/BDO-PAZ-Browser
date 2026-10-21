# `yachtautobubbletextinfo.bss` Format

## Purpose

The speech bubbles of a Yar! match: what the player character and each
NPC opponent of [`yachtnpcdiceinfo.bss`](yachtnpcdiceinfo_bss.md) say when
something happens in the game. Each row is one trigger, either a game event
(scoring zero, winning, a turn passing) or a
[`yachthandrank.bss`](yachthandrank_bss.md) hand rank, with up to six
Korean lines. The plain PABR file holds the player's rows, then the NPCs'
rows, then the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes  | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ------ | ------- | --------- |
| 1      | 1784 and later | 3474    | `yachtautobubbletextinfo.bss` | 10,529 | 61 Row  | 36        |

| Layout | File                          | Known            | Unknown     |
| ------ | ----------------------------- | ---------------- | ----------- |
| 1      | `yachtautobubbletextinfo.bss` | 10,468 B (99.4%) | 61 B (0.6%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                                 |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
| `yachthandrank.bss`   | Optional | Korean hand rank names, where LOC has none                                                           |
| `languagedata_en.loc` | Optional | Lines (LOC type 112, `str_id1=bubble_text_key`, `str_id4` = line slot `0` to `5`), NPC names (LOC type 6), hand rank names (LOC type 105) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field              | Notes                                         |
| ------------------- | --------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]         | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32             | pc_count           | Number of player rows                         |
| `+0x08`             | Row[pc_count]   | pc_rows            | Rows with `character_key` `0`; see Row        |
| `pc_rows+0x00`      | u32             | npc_count          | Number of NPC rows                            |
| `pc_rows+0x04`      | Row[npc_count]  | npc_rows           | Rows with an NPC's `character_key`; see Row   |
| `npc_rows+0x00`     | String Table    | string_table       | See String Table                              |
| `string_table+0x00` | u32             | string_table_start | Offset of `string_count`, where the rows end  |
| `string_table+0x04` | u32             | zero               | Always `0`                                    |

The string table has the shape `exploration.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). The NPC rows end exactly at
`string_table_start`.

### Row (36 bytes)

| Offset  | Type   | Field            | Notes                                                                       |
| ------- | ------ | ---------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32    | bubble_text_key  | Unique key over both groups, LOC type 112 `str_id1`                         |
| `+0x04` | u16    | character_key    | The NPC who speaks; `0` in every player row                                 |
| `+0x06` | u32    | hand_rank_key    | The `yachthandrank.bss` hand that triggers the row; `0` when `condition` does |
| `+0x0A` | u32[6] | text_kr_indexes  | String table index of each Korean line; unused slots point at an empty string |
| `+0x22` | u8     | condition        | The game event that triggers the row, see Conditions; `0` when `hand_rank_key` does |
| `+0x23` | u8     | unknown_23       | `1` in every player row, `0` in every NPC row (clients 1784 and 3474)       |

The two groups share the key range: on client 3474 the player rows hold
keys 1 to 5 and the NPC rows 6 to 61.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                        |
| ------- | ------------------ | ------------ | ------------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings (185 on client 3474)                       |
| `+0x04` | pstr[string_count] | strings      | UTF-16 lines, each once: rows with the same line share its index |

## Conditions

The names come from the developer note on the `Condition` column in the
`#참조` sheet of a private server's `datasheet_minigame.xlsm` on client
1784; the speaker is the row's NPC, or the player in a player row.

| Value | Trigger                                  |
| ----- | ---------------------------------------- |
| `0`   | None; the row has a `hand_rank_key`      |
| `1`   | The speaker scores 0 points              |
| `2`   | The speaker scores more than the opponent |
| `3`   | The game starts                          |
| `4`   | The speaker wins                         |
| `5`   | The speaker loses                        |
| `6`   | 10 seconds are left in the turn          |
| `7`   | The turn passes to the speaker           |

On client 3474 the 5 player rows are conditions `1` and `2` and hand ranks
`11`, `12` and `14`. Each of the 8 NPCs of `yachtnpcdiceinfo.bss` has 7
rows, conditions `1` to `7` in order; condition `7` has six lines, every
other row three.

## Field Names

The `YachtBubbleText` sheet of a private server's `datasheet_minigame.xlsm`
on client 1784 has the columns `Index` (`bubble_text_key`), `CharacterKey`
(`character_key`), `Condition` (`condition`), `HandRankKey`
(`hand_rank_key`) and `~Desc_1` to `~Desc_6` (`text_kr_indexes`, in slot
order). Its 33 rows match the 33 rows of client 1784 and rows 1 to 33 of
client 3474 in every column and line. The sheet has no column for
`unknown_23` and no grouping: the file puts the rows without an NPC first,
which the `#참조` sheet marks as the player (`<null> = PC`).

## Notes

- Client 1784 holds the 5 player rows and 28 NPC rows (keys 6 to 33, the
  first four NPCs). Client 3474 adds keys 34 to 61 for Narangerel, Kakuo,
  Shakatu and Nolbu.
- Kakuo (`59739`) reuses Crio's (`40012`) Korean lines, one line aside, so
  their rows share string indexes. LOC type 112 gives each its own English
  text: slot 2 of Crio's key 20 reads "Were these cards hidden up your
  sleeve? Queek?", slot 2 of Kakuo's key 41 "Were these cards hidden up yer
  sleeve? Queek?".
- The client Lua calls no getter of this table. The match window
  (`panel_window_minigame_yachtdice_2.luac`) gets each bubble through the
  event `FromClient_processYachtGameBubbleText(isPlayer, bubbleText)` and
  shows it only in a game against an NPC
  (`__eMiniGameDBType_YachtDice_PVE`).

## Open Questions

### What `unknown_23` Is

The byte is `1` in the 5 player rows and `0` in the NPC rows on both
clients, so it repeats which group a row is in. No sheet column holds it.
The bubble event passes an `isPlayer` flag, which the byte may feed; a
player row with `0`, or an NPC row with `1`, would tell whether it is a
separate flag.
