# `languagedata_en.loc` Format

## Purpose

Stores all localized strings for the game, keyed by a compound ID (str_type, str_id1–4). Used as the primary English text source across all file format handlers.

Example:

```text
str_type: 1, str_id1: 44, str_id4: 0  →  "Stoneback Crab Artisan"
str_type: 7, str_id1: 1,  str_id4: 0  →  "Hammer"
str_type: 54, str_id1: 40012          →  "Thank you! I really like this."
```

## Graph

### Tags

- file format
- loc
- localization

### Connections

- [title.dbss](title_dbss.md) — title names and requirements (str_type=1)
- [zodiacsign.dbss](zodiacsign_dbss.md) — zodiac sign names and traits (str_type=7)
- [npcgift.dbss](npcgift_dbss.md) — NPC gift dialogue (str_type=54)
- [mentalcard.dbss](mentalcard_dbss.md) — knowledge entries (str_type=34) and categories (str_type=9)
- [titlebufflist.dbss](titlebufflist_dbss.md) — title effects tooltip (str_type=37)
- [journalquest.dbss](journalquest_dbss.md) — journal quest adventure log metadata (str_type=63, str_id1=group_id) and page titles/story text (str_type=18, str_id1=journal_cat_id)

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
| +0x08  | u32         | str_id1  | Primary ID — main lookup key (matches title_id, knowledge_id, etc.)        |
| +0x0C  | u16         | str_id2  | ID part 2 — secondary component of the compound ID                         |
| +0x0E  | u8          | str_id3  | ID part 3 — tertiary component of the compound ID                          |
| +0x0F  | u8          | str_id4  | ID part 4 — selects sub-field within the record (e.g. name vs requirement) |
| +0x10  | UTF-16LE[]  | text     | String data (`str_size` UTF-16 code units)                                 |
| ...    | UTF-16LE[2] | padding  | Always 2 extra UTF-16 code units (4 bytes), typically `0x0000 0x0000`      |

Next record starts at: `+0x10 + str_size * 2 + 4`

## Important Types

| str_type | Meaning                                                                                     |
| -------- | ------------------------------------------------------------------------------------------- |
| 0        | General strings                                                                             |
| 1        | Title names + requirements                                                                  |
| 2        | Skill names                                                                                 |
| 4        | Territory names                                                                             |
| 5        | Buff/effect text; some rows include the buff name plus effect, most only effect             |
| 6        | NPC names                                                                                   |
| 7        | Zodiac sign data — `str_id1` = zodiac_id (1–12), `str_id4` selects sub-field                |
| 8        | Mount skill names                                                                           |
| 9        | Knowledge category (group) names — `str_id1` = node_id                                      |
| 10       | Buff effects / fairy skill names; exact split is not confirmed                              |
| 11       | City names, with some node names mixed in                                                   |
| 12       | Region/area names such as O'dyllita, Mountain of Eternal Winter, Valencia                   |
| 15       | Emote/pose/placeable interaction names                                                      |
| 16       | House/facility type names                                                                   |
| 18       | Quest and journal page text; two key domains share this type — see Type 18 sub-fields below |
| 25       | Quest chain/group names — `str_id1` = chain/group ID (matches `questgroup.dbss` group_id)   |
| 34       | Knowledge entry names — `str_id1` = knowledge_id / entry_id                                 |
| 37/38    | Other systems                                                                               |
| 39       | Audio voice lines                                                                           |
| 54       | NPC gift/confession response dialogue — `str_id1` = NPC ID                                  |
| 63       | Journal quest adventure log metadata — `str_id1` = group_id, `str_id2` = entry_no           |

The parsed preview labels confirmed and useful provisional types. Unconfirmed
types are shown as `Unknown`.

### Type 1 sub-fields (`str_id4`)

| str_id4 | Meaning           |
| ------- | ----------------- |
| 0       | Title name        |
| 1       | Title requirement |

### Type 7 sub-fields (`str_id4`)

| str_id4 | Meaning           | Example                               |
| ------- | ----------------- | ------------------------------------- |
| 0       | Sign name         | `"Hammer"`                            |
| 1       | Trait description | `"Brave, Conservative, Hot-Blooded."` |

### Type 18 — two domains

Type 18 is shared by regular quests and journal quest (adventure log) pages. The `str_id1` value determines which domain applies.

#### Regular quests (`quest.dbss`)

| Field     | Value                                                                   |
| --------- | ----------------------------------------------------------------------- |
| `str_id1` | `quest_chain_id` — packed lower 16 bits of the quest record's packed ID |
| `str_id2` | `quest_id` — packed upper 16 bits                                       |
| `str_id4` | Sub-field selector (see table below; provisional)                       |

| str_id4 | Meaning (provisional) |
| ------- | --------------------- |
| 0       | Quest title           |
| 1       | Summary / description |
| 2       | NPC / speaker name    |
| 3       | Objective text        |

#### Journal quest adventure log pages (`journalquest.dbss`)

| Field     | Value                                                            |
| --------- | ---------------------------------------------------------------- |
| `str_id1` | `journal_cat_id` — from the page reference u32 in the entry tail |
| `str_id2` | Page number (1-based)                                            |
| `str_id4` | Sub-field selector (see table below; confirmed)                  |

| str_id4 | Meaning    | Example                             |
| ------- | ---------- | ----------------------------------- |
| 0       | Page title | `"Hey There Big Fellow!"`           |
| 1       | Story text | `"January 2\n\nMy name is Deve. …"` |

### Type 63 — journal quest metadata (`journalquest.dbss`)

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

## Example

str_type: 1, str_id1: 218, text: "Mudskipper Enthusiast"

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
