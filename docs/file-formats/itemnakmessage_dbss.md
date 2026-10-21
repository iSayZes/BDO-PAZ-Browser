# `itemnakmessage.dbss` Format

## Purpose

The screen-wide message shown when someone obtains one of a few rare items
(Rich Merchant's Ring, Archaeologist's Map, Ornette's and Odore's Spirit
Essence, Krogdalo's Sanctuary and others): per item key a main line and a sub line, both stored as
`GAME` sheet keys of [`stringtable.bss`](stringtable_bss.md). The main line
holds `{playerName}` and `{itemName}` placeholders. Companion
`itemnakmessageoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | ------------- | --------- |
| 1      | 1485 and later | 3474    | `itemnakmessage.dbss`       | 1,412 | 11 Row        | 128       |
| 1      | 1485 and later | 3474    | `itemnakmessageoffset.dbss` | 152   | 11 Offset Row | 12        |

| Layout | File                        | Known            | Unknown    |
| ------ | --------------------------- | ---------------- | ---------- |
| 1      | `itemnakmessage.dbss`       | 1,412 B (100.0%) | 0 B (0.0%) |
| 1      | `itemnakmessageoffset.dbss` | 152 B (100.0%)   | 0 B (0.0%) |

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

| File                        | Required | Role                                                                          |
| --------------------------- | -------- | ----------------------------------------------------------------------------- |
| `itemnakmessageoffset.dbss` | Optional | `item_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`       | Optional | Item names (type `0`) and the message text (type `37`)                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                               |
| ------- | ---------- | ----- | ----------------------------------- |
| `+0x00` | u32        | count | Number of rows; `11` on client 3474 |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 20 bytes + message keys)

| Offset                  | Type  | Field            | Notes                                                                |
| ----------------------- | ----- | ---------------- | -------------------------------------------------------------------- |
| `+0x00`                 | u32   | item_key         | The item, an item enchant key (`enchant_level << 24 \| item_id`); level `0` on every row of clients 1784 and 3474 |
| `+0x04`                 | str16 | main_message_key | `GAME` sheet key of the main line, `NAKMESSAGE_LUXURYFIND_MAIN` on every row of client 3474 |
| `main_message_key+0x00` | str16 | sub_message_key  | `GAME` sheet key of the sub line, `NAKMESSAGE_LUXURYFIND_SUB_01` to `_09` on client 3474 |

The rows are not sorted by key. On client 3474 every row is 128 bytes
long, since all keys there have the same length; on client 1784 the rows
are 138 and 140 bytes.

### `itemnakmessageoffset.dbss`

`PABR` index with 12-byte rows and a u32 key.

| Offset              | Type              | Field              | Notes                                         |
| ------------------- | ----------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]           | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32               | count              | Equals the `itemnakmessage.dbss` count        |
| `+0x08`             | Offset Row[count] | rows               | See Offset Row                                |
| `rows+0x00`         | String Table      | string_table       | The PABR string table, present but empty      |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 12 x count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                    |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u32  | item_key    | Key of the row it points at                                  |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `itemnakmessage.dbss`, at its `item_key` |
| `+0x08` | u32  | data_size   | The whole row                                                |

Read by `parse_pabr_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in another order than the file; on clients 1784 and 3474
every index row points at the row with its key.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Field Names

The `BigNakMessage` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `itemkey`, `mainMsg` and `subMsg`, and its 8
rows match the 8 rows of client 1784 on all three columns. Client 3474 has
the same 8 items and 3 more (`53803`, `59418`, `65299`), and new keys in
both columns: the 1784 keys `LUA_NAKMESSAGE_LUXURYFIND_MAIN`, `_MAIN2` and
`_MAIN3` (three wordings of the adventurer's title) and the shared
`LUA_NAKMESSAGE_LUXURYFIND_SUB` became one `NAKMESSAGE_LUXURYFIND_MAIN` and
one `NAKMESSAGE_LUXURYFIND_SUB_NN` per item. The developer workbook
(`datasheet_bignakmessage.xlsm`) adds the note column `#itemname` with the
Korean item name. The field names here add `_key`, since the values are
string keys.

## Notes

- Every key on client 3474 is a `GAME` sheet row of `stringtable.bss`; the
  handler shows its LOC type 37 text, found by the key's hash.
- No client Lua names the table or its keys; the message window
  (`nakmessage_renewel.luac`) has a separate `__eNakMessage_RichMerchantRing`
  type for the Rich Merchant's Ring reward.
