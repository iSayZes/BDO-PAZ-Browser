# `elementalserverbuff.bss` Format

## Purpose

The server-wide Blessings of the Black Shrine (Land of the Morning Light):
after a Black Shrine boss is defeated, its server gets the Blessing of the
Sun (AP), the Blessing of the Moon (DP) or the Blessing of the Earth (Item
Drop Rate) for 180 minutes. Each of the four rows holds the three blessing
values and their duration, `1` AP, `1` DP, `200000` (+20%) and `10800`
seconds on every row (client 3474). What the row key stands for is open. The file has no
PABR magic and no trailer. The aura stats of the same content are in
[`elementalstat.bss`](elementalstat_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 2519 and later | 3474    | `elementalserverbuff.bss` | 92    | 4 Row   | 22        |

| Layout | File                      | Known        | Unknown      |
| ------ | ------------------------- | ------------ | ------------ |
| 1      | `elementalserverbuff.bss` | 68 B (73.9%) | 24 B (26.1%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

The rows fill the file exactly: 4 + 4 x 22 = 92 bytes on client 3474, in
the order `9`, `8`, `7`, `6`.

### Row (22 bytes)

| Offset  | Type | Field                    | Notes                                                                  |
| ------- | ---- | ------------------------ | ---------------------------------------------------------------------- |
| `+0x00` | u8   | unknown_00               | Row key, `6` to `9` on client 3474; see Open Questions                 |
| `+0x01` | u8   | unknown_01               | Equals `unknown_00` on every row                                       |
| `+0x02` | f32  | sun_blessing_ap          | AP of the Blessing of the Sun; `1.0` on every row (client 3474)        |
| `+0x06` | f32  | moon_blessing_dp         | DP of the Blessing of the Moon; `1.0` on every row (client 3474)       |
| `+0x0a` | u32  | earth_blessing_drop_rate | Item Drop Rate of the Blessing of the Earth; 1,000,000 = 100%, `200000` (+20%) on every row (client 3474) |
| `+0x0e` | u32  | buff_duration            | Seconds the blessing lasts; `10800` (180 minutes) on every row (client 3474) |
| `+0x12` | u32  | unknown_12               | `0` on every row (client 3474)                                         |

## Field Names

No reference source has the file. It first appears on client 2519 (absent
on client 2107), so a private server's `DataSheets.bexcel` on client 1784
has no sheet with `Elemental` in its name, and the 2016 client and the
client 519 server tables predate it.

The three blessing fields follow the client Lua and LOC of client 3474.
`panel_personalicon_left_remaster.luac` shows one icon for the three
blessings (`ElementalMonsterBuff`), asks `ToClient_isAppliedElementalMonsterBuff(type)`
and `ToClient_getElementalMonsterBuffRemainTime(type)` for the Sun (`0`),
Moon (`1`) and Land (`2`) types, the order of
[Element Types](elementalstat_bss.md#element-types), and fills the tooltip
from three resource strings:

| Lua type | Tooltip (LOC, client 3474)                                                     | Field                    |
| -------- | ------------------------------------------------------------------------------ | ------------------------ |
| `0` Sun  | "Great Adventurer {familyName} bestows the Blessing of the Sun. AP +1"          | sun_blessing_ap          |
| `1` Moon | "Great Adventurer {familyName} bestows the Blessing of the Moon. DP +1"         | moon_blessing_dp         |
| `2` Land | "Great Adventurer {familyName} bestows the Blessing of the Earth. Item Drop Rate +20%" | earth_blessing_drop_rate |

The values `1`, `1` and `200000` (+20% on the 1,000,000 = 100% scale) sit
in that order in every row. The Item Drop Rate tooltip adds: "Blessing of
the Earth is applied for a certain period on a server where a Black Shrine
boss vulnerable to earth is defeated."

`buff_duration` follows the official Black Desert wiki page "Black Shrine:
Donghae (Solo)" (section "Blessing of Morning Light"): "This buff lasts for
180 minutes", which is `10800` seconds. The same page lists the blessings
as Blessing of the Warm Sun (AP +1), Blessing of the Soft Moon (DP +1) and
Blessing of the Thriving Earth (Item Drop Rate +20%), each from its own
bosses.

## Notes

- The file is the same 92 bytes on clients 3002, 3251 and 3474. On client
  2519, row `6` held `2.0`, `2.0` and `400000` (+40%), twice the values of
  the other rows; the three blessing fields doubled together, and
  `buff_duration` stayed `10800`.
- The official event notice "[Black Shrine] Enhanced Blessing and
  Unpurified Energy"
  ([groupContentNo 8743](https://www.naeu.playblackdesert.com/en-us/News/Detail?groupContentNo=8743),
  July 2 to 17, 2025) doubles the Blessing of the Morning on the server:
  AP +1 to +2 (Sun Aura bosses Golden Pig King, Oduksini, Apex Changui),
  DP +1 to +2 (Moon Aura: Bari, Songakshi, Bamboo Legion Lieutenant) and
  Item Drop Rate +20% to +40% (Earth Aura: Sangoon, Gumiho, Duoksini,
  Imoogi), and says the buffs "last for 3 hours, same as before". That is
  the doubled set of row `6` on client 2519 (2024-05, before this event),
  so an event of the same kind was likely live in that build.
- The stat values are `f32` while the tooltip text writes whole numbers;
  `1.0` is the only value seen, so the file does not show whether the
  client rounds them.
- The tooltip text holds the numbers itself (`AP +1`, `Item Drop Rate
  +20%`); the Lua fills only `{familyName}` and the remaining time, so a
  changed value in this file would not change the text.
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`, one row per key. The Item Drop Rate cell shows the bonus
  (`+20%`) and the Duration cell the time (`3h`); the record keeps the
  stored values.

## Open Questions

### Row Key

`unknown_00` runs `6` to `9`, with a copy in `unknown_01`. The Black Shrine
window (`panel_window_morningland_boss_all_1.luac`) has ten boss groups and
ten difficulty levels (`getLevel()` `0` to `9`, shown as Calamity 1 to 10),
so the key fits either a stored level (Calamity 7 to 10) or a boss group.
No Lua reads the key. The official Black Desert wiki page "Black Shrine:
Donghae (Solo)" says the blessing comes "every time the highest Calamity
difficulty is completed", and the page lists ten bosses (three for the
Sun, three for the Moon, four for the Earth), so neither reading follows
from it. If the key is the level, the blessings would come from Calamity 7
up. On client 2519 row `6` held twice the blessing values of rows `7` to
`9`, the set an enhanced blessing event gives (see Notes); a higher level
would not explain it, while an event applied to one row would, if row `6`
was the only one in use then.

