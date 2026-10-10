# Translating BDO PAZ Browser

## Files

Each language has one JSON file in this folder:

| File | Language |
|------|----------|
| `en.json` | English (source, do not translate) |
| `de.json` | Deutsch |
| `fr.json` | Français |
| `sp.json` | Español |
| `ru.json` | Русский |
| `kr.json` | 한국어 |

## How to translate

1. Open the target language file (e.g. `de.json`).
2. Copy the key structure from `en.json` and replace the English values with your translations.
3. Add your name to the `_meta.authors` array.

Any key you leave out falls back to the English string in the app, so a partial file still works while you translate. The test suite (`tests/test_ui_text.py`) does require every shipped language file to cover every key of `en.json`, with the same `{placeholders}`.

The same files hold the text the Python side builds: error messages (`errors`), the Save dialog filters (`dialogs`), byte units (`units`), the preview's error boxes and tab labels (`preview`) and the LOC viewer's column labels, type names and count line (`loc`). `ui_text.py` reads them like `t()` does in the page.

The parsed tables of each file format keep their column labels in the handler's own folder, `handlers/<group>/<format>/lang/en.json`. A translation there is `<code>.json` next to it, with every key of that `en.json` (`tests/test_handler_lang.py` checks this per file).

## Game terms

Use the words the game client uses in that language, so a column reads like the game's own UI. Each `languagedata_<code>.loc` stores the same row under the same key as `languagedata_en.loc`, so pairing the two gives the client's word for an English term. German, for example, says Talent (skill), Posten (node), Stufe (level), Rang (grade, tier), Gegenstand (item), Begleiter (pet), AK / VK (AP / DP), EP (EXP), Verstärkung (enhancement) and Postenwart (node manager). French uses Compétence, Géopoint, Niveau, Objet, Familier, PA / PD, Optimisation and Cartographe; Spanish Habilidad, Nodo, Nivel, Objeto, Mascota, Ataque / Defensa, Refuerzo and Responsable de nodo; Russian Навык, Узел, Уровень, Предмет, Питомец, Атака / Защита, Усиление, Управляющий узлом and НИП for NPC. Korean has no LOC file, since the Korean client keeps its text in the game tables: `stringtable.bss` holds the Korean UI text under the same key hash as the English LOC type 37 rows, which gives 기술 (skill), 거점 (node), 반려동물 (pet), 일꾼 (worker), 의뢰 (quest), 공격력 / 방어력, 강화 and 거점 관리인. Where one table would show the same word twice (pet Tier and Grade are both Rang in German), pick a second word for one of them.

## Example

`en.json` (reference):
```json
{
  "toolbar": {
    "openFolder": "Open PAZ Folder"
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
    "openFolder": "PAZ-Ordner öffnen"
  }
}
```

## Rules

- Keep punctuation and placeholders such as `{count}` that are part of the original string. Strings hold no emoji; the UI draws its icons next to the text.
- Do not translate the `_meta` block keys (`language`, `code`, `authors`, `notes`).
- Do not modify `en.json`, it is the source of truth.
- String values only, do not add new keys that do not exist in `en.json`.
- Keep every `{placeholder}` of the English string; the words around it can move.
- Plural pairs (`matchOne` / `matchMany`, `fileOne` / `fileMany`): if the language has no simple singular and plural, use one wording for both, such as `Совпадений: {count}`.

## Adding UI text (developers)

Never write user-visible text straight into HTML, JS or Python UI code:

- HTML: a `data-i18n`, `data-i18n-title` or `data-i18n-placeholder` attribute with the key.
- JS: `t("section.key", { args })` from `js/core/i18n.js`.
- Python: `ui_text("section.key", name=value)` from `ui_text.py`.

Add the key to `en.json` and translate it in every other file in the same change.

## Adding a UI language (developers)

`api/bdo_languages.py` lists all 13 languages the game ships text in, with the game's own
code (`PA_LT_<pa_type>`) and the LOC file name. The settings list the ones with
`has_ui=True`. To add one:

1. Add `<code>.json` here, with the code from `GAME_LANGUAGES`.
2. Set `has_ui=True` on its entry, and fill in `loc_file` once a client of that region or
   its CDN index (`/UploadData/ads_files`) confirms the file name (only Korean needs none:
   its text is in the tables).

`tests/test_languages.py` fails while the shipped JSON files and the `has_ui` languages
differ, or while a UI language other than Korean has no LOC file name.
