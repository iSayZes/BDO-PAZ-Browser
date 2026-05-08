"""Handler-local string table loader with English fallback."""

from __future__ import annotations

import json
from pathlib import Path


def load_handler_strings(lang: str, strings_dir: str | Path) -> dict:
    """Load a handler's string table for *lang* from *strings_dir*.

    Looks for ``{strings_dir}/{lang}.json``. Falls back to
    ``{strings_dir}/en.json`` when the requested language file is absent.
    Returns an empty dict if neither file exists.

    Typical usage inside a handler package::

        from pathlib import Path
        from _common.lang import load_handler_strings

        _LANG_DIR = Path(__file__).parent / "lang"

        class MyHandler(PreviewHandler):
            def get_records(self, data, entry, companions):
                s = load_handler_strings(self.lang, _LANG_DIR)
                ...
    """
    strings_dir = Path(strings_dir)
    for candidate in (strings_dir / f"{lang}.json", strings_dir / "en.json"):
        try:
            return json.loads(candidate.read_text(encoding="utf-8"))
        except FileNotFoundError:
            continue
    return {}
