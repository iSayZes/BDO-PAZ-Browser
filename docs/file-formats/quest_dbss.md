# `quest.dbss` Format

## Purpose

Quest definition table. Each record stores the quest's accept and completion scripts, Korean objective text, a quest category, the packed quest ID, a counted list of 178-byte reward entries (including permanent Family-stat rewards), rich text payloads, the quest icon path, and a trailing ID echo.

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

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                                        |
| ------- | ------------- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32           | count   | Number of quest records; `18,991` on client 3474             |
| `+0x04` | Record[count] | records | See Record                                                   |

Records are stored back to back with no offset table and no padding. Record 0 starts at `+0x04`; every later record starts immediately after the previous record's 13-byte trailer. Record `i` belongs to packed quest ID `allquestlist[i]`.

A sequential walk (read the strings, find the packed ID of `allquestlist[i]` right after the objective, then the ID echo and trailer) consumes every byte of the file: on client 3474 it reads `18,991` of `18,991` records, and the last record ends exactly at end of file. Record sizes, from the lead to the end of the trailer, range from `512` to `11,651` bytes. The first three records start at `0x00000004`, `0x000006EB` and `0x00000C81`.

### Record (variable: 90 bytes + text and scanned parts)

Strings are a u64 character count (equivalently a u32 count plus a u32 zero) followed by UTF-16LE (`str16`) or ASCII (`str8`) code units, with no terminator. The Q-relative names (`unknown_q04`) count from `packed_quest_id`, the position the doc calls `Q`. Counts in the Notes column are from client 3474 unless they name another client.

| Offset                       | Type                                              | Field                 | Notes |
| ---------------------------- | ------------------------------------------------- | --------------------- | ----- |
| `+0x00`                      | u32                                               | accept_dialog_key     | `dialog_index << 16 \| npc_id` of the NPC dialog that gives the quest (`detail_dialog.dbss` key); `acceptquest.bss` row of the quest. `0` or `0x10000` without an NPC |
| `+0x04`                      | u32                                               | complete_dialog_key   | The same for the dialog that takes the quest; `completequest.bss` row of the quest |
| `+0x08`                      | u32                                               | unknown_08            | `0` in 18,916 of 18,991 |
| `+0x0C`                      | str16                                             | condition_script      | Accept/prerequisite expression, e.g. `getLevel()>30;<or>clearquest(654,4);` |
| `condition_script+0x00`      | str16                                             | action_script         | Completion expression, e.g. `killmonster(20007,10);`, `meet(npc_id,dialog_index)` |
| `action_script+0x00`         | bytes[scan]                                       | unknown_objective_gap | 24 zero bytes in 18,140 records; up to 382 bytes in the other 851 (content not decoded). The parser finds its end as the lowest u64 count whose UTF-16 text ends exactly at `quest_category`, after finding `packed_quest_id` by searching for `allquestlist[i]`; see Notes |
| `unknown_objective_gap+0x00` | str16                                             | objective_text_kr     | Korean objective text shown in the quest UI; line breaks are stored as `\n` (28 on client 3458) and decoded by the parser |
| `objective_text_kr+0x00`     | u32                                               | quest_category        | Formerly `link_type`; see [Quest Category](#quest-category) |
| `objective_text_kr+0x04`     | u32                                               | packed_quest_id       | `(quest_id << 16) \| quest_chain_id`; equals `allquestlist[i]` for every record |
| `objective_text_kr+0x08`     | u32                                               | unknown_q04           | `0x00010000` in 11,353 records; also `0x00010101`, `0x00010001`, `0x00010100`, `0` |
| `objective_text_kr+0x0C`     | bytes[8]                                          | unknown_q08           | Zero in 18,800 records, exactly those with `block_kind` 7 or 4 |
| `objective_text_kr+0x14`     | u32                                               | unknown_q10           | `0` in 15,766 kind-7 blocks; also `24`, `9999`, `22`, `168` |
| `objective_text_kr+0x18`     | u8                                                | block_kind            | `7` in 18,114 records, `4` in 686, `0` in 191 (shifted layout, see Open Questions) |
| `objective_text_kr+0x19`     | u32                                               | reward_entry_count    | `0` to `12`; number of 178-byte reward entries |
| `objective_text_kr+0x1D`     | Reward Entry[reward_entry_count] if block_kind != 0 | reward_entries      | See Reward Entry. With `block_kind` `0` the block is shifted and its entries are not read |
| `reward_entries+0x00`        | bytes[scan]                                       | unknown_payload       | Rich text (PAColor markup), more length-prefixed Korean strings, numeric config. Ends at the u64 count of `icon_path`, which the parser finds by scanning back from 16, then 8, bytes before the echo for the highest count whose ASCII text ends there in `.dds` |
| `unknown_payload+0x00`       | str8                                              | icon_path             | Quest icon path such as `Icon/Quest/Hadum08.dds`; ends 16 or 8 bytes before the echo. 18,988 of 18,991 records have one; the other three store zero bytes here. See Notes |
| `icon_path+0x00`             | bytes[scan]                                       | unknown_post_icon     | 16 bytes in 18,764 records, 8 in 224. Ends at the echo, the next occurrence of `packed_quest_id` after which the next record parses |
| `unknown_post_icon+0x00`     | u32                                               | packed_quest_id_echo  | Repeats `packed_quest_id` |
| `unknown_post_icon+0x04`     | bytes[13]                                         | unknown_trailer       | Most common: `00 × 9, 01 00 00 00` (5,094) and all zero (2,786); record ends here |

Earlier versions of this doc called `accept_dialog_key` and `complete_dialog_key` `unknown_00` and `unknown_04`, and before that, with `unknown_08`, `lead_a`, `lead_b` and `lead_zero` (and `packed_quest_id_a` and `packed_quest_id_b`); `unknown_q08` was `reserved_q08`. `unknown_objective_gap` was `objective_gap` and `unknown_trailer` was `trailer`.

The split between the 13-byte `unknown_trailer` and the next record's 12-byte lead is inferred from record 0 (12 bytes before its first string at `+0x0C`) and from the last record (13 bytes after its echo to end of file). [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) groups `packed_quest_id_echo`, the trailer and the next record's lead, scripts and objective into one "condition tail" of the earlier quest; our data shows those scripts belong to the next quest: on client 3474, in 8,107 of the 11,610 such blocks with a `clearquest` call it names the previous step of the next quest, versus 181 for the earlier quest.

### Reward Entry (178 bytes)

Only the Family-stat union is decoded. Entry `k` starts at `Q+0x19 + 178 × k` and holds its union at `Q+0x80 + 178 × k`.

| Offset  | Type              | Field       | Notes |
| ------- | ----------------- | ----------- | ----- |
| `+0x00` | bytes[103]        | unknown_00  | Not decoded; see Open Questions |
| `+0x67` | Family Stat Union | family_stat | See Family Stat Union |
| `+0x9C` | bytes[22]         | unknown_9c  | Not decoded |

### Family Stat Union (53 bytes)

Offsets relative to the union start `U = Q+0x80 + 178 × k`, for `k < reward_entry_count`. Field names from [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor). The union is byte-packed (`inventory` is one byte), so later fields are unaligned.

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

Client 3474, counted entries only: type `16` in 39,263 entries; 98 entries in 98 quests carry a real Family stat, each with only the selected field non-zero. 91 are journal pages (all in entry 0) and 7 are ordinary quests in entries 1 to 4, for example `72350` "A Gift for Papu" (DP +1, entry 1) and `329740` "[Elvia] Kzarka: Barrier of Infestation IV" (HP +20, entry 4). Summed: AP +10, DP +10, HP +1,000, Stamina +438, Weight +50 LT, Inventory +6, Accuracy +29, Evasion +8, Enhancement Chance +5, Valks limit +3. The game shows no total.

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
- The Family Stat column lists the non-`16` unions of the counted reward entries (skipped when `block_kind` is `0`). On client 3474 that is 104 entries: the 98 real Family stats plus six type `12`/`13` entries in the chain `1627` test quests, shown by type number only.
- `(file_size - 4) / count` is not integral, confirming variable-length records.
- There is no step/canonical record split: `accept_dialog_key`/`complete_dialog_key` are not quest IDs, and the record's own ID is `packed_quest_id` in the fixed block.
- `accept_dialog_key` and `complete_dialog_key` equal `dialog_index << 16 | npc_id` of the quest's `acceptquest.bss` and `completequest.bss` rows in all 19,267 quests of client 3464; those two files index the same values grouped by NPC. The two are equal in 11,519 quests. Quest `795132` (record 1 on client 3474) holds `65536` (`0x10000`): no NPC, dialog index `1`.
- Some decoded rows have no direct LOC type 18 title (27 of 18,991 IDs on client 3474). In those cases the scripts may still reference localized display quests through `clearquest(chain,id)`.
- No `questoffset.dbss` was found. `guildquestoffset.dbss` and `journalquestoffset.dbss` exist for related formats, but not for the main quest table.
- Scripts use semicolon-separated calls and comparisons, `!` negation and markers such as `<or>`: `getLevel()>30`, `clearquest(group,id)`, `killmonster(id,count)`, `gatheritem(item_id,?,count)`, `meet(npc_id,dialog_index)`, `collectknowledge(id)`. The first argument of `checkequipitemgroup(group,min,max)` and `checkinventoryitemgroup(group,min,max)` is a group key in [itemequipgroup.bss](itemequipgroup_bss.md). The argument of `alreadyclearspecialquest(group)` (action scripts only) is a group key in [specialquestinfo.bss](specialquestinfo_bss.md).
- [questprogressgroup.bss](questprogressgroup_bss.md) groups quest chains (the Land of the Morning Light quest boards, the `[Bonus] Skill Up` chains) and names the quest that finishes each chain's story; its IDs are `quest_chain_id`/`quest_id` pairs of this file.
- [multiplequest.bss](multiplequest_bss.md) gives quest chains a range of quest IDs whose quests are versions of one quest (`[Beginner]` to `[Guru]`, one per contribution point band); no `condition_script` names a quest of its own range.
- The second `meet()` argument is a dialog index of the NPC (`dialog_index << 16 | npc_id` is a `detail_dialog.dbss` key), not a count. On client 3464 the action scripts hold 15,948 `meet()` calls: 889 pass only the NPC key, and of the 3,929 two-argument calls whose NPC has `detail_dialog.dbss` records, 3,906 name one of its dialogs. Where the NPC has more than one dialog that is 1,973 of 1,977 calls, against 196 if the argument were always the NPC's lowest index. The 11,130 calls whose NPC has no dialog record pass `1` in 11,084 cases.
- Journal-page records (`quest_category = 11`) all have `block_kind = 7`, zero `unknown_q08` and zero `unknown_q10`; the 91 pages with a Family stat use reward entry 0.

## Open Questions

### Shifted Fixed Block (`block_kind = 0`)

On client 3474, 191 records have `0` at `Q+0x14`; in 150 of them the `07` and count bytes appear two bytes later (`Q+0x16`/`Q+0x17`). Whether these records have extra bytes before the block or a different layout is not decoded, and their reward entries are not read. The layout marks this with `if block_kind != 0` on `reward_entries`; the bytes of these records' entries fall in `unknown_payload`.

### Reward Entry Layout

Only the Family-stat union inside each 178-byte entry is decoded. The rest of the entry (values such as `0x09`, `0x0C`, `0x0F` and `0x10` at fixed positions, `300` at one offset) probably holds item, EXP or skill rewards. The entry start at `Q+0x19` is inferred from the count field ending there, not from a decoded field.

### Contribution and Energy Union Types

Types `12` and `13` occur only in chain `1627` "Contribution Point Reward Test" quests. The values sit at `U+0x31` and `U+0x33`, but their widths and whether real quests use them are unknown.

### Unknown Payload After Reward Entries

The bytes between the reward entries and `icon_path` contain rich text, further length-prefixed Korean strings (e.g. `아이템`) and numeric config. Field boundaries are not yet decoded.

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
