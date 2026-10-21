# `displayexchangeitemnpc.dbss` Format

## Purpose

The item exchanges an NPC dialog lists in its exchange window: each row
names an NPC and one of its dialogs, and lists the `itemexchangebynpc.dbss`
keys (need item and count, result item and count) the window shows.
`displayexchangeitemnpcoffset.dbss` is the index into it, keyed by
`dialog_index << 16 | npc_character_key`, the same key
[`detail_dialog.dbss`](detail_dialog_dbss.md) uses for the dialog.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes | Records        | Row bytes               |
| ------ | -------------- | ------- | ----------------------------------- | ----- | -------------- | ----------------------- |
| 1      | 1784 and later | 3474    | `displayexchangeitemnpc.dbss`       | 2,944 | 124 Row        | 18 to 60, 24 on average |
| 1      | 1784 and later | 3474    | `displayexchangeitemnpcoffset.dbss` | 1,492 | 124 Offset Row | 12                      |

| Layout | File                                | Known            | Unknown    |
| ------ | ----------------------------------- | ---------------- | ---------- |
| 1      | `displayexchangeitemnpc.dbss`       | 2,944 B (100.0%) | 0 B (0.0%) |
| 1      | `displayexchangeitemnpcoffset.dbss` | 1,492 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                                | Required | Role                                                     |
| ----------------------------------- | -------- | -------------------------------------------------------- |
| `displayexchangeitemnpcoffset.dbss` | Optional | `dialog_key -> (data_offset, data_size)` index; the rows carry their own counts and can be walked without it |
| `characterstaticoffset.dbss`        | Optional | Every `characterstatic.dbss` key, so an NPC key without a row shows as plain text instead of a link |
| [`itemexchangebynpc.dbss`](itemexchangebynpc_dbss.md) | Optional | The need and result item and count of each listed key |
| `languagedata_en.loc`               | Optional | NPC name (type `6`) and the name the NPC shows in the dialog (type `38`, keyed `npc_character_key`, `dialog_index`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `124` on client 3474         |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 16 bytes + exchange keys)

| Offset                    | Type                     | Field                 | Notes                                                        |
| ------------------------- | ------------------------ | --------------------- | ------------------------------------------------------------ |
| `+0x00`                   | u16                      | npc_character_key     | NPC, a `characterstatic.dbss` key                            |
| `+0x02`                   | u16                      | dialog_index          | The NPC's dialog; with `npc_character_key` the `detail_dialog.dbss` key `dialog_index << 16 \| npc_character_key`, unique per row |
| `+0x04`                   | u64                      | item_exchange_count   | Number of `item_exchange_keys`; `1` to `22`, never `0` (client 3474) |
| `+0x0C`                   | u16[item_exchange_count] | item_exchange_keys    | `itemexchangebynpc.dbss` keys in window order, not sorted    |
| `item_exchange_keys+0x00` | u16                      | npc_character_key_dup | Equal to `npc_character_key` in every row                    |
| `item_exchange_keys+0x02` | u16                      | dialog_index_dup      | Equal to `dialog_index` in every row                         |

The rows are not sorted by key.

### `displayexchangeitemnpcoffset.dbss`

| Offset  | Type              | Field | Notes                                           |
| ------- | ----------------- | ----- | ----------------------------------------------- |
| `+0x00` | u32               | count | Equals the `displayexchangeitemnpc.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row            |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                      |
| ------- | ---- | ----------- | ---------------------------------------------------------- |
| `+0x00` | u32  | dialog_key  | `dialog_index << 16 \| npc_character_key` of the row       |
| `+0x04` | u32  | data_offset | Row start + 4, at `item_exchange_count`                    |
| `+0x08` | u32  | data_size   | Row size - 4: `16 + 2 * item_exchange_count - 4`           |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Field Names

The row is the 2016 `gc::DisplayExchangeItemNpcStaticStatus`:
`_itemExchangeByNpcList` (a `pa_vector` of u16 `gc::KeyType`),
`_npcCharacterKey` (u16) and `_dialogIndex` (a u32 in memory, two bytes in
the file). The file writes the key pair before the list as the index key and
again after it. The 2016 `ge::wrapper::DisplayExchangeItemNpcStaticStatusWrapper`
holds a `gc::ItemExchangeByNpcStaticStatus` per list entry, whose
`_itemExchangeByNpcKey` is the u16 key of `itemexchangebynpc.dbss`.

The values match the `DisplayExchangeItemNpc` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `NPC` and `DialogIndex`:

| Field              | Column            | Same value (client 1784) | Same value (client 3474) |
| ------------------ | ----------------- | ------------------------ | ------------------------ |
| npc_character_key  | `NPC`             | 124 of 124 rows          | 124 of 124 rows          |
| dialog_index       | `DialogIndex`     | 124 of 124               | 124 of 124               |
| item_exchange_keys | `SetItemExchange` | 124 of 124               | 114 of 124               |

The 10 rows that differ on client 3474 drop keys from the sheet's list and
add none: `1` (Freharau `41081`), `3` (Andria `43002`, Mansha `50459`,
Thyshelle Arms `44106`), `56` (Gula `44307`) and `238`, `239` (Duncan
`40744`, dialogs `1` to `5`).

## Notes

- The exchange window Lua (`panel_dialog_exchange_item.luac`) reads the row
  of the open dialog through `getCurrentDisplayExchangeWrapper()`, walks
  `getItemExchangeByNpcListSize()` entries and skips an entry whose
  `getItemExchangeByNpcStaticStatusWrapperAtIndex()` is `nil`. Each shown
  entry gives the need item and `getNeedItemCount_s64()`, the result item
  and `getToItemCount_s64()`.
- On client 3474, 124 rows list 478 keys, 216 of them distinct, from `2` to
  `261`, for 81 NPCs. 80 rows are dialog `1`; Villa Keeper `45351` and Villa
  Butler `45345` have dialogs `1` to `17`, Duncan `40744` and EUROPA Event NPC
  `35633` dialogs `1` to `5` or `7`. Villager `637` dialog `750` (dialog name
  Combatant) is the one dialog index above `17`.
- 12 of the 216 keys have no `itemexchangebynpc.dbss` row on client 3474
  (`2`, `5`, `12`, `24`, `28`, `55`, `166`, `167`, `169`, `170`, `171`,
  `172`); on client 1784 4 of 221 have none (`1`, `2`, `5`, `12`). On client
  3474 every key of five rows has no row: Taphtar `45121` (`55`), Freharau
  `41081` (`2`), Crucio Domongatt `41014` dialog `1` and Dominic Erne
  `42109` dialogs `1` and `2` (`5`, `12`).
- None of the four NPCs of those rows has an exchange button in its main
  dialog (dialog `1`) on client 3474, checked in game: Freharau shows Shop
  and Conversation, Crucio Domongatt Conversation and Lord Information,
  Dominic Erne Conversation and Give Gift, and Taphtar Quest, Trade and
  Conversation. A row whose keys all lack an `itemexchangebynpc.dbss` row
  adds no exchange button. Dominic Erne's dialog `2` (`detail_dialog.dbss`
  key `173181`, option "[Return] Dominic Erne's Carnage Axe") was not seen.
- Taphtar's dialog `1` (`detail_dialog.dbss` key `110657`) also has the
  button type `ExceptExchange` and four `[EXC]` options (Shakatu's Rarity
  Box, Memory Fragment x20, Advice of Valks (+50), Shakatu's Luxury Box).
  They are `detail_dialog.dbss` options, separate from the key `55` this
  table lists for him, and did not show on his main dialog.
- On client 3474, 121 of the 124 rows have a `detail_dialog.dbss` record
  for their dialog key; Anahi `45147`, Hetario `59227` and Pacuna `59228`
  (dialog `1`) have none.
