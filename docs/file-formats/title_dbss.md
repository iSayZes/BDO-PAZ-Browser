# title.dbss Format

## Purpose

Stores title metadata, the raw Korean title text, raw Korean requirement text,
category, and optional inline PAColor markup for special title names.

`title.dbss` is block-addressed by `titleoffset.dbss`; it is not a flat fixed
record table.

## Companion Files

- `titleoffset.dbss` - required. Provides `title_id -> (offset, size)` block
  lookup.
- `languagedata_en.loc` - optional for English title/requirement display.

## Offset File Format: titleoffset.dbss

| Offset           | Type | Description              |
| ---------------- | ---- | ------------------------ |
| `+0x00`          | u32  | Entry count              |
| `+0x04 + n*0x0C` | u32  | Title ID                 |
| `+0x08 + n*0x0C` | u32  | Offset into `title.dbss` |
| `+0x0C + n*0x0C` | u32  | Block size               |

Observed sample: 3,048 entries. The largest `offset + size` equals the
`title.dbss` byte length, so the offset table accounts for the full file.

## General Block Header

All inspected records fit one generalized header. The older A/B/C layouts are
just `key_count` values 1, 2, and 3.

| Offset                    | Type      | Name                 | Description                                                       |
| ------------------------- | --------- | -------------------- | ----------------------------------------------------------------- |
| `+0x00`                   | u32       | key_count            | Number of 32-bit key/hash/group fields before `title_id`          |
| `+0x04`                   | u32[]     | key_values           | `key_count` values                                                |
| `+0x04 + key_count*4`     | u32       | title_id             | Matches offset entry and loc string ID                            |
| `+0x08 + key_count*4`     | u32       | style_or_title_len   | Usually a style value; for styled title records, title length - 1 |
| `+0x0C + key_count*4`     | u32       | zero                 | Observed `0`                                                      |
| `+0x10 + key_count*4`     | utf16-le  | title/requirement    | Variable text payload                                             |

Observed `key_count` distribution:

| key_count | Count | Former Layout |
| --------- | ----- | ------------- |
| 1         | 2,844 | A             |
| 2         | 175   | B             |
| 3         | 15    | C             |
| 4         | 1     | Previously `?` |
| 6         | 13    | Previously `?` |

This means title ID offset is:

```text
0x04 + key_count * 4
```

and the style/length field offset is:

```text
title_id_offset + 0x04
```

## Text Payload

Most records have a plain Korean title followed by the Korean requirement
string.

```text
utf16 title text
u16 requirement_text_length
u16 0
u16 0
u16 0
utf16 requirement text, usually with PAColor tags
u16 0
u16 0
u32 category_id
padding / optional extra payload
```

The `requirement_text_length` is the UTF-16 code-unit length of the tagged
requirement string, not the visible text length after stripping PA tags.

Example, title ID `44`:

| Field | Value |
| ----- | ----- |
| English title | `Stoneback Crab Artisan` |
| Korean title | `돌멘게 공예가` |
| Requirement length marker | `66` |
| Tagged requirement length | `66` |
| Plain requirement length | `35` |
| Category | `1` / Combat |

## Styled Title Records

Thirty records, title IDs `3645..3674`, begin their text payload with a PAColor
tag. These are class "MASTER ..." titles. For these records, the header field
after `title_id` is not a style enum; it is the styled title payload length
minus one.

Example, title ID `3645`:

| Field | Value |
| ----- | ----- |
| Header field | `231` |
| Styled title payload length | `232` UTF-16 code units |
| Plain title after stripping tags | `MASTER WARRIOR` |
| Requirement length marker | `115` |
| Category | `0` / World |

The final code unit of the styled title payload is still the requirement length
marker, same as normal records.

## Category IDs

`title.dbss` itself carries a category field after the requirement text.

| ID | Name       |
| -- | ---------- |
| 0  | World      |
| 1  | Combat     |
| 2  | Life Skill |
| 3  | Fishing    |

## Extra Payload And Title Color

Most default-color titles have no non-zero payload after the category field.
Most non-default-color titles have a 64-byte or 88-byte extra payload. The title
color is encoded near the end of that payload as both an ASCII `AARRGGBB`
string and the same value as a little-endian u32.

64-byte color payload tail:

| Offset | Type      | Name        | Description                         |
| ------ | --------- | ----------- | ----------------------------------- |
| `+0x2C` | u32      | color_len   | Observed `8`                        |
| `+0x34` | char[8]  | color_argb  | ASCII hex, e.g. `FFFF7124`          |
| `+0x3C` | u32      | color_value | Same value as little-endian integer |

Example:

```text
46 46 46 46 37 31 32 34 24 71 ff ff
F  F  F  F  7  1  2  4  packed 0xFFFF7124
```

This decodes to `0xFFFF7124`, displayed in CSS as `#FF7124`.

88-byte payloads add an aura/effect string before the color:

| Offset | Type     | Name          | Description                                      |
| ------ | -------- | ------------- | ------------------------------------------------ |
| `+0x24` | u32     | effect_len    | Observed `0x18`                                  |
| `+0x2C` | char[]  | effect_name   | e.g. `vCalsutain_Buff_Aura_02A`                  |
| `+0x44` | u32     | color_len     | Observed `8`                                     |
| `+0x4C` | char[8] | color_argb    | ASCII hex                                        |
| `+0x54` | u32     | color_value   | Same color as little-endian integer              |

The name is probably misspelled data (`Calsutain` instead of `Calustian` or
similar), so parsers should preserve it exactly.

In the current extracted sample, 335 records decode a title color from this
payload. For example, title ID `3451` (`Fisher`) has the same `0xFFAFEEEE`
payload color as `Angel`. This was visually confirmed in-game.

Other visual confirmations:

| Titles | Payload Color | Result |
| ------ | ------------- | ------ |
| `The Greatest Guardian`, `#BDORemastered`, `One of the Greatest` | `0xFFFF7124` | Same color |
| `REBOOT` | `0xFFFF7124` | Same color family as the titles above |
| `Nouverikant` | `0xFFFFB400` | Not the same as `REBOOT` |

These confirmations support using the DBSS payload color as the precise source
for individual non-default title display.

## PAColor Tags

Requirement text commonly starts with:

```text
<PAColor0xFFf32200>칭호 조건<PAOldColor>:
```

This default requirement label color is not the visible title-name color.

Special "MASTER ..." title names are different: their title payload itself is
PAColor-tagged, so those PAColor tags are part of the displayed title name.

## Style Field

For normal records, `style_or_title_len` is a style/category-like value. Common
observed values include `2..17`, with rare values through `28`, `43`, and a few
high values used only by styled title records.

`style_or_title_len` is not enough by itself to identify the final visible title
color. Counterexample:

| Title ID | Title                      | Header Field | Visual Result |
| -------- | -------------------------- | ------------ | ------------- |
| `2117`   | The Greatest Guardian      | `7`          | Special color |
| `44`     | Stoneback Crab Artisan     | `7`          | Normal blue   |
| `45`     | Stoneback Crab Philosopher | `7`          | Normal blue   |

## Optional Extra Payload

Some color payloads also include small non-zero integers at offsets such as
`+0x14` and `+0x1C`. These look like grouping/effect parameters, not the title
color itself.

## Recommended Parser Behavior

1. Use `titleoffset.dbss` to slice blocks.
2. Read `key_count`, then derive `title_id_offset`.
3. Read `key_values`, `title_id`, `style_or_title_len`, and the zero field.
4. If text starts with a PAColor tag, treat `style_or_title_len` as styled title
   payload length minus one.
5. Otherwise treat `style_or_title_len` as the normal style field.
6. Extract Korean title text, tagged Korean requirement text, requirement
   length marker, and category.
7. Strip PA tags only for readable display; keep raw PA tags for debugging.
8. Look up English name/requirement from `languagedata_en.loc`:
   - Name: `str_type=1, str_id1=title_id, str_id4=0`
   - Requirement: `str_type=1, str_id1=title_id, str_id4=1`

## Suggested UI Layout

| Column | Align | Notes |
| ------ | ----- | ----- |
| Title ID | num | Loc lookup key |
| Category | | Decoded category name, falling back to the numeric value |
| Title Color | | Swatch from extra payload, if present |
| Title | | English loc text, falling back to Korean; colored when a payload color exists |
| Title Requirements | | English loc text, falling back to Korean |
| Special | | `True` when the title has a non-default payload color or inline title PAColor |
| Effect | | Extra payload effect/aura string, if present |

## Notes

- The previously unknown `?` layouts are now explained by `key_count` values 4
  and 6.
- The old `u32_14`, `u32_18`, and similar columns can be UTF-16 text fragments,
  not structured integers.
- `titlecategory.bss` is not needed for category display; `title.dbss` carries
  the category after the requirement string.

## Open Questions

### Extra Payload Parameters

The color value and optional aura/effect name are now decoded, but several
earlier integers in the extra payload are still unresolved.

### Normal Title Name Color

For titles without an extra color payload, the default visible color is still
not stored as a per-record RGB value in `title.dbss`. Disproven candidates:

- Requirement `_PA_COLOR_MARKER`
- `style_or_title_len` alone
- A fixed early `u32` field after the title text

Likely sources still to investigate:

- client-side title color table
- UI scripts / title rendering logic
- another DBSS file related to title grade/type/color
- implicit default color chosen by title category/UI code
