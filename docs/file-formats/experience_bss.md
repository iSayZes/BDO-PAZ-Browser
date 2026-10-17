# `experience.bss` Format

## Purpose

Character level rules per class and level: one 236-byte record for every
class slot and every character level from 0 to 130. Two kinds of field
change with level: the u64 `unknown_08`, which rises with level on client
3473 and reads as the EXP to the next level (Open Questions), and the
one-time AP and DP bonuses: DP `+1` from level 56 and AP `+1` from level 60,
which the level-up window shows on those two levels. The file holds no HP, MP
or weight growth.


## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes     | Records                                               | Row bytes |
| ------ | -------------- | ------- | ---------------- | --------- | ----------------------------------------------------- | --------- |
| 2      | 3473 and later | 3474    | `experience.bss` | 1,453,467 | 6,157 Stat Body, 6,157 Level Record, 47 Class Group   | 200       |
| 1      | 1784           | 1784    | `experience.bss` | 3,201,480 | 10,742 Stat Body, 10,742 Level Record, 82 Class Group | 270       |

| Layout | File             | Known             | Unknown             |
| ------ | ---------------- | ----------------- | ------------------- |
| 2      | `experience.bss` | 320,379 B (22.0%) | 1,133,088 B (78.0%) |
| 1      | `experience.bss` | 558,948 B (17.5%) | 2,642,532 B (82.5%) |

<!-- versions:end -->

## Companion Files

The file is self-contained. The handler reads class names through the shared
LOC lookup:

| File                  | Required | Role                                   |
| --------------------- | -------- | -------------------------------------- |
| `languagedata_en.loc` | Optional | Class names (LOC type 21, `str_id1` = class type) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

A PABR file with no row count after the magic: the class groups start at
`+0x04`, and each group opens with its own level count. After the groups come
200 zero bytes, then a PABR string table with the layout of
`employeeexp.bss`.

| Offset                      | Type                                  | Field                | Notes                                                             |
| --------------------------- | ------------------------------------- | -------------------- | ----------------------------------------------------------------- |
| `+0x00`                     | char[4]                               | magic                | ASCII `PABR`                                                      |
| `+0x04`                     | Class Group[while level_count != 0]   | class_groups         | One group per class slot, 47 groups (class types 0 to 46) on client 3464; they end at the first `level_count` of `0`, the start of `unknown_after_class_groups` |
| `class_groups+0x00`         | bytes[200]                            | unknown_after_class_groups | Always 0; the size of one stat body                               |
| `class_groups+0xC8`         | String Table                          | string_table         | See String Table                                                  |
| `string_table+0x00`         | u32                                   | table_start          | Offset of the string table                                        |
| `string_table+0x04`         | u32                                   | zero                 | Always 0                                                          |

On client 3464 the walk over 47 groups ends at `0x162CBC`, 200 bytes before
the stored `table_start` `0x162D84`. The string table holds one wide string,
`1D1`. The parser ends the groups at `table_start` minus 200 instead of at a
`level_count` of `0`; both give `0x162CBC` there.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | `1` on client 3464                   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries                  |

### Class Group (variable: 4 bytes + levels)

`4 + 236 x level_count` bytes.

| Offset  | Type                      | Field       | Notes                                          |
| ------- | ------------------------- | ----------- | ---------------------------------------------- |
| `+0x00` | u32                       | level_count | `131` in every group on client 3464 (levels 0 to 130) |
| `+0x04` | Level Record[level_count] | levels      | `level_count` level records, level 0 first     |

### Level Record (236 bytes)

| Offset  | Type      | Field      | Notes                                                           |
| ------- | --------- | ---------- | --------------------------------------------------------------- |
| `+0x00` | u32       | class_type | Equals the group index; the class type `getClassType()` returns |
| `+0x04` | u32       | level      | Equals the record index in the group                            |
| `+0x08` | u64       | unknown_08 | Rises with level, the same in every group (Open Questions)      |
| `+0x10` | bytes[20] | unknown_10 | Always 0                                                        |
| `+0x24` | Stat Body | stats      | See Stat Body                                                   |

### Stat Body (200 bytes)

Offsets are from the start of the body, `+0x24` in a level record and `+0x01`
in a [hardcorecharacterstatstaticstatus.bss](hardcorecharacterstatstaticstatus_bss.md)
row; the `unknown_*` names follow these offsets in both files. Every offset
not named below is 0 in every body on client 3464.

| Offset  | Type      | Field               | Notes                                                 |
| ------- | --------- | ------------------- | ----------------------------------------------------- |
| `+0x00` | u32       | unknown_00          | Always `0`                                            |
| `+0x04` | f32       | max_hp              | Always `1.0` here; mount HP in `servantexperience.dbss` |
| `+0x08` | u32       | max_mp              | Always `1` here; mount stamina in `servantexperience.dbss` |
| `+0x0C` | bytes[20] | unknown_0c          | Always `0`                                            |
| `+0x20` | f32       | unknown_20          | Always `1.0`                                          |
| `+0x24` | bytes[20] | unknown_24          | Always `0`                                            |
| `+0x38` | u32       | max_critical_rate   | Always `0`; `5` for mounts                            |
| `+0x3C` | u32       | max_drop_item_luck  | `0` at level 0, `5` from level 1                      |
| `+0x40` | u32       | max_fishing_luck    | `0` at level 0, `5` from level 1                      |
| `+0x44` | u32       | max_collection_luck | `0` at level 0, `5` from level 1                      |
| `+0x48` | bytes[8]  | unknown_48          | Always `0`; `characterstatic.dbss` and `servantexperience.dbss` set the u32 at `+0x48`, see Notes |
| `+0x50` | f32       | unknown_50          | Always `1.0`                                          |
| `+0x54` | bytes[16] | unknown_54          | Always `0`                                            |
| `+0x64` | u32[3]    | max_varied_speed    | Attack, movement and casting speed limits; `0, 0, 0` at level 0, `5, 5, 5` from level 1 |
| `+0x70` | f32       | unknown_70          | Always `1.0`                                          |
| `+0x74` | f32       | ap_bonus            | `LVDD`; `0` below level 60, `1.0` from level 60       |
| `+0x78` | f32       | dp_bonus            | `LVPV`; `0` below level 56, `1.0` from level 56       |
| `+0x7C` | bytes[76] | unknown_7c          | Always `0`                                            |

`ap_bonus` and `dp_bonus` are the `lvdd` and `lvpv` values of the level-up
window. `PaGlobalFunc_Levelup_Info_All_SelfPlayerCurrentLevelInfo(...,
lvdd, lvpv)` in `panel_window_levelup_info_all_2.luac` (decompiled with
unluac) clears `lvpv` unless the player is level 56 and `lvdd` unless the
player is level 60, then shows `lvdd` on the Attack line and `lvpv` on the
Defense line. Those are the two levels where `dp_bonus` and `ap_bonus` change
from 0 to 1.

## Layout 1

On client 1784 a level record is 298 bytes. The run after `level` is 20
bytes, and the stat body is 270 bytes: an i16 after `max_mp` moves every
later field 2 bytes on, `unknown_54` is 12 bytes longer and the tail after
`dp_bonus` is 56 bytes longer. The groups run up to the string table with
no 200 zero bytes between; client 1784 has 82 groups (class types 0 to 31
and 51 to 100).

### File Layout

| Offset              | Type                     | Field        | Notes                                                |
| ------------------- | ------------------------ | ------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]                  | magic        | ASCII `PABR`                                         |
| `+0x04`             | Class Group[..table_start] | class_groups | Groups back to back until `table_start`            |
| `class_groups+0x00` | String Table             | string_table | Two strings on client 1784, `82D32` and an empty one |
| `EOF-0x08`          | u32                      | table_start  | Offset of the string table, where the groups end     |
| `EOF-0x04`          | u32                      | zero         | Always 0                                             |

### Level Record (298 bytes)

| Offset  | Type      | Field      | Notes                       |
| ------- | --------- | ---------- | --------------------------- |
| `+0x00` | u32       | class_type | The class type of the group |
| `+0x04` | u32       | level      | Equals the record index in the group |
| `+0x08` | u64       | unknown_08 | Always 0 on client 1784     |
| `+0x10` | bytes[12] | unknown_10 | Always 0                    |
| `+0x1C` | Stat Body | stats      | See Stat Body               |

### Stat Body (270 bytes)

Fields are unaligned. On the 4,192 (class, level) records client 1784
shares with client 3473, every field named in Layout 2 holds the same value
in both. Where the 12 extra bytes before `max_varied_speed` sit inside the
zero run is not known; they are counted into `unknown_54`.

| Offset  | Type      | Field               | Notes                                                 |
| ------- | --------- | ------------------- | ----------------------------------------------------- |
| `+0x00` | u32       | unknown_00          | Always `0`                                            |
| `+0x04` | f32       | max_hp              | Always `1.0`                                          |
| `+0x08` | u32       | max_mp              | Always `1`                                            |
| `+0x0C` | i16       | unknown_old_0c      | `0` at level 0, `100` at level 1, then `+2` per level up to `298` at level 100; the `StunGauge` pattern of the sheet in Field Names, at the place of the i16 that [servantexperience.dbss](servantexperience_dbss.md) Layout 1 holds |
| `+0x0E` | bytes[20] | unknown_0c          | Always `0`                                            |
| `+0x22` | f32       | unknown_20          | Always `1.0`                                          |
| `+0x26` | bytes[20] | unknown_24          | Always `0`                                            |
| `+0x3A` | u32       | max_critical_rate   | Always `0`                                            |
| `+0x3E` | u32       | max_drop_item_luck  | `0` at level 0, `5` from level 1                      |
| `+0x42` | u32       | max_fishing_luck    | `0` at level 0, `5` from level 1                      |
| `+0x46` | u32       | max_collection_luck | `0` at level 0, `5` from level 1                      |
| `+0x4A` | bytes[8]  | unknown_48          | Always `0`                                            |
| `+0x52` | f32       | unknown_50          | Always `1.0`                                          |
| `+0x56` | bytes[28] | unknown_54          | Always `0`                                            |
| `+0x72` | u32[3]    | max_varied_speed    | `0, 0, 0` at level 0, `5, 5, 5` from level 1          |
| `+0x7E` | f32       | unknown_70          | Always `1.0`                                          |
| `+0x82` | f32       | ap_bonus            | `0` below level 60, `1.0` from level 60               |
| `+0x86` | f32       | dp_bonus            | `0` below level 56, `1.0` from level 56               |
| `+0x8A` | bytes[72] | unknown_7c          | Always `0`                                            |
| `+0xD2` | u32       | unknown_d2          | `1000000` in every body on client 1784                |
| `+0xD6` | bytes[8]  | unknown_d6          | Always `0`                                            |
| `+0xDE` | u32[9]    | unknown_de          | `1` in all nine, in every body on client 1784         |
| `+0x102` | bytes[12] | unknown_102        | Always `0`                                            |

## Notes

- On client 3464 the 47 groups are byte-identical apart from `class_type`,
  and each group holds four distinct stat bodies: level 0, levels 1 to 55,
  levels 56 to 59 and levels 60 to 130. The unused class types (13, 14, 18,
  22 and those above the last class) have the same records as Warrior.
- Each row of [hardcorecharacterstatstaticstatus.bss](hardcorecharacterstatstaticstatus_bss.md)
  holds a stat body; on client 3464 every one equals the level 60 body here.
- The stat body is `_bss/experience/stat_body.py`, which both handlers import.
- On client 3464 two more files carry the same 200-byte body:
  `characterstatic.dbss` (15,064 bodies found by its four `1.0` floats) and
  every record of [servantexperience.dbss](servantexperience_dbss.md), where
  the body starts at record `+0x0A` and holds the mount's max HP (`+0x04`),
  max stamina (`+0x08`) and max weight (`+0x48`, LT x 10,000), checked
  against the stable window. Both hold `5, 5, 5` in the three luck limits
  and `10, 10, 10` in `max_varied_speed`; `servantexperience.dbss` also
  holds `5` in `max_critical_rate`. `characterstatic.dbss` also sets the u32 at
  `+0x48`, max weight, which is 0 here: `1` on 13,629 bodies, `100000` on 1,177, `0` on
  254 and `10000000` on 4. `servantexperience.dbss` keeps three inline `1D1`
  strings at body `+0xA0`, the place of this file's string fields (The `1D1`
  String).
- bdo-data-extractor describes 228-byte records with 20 reserved bytes and the
  stat body at `+0x1C`. On client 3464 that run (`unknown_08` and `unknown_10`) is 28 bytes and the
  records are 236 bytes; with 228 the groups do not end before the string
  table. Its stat-relative `apBonus` (+116, `+0x74`) and `dpBonus` (+120,
  `+0x78`) are `ap_bonus` and `dp_bonus` here.
- The level-up window gets HP, MP, stun and weight gains from the same event
  (`hp, mp, stun, weight, lvdd, lvpv`), but no field of this file changes
  with them. `max_hp` and `max_mp` hold `1.0` and `1` on every level, the
  level 0 placeholders of `servantexperience.dbss`, so player HP and MP come
  from another table.

## Field Names

The names of the luck and speed limits and of `ap_bonus` and `dp_bonus` follow the `Pc_Table` sheet of a private server's `DataSheets.bexcel` on client 1784, which shares 4,192 (class, level) rows with client 3473. `LVDD` equals `ap_bonus` and `LVPV` equals `dp_bonus` on all 4,192. `MaxAttackSpeed`, `MaxMoveSpeed`, `MaxCastingSpeed`, `MaxDropItemLuck`, `MaxFishingLuck` and `MaxCollectionLuck` are `0` on level 0 and `5` from level 1, the pattern of `+0x3C` to `+0x44` and `+0x64` to `+0x6C` on all 4,192 rows, and `MaxCriticalRate` is `0` on every row, as is `+0x38`.

Here all six limits hold `5`. [servantexperience.dbss](servantexperience_dbss.md#field-names) tells them apart: its `Servant_Table` holds `5` in the four critical and luck columns and `10` in the three speed columns, and its body holds `5` at `+0x38` to `+0x44` and `10` at `+0x64`. The 2016 client's `gc::CharacterStatStaticStatus` lists `_maxCriticalHitPoint`, `_maxDropItemPoint`, `_maxFishingPoint` and `_maxCollectionPoint` in that order, which splits the four, and `_maxVariedSpeedPoint` as one array of three.

`StunGauge` and `Suspension` (`100` on level 1, rising with level) are not in this file. `RequireEXP` is `0` on every sheet row, as is `unknown_08` in the private server's file on client 1784, so the sheet cannot name the u64 that client 3473 fills.

## Open Questions

### The Level `unknown_08`

On client 3473 the u64 at `+0x08` rises with level and is the same in all 47 groups: 20 on levels 0 and 1, then 24, 28, 33, 39, 58 up to 14,313,752,948,579 on level 99, which levels 100 to 130 repeat. It never falls from one level to the next. That fits the EXP from a level to the next, as `exp` in [servantexperience.dbss](servantexperience_dbss.md) reads. The bar in `panel_selfplayerexpgage.luac` reads the player's need through `getNeedExp_s64()` and no Lua function looks it up by level, so no client source ties the field to it yet. Client 1784 holds 0 there on every record.

### The Constant Fields

`unknown_20`, `unknown_50` and `unknown_70` hold `1.0` in every body, and no `Pc_Table` column holds `1.0`. `unknown_50` sits where the 2016 member order has `_productionHit`, but `ProductionHit` is `0` on every sheet row. [servantexperience.dbss](servantexperience_dbss.md#the-constant-fields) has the same three fields.

### The `max_varied_speed` Order

The three limits are equal in every body (`5` here, `10` for mounts), so the data does not tell which index is attack, movement or casting speed. The sheet lists `MaxAttackSpeed`, `MaxMoveSpeed` and `MaxCastingSpeed` in that order. `FromClient_CharInfoBasic_All_PotentialUpdate` in `panel_characterinfo_basic_all_3.lua` reads three speed indexes, `0` movement, `1` attack and `1 + _battleSpeed` casting, caps `characterStatPointSpeed(i)` at `characterStatPointLimitedSpeed(i)` and shows the result minus 5; a character with no speed gear shows `0`. If `characterStatPointLimitedSpeed` returns these limits, a player's limit of `5` would cap the shown value at `0`, so the player limit likely comes from elsewhere; which Lua index maps to which array index is open.

### The `1D1` String

The string table holds the dice expression `1D1`, in the form of the
`employeeexp.bss` growth dice (`1D5+30`). String index 0 is that string, so
any of the always-0 u32 fields could be an index to it; no field holds a
nonzero index. [servantexperience.dbss](servantexperience_dbss.md) points
to body `+0xA0`, `+0xA8` and `+0xB0`: its records store three inline `1D1`
strings, each followed by a 0 u32, from the matching place in the body. The
use of the dice stays open.
