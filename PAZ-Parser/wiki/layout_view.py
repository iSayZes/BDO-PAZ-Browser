"""The layouts of a converted doc as the wiki shows them.

Each field gets its size and state (known, unknown, or a structure counted in
its own table), each structure its known and unknown bytes, and an older
layout takes every structure it does not list from the next newer one.
"""
from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass

from format_docs import read_layouts, structure_sizes
from format_docs.markdown import numbered_lines, sections
from format_docs.model import Field, Layout, Structure
from format_docs.names import UNKNOWN_PREFIX
from format_docs.type_grammar import fixed_size, parse_type

from .doc_source import DocSource

_TABLE_START = "| Offset"


@dataclass(frozen=True)
class FieldView:
    field: Field
    size: int | None
    state: str
    ref: str | None


@dataclass(frozen=True)
class StructureView:
    """A structure in one layout. `origin` is own, changed (differs from `against`) or inherited (from `against`)."""

    structure: Structure
    heading: str
    fields: tuple[FieldView, ...]
    desc: str
    extra: str
    origin: str
    against: int | None

    @property
    def known(self) -> int:
        return sum(view.size or 0 for view in self.fields if view.state == "known")

    @property
    def unknown(self) -> int:
        return sum(view.size or 0 for view in self.fields if view.state == "unknown")

    @property
    def variable(self) -> tuple[FieldView, ...]:
        return tuple(view for view in self.fields if view.size is None)


@dataclass(frozen=True)
class LayoutView:
    number: int
    intro: str
    structures: tuple[StructureView, ...]

    @property
    def known(self) -> int:
        return sum(view.known for view in self.structures)

    @property
    def unknown(self) -> int:
        return sum(view.unknown for view in self.structures)


def layout_views(doc: DocSource) -> tuple[LayoutView, ...]:
    """Every layout of a converted doc, newest first, older ones filled in from newer ones."""
    layouts, _ = read_layouts(doc.text)
    views: list[LayoutView] = []
    for index, layout in enumerate(layouts):
        sizes = structure_sizes(layouts[: index + 1])
        intro, prose = _layout_prose(doc, layout)
        own = {
            structure.name: _structure_view(structure, sizes, prose.get(structure.name, ("", "", structure.name)), "own", None)
            for structure in layout.structures
        }
        if index == 0:
            views.append(LayoutView(layout.number, intro, tuple(own.values())))
            continue
        newer = views[-1]
        merged = tuple(
            _with_origin(own[view.structure.name], "changed", newer.number) if view.structure.name in own
            else _with_origin(view, "inherited", view.against if view.origin == "inherited" else newer.number)
            for view in newer.structures
        )
        views.append(LayoutView(layout.number, intro, merged))
    return tuple(views)


def _structure_view(
    structure: Structure, sizes: Mapping[str, int | None], prose: tuple[str, str, str], origin: str, against: int | None
) -> StructureView:
    fields = tuple(_field_view(field, sizes) for field in structure.fields)
    desc, extra, heading = prose
    return StructureView(structure, heading, fields, desc, extra, origin, against)


def _field_view(field: Field, sizes: Mapping[str, int | None]) -> FieldView:
    spec = parse_type(field.type_text)
    if isinstance(spec, str):
        return FieldView(field, None, _name_state(field.name), None)
    size = fixed_size(spec, sizes)
    if spec.is_structure:
        return FieldView(field, size, "ref", spec.name)
    return FieldView(field, size, _name_state(field.name), None)


def _name_state(name: str) -> str:
    return "unknown" if name.startswith(UNKNOWN_PREFIX) else "known"


def _with_origin(view: StructureView, origin: str, against: int | None) -> StructureView:
    return StructureView(view.structure, view.heading, view.fields, view.desc, view.extra, origin, against)


def _layout_prose(doc: DocSource, layout: Layout) -> tuple[str, dict[str, tuple[str, str, str]]]:
    """The intro of a layout section, and per structure the markdown before and after its table and its heading."""
    section = doc.section(f"Layout {layout.number}")
    if section is None:
        return "", {}
    raw = section.markdown.splitlines()
    numbered = numbered_lines(section.markdown)
    headings = sections(numbered, 3)
    intro_end = headings[0].line - 1 if headings else len(raw)
    prose: dict[str, tuple[str, str, str]] = {}
    for heading in headings:
        body = [raw[number - 1] for number, _ in heading.body]
        start = next((k for k, line in enumerate(body) if line.startswith(_TABLE_START)), len(body))
        end = start
        while end < len(body) and body[end].startswith("|"):
            end += 1
        name = re.sub(r" \(.*\)$", "", heading.title)
        prose[name] = ("\n".join(body[:start]).strip(), "\n".join(body[end:]).strip(), heading.title)
    return "\n".join(raw[:intro_end]).strip(), prose
