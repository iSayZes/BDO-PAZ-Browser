# `rosewarfiercebattlemonsterstaticstatus.bss` Format

## Purpose

The Rose War sanctums (fierce battles): one row per fierce battle key with
the guardian character of each team, the neutral character, the sanctum's
buff skill and its Korean name. On client 3474 the file has 22 rows: keys
`1` to `10` are the Kamasylvia side sanctums, `11` to `20` the O'dyllita
side ones, and `21` and `22` the two gimmick sanctums, 정령의 제단 and
해양 성소, guarded by Mysterious Statue alone.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                         | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `rosewarfiercebattlemonsterstaticstatus.bss` | 828   | 22 Row  | 16        |

| Layout | File                                         | Known         | Unknown     |
| ------ | -------------------------------------------- | ------------- | ----------- |
| 1      | `rosewarfiercebattlemonsterstaticstatus.bss` | 784 B (94.7%) | 44 B (5.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Character names (LOC type 6), skill names (type 10) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (16 bytes)

| Offset  | Type | Field                    | Notes                                                                                   |
| ------- | ---- | ------------------------ | --------------------------------------------------------------------------------------- |
| `+0x00` | u16  | fierce_battle_key        | Sanctum key, `1` to `22` on client 3474                                                 |
| `+0x02` | u16  | kamasylvia_character_key | Kamasylvia's guardian character (Urugon, Old Mirumok, Fadus Archer); `0` on the gimmick rows |
| `+0x04` | u16  | odyllita_character_key   | O'dyllita's guardian character (Ahib Dark Champion, Turo Berserker, Khalk); `0` on the gimmick rows |
| `+0x06` | u16  | neutral_character_key    | Neutral character: Faded Relic on the 20 sanctums, Mysterious Statue on the gimmick rows |
| `+0x08` | u8   | unknown_08               | `0` on keys `1` to `20`, `1` on the gimmick rows                                        |
| `+0x09` | u16  | skill_no                 | `skill.dbss` skill number of the sanctum buff, `62814` to `62828`                        |
| `+0x0B` | u32  | name_ref                 | String table index of the Korean sanctum name                                           |
| `+0x0F` | u8   | unknown_0f               | `0` on keys `1` to `20`, `1` on key `21`, `2` on key `22`                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                  |
| ------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `22` on client 3474, one per row    |
| `+0x04` | pstr[string_count] | strings      | Wide Korean names in row order (`오네트 제1성소`)      |

## Sanctums

Client 3474. The skill names are LOC type 10, which names these buffs by
their effect.

| Keys        | Korean names                          | Guardians (Kamasylvia, O'dyllita)                    | Skills            |
| ----------- | ------------------------------------- | ---------------------------------------------------- | ----------------- |
| `1` to `10` | `오네트 제1성소` to `오네트 제10성소` | Urugon, Ronin, Narc Brishka, Griffon, Old Mirumok, Fadus Archer, Shaman and Warrior; Ahib Salun Wolf Spearmaiden, Ahib Salun Bear Spearmaiden, Ahib Dark Champion | `62814` to `62820` |
| `11` to `20`| `오도어 제1성소` to `오도어 제10성소` | Fadus Archer, Shaman and Warrior; Olun's Golem, Ulutuka, Dark Knight, Khalk, Turo Berserker and the three Ahib | `62821` to `62827` |
| `21`        | `정령의 제단`                         | none; Mysterious Statue `21699`                       | `62828` Spirit's Blessing |
| `22`        | `해양 성소`                           | none; Mysterious Statue `21700`                       | `62828` Spirit's Blessing |

Keys `8` to `10` repeat the skills of `5` to `7`, and `18` to `20` those of
`15` to `17`.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it; the names come from the
client Lua and the companion tables:

- `fierce_battle_key`: the Lua reads a sanctum with
  `ToClient_GetRoseWarFierceBattleObjectInfoWrapper(fierceBattleKey)` and
  loops keys `1` to `20` in the revive window (`panel_rosewar_deadmessage.luac`).
- The three character keys: [`rosewarnodemonsterinfostaicstatus.bss`](rosewarnodemonsterinfostaicstatus_bss.md)
  gives every character a tooltip image. The `+0x02` characters have
  `ElfWar_Kama_*` tooltips, the `+0x04` characters `ElfWar_Odyl_*` ones and
  the `+0x06` characters `ElfWar_Kama_Neutral_Tooltip` or
  `ElfWar_Odyl_Neutral_Tooltip` (`__eRoseWarTeam_Neutral` in the Lua).
- `skill_no`: `ToClient_GetRoseWarFierceBattleObjectSkillNo(fierceBattleKeyRaw)`
  feeds `getSkillStaticStatus(skillNo, 1)` for the sanctum tooltip's buff
  lines (`panel_rosewar_minimap_5.luac`).
- `name_ref`: the Lua shows `fierceBattleStaticStatusWrapper:getName()`;
  the strings are one Korean sanctum name per row.

## Notes

- The file is the same on clients 3002, 3251 and 3474, 828 bytes. It is
  not in the archives of client 1784.
- [`rosewarfiercebattlenodestaticstatus.bss`](rosewarfiercebattlenodestaticstatus_bss.md)
  links the sanctums, and the sanctum revive points of
  [`rosewarrevivepositionstaticstatus.bss`](rosewarrevivepositionstaticstatus_bss.md)
  use the same keys.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  the key and the Korean name first.

## Open Questions

### The Two Gimmick Flags

`unknown_08` is `1` and `unknown_0f` `1` or `2` on the two gimmick rows
only. The radar Lua (`radar.luac`, client 3474) has two gimmick sanctum
icons, `radarType_RoseWarGimicAdrenalinFierceBattle` and
`radarType_RoseWarGimicConquestFierceBattle`, and the war log has
`_Occupy_GimicAdrenalinFierceBattle` and `_Occupy_GimicConquestFierceBattle`,
which reads as `unknown_0f` holding the gimmick kind, but no Lua ties a
value to either name.
