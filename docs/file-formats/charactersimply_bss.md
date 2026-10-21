# `charactersimply.bss` Format

## Purpose

Stores one fixed 119-byte row per character template (player classes, NPCs, monsters, mounts, objects): the character ID, its kind, grade, level and group, spawn hours, body size and height, HP, vehicle settings, display and interaction flags, and string-table indexes for the model path, the voice bank, the Korean name and title, the action script and the interaction condition. It holds the same 24,553 characters as [characterstatic.dbss](characterstatic_dbss.md) (client 3474), and every field it shares with that file holds the same value; see [Field Names](#field-names). Names and titles in the user's language come from LOC type `6`, keyed by `character_id`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes     | Records    | Row bytes |
| ------ | -------------- | ------- | --------------------- | --------- | ---------- | --------- |
| 2      | 3474 and later | 3474    | `charactersimply.bss` | 3,861,711 | 24,553 Row | 119       |
| 1      | 1784 to 2519   | 2519    | `charactersimply.bss` | 3,364,243 | 21,201 Row | 121       |

| Layout | File                  | Known               | Unknown           |
| ------ | --------------------- | ------------------- | ----------------- |
| 2      | `charactersimply.bss` | 3,296,992 B (85.4%) | 564,719 B (14.6%) |
| 1      | `charactersimply.bss` | 2,834,218 B (84.2%) | 530,025 B (15.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 2             |
| 3251   | No documented layout |
| 3002   | No documented layout |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | No documented layout |
| 1230   | No file              |
| 794    | No file              |

<!-- versions:end -->

## Companion Files

None. Names and titles in the user's language come from LOC type `6` (see Purpose).

All multi-byte values are little-endian.

## Layout 2

### File Layout

PABR block: a fixed-width row table, then the counted string table the rows index into, then the 8-byte trailer.

| Offset              | Type          | Field        | Notes |
| ------------------- | ------------- | ------------ | ----- |
| `+0x00`             | char[4]       | magic        | ASCII `PABR` |
| `+0x04`             | u32           | count        | Number of rows; `24553` on client 3474 |
| `+0x08`             | Row[count]    | rows         | See Row |
| `rows+0x00`         | String Table  | string_table | See String Table |
| `string_table+0x00` | u32           | table_start  | Equals `0x08 + count * 119`, where the rows end |
| `string_table+0x04` | u32           | zero         | Always `0` |

### Row (119 bytes)

Counts on client 3474. A field named as in `characterstatic.dbss` holds that file's value for the same character on every row.

| Offset  | Type     | Field                     | Notes |
| ------- | -------- | ------------------------- | ----- |
| `+0x00` | u16      | character_id              | Same key as `characterstatic.dbss`; both files hold the same 24,553 IDs |
| `+0x02` | u8       | is_giant                  | `2` on 992 rows, `1` on 421 |
| `+0x03` | i16      | spawn_start_hour          | `-1` on 24,478 rows |
| `+0x05` | i16      | spawn_end_hour            | `-1` on 24,478 rows |
| `+0x07` | u8       | is_fixed                  | `1` on 4,534 rows |
| `+0x08` | u16      | collect_drop_id           | Non-zero on 886 rows |
| `+0x0A` | u8       | unknown_0a                | `1` on 45 rows, all `npc_kind` `7` (node forts, Field HQ, Command Post); see Open Questions |
| `+0x0B` | u8       | unknown_0b                | `1` on 193 rows, all `npc_kind` `9` (fences, barricades, siege installations); see Open Questions |
| `+0x0C` | u8       | is_client_ai              | `1` on 3,582 rows |
| `+0x0D` | u32      | model_path_ref            | String-table index of `model_path`, the action-chart path |
| `+0x11` | u32      | model_path_hash           | Hash of `model_path` |
| `+0x15` | u8       | npc_kind                  | `gc::CharacterKind`; see [`npc_kind` Values](characterstatic_dbss.md#npc_kind-values) |
| `+0x16` | u8       | class_type                | `101` on every row that is not a player character |
| `+0x17` | f32      | body_height               | |
| `+0x1B` | f32      | body_size                 | |
| `+0x1F` | f32      | max_hp                    | `10000.0` on Ehren (`47791`) |
| `+0x23` | u64      | attribute_type_mask       | Bit `n` set for each `AttributeType` value `n` |
| `+0x2B` | u8       | unknown_2b                | `1` on 4,860 rows: all 3,296 of `npc_kind` `3`, 902 of `2`, 563 of `4`; see Open Questions |
| `+0x2C` | u8       | unknown_2c                | `1` on 5,725 rows; `characterstatic.dbss` `unknown_b5`; see Open Questions |
| `+0x2D` | u8       | is_tamable                | `1` on 11 rows |
| `+0x2E` | u8       | is_opti_monster           | `1` on 54 rows, `2` on 13 |
| `+0x2F` | bytes[3] | unknown_2f                | Always `0` |
| `+0x32` | u8       | is_render_shadow          | `1` on 22,103 rows |
| `+0x33` | u8       | use_default_audio         | `1` on 12,462 rows |
| `+0x34` | u32      | voice_bank_ref            | String-table index of `voice_bank` (`NPC_VCE_47343`); the empty string on 14,408 rows |
| `+0x38` | u8       | unknown_38                | `1` on 87 rows: 66 of `npc_kind` `3`, 19 of `2`, 2 of `1`; see Open Questions |
| `+0x39` | u8       | is_carrier                | `1` on 368 rows |
| `+0x3A` | u8       | vehicle_type              | `CppEnums.VehicleType`; `65` when the character is not a vehicle |
| `+0x3B` | i16      | team_no                   | `-1` on 567 rows, `1` to `7` on 306 |
| `+0x3D` | u8       | unknown_3d                | `1` on 59 rows; `characterstatic.dbss` `unknown_a1` |
| `+0x3E` | u8       | is_hidden_name            | `1` on 10,373 rows |
| `+0x3F` | i32      | is_live_collect           | `-1` on 4 rows, `1` on 3, else `0`; see [Field Names](#field-names) |
| `+0x43` | u8       | unknown_43                | Always `1` |
| `+0x44` | u32      | name_kr_ref               | String-table index of `name_kr`, the Korean name |
| `+0x48` | u32      | title_kr_ref              | String-table index of `title_kr`, the Korean title; the empty string on 18,311 rows |
| `+0x4C` | u8       | unknown_4c                | `1` on 399 rows; see Open Questions |
| `+0x4D` | u8       | grade                     | `CppEnums.CharacterGradeType` |
| `+0x4E` | u8       | is_hidden_hp              | `1` on 4,054 rows |
| `+0x4F` | u32      | level                     | `1` on 9,628 rows, `99` on 5,531 |
| `+0x53` | i16      | character_group           | Non-zero on 2,450 rows |
| `+0x55` | u32      | fusion_group_key          | `1` on `530` (Aal's Breath) only; see [Field Names](#field-names) |
| `+0x59` | u8       | unknown_59                | `1` on 133 rows; `characterstatic.dbss` `unknown_b7` |
| `+0x5A` | u8       | unknown_5a                | `2` on 24,419 rows, `0` on 132, `1` on 2; `characterstatic.dbss` `unknown_b2` |
| `+0x5B` | u8       | unknown_5b                | `1` on 77 rows; `characterstatic.dbss` `unknown_a2` |
| `+0x5C` | u8       | unknown_5c                | Always `0x15`, as `characterstatic.dbss` `unknown_08` |
| `+0x5D` | u32      | action_script_ref         | String-table index of `action_script`; `getknowledge(<id>);` on most of the 5,687 non-empty rows |
| `+0x61` | u16      | steal_drop_id             | Non-zero on 526 rows |
| `+0x63` | u16      | unknown_63                | Always `0` |
| `+0x65` | u8       | inventory_max             | Non-zero on 507 rows |
| `+0x66` | u8       | absolute_interaction      | `1` on 692 rows |
| `+0x67` | u8       | is_attacked_pvp_mode_only | `1` on 1,290 rows |
| `+0x68` | u8       | vehicle_driver_ridable    | `1` on 3,303 rows |
| `+0x69` | u8       | vehicle_seat_count        | `1` on 3,034 rows, up to `15` |
| `+0x6A` | u32      | condition_script_ref      | String-table index of `condition_script`, the interaction condition; non-empty on 402 rows |
| `+0x6E` | u8       | vehicle_sub_type          | Non-zero on 100 rows (`1` to `4`) |
| `+0x6F` | u8       | is_guild_vehicle          | `1` on 85 rows |
| `+0x70` | u8       | unknown_70                | `10` on 24,112 rows; `characterstatic.dbss` `unknown_c2` |
| `+0x71` | u8       | carriage_type             | Non-zero on 30 rows (`1` to `5`); a u32 in `characterstatic.dbss` |
| `+0x72` | bytes[4] | unknown_72                | Always `0` |
| `+0x76` | u8       | unknown_76                | `1` on 2,418 rows; `characterstatic.dbss` `unknown_contents_group_hashes_17` |

The six `*_ref` fields index the string table from `0`. The parser stores each string under the field name without `_ref` (`model_path`, `voice_bank`, `name_kr`, `title_kr`, `action_script`, `condition_script`).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `31277` on client 3474 |
| `+0x04` | pstr[string_count] | strings      | Counted entries, indexed from `0` |

The entry layout is the one [npcsimply.bss](npcsimply_bss.md) uses: a u8 `is_wide` (`1` for UTF-16LE, `0` for UTF-8), a u32 byte length and the text, with no terminator. On client 3474, 17,566 entries are UTF-16LE (the scripts and the Korean texts) and 13,711 UTF-8 (model paths and voice banks). Index `1` is the empty string. The last entry ends at the trailer.

## Layout 1

The client 1784 file (15,704 rows of 121 bytes). It has 4 more bytes after `model_path_hash` and a zero byte after `absolute_interaction`, and lacks `unknown_63` and `unknown_76`. Only Row differs from Layout 2. The parser reads only Layout 2.

### Row (121 bytes)

| Offset  | Type     | Field                                | Notes |
| ------- | -------- | ------------------------------------ | ----- |
| `+0x00` | u16      | character_id                         | |
| `+0x02` | u8       | is_giant                             | |
| `+0x03` | i16      | spawn_start_hour                     | |
| `+0x05` | i16      | spawn_end_hour                       | |
| `+0x07` | u8       | is_fixed                             | |
| `+0x08` | u16      | collect_drop_id                      | |
| `+0x0A` | u8       | unknown_0a                           | |
| `+0x0B` | u8       | unknown_0b                           | |
| `+0x0C` | u8       | is_client_ai                         | |
| `+0x0D` | u32      | model_path_ref                       | |
| `+0x11` | u32      | model_path_hash                      | |
| `+0x15` | u32      | unknown_after_model_path_hash        | Non-zero on 96 rows; 28 of them hold `3171023435` |
| `+0x19` | u8       | npc_kind                             | |
| `+0x1A` | u8       | class_type                           | |
| `+0x1B` | f32      | body_height                          | |
| `+0x1F` | f32      | body_size                            | |
| `+0x23` | f32      | max_hp                               | |
| `+0x27` | u64      | attribute_type_mask                  | |
| `+0x2F` | u8       | unknown_2b                           | |
| `+0x30` | u8       | unknown_2c                           | |
| `+0x31` | u8       | is_tamable                           | |
| `+0x32` | u8       | is_opti_monster                      | |
| `+0x33` | bytes[3] | unknown_2f                           | |
| `+0x36` | u8       | is_render_shadow                     | |
| `+0x37` | u8       | use_default_audio                    | |
| `+0x38` | u32      | voice_bank_ref                       | |
| `+0x3C` | u8       | unknown_38                           | |
| `+0x3D` | u8       | is_carrier                           | |
| `+0x3E` | u8       | vehicle_type                         | |
| `+0x3F` | i16      | team_no                              | |
| `+0x41` | u8       | unknown_3d                           | |
| `+0x42` | u8       | is_hidden_name                       | |
| `+0x43` | i32      | is_live_collect                      | |
| `+0x47` | u8       | unknown_43                           | |
| `+0x48` | u32      | name_kr_ref                          | |
| `+0x4C` | u32      | title_kr_ref                         | |
| `+0x50` | u8       | unknown_4c                           | |
| `+0x51` | u8       | grade                                | |
| `+0x52` | u8       | is_hidden_hp                         | |
| `+0x53` | u32      | level                                | |
| `+0x57` | i16      | character_group                      | |
| `+0x59` | u32      | fusion_group_key                     | |
| `+0x5D` | u8       | unknown_59                           | |
| `+0x5E` | u8       | unknown_5a                           | |
| `+0x5F` | u8       | unknown_5b                           | |
| `+0x60` | u8       | unknown_5c                           | |
| `+0x61` | u32      | action_script_ref                    | |
| `+0x65` | u16      | steal_drop_id                        | |
| `+0x67` | u8       | inventory_max                        | |
| `+0x68` | u8       | absolute_interaction                 | |
| `+0x69` | u8       | unknown_after_absolute_interaction   | Always `0` |
| `+0x6A` | u8       | is_attacked_pvp_mode_only            | |
| `+0x6B` | u8       | vehicle_driver_ridable               | |
| `+0x6C` | u8       | vehicle_seat_count                   | |
| `+0x6D` | u32      | condition_script_ref                 | |
| `+0x71` | u8       | vehicle_sub_type                     | |
| `+0x72` | u8       | is_guild_vehicle                     | |
| `+0x73` | u8       | unknown_70                           | |
| `+0x74` | u8       | carriage_type                        | |
| `+0x75` | bytes[4] | unknown_72                           | Always `0` |

## Field Names

Every named field except `is_live_collect` and `fusion_group_key` carries the name of the [characterstatic.dbss](characterstatic_dbss.md) field it equals, and each `*_ref` the name of the string it points at: on client 3474 all 24,553 rows hold the same value as that file's field for the same character, the six strings included. `characterstatic.dbss` takes those names from the `Character_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (see its [Field Names](characterstatic_dbss.md#field-names)).

The other two match a `Character_Table` column by value on every row that shares a key with the sheet:

| Field | `Character_Table` column | Rows that agree, client 1784 | Rows that agree, client 3474 |
| ----- | ------------------------ | ---------------------------- | ---------------------------- |
| `is_live_collect` | `IsLiveCollect` | 15,704 of 15,704 | 16,058 of 16,058 |
| `fusion_group_key` | `FusionGroupKey` | 15,704 of 15,704 | 16,058 of 16,058 |

Both fields sit where `characterstatic.dbss` has `is_live_collect` and `unknown_1b`, and hold the same values. `fusion_group_key` is non-zero on one row in both clients (`1` on character `530`, Aal's Breath), so its match rests on that row and the zeros.

## Notes

- `characterstatic.dbss` gained `unknown_contents_group_hashes_17` in client 3464, and `unknown_76` holds the same value here. The client 1784 row has no such byte.
- The row stores the fields in another order than `characterstatic.dbss`: `team_no`, `carriage_type`, `steal_drop_id` and `attribute_type_mask` sit after the strings there and in the fixed row here.
- [Attribute Types](characterstatic_dbss.md#attribute-types) and [`npc_kind` Values](characterstatic_dbss.md#npc_kind-values) in the `characterstatic.dbss` doc apply to this file unchanged.

## Open Questions

### What do `unknown_0a` and `unknown_0b` mark?

`unknown_0a` is `1` on 45 rows, all `npc_kind` `7`: the node forts, the Field HQ (`12821`) and the Command Post (`12820`). On every row that shares a key with the private server's `Character_Table` it is `1` exactly where `MoraleValue` is non-zero (`500000`): 19 of 16,058 rows on client 3474, 21 of 15,704 on client 1784. It looks like a "has morale" flag for siege structures, but the sheet column holds the amount, not a flag, so the field stays `unknown_0a`. `unknown_0b` is `1` on 193 rows, all `npc_kind` `9` (`12842` Flimsy Wooden Fence, `12841` Flimsy Barricade, `12839` Indomitable Flag Factory), and matches no sheet column.

Checked on client 3474, without a name for either byte:

| Source | Result |
| ------ | ------ |
| `characterstatic.dbss` | No byte is non-zero on exactly the same rows. The closest is `repair_resources`: `3` on 42 of the 45 `unknown_0a` rows, but also on 23 rows without it |
| `Character_Table` of a private server on client 519 | `unknown_0a` agrees with `MoraleValue` non-zero on all 12,008 shared rows (9 flagged). `unknown_0b` matches none of its 171 columns |
| 2016 `gc::CharacterStaticStatus` | No morale member. Its `gc::ObjectStaticStatus` holds two adjacent bools, `_isSiegeTent` and `_isSiegeOrFortressTent`, but `unknown_0b` sits on fences and barricades, which are not tents |
| Client Lua | `isBarricade()`, `isSiegeTower()` and the other siege checks are called on `getObjectStaticStatus()`, the installation type, not on a character flag; no Lua reads a morale value from the character |

The client 1784 server binary has a `CharacterSimplyStaticStatusManager` (`link` and `relinkAndCheckValid` error strings); the code that fills it would name both bytes.

### What is `unknown_2c`?

It equals `characterstatic.dbss` `unknown_b5` on every row. On client 1784 it is `1` exactly where `Character_Table` `TalkAble` is non-zero (`1`, `2` or `3`) on all 15,704 rows; on client 3474 the same holds on 16,051 of 16,058 rows. The column holds a talk type rather than a flag, so the field stays unknown until the client is shown to read it as "can talk".

### What do `unknown_2b`, `unknown_38` and `unknown_4c` hold?

None of them has a counterpart in `characterstatic.dbss` or a matching `Character_Table` column. `unknown_2b` is set on every `npc_kind` `3` row and on 1,564 others; its best sheet match, `IsClientAI`, agrees on only 15,085 of 16,058 rows. `unknown_38` is set on 87 rows, among them `37065` Ancient Teleporter and `35636` Galley under Construction. `unknown_4c` is `1` exactly where `condition_script` is non-empty, except on three rows (`23751` Mirumok Watcher Offin, `23767`, `23810`) whose condition is `getitemcount(40414,0)>0;`; on client 1784 it agrees with a non-empty `InteractionCondition` on all 15,704 rows.
