# `buffsimply.bss` Format

## Purpose

A compact copy of [`buff.dbss`](buff_dbss.md): one fixed 32-byte row per buff
with the buff ID, the icon path and `effect_name` as indices into a shared
string table, `is_shown`, `is_debuff`, `remove_on_dead` and the equipment the
buff needs. It holds no name, parameters,
duration or description, so it covers what the buff bar needs to draw a buff
and nothing about its effect.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes     | Records         | Row bytes |
| ------ | -------------- | ------- | ---------------- | --------- | --------------- | --------- |
| 2      | 3473 and later | 3473    | `buffsimply.bss` | 1,489,433 | 44,690 Buff Row | 32        |

| Layout | File             | Known             | Unknown           |
| ------ | ---------------- | ----------------- | ----------------- |
| 2      | `buffsimply.bss` | 819,083 B (55.0%) | 670,350 B (45.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                        |
| --------------------- | -------- | ----------------------------------------------------------- |
| `buff.dbss`           | Optional | Full buff records; every row here has a record there        |
| `languagedata_en.loc` | Optional | English descriptions, LOC type 5 keyed by `buff_id`         |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The shared PABR string table layout of `npcsimply.bss` and
`plantexchangegroup.bss` (`_common/pabr_strings.py`).

| Offset              | Type            | Field        | Notes                                                  |
| ------------------- | --------------- | ------------ | ------------------------------------------------------ |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                           |
| `+0x04`             | u32             | count        | Number of rows; 44,683 on client 3464, equal to the `buff.dbss` count |
| `+0x08`             | Buff Row[count] | rows         | See Buff Row                                           |
| `rows+0x00`         | String Table    | string_table | See String Table                                       |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where the rows end         |
| `string_table+0x04` | u32             | zero         | Always 0                                               |

The rows follow `buffoffset.dbss` order exactly, which is neither ascending nor
descending by ID (the first row is buff 4100000000 on client 3464, 48879 on
3458).

### Buff Row (32 bytes)

Fields are unaligned. The Source column names the `buff.dbss` field that holds
the same value in every row, when one does.

| Offset  | Type     | Field           | Source (`buff.dbss`)    | Notes                                                                          |
| ------- | -------- | --------------- | ----------------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u32      | buff_id         | `buff_id`               | Unique; 43 to 65,528 and five IDs from 700,000 to 4,100,000,000                |
| `+0x04` | u8       | need_equip_type | stats `need_equip_type` | `0` in every row but buff 2078 (`13`)                                          |
| `+0x05` | bytes[2] | unknown_05      |                         | Always `0`                                                                     |
| `+0x07` | u8       | unknown_07      | stats `+0x7D`           | `0` in every row but buff 2078 (`1`)                                           |
| `+0x08` | u8       | unknown_08      | stats `+0x7D`           | Same values as `unknown_07`; not stats `+0x7E`, see Notes                      |
| `+0x09` | u8       | unknown_09      | stats `unknown_7f`      | Always `2`                                                                     |
| `+0x0A` | u8       | unknown_0a      |                         | Always `0`                                                                     |
| `+0x0B` | u8       | need_equip_slot | stats `need_equip_slot` | `46` (no slot) in every row but buff 2078 (`6`)                                |
| `+0x0C` | u8       | unknown_0c      | stats `unknown_82`      | `2` in every row but buff 2078 (`1`)                                           |
| `+0x0D` | u32      | effect_name_ref | `effect_name`           | String table index; 187 distinct, `0` (`"0"`) in 39,527 rows, `1` (`""`) in 52 |
| `+0x11` | u8       | is_debuff       | stats `is_debuff`       | `1` in 14,432 rows                                                             |
| `+0x12` | u8       | unknown_12      |                         | Always `1`; no `buff.dbss` byte matches, see Open Questions                    |
| `+0x13` | bytes[3] | unknown_13      |                         | Always `0`                                                                     |
| `+0x16` | u8       | remove_on_dead  | stats `remove_on_dead`  | `1` in 33,944 rows                                                             |
| `+0x17` | u8       | is_shown        | `is_shown`              | `1` in 12,766 rows                                                             |
| `+0x18` | u32      | unknown_18      | tail `unknown_02`       | `0` in 25,701 rows, `1` in 14,420, `2` in 4,562                                |
| `+0x1C` | u32      | icon_ref        | `icon_path`             | String table index; `1` (the empty string) in 29,357 rows                      |

### String Table (variable: 4 bytes + strings)

1,235 strings on client 3464, all distinct and all referenced. `effect_name_ref`
and `icon_ref` index the same table and share only the empty string: index 0
is `"0"`, index 1 is `""`, and every other entry is either an `effect_name`
value or an icon path.

| Offset  | Type               | Field        | Notes                |
| ------- | ------------------ | ------------ | -------------------- |
| `+0x00` | u32                | string_count | 1,235 on client 3464 |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries  |

## Layout 1

Before client 3464 `buff_id` was a u16 and every later field sat 2 bytes
earlier. Only the Buff Row differs from Layout 2. Field names keep Layout
2's offsets, so `unknown_05` sits at `+0x03` here. The parser reads only
Layout 2.

### Buff Row (30 bytes)

| Offset  | Type     | Field           | Notes |
| ------- | -------- | --------------- | ----- |
| `+0x00` | u16      | buff_id         |       |
| `+0x02` | u8       | need_equip_type |       |
| `+0x03` | bytes[2] | unknown_05      |       |
| `+0x05` | u8       | unknown_07      |       |
| `+0x06` | u8       | unknown_08      |       |
| `+0x07` | u8       | unknown_09      |       |
| `+0x08` | u8       | unknown_0a      |       |
| `+0x09` | u8       | need_equip_slot |       |
| `+0x0A` | u8       | unknown_0c      |       |
| `+0x0B` | u32      | effect_name_ref |       |
| `+0x0F` | u8       | is_debuff       |       |
| `+0x10` | u8       | unknown_12      |       |
| `+0x11` | bytes[3] | unknown_13      |       |
| `+0x14` | u8       | remove_on_dead  |       |
| `+0x15` | u8       | is_shown        |       |
| `+0x16` | u32      | unknown_18      |       |
| `+0x1A` | u32      | icon_ref        |       |

## Notes

- Checked against `buff.dbss` on client 3464: all 44,683 IDs have a record
  there, and `effect_name_ref`, `icon_ref`, `is_shown` and every field with a
  Source match the record in all 44,683 rows.
- The app builds its buff icon lookup index (`IndexKind.BUFF_ICON`, read
  through `IconKind.BUFF`) from this file: it gives the same paths as
  `buff.dbss` from a 1.4 MB fixed-row file, without walking the 12 MB of
  variable-length records.
- Icon paths follow the `buff.dbss` conventions: 15,282 rows set one, over
  1,043 stored strings that become 1,017 paths once lowercased with `\`
  turned into `/` (35 stored strings use backslashes). 206 rows store the
  placeholder `UNKNOWN`, and three double a separator
  (`04_PC_Skill//04_Debuff`); collapsing it finds their file. Resolve under
  `ui_texture/icon/`, as for `buff.dbss`. On client 3458, 14,884 of the
  15,076 real icons exist; the other 192 rows point at 22 paths the client
  does not ship.
- The icon is not unique to a headline buff: the hidden effects that follow
  one often store the same path (all of 48717 to 48734, the three Adventure's
  Boon runs, store `SilverBless.dds`), while only the headline has `is_shown`.
- Buff 2078 (`[장착용] 두건 효과 : 정체 감추기`, "equip: hood effect, hide
  identity") is the only row where `+0x04` to `+0x0C` differ from the
  constants, and its stats bytes `+0x7A` to `+0x82` read
  `0d 00 00 01 01 02 00 06 01`, the same nine bytes as this row: the
  `_needEquipType` copy of an `itemenchant.dbss` equip type (see the
  `buff.dbss` Field Names). On every other buff stats `+0x7E` (`unknown_7e`) is
  `1` in 44,588 rows while `+0x08` here stays `0`, so `+0x08` is not that
  byte. Only per-byte matches are claimed above.
- `buff.dbss` fields with no copy here: `name`, `buff_level`, `group`,
  `condition_type`, `effect_type`, the parameters, `duration_ms`,
  `apply_rate`, `description` and `stacking_category`.
- [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  mentions the file only as a 30-byte PABR projection over the buff keys (the
  pre-3464 row size) with
  an icon string-table reference; it gives no row layout.

## Field Names

The named fields take the names of the `buff.dbss` fields they copy, which come from the 2016 `gc::BuffStaticStatus` and the `Buff_Table` of a private server on client 519 ([buff.dbss Field Names](buff_dbss.md#field-names)). `unknown_07`, `unknown_08`, `unknown_09` and `unknown_0c` sit in the `_isExtractable`, `_isUseAvatarMesh`, `_rangeType` and `_enchantFailType` places of the `_needEquipType` copy; no server column holds them and the matching `itemenchant.dbss` header bytes have no name either. `unknown_18` copies `buff.dbss` tail `unknown_02`, which matches no server column.

## Open Questions

### What does `unknown_12` hold?

It is `1` in every row and matches no `buff.dbss` byte in all rows. The
closest are stats `param_1_set` (`1` in 44,525 rows) and `unknown_7e` (`1` in 44,550),
so it may be one of those with the exceptions dropped, or a constant of the
compact format.
