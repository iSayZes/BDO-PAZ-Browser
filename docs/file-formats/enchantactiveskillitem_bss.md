# `enchantactiveskillitem.bss` Format

## Purpose

Gear that grants a skill at a given enhancement level: per item enchant key
(item and level) the skill key it grants. On client 3474 these are the
Taebaek and Asadal belts and the two Asadal necklaces, each with one skill
per level from base to PEN (`Blessing of Taebaek` at base, `TET: Fury of
Asadal` at TET).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `enchantactiveskillitem.bss` | 628   | 48 Row  | 13        |

| Layout | File                         | Known         | Unknown     |
| ------ | ---------------------------- | ------------- | ----------- |
| 1      | `enchantactiveskillitem.bss` | 580 B (92.4%) | 48 B (7.6%) |

<!-- versions:end -->

## Companion Files

None. The handler names the items through LOC type 0 and the skills through
LOC type 10, with their icons.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 48 x 13 = 628 bytes.

### Row (13 bytes)

| Offset  | Type | Field        | Notes                                                                                 |
| ------- | ---- | ------------ | ------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key     | Item enchant key, `enchant_level << 24 \| item_id`; unique                            |
| `+0x04` | u32  | skill_key    | Skill granted, `skill_no << 16 \| level` as in [`skill.dbss`](skill_dbss.md); level `1` on every row of client 3474 |
| `+0x08` | u32  | item_key_dup | Equals `item_key` on every row of clients 2519 and 3474                               |
| `+0x0C` | u8   | unknown_0c   | `0` on every row of clients 2519 and 3474                                             |

The rows are grouped by enhancement level (4, 5, 2, 3, 0, 1 on client 3474),
each level listing the items in descending ID order.

## Items and Skills

On client 3474 the 48 rows are 8 items x 6 levels; the items of one set
share their skills:

| Items                                                          | Skills (base to PEN)   |
| -------------------------------------------------------------- | ---------------------- |
| 12282 Taebaek's Belt, 12283 Tidal, 12284 Nightfallen            | 10189 to 10194         |
| 11688 Asadal Necklace, 11689 Moonlit Asadal Necklace            | 10206 to 10211         |
| 12285 Asadal Belt, 12286 Tidal, 12287 Nightfallen               | 10212 to 10217         |

Client 2519 has the 18 Taebaek's Belt rows only.

## Field Names

Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
1784 has the table, and the client 1784 PAZ has no
`enchantactiveskillitem.bss`. `item_key` and `skill_key` follow their
values: every `item_key` is an item of LOC type 0 with level `0` to `5`, and
every `skill_key` splits into a skill number of LOC type 10 (`10189`
Blessing of Taebaek, `10216` TET: Fury of Asadal) and level `1`. The skill
window (`panel_window_skillgroup_all_1.luac`) shows skills with
`_isActiveItemSkill` as "active item skills" while
`ToClient_IsActiveItemSkillEquipBySkillKey(skillKey)` is true; no Lua names
this file.

## Open Questions

### Trailing Byte

`unknown_0c` is `0` on every row of clients 2519 and 3474. Whether it is a
flag that no row sets yet is unknown.
