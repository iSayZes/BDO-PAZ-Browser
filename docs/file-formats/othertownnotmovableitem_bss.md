# `othertownnotmovableitem.bss` Format

## Purpose

Items that cannot be put into another town's storage. When the storage window
opens on a town other than the one the player stands in and the client allows
moving items there (`ToClient_ablePushOrPopOtherWareHouse`), the inventory
filter `PaGlobal_Warehouse_All_OtherTownWareHouseItemFilter`
(`panel_window_warehouse_all_2.luac`) greys out every item whose
`movableOtherTown()` is false, and every bag holding one. The file's name
matches that method, and the server message `eErrNoCanNotMovableOtherTownWareHouse`
(`stringtable.bss` sheet `SymbolNo`, LOC type 37) reads "Cannot move to
another town's storage."

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `othertownnotmovableitem.bss` | 24    | 5 Entry | 4         |

| Layout | File                          | Known         | Unknown    |
| ------ | ----------------------------- | ------------- | ---------- |
| 1      | `othertownnotmovableitem.bss` | 24 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0, `str_id1` = `item_id`)    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No magic and no trailer: a count, then the entries to the end of the file.

| Offset  | Type         | Field   | Notes                                    |
| ------- | ------------ | ------- | ---------------------------------------- |
| `+0x00` | u32          | count   | Number of entries                        |
| `+0x04` | Entry[count] | entries | `count` entries of 4 bytes, ending at EOF |

### Entry (4 bytes)

| Offset  | Type | Field   | Notes                                       |
| ------- | ---- | ------- | ------------------------------------------- |
| `+0x00` | u32  | item_id | Item, as in `itemenchant.dbss`; LOC type 0  |

## Items

The five entries on client 3474, in file order:

| Item ID | Item                                  |
| ------- | ------------------------------------- |
| 65299   | Lafi Bedmountain's Upgraded Telescope |
| 59321   | Ebenruth's Nol                        |
| 16019   | Archaeologist's Map                   |
| 16016   | Lafi Bedmountain's Upgraded Compass   |
| 12034   | Rich Merchant's Ring                  |

## Notes

- The file is 24 bytes, byte for byte the same on clients 2519, 3002, 3251
  and 3474. Client 1784 has no such file, and a private server's
  `DataSheets.bexcel` on client 1784 has no sheet or column by that name.
- The entries run in falling item ID order on every client checked.
- The Lua reaches the filter only when `_ContentsGroup_ProjectAbyssOne` is
  on or the client is a console build (`isGameServiceTypeConsole()`); on the
  PC client `checkOpenWithInventoryWhenOtherTown` returns before it.
- `movableOtherTown()` is a method of the item instance, not of its static
  status, and the same filter also greys out duel copies, guild stock, trade
  goods and barter items through other checks.
- The parser is `_bss/othertownnotmovableitem/parser.py`; its test asserts
  that every entry names an item.
- Two other Lua paths in `panel_window_warehouse_all_1.luac` move items to
  or from another town's storage through `ToClient_ablePushOrPopOtherWareHouse`
  and run on the PC client: the auto-move button for an NPC, installation or
  maid storage (`_ContentsGroup_ItemMove`), and the market-register and
  cargo-sell buttons for an NPC storage (`_ContentsGroup_SellItemInOtherWarehouse`).
  Neither calls `movableOtherTown()`. They are the paths the In-Game Check
  below tests.

## Open Questions

### Other Inputs to `movableOtherTown()`

The Lua shows only the result of `movableOtherTown()`. Whether the client
decides it from this list alone, or also from instance state such as bound or
expiring items, needs the executable of client 2519 or later. The 2016
client, the client 1485 client and server and the client 1784 server have no
other-town storage code, and their names hold no `OtherTown` string.

## In-Game Checks

### Use on the PC Client

Needs item (any one):

- [Archaeologist's Map](https://bdocodex.com/us/item/16019/)
- [Rich Merchant's Ring](https://bdocodex.com/us/item/12034/)

The Lua filter runs only on console builds and under
`_ContentsGroup_ProjectAbyssOne`. This check tests whether the PC client or
the server also blocks the listed items between towns.

1. Put the item in the storage of the town you stand in.
2. Open Transport at the storage keeper and try to send the item to another
   town's storage.
3. If Transport lists it, also try a maid's storage in another town.

The message "Cannot move to another town's storage." or a greyed-out item
means the list is checked on PC too. If the item moves, the list only applies
where the Lua filter runs.
