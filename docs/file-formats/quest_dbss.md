# `quest.dbss` Format

## Purpose

Quest definition table. Each record stores the quest's accept and completion scripts, Korean objective text, a quest category, the packed quest ID, two counted lists of 178-byte reward entries (the base rewards, among them permanent Family stats, and the rewards the player picks one of), rich text payloads, the quest icon path, and a trailing ID echo.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `allquestlist.bss`    | Required | Packed quest ID of every record, in record order; the walk needs it  |
| `languagedata_en.loc` | Optional | English quest strings; raw `quest.dbss` stores Korean objective text |
| `questgroup.dbss`     | Optional | Quest chain/group metadata; links group names to child quest IDs     |
| `journalquest.dbss`   | Optional | Adventure-journal books whose pages are quest IDs of this file       |
| `stringtable.bss`     | Optional | GAME sheet key hashes of the Quest Type names (see [Quest Category](#quest-category)) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                                        |
| ------- | ------------- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32           | count   | Number of quest records; `18,991` on client 3474             |
| `+0x04` | Record[count] | records | See Record                                                   |

Records are stored back to back with no offset table and no padding. Record 0 starts at `+0x04`; every later record starts immediately after the previous record's 13-byte trailer. Record `i` belongs to packed quest ID `allquestlist[i]`.

A sequential walk (read the strings, find the packed ID of `allquestlist[i]` right after the objective, then the ID echo and trailer) consumes every byte of the file: on client 3474 it reads `18,991` of `18,991` records, and the last record ends exactly at end of file. Record sizes, from the lead to the end of the trailer, range from `512` to `11,651` bytes. The first three records start at `0x00000004`, `0x000006EB` and `0x00000C81`.

### Record (variable: 106 bytes + text, lists and scanned parts)

Strings are a u64 character count (equivalently a u32 count plus a u32 zero) followed by UTF-16LE (`str16`) or ASCII (`str8`) code units, with no terminator. The Q-relative names (`unknown_q04`) count from `packed_quest_id`, the position the doc calls `Q`. Counts in the Notes column are from client 3474 unless they name another client.

| Offset                       | Type                              | Field                     | Notes |
| ---------------------------- | --------------------------------- | ------------------------- | ----- |
| `+0x00`                      | u32                               | accept_dialog_key         | `dialog_index << 16 \| npc_id` of the NPC dialog that gives the quest (`detail_dialog.dbss` key); `acceptquest.bss` row of the quest. `0` or `0x10000` without an NPC |
| `+0x04`                      | u32                               | complete_dialog_key       | The same for the dialog that takes the quest; `completequest.bss` row of the quest |
| `+0x08`                      | u32                               | unknown_08                | `0` in 18,916 of 18,991 |
| `+0x0C`                      | str16                             | condition_script          | Accept/prerequisite expression, e.g. `getLevel()>30;<or>clearquest(654,4);` |
| `condition_script+0x00`      | str16                             | action_script             | Completion expression, e.g. `killmonster(20007,10);`, `meet(npc_id,dialog_index)` |
| `action_script+0x00`         | bytes[scan]                       | unknown_objective_gap     | 24 zero bytes in 18,140 records; up to 382 bytes in the other 851 (content not decoded). The parser finds its end as the lowest u64 count whose UTF-16 text ends exactly at `quest_category`, after finding `packed_quest_id` by searching for `allquestlist[i]`; see Notes |
| `unknown_objective_gap+0x00` | str16                             | objective_text_kr         | Korean objective text shown in the quest UI; line breaks are stored as `\n` (28 on client 3458) and decoded by the parser |
| `objective_text_kr+0x00`     | u32                               | quest_category            | Formerly `link_type`; see [Quest Category](#quest-category) |
| `objective_text_kr+0x04`     | u32                               | packed_quest_id           | `(quest_id << 16) \| quest_chain_id`; equals `allquestlist[i]` for every record |
| `objective_text_kr+0x08`     | u32                               | unknown_q04               | `0x00010000` in 11,353 records; also `0x00010101`, `0x00010001`, `0x00010100`, `0` |
| `objective_text_kr+0x0C`     | u32                               | unknown_list_count        | `0` in 18,800 records, `1` in 166, `2` in 10, `3` in 15 |
| `objective_text_kr+0x10`     | u16[unknown_list_count]           | unknown_list              | e.g. `0x069C, 0x06BC, 0x06DB` in `74860`; see Open Questions |
| `unknown_list+0x00`          | u32                               | unknown_list_00           | `0` in every record |
| `unknown_list+0x04`          | u32                               | unknown_list_04           | `0` in 16,643 records; also `24` (1,599), `9999` (635), `22`, `168`, `72`, `1`, `25`; see Open Questions |
| `unknown_list+0x08`          | u8                                | block_kind                | `7` in 18,285 records, `4` in 706 |
| `unknown_list+0x09`          | u32                               | base_reward_count         | `0` to `12` |
| `unknown_list+0x0D`          | Reward Entry[base_reward_count]   | base_rewards              | See Reward Entry |
| `base_rewards+0x00`          | u32                               | select_reward_count       | `0` in 17,589 records, up to `7` in the other 1,402 |
| `base_rewards+0x04`          | Reward Entry[select_reward_count] | select_rewards            | The rewards the player picks one of; all 3,723 are items (`reward_type` `3`) |
| `select_rewards+0x00`        | u32                               | unknown_select_rewards_00 | `0` in 18,955 records, `1` in 36 |
| `select_rewards+0x04`        | i64                               | unknown_select_rewards_04 | `0` in 13,781 records; also `13,500`, `100,000`, `200,000`, `300,000`, `1,000,000` and 973 more values |
| `select_rewards+0x0C`        | bytes[scan]                       | unknown_payload           | Rich text (PAColor markup), more length-prefixed Korean strings, numeric config. Ends at the u64 count of `icon_path`, which the parser finds by scanning back from 16, then 8, bytes before the echo for the highest count whose ASCII text ends there in `.dds` |
| `unknown_payload+0x00`       | str8                              | icon_path                 | Quest icon path such as `Icon/Quest/Hadum08.dds`; ends 16 or 8 bytes before the echo. 18,988 of 18,991 records have one; the other three store zero bytes here. See Notes |
| `icon_path+0x00`             | bytes[scan]                       | unknown_post_icon         | 16 bytes in 18,764 records, 8 in 224. Ends at the echo, the next occurrence of `packed_quest_id` after which the next record parses |
| `unknown_post_icon+0x00`     | u32                               | packed_quest_id_echo      | Repeats `packed_quest_id` |
| `unknown_post_icon+0x04`     | bytes[13]                         | unknown_trailer           | Most common: `00 × 9, 01 00 00 00` (5,094) and all zero (2,786); record ends here |

Earlier versions of this doc called `accept_dialog_key` and `complete_dialog_key` `unknown_00` and `unknown_04`, and before that, with `unknown_08`, `lead_a`, `lead_b` and `lead_zero` (and `packed_quest_id_a` and `packed_quest_id_b`); `unknown_q08` was `reserved_q08`. `unknown_objective_gap` was `objective_gap` and `unknown_trailer` was `trailer`. `unknown_list_count`, `unknown_list` and `unknown_list_00` were one `bytes[8]` field `unknown_q08`, `unknown_list_04` was `unknown_q10`, and `base_reward_count` and `base_rewards` were `reward_entry_count` and `reward_entries`. That reading put `block_kind` at `Q+0x14` and found `0` there in the 191 records with `unknown_list`; their block starts 2, 4 or 6 bytes later.

The split between the 13-byte `unknown_trailer` and the next record's 12-byte lead is inferred from record 0 (12 bytes before its first string at `+0x0C`) and from the last record (13 bytes after its echo to end of file). [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) groups `packed_quest_id_echo`, the trailer and the next record's lead, scripts and objective into one "condition tail" of the earlier quest; our data shows those scripts belong to the next quest: on client 3474, in 8,107 of the 11,610 such blocks with a `clearquest` call it names the previous step of the next quest, versus 181 for the earlier quest.

### Reward Entry (178 bytes)

The same entry as in [`guildquest.dbss`](guildquest_dbss.md#reward-entry-178-bytes): the `gc::QuestRewardElement` members of the 2016 client in their order, byte-packed with the `_item` pointer dropped, then the Family Stat Union and bytes the 2016 struct has no member for. `reward_type` picks the members that hold the reward; see [Reward Types](#reward-types). Counts from client 3474, base and select rewards together (43,342 entries).

| Offset  | Type              | Field                | Notes |
| ------- | ----------------- | -------------------- | ----- |
| `+0x00` | u32               | reward_type          | `gc::RewardType`; see Reward Types |
| `+0x04` | i64               | experience           | Combat EXP of type `0`; `0` in every other entry |
| `+0x0C` | i32               | skill_experience     | Skill EXP of type `1`; `0` in every other entry |
| `+0x10` | i32               | product_experience   | `0` in every entry |
| `+0x14` | u8                | life_experience_type | Life skill of type `2` (`CppEnums.LifeExperienceType`, as in [`lifeexp.dbss`](lifeexp_dbss.md)); `15` (`Type_Count`) in every other entry |
| `+0x15` | i32               | life_experience      | Life skill EXP of type `2`; `0` in every other entry |
| `+0x19` | u32               | item_key             | Item of type `3`, packed as `enchant_level << 24 \| item_id`; `0` in every other entry |
| `+0x1D` | i64               | item_count           | Amount of `item_key` |
| `+0x25` | u16               | intimacy_character   | NPC character key of type `4` (Amity) |
| `+0x27` | i32               | intimacy_value       | Amity points of type `4` |
| `+0x2B` | bytes[60]         | unknown_2b           | Zero apart from `16` at `+0x36` in every entry and values of the types after `4`; see Open Questions |
| `+0x67` | Family Stat Union | family_stat          | See Family Stat Union |
| `+0x9C` | bytes[22]         | unknown_9c           | Values of types `9`, `17` and `18`; see Open Questions |

### Family Stat Union (53 bytes)

Offsets relative to the union start `U`, `family_stat` of a base reward entry. Field names from [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor). The union is byte-packed (`inventory` is one byte), so later fields are unaligned.

| Offset  | Type | Field              | Notes                                           |
| ------- | ---- | ------------------ | ----------------------------------------------- |
| `+0x00` | u32  | family_stat_type   | Selects the populated field; `16` = no reward   |
| `+0x04` | f32  | offence            | Type `0`, All AP                                |
| `+0x08` | f32  | defence            | Type `1`; the Garmoth gear planner shows each +1 as +1 DP and +1 DR |
| `+0x0C` | f32  | hp                 | Type `2`, Max HP                                |
| `+0x10` | f32  | mp                 | Type `3`, Max MP (not observed)                 |
| `+0x14` | i32  | stamina            | Type `4`, Max Stamina                           |
| `+0x18` | i32  | weight             | Type `5`, divide by 10,000 for LT               |
| `+0x1C` | u8   | inventory          | Type `6`, inventory slots                       |
| `+0x1D` | f32  | accuracy           | Type `7`                                        |
| `+0x21` | f32  | evasion            | Type `8`                                        |
| `+0x25` | i32  | enhancement_chance | Type `9`                                        |
| `+0x29` | i32  | valks_limit        | Type `10`, additional enhancement chance limit  |
| `+0x2D` | i32  | stack_limit        | Type `11`, enhancement chance stack limit (not observed) |
| `+0x31` | u16  | contribution       | Type `12`, only in test quests (chain `1627`); width unconfirmed |
| `+0x33` | u16  | energy             | Type `13`, only in test quests (chain `1627`); width unconfirmed |

## Layout 1

On client 1784 a record opens with a Korean string after the two dialog
keys, has no `unknown_objective_gap` (the objective follows `action_script`
directly), and stores `packed_quest_id` once, near the end, after the
reward and text data. A counted u32 list and 14 bytes end the record. A
walk by this layout with the same `allquestlist[i]` search reads all
16,877 records of client 1784 and ends at the last byte of the file.

The reward lists sit at the start of `unknown_payload`. In 16,515 of the
16,877 records, 9 bytes after the objective (zero in 16,463 records) come
`base_reward_count`, `base_rewards`, `select_reward_count` and
`select_rewards` as in Layout 2, with entries of 188 bytes. Their members
`+0x00` to `+0x2A` are those of Layout 2, and `+0x36` and `+0x67` hold `16`
as there; the 10 extra bytes lie in the tail, where the `exploreexp` value
of type `9` sits at `+0xB4` in place of `+0xAA`. In the other 362 records
the count comes later. The layout keeps these bytes in `unknown_payload`,
as the parser reads Layout 2 only.

### Record (variable: 71 bytes + text and scanned parts)

| Offset                       | Type                          | Field                | Notes |
| ---------------------------- | ----------------------------- | -------------------- | ----- |
| `+0x00`                      | u32                           | accept_dialog_key    | |
| `+0x04`                      | u32                           | complete_dialog_key  | |
| `+0x08`                      | str16                         | unknown_old_08       | Korean text, e.g. `노먼 레이트` in record 0 |
| `unknown_old_08+0x00`        | u32                           | unknown_08           | |
| `unknown_old_08+0x04`        | str16                         | condition_script     | |
| `condition_script+0x00`      | str16                         | action_script        | |
| `action_script+0x00`         | str16                         | objective_text_kr    | |
| `objective_text_kr+0x00`     | bytes[scan]                   | unknown_payload      | Reward entries, rich text and the `.dds` icon path; ends at `packed_quest_id`, found by searching for `allquestlist[i]` after the objective, taking the first hit after which the next record parses |
| `unknown_payload+0x00`       | u32                           | packed_quest_id      | Equals `allquestlist[i]` |
| `unknown_payload+0x04`       | u32                           | unknown_payload_04   | `0` in 13,182 records, `1` in 3,576 |
| `unknown_payload+0x08`       | u8                            | unknown_payload_08   | `0` or `1` |
| `unknown_payload+0x09`       | u32                           | unknown_value_count  | `1` to `7` |
| `unknown_payload+0x0D`       | u32[unknown_value_count]      | unknown_values       | Hash-like values; `0xFEED568F` in the list of 4,514 records |
| `unknown_values+0x00`        | bytes[14]                     | unknown_end          | Zero in 16,062 of 16,877 records |

## Reward Types

`reward_type` values `0` to `4` are the 2016 `gc::RewardType` (`eRewardCount` = `5`). On clients 1784 and 3474 each of these types holds its value in its own members of the Reward Entry and leaves every other member unset, so the member sizes of the 2016 struct place every offset of `+0x00` to `+0x2A`.

The later types are not in the 2016 enum. Their names in the table are the script calls of the `Quest_Table` `BaseReward` and `SelectReward` columns of a private server's `DataSheets.bexcel` on client 1784: there, on the 15,825 records whose `BaseReward` lists as many calls as the file has base entries and the 15,849 whose `SelectReward` does the same for the select entries, each entry type pairs with one call name, and the item, EXP, Skill EXP, Life EXP and Amity members equal the call arguments in every entry but one item. Entries from client 3474, base and select rewards together:

| Value | `gc::RewardType`  | Script call     | Entries (client 3474) |
| ----: | ----------------- | --------------- | --------------------: |
| `0`   | `eRewardExp`      | `exp`           | 936    |
| `1`   | `eRewardSkillExp` | `skillexp`      | 432    |
| `2`   | `eRewardLifeExp`  | `lifeexp`       | 121    |
| `3`   | `eRewardItem`     | `item`          | 21,716 |
| `4`   | `eRewardIntimacy` | `intimacy`      | 1,599  |
| `5`   |                   | `knowledge`     | 1,660  |
| `7`   |                   | `expgrade`      | 3,016  |
| `8`   |                   | `skillexpgrade` | 360    |
| `9`   |                   | `exploreexp`    | 13,383 |
| `12`  |                   | `familystat`    | 104    |
| `14`  |                   | `growstep`      | 0      |
| `17`  |                   | `feverpoint`    | 10     |
| `18`  |                   | `seasonreward`  | 5      |

Type `14` occurs on client 1784 only. The type `12` entries are exactly the entries whose Family Stat Union holds a stat (`family_stat_type` other than `16`). `panel_widget_questrewarditem.luac` branches on `__eRewardExp`, `__eRewardSkillExp`, `__eRewardLifeExp`, `__eRewardExpGrade`, `__eRewardSkillExpGrade`, `__eRewardItem`, `__eRewardIntimacy`, `__eRewardKnowledge`, `__eRewardSeasonReward`, `__eRewardExploreExp`, `__eRewardFamilyStat` and `__eRewardCharacterStat`, which reads `getMaxFeverPoint()`; the Lua does not hold their values.

## Quest Category

The u32 immediately before `packed_quest_id`. It is the quest type, `__eQuestType` of the client Lua: on client 3474 the per-category record counts below equal, value for value, the 20 totals of [`totalquestcounttype.bss`](totalquestcountregion_bss.md#quest-types), whose value N is quest type N. The enum names follow the `__eQuestType_*` order of `panel_window_quest_all.luac`, and the quest window names are the English LOC of its `_typeString` keys (none for the three Olvia Academy types). Counts from client 3474:

| quest_category | Count | Quest type | Quest window name | Same quests as |
| -------------: | ----: | ---------- | ----------------- | -------------- |
| `0` | 458 | `BlackSpirit` | Black Spirit |  |
| `1` | 3,872 | `Main` | Main |  |
| `2` | 5,890 | `Sub` | General |  |
| `3` | 2,229 | `Repeat` | Recurring |  |
| `4` | 473 | `Adventure` | Adventure |  |
| `5` | 609 | `BaseLife` | Life |  |
| `6` | 162 | `OceanLife` | Sailing |  |
| `7` | 331 | `CraftLife` | Production |  |
| `8` | 627 | `Contents` | Content |  |
| `9` | 1,977 | `Event` | Event |  |
| `10` | 1 | `Guild` | Guild |  |
| `11` | 896 | `DirectAccept` | Adventurer's Tome | The 896 page quests of the 118 books in `journalquest.dbss`, and the 896 quests of [`specialquestlist.bss`](specialquestlist_bss.md) in the same order |
| `12` | 180 | `Sudden` | Region Bonus | The 180 quests of [`regionmonsterkillquestlist.bss`](regionmonsterkillquestlist_bss.md), in the same order |
| `13` | 410 | `SeasonPass` | Season Pass |  |
| `14` | 224 | `GrowthPass` | Progression Pass |  |
| `15` | 219 | `DirectClear` | Etc. |  |
| `16` | 0 | `Journal` | Journal | No record on client 3474 |
| `17` | 180 | `OlviaAcademyPass` | none | The 180 quests of [`olviaacademypassquestlist.bss`](olviaacademyquestlist_bss.md), in the same order |
| `18` | 85 | `OlviaAcademyReward` | none | The 85 quests of [`olviaacademyrewardquestlist.bss`](olviaacademyquestlist_bss.md), in the same order |
| `19` | 168 | `OlviaAcademyCurriculum` | none | The 168 quests of [`olviaacademycurriculumquestlist.bss`](olviaacademyquestlist_bss.md), in the same order |

The category `11`, `12` and `17` to `19` records are also exactly the quests of the lists in the last column.

## Former "Canonical Link" Sub-record

The earlier "magic marker `0x003BAE30`" is not a marker: `30 AE 3B 00` is the UTF-16LE text `기;` (U+AE30, `;`), the usual ending of a Korean objective such as `…처치하기;`. The following `link_type` and `canonical_quest_id` are `quest_category` and `packed_quest_id` of the same record. 16,570 of 18,991 objectives on client 3474 end in `기;`, which is why the scan finds only about 87% of records.

## Family-Stat Union

The layout is in [Family Stat Union](#family-stat-union-53-bytes).

Client 3474, base reward entries: type `16` in 39,515 entries; 98 entries in 98 quests carry a real Family stat, each with only the selected field non-zero. 91 are journal pages (all in entry 0) and 7 are ordinary quests in entries 1 to 4, for example `72350` "A Gift for Papu" (DP +1, entry 1) and `329740` "[Elvia] Kzarka: Barrier of Infestation IV" (HP +20, entry 4). Summed: AP +10, DP +10, HP +1,000, Stamina +438, Weight +50 LT, Inventory +6, Accuracy +29, Evasion +8, Enhancement Chance +5, Valks limit +3. The game shows no total.

I checked this against the [Garmoth](https://garmoth.com) gear planner (2026-09-27), which covers Igor Bartali's Adventure Log and a list of quests: every covered stat matches exactly.

| Source | Garmoth | This file |
| --- | --- | --- |
| Igor Bartali's Adventures (journal 1) | HP 877, Stamina 438, AP 6, All Accuracy 29, Inventory 4, DP 6, DR 6, Evasion 8, Weight 28 | HP 877, Stamina 438, AP 6, Accuracy 29, Inventory 4, defence 6, Evasion 8, Weight 28 |
| Quests: Barrier of Infestation III to V, A Gift for Papu, Mother's Warning, Ruler of Taebaek, Dokkebi's Gift, 10th Anniversary | AP 4, DP 4, DR 4, HP 123 | `264204` / `329740` / `395276` (defence 1, HP 20, AP 1), `72350` (defence 1), `139191` (AP 1), `74052` (AP 1), `598334` (defence 1), journal 6 book 10 "10th Anniversary Event Logs" (HP 103, defence 1, AP 1): AP 4, defence 4, HP 123 |

Garmoth leaves out four journals that also grant stats, which is why its Inventory (4) and Weight (28) are lower: journal 2 Shakatu Merchants' Archive (Weight 2), 3 Storybook - Morning Bosses (Weight 10), 5 Crow Merchants' Records (Weight 8, Inventory 2, Enhancement Chance 5) and 9 Old Moon Logs (Weight 2, Valks limit 3). Garmoth calls `139191` "Mother's Warning"; its LOC type 18 title is "Tungrad School".

## Observed Records

The first three records of client 3474:

| File Offset  | `accept_dialog_key` | Packed Quest ID | Condition                            | Action                                          | Objective KR                                   | Icon                                            |
| ------------ | ------------------- | --------------- | ------------------------------------ | ----------------------------------------------- | ---------------------------------------------- | ----------------------------------------------- |
| `0x00000004` | `10617774`          | `138172`        | `getLifeLevel(0)>1;getLevel()>19;`   | `gatheritem(4657,0,5); exchangeItem(4657,0,5);` | `소나무 널빤지 만들기;소나무 널빤지 건네주기;` | `Icon/Quest/himute_002.dds`                     |
| `0x000006EB` | `65536`             | `795132`        | (empty)                              | `collectknowledge(11733);`                      | `무당령전 지식 얻기;`                          | `Icon/Quest/8700_12.dds`                        |
| `0x00000C81` | `0`                 | `196891`        | `clearquest(283,2);`                 | `havegamepoint(2, 100);`                        | `공헌도 100 달성하기;`                         | `Icon/Quest/Icon_Real_ETC_ETC_00044053.dds`     |

## Localization

Quest title/text strings appear in LOC `str_type=18`. This type uses
`str_id1=quest_chain_id`, `str_id2=quest_id`, and `str_id4` for text role.
The DBSS packed ID stores `(quest_id << 16) | quest_chain_id`.

Example matches from `languagedata_en.loc`:

| Chain ID | Quest ID | LOC Type | id4 | Example English Text |
| -------: | -------: | -------- | --: | -------------------- |
| `41067`  | `1`      | `18`     | `0` | `[Godr-Ayed and Blackstar] PEN (V) Earthshaking Blackstar Shield` |
| `41067`  | `1`      | `18`     | `2` | `Merindora` |
| `41067`  | `1`      | `18`     | `3` | `Hand over Scorching Sun Crystal to Merindora;...` |
| `3500`   | `310`    | `18`     | `0` | `[Alchemy] A Small Favor` |
| `3500`   | `311`    | `18`     | `0` | `[Alchemy] A Kid's Wisdom` |

`id4=3` is the translated counterpart of `objective_text_kr` (e.g. `138172`: `소나무 널빤지 만들기;소나무 널빤지 건네주기;` and `Make pine planks;Give pine planks;`). The scripts are client DSL and have no LOC counterpart.

Quest IDs can collide with other LOC domains. For example, `65536` also matches
item LOC `str_type=0`. Previous research also matched `str_type=39`, but that
type appears to be voice/dialogue text and can produce misleading preview
titles/objectives.

## Notes

- On client 3474 the file is `34,900,081` bytes with `18,991` records; the test fixture is that same file.
- Parsed preview is a lazy handler: the walk builds a small index on open and each page parses only its own rows.
- The parser walks the records in `allquestlist.bss` order, so that file is a required companion (and the second source of the `QUEST_ICON` lookup index). For each record it reads the two scripts, finds the record's own packed ID after them (the objective string must end at the `quest_category` right before it), then takes the next occurrence of that ID as the echo; the next record must parse right after the 13-byte trailer, or end the file. The walk takes about 0.35 s and reads every script: 18,991 of 18,991 records on client 3474. The earlier scan anchored rows on icon paths and on the `기;` pattern and decoded only 8,085 script rows.
- The icon path is read through its u64 prefix, not a pattern match. That recovers paths the old `Icon/[A-Za-z0-9_./ -]+` pattern cut short or missed: `Icon/Quest/O'dylilta_820115.dds`, `UI_Artwork/IC_01245.dds`, and `New_Icon/03_ETC/...`, which the pattern read as `Icon/03_ETC/...`. Three records store no icon at all: `69183`, `69175` and `8456145`. The old scan-based icon index had given them, and about a hundred other quests (mostly O'dyllita and Sherekhan ones), a neighbouring record's icon or a truncated path.
- The Quest Type column names `quest_category` with the quest window's label for that type (GAME sheet key via `stringtable.bss` and LOC type 37), else the enum name (the three Olvia Academy types), else nothing for a value past `19`. The names follow the client 3474 enum; the handler reads Layout 2.
- The Family Stat column lists the non-`16` unions of the base reward entries. On client 3474 that is 104 entries: the 98 real Family stats plus six entries of Family stat type `12` or `13` in the chain `1627` test quests, shown by type number only.
- The Rewards and Selectable Rewards columns show `base_rewards` and `select_rewards` of reward types `0` to `4` the way `panel_widget_questrewarditem.luac` names them: the `GAME` sheet texts of `LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP`, `_SKILLEXP`, `_PRODUCTEXP` (with the life skill) and `_INTIMACY` (after the NPC name), and items with their icon, name and count. Entries of the later types are left out, as their values sit in undecoded tail bytes; the Family Stat column covers type `12`. The parser keeps the 135 bytes after `intimacy_value` of each entry as one hex field `unknown_2b`, shared with `guildquest.dbss` in `_common/quest/reward_entry.py`.
- `(file_size - 4) / count` is not integral, confirming variable-length records.
- There is no step/canonical record split: `accept_dialog_key`/`complete_dialog_key` are not quest IDs, and the record's own ID is `packed_quest_id` in the fixed block.
- `accept_dialog_key` and `complete_dialog_key` equal `dialog_index << 16 | npc_id` of the quest's `acceptquest.bss` and `completequest.bss` rows in all 19,267 quests of client 3464; those two files index the same values grouped by NPC. The two are equal in 11,519 quests. Quest `795132` (record 1 on client 3474) holds `65536` (`0x10000`): no NPC, dialog index `1`.
- Some decoded rows have no direct LOC type 18 title (27 of 18,991 IDs on client 3474). In those cases the scripts may still reference localized display quests through `clearquest(chain,id)`.
- No `questoffset.dbss` was found. `guildquestoffset.dbss` and `journalquestoffset.dbss` exist for related formats, but not for the main quest table.
- Scripts use semicolon-separated calls and comparisons, `!` negation and markers such as `<or>`: `getLevel()>30`, `clearquest(group,id)`, `killmonster(id,count)`, `gatheritem(item_id,?,count)`, `meet(npc_id,dialog_index)`, `collectknowledge(id)`. The first argument of `checkequipitemgroup(group,min,max)` and `checkinventoryitemgroup(group,min,max)` is a group key in [itemequipgroup.bss](itemequipgroup_bss.md). The argument of `alreadyclearspecialquest(group)` (action scripts only) is a group key in [specialquestinfo.bss](specialquestinfo_bss.md).
- [questprogressgroup.bss](questprogressgroup_bss.md) groups quest chains (the Land of the Morning Light quest boards, the `[Bonus] Skill Up` chains) and names the quest that finishes each chain's story; its IDs are `quest_chain_id`/`quest_id` pairs of this file.
- [multiplequest.bss](multiplequest_bss.md) gives quest chains a range of quest IDs whose quests are versions of one quest (`[Beginner]` to `[Guru]`, one per contribution point band); no `condition_script` names a quest of its own range.
- The second `meet()` argument is a dialog index of the NPC (`dialog_index << 16 | npc_id` is a `detail_dialog.dbss` key), not a count. On client 3464 the action scripts hold 15,948 `meet()` calls: 889 pass only the NPC key, and of the 3,929 two-argument calls whose NPC has `detail_dialog.dbss` records, 3,906 name one of its dialogs. Where the NPC has more than one dialog that is 1,973 of 1,977 calls, against 196 if the argument were always the NPC's lowest index. The 11,130 calls whose NPC has no dialog record pass `1` in 11,084 cases.
- Journal-page records (`quest_category = 11`) all have `block_kind = 7`, an empty `unknown_list` and zero `unknown_list_04`; the 91 pages with a Family stat use base reward entry 0.

## Open Questions

### `unknown_list` Values

On client 3474, 191 records hold one to three u16 values in `unknown_list`, for example `0x025F` in `3550966` and `0x0625, 0x0628` in `140194`. What they key is not checked. The 2016 `gc::QuestStaticStatus` has one list of u16 keys, `_contentsGroupKey` (`gc::ContentsGroupKeyList`).

### `unknown_list_04`

The values `24`, `168`, `72`, `22`, `1`, `25` and `9999` read as hours. On client 1784 the `Quest_Table` `RepeatTime` column of a private server's `DataSheets.bexcel` holds the same values, and the 2016 `gc::QuestStaticStatus` has `_resetHour`. The field is not located in the Layout 1 record, so the column is not matched row by row.

### Reward Entry Tail

The reward types after `4` hold their values in `unknown_2b` and `unknown_9c`. On client 1784, where the sheet gives the call arguments, type `5` holds its `knowledge()` key at `+0x2B` (`0x24D8` for `knowledge(9432)`), type `7` its `expgrade()` argument at `+0x31`, type `9` its `exploreexp()` argument at `+0xB4`, and types `17` and `18` theirs after `+0xA6`; type `8` stores its `skillexpgrade()` argument in none of the 188 bytes. On client 3474 the same types fill `+0x2B`, `+0x31`, `+0xAA` and `+0xA0` to `+0xA9`. The widths and the live-client meaning are not checked, and the `16` at `+0x36` (every entry of both files) has no known role.

### Fields After the Select Rewards

The 2016 `gc::QuestRewardGroup` is `_baseReward`, `_selectReward` and `_expectedPrice` (`__int64`), and `unknown_select_rewards_04` is an i64 in that place. On client 1784 it equals the sheet's `ExpectedPrice` column in 18 of the 15,849 records with a sheet row, so the name does not carry over. `unknown_select_rewards_00` is not explained either.

### Contribution and Energy Union Types

Family stat types `12` and `13` occur only in chain `1627` "Contribution Point Reward Test" quests. The values sit at `U+0x31` and `U+0x33`, but their widths and whether real quests use them are unknown.

### Unknown Payload After the Rewards

The bytes between `unknown_select_rewards_04` and `icon_path` contain rich text, further length-prefixed Korean strings (e.g. `아이템`) and numeric config. Field boundaries are not yet decoded.

### `unknown_objective_gap` Content

The gap between `action_script` and `objective_text_kr` is 24 zero bytes in most records but longer (up to 382 bytes) in 851 on client 3474. bdo-data-extractor mentions a "short counted section" here; it is not decoded.

On client 3473, 18,603 of 18,991 gaps read as three u64-counted UTF-16 strings, which are empty in the 24-zero-byte case. Other gaps hold u32-counted lists of such strings (`01 00 00 00`, then a count and `checkclass(1);`), and one holds a count of `2` followed by two values that read as Unix timestamps. Whether the gap is a fixed series of string lists is not checked.

### LOC Row Semantics

`quest_chain_id` + `quest_id` resolve to multiple LOC type 18 rows with
different `id4` values: `id4=0` title, `id4=1` summary/description, `id4=2`
NPC/giver, `id4=3` objective. bdo-data-extractor uses the same four roles.
Whether higher `id4` values exist for some quests is unconfirmed. LOC type 39
still has many quest-adjacent strings, but is not reliable as the main quest
title/objective source.

### `questgroup.dbss` Coverage

`questgroup.dbss` confirms one relationship to this file: each child link is a `(group_id, quest_no)` pair whose raw 4 bytes equal a `quest.dbss` packed quest ID. It does not explain the remaining variable-length payload fields in `quest.dbss`.
