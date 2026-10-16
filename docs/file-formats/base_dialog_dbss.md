# `base_dialog.dbss` Format

## Purpose

Stores a short base record for every NPC dialog in `detail_dialog.dbss`: the Korean display name the dialog shows for the character, and a list of short Korean lines. The lines are ambient chatter that the client shows in a speech bubble over the NPC's head (a pilgrim saying `아이고. 배야.` ("Ouch, my stomach.")).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes     | Records            | Row bytes                |
| ------ | -------------- | ------- | ------------------------ | --------- | ------------------ | ------------------------ |
| 1      | 3473 and later | 3473    | `base_dialog.dbss`       | 2,076,194 | 59,782 Base Record | 21 to 519, 35 on average |
| 1      | 3473 and later | 3473    | `base_dialogoffset.dbss` | 717,404   | 59,782 Index Row   | 12                       |

| Layout | File                     | Known               | Unknown           |
| ------ | ------------------------ | ------------------- | ----------------- |
| 1      | `base_dialog.dbss`       | 1,777,284 B (85.6%) | 298,910 B (14.4%) |
| 1      | `base_dialogoffset.dbss` | 717,404 B (100.0%)  | 0 B (0.0%)        |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                               |
| ------------------------ | -------- | -------------------------------------------------- |
| `base_dialogoffset.dbss` | Required | Maps each dialog key to its record offset and size |
| `languagedata_*.loc`     | Optional | The name and lines in the user's language (type `38`), character names (type `6`) |

All multi-byte values are little-endian. The keys are the same 59,776 keys as `detail_dialog.dbss`, in the same order (`dialog_index << 16 | character_id`, see [detail_dialog.dbss](detail_dialog_dbss.md)).

## Layout 1

### File Layout

| Offset  | Type               | Field   | Notes                                      |
| ------- | ------------------ | ------- | ------------------------------------------ |
| `+0x00` | u32                | count   | Number of records; matches the offset file |
| `+0x04` | Base Record[count] | records | Back to back; the first starts at `4`      |

Unlike `detail_dialog.dbss`, records are not preceded by a copy of their key: they tile the file from byte `4` to its end with no gap.

### Base Record (variable: 21 bytes + name and line text)

Each record sits at `offset` and is `size` bytes long, from its index row.

| Offset           | Type               | Field       | Notes                                                        |
| ---------------- | ------------------ | ----------- | ------------------------------------------------------------ |
| `+0x00`          | u32                | key         | Same as the index key                                        |
| `+0x04`          | str16              | name_kr     | Korean display name, e.g. `마티나 핀토`, `순례자` (pilgrim) |
| `name_kr+0x00`   | u32                | line_count  | `0` on 55,850 of 59,776 records, up to `10`                  |
| `name_kr+0x04`   | str16[line_count]  | lines       | Short Korean lines                                           |
| `lines+0x00`     | bytes[5]           | unknown_end | Always zero                                                  |

Every record of client 3458 walks with this layout and ends exactly at its index size.

### `base_dialogoffset.dbss`

The same layout as `detail_dialogoffset.dbss`: `PABR`, a u32 count, 12-byte rows and a 12-byte trailer (an empty PABR string table, the end offset of the rows, `u32 0`).

| Offset              | Type             | Field        | Notes                                    |
| ------------------- | ---------------- | ------------ | ---------------------------------------- |
| `+0x00`             | char[4]          | magic        | `PABR`                                   |
| `+0x04`             | u32              | count        | Number of index rows                     |
| `+0x08`             | Index Row[count] | rows         | See Index Row                            |
| `rows+0x00`         | String Table     | string_table | See String Table                         |
| `string_table+0x00` | u32              | rows_end     | End offset of the rows (`8 + 12 * count`) |
| `string_table+0x04` | u32              | zero         | Always `0`                               |

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                            |
| ------- | ---- | ------ | ------------------------------------------------ |
| `+0x00` | u32  | key    | `dialog_index << 16 \| character_id`             |
| `+0x04` | u32  | offset | Byte offset of the record in `base_dialog.dbss`  |
| `+0x08` | u32  | size   | Record size in bytes                             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes       |
| ------- | ------------------ | ------------ | ----------- |
| `+0x00` | u32                | string_count | Always `0`  |
| `+0x04` | pstr[string_count] | strings      | Empty       |

## Notes

- The name and lines are localized in LOC type `38`: `str_id1 = character_id`, `str_id2 = dialog_index`, `str_id3 = 0`, and `str_id4` `0` for the name and `1`, `2`, ... for the lines in order. In client 3458 all 10,165 lines and 59,686 of the 59,776 names have a row; Martina Finto's first line reads "Oh David... Maybe I should open up a restaurant here at the farm...".
- `name_kr` is the dialog's own name: copies of a generic NPC such as `순례자` (pilgrim) share it, and it may differ from the LOC type `6` name of the character ID.
- The lines are the speech bubbles over the NPC's head, checked in game 2026-09-29: Martina Finto showed "Oh David... Maybe I should open up a restaurant here at the farm..." in a bubble, and a villager beside her "The commander said I was the best!" (character `506`, dialog `210`, line `2`). The bubble is `UI_Data/Actor/UI_Actor_BubbleBox.XML` (`OverheadUIType_BubbleBox`, a `bubble.dds` frame around a 120 px auto-wrapping text box), which is why the lines carry hand-placed `\n` breaks. The Lua only creates the bubble panel pool (`ToClient_InitializeBubbleBoxPanelPool`); the client code picks and sets the text.
- The lines never show in the dialog window: that opens with the `detail_dialog.dbss` greeting (Martina: "It's so lonely here, all by myself... David doesn't seem to know.").
