# `acceptquest.bss` Format

## Purpose

The NPC dialog that gives each quest: one 8-byte row per quest with the quest key, the NPC's character key and the dialog index. `dialog_index << 16 | npc_id` is the `detail_dialog.dbss` key of the dialog, and the same value is `accept_dialog_key` at `+0x00` of the quest's `quest.dbss` record. [completequest_bss.md](completequest_bss.md) has the same layout for the dialog that takes the quest.

Example:

```text
quest 1001 / 49 (Dins, Spoiling for a Fight)
  npc_id 544 (Villager), dialog_index 430
  detail_dialog key 430 << 16 | 544 = 0x01AE0220, which LOC type 38 names "Dins"
```

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `languagedata_*.loc`  | Optional | Quest titles (type `18`), NPC names (type `6`) and the name the NPC shows in the dialog (type `38`, keyed `npc_id`, `dialog_index`) |

All multi-byte values are little-endian.

## File Layout

| Offset             | Type    | Field       | Notes |
| ------------------ | ------- | ----------- | ----- |
| `+0x00`            | char[4] | magic       | ASCII `PABR` |
| `+0x04`            | u32     | count       | Number of rows; `19,267` on client 3464, the count of `allquestlist.bss` |
| `+0x08`            | row[]   | rows        | 8-byte rows repeated `count` times |
| `8 + count * 8`    | u32     | string_count | `0`: the PABR string table of `exploration.bss`, here with no strings |
| EOF - 8            | u32     | rows_end    | `8 + count * 8`, where the rows end (`154,144` on client 3464) |
| EOF - 4            | u32     | zero        | Always `0` |

The file is `8 + count * 8 + 12` bytes (`154,156` on client 3464).

The rows are grouped by NPC: every NPC's rows form one run, and the rows without an NPC form one more. On client 3464 that is 1,986 runs for 1,985 NPCs plus the no-NPC run. The runs follow no sorted order of NPC or quest key.

## Record Structure

### Accept Quest Row (8 bytes, repeated `count` times)

| Offset  | Type | Field          | Notes |
| ------- | ---- | -------------- | ----- |
| `+0x00` | u16  | npc_id         | Character key (`characterstatic.dbss`) of the NPC who gives the quest; `0` when the quest names none |
| `+0x02` | u16  | quest_chain_id | LOC type 18 `str_id1` |
| `+0x04` | u16  | quest_id       | LOC type 18 `str_id2` |
| `+0x06` | u16  | dialog_index   | The NPC's dialog: `dialog_index << 16 \| npc_id` is a `detail_dialog.dbss` and `base_dialog.dbss` key. `0` (the Black Spirit) or `1` when `npc_id` is `0` |

Derived packed quest ID, as in `allquestlist.bss`:

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

## Reference Rows

Client 3464, names from `languagedata_en.loc`:

| Quest (Chain / Quest) | Title                         | npc_id | NPC Name (type 6) | dialog_index | Dialog Name (type 38) |
| --------------------- | ----------------------------- | -----: | ----------------- | -----------: | --------------------- |
| 1001 / 4              | Cat on the Roof               | 40066  | Mariano           | 1            | Mariano               |
| 1001 / 49             | Dins, Spoiling for a Fight    | 544    | Villager          | 430          | Dins                  |
| 1001 / 55             | Meutt's Sand Castle           | 544    | Villager          | 417          | Neutt                 |
| 8500 / 4              | [LoML] Emma's Invitation      | 0      | -                 | 0            | -                     |

## Suggested UI Layout

| Column      | Type | Notes |
| ----------- | ---- | ----- |
| Quest ID    | num  | `packed_quest_id` |
| Main ID     | num  | `quest_chain_id` |
| Sub ID      | num  | `quest_id` |
| Title       | text | LOC type 18 (`quest_chain_id`, `quest_id`, 0, 0), with its colours |
| NPC ID      | num  | `npc_id`; a dash when `0` |
| NPC Name    | text | LOC type 6 name of `npc_id` |
| Dialog      | num  | `dialog_index`, also on rows without an NPC |
| Dialog Name | text | LOC type 38 (`npc_id`, `dialog_index`, 0, 0): the name the NPC shows in that dialog |

## Notes

Figures from client 3464.

- Each packed quest ID of `allquestlist.bss` appears exactly once. The rows are in a different order from `allquestlist.bss`.
- `npc_id` is nonzero on 14,274 rows, and every one of those values is a `characterstatic.dbss` key. The other 4,993 rows have no NPC; their `dialog_index` is `0` on 2,532 and `1` on 2,461.
- `npc_id` `0` has dialogs of its own: `detail_dialog.dbss` holds keys `0` and `65536` (dialogs `0` and `1` of NPC `0`). Key `0` is the Black Spirit's dialog: LOC type 38 names (`0`, `0`) `Black Spirit`, and its greeting and options are the Black Spirit's lines. Key `65536` has no LOC name. On client 3464 the dialog `0` rows are dailies and story quests (`[Daily] Bolero's Helm Subjugation Request`, `Battle Against the Bashims`), the dialog `1` rows pass and guide quests (`Hands-On Sailing! 10.`, `Enhancing Tuvala Adventure Gear 2`); see Open Questions.
- 14,198 of the 14,274 NPC rows give a `detail_dialog.dbss` key. The test that this is the dialog index and not a count: on the 5,282 rows whose NPC has more than one dialog, 5,212 name one of that NPC's dialog indexes, where always taking the NPC's lowest index would match 521. The other 76 rows name a dialog the client does not have: 24 on the Villager character `35695`, 21 on the Quest NPC character `59878`, and the `[Ulukita]` quests of character `59981` with indexes `300` to `310`.
- Generic characters speak through many dialogs, so the dialog name tells more than the NPC name: the Villager character `544` gives "Dins, Spoiling for a Fight" as Dins (dialog `430`). The LOC type 38 dialog name differs from the LOC type 6 name on 3,923 rows.
- `quest.dbss` stores `dialog_index << 16 | npc_id` of this file as its `accept_dialog_key` (`+0x00`) for all 19,267 quests, so this file is an index of that field, grouped by NPC.
- Quest scripts call `meet(npc_id, dialog_index)` with the same pair (see `quest_dbss.md`); only 403 rows of this file hold their pair in a `meet()` call of their own quest, against 3,196 rows of `completequest.bss`.
- `completequest.bss` has the same size, header, row width and trailer, and holds the same quest set.

## Open Questions

### No-NPC Dialog `1`

Rows with `npc_id` `0` and `dialog_index` `1` point at `detail_dialog.dbss` key `65536`, a record with no LOC name and a stock social greeting. Whether it means the quest is given or taken without a dialog (automatically) is not confirmed.

### Dialogs the Client Lacks

76 NPC rows (client 3464) give a `dialog_index << 16 | npc_id` key that `detail_dialog.dbss` does not hold, among them `[Ulukita]` quests and `[Test]` quests. Whether these quests are cut content or open a dialog from another source is not known.
