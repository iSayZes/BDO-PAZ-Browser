# BDO PAZ Browser & Binary Format Tools

> **Work in progress.** Format coverage is incomplete and the API may change. Contributions and corrections are welcome.

A Python tool for browsing, extracting, and previewing files from **Black Desert Online**'s `.paz` game archives, with a plugin system for parsing BDO-specific binary formats.

---

## Features

- **GUI browser** — tree-view file explorer for the full PAZ archive, with live search and file preview
- **CLI extraction** — extract files by name or glob pattern without opening the GUI
- **File preview** — text, hex dump, DDS images, and parsed binary tables for known formats
- **Plugin system** — add handlers for new binary formats by dropping a file into `handlers/`
- **Caching** — PAZ index is parsed once and cached; subsequent launches load instantly

---

## Documented Formats

| File                     | Description                                                  | Docs                                                               |
| ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------------ |
| `languagedata_en.loc`    | Localization string table (zlib-compressed, UTF-16-LE)       | [loc](docs/file-formats/languagedata_loc.md)                     |
| `title.dbss`             | Title record table (multiple layouts, embedded PAColor text) | [title](docs/file-formats/title_dbss.md)                         |
| `titleoffset.dbss`       | Index into `title.dbss` — maps title ID → offset/size        | [titleoffset](docs/file-formats/titleoffset_dbss.md)             |
| `titlebufflist.dbss`     | Title collection buff rewards (KR text + LOC tooltip match)  | [titlebufflist](docs/file-formats/titlebufflist_dbss.md)         |
| `titlecategory.bss`      | Groups titles into display categories                        | [titlecategory](docs/file-formats/titlecategory_bss.md)          |
| `mentalcard.dbss`        | Knowledge entry → node/category ID mapping                   | [mentalcard](docs/file-formats/mentalcard_dbss.md)               |
| `knowledgelearning.dbss` | Mob ID → knowledge ID mapping (kind 13 records)              | [knowledgelearning](docs/file-formats/knowledgelearning_dbss.md) |
| `npcpersonality.dbss`    | NPC personality ID → type refs + behavioural float params    | [npcpersonality](docs/file-formats/npcpersonality_dbss.md)         |

All formats are little-endian. Unknown fields are named `unknown_*`.

---

## Requirements

- Python 3.10+
- [pywebview](https://pywebview.flowrl.com/) — GUI shell
- [Pillow](https://python-pillow.org/) — optional, for DDS image preview

```
pip install pywebview
pip install pillow        # optional
```

Or install from the provided requirements file:

```
pip install -r PAZ-Parser/requirements.txt
```

---

## Usage

### GUI

```bash
python PAZ-Parser/bdo_app.py
```

On first launch, click **Open Folder** and select your BDO PAZ directory (typically `Black Desert/Paz`). The index is parsed and cached — subsequent launches load from cache automatically.

### CLI

```bash
# List files matching a pattern
python PAZ-Parser/bdo_app.py --paz-folder "C:/Games/Black Desert/Paz" --list "title*.dbss"

# Extract files matching a pattern
python PAZ-Parser/bdo_app.py --paz-folder "C:/Games/Black Desert/Paz" --file "title.dbss" --output ./out

# Glob extraction
python PAZ-Parser/bdo_app.py --paz-folder "C:/Games/Black Desert/Paz" --file "*title*" --output ./out
```

If `--paz-folder` is omitted, the CLI reuses the last folder opened in the GUI.

---

## Project Structure

```
PAZ-Parser/
├── bdo_app.py              # Entry point — GUI + CLI
├── bdo_api.py              # pywebview JS API bridge
├── bdo_paz_reader.py       # PAZ archive parser
├── bdo_paz_extract.py      # File extraction logic
├── bdo_meta_reader.py      # Meta file reader
├── bdo_payload_reader.py   # Payload decompression + ICE decryption
├── bdo_cache.py            # PAZ index cache
├── bdo_models.py           # Data models
├── bdo_ice.py              # ICE cipher implementation
├── bdo_preview.py          # Preview handler registry + built-in handlers
│
├── ui/                     # Web UI (HTML + JS + CSS)
│   ├── index.html
│   ├── app.js
│   └── style.css
│
└── handlers/               # Format preview plugins (auto-loaded)
    ├── dbss_handler.py     # DBSS entry point
    ├── _dbss/              # DBSS format implementations
    │   ├── common/         # Shared binary/HTML helpers
    │   ├── title/
    │   ├── titleoffset/
    │   ├── titlebuff/
    │   ├── mentalcard/
    │   └── knowledgelearning/
    └── _common/            # Helpers shared across formats
        └── loc.py

docs/
├── handler.md              # Guide for writing preview handlers
├── style-guide.md          # UI color palette and component reference
└── file-formats/           # Per-format binary layout documentation
```

---

## Writing a Preview Handler

Drop a `.py` file (not starting with `_`) into `handlers/` — it is auto-loaded at startup.

```python
# handlers/myformat_handler.py
from bdo_preview import PreviewHandler, register_handler
from bdo_models import PazEntry

class MyFormatHandler(PreviewHandler):
    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        return f"<pre>{len(data):,} bytes</pre>"

register_handler("myfile.dbss", MyFormatHandler())
```

See [docs/handler.md](docs/handler.md) for the full guide, including companion files, shared helpers, and registration patterns.

> **Tip:** Press **Ctrl+R** in the GUI to reload all handlers without restarting the app. If you have a file open on the Parsed tab, the preview re-renders automatically with the updated handler.

---

## Disclaimer

This project is for research purposes only. BDO game data is copyright Pearl Abyss. Do not redistribute extracted game assets.
