# `playercharacterstatic.bss` Format

## Purpose

The player characters: a u32 count after the PABR magic, then one u16
`characterstatic.dbss` key per character. On client 3482 the 106 keys are
the classes `1` to `47` (Warrior `1`), `201` to `214` (`Warrior_TEST`,
Tamer, Musa, Valkyrie, Guardian and others), the mercenaries `521`, `523`
to `528` and `536`, and the 37 keys `39831` to `39867` named `집사 PC-<class>`. Client
1784 lists 104 keys, with `65001` to `65050` where client 3482 has the
`398xx` keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | -------------- | --------- |
| 1      | 1348 and later | 3482    | `playercharacterstatic.bss` | 232   | 1 String Table | 4         |

| Layout | File                        | Known          | Unknown    |
| ------ | --------------------------- | -------------- | ---------- |
| 1      | `playercharacterstatic.bss` | 232 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                        |
| ---------------------------- | -------- | --------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a key without a row shows as plain text |
| `languagedata_en.loc`        | Optional | Character names, LOC type 6                                                 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset               | Type                 | Field              | Notes                                                    |
| -------------------- | -------------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`              | char[4]              | magic              | ASCII `PABR`                                             |
| `+0x04`              | u32                  | character_count    | Number of keys; 106 on client 3482                       |
| `+0x08`              | u16[character_count] | character_key      | A `characterstatic.dbss` character; each key once         |
| `character_key+0x00` | String Table         | string_table       | See String Table                                         |
| `string_table+0x00`  | u32                  | string_table_start | Offset of the string table, where `character_key` ends   |
| `string_table+0x04`  | u32                  | zero               | Always `0`                                               |

On client 3482 the file is 8 + 106 x 2 + 4 + 8 = 232 bytes.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                          |
| ------- | ------------------ | ------------ | ------------------------------ |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482   |
| `+0x04` | pstr[string_count] | strings      | No field reads a string        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 is named
after the file; its `Pc_Table` holds stats per class and level (`Class`,
`Level`, `RequireEXP`, ...), not this list. The server dump of client 1784 logs `readFromBinarybyDynamic()
Failed. (playerCharacterStatic)` from `CharacterStaticStatusManager`. Every
key has a `characterstatic.dbss` row on client 3482, so `character_key`
names the meaning.

## Notes

- The keys run in descending blocks: `39855` down to `39840`, `39867` down
  to `39856`, `39839` down to `39831`, then `527` to `523`, `521`, `536`,
  `528`, `207` to `201`,
  `214` to `208`, `47` to `32`, `15` to `1` and `31` to `16` (client 3482).
- `201` to `204` are named `Warrior_TEST` to `Giant_TEST` in LOC type 6,
  `521` to `526` Combat Mercenary and `527`, `528` and `536` PC Mercenary.
