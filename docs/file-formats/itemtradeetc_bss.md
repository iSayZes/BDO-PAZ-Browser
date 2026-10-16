# `itemtradeetc.bss` Format

## Purpose

The desert trade buff per pair of trade group types: for each pair of the
trade goods' group and the buying trade NPC's group, a distance and a buff
rate. The trade sell list shows the `Desert Buff Applied` icon from these two
values. A second table of five 12-byte rows follows, whose use is unknown.

```text
From  To  Distance   Desert Buff Rate
1     2   700,000    1,000,000
2     99  700,000      500,000
```

## Companion Files

None. The trade group type codes are the `trade_group_type` codes of
[`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md).

All multi-byte values are little-endian.

## File Layout

A PABR file with variable-size groups and an empty string table. 184 bytes on
client 3464.

| Offset  | Type    | Field       | Notes                                                  |
| ------- | ------- | ----------- | ------------------------------------------------------ |
| `+0x00` | char[4] | magic       | `PABR`                                                 |
| `+0x04` | u32     | group_count | Number of groups; `4` on client 3464                   |
| `+0x08` | group[] | groups      | `group_count` groups, one per from group               |
| ...     | u32     | row_count   | Number of 12-byte rows; `5` on client 3464             |
| ...     | row[]   | rows        | `row_count` rows                                       |
| ...     | u32     | string_count | `0`: the string table holds no strings                |
| ...     | u32     | table_start | Offset of `string_count`; `0xAC` on client 3464        |
| ...     | u32     | zero        | `0`                                                    |

The last eight bytes are the PABR trailer that `_common/pabr_strings.py`
reads. The rows end where `table_start` points.

## Record Structure

### Group (5 + 10 * `pair_count` bytes)

| Offset  | Type   | Field      | Notes                                  |
| ------- | ------ | ---------- | -------------------------------------- |
| `+0x00` | u8     | from_group | Trade group type of the goods          |
| `+0x01` | u32    | pair_count | Number of pairs                        |
| `+0x05` | pair[] | pairs      | `pair_count` pairs of 10 bytes         |

### Pair (10 bytes)

| Offset  | Type | Field      | Notes                                                        |
| ------- | ---- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8   | from_group | Repeats the group's `from_group`                             |
| `+0x01` | u8   | to_group   | Trade group type of the buying trade NPC                     |
| `+0x02` | f32  | distance   | Distance the goods must travel; `700,000.0` on every pair on client 3464 |
| `+0x06` | u32  | add_rate   | Desert buff rate; `1,000,000` or `500,000` on client 3464    |

The bytes at `+0x02` are `00 E6 2A 49` on every pair, which is exactly
`700000.0` as an f32.

The names `distance` and `add_rate` are our reading. The Lua reads the pair
only through `ToClient_TradeGroupFromToDistance` and
`ToClient_TradeGroupFromToAddPercent`, which name no byte. A pair holds
exactly two values, and the names follow their types: the f32 for the
distance the Lua compares against `getFromToDistanceTradeShop()`, and the
u32 on the 1,000,000 scale the same Lua uses for trade rates. An in-game
check (In-Game Checks) can confirm the rate.

### Row (12 bytes)

| Offset  | Type | Field      | Notes                                  |
| ------- | ---- | ---------- | -------------------------------------- |
| `+0x00` | u64  | unknown_00 | Rises from `0`; upper four bytes `0`   |
| `+0x08` | u32  | unknown_08 | Falls from `1,000,000`                 |

On client 3464 the five rows are (`0`, `1,000,000`), (`4,500,000`,
`750,000`), (`9,000,000`, `500,000`), (`13,500,000`, `250,000`) and
(`18,000,000`, `180,000`). See Open Questions.

## Trade Group Types

The client does not name the codes; no Lua enum or string key covers them.
[Trade Group Types](itemtradegrouptonpc_dbss.md#trade-group-types) in the
`itemtradegrouptonpc.dbss` doc lists the trade NPCs and goods that hold each
one. In short: `2` is the Valencia City trade managers, `3` the Ibellab Oasis
trade manager, `1` the other trade NPCs and the regional trade goods, `99`
the rest of the shared Fish Dad list (relics, fish, crates, trash loot).

LOC text places the NPCs: quest 5053 names "Yis Kunjamin of Capital
Valencia", item 8175 sends the player to "Burita Allon in Valencia City", and
quest 5801 names "Shuriar the trade manager at Ibellab Oasis".

### Pairs on Client 3464

| From | To | Distance | Desert Buff Rate |
| ---- | -- | -------- | ---------------- |
| 1    | 2  | 700,000  | 1,000,000        |
| 1    | 3  | 700,000  | 1,000,000        |
| 2    | 1  | 700,000  | 1,000,000        |
| 3    | 1  | 700,000  | 1,000,000        |
| 2    | 99 | 700,000  | 500,000          |
| 3    | 99 | 700,000  | 500,000          |
| 99   | 2  | 700,000  | 500,000          |
| 99   | 3  | 700,000  | 500,000          |

Every pair links Valencia City or Ibellab Oasis with the rest of the world;
no pair links 2 and 3, and none links 1 and 99. The matrix is symmetric, so
this client's data cannot tell which of the two bytes is the goods' group;
I follow the Lua's argument order (goods first, NPC second) in the names.

## Notes

- `panel_dialog_trade_mybasket_all_1.luac` (the trade sell list) is the only
  client Lua that reads these values. Per item it calls
  `ToClient_TradeGroupFromToAddPercent(tradeItemWrapper:getTradeGroupType(),
  characterStaticStatus:getTradeGroupType())` and
  `ToClient_TradeGroupFromToDistance(...)` with the same two arguments: the
  trade item's group type and the trade NPC's. It shows the `Desert Buff
  Applied` icon (`LUA_TRADEMARKET_DESERTBUFF`) when the player's
  `getSellTradeItemPricePercent()` is above `0`, the add percent is above
  `100` and the item's travel distance (`getFromToDistanceTradeShop()`) is at
  least the pair's distance.
- The file holds two values per pair, one f32 and one u32 in the 1,000,000
  scale the same Lua uses for trade rates (`getlTradeItemCountRate()` is
  `1000000` when no limit applies), so I read the f32 as the distance and the
  u32 as the add percent.
- The client's own text matches the pairs: knowledge 9239 (Token of Desert
  Trading) says validated trade goods trade "exclusively at Valencia City"
  and only for goods carried a long distance through the desert, and a
  dialog line (LOC type 39, 110639) reads "You can sell trade goods from
  other regions for a higher price in Valencia City and Ibellab Oasis.
  However, you must cross the great desert in order to get there." Dialog
  116155 requires Trading Artisan 2 and the quest `To the Wild Desert!` for
  the desert trade buff.
- The third-party project calpheonlabs reads `+0x02` as a zero byte followed
  by a 3-byte marker `E6 2A 49`; the f32 reading covers the same four bytes.

## Open Questions

### What Scale add_rate and distance Use

The Lua compares the add percent with `100`, but the file stores `1,000,000`
and `500,000`, both far above it, so the native getter converts the value.
Elsewhere in the same Lua `_CONST_CALCULATE_PERCENT_VALUE` is `10000`, which
makes `1,000,000` read as 100% and `500,000` as 50%; whether that is the
price added to the sale or something else is open. The unit of the `700,000`
distance against `getFromToDistanceTradeShop()` is open too.

### What the 12-byte Rows Hold

A rising u64 (`0` to `18,000,000` on client 3464) paired with a falling u32
that starts at `1,000,000`. No client Lua reads them. One guess: the Big Hand
rule of `panel_dialog_trade_function_all.xml` (`PANEL_TRADEMARKETBUYLIST_DESC`),
under which a player who buys limited trade goods past a set amount in a day
gets less stock offered; `getlTradeItemCountRate()` is `1000000` until that
happens. The u64 would then be the day's purchase total in silver and the u32
the stock rate. Nothing in the data confirms it.

### Where the NPC's Trade Group Type Comes From

The Lua reads the NPC's code from `characterStaticStatus:getTradeGroupType()`.
In `itemtradegrouptonpc.dbss` the one-item group of each trade NPC carries
the NPC's code (`2` for the Valencia City managers), but whether the client
takes it from there or from a field of `characterstatic.dbss` is open.

## In-Game Checks

### Big Hand Stock Rate

Needs zone: Valencia City or Port Ratt (limited trade goods)

Buy limited trade goods for more than 4,500,000 silver in one day and watch
the stock the trade manager offers. If it drops to three quarters as the
total passes 4,500,000 (and to half past 9,000,000), the 12-byte rows are the
Big Hand table: `unknown_00` the purchase total and `unknown_08` the stock
rate.

### Desert Buff Rate

Needs NPC (any one):

- [Yis Kunjamin](https://bdocodex.com/us/npc/45011/)
- [Burita Allon](https://bdocodex.com/us/npc/45012/)

Needs quest: To the Wild Desert!

With the desert trade buff, sell a Calpheon trade good (group `1`, rate
`1,000,000`) at Valencia City and note the price with and without the
`Desert Buff Applied` icon. A doubled price means `1,000,000` adds 100%; a
50% rise means the rate is applied another way.
