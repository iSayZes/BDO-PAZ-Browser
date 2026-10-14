from __future__ import annotations

import html as _html
import re
from collections.abc import Sequence
from typing import NamedTuple, TypeVar

from ui_text import ui_text

T = TypeVar("T")

# Hidden entries the `... (+N)` of a cut list names on hover; past this it counts.
MORE_TOOLTIP_ITEMS = 40


class Column(NamedTuple):
    """One parsed-table column.

    ``sort_key`` names the raw record field the server sorts this column by
    (``duration_ms``, not the rendered ``1h 30m``). Columns without one render
    a plain, non-clickable header.
    """

    label: str
    css_class: str = ""
    extra_attrs: str = ""
    sort_key: str | None = None


def e(value: object) -> str:
    return _html.escape(str(value))


def truncate(text: str, max_len: int) -> str:
    """`text` cut to `max_len` characters plus an ellipsis, for long text cells."""
    return text if len(text) <= max_len else text[:max_len] + "…"


def hidden_slice(values: Sequence[T], max_items: int) -> Sequence[T]:
    """The hidden values a `more_marker` lists on hover, when a cell shows `max_items`.

    For callers that turn each value into a name: only these few need one.
    """
    return values[max_items : max_items + MORE_TOOLTIP_ITEMS]


def more_marker(hidden_count: int, hidden_names: Sequence[str]) -> str:
    """The `... (+N)` that ends a cut list; hovering it lists the hidden entries.

    `hidden_names` are plain text, the first hidden entries in order
    (`hidden_slice`). Past `MORE_TOOLTIP_ITEMS` the hover only counts the rest.
    """
    names = list(hidden_names[:MORE_TOOLTIP_ITEMS])
    rest = hidden_count - len(names)
    if rest > 0:
        names.append(ui_text("table.moreHidden", count=f"{rest:,}"))
    return f'<span class="list-more" title="{e(chr(10).join(names))}">... (+{hidden_count})</span>'


def html_list_cell(
    shown_html: Sequence[str],
    hidden_count: int = 0,
    hidden_names: Sequence[str] = (),
    separator: str = ", ",
) -> str:
    """Join entries that are already safe HTML, then a `more_marker` for the hidden ones."""
    shown = separator.join(shown_html)
    if hidden_count <= 0:
        return shown
    return f"{shown}{separator}{more_marker(hidden_count, hidden_names)}"


def text_list_cell(values: Sequence[object], max_items: int, separator: str = ", ") -> str:
    """The first `max_items` values as escaped text and a hoverable count of the rest, or ''."""
    texts = [str(value) for value in values]
    return html_list_cell(
        [e(text) for text in texts[:max_items]],
        len(texts) - max_items,
        hidden_slice(texts, max_items),
        separator,
    )


def record_link(text: str, path: str, field: str, value: object, css_class: str = "") -> str:
    """A button that opens the table at PAZ `path` on the first record whose `field` reads `value`.

    `_openRecord()` in ui/js/features/preview-views.js handles the click.
    """
    return (
        f'<button type="button" class="{e(css_class)}" data-action="open-record" data-path="{e(path)}" '
        f'data-field="{e(field)}" data-value="{e(value)}">{e(text)}</button>'
    )


def flag_cell(is_set: bool) -> str:
    """A yes/no cell: a green check mark or a red cross."""
    return '<span class="flag-yes">✓</span>' if is_set else '<span class="flag-no">✗</span>'


# The swatch an icon cell shows until the GUI (ui/js/features/table.js) or
# `browser.py --render` swaps in the image.
_ICON_PLACEHOLDER = '<span class="icon-cell-thumb icon-cell-placeholder" aria-hidden="true"></span>'


def _icon_thumb(image_src: str | None) -> str:
    """The loaded image, or the placeholder swatch without `image_src`."""
    if not image_src:
        return _ICON_PLACEHOLDER
    return f'<img class="icon-cell-thumb" src="{e(image_src)}" alt="" loading="lazy">'


# An `icon_cell` still waiting for its image; group 1 is the escaped path.
PENDING_ICON_CELL_RE = re.compile(
    r'<span class="icon-cell" title="([^"]*)" data-icon-path="\1">'
    + re.escape(_ICON_PLACEHOLDER)
    + r'<span class="icon-cell-path">\1</span></span>'
)


def icon_cell(path: object, image_src: str | None = None) -> str:
    icon_path = str(path).strip()
    if not icon_path:
        return "-"

    escaped_path = e(icon_path)
    return (
        f'<span class="icon-cell" title="{escaped_path}" data-icon-path="{escaped_path}">'
        f'{_icon_thumb(image_src)}'
        f'<span class="icon-cell-path">{escaped_path}</span>'
        f'</span>'
    )


# A sprite cell loads nothing: the sheet is shared by many rows and the sprite
# only shows in the icon popup a click opens (ui/js/features/icon-preview.js).
_SPRITE_PLACEHOLDER = '<span class="icon-cell-thumb sprite-cell-placeholder" aria-hidden="true"></span>'


def sprite_icon_cell(path: object, region: Sequence[int] | None) -> str:
    """An icon that is the (x1, y1, x2, y2) region of a sprite sheet; a dash without one."""
    sheet = str(path).strip()
    if not sheet or region is None or len(region) != 4:
        return "-"

    x1, y1, x2, y2 = (int(v) for v in region)
    escaped_sheet = e(sheet)
    title = e(f"{sheet} ({x1}, {y1}) to ({x2}, {y2})")
    return (
        f'<span class="icon-cell sprite-cell" title="{title}" data-sprite-path="{escaped_sheet}" '
        f'data-sprite-region="{x1},{y1},{x2},{y2}">'
        f'{_SPRITE_PLACEHOLDER}'
        f'<span class="icon-cell-path">{escaped_sheet}</span>'
        f'</span>'
    )


# `(icon_path, label)` of one entry in an icon list cell.
IconEntry = tuple[str, str]

_ICON_LABEL_CLASSES = "icon-cell icon-label-cell"

# The head of an `icon_label_cell` still waiting for its image, up to its
# swatch; the label after it can hold markup (game text colours) and is left
# alone, as the GUI (ui/js/features/table.js) leaves it. Group 1 is the
# escaped tooltip (the path unless the caller gave one), group 2 the escaped
# path.
PENDING_ICON_LABEL_RE = re.compile(
    rf'<span class="{_ICON_LABEL_CLASSES}" title="([^"]*)" data-icon-path="([^"]*)">'
    + re.escape(_ICON_PLACEHOLDER)
)


def _icon_label_open(icon_path: str, tooltip: str | None, is_missing: bool = False) -> str:
    classes = f"{_ICON_LABEL_CLASSES} icon-cell-missing" if is_missing else _ICON_LABEL_CLASSES
    return f'<span class="{classes}" title="{e(tooltip or icon_path)}" data-icon-path="{e(icon_path)}">'


def resolved_icon_label_head(path: str, tooltip: str | None, image_src: str | None) -> str:
    """What a `PENDING_ICON_LABEL_RE` head becomes once its icon is looked up.

    With `image_src`, the image; without, the head marked missing and no
    swatch, as the GUI does for an icon the client does not ship.
    """
    if image_src:
        return _icon_label_open(path, tooltip) + _icon_thumb(image_src)
    return _icon_label_open(path, tooltip, is_missing=True)


def icon_label_cell(
    path: object,
    label: str,
    image_src: str | None = None,
    tooltip: str | None = None,
) -> str:
    """An icon with a label after it instead of its path; the label alone without a path.

    The hover text is `tooltip`, else the icon path. The GUI drops the swatch
    of an icon the client does not ship and keeps the label.
    """
    return icon_html_label_cell(path, e(label), image_src, tooltip)


def icon_html_label_cell(
    path: object,
    label_html: str,
    image_src: str | None = None,
    tooltip: str | None = None,
) -> str:
    """`icon_label_cell` with a label that is already safe HTML, such as `pa_html()` text."""
    icon_path = str(path).strip()
    if not icon_path:
        return f'<span title="{e(tooltip)}">{label_html}</span>' if tooltip else label_html

    return (
        f'{_icon_label_open(icon_path, tooltip)}'
        f'{_icon_thumb(image_src)}'
        f'<span class="icon-cell-label">{label_html}</span>'
        f'</span>'
    )


def icon_list_cell(
    entries: Sequence[IconEntry],
    hidden_count: int = 0,
    tooltips: Sequence[str] | None = None,
    hidden_names: Sequence[str] = (),
) -> str:
    """Comma-join `icon_label_cell` entries and count the `hidden_count` not shown.

    The icon form of `text_list_cell()`: the caller slices the entries, so icon
    paths are only looked up for the ones shown. `tooltips`, one per entry,
    replace the icon path as hover text; `hidden_names` (`hidden_slice`) are
    what hovering the count lists.
    """
    escaped = [(path, e(label)) for path, label in entries]
    return icon_html_list_cell(escaped, hidden_count, tooltips, hidden_names)


def icon_html_list_cell(
    entries: Sequence[IconEntry],
    hidden_count: int = 0,
    tooltips: Sequence[str] | None = None,
    hidden_names: Sequence[str] = (),
) -> str:
    """`icon_list_cell` with labels that are already safe HTML, such as `pa_html()` text."""
    hover: Sequence[str | None] = tooltips if tooltips is not None else [None] * len(entries)
    shown = [
        icon_html_label_cell(path, label_html, tooltip=tip)
        for (path, label_html), tip in zip(entries, hover)
    ]
    return html_list_cell(shown, hidden_count, hidden_names)


def missing_icon_cell(path: object) -> str:
    """An icon cell whose file the client does not ship: a dash, path in the tooltip.

    Matches what the GUI turns an unresolved `icon_cell` into.
    """
    escaped_path = e(str(path).strip())
    return (
        f'<span class="icon-cell icon-cell-missing" title="{escaped_path}" '
        f'data-icon-path="{escaped_path}">-</span>'
    )


def debug_cell(fields: dict[str, int], highlight_offset: int) -> str:
    parts: list[str] = []

    for name, value in fields.items():
        offset = int(name.split("_")[1], 16)
        css_class = "debug-field debug-field-hit" if offset == highlight_offset else "debug-field"
        parts.append(f'<span class="{css_class}">{e(name)}={e(value)}</span>')

    return " ".join(parts)


def sort_keys(columns: Sequence[Column]) -> tuple[str, ...]:
    """Record fields the given columns can be sorted by, in column order.

    The order matters: a table opens sorted by the first one (see
    ``PreviewHandler.default_sort``).
    """
    return tuple(dict.fromkeys(column.sort_key for column in columns if column.sort_key))


def header_cell(column: Column) -> str:
    """Render one `<th>`. Only columns with a sort key are clickable."""
    if not column.sort_key:
        return f'<th class="{column.css_class}" {column.extra_attrs}>{column.label}</th>'

    css_class = f"{column.css_class} sortable".strip()
    return (
        f'<th class="{css_class}" data-sort-key="{e(column.sort_key)}" {column.extra_attrs}>'
        f'{column.label}</th>'
    )


def table(
    meta: str,
    headers: Sequence[Column | tuple[str, str, str]],
    rows: list[list],
) -> str:
    """Render a parsed table. Plain ``(label, css_class, extra_attrs)`` tuples
    are accepted as unsortable columns."""
    columns = [header if isinstance(header, Column) else Column(*header) for header in headers]
    head = "".join(header_cell(column) for column in columns)

    body = "".join(
        "<tr>"
        + "".join(
            f'<td class="{columns[index].css_class}">{cell}</td>'
            for index, cell in enumerate(row)
        )
        + "</tr>"
        for row in rows
    )

    return (
        f'<div class="table-meta">{e(meta)}</div>'
        f'<div class="table-wrap">'
        f'<table class="data-table">'
        f'<thead><tr>{head}</tr></thead>'
        f'<tbody>{body}</tbody>'
        f'</table>'
        f'</div>'
    )


def error(text: str) -> str:
    return f'<div class="error">{e(text)}</div>'
