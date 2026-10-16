"""Checks on one structure: types, sizes, offsets and field names."""
from __future__ import annotations

from collections.abc import Mapping

from .model import Field, Problem, Structure
from .names import name_problems
from .offsets import Offset, parse_offset
from .type_grammar import TypeSpec, fixed_part, fixed_size, parse_type, referenced_fields

StructureSizes = Mapping[str, int | None]


def check_structure(structure: Structure, sizes: StructureSizes, newer_names: frozenset[str] = frozenset()) -> tuple[Problem, ...]:
    """Every problem in one structure.

    `sizes` holds the structures its types may name; `newer_names` the field names the same structure has
    in newer layouts, which an older layout's `unknown_after_` and `_dup` names may also point at.
    """
    specs, problems = _parse_types(structure, sizes)
    problems += _name_problems(structure, newer_names)
    problems += _reference_problems(structure, specs)
    problems += _offset_problems(structure, specs, sizes)
    problems += _size_problems(structure, specs, sizes)
    return tuple(problems)


def _parse_types(structure: Structure, sizes: StructureSizes) -> tuple[dict[int, TypeSpec], list[Problem]]:
    specs: dict[int, TypeSpec] = {}
    problems: list[Problem] = []
    for field in structure.fields:
        spec = parse_type(field.type_text)
        if isinstance(spec, str):
            problems.append(Problem(field.line, spec))
        elif spec.is_structure and spec.name not in sizes:
            problems.append(Problem(field.line, f"`{spec.name}` has no `### {spec.name} (...)` heading in this layout or a newer one"))
        else:
            specs[field.line] = spec
            if spec.count is not None and spec.count.kind == "scan" and (not field.name.startswith("unknown_") or not field.notes):
                problems.append(Problem(field.line, "`bytes[scan]` is a field named `unknown_*` with the scan in Notes"))
    return specs, problems


def _name_problems(structure: Structure, newer_names: frozenset[str]) -> list[Problem]:
    names = frozenset(field.name for field in structure.fields) | newer_names
    problems: list[Problem] = []
    seen: set[str] = set()
    for field in structure.fields:
        if field.name in seen:
            problems.append(Problem(field.line, f"`{field.name}` is used twice in `{structure.name}`"))
        seen.add(field.name)
        problems.extend(Problem(field.line, text) for text in name_problems(field, names, structure.is_top_level))
    return problems


def _reference_problems(structure: Structure, specs: Mapping[int, TypeSpec]) -> list[Problem]:
    """Counts and conditions read earlier fields; `size` and `rest` need a size from outside.

    In a top-level table, a field at `EOF-0xNN` is read before the body, so `[..field]` may name it.
    """
    problems: list[Problem] = []
    earlier: set[str] = set()
    from_eof = {field.name for field in structure.fields if structure.is_top_level and field.offset.strip("`").startswith("EOF-")}
    has_outside_size = structure.is_top_level or (structure.size is not None and structure.size.external is not None)
    for field in structure.fields:
        spec = specs.get(field.line)
        if spec is not None:
            problems.extend(
                Problem(field.line, f"`{name}` is not an earlier field of `{structure.name}`")
                for name in referenced_fields(spec)
                if name not in earlier and not (name in from_eof and _is_until(spec, name))
            )
            if not has_outside_size and _needs_outside_size(spec):
                problems.append(Problem(field.line, "`size` and `[rest]` need `size from <offset file>` in the heading"))
        earlier.add(field.name)
    return problems


def _is_until(spec: TypeSpec, name: str) -> bool:
    return spec.count is not None and spec.count.kind == "until" and spec.count.value == name


def _needs_outside_size(spec: TypeSpec) -> bool:
    is_rest = spec.count is not None and spec.count.kind == "rest"
    return is_rest or (spec.condition is not None and spec.condition.field == "size")


def _offset_problems(structure: Structure, specs: Mapping[int, TypeSpec], sizes: StructureSizes) -> list[Problem]:
    """Offsets follow on from the start, from the last variable field, or back from the end."""
    problems: list[Problem] = []
    anchor: str | None = None
    position = 0
    from_end: list[tuple[Field, Offset, int | None]] = []
    for field in structure.fields:
        offset = parse_offset(field.offset)
        if isinstance(offset, str):
            problems.append(Problem(field.line, offset))
            return problems
        spec = specs.get(field.line)
        size = fixed_size(spec, sizes) if spec is not None else None
        if offset.is_from_end:
            from_end.append((field, offset, size))
            continue
        if from_end:
            problems.append(Problem(field.line, "after an `end-` or `EOF-` offset every row counts from the end"))
            return problems
        if (offset.anchor, offset.value) != (anchor, position):
            problems.append(Problem(field.line, f"offset should be `{_format(anchor, position)}`"))
            anchor, position = offset.anchor, offset.value
        anchor, position = (anchor, position + size) if size is not None else (field.name, 0)
    return problems + _end_problems(structure, from_end)


def _end_problems(structure: Structure, rows: list[tuple[Field, Offset, int | None]]) -> list[Problem]:
    problems: list[Problem] = []
    for index, (field, offset, size) in enumerate(rows):
        expected_anchor = "EOF" if structure.is_top_level else "end"
        if offset.anchor != expected_anchor:
            problems.append(Problem(field.line, _END_ANCHOR_ADVICE[expected_anchor]))
        if size is None:
            problems.append(Problem(field.line, "a field counted back from the end needs a fixed size"))
            continue
        next_value = rows[index + 1][1].value if index + 1 < len(rows) else 0
        if offset.value - size != next_value:
            problems.append(Problem(field.line, f"`{offset.anchor}-0x{offset.value:02X}` minus its {size} bytes does not reach the next row"))
    return problems


def _size_problems(structure: Structure, specs: Mapping[int, TypeSpec], sizes: StructureSizes) -> list[Problem]:
    """A fixed heading equals the sum of the fields; a variable heading's number is their fixed part."""
    if structure.size is None or len(specs) != len(structure.fields):
        return []
    fields = [specs[field.line] for field in structure.fields]
    exact = [fixed_size(spec, sizes) for spec in fields]
    stated = structure.size.fixed
    if not structure.size.is_variable:
        if None in exact:
            return [Problem(structure.line, f"`{structure.name}` holds a variable-size field, so its heading says `variable`")]
        total = sum(size for size in exact if size is not None)
        return [] if total == stated else [Problem(structure.line, f"`{structure.name}` states {stated} bytes, its fields add up to {total}")]
    if None not in exact:
        return [Problem(structure.line, f"every field of `{structure.name}` has a fixed size, so its heading gives `(N bytes)`")]
    part = sum(fixed_part(spec, sizes) for spec in fields)
    return [] if part == stated else [Problem(structure.line, f"`{structure.name}` states a fixed part of {stated} bytes, its fields give {part}")]


_END_ANCHOR_ADVICE = {
    "EOF": "a top-level table counts back from the end with `EOF-0xNN`",
    "end": "a structure counts back from its end with `end-0xNN`",
}


def _format(anchor: str | None, position: int) -> str:
    return f"{anchor or ''}+0x{position:02X}"
