"""HTML for the markdown the format docs use.

Covers headings, paragraphs, nested lists, tables, fenced code, block quotes,
code spans, links and bold text; HTML comments are dropped. Links go through
a `LinkMap`, so a link to another format doc points at its wiki page.
"""
from __future__ import annotations

import html
import re
from collections.abc import Callable

from format_docs.markdown import split_row

LinkMap = Callable[[str], str]

_HEADING = re.compile(r"^(#{1,6}) +(.*?) *$")
_LIST_ITEM = re.compile(r"^( *)(?:[-*]|\d+\.) +(.*)$")
_TABLE_SEPARATOR = re.compile(r"^\|(?: *:?-+:? *\|)+$")
_INLINE = re.compile(r"``(?P<code2>.+?)``|`(?P<code>[^`]+)`|\[(?P<text>(?:[^\]`]|`[^`]*`)+)\]\((?P<url>[^)\s]+)\)|\*\*(?P<bold>.+?)\*\*")
_FENCE = "```"


def slug(text: str) -> str:
    """The id GitHub gives a heading, so a doc's `#section` links work in the wiki too."""
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def render_inline(text: str, links: LinkMap) -> str:
    """One line of markdown as HTML."""
    parts: list[str] = []
    position = 0
    for match in _INLINE.finditer(text):
        parts.append(html.escape(text[position : match.start()], quote=False))
        parts.append(_inline_token(match, links))
        position = match.end()
    parts.append(html.escape(text[position:], quote=False))
    return "".join(parts)


def render_markdown(text: str, links: LinkMap, heading_offset: int = 0) -> str:
    """A markdown block as HTML; `heading_offset` moves every heading down that many levels."""
    lines = _without_comments(text).splitlines()
    out: list[str] = []
    index = 0
    while index < len(lines):
        index = _render_block(lines, index, out, links, heading_offset)
    return "\n".join(out)


def _render_block(lines: list[str], index: int, out: list[str], links: LinkMap, heading_offset: int) -> int:
    """Renders the block that starts at `index` and returns the index after it."""
    line = lines[index]
    if not line.strip():
        return index + 1
    if line.lstrip().startswith(_FENCE):
        return _code_block(lines, index, out)
    heading = _HEADING.match(line)
    if heading:
        level = min(6, len(heading.group(1)) + heading_offset)
        title = heading.group(2)
        out.append(f'<h{level} id="{slug(title)}">{render_inline(title, links)}</h{level}>')
        return index + 1
    if line.startswith("|") and index + 1 < len(lines) and _TABLE_SEPARATOR.match(lines[index + 1].strip()):
        return _table(lines, index, out, links)
    if _LIST_ITEM.match(line):
        return _list(lines, index, out, links)
    if line.startswith(">"):
        return _quote(lines, index, out, links)
    return _paragraph(lines, index, out, links)


def _code_block(lines: list[str], index: int, out: list[str]) -> int:
    end = index + 1
    while end < len(lines) and not lines[end].lstrip().startswith(_FENCE):
        end += 1
    code = html.escape("\n".join(lines[index + 1 : end]), quote=False)
    out.append(f"<pre><code>{code}</code></pre>")
    return end + 1


def _table(lines: list[str], index: int, out: list[str], links: LinkMap) -> int:
    end = index + 2
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    header = "".join(f"<th>{render_inline(cell, links)}</th>" for cell in split_row(lines[index]))
    rows = "".join(
        "<tr>" + "".join(f"<td>{render_inline(cell, links)}</td>" for cell in split_row(row)) + "</tr>"
        for row in lines[index + 2 : end]
    )
    out.append(f'<div class="table-wrap"><table class="data-table"><thead><tr>{header}</tr></thead><tbody>{rows}</tbody></table></div>')
    return end


def _list(lines: list[str], index: int, out: list[str], links: LinkMap) -> int:
    """A list and the lists nested in it, by indent; indented lines continue the item above."""
    items: list[tuple[int, str, bool]] = []
    end = index
    while end < len(lines) and lines[end].strip():
        item = _LIST_ITEM.match(lines[end])
        if item:
            is_ordered = item.group(0).lstrip()[0].isdigit()
            items.append((len(item.group(1)), item.group(2), is_ordered))
        elif items and lines[end].startswith(" "):
            indent, text, is_ordered = items[-1]
            items[-1] = (indent, f"{text} {lines[end].strip()}", is_ordered)
        else:
            break
        end += 1
    out.append(_list_html(items, links))
    return end


def _list_html(items: list[tuple[int, str, bool]], links: LinkMap) -> str:
    if not items:
        return ""
    base, tag = items[0][0], "ol" if items[0][2] else "ul"
    parts: list[str] = []
    index = 0
    while index < len(items):
        _, text, _ = items[index]
        nested_end = index + 1
        while nested_end < len(items) and items[nested_end][0] > base:
            nested_end += 1
        parts.append(f"<li>{render_inline(text, links)}{_list_html(items[index + 1 : nested_end], links)}</li>")
        index = nested_end
    return f"<{tag}>{''.join(parts)}</{tag}>"


def _quote(lines: list[str], index: int, out: list[str], links: LinkMap) -> int:
    end = index
    while end < len(lines) and lines[end].startswith(">"):
        end += 1
    inner = "\n".join(line[1:].lstrip() for line in lines[index:end])
    out.append(f"<blockquote>{render_markdown(inner, links)}</blockquote>")
    return end


def _paragraph(lines: list[str], index: int, out: list[str], links: LinkMap) -> int:
    end = index
    while end < len(lines) and lines[end].strip() and not _starts_block(lines, end):
        end += 1
    end = max(end, index + 1)
    text = " ".join(line.strip() for line in lines[index:end])
    out.append(f"<p>{render_inline(text, links)}</p>")
    return end


def _starts_block(lines: list[str], index: int) -> bool:
    line = lines[index]
    return bool(
        _HEADING.match(line) or _LIST_ITEM.match(line) or line.startswith(("|", ">")) or line.lstrip().startswith(_FENCE)
    )


def _inline_token(match: re.Match[str], links: LinkMap) -> str:
    code = match.group("code2") or match.group("code")
    if code is not None:
        return f"<code>{html.escape(code.strip(), quote=False)}</code>"
    if match.group("url") is not None:
        url = html.escape(links(match.group("url")))
        return f'<a href="{url}">{render_inline(match.group("text"), links)}</a>'
    return f"<b>{render_inline(match.group('bold'), links)}</b>"


def _without_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
