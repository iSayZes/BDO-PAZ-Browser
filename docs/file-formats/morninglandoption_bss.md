# `morninglandoption.bss` Format

## Purpose

Three option values for the Land of the Morning Light, with no PABR magic
and no string table: two u64 numbers and one byte. On client 3474 they are
`500000`, `2000000` and `5`. The two u64 values are the silver costs of the
two resets in the Black Shrine aura window, and the byte is the number of
Black Shrine clears a family gets per week (see Field Names).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `morninglandoption.bss` | 17    | -       | -         |

| Layout | File                    | Known         | Unknown    |
| ------ | ----------------------- | ------------- | ---------- |
| 1      | `morninglandoption.bss` | 17 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type | Field                | Notes                                                              |
| ------- | ---- | -------------------- | ------------------------------------------------------------------ |
| `+0x00` | u64  | stat_reset_cost      | Silver to reset one aura's Additional Stats; `500000` on clients 2519 to 3474 |
| `+0x08` | u64  | light_orb_reset_cost | Silver to reset the Light Orbs; `2000000` on clients 2519 to 3474  |
| `+0x10` | u8   | weekly_clear_limit   | Black Shrine clears per family per week; `5` on clients 2519 to 3474 |

## Field Names

The client Lua (`panel_window_morningland_boss_all_1.luac`, client 3474)
calls `ToClient_getMorningLandOptionManager()` and reads two silver costs
from it, and no other Lua reads that manager: `getStateResetCost` for the
"Reset Aura stats?" message (`Button_MyStat_Reset`) and
`getAllStatsResetCost` for the "Reset Light Orb?" message
(`Button_Attribute_Reset`). Garmoth's Black Shrine guide (section "Black
Shrine Auras") says "Resetting only your additional stats will be 500k, so
even less than resetting your Light Orbs", which is the `500000` at `+0x00`.
The other cost, `2000000` at `+0x08`, is then the Light Orb reset.

The boss window Lua also counts against `__eElementalMonsterWeekLimit`
(weekly boss conquests), a global no Lua file defines, so the client sets
it. The official update history page "[Update History] Black Shrine (Boss
Blitz)"
([groupMasterNo 8498](https://www.naeu.playblackdesert.com/en-us/Adventure/History?_groupMasterNo=8498))
says "You have 5 weekly successful attempts per Family to defeat bosses of
the Black Shrine" (resetting at midnight on Sunday), which is the `5` at
`+0x10`, the only other value of this option file.

## Notes

- Raw bytes on clients 2519, 3002, 3251 and 3474:
  `20 A1 07 00 00 00 00 00 80 84 1E 00 00 00 00 00 05` (17 bytes).
- The file is not in the client 1784 archive. A private server's
  `DataSheets.bexcel` on client 1784 has no sheet with `MorningLand` in its
  name, so no column names carry over.
- The high four bytes of both u64 fields are `0`, so two u32 values with a
  u32 `0` after each fit the bytes too.
- The installed `BlackDesert64.exe` (client 3474) holds neither the file
  name nor `MorningLandOption` as ASCII or UTF-16 text, so it does not show
  the loader or its struct.
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`: the values alone, with no magic, string table or trailer.
  A file of any other size raises.
