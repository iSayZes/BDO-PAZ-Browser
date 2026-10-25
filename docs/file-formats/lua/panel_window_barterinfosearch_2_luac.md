# `panel_window_barterinfosearch_2.luac`

## Purpose

The Great Ocean barter search window: the barter list per island, the
exchange cost of each barter, the daily barter list reset and its cooldown.
Its `source` is `window\exchange\panel_window_barterinfosearch_2.lua`. The
bytes follow [`luascript_luac.md`](luascript_luac.md); on client 3483 the
script is 51,932 bytes.

## Calls Into Client Data

| Call                                               | What the script does with it                                                                 | Format doc field                                                              | Client |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------ |
| `ToClient_getMaxChangeSeedCountForDay()`           | Daily limit of barter list resets: the reset button reads remaining / limit, and a reset at the limit fails with `eErrNoBarterSeedChangeCountIsFull` | [`greatseaoption.bss`](../bss/greatseaoption_bss.md) `max_reset_count`?       | 3483   |
| `ToClient_getChangeSeedCountForDay()`              | Resets used today, subtracted from the limit                                                 |                                                                               | 3483   |
| `ToClient_isEnableChangeBarterSeed()`              | Greys out the reset button while it returns false                                            |                                                                               | 3483   |
| `ToClient_changeBarterInfoRemainSec()`             | Seconds until the list renews, shown in the reset button's tooltip                           | [`greatseaoption.bss`](../bss/greatseaoption_bss.md) `reset_cool_time`?       | 3483   |
| `ToClient_needExchangeCount(RegionKey(regionKey))` | Ticket cost of a barter on the island of `regionKey`                                         |                                                                               | 3483   |
| `barterWrapper:getExchangeCountForTime()`          | Base exchange cost shown in the cost tooltip                                                 |                                                                               | 3483   |
| `ToClient_discountPointByBarterLevel()`            | Barter level discount, divided by `CppDefine.e1Percent` (`10000`) and shown as a percentage  | [`greatseaoption.bss`](../bss/greatseaoption_bss.md) `discount_rate`?         | 3483   |
| `ToClient_discountPointByPremiumPackage()`         | Premium package discount, same scale                                                         |                                                                               | 3483   |
| `ToClient_discountPointByViceCaptain()`            | Vice captain discount, same scale, shown while `_ContentsGroup_EmployeePresetJob` is set     |                                                                               | 3483   |

## Enums Used

`CppEnums.ItemWhereType.eWarehouse` and `eServantInventory` pick the
inventory when the window moves barter goods between the warehouse and the
ship.

## Versions

Client 1256 ships the script without any of the reset or discount calls.
Client 1267 adds `ToClient_getMaxChangeSeedCountForDay`,
`ToClient_needExchangeCount` and `ToClient_discountPointByBarterLevel`, on
the same client where `greatseaoption.bss` gains `max_reset_count`,
`discount_rate` and `add_reset_count` (its Layout 2).

## Open Questions

### Which `greatseaoption.bss` Fields the Getters Return

The three `?` links rest on the client the getters and the fields arrive
together, and on the scale: `discount_rate` is `100000` on client 3482, which
reads as 10% through `CppDefine.e1Percent`. No getter has been compared with
the field's value yet, and `add_reset_count` has no getter in this script.
