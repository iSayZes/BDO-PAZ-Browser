# `completequest.bss` Format

## Purpose

The NPC dialog that takes each quest (the turn-in): one 8-byte row per quest with the quest key, the NPC's character key and the dialog index. `dialog_index << 16 | npc_id` is the `detail_dialog.dbss` key of the dialog, and the same value is `complete_dialog_key` at `+0x04` of the quest's `quest.dbss` record. The layout is that of [acceptquest_bss.md](acceptquest_bss.md), which holds the dialog that gives the quest.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes   | Records                   | Row bytes |
| ------ | -------------- | ------- | ------------------- | ------- | ------------------------- | --------- |
| 1      | 1784 and later | 3473    | `completequest.bss` | 151,948 | 18,991 Complete Quest Row | 8         |

| Layout | File                | Known              | Unknown    |
| ------ | ------------------- | ------------------ | ---------- |
| 1      | `completequest.bss` | 151,948 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `languagedata_*.loc`  | Optional | Quest titles (type `18`), NPC names (type `6`) and the name the NPC shows in the dialog (type `38`, keyed `npc_id`, `dialog_index`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                   | Field        | Notes |
| ------------------- | ---------------------- | ------------ | ----- |
| `+0x00`             | char[4]                | magic        | ASCII `PABR` |
| `+0x04`             | u32                    | count        | Number of rows; `19,267` on client 3464, the count of `allquestlist.bss` |
| `+0x08`             | Complete Quest Row[count] | rows         | See Complete Quest Row |
| `rows+0x00`         | String Table           | string_table | The PABR string table of `exploration.bss`, here with no strings |
| `string_table+0x00` | u32                    | rows_end     | `8 + count * 8`, where the rows end (`154,144` on client 3464) |
| `string_table+0x04` | u32                    | zero         | Always `0` |

The file is `8 + count * 8 + 12` bytes (`154,156` on client 3464).

The rows are grouped by NPC: every NPC's rows form one run, and the rows without an NPC form one more. On client 3464 that is 2,024 runs for 2,023 NPCs plus the no-NPC run.

### Complete Quest Row (8 bytes)

| Offset  | Type | Field          | Notes |
| ------- | ---- | -------------- | ----- |
| `+0x00` | u16  | npc_id         | Character key (`characterstatic.dbss`) of the NPC who takes the quest; `0` when the quest names none |
| `+0x02` | u16  | quest_chain_id | LOC type 18 `str_id1` |
| `+0x04` | u16  | quest_id       | LOC type 18 `str_id2` |
| `+0x06` | u16  | dialog_index   | The NPC's dialog: `dialog_index << 16 \| npc_id` is a `detail_dialog.dbss` and `base_dialog.dbss` key. `0` (the Black Spirit) or `1` when `npc_id` is `0`, except one row with `12` |

Derived packed quest ID, as in `allquestlist.bss`:

```text
packed_quest_id = (quest_id << 16) | quest_chain_id
```

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Reference Rows

Client 3464, names from `languagedata_en.loc`:

| Quest (Chain / Quest) | Title                         | npc_id | NPC Name (type 6) | dialog_index | Dialog Name (type 38) |
| --------------------- | ----------------------------- | -----: | ----------------- | -----------: | --------------------- |
| 1001 / 4              | Cat on the Roof               | 40066  | Mariano           | 1            | Mariano               |
| 1001 / 49             | Dins, Spoiling for a Fight    | 544    | Villager          | 326          | Vigilante             |
| 8500 / 4              | [LoML] Emma's Invitation      | 59875  | Quest NPC         | 73           | Igor Bartali          |

## Notes

Figures from client 3464.

- Each packed quest ID of `allquestlist.bss` appears exactly once, in a different order from `allquestlist.bss` and from `acceptquest.bss`.
- `npc_id` is nonzero on 15,728 rows, and every one of those values is a `characterstatic.dbss` key. The other 3,539 rows have no NPC; their `dialog_index` is `0` on 2,507, `1` on 1,031 and `12` on one (quest 21420 / 7, a key `detail_dialog.dbss` does not hold). Dialogs `0` and `1` of NPC `0` are those of `acceptquest.bss`: `0` is the Black Spirit.
- 15,672 of the 15,728 NPC rows give a `detail_dialog.dbss` key. On the 5,971 rows whose NPC has more than one dialog, 5,931 name one of that NPC's dialog indexes, where always taking the NPC's lowest index would match 561.
- The LOC type 38 dialog name differs from the LOC type 6 name on 4,557 rows. The generic Quest NPC character `59875` speaks as Igor Bartali, Dolswe, Yibang and others, one name per dialog.
- `quest.dbss` stores `dialog_index << 16 | npc_id` of this file as its `complete_dialog_key` (`+0x04`) for all 19,267 quests.
- Quest scripts call `meet(npc_id, dialog_index)` with the same pair (see `quest_dbss.md`): 3,196 rows of this file hold their exact pair in a `meet()` call of their own quest, against 403 rows of `acceptquest.bss`.

## Open Questions

### Dialogs the Client Lacks

56 NPC rows (client 3464) give a `dialog_index << 16 | npc_id` key that `detail_dialog.dbss` does not hold, as in `acceptquest.bss`. The largest groups are character `59725` (18 rows) and the Villager character `35695` (14 rows).
