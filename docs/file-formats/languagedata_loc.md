# `languagedata_en.loc` Format

## Purpose

Stores all localized strings for the game, keyed by a compound ID (str_type, str_id1–4). Used as the primary English text source across all file format handlers.

Example:

```text
str_type: 1, str_id1: 44, str_id4: 0  →  "Stoneback Crab Artisan"
str_type: 7, str_id1: 1,  str_id4: 0  →  "Hammer"
str_type: 54, str_id1: 40012          →  "Thank you! I really like this."
str_type: 71, str_id1: 47, str_id3: 12 →  "Guile"
```

## Graph

### Tags

- file format
- loc
- localization

### Connections

- [title.dbss](title_dbss.md), title names and requirements (str_type=1)
- [zodiacsign.dbss](zodiacsign_dbss.md), zodiac sign names and traits (str_type=7)
- [npcgift.dbss](npcgift_dbss.md), NPC gift dialogue (str_type=54)
- [mentalcard.dbss](mentalcard_dbss.md), knowledge entries (str_type=34) and categories (str_type=9)
- [titlebufflist.dbss](titlebufflist_dbss.md), title effects tooltip (str_type=37)
- [journalquest.dbss](journalquest_dbss.md), journal quest adventure log metadata (str_type=63, str_id1=group_id) and page titles/story text (str_type=18, str_id1=journal_cat_id)
- [petaction.dbss](petaction_dbss.md), pet action labels (str_type=19, str_id1=action_id)
- [employeename.dbss](employeename_dbss.md), employee names (str_type=71, str_id1=employee_name_id, str_id3=12)
- [plantworkerselect.bss](plantworkerselect_bss.md), town/node selection names (str_type=17, str_id1=selection_id)
- [planttown.bss](planttown_bss.md), town/node names (str_type=29, str_id1=node_id)
- [petequipskill.bss](petequipskill_bss.md), pet passive skill names and descriptions (str_type=10, str_id1=loc_id)
- [fairyequipskill.bss](fairyequipskill_bss.md), fairy passive skill names and descriptions (str_type=10, str_id1=loc_id)
- [buff.dbss](buff_dbss.md), buff descriptions (str_type=5, str_id1=buff_id)

---

## File Layout

The file is **zlib-compressed**:

| Offset | Type | Description                     |
| ------ | ---- | ------------------------------- |
| +0x00  | u32  | Header / uncompressed size hint |
| +0x04  | ...  | zlib-compressed record stream   |

Decompress with: `zlib.decompress(raw[4:])`

## Record Structure

Each record in the decompressed stream:

| Offset | Type        | Name     | Description                                                                |
| ------ | ----------- | -------- | -------------------------------------------------------------------------- |
| +0x00  | u32         | str_size | Length of the string (UTF-16 code units, excluding trailing padding/nulls) |
| +0x04  | u32         | str_type | String type identifier                                                     |
| +0x08  | u32         | str_id1  | Primary ID, main lookup key (matches title_id, knowledge_id, etc.)         |
| +0x0C  | u16         | str_id2  | ID part 2, secondary component of the compound ID                          |
| +0x0E  | u8          | str_id3  | ID part 3, tertiary component of the compound ID                           |
| +0x0F  | u8          | str_id4  | ID part 4, selects sub-field within the record (e.g. name vs requirement)  |
| +0x10  | UTF-16LE[]  | text     | String data (`str_size` UTF-16 code units)                                 |
| ...    | UTF-16LE[2] | padding  | Always 2 extra UTF-16 code units (4 bytes), typically `0x0000 0x0000`      |

Next record starts at: `+0x10 + str_size * 2 + 4`

## Important Types

| str_type | Meaning                                                                                    |
| -------- | ------------------------------------------------------------------------------------------ |
| 0        | General strings                                                                            |
| 1        | Title names + requirements                                                                 |
| 2        | Skill names                                                                                |
| 4        | Territory names                                                                            |
| 5        | Buff descriptions, `str_id1` = `buff.dbss` buff_id; see Type 5 below                       |
| 6        | NPC names                                                                                  |
| 7        | Zodiac sign data, `str_id1` = zodiac_id (1–12), `str_id4` selects sub-field                |
| 8        | Mount skill names                                                                          |
| 9        | Knowledge category (group) names, `str_id1` = node_id                                      |
| 10       | Skill names and descriptions, including pet and fairy passives; see Type 10 below          |
| 11       | City names, with some node names mixed in                                                  |
| 12       | Region/area names such as O'dyllita, Mountain of Eternal Winter, Valencia                  |
| 15       | Emote/pose/placeable interaction names                                                     |
| 16       | House/facility type names                                                                  |
| 17       | Town/node names, `str_id1` = selection_id from `plantworkerselect.bss`                     |
| 18       | Quest and journal page text; two key domains share this type, see Type 18 sub-fields below |
| 19       | Pet action labels, `str_id1` = `petaction.dbss` action_id                                  |
| 20       | "You have learned about [x]." knowledge messages, keyed by `str_id1` + `str_id2`           |
| 21       | Class names and descriptions, `str_id1` = class type, `str_id4` selects sub-field          |
| 22       | Worker skill names and descriptions, `str_id1` = skill ID, `str_id4` selects sub-field     |
| 23       | NPC dialogue lines, `str_id1` = dialogue ID, `str_id4` = line index                        |
| 25       | Quest chain/group names, `str_id1` = chain/group ID (matches `questgroup.dbss` group_id)   |
| 29       | Town/node names, `str_id1` = node_id from `planttown.bss`; `str_id4` selects sub-field     |
| 34       | Knowledge entry names, `str_id1` = knowledge_id / entry_id                                 |
| 37/38    | Other systems                                                                              |
| 39       | Audio voice lines                                                                          |
| 54       | NPC gift/confession response dialogue, `str_id1` = NPC ID                                  |
| 63       | Journal quest adventure log metadata, `str_id1` = group_id, `str_id2` = entry_no           |
| 71       | Employee names, `str_id1` = `employeename.dbss` employee_name_id, `str_id3` = 12           |

The parsed preview labels confirmed and useful provisional types. Unconfirmed
types are shown as `Unknown`.

### Type 1 sub-fields (`str_id4`)

| str_id4 | Meaning           |
| ------- | ----------------- |
| 0       | Title name        |
| 1       | Title requirement |

### Type 5, buff descriptions (`buff.dbss`)

Type 5 is the English form of the description stored inline in `buff.dbss`,
keyed by buff ID. 44,517 of the 44,609 buff IDs have a row, and for descriptions
that contain numbers the numbers agree in 11,027 of 12,967 cases; the rest
differ only by thousands separators (`+2560350` against `+2,560,350`).

| Field     | Value                        |
| --------- | ---------------------------- |
| `str_id1` | `buff_id` from `buff.dbss`   |
| `str_id2` | Observed `0`                 |
| `str_id3` | Observed `0`                 |
| `str_id4` | Observed `0`                 |

Buffs with an empty inline description map to the literal text `<null>`. The
buff *name* in `buff.dbss` has no LOC counterpart; it is an internal Korean
label.

| buff_id | Inline description (KR) | Type 5 text                                             |
| ------- | ----------------------- | ------------------------------------------------------- |
| 48830   | `수렵 숙련도 +70`       | `Hunting Mastery <PAColor0xffe9bd23>+70<PAOldColor>`    |
| 47694   | (empty)                 | `<null>`                                                |

### Type 7 sub-fields (`str_id4`)

| str_id4 | Meaning           | Example                               |
| ------- | ----------------- | ------------------------------------- |
| 0       | Sign name         | `"Hammer"`                            |
| 1       | Trait description | `"Brave, Conservative, Hot-Blooded."` |

### Type 10, skill names and descriptions

Type 10 holds 84,442 rows over 28,644 IDs, each a name with a description.
`petequipskill.bss` and `fairyequipskill.bss` resolve their pet and fairy
passive skills here through their `loc_id`. The same table also covers other
skill-like entries: class skills (`"Flow: Water Slice"`, described as
`"Preceding Skill: [Soaring Kick I] ..."`), pet and fairy skills
(`"Inexhaustible Well V"`), consumables (`"[Scroll] Blessing (60 min)"`), title
effects (`"[Title] The Magnus"`) and placeable furniture
(`"Stuffed Rock Elephant Head"`).

| Field     | Value                                |
| --------- | ------------------------------------ |
| `str_id1` | Skill `loc_id`                       |
| `str_id2` | Observed `0`                         |
| `str_id3` | Observed `0`                         |
| `str_id4` | Sub-field selector (see table below) |

| str_id4 | Meaning     | Example                                               |
| ------- | ----------- | ----------------------------------------------------- |
| 0       | Name        | `"Inexhaustible Well V"`                              |
| 1       | Description | `"Auto-use Purified Water/Star Anise Tea during ..."` |
| 2       | Placeholder | Always the literal text `<null>`                      |

When an entry has no real description, `str_id4=1` repeats the name.

`str_id1` is **not** the `buff.dbss` key. Only half of the buff IDs have a type
10 row at all, and where both exist the text usually disagrees: buff 47694 is
`생활 숙련도 +100 (120분)` (Life Skill Mastery +100) while type 10 47694 is
`"[Scroll] Blessing (60 min)"`. Buff text lives in type 5.

### Type 17, town/node names (`plantworkerselect.bss`)

Type 17 stores localized town and node names used as worker-selection locations.

| Field     | Value                                       |
| --------- | ------------------------------------------- |
| `str_id1` | `selection_id` from `plantworkerselect.bss` |
| `str_id2` | Observed `0`                                |
| `str_id3` | Observed `0`                                |
| `str_id4` | Observed `0`                                |

Observed English examples:

| str_id1 | Text          |
| ------- | ------------- |
| 5       | Velia         |
| 32      | Heidel        |
| 77      | Calpheon City |
| 735     | Grana         |
| 1444    | Bukpo         |

### Type 18, two domains

Type 18 is shared by regular quests and journal quest (adventure log) pages. The `str_id1` value determines which domain applies.

#### Regular quests (`quest.dbss`)

| Field     | Value                                                                  |
| --------- | ---------------------------------------------------------------------- |
| `str_id1` | `quest_chain_id`, packed lower 16 bits of the quest record's packed ID |
| `str_id2` | `quest_id`, packed upper 16 bits                                       |
| `str_id4` | Sub-field selector (see table below; provisional)                      |

| str_id4 | Meaning (provisional) |
| ------- | --------------------- |
| 0       | Quest title           |
| 1       | Summary / description |
| 2       | NPC / speaker name    |
| 3       | Objective text        |

#### Journal quest adventure log pages (`journalquest.dbss`)

| Field     | Value                                                           |
| --------- | --------------------------------------------------------------- |
| `str_id1` | `journal_cat_id`, from the page reference u32 in the entry tail |
| `str_id2` | Page number (1-based)                                           |
| `str_id4` | Sub-field selector (see table below; confirmed)                 |

| str_id4 | Meaning    | Example                             |
| ------- | ---------- | ----------------------------------- |
| 0       | Page title | `"Hey There Big Fellow!"`           |
| 1       | Story text | `"January 2\n\nMy name is Deve. …"` |

### Type 19, pet action labels (`petaction.dbss`)

Type 19 stores localized pet action labels keyed by `action_id`.

| Field     | Value                             |
| --------- | --------------------------------- |
| `str_id1` | `action_id` from `petaction.dbss` |
| `str_id2` | Observed `0`                      |
| `str_id3` | Observed `0`                      |
| `str_id4` | Observed `0`                      |

Observed English labels:

| action_id | Text   |
| --------- | ------ |
| 0         | Joy    |
| 1         | Feed   |
| 2         | Angry  |
| 3         | Sleepy |
| 4         | Jump   |
| 5         | Sit    |
| 6         | Play   |
| 7         | Crouch |
| 8         | Weep   |
| 9         | Sulky  |

### Type 20, knowledge learned messages

Type 20 holds 77 long-form "You have learned about [x]." messages, most followed
by a paragraph of lore or a hint. The key is the pair `str_id1` + `str_id2`:
`str_id1` names a group (1 to 7, 11 to 23, 51, 52, 101, 102, 151, 152, 300 to 302) and `str_id2` numbers the messages inside it (0 to 5).

| Field     | Value                          |
| --------- | ------------------------------ |
| `str_id1` | Group ID                       |
| `str_id2` | Message index within the group |
| `str_id3` | Observed `0`                   |
| `str_id4` | Observed `0`                   |

| str_id1 | str_id2 | Text (truncated)                                        |
| ------- | ------- | ------------------------------------------------------- |
| 1       | 0       | `"You have learned about [Lani]. ..."`                  |
| 1       | 1       | `"You have learned about [Uno]. ..."`                   |
| 2       | 1       | `"You have learned about [Heidel Pass]. ..."`           |
| 3       | 1       | `"You have learned about [Ancient Stone Chamber]. ..."` |

Which table owns these group IDs is not known yet.

### Type 21, class names and descriptions

Type 21 is keyed by class type. `str_id4=0` is the class name and `str_id4=1`
its description.

| Field     | Value                                |
| --------- | ------------------------------------ |
| `str_id1` | Class type                           |
| `str_id2` | Observed `0`                         |
| `str_id3` | Observed `0`                         |
| `str_id4` | Sub-field selector (see table below) |

| str_id4 | Meaning           | Example                                         |
| ------- | ----------------- | ----------------------------------------------- |
| 0       | Class name        | `"Warrior"`                                     |
| 1       | Class description | `"Warriors are skilled fighters with both ..."` |

IDs 0 to 36 are class names, including internal and retired entries such as
`"Temp Maehwa"`, `"Ain (No Use)"` and `"PBM"`. IDs 70 to 100 are placeholder
names (`"[PH] 11"` to `"[PH] 41"`) whose descriptions all repeat the Warrior
text.

| str_id1 | Name        |
| ------- | ----------- |
| 0       | Warrior     |
| 1       | Hashashin   |
| 4       | Ranger      |
| 8       | Sorceress   |
| 10      | Corsair     |
| 20      | Musa        |
| 27      | Dark Knight |
| 31      | Witch       |
| 34      | Deadeye     |

### Type 22, worker skill names and descriptions

Type 22 stores worker skill display text keyed by skill ID. `str_id4` selects the text role.

| Field     | Value                                |
| --------- | ------------------------------------ |
| `str_id1` | Worker skill ID                      |
| `str_id2` | Observed `0`                         |
| `str_id3` | Observed `0`                         |
| `str_id4` | Sub-field selector (see table below) |

| str_id4 | Meaning           | Example                |
| ------- | ----------------- | ---------------------- |
| 0       | Skill name        | `"Wings C"`            |
| 1       | Skill description | `"Movement Speed +6%"` |

Observed English examples:

| str_id1 | str_id4=0 | str_id4=1           |
| ------- | --------- | ------------------- |
| 1603    | Wings C   | Movement Speed +6%  |
| 1602    | Wings B   | Movement Speed +8%  |
| 1601    | Wings A   | Movement Speed +11% |

### Type 23, NPC dialogue lines

Type 23 holds 5,174 lines of NPC talk over 2,197 dialogue IDs (30,122 to
62,551). `str_id4` is the line index within one dialogue (0 to 6), so a
multi-line conversation is one `str_id1` with several `str_id4` rows.

| Field     | Value               |
| --------- | ------------------- |
| `str_id1` | Dialogue ID         |
| `str_id2` | Observed `0`        |
| `str_id3` | Observed `0`        |
| `str_id4` | Line index (0 to 6) |

Lines can carry inline script tags ahead of the text:

- `{AudioVoice(NPC_VCE_<id>_...)}` on 559 lines names the voice clip. For 550 of
  them `<id>` equals the line's own `str_id1`.
- `{ChangeScene(<name>)}` on 45 lines switches the camera or scene.

| str_id1 | str_id4 | Text (truncated)                                                |
| ------- | ------- | --------------------------------------------------------------- |
| 30122   | 0       | `"You hear a weird sound nearby."`                              |
| 40001   | 1       | `"{ChangeScene(IslinBartali)}Welcome. You must have come ..."`  |
| 47469   | 1       | `"{AudioVoice(NPC_VCE_47469_194_1_2_1)}Though I'm dressed ..."` |

Mostly spoken NPC dialogue rather than cutscene subtitles, although some lines
are narration (`"You hear a weird sound nearby."`).

### Type 29, town/node names (`planttown.bss`)

Type 29 stores localized town and node display text keyed by node ID. `planttown.bss` uses `str_id4=0` as the user-facing node name.

| Field     | Value                                |
| --------- | ------------------------------------ |
| `str_id1` | `node_id` from `planttown.bss`       |
| `str_id2` | Observed `0`                         |
| `str_id3` | Observed `0`                         |
| `str_id4` | Sub-field selector (see table below) |

| str_id4 | Meaning                  | Example             |
| ------- | ------------------------ | ------------------- |
| 0       | Node display name        | `"Velia"`           |
| 1       | Node category/descriptor | `"This is a city."` |

Observed English examples:

| str_id1 | str_id4=0              | str_id4=1       |
| ------- | ---------------------- | --------------- |
| 1785    | Nampo's Moodle Village | A normal node.  |
| 1623    | Grána                  | A normal node.  |
| 1301    | Valencia City          | This is a city. |
| 601     | Calpheon               | This is a city. |
| 1       | Velia                  | This is a city. |

### Type 63, journal quest metadata (`journalquest.dbss`)

Type 63 stores localized Adventure Log / journal metadata keyed by the journal group and entry number.

| Field     | Value                                |
| --------- | ------------------------------------ |
| `str_id1` | `group_id` from `journalquest.dbss`  |
| `str_id2` | `entry_no` within the journal group  |
| `str_id3` | Observed `0`                         |
| `str_id4` | Sub-field selector (see table below) |

| str_id4 | Meaning          | Example                                                                 |
| ------- | ---------------- | ----------------------------------------------------------------------- |
| 0       | Category title   | `"Igor Bartali's Adventures"`                                           |
| 1       | Subtitle         | `"Logs of Velia's Chief Igor Bartali's youthful past"`                  |
| 2       | Unlock condition | `"Reach Lv. 57, accept and complete ..."`                               |
| 3       | Volume title     | `"Deve's Encyclopedia - Volume 1\nThe Altinovan on all things random!"` |

Some journal groups do not have unlock-condition rows (`str_id4=2`), and placeholder group 8 may have no type 63 rows.

### Type 71, employee names (`employeename.dbss`)

Type 71 stores localized employee display names keyed by `employee_name_id`.

| Field     | Value                                       |
| --------- | ------------------------------------------- |
| `str_id1` | `employee_name_id` from `employeename.dbss` |
| `str_id2` | Observed `0`                                |
| `str_id3` | Observed `12`                               |
| `str_id4` | Observed `0`                                |

Observed English examples:

| employee_name_id | Text      |
| ---------------- | --------- |
| 1                | Philav    |
| 15               | Neil Moss |
| 34               | Pilgrave  |
| 47               | Guile     |
| 60               | Tails     |

## Suggested UI Layout

| Column        | Type | Notes                                                       |
| ------------- | ---- | ----------------------------------------------------------- |
| Id1           | num  | `str_id1`                                                   |
| Id2           | num  | `str_id2`                                                   |
| Id3           | num  | `str_id3`                                                   |
| Id4           | num  | `str_id4`                                                   |
| Type (number) | num  | `str_type`                                                  |
| Type (text)   | text | Human-readable label for confirmed types, otherwise Unknown |
| Text          | text | Localized string                                            |

## Notes

- All four ID fields together form a compound identifier; `str_id1` is the primary lookup key.
- The same `str_id1` can appear multiple times with `str_type=1`:
  one entry for the title name (`str_id4=0`), one for the requirement text (`str_id4=1`).
- `str_id1` matches `title_id` in `title.dbss` and `titleoffset.dbss`.
- For `str_type=54`, `str_id1` matches `npc_id` in `npcgiftdata.dbss` and
  provides the English localized gift/confession response dialogue.
- The file is located on disk at `<paz_root_parent>/ads/languagedata_en.loc`
  (one level above the PAZ folder) and is pre-loaded by the browser as a companion for all handlers.
- To get a loc file you dont have go here:
  http://nez-o-dn.playblackdesert.com/UploadData/ads_files copy the number and replace x here:
  http://nez-o-dn.playblackdesert.com/UploadData/ads/languagedata_ru/x/languagedata_ru.loc

  and also the ru if you need another one.

## Open Questions

### Type 10 key namespace

Pet and fairy passives confirm that `str_id1` is a skill `loc_id`, but class
skills (`"Flow: Water Slice"`), scrolls and title effects share the same ID
space. Which table owns the full range, possibly `skilltype.dbss` once its keys
are decoded, is not known.

### Type 20 group owner

Which table owns the `str_id1` group IDs of the knowledge learned messages is
not known.
