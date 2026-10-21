# `supplyservantquestlist.bss` Format

## Purpose

Quest list with no entries: the `count` is `0` on client 3474 and on client 1784, and the file is the 20 bytes of an empty list. The file name points to the stable's supply-for-quest entry of the client Lua (see [Client Use](#client-use)); which quests the list would hold is not known.

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` would be `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, here `8`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | -------------- | --------- |
| 1      | 1485 and later | 3474    | `supplyservantquestlist.bss` | 20    | 1 String Table | 4         |

| Layout | File                         | Known         | Unknown    |
| ------ | ---------------------------- | ------------- | ---------- |
| 1      | `supplyservantquestlist.bss` | 20 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

The same as [`allquestlist.bss`](allquestlist_bss.md).

All multi-byte values are little-endian.

## Client Use

`panel_dialog_servantlist_all_1.luac` and `panel_dialog_servantlist_all_2.luac` (client 3474, also in client 1784) have a stable submenu entry `_SUPPLYFORQUEST` next to the Imperial delivery entry `_SUPPLYHORSE`:

- The submenu adds `_SUPPLYFORQUEST` when `servantInfo:isSuppliableForQuest()` is true and the servant is not rented, not a PC room servant and not in stallion training. The check sits outside the vehicle type test, so it applies to every servant type.
- `HandleEventLUp_ServantList_All_SupplyForQueset()` sends `ToClient_RequestSupplyServant(servantNo)`. The Imperial delivery entry (`HandleEventLUp_ServantList_All_SupplyServant()`) calls `stable_changeToReward(servantNo, CppEnums.ServantToRewardType.Type_Money)` instead.
- The entry's label is the resource string `PANEL_WINDOW_STABLEFUNCTION_LOOKCHANGE`, the same key as the change-look entry `_CHANGELOOK`.

No Lua names this file or reads a quest list for the entry; `isSuppliableForQuest()` is a client function.

## Notes

- Bytes on client 3474 and client 1784: `PABR`, `count` `0`, then the 12-byte trailer `0`, `8`, `0` (`string_count`, `end_of_entries`, `zero`).
- The `binary/` folder of a private server on client 1784 holds the same 20 bytes. Its `DataSheets.bexcel` has no column or cell naming a supply quest (`Quest_Table` has `DoGuide`, the source of [`doguildquestlist.bss`](doguildquestlist_bss.md), but no supply column), and the 2016 client PDB has no symbol for it.
- `test_supply_servant_quest_list.py` checks the declared count and that any entry is a quest of `allquestlist.bss`.

## Open Questions

### What Fills the List

The list is empty on clients 1784 and 3474, so no entry shows which quests it holds. A guess from the Lua: the quests whose objective is to hand over a servant through the stable's supply-for-quest entry, with `isSuppliableForQuest()` true while such a quest is in progress. No source sheet or Lua confirms the link.
