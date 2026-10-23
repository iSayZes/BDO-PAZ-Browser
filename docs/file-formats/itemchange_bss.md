# `itemchange.bss` Format

## Purpose

The Change Item conversions: per row an armor item and the costume it turns
into in the Change Item window (`[Warrior] Calpheon Noble Suit` to
`[Warrior] Calpheon Noble Suit (Costume)`). The window
(`panel_window_changeitem_renew.luac`) offers an inventory item only when
`getItemChange(itemKey)` finds a row for it and shows the item that row
makes.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File             | Bytes | Records | Row bytes |
| ------ | ------------- | ------- | ---------------- | ----- | ------- | --------- |
| 2      | 822 and later | 3482    | `itemchange.bss` | 6,548 | 408 Row | 16        |
| 1      | 435 to 794    | 794     | `itemchange.bss` | 3,908 | 244 Row | 16        |

| Layout | File             | Known            | Unknown    |
| ------ | ---------------- | ---------------- | ---------- |
| 2      | `itemchange.bss` | 6,548 B (100.0%) | 0 B (0.0%) |
| 1      | `itemchange.bss` | 3,908 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3454   | Layout 2 |
| 3412   | Layout 2 |
| 3381   | Layout 2 |
| 3349   | Layout 2 |
| 3314   | Layout 2 |
| 3283   | Layout 2 |
| 3251   | Layout 2 |
| 3212   | Layout 2 |
| 3177   | Layout 2 |
| 3144   | Layout 2 |
| 3103   | Layout 2 |
| 3062   | Layout 2 |
| 3037   | Layout 2 |
| 3002   | Layout 2 |
| 2959   | Layout 2 |
| 2923   | Layout 2 |
| 2900   | Layout 2 |
| 2872   | Layout 2 |
| 2834   | Layout 2 |
| 2803   | Layout 2 |
| 2765   | Layout 2 |
| 2736   | Layout 2 |
| 2703   | Layout 2 |
| 2665   | Layout 2 |
| 2637   | Layout 2 |
| 2606   | Layout 2 |
| 2583   | Layout 2 |
| 2545   | Layout 2 |
| 2519   | Layout 2 |
| 2498   | Layout 2 |
| 2468   | Layout 2 |
| 2438   | Layout 2 |
| 2414   | Layout 2 |
| 2384   | Layout 2 |
| 2358   | Layout 2 |
| 2335   | Layout 2 |
| 2313   | Layout 2 |
| 2290   | Layout 2 |
| 2250   | Layout 2 |
| 2224   | Layout 2 |
| 2203   | Layout 2 |
| 2179   | Layout 2 |
| 2151   | Layout 2 |
| 2134   | Layout 2 |
| 2107   | Layout 2 |
| 2073   | Layout 2 |
| 2052   | Layout 2 |
| 2011   | Layout 2 |
| 1996   | Layout 2 |
| 1969   | Layout 2 |
| 1937   | Layout 2 |
| 1914   | Layout 2 |
| 1886   | Layout 2 |
| 1866   | Layout 2 |
| 1838   | Layout 2 |
| 1818   | Layout 2 |
| 1794   | Layout 2 |
| 1784   | Layout 2 |
| 1749   | Layout 2 |
| 1717   | Layout 2 |
| 1698   | Layout 2 |
| 1674   | Layout 2 |
| 1636   | Layout 2 |
| 1608   | Layout 2 |
| 1587   | Layout 2 |
| 1565   | Layout 2 |
| 1537   | Layout 2 |
| 1509   | Layout 2 |
| 1485   | Layout 2 |
| 1466   | Layout 2 |
| 1445   | Layout 2 |
| 1426   | Layout 2 |
| 1409   | Layout 2 |
| 1390   | Layout 2 |
| 1372   | Layout 2 |
| 1360   | Layout 2 |
| 1348   | Layout 2 |
| 1338   | Layout 2 |
| 1324   | Layout 2 |
| 1316   | Layout 2 |
| 1309   | Layout 2 |
| 1286   | Layout 2 |
| 1256   | Layout 2 |
| 1230   | Layout 2 |
| 1211   | Layout 2 |
| 1194   | Layout 2 |
| 1177   | Layout 2 |
| 1156   | Layout 2 |
| 1127   | Layout 2 |
| 1109   | Layout 2 |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | Layout 2 |
| 794    | Layout 1 |
| 748    | Layout 1 |
| 711    | Layout 1 |
| 683    | Layout 1 |
| 656    | Layout 1 |
| 630    | Layout 1 |
| 606    | Layout 1 |
| 577    | Layout 1 |
| 542    | Layout 1 |
| 526    | Layout 1 |
| 508    | Layout 1 |
| 485    | Layout 1 |
| 457    | Layout 1 |
| 435    | Layout 1 |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (16 bytes)

The 2016 `gc::ItemChangeStaticStatus` packed, after its u16 map key: its
members in order, without the alignment padding after `_key` and without the
two `gc::ItemEnchantStaticStatus` pointers.

| Offset  | Type | Field         | Notes                                                                                  |
| ------- | ---- | ------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u16  | key           | Row key; unique, the rows are in no key order                                          |
| `+0x02` | u16  | key_dup       | Equals `key` on every row of clients 1784 and 3482                                     |
| `+0x04` | u32  | from_item_key | Item the conversion takes, a packed item key (`enchant_level << 24 \| item_id`)          |
| `+0x08` | u32  | to_item_key   | Item it makes, a packed item key; enhancement level `0` on every row of clients 1784 and 3482 |
| `+0x0C` | i32  | type          | `0` on every row of clients 1784 and 3482                                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

A bare row count and the rows: no PABR magic and no string table. Only the
File Layout differs from Layout 2.

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

## Field Names

The 2016 `gc::ItemChangeStaticStatus` holds `_key` (u16), `_fromItemKey`
and `_toItemKey` (`gc::ItemEnchantKey`), `_type` (int) and a pointer to each
item's `gc::ItemEnchantStaticStatus`; its manager keys the rows by a u16
`gc::KeyType`, which the file stores before the row. The `ItemChange_Table`
sheet of a private server's `DataSheets.bexcel` on client 1784 has the
columns `Index`, `FromItemKey`, `FromEnchantLevel`, `ToItemKey`,
`ToEnchantLevel` and `Type`:

| Field         | Column                              | Same value (client 1784) | Same value (client 3482) |
| ------------- | ----------------------------------- | ------------------------ | ------------------------ |
| key, key_dup  | `Index`                             | 324 of 324               | 317 of 408               |
| from_item_key | `FromItemKey`, `FromEnchantLevel`   | 324 of 324               | 317 of 317               |
| to_item_key   | `ToItemKey`, `ToEnchantLevel`       | 324 of 324               | 317 of 317               |
| type          | `Type`                              | 324 of 324               | 317 of 317               |

The sheet has 327 keys; client 3482 adds 91 keys the sheet does not have.
Both enhancement levels and `Type` are `0` on every sheet row, so the
column match places `type` by the 2016 member order only.

## Notes

- On client 3482, 406 of the 408 rows take a different item; two items have
  two rows each, as in the sheet (`FromItemKey` 12581 and 12597).
- The made item is the costume of the item it takes on every row checked:
  `12672` [Mystic] Delphe Knight Armor makes `12683` [Mystic] Delphe Knight
  Armor (Costume), `933420` [Agent] Serendian Smith Garb makes `933421`.
- The handler (`_bss/itemchange/`) shows one row per conversion with both
  items.

## Open Questions

### What `type` Selects

`type` is `0` on every row of clients 1784 and 3482 and in every sheet row.
The client 3482 Lua reads `getItemChange(itemKey)` and the item it returns,
never a type.
