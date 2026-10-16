# `fieldboss.dbss` Format

## Purpose

A list of character IDs, one per row, under the name "field boss". On client
3464 the 694 rows are world bosses (Garmoth, Karanda, Vell), field, node and
guild boss variants, event bosses, Atoraxion and Hadum bosses, and a few
characters that are not bosses by name: the GM war summons (`8996` Shadow
Knight, `8997` Ogre, `8998` Muraka) and `59670` Military Supply Wagon. Every
ID exists in `characterstatic.dbss`. Besides the ID, a row holds only two
bytes that are `1` on every row.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes  | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ------ | ------------- | --------- |
| 1      | 3473 and later | 3473    | `fieldboss.dbss`       | 22,906 | 694 Row       | 33        |
| 1      | 3473 and later | 3473    | `fieldbossoffset.dbss` | 6,944  | 694 Index Row | 10        |

| Layout | File                   | Known            | Unknown          |
| ------ | ---------------------- | ---------------- | ---------------- |
| 1      | `fieldboss.dbss`       | 2,780 B (12.1%)  | 20,126 B (87.9%) |
| 1      | `fieldbossoffset.dbss` | 6,944 B (100.0%) | 0 B (0.0%)       |

<!-- versions:end -->

## Companion Files

None. The handler reads the rows in file order and does not need
`fieldbossoffset.dbss` (see below). Names and titles come from LOC type 6
(`_common/character.py`).

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then 33-byte rows; the
file ends after the last row.

| Offset  | Type           | Field     | Notes                    |
| ------- | -------------- | --------- | ------------------------ |
| `+0x00` | u32            | row_count | `694` on client 3464     |
| `+0x04` | Row[row_count] | rows      | See Row                  |

### Row (33 bytes)

| Offset  | Type      | Field        | Notes                                              |
| ------- | --------- | ------------ | -------------------------------------------------- |
| `+0x00` | u16       | key          | Row key; equals `character_id` on every row        |
| `+0x02` | u8        | unknown_02   | `1` on every row                                   |
| `+0x03` | u16       | character_id | `characterstatic.dbss` character ID, LOC type 6    |
| `+0x05` | bytes[12] | unknown_05   | Zero on every row                                  |
| `+0x11` | u8        | unknown_11   | `1` on every row                                   |
| `+0x12` | bytes[15] | unknown_12   | Zero on every row                                  |

The `u8, u16 character_id, u16` head has the shape of the block after the
scripts in a `characterstatic.dbss` record (`unknown_p`, `character_id`,
`unknown_p3`), but the values differ: none of the 694 characters has
`unknown_p` set to `1` there.

### `fieldbossoffset.dbss`

A u32 row count (equal to the main file's), then 10-byte rows
(`parse_bare_offset_rows()`).

| Offset  | Type                 | Field     | Notes                              |
| ------- | -------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                      |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first one points at main row 0, the second
at main row 596).

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                                      |
| ------- | ---- | ------------ | ---------------------------------------------------------- |
| `+0x00` | u16  | character_id | Row key, the main row's `key`                              |
| `+0x02` | u32  | offset       | Start of the row in `fieldboss.dbss` plus 2, at `unknown_02` |
| `+0x06` | u32  | size         | Always `31`, the row size minus the 2-byte `key`           |

## Notes

- The client Lua never names this file. Its only field boss reference is the
  chat notice type `CppEnums.EChatNoticeType.FieldBoss = 13`
  (`global_define_cpp_enum`), which `noticealert` turns into a
  `__eNakMessage_FieldBoss` message.
- The list is not what the Boss Info window shows. That window
  (`panel_worldmap_bosslist_all`) reads each boss through
  `ToClient_getBossStaticStatus(index)` (character key, textures, position,
  next spawn time, reward items), which matches the records of
  [`bossinfostaicstatusmanager.bss`](bossinfostaicstatusmanager_bss.md), not
  this file. The five bosses of its
  Field tab (23069 Dastard Bheg, 23061 Red Nose, 23056 Dim Tree Spirit,
  23055 Giant Mudster, 23144 Katzvariak) are all on this list, but so are
  689 other characters, and 23809 Mirumok Destroyer Offin from the Boss
  Info file is not.
- The list is not every boss: `characterstatic.dbss` has 1,877 characters
  with `boss` in the model path on client 3464, and 319 of them are here.
  375 of the 694 rows have no `boss` in the model path, among them event
  monsters such as `29862` Mischievous Jack.

## Open Questions

### What the List Selects

The client code that reads the file is not in Lua, so it is not known what
being on the list does: a boss HP bar, the field boss chat notice, loot or
contribution rules, or something else. The GM summons and the Military Supply
Wagon rule out "named world and field bosses" as the whole answer, and the
Boss Info window's Field tab comes from another file (see Notes).

### unknown_02 and unknown_11

Both bytes are `1` on every row, so the data cannot tell flags from
constants. A future client with a `0` in either would show which.
