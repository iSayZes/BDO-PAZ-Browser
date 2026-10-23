# `abyssoneaudioinfo.bss` Format

## Purpose

The background music and ambience of the Abyss One (The Magnus) fields: per
`fieldinfo.bss` field (`A1_001` to `A1_065`) the four Wwise `BGM` states
it plays and its ambience index, the same pair of values
[`audioinfo.bss`](audioinfo_bss.md) holds per area colour of the world.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 1      | 2011 and later | 3482    | `abyssoneaudioinfo.bss` | 1,988 | 49 Row  | 22        |

| Layout | File                    | Known            | Unknown    |
| ------ | ----------------------- | ---------------- | ---------- |
| 1      | `abyssoneaudioinfo.bss` | 1,988 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3454   | Layout 1 |
| 3412   | Layout 1 |
| 3381   | Layout 1 |
| 3349   | Layout 1 |
| 3314   | Layout 1 |
| 3283   | Layout 1 |
| 3251   | Layout 1 |
| 3212   | Layout 1 |
| 3177   | Layout 1 |
| 3144   | Layout 1 |
| 3103   | Layout 1 |
| 3062   | Layout 1 |
| 3037   | Layout 1 |
| 3002   | Layout 1 |
| 2959   | Layout 1 |
| 2923   | Layout 1 |
| 2900   | Layout 1 |
| 2872   | Layout 1 |
| 2834   | Layout 1 |
| 2803   | Layout 1 |
| 2765   | Layout 1 |
| 2736   | Layout 1 |
| 2703   | Layout 1 |
| 2665   | Layout 1 |
| 2637   | Layout 1 |
| 2606   | Layout 1 |
| 2583   | Layout 1 |
| 2545   | Layout 1 |
| 2519   | Layout 1 |
| 2498   | Layout 1 |
| 2468   | Layout 1 |
| 2438   | Layout 1 |
| 2414   | Layout 1 |
| 2384   | Layout 1 |
| 2358   | Layout 1 |
| 2335   | Layout 1 |
| 2313   | Layout 1 |
| 2290   | Layout 1 |
| 2250   | Layout 1 |
| 2224   | Layout 1 |
| 2203   | Layout 1 |
| 2179   | Layout 1 |
| 2151   | Layout 1 |
| 2134   | Layout 1 |
| 2107   | Layout 1 |
| 2073   | Layout 1 |
| 2052   | Layout 1 |
| 2011   | Layout 1 |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names the field through the `fieldinfo.bss` field name
lookup.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of fields                              |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (22 bytes)

| Offset  | Type   | Field               | Notes                                                                                   |
| ------- | ------ | ------------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u16    | field_no            | A `fieldinfo.bss` field (`4001` `A1_001`); each key once, in no order                   |
| `+0x02` | u32[4] | bgm_states          | Indexes into `strings`: four Wwise `BGM` states; the four are one string on every row of client 3482 |
| `+0x12` | u32    | bank_no_environment | Ambience: the Wwise `ENV_INDEX_<n>` state (`201` to `208`, `12`, `13`, `43`, `0`)       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                            |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                |
| `+0x04` | pstr[string_count] | strings      | State names, UTF-8 (`W11_AbyssOne_Quest_Idx062`, `W02_Ocean_Empty`); a string several rows use is stored once |

## Field Names

No sheet of the client 1784 `DataSheets.bexcel` and no table of the client
519 server data holds the file; client 2011 is the first test client that
has it. The names follow [`audioinfo.bss`](audioinfo_bss.md), whose Row
ends in the same four state indexes and ambience value:

- `field_no`: 49 of 49 keys are `fieldinfo.bss` fields, all named `A1_`
  (client 3482).
- `bgm_states`: 21 of the 34 strings are states of the `BGM` state group
  in `sound2022/wwise_ids.h`; the 13 `W<nn>_Ocean_Empty` names are in no
  state group (client 3482).
- `bank_no_environment`: 49 of 49 values are `ENV_INDEX_<n>` states of
  the same header (client 3482).

## Open Questions

### Ocean Empty States

The 13 `W<nn>_Ocean_Empty` names are not `BGM` states in
`sound2022/wwise_ids.h`. The client may fall back to silence for an
unknown state, which would make these fields play no music.
