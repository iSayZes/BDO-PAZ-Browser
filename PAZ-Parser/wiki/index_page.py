"""The wiki's index page; index.js fills the summary and the table from formats.js."""
from __future__ import annotations

from .page_shell import FORMATS_SCRIPT, STATIC_DIR, page

_BODY = """<main class="page">
  <section class="head">
    <h1>Format docs</h1>
    <p class="lead">Every format the browser documents, with how much of it is known and what is still open. Pick a format to read its layout.</p>
  </section>
  <section class="summary" aria-label="Summary" id="summary"></section>
  <section class="filters" aria-label="Filters">
    <label class="input-box" for="q"><span aria-hidden="true">⌕</span>
      <input id="q" type="search" placeholder="Search names, files and descriptions" autocomplete="off" spellcheck="false"></label>
    <div class="segmented" role="group" aria-label="File type" id="extFilter">
      <button type="button" data-ext="" class="active">All</button>
      <button type="button" data-ext="bss">.bss</button>
      <button type="button" data-ext="dbss">.dbss</button>
      <button type="button" data-ext="other">Other</button>
    </div>
    <button type="button" class="toggle" id="onlyQ" aria-pressed="false"><span class="cnt q" aria-hidden="true">?</span>Has open questions</button>
    <button type="button" class="toggle" id="onlyIg" aria-pressed="false"><span class="cnt ig" aria-hidden="true">⌖</span>Has in-game checks</button>
    <span class="filters-gap"></span>
    <span class="result-count" id="resultCount" aria-live="polite"></span>
  </section>
  <div class="table-wrap">
    <table class="data-table" id="index">
      <thead><tr>
        <th class="sortable col-format" data-sort="name" tabindex="0" aria-sort="ascending">Format</th>
        <th>Description</th>
        <th class="sortable num" data-sort="known" tabindex="0" aria-sort="none">Known</th>
        <th class="sortable num" data-sort="oq" tabindex="0" aria-sort="none">Open questions</th>
        <th class="sortable num" data-sort="ig" tabindex="0" aria-sort="none">In-game checks</th>
      </tr></thead>
      <tbody></tbody>
    </table>
  </div>
  <p class="foot">Built from <code>docs/documented-formats.md</code> and <code>docs/file-formats/</code>. Known counts the bytes of a doc's newest layout in the game files its Versions section names, every record included; a doc without Versions counts its fixed-size fields, each structure once. Each share's tooltip says which.</p>
</main>"""


def index_page() -> str:
    return page(
        "PAZ Format Docs",
        "",
        "index-page",
        _BODY,
        (FORMATS_SCRIPT, f"{STATIC_DIR}/common.js", f"{STATIC_DIR}/index.js"),
    )
