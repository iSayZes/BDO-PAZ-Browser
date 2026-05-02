# languagedata_en.loc Format

## Purpose

Stores all localized strings for the game, including title names and requirements.

## File Layout

The file is **zlib-compressed**:

| Offset | Type | Description                     |
| ------ | ---- | ------------------------------- |
| +0x00  | u32  | Header / uncompressed size hint |
| +0x04  | ...  | zlib-compressed record stream   |

Decompress with: `zlib.decompress(raw[4:])`

## Record Structure

Each record in the decompressed stream:

| Offset | Type        | Name     | Description                                                                |
| ------ | ----------- | -------- | -------------------------------------------------------------------------- |
| +0x00  | u32         | str_size | Length of the string (UTF-16 code units, excluding trailing padding/nulls) |
| +0x04  | u32         | str_type | String type identifier                                                     |
| +0x08  | u32         | str_id1  | Primary ID — main lookup key (matches title_id, knowledge_id, etc.)        |
| +0x0C  | u16         | str_id2  | ID part 2 — secondary component of the compound ID                        |
| +0x0E  | u8          | str_id3  | ID part 3 — tertiary component of the compound ID                         |
| +0x0F  | u8          | str_id4  | ID part 4 — selects sub-field within the record (e.g. name vs requirement) |
| +0x10  | UTF-16LE[]  | text     | String data (`str_size` UTF-16 code units)                                 |
| ...    | UTF-16LE[2] | padding  | Always 2 extra UTF-16 code units (4 bytes), typically `0x0000 0x0000`      |

Next record starts at: `+0x10 + str_size * 2 + 4`

## Important Types

| str_type | Meaning                                                                      |
| -------- | ---------------------------------------------------------------------------- |
| 0        | General strings                                                              |
| 1        | Title names + requirements                                                   |
| 2        | Skill names?                                                                 |
| 4        | Territory names                                                              |
| 5        | Buff text?                                                                   |
| 6        | Npcs?                                                                        |
| 7        | Zodiac sign data — `str_id1` = zodiac_id (1–12), `str_id4` selects sub-field |
| 8        | Mount skills?                                                                |
| 9        | Knowledge category (group) names — `str_id1` = node_id                       |
| 34       | Knowledge entry names — `str_id1` = knowledge_id / entry_id                  |
| 37/38/39 | Other systems                                                                |

### Type 1 sub-fields (`str_id4`)

| str_id4 | Meaning           |
| ------- | ----------------- |
| 0       | Title name        |
| 1       | Title requirement |

### Type 7 sub-fields (`str_id4`)

| str_id4 | Meaning           | Example                               |
| ------- | ----------------- | ------------------------------------- |
| 0       | Sign name         | `"Hammer"`                            |
| 1       | Trait description | `"Brave, Conservative, Hot-Blooded."` |

## Notes

- All four ID fields together form a compound identifier; `str_id1` is the primary lookup key.
- The same `str_id1` can appear multiple times with `str_type=1`:
  one entry for the title name (`str_id4=0`), one for the requirement text (`str_id4=1`).
- `str_id1` matches `title_id` in `title.dbss` and `titleoffset.dbss`.
- The file is located on disk at `<paz_root_parent>/ads/languagedata_en.loc`
  (one level above the PAZ folder) and is pre-loaded by the browser as a companion for all handlers.

## Example

str_type: 1, str_id1: 218, text: "Mudskipper Enthusiast"

## Open Questions

- What values does `str_id3` take in practice — whether it's always 0 or carries meaningful data
- Whether `str_id2` encodes a sub-type, sequence index, or part of a 6-byte composite key with id3/id4
- Whether `str_id4` has sub-field semantics in types other than 1 and 7
