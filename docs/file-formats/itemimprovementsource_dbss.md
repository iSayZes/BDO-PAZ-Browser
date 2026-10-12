# `itemimprovementsource.dbss` Format

## Purpose

The reform stones of Gear Reform, see
[`itemimprovement.dbss`](itemimprovement_dbss.md). A record is a stone item
with a stone category and a reform group; the gear records of the same group
are what the stone reforms.

```text
stone 820974 Cup of Destined Dawn  category 3  group 13  shown by default
stone 9793   Heart of Kutum        category 1  group 33  shown by default
```

## Companion Files

| File                             | Required | Role                                                     |
| -------------------------------- | -------- | -------------------------------------------------------- |
| `itemimprovementsourceoffset.dbss` | Optional | `item_id -> (data_offset, data_size)` index, see below; the handler walks the records without it |

Item names come from LOC type 0 and icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## File Layout

| Offset  | Type     | Field   | Notes                                                |
| ------- | -------- | ------- | ---------------------------------------------------- |
| `+0x00` | u32      | count   | Number of records; `101` on client 3464              |
| `+0x04` | record[] | records | `count` records, back to back to the end of the file |

## Record Structure

### Record (`22 + 4 * value_count` bytes)

| Offset       | Type   | Field              | Notes                                                    |
| ------------ | ------ | ------------------ | -------------------------------------------------------- |
| `+0x00`      | u32    | item_id            | The stone; the index's `data_offset` points past it      |
| `+0x04`      | u64    | value_count        | `5` in every record                                      |
| `+0x0C`      | u32[n] | unknown_0c         | `1,000,000` in every slot of every record (client 3464)  |
| `+0x0C + 4n` | u32    | category           | Gear the stone takes, see below                          |
| `+0x10 + 4n` | u32    | group              | Reform group, `1` to `48`; matches `group` of the gear records |
| `+0x14 + 4n` | u16    | is_default_display | `1` for the 24 stones of [`itemimprovementdefaultdisplaylist.bss`](itemimprovementdefaultdisplaylist_bss.md), else `0` |

Each `(category, group)` pair belongs to one stone (101 pairs, client 3464).

| category | Stones (client 3464)                                                             |
| -------- | -------------------------------------------------------------------------------- |
| `1`      | Weapon stones: Heart of Kutum, Resplendent Boss Weapon Reform Stone I to V, `[Season] Tuvala Main Weapon Conversion Stone` |
| `2`      | Armor stones: Resplendent Boss Armor Reform Stone I to V, `Combatant's Stone (Armor)`, `[Season] Tuvala Helmet Conversion Stone` |
| `3`      | Accessory stones: Cup of Destined Dawn and the other Cups, `[Season] Tuvala Necklace Conversion Stone` |
| `4`      | Blessed Soul Fragment, Exalted Soul Fragment, Crimson Behelit Alchemy Stone Appearance |
| `5`      | Flawless Herald's Crystal                                                        |

## `itemimprovementsourceoffset.dbss`

| Offset  | Type  | Field | Notes                                            |
| ------- | ----- | ----- | ------------------------------------------------ |
| `+0x00` | u32   | count | Equals the `itemimprovementsource.dbss` count    |
| `+0x04` | row[] | rows  | `count` 12-byte rows; no magic, no trailer       |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | item_id     | Record key                              |
| `+0x04` | u32  | data_offset | Record start + 4, past `item_id`        |
| `+0x08` | u32  | data_size   | Record size - 4: `38`                   |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`; on client
3464 every row matches the record walked from the start of the file.

## Suggested UI Layout

| Column          | Type | Notes                                              |
| --------------- | ---- | -------------------------------------------------- |
| Item ID         | num  | `item_id`                                          |
| Icon            | icon | Item icon                                          |
| Stone           | text | LOC type 0 name in its grade colour, else the ID   |
| Category        | num  | `category`                                         |
| Group           | num  | `group`                                            |
| Default Display | flag | `is_default_display`                               |

## Notes

- `category` follows from the stone names; the gear side of the match is an
  open question in [`itemimprovement.dbss`](itemimprovement_dbss.md#which-stone-a-record-takes).
- 28 groups (`17` to `32`, `36`, `38` to `48`) have stones but no gear record
  on client 3464.
- `is_default_display` and the default display list hold the same 24 stones;
  the Reform window loads the list through
  `ToClient_GetImprovementSourceItemCount()` and
  `ToClient_GetDefaultDisplayImprovementSourceItemByIndex(index)`
  (`panel_improvement_all_1`).

## Open Questions

### `unknown_0c`

Five u32 values of `1,000,000` in every record. A million is the scale of
rates elsewhere (`buff.dbss` `apply_rate`), and the window text says a
higher-grade stone gives a higher chance of higher-grade gear, but no record
holds a value other than 100%.
