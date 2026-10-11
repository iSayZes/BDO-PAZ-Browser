# `commonlifestatdata.bss` Format

## Purpose

The mastery a Gathering or Processing level gives: one f32 per life level,
from level 1 (Beginner 1) to 180 (Guru 100). The Life Skill tab shows it as
"Mastery N" next to the Gathering and Processing levels.

```text
commonlifestatdata.bss, client 3464:
  Beginner 1 0, Beginner 2 10, Apprentice 1 60, Artisan 1 355,
  Guru 1 555, Guru 50 800, Guru 100 800
```

The file is self-contained. All multi-byte values are little-endian.

## File Layout

The PABR layout of [`blizzardregioninfo.bss`](blizzardregioninfo_bss.md)
without a row count: the values start right after the magic and run up to
the empty string table.

| Offset   | Type    | Field        | Notes                                              |
| -------- | ------- | ------------ | -------------------------------------------------- |
| `+0x00`  | char[4] | magic        | ASCII `PABR`                                       |
| `+0x04`  | f32[]   | mastery      | One value per level from level 1; 180 on client 3464 |
| after    | u32     | string_count | Always `0`                                         |
| EOF - 8  | u32     | table_start  | Offset of `string_count`, where the values end     |
| EOF - 4  | u32     | zero         | Always `0`                                         |

## Record Structure

### Level Value (4 bytes)

| Offset  | Type | Field   | Notes                                       |
| ------- | ---- | ------- | ------------------------------------------- |
| `+0x00` | f32  | mastery | Mastery at level `index + 1`, a whole number |

The level is not stored. Value `n` (from 0) belongs to level `n + 1`. Under
that reading the step between values changes where a rank starts; read as
level `n`, it would change at the last level of a rank. On client 3464
Beginner 1 is `0` and Beginner 2 `10`, then the values rise by 5 per level
to Beginner 10 (`50`), by 10 from Apprentice 1 (`60`) to Professional 10
(`350`), by 5 from Artisan 1 (`355`) to Guru 50 (`800`), and stay at `800`
up to Guru 100. The 180 values match the max level 180 of Gathering and
Processing in [`lifeexpmaxlevel.bss`](lifeexpmaxlevel_bss.md). The first
column of [`traininglevelskillstat.bss`](traininglevelskillstat_bss.md)
changes its step at every rank start under the same reading.

`PaGlobal_CharInfoLife_All:update` in `panel_characterinfo_life_all_1.luac`
shows `ToClient_GetCommonLifeStat(idx)` as `LUA_CHARINFO_COMMONLIFESTAT_SHORT`
("Mastery") for `LifeExperienceType.gather` and `.manufacture` only; the
other life skills show `getLifeStat(idx, 1)` there instead. The getter name
matches the file name. The per-type masteries next to it
(`getLifeStat(idx, subType)`) select the rows of
[`collectingstatdata.bss` and `manufacturingstat.bss`](masterystatdata_bss.md).

## Suggested UI Layout

| Column  | Type | Notes                                                           |
| ------- | ---- | --------------------------------------------------------------- |
| Level   | num  | `level`, the raw life level                                     |
| Rank    | text | `Guru 12` for level 92, from the client rank names (see [`lifeexp.dbss`](lifeexp_dbss.md)) |
| Mastery | num  | `mastery`, shown as `355`                                       |

## Notes

- The handler is `_bss/commonlifestatdata/`; the rank text comes from
  `rank_text` in `_dbss/lifeexp/labels.py`.
- [`traininglevelskillstat.bss`](traininglevelskillstat_bss.md) has the same
  level-indexed layout with two u32 rates per level; both handlers read the
  entries with `parse_level_entries` in `_bss/commonlifestatdata/parser.py`.
  Its Training tooltip at Artisan 7 (level 47) matches entry 46, which
  confirms the entry `n` = level `n + 1` reading for this layout.
