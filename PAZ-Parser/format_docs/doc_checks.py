"""Checks on a whole doc: section order, layouts and the Versions markers."""
from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from pathlib import Path

from .markdown import numbered_lines, sections
from .model import Layout, Problem, Section, Structure
from .names import OFFSET_FIELD, SIZE_FIELD
from .reader import FILE_LAYOUT, layout_number, read_layout
from .structure_checks import StructureSizes, check_structure
from .type_grammar import parse_type

VERSIONS_BEGIN = "<!-- versions:begin"
VERSIONS_END = "<!-- versions:end -->"
_DROPPED_SECTIONS = ("Suggested UI Layout",)
# A line that opens with this sentence shares the whole layout of the linked doc.
_SHARED_LAYOUT = re.compile(r"^Same layout as \[`[^`]+`\]\((?P<doc>[a-z0-9_]+\.md)\)")


def is_converted(text: str) -> bool:
    """True for a doc in the layout format, the docs the checks run on: its own layouts, or a shared one."""
    return bool(_own_layouts(text)[0]) or shared_layout_doc(text) is not None


def shared_layout_doc(text: str) -> str | None:
    """The file name of the doc whose layouts this doc shares, from its `Same layout as [...](x.md)` line."""
    link = _shared_layout_link(text)
    return link[1] if link else None


def read_layouts(text: str, folder: Path | None = None) -> tuple[tuple[Layout, ...], tuple[Problem, ...]]:
    """The `## Layout N` sections of a doc, newest first as written, and the problems in them.

    A doc with no layouts of its own that shares another doc's gets that doc's layouts when `folder`
    holds it; the problems are then the other doc's, which its own check reports.
    """
    layouts, problems = _own_layouts(text)
    linked = shared_layout_doc(text)
    if layouts or linked is None or folder is None or not (folder / linked).is_file():
        return layouts, problems
    return _own_layouts((folder / linked).read_text(encoding="utf-8"))


def _own_layouts(text: str) -> tuple[tuple[Layout, ...], tuple[Problem, ...]]:
    layouts: list[Layout] = []
    problems: list[Problem] = []
    for section in sections(numbered_lines(text), 2):
        number = layout_number(section)
        if number is not None:
            layout, layout_problems = read_layout(section, number)
            layouts.append(layout)
            problems.extend(layout_problems)
    return tuple(layouts), tuple(problems)


def check_doc(text: str, folder: Path | None = None) -> tuple[Problem, ...]:
    """Every problem in a converted doc, in line order; with `folder`, a shared layout's doc is checked to exist."""
    top = sections(numbered_lines(text), 2)
    layouts, layout_problems = _own_layouts(text)
    problems: list[Problem] = list(_section_problems(top, text)) + list(layout_problems)
    problems.extend(_shared_layout_problems(text, bool(layouts), folder))
    problems.extend(_layout_problems(list(layouts)))
    for index, layout in enumerate(layouts):
        sizes = structure_sizes(layouts[: index + 1])
        resolved = resolved_structures(layouts, index)
        for structure in layout.structures:
            problems.extend(check_structure(structure, sizes, _newer_field_names(layouts[:index], structure.name)))
            problems.extend(_offset_file_problems(structure, resolved))
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


def _shared_layout_link(text: str) -> tuple[int, str] | None:
    for number, line in numbered_lines(text):
        match = _SHARED_LAYOUT.match(line)
        if match:
            return number, match.group("doc")
    return None


def _shared_layout_problems(text: str, has_own_layouts: bool, folder: Path | None) -> list[Problem]:
    """A shared layout replaces the doc's own, and the linked doc holds layouts of its own."""
    link = _shared_layout_link(text)
    if link is None:
        return []
    line, linked = link
    if has_own_layouts:
        return [Problem(line, "a doc with its own layouts does not also share another doc's")]
    if folder is None:
        return []
    path = folder / linked
    if not path.is_file():
        return [Problem(line, f"`{linked}` does not exist")]
    if not _own_layouts(path.read_text(encoding="utf-8"))[0]:
        return [Problem(line, f"`{linked}` has no layouts of its own to share")]
    return []


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
        # A structure only this older layout has is fine when one of its own structures uses it.
        used_here = {name for structure in layout.structures for name in _structure_types(structure)}
        problems.extend(
            Problem(structure.line, f"`{structure.name}` is not in a newer layout and nothing in this layout uses it")
            for structure in layout.structures
            if structure.name not in newer_names and structure.name not in used_here and not structure.is_top_level
        )
    return problems


def _newer_field_names(newer: Sequence[Layout], name: str) -> frozenset[str]:
    """The field names structure `name` has in the newer layouts."""
    return frozenset(field.name for layout in newer if (found := layout.find(name)) for field in found.fields)


def _structure_types(structure: Structure) -> tuple[str, ...]:
    """The structure names the Type cells of `structure` use."""
    specs = (parse_type(field.type_text) for field in structure.fields)
    return tuple(spec.name for spec in specs if not isinstance(spec, str) and spec.is_structure)


def resolved_structures(layouts: Sequence[Layout], index: int) -> dict[str, Structure]:
    """Every structure layout `index` uses: its own, the rest from the newer layouts above it."""
    structures: dict[str, Structure] = {}
    for layout in layouts[: index + 1]:
        structures.update((structure.name, structure) for structure in layout.structures)
    return structures


def _offset_file_problems(structure: Structure, resolved: Mapping[str, Structure]) -> list[Problem]:
    """A structure sized by an offset file needs that file's table and a row with one offset and one size field."""
    external = structure.size.external if structure.size else None
    if external is None:
        return []
    table = resolved.get(f"`{external}`")
    if table is None:
        return [Problem(structure.line, f"`{structure.name}` is sized by `{external}`, which has no ``### `{external}` `` table")]
    for field in table.fields:
        spec = parse_type(field.type_text)
        row = resolved.get(spec.name) if not isinstance(spec, str) and spec.is_structure else None
        if row is None:
            continue
        names = [row_field.name for row_field in row.fields]
        if sum(map(bool, map(OFFSET_FIELD.match, names))) == 1 and sum(map(bool, map(SIZE_FIELD.match, names))) == 1:
            return []
    return [Problem(structure.line, f"no row of `{external}` holds one `offset` or `*_offset` field and one `size` or `*_size` field")]


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
