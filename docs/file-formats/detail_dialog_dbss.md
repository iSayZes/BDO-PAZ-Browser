# `detail_dialog.dbss` Format

## Purpose

Stores the NPC dialog trees: for each character and dialog index, the greeting text and the list of dialog options the player can pick (quest turn-ins, knowledge, exchanges, cutscenes, leases and more). Each option carries a condition script, a Korean title, the NPC's answer text and an action script that the client runs when the option is chosen.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes      | Records                                                                                            | Row bytes                     |
| ------ | -------------- | ------- | -------------------------- | ---------- | -------------------------------------------------------------------------------------------------- | ----------------------------- |
| 1      | 1784 and later | 3474    | `detail_dialog.dbss`       | 28,282,772 | 35,766 Option, 59,782 Dialog Record, 59,782 Record, 12,774 Conditional Greeting, 197 Greeting Line | 56 to 603,491, 469 on average |
| 1      | 1784 and later | 3474    | `detail_dialogoffset.dbss` | 717,404    | 59,782 Index Row                                                                                   | 12                            |

| Layout | File                       | Known                | Unknown            |
| ------ | -------------------------- | -------------------- | ------------------ |
| 1      | `detail_dialog.dbss`       | 26,852,567 B (94.9%) | 1,430,205 B (5.1%) |
| 1      | `detail_dialogoffset.dbss` | 717,404 B (100.0%)   | 0 B (0.0%)         |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                  |
| -------------------------- | -------- | ----------------------------------------------------- |
| `detail_dialogoffset.dbss` | Required | Maps each dialog key to its record offset and size    |
| `languagedata_*.loc`       | Optional | The dialog text in the user's language (type `39`, see Localization) and character names (type `6`) |

All multi-byte values are little-endian. [base_dialog.dbss](base_dialog_dbss.md) holds the same 59,776 keys in the same order with a short base record each (display name and short lines).

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                                        |
| ------- | ------------- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32           | count   | Number of records; matches the offset file                   |
| `+0x04` | Record[count] | records | Each record is preceded by a repeated copy of its `u32` key; see Record |

The records tile the file: every record starts 4 bytes after the previous one ends (the repeated key), the first at `8`, and the last ends at end of file.

Strings are a `u64` count followed by that many units: UTF-16LE for text and scripts, single-byte ASCII for the two internal names. There is no terminator.

### Record (variable: 4 bytes + dialog record)

| Offset  | Type          | Field      | Notes                                                       |
| ------- | ------------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32           | key_prefix | Repeated copy of the record's `key`                         |
| `+0x04` | Dialog Record | dialog     | `size` bytes; the index row's `offset` points at this field |

### Dialog Record (variable: 54 bytes + text and lists)

| Offset                | Type                                    | Field              | Notes |
| --------------------- | --------------------------------------- | ------------------ | ----- |
| `+0x00`               | u32                                     | key                | Same as the index key |
| `+0x04`               | u16                                     | text_id            | LOC text ID of the greeting and its lines, see Localization; `1` on 3,193 records. Increases with the dialog index inside a character (`1233`, `1235`, `1238`, ...) |
| `+0x06`               | str8                                    | internal_name      | E.g. `Martina`, `IgorBartali1`, `Social_Low_Front_01`; empty on 7,071 records |
| `internal_name+0x00`  | str8                                    | unknown_name_2     | Empty on all but 325 records (`2,0` on 101, `Social_*` names on the rest) |
| `unknown_name_2+0x00` | str16                                   | greeting           | The NPC's opening line, Korean |
| `greeting+0x00`       | u32                                     | line_count         | Extra greeting lines that follow; `0` on all but 136 records |
| `greeting+0x04`       | Greeting Line[line_count]               | lines              | See Greeting Line |
| `lines+0x00`          | u32                                     | option_count       | `0` on 49,710 records; up to 1,522 (`0x0001AE99`, Dorin Morgrim) |
| `lines+0x04`          | Option[option_count]                    | options            | 36,276 options in all |
| `options+0x00`        | u32                                     | conditional_count  | Conditional greetings that follow; `0` on 55,202 records |
| `options+0x04`        | Conditional Greeting[conditional_count] | conditionals       | See Conditional Greeting |
| `conditionals+0x00`   | u64                                     | unknown_list_count | `2` on 57,387 records, `0` on 2,389 |
| `conditionals+0x08`   | u16[unknown_list_count]                 | unknown_list       | `[2, 0]` on 57,383 records |
| `unknown_list+0x00`   | u32                                     | unknown_end        | Always `0`; the record ends exactly here |

Every one of the 59,776 records in client 3458 walks with this layout and ends exactly at its index size.

### Greeting Line (variable: 9 bytes + text)

| Offset  | Type  | Field         | Notes |
| ------- | ----- | ------------- | ----- |
| `+0x00` | u8    | contents_type | The NPC function the line belongs to, a client `CppEnums.ContentsType` value (see Notes); `2` (`Contents_Shop`) on 120 of 197 lines (client 3458), otherwise `3` to `39` |
| `+0x01` | str16 | text          | Korean |

### Option (variable: 38 bytes + text)

| Offset           | Type  | Field              | Notes |
| ---------------- | ----- | ------------------ | ----- |
| `+0x00`          | str16 | condition          | Client script that must hold for the option to show, e.g. `!getitemcount(3001,0)>0;`; may be empty |
| `condition+0x00` | str16 | title              | Korean option label; many start with a bracketed category such as `[교환]` (exchange) or `[대여]` (lease) |
| `title+0x00`     | u32   | dialog_button_type | A client `CppEnums.DialogButtonType` value, `0` to `7`, or `99`; see Notes |
| `title+0x04`     | str16 | text               | The NPC's answer, Korean |
| `text+0x00`      | str16 | action             | Client script run when the option is picked, e.g. `buyItemByPoint(58010,0,1,5,3)`; may be empty |
| `action+0x00`    | u16   | text_id            | LOC text ID of the title and text, see Localization |

### Conditional Greeting (variable: 18 bytes + text)

| Offset           | Type  | Field     | Notes |
| ---------------- | ----- | --------- | ----- |
| `+0x00`          | str16 | condition | E.g. `clearquest(8541,3);` or `checkclass(20);` |
| `condition+0x00` | str16 | text      | Korean |
| `text+0x00`      | u16   | text_id   | LOC text ID of the text, see Localization |

### `detail_dialogoffset.dbss`

| Offset              | Type             | Field        | Notes                                        |
| ------------------- | ---------------- | ------------ | -------------------------------------------- |
| `+0x00`             | char[4]          | magic        | `PABR`                                       |
| `+0x04`             | u32              | count        | Number of index rows; `59776` in client 3458 |
| `+0x08`             | Index Row[count] | rows         | See Index Row                                |
| `rows+0x00`         | String Table     | string_table | See String Table                             |
| `string_table+0x00` | u32              | rows_end     | End offset of the rows (`8 + 12 * count`)    |
| `string_table+0x04` | u32              | zero         | Always `0`                                   |

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                             |
| ------- | ---- | ------ | ------------------------------------------------- |
| `+0x00` | u32  | key    | `dialog_index << 16 \| character_id`              |
| `+0x04` | u32  | offset | Byte offset of the record in `detail_dialog.dbss` |
| `+0x08` | u32  | size   | Record size in bytes                              |

### String Table (variable: 4 bytes + strings)

The 12-byte trailer of the offset file is an empty PABR string table, the end offset of the rows and `zero`.

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Localization

The Korean strings are localized in LOC type `39`, keyed by the record's `key`, a `text_id` and a field (`str_id1 = key`, `str_id2 = text_id`, `str_id3 = 0`, `str_id4 = field`):

| Field | String | Coverage in client 3458 |
| ----: | ------ | ----------------------- |
| `0` | `greeting`, with the record's `text_id` | 59,680 of 59,770 non-empty greetings |
| `1` | The greeting lines, with the record's `text_id`, packed in one string as `function>text;` per line, e.g. `shop>Excellent choice!;` | Records with lines |
| `2` | Option `title`, with the option's `text_id` | 36,117 of 36,276 options |
| `3` | Option `text`, with the option's `text_id` | 36,112 of 36,276 options |
| `4` | Conditional greeting `text`, with its `text_id` | 12,796 of 12,796 |

For Martina Finto (`0x00019C58`), field `0` of text ID `689` reads "It's so lonely here, all by myself... David doesn't...", and option text ID `42` field `2` reads `[Rent] Small Fence`. The function names of field `1` (`shop`, `repair`, `extract`, `weakenItem`, `talk`, `exchange`) name what `contents_type` picks: `2` `shop`, `4` `repair`, `19` `extract`, `33` `weakenItem`, `38` `talk`, `39` `exchange` and the others in Notes.

## Lease Options

A lease is an option whose `action` is `buyItemByPoint(item, 0, 1, 5, cost)`: the item key, `0`, `1`, `5` and the contribution point cost. Client 3458 has 184 lease options on 63 characters, all with `dialog_button_type` `0` (Normal) and titled `[대여] <item>` ("[Lease]"). `npcsimply.bss` repeats the first lease option of 58 of these characters (`lease_item_id`, `lease_cost`, `has_lease_condition`); the file lists all of them, such as the 84 Nesser gear leases of Sahazad Nesser (`45006`), the 25 Kaia weapons of Kanobas (`42152`) and the Small Fence of Wale (`40605`), who has no lease in `npcsimply.bss`. See `npcsimply_bss.md` for the cost check in game.

## Notes

- The key's low 16 bits are a character ID: 49,252 of the 59,776 records resolve to a LOC type `6` name, and 10,153 of the other 10,524 are shared social dialogs (`Social_Low_Front_01` and similar), many on low IDs such as `817` to `864`. The high 16 bits number the dialogs of one character from `0` up; the main NPC dialog is usually index `1` (`0x00019C58` Martina Finto, `0x00019C51` Igor Bartali). 3,788 of 4,569 characters have one record.
- The main dialog's `internal_name` is often the NPC's name plus a digit (`IgorBartali1`, `OttavioFerre1`).
- A greeting can be the tag `{GetRandomText(<name>)}`, which picks a line from the pool of that name in [dialogtext.dbss](dialogtext_dbss.md), e.g. `{GetRandomText(PEDU_47759_1)}`.
- `dialog_button_type` is the client's `CppEnums.DialogButtonType` (`global_define_cpp_enum.luac`), listed in order from `0`: `eDialogButton_Normal`, `_Knowledge`, `_Function`, `_CutScene`, `_Exchange`, `_ExceptExchange`, `_TimeAttack`, `_Sequence`, `_Count`. The data fits that order by the title prefixes and actions: `1` knowledge (지식, `pushknowledge`), `3` cutscenes and videos (회상, 이야기, `showCutScene`, `showVideo`), `4` and `5` exchanges (교환, `ExchangeItem...`), `6` time-limited quests (시간 제한, `resettimeattackquest`) and `7` sequences (`playsequence`). `0` (Normal, 21,252 options on client 3458) and `2` (Function, 4,185) mix quest turn-ins, returns and leases; `99` (options with an empty action) is not in the enum. The dialog list Lua (`panel_dialog_list_all_1.luac`) reads it as `_dialogButtonType`: it starts the cutscene for `eDialogButton_CutScene` and the sequence state for `eDialogButton_Sequence`, and `panel_dialog_exchangelist_all_2.luac` checks `eDialogButton_Exchange` and `eDialogButton_ExceptExchange` for the exchange list.
- `contents_type` is the client's `CppEnums.ContentsType`, listed in order from `0` (`Contents_Quest`, `Contents_NewQuest`, `Contents_Shop`, `Contents_Skill`, `Contents_Repair`, `Contents_Auction`, `Contents_Inn`, `Contents_Warehouse`, `Contents_IntimacyGame`, `Contents_Stable`, `Contents_Transfer`, ...). The values match the function names in LOC type `39` field `1` on 135 of the 136 records with lines (client 3458): `2` `shop`, `3` `skill`, `4` `repair`, `5` `auction`, `6` `inn`, `7` `warehouse`, `9` `stable`, `10` `transfer`, `19` `extract` (`Contents_Extract`), `33` `weakenItem` (`Contents_WeakenEnchant`), `38` `talk` and `39` `exchange`. The exception is Ambrosia (`0x0001A075`, character `41077`, the `<Stable Keeper>` in Glish), which stores `9` where LOC says `shop`. The stored value is right: in game she has Repair, Stable and Conversation buttons and no Shop, and her line's camera tag is `Ambrosia_Stable_Camera_01`, so the LOC function word is the error. The LOC string does not keep the record's line order: `0x0001B7B1` stores `39, 38, 33, 4, 2, 19` and LOC lists `shop`, `repair`, `extract`, `weakenItem`, `talk`, `exchange`.
- The whole file walks in about 0.5 s after decompression. The `CHARACTER_LEASES` lookup index (see `docs/handler.md`) collects every lease option per character from it for the `npcsimply.bss` Leases column.

## Open Questions

### What are `unknown_name_2` and `unknown_list`?

`unknown_name_2` is empty on all but 325 records; `unknown_list` is `[2, 0]` on almost every record. Neither has a visible counterpart yet.
