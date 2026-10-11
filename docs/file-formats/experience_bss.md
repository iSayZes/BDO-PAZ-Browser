# `experience.bss` Format

## Purpose

Character level rules per class and level: one 236-byte record for every
class slot and every character level from 0 to 130. The only fields that
change with level are the one-time AP and DP bonuses: DP `+1` from level 56
and AP `+1` from level 60, which the level-up window shows on those two
levels. The file holds no EXP-to-next-level values and no HP, MP or weight
growth.

Example:

```text
class 0 Warrior, level 55: AP 0, DP 0
class 0 Warrior, level 56: AP 0, DP 1
class 0 Warrior, level 60: AP 1, DP 1
```

## Companion Files

The file is self-contained. The handler reads class names through the shared
LOC lookup:

| File                  | Required | Role                                   |
| --------------------- | -------- | -------------------------------------- |
| `languagedata_en.loc` | Optional | Class names (LOC type 21, `str_id1` = class type) |

All multi-byte values are little-endian.

## File Layout

A PABR file with no row count after the magic: the class groups start at
`+0x04`, and each group opens with its own level count. After the groups come
200 zero bytes, then a PABR string table with the layout of
`employeeexp.bss`.

| Offset   | Type    | Field        | Notes                                                             |
| -------- | ------- | ------------ | ----------------------------------------------------------------- |
| `+0x00`  | char[4] | magic        | ASCII `PABR`                                                      |
| `+0x04`  | group[] | class_groups | One group per class slot, 47 groups (class types 0 to 46) on client 3464 |
| after    | byte[200] | padding    | Always 0; the size of one stat body                               |
| after    | table   | string_table | u32 count, then `count` x (u8 is_wide, u32 byte length, payload)  |
| EOF - 8  | u32     | table_start  | Offset of the string table                                        |
| EOF - 4  | u32     | zero         | Always 0                                                          |

On client 3464 the walk over 47 groups ends at `0x162CBC`, 200 bytes before
the stored `table_start` `0x162D84`. The string table holds one wide string,
`1D1`.

## Record Structure

### Class Group (4 + 236 x `level_count` bytes)

| Offset  | Type     | Field       | Notes                                          |
| ------- | -------- | ----------- | ---------------------------------------------- |
| `+0x00` | u32      | level_count | `131` in every group on client 3464 (levels 0 to 130) |
| `+0x04` | record[] | levels      | `level_count` level records, level 0 first     |

### Level Record (236 bytes)

| Offset  | Type      | Field      | Notes                                                           |
| ------- | --------- | ---------- | --------------------------------------------------------------- |
| `+0x00` | u32       | class_type | Equals the group index; the class type `getClassType()` returns |
| `+0x04` | u32       | level      | Equals the record index in the group                            |
| `+0x08` | byte[28]  | reserved   | Always 0                                                        |
| `+0x24` | stat body | stats      | See Stat Body                                                   |

### Stat Body (200 bytes)

Offsets are from the start of the body, `+0x24` in a level record and `+0x01`
in a [hardcorecharacterstatstaticstatus.bss](hardcorecharacterstatstaticstatus_bss.md)
row; the `unknown_*` names follow these offsets in both files. Every offset
not in this table is 0 in every body on client 3464.

| Offset  | Type   | Field      | Notes                                                 |
| ------- | ------ | ---------- | ----------------------------------------------------- |
| `+0x04` | f32    | unknown_04 | Always `1.0`                                          |
| `+0x08` | u32    | unknown_08 | Always `1`                                            |
| `+0x20` | f32    | unknown_20 | Always `1.0`                                          |
| `+0x3C` | u32[3] | unknown_3c | `0, 0, 0` at level 0, `5, 5, 5` from level 1          |
| `+0x50` | f32    | unknown_50 | Always `1.0`                                          |
| `+0x64` | u32[3] | unknown_64 | `0, 0, 0` at level 0, `5, 5, 5` from level 1          |
| `+0x70` | f32    | unknown_70 | Always `1.0`                                          |
| `+0x74` | f32    | ap_bonus   | `0` below level 60, `1.0` from level 60               |
| `+0x78` | f32    | dp_bonus   | `0` below level 56, `1.0` from level 56               |

`ap_bonus` and `dp_bonus` are the `lvdd` and `lvpv` values of the level-up
window. `PaGlobalFunc_Levelup_Info_All_SelfPlayerCurrentLevelInfo(...,
lvdd, lvpv)` in `panel_window_levelup_info_all_2.luac` (decompiled with
unluac) clears `lvpv` unless the player is level 56 and `lvdd` unless the
player is level 60, then shows `lvdd` on the Attack line and `lvpv` on the
Defense line. Those are the two levels where `dp_bonus` and `ap_bonus` change
from 0 to 1.

## Suggested UI Layout

| Column   | Type | Notes                                     |
| -------- | ---- | ----------------------------------------- |
| Class Type | num | `class_type`                             |
| Class    | text | LOC type 21 name, else the number         |
| Level    | num  | `level`                                   |
| AP       | num  | `ap_bonus`                                |
| DP       | num  | `dp_bonus`                                |

## Notes

- On client 3464 the 47 groups are byte-identical apart from `class_type`,
  and each group holds four distinct stat bodies: level 0, levels 1 to 55,
  levels 56 to 59 and levels 60 to 130. The unused class types (13, 14, 18,
  22 and those above the last class) have the same records as Warrior.
- Each row of [hardcorecharacterstatstaticstatus.bss](hardcorecharacterstatstaticstatus_bss.md)
  holds a stat body; on client 3464 every one equals the level 60 body here.
- The stat body is `_bss/experience/stat_body.py`, which both handlers import.
- bdo-data-extractor describes 228-byte records with 20 reserved bytes and the
  stat body at `+0x1C`. On client 3464 the reserved run is 28 bytes and the
  records are 236 bytes; with 228 the groups do not end before the string
  table. Its stat-relative `apBonus` (+116, `+0x74`) and `dpBonus` (+120,
  `+0x78`) are `ap_bonus` and `dp_bonus` here.
- The level-up window gets HP, MP, stun and weight gains from the same event
  (`hp, mp, stun, weight, lvdd, lvpv`), but no field of this file changes
  with them.

## Open Questions

### The Constant Fields

`unknown_04`, `unknown_08`, `unknown_20`, `unknown_50` and `unknown_70` hold
the same value in every record, and `unknown_3c` and `unknown_64` only change
between level 0 and level 1, so the data gives nothing to tell them apart.
bdo-data-extractor links the two `5, 5, 5` triads to attack and defence growth
without naming a stat.

### The `1D1` String

The string table holds the dice expression `1D1`, in the form of the
`employeeexp.bss` growth dice (`1D5+30`). String index 0 is that string, so
any of the always-0 u32 fields could be an index to it; no field holds a
nonzero index.
