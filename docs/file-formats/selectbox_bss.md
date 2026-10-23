# `selectbox.bss` Format

## Purpose

The contents of the choose-your-item boxes ("Choose Your Ultimate
Enhancement Box"): per box key up to five types, each a list of items with
a count and the texture name of its tab. The select box window
(`panel_window_selectbox_1.luac`) opens for an item whose contents event is
`__eContentsType_SelectBox`, reads the box key from the item's
`getContentsEventParam1()`, and per type `0` to `__eSelectBoxTypeCount - 1`
shows the items with `ToClient_selectBoxItemEnchantKey(key, type, index)`,
`ToClient_selectBoxItemCount(key, type, index)` and the tab with
`ToClient_selectBoxTextureName(key, type)`. The player picks one item of
each type that has items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes  | Records                               | Row bytes |
| ------ | -------------- | ------- | --------------- | ------ | ------------------------------------- | --------- |
| 1      | 1608 and later | 3482    | `selectbox.bss` | 51,612 | 2,060 Entry, 2,015 Type List, 403 Box | 21        |

| Layout | File            | Known             | Unknown    |
| ------ | --------------- | ----------------- | ---------- |
| 1      | `selectbox.bss` | 51,612 B (100.0%) | 0 B (0.0%) |

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
| 2224   | Layout 1 |
| 2203   | Layout 1 |
| 2179   | Layout 1 |
| 2151   | Layout 1 |
| 2134   | Layout 1 |
| 2107   | Layout 1 |
| 2073   | Layout 1 |
| 2052   | Layout 1 |
| 2011   | Layout 1 |
| 1996   | Layout 1 |
| 1969   | Layout 1 |
| 1937   | Layout 1 |
| 1914   | Layout 1 |
| 1886   | Layout 1 |
| 1866   | Layout 1 |
| 1838   | Layout 1 |
| 1818   | Layout 1 |
| 1794   | Layout 1 |
| 1784   | Layout 1 |
| 1749   | Layout 1 |
| 1717   | Layout 1 |
| 1698   | Layout 1 |
| 1674   | Layout 1 |
| 1636   | Layout 1 |
| 1608   | Layout 1 |
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

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                 | Field        | Notes                                         |
| ------------------- | -------------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32                  | box_count    | Number of boxes                               |
| `+0x08`             | Box[box_count]       | boxes        | See Box; in no key order                      |
| `boxes+0x00`        | String Table         | string_table | See String Table                              |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where `boxes` ends |
| `string_table+0x04` | u32                  | zero         | Always `0`                                    |

### Box (variable: 0 bytes + five type lists)

The box stores no key of its own; every entry repeats it.

| Offset  | Type         | Field      | Notes                                                                 |
| ------- | ------------ | ---------- | --------------------------------------------------------------------- |
| `+0x00` | Type List[5] | type_lists | Type `0` to `4` in order (`__eSelectBoxTypeCount`); see Type List      |

### Type List (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                                    |
| ------- | ------------------ | ----------- | -------------------------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; `0` for a type the box does not use |
| `+0x04` | Entry[entry_count] | entries     | See Entry; the index the Lua passes is the place in this list |

### Entry (21 bytes)

| Offset  | Type | Field        | Notes                                                                                          |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------------------------- |
| `+0x00` | u32  | key          | Box key, the same in every entry of a box; the `contents_event_param1` of the box item          |
| `+0x04` | u8   | type         | The type list the entry is in, `0` to `4`                                                       |
| `+0x05` | u32  | item_key     | Item the entry gives, a packed item key (`enchant_level << 24 \| item_id`); levels up to `20` on client 3482 |
| `+0x09` | u64  | item_count   | How many of the item                                                                            |
| `+0x11` | u32  | texture_name | Index into `strings`: the tab texture (`Combine_Tab_Icon_Daily`)                                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                 |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; 10 on client 3482                                  |
| `+0x04` | pstr[string_count] | strings      | The tab texture names, UTF-8, each once (`Combine_Tab_Icon_Dark`, `Combine_Tab_Icon_Hunt`) |

## Field Names

The `Item_SelectBox` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Key`, `TextureName`, `Type`, `ItemKey`,
`ItemCount` and `ContentsGroupKey`, one sheet row per entry. All 214
entries of the client 1784 file equal a sheet row on `Key`, `ItemKey`,
`ItemCount` and the string `TextureName` points at, with `type` one less
than the sheet's `Type` (`1` to `4`). The sheet has 232 rows; the 18 the file
lacks are the rows of keys 42 and 48 to 50. `ContentsGroupKey` has no field,
and the sheet's `Type` gives the name of `type`.

On client 3482, 216 of the 2,060 entries equal a sheet row; the file has 403
boxes against the sheet's 43 keys.

## Notes

- On clients 1784 and 3482 the entries of a box share one key, each type
  list holds only entries of its own type, and no box has all five lists
  empty. Client 3482 has 354 boxes with one used type, 23 with two, 13 with
  three, 11 with four and 2 with five; the longest list has 10 entries.
- On client 3482, two type lists hold entries with different textures; the
  Lua asks for one texture per type.
- An item whose `contents_event_type` is `114` names a box in
  `contents_event_param1`: on client 3482 the 386 such items name 379
  boxes, every one a key of the file ("Choose Your Ultimate Enhancement
  Box", item 860344, names `403`).
- The handler (`_bss/selectbox/`) shows one row per box with the items of
  each type and the tab textures.

## Open Questions

### Which Boxes No Item Opens

On client 3482, 24 box keys (14, 30, 38, 48, 56, 97, 151, 265, 297 and
more) are named by no item with contents event `114`. They may be boxes of
removed events, or boxes another contents event opens.
