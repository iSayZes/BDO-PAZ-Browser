# `blackspiritchangeformcondition.bss` Format

## Purpose

The condition a character must meet before it can change the Black
Spirit's form: the whole file is one UTF-16 condition script. On client
3482 it reads `clearquest(5007,4);getlevel()>55;<or>clearquest(9107,5);getlevel()>59;`
(client 1784: the first alternative only). The forms themselves and the
condition of each are in [`blackspirit.dbss`](blackspirit_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------------ | ----- | ------- | --------- |
| 1      | 1348 and later | 3482    | `blackspiritchangeformcondition.bss` | 148   | -       | -         |

| Layout | File                                 | Known          | Unknown    |
| ------ | ------------------------------------ | -------------- | ---------- |
| 1      | `blackspiritchangeformcondition.bss` | 148 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None; the handler reads this file alone.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type  | Field            | Notes                                                   |
| ------- | ----- | ---------------- | ------------------------------------------------------- |
| `+0x00` | str16 | change_condition | Condition script, `<or>` between alternatives; ends the file |

On client 3482 the file is 8 + 2 x 70 = 148 bytes.

## Field Names

The `Option_Table` sheet of `DataSheet_BlackSpirit.xlsx` in a private
server's `DataSheet` folder on client 1784 has one column,
`ChangeCondition`, and one row: `clearquest(5007,4);getlevel()>55;`, the
same text as the client 1784 file. The server dump of that client names the
loader `loadBlackSpiritChangeFormConditionInfo`.

## Notes

- No client Lua (3482) reads the condition; the skin select window
  (`panel_widget_blackspirit_skillselect.luac`) lists only the forms the
  client reports as unlocked.
