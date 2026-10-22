# `siegeangerskill.bss` Format

## Purpose

The guild skills of the siege Spirit of Battle gauge and the gauge's
values. Rows of a skill number, its cost, a skill type and a resource
type, then one block of eight u32: how much Spirit of Battle a death, a
kill and the war itself give, the maximum, and the survival rates. Client
3482 has 15 skills; the two with resource type `1` (Breath of Life and
Blessing of Battle) cost the whole gauge.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3482    | `siegeangerskill.bss` | 172   | 15 Row  | 8         |

| Layout | File                  | Known          | Unknown    |
| ------ | --------------------- | -------------- | ---------- |
| 1      | `siegeangerskill.bss` | 172 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                     |
| --------------------- | -------- | ------------------------ |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field                     | Notes                                                    |
| ------------------- | -------------- | ------------------------- | -------------------------------------------------------- |
| `+0x00`             | char[4]        | magic                     | ASCII `PABR`                                             |
| `+0x04`             | u32            | row_count                 | Number of rows                                           |
| `+0x08`             | Row[row_count] | rows                      | See Row; byte-packed                                     |
| `rows+0x00`         | u32            | anger_point_per_death     | `200` on clients 1784 and 3482                           |
| `rows+0x04`         | u32            | max_anger_point           | `10000`; `ToClient_GetMaxAngerPoint()`                   |
| `rows+0x08`         | u32            | anger_point_per_kill      | `100` on clients 1784 and 3482                           |
| `rows+0x0C`         | u32            | increase_point            | `100` on clients 1784 and 3482                           |
| `rows+0x10`         | u32            | decrease_survival_percent | `900000` (90% on the 1,000,000 = 100% scale)             |
| `rows+0x14`         | u32            | decrease_survival_point   | `100` on clients 1784 and 3482                           |
| `rows+0x18`         | u32            | increase_survival_percent | `500000` (50%)                                           |
| `rows+0x1C`         | u32            | increase_survival_point   | `200` on clients 1784 and 3482                           |
| `rows+0x20`         | String Table   | string_table              | See String Table                                         |
| `string_table+0x00` | u32            | table_start               | Offset of the string table, where the eight u32 end      |
| `string_table+0x04` | u32            | zero                      | Always `0`                                               |

### Row (8 bytes)

| Offset  | Type | Field                     | Notes                                                                       |
| ------- | ---- | ------------------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16  | skill_no                  | `skilltype.dbss` skill number; one row each                                 |
| `+0x02` | u32  | resource_point            | Cost in the resource; `10000` on the resource type `1` rows, else `0`       |
| `+0x06` | u8   | siege_anger_skill_type    | `2`, `3` or `4`; see Skills                                                 |
| `+0x07` | u8   | siege_skill_resource_type | `1` on the two rows that cost Spirit of Battle, else `0`                    |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Skills

Client 3482, in file order, with the LOC type 10 skill name. Every
`resource_point` is `0` but the two type `1` rows.

| `skill_no` | Name                     | `siege_anger_skill_type` | `siege_skill_resource_type` |
| ---------- | ------------------------ | ------------------------ | --------------------------- |
| 65216      | Breath of Life           | 3                        | 1                           |
| 62846      | BreezyVoyage             | 4                        | 0                           |
| 65227      | Blessing of Battle       | 3                        | 1                           |
| 65225      | Battle Command to Gather | 3                        | 0                           |
| 65033      | Call of the Lord         | 2                        | 0                           |
| 65202      | Boost Morale             | 3                        | 0                           |
| 65106      | Horrors of Battle        | 3                        | 0                           |
| 62845      | Seaforge Blessing        | 4                        | 0                           |
| 65108      | Battle Reorganization I  | 3                        | 0                           |
| 65109      | Frenzied Fighter         | 3                        | 0                           |
| 65111      | Intimidating Force       | 3                        | 0                           |
| 62848      | Admiral's Rally          | 4                        | 0                           |
| 65209      | Healing Touch            | 3                        | 0                           |
| 65211      | Battle Reorganization II | 3                        | 0                           |
| 62847      | Seawatch Pulse           | 4                        | 0                           |

Client 1784 has the 11 rows with types `2` and `3`, in the same order;
client 3482 adds the four type `4` skills `62845` to `62848`.

## Field Names

The `SiegeAngerSkill` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `SkillNo`, `ResourcePoint`, `SkillType` and
`ResourceType`, and its 11 rows match the 11 rows of the client 1784 file
in order and value (11 of 11). That server's dump (client 1784) names the
members `SiegeAngerSkillStaticStatus _skillNo`, `_resourcePoint`,
`_siegeAngerSkillType` and `_siegeSkillResourceType`; the field names are
these members.

The eight u32 after the rows are the `SiegeAngerPoint` sheet (client 1784,
one row). The dump checks its columns in the order
`AngerPointPerDeath`, `MaxAngerPoint`, `AngerPointPerKill`,
`IncreasePoint`, `DecreaseSurvivalPercent`, `DecreasesurvivalPoint`,
`IncreaseSurvivalPercent`, `IncreaseSurvivalPoint`, then the four
distance columns. In that order the sheet's values are the client 1784
file's eight u32 (8 of 8); in the sheet's own column order
(`MaxAngerPoint` first) only five of eight match. `anger_point_per_kill`
and `increase_point` are both `100` on every client checked, so their
order rests on the dump alone. The four distance columns
(`AngerPointDeathDistance` to `AngerPointEffectiveCastleDistance`, `6500`
each in the sheet) are not in this file.

The client Lua of client 3482 reads `ToClient_GetMaxAngerPoint()` and
`ToClient_GetCostPointSiegeAngerSkill(skillNo)` and shows a skill's cost
as cost / maximum when `ToClient_SiegeSkillResourceType(skillNo)` is
`__eSiegeSkillResourceType_SiegeAngerPoint`
(`panel_tooltip_skillgroup_1.luac`). The gauge tooltip
`LUA_ANGRYPOINT_DESC` reads "Can obtain by fighting in Node/Conquest
Wars. Consume Spirit of Battle to cast certain Guild Skills."

## Notes

- The two `resource_point` `10000` rows cost 100% of `max_anger_point`.
- The type `4` skills (Seaforge Blessing, Admiral's Rally and two more)
  have Blue Battlefield names.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  one line per skill with its name, and the eight gauge values (stored
  once) on every line, the two rates as percentages.

## Open Questions

### Skill Type and Resource Type Values

`siege_anger_skill_type` is `2` (Call of the Lord), `3` (the Node War and
Conquest War guild skills) or `4` (four Blue Battlefield skills). The client
Lua has no `__eSiegeAngerSkillType` constant and the 2016 PDB no enum, so
the values have no names. For `siege_skill_resource_type` the Lua only
names `__eSiegeSkillResourceType_SiegeAngerPoint`, without its value; the
two rows that cost the gauge hold `1`.
