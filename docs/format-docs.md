# Writing Format Docs

A format doc in `docs/file-formats/` describes the bytes of one file so that a
script can check it: every byte belongs to a field, every field has a type
with a size, and the sizes add up to the file. `PAZ-Parser/format_docs/`
reads the docs and `PAZ-Parser/tests/test_format_docs.py` runs its checks on
every doc that has a `## Layout` section. Start a new doc from
[`_template.md`](file-formats/_template.md).

## Doc Order

| Section             | Content                                                                 |
| ------------------- | ----------------------------------------------------------------------- |
| Title               | ``# `file.bss` Format``                                                 |
| `## Purpose`        | What the file stores, in prose; no example block                        |
| `## Versions`       | Two markers; the doc check writes the clients, sizes and coverage between them |
| `## Companion Files`| The files the handler loads, or a sentence saying there are none        |
| `## Layout N`       | One per known layout, newest first                                      |
| Topic sections      | Enums, conditions, tables of observed values                            |
| `## Notes`          | Facts that fit no table                                                 |
| `## Open Questions` | One `###` per question; omitted when empty                              |
| `## In-Game Checks` | One `###` per check; omitted when empty                                 |

A format doc describes the bytes only. Which fields a handler shows as
columns is decided in the handler.

## Layouts

A file whose layout changed between clients keeps every known layout. Layout
1 is the oldest; a new layout takes the next number, and the sections go
newest first, so the current layout is always the first one.

- The newest layout is written in full and has a `### File Layout`.
- An older layout lists only the structures that differ from the next newer
  layout. A structure it does not list is the same as there.
- A field keeps one name in every layout. A name with an offset in it, like
  `unknown_04`, keeps the newest layout's offset.
- A doc that shares another doc's layout says so in one sentence,
  ``Same layout as [`newquest.bss`](newquest_bss.md)``, and has no layout
  sections of its own.

Nobody writes a client number into a layout heading: the doc check finds out
which clients each layout fits and writes it into `## Versions`.

## Structures

Inside a layout, each `###` heading is one structure and holds one layout
table. The heading names the structure and gives its size:

| Heading                                        | Use                                                  |
| ---------------------------------------------- | ---------------------------------------------------- |
| `### File Layout`                              | The top-level table of the main file                 |
| ``### `companionoffset.dbss` ``                | The top-level table of a companion file              |
| `### Row (24 bytes)`                           | A structure of fixed size                            |
| `### Row (variable: 56 bytes + condition text)`| A structure with strings, counted arrays or optional fields; the number is the fixed part, the text after `+` is free |
| ``### Payload (variable: 189 bytes, size from `petskilloffset.dbss`)`` | A structure whose size only an offset file gives |

The fixed part of a variable structure counts every field of fixed size and
the count of a single `str8` or `str16` (8 bytes) or `pstr` (5 bytes). A
counted array, a conditional field and a variable structure count 0:
`alchemystonechange.dbss` Row is 36 bytes of head, the 8-byte count of
`condition` and a 12-byte tail, so `(variable: 56 bytes + condition text)`.

Structure names are unique within a layout. A layout table starts with the
columns `Offset | Type | Field` and ends with `Notes`; columns in between
(`Source`) are allowed. Tables whose first column is not `Offset` are not
layout tables and the check leaves them alone.

## Types

| Type                                | Meaning                                                    | Size |
| ----------------------------------- | ---------------------------------------------------------- | ---- |
| `u8` `i8` `u16` `i16` `u32` `i32` `u64` `i64` `f32` `f64` | Little-endian numbers             | 1, 2, 4 or 8 |
| `bytes[N]`, `bytes[field]`          | Bytes with no inner layout                                 | N, or the field's value |
| `char[N]`, `char[field]`            | ASCII characters, e.g. `char[4]` for `PABR`                | N, or the field's value |
| `char16[N]`, `char16[field]`        | UTF-16LE code units                                        | 2 x N, or 2 x the field's value |
| `str8`                              | u64 count, then that many ASCII bytes                      | 8 + count |
| `str16`                             | u64 count, then that many UTF-16LE code units              | 8 + 2 x count |
| `pstr`                              | PABR string-table entry: u8 `is_wide`, u32 byte length, then UTF-16LE (`1`) or UTF-8 (`0`) bytes | 5 + length |
| `T[N]`, `T[field]`                  | Several numbers of type T, e.g. `u32[3]`, `u16[list_count]` | count x size of T |
| `T[N][M]`, `T[field][M]`            | Two-dimensional array, outer count first                   | N x M x size of T |
| `Name`                              | One structure from a `### Name (...)` heading              | its size |
| `Name[N]`, `Name[field]`            | Several of them                                            | count x its size |
| `Name[..field]`, `Name[..end]`      | Repeated up to the offset a field holds, or to the end of the enclosing structure | the bytes up to there |
| `Name[while field != V]`            | Repeated up to the first one whose `field` is `V`, that one excluded | count x its size |
| `bytes[rest]`                       | The bytes left in a structure whose size comes from an offset file | the rest |
| `T if field = V`, `T if field != V` | Present only when the condition holds; `size` names the structure's size from its offset file | T's size, or 0 |

A count field named in `[field]` or `if field` is an earlier field of the
same structure. A u32 count followed by a u32 `0` is a u64 count: write
`str8` or `str16`. A count that does not sit right before its text is two
rows: the count as its own field, then `char[field]` or `char16[field]`. A
conditional row with the opposite condition right after it is a union.

## Offsets

| Offset          | Counts from                                                     |
| --------------- | --------------------------------------------------------------- |
| `+0xNN`         | The start of the structure                                      |
| `field+0xNN`    | The end of `field`, the last variable-size field before the row |
| `end-0xNN`      | The end of a structure whose size comes from an offset file     |
| `EOF-0xNN`      | The end of the file, in `### File Layout`                       |

Offsets follow on with no gap and no overlap: each offset is the previous
offset plus the previous size. Bytes nobody understands get a row of their
own, a `bytes[N]` field named `unknown_*`.

## Field Names

One snake_case name per Field cell, unique within its structure.

| Form                                  | Counts as | Rule                                                              |
| ------------------------------------- | --------- | ----------------------------------------------------------------- |
| A name for the meaning                | Known     | Only once the meaning is confirmed                                |
| `unknown_<hex>`                       | Unknown   | 2 or more lowercase hex digits, the offset in the structure; also for fields that are always zero |
| `unknown_<words>`                     | Unknown   | A field without a fixed offset (`unknown_end`, `unknown_after_<field>`, `unknown_tail_<hex>`) or a role the bytes show (`unknown_str_ref` indexes the string table), never a guessed meaning |
| `padding_<hex>`                       | Known     | Proven filler; Notes cite the 2016 PDB struct or the alignment    |
| `<field>_dup`, `<field>_dup2`         | Known     | A copy of `<field>`, which exists in the same structure           |
| `zero`                                | Known     | Only the u32 that ends the PABR string-table trailer              |
| `<name>_kr`                           | Known     | Inline Korean text                                                |

The check rejects a name that states a value in place of a meaning
(`reserved`, `pad0`, `const1`, `zero_a`, `flag_17`), a bare `unknown`, an
`_ko` suffix, upper-case hex, and a cell holding more than one name.

## Format Docs Wiki

The Wiki workflow (`.github/workflows/wiki.yml`) publishes the docs as a
static site on GitHub Pages. It runs `build_wiki.py` on every push to `main`
that changes `docs/`, `PAZ-Parser/wiki/` or `PAZ-Parser/format_docs/`, so
the site shows the released docs. `python build_wiki.py` builds the same
site into `_site/` for a local preview. The generator is
`PAZ-Parser/wiki/`; the site holds:

| File                | Content                                                                 |
| ------------------- | ----------------------------------------------------------------------- |
| `index.html`        | Every doc with its description, known share, open questions and in-game checks, searchable and sortable |
| `<doc>.html`        | One page per doc, e.g. `buffsimply_bss.html`; a converted doc shows its layouts as tabs, each structure with a byte map and its field table |
| `formats.js`        | The doc list both page kinds read                                       |
| `static/`           | The CSS and JS, copied from `PAZ-Parser/wiki/static/`                   |

The known share counts the fixed-size fields of the newest layout, each
structure once, so a row type counts the same as the header. A doc not
converted yet shows as written and has no share. Links between docs go to
their pages, links to other repo files to GitHub, and `#section` links work
as on GitHub. The descriptions and file lists come from
[`documented-formats.md`](documented-formats.md). The index's Documented
tile counts its `.bss` and `.dbss` rows against the game totals in the
README's Supported Formats lines, which the pre-commit hook keeps current
from a PAZ folder.

## Versions

```markdown
## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->
```

Until the doc check reads game files, the section holds only the markers.
