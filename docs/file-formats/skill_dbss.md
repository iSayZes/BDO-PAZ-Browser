# `skill.dbss` Format

## Purpose

The rule record of every skill rank: class skills, passives, item and event
skills, mount and guild skills. Each record carries the rank's cooldown, the
buffs it applies, an effect script, and the skills it leads to. This is the
middle link of the item effect chain: a consumable names a skill key, and
the skill names its buffs.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes     | Records                            | Row bytes                    |
| ------ | -------------- | ------- | ------------------ | --------- | ---------------------------------- | ---------------------------- |
| 2      | 3473 and later | 3473    | `skill.dbss`       | 9,767,040 | 30,487 Skill Record, 30,487 Record | 210 to 1,540, 316 on average |
| 2      | 3473 and later | 3473    | `skilloffset.dbss` | 365,864   | 30,487 Index Row                   | 12                           |

| Layout | File               | Known               | Unknown             |
| ------ | ------------------ | ------------------- | ------------------- |
| 2      | `skill.dbss`       | 6,169,574 B (63.2%) | 3,597,466 B (36.8%) |
| 2      | `skilloffset.dbss` | 365,864 B (100.0%)  | 0 B (0.0%)          |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                            |
| --------------------- | -------- | --------------------------------------------------------------- |
| `skilloffset.dbss`    | Required | `skill_key → (offset, size)` index into this file               |
| `buff.dbss`           | Optional | The buffs named by `buff_ids`                                   |
| `skilltype.dbss`      | Optional | Korean name, kind and icon of the same skill, see [`skilltype.dbss`](skilltype_dbss.md); the app reads name and icon through the `SKILL_NAME_KR` and `SKILL_ICON` lookup indexes |
| `languagedata_en.loc` | Optional | Skill names and descriptions, LOC type `10`, `str_id1 = skill_no`; each rank's own text, LOC type `13`, `str_id1 = skill_no`, `str_id2 = level` |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                                    |
| ------- | ------------- | ------- | -------------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; matches the offset file               |
| `+0x04` | Record[count] | records | Each record is preceded by a repeated copy of its key   |

The records tile the file: each starts 4 bytes after the previous one ends
(the repeated key), the first at `8`, and the last ends at end of file.

Strings are a `u64` count followed by that many units: UTF-16LE for text and
scripts, single-byte ASCII for `name`. There is no terminator.

### Record (variable: 4 bytes + record)

| Offset  | Type         | Field      | Notes                                                       |
| ------- | ------------ | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32          | key_prefix | Repeated copy of the record's `skill_key`                   |
| `+0x04` | Skill Record | record     | `size` bytes; the index row's `offset` points at this field |

### Skill Record (variable: 210 bytes + text and key lists)

Offsets `name+0xNN` count from the end of `name`, called `N` in the notes
below; with an empty name `N` is `17`.

| Offset                 | Type                   | Field               | Notes                                                           |
| ---------------------- | ---------------------- | ------------------- | --------------------------------------------------------------- |
| `+0x00`                | u32                    | skill_key           | Equals the index key                                            |
| `+0x04`                | u32                    | level_1_key         | `skill_no << 16 \| 1`; equals `skill_key` except on the 82 keys above level 1 |
| `+0x08`                | u8                     | unknown_08          | Non-zero on 8,842 records; equals `skillsimply.dbss` `unknown_e08`, which follows damage tooltips on Wizard |
| `+0x09`                | str8                   | name                | ASCII internal name such as `SUMMON_BOSS`, `SETUP_QUESTITEM`; empty on 24,794 records |
| `name+0x00`            | u32                    | name_hash           | `0` when `name` is empty; one value per name (4,461 names)      |
| `name+0x04`            | bytes[40]              | unknown_n04         | Not decoded                                                     |
| `name+0x2C`            | u16                    | resource_cost       | MP or WP the skill costs, by class; `0` on 26,837 records, up to `660`; see below |
| `name+0x2E`            | bytes[7]               | unknown_n46         | Not decoded                                                     |
| `name+0x35`            | u16                    | stamina_cost        | Stamina the skill costs; `0` on 26,635 records, `1` on 2,825, up to `600`; see below |
| `name+0x37`            | bytes[23]              | unknown_n55         | Not decoded                                                     |
| `name+0x4E`            | u32                    | cooldown_ms         | Cooldown in milliseconds; `0` on 22,798 records, see Notes      |
| `name+0x52`            | u32[10]                | buff_ids            | `buff.dbss` IDs, zero-padded; see below                          |
| `name+0x7A`            | str16                  | description         | Korean description, UTF-16; empty on 21,114 records, `UNKNOWN` on 1,284, `<null>` on 43. The Korean source of LOC type `13` for the same `(skill_no, level)`, and often the same text as LOC type `10` `str_id4 = 1`, see Notes. Line breaks are stored as the two characters `\n` (873 on client 3458) and decoded by the parser |
| `description+0x00`     | str16                  | script              | UTF-16 effect script such as `DAM_ATT_2(...)`, `AWAKEN();`, `BATH();`; empty on 21,594 records |
| `script+0x00`          | bytes[36]              | unknown_tail        | Not decoded                                                     |
| `script+0x24`          | u32                    | next_skill_count    | `0` on 25,209 records, `1` on 4,560; up to `75`, see below       |
| `script+0x28`          | u32[next_skill_count]  | next_skill_keys     | Skill keys this rank leads to, see below                        |
| `next_skill_keys+0x00` | u32                    | unknown_after_next_skill_keys | Always `0`                                            |
| `next_skill_keys+0x04` | u32                    | base_skill_count    | `1` on 155 records, else `0`                                    |
| `next_skill_keys+0x08` | u32[base_skill_count]  | base_skill_keys     | The skill a Core skill enhances, see below                      |
| `base_skill_keys+0x00` | f32                    | unknown_f32         | `-1.0` on 29,722 records, else `0.0`                            |
| `base_skill_keys+0x04` | bytes[3]               | unknown_end         | Usually zero                                                    |

Every one of the 30,481 records on client 3464 walks to exactly its `size`
with this layout.

### `skilloffset.dbss`

| Offset              | Type             | Field        | Notes                                                 |
| ------------------- | ---------------- | ------------ | ----------------------------------------------------- |
| `+0x00`             | char[4]          | magic        | `PABR`                                                |
| `+0x04`             | u32              | count        | Number of index rows; `30424` on client 3458          |
| `+0x08`             | Index Row[count] | rows         | See Index Row                                         |
| `rows+0x00`         | String Table     | string_table | An empty PABR string table                            |
| `string_table+0x00` | u32              | rows_end     | End of the rows (`8 + 12 * count`)                    |
| `string_table+0x04` | u32              | zero         | Always `0`                                            |

Read it with `parse_pabr_u32_offset_rows()`.

### Index Row (12 bytes)

| Offset  | Type | Field     | Notes                                        |
| ------- | ---- | --------- | -------------------------------------------- |
| `+0x00` | u32  | skill_key | `skill_no << 16 \| level`                    |
| `+0x04` | u32  | offset    | Byte offset of the record in `skill.dbss`     |
| `+0x08` | u32  | size      | Record size in bytes                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

Before client 3464 the `buff_ids` slots were u16, so the Skill Record was 20
bytes shorter and `description` started at `N+102`; see `buff_ids`. Only the
Skill Record differs from Layout 2. The parser reads only Layout 2.

### Skill Record (variable: 190 bytes + text and key lists)

| Offset                 | Type                   | Field               | Notes |
| ---------------------- | ---------------------- | ------------------- | ----- |
| `+0x00`                | u32                    | skill_key           |       |
| `+0x04`                | u32                    | level_1_key         |       |
| `+0x08`                | u8                     | unknown_08          |       |
| `+0x09`                | str8                   | name                |       |
| `name+0x00`            | u32                    | name_hash           |       |
| `name+0x04`            | bytes[40]              | unknown_n04         |       |
| `name+0x2C`            | u16                    | resource_cost       |       |
| `name+0x2E`            | bytes[7]               | unknown_n46         |       |
| `name+0x35`            | u16                    | stamina_cost        |       |
| `name+0x37`            | bytes[23]              | unknown_n55         |       |
| `name+0x4E`            | u32                    | cooldown_ms         |       |
| `name+0x52`            | u16[10]                | buff_ids            |       |
| `name+0x66`            | str16                  | description         |       |
| `description+0x00`     | str16                  | script              |       |
| `script+0x00`          | bytes[36]              | unknown_tail        |       |
| `script+0x24`          | u32                    | next_skill_count    |       |
| `script+0x28`          | u32[next_skill_count]  | next_skill_keys     |       |
| `next_skill_keys+0x00` | u32                    | unknown_after_next_skill_keys |  |
| `next_skill_keys+0x04` | u32                    | base_skill_count    |       |
| `next_skill_keys+0x08` | u32[base_skill_count]  | base_skill_keys     |       |
| `base_skill_keys+0x00` | f32                    | unknown_f32         |       |
| `base_skill_keys+0x04` | bytes[3]               | unknown_end         |       |

## Skill Keys

Every table in the skill cluster keys a skill rank by a u32:

```text
skill_key = skill_no << 16 | level
```

30,424 keys on client 3458, over 30,342 skill numbers. Almost every key is
level `1` (30,342); 54 are level `2`, 18 level `3`, and a handful go up to
`13`. Rank chains such as "Grave Digging I" to "IV" use separate skill numbers,
not levels, and [`skillgroup.bss`](skillgroup_bss.md) lists them.

The first key in the index, `0xDEAD0001`, is skill `57005` level 1,
"[Event] Energy of Happiness". It looks like a sentinel but is an ordinary
skill; `0xDEAC0001` next to it is skill `57004`, "Grim Reaper's Fury".

## `buff_ids`

Ten u32 slots. The IDs fill the front and the rest are `0`; no record has a
non-zero ID after a zero. On client 3464, 20,418 records name one buff, 507
fill all ten, and 96 name none. Every ID is a `buff.dbss` key.

Before client 3464 the slots were u16, so the block was 20 bytes shorter and
`description` started at `N+102`. The widening came with the first buff IDs
above 65,535 (see the `buff.dbss` Notes); skills 44974 to 44978 (level 1)
apply those five buffs. The parser reads only the u32 layout.

This is the item to buff link: `itemenchant.dbss` `skill_key_1` and
`skill_key_2` are keys of this table, and the buffs of both skills are the
item's effects. Item 761880 casts skill 47683, which applies the six buffs
48723 to 48728. The browser builds the `SKILL_BUFFS` and `BUFF_ITEMS` lookup
indexes from it (see "Lookup Indexes" in docs/handler.md): the
`itemenchant.dbss` Buffs column and the `buff.dbss` Applied By column read
them.

## `resource_cost` and `stamina_cost`

`resource_cost` is the class's own resource, so the tooltip names it by
class: MP on Wizard, WP on Mystic. Checked in game (2026-10-01): "Fireball IV"
shows "Required MP : 30" and "Lightning V" 60, the Mystic's "Thunder Pound
IV" costs 50 WP, and "Teleport III" shows "Required Stamina : 200", each as
stored. bdocodex lists 100 MP for "Grave Digging III" (stored `100`) and no
cost for "Imminent Doom" (`0`). The skill tooltip Lua reads them as
`_requireMp` and `_requireSp`. 18 records set both.

2,825 records store a stamina cost of `1`, mostly basic attacks and weapon
training ranks ("Staff Attack I" to "X", "Magic Arrow I" to "V"); whether the
tooltip shows that is not checked.

## `next_skill_keys` and `base_skill_keys`

Every key in both lists is a `skill.dbss` key (7,877 and 155 entries).

`next_skill_keys` points forward along a skill line: "Ample Storage Lv. 26"
lists Lv. 27, "Soul Shower III" lists its next rank and "Core: Soul Shower".
Awakening, Succession and a few other hub skills list every skill they
unlock: most "Succession:" skills list 34 Prime skills, and "Succession:
Elemental Revelation" (4933) lists 75.
Of the 3,858 consecutive rank pairs in `skillgroup.bss`, 3,422 appear here as
rank `i` listing rank `i + 1`.

`base_skill_keys` is set only on the 155 "Core:" skills and names the skill
the Core enhances ("Core: Soul Shower" -> "Soul Shower III"). In 154 of the
155 cases that base skill lists the Core in its `next_skill_keys`.

## Notes

- `cooldown_ms` is checked on the wiki (2026-09-28) on three skill lines:
  Warrior's Grave Digging I to IV show 8 s (8,000 stored), Imminent Doom (1209)
  18 s (18,000) and Succession: Imminent Doom (4859) 14 s (14,000), and in
  game (2026-10-01) on Wizard: Fireball IV 3 s, Lightning V 5 s and Teleport
  III 7 s. 7,547 of the 7,626 non-zero values are whole
  seconds; the other 79 are mostly Black Spirit variants at 90% of a round
  value (13,500, 8,100). The field name and its position `@95` come from
  bdo-data-extractor, which reads it at a fixed offset. That only holds when
  `name` is empty: skill 17569 has the 22-character name
  `SHADOW_SKILL_SLOT4_2LV`, and its cooldown (9,000) sits 22 bytes later.
- `description` holds real text on 7,983 records (client 3458); 43 more
  store the literal `<null>`. Class skills leave it empty, so their LOC
  type `10` `str_id4 = 1` text has no Korean copy here.
- It is the Korean source of LOC type `13`, keyed `str_id1 = skill_no`,
  `str_id2 = level`: 28,537 of the 28,869 type 13 keys are `skill.dbss`
  ranks, and the numbers in the two texts agree on 7,955 of 7,959 pairs.
  Type 13 stores `0` where `description` is `UNKNOWN` (set effect skills).
- On 7,324 records it is also the source of LOC type `10` `str_id4 = 1`,
  the same text: utility skills whose buffs have no description, such as
  knowledge entries ("Adds acquired knowledge to the book.", 5,651),
  exploration nodes (1,028), workers (540), trade stock refreshes (66) and
  contribution points (39).
- 657 are guild skills (skill numbers 62000 to 65999). Their type 10
  `str_id4 = 1` is missing (614) or a usage hint such as
  `{TextBind:CASTING_CLICK_RMB} after learning the skill` (Healing Touch,
  65209; the browser fills it as `Cast with [Attack2] after learning the
  skill`), while type 13 holds the effect (`- Effect: Recover 200 HP every
  3 sec (only during Node/Conquest War)`). The Description column shows
  both, the hint first; which order the game tooltip uses is not checked.
  The effect text is close to the Korean `buff.dbss` description of the
  skill's buffs but never equal to it: 375 contain every buff text and add
  a line ("does not stack with the previous rank"), the rest add the
  war-only condition, the duration and the caster, or reword it. So the
  buff text cannot stand in for it; the Buffs column shows the buffs.
- Five guild skill ranks (Monster Extra AP, 65077 to 65081) have Korean
  text only, so their Description stays Korean.
- The skill tooltip Lua (`panel_tooltip_skill.luac`) calls `getDescription`
  on both the skill type and the rank's static data, matching the two
  texts.
- `name_hash` is not the `stringtable.bss` key hash (both are unknown
  functions); it is kept as a hash because it is fixed per name and zero
  when the name is empty.
- `skillsimply.dbss` has exactly the same 30,424 keys and holds the learning
  rules (class, level, skill points, prerequisites), see
  [`skillsimply.dbss`](skillsimply_dbss.md).

## Open Questions

### What do `unknown_n04`, `unknown_n46` and `unknown_n55` hold?

Around `resource_cost` and `stamina_cost` the 74 bytes between `name_hash` and
`cooldown_ms` are sparse: byte `N+69` (`+86` with an empty name) is set on all
but 13 records, `N+5` and `N+7` on about two thirds and `N+4` on about a
third. The skill tooltip Lua also reads an HP cost (`_requireHp`), which is a
candidate; it needs a skill whose tooltip shows one.

### What do `unknown_tail` and `unknown_f32` control?

The 36 bytes before `next_skill_count` are zero on most records. On class
skills they hold a hash-like u32 at `+8`, an f32 at `+20` (`900.0` on Soul
Shower III) and sometimes a skill key and a u16 after it, and `unknown_f32` is `-1.0` on nearly every record. Their meaning
needs a skill whose tooltip shows a value that only these bytes could hold.
