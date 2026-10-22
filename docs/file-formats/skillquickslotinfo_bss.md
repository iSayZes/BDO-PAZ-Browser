# `skillquickslotinfo.bss` Format

## Purpose

The skill each class has in its quick slots: one row per class type with
20 slots, each a skill number or empty. On client 3482 every class with
an entry fills slots 2 to 6 with five early skills (Warrior: Charging
Thrust I, Shield Charge I, Ground Slash I, Spinning Slash I, Scars of
Dusk).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------------------ | --------- |
| 1      | 1156 and later | 3482    | `skillquickslotinfo.bss` | 7,776 | 1,940 Slot, 97 Class Row | 4         |

| Layout | File                     | Known           | Unknown         |
| ------ | ------------------------ | --------------- | --------------- |
| 1      | `skillquickslotinfo.bss` | 3,896 B (50.1%) | 3,880 B (49.9%) |

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
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | Layout 1 |
| 1156   | Layout 1 |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. Class names come from LOC type 21 and skill names from LOC type 10.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                   | Field        | Notes                                                    |
| ------------------- | ---------------------- | ------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]                | magic        | `PABR`                                                   |
| `+0x04`             | Class Row[..table_start] | rows       | No row count: row `n` is class type `n`; 97 rows on client 3482, 82 on client 1784 |
| `rows+0x00`         | String Table           | string_table | See String Table                                         |
| `EOF-0x08`          | u32                    | table_start  | Offset of the string table, where `rows` ends            |
| `EOF-0x04`          | u32                    | zero         | Always `0`                                               |

### Class Row (80 bytes)

| Offset  | Type     | Field | Notes                                        |
| ------- | -------- | ----- | -------------------------------------------- |
| `+0x00` | Slot[20] | slots | Quick slots 0 to 19 in order; see Slot       |

### Slot (4 bytes)

| Offset  | Type | Field      | Notes                                                          |
| ------- | ---- | ---------- | -------------------------------------------------------------- |
| `+0x00` | u16  | skill_no   | Skill number, LOC type `10`; `0` in an empty slot              |
| `+0x02` | u16  | unknown_02 | `1` in every filled slot and `0` in every empty one (clients 1784 and 3482) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482                   |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `SkillQuickSlot_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `ClassType`, `SkillNo` and `SlotNo`, one
row per filled slot (a `ClassType` of `28, 31` fills Wizard and Witch). Read
with the row as `ClassType` and the slot as `SlotNo`, its 115 slots match
the 115 filled slots of the official client 1784 file on `SkillNo` (115 of
115) and all 115 of client 3482, which adds classes 6, 7, 15, 30, 33 and
35 (145 filled slots). The developer workbook of the same server
(`datasheet_skillquickslot.xlsm`) adds the note columns
`#PcLevel_ForLearning` (the level that learns the skill) and
`#SkillName`, and a memo that marks rows "expected to give a poor early
experience" for change.

The 2016 `gc::QuickSlot` is a `pa::Array` of 20 `value_type`, which is why
a row has 20 slots; its slot holds a `gc::SkillKey` (u32), an item key and
a position, not the 4 bytes here.

## Notes

- The other rows are all zero: on client 3482 rows 3, 13, 14, 18, 22, 32
  (Seraph), 34 and 36 to 96.
- The slot is a skill number with the `1` in the high half, the reverse of
  the skill key `skill_no << 16 | level` of `skill.dbss`. Whether
  `unknown_02` is the skill level is open.

## Open Questions

### When the Client Places These Skills

The workbook memo and `#PcLevel_ForLearning` point at the quick slots a new
character starts with, but no client Lua of client 3482 names the table.
Whether the skills go into the slots at creation or when the skill is
learned is open.

### What Fixes the Row Count

The file has 32 rows on client 1156, 82 on clients 1230 to 2107, 87 on
clients 2313 to 3251 and 97 from client 3474; `instancedungeonskillinfo.bss`
has the same count from client 1636 on, while `ui_skillgroup_*.bss` keeps
101 class slots. LOC type 21 names class types up to 100 on client 3482,
so the count is not the number of named class types.
