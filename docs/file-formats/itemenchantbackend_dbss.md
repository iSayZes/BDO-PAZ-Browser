# `itemenchantbackend.dbss` Format

## Purpose

The back part of every [`itemenchant.dbss`](itemenchant_dbss.md) block: for
each (item, enchant level) the bytes from Message Tail `+0x2B` to the end of
the block, which holds `item_access_level`, the undecoded remainder, the
packed key and the crystal group. The front part, from the key to
`life_restrict_type`, is in
[`itemenchantbackendtest.dbss`](itemenchantbackendtest_dbss.md); that doc
has how the three files fit together. `itemenchantbackendoffset.dbss` indexes
the blocks with the keys of `itemenchantoffset.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes       | Records            | Row bytes                    |
| ------ | -------------- | ------- | ------------------------------- | ----------- | ------------------ | ---------------------------- |
| 1      | 1964 and later | 3483    | `itemenchantbackend.dbss`       | 126,919,140 | 169,345 Block      | 320 to 4,484, 749 on average |
| 1      | 1964 and later | 3483    | `itemenchantbackendoffset.dbss` | 2,032,160   | 169,345 Offset Row | 12                           |

| Layout | File                            | Known                | Unknown               |
| ------ | ------------------------------- | -------------------- | --------------------- |
| 1      | `itemenchantbackend.dbss`       | 1,185,419 B (0.9%)   | 125,733,721 B (99.1%) |
| 1      | `itemenchantbackendoffset.dbss` | 2,032,160 B (100.0%) | 0 B (0.0%)            |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3251   | Layout 1 |
| 2335   | Layout 1 |
| 2327   | Layout 1 |
| 2324   | Layout 1 |
| 2319   | Layout 1 |
| 2313   | Layout 1 |
| 2308   | Layout 1 |
| 2302   | Layout 1 |
| 2295   | Layout 1 |
| 2290   | Layout 1 |
| 2284   | Layout 1 |
| 2276   | Layout 1 |
| 2269   | Layout 1 |
| 2259   | Layout 1 |
| 2250   | Layout 1 |
| 2243   | Layout 1 |
| 2235   | Layout 1 |
| 2229   | Layout 1 |
| 2224   | Layout 1 |
| 2218   | Layout 1 |
| 2215   | Layout 1 |
| 2207   | Layout 1 |
| 2203   | Layout 1 |
| 2196   | Layout 1 |
| 2192   | Layout 1 |
| 2189   | Layout 1 |
| 2183   | Layout 1 |
| 2179   | Layout 1 |
| 2171   | Layout 1 |
| 2163   | Layout 1 |
| 2156   | Layout 1 |
| 2151   | Layout 1 |
| 2147   | Layout 1 |
| 2142   | Layout 1 |
| 2138   | Layout 1 |
| 2134   | Layout 1 |
| 2130   | Layout 1 |
| 2122   | Layout 1 |
| 2107   | Layout 1 |
| 2098   | Layout 1 |
| 2089   | Layout 1 |
| 2081   | Layout 1 |
| 2073   | Layout 1 |
| 2067   | Layout 1 |
| 2063   | Layout 1 |
| 2059   | Layout 1 |
| 2052   | Layout 1 |
| 2044   | Layout 1 |
| 2039   | Layout 1 |
| 2032   | Layout 1 |
| 2025   | Layout 1 |
| 2011   | Layout 1 |
| 2005   | Layout 1 |
| 2000   | Layout 1 |
| 1996   | Layout 1 |
| 1991   | Layout 1 |
| 1985   | Layout 1 |
| 1980   | Layout 1 |
| 1969   | Layout 1 |
| 1964   | Layout 1 |
| 1958   | No file  |
| 1950   | No file  |
| 1945   | No file  |
| 1937   | No file  |
| 1933   | No file  |
| 1927   | No file  |
| 1921   | No file  |
| 1914   | No file  |
| 1908   | No file  |
| 1897   | No file  |
| 1892   | No file  |
| 1886   | No file  |
| 1881   | No file  |
| 1871   | No file  |
| 1866   | No file  |
| 1862   | No file  |
| 1854   | No file  |
| 1846   | No file  |
| 1838   | No file  |
| 1832   | No file  |
| 1826   | No file  |
| 1822   | No file  |
| 1818   | No file  |
| 1804   | No file  |
| 1794   | No file  |
| 1790   | No file  |
| 1784   | No file  |
| 1774   | No file  |
| 1771   | No file  |
| 1762   | No file  |
| 1759   | No file  |
| 1754   | No file  |
| 1749   | No file  |
| 1743   | No file  |
| 1737   | No file  |
| 1731   | No file  |
| 1725   | No file  |
| 1717   | No file  |
| 1710   | No file  |
| 1704   | No file  |
| 1698   | No file  |
| 1690   | No file  |
| 1685   | No file  |
| 1680   | No file  |
| 1674   | No file  |
| 1668   | No file  |
| 1659   | No file  |
| 1649   | No file  |
| 1642   | No file  |
| 1636   | No file  |
| 1628   | No file  |
| 1622   | No file  |
| 1614   | No file  |
| 1608   | No file  |
| 1602   | No file  |
| 1598   | No file  |
| 1594   | No file  |
| 1590   | No file  |
| 1587   | No file  |
| 1584   | No file  |
| 1579   | No file  |
| 1572   | No file  |
| 1565   | No file  |
| 1559   | No file  |
| 1554   | No file  |
| 1547   | No file  |
| 1537   | No file  |
| 1529   | No file  |
| 1524   | No file  |
| 1519   | No file  |
| 1509   | No file  |
| 1506   | No file  |
| 1504   | No file  |
| 1500   | No file  |
| 1493   | No file  |
| 1489   | No file  |
| 1485   | No file  |
| 1481   | No file  |
| 1474   | No file  |
| 1466   | No file  |
| 1462   | No file  |
| 1459   | No file  |
| 1453   | No file  |
| 1450   | No file  |
| 1445   | No file  |
| 1439   | No file  |
| 1433   | No file  |
| 1430   | No file  |
| 1426   | No file  |
| 1421   | No file  |
| 1417   | No file  |
| 1416   | No file  |
| 1409   | No file  |
| 1405   | No file  |
| 1401   | No file  |
| 1396   | No file  |
| 1391   | No file  |
| 1390   | No file  |
| 1386   | No file  |
| 1381   | No file  |
| 1379   | No file  |
| 1372   | No file  |
| 1366   | No file  |
| 1364   | No file  |
| 1363   | No file  |
| 1360   | No file  |
| 1358   | No file  |
| 1355   | No file  |
| 1351   | No file  |
| 1348   | No file  |
| 1346   | No file  |
| 1341   | No file  |
| 1340   | No file  |
| 1338   | No file  |
| 1335   | No file  |
| 1333   | No file  |
| 1329   | No file  |
| 1327   | No file  |
| 1324   | No file  |
| 1321   | No file  |
| 1319   | No file  |
| 1318   | No file  |
| 1316   | No file  |
| 1313   | No file  |
| 1311   | No file  |
| 1309   | No file  |
| 1304   | No file  |
| 1292   | No file  |
| 1286   | No file  |
| 1280   | No file  |
| 1276   | No file  |
| 1267   | No file  |
| 1261   | No file  |
| 1256   | No file  |
| 1250   | No file  |
| 1246   | No file  |
| 1239   | No file  |
| 1230   | No file  |
| 1226   | No file  |
| 1220   | No file  |
| 1217   | No file  |
| 1211   | No file  |
| 1210   | No file  |
| 1208   | No file  |
| 1203   | No file  |
| 1197   | No file  |
| 1194   | No file  |
| 1192   | No file  |
| 1187   | No file  |
| 1183   | No file  |
| 1177   | No file  |
| 1173   | No file  |
| 1167   | No file  |
| 1164   | No file  |
| 1156   | No file  |
| 1149   | No file  |
| 1144   | No file  |
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

| File                            | Required | Role                                                                                     |
| ------------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `itemenchantbackendoffset.dbss` | Required | Maps the packed key to a block offset and size                                           |
| `languagedata_en.loc`           | Optional | Item name for the item ID (`str_type=0`)                                                 |
| `jewelgroupstaticstatus.bss`    | Optional | Crystal group name and preset limit for `crystal_group`; without it the column shows the number |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes |
| ------- | ------------ | ------ | ----- |
| `+0x00` | u32          | count  | Block count, matching the companion |
| `+0x04` | Block[count] | blocks | Contiguous, in the order of the companion rows; the last block ends at the end of the file |

### Block (variable: 54 bytes, size from `itemenchantbackendoffset.dbss`)

The offsets in `itemenchant.dbss` are Message Tail `+0x2B` for `unknown_00`
and `+0x5A` for `item_access_level`; the remainder and the two fields at
the end are the same bytes there.

| Offset     | Type        | Field             | Notes |
| ---------- | ----------- | ----------------- | ----- |
| `+0x00`    | bytes[47]   | unknown_00        | `unknown_2b` in `itemenchant.dbss`. Bytes `0x03` to `0x2D` are `0x77` in all 70,826 base blocks (client 3483); bytes `0x00` to `0x02` are `0x77` in 67,056 of them, and hold small values such as `0x18 0x19` in the rest |
| `+0x2F`    | u8          | item_access_level | 2016 `_itemAccessLevel`, see Field Names in `itemenchant_dbss.md`. On client 3483: `0` (31,713 base items), `1` (21,179), `10` (12,389), `99` (3,204), `20` (2,298), and `15`, `19` and `40` on 41 more |
| `+0x30`    | bytes[rest] | unknown_30        | Undecoded, `unknown_after_message_tail` in `itemenchant.dbss`; 266 to 4,430 bytes (client 3483) |
| `end-0x06` | u32         | key               | The packed key of the offset row, `enchant_level << 24 \| item_id`, in every block (client 3483); `key_dup` in `itemenchant.dbss` |
| `end-0x02` | u16         | crystal_group     | The crystal's [jewelgroupstaticstatus.bss](jewelgroupstaticstatus_bss.md) group; `0xFFFF` on everything else and on every higher level |

### `itemenchantbackendoffset.dbss`

The layout of `itemenchantoffset.dbss`, with the same keys in the same
order (169,345 rows on client 3483).

| Offset              | Type              | Field        | Notes |
| ------------------- | ----------------- | ------------ | ----- |
| `+0x00`             | char[4]           | magic        | `PABR` (ASCII) |
| `+0x04`             | u32               | count        | Number of rows |
| `+0x08`             | Offset Row[count] | rows         | `count` × 12-byte rows |
| `rows+0x00`         | String Table      | string_table | The PABR string table, here with no strings |
| `string_table+0x00` | u32               | end_of_rows  | Equals `8 + count × 12` |
| `string_table+0x04` | u32               | zero         | Always zero |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes |
| ------- | ---- | ----------- | ----- |
| `+0x00` | u32  | key         | Packed item ID and enchant level, see Key Packing in `itemenchant_dbss.md` |
| `+0x04` | u32  | data_offset | Byte offset of the block in `itemenchantbackend.dbss` |
| `+0x08` | u32  | data_size   | Block length in bytes |

Rows are contiguous: `data_offset + data_size` of one row equals the next
row's `data_offset`. For every key, `data_size` is the `itemenchant.dbss`
block size less the `itemenchantbackendtest.dbss` block size (client 3483).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` in observed data |
| `+0x04` | pstr[string_count] | strings      | PABR string-table entries |

## Notes

- The doc check fits Layout 1 back to client 1964 because the block is
  mostly `bytes[rest]`: on those clients it confirms the offset rows and the
  key at `end-0x06` only. Where the split point and `item_access_level` sit
  in their blocks is checked on client 3483 only; the `itemenchant.dbss`
  layout before client 3473 is not documented.
- The `itemenchant.dbss` doc decodes nothing between `item_access_level`
  and `key_dup` beyond the scan for `second_string`, so this file's known
  bytes are the 7 named ones per block. What the remainder holds, and why
  the client data stores the blocks a second time split in two, are open
  (Open Questions in `itemenchant_dbss.md` and
  `itemenchantbackendtest_dbss.md`).
