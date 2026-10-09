# Handler Guide

This guide explains how custom preview handlers should be structured, loaded, and registered.

## Loader Rules

The browser loads handlers from the `handlers/` folder at startup. Importing
`bdo_preview` registers nothing: each entry point calls
`load_plugins(BUNDLED_HANDLERS_DIR)` (`bdo_app.main()`, `bench.cli.main()` and
`pytest_sessionstart()` in `conftest.py`), so the Windows exe can pass an
updated handler pack instead.

Only files matching these rules are auto-loaded:

- Must be a `.py` file directly inside `handlers/`
- Must **not** start with `_`
- Each loaded file may register one or more handlers with `register_handler(...)`

Example loaded files:

```text
handlers/
├── dbss_handler.py
├── texture_handler.py
└── model_handler.py
```

Example ignored files/folders:

```text
handlers/
├── _dbss/
├── _common/
├── _helper.py
└── README.md
```

Folders and files starting with `_` are treated as private implementation details.

## Recommended Folder Structure

Use one public entry file per format, and keep implementation code in private folders.

```text
handlers/
├── dbss_handler.py                 # Public entry file, auto-loaded
│
├── _dbss/                          # Private DBSS package
│   ├── __init__.py
│   ├── registration.py             # Registers DBSS handlers
│   │
│   ├── common/                     # DBSS-specific helpers
│   │   ├── __init__.py
│   │   ├── binary.py
│   │   ├── html.py
│   │   └── constants.py
│   │
│   ├── titleoffset/
│   │   ├── __init__.py
│   │   └── handler.py
│   │
│   ├── title/
│   │   ├── __init__.py
│   │   └── handler.py
│   │
│   └── titlebuff/
│       ├── __init__.py
│       └── handler.py
│
└── _common/                        # Shared helpers for all formats
    ├── __init__.py
    └── loc.py
```

When adding another format later:

```text
handlers/
├── dbss_handler.py
├── texture_handler.py
├── model_handler.py
│
├── _dbss/
├── _texture/
├── _model/
└── _common/
```

## Public Entry File

A public entry file should stay small.

Example:

```python
# handlers/dbss_handler.py

from _dbss.registration import register_dbss_handlers

register_dbss_handlers()
```

The entry file exists so the plugin loader can discover the handler package.

## Registration File

Group all registrations for one format in a registration module.

```python
# handlers/_dbss/registration.py

from bdo_preview import register_handler

from .titleoffset.handler import title_offset_handler
from .title.handler import TitleDbssHandler
from .titlebuff.handler import TitleBuffListHandler, title_buff_list_offset_handler


def register_dbss_handlers() -> None:
    register_handler("titleoffset.dbss", title_offset_handler())
    register_handler("title.dbss", TitleDbssHandler())
    register_handler("titlebufflistoffset.dbss", title_buff_list_offset_handler())
    register_handler("titlebufflist.dbss", TitleBuffListHandler())
```

Offset companions register a factory call instead of a class (see
[Offset Tables](#offset-tables)).

## Registration Keys

Handlers can be registered by exact filename or by extension.

```python
register_handler("title.dbss", TitleDbssHandler())
register_handler(".dbss", GenericDbssHandler())
```

Resolution order:

1. Exact filename match
2. Extension fallback
3. Raw hex fallback

Exact filename handlers should be preferred for known formats.

Extension handlers are useful for generic fallback previews.

The **Show only handled tables** setting keeps a file in the tree when
`is_handled_file()` (`bdo_preview.py`) finds a registered key for it by the
same order, built-in text and image views aside. A new handler shows up there
with no second list to update. An extension key such as `.dbss` would count
every file of that extension as handled, so register known formats by name.

## Handler Template

All parsed-view handlers must implement `get_records()` and `render_records_page()`.

- `get_records()` parses the binary and returns all records as plain dicts (no HTML). The base class caches the result per data object in `all_records()` (through `_data_cache`), so paging, sorting, tab search, CSV export and the CLI all reuse the same parse without re-reading the file. Call `all_records()`, not `get_records()`, from outside the handler. In the app, `all_records()` may return records from the disk cache instead, see [Parsed Table Cache](#parsed-table-cache).
- `render_records_page()` converts one page of records into an HTML fragment.
- `sortable_fields()` opts the table into sorting, and `default_sort()` picks the order it opens in, see [Sortable Columns](#sortable-columns).

```python
# handlers/_example/myfile/handler.py

from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from _common.html import Column, e, sort_keys, table


_COLUMNS = [
    Column("ID",   "num", sort_key="id"),
    Column("Name",        sort_key="name"),
]


class MyFileHandler(PreviewHandler):
    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(_COLUMNS)

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/myindex.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [{"id": r.id, "name": r.name} for r in _parse(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} records"
        rows = [[e(r["id"]), e(r["name"])] for r in slice_]
        return table(meta, _COLUMNS, rows)
```

### Sortable Columns

Parsed tables are paged, so the server sorts the full record list and then
renders the requested page. The browser never sorts the rows on screen.

A handler opts in with two pieces:

1. Give each sortable `Column` a `sort_key`: the record field (from
   `get_records()`) the column sorts by. Use the raw value, not the rendered
   text: `duration_ms`, not the `1h 30m` string; `offset`, not `0x0000ABCD`.
2. Return `sort_keys(columns)` from `sortable_fields()`. It keeps column
   order, and the API rejects any field not in it.

The column labels come from the handler's `lang/*.json`, so build the list in a
`_columns()` method and use it in both places. Index the table directly
(`cols["buffId"]`): `en.json` holds every key, and a missing one should fail
rather than show a stale English default:

```python
def _columns(self) -> list[Column]:
    cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
    return [
        Column(cols["buffId"], "num", sort_key="buff_id"),
        Column(cols["icon"], sort_key="icon_path"),
    ]

def sortable_fields(self) -> tuple[str, ...]:
    return sort_keys(self._columns())
```

Columns without a `sort_key`, and plain `(label, css_class, extra_attrs)`
tuples, render as normal headers you cannot click. A handler that declares no
fields shows no sortable headers at all.

#### Default Sort

A file without a saved sort opens sorted by `default_sort()`: the first
sortable column, descending. Since the ID column comes first, most tables
open with the highest ID on top, and the header shows the sort like a
clicked one. The default is never saved, so a later change to it reaches
every file that has no saved sort.

Override `default_sort()` to open on another field from `sortable_fields()`,
or return `None` to open in `get_records()` order. Use `None` only when no
single field gives the order: `ui_skillgroup_*.bss` keeps its skill window
order, which spans class, tab, card column, row and column.

```python
def default_sort(self) -> TableSort | None:
    return TableSort("duration_ms", SORT_ASC)
```

A handler that sorts in `get_records()` (`stringtable.bss` by key hash,
`skill.dbss` by skill key) keeps that sort: it sets the order of equal values
under the default sort, of CSV export and of `browser.py --records` and
`--render`.

The default sort runs on every open, so a page-at-a-time handler should sort
its first column from its index (see below). On the fixtures it adds under
50 ms to every table, and about 0.25 s to a 1.38-million-row LOC file.

Picking the field behind a column:

- **Derived cells get their own field.** When a cell is built at render time (a
  LOC name with a Korean fallback, a label from a lookup table, an icon path
  resolved from an ID), compute it once in `get_records()`, store it on the
  record and render from that field. The sort and the cell then agree, and the
  logic lives in one place. `title.dbss` stores `title`, `requirement`,
  `category` and `is_special` this way.
- **Text in the user's language, one column.** A text column shows the loaded
  LOC text (the language picked in settings) and falls back to the inline
  Korean only when LOC has no row: `character_name(id) or record["name_kr"]`.
  Keep the raw `*_kr` field on the record, but never render it as its own
  column or label a column `(EN)` / `(KR)`. Never find LOC text by searching
  for an English phrase, since other languages miss it. Cover the column with
  `UserLanguageTest`.
- **Columns that come and go stay declared.** A LOC name column that only
  renders with LOC loaded, or flag columns that only render when a flag is set
  somewhere, still belong in `sortable_fields()`. Otherwise a saved sort on
  them is dropped the first time the file opens without them. Build the list
  with a parameter (`_columns(has_loc)`) and declare the full set:
  `sort_keys(self._columns(has_loc=True))`.
- **Fields that are not on the record** (one entry of a list, say) can still
  sort: override `records_sort_order(records, sort)`, pull the values yourself
  and pass them to `table_sort.sort_order_by_values`. Override this, not
  `_build_sort_order`, so the order stays a function of the records and the
  disk cache can keep it (see [Parsed Table Cache](#parsed-table-cache)).
  `characterspawntype.dbss` sorts its
  `flag_NN` columns this way from each record's `flags` list, so it does not
  add 44 keys to every one of its 24,017 records.
- **Leave list columns unsortable** (quest titles, page titles, value lists).
  They would sort by their string form, which is rarely useful.
- **Store "none" as `None`, not `0`.** When a field uses `0` for "no linked
  item" or "no next tier" and the cell shows a dash, set it to `None` in
  `get_records()` (`record["item_id"] = record["item_id"] or None`). A `0`
  would sort first ascending even though the cell looks empty; `None` sorts
  last both ways and exports as an empty CSV cell. Keep the parser returning
  the raw `0` and convert only in the handler. A `0` that the cell shows as
  `0` (a count, a `+0` level, an enum value) stays `0`.
- **Sort a derived cell by what it shows.** When a cell's dash depends on more
  than its own field (a reward shown as `-` because it repeats the one before)
  or the field means different things per row, add a sort field that holds
  the shown number or `None`, and keep the raw field for export:
  `energy_reward_2_amount` in `mentaltheme.dbss`, `effect_sort_values()` in
  `plantworkerpassiveskill.bss`. `tests/test_empty_cells.py` enforces both rules.

Ordering rules (`table_sort.py`):

- Numbers sort before text, and text ignores case. Anything else (lists,
  tuples) sorts by its string form.
- Empty values (`None`, blank strings, empty lists, NaN) go last in both
  directions.
- The sort is stable, so equal values keep their file order.

Clicking a new column sorts it ascending. Clicking the active column flips the
direction. Both jump to page 1, and paging keeps the sort. The sorted header
shows an arrow for its direction and keeps the header hover colour. While the
sorted page loads, the clicked header shows a spinner, the rows fade (after
120 ms, so fast sorts do not flicker) and headers ignore further clicks. This
needs no handler code. Each file's sort is saved in `paz_config.json` under `table_sort`, keyed by file name and storing
the field key (`{"buff.dbss": {"field": "duration_ms", "dir": "desc"}}`). The
file reopens sorted. If the handler no longer declares that field, the entry is
dropped and the file opens in its default sort.

The sorted order is cached per field and direction for each loaded file, as a
compact `array("I")` of record indices. Tab search reports its matches as
positions in the sorted view. Changing the sort re-runs an active search
without leaving page 1: the first match is highlighted when it is on that page,
otherwise the counter shows the total and Enter jumps to it. CSV export ignores the sort and writes
`get_records()` in file order, the cheapest path.

Ordering rules have fast paths for all-integer and all-text columns, which
matter at a million rows. Mixed columns fall back to a slower per-row key.

#### Sorting a Page-at-a-Time Handler

By default a sort goes through `get_records()`, which materialises every
record. That is fine for tens of thousands of rows. A handler that overrides
`render_data_page()` to avoid a full parse should override two more methods,
so sorting reads its index instead:

- `_build_sort_order(data, entry, companions, sort)` returns the record
  indices in sorted order. Pull one raw value per record from the index and
  pass them to `table_sort.sort_order_by_values(values, sort.descending)`.
- `render_sorted_page(data, entry, companions, page, page_size, sort)` slices
  `self.sorted_order(...)` for the page and builds only those records.

`handlers/loc_handler.py` is the reference: 1.38 million strings, where a
numeric column sorts in about 0.25 s and the text column in about 1.3 s, then
each page renders in a few milliseconds. If a table renders its own HTML instead of
`table()`, emit its headers with `header_cell(column)` so they carry the
`sortable` class and `data-sort-key`.

`handlers/_dbss/quest/handler.py` does the same over its record index.
Its records carry scripts thousands of characters long, so `_build_sort_order`
parses one row at a time and keeps only the sorted field. Every column sorts in
about 0.5 s on the 19,599-quest fixture, on top of the 0.35 s walk that builds
the index on open. The default sort on `packed_quest_id` reads the IDs straight
from the index instead, so opening the table parses only the first page.

## Unit Tests

Every parsed handler should have a handler-local pytest file named `test_handler.py`.
Place it beside the handler implementation so the format contract stays close to the
code that parses it.

Example:

```text
PAZ-Parser/
├── tests/
│   ├── framework.py          # public re-export for test helpers
│   ├── specs.py              # DeclaredCountTest, TargetTest, SchemaTest, RangeTest, PaFieldTest, UserLanguageTest
│   ├── declared.py           # header_count(), fixed_rows(): counts read from the input
│   ├── case_input.py         # CaseInput: the data file and companion bytes a case parsed
│   ├── models.py             # HandlerCase, HandlerResult
│   ├── runner.py             # run_case(), load_case()
│   ├── fixtures.py           # auto-fetches test inputs
│   ├── fixture_sync.py       # refreshes fixtures when the client changes
│   └── fixtures/             # gitignored cached binaries
└── handlers/
    └── _dbss/
        └── title/
            ├── handler.py
            └── test_handler.py
```

`HandlerCase` describes one handler input and its assertions:

```python
from tests.framework import DeclaredCountTest, HandlerCase, TargetTest, case_id, header_count

CASE = HandlerCase(
    handler_name="title.dbss",
    data_file="title.dbss",
    companion_files={"titleoffset.dbss": "titleoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title", "TitleRequirements"],
    internal_path="gamecommondata/binary/title.dbss",
    tests=[
        DeclaredCountTest(declared=header_count(offset=0, companion="titleoffset.dbss")),
        TargetTest(col="TitleId", value=3, expected={"TitleId": 3}),
    ],
)


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_title_dbss(spec, title_result):
    title_result.check(spec)
```

Available specs:

| Spec | Purpose |
|---|---|
| `DeclaredCountTest` | Checks the parsed row count against the count the input declares. |
| `TargetTest` | Finds records by column value and checks one or more expected rows. |
| `SchemaTest` | Checks required keys exist on every row. |
| `RangeTest` | Checks every value in one column is within a min/max range. `None` (an empty cell) is skipped. |
| `PaFieldTest` | Checks a `pa_fields` text: the plain field is its tagged copy without tags, and some row keeps a game colour. |
| `UserLanguageTest` | Checks no row shows Korean in the given text fields with English LOC loaded, so a missed LOC lookup fails. `None` is skipped. |

`HandlerResult.check(spec)` runs a spec against the parsed records and the input
bytes (`CaseInput`: the data file and its companions by basename). Only
`DeclaredCountTest` reads the bytes: its `declared` callable takes the `CaseInput`
and returns the count the file states about itself. `tests.framework` has two
builders, `header_count(offset, fmt="<I", companion=None)` for a count field and
`fixed_rows(row_size, header_size=0, companion=None)` for a table of fixed rows
that must fill the file exactly. A format whose count needs more (a grouped
offset table, a count spread over blocks) defines its own callable in its test
module, like `_offset_rows` in `journalquest/test_handler.py`. Derive it from
headers and sizes, not by repeating the parser's walk.

Expected dictionaries use subset matching. Tests only check declared keys, so adding
new fields to a handler does not break existing tests.

A test module must not import a `handler.py` directly. Importing it first loads
`bdo_preview`, which loads every registration file, which imports the same
half-loaded handler module again and fails with a circular import; the case then
runs against a fallback handler. Put anything a test calls outside `run_case`
(a text or lease helper, a display table) in its own module next to the handler,
such as `_bss/npcsimply/leases.py`, `_dbss/dialogtext/text.py` or
`_bss/plantworkerpassiveskill/display.py`, and import that instead.

A handler that reads a [lookup index](#lookup-indexes) sees none in a test
unless the case installs it: `lookup_indexes={IndexKind.CHARACTER_ITEM: {2053:
58011}}`. Install only the links the `TargetTest`s check, since the real index
comes from another table; test the builder itself against that table's fixture
(see `test_knowledge_index_holds_every_granting_character` in
`characterstatic/test_handler.py`).

### Tests Must Survive a Game Update

A test fails only when the parser is wrong, never because a patch added,
removed or rebalanced content. The fixtures are cached copies of the installed
client and get refreshed when it is patched (see below), and a patch changes
counts, file order and balance values while the layout stays the same. So assert what stays true:

- **Structure and invariants.** Every record parses, the walk ends exactly at
  the end of the file or at the offset table's last byte, the row count equals
  the count the file or its offset table declares, keys repeat where the
  format repeats them. Derive expected counts from the data, never write the
  current number.
- **Schemas and value domains.** `SchemaTest` for required keys, `RangeTest`
  for enums and bounded fields (`quest_category` in `0`-`19`, flags `0`/`1`).
- **Identity anchors.** `TargetTest` by a stable key on identity fields that a
  patch does not touch: node `1` is Velia, class type `25` is Kunoichi, packed
  quest ID `1050655` splits into chain `2079` / quest `16`, an icon path's
  folder. Look records up by key, not by position.

Avoid:

- Literal row counts: new content changes them. Use `DeclaredCountTest`.
- Record positions (`records[0]`, the last row): inserted records shift every
  later row. Use a keyed `TargetTest` instead.
- Balance values: favor, interest, prices, stats, rewards and costs are
  retuned by patches. Assert their type or range, not the number.
- Totals and "N of M" counts from the current client; put those in the
  format doc as observations, dated, where a patch can make them stale.

Check a converted test against freshly extracted fixtures as well as the
frozen ones: point `PAZ_PARSER_FIXTURES_DIR` at an empty folder and the run
fetches every fixture from the configured client. English LOC text changes too
(journal book titles were renamed between clients), so keep a LOC-text
assertion only if it holds on both.

If `get_records()` returns raw snake_case fields but the test should assert the
user-facing table contract, add a `record_mapper` to `HandlerCase`. The mapper
receives one raw record and returns the normalized dictionary used by test specs.

`tests/test_handler_sort.py` needs no per-handler code. It collects every
`HandlerCase` in the handler-local test modules (`tests/handler_cases.py`),
renders page 1 and checks that
each `data-sort-key` header is in `sortable_fields()`, then sorts by every
declared field in both directions. A handler that renders no sortable headers,
or crashes while rendering or sorting, fails there. Parsed LOC is kept per
fixture and restored between cases, so the whole sweep takes about 25 s.

`tests/test_empty_cells.py` runs over the same cases. It renders every record
and fails when a sortable cell shows a dash or nothing while its record holds a
value that is not empty, which would sort that row among the real values (see
"Store none as None" above). A text value that is itself `-`, such as a name in
the game data, passes; image cells are skipped. It takes about 25 s too.

Fixtures are input files required by tests. Do not commit extracted game files.
`PAZ-Parser/tests/fixtures/` is gitignored except for `.gitkeep`. Missing fixtures
are fetched automatically:

- PAZ files are extracted with `browser.py --file <name> --output PAZ-Parser/tests/fixtures`.
- External files such as `languagedata_en.loc` are copied from the configured game folder.

The cached fixtures follow the installed client. `.client_stamp.json` in the
fixtures folder records which client they came from: the `.meta` header
version and size, plus the size and modified time of `languagedata_en.loc`
(it sits outside the PAZ folder, so the meta version does not cover it). At
the start of every run the stamp is compared with the installed client, and
when they differ every cached fixture is fetched again before any test runs:

```text
fixtures: refreshing 74 files (client 3457 -> client 3458)
fixtures: up to date with client 3458
```

Each file is fetched into a staging folder and then replaces the cached copy,
and the stamp is written only after every fetch succeeded. A failed fetch
stops the run and keeps the old files and stamp, so the next run retries.
Without a configured or reachable client the run uses the cached fixtures as
they are and says so. A test whose fixtures are not cached is then skipped
instead of failed (`fetch_missing()` in `tests/fixtures.py`), so CI, which has
no client, runs only the tests that need no game files. With a client, a fetch
that fails still fails the test. Load fixtures inside a test or fixture, never
at import time: a skip at import time fails collection for every module that
imports it.

| Option                | Effect                                                          |
|-----------------------|-----------------------------------------------------------------|
| (none)                | Refresh only when the installed client changed                  |
| `--refresh-fixtures`  | Fetch every cached fixture again, even from the same client     |
| `--frozen-fixtures`   | Skip the client check, use the cached files (compare snapshots) |

Do not re-pin expected values to make a refreshed run pass; a failure after a
refresh means the parser or the test assumed something a patch can change.

The app must have a saved PAZ folder in `paz_config.json` in its data folder
(`%LOCALAPPDATA%\BDO-PAZ-Browser` unless picked in the settings). Open a PAZ
folder once in the GUI if test fixture fetching fails.

Run all unit tests with:

```bash
python -m pytest -v -s
```

Pytest expands each spec into a separate test item and parses each handler once.

Use `case_id` from `tests.framework` for `pytest.mark.parametrize(..., ids=case_id)`
so test output names stay readable instead of pytest's default `spec0`, `spec1`, `spec2`.

| Spec type           | ID format                               | Example                  |
|---------------------|-----------------------------------------|--------------------------|
| `DeclaredCountTest` | `declared row count`                    | `declared row count`     |
| `SchemaTest`        | `schema: {key1}, {key2}, ...`           | `schema: id, name, kind` |
| `RangeTest`         | `{col} in [{min}, {max}]`               | `kind in [1, 13]`        |
| `TargetTest`        | `{col} = {value}`                       | `TitleId = 3`            |
| `TargetTest`        | `{col} in {a}-{b}` (2-value collection) | `slot in 0-19598`        |
| `TargetTest`        | `{col} in {v1}, {v2}, ...` (3+)         | `kind in 1, 2, 5`        |

```text
title.dbss
  rows:   3,048
  parse:  64 ms
  loc:    0 misses / 6,096 lookups

PAZ-Parser/handlers/_dbss/title/test_handler.py::test_title_dbss[declared row count] PASSED
PAZ-Parser/handlers/_dbss/title/test_handler.py::test_title_dbss[TitleId = 3] PASSED
```

`pytest --clean` leaves out the per-handler blocks and prints only failed tests
and a pass/total line; run without it to see them.

## Checking a Handler from the Command Line

`browser.py` runs a handler the way the GUI does, with LOC and the lookup
indexes loaded, so most checks need no script in `test-scripts/`:

```bash
# The rows get_records() returns, filtered and cut down to a few fields
python browser.py --records buffsimply.bss --where buff_id=48723..48728 --fields buff_id,icon_path
# One rendered page, with the app's CSS and icons inlined, to check the cells
python browser.py --render buffsimply.bss --page 1 > page.html
# What a lookup index holds for one ID
python browser.py --index buff_icon --id 48724
```

See the CLI section of the README for every option. `--records --csv` gives
the same columns as the GUI's CSV export (`record_export.py`).

## Lazy Parsed Handlers

All handlers are lazy by default. The base class caches the result of `get_records()`
per data object, so paging, search, and record count never re-parse the same file.
No opt-in is required: implement `get_records()` and `render_records_page()` and the
rest is handled automatically.

### Building a Parsed Index

For formats that build a heavy internal structure (an offset table, a packed index,
etc.), use `_data_cache()` to build it once per data object:

```python
class MyFormatHandler(PreviewHandler):

    def _get_index(self, data: bytes) -> MyIndex:
        # Build once; rebuild only when data object identity changes.
        return self._data_cache(data, "index", lambda: build_index(data))

    def get_record_count(self, data, entry, companions) -> int:
        return self._get_index(data).count

    def render_data_page(self, data, entry, companions, page, page_size) -> str:
        # Parse only the needed page, avoid materialising all records first.
        records = self._get_index(data).records_for_page(page, page_size)
        return _render_table(records, page, page_size)

    def search_records(self, data, entry, companions, query) -> list[int]:
        return self._get_index(data).search(query)

    def get_records(self, data, entry, companions) -> list[dict]:
        # Compatibility fallback for CSV export and test assertions.
        return self._get_index(data).all_records()
```

`_data_cache(data, name, build_fn)` supports multiple named slots per handler instance
and rebuilds automatically when a different file is selected. Each slot holds the payload
it was built from until the next payload replaces it, so a freed payload's `id()` can
never be mistaken for a new one. Use a descriptive name
(`"index"`, `"offset_table"`) so slots do not collide if the handler caches more than one
structure. `build_fn` runs with the garbage collector paused (`gc_pause.py`): a cached
value is a big structure that stays alive, and collections during its build only walk the
loaded LOC and lookup indexes (`detail_dialog.dbss` parses 1.5x faster). `clear_data_cache()`
drops every slot; the benchmark's `parse` stage calls it before each run so every run
parses cold. `release_data(data)` drops only the slots built from one payload; the
background cache fill calls it after each table it parses.

Slots live on the handler instance, so without a limit every handler would keep the last
table it parsed for the whole session (the 20 biggest tables take about 1 GB together).
The app keeps the slots of the last three parsed tables viewed (`KEPT_TABLES` in
`api/bdo_recent_tables.py`); an older handler drops its slots, and reopening its table
reads the [Parsed Table Cache](#parsed-table-cache) again, or parses when the cache is
off. Every handler drops its slots (`clear_handler_caches()`) when a folder loads, when
the LOC text changes and before plugins reload, since the slots were built from the old
payloads, LOC and lookup indexes. A handler must not keep parsed data anywhere else that
outlives these rules.

### Parsed Table Cache

The app saves what `get_records()` returns in `paz_browser_records.sqlite` in the
client's cache folder (`app_dirs.py`, `paz/bdo_records_cache.py`, keys in `api/bdo_records_store.py`), and
`all_records()` serves it on the next open. The CLI and the benchmark never use it. A
row is reused only while all of these match:

- the handler's code: its class, the project modules it reaches through imports and
  constructor arguments, and the JSON files beside them (`paz/source_fingerprint.py`)
- the handler's language
- the table and every path `companions()` returns: archive, archive CRC and size,
  offset and sizes
- the LOC text and each lookup index the build read, by content digest

So `get_records()` has to follow a few rules:

- **Read shared data only through `_common/loc.py` and `_common/lookup_index.py`.**
  Their functions report each read to `_common/data_deps.py`; a build that never read
  LOC keeps its row when a patch changes LOC. A module-level memo of LOC text or an
  index value would hide the read and serve another language's text.
- **Depend only on the payload, the declared companions, LOC, the lookup indexes and
  `self.lang`.** Anything else, such as a setting or the time, is not in the key.
- **Return picklable plain values** (dicts, lists, tuples, str, int, float, bool,
  None), and do not change the records after returning them: a background thread
  pickles them.

Sort orders are cached too, next to the records they index: opening
`itemenchant.dbss` from the cache takes 0.5 s instead of 1.3 s with the default
sort rebuilt. An order row carries the stamp (input key and read dependencies) of
the records it was built from, and is served only for records with that stamp.
Only handlers whose order comes from `records_sort_order()` alone qualify
(`sorts_records_only()`); a handler that overrides `_build_sort_order()` to sort
its own index, such as `quest.dbss` or the LOC handler, always builds. The "cache
all tables" pass also stores each table's opening sort: the saved one, else
`default_sort()`.

### When to Override `render_data_page`

Override `render_data_page()` only when the format supports parsing a single page
without reading all records first, for example a format with a stored offset table
that lets you seek directly to each record.

If `get_records()` is fast (small file, trivial parse), the base implementation is
sufficient: it calls `get_records()` once, caches the result, and slices it per page.

## Streamed Preview Handlers

Large browser-native previews should subclass `StreamPreviewHandler` instead of
reading the full payload into HTML.

Use streamed handlers for formats that can preview from a local URL, such as
video or audio. The API supplies a tokenized localhost URL and skips the eager
`read_entry_payload(...)` call during initial selection.

```python
from bdo_models import PazEntry
from bdo_preview import StreamPreviewHandler, register_handler


class MyVideoHandler(StreamPreviewHandler):
    mime_type = "video/webm"

    def render_stream(self, stream_url: str, entry: PazEntry) -> str:
        return (
            '<div class="video-view">'
            f'<video controls preload="metadata" src="{stream_url}"></video>'
            '</div>'
        )


register_handler(".webm", MyVideoHandler())
```

Rules:

- `mime_type` should match the streamed content type.
- `render_stream()` returns only the preview shell HTML.
- Do not base64-encode the payload inside the handler.
- The stream endpoint supports browser `Range` requests, but the current backend still decodes the full entry before slicing the response.

## Companion Files

Override `companions()` when a handler needs related files.

```python
def companions(self, entry: PazEntry) -> list[str]:
    folder = entry.internal_path.rsplit("/", 1)[0]

    return [
        f"{folder}/titleoffset.dbss",
        f"{folder}/languagedata_en.loc",
    ]
```

Companion files are passed into `get_records()` as:

```python
companions: dict[str, bytes]
```

The dictionary is keyed by basename.

`data` and every companion hold exactly the file's recorded size: a stored
(uncompressed) `.bss` is padded to the 8-byte ICE block in the archive, and the
reader trims that zero padding, as extraction does. A trailer read from the end
of the file, such as the PABR string table offset (`_common/pabr_strings.py`),
is therefore safe.

`_common/pabr_strings.py` also holds the checks every PABR parser needs, so a
layout change fails loudly instead of yielding shifted fields:
`fixed_row_offsets(data, row_size, file_name)` checks the magic and returns the
start of every fixed-size row, raising when the rows do not end where the string
table starts; `check_rows_end(data, rows_end, what)` does that last check for
records walked by hand; `checked_string_table_start(data, file_name)` returns the
bound for a variable-size walk; `check_pabr(data, file_name)` checks the magic only.

Example:

```python
offset_raw = companions.get("titleoffset.dbss")
loc_raw = companions.get("languagedata_en.loc")
```

A companion can live in another folder. Tables under `gamecommondata/binary/`
that need the worldmap node graph use `worldmap_companion(entry)` for its path
and `worldmap_links(companions)` for its links (node key -> linked node keys,
empty when the file is missing), both from `_bwp/waypoint/worldmap.py`.

Disk files pre-loaded by the browser may also be merged into `companions`.

For example:

```python
companions.get("languagedata_en.loc")
```

## HTML Output Rules

Handlers return HTML fragments.

Always escape user-visible or file-derived values.

Good:

```python
import html

return f"<div>{html.escape(name)}</div>"
```

Avoid:

```python
return f"<div>{name}</div>"
```

Use shared HTML helpers when available.

Example:

```python
from _common.html import error, icon_cell, table
```

Give number columns the `"num"` class (`Column("Buff ID", "num", ...)`). The
table CSS right-aligns them and shrinks them to their content, so text columns
take the spare width of the pane.

Draw game text that may hold `<PAColor0xAARRGGBB>` / `<PAOldColor>` tags with
`pa_html(raw)` from `_common/pa_text.py`, never with `e(raw)`: it escapes the
text and turns each colour into a span. Keep the plain text in the record and
the tagged copy in a display-only field, see
[Display-Only Fields](#display-only-fields).

Use `icon_cell(path)` for icon path columns so DBSS/BSS table previews keep
consistent spacing and escaping. The frontend lazy-loads matching PAZ image
entries into those cells, while parsed CSV export keeps the raw icon path field.

### Display-Only Fields

A record key starting with `_` is for rendering only (`record_fields.py`).
Tab search (`record_matches()`, also for a handler with its own
`search_records`), sorting (`TableSort.parse` rejects it) and the CSV export
skip it, so a handler keeps its plain field for those and adds the tagged text
next to it. Read LOC text with its tags through `loc_tagged()` (the tagged
twin of `loc_text()`), then:

```python
from _common.loc import loc_tagged
from _common.pa_text import pa_cell, pa_fields, pa_key, pa_line_cell, pa_list_cell, pa_list_fields

# get_records: `description` plain, `_description_pa` tagged
record = {**record, **pa_fields("description", loc_tagged(5, buff_id))}

# render_records_page: coloured, or "-" when blank; max_chars cuts the
# visible text like truncate()
pa_cell(r, "description")
pa_cell(r, "objective", 140)

# Long text (descriptions, greetings) on one line: line breaks become spaces,
# then the text is cut after max_chars (LINE_PREVIEW_CHARS, 120, by default)
pa_line_cell(r, "description")

# A list field: pa_list_fields() puts the plain list under the field and the
# tagged list under pa_key()
record = {**record, **pa_list_fields("texts", tagged_texts)}
pa_list_cell(r[pa_key("texts")], 3)
```

Text that has its own fallback chain gets a tagged helper next to the plain
one: `skill_name_tagged()` / `skill_description_tagged()` in `_common/skill.py`,
`quest_title_tagged()` in `_common/quest/quest.py` and `ui_hash_tagged()` in
`_bss/stringtable/text.py`.

An icon list label in colour goes through `icon_html_label_cell()` /
`icon_html_list_cell()`, which take labels that are already safe HTML
(`pa_html()` output); `icon_label_cell()` / `icon_list_cell()` escape plain
labels. `buff_list_cell()` draws each buff's first line in its colours this
way. Item names (LOC type 0 field 0) carry no tags; `item_name_tagged()` and
`item_key_list_cell()` in `_common/item_key.py` draw them in their grade colour.

A LOC type whose keys hold a part the caller cannot know up front reads all of
its rows through `loc_type_entries(str_type)` (read-only, built once per loaded
LOC): type 50 keeps a service code in `str_id3`, see
`_dbss/cashproduct/text.py`.

A handler test checks a `pa_fields` text with `PaFieldTest(field="text")` from
`tests/framework.py`: every plain value is its tagged copy without tags, and
at least one copy keeps a `<PAColor>` tag.

`pa_html(raw, colors=False)` drops the colours and returns
`e(strip_pa_tags(raw))`, so a column can turn colour off without changing its
call. Colours nest; a stray `<PAOldColor>` is dropped, colours left open are
closed at the end, and other `<PA...>` tags are dropped. The **Show game text
tags** setting (off by default) makes `pa_html` show every tag as a dimmed
`pa-tag` span too; the app applies it through `set_show_pa_tags()` at start and
on save, and the CLI always turns it on. A colour stored as a u32 rather than
in tag text (`dropuitaginfo.bss`) goes through `argb_css(argb)`, which keeps
the alpha (`rgba(r, g, b, a)`); `argb_css(argb, alpha_scale)` multiplies it,
for a colour the game uses to tint a translucent texture (the hunting ground
tag pills).

`_common/pa_color.py` is a different job: it finds colour markers in raw UTF-16
bytes for `title.dbss`.

The CLI `--records` table and JSON keep display-only fields, to show the tags.

## Raw Hex Preview

Handlers should only render their parsed preview.

The main preview UI is responsible for switching between:

- Parsed preview
- Raw hex preview

Do not manually include raw hex tabs inside individual handlers.

This keeps all handlers consistent.

## Shared Helpers

Use `_common/` for helpers shared by multiple formats.

Examples:

```text
_common/
├── loc.py               # LOC index: loc_lookup(), loc_tagged() / loc_text(), loc_type_entries()
├── binary.py
├── buff.py              # buff icon paths and LOC type 5 buff text
├── character.py         # character names and titles (LOC type 6)
├── class_type.py        # class types: LOC type 21 names, class bit masks
├── duration.py          # format_duration(): milliseconds as "1h 30m", "45s", "1.5s"
├── enum_name.py         # enum_name(): CppEnums member name of a stored value, or the bare value
├── html.py
├── hunting_ground.py    # drop window hunting ground names by key (LOC type 116)
├── offset_table.py      # OffsetTableHandler: the one preview handler for every offset companion
├── pabr_offset.py       # offset companions: u8, u16 or u32 keys, with or without PABR magic
├── prefixed_string.py   # length-prefixed strings: strict and lenient readers
├── inline_text.py       # decode_inline_text(): the stored \n escape of inline text
├── item_key.py          # item keys (enchant_level << 24 | item_id), LOC type 0 names, per-level icons
├── knowledge.py         # knowledge entry names (LOC type 34)
├── lease.py             # Lease, its text and dialog_leases() (CHARACTER_LEASES)
├── pa_text.py           # game text tags: pa_fields() / pa_cell() / pa_line_cell() for records, pa_html(), argb_css()
├── record_reader.py     # RecordReader: walks one variable-length record in order
├── skill.py             # skill keys (skill_no << 16 | level) and LOC type 10 names
└── worker.py            # plantation workers: WorkerGrade, worker_name_cell(), stat scales and format_stat()
```

Read an offset companion with `parse_pabr_offset_rows()` (PABR magic, count,
u16-keyed rows), `parse_pabr_u32_offset_rows()` (the same with u32 keys, e.g.
`mentalcardoffset.dbss`), `parse_bare_offset_rows()`,
`parse_bare_u32_offset_rows()` or `parse_bare_u8_offset_rows()` (count, rows;
the u8 key of `pcgrowthoffset.dbss`), never by hand. A u16 field
followed by a zero u16 (`plantzoneoffset.dbss` keys, `petoffset.dbss` sizes)
reads as one u32. Walk a record of fixed fields
and u64-prefixed strings with `RecordReader(data, start, end, label)`: `unpack`,
`text(wide=...)`, `skip`, and `at_end()` / `remaining()` for the final size
check; it raises ValueError as soon as a field runs past the record. For inline
strings at unknown positions, `read_prefixed_at()` reads a prefix at a known
position and returns the next one; `read_prefixed_utf16()` and
`find_prefixed_ascii()` are for text whose position is only a guess.

Name a character with `character_name()` from `character.py` (LOC type 6; its
title, `<Storage Keeper>`, with `character_title()`), a
knowledge entry with `knowledge_name()` from `knowledge.py` (LOC type 34), a
worldmap node with `node_name()` or `full_node_name()` from `node.py` (LOC
type 29, see `NODE_PARENT` under Lookup Indexes) and a title with
`title_name()` from `title.py` (LOC type 1, tags removed; `title.dbss` keeps
its own tagged lookup for the colours). All return `''` when LOC is not
loaded, so no `is_loc_loaded()` guard is needed. Do not define those LOC types
in a handler.

Tables in the skill cluster split a skill key with `split_skill_key()` and name
a skill with `skill_name(skill_no)` from `skill.py`: LOC type 10 first, then
the Korean `skilltype.dbss` name from the `SKILL_NAME_KR` lookup index, so no
skill table needs `skilltype.dbss` as a companion. A `GAME` sheet UI key
(`LUA_SKILLTREE_PANEL_NAME0`) gets its LOC type 37 hash from
`parse_key_hashes()` in `_bss/stringtable/parser.py`, and its text from
`ui_key_text()` (by key) or `ui_hash_text()` (by hash) in
`_bss/stringtable/text.py`, which try LOC `str_id3` 0 and then 1.

A class type (`0` Warrior, `8` Sorceress) is named with `class_name()` from
`class_type.py` (LOC type 21). Skill tables that store a set of classes as a
bit mask (`skillsimply.dbss` `class_mask`) split it with
`class_types_in_mask()`; `ALL_CLASSES_MASK` is the "every class" value.
Items store every playable class as `PLAYABLE_CLASSES_MASK` instead, which
skips unused class types: test for it with `is_all_classes()`, a superset
check that keeps working when a class is added, and name the playable
classes of a mask with `class_names()`.

`html.py` has `truncate(text, max_len)` for long text cells,
`text_list_cell(values, max_items)` for list cells, `icon_list_cell(entries,
hidden_count)` for list cells with an icon per entry (see [Icons](#icons)) and
`flag_cell(is_set)` for yes/no cells (a green check mark or a red cross).

A cut list ends in `... (+N)` (`more_marker()`), and hovering it lists the
hidden entries: the first `MORE_TOOLTIP_ITEMS` (40) by name, then a count.
`text_list_cell()` and `pa_list_cell()` name them themselves. Cells that build
each entry, such as `icon_list_cell()` and `html_list_cell()` for entries that
are already safe HTML, take `hidden_names`: plain text for
`hidden_slice(values, max_items)`, so only those few entries are named.

Use format-specific helpers inside that format package.

Examples:

```text
_dbss/common/
├── binary.py
├── constants.py
└── html.py
```

Rule of thumb:

- Used by only DBSS → `_dbss/common/`
- Used by multiple formats → `_common/`

### Offset Tables

An offset companion (`*offset.dbss`: a key, a byte offset and a size per row)
gets no handler class of its own. Its package defines a factory that returns an
`OffsetTableHandler` from `_common/offset_table.py`, and the registration
module registers the factory's result:

```python
def buff_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("buff_id", "buffId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_pabr_offset_rows, "buff_id"),
    )
```

- Each column names the record field it shows and sorts by and its label key
  in the `offsetColumns` block of `lang/<lang>.json`.
  `offset_column()` shows `0x0001A2B0`, `size_column()` shows `1,024`, and a
  plain `OffsetColumn` shows the number; pass `text=` for another form (a hash
  key through `offset_text`, a pet key as `0x5A06 (23046)`).
- The reader turns the file into records and keeps the format's field names,
  which its parser, its tests and the CSV export share: `offset_records()` for
  the shared rows of `_common/pabr_offset.py`, `offset_map_records()` for
  `parse_offset_table()` files, `picked_records()` to keep some fields of a
  parsed row, or the format's own reader when a key splits into several
  fields (`skill_offset_handler()`, `detail_dialog_offset_handler()`).
- `lang_block=` names another label block, and `meta=` replaces the
  "N offset records" header with a `(records, lang) -> str` function
  (`journalquestoffset.dbss` counts its groups). The shared header text is in
  `_common/lang/`.

## Lookup Indexes

Some joins need a table far too large to open as a companion on every preview,
such as the 194 MB `itemenchant.dbss`. For those the app keeps **lookup
indexes**: cached `entity ID -> value` tables built once per PAZ folder and
injected into `_common/lookup_index.py`, the same way `init_loc()` supplies LOC
data. A handler reads one by kind and ID:

```python
from _common.lookup_index import IndexKind, lookup

item_id = lookup(IndexKind.CHARACTER_ITEM, character_id)  # None when missing
```

`lookup()` returns `None` both when the index is not loaded and when it has no
entry for the ID; render a dash in either case. `is_index_loaded()` tells the
two apart when it matters. Unit tests install an index with
`init_index(kind, mapping)` and drop it with `clear_indexes()`; a
`HandlerCase` takes `lookup_indexes={kind: mapping}`, which the runner installs
while the handler runs and removes afterwards. For an index built from other
fixtures, pass a function that returns the mapping instead; the runner calls it
when the case runs (see `_node_parent_index` in
`plantexchangegroup/test_handler.py`).

Every index is one `IndexSpec(kind, sources, build)` in
`INDEX_SPECS` (`_common/lookup_builders.py`). `build` receives the payloads of
`sources` as positional arguments, in the order listed, and returns
`{entity_id: value}`. `build_indexes()` reads each source once, so specs that
share a table reuse its payload; a spec with a missing source is skipped. Adding
an index is one `IndexKind` member plus one spec, both on the handler side: the
app core only calls `build_indexes()`, so a new index needs no core change.

`Api._load_lookup_indexes()` installs every index at folder load. The app
shows the tree before LOC and the indexes are in, and the calls that run a
handler (`load_entry`, `get_parsed_page`, export, content search, icons) wait
for both (`_wait_for_folder_text()`), so a handler never runs without them.
Results are
cached by `paz/bdo_index_cache.py` in `paz_browser_indexes.cache` in the
client's cache folder, keyed by `IndexKind.value` (renaming a value orphans its cached data
until the rebuild) and invalidated on the PAZ meta version or when the code that
builds them changes. The cache stores `builder_fingerprint()` (through
`index_fingerprint()` in `api/bdo_lookup_indexes.py`), a hash of
`_common/lookup_builders.py` plus every project module it imports and the JSON
files beside them (`paz/source_fingerprint.py`), so editing a builder, a helper
such as `_common/prefixed_string.py` or `_common/icon_overrides.json` rebuilds
the indexes on the next launch. Keep the builder imports at the top of that
module: a lazy import would hide the builder from the fingerprint.

Values are pickled, so an index may hold icon paths, linked IDs or tuples of
IDs (`LookupValue`).

| Kind             | Sources                                    | Value          |
| ---------------- | ------------------------------------------ | -------------- |
| `ITEM_ICON`      | `itemenchant.dbss`, `itemenchantoffset.dbss` | icon path    |
| `QUEST_ICON`     | `quest.dbss`, `allquestlist.bss` (record order) | icon path |
| `CHARACTER_ICON` | `characterobject.dbss`, `characterobjectoffset.dbss` | icon path |
| `CHARACTER_ITEM` | `itemenchant.dbss`, `itemenchantoffset.dbss` | item ID      |
| `KNOWLEDGE_CHARACTERS` | `characterstatic.dbss`, `characterstaticoffset.dbss` | character IDs (tuple) |
| `KNOWLEDGE_LEARNING_CHARACTERS` | `knowledgelearning.dbss`, `knowledgelearningoffset.dbss` | character IDs (tuple) |
| `KNOWLEDGE_LEARNING_ITEMS` | `knowledgelearning.dbss`, `knowledgelearningoffset.dbss` | item IDs (tuple) |
| `CHARACTER_LEASES` | `detail_dialog.dbss`, `detail_dialogoffset.dbss` | flat `(item_id, cost, ...)` pairs |
| `SKILL_ICON`     | `skilltype.dbss`, `skilltypeoffset.dbss`   | icon path      |
| `SKILL_NAME_KR`  | `skilltype.dbss`, `skilltypeoffset.dbss`   | Korean name    |
| `BUFF_ICON`      | `buffsimply.bss`                           | icon path      |
| `ITEM_KEY_ICON`  | `specialenchantitem.bss`                   | icon path      |
| `ITEM_GRADE`     | `itemenchant.dbss`, `itemenchantoffset.dbss` | grade, 0 to 5 |
| `QUEST_ARTWORK_ICON` | `questjournalvideoinfo.bss`            | artwork path   |
| `MANOR_PART_ICON` | `mansionpartinfo.bss`                     | icon path      |
| `CUTSCENE_ICON`  | `groupcameradata.bss`                      | icon path      |
| `WORLDMAP_MARKER_ICON` | `worldmapmonster.dbss`, `worldmapmonsteroffset.dbss` | icon path |
| `MENU_ICON`, `SUBMENU_ICON` | `menu.bss`, `submenu.bss`       | sprite sheet path |
| `MENU_ICON_REGION`, `SUBMENU_ICON_REGION` | `menu.bss`, `submenu.bss` | `(x1, y1, x2, y2)` |
| `PRODUCTION_ITEMS` | `plantexchangegroup.bss`, `itemsubgroup.dbss`, `itemsubgroupoffset.dbss` | item keys (tuple) |
| `SKILL_BUFFS`    | `skill.dbss`, `skilloffset.dbss`           | buff IDs (tuple) |
| `BUFF_ITEMS`     | `itemenchant.dbss`, `itemenchantoffset.dbss`, `skill.dbss`, `skilloffset.dbss` | item IDs (tuple) |
| `NODE_PARENT`    | `exploration.bss`, `mapdata_realexplore2.bwp` | parent node key |
| `TELEPORT_BUFFS` | `buff.dbss`, `buffoffset.dbss`             | buff IDs (tuple) |
| `TELEPORT_BUFF_NAME_KR` | `buff.dbss`, `buffoffset.dbss`      | Korean buff name |
| `TELEPORT_NEAREST_NODE` | `teleport.dbss`, `mapdata_realexplore2.bwp` | `(node key, metres)` |
| `LIGHTSTONE_SETS` | `lightstoneset.bss`                       | set IDs (tuple) |
| `INSTANCE_FIELD_NAME` | `instancefield.dbss`                  | internal field name |
| `INSTANCE_FIELD_TITLE` | `instancefieldmapinfo.bss`, `stringtable.bss` | `GAME` sheet key hash of the title |

`CHARACTER_ITEM` maps a character to the one base item that places or summons
it (`character_id` at `+0xAA` in
[itemenchant.dbss](file-formats/itemenchant_dbss.md)); characters named by zero
or several items are left out. The `characterobject.dbss` Item column reads it.

`KNOWLEDGE_CHARACTERS` maps a knowledge card to every character whose
`getknowledge(<id>);` action script grants it, in ascending ID order.
`KNOWLEDGE_LEARNING_CHARACTERS` maps a card to the monsters, NPCs and
gathering nodes that teach it through
[knowledgelearning.dbss](file-formats/knowledgelearning_dbss.md) table 0, also
in ascending ID order. The two overlap but neither covers the other, so the
`mentalcard.dbss` Learned From column reads both and merges them.
`KNOWLEDGE_LEARNING_ITEMS` maps a card to the items that teach it (table 1),
in ascending ID order; the Learned From Items column shows them with
`item_key_list_cell()`.

`CHARACTER_LEASES` maps a character to every `buyItemByPoint(...)` lease
option in its dialogs ([detail_dialog.dbss](file-formats/detail_dialog_dbss.md)),
in dialog order and without repeats, as flat `(item_id, cost)` pairs. It is
built by `build_character_lease_index()` in `_dbss/detail_dialog/parser.py`.
Read it through `dialog_leases(character_id)` in `_common/lease.py`, which
unpacks the pairs with `lease_pairs()`. The `npcsimply.bss` Leases column
reads it. Its source is 27 MB, which takes about 2 s to read and
build once per client.

`SKILL_ICON` maps a skill number to the icon its `skilltype.dbss` record
stores; skills without one are left out. `skill.dbss`, `skillgroup.bss` (the
first rank's icon) and the `ui_skillgroup_*.bss` skill windows read it through
`IconKind.SKILL`; `skilltype.dbss` shows its own stored path.

`SKILL_NAME_KR` maps a skill number to its Korean `skilltype.dbss` name.
`skill_name()` in `_common/skill.py` falls back to it when LOC type 10 has no
name, which on client 3458 names 1,920 `skill.dbss` ranks (set effects, event
skills) that would otherwise show only an ID.

`BUFF_ICON` maps a buff ID to its icon. It reads
[buffsimply.bss](file-formats/buffsimply_bss.md), which stores the same icon
paths as `buff.dbss` in fixed 32-byte rows (1.4 MB against 12 MB of
variable-length records). Buffs without an icon or with the `UNKNOWN`
placeholder are left out. Read it through `IconKind.BUFF`, or through
`buff_list_cell()` in `_common/buff.py`, which draws a buff list with icons
(the Buffs columns of `skill.dbss` and `itemenchant.dbss`). `buff_icon_path()`
there normalizes the stored paths for both buff tables.

`ITEM_KEY_ICON` maps a packed item key (`enchant_level << 24 | item_id`) to
the icon of that level, for the 551 items whose icon or name changes with
their level (Sovereign weapons, Fallen God armor, PEN Nouver sub-weapons). It
reads [specialenchantitem.bss](file-formats/specialenchantitem_bss.md), which
copies those per-level icons out of `itemenchant.dbss` in fixed 19-byte rows
(175 KB); `ITEM_ICON` reads level-0 blocks only and cannot reach them. Read it
through `item_key_icon_path(item_key)` in `_common/item_key.py`, which falls
back to the item's own `IconKind.ITEM` icon for every other key. Item key
lists show it through `item_key_list_cell(item_keys, max_items)` in the same
module: the `itemsubgroup.dbss` Item Names column, the `plantexchangegroup.bss`
Items column, the `plantzone.dbss` Produced Items column and the
`dropuihuntinggroundinfo.bss` Items column. A plain item ID is its level 0
key, so lists of item IDs use it too.

Those lists name each key with `item_key_text()` from the same module. A level
with its own LOC type 79 name (`str_id1` item ID, `str_id2` level, read with
`item_level_name()`) shows that name alone, `DEC: Sovereign Longsword` or
`Wailing Fallen God's Armor`: on client 3458 such a name never repeats across
the levels of one item. Every other level shows the LOC type 0 name and the
level, `Blackstar Helmet (19)`, including levels whose LOC type 79 name is just
the item name (`Preonne Belt (3)`).

`ITEM_GRADE` maps a base item ID to its grade (`+0x06` in
[itemenchant.dbss](file-formats/itemenchant_dbss.md)), which the game draws
the name in. `item_key_list_cell()` reads it through
`item_key_text_tagged()`, which wraps the name in the grade's `<PAColor>`
tag, so every item list (and the `buff.dbss` Applied By and `teleport.dbss`
Used By columns) shows item names in their grade colour. The colours are
`ITEM_GRADE_COLORS` in `_common/item_grade.py`; `itemenchant.dbss` colours its
own Item column from the record. A single item name column uses
`item_name_tagged(item_id)` from `_common/item_key.py` with `pa_fields()`
(`cashproduct.dbss`, `fairyupgraderate.bss`, `characterobject.dbss`), and
the lease lists use `lease_text_tagged()` from `_common/lease.py`.

Six small tables are indexed although only their own handlers show their
icons today, so a later table can reuse them without opening the source
file. Each has its own icon kind, apart from the entity's real icon, so none
of them changes an icon an existing table shows:

- `QUEST_ARTWORK_ICON` (`IconKind.QUEST_ARTWORK`): the journal page artwork of
  80 Land of the Morning Light quests by packed quest ID; mostly the `_Full`
  version of the `QUEST_ICON` path.
- `MANOR_PART_ICON` (`IconKind.MANOR_PART`): manor part blueprints (the building with one part highlighted) by
  `manor_part_key(character_id, part_index)` from
  `_bss/mansionpartinfo/parser.py`.
- `CUTSCENE_ICON` (`IconKind.CUTSCENE`): the region symbol of each cutscene
  skip summary by scene ID.
- `WORLDMAP_MARKER_ICON` (`IconKind.WORLDMAP_MARKER`): world map marker art by
  marker key; the Abyssal Wells store none.
- `MENU_ICON` / `SUBMENU_ICON` (`IconKind.MENU` / `IconKind.SUBMENU`): the
  main menu sprite sheet by menu or entry ID, with the region in
  `MENU_ICON_REGION` / `SUBMENU_ICON_REGION` (see [Sprite Icons](#sprite-icons)).
  The `menu.bss` and `submenu.bss` tables show them with `sprite_icon_cell()`.

`PRODUCTION_ITEMS` maps a worker production key to the packed item keys
(`enchant_level << 24 | item_id`) of its
[itemsubgroup.dbss](file-formats/itemsubgroup_dbss.md) subgroup, through the
subgroup key in [plantexchangegroup.bss](file-formats/plantexchangegroup_bss.md).
Only the few hundred production subgroups are read, so no table needs the
13 MB `itemsubgroup.dbss` as a companion to show production items. Production
keys whose subgroup is missing from `itemsubgroupoffset.dbss` are left out.
It is built by `build_production_item_index()` in
`_bss/plantexchangegroup/parser.py`. Read it through `production_item_keys()`
in `_common/production_items.py`, or through `production_item_fields()`
there, which adds the `item_keys` and `items`
record fields (names from `item_key_text()` in `_common/item_key.py`). The
`plantexchangegroup.bss` Items column and the `plantzone.dbss` Produced Items
column read it that way.

`SKILL_BUFFS` and `BUFF_ITEMS` are the item to buff link. An item's
`itemenchant.dbss` skill keys name [skill.dbss](file-formats/skill_dbss.md)
records, whose `buff_ids` are the item's buffs (item 761880 -> skill 47683 ->
buffs 48723 to 48728). `SKILL_BUFFS` maps a skill key to its buff IDs in slot
order, leaving out skills without buffs; read it through `skill_buff_ids()` in
`_common/skill.py`, which the `itemenchant.dbss` Buffs column uses. The
`buff.dbss` handler also reads every entry to give the untitled buffs of a
consumable the title of its headline buff. `BUFF_ITEMS` maps a buff ID to
every base item whose skills apply it, in ascending ID order; the
`buff.dbss` Applied By column reads it. It is built by
`build_buff_item_index()` in `_dbss/itemenchant/parser.py`, which reads both
tables, so `BUFF_ITEMS` costs no second read of `itemenchant.dbss`.

`NODE_PARENT` maps a worldmap sub-node (`is_sub_node` in
[exploration.bss](file-formats/exploration_bss.md)) to the one node it links
to in the worldmap graph, its parent; sub-nodes with no link or several are
left out. Read it through `full_node_name()` in `_common/node.py`, which names
a sub-node `Bambu Valley - Mining` where LOC type 29 alone says `Mining`; the
`buff.dbss` Effect column uses it for node registration buffs.
`node_with_parent_name()` returns that joined name or `''` when the parent or
a name is missing, for a table with a better fallback than the bare sub-node
name (`plantexchangegroup.bss` keeps its Korean label). `node_name()`
in the same module is the plain LOC type 29 name the node tables show. It is
built by `build_node_parent_index()` in `_bss/exploration/parser.py`.

`TELEPORT_BUFFS` maps a [teleport.dbss](file-formats/teleport_dbss.md) point
to the effect type 23 buffs that go there, and `TELEPORT_BUFF_NAME_KR` maps
those buffs to their Korean names; the point ID packs section and key
(`teleport_point_id()` in `_common/teleport.py`, which also reads both
indexes). The `teleport.dbss` Used By column names each buff by its item
(`BUFF_ITEMS`), else its LOC type 5 text, else the Korean name. Both are built
in `_dbss/buff/parser.py` and keep only the 654 teleport buffs, so the table
does not open the 12 MB `buff.dbss`. `TELEPORT_NEAREST_NODE` goes the other
way: each point's nearest worldmap node and its distance, found without LOC
over every node (`build_teleport_nearest_node_index()` in
`_dbss/teleport/parser.py`). `teleport_point_place()` turns it into `Marni's
Lab (12 m)` for the `buff.dbss` Effect text of type 23.

`LIGHTSTONE_SETS` maps a Lightstone item to the
[lightstoneset.bss](file-formats/lightstoneset_bss.md) sets it counts toward,
in ascending set ID order: a member to every set that lists it, and a
substitute (an Amplified Lightstone) to the sets of its base Lightstone. It
is built by `build_lightstone_set_index()` in `_bss/lightstoneset/parser.py`.
Read it through `item_set_ids()` in `_bss/lightstoneset/item_sets.py`, whose
`set_label_tagged()` names a set by its LOC type 113 name; the
`itemenchant.dbss` Lightstone Sets column uses both.

`INSTANCE_FIELD_NAME` maps an
[instancefield.dbss](file-formats/instancefield_dbss.md) key to the field's
internal ASCII name (`A1_001`, `Solare_Arena_Kell`); no LOC type names the
fields. It is built by `build_instance_field_name_index()` in
`_dbss/instancefield/parser.py`. Read it through `instance_field_name()` in
`_common/instance_field.py`.

`INSTANCE_FIELD_TITLE` maps the same key to the `GAME` sheet hash of the
field's title key in
[instancefieldmapinfo.bss](file-formats/instancefieldmapinfo_bss.md)
(`INSTANCEDUNGEONDATA_A1_001_NAME`), so the text follows the loaded LOC
language without a rebuild. It is built by
`build_instance_field_title_index()` in `_bss/instancefieldmapinfo/parser.py`
and read through `instance_field_title()` in
`_bss/instancefieldmapinfo/titles.py` (LOC type 37, `The Magnus: The Great
Single Path`). `instance_field_label()` there joins both indexes; the
`buff.dbss` Effect text of type 176 uses it, `Teleport to Instance Field The
Magnus: The Great Single Path (A1_001)`, and the `instancefield.dbss` Title
column uses the title alone.

## Icons

`icon_cell(path)` renders an icon cell. The path is not fetched at parse time;
the UI lazily resolves it against the PAZ entry map when the cell scrolls into
view, so a handler only has to emit a correct path string.

A list of entities with an icon each (the items of a subgroup) goes in one cell
with `icon_list_cell(entries, hidden_count)`: each `(icon_path, label)` entry
becomes an `icon_label_cell()`, the icon followed by its label instead of its
path, comma-separated like `text_list_cell()`. The caller slices the entries to
the ones shown and passes the count of the rest, so icon paths are looked up
for one page of entries only. Pass `hidden_names` too, so hovering the count
names the rest (`item_key_list_cell()` does). An entry without a path is its label alone. When
the client does not ship an entry's icon, the GUI and `browser.py --render`
drop the swatch and keep the label, where a plain icon cell becomes a dash.
Both swap only the head of the entry (`PENDING_ICON_LABEL_RE` matches the
opening span and the swatch) and leave the label alone, so a coloured label
(`icon_html_list_cell()`, see [Display-Only Fields](#display-only-fields))
keeps its markup.
Records keep the plain names (`items`) for search, sort and CSV. The hover
text of an entry is its icon path; pass `tooltips` (one string per shown
entry) to replace it, as the `teleport.dbss` Used By column does with the
buff IDs behind each name. `browser.py --render` keeps those tooltips.

The backend turns the file into a 64 x 64 PNG thumbnail
(`api/bdo_icon_images.py`). Uncompressed 32-bit BGRA DDS files are wrapped
straight into an image, because Pillow's own decoder takes seconds on the
full-size art some tables use as icons (the 2560 x 1440 journal artwork).
Thumbnails are built one at a time, since each JS call runs on its own thread
and a screen of large textures would otherwise starve the window thread, and
each finished one is stored in `paz_browser_thumbnails.sqlite` in the client's
cache folder (`paz/bdo_thumbnail_cache.py`), cleared when the meta version changes. A
large texture therefore costs its read (about 1 s for a 14 MB file, mostly
decompression) once per client version, not once per session.

Icons are looked up by kind and entity ID through `_common/icon_index.py`,
never by hand-written template:

```python
from _common.icon_index import IconKind, icon_path

row["icon_path"] = icon_path(IconKind.ITEM, item_id)
```

`icon_path()` tries two sources in order:

1. **The lookup index for that kind**: named by `ICON_INDEXES`
   (`IconKind.ITEM` reads `IndexKind.ITEM_ICON`, and so on). For items it is
   built from the level-0 records of `itemenchant.dbss`, which store each item's
   icon path inline.
2. **Derivation from the ID**: when that kind declares one and the index has no
   entry. `IconKind.ITEM` derives into the flat `product_icon_png` folder.

Kinds are an `Enum` so a typo is a failure at import rather than a silently
empty icon column. Adding one means adding the member, its optional deriver in
`_DERIVERS`, and, when a table stores its icons, an `IndexKind` with its spec
(see [Lookup Indexes](#lookup-indexes)) mapped in `ICON_INDEXES`.

`CHARACTER` has one extra step. After every index is built,
`build_indexes()` gives each character without a working icon the icon of the
item that places or summons it, through `CHARACTER_ITEM` and `borrow_icons()`.
A working own icon always wins, and a borrowed icon is used only when its file
exists. The cached `CHARACTER_ICON` index already holds the borrowed icons.

| Kind                | Source                  | Entries (client 3458) | Derivation fallback |
| ------------------- | ----------------------- | ------- | ------------------------- |
| `ITEM`              | `itemenchant.dbss`      | 70,284  | `product_icon_png`        |
| `QUEST`             | `quest.dbss`            | 19,324  | none                      |
| `CHARACTER`         | `characterobject.dbss`, gaps from `itemenchant.dbss` | 6,165 | none |
| `PET_EQUIP_SKILL`   | none                    | 0       | `08_servant_skill/02_pet` |
| `FAIRY_EQUIP_SKILL` | none                    | 0       | `08_servant_skill/02_pet` |
| `SKILL`             | `skilltype.dbss`        | 9,402   | none                      |
| `BUFF`              | `buffsimply.bss`        | 15,076  | none                      |
| `ITEM_KEY`          | `specialenchantitem.bss` | 3,081  | none; `item_key_icon_path()` falls back to `ITEM` |
| `QUEST_ARTWORK`     | `questjournalvideoinfo.bss` | 80  | none                      |
| `MANOR_PART`        | `mansionpartinfo.bss`   | 9       | none                      |
| `CUTSCENE`          | `groupcameradata.bss`   | 92      | none                      |
| `WORLDMAP_MARKER`   | `worldmapmonster.dbss`  | 213     | none                      |
| `MENU`              | `menu.bss` (sprite)     | 12      | none                      |
| `SUBMENU`           | `submenu.bss` (sprite)  | 155     | none                      |

### Sprite Icons

Some icons are a region of a shared sprite sheet rather than a file of their
own. For those kinds (`MENU`, `SUBMENU`) `icon_path()` returns the sheet and
`icon_region(kind, id)` the `(x1, y1, x2, y2)` pixel region in it, from the
kind's entry in `ICON_REGION_INDEXES`; it returns `None` for whole-file kinds
and missing IDs.

A table shows one with `sprite_icon_cell(sheet_path, region)` from
`_common/html.py`: a sheet placeholder that loads nothing, since every row
shares the sheet. `icon_cell()` would draw the whole sheet.

### Icon Popup

A click on any icon cell opens a popup (`ui/js/features/icon-preview.js`)
with the image at its own size: scaled down to fit when larger than 1280
pixels, drawn larger with crisp pixels when small. For a sprite cell it also
shows the cropped sprite and outlines the region on the sheet. The backend is
`get_icon_preview(path, region)` in `api/bdo_api_preview.py`; it keeps the last
four decoded images, so every sprite of one sheet reuses a single decode, and
it runs under its own lock, so a click is not queued behind the icon cells
still loading. Thumbnails are unchanged: the popup reads the file itself.

### Fixing an icon by hand

`icon_path()` checks three tiers in order: override, index, derivation.

Overrides live in `_common/icon_overrides.json`, keyed by `IconKind.value` then
entity ID. They are repo data, not PAZ data, so they survive every index rebuild
and every game patch:

```json
{
  "item": { "222": "ui_texture/icon/new_icon/03_etc/00000222.dds" },
  "quest": {},
  "character": {}
}
```

An empty string means "this entity genuinely has no icon", which suppresses a
wrong derived guess rather than replacing it. A malformed file is reported by
`icon_override_error()` and ignored rather than crashing the app, so check that
helper if an override does not take effect.

Overrides are the intended fix for the ~535 IDs whose source table references an
icon the client does not ship. Those references do not change between patches,
so a correction made once keeps working.

When a referenced icon is not in the PAZ, the cell collapses to a dash rather
than leaving an empty swatch beside a path that resolves to nothing. The full
path stays in the cell's `title` attribute, so it is still there on hover. That
covers the roughly 535 IDs whose source table points at an icon the client does
not ship, until an override supplies the right path.

How far each index actually reaches differs a lot, so check before assuming an
icon column will look populated. Measured against the live PAZ:

| Kind        | IDs that exist | Resolve to a real file |
| ----------- | -------------- | ---------------------- |
| `ITEM`      | 73,790         | 93.8%                  |
| `QUEST`     | 19,486         | 83.9%                  |
| `CHARACTER` | 24,418         | 24.9%                  |
| `BUFF`      | 44,645         | 33.3%                  |

`CHARACTER` is low because only placeable world objects (mostly house
furniture) and the characters an item places or summons (fences, crops, pets)
have an icon, 6,068 of 24,418 IDs. NPCs and monsters have none. That is expected
rather than broken, but it means a character icon column is mostly empty.

The two equip-skill kinds are derivation only: no table stores their paths, but
routing them through the registry keeps every icon template in one module and
lets `icon_overrides.json` correct them like any other kind. Quest and character icons are named after
assets far more often than after their ID, so a guess would be wrong more often
than right; those kinds return an empty path and the cell renders a placeholder.

`BUFF` is low for the same reason: only 15,076 of 44,645 buffs store an icon,
mostly the shown buffs and the runs of hidden effects behind them. Of those,
14,884 files exist; the other 192 buffs point at 22 paths the client does not
ship.

The index matters because most item icons are not reachable from the ID. Of
~77,000 files under `ui_texture/icon`, the ID-named ones live in dozens of
per-category folders, and thousands more are named after a 3D asset
(`inhouse_cultivate_sea_clam_01_wall.dds`) with no numeric component at all.

| Item set                     | Derived from ID | With the index |
| ---------------------------- | --------------- | -------------- |
| All LOC type 0 IDs           | 14.9%           | 93.7%          |
| `npcgift.dbss` gift items    | 90%             | 100%           |

Cash-shop product icons are deliberately excluded. `cashproduct.dbss` links a
product to the item it grants, but its icon is the shop product art, not the
item's icon: item 1 (Silver) maps to `loyalties.dds`, the product that grants
it. Its icons differ from the item's own in every overlapping case, and it adds
no items that `itemenchant.dbss` does not already cover.

Handlers that read an icon path stored in their own records, such as `pet.dbss`,
`petaction.dbss`, `quest.dbss`, `plantworker.bss`, `itemenchant.dbss`,
`cashproduct.dbss`, `buff.dbss`, `buffsimply.bss` and `specialenchantitem.bss`, keep using that path directly. It is already authoritative,
and for `itemenchant`, `quest`, `buffsimply` and `specialenchantitem` the index is built from it, so routing those
through `icon_path()` would be circular.

## Localization

The app's active language code (`"en"`, `"de"`, `"fr"`, `"sp"`, `"ru"`, `"kr"`) is
available to every handler via `self.lang`. It is set automatically before any handler
method is called and updated whenever the user changes language in Settings. A change
drops every handler's `_data_cache` slots, since what they hold was built with the old
language's labels; the records cache keys on `self.lang` too.

Use it in `get_records()` to return language-appropriate display strings:

```python
_LABELS = {
    "en": {"active": "Active", "inactive": "Inactive"},
    "de": {"active": "Aktiv",  "inactive": "Inaktiv"},
    "kr": {"active": "활성",    "inactive": "비활성"},
}

class MyHandler(PreviewHandler):
    def get_records(self, data, entry, companions):
        labels = _LABELS.get(self.lang, _LABELS["en"])
        return [
            {"id": r.id, "status": labels["active"] if r.active else labels["inactive"]}
            for r in _parse(data)
        ]
```

For larger string sets, ship JSON files next to the handler and use the shared helper:

```python
from pathlib import Path
from _common.lang import load_handler_strings

_LANG_DIR = Path(__file__).parent / "lang"

class MyHandler(PreviewHandler):
    def get_records(self, data, entry, companions):
        s = load_handler_strings(self.lang, _LANG_DIR)
        ...
```

`load_handler_strings(lang, strings_dir)` reads `{strings_dir}/{lang}.json` and fills
every key it lacks, at any depth, from `{strings_dir}/en.json`. Returns `{}` if neither
file exists; a file that is not valid JSON is logged and treated as missing. Each table
is read once per language and shared between calls, so never change the dict it returns.

**Example `lang/en.json`** for a handler that displays category names and column headers:

```json
{
  "columns": {
    "id":       "Title ID",
    "category": "Category",
    "title":    "Title",
    "effect":   "Effect"
  },
  "category": {
    "0": "World",
    "1": "Combat",
    "2": "Life Skill",
    "3": "Fishing"
  }
}
```

A translation (`lang/de.json`) has the same keys with translated values. Name it after a
UI language code (the `ui/lang/*.json` names) and cover every key of `en.json` with the
same `{placeholders}`: `tests/test_handler_lang.py` fails on a missing or extra key, so a
handler is either English only or fully translated in a language. For text with values in
it, fill the placeholders with `fill_placeholders(text, name=value)` from `ui_text.py`,
the same rule `ui_text()` uses.

The count line above a table (`table(meta, ...)`) is handler text too: put it
in a `meta` block of `lang/en.json` and fill it with `handler_text()`, which
formats whole numbers with `,` in every language:

```python
meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), groups=group_count)
```

```json
"meta": {
  "count": "{count} quest references · {groups} groups"
}
```

A part added only sometimes (`meta += ...`) gets its own key with the leading
` · `. The simple examples elsewhere in this guide keep an English f-string for
brevity; a real handler uses `handler_text()`.

Text that belongs to a built-in viewer rather than one format (the hex, text and LOC
views) goes through `ui_text()` and the `ui/lang/*.json` files instead; the LOC viewer's
column labels, type names and count line are its `loc` section.

Rules:
- Always provide English (`"en"`) as the fallback, since `self.lang` may be a code your
  handler does not yet translate.
- Put translated strings in `get_records()` so they land in `records` dicts, which
  means tab search and CSV export also see the localized values.
- Do not put translated labels directly in `render_records_page()`, because the HTML layer
  should be format-agnostic.

## Import Rules

From a root handler:

```python
from _dbss.registration import register_dbss_handlers
```

From inside a format package:

```python
from _common.binary import u32
from _common.loc import parse_loc_entries
```

Avoid deep cross-format imports like:

```python
from _texture.some_internal_file import ...
```

If something is shared across formats, move it to `_common/`.

### Handler API

Handlers ship apart from the Windows exe as handler packs (see Handler Packs
below), so handler code may import only what every exe bundles.
`handler_api.py` lists it:

| List | Holds |
|------|-------|
| `CORE_MODULES` | `bdo_models`, `bdo_preview`, `record_fields`, `table_sort`, `ui_text` |
| `STDLIB_MODULES` | the standard library modules handlers use today (`struct`, `dataclasses`, `re`, ...) |
| `CORE_CALLED_COMMON` | the `_common` modules the core imports: `data_deps`, `html`, `loc`, `lookup_builders`, `lookup_index`, `pa_text` |

`tests/test_handler_imports.py` fails when handler code (anything under
`handlers/` but `test_*.py`) imports a module outside the first two lists, or
when the core imports a `_common` module outside the third. Test modules may
import anything, since packs ship without them.

`HANDLER_API` in the same file is the version of that contract; an exe loads
only a pack with the same number. Bump it only on a breaking change: a removed
or renamed function, or a changed signature or return shape, in a
`CORE_MODULES` module or a `CORE_CALLED_COMMON` module. Adding a module to an
allowlist is a bump too, since an older exe lacks it. Adding a function or a
handler is not.

### Handler Packs

A merge into `main` that changes `handlers/` publishes a handler pack, with no
new exe: the release workflow writes `manifest.json`
(`.github/scripts/handler_pack.py`) into the `handlers-latest` release, and
every exe with the same `HANDLER_API` downloads the changed files on its next
start. The pack is everything under `handlers/` except `test_*.py`, so a data
file a handler reads must live in that folder, and text files ship with LF
line endings.

A handler's version is the pack in which its code last changed: the module
that defines its class, the project modules that module imports (a `_common`
fix counts for every handler that imports it) and the JSON files next to
them, the files `source_fingerprint.project_files()` returns. A file the
handler opens by path without importing it is not in that set, so a change
to it alone leaves the version as it was.

## Required `__init__.py`

Every package folder should contain `__init__.py`.

Example:

```text
_dbss/
├── __init__.py
├── common/
│   └── __init__.py
└── title/
    └── __init__.py
```

This keeps imports predictable when handlers are loaded dynamically.

## Loader Requirement

The handlers folder has to be on `sys.path` before anything imports from it:
plugins import `_dbss.registration` and the like, and the core imports
`_common` (see Handler API). `use_handlers_dir()` in `bdo_preview.py` puts it
first on the path, and the entry points call it before importing the core:
`bdo_app.py` at the top, `benchmark.py` before `bench.cli`, and `conftest.py`
for the tests. `load_plugins()` calls it as well.

## Naming Conventions

Use clear names:

```text
handler.py
registration.py
binary.py
html.py
constants.py
```

Use one handler class per preview type when practical.

Good:

```python
class TitleDbssHandler(PreviewHandler):
    ...
```

Avoid vague names:

```python
class Handler(PreviewHandler):
    ...
```

## Error Handling

Return a visible error fragment for expected missing data.

```python
return '<div class="error">titleoffset.dbss companion not found.</div>'
```

Do not raise for normal missing companion files.

Raise only for actual programming errors.

## Checklist for a New Handler

1. Create a public root file if this is a new format.
2. Create a private implementation folder starting with `_`.
3. Add `__init__.py` to every package folder.
4. Create a `registration.py`.
5. Implement one or more `PreviewHandler` classes with `get_records()` and `render_records_page()`.
6. `get_records()` must return plain dicts, no HTML. Include any LOC-lookup strings here so tab search can find them. Use `self.lang` for language-aware display strings.
7. `render_records_page()` slices `records[page * page_size : ...]` and returns an HTML fragment.
8. Give sortable columns a `sort_key` and return `sort_keys(columns)` from `sortable_fields()` (see [Sortable Columns](#sortable-columns)).
9. Paging and search are lazy by default. For formats with a heavy internal structure, use `_data_cache()` to build the index once and override `render_data_page()` to parse only the requested page.
10. Register by exact filename or extension.
11. Escape all file-derived output (`e()` helper or `html.escape()`).
12. Use `companions()` for related files.
13. Add a handler-local `test_handler.py` with at least count and representative row tests.
14. Keep raw hex switching in the frontend, not the handler.
15. Move reusable logic to `_common/` when another format needs it.

> **Tip:** Press **Ctrl+R** in the GUI to reload all handlers without restarting the app. Changes to any file under `handlers/`, including private packages like `_dbss/`, take effect immediately. If a file is open on the Parsed tab, the preview re-renders automatically. Write and reload handlers in the source version: the Windows exe runs its bundled handlers and answers Ctrl+R with "Handler reload is only available when running from source".

## Minimal New Format Example

```text
handlers/
├── texture_handler.py
└── _texture/
    ├── __init__.py
    ├── registration.py
    └── dds/
        ├── __init__.py
        └── handler.py
```

```python
# handlers/texture_handler.py

from _texture.registration import register_texture_handlers

register_texture_handlers()
```

```python
# handlers/_texture/registration.py

from bdo_preview import register_handler

from .dds.handler import TextureDdsHandler


def register_texture_handlers() -> None:
    register_handler(".dds", TextureDdsHandler())
```

```python
# handlers/_texture/dds/handler.py

from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from _common.html import e, table

_HEADERS = [("Offset", "num", ""), ("Size", "num", "")]


class TextureDdsHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [{"offset": 0, "size": len(data)}]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        rows = [[e(r["offset"]), e(r["size"])] for r in slice_]
        return table(f"{len(records):,} records", _HEADERS, rows)
```

This is the simplest possible handler: `get_records()` is called once per file and the base class caches the result automatically. If the format requires a heavy parse (offset table, packed index), see the [Lazy Parsed Handlers](#lazy-parsed-handlers) section and use `_data_cache()` to build the index once.
