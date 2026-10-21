# `petleaderbuff.bss` Format

## Purpose

The alpha pet bonus per pet tier: how much an alpha pet ("Pack Leader")
cuts the loot cooldown of every active pet. The client reads it through
`ToClient_getPetLeaderBuff(tier)`. On client 3474 the file holds one entry,
tier `4` (Tier 5 in the game) with `150000`, which reads as 15% on the
client's 1,000,000 = 100% rate scale (see Notes). The file has
no PABR magic and no trailer.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 2107 and later | 3474    | `petleaderbuff.bss` | 10    | 1 Entry | 6         |

| Layout | File                | Known       | Unknown     |
| ------ | ------------------- | ----------- | ----------- |
| 1      | `petleaderbuff.bss` | 9 B (90.0%) | 1 B (10.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
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

| Offset  | Type         | Field   | Notes                                  |
| ------- | ------------ | ------- | -------------------------------------- |
| `+0x00` | u32          | count   | Number of entries; `1` on client 3474  |
| `+0x04` | Entry[count] | entries | See Entry                              |

### Entry (6 bytes)

| Offset  | Type | Field            | Notes                                                                 |
| ------- | ---- | ---------------- | --------------------------------------------------------------------- |
| `+0x00` | u8   | pet_tier         | Map key: the pet tier as `tier` of [`pet.dbss`](pet_dbss.md) stores it, from 0; `4` is Tier 5 |
| `+0x01` | u8   | unknown_01       | `4` on the only entry, equal to `pet_tier`                            |
| `+0x02` | u32  | leader_buff_rate | Loot cooldown cut for active pets; 1,000,000 = 100%, `150000` (15%) on client 3474 |

## Field Names

No reference source has the table: the file is in the client 2107 archive
but not in the client 1784 one, and a private server's `DataSheets.bexcel`
and `.xlsm` sheets on client 1784 have no sheet or column with `Leader` in
its name. The names come from the client Lua of client 3474:

- `panel_dialog_petleader_all_1.luac` and `panel_window_petlist_all_1.luac`
  call `ToClient_getPetLeaderBuff(petStaticStatus:getPetTier())` and fill the
  result into the resource string `PANEL_WINDOW_PETLEADER_SKILL_DESC`,
  "Pack Leader: Loot cooldown -{percent}% for active pets" (Korean
  `우리들의 골목대장 : 찾은 반려동물 모두의 줍기 재사용 대기시간 감소 ({percent}%)`).
  The Lua names the value `leaderBuffPercent`.
- `getPetTier()` is the stored tier: both scripts add 1 for display
  (`petTier = petStaticStatus:getPetTier() + 1`), and the training window
  asks for the tier the Tier 4 pet trains into. `pet_tier` `4` is therefore Tier 5,
  the only tier that can be appointed alpha (`LUA_PETLEADER_TOOLTIP_DESC`:
  "Appoints one Tier 5 pet as the alpha").

The Lua does not show which of the two equal bytes the client looks the tier
up by; see Open Questions.

## Notes

- Raw bytes on client 3474: `01 00 00 00 04 04 F0 49 02 00`. Clients 2107,
  2519, 3002 and 3251 ship the same ten bytes.
- `global_contentsoptions.luac` sets
  `_ContentsGroup_PetLeader = ToClient_IsContentsGroupOpen("1832")`. Both
  pet leader windows return early when it is off.
- The installed `BlackDesert64.exe` (client 3474) holds no `PetLeader` or
  `leaderbuff` text as ASCII or UTF-16, so it does not show the loader.
- No buff key is stored: the bonus is a rate, not a `buff.dbss` reference.
- The item the Tier 5 training uses is in [`petupgrade.bss`](petupgrade_bss.md).
- In game on client 3474, the Tier 5 Pet Training window shows "Pack
  Leader: Loot cooldown -15% for active pets" under Tier 5 Pet Effects,
  which is `150000` on the 1,000,000 = 100% scale.
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`. The Loot Cooldown cell shows `leader_buff_rate` as that
  cut (`-15%`); the record keeps the stored value.

## Open Questions

### Second Tier Byte

`unknown_01` equals `pet_tier` on the only entry. `plantupgradeparam.bss`
stores its map key again as the first member of the value (`param_key`),
which would make this byte a copy of the tier. With one entry the file
cannot tell a copy from a separate field that happens to hold `4`.
