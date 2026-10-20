# `npcgiftetc.bss` Format

## Purpose

The global values of the NPC gift and confession system: the Energy cost of a gift and of a confession, the lowest amity for a confession and the highest item price a gift may have. The file is one fixed-size `PABR` block with no row count or companion offset table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `npcgiftetc.bss` | 32    | -       | -         |

| Layout | File             | Known        | Unknown      |
| ------ | ---------------- | ------------ | ------------ |
| 1      | `npcgiftetc.bss` | 20 B (62.5%) | 12 B (37.5%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The file is exactly 32 bytes. Unlike DBSS records, it does not start with a record count; the first four bytes are the ASCII magic `PABR`.

| Offset  | Type    | Field                | Client 3473 | Notes                                                 |
| ------- | ------- | -------------------- | ----------- | ----------------------------------------------------- |
| `+0x00` | char[4] | magic                | `PABR`      | Fixed ASCII file signature                            |
| `+0x04` | u16     | use_gift_wp          | 5           | Energy spent on one gift (`UseGiftWp`)                |
| `+0x06` | u16     | use_propose_wp       | 5           | Energy spent on one confession (`UseProposeWp`)       |
| `+0x08` | u32     | min_propose_intimacy | 1000        | Lowest amity for a confession (`MinProposeIntimacy`)  |
| `+0x0C` | u64     | limit_gift_price     | 50000000    | Highest item price a gift may have (`LimitGiftPrice`) |
| `+0x14` | u32     | unknown_14           | 0           | Observed zero                                         |
| `+0x18` | u32     | unknown_18           | 20          | Not a `NpcGift_Option` column                         |
| `+0x1C` | u32     | unknown_1c           | 0           | Observed zero                                         |

## Field Names

The four named fields are the columns of the one-row `NpcGift_Option` sheet, in sheet order, that a private server on client 1784 ships in its `DataSheets.bexcel` and in the developer workbook `DataSheet_IntimacyDataTable.xlsm`. The sheet row is `5`, `5`, `1000`, `50000000`, the same values as client 3473, and that private server's own `npcgiftetc.bss` built from the sheet is byte-identical to the client 3473 file. The workbook's Korean column comments give the meanings:

| Column               | Comment             | English                                        |
| -------------------- | ------------------- | ---------------------------------------------- |
| `UseGiftWp`          | 선물 줄 때 기운 소모        | Energy spent when giving a gift                |
| `UseProposeWp`       | 고백 할 때 기운 소모        | Energy spent when confessing                   |
| `MinProposeIntimacy` | 고백 가능 최소 친밀도        | Lowest amity at which a confession is possible |
| `LimitGiftPrice`     | 선물할 수 있는 아이템 가격 한계값 | Price limit of an item that can be given       |

The field widths come from the server dump of that private server. Its `NpcGift_Option` loader reads exactly these four columns and stores them in a 16-byte global: `UseGiftWp` and `UseProposeWp` as u16 at `+0` and `+2`, `MinProposeIntimacy` as u32 at `+4` and `LimitGiftPrice` as an 8-byte value at `+8`. That global is the file's `+0x04..+0x14`, so the price is a u64 and the former `unknown_10` is its high half.

Neither the 2016 client with debug symbols nor the code of a private server on client 519 has a gift option type or loader; the workbook comments date the gift sheets to 2019-04-09. That server's `NpcGift_Option` table holds `0` in every column. The client Lua gift window (`panel_dialog_npcgift_renew.lua`) calls `ToClient_giveNpcGift` and `ToClient_proposeToNpc` and reads none of these values.

## Notes

- `npcgiftetc.bss` is self-contained; no offset companion has been observed.
- The block uses the same `PABR` magic seen in several compact BSS lookup and config files, but this file holds scalar config values, not a repeated table.
- Earlier versions of this doc called `use_gift_wp`, `use_propose_wp`, `min_propose_intimacy`, the low half of `limit_gift_price` and `unknown_18` `config_a` to `config_e`, and then `unknown_04` to `unknown_18`.
- The file is byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.

## Open Questions

### The Three Trailing u32 Fields

`unknown_14`, `unknown_18` and `unknown_1c` (`0`, `20`, `0` on client 3473) are not `NpcGift_Option` columns, and the server dump's loader does not write them. The client 1784 build of the four-column sheet still writes `20` at `+0x18`, so the value comes from the client's own struct, not from the sheet. Its meaning is unknown.
