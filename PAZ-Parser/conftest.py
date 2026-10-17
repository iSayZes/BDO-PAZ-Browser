from __future__ import annotations

from collections.abc import Iterator
from dataclasses import replace
import gc
import os
import sys
import time
from pathlib import Path
from typing import Any

import pytest

PAZ_PARSER_DIR = Path(__file__).parent.resolve()
TESTS_DIR = PAZ_PARSER_DIR / "tests"
HANDLERS_DIR = PAZ_PARSER_DIR / "handlers"
FIXTURES_DIR = Path(
    os.environ.get("PAZ_PARSER_FIXTURES_DIR", TESTS_DIR / "fixtures")
).resolve()

for path in (PAZ_PARSER_DIR, HANDLERS_DIR):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)


@pytest.fixture(autouse=True)
def _english_after_each_test() -> Iterator[None]:
    # set_handler_lang() is process-wide, and BdoApi applies the saved
    # language when it is built or saves settings; tests expect English.
    yield
    from bdo_preview import set_handler_lang

    set_handler_lang("en")


def _is_xdist_worker(config: pytest.Config) -> bool:
    return hasattr(config, "workerinput")


def pytest_collection_finish(session: pytest.Session) -> None:
    # An xdist worker runs only the cases of the handler modules it is sent
    # (see pytest_collection_modifyitems), through each module's own result
    # fixture, instead of every case up front.
    if not _is_xdist_worker(session.config):
        _run_handler_cases(session)

    # The handler results stay alive for the whole session. Freezing them
    # keeps every later collection (bench.timing calls gc.collect() per run)
    # from walking millions of record objects.
    gc.collect()
    gc.freeze()


def _run_handler_cases(session: pytest.Session) -> None:
    """Run each collected module's CASE once and keep the result on the module."""
    # --clean keeps the output to failures and the pass/total line.
    reporter = None
    if not session.config.getoption("--clean"):
        reporter = session.config.pluginmanager.get_plugin("terminalreporter")
    modules: set[Any] = set()

    for item in session.items:
        module = getattr(item, "module", None)
        if module is None or module in modules:
            continue

        modules.add(module)
        case = getattr(module, "CASE", None)
        if case is None or getattr(module, "_HANDLER_RESULT", None) is not None:
            continue

        from tests.framework import run_case

        try:
            result = run_case(replace(case, tests=[]))
        except pytest.skip.Exception:
            # No client: the module's own result fixture skips its tests.
            continue
        setattr(module, "_HANDLER_RESULT", result)

        if reporter is not None:
            loc = "disabled"
            if result.loc_total_calls is not None and result.loc_fallback_count is not None:
                loc = (
                    f"{result.loc_fallback_count:,} misses / "
                    f"{result.loc_total_calls:,} lookups"
                )
            reporter.write_sep("=", case.handler_name)
            reporter.write_line(f"rows:   {result.row_count:,}")
            reporter.write_line(f"parse:  {result.elapsed_ms:.0f} ms")
            reporter.write_line(f"loc:    {loc}")


# Before xdist's own hook, which reads the xdist_group marks.
@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    items.sort(key=lambda item: (item.path.name if item.path else "", item.name))
    if _is_xdist_worker(config):
        _group_handler_modules(items)
        return
    for item in items:
        item._nodeid = item.name


def _group_handler_modules(items: list[pytest.Item]) -> None:
    """Keep each handler test module on one xdist worker under `--dist loadgroup`.

    Its module fixtures then parse the case once, not once per worker that
    gets one of its tests. Node IDs keep their paths: the short names repeat
    across handler modules, and xdist matches the workers' collections by ID.
    """
    for item in items:
        if item.path is not None and item.path.is_relative_to(HANDLERS_DIR):
            item.add_marker(pytest.mark.xdist_group(item.path.relative_to(HANDLERS_DIR).as_posix()))


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--clean",
        action="store_true",
        default=False,
        help="Show only failed tests and a pass/total summary",
    )
    parser.addoption(
        "--refresh-fixtures",
        action="store_true",
        default=False,
        help="Fetch every fixture again from the installed client, even if it did not change",
    )
    parser.addoption(
        "--frozen-fixtures",
        action="store_true",
        default=False,
        help="Use the cached fixtures as they are, without checking the installed client",
    )


def pytest_configure(config: pytest.Config) -> None:
    if config.getoption("--refresh-fixtures") and config.getoption("--frozen-fixtures"):
        raise pytest.UsageError("--refresh-fixtures and --frozen-fixtures cannot be combined")
    if config.getoption("--clean", default=False):
        config.pluginmanager.register(_CleanPlugin(config), "clean_plugin")


def pytest_sessionstart(session: pytest.Session) -> None:
    # Before collection: pytest_collection_finish() already runs handlers.
    import bdo_preview

    bdo_preview.load_plugins(bdo_preview.BUNDLED_HANDLERS_DIR)

    config = session.config
    # Under pytest-xdist the controller syncs before it starts the workers,
    # which then only read the fixtures.
    if config.getoption("--frozen-fixtures") or hasattr(config, "workerinput"):
        return

    from tests.fixture_sync import sync_fixtures
    from tests.fixtures import FixtureFetchError

    reporter = config.pluginmanager.get_plugin("terminalreporter")
    report = reporter.write_line if reporter is not None else print
    try:
        sync_fixtures(force=bool(config.getoption("--refresh-fixtures")), report=report)
    except FixtureFetchError as ex:
        pytest.exit(f"fixture refresh failed, cached fixtures kept:\n{ex}", returncode=1)


class _CleanPlugin:
    def __init__(self, config: pytest.Config) -> None:
        self._failures: list[str] = []
        self._passed = 0
        self._failed = 0
        # Registered in pytest_configure, just before the session starts.
        # pytest's own start time is private and was renamed in pytest 9.
        self._start = time.perf_counter()
        config.option.verbose = -1

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        if report.when != "call":
            return
        if report.passed:
            self._passed += 1
        elif report.failed:
            self._failed += 1
            self._failures.append(report.nodeid)

    @pytest.hookimpl(tryfirst=True)
    def pytest_terminal_summary(self, terminalreporter: Any, exitstatus: int) -> None:
        elapsed = int(time.perf_counter() - self._start)
        duration = f"{elapsed // 3600:02d}:{(elapsed % 3600) // 60:02d}:{elapsed % 60:02d}"

        for nodeid in self._failures:
            terminalreporter.write_line(f"FAILED  {nodeid}", red=True)
        total = self._passed + self._failed
        color = "green" if not self._failures else "red"
        terminalreporter.write_sep("=", f"{self._passed}/{total} passed in {duration}", **{color: True})
        terminalreporter.stats.clear()
        terminalreporter.summary_stats = lambda: None