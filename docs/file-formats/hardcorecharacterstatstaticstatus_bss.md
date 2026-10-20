# `hardcorecharacterstatstaticstatus.bss` Format

## Purpose

One stat body per class type, in the layout of the
[experience.bss](experience_bss.md) level records. The name ties it to the
Hardcore server (`ToClient_isHardCoreCharacter` in the client Lua), which LOC
type 37 says needs a level 60+ character on a normal server. On client 3464
every row equals the `experience.bss` level 60 body: AP `+1` and DP `+1`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records              | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | -------------------- | --------- |
| 1      | 3473 and later | 3474    | `hardcorecharacterstatstaticstatus.bss` | 9,474 | 47 Stat Body, 47 Row | 200       |

| Layout | File                                    | Known           | Unknown         |
| ------ | --------------------------------------- | --------------- | --------------- |
| 1      | `hardcorecharacterstatstaticstatus.bss` | 2,142 B (22.6%) | 7,332 B (77.4%) |

<!-- versions:end -->

## Companion Files

The file is self-contained. The handler reads class names through the shared
LOC lookup:

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Class names (LOC type 21, `str_id1` = class type) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with no row count after the magic: the rows start at `+0x04`
and fill the space up to the string table.

| Offset              | Type               | Field        | Notes                                                  |
| ------------------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                           |
| `+0x04`             | Row[..table_start] | rows         | 47 rows (class types 0 to 46) on client 3464; see Row  |
| `rows+0x00`         | String Table       | string_table | See String Table                                       |
| `EOF-0x08`          | u32                | table_start  | Offset of the string table, where the rows end         |
| `EOF-0x04`          | u32                | zero         | Always 0                                               |

On client 3464 the 47 rows end at `0x24EB`, the stored `table_start`. The
string table holds one wide string, `1D1`, as in `experience.bss`.

### Row (201 bytes)

Fields are unaligned.

| Offset  | Type      | Field      | Notes                                                        |
| ------- | --------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8        | class_type | Equals the row index; the class type `getClassType()` returns |
| `+0x01` | Stat Body | stats      | The [experience.bss](experience_bss.md) Stat Body            |

The body fields (`max_hp`, `max_mp`, the luck and speed limits, the
`unknown_*` fields, `ap_bonus` and `dp_bonus`) keep the names and the body-relative offsets of the
`experience.bss` Stat Body table; `max_hp` and `max_mp` hold the `1.0` and `1`
placeholders here too.

### Stat Body (200 bytes)

The [experience.bss](experience_bss.md) Stat Body, read by
`_bss/experience/stat_body.py`. Offsets are from the start of the body, `+0x01`
in a row.

| Offset  | Type      | Field               | Notes                                     |
| ------- | --------- | ------------------- | ----------------------------------------- |
| `+0x00` | bytes[4]  | unknown_00          | Always `0` (client 3464)                  |
| `+0x04` | f32       | max_hp              | `1.0` placeholder                         |
| `+0x08` | u32       | max_mp              | `1` placeholder                           |
| `+0x0C` | bytes[20] | unknown_0c          | Always `0` (client 3464)                  |
| `+0x20` | f32       | unknown_20          | `1.0` on every row (client 3464)          |
| `+0x24` | bytes[20] | unknown_24          | Always `0` (client 3464)                  |
| `+0x38` | u32       | max_critical_rate   | `0` on every row (client 3464)            |
| `+0x3C` | u32       | max_drop_item_luck  | `5` on every row (client 3464)            |
| `+0x40` | u32       | max_fishing_luck    | `5` on every row (client 3464)            |
| `+0x44` | u32       | max_collection_luck | `5` on every row (client 3464)            |
| `+0x48` | bytes[8]  | unknown_48          | Always `0` (client 3464)                  |
| `+0x50` | f32       | unknown_50          | `1.0` on every row (client 3464)          |
| `+0x54` | bytes[16] | unknown_54          | Always `0` (client 3464)                  |
| `+0x64` | u32[3]    | max_varied_speed    | Attack, movement and casting speed limits; `5, 5, 5` on every row (client 3464) |
| `+0x70` | f32       | unknown_70          | `1.0` on every row (client 3464)          |
| `+0x74` | f32       | ap_bonus            | AP `+1` on every row (client 3464)        |
| `+0x78` | f32       | dp_bonus            | DP `+1` on every row (client 3464)        |
| `+0x7C` | bytes[76] | unknown_7c          | Always `0` (client 3464)                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                  |
| ------- | ------------------ | ------------ | -------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                      |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries                    |

## Notes

- On client 3464 all 47 bodies are byte-identical and equal the
  `experience.bss` level 60 to 130 body, the one with both bonuses.
- The table has a row for every class type, while the LOC type 37 server
  text (id `970407542`) opens Hardcore characters to four classes: Warrior,
  Ranger, Sorceress and Berserker. The class list comes from the server
  through `ToClient_getHardCorePossbieClassFromIndex()` in
  `panel_lobby_classselect_renew.lua`.
- The two `5, 5, 5` triads are the drop item, fishing and collection luck
  limits and `max_varied_speed`, named in the
  [experience.bss](experience_bss.md#field-names) Field Names.
- bdo-data-extractor describes the same 201-byte rows and the level 60
  match.
- The parser is `_bss/hardcorecharacterstatstaticstatus/parser.py`; it reads
  the body through `_bss/experience/stat_body.py`.

## Open Questions

### What Reads the Table

No client Lua names the file or a function that returns its values. The
Hardcore basic info panel (`panel_characterinfo_hardcore_basic_all_3.lua`,
`FromClient_CharInfoBasic_HardCore_All_BattleStatUpdate`) shows total AP and
DP through `ToClient_getOffence()` and `ToClient_getDefence()`, the same
getters the normal panel calls, so a Hardcore character's totals do not show
whether the server adds this row in place of the `experience.bss` record.
Garmoth's Hardcore PvP Server guide (pre-season, March 2025) lists a level 63
start and Combat EXP as unavailable. Level 63 falls in the `experience.bss`
level 60 to 130 range, whose body equals every row here, so both readings give
the same AP and DP. The client data holds no starting level: the lobby reads
the entry level from `ToClient_isHardCoreChannelEnterPossibleLevel()`.
