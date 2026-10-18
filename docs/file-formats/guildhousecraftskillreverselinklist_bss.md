# `guildhousecraftskillreverselinklist.bss` Format

## Purpose

The reverse of [`guildhousecraftskill.dbss`](guildhousecraftskill_dbss.md):
for each guild skill a guild house use grants, the house uses that grant it
and the skill slot it sits in there. Skill `65058` Local Economy
Revitalization lists the five specialty packing workshops `1605` to `1609`,
every other skill one house use. The plain PABR file holds the skills, then
an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                      | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | ----------------------------------------- | ----- | ----------------- | --------- |
| 1      | 1784 and later | 3474    | `guildhousecraftskillreverselinklist.bss` | 668   | 48 Link, 44 Skill | 8         |

| Layout | File                                      | Known          | Unknown    |
| ------ | ----------------------------------------- | -------------- | ---------- |
| 1      | `guildhousecraftskillreverselinklist.bss` | 668 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Skill name (type `10`, `str_id1` = `skill_no`) and house use name (type `16`, `str_id1` = `receipe_key`) |

The handler links each skill number to its first `skill.dbss` row and each
`receipe_key` to its `guildhousecraftskill.dbss` row. It loads neither file.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                         |
| ------------------- | ------------ | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32          | count              | Number of skills                              |
| `+0x08`             | Skill[count] | skills             | Variable-size entries, back to back; see Skill |
| `skills+0x00`       | String Table | string_table       | See String Table                              |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the skills end |
| `string_table+0x04` | u32          | zero               | Always `0`                                    |

The string table has the shape `exploration.bss`, `npcsimply.bss` and
[`itemequipgroup.bss`](itemequipgroup_bss.md) use
(`_common/pabr_strings.py`). Walking `count` skills ends exactly at
`string_table_start`.

### Skill (variable: 6 bytes + links)

| Offset  | Type             | Field      | Notes                                                        |
| ------- | ---------------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u16              | skill_no   | `skill.dbss` skill number; unique                            |
| `+0x02` | u32              | link_count | Number of links; at least `1` on clients 1784 and 3474       |
| `+0x06` | Link[link_count] | links      | The `guildhousecraftskill.dbss` rows that list this skill; see Link |

The skill entries have no padding: `link_count` sits at `+0x02` and the
links at `+0x06`.

### Link (8 bytes)

| Offset  | Type | Field       | Notes                                                                  |
| ------- | ---- | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | i32  | receipe_key | House use, the `receipe_key` of a `guildhousecraftskill.dbss` row       |
| `+0x04` | u32  | slot        | Where the skill sits in that row: `1` for `skill_nos[0]` up to `5` for `skill_nos[4]` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No skill reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 and no
string in its server dump names this file or holds `ReverseLink`.
`skill_no` and `receipe_key` take their names from
[`guildhousecraftskill.dbss`](guildhousecraftskill_dbss.md), whose key
type `gc::KeyType<int,-1>` makes `receipe_key` an i32 here too.

`slot` is named by value. Inverting `guildhousecraftskill.dbss` (every
filled `skill_nos[i]` gives skill, `receipe_key`, `i + 1`) gives exactly the
links of this file, with no link missing or extra:

| Client | Skills | Links | Matching links |
| ------ | ------ | ----- | -------------- |
| 1784   | 31     | 35    | 35 of 35       |
| 3474   | 44     | 48    | 48 of 48       |

## Notes

- A skill that several rows list keeps those rows in
  `guildhousecraftskill.dbss` file order: skill `65058` lists `1609`,
  `1608`, `1607`, `1606`, `1605`, each at slot `1`, on clients 1784 and
  3474.
- On client 1784 the skills follow the order in which they first appear
  walking `guildhousecraftskill.dbss` row by row and slot by slot. On client
  3474 they do not (the file starts with `65104`, `65232`, `65240`, `65236`),
  and the order follows neither the skill numbers nor the forward rows.
- No client 3474 Lua file (`luacscript/`) names the file or a reverse link
  function; the guild house Lua reads the house uses through
  `getGuildHouseCraftInfoManager()` only.
