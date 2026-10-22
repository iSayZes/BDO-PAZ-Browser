# `form.dbss` Format

## Purpose

The forms (looks) of horses and other mounts that the look change windows
offer: one row per form with its type, the action chart index the model
uses, the horse tier, two UI icons and, on newer clients, the characters
that can take the form. On client 3482 the file holds 297 forms (272 on
client 1784): 115 with `type` `0`, all with a horse icon, and 182 with
`type` `1`: 119 more horses, ships and boats, carriages, donkeys, elephants
and a few others. Companion `formoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes  | Records        | Row bytes                 |
| ------ | -------------- | ------- | ----------------- | ------ | -------------- | ------------------------- |
| 2      | 2107 and later | 3482    | `form.dbss`       | 76,275 | 297 Row        | 31 to 269, 257 on average |
| 2      | 2107 and later | 3482    | `formoffset.dbss` | 2,974  | 297 Offset Row | 10                        |
| 1      | 1348 to 1937   | 1937    | `form.dbss`       | 69,214 | 274 Row        | 27 to 265, 253 on average |
| 1      | 1348 to 1937   | 1937    | `formoffset.dbss` | 2,744  | 274 Offset Row | 10                        |

| Layout | File              | Known             | Unknown    |
| ------ | ----------------- | ----------------- | ---------- |
| 2      | `form.dbss`       | 76,275 B (100.0%) | 0 B (0.0%) |
| 2      | `formoffset.dbss` | 2,974 B (100.0%)  | 0 B (0.0%) |
| 1      | `form.dbss`       | 69,214 B (100.0%) | 0 B (0.0%) |
| 1      | `formoffset.dbss` | 2,744 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2765   | Layout 2 |
| 2519   | Layout 2 |
| 2313   | Layout 2 |
| 2107   | Layout 2 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                      |
| ---------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `formoffset.dbss`            | Optional | `index -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a listed character without a row shows as plain text   |
| `languagedata_en.loc`        | Optional | Names of the listed characters, LOC type 6                                                |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 31 bytes + icon texts + character keys)

| Offset                       | Type                     | Field               | Notes                                                                                      |
| ---------------------------- | ------------------------ | ------------------- | ------------------------------------------------------------------------------------------ |
| `+0x00`                      | u16                      | index               | Row key: the form                                                                          |
| `+0x02`                      | u16                      | index_dup           | Equal to `index` on every row; the offset index points here                               |
| `+0x04`                      | u8                       | type                | `gc::FormType`: `0` horse, `1` the enum count, where the sheet leaves it blank; see Form Types |
| `+0x05`                      | u32                      | action_index        | Action chart index of the look; `0` on 48 rows (client 3482)                               |
| `+0x09`                      | u16                      | tier                | Horse tier `1` to `9`; `0` on 72 rows (client 3482)                                         |
| `+0x0B`                      | str16                    | icon_1              | Stable icon under `ui_texture/` (`New_UI_Common_forLua\Window\Stable\Horse_01.dds`); empty on form `9` |
| `icon_1+0x00`                | str16                    | icon_2              | Second icon: `UI_Main_Mercenary_Icon_Horse.dds` on 295 rows, the goat icon on form `33`, empty on form `9` (client 3482) |
| `icon_2+0x00`                | u32                      | character_key_count | Number of `character_keys`; `0` on 295 of 297 rows (client 3482)                           |
| `icon_2+0x04`                | u16[character_key_count] | character_keys      | `characterstatic.dbss` characters that can take this form                                 |

The rows are in no key order; client 3482 opens with 239, 238, 237.

### `formoffset.dbss`

Bare offset table into `form.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                        |
| ------- | ----------------- | ----- | ---------------------------- |
| `+0x00` | u32               | count | Equals the `form.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row               |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u16  | index       | Key of the row it points at             |
| `+0x02` | u32  | data_offset | Row start + 2, at `index_dup`           |
| `+0x06` | u32  | data_size   | The row less its leading `index`        |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on clients 1784 and 3482 every index row points at
the row whose `index` is its key.

## Layout 1

The row has no character key list. Only the Row differs from Layout 2.

### Row (variable: 27 bytes + icon texts)

| Offset   | Type  | Field        | Notes                          |
| -------- | ----- | ------------ | ------------------------------ |
| `+0x00`  | u16   | index        | Row key: the form              |
| `+0x02`  | u16   | index_dup    | Equal to `index` on every row  |
| `+0x04`  | u8    | type         | `0` horse, `1` the enum count  |
| `+0x05`  | u32   | action_index | Action chart index of the look |
| `+0x09`  | u16   | tier         | Horse tier                     |
| `+0x0B`  | str16 | icon_1       | Stable icon                    |
| `icon_1+0x00` | str16 | icon_2  | Second icon                    |

## Form Types

The 2016 client's `gc::FormType` (u8) has two values. The `Form_Table`
sheet leaves `Type` blank on 166 rows; the client file holds `1` there.

| Value | Name              | Rows (client 3482) |
| ----- | ----------------- | ------------------ |
| 0     | `eFormType_Horse` | 115                |
| 1     | `eFormType_Count` | 182                |

## Field Names

The 2016 `gc::FormStaticStatus` holds `_index` (u16), `_type`
(`gc::FormType`, u8), `_actionIndex` (u32), `_tier` (u16), `_icon1` and
`_icon2` in this order, the members of Layout 1 packed. The `Form_Table`
sheet of a private server's `DataSheets.bexcel` on client 1784 has the
columns `Index`, `Type`, `ActionIndex`, `Tier`, `IconImageFile1` and
`IconImageFile2`, 274 rows.

| Field        | Column           | Same value (client 1784) | Same value (client 3482) |
| ------------ | ---------------- | ------------------------ | ------------------------ |
| index        | `Index`          | 272 of 272               | 274 of 274               |
| type         | `Type`           | 272 of 272, blank as `1` | 274 of 274, blank as `1` |
| action_index | `ActionIndex`    | 272 of 272               | 274 of 274               |
| tier         | `Tier`           | 272 of 272               | 269 of 274               |
| icon_1       | `IconImageFile1` | 272 of 272               | 274 of 274               |
| icon_2       | `IconImageFile2` | 272 of 272               | 274 of 274               |

On client 3482 forms `265` to `269` hold tier `9` where the sheet has `4`.
The sheet's `#Grade` note column is not compiled.

`character_keys` has no sheet column. The client Lua (3482) looks forms up
by character: `panel_dialog_servant_fantasyskin_all_1.luac` asks
`formManager:getFormCountByCharacterKey(key)` and
`formManager:getFormByCharacterKey(key, 0)` for the horse in the fantasy
skin window, and the three keys the file lists (`31539`, `31558`, `31562`)
are all Mythical Arduanatt (LOC type 6).

## Notes

- The look change window (`panel_dialog_servantlookchange_all_2.luac`)
  reads forms per tier with `formManager:getFormTierSize(tier)` and
  `formManager:getFormTierStaticWrapper(tier, i)`, and compares
  `formInfo:getActionIndex()` with the horse's own action index. The horse
  upgrade window (`panel_window_servantupgrade_1.luac`) shows
  `ToClient_FormStaticStatusWrapper(characterKey):getIcon1()`.
- On client 3482 forms `260` (`31562`) and `275` (`31539`, `31558`) list
  characters; the other 295 rows have an empty list.
- Form `9` has empty icons on clients 1784 and 3482.

## Open Questions

### What Type 0 Changes

All 115 forms with `type` `0` (`eFormType_Horse`) use a `Horse_*.dds`
stable icon, but so do 119 of the 182 forms with `type` `1`, the value the
sheet's blank compiles to. No client Lua (3482) reads the type, so which
window or rule tells the two horse groups apart is open.
