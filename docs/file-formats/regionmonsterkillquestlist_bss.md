# `regionmonsterkillquestlist.bss` Format

## Purpose

Quest list of the region monster kill quests: zone subjugation quests (`Magaia Subjugation I`, `[Subjugation] Pluck Those Manshaum Fangs`), weekly loot quests (`[Weekly] Looting Garmoth I`) and the `[Season]` hunting quests. On client 3474 the list holds exactly the 180 `quest.dbss` records with `quest_category` 12, in `quest.dbss` record order.

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, where the trailer starts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records   | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ----- | --------- | --------- |
| 1      | 1784 and later | 3474    | `regionmonsterkillquestlist.bss` | 740   | 180 Entry | 4         |

| Layout | File                             | Known          | Unknown    |
| ------ | -------------------------------- | -------------- | ---------- |
| 1      | `regionmonsterkillquestlist.bss` | 740 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

The same as [`allquestlist.bss`](allquestlist_bss.md).

All multi-byte values are little-endian.

## Quest Chains

On client 3474 the 180 quests come from 27 quest chains. Every entry has a LOC type 18 title.

| Chains                       | Quests | Example title                                     |
| ---------------------------- | -----: | ------------------------------------------------- |
| 769                          | 3      | Accessory Filled with the Witch's Power - Part I  |
| 785, 894                     | 29     | [Subjugation] Pluck Those Manshaum Fangs          |
| 3724, 3733, 3734             | 23     | Saltwater Crocodile's Treasure I                  |
| 9035, 9037, 9051, 9083       | 4      | [Weekly] Sycrakea: Abyssal Chest                  |
| 9121 to 9125, 9322 to 9326   | 30     | Magaia Subjugation I                              |
| 11491, 15501                 | 6      | [Weekly] Looting Garmoth I                        |
| 12022                        | 9      | Defend the Delphe Knights Castle!                 |
| 12023, 12024, 40015, 40032   | 76     | [Season] Settling Down at the Bashim Base         |

The completion scripts (`action_script` in `quest.dbss`) on client 3474: 151 `killmonstergroup` (any case), 16 `killmonster`, 3 `KillMonsterTogether` and 10 `checkLooting`. Other categories hold kill quests too: 702 of the 853 quests with a `killmonstergroup` script (any case) are not in this list. The first argument of `killmonstergroup` is a `character_group` key of [`characterstatic.dbss`](characterstatic_dbss.md#character-group); all 167 keys of these 853 quests have characters on client 3474.

## Client Use

The client Lua reads a list of the same name through the quest list object: `questList:getRegionMonsterKillQuestCount()` and `questList:getRegionMonsterKillQuestAt(i)`, each entry a quest number with `_group` (the chain) and `_quest`. The only caller in the client Lua is the alert widget (`panel_widget_alertarea_renew.luac`): a checked quest that is satisfied and completes at the Black Spirit raises the Black Spirit alert only when it is not in this list. `panel_widget_accesoryquest.luac` registers the event `FromClient_notifyUpdateRegionMonsterKillQuest` with an empty function; that widget shows the current region's quest from `getSuddenQuestWrapperOnCurrentRegion()` with its kill counter and a complete button.

## Notes

- Decompressed size on client 3474: `740` bytes, `8 + 180 * 4 + 12`.
- On client 3474 `quest.dbss` has 180 records with `quest_category` 12, and they are this list in the same order. `test_region_monster_kill_list.py` checks the match.
- Client 1784 has 114 entries in 8 chains (769, 785, 3724, 12022, 12023, 12024, 40015, 40032). 110 of them are still in the client 3474 list; 40015 / 17 to 20 are gone. All 114 have `QuestType` 11 in the `Quest_Table` sheet of a private server's `DataSheets.bexcel` on client 1784; the one other `QuestType` 11 row of that sheet (3431 / 1, `killMonsterGroup(116,300);`) is not in the list. On the 110 keys that both clients share, `QuestType` 11 lines up with the live `quest_category` 12.