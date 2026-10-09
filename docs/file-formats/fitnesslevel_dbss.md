# `fitnesslevel.dbss` Format

## Purpose

Level tables of the three fitness stats in the character window: Breath, Strength and Health. Each row gives the EXP to the next level and the total bonus the fitness stat grants at that level (max Stamina for Breath, weight limit for Strength, max HP and max MP/WP/SP for Health). Companion `fitnessleveloffset.dbss` lists where every row sits.

Example:

```text
Breath    Lv 30   EXP 20,000   Max Stamina +500
Strength  Lv 30   EXP 10,000   Weight Limit +40 LT
Health    Lv 30   EXP 5,000    Max HP +290, Max MP/WP/SP +200
```

## Companion Files

| File                      | Required | Role                                                   |
| ------------------------- | -------- | ------------------------------------------------------ |
| `fitnessleveloffset.dbss` | Required | `(fitness type, level) -> (offset, size)` of every row |

All multi-byte values are little-endian.

## File Layout

| Offset  | Type    | Field      | Notes                                       |
| ------- | ------- | ---------- | ------------------------------------------- |
| `+0x00` | u32     | type_count | Number of fitness blocks (observed: 3)      |
| `+0x04` | block[] | blocks     | `type_count` blocks, one per fitness type   |

### Block (repeated `type_count` times)

| Offset  | Type      | Field       | Notes                                |
| ------- | --------- | ----------- | ------------------------------------ |
| `+0x00` | u32       | level_count | Rows in this block (observed: 51)    |
| `+0x04` | row[]     | rows        | `level_count` rows of 29 bytes       |

The blocks fill the file exactly: 4 + 3 x (4 + 51 x 29) = 4,453 bytes on client 3458.

## Record Structure

### Level Row (29 bytes)

| Offset  | Type | Field        | Notes                                                                                          |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------------------------- |
| `+0x00` | u8   | fitness_type | `0` Breath, `1` Strength, `2` Health; equals the block index                                   |
| `+0x01` | u32  | level        | `0` to `50`, ascending inside a block                                                          |
| `+0x05` | u64  | exp          | EXP needed to go from this level to the next, read like `lifeexp.dbss` (Notes); `0` on level 0, rising to 5,500,000 (Breath, Strength) and 2,750,000 (Health) on level 50 |
| `+0x0D` | f32  | max_stamina  | Breath total: max Stamina bonus; `0` in Strength and Health rows                               |
| `+0x11` | f32  | weight_limit | Strength total: weight limit bonus in 1/10,000 LT (`400000` is 40 LT); `0` elsewhere          |
| `+0x15` | f32  | max_hp       | Health total: max HP bonus; `0` elsewhere                                                      |
| `+0x19` | f32  | max_mp       | Health total: max MP/WP/SP bonus (the class's combat resource); `0` elsewhere                  |

Every row carries all four stat floats; only the ones of its own fitness type are non-zero. All stored floats are whole numbers except `weight_limit`, whose LT value can end in `.5` (Strength level 29 is 385,000, 38.5 LT). Levels 0 and 1 hold no bonus; level 2 is the first that grants one.

A row's totals are the bonus at that row's own level, confirmed in game on 2026-10-06: the tooltips at Breath Lv.37, Strength Lv.31 and Health Lv.33 read `Max Stamina +570`, `Weight Limit +42 LT` and `Max HP +320`, the values of rows 37, 31 and 33.

## Enum Values

### Fitness Type

| ID  | Name     | Stat in the row                     |
| --- | -------- | ----------------------------------- |
| 0   | Breath   | `max_stamina`                       |
| 1   | Strength | `weight_limit`                      |
| 2   | Health   | `max_hp`, `max_mp`                  |

The order matches the client's `_ENUM_FITNESS` in `panel_characterinfo_basic_all.luac` (`BREATH`, `POWER`, then Health), whose hover handlers pass `0`, `1` and `2` for the Breath, Strength and Health texts. The stat per type matches the client's tooltip strings `Breath: Max Stamina +`, `Strength: Weight Limit +` and `Health: Max HP +{hpIncrease}, Max {mpTypeName} +{mpIncrease}`.

## fitnessleveloffset.dbss

Index into `fitnesslevel.dbss`, with the same block shape as the main file but no leading type count.

### Block (repeated until the end of the file)

| Offset  | Type  | Field       | Notes                                 |
| ------- | ----- | ----------- | ------------------------------------- |
| `+0x00` | u32   | level_count | Rows in this block (observed: 51)     |
| `+0x04` | row[] | rows        | `level_count` rows of 12 bytes        |

The block index is the fitness type; the file stores no type field. 3 x (4 + 51 x 12) = 1,848 bytes on client 3458.

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                    |
| ------- | ---- | ----------- | ------------------------------------------------------------------------ |
| `+0x00` | u32  | level       | Level of the row it points at                                            |
| `+0x04` | u32  | data_offset | Absolute byte offset of the 29-byte row in `fitnesslevel.dbss`           |
| `+0x08` | u32  | data_size   | Always 29                                                                |

The first Breath row sits at `0x08`, after the type count and Breath's level count; each later block starts 4 bytes past the previous block's last row, skipping that block's level count. The parser reads the main file through these rows and checks that each row's `fitness_type` and `level` match the offset row's block and key.

## Suggested UI Layout

### fitnesslevel.dbss

| Column        | Type | Notes                                                          |
| ------------- | ---- | -------------------------------------------------------------- |
| Fitness       | text | Breath, Strength or Health; sorts by `fitness_type`            |
| Level         | num  | `level`                                                        |
| EXP to Next Level | num | `exp`                                                        |
| Max Stamina   | num  | `max_stamina`                                                  |
| Weight Limit  | num  | `weight_limit` / 10,000, shown as `40 LT`                      |
| Max HP        | num  | `max_hp`                                                       |
| Max MP/WP/SP  | num  | `max_mp`                                                       |

### fitnessleveloffset.dbss

| Column      | Type | Notes                          |
| ----------- | ---- | ------------------------------ |
| Fitness     | num  | Block index (`fitness_type`)   |
| Level       | num  | `level`                        |
| Data Offset | num  | `data_offset`, as hex          |
| Data Size   | num  | `data_size`                    |

## Notes

- `fitnessmaxlevel.bss` stores the max level of each fitness type, `50` for all three on client 3464, the top row of every block here; see [fitnessmaxlevel](fitnessmaxlevel_bss.md).
- Level 30 is the soft cap. No file stores it, but on client 3464 the EXP to the next level jumps between rows 30 and 31 in every block: Breath 20,000 to 50,000, Strength 10,000 to 30,000, Health 5,000 to 20,000. Up to row 30 the step between rows is at most 3,500.
- The client reads a fitness level and its EXP through `getFitnessLevel`, `getCurrFitnessExperiencePoint` and `getDemandFItnessExperiencePoint` (`panel_characterinfo_basic_all_3.luac`); the bonus shown in the tooltip comes from `ToClient_GetFitnessLevelStatus(type)`.
- The four stat floats are cumulative totals, not per-level increments: every column only rises with the level (Breath 25, 50, 75 up to 800; Strength 2 LT up to 80 LT; Health HP 10 up to 490 and MP/WP/SP 10 up to 300).
- Breath and Strength have the same EXP from level 41 up and Strength needs less than Breath on levels 1 to 40.
- Row direction: read like [lifeexp](lifeexp_dbss.md), where a packet capture confirmed that the row of level N is the EXP to go from N to N + 1. Both tables use the same block shape and the client draws both bars as current / demand (`getCurrFitnessExperiencePoint` / `getDemandFItnessExperiencePoint` here, the life skill pair there). Row 0 (`0` EXP, no bonus) is then an unused placeholder, as characters start every fitness stat at Lv.1. No fitness capture yet; a fitness EXP message whose bar matches row N + 1, or a fresh character at Breath Lv.0, would flip it.
