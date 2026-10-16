"""HTML for the Layouts card of a converted doc: tabs, structure cards, byte maps and field tables."""
from __future__ import annotations

from html import escape

from .layout_view import FieldView, LayoutView, StructureView
from .markdown_html import LinkMap, render_inline, render_markdown, slug

_STATE_LABEL = {"known": "Known", "unknown": "Unknown", "ref": "Structure"}
_EMPTY_CELL = '<span class="muted">-</span>'


def layouts_card(views: tuple[LayoutView, ...], links: LinkMap) -> str:
    tabs = "".join(_tab(view, index == 0) for index, view in enumerate(views))
    panels = "".join(_panel(view, index == 0, links) for index, view in enumerate(views))
    tab_bar = f'<div class="segmented" role="tablist" aria-label="Layout" id="layoutTabs">{tabs}</div>' if len(views) > 1 else ""
    return (
        '<section class="card" aria-labelledby="layouts"><div class="card-head">'
        f'<h2 id="layouts">Layouts</h2>{tab_bar}</div><div class="card-body">'
        '<div class="legend-row" aria-hidden="true"><span><i class="dot known"></i>Known</span>'
        '<span><i class="dot unknown"></i>Unknown</span><span><i class="dot ref"></i>Structure, counted in its own table</span>'
        f'<span>Hatched: variable size</span></div><div id="layoutPanels">{panels}</div></div></section>'
    )


def _tab(view: LayoutView, is_current: bool) -> str:
    active = ' class="active"' if is_current else ""
    label = "current" if is_current else "older"
    return (
        f'<button type="button" role="tab" id="tab-l{view.number}" aria-controls="panel-l{view.number}" '
        f'data-layout="{view.number}"{active}>Layout {view.number}<span class="seg-sub">{label}</span></button>'
    )


def _panel(view: LayoutView, is_shown: bool, links: LinkMap) -> str:
    intro = f'<div class="layout-intro prose">{render_markdown(view.intro, links)}</div>' if view.intro else ""
    cards = "".join(_structure_card(structure, view.number, is_shown, links) for structure in view.structures)
    hidden = "" if is_shown else " hidden"
    return (
        f'<div class="layout-panel" role="tabpanel" id="panel-l{view.number}" aria-labelledby="tab-l{view.number}" '
        f'data-layout="{view.number}"{hidden}>{intro}{cards}</div>'
    )


def _structure_card(view: StructureView, layout: int, is_current: bool, links: LinkMap) -> str:
    size = view.heading[len(view.structure.name):].strip()
    size_html = f' <span class="struct-size">{escape(size)}</span>' if size else ""
    badge = ""
    if view.origin == "inherited":
        badge = f'<span class="badge">Same as Layout {view.against}</span>'
    elif view.origin == "changed":
        badge = f'<span class="badge changed">Differs from Layout {view.against}</span>'
    head = (
        f'<div class="struct-head"><h3{_heading_id(view, is_current)}>{render_inline(view.structure.name, links)}{size_html}</h3>{badge}'
        f'<span class="struct-cov">{_coverage(view)}</span></div>'
    )
    desc = f'<div class="struct-desc prose">{render_markdown(view.desc, links)}</div>' if view.desc else ""
    extra = f'<div class="struct-extra prose">{render_markdown(view.extra, links)}</div>' if view.extra else ""
    readout = '<div class="readout" aria-live="polite">Point at a byte or a row to see its field.</div>'
    body = desc + readout + _byte_map(view.fields, layout) + _field_table(view.fields, layout, links) + extra
    return f'<article class="struct" id="{structure_id(layout, view.structure.name)}" data-struct>{head}{body}</article>'


def _heading_id(view: StructureView, is_current: bool) -> str:
    """The id GitHub gives the structure heading, on the current layout only, so `#row-24-bytes` links work."""
    return f' id="{slug(view.heading)}"' if is_current and view.origin == "own" else ""


def structure_id(layout: int, name: str) -> str:
    return f"l{layout}-{slug(name)}"


def _coverage(view: StructureView) -> str:
    parts = [
        f'<span><i class="dot known"></i>{view.known} B known</span>',
        f'<span><i class="dot unknown"></i>{view.unknown} B unknown</span>',
    ]
    if view.variable:
        parts.append(f"<span>+ {escape(', '.join(field.field.name for field in view.variable))}</span>")
    return "".join(parts)


def _byte_map(fields: tuple[FieldView, ...], layout: int) -> str:
    """One cell per byte while offsets are absolute; a variable field is one wide cell."""
    cells: list[str] = []
    is_absolute = True
    position = 0
    for index, view in enumerate(fields):
        if view.size is None:
            is_absolute = False
            label = f"{escape(view.field.name)} · {escape(view.field.type_text)}"
            if view.ref:
                cells.append(f'<a class="b var {view.state} start end" data-f="{index}" href="#{structure_id(layout, view.ref)}">{label}</a>')
            else:
                cells.append(f'<span class="b var {view.state} start end" data-f="{index}">{label}</span>')
            continue
        for k in range(view.size):
            edges = (" start" if k == 0 else "") + (" end" if k == view.size - 1 else "")
            text = f"{position + k:02X}" if is_absolute else ""
            cells.append(f'<span class="b {view.state}{edges}" data-f="{index}">{text}</span>')
        position += view.size
    return f'<div class="bytemap" aria-hidden="true">{"".join(cells)}</div>'


def _field_table(fields: tuple[FieldView, ...], layout: int, links: LinkMap) -> str:
    extra_headers = [header for header, _ in fields[0].field.extra] if fields else []
    head = "<tr><th>Offset</th><th>Type</th><th>Field</th>"
    head += "".join(f"<th>{render_inline(header, links)}</th>" for header in extra_headers) + "<th>Notes</th></tr>"
    rows = "".join(_field_row(index, view, layout, links) for index, view in enumerate(fields))
    return f'<div class="table-wrap"><table class="data-table"><thead>{head}</thead><tbody>{rows}</tbody></table></div>'


def _field_row(index: int, view: FieldView, layout: int, links: LinkMap) -> str:
    field = view.field
    type_html = escape(field.type_text)
    if view.ref:
        type_html = f'<a href="#{structure_id(layout, view.ref)}">{type_html}</a>'
    extra = "".join(f"<td>{render_inline(cell, links) if cell else _EMPTY_CELL}</td>" for _, cell in field.extra)
    return (
        f'<tr data-f="{index}"><td class="mono muted">{escape(field.offset.strip("`"))}</td><td class="mono">{type_html}</td>'
        f'<td><span class="field-name" title="{_STATE_LABEL[view.state]}"><i class="dot {view.state}"></i>{escape(field.name)}</span></td>'
        f'{extra}<td class="notes">{render_inline(field.notes, links)}</td></tr>'
    )
