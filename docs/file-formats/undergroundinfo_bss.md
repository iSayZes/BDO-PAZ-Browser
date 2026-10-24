# `undergroundinfo.bss` Format

## Purpose

The drop areas of the server's underground bitmap. A PABR list of
colours; each row is one colour key of the bitmap and bytes that are `0`
on every row, where the source sheet has a drop ID. On client 3482 it
holds 29 colours. The client 1784 sheet notes name what each area drops:
gold bars, ores and muddy water pouches by level, quest items, and
treasure maps for harpoon fishing.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ------- | --------- |
| 3      | 2726 and later | 3483    | `undergroundinfo.bss` | 368   | 29 Row  | 12        |
| 2      | 805 to 2717    | 2717    | `undergroundinfo.bss` | 310   | 29 Row  | 10        |
| 1      | 435 to 794     | 794     | `undergroundinfo.bss` | 284   | 28 Row  | 10        |

| Layout | File                  | Known         | Unknown       |
| ------ | --------------------- | ------------- | ------------- |
| 3      | `undergroundinfo.bss` | 107 B (29.1%) | 261 B (70.9%) |
| 2      | `undergroundinfo.bss` | 107 B (34.5%) | 203 B (65.5%) |
| 1      | `undergroundinfo.bss` | 88 B (31.0%)  | 196 B (69.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 3 |
| 3482   | Layout 3 |
| 3474   | Layout 3 |
| 3473   | Layout 3 |
| 3464   | Layout 3 |
| 3458   | Layout 3 |
| 3454   | Layout 3 |
| 3444   | Layout 3 |
| 3435   | Layout 3 |
| 3426   | Layout 3 |
| 3418   | Layout 3 |
| 3412   | Layout 3 |
| 3402   | Layout 3 |
| 3396   | Layout 3 |
| 3387   | Layout 3 |
| 3381   | Layout 3 |
| 3373   | Layout 3 |
| 3364   | Layout 3 |
| 3356   | Layout 3 |
| 3349   | Layout 3 |
| 3342   | Layout 3 |
| 3335   | Layout 3 |
| 3326   | Layout 3 |
| 3321   | Layout 3 |
| 3314   | Layout 3 |
| 3303   | Layout 3 |
| 3302   | Layout 3 |
| 3293   | Layout 3 |
| 3283   | Layout 3 |
| 3275   | Layout 3 |
| 3267   | Layout 3 |
| 3258   | Layout 3 |
| 3251   | Layout 3 |
| 3242   | Layout 3 |
| 3235   | Layout 3 |
| 3229   | Layout 3 |
| 3212   | Layout 3 |
| 3203   | Layout 3 |
| 3193   | Layout 3 |
| 3186   | Layout 3 |
| 3177   | Layout 3 |
| 3169   | Layout 3 |
| 3158   | Layout 3 |
| 3151   | Layout 3 |
| 3144   | Layout 3 |
| 3133   | Layout 3 |
| 3125   | Layout 3 |
| 3118   | Layout 3 |
| 3111   | Layout 3 |
| 3103   | Layout 3 |
| 3095   | Layout 3 |
| 3086   | Layout 3 |
| 3072   | Layout 3 |
| 3062   | Layout 3 |
| 3052   | Layout 3 |
| 3045   | Layout 3 |
| 3037   | Layout 3 |
| 3030   | Layout 3 |
| 3021   | Layout 3 |
| 3012   | Layout 3 |
| 3002   | Layout 3 |
| 2995   | Layout 3 |
| 2987   | Layout 3 |
| 2978   | Layout 3 |
| 2970   | Layout 3 |
| 2959   | Layout 3 |
| 2951   | Layout 3 |
| 2942   | Layout 3 |
| 2935   | Layout 3 |
| 2932   | Layout 3 |
| 2923   | Layout 3 |
| 2919   | Layout 3 |
| 2907   | Layout 3 |
| 2900   | Layout 3 |
| 2891   | Layout 3 |
| 2882   | Layout 3 |
| 2872   | Layout 3 |
| 2863   | Layout 3 |
| 2855   | Layout 3 |
| 2849   | Layout 3 |
| 2844   | Layout 3 |
| 2834   | Layout 3 |
| 2825   | Layout 3 |
| 2819   | Layout 3 |
| 2811   | Layout 3 |
| 2803   | Layout 3 |
| 2794   | Layout 3 |
| 2783   | Layout 3 |
| 2774   | Layout 3 |
| 2765   | Layout 3 |
| 2756   | Layout 3 |
| 2750   | Layout 3 |
| 2743   | Layout 3 |
| 2736   | Layout 3 |
| 2726   | Layout 3 |
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
| 2005   | Layout 2 |
| 2000   | Layout 2 |
| 1996   | Layout 2 |
| 1991   | Layout 2 |
| 1985   | Layout 2 |
| 1980   | Layout 2 |
| 1969   | Layout 2 |
| 1964   | Layout 2 |
| 1958   | Layout 2 |
| 1950   | Layout 2 |
| 1945   | Layout 2 |
| 1937   | Layout 2 |
| 1933   | Layout 2 |
| 1927   | Layout 2 |
| 1921   | Layout 2 |
| 1914   | Layout 2 |
| 1908   | Layout 2 |
| 1897   | Layout 2 |
| 1892   | Layout 2 |
| 1886   | Layout 2 |
| 1881   | Layout 2 |
| 1871   | Layout 2 |
| 1866   | Layout 2 |
| 1862   | Layout 2 |
| 1854   | Layout 2 |
| 1846   | Layout 2 |
| 1838   | Layout 2 |
| 1832   | Layout 2 |
| 1826   | Layout 2 |
| 1822   | Layout 2 |
| 1818   | Layout 2 |
| 1804   | Layout 2 |
| 1794   | Layout 2 |
| 1790   | Layout 2 |
| 1784   | Layout 2 |
| 1774   | Layout 2 |
| 1771   | Layout 2 |
| 1762   | Layout 2 |
| 1759   | Layout 2 |
| 1754   | Layout 2 |
| 1749   | Layout 2 |
| 1743   | Layout 2 |
| 1737   | Layout 2 |
| 1731   | Layout 2 |
| 1725   | Layout 2 |
| 1717   | Layout 2 |
| 1710   | Layout 2 |
| 1704   | Layout 2 |
| 1698   | Layout 2 |
| 1690   | Layout 2 |
| 1685   | Layout 2 |
| 1680   | Layout 2 |
| 1674   | Layout 2 |
| 1668   | Layout 2 |
| 1659   | Layout 2 |
| 1649   | Layout 2 |
| 1642   | Layout 2 |
| 1636   | Layout 2 |
| 1628   | Layout 2 |
| 1622   | Layout 2 |
| 1614   | Layout 2 |
| 1608   | Layout 2 |
| 1602   | Layout 2 |
| 1598   | Layout 2 |
| 1594   | Layout 2 |
| 1590   | Layout 2 |
| 1587   | Layout 2 |
| 1584   | Layout 2 |
| 1579   | Layout 2 |
| 1572   | Layout 2 |
| 1565   | Layout 2 |
| 1559   | Layout 2 |
| 1554   | Layout 2 |
| 1547   | Layout 2 |
| 1537   | Layout 2 |
| 1529   | Layout 2 |
| 1524   | Layout 2 |
| 1519   | Layout 2 |
| 1509   | Layout 2 |
| 1506   | Layout 2 |
| 1504   | Layout 2 |
| 1500   | Layout 2 |
| 1493   | Layout 2 |
| 1489   | Layout 2 |
| 1485   | Layout 2 |
| 1481   | Layout 2 |
| 1474   | Layout 2 |
| 1466   | Layout 2 |
| 1462   | Layout 2 |
| 1459   | Layout 2 |
| 1453   | Layout 2 |
| 1450   | Layout 2 |
| 1445   | Layout 2 |
| 1439   | Layout 2 |
| 1433   | Layout 2 |
| 1430   | Layout 2 |
| 1426   | Layout 2 |
| 1421   | Layout 2 |
| 1417   | Layout 2 |
| 1416   | Layout 2 |
| 1409   | Layout 2 |
| 1405   | Layout 2 |
| 1401   | Layout 2 |
| 1396   | Layout 2 |
| 1391   | Layout 2 |
| 1390   | Layout 2 |
| 1386   | Layout 2 |
| 1381   | Layout 2 |
| 1379   | Layout 2 |
| 1372   | Layout 2 |
| 1366   | Layout 2 |
| 1364   | Layout 2 |
| 1363   | Layout 2 |
| 1360   | Layout 2 |
| 1358   | Layout 2 |
| 1355   | Layout 2 |
| 1351   | Layout 2 |
| 1348   | Layout 2 |
| 1346   | Layout 2 |
| 1341   | Layout 2 |
| 1340   | Layout 2 |
| 1338   | Layout 2 |
| 1335   | Layout 2 |
| 1333   | Layout 2 |
| 1329   | Layout 2 |
| 1327   | Layout 2 |
| 1324   | Layout 2 |
| 1321   | Layout 2 |
| 1319   | Layout 2 |
| 1318   | Layout 2 |
| 1316   | Layout 2 |
| 1313   | Layout 2 |
| 1311   | Layout 2 |
| 1309   | Layout 2 |
| 1304   | Layout 2 |
| 1292   | Layout 2 |
| 1286   | Layout 2 |
| 1280   | Layout 2 |
| 1276   | Layout 2 |
| 1267   | Layout 2 |
| 1261   | Layout 2 |
| 1256   | Layout 2 |
| 1250   | Layout 2 |
| 1246   | Layout 2 |
| 1239   | Layout 2 |
| 1230   | Layout 2 |
| 1226   | Layout 2 |
| 1220   | Layout 2 |
| 1217   | Layout 2 |
| 1211   | Layout 2 |
| 1210   | Layout 2 |
| 1208   | Layout 2 |
| 1203   | Layout 2 |
| 1197   | Layout 2 |
| 1194   | Layout 2 |
| 1192   | Layout 2 |
| 1187   | Layout 2 |
| 1183   | Layout 2 |
| 1177   | Layout 2 |
| 1173   | Layout 2 |
| 1167   | Layout 2 |
| 1164   | Layout 2 |
| 1156   | Layout 2 |
| 1149   | Layout 2 |
| 1144   | Layout 2 |
| 1137   | Layout 2 |
| 1132   | Layout 2 |
| 1127   | Layout 2 |
| 1122   | Layout 2 |
| 1118   | Layout 2 |
| 1114   | Layout 2 |
| 1109   | Layout 2 |
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
| 829    | Layout 2 |
| 822    | Layout 2 |
| 814    | Layout 2 |
| 805    | Layout 2 |
| 794    | Layout 1 |
| 787    | Layout 1 |
| 780    | Layout 1 |
| 771    | Layout 1 |
| 760    | Layout 1 |
| 748    | Layout 1 |
| 741    | Layout 1 |
| 736    | Layout 1 |
| 731    | Layout 1 |
| 723    | Layout 1 |
| 711    | Layout 1 |
| 707    | Layout 1 |
| 697    | Layout 1 |
| 689    | Layout 1 |
| 683    | Layout 1 |
| 678    | Layout 1 |
| 670    | Layout 1 |
| 661    | Layout 1 |
| 656    | Layout 1 |
| 652    | Layout 1 |
| 643    | Layout 1 |
| 637    | Layout 1 |
| 630    | Layout 1 |
| 627    | Layout 1 |
| 621    | Layout 1 |
| 617    | Layout 1 |
| 615    | Layout 1 |
| 606    | Layout 1 |
| 599    | Layout 1 |
| 592    | Layout 1 |
| 586    | Layout 1 |
| 577    | Layout 1 |
| 569    | Layout 1 |
| 561    | Layout 1 |
| 554    | Layout 1 |
| 542    | Layout 1 |
| 532    | Layout 1 |
| 531    | Layout 1 |
| 526    | Layout 1 |
| 521    | Layout 1 |
| 517    | Layout 1 |
| 510    | Layout 1 |
| 508    | Layout 1 |
| 504    | Layout 1 |
| 497    | Layout 1 |
| 491    | Layout 1 |
| 485    | Layout 1 |
| 478    | Layout 1 |
| 472    | Layout 1 |
| 466    | Layout 1 |
| 457    | Layout 1 |
| 452    | Layout 1 |
| 449    | Layout 1 |
| 435    | Layout 1 |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Shared Layout

Same layout as [`waterinfo.bss`](waterinfo_bss.md), read by the same
handler: a PABR u32 count of rows, each a 3-byte `color_key` stored blue,
green, red, an unnamed u8 that is always `0` and eight bytes that are
always `0` (six on older layouts), then the string table and the trailer.
Clients up to 794 have no PABR magic, string table or trailer, and clients
up to 504 store a copy of the colour and a u16 drop ID in the six bytes.

## Colours

The `Underground_Table` sheet of a private server's
`datasheet_regiondatatable.xlsm` on client 1784 has 29 rows with a note
each. `color_key` as `rrggbb`, grouped by the sheet note (client 1784):

| `color_key`                                 | Sheet note                                                                         |
| ------------------------------------------- | ---------------------------------------------------------------------------------- |
| `649664`, `643c3c`, `5050c8`                | `레벨1`, `레벨2 드랍`, `레벨3 드랍` (levels 1 to 3): gold bars, ores, muddy water pouches |
| `fac8c8`                                    | `발렌시아 전역` (all of Valencia): the same drops                                   |
| `000064`                                    | `기본` (default): muddy water pouch                                                |
| `c80a0a`, `c80b0b`, `c80c0c`, `c87878`      | `의뢰용` (for quests): one drop item each                                           |
| `c87896`                                    | `북미 트레져 헌터용` (NA treasure hunter)                                           |
| `f42c01` to `f42c0a`                        | `작살낚시 전용 보물 지도 #1` to `#10` (treasure maps for harpoon fishing only)      |
| `2bffee`, `93fff7`, `65fff3`, `4cfff1`, `16ffec`, `00ffea`, `3affef` | `이벤트 의뢰용 # 1` to `# 7` (for event quests)                    |
| `003232`                                    | `히스트리아 의뢰용` (for the Hystria quest)                                         |
| `983535`                                    | `아르티니 승급 의뢰용` (for the Artini promotion quest)                             |

## Field Names

The `Underground_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `R`, `G`, `B` and `DropID`. All 29 of 29 file
colours on clients 1784 and 3482 are sheet rows, with the bytes in blue,
green, red order, and the file order is not the sheet order. The 2016
`gc::UndergroundInfoManager` holds the same `gc::BitmapDropInfo` rows as
`gc::WaterInfoManager`, keyed by `_colorKey`; the names follow
[`waterinfo.bss`](waterinfo_bss.md). On clients 435 and 504 the file holds
20 colours, each with the colour copy and a u16 that equals the client
1784 sheet's `DropID` on 20 of 20 rows. The `Underground_Table` of a
private server on client 519 has 28 of the 29 colours; `983535` is not
there.

## Notes

- On clients 606, 794, 1784 and 3482 every byte after the colour is `0`,
  where the client 1784 sheet has drop IDs `10060` to `10077` and `10881`
  to `10890`, as in `waterinfo.bss`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/server_tables.py`,
  `color_key` as `rrggbb`.
