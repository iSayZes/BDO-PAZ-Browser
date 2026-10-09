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

## File Layout

The file is zlib-compressed:

| Offset | Type | Description                     |
| ------ | ---- | ------------------------------- |
| +0x00  | u32  | Exact size of the decompressed record stream (`227,667,486` bytes in the current English file) |
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
| ...    | u32         | terminator | Always `0` (all 1,421,290 records in the current English file)           |

Next record starts at: `+0x10 + str_size * 2 + 4`

The four bytes at `+0x0C` can also be read as one u32 selector, as
[bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) does (their
`key1`): the high byte is `str_id4`, the field or column, and the low 24 bits
are `str_id2 | str_id3 << 16`. Their `key0` is `str_type` and their `id` is
`str_id1`. The current English file holds 1,421,290 strings in 116 types.

## Important Types

| str_type | Meaning                                                                                    |
| -------- | ------------------------------------------------------------------------------------------ |
| 0        | Item text, `str_id1` = item ID; see Type 0 below                                           |
| 1        | Title names + requirements                                                                 |
| 2        | Skill command text, `str_id1` = skill number; `str_id4=0` name, `1` and `2` key-binding combos |
| 4        | Territory names                                                                            |
| 5        | Buff descriptions, `str_id1` = `buff.dbss` buff_id; see Type 5 below                       |
| 6        | Character names (NPCs, monsters, gathering nodes, objects, houses), `str_id1` = character ID; `str_id4=1` is a secondary label such as `<Open>` |
| 7        | Zodiac sign data, `str_id1` = zodiac_id (1–12), `str_id4` selects sub-field                |
| 8        | Mount skill names                                                                          |
| 9        | Knowledge category (theme) names, `str_id1` = `mentaltheme.dbss` theme_id; also the bookshelf themes of `buff.dbss` type 101 |
| 10       | Skill names and descriptions, `str_id1` = skill number; see Type 10 below                  |
| 11       | City names, with some node names mixed in                                                  |
| 12       | Territory names, `str_id1` = territory 0 to 13; `str_id4=0` nation or realm, `1` territory; see Type 12 below |
| 13       | Skill rank texts, `str_id1` = skill number, `str_id2` = level; English of the `skill.dbss` `description`, see Type 13 below |
| 15       | Emote/pose/placeable interaction names                                                     |
| 16       | House/facility type names                                                                  |
| 17       | Region names, `str_id1` = `region_key` from `regioninfo.bss`; the `plantworkerselect.bss` selection IDs and the towns of the `buff.dbss` worker contracts and storage expansions are region keys; see Type 17 below |
| 18       | Quest and journal page text; two key domains share this type, see Type 18 sub-fields below |
| 19       | Pet action labels, `str_id1` = `petaction.dbss` action_id                                  |
| 20       | "You have learned about [x]." knowledge messages, keyed by `str_id1` + `str_id2`           |
| 21       | Class names and descriptions, `str_id1` = class type, `str_id4` selects sub-field          |
| 22       | Worker skill names and descriptions, `str_id1` = skill ID, `str_id4` selects sub-field     |
| 23       | NPC dialogue lines, `str_id1` = dialogue ID, `str_id4` = line index                        |
| 25       | Quest chain/group names, `str_id1` = chain/group ID (matches `questgroup.dbss` group_id)   |
| 28       | `recommendationquest.bss` group names (`str_id1` = group key, `str_id4=0`) and quest condition lines (`str_id1` = packed quest ID, `str_id2` = group key, `str_id4=1`); see Type 58 below |
| 29       | Town/node names, `str_id1` = node_id from `planttown.bss`; `str_id4` selects sub-field     |
| 34       | Knowledge card text, `str_id1` = `mentalcard.dbss` card_id; see Type 34 below              |
| 37       | UI string sheets, `str_id1` = `stringtable.bss` key hash; see Type 37 below                |
| 38       | Other systems                                                                              |
| 39       | Audio voice lines                                                                          |
| 42       | `repetitionquest.bss` group names (`str_id1` = group key, `str_id4=0`) and quest condition lines (`str_id1` = packed quest ID, `str_id2` = group key, `str_id4=1`); see Type 58 below |
| 43       | `mainquest.bss` group names (`str_id1` = group key, `str_id4=0`) and quest condition lines (`str_id1` = packed quest ID, `str_id2` = group key, `str_id4=1`); see Type 58 below |
| 44       | Central Market categories, `str_id1` = main category; see Type 44 below                    |
| 50       | Pearl Shop product names and descriptions, `str_id1` = `cashproduct.dbss` product_id, `str_id3` = service code; see Type 50 below |
| 52       | Item-set bonus text, `str_id1` = `skillpiece.dbss` key; see Type 52 below                  |
| 54       | NPC gift/confession response dialogue, `str_id1` = NPC ID                                  |
| 58       | `newquest.bss` group names (`str_id1` = group key, `str_id4=0`) and quest condition lines (`str_id1` = packed quest ID, `str_id2` = group key, `str_id4=1`); see Type 58 below |
| 63       | Journal quest adventure log metadata, `str_id1` = journal_key, `str_id2` = book_key         |
| 71       | Employee names, `str_id1` = `employeename.dbss` employee_name_id, `str_id3` = 12           |
| 113      | Lightstone combination names with their effects (`"[Imperial Chef] Cooking Mastery +30"`, name and effect split by a newline), `str_id1` = `lightstoneset.bss` set ID, 1 to 182 |
| 115      | Monster Zone Info categories (`"Elvia Realm"`, `"Region Quests"`), `str_id1` = `dropuisubcategoryinfo.bss` key 1 to 8 |
| 116      | Monster Zone Info zone names (`"Sherekhan Necropolis (Day)"`), `str_id1` = `dropuihuntinggroundinfo.bss` key; 113 IDs from 0 to 119, 49 has no row |
| 117      | Monster Zone Info tags, `str_id1` = `dropuihuntinggroundinfo.bss` tag key; `str_id4=0` tag (`"#LotsOfMobs"`), `1` tag description |
| 121      | Crystal transfusion groups, `str_id1` = group, `str_id2` = equip limit; see Type 121 below  |
| 123      | Workshop and house use names (`"Refinery"`, `"Worker's Lodging"`), `str_id1` 0 to 35       |

The parsed preview labels confirmed and useful provisional types. Unconfirmed
types are shown as `Unknown`.

### Type 0, item text

Type 0 holds 294,351 rows over 73,947 item IDs, four fields per item.

| str_id4 | Meaning           | Example                                                         |
| ------- | ----------------- | --------------------------------------------------------------- |
| 0       | Item name         | `"[Event] Golden Gilded Coin"`                                  |
| 1       | Description       | `"You'll be able to use an awakening weapon. ..."`              |
| 2       | Use confirmation  | `"The item will disappear and you will gain 5 Crystal Inventory slots ..."`; `<null>` on most items |
| 3       | Exchange text     | `"<Trent>\n- Exchange 100: 30,000 Silver"`; non-null on 110 items |

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

Type 10 holds 86,692 rows over 29,398 IDs, each a name with a description.
`str_id1` is the skill number (`skillNo`). [`skill.dbss`](skill_dbss.md) and
[`skilltype.dbss`](skilltype_dbss.md) key their records with a u32
`skillNo << 16 | skillLevel`, and on client 3458 28,343 of the 29,398 type 10
IDs are skill numbers there. The Korean `skilltype.dbss` names match the English
text: skill `62480` is `칼페온 - 가공 경험치 획득량 +20%` and type 10 `62480` is
`"Calpheon - Processing EXP +20%"`; skill `47059` is `[칭호] 제일 큰 흑새치를 낚은`
and type 10 is `"[Title] The Biggest Black Marlin"`. Type 10 has no level
dimension: every row has `str_id2 = str_id3 = 0`, so all ranks of one
`skillNo` share one name. 2,009 skill numbers have no type 10 row, and 1,055
type 10 IDs (for example `16626` to `16635`) have no skill record.

`petequipskill.bss` and `fairyequipskill.bss` resolve their pet and fairy
passive skills here through their `loc_id`, which is therefore a skill number.
The same table covers every skill-like entry: class skills (`"Flow: Water Slice"`, described as
`"Preceding Skill: [Soaring Kick I] ..."`), pet and fairy skills
(`"Inexhaustible Well V"`), consumables (`"[Scroll] Blessing (60 min)"`), title
effects (`"[Title] The Magnus"`) and placeable furniture
(`"Stuffed Rock Elephant Head"`).

| Field     | Value                                |
| --------- | ------------------------------------ |
| `str_id1` | Skill number (`skillNo`)             |
| `str_id2` | Observed `0`                         |
| `str_id3` | Observed `0`                         |
| `str_id4` | Sub-field selector (see table below) |

| str_id4 | Meaning     | Example                                               |
| ------- | ----------- | ----------------------------------------------------- |
| 0       | Name        | `"Inexhaustible Well V"`                              |
| 1       | Description | `"Auto-use Purified Water/Star Anise Tea during ..."` |
| 2       | Placeholder | The literal text `<null>` on 27,961 of 27,972 rows    |

When an entry has no real description, `str_id4=1` repeats the name.

`str_id1` is **not** the `buff.dbss` key. Only half of the buff IDs have a type
10 row at all, and where both exist the text usually disagrees: buff 47694 is
`생활 숙련도 +100 (120분)` (Life Skill Mastery +100) while type 10 47694 is
`"[Scroll] Blessing (60 min)"`. Buff text lives in type 5.

### Type 12, territories

Type 12 has 14 IDs, each with a nation or realm name and a territory name.
This is a different key space from type 4, whose IDs 0 to 11 are territory
display names such as `"Balenos Territory"`.

| str_id1 | str_id4=0            | str_id4=1       |
| ------- | -------------------- | --------------- |
| 0       | Republic of Calpheon | Balenos         |
| 1       | Republic of Calpheon | Serendia        |
| 4       | Kingdom of Valencia  | Valencia        |
| 12      | Alyaelli             | Outer Edania    |
| 13      | Alyaelli             | Inner Edania    |

### Type 13, skill rank texts (`skill.dbss`)

Type 13 holds 28,869 rows, one per `str_id1 = skill_no`, `str_id2 = level`
(`1` on all but 66), `str_id3 = str_id4 = 0`. 28,537 keys are `skill.dbss`
ranks, and each text is the English of that rank's Korean `description`;
8,383 are real text, the rest `<null>`, and set effect skills store `0`.

| Key           | Text                                                          |
| ------------- | ------------------------------------------------------------- |
| `(65069, 1)`  | `"- Effect:
Adds 10 slots to the Guild Storage."` (tagged)  |
| `(61612, 1)`  | `"Can register Exploration Node."`                           |
| `(15313, 1)`  | `"Summon Cannon"`                                             |

Where type 10 `str_id4 = 1` also exists the two are usually equal; on guild
skills type 10 holds a usage hint and type 13 the effect. See
`skill_dbss.md`, Notes.

### Type 17, region names (`regioninfo.bss`)

Type 17 names every region of [`regioninfo.bss`](regioninfo_bss.md): towns,
hunting grounds, castles, arenas, caves and sea areas. Towns are regions, so
the worker-selection towns of `plantworkerselect.bss` (all 31 selection IDs are
region keys of type `MainTown` or `MinorTown`) and the towns of the `buff.dbss`
worker contracts and storage expansions use the same keys. All 1594 region keys
of client 3458 resolve; 64 of the 1658 type 17 IDs (750, 807 to 809, 821 ...)
have no region.

| Field     | Value                                                                       |
| --------- | --------------------------------------------------------------------------- |
| `str_id1` | `region_key` from `regioninfo.bss` (= `selection_id` in `plantworkerselect.bss`) |
| `str_id2` | Observed `0`                                                                |
| `str_id3` | Observed `0`                                                                |
| `str_id4` | Observed `0`                                                                |

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
| 4 to 6  | Dialogue text, about 29,700 rows each                     |
| 7 to 9  | Rare extra lines (103, 28 and 93 rows)                    |

#### Journal quest adventure log pages (`journalquest.dbss`)

| Field     | Value                                                           |
| --------- | --------------------------------------------------------------- |
| `str_id1` | `page_quest_id & 0xFFFF` (quest chain ID of the page)           |
| `str_id2` | `page_quest_id >> 16` (quest ID, no offset)                     |
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

### Type 34, knowledge card text (`mentalcard.dbss`)

Type 34 holds 37,529 rows over 12,751 IDs. `str_id1` is the `mentalcard.dbss`
`card_id`; 12,485 of the 12,502 cards have a name row.

| str_id4 | Meaning          | Rows   | Example                                                         |
| ------- | ---------------- | ------ | --------------------------------------------------------------- |
| 0       | Card name        | 12,751 | `"Rainbow Fox"`                                                 |
| 1       | Description      | 12,751 | `"A gigantic squid native to Margoria Sea. ..."`                |
| 2       | Acquisition text | 12,027 | `"Can be obtained through [Interaction]"`                       |

The three fields are the English forms of the card's inline Korean name,
description and acquisition strings.

### Type 37, UI string sheets

Type 37 holds 54,094 UI strings, the translations of
[`stringtable.bss`](stringtable_bss.md). `str_id1` is the hash of the string
key (`LUA_WIDGET_TOWNNPCNAVI_NPCTYPETEXT_6` -> `0x4D282741`), which
`stringtable.bss` stores next to each key. `str_id2` is the sheet the key sits
in:

| str_id2 | Sheet         | Holds                                   |
| ------- | ------------- | --------------------------------------- |
| 0       | `CUTSCENE`    | Cutscene subtitles                      |
| 1       | `GAME`        | Lua UI strings, labels and tooltips     |
| 2       | `RESOURCE`    | UI panel resources                      |
| 3       | `ACTIONCHART` | Speech bubbles and action lines         |
| 4       | `TOOL`        | Enum labels                             |
| 5       | `WEB`         | In-game web page strings                |
| 6       | `SymbolNo`    | Server error and result messages        |
| 7       | `IMAGESLIDE`  | Image slide subtitles                   |

`str_id3` is `0`, or `1` for a second variant of the key (352 rows, mostly
regional URLs and date lines); `str_id4` is always `0`.
`titlebufflist.dbss` uses this type for its tooltip text.

### Type 44, Central Market categories

Type 44 has 18 main categories (`str_id1` `1` to `85` in steps of 5) and 421
rows.

| Selector                         | Meaning                          | Example (category 55)          |
| -------------------------------- | -------------------------------- | ------------------------------ |
| `str_id2=0, str_id3=0`           | Main category name               | `"Pearl Item"`                 |
| `str_id2=n, str_id3=0`           | Sub-category `n`                 | `str_id2=7` `"Mount"`          |
| `str_id2=0, str_id3=n`           | Filter option `n`                | `str_id3=9` `"Kunoichi"`       |

The filter options depend on the category: enhancement levels `+ 0` to
`PEN (V)` for weapons, armor and life tools, `+ 0` to `+ 10` for mounts, ships
and wagons, `+ 0` to `DEC (X)` for accessories, grades for Alchemy Stones, crystal kinds for Magic
Crystals, class names for Pearl Items and colours for Dyes. Materials, Enhancement,
Consumables, Furniture and Lightstones have none.

### Type 50, Pearl Shop products (`cashproduct.dbss`)

Type 50 holds 105,534 rows over 29,130 IDs on client 3458. `str_id1` is the
`cashproduct.dbss` `product_id` (all 28,945 products have rows), `str_id2` is
`0`, `str_id3` is a service code and `str_id4` selects the string:

| str_id4 | Meaning            | Rows (code 12) | Example                                                    |
| ------- | ------------------ | -------------- | ---------------------------------------------------------- |
| 0       | Product name       | 29,115         | `"Polar Bear <PAColor0xffe9bd23>(Tier 3)<PAOldColor>"`      |
| 1       | Name, first part   | 29,115         | `"[Dosa] Yeoreum"`                                          |
| 2       | Name, second part  | 18,040         | `"Gloves"`                                                  |
| 3       | Description        | 29,115         | `"... <PAColor0xffe9bd23>※ Contains:<PAOldColor> ..."`      |

Fields 1 and 2 split the name in two where it is long; field 1 repeats the
whole name otherwise. Names and descriptions carry `<PAColor>` tags.

One code covers nearly every product of a file: `12` on 105,385 of the en
rows (also the main code of the de, fr and sp files) and `8` in the ru file.
A few products also or only have rows under other codes (en: `1` on 23
products, `26`, `28`, `6`, `20` and `0` on a handful). Under code `1` the
same product can read differently, e.g. product 21007 is `[Loyalty] Unknown
Dye Box` under 12 and `[Loyalty] Unknown Dye Box (Used once per day)` under 1.
The app reads the code most products use and falls back to a product's lowest
code. Type 71 keeps `12` in `str_id3` too.

### Type 52, item-set bonus text (`skillpiece.dbss`)

Type 52 holds 448 rows over 93 IDs. `str_id1` is the `skillpiece.dbss`
record key (87 of the 93 IDs; 89 are also skill numbers in `skill.dbss`).
`str_id2` is the tier's `apply` value and `str_id4` selects the string:

| str_id4 | Meaning                   | Example                          |
| ------- | ------------------------- | -------------------------------- |
| 0       | Bonus description         | `"Skill EXP +10%"`               |
| 1       | Piece-count label         | `"2 Parts"`                      |
| 2       | Set group title           | `"Agris Set Effect"`             |

The selector split follows the notes of
[bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor).

### Types 58, 43, 28 and 42, quest lists (`newquest.bss`, `mainquest.bss`, `recommendationquest.bss`, `repetitionquest.bss`)

Type 58 holds 1,883 rows. `str_id4 = 0` rows name the list's groups,
`str_id1` = the group key in `newquest.bss` (265 keys, 1 to 322); the
`str_id4 = 1` rows are one condition line per quest of a group,
`str_id1` = packed quest ID (`quest_id << 16 | chain`), `str_id2` = the
group key, e.g. `(132178, 3)` `Complete <PAColor0xfff3d900>A Struggle with the
Seagull<PAOldColor>`. Every `newquest.bss` group and row has its row on client 3458.

Types 43, 28 and 42 have the same two-field shape and hold the text of
the other three quest lists, which share the `newquest.bss` layout: type 43
names the `mainquest.bss` chains (key 104 `[Special Growth] Taking My Own
Path`), type 28 the `recommendationquest.bss` groups (key 165 `[Life 101]
The Adventurer That Does It All`) and type 42 the `repetitionquest.bss`
groups (key 51 `[Throne of Edana] [Weekly] For the Throne`). On client 3458
every group of the three files has a name and every row a condition line.
Each type has more names than its file has groups (170 for 120, 192 for
122, 54 for 48).

### Type 63, journal quest metadata (`journalquest.dbss`)

Type 63 stores localized Adventure Log / journal metadata keyed by the journal key and book key.

| Field     | Value                                |
| --------- | ------------------------------------ |
| `str_id1` | `journal_key` from `journalquest.dbss` |
| `str_id2` | `book_key` within the journal        |
| `str_id3` | Observed `0`                         |
| `str_id4` | Sub-field selector (see table below) |

| str_id4 | Meaning          | Example                                                                 |
| ------- | ---------------- | ----------------------------------------------------------------------- |
| 0       | Category title   | `"Igor Bartali's Adventures"`                                           |
| 1       | Subtitle         | `"Logs of Velia's Chief Igor Bartali's youthful past"`                  |
| 2       | Unlock condition | `"Reach Lv. 57, accept and complete ..."`                               |
| 3       | Volume title     | `"Deve's Encyclopedia - Volume 1\nThe Altinovan on all things random!"` |

In the current client, `str_id4=0`, `1` and `3` exist for all 112 books and `str_id4=2` exists for exactly the 61 books with a non-empty Korean unlock requirement. Rows with `str_id2=0` and a journal key `13` exist without matching `journalquest.dbss` records.

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

### Type 121, crystal transfusion groups

Type 121 has 44 rows over 43 group IDs (1 to 103). `str_id2` is the
group's equip limit (I confirmed it in game for Viper `2` and Ultimate Hoom `4`,
2026-09-27): `1` for `"Primordial"`, `"Ancient Spirit"` and `"Edania"`, `2` for
most groups (`"Viper"`, `"Max HP"`), `4` for `"Ultimate Hoom"`, `6` for
`"Dawn"`, and `1000` for `"No Group"`, `"Hoom"`, `"Macalod"` and `"Gervish"`.
Group `26` (`"Dim Magic"`) has rows at both `2` and `6`.

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
- To get a loc file you don't have, copy the number from
  http://nez-o-dn.playblackdesert.com/UploadData/ads_files and replace x with it here:
  http://nez-o-dn.playblackdesert.com/UploadData/ads/languagedata_ru/x/languagedata_ru.loc

  For another language, replace the ru as well.

## Open Questions

### Type 26 key

Type 26 holds 84,552 rows over 14,000 IDs, `str_id2` from 0 up, `str_id3`
and `str_id4` 0; only 1,799 rows on 449 IDs are text, the rest `<null>`.
`str_id1` looks like an item ID: 10078 is Ramones's Longsword and its rows
read `Item Effects: Extra Damage to All Species +5 / Enhancement Effects:
AP, Accuracy, Extra Damage to All Species Increase`, and outfits read
`Equip Effect: Death Penalty -10% / Set Effect: Combat EXP +10%`. But
`str_id2` is not the `itemenchant.dbss` enhancement level: weapons have
rows 1 to 20 and outfits 2 to 4 where the file has blocks for levels 0 or
0 and 1 only (408 of 449 IDs), and 40 IDs are no item at all (25321 to
25325 change per `str_id2` like ship parts, `Max Rations +10,000` at 0 to
`+28,000` at 10). The table that owns these keys is not found yet, so no
column shows type 26.

### Type 50 service codes

Which service each `str_id3` code stands for is not known. `12` is the main
code of the en, de, fr and sp files and `8` of the ru file; `1`, `6`, `20`,
`26` and `28` hold a few products each, some of them old Loyalty items.

### Type 20 group owner

Which table owns the `str_id1` group IDs of the knowledge learned messages is
not known. The groups are not `mentaltheme.dbss` themes or `knowledgelearning.dbss`
sources: groups `1` to `7`, `51`, `52`, `101`, `102` and `151` each hold four to
six unrelated tips (group `1` mixes `[Lani]`, `[Uno]` and `[River and Ocean Fish]`),
while groups `11` to `15`, `16` to `20` and `300` to `302` repeat one message
(`Olivia`, `Elixir of Old Memory`, `Study: Farmer Drunk on the Scent of Grapes`)
with different lore text. That pattern suggests quest or dialogue scripts pick
the message by group and index.

### Type 123 key

bdo-data-extractor keys type 123 by the client's `eHouseIconType` enum. No
file we decode uses that enum yet, so the key is not confirmed.
