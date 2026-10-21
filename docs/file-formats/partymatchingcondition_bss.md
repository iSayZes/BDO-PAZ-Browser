# `partymatchingcondition.bss` Format

## Purpose

The minimum AP and DP of Atoraxxion party matching, per Atoraxxion
instance field. Two lists of the same entry shape: the first holds the
normal-difficulty fields of Vahmalkea, Sycrakea, Yolunakea and Orzekea
(`151`, `153`, `155`, `157`) on client 3474, the second the first three of
them with the same values.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records     | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ----------- | --------- |
| 1      | 2107 and later | 3474    | `partymatchingcondition.bss` | 94    | 7 Condition | 10        |

| Layout | File                         | Known        | Unknown    |
| ------ | ---------------------------- | ------------ | ---------- |
| 1      | `partymatchingcondition.bss` | 90 B (95.7%) | 4 B (4.3%) |

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
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone; the instance field names come from
the `instancefield.dbss` lookup index the app loads at start.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                       | Type                                   | Field                    | Notes                                                       |
| ---------------------------- | -------------------------------------- | ------------------------ | ----------------------------------------------------------- |
| `+0x00`                      | char[4]                                | magic                    | ASCII `PABR`                                                |
| `+0x04`                      | u32                                    | matching_condition_count | Number of `matching_conditions`                             |
| `+0x08`                      | Condition[matching_condition_count]    | matching_conditions      | See Condition; 4 entries on client 3474                     |
| `matching_conditions+0x00`   | u32                                    | unknown_condition_count  | Number of `unknown_conditions`                              |
| `matching_conditions+0x04`   | Condition[unknown_condition_count]     | unknown_conditions       | See Condition; 3 entries on client 3474; see Open Questions |
| `unknown_conditions+0x00`    | String Table                           | string_table             | See String Table                                            |
| `string_table+0x00`          | u32                                    | table_start              | Offset of the string table, where `unknown_conditions` ends |
| `string_table+0x04`          | u32                                    | zero                     | Always `0`                                                  |

### Condition (10 bytes)

| Offset  | Type | Field              | Notes                                                                        |
| ------- | ---- | ------------------ | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | instance_field_key | `instancefield.dbss` key: `151` `Atoraxion_Desert_EZ`, `153` `Atoraxion_SEA_EZ`, `155` `Atoraxion_Jungle_EZ`, `157` `Atoraxion_Thorn_EZ` |
| `+0x02` | u32  | min_ap             | Minimum AP; `220`, `300` for `157` (client 3474)                             |
| `+0x06` | u32  | min_dp             | Minimum DP; `270`, `380` for `157` (client 3474)                             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 covers
the file, which client 1784 does not ship. `instance_field_key` follows
`instancefield.dbss`: the four keys are the odd keys of the Atoraxxion
fields `150` to `157`, the `_EZ` ones, and the party matching window
(`panel_partycontentsrecurit.luac`) offers the same four Atoraxxion kinds
(`__ePartyContentsType_AtoraxionDesert`, `...Sea`, `...Velly`,
`...Thorn`). `min_ap` and `min_dp` follow the RESOURCE sheet text of the
window on client 3474 (LOC type 37, hash `4156161109`): "At least 220 AP
and 270 DP is required to use (normal) Atoraxxion Party Matching. However,
at least 300 AP and 380 DP is required for Orzekea."

## Notes

- Clients 2107 and 2519 store 3 entries in each list (84 bytes); from
  client 3002 the first list has `157` too (94 bytes). Client 1784 does not
  ship the file.
- The window also checks character level 60 in Lua
  (`LUA_ATORAXXION_MATCHING_CONDITION_LV`), which the file does not store.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`:
  each entry as the field key, its internal name and `AP / DP`.
  `test_pvp_tables.py` checks that every key is an Atoraxxion field.

## Open Questions

### Second List

What `unknown_conditions` is for. It holds the same entries as
`matching_conditions` without Orzekea (`157`) on every client from 3002;
on clients 2107 and 2519 the two lists are the same. No Lua reads either
list by a name.
