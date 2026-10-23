# `reusegroup.bss` Format

## Purpose

The skill cooldown groups: skills that share a `ReuseGroup` share one
cooldown. A PABR list with one row per group key and a flag that is set
when the group's cooldown runs out while the player is offline. On client
3482 it holds 178 groups, `1` to `180` without `30` and `31`, and the
flag is set on ten of them; client 1784 holds `1` to `144`. The rows are
not in key order: they run down in blocks of up to 16 keys (`175` to
`160`, `180` to `176`, `143` to `128`, ...).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------- | --------- |
| 2      | 3251 and later | 3482    | `reusegroup.bss` | 910   | 178 Row | 5         |
| 1      | 1194 to 3212   | 3212    | `reusegroup.bss` | 562   | 180 Row | 3         |

| Layout | File             | Known          | Unknown    |
| ------ | ---------------- | -------------- | ---------- |
| 2      | `reusegroup.bss` | 910 B (100.0%) | 0 B (0.0%) |
| 1      | `reusegroup.bss` | 560 B (99.6%)  | 2 B (0.4%) |

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
| 1996   | Layout 1 |
| 1969   | Layout 1 |
| 1937   | Layout 1 |
| 1914   | Layout 1 |
| 1886   | Layout 1 |
| 1866   | Layout 1 |
| 1838   | Layout 1 |
| 1818   | Layout 1 |
| 1794   | Layout 1 |
| 1784   | Layout 1 |
| 1749   | Layout 1 |
| 1717   | Layout 1 |
| 1698   | Layout 1 |
| 1674   | Layout 1 |
| 1636   | Layout 1 |
| 1608   | Layout 1 |
| 1587   | Layout 1 |
| 1565   | Layout 1 |
| 1537   | Layout 1 |
| 1509   | Layout 1 |
| 1485   | Layout 1 |
| 1466   | Layout 1 |
| 1445   | Layout 1 |
| 1426   | Layout 1 |
| 1409   | Layout 1 |
| 1390   | Layout 1 |
| 1372   | Layout 1 |
| 1360   | Layout 1 |
| 1348   | Layout 1 |
| 1338   | Layout 1 |
| 1324   | Layout 1 |
| 1316   | Layout 1 |
| 1309   | Layout 1 |
| 1286   | Layout 1 |
| 1256   | Layout 1 |
| 1230   | Layout 1 |
| 1211   | Layout 1 |
| 1194   | Layout 1 |
| 1177   | No file  |
| 1156   | No file  |
| 1137   | No file  |
| 1132   | No file  |
| 1127   | No file  |
| 1122   | No file  |
| 1118   | No file  |
| 1114   | No file  |
| 1109   | No file  |
| 1102   | No file  |
| 1096   | No file  |
| 1088   | No file  |
| 1081   | No file  |
| 1076   | No file  |
| 1069   | No file  |
| 1064   | No file  |
| 1058   | No file  |
| 1051   | No file  |
| 1044   | No file  |
| 1036   | No file  |
| 1026   | No file  |
| 1016   | No file  |
| 1009   | No file  |
| 1005   | No file  |
| 1000   | No file  |
| 998    | No file  |
| 990    | No file  |
| 979    | No file  |
| 972    | No file  |
| 963    | No file  |
| 955    | No file  |
| 946    | No file  |
| 938    | No file  |
| 927    | No file  |
| 911    | No file  |
| 904    | No file  |
| 899    | No file  |
| 894    | No file  |
| 885    | No file  |
| 879    | No file  |
| 872    | No file  |
| 864    | No file  |
| 855    | No file  |
| 853    | No file  |
| 845    | No file  |
| 837    | No file  |
| 829    | No file  |
| 822    | No file  |
| 814    | No file  |
| 805    | No file  |
| 794    | No file  |
| 787    | No file  |
| 780    | No file  |
| 771    | No file  |
| 760    | No file  |
| 748    | No file  |
| 741    | No file  |
| 736    | No file  |
| 731    | No file  |
| 723    | No file  |
| 711    | No file  |
| 707    | No file  |
| 697    | No file  |
| 689    | No file  |
| 683    | No file  |
| 678    | No file  |
| 670    | No file  |
| 661    | No file  |
| 656    | No file  |
| 652    | No file  |
| 643    | No file  |
| 637    | No file  |
| 630    | No file  |
| 627    | No file  |
| 621    | No file  |
| 617    | No file  |
| 615    | No file  |
| 606    | No file  |
| 599    | No file  |
| 592    | No file  |
| 586    | No file  |
| 577    | No file  |
| 569    | No file  |
| 561    | No file  |
| 554    | No file  |
| 542    | No file  |
| 532    | No file  |
| 531    | No file  |
| 526    | No file  |
| 521    | No file  |
| 517    | No file  |
| 510    | No file  |
| 508    | No file  |
| 504    | No file  |
| 497    | No file  |
| 491    | No file  |
| 485    | No file  |
| 478    | No file  |
| 472    | No file  |
| 466    | No file  |
| 457    | No file  |
| 452    | No file  |
| 449    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of groups                              |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (5 bytes)

| Offset  | Type | Field                 | Notes                                                          |
| ------- | ---- | --------------------- | -------------------------------------------------------------- |
| `+0x00` | u32  | reuse_group           | Group key, the `ReuseGroup` of the skills in the group; unique |
| `+0x04` | u8   | is_expired_in_offline | `1` when a skill of the group has `isExpiredInOffline` set     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### File Layout

| Offset              | Type           | Field              | Notes                                                       |
| ------------------- | -------------- | ------------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                                |
| `+0x04`             | u32            | row_count          | Number of groups                                            |
| `+0x08`             | Row[row_count] | rows               | See Row                                                     |
| `rows+0x00`         | u16            | unknown_after_rows | `144` on client 1784, equal to `row_count` and the top key  |
| `rows+0x02`         | String Table   | string_table       | See String Table                                            |
| `string_table+0x00` | u32            | table_start        | Offset of the string table, where `unknown_after_rows` ends |
| `string_table+0x04` | u32            | zero               | Always `0`                                                  |

### Row (3 bytes)

| Offset  | Type | Field                 | Notes                         |
| ------- | ---- | --------------------- | ----------------------------- |
| `+0x00` | u16  | reuse_group           | Group key                     |
| `+0x02` | u8   | is_expired_in_offline | Same as Layout 2              |

## Field Names

The `Skill_Table_New` sheet of a private server's `DataSheets.bexcel` on
client 1784 has a `ReuseGroup` column, and its server dump reads it next
to `ReuseCycle`, `IsGlobalCycle` and `isExpiredInOffline`. All 144 group
keys of the client 1784 file are `ReuseGroup` values of that sheet, so the
key is `reuse_group`. The flag matches `isExpiredInOffline` on 144 of 144
groups: it is `1` on the six groups where at least one skill of the group
sets `isExpiredInOffline` (`54`, `55`, `120`, `127`, `140`, `141`) and `0`
on every group where no skill does. `IsGlobalCycle` is `0` on every skill
of every group, so it does not place the flag.

## Notes

- On client 3482 the flag is set on groups `54`, `55`, `120`, `127`,
  `140`, `141`, `158`, `159`, `160` and `177`.
- Group `141` mixes skills with and without `isExpiredInOffline` on client
  1784 (3 of 9); the flag is `1`, so one set skill sets the group.
- The cooldown lengths (`ReuseCycle` on the sheet) stay in the skill
  tables; this file holds none.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/world_tables.py`.

## Open Questions

### The u16 After the Rows of Layout 1

Layout 1 ends its rows with a u16 that is `144` on client 1784, both the
row count and the highest group key there, so the values cannot tell a
second count from a top key. Layout 2 no longer has it.
