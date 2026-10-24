# `fairyfeedenchantfailcount.bss` Format

## Purpose

The equipment feeding table, compiled from the `FairyFeed_Table` developer
sheet: for each feed key and enhancement level, what feeding a piece of
equipment gives. Each record holds the entries of one `fairy_feed_key`, one
11-byte entry per enhancement level. The field names are the sheet's columns
(see Field Names).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | ----------------- | --------- |
| 1      | 3229 and later | 3483    | `fairyfeedenchantfailcount.bss` | 147   | 9 Entry, 7 Record | 11        |

| Layout | File                            | Known          | Unknown    |
| ------ | ------------------------------- | -------------- | ---------- |
| 1      | `fairyfeedenchantfailcount.bss` | 147 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 1             |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3473   | Layout 1             |
| 3464   | Layout 1             |
| 3458   | Layout 1             |
| 3454   | Layout 1             |
| 3444   | Layout 1             |
| 3435   | Layout 1             |
| 3426   | Layout 1             |
| 3418   | Layout 1             |
| 3412   | Layout 1             |
| 3402   | Layout 1             |
| 3396   | Layout 1             |
| 3387   | Layout 1             |
| 3381   | Layout 1             |
| 3373   | Layout 1             |
| 3364   | Layout 1             |
| 3356   | Layout 1             |
| 3349   | Layout 1             |
| 3342   | Layout 1             |
| 3335   | Layout 1             |
| 3326   | Layout 1             |
| 3321   | Layout 1             |
| 3314   | Layout 1             |
| 3303   | Layout 1             |
| 3302   | Layout 1             |
| 3293   | Layout 1             |
| 3283   | Layout 1             |
| 3275   | Layout 1             |
| 3267   | Layout 1             |
| 3258   | Layout 1             |
| 3251   | Layout 1             |
| 3242   | Layout 1             |
| 3235   | Layout 1             |
| 3229   | Layout 1             |
| 3212   | No file              |
| 3203   | No file              |
| 3193   | No file              |
| 3186   | No file              |
| 3177   | No file              |
| 3169   | No file              |
| 3158   | No file              |
| 3151   | No file              |
| 3144   | No file              |
| 3133   | No file              |
| 3125   | No file              |
| 3118   | No file              |
| 3111   | No file              |
| 3103   | No file              |
| 3095   | No file              |
| 3086   | No file              |
| 3072   | No file              |
| 3062   | No file              |
| 3052   | No file              |
| 3045   | No file              |
| 3037   | No file              |
| 3030   | No file              |
| 3021   | No file              |
| 3012   | No file              |
| 3002   | No file              |
| 2995   | No file              |
| 2987   | No file              |
| 2978   | No file              |
| 2970   | No file              |
| 2959   | No file              |
| 2951   | No file              |
| 2942   | No file              |
| 2935   | No file              |
| 2932   | No file              |
| 2923   | No file              |
| 2919   | No file              |
| 2907   | No file              |
| 2900   | No file              |
| 2891   | No file              |
| 2882   | No file              |
| 2872   | No file              |
| 2863   | No file              |
| 2855   | No file              |
| 2849   | No file              |
| 2844   | No file              |
| 2834   | No file              |
| 2825   | No file              |
| 2819   | No file              |
| 2811   | No file              |
| 2803   | No file              |
| 2794   | No file              |
| 2783   | No file              |
| 2774   | No file              |
| 2765   | No file              |
| 2756   | No file              |
| 2750   | No file              |
| 2743   | No file              |
| 2736   | No file              |
| 2726   | No file              |
| 2717   | No file              |
| 2709   | No file              |
| 2703   | No file              |
| 2695   | No file              |
| 2684   | No file              |
| 2672   | No file              |
| 2665   | No file              |
| 2657   | No file              |
| 2649   | No file              |
| 2644   | No file              |
| 2637   | No file              |
| 2629   | No file              |
| 2619   | No file              |
| 2612   | No file              |
| 2606   | No file              |
| 2602   | No file              |
| 2601   | No file              |
| 2592   | No file              |
| 2583   | No file              |
| 2575   | No file              |
| 2567   | No file              |
| 2560   | No file              |
| 2553   | No file              |
| 2545   | No file              |
| 2538   | No file              |
| 2529   | No file              |
| 2519   | No file              |
| 2513   | No file              |
| 2510   | No file              |
| 2507   | No file              |
| 2503   | No file              |
| 2498   | No file              |
| 2492   | No file              |
| 2487   | No file              |
| 2480   | No file              |
| 2474   | No file              |
| 2468   | No file              |
| 2460   | No file              |
| 2453   | No file              |
| 2444   | No file              |
| 2438   | No file              |
| 2434   | No file              |
| 2429   | No file              |
| 2421   | No file              |
| 2414   | No file              |
| 2407   | No file              |
| 2401   | No file              |
| 2397   | No file              |
| 2393   | No file              |
| 2384   | No file              |
| 2378   | No file              |
| 2372   | No file              |
| 2358   | No file              |
| 2352   | No file              |
| 2347   | No file              |
| 2343   | No file              |
| 2335   | No file              |
| 2327   | No file              |
| 2324   | No file              |
| 2319   | No file              |
| 2313   | No file              |
| 2308   | No file              |
| 2302   | No file              |
| 2295   | No file              |
| 2290   | No file              |
| 2284   | No file              |
| 2276   | No file              |
| 2269   | No file              |
| 2259   | No file              |
| 2250   | No file              |
| 2243   | No file              |
| 2235   | No file              |
| 2229   | No file              |
| 2224   | No file              |
| 2218   | No file              |
| 2215   | No file              |
| 2207   | No file              |
| 2203   | No file              |
| 2196   | No file              |
| 2192   | No file              |
| 2189   | No file              |
| 2183   | No file              |
| 2179   | No file              |
| 2171   | No file              |
| 2163   | No file              |
| 2156   | No file              |
| 2151   | No file              |
| 2147   | No file              |
| 2142   | No file              |
| 2138   | No file              |
| 2134   | No file              |
| 2130   | No file              |
| 2122   | No file              |
| 2107   | No file              |
| 2098   | No file              |
| 2089   | No file              |
| 2081   | No file              |
| 2073   | No file              |
| 2067   | No file              |
| 2063   | No file              |
| 2059   | No file              |
| 2052   | No file              |
| 2044   | No file              |
| 2039   | No file              |
| 2032   | No file              |
| 2025   | No file              |
| 2011   | No file              |
| 2005   | No file              |
| 2000   | No file              |
| 1996   | No file              |
| 1991   | No file              |
| 1985   | No file              |
| 1980   | No file              |
| 1969   | No file              |
| 1964   | No file              |
| 1958   | No file              |
| 1950   | No file              |
| 1945   | No file              |
| 1937   | No file              |
| 1933   | No file              |
| 1927   | No file              |
| 1921   | No file              |
| 1914   | No file              |
| 1908   | No file              |
| 1897   | No file              |
| 1892   | No file              |
| 1886   | No file              |
| 1881   | No file              |
| 1871   | No file              |
| 1866   | No file              |
| 1862   | No file              |
| 1854   | No file              |
| 1846   | No file              |
| 1838   | No file              |
| 1832   | No file              |
| 1826   | No file              |
| 1822   | No file              |
| 1818   | No file              |
| 1804   | No file              |
| 1794   | No file              |
| 1790   | No file              |
| 1784   | No file              |
| 1774   | No file              |
| 1771   | No file              |
| 1762   | No file              |
| 1759   | No file              |
| 1754   | No file              |
| 1749   | No file              |
| 1743   | No file              |
| 1737   | No file              |
| 1731   | No file              |
| 1725   | No file              |
| 1717   | No file              |
| 1710   | No file              |
| 1704   | No file              |
| 1698   | No file              |
| 1690   | No file              |
| 1685   | No file              |
| 1680   | No file              |
| 1674   | No file              |
| 1668   | No file              |
| 1659   | No file              |
| 1649   | No file              |
| 1642   | No file              |
| 1636   | No file              |
| 1628   | No file              |
| 1622   | No file              |
| 1614   | No file              |
| 1608   | No file              |
| 1602   | No file              |
| 1598   | No file              |
| 1594   | No file              |
| 1590   | No file              |
| 1587   | No file              |
| 1584   | No file              |
| 1579   | No file              |
| 1572   | No file              |
| 1565   | No file              |
| 1559   | No file              |
| 1554   | No file              |
| 1547   | No file              |
| 1537   | No file              |
| 1529   | No file              |
| 1524   | No file              |
| 1519   | No file              |
| 1509   | No file              |
| 1506   | No file              |
| 1504   | No file              |
| 1500   | No file              |
| 1493   | No file              |
| 1489   | No file              |
| 1485   | No file              |
| 1481   | No file              |
| 1474   | No file              |
| 1466   | No file              |
| 1462   | No file              |
| 1459   | No file              |
| 1453   | No file              |
| 1450   | No file              |
| 1445   | No file              |
| 1439   | No file              |
| 1433   | No file              |
| 1430   | No file              |
| 1426   | No file              |
| 1421   | No file              |
| 1417   | No file              |
| 1416   | No file              |
| 1409   | No file              |
| 1405   | No file              |
| 1401   | No file              |
| 1396   | No file              |
| 1391   | No file              |
| 1390   | No file              |
| 1386   | No file              |
| 1381   | No file              |
| 1379   | No file              |
| 1372   | No file              |
| 1366   | No file              |
| 1364   | No file              |
| 1363   | No file              |
| 1360   | No file              |
| 1358   | No file              |
| 1355   | No file              |
| 1351   | No file              |
| 1348   | No file              |
| 1346   | No file              |
| 1341   | No file              |
| 1340   | No file              |
| 1338   | No file              |
| 1335   | No file              |
| 1333   | No file              |
| 1329   | No file              |
| 1327   | No file              |
| 1324   | No file              |
| 1321   | No file              |
| 1319   | No file              |
| 1318   | No file              |
| 1316   | No file              |
| 1313   | No file              |
| 1311   | No file              |
| 1309   | No file              |
| 1304   | No file              |
| 1292   | No file              |
| 1286   | No file              |
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No file              |
| 1261   | No file              |
| 1256   | No documented layout |
| 1250   | No documented layout |
| 1246   | No documented layout |
| 1239   | No documented layout |
| 1230   | No documented layout |
| 1226   | No documented layout |
| 1220   | No documented layout |
| 1217   | No documented layout |
| 1211   | No documented layout |
| 1210   | No documented layout |
| 1208   | No documented layout |
| 1203   | No documented layout |
| 1197   | No documented layout |
| 1194   | No documented layout |
| 1192   | No documented layout |
| 1187   | No documented layout |
| 1183   | No documented layout |
| 1177   | No documented layout |
| 1173   | No documented layout |
| 1167   | No documented layout |
| 1164   | No documented layout |
| 1156   | No documented layout |
| 1149   | No documented layout |
| 1144   | No documented layout |
| 1137   | No documented layout |
| 1132   | No documented layout |
| 1127   | No documented layout |
| 1122   | No documented layout |
| 1118   | No documented layout |
| 1114   | No documented layout |
| 1109   | No documented layout |
| 1102   | No file              |
| 1096   | No file              |
| 1088   | No file              |
| 1081   | No file              |
| 1076   | No file              |
| 1069   | No file              |
| 1064   | No file              |
| 1058   | No file              |
| 1051   | No file              |
| 1044   | No file              |
| 1036   | No file              |
| 1026   | No file              |
| 1016   | No file              |
| 1009   | No file              |
| 1005   | No file              |
| 1000   | No file              |
| 998    | No file              |
| 990    | No file              |
| 979    | No file              |
| 972    | No file              |
| 963    | No file              |
| 955    | No file              |
| 946    | No file              |
| 938    | No file              |
| 927    | No file              |
| 911    | No file              |
| 904    | No file              |
| 899    | No file              |
| 894    | No file              |
| 885    | No file              |
| 879    | No file              |
| 872    | No file              |
| 864    | No file              |
| 855    | No file              |
| 853    | No file              |
| 845    | No file              |
| 837    | No file              |
| 829    | No file              |
| 822    | No file              |
| 814    | No file              |
| 805    | No file              |
| 794    | No file              |
| 787    | No file              |
| 780    | No file              |
| 771    | No file              |
| 760    | No file              |
| 748    | No file              |
| 741    | No file              |
| 736    | No file              |
| 731    | No file              |
| 723    | No file              |
| 711    | No file              |
| 707    | No file              |
| 697    | No file              |
| 689    | No file              |
| 683    | No file              |
| 678    | No file              |
| 670    | No file              |
| 661    | No file              |
| 656    | No file              |
| 652    | No file              |
| 643    | No file              |
| 637    | No file              |
| 630    | No file              |
| 627    | No file              |
| 621    | No file              |
| 617    | No file              |
| 615    | No file              |
| 606    | No file              |
| 599    | No file              |
| 592    | No file              |
| 586    | No file              |
| 577    | No file              |
| 569    | No file              |
| 561    | No file              |
| 554    | No file              |
| 542    | No file              |
| 532    | No file              |
| 531    | No file              |
| 526    | No file              |
| 521    | No file              |
| 517    | No file              |
| 510    | No file              |
| 508    | No file              |
| 504    | No file              |
| 497    | No file              |
| 491    | No file              |
| 485    | No file              |
| 478    | No file              |
| 472    | No file              |
| 466    | No file              |
| 457    | No file              |
| 452    | No file              |
| 449    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

None: the file has no `fairyfeedenchantfailcountoffset.dbss`, and no
companion is needed to parse it. Clients 1485 and 1784 ship the same table as
`fairyfeedenchantfailcount.dbss` with an offset index instead (see Field
Names).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type          | Field          | Notes                                        |
| ------------------- | ------------- | -------------- | -------------------------------------------- |
| `+0x00`             | char[4]       | magic          | `PABR` (ASCII)                               |
| `+0x04`             | u32           | count          | Number of records; observed 7 (see Notes)    |
| `+0x08`             | Record[count] | records        | Variable-length records, back to back        |
| `records+0x00`      | String Table  | string_table   | The PABR string table, here with no strings  |
| `string_table+0x00` | u32           | end_of_records | Byte offset just past the last record; observed 135 |
| `string_table+0x04` | u32           | zero           | Always `0`                                   |

Observed file size is 147 bytes: 8-byte header, 127 bytes of records, 12-byte
trailer.

The 12-byte trailer (`string_table`, `end_of_records`, `zero`) is the same
trailer shape used by [fairyupgraderate.bss](fairyupgraderate_bss.md) and
[zodiacsignindex.bss](zodiacsignindex_bss.md).

### Record (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Observed | Notes                              |
| ------- | ------------------ | ----------- | -------- | ---------------------------------- |
| `+0x00` | u32                | entry_count | 1 or 2   | Number of entries that follow      |
| `+0x04` | Entry[entry_count] | entries     |          | `entry_count` × 11-byte entries    |

Records have no key of their own. Every entry in a record repeats the same
`fairy_feed_key`, and on client 3474 that value equals the record index plus
one across all seven records.

### Entry (11 bytes)

| Offset  | Type | Field          | Notes                                                            |
| ------- | ---- | -------------- | ---------------------------------------------------------------- |
| `+0x00` | u16  | fairy_feed_key | `FairyFeedKey`; the same for every entry in a record             |
| `+0x02` | u8   | enchant_level  | `EnchantValue`; enhancement level of the fed item (19 TET, 20 PEN); 0 under keys 3 to 7 |
| `+0x03` | u32  | feed_value     | `FeedValue`                                                      |
| `+0x07` | u32  | equip_exp      | `EquipExp`; a u64 in the 1784 `.dbss`                            |

Earlier versions of this doc called `fairy_feed_key` `unknown_00` (before
that `group_id`), `enchant_level` `unknown_02` (`sub_key`), `feed_value`
`unknown_03` (`value_a`) and `equip_exp` `unknown_07` (`value_b`).

The 11-byte entry is unaligned: `feed_value` starts at an odd offset, so a
parser must read the two u32 fields at `+0x03` and `+0x07` rather than assume
4-byte alignment.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Observed | Notes                       |
| ------- | ------------------ | ------------ | -------- | --------------------------- |
| `+0x00` | u32                | string_count | 0        | Always zero                 |
| `+0x04` | pstr[string_count] | strings      |          | Empty                       |

Earlier versions of this doc called `string_count` the trailer's `unknown_00`
and `zero` its `unknown_08`.

## Decoded Table

All nine entries on client 3474:

| Record | fairy_feed_key | enchant_level | feed_value | equip_exp |
| ------ | -------------- | ------------- | ---------- | --------- |
| 0      | 1              | 19 (TET)      | 0          | 200       |
| 0      | 1              | 20 (PEN)      | 0          | 300       |
| 1      | 2              | 19 (TET)      | 0          | 200       |
| 1      | 2              | 20 (PEN)      | 0          | 300       |
| 2      | 3              | 0             | 100        | 300       |
| 3      | 4              | 0             | 100        | 300       |
| 4      | 5              | 0             | 100        | 300       |
| 5      | 6              | 0             | 100        | 300       |
| 6      | 7              | 0             | 300        | 350       |

The table splits in two. Keys 1 and 2 carry an entry for TET and one for PEN,
both with `feed_value` 0. Keys 3 to 7 carry one entry with `enchant_level` 0
and a non-zero `feed_value`.

## Field Names

The names come from the server dump of a private server on client 1784
(`Instance_dumpFull.exe`). It loads the table twice into one static status,
`FairyFeedEnchantFailCountStaticStatusManager`: from the client's
`FairyFeedEnchantFailCount` binary (row reader at VA `0x140b5b660`, called
from VA `0x140b70433`) and from the `FairyFeed_Table` developer sheet (column
reads at VA `0x14090b999` to `0x14090bac6`). Both write the same members:

| Field            | Member  | Read from the 1784 file | Sheet column   |
| ---------------- | ------- | ----------------------- | -------------- |
| `fairy_feed_key` | `+0x14` | u16                     | `FairyFeedKey` |
| `enchant_level`  | `+0x16` | u8                      | `EnchantValue` |
| `feed_value`     | `+0x10` | u32                     | `FeedValue`    |
| `equip_exp`      | `+0x08` | u64                     | `EquipExp`     |

The reader reads the members in the table's order, and its error message
names the first two: "getXXX key : %# level : %#".

Clients 1485 and 1784 ship the table as `fairyfeedenchantfailcount.dbss`: a
u32 key count, then per key a u32 entry count and 15-byte entries in the
order above. The official files of both clients are byte-identical to each
other and to the private server's copy, and hold the sheet's 28 rows with
every column equal: key 1 at enhancement levels 8 to 20 and key 2 at 6 to
20.

The client 3474 `.bss` keeps that nesting (one record per key, the key
repeated in every entry) and the first three fields at the same offsets and
widths. The entry is 4 bytes shorter, so `equip_exp` is read as a u32. The
values do not match: on the four (key, level) pairs both clients have, keys 1
and 2 at TET and PEN, client 3474 stores `feed_value` 0 and `equip_exp` 200
or 300, where client 1784 stores 50 to 75 and 434,760 to 1,830,510. The names
rest on the reader order and the layout, not on values.

The sheet's cell comments (an English translation in this copy, dated
2019-01-08) say that `FairyFeedKey` matches the column of the same name in
the item sheet, which marks the equipment that can be fed to the Black
Spirit; that `EnchantValue` is the enhancement level; and that `FeedValue`
is the "potential breakthrough stack" an item at that level gives when fed.
`EquipExp` has no comment. The sheet's `#Description` column names the rows
("Weapon potential breakthrough +8" up to PEN for key 1, armor from +6 for
key 2) and is not in the file.

A private server on client 519 has the same sheet without `EquipExp`. Its
`EatEnchantEvent.java` takes weapons from +8 and armor from +6, which are
keys 1 and 2, and adds a fail count by level to the player's enchant fail
count; its hardcoded counts are the sheet's `FeedValue` column on client 519
(34 for a PEN weapon, 30 for PEN armor).

The sibling sheet `FairyFeed_Range` (`Stack`, `StackExp`) goes into a second
static status in the same dump (insert at VA `0x140b70a20`, which logs
"EnchantFailCountExpStaticStatusManager Insert Fail Stack(%#) , NeedExp(%#)").
The client file for it is
[enchantfailcountexpstaticstatus.bss](enchantfailcountexpstaticstatus_bss.md)
(`.dbss` on client 1784). On client 3474 that file is keyed by fail stack
and holds this file's nine (key, level) pairs per stack, each non-zero only
from `feed_value` up to below `equip_exp` (see its Stack Ranges).

The 2016 client PDB has no struct for this table.

## Notes

- The record stream lands exactly on `end_of_records`: `7 × 4 + 9 × 11 = 127`
  bytes of records after the 8-byte header. That exact fit is what confirms the
  4-byte `entry_count` prefix and the 11-byte entry size.
- Records are variable length, so a parser must follow `entry_count` rather than
  assume the 15-byte or 26-byte sizes seen in this file.
- `fairy_feed_key` is redundant with the record index on client 3474, but it
  is stored per entry rather than per record, so it is read from the entry.
- Observed: 7 records and 9 entries in the pre-2026-09-27 fixture and in the
  2026-09-27 client; the file is byte-identical between the two.
- The file stem says fairy; the sheet comments say the equipment is fed to
  the Black Spirit. Nothing in this file links it to
  [fairyupgraderate.bss](fairyupgraderate_bss.md) or
  [fairyfeedingitem.dbss](fairyfeedingitem_dbss.md).
- No LOC lookup applies: every field is a small integer, and none of the values
  match a localization key.

## Open Questions

### Items Under Keys 3 to 7

Keys 1 and 2 are weapons and armor on clients 519 to 1784. Keys 3 to 7 are
new on client 3474 and have `enchant_level` 0, so they key items fed at no
particular level. The item sheet's `FairyFeedKey` column has not been found in
a client item file, so which items carry these keys is open.

### `feed_value` and `equip_exp` as a Stack Range

On client 3474 every entry's `feed_value` and `equip_exp` are the first
stack and one past the last stack at which
[enchantfailcountexpstaticstatus.bss](enchantfailcountexpstaticstatus_bss.md)
holds a non-zero value for that key and level: 0 to 199 for TET, 0 to 299
for PEN, 100 to 299 for keys 3 to 6, 300 to 349 for key 7, with 0 misses
over 3,600 values. The client Lua titles the enchant stack list groups with
a start and end stack (`ToClient_GetStartStackByIndex`,
`ToClient_GetEndStackByIndex`). Whether the client reads these two fields
as that start and end, which would leave the 1784 names wrong for client
3474, is open.

### `equip_exp` Width

The 1784 reader reads `EquipExp` as a u64; the client 3474 entry has room for
a u32 only. No reader for the 3474 file was found, so the narrower field rests
on the entry size alone.
