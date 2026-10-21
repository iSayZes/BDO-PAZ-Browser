# `yachtnpcdiceinfo.bss` Format

## Purpose

The NPC opponents of Yar!, a dice minigame (`panel_window_minigame_yachtdice` in the client Lua) that a client 3474 quest text describes as "inspired by Poker and Yacht". Each row is one game setup for one NPC: the dice preset the NPC plays, the hand ranks (scoring combinations) the game offers, the NPC's knowledge entry, the deck limit and how many rolls a turn allows. An NPC can have more than one row. The plain PABR file holds the rows, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ---------------------- | ----- | ------- | ----------------------- |
| 1      | 3474 and later | 3474    | `yachtnpcdiceinfo.bss` | 560   | 11 Row  | 44 to 60, 49 on average |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `yachtnpcdiceinfo.bss` | 560 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                                                 |
| ---------------------- | -------- | ------------------------------------------------------------------------------------ |
| `yachthandrank.bss`    | Optional | Korean hand rank names, where LOC has none ([`yachthandrank.bss`](yachthandrank_bss.md)) |
| `yachtdicepreset.dbss` | Optional | The five dice of each `dice_preset_key` ([`yachtdicepreset.dbss`](yachtdicepreset_dbss.md)) |
| `languagedata_en.loc`  | Optional | NPC names (LOC type 6 at `str_id1=npc_key`), knowledge names (LOC type 34 at `str_id1=knowledge_key`), hand rank names (LOC type 105 at `str_id1=hand_rank_key`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                         |
| ------------------- | ------------ | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32          | count              | Number of rows                                |
| `+0x08`             | Row[count]   | rows               | Variable-size rows, back to back; see Row     |
| `rows+0x00`         | String Table | string_table       | See String Table                              |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end  |
| `string_table+0x04` | u32          | zero               | Always `0`                                    |

The string table has the shape `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Walking `count` rows ends exactly at `string_table_start`.

### Row (variable: 24 bytes + hand ranks)

| Offset            | Type                 | Field             | Notes                                                                   |
| ----------------- | -------------------- | ----------------- | ----------------------------------------------------------------------- |
| `+0x00`           | u32                  | npc_dice_info_key | Unique row key                                                          |
| `+0x04`           | u16                  | npc_key           | Character key of the NPC, LOC type 6 `str_id1`                          |
| `+0x06`           | u32                  | dice_preset_key   | A key of `yachtdicepreset.dbss` (keys 1 to 31 on client 3474)           |
| `+0x0A`           | u64                  | hand_rank_count   | Number of hand ranks                                                    |
| `+0x12`           | u32[hand_rank_count] | hand_rank_keys    | Keys of `yachthandrank.bss` (15 hand ranks on client 3474); ascending on every row (client 3474) |
| `hand_rank_keys+0x00` | u32              | knowledge_key     | The NPC's knowledge entry, LOC type 34 `str_id1`                        |
| `hand_rank_keys+0x04` | u8               | deck_limit        | `150` on every row (client 3474)                                        |
| `hand_rank_keys+0x05` | u8               | roll_count_max    | Rolls per turn; `3` or `4` (client 3474)                                |

`npc_key` sits at `+0x04` with no padding, so `dice_preset_key` and the hand rank list are not 4-byte aligned.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3474          |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Rows

On client 3474 the file holds 11 rows for 8 NPCs:

| Key | NPC (`npc_key`)       | Dice preset | Hand ranks | Knowledge (`knowledge_key`) | Rolls |
| --- | --------------------- | ----------- | ---------- | --------------------------- | ----- |
| 1   | Eileen (40063)        | 26          | 1 to 6     | Eileen (45)                 | 3     |
| 2   | Eileen (40063)        | 25          | 1 to 4, 7  | Eileen (45)                 | 3     |
| 3   | Islin Bartali (40001) | 26          | 2, 3, 5, 6, 7 | Islin Bartali (1)        | 3     |
| 4   | Islin Bartali (40001) | 26          | 1, 3, 4, 5, 8 | Islin Bartali (1)        | 3     |
| 5   | Crio (40012)          | 1           | 2 to 5, 7  | Crio (12)                   | 3     |
| 6   | Crio (40012)          | 26          | 1 to 7     | Crio (12)                   | 4     |
| 7   | Igor Bartali (40017)  | 31          | 1 to 6     | Igor Bartali (18)           | 3     |
| 8   | Narangerel (50857)    | 31          | 1 to 4, 6, 7 | Narangerel (1678)         | 3     |
| 9   | Kakuo (59739)         | 31          | 1 to 6     | Kakuo (11155)               | 4     |
| 10  | Shakatu (45120)       | 26          | 1 to 9     | Shakatu (894)               | 4     |
| 11  | Nolbu (47240)         | 26          | 1 to 9     | Nolbu (2003)                | 4     |

On every row the knowledge entry's English name (LOC type 34) is the NPC's English name (LOC type 6).

## Field Names

The `NPC_DiceList` sheet of a private server's `datasheet_minigame.xlsm` on client 1784 has the columns `NpcDiceInfoKey` (`npc_dice_info_key`), `NPCKey` (`npc_key`), `PresetList` (`dice_preset_key`), `HandRankKeyList` (`hand_rank_keys`, one comma-separated list), `DeckLimit` (`deck_limit`), `MentalCardKey` (`knowledge_key`) and `RollCountMax` (`roll_count_max`). Its 7 compiled rows (keys 1 to 7) match rows 1 to 7 of the client 3474 file in every column; the file writes `MentalCardKey` before `DeckLimit`. `PresetList` holds one value per row, the `PresetIndex` of the same workbook's `DicePreset` sheet, and the file stores it as one u32. `HandRankKeyList` names the `HandRankKey` of the `HandRanking` sheet (Ones, Twos, ..., Two of a kind, Full House). The sheet has 10 more rows, commented out with `<주석>`, for NPCs that are not in either client's file.

## Notes

- The client Lua reads the hand ranks through `ToClient_getYachtHandRankKeyList` and the roll limit through `ToClient_getMiniGameYachtCurrentGameRollCountMax` (`panel_window_minigame_yachtdice_1.luac`).
- Every `dice_preset_key` on client 3474 is a key of `yachtdicepresetoffset.dbss`; `test_handler.py` checks it.
- The quote in Purpose is LOC type 37 text from a Narangerel quest: "Yar! is a minigame inspired by Poker and Yacht, and you can challenge various NPCs in the world of Black Desert."
- Client 1784 has no `yachtnpcdiceinfo.bss`. It ships `yachtnpcdiceinfo.dbss` with `yachtnpcdiceinfooffset.dbss` instead: a u32 count, then each row as here with a u32 copy of its key in front, in reverse key order (7 down to 1). The offset file lists key, offset and size per row (`0x30` for row 7, the size this doc's Row gives for 6 hand ranks). Its 7 rows hold the same values as rows 1 to 7 of the client 3474 file.
