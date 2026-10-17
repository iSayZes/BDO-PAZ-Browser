# `extractitem.dbss` Format

## Purpose

Reform stone extraction (`PANEL_EXTRACTIONSYSTEM_TITLE` "Extract Reform
Stone"): the blacksmith window that splits reformed gear back into the gear
it was made from and the reform stone. A row names the reformed item, the
item the extraction uses up, and the two items it returns.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes   | Records         | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ------- | --------------- | --------- |
| 1      | 1784 and later | 3473    | `extractitem.dbss`       | 112,132 | 2,336 Row       | 48        |
| 1      | 1784 and later | 3473    | `extractitemoffset.dbss` | 28,036  | 2,336 Index Row | 12        |

| Layout | File                     | Known              | Unknown    |
| ------ | ------------------------ | ------------------ | ---------- |
| 1      | `extractitem.dbss`       | 112,132 B (100.0%) | 0 B (0.0%) |
| 1      | `extractitemoffset.dbss` | 28,036 B (100.0%)  | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                      |
| ------------------------- | -------- | --------------------------------------------------------- |
| `extractitemoffset.dbss`  | Optional | `item_id -> (data_offset, data_size)` index, see below; the rows can be walked without it |
| [`itemimprovement.dbss`](itemimprovement_dbss.md) | Optional | Reform records; the handler's Reform Group column, see Notes |
| [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md) | Optional | Reform stone groups; picks one group when a reform pair has several |

Item names come from LOC type 0.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                                     |
| ------- | ---------- | ----- | --------------------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `2,336` on client 3464                    |
| `+0x04` | Row[count] | rows  | `count` 48-byte rows, back to back to the end of the file |

### Row (48 bytes)

The row is four 12-byte slots of a u32 item ID and its u64 count. Every
count is `1` on all 2,336 rows (client 3473).

| Offset  | Type | Field                 | Notes                                                         |
| ------- | ---- | --------------------- | ------------------------------------------------------------- |
| `+0x00` | u32  | item_id               | Reformed gear the window takes; unique per row, the index key |
| `+0x04` | u64  | item_count            | Fixed `1`, see Field Names                                    |
| `+0x0C` | u32  | need_item_id          | Item the extraction uses up, see below                        |
| `+0x10` | u64  | need_item_count       | How many `need_item_id` the extraction uses up                |
| `+0x18` | u32  | result_item_id        | Gear returned; never equal to `item_id`                       |
| `+0x1C` | u64  | result_item_count     | Fixed `1`, see Field Names                                    |
| `+0x24` | u32  | result_material_id    | Reform stone (or other material) returned                     |
| `+0x28` | u64  | result_material_count | Fixed `1`, see Field Names                                    |

Byte `+0x03` of each item ID is `0` on every row, so no ID carries an
enchant level in its top byte. The rows are not sorted by `item_id`.

Each `result_material_id` goes with one `need_item_id` (client 3464):

| need_item_id                         | result_material_id                                   | Rows |
| ------------------------------------ | ---------------------------------------------------- | ---- |
| `320060` Mirror of Equilibrium       | `9771` Inverted Heart of Garmoth                     | 844  |
| `320060` Mirror of Equilibrium       | `9793` Heart of Kutum                                | 455  |
| `320060` Mirror of Equilibrium       | `9787` Heart of Karanda                              | 363  |
| `320060` Mirror of Equilibrium       | `8421` Blessed Soul Fragment, `8432` Exalted Soul Fragment | 26 each |
| `320060` Mirror of Equilibrium       | Six Cups (`8141`, `8148`, `8149`, `8181`, `8182`, `8417`) | 10 each |
| `320060` Mirror of Equilibrium       | `9788` Obsidian Specter's Energy                     | 4    |
| `320060` Mirror of Equilibrium       | `820974` to `820977` Cups, `821251` Flawless Herald's Crystal | 3 each |
| `320060` Mirror of Equilibrium       | `820018` Gauche Rawr-Rawr's Heart                    | 2    |
| `320060` Mirror of Equilibrium       | `820969` Crimson Behelit Alchemy Stone Appearance    | 1    |
| `4929` Restoration Stone             | `4912` Ultimate Weapon Reform Stone                  | 407  |
| `4929` Restoration Stone             | `4913` Ultimate Armor Reform Stone                   | 44   |
| `4929` Restoration Stone             | `8179` Sunset Glow Crystal                           | 6    |
| `8172` Combatant's Restoration Stone | `8170` Combatant's Stone (Weapon)                    | 79   |
| `8172` Combatant's Restoration Stone | `8171` Combatant's Stone (Armor)                     | 4    |

The three need items' own texts list these pairs: the Mirror of Equilibrium
(TextBind `MIRROR_OF_EQUILIBRIUM`) reads "Extract Heart of Karanda from
Storm Devoured gear", "Extract Inverted Heart of Garmoth from Fiery gear"
and so on; Restoration Stone (`4929`) names the two Ultimate Reform Stones
and Sunset Glow Crystal; Combatant's Restoration Stone (`8172`) names the
two Combatant's Stones.

### `extractitemoffset.dbss`

| Offset  | Type             | Field | Notes                                      |
| ------- | ---------------- | ----- | ------------------------------------------ |
| `+0x00` | u32              | count | Equals the `extractitem.dbss` count        |
| `+0x04` | Index Row[count] | rows  | `count` 12-byte rows; no magic, no trailer |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                         |
| ------- | ---- | ----------- | --------------------------------------------- |
| `+0x00` | u32  | item_id     | Row key, the `item_id` at `data_offset`       |
| `+0x04` | u32  | data_offset | Row start, the `item_id` itself (not past it) |
| `+0x08` | u32  | data_size   | `48`, the whole row                           |

Unlike the `itemimprovementoffset.dbss` index, `data_offset` points at the
key and `data_size` covers it. The index rows are not in file order; on
client 3464 the 2,336 offsets are exactly the 2,336 row starts, and the key
at each offset equals the index `item_id`.

## Field Names

The row is the `Item_ImprovementExtract_Table` sheet that a private server
on client 1784 ships in its `DataSheets.bexcel`. Its columns are
`ExtractionItem`, `NeedExtractMaterialKey`, `NeedExtractMaterialCount`,
`ExtractDropItem1`, `ExtractDropItem2` and `ContentsGroupKey`; the last one
is not in the row.

| Field                 | Column                     |
| --------------------- | -------------------------- |
| `item_id`             | `ExtractionItem`           |
| `need_item_id`        | `NeedExtractMaterialKey`   |
| `need_item_count`     | `NeedExtractMaterialCount` |
| `result_item_id`      | `ExtractDropItem1`         |
| `result_material_id`  | `ExtractDropItem2`         |

Matched by `ExtractionItem` against client 3473, the sheet and the client
file share 1,127 keys. `need_item_id` and `result_item_id` match on all
1,127 and `result_material_id` on 1,086; the other 41 are Cups whose key
changed (sheet `8135`, `8146` and `8147`, client `8141`, `8148`, `8149`,
`8181` and `8182`). That private server's own `extractitem.dbss`, built from
the sheet, holds 1,196 rows; all three item columns match on every one.

`NeedExtractMaterialCount` is `1` on every sheet row, so the values do not
place it. The server dump of that private server does. Its
`Item_ImprovementExtract_Table` loader builds four (item key, 8-byte count)
pairs per row, in row order: `ExtractionItem` with a literal count of `1`,
`NeedExtractMaterialKey` with `NeedExtractMaterialCount`, then
`ExtractDropItem1` and `ExtractDropItem2` (one `ExtractDropItem%#` string,
read for 1 and 2), each with a literal `1`. It rejects a row when any key is
`0` or any count is not above `0`. So `need_item_count` is the only count
the sheet sets, and the other three are `1` by the loader.

Neither the 2016 client with debug symbols nor the BdoEmu tables of client
519 have an extraction type or table.

## Notes

- The window is `panel_window_extraction_system_all`
  (`PaGlobal_Extraction_System_All`, decompiled with unluac). For the item in
  the window it calls `ToClient_ExtractNeedItemEnchantKey(itemKey)` for the
  item to use up (shown with `PANEL_EXTRACTIONSYSTEM_NEEDCATALYST` "※ You
  need a [{itemName}]." when the inventory has none),
  `ToClient_ExtractToItemEnchantKey(itemKey, 0)` for the result item and
  `ToClient_ExtractToItemEnchantKey(itemKey, 1)` for the result material, the
  three IDs at `+0x0C`, `+0x18` and `+0x24`. The inventory list takes items
  for which `ToClient_isExtractFromItem(key)` is true, and the request is
  `ToClient_requestExtractItem(extractableSlotNo, materialSlotNo)`. The
  result line is `LUA_EXTRACTIONSYSTEM_RESULTMSG` "{item1} and {itme2} were
  separated.", and the two result icons hide their count. The need item is
  drawn with a literal `1` (or `0` when the inventory has none), not with
  `need_item_count`.
- The window refuses gear with Caphras EXP (`LUA_EXTRACTIONSYSTEM_FAIL_DESC_1`)
  or transfused crystals (`LUA_EXTRACTIONSYSTEM_FAIL_DESC_2`); the table has no
  field for either.
- A row is a [`itemimprovement.dbss`](itemimprovement_dbss.md) reform run
  backwards. On client 3464, 2,323 of the 2,336 rows have a 5-item reform
  record whose result is `item_id` and whose input is `result_item_id`, and
  `result_material_id` is a stone of that record's group in
  [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md). This holds
  for all three need items, the Ultimate and Combatant's gear included.
  20 (result, input) pairs have reform records in two groups; on the 10
  rows that hit one (client 3464), Dandelion Purgatum gear from `742928` to
  `743330`, only one of the two groups holds `result_material_id` as a
  stone. The handler's Reform Group is that one group, and `-` on the other
  13 rows.
- The other 13 rows (client 3464) return a different gear key than the
  reform input: ten Dandelion Purgatum rows (`742932`, `742933`, `743032`,
  `743033`, `743132`, `743133`, `743232`, `743233`, `743332`, `743333`) and
  three Hexround rows (`736624`, `736724`, `736824`). For example `743332`
  (Fiery Dandelion Purgatum) is reformed from `743232` but extracts to
  `743231` (Dandelion Purgatum).
- 41 `result_item_id` values (client 3464) are themselves an `item_id` of
  another row, so reformed gear can be extracted down more than one step.
- One `item_id` has no LOC type 0 name on client 3464: `748603`, which
  extracts to `748601` Dandelion Enlightened Blade and Heart of Karanda. The
  handler shows the Korean name `itemenchant.dbss` stores for it
  (폭풍을 삼킨 단델리온 선검).
- calpheonlabs' page gives the example `731222` and `320060` to `694273` and
  `9771` (Inverted Heart of Garmoth). On client 3464 the `731222` row returns
  `9787` (Heart of Karanda), which is what the Mirror of Equilibrium text
  says for Storm Devoured gear; its capture has 2,328 rows.

## Open Questions

### Enchant Level on the Key

The Lua passes the item's `getKey()`, an item enchant key, to
`ToClient_isExtractFromItem` and the two lookup functions, while the table
stores plain item IDs. Whether the client drops the enchant level before
the lookup, and whether the returned gear keeps the enchant level of the
extracted gear, is not in the table.
