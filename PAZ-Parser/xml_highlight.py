"""XML syntax colours for the Text view: one HTML string per line.

The scanner reads the whole text, so a comment, tag or attribute value that
spans lines keeps its colour on every line. Client XML is not always
well-formed: `.ai` scripts hold a raw `<` in attribute values (`cmp="<="`)
and `--` inside comments. The scanner never fails; text it cannot read as
markup stays plain.

The classes (`xml-tag`, `xml-attr`, ...) are styled in
ui/css/13-text-hex-views.css from the `--syntax-*` tokens.
"""
from __future__ import annotations

import html as _html
import re
from pathlib import PurePosixPath

# Extensions whose Text view gets XML colours.
XML_EXTENSIONS = frozenset({
    ".xml", ".mxml", ".weathercolortablexml", ".xmp",
    ".ai", ".cl",
    ".svg",
})

_COMMENT = "xml-comment"
_DECL = "xml-decl"
_CDATA = "xml-cdata"
_TAG = "xml-tag"
_ATTR = "xml-attr"
_VALUE = "xml-value"
_PUNCT = "xml-punct"
_ENTITY = "xml-entity"

# Markup that starts with `<`. An unterminated comment, CDATA or declaration
# runs to the end of the text, as a parser would read it.
_MARKUP = re.compile(
    r"(?P<comment><!--.*?(?:-->|\Z))"
    r"|(?P<cdata><!\[CDATA\[.*?(?:\]\]>|\Z))"
    r"|(?P<decl><\?.*?(?:\?>|\Z)|<![A-Za-z].*?(?:>|\Z))"
    r"|(?P<open></?)(?P<name>[A-Za-z_:][\w.:-]*)",
    re.S,
)

# The inside of a tag after its name, up to `>` or `/>`. A quoted value is
# read whole, so a `<` or `>` in it does not end the tag.
_TAG_PART = re.compile(
    r"(?P<space>\s+)"
    r"|(?P<end>/?>)"
    r"|(?P<value>\"[^\"]*(?:\"|\Z)|'[^']*(?:'|\Z))"
    r"|(?P<eq>=)"
    r"|(?P<attr>[^\s=/>\"']+)"
    r"|(?P<other>.)",
    re.S,
)

_ENTITY_REF = re.compile(r"&(?:#\d+|#x[0-9A-Fa-f]+|[A-Za-z][\w.-]*);")

Token = tuple[str | None, str]


def is_xml_path(path: str) -> bool:
    """True when the file at `path` gets XML colours in the Text view."""
    return PurePosixPath(path.replace("\\", "/")).suffix.lower() in XML_EXTENSIONS


def xml_tokens(text: str) -> list[Token]:
    """(class, text) pieces that join back to `text`; class None is plain text."""
    tokens: list[Token] = []
    pos = 0
    while pos < len(text):
        match = _MARKUP.search(text, pos)
        if match is None:
            _add_text(tokens, text[pos:])
            break
        _add_text(tokens, text[pos:match.start()])
        kind = match.lastgroup
        if kind == "name":
            tokens.append((_PUNCT, match.group("open")))
            tokens.append((_TAG, match.group("name")))
            pos = _add_tag_parts(tokens, text, match.end())
            continue
        tokens.append(({"comment": _COMMENT, "cdata": _CDATA}.get(kind or "", _DECL), match.group()))
        pos = match.end()
    return tokens


def _add_text(tokens: list[Token], text: str) -> None:
    pos = 0
    for match in _ENTITY_REF.finditer(text):
        if match.start() > pos:
            tokens.append((None, text[pos:match.start()]))
        tokens.append((_ENTITY, match.group()))
        pos = match.end()
    if pos < len(text):
        tokens.append((None, text[pos:]))


def _add_tag_parts(tokens: list[Token], text: str, pos: int) -> int:
    """Tokens of a tag's attributes and its closing `>`; returns the position after it."""
    classes = {"end": _PUNCT, "value": _VALUE, "eq": _PUNCT, "attr": _ATTR}
    while pos < len(text):
        match = _TAG_PART.match(text, pos)
        if match is None:  # not reached: `other` matches any one character
            break
        kind = match.lastgroup or "other"
        tokens.append((classes.get(kind), match.group()))
        pos = match.end()
        if kind == "end":
            break
    return pos


def highlight_xml_lines(lines: list[str]) -> list[str]:
    """`lines` as escaped HTML with colour spans, one string per line.

    A piece that crosses a line break is closed at the end of the line and
    opened again on the next, so each line is complete HTML on its own.
    """
    if not lines:
        return []
    out: list[str] = []
    current: list[str] = []
    for cls, piece in xml_tokens("\n".join(lines)):
        parts = piece.split("\n")
        for index, part in enumerate(parts):
            if index:
                out.append("".join(current))
                current = []
            if part:
                escaped = _html.escape(part, quote=False)
                current.append(f'<span class="{cls}">{escaped}</span>' if cls else escaped)
    out.append("".join(current))
    return out
