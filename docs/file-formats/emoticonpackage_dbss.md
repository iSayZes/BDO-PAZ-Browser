# `emoticonpackage.dbss` Format

## Purpose

The emoticon packages: one row per package with a Korean name and the
[`emoticon.dbss`](emoticon_dbss.md) keys it unlocks. On client 3482, 38 of
the 47 packages hold one emoticon; package `1` holds the item link and
emoticons `2` to `5`. No Lua call names this table; the chat window lists
the unlocked emoticons through `ToClient_getEmoticonInfoList()` and shows
an expiry date from `ToClient_getEmoticonExpirationDate()`. Companion
`emoticonpackageoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records              | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | -------------------- | --------- |
| 1      | 1348 and later | 3482    | `emoticonpackage.dbss`       | 2,186 | 120 Emoticon, 47 Row | 8         |
| 1      | 1348 and later | 3482    | `emoticonpackageoffset.dbss` | 756   | 47 Offset Row        | 16        |

| Layout | File                         | Known           | Unknown       |
| ------ | ---------------------------- | --------------- | ------------- |
| 1      | `emoticonpackage.dbss`       | 1,518 B (69.4%) | 668 B (30.6%) |
| 1      | `emoticonpackageoffset.dbss` | 568 B (75.1%)   | 188 B (24.9%) |

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

| File                         | Required | Role                                                                                       |
| ---------------------------- | -------- | ------------------------------------------------------------------------------------------ |
| `emoticonpackageoffset.dbss` | Optional | `package_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `emoticon.dbss`              | Optional | The emoticon names (LOC type 60, else the Korean name) and icons of the listed keys        |
| `languagedata_en.loc`        | Optional | Emoticon names, LOC type 60                                                                |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 20 bytes + name and emoticons)

| Offset         | Type                      | Field          | Notes                                                                               |
| -------------- | ------------------------- | -------------- | ----------------------------------------------------------------------------------- |
| `+0x00`        | u32                       | package_key    | Row key, `1` to `47` in file order on client 3482                                   |
| `+0x04`        | u32                       | unknown_04     | `0` on every row; the index rows carry it after the key too                         |
| `+0x08`        | str16                     | name_kr        | Korean name: `무제한` (unlimited) on 45 rows, `기간제` (limited-time) on rows `2` and `3` (client 3482) |
| `name_kr+0x00` | u32                       | emoticon_count | Number of `emoticons`, `1` to `12` on client 3482                                   |
| `name_kr+0x04` | Emoticon[emoticon_count]  | emoticons      | See Emoticon                                                                        |

### Emoticon (8 bytes)

| Offset  | Type | Field        | Notes                                                                       |
| ------- | ---- | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32  | emoticon_key | An [`emoticon.dbss`](emoticon_dbss.md) key; all 120 entries of client 3482 have a row there |
| `+0x04` | u32  | unknown_04   | `0` on every entry                                                          |

### `emoticonpackageoffset.dbss`

Bare offset table into `emoticonpackage.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `emoticonpackage.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                          |

### Offset Row (16 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | package_key | Key of the row it points at                                        |
| `+0x04` | u32  | unknown_04  | `0` on every row, as the row's `unknown_04`                        |
| `+0x08` | u32  | data_offset | Absolute offset of the row in `emoticonpackage.dbss`, at `package_key` |
| `+0x0C` | u32  | data_size   | The whole row                                                      |

The index rows are in file order; on clients 1784 and 3482 every index row
points at the row with its key.

## Field Names

The `EmoticonPackage_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `key`, `EmoticonKey` (a comma list) and
`name`, 7 rows.

| Field         | Column        | Same value (client 1784) | Same value (client 3482) |
| ------------- | ------------- | ------------------------ | ------------------------ |
| package_key   | `key`         | 7 of 7                   | 7 of 7                   |
| name_kr       | `name`        | 7 of 7                   | 7 of 7                   |
| emoticons     | `EmoticonKey` | 6 of 7                   | 6 of 7                   |

Package `2` lists the same seven keys as the sheet in another order
(`1, 2, 10, 3, 11, 4, 12` against `1,2,3,4,10,11,12`) on both clients, so
the file does not keep the sheet's list order.

## Open Questions

### What the Zero Fields Hold

`unknown_04` after the package key, in the row and the index row, and after
every emoticon key is `0` on clients 1784 and 3482, as in
[`emoticon.dbss`](emoticon_dbss.md). Each key and its `unknown_04` may be
one 8-byte key.

### How a Package Is Granted

No Lua call or sheet column links a package to the item or Pearl Shop
product that unlocks it, so where `package_key` is used is open. The
`기간제` (limited-time) rows suggest an expiry, which
`ToClient_getEmoticonExpirationDate()` reads without a package argument.
