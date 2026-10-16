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
newest first, so the current layout is always the first one. A layout
older than Layout 1, found later in an older client, becomes Layout 1 and
the others move up by one; the doc check then rewrites Versions for them.

- The newest layout is written in full and has a `### File Layout`.
- An older layout lists only the structures that differ from the next newer
  layout. A structure it does not list is the same as there. A structure
  only the older layout has is allowed when one of its own structures uses
  it, and a ``### `x.dbss` `` table for a file only that client fills is
  always allowed.
- In an older layout, `unknown_after_<field>` and `<field>_dup` may name a
  field the same structure has in a newer layout, so a block keeps its name
  when the field it follows did not exist yet.
- A field keeps one name in every layout. A name with an offset in it, like
  `unknown_04`, keeps the newest layout's offset.
- A doc that shares another doc's layout says so in one sentence at the
  start of a line, ``Same layout as [`newquest.bss`](newquest_bss.md)``,
  and has no layout sections of its own. The check and the wiki read the
  linked doc's layouts for it; the linked doc must have layouts of its own.
  A link with a `#section` anchor (a companion only) does not count: such a
  doc writes the companion table into its own layout.

Nobody writes a client number into a layout heading: the doc check finds out
which clients each layout fits and writes it into `## Versions`.

## Structures

Inside a layout, each `###` heading is one structure and holds one layout
table. The heading names the structure and gives its size:

| Heading                                        | Use                                                  |
| ---------------------------------------------- | ---------------------------------------------------- |
| `### File Layout`                              | The top-level table of the main file                 |
| ``### `companionoffset.dbss` ``                | The top-level table of a companion file              |
| `### Row (24 bytes)`, `### Entry (1 byte)`     | A structure of fixed size                            |
| `### Row (variable: 56 bytes + condition text)`| A structure with strings, counted arrays or optional fields; the number is the fixed part, the text after `+` is free |
| ``### Payload (variable: 189 bytes, size from `petskilloffset.dbss`)`` | A structure whose size only an offset file gives |

The fixed part of a variable structure counts every field of fixed size and
the count of a single `str8` or `str16` (8 bytes) or `pstr` (5 bytes). A
counted array, a conditional field and a variable structure count 0:
`alchemystonechange.dbss` Row is 36 bytes of head, the 8-byte count of
`condition` and a 12-byte tail, so `(variable: 56 bytes + condition text)`.

A structure sized by an offset file needs that file's ``### `x.dbss` ``
table in its layout or a newer one, and a row structure there with one field
named `offset` or `*_offset` (where the structure starts in the main file)
and one named `size` or `*_size` (its length): `petskilloffset.dbss` Offset
Row has `data_offset` and `data_size`. The check reads each structure's size
from the row whose offset is its start.

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
| `T[N][M]`, `T[field][field]`        | Two-dimensional array, outer count first; each count a number or a field | N x M x size of T |
| `Name`                              | One structure from a `### Name (...)` heading              | its size |
| `Name[N]`, `Name[field]`            | Several of them                                            | count x its size |
| `Name[..field]`, `Name[..end]`      | Repeated up to the offset a field holds, or to the end of the enclosing structure; in a top-level table `..end` stops at the first `EOF-` row | the bytes up to there |
| `Name[while field != V]`            | Repeated up to the first one whose `field` is `V`, that one excluded; `field` is a field of `Name` | count x its size |
| `bytes[rest]`                       | The bytes left in a structure whose size comes from an offset file | the rest |
| `bytes[scan]`                       | Bytes whose end only a scan finds, in a structure with no size from outside; named `unknown_*`, the scan in Notes, later rows count from it | what the scan finds |
| `T if field = V`, `T if field != V` | Present only when the condition holds; `size` names the structure's size from its offset file | T's size, or 0 |
| `T if field ^= V`, `T if field !^= V` | Present only when the string `field` starts (or does not start) with `V` | T's size, or 0 |
| `T if a ^= V or b = ""`             | Clauses joined by `or`: present when any of them holds; `""` is the empty string | T's size, or 0 |

A count field named in `[field]` or `if field` is an earlier field of the
same structure. In a top-level table, `[..field]` may also name a later
field at `EOF-0xNN`: a reader takes it before the body, as for the PABR
`table_start`. A u32 count followed by a u32 `0` is a u64 count: write
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
| `unknown_<field>_<hex>`               | Unknown   | A field at `field+0xNN` after a variable-size field, with that offset (`unknown_effects_06`) |
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
that adds, changes or deletes a doc in `docs/file-formats/`, or changes
`docs/documented-formats.md` or the generator (`PAZ-Parser/wiki/`,
`PAZ-Parser/format_docs/`, `build_wiki.py`), so the site shows the released
docs. `python build_wiki.py` builds the same
site into `_site/` for a local preview. The generator is
`PAZ-Parser/wiki/`; the site holds:

| File                | Content                                                                 |
| ------------------- | ----------------------------------------------------------------------- |
| `index.html`        | Every doc with its description, known share, open questions and in-game checks, searchable and sortable |
| `<doc>.html`        | One page per doc, e.g. `buffsimply_bss.html`; a converted doc shows its layouts as tabs, each structure with a byte map and its field table |
| `formats.js`        | The doc list both page kinds read                                       |
| `static/`           | The CSS and JS, copied from `PAZ-Parser/wiki/static/`                   |

A doc page's Versions card shows each layout's clients and a known/unknown
bar from its Versions tables, and the layout tabs name the clients. The
known share in the index and the sidebar counts the newest layout's bytes in
the game files of the client Versions names, every record included. A doc
without Versions counts the fixed-size fields of its newest layout, each
structure once; the share's tooltip says which of the two it is. A doc not
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

`check_docs.py` writes the section. It reads the doc's files from a PAZ
folder: the rows of [`documented-formats.md`](documented-formats.md) that
link to the doc, and every file a ``### `x.dbss` `` heading names. It walks
them by each layout, newest first, and takes the first layout every file
walks to its last byte by. Two tables follow, one row per layout per file:

| Table    | Columns                                                                 |
| -------- | ----------------------------------------------------------------------- |
| Sizes    | Layout, Clients, Checked (the client the numbers come from), File, Bytes, Records (per repeated structure), Row bytes (of the most frequent structure) |
| Coverage | Layout, File, Known and Unknown bytes over the whole file, every instance of every field counted |

- A client range only widens: each check adds its client to the layout it
  fits, and a layout's row stays once a client has fit it. The newest layout
  reads `<first client> and later`, an older one `<first> to <last>`.
- Sizes and coverage come from the newest client checked for that layout;
  an older client never overwrites them.
- A doc whose layout holds `bytes[scan]` cannot be walked and keeps its
  markers only.

| Command                                              | Checks                                                      |
| ---------------------------------------------------- | ----------------------------------------------------------- |
| `python check_docs.py --staged`                      | The docs in the commit; the pre-commit hook runs this       |
| `python check_docs.py --all`                         | Every doc in the layout format                              |
| `python check_docs.py buffsimply_bss.md`             | Named docs                                                  |
| `python check_docs.py --all --paz-folder DIR --client N` | Another client's folder, by hand, with its real client number |
| `python check_docs.py --all --docs-only`             | The doc rules only, no game files                           |
| `python check_docs.py buffsimply_bss.md --no-write`  | Which layout each doc's files fit; Versions stay as they are |

Without `--paz-folder` the check reads the PAZ folder last opened in the
app, the live client, and names it by the number its `.meta` holds. A
`.meta` that says `1` (a private server or a leaked client) needs
`--client`. The command exits 1 when a doc breaks a rule, when a client's
files fit no layout (it names the layout, structure, field and offset where
the walk broke), or when it rewrote a Versions section; the hook then stops
the commit for a review and `git add`. A staged handler `parser.py` whose
doc is not staged gets a warning, not a stop.
