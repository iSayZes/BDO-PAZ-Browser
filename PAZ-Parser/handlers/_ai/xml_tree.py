"""A forgiving XML reader for client AI scripts (`.ai`).

Many `.ai` files fail a strict XML parser even after escaping `<` in
attribute values (counts in docs/file-formats/aiscript_ai.md). This reader takes them
as written:

- A quoted attribute value is read whole, so `cmp="<="` and `expr="a>0&&b"` work.
- `--` inside a comment is text (`<!-- 비전투 상태 ------ -->`).
- Tag names match without case: `</findTarget>` closes `<findtarget>`.
- An end tag closes the nearest open element with its name and every element
  inside it; an end tag with no open element of that name (`</change>` for
  `<changeState>`) is skipped.
- A repeated attribute keeps its first value.

How the client itself reads the malformed cases is not known; these are the
browser's rules.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

_TOKEN = re.compile(
    r"<!--(?P<comment>.*?)(?:-->|\Z)"
    r"|<!\[CDATA\[.*?(?:\]\]>|\Z)"
    r"|<[?!].*?(?:>|\Z)"
    r"|<(?P<close>/?)(?P<tag>[A-Za-z_:][\w.:-]*)"
    r"(?P<attrs>(?:[^>\"']|\"[^\"]*\"|'[^']*')*)>",
    re.S,
)
_ATTR = re.compile(r"([^\s=/>\"']+)\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))")
_SPACE = re.compile(r"\s+")


@dataclass(frozen=True)
class XmlNode:
    tag: str
    # Attribute names as written, first value of a repeated name.
    attrs: dict[str, str]
    children: tuple[XmlNode, ...] = ()
    # Comments between the previous sibling (or the parent's start tag) and
    # this element, whitespace collapsed. A comment on the line where the
    # previous sibling ends is that sibling's, and is left out.
    comments: tuple[str, ...] = ()

    @property
    def name(self) -> str:
        """The tag in lower case, for comparing."""
        return self.tag.lower()

    def attr(self, name: str, default: str = "") -> str:
        """The value of attribute `name`, matched without case."""
        wanted = name.lower()
        return next((value for key, value in self.attrs.items() if key.lower() == wanted), default)

    def has_attr(self, name: str) -> bool:
        wanted = name.lower()
        return any(key.lower() == wanted for key in self.attrs)


@dataclass
class _OpenElement:
    """An element whose end tag has not been read yet."""

    tag: str
    attrs: dict[str, str]
    comments: tuple[str, ...]
    children: list[XmlNode] = field(default_factory=list)
    pending_comments: list[str] = field(default_factory=list)
    # Where the last child ended; a comment after it on the same line is the child's.
    last_child_end: int | None = None

    def close(self) -> XmlNode:
        return XmlNode(self.tag, self.attrs, tuple(self.children), self.comments)


def parse_attrs(text: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for match in _ATTR.finditer(text):
        name = match.group(1)
        value = next(group for group in match.groups()[1:] if group is not None)
        attrs.setdefault(name, value)
    return attrs


def parse_xml(text: str) -> XmlNode:
    """A document element holding every top-level element of `text`.

    Its tag is `#document`; the file's own root (`<root>`) is its child.
    Never raises: text that is not markup is skipped.
    """
    stack = [_OpenElement("#document", {}, ())]
    for match in _TOKEN.finditer(text):
        parent = stack[-1]
        if match.group("comment") is not None:
            _add_comment(parent, text, match)
        elif match.group("tag") is None:
            continue  # CDATA, <?xml ?>, <!DOCTYPE>
        elif match.group("close"):
            _close(stack, match.group("tag").lower(), match.end())
        else:
            _open(stack, match)
    while len(stack) > 1:
        _close_top(stack, len(text))
    return stack[0].close()


def _add_comment(parent: _OpenElement, text: str, match: re.Match[str]) -> None:
    is_trailing = parent.last_child_end is not None and "\n" not in text[parent.last_child_end:match.start()]
    comment = _SPACE.sub(" ", match.group("comment")).strip()
    if comment and not is_trailing:
        parent.pending_comments.append(comment)


def _open(stack: list[_OpenElement], match: re.Match[str]) -> None:
    parent = stack[-1]
    raw_attrs = match.group("attrs")
    is_empty = raw_attrs.rstrip().endswith("/")
    element = _OpenElement(match.group("tag"), parse_attrs(raw_attrs), tuple(parent.pending_comments))
    parent.pending_comments.clear()
    if is_empty:
        parent.children.append(element.close())
        parent.last_child_end = match.end()
    else:
        stack.append(element)


def _close(stack: list[_OpenElement], name: str, end: int) -> None:
    depth = next((i for i in range(len(stack) - 1, 0, -1) if stack[i].tag.lower() == name), None)
    if depth is None:
        return
    while len(stack) > depth:
        _close_top(stack, end)


def _close_top(stack: list[_OpenElement], end: int) -> None:
    node = stack.pop().close()
    parent = stack[-1]
    parent.children.append(node)
    parent.last_child_end = end
