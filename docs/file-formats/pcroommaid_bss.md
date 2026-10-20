# `pcroommaid.bss` Format

## Purpose

The PC room maids and butlers: a u32 count and the u16 character key of
every [`maid.dbss`](maid_dbss.md) row whose `pc_room_type` is set, in
`maid.dbss` row order.
On client 3474 these are the eight keys `18964` to `18967` and `18974` to
`18977`, each a Fairy Chiara or Ethan the Butler with the `[Oasis]` name
prefix (LOC type 6).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------- | --------- |
| 1      | 1230 and later | 3474    | `pcroommaid.bss` | 20    | 8 Row   | 2         |

| Layout | File             | Known         | Unknown    |
| ------ | ---------------- | ------------- | ---------- |
| 1      | `pcroommaid.bss` | 20 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                        |
| ---------------------------- | -------- | ----------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | Which keys have a `characterstatic.dbss` row to link to     |
| `languagedata_*.loc`         | Optional | Character names, LOC type 6, keyed by `character_key`       |

All multi-byte values are little-endian.

## Layout 1

### File Layout

Plain binary: no `PABR` magic, no offset file and no trailer.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 8 x 2 = 20 bytes on client 3474.

### Row (2 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of a `maid.dbss` row and a LOC type 6 character name    |

## PC Room Maids

| character_key | Name (LOC type 6, client 3474) | Duty in the client 1784 `Maid_Table` |
| ------------- | ------------------------------ | ------------------------------------ |
| `18964`       | [Oasis] Fairy Chiara           | Warehouse                            |
| `18965`       | [Oasis] Fairy Chiara           | Marketplace                          |
| `18966`       | [Oasis] Ethan the Butler       | Warehouse                            |
| `18967`       | [Oasis] Ethan the Butler       | Marketplace                          |
| `18974`       | [Oasis] Fairy Chiara           | Not in the sheet                     |
| `18975`       | [Oasis] Fairy Chiara           | Not in the sheet                     |
| `18976`       | [Oasis] Ethan the Butler       | Not in the sheet                     |
| `18977`       | [Oasis] Ethan the Butler       | Not in the sheet                     |

The duty is the sheet's `IsAbleInWareHouse` (warehouse) or
`IsAbleSubmitMarket` (marketplace) column. On client 3474 the `maid.dbss`
rows of `18974` to `18977` are the bytes of `18964` to `18967` with only
the key changed.

## Field Names

The `Maid_Table` sheet of a private server's `DataSheets.bexcel` on client
1784 has a `PcRoomType` column, `1` on `18964` to `18967` and `0` on its
other 17 rows; the file on client 1784 lists exactly those four keys. The
sheet names the key column `CharacterKey`, hence `character_key`. No sheet
of that workbook is named after the file; its only PC room maid data is
the `PcRoomType` column.

## Notes

- The keys match `maid.dbss` by value on both clients checked: the u8 at
  `+0x13` of each `maid.dbss` row (counted from its u16 key, where
  `maidoffset.dbss` points) is `1` on exactly the listed keys and `0` on
  the rest (4 of 21 rows on client 1784, 8 of 27 on client 3474), and the
  file lists them in the order `maidoffset.dbss` lists the rows.
- Clients 1230, 1485, 1784 and 2107 hold the 12-byte file with `18967` to
  `18964`; clients 2519, 3002, 3251 and 3474 hold the 20-byte file with
  `18977` to `18974` added in front. Client 794 has no file. The private
  server's own compiled `pcroommaid.bss` (client 1784) is the same 12 bytes
  as the client file.
- The client Lua of the maid list (`panel_window_maidlist_all`) shows a PC
  room button when `_ContentsGroup_KR_Transfer` is on and
  `ToClient_isShowRegistPcRoomMaidButton()` returns true, and the button
  calls `ToClient_RegistPcRoomMaid()`. With the same content group the maid
  list opens in a premium PC room (`isPremiumPcRoom()`) even when the
  player has no maids. The client 1784 server dump has the request
  `eTrRegistPcRoomMaidReq` and `gm::PlayerActor::registPcRoomMaid`. No
  client Lua reads the keys directly.

## Open Questions

### Why Two Sets of PC Room Maids

Client 2519 added `18974` to `18977`, copies of `18964` to `18967` with new
keys and the same names. Whether the server registers one set or both in a
PC room cannot be read from the client data, and neither the LOC nor the
client Lua says what the second set is for.
