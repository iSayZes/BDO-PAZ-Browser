from __future__ import annotations

from dataclasses import replace
import os
import sys
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


@pytest.fixture(scope="session", autouse=True)
def load_handlers():
    import bdo_preview

    return bdo_preview


def pytest_collection_finish(session: pytest.Session) -> None:
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

        result = run_case(replace(case, tests=[]))
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

def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    items.sort(key=lambda item: (item.path.name if item.path else "", item.name))
    for item in items:
        item._nodeid = item.name


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--clean",
        action="store_true",
        default=False,
        help="Show only failed tests and a pass/total summary",
    )


def pytest_configure(config: pytest.Config) -> None:
    if config.getoption("--clean", default=False):
        config.pluginmanager.register(_CleanPlugin(config), "clean_plugin")


class _CleanPlugin:
    def __init__(self, config: pytest.Config) -> None:
        self._failures: list[str] = []
        self._passed = 0
        self._failed = 0
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
        import time

        elapsed = int(time.time() - terminalreporter._sessionstarttime)
        duration = f"{elapsed // 3600:02d}:{(elapsed % 3600) // 60:02d}:{elapsed % 60:02d}"

        for nodeid in self._failures:
            terminalreporter.write_line(f"FAILED  {nodeid}", red=True)
        total = self._passed + self._failed
        color = "green" if not self._failures else "red"
        terminalreporter.write_sep("=", f"{self._passed}/{total} passed in {duration}", **{color: True})
        terminalreporter.stats.clear()
        terminalreporter.summary_stats = lambda: None