# `solareetcoptionstaticstatus.bss` Format

## Purpose

Arena of Solare options: five f32 values with no magic, no count and no
string table. On client 3474 they are `60`, `115`, `400`, `37` and `57`; no
source confirms what any of them holds.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------- | --------- |
| 2      | 3251 and later | 3474    | `solareetcoptionstaticstatus.bss` | 20    | -       | -         |
| 1      | 3002           | 3002    | `solareetcoptionstaticstatus.bss` | 12    | -       | -         |

| Layout | File                              | Known      | Unknown       |
| ------ | --------------------------------- | ---------- | ------------- |
| 2      | `solareetcoptionstaticstatus.bss` | 0 B (0.0%) | 20 B (100.0%) |
| 1      | `solareetcoptionstaticstatus.bss` | 0 B (0.0%) | 12 B (100.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type | Field      | Notes                          |
| ------- | ---- | ---------- | ------------------------------ |
| `+0x00` | f32  | unknown_00 | `60` on clients 3251 and 3474  |
| `+0x04` | f32  | unknown_04 | `115` on clients 3251 and 3474 |
| `+0x08` | f32  | unknown_08 | `400` on clients 3251 and 3474 |
| `+0x0C` | f32  | unknown_0c | `37` on clients 3251 and 3474  |
| `+0x10` | f32  | unknown_10 | `57` on clients 3251 and 3474  |

## Layout 1

### File Layout

| Offset  | Type | Field      | Notes                |
| ------- | ---- | ---------- | -------------------- |
| `+0x00` | f32  | unknown_00 | `200` on client 3002 |
| `+0x04` | f32  | unknown_04 | `200` on client 3002 |
| `+0x08` | f32  | unknown_08 | `200` on client 3002 |

## Notes

- Raw bytes on client 3474:
  `00 00 70 42 00 00 E6 42 00 00 C8 43 00 00 14 42 00 00 64 42`
  (20 bytes). Client 3251 has the same bytes; client 3002 has
  `00 00 48 43` three times (12 bytes).
- Every value is a whole number as f32. Read as u32 they lie between
  `1108606976` and `1137180672`, so f32 is the reading.
- The file is not in the archives of clients 1784, 2107 and 2519.
- Layout 1 gives its three fields the names of the first three Layout 2
  fields by offset. Whether they hold the same options is not shown by the
  data: all three changed from `200` between clients 3002 and 3251.
- The other `*etcoptionstaticstatus.bss` files (`edania`,
  `hardcorechannel`) start with the PABR magic; this file does not.
- The handler (`_bss/solareetcoptionstaticstatus/`) reads Layout 2 with a
  layout table of the PABR option tables handler (`_bss/pabr_values/`) and
  its preview, and raises on a file of any other size. With no confirmed
  field, the preview shows the raw value bytes.

## Open Questions

### Solare Option Values

No source names the five values. The client Lua on client 3473 (152 of the
3,073 `.luac` files name Solare) has no function with `SolareEtc` or
`SolareOption` in its name; the only `EtcOption` getter is
`ToClient_GetEdaniaEtcOption`. The installed `BlackDesert64.exe` (client
3474) holds no `Solare` text as ASCII or UTF-16, so it does not show the
loader or its struct. The 2016 PDB has no `Solare` text. A private
server's `DataSheets.bexcel` on client 1784 has no sheet or column with
`Solare` in its name, its `.xlsm` folders no such file, and its server dump
no such text; the `EtcOption` sheet there is the general option sheet, with
house auction, trade and worker columns.
