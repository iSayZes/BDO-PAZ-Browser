# `abyssonecoin.bss` Format

## Purpose

A Magnus (`AbyssOne`) table with no PABR magic: rows of a u16 key and a
u64 value. On client 3482 the keys are `4001` to `4071`, one row each, and
the value grows with the key from `50` to `690` in steps of `10`. The file
name and the Magnus coin currency (`__eInventoryMoneyType_Abyss`) suggest
a coin amount per key; what the key counts is open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------ | ----- | ------- | --------- |
| 1      | 2011 and later | 3482    | `abyssonecoin.bss` | 714   | 71 Row  | 10        |

| Layout | File               | Known      | Unknown       |
| ------ | ------------------ | ---------- | ------------- |
| 1      | `abyssonecoin.bss` | 4 B (0.6%) | 710 B (99.4%) |

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

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

### Row (10 bytes)

| Offset  | Type | Field      | Notes                                                                  |
| ------- | ---- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | u16  | unknown_00 | Row key; `4001` to `4071` on client 3482, unique per row               |
| `+0x02` | u64  | unknown_02 | `50` to `690` on client 3482; see Values                               |

## Values

On client 3482 `unknown_02` is `(unknown_00 - 4001) x 10 + 50` for the
keys `4001` to `4061`. `4062` repeats the `650` of `4061`, so `4063` to
`4066` run one step behind (`660` to `690`), and `4067` to `4071` hold
`690` as well. The rows are not in key order: they run down from `4071` in blocks
(`4071` to `4064`, `4047` to `4032`, `4063` to `4048`, `4015` to `4001`,
`4031` to `4016`).

| Client | Rows | Keys           | Values      |
| ------ | ---- | -------------- | ----------- |
| 2107   | 66   | `4001`-`4066`  | `50`-`690`  |
| 3482   | 71   | `4001`-`4071`  | `50`-`690`  |

## Field Names

The Magnus is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`Abyss` in its name. The keys match no LOC type 17 region and no
`regioninfo.bss` key, and their LOC entries in other types (item `4001`
Iron Ore, knowledge `4001` Parasitic Bee) have nothing to do with the
Magnus. Both fields stay unknown.

## Notes

- The u64 value fits the Magnus coin type: the equipment preset Lua reads
  its coin price as an s64 (`presetEquipSSW:getAbyssCoin()`,
  `panel_abyssone_equippresetlist.luac`), and
  [`abyssoneequipmentpreset.bss`](abyssoneequipmentpreset_bss.md) stores
  that price as a u64.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/abyssone_tables.py`: each
  row's bytes as hex, since no field is named.

## Open Questions

### What the Key Counts

The keys run from `4001` with no gap, and client 3482 adds `4067` to
`4071` to the 66 keys of client 2107 with the capped value `690`. A level
or tier of Magnus content would fit a key that only grows. The only coin
names with `Abyss` in the client 3482 Lua are `_ContentsGroup_AbyssOneCoin`,
`__eInventoryMoneyType_Abyss` and `getAbyssCoin()` of the equipment
presets, and none of them takes a key.
