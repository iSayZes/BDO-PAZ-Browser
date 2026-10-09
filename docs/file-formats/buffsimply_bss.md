# `buffsimply.bss` Format

## Purpose

A compact copy of [`buff.dbss`](buff_dbss.md): one fixed 32-byte row per buff
with the buff ID, the icon path and `unknown_str` as indices into a shared
string table, `is_shown` and a few flag bytes. It holds no name, parameters,
duration or description, so it covers what the buff bar needs to draw a buff
and nothing about its effect.

Example:

```text
buff_id 48830
  icon_ref -> New_Icon/04_PC_Skill/03_Buff/HuntingBuff.dds
  is_shown 1
```

## Companion Files

| File                  | Required | Role                                                        |
| --------------------- | -------- | ----------------------------------------------------------- |
| `buff.dbss`           | Optional | Full buff records; every row here has a record there        |
| `languagedata_en.loc` | Optional | English descriptions, LOC type 5 keyed by `buff_id`         |

All multi-byte values are little-endian.

## File Layout

The shared PABR string table layout of `npcsimply.bss` and
`plantexchangegroup.bss` (`_common/pabr_strings.py`).

| Offset             | Type     | Field        | Notes                                                  |
| ------------------ | -------- | ------------ | ------------------------------------------------------ |
| `+0x00`            | char[4]  | magic        | ASCII `PABR`                                           |
| `+0x04`            | u32      | count        | Number of rows; 44,683 on client 3464, equal to the `buff.dbss` count |
| `+0x08`            | row[]    | rows         | 32-byte rows repeated `count` times                    |
| `8 + count * 32`   | table    | string_table | u32 count, then `count` x (u8 is_wide, u32 byte length, payload) |
| EOF - 8            | u32      | table_start  | Offset of the string table, where the rows end         |
| EOF - 4            | u32      | zero         | Always 0                                               |

The rows follow `buffoffset.dbss` order exactly, which is neither ascending nor
descending by ID (the first row is buff 4100000000 on client 3464, 48879 on
3458).

## Record Structure

### Buff Row (32 bytes, repeated `count` times)

Fields are unaligned. The Source column names the `buff.dbss` field that holds
the same value in every row, when one does.

| Offset  | Type  | Field           | Source (`buff.dbss`)   | Notes                                                        |
| ------- | ----- | --------------- | ---------------------- | ------------------------------------------------------------ |
| `+0x00` | u32   | buff_id         | `buff_id`              | Unique; 43 to 65,528 and five IDs from 700,000 to 4,100,000,000; a u16 before client 3464 |
| `+0x04` | u8    | unknown_04      | stats `+0x7A`          | `0` in every row but buff 2078 (`13`)                        |
| `+0x05` | u8[2] | reserved        |                        | Always `0`                                                   |
| `+0x07` | u8    | unknown_07      | stats `+0x7D`          | `0` in every row but buff 2078 (`1`)                         |
| `+0x08` | u8    | unknown_08      | stats `+0x7D`          | Same values as `unknown_07`; not stats `+0x7E`, see Notes    |
| `+0x09` | u8    | unknown_09      | stats `unknown_7f`     | Always `2`                                                   |
| `+0x0A` | u8    | reserved        |                        | Always `0`                                                   |
| `+0x0B` | u8    | unknown_0b      | stats `unknown_81`     | `46` in every row but buff 2078 (`6`)                        |
| `+0x0C` | u8    | unknown_0c      | stats `unknown_82`     | `2` in every row but buff 2078 (`1`)                         |
| `+0x0D` | u32   | unknown_str_ref | `unknown_str`          | String table index; 187 distinct, `0` (`"0"`) in 39,527 rows, `1` (`""`) in 52 |
| `+0x11` | u8    | unknown_11      | stats `flag_63`        | `1` in 14,432 rows                                           |
| `+0x12` | u8    | unknown_12      |                        | Always `1`; no `buff.dbss` byte matches, see Open Questions  |
| `+0x13` | u8[3] | reserved        |                        | Always `0`                                                   |
| `+0x16` | u8    | unknown_16      | stats `flag_83`        | `1` in 33,944 rows                                           |
| `+0x17` | u8    | is_shown        | `is_shown`             | `1` in 12,766 rows                                           |
| `+0x18` | u32   | unknown_18      | tail `unknown_02`      | `0` in 25,701 rows, `1` in 14,420, `2` in 4,562               |
| `+0x1C` | u32   | icon_ref        | `icon_path`            | String table index; `1` (the empty string) in 29,357 rows    |

Before client 3464 `buff_id` was a u16 and every later field sat 2 bytes
earlier, in 30-byte rows. The parser reads only the 32-byte layout.

### String Table

1,235 strings on client 3464, all distinct and all referenced. `unknown_str_ref`
and `icon_ref` index the same table and share only the empty string: index 0
is `"0"`, index 1 is `""`, and every other entry is either an `unknown_str`
value or an icon path.

## Suggested UI Layout

| Column      | Type | Notes                                                                        |
| ----------- | ---- | ---------------------------------------------------------------------------- |
| Buff ID     | num  | `buff_id`; right-aligned                                                     |
| Icon        | text | `icon_ref`, resolved like `buff.dbss` `icon_path`; dash when empty or `UNKNOWN` |
| Description | text | LOC type 5, `str_id1` = `buff_id`, `<null>` counts as empty; dash without LOC, since the file holds no inline text |
| Shown       | text | `is_shown` as Yes / No                                                       |

The `unknown_*` fields and `unknown_str_ref` stay on the record but out of the
table.

## Notes

- Checked against `buff.dbss` on client 3464: all 44,683 IDs have a record
  there, and `unknown_str_ref`, `icon_ref`, `is_shown` and every field with a
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
  `0d 00 00 01 01 02 00 06 01`, the same nine bytes as this row. That looks
  like a straight copy, but on every other buff stats `+0x7E` (`flag_7e`) is
  `1` in 44,550 rows while `+0x08` here stays `0`, so `+0x08` is not that
  byte. Only per-byte matches are claimed above.
- `buff.dbss` fields with no copy here: `name`, `buff_level`, `group`,
  `condition_type`, `effect_type`, the parameters, `duration_ms`,
  `apply_rate`, `description` and `stacking_category`.
- [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  mentions the file only as a 30-byte PABR projection over the buff keys (the
  pre-3464 row size) with
  an icon string-table reference; it gives no row layout.

## Open Questions

### What does `unknown_12` hold?

It is `1` in every row and matches no `buff.dbss` byte in all rows. The
closest are stats `flag_09` (`1` in 44,525 rows) and `flag_7e` (`1` in 44,550),
so it may be one of those with the exceptions dropped, or a constant of the
compact format.
