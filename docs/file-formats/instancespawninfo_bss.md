# `instancespawninfo.bss` Format

## Purpose

The hunting grounds of the private monster zones (personal fields, Marni's
Realm): per zone a sector box, a centre point and radius, the Korean area
name, the recommended AP, the scroll a deep entry consumes and the entry
type. The Personal Field window (`panel_window_personalfield_main_all_1.luac`)
lists them through `ToClient_getInstanceSpawnInfoWrapperByIndex(index)`.
On client 3482 the file has 54 zones, from Tshira Ruins (recommended AP
140) to Event Horizon (420). The file is a u32 count and variable rows,
with no PABR magic.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes                 |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | ------------------------- |
| 6      | 3454 and later | 3482    | `instancespawninfo.bss` | 4,582 | 54 Row  | 74 to 98, 85 on average   |
| 5      | 3144 to 3412   | 3412    | `instancespawninfo.bss` | 5,878 | 54 Row  | 98 to 122, 109 on average |
| 4      | 3002 to 3103   | 3103    | `instancespawninfo.bss` | 4,592 | 44 Row  | 93 to 117, 104 on average |
| 3      | 2134 to 2959   | 2959    | `instancespawninfo.bss` | 3,490 | 38 Row  | 80 to 104, 92 on average  |
| 2      | 1886 to 2107   | 2107    | `instancespawninfo.bss` | 2,182 | 24 Row  | 78 to 102, 91 on average  |
| 1      | 1866           | 1866    | `instancespawninfo.bss` | 40    | 1 Row   | 36                        |

| Layout | File                    | Known           | Unknown       |
| ------ | ----------------------- | --------------- | ------------- |
| 6      | `instancespawninfo.bss` | 3,664 B (80.0%) | 918 B (20.0%) |
| 5      | `instancespawninfo.bss` | 4,960 B (84.4%) | 918 B (15.6%) |
| 4      | `instancespawninfo.bss` | 4,064 B (88.5%) | 528 B (11.5%) |
| 3      | `instancespawninfo.bss` | 3,338 B (95.6%) | 152 B (4.4%)  |
| 2      | `instancespawninfo.bss` | 2,134 B (97.8%) | 48 B (2.2%)   |
| 1      | `instancespawninfo.bss` | 38 B (95.0%)    | 2 B (5.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 6 |
| 3474   | Layout 6 |
| 3454   | Layout 6 |
| 3412   | Layout 5 |
| 3381   | Layout 5 |
| 3349   | Layout 5 |
| 3314   | Layout 5 |
| 3283   | Layout 5 |
| 3251   | Layout 5 |
| 3212   | Layout 5 |
| 3177   | Layout 5 |
| 3144   | Layout 5 |
| 3103   | Layout 4 |
| 3062   | Layout 4 |
| 3037   | Layout 4 |
| 3002   | Layout 4 |
| 2959   | Layout 3 |
| 2923   | Layout 3 |
| 2900   | Layout 3 |
| 2872   | Layout 3 |
| 2834   | Layout 3 |
| 2803   | Layout 3 |
| 2765   | Layout 3 |
| 2736   | Layout 3 |
| 2703   | Layout 3 |
| 2665   | Layout 3 |
| 2637   | Layout 3 |
| 2606   | Layout 3 |
| 2583   | Layout 3 |
| 2545   | Layout 3 |
| 2519   | Layout 3 |
| 2498   | Layout 3 |
| 2468   | Layout 3 |
| 2438   | Layout 3 |
| 2414   | Layout 3 |
| 2384   | Layout 3 |
| 2358   | Layout 3 |
| 2335   | Layout 3 |
| 2313   | Layout 3 |
| 2290   | Layout 3 |
| 2250   | Layout 3 |
| 2224   | Layout 3 |
| 2203   | Layout 3 |
| 2179   | Layout 3 |
| 2151   | Layout 3 |
| 2134   | Layout 3 |
| 2107   | Layout 2 |
| 2073   | Layout 2 |
| 2052   | Layout 2 |
| 2011   | Layout 2 |
| 1996   | Layout 2 |
| 1969   | Layout 2 |
| 1937   | Layout 2 |
| 1914   | Layout 2 |
| 1886   | Layout 2 |
| 1866   | Layout 1 |
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

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `languagedata_en.loc` | Optional | Item names of `enter_item_key` (LOC type 0) |

All multi-byte values are little-endian.

## Layout 6

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 68 bytes + name text)

| Offset              | Type  | Field                       | Notes |
| ------------------- | ----- | --------------------------- | ----- |
| `+0x00`             | u16   | key                         | Row key, `0` to `53` (client 3482), not sorted |
| `+0x02`             | i32   | max_x                       | Sector box, upper corner, in world units; a multiple of 12,800 (one sector) |
| `+0x06`             | i32   | max_z                       | |
| `+0x0A`             | i32   | min_x                       | Lower corner |
| `+0x0E`             | i32   | min_z                       | |
| `+0x12`             | u16   | unknown_12                  | Equals `key` on every row of every client |
| `+0x14`             | f32   | x                           | Centre point (centimetres), inside the box on every row |
| `+0x18`             | f32   | y                           | |
| `+0x1C`             | f32   | z                           | |
| `+0x20`             | f32   | radius                      | Centimetres around the centre point (`5000` to `30000`) |
| `+0x24`             | str16 | area_name_kr                | Korean area name (`트쉬라 폐허`, `[엘비아] 오크 캠프`) |
| `area_name_kr+0x00` | f32   | offense_point               | Recommended AP, a whole number (`140` to `420`) |
| `area_name_kr+0x04` | u16   | unknown_area_name_kr_04     | `1` on every row |
| `area_name_kr+0x06` | u32   | enter_item_key              | Item a deep entry consumes, `0` for none (`761679` Zephyros Castle Scroll) |
| `area_name_kr+0x0A` | u32   | unknown_area_name_kr_0a     | `1` where `enter_item_key` is set, else `0` |
| `area_name_kr+0x0E` | u32   | unknown_area_name_kr_0e     | `0` on every row |
| `area_name_kr+0x12` | u8    | enter_type                  | `1` on the ten Edania zones, else `0`; see [Field Names](#field-names) |
| `area_name_kr+0x13` | u32   | unknown_item_key            | A different item key on every row; see [unknown_item_key](#unknown_item_key) |
| `area_name_kr+0x17` | u8    | unknown_area_name_kr_17     | `0` to `4`; `4` on the ten Edania zones |

## Layout 5

Clients 3144 to 3412 store the recommended AP as Korean text (`추천 공격력 340`,
"recommended AP 340") right after the name; the fields after it are the
same.

### Row (variable: 72 bytes + texts)

| Offset                 | Type  | Field                   | Notes |
| ---------------------- | ----- | ----------------------- | ----- |
| `+0x00`                | u16   | key                     | |
| `+0x02`                | i32   | max_x                   | |
| `+0x06`                | i32   | max_z                   | |
| `+0x0A`                | i32   | min_x                   | |
| `+0x0E`                | i32   | min_z                   | |
| `+0x12`                | u16   | unknown_12              | |
| `+0x14`                | f32   | x                       | |
| `+0x18`                | f32   | y                       | |
| `+0x1C`                | f32   | z                       | |
| `+0x20`                | f32   | radius                  | |
| `+0x24`                | str16 | area_name_kr            | |
| `area_name_kr+0x00`    | str16 | offense_text_kr         | `추천 공격력` and the AP |
| `offense_text_kr+0x00` | u16   | unknown_area_name_kr_04 | |
| `offense_text_kr+0x02` | u32   | enter_item_key          | |
| `offense_text_kr+0x06` | u32   | unknown_area_name_kr_0a | |
| `offense_text_kr+0x0A` | u32   | unknown_area_name_kr_0e | |
| `offense_text_kr+0x0E` | u8    | enter_type              | |
| `offense_text_kr+0x0F` | u32   | unknown_item_key        | |
| `offense_text_kr+0x13` | u8    | unknown_area_name_kr_17 | |

## Layout 4

Clients 3002 to 3103 end the row after `enter_type`.

### Row (variable: 67 bytes + texts)

| Offset                 | Type  | Field                   | Notes |
| ---------------------- | ----- | ----------------------- | ----- |
| `+0x00`                | u16   | key                     | |
| `+0x02`                | i32   | max_x                   | |
| `+0x06`                | i32   | max_z                   | |
| `+0x0A`                | i32   | min_x                   | |
| `+0x0E`                | i32   | min_z                   | |
| `+0x12`                | u16   | unknown_12              | |
| `+0x14`                | f32   | x                       | |
| `+0x18`                | f32   | y                       | |
| `+0x1C`                | f32   | z                       | |
| `+0x20`                | f32   | radius                  | |
| `+0x24`                | str16 | area_name_kr            | |
| `area_name_kr+0x00`    | str16 | offense_text_kr         | |
| `offense_text_kr+0x00` | u16   | unknown_area_name_kr_04 | |
| `offense_text_kr+0x02` | u32   | enter_item_key          | |
| `offense_text_kr+0x06` | u32   | unknown_area_name_kr_0a | |
| `offense_text_kr+0x0A` | u32   | unknown_area_name_kr_0e | |
| `offense_text_kr+0x0E` | u8    | enter_type              | |

## Layout 3

Clients 2134 to 2959 end the row after `unknown_area_name_kr_04`.

### Row (variable: 54 bytes + texts)

| Offset                 | Type  | Field                   | Notes |
| ---------------------- | ----- | ----------------------- | ----- |
| `+0x00`                | u16   | key                     | |
| `+0x02`                | i32   | max_x                   | |
| `+0x06`                | i32   | max_z                   | |
| `+0x0A`                | i32   | min_x                   | |
| `+0x0E`                | i32   | min_z                   | |
| `+0x12`                | u16   | unknown_12              | |
| `+0x14`                | f32   | x                       | |
| `+0x18`                | f32   | y                       | |
| `+0x1C`                | f32   | z                       | |
| `+0x20`                | f32   | radius                  | |
| `+0x24`                | str16 | area_name_kr            | |
| `area_name_kr+0x00`    | str16 | offense_text_kr         | |
| `offense_text_kr+0x00` | u16   | unknown_area_name_kr_04 | |

## Layout 2

Clients 1886 to 2107 end the row after the AP text.

### Row (variable: 52 bytes + texts)

| Offset              | Type  | Field           | Notes |
| ------------------- | ----- | --------------- | ----- |
| `+0x00`             | u16   | key             | |
| `+0x02`             | i32   | max_x           | |
| `+0x06`             | i32   | max_z           | |
| `+0x0A`             | i32   | min_x           | |
| `+0x0E`             | i32   | min_z           | |
| `+0x12`             | u16   | unknown_12      | |
| `+0x14`             | f32   | x               | |
| `+0x18`             | f32   | y               | |
| `+0x1C`             | f32   | z               | |
| `+0x20`             | f32   | radius          | |
| `+0x24`             | str16 | area_name_kr    | |
| `area_name_kr+0x00` | str16 | offense_text_kr | |

## Layout 1

Client 1866 has one row and no texts: the row ends after `radius`.

### Row (36 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u16  | key        | `0` |
| `+0x02` | i32  | max_x      | |
| `+0x06` | i32  | max_z      | |
| `+0x0A` | i32  | min_x      | |
| `+0x0E` | i32  | min_z      | |
| `+0x12` | u16  | unknown_12 | |
| `+0x14` | f32  | x          | |
| `+0x18` | f32  | y          | |
| `+0x1C` | f32  | z          | |
| `+0x20` | f32  | radius     | |

## Field Names

The names follow the getters of the wrapper the Personal Field window
reads (`panel_window_personalfield_main_all_1.luac`,
`panel_widget_personalfield_all_1.luac`, client 3482): `getAreaName()`,
`getCenterPos()`, `getRadius()` (the window offers the entry button below
80% of it), `getOffensePoint()` (shown after the "AP" label of
`LUA_DROPINFO_MYVIEWSTATSINFO_ATT`), `getEnterItemKey()` and
`getEnterType()`. The scrolls of `enter_item_key` say they are consumed on
entry to that zone (`761679` Zephyros Castle Scroll, `980137` Event
Horizon Scroll). `getEnterType()` is compared with
`__ePersonalMirrorFieldEnterType_Edania` to pick the Edania or the
Atoraxion button texture; `enter_type` is `1` on the ten zones whose
scroll pays a tax to an Edana (the five castles `39` to `43` and the
five zones `49` to `53`, Aphrodon Temple to Event Horizon) and `0` on Orzekea, whose entry item is
Maha's Fragment `757182` of Atoraxion. The getters `getIndex()` and
`getFieldNo()` match `key` or `unknown_12`; the two are equal on every row,
so which is which is not shown. The box fields follow the corner order of
the centre point: `max_x` is above and `min_x` below `x` on all 54 rows.
The file is not in client 1784 and has no sheet in a private server's
`DataSheets.bexcel` on client 1784.

## Notes

- Row counts: 24 on client 2107, 38 on clients 2519 and 2765, 42 on
  client 3002, 48 on client 3251 and 54 on client 3482.

## Open Questions

### unknown_item_key

Every row holds an item key that LOC type 0 names: Decayed Cloth `65330`
in `어둠 추종자 침소`, Hardened Lava Chunk `767248` in Zephyros Castle,
Black Crystal Fragment `980128` in Event Horizon. They look like a
typical drop of the zone, which the looting report window
(`panel_window_lootingitemreport_main_all_1.luac`) could show, but the Lua
reads no such getter.

### unknown_area_name_kr_17

`0` to `4`, with `4` on every Edania zone. It is not the recommended AP
band (Tshira Ruins at 140 has `2`, Hystria Ruins at 230 also `2`).
What it selects is open.
