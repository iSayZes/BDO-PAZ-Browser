# `dialogtext.dbss` Format

## Purpose

Stores named pools of NPC lines. A dialog greeting in `detail_dialog.dbss` can be the tag `{GetRandomText(<name>)}`, and the client then shows a random line from the pool with that name each time the dialog opens. Most lines start with an `{AudioVoice(...)}` tag that names the voice file.

Example (pool `PEDU_47759_1`, three lines):

```text
1: {AudioVoice(NPC_VCE_47759_1_1_Jamalko)}물고기를 황실에 납품하시겠습니까?\n납품 가능 항목인지 상세히 살펴보십시오.
2: {AudioVoice(NPC_VCE_47759_1_2_Jamalko)}이곳에서 황실까지 납품하는 게 쉽진 않습니다.\n물고기는 금방 상해버리니까요.
3: {AudioVoice(NPC_VCE_47759_1_3_Jamalko)}여기에서도 황실에 납품해 주신다니,\n황실을 대신해 감사드립니다.
```

## Companion Files

| File                    | Required | Role                                         |
| ----------------------- | -------- | -------------------------------------------- |
| `dialogtextoffset.dbss` | Required | Maps each pool key to its record offset and size |
| `languagedata_*.loc`    | Optional | The lines in the user's language, LOC type `36` |

All multi-byte values are little-endian.

## File Layout

### dialogtextoffset.dbss

No `PABR` magic and no trailer.

| Offset  | Type | Field | Notes                                   |
| ------- | ---- | ----- | --------------------------------------- |
| `+0x00` | u32  | count | Number of index rows; `1043` in client 3458 |
| `+0x04` | ...  | rows  | `count` 12-byte rows: `u32 key`, `u32 offset`, `u32 size` |

The key is a u32 unique per pool with no visible structure (`0x24E52C6C` for `PEDU_47759_1`); it is not a plain CRC-32 of the name (ASCII, lowercase or UTF-16).

### dialogtext.dbss

| Offset  | Type | Field   | Notes                                                        |
| ------- | ---- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32  | count   | Number of records; matches the offset file                   |
| `+0x04` | ...  | records | Each record is preceded by a repeated copy of its `u32` key |

As in `detail_dialog.dbss`, the first record starts at `8`, every record starts 4 bytes after the previous one ends, and the last ends at end of file.

## Record Structure

### Pool Record (variable, `size` bytes from `offset`)

| Order | Type | Field | Notes |
| ----- | ---- | ----- | ----- |
| 1 | u32 | key | Same as the index key |
| 2 | u64 + utf16 | name | Pool name, unique; e.g. `PEDU_47759_1`, `Morning_47295`, `SnowyMountain_50953` |
| 3 | u32 | line_count | `3` on 527 of 1,043 pools, `2` on 222, `4` on 170, up to `30` |
| 4 | line_count × Line | lines | |
| 5 | u32 | end | Always `0`; the record ends exactly here |

### Line

| Order | Type | Field | Notes |
| ----- | ---- | ----- | ----- |
| 1 | u16 | text_id | LOC text ID of the line: LOC type `36`, `str_id1 = key`, `str_id2 = text_id`; counts up by one inside a pool, from `1` in 260 pools and from a larger number elsewhere (`379` in `Morning_47295`) |
| 2 | u64 + utf16 | text | Korean, usually with a leading `{AudioVoice(...)}` tag; line breaks are the two characters `\n`, not a newline |

All 1,043 records of client 3458 walk with this layout and end exactly at their index size.

## Notes

- Checked in game 2026-09-29: Ganin Arth (`47744`) has the greeting `{GetRandomText(PEDU_47744_1)}`, and talking to her three times showed all three pool lines: `1` ("It has been some time, Adventurer..."), `2` ("If you seek to hone your skills, say the word...") and `3` ("I am here to oversee the Hashashin..."). A random line is picked each time the dialog opens, not only on the first talk.
- 82 of the first 200 pool names occur in `detail_dialog.dbss` greetings as `{GetRandomText(<name>)}`.
- The names mostly start with a region or content prefix: `Morning` (290, Land of the Morning Light), `SnowyMountain` (163), `PEDU` (149), `Ulukita` (143), `MediaS` (100), `Olvia` (49).
- 2,931 of the 3,645 lines carry an `{AudioVoice(...)}` tag. The last number of the voice name equals `text_id` on only 553 of them.
- All 3,645 lines have a LOC type `36` row (`36, key, text_id, 0, 0`), e.g. `PEDU_47759_1` line `1`: "{AudioVoice(NPC_VCE_47759_1_1_Jamalko)}Fish for the Imperial..."; the English text keeps the voice tag.
