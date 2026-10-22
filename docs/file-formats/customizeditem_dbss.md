# `customizeditem.dbss` Format

## Purpose

Item lists for boxes that give a different item to each character: an item
whose contents event is `31 CustomizedItemBox` (`itemenchant.dbss`
`contents_event_type`) names one record here by its
`contents_event_param1`, and the record lists condition scripts with the item
each one gives. Most conditions are `checkClass(N);`, so an outfit or weapon
box hands out the version for the opening character's class. The pearl shop
Lua (`panel_ingamecashshop_setequip.luac`,
`panel_pearlshop_displaycontroller.luac`) reads a record through
`ToClient_getCustomizedItemStaticStatusWrapper(CustomizedItemKey(itemSSW:getContentsEventParam1()))`
and takes `getMatchedItem()`, the item for the current character, to preview
the box contents.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes   | Records                 | Row bytes               |
| ------ | -------------- | ------- | --------------------------- | ------- | ----------------------- | ----------------------- |
| 1      | 1348 and later | 3482    | `customizeditem.dbss`       | 763,556 | 18,295 Item, 879 Record | 40 to 54, 41 on average |
| 1      | 1348 and later | 3482    | `customizeditemoffset.dbss` | 8,794   | 879 Index Row           | 10                      |

| Layout | File                        | Known              | Unknown    |
| ------ | --------------------------- | ------------------ | ---------- |
| 1      | `customizeditem.dbss`       | 763,556 B (100.0%) | 0 B (0.0%) |
| 1      | `customizeditemoffset.dbss` | 8,794 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                        | Required | Role                                                                                      |
| --------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `customizeditemoffset.dbss` | Optional | `customized_item_key -> (data_offset, data_size)` index, see below; the records can be walked without it |
| `languagedata_en.loc`       | Optional | Item names (LOC type 0), class names (LOC type 21) and quest titles (LOC type 18) for the view |
| `itemenchant.dbss`          | Optional | The box items that open each record, for the Boxes column; the handler reads them from the `CUSTOMIZED_ITEM_BOXES` lookup index, not as a companion |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                           |
| ------- | ------------- | ------- | ----------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `879` on client 3482         |
| `+0x04` | Record[count] | records | Back to back to the end of the file; see Record |

### Record (variable: 8 bytes + items)

| Offset         | Type              | Field                   | Notes                                                                          |
| -------------- | ----------------- | ----------------------- | ------------------------------------------------------------------------------ |
| `+0x00`        | u16               | customized_item_key     | The record key, the `contents_event_param1` of the box items that open it      |
| `+0x02`        | u32               | item_count              | Number of `items`; the index's `data_offset` points here                       |
| `+0x06`        | Item[item_count]  | items                   | Condition and item pairs in sheet column order; see Item                       |
| `items+0x00`   | u16               | customized_item_key_dup | Equal to `customized_item_key` in every record (clients 1784 and 3482)         |

### Item (variable: 12 bytes + condition text)

| Offset           | Type  | Field     | Notes                                                                                  |
| ---------------- | ----- | --------- | -------------------------------------------------------------------------------------- |
| `+0x00`          | str16 | condition | Condition script, see Conditions                                                       |
| `condition+0x00` | u32   | item_key  | Packed item key, `enchant_level << 24 \| item_id`: the item and enhancement level given |

### `customizeditemoffset.dbss`

| Offset  | Type             | Field | Notes                                   |
| ------- | ---------------- | ----- | --------------------------------------- |
| `+0x00` | u32              | count | Equals the `customizeditem.dbss` count  |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row     |

### Index Row (10 bytes)

| Offset  | Type | Field               | Notes                                               |
| ------- | ---- | ------------------- | --------------------------------------------------- |
| `+0x00` | u16  | customized_item_key | Record key                                          |
| `+0x02` | u32  | data_offset         | Record start + 2, at `item_count`                   |
| `+0x06` | u32  | data_size           | Record size - 2, through `customized_item_key_dup`  |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The rows are
not in file order; on clients 1784 and 3482 every row matches the record
walked from the start of the file.

## Field Names

The record is the `CustomizedItemList` sheet of a private server's
`DataSheets.bexcel` on client 1784: `CustomizedItemKey`, then up to 25
column triples `ConditionN`, `ItemN` and `EnchantN`. The file stores one
item per filled `ConditionN` and packs `EnchantN` into the top byte of
`ItemN`. The 2016 `gc::CustomizedItemStaticStatus` has the same shape:
`_itemList` (a vector of `gc::CustomizedItem` with `_conditionString` and the
`gc::ItemEnchantKey` `_itemKey`), then the u16 `_key`, which is
`customized_item_key_dup`; the leading `customized_item_key` is the map key.

| Field               | Column                    | Match                                                                                   |
| ------------------- | ------------------------- | --------------------------------------------------------------------------------------- |
| customized_item_key | `CustomizedItemKey`       | 410 of 410 keys are sheet keys (client 1784), 483 of 879 (client 3482)                 |
| condition           | `ConditionN`              | Same pairs in the same order on 384 of 410 shared keys (client 1784), 38 of 483 (client 3482) |
| item_key            | `ItemN \| EnchantN << 24` | Compared with `condition` as pairs                                                      |

On client 3482, 279 of the 445 shared records that differ keep the sheet's
pairs as their first entries and add pairs behind them for class types the
sheet has none for (`3`, `6`, `7`, `15`, `30`, `32` to `35`). The other 166
differ from the private server's sheet in their items or conditions.

## Conditions

Two script forms occur, counted on client 3482 (18,295 entries):

| Script                      | Entries | Meaning in the view                                                       |
| --------------------------- | ------- | ------------------------------------------------------------------------- |
| `checkClass(N);`            | 18,292  | Class type `N` (`getClassType()`, LOC type 21 name)                       |
| `clearquest(chain,quest);`  | 3       | Quest done, LOC type 18 title; record `497`, three `[Crossroad]` quests  |

Record `497` is the Mysterious Secret Note (item `66297`): it gives the
Secret Dispatch: The Giving Tree item `66298`, `66299` or `66300` after
quest `22226` part `20`, `21` or `22` ([Crossroad] For Calpheon, For
O'dyllita, For Power).

## Notes

- `item_count` runs from 1 to 32 on client 3482; 304 of the 879 records
  hold 32 entries, one per playable class type (0 to 35 without 13, 14, 18
  and 22).
- 84 records on client 3482 give the same item to every condition.
- Five records (`31`, `32`, `34`, `35`, `42`) list `checkClass(15);` twice
  with the same item on client 3482.
- 4,660 of the 18,295 items on client 3482 carry an enhancement level above
  0 in the top byte, 3,033 of them PRI to PEN (16 to 20).
- On client 3482, 754 `itemenchant.dbss` items have contents event `31`;
  731 of their 740 distinct `contents_event_param1` values are keys here.
  The nine others (`536`, `60013`, `60016`, `60025`, `60113`, `60116`,
  `60119`, `60122`, `60125`) have no record, and 148 records have no box item.
  The `CUSTOMIZED_ITEM_BOXES` lookup index turns `contents_event_param1`
  around: the Boxes column lists the items that open each record, and the
  `itemenchant.dbss` Event Param 1 of a box item links to its record here.
- Client 1784 has 410 records with keys 1 to 485 and the same layout.

## Open Questions

### Boxes Without a Record

Nine `contents_event_param1` values of `CustomizedItemBox` items have no
record on client 3482 (listed in Notes). The items are Awakening Secret Book
Box (65297, `536`), three Enduring Crow Main Weapon Boxes (950323, 950326,
950335: `60013`, `60016`, `60025`) and five Enduring Crow Awakening Weapon
Boxes (950423 to 950435: `60113` to `60125`). No client Lua shows what opening
such a box does: only `panel_ingamecashshop_setequip.luac` and
`panel_pearlshop_displaycontroller.luac` read a record, and
`getMatchedItem()` is only read after a `nil` check of the wrapper.
