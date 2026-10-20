# Contributing

Thanks for helping out. BDO has hundreds of undocumented binary formats, so research notes, corrections and small fixes are all useful, not only code.

## Ways to Contribute

- **Research a new format.** Open an issue with the [file format template](../../issues/new?template=file-format.yml) and title it `filename.ext` (e.g. `yachtdicepreset.dbss` or `.pac`). Hex observations and layout guesses are welcome, even if incomplete.
- **Answer an open question.** Every doc in [`docs/file-formats/`](docs/file-formats/) ends with an **Open Questions** section. If you can answer one, edit the doc directly and open a pull request.
- **Run an in-game check.** Some docs end with an **In-Game Checks** section after Open Questions: a test that needs a character with a given item, quest, NPC, class or zone, and what each result means. You don't need to read the binary layout to answer one; post the result in an issue or edit the doc.
- **Document a format.** Start from [`docs/file-formats/_template.md`](docs/file-formats/_template.md), write the layout tables as [Writing Format Docs](docs/format-docs.md) describes, and add the format to [`docs/documented-formats.md`](docs/documented-formats.md).
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

The compiled decoders are optional. With a Rust toolchain installed, `python -m pip install ./PAZ-Parser/native` builds them, and the tests then also check them against the Python and numpy versions. Install it again after changing the Rust code.

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

- **Format docs follow [Writing Format Docs](docs/format-docs.md).** It holds every doc rule: which files get a doc, section order, layouts, types and field names. Unconfirmed fields are `unknown_<offset>`; don't guess a name, describe the observation in the doc's Open Questions.
- **Format docs pass `pytest` and fit the game files.** `PAZ-Parser/tests/test_format_docs.py` checks every doc's layout tables (types, sizes, offsets, field names), and every `.bss` / `.dbss` doc must have them. `python check_docs.py <doc>.md` walks the doc's files from your PAZ folder by its layouts and writes its `## Versions` section; don't edit that section by hand.
- **Tests survive game patches.** Assert structure and stable identity (schemas, ranges, known IDs), never row counts, positions or balance values that change with an update.
- **Counts in docs name their client.** A figure counted from game data carries the client it came from, e.g. "`1` on 4,643 records (client 3458)", and stays as written after a patch. The client number is the `.meta` header version that `pytest` prints at the start of a run.
- **Text columns** use the loaded LOC language first, then fall back to the inline Korean text.
- **Small, focused files.** Split code by responsibility and reuse the shared helpers in `handlers/_common/` and `handlers/_dbss/common/` rather than copying them.
- **Commit messages** follow [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `perf:`, `docs:`, `refactor:`, `test:`, `ci:`, `style:`. Release notes list `feat`, `fix`, `perf` and `refactor` commits that change the app or a handler. Keep the subject short and say what it adds or changes, e.g. `feat: add the buffsimply.bss handler and buff icons` or `feat: blizzardregioninfo and edaniaregioninfo tables`.

## Contact

For questions about a format, a handler or a pull request, add me on Discord: `sayzes`.

## Code of Conduct

By taking part you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
