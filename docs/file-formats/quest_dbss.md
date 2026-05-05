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

- [languagedata_en.loc](languagedata_loc.md) — English quest dialogue/objective strings, observed as LOC `str_type=39` keyed by `quest_id`
- `questgroup.dbss` — likely groups/categories quests; extraction failed in the current sample, so relationship is not yet confirmed

---

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | English quest strings; raw `quest.dbss` stores Korean objective text |
| `questgroup.dbss`     | Optional | Likely quest grouping metadata; not decoded yet                      |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                      |
| ------- | ---- | ----- | ------------------------------------------ |
| `+0x00` | u32  | count | Number of quest records; observed: `19599` |

### Record Stream

Records start immediately after the header at `+0x04`. Records are variable length and are not preceded by an offset table in the observed archive. Record starts can be identified by a repeated `quest_id` pair followed by a length-prefixed UTF-16-LE script field.

The first observed record starts at file offset `0x00000004`; the next confirmed record starts at `0x000005F8`.

---

## Record Structure

### Quest Record (variable length)

| Offset   | Type              | Field               | Notes                                                                                   |
| -------- | ----------------- | ------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`  | u32               | quest_id_a          | Quest identifier                                                                         |
| `+0x04`  | u32               | quest_id_b          | Duplicate of `quest_id_a` in observed records                                           |
| `+0x08`  | u32               | unknown_08          | Observed `0` in sampled records                                                         |
| `+0x0C`  | u32               | condition_len       | UTF-16 code unit count for `condition_script`                                           |
| `+0x10`  | u32               | condition_zero      | Observed `0`                                                                            |
| `+0x14`  | utf16le[len]      | condition_script    | Quest availability / prerequisite expression                                            |
| varies   | u32               | action_len          | UTF-16 code unit count for `action_script`                                              |
| varies   | u32               | action_zero         | Observed `0`                                                                            |
| varies   | utf16le[len]      | action_script       | Completion target/action expression                                                     |
| varies   | u8[]              | zero_padding_a      | Zero padding before objective text length; length varies                                |
| varies   | u32               | objective_len       | UTF-16 code unit count for `objective_text_kr`                                          |
| varies   | u32               | objective_zero      | Observed `0`                                                                            |
| varies   | utf16le[len]      | objective_text_kr   | Korean objective text shown in quest UI                                                 |
| varies   | u8[]              | unknown_payload     | Mixed numeric fields and text/rich-text payloads; includes PAColor markup in some rows  |
| varies   | ascii nul-terminated | icon_path        | Quest icon path such as `Icon/Quest/Hadum08.dds`; appears near the tail of each record  |
| varies   | u8[]              | unknown_tail        | Numeric flags/config values after icon path                                             |

### Length-Prefixed UTF-16 Field

| Offset  | Type         | Field | Notes                                      |
| ------- | ------------ | ----- | ------------------------------------------ |
| `+0x00` | u32          | len   | Number of UTF-16 code units, not byte size |
| `+0x04` | u32          | zero  | Observed `0`                               |
| `+0x08` | utf16le[len] | text  | No trailing NUL included in `len`          |

---

## Observed Records

| File Offset | Quest ID | Condition | Action | Objective KR | Icon |
| ----------- | -------- | --------- | ------ | ------------ | ---- |
| `0x00000004` | `125285` | `checkFieldType(hadumField);getLevel()>59;clearquest(2080,10);` | `killMonsterGroup(189,1);` | `<악몽의 그림자> 기가고드 처치하기;` | `Icon/Quest/Hadum08.dds` |
| `0x000005F8` | `65536` | `getLevel()>0;` | `gatheritem(16004,0,1);` | `응축된 마력의 블랙스톤 제작하기;` | `Icon/Quest/GrowthPass_GUV_07.dds` |
| `0x00000936` | `115546` | `getLevel()>30;<or>clearquest(654,4);` | `killmonster(20007,10); killmonster(20009,6); killmonster(24001,2);` | `임프 병사 처치하기;임프 요술사 처치하기;임프 방어탑 파괴하기;` | `Icon/Quest/Imp.dds` |

---

## Localization

`quest_id` matches LOC `str_type=39` entries for quest dialogue/objective text. Example matches from `languagedata_en.loc`:

| Quest ID | LOC Type | Example English Text |
| -------- | -------- | -------------------- |
| `125285` | `39` | `Hand over Mark of Hadum.` |
| `125285` | `39` | `A greater darkness is approaching.` |
| `115546` | `39` | `Discover Western Gateway` |

Quest IDs can collide with other LOC domains. For example, `65536` also matches item LOC `str_type=0`, so UI code should prefer quest LOC type `39` when resolving quest display strings.

---

## Suggested UI Layout

| Column        | Type | Notes                                                        |
| ------------- | ---- | ------------------------------------------------------------ |
| Quest ID      | num  | `quest_id_a`; right-aligned                                  |
| Title / Name  | text | Prefer LOC type 39 when a suitable title/name row is known   |
| Condition     | text | `condition_script`                                           |
| Action        | text | `action_script`                                              |
| Objective KR  | text | Inline Korean objective text                                 |
| Objective EN  | text | LOC type 39 fallback when matching row semantics are known   |
| Icon          | text | `icon_path`; render thumbnail when DDS preview is available  |

---

## Notes

- `quest.dbss` is much larger than existing documented DBSS samples: observed decompressed size is `36,525,439` bytes.
- `(file_size - 4) / count` is not integral, confirming variable-length records.
- No `questoffset.dbss` was found. `guildquestoffset.dbss` and `journalquestoffset.dbss` exist for related formats, but not for the main quest table.
- Scripts use readable expression syntax such as `getLevel()>30`, `<or>`, `clearquest(group,id)`, `killmonster(id,count)`, `gatheritem(item_id,?,count)`, and `meet(npc_id,count)`.
- Raw objective text is Korean. English display strings appear to live in LOC type 39, but exact mapping from each inline objective to LOC row IDs (`id2`, `id3`, `id4`) is not fully decoded.

---

## Open Questions

### Record Boundary Algorithm

Record starts can be detected heuristically from repeated `quest_id` pairs and the first length-prefixed UTF-16 field, but the file has no confirmed offset table. Need a deterministic parser for all `19599` records.

### Unknown Payload

The data after `objective_text_kr` contains many numeric fields, PAColor-tagged rich text, and possibly reward/condition/config arrays. Field boundaries and meanings are not yet confirmed.

### Icon Field Prefix

Icon paths are ASCII NUL-terminated and appear near record tails, often preceded by a small length-like value, but exact field encoding is not confirmed.

### LOC Row Semantics

`quest_id` resolves to multiple LOC type 39 rows with different `id2`/`id4` values. Need map for title, summary, objective, start dialogue, and completion dialogue.

### `questgroup.dbss`

`questgroup.dbss` appears related by name, but extraction failed with a size mismatch in the current archive sample. Need a valid extraction before documenting companion semantics.
