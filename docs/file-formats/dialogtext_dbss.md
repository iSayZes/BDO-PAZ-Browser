# `dialogtext.dbss` Format

## Purpose

Stores named pools of NPC lines. A dialog greeting in `detail_dialog.dbss` can be the tag `{GetRandomText(<name>)}`, and the client then shows a random line from the pool with that name each time the dialog opens. Most lines start with an `{AudioVoice(...)}` tag that names the voice file.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes   | Records                                     | Row bytes                 |
| ------ | -------------- | ------- | ----------------------- | ------- | ------------------------------------------- | ------------------------- |
| 1      | 3473 and later | 3473    | `dialogtext.dbss`       | 614,336 | 3,645 Line, 1,043 Pool Record, 1,043 Record | 20 to 308, 153 on average |
| 1      | 3473 and later | 3473    | `dialogtextoffset.dbss` | 12,520  | 1,043 Index Row                             | 12                        |

| Layout | File                    | Known             | Unknown        |
| ------ | ----------------------- | ----------------- | -------------- |
| 1      | `dialogtext.dbss`       | 610,164 B (99.3%) | 4,172 B (0.7%) |
| 1      | `dialogtextoffset.dbss` | 12,520 B (100.0%) | 0 B (0.0%)     |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                         |
| ----------------------- | -------- | -------------------------------------------- |
| `dialogtextoffset.dbss` | Required | Maps each pool key to its record offset and size |
| `languagedata_*.loc`    | Optional | The lines in the user's language, LOC type `36` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                                        |
| ------- | ------------- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32           | count   | Number of records; matches the offset file                   |
| `+0x04` | Record[count] | records | Each record is preceded by a repeated copy of its `u32` key; see Record |

As in `detail_dialog.dbss`, the first record starts at `8`, every record starts 4 bytes after the previous one ends, and the last ends at end of file.

### Record (variable: 4 bytes + pool record)

| Offset  | Type        | Field      | Notes                                                       |
| ------- | ----------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32         | key_prefix | Repeated copy of the record's `key`                         |
| `+0x04` | Pool Record | pool       | `size` bytes; the index row's `offset` points at this field |

### Pool Record (variable: 20 bytes + name and lines)

| Offset      | Type             | Field       | Notes |
| ----------- | ---------------- | ----------- | ----- |
| `+0x00`     | u32              | key         | Same as the index key |
| `+0x04`     | str16            | name        | Pool name, unique; e.g. `PEDU_47759_1`, `Morning_47295`, `SnowyMountain_50953` |
| `name+0x00` | u32              | line_count  | `3` on 527 of 1,043 pools, `2` on 222, `4` on 170, up to `30` |
| `name+0x04` | Line[line_count] | lines       | See Line |
| `lines+0x00` | u32              | unknown_end | Always `0`; the record ends exactly here |

### Line (variable: 10 bytes + text)

| Offset  | Type  | Field   | Notes |
| ------- | ----- | ------- | ----- |
| `+0x00` | u16   | text_id | LOC text ID of the line: LOC type `36`, `str_id1 = key`, `str_id2 = text_id`; counts up by one inside a pool, from `1` in 260 pools and from a larger number elsewhere (`379` in `Morning_47295`) |
| `+0x02` | str16 | text    | Korean, usually with a leading `{AudioVoice(...)}` tag; line breaks are the two characters `\n`, not a newline |

All 1,043 records of client 3458 walk with this layout and end exactly at their index size.

### `dialogtextoffset.dbss`

No `PABR` magic and no trailer.

| Offset  | Type             | Field | Notes                                       |
| ------- | ---------------- | ----- | ------------------------------------------- |
| `+0x00` | u32              | count | Number of index rows; `1043` in client 3458 |
| `+0x04` | Index Row[count] | rows  | See Index Row                               |

The key is a u32 unique per pool with no visible structure (`0x24E52C6C` for `PEDU_47759_1`); it is not a plain CRC-32 of the name (ASCII, lowercase or UTF-16).

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                          |
| ------- | ---- | ------ | ---------------------------------------------- |
| `+0x00` | u32  | key    | Pool key                                       |
| `+0x04` | u32  | offset | Byte offset of the record in `dialogtext.dbss` |
| `+0x08` | u32  | size   | Record size in bytes                           |

## Notes

- Checked in game 2026-09-29: Ganin Arth (`47744`) has the greeting `{GetRandomText(PEDU_47744_1)}`, and talking to her three times showed all three pool lines: `1` ("It has been some time, Adventurer..."), `2` ("If you seek to hone your skills, say the word...") and `3` ("I am here to oversee the Hashashin..."). A random line is picked each time the dialog opens, not only on the first talk.
- 82 of the first 200 pool names occur in `detail_dialog.dbss` greetings as `{GetRandomText(<name>)}`.
- The names mostly start with a region or content prefix: `Morning` (290, Land of the Morning Light), `SnowyMountain` (163), `PEDU` (149), `Ulukita` (143), `MediaS` (100), `Olvia` (49).
- 2,931 of the 3,645 lines carry an `{AudioVoice(...)}` tag. The last number of the voice name equals `text_id` on only 553 of them.
- All 3,645 lines have a LOC type `36` row (`36, key, text_id, 0, 0`), e.g. `PEDU_47759_1` line `1`: "{AudioVoice(NPC_VCE_47759_1_1_Jamalko)}Fish for the Imperial..."; the English text keeps the voice tag.
