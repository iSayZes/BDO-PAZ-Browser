"""The contract between the app core and the handlers, and its version.

Handlers ship apart from the Windows exe as handler packs: the `handlers/`
folder of one commit, downloaded by an exe that may be older or newer than
the pack (`updates/handler_packs.py`). A pack and an exe fit when their
`HANDLER_API` matches.

Two sides make up the contract:

- What handler code may import: the core modules in `CORE_MODULES` and the
  standard library modules in `STDLIB_MODULES`. The exe bundles exactly
  these, so a pack can never need a module an older exe lacks.
  `tests/test_handler_imports.py` fails on any other import.
- What the core calls in handler code: the `_common` modules in
  `CORE_CALLED_COMMON`.

Bump `HANDLER_API` only on a breaking change to either side: a removed or
renamed function, a changed signature or return shape in a `CORE_MODULES`
module or a `CORE_CALLED_COMMON` module. Adding a function, or a handler, is
not breaking. Adding a module to an allowlist needs a new exe, so it is a bump
too. `docs/handler.md` (Handler API) repeats the rule.
"""

from __future__ import annotations

HANDLER_API = 1

# Core modules handler code may import.
CORE_MODULES = frozenset({
    "bdo_models",
    "bdo_preview",
    "record_fields",
    "table_sort",
    "ui_text",
})

# Standard library modules handler code may import.
STDLIB_MODULES = frozenset({
    "__future__",
    "codecs",
    "collections",
    "contextlib",
    "dataclasses",
    "enum",
    "functools",
    "html",
    "json",
    "logging",
    "math",
    "pathlib",
    "re",
    "string",
    "struct",
    "sys",
    "threading",
    "types",
    "typing",
    "zlib",
})

# `_common` modules the core imports (`api/`, `cli/`, `bench/stages.py`).
CORE_CALLED_COMMON = frozenset({
    "_common.data_deps",
    "_common.html",
    "_common.loc",
    "_common.lookup_builders",
    "_common.lookup_index",
    "_common.pa_text",
})
