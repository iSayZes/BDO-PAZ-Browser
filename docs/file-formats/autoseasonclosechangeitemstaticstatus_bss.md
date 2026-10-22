# `autoseasonclosechangeitemstaticstatus.bss` Format

## Purpose

The Season server gear conversions: per row a conversion item ([Season]
Tuvala Helmet Conversion Stone), the Season item it applies to and the
normal item it turns into. After the rows come four lists of the season's
graduation settings: the season challenges with their reward items, the
character types, the graduation quest and the graduation items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                        | Bytes | Records                                      | Row bytes |
| ------ | -------------- | ------- | ------------------------------------------- | ----- | -------------------------------------------- | --------- |
| 1      | 1636 and later | 3482    | `autoseasonclosechangeitemstaticstatus.bss` | 1,496 | 89 Row, 2 Season Challenge, 2 Character Type | 16        |

| Layout | File                                        | Known           | Unknown     |
| ------ | ------------------------------------------- | --------------- | ----------- |
| 1      | `autoseasonclosechangeitemstaticstatus.bss` | 1,484 B (99.2%) | 12 B (0.8%) |

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
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                                   | Type                                            | Field                                | Notes                                                    |
| ---------------------------------------- | ----------------------------------------------- | ------------------------------------ | -------------------------------------------------------- |
| `+0x00`                                  | char[4]                                         | magic                                | ASCII `PABR`                                             |
| `+0x04`                                  | u32                                             | row_count                            | Number of rows                                           |
| `+0x08`                                  | Row[row_count]                                  | rows                                 | See Row                                                  |
| `rows+0x00`                              | u32                                             | season_challenge_count               | Number of `season_challenges`; `2` on every client checked |
| `rows+0x04`                              | Season Challenge[season_challenge_count]        | season_challenges                    | See Season Challenge                                     |
| `season_challenges+0x00`                 | u32                                             | character_type_count                 | Number of `auto_graduation_character_types`              |
| `season_challenges+0x04`                 | Character Type[character_type_count]            | auto_graduation_character_types      | See Character Type                                       |
| `auto_graduation_character_types+0x00`   | u32                                             | graduation_quest_count               | Number of `auto_graduation_quests`; `1`                  |
| `auto_graduation_character_types+0x04`   | u32[graduation_quest_count]                     | auto_graduation_quests               | Packed quest IDs (low u16 chain, high u16 quest); `40071/2` on client 3482 |
| `auto_graduation_quests+0x00`            | u32                                             | graduation_item_count                | Number of `auto_graduation_items`; `2`                   |
| `auto_graduation_quests+0x04`            | u32[graduation_item_count]                      | auto_graduation_items                | Item IDs; Season Graduation Gift Box and Fughar's Letter of Encouragement on client 3482 |
| `auto_graduation_items+0x00`             | bytes[4]                                        | unknown_auto_graduation_items_00     | Differs between clients; see Open Questions              |
| `auto_graduation_items+0x04`             | String Table                                    | string_table                         | See String Table                                         |
| `EOF-0x08`                               | u32                                             | table_start                          | Offset of the string table                               |
| `EOF-0x04`                               | u32                                             | zero                                 | Always `0`                                               |

### Row (16 bytes)

| Offset  | Type | Field           | Notes                                                                                  |
| ------- | ---- | --------------- | -------------------------------------------------------------------------------------- |
| `+0x00` | u32  | index           | Row number; `54` and `85` appear twice on client 3482                                   |
| `+0x04` | u32  | change_item_key | Conversion item, a packed item key (`8046` [Season] Tuvala Helmet Conversion Stone)     |
| `+0x08` | u32  | before_item_key | Season item the conversion applies to (`694105` Tuvala Helmet); unique per row          |
| `+0x0C` | u32  | after_item_key  | Normal item it turns into (`695105` Tuvala Helmet)                                      |

### Season Challenge (8 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | challenge_key | Challenge key; `2964` and `2965` on clients 1784 to 3482     |
| `+0x02` | u32  | item_id       | Item; `694111` Tuvala Ring and `694110` Tuvala Earring       |
| `+0x06` | u8   | unknown_06    | `5` on both entries; see Open Questions                      |
| `+0x07` | u8   | unknown_07    | `1` on both entries                                          |

### Character Type (2 bytes)

| Offset  | Type | Field      | Notes                         |
| ------- | ---- | ---------- | ----------------------------- |
| `+0x00` | u8   | unknown_00 | `1` and `2`                    |
| `+0x01` | u8   | unknown_01 | `0` on both entries            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

A private server's `DataSheets.bexcel` on client 1784 has the rows in the
`SeasonAutoChangeItem` sheet (`Index`, `ChangeItemKey`, `BeforeItemKey`,
`AfterItemKey`), 63 of 63 rows equal to the file of that client. The
lists come from two sheets of the same workbook:

| Field                           | Sheet and column                                   | Client 1784                                    |
| ------------------------------- | -------------------------------------------------- | ---------------------------------------------- |
| season_challenges               | `SeasonChallenges` `ChallengesKey`                 | `2964, 694111, 5, 1; 2965, 694110, 5, 1;` (the row for service type 12, nations 0 and 1), equal |
| auto_graduation_character_types | `SeasonEtc` `SeasonAutoGraduationCharacterType`    | `1, 0; 2, 0;`, equal                            |
| auto_graduation_quests          | `SeasonEtc` `SeasonAutoGraduationQuest`            | `40041, 2` against `40036/2` in the file        |
| auto_graduation_items           | `SeasonEtc` `SeasonAutoGraduationItem`             | `8089, 8200`, equal                             |

The quest differs (private server values are edited); the column order
places it. `SeasonEtc` also has the graduation mail title, sender and text
(`{TextBind:SEASON_TITLE5}`) and `RunSeasonAutoGraduation`, which the
file does not hold. The sheet names each challenge entry's four numbers as
one `ChallengesKey` cell, so the two u8 stay unnamed.

## Notes

- The 89 rows of client 3482 convert Tuvala gear and accessories to the
  normal Tuvala items, several Season items through one conversion item
  (`8044`, `8045` Tuvala Awakening Weapon Conversion Stone).
- The four lists hold the same values on clients 1784 to 3482, apart
  from the quest (`40036/2` on 1784, `40056/2` on 2107, `40071/2` from
  2519) and the first item (`8089` up to 3251, `890081` Season Graduation
  Gift Box from 3474); the second item is `8200`, `5919` and from 2519
  `8445`.
- Client 1784 has 63 rows in index order; client 3482 adds rows out of
  order (`86, 85, 87` at the end) and repeats indices 54 and 85.
- The handler (`_bss/autoseasonclosechangeitemstaticstatus/`) shows one
  row per conversion with the three items; the lists after the rows are
  read and checked but not shown.

## Open Questions

### What the Season Challenge Bytes and Character Types Are

Each season challenge entry ends with `5` and `1`, which fit an
enhancement level (PEN) and a count of its Tuvala ring or earring; the
character types `1, 0` and `2, 0` may name the Season character kinds
that graduate. Neither is read by a Lua getter of client 3482.

### What the Four Bytes After the Lists Hold

`unknown_auto_graduation_items_00` is `00 00 00 00` on clients 1784, 3002,
3474 and 3482, `01 00 01 00` on 2765 and 3251, `00 00 e5 44` on 2107 and
`00 00 a9 69` on 2519. It matches no `SeasonEtc` column, and as u16 pairs,
a u32 or an f32 none of the values names anything in the other lists.
