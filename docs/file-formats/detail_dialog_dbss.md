# `detail_dialog.dbss` Format

## Purpose

Stores the NPC dialog trees: for each character and dialog index, the greeting text and the list of dialog options the player can pick (quest turn-ins, knowledge, exchanges, cutscenes, leases and more). Each option carries a condition script, a Korean title, the NPC's answer text and an action script that the client runs when the option is chosen.

Example (Martina Finto, character `40024`, dialog index `1`):

```text
key 0x00019C58 -> internal name "Martina", 46 options, one of them:
  condition: !iscontentsgroupopen(0,4017);<or>...;clearquest(21125,64);clearquest(21125,74);
  title:     [대여] 작은 울타리            ("[Lease] Small Fence")
  text:      작물을 가꾸시겠다고요? 여기 남는 울타리가 있으니 사용하셔도 좋아요.
  action:    buyItemByPoint(58010,0,1,5,3)   ([CP] Small Fence for 3 CP)
```

## Companion Files

| File                       | Required | Role                                                  |
| -------------------------- | -------- | ----------------------------------------------------- |
| `detail_dialogoffset.dbss` | Required | Maps each dialog key to its record offset and size    |
| `languagedata_*.loc`       | Optional | The dialog text in the user's language (type `39`, see Localization) and character names (type `6`) |

All multi-byte values are little-endian. [base_dialog.dbss](base_dialog_dbss.md) holds the same 59,776 keys in the same order with a short base record each (display name and short lines).

## File Layout

### detail_dialogoffset.dbss

| Offset  | Type | Field   | Notes                                              |
| ------- | ---- | ------- | -------------------------------------------------- |
| `+0x00` | u8[4] | magic  | `PABR`                                             |
| `+0x04` | u32  | count   | Number of index rows; `59776` in client 3458       |
| `+0x08` | ...  | rows    | `count` index rows                                 |
| end     | 12 bytes | trailer | `u32 0`, `u32` end offset of the rows (`8 + 12 * count`), `u32 0` |

#### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                            |
| ------- | ---- | ------ | ------------------------------------------------ |
| `+0x00` | u32  | key    | `dialog_index << 16 \| character_id`             |
| `+0x04` | u32  | offset | Byte offset of the record in `detail_dialog.dbss` |
| `+0x08` | u32  | size   | Record size in bytes                             |

### detail_dialog.dbss

| Offset  | Type | Field   | Notes                                                        |
| ------- | ---- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32  | count   | Number of records; matches the offset file                   |
| `+0x04` | ...  | records | Each record is preceded by a repeated copy of its `u32` key |

The records tile the file: every record starts 4 bytes after the previous one ends (the repeated key), the first at `8`, and the last ends at end of file.

Strings are a `u64` count followed by that many units: UTF-16LE for text and scripts, single-byte ASCII for the two internal names. There is no terminator.

## Record Structure

### Dialog Record (variable, `size` bytes from `offset`)

| Order | Type | Field | Notes |
| ----- | ---- | ----- | ----- |
| 1  | u32 | key | Same as the index key |
| 2  | u16 | text_id | LOC text ID of the greeting and its lines, see Localization; `1` on 3,193 records. Increases with the dialog index inside a character (`1233`, `1235`, `1238`, ...) |
| 3  | u64 + ascii | internal_name | E.g. `Martina`, `IgorBartali1`, `Social_Low_Front_01`; empty on 7,071 records |
| 4  | u64 + ascii | unknown_name_2 | Empty on all but 325 records (`2,0` on 101, `Social_*` names on the rest) |
| 5  | u64 + utf16 | greeting | The NPC's opening line, Korean |
| 6  | u32 | line_count | Extra greeting lines that follow; `0` on all but 136 records |
| 7  | line_count × Greeting Line | lines | |
| 8  | u32 | option_count | `0` on 49,710 records; up to 1,522 (`0x0001AE99`, Dorin Morgrim) |
| 9  | option_count × Option | options | 36,276 options in all |
| 10 | u32 | conditional_count | Conditional greetings that follow; `0` on 55,202 records |
| 11 | conditional_count × Conditional Greeting | conditionals | |
| 12 | u64 | unknown_list_count | `2` on 57,387 records, `0` on 2,389 |
| 13 | u16 × unknown_list_count | unknown_list | `[2, 0]` on 57,383 records |
| 14 | u32 | end | Always `0`; the record ends exactly here |

Every one of the 59,776 records in client 3458 walks with this layout and ends exactly at its index size.

### Greeting Line

| Order | Type | Field | Notes |
| ----- | ---- | ----- | ----- |
| 1 | u8          | contents_type     | The NPC function the line belongs to, a client `CppEnums.ContentsType` value (see Notes); `2` (`Contents_Shop`) on 120 of 197 lines (client 3458), otherwise `3` to `39` |
| 2 | u64 + utf16 | text              | Korean |

### Option

| Order | Type | Field | Notes |
| ----- | ---- | ----- | ----- |
| 1 | u64 + utf16 | condition | Client script that must hold for the option to show, e.g. `!getitemcount(3001,0)>0;`; may be empty |
| 2 | u64 + utf16 | title | Korean option label; many start with a bracketed category such as `[교환]` (exchange) or `[대여]` (lease) |
| 3 | u32         | dialog_button_type  | A client `CppEnums.DialogButtonType` value, `0` to `7`, or `99`; see Notes |
| 4 | u64 + utf16 | text | The NPC's answer, Korean |
| 5 | u64 + utf16 | action | Client script run when the option is picked, e.g. `buyItemByPoint(58010,0,1,5,3)`; may be empty |
| 6 | u16         | text_id | LOC text ID of the title and text, see Localization |

### Conditional Greeting

| Order | Type | Field | Notes |
| ----- | ---- | ----- | ----- |
| 1 | u64 + utf16 | condition | E.g. `clearquest(8541,3);` or `checkclass(20);` |
| 2 | u64 + utf16 | text | Korean |
| 3 | u16         | text_id | LOC text ID of the text, see Localization |

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

## Suggested UI Layout

One row per record:

| Column         | Type | Notes |
| -------------- | ---- | ----- |
| Character ID   | num  | `key & 0xFFFF` |
| Dialog         | num  | `key >> 16` |
| Character      | text | LOC `str_type=6` for the character ID; fallback to `internal_name`, then a dash |
| Greeting       | text | LOC type `39` field `0`, fallback to `greeting`; truncated |
| Functions      | list | `contents_type` of each greeting line as its `ContentsType` name without `Contents_` (`Shop`, `Repair`), each once in line order; a dash without lines |
| Options        | num  | `option_count` |
| Option Types   | list | `dialog_button_type` of each option as its `DialogButtonType` name without `eDialogButton_` (`Normal`, `Exchange`), each once in option order; `99` stays a number |
| Option Titles  | list | LOC type `39` field `2` of each option, fallback to `title`; first few then a count |
| Leases         | list | For each lease option: LOC `str_type=0` name of the item (in its grade colour) and the cost, e.g. `[CP] Small Fence (3 CP)` |

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
