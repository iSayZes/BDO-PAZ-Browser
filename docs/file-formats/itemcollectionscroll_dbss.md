# `itemcollectionscroll.dbss` Format

## Purpose

The levels of the Item Collection Increase gauge. Item Collection Increase
Scrolls charge time into a family gauge, and the player switches it between
Lv. 0 (off), Lv. 1 and Lv. 2 in the gauge widget
(`panel_widget_hopegaugeonoff_1.luac`). One 16-byte row per level: the
level, the Item Drop Rate and Item Drop Amount bonuses it gives and how fast
it uses the charged time, all three on the 1,000,000 = 100% scale. Lv. 0 has
no row. Companion `itemcollectionscrolloffset.dbss` lists where every row
sits.

| Level | Item Drop Rate | Item Drop Amount | Time use |
| ----- | -------------- | ---------------- | -------- |
| `1`   | 100%           | 50%              | 100%     |
| `2`   | 100%           | 100%             | 200%     |

Values from clients 1784 and 3474. The scroll's TextBind description
(`ItemDropIncrease_Scroll`, LOC type 59, client 3474) gives the same
numbers: Lv. 1 "Item Drop Rate +100%, Item Drop Amount +50%", Lv. 2 "Item
Drop Rate +100%, Item Drop Amount +100%" and "Activating Lv. 2 consumes time
twice as fast".

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `itemcollectionscroll.dbss`       | 36    | 2 Row        | 16        |
| 1      | 1485 and later | 3474    | `itemcollectionscrolloffset.dbss` | 28    | 2 Offset Row | 12        |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `itemcollectionscroll.dbss`       | 36 B (100.0%) | 0 B (0.0%) |
| 1      | `itemcollectionscrolloffset.dbss` | 28 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                                 |
| --------------------------------- | -------- | -------------------------------------------------------------------- |
| `itemcollectionscrolloffset.dbss` | Optional | `grade -> (data_offset, data_size)` of every row; the rows are fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                              |
| ------- | ---------- | ----- | ---------------------------------- |
| `+0x00` | u32        | count | Number of rows; `2` on client 3474 |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (16 bytes)

| Offset  | Type | Field        | Notes                                                                 |
| ------- | ---- | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32  | grade        | Gauge level, `1` or `2`; unique per row, the index key                |
| `+0x04` | i32  | drop_rate    | Item Drop Rate bonus, 1,000,000 = 100%                                |
| `+0x08` | i32  | count_rate   | Item Drop Amount bonus, 1,000,000 = 100%                              |
| `+0x0C` | i32  | cost_percent | Charged time used per real second, 1,000,000 = 1 second (100%)        |

### `itemcollectionscrolloffset.dbss`

| Offset  | Type              | Field | Notes                                        |
| ------- | ----------------- | ----- | -------------------------------------------- |
| `+0x00` | u32               | count | Equals the `itemcollectionscroll.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row         |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                               |
| ------- | ---- | ----------- | ----------------------------------- |
| `+0x00` | u32  | grade       | Key of the row it points at         |
| `+0x04` | u32  | data_offset | Start of the row, at its `grade`    |
| `+0x08` | u32  | data_size   | `16`, the whole row                 |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. On
clients 1784 and 3474 the index lists level `2` first and level `1` second,
in the order of the main file, and every index row points at the row with
its key.

## Field Names

The names are the columns of the `ItemDropIncrease_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784: `Index`, `CoutRate` (sic),
`DropRate`, `CostPercent` and `SkillNo`. Its two rows, (`1`, `500000`,
`1000000`, `1000000`, `52597`) and (`2`, `1000000`, `1000000`, `2000000`,
`52598`), match the file on 2 of 2 keys on clients 1784 and 3474, and the
values place each column: only `CoutRate` holds `500000` and only
`CostPercent` holds `2000000`. The 1784 and 3474 files are byte for byte the
same.

The client 1784 server dump of the same private server loads the sheet in
`GameCommonParameterLoaderFromExcel::loadMain(loadItemCollectionScroll)`
into `ItemCollectionScrollBuffManager`. The loader reads `Index`, `CoutRate`,
`DropRate` and `CostPercent` as ints, stores them as `Index`, `DropRate`,
`CoutRate`, `CostPercent` (the order of this file) and logs a bad row as
`%#:grade(%#) : ErrNo(%#)`. It does not read `SkillNo`, which is not in
the file. `Index` is named `grade` here after that message and the client
Lua, which reads the level with `getItemCollectionScrollGrade()` and the two
bonuses with `ToClient_GetHopeDropByGrade(grade)` and
`ToClient_GetHopeCountByGrade(grade)`. The 2016 PDB has no item collection
struct.

## Notes

- The level `2` tooltip `LUA_HOPEGAUGE_TOOLTIP_DESC2` (client 3474) says
  "Consumes double Level 1 time", and `LUA_HOPE_GRADE_ON2` says "Consumes 2
  sec of charged time per 1 real sec", which is `cost_percent` `2000000`.
- The sheet's `SkillNo` values are skills of client 3474's `skill.dbss`:
  `52597` Item Collection Increase Function Rework (buffs `52349` and
  `52350`) and `52598` Item Collection Increase Function Rework Advanced
  (buffs `52351` and `52352`). In [`buff.dbss`](buff_dbss.md) `52349` and
  `52351` are effect type `57` (Item Drop Rate) with `param_1` `1000000`,
  `52350` and `52352` effect type `112` (Item Drop Amount) with `param_1`
  `500000` and `1000000`: the `drop_rate` and `count_rate` of levels 1 and 2.
- The gauge cap and the 5-minute change cooldown are not in this file. The
  client 1784 bexcel holds them in the `EtcOption` sheet
  (`ItemDropIncreasePointLimit`, `ItemDropIncreaseCoolTime`,
  `ItemDropIncreaseWarning`); the Lua reads them with
  `ToClient_ItemCollectionPointLimit()`, `ToClient_getItemCollectionScrollCoolTime()`
  and `ToClient_getHopeGaugeAlert()`.
- `LUA_HOPE_CHARGE_INFO` (client 3474) lists what each scroll charges:
  1,800 seconds for the 30-minute scroll, 3,600 for the 60-minute scroll and
  7,200 for the Advanced scroll, up to 10 hours. The charge per scroll is
  the item's `getContentsEventParam1()` in `panel_widget_hopegauge_1.luac`,
  not a field of this file.
