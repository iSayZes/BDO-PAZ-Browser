# `olviaacademy*questlist.bss` Format

## Purpose

Quest lists of the Olvia Academy windows (`panel_window_olviaacademy_main_all*.luac`, `panel_window_olviaacademy_pass_all*.luac`). Three files share one layout and one handler. Each holds exactly the [`quest.dbss`](quest_dbss.md) records of one `quest_category`, in `quest.dbss` record order:

| File                                  | quest_category | Holds                                                        |
| ------------------------------------- | -------------: | ------------------------------------------------------------ |
| `olviaacademycurriculumquestlist.bss` | `19`           | The course quests of the curriculum, chains 2308 to 2318 and 2325 |
| `olviaacademypassquestlist.bss`       | `17`           | The Olvia Academy Pass quests, chain 2324                    |
| `olviaacademyrewardquestlist.bss`     | `18`           | The family reward quests, chain 2323                         |

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` is `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, where the trailer starts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                  | Bytes | Records   | Row bytes |
| ------ | -------------- | ------- | ------------------------------------- | ----- | --------- | --------- |
| 1      | 3474 and later | 3474    | `olviaacademycurriculumquestlist.bss` | 692   | 168 Entry | 4         |
| 1      | 3474 and later | 3474    | `olviaacademypassquestlist.bss`       | 740   | 180 Entry | 4         |
| 1      | 3474 and later | 3474    | `olviaacademyrewardquestlist.bss`     | 360   | 85 Entry  | 4         |

| Layout | File                                  | Known          | Unknown    |
| ------ | ------------------------------------- | -------------- | ---------- |
| 1      | `olviaacademycurriculumquestlist.bss` | 692 B (100.0%) | 0 B (0.0%) |
| 1      | `olviaacademypassquestlist.bss`       | 740 B (100.0%) | 0 B (0.0%) |
| 1      | `olviaacademyrewardquestlist.bss`     | 360 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

The same as [`allquestlist.bss`](allquestlist_bss.md).

All multi-byte values are little-endian.

## Curriculum Quests

`olviaacademycurriculumquestlist.bss` on client 3474: 168 quests in twelve chains. The title tag names the course. Each course runs from sub ID 1 (`Sign Up for ...`) to its `Course Completed` quest; the 24 `Material Support` and `Ship Support` quests sit at sub IDs 53 to 62.

| Chain | Title tag            | Quests | Sub IDs              |
| ----: | -------------------- | -----: | -------------------- |
| 2308  | `[Olvia Academy]`    | 1      | 1 (Your First Steps In) |
| 2309  | `[Olvia Academy]`    | 1      | 1 (Graduation with Honor) |
| 2310  | `[Combat Course]`    | 31     | 1 to 32, no 19       |
| 2311  | `[Alchemy Course]`   | 18     | 1 to 12, six from 54 to 61 |
| 2312  | `[Training Course]`  | 14     | 1 to 14              |
| 2313  | `[Cooking Course]`   | 19     | 1 to 13, six from 54 to 62 |
| 2314  | `[Hunting Course]`   | 14     | 1 to 13, 53          |
| 2315  | `[Sailing Course]`   | 15     | 1 to 13, 53, 56      |
| 2316  | `[Fishing Course]`   | 14     | 1 to 13, 53          |
| 2317  | `[Processing Course]`| 17     | 1 to 11, 53 to 58    |
| 2318  | `[Farming Course]`   | 14     | 1 to 12, 58, 60      |
| 2325  | `[Gathering Course]` | 10     | 1 to 10              |

Chains 2321 and 2322 (`[Academy] [Weekly ...]` quests, 38 in `allquestlist.bss`) are in none of the three lists.

## Pass Quests

`olviaacademypassquestlist.bss` on client 3474: 180 quests, all in chain 2324. The hundreds digit of the sub ID is the pass tab. Each tab has ten steps; step `n` is the base quest at sub ID `x00 + 2n - 1` and the pass quest at `x00 + 2n`. Every pass quest title ends in `(Olvia Academy Pass)` and no base quest title does. The tabs follow the order in which `panel_window_olviaacademy_pass_all.luac` lists the `__eOlviaAcademyPassType_*` values:

| Sub IDs    | Pass type (Lua)                    | Title          |
| ---------- | ---------------------------------- | -------------- |
| 101 to 120 | `__eOlviaAcademyPassType_Collect`  | Gathering Time! `n`. |
| 201 to 220 | `__eOlviaAcademyPassType_Fish`     | Hands-On Fishing! `n`. |
| 301 to 320 | `__eOlviaAcademyPassType_Hunt`     | Happy Hunting! `n`. |
| 401 to 420 | `__eOlviaAcademyPassType_Cook`     | Win Them Over with Cooking! `n`. |
| 501 to 520 | `__eOlviaAcademyPassType_Alchemy`  | Hands-On Alchemy! `n`. |
| 601 to 620 | `__eOlviaAcademyPassType_Work`     | Processing in Progress! `n`. |
| 701 to 720 | `__eOlviaAcademyPassType_Train`    | Hands-On Training! `n`. |
| 801 to 820 | `__eOlviaAcademyPassType_Farm`     | Fantastic Farming! `n`. |
| 901 to 920 | `__eOlviaAcademyPassType_Ship`     | Hands-On Sailing! `n`. |

`panel_window_olviaacademy_pass_all_1.luac` asks for each row with `ToClient_GetOlviaAcademyQuest(passType, questIndex, __eOlviaAcademyPassQuestType_Base)` and `..._Pass`, and shows the pass quest's reward as locked while `ToClient_HasOlviaAcademyPass(passType)` is false. The file order is not the step order.

## Family Reward Quests

`olviaacademyrewardquestlist.bss` on client 3474: 85 quests, all in chain 2323. Every title is `[Olvia Academy] <Family> Family Reward`, and each family has its own sub ID block:

| Sub IDs    | Title                     | Quests |
| ---------- | ------------------------- | -----: |
| 1 to 36    | Combat Family Reward      | 36     |
| 101 to 106 | Gathering Family Reward   | 6      |
| 111 to 116 | Cooking Family Reward     | 6      |
| 121 to 126 | Alchemy Family Reward     | 6      |
| 131 to 135 | Training Family Reward    | 5      |
| 141 to 145 | Hunting Family Reward     | 5      |
| 151 to 155 | Sailing Family Reward     | 5      |
| 161 to 166 | Fishing Family Reward     | 6      |
| 171 to 175 | Processing Family Reward  | 5      |
| 181 to 185 | Farming Family Reward     | 5      |

Quest 201 of chain 2323 (`Finest First Impression`) is `quest_category` 2 and not in the list.

## Notes

- Decompressed sizes on client 3474: `692` bytes for the curriculum list (168 quests), `740` for the pass list (180), `360` for the reward list (85); all match `8 + count * 4 + 12`.
- Every quest of the three lists is in `allquestlist.bss` and has a LOC type 18 title (client 3474).
- The test client 1784 has none of the three files.
- `olviaacademypassstaticstatusmanager.bss` (0.8 KB, not documented yet) is a `PABR` file whose first block is a u32 `10` and 20 packed quest IDs, 101 to 120 of chain 2324 in sub ID order, followed by the same for 201 to 220 and 301 to 320. It is the first file to check for the pass step order.
- `test_olvia_academy_lists.py` asserts that each list is its `quest_category` in `quest.dbss` record order and that every pass base quest has its pass quest at sub ID + 1.

## Open Questions

### What Reads the Lists

No Lua reads the three lists by name. The main window walks `ToClient_RequestOlviaAcademyCurriculumCount()` curricula with `getSubjectCount()` subjects each and `ToClient_RequestOlviaAcademyRewardCount()` family rewards with `getRewardTitle()` and `getRewardIcon()`; the pass window walks `ToClient_GetOlviaAcademyPassSize(passType)` rows. Whether the client builds those from these lists or from `olviaacademycurriculumss.bss` and `olviaacademypassstaticstatusmanager.bss` (both not documented yet) is open.
