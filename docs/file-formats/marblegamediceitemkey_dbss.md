# `marblegamediceitemkey.dbss` Format

## Purpose

The keys of the Black Spirit's Adventure dice items: the dice and the board
cards (Pace of Delight, Lucky Day, Fated Encounter and more) a player rolls
or plays on the board. The file holds the keys only, 45 on client 3482 and
28 on client 1784. Which dice drop together is in
[`marblegamediceitemgroup.dbss`](marblegamediceitemgroup_dbss.md).
Companion `marblegamediceitemkeyoffset.dbss` lists where every key sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ----- | ------------- | --------- |
| 1      | 1485 and later | 3482    | `marblegamediceitemkey.dbss`       | 184   | 45 Row        | 4         |
| 1      | 1485 and later | 3482    | `marblegamediceitemkeyoffset.dbss` | 544   | 45 Offset Row | 12        |

| Layout | File                               | Known          | Unknown    |
| ------ | ---------------------------------- | -------------- | ---------- |
| 1      | `marblegamediceitemkey.dbss`       | 184 B (100.0%) | 0 B (0.0%) |
| 1      | `marblegamediceitemkeyoffset.dbss` | 544 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                                          |
| ---------------------------------- | -------- | ----------------------------------------------------------------------------- |
| `marblegamediceitemkeyoffset.dbss` | Optional | `dice_item_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `marblegamediceitemgroup.dbss`     | Optional | The drop groups that list each key, for the Drop Groups and Items columns     |
| `itemenchant.dbss`                 | Optional | The items that grant those groups; the handler reads them from the `MARBLE_DICE_GROUP_ITEMS` lookup index, not as a companion |
| `languagedata_en.loc`              | Optional | Item names (type 0)                                                           |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of keys |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3482 the file is 4 + 45 x 4 = 184 bytes.

### Row (4 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | dice_item_key | Row key; each key once. See Keys                            |

### `marblegamediceitemkeyoffset.dbss`

Bare offset table into `marblegamediceitemkey.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                        |
| ------- | ----------------- | ----- | -------------------------------------------- |
| `+0x00` | u32               | count | Equals the `marblegamediceitemkey.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                               |

### Offset Row (12 bytes)

| Offset  | Type | Field         | Notes                                   |
| ------- | ---- | ------------- | --------------------------------------- |
| `+0x00` | u32  | dice_item_key | Key of the row it points at             |
| `+0x04` | u32  | data_offset   | Row start, at `dice_item_key`           |
| `+0x08` | u32  | data_size     | `4` on every row                        |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order; on clients 1784 and 3482 every index row
points at the row with its key.

## Keys

The keys fall in ranges. The Item column names the items whose contents
event `98` grants a drop group that holds the key alone (see
[`marblegamediceitemgroup.dbss`](marblegamediceitemgroup_dbss.md)), on
client 3482; the Sheet Note column translates the Korean `#Desc` note
column of the `DiceItem_Table` sheet of a private server on client 1784.

| Keys         | Item (client 3482)                                                  | Sheet Note (client 1784)                     |
| ------------ | ------------------------------------------------------------------- | -------------------------------------------- |
| `1`          | Black Spirit's Dice                                                 | A die that rolls 1 to 6                      |
| `2` to `7`   | Black Spirit's Special Dice (1, 1) to (6,6)                         | A die that rolls only 1, ..., only 6         |
| `8`          | Black Spirit's Dice                                                 | Golden die                                   |
| `11` to `14` | [Event] Black Spirit's Purple, Orange, Small Snowflake and Large Snowflake Die | Purple, orange, small and large snowflake die |
| `15` to `31` | [Event] dice, `24` to `29` Festival Die (1) to (6); `18` and `19` have none | Not in the sheet                    |
| `101` to `106` | Pace of Delight - 1 Square to 6 Squares                           | Pace of Delight, 1 to 6 squares              |
| `201`, `202` | None                                                                | Move back 1 or 2 squares                     |
| `301` to `303` | Lucky Day - 1 to 3 Additional Rolls                               | Lucky Day, 1 to 3 more rolls                 |
| `401`        | Fated Encounter                                                     | Fated Encounter                              |
| `501`        | None                                                                | Resets the free die delay                    |
| `601`, `701`, `801` | Nice Fluke!, Clattering Rattle, Cosmos Cataclysm             | The Korean names of the same three cards     |

## Field Names

The `DiceItem_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `DiceItemKey` and `ItemType`; its 28 keys are
the 28 keys of the client 1784 file, and all 28 are in the client 3482
file. The `.xlsm` copy of the sheet
(`datasheet_itemdatatable_marblegamedice.xlsm`) adds the note column
`#Desc`, which is not compiled. `ItemType` (`0` on `1` to `8`, `2` on `11`
to `14`, `1` on the board cards from `101`) is not in the client file: a
row is the key alone.

## Notes

- Black Spirit's Adventure runs in a web control: `panel_eventmarblegame.luac`
  on client 3482 opens `bAdventureWebUrl .. "/MarbleGame/EventStart"`, and
  no client Lua reads this table.
- The Yar! dice keys of [`yachtdice.dbss`](yachtdice_dbss.md) (`1` to `15`)
  overlap these keys by number only. The Yar! sheets (`DiceList`,
  `DicePreset`) are in `datasheet_minigame.xlsm`, this one in
  `datasheet_itemdatatable_marblegamedice.xlsm`, and a Yar! die is six
  `yachtbasecard.dbss` faces, so the view does not link the two.
- The view shows each key with the drop groups that list it (each a link to
  its `marblegamediceitemgroup.dbss` row) and the items that grant those
  groups. Keys `201`, `202` and `501` are in no group on clients 1784 and
  3482.

## Open Questions

### How Keys Outside Every Group Are Handed Out

No drop group lists `201`, `202` (move back) or `501` (free die delay
reset), and no item grants them, on clients 1784 and 3482. Whether the
board hands them out through its squares on the web side is open.
