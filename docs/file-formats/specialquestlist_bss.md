# `specialquestlist.bss` Format

## Purpose

Quest list of the Adventure Log pages: every page quest of the books in [`journalquest.dbss`](journalquest_dbss.md), the quests the client Lua calls special quests. On client 3474 the list holds exactly the 896 `quest.dbss` records with `quest_category` 11, in `quest.dbss` record order, and they are the 896 page quests of the 118 books.

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, where the trailer starts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records   | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | --------- | --------- |
| 1      | 1485 and later | 3482    | `specialquestlist.bss` | 3,604 | 896 Entry | 4         |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `specialquestlist.bss` | 3,604 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
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

## Quest Chains

Each book of `journalquest.dbss` is one quest chain (`journal_cat_id`), and its pages are that chain's quests. On client 3474 the 896 entries come from 118 chains, one per book, and every entry has a LOC type 18 title. Grouped by journal from `journalquest.dbss`, with the journal's English name from LOC type 63; Chains gives its lowest and highest book chain, not every chain in between:

| Journal Key | Journal                     | Books | Pages | Chains        |
| ----------: | --------------------------- | ----: | ----: | ------------- |
| 1           | Igor Bartali's Adventures   | 15    | 71    | 748 to 802    |
| 2           | Shakatu Merchants' Archive  | 11    | 51    | 826 to 30008  |
| 3           | Storybook - Morning Bosses  | 10    | 105   | 897 to 962    |
| 4           | Justin Bartali's Adventures | 1     | 17    | 2302          |
| 5           | Crow Merchants' Records     | 13    | 66    | 790 to 9007   |
| 6           | Event Logs                  | 6     | 39    | 9008 to 11551 |
| 7           | Storybook - Donghae         | 15    | 180   | 8700 to 8714  |
| 8           | Olvia Academy Journal       | 1     | 13    | 2326          |
| 9           | Old Moon Logs               | 10    | 53    | 792 to 841    |
| 10          | Outer Edania                | 7     | 44    | 9131 to 9137  |
| 11          | The Eyes of Adventure       | 9     | 45    | 8721 to 8729  |
| 12          | Storybook - Hwanghae        | 13    | 138   | 8542 to 8554  |
| 13          | Inner Edania                | 7     | 74    | 9331 to 9337  |

The list does not keep a book's pages together or in page order: on client 3474 the 118 chains form 331 runs, and in 38 chains the quest IDs are not ascending. The order is the `quest.dbss` record order.

## Client Use

The client Lua reads a list of the same name through the quest list object: `questList:getSpecialQuestCount()` and `questList:getSpecialQuestAt(i)`, each entry a quest number with `_group` (the chain) and `_quest`, and through the globals `ToClient_SpecialQuestCount()` and `ToClient_GetSpecialQuest(i)`, which return a quest wrapper.

- `panel_window_achievement.luac` (the Adventure Log book window, behind `_ContentsGroup_AchievementQuest`): `questSetting(groupNo)` walks `ToClient_GetSpecialQuest` and keeps the entries whose `_group` is the opened book's chain, then sorts them by `_quest`. The reward button looks up the quest's index in `getSpecialQuestAt` and sends it with `ToClient_RequestCompleteSpecialQuest(i)`, so the request carries the list position, not the quest number. The window registers `FromClient_notifyUpdateSpecialQuest` and refreshes when the updated quest is the shown page.
- `panel_widget_challengealert.luac`: `setProgressCount()` walks `getSpecialQuestAt` and stores the first demand's `_currentCount` of each special quest in progress, per chain. Its `FromClient_notifyUpdateSpecialQuest` handler runs only with `_ContentsGroup_AchievementQuest` and a character over level 60.

## Notes

- Decompressed size on client 3474: `3,604` bytes, `8 + 896 * 4 + 12`.
- On client 3474 `quest.dbss` has 896 records with `quest_category` 11, and they are this list in the same order. The same 896 quests are the page references of the 118 `journalquest.dbss` books, each once. `test_special_quest_list.py` checks the order and that every page is in the list.
- Client 3482 keeps the 896 entries but drops the book of chain 962 (the ten "Boss: Calamity 10" quests of the Black Shrine) from `journalquest.dbss`: 886 pages in 117 books, so chain 962 is in the list without a book.
- Client 1784 has 261 entries in 52 chains; its `journalquest.dbss` has 52 books. The 1784 list follows the 1784 `allquestlist.bss` order. 256 of the 261 entries are still in the client 3474 list; chain 11103 (5 quests) is gone. All 261 have `QuestType` 10 in the `Quest_Table` sheet of a private server's `DataSheets.bexcel` on client 1784; 219 other `QuestType` 10 rows of that sheet are not in the list. On the 256 keys that both clients share, `QuestType` 10 lines up with the live `quest_category` 11.
- [`specialquestinfo.bss`](specialquestinfo_bss.md) is a separate file with its own layout: the quest groups that `alreadyclearspecialquest(group)` action scripts name. On client 3474, 65 of its 277 quest entries are entries of this list.
