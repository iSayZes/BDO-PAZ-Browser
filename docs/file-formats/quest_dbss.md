# `quest.dbss` Format

## Purpose

Quest definition table. Each record stores a quest ID, prerequisite/evaluation script, objective/action script, Korean objective text, rich text payloads, quest icon path, and trailing state/config fields.

Example:

```text
quest_id: 125285
condition: checkFieldType(hadumField);getLevel()>59;clearquest(2080,10);
objective: <악몽의 그림자> 기가고드 처치하기;
icon: Icon/Quest/Hadum08.dds
```

## Graph

### Tags

- file format
- dbss
- quest

### Connections

- [languagedata_en.loc](languagedata_loc.md) — English quest title/text strings, mapped to LOC `str_type=18` with `str_id1=quest_chain_id` and `str_id2=quest_id`; `str_type=39` appears to contain voice/dialogue lines and should not be used as quest title text
- [allquestlist.bss](allquestlist_bss.md) — PABR list of canonical/display packed quest IDs; count matches `quest.dbss`, and most extracted `canonical_link` IDs resolve into this list
- [questgroup.dbss](questgroup_dbss.md) — groups quest chains and lists child quest IDs that resolve to `quest.dbss`
- [journalquest.dbss](journalquest_dbss.md) — adventure log / journal quest category data; related quest format with its own offset index

---

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `allquestlist.bss`    | Optional | Canonical/display packed quest ID list using the same ID scheme      |
| `languagedata_en.loc` | Optional | English quest strings; raw `quest.dbss` stores Korean objective text |
| `questgroup.dbss`     | Optional | Quest chain/group metadata; links group names to child quest IDs     |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                      |
| ------- | ---- | ----- | ------------------------------------------ |
| `+0x00` | u32  | count | Number of quest records; observed: `19599` |

### Record Stream

Records start immediately after the header at `+0x04`. Records are variable length and are not preceded by an offset table in the observed archive. Some records can be identified by a repeated packed ID pair followed by a length-prefixed UTF-16-LE script field, but this only covers part of the file.

The first observed record starts at file offset `0x00000004`; the next confirmed record starts at `0x000005F8`.

The header declares `19,599` records. The preview currently anchors `19,481`
rows from quest icon paths, extracts `16,977` canonical display IDs from
`canonical_link` sub-records, and fully decodes `7,850` rows whose script layout
is recognized. Rows whose alternate layout is not decoded yet are shown as
icon-only instead of being hidden.

Many rows appear to be quest step/config records rather than canonical quest
title records. The preview therefore prefers the embedded `canonical_link`
display ID when present, then falls back to the record-start packed ID.

---

## Record Structure

### Quest Record (variable length)

Two record types share the same layout. In **step records** both ID slots are equal; in **canonical quest records** `packed_quest_id_a` holds a small internal type/step value and `packed_quest_id_b` holds the canonical display ID that matches `allquestlist.bss` and `LOC str_type=18`. When parsing, use `packed_quest_id_b` when `a ≠ b`, otherwise use `packed_quest_id_a`.

| Offset  | Type                 | Field             | Notes                                                                                  |
| ------- | -------------------- | ----------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u32                  | packed_quest_id_a | Step records: same as b. Canonical records: small internal type/step value             |
| `+0x04` | u32                  | packed_quest_id_b | Step records: same as a. Canonical records: display packed ID `(quest_id << 16) \| quest_chain_id` |
| `+0x08` | u32                  | unknown_08        | Observed `0` in sampled records                                                        |
| `+0x0C` | u32                  | condition_len     | UTF-16 code unit count for `condition_script`                                          |
| `+0x10` | u32                  | condition_zero    | Observed `0`                                                                           |
| `+0x14` | utf16le[len]         | condition_script  | Quest availability / prerequisite expression                                           |
| varies  | u32                  | action_len        | UTF-16 code unit count for `action_script`                                             |
| varies  | u32                  | action_zero       | Observed `0`                                                                           |
| varies  | utf16le[len]         | action_script     | Completion target/action expression                                                    |
| varies  | u8[]                 | zero_padding_a    | Zero padding before objective text length; length varies                               |
| varies  | u32                  | objective_len     | UTF-16 code unit count for `objective_text_kr`                                         |
| varies  | u32                  | objective_zero    | Observed `0`                                                                           |
| varies  | utf16le[len]         | objective_text_kr | Korean objective text shown in quest UI                                                |
| varies  | u8[]                 | unknown_payload   | Mixed sub-records, rich text, and reward data; includes `canonical_link` sub-record (see below) and PAColor markup in some rows |
| varies  | ascii nul-terminated | icon_path         | Quest icon path such as `Icon/Quest/Hadum08.dds`; appears near the tail of each record |
| varies  | u8[]                 | unknown_tail      | Numeric flags/config values after icon path                                            |

### Canonical Link Sub-record

Every record's `unknown_payload` contains at least one sub-record with the following layout, identified by the magic marker `0x003BAE30`:

| Offset  | Type | Field              | Notes                                                                 |
| ------- | ---- | ------------------ | --------------------------------------------------------------------- |
| `+0x00` | u32  | magic              | Always `0x003BAE30` (`\x30\xae\x3b\x00`)                             |
| `+0x04` | u32  | link_type          | Quest category/type tag; values `0..15` and `18` observed; values > 31 are noise/false positives |
| `+0x08` | u32  | canonical_quest_id | Packed display quest ID `(quest_id << 16) \| quest_chain_id`; matches `allquestlist.bss` and LOC `str_type=18` |

To extract the canonical quest ID from a record: search the payload for the first occurrence of `\x30\xae\x3b\x00` where the following `link_type` ≤ 31 and `canonical_quest_id` ≠ 0.

Some records contain multiple magic markers; false positives have `link_type > 31`. When a record has two valid canonical links, the first one (smallest offset) is the primary display quest.

#### Observed `link_type` values

| link_type | Count | Apparent category |
| --------: | ----: | ----------------- |
| `0`  | 408   | Character progression / world knowledge |
| `1`  | 3,651 | Main story / zone quests |
| `2`  | 5,485 | Regular repeatable / item quests |
| `3`  | 2,368 | Daily / weekly / repeat quests |
| `4`  | 164   | Dungeon / instance quests (e.g. Atoraxxion) |
| `5`  | 562   | Side story / life content |
| `6`  | 153   | Fishing quests |
| `7`  | 285   | Cooking quests |
| `8`  | 612   | Crafting / equipment quests (e.g. Blackstar) |
| `9`  | 1,946 | Event quests (`[Event]` prefix) |
| `10` | 1     | Guild quests (single observed) |
| `11` | 659   | Main narrative / storybook quests |
| `12` | 147   | Season / weekly quests |
| `13` | 174   | Black Spirit Pass progression quests |
| `14` | 176   | Tutorial / beginner guide quests |
| `15` | 173   | The Magnus / endgame zone quests |
| `18` | 13    | Olvia Academy family reward quests |

Categories are inferred from English title strings; exact game-engine semantics are not confirmed.

---

### Length-Prefixed UTF-16 Field

| Offset  | Type         | Field | Notes                                      |
| ------- | ------------ | ----- | ------------------------------------------ |
| `+0x00` | u32          | len   | Number of UTF-16 code units, not byte size |
| `+0x04` | u32          | zero  | Observed `0`                               |
| `+0x08` | utf16le[len] | text  | No trailing NUL included in `len`          |

---

## Observed Records

| File Offset  | Raw `+0x00` ID | Condition                                                       | Action                                                               | Objective KR                                                    | Icon                               |
| ------------ | -------- | --------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------- |
| `0x00000004` | `125285` | `checkFieldType(hadumField);getLevel()>59;clearquest(2080,10);` | `killMonsterGroup(189,1);`                                           | `<악몽의 그림자> 기가고드 처치하기;`                            | `Icon/Quest/Hadum08.dds`           |
| `0x000005F8` | `65536`  | `getLevel()>0;`                                                 | `gatheritem(16004,0,1);`                                             | `응축된 마력의 블랙스톤 제작하기;`                              | `Icon/Quest/GrowthPass_GUV_07.dds` |
| `0x00000936` | `115546` | `getLevel()>30;<or>clearquest(654,4);`                          | `killmonster(20007,10); killmonster(20009,6); killmonster(24001,2);` | `임프 병사 처치하기;임프 요술사 처치하기;임프 방어탑 파괴하기;` | `Icon/Quest/Imp.dds`               |

---

## Localization

Quest title/text strings appear in LOC `str_type=18`. This type uses
`str_id1=quest_chain_id`, `str_id2=quest_id`, and `str_id4` for text role/order.
The DBSS packed ID appears to store `(quest_id << 16) | quest_chain_id`.
Exact `str_id4` role semantics are still provisional.

Example matches from `languagedata_en.loc`:

| Chain ID | Quest ID | LOC Type | id4 | Example English Text |
| -------: | -------: | -------- | --: | -------------------- |
| `41067`  | `1`      | `18`     | `0` | `[Godr-Ayed and Blackstar] PEN (V) Earthshaking Blackstar Shield` |
| `41067`  | `1`      | `18`     | `2` | `Merindora` |
| `41067`  | `1`      | `18`     | `3` | `Hand over Scorching Sun Crystal to Merindora;...` |
| `3500`   | `310`    | `18`     | `0` | `[Alchemy] A Small Favor` |
| `3500`   | `311`    | `18`     | `0` | `[Alchemy] A Kid's Wisdom` |

Quest IDs can collide with other LOC domains. For example, `65536` also matches
item LOC `str_type=0`. Previous research also matched `str_type=39`, but that
type appears to be voice/dialogue text and can produce misleading preview
titles/objectives.

---

## Suggested UI Layout

| Column       | Type | Notes                                                       |
| ------------ | ---- | ----------------------------------------------------------- |
| Display ID   | num  | Prefer `canonical_link.canonical_quest_id`; fallback to packed ID from `+0x00` |
| Chain ID     | num  | `packed_quest_id & 0xFFFF`; LOC type 18 `str_id1`           |
| Quest ID     | num  | `packed_quest_id >> 16`; LOC type 18 `str_id2`              |
| Title / Name | text | LOC type 18 `str_id4=0` when available                      |
| Condition    | text | `condition_script`                                          |
| Action       | text | `action_script`                                             |
| Objective    | text | Prefer LOC type 18 objective text; fall back to inline Korean objective text |
| Icon         | text | `icon_path`; render thumbnail when DDS preview is available |

---

## Notes

- `quest.dbss` is much larger than existing documented DBSS samples: observed decompressed size is `36,525,439` bytes.
- Parsed preview is implemented as a lazy handler because the table has nearly twenty thousand variable-length records.
- The preview derives row coverage from quest icon paths. It decodes rows whose script layout can be identified and shows icon-only rows for still-unknown layouts.
- `allquestlist.bss` has the same entry count (`19,599`) and uses the same packed ID split. The current parser extracts `16,977` non-zero canonical display IDs from `quest.dbss`; `16,976` of those exist in `allquestlist.bss`.
- English columns use loaded LOC type `18` rows keyed by `(quest_chain_id, quest_id)`; exact title/objective row semantics remain provisional.
- Some decoded rows have no direct LOC type 18 title. In those cases the scripts may still reference localized display quests through `clearquest(chain,id)`.
- `(file_size - 4) / count` is not integral, confirming variable-length records.
- Two record variants exist: **step records** (`packed_id_a == packed_id_b`, small internal step IDs) and **canonical records** (`packed_id_a ≠ packed_id_b`, where `packed_id_b` is often the display ID matching `allquestlist.bss` and LOC type 18).
- The most reliable display key found so far is the `canonical_link` sub-record. Parsers should use it when present, then fall back to the record-start packed ID.
- No `questoffset.dbss` was found. `guildquestoffset.dbss` and `journalquestoffset.dbss` exist for related formats, but not for the main quest table. See [journalquest_dbss.md](journalquest_dbss.md) for the documented journal quest format.
- Scripts use readable expression syntax such as `getLevel()>30`, `<or>`, `clearquest(group,id)`, `killmonster(id,count)`, `gatheritem(item_id,?,count)`, and `meet(npc_id,count)`.
- Raw objective text is Korean. English display strings appear to live in LOC type 18, keyed by `id1=quest_chain_id`, `id2=quest_id`; exact `id4` role mapping is not fully decoded.

---

## Open Questions

### Record Boundary Algorithm

Record starts can be detected heuristically from repeated `quest_id` pairs and
the first length-prefixed UTF-16 field, but this only covers some rows. Some
quests use compound IDs such as `3500/310`, and later records do not always
repeat a single packed ID. Need a deterministic parser for all `19,599`
records and the missing `118` rows that do not currently expose a matched icon
path.

### Unknown Payload

The data after `objective_text_kr` contains many numeric fields, PAColor-tagged rich text, and possibly reward/condition/config arrays. Field boundaries and meanings are not yet confirmed.

### Icon Field Prefix

Icon paths are ASCII NUL-terminated and appear near record tails, often preceded by a small length-like value, but exact field encoding is not confirmed.

### LOC Row Semantics

`quest_chain_id` + `quest_id` resolve to multiple LOC type 18 rows with
different `id4` values. Current observed pattern: `id4=0` title, `id4=1`
summary/description, `id4=2` NPC/speaker, `id4=3` objective. Need confirm
remaining roles. LOC type 39 still has many quest-adjacent strings, but is not
reliable as the main quest title/objective source.

### `questgroup.dbss` Coverage

`questgroup.dbss` confirms one relationship to this file: each child link is a `(group_id, quest_no)` pair whose raw 4 bytes equal a `quest.dbss` `quest_id`. It does not explain the remaining variable-length payload fields in `quest.dbss`.

### `allquestlist.bss` Coverage

`allquestlist.bss` confirms the canonical display quest ID scheme and record-count scale. Current `quest.dbss` parsing extracts `16,977` non-zero `canonical_link` IDs, and `16,976` of them exist in `allquestlist.bss`. This confirms `allquestlist.bss` is the canonical display quest ID list; remaining work is explaining the `2,622` allquestlist IDs not reached by the current icon-window parser.

### Canonical Link `link_type` Semantics

Values `0..15` and `18` have been sampled and mapped to apparent quest categories (see the Observed `link_type` values table in the Canonical Link Sub-record section). The mapping is inferred from English title strings, not confirmed engine source. Some categories are ambiguous (e.g., types 1 vs 11 both appear on story quests; types 2 vs 3 partially overlap on repeatables). Exact game-engine semantics for each value remain unconfirmed.

### Payload Sub-records Beyond `0x003BAE30`

The canonical link sub-record (`0x003BAE30`) is the only confirmed structure in `unknown_payload`. The payload likely contains additional structured sub-records encoding rewards, reputation gains, XP values, item drops, or other quest config data. Whether these are worth decoding — and what marker bytes or length prefixes identify them — is not yet investigated.
