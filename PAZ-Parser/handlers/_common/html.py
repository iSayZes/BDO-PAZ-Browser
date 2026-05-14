from __future__ import annotations

import html as _html


def e(value: object) -> str:
    return _html.escape(str(value))


def color_cell(colors: list[str]) -> str:
    if not colors:
        return "—"

    parts: list[str] = []

    for color in colors:
        escaped_color = e(color)
        parts.append(
            f'<span class="color-swatch" style="background:#{escaped_color}"></span>'
            f'#{escaped_color}'
        )

    return " ".join(parts)


def icon_cell(path: object, image_src: str | None = None) -> str:
    icon_path = str(path).strip()
    if not icon_path:
        return "-"

    escaped_path = e(icon_path)
    thumb = '<span class="icon-cell-thumb icon-cell-placeholder" aria-hidden="true"></span>'
    if image_src:
        thumb = f'<img class="icon-cell-thumb" src="{e(image_src)}" alt="" loading="lazy">'

    return (
        f'<span class="icon-cell" title="{escaped_path}" data-icon-path="{escaped_path}">'
        f'{thumb}'
        f'<span class="icon-cell-path">{escaped_path}</span>'
        f'</span>'
    )


def debug_cell(fields: dict[str, int], highlight_offset: int) -> str:
    parts: list[str] = []

    for name, value in fields.items():
        offset = int(name.split("_")[1], 16)
        css_class = "debug-field debug-field-hit" if offset == highlight_offset else "debug-field"
        parts.append(f'<span class="{css_class}">{e(name)}={e(value)}</span>')

    return " ".join(parts)


def table(meta: str, headers: list[tuple[str, str, str]], rows: list[list]) -> str:
    head = "".join(
        f'<th class="{css_class} sortable" {extra_attrs}>{label}</th>'
        for label, css_class, extra_attrs in headers
    )

    body = "".join(
        "<tr>"
        + "".join(
            f'<td class="{headers[index][1]}">{cell}</td>'
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
