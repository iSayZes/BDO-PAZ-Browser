# `exchangecoin.bss` Format

## Purpose

The coin exchange: per coin item (seals, tokens and medals) its category,
the coin counts of its accumulated use levels and the rewards it buys, each
with its exchange number, coin cost, item and count, exchange type, limit
and the accumulated level it needs. The exchange window Lua
(`panel_exchangecoin_all_1.luac`) walks the coins with
`ToClient_getCountOfCoinList()` and `ToClient_getCoinItemEnchantKeyByIndex(index)`,
reads the category with `ToClient_getCoinInfoCategoryByIndex(index)` and a
reward with `ToClient_getExchangeNo`, `ToClient_getNeedCoinCount`,
`ToClient_getRewardItemWrapperByType`, `ToClient_getLimitCountByExchangeNo`
and `ToClient_getAccumulatedCoinNeedLevel`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records             | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | ------------------- | --------- |
| 3      | 3474 and later | 3482    | `exchangecoin.bss` | 27,980 | 752 Reward, 54 Coin | 35        |
| 2      | 3251           | 3251    | `exchangecoin.bss` | 23,526 | 660 Reward, 49 Coin | 34        |
| 1      | 2519 to 3002   | 3002    | `exchangecoin.bss` | 19,289 | 543 Reward, 39 Coin | 34        |

| Layout | File               | Known            | Unknown         |
| ------ | ------------------ | ---------------- | --------------- |
| 3      | `exchangecoin.bss` | 21,258 B (76.0%) | 6,722 B (24.0%) |
| 2      | `exchangecoin.bss` | 17,605 B (74.8%) | 5,921 B (25.2%) |
| 1      | `exchangecoin.bss` | 14,473 B (75.0%) | 4,816 B (25.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 3 |
| 3474   | Layout 3 |
| 3251   | Layout 2 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
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

None. The handler names the coin and reward items from the item lookup
indexes and LOC type 0.

All multi-byte values are little-endian.

## Layout 3

### File Layout

No `PABR` magic and no string table.

| Offset           | Type                     | Field              | Notes                                                                    |
| ---------------- | ------------------------ | ------------------ | ------------------------------------------------------------------------ |
| `+0x00`          | u32                      | coin_count         | Number of coins, `54` on client 3482                                     |
| `+0x04`          | Coin[coin_count]         | coins              | See Coin                                                                 |
| `coins+0x00`     | u32                      | unknown_order_count | Equals `coin_count` on client 3482                                      |
| `coins+0x04`     | u32[unknown_order_count] | unknown_order_keys | The `coin_item_key` of every coin, in another order than `coins`; see Open Questions |

### Coin (variable: 26 bytes + levels and rewards)

| Offset                            | Type                                | Field                     | Notes                                                                       |
| --------------------------------- | ----------------------------------- | ------------------------- | --------------------------------------------------------------------------- |
| `+0x00`                           | u8                                  | unknown_00                | `1` on four coins of client 3482 (`860216`, `860333`, `860451`, `890085`), else `0` |
| `+0x01`                           | u32                                 | coin_item_key             | The coin item (`ItemEnchantKey`, level 0 here); unique                      |
| `+0x05`                           | u8                                  | info_category             | See Info Categories                                                         |
| `+0x06`                           | i64                                 | unknown_06                | `-1` on every coin of client 3482                                           |
| `+0x0E`                           | u64                                 | accumulated_level_count   | Number of `accumulated_need_counts`; `4` on Agris Gold Coin (`890085`), `0` on the other 53 coins |
| `+0x16`                           | u64[accumulated_level_count]        | accumulated_need_counts   | Coins to have used for each accumulated level, rising (`200`, `1000`, `1800`, `3500`) |
| `accumulated_need_counts+0x00`    | u32                                 | reward_count              | Number of `rewards`                                                         |
| `accumulated_need_counts+0x04`    | Reward[reward_count]                | rewards                   | See Reward                                                                  |

### Reward (35 bytes)

| Offset  | Type | Field                  | Notes                                                                                      |
| ------- | ---- | ---------------------- | ------------------------------------------------------------------------------------------ |
| `+0x00` | u32  | exchange_no            | Exchange number (`ToClient_getExchangeNo`), unique over the file                           |
| `+0x04` | u64  | need_coin_count        | Coins one exchange costs                                                                   |
| `+0x0C` | u32  | item_key               | Item given (`ItemEnchantKey`)                                                              |
| `+0x10` | u64  | item_count             | Count given per exchange                                                                   |
| `+0x18` | u8   | exchange_type          | See Exchange Types                                                                         |
| `+0x19` | u8   | limit_count            | Exchanges allowed per period of `exchange_type` (`ToClient_getLimitCountByExchangeNo`); `0` on 331 of the 339 `Always` rewards of client 3482 |
| `+0x1A` | i64  | unknown_1a             | `-1` on every reward of client 3482                                                        |
| `+0x22` | u8   | accumulated_need_level | Accumulated level the reward needs, `0` to `accumulated_level_count`; `255` for none, the value of every reward of coins without levels |

On client 3482 the 54 coins hold 752 rewards.

## Layout 2

No accumulated levels: a coin has no `accumulated_level_count` and
`accumulated_need_counts`, a reward no `accumulated_need_level`. Only the
Coin and the Reward differ from Layout 3.

### Coin (variable: 18 bytes + rewards)

| Offset  | Type                 | Field         | Notes |
| ------- | -------------------- | ------------- | ----- |
| `+0x00` | u8                   | unknown_00    |       |
| `+0x01` | u32                  | coin_item_key |       |
| `+0x05` | u8                   | info_category |       |
| `+0x06` | i64                  | unknown_06    |       |
| `+0x0E` | u32                  | reward_count  |       |
| `+0x12` | Reward[reward_count] | rewards       |       |

### Reward (34 bytes)

| Offset  | Type | Field           | Notes |
| ------- | ---- | --------------- | ----- |
| `+0x00` | u32  | exchange_no     |       |
| `+0x04` | u64  | need_coin_count |       |
| `+0x0C` | u32  | item_key        |       |
| `+0x10` | u64  | item_count      |       |
| `+0x18` | u8   | exchange_type   |       |
| `+0x19` | u8   | limit_count     |       |
| `+0x1A` | i64  | unknown_1a      |       |

## Layout 1

No `unknown_00` byte before the coin item key; the rest is as in Layout 2.

### Coin (variable: 17 bytes + rewards)

| Offset  | Type                 | Field         | Notes |
| ------- | -------------------- | ------------- | ----- |
| `+0x00` | u32                  | coin_item_key |       |
| `+0x04` | u8                   | info_category |       |
| `+0x05` | i64                  | unknown_06    |       |
| `+0x0D` | u32                  | reward_count  |       |
| `+0x11` | Reward[reward_count] | rewards       |       |

## Info Categories

`ToClient_getCoinInfoCategoryByIndex()` returns a coin's category, which
the Lua compares with `__eExchangeCoinInfoCategory_Season`, `_Event`,
`_Contents`, `_BossReward` and `_Bookmark`; the Lua does not hold their
values. The coins of each value on client 3482 name it:

| Value | Category   | Coins (client 3482)                                                        |
| ----- | ---------- | -------------------------------------------------------------------------- |
| 0     | Season     | The two `[Season]` items (`[Season] Adventure Token`, `[Season] Seal of Journey`) |
| 1     | Event      | 16 coins, 13 of them named `[Event] ...`                                   |
| 2     | Contents   | 29 coins of standing content (`Hunter's Seal`, `Golden Seal - [Imperial Training]`, `Battlefield Token`) |
| 4     | BossReward | The seven `Boss Blitz Token - ...` items                                   |

No coin has `3`; the bookmark tab is the player's own list.

## Exchange Types

`exchange_type` is the `_exchangeTypeEnum` of the exchange window Lua
(`panel_exchangecoin_all.luac`), which passes it to
`ToClient_getCountOfRewardListByType(coin, type)`.

| Value | Lua name | Rewards (client 3482) |
| ----- | -------- | --------------------- |
| 0     | `ALWAYS` | 339                   |
| 1     | `DAY`    | 6                     |
| 2     | `WEEK`   | 65                    |
| 3     | `FAMILY` | 342                   |
| 4     | `LEVEL`  | 0                     |

The rewards of Agris Gold Coin that need an accumulated level are type `3`.

## Notes

- Client 1784 has no `exchangecoin.bss`, and a private server's
  `DataSheets.bexcel` on client 1784 has no coin exchange sheet, so the
  field names come from the Lua.

## Open Questions

### What the Coin Head Fields Hold

`unknown_00` is `1` on Faded Golden Seal, Dreamer's Seal, Strange
Moonlight Seal and Agris Gold Coin and `0` on the other 50 coins of client
3482; `ToClient_isSealedCoin(coin)` is a lead. `unknown_06` is `-1` on every
coin.

### What the Reward's `-1` Holds

`unknown_1a` is `-1` on all 752 rewards of client 3482. A sale end time or
a per-account limit that is off would read this way.

### What the Coin Key List Orders

`unknown_order_keys` lists the same 54 coins as `coins` in another order
(`860451`, `1000845`, `980170`, ...). The window sorts by its bookmark list
first and has a `LINEUP` tab; which of the two lists
`ToClient_getCoinItemEnchantKeyByIndex()` walks is open.
