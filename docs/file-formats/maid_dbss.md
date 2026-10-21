# `maid.dbss` Format

## Purpose

The maids and butlers a player can own: per character key the warehouse
and marketplace duties, the cooldown, the PC room flag, the head maid flags
and the list icons. Companion `maidoffset.dbss` lists where every row
sits. [`pcroommaid.bss`](pcroommaid_bss.md) lists the keys whose
`pc_room_type` is set.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records                    | Row bytes                |
| ------ | -------------- | ------- | ----------------- | ----- | -------------------------- | ------------------------ |
| 2      | 1784 and later | 3474    | `maid.dbss`       | 2,566 | 27 Row, 27 Record, 15 Form | 34 to 140, 93 on average |
| 2      | 1784 and later | 3474    | `maidoffset.dbss` | 274   | 27 Offset Row              | 10                       |
| 1      | 1485           | 1485    | `maid.dbss`       | 1,536 | 9 Form, 17 Row, 17 Record  | 32 to 138, 88 on average |
| 1      | 1485           | 1485    | `maidoffset.dbss` | 174   | 17 Offset Row              | 10                       |

| Layout | File              | Known            | Unknown    |
| ------ | ----------------- | ---------------- | ---------- |
| 2      | `maid.dbss`       | 2,566 B (100.0%) | 0 B (0.0%) |
| 2      | `maidoffset.dbss` | 274 B (100.0%)   | 0 B (0.0%) |
| 1      | `maid.dbss`       | 1,536 B (100.0%) | 0 B (0.0%) |
| 1      | `maidoffset.dbss` | 174 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 2 |
| 2107   | Layout 2 |
| 1784   | Layout 2 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                      |
| ---------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `maidoffset.dbss`            | Optional | `character_key -> (offset, size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key link |
| `languagedata_*.loc`         | Optional | Character names, LOC type 6, keyed by `character_key`                                     |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes          |
| ------- | ------------- | ------- | -------------- |
| `+0x00` | u32           | count   | Number of rows |
| `+0x04` | Record[count] | records | See Record     |

### Record (variable: 2 bytes + row)

| Offset  | Type | Field      | Notes                                                 |
| ------- | ---- | ---------- | ----------------------------------------------------- |
| `+0x00` | u16  | key_prefix | Equals the row's `character_key`                      |
| `+0x02` | Row  | row        | `maidoffset.dbss` points here, at the `character_key` |

### Row (variable: 34 bytes + forms)

| Offset        | Type             | Field                 | Notes                                                                      |
| ------------- | ---------------- | --------------------- | -------------------------------------------------------------------------- |
| `+0x00`       | u16              | character_key         | Row key; a LOC type 6 character name                                       |
| `+0x02`       | u32              | max_action_index      | `0` on every row                                                           |
| `+0x06`       | i64              | cool_time             | Milliseconds; `1200000` (20 minutes) on every row                          |
| `+0x0E`       | u8               | is_able_in_warehouse  | `1` on the warehouse maids: stores items                                   |
| `+0x0F`       | u8               | is_able_out_warehouse | `1` on the warehouse maids: takes items out                                |
| `+0x10`       | u8               | is_able_submit_market | `1` on the marketplace maids: registers items                              |
| `+0x11`       | u8               | is_able_buy_market    | `1` on the marketplace maids                                               |
| `+0x12`       | u8               | is_able_repair        | `0` on every row                                                           |
| `+0x13`       | u8               | pc_room_type          | `1` on the PC room maids, the keys of `pcroommaid.bss`                     |
| `+0x14`       | u32              | skill_0               | `0` on every row (an empty sheet cell); see Field Names                    |
| `+0x18`       | u32              | skill_1               | `0` on every row (an empty sheet cell)                                     |
| `+0x1C`       | u32              | form_count            | `0` or `1`                                                                 |
| `+0x20`       | Form[form_count] | forms                 | See Form                                                                   |
| `forms+0x00`  | u8               | is_maid_chief         | `1` on the two warehouse head maids                                        |
| `forms+0x01`  | u8               | is_maid_chief_market  | `1` on the two marketplace head maids                                      |

A row without a form is 34 bytes and one with a form 140 bytes, the size
`maidoffset.dbss` gives (client 3474: 12 of 27 rows without, 15 with).

### Form (variable: 12 bytes + icon text)

| Offset  | Type  | Field        | Notes                                                                   |
| ------- | ----- | ------------ | ----------------------------------------------------------------------- |
| `+0x00` | i32   | action_index | `0` on every form                                                       |
| `+0x04` | str16 | icon_path    | Under `ui_texture/`, with backslashes: `New_UI_Common_forLua\Window\Stable\Horse_01.dds` |

### `maidoffset.dbss`

Bare offset table into `maid.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                         |
| ------- | ----------------- | ----- | ----------------------------- |
| `+0x00` | u32               | count | Equals the `maid.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                                       |
| ------- | ---- | ------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                                                 |
| `+0x02` | u32  | offset        | Absolute byte offset of the row in `maid.dbss`, at its `character_key`      |
| `+0x06` | u32  | size          | The row without its key prefix: `34` or `140` on client 3474                |

Both files list the keys in the same order, neither sorted nor grouped by
duty: on client 3474 `18977`, `18976`, `18959` down to `18951`, `18975`
down to `18960`.

## Layout 1

### Row (variable: 32 bytes + forms)

The Layout 2 row without the two head maid flags at the end.

| Offset  | Type             | Field                 | Notes                                    |
| ------- | ---------------- | --------------------- | ---------------------------------------- |
| `+0x00` | u16              | character_key         | Row key; a LOC type 6 character name     |
| `+0x02` | u32              | max_action_index      | `0` on every row                         |
| `+0x06` | i64              | cool_time             | Milliseconds; `1200000` on every row     |
| `+0x0E` | u8               | is_able_in_warehouse  | `1` on the warehouse maids               |
| `+0x0F` | u8               | is_able_out_warehouse | `1` on the warehouse maids               |
| `+0x10` | u8               | is_able_submit_market | `1` on the marketplace maids             |
| `+0x11` | u8               | is_able_buy_market    | `1` on the marketplace maids             |
| `+0x12` | u8               | is_able_repair        | `0` on every row                         |
| `+0x13` | u8               | pc_room_type          | `1` on `18964` to `18967`                |
| `+0x14` | u32              | skill_0               | `0` on every row                         |
| `+0x18` | u32              | skill_1               | `0` on every row                         |
| `+0x1C` | u32              | form_count            | `0` or `1`                               |
| `+0x20` | Form[form_count] | forms                 | See Form                                 |

## Maids and Butlers

On client 3474 every row has `cool_time` `1200000`, and each key is either
a warehouse maid (`is_able_in_warehouse` and `is_able_out_warehouse` set)
or a marketplace maid (`is_able_submit_market` and `is_able_buy_market`
set). The names are LOC type 6 (client 3474).

| character_key | Name                     | Duty        | Other flags            | Icon           |
| ------------- | ------------------------ | ----------- | ---------------------- | -------------- |
| `18951`       | Fairy Irene              | Warehouse   |                        | `Horse_01.dds` |
| `18952`       | Fairy Irene              | Marketplace |                        | `Horse_02.dds` |
| `18953`       | Fairy Risty              | Warehouse   |                        | `Horse_03.dds` |
| `18954`       | Fairy Risty              | Marketplace |                        | `Horse_04.dds` |
| `18955`       | Fairy Chiara             | Warehouse   |                        | `Horse_05.dds` |
| `18956`       | Fairy Chiara             | Marketplace |                        | `Horse_06.dds` |
| `18957`       | Sandbag                  | Warehouse   |                        | `Horse_01.dds` |
| `18958`       | Goblin Butler            | Warehouse   |                        | `Horse_06.dds` |
| `18959`       | Goblin Butler            | Marketplace |                        | `Horse_01.dds` |
| `18960`       | Ethan the Butler         | Warehouse   |                        | None           |
| `18961`       | Ethan the Butler         | Marketplace |                        | None           |
| `18962`       | Pietro the Butler        | Warehouse   |                        | None           |
| `18963`       | Pietro the Butler        | Marketplace |                        | None           |
| `18964`       | [Oasis] Fairy Chiara     | Warehouse   | `pc_room_type`         | None           |
| `18965`       | [Oasis] Fairy Chiara     | Marketplace | `pc_room_type`         | None           |
| `18966`       | [Oasis] Ethan the Butler | Warehouse   | `pc_room_type`         | None           |
| `18967`       | [Oasis] Ethan the Butler | Marketplace | `pc_room_type`         | None           |
| `18968`       | Cecilia the Maid         | Warehouse   | `is_maid_chief`        | `Horse_06.dds` |
| `18969`       | Sebastian the Butler     | Warehouse   | `is_maid_chief`        | `Horse_01.dds` |
| `18970`       | Cecilia the Maid         | Marketplace | `is_maid_chief_market` | `Horse_06.dds` |
| `18971`       | Butler Sebastian         | Marketplace | `is_maid_chief_market` | `Horse_01.dds` |
| `18972`       | No LOC name              | Warehouse   |                        | `Horse_01.dds` |
| `18973`       | No LOC name              | Marketplace |                        | `Horse_02.dds` |
| `18974`       | [Oasis] Fairy Chiara     | Warehouse   | `pc_room_type`         | None           |
| `18975`       | [Oasis] Fairy Chiara     | Marketplace | `pc_room_type`         | None           |
| `18976`       | [Oasis] Ethan the Butler | Warehouse   | `pc_room_type`         | None           |
| `18977`       | [Oasis] Ethan the Butler | Marketplace | `pc_room_type`         | None           |

Each icon sits in `New_UI_Common_forLua\Window\Stable\`, the stable
window's horse portraits; every one of them is in the client 3474 PAZ.

## Field Names

The `Maid_Table` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `CharacterKey`, `CoolTime`, `IsAbleInWareHouse`,
`IsAbleOutWareHouse`, `IsAbleSubmitMarket`, `IsAbleBuyMarket`,
`IsAbleRepair`, `PcRoomType`, `IsMaidChief`, `IsMaidChiefMarket`,
`MaxActionIndex`, `Skill_0` and `Skill_1`, and four `IsAble*CoolTime`
columns. The `MaidFormList_Table` sheet has `CharacterKey`, `ActionIndex`
and `IconImageFile1`, one row per form. Matched by value over the 21 keys
both hold, on clients 1784 (21 of 21 rows) and 3474 (21 of 27 rows; the
sheet lacks `18972` to `18977`):

| Field                   | Column               | Rows matching |
| ----------------------- | -------------------- | ------------- |
| `character_key`         | `CharacterKey`       | 21 of 21      |
| `max_action_index`      | `MaxActionIndex`     | 21 of 21, all `0` |
| `cool_time`             | `CoolTime`           | 21 of 21      |
| `is_able_in_warehouse`  | `IsAbleInWareHouse`  | 21 of 21      |
| `is_able_out_warehouse` | `IsAbleOutWareHouse` | 21 of 21      |
| `is_able_submit_market` | `IsAbleSubmitMarket` | 21 of 21      |
| `is_able_buy_market`    | `IsAbleBuyMarket`    | 21 of 21      |
| `is_able_repair`        | `IsAbleRepair`       | 21 of 21, all `0` |
| `pc_room_type`          | `PcRoomType`         | 21 of 21      |
| `skill_0`, `skill_1`    | `Skill_0`, `Skill_1` | 21 of 21, all empty cells and `0` |
| `forms`                 | `MaidFormList_Table` | 21 of 21 (13 keys with one form, 8 with none) |
| `is_maid_chief`         | `IsMaidChief`        | 21 of 21      |
| `is_maid_chief_market`  | `IsMaidChiefMarket`  | 21 of 21      |

The client 1784 server dump has the loader of `Maid_Table` (VA
`0x140866390`). It reads `CharacterKey` with `ReadCellInt` and keeps the
low u16, then `MaxActionIndex` (`ReadColumnInt32B`), `CoolTime`
(`ReadColumnTime`, 8 bytes), the six bools `IsAbleInWareHouse` to
`PcRoomType`, `Skill_0` and `Skill_1` (a `Skill_%d` loop with
`ReadColumnInt`, the cell optional), then `IsMaidChief` and
`IsMaidChiefMarket`. The file holds the fields in that order, with the
forms between the skills and the head maid flags. `max_action_index`,
`is_able_repair`, `skill_0` and `skill_1` match only as zeros, so their
names rest on that read order. The four `IsAble*CoolTime` columns are not
read and have no bytes in the file. The `MaidFormList_Table` loader (VA
`0x140866ea0`) reads `ActionIndex` with `ReadColumnInt` and
`IconImageFile1` with `ReadColumnWString`. The 2016 client's debug symbols
have no maid type.

## Notes

- Clients 1784, 2107, 2519, 3002, 3251 and 3474 fit Layout 2; client 1485
  fits Layout 1, the 17 keys `18951` to `18967` with no head maid flags.
  Client 2107 adds `18972` and `18973`, client 2519 `18974` to `18977`.
  Clients 794 and 1230 have no `maid.dbss`; they ship a `maid.bss`
  (`gamecommondata/binary/en/maid.bss` on client 794), which has no doc.
- The private server's own compiled `maid.dbss` and `maidoffset.dbss`
  (client 1784) are the same bytes as the client files.
- `18974` to `18977` are the bytes of `18964` to `18967` with only the key
  changed, as [`pcroommaid.bss`](pcroommaid_bss.md) notes.
- The client Lua of the maid list (`panel_window_maidlist_all`) sorts each
  maid into the warehouse tab when `isAbleInWarehouse()` or
  `isAbleOutWarehouse()` is true and into the marketplace tab when
  `isAbleSubmitMarket()` is, and marks it as head maid when
  `isMaidChief()` or `isMaidChiefMarket()` is true. Its `getCoolTime()` is
  the time left on an owned maid, not this table's value. No client Lua
  reads the skills, the action index or the icon.

## Open Questions

### What the Skills and the Action Index Hold

`skill_0`, `skill_1`, `max_action_index` and every form's `action_index`
are `0` on all rows of every client checked. The client 1784 server
loader stores a set `Skill_N` cell as `(value << 16) | 1` in a 4-byte
slot, so a set skill would read as an odd u32 here; with no set cell in
any sheet row or file, neither that encoding in the client file nor what
the skill numbers point at can be confirmed.

### What the Form Icons Are For

The forms of 15 rows name a horse portrait of the stable window
(`Horse_01.dds` to `Horse_06.dds`) and 12 rows, among them all PC room
maids and the butlers Ethan and Pietro, have none. No client Lua of the
maid windows (`panel_window_maidlist_all`, `panel_widget_topicon_maid`)
reads the icon, so where the game shows it is not known.
