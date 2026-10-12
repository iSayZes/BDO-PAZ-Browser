# `itemtrade.dbss` Format

## Purpose

The character keys of the NPCs that buy trade goods: trade managers, node
managers with a trade counter and a few quest-area traders. A row is the u16
character key and nothing else.

```text
40010  Bahar               <Trade Manager>
40026  Severo Loggia       <Node Management>
47747  Isobelle Encarotia  <Acher Trade Manager>
```

## Companion Files

None. The handler reads the keys in file order and does not need
`itemtradeoffset.dbss` (see below). Names and titles come from LOC type `6`
(`str_id4` `0` and `1`, `_common/character.py`).

All multi-byte values are little-endian.

## File Layout

A bare table: no `PABR` magic and no string table. The file is exactly
`4 + 2 * count` bytes.

| Offset  | Type  | Field | Notes                                        |
| ------- | ----- | ----- | -------------------------------------------- |
| `+0x00` | u32   | count | Number of keys; `126` on client 3464         |
| `+0x04` | u16[] | keys  | `count` character keys, unique, not sorted   |

### Row (2 bytes)

| Offset  | Type | Field        | Notes                                      |
| ------- | ---- | ------------ | ------------------------------------------ |
| `+0x00` | u16  | character_id | Character key, LOC type `6`                |

## `itemtradeoffset.dbss`

The bare u16 index layout of `petexpoffset.dbss`, read by
`parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type  | Field | Notes                                 |
| ------- | ----- | ----- | ------------------------------------- |
| `+0x00` | u32   | count | Equals the `itemtrade.dbss` count     |
| `+0x04` | row[] | rows  | `count` 10-byte rows, no trailer      |

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u16  | character_id | Row key                                                  |
| `+0x02` | u32  | offset       | Start of the key in `itemtrade.dbss` (`4 + 2 * row`)     |
| `+0x06` | u32  | size         | Always `2`, the key itself                               |

The index rows are in neither key nor file order; each points at its own key
in `itemtrade.dbss` (`test_every_offset_row_points_at_its_key`).

## Suggested UI Layout

| Column       | Type | Notes                                          |
| ------------ | ---- | ---------------------------------------------- |
| Character ID | num  | `character_id`                                 |
| Name         | text | LOC type `6`, `str_id4` `0`                    |
| Title        | text | LOC type `6`, `str_id4` `1`; `-` when it has none |

The offset table shows Character ID, Data Offset and Size.

## Notes

- Titles on client 3464: 57 `<Trade Manager>`, 54 `<Node Management>`, 2
  `<Farm Owner>`, 12 single titles such as `<Acher Trade Manager>`,
  `<Katan Military - Trade Manager>` and `<Trader of Shakatu>`, and one key
  without a title (40075 Fish Dad).
- On client 3464 the file holds every character whose
  `characterfunction.dbss` buttons include Trade (122 keys), plus four more:
  47546 Taeseok, 47563 Gyeonghwan and 47600 Chunsu (`<Trade Manager>`, whose
  LOC type `32` button reads `Trading`) and 40075 Fish Dad.
- `itemtradegrouptonpc.dbss` and its offset table hold the same 126 keys on
  client 3464, in a different order.
- No NPC has a character icon in the `CHARACTER_ICON` index, so the table has
  no icon column.
- 40075 Fish Dad has no `characterfunction.dbss` record, no `npcsimply.bss`
  record and no title; `characterstatic.dbss` gives it only the action script
  `getknowledge(19);`. In game it reads as a removed or unused NPC, but in
  `itemtradegrouptonpc.dbss` its key holds 1,501 trade items on client 3464,
  where every other key holds one. I read 40075 as the holder of the default
  trade list; whether every trade NPC uses that list is open in the
  `itemtradegrouptonpc.dbss` doc.
