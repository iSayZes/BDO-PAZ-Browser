# `intimacyinfo.bss` Format

## Purpose

The amity list of the NPC dialog window: per NPC character the entries it
unlocks at an amity value, each a quest, a shop, a knowledge or a talk. The
dialog Lua (`panel_dialog_intimacy_all_1.luac`) reads them through
`getIntimacyInformationCount(characterKey)` and
`getIntimacyInformation(characterKey, index)` and the getters
`getIntimacy()`, `getTypeIndex()`, `getOperatorType()`, `getQuestNo()`,
`getMentalCardKeyRaw()` and `getDialogIndex()`, and shows each entry as
`<type name> : <description> (<operator> <amity>)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes  | Records           | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------ | ----------------- | --------- |
| 1      | 1230 and later | 3482    | `intimacyinfo.bss` | 22,028 | 765 Info, 353 Row | 26        |

| Layout | File               | Known            | Unknown         |
| ------ | ------------------ | ---------------- | --------------- |
| 1      | `intimacyinfo.bss` | 18,968 B (86.1%) | 3,060 B (13.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2765   | Layout 1             |
| 2519   | Layout 1             |
| 2313   | Layout 1             |
| 2107   | Layout 1             |
| 1937   | Layout 1             |
| 1784   | Layout 1             |
| 1636   | Layout 1             |
| 1485   | Layout 1             |
| 1348   | Layout 1             |
| 1230   | Layout 1             |
| 1058   | No file              |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                              |
| ---------------------------- | -------- | --------------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so an NPC key without a row shows as plain text   |
| `languagedata_en.loc`        | Optional | NPC names (type 6), quest titles (type 18), knowledge names (type 34) and dialog names (type 38) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of NPCs                                |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 6 bytes + entries)

| Offset  | Type             | Field         | Notes                                                                           |
| ------- | ---------------- | ------------- | ------------------------------------------------------------------------------- |
| `+0x00` | u16              | character_key | NPC character key (LOC type 6); the rows are in ascending key order, `507` first on client 3482 |
| `+0x02` | u32              | info_count    | Number of `infos`; `1` to `5` on 350 of 353 rows of client 3482, `78` at most  |
| `+0x06` | Info[info_count] | infos         | See Info                                                                        |

### Info (variable: 24 bytes + quest group or dialog index)

| Offset             | Type                   | Field               | Notes                                                                                   |
| ------------------ | ---------------------- | ------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`            | u16                    | character_key       | Equals the row's `character_key` on every entry                                         |
| `+0x02`            | i32                    | intimacy            | Amity value the entry compares against, `0` to `2000` on client 3482; the window shows it out of 1,000 |
| `+0x06`            | u32                    | type_index          | `CppEnums.IntimacyInformationTypeInfo`; see Type Index                                  |
| `+0x0A`            | u32                    | operator_type       | `CppEnums.DlgCommonConditionOperatorType`: `0` Equal, `1` Large (▲), `2` Small (▼)      |
| `+0x0E`            | u32                    | knowledge_key       | `mentalcard.dbss` knowledge key on type `3` (Knowledge), `0` on the others              |
| `+0x12`            | u16 if type_index = 0  | quest_group         | Quest group of the quest (`getQuestNo()._group`)                                        |
| `quest_group+0x00` | u16 if type_index != 0 | dialog_index        | The NPC's dialog index on types `3` and `4` (`getDialogIndex()`), `0` on type `1`       |
| `dialog_index+0x00` | u16                   | quest_id            | Quest number in its group on type `0`; `0` on the others                                |
| `dialog_index+0x02` | u32                   | unknown_quest_id_02 | `0` on type `0`; see Open Questions                                                     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Type Index

`CppEnums.IntimacyInformationTypeInfo` of the client 3482 Lua
(`global_define_cpp_enum.luac`). Entries on client 3482 in the last column.

| Value | Name      | What the entry links             | Entries (client 3482) |
| ----- | --------- | -------------------------------- | --------------------- |
| 0     | Quest     | `quest_group`, `quest_id`        | 145                   |
| 1     | Shop      | Nothing; `unknown_quest_id_02`   | 175                   |
| 2     | Buff      |                                  | 0                     |
| 3     | Knowledge | `knowledge_key`, `dialog_index`  | 363                   |
| 4     | Talk      | `dialog_index`                   | 82                    |
| 5     | Item      |                                  | 0                     |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
these rows; `DataSheet_IntimacyDataTable.xlsm` holds the NPC to NPC amity
table instead. The 2016 `gc::IntimacyInformation` holds `_characterKey`,
`_intimacy`, `_typeIndex` (`gc::IntimacyInformationTypeInfo`),
`_operatorType` (`gc::DlgCommonCondition::OperatorType`), `_typeDescription`
and a condition list pointer, in that order. The names after
`operator_type` follow the client 3482 Lua getters and the data:

| Field          | Evidence (client 3482)                                                                 |
| -------------- | -------------------------------------------------------------------------------------- |
| knowledge_key  | 363 of 363 type `3` entries have a LOC type 34 knowledge name (`3001` Velia)           |
| quest_group, quest_id | 145 of 145 type `0` entries have a LOC type 18 quest title                      |
| dialog_index   | 445 of 445 type `3` and `4` entries name a dialog with a LOC type 38 dialog name, keyed `(character_key, dialog_index)`; the Lua skips a knowledge entry whose `getDialogIndex()` is not the open dialog's |

## Notes

- Every entry of client 3482 has `knowledge_key` `0` unless its type is
  `3`, and `quest_id` `0` unless its type is `0`.
- The window marks a knowledge entry as learned or not from
  `ToClinet_getMentalCardStaticStatus(getMentalCardKeyRaw()):isHasCard()`
  (the Lua spells the function `ToClinet`).
- The `CppEnums.IntimacyInformationTypeInfo` values `2` (Buff) and `5`
  (Item) have no entry on client 3482.

## Open Questions

### What the Last Field Holds

`unknown_quest_id_02` is `0` on every quest entry. On shop entries it is
`0`, `1`, `2`, `3` or `0xFFFFFFFF` (3, 61, 46, 31 and 34 entries on client
3482), on knowledge entries `0` to `281` and rising within an NPC (Igor
Bartali `162` to `166`), on talk entries `0` to `75`. The 2016 struct stored a
`_typeDescription` string here; the window's description text
(`getTypeDescription()`) may come from a string this value selects, but no
LOC type keyed by NPC and this value holds it on client 3482.
