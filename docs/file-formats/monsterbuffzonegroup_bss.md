# `monsterbuffzonegroup.bss` Format

## Purpose

Per region a list of structure monsters (totems, guard towers, statues,
altars) and for each one a list of up to five other character keys. On
client 3482 the file has 28 regions, all hunting grounds (Olun's Valley,
Tunkuta, Hystria Ruins, Aakman Temple, Gyfin Rhasia Temple, Roud Sulfur
Works and more); Olun's Golem `21249` in Olun's Valley lists `21250` and
`21253`, Cyclops Statue `21696` in Cyclops Land lists Cyclops `21693`. The
file name ties it to the monster buff zone of
[`monsterbuffzone.bss`](monsterbuffzone_bss.md). The file is a u32 count
and variable rows, with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ---------------- | --------- |
| 1      | 2250 and later | 3482    | `monsterbuffzonegroup.bss` | 1,026 | 34 Entry, 28 Row | 21        |

| Layout | File                       | Known         | Unknown       |
| ------ | -------------------------- | ------------- | ------------- |
| 1      | `monsterbuffzonegroup.bss` | 784 B (76.4%) | 242 B (23.6%) |

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
| `languagedata_en.loc`        | Optional | Region names (LOC type 17) and character names (LOC type 6) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 11 bytes + entries)

| Offset  | Type               | Field       | Notes |
| ------- | ------------------ | ----------- | ----- |
| `+0x00` | u16                | region_key  | `regioninfo.bss` region key; unique, not sorted |
| `+0x02` | u32                | unknown_02  | `1` on every row (client 3482) |
| `+0x06` | u8                 | unknown_06  | `0` on every row |
| `+0x07` | u32                | entry_count | Number of entries, `1` or `2` |
| `+0x0B` | Entry[entry_count] | entries     | See Entry |

### Entry (variable: 11 bytes + list)

| Offset  | Type                   | Field             | Notes |
| ------- | ---------------------- | ----------------- | ----- |
| `+0x00` | u16                    | character_key     | `characterstatic.dbss` character key of a structure monster |
| `+0x02` | u8                     | unknown_02        | `0` on every entry |
| `+0x03` | u16                    | character_key_dup | Equals `character_key` on every entry |
| `+0x05` | u16                    | unknown_05        | Equals the row's `region_key` on every entry |
| `+0x07` | u32                    | character_count   | `5` on every entry |
| `+0x0B` | u16[character_count]   | character_keys    | Character keys, the unused slots `0` (client 3482) |

## Regions (Client 3482)

| Structure monster                  | Listed characters             | Regions |
| ---------------------------------- | ----------------------------- | ------- |
| Olun's Golem `21249`               | `21250`, `21253`              | 958, 1030, 1041, 1058 |
| Turo Totem `21618`, Turo Charm `21617` | `21500`, `21499`          | 965, 967, 1013, 1032, 1034, 1049 |
| Eye of Despair `20411`             | `21630`                       | 962, 1047, 1051 |
| Rift Seed `20000`                  | `21100`, `21105`              | 743 |
| Gyfin Rhasia Tower of Carnage `28470` | `28471`                    | 739, 740 |
| Mirumok Lookout `21634`            | `21635`                       | 729, 732 |
| Jail Alarm Device `22599`          | `22491`                       | 691 |
| Hystria Guard Tower `22489`        | `22598`                       | 689 |
| Aakman Illusion Statue `22595`     | `22597`                       | 688 |
| Argos Obsidian Altar `21141`       | `21140`                       | 622, 625 |
| Cadry Cannon `21660`               | `21666`                       | 579, 631 |
| Cyclops Statue `21696`             | Cyclops `21693`               | 249 |
| Lava Phlogiston Condenser `22896`  | `22493`                       | 418, 420 |

Every listed character has the name of its structure monster, except
Cyclops `21693`. The two Turo entries are always together.

## Field Names

`region_key` resolves to a LOC type 17 region name on all 28 rows, and the
regions hold the structure monsters of their entries (Turo Totem in
Tunkuta, Lava Phlogiston Condenser in Roud Sulfur Works). The character
keys resolve to LOC type 6 names. The file is not in client 1784, no sheet
of a private server's `DataSheets.bexcel` on client 1784 has a column
with `BuffZone` in its name, and no client Lua function on client 3482
reads the table, so the other fields keep `unknown_` names.

## Notes

- The file is in client 2250 and later. Client 2519 has 19 rows, and its
  `character_keys` hold five keys on every entry: the first key repeated
  (`22493` five times), or other keys (`21250, 21068, 21650, 21660,
  21669` for Olun's Golem, where client 2765 and later have `21250, 0, 0,
  0, 0`).

## Open Questions

### What the Listed Characters Are

The listed characters carry the structure monster's name (Olun's Golem
`21250` and `21253` for `21249`), except the Cyclops listed for the
Cyclops Statue. They could be the forms the structure takes while a
monster buff zone is active, or the monsters it summons; the file and
the Lua show neither.

### unknown_02 and unknown_06

`1` and `0` on every row of every client that has the file. Whether
`unknown_02` is a count of something with `unknown_06` its only entry is
open.
