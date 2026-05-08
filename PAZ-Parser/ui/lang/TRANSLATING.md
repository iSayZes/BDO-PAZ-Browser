# Translating BDO PAZ Browser

## Files

Each language has one JSON file in this folder:

| File | Language |
|------|----------|
| `en.json` | English (source — do not translate) |
| `de.json` | Deutsch |
| `fr.json` | Français |
| `sp.json` | Español |
| `ru.json` | Русский |
| `kr.json` | 한국어 |

## How to translate

1. Open the target language file (e.g. `de.json`).
2. Copy the key structure from `en.json` and replace the English values with your translations.
3. Add your name to the `_meta.authors` array.

Any key you leave out falls back to the English string automatically — you do not need to translate everything at once.

## Example

`en.json` (reference):
```json
{
  "toolbar": {
    "openFolder": "📂 Open PAZ Folder"
  }
}
```

`de.json` (partial translation):
```json
{
  "_meta": {
    "language": "Deutsch",
    "code": "de",
    "authors": ["yourname"]
  },
  "toolbar": {
    "openFolder": "📂 PAZ-Ordner öffnen"
  }
}
```

## Rules

- Keep emoji and punctuation that is part of the original string (e.g. `📂`, `⬇`, `✕`).
- Do not translate the `_meta` block keys (`language`, `code`, `authors`, `notes`).
- Do not modify `en.json` — it is the source of truth.
- String values only — do not add new keys that do not exist in `en.json`.
