# `fevertimeskill.bss` Format

## Purpose

The Agris Fever drop skills: one 10-byte row per step with the skill that
Agris Fever applies and the item drop amount bonus it gives. On client 3474
the file lists five rows, index `1` to `5`, for the skills `Item Drop
Quantity Effect +100% (On)` (58988) and `+150% (On)` to `+300% (On)` (59042
to 59045), with `description` `1000000` to `3000000` on the client's
1,000,000 = 100% scale. The plain PABR file holds a u16 after the row count,
the rows, then an empty string table. The quests that spend Agris Fever
points are in [`feverquestdatatable.bss`](feverquestdatatable_bss.md), next
to this file in the same PAZ.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ----------------- | --------- |
| 1      | 1485 and later | 3474    | `fevertimeskill.bss` | 72    | 5 Fever Skill Row | 10        |

| Layout | File                 | Known        | Unknown    |
| ------ | -------------------- | ------------ | ---------- |
| 1      | `fevertimeskill.bss` | 70 B (97.2%) | 2 B (2.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10 at `str_id1=skill_no`    |

Without LOC the handler shows the Korean skill name from `skilltype.dbss`
through the skill name lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                   | Field              | Notes                                        |
| ------------------- | ---------------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]                | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32                    | count              | Number of rows                               |
| `+0x08`             | u16                    | unknown_08         | `5` on every client checked, equal to `count` and to the highest `index`; see Open Questions |
| `+0x0A`             | Fever Skill Row[count] | rows               | 10-byte rows repeated `count` times          |
| `rows+0x00`         | String Table           | string_table       | See String Table                             |
| `string_table+0x00` | u32                    | string_table_start | Offset of `string_count`, where the rows end (`10 + 10 * count`) |
| `string_table+0x04` | u32                    | zero               | Always `0`                                   |

The string table has the shape
[`feverquestdatatable.bss`](feverquestdatatable_bss.md) and
`specialquestinfo.bss` use (`_common/pabr_strings.py`). The rows run from
index `5` down to `1`.

### Fever Skill Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                     |
| ------- | ---- | ----------- | ------------------------------------------------------------------------- |
| `+0x00` | u16  | index       | Step, `1` to `5` on client 3474; unique                                   |
| `+0x02` | u16  | skill_level | Skill level of the `gc::SkillKey`; always `1`                             |
| `+0x04` | u16  | skill_no    | Skill number (`SkillNo`); keys the LOC type 10 name; `skill_no << 16 \| skill_level` is the `skill_key` of a `skill.dbss` record |
| `+0x06` | u32  | description | Item drop amount bonus of the skill; 1,000,000 = 100%                     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Field Names

The `FeverTimeSkill` sheet of a private server's `DataSheets.bexcel` on
client 1784 has three columns: `Index` (`index`), `SkillNo` (`skill_no`)
and `Description` (`description`). Its 5 rows match the client 1784 file in
all 5 rows, and the client 3474 file is byte for byte the same as the client
1784 one. The sheet has no level column; every row stores `skill_level`
`1`, the level the private server's `FeverTime` loader also gives its
`ClearBuffSkill` key (`SkillNo << 16 | 1`). The server executable of that
private server names the record type `FeverTimeSkillStaticStatus` and its
manager `FeverTimeSkillStaticStatusManager`, which reports a missing row as
`FeverTimeSkillStaticStatusManager SkillKey(%#)`, so it looks rows up by
skill key. The 2016 PDB has no `Fever` symbol.

`description` is the drop bonus. The client Lua reads
`player:getUseFeverSkillDropDesc()`, divides it by 10000 and fills it into
`{feverDropRate}` of `LUA_AGRISSPOINT_ICON_TOOLTIP` ("Item Drop Amount for
loot or basic resources +{feverDropRate}% by consuming points ...") in
`panel_widget_agrisgaugetooltip_1.luac` and
`panel_characterinfo_cashbuff_all_1.luac`. The values `1000000` to
`3000000` give the `+100%` to `+300%` in the skill names of their rows.

## Notes

- Raw rows on client 3474, in file order: index `5` / skill 59045 /
  `3000000`, `4` / 59044 / `2500000`, `3` / 59043 / `2000000`, `2` / 59042 /
  `1500000`, `1` / 58988 / `1000000`. Clients 1485, 1784, 2107, 2519, 3002
  and 3251 ship the same 72 bytes; clients 794 and 1230 have no
  `fevertimeskill.bss`.
- Each skill has one `skill.dbss` record, level `1`, and that record applies
  one buff: 58988 buff 58941, 59042 to 59045 buffs 59467 to 59470.
- The `FeverTime` sheet of the same `DataSheets.bexcel` (one row:
  `MaxPointOfFeverTime` `500000`, `MaxPointLimit`, `MaxPointPerDay`
  `150000`, `MaxPointLimitPerDay`, `SkillNo1` 58988, `SkillNo2` 58989,
  `AcceptConditions` `834,1`, `ClearBuffSkill` 58989, `Description`
  `500000`) is not in this file. The private server's `Load_FeverTime` reads
  it into one server parameter block. Skill 58989 is `Item Drop Quantity
  Effect (Off)` (buff 58942).
- The Lua toggles the buff icon through `getIsUseFeverSkill()` and the
  `FromClient_FeverSkillToggle` event (`panel_personalicon_left_remaster.luac`,
  `panel_widget_agrisgauge_2.luac`). No Lua file names this table or reads
  an index.

## Open Questions

### Field Before the Rows

`unknown_08` is a u16 between the PABR `count` and the first row, `5` on
every client from 1485 to 3474, where `count` and the highest `index` are
`5` as well. No other `.bss` in the test fixtures has a u16 equal to its
count at `+0x08` followed by rows that fill the file up to the string
table. A patch that adds or drops a step would show whether the field
follows `count`, the highest `index`, or neither.

### What Picks the Index

The file does not say which row is active for a family. The Agris tooltip
(LOC type 37, `LUA_AGRISSPOINT_ICON_TOOLTIP`) says completing the "Book of
Margahan" adventure logs Volumes 1 and 2 enhances Agris Fever. BDFoundry's
Book of Margahan guide gives a 100% junk drop increase without the logs
and "Junk item drop amount +50% (When consuming Agris Fever points)" as the
last reward of Book 1, for 150%; Book 2 adds points and daily recovery only
and stays at 150%. In game I started at 100% and had 150% after both
books. That fits index `1` (`1000000`) and index `2` (`1500000`). What
reaches indexes `3` to `5` (200% to 300%) is unknown.
None of the 3,073 client Lua files of client 3474 holds the skill numbers
58988 or 59042 to 59045 as a constant, so the Lua does not show the rule.
