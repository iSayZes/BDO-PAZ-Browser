# `title.dbss` Format

## Purpose

Stores title metadata, the raw Korean title text, raw Korean requirement text,
category, and optional inline PAColor markup for special title names.

`title.dbss` is block-addressed by `titleoffset.dbss`; it is not a flat fixed
record table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes   | Records          | Row bytes                  |
| ------ | -------------- | ------- | ------------------ | ------- | ---------------- | -------------------------- |
| 1      | 1784 and later | 3474    | `title.dbss`       | 869,748 | 3,177 Record     | 200 to 870, 274 on average |
| 1      | 1784 and later | 3474    | `titleoffset.dbss` | 38,128  | 3,177 Offset Row | 12                         |

| Layout | File               | Known             | Unknown           |
| ------ | ------------------ | ----------------- | ----------------- |
| 1      | `title.dbss`       | 704,544 B (81.0%) | 165,204 B (19.0%) |
| 1      | `titleoffset.dbss` | 38,128 B (100.0%) | 0 B (0.0%)        |

<!-- versions:end -->

## Companion Files

- `titleoffset.dbss` - required. Provides `title_id -> (offset, size)` block
  lookup.
- `languagedata_en.loc` - optional for English title/requirement display.

## Layout 1

### File Layout

A record count, then the records back to back; `titleoffset.dbss` addresses
each one.

| Offset  | Type          | Field   | Notes                                           |
| ------- | ------------- | ------- | ----------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; equals the `titleoffset.dbss` count |
| `+0x04` | Record[count] | records | See Record                                      |

### Record (variable: 100 bytes + text)

All inspected records fit one generalized header. The older A/B/C layouts are
just `key_count` values 1, 2, and 3. The tail after `requirement_text_kr`
reads the same on all 3,177 records of client 3473; the tail names count from
the end of `requirement_text_kr`.

| Offset                     | Type           | Field                     | Notes                                                             |
| -------------------------- | -------------- | ------------------------- | ----------------------------------------------------------------- |
| `+0x00`                    | u32            | key_count                 | Number of 32-bit key/hash/group fields before `title_id`          |
| `+0x04`                    | u32[key_count] | key_values                | `key_count` values                                                |
| `key_values+0x00`          | u32            | title_id                  | Matches offset entry and loc string ID                            |
| `key_values+0x04`          | str16          | title_text_kr             | Korean title; PAColor-tagged on the styled title records, see Styled Title Records |
| `title_text_kr+0x00`       | str16          | requirement_text_kr       | Korean requirement, usually with PAColor tags                     |
| `requirement_text_kr+0x00` | u32            | unknown_tail_00           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x04` | u32            | category_id               | See Category IDs; `0` on 1,321 records, `1` on 900, `2` on 197, `3` on 759 (client 3473) |
| `requirement_text_kr+0x08` | bytes[20]      | unknown_tail_08           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x1C` | u32            | unknown_tail_1c           | `0` on 3,102 records; else `3600` to `7776000`, all multiples of 3,600 (`2592000` on 37) (client 3473) |
| `requirement_text_kr+0x20` | u32            | unknown_tail_20           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x24` | u32            | unknown_tail_24           | `0` on 3,082 records; else `604800` to `15552000`, all multiples of 3,600 (`2592000` on 50) (client 3473) |
| `requirement_text_kr+0x28` | u32            | unknown_tail_28           | Always `0` (client 3473)                                          |
| `requirement_text_kr+0x2C` | str8           | effect_name               | Aura/effect name, e.g. `vCalsutain_Buff_Aura_02A`; empty on 3,105 records (client 3473) |
| `effect_name+0x00`         | str8           | color_argb                | ASCII hex, e.g. `FFFF7124`; 8 characters on 365 records, else empty (client 3473) |
| `color_argb+0x00`          | u32            | color_value               | Same value as little-endian integer; `0` when `color_argb` is empty |
| `color_argb+0x04`          | bytes[12]      | unknown_after_color_value | Always `0` (client 3473)                                          |

Observed `key_count` distribution:

| key_count | Count | Former Layout  |
| --------- | ----- | -------------- |
| 1         | 2,844 | A              |
| 2         | 175   | B              |
| 3         | 15    | C              |
| 4         | 1     | Previously `?` |
| 6         | 13    | Previously `?` |

Earlier versions of this doc read the count of `title_text_kr` as a u32
`style_or_title_len` and a u32 `zero`, and the count of
`requirement_text_kr` as a u16 `requirement_text_length` and three u16 `0`.
Both are the u64 count of a `str16`.

### `titleoffset.dbss`

| Offset  | Type              | Field | Notes       |
| ------- | ----------------- | ----- | ----------- |
| `+0x00` | u32               | count | Entry count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row |

Observed entries: 3,048 in the pre-2026-09-27 test fixture, 3,172 in the
2026-09-27 client. The largest `offset + size` equals the `title.dbss` byte
length, so the offset table accounts for the full file.

### Offset Row (12 bytes)

| Offset  | Type | Field    | Notes                                                |
| ------- | ---- | -------- | ---------------------------------------------------- |
| `+0x00` | u32  | title_id | Title ID                                             |
| `+0x04` | u32  | offset   | Offset into `title.dbss`, at the record's `key_count` |
| `+0x08` | u32  | size     | Block size                                           |

## Text Payload

Most records have a plain Korean title followed by the Korean requirement
string.

The count of `requirement_text_kr` is the UTF-16 code-unit length of the tagged
requirement string, not the visible text length after stripping PA tags.

Example, title ID `44`:

| Field                     | Value                    |
| ------------------------- | ------------------------ |
| English title             | `Stoneback Crab Artisan` |
| Korean title              | `돌멘게 공예가`          |
| Requirement length marker | `66`                     |
| Tagged requirement length | `66`                     |
| Plain requirement length  | `35`                     |
| Category                  | `1` / Combat             |

## Styled Title Records

Thirty records, title IDs `3645..3674`, begin their text payload with a PAColor
tag. These are class "MASTER ..." titles. For these records, as for every
other, the header field after `title_id` is the count of `title_text_kr`, here
the length of the styled title payload.

Example, title ID `3645`:

| Field                            | Value                   |
| -------------------------------- | ----------------------- |
| Header field                     | `231`                   |
| Styled title payload length      | `231` UTF-16 code units |
| Plain title after stripping tags | `MASTER WARRIOR`        |
| Requirement length marker        | `115`                   |
| Category                         | `0` / World             |

An earlier version of this doc read the styled title payload as 232 code units,
the header field plus one, with the requirement length marker as its final code
unit. That last unit is the low half of the `requirement_text_kr` count.

## Category IDs

`title.dbss` itself carries a category field after the requirement text.

| ID  | Name       |
| --- | ---------- |
| 0   | World      |
| 1   | Combat     |
| 2   | Life Skill |
| 3   | Fishing    |

## Extra Payload And Title Color

Most default-color titles have no non-zero payload after the category field.
Most non-default-color titles have a 64-byte or 88-byte extra payload. The title
color is encoded near the end of that payload as both an ASCII `AARRGGBB`
string and the same value as a little-endian u32.

The extra payload is the Record tail from `unknown_tail_08` to
`unknown_after_color_value` with its trailing zeros cut: 64 bytes when
`effect_name` is empty and `color_argb` holds 8 characters, 88 bytes when
`effect_name` holds 24. `color_argb` is the `color_len` and `color_argb` of
earlier versions of this doc, and `effect_name` their `effect_len` and
`effect_name`.

Example:

```text
46 46 46 46 37 31 32 34 24 71 ff ff
F  F  F  F  7  1  2  4  packed 0xFFFF7124
```

This decodes to `0xFFFF7124`, displayed in CSS as `#FF7124`.

88-byte payloads add an aura/effect string before the color. The name is
probably misspelled data (`Calsutain` instead of `Calustian` or similar), so
parsers should preserve it exactly.

In the current extracted sample, 335 records decode a title color from this
payload. For example, title ID `3451` (`Fisher`) has the same `0xFFAFEEEE`
payload color as `Angel`. This was visually confirmed in-game.

Other visual confirmations:

| Titles                                                           | Payload Color | Result                                |
| ---------------------------------------------------------------- | ------------- | ------------------------------------- |
| `The Greatest Guardian`, `#BDORemastered`, `One of the Greatest` | `0xFFFF7124`  | Same color                            |
| `REBOOT`                                                         | `0xFFFF7124`  | Same color family as the titles above |
| `Nouverikant`                                                    | `0xFFFFB400`  | Not the same as `REBOOT`              |

These confirmations support using the DBSS payload color as the precise source
for individual non-default title display.

## PAColor Tags

Requirement text commonly starts with:

```text
<PAColor0xFFf32200>칭호 조건<PAOldColor>:
```

This default requirement label color is not the visible title-name color.
The English requirement (LOC type 1, `str_id4` 1) carries the same tag on its
`Title Requirement` label in all 3,322 rows on client 3458. The parser keeps the
tags in `requirement_text_kr`, and the table draws them.

Special "MASTER ..." title names are different: their title payload itself is
PAColor-tagged, so those PAColor tags are part of the displayed title name. The
tags draw a gradient, one colour per letter pair: `MASTER WARRIOR` goes from
`0xffffffff` on `MA` down to `0xff424242` on `R`, as in game. The parser keeps
the tags in `title_text_kr`, and the English LOC name (type 1) carries the same
tags. Two more LOC names are tagged without a styled payload (`Seasonal
Sensation!`, `Rise Above the Disorder`); 1348 `Lights, Camera, Action!` has a
stored payload colour and a different LOC tag colour; the table draws the tag
colour (unchecked in game).

## Style Field

Earlier versions of this doc read the header field after `title_id`
(`style_or_title_len`) as a style/category-like value for normal records, with
common values `2..17`, rare values through `28` and `43`, and a few high values
used only by styled title records. It is the count of `title_text_kr`: the
title's length in UTF-16 code units.

It does not identify the final visible title color. Counterexample: three
titles of 7 code units each.

| Title ID | Title                      | Header Field | Visual Result |
| -------- | -------------------------- | ------------ | ------------- |
| `2117`   | The Greatest Guardian      | `7`          | Special color |
| `44`     | Stoneback Crab Artisan     | `7`          | Normal blue   |
| `45`     | Stoneback Crab Philosopher | `7`          | Normal blue   |

## Optional Extra Payload

Some color payloads also include small non-zero integers at `unknown_tail_1c`
and `unknown_tail_24` (`+0x14` and `+0x1C` of the extra payload). These look
like grouping/effect parameters, not the title color itself.

## Recommended Parser Behavior

1. Use `titleoffset.dbss` to slice blocks.
2. Read `key_count`, then `key_values` and `title_id`.
3. Read `title_text_kr` and `requirement_text_kr` through their u64 counts.
4. Read `category_id`, then `effect_name`, `color_argb` and `color_value` at
   their Record offsets.
5. A `title_text_kr` that starts with a PAColor tag is a styled title.
6. Strip PA tags only for readable display; keep raw PA tags for debugging.
7. Look up English name/requirement from `languagedata_en.loc`:
   - Name: `str_type=1, str_id1=title_id, str_id4=0`
   - Requirement: `str_type=1, str_id1=title_id, str_id4=1`

## Notes

- The previously unknown `?` layouts are now explained by `key_count` values 4
  and 6.
- The old `u32_14`, `u32_18`, and similar columns can be UTF-16 text fragments,
  not structured integers.
- `titlecategory.bss` is not needed for category display; `title.dbss` carries
  the category after the requirement string.

## Open Questions

### Extra Payload Parameters

The color value and optional aura/effect name are now decoded, but
`unknown_tail_1c` and `unknown_tail_24` in the extra payload are still
unresolved.

### Normal Title Name Color

For titles without an extra color payload, the default visible color is still
not stored as a per-record RGB value in `title.dbss`. Disproven candidates:

- Requirement `_PA_COLOR_MARKER`
- `style_or_title_len` alone (the count of `title_text_kr`)
- A fixed early `u32` field after the title text

Likely sources still to investigate:

- client-side title color table
- UI scripts / title rendering logic
- another DBSS file related to title grade/type/color
- implicit default color chosen by title category/UI code
