# `worldmapmonster.dbss` Format

## Purpose

The monster markers of the world map: hunting zones, field and world bosses,
Black Shrine bosses, Abyssal Wells and the Pilgrim's Sanctum spots. One
variable-length record per marker with two Korean label lines and a name, the
world position, the marker illustration and an optional condition script.
LOC type 40 holds the translations.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes  | Records                       | Row bytes                  |
| ------ | -------------- | ------- | ---------------------------- | ------ | ----------------------------- | -------------------------- |
| 2      | 3251 and later | 3483    | `worldmapmonster.dbss`       | 43,034 | 231 Marker Record, 231 Record | 138 to 277, 184 on average |
| 2      | 3251 and later | 3483    | `worldmapmonsteroffset.dbss` | 2,314  | 231 Offset Row                | 10                         |
| 1      | 1565 to 1908   | 1908    | `worldmapmonster.dbss`       | 18,285 | 119 Marker Record, 119 Record | 124 to 214, 152 on average |
| 1      | 1565 to 1908   | 1908    | `worldmapmonsteroffset.dbss` | 1,194  | 119 Offset Row                | 10                         |

| Layout | File                         | Known            | Unknown        |
| ------ | ---------------------------- | ---------------- | -------------- |
| 2      | `worldmapmonster.dbss`       | 39,569 B (91.9%) | 3,465 B (8.1%) |
| 2      | `worldmapmonsteroffset.dbss` | 2,314 B (100.0%) | 0 B (0.0%)     |
| 1      | `worldmapmonster.dbss`       | 17,333 B (94.8%) | 952 B (5.2%)   |
| 1      | `worldmapmonsteroffset.dbss` | 1,194 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 2             |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3464   | Layout 2             |
| 3458   | Layout 2             |
| 3454   | Layout 2             |
| 3444   | Layout 2             |
| 3435   | Layout 2             |
| 3426   | Layout 2             |
| 3418   | Layout 2             |
| 3412   | Layout 2             |
| 3402   | Layout 2             |
| 3396   | Layout 2             |
| 3387   | Layout 2             |
| 3381   | Layout 2             |
| 3373   | Layout 2             |
| 3364   | Layout 2             |
| 3356   | Layout 2             |
| 3349   | Layout 2             |
| 3342   | Layout 2             |
| 3335   | Layout 2             |
| 3326   | Layout 2             |
| 3321   | Layout 2             |
| 3314   | Layout 2             |
| 3303   | Layout 2             |
| 3302   | Layout 2             |
| 3293   | Layout 2             |
| 3283   | Layout 2             |
| 3275   | Layout 2             |
| 3267   | Layout 2             |
| 3258   | Layout 2             |
| 3251   | Layout 2             |
| 3242   | No documented layout |
| 3235   | No documented layout |
| 3229   | No documented layout |
| 3212   | No documented layout |
| 3203   | No documented layout |
| 3193   | No documented layout |
| 3186   | No documented layout |
| 3177   | No documented layout |
| 3169   | No documented layout |
| 3158   | No documented layout |
| 3151   | No documented layout |
| 3144   | No documented layout |
| 3133   | No documented layout |
| 3125   | No documented layout |
| 3118   | No documented layout |
| 3111   | No documented layout |
| 3103   | No documented layout |
| 3095   | No documented layout |
| 3086   | No documented layout |
| 3072   | No documented layout |
| 3062   | No documented layout |
| 3052   | No documented layout |
| 3045   | No documented layout |
| 3037   | No documented layout |
| 3030   | No documented layout |
| 3021   | No documented layout |
| 3012   | No documented layout |
| 3002   | No documented layout |
| 2995   | No documented layout |
| 2987   | No documented layout |
| 2978   | No documented layout |
| 2970   | No documented layout |
| 2959   | No documented layout |
| 2951   | No documented layout |
| 2942   | No documented layout |
| 2935   | No documented layout |
| 2932   | No documented layout |
| 2923   | No documented layout |
| 2919   | No documented layout |
| 2907   | No documented layout |
| 2900   | No documented layout |
| 2891   | No documented layout |
| 2882   | No documented layout |
| 2872   | No documented layout |
| 2863   | No documented layout |
| 2855   | No documented layout |
| 2849   | No documented layout |
| 2844   | No documented layout |
| 2834   | No documented layout |
| 2825   | No documented layout |
| 2819   | No documented layout |
| 2811   | No documented layout |
| 2803   | No documented layout |
| 2794   | No documented layout |
| 2783   | No documented layout |
| 2774   | No documented layout |
| 2765   | No documented layout |
| 2756   | No documented layout |
| 2750   | No documented layout |
| 2743   | No documented layout |
| 2736   | No documented layout |
| 2726   | No documented layout |
| 2717   | No documented layout |
| 2709   | No documented layout |
| 2703   | No documented layout |
| 2695   | No documented layout |
| 2684   | No documented layout |
| 2672   | No documented layout |
| 2665   | No documented layout |
| 2657   | No documented layout |
| 2649   | No documented layout |
| 2644   | No documented layout |
| 2637   | No documented layout |
| 2629   | No documented layout |
| 2619   | No documented layout |
| 2612   | No documented layout |
| 2606   | No documented layout |
| 2602   | No documented layout |
| 2601   | No documented layout |
| 2592   | No documented layout |
| 2583   | No documented layout |
| 2575   | No documented layout |
| 2567   | No documented layout |
| 2560   | No documented layout |
| 2553   | No documented layout |
| 2545   | No documented layout |
| 2538   | No documented layout |
| 2529   | No documented layout |
| 2519   | No documented layout |
| 2513   | No documented layout |
| 2510   | No documented layout |
| 2507   | No documented layout |
| 2503   | No documented layout |
| 2498   | No documented layout |
| 2492   | No documented layout |
| 2487   | No documented layout |
| 2480   | No documented layout |
| 2474   | No documented layout |
| 2468   | No documented layout |
| 2460   | No documented layout |
| 2453   | No documented layout |
| 2444   | No documented layout |
| 2438   | No documented layout |
| 2434   | No documented layout |
| 2429   | No documented layout |
| 2421   | No documented layout |
| 2414   | No documented layout |
| 2407   | No documented layout |
| 2401   | No documented layout |
| 2397   | No documented layout |
| 2393   | No documented layout |
| 2384   | No documented layout |
| 2378   | No documented layout |
| 2372   | No documented layout |
| 2358   | No documented layout |
| 2352   | No documented layout |
| 2347   | No documented layout |
| 2343   | No documented layout |
| 2335   | No documented layout |
| 2327   | No documented layout |
| 2324   | No documented layout |
| 2319   | No documented layout |
| 2313   | No documented layout |
| 2308   | No documented layout |
| 2302   | No documented layout |
| 2295   | No documented layout |
| 2290   | No documented layout |
| 2284   | No documented layout |
| 2276   | No documented layout |
| 2269   | No documented layout |
| 2259   | No documented layout |
| 2250   | No documented layout |
| 2243   | No documented layout |
| 2235   | No documented layout |
| 2229   | No documented layout |
| 2224   | No documented layout |
| 2218   | No documented layout |
| 2215   | No documented layout |
| 2207   | No documented layout |
| 2203   | No documented layout |
| 2196   | No documented layout |
| 2192   | No documented layout |
| 2189   | No documented layout |
| 2183   | No documented layout |
| 2179   | No documented layout |
| 2171   | No documented layout |
| 2163   | No documented layout |
| 2156   | No documented layout |
| 2151   | No documented layout |
| 2147   | No documented layout |
| 2142   | No documented layout |
| 2138   | No documented layout |
| 2134   | No documented layout |
| 2130   | No documented layout |
| 2122   | No documented layout |
| 2107   | No documented layout |
| 2098   | No documented layout |
| 2089   | No documented layout |
| 2081   | No documented layout |
| 2073   | No documented layout |
| 2067   | No documented layout |
| 2063   | No documented layout |
| 2059   | No documented layout |
| 2052   | No documented layout |
| 2044   | No documented layout |
| 2039   | No documented layout |
| 2032   | No documented layout |
| 2025   | No documented layout |
| 2011   | No documented layout |
| 2005   | No documented layout |
| 2000   | No documented layout |
| 1996   | No documented layout |
| 1991   | No documented layout |
| 1985   | No documented layout |
| 1980   | No documented layout |
| 1969   | No documented layout |
| 1964   | No documented layout |
| 1958   | No documented layout |
| 1950   | No documented layout |
| 1945   | No documented layout |
| 1937   | No documented layout |
| 1933   | No documented layout |
| 1927   | No documented layout |
| 1921   | No documented layout |
| 1914   | No documented layout |
| 1908   | Layout 1             |
| 1897   | Layout 1             |
| 1892   | Layout 1             |
| 1886   | Layout 1             |
| 1881   | Layout 1             |
| 1871   | Layout 1             |
| 1866   | Layout 1             |
| 1862   | Layout 1             |
| 1854   | Layout 1             |
| 1846   | Layout 1             |
| 1838   | Layout 1             |
| 1832   | Layout 1             |
| 1826   | Layout 1             |
| 1822   | Layout 1             |
| 1818   | Layout 1             |
| 1804   | Layout 1             |
| 1794   | Layout 1             |
| 1790   | Layout 1             |
| 1784   | Layout 1             |
| 1774   | Layout 1             |
| 1771   | Layout 1             |
| 1762   | Layout 1             |
| 1759   | Layout 1             |
| 1754   | Layout 1             |
| 1749   | Layout 1             |
| 1743   | Layout 1             |
| 1737   | Layout 1             |
| 1731   | Layout 1             |
| 1725   | Layout 1             |
| 1717   | Layout 1             |
| 1710   | Layout 1             |
| 1704   | Layout 1             |
| 1698   | Layout 1             |
| 1690   | Layout 1             |
| 1685   | Layout 1             |
| 1680   | Layout 1             |
| 1674   | Layout 1             |
| 1668   | Layout 1             |
| 1659   | Layout 1             |
| 1649   | Layout 1             |
| 1642   | Layout 1             |
| 1636   | Layout 1             |
| 1628   | Layout 1             |
| 1622   | Layout 1             |
| 1614   | Layout 1             |
| 1608   | Layout 1             |
| 1602   | Layout 1             |
| 1598   | Layout 1             |
| 1594   | Layout 1             |
| 1590   | Layout 1             |
| 1587   | Layout 1             |
| 1584   | Layout 1             |
| 1579   | Layout 1             |
| 1572   | Layout 1             |
| 1565   | Layout 1             |
| 1559   | No documented layout |
| 1554   | No documented layout |
| 1547   | No documented layout |
| 1537   | No documented layout |
| 1529   | No documented layout |
| 1524   | No documented layout |
| 1519   | No documented layout |
| 1509   | No documented layout |
| 1506   | No documented layout |
| 1504   | No documented layout |
| 1500   | No documented layout |
| 1493   | No documented layout |
| 1489   | No documented layout |
| 1485   | No documented layout |
| 1481   | No documented layout |
| 1474   | No documented layout |
| 1466   | No documented layout |
| 1462   | No documented layout |
| 1459   | No documented layout |
| 1453   | No documented layout |
| 1450   | No documented layout |
| 1445   | No documented layout |
| 1439   | No documented layout |
| 1433   | No documented layout |
| 1430   | No documented layout |
| 1426   | No documented layout |
| 1421   | No documented layout |
| 1417   | No documented layout |
| 1416   | No documented layout |
| 1409   | No documented layout |
| 1405   | No documented layout |
| 1401   | No documented layout |
| 1396   | No documented layout |
| 1391   | No documented layout |
| 1390   | No documented layout |
| 1386   | No documented layout |
| 1381   | No documented layout |
| 1379   | No documented layout |
| 1372   | No documented layout |
| 1366   | No documented layout |
| 1364   | No documented layout |
| 1363   | No documented layout |
| 1360   | No documented layout |
| 1358   | No documented layout |
| 1355   | No documented layout |
| 1351   | No documented layout |
| 1348   | No documented layout |
| 1346   | No documented layout |
| 1341   | No documented layout |
| 1340   | No documented layout |
| 1338   | No documented layout |
| 1335   | No documented layout |
| 1333   | No documented layout |
| 1329   | No documented layout |
| 1327   | No documented layout |
| 1324   | No documented layout |
| 1321   | No documented layout |
| 1319   | No documented layout |
| 1318   | No documented layout |
| 1316   | No documented layout |
| 1313   | No documented layout |
| 1311   | No documented layout |
| 1309   | No documented layout |
| 1304   | No documented layout |
| 1292   | No documented layout |
| 1286   | No documented layout |
| 1280   | No documented layout |
| 1276   | No file              |
| 1267   | No file              |
| 1261   | No file              |
| 1256   | No file              |
| 1250   | No file              |
| 1246   | No file              |
| 1239   | No file              |
| 1230   | No file              |
| 1226   | No file              |
| 1220   | No file              |
| 1217   | No file              |
| 1211   | No file              |
| 1210   | No file              |
| 1208   | No file              |
| 1203   | No file              |
| 1197   | No file              |
| 1194   | No file              |
| 1192   | No file              |
| 1187   | No file              |
| 1183   | No file              |
| 1177   | No file              |
| 1173   | No file              |
| 1167   | No file              |
| 1164   | No file              |
| 1156   | No file              |
| 1149   | No file              |
| 1144   | No file              |
| 1137   | No file              |
| 1132   | No file              |
| 1127   | No file              |
| 1122   | No file              |
| 1118   | No file              |
| 1114   | No file              |
| 1109   | No file              |
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

| File                         | Required | Role                                                                 |
| ---------------------------- | -------- | -------------------------------------------------------------------- |
| `worldmapmonsteroffset.dbss` | Required | Bare u16-keyed index: marker key -> record offset and size           |
| `languagedata_en.loc`        | Optional | LOC type 40, `str_id1` = key, `str_id4` 0 / 1 / 2 = name / line 1 / line 2 |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                          |
| ------- | ------------- | ------- | ------------------------------ |
| `+0x00` | u32           | count   | Same count as the offset table |
| `+0x04` | Record[count] | records | See Record                     |

### Record (variable: 2 bytes + marker text)

Each record is preceded by a copy of its u16 key. The offset of a row points
past that preceding copy, at the record's own key.

| Offset  | Type          | Field      | Notes                                                    |
| ------- | ------------- | ---------- | -------------------------------------------------------- |
| `+0x00` | u16           | key_prefix | Copy of the marker's `key`                               |
| `+0x02` | Marker Record | marker     | `size` bytes of the offset row; the offset row points here |

### Marker Record (variable: 69 bytes + text)

Strings are a u64 unit count followed by the text, with no terminator: UTF-16LE
for the wide ones, ASCII for the icon path (`RecordReader`).

| Offset             | Type   | Field        | Notes                                                                 |
| ------------------ | ------ | ------------ | --------------------------------------------------------------------- |
| `+0x00`            | u16    | key          | Same as the offset row                                                |
| `+0x02`            | str16  | line1_kr     | First label line: a level range (`Lv 12~15`), a recommended AP, or a category (`월드 우두머리`, world boss) |
| `line1_kr+0x00`    | str16  | line2_kr     | Second label line: the final AP, or the same text as line 1 (142 records) |
| `line2_kr+0x00`    | str16  | name_kr      | Zone or boss name                                                     |
| `name_kr+0x00`     | f32[3] | position     | World position; the second value is the height                        |
| `name_kr+0x0C`     | str8   | icon         | Marker illustration relative to `ui_texture/`; empty on the 16 Abyssal Wells |
| `icon+0x00`        | str16  | condition    | Condition script, empty on 165 records (`getknowledge(10497);`, `!checkFieldType(hadumField);`, `getlevel()>59;`) |
| `condition+0x00`   | str16  | unknown_str  | Always empty                                                          |
| `unknown_str+0x00` | i32    | unknown_ref  | `-1` on 120 records; on hunting zones the drop window hunting ground ID, see Notes |
| `unknown_str+0x04` | u8     | unknown_kind | 0 to 4, groups the markers; see Open Questions                        |
| `unknown_str+0x05` | u8     | unknown_flag | Always `1`                                                            |
| `unknown_str+0x06` | u8     | unknown_end  | Always `0`                                                            |

### `worldmapmonsteroffset.dbss`

No magic and no trailer (`parse_bare_offset_rows()`).

| Offset  | Type              | Field | Notes                              |
| ------- | ----------------- | ----- | ---------------------------------- |
| `+0x00` | u32               | count | Number of rows; 229 on client 3458 |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                     |

The rows are not in file order: they interleave the regular keys (1 to 249)
with the 20 keys from 10001 to 10020, both counting down.

### Offset Row (10 bytes)

| Offset  | Type | Field  | Notes                                                       |
| ------- | ---- | ------ | ----------------------------------------------------------- |
| `+0x00` | u16  | key    | Marker key                                                  |
| `+0x02` | u32  | offset | Start of the marker record in `worldmapmonster.dbss`, past the key copy |
| `+0x06` | u32  | size   | Length of the marker record, the key copy left out          |

## Layout 1

On client 1784 a Marker Record held one label line: the zone or boss name
followed `line1_kr` directly, without `line2_kr`, and the record ended after
`unknown_str`, without `unknown_ref`, `unknown_kind`, `unknown_flag` and
`unknown_end`. Only the Marker Record differs from Layout 2. On client 1784
the file holds 127 records.

### Marker Record (variable: 54 bytes + text)

| Offset           | Type   | Field       | Notes                             |
| ---------------- | ------ | ----------- | --------------------------------- |
| `+0x00`          | u16    | key         |                                   |
| `+0x02`          | str16  | line1_kr    |                                   |
| `line1_kr+0x00`  | str16  | name_kr     |                                   |
| `name_kr+0x00`   | f32[3] | position    |                                   |
| `name_kr+0x0C`   | str8   | icon        |                                   |
| `icon+0x00`      | str16  | condition   |                                   |
| `condition+0x00` | str16  | unknown_str | Empty on every record on client 1784 |

## Notes

- All 229 records walk to exactly their offset-table size with the layout
  above on client 3458.
- The markers are the world map monster icons the drop item window links to
  (`window/dropitem/panel_window_renewdropitem_all_1` registers
  `FromClient_Worldmap_LinkedDropUI_MouseOn` / `MouseOut` / `MouseClick` for
  them).
- LOC type 40 names all 229 markers and has both label lines for each.
- All 191 distinct icons exist once resolved under `ui_texture/` and
  lowercased: `combine/etc/worldmapboss/` for the zone and boss art,
  `combine/icon/` for the portal, sanctum, Griffon platform and Sea Palace
  markers, and
  `combine/etc/combine_etc_ocean_change02.dds` for the Margoria sea markers.
- The `unknown_kind` groups on client 3458: `0` hunting zones (161, the level
  and AP labels), `1` Abyssal Wells (16, no icon), `2` Black Shrine bosses
  (17), `3` the keys from 10001 (20, Pilgrim's Sanctum and the Offering Site
  markers, whose icons are named `Combine_WorldMap_HardcoreServer_*`; the drop
  item window checks `ToClient_HardCoreChannelWithContensOption`), `4` world, field and hunting field bosses (15).
- On hunting zones (`unknown_kind` 0) `unknown_ref` is the hunting ground ID
  of [`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md), the drop item window's hunting ground
  table. All 92 hunting zones that set it point at the row of the same place
  on client 3458: 87 by name (`바실리스크 소굴` -> hunting ground 35,
  `바실리스크 소굴`), the other five under another name for that place
  (`하스라 고대 유적` -> `하스라 절벽`, `트롤 서식지` -> `귄트 언덕 [엘비아]`,
  `시크라이아 해저 유적` -> `시크라이아 유적 상층부`, `카드리 무리` ->
  `카드리 폐허`, `외눈박이 거인` -> `외눈박이 땅 [데키아의 등불]`). The other 69
  hunting zones store `-1`: the older level-range markers that a newer AP
  marker replaced (Biraghi Den is key 8 with `-1` and key 115 with hunting
  ground 62), the sea zones (Margoria, sea monster habitats), the god and
  demonlord markers, and a few single zones such as Lyngbakr Habitat and the
  Griffon Stations. Field name kept as `unknown_ref` because it means something else
  on the Black Shrine markers (`unknown_kind` 2): `1` to `9` on the nine
  Black Shrine bosses and `0` on the eight Land of the Morning Light world
  and party bosses.
- The drop window groups those hunting grounds the way Garmoth's grind spot
  list does: a region tab per row (13 tabs, Balenos to Inner Edania) and the
  filters of `dropuisubcategoryinfo.bss` (`파티 사냥터` party, `엘비아의 영역`
  Elvia, `마르니의 밀실` Marni's Realm, `데키아의 등불` and `데키아의 등불 II`
  Dehkia, `추천` recommended, `지역 의뢰` regional requests). Every Garmoth
  grind spot found here by name (58 of its 95) is an `unknown_kind` 0 marker
  with a hunting ground.
- The app indexes the marker illustrations by key
  (`IndexKind.WORLDMAP_MARKER_ICON`, read through `IconKind.WORLDMAP_MARKER`);
  the 16 Abyssal Wells store none and are left out.

## Open Questions

### What does `unknown_ref` hold on Black Shrine markers?

On hunting zones it is the drop window hunting ground (see Notes). The 17
Black Shrine markers use `0` to `9` instead, `0` on the Land of the Morning
Light world and party bosses and `1` to `9` once each on the Black Shrine
bosses, which reads like a boss order or difficulty step; nothing names it.

### What names the `unknown_kind` values?

The five values line up with the marker groups in Notes, and `0` is at least
the hunting zones: every marker with a drop window hunting ground is `0`. No
Lua enum or string names the values, and the world map code that reads the
file is engine side. Garmoth's grind spot list only covers hunting zones, so
it names none of the others.
