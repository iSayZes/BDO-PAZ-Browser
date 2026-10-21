# `elementalstat.bss` Format

## Purpose

One row per aura of the Black Shrine (검은 사당) boss blitz in the Land of
the Morning Light: Sun Aura, Moon Aura and Earth Aura. The player enhances an
aura with Light Orbs and spends the Additional Stats it gives on the aura's
AP and DP. Each row holds the aura's `element_type` and what one Light Orb
adds to it: 50 AP, 100 DP and 3 Additional Stats on every row (client
3474).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `elementalstat.bss` | 46    | 3 Row   | 14        |

| Layout | File                | Known         | Unknown    |
| ------ | ------------------- | ------------- | ---------- |
| 1      | `elementalstat.bss` | 46 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. The handler names each aura with its LOC type 37 text (GAME sheet
keys `LUA_MORNING_ATTRBOSS_SUN`, `_MOON` and `_SOIL`, the keys the Black
Shrine window uses) from `languagedata_*.loc` when it is loaded, and with the
enum name otherwise.

All multi-byte values are little-endian.

## Layout 1

### File Layout

Plain binary: no `PABR` magic, no offset file and no trailer.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 3 x 14 = 46 bytes on client 3474, in
the order `2`, `1`, `0`.

### Row (14 bytes)

| Offset  | Type | Field               | Notes                                                       |
| ------- | ---- | ------------------- | ----------------------------------------------------------- |
| `+0x00` | u8   | element_type        | Row key, see [Element Types](#element-types)                |
| `+0x01` | u32  | ap_per_orb          | AP per activated Light Orb; `50` on every row (client 3474) |
| `+0x05` | u32  | dp_per_orb          | DP per activated Light Orb; `100` on every row (client 3474) |
| `+0x09` | u32  | stat_points_per_orb | Additional Stats per activated Light Orb; `3` on every row (client 3474) |
| `+0x0d` | u8   | element_type_dup    | Equals `element_type` on every row                          |

## Element Types

| Value | Lua enum                 | Name (LOC, client 3474) |
| ----- | ------------------------ | ----------------------- |
| `0`   | `__eElementalStat_Sun`   | Sun Aura                |
| `1`   | `__eElementalStat_Moon`  | Moon Aura               |
| `2`   | `__eElementalStat_Land`  | Earth Aura              |

## Field Names

No reference source has the file. It first appears on client 2519 (absent
on client 2107), so a private server's `DataSheets.bexcel`, `.xlsm` sheets
and server dump on client 1784 have no `Elemental` sheet or column, the 2016
client and the client 519 server tables predate it, and the live client exe
holds no readable strings.

`element_type` follows the client Lua of the Black Shrine window
(`panel_window_morningland_boss_all.luac` and `_all_1.luac`). It passes
`__eElementalStat_Sun`, `_Moon` and `_Land` to `initSelectedElementalType`
from the buttons `Radiobutton_Attribute_Tap0` to `Tap2`, finds the button of
a type at list position `type + 1`, and indexes `_effectChar` (`[0]`, `[1]`,
`[2]`) by the type, so the three values are `0`, `1` and `2` in that order.
`panel_personalicon_left_remaster.luac` uses the same order for the aura
buffs (`_elementalMonsterBuffSun = 0`, `Moon = 1`, `Land = 2`). A boss's
weak aura comes from `getElementalStatType()` on the same scale.

The three u32 values follow Garmoth's Black Shrine guide (section "Black
Shrine Auras"): "Investing a light orb increases attack power (AP) by 50 and
defense power (DP) by 100 for that attribute/aura each time you invest one,
and it grants you 3 additional stat points." The three numbers are distinct
and sit in that order in every row, so `ap_per_orb`, `dp_per_orb` and
`stat_points_per_orb` take them in file order.

## Notes

- The file is the same 46 bytes on clients 2519, 3002, 3251 and 3474.
- The Black Shrine window reads per aura `ToClient_GetElementVaryPontCount(type)`,
  `ToClient_GetElementPointStat(type)` (`_fixedPoint`, `_addedPoint`,
  `_offencePoint`, `_defencePoint`) and `ToClient_GetCaculateOffenceStat(type)`
  / `ToClient_GetCaculateDffenceStat(type)`, and the global
  `ToClient_GetMaxElementPoint()` and `ToClient_GetRemainElementPoint()`. It
  shows `(fixedPoint + addedPoint) * ToClient_GetElementVaryPontCount(type)`
  as the aura's Additional Stats, and caps the Light Orb row of one aura at
  10 (`_elementStatMax`, a Lua constant). None of these reads a field of
  this file by name.
- The Light Orb is item `66667`. The tooltip `LUA_MORNING_ATTRBOSS_TOOLTIP_9`
  says "Gain additional AP and DP stats depending on the number of activated
  auras".
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`, one row per aura.
- The server Blessings of the Sun, Moon and Earth that a defeated boss
  gives are in [`elementalserverbuff.bss`](elementalserverbuff_bss.md).
- The weak aura of each boss is the `element_type` of
  [`elementalmonsterstat.bss`](elementalmonsterstat_bss.md), on the same
  scale; its ranking rewards are in
  [`elementalmonsterreward.bss`](elementalmonsterreward_bss.md).
