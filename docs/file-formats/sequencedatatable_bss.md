# `sequencedatatable.bss` Format

## Purpose

Where and when a cutscene starts on its own, and what it runs. Each row
names one cutscene file (`CS_Tutorial_06_EternalWinter_0000.pas`), the
region it belongs to, a start condition script (`checkposition(x, y, z,
radius)`, quest state checks) and two scripts the client runs when the
cutscene starts and ends (`acceptquest`, `completequestcondition`,
`setPosition`). The file holds the `CutsceneBeginningLocationInfo` sheet
plus two columns that sheet did not have yet. It is a PABR table of
27-byte rows whose text sits in the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes  | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ------ | ------- | --------- |
| 2      | 2011 and later | 3483    | `sequencedatatable.bss` | 63,181 | 185 Row | 27        |
| 1      | 1927 to 2005   | 2005    | `sequencedatatable.bss` | 38,651 | 76 Row  | 26        |

| Layout | File                    | Known            | Unknown      |
| ------ | ----------------------- | ---------------- | ------------ |
| 2      | `sequencedatatable.bss` | 62,256 B (98.5%) | 925 B (1.5%) |
| 1      | `sequencedatatable.bss` | 38,347 B (99.2%) | 304 B (0.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3464   | Layout 2 |
| 3458   | Layout 2 |
| 3454   | Layout 2 |
| 3444   | Layout 2 |
| 3435   | Layout 2 |
| 3426   | Layout 2 |
| 3418   | Layout 2 |
| 3412   | Layout 2 |
| 3402   | Layout 2 |
| 3396   | Layout 2 |
| 3387   | Layout 2 |
| 3381   | Layout 2 |
| 3373   | Layout 2 |
| 3364   | Layout 2 |
| 3356   | Layout 2 |
| 3349   | Layout 2 |
| 3342   | Layout 2 |
| 3335   | Layout 2 |
| 3326   | Layout 2 |
| 3321   | Layout 2 |
| 3314   | Layout 2 |
| 3303   | Layout 2 |
| 3302   | Layout 2 |
| 3293   | Layout 2 |
| 3283   | Layout 2 |
| 3275   | Layout 2 |
| 3267   | Layout 2 |
| 3258   | Layout 2 |
| 3251   | Layout 2 |
| 3242   | Layout 2 |
| 3235   | Layout 2 |
| 3229   | Layout 2 |
| 3212   | Layout 2 |
| 3203   | Layout 2 |
| 3193   | Layout 2 |
| 3186   | Layout 2 |
| 3177   | Layout 2 |
| 3169   | Layout 2 |
| 3158   | Layout 2 |
| 3151   | Layout 2 |
| 3144   | Layout 2 |
| 3133   | Layout 2 |
| 3125   | Layout 2 |
| 3118   | Layout 2 |
| 3111   | Layout 2 |
| 3103   | Layout 2 |
| 3095   | Layout 2 |
| 3086   | Layout 2 |
| 3072   | Layout 2 |
| 3062   | Layout 2 |
| 3052   | Layout 2 |
| 3045   | Layout 2 |
| 3037   | Layout 2 |
| 3030   | Layout 2 |
| 3021   | Layout 2 |
| 3012   | Layout 2 |
| 3002   | Layout 2 |
| 2995   | Layout 2 |
| 2987   | Layout 2 |
| 2978   | Layout 2 |
| 2970   | Layout 2 |
| 2959   | Layout 2 |
| 2951   | Layout 2 |
| 2942   | Layout 2 |
| 2935   | Layout 2 |
| 2932   | Layout 2 |
| 2923   | Layout 2 |
| 2919   | Layout 2 |
| 2907   | Layout 2 |
| 2900   | Layout 2 |
| 2891   | Layout 2 |
| 2882   | Layout 2 |
| 2872   | Layout 2 |
| 2863   | Layout 2 |
| 2855   | Layout 2 |
| 2849   | Layout 2 |
| 2844   | Layout 2 |
| 2834   | Layout 2 |
| 2825   | Layout 2 |
| 2819   | Layout 2 |
| 2811   | Layout 2 |
| 2803   | Layout 2 |
| 2794   | Layout 2 |
| 2783   | Layout 2 |
| 2774   | Layout 2 |
| 2765   | Layout 2 |
| 2756   | Layout 2 |
| 2750   | Layout 2 |
| 2743   | Layout 2 |
| 2736   | Layout 2 |
| 2726   | Layout 2 |
| 2717   | Layout 2 |
| 2709   | Layout 2 |
| 2703   | Layout 2 |
| 2695   | Layout 2 |
| 2684   | Layout 2 |
| 2672   | Layout 2 |
| 2665   | Layout 2 |
| 2657   | Layout 2 |
| 2649   | Layout 2 |
| 2644   | Layout 2 |
| 2637   | Layout 2 |
| 2629   | Layout 2 |
| 2619   | Layout 2 |
| 2612   | Layout 2 |
| 2606   | Layout 2 |
| 2602   | Layout 2 |
| 2601   | Layout 2 |
| 2592   | Layout 2 |
| 2583   | Layout 2 |
| 2575   | Layout 2 |
| 2567   | Layout 2 |
| 2560   | Layout 2 |
| 2553   | Layout 2 |
| 2545   | Layout 2 |
| 2538   | Layout 2 |
| 2529   | Layout 2 |
| 2519   | Layout 2 |
| 2513   | Layout 2 |
| 2510   | Layout 2 |
| 2507   | Layout 2 |
| 2503   | Layout 2 |
| 2498   | Layout 2 |
| 2492   | Layout 2 |
| 2487   | Layout 2 |
| 2480   | Layout 2 |
| 2474   | Layout 2 |
| 2468   | Layout 2 |
| 2460   | Layout 2 |
| 2453   | Layout 2 |
| 2444   | Layout 2 |
| 2438   | Layout 2 |
| 2434   | Layout 2 |
| 2429   | Layout 2 |
| 2421   | Layout 2 |
| 2414   | Layout 2 |
| 2407   | Layout 2 |
| 2401   | Layout 2 |
| 2397   | Layout 2 |
| 2393   | Layout 2 |
| 2384   | Layout 2 |
| 2378   | Layout 2 |
| 2372   | Layout 2 |
| 2358   | Layout 2 |
| 2352   | Layout 2 |
| 2347   | Layout 2 |
| 2343   | Layout 2 |
| 2335   | Layout 2 |
| 2327   | Layout 2 |
| 2324   | Layout 2 |
| 2319   | Layout 2 |
| 2313   | Layout 2 |
| 2308   | Layout 2 |
| 2302   | Layout 2 |
| 2295   | Layout 2 |
| 2290   | Layout 2 |
| 2284   | Layout 2 |
| 2276   | Layout 2 |
| 2269   | Layout 2 |
| 2259   | Layout 2 |
| 2250   | Layout 2 |
| 2243   | Layout 2 |
| 2235   | Layout 2 |
| 2229   | Layout 2 |
| 2224   | Layout 2 |
| 2218   | Layout 2 |
| 2215   | Layout 2 |
| 2207   | Layout 2 |
| 2203   | Layout 2 |
| 2196   | Layout 2 |
| 2192   | Layout 2 |
| 2189   | Layout 2 |
| 2183   | Layout 2 |
| 2179   | Layout 2 |
| 2171   | Layout 2 |
| 2163   | Layout 2 |
| 2156   | Layout 2 |
| 2151   | Layout 2 |
| 2147   | Layout 2 |
| 2142   | Layout 2 |
| 2138   | Layout 2 |
| 2134   | Layout 2 |
| 2130   | Layout 2 |
| 2122   | Layout 2 |
| 2107   | Layout 2 |
| 2098   | Layout 2 |
| 2089   | Layout 2 |
| 2081   | Layout 2 |
| 2073   | Layout 2 |
| 2067   | Layout 2 |
| 2063   | Layout 2 |
| 2059   | Layout 2 |
| 2052   | Layout 2 |
| 2044   | Layout 2 |
| 2039   | Layout 2 |
| 2032   | Layout 2 |
| 2025   | Layout 2 |
| 2011   | Layout 2 |
| 2005   | Layout 1 |
| 2000   | Layout 1 |
| 1996   | Layout 1 |
| 1991   | Layout 1 |
| 1985   | Layout 1 |
| 1980   | Layout 1 |
| 1969   | Layout 1 |
| 1964   | Layout 1 |
| 1958   | Layout 1 |
| 1950   | Layout 1 |
| 1945   | Layout 1 |
| 1937   | Layout 1 |
| 1933   | Layout 1 |
| 1927   | Layout 1 |
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

None. The handler names the region with its LOC type 17 name from
`languagedata_*.loc` when it is loaded. The cutscene file stays a name:
the `.pas` cutscenes under `character/cutscene/` and the `.paseqfe`
sequences under `sequence/` have no handler.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of rows                                |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (27 bytes)

| Offset  | Type | Field              | Notes                                                                                                   |
| ------- | ---- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| `+0x00` | u16  | region_key         | `regioninfo.bss` region the cutscene belongs to (`890` Duvencrune Mountain, LOC type 17)                |
| `+0x02` | u32  | file_name_hash     | ASCII key hash (lookup3, seed `0xC5EDE`) of `cutscene_file_name` without `.pas`; matches on every row   |
| `+0x06` | u32  | cutscene_file_name | Index into `strings`: the cutscene file with `.pas` (`CS_Tutorial_06_EternalWinter_0000.pas`); unique   |
| `+0x0A` | u32  | start_condition    | Index into `strings`: the script that must hold for the cutscene to start; empty when none              |
| `+0x0E` | u32  | start_execute      | Index into `strings`: the script run when the cutscene starts; empty on most rows                       |
| `+0x12` | u32  | end_execute        | Index into `strings`: the script run when the cutscene ends                                             |
| `+0x16` | u32  | unknown_16         | Unique per row, `2` to `288` with gaps on client 3482; see Open Questions                                |
| `+0x1A` | u8   | unknown_1a         | `0` or `1`; see Open Questions                                                                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                       |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                           |
| `+0x04` | pstr[string_count] | strings      | UTF-8 file names and scripts; one empty string serves every empty field     |

## Layout 1

The row has no `unknown_1a`.

### Row (26 bytes)

| Offset  | Type | Field              | Notes                                                    |
| ------- | ---- | ------------------ | -------------------------------------------------------- |
| `+0x00` | u16  | region_key         | As in Layout 2                                           |
| `+0x02` | u32  | file_name_hash     | As in Layout 2                                           |
| `+0x06` | u32  | cutscene_file_name | As in Layout 2                                           |
| `+0x0A` | u32  | start_condition    | As in Layout 2                                           |
| `+0x0E` | u32  | start_execute      | As in Layout 2                                           |
| `+0x12` | u32  | end_execute        | As in Layout 2                                           |
| `+0x16` | u32  | unknown_16         | Unique per row; see Notes                                |

## Scripts

The three script fields hold calls joined by `;`. A `!` in front of a
call negates it, and `<or>` splits a condition into alternatives (6 rows).
Counts are rows using each call, client 3482.

| Field             | Calls (rows)                                                                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_condition` | `clearquest` (123), `progressquest` (108), `checkposition` (90), `checkquestcondition` (69), `checkinstancefieldmapkey` (27), `checkreservedplaynewcutscene` (16), `isContentsGroupOpen` (13), `checkclass` (4), `getlevel` (1) |
| `start_execute`   | `acceptquest` (7), `executeonlypartyleaderskip` (3)                                                                                             |
| `end_execute`     | `setPosition` (153), `completequestcondition` (67), `acceptquest` (38), `pushitem` (22), `executereserveplaynewcutscene` (19), `completequest` (6), `executeaicall` (3) |

`checkposition(x, y, z, radius)` takes world coordinates and a radius in
the same units (`500` in 51 of the 90 calls, `300` to `10000` in the rest);
`setPosition(x, y, z, angle)` moves the player when the cutscene ends.
`executereserveplaynewcutscene` in one row's `end_execute` and
`checkreservedplaynewcutscene` in another's `start_condition` chain
cutscenes.

On client 3482 the 185 rows cover 63 regions. `start_condition` is empty
on 68 rows, `start_execute` on 175 and `end_execute` on 1. The file names
group by story: `AbyssEntranceS1` (34), `EternalWinter` (33), `AbyssOneS1`
(31), `AbyssActiveS1` (19), `ReBalenos` (18), `AbyssTerritoryS1` (16),
`Yolunakea` (15), `Tutorial` (7) and 10 more.

## Field Names

`region_key`, `cutscene_file_name`, `start_condition`, `start_execute`
and `end_execute` are the `RegionKey`, `CutsceneFileName`,
`StartCondition`, `StartExecute` and `EndExecute` columns of the
`CutsceneBeginningLocationInfo` sheet in a private server's
`DataSheets.bexcel` on client 1784. The sheet's 10 rows match the 10 rows
of that client's `newcutscenedatatable.bss` in every column. 9 of the 10
file names are in client 3482's file; the region matches on 8 of them and
all four text columns on 4; the other 5 check and grant other quest steps
now (`CS_Tutorial_01_EternalWinter_0000` added `isContentsGroupOpen(0,8)`
and checks on four more quests). The sheet stores the file name without
`.pas`; both clients' files add it. The sheet's `#RegionName` note column names each
start place (`드벤크룬 산 : 깨어났을 때`, Duvencrune Mountain: on waking up).
`file_name_hash` is not a sheet column; the hash matches the name on all
185 rows of client 3482.

## Notes

- Client 1784 has no `sequencedatatable.bss`. Its
  `newcutscenedatatable.bss` holds the sheet's rows as 22-byte rows: the
  fields up to `end_execute`. The test clients have
  `sequencedatatable.bss` in its place from client 1927, with 26-byte rows
  (Layout 1, `unknown_16` added) up to client 2005 and 27-byte rows
  (`unknown_1a` added) from client 2011.
- `unknown_16` keeps its number per file name across clients: the 61
  names client 1927 shares with client 3482 all have the same number, and
  142 of the 143 client 2011 shares
  (`CS_AbyssEntranceS1_53_LightScattering_00` moved from `191` to `242`).
- On client 3482, 114 of the file names are both a `character/cutscene/`
  `.pas` and a `sequence/` `.paseqfe` file of the same name (lower case),
  the other 71 only a `.pas`.
- Rows are in no key order: the file opens with
  `CS_Tutorial_06_EternalWinter_0000` (`unknown_16` `7`), then
  `CS_EternalWinter_50_RabreDDuk6_0000` (`43`).

## Open Questions

### What `unknown_16` Is

The u32 is unique per row and runs `2` to `288` with gaps; sorted by it,
the rows fall into story groups in release order (`2` to `47` Eternal
Winter and the Duvencrune tutorial, `50` to `69` Balenos, `105` to `245`
the Abyss chapters, `246` to `260` Yolunakea, `274` up the later
regions), and a file keeps its number across clients (Notes). It looks
like a key the source sheet gained after client 1784, but no other table
read so far points at these numbers.

### What `unknown_1a` Marks

`1` on 40 rows of client 3482, `0` on 145. The `1` rows are all 34
`AbyssEntranceS1` cutscenes and 6 of the 31 `AbyssOneS1` ones; 33 of the
40 have no start condition, but 35 `0` rows have none either, and the flag
does not follow the `.pas` or `.paseqfe` split.
