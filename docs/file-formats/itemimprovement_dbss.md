# `itemimprovement.dbss` Format

## Purpose

Gear Reform (`LUA_IMPROVEMENT_TITLE` "Reform"): the Black Spirit window where
a piece of gear and a reform stone turn into the next grade of that gear. A
record names the result and the gear it is made from, and a reform group that
ties it to the stones of
[`itemimprovementsource.dbss`](itemimprovementsource_dbss.md).

```text
key 4233  group 13
  result 11698 Dawnbound Kharazad Necklace
  input  11697 Kharazad Necklace
  stone  820974 Cup of Destined Dawn (category 3, group 13)
```

## Companion Files

| File                              | Required | Role                                                     |
| --------------------------------- | -------- | -------------------------------------------------------- |
| `itemimprovementoffset.dbss`      | Optional | `key -> (data_offset, data_size)` index, see below; the handler walks the records without it |
| `itemimprovementsource.dbss`      | Optional | The reform stones, see [`itemimprovementsource.dbss`](itemimprovementsource_dbss.md) |

Item names come from LOC type 0 and icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## File Layout

| Offset  | Type     | Field   | Notes                                                       |
| ------- | -------- | ------- | ----------------------------------------------------------- |
| `+0x00` | u32      | count   | Number of records; `3,904` on client 3464                   |
| `+0x04` | record[] | records | `count` records, back to back to the end of the file        |

## Record Structure

### Record (`25 + 4 * item_count` bytes)

| Offset           | Type          | Field       | Notes                                                    |
| ---------------- | ------------- | ----------- | -------------------------------------------------------- |
| `+0x00`          | u32           | key         | Record key, `1` to `4,949` with gaps; the index's `data_offset` points past it |
| `+0x04`          | u64           | item_count  | `5` or `1`                                               |
| `+0x0C`          | u32[n]        | item_ids    | `item_count` item IDs, see below                         |
| `+0x0C + 4n`     | u8            | unknown_tail_0 | `0` in every record                                   |
| `+0x0D + 4n`     | u8            | group       | Reform group, `1` to `37`; matches `group` of the stones |
| `+0x0E + 4n`     | u8[11]        | unknown_tail_2 | All `0` in every record                               |

With 5 items, `item_ids[0]` is the result and `item_ids[1]` to `[4]` the input
gear, the same ID four times in all 3,816 such records (client 3464).
Kharazad Necklace (`11697`) to Dawnbound Kharazad Necklace (`11698`) is
stored as `[11698, 11697, 11697, 11697, 11697]`, and Kutum Clavis (`743327`)
to Earthshaking Kutum Clavis (`737423`) as `[737423, 743327 x4]`. The 88
records with 1 item hold 87 Tuvala items, mostly in groups 3, 4 and 5 (Tuvala
Clavis `695190` in groups 4 and 5); see Open Questions.

An item can be the input of several records with different groups and
results; 1,528 items are a result in one record and an input in another.

## `itemimprovementoffset.dbss`

| Offset  | Type  | Field | Notes                                      |
| ------- | ----- | ----- | ------------------------------------------ |
| `+0x00` | u32   | count | Equals the `itemimprovement.dbss` count    |
| `+0x04` | row[] | rows  | `count` 12-byte rows; no magic, no trailer |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | key         | Record key                              |
| `+0x04` | u32  | data_offset | Record start + 4, past `key`            |
| `+0x08` | u32  | data_size   | Record size - 4: `41` or `25`           |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The rows
are not in file order; on client 3464 every row matches the record walked
from the start of the file.

## Notes

- The window is `panel_improvement_all` (`Panel_Window_Improvement_All`). It
  lists gear whose item static status says `isImprovable()`, and stones that
  `getImproveInformation():checkIsValidSubItem(slot)` accepts; both checks run
  in the client, so the Lua does not show how a stone is matched to gear.
- The window text: "You can use Reform Stones to level up gear to the next
  grade. The higher the grade of the Reform stone, the higher the chances of
  acquiring higher grade gear." (`LUA_IMPROVEMENT_DESC_RENEW`).
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  (`internal/tables/itemimprovement.go`) reads the record body as `u32 disc`,
  `u32 0`, result, four bases, a `flag` that is "always N x 256" and 9 zero
  bytes, and drops the 25-byte records. Its `disc` and `0` are the u64
  `item_count` (`5` or `1`, the number of IDs that follow), and its `flag` is
  `group` read as a u32 from one byte early: `0x2100` is group `33`.

## Open Questions

### Which Stone a Record Takes

Several stones share a `group`; they differ in `category` (see
[`itemimprovementsource.dbss`](itemimprovementsource_dbss.md)). Mapping the
input gear's `itemenchant.dbss` `category` byte (`+0x05`) to a stone category,
`1` and `2` (weapons) to `1`, `3` (armor) to `2`, `4` (accessories) to `3` and
`0` (alchemy stones) to `4`, every one of the 3,904 records (client 3464) has
a stone with its group and that category, and the names agree: Behelit's
Heart (`761877`, group 3) meets Crimson Behelit Alchemy Stone Appearance
(category 4, group 3). Whether the client matches by this pair, and what
stone category `5` (Flawless Herald's Crystal) takes, is open.

### Records With One Item

The 88 records with one item ID name Tuvala gear and no result. Groups 3, 4
and 5 are also the groups of the `[Season] Tuvala ... Conversion Stone`
items, so these may be conversions whose result is not one fixed item. What
the client does with them is open.

### The 13-Byte Tail

Only byte `+1` (`group`) is ever non-zero.
