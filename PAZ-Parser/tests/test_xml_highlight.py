"""XML colours in the Text view: token classes, line splits and malformed input."""
from __future__ import annotations

import html
import re

from bdo_models import PazEntry
from bdo_preview import TextHandler
from preview_views import text_lines
from xml_highlight import highlight_xml_lines, is_xml_path, xml_tokens


def _classes(text: str) -> list[tuple[str | None, str]]:
    return [(cls, piece) for cls, piece in xml_tokens(text) if piece.strip()]


def _plain(line_html: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", line_html))


def _entry(path: str, size: int) -> PazEntry:
    return PazEntry("t.paz", path, 0, size, size, 0, 0)


def test_tokens_join_back_to_the_text() -> None:
    text = '<?xml version="1.0"?>\n<root a="1">x &amp; y<!-- c --><![CDATA[<b>]]></root>'
    assert "".join(piece for _, piece in xml_tokens(text)) == text


def test_tag_attribute_value_and_punctuation_classes() -> None:
    assert _classes('<state name="Wait"/>') == [
        ("xml-punct", "<"), ("xml-tag", "state"), ("xml-attr", "name"),
        ("xml-punct", "="), ("xml-value", '"Wait"'), ("xml-punct", "/>"),
    ]
    assert _classes("</state>") == [("xml-punct", "</"), ("xml-tag", "state"), ("xml-punct", ">")]


def test_a_raw_lt_in_an_attribute_value_stays_in_the_value() -> None:
    tokens = _classes('<distance cmp="<=" value="900"/><a/>')
    assert ("xml-value", '"<="') in tokens
    assert ("xml-tag", "a") in tokens


def test_comments_declarations_and_entities() -> None:
    tokens = _classes('<?xml version="1.0"?><!DOCTYPE x><!---- a -- b ---->t&lt;')
    assert tokens == [
        ("xml-decl", '<?xml version="1.0"?>'),
        ("xml-decl", "<!DOCTYPE x>"),
        ("xml-comment", "<!---- a -- b ---->"),
        (None, "t"),
        ("xml-entity", "&lt;"),
    ]


def test_a_lone_lt_in_text_stays_plain() -> None:
    assert _classes("a < b") == [(None, "a < b")]


def test_unterminated_markup_runs_to_the_end_without_failing() -> None:
    assert _classes("<!-- open")[-1] == ("xml-comment", "<!-- open")
    assert _classes('<a b="open')[-1] == ("xml-value", '"open')


def test_a_comment_over_two_lines_is_coloured_on_both() -> None:
    lines = highlight_xml_lines(["<a/><!-- one", "two -->", "<b/>"])

    assert len(lines) == 3
    assert lines[0].endswith('<span class="xml-comment">&lt;!-- one</span>')
    assert lines[1] == '<span class="xml-comment">two --&gt;</span>'
    assert [_plain(line) for line in lines] == ["<a/><!-- one", "two -->", "<b/>"]


def test_empty_lines_are_kept() -> None:
    lines = ["<a>", "", "</a>"]
    assert [_plain(line) for line in highlight_xml_lines(lines)] == lines
    assert highlight_xml_lines([]) == []


def test_xml_family_extensions_are_highlighted() -> None:
    for path in ("ui/a.xml", "character/aiscript/boss/x.ai", "character/pcaiscript/y.cl", "Z.WEATHERCOLORTABLEXML"):
        assert is_xml_path(path)
    assert not is_xml_path("a.txt")
    assert not is_xml_path("a.lua")


def test_text_handler_colours_xml_and_leaves_other_text_plain() -> None:
    data = b'<root a="1"/>\r\n'

    xml_html = TextHandler().render(data, _entry("ui/x.xml", len(data)), {})
    txt_html = TextHandler().render(data, _entry("ui/x.txt", len(data)), {})

    assert 'class="xml-tag"' in xml_html
    assert "xml-" not in txt_html
    assert xml_html.count('<div class="text-line">') == len(text_lines(data.decode()))
