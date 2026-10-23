# `instancefieldcommon.bss` Format

## Purpose

Entry limits of an instance: per instance type and mode the lowest
character level, the quest that must be done first and the Korean message
shown when a character is turned away. The only row on client 3482 asks
for level 56 and quest `804, 1` ("[Awakening] The Black Spirit's Strange
Power"); its message says that `가시나무 성` can only be entered after the
character awakening quest, and not below level 56. The file is the
`InstanceCommonOption` sheet compiled into a PABR table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | --------------------- | --------- |
| 2      | 1466 and later | 3482    | `instancefieldcommon.bss` | 185   | 1 Row, 1 String Table | 22        |
| 1      | 1426 to 1445   | 1445    | `instancefieldcommon.bss` | 257   | 1 Row, 1 String Table | 16        |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 2      | `instancefieldcommon.bss` | 179 B (96.8%)  | 6 B (3.2%) |
| 1      | `instancefieldcommon.bss` | 257 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3454   | Layout 2 |
| 3412   | Layout 2 |
| 3381   | Layout 2 |
| 3349   | Layout 2 |
| 3314   | Layout 2 |
| 3283   | Layout 2 |
| 3251   | Layout 2 |
| 3212   | Layout 2 |
| 3177   | Layout 2 |
| 3144   | Layout 2 |
| 3103   | Layout 2 |
| 3062   | Layout 2 |
| 3037   | Layout 2 |
| 3002   | Layout 2 |
| 2959   | Layout 2 |
| 2923   | Layout 2 |
| 2900   | Layout 2 |
| 2872   | Layout 2 |
| 2834   | Layout 2 |
| 2803   | Layout 2 |
| 2765   | Layout 2 |
| 2736   | Layout 2 |
| 2703   | Layout 2 |
| 2665   | Layout 2 |
| 2637   | Layout 2 |
| 2606   | Layout 2 |
| 2583   | Layout 2 |
| 2545   | Layout 2 |
| 2519   | Layout 2 |
| 2498   | Layout 2 |
| 2468   | Layout 2 |
| 2438   | Layout 2 |
| 2414   | Layout 2 |
| 2384   | Layout 2 |
| 2358   | Layout 2 |
| 2335   | Layout 2 |
| 2313   | Layout 2 |
| 2290   | Layout 2 |
| 2250   | Layout 2 |
| 2224   | Layout 2 |
| 2203   | Layout 2 |
| 2179   | Layout 2 |
| 2151   | Layout 2 |
| 2134   | Layout 2 |
| 2107   | Layout 2 |
| 2073   | Layout 2 |
| 2052   | Layout 2 |
| 2011   | Layout 2 |
| 1996   | Layout 2 |
| 1969   | Layout 2 |
| 1937   | Layout 2 |
| 1914   | Layout 2 |
| 1886   | Layout 2 |
| 1866   | Layout 2 |
| 1838   | Layout 2 |
| 1818   | Layout 2 |
| 1794   | Layout 2 |
| 1784   | Layout 2 |
| 1749   | Layout 2 |
| 1717   | Layout 2 |
| 1698   | Layout 2 |
| 1674   | Layout 2 |
| 1636   | Layout 2 |
| 1608   | Layout 2 |
| 1587   | Layout 2 |
| 1565   | Layout 2 |
| 1537   | Layout 2 |
| 1509   | Layout 2 |
| 1485   | Layout 2 |
| 1466   | Layout 2 |
| 1445   | Layout 1 |
| 1426   | Layout 1 |
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

None. The handler names the quest from LOC type 18.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                              |
| ------------------- | ----------------- | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                             |
| `+0x04`             | u32               | record_count       | Number of rows                     |
| `+0x08`             | Row[record_count] | records            | See Row                            |
| `records+0x00`      | String Table      | string_table       | The limit messages                 |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`  |
| `string_table+0x04` | u32               | zero               | `0`                                |

### Row (variable: 20 bytes + list)

| Offset  | Type             | Field                   | Notes |
| ------- | ---------------- | ----------------------- | ----- |
| `+0x00` | u16              | instance_mode           | `0`; together with `instance_type` the row key |
| `+0x02` | u16              | instance_type           | `4` |
| `+0x04` | u32              | limited_character_level | Lowest character level, `56` |
| `+0x08` | u16              | limited_quest_group     | Quest chain of the required quest, `804` |
| `+0x0A` | u16              | limited_quest_id        | Quest number in that chain, `1` |
| `+0x0C` | u32              | limited_quest_string    | Index into `strings`: the message for a character that lacks the quest or the level |
| `+0x10` | u32              | unknown_10              | Number of `unknown_14` values, `1` |
| `+0x14` | u16[unknown_10]  | unknown_14              | `4`; see [unknown_10 and unknown_14](#unknown_10-and-unknown_14) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `1` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | Korean text, wide (`is_wide` 1); a `\n` is stored as the two characters `\` and `n` |

## Layout 1

Clients 1426 and 1445 end the row after `limited_quest_string`; their row
asks for quest `8003, 2` and level 56, with a longer message.

### Row (16 bytes)

| Offset  | Type | Field                   | Notes |
| ------- | ---- | ----------------------- | ----- |
| `+0x00` | u16  | instance_mode           | |
| `+0x02` | u16  | instance_type           | |
| `+0x04` | u32  | limited_character_level | |
| `+0x08` | u16  | limited_quest_group     | |
| `+0x0A` | u16  | limited_quest_id        | |
| `+0x0C` | u32  | limited_quest_string    | |

## Field Names

The names follow the `InstanceCommonOption` sheet of a private server's
`DataSheets.bexcel` on client 1784 (`InstanceType`, `InstanceMode`,
`LimitedCharacterLevel`, `LimitedQuestGroup`, `LimitedQuestID`,
`LimitedQuestString`). The sheet has one row, and every one of those six
values equals the file of client 1784, which is byte for byte the file of
client 3482. The server loader for the sheet in the client 1784 server
dump packs the key as `InstanceType << 16 | InstanceMode`, which puts
`instance_mode` in the low two bytes; it reads `LimitedQuestGroup` and
`LimitedQuestID` as 16-bit values.

## Notes

- The file has not changed from client 1784 to client 3482.

## Open Questions

### unknown_10 and unknown_14

The sheet's last column, `ContentsGroupKey`, is a list (the server loader
reads it as a list and turns every entry into another value before it
stores it), and `unknown_10` / `unknown_14` are the only list in the row.
The sheet holds `7` and the file `4`, so the list is not the contents
group key itself. What `4` stands for is open.
