# `itemimprovementdefaultdisplaylist.bss` Format

## Purpose

The reform stones the Gear Reform window lists by default, in order. Each
entry is a stone item ID of
[`itemimprovementsource.dbss`](itemimprovementsource_dbss.md); the window
loads them through `ToClient_GetImprovementSourceItemCount()` and
`ToClient_GetDefaultDisplayImprovementSourceItemByIndex(index)`
(`panel_improvement_all_1`).

```text
4912 Ultimate Weapon Reform Stone
4913 Ultimate Armor Reform Stone
8141 Cup of Arid Moonlight
```

All multi-byte values are little-endian.

## File Layout

A `PABR` table of u32 rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset  | Type     | Field   | Notes                                                       |
| ------- | -------- | ------- | ----------------------------------------------------------- |
| `+0x00` | u8[4]    | magic   | `PABR`                                                      |
| `+0x04` | u32      | count   | Number of stones; `24` on client 3464                       |
| `+0x08` | u32[]    | item_ids | `count` stone item IDs                                     |
| end     | 12 bytes | trailer | Empty string table: `u32 0`, `u32` end of the rows (`8 + 4 * count`), `u32 0` |

## Notes

- On client 3464 the 24 stones are exactly the `itemimprovementsource.dbss`
  records with `is_default_display = 1`.
