# title.dbss Format

## Purpose

Stores per-title metadata and embedded Korean title/requirement payload data.

It does **not** appear to directly store the final visible title color as a simple RGB value. Earlier assumptions that `style_value`, `_PA_COLOR_MARKER`, or fixed fields like `u32_20` directly map to the title name color were disproven by matching rows with different visible colors.

## Companion Files

- `titleoffset.dbss` — required. Provides `title_id -> (offset, size)` block lookup.

## Offset File Format: titleoffset.dbss

| Offset           | Type | Description              |
| ---------------- | ---- | ------------------------ |
| `+0x00`          | u32  | Entry count              |
| `+0x04 + n*0x0C` | u32  | Title ID                 |
| `+0x08 + n*0x0C` | u32  | Offset into `title.dbss` |
| `+0x0C + n*0x0C` | u32  | Block size               |

## Layout Detection

Layout is not determined by a dedicated layout ID. Detect it by checking where the `title_id` appears in the block.

| Condition                       | Layout |
| ------------------------------- | ------ |
| `u32(block + 0x08) == title_id` | A      |
| `u32(block + 0x0C) == title_id` | B      |
| `u32(block + 0x10) == title_id` | C      |

## Observed Layout A

Most inspected titles use Layout A.

| Offset   | Type   | Name                  | Description                                                                                                                                 | Confidence |
| -------- | ------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| `+0x00`  | u32    | unknown/version-ish   | Usually `1` in observed rows                                                                                                                | Medium     |
| `+0x04`  | u32    | group/hash/category?  | Repeats across related title groups, but not enough to define color                                                                         | Low        |
| `+0x08`  | u32    | title_id              | Matches offset entry and loc string id                                                                                                      | High       |
| `+0x0C`  | u32    | style_value/category? | Small enum-like value. Not final color.                                                                                                     | Medium     |
| `+0x10`  | u32    | unknown               | Often `0` in observed rows                                                                                                                  | Low        |
| `+0x14+` | varies | payload               | Variable payload. Often begins raw UTF-16 title text / text fragments / PA tags. Do not treat all later `u32_*` reads as structured fields. | High       |

## Observed Layout B

| Offset   | Type   | Name                  | Description                                       |
| -------- | ------ | --------------------- | ------------------------------------------------- |
| `+0x00`  | u32    | unknown               | First field                                       |
| `+0x0C`  | u32    | title_id              | Matches offset entry and loc string id            |
| `+0x10`  | u32    | style_value/category? | Small enum-like value. Not final color by itself. |
| `+0x14+` | varies | payload               | Variable payload                                  |

## Observed Layout C

| Offset   | Type   | Name                  | Description                                       |
| -------- | ------ | --------------------- | ------------------------------------------------- |
| `+0x00`  | u32    | unknown               | First field                                       |
| `+0x10`  | u32    | title_id              | Matches offset entry and loc string id            |
| `+0x14`  | u32    | style_value/category? | Small enum-like value. Not final color by itself. |
| `+0x18+` | varies | payload               | Variable payload                                  |

## Important Correction: PAColor Tags

`title.dbss` blocks can contain UTF-16 PA tags such as:

```text
<PAColor0xfff32200>Title Requirement<PAOldColor>
```

Observed behavior indicates these tags are usually inline formatting for requirement/body text, **not the final color of the title name**.

The common value:

```text
fff32200
```

appears as a default-ish requirement text marker and should not be treated as title name color.

## Important Correction: style_value

`style_value` is not enough to identify title name color.

Counterexample observed:

| Title ID | Title                      | style_value | Visual Result |
| -------- | -------------------------- | ----------- | ------------- |
| `2117`   | The Greatest Guardian      | `7`         | Special color |
| `44`     | Stoneback Crab Artisan     | `7`         | Normal blue   |
| `45`     | Stoneback Crab Philosopher | `7`         | Normal blue   |

So `style_value` is likely a category/display class/progression grouping, not a direct color enum.

## Important Correction: Fixed u32 Fields After +0x14

Several later `u32_*` values are actually UTF-16 text interpreted as integers.

Examples:

| Raw u32      | UTF-16 fragment |
| ------------ | --------------- |
| `0x006F0043` | `Co`            |
| `0x006F006C` | `lo`            |
| `0x00300072` | `r0`            |
| `0x00430041` | `AC`            |
| `0x00780030` | `x0`            |

These are fragments of strings such as:

```text
<PAColor0x...
```

For debugging, find the first `_PA_COLOR_MARKER` offset and avoid treating fields at or after that offset as structured numeric fields.

## Current Best Interpretation

```text
fixed header:
  +0x00 unknown/version-ish
  +0x04 group/category/hash-ish
  title_id at layout-dependent offset
  style_value immediately after title_id
  +next field often 0

payload:
  Korean title text / requirement text / PAColor markup / other variable data
```

## Recommended Parser Behavior

1. Use `titleoffset.dbss` to slice blocks.
2. Detect layout by title ID position.
3. Read `style_value`, but label it as `Style?/Category?`.
4. Look up English name/requirement from `languagedata_en.loc`:
   - Name: `str_type=1, str_id1=title_id, str_id4=0`
   - Requirement: `str_type=1, str_id1=title_id, str_id4=1`
5. Strip PA tags from English requirement text for readability.
6. Preserve/debug PA tags separately.
7. Treat `+0x14+` as variable payload, not fixed fields.
8. Add a first-PAColor-offset column to avoid misreading UTF-16 text as integers.

## Notes

- `Darkness` and `II` can share `style_value`, `u32_04`, and `u32_20`, yet appear visually different in-game.
- Short titles like `II`, `IV`, `VI` cause fields like `u32_14` to decode as UTF-16 title characters.
- `TITLEBUFFLIST.DBSS` was investigated but turned out to describe title collection bonuses, not per-title name colors.

## Open Questions

### Title Name Color

The visible title name color has not been proven to come from `title.dbss` alone.

Disproven candidates:

- `_PA_COLOR_MARKER` in `title.dbss` — appears to be requirement/body text formatting.
- `style_value` alone — same style can produce different visible title colors.
- `u32_04` alone — same group/hash can produce different visible title colors.
- `u32_20` alone — same key can show different visible colors, and later fields may be text/payload depending on block.
- `u32_14` — often just raw untranslated UTF-16 title text.

Likely sources still to investigate:

- client-side title color table
- UI scripts / title rendering logic
- another DBSS file related to title grade/type/color
- hardcoded handling by title ID or title group
