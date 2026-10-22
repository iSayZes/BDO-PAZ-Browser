# `innstaticstatus.dbss` Format

## Purpose

The inns and their rooms: one row per inn with a list of room characters.
On clients 1784 and 3482 the file holds one inn, key `1`, whose rooms are
every house character of [`householdlist.bss`](householdlist_bss.md) in
another order: 865 on client 3482, 801 on client 1784. Companion
`innstaticstatusoffset.dbss` lists where the row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ------------ | --------- |
| 1      | 1348 and later | 3482    | `innstaticstatus.dbss`       | 1,740 | 1 Row        | 1,736     |
| 1      | 1348 and later | 3482    | `innstaticstatusoffset.dbss` | 14    | 1 Offset Row | 10        |

| Layout | File                         | Known            | Unknown    |
| ------ | ---------------------------- | ---------------- | ---------- |
| 1      | `innstaticstatus.dbss`       | 1,740 B (100.0%) | 0 B (0.0%) |
| 1      | `innstaticstatusoffset.dbss` | 14 B (100.0%)    | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                          |
| ---------------------------- | -------- | ----------------------------------------------------------------------------- |
| `innstaticstatusoffset.dbss` | Optional | `inn_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `houseinfo.bss`              | Optional | The node house rows, for the House link and the Town column                    |
| `guildhouseinfo.dbss`        | Optional | The guild house rows, for the House link and the Town column                   |
| `languagedata_en.loc`        | Optional | House names (type 6) and town names (type 17)                                  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                  |
| ------- | ---------- | ----- | -------------------------------------- |
| `+0x00` | u32        | count | Number of inns; `1` on clients 1784 and 3482 |
| `+0x04` | Row[count] | rows  | See Row                                |

On client 3482 the file is 4 + 2 + 4 + 865 x 2 = 1,740 bytes.

### Row (variable: 6 bytes + room keys)

| Offset  | Type            | Field      | Notes                                                                    |
| ------- | --------------- | ---------- | ------------------------------------------------------------------------ |
| `+0x00` | u16             | inn_key    | Row key; `1`                                                              |
| `+0x02` | u32             | room_count | Number of `room_keys`                                                     |
| `+0x06` | u16[room_count] | room_keys  | House characters, `characterstatic.dbss` keys; each key once             |

### `innstaticstatusoffset.dbss`

Bare offset table into `innstaticstatus.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `innstaticstatus.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                          |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u16  | inn_key     | Key of the row it points at                              |
| `+0x02` | u32  | data_offset | Row start + 2, at `room_count`                           |
| `+0x06` | u32  | data_size   | The row less its key: `4 + 2 * room_count` (1,734 on client 3482) |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`.

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 is named
after the file. The 2016 `gc::InnStaticStatus` holds one member,
`_innRoomList`, a list of `CharacterStaticStatus` pointers, and
`gc::InnStaticStatusManager` keys the inns by a u16; so the list is
`room_keys` and the key `inn_key`. Every key of the list resolves to a
house name (LOC type 6).

## Notes

- On client 3482 the 865 rooms are the 823 node houses of
  [`houseinfo.bss`](houseinfo_bss.md), the 23 guild houses of
  [`guildhouseinfo.dbss`](guildhouseinfo_dbss.md), Grána (`3520`) and
  O'draxxia (`3806`) Guild Houses and the 17 villas `3371` to `3387`
  (Kunid's Villa to Oberin's Villa).
- The list opens with `3121` (Valencia 15-1, 1F) and the Calpheon slum
  houses `2410`, `2415`, `2420`. [`householdlist.bss`](householdlist_bss.md)
  holds the same keys in another order.
- The house Lua asks `isInnRoom()` of a house's object static status
  (`panel_housing.luac`, `panel_window_installationmode_house_renew.luac`
  and 12 more), next to `isFixedHouse()` and `isMansionLand()`. The server
  dump of client 1784 has the transactions `TrRentInnRoomReq`
  and `TrUpdateExpiredInnRoomReq`. The view shows one row per room, with
  a link to the room's `houseinfo.bss` or `guildhouseinfo.dbss` row.

## Open Questions

### What Makes a House an Inn Room

`isInnRoom()` reads as a flag that sets a house apart, yet the one inn
lists every house character. Whether `isInnRoom()` reads this list, and
what a rentable inn room is in game, is open.
