# `bdoservanttitless.bss` Format

## Purpose

Breed titles of the horses: one row per servant character with the index of
its title in the file's string table, Korean dev text `품종 1번` ("breed 1")
to `품종 24번`, and a contents group that gates the row. On client 3474 the
file has 254 rows and 24 titles.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 2      | 3474 and later | 3474    | `bdoservanttitless.bss` | 2,950 | 254 Row | 10        |
| 1      | 1784           | 1784    | `bdoservanttitless.bss` | 2,334 | 166 Row | 12        |

| Layout | File                    | Known            | Unknown    |
| ------ | ----------------------- | ---------------- | ---------- |
| 2      | `bdoservanttitless.bss` | 2,950 B (100.0%) | 0 B (0.0%) |
| 1      | `bdoservanttitless.bss` | 2,334 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | Servant names (LOC type 6) and the shown breed title (LOC type 111, `str_id1` = `character_id`) |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                         |
| ------------------- | ----------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                                        |
| `+0x04`             | u32               | record_count       | 254 on client 3474                            |
| `+0x08`             | Row[record_count] | records            | See Row                                       |
| `records+0x00`      | String Table      | string_table       | The titles                                    |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`             |
| `string_table+0x04` | u32               | zero               | `0`                                           |

### Row (10 bytes)

| Offset  | Type | Field           | Notes |
| ------- | ---- | --------------- | ----- |
| `+0x00` | u16  | character_id    | Servant character, as in `servant.bss`; unique |
| `+0x02` | u32  | title_name      | Index into `strings` |
| `+0x06` | u32  | contents_option | `0`, or a contents group key: 258, 590, 751, 828, 2168 on 6 rows (client 3474) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | 24 on client 3474 |
| `+0x04` | pstr[string_count] | strings      | `품종 1번` to `품종 24번`, wide (`is_wide` 1) |

## Layout 1

Client 1784 repeats `character_id` and has 166 rows and 20 titles; its
`contents_option` is `0` on every row.

### Row (12 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u16  | character_id     | |
| `+0x02` | u16  | character_id_dup | Equals `character_id` on every row |
| `+0x04` | u32  | title_name       | |
| `+0x08` | u32  | contents_option  | |

## Field Names

The names follow the `ServantTitleName_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (`CharacterKey`, `TitleName`,
`ContentsOption`), matched value by value:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `CharacterKey` | `character_id` | 166 of 166 | 166 of 254 |
| `TitleName` | the string `title_name` points at | 166 | 165 |
| `ContentsOption` | `contents_option` | 166 | 166 |

The sheet's `ContentsOption` is empty on every row, so the column match
rests on the zeros. The 6 non-zero client 3474 values are all keys of
[contentsgroupoptionstaticstatusmanager.bss](contentsgroupoptionstaticstatusmanager_bss.md),
open on that client, and sit on servants newer than the sheet: Krogdalo
(31595), Voltarion (31611, 31612) and Mythical Arduanatt, Diné and Doom
(31619 to 31621).

## Notes

- Rows are in neither key nor title order. The string table holds each title
  once; client 1784 lists them in first-use order (`품종 1번`, `품종 10번`,
  `품종 4번`, ...), client 3474 in number order.
- The title shows in the horse windows as Base Coat (LOC type 37 `Base
  Coat`), for example "Base Coat: Breed 11" on a tier 6 stallion that the
  `vehicleskillowner.dbss` learn chances identify as 9953 (`품종 11번`), and
  "Breed 2" on 9915 (`품종 2번`), and "Breed 13" on a Mythical horse, which
  only 31619 (`품종 13번`, tier 9) can be; checked in game on client 3474. The
  displayed text is "Breed N", not the Korean string: LOC type 111 holds it
  per character (`str_id1` = `character_id`, `str_id4` 0), "Breed 11" for
  9953. On client 3474 all 254 rows have that text, and its number is the
  one in the row's `품종 N번`.
