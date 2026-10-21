# `arshasetlostregion.bss` Format

## Purpose

The stages of the Arena of Arsha shrinking zone, the game rule the host
turns on with `ToClient_RequestArshaLostRegionMode(true)`
(`panel_window_arsha_func_all`). One row per stage: the stage index, an
unnamed count, a point and two distances that read as the zone's centre and
its start and end radius, and the skill the zone applies,
`41292` 아르샤의 창: 자기장 디버프(초당 -500) ("Arena of Arsha: magnetic
field debuff, -500 per second"). On client 3474 the file has 3 stages.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `arshasetlostregion.bss` | 110   | 3 Row   | 30        |

| Layout | File                     | Known        | Unknown      |
| ------ | ------------------------ | ------------ | ------------ |
| 1      | `arshasetlostregion.bss` | 38 B (34.5%) | 72 B (65.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone; the skill's Korean name comes from
the `skilltype.dbss` lookup index the app loads at start.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of stages                              |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (30 bytes)

| Offset  | Type | Field      | Notes                                                                                  |
| ------- | ---- | ---------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u32  | index      | Stage, `1` to `3`; see Field Names                                                     |
| `+0x04` | u32  | unknown_04 | `170`, `120`, `60` by stage; see Open Questions                                        |
| `+0x08` | f32  | unknown_08 | `183634` on every row                                                                  |
| `+0x0C` | f32  | unknown_0c | `-5063` on every row                                                                   |
| `+0x10` | f32  | unknown_10 | `404400` on every row                                                                  |
| `+0x14` | f32  | unknown_14 | `4600`, `2100`, `1100` by stage; the next stage's `unknown_18`                         |
| `+0x18` | f32  | unknown_18 | `9000`, `4600`, `2100` by stage                                                        |
| `+0x1C` | u16  | skill_no   | `skilltype.dbss` skill number, `41292` on every row; the handler shows its Korean name |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The server executable of a private server on client 1784 loads the file
with `GameCommonParameterLoaderFromExcel::loadArshaSetLostRegion` into the
`ArshaSetLostRegionStaticStatusManager`, whose insert error names the row
key `[index]`; the stages count from `1`. The `LostRegion_Table` sheet of
that private server's `DataSheets.bexcel` belongs to the Shadow Arena and
has the columns `Index` and `Order` and one row, so no sheet column matches
the other fields. `skill_no` is a `skilltype.dbss` skill number whose
Korean name is the Arena of Arsha zone debuff. `41292` is also a
`buff.dbss` key (Morning Sun: AP -200), which does not fit the zone.

## Notes

- The file is 110 bytes and the same on clients 1784, 2107, 2519, 3002,
  3251 and 3474.
- `unknown_08`, `unknown_0c` and `unknown_10` are the same on every row and
  read as one x, y, z point in world units, `unknown_14` and `unknown_18` as
  the radius a stage ends at and starts from: each stage starts at the
  radius the previous one ended at (9000 to 4600, 4600 to 2100, 2100 to
  1100). `test_pvp_tables.py` checks that chain.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`.

## Open Questions

### Stage Time

What `unknown_04` counts. `170`, `120` and `60` fall by stage, which fits
the seconds a stage lasts or the time before the zone shrinks, but no Lua
reads the value.

### Zone Point and Radii

Whether `unknown_08` to `unknown_10` are the centre of the zone in the
Arena of Arsha and `unknown_14` and `unknown_18` its end and start radius.
The values fit that reading; no Lua or sheet names them.
