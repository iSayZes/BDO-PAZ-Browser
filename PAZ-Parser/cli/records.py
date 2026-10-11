"""`browser.py --records <file>`: a handler's parsed records on the command line.

Runs the registered handler's `get_records()`, the rows behind the GUI table
and its CSV export, with LOC and the lookup indexes loaded as the app loads
them. `--json` wraps the rows with the file, the client version and the
handler's key and version (`updates.handler_versions`), so a saved export says
which game data and which parser it came from.
"""
from __future__ import annotations

import argparse
from collections.abc import Sequence
from dataclasses import dataclass

from api.bdo_api import Api
from table_sort import SORT_ASC, SORT_DESC, TableSort, sort_order
from updates.handler_versions import handler_version

from .errors import CliError
from .parsed_file import ParsedFile, load_parsed_file
from .record_filter import Condition, check_fields, filter_records, parse_condition
from .record_output import OutputFormat, format_json, project, record_fields, write_records
from .session import open_session
from .stdio import error, progress, write_raw


@dataclass(frozen=True)
class Selection:
    records: list[dict]
    matched: int
    total: int


def parse_fields(text: str | None) -> list[str]:
    """`--fields a,b,c` as a list; empty when not given."""
    if not text:
        return []
    fields = [f.strip() for f in text.split(",") if f.strip()]
    if not fields:
        raise CliError("--fields needs at least one field name.")
    return fields


def parse_sort(text: str | None) -> TableSort | None:
    """`--sort field` or `--sort field:desc` as a table sort; None when not given."""
    if not text:
        return None
    field, _, direction = text.strip().partition(":")
    sort = TableSort.parse(field.strip(), direction.strip().lower() or SORT_ASC)
    if sort is None:
        raise CliError(f"cannot read --sort '{text}', use field, field:{SORT_ASC} or field:{SORT_DESC}.")
    return sort


def select_records(
    records: list[dict],
    conditions: Sequence[Condition],
    fields: Sequence[str],
    limit: int | None,
    sort: TableSort | None = None,
) -> Selection:
    """Filter, sort, cut to `limit`, then keep `fields`. Validates field names.

    Sorting follows the GUI table (`table_sort`): empty values last, text
    ignoring case, equal values in file order.
    """
    known = record_fields(records)
    if records:
        check_fields(conditions, known)
        wanted = [*fields, *([sort.field] if sort else [])]
        unknown = [f for f in wanted if f not in known]
        if unknown:
            raise CliError(
                f"unknown field(s) in --fields / --sort: {', '.join(unknown)}. Fields: {', '.join(known)}"
            )

    matched = filter_records(records, conditions)
    if sort is not None:
        matched = [matched[i] for i in sort_order(matched, sort.field, sort.descending)]
    shown = matched if limit is None else matched[:limit]
    return Selection(
        records=project(shown, fields) if fields else shown,
        matched=len(matched),
        total=len(records),
    )


def json_export(file: str, client_version: int | None, records: list[dict]) -> dict:
    """The `--records --json` document: the PAZ path, the client version, its handler key and version, and the rows.

    `client_version` is the `.meta` header version. `handler_version`
    is None from source without git, or when the pack manifest lacks the key.
    """
    found = handler_version(file)
    return {
        "file": file,
        "client_version": client_version,
        "handler": found.key if found is not None else None,
        "handler_version": found.version if found is not None else None,
        "records": records,
    }


def write_selection(api: Api, parsed: ParsedFile, records: list[dict], output: OutputFormat) -> None:
    if output is OutputFormat.JSON:
        write_raw(format_json(json_export(parsed.entry.internal_path, api.meta_version, records)))
    else:
        write_records(records, output)


def output_format(args: argparse.Namespace) -> OutputFormat:
    if args.json:
        return OutputFormat.JSON
    if args.csv:
        return OutputFormat.CSV
    return OutputFormat.TABLE


def run_records(args: argparse.Namespace) -> int:
    try:
        # Read the options before the slow folder load, so a typo fails at once.
        conditions = [parse_condition(text) for text in args.where]
        fields = parse_fields(args.fields)
        sort = parse_sort(args.sort)
        output = output_format(args)

        api = open_session(args.paz_folder, load_loc=not args.no_loc)
        parsed = load_parsed_file(api, args.records)
        progress(f"Parsing {parsed.entry.internal_path}…")
        selection = select_records(parsed.records(), conditions, fields, args.limit, sort)
    except CliError as ex:
        error(str(ex))
        return 1

    write_selection(api, parsed, selection.records, output)
    progress(
        f"{len(selection.records):,} shown, {selection.matched:,} matched, "
        f"{selection.total:,} records in {parsed.entry.internal_path}."
    )
    return 0
