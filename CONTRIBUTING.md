# Contributing

Thanks for helping out. BDO has hundreds of undocumented binary formats, so research notes, corrections and small fixes are all useful, not only code.

## Ways to Contribute

- **Research a new format.** Open an issue with the [file format template](../../issues/new?template=file-format.yml) and title it `filename.ext` (e.g. `yachtdicepreset.dbss` or `.pac`). Hex observations and layout guesses are welcome, even if incomplete.
- **Answer an open question.** Every doc in [`docs/file-formats/`](docs/file-formats/) ends with an **Open Questions** section. If you can answer one, edit the doc directly and open a pull request.
- **Document a format.** Start from [`docs/file-formats/_template.md`](docs/file-formats/_template.md) and add the format to [`docs/documented-formats.md`](docs/documented-formats.md).
- **Write a preview handler.** Follow [`docs/handler.md`](docs/handler.md), including the [checklist for a new handler](docs/handler.md#checklist-for-a-new-handler).
- **Translate the UI.** See [`PAZ-Parser/ui/lang/TRANSLATING.md`](PAZ-Parser/ui/lang/TRANSLATING.md). Partial translations are fine, since missing keys fall back to English.
- **Report a bug or suggest a feature.** Use the [issue templates](../../issues/new/choose).

## Setup

You need Python 3.14 and a local Black Desert Online install, since tests read their inputs from your PAZ folder. Without one, the tests that need game files are skipped.

```bash
python -m pip install -r PAZ-Parser/requirements-dev.txt
python browser.py
```

Open your `Black Desert/Paz` folder once in the GUI, so the tests know where to fetch fixtures from.

## Branches and Pull Requests

- Branch from `staging` and open the pull request into `staging`, not `main`. `main` holds the released state and only moves with a release.
- The pull request title is a [Conventional Commit](https://www.conventionalcommits.org/) subject (see Conventions). Pull requests are squash merged, so the title becomes the commit on `staging` and a line in the release notes.
- Open unfinished work as a draft pull request.
- Releases are pull requests from `staging` into `main`, opened by the maintainer. A release with handler changes only publishes a handler pack, which the Windows exe downloads on start, and no new exe.

CI runs pyright and the tests on every pull request. Its runner has no game client, so it skips the tests that need game files; the full run is the local one below.

## Before Opening a Pull Request

Run both from the repo root. Both must pass with no errors:

```bash
python -m pytest --clean
python -m pyright
```

Docs-only changes can skip them.

Also check that:

- Docs match the change. If you change a handler, format layout, CLI option or config, update the matching doc in the same pull request.
- No extracted game files are committed. Test fixtures are fetched from your own install into a gitignored folder; never add game data to the repo.

## Conventions

- **Unknown fields** are named `unknown_<offset>` (e.g. `unknown_10`) until their meaning is confirmed. Don't guess a name; describe the observation in the doc's Open Questions instead.
- **One doc per record layout.** Every `.bss` / `.dbss` gets its own doc in `docs/file-formats/`, named after the file (`dropuitaginfo_bss.md`). Only an `*offset.dbss` index, which goes in its main file's doc, and files that share one layout and one handler class (`ui_skillgroup_{awakening,combat,succession}.bss` in `ui_skillgroup_bss.md`) share a doc. The Companion Files table lists the files a handler loads and links each one to its own doc.
- **Tests survive game patches.** Assert structure and stable identity (schemas, ranges, known IDs), never row counts, positions or balance values that change with an update.
- **Text columns** use the loaded LOC language first, then fall back to the inline Korean text.
- **Small, focused files.** Split code by responsibility and reuse the shared helpers in `handlers/_common/` and `handlers/_dbss/common/` rather than copying them.
- **Commit messages** follow [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `perf:`, `docs:`, `refactor:`, `test:`, `ci:`, `style:`. Release notes list `feat`, `fix`, `perf` and `refactor` commits that change the app or a handler. Keep the subject short and say what it adds or changes, e.g. `feat: add the buffsimply.bss handler and buff icons` or `feat: blizzardregioninfo and edaniaregioninfo tables`.

## Code of Conduct

By taking part you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
