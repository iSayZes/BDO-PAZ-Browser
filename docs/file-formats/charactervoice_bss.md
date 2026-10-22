# `charactervoice.bss` Format

## Purpose

The voices a player character can pick in character customization: per
character key, one list of voice names for each of two appearance types
and a voice count for each. The names (`PC_VCE_1Warrior_1`,
`PC_VCE_MN_T01_JP_Warrior_1`) sit in the PABR string table and the rows
point at them by index. On client 3482 the file holds 76 characters and 64
voice names (45 and 55 on client 1784); only Wizard (`29`) and `39859`
fill the second list.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes  | Records                | Row bytes                |
| ------ | -------------- | ------- | -------------------- | ------ | ---------------------- | ------------------------ |
| 2      | 1348 and later | 3482    | `charactervoice.bss` | 4,801  | 152 Voice List, 76 Row | 4 to 60, 16 on average   |
| 1      | 794            | 794     | `charactervoice.bss` | 10,952 | 36 Voice List, 18 Row  | 4 to 604, 299 on average |

| Layout | File                 | Known             | Unknown    |
| ------ | -------------------- | ----------------- | ---------- |
| 2      | `charactervoice.bss` | 4,801 B (100.0%)  | 0 B (0.0%) |
| 1      | `charactervoice.bss` | 10,952 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2765   | Layout 2 |
| 2519   | Layout 2 |
| 2313   | Layout 2 |
| 2107   | Layout 2 |
| 1937   | Layout 2 |
| 1784   | Layout 2 |
| 1636   | Layout 2 |
| 1485   | Layout 2 |
| 1348   | Layout 2 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | Layout 1 |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                        |
| ---------------------------- | -------- | --------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a key without a row shows as plain text |
| `languagedata_en.loc`        | Optional | Character names, LOC type 6                                                 |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                  |
| ------------------- | ----------------- | ------------------ | -------------------------------------- |
| `+0x00`             | char[4]           | magic              | ASCII `PABR`                           |
| `+0x04`             | u32               | record_count       | Number of rows                         |
| `+0x08`             | Row[record_count] | records            | See Row                                |
| `records+0x00`      | String Table      | string_table       | The voice names                        |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`      |
| `string_table+0x04` | u32               | zero               | `0`                                    |

### Row (variable: 10 bytes + voice lists)

| Offset         | Type          | Field         | Notes                                                                        |
| -------------- | ------------- | ------------- | ---------------------------------------------------------------------------- |
| `+0x00`        | u16           | character_key | Row key: a `characterstatic.dbss` character; each key once                   |
| `+0x02`        | Voice List[2] | voices        | Appearance type 0, then appearance type 1; see Voice List                    |
| `voices+0x00`  | u32[2]        | voice_count   | Voice count of appearance type 0, then 1; see Notes                          |

The rows are in no key order; client 3482 opens with 1, 2, 3, 4, 6, 5.

### Voice List (variable: 4 bytes + voice types)

| Offset  | Type                  | Field            | Notes                                         |
| ------- | --------------------- | ---------------- | --------------------------------------------- |
| `+0x00` | u32                   | voice_type_count | Number of `voice_types`; `0` for an unused appearance type |
| `+0x04` | u32[voice_type_count] | voice_types      | Index into `strings`, in the sheet's `VoiceType1` to `VoiceType20` order |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                      |
| ------- | ------------------ | ------------ | ---------------------------------------------------------- |
| `+0x00` | u32                | string_count | 64 on client 3482                                          |
| `+0x04` | pstr[string_count] | strings      | Voice names, UTF-8 (`is_wide` `0`); every string has an index pointing at it (clients 1784 and 3482) |

## Layout 1

No PABR magic and no string table: the file opens with the row count and
each list holds the voice names inline. The Row is the same as in Layout 2.

### File Layout

| Offset  | Type              | Field        | Notes          |
| ------- | ----------------- | ------------ | -------------- |
| `+0x00` | u32               | record_count | Number of rows |
| `+0x04` | Row[record_count] | records      | See Row        |

### Voice List (variable: 4 bytes + voice types)

| Offset  | Type                   | Field            | Notes                                          |
| ------- | ---------------------- | ---------------- | ---------------------------------------------- |
| `+0x00` | u32                    | voice_type_count | Number of `voice_types`                        |
| `+0x04` | str8[voice_type_count] | voice_types      | Voice names inline (`PC_VCE_1Warrior_1`)        |

Client 794 stores the file as `gamecommondata/binary/en/charactervoice.bss`
with 18 rows: 7 lists hold 17 names with a `voice_count` of 8 and 11 hold
19 names with a count of 12.

## Field Names

The `CharacterVoice_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `CharacterKey`, `CharName`,
`AppearanceType`, `VoiceCount` and `VoiceType1` to `VoiceType20`, one row
per character and appearance type: 46 rows, 45 of type `0` and one of type
`1` (character `29`). Each row matches one list of the client file.

| Field         | Column                         | Same value (client 1784) | Same value (client 3482) |
| ------------- | ------------------------------ | ------------------------ | ------------------------ |
| character_key | `CharacterKey`                 | 45 of 45                 | 25 of 45                 |
| voice_types   | `VoiceType1` to `VoiceType20`  | 46 of 46 lists           | 24 of 26 lists           |
| voice_count   | `VoiceCount`                   | 46 of 46                 | 25 of 26                 |

`AppearanceType` picks the list (`voices` entry `0` or `1`); `CharName` is
a note (`PC-워리어`) the client file does not hold. On client 3482 the 20
sheet keys `65001` to `65020` are gone; the file lists 33 keys from
`39831` to `39866` in their place. Character `8` (Wukong) holds one voice where the sheet has
`PC_VCE_6Blader_1`, and character `10` (Scholar) one where the sheet lists
eight.

## Notes

- `voice_count` equals the list length on 73 of 76 rows (client 3482). The
  three others (`30` Archer, `39860` and `39863`) list 8, 8 and 1 voices
  with a count of `2`; client 1784 has the same for `30`.
- The client Lua (`panel_customization_voice_renew.luac`, client 3482)
  fills the voice list from `getClassVoiceCount()` and picks a voice with
  `applyVoice(index, ...)`; no Lua call names a field of this table.
- The 33 keys from `39831` to `39866` (client 3482) are named
  `집사 PC-<class>` in `characterstatic.dbss`, with no LOC name; `39859` is
  `집사 PC-위자드`.
