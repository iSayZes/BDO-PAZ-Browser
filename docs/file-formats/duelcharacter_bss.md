# `duelcharacter.bss` Format

## Purpose

The options of Tag Characters (duel characters in the client code), one
58-byte record with no header: the quest that opens the item copy of
Marni's Suspicious Device, the fuel item the copy uses and the fuel item
the single copy uses, then eleven values not tied to a meaning yet. On
client 3482 the quest is Black Spirit's Gift (Marni's Suspicious Device)
(chain `21418`, quest `5`), the items Marni's Unstable Fuel (`45026`) and
Marni's Processed Fuel (`320157`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 3474 and later | 3482    | `duelcharacter.bss` | 58    | -       | -         |

| Layout | File                | Known        | Unknown      |
| ------ | ------------------- | ------------ | ------------ |
| 1      | `duelcharacter.bss` | 12 B (20.7%) | 46 B (79.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | No file  |
| 3002   | No file  |
| 2765   | No file  |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Quest title (LOC type 18) and item names (type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type | Field                         | Notes                                                                                   |
| ------- | ---- | ----------------------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_copy_quest               | Packed quest ID: low u16 quest chain, high u16 quest (`349098` = chain 21418, quest 5) |
| `+0x04` | u32  | need_item_for_copy            | Item key of the item copy fuel (`45026`, enhancement level 0)                          |
| `+0x08` | u32  | need_item_for_individual_copy | Item key of the single copy fuel (`320157`)                                            |
| `+0x0C` | u32  | unknown_0c                    | `1500` (client 3482); see Open Questions                                                |
| `+0x10` | u32  | unknown_10                    | `100000000` (client 3482); see Open Questions                                           |
| `+0x14` | u32  | unknown_14                    | `0` (client 3482)                                                                       |
| `+0x18` | u32  | unknown_18                    | `0` (client 3482)                                                                       |
| `+0x1C` | u32  | unknown_1c                    | `0` (client 3482)                                                                       |
| `+0x20` | u32  | unknown_20                    | `2000` (client 3482)                                                                    |
| `+0x24` | u32  | unknown_24                    | `0` (client 3482)                                                                       |
| `+0x28` | u32  | unknown_28                    | `1` (client 3482)                                                                       |
| `+0x2C` | u32  | unknown_2c                    | `1` (client 3482)                                                                       |
| `+0x30` | u32  | unknown_30                    | `0` (client 3482)                                                                       |
| `+0x34` | u32  | unknown_34                    | `2` (client 3482)                                                                       |
| `+0x38` | u16  | unknown_38                    | `5396` (`0x1514`, client 3482)                                                          |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
the table, and client 1784 ships no `duelcharacter.bss`. The three names
follow the client Lua (3482) that reads them and the records they point at:

| Field                         | Lua call                                         | Evidence (client 3482)                                                                 |
| ----------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------- |
| item_copy_quest               | `ToClient_isClearedDuelCharacterItemCopyQuest()` | The quest's text says the player can now use Marni's Suspicious Device in the Tag Character menu |
| need_item_for_copy            | `ToClient_getNeedItemForDuelCopy()`              | Marni's Unstable Fuel, "Used to copy gear so that 2 tagged characters can use it at the same time" |
| need_item_for_individual_copy | `ToClient_getNeedItemForIndividuelCopy()`        | Marni's Processed Fuel, used "to use the Single Copy function"                          |

`panel_window_equip_charactertag_itemcopy_all_1.luac` passes both item
keys to `getItemEnchantStaticStatus()`.

## Notes

- The server dump of client 1784 names `DuelCharacterExpValue` with
  `_mainCharacterExpRate`, `_subCharacterExpRate` and
  `_mainCharacterSkillExpRate` under `LocalizingOption`, not under this
  table.

## Open Questions

### What the Eleven Values Hold

`unknown_0c` (`1500`), `unknown_10` (`100000000`), `unknown_20` (`2000`),
`unknown_28` and `unknown_2c` (`1`), `unknown_34` (`2`) and `unknown_38`
(`5396`) have no Lua getter that returns them as is. The item copy window
reads two fuel counts, `ToClient_getCopyItemForDuelNeedItemCount()` and
`ToClient_getAddCopyItemForDuelNeedItemCount()`; they are leads for
`unknown_0c` and one more field, but no data ties a count to an offset.
