# `base_dialog.dbss` Format

## Purpose

Stores a short base record for every NPC dialog in `detail_dialog.dbss`: the Korean display name the dialog shows for the character, and a list of short Korean lines. The lines are ambient chatter that the client shows in a speech bubble over the NPC's head (a pilgrim saying `아이고. 배야.` ("Ouch, my stomach.")).

Example (Martina Finto, character `40024`, dialog index `1`):

```text
key 0x00019C58 -> name "마티나 핀토" (Martina Finto), 3 lines:
  "다비드.. \n차라리 농장에 음식점을 만들까?"
  "시집오면 손에 물도 \n안 묻히게 해준대 놓고.. "
  "진작에 언니 말을 듣는 건데.. "
```

## Companion Files

| File                     | Required | Role                                               |
| ------------------------ | -------- | -------------------------------------------------- |
| `base_dialogoffset.dbss` | Required | Maps each dialog key to its record offset and size |
| `languagedata_*.loc`     | Optional | The name and lines in the user's language (type `38`), character names (type `6`) |

All multi-byte values are little-endian. The keys are the same 59,776 keys as `detail_dialog.dbss`, in the same order (`dialog_index << 16 | character_id`, see [detail_dialog.dbss](detail_dialog_dbss.md)).

## File Layout

### base_dialogoffset.dbss

The same layout as `detail_dialogoffset.dbss`: `PABR`, a u32 count, 12-byte rows (`u32 key`, `u32 offset`, `u32 size`) and a 12-byte trailer (`u32 0`, the end offset of the rows, `u32 0`).

### base_dialog.dbss

| Offset  | Type | Field   | Notes                                        |
| ------- | ---- | ------- | -------------------------------------------- |
| `+0x00` | u32  | count   | Number of records; matches the offset file   |
| `+0x04` | ...  | records | Back to back; the first starts at `4`        |

Unlike `detail_dialog.dbss`, records are not preceded by a copy of their key: they tile the file from byte `4` to its end with no gap.

## Record Structure

### Base Record (variable, `size` bytes from `offset`)

| Order | Type | Field | Notes |
| ----- | ---- | ----- | ----- |
| 1 | u32 | key | Same as the index key |
| 2 | u64 + utf16 | name_kr | Korean display name, e.g. `마티나 핀토`, `순례자` (pilgrim) |
| 3 | u32 | line_count | `0` on 55,850 of 59,776 records, up to `10` |
| 4 | line_count × (u64 + utf16) | lines | Short Korean lines |
| 5 | u8[5] | unknown_end | Always zero |

Every record of client 3458 walks with this layout and ends exactly at its index size.

## Notes

- The name and lines are localized in LOC type `38`: `str_id1 = character_id`, `str_id2 = dialog_index`, `str_id3 = 0`, and `str_id4` `0` for the name and `1`, `2`, ... for the lines in order. In client 3458 all 10,165 lines and 59,686 of the 59,776 names have a row; Martina Finto's first line reads "Oh David... Maybe I should open up a restaurant here at the farm...".
- `name_kr` is the dialog's own name: copies of a generic NPC such as `순례자` (pilgrim) share it, and it may differ from the LOC type `6` name of the character ID.
- The lines are the speech bubbles over the NPC's head, checked in game 2026-09-29: Martina Finto showed "Oh David... Maybe I should open up a restaurant here at the farm..." in a bubble, and a villager beside her "The commander said I was the best!" (character `506`, dialog `210`, line `2`). The bubble is `UI_Data/Actor/UI_Actor_BubbleBox.XML` (`OverheadUIType_BubbleBox`, a `bubble.dds` frame around a 120 px auto-wrapping text box), which is why the lines carry hand-placed `\n` breaks. The Lua only creates the bubble panel pool (`ToClient_InitializeBubbleBoxPanelPool`); the client code picks and sets the text.
- The lines never show in the dialog window: that opens with the `detail_dialog.dbss` greeting (Martina: "It's so lonely here, all by myself... David doesn't seem to know.").
