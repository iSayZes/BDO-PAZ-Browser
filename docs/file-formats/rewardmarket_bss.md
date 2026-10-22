# `rewardmarket.bss` Format

## Purpose

The pet exchange: per trade the pet it takes and the items it gives for
it. On client 3482 every trade takes one pet and gives a Choose Your Tier 3
Exchange Gift Box (`1000130`) for a tier 3 pet, or a Choose Your Tier 4
Exchange Gift Box (`1000131`) and an `[Event] Pet Exchange Token`
(`1000692`) for a tier 4 pet. The exchange window Lua
(`panel_window_rewardmarket_all_1.luac`) reads a trade through
`ToClient_GetRewardMarketStaticStatusByKey(tradeKey)` and its rewards
through `ToClient_GetRewardMarketRewardItemKey(tradeKey, index)` and
`ToClient_GetRewardMarketRewardItemCount(tradeKey, index)`; its tabs are
`__eRewardMarketTradeType_PetToItem` and `_ItemToItem`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records               | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | --------------------- | --------- |
| 1      | 3002 and later | 3482    | `rewardmarket.bss` | 33,122 | 1,264 Reward, 854 Row | 12        |

| Layout | File               | Known            | Unknown         |
| ------ | ------------------ | ---------------- | --------------- |
| 1      | `rewardmarket.bss` | 23,728 B (71.6%) | 9,394 B (28.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | No file  |
| 2637   | No file  |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names the pet from LOC type 6 and links it to its
[`pet.dbss`](pet_dbss.md) row; the reward items take their names and icons
from the item lookup indexes.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                       |
| ------------------- | -------------- | ------------ | ------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                |
| `+0x04`             | u32            | row_count    | Number of trades, `854` on client 3482      |
| `+0x08`             | Row[row_count] | rows         | See Row                                     |
| `rows+0x00`         | String Table   | string_table | See String Table                            |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                  |

### Row (variable: 21 bytes + rewards)

| Offset  | Type                 | Field        | Notes                                                                       |
| ------- | -------------------- | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u16                  | trade_key    | Row key, the Lua `tradeKeyRaw`; unique, `1` to `866` on client 3482          |
| `+0x02` | u32                  | pet_key      | The pet traded in: a [`pet.dbss`](pet_dbss.md) pet ID (854 of 854 on client 3482), named by LOC type 6 |
| `+0x06` | bytes[11]            | unknown_06   | `0` on every row of client 3482                                             |
| `+0x11` | u32                  | reward_count | Number of `rewards`, `1` or `2` on client 3482                              |
| `+0x15` | Reward[reward_count] | rewards      | See Reward                                                                  |

### Reward (12 bytes)

| Offset  | Type | Field      | Notes                                       |
| ------- | ---- | ---------- | ------------------------------------------- |
| `+0x00` | u32  | item_key   | Item given (`ItemEnchantKey`, level 0 here) |
| `+0x04` | u64  | item_count | Count, `1` on every reward of client 3482   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes             |
| ------- | ------------------ | ------------ | ----------------- |
| `+0x00` | u32                | string_count | `0` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | None              |

## Notes

- The tier 3 box goes with the pets whose `pet.dbss` `tier` is `2` (444
  trades), the tier 4 box and token with `tier` `3` (410 trades), on
  client 3482.
- Client 1784 has no `rewardmarket.bss`, and a private server's
  `DataSheets.bexcel` on client 1784 has no reward market sheet, so the
  field names come from the Lua.

## Open Questions

### What the Eleven Zero Bytes Hold

`unknown_06` is `0` on all 854 rows of client 3482, where every trade is
`PetToItem`. An item to item trade would need a material item key and
count, and a trade type byte would tell the two tabs apart; the eleven
bytes would hold those if an `ItemToItem` trade ever ships.
