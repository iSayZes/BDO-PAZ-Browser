# Handler Guide

This guide explains how custom preview handlers should be structured, loaded, and registered.

## Loader Rules

The browser loads handlers from the `handlers/` folder at startup.

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

---

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

---

## Public Entry File

A public entry file should stay small.

Example:

```python
# handlers/dbss_handler.py

from _dbss.registration import register_dbss_handlers

register_dbss_handlers()
```

The entry file exists so the plugin loader can discover the handler package.

---

## Registration File

Group all registrations for one format in a registration module.

```python
# handlers/_dbss/registration.py

from bdo_preview import register_handler

from .titleoffset.handler import TitleOffsetHandler
from .title.handler import TitleDbssHandler
from .titlebuff.handler import (
    TitleBuffListOffsetHandler,
    TitleBuffListHandler,
)


def register_dbss_handlers() -> None:
    register_handler("titleoffset.dbss", TitleOffsetHandler())
    register_handler("title.dbss", TitleDbssHandler())
    register_handler("titlebufflistoffset.dbss", TitleBuffListOffsetHandler())
    register_handler("titlebufflist.dbss", TitleBuffListHandler())
```

---

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

---

## Handler Template

All parsed-view handlers must implement `get_records()` and `render_records_page()`.

- `get_records()` — parses the binary once and returns all records as plain dicts (no HTML). The result is cached for paging, tab search, and CSV export.
- `render_records_page()` — converts one page of cached records into an HTML fragment.

```python
# handlers/_example/myfile/handler.py

from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from _dbss.common.html import e, table


_HEADERS = [
    ("ID",   "num", ""),
    ("Name", "",    ""),
]


class MyFileHandler(PreviewHandler):
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
        return table(meta, _HEADERS, rows)
```

---

## Lazy Parsed Handlers

Large formats can opt into lazy parsed records so the browser can page and search
without materializing every row during file selection.

Override `supports_lazy_records()` and provide count, page, and search methods:

```python
class LargeFileHandler(PreviewHandler):
    def supports_lazy_records(self) -> bool:
        return True

    def get_record_count(self, data, entry, companions) -> int:
        return _index(data).count

    def render_data_page(self, data, entry, companions, page, page_size) -> str:
        records = _index(data).records_for_page(page, page_size)
        return _render_table(records, page, page_size)

    def search_records(self, data, entry, companions, query) -> list[int]:
        return _index(data).search(query)
```

Keep `get_records()` implemented as a compatibility fallback for CSV export and
non-lazy callers. Handlers that do not opt in keep the original eager behavior.

---

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

---

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

Example:

```python
offset_raw = companions.get("titleoffset.dbss")
loc_raw = companions.get("languagedata_en.loc")
```

Disk files pre-loaded by the browser may also be merged into `companions`.

For example:

```python
companions.get("languagedata_en.loc")
```

---

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
from _dbss.common.html import table, error
```

---

## Raw Hex Preview

Handlers should only render their parsed preview.

The main preview UI is responsible for switching between:

- Parsed preview
- Raw hex preview

Do not manually include raw hex tabs inside individual handlers.

This keeps all handlers consistent.

---

## Shared Helpers

Use `_common/` for helpers shared by multiple formats.

Examples:

```text
_common/
├── loc.py
├── binary.py
└── html.py
```

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

---

## Import Rules

From a root handler:

```python
from _dbss.registration import register_dbss_handlers
```

From inside a format package:

```python
from _dbss.common.binary import u32
from _common.loc import parse_loc_entries
```

Avoid deep cross-format imports like:

```python
from _texture.some_internal_file import ...
```

If something is shared across formats, move it to `_common/`.

---

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

---

## Loader Requirement

The plugin loader should add `handlers/` to `sys.path` before importing plugins.

```python
handlers_path = str(handlers_dir.resolve())

if handlers_path not in sys.path:
    sys.path.insert(0, handlers_path)
```

Without this, imports like this may fail:

```python
from _dbss.registration import register_dbss_handlers
```

---

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

---

## Error Handling

Return a visible error fragment for expected missing data.

```python
return '<div class="error">titleoffset.dbss companion not found.</div>'
```

Do not raise for normal missing companion files.

Raise only for actual programming errors.

---

## Checklist for a New Handler

1. Create a public root file if this is a new format.
2. Create a private implementation folder starting with `_`.
3. Add `__init__.py` to every package folder.
4. Create a `registration.py`.
5. Implement one or more `PreviewHandler` classes with `get_records()` and `render_records_page()`.
6. `get_records()` must return plain dicts — no HTML. Include any LOC-lookup strings here so tab search can find them.
7. `render_records_page()` slices `records[page * page_size : ...]` and returns an HTML fragment.
8. For very large formats, optionally implement lazy parsed methods so paging and search do not require eager parsing.
9. Register by exact filename or extension.
10. Escape all file-derived output (`e()` helper or `html.escape()`).
11. Use `companions()` for related files.
12. Keep raw hex switching in the frontend, not the handler.
13. Move reusable logic to `_common/` when another format needs it.

> **Tip:** Press **Ctrl+R** in the GUI to reload all handlers without restarting the app. Changes to any file under `handlers/` — including private packages like `_dbss/` — take effect immediately. If a file is open on the Parsed tab, the preview re-renders automatically.

---

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
from _dbss.common.html import e, table

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
