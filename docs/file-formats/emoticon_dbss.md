# `emoticon.dbss` Format

## Purpose

The chat emoticons (emoji): one row per emoticon with its icon, the
animated sequence sheet the chat window plays, the chat keyword that inserts
it (`(Angry)`) and its Korean name. Row `1` is the item link icon sheet of
the chat window. The chat Lua reads the rows through
`ToClient_getEmoticonInfoList()`, `ToClient_getEmoticonInfoByIndex()` and
`ToClient_getEmoticonInfoByKey()` and their getters `getIconPath()`,
`getSequenceImagePath()`, `getName()` and `getKeyword()`
(`panel_chat_emoticon.luac`, `panel_widget_chatmain_2.luac`). Which
emoticons a player can use comes from
[`emoticonpackage.dbss`](emoticonpackage_dbss.md). Companion
`emoticonoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes  | Records       | Row bytes                  |
| ------ | -------------- | ------- | --------------------- | ------ | ------------- | -------------------------- |
| 1      | 1348 and later | 3482    | `emoticon.dbss`       | 26,336 | 87 Row        | 140 to 342, 303 on average |
| 1      | 1348 and later | 3482    | `emoticonoffset.dbss` | 1,396  | 87 Offset Row | 16                         |

| Layout | File                  | Known            | Unknown       |
| ------ | --------------------- | ---------------- | ------------- |
| 1      | `emoticon.dbss`       | 25,640 B (97.4%) | 696 B (2.6%)  |
| 1      | `emoticonoffset.dbss` | 1,048 B (75.1%)  | 348 B (24.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                       |
| --------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `emoticonoffset.dbss` | Optional | `emoticon_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc` | Optional | Emoticon names and keywords: LOC type 60, `str_id1` = `emoticon_key`, `str_id4` `0` name, `1` keyword |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 54 bytes + paths, keyword and name)

| Offset               | Type  | Field              | Notes                                                                                                   |
| -------------------- | ----- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| `+0x00`              | u32   | emoticon_key       | Row key, `1` to `87` in file order on client 3482                                                       |
| `+0x04`              | u32   | unknown_04         | `0` on every row; the index rows carry it after the key too                                             |
| `+0x08`              | str16 | icon_path          | Icon under `ui_texture/`: `Combine/Sequence/Combine_Sequence_imojiMini_Papu.dds`; row `1` stores `Emoticon\Emoticon_Item.dds` with a backslash |
| `icon_path+0x00`     | u8    | icon_count         | Icons on the sheet: `18` on row `1`, `1` on every other row                                             |
| `icon_path+0x01`     | u32   | row_count          | Icon rows on the sheet: `5` on row `1`, `1` on every other row                                          |
| `icon_path+0x05`     | u32   | column_count       | Icon columns on the sheet: `5` on row `1`, `1` on every other row                                       |
| `icon_path+0x09`     | str16 | keyword_kr         | Korean chat keyword (`화남`); the chat inserts it as `(keyword)`. Row `1` stores the text `<NULL>`      |
| `keyword_kr+0x00`    | str16 | sequence_path      | Animated sequence sheet under `ui_texture/` (`Renewal/Sequence/PC_Sequence_imoji_Angry.dds`); row `1` stores `<NULL>` |
| `sequence_path+0x00` | u8    | group              | `0` on row `1`, `1` on every other row                                                                  |
| `sequence_path+0x01` | str16 | name_kr            | Korean name (`화난 흑정령`, Angry Black Spirit)                                                          |
| `name_kr+0x00`       | u32   | unknown_name_kr_00 | `0` on every row                                                                                        |

### `emoticonoffset.dbss`

Bare offset table into `emoticon.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                            |
| ------- | ----------------- | ----- | -------------------------------- |
| `+0x00` | u32               | count | Equals the `emoticon.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                   |

### Offset Row (16 bytes)

| Offset  | Type | Field        | Notes                                                        |
| ------- | ---- | ------------ | ------------------------------------------------------------ |
| `+0x00` | u32  | emoticon_key | Key of the row it points at                                  |
| `+0x04` | u32  | unknown_04   | `0` on every row, as the row's `unknown_04`                  |
| `+0x08` | u32  | data_offset  | Absolute offset of the row in `emoticon.dbss`, at `emoticon_key` |
| `+0x0C` | u32  | data_size    | The whole row, `unknown_name_kr_00` included                 |

The index rows are in file order; on clients 1784 and 3482 every index row
points at the row with its key.

## Field Names

The `Emoticon_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `key`, `name`, `RowCol`, `count`, `filepath`,
`sequenceFilePath`, `keyWord` and `group`, 16 rows. Every column matches
the file by value on the 16 shared keys, on client 1784 (16 rows) and on
client 3482 (87 rows). `RowCol` holds both grid sizes as `5,5`; row and
column order follows the column name.

| Field                     | Column             | Same value (client 1784) | Same value (client 3482) |
| ------------------------- | ------------------ | ------------------------ | ------------------------ |
| emoticon_key              | `key`              | 16 of 16                 | 16 of 16                 |
| icon_path                 | `filepath`         | 16 of 16                 | 16 of 16                 |
| icon_count                | `count`            | 16 of 16                 | 16 of 16                 |
| row_count, column_count   | `RowCol`           | 16 of 16                 | 16 of 16                 |
| keyword_kr                | `keyWord`          | 16 of 16                 | 16 of 16                 |
| sequence_path             | `sequenceFilePath` | 16 of 16                 | 16 of 16                 |
| group                     | `group`            | 16 of 16                 | 16 of 16                 |
| name_kr                   | `name`             | 16 of 16                 | 16 of 16                 |

## Notes

- LOC type 60 holds the English name (`str_id4` `0`, `Angry Black Spirit`)
  and keyword (`str_id4` `1`, `Angry`) of each emoticon by its key; key `1`
  has the name `Item Link` only.
- The item description of an emoticon item names the emoticon it registers
  (`- Curious Papu`, emoticon `14`), not its key.

## Open Questions

### What the Zero Fields Hold

`unknown_04` (after the key, in the row and the index row) and
`unknown_name_kr_00` (after the name) are `0` on every row of clients 1784
and 3482. The pair of key and `unknown_04` may be one 8-byte key; no Lua
getter or sheet column reads either field.

### What `group` Selects

`group` is `0` on the item link row and `1` on every emoticon, on clients
1784 and 3482; no Lua call reads it, so whether other values exist or what
they change is open.
