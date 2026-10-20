# `carriagespec.dbss` Format

## Purpose

One row per transport carriage type of the warehouse transport window
(`ToClient_NewDelivery*` in the client Lua): travel speed, loadage, weight
limits, base fee and fee per weight, and which kinds of trade goods it may
carry. On client 3474 the file has 2 rows, carriage keys `1` and `2`.
Companion `carriagespecoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `carriagespec.dbss`       | 84    | 2 Row        | 40        |
| 1      | 1485 and later | 3474    | `carriagespecoffset.dbss` | 22    | 2 Offset Row | 9         |

| Layout | File                      | Known         | Unknown    |
| ------ | ------------------------- | ------------- | ---------- |
| 1      | `carriagespec.dbss`       | 84 B (100.0%) | 0 B (0.0%) |
| 1      | `carriagespecoffset.dbss` | 22 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                 |
| ------------------------- | -------- | -------------------------------------------------------------------- |
| `carriagespecoffset.dbss` | Optional | `carriage_key -> (offset, size)` of every row; the main file can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (40 bytes)

| Offset  | Type | Field                             | Notes                                                    |
| ------- | ---- | --------------------------------- | -------------------------------------------------------- |
| `+0x00` | u8   | carriage_key                      | Carriage type; the offset file points here               |
| `+0x01` | i32  | distance_per_minute               | `6500` on both rows (client 3474)                        |
| `+0x05` | i32  | loadage                           | `20` on both rows (client 3474)                          |
| `+0x09` | i32  | transport_max_weight              | See Values per Carriage                                  |
| `+0x0D` | i32  | camasilb_add_transport_max_weight | `15000000` on both rows (client 3474)                    |
| `+0x11` | i64  | base_fee                          | See Values per Carriage                                  |
| `+0x19` | i32  | overload_weight                   | Equal to `transport_max_weight` on both rows (client 3474) |
| `+0x1D` | i64  | fee_per_weight                    | `1` on both rows (client 3474)                           |
| `+0x25` | u8   | non_stack_trade                   | Bool                                                     |
| `+0x26` | u8   | stack_trade                       | Bool                                                     |
| `+0x27` | u8   | expiration_period_trade           | Bool; `0` on both rows (client 3474)                     |

### `carriagespecoffset.dbss`

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `carriagespec.dbss` count    |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row    |

### Offset Row (9 bytes)

| Offset  | Type | Field        | Notes                                         |
| ------- | ---- | ------------ | --------------------------------------------- |
| `+0x00` | u8   | carriage_key | Key of the row it points at                   |
| `+0x01` | u32  | offset       | Row start, at its `carriage_key`              |
| `+0x05` | u32  | size         | The whole row: always `40`                    |

Read by `parse_bare_u8_offset_rows()` in `_common/pabr_offset.py`.

## Values per Carriage

Every field that differs between the two rows or between clients. The
rest are the same on both rows and both clients (see the Row notes).

| `carriage_key` | Client | `transport_max_weight` | `overload_weight` | `base_fee` | `non_stack_trade` | `stack_trade` |
| -------------- | ------ | ---------------------- | ----------------- | ---------- | ----------------- | ------------- |
| 1              | 1784   | 15000000               | 15000000          | 10         | 0                 | 0             |
| 1              | 3474   | 15000000               | 15000000          | 10         | 0                 | 0             |
| 2              | 1784   | 300000000              | 300000000         | 30         | 1                 | 1             |
| 2              | 3474   | 600000000              | 600000000         | 3          | 1                 | 1             |

## Field Names

The names follow the `New_Carriage2_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (the same sheet sits in its
`datasheet_plantdatatable.xlsm`, with no developer comments). Its columns are
`CarriageKey`, `DistancePerMinute`, `Loadage`, `BaseFee`,
`TransportMaxWeight`, `OverLoadWeight`, `FeePerWeight`, `NonStackTrade`,
`StackTrade`, `ExpirationPeriodTrade` and `CamasilbAddTransportMaxWeight`.
Both of its rows match the file on client 1784 in all 11 columns (2 of 2
keys). On client 3474 key `1` still matches in all 11; key `2` differs in
`BaseFee`, `TransportMaxWeight` and `OverLoadWeight` (table above), a
rebalance after client 1784.

The file order is not the sheet order. The client 1784 server dump
(`Instance_dumpFull.exe`) reads the sheet in the function at VA
`0x140a05260`: `CarriageKey` with `ReadCellInt8` into a byte at `+0x00`,
then `DistancePerMinute`, `Loadage`, `TransportMaxWeight` and
`CamasilbAddTransportMaxWeight` with `ReadColumnInt` at `+0x04` to `+0x10`,
`BaseFee` with `ReadColumnInt` widened to 8 bytes at `+0x18`,
`OverLoadWeight` with `ReadColumnInt` at `+0x20`, `FeePerWeight` with
`ReadColumnInt64` at `+0x28` and the three trade columns with
`ReadColumnBool` at `+0x30` to `+0x32`. Packed with no padding, that order
and those widths give the 40-byte row of the file, and the values of both
clients land in the matching fields. `CamasilbAddTransportMaxWeight` keeps
the sheet's spelling as `camasilb_add_transport_max_weight`.

The 2016 client's debug symbols have no carriage spec struct; their
`ge::wrapper::DeliveryCarriageInfo` (character key and name) belongs to the
older delivery system. The `Carriage_Table` of a private server on client
519 is that older table (per-route waypoints and prices) and has none of
these columns.

## Notes

- Clients 1485 and 1784 have the same 84-byte main file and 22-byte offset
  file layout; only the key `2` values in the table above differ.
- Client 1230 has no `carriagespec.dbss`. Its `carriagespec.bss` is a PABR
  file of the same 2 rows in 36-byte rows with a 12-byte trailer: the order
  above without `camasilb_add_transport_max_weight`. Client 794 has neither
  file.
- `carriagechar.bss` comes from the `New_Carriage_Table` sheet of the same
  workbook (`CharacterKey`, `ObjectName`: world map models
  `WorldMap_Cart.pam`, `WorldMap_WoodenBoat_small.pam`,
  `WorldMap_SailingShip.pam`) and has no carriage key column, so it does not
  join this file.
- The transport window (`panel_window_delivery_all`) labels deliverers at
  or above the client constant `__eDeliveryTradeCarriageIndex` with
  `LUA_DELIVERYNEW_FIVENUMBER_CARRIAGE` and the rest with
  `LUA_DELIVERYNEW_NUMBEROF_CARRIAGE`, and shows the remaining and maximum
  weight from `ToClient_NewDeliveryGetRemainWeight()` and
  `ToClient_NewDeliveryGetMaxWeightPerCarriage()` times `1.0E-4` as LT. No
  Lua names `carriagespec` or its columns.

## Open Questions

### Which Carriage Key Is Which

Key `2` has a 40 times larger `transport_max_weight` on client 3474 and is
the only row with `non_stack_trade` and `stack_trade` set, so it may be the
trade carriage that the transport window numbers from
`__eDeliveryTradeCarriageIndex`. The client Lua passes deliverer indexes,
not carriage keys, so the data does not tie the two together.

### Units of distance_per_minute, loadage and the Fees

The transport window divides weights by 10,000 for its LT label, so
`transport_max_weight` `15000000` would read as 1,500 LT, but the Lua reads
the limit through `ToClient_NewDeliveryGetMaxWeightPerCarriage()`, not from
this file. What `distance_per_minute` (`6500`) and `loadage` (`20`) count,
and how `base_fee` and `fee_per_weight` add up to
`Toclient_NewDeliveryGetPackItemTotalPrice()`, is open.

### camasilb_add_transport_max_weight

`15000000` on both rows and both clients. The column name reads as extra
transport weight tied to Kamasylvia or Kamasylve (`카마실브`); what grants it
is open.
