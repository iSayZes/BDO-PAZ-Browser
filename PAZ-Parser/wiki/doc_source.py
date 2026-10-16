"""A format doc split into the parts the wiki pages show."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from format_docs import is_converted
from format_docs.markdown import numbered_lines, sections

_TITLE = re.compile(r"^# +(?P<name>.+?)(?: Format)? *$")
_OPEN_QUESTIONS = "Open Questions"
_IN_GAME_CHECKS = "In-Game Checks"


@dataclass(frozen=True)
class DocSection:
    """A `##` section: its title and its markdown without the heading line."""

    title: str
    markdown: str


@dataclass(frozen=True)
class DocSource:
    path: Path
    text: str
    name: str
    sections: tuple[DocSection, ...]
    is_converted: bool

    @property
    def page(self) -> str:
        """The file name of this doc's wiki page."""
        return f"{self.path.stem}.html"

    def section(self, title: str) -> DocSection | None:
        return next((section for section in self.sections if section.title == title), None)

    @property
    def open_questions(self) -> int:
        return _subheading_count(self.section(_OPEN_QUESTIONS))

    @property
    def in_game_checks(self) -> int:
        return _subheading_count(self.section(_IN_GAME_CHECKS))


def read_doc(path: Path) -> DocSource:
    text = path.read_text(encoding="utf-8")
    raw = text.splitlines()
    numbered = numbered_lines(text)
    title_line = next((line for _, line in numbered if line.startswith("# ")), path.stem)
    match = _TITLE.match(title_line)
    name = match.group("name").replace("`", "") if match else path.stem
    doc_sections = tuple(
        DocSection(section.title, "\n".join(raw[number - 1] for number, _ in section.body).strip("\n"))
        for section in sections(numbered, 2)
    )
    return DocSource(path, text, name, doc_sections, is_converted(text))


def first_sentence(markdown: str) -> str:
    """The first sentence of a markdown paragraph, for a doc with no index description."""
    paragraph = " ".join(line.strip() for line in markdown.strip().split("\n\n")[0].splitlines())
    match = re.match(r"(.+?\.)(?:\s|$)", paragraph)
    return match.group(1) if match else paragraph


def _subheading_count(section: DocSection | None) -> int:
    if section is None:
        return 0
    lines = numbered_lines(section.markdown)
    return sum(1 for _, line in lines if line.startswith("### "))
