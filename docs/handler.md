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

```python
# handlers/_example/myfile/handler.py

from __future__ import annotations

import html

from bdo_models import PazEntry
from bdo_preview import PreviewHandler


class MyFileHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]

        return [
            f"{folder}/myindex.dbss",
        ]

    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        safe_name = html.escape(entry.internal_path)
        size = len(data)

        return (
            f'<div class="table-meta">{safe_name} · {size:,} B</div>'
        )
```

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

Companion files are passed into `render()` as:

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
5. Implement one or more `PreviewHandler` classes.
6. Register by exact filename or extension.
7. Escape all file-derived output.
8. Use `companions()` for related files.
9. Keep raw hex switching in the frontend, not the handler.
10. Move reusable logic to `_common/` when another format needs it.

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


class TextureDdsHandler(PreviewHandler):
    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        return f'<div class="table-meta">{len(data):,} B</div>'
```
