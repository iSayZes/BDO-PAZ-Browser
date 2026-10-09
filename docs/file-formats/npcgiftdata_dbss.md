# `npcgiftdata.dbss` Format

## Purpose

The NPC's reply to a confession (the Confess button of the gift window): one
variable-length record per NPC with the Korean text. The NPC IDs are the same
24 as in [`npcgift.dbss`](npcgift_dbss.md), which holds the accepted gift
items. LOC type 54 has the reply in the user's language, keyed by `npc_id`.

Example:

```text
NPC 40012 Crio
  Korean   고맙다, 끽.
  LOC 54   Thanks. Queek!
```

## Companion Files

| File                  | Required | Role                                       |
| --------------------- | -------- | ------------------------------------------ |
| `languagedata_en.loc` | Optional | NPC names (6), confession replies (54)     |

All multi-byte values are little-endian.

## File Layout

### npcgiftdata.dbss

#### Header (4 bytes)

| Offset  | Type | Field | Notes                                     |
| ------- | ---- | ----- | ----------------------------------------- |
| `+0x00` | u32  | count | Number of dialogue records (observed: 24) |

#### Dialogue Record (variable length)

| Offset  | Type              | Field         | Notes                                                                                                                        |
| ------- | ----------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `+0x00` | u16               | npc_id        | NPC key                                                                                                                      |
| `+0x02` | u32               | unknown_02    | Observed: 70 for 23 records, 35 for NPC 43408. Not the LOC type.                                                             |
| `+0x06` | u32               | text_len      | Number of visible UTF-16 code units in `text`                                                                                |
| `+0x0A` | u32               | zero          | Observed: 0                                                                                                                  |
| `+0x0E` | utf16le[text_len] | text          | Korean confession reply                                                                                                      |
| varies  | u16[2]            | tail          | Two trailing code units after `text`; observed values include `00 00 00 00`, `FF FF FF FF`, `00 00 41 DF`, and `00 00 3D E6` |

### npcgiftdataoffset.dbss

Same 4-byte header and 10-byte offset record layout as
[`npcgiftoffset.dbss`](npcgift_dbss.md#npcgiftoffsetdbss), but offsets point
into `npcgiftdata.dbss`. The `data_size` equals `12 + text_len * 2 + 4`,
excluding the leading `npc_id`.

## Suggested UI Layout

| Column   | Type | Notes                                                                  |
| -------- | ---- | ---------------------------------------------------------------------- |
| NPC ID   | num  | `npc_id`                                                               |
| NPC Name | text | LOC str_type=6, str_id1=npc_id                                         |
| Dialogue | text | LOC str_type=54 when available; Korean inline text as fallback         |

## Notes

- `npcgift.dbss` and `npcgiftdata.dbss` share the same 24 NPC IDs and offset
  record order.
- The gift window Lua (`panel_dialog_npcgift_all_1`, `_2`) wires
  `btn_confession` to `HandleEventLUp_DialogNpcGift_All_Propose`, which calls
  `ToClient_proposeToNpc`; on `FromClient_SuccessProposeToNpc` it shows
  `LUA_SUCCESS_PROPOSETONPC`, and `panel_dialog_main_all_2` puts the reply in
  the dialog through `ToClient_getNpcProposeTalk`.
- Every reply answers a confession ("I am confused and shocked by your
  confession", Brego Williar).

## Open Questions

### Dialogue Tail Bytes

The two trailing UTF-16 code units after dialogue text (`tail`) carry values including `FF FF FF FF` and non-zero pairs; their purpose is unknown.

## In-Game Checks

### Confession Amity for `unknown_02`

Needs NPC (all):

- [Luwensley](https://bdocodex.com/us/npc/43408/)
- [Crio](https://bdocodex.com/us/npc/40012/)

`unknown_02` is 70 for 23 records and 35 for Luwensley (43408); earlier versions of this doc called it `unknown_param`. The gift window and dialog Lua read the reply text but have no getter for this value. Note the lowest Amity at which the Confess button works for each NPC, and the Amity change after the confession. If Luwensley accepts a confession from about half the Amity Crio needs, or the change after it is half as large, `unknown_02` is an Amity value for the confession; the same numbers for both NPCs rule that out.
