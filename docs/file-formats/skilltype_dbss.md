# `skilltype.dbss` Format

## Purpose

The presentation record of every skill: the Korean skill name, its family
name, whether it is active or passive, the skill icon, and a long action
configuration (animation, targeting and combat behaviour) that is not decoded.
This is where a skill's icon comes from.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                             |
| ---------------------- | -------- | ---------------------------------------------------------------- |
| `skilltypeoffset.dbss` | Required | `skill_key → (offset, size)` index into this file                |
| `languagedata_en.loc`  | Optional | English names, LOC type `10`, `str_id1 = skill_no`               |

The skill key is the one shared by the whole skill cluster; see
[`skill.dbss` Skill Keys](skill_dbss.md#skill-keys). All multi-byte values are
little-endian.

## Layout 1

### File Layout

The records tile the file like `skill.dbss`: each starts 4 bytes after the
previous one ends, the first at `8`, and the last ends at end of file. Strings
are a `u64` count followed by UTF-16LE units (text) or ASCII bytes (paths).

Every key is level `1`. 30,342 of the 30,352 keys are also in `skill.dbss`;
the 82 `skill.dbss` keys above level 1 have no record here.

| Offset  | Type          | Field   | Notes                                      |
| ------- | ------------- | ------- | ------------------------------------------ |
| `+0x00` | u32           | count   | Number of records; matches the offset file |
| `+0x04` | Record[count] | records | See Record                                 |

### Record (variable: 4 bytes + payload)

| Offset  | Type    | Field      | Notes                                                       |
| ------- | ------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32     | key_prefix | Each record is preceded by a repeated copy of its key       |
| `+0x04` | Payload | payload    | `size` bytes; the index row's `offset` points at this field |

### Payload (variable: 24 bytes + names and config, size from `skilltypeoffset.dbss`)

| Offset            | Type        | Field      | Notes                                                    |
| ----------------- | ----------- | ---------- | -------------------------------------------------------- |
| `+0x00`           | u32         | skill_key  | Equals the index key                                     |
| `+0x04`           | str16       | name       | Korean skill name, e.g. `거대한 진노 III`                 |
| `name+0x00`       | str16       | group_name | Korean family name, see [`group_name`](#group_name)      |
| `group_name+0x00` | u32         | kind       | `0` other, `1` active, `2` passive; see [`kind`](#kind)  |
| `group_name+0x04` | bytes[rest] | config     | Action configuration, not decoded; holds `icon_path`, see [`icon_path`](#icon_path) |

### `skilltypeoffset.dbss`

The layout of [`skilloffset.dbss`](skill_dbss.md#skilloffsetdbss). Read it with
`parse_pabr_u32_offset_rows()`.

| Offset              | Type             | Field        | Notes                                    |
| ------------------- | ---------------- | ------------ | ---------------------------------------- |
| `+0x00`             | char[4]          | magic        | ASCII `PABR`                             |
| `+0x04`             | u32              | count        | Number of index rows; `30352` on client 3458 |
| `+0x08`             | Index Row[count] | rows         | See Index Row                            |
| `rows+0x00`         | String Table     | string_table | Empty: `string_count` is `0`             |
| `string_table+0x00` | u32              | table_start  | End of the rows, `8 + 12 * count`        |
| `string_table+0x04` | u32              | zero         | Always 0                                 |

### Index Row (12 bytes)

| Offset  | Type | Field     | Notes                                                  |
| ------- | ---- | --------- | ------------------------------------------------------ |
| `+0x00` | u32  | skill_key | `skill_no << 16 \| level`                              |
| `+0x04` | u32  | offset    | Byte offset of the record's `payload` in `skilltype.dbss` |
| `+0x08` | u32  | size      | Payload size in bytes                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes            |
| ------- | ------------------ | ------------ | ---------------- |
| `+0x00` | u32                | string_count | `0`              |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none here |

## `group_name`

Equal to `name` on 16,847 records. On the other 13,505 it is the name without
the rank or a qualifier: `거대한 진노 III` -> `거대한 진노`, `탈것 속도 증가 1.0%`
-> `속도 +1.0%`. Some are cut mid-phrase (`극 : 매화의 정신` -> `극 : 매화의`), so it
reads like a short label rather than a clean family name.

## `kind`

| Value | Meaning | Records | Example                                  |
| ----- | ------- | ------- | ---------------------------------------- |
| 0     | Other   | 14,382  | Item and event skills, "[Event] Energy of Happiness" (57005) |
| 1     | Active  | 10,219  | "Seismic Strike", "Fist Fury I"          |
| 2     | Passive | 5,751   | "Mountain Aura IX" to "XVI"              |

## `icon_path`

The skill icon is the first length-prefixed ASCII string in `config`, a `.dds`
path relative to `ui_texture/icon/`. `find_prefixed_ascii()` finds it, as for
`itemenchant.dbss`. Its position is not fixed: it follows a variable part of
the configuration, 49 to 69 bytes after `kind`.

| Kind    | With icon | Without |
| ------- | --------- | ------- |
| Other   | 186       | 14,196  |
| Active  | 7,654     | 2,565   |
| Passive | 1,562     | 4,189   |

9,402 records have an icon, never more than one, over 3,530 distinct paths.
Lower-cased under `ui_texture/icon/`, 3,452 of those paths exist in the
client's PAZ files on client 3458; the other 78 point at missing files
(for example `new_icon/04_pc_skill/01_pc_skill/31_prsa_skill/prsa_skill_8827.dds`).

`config` also holds 7,355 `.png` paths such as
`Real_ETC/Scroll/Icon_ETC_Scroll_00000000.png`; what they are for is not
known.

## Notes

- The first keys (`0xDEAD0001`, `0xDEAC0001`) look like sentinels but are
  real skills; see [`skill.dbss` Skill Keys](skill_dbss.md#skill-keys).
- The record layout of the first four fields and the `kind` meaning come from
  bdo-data-extractor; the counts, the icon rule and the `group_name` reading
  were checked against client 3458.
- LOC type `10` covers 28,343 of its 29,398 IDs with a skill number from this
  table or `skill.dbss`; 2,009 skill numbers have no type `10` row and 1,055
  type `10` IDs have no skill.

## Open Questions

### How is `config` laid out?

The configuration opens with small counts and lists (a run of `ff ff ff ff ff
7f`, the skill key again, and skill numbers and keys on class skills) before
the icon, which is why the icon moves between 49 and 69 bytes after `kind`.
Decoding it would give the icon a fixed place and expose the animation and
targeting fields, but nothing that is needed so far depends on it.
