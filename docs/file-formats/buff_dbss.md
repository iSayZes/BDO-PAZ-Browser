# `buff.dbss` Format

## Purpose

The master buff table: every buff and debuff the game can apply, from potions,
food and scrolls to title effects, furniture, boss mechanics and monster-only
debuffs. Each record carries an internal Korean name, a level, an effect type,
ten numeric parameters, a duration, an optional icon and an optional Korean
description whose English form lives in LOC type 5.

Example:

```text
buff_id 48830
  name         수렵 숙련도 +70 3시간   (internal label, "Hunting Mastery +70 3 hours")
  icon         New_Icon/04_PC_Skill/03_Buff/HuntingBuff.dds
  description  Hunting Mastery +70      (LOC str_type=5, str_id1=48830)
```

## Graph

### Tags

- file format
- dbss
- buff
- icon

### Connections

- [languagedata_en.loc](languagedata_loc.md), English buff descriptions (str_type=5, str_id1=buff_id)
- [titlebufflist.dbss](titlebufflist_dbss.md), title effects, a separate buff-like table keyed 0 to 17

---

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `buffoffset.dbss`     | Required | `buff_id → (offset, size)` index into this file   |
| `languagedata_en.loc` | Optional | English descriptions, `str_type=5`                |

`buffsimply.bss` holds the same 44,609 buff IDs in fixed 30-byte rows followed
by an icon path string table. It is not needed to read this file and is not yet
documented.

All multi-byte values are little-endian.

---

## File Layout

| Offset  | Type | Field   | Notes                                              |
| ------- | ---- | ------- | -------------------------------------------------- |
| `+0x00` | u32  | count   | Number of records; observed `44609`                |
| `+0x04` | ...  | records | Variable-length records, located via the offset file |

The records tile the file exactly: sorted by offset, each ends where the next
begins, and the last ends at EOF.

---

## Record Structure

A record is a chain of fixed blocks and length-prefixed strings. The strings use
the shared 8-byte prefix (u32 length, u32 zero, no terminator); UTF-16 lengths
count characters, ASCII lengths count bytes.

| Order | Type               | Field       | Notes                                                    |
| ----- | ------------------ | ----------- | -------------------------------------------------------- |
| 1     | u16                | buff_id     | Always equals the offset row's `buff_id`                 |
| 2     | prefixed UTF-16    | name        | Internal Korean label; no LOC counterpart                |
| 3     | 133 bytes          | stats block | See Stats Block below                                    |
| 4     | prefixed UTF-16    | unknown_str | Short digit text, `"0"` in 39,455 rows; 186 distinct     |
| 5     | prefixed ASCII     | icon_path   | Relative to `ui_texture/icon/`; see Notes                |
| 6     | u8                 | is_shown    | See Notes; `1` in 12,746 rows                            |
| 7     | u32                | apply_rate  | `1000000` (100%) in 44,427 rows; per-million scale       |
| 8     | prefixed UTF-16    | description | Korean, with `<PAColor>` tags; empty in 30,290 rows      |
| 9     | 27 bytes           | tail block  | See Tail Block below                                     |

Record sizes range from 203 to 2,198 bytes, median 237.

### Stats Block (133 bytes)

Offsets are relative to the end of the name string.

| Offset  | Type    | Field           | Notes                                                                 |
| ------- | ------- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u32     | buff_level      | 1 to 999; `1` in 32,071 rows. Staged buffs count up, e.g. boss stages 1 to 10 |
| `+0x04` | u32     | unknown_04      | `0` in 28,301 rows; otherwise runs sequentially alongside `buff_id`   |
| `+0x08` | u8      | effect_type     | 173 distinct values; see Enum Values                                  |
| `+0x09` | u8[10]  | flag_09..flag_12 | Each byte is `0` or `1`                                             |
| `+0x13` | i64[10] | param_1..param_10 | Effect parameters; meaning depends on `effect_type`. Percentages use a per-million scale (`100000` = 10%) |
| `+0x63` | u8      | flag_63         | `0` or `1`                                                            |
| `+0x64` | u8      | flag_64         | `0` or `1`                                                            |
| `+0x65` | u16     | reserved        | Always `0`                                                            |
| `+0x67` | u8      | flag_67         | `0` or `1`                                                            |
| `+0x68` | u32     | duration_ms     | `0` in 30,016 rows; max `86400000` (24 h). `3600000` = 60 min        |
| `+0x6C` | u32     | unknown_6c      | Millisecond-like (1000, 2000, 3000); only on periodic effects        |
| `+0x70` | u8[14]  | reserved        | `0` in every row but one                                              |
| `+0x7E` | u8      | flag_7e         | `1` in 44,514 rows                                                    |
| `+0x7F` | u8      | unknown_7f      | Always `2`                                                            |
| `+0x80` | u8      | reserved        | Always `0`                                                            |
| `+0x81` | u8      | unknown_81      | `46` in every row but one                                             |
| `+0x82` | u8      | unknown_82      | `2` in every row but one                                              |
| `+0x83` | u8      | flag_83         | `0` or `1`                                                            |
| `+0x84` | u8      | flag_84         | `0` or `1`                                                            |

### Tail Block (27 bytes)

Offsets are relative to the end of the description string. Mostly zero.

| Offset  | Type | Field       | Notes                                        |
| ------- | ---- | ----------- | -------------------------------------------- |
| `+0x00` | u8   | flag_00     | `1` in 34 rows                               |
| `+0x01` | u8   | flag_01     | `1` in 6 rows                                |
| `+0x02` | u32  | unknown_02  | `0`, `1` or `2`                              |
| `+0x06` | u8   | unknown_06  | `3` in 44,575 rows                           |
| `+0x07` | i32  | unknown_07  | `0`, `1000000` or `-1000000`                 |
| `+0x0B` | u8[12] | reserved  | Always `0`                                   |
| `+0x17` | u8   | flag_17     | `1` in 221 rows                              |
| `+0x18` | u8   | unknown_18  | 61 distinct values                           |
| `+0x19` | u8   | flag_19     | `1` in 2,066 rows                            |
| `+0x1A` | u8   | unknown_1a  | `6` in 18,895 rows, else `0` or `1`          |

---

## `buffoffset.dbss`

`PABR` index into `buff.dbss`, the same layout as `characterstaticoffset.dbss`
except that `data_offset` points *at* the inline `buff_id` and `size` includes
it.

### Header (8 bytes)

| Offset  | Type  | Field | Notes                                      |
| ------- | ----- | ----- | ------------------------------------------ |
| `+0x00` | u8[4] | magic | ASCII `PABR`                               |
| `+0x04` | u32   | count | Observed `44609`, matching `buff.dbss`     |

### Index Row (10 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                           |
| ------- | ---- | ----------- | ----------------------------------------------- |
| `+0x00` | u16  | buff_id     | Unique; 43 to 65,528                            |
| `+0x02` | u32  | data_offset | Absolute offset of the record in `buff.dbss`    |
| `+0x06` | u32  | size        | Record size in bytes, including the `buff_id`   |

### Trailer (12 bytes)

| Offset  | Type | Value  | Notes                                         |
| ------- | ---- | ------ | --------------------------------------------- |
| `+0x00` | u32  | `0`    |                                               |
| `+0x04` | u32  | varies | End offset of the index rows (`446098`)       |
| `+0x08` | u32  | `0`    |                                               |

---

## Enum Values

`effect_type` (stats block `+0x08`). Labels are inferred from the internal names
of the buffs that use each value.

| Value | Rows  | Observed buffs                                     | Parameters, where confirmed                          |
| ----- | ----- | -------------------------------------------------- | ---------------------------------------------------- |
| 1     | 1,662 | On-hit effects (HP recovery on hit, back attack)   |                                                      |
| 2     | 443   | Max HP                                             | `param_1` = amount                                   |
| 18    | 3,386 | Summons                                            |                                                      |
| 25    | 1,597 | Combat, skill and life EXP gain                    | `param_1` = bonus per million; `param_2` 0 combat, 1 skill, 2 life |
| 38    | 5,683 | Story and record unlocks                           |                                                      |
| 39    | 1,732 | All AP, positive or negative                       | `param_1` = `3`, `param_2` = amount                  |
| 40    | 870   | All Accuracy                                       | `param_1` = `3`, `param_2` = amount                  |
| 43    | 1,730 | All Damage Reduction                               | `param_1` = `3`, `param_2` = amount                  |
| 45    | 8,286 | Damage multipliers (monster attack %, pure damage) |                                                      |
| 46    | 1,831 | Species extra AP                                   |                                                      |
| 49    | 1,378 | Crowd-control resistance                           |                                                      |
| 58    | 1,132 | Elixirs, herbal teas, sequence check buffs         |                                                      |

---

## Suggested UI Layout

| Column      | Type | Notes                                                               |
| ----------- | ---- | ------------------------------------------------------------------- |
| Buff ID     | num  | `buff_id`; right-aligned                                            |
| Icon        | text | `icon_path`, resolved under `ui_texture/icon/`; dash when empty     |
| Title       | text | Coloured first line of the description when more lines follow; dash otherwise |
| Internal Name | text | Korean `name`; labelled internal because no English form exists   |
| Description | text | LOC `str_type=5`, `str_id1=buff_id`; falls back to the inline Korean description, `<null>` counts as empty |
| Level       | num  | `buff_level`                                                        |
| Effect Type | num  | `effect_type`                                                       |
| Duration    | text | `duration_ms` formatted as h/min/s; dash when `0`                   |
| Param 1     | num  | `param_1`                                                           |
| Param 2     | num  | `param_2`                                                           |
| Param 3     | num  | `param_3`                                                           |

---

## Notes

- `icon_path` is set in 15,272 records over 1,017 distinct paths. 221 of those
  hold the literal placeholder `UNKNOWN`, and a few use backslash separators.
  Resolve by lowercasing, normalizing `\` to `/` and prefixing
  `ui_texture/icon/`, e.g. `ui_texture/icon/new_icon/04_pc_skill/03_buff/huntingbuff.dds`.
- `is_shown` looks like a "visible in the buff bar" flag: 11,882 of its 12,746
  set rows have both an icon and a description, against 312 of the 31,863
  clear rows.
- The buff name has no English form anywhere in LOC. Of 13,658 names with at
  least two numbers, the best match under any type and sub-field keyed by
  `buff_id` is 48 of 3,522 in type 10, which is chance. Names are internal
  labels such as `테스트용 토레스 일꾼` (test Torres worker); the game shows
  players only the description.
- The inline Korean description matches LOC type 5 by content; numbers agree
  in every checked row apart from thousands separators.
- LOC type 10 was once assumed to be buff text keyed by `buff_id`. It is not:
  only half of the IDs overlap and the text disagrees (see the LOC doc).
- `unknown_04` is not a LOC key: 8827 resolves to an unrelated item in
  type 0 and a skill in type 10. Within a buff group it increases by one per
  buff (9056 to 9061 below).
- One buff record holds one effect, so a consumable with several effects
  applies a run of consecutive buffs. Only the first carries the description,
  the icon and `is_shown`, and its description opens with the display title.
  Example: item 761880, `[Blessing] Adventure's Boon (120 min)` (LOC type 0),
  applies buffs 48723 to 48728:

  | buff_id | Effect                   | effect_type | param_1  | param_2 |
  | ------- | ------------------------ | ----------- | -------- | ------- |
  | 48723   | All AP +8                | 39          | 3        | 8       |
  | 48724   | All Accuracy +8          | 40          | 3        | 8       |
  | 48725   | All Damage Reduction +8  | 43          | 3        | 8       |
  | 48726   | Max HP +150              | 2           | 150      | 0       |
  | 48727   | Combat EXP +15%          | 25          | 150000   | 0       |
  | 48728   | Skill EXP +15%           | 25          | 150000   | 1       |

  The 60 and 300 minute variants sit either side, at 48717 and 48729.
- Only headline buffs have a display name, and it is not a field: their
  description opens with it on a coloured line of its own
  (`<PAColor0xffe9bd23>[Blessing] Adventure's Boon<PAOldColor>`), then the
  effects. Against LOC type 5 the buffs split as follows:

  | Type 5 text                          | Buffs  | First line                                  |
  | ------------------------------------ | ------ | ------------------------------------------- |
  | None or `<null>`                     | 30,488 | Nothing; hidden and group-member buffs      |
  | One line                             | 11,846 | The effect itself, e.g. `Mount EXP +3%`     |
  | Coloured first line, then effects    | 2,038  | The title; 2,020 of these have `is_shown`   |
  | Several lines, no colour             | 237    | Sometimes a title, sometimes an effect list |

  421 titles equal an item name once its `(120 min)`-style suffix is dropped.
  A few are flavour lines rather than names
  (`Time in Sycraia surges forward.`). The inline Korean description uses the
  same convention, so the title survives when LOC is not loaded.
- The parameters are the only reliable effect value; the name and the
  description can each be stale. Of 11,766 buffs whose name and description
  both hold numbers, about 500 disagree beyond a change of scale, and either
  side can be the outdated one:

  | buff_id | Name              | Description | Applied parameter | Matches     |
  | ------- | ----------------- | ----------- | ----------------- | ----------- |
  | 48866   | Life EXP +15%     | +3%         | `150000` (15%)    | name        |
  | 48321   | All Evasion -6    | -8          | `-6`              | name        |
  | 48661   | HP Regen +75      | +50         | `50`              | description |
  | 48766   | Olvia pass (2594.61) | Trade EXP +53630 | `129731`  | neither     |

  The inline Korean description and LOC type 5 always agree with each other,
  so this is drift in the game data, not a parsing or translation error.
- Item IDs do not appear in this file: 761880 is not stored anywhere in it as
  a u32 or i64, so the item-to-buff link lives in another table.

---

## Open Questions

### What does `unknown_str` hold?

A short UTF-16 string of digits (`"0"`, `"90"`, `"158"`), and occasionally `*`.
It could be a group or stacking key stored as text, but no table has been
matched against it.

### What does `unknown_6c` measure?

It is only set on periodic effects such as bleeds and heal-over-time, and holds
millisecond-like values. It is not the stated tick interval: a buff named
"every 3 seconds" stores `2000`.

### What do the ten parameters mean per effect type?

`param_1` through `param_10` change meaning with `effect_type`. Types 2, 25,
39, 40 and 43 are confirmed (see Enum Values); the rest have not been worked
out. For 39, 40 and 43 `param_1` is always `3`, possibly a mask selecting
melee, ranged and magic together.

### Which table links items to their buffs?

Consumable items such as 761880 apply buff groups, but the item ID is not in
`buff.dbss`. The link is likely in an item table or runs through a skill the
item triggers.
