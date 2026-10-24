# `instancefield.dbss` Format

## Purpose

The instance fields: separate copies of a world area that a group enters
(Solare arenas, Atoraxion, node and siege war maps, horse race tracks, guild
matches, test fields). Each record has a key, an area of the world given in
sectors, and an internal ASCII name. `buff.dbss` effect type 176 stores the
key in `param_3` (`Teleport to Instance Field The Magnus: The Great Single
Path (A1_001)`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records        | Row bytes               |
| ------ | -------------- | ------- | -------------------------- | ------ | -------------- | ----------------------- |
| 1      | 1659 and later | 3483    | `instancefield.dbss`       | 10,810 | 200 Record     | 41 to 74, 54 on average |
| 1      | 1659 and later | 3483    | `instancefieldoffset.dbss` | 2,004  | 200 Offset Row | 10                      |

| Layout | File                       | Known             | Unknown    |
| ------ | -------------------------- | ----------------- | ---------- |
| 1      | `instancefield.dbss`       | 10,810 B (100.0%) | 0 B (0.0%) |
| 1      | `instancefieldoffset.dbss` | 2,004 B (100.0%)  | 0 B (0.0%) |

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
| 3212   | Layout 1             |
| 3203   | Layout 1             |
| 3193   | Layout 1             |
| 3186   | Layout 1             |
| 3177   | Layout 1             |
| 3169   | Layout 1             |
| 3158   | Layout 1             |
| 3151   | Layout 1             |
| 3144   | Layout 1             |
| 3133   | Layout 1             |
| 3125   | Layout 1             |
| 3118   | Layout 1             |
| 3111   | Layout 1             |
| 3103   | Layout 1             |
| 3095   | Layout 1             |
| 3086   | Layout 1             |
| 3072   | Layout 1             |
| 3062   | Layout 1             |
| 3052   | Layout 1             |
| 3045   | Layout 1             |
| 3037   | Layout 1             |
| 3030   | Layout 1             |
| 3021   | Layout 1             |
| 3012   | Layout 1             |
| 3002   | Layout 1             |
| 2995   | Layout 1             |
| 2987   | Layout 1             |
| 2978   | Layout 1             |
| 2970   | Layout 1             |
| 2959   | Layout 1             |
| 2951   | Layout 1             |
| 2942   | Layout 1             |
| 2935   | Layout 1             |
| 2932   | Layout 1             |
| 2923   | Layout 1             |
| 2919   | Layout 1             |
| 2907   | Layout 1             |
| 2900   | Layout 1             |
| 2891   | Layout 1             |
| 2882   | Layout 1             |
| 2872   | Layout 1             |
| 2863   | Layout 1             |
| 2855   | Layout 1             |
| 2849   | Layout 1             |
| 2844   | Layout 1             |
| 2834   | Layout 1             |
| 2825   | Layout 1             |
| 2819   | Layout 1             |
| 2811   | Layout 1             |
| 2803   | Layout 1             |
| 2794   | Layout 1             |
| 2783   | Layout 1             |
| 2774   | Layout 1             |
| 2765   | Layout 1             |
| 2756   | Layout 1             |
| 2750   | Layout 1             |
| 2743   | Layout 1             |
| 2736   | Layout 1             |
| 2726   | Layout 1             |
| 2717   | Layout 1             |
| 2709   | Layout 1             |
| 2703   | Layout 1             |
| 2695   | Layout 1             |
| 2684   | Layout 1             |
| 2672   | Layout 1             |
| 2665   | Layout 1             |
| 2657   | Layout 1             |
| 2649   | Layout 1             |
| 2644   | Layout 1             |
| 2637   | Layout 1             |
| 2629   | Layout 1             |
| 2619   | Layout 1             |
| 2612   | Layout 1             |
| 2606   | Layout 1             |
| 2602   | Layout 1             |
| 2601   | Layout 1             |
| 2592   | Layout 1             |
| 2583   | Layout 1             |
| 2575   | Layout 1             |
| 2567   | Layout 1             |
| 2560   | Layout 1             |
| 2553   | Layout 1             |
| 2545   | Layout 1             |
| 2538   | Layout 1             |
| 2529   | Layout 1             |
| 2519   | Layout 1             |
| 2513   | Layout 1             |
| 2510   | Layout 1             |
| 2507   | Layout 1             |
| 2503   | Layout 1             |
| 2498   | Layout 1             |
| 2492   | Layout 1             |
| 2487   | Layout 1             |
| 2480   | Layout 1             |
| 2474   | Layout 1             |
| 2468   | Layout 1             |
| 2460   | Layout 1             |
| 2453   | Layout 1             |
| 2444   | Layout 1             |
| 2438   | Layout 1             |
| 2434   | Layout 1             |
| 2429   | Layout 1             |
| 2421   | Layout 1             |
| 2414   | Layout 1             |
| 2407   | Layout 1             |
| 2401   | Layout 1             |
| 2397   | Layout 1             |
| 2393   | Layout 1             |
| 2384   | Layout 1             |
| 2378   | Layout 1             |
| 2372   | Layout 1             |
| 2358   | Layout 1             |
| 2352   | Layout 1             |
| 2347   | Layout 1             |
| 2343   | Layout 1             |
| 2335   | Layout 1             |
| 2327   | Layout 1             |
| 2324   | Layout 1             |
| 2319   | Layout 1             |
| 2313   | Layout 1             |
| 2308   | Layout 1             |
| 2302   | Layout 1             |
| 2295   | Layout 1             |
| 2290   | Layout 1             |
| 2284   | Layout 1             |
| 2276   | Layout 1             |
| 2269   | Layout 1             |
| 2259   | Layout 1             |
| 2250   | Layout 1             |
| 2243   | Layout 1             |
| 2235   | Layout 1             |
| 2229   | Layout 1             |
| 2224   | Layout 1             |
| 2218   | Layout 1             |
| 2215   | Layout 1             |
| 2207   | Layout 1             |
| 2203   | Layout 1             |
| 2196   | Layout 1             |
| 2192   | Layout 1             |
| 2189   | Layout 1             |
| 2183   | Layout 1             |
| 2179   | Layout 1             |
| 2171   | Layout 1             |
| 2163   | Layout 1             |
| 2156   | Layout 1             |
| 2151   | Layout 1             |
| 2147   | Layout 1             |
| 2142   | Layout 1             |
| 2138   | Layout 1             |
| 2134   | Layout 1             |
| 2130   | Layout 1             |
| 2122   | Layout 1             |
| 2107   | Layout 1             |
| 2098   | Layout 1             |
| 2089   | Layout 1             |
| 2081   | Layout 1             |
| 2073   | Layout 1             |
| 2067   | Layout 1             |
| 2063   | Layout 1             |
| 2059   | Layout 1             |
| 2052   | Layout 1             |
| 2044   | Layout 1             |
| 2039   | Layout 1             |
| 2032   | Layout 1             |
| 2025   | Layout 1             |
| 2011   | Layout 1             |
| 2005   | Layout 1             |
| 2000   | Layout 1             |
| 1996   | Layout 1             |
| 1991   | Layout 1             |
| 1985   | Layout 1             |
| 1980   | Layout 1             |
| 1969   | Layout 1             |
| 1964   | Layout 1             |
| 1958   | Layout 1             |
| 1950   | Layout 1             |
| 1945   | Layout 1             |
| 1937   | Layout 1             |
| 1933   | Layout 1             |
| 1927   | Layout 1             |
| 1921   | Layout 1             |
| 1914   | Layout 1             |
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
| 1649   | No documented layout |
| 1642   | No documented layout |
| 1636   | No documented layout |
| 1628   | No documented layout |
| 1622   | No documented layout |
| 1614   | No documented layout |
| 1608   | No documented layout |
| 1602   | No documented layout |
| 1598   | No documented layout |
| 1594   | No documented layout |
| 1590   | No documented layout |
| 1587   | No documented layout |
| 1584   | No documented layout |
| 1579   | No documented layout |
| 1572   | No documented layout |
| 1565   | No documented layout |
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
| 1276   | No documented layout |
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

| File                       | Required | Role                                                         |
| -------------------------- | -------- | ------------------------------------------------------------ |
| `instancefieldoffset.dbss` | Optional | Index of the records by key, see below; not needed to read this file |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A count followed by variable-size records. No PABR magic and no trailer; the
records fill the file exactly (199 records, 10,736 bytes on client 3464).

| Offset  | Type           | Field   | Notes                                     |
| ------- | -------------- | ------- | ----------------------------------------- |
| `+0x00` | u32            | count   | Number of records                         |
| `+0x04` | Record[count]  | records | See Record; not sorted by key             |

### Record (variable: 40 bytes + name text)

| Offset      | Type    | Field         | Notes |
| ----------- | ------- | ------------- | ----- |
| `+0x00`     | u16     | key           | Unique; `0` to `9876` |
| `+0x02`     | i32     | min_x         | Sector box, lower corner; one sector is 12,800 world units (128 m), see Notes |
| `+0x06`     | i32     | min_y         | Height |
| `+0x0A`     | i32     | min_z         | |
| `+0x0E`     | i32     | max_x         | Sector box, upper corner; never below the matching `min_*` |
| `+0x12`     | i32     | max_y         | |
| `+0x16`     | i32     | max_z         | |
| `+0x1A`     | i32     | field_grid_sector_count | `1`, `2` or `3`; see Field Names |
| `+0x1E`     | str8    | name          | ASCII, not null-terminated |
| `name+0x00` | u16     | field_no      | Key of the field the instance runs in: `1` (the world) or the record's own key on the `A1_` fields; see Field Names |

Names are not unique: on client 3464 the 199 records carry 163 names, and
`Edania_Field` / `Edania_Field_1vs1` (10 each), `CrimsonField` (6),
`CrimsonField2` (6), `CrimsonField3` (4), `Solare_Arena_Common` (4) and `ABSO`
(3) repeat with different keys.

### `instancefieldoffset.dbss`

A u32 count followed by `count` 10-byte rows, no header or trailer (1,994
bytes on client 3464).

| Offset  | Type              | Field | Notes                              |
| ------- | ----------------- | ----- | ---------------------------------- |
| `+0x00` | u32               | count | Equals the main file's `count`     |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                     |

The rows are in a hash order (`80, 16, 4053, 0, 4035, ...`), not file
order. Every row points at the start of the record with the same key and
gives its exact size, so the index adds nothing to a sequential read.

### Offset Row (10 bytes)

| Offset  | Type | Field  | Notes |
| ------- | ---- | ------ | ----- |
| `+0x00` | u16  | key    | Record key |
| `+0x02` | u32  | offset | `instancefield.dbss` offset of the record with this key |
| `+0x06` | u32  | size   | Byte size of that record, 40 plus the length of `name` |

## Field Names

The record is the `InstanceField_Table` sheet of a private server on client
1784. That server's dump (`Instance_dumpFull.exe`) reads the client record
with the row reader at VA `0x140b056e0`: the u16 key into `+0x00`, the two
12-byte boxes into `+0x04` and `+0x10`, a u32 into `+0x20`, the name into
`+0x30` and a u16 into `+0x50`. Its sheet loader (VA `0x1409e18f0`) fills
the same members:

| Field                     | Struct member | Sheet column                           |
| ------------------------- | ------------- | -------------------------------------- |
| `key`                     | `+0x00`       | `InstanceFieldMapKey`                  |
| `min_x` to `max_z`        | `+0x04` to `+0x18` | `StartSectorX/Y/Z`, `EndSectorX/Y/Z` |
| `field_grid_sector_count` | `+0x20`       | `FieldGridSectorCount`                 |
| `name`                    | `+0x30`       | `ScriptFileName`                       |
| `field_no`                | `+0x50`       | `FieldNo`                              |

The check at VA `0x140b05090` compares `FieldGridSectorCount` signed and
logs "인스턴스 필드의 FieldGridSectorCount는 1 이상의 정수를 입력해야 합니다"
("an instance field's FieldGridSectorCount must be an integer of 1 or
more"), so the field is an i32. After loading, the server sets a `FieldNo`
of `0` or `0xFFFF` to `1` and looks it up among its field infos, logging
"InstanceFieldMap의 필드번호가 비정상입니다" ("the instance field map's field
number is invalid") when it is missing. `FieldNo` is the key of the
`Field_Table` sheet, where `1` is `월드` ("World") and `4001` to `4066` are
`A1_001` to `A1_066`; the client copy of that table is
[fieldinfo.bss](fieldinfo_bss.md), which holds every `field_no` of client
3474.

The sheet and the private server's own file hold the same 92 fields; every
column above matches on all 92, and client 3474 has the same
`field_grid_sector_count` and `field_no` on all 92 keys it shares.

## Notes

- The box unit is a 12,800-unit sector of the world frame that
  `teleport.dbss` and `mapdata_realexplore2.bwp` use. Divided by 12,800 and
  floored, the `teleport.dbss` points of the Atoraxion portal buffs
  (`아토락시온 포탈 : 사막 : 2구역 입장`, `아토락시온 포탈 : 해저 : 3구역
  입장`) fall inside the `Atoraxion_*` boxes, `벨리아 > 수궁` ("Velia > Sea
  Palace") inside `Yonggung`, and point 277 (`x -1460010, z 1419360`, sector
  `-114, 110`) inside `Solare_Arena_Janghwa` (`-117..-113, 109..113`) in the
  Land of the Morning Light. At 25,600 or 6,400 per sector those points
  leave their boxes. The check counted both bounds as inside.
- Boxes overlap the open world and each other: an instance field is a copy
  of a world area, so many open-world teleport points also fall in a box.
  The `MajorSiege_*` boxes cover whole territories (`MajorSiege_Valencia`
  `x 25..100`).
- The `INSTANCE_FIELD_NAME` lookup index maps each key to its name, so the
  `buff.dbss` Effect text of type 176 names the field without opening this
  file, after the `instancefieldmapinfo.bss` title: `Teleport to Instance
  Field The Magnus: The Great Single Path (A1_001)`.
- The 66 `A1_` fields (keys 4001 to 4066, names `A1_001` to `A1_066`) share
  the box `-3..3` on every axis, around the world origin. Items and skills
  named `A1_001` to `A1_054` apply the type 176 buffs that send a player
  there (`buff_dbss.md`).
- [instancefieldmapinfo.bss](instancefieldmapinfo_bss.md) holds the map
  data under the same keys: a `GAME` sheet name and description
  (`A1_001` is "The Magnus: The Great Single Path"), a map image, a centre
  point, an entry item and team spawn points. The other
  `instancefield*` tables (`instancefieldcommon.bss`,
  `instancefieldranking.bss`, `instancefieldreward.dbss`,
  `instancefieldcommonlimitentertime.bss`) have their own layouts.

## Open Questions

### What do the `field_grid_sector_count` values select?

On client 3464 it is `1` on 189 records, `3` on `Shadow_Ser_Main` (key 1)
and `2` on nine: keys 2 to 8 (`1`, `3_Ser_CentralGuardCamp`,
`4_Bal_Ehwaz`, `5_Cal_CalpheonCastle`, `6_Cal_SounilFortress`,
`7_Val_Desert`, `8_Kam_Naban`) and 98 / 99 (`Practice1`, `Practice`). None
of these ten has an `instancefieldmapinfo.bss` record. The client 1784
server multiplies it by 3,700 and stores the result as a float next to the
box; what a count of 2 or 3 changes in game is open.
