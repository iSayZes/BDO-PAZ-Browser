# `employeejobslotstaticstatus.bss` Format

## Purpose

Sailor preset job slots per ship: for each ship character eight slot
counts, one per preset job of the Sailor Preset window (the
`__eEmployeePresetJob_*` jobs `ViceCaptain`, `Sail`, `Helmsman`,
`CannonSlot`, `Deck`, `Cook`, `Cabin` and `Fishing`; their order in the
row is an open question). After the ships follows a table of 41 entries, keys `0` to
`40`, with values `1` to `8`. On client 3482 the file lists 15 ships, from
the Epheria Sailboat to the four Epheria Carrack types.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ---------------- | --------- |
| 1      | 2834 and later | 3482    | `employeejobslotstaticstatus.bss` | 413   | 15 Row, 41 Entry | 3         |

| Layout | File                              | Known         | Unknown       |
| ------ | --------------------------------- | ------------- | ------------- |
| 1      | `employeejobslotstaticstatus.bss` | 290 B (70.2%) | 123 B (29.8%) |

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
| 2803   | No file  |
| 2765   | No file  |
| 2736   | No file  |
| 2703   | No file  |
| 2665   | No file  |
| 2637   | No file  |
| 2606   | No file  |
| 2583   | No file  |
| 2545   | No file  |
| 2519   | No file  |
| 2498   | No file  |
| 2468   | No file  |
| 2438   | No file  |
| 2414   | No file  |
| 2384   | No file  |
| 2358   | No file  |
| 2335   | No file  |
| 2313   | No file  |
| 2290   | No file  |
| 2250   | No file  |
| 2224   | No file  |
| 2203   | No file  |
| 2179   | No file  |
| 2151   | No file  |
| 2134   | No file  |
| 2107   | No file  |
| 2073   | No file  |
| 2052   | No file  |
| 2011   | No file  |
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

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | Ship names (LOC type 6) |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a ship without a row shows as plain text instead of a link |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The PABR layout of [`bdoservanttitless.bss`](bdoservanttitless_bss.md)
with a second table between the rows and the empty string table; no count
gives its length, it runs up to `table_start`.

| Offset         | Type                  | Field        | Notes |
| -------------- | --------------------- | ------------ | ----- |
| `+0x00`        | char[4]               | magic        | `PABR` |
| `+0x04`        | u32                   | record_count | Number of ships |
| `+0x08`        | Row[record_count]     | records      | See Row |
| `records+0x00` | Entry[..table_start]  | entries      | See Entry |
| `EOF-0x0C`     | u32                   | string_count | Always `0`; the empty PABR string table |
| `EOF-0x08`     | u32                   | table_start  | Offset of `string_count`, where the entries end |
| `EOF-0x04`     | u32                   | zero         | Always `0` |

### Row (18 bytes)

| Offset  | Type   | Field           | Notes |
| ------- | ------ | --------------- | ----- |
| `+0x00` | u16    | character_key   | Ship character key (`31001` Epheria Sailboat, `31045` Epheria Carrack); unique |
| `+0x02` | u16[8] | job_slot_counts | Slots per preset job; see [Job Slots](#job-slots-client-3482) |

### Entry (3 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u16  | unknown_00 | `0` to `40`, one entry each, in this order |
| `+0x02` | u8   | unknown_02 | `1` to `8`, never falling from one entry to the next |

## Job Slots (Client 3482)

| Ships | `job_slot_counts` |
| ----- | ----------------- |
| Epheria Sailboat `31001`, Epheria Frigate `31003`, Bartali Sailboat `31053`, Improved Epheria Sailboat `31058`, Improved Epheria Frigate `31059` | `0, 0, 0, 0, 0, 0, 2, 0` |
| Epheria Caravel `31048`, Epheria Galleass `31049` | `0, 0, 0, 0, 0, 0, 6, 0` |
| Epheria Carrack `31045`, Epheria Carrack: Valor `31085` | `1, 1, 1, 1, 2, 1, 20, 0` |
| Panokseon `31025` | `1, 1, 1, 1, 3, 1, 30, 0` |
| Epheria Carrack: Advance `31054` | `1, 1, 1, 1, 1, 2, 20, 1` |
| Epheria Carrack: Balance `31055`, Epheria Carrack: Volante `31056` | `1, 2, 1, 1, 1, 1, 20, 1` |
| Epheria Carrack: Valor `31057`, GM: Epheria Carrack `31084` | `1, 1, 1, 1, 2, 1, 20, 1` |

The entries rise as `0:1, 1:2, 2:2, 3:3, 4:4, 5:5, 6:5, 7:5, 8:6, 9:6,
10:7, 11:8` and stay at `8` from key `11` to `40`.

## Field Names

`ToClient_getEmployeePresetJobCount(shipCharacterKey, job)` in
`panel_window_sailorpresetmanager_all_1.luac` (client 3482) gives the
number of slots of one preset job on a ship, for `job` from `1` to
`__eEmployeePresetJob_Count - 1`, and hides a job whose count is `0`.
The row is a ship character key and eight counts, the eight preset jobs
of that window (`ViceCaptain`, `Sail`, `Deck`, `Helmsman`, `CannonSlot`,
`Cook`, `Fishing`, `Cabin`), so the array is named `job_slot_counts`. The
file is not in client 1784 and has no sheet in a private server's
`DataSheets.bexcel` on client 1784.

## Notes

- The file is in client 2834 and later; clients 3002 to 3482 hold the
  same bytes.
- The largest count (`2` to `30`) is the seventh. The Sailor Preset window
  pages its Cabin slots (`_currentCabinPageCount`), which fits a job with
  many slots.

## Open Questions

### Order of the Preset Jobs

The Lua names the jobs but not their numbers, which the client sets.
The tooltip texts of the window are numbered `LUA_SAILOR_PRESET_SLOT_01`
(`ViceCaptain`), `_02` (`Sail`), `_03` (`Helmsman`), `_04` (`CannonSlot`),
`_05` (`Deck`), `_06` (`Cook`), `_07` (`Cabin`) and `_08` (`Fishing`).
Read in that order, the seventh count is `Cabin` (`2` to `30`), the
eighth `Fishing` (`1` on Epheria Carrack: Advance, Balance, Volante,
Valor `31057` and the GM carrack only), and Epheria Carrack: Balance and
Volante get two `Sail` slots. Whether the array follows that numbering is
not confirmed.

### What the Entries Are

41 entries with keys `0` to `40` and values `1` to `8`. Sailors reach
level 10 (`employeeexp.bss`), so the key is not a sailor level; the top
value `8` equals the number of preset jobs. What the key counts is open.
