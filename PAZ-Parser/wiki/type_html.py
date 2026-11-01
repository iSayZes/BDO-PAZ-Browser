"""Type cells as colored tokens: number and text types, structures, counts, fields, literals and keywords.

The tokens come from `parse_type`, so only text in the Type column grammar of
docs/format-docs.md is colored; wiki.css gives each `tk-` class its color.
"""
from __future__ import annotations

import re
from html import escape

from format_docs.type_grammar import NUMBER_SIZES, Clause, Count, TypeSpec, parse_type

_LITERAL = re.compile(r"^(?:0x[0-9A-Fa-f]+|-?\d+)$")
Token = tuple[str | None, str]


def type_html(text: str, *, allow_structures: bool = True) -> str | None:
    """`text` as token spans, or None when it is not a type (or names a structure and `allow_structures` is off)."""
    spec = parse_type(text)
    if isinstance(spec, str) or (spec.is_structure and not allow_structures):
        return None
    tokens = _tokens(spec)
    # The spans must spell the cell exactly; anything the grammar reads loosely stays plain.
    if "".join(part for _, part in tokens) != text:
        return None
    return "".join(escape(part) if kind is None else f'<span class="tk-{kind}">{escape(part)}</span>' for kind, part in tokens)


def _tokens(spec: TypeSpec) -> list[Token]:
    kind = "struct" if spec.is_structure else "num" if spec.name in NUMBER_SIZES else "text"
    tokens: list[Token] = [(kind, spec.name)]
    if spec.count is not None:
        tokens += [("punct", "["), *_count(spec.count), ("punct", "]")]
    if spec.inner is not None:
        inner = ("lit", str(spec.inner)) if isinstance(spec.inner, int) else ("field", spec.inner)
        tokens += [("punct", "["), inner, ("punct", "]")]
    if spec.condition is not None:
        tokens += [(None, " "), ("kw", "if"), (None, " ")]
        for group_index, group in enumerate(spec.condition.groups):
            if group_index:
                tokens += [(None, " "), ("kw", "or"), (None, " ")]
            for clause_index, clause in enumerate(group):
                if clause_index:
                    tokens += [(None, " "), ("kw", "and"), (None, " ")]
                tokens += _clause(clause)
    return tokens


def _count(count: Count) -> list[Token]:
    if count.kind == "fixed":
        return [("lit", str(count.value))]
    if count.kind in ("rest", "scan"):
        return [("kw", str(count.value))]
    if count.kind == "until":
        target = str(count.value)
        return [("punct", ".."), ("kw", target) if target == "end" else ("field", target)]
    if count.kind == "while":
        return [("kw", "while"), (None, " "), ("field", str(count.value)), (None, " "), ("op", "!="), (None, " "), _value(count.stop or "")]
    if count.kind == "sum":
        return [("kw", "sum"), (None, " "), ("field", str(count.value))]
    return [("field", str(count.value))]


def _clause(clause: Clause) -> list[Token]:
    return [("field", clause.field), (None, " "), ("op", clause.op), (None, " "), _value(clause.value)]


def _value(value: str) -> Token:
    return ("lit", value) if _LITERAL.match(value) else ("str", value)
