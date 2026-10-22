# `skillfusionslotlist.bss` Format

## Purpose

The Skill Enhancement choices of each class, grouped by slot: one row per
class type with five slots, each a list of
[`skillfusion.dbss`](skillfusion_dbss.md) keys. On client 3482 every class
offers two enhanced skills in each of slots 0, 1 and 2 (Warrior slot 0:
Seismic Strike or Frenzied Spear); slots 3 and 4 are empty.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records                 | Row bytes               |
| ------ | -------------- | ------- | ------------------------- | ------ | ----------------------- | ----------------------- |
| 1      | 1348 and later | 3482    | `skillfusionslotlist.bss` | 41,204 | 505 Slot, 101 Class Row | 4 to 260, 82 on average |

| Layout | File                      | Known             | Unknown    |
| ------ | ------------------------- | ----------------- | ---------- |
| 1      | `skillfusionslotlist.bss` | 41,204 B (100.0%) | 0 B (0.0%) |

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
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. Class names come from LOC type 21 and skill names from LOC type 10;
the main and sub skill of each choice are in `skillfusion.dbss`.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset      | Type                     | Field        | Notes                                                         |
| ----------- | ------------------------ | ------------ | ------------------------------------------------------------- |
| `+0x00`     | char[4]                  | magic        | `PABR`                                                        |
| `+0x04`     | Class Row[..table_start] | rows         | No row count: row `n` is class type `n`; 101 rows on clients 1784 and 3482 |
| `rows+0x00` | String Table             | string_table | See String Table                                              |
| `EOF-0x08`  | u32                      | table_start  | Offset of the string table, where `rows` ends                 |
| `EOF-0x04`  | u32                      | zero         | Always `0`                                                    |

### Class Row (variable: 0 bytes + slots)

| Offset  | Type    | Field | Notes                              |
| ------- | ------- | ----- | ---------------------------------- |
| `+0x00` | Slot[5] | slots | Slots 0 to 4 in order; see Slot    |

### Slot (variable: 4 bytes + keys)

| Offset  | Type                         | Field                  | Notes                                                       |
| ------- | ---------------------------- | ---------------------- | ----------------------------------------------------------- |
| `+0x00` | u32                          | skill_fusion_key_count | Number of keys; `0` for an empty slot                       |
| `+0x04` | u32[skill_fusion_key_count]  | skill_fusion_keys      | `skillfusion.dbss` keys, skill keys `skill_no << 16 \| level` (level `1`) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482         |
| `+0x04` | pstr[string_count] | strings      | No field reads a string              |

## Field Names

No sheet has the table's shape; it is `skillfusion.dbss` grouped by class
and `slot_no`. Every key in rows 0 to 50 is a `skillfusion.dbss` key whose
`slot_no` is the slot it sits in: 192 of 192 keys on client 3482, and on
client 1784 the 138 keys of the `SkillFusion` sheet of a private server's
`DataSheets.bexcel`, whose `SlotNo` matches 138 of 138. The list order is
not the sheet's `OrderNo`: on client 3482, 60 of the 96 class lists hold
order `1` first.

## Notes

- The skill window reads the table by class type and slot:
  `panel_window_skillgroup_all_1.luac` (client 3482) loops `index` from `0`
  to `__eSkillFusionSlotMaxCount - 1` and calls
  `ToClient_getFusionSkillNoByClassType(classType, index, 0)`, the first
  choice of each slot. The enum's value is not in the Lua.
- Rows 51 to 100 are the hero class types of LOC type 21 (`51` Cliff, `52`
  Jordine, ... `69` Orwen, then `[PH]` placeholders from `70`). Each holds
  the same three lists: every key of that slot over all classes, 64 keys on
  client 3482 and 46 on client 1784.
- On client 3482 rows 0 to 12, 15 to 17, 19 to 21 and 23 to 35 hold keys:
  32 classes. Client 1784 fills 27 rows below 51, row 6 with four keys per
  slot and the others with two.

## Open Questions

### Why the Hero Rows Hold Every Key

Rows 51 to 100 hold all classes' keys of each slot, while the class rows
below 51 without keys (13, 14, 18 and 22 on client 3482) stay empty.
Whether a hero character can pick any class's enhancement is not in the
Lua.
