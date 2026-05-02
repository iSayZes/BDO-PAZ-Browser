# languagedata_en.loc Format

## Purpose

Stores all localized strings for the game, including title names and requirements.

## File Layout

The file is **zlib-compressed**:

| Offset | Type | Description                        |
| ------ | ---- | ---------------------------------- |
| +0x00  | u32  | Header / uncompressed size hint    |
| +0x04  | ...  | zlib-compressed record stream      |

Decompress with: `zlib.decompress(raw[4:])`

## Record Structure

Each record in the decompressed stream:

| Offset | Type   | Name     | Description                    | Confidence |
| ------ | ------ | -------- | ------------------------------ | ---------- |
| +0x00  | u32    | str_size | String length in UTF-16 chars  | High       |
| +0x04  | u32    | str_type | String type identifier         | High       |
| +0x08  | u32    | str_id1  | Primary ID (= title_id)        | High       |
| +0x0C  | u16    | str_id2  | Secondary ID                   | Medium     |
| +0x0E  | u8     | str_id3  | Unknown                        | Low        |
| +0x0F  | u8     | str_id4  | Unknown                        | Low        |
| +0x10  | UTF-16 | text     | String data (`str_size * 2` B) | High       |
| ...    | u32    | padding  | Usually 0x00000000             | High       |

Next record starts at: `+0x10 + str_size * 2 + 4`

## Important Types

| str_type | Meaning                           |
| -------- | --------------------------------- |
| 1        | Title names + requirements        |
| 0        | General strings                   |
| 37/38/39 | Other systems (ignore for titles) |

## Notes

- The same `str_id1` can appear multiple times with `str_type=1`:
  one entry for the title name, one for the requirement text.
- `str_id1` matches `title_id` in `title.dbss` and `titleoffset.dbss`.
- The file is located on disk at `<paz_root_parent>/ads/languagedata_en.loc`
  (one level above the PAZ folder) and is pre-loaded by the browser as a companion for all handlers.

## Example

str_type: 1, str_id1: 218, text: "Mudskipper Enthusiast"

## Open Questions

- What do `str_id3` and `str_id4` represent?
- Whether `str_id2` encodes a sub-type or sequence index
