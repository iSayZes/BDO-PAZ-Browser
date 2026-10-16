"""Checks on a whole doc: section order, layouts and the Versions markers."""
from __future__ import annotations

from .markdown import numbered_lines, sections
from .model import Layout, Problem, Section
from .reader import FILE_LAYOUT, layout_number, read_layout
from .structure_checks import StructureSizes, check_structure

VERSIONS_BEGIN = "<!-- versions:begin"
VERSIONS_END = "<!-- versions:end -->"
_DROPPED_SECTIONS = ("Suggested UI Layout",)


def is_converted(text: str) -> bool:
    """True for a doc in the layout format, the docs the checks run on."""
    return any(layout_number(section) is not None for section in sections(numbered_lines(text), 2))


def read_layouts(text: str) -> tuple[tuple[Layout, ...], tuple[Problem, ...]]:
    """The `## Layout N` sections of a doc, newest first as written, and the problems in them."""
    layouts: list[Layout] = []
    problems: list[Problem] = []
    for section in sections(numbered_lines(text), 2):
        number = layout_number(section)
        if number is not None:
            layout, layout_problems = read_layout(section, number)
            layouts.append(layout)
            problems.extend(layout_problems)
    return tuple(layouts), tuple(problems)


def check_doc(text: str) -> tuple[Problem, ...]:
    """Every problem in a converted doc, in line order."""
    top = sections(numbered_lines(text), 2)
    layouts, layout_problems = read_layouts(text)
    problems: list[Problem] = list(_section_problems(top, text)) + list(layout_problems)
    problems.extend(_layout_problems(list(layouts)))
    for index, layout in enumerate(layouts):
        sizes = structure_sizes(layouts[: index + 1])
        for structure in layout.structures:
            problems.extend(check_structure(structure, sizes))
    return tuple(sorted(problems, key=lambda problem: problem.line))


def _section_problems(top: tuple[Section, ...], text: str) -> list[Problem]:
    titles = [section.title for section in top]
    first_layout = next((section for section in top if layout_number(section) is not None), None)
    problems: list[Problem] = []
    if "Purpose" not in titles:
        problems.append(Problem(1, "the doc has no `## Purpose`"))
    versions = next((section for section in top if section.title == "Versions"), None)
    if versions is None:
        problems.append(Problem(1, "the doc has no `## Versions` with its two markers"))
    else:
        problems.extend(_versions_problems(versions, text, first_layout))
    problems.extend(
        Problem(section.line, f"`## {section.title}` is no longer part of a format doc")
        for section in top
        if section.title in _DROPPED_SECTIONS
    )
    purpose = next((section for section in top if section.title == "Purpose"), None)
    if purpose is not None and any(not line and _raw_line(text, number).lstrip().startswith("```") for number, line in purpose.body):
        problems.append(Problem(purpose.line, "Purpose holds an example block; the layout tables show every field"))
    return problems


def _versions_problems(versions: Section, text: str, first_layout: Section | None) -> list[Problem]:
    raw = [_raw_line(text, number) for number, _ in versions.body]
    problems: list[Problem] = []
    if not any(line.startswith(VERSIONS_BEGIN) for line in raw) or VERSIONS_END not in raw:
        problems.append(Problem(versions.line, "`## Versions` needs the `versions:begin` and `versions:end` markers"))
    if first_layout is not None and versions.line > first_layout.line:
        problems.append(Problem(versions.line, "`## Versions` goes above the layouts"))
    return problems


def _layout_problems(layouts: list[Layout]) -> list[Problem]:
    """Layouts run N down to 1; the newest has a File Layout, older ones only list known structures."""
    problems: list[Problem] = []
    expected = list(range(len(layouts), 0, -1))
    if [layout.number for layout in layouts] != expected:
        line = layouts[0].line if layouts else 1
        problems.append(Problem(line, f"layouts should be numbered {', '.join(map(str, expected))} from the top"))
    if layouts and layouts[0].find(FILE_LAYOUT) is None:
        problems.append(Problem(layouts[0].line, f"the newest layout needs a `### {FILE_LAYOUT}`"))
    for index, layout in enumerate(layouts[1:], start=1):
        newer_names = {structure.name for newer in layouts[:index] for structure in newer.structures}
        problems.extend(
            Problem(structure.line, f"`{structure.name}` is not in a newer layout; an older layout lists only what changed")
            for structure in layout.structures
            if structure.name not in newer_names
        )
    return problems


def structure_sizes(layouts: tuple[Layout, ...]) -> StructureSizes:
    """The sizes of the structures the last of `layouts` can name: its own, then those of newer layouts."""
    sizes: dict[str, int | None] = {}
    for layout in layouts:
        for structure in layout.structures:
            if structure.size is not None:
                sizes[structure.name] = None if structure.size.is_variable else structure.size.fixed
    return sizes


def _raw_line(text: str, number: int) -> str:
    lines = text.splitlines()
    return lines[number - 1] if 0 < number <= len(lines) else ""
