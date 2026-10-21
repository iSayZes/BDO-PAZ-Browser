# `doguildquestlist.bss` Format

## Purpose

Quest list behind the guide button of the quest widget, which counts the listed quests and routes to their accept NPCs. On client 3474 the list holds 39 quests, among them life-skill starter quests (`[Alchemy] Accidental Alchemist`, `[Trading] Preparation for Trading`), Heidel and Velia side quests (`A Very Minute Flaw`, `Velia Storage`) and the opening quests of the Edania regions (`[Hakinza Sanctuary] Set Sail`, `[Aetherion] Whispers Around Edania`). The file name spells "guild", but the list has no guild quests: it is the `DoGuide` list of the client Lua (see [Client Use](#client-use) and [Source Sheet](#source-sheet)).

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, where the trailer starts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records  | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | -------- | --------- |
| 1      | 1485 and later | 3474    | `doguildquestlist.bss` | 176   | 39 Entry | 4         |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `doguildquestlist.bss` | 176 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

The same as [`allquestlist.bss`](allquestlist_bss.md).

All multi-byte values are little-endian.

## Client Use

`panel_checkedquest.luac` (client 3474) reads the list through `questList_getDoGuideQuestCount()` and `questList_getDoGuideQuestAt(i)`:

- `PaGlobal_CheckedQuest:doGuideQuest()` writes the count on the widget's `Button_Guide` and hides the button when it is `0`.
- `HandleClicked_QuestWidget_GuideQuest()` starts a navigation route to the accept NPC (`getAccecptNpc()`, `getAccecptDialogIndex()`) of every listed quest that passes `questList_isSelectQuest(getSelectType())`, then opens the world map. A second click removes the routes.
- `new_worldmap_questtooltip.luac` shows a listed quest's title, demands and description when the tooltip asks for `QuestType_DoGuide` (`3` in `CppEnums.QuestType` of `global_define_cpp_enum.luac`).

## Source Sheet

The `Quest_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 has a `DoGuide` column holding a condition script, for example `getLifeLevel(4)>15;` on quest 3500 / 310 `[Alchemy] A Small Favor`. 33 rows of the sheet fill it, and they are exactly the 33 entries of `doguildquestlist.bss` on client 1784, as a set. The file order is neither the sheet order nor the quest order.

On client 3474, 32 of those 33 quests are still in the list; 1100 / 1 `[Gathering Basics] Introduction to Processing` is gone from the list but still a quest in `allquestlist.bss`. The seven new entries are 3208 / 6 and the opening quests of chains 9101 to 9104, 9110 and 9320 (Edania regions, `[Edana's Defense Gear]`, `[Godslayer Skill]`).

## Notes

- Decompressed size on client 3474: `176` bytes, `8 + 39 * 4 + 12`. Client 1784: `152` bytes, 33 entries.
- All 39 entries have a LOC type 18 title on client 3474, and each is a record of `quest.dbss` (`test_do_guide_list.py` checks that every entry is in `allquestlist.bss` and that no entry repeats).
- calpheonlabs (`doguildquestlist.bss.mdx`, capture PAZ 3595) reads the same layout, 38 rows of (u16 quest group, u16 quest number) and a 12-byte pad, and calls them "guild-enabled quest IDs". The `DoGuide` column and the Lua above do not support a guild reading.
- The `DoGuide` script is not a decoded field of [`quest.dbss`](quest_dbss.md) yet.

## Open Questions

### Filtered Count

The Lua shows `questList_getDoGuideQuestCount()` on the guide button and hides the button at `0`. Whether the client counts every entry of this file or only the quests whose `DoGuide` condition (client 1784 sheet) the character meets is not visible in the Lua; a count that hides the button at `0` points to a filter.
