from __future__ import annotations

from pathlib import Path
from time import perf_counter

from bdo_models import PazEntry
from bdo_preview import get_handler

from .fixtures import ensure_fixtures
from .loc_counter import null_loc_counter, patch_loc_counter, reset_loc
from .models import HandlerCase, HandlerResult


def run_case(case: HandlerCase) -> HandlerResult:
    fixture_paths = ensure_fixtures(case)
    reset_loc()

    data = fixture_paths[str(case.data_file)].read_bytes()
    companions = {
        basename: fixture_paths[str(relative_path)].read_bytes()
        for basename, relative_path in case.companion_files.items()
    }

    if case.loc_file is not None:
        from _common.loc import init_loc

        init_loc(fixture_paths[str(case.loc_file)].read_bytes())

    loc_counter = patch_loc_counter() if case.uses_loc else null_loc_counter()
    with loc_counter as loc_stats:
        entry = PazEntry(
            archive_name="",
            internal_path=case.internal_path,
            offset=0,
            compressed_size=0,
            uncompressed_size=0,
            compression_type=0,
            encryption_type=0,
        )
        suffix = Path(case.internal_path).suffix
        handler = get_handler(Path(case.internal_path).name, suffix)

        start = perf_counter()
        records = handler.get_records(data, entry, companions)
        elapsed_ms = (perf_counter() - start) * 1000

    if case.record_mapper is not None:
        records = [case.record_mapper(record) for record in records]

    result = HandlerResult(
        row_count=len(records),
        elapsed_ms=elapsed_ms,
        loc_total_calls=loc_stats.total,
        loc_fallback_count=loc_stats.misses,
        records=records,
    )
    for spec in case.tests:
        try:
            result.passed.append(spec.check(records))
        except AssertionError as exc:
            result.failed.append(str(exc))

    return result
