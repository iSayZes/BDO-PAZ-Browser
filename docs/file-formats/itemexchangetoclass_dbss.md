# `itemexchangetoclass.dbss` Format

## Purpose

The weapon exchange groups behind the Weapon Exchange window
(`Panel_Window_ChangeItem_All`): each row is one group of equivalent
weapons, such as the Rusty weapons (key `1`) or the Tuvala main weapons
(key `165`), with one item key per class type. Exchanging an item for
another class gives the item in that class's slot of the item's group.
`itemexchangetoclassoffset.dbss` is the index into it, and
[`itemexchangetoclassmapkey.bss`](itemexchangetoclassmapkey_bss.md) maps
each item back to its group.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ------ | -------------- | --------- |
| 2      | 3474 and later | 3474    | `itemexchangetoclass.dbss`       | 39,404 | 200 Row        | 197       |
| 2      | 3474 and later | 3474    | `itemexchangetoclassoffset.dbss` | 2,404  | 200 Offset Row | 12        |
| 1      | 1784           | 1784    | `itemexchangetoclass.dbss`       | 22,198 | 162 Row        | 137       |
| 1      | 1784           | 1784    | `itemexchangetoclassoffset.dbss` | 1,948  | 162 Offset Row | 12        |

| Layout | File                             | Known             | Unknown    |
| ------ | -------------------------------- | ----------------- | ---------- |
| 2      | `itemexchangetoclass.dbss`       | 39,404 B (100.0%) | 0 B (0.0%) |
| 2      | `itemexchangetoclassoffset.dbss` | 2,404 B (100.0%)  | 0 B (0.0%) |
| 1      | `itemexchangetoclass.dbss`       | 22,198 B (100.0%) | 0 B (0.0%) |
| 1      | `itemexchangetoclassoffset.dbss` | 1,948 B (100.0%)  | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                             | Required | Role                                                                |
| -------------------------------- | -------- | ------------------------------------------------------------------- |
| `itemexchangetoclassoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows have one fixed size and can be walked without it |
| `languagedata_en.loc`            | Optional | Class name (type `21`, `str_id1` = class type) and item name (type `0`, `str_id1` = item ID) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `200` on client 3474         |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (197 bytes)

| Offset  | Type    | Field         | Notes                                                            |
| ------- | ------- | ------------- | ---------------------------------------------------------------- |
| `+0x00` | i32     | key           | Group key; unique per row                                        |
| `+0x04` | i32     | key_dup       | Equal to `key` in every row; the offset file points here         |
| `+0x08` | u32[47] | item_keys     | Item key (`enchant_level << 24 \| item_id`) per class type, index = class type; `0` for a class without an item |
| `+0xC4` | u8      | exchange_type | See Exchange Types                                               |

The rows are not sorted by key: on client 3474 they start `203`, `202`,
`201` and run down in runs that restart higher (`192` is followed by
`219`).

### `itemexchangetoclassoffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `itemexchangetoclass.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                      |
| ------- | ---- | ----------- | ---------------------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                                |
| `+0x04` | u32  | data_offset | Row start + 4, at `key_dup`                                |
| `+0x08` | u32  | data_size   | The row without its leading `key`: `193` on client 3474    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are not in file order (`139`, `203`, `138`, `202` on client
3474); on clients 1784 and 3474 every index row points at the row with its
key.

## Layout 1

On client 1784 the row holds 32 class slots where Layout 2 has 47, and
`data_size` is `133`. The file has 171 rows.

### Row (137 bytes)

| Offset  | Type    | Field         | Notes                                    |
| ------- | ------- | ------------- | ---------------------------------------- |
| `+0x00` | i32     | key           | Group key; unique per row                |
| `+0x04` | i32     | key_dup       | Equal to `key` in every row              |
| `+0x08` | u32[32] | item_keys     | Item key per class type, index = class type |
| `+0x88` | u8      | exchange_type | See Exchange Types                       |

## Class Slots

The slot index is the class type `getClassType()` returns, so slot `0` is
Warrior, `4` Ranger, `8` Sorceress and `32` Seraph: in every row the class
whose LOC type 21 name matches the item's weapon (Hashashin a Shamshir,
Sage a Kyve, Lahn a Crescent Pendulum). On client 3474 the rows fill class
types 0 to 35 without 13, 14, 18 and 22, the same set as
`PLAYABLE_CLASSES_MASK` in `_common/class_type.py`; slots 36 to 46 are `0`
in every row. Classes that share a weapon share the item: Musa (`20`) and
Maehwa (`21`) both get `13301` Rusty Blade in row `1`.

An item key carries no enhancement level in any row on clients 1784 and
3474 (every `item_keys` value is below `1 << 24`).

## Exchange Types

| Value | Meaning      | Rows on client 3474                             |
| ----- | ------------ | ----------------------------------------------- |
| `0`   | Normal item  | 191                                             |
| `1`   | Season item  | 9: `105` to `107`, `165` to `167`, `170` to `172` |

The names come from the developer note on the `ExchangeType` column of the
`Item_Exchange` sheet in a private server's `.xlsm` on client 1784: the
column tells whether a group is exchanged with a normal weapon exchange
coupon or a season one. Both coupons use `ContentsEventType` `38`
(`ContentsType_ItemExchangeToClass` in the client 3474 Lua enum) and
`ContentsEventParam1` `-1`; `ContentsEventParam2` `0`, `1` and `2` (main,
awakening, sub-weapon) are the normal coupons, `3`, `4` and `5` the season
ones. The client data agrees: rows `165` to `167` hold the Tuvala main,
sub-weapon and awakening weapons and rows `170` to `172` Combatant's
Tuvala weapons, both season server gear.

## Field Names

The row is the 2016 `gc::ItemExchangeToClassStaticStatus`: `_key`
(`gc::KeyType<int,0>`, an i32) and `_itemKey`, a `pa::Array` of 32
`gc::ItemEnchantKey`. The file writes the key before the struct as the
index key and again as `_key`. The 2016 struct has no exchange type; the
`ItemExchangeToClassStaticStatusManager` around it also holds
`_mapKeyFromItemKey`, the item to group map that
[`itemexchangetoclassmapkey.bss`](itemexchangetoclassmapkey_bss.md) stores.

The values match the `Item_Exchange` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `Index`. Its item columns are named
`ClassType0` to `ClassType32` after the class type, each followed by a note
column with the Korean class name; slot `n` matches the column
`ClassTypeN`. The sheet lists `ClassType26` and `ClassType27` twice, an
empty pair first, and the second pair matches.

| Field         | Column                           | Same value (client 1784) | Same value (client 3474) |
| ------------- | -------------------------------- | ------------------------ | ------------------------ |
| key           | `Index`                          | 171 of 171 rows          | 167 of 171 sheet rows    |
| item_keys     | `ClassType0` to `ClassType32`    | 170 of 171               | 161 of 167 shared rows   |
| exchange_type | `ExchangeType`                   | 171 of 171               | 164 of 167               |

- Client 1784 row `171` holds no item, while the sheet lists the Godr-Ayed
  sub-weapons (`738301` up).
- On client 3474 the sheet rows `173` to `176` have no row, and the 33
  rows `177` to `219` have none in the sheet. The 161 matching rows also
  fill class types the sheet leaves empty (3 Wukong, 6 Scholar, 7
  Drakania, 15 Maegu, 30 Woosa, 32 to 35); the comparison skips those. The
  six other rows are `105` to `107`, which the sheet fills with the Tuvala
  weapons `694113` up and client 3474 empties, and `170` to `172`, which
  hold Godr-Ayed sub-weapons and type `0` in the sheet and Combatant's
  Tuvala weapons and type `1` on client 3474.

## Notes

- The Weapon Exchange window Lua (`panel_window_changeitem_all_1.luac` and
  `_2.luac`) opens on `FromClient_UseItemExchangeToClass`, asks
  `getExchangeItem()` for the result of each inventory item and exchanges
  with `exchangeItemToClass()`; it reads no table field itself. The coupon's
  `getContentsEventParam1()` picks the target class, `-1` meaning the
  player's own class.
- On client 3474 rows `105` and `106` hold no item, and row `107` only
  `695193` Tuvala Pendant at class type 35 (Agent), which row `167` holds
  in the same slot. `931802` Ultimate Krea Clavis sits in rows `68` and
  `71` at class type 32. These two are the only items in two rows.
