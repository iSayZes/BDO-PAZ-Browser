# `npcgiftdata.dbss` Format

## Purpose

The NPC's reply to a confession (the Confess button of the gift window): one
variable-length record per NPC with the Korean text. The NPC IDs are the same
24 as in [`npcgift.dbss`](npcgift_dbss.md), which holds the accepted gift
items. LOC type 54 has the reply in the user's language, keyed by `npc_id`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records            | Row bytes                 |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------------ | ------------------------- |
| 1      | 1485 and later | 3474    | `npcgiftdata.dbss`       | 6,702 | 24 Dialogue Record | 32 to 462, 279 on average |
| 1      | 1485 and later | 3474    | `npcgiftdataoffset.dbss` | 244   | 24 Offset Record   | 10                        |

| Layout | File                     | Known           | Unknown      |
| ------ | ------------------------ | --------------- | ------------ |
| 1      | `npcgiftdata.dbss`       | 6,510 B (97.1%) | 192 B (2.9%) |
| 1      | `npcgiftdataoffset.dbss` | 196 B (80.3%)   | 48 B (19.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                       |
| --------------------- | -------- | ------------------------------------------ |
| `languagedata_en.loc` | Optional | NPC names (6), confession replies (54)     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                   | Field   | Notes                                     |
| ------- | ---------------------- | ------- | ----------------------------------------- |
| `+0x00` | u32                    | count   | Number of dialogue records (observed: 24) |
| `+0x04` | Dialogue Record[count] | records | See Dialogue Record                       |

### Dialogue Record (variable: 18 bytes + text)

| Offset      | Type   | Field           | Notes                                                                                                                        |
| ----------- | ------ | --------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `+0x00`     | u16    | npc_id          | NPC key                                                                                                                      |
| `+0x02`     | u32    | unknown_02      | Observed: 70 for 23 records, 35 for NPC 43408. Not the LOC type.                                                             |
| `+0x06`     | str16  | text            | Korean confession reply; the count is the number of visible UTF-16 code units                                                |
| `text+0x00` | u16[2] | unknown_tail_00 | Two trailing code units after `text`; observed values include `00 00 00 00`, `FF FF FF FF`, `00 00 41 DF`, and `00 00 3D E6` |

### `npcgiftdataoffset.dbss`

The 10-byte offset record layout of
[`npcgiftoffset.dbss`](npcgift_dbss.md#npcgiftoffsetdbss), but offsets point
into `npcgiftdata.dbss`. The `data_size` equals `12 + 2 x` the `text` count `+ 4`,
excluding the leading `npc_id`.

| Offset  | Type                 | Field   | Notes                                     |
| ------- | -------------------- | ------- | ----------------------------------------- |
| `+0x00` | u32                  | count   | Number of dialogue records (observed: 24) |
| `+0x04` | Offset Record[count] | records | See Offset Record                         |

### Offset Record (10 bytes)

| Offset  | Type | Field       | Notes                                                                     |
| ------- | ---- | ----------- | ------------------------------------------------------------------------- |
| `+0x00` | u16  | npc_id      | NPC key; matches the record's leading `npc_id`                            |
| `+0x02` | u32  | data_offset | Byte offset into `npcgiftdata.dbss`; points 2 bytes past the record start |
| `+0x06` | u16  | data_size   | Byte count after the leading `npc_id`                                     |
| `+0x08` | u16  | unknown_08  | Observed: 0                                                               |

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

The two trailing UTF-16 code units after dialogue text (`unknown_tail_00`) carry values including `FF FF FF FF` and non-zero pairs; their purpose is unknown.

## In-Game Checks

### Confession Amity for `unknown_02`

Needs NPC (all):

- [Luwensley](https://bdocodex.com/us/npc/43408/)
- [Crio](https://bdocodex.com/us/npc/40012/)

`unknown_02` is 70 for 23 records and 35 for Luwensley (43408); earlier versions of this doc called it `unknown_param`. The gift window and dialog Lua read the reply text but have no getter for this value. Note the lowest Amity at which the Confess button works for each NPC, and the Amity change after the confession. If Luwensley accepts a confession from about half the Amity Crio needs, or the change after it is half as large, `unknown_02` is an Amity value for the confession; the same numbers for both NPCs rule that out.
